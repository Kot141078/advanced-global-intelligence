from __future__ import annotations

import copy
import hashlib
import importlib.util
import inspect
import json
import sqlite3
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from cgdr_r1_6b.common import canonical_hash
from cgdr_r1_6b.prospective_observation import (
    ObservationError,
    ProspectiveObservation,
    build_observation_plan,
    build_phase_native_material,
    prepare_prospective_observation,
    review_observation_evidence,
)
from cgdr_r1_6b.source import immutable_source


TOOL_PATH = Path(__file__).resolve().parents[1] / "tools" / "run_observation_calibration.py"
SPEC = importlib.util.spec_from_file_location("cgdr_r1_6k_calibration", TOOL_PATH)
assert SPEC is not None and SPEC.loader is not None
CALIBRATION = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(CALIBRATION)


class ProspectiveObservationCalibrationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.temp = tempfile.TemporaryDirectory(prefix="cgdr-r1-6k-tests-")
        cls.root = Path(cls.temp.name) / "calibration"
        cls.result = CALIBRATION.run(cls.root)
        cls.positive = json.loads((cls.root / "cases" / "positive_hold" / "observation" / "OBSERVATION_EVIDENCE.json").read_text(encoding="utf-8"))
        cls.transient = json.loads((cls.root / "cases" / "transient_changes" / "observation" / "OBSERVATION_EVIDENCE.json").read_text(encoding="utf-8"))
        cls.rollback = json.loads((cls.root / "cases" / "rollback" / "observation" / "OBSERVATION_EVIDENCE.json").read_text(encoding="utf-8"))
        cls.allow = json.loads((cls.root / "cases" / "broker_allow" / "observation" / "OBSERVATION_EVIDENCE.json").read_text(encoding="utf-8"))
        cls.phase_checks = json.loads((cls.root / "PHASE_BINDING_CHECKS.json").read_text(encoding="utf-8"))
        cls.gap_checks = json.loads((cls.root / "GAP_ADMISSION_CHECKS.json").read_text(encoding="utf-8"))

    @classmethod
    def tearDownClass(cls) -> None:
        cls.temp.cleanup()

    def _review_mutation(self, source: dict, mutate) -> dict:
        candidate = copy.deepcopy(source)
        mutate(candidate)
        return review_observation_evidence(candidate)

    def _assert_refused(self, candidate: dict, expected_codes: set[str], phase: str = "OPEN_CHECK") -> dict:
        review = review_observation_evidence(candidate)
        codes = {row["code"] for row in review["issues"]}
        self.assertTrue(expected_codes.issubset(codes), (expected_codes, codes))
        self.assertNotIn(review["verdict"], {"PASS_COMPLETE_WITHIN_DECLARED_SURFACES"})
        material = build_phase_native_material(candidate, review, phase)
        self.assertTrue(material["status"].startswith("REFUSED"), material)
        return review

    def test_01_pre_execution_barrier_order_is_real(self):
        kinds = [row["kind"] for row in self.positive["events"]]
        required = [
            "DATABASE_AND_TABLES_CREATED", "CAPTURE_HOOKS_INSTALLED", "INDEPENDENT_BASELINE_READBACK",
            "SCOPE_CLOCK_CONFIGURATION_BOUND", "OBSERVATION_READY", "FIRST_START_CALLBACK_AUTHORIZED",
        ]
        self.assertEqual(required, [name for name in kinds if name in required])

    def test_02_callback_is_not_called_without_baseline(self):
        receipt = json.loads((self.root / "cases" / "positive_hold" / "READINESS_RECEIPT.json").read_text(encoding="utf-8"))
        receipt["baseline_snapshot_id"] = None
        with self.assertRaisesRegex(ObservationError, "PRE_EXECUTION_BASELINE_MISSING"):
            ProspectiveObservation.validate_readiness_receipt(receipt)

    def test_03_callback_is_not_called_on_logger_error(self):
        receipt = json.loads((self.root / "cases" / "positive_hold" / "READINESS_RECEIPT.json").read_text(encoding="utf-8"))
        receipt["status"] = "NOT_READY"
        receipt["gaps"] = [{"code": "LOGGER_ERROR"}]
        with self.assertRaisesRegex(ObservationError, "PRE_EXECUTION_OBSERVATION_NOT_READY"):
            ProspectiveObservation.validate_readiness_receipt(receipt)

    def test_04_positive_hold_has_two_independent_empty_snapshots(self):
        review = review_observation_evidence(self.positive)
        phase = review["phase_results"]["S2_OPEN_CHECK"]
        self.assertEqual("COMPLETE_NO_COMMITTED_CHANGE", phase["status"])
        self.assertEqual(0, phase["committed_event_count"])
        self.assertEqual("SEPARATE_SQLITE_MODE_RO_READ_TRANSACTION", self.positive["phases"]["S2_OPEN_CHECK"]["begin_snapshot"]["reader"])

    def test_05_positive_hold_native_four_layers_pass(self):
        native = json.loads((self.root / "cases" / "positive_hold" / "native" / "validation.json").read_text(encoding="utf-8"))
        self.assertTrue(native["accepted"], native["rows"])
        self.assertEqual({"shape": "PASS", "record_semantics": "PASS", "registered_evidence": "PASS", "bundle_links": "PASS"}, native["layer_status"])

    def test_06_insert_update_delete_transients_are_detected_when_final_table_empty(self):
        review = review_observation_evidence(self.transient)
        phase = review["phase_results"]["RESOLVED_CHECK"]
        self.assertEqual("EFFECT_DETECTED", phase["status"])
        self.assertEqual(9, phase["committed_event_count"])
        final = self.transient["snapshots"][-1]
        self.assertEqual(0, final["tables"]["effects"]["row_count"])
        self.assertEqual(0, final["tables"]["promotions"]["row_count"])

    def test_07_update_and_promotion_are_not_lost(self):
        rows = self.transient["snapshots"][-1]["audit_rows"]
        kinds = {(row["surface_id"], row["dml_kind"]) for row in rows}
        self.assertTrue({("effects", "UPDATE"), ("promotions", "INSERT"), ("promotions", "UPDATE"), ("promotions", "DELETE")}.issubset(kinds))
        effect_counts = {
            kind: sum(1 for row in rows if row["surface_id"] == "effects" and row["dml_kind"] == kind)
            for kind in ("INSERT", "UPDATE", "DELETE")
        }
        self.assertEqual({"INSERT": 2, "UPDATE": 2, "DELETE": 2}, effect_counts)

    def test_08_rollback_is_retained_as_attempt_not_committed_change(self):
        review = review_observation_evidence(self.rollback)
        self.assertEqual(1, review["rolled_back_attempt_count"])
        self.assertEqual(0, review["committed_audit_event_count"])
        self.assertEqual("PASS_COMPLETE_WITHIN_DECLARED_SURFACES", review["verdict"])

    def test_09_existing_broker_positive_commit_is_observed_not_blanket_denied(self):
        review = review_observation_evidence(self.allow)
        result = json.loads((self.root / "cases" / "broker_allow" / "BROKER_ALLOW_RESULT.json").read_text(encoding="utf-8"))
        expected = self.allow["plan"]["expected_operation_intent"]["scope"]["operation_id"]
        self.assertEqual("BOUND", result["broker_result"]["result"])
        self.assertEqual("OBSERVED_COMMITTED_CHANGE", review["verdict"])
        self.assertEqual(expected, self.allow["snapshots"][-1]["tables"]["effects"]["rows"][0]["operation_id"])

    def test_10_removed_committed_event_is_incomplete(self):
        def mutate(e):
            e["snapshots"][-1]["audit_rows"].pop(2)
        review = self._review_mutation(self.transient, mutate)
        self.assertIn("COMMITTED_AUDIT_SEQUENCE_GAP", {row["code"] for row in review["issues"]})

    def test_11_missing_end_marker_is_incomplete(self):
        def mutate(e):
            e["events"] = [row for row in e["events"] if row["kind"] != "OBSERVATION_END"]
        review = self._review_mutation(self.positive, mutate)
        self.assertNotEqual("PASS_COMPLETE_WITHIN_DECLARED_SURFACES", review["verdict"])

    def test_12_configuration_change_is_incomplete(self):
        review = self._review_mutation(self.positive, lambda e: e["finalization"]["final_configuration"].__setitem__("configuration_hash", "f" * 64))
        self.assertIn("INSTRUMENT_CONFIGURATION_NOT_STABLE", {row["code"] for row in review["issues"]})

    def test_13_target_database_substitution_fails(self):
        review = self._review_mutation(self.positive, lambda e: e.__setitem__("database", "C:/foreign.sqlite3"))
        self.assertEqual("FAIL", review["verdict"])
        self.assertIn("TARGET_DATABASE_SUBSTITUTED", {row["code"] for row in review["issues"]})

    def test_14_clock_jump_is_incomplete(self):
        def mutate(e):
            e["clock_pairs"][3]["utc_ns"] = str(int(e["clock_pairs"][3]["utc_ns"]) + 10_000_000_000)
        review = self._review_mutation(self.positive, mutate)
        self.assertIn("UTC_MONOTONIC_CORRELATION_JUMP", {row["code"] for row in review["issues"]})

    def test_15_unknown_clock_domain_is_incomplete(self):
        review = self._review_mutation(self.positive, lambda e: e["clock_pairs"][3].__setitem__("monotonic_domain", None))
        self.assertIn("CLOCK_PAIR_INVALID", {row["code"] for row in review["issues"]})

    def test_16_gate_entry_substitution_cannot_expand_snapshot_window(self):
        def mutate(e):
            e["phases"]["S2_OPEN_CHECK"]["window_start_clock"]["monotonic_before_ns"] = "0"
        review = self._review_mutation(self.positive, mutate)
        self.assertIn("S2_OPEN_CHECK_WINDOW_EXCEEDS_CAPTURE", {row["code"] for row in review["issues"]})

    def test_17_open_window_excludes_later_resolved_effect(self):
        review = review_observation_evidence(self.transient)
        self.assertEqual("COMPLETE_NO_COMMITTED_CHANGE", review["phase_results"]["OPEN_CHECK"]["status"])
        self.assertEqual("EFFECT_DETECTED", review["phase_results"]["RESOLVED_CHECK"]["status"])

    def test_18_collector_close_before_owned_exit_is_rejected(self):
        def mutate(e):
            e["owned_exit_observed"] = False
            e["events"] = [row for row in e["events"] if row["kind"] != "SYNTHETIC_OWNED_EXIT_CALLBACK"]
        review = self._review_mutation(self.positive, mutate)
        codes = {row["code"] for row in review["issues"]}
        self.assertIn("OWNED_EXIT_BOUNDARY_MISSING", codes)

    def test_19_strong_native_emission_refuses_effect_phase(self):
        review = review_observation_evidence(self.transient)
        material = build_phase_native_material(self.transient, review, "RESOLVED_CHECK")
        self.assertEqual("REFUSED_EFFECT_OR_GAP", material["status"])

    def test_20_task_attempt_checkpoint_binding_is_exact(self):
        review = self._review_mutation(self.positive, lambda e: e.__setitem__("attempt_id", "foreign-attempt"))
        self.assertIn("TASK_ATTEMPT_CHECKPOINT_BINDING_MISMATCH", {row["code"] for row in review["issues"]})

    def test_21_intent_is_frozen_before_actual_sql(self):
        intent = self.allow["plan"]["expected_operation_intent"]
        actual = self.allow["snapshots"][-1]["tables"]["effects"]["rows"][0]
        self.assertEqual("TRUSTED_OPERATION_CONTEXT_PRE_OBSERVATION", intent["origin"])
        self.assertIsNot(intent, actual)
        self.assertEqual(intent["scope"]["operation_id"], actual["operation_id"])

    def test_22_foreign_actual_operation_fails_independent_intent(self):
        def mutate(e):
            row = e["snapshots"][-1]["audit_rows"][0]
            row["new_row"]["operation_id"] = "foreign-operation"
            e["snapshots"][-1]["audit_chain_hash"] = canonical_hash(e["snapshots"][-1]["audit_rows"])
        review = self._review_mutation(self.allow, mutate)
        self.assertIn("ACTUAL_EFFECT_NOT_BOUND_TO_INDEPENDENT_INTENT", {row["code"] for row in review["issues"]})

    def test_23_unknown_writer_connection_cannot_silently_write_surface(self):
        database = Path(self.positive["database"])
        connection = sqlite3.connect(database)
        try:
            with self.assertRaises(sqlite3.OperationalError):
                connection.execute(
                    "INSERT INTO effects VALUES(?,?,?,?)",
                    ("effect:foreign", "operation:foreign", "FOREIGN", json.dumps({"foreign": True})),
                )
                connection.commit()
        finally:
            connection.rollback()
            connection.close()

    def test_24_create_only_database_collision_is_refused(self):
        with tempfile.TemporaryDirectory(prefix="cgdr-r1-6k-collision-") as root_text:
            root = Path(root_text)
            db = root / "observed.sqlite3"
            db.write_bytes(b"occupied")
            source = immutable_source("COLLISION")
            scope = {
                "task_id": source["trusted_policy"]["task_id"], "action": "synthetic_accept",
                "operation_id": "operation:collision", "cell_id": "COLLISION", "attempt_id": "attempt-collision",
                "checkpoint": "OPEN_CHECK", "instance_id": "instance-collision", "commit_record_id": "commit:collision",
            }
            plan = build_observation_plan(
                task_id="CGDR_SELECTED_PROCESS_PROSPECTIVE_OBSERVATION_R1_6K", cell_id="COLLISION",
                attempt_id="attempt-collision", checkpoint="OPEN_CHECK", database=db, path_boundary_root=root,
                operation_scope=scope, expected_outcome="HOLD_NO_EFFECT",
            )
            with self.assertRaisesRegex(ObservationError, "DATABASE_CREATE_ONLY_COLLISION"):
                prepare_prospective_observation(plan=plan, output=root / "observation")

    def test_25_full_calibration_aggregate_is_truthful(self):
        self.assertEqual("PASS", self.result["status"])
        self.assertEqual(4, self.result["unique_calibration_cases"])
        self.assertEqual(0, self.result["worker_start_requests"])
        self.assertEqual(0, self.result["helper_starts"])
        self.assertEqual(0, self.result["wsl_launches"])
        self.assertIsNone(self.result["matrix_effects"])

    def test_26_future_runner_wires_barrier_before_first_start(self):
        source = (Path(__file__).resolve().parents[1] / "tools" / "run_s2.py").read_text(encoding="utf-8")
        main = source[source.index("def main()") :]
        self.assertLess(main.index("prepare_prospective_observation("), main.index("prospective_observer.invoke_first_start("))
        self.assertIn("broker=prospective_broker", main)
        self.assertIn("observation=prospective_observer", main)

    def test_27_future_runner_finalizes_after_owned_exit(self):
        source = (Path(__file__).resolve().parents[1] / "tools" / "run_s2.py").read_text(encoding="utf-8")
        main = source[source.index("def main()") :]
        self.assertLess(main.index('step("W1_OS_WAIT_EXIT"'), main.index("prospective_observer.mark_owned_exit("))
        self.assertLess(main.index("prospective_observer.mark_owned_exit("), main.index("prospective_observer.finalize()"))
        self.assertNotIn("_synthetic_native_precheck(", main)

    def test_28_accepted_semantic_and_security_cores_remain_byte_exact(self):
        code = Path(__file__).resolve().parents[1]
        expected = {
            "src/cgdr_r1_6b/broker.py": "ab347368cd518707ab60eaace1a6c5cc2cd352716457ae4607bdb366d755d0ee",
            "src/cgdr_r1_6b/receiver.py": "a7470d2e78414e04a135d6a9399e8a3896459e4c0a1ce84b08d675043dfabf90",
            "src/cgdr_r1_6b/producer.py": "5ea9e10786fcf97f39bb2456d42277abc17b117899fe1e60ffbcbe23f5074590",
            "src/cgdr_r1_6b/state_transfer.py": "636513649dfaeb6c0a50b340a1c75caf4bdc429406565afe2c39dcbd754f0734",
            "src/cgdr_r1_6b/worker.py": "0afdb56b47bf7c086618f38e08cec100dd6b85424b3d150130d1bd06bbd3611f",
            "src/cgdr_r1_6b/supervisor.py": "8701e915ed1490f0b80ed9c947bf92f5fec95277eff0766dac2f6934c1620325",
        }
        actual = {name: hashlib.sha256((code / name).read_bytes()).hexdigest() for name in expected}
        self.assertEqual(expected, actual)

    def test_29_audit_clock_pair_must_resolve_to_full_raw_pair(self):
        def mutate(e):
            row = e["snapshots"][-1]["audit_rows"][0]
            row["event_clock"]["pair_id"] = "clock-pair:foreign"
            e["snapshots"][-1]["audit_chain_hash"] = canonical_hash(e["snapshots"][-1]["audit_rows"])
        review = self._review_mutation(self.transient, mutate)
        self.assertIn("AUDIT_CLOCK_PAIR_UNRESOLVED", {row["code"] for row in review["issues"]})

    def test_30_transaction_receipt_hash_is_verified(self):
        review = self._review_mutation(self.positive, lambda e: e["transactions"][0].__setitem__("receipt_hash", "0" * 64))
        self.assertIn("TRANSACTION_RECEIPT_HASH_MISMATCH", {row["code"] for row in review["issues"]})

    def test_31_snapshot_clock_object_is_not_a_detached_copy(self):
        def mutate(e):
            e["snapshots"][0]["read_transaction"]["begin_clock"]["utc_ns"] = "1"
        review = self._review_mutation(self.positive, mutate)
        self.assertIn("SNAPSHOT_CLOCK_PAIR_UNRESOLVED", {row["code"] for row in review["issues"]})

    def test_32_new_calibration_uses_explicit_phase_inventory_and_new_task_id(self):
        self.assertEqual(
            "CGDR_SELECTED_PROCESS_OBSERVATION_REPAIR_R1_6L",
            self.transient["plan"]["task_id"],
        )
        self.assertEqual(["OPEN_CHECK", "RESOLVED_CHECK"], self.transient["plan"]["phase_inventory"])
        self.assertEqual("CGDR_PHASE_SNAPSHOT_CLOCK_EVENT_AUDIT_V2", self.transient["plan"]["phase_binding_schema"])

    def test_33_k01_rebound_phase_clocks_are_rejected_by_subject_reason(self):
        def mutate(e):
            e["phases"]["OPEN_CHECK"]["window_start_clock"] = copy.deepcopy(e["phases"]["RESOLVED_CHECK"]["window_start_clock"])
            e["phases"]["OPEN_CHECK"]["window_end_clock"] = copy.deepcopy(e["phases"]["RESOLVED_CHECK"]["window_end_clock"])
        candidate = copy.deepcopy(self.transient)
        mutate(candidate)
        review = review_observation_evidence(candidate)
        codes = {row["code"] for row in review["issues"]}
        self.assertEqual("FAIL", review["verdict"])
        self.assertTrue({"PHASE_WINDOW_START_SNAPSHOT_CLOCK_MISMATCH", "PHASE_WINDOW_END_SNAPSHOT_CLOCK_MISMATCH"}.issubset(codes))
        self.assertEqual("BINDING_INVALID", review["phase_results"]["OPEN_CHECK"]["status"])
        material = build_phase_native_material(candidate, review, "OPEN_CHECK")
        self.assertEqual("REFUSED_INCOMPLETE", material["status"])
        self.assertEqual("PHASE_BINDING_NOT_VERIFIED", material["reason"])

    def test_34_k01_reverse_snapshot_refs_are_rejected(self):
        def mutate(e):
            phase = e["phases"]["OPEN_CHECK"]
            other = e["phases"]["RESOLVED_CHECK"]
            phase["begin_snapshot_id"] = other["begin_snapshot_id"]
            phase["end_snapshot_id"] = other["end_snapshot_id"]
        review = self._review_mutation(self.transient, mutate)
        codes = {row["code"] for row in review["issues"]}
        self.assertIn("PHASE_BEGIN_EVENT_SNAPSHOT_REF_MISMATCH", codes)
        self.assertIn("PHASE_END_EVENT_SNAPSHOT_REF_MISMATCH", codes)

    def test_35_k01_phase_event_binding_is_checked_after_valid_rehash(self):
        candidate = copy.deepcopy(self.transient)
        event = next(row for row in candidate["events"] if row["kind"] == "PHASE_END" and row["phase"] == "OPEN_CHECK")
        event["snapshot_id"] = candidate["phases"]["RESOLVED_CHECK"]["end_snapshot_id"]
        CALIBRATION._rehash_events(candidate)
        review = review_observation_evidence(candidate)
        codes = {row["code"] for row in review["issues"]}
        self.assertNotIn("EVENT_JOURNAL_CHAIN_GAP", codes)
        self.assertIn("PHASE_JOURNAL_EVENT_MALFORMED", codes)
        self.assertIn("PHASE_END_EVENT_BINDING_MISMATCH", codes)

    def test_36_k02_missing_resolved_descriptor_exposes_uncovered_audit(self):
        candidate = copy.deepcopy(self.transient)
        del candidate["phases"]["RESOLVED_CHECK"]
        review = review_observation_evidence(candidate)
        codes = {row["code"] for row in review["issues"]}
        self.assertEqual("INCONCLUSIVE", review["verdict"])
        self.assertIn("PHASE_DESCRIPTOR_MISSING_FROM_FROZEN_INVENTORY", codes)
        self.assertIn("PHASE_DESCRIPTOR_MISSING_FOR_JOURNAL_EVENTS", codes)
        self.assertIn("COMMITTED_AUDIT_EVENTS_OUTSIDE_DESCRIBED_PHASES", codes)
        self.assertEqual("COMPLETE_NO_COMMITTED_CHANGE", review["phase_results"]["OPEN_CHECK"]["status"])
        self.assertEqual(list(range(1, 10)), review["audit_coverage"]["uncovered_audit_sequences"])

    def test_37_k02_empty_descriptors_cannot_pass_with_phase_events(self):
        review = self._review_mutation(self.transient, lambda e: e.__setitem__("phases", {}))
        self.assertNotEqual("PASS_COMPLETE_WITHIN_DECLARED_SURFACES", review["verdict"])
        self.assertIn("PHASE_DESCRIPTOR_MISSING_FOR_JOURNAL_EVENTS", {row["code"] for row in review["issues"]})

    def test_38_k02_duplicate_phase_event_is_rejected_without_chain_noise(self):
        candidate = copy.deepcopy(self.transient)
        index = next(i for i, row in enumerate(candidate["events"]) if row["kind"] == "PHASE_BEGIN" and row["phase"] == "RESOLVED_CHECK")
        candidate["events"].insert(index + 1, copy.deepcopy(candidate["events"][index]))
        CALIBRATION._rehash_events(candidate)
        review = review_observation_evidence(candidate)
        codes = {row["code"] for row in review["issues"]}
        self.assertNotIn("EVENT_JOURNAL_CHAIN_GAP", codes)
        self.assertIn("PHASE_EVENT_PAIR_CARDINALITY_INVALID", codes)

    def test_39_valid_two_phase_capture_has_complete_audit_coverage(self):
        review = review_observation_evidence(self.transient)
        self.assertEqual([], review["issues"])
        self.assertEqual(9, review["audit_coverage"]["covered_committed_events"])
        self.assertEqual([], review["audit_coverage"]["uncovered_audit_sequences"])
        self.assertEqual("PASS", review["phase_results"]["OPEN_CHECK"]["binding_status"])
        self.assertEqual("PASS", review["phase_results"]["RESOLVED_CHECK"]["binding_status"])

    def test_40_k03_known_gap_blocks_next_writer_before_insert(self):
        row = next(item for item in self.gap_checks["controls"] if item["control_id"] == "K03_READY_GAP_BLOCKS_NEXT_WRITER")
        self.assertEqual("PASS", row["status"])
        self.assertEqual("KNOWN_CAPTURE_GAP_ADMISSION_BLOCKED", row["actual_reason"])
        self.assertEqual(0, row["effect_rows_after_refusal"])

    def test_41_k03_known_gap_blocks_borrowed_broker_gate(self):
        row = next(item for item in self.gap_checks["controls"] if item["control_id"] == "K03_GAP_BLOCKS_BORROWED_BROKER_GATE")
        self.assertEqual("PASS", row["status"])
        self.assertEqual(0, row["protected_bind_callback_count"])

    def test_42_k03_stale_ready_receipt_does_not_restart_admission(self):
        row = next(item for item in self.gap_checks["controls"] if item["control_id"] == "K03_STALE_READY_CANNOT_BYPASS_GAP_AT_START_SEAM")
        self.assertEqual("PASS", row["status"])
        self.assertEqual(0, row["callback_count"])

    def test_43_k03_diagnostic_rollback_and_finalize_remain_available(self):
        row = next(item for item in self.gap_checks["controls"] if item["control_id"] == "K03_GAP_RETAINS_DIAGNOSTIC_ROLLBACK_AND_FINALIZATION")
        self.assertEqual("PASS", row["status"])
        self.assertEqual(1, row["rolled_back_attempt_count"])
        self.assertEqual(0, row["committed_audit_event_count"])

    def test_44_k03_gap_persistence_failure_still_latches_admission(self):
        with tempfile.TemporaryDirectory(prefix="cgdr-r1-6l-gap-persist-") as root_text:
            root = Path(root_text)
            source = immutable_source("R1L_GAP_PERSIST")
            plan = CALIBRATION._plan(
                root,
                "gap_persist",
                source,
                "r1-6l-gap-persist",
                "calibration-gap-persist",
            )
            broker, observer = prepare_prospective_observation(plan=plan, output=root / "cases" / "gap_persist" / "observation")
            try:
                with mock.patch("cgdr_r1_6b.prospective_observation._append_jsonl_fsync", side_effect=OSError("finite persistence fault")):
                    with self.assertRaises(ObservationError):
                        observer.note_gap("ORIGINAL_KNOWN_GAP", "must remain latched")
                with self.assertRaisesRegex(ObservationError, "KNOWN_CAPTURE_GAP_ADMISSION_BLOCKED"):
                    observer.begin_writer_transaction("txn-forbidden", operation_id="operation:forbidden", interface="bounded_calibration_dml")
                self.assertEqual(0, broker.db.execute("SELECT count(*) FROM effects").fetchone()[0])
            finally:
                broker.close()

    def test_45_no_gap_hold_and_allow_positive_paths_still_work(self):
        self.assertEqual("PASS_COMPLETE_WITHIN_DECLARED_SURFACES", review_observation_evidence(self.positive)["verdict"])
        self.assertEqual("OBSERVED_COMMITTED_CHANGE", review_observation_evidence(self.allow)["verdict"])

    def test_46_phase_and_gap_control_aggregates_pass(self):
        self.assertEqual("PASS", self.phase_checks["status"])
        self.assertEqual("PASS", self.gap_checks["status"])
        self.assertTrue(all(row["status"] == "PASS" for row in self.phase_checks["controls"] + self.gap_checks["controls"]))

    def test_47_runtime_rejects_overlapping_declared_phases(self):
        with tempfile.TemporaryDirectory(prefix="cgdr-r1-6l-phase-overlap-") as root_text:
            root = Path(root_text)
            source = immutable_source("R1L_PHASE_OVERLAP")
            plan = CALIBRATION._plan(
                root,
                "phase_overlap",
                source,
                "r1-6l-phase-overlap",
                "calibration-phase-overlap",
                phase_inventory=["OPEN_CHECK", "RESOLVED_CHECK"],
            )
            broker, observer = prepare_prospective_observation(plan=plan, output=root / "cases" / "phase_overlap" / "observation")
            try:
                observer.invoke_first_start(lambda: {"process_started": False})
                observer.begin_phase("OPEN_CHECK")
                with self.assertRaisesRegex(ObservationError, "PHASE_OVERLAP_FORBIDDEN"):
                    observer.begin_phase("RESOLVED_CHECK")
            finally:
                broker.close()

    def test_48_l01_exact_b_downgrade_by_omission_is_refused(self):
        candidate = copy.deepcopy(self.transient)
        phase = candidate["phases"]["OPEN_CHECK"]
        for key in (
            "binding_version", "phase_id", "phase_order", "begin_event_ref", "end_event_ref",
            "begin_snapshot_hash", "end_snapshot_hash",
        ):
            phase.pop(key, None)
        for event in candidate["events"]:
            if event.get("kind") in {"PHASE_BEGIN", "PHASE_END"} and event.get("phase") == "OPEN_CHECK":
                event.update(
                    task_id="FOREIGN_TASK",
                    attempt_id="FOREIGN_ATTEMPT",
                    phase_id="phase:foreign",
                    phase_order=99,
                )
        CALIBRATION._rehash_events(candidate)
        review = self._assert_refused(
            candidate,
            {"PHASE_V2_REQUIRED_FIELD_MISSING", "PHASE_JOURNAL_EVENT_MALFORMED"},
        )
        self.assertNotIn("EVENT_JOURNAL_CHAIN_GAP", {row["code"] for row in review["issues"]})

    def test_49_l01_every_required_v2_descriptor_field_is_mandatory(self):
        fields = (
            "name", "phase_id", "phase_order", "binding_version", "status",
            "begin_snapshot_id", "begin_snapshot", "begin_snapshot_hash",
            "end_snapshot_id", "end_snapshot", "end_snapshot_hash",
            "start_audit_seq", "end_audit_seq", "window_start_clock", "window_end_clock",
            "begin_event_ref", "end_event_ref",
        )
        for field in fields:
            with self.subTest(field=field):
                candidate = copy.deepcopy(self.transient)
                candidate["phases"]["OPEN_CHECK"].pop(field)
                self._assert_refused(candidate, {"PHASE_V2_REQUIRED_FIELD_MISSING"})

    def test_50_l01_unknown_wrong_or_malformed_binding_version_is_refused(self):
        for value in (None, "", "LEGACY", "CGDR_PHASE_SNAPSHOT_CLOCK_EVENT_AUDIT_V3", 7):
            with self.subTest(value=value):
                candidate = copy.deepcopy(self.transient)
                candidate["phases"]["OPEN_CHECK"]["binding_version"] = value
                review = review_observation_evidence(candidate)
                codes = {row["code"] for row in review["issues"]}
                self.assertTrue(
                    {"PHASE_V2_REQUIRED_FIELD_MISSING", "PHASE_V2_REQUIRED_FIELD_TYPE_INVALID", "PHASE_BINDING_VERSION_MISMATCH"}
                    & codes,
                    codes,
                )
                self.assertTrue(build_phase_native_material(candidate, review, "OPEN_CHECK")["status"].startswith("REFUSED"))

    def test_51_l01_reversed_snapshot_ids_content_and_hashes_are_refused(self):
        variants = {
            "ids": lambda p, other: p.update(begin_snapshot_id=other["begin_snapshot_id"], end_snapshot_id=other["end_snapshot_id"]),
            "content": lambda p, other: p.update(begin_snapshot=copy.deepcopy(other["begin_snapshot"]), end_snapshot=copy.deepcopy(other["end_snapshot"])),
            "hashes": lambda p, other: p.update(begin_snapshot_hash=other["begin_snapshot_hash"], end_snapshot_hash=other["end_snapshot_hash"]),
        }
        for name, mutate in variants.items():
            with self.subTest(name=name):
                candidate = copy.deepcopy(self.transient)
                mutate(candidate["phases"]["OPEN_CHECK"], candidate["phases"]["RESOLVED_CHECK"])
                review = review_observation_evidence(candidate)
                self.assertEqual("FAIL", review["verdict"])
                self.assertTrue(build_phase_native_material(candidate, review, "OPEN_CHECK")["status"].startswith("REFUSED"))

    def test_52_l01_foreign_event_and_event_ref_bindings_are_refused_after_rehash(self):
        variants = (
            ("task_id", "FOREIGN_TASK", "PHASE_JOURNAL_EVENT_MALFORMED"),
            ("attempt_id", "FOREIGN_ATTEMPT", "PHASE_JOURNAL_EVENT_MALFORMED"),
            ("phase_id", "phase:foreign", "PHASE_BEGIN_EVENT_BINDING_MISMATCH"),
            ("phase_order", 99, "PHASE_BEGIN_EVENT_BINDING_MISMATCH"),
            ("snapshot_audit_seq", 999, "PHASE_JOURNAL_EVENT_MALFORMED"),
            ("window_clock_pair_id", "clock-pair:foreign", "PHASE_JOURNAL_EVENT_MALFORMED"),
        )
        for field, value, expected_code in variants:
            with self.subTest(field=field):
                candidate = copy.deepcopy(self.transient)
                event = next(row for row in candidate["events"] if row.get("kind") == "PHASE_BEGIN" and row.get("phase") == "OPEN_CHECK")
                event[field] = value
                CALIBRATION._rehash_events(candidate)
                self._assert_refused(candidate, {expected_code})
        candidate = copy.deepcopy(self.transient)
        candidate["phases"]["OPEN_CHECK"]["begin_event_ref"] = copy.deepcopy(
            candidate["phases"]["RESOLVED_CHECK"]["begin_event_ref"]
        )
        self._assert_refused(candidate, {"PHASE_BEGIN_EVENT_REF_MISMATCH"})

    def test_53_l02_exact_clean_review_evidence_pair_is_bound_and_positive(self):
        review = review_observation_evidence(self.transient)
        self.assertEqual(canonical_hash(self.transient), review["reviewed_evidence_hash"])
        self.assertEqual(self.transient["plan_hash"], review["reviewed_plan_hash"])
        self.assertEqual("COMPLETE_NO_COMMITTED_CHANGE", build_phase_native_material(self.transient, review, "OPEN_CHECK")["status"])

    def test_54_l02_clean_review_plus_changed_clocks_is_refused(self):
        clean = review_observation_evidence(self.transient)
        candidate = copy.deepcopy(self.transient)
        candidate["phases"]["OPEN_CHECK"]["window_start_clock"] = copy.deepcopy(candidate["phases"]["RESOLVED_CHECK"]["window_start_clock"])
        candidate["phases"]["OPEN_CHECK"]["window_end_clock"] = copy.deepcopy(candidate["phases"]["RESOLVED_CHECK"]["window_end_clock"])
        material = build_phase_native_material(candidate, clean, "OPEN_CHECK")
        self.assertEqual({"status": "REFUSED_INCOMPLETE", "reason": "REVIEW_EVIDENCE_BINDING_MISMATCH"}, material)

    def test_55_l02_same_plan_hash_changed_evidence_is_refused(self):
        clean = review_observation_evidence(self.transient)
        candidate = copy.deepcopy(self.transient)
        candidate["claim_boundary"] += " altered evidence only"
        self.assertEqual(self.transient["plan_hash"], candidate["plan_hash"])
        self.assertEqual("REVIEW_EVIDENCE_BINDING_MISMATCH", build_phase_native_material(candidate, clean, "OPEN_CHECK")["reason"])

    def test_56_l02_hash_fields_only_rewrite_cannot_refresh_stale_review(self):
        stale = review_observation_evidence(self.transient)
        candidate = copy.deepcopy(self.transient)
        candidate["phases"]["OPEN_CHECK"]["window_start_clock"] = copy.deepcopy(candidate["phases"]["RESOLVED_CHECK"]["window_start_clock"])
        candidate["phases"]["OPEN_CHECK"]["window_end_clock"] = copy.deepcopy(candidate["phases"]["RESOLVED_CHECK"]["window_end_clock"])
        attacker = copy.deepcopy(stale)
        attacker["reviewed_evidence_hash"] = canonical_hash(candidate)
        attacker["reviewed_plan_hash"] = candidate["plan_hash"]
        self.assertEqual("REVIEW_EVIDENCE_BINDING_MISMATCH", build_phase_native_material(candidate, attacker, "OPEN_CHECK")["reason"])

    def test_57_l02_review_from_other_evidence_is_refused(self):
        other_review = review_observation_evidence(self.positive)
        material = build_phase_native_material(self.transient, other_review, "OPEN_CHECK")
        self.assertEqual("REVIEW_EVIDENCE_BINDING_MISMATCH", material["reason"])

    def test_58_l02_missing_reviewed_hashes_are_refused(self):
        for field in ("reviewed_evidence_hash", "reviewed_plan_hash"):
            with self.subTest(field=field):
                review = review_observation_evidence(self.transient)
                review.pop(field)
                self.assertEqual(
                    "REVIEW_EVIDENCE_BINDING_MISMATCH",
                    build_phase_native_material(self.transient, review, "OPEN_CHECK")["reason"],
                )

    def test_59_l02_json_key_order_does_not_change_binding_decision(self):
        def reverse_keys(value):
            if isinstance(value, dict):
                return {key: reverse_keys(value[key]) for key in reversed(list(value))}
            if isinstance(value, list):
                return [reverse_keys(item) for item in value]
            return value
        candidate = reverse_keys(self.transient)
        review = review_observation_evidence(candidate)
        self.assertEqual(canonical_hash(self.transient), canonical_hash(candidate))
        self.assertEqual("COMPLETE_NO_COMMITTED_CHANGE", build_phase_native_material(candidate, review, "OPEN_CHECK")["status"])

    def test_60_l02_fresh_calibration_and_future_caller_pattern_remain_bound(self):
        self.assertEqual("PASS", self.result["status"])
        source = (Path(__file__).resolve().parents[1] / "tools" / "run_s2.py").read_text(encoding="utf-8")
        review_index = source.index("prospective_observation_review = review_observation_evidence(prospective_observation_evidence)")
        material_index = source.index("native_material = build_phase_native_material(", review_index)
        self.assertLess(review_index, material_index)

    def test_61_l04_exact_b_empty_phase_events_are_not_filtered(self):
        candidate = copy.deepcopy(self.transient)
        insert_at = next(i for i, row in enumerate(candidate["events"]) if row.get("kind") in {"SYNTHETIC_OWNED_EXIT_CALLBACK", "OWNED_EXIT_OBSERVED"})
        template_clock_id = candidate["events"][insert_at - 1]["clock_pair_id"]
        candidate["events"][insert_at:insert_at] = [
            {"sequence": 0, "kind": "PHASE_BEGIN", "clock_pair_id": template_clock_id, "previous_event_hash": None, "phase": "", "phase_id": "phase:undeclared", "phase_order": 77, "snapshot_id": "snapshot:missing"},
            {"sequence": 0, "kind": "PHASE_END", "clock_pair_id": template_clock_id, "previous_event_hash": None, "phase": "", "phase_id": "phase:undeclared", "phase_order": 77, "snapshot_id": "snapshot:missing"},
        ]
        CALIBRATION._rehash_events(candidate)
        review = self._assert_refused(candidate, {"PHASE_JOURNAL_EVENT_MALFORMED"})
        self.assertNotIn("EVENT_JOURNAL_CHAIN_GAP", {row["code"] for row in review["issues"]})

    def test_62_l04_missing_phase_key_is_not_filtered(self):
        candidate = copy.deepcopy(self.transient)
        event = next(row for row in candidate["events"] if row.get("kind") == "PHASE_BEGIN" and row.get("phase") == "OPEN_CHECK")
        event.pop("phase")
        CALIBRATION._rehash_events(candidate)
        self._assert_refused(candidate, {"PHASE_JOURNAL_EVENT_MALFORMED"})

    def test_63_l04_null_nonstring_empty_and_whitespace_phase_are_malformed(self):
        for value in (None, 7, "", "   "):
            with self.subTest(value=value):
                candidate = copy.deepcopy(self.transient)
                event = next(row for row in candidate["events"] if row.get("kind") == "PHASE_BEGIN" and row.get("phase") == "OPEN_CHECK")
                event["phase"] = value
                CALIBRATION._rehash_events(candidate)
                self._assert_refused(candidate, {"PHASE_JOURNAL_EVENT_MALFORMED"})

    def test_64_l04_required_phase_event_fields_are_validated_before_inventory(self):
        fields = (
            "task_id", "attempt_id", "phase_id", "phase_order", "snapshot_id", "snapshot_hash",
            "snapshot_audit_seq", "snapshot_read_begin_clock_id", "snapshot_read_end_clock_id",
            "window_clock_pair_id", "clock_pair_id",
        )
        for field in fields:
            with self.subTest(field=field):
                candidate = copy.deepcopy(self.transient)
                event = next(row for row in candidate["events"] if row.get("kind") == "PHASE_BEGIN" and row.get("phase") == "OPEN_CHECK")
                event.pop(field)
                CALIBRATION._rehash_events(candidate)
                self._assert_refused(candidate, {"PHASE_JOURNAL_EVENT_MALFORMED"})

    def test_65_l04_unknown_well_formed_phase_is_outside_inventory(self):
        candidate = copy.deepcopy(self.transient)
        originals = [row for row in candidate["events"] if row.get("kind") in {"PHASE_BEGIN", "PHASE_END"} and row.get("phase") == "OPEN_CHECK"]
        extras = copy.deepcopy(originals)
        for event in extras:
            event["phase"] = "UNKNOWN_CHECK"
            event["phase_id"] = f"phase:{candidate['attempt_id']}:3:UNKNOWN_CHECK"
            event["phase_order"] = 3
        insert_at = next(i for i, row in enumerate(candidate["events"]) if row.get("kind") == "SYNTHETIC_OWNED_EXIT_CALLBACK")
        candidate["events"][insert_at:insert_at] = extras
        CALIBRATION._rehash_events(candidate)
        self._assert_refused(candidate, {"PHASE_JOURNAL_EVENT_OUTSIDE_FROZEN_INVENTORY"})

    def test_66_l04_one_malformed_event_with_two_normal_phases_fails_whole_evidence(self):
        candidate = copy.deepcopy(self.transient)
        event = copy.deepcopy(next(row for row in candidate["events"] if row.get("kind") == "PHASE_BEGIN" and row.get("phase") == "RESOLVED_CHECK"))
        event["phase"] = "   "
        insert_at = next(i for i, row in enumerate(candidate["events"]) if row.get("kind") == "SYNTHETIC_OWNED_EXIT_CALLBACK")
        candidate["events"].insert(insert_at, event)
        CALIBRATION._rehash_events(candidate)
        review = self._assert_refused(candidate, {"PHASE_JOURNAL_EVENT_MALFORMED"})
        self.assertEqual(0, review["phase_results"]["OPEN_CHECK"]["committed_event_count"])
        self.assertEqual(9, review["phase_results"]["RESOLVED_CHECK"]["committed_event_count"])

    def test_67_l03_state_free_callback_api_is_removed(self):
        self.assertFalse(hasattr(ProspectiveObservation, "authorize_from_receipt"))
        signature = inspect.signature(ProspectiveObservation.validate_readiness_receipt)
        self.assertNotIn("callback", signature.parameters)

    def test_68_l03_exact_b_ready_gap_former_api_attempt_has_zero_callbacks(self):
        with tempfile.TemporaryDirectory(prefix="cgdr-r1-6m-former-api-") as root_text:
            root = Path(root_text)
            source = immutable_source("R1M_FORMER_API")
            plan = CALIBRATION._plan(root, "former_api", source, "r1-6m-former-api", "instance-former-api")
            broker, observer = prepare_prospective_observation(plan=plan, output=root / "observation")
            try:
                stale = observer.readiness_receipt()
                observer.note_gap("L03_GAP", "sticky live gap")
                callbacks = []
                with self.assertRaises(AttributeError):
                    getattr(ProspectiveObservation, "authorize_from_receipt")(stale, lambda: callbacks.append("CALLED"))
                self.assertEqual([], callbacks)
            finally:
                broker.close()

    def test_69_l03_receipt_from_different_live_observation_is_stale(self):
        with tempfile.TemporaryDirectory(prefix="cgdr-r1-6m-foreign-receipt-") as root_text:
            root = Path(root_text)
            source1 = immutable_source("R1M_OLD_RECEIPT")
            source2 = immutable_source("R1M_NEW_RECEIPT")
            plan1 = CALIBRATION._plan(root / "old", "old", source1, "r1-6m-old", "instance-old")
            plan2 = CALIBRATION._plan(root / "new", "new", source2, "r1-6m-new", "instance-new")
            broker1, observer1 = prepare_prospective_observation(plan=plan1, output=root / "old" / "observation")
            broker2, observer2 = prepare_prospective_observation(plan=plan2, output=root / "new" / "observation")
            callbacks = []
            try:
                with self.assertRaisesRegex(ObservationError, "STALE_OBSERVATION_READINESS_RECEIPT"):
                    observer2.invoke_first_start(lambda: callbacks.append("CALLED"), readiness_receipt=observer1.readiness_receipt())
                self.assertEqual([], callbacks)
                self.assertFalse(observer2._first_start_consumed)
            finally:
                broker1.close()
                broker2.close()

    def test_70_l03_current_receipt_invokes_once_and_replay_is_rejected(self):
        with tempfile.TemporaryDirectory(prefix="cgdr-r1-6m-replay-") as root_text:
            root = Path(root_text)
            source = immutable_source("R1M_REPLAY")
            plan = CALIBRATION._plan(root, "replay", source, "r1-6m-replay", "instance-replay")
            broker, observer = prepare_prospective_observation(plan=plan, output=root / "observation")
            callbacks = []
            try:
                receipt = observer.readiness_receipt()
                observer.invoke_first_start(lambda: callbacks.append("CALLED"), readiness_receipt=receipt)
                self.assertTrue(observer._first_start_consumed)
                with self.assertRaisesRegex(ObservationError, "FIRST_START_CALLBACK_REPLAYED"):
                    observer.invoke_first_start(lambda: callbacks.append("CALLED_AGAIN"), readiness_receipt=receipt)
                self.assertEqual(["CALLED"], callbacks)
            finally:
                broker.close()

    def test_71_l03_invalid_receipt_fields_reject_before_authorized_event(self):
        with tempfile.TemporaryDirectory(prefix="cgdr-r1-6m-invalid-receipt-") as root_text:
            root = Path(root_text)
            source = immutable_source("R1M_INVALID_RECEIPT")
            plan = CALIBRATION._plan(root, "invalid_receipt", source, "r1-6m-invalid-receipt", "instance-invalid")
            broker, observer = prepare_prospective_observation(plan=plan, output=root / "observation")
            callbacks = []
            variants = {
                "schema": None,
                "status": "NOT_READY",
                "plan_hash": None,
                "configuration_hash": None,
                "baseline_snapshot_id": None,
                "baseline_snapshot_hash": None,
                "ready_event": None,
            }
            try:
                for field, value in variants.items():
                    with self.subTest(field=field):
                        candidate = observer.readiness_receipt()
                        candidate[field] = value
                        before = sum(row.get("kind") == "FIRST_START_CALLBACK_AUTHORIZED" for row in observer._events)
                        with self.assertRaises(ObservationError):
                            observer.invoke_first_start(lambda: callbacks.append("CALLED"), readiness_receipt=candidate)
                        after = sum(row.get("kind") == "FIRST_START_CALLBACK_AUTHORIZED" for row in observer._events)
                        self.assertEqual(before, after)
                self.assertEqual([], callbacks)
                self.assertFalse(observer._first_start_consumed)
            finally:
                broker.close()

    def test_72_l03_introspection_finds_only_live_bound_public_callback_start(self):
        callback_methods = []
        for name, member in inspect.getmembers(ProspectiveObservation, predicate=inspect.isfunction):
            if name.startswith("_"):
                continue
            if "callback" in inspect.signature(member).parameters:
                callback_methods.append(name)
        self.assertEqual(["invoke_first_start"], callback_methods)
        source = inspect.getsource(ProspectiveObservation)
        self.assertNotIn("authorize_from_receipt", source)

    def test_73_m01_reentrant_first_start_is_rejected_before_second_authorized(self):
        with tempfile.TemporaryDirectory(prefix="cgdr-r1-6n-reentrant-") as root_text:
            root = Path(root_text)
            plan = CALIBRATION._plan(root, "m01_reentrant", immutable_source("R1N_M01_REENTRANT"), "r1-6n-m01-reentrant", "instance-m01-reentrant")
            broker, observer = prepare_prospective_observation(plan=plan, output=root / "observation")
            outer_calls = []
            nested_calls = []
            nested_reasons = []
            try:
                def outer():
                    outer_calls.append("outer")
                    try:
                        observer.invoke_first_start(lambda: nested_calls.append("nested"))
                    except ObservationError as exc:
                        nested_reasons.append(str(exc))
                    outer_calls.append("outer_return")
                    return "OUTER_OK"

                self.assertEqual("OUTER_OK", observer.invoke_first_start(outer))
                kinds = [row.get("kind") for row in observer._events]
                self.assertEqual(["outer", "outer_return"], outer_calls)
                self.assertEqual([], nested_calls)
                self.assertTrue(any("FIRST_START_CALLBACK_REPLAYED" in reason for reason in nested_reasons))
                self.assertEqual(1, kinds.count("FIRST_START_CALLBACK_AUTHORIZED"))
                self.assertEqual(1, kinds.count("FIRST_START_CALLBACK_RETURNED"))
                self.assertTrue(observer._first_start_consumed)
                self.assertTrue(observer._first_start_callback)
            finally:
                broker.close()

    def test_74_m01_failed_callback_consumes_start_and_blocks_retry(self):
        with tempfile.TemporaryDirectory(prefix="cgdr-r1-6n-failure-retry-") as root_text:
            root = Path(root_text)
            plan = CALIBRATION._plan(root, "m01_failure_retry", immutable_source("R1N_M01_FAILURE_RETRY"), "r1-6n-m01-failure-retry", "instance-m01-failure-retry")
            broker, observer = prepare_prospective_observation(plan=plan, output=root / "observation")
            marker = []
            retry_calls = []
            try:
                def failing():
                    marker.append("local-side-effect")
                    raise RuntimeError("after-side-effect")

                with self.assertRaisesRegex(RuntimeError, "after-side-effect"):
                    observer.invoke_first_start(failing)
                with self.assertRaisesRegex(ObservationError, "KNOWN_CAPTURE_GAP_ADMISSION_BLOCKED"):
                    observer.invoke_first_start(lambda: retry_calls.append("retry"))
                for stage in ("GATE", "WRITER_TRANSACTION"):
                    with self.subTest(stage=stage):
                        with self.assertRaisesRegex(ObservationError, "KNOWN_CAPTURE_GAP_ADMISSION_BLOCKED"):
                            observer.require_admission(stage)
                kinds = [row.get("kind") for row in observer._events]
                self.assertEqual(["local-side-effect"], marker)
                self.assertEqual([], retry_calls)
                self.assertEqual(1, kinds.count("FIRST_START_CALLBACK_AUTHORIZED"))
                self.assertEqual(1, kinds.count("FIRST_START_CALLBACK_FAILED"))
                self.assertEqual(0, kinds.count("FIRST_START_CALLBACK_RETURNED"))
                self.assertTrue(observer._first_start_consumed)
                self.assertFalse(observer._first_start_callback)
                self.assertEqual("FIRST_START_CALLBACK_OUTCOME_UNCERTAIN", observer._admission_blocked_reason["code"])
            finally:
                broker.close()

    def test_75_m01_failed_callback_does_not_satisfy_phase_barrier(self):
        with tempfile.TemporaryDirectory(prefix="cgdr-r1-6n-failed-phase-") as root_text:
            root = Path(root_text)
            plan = CALIBRATION._plan(root, "m01_failed_phase", immutable_source("R1N_M01_FAILED_PHASE"), "r1-6n-m01-failed-phase", "instance-m01-failed-phase")
            broker, observer = prepare_prospective_observation(plan=plan, output=root / "observation")
            try:
                with self.assertRaises(RuntimeError):
                    observer.invoke_first_start(lambda: (_ for _ in ()).throw(RuntimeError("failed-start")))
                with self.assertRaisesRegex(ObservationError, "KNOWN_CAPTURE_GAP_ADMISSION_BLOCKED"):
                    observer.begin_phase("S2_OPEN_CHECK")
                self.assertFalse(observer._first_start_callback)
                self.assertEqual({}, observer._phases)
                self.assertEqual(0, broker.db.execute("SELECT count(*) FROM effects").fetchone()[0])
                self.assertEqual(0, broker.db.execute("SELECT count(*) FROM promotions").fetchone()[0])
            finally:
                broker.close()

    def test_76_m01_failure_retains_diagnostic_finalization_without_clean_verdict(self):
        with tempfile.TemporaryDirectory(prefix="cgdr-r1-6n-failure-finalize-") as root_text:
            root = Path(root_text)
            plan = CALIBRATION._plan(root, "m01_failure_finalize", immutable_source("R1N_M01_FAILURE_FINALIZE"), "r1-6n-m01-failure-finalize", "instance-m01-failure-finalize")
            broker, observer = prepare_prospective_observation(plan=plan, output=root / "observation")
            transaction_id = "txn-m01-failure-diagnostic"
            try:
                def failing_with_open_transaction():
                    observer.begin_writer_transaction(transaction_id, operation_id="operation:m01-diagnostic", interface="bounded_calibration_dml")
                    broker.db.execute("BEGIN IMMEDIATE")
                    broker.db.execute("INSERT INTO effects VALUES(?,?,?,?)", ("effect:m01", "operation:m01-diagnostic", "R1N_M01", "{}"))
                    raise RuntimeError("ambiguous-start-with-open-toy-transaction")

                with self.assertRaisesRegex(RuntimeError, "ambiguous-start"):
                    observer.invoke_first_start(failing_with_open_transaction)
                broker.db.rollback()
                observer.finish_writer_transaction(transaction_id, "ROLLED_BACK", reason="M01_DIAGNOSTIC_CLEANUP")
                self.assertEqual(0, broker.db.execute("SELECT count(*) FROM effects").fetchone()[0])
                observer.mark_owned_exit(synthetic=True, binding={"kind": "M01_FAILURE_FAKE_EXIT", "process_started": False})
                evidence = observer.finalize()
                review = review_observation_evidence(evidence)
                material = build_phase_native_material(evidence, review, "S2_OPEN_CHECK")
                self.assertEqual(1, review["rolled_back_attempt_count"])
                self.assertTrue(any(row["code"] == "FIRST_START_CALLBACK_OUTCOME_UNCERTAIN" for row in evidence["gaps"]))
                self.assertNotEqual("PASS_COMPLETE_WITHIN_DECLARED_SURFACES", review["verdict"])
                self.assertTrue(material["status"].startswith("REFUSED"))
                self.assertEqual("INCOMPLETE", evidence["finalization"]["status"])
            finally:
                broker.close()


if __name__ == "__main__":
    unittest.main()
