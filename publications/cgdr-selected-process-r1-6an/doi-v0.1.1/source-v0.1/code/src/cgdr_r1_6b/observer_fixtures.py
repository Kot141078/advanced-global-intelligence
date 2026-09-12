from __future__ import annotations

from copy import deepcopy
from pathlib import Path
from typing import Any, Callable

from .broker import build_operation_intent
from .common import canonical_hash
from .observer import inspect_checkpoint
from .signing import TestKeyStore, sign
from .source import TASK_ID, immutable_source, resolved_source
from .state_transfer import material_projection


ATTEMPT_ID = "synthetic-regression-attempt-1"
CHECKPOINT = "RESOLVED_CHECK"
INSTANCE_ID = "synthetic-worker-w1"


def _rehash_source(source: dict[str, Any]) -> None:
    source.pop("source_hash", None)
    source["source_hash"] = canonical_hash(source)


def _reproject(evidence: dict[str, Any]) -> None:
    packet = material_projection(evidence["source_inventory"])
    evidence["materialized_packet"] = packet
    evidence["materialized_packet_hash"] = canonical_hash(packet)


def _refresh_intent(evidence: dict[str, Any], *, expect_effect: bool) -> None:
    intent = build_operation_intent(
        evidence["operation_id"],
        evidence["cell_id"],
        evidence["proposal_hash"],
        evidence["source_inventory"],
        evidence["active_instance_id"],
        evidence["attempt_id"],
        evidence["checkpoint"],
        evidence["commit_record_id"],
        expect_effect=expect_effect,
    )
    evidence["operation_intent"] = intent
    evidence["operation_intent_hash"] = canonical_hash(intent)
    evidence["expected_effect_row"] = deepcopy(intent["expected_effect_row"])


def positive_trace(key_root: Path) -> dict[str, Any]:
    """Complete process-free trace used only to test the observer itself."""
    source = resolved_source(immutable_source("SYNTHETIC_OBSERVER_POSITIVE"))
    store = TestKeyStore(key_root)
    bindings = {"approval-alpha": "root:alpha", "approval-beta": "root:beta"}
    public_map = store.public_map(bindings)
    operation_id = "synthetic-operation-1"
    cell_id = "synthetic-positive"
    proposal_hash = "fixture-proposal-hash"
    commit_id = f"{ATTEMPT_ID}:commit:1"
    payload = {
        "task_id": TASK_ID,
        "action": "synthetic_accept",
        "source_resolution_hash": canonical_hash(source["resolution"]),
        "checkpoint": CHECKPOINT,
        "instance_id": INSTANCE_ID,
        "attempt_id": ATTEMPT_ID,
        "operation_id": operation_id,
        "commit_record_id": commit_id,
    }
    approvals = [
        sign(payload, key_id, store.ensure(key_id), root)
        for key_id, root in bindings.items()
    ]
    packet = material_projection(source)
    ref = {"task_id": TASK_ID, "attempt_id": ATTEMPT_ID, "checkpoint": CHECKPOINT}
    expected_effect = {
        "effect_id": f"effect:{operation_id}",
        "operation_id": operation_id,
        "cell_id": cell_id,
        "payload": {
            "kind": "SYNTHETIC_ACCEPT", "task_id": TASK_ID, "action": "synthetic_accept",
            "operation_id": operation_id, "cell_id": cell_id,
            "attempt_id": ATTEMPT_ID, "checkpoint": CHECKPOINT, "instance_id": INSTANCE_ID,
            "commit_record_id": commit_id, "proposal_hash": proposal_hash,
            "source_id": source["source_id"],
            "source_hash": source["source_hash"],
            "source_resolution_hash": canonical_hash(source["resolution"]),
            "policy_hash": canonical_hash(source["trusted_policy"]),
        },
    }
    evidence = {
        "fixture_origin": "SYNTHETIC_REGRESSION_PROCESS_FREE",
        "task_id": TASK_ID,
        "attempt_id": ATTEMPT_ID,
        "checkpoint": CHECKPOINT,
        "operation_id": operation_id,
        "cell_id": cell_id,
        "proposal_hash": proposal_hash,
        "active_instance_id": INSTANCE_ID,
        "source_inventory": source,
        "materialized_packet": packet,
        "materialized_packet_hash": canonical_hash(packet),
        "current_registry": deepcopy(source["registry"]),
        "public_signer_map": public_map,
        "approval_envelopes": approvals,
        "supplied_decision": {"action_gate": "ALLOW", "q_state": "COLLAPSED_SCOPED"},
        "lifecycle_mode": "REPLACE_PROCESS",
        "expected_w0_lifecycle_binding": {
            "instance_id": "synthetic-worker-w0", "os_handle_id": "synthetic-handle-w0",
            "start_evidence_ref": "synthetic-start-w0",
        },
        "trusted_chronology": [
            {**ref, "kind": "PROCESS_START_REQUESTED", "instance_id": "synthetic-worker-w0", "os_handle_id": "synthetic-handle-w0", "start_evidence_ref": "synthetic-start-w0", "host_ns": 10},
            {**ref, "kind": "READY", "instance_id": "synthetic-worker-w0", "os_handle_id": "synthetic-handle-w0", "start_evidence_ref": "synthetic-start-w0", "host_ns": 11},
            {**ref, "kind": "EXIT_OBSERVED", "instance_id": "synthetic-worker-w0", "os_handle_id": "synthetic-handle-w0", "start_evidence_ref": "synthetic-start-w0", "host_ns": 12},
            {**ref, "kind": "PROCESS_START_REQUESTED", "instance_id": INSTANCE_ID, "host_ns": 13},
            {**ref, "kind": "READY", "instance_id": INSTANCE_ID, "host_ns": 14},
        ],
        "sink_before_snapshot": {"effects": [], "promotions": []},
        "sink_after_snapshot": {
            "effects": [expected_effect],
            "promotions": [],
        },
        "expected_effect_row": expected_effect,
        "commit_record_id": commit_id,
        "attempt_ref": commit_id,
        "gate_record_ref": commit_id,
        "record_scope": ref,
        "commit_evidence": {"atomic_revalidation": True, "binding_revalidated": True, "effect_delta": 1},
        "observation_interval": {"domain": "HOST_PERF_COUNTER_NS", "start_ns": 10, "end_ns": 20},
        "surface_observations": [
            {"coordinate": coordinate, "before_ref": f"before:{index}", "after_ref": f"after:{index}"}
            for index, coordinate in enumerate(source["surface_inventory"])
        ],
        "forbidden_identity_claims": [],
        "boundary_manifest": {"external_components": ["source", "authority_registry", "broker", "observer", "supervisor"]},
        "native_binding_status": "PASS",
        "availability_policy": "MISSING_IS_UNKNOWN",
        "append_only_history": True,
        "evidence_scope": "SYNTHETIC_REGRESSION",
        "observer_dependencies": ["common", "signing", "state_transfer"],
        "signature_controls_status": "PASS",
        "containment_status": "PASS",
        "memory_judge_mode": "EXCLUDED",
        "measured_matrix_started": False,
        "clock_mapping": {"semantic": "CGDR_TEST_TICKS", "native": "RFC3339", "lifecycle": "HOST_PERF_COUNTER_NS"},
        "implementation_classes": ["REUSED_UNMODIFIED", "BOUNDED_ADAPTER", "TEST_DOUBLE", "NOT_IMPLEMENTED"],
    }
    _refresh_intent(evidence, expect_effect=True)
    return evidence


def _open_source(evidence: dict[str, Any]) -> None:
    source = immutable_source("SYNTHETIC_OPEN")
    evidence["source_inventory"] = source
    evidence["current_registry"] = deepcopy(source["registry"])
    evidence["approval_envelopes"] = []
    evidence["supplied_decision"] = {"action_gate": "HOLD", "q_state": "OPEN"}
    evidence["sink_after_snapshot"] = {"effects": [], "promotions": []}
    evidence["expected_effect_row"] = None
    evidence["commit_evidence"] = {"atomic_revalidation": True, "binding_revalidated": True, "effect_delta": 0}
    _reproject(evidence)
    _refresh_intent(evidence, expect_effect=False)


def _sham_late_release(evidence: dict[str, Any]) -> None:
    ref = {"task_id": TASK_ID, "attempt_id": ATTEMPT_ID, "checkpoint": CHECKPOINT}
    evidence["lifecycle_mode"] = "SHAM_BARRIER"
    evidence["trusted_chronology"] = [
        {**ref, "kind": "PROCESS_START_REQUESTED", "instance_id": INSTANCE_ID},
        {**ref, "kind": "CONTINUED", "instance_id": INSTANCE_ID},
        {**ref, "kind": "RELEASED", "instance_id": INSTANCE_ID},
    ]


def _packet_loses_qsf_and_duty(evidence: dict[str, Any]) -> None:
    evidence["materialized_packet"].pop("qsf", None)
    evidence["materialized_packet"].pop("duty", None)
    evidence["materialized_packet_hash"] = canonical_hash(evidence["materialized_packet"])


def _revoke_source(evidence: dict[str, Any]) -> None:
    source = evidence["source_inventory"]
    source["registry"]["grant_status"] = "REVOKED"
    _rehash_source(source)
    evidence["current_registry"] = deepcopy(source["registry"])
    _reproject(evidence)
    _refresh_intent(evidence, expect_effect=True)
    evidence["supplied_decision"] = {"action_gate": "ALLOW", "q_state": "COLLAPSED_SCOPED"}


def _same_foreign_refs(evidence: dict[str, Any]) -> None:
    foreign = "foreign-attempt:commit:one"
    evidence["commit_record_id"] = foreign
    evidence["attempt_ref"] = foreign
    evidence["gate_record_ref"] = foreign


def mutation_specs() -> list[tuple[str, str, Callable[[dict[str, Any]], None]]]:
    """O01-O12 followed by the seven intake counterexamples; reasons are exact assertions."""
    return [
        ("O01", "MISSING_EXIT_OR_REPLACEMENT", lambda e: e["trusted_chronology"].__setitem__(slice(2, 3), [])),
        ("O02", "SHAM_CONTINUE_BEFORE_RELEASE", _sham_late_release),
        ("O03", "FORBIDDEN_EFFECT", lambda e: (_open_source(e), e["sink_after_snapshot"]["effects"].append({"operation_id": "forbidden"}))),
        ("O04", "MISSING_POSITIVE_EFFECT", lambda e: e.__setitem__("sink_after_snapshot", {"effects": [], "promotions": []})),
        ("O05", "DISTINCT_APPROVAL_ROOTS_INSUFFICIENT", lambda e: e.__setitem__("approval_envelopes", [e["approval_envelopes"][0], deepcopy(e["approval_envelopes"][0])])),
        ("O06", "FALSE_COLLAPSE", lambda e: (_open_source(e), e.__setitem__("supplied_decision", {"action_gate": "HOLD", "q_state": "COLLAPSED_SCOPED"}))),
        ("O07", "MATERIAL_PACKET_FIDELITY_MISMATCH", _packet_loses_qsf_and_duty),
        ("O08", "PROMOTION_OBSERVED", lambda e: e["sink_after_snapshot"]["promotions"].append({"id": "forbidden-promotion"})),
        ("O09", "STALE_CURRENT_ATTESTATION", lambda e: (e["source_inventory"].__setitem__("current_attestation", {"epoch": "E0", "source": "historical"}), _rehash_source(e["source_inventory"]), _reproject(e))),
        ("O10", "FOREIGN_ATTEMPT_REF", _same_foreign_refs),
        ("O11", "INCOMPLETE_OBSERVATION_INTERVAL", lambda e: e.__setitem__("observation_interval", {})),
        ("O12", "DUPLICATED_SURFACE", lambda e: e["surface_observations"].append(deepcopy(e["surface_observations"][0]))),
        ("NO_LIFECYCLE_EVIDENCE", "NO_LIFECYCLE_EVIDENCE", lambda e: e.__setitem__("trusted_chronology", None)),
        ("SHAM_CONTINUES_BEFORE_RELEASE", "SHAM_CONTINUE_BEFORE_RELEASE", _sham_late_release),
        ("BOTH_REFS_SAME_WRONG_RUN", "FOREIGN_ATTEMPT_REF", _same_foreign_refs),
        ("PACKET_LOSES_QSF_AND_DUTY", "MATERIAL_PACKET_FIDELITY_MISMATCH", _packet_loses_qsf_and_duty),
        ("REVOKED_SOURCE_ALLOW_CLAIM", "REVOKED_SOURCE_ALLOW_CLAIM", _revoke_source),
        ("TWO_WRONG_SURFACES", "WRONG_SURFACE_INVENTORY", lambda e: e.__setitem__("surface_observations", [{"coordinate": "wrong/one"}, {"coordinate": "wrong/two"}])),
        ("MISSING_BASELINE_COUNTS", "MISSING_BASELINE_COUNTS", lambda e: e.__setitem__("sink_before_snapshot", None)),
    ]


def _unrelated_exit(evidence: dict[str, Any]) -> None:
    event = next(item for item in evidence["trusted_chronology"] if item.get("kind") == "EXIT_OBSERVED")
    event["instance_id"] = "unrelated-worker"
    event["os_handle_id"] = "unrelated-handle"
    event["start_evidence_ref"] = "unrelated-start"


def _foreign_effect_same_count(evidence: dict[str, Any]) -> None:
    evidence["sink_after_snapshot"]["effects"] = [{
        "effect_id": "effect:foreign-operation",
        "operation_id": "foreign-operation",
        "cell_id": "foreign-cell",
        "payload": {"kind": "SYNTHETIC_ACCEPT", "commit_record_id": "foreign-attempt:commit"},
    }]


def _a6_window_open(evidence: dict[str, Any]) -> None:
    source = evidence["source_inventory"]
    source["a6_conditions"]["window"]["status"] = "OPEN"
    _rehash_source(source)
    evidence["current_registry"] = deepcopy(source["registry"])
    evidence["supplied_decision"] = {"action_gate": "HOLD", "q_state": "OPEN"}
    evidence["sink_after_snapshot"] = {"effects": [], "promotions": []}
    evidence["expected_effect_row"] = None
    evidence["commit_evidence"] = {"atomic_revalidation": True, "binding_revalidated": True, "effect_delta": 0}
    _reproject(evidence)
    _refresh_intent(evidence, expect_effect=False)


def _a6_window_allow_effect(evidence: dict[str, Any]) -> None:
    source = evidence["source_inventory"]
    source["a6_conditions"]["window"]["status"] = "OPEN"
    _rehash_source(source)
    evidence["current_registry"] = deepcopy(source["registry"])
    evidence["supplied_decision"] = {"action_gate": "ALLOW", "q_state": "COLLAPSED_SCOPED"}
    _reproject(evidence)
    _refresh_intent(evidence, expect_effect=False)


def lawful_open_phase(key_root: Path) -> dict[str, Any]:
    evidence = positive_trace(key_root)
    _open_source(evidence)
    evidence["attempt_id"] = "synthetic-open-attempt"
    evidence["checkpoint"] = "OPEN_CHECK"
    commit_id = "synthetic-open-attempt:commit"
    evidence["commit_record_id"] = commit_id
    evidence["attempt_ref"] = commit_id
    evidence["gate_record_ref"] = commit_id
    evidence["record_scope"] = {"task_id": TASK_ID, "attempt_id": evidence["attempt_id"], "checkpoint": evidence["checkpoint"]}
    evidence["lifecycle_mode"] = "NO_REPLACEMENT"
    evidence["trusted_chronology"] = [{**evidence["record_scope"], "kind": "SYNTHETIC_TRACE", "instance_id": INSTANCE_ID}]
    _refresh_intent(evidence, expect_effect=False)
    return evidence


def r1e_observer_regressions(key_root: Path) -> dict[str, Any]:
    negatives = []
    for case_id, reason, mutate in (
        ("D02", "REPLACEMENT_W0_EXIT_MISSING", _unrelated_exit),
        ("D03", "EXPECTED_EFFECT_ROW_MISSING_OR_MISMATCH", _foreign_effect_same_count),
        ("D04", "A6_CONSTRAINT_BEHAVIOR_VIOLATION", _a6_window_allow_effect),
    ):
        evidence = deepcopy(positive_trace(key_root))
        mutate(evidence)
        result = inspect_checkpoint(evidence)
        negatives.append({
            "case_id": case_id,
            "expected_reason": reason,
            "actual_reasons": result["problems"],
            "detected_substantively": reason in result["problems"],
            "observer_status": result["observer_status"],
        })
    d05 = inspect_checkpoint(lawful_open_phase(key_root))
    r28 = next(item for item in d05["assertions"] if item["requirement_id"] == "R28")
    return {
        "negative_controls": negatives,
        "D05": {
            "expected_reason": "RESOLUTION_PROGRESS_PENDING_AFTER_LAWFUL_OPEN_HOLD",
            "actual_reason": r28["reason"],
            "r28_value": r28["value"],
            "effect_delta": d05["actual_effect_delta"],
            "detected_substantively": r28["reason"] == "RESOLUTION_PROGRESS_PENDING_AFTER_LAWFUL_OPEN_HOLD" and r28["value"] == "UNKNOWN",
        },
        "all_pass": all(row["detected_substantively"] for row in negatives) and r28["reason"] == "RESOLUTION_PROGRESS_PENDING_AFTER_LAWFUL_OPEN_HOLD",
    }


def run_mutation_suite(key_root: Path) -> dict[str, Any]:
    positive = inspect_checkpoint(positive_trace(key_root))
    results = []
    for case_id, expected_reason, mutate in mutation_specs():
        evidence = deepcopy(positive_trace(key_root))
        mutate(evidence)
        actual = inspect_checkpoint(evidence)
        results.append({
            "case_id": case_id,
            "origin": "SYNTHETIC_REGRESSION_PROCESS_FREE",
            "expected_reason": expected_reason,
            "actual_reasons": actual["problems"],
            "detected_substantively": expected_reason in actual["problems"],
            "observer_status": actual["observer_status"],
        })
    return {
        "positive": {"observer_status": positive["observer_status"], "assertion_count": len(positive["assertions"])},
        "mutations": results,
        "all_expected_reasons_detected": all(item["detected_substantively"] for item in results),
    }
