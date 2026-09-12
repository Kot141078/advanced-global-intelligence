from __future__ import annotations

import argparse
import hashlib
import json
import secrets
import sys
import uuid
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from cgdr_r1_6b.common import write_json
from cgdr_r1_6b.supervisor import WorkerProcess, sha256_file, stage_worker


REQUIRED_ORDER = [
    "PROCESS_START_REQUESTED",
    "PROCESS_HANDLE_OBTAINED",
    "OS_CHILD_BOUND",
    "IPC_RECEIVED:READY",
    "IPC_SENT:PING",
    "IPC_RECEIVED:PONG",
    "IPC_SENT:STOP",
    "IPC_RECEIVED:STOP_ACK",
    "EXIT_OBSERVED",
]


def _event_tag(event: dict[str, Any]) -> str:
    kind = event.get("kind")
    if kind == "IPC_SENT":
        return f"IPC_SENT:{event.get('command')}"
    if kind == "IPC_RECEIVED":
        worker_event = event.get("worker_event") or {}
        return f"IPC_RECEIVED:{worker_event.get('event')}"
    return str(kind)


def review_s0_trace(events: list[dict[str, Any]], expected: dict[str, Any]) -> dict[str, Any]:
    """Independent evidence reader: derives the S0 verdict without producer status."""
    issues: list[dict[str, str]] = []
    by_tag: dict[str, dict[str, Any]] = {}
    cursor = -1
    for required in REQUIRED_ORDER:
        found = None
        for index in range(cursor + 1, len(events)):
            if _event_tag(events[index]) == required:
                found = index
                break
        if found is None:
            issues.append({"severity": "MISSING", "reason": f"MISSING_REQUIRED_EVENT:{required}"})
        else:
            cursor = found
            by_tag[required] = events[found]

    instance_id = expected["instance_id"]
    for tag, event in by_tag.items():
        if event.get("instance_id") != instance_id:
            issues.append({"severity": "MISMATCH", "reason": f"WRONG_INSTANCE:{tag}"})

    binding = (by_tag.get("OS_CHILD_BOUND") or {}).get("binding") or {}
    if "OS_CHILD_BOUND" in by_tag:
        for field, wanted in {
            "instance_id": instance_id,
            "receipt_nonce": expected["receipt_nonce"],
            "worker_sha256": expected["worker_sha256"],
            "launcher_sha256": expected["launcher_sha256"],
            "binding_source": "TRUSTED_DIRECT_FORK_PARENT",
            "wait_source": "POSIX_WAITPID_CHILD",
        }.items():
            if binding.get(field) != wanted:
                issues.append({"severity": "MISMATCH", "reason": f"CHILD_BINDING_MISMATCH:{field}"})
        for field in ("worker_pid", "worker_start_ticks", "waiter_pid", "waiter_start_ticks"):
            if not isinstance(binding.get(field), int):
                issues.append({"severity": "MISSING", "reason": f"CHILD_BINDING_MISSING:{field}"})

    ready = (by_tag.get("IPC_RECEIVED:READY") or {}).get("worker_event") or {}
    if "IPC_RECEIVED:READY" in by_tag and "OS_CHILD_BOUND" in by_tag:
        for field, wanted in {
            "instance_id": instance_id,
            "pid": binding.get("worker_pid"),
            "proc_start_ticks": binding.get("worker_start_ticks"),
            "pid_namespace": binding.get("pid_namespace"),
            "network_namespace": binding.get("network_namespace"),
        }.items():
            if ready.get(field) != wanted:
                issues.append({"severity": "MISMATCH", "reason": f"READY_BINDING_MISMATCH:{field}"})

    ping = by_tag.get("IPC_SENT:PING") or {}
    if "IPC_SENT:PING" in by_tag and (ping.get("nonce") != expected["ping_nonce"] or ping.get("message_id") != expected["ping_message_id"]):
        issues.append({"severity": "MISMATCH", "reason": "PING_INTENT_MISMATCH"})
    pong = (by_tag.get("IPC_RECEIVED:PONG") or {}).get("worker_event") or {}
    if "IPC_RECEIVED:PONG" in by_tag:
        for field, wanted in {
            "instance_id": instance_id,
            "nonce": expected["ping_nonce"],
            "message_id": expected["ping_message_id"],
        }.items():
            if pong.get(field) != wanted:
                issues.append({"severity": "MISMATCH", "reason": f"PONG_MISMATCH:{field}"})

    stop = by_tag.get("IPC_SENT:STOP") or {}
    stop_ack = (by_tag.get("IPC_RECEIVED:STOP_ACK") or {}).get("worker_event") or {}
    if "IPC_SENT:STOP" in by_tag and stop.get("message_id") != expected["stop_id"]:
        issues.append({"severity": "MISMATCH", "reason": "STOP_ID_MISMATCH"})
    if "IPC_RECEIVED:STOP_ACK" in by_tag:
        for field, wanted in {"instance_id": instance_id, "stop_id": expected["stop_id"]}.items():
            if stop_ack.get(field) != wanted:
                issues.append({"severity": "MISMATCH", "reason": f"STOP_ACK_MISMATCH:{field}"})

    exit_event = by_tag.get("EXIT_OBSERVED") or {}
    exit_receipt = exit_event.get("inner_exit_receipt") or {}
    if "EXIT_OBSERVED" in by_tag and "OS_CHILD_BOUND" in by_tag:
        for field in (
            "instance_id", "receipt_nonce", "worker_pid", "worker_start_ticks", "waiter_pid",
            "waiter_start_ticks", "pid_namespace", "network_namespace", "mount_namespace",
            "worker_sha256", "launcher_sha256",
        ):
            if exit_receipt.get(field) != binding.get(field):
                issues.append({"severity": "MISMATCH", "reason": f"EXIT_BINDING_MISMATCH:{field}"})
        for field, wanted in {
            "binding_source": "TRUSTED_DIRECT_FORK_PARENT",
            "wait_source": "POSIX_WAITPID_CHILD",
            "return_code": 0,
        }.items():
            if exit_receipt.get(field) != wanted:
                issues.append({"severity": "MISMATCH", "reason": f"EXIT_RECEIPT_MISMATCH:{field}"})
        if exit_event.get("return_code") != 0:
            issues.append({"severity": "MISMATCH", "reason": "WRAPPER_RETURN_CODE_NOT_ZERO"})
        if exit_event.get("inner_exit_confirmed") is not True:
            issues.append({"severity": "MISSING", "reason": "DIRECT_CHILD_WAIT_NOT_CONFIRMED"})
        if exit_event.get("reader_threads_stopped") is not True:
            issues.append({"severity": "MISSING", "reason": "READERS_NOT_STOPPED"})
        if exit_event.get("cleanup_status") != "PROVEN":
            issues.append({"severity": "MISSING", "reason": "CLEANUP_NOT_PROVEN"})

    sent_commands = [event.get("command") for event in events if event.get("kind") == "IPC_SENT"]
    if sent_commands != ["PING", "STOP"]:
        issues.append({"severity": "MISMATCH", "reason": f"FORBIDDEN_OR_DUPLICATE_COMMANDS:{sent_commands!r}"})
    if len({event.get("local_seq") for event in events}) != len(events):
        issues.append({"severity": "MISMATCH", "reason": "DUPLICATE_EVENT_SEQUENCE"})

    if any(issue["severity"] == "MISMATCH" for issue in issues):
        verdict = "FAIL"
    elif issues:
        verdict = "INCONCLUSIVE"
    else:
        verdict = "PASS"
    return {
        "reviewer": "INDEPENDENT_S0_TRACE_REVIEWER",
        "verdict": verdict,
        "required_order": REQUIRED_ORDER,
        "actual_order": [_event_tag(event) for event in events],
        "issues": issues,
        "evidence_event_count": len(events),
        "binding_summary": {
            key: binding.get(key)
            for key in (
                "instance_id", "worker_pid", "worker_start_ticks", "waiter_pid", "waiter_start_ticks",
                "pid_namespace", "network_namespace", "mount_namespace", "worker_sha256", "launcher_sha256",
            )
        },
    }


def _read_events(path: Path) -> list[dict[str, Any]]:
    if not path.is_file():
        return []
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def review_s0_files(events_path: Path, intent_path: Path) -> dict[str, Any]:
    persisted_intent = json.loads(intent_path.read_text(encoding="utf-8"))
    return review_s0_trace(_read_events(events_path), persisted_intent)


def _validate_h0(path: Path) -> dict[str, Any]:
    receipt = json.loads(path.read_text(encoding="utf-8"))
    if receipt.get("task_id") != "CGDR_SELECTED_PROCESS_LIFECYCLE_S0_R1_6G":
        raise RuntimeError("H0 receipt belongs to a different task")
    if receipt.get("current_d_residual_status") != "ABSENT_NOW_SUPPORTED":
        raise RuntimeError("H0 does not authorize S0: current residual status is not supported absent")
    if receipt.get("valid_for_s0") is not True or receipt.get("read_only_pass_count") != 2:
        raise RuntimeError("H0 pass-2 recency gate is not satisfied")
    return receipt


def prepare_fresh_output(path: Path) -> Path:
    output = path.resolve()
    if output.exists():
        raise FileExistsError(f"S0 output collision: {output}")
    output.mkdir(parents=True)
    return output


def main() -> int:
    parser = argparse.ArgumentParser(description="One bounded S0 transport attempt; never runs S1/S2/matrix.")
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--worker", type=Path, required=True)
    parser.add_argument("--h0-receipt", type=Path, required=True)
    parser.add_argument("--distro", default="Ubuntu")
    parser.add_argument("--stage-dir", required=True)
    args = parser.parse_args()
    h0 = _validate_h0(args.h0_receipt.resolve())
    try:
        output = prepare_fresh_output(args.output)
    except FileExistsError as exc:
        raise SystemExit(str(exc)) from exc
    report: dict[str, Any] = {
        "stage": "S0",
        "status": "INCONCLUSIVE",
        "worker_start_requests": 0,
        "helper_starts": 0,
        "cleanup_status": "NOT_STARTED",
        "measured_matrix_started": False,
        "external_calls": 0,
        "model_calls": 0,
        "h0_receipt_sha256": sha256_file(args.h0_receipt.resolve()),
        "h0_current_residual_status": h0["current_d_residual_status"],
    }
    worker: WorkerProcess | None = None
    expected: dict[str, Any] | None = None
    producer_exception: str | None = None
    try:
        staged = stage_worker(args.distro, args.worker, args.stage_dir, output / "setup.jsonl")
        worker = WorkerProcess(args.distro, staged, output / "events.jsonl", "S0", "ROUNDTRIP")
        ping_nonce = secrets.token_urlsafe(32)
        ping_message_id = f"s0-ping-{uuid.uuid4()}"
        stop_id = f"s0-stop-{uuid.uuid4()}"
        expected = {
            "instance_id": worker.instance_id,
            "receipt_nonce": worker.receipt_nonce,
            "worker_sha256": staged.worker_sha256,
            "launcher_sha256": staged.launcher_sha256,
            "ping_nonce": ping_nonce,
            "ping_message_id": ping_message_id,
            "stop_id": stop_id,
        }
        write_json(output / "review_intent.json", {
            **expected,
            "receipt_nonce_sha256": hashlib.sha256(worker.receipt_nonce.encode()).hexdigest(),
            "ping_nonce_sha256": hashlib.sha256(ping_nonce.encode()).hexdigest(),
            "fixed_before_start": True,
            "sensitivity": "NON_SECRET_SYNTHETIC_S0_BINDING_VALUES",
        })
        report["worker_start_requests"] = 1
        ready = worker.start(10)
        worker.send({"command": "PING", "nonce": ping_nonce, "message_id": ping_message_id})
        pong = worker.read_event(10)
        if pong != {
            "event": "PONG",
            "instance_id": worker.instance_id,
            "nonce": ping_nonce,
            "message_id": ping_message_id,
        }:
            raise RuntimeError(f"S0_NONCE_ROUNDTRIP_MISMATCH:{pong!r}")
        stop_ack = worker.stop(stop_id)
        report.update({
            "ready": ready,
            "pong": pong,
            "stop_ack": stop_ack,
            "backend": "WSL2_UNSHARE_USER_MOUNT_NET_PID",
            "backend_configuration": worker.isolation,
            "cleanup_status": worker.cleanup_status,
            "diagnostics": worker.diagnostics(),
        })
    except BaseException as exc:
        producer_exception = f"{type(exc).__name__}:{exc}"
        report["producer_exception"] = producer_exception
        report["failure_code"] = getattr(exc, "code", "S0_RUNTIME_FAILURE")
        if worker is not None and worker.cleanup_status not in {"PROVEN", "TEST_DOUBLE_COMPLETE"}:
            try:
                worker.abort()
            except BaseException as cleanup_exc:
                report["cleanup_exception"] = f"{type(cleanup_exc).__name__}:{cleanup_exc}"
        report["cleanup_status"] = "NOT_STARTED" if worker is None else worker.cleanup_status
        if worker is not None:
            report["diagnostics"] = worker.diagnostics()

    producer_facts = {
        "producer_exception": producer_exception,
        "worker_start_requests": report["worker_start_requests"],
        "cleanup_status": report["cleanup_status"],
        "events_sha256": sha256_file(output / "events.jsonl") if (output / "events.jsonl").is_file() else None,
    }
    write_json(output / "S0_PRODUCER_FACTS.json", producer_facts)
    if expected is None:
        review = {
            "reviewer": "INDEPENDENT_S0_TRACE_REVIEWER",
            "verdict": "NOT_RUN" if report["worker_start_requests"] == 0 else "INCONCLUSIVE",
            "issues": [{"severity": "MISSING", "reason": "NO_REVIEW_INTENT_OR_START_TRACE"}],
            "evidence_event_count": 0,
        }
    else:
        review = review_s0_files(output / "events.jsonl", output / "review_intent.json")
    write_json(output / "S0_REVIEW.json", review)
    report["independent_review"] = review
    report["status"] = review["verdict"]
    report["claim_ceiling"] = (
        "S0 transport roundtrip and exact owned-child exit only; no S1 isolation-denial, state handoff, "
        "selected-process conformance, effect, promotion, same-c, B5 superiority, or ROI claim."
    )
    write_json(output / "S0_REPORT.json", report)
    print(json.dumps(report, sort_keys=True))
    return 0 if report["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
