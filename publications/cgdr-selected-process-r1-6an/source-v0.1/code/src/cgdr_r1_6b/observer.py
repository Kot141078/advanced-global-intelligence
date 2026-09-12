from __future__ import annotations

from dataclasses import dataclass
from copy import deepcopy
import re
from typing import Any, Callable

from .common import canonical_hash
from .signing import verify
from .state_transfer import MATERIAL_FIELDS, material_projection

ALL_REQUIREMENTS = [f"R{i:02d}" for i in range(1, 37)]


@dataclass(frozen=True)
class RuleResult:
    value: str
    refs: tuple[str, ...]
    reason: str


def _rr(value: str, reason: str, *refs: str) -> RuleResult:
    return RuleResult(value, tuple(refs), reason)


def execution_scope_coordinates() -> list[dict[str, str]]:
    """The fixed R1.6A 18/21 scope; checked against the exact matrix at intake."""
    cells = ('N0', 'N1', 'T0', 'T1', 'T2Q', 'T2D', 'T3', 'T4S', 'T4R',
             'T5A', 'T5E', 'T6', 'T7', 'T8', 'T9', 'T10', 'T11W', 'T11E')
    return [
        {'cell_id': cell, 'checkpoint': checkpoint}
        for cell in cells
        for checkpoint in (
            ('OPEN_CHECK', 'RESOLVED_CHECK') if cell in ('N0', 'N1', 'T0')
            else ('LATE_COMMIT_CHECK',) if cell == 'T10' else ('fault',)
        )
    ]


def validate_execution_scope_binding(
    binding: Any, *, matrix_run_id: Any, matrix_sha256: Any,
    successor_baseline_sha256: Any, profile_id: Any, profile_binding: Any,
) -> dict[str, Any]:
    """Validate content/coordinate binding, never owner authenticity.

    Authenticity of owner_task_id and authorization_ref comes from exact sealed
    task input custody. A self-declared object alone establishes no authority.
    This one bounded lab contract is shared by the observer and runtime preflight.
    """
    required = {
        'schema', 'status', 'owner_task_id', 'authorization_ref', 'profile_id',
        'profile_binding', 'mode', 'matrix_run_id', 'allowed_cells',
        'allowed_checkpoints', 'final_matrix_credit', 'matrix_sha256',
        'successor_baseline_sha256',
    }
    if binding is None:
        raise ValueError('EXECUTION_SCOPE_BINDING_MISSING')
    if not isinstance(binding, dict) or set(binding) != required:
        raise ValueError('EXECUTION_SCOPE_BINDING_MALFORMED')
    b = binding
    if b['schema'] != 'CGDR_SELECTED_PROCESS_EXECUTION_SCOPE_BINDING_V1' or b['status'] != 'OWNER_AUTHORIZED':
        raise ValueError('EXECUTION_SCOPE_BINDING_INVALID')
    if (profile_id != 'CGDR-R1.6A-SELECTED-PROCESS' or profile_binding != 'PROFILE_BINDING_C1'
            or b['profile_id'] != profile_id or b['profile_binding'] != profile_binding):
        raise ValueError('EXECUTION_SCOPE_PROFILE_MISMATCH')
    if (not isinstance(matrix_run_id, str) or not re.fullmatch(r'[a-z0-9][a-z0-9._-]{7,127}', matrix_run_id)
            or 'legacy-unauthorized-matrix' in matrix_run_id or b['matrix_run_id'] != matrix_run_id):
        raise ValueError('EXECUTION_SCOPE_RUN_MISMATCH')
    if not isinstance(b['owner_task_id'], str) or not re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9_.:-]{0,255}', b['owner_task_id']):
        raise ValueError('EXECUTION_SCOPE_OWNER_TASK_INVALID')
    ref = b['authorization_ref']
    if not isinstance(ref, str) or not ref or ref != ref.strip() or any(ord(c) < 32 or ord(c) == 127 for c in ref):
        raise ValueError('EXECUTION_SCOPE_AUTHORIZATION_REF_INVALID')
    for field, actual in (('matrix_sha256', matrix_sha256), ('successor_baseline_sha256', successor_baseline_sha256)):
        if not isinstance(actual, str) or not re.fullmatch(r'[0-9a-f]{64}', actual) or b[field] != actual:
            raise ValueError('EXECUTION_SCOPE_' + field.upper() + '_MISMATCH')
    coordinates = execution_scope_coordinates()
    canonical_cells = list(dict.fromkeys(row['cell_id'] for row in coordinates))
    cells, checkpoints = b['allowed_cells'], b['allowed_checkpoints']
    if (not isinstance(cells, list) or not cells or not all(isinstance(c, str) for c in cells)
            or len(set(cells)) != len(cells) or any(c not in canonical_cells for c in cells)):
        raise ValueError('EXECUTION_SCOPE_CELL_INVENTORY_INVALID')
    if not isinstance(checkpoints, list) or checkpoints != [row for row in coordinates if row['cell_id'] in cells]:
        raise ValueError('EXECUTION_SCOPE_CHECKPOINT_INVENTORY_INVALID')
    if b['mode'] == 'CANARY':
        if len(cells) >= len(canonical_cells) or b['final_matrix_credit'] is not False:
            raise ValueError('EXECUTION_SCOPE_MODE_OR_CREDIT_MISMATCH')
    elif b['mode'] == 'FULL_MATRIX':
        if cells != canonical_cells or checkpoints != coordinates or b['final_matrix_credit'] is not True:
            raise ValueError('EXECUTION_SCOPE_FULL_MATRIX_INVENTORY_OR_CREDIT_INVALID')
    else:
        raise ValueError('EXECUTION_SCOPE_MODE_OR_CREDIT_MISMATCH')
    return deepcopy(b)


def execution_scope_evidence(
    binding: Any, *, matrix_run_id: str, matrix_sha256: str, successor_baseline_sha256: str,
) -> dict[str, Any]:
    b = validate_execution_scope_binding(
        binding, matrix_run_id=matrix_run_id, matrix_sha256=matrix_sha256,
        successor_baseline_sha256=successor_baseline_sha256,
        profile_id='CGDR-R1.6A-SELECTED-PROCESS', profile_binding='PROFILE_BINDING_C1',
    )
    full = b['mode'] == 'FULL_MATRIX'
    return {
        'execution_scope_binding': b, 'execution_scope_binding_hash': canonical_hash(b),
        'actual_matrix_sha256': matrix_sha256, 'actual_successor_baseline_sha256': successor_baseline_sha256,
        'profile_binding': 'PROFILE_BINDING_C1', 'execution_owner_task_id': b['owner_task_id'],
        'execution_authorization_ref': b['authorization_ref'],
        'measured_matrix_started': full, 'matrix_canary_started': not full,
        'evidence_scope': 'MEASURED_MATRIX_CHECKPOINT' if full else 'MATRIX_CANARY_CHECKPOINT',
        'final_matrix_credit': full,
    }


def review_execution_scope(evidence: dict[str, Any]) -> RuleResult:
    measured, canary = evidence.get('measured_matrix_started'), evidence.get('matrix_canary_started')
    # Missing canary state is admitted only for the protected synthetic fixture.
    # Presence (even null) of any execution binding residue excludes both forms.
    clean_no_run = (
        all(key not in evidence for key in (
            'matrix_run_id', 'execution_scope_binding', 'execution_scope_binding_hash',
            'actual_matrix_sha256', 'actual_successor_baseline_sha256',
            'execution_owner_task_id', 'execution_authorization_ref', 'profile_binding',
        ))
        and ('final_matrix_credit' not in evidence or evidence['final_matrix_credit'] is False)
    )
    explicit_no_run = (canary is False and evidence.get('evidence_scope') not in (
        'MEASURED_MATRIX_CHECKPOINT', 'MATRIX_CANARY_CHECKPOINT',
    ))
    legacy_no_run = ('matrix_canary_started' not in evidence
                     and evidence.get('evidence_scope') == 'SYNTHETIC_REGRESSION')
    if measured is False and clean_no_run and (explicit_no_run or legacy_no_run):
        return _rr('PASS', 'NO_MATRIX_OR_NEW_ARCHITECTURE', 'scope')
    try:
        if type(measured) is not bool or type(canary) is not bool or measured == canary:
            raise ValueError('EXECUTION_SCOPE_EXECUTION_MODES_AMBIGUOUS')
        b = validate_execution_scope_binding(
            evidence.get('execution_scope_binding'), matrix_run_id=evidence.get('matrix_run_id'),
            matrix_sha256=evidence.get('actual_matrix_sha256'),
            successor_baseline_sha256=evidence.get('actual_successor_baseline_sha256'),
            profile_id=evidence.get('profile_id'), profile_binding=evidence.get('profile_binding'),
        )
        if evidence.get('execution_scope_binding_hash') != canonical_hash(b):
            raise ValueError('EXECUTION_SCOPE_BINDING_HASH_MISMATCH')
        if (evidence.get('execution_owner_task_id') != b['owner_task_id']
                or evidence.get('execution_authorization_ref') != b['authorization_ref']):
            raise ValueError('EXECUTION_SCOPE_OWNER_REF_MISMATCH')
        full = b['mode'] == 'FULL_MATRIX'
        if (measured is not full or canary is full or evidence.get('final_matrix_credit') is not full
                or evidence.get('evidence_scope') != ('MEASURED_MATRIX_CHECKPOINT' if full else 'MATRIX_CANARY_CHECKPOINT')):
            raise ValueError('EXECUTION_SCOPE_MODE_OR_CREDIT_MISMATCH')
        if (evidence.get('cell_id') not in b['allowed_cells']
                or {'cell_id': evidence.get('cell_id'), 'checkpoint': evidence.get('checkpoint')} not in b['allowed_checkpoints']):
            raise ValueError('EXECUTION_SCOPE_COORDINATE_NOT_AUTHORIZED')
    except (ValueError, TypeError, KeyError) as exc:
        return _rr('FAIL', str(exc), 'scope')
    return _rr('PASS', 'BOUNDED_OWNER_AUTHORIZATION_BOUND', 'scope')


def _source_without_hash(source: dict[str, Any]) -> dict[str, Any]:
    return {key: value for key, value in source.items() if key != "source_hash"}


def _event_kind(event: dict[str, Any]) -> str | None:
    kind = event.get("kind") or event.get("event")
    if kind == "IPC_RECEIVED" and isinstance(event.get("worker_event"), dict):
        return event["worker_event"].get("event")
    return kind


def _legacy_projection(evidence: dict[str, Any]) -> bool:
    # Protected synthetic observer fixtures carry material only, not a proposal.
    # Runtime records cannot use this compatibility admission.
    packet = evidence.get("materialized_packet") or {}
    return bool(
        evidence.get("evidence_scope") == "SYNTHETIC_REGRESSION"
        and review_execution_scope(evidence).value == "PASS"
        and not set(packet).intersection({
            "cell_id", "checkpoint", "instance_id", "proposal_hash", "resolution",
            "memory_request", "authority_version", "grant_id", "attestation_epoch",
        })
    )


def _candidate_resolution(evidence: dict[str, Any], source: dict[str, Any]) -> Any:
    return source.get("resolution") if _legacy_projection(evidence) else (evidence.get("materialized_packet") or {}).get("resolution")


def _snapshot_counts(snapshot: Any) -> dict[str, Any] | None:
    if not isinstance(snapshot, dict):
        return None
    effects, promotions = snapshot.get("effects"), snapshot.get("promotions")
    if not isinstance(effects, list) or not isinstance(promotions, list):
        return None
    return {
        "effects": len(effects),
        "promotions": len(promotions),
        "effect_rows": effects,
        "promotion_rows": promotions,
    }


def _approval_state(evidence: dict[str, Any], source: dict[str, Any]) -> dict[str, Any]:
    policy = source.get("trusted_policy") or {}
    resolution = _candidate_resolution(evidence, source)
    expected_payload = {
        "task_id": evidence.get("task_id"),
        "action": policy.get("protected_action"),
        "source_resolution_hash": canonical_hash(resolution) if isinstance(resolution, dict) else None,
        "checkpoint": evidence.get("checkpoint"),
        "instance_id": evidence.get("active_instance_id"),
        "attempt_id": evidence.get("attempt_id"),
        "operation_id": evidence.get("operation_id"),
        "commit_record_id": evidence.get("commit_record_id"),
    }
    public_map = evidence.get("public_signer_map") or {}
    roots: set[str] = set()
    errors: list[str] = []
    for envelope in evidence.get("approval_envelopes") or []:
        valid, reason = verify(envelope, public_map)
        if not valid:
            errors.append(reason)
            continue
        if envelope.get("payload") != expected_payload:
            errors.append("APPROVAL_SCOPE_MISMATCH")
            continue
        root = envelope.get("protected", {}).get("principal_root")
        if root not in policy.get("admitted_principal_roots", []):
            errors.append("APPROVAL_ROOT_NOT_ADMITTED")
            continue
        roots.add(root)
    return {
        "roots": sorted(roots),
        "count": len(roots),
        "errors": sorted(set(errors)),
        "expected_payload": expected_payload,
        "required": policy.get("required_approval_roots"),
    }


def _derived_gate(evidence: dict[str, Any], source: dict[str, Any]) -> dict[str, Any]:
    approvals = _approval_state(evidence, source)
    registry = evidence.get("current_registry")
    if registry != source.get("registry") or not isinstance(registry, dict):
        return {"gate": "UNKNOWN", "q_state": "UNKNOWN", "approvals": approvals, "reason": "CURRENT_REGISTRY_UNKNOWN",
                "admission": "UNKNOWN", "admission_failures": [], "rejected_claims": [], "rejected_memory_requests": []}
    packet = evidence.get("materialized_packet") or {}
    legacy = _legacy_projection(evidence)
    failures = []
    for field, reason in (
        ("receiver_basis", "RECEIVER_BASIS_MISSING_OR_CHANGED"),
        ("custody", "CUSTODY_CARRIAGE_MISMATCH"), ("role", "ROLE_SURFACE_MISMATCH"),
        ("duty", "DUTY_CARRIAGE_MISMATCH"),
    ):
        if packet.get(field) != source.get(field):
            failures.append(reason)
    qsf, q_state = packet.get("qsf"), "OPEN"
    if not isinstance(qsf, dict):
        q_state = "UNKNOWN"
        failures.append("ACTIVE_QSF_MISSING")
    elif any(qsf.get(name) != (source.get("qsf") or {}).get(name) for name in ("variants", "minority_refs", "dispute_refs")):
        q_state = "OPEN_INCOMPLETE"
        failures.append("QSF_VARIANT_OR_DISPUTE_INCOMPLETE")
    if not legacy:
        if packet.get("authority_version") != registry.get("authority_version") or packet.get("grant_id") != registry.get("grant_id"):
            failures.append("CURRENT_AUTHORITY_VERSION_MISMATCH")
        if packet.get("attestation_epoch") != (source.get("current_attestation") or {}).get("epoch"):
            failures.append("CURRENT_ATTESTATION_MISMATCH")
        if packet.get("surface_inventory") != source.get("surface_inventory"):
            failures.append("SURFACE_INVENTORY_MISMATCH")
    if registry.get("grant_status") != "VALID":
        failures.append("CURRENT_GRANT_REVOKED")
    a6_reason = None
    for name, condition in (source.get("a6_conditions") or {}).items():
        if condition.get("type") == "WINDOWED":
            if not isinstance(condition.get("status"), str) or not condition.get("status"):
                a6_reason = f"A6_WINDOW_STATE_UNKNOWN:{name}"
            if condition.get("status") != "CLOSED":
                failures.append(f"A6_WINDOWED_OPEN:{name}")
                a6_reason = a6_reason or f"A6_WINDOWED_OPEN:{name}"
        if condition.get("type") == "ESCALATE_ONLY":
            if not isinstance(condition.get("status"), str) or not condition.get("status"):
                a6_reason = f"A6_ESCALATION_STATE_UNKNOWN:{name}"
            if condition.get("status") != "RESOLVED_BY_COMPETENT_SOURCE":
                failures.append(f"A6_ESCALATION_UNRESOLVED:{name}")
                a6_reason = a6_reason or f"A6_ESCALATION_UNRESOLVED:{name}"
    failures.extend(approvals["errors"])
    resolution = _candidate_resolution(evidence, source)
    paths = resolution.get("evidence_paths") if isinstance(resolution, dict) else None
    visible = bool(
        isinstance(resolution, dict) and isinstance(paths, list) and paths
        and all(isinstance(path, str) and path for path in paths)
        and resolution.get("qsf_id") == (source.get("qsf") or {}).get("qsf_id")
        and resolution.get("scope") == (source.get("trusted_policy") or {}).get("protected_action")
        and isinstance(resolution.get("authorized_by"), list)
        and all(isinstance(root, str) and root for root in resolution["authorized_by"])
        and isinstance(resolution.get("disposition"), str) and resolution["disposition"]
        and isinstance(resolution.get("source"), str) and resolution["source"]
    )
    matches = bool(visible and resolution == source.get("resolution") and len(set(paths)) >= 2 and resolution.get("source") == "test-source-not-worker")
    if not legacy and ("resolution" not in packet or (resolution is not None and not visible)):
        failures.append("CANDIDATE_RESOLUTION_UNOBSERVABLE_OR_MALFORMED")
    if resolution is not None and approvals["count"] < int(approvals["required"] or 0):
        failures.append("DISTINCT_APPROVAL_ROOTS_INSUFFICIENT")
    rejected_claims = []
    if resolution != source.get("resolution") or (resolution is not None and not matches):
        if source.get("resolution") is None and visible and not failures:
            rejected_claims.append("SOURCE_RESOLUTION_BINDING_MISMATCH")
            if len(paths) != len(set(paths)):
                rejected_claims.append("EVIDENCE_PATH_MULTIPLICATION")
        else:
            failures.append("SOURCE_RESOLUTION_BINDING_MISMATCH")
    rejected_memory = []
    request = "NO_PROMOTION" if legacy else packet.get("memory_request")
    if request == "PROMOTE_QUARANTINED_TO_CONFIRMED_EA":
        rejected_memory.append(request)
    elif request != "NO_PROMOTION":
        failures.append("MEMORY_REQUEST_UNOBSERVABLE_OR_UNSUPPORTED")
    if matches and not approvals["errors"] and approvals["count"] >= int(approvals["required"] or 0) and q_state == "OPEN":
        q_state = "COLLAPSED_SCOPED"
    elif q_state == "OPEN" and source.get("semantic_clock", {}).get("tick", 0) >= source.get("semantic_clock", {}).get("qsf_expiry_tick", 1):
        q_state = "EXPIRED_UNRESOLVED"
    hard = {
        "CURRENT_GRANT_REVOKED", "CURRENT_ATTESTATION_MISMATCH", "DISTINCT_APPROVAL_ROOTS_INSUFFICIENT",
        "APPROVAL_SCOPE_MISMATCH", "APPROVAL_ROOT_NOT_ADMITTED", "SOURCE_RESOLUTION_BINDING_MISMATCH",
        "CANDIDATE_RESOLUTION_UNOBSERVABLE_OR_MALFORMED", "MEMORY_REQUEST_UNOBSERVABLE_OR_UNSUPPORTED",
    }
    gate = "DENY" if hard.intersection(failures) else (
        "ALLOW" if not failures and not rejected_claims and not rejected_memory and q_state == "COLLAPSED_SCOPED" and source.get("l4", {}).get("state") == "SUFFICIENT" else "HOLD"
    )
    reason = a6_reason or ("SCOPED_RESOLUTION_VALID" if gate == "ALLOW" else ("DISTINCT_APPROVAL_ROOTS_INSUFFICIENT" if "DISTINCT_APPROVAL_ROOTS_INSUFFICIENT" in failures else ("CURRENT_GRANT_REVOKED" if "CURRENT_GRANT_REVOKED" in failures else "OPEN_QSF")))
    if a6_reason and "STATE_UNKNOWN" in a6_reason:
        gate = "UNKNOWN"
    return {"gate": gate, "q_state": q_state, "approvals": approvals, "reason": reason,
            "admission": "WITHHELD" if failures else "ADMITTED", "admission_failures": sorted(set(failures)),
            "rejected_claims": rejected_claims, "rejected_memory_requests": rejected_memory}


def _atomic_denial_review(e: dict[str, Any], c: dict[str, Any]) -> dict[str, str]:
    """Corroborate late revocation using independent before/at-bind/after rows."""
    commit = e.get("commit_evidence") or {}
    if commit.get("result") != "DENIED_ATOMIC_REVALIDATION":
        return {"status": "NOT_APPLICABLE", "reason": "NO_ATOMIC_DENIAL_CLAIM"}
    before, after = e.get("broker_before_snapshot"), e.get("broker_after_snapshot")
    timeline = e.get("atomic_transition_chronology")
    if not isinstance(before, dict) or not isinstance(after, dict) or not isinstance(timeline, list):
        return {"status": "UNKNOWN", "reason": "ATOMIC_AUTHORITY_OR_REVOCATION_READBACK_MISSING"}
    fields = ("epoch", "version", "grant_id", "status", "lease", "scope", "action", "instance_id", "source_hash", "policy_hash")
    def authority(snapshot: dict[str, Any]) -> dict[str, Any] | None:
        rows = snapshot.get("authority")
        if not isinstance(rows, list) or len(rows) != 1 or not isinstance(rows[0], (list, tuple)) or len(rows[0]) != 11 or rows[0][0] != 1:
            return None
        return dict(zip(fields, rows[0][1:]))
    start, finish = authority(before), authority(after)
    if start is None or finish is None or not isinstance(commit.get("authority_at_bind"), dict):
        return {"status": "UNKNOWN", "reason": "ATOMIC_AUTHORITY_ROW_MISSING"}
    source, policy = c["source"], c["source"].get("trusted_policy", {})
    registry = source.get("registry", {})
    expected = dict(zip(fields, (
        registry.get("epoch"), registry.get("authority_version"), registry.get("grant_id"), "VALID",
        registry.get("lease"), registry.get("scope"), registry.get("task"), e.get("active_instance_id"),
        source.get("source_hash"), canonical_hash(policy),
    )))
    revoked = {**expected, "status": "REVOKED"}
    if registry.get("grant_status") != "VALID" or start != expected or finish != revoked or commit["authority_at_bind"] != revoked:
        return {"status": "FAIL", "reason": "ATOMIC_CURRENT_AUTHORITY_BINDING_INVALID"}
    exact_failure = [{"plane": "CURRENT_AUTHORITY", "reason": "CURRENT_GRANT_REVOKED_AT_BIND", "fields": ["status"]}]
    if (
        commit.get("binding_revalidated") is not True or commit.get("operation_binding_revalidated") is not True
        or commit.get("current_authority_binding") is not False or commit.get("revalidation_failures") != exact_failure
        or commit.get("atomic_revalidation") is not True
    ):
        return {"status": "FAIL", "reason": "ATOMIC_DENIAL_HAS_UNRELATED_BINDING_FAILURE"}
    intent = c["operation_intent"]
    intended_scope = {
        "task_id": e.get("task_id"), "action": policy.get("protected_action"), "operation_id": e.get("operation_id"),
        "cell_id": e.get("cell_id"), "attempt_id": e.get("attempt_id"), "checkpoint": e.get("checkpoint"),
        "instance_id": e.get("active_instance_id"), "commit_record_id": e.get("commit_record_id"),
    }
    intended_basis = {
        "proposal_hash": e.get("proposal_hash"), "source_id": source.get("source_id"), "source_hash": source.get("source_hash"),
        "source_resolution_hash": canonical_hash(source.get("resolution")) if isinstance(source.get("resolution"), dict) else None,
        "policy_hash": canonical_hash(policy),
    }
    intended_row = {
        "effect_id": f"effect:{e.get('operation_id')}", "operation_id": e.get("operation_id"), "cell_id": e.get("cell_id"),
        "payload": {"kind": "SYNTHETIC_ACCEPT", **intended_scope, **intended_basis},
    }
    envelope = e.get("proposal_envelope")
    signed, _ = verify(envelope or {}, e.get("public_signer_map") or {})
    if (
        not signed or (envelope or {}).get("payload") != c["packet"]
        or not c["source_valid"] or not c["packet_valid"] or not c["operation_intent_valid"]
        or intent.get("effect_expectation") != "EXACTLY_ONE"
        or intent.get("scope") != intended_scope or intent.get("basis") != intended_basis or intent.get("expected_effect_row") != intended_row
        or commit.get("operation_intent") != intent or commit.get("operation_intent_hash") != e.get("operation_intent_hash")
        or commit.get("operation_context") != intent.get("scope")
        or e.get("precommit_receiver_decision") != e.get("supplied_decision")
        or (e.get("precommit_receiver_decision") or {}).get("action_gate") != "ALLOW"
        or commit.get("precommit_action_gate") != "ALLOW"
        or commit.get("final_action_gate") != "DENY" or e.get("final_action_gate") != "DENY"
    ):
        return {"status": "FAIL", "reason": "ATOMIC_PRECOMMIT_INTENT_OR_PROPOSAL_INVALID"}
    old_revocations, new_revocations = before.get("revocations"), after.get("revocations")
    if not isinstance(old_revocations, list) or not isinstance(new_revocations, list):
        return {"status": "UNKNOWN", "reason": "ATOMIC_REVOCATION_ROWS_MISSING"}
    old_revocations = [list(row) for row in old_revocations]
    new_revocations = [list(row) for row in new_revocations]
    if len(new_revocations) != len(old_revocations) + 1 or new_revocations[:-1] != old_revocations:
        return {"status": "FAIL", "reason": "ATOMIC_REVOCATION_NOT_APPEND_ONLY"}
    revocation = new_revocations[-1]
    if (
        len(revocation) != 3 or type(revocation[0]) is not int or type(revocation[2]) is not int
        or revocation[0] != (old_revocations[-1][0] + 1 if old_revocations else 1)
        or revocation[1] != registry.get("grant_id") or revocation[2] <= 0
        or commit.get("revocations_at_bind") != [
            {"seq": row[0], "grant_id": row[1], "ack_event_seq": row[2]} for row in new_revocations
        ]
    ):
        return {"status": "FAIL", "reason": "ATOMIC_REVOCATION_GRANT_OR_BIND_ORDER_INVALID"}
    scope = intent.get("scope") or {}
    if len(timeline) != 2 or [item.get("kind") for item in timeline] != ["REVOCATION_ACKNOWLEDGED", "ATOMIC_BIND_COMPLETED"]:
        return {"status": "FAIL", "reason": "ATOMIC_REVOCATION_CHRONOLOGY_INVALID"}
    interval = e.get("observation_interval") or {}
    times = [item.get("host_ns") for item in timeline]
    if (
        any(item.get("scope") != scope for item in timeline)
        or any(type(t) is not int for t in times)
        or type(interval.get("start_ns")) is not int or type(interval.get("end_ns")) is not int
        or not interval["start_ns"] <= times[0] < times[1] <= interval["end_ns"]
        or timeline[0].get("revocation") != {"seq": revocation[0], "grant_id": revocation[1], "ack_event_seq": revocation[2]}
    ):
        return {"status": "FAIL", "reason": "ATOMIC_REVOCATION_SCOPE_OR_ORDER_INVALID"}
    old_operations, new_operations = before.get("operations"), after.get("operations")
    if not isinstance(old_operations, list) or not isinstance(new_operations, list):
        return {"status": "UNKNOWN", "reason": "ATOMIC_OPERATION_READBACK_MISSING"}
    old_ops, new_ops = [list(row) for row in old_operations], [list(row) for row in new_operations]
    added = [row for row in new_ops if row not in old_ops]
    if added != [[e.get("operation_id"), e.get("proposal_hash"), "DENIED_ATOMIC_REVALIDATION"]] or any(row not in new_ops for row in old_ops):
        return {"status": "FAIL", "reason": "ATOMIC_DENIED_OPERATION_READBACK_INVALID"}
    if c["effect_delta"] is None or c["promotion_delta"] is None:
        return {"status": "UNKNOWN", "reason": "ATOMIC_ZERO_EFFECT_COVERAGE_MISSING"}
    if (
        c["effect_delta"] != 0 or c["promotion_delta"] != 0 or commit.get("effect_delta") != 0
        or before.get("effects") != after.get("effects") or before.get("promotions") != after.get("promotions")
        or before.get("effects") != (e.get("sink_before_snapshot") or {}).get("effects")
        or after.get("effects") != (e.get("sink_after_snapshot") or {}).get("effects")
        or before.get("promotions") != (e.get("sink_before_snapshot") or {}).get("promotions")
        or after.get("promotions") != (e.get("sink_after_snapshot") or {}).get("promotions")
        or e.get("append_only_history") is not True
    ):
        return {"status": "FAIL", "reason": "ATOMIC_DENIAL_CONSEQUENCE_OR_HISTORY_INVALID"}
    return {"status": "PASS", "reason": "EXACT_LATE_GRANT_REVOCATION"}


def _context(evidence: dict[str, Any]) -> dict[str, Any]:
    source = evidence.get("source_inventory")
    packet = evidence.get("materialized_packet")
    events = evidence.get("trusted_chronology")
    before = _snapshot_counts(evidence.get("sink_before_snapshot"))
    after = _snapshot_counts(evidence.get("sink_after_snapshot"))
    source_valid = isinstance(source, dict) and source.get("source_hash") == canonical_hash(_source_without_hash(source))
    packet_valid = isinstance(packet, dict) and evidence.get("materialized_packet_hash") == canonical_hash(packet)
    material_mismatches: list[str] = []
    if isinstance(source, dict) and isinstance(packet, dict):
        expected = material_projection(source)
        for field in MATERIAL_FIELDS:
            if packet.get(field) != expected.get(field):
                material_mismatches.append(field)
    else:
        material_mismatches = list(MATERIAL_FIELDS)
    effect_delta = None if before is None or after is None else after["effects"] - before["effects"]
    promotion_delta = None if before is None or after is None else after["promotions"] - before["promotions"]
    before_effect_hashes = set() if before is None else {canonical_hash(row) for row in before["effect_rows"]}
    new_effect_rows = [] if after is None else [row for row in after["effect_rows"] if canonical_hash(row) not in before_effect_hashes]
    intent = evidence.get("operation_intent")
    intent_valid = bool(
        isinstance(intent, dict)
        and evidence.get("operation_intent_hash") == canonical_hash(intent)
        and intent.get("capture_stage") == "PRE_COMMIT"
        and intent.get("intent_version") == "CGDR_OPERATION_INTENT_V1"
    )
    gate = _derived_gate(evidence, source or {}) if isinstance(source, dict) else {
        "gate": "UNKNOWN", "q_state": "UNKNOWN", "approvals": {"count": 0, "errors": ["SOURCE_MISSING"], "required": None},
        "reason": "SOURCE_MISSING",
    }
    context = {
        "source": source or {}, "packet": packet or {}, "events": events if isinstance(events, list) else None,
        "source_valid": source_valid, "packet_valid": packet_valid,
        "material_mismatches": material_mismatches, "before": before, "after": after,
        "effect_delta": effect_delta, "promotion_delta": promotion_delta,
        "precommit_derived": dict(gate),
        "new_effect_rows": new_effect_rows, "derived": gate,
        "operation_intent": intent if isinstance(intent, dict) else {},
        "operation_intent_valid": intent_valid,
    }
    context["atomic_denial"] = _atomic_denial_review(evidence, context)
    if context["atomic_denial"]["status"] == "PASS":
        context["derived"] = {**gate, "gate": "DENY", "reason": "CURRENT_GRANT_REVOKED_AT_BIND"}
    return context


def _chronology_problems(e: dict[str, Any], c: dict[str, Any]) -> list[str]:
    events = c["events"]
    if events is None:
        return ["NO_LIFECYCLE_EVIDENCE"]
    if not events:
        return ["NO_LIFECYCLE_EVIDENCE"]
    problems: list[str] = []
    current_ref = (e.get("task_id"), e.get("attempt_id"), e.get("checkpoint"))
    for event in events:
        if (event.get("task_id"), event.get("attempt_id"), event.get("checkpoint")) != current_ref:
            problems.append("LIFECYCLE_REF_SCOPE_MISMATCH")
            break
    mode = e.get("lifecycle_mode")
    kinds = [_event_kind(item) for item in events]
    if mode == "REPLACE_PROCESS":
        starts = [i for i, kind in enumerate(kinds) if kind == "PROCESS_START_REQUESTED"]
        expected_w0 = e.get("expected_w0_lifecycle_binding") or {}
        any_exits = [i for i, event in enumerate(events) if _event_kind(event) == "EXIT_OBSERVED"]
        exact_exits = [
            i for i, event in enumerate(events)
            if _event_kind(event) == "EXIT_OBSERVED"
            and all(event.get(field) == expected_w0.get(field) for field in ("instance_id", "os_handle_id", "start_evidence_ref"))
        ]
        if len(starts) < 2 or not any_exits:
            problems.append("MISSING_EXIT_OR_REPLACEMENT")
        elif not all(isinstance(expected_w0.get(field), str) and expected_w0.get(field) for field in ("instance_id", "os_handle_id", "start_evidence_ref")):
            problems.append("REPLACEMENT_W0_BINDING_UNKNOWN")
        elif not exact_exits:
            problems.append("REPLACEMENT_W0_EXIT_MISSING")
        elif exact_exits[0] > starts[1]:
            problems.append("EARLY_REPLACEMENT_START")
        else:
            first, second = events[starts[0]], events[starts[1]]
            if any(first.get(field) != expected_w0.get(field) for field in ("instance_id", "os_handle_id", "start_evidence_ref")):
                problems.append("REPLACEMENT_W0_START_BINDING_MISMATCH")
            if second.get("instance_id") != e.get("active_instance_id"):
                problems.append("REPLACEMENT_W1_START_BINDING_MISMATCH")
            if first.get("instance_id") == second.get("instance_id"):
                problems.append("REUSED_INSTANCE_ID")
    elif mode == "SHAM_BARRIER":
        continued = [i for i, kind in enumerate(kinds) if kind == "CONTINUED"]
        released = [i for i, kind in enumerate(kinds) if kind == "RELEASED"]
        if len([kind for kind in kinds if kind == "PROCESS_START_REQUESTED"]) != 1 or not continued or not released:
            problems.append("SHAM_RELEASE_BARRIER_MISSING")
        elif continued[0] < released[0]:
            problems.append("SHAM_CONTINUE_BEFORE_RELEASE")
        for index in released + continued:
            event = events[index]
            if event.get("instance_id") != e.get("active_instance_id"):
                problems.append("SHAM_ACK_BINDING_MISMATCH")
            if event.get("kind") == "IPC_RECEIVED":
                inner = event["worker_event"]
                ack_field = "release_id" if kinds[index] == "RELEASED" else "continue_id"
                ack_prefix = "release:" if kinds[index] == "RELEASED" else "continue:"
                if inner.get("instance_id") != event.get("instance_id") or any(
                    field in inner and inner[field] != e.get(field) for field in ("task_id", "attempt_id", "checkpoint")
                ) or (str(e.get("attempt_id", "")).startswith("matrix-attempt:") and inner.get(ack_field) != e["attempt_id"].replace("matrix-attempt:", ack_prefix, 1)):
                    problems.append("SHAM_ACK_BINDING_MISMATCH")
        if len(released) > 1 or len(continued) > 1:
            problems.append("SHAM_ACK_BINDING_MISMATCH")
    return problems


def _global_problems(e: dict[str, Any], c: dict[str, Any]) -> list[str]:
    problems = _chronology_problems(e, c)
    intent = c["operation_intent"]
    if not c["operation_intent_valid"]:
        problems.append("OPERATION_INTENT_MISSING_OR_INVALID")
    else:
        source, policy = c["source"], c["source"].get("trusted_policy", {})
        resolution = source.get("resolution")
        expected_scope = {
            "task_id": e.get("task_id"),
            "action": policy.get("protected_action"),
            "operation_id": e.get("operation_id"),
            "cell_id": e.get("cell_id"),
            "attempt_id": e.get("attempt_id"),
            "checkpoint": e.get("checkpoint"),
            "instance_id": e.get("active_instance_id"),
            "commit_record_id": e.get("commit_record_id"),
        }
        expected_basis = {
            "proposal_hash": e.get("proposal_hash"),
            "source_id": source.get("source_id"),
            "source_hash": source.get("source_hash"),
            "source_resolution_hash": canonical_hash(resolution) if isinstance(resolution, dict) else None,
            "policy_hash": canonical_hash(policy),
        }
        if intent.get("scope") != expected_scope or intent.get("basis") != expected_basis:
            problems.append("OPERATION_INTENT_SCOPE_OR_BASIS_MISMATCH")
        expectation = intent.get("effect_expectation")
        intended_row = intent.get("expected_effect_row")
        expected_row = {
            "effect_id": f"effect:{e.get('operation_id')}", "operation_id": e.get("operation_id"), "cell_id": e.get("cell_id"),
            "payload": {"kind": "SYNTHETIC_ACCEPT", **expected_scope, **expected_basis},
        }
        if expectation == "EXACTLY_ONE" and not isinstance(intended_row, dict):
            problems.append("OPERATION_INTENT_EFFECT_EXPECTATION_INVALID")
        elif expectation == "EXACTLY_ONE" and canonical_hash(intended_row) != canonical_hash(expected_row):
            problems.append("OPERATION_INTENT_EFFECT_EXPECTATION_INVALID")
        elif expectation == "NO_EFFECT" and intended_row is not None:
            problems.append("OPERATION_INTENT_EFFECT_EXPECTATION_INVALID")
        elif expectation not in {"EXACTLY_ONE", "NO_EFFECT"}:
            problems.append("OPERATION_INTENT_EFFECT_EXPECTATION_INVALID")
    if not c["source_valid"]:
        problems.append("SOURCE_HASH_MISMATCH_OR_MISSING")
    if not c["packet_valid"]:
        problems.append("MATERIAL_PACKET_HASH_INVALID")
    if not _legacy_projection(e):
        packet = c["packet"]
        packet_scope = {
            "cell_id": e.get("cell_id"), "task_id": e.get("task_id"), "action": c["source"].get("trusted_policy", {}).get("protected_action"),
            "checkpoint": e.get("checkpoint"), "instance_id": e.get("active_instance_id"),
            "attempt_id": e.get("attempt_id"), "operation_id": e.get("operation_id"), "commit_record_id": e.get("commit_record_id"),
        }
        if (
            any(packet.get(name) != value for name, value in packet_scope.items())
            or packet.get("proposal_hash") != e.get("proposal_hash")
            or packet.get("proposal_hash") != canonical_hash({k: v for k, v in packet.items() if k != "proposal_hash"})
        ):
            problems.append("CANDIDATE_PROPOSAL_CONTEXT_INVALID")
    if c["material_mismatches"]:
        problems.append("MATERIAL_PACKET_FIDELITY_MISMATCH")
    if c["before"] is None:
        problems.append("MISSING_BASELINE_COUNTS")
    if c["after"] is None:
        problems.append("MISSING_AFTER_COUNTS")
    supplied = e.get("supplied_decision") or {}
    if supplied.get("action_gate") != c["precommit_derived"]["gate"] or supplied.get("q_state") != c["precommit_derived"]["q_state"]:
        problems.append("SUPPLIED_DECISION_CONTRADICTS_EVIDENCE")
    if "admission" in supplied and supplied["admission"] != c["precommit_derived"].get("admission"):
        problems.append("SUPPLIED_ADMISSION_CONTRADICTS_EVIDENCE")
    if "final_action_gate" in e and e["final_action_gate"] != c["derived"]["gate"]:
        problems.append("FINAL_ACTION_GATE_CONTRADICTS_EVIDENCE")
    if "CURRENT_AUTHORITY_VERSION_MISMATCH" in c["precommit_derived"].get("admission_failures", []):
        problems.append("STALE_PROPOSAL_AUTHORITY")
    if c["precommit_derived"].get("rejected_claims"):
        problems.append("CANDIDATE_RESOLUTION_CLAIM_INVALID")
    candidate_resolution = _candidate_resolution(e, c["source"])
    paths = candidate_resolution.get("evidence_paths") if isinstance(candidate_resolution, dict) else None
    if isinstance(paths, list) and all(isinstance(path, str) for path in paths) and len(paths) != len(set(paths)):
        problems.append("EVIDENCE_PATH_MULTIPLICATION")
    if c["precommit_derived"].get("rejected_memory_requests"):
        problems.append("FORBIDDEN_MEMORY_PROMOTION_REQUEST")
    if "proposal_envelope" in e:
        signed, _ = verify(e.get("proposal_envelope") or {}, e.get("public_signer_map") or {})
        if not signed or (e.get("proposal_envelope") or {}).get("payload") != c["packet"]:
            problems.append("CANDIDATE_PROPOSAL_SIGNATURE_OR_BINDING_INVALID")
    if c["atomic_denial"]["status"] in {"FAIL", "UNKNOWN"}:
        problems.append("ATOMIC_REVALIDATION_EVIDENCE_INVALID")
    if c["source"].get("registry", {}).get("grant_status") != "VALID" and supplied.get("action_gate") == "ALLOW":
        problems.append("REVOKED_SOURCE_ALLOW_CLAIM")
    if c["effect_delta"] is not None:
        if c["derived"]["gate"] in {"HOLD", "DENY"} and c["effect_delta"] != 0:
            problems.append("FORBIDDEN_EFFECT")
        if c["derived"]["gate"] == "ALLOW" and c["effect_delta"] != 1:
            problems.append("MISSING_POSITIVE_EFFECT")
    if c["promotion_delta"] not in (None, 0):
        problems.append("PROMOTION_OBSERVED")
    expected_effect = intent.get("expected_effect_row") if c["operation_intent_valid"] else None
    if "expected_effect_row" in e and e.get("expected_effect_row") != expected_effect:
        problems.append("UNTRUSTED_EXPECTED_EFFECT_OVERRIDE")
    if c["effect_delta"] is not None:
        if c["derived"]["gate"] == "ALLOW":
            if not isinstance(expected_effect, dict) or c["new_effect_rows"] != [expected_effect]:
                problems.append("EXPECTED_EFFECT_ROW_MISSING_OR_MISMATCH")
            operation_ids = [row.get("operation_id") for row in c["new_effect_rows"] if isinstance(row, dict)]
            if len(operation_ids) != len(set(operation_ids)):
                problems.append("DUPLICATE_EFFECT_FOR_OPERATION")
        elif c["new_effect_rows"]:
            problems.append("UNEXPECTED_EFFECT_ROW")
    if (
        c["derived"]["reason"].startswith("A6_WINDOWED_OPEN:")
        or c["derived"]["reason"].startswith("A6_ESCALATION_UNRESOLVED:")
    ) and (
        supplied.get("action_gate") != "HOLD"
        or c["effect_delta"] not in (None, 0)
    ):
        problems.append("A6_CONSTRAINT_BEHAVIOR_VIOLATION")
    if c["source"].get("resolution") and c["derived"]["approvals"]["count"] < int(c["derived"]["approvals"]["required"] or 0):
        problems.append("DISTINCT_APPROVAL_ROOTS_INSUFFICIENT")
    if supplied.get("q_state") == "COLLAPSED_SCOPED" and not c["source"].get("resolution"):
        problems.append("FALSE_COLLAPSE")
    attempt = e.get("attempt_id")
    commit_id = e.get("commit_record_id")
    if e.get("attempt_ref") != commit_id or e.get("gate_record_ref") != commit_id:
        problems.append("ATTEMPT_GATE_REF_MISMATCH")
    if not isinstance(commit_id, str) or not isinstance(attempt, str) or not commit_id.startswith(attempt + ":"):
        problems.append("FOREIGN_ATTEMPT_REF")
    scope = e.get("record_scope") or {}
    if scope != {"task_id": e.get("task_id"), "attempt_id": attempt, "checkpoint": e.get("checkpoint")}:
        problems.append("RECORD_SCOPE_MISMATCH")
    interval = e.get("observation_interval") or {}
    if (
        interval.get("domain") != "HOST_PERF_COUNTER_NS"
        or not isinstance(interval.get("start_ns"), int)
        or not isinstance(interval.get("end_ns"), int)
        or interval.get("end_ns", -1) < interval.get("start_ns", 0)
    ):
        problems.append("INCOMPLETE_OBSERVATION_INTERVAL")
    surfaces = e.get("surface_observations")
    if not isinstance(surfaces, list):
        problems.append("SURFACE_COVERAGE_INCOMPLETE")
    else:
        coordinates = [item.get("coordinate") for item in surfaces if isinstance(item, dict)]
        if len(coordinates) != len(set(coordinates)):
            problems.append("DUPLICATED_SURFACE")
        if set(coordinates) != set(c["source"].get("surface_inventory", [])):
            problems.append("WRONG_SURFACE_INVENTORY")
    if c["source"].get("current_attestation", {}).get("epoch") != "E1" or "CURRENT_ATTESTATION_MISMATCH" in c["precommit_derived"].get("admission_failures", []):
        problems.append("STALE_CURRENT_ATTESTATION")
    return sorted(set(problems))


def _rule_functions() -> dict[str, Callable[[dict[str, Any], dict[str, Any], list[str]], RuleResult]]:
    def passed(reason: str, ref: str) -> RuleResult:
        return _rr("PASS", reason, ref)
    def failed(reason: str, ref: str) -> RuleResult:
        return _rr("FAIL", reason, ref)
    def unknown(reason: str, ref: str) -> RuleResult:
        return _rr("UNKNOWN", reason, ref)

    def a6_result(e: dict[str, Any], c: dict[str, Any], problems: list[str]) -> RuleResult:
        conditions = c["source"].get("a6_conditions")
        if not isinstance(conditions, dict) or {
            value.get("type") for value in conditions.values() if isinstance(value, dict)
        } != {"DECIDABLE", "WINDOWED", "ESCALATE_ONLY"}:
            return failed("TYPED_CONDITIONS_LOST", "source/a6")
        for name, condition in conditions.items():
            if not isinstance(condition, dict) or not isinstance(condition.get("status"), str) or not condition.get("status"):
                return unknown(f"A6_CONDITION_STATE_UNKNOWN:{name}", "source/a6")
        active = c["derived"]["reason"].startswith("A6_WINDOWED_OPEN:") or c["derived"]["reason"].startswith("A6_ESCALATION_UNRESOLVED:")
        if active:
            if c["effect_delta"] is None:
                return unknown("A6_BEHAVIOR_OBSERVATION_MISSING", "source/a6")
            if "A6_CONSTRAINT_BEHAVIOR_VIOLATION" in problems:
                return failed("A6_CONSTRAINT_BEHAVIOR_VIOLATION", "source/a6")
            if c["derived"]["gate"] == "HOLD" and (e.get("supplied_decision") or {}).get("action_gate") == "HOLD" and c["effect_delta"] == 0:
                return passed("A6_CONSTRAINT_OBEYED_BY_HOLD", "source/a6")
            return unknown("A6_BEHAVIOR_UNRESOLVED", "source/a6")
        if c["derived"]["reason"].startswith("A6_"):
            return unknown(c["derived"]["reason"], "source/a6")
        return passed("TYPED_CONDITIONS_VALUES_SATISFIED", "source/a6")

    return {
        "R01": lambda e,c,p: failed("IDENTITY_OR_AUTHORITY_SELF_CLAIM", "claims") if e.get("forbidden_identity_claims") else passed("NO_DERIVED_IDENTITY_OR_AUTHORITY", "claims"),
        "R02": lambda e,c,p: passed("BOUNDARY_COMPONENTS_EXTERNAL", "boundary") if set((e.get("boundary_manifest") or {}).get("external_components", [])) >= {"source","authority_registry","broker","observer","supervisor"} else unknown("BOUNDARY_MANIFEST_INCOMPLETE", "boundary"),
        "R03": lambda e,c,p: failed("STALE_PROPOSAL_AUTHORITY", "source/native") if "STALE_PROPOSAL_AUTHORITY" in p else (passed("SOURCE_AND_NATIVE_BINDINGS_EXACT", "source/native") if c["source_valid"] and e.get("native_binding_status") == "PASS" else unknown("SOURCE_OR_NATIVE_BINDING_UNPROVEN", "source/native")),
        "R04": lambda e,c,p: passed("MISSING_NOT_COERCED_TO_EMPTY", "availability") if e.get("availability_policy") == "MISSING_IS_UNKNOWN" else unknown("AVAILABILITY_POLICY_MISSING", "availability"),
        "R05": lambda e,c,p: (_rr("NOT_APPLICABLE","NO_REPLACEMENT_IN_THIS_TRACE","lifecycle") if e.get("lifecycle_mode") != "REPLACE_PROCESS" else (failed("REPLACEMENT_LIFECYCLE_INVALID","lifecycle") if any(x in p for x in {"MISSING_EXIT_OR_REPLACEMENT","REPLACEMENT_W0_BINDING_UNKNOWN","REPLACEMENT_W0_EXIT_MISSING","REPLACEMENT_W0_START_BINDING_MISMATCH","REPLACEMENT_W1_START_BINDING_MISMATCH","EARLY_REPLACEMENT_START","REUSED_INSTANCE_ID","NO_LIFECYCLE_EVIDENCE"}) else passed("EXACT_W0_EXIT_BEFORE_W1_START","lifecycle"))),
        "R06": lambda e,c,p: (_rr("NOT_APPLICABLE","NOT_A_SHAM_TRACE","lifecycle") if e.get("lifecycle_mode") != "SHAM_BARRIER" else (failed("SHAM_BARRIER_INVALID","lifecycle") if any(x in p for x in {"SHAM_RELEASE_BARRIER_MISSING","SHAM_CONTINUE_BEFORE_RELEASE","SHAM_ACK_BINDING_MISMATCH","LIFECYCLE_REF_SCOPE_MISMATCH"}) else passed("RELEASE_PRECEDES_CONTINUATION","lifecycle"))),
        "R07": lambda e,c,p: failed("OPEN_QSF_NOT_FAITHFULLY_CARRIED","packet") if "qsf" in c["material_mismatches"] else passed("OPEN_QSF_VARIANTS_AND_DISPUTE_CARRIED","packet"),
        "R08": lambda e,c,p: failed("CANDIDATE_RESOLUTION_CLAIM_INVALID","resolution/approvals") if c["precommit_derived"].get("rejected_claims") or any(x in c["precommit_derived"].get("admission_failures",[]) for x in ("SOURCE_RESOLUTION_BINDING_MISMATCH","CANDIDATE_RESOLUTION_UNOBSERVABLE_OR_MALFORMED","DISTINCT_APPROVAL_ROOTS_INSUFFICIENT","APPROVAL_SCOPE_MISMATCH","APPROVAL_ROOT_NOT_ADMITTED")) else passed("SCOPED_RESOLUTION_BASIS_VALID_OR_QSF_OPEN","resolution/approvals"),
        "R09": lambda e,c,p: failed("QSTATE_MEMORY_SEPARATION_VIOLATED","memory") if c["promotion_delta"] not in (None,0) or (e.get("supplied_decision") or {}).get("memory_promotion_authorized") is True else passed("QSTATE_AND_MEMORY_SEPARATE","memory"),
        "R10": lambda e,c,p: unknown("PROMOTION_BASELINE_MISSING","sink") if c["promotion_delta"] is None else (failed("AUTOMATIC_PROMOTION_OBSERVED","sink") if c["promotion_delta"] else passed("NO_AUTOMATIC_ARQ_PROMOTION","sink")),
        "R11": lambda e,c,p: failed("STALE_CURRENT_ATTESTATION","attestation") if "STALE_CURRENT_ATTESTATION" in p else passed("E0_HISTORICAL_E1_CURRENT","attestation"),
        "R12": lambda e,c,p: failed("RECEIVER_OR_APPROVAL_SCOPE_INVALID","receiver/approvals") if c["derived"]["approvals"]["errors"] or "receiver_basis" in c["material_mismatches"] else passed("EXTERNAL_SCOPED_ADMISSION","receiver/approvals"),
        "R13": a6_result,
        "R14": lambda e,c,p: failed("ROLE_OR_CUSTODY_CARRIAGE_MISMATCH","packet") if any(x in c["material_mismatches"] for x in ("role","custody","receiver_basis")) else passed("ROLE_AND_CUSTODY_CARRIED","packet"),
        "R15": lambda e,c,p: failed("UNFINISHED_DUTY_LOST","packet") if "duty" in c["material_mismatches"] else passed("DUTY_AND_LIABILITY_CARRIED","packet"),
        "R16": lambda e,c,p: failed("DISSENT_OR_QUARANTINE_LOST","packet") if any(x in c["material_mismatches"] for x in ("qsf","quarantined_memory")) else passed("DISSENT_AND_RECOURSE_RETAINED","packet"),
        "R17": lambda e,c,p: unknown("CURRENT_REGISTRY_UNKNOWN","registry") if c["derived"]["reason"] == "CURRENT_REGISTRY_UNKNOWN" else (failed("STALE_PROPOSAL_AUTHORITY","registry") if "STALE_PROPOSAL_AUTHORITY" in p else (failed("CURRENT_GRANT_NOT_VALID","registry") if c["source"].get("registry",{}).get("grant_status") != "VALID" else passed("CURRENT_GROUNDING_RECHECKED","registry"))),
        "R18": lambda e,c,p: failed("SURFACE_SCOPE_MISMATCH","surfaces") if "WRONG_SURFACE_INVENTORY" in p or "role" in c["material_mismatches"] or c["source"].get("registry",{}).get("grant_status") != "VALID" else passed("NO_SURFACE_EXPANSION","surfaces"),
        "R19": lambda e,c,p: (_rr("NOT_APPLICABLE","NO_RESOLUTION_APPROVAL_REQUIRED","approvals") if not c["source"].get("resolution") else (failed("DISTINCT_APPROVAL_ROOTS_INSUFFICIENT","approvals") if c["derived"]["approvals"]["count"] < int(c["derived"]["approvals"]["required"] or 0) else passed("DISTINCT_POLICY_ROOTS_SATISFIED","approvals"))),
        "R20": lambda e,c,p: failed("EVIDENCE_PATH_MULTIPLICATION","resolution") if "EVIDENCE_PATH_MULTIPLICATION" in p else (unknown("CANDIDATE_EVIDENCE_PATHS_UNOBSERVABLE","resolution") if "CANDIDATE_RESOLUTION_UNOBSERVABLE_OR_MALFORMED" in c["precommit_derived"].get("admission_failures",[]) else passed("NO_EVIDENCE_MULTIPLICATION","resolution")),
        "R21": lambda e,c,p: failed("SOURCE_PROJECTION_MISMATCH","source/packet") if c["material_mismatches"] else passed("SOURCE_TO_PROJECTION_FIDELITY","source/packet"),
        "R22": lambda e,c,p: passed("PERMISSION_AND_L4_SEPARATE","l4") if c["source"].get("l4",{}).get("state") in {"SUFFICIENT","INSUFFICIENT"} else unknown("L4_STATE_UNKNOWN","l4"),
        "R23": lambda e,c,p: failed("FORBIDDEN_MEMORY_PROMOTION_REQUEST","memory") if c["precommit_derived"].get("rejected_memory_requests") else (passed("QUARANTINED_MEMORY_HAS_NO_ACTION_FORCE","memory") if c["source"].get("quarantined_memory",{}).get("action_force") is False else failed("MEMORY_ACTION_FORCE_RESTORED","memory")),
        "R24": lambda e,c,p: unknown("SINK_BASELINE_OR_COMMIT_MISSING","sink/commit") if c["effect_delta"] is None or not isinstance(e.get("commit_evidence"),dict) else (failed("EXACT_COMMIT_EFFECT_BINDING_INVALID","sink/commit") if e["commit_evidence"].get("atomic_revalidation") is not True or e["commit_evidence"].get("binding_revalidated") is not True or e["commit_evidence"].get("effect_delta") != c["effect_delta"] or any(x in p for x in {"EXPECTED_EFFECT_ROW_MISSING_OR_MISMATCH","UNEXPECTED_EFFECT_ROW","DUPLICATE_EFFECT_FOR_OPERATION","OPERATION_INTENT_MISSING_OR_INVALID","OPERATION_INTENT_SCOPE_OR_BASIS_MISMATCH","OPERATION_INTENT_EFFECT_EXPECTATION_INVALID","UNTRUSTED_EXPECTED_EFFECT_OVERRIDE","CANDIDATE_PROPOSAL_CONTEXT_INVALID","ATOMIC_REVALIDATION_EVIDENCE_INVALID","INCOMPLETE_OBSERVATION_INTERVAL","SURFACE_COVERAGE_INCOMPLETE","WRONG_SURFACE_INVENTORY","DUPLICATED_SURFACE"}) else passed("EXACT_SINGLE_ATOMIC_CONSEQUENCE_BOUNDARY","sink/commit")),
        "R25": lambda e,c,p: (_rr("NOT_APPLICABLE","POSITIVE_EFFECT_TRACE","non-effect") if c["derived"]["gate"] == "ALLOW" else (unknown("NON_EFFECT_COVERAGE_UNKNOWN","non-effect") if c["effect_delta"] is None else (failed("SCOPED_NON_EFFECT_FAILED","non-effect") if c["effect_delta"] != 0 or "INCOMPLETE_OBSERVATION_INTERVAL" in p or "WRONG_SURFACE_INVENTORY" in p else passed("SCOPED_NON_EFFECT_OBSERVED","non-effect")))),
        "R26": lambda e,c,p: failed("WITNESS_ATTEMPT_BINDING_INVALID","refs") if any(x in p for x in {"ATTEMPT_GATE_REF_MISMATCH","FOREIGN_ATTEMPT_REF","RECORD_SCOPE_MISMATCH","EXPECTED_EFFECT_ROW_MISSING_OR_MISMATCH","OPERATION_INTENT_MISSING_OR_INVALID","OPERATION_INTENT_SCOPE_OR_BASIS_MISMATCH","OPERATION_INTENT_EFFECT_EXPECTATION_INVALID","UNTRUSTED_EXPECTED_EFFECT_OVERRIDE","CANDIDATE_PROPOSAL_CONTEXT_INVALID","ATOMIC_REVALIDATION_EVIDENCE_INVALID"}) else passed("EXACT_WITNESS_AND_EFFECT_TO_ATTEMPT_BINDING","refs"),
        "R27": lambda e,c,p: failed(c["atomic_denial"]["reason"],"history") if c["atomic_denial"]["status"] in {"FAIL","UNKNOWN"} else (passed("APPEND_ONLY_REEVALUATION","history") if e.get("append_only_history") is True else unknown("APPEND_ONLY_HISTORY_UNPROVEN","history")),
        "R28": lambda e,c,p: (_rr("NOT_APPLICABLE","RESOLUTION_PROGRESS_NOT_APPLICABLE_TO_THIS_CELL","scope") if e.get("cell_id") not in {"N0","N1","T0"} and not (_legacy_projection(e) and e.get("cell_id") == "synthetic-positive") else (_rr("NOT_APPLICABLE","PREFLIGHT_EXCLUDES_RESOLVED_CHECK","scope") if e.get("evidence_scope") == "PREFLIGHT" else (unknown("RESOLUTION_PROGRESS_OBSERVATION_MISSING","sink") if c["effect_delta"] is None else (unknown("RESOLUTION_PROGRESS_PENDING_AFTER_LAWFUL_OPEN_HOLD","sink") if e.get("checkpoint") == "OPEN_CHECK" and c["derived"]["gate"] == "HOLD" and c["effect_delta"] == 0 else (passed("VALID_RESOLUTION_PROGRESS_OBSERVED","sink") if e.get("checkpoint") == "RESOLVED_CHECK" and c["derived"]["gate"] == "ALLOW" and c["effect_delta"] == 1 else failed("VALID_RESOLUTION_PROGRESS_MISSING","sink")))))),
        "R29": lambda e,c,p: passed("TIMEOUT_NOT_TREATED_AS_KNOWLEDGE","qsf") if not (c["source"].get("semantic_clock",{}).get("tick",0) >= c["source"].get("semantic_clock",{}).get("qsf_expiry_tick",1) and c["derived"]["q_state"] == "COLLAPSED_SCOPED") else failed("TIMEOUT_COLLAPSED_QSTATE","qsf"),
        "R30": lambda e,c,p: passed("OBSERVER_SEPARATE_AND_EVIDENCE_BASED","observer") if e.get("observer_dependencies") == ["common","signing","state_transfer"] and c["events"] is not None else unknown("OBSERVER_SEPARATION_OR_EVIDENCE_UNKNOWN","observer"),
        "R31": lambda e,c,p: unknown("TRACE_COMPLETENESS_UNKNOWN","coverage") if c["before"] is None or c["after"] is None or c["events"] is None else (failed("TRACE_CONTAINS_SUBSTANTIVE_VIOLATION","coverage") if p else passed("ALL_REQUIRED_TRACE_SURFACES_PRESENT","coverage")),
        "R32": lambda e,c,p: passed("AUTHENTICATION_AND_CONTAINMENT_EVIDENCE_PRESENT","signer/isolation") if e.get("signature_controls_status") == "PASS" and e.get("containment_status") == "PASS" else unknown("AUTHENTICATION_OR_CONTAINMENT_UNPROVEN","signer/isolation"),
        "R33": lambda e,c,p: passed("NO_ABSOLUTE_MEMORY_JUDGE","bindings") if e.get("memory_judge_mode") == "EXCLUDED" else failed("ABSOLUTE_MEMORY_JUDGE_PRESENT","bindings"),
        "R34": lambda e,c,p: review_execution_scope(e),
        "R35": lambda e,c,p: passed("CLOCK_DOMAINS_SEPARATE","clocks") if e.get("clock_mapping") == {"semantic":"CGDR_TEST_TICKS","native":"RFC3339","lifecycle":"HOST_PERF_COUNTER_NS"} else unknown("CLOCK_MAPPING_INCOMPLETE","clocks"),
        "R36": lambda e,c,p: passed("IMPLEMENTATION_BINDINGS_CLASSIFIED","bindings") if set(e.get("implementation_classes",[])) >= {"REUSED_UNMODIFIED","BOUNDED_ADAPTER","TEST_DOUBLE","NOT_IMPLEMENTED"} else unknown("IMPLEMENTATION_BINDINGS_INCOMPLETE","bindings"),
    }


def inspect_checkpoint(evidence: dict[str, Any]) -> dict[str, Any]:
    """Observer derives findings from trusted source, chronology and sink rows, never candidate ALLOW/counts."""
    context = _context(evidence)
    problems = _global_problems(evidence, context)
    rules = _rule_functions()
    assertions = []
    for requirement in ALL_REQUIREMENTS:
        result = rules[requirement](evidence, context, problems)
        assertions.append({
            "requirement_id": requirement,
            "value": result.value,
            "evidence_refs": list(result.refs),
            "reason": result.reason,
        })
    values = [item["value"] for item in assertions]
    verdict = "FAIL" if "FAIL" in values else ("INCONCLUSIVE" if "UNKNOWN" in values else "PASS")
    return {
        "observer_status": verdict,
        "conformance_verdict": verdict,
        "problems": problems,
        "actual_effect_delta": context["effect_delta"],
        "actual_promotion_delta": context["promotion_delta"],
        "derived_gate": context["derived"],
        "precommit_derived_gate": context["precommit_derived"],
        "atomic_denial_review": context["atomic_denial"],
        "assertions": assertions,
    }


def inspect_logic_path(open_evidence: dict[str, Any], resolved_evidence: dict[str, Any]) -> dict[str, Any]:
    """Targeted F04/F06/F07 assessment; it is not a selected-process conformance verdict."""
    opened = inspect_checkpoint(open_evidence)
    resolved = inspect_checkpoint(resolved_evidence)
    open_source = open_evidence.get("source_inventory") or {}
    resolved_source = resolved_evidence.get("source_inventory") or {}
    lineage = resolved_source.get("source_lineage") or {}
    checks = {
        "same_qsf": (open_source.get("qsf") or {}).get("qsf_id") == (resolved_source.get("qsf") or {}).get("qsf_id"),
        "append_only_source_link": lineage.get("predecessor_source_hash") == open_source.get("source_hash"),
        "open_hold_zero": opened["derived_gate"]["gate"] == "HOLD" and opened["actual_effect_delta"] == 0,
        "resolved_allow_one": resolved["derived_gate"]["gate"] == "ALLOW" and resolved["actual_effect_delta"] == 1,
        "zero_promotions": opened["actual_promotion_delta"] == 0 and resolved["actual_promotion_delta"] == 0,
        "exact_effect_binding": "EXPECTED_EFFECT_ROW_MISSING_OR_MISMATCH" not in resolved["problems"],
        "native_four_layers": open_evidence.get("native_binding_status") == "PASS" and resolved_evidence.get("native_binding_status") == "PASS",
        "open_r28_pending": next(item for item in opened["assertions"] if item["requirement_id"] == "R28")["reason"] == "RESOLUTION_PROGRESS_PENDING_AFTER_LAWFUL_OPEN_HOLD",
        "resolved_r28_pass": next(item for item in resolved["assertions"] if item["requirement_id"] == "R28")["value"] == "PASS",
    }
    # Applicability is fixed before evaluating values.  R32 requires actual OS
    # containment and is outside this process-free repair; OPEN/R28 is a lawful
    # deferred check that must be discharged by the linked RESOLVED checkpoint.
    applicability = {
        requirement: {
            "scope": "OUT_OF_SCOPE" if requirement == "R32" else "IN_SCOPE",
            "basis": (
                "ACTUAL_OS_AUTHENTICATION_OR_CONTAINMENT_NOT_RUN"
                if requirement == "R32"
                else "OFFLINE_LOGIC_PATH_REQUIREMENT"
            ),
        }
        for requirement in ALL_REQUIREMENTS
    }
    pending_keys = {
        ("OPEN_CHECK", "R28", "RESOLUTION_PROGRESS_PENDING_AFTER_LAWFUL_OPEN_HOLD")
    }
    in_scope_failures: list[dict[str, Any]] = []
    in_scope_unknowns: list[dict[str, Any]] = []
    out_of_scope_unknowns: list[dict[str, Any]] = []
    pending: list[dict[str, Any]] = []
    for checkpoint_name, result in (("OPEN_CHECK", opened), ("RESOLVED_CHECK", resolved)):
        for assertion in result["assertions"]:
            item = {"checkpoint": checkpoint_name, **assertion}
            if assertion["value"] == "UNKNOWN" and applicability[assertion["requirement_id"]]["scope"] == "OUT_OF_SCOPE":
                out_of_scope_unknowns.append(item)
            elif (
                assertion["value"] == "UNKNOWN"
                and (checkpoint_name, assertion["requirement_id"], assertion["reason"]) in pending_keys
            ):
                pending.append(item)
            elif assertion["value"] == "UNKNOWN":
                in_scope_unknowns.append(item)
            elif assertion["value"] == "FAIL" and applicability[assertion["requirement_id"]]["scope"] == "IN_SCOPE":
                in_scope_failures.append(item)
    checks["no_in_scope_failures"] = not in_scope_failures
    checks["no_unresolved_in_scope_unknowns"] = not in_scope_unknowns
    checks["open_pending_discharged_by_resolved"] = bool(pending) and checks["resolved_r28_pass"]
    cross_phase_failure = not checks["same_qsf"] or not checks["append_only_source_link"]
    if in_scope_failures or cross_phase_failure:
        aggregate_status = "FAIL"
    elif in_scope_unknowns:
        aggregate_status = "INCONCLUSIVE"
    else:
        aggregate_status = "PASS"
    return {
        "offline_logic_path_status": aggregate_status,
        "checks": checks,
        "applicability": applicability,
        "in_scope_failures": in_scope_failures,
        "in_scope_unknowns": in_scope_unknowns,
        "out_of_scope_unknowns": out_of_scope_unknowns,
        "pending_then_discharged": pending,
        "open_checkpoint": opened,
        "resolved_checkpoint": resolved,
        "selected_process_conformance": "NOT_RUN",
    }
