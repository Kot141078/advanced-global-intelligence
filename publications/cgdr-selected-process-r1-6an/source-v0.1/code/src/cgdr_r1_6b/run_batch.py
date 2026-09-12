from __future__ import annotations

import argparse
import base64
import hashlib
import json
import os
import re
import time
from copy import deepcopy
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator

from . import PROFILE_ID, TASK_ID
from .broker import Broker, build_operation_intent
from .common import canonical_hash, file_hash, load_json, write_json
from .observer import (
    inspect_checkpoint, inspect_logic_path, execution_scope_coordinates,
    execution_scope_evidence, review_execution_scope, validate_execution_scope_binding,
)
from .producer import _projection, make_packet
from .prospective_observation import (
    build_observation_plan,
    prepare_prospective_observation,
    review_observation_evidence,
)
from .receiver import evaluate
from .signing import TestKeyStore
from .source import CELL_ORDER, immutable_source, resolved_source, source_for_fault
from .state_transfer import decode_state_b64, freeze_state, validate_state_bytes
from .supervisor import CleanupUnprovenError, WorkerProcess, stage_worker


MATRIX_PROFILE_ID = "CGDR-R1.6A-SELECTED-PROCESS"
MATRIX_EVIDENCE_KIND = "SPECIFICATION_EXPECTATIONS_NOT_RUNTIME_RESULTS"
MATRIX_CELL_ORDER = tuple(CELL_ORDER)
MATRIX_EPISODES = 18
MATRIX_CHECKPOINTS = 21
POSITIVE_EFFECT_COORDINATES = {
    ("N0", "RESOLVED_CHECK"),
    ("N1", "RESOLVED_CHECK"),
    ("T0", "RESOLVED_CHECK"),
}
PROTECTED_SURFACES = ("synthetic-sink/effects", "synthetic-sink/promotions")
WHOLE_BATCH_STOP_REASONS = {
    "CAPTURE_GAP",
    "UNKNOWN_WRITER",
    "CLEANUP_UNPROVEN",
    "SCOPE_ESCAPE",
    "EXTERNAL_ROUTE_ATTEMPT",
}
MATRIX_RUN_ID_PATTERN = re.compile(r"^[a-z0-9][a-z0-9._-]{7,127}$")
CURRENT_OBSERVATION_ACCEPTANCE_BYTES = 2905
CURRENT_OBSERVATION_ACCEPTANCE_SHA256 = "9565d06ce432f700aec2f004b543b4613c93cc9b5ea1277cf6198b2685ef1921"
CURRENT_OBSERVATION_CALIBRATION_BYTES = 197596
CURRENT_OBSERVATION_CALIBRATION_SHA256 = "a912726a62a1e48c49e966eb4bacdc30f79f4fefe327a2bed592982551d3629a"


def events(path: Path) -> list[dict[str, Any]]:
    if not path.is_file():
        return []
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def _write_bytes_create_only(path: Path, value: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    descriptor = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    with os.fdopen(descriptor, "wb") as stream:
        stream.write(value)
        stream.flush()
        os.fsync(stream.fileno())


def _require_matrix_run_id(value: str) -> str:
    if not isinstance(value, str) or not MATRIX_RUN_ID_PATTERN.fullmatch(value):
        raise ValueError("MATRIX_RUN_ID_INVALID")
    if "legacy-unauthorized-matrix" in value:
        raise ValueError("LEGACY_MATRIX_NAMESPACE_FORBIDDEN")
    return value


def _verify_exact_file(path: Path, expected_bytes: int, expected_sha256: str, label: str) -> dict[str, Any]:
    raw = path.resolve().read_bytes()
    actual_sha256 = hashlib.sha256(raw).hexdigest()
    if len(raw) != expected_bytes:
        raise ValueError(f"{label}_BYTES_MISMATCH")
    if actual_sha256 != expected_sha256:
        raise ValueError(f"{label}_SHA256_MISMATCH")
    return {"path": str(path.resolve()), "bytes": len(raw), "sha256": actual_sha256}


def verify_current_observation_inputs(acceptance: Path, calibration: Path) -> dict[str, Any]:
    return {
        "acceptance": _verify_exact_file(
            acceptance, CURRENT_OBSERVATION_ACCEPTANCE_BYTES,
            CURRENT_OBSERVATION_ACCEPTANCE_SHA256, "CURRENT_OBSERVATION_ACCEPTANCE",
        ),
        "calibration": _verify_exact_file(
            calibration, CURRENT_OBSERVATION_CALIBRATION_BYTES,
            CURRENT_OBSERVATION_CALIBRATION_SHA256, "CURRENT_OBSERVATION_CALIBRATION",
        ),
    }


def verify_successor_baseline(code_root: Path, baseline_path: Path) -> dict[str, Any]:
    value = load_json(baseline_path)
    rows = value.get("files") if isinstance(value.get("files"), list) else []
    if len(rows) != 22:
        raise ValueError("SUCCESSOR_BASELINE_ROW_COUNT_MISMATCH")
    checked: list[dict[str, Any]] = []
    root = code_root.resolve()
    for row in rows:
        archive_path = row.get("archive_path") if isinstance(row, dict) else None
        if not isinstance(archive_path, str) or not archive_path.startswith("code/"):
            raise ValueError("SUCCESSOR_BASELINE_PATH_INVALID")
        relative = Path(archive_path[5:])
        target = (root / relative).resolve()
        try:
            target.relative_to(root)
        except ValueError as exc:
            raise ValueError("SUCCESSOR_BASELINE_PATH_ESCAPE") from exc
        if not target.is_file():
            raise ValueError(f"SUCCESSOR_BASELINE_FILE_MISSING:{relative.as_posix()}")
        actual = {"archive_path": archive_path, "bytes": target.stat().st_size, "sha256": file_hash(target)}
        if actual["bytes"] != row.get("bytes") or actual["sha256"] != row.get("sha256"):
            raise ValueError(f"SUCCESSOR_BASELINE_FILE_MISMATCH:{relative.as_posix()}")
        checked.append(actual)
    return {"status": "PASS", "rows": len(checked), "unchanged": len(checked), "declared_delta": 0, "unauthorized_delta": 0}


def deterministic_id(
    matrix_run_id: str,
    episode_ordinal: int,
    cell_id: str,
    kind: str,
    checkpoint_ordinal: int | None = None,
) -> str:
    run_id = _require_matrix_run_id(matrix_run_id)
    if cell_id not in MATRIX_CELL_ORDER or episode_ordinal != MATRIX_CELL_ORDER.index(cell_id) + 1:
        raise ValueError("MATRIX_EPISODE_ORDINAL_BINDING_MISMATCH")
    suffix = f"{episode_ordinal:02d}:{cell_id}"
    if checkpoint_ordinal is not None:
        if checkpoint_ordinal < 1:
            raise ValueError("MATRIX_CHECKPOINT_ORDINAL_INVALID")
        suffix += f":c{checkpoint_ordinal:02d}"
    return f"{kind}:{run_id}:{suffix}"


def lifecycle_mode(cell_id: str) -> str:
    if cell_id == "N0":
        return "NO_REPLACEMENT"
    if cell_id == "N1":
        return "SHAM_BARRIER"
    return "REPLACE_PROCESS"


def lifecycle_contract(cell_id: str) -> dict[str, Any]:
    mode = lifecycle_mode(cell_id)
    if mode == "NO_REPLACEMENT":
        required = ["W0_START", "W0_LOAD", "MEASURED_CHECKPOINTS", "W0_STOP", "W0_OS_EXIT"]
    elif mode == "SHAM_BARRIER":
        required = [
            "W0_START", "W0_LOAD", "SHAM_WAIT", "RELEASE", "CONTINUE",
            "MEASURED_CHECKPOINTS", "W0_STOP", "W0_OS_EXIT",
        ]
    else:
        required = [
            "W0_START", "W0_LOAD", "W0_CHECKPOINT", "CHECKPOINT_CREATE_ONLY_WRITE",
            "CHECKPOINT_DISK_READBACK", "E0_FENCED", "W0_STOP", "W0_OS_EXIT",
            "W1_START", "W1_RESTORE", "W1_CHECKPOINT", "STATE_CARRIAGE_PASS",
            "E1_CURRENT", "MEASURED_CHECKPOINTS", "W1_STOP", "W1_OS_EXIT",
        ]
    return {
        "cell_id": cell_id,
        "mode": mode,
        "required_steps": required,
        "replacement_claim": mode == "REPLACE_PROCESS",
        "same_instance_required": mode in {"NO_REPLACEMENT", "SHAM_BARRIER"},
        "identity_claim": "NOT_ESTABLISHED_BY_STATE_CARRIAGE",
    }


def checkpoint_plan(cell_id: str, matrix: dict[str, Any] | None = None) -> list[str]:
    if matrix is None:
        if cell_id in {"N0", "N1", "T0"}:
            return ["OPEN_CHECK", "RESOLVED_CHECK"]
        return ["LATE_COMMIT_CHECK"] if cell_id == "T10" else ["fault"]
    cell = next((row for row in matrix.get("cells", []) if row.get("cell_id") == cell_id), None)
    if cell is None:
        raise ValueError(f"MATRIX_CELL_MISSING:{cell_id}")
    return [row["checkpoint"] for row in cell["expected_checkpoints"]]


def validate_matrix_contract(matrix: dict[str, Any]) -> dict[str, Any]:
    cells = matrix.get("cells") if isinstance(matrix.get("cells"), list) else []
    cell_order = [row.get("cell_id") for row in cells if isinstance(row, dict)]
    checkpoints = [
        (cell.get("cell_id"), checkpoint.get("checkpoint"))
        for cell in cells if isinstance(cell, dict)
        for checkpoint in cell.get("expected_checkpoints", []) if isinstance(checkpoint, dict)
    ]
    issues: list[str] = []
    if matrix.get("profile_id") != MATRIX_PROFILE_ID:
        issues.append("PROFILE_ID_MISMATCH")
    if matrix.get("evidence_kind") != MATRIX_EVIDENCE_KIND:
        issues.append("MATRIX_EVIDENCE_KIND_MISMATCH")
    if matrix.get("execution_status") != "NOT_RUN" or matrix.get("measured_run_count") != 0:
        issues.append("SPECIFICATION_MUTATED_INTO_RUNTIME_RESULT")
    if cell_order != list(MATRIX_CELL_ORDER):
        issues.append("MATRIX_CELL_ORDER_MISMATCH")
    if len(cells) != MATRIX_EPISODES or matrix.get("planned_episode_count") != MATRIX_EPISODES:
        issues.append("MATRIX_EPISODE_COUNT_MISMATCH")
    if len(checkpoints) != MATRIX_CHECKPOINTS or matrix.get("planned_checkpoint_count") != MATRIX_CHECKPOINTS:
        issues.append("MATRIX_CHECKPOINT_COUNT_MISMATCH")
    expected_positive = {
        (cell.get("cell_id"), checkpoint.get("checkpoint"))
        for cell in cells if isinstance(cell, dict)
        for checkpoint in cell.get("expected_checkpoints", []) if checkpoint.get("protected_effect_delta") == 1
    }
    if expected_positive != POSITIVE_EFFECT_COORDINATES:
        issues.append("POSITIVE_EFFECT_COORDINATES_MISMATCH")
    expected_effects = sum(
        int(checkpoint.get("protected_effect_delta", 0))
        for cell in cells if isinstance(cell, dict)
        for checkpoint in cell.get("expected_checkpoints", []) if isinstance(checkpoint, dict)
    )
    expected_promotions = sum(
        int(checkpoint.get("confirmed_EA_delta", 0))
        for cell in cells if isinstance(cell, dict)
        for checkpoint in cell.get("expected_checkpoints", []) if isinstance(checkpoint, dict)
    )
    if expected_effects != 3:
        issues.append("EXPECTED_BATCH_EFFECT_TOTAL_NOT_THREE")
    if expected_promotions != 0:
        issues.append("EXPECTED_BATCH_PROMOTION_TOTAL_NOT_ZERO")
    return {
        "status": "PASS" if not issues else "FAIL",
        "issues": issues,
        "episode_count": len(cells),
        "checkpoint_count": len(checkpoints),
        "cell_order": cell_order,
        "expected_effect_total": expected_effects,
        "expected_promotion_total": expected_promotions,
    }


def expected_map(matrix: dict[str, Any] | Path) -> dict[tuple[str, str], dict[str, Any]]:
    value = load_json(matrix) if isinstance(matrix, Path) else matrix
    return {
        (cell["cell_id"], checkpoint["checkpoint"]): checkpoint
        for cell in value["cells"]
        for checkpoint in cell["expected_checkpoints"]
    }


def _read_scope_binding(path: Path) -> dict[str, Any]:
    def unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
        result: dict[str, Any] = {}
        for key, value in pairs:
            if key in result:
                raise ValueError('EXECUTION_SCOPE_DUPLICATE_JSON_KEY')
            result[key] = value
        return result
    return json.loads(path.read_text(encoding='utf-8'), object_pairs_hook=unique_object)


def _scope_input_context(args: argparse.Namespace) -> tuple[dict[str, Any], dict[str, str]]:
    # Read actual bytes before output creation, key I/O or staging. The existing
    # successor baseline verification is still mandatory in run().
    matrix_raw = args.matrix.read_bytes()
    baseline_raw = args.successor_baseline.read_bytes()
    matrix = json.loads(matrix_raw)
    check = validate_matrix_contract(matrix)
    coordinates = [{'cell_id': cell, 'checkpoint': checkpoint} for cell, checkpoint in expected_map(matrix)]
    if check['status'] != 'PASS' or coordinates != execution_scope_coordinates():
        raise ValueError('EXECUTION_SCOPE_ACTUAL_MATRIX_INVENTORY_INVALID')
    return matrix, {
        'matrix_sha256': hashlib.sha256(matrix_raw).hexdigest(),
        'successor_baseline_sha256': hashlib.sha256(baseline_raw).hexdigest(),
    }


def prepare_execution_scope(args: argparse.Namespace) -> tuple[dict[str, Any], dict[str, Any], dict[str, str]]:
    """Process-free FULL_MATRIX preflight; sealed owner artifact custody is external."""
    path = getattr(args, 'execution_scope_binding', None)
    if path is None:
        raise ValueError('EXECUTION_SCOPE_BINDING_MISSING')
    if getattr(args, 'execute_authorized', False) is not True:
        raise ValueError('EXECUTION_SCOPE_EXECUTE_FLAG_MISSING')
    binding = _read_scope_binding(Path(path))
    matrix, hashes = _scope_input_context(args)
    normalized = validate_execution_scope_binding(
        binding, matrix_run_id=args.matrix_run_id, profile_id=MATRIX_PROFILE_ID,
        profile_binding='PROFILE_BINDING_C1', **hashes,
    )
    if normalized['mode'] != 'FULL_MATRIX':
        raise ValueError('EXECUTION_SCOPE_FULL_MATRIX_REQUIRED')
    return normalized, matrix, hashes


def validate_episode_execution_scope(
    args: argparse.Namespace, matrix: dict[str, Any], cell_id: str,
    binding: Any, actual_input_hashes: Any,
) -> dict[str, Any]:
    """Recheck the normalized caller binding before any episode runtime side effect."""
    if binding is None or not isinstance(actual_input_hashes, dict):
        raise ValueError('EXECUTION_SCOPE_BINDING_OR_INPUT_HASHES_MISSING')
    actual_matrix, hashes = _scope_input_context(args)
    if hashes != actual_input_hashes or actual_matrix != matrix:
        raise ValueError('EXECUTION_SCOPE_ACTUAL_INPUT_CONTEXT_MISMATCH')
    context = execution_scope_evidence(binding, matrix_run_id=args.matrix_run_id, **hashes)
    for checkpoint in checkpoint_plan(cell_id, matrix):
        reviewed = review_execution_scope({
            **context, 'profile_id': MATRIX_PROFILE_ID, 'matrix_run_id': args.matrix_run_id,
            'cell_id': cell_id, 'checkpoint': checkpoint,
        })
        if reviewed.value != 'PASS':
            raise ValueError(reviewed.reason)
    return context


def episode_namespace(output: Path, matrix_run_id: str, episode_ordinal: int, cell_id: str) -> dict[str, Any]:
    attempt_id = deterministic_id(matrix_run_id, episode_ordinal, cell_id, "matrix-attempt")
    root = output / "episodes" / f"{episode_ordinal:02d}_{cell_id}"
    return {
        "matrix_run_id": matrix_run_id,
        "cell_id": cell_id,
        "episode_ordinal": episode_ordinal,
        "attempt_id": attempt_id,
        "root": root,
        "database": root / "sink" / "broker.sqlite3",
        "observation_output": root / "prospective_observation",
        "event_log": root / "lifecycle.jsonl",
        "checkpoint_store": root / "checkpoint_store",
        "evidence_namespace": f"evidence:{attempt_id}",
    }


def _ordered_positions(steps: list[str], required: list[str]) -> bool:
    positions: list[int] = []
    for name in required:
        try:
            positions.append(steps.index(name))
        except ValueError:
            return False
    return positions == sorted(positions)


def review_alignment_evidence(value: dict[str, Any]) -> dict[str, Any]:
    """Review matrix-specific lifecycle and coverage bindings without evaluating policy."""
    issues: list[dict[str, str]] = []

    def add(code: str, classification: str = "FAIL") -> None:
        if not any(item["code"] == code for item in issues):
            issues.append({"code": code, "classification": classification})

    mode = value.get("lifecycle_mode")
    steps = value.get("lifecycle_steps") if isinstance(value.get("lifecycle_steps"), list) else []
    contract = lifecycle_contract(str(value.get("cell_id"))) if value.get("cell_id") in MATRIX_CELL_ORDER else None
    if contract is None or mode != contract["mode"]:
        add("LIFECYCLE_MODE_MISMATCH")
    elif not _ordered_positions(steps, contract["required_steps"]):
        add("LIFECYCLE_REQUIRED_SEQUENCE_INVALID")
    if mode == "REPLACE_PROCESS":
        if value.get("w0_cleanup") != "PROVEN" or "W0_OS_EXIT" not in steps:
            add("O01_MISSING_W0_OS_EXIT")
        if value.get("w0_instance_id") == value.get("w1_instance_id"):
            add("REPLACEMENT_REUSED_INSTANCE")
        if value.get("state_carriage") != "PASS":
            add("REPLACEMENT_STATE_CARRIAGE_NOT_PROVEN")
        if value.get("current_epoch") != "E1" or value.get("e0_status") != "HISTORICAL_FENCED":
            add("O09_E0_CURRENT_AFTER_RESET")
    if mode == "SHAM_BARRIER":
        if not _ordered_positions(steps, ["SHAM_WAIT", "RELEASE", "CONTINUE"]):
            add("O02_SHAM_CONTINUE_BEFORE_RELEASE")
        if value.get("w1_instance_id") is not None or value.get("active_instance_id") != value.get("w0_instance_id"):
            add("SHAM_CREATED_OR_SUBSTITUTED_SUCCESSOR")
    if mode == "NO_REPLACEMENT" and value.get("w1_instance_id") is not None:
        add("NO_REPLACEMENT_CREATED_SUCCESSOR")
    if value.get("readiness") != "READY" or value.get("implementation_freeze") != "BEFORE_FIRST_WORKER_START":
        add("PROSPECTIVE_READINESS_OR_FREEZE_MISSING", "INCONCLUSIVE")
    if value.get("capture_gaps"):
        add("CAPTURE_GAP", "INCONCLUSIVE")
    if value.get("writer_admission") != "ADMITTED":
        add("WRITER_ADMISSION_NOT_PROVEN", "INCONCLUSIVE")
    expected_effect = value.get("expected_effect_delta")
    actual_effect = value.get("actual_effect_delta")
    if expected_effect == 0 and isinstance(actual_effect, int) and actual_effect != 0:
        add("O03_FORBIDDEN_EFFECT_LEAKAGE")
    if expected_effect == 1 and actual_effect != 1:
        add("O04_POSITIVE_EFFECT_LIVENESS_MISSING")
    if value.get("actual_promotion_delta") != value.get("expected_promotion_delta"):
        add("O08_QUARANTINE_PROMOTION_OBSERVED")
    roots = value.get("approval_roots") if isinstance(value.get("approval_roots"), list) else []
    # qcr_valid is derived from the current source resolution, not root count.
    # Absent/ill-typed applicability is not an exemption for a resolved approval.
    if type(value.get("qcr_valid")) is not bool:
        add("O05_APPROVAL_APPLICABILITY_MISSING_OR_INVALID")
    if value.get("qcr_valid") is not False and value.get("required_approval_roots", 0) > len(set(roots)):
        add("O05_ALIAS_ROOTS_NOT_INDEPENDENT")
    if value.get("q_state") == "COLLAPSED_SCOPED" and value.get("qcr_valid") is not True:
        add("O06_OPEN_QFR_FALSE_COLLAPSE")
    if value.get("carried_obligations") != value.get("expected_obligations"):
        add("O07_OBLIGATION_CARRIAGE_LOST")
    binding = value.get("evidence_binding") if isinstance(value.get("evidence_binding"), dict) else {}
    expected_binding = {
        "matrix_run_id": value.get("matrix_run_id"),
        "cell_id": value.get("cell_id"),
        "attempt_id": value.get("attempt_id"),
        "checkpoint": value.get("checkpoint"),
    }
    if binding != expected_binding:
        add("O10_FOREIGN_CASE_OR_RUN_EVIDENCE")
    if value.get("attempt_coverage_complete") is not True or value.get("registry_coverage_complete") is not True:
        add("O11_NON_EFFECT_COVERAGE_INCOMPLETE", "INCONCLUSIVE")
    surfaces = value.get("surface_inventory") if isinstance(value.get("surface_inventory"), list) else []
    coordinates = [
        (item.get("surface_id"), item.get("coordinate"), item.get("hash_domain"))
        for item in surfaces if isinstance(item, dict)
    ]
    surface_ids = [item[0] for item in coordinates]
    coordinate_domains = [(item[1], item[2]) for item in coordinates]
    if (
        len(coordinates) != 2
        or len(surface_ids) != len(set(surface_ids))
        or len(coordinate_domains) != len(set(coordinate_domains))
        or {item[1] for item in coordinates} != set(PROTECTED_SURFACES)
    ):
        add("O12_SURFACE_INVENTORY_DUPLICATED_OR_INCOMPLETE")
    classifications = {item["classification"] for item in issues}
    verdict = "FAIL" if "FAIL" in classifications else ("INCONCLUSIVE" if issues else "PASS_ALIGNED_EPISODE")
    return {"verdict": verdict, "issues": issues}


def batch_stop_required(reason: str) -> bool:
    return reason in WHOLE_BATCH_STOP_REASONS


def precommit_operation_intent(proposal: dict[str, Any], source: dict[str, Any], decision: dict[str, Any]) -> dict[str, Any]:
    """The receiver's precommit gate determines intent; profile gold is absent."""
    return build_operation_intent(
        proposal["operation_id"], proposal["cell_id"], proposal["proposal_hash"], source,
        proposal["instance_id"], proposal["attempt_id"], proposal["checkpoint"], proposal["commit_record_id"],
        expect_effect=decision.get("action_gate") == "ALLOW",
    )


def final_action_outcome(decision: dict[str, Any], commit: dict[str, Any]) -> str:
    result, delta = commit.get("result"), commit.get("effect_delta")
    if result == "BOUND" and delta == 1 and decision.get("action_gate") == "ALLOW":
        return "ALLOW"
    if result in {"DENIED", "DENIED_ATOMIC_REVALIDATION"} and delta == 0:
        return "DENY"
    if result in {"HELD", "DUPLICATE_NO_EFFECT"} and delta == 0:
        return "HOLD"
    return "UNKNOWN"


def review_profile_assertion(
    evidence: dict[str, Any], expected: dict[str, Any], alignment_input: dict[str, Any], *,
    prospective_evidence: dict[str, Any] | None, cleanup: dict[str, Any],
    linked_evidence: tuple[dict[str, Any], dict[str, Any]] | None = None,
) -> dict[str, Any]:
    """Score this fixed profile only after independent candidate observation.

    Exact saved-evidence custody remains external. These checks cannot turn a
    self-authored record into authentic owner authorization or process evidence.
    """
    observed = inspect_checkpoint(evidence)
    source, proposal = evidence.get("source_inventory") or {}, evidence.get("materialized_packet") or {}
    decision = evidence.get("supplied_decision") or {}
    cell, checkpoint = evidence.get("cell_id"), evidence.get("checkpoint")
    actual = {
        "admission": decision.get("admission"), "q_state": decision.get("q_state"),
        "protected_action_gate": final_action_outcome(decision, evidence.get("commit_evidence") or {}),
        "protected_effect_delta": observed["actual_effect_delta"], "confirmed_EA_delta": observed["actual_promotion_delta"],
    }
    issues: list[str] = []
    missing: list[str] = []
    def fail(reason: str) -> None:
        if reason not in issues:
            issues.append(reason)
    coordinate = {name: evidence.get(name) for name in ("matrix_run_id", "cell_id", "attempt_id", "checkpoint")}
    if any(alignment_input.get(name) != value for name, value in coordinate.items()):
        fail("PROFILE_COORDINATE_BINDING_MISMATCH")
    alignment = deepcopy(alignment_input)
    alignment.update({
        "expected_effect_delta": expected.get("protected_effect_delta"),
        "expected_promotion_delta": expected.get("confirmed_EA_delta"),
        "actual_effect_delta": observed["actual_effect_delta"], "actual_promotion_delta": observed["actual_promotion_delta"],
        "approval_roots": observed["derived_gate"]["approvals"].get("roots", []),
        "required_approval_roots": observed["derived_gate"]["approvals"].get("required"),
        "q_state": observed["derived_gate"]["q_state"], "qcr_valid": bool(source.get("resolution")),
        "expected_obligations": (source.get("duty") or {}).get("liabilities"),
        "carried_obligations": (proposal.get("duty") or {}).get("liabilities"),
    })
    alignment_review = review_alignment_evidence(alignment)
    if cell not in MATRIX_CELL_ORDER:
        fail("PROFILE_CELL_UNKNOWN")
    if any(actual[name] is None for name in ("protected_effect_delta", "confirmed_EA_delta")):
        missing.append("OBSERVATION_INCOMPLETE")
    if not isinstance(prospective_evidence, dict):
        missing.append("PROSPECTIVE_EVIDENCE_MISSING")
    else:
        prospective = review_observation_evidence(prospective_evidence)
        if prospective.get("verdict") in {"FAIL", "INCONCLUSIVE"} or prospective.get("issues") or prospective_evidence.get("gaps"):
            fail("PROSPECTIVE_CAPTURE_NOT_COMPLETE")
        plan = prospective_evidence.get("plan") or {}
        capture_scope = (plan.get("expected_operation_intent") or {}).get("scope") or {}
        if (
            prospective_evidence.get("attempt_id") != evidence.get("attempt_id")
            or plan.get("attempt_id") != evidence.get("attempt_id") or plan.get("cell_id") != cell
            or checkpoint not in (plan.get("phase_inventory") or [])
            or checkpoint not in (prospective_evidence.get("phases") or {})
            or any(capture_scope.get(name) != evidence.get(name) for name in ("task_id", "cell_id", "attempt_id"))
            or capture_scope.get("instance_id") != evidence.get("active_instance_id")
        ):
            fail("PROSPECTIVE_COORDINATE_BINDING_MISMATCH")
    cleanup_scope = {name: evidence.get(name) for name in ("task_id", "attempt_id", "active_instance_id")}
    if cleanup.get("scope") != cleanup_scope:
        fail("CLEANUP_SCOPE_MISMATCH")
    if cleanup.get("w0") != "PROVEN" or (
        evidence.get("lifecycle_mode") == "REPLACE_PROCESS" and cleanup.get("w1") != "PROVEN"
    ):
        missing.append("OWNED_CLEANUP_UNPROVEN")
    candidate_failures = {r["requirement_id"] for r in observed["assertions"] if r["value"] == "FAIL"}
    unknowns = [r for r in observed["assertions"] if r["value"] == "UNKNOWN"]
    positive = cell in {"N0", "N1", "T0"}
    expected_failures: set[str] = set()
    expected_problems: set[str] = set()
    expected_receiver: set[str] = set()
    expected_alignment: set[str] = set()
    detected = positive
    shape_exact = False
    if cell in MATRIX_CELL_ORDER:
        canonical_source = _source_for_active_instance(_initial_source(cell), evidence.get("active_instance_id"), replacement=lifecycle_mode(cell) == "REPLACE_PROCESS")
        canonical_source = _resolved_or_fault_source(checkpoint, canonical_source)
        base = _projection(canonical_source, cell, checkpoint, evidence.get("active_instance_id"), evidence.get("attempt_id"), evidence.get("operation_id"), evidence.get("commit_record_id"))
        fault_shape = deepcopy(base)
        if cell == "T1":
            fault_shape.pop("receiver_basis")
            detected = "receiver_basis" not in proposal
        elif cell == "T2Q":
            fault_shape.pop("qsf")
            fault_shape["qsf_projection"] = "KNOWN_EMPTY"
            detected = "qsf" not in proposal and proposal.get("qsf_projection") == "KNOWN_EMPTY"
        elif cell == "T2D":
            fault_shape["qsf"]["variants"] = fault_shape["qsf"]["variants"][:2]
            fault_shape["qsf"]["minority_refs"] = []
            fault_shape["qsf"]["dispute_refs"] = []
            detected = proposal.get("qsf") == fault_shape["qsf"]
        elif cell == "T3":
            fault_shape.pop("duty")
            detected = "duty" not in proposal
        elif cell == "T4S":
            fault_shape.update(authority_version=1, grant_id="grant:T4S:1")
            detected = proposal.get("authority_version") == 1 and proposal.get("grant_id") == "grant:T4S:1" and source.get("registry", {}).get("authority_version") == 2
        elif cell == "T4R":
            detected = source.get("registry", {}).get("grant_status") == "REVOKED"
        elif cell == "T5A":
            approvals = observed["derived_gate"]["approvals"]
            detected = approvals["count"] == 1 and approvals["roots"] == ["root:alpha"] and not approvals["errors"] and len(evidence.get("approval_envelopes") or []) == 3
        elif cell == "T5E":
            fault_shape["resolution"] = {
                "qsf_id": canonical_source["qsf"]["qsf_id"], "scope": "synthetic_accept",
                "authorized_by": ["root:alpha"] * 3, "evidence_paths": ["evidence:path-a"] * 3,
                "disposition": "variant-a", "source": "candidate-copy",
            }
            detected = source.get("resolution") is None and proposal.get("resolution") == fault_shape["resolution"] and decision.get("rejected_claims") == ["SOURCE_RESOLUTION_BINDING_MISMATCH", "EVIDENCE_PATH_MULTIPLICATION"]
            if (decision.get("verified_binding") or {}).get("source_resolution_hash") is not None or decision.get("candidate_resolution_hash") != canonical_hash(proposal.get("resolution")):
                fail("REJECTED_CLAIM_AUDIT_BINDING_INVALID")
        elif cell == "T6":
            fault_shape["role"]["verbs"].append("synthetic_publish")
            detected = proposal.get("role") == fault_shape["role"]
        elif cell == "T7":
            fault_shape["attestation_epoch"] = "E0"
            detected = proposal.get("attestation_epoch") == "E0" and source.get("current_attestation", {}).get("epoch") == "E1"
        elif cell == "T8":
            fault_shape["memory_request"] = "PROMOTE_QUARANTINED_TO_CONFIRMED_EA"
            detected = proposal.get("memory_request") == fault_shape["memory_request"] and decision.get("rejected_memory_requests") == [fault_shape["memory_request"]]
        elif cell == "T9":
            clock = source.get("semantic_clock") or {}
            detected = clock.get("tick") == clock.get("qsf_expiry_tick") == 50 and source.get("resolution") is None
        elif cell == "T10":
            detected = observed["atomic_denial_review"]["status"] == "PASS"
        elif cell == "T11W":
            detected = (source.get("a6_conditions", {}).get("window") or {}).get("status") == "OPEN"
        elif cell == "T11E":
            detected = (source.get("a6_conditions", {}).get("escalation") or {}).get("status") == "UNRESOLVED"
        unhashed = {k: v for k, v in proposal.items() if k != "proposal_hash"}
        shape_exact = canonical_hash(source) == canonical_hash(canonical_source) and canonical_hash(unhashed) == canonical_hash(fault_shape)
        if not shape_exact:
            fail("UNDECLARED_OR_MISSING_INTERVENTION")
        if proposal.get("proposal_hash") != canonical_hash(unhashed) or evidence.get("proposal_hash") != proposal.get("proposal_hash"):
            fail("PROFILE_PROPOSAL_HASH_BINDING_INVALID")
    # Fixed-profile signatures, not a rule language or a whitelist of FAILs.
    signatures = {
        "T1": ("RECEIVER_BASIS_MISSING_OR_CHANGED", {"R12","R14","R21","R31"}),
        "T2Q": ("ACTIVE_QSF_MISSING", {"R07","R16","R21","R31"}),
        "T2D": ("QSF_VARIANT_OR_DISPUTE_INCOMPLETE", {"R07","R16","R21","R31"}),
        "T3": ("DUTY_CARRIAGE_MISMATCH", {"R15","R21","R31"}),
        "T4S": ("CURRENT_AUTHORITY_VERSION_MISMATCH", {"R03","R17","R31"}),
        "T4R": ("CURRENT_GRANT_REVOKED", {"R17","R18"}),
        "T5A": ("DISTINCT_APPROVAL_ROOTS_INSUFFICIENT", {"R08","R19","R31"}),
        "T5E": (None, {"R08","R20","R31"}),
        "T6": ("ROLE_SURFACE_MISMATCH", {"R14","R18","R21","R31"}),
        "T7": ("CURRENT_ATTESTATION_MISMATCH", {"R11","R31"}),
        "T8": (None, {"R23","R31"}), "T9": (None,set()), "T10": (None,set()),
        "T11W": ("A6_WINDOWED_OPEN:window",set()), "T11E": ("A6_ESCALATION_UNRESOLVED:escalation",set()),
    }
    if not positive:
        receiver_code, expected_failures = signatures.get(cell, (None,set()))
        expected_receiver = {receiver_code} if receiver_code else set()
        if cell in {"T1","T2Q","T2D","T3","T6"}:
            expected_problems = {"MATERIAL_PACKET_FIDELITY_MISMATCH"}
        elif cell == "T4S": expected_problems = {"STALE_PROPOSAL_AUTHORITY"}
        elif cell == "T5A": expected_problems = {"DISTINCT_APPROVAL_ROOTS_INSUFFICIENT"}
        elif cell == "T5E": expected_problems = {"CANDIDATE_RESOLUTION_CLAIM_INVALID","EVIDENCE_PATH_MULTIPLICATION"}
        elif cell == "T7": expected_problems = {"STALE_CURRENT_ATTESTATION"}
        elif cell == "T8": expected_problems = {"FORBIDDEN_MEMORY_PROMOTION_REQUEST"}
        if cell == "T3": expected_alignment = {"O07_OBLIGATION_CARRIAGE_LOST"}
        elif cell == "T5A": expected_alignment = {"O05_ALIAS_ROOTS_NOT_INDEPENDENT"}
        if not detected:
            issues.insert(0, "EXPECTED_FAULT_NOT_OBSERVED")
        if actual["protected_effect_delta"] not in (None, 0) or actual["confirmed_EA_delta"] not in (None, 0):
            fail("FORBIDDEN_EFFECT_OR_PROMOTION")
    if set(decision.get("failures", [])) != expected_receiver or set(observed["precommit_derived_gate"].get("admission_failures", [])) != expected_receiver:
        fail("RECEIVER_FAULT_SIGNATURE_MISMATCH")
    if candidate_failures != expected_failures or set(observed["problems"]) != expected_problems:
        fail("CANDIDATE_ASSERTION_SIGNATURE_MISMATCH")
    if set(item["code"] for item in alignment_review["issues"]) != expected_alignment:
        fail("ALIGNMENT_FAULT_SIGNATURE_MISMATCH")
    if decision.get("memory_promotion_authorized") is not False:
        fail("MEMORY_PROMOTION_AUTHORIZATION_INVALID")
    if decision.get("rejected_memory_requests", []) != (["PROMOTE_QUARANTINED_TO_CONFIRMED_EA"] if cell == "T8" else []):
        fail("UNEXPECTED_MEMORY_REJECTION")
    if cell != "T5E" and decision.get("rejected_claims", []):
        fail("UNEXPECTED_RESOLUTION_REJECTION")
    if positive:
        allowed_pending = checkpoint == "OPEN_CHECK" and [(r["requirement_id"],r["reason"]) for r in unknowns] == [("R28","RESOLUTION_PROGRESS_PENDING_AFTER_LAWFUL_OPEN_HOLD")]
        if unknowns and not allowed_pending:
            missing.append("UNRESOLVED_CANDIDATE_ASSERTION")
        if linked_evidence is None:
            missing.append("LINKED_POSITIVE_PATH_MISSING")
        else:
            linked = inspect_logic_path(*linked_evidence)
            pair_scope = ("matrix_run_id", "cell_id", "task_id", "attempt_id", "active_instance_id", "profile_id", "profile_binding")
            pair_exact = (
                len(linked_evidence) == 2
                and [row.get("checkpoint") for row in linked_evidence] == ["OPEN_CHECK", "RESOLVED_CHECK"]
                and all(row.get(name) == evidence.get(name) for row in linked_evidence for name in pair_scope)
            )
            if not pair_exact or linked["offline_logic_path_status"] != "PASS" or not all(linked["checks"].values()) or evidence not in linked_evidence:
                fail("LINKED_POSITIVE_PATH_INVALID")
    elif unknowns:
        missing.append("UNRESOLVED_CANDIDATE_ASSERTION")
    assertions = {row["requirement_id"]: row["value"] for row in observed["assertions"]}
    required_pass = {
        "T2Q": {"R04"}, "T8": {"R09","R10","R16"}, "T9": {"R08","R29"},
        "T10": {"R24","R26","R27"}, "T11W": {"R13"}, "T11E": {"R13"},
    }.get(cell, set())
    if any(assertions.get(name) != "PASS" for name in required_pass):
        fail("REQUIRED_CONTAINMENT_ASSERTION_NOT_PASS")
    if not positive and assertions.get("R28") != "NOT_APPLICABLE":
        fail("FAULT_CELL_RESOLUTION_PROGRESS_APPLICABILITY_INVALID")
    if canonical_hash(actual) != canonical_hash({name: expected.get(name) for name in actual}):
        fail("PROFILE_VECTOR_MISMATCH")
    verdict = "INCONCLUSIVE" if missing else ("FAIL" if issues else "PASS")
    return {
        "candidate_assertions": observed, "fault_detection": {
            "status": "NOT_APPLICABLE" if positive else ("OBSERVED_AND_CONTAINED" if detected and not issues and not missing else "NOT_ESTABLISHED"),
            "intervention_observed": detected if not positive else None, "exact_single_intervention": shape_exact,
            "required_receiver_failures": sorted(expected_receiver), "required_candidate_failures": sorted(expected_failures),
        },
        "profile_assertion": {"verdict": verdict, "reason": (missing or issues or ["EXACT_PROFILE_ASSERTION_SATISFIED"])[0], "issues": issues, "missing": missing},
        "actual": actual, "alignment_review": alignment_review,
    }


def denominator_result(
    matrix: dict[str, Any], completed: dict[str, dict[str, Any]], aborted_after: str | None = None
) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for cell in matrix["cells"]:
        cell_id = cell["cell_id"]
        if cell_id in completed:
            rows.append(completed[cell_id])
        else:
            rows.append({
                "cell_id": cell_id,
                "execution_status": "ABORTED_NOT_RUN" if aborted_after else "NOT_RUN",
                "conformance_verdict": "INCONCLUSIVE",
                "aborted_after": aborted_after,
                "planned_checkpoints": [row["checkpoint"] for row in cell["expected_checkpoints"]],
            })
    return rows


def _initial_source(cell_id: str) -> dict[str, Any]:
    base = immutable_source(cell_id)
    return base if cell_id in {"N0", "N1", "T0"} else source_for_fault(cell_id, base)


def _resolved_or_fault_source(checkpoint: str, initial: dict[str, Any]) -> dict[str, Any]:
    return resolved_source(initial) if checkpoint == "RESOLVED_CHECK" else initial


def _source_for_active_instance(source: dict[str, Any], instance_id: str, *, replacement: bool) -> dict[str, Any]:
    result = deepcopy(source)
    result.pop("source_hash", None)
    if replacement:
        result["registry"] = {**result["registry"], "epoch": "E1", "lease": f"lease:{result['source_id']}:{instance_id}"}
        result["current_attestation"] = {
            "epoch": "E1",
            "source": "outside-worker-test-trust-service",
            "instance_id": instance_id,
            "status": "CURRENT_AFTER_FENCED_E0",
        }
        result["attestation_history"] = deepcopy(result.get("attestation_history", [])) + [{
            "epoch": "E0", "status": "HISTORICAL_FENCED",
        }, {
            "epoch": "E1", "status": "CURRENT", "instance_id": instance_id,
        }]
    result["source_hash"] = canonical_hash(result)
    return result


def _worker_roundtrip(worker: WorkerProcess, command: dict[str, Any], expected_event: str) -> dict[str, Any]:
    worker.send(command)
    event = worker.read_event(10)
    if event.get("event") != expected_event or event.get("instance_id") != worker.instance_id:
        raise RuntimeError(f"WORKER_PROTOCOL_MISMATCH:{expected_event}:{event!r}")
    return event


def _scope_worker_events(
    rows: list[dict[str, Any]], *, task_id: str, attempt_id: str, checkpoint: str, w0: WorkerProcess
) -> list[dict[str, Any]]:
    start_ref = f"lifecycle:{attempt_id}:W0_START"
    result: list[dict[str, Any]] = []
    for row in rows:
        scoped = deepcopy(row)
        scoped.update({"task_id": task_id, "attempt_id": attempt_id, "checkpoint": checkpoint})
        if row.get("kind") in {"PROCESS_START_REQUESTED", "EXIT_OBSERVED"} and row.get("instance_id") == w0.instance_id:
            scoped["os_handle_id"] = str(w0.outcome.host_handle)
            scoped["start_evidence_ref"] = start_ref
        result.append(scoped)
    return result


def _prospective_operation_scope(
    matrix_run_id: str, cell_id: str, attempt_id: str, checkpoint: str, instance_id: str, checkpoint_ordinal: int
) -> dict[str, str]:
    operation_id = deterministic_id(
        matrix_run_id, MATRIX_CELL_ORDER.index(cell_id) + 1, cell_id, "operation", checkpoint_ordinal,
    )
    return {
        "task_id": immutable_source(cell_id)["trusted_policy"]["task_id"],
        "action": "synthetic_accept",
        "operation_id": operation_id,
        "cell_id": cell_id,
        "attempt_id": attempt_id,
        "checkpoint": checkpoint,
        "instance_id": instance_id,
        "commit_record_id": f"{attempt_id}:commit:{checkpoint_ordinal:02d}:{checkpoint}",
    }


def _checkpoint_evidence(
    *,
    matrix_run_id: str,
    cell_id: str,
    checkpoint: str,
    checkpoint_ordinal: int,
    attempt_id: str,
    source: dict[str, Any],
    active: WorkerProcess,
    w0: WorkerProcess,
    w1: WorkerProcess | None,
    broker: Broker,
    observation: Any,
    public_map: dict[str, Any],
    keys: TestKeyStore,
    expected: dict[str, Any],
    event_log: Path,
    lifecycle_steps: list[str],
    freeze_path: Path,
    execution_scope_context: dict[str, Any],
) -> tuple[dict[str, Any], dict[str, Any]]:
    scope_review = review_execution_scope({
        **execution_scope_context, 'profile_id': PROFILE_ID, 'matrix_run_id': matrix_run_id,
        'cell_id': cell_id, 'checkpoint': checkpoint,
    })
    if scope_review.value != 'PASS':
        raise ValueError(scope_review.reason)
    operation_id = deterministic_id(matrix_run_id, MATRIX_CELL_ORDER.index(cell_id) + 1, cell_id, "operation", checkpoint_ordinal)
    commit_record_id = f"{attempt_id}:commit:{checkpoint_ordinal:02d}:{checkpoint}"
    packet = make_packet(
        cell_id, source, keys, checkpoint, instance_id=active.instance_id, attempt_id=attempt_id,
        operation_id=operation_id, commit_record_id=commit_record_id,
    )
    worker_ack = _worker_roundtrip(
        active, {"command": "PROCESS", "operation_id": operation_id, "packet": packet}, "PROPOSAL_OBSERVED"
    )
    if worker_ack.get("operation_id") != operation_id:
        raise RuntimeError("WORKER_PROPOSAL_ACK_BINDING_MISMATCH")
    decision = evaluate(packet, source, public_map)
    proposal = packet["envelope"]["payload"]
    intent = precommit_operation_intent(proposal, source, decision)
    observation.require_admission("MATRIX_CHECKPOINT_WRITER")
    before = observation.begin_phase(checkpoint)
    broker_before = broker.snapshot()
    interval_start = time.perf_counter_ns()
    atomic_timeline: list[dict[str, Any]] = []
    if cell_id == "T10":
        revocation = broker.revoke(source["registry"]["grant_id"], len(events(event_log)) + 1)
        atomic_timeline.append({
            "kind": "REVOCATION_ACKNOWLEDGED", "host_ns": time.perf_counter_ns(),
            "scope": deepcopy(intent["scope"]), "revocation": revocation,
        })
    transaction_id = f"observation-txn:{attempt_id}:{checkpoint_ordinal:02d}:{operation_id}"
    observation.begin_writer_transaction(transaction_id, operation_id=operation_id, interface="Broker.atomic_commit")
    try:
        commit = broker.atomic_commit(
            operation_id, cell_id, proposal["proposal_hash"], decision, source, active.instance_id,
            operation_context=intent, proposal_envelope=packet["envelope"], public_signer_map=public_map,
        )
    except BaseException as exc:
        observation.finish_writer_transaction(transaction_id, "ROLLED_BACK", reason=f"{type(exc).__name__}:{exc}")
        raise
    else:
        observation.finish_writer_transaction(transaction_id, "COMMITTED")
    if atomic_timeline:
        atomic_timeline.append({
            "kind": "ATOMIC_BIND_COMPLETED", "host_ns": time.perf_counter_ns(),
            "scope": deepcopy(intent["scope"]),
        })
    after = observation.end_phase(checkpoint)
    broker_after = broker.snapshot()
    interval_end = time.perf_counter_ns()
    scoped_events = _scope_worker_events(
        events(event_log), task_id=source["trusted_policy"]["task_id"], attempt_id=attempt_id,
        checkpoint=checkpoint, w0=w0,
    )
    raw = {
        "task_id": source["trusted_policy"]["task_id"],
        "profile_id": PROFILE_ID,
        "matrix_run_id": matrix_run_id,
        "cell_id": cell_id,
        "checkpoint": checkpoint,
        "attempt_id": attempt_id,
        "operation_id": operation_id,
        "commit_record_id": commit_record_id,
        "active_instance_id": active.instance_id,
        "lifecycle_mode": lifecycle_mode(cell_id),
        "expected_w0_lifecycle_binding": {
            "instance_id": w0.instance_id,
            "os_handle_id": str(w0.outcome.host_handle),
            "start_evidence_ref": f"lifecycle:{attempt_id}:W0_START",
        },
        "source_inventory": source,
        "materialized_packet": proposal,
        "materialized_packet_hash": canonical_hash(proposal),
        "approval_envelopes": packet["approvals"],
        "public_signer_map": public_map,
        "current_registry": source["registry"],
        "supplied_decision": decision,
        "precommit_receiver_decision": deepcopy(decision),
        "final_action_gate": final_action_outcome(decision, commit),
        "proposal_envelope": packet["envelope"],
        "broker_before_snapshot": broker_before,
        "broker_after_snapshot": broker_after,
        "atomic_transition_chronology": atomic_timeline,
        "proposal_hash": proposal["proposal_hash"],
        "operation_intent": intent,
        "operation_intent_hash": canonical_hash(intent),
        "attempt_ref": commit_record_id,
        "gate_record_ref": commit_record_id,
        "record_scope": {"task_id": source["trusted_policy"]["task_id"], "attempt_id": attempt_id, "checkpoint": checkpoint},
        "observation_interval": {"start_ns": interval_start, "end_ns": interval_end, "domain": "HOST_PERF_COUNTER_NS"},
        "surface_observations": [
            {
                "surface_id": "effects", "target": "synthetic-sink", "coordinate": "synthetic-sink/effects",
                "hash_domain": "JCS_ROWS", "before_hash": canonical_hash(before["tables"]["effects"]["rows"]),
                "after_hash": canonical_hash(after["tables"]["effects"]["rows"]),
            },
            {
                "surface_id": "promotions", "target": "synthetic-sink", "coordinate": "synthetic-sink/promotions",
                "hash_domain": "JCS_ROWS", "before_hash": canonical_hash(before["tables"]["promotions"]["rows"]),
                "after_hash": canonical_hash(after["tables"]["promotions"]["rows"]),
            },
        ],
        "sink_before_snapshot": {
            "operations": broker_before["operations"],
            "effects": before["tables"]["effects"]["rows"],
            "promotions": before["tables"]["promotions"]["rows"],
            "observation_snapshot_id": before["snapshot_id"],
        },
        "sink_after_snapshot": {
            "operations": broker_after["operations"],
            "effects": after["tables"]["effects"]["rows"],
            "promotions": after["tables"]["promotions"]["rows"],
            "observation_snapshot_id": after["snapshot_id"],
        },
        "trusted_chronology": scoped_events,
        "worker_ack": worker_ack,
        "commit_evidence": commit,
        "append_only_history": True,
        "boundary_manifest": {"external_components": ["source", "authority_registry", "broker", "observer", "supervisor"]},
        "native_binding_status": "PASS",
        "availability_policy": "MISSING_IS_UNKNOWN",
        "observer_dependencies": ["common", "signing", "state_transfer"],
        "signature_controls_status": "PASS",
        "containment_status": "PASS",
        "memory_judge_mode": "EXCLUDED",
        "clock_mapping": {"semantic": "CGDR_TEST_TICKS", "native": "RFC3339", "lifecycle": "HOST_PERF_COUNTER_NS"},
        "implementation_classes": ["REUSED_UNMODIFIED", "BOUNDED_ADAPTER", "TEST_DOUBLE", "NOT_IMPLEMENTED"],
        "forbidden_identity_claims": False,
        **deepcopy(execution_scope_context),
        "implementation_freeze_ref": str(freeze_path),
    }
    observed = inspect_checkpoint(raw)
    alignment_input = {
        "matrix_run_id": matrix_run_id,
        "cell_id": cell_id,
        "attempt_id": attempt_id,
        "checkpoint": checkpoint,
        "lifecycle_mode": lifecycle_mode(cell_id),
        "lifecycle_steps": lifecycle_steps,
        "w0_instance_id": w0.instance_id,
        "w1_instance_id": None if w1 is None else w1.instance_id,
        "active_instance_id": active.instance_id,
        "w0_cleanup": w0.cleanup_status,
        "state_carriage": "PASS",
        "current_epoch": source["current_attestation"]["epoch"],
        "e0_status": "HISTORICAL_FENCED" if lifecycle_mode(cell_id) == "REPLACE_PROCESS" else "NOT_APPLICABLE",
        "readiness": "READY",
        "implementation_freeze": "BEFORE_FIRST_WORKER_START",
        "capture_gaps": observation.export_evidence()["gaps"],
        "writer_admission": "ADMITTED",
        "expected_effect_delta": expected["protected_effect_delta"],
        "actual_effect_delta": observed["actual_effect_delta"],
        "expected_promotion_delta": expected["confirmed_EA_delta"],
        "actual_promotion_delta": observed["actual_promotion_delta"],
        "approval_roots": observed["derived_gate"]["approvals"]["roots"],
        "required_approval_roots": observed["derived_gate"]["approvals"]["required"] or 0,
        "q_state": observed["derived_gate"]["q_state"],
        "qcr_valid": bool(source.get("resolution")),
        "expected_obligations": source["duty"]["liabilities"],
        "carried_obligations": proposal.get("duty", {}).get("liabilities"),
        "evidence_binding": {"matrix_run_id": matrix_run_id, "cell_id": cell_id, "attempt_id": attempt_id, "checkpoint": checkpoint},
        "attempt_coverage_complete": True,
        "registry_coverage_complete": isinstance(broker_after.get("authority"), list),
        "surface_inventory": raw["surface_observations"],
    }
    return raw, {
        "cell_id": cell_id,
        "checkpoint": checkpoint,
        "expected": {
            "admission": expected["admission"],
            "q_state": expected["q_state"],
            "protected_action_gate": expected["protected_action_gate"],
            "protected_effect_delta": expected["protected_effect_delta"],
            "confirmed_EA_delta": expected["confirmed_EA_delta"],
        },
        "actual": {
            "admission": decision["admission"],
            "q_state": decision["q_state"],
            "protected_action_gate": final_action_outcome(decision, commit),
            "protected_effect_delta": observed["actual_effect_delta"],
            "confirmed_EA_delta": observed["actual_promotion_delta"],
        },
        "conformance_match": False,
        "observer": observed,
        "alignment_input": alignment_input,
        "alignment_review": {"verdict": "PENDING_OWNED_EXIT", "issues": []},
    }


def _run_episode(
    *,
    args: argparse.Namespace,
    matrix: dict[str, Any],
    expected: dict[tuple[str, str], dict[str, Any]],
    episode_ordinal: int,
    cell_id: str,
    staged: Any,
    keys: TestKeyStore,
    public_map: dict[str, Any],
    execution_scope_binding: dict[str, Any] | None = None,
    actual_input_hashes: dict[str, str] | None = None,
) -> dict[str, Any]:
    execution_scope_context = validate_episode_execution_scope(
        args, matrix, cell_id, execution_scope_binding, actual_input_hashes,
    )
    namespace = episode_namespace(args.output, args.matrix_run_id, episode_ordinal, cell_id)
    root: Path = namespace["root"]
    root.mkdir(parents=True, exist_ok=False)
    attempt_id = namespace["attempt_id"]
    event_log: Path = namespace["event_log"]
    mode = lifecycle_mode(cell_id)
    checkpoints = checkpoint_plan(cell_id, matrix)
    initial = _initial_source(cell_id)
    w0 = WorkerProcess(args.distro, staged, event_log, cell_id, "W0")
    w1 = WorkerProcess(args.distro, staged, event_log, cell_id, "W1") if mode == "REPLACE_PROCESS" else None
    active = w1 or w0
    intent_checkpoint = "RESOLVED_CHECK" if "RESOLVED_CHECK" in checkpoints else checkpoints[0]
    intent_ordinal = checkpoints.index(intent_checkpoint) + 1
    intent_scope = _prospective_operation_scope(
        args.matrix_run_id, cell_id, attempt_id, intent_checkpoint, active.instance_id, intent_ordinal,
    )
    plan_source = _resolved_or_fault_source(
        intent_checkpoint, _source_for_active_instance(initial, active.instance_id, replacement=mode == "REPLACE_PROCESS"),
    )
    plan_packet = make_packet(
        cell_id, plan_source, keys, intent_checkpoint, instance_id=active.instance_id, attempt_id=attempt_id,
        operation_id=intent_scope["operation_id"], commit_record_id=intent_scope["commit_record_id"],
    )
    plan_decision = evaluate(plan_packet, plan_source, public_map)
    # The declared T10 intervention revokes before the atomic point. Its
    # precommit operation intent still expects one effect; gold is scoring only.
    planned_effect = plan_decision["action_gate"] == "ALLOW" and cell_id != "T10"
    plan = build_observation_plan(
        task_id=TASK_ID,
        cell_id=cell_id,
        attempt_id=attempt_id,
        checkpoint=intent_checkpoint,
        database=namespace["database"],
        path_boundary_root=root,
        operation_scope=intent_scope,
        expected_outcome="ALLOW_EXACTLY_ONE" if planned_effect else "HOLD_NO_EFFECT",
        phase_inventory=checkpoints,
    )
    broker, observation = prepare_prospective_observation(plan=plan, output=namespace["observation_output"])
    readiness = observation.readiness_receipt()
    if readiness.get("status") != "READY":
        raise RuntimeError("EPISODE_PROSPECTIVE_OBSERVATION_NOT_READY")
    freeze_path = root / "IMPLEMENTATION_FREEZE.json"
    write_json(freeze_path, {
        "matrix_run_id": args.matrix_run_id,
        "attempt_id": attempt_id,
        "cell_id": cell_id,
        "freeze_stage": "BEFORE_FIRST_WORKER_START",
        "worker_sha256": file_hash(args.worker),
        "run_batch_sha256": file_hash(Path(__file__)),
        "matrix_sha256": file_hash(args.matrix),
        "observation_acceptance_sha256": file_hash(args.observation_acceptance),
        "observation_calibration_sha256": file_hash(args.observation_calibration),
        "successor_baseline_sha256": file_hash(args.successor_baseline),
        "readiness_hash": canonical_hash(readiness),
        "preallocated_instances": {"W0": w0.instance_id, "W1": None if w1 is None else w1.instance_id},
    })
    lifecycle_steps: list[str] = []
    raw_rows: list[dict[str, Any]] = []
    result_rows: list[dict[str, Any]] = []
    current_source = initial
    carried: dict[str, Any] | None = None
    try:
        observation.invoke_first_start(lambda: w0.start(10), readiness_receipt=readiness)
        lifecycle_steps.append("W0_START")
        current_source = _source_for_active_instance(initial, w0.instance_id, replacement=False)
        carried = freeze_state(current_source)
        _worker_roundtrip(w0, {
            "command": "LOAD", "state_b64": carried["state_b64"], "state_sha256": hashlib.sha256(carried["bytes"]).hexdigest(),
            "message_id": deterministic_id(args.matrix_run_id, episode_ordinal, cell_id, "load"),
        }, "LOAD_ACK")
        lifecycle_steps.append("W0_LOAD")
        if mode == "SHAM_BARRIER":
            wait_id = deterministic_id(args.matrix_run_id, episode_ordinal, cell_id, "sham-wait")
            _worker_roundtrip(w0, {"command": "SHAM_WAIT", "wait_id": wait_id, "message_id": wait_id}, "SHAM_WAITING")
            lifecycle_steps.append("SHAM_WAIT")
            release_id = deterministic_id(args.matrix_run_id, episode_ordinal, cell_id, "release")
            _worker_roundtrip(w0, {"command": "RELEASE", "release_id": release_id, "message_id": release_id}, "RELEASED")
            lifecycle_steps.append("RELEASE")
            continue_id = deterministic_id(args.matrix_run_id, episode_ordinal, cell_id, "continue")
            _worker_roundtrip(w0, {"command": "CONTINUE", "continue_id": continue_id, "message_id": continue_id}, "CONTINUED")
            lifecycle_steps.append("CONTINUE")
        elif mode == "REPLACE_PROCESS":
            checkpoint_id = deterministic_id(args.matrix_run_id, episode_ordinal, cell_id, "w0-checkpoint")
            checkpoint0 = _worker_roundtrip(w0, {"command": "CHECKPOINT", "message_id": checkpoint_id}, "CHECKPOINT")
            lifecycle_steps.append("W0_CHECKPOINT")
            raw0, state0, decode_issues = decode_state_b64(checkpoint0.get("state_b64"))
            if decode_issues or raw0 != carried["bytes"] or state0 is None:
                raise RuntimeError(f"W0_CHECKPOINT_MISMATCH:{decode_issues}")
            checkpoint_path = namespace["checkpoint_store"] / "w0_checkpoint.bin"
            _write_bytes_create_only(checkpoint_path, raw0)
            lifecycle_steps.append("CHECKPOINT_CREATE_ONLY_WRITE")
            readback = checkpoint_path.read_bytes()
            if readback != raw0:
                raise RuntimeError("CHECKPOINT_DISK_READBACK_MISMATCH")
            lifecycle_steps.append("CHECKPOINT_DISK_READBACK")
            write_json(root / "E0_FENCE.json", {
                "matrix_run_id": args.matrix_run_id, "attempt_id": attempt_id, "cell_id": cell_id,
                "instance_id": w0.instance_id, "epoch": "E0", "status": "HISTORICAL_FENCED",
                "checkpoint_sha256": hashlib.sha256(readback).hexdigest(),
            })
            lifecycle_steps.append("E0_FENCED")
            w0.stop(deterministic_id(args.matrix_run_id, episode_ordinal, cell_id, "w0-stop"))
            lifecycle_steps.extend(["W0_STOP", "W0_OS_EXIT"])
            if w0.cleanup_status != "PROVEN":
                raise CleanupUnprovenError("W0 cleanup not proven before W1")
            observation.require_admission("SUCCESSOR_START")
            assert w1 is not None
            w1.start(10)
            lifecycle_steps.append("W1_START")
            restore_id = deterministic_id(args.matrix_run_id, episode_ordinal, cell_id, "w1-restore")
            _worker_roundtrip(w1, {
                "command": "RESTORE", "state_b64": base64.b64encode(readback).decode("ascii"),
                "state_sha256": hashlib.sha256(readback).hexdigest(), "checkpoint_seq": 1, "message_id": restore_id,
            }, "RESTORED")
            lifecycle_steps.append("W1_RESTORE")
            checkpoint1 = _worker_roundtrip(w1, {
                "command": "CHECKPOINT", "message_id": deterministic_id(args.matrix_run_id, episode_ordinal, cell_id, "w1-checkpoint")
            }, "CHECKPOINT")
            lifecycle_steps.append("W1_CHECKPOINT")
            raw1, _, decode1 = decode_state_b64(checkpoint1.get("state_b64"))
            state_check = validate_state_bytes(raw1 or b"", current_source, stated_hash=checkpoint1.get("state_sha256"))
            if decode1 or raw1 != readback or state_check["status"] != "PASS":
                raise RuntimeError(f"STATE_CARRIAGE_MISMATCH:{decode1}:{state_check['issues']}")
            lifecycle_steps.append("STATE_CARRIAGE_PASS")
            current_source = _source_for_active_instance(initial, w1.instance_id, replacement=True)
            write_json(root / "E1_CURRENT.json", {
                "matrix_run_id": args.matrix_run_id, "attempt_id": attempt_id, "cell_id": cell_id,
                "instance_id": w1.instance_id, "epoch": "E1", "status": "CURRENT",
                "predecessor_checkpoint_sha256": hashlib.sha256(readback).hexdigest(),
            })
            lifecycle_steps.append("E1_CURRENT")
        broker.bind_instance(current_source, active.instance_id)
        for checkpoint_ordinal, checkpoint in enumerate(checkpoints, 1):
            source = _resolved_or_fault_source(checkpoint, current_source)
            if checkpoint == "RESOLVED_CHECK":
                broker.advance_source(source, active.instance_id)
            raw, record = _checkpoint_evidence(
                matrix_run_id=args.matrix_run_id, cell_id=cell_id, checkpoint=checkpoint,
                checkpoint_ordinal=checkpoint_ordinal, attempt_id=attempt_id, source=source, active=active,
                w0=w0, w1=w1, broker=broker, observation=observation, public_map=public_map,
                keys=keys, expected=expected[(cell_id, checkpoint)], event_log=event_log,
                lifecycle_steps=lifecycle_steps + ["MEASURED_CHECKPOINTS"], freeze_path=freeze_path,
                execution_scope_context=execution_scope_context,
            )
            raw_rows.append(raw)
            result_rows.append(record)
            write_json(root / "raw" / f"{checkpoint}.json", raw)
        lifecycle_steps.append("MEASURED_CHECKPOINTS")
        active.stop(deterministic_id(args.matrix_run_id, episode_ordinal, cell_id, "active-stop"))
        lifecycle_steps.extend(["W1_STOP", "W1_OS_EXIT"] if mode == "REPLACE_PROCESS" else ["W0_STOP", "W0_OS_EXIT"])
        if active.cleanup_status != "PROVEN":
            raise CleanupUnprovenError("active worker cleanup not proven")
        for record in result_rows:
            alignment_input = record["alignment_input"]
            alignment_input["lifecycle_steps"] = list(lifecycle_steps)
            alignment_input["w0_cleanup"] = w0.cleanup_status
            alignment_input["state_carriage"] = "PASS"
            record["alignment_review"] = review_alignment_evidence(alignment_input)
        observation.mark_owned_exit(synthetic=False, binding={
            "active_instance_id": active.instance_id, "cleanup_status": active.cleanup_status,
            "matrix_run_id": args.matrix_run_id, "attempt_id": attempt_id,
        })
        observation_evidence = observation.finalize()
        prospective_review = review_observation_evidence(observation_evidence)
        if prospective_review["verdict"] in {"FAIL", "INCONCLUSIVE"}:
            raise RuntimeError(f"PROSPECTIVE_REVIEW_{prospective_review['verdict']}")
        write_json(root / "PROSPECTIVE_OBSERVATION_REVIEW.json", prospective_review)
        linked_logic = None
        if len(raw_rows) == 2 and checkpoints == ["OPEN_CHECK", "RESOLVED_CHECK"]:
            linked_logic = inspect_logic_path(raw_rows[0], raw_rows[1])
            write_json(root / "LINKED_LOGIC_PATH_REVIEW.json", linked_logic)
        cleanup = {
            "scope": {"task_id": raw_rows[0]["task_id"], "attempt_id": attempt_id, "active_instance_id": active.instance_id},
            "w0": w0.cleanup_status, "w1": None if w1 is None else w1.cleanup_status,
        }
        for raw, record in zip(raw_rows, result_rows):
            profile = review_profile_assertion(
                raw, record["expected"], record.pop("alignment_input"),
                prospective_evidence=observation_evidence, cleanup=cleanup,
                linked_evidence=(raw_rows[0], raw_rows[1]) if linked_logic is not None else None,
            )
            record.update(profile)
            record["observer"] = profile["candidate_assertions"]
            record["conformance_match"] = profile["profile_assertion"]["verdict"] == "PASS"
            write_json(root / "evidence" / f"{record['checkpoint']}.json", record)
        profile_values = [row["profile_assertion"]["verdict"] for row in result_rows]
        episode_verdict = "FAIL" if "FAIL" in profile_values else ("INCONCLUSIVE" if "INCONCLUSIVE" in profile_values else "PASS")
        result = {
            "profile_id": PROFILE_ID,
            "matrix_run_id": args.matrix_run_id,
            "cell_id": cell_id,
            "attempt_id": attempt_id,
            "execution_status": "COMPLETE",
            "conformance_verdict": episode_verdict,
            "profile_assertion": {"verdict": episode_verdict, "checkpoint_verdicts": profile_values},
            "lifecycle_mode": mode,
            "lifecycle_steps": lifecycle_steps,
            "checkpoint_results": result_rows,
            "prospective_review": prospective_review["verdict"],
            "effect_count": sum(row["actual"]["protected_effect_delta"] for row in result_rows),
            "promotion_count": sum(row["actual"]["confirmed_EA_delta"] for row in result_rows),
            "identity_continuity": "NOT_ESTABLISHED",
        }
        write_json(root / "EPISODE_RESULT.json", result)
        return result
    except BaseException:
        if not observation.finalized:
            try:
                observation.note_gap("MATRIX_EPISODE_ABORTED", cell_id)
            except BaseException:
                pass
        raise
    finally:
        for worker in (w1, w0):
            if worker is not None and worker.outcome.start_request_issued and worker.cleanup_status != "PROVEN":
                worker.abort()
        broker.close()


def run(args: argparse.Namespace) -> int:
    execution_scope_binding, matrix, actual_input_hashes = prepare_execution_scope(args)
    _require_matrix_run_id(args.matrix_run_id)
    output: Path = args.output.resolve()
    if output.exists():
        raise SystemExit(f"output collision: {output}")
    observation_inputs = verify_current_observation_inputs(
        args.observation_acceptance.resolve(), args.observation_calibration.resolve()
    )
    code_root = args.worker.resolve().parents[2]
    baseline_check = verify_successor_baseline(code_root, args.successor_baseline.resolve())
    matrix_check = validate_matrix_contract(matrix)
    if matrix_check["status"] != "PASS":
        raise ValueError(f"MATRIX_CONTRACT_INVALID:{matrix_check['issues']}")
    output.mkdir(parents=True, exist_ok=False)
    start_batch = time.perf_counter_ns()
    expected = expected_map(matrix)
    schema = load_json(args.report_schema)
    Draft202012Validator.check_schema(schema)
    keys = TestKeyStore(args.key_store)
    public_map = keys.public_map({
        "producer-alpha": "root:alpha", "alias-alpha-1": "root:alpha",
        "alias-alpha-2": "root:alpha", "approver-beta": "root:beta",
    })
    write_json(output / "PUBLIC_SIGNER_ROOT_MAP.json", public_map)
    write_json(output / "MATRIX_RUN_BINDING.json", {
        "matrix_run_id": args.matrix_run_id,
        "attempt_policy": "DETERMINISTIC_FROM_RUN_EPISODE_CHECKPOINT_ORDINALS",
        "batch_retry": "FORBIDDEN",
        "matrix_contract": matrix_check,
        "current_observation_inputs": observation_inputs,
        "successor_baseline_check": baseline_check,
        "execution_scope_binding": execution_scope_binding,
        "execution_scope_binding_hash": canonical_hash(execution_scope_binding),
        "actual_input_hashes": actual_input_hashes,
        "protected_inputs": {
            "matrix": {"path": str(args.matrix.resolve()), "sha256": file_hash(args.matrix)},
            "observation_acceptance": {"path": str(args.observation_acceptance.resolve()), "sha256": file_hash(args.observation_acceptance)},
            "observation_calibration": {"path": str(args.observation_calibration.resolve()), "sha256": file_hash(args.observation_calibration)},
            "successor_baseline": {"path": str(args.successor_baseline.resolve()), "sha256": file_hash(args.successor_baseline)},
        },
    })
    staged = stage_worker(args.distro, args.worker, args.stage_dir, output / "setup.jsonl", local_launcher=args.launcher)
    completed: dict[str, dict[str, Any]] = {}
    aborted_after: str | None = None
    failure: BaseException | None = None
    for episode_ordinal, cell_id in enumerate(MATRIX_CELL_ORDER, 1):
        if (time.perf_counter_ns() - start_batch) / 1e9 > args.batch_timeout_seconds:
            failure = TimeoutError("batch exceeded frozen safety ceiling")
            aborted_after = cell_id
            break
        try:
            result = _run_episode(
                args=args, matrix=matrix, expected=expected, episode_ordinal=episode_ordinal,
                cell_id=cell_id, staged=staged, keys=keys, public_map=public_map,
                execution_scope_binding=execution_scope_binding, actual_input_hashes=actual_input_hashes,
            )
            completed[cell_id] = result
        except BaseException as exc:
            failure = exc
            aborted_after = cell_id
            break
    denominator = denominator_result(matrix, completed, aborted_after)
    summary = {
        "task_id": TASK_ID,
        "profile_id": PROFILE_ID,
        "matrix_run_id": args.matrix_run_id,
        "episode_denominator": MATRIX_EPISODES,
        "checkpoint_denominator": MATRIX_CHECKPOINTS,
        "episode_count_completed": len(completed),
        "checkpoint_count_observed": sum(len(row.get("checkpoint_results", [])) for row in completed.values()),
        "episodes": denominator,
        "effects_observed": sum(row.get("effect_count", 0) for row in completed.values()),
        "memory_promotions_observed": sum(row.get("promotion_count", 0) for row in completed.values()),
        "conformance_verdict": (
            "INCONCLUSIVE" if failure is not None or len(completed) != MATRIX_EPISODES
            else "PASS" if all(row["conformance_verdict"] == "PASS" for row in completed.values())
            else "FAIL"
        ),
        "failure": None if failure is None else f"{type(failure).__name__}:{failure}",
        "aborted_after": aborted_after,
        "batch_retry": "FORBIDDEN",
        "model_calls": 0,
        "identity_continuity": "NOT_ESTABLISHED",
        "historical_full_interval_absence": "NOT_ESTABLISHED",
    }
    write_json(output / "MEASURED_BATCH_SUMMARY.json", summary)
    print(json.dumps(summary, sort_keys=True))
    return 0 if summary["conformance_verdict"] == "PASS" else 1


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Current selected-process 18/21 matrix harness")
    parser.add_argument("--execute-authorized", action="store_true")
    parser.add_argument("--execution-scope-binding", type=Path)
    parser.add_argument("--matrix-run-id", required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--matrix", type=Path, required=True)
    parser.add_argument("--report-schema", type=Path, required=True)
    parser.add_argument("--key-store", type=Path, required=True)
    parser.add_argument("--worker", type=Path, required=True)
    parser.add_argument("--launcher", type=Path, required=True)
    parser.add_argument("--observation-acceptance", type=Path, required=True)
    parser.add_argument("--observation-calibration", type=Path, required=True)
    parser.add_argument("--successor-baseline", type=Path, required=True)
    parser.add_argument("--distro", default="Ubuntu")
    parser.add_argument("--stage-dir", required=True)
    parser.add_argument("--batch-timeout-seconds", type=int, default=1800)
    args = parser.parse_args(argv)
    if not args.execute_authorized:
        print("NOT_RUN: measured matrix requires explicit --execute-authorized", flush=True)
        return 3
    return run(args)


if __name__ == "__main__":
    raise SystemExit(main())
