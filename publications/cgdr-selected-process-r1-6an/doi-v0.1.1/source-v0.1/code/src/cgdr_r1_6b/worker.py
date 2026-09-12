from __future__ import annotations

import base64
import binascii
import ctypes
import errno
import hashlib
import json
import os
import socket
import sys
import time
from pathlib import Path
from typing import Any

MAX_FRAME_BYTES = 32 * 1024
MAX_S1_FILE_BYTES = 4096
S1_TASK_ID = "CGDR_SELECTED_PROCESS_ACCESS_BOUNDARY_S1_R1_6H"
S1_OPERATIONS = {"FILE_READ", "FILE_APPEND", "SCRATCH_WRITE_READBACK", "UNIX_CONNECT", "TCP_CONNECT"}
S2_TASK_ID = "CGDR_SELECTED_PROCESS_OPEN_STATE_HANDOFF_S2_R1_6I"
S2_OPERATIONS = {"FILE_READ", "FILE_APPEND", "SCRATCH_WRITE_READBACK"}
S2_ALLOWED_COMMANDS = {
    "W0": {"PING", "S2_DELTA", "LOAD", "CHECKPOINT", "SHAM_WAIT", "RELEASE", "CONTINUE", "STOP"},
    "W1": {"PING", "S2_DELTA", "RESTORE", "CHECKPOINT", "STOP"},
}
S2_EXTERNAL_MASK_BOUNDARY = "/mnt mode-000 tmpfs mask inside worker namespace"
S2_EXTERNAL_MASK_SUFFIXES = {
    "checkpoint_store_canary": "/external_trusted/checkpoint_store/checkpoint_store_canary.bin",
    "private_canary": "/external_trusted/private/private_canary.bin",
}
S2_EXTERNAL_MASK_ENTRY_FIELDS = {"windows_path", "wsl_path", "boundary"}


def _strict_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def emit(value: dict[str, Any]) -> None:
    payload = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True)
    if len(payload.encode("utf-8")) + 1 > MAX_FRAME_BYTES:
        raise RuntimeError("outbound protocol frame exceeds fixed limit")
    print(payload, flush=True)


def _proc_start_ticks() -> int:
    fields = open("/proc/self/stat", "r", encoding="ascii").read().split()
    return int(fields[21])


def _namespace_identity(kind: str) -> str:
    try:
        return os.readlink(f"/proc/self/ns/{kind}")
    except OSError as exc:
        return f"UNAVAILABLE:{type(exc).__name__}:{exc.errno}"


def _sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    total = 0
    with path.open("rb") as stream:
        while True:
            chunk = stream.read(4096)
            if not chunk:
                break
            total += len(chunk)
            if total > MAX_S1_FILE_BYTES:
                raise ValueError("S1 file exceeds bounded read ceiling")
            digest.update(chunk)
    return digest.hexdigest()


def _security_metadata() -> dict[str, Any]:
    wanted = {"Uid", "Gid", "Groups", "CapInh", "CapPrm", "CapEff", "CapBnd", "CapAmb", "NoNewPrivs", "Seccomp", "Seccomp_filters"}
    values: dict[str, str] = {}
    for line in Path("/proc/self/status").read_text(encoding="utf-8").splitlines():
        key, separator, value = line.partition(":")
        if separator and key in wanted:
            values[key] = value.strip()
    fds = []
    for name in os.listdir("/proc/self/fd"):
        if not name.isdigit():
            continue
        try:
            os.readlink(f"/proc/self/fd/{name}")
        except FileNotFoundError:
            continue
        fds.append(int(name))
    fds.sort()
    libc = ctypes.CDLL(None, use_errno=True)
    securebits = int(libc.prctl(27, 0, 0, 0, 0))  # PR_GET_SECUREBITS
    return {
        "status_fields": values,
        "open_fds": fds,
        "uid": os.getuid(),
        "gid": os.getgid(),
        "groups": os.getgroups(),
        "environment_keys": sorted(os.environ),
        "mount_namespace": _namespace_identity("mnt"),
        "securebits": securebits,
    }


def _load_s1_plan() -> tuple[dict[str, Any], str]:
    plan_path = Path(os.environ["CGDR_S1_PLAN"])
    expected_hash = os.environ["CGDR_S1_PLAN_SHA256"]
    raw = plan_path.read_bytes()
    if len(raw) > MAX_FRAME_BYTES:
        raise ValueError("S1 plan exceeds fixed limit")
    digest = hashlib.sha256(raw).hexdigest()
    if digest != expected_hash:
        raise ValueError("S1 plan hash mismatch")
    plan = json.loads(raw.decode("utf-8", errors="strict"), object_pairs_hook=_strict_object)
    if not isinstance(plan, dict) or plan.get("schema") != "TASK_LOCAL_S1_ACCESS_PLAN_V1":
        raise ValueError("S1 plan schema mismatch")
    if plan.get("task_id") != S1_TASK_ID or plan.get("attempt_id") != os.environ.get("CGDR_S1_ATTEMPT_ID"):
        raise ValueError("S1 plan task/attempt binding mismatch")
    stage = str(plan.get("stage_dir", ""))
    if not stage.startswith("/tmp/cgdr-r1-6h-s1-"):
        raise ValueError("S1 plan stage binding mismatch")
    probes = plan.get("probes")
    if not isinstance(probes, list) or not probes or len(probes) > 32:
        raise ValueError("S1 plan probe list invalid")
    seen: set[str] = set()
    helper_dir = str((plan.get("endpoint_binding") or {}).get("helper_dir", ""))
    for item in probes:
        if not isinstance(item, dict) or not isinstance(item.get("probe_id"), str) or item["probe_id"] in seen:
            raise ValueError("S1 plan duplicate/invalid probe id")
        seen.add(item["probe_id"])
        if item.get("operation") not in S1_OPERATIONS or item.get("expectation") not in {"EXPECT_ALLOW", "EXPECT_DENY"}:
            raise ValueError("S1 plan operation/expectation invalid")
        target = str(item.get("target", ""))
        if not (target.startswith(stage + "/") or target.startswith(helper_dir + "/") or item.get("operation") == "TCP_CONNECT"):
            raise ValueError("S1 plan target outside frozen roots")
    return plan, digest


def _validate_s2_external_masked_targets(value: Any) -> set[str]:
    if not isinstance(value, dict) or set(value) != set(S2_EXTERNAL_MASK_SUFFIXES):
        raise ValueError("S2 external masked target inventory mismatch")
    roots: dict[str, str] = {}
    allowed_external: set[str] = set()
    for name, suffix in S2_EXTERNAL_MASK_SUFFIXES.items():
        entry = value[name]
        if not isinstance(entry, dict) or set(entry) != S2_EXTERNAL_MASK_ENTRY_FIELDS:
            raise ValueError("S2 external masked target entry mismatch")
        windows_path = entry.get("windows_path")
        wsl_path = entry.get("wsl_path")
        boundary = entry.get("boundary")
        if not isinstance(windows_path, str) or not windows_path or not isinstance(wsl_path, str) or not wsl_path:
            raise ValueError("S2 external masked target entry mismatch")
        if boundary != S2_EXTERNAL_MASK_BOUNDARY:
            raise ValueError("S2 external masked target boundary mismatch")
        if len(windows_path) < 4 or windows_path[0].casefold() != "c" or windows_path[1] != ":" or windows_path[2] not in {"/", "\\"}:
            raise ValueError("S2 external masked target Windows path mismatch")
        windows_components = windows_path[3:].replace("\\", "/").split("/")
        if not windows_components or any(component in {"", ".", ".."} for component in windows_components):
            raise ValueError("S2 external masked target path safety mismatch")
        if not wsl_path.startswith("/mnt/c/"):
            raise ValueError("S2 external masked target path safety mismatch")
        wsl_components = wsl_path[len("/mnt/c/") :].split("/")
        if not wsl_components or any(component in {"", ".", ".."} for component in wsl_components):
            raise ValueError("S2 external masked target path safety mismatch")
        expected_wsl_path = "/mnt/c/" + "/".join(windows_components)
        if wsl_path != expected_wsl_path:
            raise ValueError("S2 external masked target representation mismatch")
        if not wsl_path.endswith(suffix):
            raise ValueError("S2 external masked target suffix mismatch")
        roots[name] = wsl_path[: -len(suffix)]
        allowed_external.add(wsl_path)
    if len(set(roots.values())) != 1:
        raise ValueError("S2 external masked target shared root mismatch")
    return allowed_external


def _load_s2_plan() -> tuple[dict[str, Any], str, str]:
    plan_path = Path(os.environ["CGDR_S2_PLAN"])
    expected_hash = os.environ["CGDR_S2_PLAN_SHA256"]
    raw = plan_path.read_bytes()
    if len(raw) > MAX_FRAME_BYTES:
        raise ValueError("S2 plan exceeds fixed limit")
    digest = hashlib.sha256(raw).hexdigest()
    if digest != expected_hash:
        raise ValueError("S2 plan hash mismatch")
    plan = json.loads(raw.decode("utf-8", errors="strict"), object_pairs_hook=_strict_object)
    role = str(plan.get("worker_role", ""))
    if not isinstance(plan, dict) or plan.get("schema") != "TASK_LOCAL_S2_DELTA_PLAN_V1":
        raise ValueError("S2 plan schema mismatch")
    if (
        plan.get("task_id") != S2_TASK_ID
        or plan.get("attempt_id") != os.environ.get("CGDR_S2_ATTEMPT_ID")
        or role != os.environ.get("CGDR_S2_WORKER_ROLE")
        or role not in S2_ALLOWED_COMMANDS
    ):
        raise ValueError("S2 plan task/attempt/role binding mismatch")
    stage = str(plan.get("stage_dir", ""))
    if not stage.startswith(f"/tmp/cgdr-r1-6i-s2-{role.casefold()}-"):
        raise ValueError("S2 plan stage binding mismatch")
    if set(plan.get("allowed_commands") or []) != S2_ALLOWED_COMMANDS[role]:
        raise ValueError("S2 allowed command set mismatch")
    allowed_external = _validate_s2_external_masked_targets(plan.get("external_masked_targets"))
    probes = plan.get("probes")
    if not isinstance(probes, list) or len(probes) != 5:
        raise ValueError("S2 delta probe list invalid")
    seen: set[str] = set()
    for item in probes:
        if not isinstance(item, dict) or not isinstance(item.get("probe_id"), str) or item["probe_id"] in seen:
            raise ValueError("S2 plan duplicate/invalid probe id")
        seen.add(item["probe_id"])
        if item.get("operation") not in S2_OPERATIONS or item.get("expectation") not in {"EXPECT_ALLOW", "EXPECT_DENY"}:
            raise ValueError("S2 plan operation/expectation invalid")
        target = str(item.get("target", ""))
        if not (target.startswith(stage + "/") or target in allowed_external):
            raise ValueError("S2 plan target outside frozen roots")
    return plan, digest, role


def _s1_file_operation(item: dict[str, Any]) -> dict[str, Any]:
    operation = item["operation"]
    target = str(item["target"])
    flags_no_follow = getattr(os, "O_NOFOLLOW", 0) | getattr(os, "O_BINARY", 0)
    try:
        if operation == "FILE_READ":
            fd = os.open(target, os.O_RDONLY | flags_no_follow)
            try:
                data = os.read(fd, MAX_S1_FILE_BYTES + 1)
            finally:
                os.close(fd)
            if len(data) > MAX_S1_FILE_BYTES:
                raise OSError(errno.EOVERFLOW, "bounded read overflow")
            return {"allowed": True, "bytes": len(data), "observed_sha256": hashlib.sha256(data).hexdigest()}
        if operation == "FILE_APPEND":
            fd = os.open(target, os.O_WRONLY | os.O_APPEND | flags_no_follow)
            try:
                written = os.write(fd, b"S1_DENIED_WRITE_ATTEMPT\n")
                os.fsync(fd)
            finally:
                os.close(fd)
            return {"allowed": True, "bytes_written": written}
        if operation == "SCRATCH_WRITE_READBACK":
            payload = str(item.get("write_payload", "")).encode("utf-8")
            if not payload or len(payload) > 512:
                raise ValueError("invalid bounded scratch payload")
            fd = os.open(target, os.O_WRONLY | os.O_CREAT | os.O_EXCL | flags_no_follow, 0o600)
            try:
                written = os.write(fd, payload)
                os.fsync(fd)
            finally:
                os.close(fd)
            readback = Path(target).read_bytes()
            return {"allowed": True, "bytes_written": written, "bytes_read": len(readback), "observed_sha256": hashlib.sha256(readback).hexdigest()}
        raise ValueError("not a file operation")
    except OSError as exc:
        return {"allowed": False, "errno": exc.errno, "error_class": type(exc).__name__}


def _s1_socket_operation(item: dict[str, Any]) -> dict[str, Any]:
    operation = item["operation"]
    family = socket.AF_UNIX if operation == "UNIX_CONNECT" else socket.AF_INET
    sock = socket.socket(family, socket.SOCK_STREAM)
    sock.settimeout(2.0)
    try:
        address: Any = str(item["target"]) if operation == "UNIX_CONNECT" else (str(item["tcp_host"]), int(item["tcp_port"]))
        sock.connect(address)
        try:
            sock.sendall(b"S1_WORKER_PROBE")
        except OSError:
            pass
        return {"allowed": True, "connect_completed": True}
    except OSError as exc:
        return {"allowed": False, "errno": exc.errno, "error_class": type(exc).__name__}
    finally:
        sock.close()


def run_s1_plan(plan: dict[str, Any]) -> dict[str, Any]:
    rows: list[dict[str, Any]] = []
    stopped_after: str | None = None
    for item in plan["probes"]:
        operation = item["operation"]
        outcome = _s1_socket_operation(item) if operation in {"UNIX_CONNECT", "TCP_CONNECT"} else _s1_file_operation(item)
        row = {
            "probe_id": item["probe_id"],
            "object_id": item["object_id"],
            "operation": operation,
            "expectation": item["expectation"],
            "target": item["target"],
            "syscall_attempted": True,
            **outcome,
        }
        rows.append(row)
        if item["expectation"] == "EXPECT_DENY" and outcome.get("allowed") is True:
            stopped_after = item["probe_id"]
            break
    return {"rows": rows, "stopped_after_forbidden_success": stopped_after, "planned_count": len(plan["probes"])}


def _s2_file_operation(item: dict[str, Any]) -> dict[str, Any]:
    operation = item["operation"]
    target = str(item["target"])
    flags_no_follow = getattr(os, "O_NOFOLLOW", 0) | getattr(os, "O_BINARY", 0)
    try:
        if operation == "FILE_READ":
            fd = os.open(target, os.O_RDONLY | flags_no_follow)
            try:
                data = os.read(fd, MAX_S1_FILE_BYTES + 1)
            finally:
                os.close(fd)
            if len(data) > MAX_S1_FILE_BYTES:
                raise OSError(errno.EOVERFLOW, "bounded read overflow")
            return {"allowed": True, "bytes": len(data), "observed_sha256": hashlib.sha256(data).hexdigest()}
        if operation == "FILE_APPEND":
            fd = os.open(target, os.O_WRONLY | os.O_APPEND | flags_no_follow)
            try:
                written = os.write(fd, b"S2_DENIED_WRITE_ATTEMPT\n")
                os.fsync(fd)
            finally:
                os.close(fd)
            return {"allowed": True, "bytes_written": written}
        if operation == "SCRATCH_WRITE_READBACK":
            payload = str(item.get("write_payload", "")).encode("utf-8")
            if not payload or len(payload) > 512:
                raise ValueError("invalid bounded S2 scratch payload")
            fd = os.open(target, os.O_WRONLY | os.O_CREAT | os.O_EXCL | flags_no_follow, 0o600)
            try:
                written = os.write(fd, payload)
                os.fsync(fd)
            finally:
                os.close(fd)
            readback = Path(target).read_bytes()
            return {"allowed": True, "bytes_written": written, "bytes_read": len(readback), "observed_sha256": hashlib.sha256(readback).hexdigest()}
        raise ValueError("not an S2 file operation")
    except OSError as exc:
        return {"allowed": False, "errno": exc.errno, "error_class": type(exc).__name__}


def run_s2_delta(plan: dict[str, Any]) -> dict[str, Any]:
    rows: list[dict[str, Any]] = []
    stopped_after: str | None = None
    for item in plan["probes"]:
        outcome = _s2_file_operation(item)
        row = {
            "probe_id": item["probe_id"],
            "object_id": item["object_id"],
            "operation": item["operation"],
            "expectation": item["expectation"],
            "target": item["target"],
            "syscall_attempted": True,
            **outcome,
        }
        rows.append(row)
        if item["expectation"] == "EXPECT_DENY" and outcome.get("allowed") is True:
            stopped_after = item["probe_id"]
            break
    return {"rows": rows, "stopped_after_forbidden_success": stopped_after, "planned_count": len(plan["probes"])}


def attempt_file(path: str, write: bool) -> dict[str, Any]:
    flags = os.O_WRONLY | os.O_APPEND if write else os.O_RDONLY
    try:
        fd = os.open(path, flags)
        try:
            data = b""
            if write:
                os.write(fd, b"FORBIDDEN-WRITE\n")
            else:
                data = os.read(fd, 32)
            return {"allowed": True, "bytes": len(data)}
        finally:
            os.close(fd)
    except OSError as exc:
        return {"allowed": False, "error": f"{type(exc).__name__}:{exc.errno}", "errno": exc.errno}


def probe(message: dict[str, Any]) -> dict[str, Any]:
    net_name = _namespace_identity("net")
    pid_name = _namespace_identity("pid")
    try:
        network_devices = open("/proc/net/dev", "r", encoding="utf-8").read()
    except OSError as exc:
        network_devices = f"UNAVAILABLE:{type(exc).__name__}:{exc.errno}"
    try:
        with socket.create_connection(("127.0.0.1", int(message["endpoint_port"])), timeout=1.0):
            network = {"allowed": True}
    except OSError as exc:
        network = {"allowed": False, "error": f"{type(exc).__name__}:{exc.errno}", "errno": exc.errno}
    ipc_socket = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    ipc_socket.settimeout(1.0)
    try:
        ipc_socket.connect("\0" + str(message["ipc_abstract_name"]))
        ipc = {"allowed": True}
    except OSError as exc:
        ipc = {"allowed": False, "error": f"{type(exc).__name__}:{exc.errno}", "errno": exc.errno}
    finally:
        ipc_socket.close()
    return {
        "write_sentinel": attempt_file(message["write_path"], True),
        "read_secret": attempt_file(message["secret_path"], False),
        "forbidden_ipc": ipc,
        "network_endpoint": network,
        "network_namespace": net_name,
        "pid_namespace": pid_name,
        "network_devices_sha256": hashlib.sha256(network_devices.encode()).hexdigest(),
        "network_devices_excerpt": network_devices[:512],
        "environment_keys": sorted(os.environ),
        "uid": os.getuid(),
        "pid": os.getpid(),
    }


def material_summary(state: dict[str, Any]) -> dict[str, Any]:
    qsf = state.get("qsf") or {}
    duty = state.get("duty") or {}
    return {
        "source_id": state.get("source_id"),
        "qsf_id": qsf.get("qsf_id"),
        "qsf_state": qsf.get("state"),
        "variant_ids": [item.get("id") for item in qsf.get("variants", []) if isinstance(item, dict)],
        "duty_id": duty.get("id"),
        "duty_status": duty.get("status"),
        "minority_refs": qsf.get("minority_refs"),
        "dispute_refs": qsf.get("dispute_refs"),
        "role": state.get("role"),
        "custody": state.get("custody"),
        "arq_standing": state.get("arq_standing"),
    }


class StateMachine:
    def __init__(
        self,
        instance_id: str,
        s1_plan: dict[str, Any] | None = None,
        s1_plan_sha256: str | None = None,
        s2_plan: dict[str, Any] | None = None,
        s2_plan_sha256: str | None = None,
        s2_role: str | None = None,
    ):
        self.instance_id = instance_id
        self.state_bytes: bytes | None = None
        self.state: dict[str, Any] | None = None
        self.waiting = False
        self.released = False
        self.checkpoint_seq = 0
        self.s1_plan = s1_plan
        self.s1_plan_sha256 = s1_plan_sha256
        self.s1_executed = False
        self.s2_plan = s2_plan
        self.s2_plan_sha256 = s2_plan_sha256
        self.s2_role = s2_role
        self.s2_delta_executed = False

    def _decode_state(self, encoded: Any, expected_hash: Any) -> tuple[bytes, dict[str, Any], str]:
        if not isinstance(encoded, str) or not isinstance(expected_hash, str):
            raise ValueError("state bytes/hash missing")
        raw = base64.b64decode(encoded.encode("ascii"), validate=True)
        if len(raw) > MAX_FRAME_BYTES // 2:
            raise ValueError("state payload exceeds fixed limit")
        digest = hashlib.sha256(raw).hexdigest()
        if digest != expected_hash:
            raise ValueError("state hash mismatch")
        state = json.loads(raw.decode("utf-8", errors="strict"), object_pairs_hook=_strict_object)
        if not isinstance(state, dict):
            raise ValueError("state must be an object")
        return raw, state, digest

    def handle(self, message: dict[str, Any]) -> tuple[dict[str, Any], bool]:
        command = message.get("command")
        if self.s2_role is not None and command not in S2_ALLOWED_COMMANDS[self.s2_role]:
            return {"event": "REJECTED", "reason": "COMMAND_NOT_ALLOWED_IN_S2_ROLE", "instance_id": self.instance_id}, False
        if command == "PING":
            return {
                "event": "PONG", "instance_id": self.instance_id,
                "nonce": message.get("nonce"), "message_id": message.get("message_id"),
            }, False
        if command == "LOAD":
            raw, state, digest = self._decode_state(message.get("state_b64"), message.get("state_sha256"))
            self.state_bytes, self.state = raw, state
            return {
                "event": "LOAD_ACK", "instance_id": self.instance_id,
                "state_sha256": digest, "material": material_summary(state),
                "message_id": message.get("message_id"),
            }, False
        if command == "CHECKPOINT":
            if self.state_bytes is None or self.state is None:
                return {"event": "REJECTED", "reason": "STATE_NOT_LOADED", "instance_id": self.instance_id}, False
            self.checkpoint_seq += 1
            return {
                "event": "CHECKPOINT", "instance_id": self.instance_id,
                "state_b64": base64.b64encode(self.state_bytes).decode("ascii"),
                "state_sha256": hashlib.sha256(self.state_bytes).hexdigest(),
                "material": material_summary(self.state),
                "checkpoint_seq": self.checkpoint_seq,
                "message_id": message.get("message_id"),
                "monotonic_ns": time.monotonic_ns(),
            }, False
        if command == "SHAM_WAIT":
            if self.state is None:
                return {"event": "REJECTED", "reason": "STATE_NOT_LOADED", "instance_id": self.instance_id}, False
            self.waiting = True
            self.released = False
            return {
                "event": "SHAM_WAITING", "instance_id": self.instance_id,
                "state_sha256": hashlib.sha256(self.state_bytes or b"").hexdigest(),
                "wait_id": message.get("wait_id"),
            }, False
        if command == "RELEASE":
            if not self.waiting:
                return {"event": "REJECTED", "reason": "NOT_WAITING", "instance_id": self.instance_id}, False
            self.released = True
            return {
                "event": "RELEASED", "instance_id": self.instance_id,
                "release_id": message.get("release_id"), "monotonic_ns": time.monotonic_ns(),
            }, False
        if command == "CONTINUE":
            if not (self.waiting and self.released):
                return {"event": "REJECTED", "reason": "RELEASE_REQUIRED", "instance_id": self.instance_id}, False
            self.waiting = False
            return {
                "event": "CONTINUED", "instance_id": self.instance_id,
                "state_sha256": hashlib.sha256(self.state_bytes or b"").hexdigest(),
                "continue_id": message.get("continue_id"), "monotonic_ns": time.monotonic_ns(),
            }, False
        if command == "RESTORE":
            raw, state, digest = self._decode_state(message.get("state_b64"), message.get("state_sha256"))
            self.state_bytes, self.state = raw, state
            return {
                "event": "RESTORED", "instance_id": self.instance_id,
                "state_sha256": digest, "material": material_summary(state),
                "checkpoint_seq": message.get("checkpoint_seq"),
                "message_id": message.get("message_id"),
            }, False
        if command == "PROCESS":
            packet = message.get("packet")
            encoded = json.dumps(packet, sort_keys=True, separators=(",", ":")).encode()
            return {
                "event": "PROPOSAL_OBSERVED", "instance_id": self.instance_id,
                "packet_sha256": hashlib.sha256(encoded).hexdigest(),
                "operation_id": message.get("operation_id"),
            }, False
        if command == "PROBE":
            if self.s1_plan is not None:
                return {"event": "REJECTED", "reason": "LEGACY_PROBE_DISABLED_IN_S1", "instance_id": self.instance_id}, False
            return {"event": "PROBE_RESULT", "instance_id": self.instance_id, "result": probe(message)}, False
        if command == "S1_RUN":
            if self.s1_plan is None or self.s1_plan_sha256 is None:
                return {"event": "REJECTED", "reason": "S1_MODE_NOT_ACTIVE", "instance_id": self.instance_id}, False
            if self.s1_executed:
                return {"event": "REJECTED", "reason": "S1_PLAN_ALREADY_EXECUTED", "instance_id": self.instance_id}, False
            if message.get("plan_sha256") != self.s1_plan_sha256 or message.get("attempt_id") != self.s1_plan.get("attempt_id"):
                return {"event": "REJECTED", "reason": "S1_COMMAND_BINDING_MISMATCH", "instance_id": self.instance_id}, False
            self.s1_executed = True
            return {
                "event": "S1_PROBE_BATCH_RESULT",
                "instance_id": self.instance_id,
                "attempt_id": self.s1_plan["attempt_id"],
                "plan_sha256": self.s1_plan_sha256,
                "result": run_s1_plan(self.s1_plan),
            }, False
        if command == "S2_DELTA":
            if self.s2_plan is None or self.s2_plan_sha256 is None or self.s2_role is None:
                return {"event": "REJECTED", "reason": "S2_MODE_NOT_ACTIVE", "instance_id": self.instance_id}, False
            if self.s2_delta_executed:
                return {"event": "REJECTED", "reason": "S2_DELTA_ALREADY_EXECUTED", "instance_id": self.instance_id}, False
            if (
                message.get("plan_sha256") != self.s2_plan_sha256
                or message.get("attempt_id") != self.s2_plan.get("attempt_id")
                or message.get("worker_role") != self.s2_role
            ):
                return {"event": "REJECTED", "reason": "S2_COMMAND_BINDING_MISMATCH", "instance_id": self.instance_id}, False
            self.s2_delta_executed = True
            return {
                "event": "S2_DELTA_RESULT",
                "instance_id": self.instance_id,
                "attempt_id": self.s2_plan["attempt_id"],
                "worker_role": self.s2_role,
                "plan_sha256": self.s2_plan_sha256,
                "result": run_s2_delta(self.s2_plan),
            }, False
        if command == "STOP":
            return {
                "event": "STOP_ACK", "instance_id": self.instance_id,
                "stop_id": message.get("stop_id"), "monotonic_ns": time.monotonic_ns(),
            }, True
        return {"event": "REJECTED", "reason": "UNKNOWN_COMMAND", "instance_id": self.instance_id}, False


def main() -> int:
    instance_id = os.environ.get("CGDR_INSTANCE_ID", "MISSING_INSTANCE")
    s1_plan: dict[str, Any] | None = None
    s1_plan_sha256: str | None = None
    s2_plan: dict[str, Any] | None = None
    s2_plan_sha256: str | None = None
    s2_role: str | None = None
    if os.environ.get("CGDR_S1_MODE") == "1":
        s1_plan, s1_plan_sha256 = _load_s1_plan()
    if os.environ.get("CGDR_S2_MODE") == "1":
        if s1_plan is not None:
            raise ValueError("S1 and S2 modes are mutually exclusive")
        s2_plan, s2_plan_sha256, s2_role = _load_s2_plan()
    emit({
        "event": "READY", "instance_id": instance_id, "pid": os.getpid(),
        "proc_start_ticks": _proc_start_ticks(), "pid_namespace": _namespace_identity("pid"),
        "network_namespace": _namespace_identity("net"), "mount_namespace": _namespace_identity("mnt"),
        "monotonic_ns": time.monotonic_ns(), "s1_mode": s1_plan is not None,
        "s1_plan_sha256": s1_plan_sha256, "s2_mode": s2_plan is not None,
        "s2_plan_sha256": s2_plan_sha256, "s2_worker_role": s2_role,
        "s2_attempt_id": None if s2_plan is None else s2_plan.get("attempt_id"),
        "security_metadata": _security_metadata(),
        "protocol_limits": {"frame_bytes": MAX_FRAME_BYTES},
    })
    machine = StateMachine(instance_id, s1_plan, s1_plan_sha256, s2_plan, s2_plan_sha256, s2_role)
    stream = sys.stdin.buffer
    while True:
        raw = stream.readline(MAX_FRAME_BYTES + 1)
        if raw == b"":
            return 0
        if len(raw) > MAX_FRAME_BYTES or not raw.endswith(b"\n"):
            emit({"event": "REJECTED", "reason": "FRAME_OVERFLOW_OR_INCOMPLETE", "instance_id": instance_id})
            return errno.EOVERFLOW
        try:
            text = raw.decode("utf-8", errors="strict")
            message = json.loads(text, object_pairs_hook=_strict_object)
            if not isinstance(message, dict):
                raise ValueError("protocol frame is not an object")
            response, should_stop = machine.handle(message)
        except (UnicodeDecodeError, json.JSONDecodeError, ValueError, TypeError, binascii.Error) as exc:
            emit({"event": "REJECTED", "reason": f"INVALID_FRAME:{type(exc).__name__}", "instance_id": instance_id})
            continue
        emit(response)
        if should_stop:
            return 0


if __name__ == "__main__":
    raise SystemExit(main())
