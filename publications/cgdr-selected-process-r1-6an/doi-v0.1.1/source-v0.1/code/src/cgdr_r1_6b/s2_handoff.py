from __future__ import annotations

import hashlib
from copy import deepcopy
from pathlib import Path
from typing import Any, TYPE_CHECKING

from .broker import Broker, build_operation_intent
from .common import canonical_hash, write_json
from .producer import make_packet
from .receiver import evaluate
from .signing import TestKeyStore, sign, verify
from .source import TASK_ID as SYNTHETIC_POLICY_TASK_ID, immutable_source
from .state_transfer import MATERIAL_FIELDS, freeze_state, validate_state_bytes

if TYPE_CHECKING:
    from .prospective_observation import ProspectiveObservation


TASK_ID = "CGDR_SELECTED_PROCESS_OPEN_STATE_HANDOFF_S2_R1_6I"
PROFILE_ID = "CGDR-R1.6A-SELECTED-PROCESS"
PROFILE_BINDING = "PROFILE_BINDING_C1"
S2_PLAN_SCHEMA = "TASK_LOCAL_OPEN_STATE_HANDOFF_S2_PLAN_V1"
S2_DELTA_SCHEMA = "TASK_LOCAL_S2_DELTA_PLAN_V1"
S2_STAGE_PREFIX = "/tmp/cgdr-r1-6i-s2-"
PROTECTED_CARRIAGE_FIELDS = (
    "qsf",
    "duty",
    "custody",
    "role",
    "arq_standing",
    "quarantined_memory",
    "a6_conditions",
    "l4",
    "toy_lineage",
    "handoff_authority",
)


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def build_open_prestate(attempt_id: str, w0_instance_id: str) -> dict[str, Any]:
    """Build the single source fixture before W0 starts.

    The policy task namespace is deliberately retained from the accepted F path;
    the outer S2 task and attempt are separate lifecycle bindings.
    """
    source = deepcopy(immutable_source("S2I"))
    source.pop("source_hash", None)
    source["source_id"] = "sealed-source:S2I:open:1"
    source["semantic_clock"] = {"domain": "CGDR_TEST_TICKS", "tick": 10, "qsf_expiry_tick": 80}
    source["qsf"]["qsf_id"] = "qsf:S2I:open:1"
    source["qsf"]["blocked_actions"] = ["synthetic_accept"]
    source["qsf"]["memory_block"] = True
    source["duty"] = {
        "id": "duty:S2I:unfinished:1",
        "status": "PENDING",
        "liabilities": ["liability:S2I:one"],
    }
    source["receiver_basis"] = {
        "issuer": "test-owner",
        "scope": "carried-open-state-context-only",
        "accepted": False,
        "status": "CARRIED_NOT_CURRENT_AUTHORITY",
    }
    source["registry"] = {
        "epoch": "E0",
        "authority_version": 1,
        "grant_id": "grant:S2I:E0",
        "grant_status": "VALID",
        "lease": "lease:S2I:W0",
        "scope": "synthetic-sink",
        "task": "synthetic_accept",
    }
    source["current_attestation"] = {
        "epoch": "E0",
        "source": "outside-worker-test-trust-service",
        "outer_task_id": TASK_ID,
        "attempt_id": attempt_id,
        "instance_id": w0_instance_id,
        "status": "CURRENT_FOR_W0_PRE_FENCE",
    }
    source["attestation_history"] = [{
        "epoch": "E0",
        "status": "CURRENT_FOR_W0_PRE_FENCE",
        "outer_task_id": TASK_ID,
        "attempt_id": attempt_id,
        "instance_id": w0_instance_id,
        "source": "outside-worker-test-trust-service",
    }]
    source["l4"] = {"state": "SUFFICIENT", "budget": 1, "expiry_tick": 60}
    source["resolution"] = None
    source["trusted_policy"]["task_id"] = SYNTHETIC_POLICY_TASK_ID
    source["source_hash"] = canonical_hash(source)
    return source


def build_source_inventory(source: dict[str, Any]) -> dict[str, Any]:
    frozen = freeze_state(source)
    qsf = source["qsf"]
    return {
        "schema": "S2_SOURCE_INVENTORY_V1",
        "outer_task_id": TASK_ID,
        "profile_id": PROFILE_ID,
        "profile_binding": PROFILE_BINDING,
        "source_id": source["source_id"],
        "source_hash": source["source_hash"],
        "material_fields": list(MATERIAL_FIELDS),
        "state_raw_sha256": sha256_bytes(frozen["bytes"]),
        "state_canonical_sha256": frozen["state_sha256"],
        "qsf": {
            "id": qsf["qsf_id"],
            "state": qsf["state"],
            "variant_ids": [item["id"] for item in qsf["variants"]],
            "variant_support_refs": {item["id"]: list(item["support_refs"]) for item in qsf["variants"]},
            "variant_oppose_refs": {item["id"]: list(item["oppose_refs"]) for item in qsf["variants"]},
            "minority_refs": list(qsf["minority_refs"]),
            "dispute_refs": list(qsf["dispute_refs"]),
            "blocked_actions": list(qsf["blocked_actions"]),
            "memory_block": qsf["memory_block"],
        },
        "duty": deepcopy(source["duty"]),
        "custody": deepcopy(source["custody"]),
        "role": deepcopy(source["role"]),
        "arq_standing": deepcopy(source["arq_standing"]),
        "quarantined_memory": deepcopy(source["quarantined_memory"]),
        "a6_conditions": deepcopy(source["a6_conditions"]),
        "l4": deepcopy(source["l4"]),
        "toy_lineage": deepcopy(source["toy_lineage"]),
        "slot_owners": {
            "pre_state": "trusted-source-custodian",
            "q_frame": "trusted-source-custodian",
            "custody_and_duties": "trusted-source-custodian",
            "receiver_basis": "external-receiver-service",
            "current_authority": "external-test-trust-service",
            "effect_sink": "broker-only",
            "promotion_store": "broker-only",
        },
        "claim_boundary": "Bounded source inventory and transport projection; not every native slot is implemented by this local projection.",
    }


def inventory_issues(state: dict[str, Any], inventory: dict[str, Any]) -> list[str]:
    issues: list[str] = []
    if set(state) != set(MATERIAL_FIELDS):
        issues.append("MATERIAL_FIELD_SET_MISMATCH")
    if state.get("source_id") != inventory.get("source_id") or state.get("source_hash") != inventory.get("source_hash"):
        issues.append("SOURCE_ID_OR_HASH_MISMATCH")
    qsf, wanted = state.get("qsf") or {}, inventory.get("qsf") or {}
    if qsf.get("state") != "OPEN" or qsf.get("qsf_id") != wanted.get("id"):
        issues.append("OPEN_QSF_ID_OR_STATE_MISMATCH")
    variants = qsf.get("variants")
    if not isinstance(variants, list) or [item.get("id") for item in variants if isinstance(item, dict)] != wanted.get("variant_ids"):
        issues.append("QSF_VARIANT_INVENTORY_MISMATCH")
    if qsf.get("minority_refs") != wanted.get("minority_refs"):
        issues.append("QSF_MINORITY_INVENTORY_MISMATCH")
    if qsf.get("dispute_refs") != wanted.get("dispute_refs"):
        issues.append("QSF_DISPUTE_INVENTORY_MISMATCH")
    if state.get("duty") != inventory.get("duty"):
        issues.append("DUTY_OR_LIABILITY_INVENTORY_MISMATCH")
    for field in ("custody", "role", "arq_standing", "quarantined_memory", "a6_conditions", "l4", "toy_lineage"):
        if state.get(field) != inventory.get(field):
            issues.append(f"INVENTORY_MISMATCH:{field}")
    return sorted(set(issues))


def build_delta_plan(
    *,
    attempt_id: str,
    worker_role: str,
    stage_dir: str,
    input_sha256: str,
    input_bytes: int,
    checkpoint_canary_windows: str,
    checkpoint_canary_wsl: str,
    private_canary_windows: str,
    private_canary_wsl: str,
) -> dict[str, Any]:
    if worker_role not in {"W0", "W1"}:
        raise ValueError("S2 worker role must be W0 or W1")
    expected_prefix = f"{S2_STAGE_PREFIX}{worker_role.casefold()}-"
    if not stage_dir.startswith(expected_prefix):
        raise ValueError("S2 stage/role prefix mismatch")
    stage = stage_dir.rstrip("/")
    return {
        "schema": S2_DELTA_SCHEMA,
        "task_id": TASK_ID,
        "profile_id": PROFILE_ID,
        "attempt_id": attempt_id,
        "worker_role": worker_role,
        "stage_dir": stage,
        "allowed_commands": (
            ["PING", "S2_DELTA", "LOAD", "CHECKPOINT", "SHAM_WAIT", "RELEASE", "CONTINUE", "STOP"]
            if worker_role == "W0"
            else ["PING", "S2_DELTA", "RESTORE", "CHECKPOINT", "STOP"]
        ),
        "external_masked_targets": {
            "checkpoint_store_canary": {
                "windows_path": checkpoint_canary_windows,
                "wsl_path": checkpoint_canary_wsl,
                "boundary": "/mnt mode-000 tmpfs mask inside worker namespace",
            },
            "private_canary": {
                "windows_path": private_canary_windows,
                "wsl_path": private_canary_wsl,
                "boundary": "/mnt mode-000 tmpfs mask inside worker namespace",
            },
        },
        "probes": [
            {
                "probe_id": f"{worker_role}_D01_INPUT_READ",
                "object_id": "S2_INPUT_FIXTURE",
                "operation": "FILE_READ",
                "expectation": "EXPECT_ALLOW",
                "target": f"{stage}/input_fixture.bin",
                "expected_sha256": input_sha256,
                "expected_bytes": input_bytes,
            },
            {
                "probe_id": f"{worker_role}_D02_INPUT_WRITE_DENY",
                "object_id": "S2_INPUT_FIXTURE",
                "operation": "FILE_APPEND",
                "expectation": "EXPECT_DENY",
                "target": f"{stage}/input_fixture.bin",
            },
            {
                "probe_id": f"{worker_role}_D03_SCRATCH_WRITE_READBACK",
                "object_id": "S2_WORKER_SCRATCH",
                "operation": "SCRATCH_WRITE_READBACK",
                "expectation": "EXPECT_ALLOW",
                "target": f"{stage}/scratch/{worker_role.casefold()}_allowed.bin",
                "write_payload": f"S2_ALLOWED_SCRATCH::{attempt_id}::{worker_role}",
            },
            {
                "probe_id": f"{worker_role}_D04_CHECKPOINT_STORE_WRITE_DENY",
                "object_id": "HOST_CHECKPOINT_STORE_CANARY",
                "operation": "FILE_APPEND",
                "expectation": "EXPECT_DENY",
                "target": checkpoint_canary_wsl,
            },
            {
                "probe_id": f"{worker_role}_D05_PRIVATE_CANARY_READ_DENY",
                "object_id": "HOST_PRIVATE_CANARY",
                "operation": "FILE_READ",
                "expectation": "EXPECT_DENY",
                "target": private_canary_wsl,
            },
        ],
        "claim_boundary": "Only the listed task-local objects and operations are qualified; no S1 replay or broad sandbox certification.",
    }


def make_e0_fence_payload(
    *, attempt_id: str, source: dict[str, Any], w0_binding: dict[str, Any], checkpoint_raw_sha256: str
) -> dict[str, Any]:
    return {
        "record_type": "S2_EPOCH_FENCE_V1",
        "outer_task_id": TASK_ID,
        "attempt_id": attempt_id,
        "epoch": "E0",
        "status": "HISTORICAL_NOT_CURRENT_AFTER_FENCE",
        "instance_id": w0_binding["instance_id"],
        "worker_pid": w0_binding["worker_pid"],
        "worker_start_ticks": w0_binding["worker_start_ticks"],
        "source_id": source["source_id"],
        "source_hash": source["source_hash"],
        "checkpoint_raw_sha256": checkpoint_raw_sha256,
        "authority_effect": "CLOSE_W0_LEASE_AND_CURRENT_USE_ONLY",
        "does_not_resolve_qsf": True,
    }


def make_e1_payload(
    *,
    attempt_id: str,
    w1_binding: dict[str, Any],
    source: dict[str, Any],
    checkpoint_raw_sha256: str,
    checkpoint_canonical_sha256: str,
    fence_envelope: dict[str, Any],
) -> dict[str, Any]:
    return {
        "record_type": "S2_EXTERNAL_ATTESTATION_V1",
        "outer_task_id": TASK_ID,
        "profile_id": PROFILE_ID,
        "profile_binding": PROFILE_BINDING,
        "attempt_id": attempt_id,
        "epoch": "E1",
        "status": "CURRENT_FOR_W1_SCOPED_ADMISSION",
        "instance_id": w1_binding["instance_id"],
        "worker_pid": w1_binding["worker_pid"],
        "worker_start_ticks": w1_binding["worker_start_ticks"],
        "pid_namespace": w1_binding["pid_namespace"],
        "source_id": source["source_id"],
        "source_hash": source["source_hash"],
        "checkpoint_raw_sha256": checkpoint_raw_sha256,
        "checkpoint_canonical_sha256": checkpoint_canonical_sha256,
        "fence_envelope_sha256": canonical_hash(fence_envelope),
        "scope": ["receiver-admission", "proposal-only", "no-protected-effect-authority"],
        "semantic_tick": 45,
        "attestation_kind": "TEST_SERVICE_SIGNED_NOT_TPM_OR_HUMAN_INDEPENDENCE",
    }


def sign_authority_payload(payload: dict[str, Any], keys: TestKeyStore) -> dict[str, Any]:
    return sign(payload, "trust-service-e1", keys.ensure("trust-service-e1"), "root:test-trust-service")


def authority_public_map(keys: TestKeyStore) -> dict[str, Any]:
    return keys.public_map({
        "trust-service-e1": "root:test-trust-service",
        "producer-alpha": "root:alpha",
        "alias-alpha-1": "root:alpha",
        "alias-alpha-2": "root:alpha",
        "approver-beta": "root:beta",
    })


def build_current_source_view(
    restored_state: dict[str, Any],
    *,
    attempt_id: str,
    w1_binding: dict[str, Any],
    e0_fence: dict[str, Any],
    e1_envelope: dict[str, Any],
    public_map: dict[str, Any],
) -> tuple[dict[str, Any], dict[str, Any]]:
    if set(restored_state) != set(MATERIAL_FIELDS):
        raise ValueError("RESTORED_MATERIAL_FIELD_SET_MISMATCH")
    valid, reason = verify(e1_envelope, public_map)
    if not valid:
        raise ValueError(f"E1_SIGNATURE_INVALID:{reason}")
    e1 = e1_envelope["payload"]
    if (
        e1.get("outer_task_id") != TASK_ID
        or e1.get("attempt_id") != attempt_id
        or e1.get("instance_id") != w1_binding.get("instance_id")
        or e1.get("worker_pid") != w1_binding.get("worker_pid")
        or e1.get("worker_start_ticks") != w1_binding.get("worker_start_ticks")
        or e1.get("epoch") != "E1"
    ):
        raise ValueError("E1_SCOPE_BINDING_MISMATCH")
    carried_id, carried_hash = restored_state["source_id"], restored_state["source_hash"]
    source = deepcopy(restored_state)
    source["source_id"] = f"{carried_id}:current-view:E1"
    source["source_lineage"] = {
        "lineage_id": f"source-lineage:{restored_state['qsf']['qsf_id']}",
        "predecessor_source_id": carried_id,
        "predecessor_source_hash": carried_hash,
        "transition": "EXTERNAL_EPOCH_REQUALIFICATION_NO_QSF_RESOLUTION",
        "fence_envelope_sha256": canonical_hash(e0_fence),
        "attestation_envelope_sha256": canonical_hash(e1_envelope),
    }
    source["receiver_basis"] = {
        "issuer": "outside-worker-test-trust-service",
        "scope": "proposal-only-open-state-hold",
        "accepted": True,
        "outer_task_id": TASK_ID,
        "attempt_id": attempt_id,
        "instance_id": w1_binding["instance_id"],
        "attestation_envelope_sha256": canonical_hash(e1_envelope),
    }
    source["attestation_history"] = deepcopy(restored_state["attestation_history"]) + [
        {
            "epoch": "E0",
            "status": "HISTORICAL_NOT_CURRENT_AFTER_FENCE",
            "fence_envelope_sha256": canonical_hash(e0_fence),
        },
        {
            "epoch": "E1",
            "status": "CURRENT_FOR_W1_SCOPED_ADMISSION",
            "attestation_envelope_sha256": canonical_hash(e1_envelope),
        },
    ]
    source["semantic_clock"] = {"domain": "CGDR_TEST_TICKS", "tick": 45, "qsf_expiry_tick": 80}
    source["registry"] = {
        "epoch": "E1",
        "authority_version": 2,
        "grant_id": "grant:S2I:E1:proposal-only",
        "grant_status": "VALID",
        "lease": f"lease:S2I:{w1_binding['instance_id']}",
        "scope": "synthetic-sink",
        "task": "synthetic_accept",
    }
    source["current_attestation"] = {
        "epoch": "E1",
        "source": "outside-worker-test-trust-service",
        "envelope_sha256": canonical_hash(e1_envelope),
        "scope": list(e1["scope"]),
    }
    source["surface_inventory"] = ["synthetic-sink/effects", "synthetic-sink/promotions"]
    source["trusted_policy"] = deepcopy(immutable_source("S2I")["trusted_policy"])
    source["trusted_policy"]["task_id"] = SYNTHETIC_POLICY_TASK_ID
    source["resolution"] = None
    source.pop("source_hash", None)
    source["source_hash"] = canonical_hash(source)
    protected_changes = [field for field in PROTECTED_CARRIAGE_FIELDS if source.get(field) != restored_state.get(field)]
    if protected_changes:
        raise ValueError(f"E1_OVERLAY_CHANGED_CARRIED_MATERIAL:{protected_changes}")
    transition = {
        "prestate_source_id": carried_id,
        "prestate_source_hash": carried_hash,
        "current_source_id": source["source_id"],
        "current_source_hash": source["source_hash"],
        "e0_status": "HISTORICAL_NOT_CURRENT_AFTER_FENCE",
        "e1_status": "CURRENT_FOR_W1_SCOPED_ADMISSION",
        "protected_carriage_fields_unchanged": list(PROTECTED_CARRIAGE_FIELDS),
        "receiver_basis_recomputed_externally": True,
        "resolution_added": False,
    }
    return source, transition


def run_hold_gate(
    *,
    database: Path | None = None,
    broker: Broker | None = None,
    observation: ProspectiveObservation | None = None,
    source: dict[str, Any],
    keys: TestKeyStore,
    public_map: dict[str, Any],
    attempt_id: str,
    instance_id: str,
    intent_capture_path: Path | None = None,
) -> dict[str, Any]:
    operation_id = f"operation:{attempt_id}:open-hold"
    commit_record_id = f"commit:{attempt_id}:open-hold"
    checkpoint = "S2_OPEN_CHECK"
    cell_id = "S2_OPEN_HANDOFF"
    owns_broker = broker is None
    if broker is None:
        if database is None:
            raise ValueError("database or pre-created broker is required")
        broker = Broker(database)
    elif database is not None and broker.path.resolve() != database.resolve():
        raise ValueError("PRECREATED_BROKER_DATABASE_MISMATCH")
    if observation is not None:
        if observation.broker is not broker or observation.database != broker.path.resolve():
            raise ValueError("OBSERVATION_BROKER_BINDING_MISMATCH")
        planned_scope = observation.plan["expected_operation_intent"]["scope"]
        actual_scope = {
            "task_id": source["trusted_policy"]["task_id"],
            "action": source["trusted_policy"]["protected_action"],
            "operation_id": operation_id,
            "cell_id": cell_id,
            "attempt_id": attempt_id,
            "checkpoint": checkpoint,
            "instance_id": instance_id,
            "commit_record_id": commit_record_id,
        }
        if planned_scope != actual_scope:
            raise ValueError("OBSERVATION_OPERATION_INTENT_BINDING_MISMATCH")
    try:
        if observation is not None:
            observation.require_admission("PROTECTED_GATE")
        observation_before = observation.begin_phase(checkpoint) if observation is not None else None
        broker.bind_instance(source, instance_id)
        packet = make_packet(
            cell_id,
            source,
            keys,
            checkpoint,
            instance_id=instance_id,
            attempt_id=attempt_id,
            operation_id=operation_id,
            commit_record_id=commit_record_id,
        )
        decision = evaluate(packet, source, public_map)
        proposal = packet["envelope"]["payload"]
        intent = build_operation_intent(
            operation_id,
            cell_id,
            proposal["proposal_hash"],
            source,
            instance_id,
            attempt_id,
            checkpoint,
            commit_record_id,
            expect_effect=False,
        )
        if intent_capture_path is not None:
            write_json(intent_capture_path, {
                "outer_task_id": TASK_ID,
                "attempt_id": attempt_id,
                "capture_stage": "PRE_COMMIT",
                "operation_intent": intent,
                "operation_intent_hash": canonical_hash(intent),
            })
        broker_before = broker.snapshot()
        before = (
            {
                "operations": broker_before["operations"],
                "effects": observation_before["tables"]["effects"]["rows"],
                "promotions": observation_before["tables"]["promotions"]["rows"],
                "observation_snapshot_id": observation_before["snapshot_id"],
            }
            if observation_before is not None else broker_before
        )
        transaction_id = f"observation-txn:{attempt_id}:{checkpoint}:{operation_id}"
        if observation is not None:
            observation.begin_writer_transaction(
                transaction_id,
                operation_id=operation_id,
                interface="Broker.atomic_commit",
            )
        try:
            result = broker.atomic_commit(
                operation_id,
                cell_id,
                proposal["proposal_hash"],
                decision,
                source,
                instance_id,
                operation_context=intent,
                proposal_envelope=packet["envelope"],
                public_signer_map=public_map,
            )
        except BaseException as exc:
            if observation is not None:
                observation.finish_writer_transaction(
                    transaction_id,
                    "ROLLED_BACK",
                    reason=f"{type(exc).__name__}:{exc}",
                )
            raise
        else:
            if observation is not None:
                observation.finish_writer_transaction(transaction_id, "COMMITTED")
        observation_after = observation.end_phase(checkpoint) if observation is not None else None
        broker_after = broker.snapshot()
        after = (
            {
                "operations": broker_after["operations"],
                "effects": observation_after["tables"]["effects"]["rows"],
                "promotions": observation_after["tables"]["promotions"]["rows"],
                "observation_snapshot_id": observation_after["snapshot_id"],
            }
            if observation_after is not None else broker_after
        )
        return {
            "operation_id": operation_id,
            "commit_record_id": commit_record_id,
            "checkpoint": checkpoint,
            "packet": packet,
            "packet_projection": proposal,
            "decision": decision,
            "operation_intent": intent,
            "operation_intent_hash": canonical_hash(intent),
            "sink_before": before,
            "broker_result": result,
            "sink_after": after,
            "effect_row": None,
            "effect_intent_id": f"effect:{operation_id}",
            "retry_path_state": "ABSENT_NO_QUEUE_OR_RETRY_PRIMITIVE",
            "prospective_observation": (
                None if observation is None else deepcopy(observation.export_evidence()["phases"][checkpoint])
            ),
        }
    finally:
        if owns_broker:
            broker.close()


def validate_carried_state(raw: bytes, source: dict[str, Any], inventory: dict[str, Any]) -> dict[str, Any]:
    result = validate_state_bytes(raw, source, stated_hash=sha256_bytes(raw))
    # validate_state_bytes's state hash is the canonical object hash. Raw bytes are
    # canonical in this profile, so both domains intentionally coincide here.
    state = result.get("state") if isinstance(result.get("state"), dict) else {}
    issues = list(result.get("issues") or []) + inventory_issues(state, inventory)
    return {**result, "status": "PASS" if not issues else "FAIL", "issues": sorted(set(issues))}
