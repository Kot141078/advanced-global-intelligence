from __future__ import annotations

import argparse
import hashlib
import json
import os
import queue
import secrets
import subprocess
import sys
import time
import uuid
from dataclasses import asdict
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from cgdr_r1_6b.common import write_json
from cgdr_r1_6b.s1_review import review_s1_evidence
from cgdr_r1_6b.supervisor import (
    BoundedStreamCollector,
    CleanupUnprovenError,
    StagedRuntime,
    WorkerProcess,
    sha256_file,
    stage_s1_runtime,
    utc_now,
)

TASK_ID = "CGDR_SELECTED_PROCESS_ACCESS_BOUNDARY_S1_R1_6H"
MAX_FRAME_BYTES = 32 * 1024


def _read_events(path: Path) -> list[dict[str, Any]]:
    if not path.is_file():
        return []
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def _append_jsonl(path: Path, value: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8", newline="\n") as stream:
        stream.write(json.dumps(value, sort_keys=True) + "\n")


def _host_env() -> dict[str, str]:
    return {key: os.environ[key] for key in ("SystemRoot", "WINDIR", "PATH") if key in os.environ}


class EndpointHelperProcess:
    """One owned trusted helper tree with parent-only receipt provenance."""

    def __init__(self, distro: str, runtime: StagedRuntime, tcp_port: int, event_log: Path):
        if runtime.mode != "S1" or not runtime.helper or not runtime.helper_sha256 or not runtime.helper_dir:
            raise ValueError("helper requires a complete S1 staged runtime")
        self.instance_id = str(uuid.uuid4())
        self.receipt_nonce = secrets.token_hex(32)
        self.event_log = event_log
        self.command = [
            "wsl.exe", "-d", distro, "--", "/usr/bin/python3", runtime.launcher, "wait-helper",
            "--helper-dir", runtime.helper_dir,
            "--helper", runtime.helper,
            "--helper-sha256", runtime.helper_sha256,
            "--tcp-port", str(tcp_port),
            "--instance-id", self.instance_id,
            "--receipt-nonce", self.receipt_nonce,
        ]
        self.process: Any | None = None
        self.stdout: BoundedStreamCollector | None = None
        self.stderr: BoundedStreamCollector | None = None
        self.binding: dict[str, Any] | None = None
        self.ready: dict[str, Any] | None = None
        self.post_control: dict[str, Any] | None = None
        self.exit_receipt: dict[str, Any] | None = None
        self.cleanup_status = "NOT_STARTED"
        self._seq = 0

    def _event(self, value: dict[str, Any]) -> None:
        self._seq += 1
        _append_jsonl(self.event_log, {"local_seq": self._seq, **value})

    def _read(self, timeout: float) -> dict[str, Any]:
        if self.stdout is None:
            raise RuntimeError("helper stdout unavailable")
        deadline = time.perf_counter() + timeout
        while True:
            if self.stdout.overflow or self.stdout.error:
                raise RuntimeError(f"helper stdout collector failure:{self.stdout.overflow or self.stdout.error}")
            remaining = deadline - time.perf_counter()
            if remaining <= 0:
                raise TimeoutError("helper protocol deadline")
            try:
                kind, payload = self.stdout.items.get(timeout=min(remaining, 0.05))
            except queue.Empty:
                continue
            if kind != "line" or not isinstance(payload, str):
                raise RuntimeError(f"helper protocol terminated:{kind}:{payload}")
            value = json.loads(payload)
            if not isinstance(value, dict) or not isinstance(value.get("event"), str):
                raise RuntimeError("helper frame is not an event object")
            self._event({"kind": "HELPER_IPC_RECEIVED", "instance_id": self.instance_id, "helper_event": value, "host_utc": utc_now(), "host_perf_counter_ns": time.perf_counter_ns()})
            return value

    def _send(self, value: dict[str, Any]) -> None:
        if self.process is None or self.process.poll() is not None or self.process.stdin is None:
            raise RuntimeError("helper exited before send")
        encoded = (json.dumps(value, sort_keys=True, separators=(",", ":")) + "\n").encode()
        if len(encoded) > MAX_FRAME_BYTES:
            raise RuntimeError("helper outbound frame overflow")
        self.process.stdin.write(encoded)
        self.process.stdin.flush()
        self._event({"kind": "HELPER_IPC_SENT", "instance_id": self.instance_id, "command": value.get("command"), "message_id": value.get("message_id") or value.get("stop_id"), "host_utc": utc_now(), "host_perf_counter_ns": time.perf_counter_ns()})

    def _find_marker(self, name: str) -> dict[str, Any] | None:
        if self.stderr is None:
            return None
        return next((value for value in self.stderr.markers if value.get("marker") == name and value.get("instance_id") == self.instance_id), None)

    def start(self, timeout: float = 10.0) -> dict[str, Any]:
        self._event({"kind": "HELPER_START_REQUESTED", "instance_id": self.instance_id, "argv": self.command, "receipt_nonce_sha256": hashlib.sha256(self.receipt_nonce.encode()).hexdigest(), "host_utc": utc_now(), "host_perf_counter_ns": time.perf_counter_ns()})
        self.process = subprocess.Popen(self.command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=False, bufsize=0, env=_host_env())
        if self.process.stdout is None or self.process.stderr is None:
            raise RuntimeError("helper wrapper lacks pipes")
        self.stdout = BoundedStreamCollector(self.process.stdout, forward_lines=True)
        self.stderr = BoundedStreamCollector(self.process.stderr, forward_lines=False, trusted_markers_only=True)
        deadline = time.perf_counter() + timeout
        while time.perf_counter() < deadline:
            marker = self._find_marker("CGDR_HELPER_BOUND")
            if marker is not None:
                self.binding = marker
                break
            if self.process.poll() is not None:
                raise RuntimeError(f"helper wrapper exited before binding rc={self.process.poll()}")
            time.sleep(0.01)
        if self.binding is None:
            raise TimeoutError("trusted helper binding deadline")
        for field, wanted in {
            "binding_source": "TRUSTED_DIRECT_FORK_PARENT",
            "wait_source": "POSIX_WAITPID_CHILD",
            "receipt_channel": "PARENT_ONLY_STDERR_V1",
            "instance_id": self.instance_id,
            "receipt_nonce": self.receipt_nonce,
        }.items():
            if self.binding.get(field) != wanted:
                raise RuntimeError(f"helper binding mismatch:{field}")
        self._event({"kind": "HELPER_OS_CHILD_BOUND", "instance_id": self.instance_id, "binding": self.binding, "host_utc": utc_now(), "host_perf_counter_ns": time.perf_counter_ns()})
        ready = self._read(max(0.01, deadline - time.perf_counter()))
        if ready.get("event") != "HELPER_READY" or ready.get("instance_id") != self.instance_id or ready.get("pid") != self.binding.get("helper_pid") or ready.get("proc_start_ticks") != self.binding.get("helper_start_ticks"):
            raise RuntimeError("helper READY binding mismatch")
        self.ready = ready
        return ready

    def post_and_stop(self) -> None:
        post_id = f"s1-helper-post-{uuid.uuid4()}"
        self._send({"command": "POST_CONTROL", "message_id": post_id})
        post = self._read(10)
        if post.get("event") != "HELPER_POST_CONTROL" or post.get("message_id") != post_id or post.get("instance_id") != self.instance_id:
            raise RuntimeError("helper post-control response mismatch")
        self.post_control = post
        stop_id = f"s1-helper-stop-{uuid.uuid4()}"
        self._send({"command": "STOP", "stop_id": stop_id})
        ack = self._read(10)
        if ack.get("event") != "HELPER_STOP_ACK" or ack.get("stop_id") != stop_id:
            raise RuntimeError("helper STOP_ACK mismatch")
        if self.process is None:
            raise RuntimeError("helper wrapper handle unavailable")
        rc = self.process.wait(timeout=10)
        stdout_stopped = self.stdout is not None and (self.stdout.join(2) or self.stdout.close_and_join(2))
        stderr_stopped = self.stderr is not None and (self.stderr.join(2) or self.stderr.close_and_join(2))
        self.exit_receipt = self._find_marker("CGDR_HELPER_EXIT")
        exact = self.binding is not None and self.exit_receipt is not None and all(
            self.exit_receipt.get(field) == self.binding.get(field)
            for field in ("instance_id", "receipt_nonce", "helper_pid", "helper_start_ticks", "waiter_pid", "waiter_start_ticks", "pid_namespace", "network_namespace", "mount_namespace", "helper_sha256")
        )
        self.cleanup_status = "PROVEN" if rc == 0 and stdout_stopped and stderr_stopped and exact and self.exit_receipt.get("return_code") == 0 else "UNPROVEN"
        self._event({"kind": "HELPER_EXIT_OBSERVED", "instance_id": self.instance_id, "return_code": rc, "exit_receipt": self.exit_receipt, "reader_threads_stopped": bool(stdout_stopped and stderr_stopped), "cleanup_status": self.cleanup_status, "host_utc": utc_now(), "host_perf_counter_ns": time.perf_counter_ns()})
        if self.cleanup_status != "PROVEN":
            raise CleanupUnprovenError("endpoint helper cleanup unproven")

    def abort(self) -> None:
        if self.process is None:
            self.cleanup_status = "NOT_STARTED"
            return
        try:
            if self.process.poll() is None:
                self._send({"command": "STOP", "stop_id": f"s1-helper-abort-{uuid.uuid4()}"})
                try:
                    self._read(3)
                except BaseException:
                    pass
                self.process.wait(timeout=5)
        except BaseException:
            self.cleanup_status = "UNPROVEN"
            return
        stdout_stopped = self.stdout is not None and (self.stdout.join(1) or self.stdout.close_and_join(1))
        stderr_stopped = self.stderr is not None and (self.stderr.join(1) or self.stderr.close_and_join(1))
        self.exit_receipt = self._find_marker("CGDR_HELPER_EXIT")
        self.cleanup_status = "PROVEN" if self.process.poll() is not None and stdout_stopped and stderr_stopped and self.exit_receipt is not None else "UNPROVEN"

    def evidence(self) -> dict[str, Any]:
        return {
            "instance_id": self.instance_id,
            "binding": self.binding,
            "ready": self.ready,
            "post_control": self.post_control,
            "exit_receipt": self.exit_receipt,
            "cleanup_status": self.cleanup_status,
            "argv": self.command,
            "return_code": None if self.process is None else self.process.poll(),
            "stdout": None if self.stdout is None else self.stdout.snapshot(),
            "stderr": None if self.stderr is None else self.stderr.snapshot(),
        }


def _snapshot(distro: str, runtime: StagedRuntime, attempt_id: str, output: Path, phase: str, setup_log: Path, include_helper_log: bool = False) -> dict[str, Any]:
    command = [
        "wsl.exe", "-d", distro, "--", "/usr/bin/python3", runtime.launcher, "snapshot-s1",
        "--stage-dir", runtime.stage_dir,
        "--helper-dir", str(runtime.helper_dir),
        "--attempt-id", attempt_id,
        "--plan", str(runtime.s1_plan),
        "--plan-sha256", str(runtime.s1_plan_sha256),
    ]
    if include_helper_log:
        command.append("--include-helper-log")
    started = time.perf_counter_ns()
    completed = subprocess.run(command, stdin=subprocess.DEVNULL, capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=10, check=False, env=_host_env())
    record = {"kind": f"WSL_S1_{phase}_TRUSTED_SNAPSHOT", "argv": command, "return_code": completed.returncode, "stdout": completed.stdout[:65536], "stderr": completed.stderr[:16384], "start_ns": started, "end_ns": time.perf_counter_ns(), "clock_domain": "HOST_PERF_COUNTER_NS"}
    _append_jsonl(setup_log, record)
    if completed.returncode:
        raise RuntimeError(f"S1 {phase} snapshot failed rc={completed.returncode}:{completed.stderr[:1000]}")
    value = json.loads(completed.stdout)
    write_json(output / f"S1_{phase}_SNAPSHOT.json", value)
    return value


def main() -> int:
    parser = argparse.ArgumentParser(description="One bounded R1.6H S1 access-boundary attempt; never runs S2 or matrix.")
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--worker", type=Path, required=True)
    parser.add_argument("--plan", type=Path, required=True)
    parser.add_argument("--fixture-manifest", type=Path, required=True)
    parser.add_argument("--fixture-root", type=Path, required=True)
    parser.add_argument("--helper", type=Path, required=True)
    parser.add_argument("--stage-dir", required=True)
    parser.add_argument("--helper-dir", required=True)
    parser.add_argument("--distro", default="Ubuntu")
    args = parser.parse_args()
    output = args.output.resolve()
    if output.exists():
        raise SystemExit(f"S1 output collision: {output}")
    output.mkdir(parents=True)
    plan_raw = args.plan.resolve().read_bytes()
    plan = json.loads(plan_raw)
    fixture_manifest_raw = args.fixture_manifest.resolve().read_bytes()
    fixture_manifest = json.loads(fixture_manifest_raw)
    fixture_manifest_sha = hashlib.sha256(fixture_manifest_raw).hexdigest()
    plan_file_sha = hashlib.sha256(plan_raw).hexdigest()
    plan_canonical_sha = hashlib.sha256(json.dumps(plan, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
    attempt_id = plan.get("attempt_id")
    endpoint = plan.get("endpoint_binding") or {}
    if plan.get("task_id") != TASK_ID or plan.get("stage_dir") != args.stage_dir or endpoint.get("helper_dir") != args.helper_dir:
        raise SystemExit("S1 runner/plan task path binding mismatch")
    setup_log = output / "setup_commands.jsonl"
    report: dict[str, Any] = {
        "task_id": TASK_ID,
        "stage": "S1",
        "status": "INCONCLUSIVE",
        "worker_start_requests": 0,
        "endpoint_helper_starts": 0,
        "cleanup_status": "NOT_STARTED",
        "measured_matrix_started": False,
        "s2_started": False,
        "external_calls": 0,
        "model_calls": 0,
    }
    staged: StagedRuntime | None = None
    worker: WorkerProcess | None = None
    helper: EndpointHelperProcess | None = None
    pre_snapshot: dict[str, Any] = {}
    post_snapshot: dict[str, Any] = {}
    producer_exception: str | None = None
    expected: dict[str, Any] = {}
    try:
        staged = stage_s1_runtime(
            args.distro, args.worker, args.stage_dir, args.helper_dir, attempt_id,
            args.plan, args.fixture_manifest, args.fixture_root, args.helper, setup_log,
        )
        pre_snapshot = _snapshot(args.distro, staged, attempt_id, output, "PRE", setup_log)
        helper = EndpointHelperProcess(args.distro, staged, int(endpoint["tcp_port"]), output / "helper_host_events.jsonl")
        worker = WorkerProcess(args.distro, staged, output / "worker_events.jsonl", "S1", "ACCESS_BOUNDARY")
        ping_nonce = secrets.token_urlsafe(32)
        ping_message_id = f"s1-ping-{uuid.uuid4()}"
        s1_message_id = f"s1-run-{uuid.uuid4()}"
        stop_id = f"s1-stop-{uuid.uuid4()}"
        expected = {
            "task_id": TASK_ID,
            "attempt_id": attempt_id,
            "plan_file_sha256": plan_file_sha,
            "fixture_manifest_sha256": fixture_manifest_sha,
            "instance_id": worker.instance_id,
            "receipt_nonce": worker.receipt_nonce,
            "worker_sha256": staged.worker_sha256,
            "launcher_sha256": staged.launcher_sha256,
            "helper_instance_id": helper.instance_id,
            "helper_receipt_nonce": helper.receipt_nonce,
            "helper_sha256": staged.helper_sha256,
            "ping_nonce": ping_nonce,
            "ping_message_id": ping_message_id,
            "s1_message_id": s1_message_id,
            "stop_id": stop_id,
            "fixed_before_helper_or_worker_start": True,
        }
        write_json(output / "review_intent.json", {**expected, "receipt_nonce_sha256": hashlib.sha256(worker.receipt_nonce.encode()).hexdigest(), "helper_receipt_nonce_sha256": hashlib.sha256(helper.receipt_nonce.encode()).hexdigest(), "ping_nonce_sha256": hashlib.sha256(ping_nonce.encode()).hexdigest()})
        report["endpoint_helper_starts"] = 1
        helper_ready = helper.start(10)
        report["worker_start_requests"] = 1
        ready = worker.start(10)
        worker.send({"command": "PING", "nonce": ping_nonce, "message_id": ping_message_id})
        pong = worker.read_event(10)
        if pong != {"event": "PONG", "instance_id": worker.instance_id, "nonce": ping_nonce, "message_id": ping_message_id}:
            raise RuntimeError(f"S1 nonce roundtrip mismatch:{pong!r}")
        worker.send({"command": "S1_RUN", "attempt_id": attempt_id, "plan_sha256": plan_file_sha, "message_id": s1_message_id})
        batch = worker.read_event(120)
        if batch.get("event") != "S1_PROBE_BATCH_RESULT" or batch.get("instance_id") != worker.instance_id:
            raise RuntimeError(f"S1 probe response mismatch:{batch!r}")
        worker.stop(stop_id)
        helper.post_and_stop()
        post_snapshot = _snapshot(args.distro, staged, attempt_id, output, "POST", setup_log, include_helper_log=True)
        report.update({
            "ready": ready,
            "helper_ready": helper_ready,
            "pong": pong,
            "probe_batch": batch,
            "cleanup_status": "PROVEN" if worker.cleanup_status == "PROVEN" and helper.cleanup_status == "PROVEN" else "UNPROVEN",
        })
    except BaseException as exc:
        producer_exception = f"{type(exc).__name__}:{exc}"
        report["producer_exception"] = producer_exception
        report["failure_code"] = getattr(exc, "code", "S1_RUNTIME_FAILURE")
        if worker is not None and worker.cleanup_status != "PROVEN":
            try:
                worker.abort()
            except BaseException as cleanup_exc:
                report["worker_cleanup_exception"] = f"{type(cleanup_exc).__name__}:{cleanup_exc}"
        if helper is not None and helper.cleanup_status != "PROVEN":
            helper.abort()
        if staged is not None:
            try:
                post_snapshot = _snapshot(args.distro, staged, attempt_id, output, "POST", setup_log, include_helper_log=True)
            except BaseException as snapshot_exc:
                report["post_snapshot_exception"] = f"{type(snapshot_exc).__name__}:{snapshot_exc}"
        report["cleanup_status"] = "PROVEN" if worker is not None and worker.cleanup_status == "PROVEN" and helper is not None and helper.cleanup_status == "PROVEN" else "UNPROVEN"

    worker_events = _read_events(output / "worker_events.jsonl")
    helper_evidence = {} if helper is None else helper.evidence()
    bundle = {
        "plan": plan,
        "fixture_manifest": fixture_manifest,
        "fixture_manifest_file_sha256": fixture_manifest_sha,
        "plan_file_sha256": plan_file_sha,
        "plan_canonical_sha256": plan_canonical_sha,
        "expected": expected,
        "events": worker_events,
        "pre_snapshot": pre_snapshot,
        "post_snapshot": post_snapshot,
        "helper": helper_evidence,
        "producer_exception": producer_exception,
    }
    write_json(output / "S1_EVIDENCE_BUNDLE.json", bundle)
    review = review_s1_evidence(bundle) if expected else {
        "reviewer": "INDEPENDENT_R1_6H_S1_EVIDENCE_REVIEWER", "verdict": "INCONCLUSIVE",
        "issues": [{"severity": "MISSING", "reason": "NO_FROZEN_REVIEW_INTENT"}],
        "planned_probe_count": len(plan.get("probes", [])), "observed_probe_count": 0,
    }
    write_json(output / "S1_REVIEW.json", review)
    rows = (((next((event for event in worker_events if _event_tag_local(event) == "IPC_RECEIVED:S1_PROBE_BATCH_RESULT"), {}) or {}).get("worker_event") or {}).get("result") or {}).get("rows") or []
    probe_results = output / "S1_PROBE_RESULTS.jsonl"
    probe_results.touch(exist_ok=False)
    for row in rows:
        _append_jsonl(probe_results, row)
    report["independent_review"] = review
    report["status"] = review["verdict"]
    report["worker_cleanup_status"] = "NOT_STARTED" if worker is None else worker.cleanup_status
    report["helper_cleanup_status"] = "NOT_STARTED" if helper is None else helper.cleanup_status
    report["candidate_runtime"] = None if staged is None else asdict(staged)
    report["claim_ceiling"] = "Scoped S1 only for listed synthetic objects/operations/configuration/window; no S2, state transfer, process conformance, matrix, c-effect, same-c, B5 superiority, ROI, or live readiness."
    write_json(output / "S1_REPORT.json", report)
    for name, collector in (("worker_stdout.txt", None if worker is None else worker.stdout), ("worker_stderr.txt", None if worker is None else worker.stderr), ("helper_stdout.txt", None if helper is None else helper.stdout), ("helper_stderr.txt", None if helper is None else helper.stderr)):
        (output / name).write_text("" if collector is None else str(collector.snapshot().get("captured", "")), encoding="utf-8", newline="\n")
    print(json.dumps(report, sort_keys=True))
    return 0 if report["status"] == "PASS_SCOPED_S1" else 1


def _event_tag_local(event: dict[str, Any]) -> str:
    if event.get("kind") == "IPC_RECEIVED":
        return f"IPC_RECEIVED:{(event.get('worker_event') or {}).get('event')}"
    return str(event.get("kind"))


if __name__ == "__main__":
    raise SystemExit(main())
