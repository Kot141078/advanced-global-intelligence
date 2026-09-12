from __future__ import annotations

import copy
import io
import json
import subprocess
import sys
import tempfile
import threading
import time
import unittest
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "tools"))

from cgdr_r1_6b.supervisor import (
    BoundedStreamCollector,
    CleanupUnprovenError,
    StagedRuntime,
    WorkerDeadlineTimeout,
    WorkerEOFError,
    WorkerEarlyExitError,
    WorkerProcess,
    WorkerProtocolError,
    _worker_command,
    sha256_file,
    stage_worker,
)
from run_s0 import prepare_fresh_output, review_s0_files, review_s0_trace


class ControlledRaw(io.RawIOBase):
    """Finite controlled raw source whose EOF is independent from available data."""

    def __init__(self) -> None:
        super().__init__()
        self._bytes = bytearray()
        self._eof = False
        self._condition = threading.Condition()

    def readable(self) -> bool:
        return True

    def feed(self, value: bytes) -> None:
        with self._condition:
            self._bytes.extend(value)
            self._condition.notify_all()

    def finish(self) -> None:
        with self._condition:
            self._eof = True
            self._condition.notify_all()

    def readinto(self, target: bytearray) -> int:
        with self._condition:
            while not self._bytes and not self._eof and not self.closed:
                self._condition.wait(0.1)
            if not self._bytes:
                return 0
            count = min(len(target), len(self._bytes))
            target[:count] = self._bytes[:count]
            del self._bytes[:count]
            return count

    def close(self) -> None:
        with self._condition:
            self._eof = True
            self._condition.notify_all()
        super().close()


class FakeProcess:
    next_pid = 8000

    def __init__(self, stdout: io.BufferedIOBase | None, stderr: io.BufferedIOBase | None, rc: int | None = None):
        FakeProcess.next_pid += 1
        self.pid = FakeProcess.next_pid
        self._handle = 9000 + self.pid
        self.stdin = io.BytesIO()
        self.stdout = stdout
        self.stderr = stderr
        self.rc = rc
        self.kill_called = False

    def poll(self) -> int | None:
        return self.rc

    def wait(self, timeout: float | None = None) -> int:
        if self.rc is None:
            if self.kill_called:
                self.rc = -9
            else:
                raise subprocess.TimeoutExpired("TEST", timeout)
        return self.rc

    def kill(self) -> None:
        self.kill_called = True
        self.rc = -9


class ManualClock:
    def __init__(self) -> None:
        self.value = 0.0

    def __call__(self) -> float:
        self.value += 1.0
        return self.value


def runtime() -> StagedRuntime:
    return StagedRuntime(
        stage_dir="/tmp/cgdr-r1-6g-s0-test-a1",
        worker="/tmp/cgdr-r1-6g-s0-test-a1/worker.py",
        worker_sha256="a" * 64,
        launcher="/tmp/cgdr-r1-6g-s0-test-a1/s0_launcher.py",
        launcher_sha256="b" * 64,
        stage_receipt={"kind": "PROCESS_FREE_TEST_DOUBLE"},
    )


def child_binding(instance: str, receipt_nonce: str = "receipt-1") -> dict[str, object]:
    return {
        "marker": "CGDR_CHILD_BOUND",
        "binding_source": "TRUSTED_DIRECT_FORK_PARENT",
        "wait_source": "POSIX_WAITPID_CHILD",
        "instance_id": instance,
        "receipt_nonce": receipt_nonce,
        "worker_pid": 2,
        "worker_start_ticks": 4321,
        "waiter_pid": 1,
        "waiter_start_ticks": 4300,
        "pid_namespace": "pid:[101]",
        "network_namespace": "net:[202]",
        "mount_namespace": "mnt:[303]",
        "worker_sha256": "a" * 64,
        "launcher_sha256": "b" * 64,
        "receipt_channel": "PARENT_ONLY_STDERR_V1",
        "_receipt_record_type": "TRUSTED_PARENT_RECEIPT",
        "_receipt_channel": "PARENT_ONLY_STDERR_V1",
    }


def exit_receipt(binding: dict[str, object], rc: int = 0) -> dict[str, object]:
    return {**binding, "marker": "CGDR_INNER_EXIT", "return_code": rc, "signal": None}


def receipt_line(payload: dict[str, object]) -> bytes:
    clean = {key: value for key, value in payload.items() if not key.startswith("_")}
    return (json.dumps({
        "record_type": "TRUSTED_PARENT_RECEIPT",
        "receipt_channel": "PARENT_ONLY_STDERR_V1",
        "payload": clean,
    }) + "\n").encode()


def valid_trace() -> tuple[list[dict[str, object]], dict[str, object]]:
    instance = "instance-valid"
    binding = child_binding(instance)
    ping_nonce = "ping-nonce"
    ping_id = "ping-id"
    stop_id = "stop-id"
    events: list[dict[str, object]] = [
        {"local_seq": 1, "kind": "PROCESS_START_REQUESTED", "instance_id": instance},
        {"local_seq": 2, "kind": "PROCESS_HANDLE_OBTAINED", "instance_id": instance},
        {"local_seq": 3, "kind": "OS_CHILD_BOUND", "instance_id": instance, "binding": binding},
        {"local_seq": 4, "kind": "IPC_RECEIVED", "instance_id": instance, "worker_event": {
            "event": "READY", "instance_id": instance, "pid": 2, "proc_start_ticks": 4321,
            "pid_namespace": "pid:[101]", "network_namespace": "net:[202]",
        }},
        {"local_seq": 5, "kind": "IPC_SENT", "instance_id": instance, "command": "PING", "nonce": ping_nonce, "message_id": ping_id},
        {"local_seq": 6, "kind": "IPC_RECEIVED", "instance_id": instance, "worker_event": {
            "event": "PONG", "instance_id": instance, "nonce": ping_nonce, "message_id": ping_id,
        }},
        {"local_seq": 7, "kind": "IPC_SENT", "instance_id": instance, "command": "STOP", "message_id": stop_id},
        {"local_seq": 8, "kind": "IPC_RECEIVED", "instance_id": instance, "worker_event": {
            "event": "STOP_ACK", "instance_id": instance, "stop_id": stop_id,
        }},
        {"local_seq": 9, "kind": "EXIT_OBSERVED", "instance_id": instance, "return_code": 0,
         "inner_exit_receipt": exit_receipt(binding), "inner_exit_confirmed": True,
         "reader_threads_stopped": True, "cleanup_status": "PROVEN"},
    ]
    expected = {
        "instance_id": instance,
        "receipt_nonce": "receipt-1",
        "worker_sha256": "a" * 64,
        "launcher_sha256": "b" * 64,
        "ping_nonce": ping_nonce,
        "ping_message_id": ping_id,
        "stop_id": stop_id,
    }
    return events, expected


class CollectorTests(unittest.TestCase):
    def test_short_ready_is_available_before_eof_on_real_buffered_wrapper(self) -> None:
        raw = ControlledRaw()
        buffered = io.BufferedReader(raw, buffer_size=8)
        collector = BoundedStreamCollector(buffered, forward_lines=True, read_chunk_bytes=64)
        frame = b'{"event":"READY","instance_id":"i"}\n'
        raw.feed(frame)
        kind, value = collector.items.get(timeout=1)
        self.assertEqual((kind, value), ("line", frame.decode()))
        self.assertFalse(raw._eof)
        raw.finish()
        self.assertTrue(collector.join(1))

    def test_split_utf8_and_multiple_frames(self) -> None:
        raw = ControlledRaw()
        collector = BoundedStreamCollector(io.BufferedReader(raw, buffer_size=4), forward_lines=True, read_chunk_bytes=3)
        payload = '{"event":"РЕЗУЛЬТАТ"}\n{"event":"NEXT"}\n'.encode("utf-8")
        for index in range(0, len(payload), 2):
            raw.feed(payload[index:index + 2])
        raw.finish()
        self.assertTrue(collector.join(1))
        lines = []
        while not collector.items.empty():
            kind, value = collector.items.get_nowait()
            if kind == "line":
                lines.append(value)
        self.assertEqual(lines, ['{"event":"РЕЗУЛЬТАТ"}\n', '{"event":"NEXT"}\n'])
        self.assertIsNone(collector.snapshot()["reader_error"])

    def test_invalid_utf8_is_explicit_protocol_input_error(self) -> None:
        collector = BoundedStreamCollector(io.BytesIO(b"\xff\n"), forward_lines=True)
        self.assertTrue(collector.join(1))
        self.assertTrue(str(collector.snapshot()["reader_error"]).startswith("INVALID_UTF8:"))

    def test_incomplete_frame_and_bounded_overflow(self) -> None:
        incomplete = BoundedStreamCollector(io.BytesIO(b'{"event":"READY"'), forward_lines=True)
        self.assertTrue(incomplete.join(1))
        self.assertTrue(incomplete.snapshot()["incomplete_frame"])
        overflow = BoundedStreamCollector(
            io.BytesIO((b"x" * 100) + b"\n" + (b"{}\n" * 20)),
            forward_lines=True,
            max_chars=16,
            max_frame_chars=32,
            queue_limit=2,
            read_chunk_bytes=8,
        )
        self.assertTrue(overflow.join(1))
        snap = overflow.snapshot()
        self.assertEqual(snap["captured_chars"], 16)
        self.assertIn(snap["overflow"], {"FRAME_SIZE_LIMIT", "FRAME_QUEUE_LIMIT"})
        self.assertLessEqual(overflow.items.qsize(), 2)

    def test_reader_shutdown_unblocks_controlled_stream(self) -> None:
        raw = ControlledRaw()
        collector = BoundedStreamCollector(raw, forward_lines=True)
        self.assertTrue(collector.close_and_join(1))
        self.assertFalse(collector.thread.is_alive())

    def test_worker_marker_shaped_payload_is_not_a_trusted_receipt(self) -> None:
        spoof = json.dumps({"marker": "CGDR_INNER_EXIT", "instance_id": "spoof"}).encode() + b"\n"
        wrapped = json.dumps({"record_type": "WORKER_STDERR_DATA", "source_channel": "DEDICATED_CHILD_STDERR_PIPE", "payload_b64": "e30=", "truncated": False}).encode() + b"\n"
        collector = BoundedStreamCollector(io.BytesIO(spoof + wrapped), forward_lines=False, trusted_markers_only=True)
        self.assertTrue(collector.join(1))
        self.assertEqual(collector.markers, [])
        self.assertEqual(len(collector.worker_diagnostics), 1)


class OwnershipAndClassificationTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)

    def tearDown(self) -> None:
        self.temp.cleanup()

    def make_worker(self, **kwargs: object) -> WorkerProcess:
        return WorkerProcess("TEST", runtime(), self.root / "events.jsonl", "S0", "TEST", receipt_nonce="receipt-1", **kwargs)

    def test_eof_and_early_exit_are_distinct(self) -> None:
        worker = self.make_worker()
        worker.process = FakeProcess(io.BytesIO(b""), io.BytesIO(b""), rc=None)
        worker._attach_process()
        with self.assertRaises(WorkerEOFError):
            worker.read_event(0.5)
        worker2 = WorkerProcess("TEST", runtime(), self.root / "events2.jsonl", "S0", "TEST", receipt_nonce="receipt-1")
        worker2.process = FakeProcess(io.BytesIO(b""), io.BytesIO(b""), rc=7)
        worker2._attach_process()
        with self.assertRaises(WorkerEarlyExitError):
            worker2.read_event(0.5)

    def test_monotonic_deadline_classification(self) -> None:
        raw = ControlledRaw()
        worker = self.make_worker(clock=ManualClock())
        worker.process = FakeProcess(raw, io.BytesIO(b""), rc=None)
        worker._attach_process()
        with self.assertRaises(WorkerDeadlineTimeout):
            worker.read_event(0.5)
        raw.finish()

    def test_start_exception_keeps_unproven_ownership(self) -> None:
        def explode(*args: object, **kwargs: object) -> object:
            raise OSError("synthetic constructor failure")

        worker = self.make_worker(popen_factory=explode)
        with self.assertRaises(CleanupUnprovenError):
            worker.start(0.1)
        self.assertTrue(worker.outcome.start_request_issued)
        self.assertFalse(worker.outcome.process_handle_obtained)
        self.assertEqual(worker.cleanup_status, "UNPROVEN")

    def test_failure_after_handle_return_invokes_bounded_cleanup(self) -> None:
        process = FakeProcess(None, None, rc=3)
        worker = self.make_worker(popen_factory=lambda *a, **k: process)
        with self.assertRaises(CleanupUnprovenError):
            worker.start(0.1)
        self.assertTrue(worker.outcome.process_handle_obtained)
        self.assertEqual(worker.outcome.failure_classification, "PROTOCOL_ERROR")
        self.assertEqual(worker.cleanup_status, "UNPROVEN")

    def test_direct_wait_receipt_proves_exit_without_ready(self) -> None:
        worker = self.make_worker()
        binding = child_binding(worker.instance_id)
        receipt = receipt_line(exit_receipt(binding))
        worker.outcome.start_request_issued = True
        worker.process = FakeProcess(io.BytesIO(b""), io.BytesIO(receipt), rc=0)
        worker._attach_process()
        worker.child_binding = binding
        worker.outcome.child_binding_obtained = True
        worker.outcome.worker_pid = 2
        worker.outcome.worker_start_ticks = 4321
        self.assertEqual(worker._cleanup_owned(reason="TEST_NO_READY"), "PROVEN")
        self.assertFalse(worker.outcome.ready_observed)

    def test_wrapper_exit_or_stop_ack_without_wait_is_unproven(self) -> None:
        worker = self.make_worker()
        worker.outcome.start_request_issued = True
        worker.process = FakeProcess(io.BytesIO(b'{"event":"STOP_ACK"}\n'), io.BytesIO(b""), rc=0)
        worker._attach_process()
        self.assertEqual(worker._cleanup_owned(reason="WRAPPER_ONLY"), "UNPROVEN")


class LauncherTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)

    def tearDown(self) -> None:
        self.temp.cleanup()

    def test_direct_argv_preserves_literal_parameters_without_shell(self) -> None:
        rt = runtime()
        command, config = _worker_command("Ubuntu", rt, "instance-$(not-executed)", "nonce;still-data")
        self.assertNotIn("sh", command)
        self.assertNotIn("-c", command)
        self.assertEqual(command[-1], "nonce;still-data")
        self.assertIn("instance-$(not-executed)", command)
        self.assertTrue(any("no shell" in item for item in config))

    def test_stage_worker_uses_direct_argv_and_exact_receipt(self) -> None:
        worker = ROOT / "src" / "cgdr_r1_6b" / "worker.py"
        launcher = ROOT / "src" / "cgdr_r1_6b" / "s0_launcher.py"
        stage_dir = "/tmp/cgdr-r1-6g-s0-test-stage"
        captured: dict[str, object] = {}

        def completed(command: list[str], **kwargs: object) -> subprocess.CompletedProcess[str]:
            captured["command"] = command
            captured["kwargs"] = kwargs
            receipt = {
                "kind": "S0_STAGE_RECEIPT",
                "stage_dir": stage_dir,
                "worker": stage_dir + "/worker.py",
                "worker_sha256": sha256_file(worker),
                "launcher": stage_dir + "/s0_launcher.py",
                "launcher_sha256": sha256_file(launcher),
                "collision_policy": "O_EXCL_NO_OVERWRITE",
            }
            return subprocess.CompletedProcess(command, 0, json.dumps(receipt), "")

        with mock.patch("cgdr_r1_6b.supervisor.subprocess.run", side_effect=completed):
            staged = stage_worker("Ubuntu", worker, stage_dir, self.root / "setup.jsonl", local_launcher=launcher)
        command = captured["command"]
        self.assertIsInstance(command, list)
        self.assertNotIn("sh", command)
        self.assertNotIn("-c", command)
        self.assertFalse(captured["kwargs"].get("shell", False))
        self.assertEqual(staged.stage_receipt["collision_policy"], "O_EXCL_NO_OVERWRITE")

    def test_output_collision_is_fail_closed(self) -> None:
        target = self.root / "output"
        target.mkdir()
        with self.assertRaises(FileExistsError):
            prepare_fresh_output(target)
        fresh = prepare_fresh_output(self.root / "fresh")
        self.assertTrue(fresh.is_dir())


class IndependentReviewerTests(unittest.TestCase):
    def test_valid_trace_passes(self) -> None:
        events, expected = valid_trace()
        result = review_s0_trace(events, expected)
        self.assertEqual(result["verdict"], "PASS", result)

    def test_reviewer_reads_persisted_intent_and_raw_events(self) -> None:
        events, expected = valid_trace()
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "events.jsonl").write_text(
                "".join(json.dumps(event, sort_keys=True) + "\n" for event in events), encoding="utf-8"
            )
            (root / "intent.json").write_text(json.dumps(expected, sort_keys=True), encoding="utf-8")
            result = review_s0_files(root / "events.jsonl", root / "intent.json")
        self.assertEqual(result["verdict"], "PASS", result)

    def test_missing_wait_ack_without_exit_and_unfinished_readers_are_not_pass(self) -> None:
        events, expected = valid_trace()
        self.assertEqual(review_s0_trace(events[:-1], expected)["verdict"], "INCONCLUSIVE")
        changed = copy.deepcopy(events)
        changed[-1]["reader_threads_stopped"] = False
        self.assertEqual(review_s0_trace(changed, expected)["verdict"], "INCONCLUSIVE")

    def test_wrong_child_stale_start_and_replayed_receipt_nonce_fail(self) -> None:
        events, expected = valid_trace()
        for mutator in ("child", "start", "nonce"):
            changed = copy.deepcopy(events)
            binding = changed[2]["binding"]
            if mutator == "child":
                binding["worker_pid"] = 99
            elif mutator == "start":
                binding["worker_start_ticks"] = 9999
            else:
                binding["receipt_nonce"] = "replayed-old-nonce"
            with self.subTest(mutator=mutator):
                result = review_s0_trace(changed, expected)
                self.assertEqual(result["verdict"], "FAIL", result)

    def test_wrong_ping_nonce_and_duplicate_sequence_fail(self) -> None:
        events, expected = valid_trace()
        changed = copy.deepcopy(events)
        changed[5]["worker_event"]["nonce"] = "wrong"
        self.assertEqual(review_s0_trace(changed, expected)["verdict"], "FAIL")
        changed = copy.deepcopy(events)
        changed[-1]["local_seq"] = 8
        self.assertEqual(review_s0_trace(changed, expected)["verdict"], "FAIL")

    def test_wrong_wait_source_and_missing_rc_fail(self) -> None:
        events, expected = valid_trace()
        changed = copy.deepcopy(events)
        changed[-1]["inner_exit_receipt"]["wait_source"] = "WRAPPER_ONLY"
        self.assertEqual(review_s0_trace(changed, expected)["verdict"], "FAIL")
        changed = copy.deepcopy(events)
        changed[-1]["inner_exit_receipt"].pop("return_code")
        self.assertEqual(review_s0_trace(changed, expected)["verdict"], "FAIL")


if __name__ == "__main__":
    unittest.main(verbosity=2)
