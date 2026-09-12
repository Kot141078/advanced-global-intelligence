from __future__ import annotations

from typing import Any

from .common import canonical_hash
from .signing import verify


def _approval_state(packet: dict[str, Any], proposal: dict[str, Any], source: dict[str, Any], public_map: dict[str, Any]) -> dict[str, Any]:
    policy = source["trusted_policy"]
    resolution = proposal.get("resolution")
    expected = {
        "task_id": proposal.get("task_id"),
        "action": proposal.get("action"),
        "source_resolution_hash": canonical_hash(resolution) if isinstance(resolution, dict) else None,
        "checkpoint": proposal.get("checkpoint"),
        "instance_id": proposal.get("instance_id"),
        "attempt_id": proposal.get("attempt_id"),
        "operation_id": proposal.get("operation_id"),
        "commit_record_id": proposal.get("commit_record_id"),
    }
    roots: set[str] = set()
    errors: list[str] = []
    for envelope in packet.get("approvals", []):
        valid, reason = verify(envelope, public_map)
        if not valid:
            errors.append(reason)
            continue
        if envelope.get("payload") != expected:
            errors.append("APPROVAL_SCOPE_MISMATCH")
            continue
        root = envelope.get("protected", {}).get("principal_root")
        if root not in policy["admitted_principal_roots"]:
            errors.append("APPROVAL_ROOT_NOT_ADMITTED")
            continue
        roots.add(root)
    return {"roots": sorted(roots), "errors": sorted(set(errors)), "expected": expected}


def evaluate(packet: dict[str, Any], source: dict[str, Any], public_map: dict[str, Any]) -> dict[str, Any]:
    failures: list[str] = []
    envelope = packet.get("envelope", {})
    sig_ok, sig_reason = verify(envelope, public_map)
    proposal = envelope.get("payload", {})
    if not sig_ok:
        failures.append(sig_reason)
    stated_hash = proposal.get("proposal_hash")
    unhashed = dict(proposal)
    unhashed.pop("proposal_hash", None)
    if stated_hash != canonical_hash(unhashed):
        failures.append("PROPOSAL_HASH_MISMATCH")
    if packet.get("transport_hash") != canonical_hash({"envelope": envelope, "approvals": packet.get("approvals", [])}):
        failures.append("TRANSPORT_HASH_MISMATCH")
    policy = source["trusted_policy"]
    if proposal.get("task_id") != policy["task_id"] or proposal.get("action") != policy["protected_action"]:
        failures.append("PROPOSAL_POLICY_SCOPE_MISMATCH")
    if not all(
        isinstance(proposal.get(name), str) and proposal.get(name)
        for name in ("checkpoint", "instance_id", "attempt_id", "operation_id", "commit_record_id")
    ):
        failures.append("PROPOSAL_RUNTIME_SCOPE_MISSING")
    if proposal.get("source_id") != source.get("source_id") or proposal.get("source_hash") != source.get("source_hash"):
        failures.append("SOURCE_BINDING_MISMATCH")
    if proposal.get("receiver_basis") != source.get("receiver_basis"):
        failures.append("RECEIVER_BASIS_MISSING_OR_CHANGED")
    if proposal.get("custody") != source.get("custody"):
        failures.append("CUSTODY_CARRIAGE_MISMATCH")
    if proposal.get("role") != source.get("role"):
        failures.append("ROLE_SURFACE_MISMATCH")
    if proposal.get("duty") != source.get("duty"):
        failures.append("DUTY_CARRIAGE_MISMATCH")
    qsf, source_qsf = proposal.get("qsf"), source.get("qsf")
    if not isinstance(qsf, dict):
        q_state = "UNKNOWN"
        failures.append("ACTIVE_QSF_MISSING")
    elif any(qsf.get(name) != source_qsf.get(name) for name in ("variants", "minority_refs", "dispute_refs")):
        q_state = "OPEN_INCOMPLETE"
        failures.append("QSF_VARIANT_OR_DISPUTE_INCOMPLETE")
    else:
        q_state = "OPEN"
    registry = source["registry"]
    if proposal.get("authority_version") != registry["authority_version"] or proposal.get("grant_id") != registry["grant_id"]:
        failures.append("CURRENT_AUTHORITY_VERSION_MISMATCH")
    if registry["grant_status"] != "VALID":
        failures.append("CURRENT_GRANT_REVOKED")
    if proposal.get("attestation_epoch") != source["current_attestation"]["epoch"]:
        failures.append("CURRENT_ATTESTATION_MISMATCH")
    if proposal.get("surface_inventory") != source["surface_inventory"]:
        failures.append("SURFACE_INVENTORY_MISMATCH")
    for name, condition in source["a6_conditions"].items():
        if condition["type"] == "WINDOWED" and condition["status"] != "CLOSED":
            failures.append(f"A6_WINDOWED_OPEN:{name}")
        if condition["type"] == "ESCALATE_ONLY" and condition["status"] != "RESOLVED_BY_COMPETENT_SOURCE":
            failures.append(f"A6_ESCALATION_UNRESOLVED:{name}")

    resolution = proposal.get("resolution")
    approval_state = _approval_state(packet, proposal, source, public_map)
    failures.extend(approval_state["errors"])
    required = int(policy["required_approval_roots"])
    source_resolution = source.get("resolution")
    rejected_claims: list[str] = []
    rejected_memory_requests: list[str] = []
    paths = resolution.get("evidence_paths") if isinstance(resolution, dict) else None
    claim_visible = bool(
        isinstance(resolution, dict) and isinstance(paths, list) and paths
        and all(isinstance(path, str) and path for path in paths)
        and resolution.get("qsf_id") == source["qsf"]["qsf_id"]
        and resolution.get("scope") == policy["protected_action"]
        and isinstance(resolution.get("authorized_by"), list)
        and all(isinstance(root, str) and root for root in resolution["authorized_by"])
        and isinstance(resolution.get("disposition"), str) and resolution["disposition"]
        and isinstance(resolution.get("source"), str) and resolution["source"]
    )
    resolution_matches = bool(
        claim_visible and resolution == source_resolution
        and len(set(paths)) >= 2
        and resolution.get("source") == "test-source-not-worker"
    )
    if "resolution" not in proposal or (resolution is not None and not claim_visible):
        failures.append("CANDIDATE_RESOLUTION_UNOBSERVABLE_OR_MALFORMED")
    if resolution is not None and len(approval_state["roots"]) < required:
        failures.append("DISTINCT_APPROVAL_ROOTS_INSUFFICIENT")
    if resolution != source_resolution or (resolution is not None and not resolution_matches):
        # Reject a visible claim separately from an otherwise valid OPEN
        # handoff. Core/approval defects and resolved-source mismatches deny.
        if source_resolution is None and claim_visible and not failures:
            rejected_claims.append("SOURCE_RESOLUTION_BINDING_MISMATCH")
            if len(paths) != len(set(paths)):
                rejected_claims.append("EVIDENCE_PATH_MULTIPLICATION")
        else:
            failures.append("SOURCE_RESOLUTION_BINDING_MISMATCH")
    request = proposal.get("memory_request")
    if request == "PROMOTE_QUARANTINED_TO_CONFIRMED_EA":
        rejected_memory_requests.append(request)
    elif request != "NO_PROMOTION":
        failures.append("MEMORY_REQUEST_UNOBSERVABLE_OR_UNSUPPORTED")
    valid_resolution = resolution_matches and not approval_state["errors"] and len(approval_state["roots"]) >= required
    if valid_resolution and q_state == "OPEN":
        q_state = "COLLAPSED_SCOPED"
    elif source["semantic_clock"]["tick"] >= source["semantic_clock"]["qsf_expiry_tick"] and q_state == "OPEN":
        q_state = "EXPIRED_UNRESOLVED"

    hard_deny = any(name in failures for name in (
        "CURRENT_GRANT_REVOKED", "CURRENT_ATTESTATION_MISMATCH", "DISTINCT_APPROVAL_ROOTS_INSUFFICIENT",
        "APPROVAL_SCOPE_MISMATCH", "APPROVAL_ROOT_NOT_ADMITTED", "SOURCE_RESOLUTION_BINDING_MISMATCH",
        "CANDIDATE_RESOLUTION_UNOBSERVABLE_OR_MALFORMED", "MEMORY_REQUEST_UNOBSERVABLE_OR_UNSUPPORTED",
    ))
    admitted = not failures
    if hard_deny:
        gate = "DENY"
    elif admitted and not rejected_claims and not rejected_memory_requests and q_state == "COLLAPSED_SCOPED" and source["l4"]["state"] == "SUFFICIENT":
        gate = "ALLOW"
    else:
        gate = "HOLD"
    binding = {
        "task_id": proposal.get("task_id"), "action": proposal.get("action"), "source_hash": proposal.get("source_hash"),
        "source_resolution_hash": canonical_hash(source_resolution) if isinstance(source_resolution, dict) else None,
        "checkpoint": proposal.get("checkpoint"), "instance_id": proposal.get("instance_id"),
        "attempt_id": proposal.get("attempt_id"), "operation_id": proposal.get("operation_id"),
        "commit_record_id": proposal.get("commit_record_id"), "proposal_hash": stated_hash,
        "policy_hash": canonical_hash(policy), "verified_approval_roots": approval_state["roots"],
    }
    return {
        "admission": "ADMITTED" if admitted else "WITHHELD", "q_state": q_state, "action_gate": gate,
        "failures": sorted(set(failures)), "signature_status": sig_reason,
        "distinct_approval_roots": len(approval_state["roots"]), "approval_roots": approval_state["roots"],
        "memory_promotion_authorized": False, "verified_binding": binding,
        "rejected_claims": rejected_claims,
        "candidate_resolution_hash": canonical_hash(resolution) if isinstance(resolution, dict) else None,
        "rejected_memory_requests": rejected_memory_requests,
    }
