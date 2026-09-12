"""R1.6AK: receipt CLI domain only; no process or protocol execution."""
from __future__ import annotations

import ast
import contextlib
import hashlib
import io
import json
import os
import re
import tempfile
import unittest
from pathlib import Path
from unittest.mock import Mock, patch

from cgdr_r1_6b import s0_launcher, supervisor
import run_s1

CANDIDATE = Path(__file__).resolve().parents[1]
INPUT = Path(os.environ.get("CGDR_AK_INPUT", str(CANDIDATE.parent / "input")))
HEX = "0123456789abcdef" * 4
ERROR = "receipt nonce must be a non-empty CLI-safe token"


def runtime(mode="S0"):
    return supervisor.StagedRuntime(
        stage_dir="/tmp/offline-receipt-fixture",
        worker="/tmp/offline-receipt-fixture/worker.py",
        worker_sha256="a" * 64,
        launcher="/tmp/offline-receipt-fixture/s0_launcher.py",
        launcher_sha256="b" * 64,
        stage_receipt={}, mode=mode,
        s1_plan="/tmp/offline/plan.json", s1_plan_sha256="c" * 64,
        s1_fixture_manifest="/tmp/offline/fixtures.json",
        s1_fixture_manifest_sha256="d" * 64, s1_attempt_id="offline-s1",
        helper_dir="/tmp/offline/helper", helper="/tmp/offline/helper/helper.py",
        helper_sha256="e" * 64,
        s2_plan="/tmp/offline/s2.json", s2_plan_sha256="f" * 64,
        s2_fixture_manifest="/tmp/offline/s2-fixtures.json",
        s2_fixture_manifest_sha256="a" * 64, s2_attempt_id="offline-s2",
        s2_worker_role="bounded-worker",
    )


def parser_argv(command, subcommand="wait"):
    return command[command.index(subcommand):]


class ReceiptNonceCliSafetyR16AKTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="ak-nonce-offline-")
        self.addCleanup(self.temp.cleanup)
        self.event_log = Path(self.temp.name) / "never-created-lifecycle.jsonl"
        self.factory = Mock(side_effect=AssertionError("process creation forbidden"))

    def tearDown(self):
        self.factory.assert_not_called()
        self.assertFalse(self.event_log.exists())

    def worker(self, mode="S0", **kwargs):
        value = supervisor.WorkerProcess(
            "Ubuntu", runtime(mode), self.event_log, "OFFLINE", "W0",
            popen_factory=self.factory, **kwargs,
        )
        self.assertIsNone(value.process)
        self.assertIs(value.outcome.start_request_issued, False)
        return value

    def helper(self):
        with patch.object(run_s1.subprocess, "Popen", self.factory):
            value = run_s1.EndpointHelperProcess(
                "Ubuntu", runtime("S1"), 12345, self.event_log)
        self.assertIsNone(value.process)
        self.assertEqual(value.cleanup_status, "NOT_STARTED")
        return value

    def test_ak01_exact_predecessor_separate_hyphen_parser_failure(self):
        lines = (INPUT / "aj_evidence/sentinel_output/episodes/07_T3/lifecycle.jsonl").read_text().splitlines()
        start = next(r for r in map(json.loads, lines)
                     if r.get("kind") == "PROCESS_START_REQUESTED" and r.get("label") == "W1")
        args = parser_argv(start["argv"])
        nonce = args[args.index("--receipt-nonce") + 1]
        self.assertTrue(nonce.startswith("-"))
        stderr = io.StringIO()
        with contextlib.redirect_stderr(stderr), self.assertRaises(SystemExit) as caught:
            s0_launcher.build_parser().parse_args(args)
        self.assertEqual(caught.exception.code, 2)
        self.assertIn("argument --receipt-nonce: expected one argument", stderr.getvalue())

    def test_ak02_worker_uses_32_random_bytes_hex(self):
        with patch.object(supervisor.secrets, "token_hex", return_value=HEX) as generate:
            value = self.worker()
        generate.assert_called_once_with(32)
        self.assertEqual(value.receipt_nonce, HEX)

    def test_ak03_worker_generated_domain_is_64_lowercase_hex(self):
        nonce = self.worker().receipt_nonce
        self.assertEqual(len(nonce), 64)
        self.assertIsNotNone(re.fullmatch("[0-9a-f]{64}", nonce))

    def test_ak04_generated_worker_command_parses_exact_launcher(self):
        value = self.worker()
        parsed = s0_launcher.build_parser().parse_args(parser_argv(value.command))
        self.assertEqual(parsed.receipt_nonce, value.receipt_nonce)
        self.assertEqual(parsed.instance_id, value.instance_id)
        self.assertEqual(parsed.worker_sha256, value.runtime.worker_sha256)

    def test_ak05_unsafe_explicit_value_rejected_before_process(self):
        for nonce in ("-leading-hyphen", "--receipt-nonce", 42, ["unsafe"]):
            with self.subTest(nonce=nonce):
                with self.assertRaises(ValueError) as caught:
                    self.worker(receipt_nonce=nonce)
                self.assertEqual(str(caught.exception), ERROR)
        self.factory.assert_not_called()

    def test_ak06_safe_explicit_value_preserved_separately(self):
        nonce = "safe_exact_A-Z_0123"
        with patch.object(supervisor.secrets, "token_hex") as generate:
            value = self.worker(receipt_nonce=nonce)
        generate.assert_not_called()
        i = value.command.index("--receipt-nonce")
        self.assertEqual(value.command[i:i + 2], ["--receipt-nonce", nonce])
        self.assertEqual(value.receipt_nonce, nonce)

    def test_ak07_metacharacters_remain_literal_direct_argv_data(self):
        nonce = "literal; & $(never-execute) | > file"
        value = self.worker(receipt_nonce=nonce)
        self.assertIs(type(value.command), list)
        self.assertEqual(value.command[:4], ["wsl.exe", "-d", "Ubuntu", "--"])
        self.assertEqual(value.command[value.command.index("--receipt-nonce") + 1], nonce)
        parsed = s0_launcher.build_parser().parse_args(parser_argv(value.command))
        self.assertEqual(parsed.receipt_nonce, nonce)
        self.assertFalse(any(s in value.command for s in ("sh", "bash", "cmd", "/bin/sh")))
        self.factory.assert_not_called()

    def test_ak08_worker_receipt_does_not_call_token_urlsafe(self):
        with patch.object(supervisor.secrets, "token_urlsafe",
                          side_effect=AssertionError("wrong nonce domain")) as old:
            nonce = self.worker().receipt_nonce
        old.assert_not_called()
        self.assertEqual(len(nonce), 64)

    def test_ak09_helper_uses_32_random_bytes_hex(self):
        with patch.object(run_s1.secrets, "token_hex", return_value=HEX) as generate:
            value = self.helper()
        generate.assert_called_once_with(32)
        self.assertEqual(value.receipt_nonce, HEX)

    def test_ak10_helper_generated_domain_is_64_lowercase_hex(self):
        nonce = self.helper().receipt_nonce
        self.assertEqual(len(nonce), 64)
        self.assertIsNotNone(re.fullmatch("[0-9a-f]{64}", nonce))

    def test_ak11_helper_command_parses_exact_wait_helper(self):
        value = self.helper()
        parsed = s0_launcher.build_parser().parse_args(parser_argv(value.command, "wait-helper"))
        self.assertEqual(parsed.receipt_nonce, value.receipt_nonce)
        self.assertEqual(parsed.instance_id, value.instance_id)
        self.assertEqual(parsed.tcp_port, 12345)
        i = value.command.index("--receipt-nonce")
        self.assertEqual(value.command[i:i + 2], ["--receipt-nonce", value.receipt_nonce])

    def test_ak12_helper_receipt_does_not_call_token_urlsafe(self):
        with patch.object(run_s1.secrets, "token_urlsafe",
                          side_effect=AssertionError("wrong nonce domain")) as old:
            nonce = self.helper().receipt_nonce
        old.assert_not_called()
        self.assertEqual(len(nonce), 64)

    def test_ak13_json_ipc_ping_nonce_expression_unchanged(self):
        def ping_assignments(path):
            tree = ast.parse(path.read_text())
            return [ast.dump(n, include_attributes=False) for n in ast.walk(tree)
                    if isinstance(n, ast.Assign) and any(isinstance(t, ast.Name)
                    and t.id == "ping_nonce" for t in n.targets)]
        current = ping_assignments(CANDIDATE / "tools/run_s1.py")
        self.assertEqual(current, ping_assignments(INPUT / "code/tools/run_s1.py"))
        self.assertEqual(len(current), 1)
        self.assertIn("attr='token_urlsafe'", current[0])
        self.assertIn("Constant(value=32)", current[0])

    def test_ak14_s0_s1_s2_safe_receipt_pair(self):
        for mode in ("S0", "S1", "S2"):
            with self.subTest(mode=mode):
                value = self.worker(mode)
                args = parser_argv(value.command)
                parsed = s0_launcher.build_parser().parse_args(args)
                i = args.index("--receipt-nonce")
                self.assertEqual(args[i:i + 2], ["--receipt-nonce", value.receipt_nonce])
                self.assertEqual(parsed.receipt_nonce, value.receipt_nonce)
                self.assertEqual(parsed.s1_mode, mode == "S1")
                self.assertEqual(parsed.s2_mode, mode == "S2")

    def test_ak15_exact_launcher_required_receipt_contract(self):
        launcher = CANDIDATE / "src/cgdr_r1_6b/s0_launcher.py"
        self.assertEqual(hashlib.sha256(launcher.read_bytes()).hexdigest(),
                         "d9d255066f6267120088f6f396f914d6c8d1bc1e1077fc5947b7a4200b80592f")
        for command, subcommand in ((self.worker().command, "wait"),
                                    (self.helper().command, "wait-helper")):
            with self.subTest(subcommand=subcommand):
                args = parser_argv(command, subcommand)
                i = args.index("--receipt-nonce")
                del args[i:i + 2]
                stderr = io.StringIO()
                with contextlib.redirect_stderr(stderr), self.assertRaises(SystemExit) as caught:
                    s0_launcher.build_parser().parse_args(args)
                self.assertEqual(caught.exception.code, 2)
                self.assertIn("required: --receipt-nonce", stderr.getvalue())

    def test_ak16_cleanup_without_bound_inner_exit_remains_unproven(self):
        value = self.worker()
        value.outcome.start_request_issued = True  # Synthetic ownership state; start() is never called.
        fake_process = Mock()
        fake_process.poll.return_value = 2
        fake_process.stdin = None
        value.process = fake_process
        with patch.object(value, "_finish_collectors", return_value=True), \
                patch.object(value, "_find_marker", return_value=None), \
                patch.object(value, "_event"):
            result = value._cleanup_owned(reason="OFFLINE_RECEIPT_CONTROL")
        self.assertEqual(result, "UNPROVEN")
        self.assertIs(value._inner_exit_valid(2), False)
        self.assertIsNone(value.child_binding)
        self.assertIsNone(value.inner_exit)
        fake_process.wait.assert_not_called()
        fake_process.kill.assert_not_called()

    def test_ak17_all_90_protected_current_ai_files_unchanged(self):
        manifest = json.loads((INPUT / "MANIFEST_CURRENT_AI.json").read_text())
        changed = {"src/cgdr_r1_6b/supervisor.py", "tools/run_s1.py"}
        protected = [r for r in manifest["files"] if r["path"] not in changed]
        self.assertEqual(len(protected), 90)
        for row in protected:
            with self.subTest(path=row["path"]):
                data = (CANDIDATE / row["path"]).read_bytes()
                self.assertEqual(len(data), row["bytes"])
                self.assertEqual(hashlib.sha256(data).hexdigest(), row["sha256"])


if __name__ == "__main__":
    unittest.main()

