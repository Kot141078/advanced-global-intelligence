from __future__ import annotations

import codecs
import hashlib
import json
import os
import queue
import secrets
import subprocess
import threading
import time
import uuid
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, BinaryIO, Callable

MAX_STREAM_CHARS = 64 * 1024
MAX_PROTOCOL_FRAME_CHARS = 32 * 1024
MAX_PROTOCOL_QUEUE = 32
READ_CHUNK_BYTES = 1024
MAX_MARKERS = 16


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


class WorkerStartupError(RuntimeError):
    code = "STARTUP_ERROR"


class WorkerEOFError(WorkerStartupError):
    code = "EOF"


class WorkerEarlyExitError(WorkerStartupError):
    code = "EARLY_EXIT"


class WorkerDeadlineTimeout(WorkerStartupError):
    code = "TIMEOUT"


class WorkerProtocolError(WorkerStartupError):
    code = "PROTOCOL_ERROR"


class WorkerOverflowError(WorkerStartupError):
    code = "OVERFLOW"


class CleanupUnprovenError(WorkerStartupError):
    code = "STOP_CLEANUP_UNPROVEN"


@dataclass(frozen=True)
class StagedRuntime:
    stage_dir: str
    worker: str
    worker_sha256: str
    launcher: str
    launcher_sha256: str
    stage_receipt: dict[str, Any]
    mode: str = "S0"
    s1_plan: str | None = None
    s1_plan_sha256: str | None = None
    s1_fixture_manifest: str | None = None
    s1_fixture_manifest_sha256: str | None = None
    s1_attempt_id: str | None = None
    helper_dir: str | None = None
    helper: str | None = None
    helper_sha256: str | None = None
    s2_plan: str | None = None
    s2_plan_sha256: str | None = None
    s2_fixture_manifest: str | None = None
    s2_fixture_manifest_sha256: str | None = None
    s2_attempt_id: str | None = None
    s2_worker_role: str | None = None


@dataclass
class LaunchOutcome:
    """Monotone ownership state created before any process-start request."""

    instance_id: str
    start_request_issued: bool = False
    process_handle_obtained: bool = False
    host_pid: int | None = None
    host_handle: int | None = None
    child_binding_obtained: bool = False
    worker_pid: int | None = None
    worker_start_ticks: int | None = None
    ready_observed: bool = False
    cleanup_status: str = "NOT_STARTED"
    failure_classification: str | None = None


class BoundedStreamCollector:
    """One binary reader per pipe with bounded capture, framing, and queue."""

    def __init__(
        self,
        stream: BinaryIO,
        *,
        forward_lines: bool,
        max_chars: int = MAX_STREAM_CHARS,
        max_frame_chars: int = MAX_PROTOCOL_FRAME_CHARS,
        queue_limit: int = MAX_PROTOCOL_QUEUE,
        read_chunk_bytes: int = READ_CHUNK_BYTES,
        trusted_markers_only: bool = False,
    ):
        if min(max_chars, max_frame_chars, queue_limit, read_chunk_bytes) <= 0:
            raise ValueError("collector limits must be positive")
        self.stream = stream
        self.forward_lines = forward_lines
        self.max_chars = max_chars
        self.max_frame_chars = max_frame_chars
        self.read_chunk_bytes = read_chunk_bytes
        self.trusted_markers_only = trusted_markers_only
        self.items: queue.Queue[tuple[str, str | BaseException | None]] = queue.Queue(maxsize=queue_limit)
        self._parts: list[str] = []
        self._captured = 0
        self._buffer = ""
        self._markers: list[dict[str, Any]] = []
        self._worker_diagnostics: list[dict[str, Any]] = []
        self._marker_lock = threading.Lock()
        self.total_chars = 0
        self.total_bytes = 0
        self.truncated = False
        self.overflow: str | None = None
        self.error: str | None = None
        self.incomplete_frame = False
        self.max_observed_frame_chars = 0
        self.thread = threading.Thread(target=self._run, name="cgdr-bounded-binary-pipe-reader", daemon=True)
        self.thread.start()

    @property
    def markers(self) -> list[dict[str, Any]]:
        with self._marker_lock:
            return [dict(item) for item in self._markers]

    @property
    def worker_diagnostics(self) -> list[dict[str, Any]]:
        with self._marker_lock:
            return [dict(item) for item in self._worker_diagnostics]

    def _remember(self, value: str) -> None:
        self.total_chars += len(value)
        remaining = self.max_chars - self._captured
        if remaining > 0:
            kept = value[:remaining]
            self._parts.append(kept)
            self._captured += len(kept)
        if len(value) > max(remaining, 0):
            self.truncated = True

    def _put(self, kind: str, value: str | BaseException | None) -> None:
        if not self.forward_lines:
            return
        try:
            self.items.put_nowait((kind, value))
        except queue.Full:
            self.overflow = self.overflow or "FRAME_QUEUE_LIMIT"

    def _frame(self, frame: str) -> None:
        self.max_observed_frame_chars = max(self.max_observed_frame_chars, len(frame))
        if len(frame) > self.max_frame_chars:
            self.overflow = self.overflow or "FRAME_SIZE_LIMIT"
            self._put("overflow", self.overflow)
            return
        stripped = frame.rstrip("\r\n")
        if stripped.startswith("{"):
            try:
                candidate = json.loads(stripped)
            except (json.JSONDecodeError, TypeError):
                candidate = None
            if isinstance(candidate, dict):
                marker: dict[str, Any] | None = None
                if self.trusted_markers_only:
                    if (
                        candidate.get("record_type") == "TRUSTED_PARENT_RECEIPT"
                        and candidate.get("receipt_channel") == "PARENT_ONLY_STDERR_V1"
                        and isinstance(candidate.get("payload"), dict)
                        and isinstance(candidate["payload"].get("marker"), str)
                    ):
                        marker = dict(candidate["payload"])
                        marker["_receipt_record_type"] = candidate["record_type"]
                        marker["_receipt_channel"] = candidate["receipt_channel"]
                    elif candidate.get("record_type") == "WORKER_STDERR_DATA":
                        with self._marker_lock:
                            if len(self._worker_diagnostics) < MAX_MARKERS:
                                self._worker_diagnostics.append(candidate)
                elif isinstance(candidate.get("marker"), str):
                    marker = candidate
                if marker is not None:
                    with self._marker_lock:
                        if len(self._markers) < MAX_MARKERS:
                            self._markers.append(marker)
                        else:
                            self.overflow = self.overflow or "MARKER_QUEUE_LIMIT"
        self._put("line", frame)

    def _read(self) -> bytes | str:
        read1 = getattr(self.stream, "read1", None)
        return read1(self.read_chunk_bytes) if callable(read1) else self.stream.read(self.read_chunk_bytes)

    def _consume_text(self, text: str) -> None:
        if not text:
            return
        self._remember(text)
        self._buffer += text
        while "\n" in self._buffer:
            line, self._buffer = self._buffer.split("\n", 1)
            self._frame(line + "\n")
        if len(self._buffer) > self.max_frame_chars:
            self.max_observed_frame_chars = max(self.max_observed_frame_chars, len(self._buffer))
            self.overflow = self.overflow or "FRAME_SIZE_LIMIT"
            self._buffer = ""
            self._put("overflow", self.overflow)

    def _run(self) -> None:
        decoder = codecs.getincrementaldecoder("utf-8")("strict")
        try:
            while True:
                chunk = self._read()
                if chunk in (b"", ""):
                    self._consume_text(decoder.decode(b"", final=True))
                    if self._buffer:
                        self.incomplete_frame = True
                        self._put("incomplete", self._buffer[: self.max_frame_chars])
                    else:
                        self._put("eof", None)
                    return
                if isinstance(chunk, str):
                    self.total_bytes += len(chunk.encode("utf-8", errors="strict"))
                    self._consume_text(chunk)
                elif isinstance(chunk, (bytes, bytearray)):
                    raw = bytes(chunk)
                    self.total_bytes += len(raw)
                    self._consume_text(decoder.decode(raw, final=False))
                else:
                    raise TypeError("stream returned neither bytes nor text")
        except UnicodeDecodeError as exc:
            self.error = f"INVALID_UTF8:{exc.start}:{exc.reason}"
            self._put("error", WorkerProtocolError(self.error))
        except BaseException as exc:
            self.error = f"{type(exc).__name__}:{exc}"
            self._put("error", exc)

    def snapshot(self) -> dict[str, Any]:
        text = "".join(self._parts)
        return {
            "captured": text,
            "captured_chars": len(text),
            "total_chars": self.total_chars,
            "total_bytes": self.total_bytes,
            "truncated": self.truncated,
            "overflow": self.overflow,
            "incomplete_frame": self.incomplete_frame,
            "max_frame_chars": self.max_frame_chars,
            "queue_maxsize": self.items.maxsize,
            "read_chunk_bytes": self.read_chunk_bytes,
            "max_observed_frame_chars": self.max_observed_frame_chars,
            "sha256_captured_utf8": hashlib.sha256(text.encode("utf-8", errors="replace")).hexdigest(),
            "reader_error": self.error,
            "reader_alive": self.thread.is_alive(),
            "markers": self.markers,
            "worker_diagnostics": self.worker_diagnostics,
            "trusted_markers_only": self.trusted_markers_only,
        }

    def close_and_join(self, timeout: float) -> bool:
        try:
            if not getattr(self.stream, "closed", False):
                self.stream.close()
        except (OSError, ValueError, AttributeError):
            pass
        self.thread.join(timeout)
        return not self.thread.is_alive()

    def join(self, timeout: float) -> bool:
        self.thread.join(timeout)
        return not self.thread.is_alive()


def _runtime_from_legacy(staged_worker: str) -> StagedRuntime:
    worker = str(staged_worker)
    stage_dir = str(Path(worker).parent).replace("\\", "/")
    return StagedRuntime(
        stage_dir=stage_dir,
        worker=worker,
        worker_sha256="UNVERIFIED_LEGACY_INPUT",
        launcher=f"{stage_dir}/s0_launcher.py",
        launcher_sha256="UNVERIFIED_LEGACY_INPUT",
        stage_receipt={"kind": "LEGACY_UNVERIFIED_INPUT"},
    )


def _worker_command(
    distro: str,
    staged_runtime: StagedRuntime | str,
    instance_id: str,
    receipt_nonce: str | None = None,
) -> tuple[list[str], list[str]]:
    runtime = staged_runtime if isinstance(staged_runtime, StagedRuntime) else _runtime_from_legacy(staged_runtime)
    nonce = receipt_nonce or "OFFLINE_COMMAND_CONSTRUCTION_ONLY"
    if not isinstance(nonce, str) or not nonce or nonce.startswith("-"):
        raise ValueError("receipt nonce must be a non-empty CLI-safe token")
    inner_argv = [
        "unshare", "--user", "--map-root-user", "--mount", "--net", "--pid", "--fork", "--mount-proc",
        "/usr/bin/python3", runtime.launcher, "wait",
        "--stage-dir", runtime.stage_dir,
        "--worker", runtime.worker,
        "--worker-sha256", runtime.worker_sha256,
        "--launcher", runtime.launcher,
        "--launcher-sha256", runtime.launcher_sha256,
        "--instance-id", instance_id,
        "--receipt-nonce", nonce,
    ]
    if runtime.mode == "S1":
        required = {
            "s1_plan": runtime.s1_plan,
            "s1_plan_sha256": runtime.s1_plan_sha256,
            "s1_fixture_manifest": runtime.s1_fixture_manifest,
            "s1_fixture_manifest_sha256": runtime.s1_fixture_manifest_sha256,
            "s1_attempt_id": runtime.s1_attempt_id,
            "helper_dir": runtime.helper_dir,
        }
        missing = [name for name, value in required.items() if not value]
        if missing:
            raise ValueError(f"S1 staged runtime binding missing: {missing}")
        inner_argv.extend([
            "--s1-mode",
            "--s1-plan", str(runtime.s1_plan),
            "--s1-plan-sha256", str(runtime.s1_plan_sha256),
            "--s1-fixture-manifest", str(runtime.s1_fixture_manifest),
            "--s1-fixture-manifest-sha256", str(runtime.s1_fixture_manifest_sha256),
            "--s1-scratch", f"{runtime.stage_dir.rstrip('/')}/scratch",
            "--s1-private", f"{runtime.stage_dir.rstrip('/')}/private",
            "--s1-attempt-id", str(runtime.s1_attempt_id),
            "--endpoint-mask-dir", str(runtime.helper_dir),
        ])
    if runtime.mode == "S2":
        required = {
            "s2_plan": runtime.s2_plan,
            "s2_plan_sha256": runtime.s2_plan_sha256,
            "s2_fixture_manifest": runtime.s2_fixture_manifest,
            "s2_fixture_manifest_sha256": runtime.s2_fixture_manifest_sha256,
            "s2_attempt_id": runtime.s2_attempt_id,
            "s2_worker_role": runtime.s2_worker_role,
        }
        missing = [name for name, value in required.items() if not value]
        if missing:
            raise ValueError(f"S2 staged runtime binding missing: {missing}")
        inner_argv.extend([
            "--s2-mode",
            "--s2-plan", str(runtime.s2_plan),
            "--s2-plan-sha256", str(runtime.s2_plan_sha256),
            "--s2-fixture-manifest", str(runtime.s2_fixture_manifest),
            "--s2-fixture-manifest-sha256", str(runtime.s2_fixture_manifest_sha256),
            "--s2-scratch", f"{runtime.stage_dir.rstrip('/')}/scratch",
            "--s2-private", f"{runtime.stage_dir.rstrip('/')}/private",
            "--s2-attempt-id", str(runtime.s2_attempt_id),
            "--s2-worker-role", str(runtime.s2_worker_role),
        ])
    command = ["wsl.exe", "-d", distro, "--", *inner_argv]
    isolation = [
        "WSL2 Ubuntu distro process",
        "new user namespace with outer user mapped to inner root",
        "new mount namespace with private propagation",
        "new network namespace",
        "new PID namespace and mounted private proc",
        "mode-000 nosuid nodev noexec tmpfs masks /home, /root and /mnt",
        "worker stdin/stdout/stderr inherit bounded host IPC pipes through a direct fork/exec",
        "trusted launcher binds child PID/start/namespaces before releasing it to exec",
        "trusted launcher uses direct waitpid on that child and emits the exit receipt",
        "worker environment is an explicit allowlist and excludes the receipt nonce",
        "trusted parent receipts use a parent-only FD; child stderr is separately piped and externally tagged",
        "child sets no_new_privs, locked securebits, zero capability sets/bounding set, and dumpable=0 before exec",
        "no shell, eval, nested interpolation, endpoint helper, or background watcher",
    ]
    if runtime.mode == "S1":
        isolation.extend([
            "whole task stage is a read-only bind mount",
            "worker scratch is a private writable tmpfs submount",
            "private canary and trusted helper directory are hidden by mode-000 tmpfs mounts",
            "the worker executes only the frozen S1 plan operations",
        ])
    if runtime.mode == "S2":
        isolation.extend([
            "whole task stage is a read-only bind mount",
            "worker scratch is a private writable tmpfs submount",
            "private stage area and all host mounts are hidden by mode-000 tmpfs mounts",
            "the worker executes only the fixed command set for its frozen W0 or W1 S2 role",
            "checkpoint bytes traverse bounded stdin/stdout IPC; checkpoint store and authority services are not mounted into the worker",
        ])
    return command, isolation


class WorkerProcess:
    """Prepared ownership object. Construction never launches a process."""

    def __init__(
        self,
        distro: str,
        staged_runtime: StagedRuntime | str,
        event_log: Path,
        cell_id: str,
        label: str,
        *,
        popen_factory: Callable[..., Any] = subprocess.Popen,
        clock: Callable[[], float] = time.perf_counter,
        clock_ns: Callable[[], int] = time.perf_counter_ns,
        cleanup_timeout: float = 10.0,
        receipt_nonce: str | None = None,
    ):
        self.instance_id = str(uuid.uuid4())
        self.runtime = staged_runtime if isinstance(staged_runtime, StagedRuntime) else _runtime_from_legacy(staged_runtime)
        self.receipt_nonce = receipt_nonce or secrets.token_hex(32)
        self.command, self.isolation = _worker_command(distro, self.runtime, self.instance_id, self.receipt_nonce)
        self.inner_argv = self.command[4:]
        self.event_log = event_log
        self.cell_id = cell_id
        self.label = label
        self._popen_factory = popen_factory
        self._clock = clock
        self._clock_ns = clock_ns
        self._cleanup_timeout = cleanup_timeout
        self._seq = 0
        self.process: Any | None = None
        self.stdout: BoundedStreamCollector | None = None
        self.stderr: BoundedStreamCollector | None = None
        self.child_binding: dict[str, Any] | None = None
        self.child_security: dict[str, Any] | None = None
        self.inner_exit: dict[str, Any] | None = None
        self.cleanup_forced_kill = False
        self.cleanup_natural_exit = False
        self._test_double = False
        self.outcome = LaunchOutcome(instance_id=self.instance_id)

    @property
    def cleanup_status(self) -> str:
        return self.outcome.cleanup_status

    @cleanup_status.setter
    def cleanup_status(self, value: str) -> None:
        self.outcome.cleanup_status = value

    def start(self, ready_timeout: float = 10.0) -> dict[str, Any]:
        if self.outcome.start_request_issued:
            raise RuntimeError("start request already issued")
        if not self._test_double and (
            self.runtime.worker_sha256 == "UNVERIFIED_LEGACY_INPUT"
            or self.runtime.launcher_sha256 == "UNVERIFIED_LEGACY_INPUT"
        ):
            raise WorkerProtocolError("live start requires a verified StagedRuntime receipt")
        self.outcome.start_request_issued = True
        self._event({
            "kind": "PROCESS_START_REQUESTED",
            "cell_id": self.cell_id,
            "label": self.label,
            "instance_id": self.instance_id,
            "argv": self.command,
            "inner_argv": self.inner_argv,
            "receipt_nonce_sha256": hashlib.sha256(self.receipt_nonce.encode()).hexdigest(),
            "staged_runtime": asdict(self.runtime),
            "isolation_configuration": self.isolation,
            "host_utc": utc_now(),
            "host_perf_counter_ns": self._clock_ns(),
            "clock_domain": "HOST_PERF_COUNTER_NS",
        })
        try:
            self.process = self._popen_factory(
                self.command,
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=False,
                bufsize=0,
                env={key: os.environ[key] for key in ("SystemRoot", "WINDIR", "PATH") if key in os.environ},
            )
        except BaseException as exc:
            self.outcome.failure_classification = "EARLY_EXIT"
            self.cleanup_status = "UNPROVEN"
            self._event({
                "kind": "PROCESS_START_EXCEPTION",
                "classification": "EARLY_EXIT",
                "exception": f"{type(exc).__name__}:{exc}",
                "argv": self.command,
                "instance_id": self.instance_id,
                "cleanup_status": self.cleanup_status,
                "host_utc": utc_now(),
                "host_perf_counter_ns": self._clock_ns(),
                "clock_domain": "HOST_PERF_COUNTER_NS",
            })
            raise CleanupUnprovenError("start request issued but no owned handle was returned") from exc
        try:
            self._attach_process()
        except BaseException as exc:
            self.outcome.failure_classification = "PROTOCOL_ERROR"
            cleanup = self._cleanup_owned(reason="PROCESS_ATTACH_EXCEPTION")
            self._event({
                "kind": "PROCESS_ATTACH_EXCEPTION",
                "classification": "PROTOCOL_ERROR",
                "exception": f"{type(exc).__name__}:{exc}",
                "instance_id": self.instance_id,
                "cleanup_status": cleanup,
                "host_utc": utc_now(),
                "host_perf_counter_ns": self._clock_ns(),
                "clock_domain": "HOST_PERF_COUNTER_NS",
            })
            raise CleanupUnprovenError(f"owned handle returned but pipe attachment failed; cleanup={cleanup}") from exc
        return self._await_binding_and_ready(ready_timeout)

    def _attach_process(self) -> None:
        if self.process is None:
            raise RuntimeError("process handle unavailable")
        self.outcome.process_handle_obtained = True
        self.outcome.host_pid = getattr(self.process, "pid", None)
        handle = getattr(self.process, "_handle", None)
        self.outcome.host_handle = int(handle) if handle is not None else None
        self._event({
            "kind": "PROCESS_HANDLE_OBTAINED",
            "cell_id": self.cell_id,
            "label": self.label,
            "instance_id": self.instance_id,
            "host_pid": self.outcome.host_pid,
            "host_handle": self.outcome.host_handle,
            "host_utc": utc_now(),
            "host_perf_counter_ns": self._clock_ns(),
            "clock_domain": "HOST_PERF_COUNTER_NS",
        })
        if self.process.stdout is None or self.process.stderr is None:
            raise RuntimeError("process handle returned without required stdout/stderr pipes")
        self.stdout = BoundedStreamCollector(self.process.stdout, forward_lines=True)
        self.stderr = BoundedStreamCollector(self.process.stderr, forward_lines=False, trusted_markers_only=True)

    def _valid_child_binding(self, value: dict[str, Any]) -> bool:
        return bool(
            value.get("marker") == "CGDR_CHILD_BOUND"
            and value.get("binding_source") == "TRUSTED_DIRECT_FORK_PARENT"
            and value.get("wait_source") == "POSIX_WAITPID_CHILD"
            and value.get("_receipt_record_type") == "TRUSTED_PARENT_RECEIPT"
            and value.get("_receipt_channel") == "PARENT_ONLY_STDERR_V1"
            and value.get("receipt_channel") == "PARENT_ONLY_STDERR_V1"
            and value.get("instance_id") == self.instance_id
            and value.get("receipt_nonce") == self.receipt_nonce
            and value.get("worker_sha256") == self.runtime.worker_sha256
            and value.get("launcher_sha256") == self.runtime.launcher_sha256
            and isinstance(value.get("worker_pid"), int)
            and isinstance(value.get("worker_start_ticks"), int)
            and isinstance(value.get("waiter_pid"), int)
            and isinstance(value.get("waiter_start_ticks"), int)
            and all(isinstance(value.get(name), str) for name in ("pid_namespace", "network_namespace", "mount_namespace"))
        )

    def _valid_child_security(self, value: dict[str, Any], binding: dict[str, Any]) -> bool:
        if not (
            value.get("marker") == "CGDR_CHILD_SECURITY"
            and value.get("binding_source") == "TRUSTED_DIRECT_FORK_PARENT_POST_EXEC_PROCFS"
            and value.get("_receipt_record_type") == "TRUSTED_PARENT_RECEIPT"
            and value.get("_receipt_channel") == "PARENT_ONLY_STDERR_V1"
            and value.get("receipt_channel") == "PARENT_ONLY_STDERR_V1"
            and value.get("instance_id") == self.instance_id
            and value.get("receipt_nonce") == self.receipt_nonce
            and value.get("worker_pid") == binding.get("worker_pid")
            and value.get("worker_start_ticks") == binding.get("worker_start_ticks")
            and value.get("pid_namespace") == binding.get("pid_namespace")
            and value.get("network_namespace") == binding.get("network_namespace")
            and value.get("mount_namespace") == binding.get("mount_namespace")
            and isinstance(value.get("security_receipt_sha256"), str)
        ):
            return False
        status = value.get("status") or {}
        fields = status.get("status_fields") or {}
        fds = status.get("fds") or []
        if not isinstance(fields, dict) or not isinstance(fds, list):
            return False
        if self.runtime.mode not in {"S1", "S2"}:
            return True
        zero_caps = all(fields.get(name) == "0000000000000000" for name in ("CapInh", "CapPrm", "CapEff", "CapBnd", "CapAmb"))
        exact_fds = [item.get("fd") for item in fds if isinstance(item, dict)] == [0, 1, 2]
        routes_separate = (
            value.get("worker_stderr_route") == "DEDICATED_PIPE_WRAPPED_BY_TRUSTED_PARENT"
            and value.get("trusted_receipt_route") == "PARENT_ONLY_STDERR_V1"
        )
        mounts = {item.get("mount_point"): item for item in value.get("mounts", []) if isinstance(item, dict)}
        stage = mounts.get(self.runtime.stage_dir) or {}
        scratch = mounts.get(f"{self.runtime.stage_dir.rstrip('/')}/scratch") or {}
        private = mounts.get(f"{self.runtime.stage_dir.rstrip('/')}/private") or {}
        helper = mounts.get(str(self.runtime.helper_dir)) or {}
        host_mask = mounts.get("/mnt") or {}
        mount_policy = bool(
            "ro" in stage.get("mount_options", [])
            and "rw" in scratch.get("mount_options", [])
            and private.get("filesystem") == "tmpfs"
            and (
                (self.runtime.mode == "S1" and helper.get("filesystem") == "tmpfs")
                or (self.runtime.mode == "S2" and host_mask.get("filesystem") == "tmpfs")
            )
        )
        return bool(zero_caps and fields.get("NoNewPrivs") == "1" and exact_fds and routes_separate and mount_policy)

    def _await_child_security(self, deadline: float, binding: dict[str, Any]) -> dict[str, Any]:
        if self.stderr is None:
            raise WorkerProtocolError("stderr collector unavailable")
        while True:
            if self.stderr.overflow:
                raise WorkerOverflowError(self.stderr.overflow)
            if self.stderr.error:
                raise WorkerProtocolError(f"stderr reader failed: {self.stderr.error}")
            for marker in self.stderr.markers:
                if marker.get("marker") == "CGDR_CHILD_SECURITY":
                    # Preserve the exact receipt for lifecycle cleanup review even when
                    # its separate access-policy validation fails.
                    self.child_security = marker
                    if not self._valid_child_security(marker, binding):
                        raise WorkerProtocolError(f"invalid trusted child security receipt: {marker!r}")
                    self._event({
                        "kind": "OS_CHILD_SECURITY_BOUND",
                        "instance_id": self.instance_id,
                        "security": marker,
                        "host_utc": utc_now(),
                        "host_perf_counter_ns": self._clock_ns(),
                        "clock_domain": "HOST_PERF_COUNTER_NS",
                    })
                    return marker
            remaining = deadline - self._clock()
            if remaining <= 0:
                if self._poll() is not None:
                    raise WorkerEarlyExitError(f"wrapper exited rc={self._poll()} before trusted security receipt")
                raise WorkerDeadlineTimeout("deadline elapsed before trusted child security receipt")
            time.sleep(min(remaining, 0.01))

    def _await_child_binding(self, deadline: float) -> dict[str, Any]:
        if self.stderr is None:
            raise WorkerProtocolError("stderr collector unavailable")
        while True:
            if self.stderr.overflow:
                raise WorkerOverflowError(self.stderr.overflow)
            if self.stderr.error:
                raise WorkerProtocolError(f"stderr reader failed: {self.stderr.error}")
            for marker in self.stderr.markers:
                if marker.get("marker") == "CGDR_CHILD_BOUND" and self._valid_child_binding(marker):
                    self.child_binding = marker
                    self.outcome.child_binding_obtained = True
                    self.outcome.worker_pid = marker["worker_pid"]
                    self.outcome.worker_start_ticks = marker["worker_start_ticks"]
                    self._event({
                        "kind": "OS_CHILD_BOUND",
                        "instance_id": self.instance_id,
                        "binding": marker,
                        "host_utc": utc_now(),
                        "host_perf_counter_ns": self._clock_ns(),
                        "clock_domain": "HOST_PERF_COUNTER_NS",
                    })
                    return marker
            remaining = deadline - self._clock()
            if remaining <= 0:
                rc = self._poll()
                if rc is not None:
                    raise WorkerEarlyExitError(f"wrapper exited rc={rc} before trusted child binding")
                raise WorkerDeadlineTimeout("deadline elapsed before trusted OS child binding")
            if self._poll() is not None and not self.stderr.thread.is_alive():
                raise WorkerEarlyExitError(f"wrapper exited rc={self._poll()} before trusted child binding")
            time.sleep(min(remaining, 0.01))

    def _await_binding_and_ready(self, ready_timeout: float) -> dict[str, Any]:
        deadline = self._clock() + ready_timeout
        try:
            binding = self._await_child_binding(deadline)
            security = self._await_child_security(deadline, binding)
            remaining = deadline - self._clock()
            if remaining <= 0:
                raise WorkerDeadlineTimeout("deadline elapsed between child binding and READY")
            ready = self.read_event(timeout_seconds=remaining, startup=True)
            if ready.get("event") != "READY" or ready.get("instance_id") != self.instance_id:
                raise WorkerProtocolError(f"READY mismatch: {ready!r}")
            expected = {
                "pid": binding["worker_pid"],
                "proc_start_ticks": binding["worker_start_ticks"],
                "pid_namespace": binding["pid_namespace"],
                "network_namespace": binding["network_namespace"],
                "mount_namespace": binding["mount_namespace"],
            }
            if any(ready.get(key) != value for key, value in expected.items()):
                raise WorkerProtocolError(f"READY does not match trusted OS child binding: expected={expected!r}, actual={ready!r}")
            if self.runtime.mode == "S2" and (
                ready.get("s2_mode") is not True
                or ready.get("s2_plan_sha256") != self.runtime.s2_plan_sha256
                or ready.get("s2_worker_role") != self.runtime.s2_worker_role
                or ready.get("s2_attempt_id") != self.runtime.s2_attempt_id
            ):
                raise WorkerProtocolError(f"READY does not match frozen S2 role/plan: {ready!r}")
            self.outcome.ready_observed = True
            self._event({
                "kind": "WORKER_READY",
                "cell_id": self.cell_id,
                "label": self.label,
                "instance_id": self.instance_id,
                "worker_event": ready,
                "trusted_binding_ref": {
                    "worker_pid": binding["worker_pid"],
                    "worker_start_ticks": binding["worker_start_ticks"],
                    "waiter_pid": binding["waiter_pid"],
                    "security_receipt_sha256": security["security_receipt_sha256"],
                },
                "host_utc": utc_now(),
                "host_perf_counter_ns": self._clock_ns(),
                "clock_domain": "HOST_PERF_COUNTER_NS",
            })
            return ready
        except BaseException as exc:
            classification = exc.code if isinstance(exc, WorkerStartupError) else "PROTOCOL_ERROR"
            self.outcome.failure_classification = classification
            cleanup = self._cleanup_owned(reason=f"STARTUP_{classification}")
            if isinstance(exc, WorkerEOFError) and self.cleanup_natural_exit:
                classification = "EARLY_EXIT"
                self.outcome.failure_classification = classification
                exc = WorkerEarlyExitError(f"stdout EOF followed by natural wrapper exit rc={self._poll()}")
            self._event({
                "kind": "STARTUP_FAILED",
                "classification": classification,
                "exception": f"{type(exc).__name__}:{exc}",
                "instance_id": self.instance_id,
                "return_code": self._poll(),
                "return_code_available": self._poll() is not None,
                "diagnostics": self.diagnostics(),
                "cleanup": cleanup,
                "host_utc": utc_now(),
                "host_perf_counter_ns": self._clock_ns(),
            })
            if cleanup not in {"PROVEN", "TEST_DOUBLE_COMPLETE"}:
                raise CleanupUnprovenError(f"startup {classification}; cleanup={cleanup}") from exc
            raise exc

    def _event(self, value: dict[str, Any]) -> None:
        self._seq += 1
        record = {"local_seq": self._seq, **value}
        self.event_log.parent.mkdir(parents=True, exist_ok=True)
        with self.event_log.open("a", encoding="utf-8", newline="\n") as stream:
            stream.write(json.dumps(record, sort_keys=True) + "\n")

    def _poll(self) -> int | None:
        return None if self.process is None else self.process.poll()

    def send(self, value: dict[str, Any]) -> None:
        if self.process is None or self.process.poll() is not None:
            raise WorkerEarlyExitError(f"worker exited rc={self._poll()} before send")
        if self.process.stdin is None:
            raise WorkerProtocolError("worker stdin unavailable")
        encoded = (json.dumps(value, sort_keys=True, separators=(",", ":")) + "\n").encode("utf-8")
        if len(encoded) > MAX_PROTOCOL_FRAME_CHARS:
            raise WorkerOverflowError("outbound frame exceeds fixed limit")
        self.process.stdin.write(encoded)
        self.process.stdin.flush()
        self._event({
            "kind": "IPC_SENT",
            "instance_id": self.instance_id,
            "command": value.get("command"),
            "message_id": value.get("message_id") or value.get("operation_id") or value.get("release_id") or value.get("stop_id"),
            "nonce": value.get("nonce"),
            "frame_bytes": len(encoded),
            "host_utc": utc_now(),
            "host_perf_counter_ns": self._clock_ns(),
            "clock_domain": "HOST_PERF_COUNTER_NS",
        })

    def read_event(self, timeout_seconds: float = 10.0, *, startup: bool = False) -> dict[str, Any]:
        if self.stdout is None:
            raise WorkerProtocolError("stdout collector unavailable")
        deadline = self._clock() + timeout_seconds
        while True:
            if self.stdout.overflow:
                raise WorkerOverflowError(self.stdout.overflow)
            if self.stdout.error:
                raise WorkerProtocolError(f"stdout reader failed: {self.stdout.error}")
            remaining = deadline - self._clock()
            if remaining <= 0:
                rc = self._poll()
                if rc is not None:
                    raise WorkerEarlyExitError(f"process exited rc={rc} before protocol event")
                raise WorkerDeadlineTimeout(f"deadline elapsed after {timeout_seconds:.6f}s")
            try:
                kind, payload = self.stdout.items.get(timeout=min(remaining, 0.05))
            except queue.Empty:
                continue
            if kind == "overflow":
                raise WorkerOverflowError(str(payload))
            if kind == "incomplete":
                raise WorkerProtocolError("stdout EOF before newline completed the frame")
            if kind == "eof":
                rc = self._poll()
                if rc is not None:
                    raise WorkerEarlyExitError(f"stdout EOF after process exit rc={rc}")
                raise WorkerEOFError("stdout EOF while wrapper exit status unavailable")
            if kind == "error":
                raise WorkerProtocolError(f"stdout reader failed: {payload}")
            if not isinstance(payload, str):
                raise WorkerProtocolError("protocol collector yielded a non-text frame")
            try:
                event = json.loads(payload)
            except json.JSONDecodeError as exc:
                raise WorkerProtocolError(f"malformed JSON event: {exc.msg}") from exc
            if not isinstance(event, dict) or not isinstance(event.get("event"), str):
                raise WorkerProtocolError("protocol event must be an object with string event")
            self._event({
                "kind": "IPC_RECEIVED",
                "instance_id": self.instance_id,
                "worker_event": event,
                "startup_phase": startup,
                "host_utc": utc_now(),
                "host_perf_counter_ns": self._clock_ns(),
                "clock_domain": "HOST_PERF_COUNTER_NS",
            })
            return event

    def _find_marker(self, marker_name: str) -> dict[str, Any] | None:
        if self.stderr is None:
            return None
        for value in self.stderr.markers:
            if value.get("marker") == marker_name and value.get("instance_id") == self.instance_id:
                return value
        return None

    def _inner_exit_valid(self, rc: int | None) -> bool:
        if not self.child_binding or not self.inner_exit or rc is None:
            return False
        exact_fields = (
            "instance_id", "receipt_nonce", "worker_pid", "worker_start_ticks", "waiter_pid",
            "waiter_start_ticks", "pid_namespace", "network_namespace", "mount_namespace",
            "worker_sha256", "launcher_sha256",
        )
        return bool(
            self._valid_child_binding(self.child_binding)
            and self.inner_exit.get("marker") == "CGDR_INNER_EXIT"
            and self.inner_exit.get("binding_source") == "TRUSTED_DIRECT_FORK_PARENT"
            and self.inner_exit.get("wait_source") == "POSIX_WAITPID_CHILD"
            and self.inner_exit.get("_receipt_record_type") == "TRUSTED_PARENT_RECEIPT"
            and self.inner_exit.get("_receipt_channel") == "PARENT_ONLY_STDERR_V1"
            and self.inner_exit.get("receipt_channel") == "PARENT_ONLY_STDERR_V1"
            and self.inner_exit.get("return_code") == rc
            and all(self.inner_exit.get(field) == self.child_binding.get(field) for field in exact_fields)
            and (self.runtime.mode not in {"S1", "S2"} or (
                self.child_security is not None
                and self.inner_exit.get("security_receipt_sha256") == self.child_security.get("security_receipt_sha256")
            ))
        )

    def diagnostics(self) -> dict[str, Any]:
        return {
            "argv": self.command,
            "inner_argv": self.inner_argv,
            "instance_id": self.instance_id,
            "receipt_nonce_sha256": hashlib.sha256(self.receipt_nonce.encode()).hexdigest(),
            "staged_runtime": asdict(self.runtime),
            "launch_outcome": asdict(self.outcome),
            "child_binding": self.child_binding,
            "child_security": self.child_security,
            "inner_exit": self.inner_exit,
            "return_code": self._poll(),
            "return_code_available": self._poll() is not None,
            "stdout": None if self.stdout is None else self.stdout.snapshot(),
            "stderr": None if self.stderr is None else self.stderr.snapshot(),
        }

    @staticmethod
    def _close_pipe(pipe: Any) -> None:
        try:
            if pipe is not None and not pipe.closed:
                pipe.close()
        except (OSError, ValueError, AttributeError):
            pass

    def _finish_collectors(self) -> bool:
        stdout_stopped = self.stdout is not None and (self.stdout.join(2) or self.stdout.close_and_join(2))
        stderr_stopped = self.stderr is not None and (self.stderr.join(2) or self.stderr.close_and_join(2))
        return bool(stdout_stopped and stderr_stopped)

    def _cleanup_owned(self, *, reason: str) -> str:
        if not self.outcome.start_request_issued:
            self.cleanup_status = "NOT_STARTED"
            return self.cleanup_status
        if self.process is None:
            self.cleanup_status = "UNPROVEN"
            return self.cleanup_status
        self.cleanup_status = "IN_PROGRESS"
        self._close_pipe(getattr(self.process, "stdin", None))
        if self.process.poll() is None:
            try:
                self.process.wait(timeout=self._cleanup_timeout)
                self.cleanup_natural_exit = True
            except subprocess.TimeoutExpired:
                try:
                    self.cleanup_forced_kill = True
                    self.process.kill()
                    self.process.wait(timeout=self._cleanup_timeout)
                except BaseException:
                    pass
            except BaseException:
                pass
        rc = self.process.poll()
        readers_stopped = self._finish_collectors()
        self.inner_exit = self._find_marker("CGDR_INNER_EXIT")
        if self._test_double:
            self.cleanup_status = "TEST_DOUBLE_COMPLETE" if rc is not None and readers_stopped else "UNPROVEN"
        else:
            self.cleanup_status = "PROVEN" if rc is not None and readers_stopped and self._inner_exit_valid(rc) else "UNPROVEN"
        self._event({
            "kind": "OWNED_PROCESS_CLEANUP",
            "instance_id": self.instance_id,
            "reason": reason,
            "status": self.cleanup_status,
            "return_code": rc,
            "reader_threads_stopped": readers_stopped,
            "child_binding": self.child_binding,
            "inner_exit_receipt": self.inner_exit,
            "inner_exit_confirmed": self._inner_exit_valid(rc) if not self._test_double else False,
            "natural_exit_before_kill": self.cleanup_natural_exit,
            "forced_wrapper_kill": self.cleanup_forced_kill,
            "host_utc": utc_now(),
            "host_perf_counter_ns": self._clock_ns(),
            "clock_domain": "HOST_PERF_COUNTER_NS",
        })
        return self.cleanup_status

    def stop(self, stop_id: str) -> dict[str, Any]:
        try:
            self.send({"command": "STOP", "stop_id": stop_id, "message_id": stop_id})
            ack = self.read_event(10)
            if ack.get("event") != "STOP_ACK" or ack.get("stop_id") != stop_id or ack.get("instance_id") != self.instance_id:
                raise WorkerProtocolError(f"invalid STOP_ACK: {ack!r}")
            requested = self._clock_ns()
            if self.process is None:
                raise CleanupUnprovenError("owned wrapper handle unavailable")
            rc = self.process.wait(timeout=10)
            observed = self._clock_ns()
            readers_stopped = self._finish_collectors()
            self.inner_exit = self._find_marker("CGDR_INNER_EXIT")
            if self._test_double:
                self.cleanup_status = "TEST_DOUBLE_COMPLETE" if readers_stopped and rc is not None else "UNPROVEN"
            else:
                self.cleanup_status = "PROVEN" if readers_stopped and self._inner_exit_valid(rc) else "UNPROVEN"
            self._event({
                "kind": "EXIT_OBSERVED",
                "instance_id": self.instance_id,
                "worker_pid": self.outcome.worker_pid,
                "worker_start_ticks": self.outcome.worker_start_ticks,
                "return_code": rc,
                "child_binding": self.child_binding,
                "inner_exit_receipt": self.inner_exit,
                "inner_exit_confirmed": self._inner_exit_valid(rc) if not self._test_double else False,
                "reader_threads_stopped": readers_stopped,
                "cleanup_status": self.cleanup_status,
                "host_utc": utc_now(),
                "stop_wait_start_ns": requested,
                "host_perf_counter_ns": observed,
                "elapsed_ns": observed - requested,
                "clock_domain": "HOST_PERF_COUNTER_NS",
            })
            if self.cleanup_status not in {"PROVEN", "TEST_DOUBLE_COMPLETE"}:
                raise CleanupUnprovenError("specific child wait/exit or pipe cleanup not proven")
            return ack
        except CleanupUnprovenError:
            raise
        except BaseException:
            cleanup = self._cleanup_owned(reason="STOP_FAILURE")
            if cleanup not in {"PROVEN", "TEST_DOUBLE_COMPLETE"}:
                raise CleanupUnprovenError("stop failed and cleanup is unproven")
            raise

    def abort(self) -> None:
        if self._cleanup_owned(reason="ABORT") not in {"PROVEN", "TEST_DOUBLE_COMPLETE"}:
            raise CleanupUnprovenError("abort cleanup unproven")


def _windows_c_to_wsl(path: Path) -> str:
    value = path.resolve().as_posix()
    if not value.lower().startswith("c:/"):
        raise ValueError("S0 staging sources must be on C drive")
    return "/mnt/c/" + value[3:]


def stage_worker(
    distro: str,
    local_worker: Path,
    stage_dir: str,
    setup_log: Path | None = None,
    *,
    local_launcher: Path | None = None,
) -> StagedRuntime:
    launcher = (local_launcher or Path(__file__).with_name("s0_launcher.py")).resolve()
    worker = local_worker.resolve()
    worker_sha = sha256_file(worker)
    launcher_sha = sha256_file(launcher)
    worker_source = _windows_c_to_wsl(worker)
    launcher_source = _windows_c_to_wsl(launcher)
    inner_argv = [
        "/usr/bin/python3", launcher_source, "stage",
        "--stage-dir", stage_dir,
        "--worker-source", worker_source,
        "--worker-sha256", worker_sha,
        "--launcher-source", launcher_source,
        "--launcher-sha256", launcher_sha,
    ]
    command = ["wsl.exe", "-d", distro, "--", *inner_argv]
    started = time.perf_counter_ns()
    completed = subprocess.run(
        command,
        stdin=subprocess.DEVNULL,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        timeout=10,
        check=False,
        env={key: os.environ[key] for key in ("SystemRoot", "WINDIR", "PATH") if key in os.environ},
    )
    record = {
        "kind": "WSL_SETUP_STAGE_S0_RUNTIME",
        "argv": command,
        "inner_argv": inner_argv,
        "return_code": completed.returncode,
        "stdout": completed.stdout[:16384],
        "stderr": completed.stderr[:16384],
        "stdout_truncated": len(completed.stdout) > 16384,
        "stderr_truncated": len(completed.stderr) > 16384,
        "start_ns": started,
        "end_ns": time.perf_counter_ns(),
        "clock_domain": "HOST_PERF_COUNTER_NS",
        "stage_dir": stage_dir,
        "worker_source": str(worker),
        "worker_sha256": worker_sha,
        "launcher_source": str(launcher),
        "launcher_sha256": launcher_sha,
        "shell": False,
    }
    if setup_log is not None:
        setup_log.parent.mkdir(parents=True, exist_ok=True)
        with setup_log.open("a", encoding="utf-8", newline="\n") as stream:
            stream.write(json.dumps(record, sort_keys=True) + "\n")
    if completed.returncode:
        raise RuntimeError(f"S0 runtime staging failed rc={completed.returncode}: {completed.stderr[:1000]}")
    try:
        receipt = json.loads(completed.stdout.strip())
    except json.JSONDecodeError as exc:
        raise RuntimeError("S0 staging did not return its bounded JSON receipt") from exc
    expected = {
        "kind": "S0_STAGE_RECEIPT",
        "stage_dir": stage_dir,
        "worker": f"{stage_dir.rstrip('/')}/worker.py",
        "worker_sha256": worker_sha,
        "launcher": f"{stage_dir.rstrip('/')}/s0_launcher.py",
        "launcher_sha256": launcher_sha,
        "collision_policy": "O_EXCL_NO_OVERWRITE",
    }
    if receipt != expected:
        raise RuntimeError(f"S0 staging receipt mismatch: expected={expected!r}, actual={receipt!r}")
    return StagedRuntime(
        stage_dir=stage_dir,
        worker=receipt["worker"],
        worker_sha256=worker_sha,
        launcher=receipt["launcher"],
        launcher_sha256=launcher_sha,
        stage_receipt=receipt,
    )


def stage_s1_runtime(
    distro: str,
    local_worker: Path,
    stage_dir: str,
    helper_dir: str,
    attempt_id: str,
    plan: Path,
    fixture_manifest: Path,
    fixture_root: Path,
    helper_source: Path,
    setup_log: Path | None = None,
    *,
    local_launcher: Path | None = None,
) -> StagedRuntime:
    launcher = (local_launcher or Path(__file__).with_name("s0_launcher.py")).resolve()
    worker = local_worker.resolve()
    plan = plan.resolve()
    fixture_manifest = fixture_manifest.resolve()
    fixture_root = fixture_root.resolve()
    helper_source = helper_source.resolve()
    hashes = {
        "worker": sha256_file(worker),
        "launcher": sha256_file(launcher),
        "plan": sha256_file(plan),
        "fixture_manifest": sha256_file(fixture_manifest),
        "helper": sha256_file(helper_source),
    }
    inner_argv = [
        "/usr/bin/python3", _windows_c_to_wsl(launcher), "stage-s1",
        "--stage-dir", stage_dir,
        "--helper-dir", helper_dir,
        "--attempt-id", attempt_id,
        "--worker-source", _windows_c_to_wsl(worker),
        "--worker-sha256", hashes["worker"],
        "--launcher-source", _windows_c_to_wsl(launcher),
        "--launcher-sha256", hashes["launcher"],
        "--plan-source", _windows_c_to_wsl(plan),
        "--plan-sha256", hashes["plan"],
        "--fixture-manifest-source", _windows_c_to_wsl(fixture_manifest),
        "--fixture-manifest-sha256", hashes["fixture_manifest"],
        "--fixture-root-source", _windows_c_to_wsl(fixture_root),
        "--helper-source", _windows_c_to_wsl(helper_source),
        "--helper-sha256", hashes["helper"],
    ]
    command = ["wsl.exe", "-d", distro, "--", *inner_argv]
    started = time.perf_counter_ns()
    completed = subprocess.run(
        command,
        stdin=subprocess.DEVNULL,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        timeout=15,
        check=False,
        env={key: os.environ[key] for key in ("SystemRoot", "WINDIR", "PATH") if key in os.environ},
    )
    record = {
        "kind": "WSL_SETUP_STAGE_S1_RUNTIME",
        "argv": command,
        "inner_argv": inner_argv,
        "return_code": completed.returncode,
        "stdout": completed.stdout[:16384],
        "stderr": completed.stderr[:16384],
        "stdout_truncated": len(completed.stdout) > 16384,
        "stderr_truncated": len(completed.stderr) > 16384,
        "start_ns": started,
        "end_ns": time.perf_counter_ns(),
        "clock_domain": "HOST_PERF_COUNTER_NS",
        "stage_dir": stage_dir,
        "helper_dir": helper_dir,
        "attempt_id": attempt_id,
        "source_hashes": hashes,
        "shell": False,
    }
    if setup_log is not None:
        setup_log.parent.mkdir(parents=True, exist_ok=True)
        with setup_log.open("a", encoding="utf-8", newline="\n") as stream:
            stream.write(json.dumps(record, sort_keys=True) + "\n")
    if completed.returncode:
        raise RuntimeError(f"S1 runtime staging failed rc={completed.returncode}: {completed.stderr[:1000]}")
    try:
        receipt = json.loads(completed.stdout.strip())
    except json.JSONDecodeError as exc:
        raise RuntimeError("S1 staging did not return its bounded JSON receipt") from exc
    exact = {
        "kind": "S1_STAGE_RECEIPT",
        "attempt_id": attempt_id,
        "stage_dir": stage_dir,
        "helper_dir": helper_dir,
        "worker": f"{stage_dir.rstrip('/')}/worker.py",
        "worker_sha256": hashes["worker"],
        "launcher": f"{stage_dir.rstrip('/')}/s0_launcher.py",
        "launcher_sha256": hashes["launcher"],
        "plan": f"{stage_dir.rstrip('/')}/S1_ACCESS_PLAN.json",
        "plan_sha256": hashes["plan"],
        "fixture_manifest": f"{stage_dir.rstrip('/')}/S1_FIXTURE_MANIFEST.json",
        "fixture_manifest_sha256": hashes["fixture_manifest"],
        "helper": f"{helper_dir.rstrip('/')}/s1_endpoint_helper.py",
        "helper_sha256": hashes["helper"],
        "collision_policy": "O_EXCL_NO_OVERWRITE",
    }
    for key, expected in exact.items():
        if receipt.get(key) != expected:
            raise RuntimeError(f"S1 staging receipt mismatch for {key}: expected={expected!r}, actual={receipt.get(key)!r}")
    if not isinstance(receipt.get("staged_fixtures"), list):
        raise RuntimeError("S1 staging receipt lacks bounded fixture list")
    return StagedRuntime(
        stage_dir=stage_dir,
        worker=receipt["worker"],
        worker_sha256=hashes["worker"],
        launcher=receipt["launcher"],
        launcher_sha256=hashes["launcher"],
        stage_receipt=receipt,
        mode="S1",
        s1_plan=receipt["plan"],
        s1_plan_sha256=hashes["plan"],
        s1_fixture_manifest=receipt["fixture_manifest"],
        s1_fixture_manifest_sha256=hashes["fixture_manifest"],
        s1_attempt_id=attempt_id,
        helper_dir=helper_dir,
        helper=receipt["helper"],
        helper_sha256=hashes["helper"],
    )


def stage_s2_runtime(
    distro: str,
    local_worker: Path,
    stage_dir: str,
    attempt_id: str,
    worker_role: str,
    plan: Path,
    fixture_manifest: Path,
    fixture_root: Path,
    setup_log: Path | None = None,
    *,
    local_launcher: Path | None = None,
) -> StagedRuntime:
    if worker_role not in {"W0", "W1"}:
        raise ValueError("S2 worker role must be W0 or W1")
    launcher = (local_launcher or Path(__file__).with_name("s0_launcher.py")).resolve()
    worker = local_worker.resolve()
    plan = plan.resolve()
    fixture_manifest = fixture_manifest.resolve()
    fixture_root = fixture_root.resolve()
    hashes = {
        "worker": sha256_file(worker),
        "launcher": sha256_file(launcher),
        "plan": sha256_file(plan),
        "fixture_manifest": sha256_file(fixture_manifest),
    }
    inner_argv = [
        "/usr/bin/python3", _windows_c_to_wsl(launcher), "stage-s2",
        "--stage-dir", stage_dir,
        "--attempt-id", attempt_id,
        "--worker-role", worker_role,
        "--worker-source", _windows_c_to_wsl(worker),
        "--worker-sha256", hashes["worker"],
        "--launcher-source", _windows_c_to_wsl(launcher),
        "--launcher-sha256", hashes["launcher"],
        "--plan-source", _windows_c_to_wsl(plan),
        "--plan-sha256", hashes["plan"],
        "--fixture-manifest-source", _windows_c_to_wsl(fixture_manifest),
        "--fixture-manifest-sha256", hashes["fixture_manifest"],
        "--fixture-root-source", _windows_c_to_wsl(fixture_root),
    ]
    command = ["wsl.exe", "-d", distro, "--", *inner_argv]
    started = time.perf_counter_ns()
    completed = subprocess.run(
        command,
        stdin=subprocess.DEVNULL,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        timeout=15,
        check=False,
        env={key: os.environ[key] for key in ("SystemRoot", "WINDIR", "PATH") if key in os.environ},
    )
    record = {
        "kind": "WSL_SETUP_STAGE_S2_RUNTIME",
        "argv": command,
        "inner_argv": inner_argv,
        "return_code": completed.returncode,
        "stdout": completed.stdout[:16384],
        "stderr": completed.stderr[:16384],
        "stdout_truncated": len(completed.stdout) > 16384,
        "stderr_truncated": len(completed.stderr) > 16384,
        "start_ns": started,
        "end_ns": time.perf_counter_ns(),
        "clock_domain": "HOST_PERF_COUNTER_NS",
        "stage_dir": stage_dir,
        "attempt_id": attempt_id,
        "worker_role": worker_role,
        "source_hashes": hashes,
        "shell": False,
    }
    if setup_log is not None:
        setup_log.parent.mkdir(parents=True, exist_ok=True)
        with setup_log.open("a", encoding="utf-8", newline="\n") as stream:
            stream.write(json.dumps(record, sort_keys=True) + "\n")
    if completed.returncode:
        raise RuntimeError(f"S2 runtime staging failed rc={completed.returncode}: {completed.stderr[:1000]}")
    try:
        receipt = json.loads(completed.stdout.strip())
    except json.JSONDecodeError as exc:
        raise RuntimeError("S2 staging did not return its bounded JSON receipt") from exc
    exact = {
        "kind": "S2_STAGE_RECEIPT",
        "attempt_id": attempt_id,
        "worker_role": worker_role,
        "stage_dir": stage_dir,
        "worker": f"{stage_dir.rstrip('/')}/worker.py",
        "worker_sha256": hashes["worker"],
        "launcher": f"{stage_dir.rstrip('/')}/s0_launcher.py",
        "launcher_sha256": hashes["launcher"],
        "plan": f"{stage_dir.rstrip('/')}/S2_DELTA_PLAN.json",
        "plan_sha256": hashes["plan"],
        "fixture_manifest": f"{stage_dir.rstrip('/')}/S2_FIXTURE_MANIFEST.json",
        "fixture_manifest_sha256": hashes["fixture_manifest"],
        "collision_policy": "O_EXCL_NO_OVERWRITE",
    }
    for key, expected in exact.items():
        if receipt.get(key) != expected:
            raise RuntimeError(f"S2 staging receipt mismatch for {key}: expected={expected!r}, actual={receipt.get(key)!r}")
    if not isinstance(receipt.get("staged_fixtures"), list):
        raise RuntimeError("S2 staging receipt lacks bounded fixture list")
    return StagedRuntime(
        stage_dir=stage_dir,
        worker=receipt["worker"],
        worker_sha256=hashes["worker"],
        launcher=receipt["launcher"],
        launcher_sha256=hashes["launcher"],
        stage_receipt=receipt,
        mode="S2",
        s2_plan=receipt["plan"],
        s2_plan_sha256=hashes["plan"],
        s2_fixture_manifest=receipt["fixture_manifest"],
        s2_fixture_manifest_sha256=hashes["fixture_manifest"],
        s2_attempt_id=attempt_id,
        s2_worker_role=worker_role,
    )
