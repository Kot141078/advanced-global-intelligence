from __future__ import annotations

import argparse
import base64
import hashlib
import json
import os
import secrets
import sys
import time
import uuid
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from cgdr_r1_6b.common import canonical_hash, write_json
from cgdr_r1_6b.prospective_observation import (
    build_observation_plan,
    build_phase_native_material,
    prepare_prospective_observation,
    review_observation_evidence,
)
from cgdr_r1_6b.s2_handoff import (
    PROFILE_BINDING,
    PROFILE_ID,
    TASK_ID,
    authority_public_map,
    build_current_source_view,
    build_delta_plan,
    build_open_prestate,
    build_source_inventory,
    make_e0_fence_payload,
    make_e1_payload,
    run_hold_gate,
    sha256_bytes,
    sign_authority_payload,
)
from cgdr_r1_6b.s2_native import emit_and_validate_s2_hold
from cgdr_r1_6b.s2_review import REQUIRED_STEPS, review_s2_evidence
from cgdr_r1_6b.signing import TestKeyStore
from cgdr_r1_6b.source import TASK_ID as SYNTHETIC_POLICY_TASK_ID
from cgdr_r1_6b.state_transfer import decode_state_b64, freeze_state, validate_state_bytes
from cgdr_r1_6b.supervisor import (
    CleanupUnprovenError,
    WorkerProcess,
    sha256_file,
    stage_s2_runtime,
    utc_now,
)


CURRENT_OBSERVATION_ACCEPTANCE_SCHEMA = "CGDR_CURRENT_PROSPECTIVE_OBSERVATION_ACCEPTANCE_V1"
CURRENT_OBSERVATION_ACCEPTANCE_STATUS = "ACCEPTED_FOR_SEPARATELY_AUTHORIZED_PROCESS_BOUND_QUALIFICATION_INPUT"
CURRENT_OBSERVATION_COORDINATOR_VERDICT = "ACCEPTED_BOUNDED_M01_CLOSURE_CURRENT_SINGLE_THREADED_FIRST_START_SEAM"
CURRENT_OBSERVATION_ACCEPTANCE_B_BYTES = 2905
CURRENT_OBSERVATION_ACCEPTANCE_B_SHA256 = "9565d06ce432f700aec2f004b543b4613c93cc9b5ea1277cf6198b2685ef1921"
CURRENT_OBSERVATION_NATIVE_LAYERS = {
    "shape": "PASS",
    "record_semantics": "PASS",
    "registered_evidence": "PASS",
    "bundle_links": "PASS",
}
CURRENT_OBSERVATION_CODE_PINS = {
    "prospective_observation.py": (
        "src/cgdr_r1_6b/prospective_observation.py",
        "d81c85ee213699b4b8637c56e5acb68a2673b4946e52f73873f3c65314b76f9f",
    ),
    "test_prospective_observation_r1_6k.py": (
        "tests/test_prospective_observation_r1_6k.py",
        "46bd743410c5852ca7bc5b0b8395aafba6dfeea78e27ce4277e949a9ee50436c",
    ),
    "run_observation_calibration.py": (
        "tools/run_observation_calibration.py",
        "7cf15929ae27a56e357dae01938d6fed6adb1b7fc26dd1552d565ef87aa1516d",
    ),
}
CURRENT_OBSERVATION_N_TECHNICAL_RETURN = {
    "bytes": 576641,
    "drive_id": "1ZdDhZuexXD56XeDQja6XSVSbQNm8zaSw",
    "sha256": "15f43b2622d1fb4db7bfd21e371a7db49288883d84fa43ebcad8adf47f6f0440",
}
CURRENT_OBSERVATION_N_COORDINATOR_INTAKE = {
    "zip_bytes": 6802,
    "zip_id": "1MAvvKig7t7UeFr68hQ4Qbg_KppkKBCQm",
    "zip_sha256": "9099b35e22658cbb610f1612cdfce87f3196f57bc2840c0889c1da15e39a62bc",
}


def _write_bytes(path: Path, value: bytes, mode: int = 0o600) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL, mode)
    with os.fdopen(fd, "wb") as stream:
        stream.write(value)
        stream.flush()
        os.fsync(stream.fileno())


def _append_jsonl(path: Path, value: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8", newline="\n") as stream:
        stream.write(json.dumps(value, sort_keys=True, ensure_ascii=False) + "\n")


def _snapshot(path: Path) -> dict[str, Any]:
    if not path.is_file():
        return {"exists": False, "path": str(path)}
    data = path.read_bytes()
    return {"exists": True, "path": str(path), "bytes": len(data), "sha256": sha256_bytes(data)}


def _windows_c_to_wsl(path: Path) -> str:
    value = path.resolve().as_posix()
    if not value.lower().startswith("c:/"):
        raise ValueError("S2 external masked targets must be on C drive")
    return "/mnt/c/" + value[3:]


def _read_events(path: Path) -> list[dict[str, Any]]:
    if not path.is_file():
        return []
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def _last_kind(path: Path, kind: str) -> dict[str, Any] | None:
    matches = [row for row in _read_events(path) if row.get("kind") == kind]
    return matches[-1] if matches else None


def _phase_times(
    window_start_ns: int,
    window_end_ns: int,
    planning_utc: str,
    basis_utc: str,
    changed_utc: str,
    commit_utc: str,
) -> dict[str, Any]:
    return {
        "planning_utc": planning_utc,
        "basis_utc": basis_utc,
        "changed_utc": changed_utc,
        "window_start_utc": planning_utc,
        "commit_utc": commit_utc,
        "window_end_utc": commit_utc,
        "perf_counter_start_ns": window_start_ns,
        "perf_counter_end_ns": window_end_ns,
        "clock_domains": {
            "semantic": "CGDR_TEST_TICKS",
            "native": "RFC3339_UTC_FROM_HOST_OBSERVATION",
            "host": "HOST_PERF_COUNTER_NS",
        },
    }


def _native_phase(
    gate: dict[str, Any],
    source: dict[str, Any],
    attempt_id: str,
    start_ns: int,
    end_ns: int,
    planning_utc: str,
    basis_utc: str,
    changed_utc: str,
    commit_utc: str,
) -> dict[str, Any]:
    return {
        **gate,
        "source": source,
        "attempt_id": attempt_id,
        "times": _phase_times(start_ns, end_ns, planning_utc, basis_utc, changed_utc, commit_utc),
        "grant_valid_until_utc": "2099-01-01T00:00:00Z",
    }


def _prospective_native_phase(
    gate: dict[str, Any],
    source: dict[str, Any],
    attempt_id: str,
    planning_utc: str,
    observation_evidence: dict[str, Any],
    observation_review: dict[str, Any],
    native_material: dict[str, Any],
) -> dict[str, Any]:
    phase_name = "S2_OPEN_CHECK"
    phase = observation_review["phase_results"][phase_name]
    begin = next(
        row for row in observation_evidence["snapshots"]
        if row["snapshot_id"] == phase["begin_snapshot_id"]
    )
    transaction_start = next(
        row for row in observation_evidence["transactions"] if row.get("state") == "STARTED"
    )
    transaction_commit = next(
        row for row in observation_evidence["transactions"] if row.get("state") == "COMMITTED"
    )
    times = {
        "planning_utc": planning_utc,
        "basis_utc": begin["read_transaction"]["end_clock"]["utc"],
        "changed_utc": transaction_start["clock"]["utc"],
        "window_start_utc": phase["window"]["start_utc"],
        "commit_utc": transaction_commit["clock"]["utc"],
        "window_end_utc": phase["window"]["end_utc"],
        "perf_counter_start_ns": int(phase["window"]["start_monotonic_ns"]),
        "perf_counter_end_ns": int(phase["window"]["end_monotonic_ns"]),
        "raw_points": {
            "planning": {"utc": planning_utc, "provenance": "S2_PLAN"},
            "basis": begin["read_transaction"]["end_clock"],
            "changed": transaction_start["clock"],
            "commit": transaction_commit["clock"],
            "window": phase["window"],
        },
    }
    return {
        **gate,
        "source": source,
        "attempt_id": attempt_id,
        "times": times,
        "grant_valid_until_utc": "2099-01-01T00:00:00Z",
        "prospective_native_material": native_material,
    }


def _make_manifest(attempt_id: str, role: str, fixture_root: Path) -> dict[str, Any]:
    files = []
    for relative in ("input_fixture.bin", "private/staged_private_placeholder.bin"):
        path = fixture_root / relative
        files.append({
            "relative_path": relative,
            "destination": "STAGE",
            "bytes": path.stat().st_size,
            "sha256": sha256_file(path),
            "mode": "0400",
        })
    return {
        "schema": "S2_FIXTURE_MANIFEST_V1",
        "task_id": TASK_ID,
        "attempt_id": attempt_id,
        "worker_role": role,
        "files": files,
        "collision_policy": "O_EXCL_NO_OVERWRITE",
    }


def _worker_view(worker: WorkerProcess | None, facts: dict[str, Any], event_log: Path) -> dict[str, Any]:
    result = dict(facts)
    result["instance_id"] = None if worker is None else worker.instance_id
    result["diagnostics"] = {} if worker is None else worker.diagnostics()
    result["raw_host_events"] = _read_events(event_log)
    return result


def _synthetic_native_precheck(output: Path, keys: TestKeyStore, public_map: dict[str, Any]) -> dict[str, Any]:
    attempt_id = "s2-r1-6i-pre-run-native-control"
    w0_binding = {
        "instance_id": "synthetic-w0-instance",
        "worker_pid": 101,
        "worker_start_ticks": 1001,
        "pid_namespace": "pid:[synthetic-w0]",
    }
    w1_binding = {
        "instance_id": "synthetic-w1-instance",
        "worker_pid": 102,
        "worker_start_ticks": 1002,
        "pid_namespace": "pid:[synthetic-w1]",
    }
    source = build_open_prestate(attempt_id, w0_binding["instance_id"])
    frozen = freeze_state(source)
    fence = sign_authority_payload(
        make_e0_fence_payload(
            attempt_id=attempt_id,
            source=source,
            w0_binding=w0_binding,
            checkpoint_raw_sha256=sha256_bytes(frozen["bytes"]),
        ),
        keys,
    )
    e1 = sign_authority_payload(
        make_e1_payload(
            attempt_id=attempt_id,
            w1_binding=w1_binding,
            source=source,
            checkpoint_raw_sha256=sha256_bytes(frozen["bytes"]),
            checkpoint_canonical_sha256=frozen["state_sha256"],
            fence_envelope=fence,
        ),
        keys,
    )
    current, _ = build_current_source_view(
        frozen["state"],
        attempt_id=attempt_id,
        w1_binding=w1_binding,
        e0_fence=fence,
        e1_envelope=e1,
        public_map=public_map,
    )
    gate = run_hold_gate(
        database=output / "synthetic_gate.sqlite3",
        source=current,
        keys=keys,
        public_map=public_map,
        attempt_id=attempt_id,
        instance_id=w1_binding["instance_id"],
        intent_capture_path=output / "synthetic_operation_intent.json",
    )
    phase = _native_phase(
        gate,
        current,
        attempt_id,
        100,
        200,
        "2026-09-06T12:00:00Z",
        "2026-09-06T12:00:01Z",
        "2026-09-06T12:00:02Z",
        "2026-09-06T12:00:03Z",
    )
    return emit_and_validate_s2_hold(phase, output / "native", evidence_scope="SYNTHETIC_REGRESSION")


def _check_offline_acceptance(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if value.get("status") != "PASS" or value.get("task_id") != TASK_ID:
        raise RuntimeError("final offline acceptance is not a frozen PASS for this task")
    return value


def _check_observation_acceptance(acceptance_path: Path, calibration_path: Path, code_root: Path) -> dict[str, Any]:
    acceptance_bytes = acceptance_path.read_bytes()
    acceptance_hash = hashlib.sha256(acceptance_bytes).hexdigest()
    calibration_bytes = calibration_path.read_bytes()
    acceptance = json.loads(acceptance_bytes.decode("utf-8-sig"))

    def require(condition: bool, reason: str) -> None:
        if not condition:
            raise RuntimeError(reason)

    require(acceptance.get("schema") == CURRENT_OBSERVATION_ACCEPTANCE_SCHEMA, "OBSERVATION_ACCEPTANCE_SCHEMA_MISMATCH")
    require(acceptance.get("status") == CURRENT_OBSERVATION_ACCEPTANCE_STATUS, "OBSERVATION_ACCEPTANCE_STATUS_MISMATCH")
    require(acceptance.get("profile_id") == PROFILE_ID, "OBSERVATION_ACCEPTANCE_PROFILE_ID_MISMATCH")
    require(acceptance.get("profile_binding") == PROFILE_BINDING, "OBSERVATION_ACCEPTANCE_PROFILE_BINDING_MISMATCH")
    require(acceptance.get("coordinator_verdict") == CURRENT_OBSERVATION_COORDINATOR_VERDICT, "OBSERVATION_ACCEPTANCE_COORDINATOR_VERDICT_MISMATCH")

    findings = acceptance.get("accepted_findings") or {}
    for finding in ("K01", "K02", "K03"):
        require(findings.get(finding) == "RETAINED_PASS", f"OBSERVATION_ACCEPTANCE_{finding}_NOT_RETAINED_PASS")
    for finding in ("L01", "L02", "L04"):
        require(findings.get(finding) == "RETAINED", f"OBSERVATION_ACCEPTANCE_{finding}_NOT_RETAINED")
    require(
        findings.get("M01") == "CLOSED_WITHIN_CURRENT_SINGLE_THREADED_FIRST_START_SEAM",
        "OBSERVATION_ACCEPTANCE_M01_NOT_CLOSED",
    )
    require(acceptance.get("actual_process_observation_qualification") == "NOT_RUN", "OBSERVATION_ACCEPTANCE_ACTUAL_PROCESS_STATE_INVALID")
    require(acceptance.get("historical_full_interval_absence") == "NOT_ESTABLISHED", "OBSERVATION_ACCEPTANCE_HISTORICAL_INTERVAL_CLAIM_INVALID")
    require(acceptance.get("r1_6n_technical_return") == CURRENT_OBSERVATION_N_TECHNICAL_RETURN, "OBSERVATION_ACCEPTANCE_N_TECHNICAL_RETURN_LINEAGE_MISMATCH")
    intake = acceptance.get("coordinator_intake") or {}
    require(
        {key: intake.get(key) for key in CURRENT_OBSERVATION_N_COORDINATOR_INTAKE} == CURRENT_OBSERVATION_N_COORDINATOR_INTAKE,
        "OBSERVATION_ACCEPTANCE_N_COORDINATOR_INTAKE_LINEAGE_MISMATCH",
    )

    calibration_hash = hashlib.sha256(calibration_bytes).hexdigest()
    calibration_binding = acceptance.get("current_calibration") or {}
    require(calibration_binding.get("bytes") == len(calibration_bytes), "OBSERVATION_CALIBRATION_BYTES_MISMATCH")
    require(calibration_binding.get("sha256") == calibration_hash, "OBSERVATION_CALIBRATION_HASH_MISMATCH")
    calibration = json.loads(calibration_bytes.decode("utf-8-sig"))
    require(calibration.get("status") == "PASS", "OBSERVATION_CALIBRATION_STATUS_NOT_PASS")
    require(calibration.get("unique_calibration_cases") == 4, "OBSERVATION_CALIBRATION_CASE_COUNT_MISMATCH")
    for key in ("worker_start_requests", "helper_starts", "wsl_launches", "s2_attempts"):
        require(calibration.get(key) == 0, f"OBSERVATION_CALIBRATION_{key.upper()}_NONZERO")
    positive_hold = calibration.get("positive_hold") or {}
    require(positive_hold.get("effect_delta") == 0, "OBSERVATION_CALIBRATION_HOLD_EFFECT_DELTA_NONZERO")
    require(positive_hold.get("promotion_delta") == 0, "OBSERVATION_CALIBRATION_HOLD_PROMOTION_DELTA_NONZERO")
    require(positive_hold.get("native_layers") == CURRENT_OBSERVATION_NATIVE_LAYERS, "OBSERVATION_CALIBRATION_NATIVE_LAYER_NOT_PASS")
    require(
        calibration.get("committed_sql_change_counts")
        == {
            "effects": {"INSERT": 3, "UPDATE": 2, "DELETE": 2},
            "promotions": {"INSERT": 1, "UPDATE": 1, "DELETE": 1},
        },
        "OBSERVATION_CALIBRATION_SQL_COUNTS_MISMATCH",
    )

    claimed_code = acceptance.get("current_code") or {}
    code_hashes = {}
    for name, (relative, expected_hash) in CURRENT_OBSERVATION_CODE_PINS.items():
        path = code_root / relative
        require(path.is_file(), f"OBSERVATION_CURRENT_CODE_MISSING:{relative}")
        actual_hash = sha256_file(path)
        claimed_hash = (claimed_code.get(name) or {}).get("sha256")
        require(claimed_hash == expected_hash, f"OBSERVATION_CURRENT_CODE_CLAIM_MISMATCH:{relative}")
        require(actual_hash == expected_hash, f"OBSERVATION_CURRENT_CODE_HASH_MISMATCH:{relative}")
        code_hashes[relative] = actual_hash

    require(
        len(acceptance_bytes) == CURRENT_OBSERVATION_ACCEPTANCE_B_BYTES,
        "OBSERVATION_ACCEPTANCE_ARTIFACT_BYTES_MISMATCH",
    )
    require(
        acceptance_hash == CURRENT_OBSERVATION_ACCEPTANCE_B_SHA256,
        "OBSERVATION_ACCEPTANCE_ARTIFACT_HASH_MISMATCH",
    )

    return {
        "status": "PASS_CURRENT_N_OBSERVATION_ACCEPTANCE_BOUND",
        "current_acceptance": acceptance,
        "current_calibration": calibration,
        "acceptance_sha256": acceptance_hash,
        "calibration_sha256": calibration_hash,
        "current_code_hashes": code_hashes,
    }


def _hashes(paths: list[Path]) -> dict[str, dict[str, Any]]:
    return {str(path.resolve()): {"bytes": path.stat().st_size, "sha256": sha256_file(path)} for path in paths}


def _verify_baseline_bindings(code_root: Path, bindings: dict[str, Any]) -> dict[str, Any]:
    allowed_delta = {
        "tools/run_s2.py",
        "src/cgdr_r1_6b/native_adapter.py",
        "src/cgdr_r1_6b/s2_handoff.py",
        "src/cgdr_r1_6b/s2_native.py",
    }
    rows = []
    for entry in bindings.get("files", []):
        archive_path = str(entry.get("archive_path", ""))
        relative = archive_path[5:] if archive_path.startswith("code/") else archive_path
        path = code_root / relative
        actual = {"bytes": path.stat().st_size, "sha256": sha256_file(path)} if path.is_file() else {"bytes": None, "sha256": None}
        changed = actual["bytes"] != entry.get("bytes") or actual["sha256"] != entry.get("sha256")
        rows.append({"relative_path": relative, "expected_bytes": entry.get("bytes"), "expected_sha256": entry.get("sha256"), "actual": actual, "classification": "DECLARED_S2_DELTA" if changed and relative in allowed_delta else ("UNCHANGED" if not changed else "UNAUTHORIZED_DELTA")})
    unauthorized = [row for row in rows if row["classification"] == "UNAUTHORIZED_DELTA"]
    if unauthorized:
        raise RuntimeError(f"accepted semantic/core hash guard failed: {unauthorized}")
    return {"status": "PASS", "declared_delta": sorted(allowed_delta), "rows": rows}


def main() -> int:
    parser = argparse.ArgumentParser(description="One bounded W0-to-W1 OPEN-state S2 preflight")
    parser.add_argument("--execute-authorized", action="store_true")
    parser.add_argument("--distro", default="Ubuntu")
    parser.add_argument("--attempt-id", required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--private-key-dir", type=Path, required=True)
    parser.add_argument("--worker", type=Path, required=True)
    parser.add_argument("--launcher", type=Path, required=True)
    parser.add_argument("--offline-acceptance", type=Path, required=True)
    parser.add_argument("--observation-acceptance", type=Path, required=True)
    parser.add_argument("--observation-calibration", type=Path, required=True)
    parser.add_argument("--baseline-bindings", type=Path, required=True)
    parser.add_argument("--accepted-s1-boundary", type=Path, required=True)
    parser.add_argument("--stage-w0", required=True)
    parser.add_argument("--stage-w1", required=True)
    args = parser.parse_args()
    if not args.execute_authorized:
        print("NOT_RUN: live S2 requires the explicit --execute-authorized flag", file=sys.stderr)
        return 3
    if not args.attempt_id.startswith("s2-r1-6i-"):
        raise ValueError("attempt id is outside the R1.6I namespace")
    if not args.stage_w0.startswith("/tmp/cgdr-r1-6i-s2-w0-") or not args.stage_w1.startswith("/tmp/cgdr-r1-6i-s2-w1-"):
        raise ValueError("S2 stages are outside fixed role prefixes")
    if args.stage_w0 == args.stage_w1:
        raise ValueError("W0 and W1 stages must be distinct")
    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=False)
    setup_log = output / "setup.jsonl"
    chronology_log = output / "S2_CHRONOLOGY.jsonl"
    w0_events, w1_events = output / "w0_events.jsonl", output / "w1_events.jsonl"
    chronology: list[dict[str, Any]] = []

    def step(name: str, **facts: Any) -> None:
        row = {"sequence": len(chronology) + 1, "step": name, "host_utc": utc_now(), "host_perf_counter_ns": time.perf_counter_ns(), "clock_domain": "HOST_PERF_COUNTER_NS", **facts}
        chronology.append(row)
        _append_jsonl(chronology_log, row)

    report: dict[str, Any] = {
        "task_id": TASK_ID,
        "profile_id": PROFILE_ID,
        "profile_binding": PROFILE_BINDING,
        "status": "INCONCLUSIVE",
        "worker_start_requests": 0,
        "s2_attempts": 0,
        "endpoint_helper_starts": 0,
        "measured_matrix_started": False,
        "matrix_episodes_executed": 0,
        "matrix_checkpoints_observed": 0,
        "matrix_effects": None,
        "matrix_promotions": None,
        "model_calls": 0,
        "model_evidence": "NOT_EXPOSED",
    }
    w0: WorkerProcess | None = None
    w1: WorkerProcess | None = None
    w0_facts: dict[str, Any] = {}
    w1_facts: dict[str, Any] = {}
    source: dict[str, Any] = {}
    inventory: dict[str, Any] = {}
    disk_receipt: dict[str, Any] = {}
    delta_plans: dict[str, Any] = {}
    delta_hashes: dict[str, str] = {}
    authority: dict[str, Any] = {}
    gate: dict[str, Any] = {}
    native: dict[str, Any] = {}
    prospective_observation_evidence: dict[str, Any] = {}
    prospective_observation_review: dict[str, Any] = {}
    prospective_broker = None
    prospective_observer = None
    s1_delta: dict[str, Any] = {}
    canary_before: dict[str, Any] = {}
    canary_after: dict[str, Any] = {}
    public_map: dict[str, Any] = {}
    frozen = False
    failure: BaseException | None = None
    try:
        offline = _check_offline_acceptance(args.offline_acceptance.resolve())
        code_root = args.worker.resolve().parents[2]
        observation_binding = _check_observation_acceptance(
            args.observation_acceptance.resolve(), args.observation_calibration.resolve(), code_root
        )
        baseline_bindings = json.loads(args.baseline_bindings.read_text(encoding="utf-8"))
        baseline_guard = _verify_baseline_bindings(code_root, baseline_bindings)
        accepted_boundary = json.loads(args.accepted_s1_boundary.read_text(encoding="utf-8"))
        if accepted_boundary.get("candidate", {}).get("classification") != "S1_CANDIDATE_HARDENED":
            raise RuntimeError("accepted S1 boundary binding missing")
        keys = TestKeyStore(args.private_key_dir.resolve())
        public_map = authority_public_map(keys)
        write_json(output / "PUBLIC_SIGNER_MAP.json", public_map)
        pre_native = {
            "status": "REUSED_CURRENT_R1_6N_CALIBRATION_BOUND_BY_COORDINATOR_ACCEPTANCE",
            "acceptance_path": str(args.observation_acceptance.resolve()),
            "acceptance_sha256": observation_binding["acceptance_sha256"],
            "calibration_path": str(args.observation_calibration.resolve()),
            "calibration_sha256": observation_binding["calibration_sha256"],
            "native_layers": observation_binding["current_calibration"]["positive_hold"]["native_layers"],
            "claim_boundary": "Local process-free calibration only; actual future process evidence remains to be collected.",
        }

        external_root = output / "external_trusted"
        checkpoint_canary = external_root / "checkpoint_store" / "checkpoint_store_canary.bin"
        private_canary = external_root / "private" / "private_canary.bin"
        _write_bytes(checkpoint_canary, b"S2_CHECKPOINT_STORE_CANARY::" + secrets.token_bytes(48))
        _write_bytes(private_canary, b"S2_PRIVATE_CANARY::" + secrets.token_bytes(48))
        canary_before = {
            "checkpoint_store_canary": _snapshot(checkpoint_canary),
            "private_canary": _snapshot(private_canary),
        }
        fixture_roots: dict[str, Path] = {}
        plan_paths: dict[str, Path] = {}
        manifest_paths: dict[str, Path] = {}
        for role, stage_dir in (("W0", args.stage_w0), ("W1", args.stage_w1)):
            root = output / "fixture_source" / role.casefold()
            input_value = json.dumps({"task_id": TASK_ID, "attempt_id": args.attempt_id, "worker_role": role, "purpose": "bounded-state-channel-control"}, sort_keys=True, separators=(",", ":")).encode()
            _write_bytes(root / "input_fixture.bin", input_value)
            _write_bytes(root / "private" / "staged_private_placeholder.bin", b"S2_STAGED_PRIVATE_MASK_CANARY::" + secrets.token_bytes(32))
            plan = build_delta_plan(
                attempt_id=args.attempt_id,
                worker_role=role,
                stage_dir=stage_dir,
                input_sha256=sha256_bytes(input_value),
                input_bytes=len(input_value),
                checkpoint_canary_windows=str(checkpoint_canary),
                checkpoint_canary_wsl=_windows_c_to_wsl(checkpoint_canary),
                private_canary_windows=str(private_canary),
                private_canary_wsl=_windows_c_to_wsl(private_canary),
            )
            plan_path = output / "pre_run" / role.casefold() / "S2_DELTA_PLAN.json"
            manifest_path = output / "pre_run" / role.casefold() / "S2_FIXTURE_MANIFEST.json"
            write_json(plan_path, plan)
            write_json(manifest_path, _make_manifest(args.attempt_id, role, root))
            fixture_roots[role], plan_paths[role], manifest_paths[role] = root, plan_path, manifest_path
            delta_plans[role], delta_hashes[role] = plan, sha256_file(plan_path)

        staged_w0 = stage_s2_runtime(args.distro, args.worker, args.stage_w0, args.attempt_id, "W0", plan_paths["W0"], manifest_paths["W0"], fixture_roots["W0"], setup_log, local_launcher=args.launcher)
        staged_w1 = stage_s2_runtime(args.distro, args.worker, args.stage_w1, args.attempt_id, "W1", plan_paths["W1"], manifest_paths["W1"], fixture_roots["W1"], setup_log, local_launcher=args.launcher)
        w0 = WorkerProcess(args.distro, staged_w0, w0_events, "S2", "W0_OPEN_STATE")
        w1 = WorkerProcess(args.distro, staged_w1, w1_events, "S2", "W1_OPEN_STATE")
        source = build_open_prestate(args.attempt_id, w0.instance_id)
        inventory = build_source_inventory(source)
        carried = freeze_state(source)
        write_json(output / "S2_SOURCE_PRESTATE.json", source)
        write_json(output / "S2_SOURCE_INVENTORY.json", inventory)
        _write_bytes(output / "S2_PRESTATE_BYTES.json", carried["bytes"])

        ids = {
            "w0_ping_nonce": secrets.token_urlsafe(32),
            "w0_ping_id": f"s2-w0-ping-{uuid.uuid4()}",
            "w0_delta_id": f"s2-w0-delta-{uuid.uuid4()}",
            "w0_load_id": f"s2-w0-load-{uuid.uuid4()}",
            "w0_checkpoint_id": f"s2-w0-checkpoint-{uuid.uuid4()}",
            "w0_wait_id": f"s2-w0-wait-{uuid.uuid4()}",
            "w0_release_id": f"s2-w0-release-{uuid.uuid4()}",
            "w0_continue_id": f"s2-w0-continue-{uuid.uuid4()}",
            "w0_stop_id": f"s2-w0-stop-{uuid.uuid4()}",
            "w1_ping_nonce": secrets.token_urlsafe(32),
            "w1_ping_id": f"s2-w1-ping-{uuid.uuid4()}",
            "w1_delta_id": f"s2-w1-delta-{uuid.uuid4()}",
            "w1_restore_id": f"s2-w1-restore-{uuid.uuid4()}",
            "w1_checkpoint_id": f"s2-w1-checkpoint-{uuid.uuid4()}",
            "w1_stop_id": f"s2-w1-stop-{uuid.uuid4()}",
            "operation_id": f"operation:{args.attempt_id}:open-hold",
            "commit_record_id": f"commit:{args.attempt_id}:open-hold",
        }
        planning_utc = utc_now()
        s2_plan = {
            "schema": "ONE_BOUNDED_OPEN_STATE_HANDOFF_S2_PLAN_V1",
            "task_id": TASK_ID,
            "profile_id": PROFILE_ID,
            "profile_binding": PROFILE_BINDING,
            "attempt_id": args.attempt_id,
            "attempt_limit": 1,
            "worker_start_limit": 2,
            "endpoint_helper_limit": 0,
            "w0_instance_id": w0.instance_id,
            "w1_instance_id": w1.instance_id,
            "stage_dirs": {"W0": args.stage_w0, "W1": args.stage_w1},
            "delta_plan_sha256": delta_hashes,
            "prestate_raw_sha256": sha256_bytes(carried["bytes"]),
            "prestate_canonical_sha256": carried["state_sha256"],
            "source_inventory_sha256": canonical_hash(inventory),
            "protocol_ids": ids,
            "required_steps": list(REQUIRED_STEPS),
            "expected_gate": {"admission": "ADMITTED", "q_state": "OPEN", "action_gate": "HOLD", "effect_delta": 0, "promotion_delta": 0},
            "semantic_ticks": {"source_open": 10, "checkpoint": 40, "post_boundary_open": 45, "qsf_expiry": 80},
            "planning_observed_utc": planning_utc,
            "claim_ceiling": "One W0-to-W1 process replacement and OPEN/HOLD observation; no resolved check, matrix, same-c, or live authority.",
        }
        write_json(output / "S2_PLAN.json", s2_plan)
        observation_plan = build_observation_plan(
            task_id=TASK_ID,
            cell_id="S2_OPEN_HANDOFF",
            attempt_id=args.attempt_id,
            checkpoint="S2_OPEN_CHECK",
            database=output / "s2_effects.sqlite3",
            path_boundary_root=output,
            operation_scope={
                "task_id": SYNTHETIC_POLICY_TASK_ID,
                "action": "synthetic_accept",
                "operation_id": ids["operation_id"],
                "cell_id": "S2_OPEN_HANDOFF",
                "attempt_id": args.attempt_id,
                "checkpoint": "S2_OPEN_CHECK",
                "instance_id": w1.instance_id,
                "commit_record_id": ids["commit_record_id"],
            },
            expected_outcome="HOLD_NO_EFFECT",
        )
        write_json(output / "S2_OBSERVATION_PLAN.json", observation_plan)
        prospective_broker, prospective_observer = prepare_prospective_observation(
            plan=observation_plan,
            output=output / "prospective_observation",
        )
        readiness = prospective_observer.readiness_receipt()
        if readiness.get("status") != "READY":
            raise RuntimeError("prospective observation barrier not ready before first worker start")
        write_json(output / "OBSERVATION_READINESS.json", readiness)
        s1_delta = {
            "task_id": TASK_ID,
            "status": "STATIC_CONFIG_VERIFIED_FOR_S2_OBJECT_DELTA",
            "accepted_s1_boundary_sha256": sha256_file(args.accepted_s1_boundary),
            "accepted_s1_classification": accepted_boundary["candidate"]["classification"],
            "baseline_code_bindings_sha256": sha256_file(args.baseline_bindings),
            "baseline_code_bindings": baseline_bindings,
            "baseline_hash_guard": baseline_guard,
            "reused_mechanisms": [
                "WSL2 Ubuntu", "user/mount/network/PID namespaces", "read-only stage bind",
                "private writable scratch tmpfs", "private and /home/root/mnt mode-000 masks",
                "zero capability sets", "NoNewPrivs=1", "FDs 0/1/2", "parent-only receipt channel", "direct parent waitpid",
            ],
            "new_objects_and_access": [
                "W0 and W1 role-specific stages", "bounded LOAD/CHECKPOINT/RESTORE frames",
                "external host create-only checkpoint artifact", "external signed E0 fence and E1 current attestation",
            ],
            "not_reused_as_evidence": ["historical S1 object denials", "historical S1 endpoint observations"],
            "no_endpoint_helper": True,
            "network_isolation_unchanged": True,
            "trusted_writers_not_mounted": True,
            "delta_plans": delta_hashes,
        }
        write_json(output / "S1_TO_S2_DELTA.json", s1_delta)
        protected = [
            code_root / "src" / "cgdr_r1_6b" / name
            for name in (
                "worker.py", "supervisor.py", "s0_launcher.py", "s2_handoff.py", "s2_review.py",
                "s2_native.py", "prospective_observation.py", "producer.py", "receiver.py", "broker.py",
                "observer.py", "native_adapter.py", "state_transfer.py",
            )
        ] + [
            Path(__file__).resolve(), args.offline_acceptance.resolve(), args.observation_acceptance.resolve(),
            args.observation_calibration.resolve(),
            args.baseline_bindings.resolve(), args.accepted_s1_boundary.resolve(),
            output / "S2_PLAN.json", output / "S2_OBSERVATION_PLAN.json", output / "OBSERVATION_READINESS.json",
            output / "S1_TO_S2_DELTA.json", plan_paths["W0"], plan_paths["W1"],
            manifest_paths["W0"], manifest_paths["W1"],
        ]
        validator = code_root / "dependencies" / "Kot141078" / "c-hardening-pack" / "47fed105d7b1df1df7375aa203a551b0f684c13d" / "tools" / "validate_runtime_integrity_extension.py"
        protected.append(validator)
        freeze_receipt = {
            "task_id": TASK_ID,
            "attempt_id": args.attempt_id,
            "freeze_stage": "BEFORE_FIRST_WORKER_START_REQUEST",
            "created_utc": utc_now(),
            "files": _hashes(protected),
            "worker_instances_preallocated_without_start": {"W0": w0.instance_id, "W1": w1.instance_id},
            "stage_receipts": {"W0": staged_w0.stage_receipt, "W1": staged_w1.stage_receipt},
            "offline_acceptance": offline,
            "current_observation_acceptance": {
                "path": str(args.observation_acceptance.resolve()),
                "bytes": args.observation_acceptance.resolve().stat().st_size,
                "sha256": observation_binding["acceptance_sha256"],
            },
            "current_observation_calibration": {
                "path": str(args.observation_calibration.resolve()),
                "bytes": args.observation_calibration.resolve().stat().st_size,
                "sha256": observation_binding["calibration_sha256"],
            },
            "pre_run_native": pre_native,
            "future_edits_or_retry_authorized": False,
        }
        write_json(output / "IMPLEMENTATION_FREEZE.json", freeze_receipt)
        frozen = True

        report["s2_attempts"] = 1
        report["worker_start_requests"] = 1
        step("W0_START_REQUEST", instance_id=w0.instance_id)
        ready0 = prospective_observer.invoke_first_start(lambda: w0.start(10))
        w0_facts["ready"] = ready0
        step("W0_CHILD_BOUND", instance_id=w0.instance_id, binding=w0.child_binding)
        step("W0_SECURITY_BOUND", instance_id=w0.instance_id, security_receipt_sha256=(w0.child_security or {}).get("security_receipt_sha256"))
        step("W0_READY", instance_id=w0.instance_id)
        w0.send({"command": "PING", "nonce": ids["w0_ping_nonce"], "message_id": ids["w0_ping_id"]})
        pong0 = w0.read_event(10)
        if pong0 != {"event": "PONG", "instance_id": w0.instance_id, "nonce": ids["w0_ping_nonce"], "message_id": ids["w0_ping_id"]}:
            raise RuntimeError("W0_PONG_BINDING_MISMATCH")
        w0_facts["pong"] = pong0
        step("W0_PONG", instance_id=w0.instance_id)
        w0.send({"command": "S2_DELTA", "attempt_id": args.attempt_id, "worker_role": "W0", "plan_sha256": delta_hashes["W0"], "message_id": ids["w0_delta_id"]})
        delta0 = w0.read_event(10)
        w0_facts["delta_result"] = delta0
        if delta0.get("event") != "S2_DELTA_RESULT" or delta0.get("result", {}).get("stopped_after_forbidden_success") is not None:
            raise RuntimeError("W0_S1_DELTA_CONTROL_FAILURE")
        step("W0_DELTA_CONTROLS", instance_id=w0.instance_id)
        w0.send({"command": "LOAD", "state_b64": carried["state_b64"], "state_sha256": carried["state_sha256"], "message_id": ids["w0_load_id"]})
        load_ack = w0.read_event(10)
        w0_facts["load_ack"] = load_ack
        if load_ack.get("event") != "LOAD_ACK" or load_ack.get("state_sha256") != carried["state_sha256"] or load_ack.get("instance_id") != w0.instance_id:
            raise RuntimeError("W0_LOAD_ACK_INVALID")
        step("W0_LOAD_ACK", instance_id=w0.instance_id)
        w0.send({"command": "CHECKPOINT", "message_id": ids["w0_checkpoint_id"]})
        checkpoint0 = w0.read_event(10)
        w0_facts["checkpoint"] = checkpoint0
        raw0, state0, decode0 = decode_state_b64(checkpoint0.get("state_b64"))
        if decode0 or raw0 is None or state0 is None or raw0 != carried["bytes"] or checkpoint0.get("checkpoint_seq") != 1:
            raise RuntimeError(f"W0_CHECKPOINT_INVALID:{decode0}")
        step("W0_CHECKPOINT", instance_id=w0.instance_id)
        checkpoint_path = external_root / "checkpoint_store" / "w0_checkpoint.bin"
        _write_bytes(checkpoint_path, raw0)
        readback = checkpoint_path.read_bytes()
        disk_receipt = {
            "path": str(checkpoint_path),
            "write_b64": base64.b64encode(raw0).decode("ascii"),
            "readback_b64": base64.b64encode(readback).decode("ascii"),
            "bytes": len(readback),
            "write_raw_sha256": sha256_bytes(raw0),
            "readback_raw_sha256": sha256_bytes(readback),
            "canonical_sha256": canonical_hash(json.loads(readback.decode("utf-8"))),
            "create_policy": "O_EXCL_NO_OVERWRITE_FSYNC",
        }
        write_json(output / "W0_CHECKPOINT_DISK_READBACK.json", disk_receipt)
        w0.send({"command": "SHAM_WAIT", "wait_id": ids["w0_wait_id"], "message_id": ids["w0_wait_id"]})
        sham = w0.read_event(10); w0_facts["sham_wait"] = sham
        if sham.get("event") != "SHAM_WAITING" or sham.get("wait_id") != ids["w0_wait_id"]:
            raise RuntimeError("W0_SHAM_WAIT_INVALID")
        step("W0_SHAM_WAIT", instance_id=w0.instance_id)
        w0.send({"command": "RELEASE", "release_id": ids["w0_release_id"], "message_id": ids["w0_release_id"]})
        release = w0.read_event(10); w0_facts["release"] = release
        if release.get("event") != "RELEASED" or release.get("release_id") != ids["w0_release_id"]:
            raise RuntimeError("W0_RELEASE_INVALID")
        step("W0_RELEASE", instance_id=w0.instance_id)
        w0.send({"command": "CONTINUE", "continue_id": ids["w0_continue_id"], "message_id": ids["w0_continue_id"]})
        continued = w0.read_event(10); w0_facts["continued"] = continued
        if continued.get("event") != "CONTINUED" or continued.get("continue_id") != ids["w0_continue_id"] or continued.get("state_sha256") != carried["state_sha256"]:
            raise RuntimeError("W0_CONTINUE_INVALID")
        step("W0_CONTINUE", instance_id=w0.instance_id)
        fence = sign_authority_payload(make_e0_fence_payload(attempt_id=args.attempt_id, source=source, w0_binding=w0.child_binding or {}, checkpoint_raw_sha256=sha256_bytes(readback)), keys)
        authority["e0_fence"] = fence
        _append_jsonl(output / "CURRENT_AUTHORITY_RECEIPTS.jsonl", {"kind": "E0_FENCE", "envelope": fence})
        step("E0_FENCED", instance_id=w0.instance_id, envelope_sha256=canonical_hash(fence))
        stop0 = w0.stop(ids["w0_stop_id"]); w0_facts["stop_ack"] = stop0
        step("W0_STOP_ACK", instance_id=w0.instance_id)
        exit0 = _last_kind(w0_events, "EXIT_OBSERVED"); w0_facts["exit_event"] = exit0
        if w0.cleanup_status != "PROVEN" or not exit0:
            raise CleanupUnprovenError("W0 direct-wait cleanup not proven")
        step("W0_OS_WAIT_EXIT", instance_id=w0.instance_id, return_code=exit0.get("return_code"), cleanup_status=w0.cleanup_status)

        report["worker_start_requests"] = 2
        step("W1_START_REQUEST", instance_id=w1.instance_id)
        ready1 = w1.start(10); w1_facts["ready"] = ready1
        step("W1_CHILD_BOUND", instance_id=w1.instance_id, binding=w1.child_binding)
        step("W1_SECURITY_BOUND", instance_id=w1.instance_id, security_receipt_sha256=(w1.child_security or {}).get("security_receipt_sha256"))
        step("W1_READY", instance_id=w1.instance_id)
        w1.send({"command": "PING", "nonce": ids["w1_ping_nonce"], "message_id": ids["w1_ping_id"]})
        pong1 = w1.read_event(10)
        if pong1 != {"event": "PONG", "instance_id": w1.instance_id, "nonce": ids["w1_ping_nonce"], "message_id": ids["w1_ping_id"]}:
            raise RuntimeError("W1_PONG_BINDING_MISMATCH")
        w1_facts["pong"] = pong1
        step("W1_PONG", instance_id=w1.instance_id)
        w1.send({"command": "S2_DELTA", "attempt_id": args.attempt_id, "worker_role": "W1", "plan_sha256": delta_hashes["W1"], "message_id": ids["w1_delta_id"]})
        delta1 = w1.read_event(10); w1_facts["delta_result"] = delta1
        if delta1.get("event") != "S2_DELTA_RESULT" or delta1.get("result", {}).get("stopped_after_forbidden_success") is not None:
            raise RuntimeError("W1_S1_DELTA_CONTROL_FAILURE")
        step("W1_DELTA_CONTROLS", instance_id=w1.instance_id)
        w1.send({"command": "RESTORE", "state_b64": base64.b64encode(readback).decode("ascii"), "state_sha256": sha256_bytes(readback), "checkpoint_seq": 1, "message_id": ids["w1_restore_id"]})
        restore = w1.read_event(10); w1_facts["restore"] = restore
        if restore.get("event") != "RESTORED" or restore.get("state_sha256") != sha256_bytes(readback) or restore.get("checkpoint_seq") != 1:
            raise RuntimeError("W1_RESTORE_ACK_INVALID")
        step("W1_RESTORE", instance_id=w1.instance_id)
        w1.send({"command": "CHECKPOINT", "message_id": ids["w1_checkpoint_id"]})
        checkpoint1 = w1.read_event(10); w1_facts["checkpoint"] = checkpoint1
        raw1, state1, decode1 = decode_state_b64(checkpoint1.get("state_b64"))
        if decode1 or raw1 != readback or state1 is None or checkpoint1.get("checkpoint_seq") != 1:
            raise RuntimeError(f"W1_FULL_CHECKPOINT_INVALID:{decode1}")
        state_check = validate_state_bytes(raw1, source, stated_hash=checkpoint1.get("state_sha256"))
        if state_check["status"] != "PASS":
            raise RuntimeError(f"W1_STATE_CARRIAGE_FAILED:{state_check['issues']}")
        step("W1_CHECKPOINT", instance_id=w1.instance_id)
        write_json(output / "W1_FULL_CHECKPOINT.json", checkpoint1)

        e1_changed_utc = utc_now()
        e1 = sign_authority_payload(make_e1_payload(attempt_id=args.attempt_id, w1_binding=w1.child_binding or {}, source=source, checkpoint_raw_sha256=sha256_bytes(readback), checkpoint_canonical_sha256=canonical_hash(state1), fence_envelope=authority["e0_fence"]), keys)
        authority["e1_current"] = e1
        _append_jsonl(output / "CURRENT_AUTHORITY_RECEIPTS.jsonl", {"kind": "E1_CURRENT", "envelope": e1})
        step("E1_ISSUED", instance_id=w1.instance_id, envelope_sha256=canonical_hash(e1))
        current_source, transition = build_current_source_view(state1, attempt_id=args.attempt_id, w1_binding=w1.child_binding or {}, e0_fence=authority["e0_fence"], e1_envelope=e1, public_map=public_map)
        authority["current_source_view"] = current_source
        authority["epoch_transition"] = transition
        write_json(output / "CURRENT_SOURCE_VIEW.json", current_source)
        write_json(output / "CURRENT_EPOCH_TRANSITION.json", transition)
        gate_start_ns, gate_basis_utc = time.perf_counter_ns(), utc_now()
        gate = run_hold_gate(
            broker=prospective_broker,
            observation=prospective_observer,
            source=current_source,
            keys=keys,
            public_map=public_map,
            attempt_id=args.attempt_id,
            instance_id=w1.instance_id,
            intent_capture_path=output / "IMMUTABLE_OPERATION_INTENT.json",
        )
        step("W1_ADMISSION", instance_id=w1.instance_id, admission=gate["decision"]["admission"], q_state=gate["decision"]["q_state"])
        step("W1_BROKER_HOLD", instance_id=w1.instance_id, action_gate=gate["decision"]["action_gate"], broker_result=gate["broker_result"]["result"])
        gate_end_ns, gate_commit_utc = time.perf_counter_ns(), utc_now()
        stop1 = w1.stop(ids["w1_stop_id"]); w1_facts["stop_ack"] = stop1
        step("W1_STOP_ACK", instance_id=w1.instance_id)
        exit1 = _last_kind(w1_events, "EXIT_OBSERVED"); w1_facts["exit_event"] = exit1
        if w1.cleanup_status != "PROVEN" or not exit1:
            raise CleanupUnprovenError("W1 direct-wait cleanup not proven")
        step("W1_OS_WAIT_EXIT", instance_id=w1.instance_id, return_code=exit1.get("return_code"), cleanup_status=w1.cleanup_status)
        prospective_observer.mark_owned_exit(
            synthetic=False,
            binding={
                "instance_id": w1.instance_id,
                "child_binding": w1.child_binding,
                "inner_exit": (w1.diagnostics() or {}).get("inner_exit"),
                "cleanup_status": w1.cleanup_status,
            },
        )
        prospective_observation_evidence = prospective_observer.finalize()
        prospective_observation_review = review_observation_evidence(prospective_observation_evidence)
        write_json(output / "PROSPECTIVE_OBSERVATION_REVIEW.json", prospective_observation_review)
        if prospective_observation_review.get("verdict") != "PASS_COMPLETE_WITHIN_DECLARED_SURFACES":
            raise RuntimeError("ACTUAL_PROSPECTIVE_OBSERVATION_NOT_COMPLETE")
        native_material = build_phase_native_material(
            prospective_observation_evidence,
            prospective_observation_review,
            "S2_OPEN_CHECK",
        )
        if native_material.get("status") != "COMPLETE_NO_COMMITTED_CHANGE":
            raise RuntimeError("ACTUAL_PROSPECTIVE_NATIVE_MATERIAL_REFUSED")
        write_json(output / "PROSPECTIVE_NATIVE_MATERIAL.json", native_material)
        native_phase = _prospective_native_phase(
            gate,
            current_source,
            args.attempt_id,
            planning_utc,
            prospective_observation_evidence,
            prospective_observation_review,
            native_material,
        )
        native = emit_and_validate_s2_hold(native_phase, output / "native_actual", evidence_scope="ACTUAL_S2_PREFLIGHT")
        if not native.get("accepted"):
            raise RuntimeError("ACTUAL_S2_NATIVE_FOUR_LAYER_FAILED")
    except BaseException as exc:
        failure = exc
        report["failure"] = f"{type(exc).__name__}:{exc}"
    finally:
        for role, worker in (("W1", w1), ("W0", w0)):
            if worker is not None and worker.outcome.start_request_issued and worker.cleanup_status != "PROVEN":
                try:
                    worker.abort()
                except BaseException as cleanup_exc:
                    report[f"{role.lower()}_cleanup_exception"] = f"{type(cleanup_exc).__name__}:{cleanup_exc}"
        if prospective_observer is not None and not prospective_observer.finalized:
            try:
                prospective_observer.note_gap(
                    "RUNTIME_PATH_ABORTED_BEFORE_NORMAL_OBSERVATION_END",
                    "unknown" if failure is None else f"{type(failure).__name__}:{failure}",
                )
                started = [worker for worker in (w0, w1) if worker is not None and worker.outcome.start_request_issued]
                if not started or all(worker.cleanup_status == "PROVEN" for worker in started):
                    prospective_observer.mark_owned_exit(
                        synthetic=False,
                        binding={
                            "status": "NO_PROCESS_STARTED" if not started else "ALL_STARTED_WORKERS_CLEANUP_PROVEN",
                            "instances": [worker.instance_id for worker in started],
                        },
                    )
                prospective_observation_evidence = prospective_observer.finalize()
                prospective_observation_review = review_observation_evidence(prospective_observation_evidence)
                if not (output / "PROSPECTIVE_OBSERVATION_REVIEW.json").exists():
                    write_json(output / "PROSPECTIVE_OBSERVATION_REVIEW.json", prospective_observation_review)
            except BaseException as observation_exc:
                report["prospective_observation_finalize_exception"] = f"{type(observation_exc).__name__}:{observation_exc}"
        if prospective_broker is not None:
            prospective_broker.close()
        canary_after = {
            "checkpoint_store_canary": _snapshot(output / "external_trusted" / "checkpoint_store" / "checkpoint_store_canary.bin"),
            "private_canary": _snapshot(output / "external_trusted" / "private" / "private_canary.bin"),
        }

    bundle = {
        "task_id": TASK_ID,
        "profile_id": PROFILE_ID,
        "profile_binding": PROFILE_BINDING,
        "evidence_scope": "ACTUAL_S2_PREFLIGHT",
        "attempt_id": args.attempt_id,
        "implementation_frozen_before_start": frozen,
        "chronology": chronology,
        "prestate": source,
        "inventory": inventory,
        "delta_plans": delta_plans,
        "delta_plan_hashes": delta_hashes,
        "s1_to_s2_delta": s1_delta,
        "w0": _worker_view(w0, w0_facts, w0_events),
        "checkpoint_disk": disk_receipt,
        "w1": _worker_view(w1, w1_facts, w1_events),
        "authority": authority,
        "public_signer_map": public_map,
        "gate": gate,
        "native_validation": native,
        "prospective_observation": prospective_observation_evidence,
        "prospective_observation_review": prospective_observation_review,
        "canary_snapshots": {
            name: {"before": canary_before.get(name), "after": canary_after.get(name)}
            for name in ("checkpoint_store_canary", "private_canary")
        },
        "producer_failure": None if failure is None else f"{type(failure).__name__}:{failure}",
    }
    write_json(output / "S2_EVIDENCE_BUNDLE.json", bundle)
    review = review_s2_evidence(bundle)
    write_json(output / "S2_REVIEW.json", review)
    state_carriage = {
        "w0_prestate_source_id": source.get("source_id"),
        "w0_prestate_source_hash": source.get("source_hash"),
        "checkpoint_disk_readback": disk_receipt,
        "w1_restore": w1_facts.get("restore"),
        "w1_full_checkpoint": w1_facts.get("checkpoint"),
        "inventory_issues": [item for item in review["issues"] if "INVENTORY" in item["code"] or "STATE" in item["code"] or "CHECKPOINT" in item["code"]],
        "status": "PASS" if not [item for item in review["issues"] if "INVENTORY" in item["code"] or "STATE" in item["code"] or "CHECKPOINT" in item["code"]] else "FAIL",
    }
    write_json(output / "STATE_CARRIAGE_CHECK.json", state_carriage)
    report.update({
        "status": review["verdict"],
        "independent_review": review,
        "w0_cleanup": "NOT_STARTED" if w0 is None or not w0.outcome.start_request_issued else w0.cleanup_status,
        "w1_cleanup": "NOT_STARTED" if w1 is None or not w1.outcome.start_request_issued else w1.cleanup_status,
        "checkpoint_disk_readback": "PASS" if disk_receipt and disk_receipt.get("write_b64") == disk_receipt.get("readback_b64") else "NOT_RUN_OR_FAIL",
        "observed_s2_effect_delta": review.get("observed_effect_delta"),
        "observed_s2_promotion_delta": review.get("observed_promotion_delta"),
        "native_validation": native.get("layer_status") if native else {},
        "s0": "NOT_RUN",
        "s1": "NOT_RUN",
        "full_selected_process_conformance": "NOT_RUN",
        "historical_d_exit": "UNPROVEN_NOT_REWRITTEN",
    })
    write_json(output / "S2_REPORT.json", report)
    for name, worker in (("w0", w0), ("w1", w1)):
        diagnostics = {} if worker is None else worker.diagnostics()
        write_json(output / f"{name}_diagnostics.json", diagnostics)
        stdout = "" if worker is None or worker.stdout is None else str(worker.stdout.snapshot().get("captured", ""))
        stderr = "" if worker is None or worker.stderr is None else str(worker.stderr.snapshot().get("captured", ""))
        (output / f"{name}_stdout.txt").write_text(stdout, encoding="utf-8", newline="\n")
        (output / f"{name}_stderr.txt").write_text(stderr, encoding="utf-8", newline="\n")
    print(json.dumps(report, sort_keys=True))
    return 0 if review["verdict"] == "PASS_SCOPED_S2" else 2


if __name__ == "__main__":
    raise SystemExit(main())
