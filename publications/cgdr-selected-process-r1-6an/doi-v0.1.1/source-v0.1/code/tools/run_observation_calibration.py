from __future__ import annotations

import argparse
import copy
import inspect
import json
import tempfile
from pathlib import Path
from typing import Any, Callable

from cgdr_r1_6b.broker import build_operation_intent
from cgdr_r1_6b.common import canonical_hash, write_json
from cgdr_r1_6b.producer import make_packet
from cgdr_r1_6b.prospective_observation import (
    TASK_ID as K_IMPLEMENTATION_TASK_ID,
    ObservationError,
    ProspectiveObservation,
    build_observation_plan,
    build_phase_native_material,
    prepare_prospective_observation,
    review_observation_evidence,
    system_clock_pair,
)
from cgdr_r1_6b.receiver import evaluate
from cgdr_r1_6b.s2_handoff import (
    authority_public_map,
    build_current_source_view,
    build_open_prestate,
    make_e0_fence_payload,
    make_e1_payload,
    run_hold_gate,
    sha256_bytes,
    sign_authority_payload,
)
from cgdr_r1_6b.s2_native import emit_and_validate_s2_hold
from cgdr_r1_6b.signing import TestKeyStore
from cgdr_r1_6b.source import immutable_source, resolved_source
from cgdr_r1_6b.state_transfer import freeze_state


TASK_ID = "CGDR_SELECTED_PROCESS_OBSERVATION_REPAIR_R1_6L"
ITERATION_TASK_ID = "CGDR_SELECTED_PROCESS_OBSERVATION_BINDING_REPAIR_R1_6M"


def _binding(instance: str, pid: int) -> dict[str, Any]:
    return {
        "instance_id": instance,
        "worker_pid": pid,
        "worker_start_ticks": pid * 100,
        "pid_namespace": f"pid:[synthetic-{pid}]",
    }


def _open_current_source(
    attempt_id: str, instance_id: str, keys: TestKeyStore, public_map: dict[str, Any]
) -> dict[str, Any]:
    w0 = _binding(f"{instance_id}-w0", 4101)
    w1 = _binding(instance_id, 4102)
    source = build_open_prestate(attempt_id, w0["instance_id"])
    frozen = freeze_state(source)
    fence = sign_authority_payload(
        make_e0_fence_payload(
            attempt_id=attempt_id,
            source=source,
            w0_binding=w0,
            checkpoint_raw_sha256=sha256_bytes(frozen["bytes"]),
        ),
        keys,
    )
    e1 = sign_authority_payload(
        make_e1_payload(
            attempt_id=attempt_id,
            w1_binding=w1,
            source=source,
            checkpoint_raw_sha256=sha256_bytes(frozen["bytes"]),
            checkpoint_canonical_sha256=frozen["state_sha256"],
            fence_envelope=fence,
        ),
        keys,
    )
    current, _ = build_current_source_view(
        frozen["state"],
        attempt_id=attempt_id,
        w1_binding=w1,
        e0_fence=fence,
        e1_envelope=e1,
        public_map=public_map,
    )
    return current


def _scope(source: dict[str, Any], attempt: str, instance: str, checkpoint: str, cell: str) -> dict[str, str]:
    return {
        "task_id": source["trusted_policy"]["task_id"],
        "action": source["trusted_policy"]["protected_action"],
        "operation_id": f"operation:{attempt}:open-hold" if checkpoint == "S2_OPEN_CHECK" else f"operation:{attempt}:allow",
        "cell_id": cell,
        "attempt_id": attempt,
        "checkpoint": checkpoint,
        "instance_id": instance,
        "commit_record_id": f"commit:{attempt}:open-hold" if checkpoint == "S2_OPEN_CHECK" else f"commit:{attempt}:allow",
    }


def _plan(
    root: Path,
    case: str,
    source: dict[str, Any],
    attempt: str,
    instance: str,
    checkpoint: str = "S2_OPEN_CHECK",
    cell: str = "S2_OPEN_HANDOFF",
    expected: str = "HOLD_NO_EFFECT",
    phase_inventory: list[str] | None = None,
) -> dict[str, Any]:
    case_root = root / "cases" / case
    return build_observation_plan(
        task_id=TASK_ID,
        cell_id=cell,
        attempt_id=attempt,
        checkpoint=checkpoint,
        database=case_root / "observed.sqlite3",
        path_boundary_root=root,
        operation_scope=_scope(source, attempt, instance, checkpoint, cell),
        expected_outcome=expected,
        phase_inventory=phase_inventory,
    )


def _fake_start(ledger: list[dict[str, Any]], label: str) -> dict[str, Any]:
    row = {"kind": "SYNTHETIC_FIRST_START_CALLBACK", "label": label, "process_started": False}
    ledger.append(row)
    return row


def _times_from_evidence(
    evidence: dict[str, Any], review: dict[str, Any], phase: str
) -> dict[str, Any]:
    result = review["phase_results"][phase]
    transactions = evidence["transactions"]
    commit = next(row for row in transactions if row.get("state") == "COMMITTED")
    start_snapshot = next(row for row in evidence["snapshots"] if row["snapshot_id"] == result["begin_snapshot_id"])
    planning = evidence["plan"]["plan_created_clock"]
    basis = start_snapshot["read_transaction"]["end_clock"]
    transaction_start = next(row for row in transactions if row.get("state") == "STARTED")
    changed = transaction_start["clock"]
    return {
        "planning_utc": planning["utc"],
        "basis_utc": basis["utc"],
        "changed_utc": changed["utc"],
        "window_start_utc": result["window"]["start_utc"],
        "commit_utc": commit["clock"]["utc"],
        "window_end_utc": result["window"]["end_utc"],
        "perf_counter_start_ns": int(result["window"]["start_monotonic_ns"]),
        "perf_counter_end_ns": int(result["window"]["end_monotonic_ns"]),
        "raw_points": {
            "planning": planning,
            "basis": basis,
            "changed": changed,
            "commit": commit["clock"],
        },
    }


def _finish_case(
    case_root: Path,
    broker: Any,
    observer: Any,
    *,
    binding_label: str,
) -> tuple[dict[str, Any], dict[str, Any]]:
    observer.mark_owned_exit(
        synthetic=True,
        binding={"kind": binding_label, "process_started": False, "claim": "DEPENDENCY_INJECTION_CALLBACK_ONLY"},
    )
    evidence = observer.finalize()
    review = review_observation_evidence(evidence)
    write_json(case_root / "OBSERVATION_REVIEW.json", review)
    broker.close()
    return evidence, review


def _transaction(
    observer: Any,
    broker: Any,
    transaction_id: str,
    operation_id: str,
    statements: Callable[[], None],
    *,
    commit: bool,
) -> None:
    observer.begin_writer_transaction(
        transaction_id,
        operation_id=operation_id,
        interface="bounded_calibration_dml",
    )
    try:
        broker.db.execute("BEGIN IMMEDIATE")
        statements()
        if commit:
            broker.db.commit()
            observer.finish_writer_transaction(transaction_id, "COMMITTED")
        else:
            broker.db.rollback()
            observer.finish_writer_transaction(transaction_id, "ROLLED_BACK", reason="CALIBRATION_REQUESTED_ROLLBACK")
    except BaseException as exc:
        if broker.db.in_transaction:
            broker.db.rollback()
        if observer._current_transaction_id == transaction_id:  # bounded cleanup of this local calibration context
            observer.finish_writer_transaction(transaction_id, "ROLLED_BACK", reason=f"{type(exc).__name__}:{exc}")
        raise


def _positive_hold(
    root: Path, keys: TestKeyStore, public_map: dict[str, Any]
) -> dict[str, Any]:
    case_root = root / "cases" / "positive_hold"
    attempt, instance = "r1-6l-positive-hold", "calibration-w1-positive"
    source = _open_current_source(attempt, instance, keys, public_map)
    plan = _plan(root, "positive_hold", source, attempt, instance)
    broker, observer = prepare_prospective_observation(plan=plan, output=case_root / "observation")
    readiness = observer.readiness_receipt()
    callback_ledger: list[dict[str, Any]] = []
    observer.invoke_first_start(lambda: _fake_start(callback_ledger, "positive_hold"))
    gate = run_hold_gate(
        broker=broker,
        observation=observer,
        source=source,
        keys=keys,
        public_map=public_map,
        attempt_id=attempt,
        instance_id=instance,
        intent_capture_path=case_root / "IMMUTABLE_OPERATION_INTENT.json",
    )
    evidence, review = _finish_case(case_root, broker, observer, binding_label="POSITIVE_HOLD_FAKE_EXIT")
    native_material = build_phase_native_material(evidence, review, "S2_OPEN_CHECK")
    write_json(case_root / "PROSPECTIVE_NATIVE_MATERIAL.json", native_material)
    phase = {
        **gate,
        "source": source,
        "attempt_id": attempt,
        "times": _times_from_evidence(evidence, review, "S2_OPEN_CHECK"),
        "grant_valid_until_utc": "2099-01-01T00:00:00Z",
        "prospective_native_material": native_material,
    }
    native = emit_and_validate_s2_hold(
        phase,
        case_root / "native",
        evidence_scope="LOCAL_CALIBRATION_PROSPECTIVE",
    )
    write_json(case_root / "READINESS_RECEIPT.json", readiness)
    write_json(case_root / "GATE_RESULT.json", gate)
    write_json(case_root / "PUBLIC_SIGNER_MAP.json", public_map)
    return {
        "plan": plan,
        "readiness": readiness,
        "callback_ledger": callback_ledger,
        "gate": gate,
        "evidence": evidence,
        "review": review,
        "native_material": native_material,
        "native": native,
    }


def _transient_changes(root: Path) -> dict[str, Any]:
    case_root = root / "cases" / "transient_changes"
    attempt, instance = "r1-6l-transient", "calibration-transient"
    source = immutable_source("R1L_TRANSIENT")
    plan = _plan(
        root,
        "transient_changes",
        source,
        attempt,
        instance,
        phase_inventory=["OPEN_CHECK", "RESOLVED_CHECK"],
    )
    broker, observer = prepare_prospective_observation(plan=plan, output=case_root / "observation")
    observer.invoke_first_start(lambda: {"process_started": False})
    observer.begin_phase("OPEN_CHECK")
    observer.end_phase("OPEN_CHECK")
    observer.begin_phase("RESOLVED_CHECK")

    payload_a = json.dumps({"operation_id": plan["expected_operation_intent"]["scope"]["operation_id"], "value": 1}, sort_keys=True)
    payload_b = json.dumps({"operation_id": plan["expected_operation_intent"]["scope"]["operation_id"], "value": 2}, sort_keys=True)
    payload_c = json.dumps({"operation_id": plan["expected_operation_intent"]["scope"]["operation_id"], "value": 3}, sort_keys=True)
    _transaction(observer, broker, "txn-transient-effect-insert", "transient-effect", lambda: broker.db.execute(
        "INSERT INTO effects VALUES(?,?,?,?)", ("effect:transient", "operation:transient", "R1L_TRANSIENT", payload_a)
    ), commit=True)
    _transaction(observer, broker, "txn-transient-effect-update", "transient-effect", lambda: broker.db.execute(
        "UPDATE effects SET payload=? WHERE effect_id=?", (payload_b, "effect:transient")
    ), commit=True)
    _transaction(observer, broker, "txn-transient-effect-replace", "transient-effect", lambda: broker.db.execute(
        "INSERT OR REPLACE INTO effects VALUES(?,?,?,?)",
        ("effect:transient", "operation:transient", "R1L_TRANSIENT", payload_c),
    ), commit=True)
    _transaction(observer, broker, "txn-transient-effect-upsert", "transient-effect", lambda: broker.db.execute(
        "INSERT INTO effects VALUES(?,?,?,?) ON CONFLICT(effect_id) DO UPDATE SET payload=excluded.payload",
        ("effect:transient", "operation:transient", "R1L_TRANSIENT", payload_b),
    ), commit=True)
    _transaction(observer, broker, "txn-transient-effect-delete", "transient-effect", lambda: broker.db.execute(
        "DELETE FROM effects WHERE effect_id=?", ("effect:transient",)
    ), commit=True)
    _transaction(observer, broker, "txn-transient-promotion-insert", "transient-promotion", lambda: broker.db.execute(
        "INSERT INTO promotions VALUES(?,?,?)", ("promotion:transient", "R1L_TRANSIENT", payload_a)
    ), commit=True)
    _transaction(observer, broker, "txn-transient-promotion-update", "transient-promotion", lambda: broker.db.execute(
        "UPDATE promotions SET payload=? WHERE promotion_id=?", (payload_b, "promotion:transient")
    ), commit=True)
    _transaction(observer, broker, "txn-transient-promotion-delete", "transient-promotion", lambda: broker.db.execute(
        "DELETE FROM promotions WHERE promotion_id=?", ("promotion:transient",)
    ), commit=True)
    observer.end_phase("RESOLVED_CHECK")
    evidence, review = _finish_case(case_root, broker, observer, binding_label="TRANSIENT_FAKE_EXIT")
    native_refusal = build_phase_native_material(evidence, review, "RESOLVED_CHECK")
    write_json(case_root / "NATIVE_EMISSION_REFUSAL.json", native_refusal)
    return {"plan": plan, "evidence": evidence, "review": review, "native_refusal": native_refusal}


def _rollback(root: Path) -> dict[str, Any]:
    case_root = root / "cases" / "rollback"
    attempt, instance = "r1-6l-rollback", "calibration-rollback"
    source = immutable_source("R1L_ROLLBACK")
    plan = _plan(root, "rollback", source, attempt, instance, phase_inventory=["OPEN_CHECK"])
    broker, observer = prepare_prospective_observation(plan=plan, output=case_root / "observation")
    observer.invoke_first_start(lambda: {"process_started": False})
    observer.begin_phase("OPEN_CHECK")
    payload = json.dumps({"kind": "ROLLED_BACK_CALIBRATION"}, sort_keys=True)
    _transaction(observer, broker, "txn-rollback-effect", "rollback-effect", lambda: broker.db.execute(
        "INSERT INTO effects VALUES(?,?,?,?)", ("effect:rollback", "operation:rollback", "R1L_ROLLBACK", payload)
    ), commit=False)
    observer.end_phase("OPEN_CHECK")
    evidence, review = _finish_case(case_root, broker, observer, binding_label="ROLLBACK_FAKE_EXIT")
    return {"plan": plan, "evidence": evidence, "review": review}


def _broker_allow(
    root: Path, keys: TestKeyStore, public_map: dict[str, Any]
) -> dict[str, Any]:
    case_root = root / "cases" / "broker_allow"
    attempt, instance = "r1-6l-broker-allow", "calibration-broker-allow"
    source = resolved_source(immutable_source("R1L_ALLOW"))
    checkpoint, cell = "RESOLVED_CHECK", "R1L_ALLOW"
    scope = _scope(source, attempt, instance, checkpoint, cell)
    plan = build_observation_plan(
        task_id=TASK_ID,
        cell_id=cell,
        attempt_id=attempt,
        checkpoint=checkpoint,
        database=case_root / "observed.sqlite3",
        path_boundary_root=root,
        operation_scope=scope,
        expected_outcome="ALLOW_EXACTLY_ONE",
    )
    broker, observer = prepare_prospective_observation(plan=plan, output=case_root / "observation")
    observer.invoke_first_start(lambda: {"process_started": False})
    observer.begin_phase(checkpoint)
    broker.bind_instance(source, instance)
    packet = make_packet(
        cell,
        source,
        keys,
        checkpoint,
        instance_id=instance,
        attempt_id=attempt,
        operation_id=scope["operation_id"],
        commit_record_id=scope["commit_record_id"],
    )
    decision = evaluate(packet, source, public_map)
    proposal = packet["envelope"]["payload"]
    intent = build_operation_intent(
        scope["operation_id"], cell, proposal["proposal_hash"], source, instance,
        attempt, checkpoint, scope["commit_record_id"], expect_effect=True,
    )
    transaction_id = f"observation-txn:{attempt}:{checkpoint}:{scope['operation_id']}"
    observer.begin_writer_transaction(transaction_id, operation_id=scope["operation_id"], interface="Broker.atomic_commit")
    try:
        result = broker.atomic_commit(
            scope["operation_id"], cell, proposal["proposal_hash"], decision, source, instance,
            operation_context=intent, proposal_envelope=packet["envelope"], public_signer_map=public_map,
        )
    except BaseException as exc:
        observer.finish_writer_transaction(transaction_id, "ROLLED_BACK", reason=f"{type(exc).__name__}:{exc}")
        raise
    else:
        observer.finish_writer_transaction(transaction_id, "COMMITTED")
    observer.end_phase(checkpoint)
    evidence, review = _finish_case(case_root, broker, observer, binding_label="BROKER_ALLOW_FAKE_EXIT")
    write_json(case_root / "BROKER_ALLOW_RESULT.json", {
        "decision": decision,
        "operation_intent": intent,
        "broker_result": result,
        "readback": evidence["snapshots"][-1]["tables"],
    })
    return {"plan": plan, "evidence": evidence, "review": review, "decision": decision, "result": result, "intent": intent}


def _control(name: str, expected: str, evidence: dict[str, Any], mutate: Callable[[dict[str, Any]], None]) -> dict[str, Any]:
    candidate = copy.deepcopy(evidence)
    mutate(candidate)
    result = review_observation_evidence(candidate)
    codes = sorted({item["code"] for item in result["issues"]})
    return {
        "control_id": name,
        "expected_reason": expected,
        "actual_reasons": codes,
        "actual_verdict": result["verdict"],
        "status": "PASS" if any(code == expected or code.startswith(expected) for code in codes) else "FAIL",
    }


def _fault_controls(positive: dict[str, Any], transient: dict[str, Any]) -> list[dict[str, Any]]:
    controls: list[dict[str, Any]] = []
    controls.append(_control("MISSING_BASELINE", "BASELINE_SNAPSHOT_MISSING", positive["evidence"], lambda e: e.__setitem__(
        "snapshots", [row for row in e["snapshots"] if row["label"] != "BASELINE_BEFORE_FIRST_START"]
    )))
    controls.append(_control("TARGET_SUBSTITUTION", "TARGET_DATABASE_SUBSTITUTED", positive["evidence"], lambda e: e.__setitem__("database", "C:/foreign.sqlite3")))
    controls.append(_control("LOGGER_GAP", "CAPTURE_GAP:FORCED_LOGGER_ERROR", positive["evidence"], lambda e: e["gaps"].append({"code": "FORCED_LOGGER_ERROR", "detail": "synthetic fault double"})))
    controls.append(_control("MISSING_END", "COLLECTOR_ENDED_BEFORE_OWNED_EXIT", positive["evidence"], lambda e: e["events"].__setitem__(-1, {**e["events"][-1], "kind": "END_REMOVED"})))
    controls.append(_control("TRUNCATED_AUDIT", "COMMITTED_AUDIT_SEQUENCE_GAP", transient["evidence"], lambda e: e["snapshots"][-1]["audit_rows"].pop(2)))
    controls.append(_control("CONFIG_CHANGED", "INSTRUMENT_CONFIGURATION_NOT_STABLE", positive["evidence"], lambda e: e["finalization"]["final_configuration"].__setitem__("configuration_hash", "0" * 64)))

    def jump(e: dict[str, Any]) -> None:
        pair = e["clock_pairs"][3]
        pair["utc_ns"] = str(int(pair["utc_ns"]) + 10_000_000_000)
    controls.append(_control("CLOCK_JUMP", "UTC_MONOTONIC_CORRELATION_JUMP", positive["evidence"], jump))

    def expanded(e: dict[str, Any]) -> None:
        phase = e["phases"]["S2_OPEN_CHECK"]
        phase["window_start_clock"]["monotonic_before_ns"] = "0"
    controls.append(_control("WINDOW_EXPANSION", "S2_OPEN_CHECK_WINDOW_EXCEEDS_CAPTURE", positive["evidence"], expanded))

    def unknown_writer(e: dict[str, Any]) -> None:
        e["snapshots"][-1]["audit_rows"][0]["transaction_id"] = "foreign-unregistered-transaction"
    controls.append(_control("UNKNOWN_WRITER", "AUDIT_EVENT_WITHOUT_COMMIT_RECEIPT", transient["evidence"], unknown_writer))

    def missing_snapshot(e: dict[str, Any]) -> None:
        e["phases"]["S2_OPEN_CHECK"]["end_snapshot_id"] = "snapshot:missing"
    controls.append(_control("MISSING_PHASE_SNAPSHOT", "PHASE_S2_OPEN_CHECK_BOUNDARY_INCOMPLETE", positive["evidence"], missing_snapshot))
    return controls


def _barrier_controls(readiness: dict[str, Any]) -> list[dict[str, Any]]:
    rows = []
    for control_id, mutate, expected in (
        ("BARRIER_MISSING_BASELINE", lambda r: r.__setitem__("baseline_snapshot_id", None), "PRE_EXECUTION_BASELINE_MISSING"),
        ("BARRIER_WRONG_TARGET", lambda r: r.__setitem__("status", "NOT_READY"), "PRE_EXECUTION_OBSERVATION_NOT_READY"),
        ("BARRIER_LOGGER_ERROR", lambda r: (r.__setitem__("status", "NOT_READY"), r["gaps"].append({"code": "LOGGER_ERROR"})), "PRE_EXECUTION_OBSERVATION_NOT_READY"),
    ):
        receipt = copy.deepcopy(readiness)
        mutate(receipt)
        try:
            from cgdr_r1_6b.prospective_observation import ProspectiveObservation
            ProspectiveObservation.validate_readiness_receipt(receipt)
            actual = "NO_ERROR"
        except ObservationError as exc:
            actual = exc.code
        rows.append({
            "control_id": control_id,
            "expected_reason": expected,
            "actual_reason": actual,
            "callback_count": 0,
            "validator_callback_capability": False,
            "status": "PASS" if actual == expected else "FAIL",
        })
    return rows


def _rehash_events(evidence: dict[str, Any]) -> None:
    previous = None
    for sequence, event in enumerate(evidence["events"], start=1):
        event["sequence"] = sequence
        event["previous_event_hash"] = previous
        event.pop("event_hash", None)
        event["event_hash"] = canonical_hash(event)
        previous = event["event_hash"]
    for name, phase in (evidence.get("phases") or {}).items():
        if phase.get("binding_version") != "CGDR_PHASE_SNAPSHOT_CLOCK_EVENT_AUDIT_V2":
            continue
        begin = next(
            (row for row in evidence["events"] if row.get("kind") == "PHASE_BEGIN" and row.get("phase") == name),
            None,
        )
        end = next(
            (row for row in evidence["events"] if row.get("kind") == "PHASE_END" and row.get("phase") == name),
            None,
        )
        if begin is not None:
            phase["begin_event_ref"] = {"sequence": begin["sequence"], "event_hash": begin["event_hash"]}
        if end is not None:
            phase["end_event_ref"] = {"sequence": end["sequence"], "event_hash": end["event_hash"]}


def _phase_control(
    control_id: str,
    evidence: dict[str, Any],
    mutate: Callable[[dict[str, Any]], None],
    expected_reasons: list[str],
    *,
    phase: str = "OPEN_CHECK",
) -> dict[str, Any]:
    candidate = copy.deepcopy(evidence)
    mutate(candidate)
    review = review_observation_evidence(candidate)
    material = build_phase_native_material(candidate, review, phase)
    actual_reasons = sorted({item["code"] for item in review["issues"]})
    matched = all(reason in actual_reasons for reason in expected_reasons)
    return {
        "control_id": control_id,
        "expected_reasons": expected_reasons,
        "actual_reasons": actual_reasons,
        "actual_verdict": review["verdict"],
        "phase_result": (review.get("phase_results") or {}).get(phase),
        "audit_coverage": review.get("audit_coverage"),
        "strongest_material": material,
        "status": "PASS" if matched and review["verdict"] != "PASS_COMPLETE_WITHIN_DECLARED_SURFACES" and material["status"].startswith("REFUSED") else "FAIL",
    }


def _phase_binding_controls(transient: dict[str, Any]) -> list[dict[str, Any]]:
    evidence = transient["evidence"]
    rows: list[dict[str, Any]] = []

    def rebound_clocks(candidate: dict[str, Any]) -> None:
        candidate["phases"]["OPEN_CHECK"]["window_start_clock"] = copy.deepcopy(
            candidate["phases"]["RESOLVED_CHECK"]["window_start_clock"]
        )
        candidate["phases"]["OPEN_CHECK"]["window_end_clock"] = copy.deepcopy(
            candidate["phases"]["RESOLVED_CHECK"]["window_end_clock"]
        )

    rows.append(_phase_control(
        "K01_REBOUND_OPEN_WINDOW_TO_RESOLVED_CLOCKS",
        evidence,
        rebound_clocks,
        ["PHASE_WINDOW_START_SNAPSHOT_CLOCK_MISMATCH", "PHASE_WINDOW_END_SNAPSHOT_CLOCK_MISMATCH"],
    ))

    def reverse_snapshot_refs(candidate: dict[str, Any]) -> None:
        phase = candidate["phases"]["OPEN_CHECK"]
        other = candidate["phases"]["RESOLVED_CHECK"]
        phase["begin_snapshot_id"] = other["begin_snapshot_id"]
        phase["end_snapshot_id"] = other["end_snapshot_id"]

    rows.append(_phase_control(
        "K01_REBOUND_OPEN_SNAPSHOT_REFS",
        evidence,
        reverse_snapshot_refs,
        ["PHASE_BEGIN_EVENT_SNAPSHOT_REF_MISMATCH", "PHASE_END_EVENT_SNAPSHOT_REF_MISMATCH"],
    ))

    def wrong_phase_event(candidate: dict[str, Any]) -> None:
        other_end = candidate["phases"]["RESOLVED_CHECK"]["end_snapshot_id"]
        event = next(
            row for row in candidate["events"]
            if row.get("kind") == "PHASE_END" and row.get("phase") == "OPEN_CHECK"
        )
        event["snapshot_id"] = other_end
        _rehash_events(candidate)

    rows.append(_phase_control(
        "K01_WRONG_PHASE_EVENT_SNAPSHOT_BINDING",
        evidence,
        wrong_phase_event,
        ["PHASE_JOURNAL_EVENT_MALFORMED", "PHASE_END_EVENT_BINDING_MISMATCH"],
    ))

    def missing_resolved_descriptor(candidate: dict[str, Any]) -> None:
        del candidate["phases"]["RESOLVED_CHECK"]

    rows.append(_phase_control(
        "K02_MISSING_RESOLVED_DESCRIPTOR_WITH_NINE_AUDIT_ROWS",
        evidence,
        missing_resolved_descriptor,
        ["PHASE_DESCRIPTOR_MISSING_FROM_FROZEN_INVENTORY", "PHASE_DESCRIPTOR_MISSING_FOR_JOURNAL_EVENTS", "COMMITTED_AUDIT_EVENTS_OUTSIDE_DESCRIBED_PHASES"],
    ))

    rows.append(_phase_control(
        "K02_EMPTY_PHASE_DESCRIPTORS_WITH_PHASE_JOURNAL",
        evidence,
        lambda candidate: candidate.__setitem__("phases", {}),
        ["PHASE_DESCRIPTOR_MISSING_FOR_JOURNAL_EVENTS", "COMMITTED_AUDIT_EVENTS_OUTSIDE_DESCRIBED_PHASES"],
    ))

    def duplicate_begin(candidate: dict[str, Any]) -> None:
        index = next(
            index for index, row in enumerate(candidate["events"])
            if row.get("kind") == "PHASE_BEGIN" and row.get("phase") == "RESOLVED_CHECK"
        )
        candidate["events"].insert(index + 1, copy.deepcopy(candidate["events"][index]))
        _rehash_events(candidate)

    rows.append(_phase_control(
        "K02_DUPLICATE_PHASE_BEGIN_EVENT",
        evidence,
        duplicate_begin,
        ["PHASE_EVENT_PAIR_CARDINALITY_INVALID"],
        phase="RESOLVED_CHECK",
    ))

    def missing_end(candidate: dict[str, Any]) -> None:
        candidate["events"] = [
            row for row in candidate["events"]
            if not (row.get("kind") == "PHASE_END" and row.get("phase") == "RESOLVED_CHECK")
        ]
        _rehash_events(candidate)

    rows.append(_phase_control(
        "K02_UNPAIRED_PHASE_BEGIN_EVENT",
        evidence,
        missing_end,
        ["PHASE_EVENT_PAIR_CARDINALITY_INVALID"],
        phase="RESOLVED_CHECK",
    ))

    positive = review_observation_evidence(evidence)
    rows.append({
        "control_id": "K01_K02_POSITIVE_TWO_PHASE_OPEN_THEN_RESOLVED",
        "expected_reasons": [],
        "actual_reasons": [item["code"] for item in positive["issues"]],
        "actual_verdict": positive["verdict"],
        "open_phase": positive["phase_results"]["OPEN_CHECK"],
        "resolved_phase": positive["phase_results"]["RESOLVED_CHECK"],
        "audit_coverage": positive["audit_coverage"],
        "status": "PASS" if (
            positive["verdict"] == "OBSERVED_COMMITTED_CHANGE"
            and positive["phase_results"]["OPEN_CHECK"]["status"] == "COMPLETE_NO_COMMITTED_CHANGE"
            and positive["phase_results"]["RESOLVED_CHECK"]["committed_event_count"] == 9
            and positive["audit_coverage"]["uncovered_audit_sequences"] == []
        ) else "FAIL",
    })
    return rows


def _r1_6m_phase_v2_controls(transient: dict[str, Any]) -> list[dict[str, Any]]:
    evidence = transient["evidence"]
    rows: list[dict[str, Any]] = []

    def exact_downgrade(candidate: dict[str, Any]) -> None:
        phase = candidate["phases"]["OPEN_CHECK"]
        for key in (
            "binding_version", "phase_id", "phase_order", "begin_event_ref", "end_event_ref",
            "begin_snapshot_hash", "end_snapshot_hash",
        ):
            phase.pop(key, None)
        for event in candidate["events"]:
            if event.get("kind") in {"PHASE_BEGIN", "PHASE_END"} and event.get("phase") == "OPEN_CHECK":
                event.update(task_id="FOREIGN_TASK", attempt_id="FOREIGN_ATTEMPT", phase_id="phase:foreign", phase_order=99)
        _rehash_events(candidate)

    rows.append(_phase_control(
        "L01_EXACT_B_DOWNGRADE_BY_OMISSION",
        evidence,
        exact_downgrade,
        ["PHASE_V2_REQUIRED_FIELD_MISSING", "PHASE_JOURNAL_EVENT_MALFORMED"],
    ))

    for field in (
        "name", "phase_id", "phase_order", "binding_version", "status",
        "begin_snapshot_id", "begin_snapshot", "begin_snapshot_hash",
        "end_snapshot_id", "end_snapshot", "end_snapshot_hash",
        "start_audit_seq", "end_audit_seq", "window_start_clock", "window_end_clock",
        "begin_event_ref", "end_event_ref",
    ):
        rows.append(_phase_control(
            f"L01_REQUIRED_DESCRIPTOR_FIELD_OMITTED:{field}",
            evidence,
            lambda candidate, field=field: candidate["phases"]["OPEN_CHECK"].pop(field),
            ["PHASE_V2_REQUIRED_FIELD_MISSING"],
        ))

    for label, value in (
        ("NULL", None),
        ("EMPTY", ""),
        ("LEGACY", "LEGACY"),
        ("UNKNOWN", "CGDR_PHASE_SNAPSHOT_CLOCK_EVENT_AUDIT_V3"),
        ("NON_STRING", 7),
    ):
        rows.append(_phase_control(
            f"L01_BINDING_VERSION_{label}",
            evidence,
            lambda candidate, value=value: candidate["phases"]["OPEN_CHECK"].__setitem__("binding_version", value),
            [
                "PHASE_BINDING_VERSION_MISMATCH"
                if isinstance(value, str) and value
                else "PHASE_V2_REQUIRED_FIELD_TYPE_INVALID"
                if value is not None
                else "PHASE_V2_REQUIRED_FIELD_MISSING"
            ],
        ))

    def substitute_snapshot_content(candidate: dict[str, Any]) -> None:
        phase = candidate["phases"]["OPEN_CHECK"]
        other = candidate["phases"]["RESOLVED_CHECK"]
        phase["begin_snapshot"] = copy.deepcopy(other["begin_snapshot"])
        phase["end_snapshot"] = copy.deepcopy(other["end_snapshot"])
    rows.append(_phase_control(
        "L01_SUBSTITUTED_SNAPSHOT_CONTENT",
        evidence,
        substitute_snapshot_content,
        ["PHASE_BEGIN_SNAPSHOT_CONTENT_MISMATCH", "PHASE_END_SNAPSHOT_CONTENT_MISMATCH"],
    ))

    def substitute_snapshot_hashes(candidate: dict[str, Any]) -> None:
        phase = candidate["phases"]["OPEN_CHECK"]
        other = candidate["phases"]["RESOLVED_CHECK"]
        phase["begin_snapshot_hash"] = other["begin_snapshot_hash"]
        phase["end_snapshot_hash"] = other["end_snapshot_hash"]
    rows.append(_phase_control(
        "L01_SUBSTITUTED_SNAPSHOT_HASHES",
        evidence,
        substitute_snapshot_hashes,
        ["PHASE_BEGIN_SNAPSHOT_HASH_MISMATCH", "PHASE_END_SNAPSHOT_HASH_MISMATCH"],
    ))

    def empty_phase_events(candidate: dict[str, Any]) -> None:
        insert_at = next(i for i, row in enumerate(candidate["events"]) if row.get("kind") in {"SYNTHETIC_OWNED_EXIT_CALLBACK", "OWNED_EXIT_OBSERVED"})
        clock_id = candidate["events"][insert_at - 1]["clock_pair_id"]
        candidate["events"][insert_at:insert_at] = [
            {"sequence": 0, "kind": "PHASE_BEGIN", "clock_pair_id": clock_id, "previous_event_hash": None, "phase": "", "phase_id": "phase:undeclared", "phase_order": 77, "snapshot_id": "snapshot:missing"},
            {"sequence": 0, "kind": "PHASE_END", "clock_pair_id": clock_id, "previous_event_hash": None, "phase": "", "phase_id": "phase:undeclared", "phase_order": 77, "snapshot_id": "snapshot:missing"},
        ]
        _rehash_events(candidate)

    rows.append(_phase_control(
        "L04_EXACT_B_EMPTY_PHASE_BEGIN_END",
        evidence,
        empty_phase_events,
        ["PHASE_JOURNAL_EVENT_MALFORMED"],
    ))

    for label, value in (("NULL", None), ("NON_STRING", 7), ("EMPTY", ""), ("WHITESPACE", "   ")):
        def mutate_phase(candidate: dict[str, Any], value: Any = value) -> None:
            event = next(row for row in candidate["events"] if row.get("kind") == "PHASE_BEGIN" and row.get("phase") == "OPEN_CHECK")
            event["phase"] = value
            _rehash_events(candidate)
        rows.append(_phase_control(
            f"L04_PHASE_VALUE_{label}",
            evidence,
            mutate_phase,
            ["PHASE_JOURNAL_EVENT_MALFORMED"],
        ))

    def missing_phase(candidate: dict[str, Any]) -> None:
        event = next(row for row in candidate["events"] if row.get("kind") == "PHASE_BEGIN" and row.get("phase") == "OPEN_CHECK")
        event.pop("phase")
        _rehash_events(candidate)
    rows.append(_phase_control(
        "L04_PHASE_KEY_MISSING",
        evidence,
        missing_phase,
        ["PHASE_JOURNAL_EVENT_MALFORMED"],
    ))

    for field in (
        "task_id", "attempt_id", "phase_id", "phase_order", "snapshot_id", "snapshot_hash",
        "snapshot_audit_seq", "snapshot_read_begin_clock_id", "snapshot_read_end_clock_id",
        "window_clock_pair_id", "clock_pair_id",
    ):
        def omit_event_field(candidate: dict[str, Any], field: str = field) -> None:
            event = next(row for row in candidate["events"] if row.get("kind") == "PHASE_BEGIN" and row.get("phase") == "OPEN_CHECK")
            event.pop(field)
            _rehash_events(candidate)
        rows.append(_phase_control(
            f"L04_REQUIRED_EVENT_FIELD_OMITTED:{field}",
            evidence,
            omit_event_field,
            ["PHASE_JOURNAL_EVENT_MALFORMED"],
        ))

    def outside_inventory(candidate: dict[str, Any]) -> None:
        originals = [
            row for row in candidate["events"]
            if row.get("kind") in {"PHASE_BEGIN", "PHASE_END"} and row.get("phase") == "OPEN_CHECK"
        ]
        extras = copy.deepcopy(originals)
        for event in extras:
            event["phase"] = "UNKNOWN_CHECK"
            event["phase_id"] = f"phase:{candidate['attempt_id']}:3:UNKNOWN_CHECK"
            event["phase_order"] = 3
        insert_at = next(i for i, row in enumerate(candidate["events"]) if row.get("kind") == "SYNTHETIC_OWNED_EXIT_CALLBACK")
        candidate["events"][insert_at:insert_at] = extras
        _rehash_events(candidate)
    rows.append(_phase_control(
        "L04_UNKNOWN_PHASE_OUTSIDE_FROZEN_INVENTORY",
        evidence,
        outside_inventory,
        ["PHASE_JOURNAL_EVENT_OUTSIDE_FROZEN_INVENTORY"],
    ))

    def malformed_beside_two_normal(candidate: dict[str, Any]) -> None:
        event = copy.deepcopy(next(
            row for row in candidate["events"]
            if row.get("kind") == "PHASE_BEGIN" and row.get("phase") == "RESOLVED_CHECK"
        ))
        event["phase"] = "   "
        insert_at = next(i for i, row in enumerate(candidate["events"]) if row.get("kind") == "SYNTHETIC_OWNED_EXIT_CALLBACK")
        candidate["events"].insert(insert_at, event)
        _rehash_events(candidate)
    rows.append(_phase_control(
        "L04_ONE_MALFORMED_EVENT_BESIDE_TWO_NORMAL_PHASES",
        evidence,
        malformed_beside_two_normal,
        ["PHASE_JOURNAL_EVENT_MALFORMED"],
    ))
    return rows


def _r1_6m_review_binding_controls(
    positive: dict[str, Any], transient: dict[str, Any]
) -> list[dict[str, Any]]:
    evidence = transient["evidence"]
    clean = review_observation_evidence(evidence)
    rows: list[dict[str, Any]] = []

    def row(control_id: str, candidate: dict[str, Any], supplied: dict[str, Any], expected: str) -> None:
        material = build_phase_native_material(candidate, supplied, "OPEN_CHECK")
        rows.append({
            "control_id": control_id,
            "expected_reason_or_status": expected,
            "actual": material,
            "reviewed_evidence_hash": supplied.get("reviewed_evidence_hash"),
            "reviewed_plan_hash": supplied.get("reviewed_plan_hash"),
            "status": "PASS" if material.get("reason", material.get("status")) == expected else "FAIL",
        })

    row("L02_EXACT_CLEAN_REVIEW_AND_EVIDENCE", evidence, clean, "COMPLETE_NO_COMMITTED_CHANGE")

    changed_clocks = copy.deepcopy(evidence)
    changed_clocks["phases"]["OPEN_CHECK"]["window_start_clock"] = copy.deepcopy(changed_clocks["phases"]["RESOLVED_CHECK"]["window_start_clock"])
    changed_clocks["phases"]["OPEN_CHECK"]["window_end_clock"] = copy.deepcopy(changed_clocks["phases"]["RESOLVED_CHECK"]["window_end_clock"])
    row("L02_CLEAN_REVIEW_CHANGED_CLOCKS", changed_clocks, clean, "REVIEW_EVIDENCE_BINDING_MISMATCH")

    same_plan_change = copy.deepcopy(evidence)
    same_plan_change["claim_boundary"] += " altered evidence only"
    row("L02_SAME_PLAN_HASH_CHANGED_EVIDENCE", same_plan_change, clean, "REVIEW_EVIDENCE_BINDING_MISMATCH")

    attacker = copy.deepcopy(clean)
    attacker["reviewed_evidence_hash"] = canonical_hash(changed_clocks)
    attacker["reviewed_plan_hash"] = changed_clocks["plan_hash"]
    row("L02_HASH_FIELDS_ONLY_ATTACK", changed_clocks, attacker, "REVIEW_EVIDENCE_BINDING_MISMATCH")

    row(
        "L02_REVIEW_FROM_OTHER_EVIDENCE",
        evidence,
        review_observation_evidence(positive["evidence"]),
        "REVIEW_EVIDENCE_BINDING_MISMATCH",
    )
    for field in ("reviewed_evidence_hash", "reviewed_plan_hash"):
        missing = copy.deepcopy(clean)
        missing.pop(field)
        row(f"L02_MISSING_{field.upper()}", evidence, missing, "REVIEW_EVIDENCE_BINDING_MISMATCH")

    def reverse_keys(value: Any) -> Any:
        if isinstance(value, dict):
            return {key: reverse_keys(value[key]) for key in reversed(list(value))}
        if isinstance(value, list):
            return [reverse_keys(item) for item in value]
        return value

    reordered_evidence = reverse_keys(evidence)
    row(
        "L02_JSON_KEY_ORDER_INVARIANT",
        reordered_evidence,
        review_observation_evidence(reordered_evidence),
        "COMPLETE_NO_COMMITTED_CHANGE",
    )
    return rows


def _new_gap_observation(
    root: Path,
    case: str,
    source: dict[str, Any],
    attempt: str,
    instance: str,
) -> tuple[Any, Any]:
    plan = _plan(root, case, source, attempt, instance)
    return prepare_prospective_observation(
        plan=plan,
        output=root / "cases" / case / "observation",
    )


def _gap_admission_controls(
    root: Path,
    keys: TestKeyStore,
    public_map: dict[str, Any],
) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []

    source = immutable_source("R1L_GAP_WRITER")
    broker, observer = _new_gap_observation(
        root, "gap_blocks_writer", source, "r1-6l-gap-writer", "calibration-gap-writer"
    )
    observer.invoke_first_start(lambda: {"process_started": False})
    observer.begin_phase("S2_OPEN_CHECK")
    observer.note_gap("CALIBRATION_KNOWN_GAP", "known loss before next writer")
    try:
        observer.begin_writer_transaction(
            "txn-after-gap",
            operation_id="operation:after-gap",
            interface="bounded_calibration_dml",
        )
        writer_reason = "NO_ERROR"
    except ObservationError as exc:
        writer_reason = exc.code
    effect_rows = broker.db.execute("SELECT count(*) FROM effects").fetchone()[0]
    observer.end_phase("S2_OPEN_CHECK")
    evidence, review = _finish_case(
        root / "cases" / "gap_blocks_writer", broker, observer, binding_label="GAP_WRITER_FAKE_EXIT"
    )
    material = build_phase_native_material(evidence, review, "S2_OPEN_CHECK")
    rows.append({
        "control_id": "K03_READY_GAP_BLOCKS_NEXT_WRITER",
        "expected_reason": "KNOWN_CAPTURE_GAP_ADMISSION_BLOCKED",
        "actual_reason": writer_reason,
        "effect_rows_after_refusal": effect_rows,
        "final_verdict": review["verdict"],
        "strongest_material": material,
        "status": "PASS" if (
            writer_reason == "KNOWN_CAPTURE_GAP_ADMISSION_BLOCKED"
            and effect_rows == 0
            and review["verdict"] == "INCONCLUSIVE"
            and material["status"] == "REFUSED_INCOMPLETE"
        ) else "FAIL",
    })

    attempt, instance = "r1-6l-gap-gate", "calibration-gap-gate"
    source = _open_current_source(attempt, instance, keys, public_map)
    broker, observer = _new_gap_observation(root, "gap_blocks_gate", source, attempt, instance)
    observer.invoke_first_start(lambda: {"process_started": False})
    stale_ready = observer.readiness_receipt()
    observer.note_gap("CALIBRATION_KNOWN_GAP", "known loss before protected gate")
    bind_calls = 0
    original_bind = broker.bind_instance

    def counted_bind(*args: Any, **kwargs: Any) -> Any:
        nonlocal bind_calls
        bind_calls += 1
        return original_bind(*args, **kwargs)

    broker.bind_instance = counted_bind  # type: ignore[method-assign]
    try:
        run_hold_gate(
            broker=broker,
            observation=observer,
            source=source,
            keys=keys,
            public_map=public_map,
            attempt_id=attempt,
            instance_id=instance,
        )
        gate_reason = "NO_ERROR"
    except ObservationError as exc:
        gate_reason = exc.code
    observer.mark_owned_exit(
        synthetic=True,
        binding={"kind": "GAP_GATE_FAKE_EXIT", "process_started": False},
    )
    gate_evidence = observer.finalize()
    gate_review = review_observation_evidence(gate_evidence)
    write_json(root / "cases" / "gap_blocks_gate" / "OBSERVATION_REVIEW.json", gate_review)
    broker.close()
    rows.append({
        "control_id": "K03_GAP_BLOCKS_BORROWED_BROKER_GATE",
        "expected_reason": "KNOWN_CAPTURE_GAP_ADMISSION_BLOCKED",
        "actual_reason": gate_reason,
        "protected_bind_callback_count": bind_calls,
        "stale_ready_status_before_gap": stale_ready["status"],
        "final_verdict": gate_review["verdict"],
        "status": "PASS" if gate_reason == "KNOWN_CAPTURE_GAP_ADMISSION_BLOCKED" and bind_calls == 0 else "FAIL",
    })

    source = immutable_source("R1L_GAP_START")
    broker, observer = _new_gap_observation(
        root, "gap_blocks_start", source, "r1-6l-gap-start", "calibration-gap-start"
    )
    stale_ready = observer.readiness_receipt()
    observer.note_gap("CALIBRATION_KNOWN_GAP", "known loss before first-start seam")
    callbacks: list[str] = []
    try:
        observer.invoke_first_start(
            lambda: callbacks.append("CALLED"),
            readiness_receipt=stale_ready,
        )
        start_reason = "NO_ERROR"
    except ObservationError as exc:
        start_reason = exc.code
    observer.mark_owned_exit(
        synthetic=True,
        binding={"kind": "GAP_START_FAKE_EXIT", "process_started": False},
    )
    start_evidence = observer.finalize()
    start_review = review_observation_evidence(start_evidence)
    write_json(root / "cases" / "gap_blocks_start" / "OBSERVATION_REVIEW.json", start_review)
    broker.close()
    rows.append({
        "control_id": "K03_STALE_READY_CANNOT_BYPASS_GAP_AT_START_SEAM",
        "expected_reason": "KNOWN_CAPTURE_GAP_ADMISSION_BLOCKED",
        "actual_reason": start_reason,
        "callback_count": len(callbacks),
        "final_verdict": start_review["verdict"],
        "status": "PASS" if start_reason == "KNOWN_CAPTURE_GAP_ADMISSION_BLOCKED" and callbacks == [] else "FAIL",
    })

    source = immutable_source("R1L_GAP_ROLLBACK")
    broker, observer = _new_gap_observation(
        root, "gap_allows_diagnostic_rollback", source, "r1-6l-gap-rollback", "calibration-gap-rollback"
    )
    observer.invoke_first_start(lambda: {"process_started": False})
    observer.begin_phase("S2_OPEN_CHECK")
    observer.begin_writer_transaction(
        "txn-gap-rollback",
        operation_id="operation:gap-rollback",
        interface="bounded_calibration_dml",
    )
    broker.db.execute("BEGIN IMMEDIATE")
    broker.db.execute(
        "INSERT INTO effects VALUES(?,?,?,?)",
        ("effect:gap-rollback", "operation:gap-rollback", "R1L_GAP_ROLLBACK", json.dumps({"rolled_back": True})),
    )
    observer.note_gap("CALIBRATION_KNOWN_GAP", "gap while transaction requires diagnostic rollback")
    broker.db.rollback()
    observer.finish_writer_transaction(
        "txn-gap-rollback",
        "ROLLED_BACK",
        reason="DIAGNOSTIC_ROLLBACK_AFTER_GAP",
    )
    observer.end_phase("S2_OPEN_CHECK")
    diagnostic_evidence, diagnostic_review = _finish_case(
        root / "cases" / "gap_allows_diagnostic_rollback",
        broker,
        observer,
        binding_label="GAP_ROLLBACK_FAKE_EXIT",
    )
    rows.append({
        "control_id": "K03_GAP_RETAINS_DIAGNOSTIC_ROLLBACK_AND_FINALIZATION",
        "expected_reason": "CAPTURE_GAP:CALIBRATION_KNOWN_GAP",
        "actual_reasons": sorted({item["code"] for item in diagnostic_review["issues"]}),
        "rolled_back_attempt_count": diagnostic_review["rolled_back_attempt_count"],
        "committed_audit_event_count": diagnostic_review["committed_audit_event_count"],
        "final_effect_rows": diagnostic_evidence["snapshots"][-1]["tables"]["effects"]["row_count"],
        "final_verdict": diagnostic_review["verdict"],
        "status": "PASS" if (
            "CAPTURE_GAP:CALIBRATION_KNOWN_GAP" in {item["code"] for item in diagnostic_review["issues"]}
            and diagnostic_review["rolled_back_attempt_count"] == 1
            and diagnostic_review["committed_audit_event_count"] == 0
            and diagnostic_review["verdict"] == "INCONCLUSIVE"
        ) else "FAIL",
    })
    return rows


def _r1_6m_start_authorization_controls(root: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []

    source = immutable_source("R1M_FORMER_API")
    broker, observer = _new_gap_observation(
        root, "r1_6m_former_api_after_gap", source, "r1-6m-former-api", "instance-former-api"
    )
    stale = observer.readiness_receipt()
    observer.note_gap("L03_GAP", "sticky live gap before former receipt-only API attempt")
    callbacks: list[str] = []
    try:
        getattr(ProspectiveObservation, "authorize_from_receipt")(
            stale,
            lambda: callbacks.append("CALLED"),
        )
        former_reason = "NO_ERROR"
    except AttributeError:
        former_reason = "STATE_FREE_CALLBACK_API_ABSENT"
    observer.mark_owned_exit(synthetic=True, binding={"kind": "L03_FORMER_API_FAKE_EXIT", "process_started": False})
    observer.finalize()
    broker.close()
    rows.append({
        "control_id": "L03_EXACT_B_READY_GAP_FORMER_PUBLIC_API",
        "expected_reason": "STATE_FREE_CALLBACK_API_ABSENT",
        "actual_reason": former_reason,
        "callback_count": len(callbacks),
        "status": "PASS" if former_reason == "STATE_FREE_CALLBACK_API_ABSENT" and not callbacks else "FAIL",
    })

    source_old = immutable_source("R1M_OLD_RECEIPT")
    source_new = immutable_source("R1M_NEW_RECEIPT")
    broker_old, observer_old = _new_gap_observation(
        root, "r1_6m_old_receipt", source_old, "r1-6m-old-receipt", "instance-old"
    )
    broker_new, observer_new = _new_gap_observation(
        root, "r1_6m_new_receipt", source_new, "r1-6m-new-receipt", "instance-new"
    )
    callbacks = []
    try:
        observer_new.invoke_first_start(
            lambda: callbacks.append("CALLED"),
            readiness_receipt=observer_old.readiness_receipt(),
        )
        stale_reason = "NO_ERROR"
    except ObservationError as exc:
        stale_reason = exc.code
    observer_old.mark_owned_exit(synthetic=True, binding={"kind": "OLD_RECEIPT_FAKE_EXIT", "process_started": False})
    observer_new.mark_owned_exit(synthetic=True, binding={"kind": "NEW_RECEIPT_FAKE_EXIT", "process_started": False})
    observer_old.finalize()
    observer_new.finalize()
    broker_old.close()
    broker_new.close()
    rows.append({
        "control_id": "L03_OLDER_RECEIPT_CANNOT_AUTHORIZE_NEW_LIVE_OBSERVATION",
        "expected_reason": "STALE_OBSERVATION_READINESS_RECEIPT",
        "actual_reason": stale_reason,
        "callback_count": len(callbacks),
        "status": "PASS" if stale_reason == "STALE_OBSERVATION_READINESS_RECEIPT" and not callbacks else "FAIL",
    })

    source = immutable_source("R1M_REPLAY")
    broker, observer = _new_gap_observation(
        root, "r1_6m_current_once_replay", source, "r1-6m-current-replay", "instance-replay"
    )
    receipt = observer.readiness_receipt()
    callbacks = []
    observer.invoke_first_start(lambda: callbacks.append("CALLED"), readiness_receipt=receipt)
    try:
        observer.invoke_first_start(lambda: callbacks.append("CALLED_AGAIN"), readiness_receipt=receipt)
        replay_reason = "NO_ERROR"
    except ObservationError as exc:
        replay_reason = exc.code
    observer.mark_owned_exit(synthetic=True, binding={"kind": "REPLAY_FAKE_EXIT", "process_started": False})
    observer.finalize()
    broker.close()
    rows.append({
        "control_id": "L03_CURRENT_RECEIPT_ONCE_THEN_REPLAY",
        "expected_reason": "FIRST_START_CALLBACK_REPLAYED",
        "actual_reason": replay_reason,
        "callback_count": len(callbacks),
        "status": "PASS" if replay_reason == "FIRST_START_CALLBACK_REPLAYED" and callbacks == ["CALLED"] else "FAIL",
    })

    source = immutable_source("R1M_INVALID_RECEIPT")
    broker, observer = _new_gap_observation(
        root, "r1_6m_invalid_receipts", source, "r1-6m-invalid-receipts", "instance-invalid"
    )
    invalid_rows = []
    callbacks = []
    for field, value in (
        ("schema", None),
        ("status", "NOT_READY"),
        ("plan_hash", None),
        ("configuration_hash", None),
        ("baseline_snapshot_id", None),
        ("baseline_snapshot_hash", None),
        ("ready_event", None),
    ):
        candidate = observer.readiness_receipt()
        candidate[field] = value
        before = sum(row.get("kind") == "FIRST_START_CALLBACK_AUTHORIZED" for row in observer._events)
        try:
            observer.invoke_first_start(lambda: callbacks.append("CALLED"), readiness_receipt=candidate)
            actual = "NO_ERROR"
        except ObservationError as exc:
            actual = exc.code
        after = sum(row.get("kind") == "FIRST_START_CALLBACK_AUTHORIZED" for row in observer._events)
        invalid_rows.append({
            "field": field,
            "actual_reason": actual,
            "authorized_event_delta": after - before,
            "status": "PASS" if actual != "NO_ERROR" and after == before else "FAIL",
        })
    observer.mark_owned_exit(synthetic=True, binding={"kind": "INVALID_RECEIPT_FAKE_EXIT", "process_started": False})
    observer.finalize()
    broker.close()
    rows.append({
        "control_id": "L03_INVALID_RECEIPTS_BEFORE_AUTHORIZED_EVENT",
        "cases": invalid_rows,
        "callback_count": len(callbacks),
        "status": "PASS" if not callbacks and all(row["status"] == "PASS" for row in invalid_rows) else "FAIL",
    })

    callback_methods = []
    for name, member in inspect.getmembers(ProspectiveObservation, predicate=inspect.isfunction):
        if not name.startswith("_") and "callback" in inspect.signature(member).parameters:
            callback_methods.append(name)
    rows.append({
        "control_id": "L03_PUBLIC_CALLBACK_API_INTROSPECTION",
        "expected_callback_methods": ["invoke_first_start"],
        "actual_callback_methods": callback_methods,
        "authorize_from_receipt_present": hasattr(ProspectiveObservation, "authorize_from_receipt"),
        "status": "PASS" if callback_methods == ["invoke_first_start"] and not hasattr(ProspectiveObservation, "authorize_from_receipt") else "FAIL",
    })
    return rows


def run(output: Path) -> dict[str, Any]:
    output = output.resolve()
    output.mkdir(parents=True, exist_ok=False)
    with tempfile.TemporaryDirectory(prefix="cgdr-r1-6k-keys-") as private_key_dir:
        keys = TestKeyStore(Path(private_key_dir))
        public_map = authority_public_map(keys)
        positive = _positive_hold(output, keys, public_map)
        transient = _transient_changes(output)
        rollback = _rollback(output)
        allow = _broker_allow(output, keys, public_map)
        gap_controls = _gap_admission_controls(output, keys, public_map)
    controls = _fault_controls(positive, transient)
    barriers = _barrier_controls(positive["readiness"])
    phase_controls = _phase_binding_controls(transient)
    r1_6m_phase_controls = _r1_6m_phase_v2_controls(transient)
    review_binding_controls = _r1_6m_review_binding_controls(positive, transient)
    start_authorization_controls = _r1_6m_start_authorization_controls(output)
    open_phase = transient["review"]["phase_results"]["OPEN_CHECK"]
    resolved_phase = transient["review"]["phase_results"]["RESOLVED_CHECK"]
    committed = transient["evidence"]["snapshots"][-1]["audit_rows"] + allow["evidence"]["snapshots"][-1]["audit_rows"]
    counts: dict[str, dict[str, int]] = {surface: {kind: 0 for kind in ("INSERT", "UPDATE", "DELETE")} for surface in ("effects", "promotions")}
    for row in committed:
        counts[row["surface_id"]][row["dml_kind"]] += 1
    results = {
        "task_id": TASK_ID,
        "repair_iteration_task_id": ITERATION_TASK_ID,
        "scope": "LOCAL_SQLITE_CALIBRATION_ONLY_NO_WORKER_HELPER_WSL_OR_S2",
        "status": "PASS" if (
            positive["review"]["verdict"] == "PASS_COMPLETE_WITHIN_DECLARED_SURFACES"
            and positive["native"].get("accepted") is True
            and transient["review"]["verdict"] == "OBSERVED_COMMITTED_CHANGE"
            and transient["native_refusal"].get("status") == "REFUSED_EFFECT_OR_GAP"
            and rollback["review"]["rolled_back_attempt_count"] == 1
            and rollback["review"]["committed_audit_event_count"] == 0
            and allow["result"].get("result") == "BOUND"
            and allow["review"]["verdict"] == "OBSERVED_COMMITTED_CHANGE"
            and all(row["status"] == "PASS" for row in controls + barriers)
            and all(row["status"] == "PASS" for row in phase_controls + gap_controls)
            and all(row["status"] == "PASS" for row in r1_6m_phase_controls)
            and all(row["status"] == "PASS" for row in review_binding_controls)
            and all(row["status"] == "PASS" for row in start_authorization_controls)
            and open_phase["status"] == "COMPLETE_NO_COMMITTED_CHANGE"
            and resolved_phase["status"] == "EFFECT_DETECTED"
        ) else "FAIL",
        "unique_calibration_cases": 4,
        "fault_controls": len(controls),
        "barrier_control_count": len(barriers),
        "phase_binding_control_count": len(phase_controls),
        "gap_admission_control_count": len(gap_controls),
        "r1_6m_phase_v2_control_count": len(r1_6m_phase_controls),
        "r1_6m_review_binding_control_count": len(review_binding_controls),
        "r1_6m_start_authorization_control_count": len(start_authorization_controls),
        "positive_hold": {
            "review_verdict": positive["review"]["verdict"],
            "effect_delta": positive["gate"]["broker_result"]["effect_delta"],
            "promotion_delta": 0,
            "native_layers": positive["native"]["layer_status"],
        },
        "transient_changes": {
            "review_verdict": transient["review"]["verdict"],
            "final_effect_rows": transient["evidence"]["snapshots"][-1]["tables"]["effects"]["row_count"],
            "final_promotion_rows": transient["evidence"]["snapshots"][-1]["tables"]["promotions"]["row_count"],
            "committed_audit_events": transient["review"]["committed_audit_event_count"],
            "open_phase": open_phase,
            "resolved_phase": resolved_phase,
            "native_emission": transient["native_refusal"],
            "sql_forms_exercised": ["INSERT", "UPDATE", "DELETE", "INSERT_OR_REPLACE", "ON_CONFLICT_DO_UPDATE"],
        },
        "rollback": {
            "rolled_back_attempts": rollback["review"]["rolled_back_attempt_count"],
            "committed_audit_events": rollback["review"]["committed_audit_event_count"],
            "final_effect_rows": rollback["evidence"]["snapshots"][-1]["tables"]["effects"]["row_count"],
        },
        "positive_broker_commit": {
            "broker_result": allow["result"],
            "review_verdict": allow["review"]["verdict"],
            "exact_operation_id": allow["intent"]["scope"]["operation_id"],
            "effect_rows": allow["evidence"]["snapshots"][-1]["tables"]["effects"]["row_count"],
        },
        "committed_sql_change_counts": counts,
        "controls": controls,
        "barrier_controls": barriers,
        "phase_binding_controls": phase_controls,
        "gap_admission_controls": gap_controls,
        "r1_6m_phase_v2_controls": r1_6m_phase_controls,
        "r1_6m_review_binding_controls": review_binding_controls,
        "r1_6m_start_authorization_controls": start_authorization_controls,
        "worker_start_requests": 0,
        "helper_starts": 0,
        "wsl_launches": 0,
        "s2_attempts": 0,
        "matrix_episodes": 0,
        "matrix_checkpoints": 0,
        "matrix_effects": None,
        "matrix_promotions": None,
    }
    write_json(output / "OBSERVATION_PLAN.json", positive["plan"])
    write_json(output / "OBSERVATION_READINESS_REPORT.json", {
        "task_id": TASK_ID,
        "status": "PASS" if all(row["status"] == "PASS" for row in barriers) else "FAIL",
        "actual_positive_receipt": positive["readiness"],
        "pre_execution_order": [
            "DATABASE_AND_TABLES_CREATED", "CAPTURE_HOOKS_INSTALLED", "INDEPENDENT_BASELINE_READBACK",
            "SCOPE_CLOCK_CONFIGURATION_BOUND", "OBSERVATION_READY", "FIRST_START_CALLBACK_AUTHORIZED",
        ],
        "callback_processes_started": 0,
        "controls": barriers,
    })
    write_json(output / "CALIBRATION_RESULTS.json", results)
    write_json(output / "PHASE_BINDING_CHECKS.json", {
        "task_id": TASK_ID,
        "historical_implementation_task_id": K_IMPLEMENTATION_TASK_ID,
        "status": "PASS" if all(row["status"] == "PASS" for row in phase_controls) else "FAIL",
        "controls": phase_controls,
    })
    write_json(output / "GAP_ADMISSION_CHECKS.json", {
        "task_id": TASK_ID,
        "status": "PASS" if all(row["status"] == "PASS" for row in gap_controls) else "FAIL",
        "controls": gap_controls,
    })
    write_json(output / "PHASE_V2_VALIDATION_CHECKS.json", {
        "task_id": ITERATION_TASK_ID,
        "historical_calibration_task_id": TASK_ID,
        "status": "PASS" if all(row["status"] == "PASS" for row in phase_controls + r1_6m_phase_controls) else "FAIL",
        "positive_one_phase_hold": positive["review"]["verdict"],
        "positive_two_phase_open": open_phase["status"],
        "positive_two_phase_resolved_events": resolved_phase["committed_event_count"],
        "retained_k01_k02_controls": phase_controls,
        "l01_l04_controls": r1_6m_phase_controls,
    })
    write_json(output / "REVIEW_EVIDENCE_BINDING_CHECKS.json", {
        "task_id": ITERATION_TASK_ID,
        "status": "PASS" if all(row["status"] == "PASS" for row in review_binding_controls) else "FAIL",
        "canonical_review_scope": [
            "schema", "task_id", "attempt_id", "reviewed_evidence_hash", "reviewed_plan_hash",
            "verdict", "issues", "phase_results", "phase_inventory", "audit_coverage",
            "committed_audit_event_count", "rolled_back_attempt_count", "pre_execution_barrier",
            "clock_correlation", "claim_boundary",
        ],
        "controls": review_binding_controls,
    })
    write_json(output / "START_AUTHORIZATION_CHECKS.json", {
        "task_id": ITERATION_TASK_ID,
        "status": "PASS" if all(row["status"] == "PASS" for row in gap_controls + start_authorization_controls) else "FAIL",
        "callback_capable_public_paths": ["ProspectiveObservation.invoke_first_start"],
        "retained_gap_controls": gap_controls,
        "l03_controls": start_authorization_controls,
    })
    write_json(output / "NATIVE_DERIVATION_MAP.json", {
        "task_id": TASK_ID,
        "historical_implementation_task_id": K_IMPLEMENTATION_TASK_ID,
        "scope": "POSITIVE_HOLD_LOCAL_CALIBRATION_ONLY",
        "native_material": positive["native_material"],
        "derivations": {
            "observation_window": "OPEN phase begin/end independent read-transaction clock pairs",
            "before_after_hashes": "JCS hashes of separately read effects/promotions row arrays",
            "collector_availability": "trigger/config continuity + audit chain + final readback after synthetic owned-exit callback",
            "event_log": "committed trigger rows in the OPEN phase; empty in this positive case",
            "external_call_count": "committed DML event count for each declared surface under the single trusted-writer scope",
            "queue_retry": "code-derived absence in bounded Broker API; not host/network interception",
            "clock": "local UTC/perf-counter raw pairs; no external UTC accuracy claim",
            "record_created_at": "post-calibration native material creation clock, distinct from observation times",
        },
        "shared_dependencies": ["jcs 0.2.1", "unchanged pinned validator/schema library"],
        "not_derived": ["historical R1.6I interval", "process lifecycle", "current live authority", "matrix effects"],
    })
    return results


def main() -> int:
    parser = argparse.ArgumentParser(description="Offline prospective observation calibration; never starts worker/WSL/S2")
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = run(args.output)
    print(json.dumps({"status": result["status"], "unique_calibration_cases": result["unique_calibration_cases"]}, sort_keys=True))
    return 0 if result["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
