from __future__ import annotations

import copy
import json
import os
import tempfile
import unittest
from pathlib import Path

from cgdr_r1_6b import run_batch
from cgdr_r1_6b.broker import Broker


class SelectedProcessMatrixR16XTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        matrix_path = os.environ.get("CGDR_X_MATRIX")
        if not matrix_path:
            raise RuntimeError("CGDR_X_MATRIX must bind the exact TRANSITION_TEST_MATRIX.json")
        cls.matrix_path = Path(matrix_path).resolve()
        cls.matrix = json.loads(cls.matrix_path.read_text(encoding="utf-8"))

    def _valid(self, *, cell_id: str = "T0", checkpoint: str = "RESOLVED_CHECK") -> dict:
        episode = run_batch.MATRIX_CELL_ORDER.index(cell_id) + 1
        run_id = "x-offline-control-001"
        attempt_id = run_batch.deterministic_id(run_id, episode, cell_id, "matrix-attempt")
        mode = run_batch.lifecycle_mode(cell_id)
        steps = list(run_batch.lifecycle_contract(cell_id)["required_steps"])
        w0, w1 = "instance-w0", ("instance-w1" if mode == "REPLACE_PROCESS" else None)
        active = w1 or w0
        positive = (cell_id, checkpoint) in run_batch.POSITIVE_EFFECT_COORDINATES
        return {
            "matrix_run_id": run_id,
            "cell_id": cell_id,
            "attempt_id": attempt_id,
            "checkpoint": checkpoint,
            "lifecycle_mode": mode,
            "lifecycle_steps": steps,
            "w0_instance_id": w0,
            "w1_instance_id": w1,
            "active_instance_id": active,
            "w0_cleanup": "PROVEN",
            "state_carriage": "PASS",
            "current_epoch": "E1",
            "e0_status": "HISTORICAL_FENCED" if mode == "REPLACE_PROCESS" else "NOT_APPLICABLE",
            "readiness": "READY",
            "implementation_freeze": "BEFORE_FIRST_WORKER_START",
            "capture_gaps": [],
            "writer_admission": "ADMITTED",
            "expected_effect_delta": 1 if positive else 0,
            "actual_effect_delta": 1 if positive else 0,
            "expected_promotion_delta": 0,
            "actual_promotion_delta": 0,
            "approval_roots": ["root:alpha", "root:beta"] if positive else [],
            "required_approval_roots": 2 if positive else 0,
            "q_state": "COLLAPSED_SCOPED" if positive else "OPEN",
            "qcr_valid": positive,
            "expected_obligations": ["liability:one"],
            "carried_obligations": ["liability:one"],
            "evidence_binding": {
                "matrix_run_id": run_id,
                "cell_id": cell_id,
                "attempt_id": attempt_id,
                "checkpoint": checkpoint,
            },
            "attempt_coverage_complete": True,
            "registry_coverage_complete": True,
            "surface_inventory": [
                {"surface_id": "effects", "coordinate": "synthetic-sink/effects", "hash_domain": "JCS_ROWS"},
                {"surface_id": "promotions", "coordinate": "synthetic-sink/promotions", "hash_domain": "JCS_ROWS"},
            ],
        }

    def _codes(self, value: dict) -> set[str]:
        return {row["code"] for row in run_batch.review_alignment_evidence(value)["issues"]}

    def test_x01_exact_matrix_identity_order_is_18_21(self) -> None:
        result = run_batch.validate_matrix_contract(self.matrix)
        self.assertEqual(result["status"], "PASS")
        self.assertEqual(result["cell_order"], list(run_batch.MATRIX_CELL_ORDER))
        self.assertEqual((result["episode_count"], result["checkpoint_count"]), (18, 21))

    def test_x02_explicit_matrix_run_id_required_and_legacy_forbidden(self) -> None:
        for invalid in ("", "short", "legacy-unauthorized-matrix", "UPPERCASE-NOT-BOUND"):
            with self.subTest(invalid=invalid), self.assertRaises(ValueError):
                run_batch._require_matrix_run_id(invalid)

    def test_x03_deterministic_ids_bind_run_episode_checkpoint(self) -> None:
        first = run_batch.deterministic_id("run-bound-001", 1, "N0", "operation", 2)
        self.assertEqual(first, run_batch.deterministic_id("run-bound-001", 1, "N0", "operation", 2))
        self.assertNotEqual(first, run_batch.deterministic_id("run-bound-002", 1, "N0", "operation", 2))
        self.assertIn(":01:N0:c02", first)

    def test_x04_each_episode_has_distinct_output_db_and_evidence_namespace(self) -> None:
        root = Path("X:/bounded-output")
        values = [run_batch.episode_namespace(root, "run-bound-001", i, cell) for i, cell in enumerate(run_batch.MATRIX_CELL_ORDER, 1)]
        for key in ("root", "database", "observation_output", "evidence_namespace", "attempt_id"):
            self.assertEqual(len({str(row[key]) for row in values}), 18)

    def test_x05_no_cross_episode_broker_rows_in_before_state(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            first = Broker(Path(directory) / "one.sqlite3")
            second = Broker(Path(directory) / "two.sqlite3")
            try:
                first.db.execute("INSERT INTO operations VALUES(?,?,?)", ("op-one", "a" * 64, "HELD"))
                self.assertEqual(len(first.snapshot()["operations"]), 1)
                self.assertEqual(second.snapshot()["operations"], [])
                self.assertEqual(second.counts(), {"effects": 0, "promotions": 0})
            finally:
                first.close()
                second.close()

    def test_x06_n0_lifecycle_is_no_replacement(self) -> None:
        contract = run_batch.lifecycle_contract("N0")
        self.assertEqual(contract["mode"], "NO_REPLACEMENT")
        self.assertNotIn("W1_START", contract["required_steps"])
        self.assertEqual(run_batch.review_alignment_evidence(self._valid(cell_id="N0", checkpoint="OPEN_CHECK"))["verdict"], "PASS_ALIGNED_EPISODE")

    def test_x07_n1_requires_sham_wait_release_continue_same_instance(self) -> None:
        value = self._valid(cell_id="N1", checkpoint="OPEN_CHECK")
        self.assertEqual(run_batch.review_alignment_evidence(value)["verdict"], "PASS_ALIGNED_EPISODE")
        self.assertLess(value["lifecycle_steps"].index("SHAM_WAIT"), value["lifecycle_steps"].index("RELEASE"))
        self.assertLess(value["lifecycle_steps"].index("RELEASE"), value["lifecycle_steps"].index("CONTINUE"))
        self.assertIsNone(value["w1_instance_id"])

    def test_x08_replacement_lifecycle_has_checkpoint_fence_exit_restore_e1(self) -> None:
        required = run_batch.lifecycle_contract("T0")["required_steps"]
        ordered = ["W0_CHECKPOINT", "CHECKPOINT_DISK_READBACK", "E0_FENCED", "W0_OS_EXIT", "W1_START", "W1_RESTORE", "STATE_CARRIAGE_PASS", "E1_CURRENT"]
        self.assertEqual([required.index(name) for name in ordered], sorted(required.index(name) for name in ordered))
        self.assertEqual(run_batch.review_alignment_evidence(self._valid())["verdict"], "PASS_ALIGNED_EPISODE")

    def test_x09_prospective_readiness_is_hard_prestart_gate(self) -> None:
        value = self._valid()
        value["readiness"] = "NOT_READY"
        result = run_batch.review_alignment_evidence(value)
        self.assertEqual(result["verdict"], "INCONCLUSIVE")
        self.assertIn("PROSPECTIVE_READINESS_OR_FREEZE_MISSING", self._codes(value))

    def test_x10_capture_gap_blocks_writer_and_is_inconclusive(self) -> None:
        value = self._valid()
        value["capture_gaps"] = [{"code": "UNKNOWN_WRITER"}]
        value["writer_admission"] = "BLOCKED"
        result = run_batch.review_alignment_evidence(value)
        self.assertEqual(result["verdict"], "INCONCLUSIVE")
        self.assertIn("CAPTURE_GAP", self._codes(value))

    def test_x11_observer_derived_effects_promotions_are_exact_protected_surfaces(self) -> None:
        value = self._valid()
        self.assertEqual({row["coordinate"] for row in value["surface_inventory"]}, set(run_batch.PROTECTED_SURFACES))
        self.assertEqual(run_batch.review_alignment_evidence(value)["verdict"], "PASS_ALIGNED_EPISODE")

    def test_x12_positive_n0_n1_t0_effect_coordinates_total_three(self) -> None:
        check = run_batch.validate_matrix_contract(self.matrix)
        self.assertEqual(check["expected_effect_total"], 3)
        self.assertEqual(run_batch.POSITIVE_EFFECT_COORDINATES, {("N0", "RESOLVED_CHECK"), ("N1", "RESOLVED_CHECK"), ("T0", "RESOLVED_CHECK")})

    def test_x13_confirmed_ea_expected_total_zero(self) -> None:
        self.assertEqual(run_batch.validate_matrix_contract(self.matrix)["expected_promotion_total"], 0)

    def test_x14_fresh_per_episode_database_rule_is_create_only(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "fresh.sqlite3"
            broker = Broker(path)
            broker.close()
            with self.assertRaises(FileExistsError):
                Broker(path)

    def test_x15_no_batch_retry_path(self) -> None:
        source = Path(run_batch.__file__).read_text(encoding="utf-8")
        self.assertIn('"batch_retry": "FORBIDDEN"', source)
        self.assertNotIn("for retry", source.casefold())

    def test_x16_unrun_aborted_cells_remain_in_denominator(self) -> None:
        rows = run_batch.denominator_result(self.matrix, {"N0": {"cell_id": "N0", "execution_status": "COMPLETE"}}, "N1")
        self.assertEqual(len(rows), 18)
        self.assertEqual(sum(row["execution_status"] == "ABORTED_NOT_RUN" for row in rows), 17)

    def test_x17_o01_missing_w0_os_exit_refused(self) -> None:
        value = self._valid()
        value["lifecycle_steps"].remove("W0_OS_EXIT")
        value["w0_cleanup"] = "UNPROVEN"
        self.assertIn("O01_MISSING_W0_OS_EXIT", self._codes(value))

    def test_x18_o02_sham_continuation_before_release_refused(self) -> None:
        value = self._valid(cell_id="N1", checkpoint="OPEN_CHECK")
        steps = value["lifecycle_steps"]
        release_index, continue_index = steps.index("RELEASE"), steps.index("CONTINUE")
        steps[release_index], steps[continue_index] = steps[continue_index], steps[release_index]
        self.assertIn("O02_SHAM_CONTINUE_BEFORE_RELEASE", self._codes(value))

    def test_x19_o03_blocked_t3_target_row_refused(self) -> None:
        value = self._valid(cell_id="T3", checkpoint="fault")
        value["actual_effect_delta"] = 1
        self.assertIn("O03_FORBIDDEN_EFFECT_LEAKAGE", self._codes(value))

    def test_x20_o04_positive_resolved_without_row_refused(self) -> None:
        value = self._valid()
        value["actual_effect_delta"] = 0
        self.assertIn("O04_POSITIVE_EFFECT_LIVENESS_MISSING", self._codes(value))

    def test_x21_o05_alias_roots_not_independent(self) -> None:
        value = self._valid()
        value["approval_roots"] = ["root:alpha", "root:alpha"]
        self.assertIn("O05_ALIAS_ROOTS_NOT_INDEPENDENT", self._codes(value))

    def test_x22_o06_open_qfr_cannot_collapse_without_qcr(self) -> None:
        value = self._valid()
        value["qcr_valid"] = False
        self.assertIn("O06_OPEN_QFR_FALSE_COLLAPSE", self._codes(value))

    def test_x23_o07_lost_obligation_fails_carriage(self) -> None:
        value = self._valid(cell_id="T3", checkpoint="fault")
        value["carried_obligations"] = []
        self.assertIn("O07_OBLIGATION_CARRIAGE_LOST", self._codes(value))

    def test_x24_o08_promotion_row_refused(self) -> None:
        value = self._valid(cell_id="T8", checkpoint="fault")
        value["actual_promotion_delta"] = 1
        self.assertIn("O08_QUARANTINE_PROMOTION_OBSERVED", self._codes(value))

    def test_x25_o09_e0_current_after_reset_refused(self) -> None:
        value = self._valid()
        value["current_epoch"] = "E0"
        self.assertIn("O09_E0_CURRENT_AFTER_RESET", self._codes(value))

    def test_x26_o10_foreign_case_run_evidence_refused(self) -> None:
        value = self._valid()
        value["evidence_binding"]["matrix_run_id"] = "foreign-run"
        self.assertIn("O10_FOREIGN_CASE_OR_RUN_EVIDENCE", self._codes(value))

    def test_x27_o11_incomplete_attempt_registry_is_inconclusive(self) -> None:
        value = self._valid(cell_id="T3", checkpoint="fault")
        value["attempt_coverage_complete"] = False
        value["registry_coverage_complete"] = False
        result = run_batch.review_alignment_evidence(value)
        self.assertEqual(result["verdict"], "INCONCLUSIVE")
        self.assertIn("O11_NON_EFFECT_COVERAGE_INCOMPLETE", self._codes(value))

    def test_x28_o12_duplicate_surface_id_coordinate_fails_inventory(self) -> None:
        value = self._valid()
        value["surface_inventory"][1] = copy.deepcopy(value["surface_inventory"][0])
        self.assertIn("O12_SURFACE_INVENTORY_DUPLICATED_OR_INCOMPLETE", self._codes(value))

    def test_x29_protected_components_are_reused_not_reimplemented(self) -> None:
        source = Path(run_batch.__file__).read_text(encoding="utf-8")
        for import_name in ("Broker", "WorkerProcess", "prepare_prospective_observation", "inspect_checkpoint", "evaluate"):
            self.assertIn(import_name, source)
        self.assertFalse((Path(run_batch.__file__).parent / "matrix_framework.py").exists())

    def test_x30_offline_validation_does_not_enter_measured_run(self) -> None:
        argv = [
            "--matrix-run-id", "x-offline-control-001", "--output", "unused-output", "--matrix", "unused-matrix",
            "--report-schema", "unused-schema", "--key-store", "unused-keys", "--worker", "unused-worker",
            "--launcher", "unused-launcher", "--observation-acceptance", "unused-b", "--observation-calibration", "unused-c",
            "--successor-baseline", "unused-baseline", "--stage-dir", "/tmp/unused-stage",
        ]
        self.assertEqual(run_batch.main(argv), 3)

    def test_x31_cli_requires_current_acceptance_calibration_and_successor_baseline(self) -> None:
        with self.assertRaises(SystemExit):
            run_batch.main(["--matrix-run-id", "x-offline-control-001"])

    def test_x32_clean_alignment_evidence_passes(self) -> None:
        self.assertEqual(run_batch.review_alignment_evidence(self._valid())["verdict"], "PASS_ALIGNED_EPISODE")

    def test_x33_only_safety_boundary_reasons_stop_whole_batch(self) -> None:
        self.assertFalse(run_batch.batch_stop_required("ORDINARY_CONFORMANCE_FAILURE"))
        for reason in run_batch.WHOLE_BATCH_STOP_REASONS:
            with self.subTest(reason=reason):
                self.assertTrue(run_batch.batch_stop_required(reason))


if __name__ == "__main__":
    unittest.main()
