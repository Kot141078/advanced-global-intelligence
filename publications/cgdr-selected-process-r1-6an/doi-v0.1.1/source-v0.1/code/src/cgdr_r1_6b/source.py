from __future__ import annotations

from copy import deepcopy
from typing import Any

from .common import canonical_hash


TASK_ID = "CGDR_SELECTED_PROCESS_LOGIC_REPAIR_R1_6F"


CELL_ORDER = [
    "N0", "N1", "T0", "T1", "T2Q", "T2D", "T3", "T4S", "T4R",
    "T5A", "T5E", "T6", "T7", "T8", "T9", "T10", "T11W", "T11E",
]


def immutable_source(cell_id: str) -> dict[str, Any]:
    source: dict[str, Any] = {
        "source_id": f"sealed-source:{cell_id}",
        "semantic_clock": {"domain": "CGDR_TEST_TICKS", "tick": 10, "qsf_expiry_tick": 50},
        "qsf": {
            "qsf_id": f"qsf:{cell_id}",
            "state": "OPEN",
            "variants": [
                {"id": "variant-a", "support_refs": ["evidence:path-a"], "oppose_refs": ["evidence:path-b"]},
                {"id": "variant-b", "support_refs": ["evidence:path-b"], "oppose_refs": ["evidence:path-c"]},
                {"id": "variant-c", "support_refs": ["evidence:path-c"], "oppose_refs": ["evidence:path-a"]},
            ],
            "minority_refs": ["variant-c"],
            "dispute_refs": ["dispute:one"],
            "blocked_actions": ["synthetic_accept"],
            "memory_block": True,
            "collapse_policy": "AUTHORIZED_NEW_SOURCE_DISTINCT_PATH",
        },
        "duty": {"id": "duty:unfinished-one", "status": "PENDING", "liabilities": ["liability:one"]},
        "custody": {"known": True, "holder": "source-custodian", "basis": "independent-current-record"},
        "role": {"name": "bounded-worker", "verbs": ["propose_synthetic_accept"]},
        "receiver_basis": {"issuer": "test-owner", "scope": "selected-process-only", "accepted": True},
        "arq_standing": {
            "status": "STANDING_WITH_OPEN_QSF",
            "history_ref": "arq-history:synthetic-one",
            "current_use_requires_external_attestation": True,
        },
        "registry": {
            "epoch": "E1",
            "authority_version": 1,
            "grant_id": f"grant:{cell_id}:1",
            "grant_status": "VALID",
            "lease": f"lease:{cell_id}:1",
            "scope": "synthetic-sink",
            "task": "synthetic_accept",
        },
        "toy_lineage": {
            "lineage_id": "toy-lineage:explicit-1",
            "w0": "toy-worker-generation-0",
            "w1": "toy-worker-generation-1",
            "basis": "STIPULATED_TEST_LINEAGE_NOT_PID_OR_IDENTITY_PROOF",
        },
        "current_attestation": {"epoch": "E1", "source": "outside-worker-test-trust-service"},
        "attestation_history": [
            {"epoch": "E0", "status": "HISTORICAL_NOT_CURRENT_AFTER_RESET"},
            {"epoch": "E1", "status": "CURRENT", "source": "outside-worker-test-trust-service"},
        ],
        "quarantined_memory": {
            "id": "memory:quarantined-one",
            "state": "QUARANTINED",
            "action_force": False,
            "historical": True,
        },
        "a6_conditions": {
            "decidable": {"type": "DECIDABLE", "status": "RESOLVED"},
            "window": {"type": "WINDOWED", "status": "CLOSED"},
            "escalation": {"type": "ESCALATE_ONLY", "status": "RESOLVED_BY_COMPETENT_SOURCE"},
        },
        "l4": {"state": "SUFFICIENT", "budget": 1, "expiry_tick": 60},
        "surface_inventory": ["synthetic-sink/effects", "synthetic-sink/promotions"],
        "trusted_policy": {
            "policy_id": "policy:selected-process:synthetic-accept:v1",
            "task_id": TASK_ID,
            "protected_action": "synthetic_accept",
            "required_approval_roots": 2,
            "admitted_principal_roots": ["root:alpha", "root:beta"],
            "approval_binding_fields": [
                "task_id", "action", "source_resolution_hash",
                "checkpoint", "instance_id", "attempt_id",
                "operation_id", "commit_record_id",
            ],
        },
        "handoff_authority": {
            "state_transfer_grants_no_authority": True,
            "admission_and_current_registry_remain_external": True,
        },
        "resolution": None,
    }
    source["source_hash"] = canonical_hash(source)
    return source


def resolved_source(source: dict[str, Any]) -> dict[str, Any]:
    result = deepcopy(source)
    result.pop("source_hash", None)
    predecessor_hash = source["source_hash"]
    predecessor_id = source["source_id"]
    result["source_id"] = f"{predecessor_id}:resolved:1"
    result["source_lineage"] = {
        "lineage_id": f"source-lineage:{source['qsf']['qsf_id']}",
        "predecessor_source_id": predecessor_id,
        "predecessor_source_hash": predecessor_hash,
        "transition": "SCOPED_CLARIFICATION_APPEND",
    }
    result["semantic_clock"]["tick"] = 20
    result["resolution"] = {
        "qsf_id": result["qsf"]["qsf_id"],
        "scope": "synthetic_accept",
        "authorized_by": ["root:alpha", "root:beta"],
        "evidence_paths": ["source-event:clarification-alpha", "source-event:clarification-beta"],
        "disposition": "variant-a",
        "source": "test-source-not-worker",
    }
    result["source_hash"] = canonical_hash(result)
    return result


def source_for_fault(cell_id: str, base: dict[str, Any]) -> dict[str, Any]:
    result = deepcopy(base)
    if cell_id in {"T5A", "T10"}:
        result = resolved_source(result)
        result.pop("source_hash", None)
    else:
        result.pop("source_hash", None)
    if cell_id == "T4S":
        result["registry"]["authority_version"] = 2
        result["registry"]["grant_id"] = "grant:T4S:2"
    elif cell_id == "T4R":
        result["registry"]["grant_status"] = "REVOKED"
    elif cell_id == "T7":
        result["current_attestation"]["epoch"] = "E1"
    elif cell_id == "T9":
        result["semantic_clock"]["tick"] = result["semantic_clock"]["qsf_expiry_tick"]
    elif cell_id == "T11W":
        result["a6_conditions"]["window"]["status"] = "OPEN"
    elif cell_id == "T11E":
        result["a6_conditions"]["escalation"]["status"] = "UNRESOLVED"
    result["source_hash"] = canonical_hash(result)
    return result
