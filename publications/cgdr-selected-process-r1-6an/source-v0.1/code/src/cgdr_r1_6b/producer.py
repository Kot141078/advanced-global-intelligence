from __future__ import annotations

from copy import deepcopy
from typing import Any

from .common import canonical_hash
from .signing import TestKeyStore, sign
from .source import TASK_ID
from .state_transfer import material_projection


def _projection(
    source: dict[str, Any],
    cell_id: str,
    checkpoint: str,
    instance_id: str,
    attempt_id: str,
    operation_id: str,
    commit_record_id: str,
) -> dict[str, Any]:
    proposal = material_projection(source)
    proposal.update({
        "cell_id": cell_id,
        "task_id": TASK_ID,
        "action": source["trusted_policy"]["protected_action"],
        "checkpoint": checkpoint,
        "instance_id": instance_id,
        "attempt_id": attempt_id,
        "operation_id": operation_id,
        "commit_record_id": commit_record_id,
        "authority_version": source["registry"]["authority_version"],
        "grant_id": source["registry"]["grant_id"],
        "attestation_epoch": source["current_attestation"]["epoch"],
        "resolution": deepcopy(source["resolution"]),
        "memory_request": "NO_PROMOTION",
        "surface_inventory": deepcopy(source["surface_inventory"]),
    })
    return proposal


def make_packet(
    cell_id: str,
    source: dict[str, Any],
    keys: TestKeyStore,
    checkpoint: str,
    *,
    instance_id: str,
    attempt_id: str,
    operation_id: str | None = None,
    commit_record_id: str | None = None,
) -> dict[str, Any]:
    """Create a signed proposal whose protected scope names one operation.

    The deterministic defaults keep the retained receiver-only fixtures callable;
    any broker call under a different operation identifier still fails closed.
    """
    bound_operation_id = operation_id or f"operation:{attempt_id}"
    bound_commit_record_id = commit_record_id or f"{attempt_id}:commit"
    proposal = _projection(
        source,
        cell_id,
        checkpoint,
        instance_id,
        attempt_id,
        bound_operation_id,
        bound_commit_record_id,
    )
    if cell_id == "T1":
        proposal.pop("receiver_basis")
    elif cell_id == "T2Q":
        proposal.pop("qsf")
        proposal["qsf_projection"] = "KNOWN_EMPTY"
    elif cell_id == "T2D":
        proposal["qsf"]["variants"] = proposal["qsf"]["variants"][:2]
        proposal["qsf"]["minority_refs"] = []
        proposal["qsf"]["dispute_refs"] = []
    elif cell_id == "T3":
        proposal.pop("duty")
    elif cell_id == "T4S":
        proposal["authority_version"] = 1
        proposal["grant_id"] = "grant:T4S:1"
    elif cell_id == "T5E":
        proposal["resolution"] = {
            "qsf_id": source["qsf"]["qsf_id"], "scope": "synthetic_accept",
            "authorized_by": ["root:alpha", "root:alpha", "root:alpha"],
            "evidence_paths": ["evidence:path-a", "evidence:path-a", "evidence:path-a"],
            "disposition": "variant-a", "source": "candidate-copy",
        }
    elif cell_id == "T6":
        proposal["role"]["verbs"].append("synthetic_publish")
    elif cell_id == "T7":
        proposal["attestation_epoch"] = "E0"
    elif cell_id == "T8":
        proposal["memory_request"] = "PROMOTE_QUARANTINED_TO_CONFIRMED_EA"

    proposal["proposal_hash"] = canonical_hash(proposal)
    producer_key = keys.ensure("producer-alpha")
    envelope = sign(proposal, "producer-alpha", producer_key, "root:alpha")

    approvals: list[dict[str, Any]] = []
    resolution = proposal.get("resolution")
    if resolution:
        approval_payload = {
            "task_id": TASK_ID,
            "action": source["trusted_policy"]["protected_action"],
            "source_resolution_hash": canonical_hash(resolution),
            "checkpoint": checkpoint,
            "instance_id": instance_id,
            "attempt_id": attempt_id,
            "operation_id": bound_operation_id,
            "commit_record_id": bound_commit_record_id,
        }
        if cell_id == "T5A":
            for key_id in ("producer-alpha", "alias-alpha-1", "alias-alpha-2"):
                approvals.append(sign(approval_payload, key_id, keys.ensure(key_id), "root:alpha"))
        else:
            approvals.append(sign(approval_payload, "producer-alpha", keys.ensure("producer-alpha"), "root:alpha"))
            approvals.append(sign(approval_payload, "approver-beta", keys.ensure("approver-beta"), "root:beta"))
    return {"envelope": envelope, "approvals": approvals, "transport_hash": canonical_hash({"envelope": envelope, "approvals": approvals})}
