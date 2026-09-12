from __future__ import annotations

import json
import os
import sqlite3
import time
from copy import deepcopy
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Callable
from urllib.parse import quote

from .broker import Broker
from .common import canonical_hash, write_json


TASK_ID = "CGDR_SELECTED_PROCESS_PROSPECTIVE_OBSERVATION_R1_6K"
PLAN_SCHEMA = "CGDR_PROSPECTIVE_OBSERVATION_PLAN_V1"
EVIDENCE_SCHEMA = "CGDR_PROSPECTIVE_OBSERVATION_EVIDENCE_V1"
REVIEW_SCHEMA = "CGDR_PROSPECTIVE_OBSERVATION_REVIEW_V1"
SURFACES = ("effects", "promotions")
TRIGGER_PREFIX = "_cgdr_observation_"
DEFAULT_MAX_EVENTS = 256
DEFAULT_MAX_SNAPSHOT_ROWS = 512
DEFAULT_MAX_CLOCK_RESIDUAL_NS = 1_000_000_000
PHASE_BINDING_SCHEMA = "CGDR_PHASE_SNAPSHOT_CLOCK_EVENT_AUDIT_V2"
PHASE_V2_REQUIRED_FIELDS = (
    "name",
    "phase_id",
    "phase_order",
    "binding_version",
    "status",
    "begin_snapshot_id",
    "begin_snapshot",
    "begin_snapshot_hash",
    "end_snapshot_id",
    "end_snapshot",
    "end_snapshot_hash",
    "start_audit_seq",
    "end_audit_seq",
    "window_start_clock",
    "window_end_clock",
    "begin_event_ref",
    "end_event_ref",
)
REVIEW_BINDING_FIELDS = (
    "schema",
    "task_id",
    "attempt_id",
    "reviewed_evidence_hash",
    "reviewed_plan_hash",
    "verdict",
    "issues",
    "phase_results",
    "phase_inventory",
    "audit_coverage",
    "committed_audit_event_count",
    "rolled_back_attempt_count",
    "pre_execution_barrier",
    "clock_correlation",
    "claim_boundary",
)


def _nonempty_string(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _plain_int(value: Any, *, minimum: int = 0) -> bool:
    return isinstance(value, int) and not isinstance(value, bool) and value >= minimum


def _hash_string(value: Any) -> bool:
    return isinstance(value, str) and len(value) == 64 and all(char in "0123456789abcdef" for char in value.lower())


def _review_binding_body(review: dict[str, Any]) -> dict[str, Any]:
    """Canonical deterministic review fields bound at the native-emission boundary."""
    return {field: deepcopy(review.get(field)) for field in REVIEW_BINDING_FIELDS}


def _phase_v2_descriptor_shape_issues(name: str, phase: Any) -> list[dict[str, Any]]:
    """Validate the fixed V2 descriptor contract without creating a generic schema engine."""
    if not isinstance(phase, dict):
        return [{
            "code": "PHASE_V2_DESCRIPTOR_MALFORMED",
            "classification": "FAIL",
            "phase": name,
        }]
    issues: list[dict[str, Any]] = []
    for field in PHASE_V2_REQUIRED_FIELDS:
        value = phase.get(field)
        missing = (
            field not in phase
            or value is None
            or (isinstance(value, str) and not value.strip())
            or (field in {"begin_snapshot", "end_snapshot", "window_start_clock", "window_end_clock", "begin_event_ref", "end_event_ref"} and not value)
        )
        if missing:
            issues.append({
                "code": "PHASE_V2_REQUIRED_FIELD_MISSING",
                "classification": "INCOMPLETE",
                "phase": name,
                "field": field,
            })
    string_fields = {
        "name", "phase_id", "binding_version", "status", "begin_snapshot_id",
        "begin_snapshot_hash", "end_snapshot_id", "end_snapshot_hash",
    }
    dict_fields = {
        "begin_snapshot", "end_snapshot", "window_start_clock", "window_end_clock",
        "begin_event_ref", "end_event_ref",
    }
    for field in string_fields:
        if field in phase and phase.get(field) is not None and not _nonempty_string(phase.get(field)):
            issues.append({
                "code": "PHASE_V2_REQUIRED_FIELD_TYPE_INVALID",
                "classification": "FAIL",
                "phase": name,
                "field": field,
            })
    for field in dict_fields:
        if field in phase and phase.get(field) is not None and not isinstance(phase.get(field), dict):
            issues.append({
                "code": "PHASE_V2_REQUIRED_FIELD_TYPE_INVALID",
                "classification": "FAIL",
                "phase": name,
                "field": field,
            })
    for field in ("phase_order", "start_audit_seq", "end_audit_seq"):
        minimum = 1 if field == "phase_order" else 0
        if field in phase and phase.get(field) is not None and not _plain_int(phase.get(field), minimum=minimum):
            issues.append({
                "code": "PHASE_V2_REQUIRED_FIELD_TYPE_INVALID",
                "classification": "FAIL",
                "phase": name,
                "field": field,
            })
    for field in ("begin_snapshot_hash", "end_snapshot_hash"):
        if _nonempty_string(phase.get(field)) and not _hash_string(phase.get(field)):
            issues.append({
                "code": "PHASE_V2_REQUIRED_FIELD_TYPE_INVALID",
                "classification": "FAIL",
                "phase": name,
                "field": field,
            })
    version = phase.get("binding_version")
    if _nonempty_string(version) and version != PHASE_BINDING_SCHEMA:
        issues.append({
            "code": "PHASE_BINDING_VERSION_MISMATCH",
            "classification": "FAIL",
            "phase": name,
            "actual": version,
            "expected": PHASE_BINDING_SCHEMA,
        })
    return issues


class ObservationError(RuntimeError):
    def __init__(self, code: str, details: dict[str, Any] | None = None):
        super().__init__(code)
        self.code = code
        self.details = details or {}

    def as_dict(self) -> dict[str, Any]:
        return {"code": self.code, "details": self.details}


def _rfc3339_ns(value: int) -> str:
    seconds, nanos = divmod(value, 1_000_000_000)
    prefix = datetime.fromtimestamp(seconds, tz=timezone.utc).strftime("%Y-%m-%dT%H:%M:%S")
    return f"{prefix}.{nanos:09d}Z"


def system_clock_pair(label: str) -> dict[str, Any]:
    before = time.perf_counter_ns()
    utc_ns = time.time_ns()
    after = time.perf_counter_ns()
    info = time.get_clock_info("perf_counter")
    return {
        "label": label,
        "monotonic_domain": "PYTHON_PERF_COUNTER_NS_CURRENT_PROCESS",
        "utc_domain": "LOCAL_OS_UTC_VIA_PYTHON_TIME_NS",
        "monotonic_before_ns": str(before),
        "utc_ns": str(utc_ns),
        "utc": _rfc3339_ns(utc_ns),
        "monotonic_after_ns": str(after),
        "correlation_uncertainty_ns": str(after - before),
        "monotonic": bool(info.monotonic),
        "adjustable": bool(info.adjustable),
        "clock_resolution_ns": str(max(1, int(info.resolution * 1_000_000_000))),
        "claim_boundary": "Local UTC/perf-counter correlation only; no external UTC accuracy claim.",
    }


def _append_jsonl_fsync(path: Path, value: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8", newline="\n") as stream:
        stream.write(json.dumps(value, sort_keys=True, ensure_ascii=False, separators=(",", ":")) + "\n")
        stream.flush()
        os.fsync(stream.fileno())


def _inside(path: Path, root: Path) -> bool:
    try:
        path.resolve().relative_to(root.resolve())
        return True
    except ValueError:
        return False


def build_observation_plan(
    *,
    task_id: str,
    cell_id: str,
    attempt_id: str,
    checkpoint: str,
    database: Path,
    path_boundary_root: Path,
    operation_scope: dict[str, Any],
    expected_outcome: str,
    phase_inventory: list[str] | None = None,
    max_events: int = DEFAULT_MAX_EVENTS,
    max_snapshot_rows: int = DEFAULT_MAX_SNAPSHOT_ROWS,
    clock_pair: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """Freeze the observation target and intent before the target database exists."""
    database = database.resolve()
    boundary = path_boundary_root.resolve()
    if not _inside(database, boundary):
        raise ObservationError("DATABASE_OUTSIDE_TASK_BOUNDARY", {"database": str(database), "root": str(boundary)})
    if expected_outcome not in {"HOLD_NO_EFFECT", "ALLOW_EXACTLY_ONE"}:
        raise ObservationError("INVALID_EXPECTED_OUTCOME")
    required = {
        "task_id", "action", "operation_id", "cell_id", "attempt_id", "checkpoint",
        "instance_id", "commit_record_id",
    }
    if set(operation_scope) != required or any(not isinstance(operation_scope.get(key), str) or not operation_scope[key] for key in required):
        raise ObservationError("OPERATION_SCOPE_INCOMPLETE", {"required": sorted(required), "actual": sorted(operation_scope)})
    if operation_scope["cell_id"] != cell_id:
        raise ObservationError("OPERATION_SCOPE_PLAN_MISMATCH")
    if operation_scope["attempt_id"] != attempt_id or operation_scope["checkpoint"] != checkpoint:
        raise ObservationError("OPERATION_SCOPE_ATTEMPT_MISMATCH")
    if not (1 <= max_events <= 4096 and 1 <= max_snapshot_rows <= 4096):
        raise ObservationError("OBSERVATION_LIMIT_OUT_OF_RANGE")
    phases = [checkpoint] if phase_inventory is None else list(phase_inventory)
    if not phases or len(phases) != len(set(phases)) or any(not isinstance(name, str) or not name for name in phases):
        raise ObservationError("PHASE_INVENTORY_INVALID")
    created = deepcopy(clock_pair or system_clock_pair("PLAN_FROZEN"))
    plan = {
        "schema": PLAN_SCHEMA,
        "task_id": task_id,
        "cell_id": cell_id,
        "attempt_id": attempt_id,
        "checkpoint": checkpoint,
        "phase_inventory": phases,
        "phase_binding_schema": PHASE_BINDING_SCHEMA,
        "database": {
            "path": str(database),
            "path_boundary_root": str(boundary),
            "create_policy": "CREATE_ONLY_REFUSE_EXISTING",
            "journal_mode": "WAL",
        },
        "surfaces": [
            {
                "surface_id": name,
                "table": name,
                "target_ref": "synthetic-sink",
                "target_coordinate": f"synthetic-sink/{name}",
                "captured_dml": ["INSERT", "UPDATE", "DELETE"],
                "snapshot_reader": "SEPARATE_SQLITE_MODE_RO_READ_TRANSACTION",
            }
            for name in SURFACES
        ],
        "writer_scope": {
            "connection_id": "BROKER_PRIMARY_CONNECTION",
            "allowed_interfaces": ["Broker.bind_instance", "Broker.atomic_commit", "bounded_calibration_dml"],
            "unknown_connection_policy": "SURFACE_DML_FAILS_WITH_MISSING_TRANSACTION_UDF",
            "owner_assumption": "TRUSTED_TASK_LOCAL_DATABASE_OWNER",
            "not_covered": ["hostile database owner", "direct database-file writes", "unknown external callers"],
        },
        "expected_operation_intent": {
            "origin": "TRUSTED_OPERATION_CONTEXT_PRE_OBSERVATION",
            "outer_observation_task_id": task_id,
            "operation_policy_task_id": operation_scope["task_id"],
            "scope": deepcopy(operation_scope),
            "expected_outcome": expected_outcome,
        },
        "alternate_paths": [{
            "path_id": "offline-broker-no-queue-retry",
            "status": "NOT_REACHABLE",
            "basis": "The bounded Broker exposes no queue, retry, socket, or external effect writer interface.",
        }],
        "technical_writes": [
            "observation audit rows", "transaction-attempt journal", "clock-pair journal",
            "consistent readback snapshots", "configuration receipts",
        ],
        "excluded_surfaces": [
            "authority", "operations", "source_bindings", "host network", "host processes",
            "historical R1.6I/R1.6J databases", "measured matrix",
        ],
        "limits": {
            "max_committed_audit_events": max_events,
            "max_snapshot_rows_per_surface": max_snapshot_rows,
            "max_clock_residual_ns": DEFAULT_MAX_CLOCK_RESIDUAL_NS,
            "overflow_policy": "ABORT_SURFACE_DML_NO_SILENT_DROP",
        },
        "plan_created_clock": created,
        "claim_boundary": (
            "Committed changes to effects/promotions through the declared trusted task-local SQLite writer only; "
            "not arbitrary file writes, hostile database ownership, host-wide network interception, or process evidence."
        ),
    }
    plan["plan_hash"] = canonical_hash({key: value for key, value in plan.items() if key != "plan_hash"})
    return plan


def _validate_plan(plan: dict[str, Any]) -> None:
    if plan.get("schema") != PLAN_SCHEMA:
        raise ObservationError("OBSERVATION_PLAN_SCHEMA_MISMATCH")
    body = {key: value for key, value in plan.items() if key != "plan_hash"}
    if plan.get("plan_hash") != canonical_hash(body):
        raise ObservationError("OBSERVATION_PLAN_HASH_MISMATCH")
    surface_ids = [item.get("surface_id") for item in plan.get("surfaces", []) if isinstance(item, dict)]
    if surface_ids != list(SURFACES):
        raise ObservationError("OBSERVATION_SURFACE_SET_MISMATCH")
    phases = plan.get("phase_inventory")
    if (
        not isinstance(phases, list)
        or not phases
        or len(phases) != len(set(phases))
        or any(not isinstance(name, str) or not name for name in phases)
    ):
        raise ObservationError("PHASE_INVENTORY_INVALID")
    if plan.get("phase_binding_schema") != PHASE_BINDING_SCHEMA:
        raise ObservationError("PHASE_BINDING_SCHEMA_MISMATCH")
    database = Path(str((plan.get("database") or {}).get("path", ""))).resolve()
    boundary = Path(str((plan.get("database") or {}).get("path_boundary_root", ""))).resolve()
    if not _inside(database, boundary):
        raise ObservationError("DATABASE_OUTSIDE_TASK_BOUNDARY")


def _trigger_sql(max_events: int) -> str:
    def trigger(name: str, timing: str, table: str, dml: str, row_key: str, old_json: str, new_json: str) -> str:
        return f"""
CREATE TRIGGER {name} AFTER {timing} ON {table}
BEGIN
  SELECT CASE WHEN (SELECT COUNT(*) FROM _cgdr_observation_audit) >= {max_events}
    THEN RAISE(ABORT, 'CGDR_OBSERVATION_EVENT_LIMIT') END;
  INSERT INTO _cgdr_observation_audit(
    transaction_id,surface_id,dml_kind,row_key,old_row_json,new_row_json,event_clock_json
  ) VALUES(
    cgdr_observation_txn_id(),'{table}','{dml}',{row_key},{old_json},{new_json},cgdr_observation_clock_pair()
  );
END;
"""

    effect_new = "json_object('effect_id',NEW.effect_id,'operation_id',NEW.operation_id,'cell_id',NEW.cell_id,'payload',json(NEW.payload))"
    effect_old = "json_object('effect_id',OLD.effect_id,'operation_id',OLD.operation_id,'cell_id',OLD.cell_id,'payload',json(OLD.payload))"
    promotion_new = "json_object('promotion_id',NEW.promotion_id,'cell_id',NEW.cell_id,'payload',json(NEW.payload))"
    promotion_old = "json_object('promotion_id',OLD.promotion_id,'cell_id',OLD.cell_id,'payload',json(OLD.payload))"
    return """
CREATE TABLE _cgdr_observation_meta(
  singleton INTEGER PRIMARY KEY CHECK(singleton=1),
  plan_hash TEXT NOT NULL,
  writer_connection_id TEXT NOT NULL,
  installed_utc TEXT NOT NULL
);
CREATE TABLE _cgdr_observation_audit(
  audit_seq INTEGER PRIMARY KEY AUTOINCREMENT,
  transaction_id TEXT NOT NULL,
  surface_id TEXT NOT NULL CHECK(surface_id IN ('effects','promotions')),
  dml_kind TEXT NOT NULL CHECK(dml_kind IN ('INSERT','UPDATE','DELETE')),
  row_key TEXT NOT NULL,
  old_row_json TEXT,
  new_row_json TEXT,
  event_clock_json TEXT NOT NULL
);
""" + trigger("_cgdr_observation_effects_ai", "INSERT", "effects", "INSERT", "NEW.effect_id", "NULL", effect_new) + \
        trigger("_cgdr_observation_effects_au", "UPDATE", "effects", "UPDATE", "NEW.effect_id", effect_old, effect_new) + \
        trigger("_cgdr_observation_effects_ad", "DELETE", "effects", "DELETE", "OLD.effect_id", effect_old, "NULL") + \
        trigger("_cgdr_observation_promotions_ai", "INSERT", "promotions", "INSERT", "NEW.promotion_id", "NULL", promotion_new) + \
        trigger("_cgdr_observation_promotions_au", "UPDATE", "promotions", "UPDATE", "NEW.promotion_id", promotion_old, promotion_new) + \
        trigger("_cgdr_observation_promotions_ad", "DELETE", "promotions", "DELETE", "OLD.promotion_id", promotion_old, "NULL")


class ProspectiveObservation:
    """Bounded collector attached to one already-created Broker connection."""

    def __init__(
        self,
        broker: Broker,
        plan: dict[str, Any],
        output: Path,
        *,
        clock: Callable[[str], dict[str, Any]] | None = None,
    ):
        _validate_plan(plan)
        self.broker = broker
        self.database = broker.path.resolve()
        self.plan = deepcopy(plan)
        self.output = output.resolve()
        self.clock = clock or system_clock_pair
        self._current_transaction_id: str | None = None
        self._events: list[dict[str, Any]] = []
        self._transactions: list[dict[str, Any]] = []
        self._clock_pairs: list[dict[str, Any]] = []
        self._snapshots: list[dict[str, Any]] = []
        self._phases: dict[str, dict[str, Any]] = {}
        self._gaps: list[dict[str, Any]] = []
        self._admission_blocked_reason: dict[str, Any] | None = None
        self._ready = False
        self._first_start_consumed = False
        self._first_start_callback = False
        self._owned_exit = False
        self._finalized = False
        self._initial_configuration: dict[str, Any] | None = None
        if self.database != Path(self.plan["database"]["path"]).resolve():
            raise ObservationError("OBSERVATION_TARGET_DATABASE_MISMATCH")
        self._initialize()

    @property
    def ready(self) -> bool:
        return self._ready

    @property
    def finalized(self) -> bool:
        return self._finalized

    def _clock(self, label: str) -> dict[str, Any]:
        try:
            pair = deepcopy(self.clock(label))
            required = {
                "label", "monotonic_domain", "utc_domain", "monotonic_before_ns", "utc_ns",
                "utc", "monotonic_after_ns", "correlation_uncertainty_ns",
            }
            if not required.issubset(pair) or pair.get("label") != label:
                raise ValueError("clock pair shape")
            pair["pair_seq"] = len(self._clock_pairs) + 1
            pair["pair_id"] = f"clock-pair:{self.plan['attempt_id']}:{pair['pair_seq']}"
            self._clock_pairs.append(pair)
            _append_jsonl_fsync(self.output / "raw_clock_pairs.jsonl", pair)
            return pair
        except BaseException as exc:
            self._latch_gap("CLOCK_CAPTURE_FAILED", f"{type(exc).__name__}:{exc}")
            raise ObservationError("CLOCK_CAPTURE_FAILED", {"exception": f"{type(exc).__name__}:{exc}"}) from exc

    def _append_event(self, kind: str, **details: Any) -> dict[str, Any]:
        pair = self._clock(f"EVENT:{kind}")
        base = {
            "sequence": len(self._events) + 1,
            "kind": kind,
            "clock_pair_id": pair["pair_id"],
            "previous_event_hash": self._events[-1]["event_hash"] if self._events else None,
            **details,
        }
        base["event_hash"] = canonical_hash(base)
        self._events.append(base)
        try:
            _append_jsonl_fsync(self.output / "observation_events.jsonl", base)
        except BaseException as exc:
            self._latch_gap("EVENT_JOURNAL_PERSIST_FAILED", f"{type(exc).__name__}:{exc}")
            raise ObservationError(
                "EVENT_JOURNAL_PERSIST_FAILED",
                {"kind": kind, "exception": f"{type(exc).__name__}:{exc}"},
            ) from exc
        return base

    def _latch_gap(self, code: str, detail: str) -> None:
        row = {"code": code, "detail": detail}
        self._ready = False
        if self._admission_blocked_reason is None:
            self._admission_blocked_reason = deepcopy(row)
        if row not in self._gaps:
            self._gaps.append(row)

    def require_admission(self, stage: str) -> None:
        """Fail closed for new work while retaining diagnostic/finalization paths."""
        if self._admission_blocked_reason is not None or self._gaps:
            raise ObservationError(
                "KNOWN_CAPTURE_GAP_ADMISSION_BLOCKED",
                {"stage": stage, "reason": deepcopy(self._admission_blocked_reason or self._gaps[0])},
            )
        if not self._ready or self._finalized:
            raise ObservationError("ADMISSION_OUTSIDE_ACTIVE_CAPTURE", {"stage": stage})

    def _event_clock_udf(self) -> str:
        if self._current_transaction_id is None:
            raise sqlite3.OperationalError("CGDR_OBSERVATION_TRANSACTION_CONTEXT_MISSING")
        pair = self._clock(f"SQL_TRIGGER:{self._current_transaction_id}")
        return json.dumps(pair, sort_keys=True, separators=(",", ":"))

    def _transaction_id_udf(self) -> str:
        if self._current_transaction_id is None:
            raise sqlite3.OperationalError("CGDR_OBSERVATION_TRANSACTION_CONTEXT_MISSING")
        return self._current_transaction_id

    def _initialize(self) -> None:
        if self.database.exists() is False:
            raise ObservationError("BROKER_DATABASE_MISSING_AFTER_CREATE")
        self.broker.db.create_function("cgdr_observation_txn_id", 0, self._transaction_id_udf)
        self.broker.db.create_function("cgdr_observation_clock_pair", 0, self._event_clock_udf)
        self.broker.db.execute("PRAGMA recursive_triggers=ON")
        installed = self._clock("HOOK_INSTALL")
        try:
            self.broker.db.executescript(_trigger_sql(int(self.plan["limits"]["max_committed_audit_events"])))
            self.broker.db.execute(
                "INSERT INTO _cgdr_observation_meta VALUES(1,?,?,?)",
                (self.plan["plan_hash"], self.plan["writer_scope"]["connection_id"], installed["utc"]),
            )
        except BaseException as exc:
            self._gaps.append({"code": "CAPTURE_HOOK_INSTALL_FAILED", "detail": f"{type(exc).__name__}:{exc}"})
            raise ObservationError("CAPTURE_HOOK_INSTALL_FAILED", {"exception": f"{type(exc).__name__}:{exc}"}) from exc
        self._append_event("DATABASE_AND_TABLES_CREATED", database=str(self.database))
        self._append_event("CAPTURE_HOOKS_INSTALLED", mechanism="SQLITE_AFTER_TRIGGERS_TRANSACTIONAL_AUDIT")
        self._initial_configuration = self.configuration_snapshot()
        write_json(self.output / "BOUNDARY_CONFIGURATION.json", self._initial_configuration)
        baseline = self.snapshot("BASELINE_BEFORE_FIRST_START")
        self._append_event("INDEPENDENT_BASELINE_READBACK", snapshot_id=baseline["snapshot_id"])
        self._append_event(
            "SCOPE_CLOCK_CONFIGURATION_BOUND",
            plan_hash=self.plan["plan_hash"],
            configuration_hash=self._initial_configuration["configuration_hash"],
        )
        self._ready = True
        self._append_event("OBSERVATION_READY", baseline_snapshot_id=baseline["snapshot_id"])

    def configuration_snapshot(self) -> dict[str, Any]:
        rows = self.broker.db.execute(
            "SELECT type,name,tbl_name,sql FROM sqlite_master "
            "WHERE name LIKE '_cgdr_observation_%' ORDER BY type,name"
        ).fetchall()
        config = {
            "database": str(self.database),
            "plan_hash": self.plan["plan_hash"],
            "sqlite_version": sqlite3.sqlite_version,
            "journal_mode": self.broker.db.execute("PRAGMA journal_mode").fetchone()[0],
            "recursive_triggers": self.broker.db.execute("PRAGMA recursive_triggers").fetchone()[0],
            "writer_connection_id": self.plan["writer_scope"]["connection_id"],
            "instrumentation": [
                {"type": row[0], "name": row[1], "table": row[2], "sql": row[3]}
                for row in rows
            ],
            "surface_columns": {
                table: [
                    {"name": row[1], "type": row[2], "not_null": bool(row[3]), "primary_key": bool(row[5])}
                    for row in self.broker.db.execute(f"PRAGMA table_info({table})").fetchall()
                ]
                for table in SURFACES
            },
            "scope_limit": deepcopy(self.plan["writer_scope"]),
        }
        config["configuration_hash"] = canonical_hash(config)
        return config

    def _readonly_connection(self) -> sqlite3.Connection:
        uri = "file:" + quote(self.database.as_posix(), safe="/:_") + "?mode=ro"
        connection = sqlite3.connect(uri, uri=True, isolation_level=None)
        connection.execute("PRAGMA query_only=ON")
        return connection

    @staticmethod
    def _decode_payload(value: str) -> Any:
        try:
            return json.loads(value)
        except json.JSONDecodeError:
            return {"invalid_json_sha256": canonical_hash(value)}

    def snapshot(self, label: str) -> dict[str, Any]:
        if self._finalized:
            raise ObservationError("SNAPSHOT_AFTER_FINALIZATION")
        start = self._clock(f"SNAPSHOT_BEGIN:{label}")
        connection = self._readonly_connection()
        try:
            connection.execute("BEGIN")
            data_version = connection.execute("PRAGMA data_version").fetchone()[0]
            effects = [
                {"effect_id": row[0], "operation_id": row[1], "cell_id": row[2], "payload": self._decode_payload(row[3])}
                for row in connection.execute(
                    "SELECT effect_id,operation_id,cell_id,payload FROM effects ORDER BY effect_id"
                ).fetchall()
            ]
            promotions = [
                {"promotion_id": row[0], "cell_id": row[1], "payload": self._decode_payload(row[2])}
                for row in connection.execute(
                    "SELECT promotion_id,cell_id,payload FROM promotions ORDER BY promotion_id"
                ).fetchall()
            ]
            raw_audit = connection.execute(
                "SELECT audit_seq,transaction_id,surface_id,dml_kind,row_key,old_row_json,new_row_json,event_clock_json "
                "FROM _cgdr_observation_audit ORDER BY audit_seq"
            ).fetchall()
            max_rows = int(self.plan["limits"]["max_snapshot_rows_per_surface"])
            if len(effects) > max_rows or len(promotions) > max_rows:
                raise ObservationError("SNAPSHOT_ROW_LIMIT_EXCEEDED")
            audit = [{
                "audit_seq": row[0],
                "transaction_id": row[1],
                "surface_id": row[2],
                "dml_kind": row[3],
                "row_key": row[4],
                "old_row": None if row[5] is None else json.loads(row[5]),
                "new_row": None if row[6] is None else json.loads(row[6]),
                "event_clock": json.loads(row[7]),
            } for row in raw_audit]
            end = self._clock(f"SNAPSHOT_END:{label}")
            connection.commit()
        except BaseException:
            connection.rollback()
            raise
        finally:
            connection.close()
        snapshot = {
            "snapshot_id": f"snapshot:{self.plan['attempt_id']}:{len(self._snapshots) + 1}",
            "sequence": len(self._snapshots) + 1,
            "label": label,
            "database": str(self.database),
            "reader": "SEPARATE_SQLITE_MODE_RO_READ_TRANSACTION",
            "read_transaction": {
                "begin_clock": start,
                "end_clock": end,
                "state_definition": "One SQLite read transaction; state is pinned by the first SELECT and retained through both surface reads.",
                "data_version": data_version,
            },
            "tables": {
                "effects": {"rows": effects, "row_count": len(effects), "canonical_hash": canonical_hash(effects)},
                "promotions": {"rows": promotions, "row_count": len(promotions), "canonical_hash": canonical_hash(promotions)},
            },
            "audit_rows": audit,
            "audit_seq_max": audit[-1]["audit_seq"] if audit else 0,
            "audit_chain_hash": canonical_hash(audit),
            "wal_claim": "CONSISTENT_READ_TRANSACTION; no claim that copying the main file alone captures live WAL state.",
        }
        self._snapshots.append(snapshot)
        try:
            write_json(self.output / "snapshots" / f"{snapshot['sequence']:02d}_{label.casefold()}.json", snapshot)
        except BaseException as exc:
            self._latch_gap("SNAPSHOT_PERSIST_FAILED", f"{type(exc).__name__}:{exc}")
            raise ObservationError(
                "SNAPSHOT_PERSIST_FAILED",
                {"snapshot_id": snapshot["snapshot_id"], "exception": f"{type(exc).__name__}:{exc}"},
            ) from exc
        return snapshot

    def readiness_receipt(self) -> dict[str, Any]:
        baseline = next((item for item in self._snapshots if item["label"] == "BASELINE_BEFORE_FIRST_START"), None)
        ready_event = next((item for item in self._events if item["kind"] == "OBSERVATION_READY"), None)
        return {
            "schema": "CGDR_OBSERVATION_READINESS_V1",
            "status": "READY" if self._ready and baseline and ready_event and not self._gaps else "NOT_READY",
            "task_id": self.plan["task_id"],
            "attempt_id": self.plan["attempt_id"],
            "database": str(self.database),
            "plan_hash": self.plan["plan_hash"],
            "configuration_hash": None if self._initial_configuration is None else self._initial_configuration["configuration_hash"],
            "baseline_snapshot_id": None if baseline is None else baseline["snapshot_id"],
            "baseline_snapshot_hash": None if baseline is None else canonical_hash(baseline),
            "ready_event": deepcopy(ready_event),
            "gaps": deepcopy(self._gaps),
            "admission_state": "BLOCKED" if self._admission_blocked_reason is not None else "OPEN",
            "admission_blocked_reason": deepcopy(self._admission_blocked_reason),
        }

    @staticmethod
    def validate_readiness_receipt(receipt: dict[str, Any]) -> dict[str, Any]:
        """Pure data validation only; serialized readiness never executes a callback."""
        if not isinstance(receipt, dict) or receipt.get("schema") != "CGDR_OBSERVATION_READINESS_V1":
            raise ObservationError("PRE_EXECUTION_READINESS_SCHEMA_INVALID")
        if receipt.get("status") != "READY":
            raise ObservationError("PRE_EXECUTION_OBSERVATION_NOT_READY")
        if not receipt.get("baseline_snapshot_id") or not receipt.get("baseline_snapshot_hash"):
            raise ObservationError("PRE_EXECUTION_BASELINE_MISSING")
        if not receipt.get("plan_hash") or not receipt.get("configuration_hash"):
            raise ObservationError("PRE_EXECUTION_BINDING_MISSING")
        for field in ("task_id", "attempt_id", "database"):
            if not _nonempty_string(receipt.get(field)):
                raise ObservationError("PRE_EXECUTION_BINDING_MISSING", {"field": field})
        if not _hash_string(receipt.get("plan_hash")) or not _hash_string(receipt.get("configuration_hash")):
            raise ObservationError("PRE_EXECUTION_BINDING_INVALID")
        if not _hash_string(receipt.get("baseline_snapshot_hash")):
            raise ObservationError("PRE_EXECUTION_BASELINE_INVALID")
        ready_event = receipt.get("ready_event")
        if (
            not isinstance(ready_event, dict)
            or ready_event.get("kind") != "OBSERVATION_READY"
            or not _plain_int(ready_event.get("sequence"), minimum=1)
            or not _hash_string(ready_event.get("event_hash"))
        ):
            raise ObservationError("PRE_EXECUTION_READY_EVENT_INVALID")
        if receipt.get("gaps") != [] or receipt.get("admission_state") != "OPEN" or receipt.get("admission_blocked_reason") is not None:
            raise ObservationError("PRE_EXECUTION_OBSERVATION_NOT_READY")
        return deepcopy(receipt)

    def invoke_first_start(
        self,
        callback: Callable[[], Any],
        *,
        readiness_receipt: dict[str, Any] | None = None,
    ) -> Any:
        self.require_admission("FIRST_START")
        if self._first_start_consumed:
            raise ObservationError("FIRST_START_CALLBACK_REPLAYED")
        current_receipt = self.validate_readiness_receipt(self.readiness_receipt())
        receipt = self.validate_readiness_receipt(deepcopy(readiness_receipt or current_receipt))
        if readiness_receipt is not None and canonical_hash(receipt) != canonical_hash(current_receipt):
            raise ObservationError("STALE_OBSERVATION_READINESS_RECEIPT")
        if receipt.get("database") != self.plan["database"]["path"]:
            raise ObservationError("PRE_EXECUTION_TARGET_SUBSTITUTION")
        if receipt.get("task_id") != self.plan["task_id"] or receipt.get("attempt_id") != self.plan["attempt_id"]:
            raise ObservationError("PRE_EXECUTION_TASK_ATTEMPT_SUBSTITUTION")
        if receipt.get("plan_hash") != self.plan["plan_hash"]:
            raise ObservationError("PRE_EXECUTION_PLAN_SUBSTITUTION")
        if (
            self._initial_configuration is None
            or receipt.get("configuration_hash") != self._initial_configuration.get("configuration_hash")
        ):
            raise ObservationError("PRE_EXECUTION_CONFIGURATION_SUBSTITUTION")
        baseline = next(
            (item for item in self._snapshots if item.get("label") == "BASELINE_BEFORE_FIRST_START"),
            None,
        )
        if (
            baseline is None
            or receipt.get("baseline_snapshot_id") != baseline.get("snapshot_id")
            or receipt.get("baseline_snapshot_hash") != canonical_hash(baseline)
        ):
            raise ObservationError("PRE_EXECUTION_BASELINE_SUBSTITUTION")
        self._append_event("FIRST_START_CALLBACK_AUTHORIZED", readiness_hash=canonical_hash(receipt))
        self._first_start_consumed = True
        try:
            result = callback()
        except BaseException as exc:
            exception = f"{type(exc).__name__}:{exc}"
            self._latch_gap("FIRST_START_CALLBACK_OUTCOME_UNCERTAIN", exception)
            self._append_event(
                "FIRST_START_CALLBACK_FAILED",
                exception=exception,
                side_effect_status="UNKNOWN_CALLBACK_RAISED_AFTER_AUTHORIZATION",
            )
            raise
        self._first_start_callback = True
        self._append_event("FIRST_START_CALLBACK_RETURNED", callback_kind="INJECTED_BOUNDED_CALLBACK")
        return result

    def begin_writer_transaction(self, transaction_id: str, *, operation_id: str, interface: str) -> None:
        self.require_admission("WRITER_TRANSACTION")
        if self._current_transaction_id is not None:
            raise ObservationError("NESTED_OBSERVATION_TRANSACTION")
        if not transaction_id or any(item.get("transaction_id") == transaction_id for item in self._transactions):
            raise ObservationError("TRANSACTION_ID_INVALID_OR_REPLAYED")
        self._current_transaction_id = transaction_id
        try:
            start_clock = self._clock(f"TRANSACTION_START:{transaction_id}")
        except BaseException:
            self._current_transaction_id = None
            raise
        row = {
            "sequence": len(self._transactions) + 1,
            "transaction_id": transaction_id,
            "operation_id": operation_id,
            "interface": interface,
            "state": "STARTED",
            "clock": start_clock,
        }
        row["receipt_hash"] = canonical_hash(row)
        self._transactions.append(row)
        try:
            _append_jsonl_fsync(self.output / "transaction_attempts.jsonl", row)
        except BaseException as exc:
            self._latch_gap("TRANSACTION_JOURNAL_PERSIST_FAILED", f"{type(exc).__name__}:{exc}")
            self._current_transaction_id = None
            raise ObservationError(
                "TRANSACTION_JOURNAL_PERSIST_FAILED",
                {"transaction_id": transaction_id, "exception": f"{type(exc).__name__}:{exc}"},
            ) from exc

    def finish_writer_transaction(self, transaction_id: str, outcome: str, *, reason: str | None = None) -> None:
        if transaction_id != self._current_transaction_id:
            raise ObservationError("TRANSACTION_CONTEXT_MISMATCH")
        if outcome not in {"COMMITTED", "ROLLED_BACK"}:
            raise ObservationError("TRANSACTION_OUTCOME_INVALID")
        if self.broker.db.in_transaction:
            raise ObservationError("TRANSACTION_STILL_OPEN_AT_RECEIPT")
        row = {
            "sequence": len(self._transactions) + 1,
            "transaction_id": transaction_id,
            "state": outcome,
            "reason": reason,
            "clock": self._clock(f"TRANSACTION_END:{transaction_id}:{outcome}"),
        }
        row["receipt_hash"] = canonical_hash(row)
        self._transactions.append(row)
        try:
            _append_jsonl_fsync(self.output / "transaction_attempts.jsonl", row)
        except BaseException as exc:
            self._latch_gap("TRANSACTION_JOURNAL_PERSIST_FAILED", f"{type(exc).__name__}:{exc}")
            raise ObservationError(
                "TRANSACTION_JOURNAL_PERSIST_FAILED",
                {"transaction_id": transaction_id, "exception": f"{type(exc).__name__}:{exc}"},
            ) from exc
        finally:
            self._current_transaction_id = None

    def begin_phase(self, name: str) -> dict[str, Any]:
        self.require_admission("PHASE_BEGIN")
        if name in self._phases:
            raise ObservationError("PHASE_REPLAYED", {"phase": name})
        open_phase = next((phase_name for phase_name, phase in self._phases.items() if phase.get("status") == "OPEN"), None)
        if open_phase is not None:
            raise ObservationError("PHASE_OVERLAP_FORBIDDEN", {"open_phase": open_phase, "requested_phase": name})
        inventory = self.plan["phase_inventory"]
        expected_name = inventory[len(self._phases)] if len(self._phases) < len(inventory) else None
        if name not in inventory or name != expected_name:
            raise ObservationError(
                "PHASE_NOT_DECLARED_OR_OUT_OF_ORDER",
                {"phase": name, "expected_phase": expected_name, "phase_inventory": deepcopy(inventory)},
            )
        if not self._first_start_callback:
            raise ObservationError("PHASE_BEFORE_FIRST_START_BARRIER")
        snapshot = self.snapshot(f"{name}_BEGIN")
        phase_order = len(self._phases) + 1
        phase_id = f"phase:{self.plan['attempt_id']}:{phase_order}:{name}"
        phase = {
            "name": name,
            "phase_id": phase_id,
            "phase_order": phase_order,
            "binding_version": PHASE_BINDING_SCHEMA,
            "status": "OPEN",
            "begin_snapshot_id": snapshot["snapshot_id"],
            "begin_snapshot": deepcopy(snapshot),
            "begin_snapshot_hash": canonical_hash(snapshot),
            "start_audit_seq": snapshot["audit_seq_max"],
            "window_start_clock": deepcopy(snapshot["read_transaction"]["begin_clock"]),
        }
        self._phases[name] = phase
        event = self._append_event(
            "PHASE_BEGIN",
            task_id=self.plan["task_id"],
            attempt_id=self.plan["attempt_id"],
            phase=name,
            phase_id=phase_id,
            phase_order=phase_order,
            snapshot_id=snapshot["snapshot_id"],
            snapshot_hash=canonical_hash(snapshot),
            snapshot_audit_seq=snapshot["audit_seq_max"],
            snapshot_read_begin_clock_id=snapshot["read_transaction"]["begin_clock"]["pair_id"],
            snapshot_read_end_clock_id=snapshot["read_transaction"]["end_clock"]["pair_id"],
            window_clock_pair_id=phase["window_start_clock"]["pair_id"],
        )
        phase["begin_event_ref"] = {"sequence": event["sequence"], "event_hash": event["event_hash"]}
        return snapshot

    def end_phase(self, name: str) -> dict[str, Any]:
        phase = self._phases.get(name)
        if not phase or phase.get("status") != "OPEN":
            raise ObservationError("PHASE_NOT_OPEN", {"phase": name})
        snapshot = self.snapshot(f"{name}_END")
        phase.update({
            "status": "CLOSED",
            "end_snapshot_id": snapshot["snapshot_id"],
            "end_snapshot": deepcopy(snapshot),
            "end_snapshot_hash": canonical_hash(snapshot),
            "end_audit_seq": snapshot["audit_seq_max"],
            "window_end_clock": deepcopy(snapshot["read_transaction"]["end_clock"]),
        })
        event = self._append_event(
            "PHASE_END",
            task_id=self.plan["task_id"],
            attempt_id=self.plan["attempt_id"],
            phase=name,
            phase_id=phase["phase_id"],
            phase_order=phase["phase_order"],
            snapshot_id=snapshot["snapshot_id"],
            snapshot_hash=canonical_hash(snapshot),
            snapshot_audit_seq=snapshot["audit_seq_max"],
            snapshot_read_begin_clock_id=snapshot["read_transaction"]["begin_clock"]["pair_id"],
            snapshot_read_end_clock_id=snapshot["read_transaction"]["end_clock"]["pair_id"],
            window_clock_pair_id=phase["window_end_clock"]["pair_id"],
        )
        phase["end_event_ref"] = {"sequence": event["sequence"], "event_hash": event["event_hash"]}
        return snapshot

    def mark_owned_exit(self, *, synthetic: bool, binding: dict[str, Any]) -> None:
        if self._owned_exit:
            raise ObservationError("OWNED_EXIT_REPLAYED")
        self._owned_exit = True
        self._append_event(
            "OWNED_EXIT_OBSERVED" if not synthetic else "SYNTHETIC_OWNED_EXIT_CALLBACK",
            evidence_class="SYNTHETIC_CALLBACK_NOT_OS_EVIDENCE" if synthetic else "TRUSTED_DIRECT_PARENT_WAIT",
            binding=deepcopy(binding),
        )

    def note_gap(self, code: str, detail: str) -> None:
        self._latch_gap(code, detail)
        try:
            self._append_event("CAPTURE_GAP_RECORDED", code=code, detail=detail)
        except BaseException as exc:
            self._latch_gap("CAPTURE_GAP_RECORD_PERSISTENCE_FAILED", f"{type(exc).__name__}:{exc}")
            raise

    def finalize(self) -> dict[str, Any]:
        if self._finalized:
            raise ObservationError("OBSERVATION_ALREADY_FINALIZED")
        if self._current_transaction_id is not None or self.broker.db.in_transaction:
            self._latch_gap("OPEN_TRANSACTION_AT_END", str(self._current_transaction_id))
        if not self._owned_exit:
            self._latch_gap("OWNED_EXIT_NOT_OBSERVED", "collector cannot close before the declared owned-exit boundary")
        for name, phase in self._phases.items():
            if phase.get("status") != "CLOSED":
                self._latch_gap("PHASE_END_MISSING", name)
        for name in self.plan["phase_inventory"]:
            if name not in self._phases:
                self._latch_gap("PLANNED_PHASE_MISSING", name)
        final_snapshot = self.snapshot("FINAL_AFTER_OWNED_EXIT")
        final_configuration = self.configuration_snapshot()
        if self._initial_configuration is None or final_configuration["configuration_hash"] != self._initial_configuration["configuration_hash"]:
            self._latch_gap("INSTRUMENT_CONFIGURATION_CHANGED", "initial/final configuration hash mismatch")
        end = self._append_event("OBSERVATION_END", final_snapshot_id=final_snapshot["snapshot_id"])
        self._finalized = True
        evidence = self.export_evidence()
        evidence["finalization"] = {
            "status": "COMPLETE" if not self._gaps else "INCOMPLETE",
            "owned_exit_observed": self._owned_exit,
            "final_snapshot_id": final_snapshot["snapshot_id"],
            "final_configuration": final_configuration,
            "end_event": end,
        }
        write_json(self.output / "OBSERVATION_EVIDENCE.json", evidence)
        return evidence

    def export_evidence(self) -> dict[str, Any]:
        return {
            "schema": EVIDENCE_SCHEMA,
            "task_id": self.plan["task_id"],
            "attempt_id": self.plan["attempt_id"],
            "checkpoint": self.plan["checkpoint"],
            "plan": deepcopy(self.plan),
            "plan_hash": self.plan["plan_hash"],
            "database": str(self.database),
            "configuration_initial": deepcopy(self._initial_configuration),
            "events": deepcopy(self._events),
            "transactions": deepcopy(self._transactions),
            "clock_pairs": deepcopy(self._clock_pairs),
            "snapshots": deepcopy(self._snapshots),
            "phases": deepcopy(self._phases),
            "gaps": deepcopy(self._gaps),
            "first_start_callback_invoked": self._first_start_callback,
            "owned_exit_observed": self._owned_exit,
            "claim_boundary": self.plan["claim_boundary"],
        }


def prepare_prospective_observation(
    *,
    plan: dict[str, Any],
    output: Path,
    clock: Callable[[str], dict[str, Any]] | None = None,
) -> tuple[Broker, ProspectiveObservation]:
    """Create the database and collector in the mandated pre-start order."""
    _validate_plan(plan)
    output = output.resolve()
    output.mkdir(parents=True, exist_ok=False)
    write_json(output / "OBSERVATION_PLAN.json", plan)
    database = Path(plan["database"]["path"]).resolve()
    if database.exists():
        raise ObservationError("DATABASE_CREATE_ONLY_COLLISION", {"database": str(database)})
    broker = Broker(database)
    try:
        collector = ProspectiveObservation(broker, plan, output, clock=clock)
    except BaseException:
        broker.close()
        raise
    return broker, collector


def _snapshot_by_id(evidence: dict[str, Any], snapshot_id: str | None) -> dict[str, Any] | None:
    return next((item for item in evidence.get("snapshots", []) if item.get("snapshot_id") == snapshot_id), None)


def _int(value: Any) -> int | None:
    try:
        return int(value)
    except (TypeError, ValueError):
        return None


def _validate_clock_pairs(evidence: dict[str, Any], issues: list[dict[str, Any]]) -> None:
    pairs = evidence.get("clock_pairs")
    if not isinstance(pairs, list) or not pairs:
        issues.append({"code": "CLOCK_CORRELATION_UNKNOWN", "classification": "INCOMPLETE"})
        return
    max_residual = int((evidence.get("plan") or {}).get("limits", {}).get("max_clock_residual_ns", DEFAULT_MAX_CLOCK_RESIDUAL_NS))
    previous: tuple[int, int, str, str] | None = None
    for expected_seq, pair in enumerate(pairs, start=1):
        before = _int(pair.get("monotonic_before_ns"))
        after = _int(pair.get("monotonic_after_ns"))
        utc_ns = _int(pair.get("utc_ns"))
        mono_domain, utc_domain = pair.get("monotonic_domain"), pair.get("utc_domain")
        if (
            pair.get("pair_seq") != expected_seq
            or before is None
            or after is None
            or utc_ns is None
            or before > after
            or not mono_domain
            or not utc_domain
        ):
            issues.append({"code": "CLOCK_PAIR_INVALID", "classification": "INCOMPLETE", "pair_id": pair.get("pair_id")})
            continue
        if pair.get("utc") != _rfc3339_ns(utc_ns):
            issues.append({"code": "CLOCK_UTC_STRING_MISMATCH", "classification": "INCOMPLETE", "pair_id": pair.get("pair_id")})
        midpoint = (before + after) // 2
        if previous is not None:
            prior_mid, prior_utc, prior_mono_domain, prior_utc_domain = previous
            if mono_domain != prior_mono_domain or utc_domain != prior_utc_domain:
                issues.append({"code": "CLOCK_DOMAIN_CHANGED_OR_UNCORRELATED", "classification": "INCOMPLETE"})
            residual = abs((utc_ns - prior_utc) - (midpoint - prior_mid))
            if residual > max_residual:
                issues.append({"code": "UTC_MONOTONIC_CORRELATION_JUMP", "classification": "INCOMPLETE", "residual_ns": str(residual)})
        previous = (midpoint, utc_ns, str(mono_domain), str(utc_domain))


def review_observation_evidence(evidence: dict[str, Any]) -> dict[str, Any]:
    """Independently review frozen observations without importing receiver or Broker policy."""
    issues: list[dict[str, Any]] = []
    if evidence.get("schema") != EVIDENCE_SCHEMA:
        issues.append({"code": "EVIDENCE_SCHEMA_MISMATCH", "classification": "INCOMPLETE"})
    plan = evidence.get("plan") if isinstance(evidence.get("plan"), dict) else {}
    body = {key: value for key, value in plan.items() if key != "plan_hash"}
    plan_binding_valid = bool(
        plan
        and plan.get("plan_hash") == canonical_hash(body)
        and evidence.get("plan_hash") == plan.get("plan_hash")
    )
    if not plan_binding_valid:
        issues.append({"code": "PLAN_HASH_OR_BINDING_INVALID", "classification": "FAIL"})
    if (
        evidence.get("task_id") != plan.get("task_id")
        or evidence.get("attempt_id") != plan.get("attempt_id")
        or evidence.get("checkpoint") != plan.get("checkpoint")
    ):
        issues.append({"code": "TASK_ATTEMPT_CHECKPOINT_BINDING_MISMATCH", "classification": "FAIL"})
    intended = plan.get("expected_operation_intent") if isinstance(plan.get("expected_operation_intent"), dict) else {}
    if intended.get("origin") != "TRUSTED_OPERATION_CONTEXT_PRE_OBSERVATION" or not isinstance(intended.get("scope"), dict):
        issues.append({"code": "INDEPENDENT_OPERATION_INTENT_MISSING", "classification": "FAIL"})
    if evidence.get("database") != (plan.get("database") or {}).get("path"):
        issues.append({"code": "TARGET_DATABASE_SUBSTITUTED", "classification": "FAIL"})
    initial = evidence.get("configuration_initial") or {}
    final = (evidence.get("finalization") or {}).get("final_configuration") or {}
    if initial.get("database") != evidence.get("database") or initial.get("plan_hash") != evidence.get("plan_hash"):
        issues.append({"code": "CONFIGURATION_TARGET_BINDING_INVALID", "classification": "FAIL"})
    if not final or final.get("configuration_hash") != initial.get("configuration_hash"):
        issues.append({"code": "INSTRUMENT_CONFIGURATION_NOT_STABLE", "classification": "INCOMPLETE"})

    events = evidence.get("events") if isinstance(evidence.get("events"), list) else []
    previous_hash = None
    kinds: dict[str, int] = {}
    events_by_kind: dict[str, list[dict[str, Any]]] = {}
    for index, event in enumerate(events, start=1):
        supplied_hash = event.get("event_hash")
        body_event = {key: value for key, value in event.items() if key != "event_hash"}
        if event.get("sequence") != index or event.get("previous_event_hash") != previous_hash or supplied_hash != canonical_hash(body_event):
            issues.append({"code": "EVENT_JOURNAL_CHAIN_GAP", "classification": "INCOMPLETE", "sequence": index})
        previous_hash = supplied_hash
        kind = str(event.get("kind", ""))
        kinds.setdefault(kind, event.get("sequence", index))
        events_by_kind.setdefault(kind, []).append(event)
    required_order = (
        "DATABASE_AND_TABLES_CREATED", "CAPTURE_HOOKS_INSTALLED", "INDEPENDENT_BASELINE_READBACK",
        "SCOPE_CLOCK_CONFIGURATION_BOUND", "OBSERVATION_READY", "FIRST_START_CALLBACK_AUTHORIZED",
    )
    if any(name not in kinds for name in required_order):
        issues.append({"code": "PRE_EXECUTION_BARRIER_EVIDENCE_MISSING", "classification": "INCOMPLETE"})
    elif [kinds[name] for name in required_order] != sorted(kinds[name] for name in required_order):
        issues.append({"code": "PRE_EXECUTION_BARRIER_ORDER_INVALID", "classification": "FAIL"})
    if not evidence.get("first_start_callback_invoked"):
        issues.append({"code": "FIRST_START_CALLBACK_NOT_OBSERVED", "classification": "INCOMPLETE"})
    if not evidence.get("owned_exit_observed"):
        issues.append({"code": "OWNED_EXIT_BOUNDARY_MISSING", "classification": "INCOMPLETE"})
    if kinds.get("OBSERVATION_END", 0) <= kinds.get("SYNTHETIC_OWNED_EXIT_CALLBACK", kinds.get("OWNED_EXIT_OBSERVED", 0)):
        issues.append({"code": "COLLECTOR_ENDED_BEFORE_OWNED_EXIT", "classification": "INCOMPLETE"})
    if evidence.get("gaps"):
        for gap in evidence["gaps"]:
            issues.append({"code": f"CAPTURE_GAP:{gap.get('code')}", "classification": "INCOMPLETE", "detail": gap.get("detail")})

    _validate_clock_pairs(evidence, issues)
    clock_pair_map = {
        str(pair.get("pair_id")): pair
        for pair in evidence.get("clock_pairs", [])
        if isinstance(pair, dict) and pair.get("pair_id")
    }

    def clock_object_resolves(value: Any) -> bool:
        return (
            isinstance(value, dict)
            and value.get("pair_id") in clock_pair_map
            and canonical_hash(value) == canonical_hash(clock_pair_map[value["pair_id"]])
        )

    for event in events:
        if event.get("clock_pair_id") not in clock_pair_map:
            issues.append({"code": "EVENT_CLOCK_PAIR_UNRESOLVED", "classification": "INCOMPLETE", "sequence": event.get("sequence")})
    snapshots = evidence.get("snapshots") if isinstance(evidence.get("snapshots"), list) else []
    for snapshot in snapshots:
        if snapshot.get("database") != evidence.get("database"):
            issues.append({"code": "SNAPSHOT_TARGET_DATABASE_MISMATCH", "classification": "FAIL"})
        for surface in SURFACES:
            table = (snapshot.get("tables") or {}).get(surface) or {}
            rows = table.get("rows")
            if not isinstance(rows, list) or table.get("row_count") != len(rows) or table.get("canonical_hash") != canonical_hash(rows):
                issues.append({"code": f"SNAPSHOT_{surface.upper()}_HASH_OR_COUNT_INVALID", "classification": "INCOMPLETE"})
        read_transaction = snapshot.get("read_transaction") or {}
        if not clock_object_resolves(read_transaction.get("begin_clock")) or not clock_object_resolves(read_transaction.get("end_clock")):
            issues.append({"code": "SNAPSHOT_CLOCK_PAIR_UNRESOLVED", "classification": "INCOMPLETE", "snapshot_id": snapshot.get("snapshot_id")})
    baseline = next((item for item in snapshots if item.get("label") == "BASELINE_BEFORE_FIRST_START"), None)
    if baseline is None:
        issues.append({"code": "BASELINE_SNAPSHOT_MISSING", "classification": "INCOMPLETE"})

    final_snapshot = _snapshot_by_id(evidence, (evidence.get("finalization") or {}).get("final_snapshot_id"))
    audit_rows = [] if final_snapshot is None else final_snapshot.get("audit_rows", [])
    if final_snapshot is None:
        issues.append({"code": "FINAL_READBACK_MISSING", "classification": "INCOMPLETE"})
    else:
        seqs = [item.get("audit_seq") for item in audit_rows]
        if seqs != list(range(1, int(final_snapshot.get("audit_seq_max", 0)) + 1)):
            issues.append({"code": "COMMITTED_AUDIT_SEQUENCE_GAP", "classification": "INCOMPLETE"})
        if final_snapshot.get("audit_chain_hash") != canonical_hash(audit_rows):
            issues.append({"code": "COMMITTED_AUDIT_HASH_MISMATCH", "classification": "INCOMPLETE"})

    transactions = evidence.get("transactions") if isinstance(evidence.get("transactions"), list) else []
    states: dict[str, list[str]] = {}
    for row in transactions:
        supplied_hash = row.get("receipt_hash")
        receipt_body = {key: value for key, value in row.items() if key != "receipt_hash"}
        if supplied_hash != canonical_hash(receipt_body):
            issues.append({"code": "TRANSACTION_RECEIPT_HASH_MISMATCH", "classification": "INCOMPLETE", "transaction_id": row.get("transaction_id")})
        if not clock_object_resolves(row.get("clock")):
            issues.append({"code": "TRANSACTION_CLOCK_PAIR_UNRESOLVED", "classification": "INCOMPLETE", "transaction_id": row.get("transaction_id")})
        states.setdefault(str(row.get("transaction_id")), []).append(str(row.get("state")))
    for transaction_id, transaction_states in states.items():
        if transaction_states[0] != "STARTED" or transaction_states[-1] not in {"COMMITTED", "ROLLED_BACK"}:
            issues.append({"code": "TRANSACTION_RECEIPT_INCOMPLETE", "classification": "INCOMPLETE", "transaction_id": transaction_id})
    for row in audit_rows:
        if not clock_object_resolves(row.get("event_clock")):
            issues.append({"code": "AUDIT_CLOCK_PAIR_UNRESOLVED", "classification": "INCOMPLETE", "audit_seq": row.get("audit_seq")})
        if states.get(str(row.get("transaction_id")), [])[-1:] != ["COMMITTED"]:
            issues.append({"code": "AUDIT_EVENT_WITHOUT_COMMIT_RECEIPT", "classification": "INCOMPLETE", "audit_seq": row.get("audit_seq")})
    for transaction_id, transaction_states in states.items():
        if transaction_states[-1:] == ["ROLLED_BACK"] and any(row.get("transaction_id") == transaction_id for row in audit_rows):
            issues.append({"code": "ROLLED_BACK_DML_CLASSIFIED_COMMITTED", "classification": "FAIL", "transaction_id": transaction_id})
    if intended.get("expected_outcome") == "ALLOW_EXACTLY_ONE":
        expected_operation = (intended.get("scope") or {}).get("operation_id")
        new_effect_rows = [
            row.get("new_row") for row in audit_rows
            if row.get("surface_id") == "effects" and row.get("dml_kind") == "INSERT"
        ]
        if len(new_effect_rows) != 1 or (new_effect_rows[0] or {}).get("operation_id") != expected_operation:
            issues.append({"code": "ACTUAL_EFFECT_NOT_BOUND_TO_INDEPENDENT_INTENT", "classification": "FAIL"})

    phase_results: dict[str, Any] = {}
    phases = evidence.get("phases") if isinstance(evidence.get("phases"), dict) else {}
    snapshot_ids = [str(item.get("snapshot_id")) for item in snapshots if item.get("snapshot_id")]
    snapshot_map = {
        str(item.get("snapshot_id")): item
        for item in snapshots
        if isinstance(item, dict) and item.get("snapshot_id")
    }
    if len(snapshot_ids) != len(set(snapshot_ids)):
        issues.append({"code": "SNAPSHOT_ID_DUPLICATED", "classification": "INCOMPLETE"})

    raw_phase_begin_events = events_by_kind.get("PHASE_BEGIN", [])
    raw_phase_end_events = events_by_kind.get("PHASE_END", [])
    planned_inventory = plan.get("phase_inventory")
    planned_names_for_event_validation = (
        set(planned_inventory)
        if isinstance(planned_inventory, list)
        and all(_nonempty_string(item) for item in planned_inventory)
        else set()
    )
    event_positions = {id(event): index for index, event in enumerate(events, start=1)}
    valid_phase_begin_events: list[dict[str, Any]] = []
    valid_phase_end_events: list[dict[str, Any]] = []
    for event in raw_phase_begin_events + raw_phase_end_events:
        position = event_positions.get(id(event), 0)
        missing_or_malformed: list[str] = []
        mismatched: list[str] = []
        for field in (
            "phase", "task_id", "attempt_id", "phase_id", "snapshot_id",
            "snapshot_hash", "snapshot_read_begin_clock_id",
            "snapshot_read_end_clock_id", "window_clock_pair_id",
            "event_hash", "clock_pair_id",
        ):
            if not _nonempty_string(event.get(field)):
                missing_or_malformed.append(field)
        if not _plain_int(event.get("phase_order"), minimum=1):
            missing_or_malformed.append("phase_order")
        if not _plain_int(event.get("snapshot_audit_seq"), minimum=0):
            missing_or_malformed.append("snapshot_audit_seq")
        if not _plain_int(event.get("sequence"), minimum=1):
            missing_or_malformed.append("sequence")
        if _nonempty_string(event.get("snapshot_hash")) and not _hash_string(event.get("snapshot_hash")):
            missing_or_malformed.append("snapshot_hash")
        if _nonempty_string(event.get("event_hash")) and not _hash_string(event.get("event_hash")):
            missing_or_malformed.append("event_hash")
        if _nonempty_string(event.get("task_id")) and event.get("task_id") != evidence.get("task_id"):
            mismatched.append("task_id")
        if _nonempty_string(event.get("attempt_id")) and event.get("attempt_id") != evidence.get("attempt_id"):
            mismatched.append("attempt_id")
        if event.get("clock_pair_id") not in clock_pair_map:
            mismatched.append("clock_pair_id")
        for field in (
            "snapshot_read_begin_clock_id",
            "snapshot_read_end_clock_id",
            "window_clock_pair_id",
        ):
            if _nonempty_string(event.get(field)) and event.get(field) not in clock_pair_map:
                mismatched.append(field)
        snapshot = snapshot_map.get(str(event.get("snapshot_id")))
        if _nonempty_string(event.get("snapshot_id")) and snapshot is None:
            mismatched.append("snapshot_id")
        if snapshot is not None:
            read_transaction = snapshot.get("read_transaction") or {}
            endpoint_clock = (
                read_transaction.get("begin_clock")
                if event.get("kind") == "PHASE_BEGIN"
                else read_transaction.get("end_clock")
            ) or {}
            expected_snapshot_values = {
                "snapshot_hash": canonical_hash(snapshot),
                "snapshot_audit_seq": snapshot.get("audit_seq_max"),
                "snapshot_read_begin_clock_id": (read_transaction.get("begin_clock") or {}).get("pair_id"),
                "snapshot_read_end_clock_id": (read_transaction.get("end_clock") or {}).get("pair_id"),
                "window_clock_pair_id": endpoint_clock.get("pair_id"),
            }
            for field, expected in expected_snapshot_values.items():
                if field not in missing_or_malformed and event.get(field) != expected:
                    mismatched.append(field)
        if position:
            expected_previous = events[position - 2].get("event_hash") if position > 1 else None
            event_body = {key: value for key, value in event.items() if key != "event_hash"}
            if (
                event.get("sequence") != position
                or event.get("previous_event_hash") != expected_previous
                or event.get("event_hash") != canonical_hash(event_body)
            ):
                mismatched.append("event_chain")
        else:
            mismatched.append("event_position")
        if missing_or_malformed or mismatched:
            issues.append({
                "code": "PHASE_JOURNAL_EVENT_MALFORMED",
                "classification": "FAIL" if mismatched else "INCOMPLETE",
                "phase": event.get("phase"),
                "kind": event.get("kind"),
                "sequence": event.get("sequence"),
                "missing_or_malformed_fields": sorted(set(missing_or_malformed)),
                "mismatched_bindings": sorted(set(mismatched)),
            })
            continue
        phase_name = str(event["phase"])
        if planned_names_for_event_validation and phase_name not in planned_names_for_event_validation:
            issues.append({
                "code": "PHASE_JOURNAL_EVENT_OUTSIDE_FROZEN_INVENTORY",
                "classification": "FAIL",
                "phase": phase_name,
                "kind": event.get("kind"),
                "sequence": event.get("sequence"),
            })
        if event.get("kind") == "PHASE_BEGIN":
            valid_phase_begin_events.append(event)
        else:
            valid_phase_end_events.append(event)
    phase_begin_events = valid_phase_begin_events
    phase_end_events = valid_phase_end_events
    journal_phase_names = {
        str(event.get("phase"))
        for event in phase_begin_events + phase_end_events
    }
    descriptor_names = {str(name) for name in phases}
    if plan.get("phase_binding_schema") != PHASE_BINDING_SCHEMA:
        issues.append({"code": "PHASE_BINDING_SCHEMA_MISMATCH", "classification": "INCOMPLETE"})
    if isinstance(planned_inventory, list):
        if (
            not planned_inventory
            or len(planned_inventory) != len(set(planned_inventory))
            or any(not isinstance(name, str) or not name for name in planned_inventory)
        ):
            issues.append({"code": "PHASE_INVENTORY_INVALID", "classification": "INCOMPLETE"})
            planned_phase_names: set[str] = set()
        else:
            planned_phase_names = set(planned_inventory)
            missing_descriptors = planned_phase_names - descriptor_names
            unexpected_descriptors = descriptor_names - planned_phase_names
            for name in sorted(missing_descriptors):
                issues.append({
                    "code": "PHASE_DESCRIPTOR_MISSING_FROM_FROZEN_INVENTORY",
                    "classification": "INCOMPLETE",
                    "phase": name,
                })
            for name in sorted(unexpected_descriptors):
                issues.append({
                    "code": "PHASE_DESCRIPTOR_NOT_IN_FROZEN_INVENTORY",
                    "classification": "FAIL",
                    "phase": name,
                })
    else:
        # R1.6K evidence predates the explicit inventory field. Its complete event
        # journal is still authoritative for detecting a removed descriptor.
        planned_phase_names = set(journal_phase_names)

    for name in sorted(journal_phase_names - descriptor_names):
        issues.append({
            "code": "PHASE_DESCRIPTOR_MISSING_FOR_JOURNAL_EVENTS",
            "classification": "INCOMPLETE",
            "phase": name,
        })
    for name in sorted(descriptor_names - journal_phase_names):
        issues.append({
            "code": "PHASE_JOURNAL_EVENTS_MISSING_FOR_DESCRIPTOR",
            "classification": "INCOMPLETE",
            "phase": name,
        })
    journal_order = (
        list(planned_inventory)
        if isinstance(planned_inventory, list) and planned_inventory
        else list(dict.fromkeys(
            str(event.get("phase"))
            for event in phase_begin_events
            if isinstance(event.get("phase"), str) and event.get("phase")
        ))
    )
    previous_phase_end = 0
    for name in journal_order:
        begin_for_name = [event for event in phase_begin_events if event.get("phase") == name]
        end_for_name = [event for event in phase_end_events if event.get("phase") == name]
        if len(begin_for_name) == 1 and len(end_for_name) == 1:
            begin_sequence = int(begin_for_name[0].get("sequence", 0))
            end_sequence = int(end_for_name[0].get("sequence", 0))
            if begin_sequence <= previous_phase_end or end_sequence <= begin_sequence:
                issues.append({
                    "code": "PHASE_JOURNAL_ORDER_OR_OVERLAP_INVALID",
                    "classification": "FAIL",
                    "phase": name,
                    "previous_phase_end_sequence": previous_phase_end,
                    "begin_sequence": begin_sequence,
                    "end_sequence": end_sequence,
                })
            previous_phase_end = max(previous_phase_end, end_sequence)

    covered_audit_sequences: dict[int, str] = {}
    for name, phase in phases.items():
        phase_issues: list[dict[str, Any]] = [
            deepcopy(row) for row in issues if row.get("phase") == name
        ]

        def add_phase_issue(code: str, classification: str, **details: Any) -> None:
            row = {"code": code, "classification": classification, "phase": name, **details}
            issues.append(row)
            phase_issues.append(row)

        v2_shape_issues = (
            _phase_v2_descriptor_shape_issues(name, phase)
            if plan.get("phase_binding_schema") == PHASE_BINDING_SCHEMA
            else []
        )
        for row in v2_shape_issues:
            issues.append(row)
            phase_issues.append(row)
        v2_shape_complete = not any(
            row["code"] in {
                "PHASE_V2_DESCRIPTOR_MALFORMED",
                "PHASE_V2_REQUIRED_FIELD_MISSING",
                "PHASE_V2_REQUIRED_FIELD_TYPE_INVALID",
                "PHASE_BINDING_VERSION_MISMATCH",
            }
            for row in v2_shape_issues
        )

        begin = snapshot_map.get(str(phase.get("begin_snapshot_id")))
        end = snapshot_map.get(str(phase.get("end_snapshot_id")))
        begin_events = [event for event in phase_begin_events if event.get("phase") == name]
        end_events = [event for event in phase_end_events if event.get("phase") == name]
        if phase.get("status") != "CLOSED" or begin is None or end is None:
            add_phase_issue(f"PHASE_{name}_BOUNDARY_INCOMPLETE", "INCOMPLETE")
            phase_results[name] = {
                "status": "INCOMPLETE",
                "binding_status": "INCOMPLETE",
                "binding_issues": deepcopy(phase_issues),
                "committed_event_count": None,
            }
            continue
        if phase.get("name") != name:
            add_phase_issue("PHASE_DESCRIPTOR_NAME_MISMATCH", "FAIL", descriptor_name=phase.get("name"))
        if len(begin_events) != 1 or len(end_events) != 1:
            add_phase_issue(
                "PHASE_EVENT_PAIR_CARDINALITY_INVALID",
                "INCOMPLETE",
                begin_count=len(begin_events),
                end_count=len(end_events),
            )
        begin_event = begin_events[0] if len(begin_events) == 1 else None
        end_event = end_events[0] if len(end_events) == 1 else None
        if begin_event is not None and end_event is not None:
            if int(begin_event.get("sequence", 0)) >= int(end_event.get("sequence", 0)):
                add_phase_issue("PHASE_EVENT_ORDER_INVALID", "FAIL")
            if begin_event.get("snapshot_id") != begin.get("snapshot_id"):
                add_phase_issue("PHASE_BEGIN_EVENT_SNAPSHOT_REF_MISMATCH", "FAIL")
            if end_event.get("snapshot_id") != end.get("snapshot_id"):
                add_phase_issue("PHASE_END_EVENT_SNAPSHOT_REF_MISMATCH", "FAIL")

        for endpoint, resolved in (("begin", begin), ("end", end)):
            embedded = phase.get(f"{endpoint}_snapshot")
            if isinstance(embedded, dict) and embedded and canonical_hash(embedded) != canonical_hash(resolved):
                add_phase_issue(f"PHASE_{endpoint.upper()}_SNAPSHOT_CONTENT_MISMATCH", "FAIL")
            supplied_hash = phase.get(f"{endpoint}_snapshot_hash")
            if _nonempty_string(supplied_hash) and supplied_hash != canonical_hash(resolved):
                add_phase_issue(f"PHASE_{endpoint.upper()}_SNAPSHOT_HASH_MISMATCH", "FAIL")

        start_seq = int(begin.get("audit_seq_max", 0))
        end_seq = int(end.get("audit_seq_max", 0))
        if (
            _plain_int(phase.get("start_audit_seq"), minimum=0)
            and _plain_int(phase.get("end_audit_seq"), minimum=0)
            and (phase.get("start_audit_seq") != start_seq or phase.get("end_audit_seq") != end_seq)
        ):
            add_phase_issue(
                "PHASE_AUDIT_BOUNDARY_MISMATCH",
                "FAIL",
                expected_start=start_seq,
                expected_end=end_seq,
            )
        if start_seq > end_seq:
            add_phase_issue("PHASE_AUDIT_BOUNDARY_ORDER_INVALID", "FAIL")
        phase_events = [row for row in audit_rows if start_seq < int(row.get("audit_seq", 0)) <= end_seq]
        for row in phase_events:
            sequence = int(row.get("audit_seq", 0))
            if sequence in covered_audit_sequences:
                add_phase_issue(
                    "PHASE_AUDIT_RANGE_OVERLAP",
                    "FAIL",
                    audit_seq=sequence,
                    other_phase=covered_audit_sequences[sequence],
                )
            else:
                covered_audit_sequences[sequence] = name

        start_clock = phase.get("window_start_clock") if isinstance(phase.get("window_start_clock"), dict) else {}
        end_clock = phase.get("window_end_clock") if isinstance(phase.get("window_end_clock"), dict) else {}
        required_start_clock = (begin.get("read_transaction") or {}).get("begin_clock")
        required_end_clock = (end.get("read_transaction") or {}).get("end_clock")
        if start_clock and (
            not clock_object_resolves(start_clock)
            or not isinstance(required_start_clock, dict)
            or canonical_hash(start_clock) != canonical_hash(required_start_clock)
        ):
            add_phase_issue("PHASE_WINDOW_START_SNAPSHOT_CLOCK_MISMATCH", "FAIL")
        if end_clock and (
            not clock_object_resolves(end_clock)
            or not isinstance(required_end_clock, dict)
            or canonical_hash(end_clock) != canonical_hash(required_end_clock)
        ):
            add_phase_issue("PHASE_WINDOW_END_SNAPSHOT_CLOCK_MISMATCH", "FAIL")

        if phase.get("binding_version") == PHASE_BINDING_SCHEMA and v2_shape_complete:
            expected_order = (
                planned_inventory.index(name) + 1
                if isinstance(planned_inventory, list) and name in planned_inventory
                else list(phases).index(name) + 1
            )
            expected_phase_id = f"phase:{evidence.get('attempt_id')}:{expected_order}:{name}"
            if phase.get("phase_order") != expected_order or phase.get("phase_id") != expected_phase_id:
                add_phase_issue("PHASE_ID_OR_ORDER_MISMATCH", "FAIL")
            rich_event_expectations = (
                (
                    "BEGIN",
                    begin_event,
                    begin,
                    phase.get("begin_event_ref"),
                    required_start_clock,
                ),
                (
                    "END",
                    end_event,
                    end,
                    phase.get("end_event_ref"),
                    required_end_clock,
                ),
            )
            for endpoint, event, snapshot, event_ref, window_clock in rich_event_expectations:
                expected_event = {
                    "task_id": evidence.get("task_id"),
                    "attempt_id": evidence.get("attempt_id"),
                    "phase_id": expected_phase_id,
                    "phase_order": expected_order,
                    "snapshot_hash": canonical_hash(snapshot),
                    "snapshot_audit_seq": snapshot.get("audit_seq_max"),
                    "snapshot_read_begin_clock_id": snapshot["read_transaction"]["begin_clock"]["pair_id"],
                    "snapshot_read_end_clock_id": snapshot["read_transaction"]["end_clock"]["pair_id"],
                    "window_clock_pair_id": window_clock.get("pair_id") if isinstance(window_clock, dict) else None,
                }
                if event is None or any(event.get(key) != value for key, value in expected_event.items()):
                    add_phase_issue(f"PHASE_{endpoint}_EVENT_BINDING_MISMATCH", "FAIL")
                if (
                    event is None
                    or not isinstance(event_ref, dict)
                    or event_ref.get("sequence") != event.get("sequence")
                    or event_ref.get("event_hash") != event.get("event_hash")
                ):
                    add_phase_issue(f"PHASE_{endpoint}_EVENT_REF_MISMATCH", "FAIL")

        changed_surfaces = []
        for surface in SURFACES:
            before_table = begin["tables"][surface]
            after_table = end["tables"][surface]
            surface_events = [row for row in phase_events if row.get("surface_id") == surface]
            if before_table["canonical_hash"] != after_table["canonical_hash"] or surface_events:
                changed_surfaces.append(surface)
            if before_table["canonical_hash"] != after_table["canonical_hash"] and not surface_events:
                add_phase_issue(f"{name}_{surface.upper()}_CHANGE_WITHOUT_AUDIT", "INCOMPLETE")
        start_ns = _int(start_clock.get("monotonic_before_ns"))
        end_ns = _int(end_clock.get("monotonic_after_ns"))
        if start_ns is None or end_ns is None or start_ns >= end_ns:
            add_phase_issue(f"{name}_WINDOW_INVALID", "INCOMPLETE")
        first_pair = (evidence.get("clock_pairs") or [{}])[0]
        last_pair = (evidence.get("clock_pairs") or [{}])[-1]
        if start_ns is not None and end_ns is not None:
            if start_ns < (_int(first_pair.get("monotonic_before_ns")) or start_ns) or end_ns > (_int(last_pair.get("monotonic_after_ns")) or end_ns):
                add_phase_issue(f"{name}_WINDOW_EXCEEDS_CAPTURE", "INCOMPLETE")

        binding_classifications = {row["classification"] for row in phase_issues}
        binding_status = (
            "FAIL" if "FAIL" in binding_classifications
            else "INCOMPLETE" if "INCOMPLETE" in binding_classifications
            else "PASS"
        )
        phase_status = (
            "BINDING_INVALID" if binding_status == "FAIL"
            else "INCOMPLETE" if binding_status == "INCOMPLETE"
            else "EFFECT_DETECTED" if phase_events or changed_surfaces
            else "COMPLETE_NO_COMMITTED_CHANGE"
        )
        phase_results[name] = {
            "status": phase_status,
            "binding_status": binding_status,
            "binding_issues": deepcopy(phase_issues),
            "committed_event_count": len(phase_events),
            "committed_events": phase_events,
            "changed_surfaces": changed_surfaces,
            "begin_snapshot_id": begin["snapshot_id"],
            "end_snapshot_id": end["snapshot_id"],
            "window": {
                "start_utc": start_clock.get("utc"),
                "end_utc": end_clock.get("utc"),
                "start_monotonic_ns": start_clock.get("monotonic_before_ns"),
                "end_monotonic_ns": end_clock.get("monotonic_after_ns"),
            },
            "surface_counts": {
                surface: len([row for row in phase_events if row.get("surface_id") == surface]) for surface in SURFACES
            },
        }

    all_audit_sequences = {
        int(row.get("audit_seq", 0)) for row in audit_rows if int(row.get("audit_seq", 0)) > 0
    }
    uncovered_audit_sequences = sorted(all_audit_sequences - set(covered_audit_sequences))
    if uncovered_audit_sequences:
        issues.append({
            "code": "COMMITTED_AUDIT_EVENTS_OUTSIDE_DESCRIBED_PHASES",
            "classification": "INCOMPLETE",
            "audit_sequences": uncovered_audit_sequences,
        })

    classifications = {item["classification"] for item in issues}
    if "FAIL" in classifications:
        verdict = "FAIL"
    elif "INCOMPLETE" in classifications:
        verdict = "INCONCLUSIVE"
    elif any(item.get("status") == "EFFECT_DETECTED" for item in phase_results.values()):
        verdict = "OBSERVED_COMMITTED_CHANGE"
    else:
        verdict = "PASS_COMPLETE_WITHIN_DECLARED_SURFACES"
    return {
        "schema": REVIEW_SCHEMA,
        "task_id": evidence.get("task_id"),
        "attempt_id": evidence.get("attempt_id"),
        "reviewed_evidence_hash": canonical_hash(evidence),
        "reviewed_plan_hash": plan.get("plan_hash") if plan_binding_valid else None,
        "verdict": verdict,
        "issues": issues,
        "phase_results": phase_results,
        "phase_inventory": {
            "planned": deepcopy(planned_inventory),
            "described": list(phases),
            "journaled": sorted(journal_phase_names),
        },
        "audit_coverage": {
            "total_committed_events": len(all_audit_sequences),
            "covered_committed_events": len(set(covered_audit_sequences)),
            "uncovered_audit_sequences": uncovered_audit_sequences,
        },
        "committed_audit_event_count": len(audit_rows),
        "rolled_back_attempt_count": sum(1 for states_for_txn in states.values() if states_for_txn[-1:] == ["ROLLED_BACK"]),
        "pre_execution_barrier": "PASS" if not any(item["code"].startswith("PRE_EXECUTION") or item["code"] == "BASELINE_SNAPSHOT_MISSING" for item in issues) else "FAIL",
        "clock_correlation": "PASS_LOCAL_ONLY" if not any("CLOCK" in item["code"] or "UTC_" in item["code"] for item in issues) else "INCOMPLETE",
        "claim_boundary": evidence.get("claim_boundary"),
    }


def build_phase_native_material(
    evidence: dict[str, Any], review: dict[str, Any], phase_name: str
) -> dict[str, Any]:
    """Map one independently reviewed empty phase to the existing closed native evidence shapes."""
    if not isinstance(evidence, dict) or not isinstance(review, dict):
        return {"status": "REFUSED_INCOMPLETE", "reason": "REVIEW_EVIDENCE_BINDING_MISMATCH"}
    recomputed_review = review_observation_evidence(evidence)
    if (
        not _hash_string(review.get("reviewed_evidence_hash"))
        or not _hash_string(review.get("reviewed_plan_hash"))
        or review.get("reviewed_evidence_hash") != canonical_hash(evidence)
        or review.get("reviewed_plan_hash") != evidence.get("plan_hash")
        or canonical_hash(_review_binding_body(review))
        != canonical_hash(_review_binding_body(recomputed_review))
    ):
        return {"status": "REFUSED_INCOMPLETE", "reason": "REVIEW_EVIDENCE_BINDING_MISMATCH"}
    phase_result = (review.get("phase_results") or {}).get(phase_name) or {}
    if phase_result.get("binding_status") != "PASS":
        return {"status": "REFUSED_INCOMPLETE", "reason": "PHASE_BINDING_NOT_VERIFIED"}
    if review.get("verdict") not in {"PASS_COMPLETE_WITHIN_DECLARED_SURFACES", "OBSERVED_COMMITTED_CHANGE"}:
        return {"status": "REFUSED_INCOMPLETE", "reason": "OBSERVATION_REVIEW_NOT_COMPLETE"}
    if phase_result.get("status") != "COMPLETE_NO_COMMITTED_CHANGE":
        return {"status": "REFUSED_EFFECT_OR_GAP", "reason": "PHASE_NOT_EMPTY_AND_COMPLETE"}
    begin = _snapshot_by_id(evidence, phase_result.get("begin_snapshot_id"))
    end = _snapshot_by_id(evidence, phase_result.get("end_snapshot_id"))
    if begin is None or end is None:
        return {"status": "REFUSED_INCOMPLETE", "reason": "PHASE_SNAPSHOT_UNRESOLVED"}
    plan = evidence["plan"]
    window = {"start": phase_result["window"]["start_utc"], "end": phase_result["window"]["end_utc"]}
    suffix = f"{evidence['attempt_id']}:{phase_name.casefold()}"
    collector_id = f"collector:{suffix}"
    event_id = f"event-log:{suffix}"
    clock_id = f"clock-evidence:{suffix}"
    inventory_id = f"scope-inventory:{suffix}"
    route_id = plan["alternate_paths"][0]["path_id"]
    route_evidence_id = f"route-evidence:{suffix}"
    surfaces = []
    for surface in plan["surfaces"]:
        surface_id = surface["surface_id"]
        surfaces.append({
            "surface_id": surface_id,
            "surface_kind": "DATABASE",
            "target_ref": surface["target_ref"],
            "target_coordinate": surface["target_coordinate"],
            "hash_domain": "CANONICAL_STATE_SHA256_V1",
            "before_hash": begin["tables"][surface_id]["canonical_hash"],
            "after_hash": end["tables"][surface_id]["canonical_hash"],
            "external_call_count": phase_result["surface_counts"][surface_id],
            "queue_state": "NOT_APPLICABLE",
            "retry_state": "NOT_APPLICABLE",
            "coverage": "COMPLETE",
        })
    protected = ["synthetic acceptance row", "memory promotion row"]
    effect_scope_ref = f"effect:{plan['expected_operation_intent']['scope']['operation_id']}"
    inventory = {
        "schema_version": "c-non-effect-scope-inventory-0.1",
        "evidence_ids": [inventory_id],
        "effect_scope_ref": effect_scope_ref,
        "effect_target_ref": "synthetic-sink",
        "protected_effects": protected,
        "observation_surface_descriptors": [
            {key: item[key] for key in ("surface_id", "surface_kind", "target_ref", "target_coordinate", "hash_domain")}
            for item in surfaces
        ],
        "alternate_path_ids": [route_id],
    }
    artifacts = {
        "scope_inventory": inventory,
        "route": {
            "schema_version": "c-route-evidence-0.1", "evidence_ids": [route_evidence_id],
            "collector_ref": collector_id, "window": window,
            "path_states": [{"path_id": route_id, "status": "NOT_REACHABLE"}],
        },
        "clock": {
            "schema_version": "c-clock-evidence-0.1", "evidence_ids": [clock_id],
            "clock_kind": "MONOTONIC_WITH_UTC_CORRELATION", "correlation_window": window,
        },
        "collector": {
            "schema_version": "c-collector-evidence-0.1", "evidence_ids": [collector_id],
            "availability": "COMPLETE", "continuous_event_log_ref": event_id,
            "surface_ids": [item["surface_id"] for item in surfaces], "window": window,
        },
        "event_log": {
            "schema_version": "c-non-effect-event-log-0.1", "evidence_ids": [event_id],
            "collector_ref": collector_id, "window": window, "availability": "COMPLETE",
            "surface_observations": surfaces, "events": [],
        },
    }
    created = system_clock_pair(f"NATIVE_MATERIAL_CREATED:{phase_name}")
    return {
        "schema": "CGDR_PROSPECTIVE_NATIVE_MATERIAL_V1",
        "status": "COMPLETE_NO_COMMITTED_CHANGE",
        "phase": phase_name,
        "plan_hash": evidence["plan_hash"],
        "window": window,
        "clock_source_ref": clock_id,
        "collector_ref": collector_id,
        "event_log_ref": event_id,
        "scope_inventory_ref": inventory_id,
        "route_evidence_ref": route_evidence_id,
        "route_id": route_id,
        "effect_scope_ref": effect_scope_ref,
        "effect_target_ref": "synthetic-sink",
        "protected_effects": protected,
        "surfaces": surfaces,
        "artifacts": artifacts,
        "record_created_at_utc": created["utc"],
        "raw_provenance": {
            "begin_snapshot_hash": canonical_hash(begin),
            "end_snapshot_hash": canonical_hash(end),
            "begin_read_clock": begin["read_transaction"]["begin_clock"],
            "end_read_clock": end["read_transaction"]["end_clock"],
            "native_material_created_clock": created,
            "clock_claim": "Local correlation only; raw pairs are outside the closed native clock artifact.",
            "committed_dml_claim": "All committed DML on declared surfaces through the single trusted instrumented connection.",
        },
        "claim_boundary": evidence["claim_boundary"],
    }
