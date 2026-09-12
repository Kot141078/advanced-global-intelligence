from __future__ import annotations

import tempfile
import time
from copy import deepcopy
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from .broker import Broker, build_operation_intent
from .common import canonical_hash, write_json
from .native_adapter import NativeInputFactConflict, derive_native_outcome, emit_and_validate_logic_path
from .observer import inspect_checkpoint, inspect_logic_path
from .observer_fixtures import r1e_observer_regressions, run_mutation_suite
from .producer import make_packet
from .receiver import evaluate
from .signing import TestKeyStore
from .source import TASK_ID, immutable_source, resolved_source
from .state_transfer import material_projection


def _rfc3339_ns(value: int) -> str:
    seconds, nanos = divmod(value, 1_000_000_000)
    whole = datetime.fromtimestamp(seconds, tz=timezone.utc).strftime("%Y-%m-%dT%H:%M:%S")
    return f"{whole}.{nanos:09d}Z"


def _clock_point() -> dict[str, Any]:
    return {"utc_ns": time.time_ns(), "perf_counter_ns": time.perf_counter_ns()}


def _clock_point_after(previous: dict[str, Any]) -> dict[str, Any]:
    deadline = time.perf_counter_ns() + 1_000_000_000
    while time.perf_counter_ns() <= deadline:
        current = _clock_point()
        if current["utc_ns"] > previous["utc_ns"]:
            return current
    raise RuntimeError("CLOCK_RESOLUTION_INSUFFICIENT:UTC did not advance within one second")


def _phase_times(planning: dict[str, Any], basis: dict[str, Any], changed: dict[str, Any],
                 window_start: dict[str, Any], commit: dict[str, Any], window_end: dict[str, Any]) -> dict[str, Any]:
    return {
        "planning_utc": _rfc3339_ns(planning["utc_ns"]), "basis_utc": _rfc3339_ns(basis["utc_ns"]),
        "changed_utc": _rfc3339_ns(changed["utc_ns"]), "window_start_utc": _rfc3339_ns(window_start["utc_ns"]),
        "commit_utc": _rfc3339_ns(commit["utc_ns"]), "window_end_utc": _rfc3339_ns(window_end["utc_ns"]),
        "perf_counter_start_ns": window_start["perf_counter_ns"], "perf_counter_end_ns": window_end["perf_counter_ns"],
        "raw_points": {"planning": planning, "basis": basis, "changed": changed, "window_start": window_start,
                       "commit": commit, "window_end": window_end},
    }


def _observer_evidence(phase: dict[str, Any], public_map: dict[str, Any], native_pass: bool) -> dict[str, Any]:
    source = phase["source"]
    operation_intent = deepcopy(phase["operation_intent"])
    return {
        "fixture_origin": "SYNTHETIC_REGRESSION_OFFLINE_SQLITE_READBACK",
        "task_id": TASK_ID, "attempt_id": phase["attempt_id"], "checkpoint": phase["checkpoint"],
        "operation_id": operation_intent["scope"]["operation_id"],
        "cell_id": operation_intent["scope"]["cell_id"],
        "proposal_hash": operation_intent["basis"]["proposal_hash"],
        "active_instance_id": "offline-receiver-instance", "source_inventory": source,
        "materialized_packet": phase["packet_projection"],
        "materialized_packet_hash": canonical_hash(phase["packet_projection"]),
        "current_registry": deepcopy(source["registry"]), "public_signer_map": public_map,
        "approval_envelopes": phase["packet"]["approvals"],
        "supplied_decision": {"action_gate": phase["decision"]["action_gate"], "q_state": phase["decision"]["q_state"]},
        "lifecycle_mode": "NO_REPLACEMENT",
        "trusted_chronology": [{
            "task_id": TASK_ID, "attempt_id": phase["attempt_id"], "checkpoint": phase["checkpoint"],
            "kind": "SYNTHETIC_TRACE", "instance_id": "offline-receiver-instance",
        }],
        "sink_before_snapshot": {"effects": phase["sink_before"]["effects"], "promotions": phase["sink_before"]["promotions"]},
        "sink_after_snapshot": {"effects": phase["sink_after"]["effects"], "promotions": phase["sink_after"]["promotions"]},
        "operation_intent": operation_intent,
        "operation_intent_hash": canonical_hash(operation_intent),
        "expected_effect_row": deepcopy(operation_intent["expected_effect_row"]),
        "commit_record_id": phase["commit_record_id"],
        "attempt_ref": phase["commit_record_id"], "gate_record_ref": phase["commit_record_id"],
        "record_scope": {"task_id": TASK_ID, "attempt_id": phase["attempt_id"], "checkpoint": phase["checkpoint"]},
        "commit_evidence": {
            "atomic_revalidation": phase["broker_result"]["atomic_revalidation"],
            "binding_revalidated": phase["broker_result"].get("binding_revalidated"),
            "effect_delta": phase["broker_result"]["effect_delta"],
        },
        "observation_interval": {"domain": "HOST_PERF_COUNTER_NS", "start_ns": phase["times"]["perf_counter_start_ns"],
                                 "end_ns": phase["times"]["perf_counter_end_ns"]},
        "surface_observations": [{"coordinate": coordinate, "before_ref": f"{phase['checkpoint']}:before:{i}",
                                  "after_ref": f"{phase['checkpoint']}:after:{i}"}
                                 for i, coordinate in enumerate(source["surface_inventory"])],
        "forbidden_identity_claims": [],
        "boundary_manifest": {"external_components": ["source", "authority_registry", "broker", "observer", "supervisor"]},
        "native_binding_status": "PASS" if native_pass else "FAIL", "availability_policy": "MISSING_IS_UNKNOWN",
        "append_only_history": True, "evidence_scope": "SYNTHETIC_REGRESSION",
        "observer_dependencies": ["common", "signing", "state_transfer"], "signature_controls_status": "PASS",
        "containment_status": "NOT_RUN", "memory_judge_mode": "EXCLUDED", "measured_matrix_started": False,
        "clock_mapping": {"semantic": "CGDR_TEST_TICKS", "native": "RFC3339", "lifecycle": "HOST_PERF_COUNTER_NS"},
        "implementation_classes": ["REUSED_UNMODIFIED", "BOUNDED_ADAPTER", "TEST_DOUBLE", "NOT_IMPLEMENTED"],
    }


def _run_e_controls(
    artifacts: Path,
    keys: TestKeyStore,
    public_map: dict[str, Any],
    open_evidence: dict[str, Any],
    resolved_evidence: dict[str, Any],
    open_phase: dict[str, Any],
    resolved_phase: dict[str, Any],
) -> dict[str, Any]:
    """Exercise E01-E05 through the repaired top-level boundaries."""
    e01_evidence = deepcopy(resolved_evidence)
    e01_evidence["materialized_packet"].pop("duty")
    e01_evidence["materialized_packet_hash"] = canonical_hash(e01_evidence["materialized_packet"])
    e01_observed = inspect_logic_path(open_evidence, e01_evidence)
    e01_reasons = sorted({row["reason"] for row in e01_observed["in_scope_failures"]})

    e02_phase = deepcopy(resolved_phase)
    foreign_row = deepcopy(e02_phase["effect_row"])
    foreign_row["operation_id"] = "foreign-operation"
    foreign_row["effect_id"] = "effect:foreign-operation"
    foreign_row["payload"]["operation_id"] = "foreign-operation"
    foreign_row["payload"]["attempt_id"] = "foreign-attempt"
    foreign_row["payload"]["commit_record_id"] = "foreign-attempt:commit"
    e02_phase["sink_after"]["effects"] = [foreign_row]
    e02_phase["effect_row"] = foreign_row
    e02_evidence = _observer_evidence(e02_phase, public_map, True)
    e02_evidence["expected_effect_row"] = deepcopy(foreign_row)
    e02_observed = inspect_logic_path(open_evidence, e02_evidence)

    e03_evidence = deepcopy(open_evidence)
    e03_source = e03_evidence["source_inventory"]
    e03_source["a6_conditions"]["window"]["status"] = "OPEN"
    e03_source.pop("source_hash")
    e03_source["source_hash"] = canonical_hash(e03_source)
    e03_evidence["current_registry"] = deepcopy(e03_source["registry"])
    e03_evidence["materialized_packet"] = material_projection(e03_source)
    e03_evidence["materialized_packet_hash"] = canonical_hash(e03_evidence["materialized_packet"])
    e03_evidence["proposal_hash"] = canonical_hash({"control": "E03", "source_hash": e03_source["source_hash"]})
    e03_intent = build_operation_intent(
        e03_evidence["operation_id"], e03_evidence["cell_id"], e03_evidence["proposal_hash"],
        e03_source, e03_evidence["active_instance_id"], e03_evidence["attempt_id"],
        e03_evidence["checkpoint"], e03_evidence["commit_record_id"], expect_effect=False,
    )
    e03_evidence["operation_intent"] = e03_intent
    e03_evidence["operation_intent_hash"] = canonical_hash(e03_intent)
    e03_evidence["expected_effect_row"] = None
    e03_lawful = inspect_checkpoint(e03_evidence)
    e03_wrong_evidence = deepcopy(e03_evidence)
    e03_wrong_evidence["supplied_decision"] = {"action_gate": "ALLOW", "q_state": "COLLAPSED_SCOPED"}
    e03_wrong_evidence["sink_after_snapshot"]["effects"] = [{
        "effect_id": "effect:forbidden-e03", "operation_id": e03_evidence["operation_id"],
        "cell_id": e03_evidence["cell_id"], "payload": {"kind": "SYNTHETIC_ACCEPT"},
    }]
    e03_wrong_evidence["commit_evidence"]["effect_delta"] = 1
    e03_wrong = inspect_checkpoint(e03_wrong_evidence)
    lawful_r13 = next(row for row in e03_lawful["assertions"] if row["requirement_id"] == "R13")
    wrong_r13 = next(row for row in e03_wrong["assertions"] if row["requirement_id"] == "R13")

    e04_source = resolved_source(immutable_source("R1_6F_E04_OPERATION_SCOPE"))
    e04_operation = "e04-declared-operation"
    e04_attempt = "r1f-e04-attempt"
    e04_packet = make_packet(
        "R1F_E04", e04_source, keys, "RESOLVED_CHECK",
        instance_id="offline-receiver-instance", attempt_id=e04_attempt,
        operation_id=e04_operation, commit_record_id=f"{e04_attempt}:commit",
    )
    e04_decision = evaluate(e04_packet, e04_source, public_map)
    e04_proposal = e04_packet["envelope"]["payload"]
    e04_intent = build_operation_intent(
        e04_operation, "R1F_E04", e04_proposal["proposal_hash"], e04_source,
        "offline-receiver-instance", e04_attempt, "RESOLVED_CHECK",
        f"{e04_attempt}:commit", expect_effect=True,
    )
    e04_broker = Broker(artifacts / "e04_operation_scope.sqlite3")
    e04_broker.bind_instance(e04_source, "offline-receiver-instance")
    e04_calls: list[dict[str, Any]] = []
    try:
        for operation_id in ("e04-wrong-before", e04_operation, e04_operation, "e04-renamed-after"):
            outcome = e04_broker.atomic_commit(
                operation_id, "R1F_E04", e04_proposal["proposal_hash"], e04_decision,
                e04_source, "offline-receiver-instance", operation_context=e04_intent,
                proposal_envelope=e04_packet["envelope"], public_signer_map=public_map,
            )
            e04_calls.append({"operation_id": operation_id, "result": outcome})
        e04_snapshot = e04_broker.snapshot()
    finally:
        e04_broker.close()

    e05_phase = deepcopy(resolved_phase)
    e05_phase["decision"]["action_gate"] = "HOLD"
    e05_phase["decision"]["q_state"] = "OPEN"
    e05_phase["broker_result"].update(
        result="DENIED_ATOMIC_REVALIDATION", effect_delta=0, binding_revalidated=False,
    )
    e05_phase["sink_after"]["effects"] = deepcopy(e05_phase["sink_before"]["effects"])
    e05_phase["effect_row"] = None
    try:
        derive_native_outcome(e05_phase)
        e05_error: dict[str, Any] | None = None
    except NativeInputFactConflict as conflict:
        e05_error = conflict.as_dict()

    controls = {
        "scope": "OFFLINE_DEFENSIVE_REGRESSION_NOT_PROCESS_CONFORMANCE",
        "E01": {
            "expected": ["UNFINISHED_DUTY_LOST", "SOURCE_PROJECTION_MISMATCH", "TRACE_CONTAINS_SUBSTANTIVE_VIOLATION"],
            "actual": e01_reasons,
            "aggregate_status": e01_observed["offline_logic_path_status"],
            "passed": e01_observed["offline_logic_path_status"] == "FAIL" and set({
                "UNFINISHED_DUTY_LOST", "SOURCE_PROJECTION_MISMATCH", "TRACE_CONTAINS_SUBSTANTIVE_VIOLATION",
            }).issubset(e01_reasons),
        },
        "E02": {
            "expected": ["EXPECTED_EFFECT_ROW_MISSING_OR_MISMATCH", "UNTRUSTED_EXPECTED_EFFECT_OVERRIDE"],
            "actual": e02_observed["resolved_checkpoint"]["problems"],
            "intent_row_hash": canonical_hash(resolved_phase["operation_intent"]["expected_effect_row"]),
            "actual_foreign_row_hash": canonical_hash(foreign_row),
            "aggregate_status": e02_observed["offline_logic_path_status"],
            "passed": e02_observed["offline_logic_path_status"] == "FAIL" and all(
                reason in e02_observed["resolved_checkpoint"]["problems"]
                for reason in ("EXPECTED_EFFECT_ROW_MISSING_OR_MISMATCH", "UNTRUSTED_EXPECTED_EFFECT_OVERRIDE")
            ),
        },
        "E03": {
            "lawful": {"r13": lawful_r13, "problems": e03_lawful["problems"], "effect_delta": e03_lawful["actual_effect_delta"]},
            "violation": {"r13": wrong_r13, "problems": e03_wrong["problems"], "effect_delta": e03_wrong["actual_effect_delta"]},
            "passed": lawful_r13["value"] == "PASS" and wrong_r13["reason"] == "A6_CONSTRAINT_BEHAVIOR_VIOLATION",
        },
        "E04": {
            "authorized_operation_id": e04_operation,
            "calls": e04_calls,
            "readback": e04_snapshot,
            "excluded_from_linked_path_effect_counter": True,
            "passed": [row["result"]["effect_delta"] for row in e04_calls] == [0, 1, 0, 0]
            and len(e04_snapshot["effects"]) == 1
            and e04_snapshot["effects"][0]["operation_id"] == e04_operation,
        },
        "E05": {
            "expected": "INPUT_FACT_CONFLICT",
            "actual": e05_error,
            "success_record_emitted": False,
            "passed": isinstance(e05_error, dict) and e05_error.get("code") == "INPUT_FACT_CONFLICT",
        },
    }
    controls["all_pass"] = all(controls[name]["passed"] for name in ("E01", "E02", "E03", "E04", "E05"))
    return controls


def execute(output: Path) -> dict[str, Any]:
    """Execute the one authorized process-free OPEN->RESOLVED SQLite logic path."""
    output.mkdir(parents=True, exist_ok=False)
    artifacts = output / "artifacts"
    artifacts.mkdir()
    initial = _clock_point()
    grant_valid_until_utc = _rfc3339_ns(initial["utc_ns"] + 3_600_000_000_000)
    open_source = immutable_source("R1_6F_LOGIC_PATH")
    with tempfile.TemporaryDirectory(prefix="cgdr-r1f-private-keys-") as private_root:
        keys = TestKeyStore(Path(private_root))
        public_map = keys.public_map({"producer-alpha": "root:alpha", "approver-beta": "root:beta"})
        broker = Broker(artifacts / "logic_path.sqlite3")
        try:
            broker.bind_instance(open_source, "offline-receiver-instance")
            open_planning = _clock_point_after(initial)
            open_basis = _clock_point_after(open_planning)
            open_operation_id = "logic-path:open-hold"
            open_attempt_id = "r1f-open-attempt"
            open_commit_record_id = f"{open_attempt_id}:commit"
            open_packet = make_packet(
                "R1F_OPEN", open_source, keys, "OPEN_CHECK",
                instance_id="offline-receiver-instance", attempt_id=open_attempt_id,
                operation_id=open_operation_id, commit_record_id=open_commit_record_id,
            )
            open_decision = evaluate(open_packet, open_source, public_map)
            open_changed = _clock_point_after(open_basis)
            open_window_start = _clock_point_after(open_changed)
            open_commit = _clock_point_after(open_window_start)
            open_before = broker.snapshot()
            open_context = build_operation_intent(
                open_operation_id, "R1F_OPEN", open_packet["envelope"]["payload"]["proposal_hash"],
                open_source, "offline-receiver-instance", open_attempt_id, "OPEN_CHECK",
                open_commit_record_id, expect_effect=False,
            )
            open_result = broker.atomic_commit(
                open_operation_id, "R1F_OPEN", open_packet["envelope"]["payload"]["proposal_hash"],
                open_decision, open_source, "offline-receiver-instance", operation_context=open_context,
                proposal_envelope=open_packet["envelope"], public_signer_map=public_map,
            )
            open_window_end, open_after = _clock_point_after(open_commit), broker.snapshot()
            open_phase = {
                "checkpoint": "OPEN_CHECK", "attempt_id": open_attempt_id,
                "commit_record_id": open_commit_record_id, "operation_id": open_operation_id,
                "effect_intent_id": "effect:logic-path:synthetic-accept", "effect_row": None,
                "operation_intent": open_context, "operation_intent_hash": canonical_hash(open_context),
                "source": open_source, "packet": open_packet, "packet_projection": material_projection(open_source),
                "decision": open_decision, "broker_result": open_result, "sink_before": open_before, "sink_after": open_after,
                "times": _phase_times(open_planning, open_basis, open_changed, open_window_start, open_commit, open_window_end),
                "retry_path_state": "ABSENT_NO_QUEUE_OR_RETRY_PRIMITIVE",
            }

            resolved = resolved_source(open_source)
            broker.advance_source(resolved, "offline-receiver-instance")
            resolved_planning = _clock_point_after(open_window_end)
            resolved_basis = _clock_point_after(resolved_planning)
            resolved_operation_id = "logic-path:synthetic-accept"
            resolved_attempt_id = "r1f-resolved-attempt"
            resolved_commit_record_id = f"{resolved_attempt_id}:commit"
            resolved_packet = make_packet(
                "R1F_RESOLVED", resolved, keys, "RESOLVED_CHECK",
                instance_id="offline-receiver-instance", attempt_id=resolved_attempt_id,
                operation_id=resolved_operation_id, commit_record_id=resolved_commit_record_id,
            )
            resolved_decision = evaluate(resolved_packet, resolved, public_map)
            resolved_changed = _clock_point_after(resolved_basis)
            resolved_window_start = _clock_point_after(resolved_changed)
            resolved_commit = _clock_point_after(resolved_window_start)
            resolved_before = broker.snapshot()
            resolved_context = build_operation_intent(
                resolved_operation_id, "R1F_RESOLVED",
                resolved_packet["envelope"]["payload"]["proposal_hash"], resolved,
                "offline-receiver-instance", resolved_attempt_id, "RESOLVED_CHECK",
                resolved_commit_record_id, expect_effect=True,
            )
            resolved_result = broker.atomic_commit(
                resolved_operation_id, "R1F_RESOLVED",
                resolved_packet["envelope"]["payload"]["proposal_hash"], resolved_decision, resolved,
                "offline-receiver-instance", operation_context=resolved_context,
                proposal_envelope=resolved_packet["envelope"], public_signer_map=public_map,
            )
            resolved_window_end, resolved_after = _clock_point_after(resolved_commit), broker.snapshot()
            effect_rows = [row for row in resolved_after["effects"] if row["operation_id"] == "logic-path:synthetic-accept"]
            resolved_phase = {
                "checkpoint": "RESOLVED_CHECK", "attempt_id": resolved_attempt_id,
                "commit_record_id": resolved_commit_record_id, "operation_id": resolved_operation_id,
                "effect_intent_id": "effect:logic-path:synthetic-accept", "effect_row": effect_rows[0] if len(effect_rows) == 1 else None,
                "operation_intent": resolved_context, "operation_intent_hash": canonical_hash(resolved_context),
                "source": resolved, "packet": resolved_packet, "packet_projection": material_projection(resolved),
                "decision": resolved_decision, "broker_result": resolved_result, "sink_before": resolved_before, "sink_after": resolved_after,
                "times": _phase_times(resolved_planning, resolved_basis, resolved_changed, resolved_window_start, resolved_commit, resolved_window_end),
                "retry_path_state": "ABSENT_NO_QUEUE_OR_RETRY_PRIMITIVE",
            }
        finally:
            broker.close()

        path_facts = {"task_id": TASK_ID, "scope": "SYNTHETIC_REGRESSION", "grant_effective_utc": _rfc3339_ns(initial["utc_ns"]),
                      "grant_valid_until_utc": grant_valid_until_utc, "phases": [open_phase, resolved_phase]}
        native = emit_and_validate_logic_path(path_facts, output / "native")
        open_evidence = _observer_evidence(open_phase, public_map, native["accepted"])
        resolved_evidence = _observer_evidence(resolved_phase, public_map, native["accepted"])
        observer = inspect_logic_path(open_evidence, resolved_evidence)
        mutations = run_mutation_suite(Path(private_root) / "observer-mutation-keys")
        r1e_controls = r1e_observer_regressions(Path(private_root) / "observer-r1f-keys")
        e_controls = _run_e_controls(
            artifacts, keys, public_map, open_evidence, resolved_evidence, open_phase, resolved_phase,
        )
        public_information = public_map

    write_json(artifacts / "path_facts.json", path_facts)
    write_json(artifacts / "public_signer_map.json", public_information)
    for phase in path_facts["phases"]:
        target = artifacts / phase["checkpoint"].casefold()
        target.mkdir()
        for name in ("source", "packet", "packet_projection", "decision", "broker_result", "operation_intent", "sink_before", "sink_after", "times"):
            write_json(target / f"{name}.json", phase[name])
    write_json(artifacts / "observer_open.json", open_evidence)
    write_json(artifacts / "observer_resolved.json", resolved_evidence)
    write_json(output / "observer_logic_path.json", observer)
    write_json(output / "observer_mutations_19.json", mutations)
    write_json(output / "observer_d02_d05.json", r1e_controls)
    write_json(output / "e01_e05_controls.json", e_controls)
    checks = {
        "open_hold_zero": open_result["result"] == "HELD" and open_result["effect_delta"] == 0,
        "resolved_allow_one": resolved_result["result"] == "BOUND" and resolved_result["effect_delta"] == 1 and len(effect_rows) == 1,
        "zero_promotions": len(open_after["promotions"]) == 0 and len(resolved_after["promotions"]) == 0,
        "observer_logic_path": observer["offline_logic_path_status"] == "PASS",
        "observer_19_controls": mutations["all_expected_reasons_detected"],
        "observer_d02_d05": r1e_controls["all_pass"],
        "native_four_layers": native["accepted"],
        "e01_e05_controls": e_controls["all_pass"],
    }
    result = {
        "task_id": TASK_ID, "offline_logic_path_status": "PASS" if all(checks.values()) else "FAIL",
        "checks": checks, "open_effect_delta": open_result["effect_delta"], "resolved_effect_delta": resolved_result["effect_delta"],
        "resolved_operation_id": "logic-path:synthetic-accept", "resolved_effect_row": effect_rows[0] if len(effect_rows) == 1 else None,
        "memory_promotions": 0, "private_key_cleanup": "TEMPORARY_DIRECTORY_REMOVED_AFTER_USE",
        "worker_start_requests": 0, "helper_starts": 0, "wsl_launches": 0,
        "selected_process_conformance": "NOT_RUN", "matrix_effects": None, "matrix_promotions": None,
    }
    write_json(output / "result.json", result)
    return result
