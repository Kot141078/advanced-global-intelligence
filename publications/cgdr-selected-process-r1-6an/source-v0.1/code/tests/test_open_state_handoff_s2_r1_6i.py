from __future__ import annotations

import base64
import copy
import hashlib
import importlib.util
import json
import os
import shutil
import sqlite3
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from cgdr_r1_6b.broker import Broker
from cgdr_r1_6b.common import canonical_hash
from cgdr_r1_6b.s2_handoff import (
    TASK_ID,
    authority_public_map,
    build_current_source_view,
    build_delta_plan,
    build_open_prestate,
    build_source_inventory,
    inventory_issues,
    make_e0_fence_payload,
    make_e1_payload,
    run_hold_gate,
    sha256_bytes,
    sign_authority_payload,
)
from cgdr_r1_6b.s2_native import emit_and_validate_s2_hold
from cgdr_r1_6b.s2_review import REQUIRED_STEPS, review_s2_evidence
from cgdr_r1_6b.signing import TestKeyStore
from cgdr_r1_6b.state_transfer import freeze_state
from cgdr_r1_6b.supervisor import StagedRuntime, _worker_command
from cgdr_r1_6b.worker import StateMachine, _load_s2_plan


_RUN_S2_PATH = Path(__file__).resolve().parents[1] / "tools" / "run_s2.py"
_RUN_S2_SPEC = importlib.util.spec_from_file_location("r16o_run_s2", _RUN_S2_PATH)
_RUN_S2 = importlib.util.module_from_spec(_RUN_S2_SPEC)
assert _RUN_S2_SPEC.loader is not None
_RUN_S2_SPEC.loader.exec_module(_RUN_S2)
_check_observation_acceptance = _RUN_S2._check_observation_acceptance


def _binding(instance: str, pid: int, ticks: int, role: str, stage: str) -> tuple[dict, dict, dict]:
    binding = {
        "marker": "CGDR_CHILD_BOUND",
        "binding_source": "TRUSTED_DIRECT_FORK_PARENT",
        "wait_source": "POSIX_WAITPID_CHILD",
        "receipt_channel": "PARENT_ONLY_STDERR_V1",
        "instance_id": instance,
        "worker_pid": pid,
        "worker_start_ticks": ticks,
        "waiter_pid": 1,
        "waiter_start_ticks": ticks - 1,
        "pid_namespace": f"pid:[{pid}]",
        "network_namespace": f"net:[{pid}]",
        "mount_namespace": f"mnt:[{pid}]",
        "worker_sha256": "a" * 64,
        "launcher_sha256": "b" * 64,
    }
    security = {
        "marker": "CGDR_CHILD_SECURITY",
        "binding_source": "TRUSTED_DIRECT_FORK_PARENT_POST_EXEC_PROCFS",
        "receipt_channel": "PARENT_ONLY_STDERR_V1",
        "instance_id": instance,
        "worker_pid": pid,
        "worker_start_ticks": ticks,
        "pid_namespace": binding["pid_namespace"],
        "network_namespace": binding["network_namespace"],
        "mount_namespace": binding["mount_namespace"],
        "worker_stderr_route": "DEDICATED_PIPE_WRAPPED_BY_TRUSTED_PARENT",
        "trusted_receipt_route": "PARENT_ONLY_STDERR_V1",
        "security_receipt_sha256": "c" * 64,
        "status": {
            "status_fields": {
                "CapInh": "0000000000000000",
                "CapPrm": "0000000000000000",
                "CapEff": "0000000000000000",
                "CapBnd": "0000000000000000",
                "CapAmb": "0000000000000000",
                "NoNewPrivs": "1",
            },
            "fds": [{"fd": 0}, {"fd": 1}, {"fd": 2}],
        },
        "mounts": [
            {"mount_point": stage, "mount_options": ["ro"], "filesystem": "ext4"},
            {"mount_point": f"{stage}/scratch", "mount_options": ["rw"], "filesystem": "tmpfs"},
            {"mount_point": f"{stage}/private", "mount_options": ["rw"], "filesystem": "tmpfs"},
            {"mount_point": "/mnt", "mount_options": ["rw"], "filesystem": "tmpfs"},
        ],
    }
    inner_exit = {
        **binding,
        "marker": "CGDR_INNER_EXIT",
        "security_receipt_sha256": security["security_receipt_sha256"],
        "return_code": 0,
    }
    return binding, security, inner_exit


class S2Fixture:
    def __init__(self, root: Path):
        self.root = root
        self.attempt = "s2-r1-6i-process-free-control"
        self.w0_id = "synthetic-w0"
        self.w1_id = "synthetic-w1"
        self.stage0 = "/tmp/cgdr-r1-6i-s2-w0-process-free"
        self.stage1 = "/tmp/cgdr-r1-6i-s2-w1-process-free"
        self.keys = TestKeyStore(root / "keys")
        self.public = authority_public_map(self.keys)
        self.source = build_open_prestate(self.attempt, self.w0_id)
        self.frozen = freeze_state(self.source)
        self.inventory = build_source_inventory(self.source)
        self.checkpoint_canary = "/mnt/c/Users/kotov/CGDR-lab/CGDR_SELECTED_PROCESS_OPEN_STATE_HANDOFF_S2_R1_6I/test/checkpoint.bin"
        self.private_canary = "/mnt/c/Users/kotov/CGDR-lab/CGDR_SELECTED_PROCESS_OPEN_STATE_HANDOFF_S2_R1_6I/test/private.bin"
        self.plans = {}
        self.plan_hashes = {"W0": "0" * 64, "W1": "1" * 64}
        for role, stage in (("W0", self.stage0), ("W1", self.stage1)):
            payload = f"input::{role}".encode()
            self.plans[role] = build_delta_plan(
                attempt_id=self.attempt,
                worker_role=role,
                stage_dir=stage,
                input_sha256=sha256_bytes(payload),
                input_bytes=len(payload),
                checkpoint_canary_windows="C:\\synthetic\\checkpoint.bin",
                checkpoint_canary_wsl=self.checkpoint_canary,
                private_canary_windows="C:\\synthetic\\private.bin",
                private_canary_wsl=self.private_canary,
            )
        b0, s0, x0 = _binding(self.w0_id, 11, 101, "W0", self.stage0)
        b1, s1, x1 = _binding(self.w1_id, 12, 201, "W1", self.stage1)
        self.fence = sign_authority_payload(make_e0_fence_payload(attempt_id=self.attempt, source=self.source, w0_binding=b0, checkpoint_raw_sha256=sha256_bytes(self.frozen["bytes"])), self.keys)
        self.e1 = sign_authority_payload(make_e1_payload(attempt_id=self.attempt, w1_binding=b1, source=self.source, checkpoint_raw_sha256=sha256_bytes(self.frozen["bytes"]), checkpoint_canonical_sha256=self.frozen["state_sha256"], fence_envelope=self.fence), self.keys)
        self.current, self.transition = build_current_source_view(self.frozen["state"], attempt_id=self.attempt, w1_binding=b1, e0_fence=self.fence, e1_envelope=self.e1, public_map=self.public)
        self.gate = run_hold_gate(database=root / "gate.sqlite3", source=self.current, keys=self.keys, public_map=self.public, attempt_id=self.attempt, instance_id=self.w1_id)
        self.bundle = self._bundle(b0, s0, x0, b1, s1, x1)

    def _delta(self, role: str) -> dict:
        rows = []
        for item in self.plans[role]["probes"]:
            if item["expectation"] == "EXPECT_DENY":
                outcome = {"allowed": False, "errno": 13, "error_class": "PermissionError"}
            elif item["operation"] == "FILE_READ":
                outcome = {"allowed": True, "bytes": item["expected_bytes"], "observed_sha256": item["expected_sha256"]}
            else:
                outcome = {"allowed": True, "bytes_written": 12, "bytes_read": 12, "observed_sha256": "d" * 64}
            rows.append({"probe_id": item["probe_id"], "object_id": item["object_id"], "operation": item["operation"], "expectation": item["expectation"], "target": item["target"], "syscall_attempted": True, **outcome})
        return {"event": "S2_DELTA_RESULT", "instance_id": self.w0_id if role == "W0" else self.w1_id, "worker_role": role, "plan_sha256": self.plan_hashes[role], "result": {"rows": rows, "stopped_after_forbidden_success": None, "planned_count": 5}}

    def _worker(self, role: str, binding: dict, security: dict, inner_exit: dict) -> dict:
        instance = binding["instance_id"]
        stage = self.stage0 if role == "W0" else self.stage1
        diagnostics = {
            "child_binding": binding,
            "child_security": security,
            "inner_exit": inner_exit,
            "staged_runtime": {"mode": "S2", "stage_dir": stage},
            "launch_outcome": {"cleanup_status": "PROVEN"},
        }
        ready = {
            "event": "READY",
            "instance_id": instance,
            "security_metadata": {"environment_keys": [
                "CGDR_INSTANCE_ID", "CGDR_PDEATHSIG_SET", "CGDR_S1_MODE", "CGDR_S2_ATTEMPT_ID",
                "CGDR_S2_MODE", "CGDR_S2_PLAN", "CGDR_S2_PLAN_SHA256", "CGDR_S2_WORKER_ROLE",
                "LANG", "PATH", "PYTHONHASHSEED",
            ]},
        }
        if role == "W0":
            return {
                "instance_id": instance,
                "diagnostics": diagnostics,
                "ready": ready,
                "delta_result": self._delta(role),
                "load_ack": {"event": "LOAD_ACK", "instance_id": instance, "state_sha256": self.frozen["state_sha256"]},
                "checkpoint": {"event": "CHECKPOINT", "instance_id": instance, "state_b64": self.frozen["state_b64"], "state_sha256": self.frozen["state_sha256"], "checkpoint_seq": 1},
                "sham_wait": {"event": "SHAM_WAITING", "instance_id": instance},
                "release": {"event": "RELEASED", "instance_id": instance},
                "continued": {"event": "CONTINUED", "instance_id": instance},
            }
        return {
            "instance_id": instance,
            "diagnostics": diagnostics,
            "ready": ready,
            "delta_result": self._delta(role),
            "restore": {"event": "RESTORED", "instance_id": instance, "state_sha256": sha256_bytes(self.frozen["bytes"]), "checkpoint_seq": 1},
            "checkpoint": {"event": "CHECKPOINT", "instance_id": instance, "state_b64": self.frozen["state_b64"], "state_sha256": self.frozen["state_sha256"], "checkpoint_seq": 1},
        }

    def _bundle(self, b0: dict, s0: dict, x0: dict, b1: dict, s1: dict, x1: dict) -> dict:
        chronology = []
        for step in REQUIRED_STEPS:
            chronology.append({"step": step, "instance_id": self.w0_id if step.startswith("W0_") or step == "E0_FENCED" else self.w1_id})
        raw_b64 = base64.b64encode(self.frozen["bytes"]).decode("ascii")
        gate = {**self.gate}
        return {
            "task_id": TASK_ID,
            "evidence_scope": "SYNTHETIC_TRACE",
            "attempt_id": self.attempt,
            "chronology": chronology,
            "prestate": self.source,
            "inventory": self.inventory,
            "delta_plans": self.plans,
            "delta_plan_hashes": self.plan_hashes,
            "s1_to_s2_delta": {"status": "STATIC_CONFIG_VERIFIED_FOR_S2_OBJECT_DELTA"},
            "w0": self._worker("W0", b0, s0, x0),
            "checkpoint_disk": {"write_b64": raw_b64, "readback_b64": raw_b64, "write_raw_sha256": sha256_bytes(self.frozen["bytes"]), "readback_raw_sha256": sha256_bytes(self.frozen["bytes"]), "canonical_sha256": self.frozen["state_sha256"]},
            "w1": self._worker("W1", b1, s1, x1),
            "authority": {"e0_fence": self.fence, "e1_current": self.e1, "current_source_view": self.current, "epoch_transition": self.transition},
            "public_signer_map": self.public,
            "gate": gate,
            "native_validation": {"scope": "SYNTHETIC_REGRESSION", "accepted": True, "layer_status": {"shape": "PASS", "record_semantics": "PASS", "registered_evidence": "PASS", "bundle_links": "PASS"}},
            "canary_snapshots": {"checkpoint_store_canary": {"before": {"sha256": "a"}, "after": {"sha256": "a"}}, "private_canary": {"before": {"sha256": "b"}, "after": {"sha256": "b"}}},
        }


class S2ExternalMaskedTargetRelocatabilityTests(unittest.TestCase):
    checkpoint_suffix = "/external_trusted/checkpoint_store/checkpoint_store_canary.bin"
    private_suffix = "/external_trusted/private/private_canary.bin"

    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.attempt = "s2-r1-6i-t-process-free-control"
        self.stage = "/tmp/cgdr-r1-6i-s2-w0-t-process-free"

    def tearDown(self) -> None:
        self.temp.cleanup()

    def _plan(self, windows_root: str, wsl_root: str) -> dict:
        payload = b"r1-6t-process-free-input"
        return build_delta_plan(
            attempt_id=self.attempt,
            worker_role="W0",
            stage_dir=self.stage,
            input_sha256=hashlib.sha256(payload).hexdigest(),
            input_bytes=len(payload),
            checkpoint_canary_windows=windows_root + self.checkpoint_suffix.replace("/", "\\"),
            checkpoint_canary_wsl=wsl_root + self.checkpoint_suffix,
            private_canary_windows=windows_root + self.private_suffix.replace("/", "\\"),
            private_canary_wsl=wsl_root + self.private_suffix,
        )

    def _load(self, plan: dict, *, expected_hash: str | None = None):
        path = self.root / "S2_DELTA_PLAN.json"
        raw = (json.dumps(plan, indent=2, sort_keys=True) + "\n").encode()
        path.write_bytes(raw)
        environment = {
            "CGDR_S2_PLAN": str(path),
            "CGDR_S2_PLAN_SHA256": expected_hash or hashlib.sha256(raw).hexdigest(),
            "CGDR_S2_ATTEMPT_ID": self.attempt,
            "CGDR_S2_WORKER_ROLE": "W0",
        }
        with mock.patch.dict(os.environ, environment, clear=False):
            return _load_s2_plan()

    @staticmethod
    def _replace_probe_target(plan: dict, old: str, new: str) -> None:
        for probe in plan["probes"]:
            if probe["target"] == old:
                probe["target"] = new

    def test_t01_relocated_current_task_external_root_accepted(self):
        plan = self._plan(
            r"C:\Users\kotov\CGDR-lab\CGDR_SELECTED_PROCESS_S2_EXTERNAL_MASKED_TARGET_RELOCATABILITY_REPAIR_R1_6T\control",
            "/mnt/c/Users/kotov/CGDR-lab/CGDR_SELECTED_PROCESS_S2_EXTERNAL_MASKED_TARGET_RELOCATABILITY_REPAIR_R1_6T/control",
        )
        loaded, digest, role = self._load(plan)
        self.assertEqual(plan, loaded)
        self.assertEqual("W0", role)
        self.assertEqual(64, len(digest))

    def test_t02_historical_i_shaped_external_root_remains_accepted(self):
        plan = self._plan(
            r"C:\Users\kotov\CGDR-lab\CGDR_SELECTED_PROCESS_OPEN_STATE_HANDOFF_S2_R1_6I\control",
            "/mnt/c/Users/kotov/CGDR-lab/CGDR_SELECTED_PROCESS_OPEN_STATE_HANDOFF_S2_R1_6I/control",
        )
        self.assertEqual("W0", self._load(plan)[2])

    def test_t03_windows_wsl_representation_mismatch_refused(self):
        plan = self._plan(r"C:\CGDR\T\control", "/mnt/c/CGDR/T/control")
        plan["external_masked_targets"]["checkpoint_store_canary"]["wsl_path"] = (
            "/mnt/c/CGDR/T/other" + self.checkpoint_suffix
        )
        with self.assertRaisesRegex(ValueError, "external masked target representation mismatch"):
            self._load(plan)

    def test_t04_checkpoint_private_different_shared_roots_refused(self):
        plan = self._plan(r"C:\CGDR\T\control", "/mnt/c/CGDR/T/control")
        entry = plan["external_masked_targets"]["private_canary"]
        old = entry["wsl_path"]
        entry["windows_path"] = r"C:\CGDR\T\other" + self.private_suffix.replace("/", "\\")
        entry["wsl_path"] = "/mnt/c/CGDR/T/other" + self.private_suffix
        self._replace_probe_target(plan, old, entry["wsl_path"])
        with self.assertRaisesRegex(ValueError, "external masked target shared root mismatch"):
            self._load(plan)

    def test_t05_wrong_checkpoint_or_private_suffix_refused(self):
        cases = (
            ("checkpoint_store_canary", self.checkpoint_suffix, "/external_trusted/checkpoint_store/wrong.bin"),
            ("private_canary", self.private_suffix, "/external_trusted/private/wrong.bin"),
        )
        for name, suffix, wrong_suffix in cases:
            with self.subTest(name=name):
                plan = self._plan(r"C:\CGDR\T\control", "/mnt/c/CGDR/T/control")
                entry = plan["external_masked_targets"][name]
                old = entry["wsl_path"]
                entry["windows_path"] = entry["windows_path"][: -len(suffix)] + wrong_suffix.replace("/", "\\")
                entry["wsl_path"] = entry["wsl_path"][: -len(suffix)] + wrong_suffix
                self._replace_probe_target(plan, old, entry["wsl_path"])
                with self.assertRaisesRegex(ValueError, "external masked target suffix mismatch"):
                    self._load(plan)

    def test_t06_dot_or_dot_dot_component_refused(self):
        for component in (".", ".."):
            with self.subTest(component=component):
                plan = self._plan(
                    rf"C:\CGDR\T\{component}\control",
                    f"/mnt/c/CGDR/T/{component}/control",
                )
                with self.assertRaisesRegex(ValueError, "external masked target path safety mismatch"):
                    self._load(plan)

    def test_t07_target_outside_mnt_c_refused(self):
        plan = self._plan(r"C:\CGDR\T\control", "/mnt/c/CGDR/T/control")
        entry = plan["external_masked_targets"]["checkpoint_store_canary"]
        old = entry["wsl_path"]
        entry["wsl_path"] = "/opt/CGDR/T/control" + self.checkpoint_suffix
        self._replace_probe_target(plan, old, entry["wsl_path"])
        with self.assertRaisesRegex(ValueError, "external masked target path safety mismatch"):
            self._load(plan)

    def test_t08_missing_or_extra_external_target_identity_refused(self):
        for mode in ("missing", "extra"):
            with self.subTest(mode=mode):
                plan = self._plan(r"C:\CGDR\T\control", "/mnt/c/CGDR/T/control")
                if mode == "missing":
                    plan["external_masked_targets"].pop("private_canary")
                else:
                    plan["external_masked_targets"]["extra_canary"] = copy.deepcopy(
                        plan["external_masked_targets"]["private_canary"]
                    )
                with self.assertRaisesRegex(ValueError, "external masked target inventory mismatch"):
                    self._load(plan)

    def test_t09_wrong_mask_boundary_declaration_refused(self):
        for name in ("checkpoint_store_canary", "private_canary"):
            with self.subTest(name=name):
                plan = self._plan(r"C:\CGDR\T\control", "/mnt/c/CGDR/T/control")
                plan["external_masked_targets"][name]["boundary"] = "WEAK_OR_UNKNOWN_BOUNDARY"
                with self.assertRaisesRegex(ValueError, "external masked target boundary mismatch"):
                    self._load(plan)

    def test_t10_plan_hash_mismatch_remains_refused(self):
        plan = self._plan(r"C:\CGDR\T\control", "/mnt/c/CGDR/T/control")
        with self.assertRaisesRegex(ValueError, "S2 plan hash mismatch"):
            self._load(plan, expected_hash="0" * 64)

    def test_t11_task_attempt_and_role_bindings_remain_refused(self):
        cases = (("task_id", "WRONG"), ("attempt_id", "WRONG"), ("worker_role", "W1"))
        for field, value in cases:
            with self.subTest(field=field):
                plan = self._plan(r"C:\CGDR\T\control", "/mnt/c/CGDR/T/control")
                plan[field] = value
                with self.assertRaisesRegex(ValueError, "S2 plan task/attempt/role binding mismatch"):
                    self._load(plan)

    def test_t12_stage_and_command_bindings_remain_refused(self):
        plan = self._plan(r"C:\CGDR\T\control", "/mnt/c/CGDR/T/control")
        plan["stage_dir"] = "/tmp/not-the-frozen-stage"
        with self.assertRaisesRegex(ValueError, "S2 plan stage binding mismatch"):
            self._load(plan)
        plan = self._plan(r"C:\CGDR\T\control", "/mnt/c/CGDR/T/control")
        plan["allowed_commands"].append("PROCESS")
        with self.assertRaisesRegex(ValueError, "S2 allowed command set mismatch"):
            self._load(plan)

    def test_t13_probe_structure_operation_and_target_bindings_remain_refused(self):
        cases = ("count", "duplicate", "operation", "target")
        for mode in cases:
            with self.subTest(mode=mode):
                plan = self._plan(r"C:\CGDR\T\control", "/mnt/c/CGDR/T/control")
                if mode == "count":
                    plan["probes"].pop()
                    reason = "S2 delta probe list invalid"
                elif mode == "duplicate":
                    plan["probes"][1]["probe_id"] = plan["probes"][0]["probe_id"]
                    reason = "S2 plan duplicate/invalid probe id"
                elif mode == "operation":
                    plan["probes"][0]["operation"] = "EXEC"
                    reason = "S2 plan operation/expectation invalid"
                else:
                    plan["probes"][0]["target"] = "/etc/passwd"
                    reason = "S2 plan target outside frozen roots"
                with self.assertRaisesRegex(ValueError, reason):
                    self._load(plan)


class OpenStateHandoffTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.fx = S2Fixture(Path(self.temp.name))

    def tearDown(self) -> None:
        self.temp.cleanup()

    def _review(self, mutate=None):
        bundle = copy.deepcopy(self.fx.bundle)
        if mutate:
            mutate(bundle)
        return review_s2_evidence(bundle)

    def test_positive_synthetic_review_control(self):
        result = self._review()
        self.assertEqual("PASS_SYNTHETIC_REVIEW_CONTROL", result["verdict"])
        self.assertEqual([], result["issues"])

    def test_missing_load_before_exit_is_not_pass(self):
        result = self._review(lambda b: b["chronology"].__setitem__(6, {"step": "REMOVED"}))
        self.assertEqual("INCONCLUSIVE", result["verdict"])
        self.assertIn("MISSING_CAUSAL_STEP:W0_LOAD_ACK", {x["code"] for x in result["issues"]})

    def test_missing_checkpoint_before_exit_is_not_pass(self):
        result = self._review(lambda b: b["chronology"].__setitem__(7, {"step": "REMOVED"}))
        self.assertEqual("INCONCLUSIVE", result["verdict"])
        self.assertIn("MISSING_CAUSAL_STEP:W0_CHECKPOINT", {x["code"] for x in result["issues"]})

    def test_foreign_direct_wait_is_not_pass(self):
        def mutate(b):
            b["w0"]["diagnostics"]["inner_exit"]["worker_pid"] = 999
        result = self._review(mutate)
        self.assertIn("W0_DIRECT_WAIT_EXIT_BINDING_INVALID", {x["code"] for x in result["issues"]})

    def test_early_w1_is_fail(self):
        def mutate(b):
            rows = b["chronology"]
            w1 = next(row for row in rows if row["step"] == "W1_START_REQUEST")
            rows.remove(w1)
            rows.insert(10, w1)
        result = self._review(mutate)
        self.assertEqual("FAIL", result["verdict"])
        self.assertTrue(any(x["code"].startswith("CAUSAL_ORDER_INVALID") for x in result["issues"]))

    def test_continue_before_release_is_fail(self):
        def mutate(b):
            rows = b["chronology"]
            a = next(i for i, row in enumerate(rows) if row["step"] == "W0_RELEASE")
            c = next(i for i, row in enumerate(rows) if row["step"] == "W0_CONTINUE")
            rows[a], rows[c] = rows[c], rows[a]
        result = self._review(mutate)
        self.assertEqual("FAIL", result["verdict"])

    def test_rehashed_variant_loss_detected(self):
        def mutate(b):
            state = json.loads(base64.b64decode(b["w1"]["checkpoint"]["state_b64"]))
            state["qsf"]["variants"] = state["qsf"]["variants"][:2]
            raw = json.dumps(state, sort_keys=True, separators=(",", ":")).encode()
            b["w1"]["checkpoint"]["state_b64"] = base64.b64encode(raw).decode()
            b["w1"]["checkpoint"]["state_sha256"] = hashlib.sha256(raw).hexdigest()
        result = self._review(mutate)
        self.assertEqual("FAIL", result["verdict"])
        self.assertTrue(any("W1_RESTORED_BYTES_OR_SEQUENCE_MISMATCH" in x["code"] or "W1_INVENTORY" in x["code"] for x in result["issues"]))

    def test_rehashed_duty_loss_detected(self):
        def mutate(b):
            state = json.loads(base64.b64decode(b["checkpoint_disk"]["readback_b64"]))
            state.pop("duty")
            raw = json.dumps(state, sort_keys=True, separators=(",", ":")).encode()
            enc, digest = base64.b64encode(raw).decode(), hashlib.sha256(raw).hexdigest()
            for name in ("write_b64", "readback_b64"):
                b["checkpoint_disk"][name] = enc
            b["checkpoint_disk"]["write_raw_sha256"] = digest
            b["checkpoint_disk"]["readback_raw_sha256"] = digest
            b["checkpoint_disk"]["canonical_sha256"] = digest
        result = self._review(mutate)
        self.assertEqual("FAIL", result["verdict"])
        self.assertTrue(any("duty" in x["code"].lower() or "MATERIAL_FIELD" in x["code"] for x in result["issues"]))

    def test_rehashed_dispute_loss_detected(self):
        def mutate(b):
            state = json.loads(base64.b64decode(b["w1"]["checkpoint"]["state_b64"]))
            state["qsf"]["dispute_refs"] = []
            raw = json.dumps(state, sort_keys=True, separators=(",", ":")).encode()
            b["w1"]["checkpoint"]["state_b64"] = base64.b64encode(raw).decode()
            b["w1"]["checkpoint"]["state_sha256"] = hashlib.sha256(raw).hexdigest()
        result = self._review(mutate)
        self.assertTrue(any("W1_INVENTORY:QSF_DISPUTE_INVENTORY_MISMATCH" == x["code"] or "W1_RESTORED_BYTES" in x["code"] for x in result["issues"]))

    def test_wrong_restore_sequence_is_fail(self):
        result = self._review(lambda b: b["w1"]["restore"].__setitem__("checkpoint_seq", 7))
        self.assertIn("W1_RESTORE_HASH_OR_SEQUENCE_MISMATCH", {x["code"] for x in result["issues"]})

    def test_wrong_load_ack_hash_is_fail(self):
        result = self._review(lambda b: b["w0"]["load_ack"].__setitem__("state_sha256", "f" * 64))
        self.assertIn("W0_LOAD_ACK_HASH_MISMATCH", {x["code"] for x in result["issues"]})

    def test_reuse_e0_is_fail(self):
        def mutate(b):
            b["authority"]["e1_current"] = b["authority"]["e0_fence"]
            b["authority"]["current_source_view"]["current_attestation"]["epoch"] = "E0"
        result = self._review(mutate)
        self.assertEqual("FAIL", result["verdict"])
        self.assertIn("E1_CURRENT_SCOPE_MISMATCH_OR_E0_REUSED", {x["code"] for x in result["issues"]})

    def test_copy_without_current_admission_is_fail(self):
        result = self._review(lambda b: b["gate"]["decision"].__setitem__("admission", "WITHHELD"))
        self.assertIn("W1_CURRENT_ADMISSION_NOT_ADMITTED", {x["code"] for x in result["issues"]})

    def test_unexpected_effect_and_promotion_are_fail(self):
        def mutate(b):
            b["gate"]["sink_after"]["effects"].append({"effect_id": "wrong"})
            b["gate"]["sink_after"]["promotions"].append(["wrong"])
        result = self._review(mutate)
        codes = {x["code"] for x in result["issues"]}
        self.assertIn("UNEXPECTED_S2_EFFECT", codes)
        self.assertIn("UNEXPECTED_S2_PROMOTION", codes)

    def test_unknown_sink_observation_is_inconclusive(self):
        result = self._review(lambda b: b["gate"].__setitem__("sink_after", None))
        self.assertEqual("INCONCLUSIVE", result["verdict"])
        self.assertIn("S2_SINK_OBSERVATION_UNKNOWN", {x["code"] for x in result["issues"]})

    def test_configuration_binding_drift_is_fail(self):
        result = self._review(lambda b: b["w1"]["diagnostics"]["child_security"]["status"]["status_fields"].__setitem__("CapEff", "0000000000000001"))
        self.assertIn("W1_CAPABILITY_SET_NOT_ZERO", {x["code"] for x in result["issues"]})

    def test_forbidden_delta_success_stops_and_fails(self):
        def mutate(b):
            row = b["w0"]["delta_result"]["result"]["rows"][1]
            row["allowed"] = True
            row.pop("errno", None)
            b["w0"]["delta_result"]["result"]["stopped_after_forbidden_success"] = row["probe_id"]
        result = self._review(mutate)
        self.assertTrue(any("FORBIDDEN_ACCESS_SUCCEEDED" in x["code"] for x in result["issues"]))

    def test_role_specific_state_machine_rejects_cross_role_commands(self):
        w0 = StateMachine("w0", s2_plan={"attempt_id": "a"}, s2_plan_sha256="h", s2_role="W0")
        w1 = StateMachine("w1", s2_plan={"attempt_id": "a"}, s2_plan_sha256="h", s2_role="W1")
        self.assertEqual("COMMAND_NOT_ALLOWED_IN_S2_ROLE", w0.handle({"command": "RESTORE"})[0]["reason"])
        self.assertEqual("COMMAND_NOT_ALLOWED_IN_S2_ROLE", w1.handle({"command": "LOAD"})[0]["reason"])
        self.assertEqual("COMMAND_NOT_ALLOWED_IN_S2_ROLE", w1.handle({"command": "PROCESS"})[0]["reason"])

    def test_launcher_argv_is_literal_and_helper_free(self):
        runtime = StagedRuntime(
            stage_dir=self.fx.stage0,
            worker=f"{self.fx.stage0}/worker.py",
            worker_sha256="a" * 64,
            launcher=f"{self.fx.stage0}/s0_launcher.py",
            launcher_sha256="b" * 64,
            stage_receipt={"kind": "S2_STAGE_RECEIPT"},
            mode="S2",
            s2_plan=f"{self.fx.stage0}/S2_DELTA_PLAN.json",
            s2_plan_sha256="c" * 64,
            s2_fixture_manifest=f"{self.fx.stage0}/S2_FIXTURE_MANIFEST.json",
            s2_fixture_manifest_sha256="d" * 64,
            s2_attempt_id=self.fx.attempt,
            s2_worker_role="W0",
        )
        command, _ = _worker_command("Ubuntu", runtime, "instance", "nonce")
        self.assertNotIn("sh", command)
        self.assertNotIn("eval", command)
        self.assertNotIn("--endpoint-mask-dir", command)
        self.assertIn("--s2-mode", command)

    def test_native_hold_adapter_passes_unchanged_validator_four_layers(self):
        phase = {**self.fx.gate, "source": self.fx.current, "attempt_id": self.fx.attempt, "grant_valid_until_utc": "2099-01-01T00:00:00Z", "times": {"planning_utc": "2026-09-06T12:00:00Z", "basis_utc": "2026-09-06T12:00:01Z", "changed_utc": "2026-09-06T12:00:02Z", "window_start_utc": "2026-09-06T12:00:00Z", "commit_utc": "2026-09-06T12:00:03Z", "window_end_utc": "2026-09-06T12:00:03Z", "perf_counter_start_ns": 1, "perf_counter_end_ns": 2}}
        result = emit_and_validate_s2_hold(phase, self.fx.root / "native", evidence_scope="SYNTHETIC_REGRESSION")
        self.assertTrue(result["accepted"], result["rows"])
        self.assertEqual({"shape": "PASS", "record_semantics": "PASS", "registered_evidence": "PASS", "bundle_links": "PASS"}, result["layer_status"])

    def test_prestate_inventory_is_complete_and_open(self):
        self.assertEqual([], inventory_issues(self.fx.frozen["state"], self.fx.inventory))
        self.assertEqual("OPEN", self.fx.source["qsf"]["state"])
        self.assertEqual(3, len(self.fx.source["qsf"]["variants"]))
        self.assertEqual("PENDING", self.fx.source["duty"]["status"])
        self.assertFalse(self.fx.source["quarantined_memory"]["action_force"])


class _ProcessFreeObservationStub:
    def __init__(self, broker: Broker, source: dict, attempt_id: str, instance_id: str):
        operation_id = f"operation:{attempt_id}:open-hold"
        self.broker = broker
        self.database = broker.path.resolve()
        self.plan = {
            "expected_operation_intent": {
                "scope": {
                    "task_id": source["trusted_policy"]["task_id"],
                    "action": source["trusted_policy"]["protected_action"],
                    "operation_id": operation_id,
                    "cell_id": "S2_OPEN_HANDOFF",
                    "attempt_id": attempt_id,
                    "checkpoint": "S2_OPEN_CHECK",
                    "instance_id": instance_id,
                    "commit_record_id": f"commit:{attempt_id}:open-hold",
                }
            }
        }
        self.before = {
            "snapshot_id": "observer-snapshot:before",
            "tables": {
                "effects": {"rows": [{"observer_surface": "before-effect"}]},
                "promotions": {"rows": [["observer-before-promotion"]]},
            },
        }
        self.after = {
            "snapshot_id": "observer-snapshot:after",
            "tables": {
                "effects": {"rows": [{"observer_surface": "after-effect"}]},
                "promotions": {"rows": [["observer-after-promotion"]]},
            },
        }
        self.admissions = []
        self.transactions = []

    def require_admission(self, name: str) -> None:
        self.admissions.append(name)

    def begin_phase(self, name: str) -> dict:
        if name != "S2_OPEN_CHECK":
            raise AssertionError(name)
        return copy.deepcopy(self.before)

    def begin_writer_transaction(self, transaction_id: str, **context) -> None:
        self.transactions.append([transaction_id, "BEGIN", context])

    def finish_writer_transaction(self, transaction_id: str, status: str, **context) -> None:
        self.transactions.append([transaction_id, status, context])

    def end_phase(self, name: str) -> dict:
        if name != "S2_OPEN_CHECK":
            raise AssertionError(name)
        return copy.deepcopy(self.after)

    def export_evidence(self) -> dict:
        return {"phases": {"S2_OPEN_CHECK": {"name": "S2_OPEN_CHECK", "status": "CLOSED"}}}


class ProspectiveSinkHeldReadbackTests(unittest.TestCase):
    U_OPERATION = [
        "operation:s2-r1-6i-u-68bbdddb97a01241f47f282c:open-hold",
        "4b55c92c98531d8ca564f060fb173996834b5cf09428955aa80a5c407ebc0d28",
        "HELD",
    ]

    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.fx = S2Fixture(self.root / "fixture")
        self.broker = Broker(self.root / "prospective.sqlite3")
        self.observation = _ProcessFreeObservationStub(
            self.broker,
            self.fx.current,
            self.fx.attempt,
            self.fx.w1_id,
        )
        self.evidence = Path(__file__).resolve().parents[2] / "evidence"

    def tearDown(self) -> None:
        self.broker.close()
        self.temp.cleanup()

    def _prospective_gate(self) -> dict:
        return run_hold_gate(
            broker=self.broker,
            observation=self.observation,
            source=self.fx.current,
            keys=self.fx.keys,
            public_map=self.fx.public,
            attempt_id=self.fx.attempt,
            instance_id=self.fx.w1_id,
        )

    def _u_bundle(self) -> dict:
        return json.loads((self.evidence / "U_S2_EVIDENCE_BUNDLE.json").read_text(encoding="utf-8"))

    def test_v01_exact_u_predecessor_is_sole_held_readback_mismatch(self):
        result = review_s2_evidence(self._u_bundle())
        self.assertEqual("FAIL", result["verdict"])
        self.assertEqual(
            [{"code": "EXACT_HELD_OPERATION_READBACK_MISMATCH", "severity": "FAIL"}],
            result["issues"],
        )

    def test_v02_exact_u_sqlite_row_in_memory_completion_passes(self):
        database = self.evidence / "U_S2_EFFECTS.sqlite3"
        self.assertEqual(
            "05e85e6f43ae77bede0fb1f67a24d1f407e2647a12c267f45d1198cadf6f8359",
            hashlib.sha256(database.read_bytes()).hexdigest(),
        )
        connection = sqlite3.connect(database.resolve().as_uri() + "?mode=ro&immutable=1", uri=True)
        try:
            operations = [list(row) for row in connection.execute(
                "SELECT operation_id,proposal_hash,result FROM operations ORDER BY operation_id"
            ).fetchall()]
        finally:
            connection.close()
        self.assertEqual([self.U_OPERATION], operations)
        bundle = self._u_bundle()
        bundle["gate"]["sink_after"]["operations"] = operations
        result = review_s2_evidence(bundle)
        self.assertEqual("PASS_SCOPED_S2", result["verdict"])
        self.assertEqual([], result["issues"])

    def test_v03_candidate_prospective_after_has_exact_held_readback(self):
        gate = self._prospective_gate()
        expected = [[gate["operation_id"], gate["packet_projection"]["proposal_hash"], "HELD"]]
        self.assertEqual(expected, [list(row) for row in gate["sink_after"]["operations"]])

    def test_v04_candidate_prospective_before_and_after_operations_are_bound(self):
        gate = self._prospective_gate()
        self.assertEqual([], gate["sink_before"]["operations"])
        self.assertEqual(1, len(gate["sink_after"]["operations"]))
        self.assertEqual("HELD", gate["sink_after"]["operations"][0][2])

    def test_v05_observer_surfaces_and_ids_are_preserved_while_operations_use_broker(self):
        gate = self._prospective_gate()
        self.assertEqual(self.observation.before["tables"]["effects"]["rows"], gate["sink_before"]["effects"])
        self.assertEqual(self.observation.before["tables"]["promotions"]["rows"], gate["sink_before"]["promotions"])
        self.assertEqual(self.observation.before["snapshot_id"], gate["sink_before"]["observation_snapshot_id"])
        self.assertEqual(self.observation.after["tables"]["effects"]["rows"], gate["sink_after"]["effects"])
        self.assertEqual(self.observation.after["tables"]["promotions"]["rows"], gate["sink_after"]["promotions"])
        self.assertEqual(self.observation.after["snapshot_id"], gate["sink_after"]["observation_snapshot_id"])
        self.assertEqual([], gate["sink_before"]["operations"])
        self.assertEqual("HELD", gate["sink_after"]["operations"][0][2])

    def test_v06_non_prospective_gate_retains_full_broker_snapshot_operations(self):
        before, after = self.fx.gate["sink_before"], self.fx.gate["sink_after"]
        expected_keys = {"authority", "operations", "effects", "promotions", "revocations", "source_bindings"}
        self.assertEqual(expected_keys, set(before))
        self.assertEqual(expected_keys, set(after))
        self.assertEqual([], before["operations"])
        self.assertEqual("HELD", after["operations"][0][2])

    def test_v07_unchanged_reviewer_rejects_missing_or_wrong_held_tuple(self):
        variants = {
            "missing": [],
            "wrong_operation": [["operation:wrong", self.fx.gate["packet_projection"]["proposal_hash"], "HELD"]],
            "wrong_proposal": [[self.fx.gate["operation_id"], "f" * 64, "HELD"]],
            "wrong_result": [[self.fx.gate["operation_id"], self.fx.gate["packet_projection"]["proposal_hash"], "RETURNED"]],
        }
        for name, operations in variants.items():
            with self.subTest(name=name):
                bundle = copy.deepcopy(self.fx.bundle)
                bundle["gate"]["sink_after"]["operations"] = operations
                result = review_s2_evidence(bundle)
                self.assertEqual("FAIL", result["verdict"])
                self.assertIn("EXACT_HELD_OPERATION_READBACK_MISMATCH", {issue["code"] for issue in result["issues"]})


class ObservationAcceptanceBindingTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.workspace = Path(__file__).resolve().parents[2]
        cls.code_root = Path(__file__).resolve().parents[1]
        cls.acceptance_path = cls.workspace / "inputs" / "B_CURRENT_ACCEPTANCE.json"
        cls.calibration_path = cls.workspace / "inputs" / "C_CURRENT_CALIBRATION.json"
        cls.historical_k_path = cls.workspace / "inputs" / "HISTORICAL_K_CALIBRATION.json"
        cls.acceptance = json.loads(cls.acceptance_path.read_text(encoding="utf-8-sig"))
        cls.calibration = json.loads(cls.calibration_path.read_text(encoding="utf-8-sig"))

    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)

    def tearDown(self) -> None:
        self.temp.cleanup()

    def _write_json(self, name: str, value: dict) -> Path:
        path = self.root / name
        path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8", newline="\n")
        return path

    def _code_fixture(self) -> Path:
        root = self.root / "code"
        for relative, _ in _RUN_S2.CURRENT_OBSERVATION_CODE_PINS.values():
            target = root / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(self.code_root / relative, target)
        return root

    def test_o01_1_old_k_as_current_refused(self):
        with self.assertRaisesRegex(RuntimeError, "OBSERVATION_ACCEPTANCE_SCHEMA_MISMATCH"):
            _check_observation_acceptance(self.historical_k_path, self.calibration_path, self.code_root)

    def test_o01_2_current_n_exact_pass(self):
        result = _check_observation_acceptance(self.acceptance_path, self.calibration_path, self.code_root)
        self.assertEqual("PASS_CURRENT_N_OBSERVATION_ACCEPTANCE_BOUND", result["status"])
        self.assertEqual(hashlib.sha256(self.acceptance_path.read_bytes()).hexdigest(), result["acceptance_sha256"])
        self.assertEqual(hashlib.sha256(self.calibration_path.read_bytes()).hexdigest(), result["calibration_sha256"])
        self.assertEqual(3, len(result["current_code_hashes"]))
        self.assertEqual(4, result["current_calibration"]["unique_calibration_cases"])

    def test_o01_3_m01_downgraded_refused(self):
        value = copy.deepcopy(self.acceptance)
        for downgraded in ("OPEN", "UNKNOWN"):
            with self.subTest(downgraded=downgraded):
                value["accepted_findings"]["M01"] = downgraded
                path = self._write_json(f"acceptance-{downgraded}.json", value)
                with self.assertRaisesRegex(RuntimeError, "OBSERVATION_ACCEPTANCE_M01_NOT_CLOSED"):
                    _check_observation_acceptance(path, self.calibration_path, self.code_root)

    def test_o01_4_current_code_hash_mismatch_refused(self):
        claimed = copy.deepcopy(self.acceptance)
        claimed["current_code"]["prospective_observation.py"]["sha256"] = "0" * 64
        claimed_path = self._write_json("acceptance-code-claim-mismatch.json", claimed)
        with self.assertRaisesRegex(RuntimeError, "OBSERVATION_CURRENT_CODE_CLAIM_MISMATCH"):
            _check_observation_acceptance(claimed_path, self.calibration_path, self.code_root)

        fixture = self._code_fixture()
        prospective = fixture / "src" / "cgdr_r1_6b" / "prospective_observation.py"
        prospective.write_bytes(prospective.read_bytes() + b"\n# O01 finite hash-mismatch fixture\n")
        with self.assertRaisesRegex(RuntimeError, "OBSERVATION_CURRENT_CODE_HASH_MISMATCH"):
            _check_observation_acceptance(self.acceptance_path, self.calibration_path, fixture)

    def test_o01_5_calibration_hash_mismatch_refused(self):
        original = self.calibration_path.read_bytes()
        mutated = original.replace(b'"status": "PASS"', b'"status": "PAXX"', 1)
        self.assertEqual(len(original), len(mutated))
        self.assertNotEqual(original, mutated)
        path = self.root / "calibration-hash-mismatch.json"
        path.write_bytes(mutated)
        with self.assertRaisesRegex(RuntimeError, "OBSERVATION_CALIBRATION_HASH_MISMATCH"):
            _check_observation_acceptance(self.acceptance_path, path, self.code_root)

    def test_o01_6_calibration_native_layer_fail_refused(self):
        calibration = copy.deepcopy(self.calibration)
        calibration["positive_hold"]["native_layers"]["bundle_links"] = "FAIL"
        calibration_path = self._write_json("calibration-native-fail.json", calibration)
        acceptance = copy.deepcopy(self.acceptance)
        data = calibration_path.read_bytes()
        acceptance["current_calibration"]["bytes"] = len(data)
        acceptance["current_calibration"]["sha256"] = hashlib.sha256(data).hexdigest()
        acceptance_path = self._write_json("acceptance-native-fail-binding.json", acceptance)
        with self.assertRaisesRegex(RuntimeError, "OBSERVATION_CALIBRATION_NATIVE_LAYER_NOT_PASS"):
            _check_observation_acceptance(acceptance_path, calibration_path, self.code_root)

    def test_o01_7_profile_or_coordinator_verdict_mismatch_refused(self):
        cases = (
            ("profile_binding", "PROFILE_BINDING_WRONG", "OBSERVATION_ACCEPTANCE_PROFILE_BINDING_MISMATCH"),
            ("coordinator_verdict", "UNKNOWN", "OBSERVATION_ACCEPTANCE_COORDINATOR_VERDICT_MISMATCH"),
        )
        for field, replacement, reason in cases:
            with self.subTest(field=field):
                value = copy.deepcopy(self.acceptance)
                value[field] = replacement
                path = self._write_json(f"acceptance-{field}-mismatch.json", value)
                with self.assertRaisesRegex(RuntimeError, reason):
                    _check_observation_acceptance(path, self.calibration_path, self.code_root)

    def test_o01_8_k_history_retained_not_current(self):
        self.assertEqual(
            "a71bb879febe12e29e2a26b790025fc351693ca8522bb36d7bdb029cdf580bfb",
            hashlib.sha256(self.historical_k_path.read_bytes()).hexdigest(),
        )
        historical = json.loads(self.historical_k_path.read_text(encoding="utf-8-sig"))
        self.assertEqual("CGDR_SELECTED_PROCESS_PROSPECTIVE_OBSERVATION_R1_6K", historical["task_id"])
        with self.assertRaisesRegex(RuntimeError, "OBSERVATION_ACCEPTANCE_SCHEMA_MISMATCH"):
            _check_observation_acceptance(self.historical_k_path, self.calibration_path, self.code_root)
        self.assertEqual(
            "PASS_CURRENT_N_OBSERVATION_ACCEPTANCE_BOUND",
            _check_observation_acceptance(self.acceptance_path, self.calibration_path, self.code_root)["status"],
        )

    def test_p01_claim_ceiling_byte_mutation_refused(self):
        value = copy.deepcopy(self.acceptance)
        value["claim_ceiling"] = "FULL_RUNTIME_PASS_SAME_C"
        path = self._write_json("p01-claim-ceiling-mutation.json", value)
        with self.assertRaisesRegex(RuntimeError, "OBSERVATION_ACCEPTANCE_ARTIFACT_BYTES_MISMATCH"):
            _check_observation_acceptance(path, self.calibration_path, self.code_root)

    def test_p02_current_iteration_byte_mutation_refused(self):
        value = copy.deepcopy(self.acceptance)
        value["current_iteration"] = "FORGED_CURRENT"
        path = self._write_json("p02-current-iteration-mutation.json", value)
        with self.assertRaisesRegex(RuntimeError, "OBSERVATION_ACCEPTANCE_ARTIFACT_BYTES_MISMATCH"):
            _check_observation_acceptance(path, self.calibration_path, self.code_root)

    def test_p03_calibration_drive_id_byte_mutation_refused(self):
        value = copy.deepcopy(self.acceptance)
        value["current_calibration"]["drive_id"] = "FORGED"
        path = self._write_json("p03-calibration-drive-id-mutation.json", value)
        with self.assertRaisesRegex(RuntimeError, "OBSERVATION_ACCEPTANCE_ARTIFACT_BYTES_MISMATCH"):
            _check_observation_acceptance(path, self.calibration_path, self.code_root)

    def test_p04_format_only_byte_mutation_refused(self):
        original = self.acceptance_path.read_bytes()
        mutated = original.replace(b'": ', b'" :', 1)
        self.assertEqual(len(original), len(mutated))
        self.assertNotEqual(original, mutated)
        self.assertEqual(json.loads(original.decode("utf-8-sig")), json.loads(mutated.decode("utf-8-sig")))
        path = self.root / "p04-format-only-mutation.json"
        path.write_bytes(mutated)
        with self.assertRaisesRegex(RuntimeError, "OBSERVATION_ACCEPTANCE_ARTIFACT_HASH_MISMATCH"):
            _check_observation_acceptance(path, self.calibration_path, self.code_root)


if __name__ == "__main__":
    unittest.main()
