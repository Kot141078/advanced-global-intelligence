from __future__ import annotations

"""Direct-argv staging and trusted Linux child waiter for bounded S0/S1/S2 runs."""

import argparse
import base64
import ctypes
import errno
import hashlib
import json
import os
import select
import shutil
import signal
import subprocess
import sys
import time
from pathlib import Path, PurePosixPath
from typing import Any

MAX_COPY_BYTES = 2 * 1024 * 1024
MAX_DIAGNOSTIC_CHARS = 4096
MAX_WORKER_STDERR_BYTES = 64 * 1024
STAGE_PREFIXES = ("/tmp/cgdr-r1-6g-s0-", "/tmp/cgdr-r1-6h-s1-", "/tmp/cgdr-r1-6i-s2-w0-", "/tmp/cgdr-r1-6i-s2-w1-")
HELPER_PREFIX = "/tmp/cgdr-r1-6h-helper-"
RECEIPT_CHANNEL = "PARENT_ONLY_STDERR_V1"


def _emit_stderr(value: dict[str, Any]) -> None:
    sys.stderr.write(json.dumps(value, sort_keys=True, separators=(",", ":")) + "\n")
    sys.stderr.flush()


def _emit_receipt(payload: dict[str, Any]) -> None:
    _emit_stderr({"record_type": "TRUSTED_PARENT_RECEIPT", "receipt_channel": RECEIPT_CHANNEL, "payload": payload})


def _emit_worker_stderr(raw: bytes, *, truncated: bool = False) -> None:
    _emit_stderr({
        "record_type": "WORKER_STDERR_DATA",
        "source_channel": "DEDICATED_CHILD_STDERR_PIPE",
        "payload_b64": base64.b64encode(raw).decode("ascii"),
        "truncated": truncated,
    })


def _emit_stdout(value: dict[str, Any]) -> None:
    sys.stdout.write(json.dumps(value, sort_keys=True, separators=(",", ":")) + "\n")
    sys.stdout.flush()


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    total = 0
    with path.open("rb") as stream:
        while True:
            chunk = stream.read(65536)
            if not chunk:
                break
            total += len(chunk)
            if total > MAX_COPY_BYTES:
                raise ValueError(f"file exceeds {MAX_COPY_BYTES} byte staging ceiling: {path}")
            digest.update(chunk)
    return digest.hexdigest()


def _single_file_snapshot(path: Path) -> dict[str, Any]:
    try:
        metadata = path.lstat()
    except FileNotFoundError:
        return {"exists": False}
    if path.is_symlink() or not path.is_file():
        return {"exists": True, "regular_file": False, "mode": oct(metadata.st_mode & 0o777)}
    return {
        "exists": True,
        "regular_file": True,
        "bytes": metadata.st_size,
        "mode": oct(metadata.st_mode & 0o777),
        "sha256": _sha256(path),
    }


def _validate_prefixed_dir(value: str, prefixes: tuple[str, ...]) -> Path:
    if not any(value.startswith(prefix) for prefix in prefixes):
        raise ValueError(f"directory is outside task-local prefixes: {value}")
    path = Path(value)
    if not path.is_absolute() or ".." in path.parts:
        raise ValueError("directory must be an absolute normalized task-local path")
    return path


def _validate_stage_dir(value: str) -> Path:
    return _validate_prefixed_dir(value, STAGE_PREFIXES)


def _validate_helper_dir(value: str) -> Path:
    return _validate_prefixed_dir(value, (HELPER_PREFIX,))


def _safe_relative(value: str) -> Path:
    pure = PurePosixPath(value)
    if pure.is_absolute() or not pure.parts or any(part in ("", ".", "..") for part in pure.parts):
        raise ValueError(f"unsafe fixture relative path: {value!r}")
    return Path(*pure.parts)


def _copy_exclusive(source: Path, target: Path, expected_sha256: str, mode: int = 0o400) -> None:
    if not source.is_file() or source.is_symlink():
        raise ValueError(f"staging source is not a regular non-symlink file: {source}")
    actual = _sha256(source)
    if actual != expected_sha256:
        raise ValueError(f"source hash mismatch for {source}: {actual}")
    target.parent.mkdir(parents=True, exist_ok=True, mode=0o700)
    flags = os.O_WRONLY | os.O_CREAT | os.O_EXCL | getattr(os, "O_NOFOLLOW", 0)
    source_fd = os.open(source, os.O_RDONLY | getattr(os, "O_NOFOLLOW", 0))
    try:
        target_fd = os.open(target, flags, mode)
        try:
            total = 0
            while True:
                chunk = os.read(source_fd, 65536)
                if not chunk:
                    break
                total += len(chunk)
                if total > MAX_COPY_BYTES:
                    raise ValueError("staging source exceeded bounded copy ceiling")
                view = memoryview(chunk)
                while view:
                    written = os.write(target_fd, view)
                    view = view[written:]
            os.fsync(target_fd)
        finally:
            os.close(target_fd)
    finally:
        os.close(source_fd)
    os.chmod(target, mode)
    if _sha256(target) != expected_sha256:
        raise ValueError(f"staged target hash mismatch: {target}")


def stage(args: argparse.Namespace) -> int:
    stage_dir = _validate_stage_dir(args.stage_dir)
    os.mkdir(stage_dir, 0o700)
    worker_target = stage_dir / "worker.py"
    launcher_target = stage_dir / "s0_launcher.py"
    _copy_exclusive(Path(args.worker_source), worker_target, args.worker_sha256, 0o500)
    _copy_exclusive(Path(args.launcher_source), launcher_target, args.launcher_sha256, 0o500)
    _emit_stdout({
        "kind": "S0_STAGE_RECEIPT", "stage_dir": str(stage_dir), "worker": str(worker_target),
        "worker_sha256": _sha256(worker_target), "launcher": str(launcher_target),
        "launcher_sha256": _sha256(launcher_target), "collision_policy": "O_EXCL_NO_OVERWRITE",
    })
    return 0


def stage_s1(args: argparse.Namespace) -> int:
    stage_dir = _validate_stage_dir(args.stage_dir)
    helper_dir = _validate_helper_dir(args.helper_dir)
    os.mkdir(stage_dir, 0o700)
    os.mkdir(helper_dir, 0o700)
    worker_target = stage_dir / "worker.py"
    launcher_target = stage_dir / "s0_launcher.py"
    plan_target = stage_dir / "S1_ACCESS_PLAN.json"
    manifest_target = stage_dir / "S1_FIXTURE_MANIFEST.json"
    helper_target = helper_dir / "s1_endpoint_helper.py"
    _copy_exclusive(Path(args.worker_source), worker_target, args.worker_sha256, 0o500)
    _copy_exclusive(Path(args.launcher_source), launcher_target, args.launcher_sha256, 0o500)
    _copy_exclusive(Path(args.plan_source), plan_target, args.plan_sha256, 0o400)
    _copy_exclusive(Path(args.fixture_manifest_source), manifest_target, args.fixture_manifest_sha256, 0o400)
    _copy_exclusive(Path(args.helper_source), helper_target, args.helper_sha256, 0o500)
    manifest = json.loads(manifest_target.read_text(encoding="utf-8"))
    if manifest.get("task_id") != "CGDR_SELECTED_PROCESS_ACCESS_BOUNDARY_S1_R1_6H" or manifest.get("attempt_id") != args.attempt_id:
        raise ValueError("fixture manifest task/attempt binding mismatch")
    files = manifest.get("files")
    if not isinstance(files, list) or not files or len(files) > 32:
        raise ValueError("fixture manifest file list is invalid")
    seen: set[str] = set()
    staged_fixtures: list[dict[str, Any]] = []
    root = Path(args.fixture_root_source)
    for entry in files:
        if not isinstance(entry, dict):
            raise ValueError("fixture entry must be an object")
        relative_text = entry.get("relative_path")
        if not isinstance(relative_text, str) or relative_text.casefold() in seen:
            raise ValueError("duplicate or invalid fixture relative path")
        seen.add(relative_text.casefold())
        relative = _safe_relative(relative_text)
        expected_sha = entry.get("sha256")
        expected_bytes = entry.get("bytes")
        if not isinstance(expected_sha, str) or not isinstance(expected_bytes, int):
            raise ValueError("fixture hash/size binding missing")
        source = root / relative
        if entry.get("destination") == "STAGE":
            target = stage_dir / relative
        elif entry.get("destination") == "HELPER" and relative.parts[0] == "parent_service":
            target = helper_dir.joinpath(*relative.parts[1:])
        else:
            raise ValueError(f"unsupported fixture destination: {entry.get('destination')!r}")
        _copy_exclusive(source, target, expected_sha, int(str(entry.get("mode", "0400")), 8))
        if target.stat().st_size != expected_bytes:
            raise ValueError(f"fixture byte count mismatch: {relative_text}")
        staged_fixtures.append({"relative_path": relative_text, "destination": str(target), "bytes": expected_bytes, "sha256": expected_sha})
    (stage_dir / "scratch").mkdir(mode=0o700)
    if not (stage_dir / "private").is_dir() or not (stage_dir / "trusted").is_dir():
        raise ValueError("required private/trusted fixture directories are missing")
    receipt = {
        "kind": "S1_STAGE_RECEIPT", "attempt_id": args.attempt_id, "stage_dir": str(stage_dir),
        "helper_dir": str(helper_dir), "worker": str(worker_target), "worker_sha256": _sha256(worker_target),
        "launcher": str(launcher_target), "launcher_sha256": _sha256(launcher_target),
        "plan": str(plan_target), "plan_sha256": _sha256(plan_target),
        "fixture_manifest": str(manifest_target), "fixture_manifest_sha256": _sha256(manifest_target),
        "helper": str(helper_target), "helper_sha256": _sha256(helper_target),
        "staged_fixtures": staged_fixtures, "collision_policy": "O_EXCL_NO_OVERWRITE",
    }
    _emit_stdout(receipt)
    return 0


def stage_s2(args: argparse.Namespace) -> int:
    stage_dir = _validate_stage_dir(args.stage_dir)
    role = str(args.worker_role)
    if role not in {"W0", "W1"} or not str(stage_dir).startswith(f"/tmp/cgdr-r1-6i-s2-{role.casefold()}-"):
        raise ValueError("S2 stage directory/role binding mismatch")
    os.mkdir(stage_dir, 0o700)
    worker_target = stage_dir / "worker.py"
    launcher_target = stage_dir / "s0_launcher.py"
    plan_target = stage_dir / "S2_DELTA_PLAN.json"
    manifest_target = stage_dir / "S2_FIXTURE_MANIFEST.json"
    _copy_exclusive(Path(args.worker_source), worker_target, args.worker_sha256, 0o500)
    _copy_exclusive(Path(args.launcher_source), launcher_target, args.launcher_sha256, 0o500)
    _copy_exclusive(Path(args.plan_source), plan_target, args.plan_sha256, 0o400)
    _copy_exclusive(Path(args.fixture_manifest_source), manifest_target, args.fixture_manifest_sha256, 0o400)
    manifest = json.loads(manifest_target.read_text(encoding="utf-8"))
    if (
        manifest.get("schema") != "S2_FIXTURE_MANIFEST_V1"
        or manifest.get("task_id") != "CGDR_SELECTED_PROCESS_OPEN_STATE_HANDOFF_S2_R1_6I"
        or manifest.get("attempt_id") != args.attempt_id
        or manifest.get("worker_role") != role
    ):
        raise ValueError("S2 fixture manifest binding mismatch")
    files = manifest.get("files")
    if not isinstance(files, list) or not files or len(files) > 16:
        raise ValueError("S2 fixture manifest file list is invalid")
    root = Path(args.fixture_root_source)
    seen: set[str] = set()
    staged_fixtures: list[dict[str, Any]] = []
    for entry in files:
        if not isinstance(entry, dict):
            raise ValueError("S2 fixture entry must be an object")
        relative_text = entry.get("relative_path")
        if not isinstance(relative_text, str) or relative_text.casefold() in seen:
            raise ValueError("duplicate or invalid S2 fixture relative path")
        seen.add(relative_text.casefold())
        relative = _safe_relative(relative_text)
        expected_sha, expected_bytes = entry.get("sha256"), entry.get("bytes")
        if not isinstance(expected_sha, str) or not isinstance(expected_bytes, int) or entry.get("destination") != "STAGE":
            raise ValueError("S2 fixture binding missing or destination invalid")
        source, target = root / relative, stage_dir / relative
        _copy_exclusive(source, target, expected_sha, int(str(entry.get("mode", "0400")), 8))
        if target.stat().st_size != expected_bytes:
            raise ValueError(f"S2 fixture byte count mismatch: {relative_text}")
        staged_fixtures.append({"relative_path": relative_text, "destination": str(target), "bytes": expected_bytes, "sha256": expected_sha})
    (stage_dir / "scratch").mkdir(mode=0o700)
    if not (stage_dir / "private").is_dir():
        raise ValueError("required S2 private fixture directory is missing")
    _emit_stdout({
        "kind": "S2_STAGE_RECEIPT",
        "attempt_id": args.attempt_id,
        "worker_role": role,
        "stage_dir": str(stage_dir),
        "worker": str(worker_target),
        "worker_sha256": _sha256(worker_target),
        "launcher": str(launcher_target),
        "launcher_sha256": _sha256(launcher_target),
        "plan": str(plan_target),
        "plan_sha256": _sha256(plan_target),
        "fixture_manifest": str(manifest_target),
        "fixture_manifest_sha256": _sha256(manifest_target),
        "staged_fixtures": staged_fixtures,
        "collision_policy": "O_EXCL_NO_OVERWRITE",
    })
    return 0


def snapshot_s1(args: argparse.Namespace) -> int:
    stage_dir = _validate_stage_dir(args.stage_dir)
    helper_dir = _validate_helper_dir(args.helper_dir)
    plan_path = Path(args.plan)
    if plan_path != stage_dir / "S1_ACCESS_PLAN.json" or _sha256(plan_path) != args.plan_sha256:
        raise ValueError("snapshot plan path/hash binding mismatch")
    plan = json.loads(plan_path.read_text(encoding="utf-8"))
    if plan.get("attempt_id") != args.attempt_id or plan.get("stage_dir") != str(stage_dir):
        raise ValueError("snapshot plan attempt/stage mismatch")
    if (plan.get("endpoint_binding") or {}).get("helper_dir") != str(helper_dir):
        raise ValueError("snapshot helper binding mismatch")
    paths: dict[str, dict[str, Any]] = {}
    for probe in plan.get("probes", []):
        if probe.get("operation") not in {"FILE_READ", "FILE_APPEND"}:
            continue
        target = str(probe.get("target", ""))
        if not (target.startswith(str(stage_dir) + "/") or target.startswith(str(helper_dir) + "/")):
            raise ValueError("snapshot target outside frozen roots")
        paths[target] = _single_file_snapshot(Path(target))
    helper_log = helper_dir / "helper_events.jsonl"
    helper_events: list[Any] = []
    if args.include_helper_log and helper_log.is_file():
        if helper_log.stat().st_size > 65536:
            raise ValueError("helper log exceeds bounded read ceiling")
        helper_events = [json.loads(line) for line in helper_log.read_text(encoding="utf-8").splitlines() if line.strip()]
    _emit_stdout({
        "kind": "S1_TRUSTED_OUTER_SNAPSHOT",
        "attempt_id": args.attempt_id,
        "stage_dir": str(stage_dir),
        "helper_dir": str(helper_dir),
        "paths": paths,
        "helper_events": helper_events,
        "snapshot_source": "TRUSTED_LAUNCHER_OUTSIDE_WORKER_NAMESPACES",
    })
    return 0


def _proc_start_ticks(pid: int) -> int:
    return int(Path(f"/proc/{pid}/stat").read_text(encoding="ascii").split()[21])


def _namespace_identity(pid: int, kind: str) -> str:
    return os.readlink(f"/proc/{pid}/ns/{kind}")


def _run_mount(command: list[str]) -> None:
    completed = subprocess.run(command, stdin=subprocess.DEVNULL, capture_output=True, timeout=5, check=False)
    if completed.returncode:
        stderr = completed.stderr.decode("utf-8", errors="replace")[:MAX_DIAGNOSTIC_CHARS]
        raise RuntimeError(f"isolation mount failed rc={completed.returncode} argv={command!r}: {stderr}")


def _mount_isolation(args: argparse.Namespace) -> list[list[str]]:
    mount = shutil.which("mount")
    if not mount:
        raise RuntimeError("mount binary unavailable in isolated namespace")
    commands = [[mount, "--make-rprivate", "/"]]
    for target in ("/home", "/root", "/mnt"):
        commands.append([mount, "-t", "tmpfs", "-o", "mode=000,nosuid,nodev,noexec", "tmpfs", target])
    if args.s1_mode or args.s2_mode:
        stage_dir = _validate_stage_dir(args.stage_dir)
        helper_dir = _validate_helper_dir(args.endpoint_mask_dir) if args.s1_mode else None
        scratch = Path(args.s1_scratch if args.s1_mode else args.s2_scratch)
        private = Path(args.s1_private if args.s1_mode else args.s2_private)
        if scratch != stage_dir / "scratch" or private != stage_dir / "private":
            raise ValueError("private/scratch mount binding mismatch")
        paths = (stage_dir, scratch, private) if helper_dir is None else (stage_dir, helper_dir, scratch, private)
        for path in paths:
            if not path.is_dir() or path.is_symlink():
                raise ValueError(f"bounded mount target is not a real directory: {path}")
        commands.extend([
            [mount, "--bind", str(stage_dir), str(stage_dir)],
            [mount, "-o", "remount,bind,ro,nosuid,nodev", str(stage_dir)],
            [mount, "-t", "tmpfs", "-o", "mode=700,nosuid,nodev,noexec", "tmpfs", str(scratch)],
            [mount, "-t", "tmpfs", "-o", "mode=000,nosuid,nodev,noexec", "tmpfs", str(private)],
        ])
        if helper_dir is not None:
            commands.append([mount, "-t", "tmpfs", "-o", "mode=000,nosuid,nodev,noexec", "tmpfs", str(helper_dir)])
    for command in commands:
        _run_mount(command)
    return commands


def _set_parent_death_signal() -> bool:
    try:
        libc = ctypes.CDLL(None, use_errno=True)
        return libc.prctl(1, signal.SIGKILL, 0, 0, 0) == 0
    except BaseException:
        return False


class _CapHeader(ctypes.Structure):
    _fields_ = [("version", ctypes.c_uint32), ("pid", ctypes.c_int)]


class _CapData(ctypes.Structure):
    _fields_ = [("effective", ctypes.c_uint32), ("permitted", ctypes.c_uint32), ("inheritable", ctypes.c_uint32)]


def _prctl(libc: Any, option: int, arg2: int = 0) -> None:
    if libc.prctl(option, arg2, 0, 0, 0) != 0:
        code = ctypes.get_errno()
        raise OSError(code, os.strerror(code))


def _apply_child_hardening() -> None:
    libc = ctypes.CDLL(None, use_errno=True)
    _prctl(libc, 38, 1)
    _prctl(libc, 28, 1 | 2 | 4 | 8 | 64 | 128)
    last_cap = int(Path("/proc/sys/kernel/cap_last_cap").read_text(encoding="ascii").strip())
    for cap in range(last_cap + 1):
        _prctl(libc, 24, cap)
    header = _CapHeader(0x20080522, 0)
    data = (_CapData * 2)()
    if libc.capset(ctypes.byref(header), ctypes.byref(data)) != 0:
        code = ctypes.get_errno()
        raise OSError(code, os.strerror(code))
    try:
        _prctl(libc, 47, 4)
    except OSError as exc:
        if exc.errno != errno.EINVAL:
            raise
    _prctl(libc, 4, 0)


def _close_extra_fds(keep: set[int]) -> None:
    for name in os.listdir("/proc/self/fd"):
        try:
            fd = int(name)
        except ValueError:
            continue
        if fd > 2 and fd not in keep:
            try:
                os.close(fd)
            except OSError:
                pass


def _pipe_cloexec() -> tuple[int, int]:
    if hasattr(os, "pipe2"):
        return os.pipe2(os.O_CLOEXEC)
    read_fd, write_fd = os.pipe()
    os.set_inheritable(read_fd, False)
    os.set_inheritable(write_fd, False)
    return read_fd, write_fd


def _await_exec(exec_fd: int, child_pid: int, timeout: float = 5.0) -> None:
    deadline = time.monotonic() + timeout
    collected = bytearray()
    while time.monotonic() < deadline:
        ready, _, _ = select.select([exec_fd], [], [], min(0.05, max(0.0, deadline - time.monotonic())))
        if not ready:
            waited, status = os.waitpid(child_pid, os.WNOHANG)
            if waited == child_pid:
                raise RuntimeError(f"child exited before exec receipt status={status}")
            continue
        chunk = os.read(exec_fd, 4096)
        if not chunk:
            return
        collected.extend(chunk)
        if len(collected) > MAX_DIAGNOSTIC_CHARS:
            raise RuntimeError("child exec diagnostic overflow")
    raise RuntimeError(f"child exec receipt timeout diagnostic={bytes(collected)!r}")


def _status_snapshot(pid: int) -> dict[str, Any]:
    wanted = {"Uid", "Gid", "Groups", "CapInh", "CapPrm", "CapEff", "CapBnd", "CapAmb", "NoNewPrivs", "Seccomp", "Seccomp_filters"}
    fields: dict[str, str] = {}
    for line in Path(f"/proc/{pid}/status").read_text(encoding="utf-8").splitlines():
        key, separator, value = line.partition(":")
        if separator and key in wanted:
            fields[key] = value.strip()
    fds = []
    for name in sorted(os.listdir(f"/proc/{pid}/fd"), key=int):
        try:
            target = os.readlink(f"/proc/{pid}/fd/{name}")
        except FileNotFoundError:
            continue
        fds.append({"fd": int(name), "target": target})
    return {"status_fields": fields, "fds": fds, "exe": os.readlink(f"/proc/{pid}/exe")}


def _settled_status_snapshot(pid: int, timeout: float = 2.0) -> dict[str, Any]:
    """Wait only for transient dynamic-loader FDs to close; never infer policy from a single early sample."""
    deadline = time.monotonic() + timeout
    observations: list[list[dict[str, Any]]] = []
    while True:
        snapshot = _status_snapshot(pid)
        fds = snapshot.get("fds") or []
        observations.append(fds)
        if [row.get("fd") for row in fds] == [0, 1, 2]:
            snapshot["fd_settlement_observations"] = observations[:32]
            snapshot["fd_settled"] = True
            return snapshot
        if time.monotonic() >= deadline:
            snapshot["fd_settlement_observations"] = observations[:32]
            snapshot["fd_settled"] = False
            return snapshot
        time.sleep(0.01)


def _mount_snapshot(pid: int, paths: list[str]) -> list[dict[str, Any]]:
    result: list[dict[str, Any]] = []
    for line in Path(f"/proc/{pid}/mountinfo").read_text(encoding="utf-8").splitlines():
        left, separator, right = line.partition(" - ")
        fields = left.split()
        if not separator or len(fields) < 6:
            continue
        mount_point = fields[4].replace("\\040", " ")
        if mount_point in paths:
            result.append({"mount_point": mount_point, "mount_options": fields[5].split(","), "optional_fields": fields[6:], "filesystem": right.split()[0] if right.split() else "UNKNOWN"})
    return result


def _forward_and_wait(child_pid: int, stderr_fd: int) -> tuple[int, int | None, int]:
    os.set_blocking(stderr_fd, False)
    wait_status: int | None = None
    total = 0
    kept = 0
    overflow_reported = False
    while wait_status is None:
        ready, _, _ = select.select([stderr_fd], [], [], 0.05)
        if ready:
            try:
                chunk = os.read(stderr_fd, 4096)
            except BlockingIOError:
                chunk = b""
            if chunk:
                total += len(chunk)
                remaining = MAX_WORKER_STDERR_BYTES - kept
                if remaining > 0:
                    forwarded = chunk[:remaining]
                    kept += len(forwarded)
                    _emit_worker_stderr(forwarded, truncated=len(chunk) > len(forwarded))
                elif not overflow_reported:
                    _emit_worker_stderr(b"", truncated=True)
                    overflow_reported = True
        waited_pid, status = os.waitpid(child_pid, os.WNOHANG)
        if waited_pid == child_pid:
            wait_status = status
    for _ in range(16):
        try:
            chunk = os.read(stderr_fd, 4096)
        except BlockingIOError:
            break
        if not chunk:
            break
        total += len(chunk)
        remaining = MAX_WORKER_STDERR_BYTES - kept
        if remaining > 0:
            forwarded = chunk[:remaining]
            kept += len(forwarded)
            _emit_worker_stderr(forwarded, truncated=len(chunk) > len(forwarded))
    os.close(stderr_fd)
    if os.WIFEXITED(wait_status):
        return os.WEXITSTATUS(wait_status), None, total
    if os.WIFSIGNALED(wait_status):
        signum = os.WTERMSIG(wait_status)
        return 128 + signum, signum, total
    return 125, None, total


def wait_for_worker(args: argparse.Namespace) -> int:
    stage_dir = _validate_stage_dir(args.stage_dir)
    worker = Path(args.worker)
    launcher = Path(args.launcher)
    if worker.parent != stage_dir or launcher.parent != stage_dir:
        raise ValueError("worker and launcher must be in the declared fresh stage directory")
    if _sha256(worker) != args.worker_sha256 or _sha256(launcher) != args.launcher_sha256:
        raise ValueError("staged worker/launcher hash verification failed")
    if args.s1_mode and args.s2_mode:
        raise ValueError("S1 and S2 modes are mutually exclusive")
    if args.s1_mode:
        plan = Path(args.s1_plan)
        manifest = Path(args.s1_fixture_manifest)
        if plan.parent != stage_dir or manifest.parent != stage_dir:
            raise ValueError("S1 plan/manifest must be in the declared stage")
        if _sha256(plan) != args.s1_plan_sha256 or _sha256(manifest) != args.s1_fixture_manifest_sha256:
            raise ValueError("S1 plan/fixture manifest hash verification failed")
    if args.s2_mode:
        plan = Path(args.s2_plan)
        manifest = Path(args.s2_fixture_manifest)
        if plan.parent != stage_dir or manifest.parent != stage_dir:
            raise ValueError("S2 plan/manifest must be in the declared stage")
        if _sha256(plan) != args.s2_plan_sha256 or _sha256(manifest) != args.s2_fixture_manifest_sha256:
            raise ValueError("S2 plan/fixture manifest hash verification failed")
    mount_commands = _mount_isolation(args)
    os.chdir("/tmp")
    barrier_r, barrier_w = os.pipe()
    stderr_r, stderr_w = os.pipe()
    exec_r, exec_w = _pipe_cloexec()
    child_pid = os.fork()
    if child_pid == 0:
        try:
            os.close(barrier_w); os.close(stderr_r); os.close(exec_r)
            os.dup2(stderr_w, 2)
            if stderr_w != 2:
                os.close(stderr_w)
            pdeathsig = _set_parent_death_signal()
            token = os.read(barrier_r, 1); os.close(barrier_r)
            if token != b"1":
                os._exit(126)
            _apply_child_hardening()
            _close_extra_fds({exec_w})
            environment = {"PATH": "/usr/bin:/bin", "LANG": "C.UTF-8", "PYTHONHASHSEED": "0", "CGDR_INSTANCE_ID": args.instance_id, "CGDR_PDEATHSIG_SET": "1" if pdeathsig else "0", "CGDR_S1_MODE": "1" if args.s1_mode else "0", "CGDR_S2_MODE": "1" if args.s2_mode else "0"}
            if args.s1_mode:
                environment.update({"CGDR_S1_PLAN": args.s1_plan, "CGDR_S1_PLAN_SHA256": args.s1_plan_sha256, "CGDR_S1_ATTEMPT_ID": args.s1_attempt_id})
            if args.s2_mode:
                environment.update({"CGDR_S2_PLAN": args.s2_plan, "CGDR_S2_PLAN_SHA256": args.s2_plan_sha256, "CGDR_S2_ATTEMPT_ID": args.s2_attempt_id, "CGDR_S2_WORKER_ROLE": args.s2_worker_role})
            os.execve("/usr/bin/python3", ["python3", "-u", str(worker)], environment)
        except BaseException as exc:
            try:
                os.write(exec_w, f"{type(exc).__name__}:{exc}".encode("utf-8", errors="replace")[:MAX_DIAGNOSTIC_CHARS])
            except BaseException:
                pass
            os._exit(127)
    os.close(barrier_r); os.close(stderr_w); os.close(exec_w)
    waiter_pid = os.getpid()
    try:
        child_start_ticks = _proc_start_ticks(child_pid)
        binding = {
            "marker": "CGDR_CHILD_BOUND", "binding_source": "TRUSTED_DIRECT_FORK_PARENT", "wait_source": "POSIX_WAITPID_CHILD",
            "receipt_channel": RECEIPT_CHANNEL, "instance_id": args.instance_id, "receipt_nonce": args.receipt_nonce,
            "worker_pid": child_pid, "worker_start_ticks": child_start_ticks, "waiter_pid": waiter_pid,
            "waiter_start_ticks": _proc_start_ticks(waiter_pid), "pid_namespace": _namespace_identity(child_pid, "pid"),
            "network_namespace": _namespace_identity(child_pid, "net"), "mount_namespace": _namespace_identity(child_pid, "mnt"),
            "worker_sha256": args.worker_sha256, "launcher_sha256": args.launcher_sha256, "stdin_fd": 0, "stdout_fd": 1,
            "worker_stderr_route": "DEDICATED_PIPE_WRAPPED_BY_TRUSTED_PARENT", "trusted_receipt_route": RECEIPT_CHANNEL,
            "mount_argv": mount_commands, "s1_mode": bool(args.s1_mode), "s2_mode": bool(args.s2_mode),
        }
        _emit_receipt(binding); os.write(barrier_w, b"1")
    except BaseException:
        try:
            os.kill(child_pid, signal.SIGKILL)
        except ProcessLookupError:
            pass
        raise
    finally:
        os.close(barrier_w)
    try:
        _await_exec(exec_r, child_pid)
    finally:
        os.close(exec_r)
    status = _settled_status_snapshot(child_pid)
    paths = ["/home", "/root", "/mnt"]
    if args.s1_mode:
        paths.extend([args.stage_dir, args.s1_scratch, args.s1_private, args.endpoint_mask_dir])
    if args.s2_mode:
        paths.extend([args.stage_dir, args.s2_scratch, args.s2_private])
    security = {
        "marker": "CGDR_CHILD_SECURITY", "binding_source": "TRUSTED_DIRECT_FORK_PARENT_POST_EXEC_PROCFS",
        "receipt_channel": RECEIPT_CHANNEL, "instance_id": args.instance_id, "receipt_nonce": args.receipt_nonce,
        "worker_pid": child_pid, "worker_start_ticks": child_start_ticks, "status": status,
        "mounts": _mount_snapshot(child_pid, paths), "pid_namespace": _namespace_identity(child_pid, "pid"),
        "network_namespace": _namespace_identity(child_pid, "net"), "mount_namespace": _namespace_identity(child_pid, "mnt"),
        "worker_stderr_route": "DEDICATED_PIPE_WRAPPED_BY_TRUSTED_PARENT", "trusted_receipt_route": RECEIPT_CHANNEL,
    }
    security_sha = hashlib.sha256(json.dumps(security, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
    security["security_receipt_sha256"] = security_sha
    _emit_receipt(security)
    return_code, signal_number, stderr_total = _forward_and_wait(child_pid, stderr_r)
    scratch_snapshot = _single_file_snapshot(Path(args.s1_scratch) / "allowed_write.bin") if args.s1_mode else None
    s2_scratch_snapshot = _single_file_snapshot(Path(args.s2_scratch) / f"{args.s2_worker_role.casefold()}_allowed.bin") if args.s2_mode else None
    _emit_receipt({
        "marker": "CGDR_INNER_EXIT", "binding_source": "TRUSTED_DIRECT_FORK_PARENT", "wait_source": "POSIX_WAITPID_CHILD",
        "receipt_channel": RECEIPT_CHANNEL, "instance_id": args.instance_id, "receipt_nonce": args.receipt_nonce,
        "worker_pid": child_pid, "worker_start_ticks": child_start_ticks, "waiter_pid": waiter_pid,
        "waiter_start_ticks": binding["waiter_start_ticks"], "pid_namespace": binding["pid_namespace"],
        "network_namespace": binding["network_namespace"], "mount_namespace": binding["mount_namespace"],
        "worker_sha256": args.worker_sha256, "launcher_sha256": args.launcher_sha256,
        "security_receipt_sha256": security_sha, "worker_stderr_total_bytes": stderr_total,
        "s1_scratch_snapshot": scratch_snapshot,
        "s2_scratch_snapshot": s2_scratch_snapshot,
        "return_code": return_code, "signal": signal_number,
    })
    return return_code


def wait_for_helper(args: argparse.Namespace) -> int:
    helper_dir = _validate_helper_dir(args.helper_dir)
    helper = Path(args.helper)
    if helper.parent != helper_dir or _sha256(helper) != args.helper_sha256:
        raise ValueError("helper path/hash binding failed")
    barrier_r, barrier_w = os.pipe(); stderr_r, stderr_w = os.pipe(); exec_r, exec_w = _pipe_cloexec()
    child_pid = os.fork()
    if child_pid == 0:
        try:
            os.close(barrier_w); os.close(stderr_r); os.close(exec_r); os.dup2(stderr_w, 2)
            if stderr_w != 2:
                os.close(stderr_w)
            _set_parent_death_signal()
            if os.read(barrier_r, 1) != b"1":
                os._exit(126)
            os.close(barrier_r); _close_extra_fds({exec_w})
            environment = {"PATH": "/usr/bin:/bin", "LANG": "C.UTF-8", "PYTHONHASHSEED": "0"}
            argv = ["python3", "-u", str(helper), "serve", "--helper-dir", str(helper_dir), "--tcp-port", str(args.tcp_port), "--instance-id", args.instance_id]
            os.execve("/usr/bin/python3", argv, environment)
        except BaseException as exc:
            try:
                os.write(exec_w, f"{type(exc).__name__}:{exc}".encode("utf-8", errors="replace")[:MAX_DIAGNOSTIC_CHARS])
            except BaseException:
                pass
            os._exit(127)
    os.close(barrier_r); os.close(stderr_w); os.close(exec_w)
    start_ticks = _proc_start_ticks(child_pid)
    binding = {
        "marker": "CGDR_HELPER_BOUND", "binding_source": "TRUSTED_DIRECT_FORK_PARENT", "wait_source": "POSIX_WAITPID_CHILD",
        "receipt_channel": RECEIPT_CHANNEL, "instance_id": args.instance_id, "receipt_nonce": args.receipt_nonce,
        "helper_pid": child_pid, "helper_start_ticks": start_ticks, "waiter_pid": os.getpid(),
        "waiter_start_ticks": _proc_start_ticks(os.getpid()), "pid_namespace": _namespace_identity(child_pid, "pid"),
        "network_namespace": _namespace_identity(child_pid, "net"), "mount_namespace": _namespace_identity(child_pid, "mnt"),
        "helper_sha256": args.helper_sha256,
    }
    _emit_receipt(binding); os.write(barrier_w, b"1"); os.close(barrier_w)
    try:
        _await_exec(exec_r, child_pid)
    finally:
        os.close(exec_r)
    return_code, signal_number, stderr_total = _forward_and_wait(child_pid, stderr_r)
    _emit_receipt({**binding, "marker": "CGDR_HELPER_EXIT", "worker_stderr_total_bytes": stderr_total, "return_code": return_code, "signal": signal_number})
    return return_code


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Direct-argv staging and trusted child waiter")
    subparsers = parser.add_subparsers(dest="subcommand", required=True)
    stage_parser = subparsers.add_parser("stage")
    for name in ("stage_dir", "worker_source", "worker_sha256", "launcher_source", "launcher_sha256"):
        stage_parser.add_argument("--" + name.replace("_", "-"), required=True)
    stage_parser.set_defaults(handler=stage)
    s1_parser = subparsers.add_parser("stage-s1")
    for name in ("stage_dir", "helper_dir", "attempt_id", "worker_source", "worker_sha256", "launcher_source", "launcher_sha256", "plan_source", "plan_sha256", "fixture_manifest_source", "fixture_manifest_sha256", "fixture_root_source", "helper_source", "helper_sha256"):
        s1_parser.add_argument("--" + name.replace("_", "-"), required=True)
    s1_parser.set_defaults(handler=stage_s1)
    s2_parser = subparsers.add_parser("stage-s2")
    for name in ("stage_dir", "attempt_id", "worker_role", "worker_source", "worker_sha256", "launcher_source", "launcher_sha256", "plan_source", "plan_sha256", "fixture_manifest_source", "fixture_manifest_sha256", "fixture_root_source"):
        s2_parser.add_argument("--" + name.replace("_", "-"), required=True)
    s2_parser.set_defaults(handler=stage_s2)
    snapshot_parser = subparsers.add_parser("snapshot-s1")
    for name in ("stage_dir", "helper_dir", "attempt_id", "plan", "plan_sha256"):
        snapshot_parser.add_argument("--" + name.replace("_", "-"), required=True)
    snapshot_parser.add_argument("--include-helper-log", action="store_true")
    snapshot_parser.set_defaults(handler=snapshot_s1)
    wait_parser = subparsers.add_parser("wait")
    for name in ("stage_dir", "worker", "worker_sha256", "launcher", "launcher_sha256", "instance_id", "receipt_nonce"):
        wait_parser.add_argument("--" + name.replace("_", "-"), required=True)
    wait_parser.add_argument("--s1-mode", action="store_true")
    wait_parser.add_argument("--s2-mode", action="store_true")
    for name in ("s1_plan", "s1_plan_sha256", "s1_fixture_manifest", "s1_fixture_manifest_sha256", "s1_scratch", "s1_private", "s1_attempt_id", "endpoint_mask_dir"):
        wait_parser.add_argument("--" + name.replace("_", "-"))
    for name in ("s2_plan", "s2_plan_sha256", "s2_fixture_manifest", "s2_fixture_manifest_sha256", "s2_scratch", "s2_private", "s2_attempt_id", "s2_worker_role"):
        wait_parser.add_argument("--" + name.replace("_", "-"))
    wait_parser.set_defaults(handler=wait_for_worker)
    helper_parser = subparsers.add_parser("wait-helper")
    for name in ("helper_dir", "helper", "helper_sha256", "instance_id", "receipt_nonce"):
        helper_parser.add_argument("--" + name.replace("_", "-"), required=True)
    helper_parser.add_argument("--tcp-port", type=int, required=True)
    helper_parser.set_defaults(handler=wait_for_helper)
    return parser


def main() -> int:
    args = build_parser().parse_args()
    try:
        return int(args.handler(args))
    except BaseException as exc:
        _emit_receipt({"marker": "CGDR_LAUNCHER_ERROR", "subcommand": args.subcommand, "error": f"{type(exc).__name__}:{exc}"})
        return 125


if __name__ == "__main__":
    raise SystemExit(main())
