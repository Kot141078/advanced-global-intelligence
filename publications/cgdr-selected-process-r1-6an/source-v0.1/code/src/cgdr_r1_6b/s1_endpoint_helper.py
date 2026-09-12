from __future__ import annotations

"""One bounded trusted endpoint helper for the R1.6H synthetic S1 attempt."""

import argparse
import hashlib
import json
import os
import socket
import sys
import time
from pathlib import Path
from typing import Any

MAX_FRAME_BYTES = 4096
MAX_ACCEPTS_PER_CONTROL = 8
HELPER_PREFIX = "/tmp/cgdr-r1-6h-helper-"


def emit(value: dict[str, Any]) -> None:
    encoded = json.dumps(value, sort_keys=True, separators=(",", ":"))
    if len(encoded.encode("utf-8")) + 1 > MAX_FRAME_BYTES:
        raise RuntimeError("helper protocol frame overflow")
    print(encoded, flush=True)


def append_event(path: Path, value: dict[str, Any]) -> None:
    record = {"monotonic_ns": time.monotonic_ns(), **value}
    with path.open("a", encoding="utf-8", newline="\n") as stream:
        stream.write(json.dumps(record, sort_keys=True) + "\n")


def proc_start_ticks() -> int:
    return int(Path("/proc/self/stat").read_text(encoding="ascii").split()[21])


def namespace(kind: str) -> str:
    return os.readlink(f"/proc/self/ns/{kind}")


def _control_one(listener: socket.socket, address: Any, family: int, token: bytes, log: Path, channel: str) -> dict[str, Any]:
    client = socket.socket(family, socket.SOCK_STREAM)
    client.settimeout(2.0)
    accepted_rows: list[dict[str, Any]] = []
    try:
        client.connect(address)
        client.sendall(token)
        listener.settimeout(2.0)
        matched = False
        for _ in range(MAX_ACCEPTS_PER_CONTROL):
            connection, _peer = listener.accept()
            with connection:
                connection.settimeout(1.0)
                payload = connection.recv(64)
                accepted_rows.append({"bytes": len(payload), "sha256": hashlib.sha256(payload).hexdigest()})
                if payload == token:
                    connection.sendall(b"S1_ENDPOINT_OK")
                    matched = True
                    break
                connection.sendall(b"S1_UNEXPECTED_CLIENT")
        response = client.recv(64) if matched else b""
        result = {
            "channel": channel,
            "matched_control": matched,
            "response_sha256": hashlib.sha256(response).hexdigest(),
            "response_bytes": len(response),
            "accepted": accepted_rows,
        }
        append_event(log, {"kind": "POSITIVE_ENDPOINT_CONTROL", **result})
        return result
    finally:
        client.close()


def positive_controls(unix_listener: socket.socket, tcp_listener: socket.socket, unix_path: str, tcp_port: int, log: Path, phase: str) -> dict[str, Any]:
    unix_token = f"S1_{phase}_UNIX_CONTROL".encode("ascii")
    tcp_token = f"S1_{phase}_TCP_CONTROL".encode("ascii")
    unix_result = _control_one(unix_listener, unix_path, socket.AF_UNIX, unix_token, log, "UNIX")
    tcp_result = _control_one(tcp_listener, ("127.0.0.1", tcp_port), socket.AF_INET, tcp_token, log, "TCP")
    return {"phase": phase, "unix": unix_result, "tcp": tcp_result}


def serve(args: argparse.Namespace) -> int:
    helper_dir = Path(args.helper_dir)
    if not str(helper_dir).startswith(HELPER_PREFIX) or not helper_dir.is_dir() or helper_dir.is_symlink():
        raise ValueError("helper directory binding invalid")
    unix_path = str(helper_dir / "s1.sock")
    log = helper_dir / "helper_events.jsonl"
    if log.exists() or Path(unix_path).exists():
        raise FileExistsError("helper output/socket collision")
    log.touch(mode=0o600, exist_ok=False)
    unix_listener = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    tcp_listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        unix_listener.bind(unix_path)
        unix_listener.listen(8)
        tcp_listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 0)
        tcp_listener.bind(("127.0.0.1", args.tcp_port))
        tcp_listener.listen(8)
        pre = positive_controls(unix_listener, tcp_listener, unix_path, args.tcp_port, log, "PRE")
        ready = {
            "event": "HELPER_READY",
            "instance_id": args.instance_id,
            "pid": os.getpid(),
            "proc_start_ticks": proc_start_ticks(),
            "pid_namespace": namespace("pid"),
            "network_namespace": namespace("net"),
            "mount_namespace": namespace("mnt"),
            "unix_path": unix_path,
            "tcp_host": "127.0.0.1",
            "tcp_port": args.tcp_port,
            "pre_controls": pre,
            "environment_keys": sorted(os.environ),
        }
        append_event(log, {"kind": "HELPER_READY", "instance_id": args.instance_id})
        emit(ready)
        while True:
            raw = sys.stdin.buffer.readline(MAX_FRAME_BYTES + 1)
            if raw == b"":
                append_event(log, {"kind": "HELPER_STDIN_EOF"})
                return 2
            if len(raw) > MAX_FRAME_BYTES or not raw.endswith(b"\n"):
                emit({"event": "HELPER_REJECTED", "reason": "FRAME_OVERFLOW_OR_INCOMPLETE", "instance_id": args.instance_id})
                return 3
            message = json.loads(raw.decode("utf-8", errors="strict"))
            if message.get("command") == "POST_CONTROL":
                post = positive_controls(unix_listener, tcp_listener, unix_path, args.tcp_port, log, "POST")
                emit({"event": "HELPER_POST_CONTROL", "instance_id": args.instance_id, "message_id": message.get("message_id"), "controls": post})
            elif message.get("command") == "STOP":
                emit({"event": "HELPER_STOP_ACK", "instance_id": args.instance_id, "stop_id": message.get("stop_id")})
                append_event(log, {"kind": "HELPER_STOP_ACK", "stop_id": message.get("stop_id")})
                return 0
            else:
                emit({"event": "HELPER_REJECTED", "reason": "UNKNOWN_COMMAND", "instance_id": args.instance_id})
    finally:
        unix_listener.close()
        tcp_listener.close()
        try:
            Path(unix_path).unlink()
        except FileNotFoundError:
            pass


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="R1.6H bounded endpoint helper")
    subparsers = parser.add_subparsers(dest="subcommand", required=True)
    serve_parser = subparsers.add_parser("serve")
    serve_parser.add_argument("--helper-dir", required=True)
    serve_parser.add_argument("--tcp-port", type=int, required=True)
    serve_parser.add_argument("--instance-id", required=True)
    serve_parser.set_defaults(handler=serve)
    return parser


def main() -> int:
    args = build_parser().parse_args()
    return int(args.handler(args))


if __name__ == "__main__":
    raise SystemExit(main())
