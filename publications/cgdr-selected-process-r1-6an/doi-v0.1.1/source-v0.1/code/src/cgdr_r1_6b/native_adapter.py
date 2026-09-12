from __future__ import annotations

import hashlib
import importlib.metadata
import importlib.util
import platform
import sys
from pathlib import Path
from typing import Any, Callable

from .common import canonical_hash, file_hash, write_json


PINNED_COMMIT = "47fed105d7b1df1df7375aa203a551b0f684c13d"
PINNED_VALIDATOR_BLOB = "c2ba855dad55c5ce6e96d5d38543e7d0a2bebc01"
PINNED_VALIDATOR_BYTES = 162707
PINNED_VALIDATOR_SHA256 = "c1d9278af6848995ce9bcfaf3ecceb9b3f24e04a30a2fe8bedef4784f4a2ec73"
SCHEMA_IDS = {
    "decision_basis_record": "urn:ivan-kotov:c-runtime-integrity:decision-basis-record:0.1.1",
    "memory_reliance_record": "urn:ivan-kotov:c-runtime-integrity:memory-reliance-record:0.1.1",
    "consequence_commit_record": "urn:ivan-kotov:c-runtime-integrity:consequence-commit-record:0.1.1",
    "non_effect_witness_record": "urn:ivan-kotov:c-runtime-integrity:non-effect-witness-record:0.1.1",
}


class NativeInputFactConflict(ValueError):
    def __init__(self, code: str, details: dict[str, Any]):
        super().__init__(code)
        self.code = code
        self.details = details

    def as_dict(self) -> dict[str, Any]:
        return {"code": self.code, "details": self.details}


def _new_rows(before: list[Any], after: list[Any]) -> list[Any]:
    before_hashes = {canonical_hash(row) for row in before}
    return [row for row in after if canonical_hash(row) not in before_hashes]


def derive_native_outcome(phase: dict[str, Any]) -> dict[str, Any]:
    """Derive a native outcome from source, decision, broker result and SQL rows."""
    decision = phase.get("decision") or {}
    broker = phase.get("broker_result") or {}
    before = phase.get("sink_before") or {}
    after = phase.get("sink_after") or {}
    intent = phase.get("operation_intent")
    conflicts: list[str] = []
    if (
        not isinstance(intent, dict)
        or phase.get("operation_intent_hash") != canonical_hash(intent)
        or intent.get("capture_stage") != "PRE_COMMIT"
    ):
        conflicts.append("OPERATION_INTENT_MISSING_OR_INVALID")
    before_effects = before.get("effects") if isinstance(before, dict) else None
    after_effects = after.get("effects") if isinstance(after, dict) else None
    before_promotions = before.get("promotions") if isinstance(before, dict) else None
    after_promotions = after.get("promotions") if isinstance(after, dict) else None
    if not all(isinstance(value, list) for value in (before_effects, after_effects, before_promotions, after_promotions)):
        conflicts.append("SQL_READBACK_SNAPSHOT_MISSING")
        new_effects: list[Any] = []
        effect_delta = promotion_delta = None
    else:
        new_effects = _new_rows(before_effects, after_effects)
        effect_delta = len(after_effects) - len(before_effects)
        promotion_delta = len(after_promotions) - len(before_promotions)
    if broker.get("effect_delta") != effect_delta:
        conflicts.append("BROKER_EFFECT_DELTA_READBACK_MISMATCH")
    if promotion_delta != 0:
        conflicts.append("MEMORY_PROMOTION_OBSERVED")

    gate = decision.get("action_gate")
    broker_result = broker.get("result")
    expected_row = intent.get("expected_effect_row") if isinstance(intent, dict) else None
    if gate == "ALLOW":
        source = phase.get("source") or {}
        if not isinstance(source.get("resolution"), dict):
            conflicts.append("ALLOW_WITHOUT_SOURCE_RESOLUTION")
        if broker_result != "BOUND" or broker.get("binding_revalidated") is not True:
            conflicts.append("ALLOW_NOT_ATOMICALLY_BOUND")
        if not isinstance(intent, dict) or intent.get("effect_expectation") != "EXACTLY_ONE":
            conflicts.append("ALLOW_INTENT_EXPECTATION_MISMATCH")
        if effect_delta != 1 or len(new_effects) != 1:
            conflicts.append("ALLOW_READBACK_NOT_EXACTLY_ONE")
        if not isinstance(expected_row, dict) or new_effects != [expected_row] or phase.get("effect_row") != expected_row:
            conflicts.append("ALLOW_EFFECT_ROW_NOT_INTENDED_ROW")
        commit_outcome, effect_state = "OPEN", "BOUND"
    elif gate == "HOLD":
        if broker_result != "HELD":
            conflicts.append("HOLD_BROKER_STATUS_CONTRADICTION")
        if not isinstance(intent, dict) or intent.get("effect_expectation") != "NO_EFFECT":
            conflicts.append("HOLD_INTENT_EXPECTATION_MISMATCH")
        if effect_delta != 0 or new_effects or phase.get("effect_row") is not None:
            conflicts.append("HOLD_READBACK_CONTAINS_EFFECT")
        commit_outcome, effect_state = "HOLD", "NOT_BOUND"
    elif gate == "DENY":
        if broker_result != "DENIED":
            conflicts.append("DENY_BROKER_STATUS_CONTRADICTION")
        if effect_delta != 0 or new_effects or phase.get("effect_row") is not None:
            conflicts.append("DENY_READBACK_CONTAINS_EFFECT")
        commit_outcome, effect_state = "DENY", "NOT_BOUND"
    else:
        conflicts.append("DECISION_GATE_UNKNOWN")
        commit_outcome, effect_state = "HOLD", "UNRESOLVED"
    if conflicts:
        raise NativeInputFactConflict(
            "INPUT_FACT_CONFLICT",
            {
                "checkpoint_label": phase.get("checkpoint"),
                "decision_gate": gate,
                "broker_result": broker_result,
                "broker_effect_delta": broker.get("effect_delta"),
                "readback_effect_delta": effect_delta,
                "readback_new_effect_count": len(new_effects),
                "promotion_delta": promotion_delta,
                "conflicts": sorted(set(conflicts)),
            },
        )
    return {
        "commit_outcome": commit_outcome,
        "effect_state": effect_state,
        "effect_row": expected_row if effect_state == "BOUND" else None,
        "effect_delta": effect_delta,
        "promotion_delta": promotion_delta,
        "basis": "ACTUAL_SOURCE_DECISION_BROKER_AND_SQL_READBACK",
    }


def dependency_root() -> Path:
    return Path(__file__).resolve().parents[2] / "dependencies" / "Kot141078" / "c-hardening-pack" / PINNED_COMMIT


def load_validator() -> Any:
    path = dependency_root() / "tools" / "validate_runtime_integrity_extension.py"
    actual = hashlib.sha256(path.read_bytes()).hexdigest()
    if path.stat().st_size != PINNED_VALIDATOR_BYTES or actual != PINNED_VALIDATOR_SHA256:
        raise RuntimeError(f"PINNED_VALIDATOR_MISMATCH:bytes={path.stat().st_size}:sha256={actual}")
    spec = importlib.util.spec_from_file_location("cgdr_r1f_pinned_native_validator", path)
    if spec is None or spec.loader is None:
        raise RuntimeError("PINNED_VALIDATOR_IMPORT_FAILED")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def dependency_status() -> dict[str, Any]:
    root = dependency_root()
    packages = {}
    for name in ("jcs", "jsonschema", "referencing", "rfc3339-validator", "typing-extensions", "cryptography"):
        try:
            packages[name] = importlib.metadata.version(name)
        except importlib.metadata.PackageNotFoundError:
            packages[name] = "NOT_INSTALLED"
    validator = root / "tools" / "validate_runtime_integrity_extension.py"
    lock = root / "requirements-runtime-integrity.lock"
    return {
        "repository": "Kot141078/c-hardening-pack", "commit": PINNED_COMMIT,
        "validator_git_blob": PINNED_VALIDATOR_BLOB, "validator_bytes": validator.stat().st_size,
        "validator_sha256": file_hash(validator), "validator_modified": file_hash(validator) != PINNED_VALIDATOR_SHA256,
        "runtime_lock_sha256": file_hash(lock), "interpreter": sys.executable,
        "python": platform.python_version(), "packages": packages,
    }


def _artifact_ref(validator: Any, artifact: dict[str, Any], uri: str | None = None) -> dict[str, str]:
    result = {"artifact_id": artifact["artifact_id"], "version": artifact["version"], "hash": validator.jcs_sha256(artifact)}
    if uri is not None:
        result["uri"] = uri
    return result


def _state_ref(ref_id: str, captured_at: str, value: Any) -> dict[str, str]:
    return {"ref_id": ref_id, "captured_at": captured_at, "hash": canonical_hash(value)}


def _decision(validator: Any, phase: dict[str, Any], grant_ref: dict[str, str]) -> dict[str, Any]:
    timestamp, source = phase["times"]["basis_utc"], phase["source"]
    basis = {
        "captured_at": timestamp, "human_anchor_ref": "synthetic-owner:not-live-authority",
        "policy_refs": [{"artifact_id": source["trusted_policy"]["policy_id"], "version": "1", "hash": canonical_hash(source["trusted_policy"])}],
        "authority_refs": [grant_ref], "permission_grant_ref": grant_ref,
        "grounding_ref": _state_ref(f"source-grounding:{phase['checkpoint']}", timestamp, source),
        "continuity_ref": _state_ref(source["toy_lineage"]["lineage_id"], timestamp, source["toy_lineage"]),
        "l4_ref": _state_ref(f"l4:{phase['checkpoint']}", timestamp, source["l4"]),
        "memory_reliance_refs": [],
        "evidence_refs": [
            {"artifact_id": source["source_id"], "version": "1", "hash": source["source_hash"]},
            {"artifact_id": f"packet:{phase['checkpoint']}", "version": "1", "hash": canonical_hash(phase["packet_projection"])},
            {"artifact_id": f"decision:{phase['checkpoint']}", "version": "1", "hash": canonical_hash(phase["decision"])},
        ],
        "witness_chain_head": canonical_hash({"source": source["source_hash"], "decision": phase["decision"], "checkpoint": phase["checkpoint"]}),
    }
    return {
        "schema_version": "c-decision-basis-record-0.1.1", "record_type": "decision_basis_record",
        "record_id": f"native:{phase['attempt_id']}:decision", "created_at": timestamp, "basis": basis,
        "basis_hash": validator.jcs_sha256(basis), "rule_basis_visibility": "FULL",
        "claim_boundary": "Synthetic regression basis for one local offline checkpoint; it is not live authority or process-conformance evidence.",
    }


def _memory_record(
    validator: Any, phase: dict[str, Any], grant_ref: dict[str, str], task_ref: dict[str, str],
    register_evidence: Callable[[str, dict[str, Any]], None],
) -> dict[str, Any]:
    timestamp, source = phase["times"]["basis_utc"], phase["source"]
    memory_item, memory_id = source["quarantined_memory"], f"memory-item:{phase['checkpoint']}"
    evaluator_refs: dict[str, dict[str, str]] = {}
    artifacts = []
    for label, kind, result in (
        ("freshness", "FRESHNESS", "CURRENT"), ("provenance", "PROVENANCE", "VERIFIED"),
        ("contamination", "CONTAMINATION", "CLEAR"), ("revocation", "REVOCATION", "NOT_REVOKED"),
    ):
        item = {"artifact_id": f"{label}-evaluator:{phase['checkpoint']}", "version": "0.1", "evaluator_kind": kind,
                "subject_artifact_id": memory_id, "result": result, "evaluated_at": timestamp}
        artifacts.append(item)
        evaluator_refs[label] = {"artifact_id": item["artifact_id"], "version": item["version"], "hash": validator.jcs_sha256(item)}
    qualification = {
        "artifact_id": f"memory-qualification-registry:{phase['checkpoint']}", "version": "0.1", "artifacts": artifacts,
        "claim_boundary": "Synthetic evaluator bindings qualify retained history only; they do not authorize action or promotion.",
    }
    relative = f"fixtures/runtime-integrity/evidence/memory_qualification_{phase['checkpoint'].casefold()}.json"
    register_evidence(relative, qualification)
    return {
        "schema_version": "c-memory-reliance-record-0.1.1", "record_type": "memory_reliance_record",
        "record_id": f"native:{phase['attempt_id']}:memory", "created_at": timestamp,
        "memory_item_ref": {"artifact_id": memory_id, "version": "1", "hash": canonical_hash(memory_item)},
        "admission_record_ref": {"artifact_id": f"memory-admission:{phase['checkpoint']}", "version": "1", "hash": canonical_hash({"memory": memory_item, "state": "QUARANTINED"})},
        "current_task_ref": task_ref, "current_purpose": "Retain quarantined history without decision influence, action force, or promotion.",
        "current_role": source["role"]["name"], "current_authority_ref": grant_ref,
        "qualification_registry_ref": _artifact_ref(validator, qualification, relative),
        "freshness_evaluator_ref": evaluator_refs["freshness"], "provenance_evaluator_ref": evaluator_refs["provenance"],
        "contamination_evaluator_ref": evaluator_refs["contamination"], "revocation_source_ref": evaluator_refs["revocation"],
        "provenance_state": "VERIFIED", "freshness_state": "CURRENT", "revocation_state": "NOT_REVOKED",
        "consent_state": "NOT_REQUIRED", "conflict_state": "CLEAR", "contamination_state": "CLEAR",
        "consequence_class": "REVERSIBLE_ACTION", "verdict": "HOLD",
        "use_limits": ["retained history is not a decision basis", "no action force", "no promotion"],
        "previous_reliance_record_ref": None,
        "witness_chain_head": canonical_hash({"memory": memory_item, "checkpoint": phase["checkpoint"], "influence": "NONE"}),
        "claim_boundary": "This record preserves a quarantined memory assessment while decision and commit declare memory influence NONE.",
    }


def _preconditions(phase: dict[str, Any], grant_id: str, facts: dict[str, Any]) -> list[dict[str, str]]:
    source = phase.get("source") or {}
    source_body = {key: value for key, value in source.items() if key != "source_hash"}
    times = phase.get("times") or {}
    before, after = phase.get("sink_before") or {}, phase.get("sink_after") or {}
    refs = {
        "SOURCE_GROUNDING": f"source-grounding:{phase['checkpoint']}", "IDENTITY_CONTINUITY": phase["source"]["toy_lineage"]["lineage_id"],
        "CURRENT_AUTHORITY": grant_id, "PERIMETER": "perimeter:synthetic-sink-only",
        "TIME_WINDOW": f"source-current:{phase['checkpoint']}", "L4_BUDGET": f"l4:{phase['checkpoint']}",
        "MEMORY_RELIANCE": "memory-influence:none", "WITNESS_READINESS": f"witness-ready:{phase['checkpoint']}",
        "BLOCKING_STATE": "broker-implementation:no-queue-or-retry-primitive",
    }
    checks = {
        "SOURCE_GROUNDING": source.get("source_hash") == canonical_hash(source_body),
        "IDENTITY_CONTINUITY": (source.get("toy_lineage") or {}).get("basis") == "STIPULATED_TEST_LINEAGE_NOT_PID_OR_IDENTITY_PROOF",
        "CURRENT_AUTHORITY": (source.get("registry") or {}).get("grant_status") == "VALID" and phase.get("broker_result", {}).get("binding_revalidated") is True,
        "PERIMETER": source.get("surface_inventory") == ["synthetic-sink/effects", "synthetic-sink/promotions"],
        "TIME_WINDOW": (
            isinstance(times.get("perf_counter_start_ns"), int)
            and isinstance(times.get("perf_counter_end_ns"), int)
            and times["perf_counter_end_ns"] >= times["perf_counter_start_ns"]
            and all(isinstance(times.get(name), str) and times.get(name) for name in (
                "planning_utc", "basis_utc", "changed_utc", "window_start_utc", "commit_utc", "window_end_utc"
            ))
        ),
        "L4_BUDGET": (source.get("l4") or {}).get("state") == "SUFFICIENT",
        "MEMORY_RELIANCE": (source.get("quarantined_memory") or {}).get("action_force") is False and facts.get("promotion_delta") == 0,
        "WITNESS_READINESS": all(isinstance(value, list) for value in (
            before.get("effects"), before.get("promotions"), after.get("effects"), after.get("promotions")
        )),
        "BLOCKING_STATE": (
            phase.get("retry_path_state") == "ABSENT_NO_QUEUE_OR_RETRY_PRIMITIVE"
            and phase.get("broker_result", {}).get("result") in {"HELD", "BOUND", "DENIED"}
        ),
    }
    order = ("SOURCE_GROUNDING", "IDENTITY_CONTINUITY", "CURRENT_AUTHORITY", "PERIMETER", "TIME_WINDOW",
             "L4_BUDGET", "MEMORY_RELIANCE", "WITNESS_READINESS", "BLOCKING_STATE")
    return [{"name": name, "status": "PASS" if checks[name] else "FAIL", "evidence_ref": refs[name]} for name in order]


def _conditions(
    phase: dict[str, Any],
    grant_ref: dict[str, str],
    task_ref: dict[str, str],
    decision: dict[str, Any],
    facts: dict[str, Any],
) -> dict[str, Any]:
    timestamp = phase["times"]["commit_utc"]
    refs = {item["name"]: item["evidence_ref"] for item in _preconditions(phase, grant_ref["artifact_id"], facts)}
    return {
        "artifact_id": f"current-conditions:{phase['checkpoint']}", "version": "0.1", "captured_at": timestamp,
        "planning_state": {"observed_at": phase["times"]["planning_utc"], "permission_status": "VALID", "task_contract_status": "CURRENT",
                           "endpoint_ref": "synthetic-sink", "source_evidence_state": "FRESH", "l4_budget_state": "SUFFICIENT"},
        "changed_state": {"observed_at": phase["times"]["changed_utc"], "permission_status": "VALID", "task_contract_status": "CURRENT",
                          "endpoint_ref": "synthetic-sink", "source_evidence_state": "FRESH", "l4_budget_state": "SUFFICIENT", "queued_retry_state": "CLEAR"},
        "permission_grant_ref": grant_ref, "permission_status": "VALID", "task_contract_ref": task_ref, "task_contract_status": "CURRENT",
        "planning_target_ref": "synthetic-sink", "current_endpoint_ref": "synthetic-sink", "source_evidence_state": "FRESH",
        "l4_budget_state": "SUFFICIENT", "queued_retry_state": "CLEAR",
        "source_grounding_ref": decision["basis"]["grounding_ref"], "continuity_evidence_ref": decision["basis"]["continuity_ref"],
        "l4_state_ref": decision["basis"]["l4_ref"], "precondition_evidence_refs": refs,
        "claim_boundary": "Exact synthetic commit-time facts; no queue or retry mechanism exists in this offline path.",
    }


def _non_effect(
    validator: Any, phase: dict[str, Any], register_evidence: Callable[[str, dict[str, Any]], None],
) -> tuple[dict[str, Any], dict[str, str]]:
    prospective = phase.get("prospective_native_material")
    if prospective is not None:
        if not isinstance(prospective, dict) or prospective.get("status") != "COMPLETE_NO_COMMITTED_CHANGE":
            raise NativeInputFactConflict(
                "OBSERVATION_EVIDENCE_INCOMPLETE",
                {"status": prospective.get("status") if isinstance(prospective, dict) else None},
            )
        required_artifacts = {"scope_inventory", "route", "clock", "collector", "event_log"}
        artifacts = prospective.get("artifacts") if isinstance(prospective.get("artifacts"), dict) else {}
        if set(artifacts) != required_artifacts:
            raise NativeInputFactConflict(
                "OBSERVATION_EVIDENCE_INCOMPLETE",
                {"reason": "NATIVE_ARTIFACT_SET_MISMATCH", "actual": sorted(artifacts)},
            )
        window = prospective.get("window")
        surfaces = prospective.get("surfaces")
        if (
            prospective.get("effect_scope_ref") != phase.get("effect_intent_id")
            or prospective.get("effect_target_ref") != "synthetic-sink"
            or not isinstance(window, dict)
            or not isinstance(surfaces, list)
            or len(surfaces) != 2
            or artifacts["event_log"].get("events") != []
            or artifacts["event_log"].get("surface_observations") != surfaces
            or any(
                item.get("before_hash") != item.get("after_hash")
                or item.get("external_call_count") != 0
                or item.get("coverage") != "COMPLETE"
                for item in surfaces
            )
        ):
            raise NativeInputFactConflict(
                "OBSERVATION_EVIDENCE_CONTRADICTS_NO_EFFECT",
                {"phase": phase.get("checkpoint"), "plan_hash": prospective.get("plan_hash")},
            )
        relative_paths = {
            "scope_inventory": "fixtures/runtime-integrity/evidence/prospective_open_scope_inventory.json",
            "route": "fixtures/runtime-integrity/evidence/prospective_open_route.json",
            "clock": "fixtures/runtime-integrity/evidence/prospective_open_clock.json",
            "collector": "fixtures/runtime-integrity/evidence/prospective_open_collector.json",
            "event_log": "fixtures/runtime-integrity/evidence/prospective_open_event_log.json",
        }
        for name in ("scope_inventory", "route", "clock", "collector", "event_log"):
            register_evidence(relative_paths[name], artifacts[name])
        witness = {
            "schema_version": "c-non-effect-witness-record-0.1.1",
            "record_type": "non_effect_witness_record",
            "record_id": f"native:{phase['attempt_id']}:non-effect",
            "created_at": prospective["record_created_at_utc"],
            "attempt_ref": phase["commit_record_id"],
            "gate_record_ref": phase["commit_record_id"],
            "effect_scope_ref": prospective["effect_scope_ref"],
            "effect_target_ref": prospective["effect_target_ref"],
            "observation_window": window,
            "clock_source_ref": prospective["clock_source_ref"],
            "claim_scope": "DECLARED_SURFACES_AND_WINDOW_ONLY",
            "scope_inventory_ref": prospective["scope_inventory_ref"],
            "scope_inventory_hash": validator.jcs_sha256(artifacts["scope_inventory"]),
            "evidence_collection": {
                "collector_ref": prospective["collector_ref"],
                "availability": "COMPLETE",
                "continuous_event_log_ref": prospective["event_log_ref"],
            },
            "protected_effects": prospective["protected_effects"],
            "observation_surfaces": surfaces,
            "alternate_path_checks": [{
                "path_id": prospective["route_id"],
                "status": "NOT_REACHABLE",
                "evidence_ref": prospective["route_evidence_ref"],
            }],
            "coverage_state": "COMPLETE_WITHIN_DECLARED_SURFACE",
            "conclusion": "NO_EFFECT_OBSERVED_WITHIN_DECLARED_SCOPE",
            "witness_chain_head": canonical_hash({
                "window": window,
                "surfaces": surfaces,
                "commit": phase["commit_record_id"],
                "observation_plan": prospective["plan_hash"],
            }),
            "claim_boundary": "The conclusion is limited to the declared observation window and enumerated surfaces. It is not a metaphysical proof that no effect occurred anywhere outside those surfaces.",
        }
        return witness, {
            "artifact_id": witness["record_id"],
            "version": "0.1.1",
            "hash": validator.jcs_sha256(witness),
        }

    window = {"start": phase["times"]["window_start_utc"], "end": phase["times"]["window_end_utc"]}
    target, effect_id = "synthetic-sink", phase["effect_intent_id"]
    protected = ["synthetic acceptance row", "memory promotion row"]
    surfaces = [{
        "surface_id": sid, "surface_kind": "DATABASE", "target_ref": target, "target_coordinate": f"{target}/{sid}",
        "hash_domain": "CANONICAL_STATE_SHA256_V1", "before_hash": canonical_hash(phase["sink_before"][sid]),
        "after_hash": canonical_hash(phase["sink_after"][sid]), "external_call_count": 0,
        "queue_state": "NOT_APPLICABLE", "retry_state": "DISABLED", "coverage": "COMPLETE",
    } for sid in ("effects", "promotions")]
    route_id, route_eid = "offline-broker-retry-path", f"route-evidence:{phase['checkpoint']}"
    clock_id, collector_id, event_id, inventory_id = (f"clock-evidence:{phase['checkpoint']}", f"collector:{phase['checkpoint']}",
                                                       f"event-log:{phase['checkpoint']}", f"scope-inventory:{phase['checkpoint']}")
    inventory = {"schema_version": "c-non-effect-scope-inventory-0.1", "evidence_ids": [inventory_id],
                 "effect_scope_ref": effect_id, "effect_target_ref": target, "protected_effects": protected,
                 "observation_surface_descriptors": [{key: s[key] for key in ("surface_id", "surface_kind", "target_ref", "target_coordinate", "hash_domain")} for s in surfaces],
                 "alternate_path_ids": [route_id]}
    artifacts = {
        "scope_inventory": inventory,
        "route": {"schema_version": "c-route-evidence-0.1", "evidence_ids": [route_eid], "collector_ref": collector_id,
                  "window": window, "path_states": [{"path_id": route_id, "status": "NOT_REACHABLE"}]},
        "clock": {"schema_version": "c-clock-evidence-0.1", "evidence_ids": [clock_id],
                  "clock_kind": "MONOTONIC_WITH_UTC_CORRELATION", "correlation_window": window},
        "collector": {"schema_version": "c-collector-evidence-0.1", "evidence_ids": [collector_id], "availability": "COMPLETE",
                      "continuous_event_log_ref": event_id, "surface_ids": [s["surface_id"] for s in surfaces], "window": window},
        "event_log": {"schema_version": "c-non-effect-event-log-0.1", "evidence_ids": [event_id], "collector_ref": collector_id,
                      "window": window, "availability": "COMPLETE", "surface_observations": surfaces, "events": []},
    }
    for name, artifact in artifacts.items():
        register_evidence(f"fixtures/runtime-integrity/evidence/open_{name}.json", artifact)
    witness = {
        "schema_version": "c-non-effect-witness-record-0.1.1", "record_type": "non_effect_witness_record",
        "record_id": f"native:{phase['attempt_id']}:non-effect", "created_at": window["end"],
        "attempt_ref": phase["commit_record_id"], "gate_record_ref": phase["commit_record_id"],
        "effect_scope_ref": effect_id, "effect_target_ref": target, "observation_window": window, "clock_source_ref": clock_id,
        "claim_scope": "DECLARED_SURFACES_AND_WINDOW_ONLY", "scope_inventory_ref": inventory_id,
        "scope_inventory_hash": validator.jcs_sha256(inventory),
        "evidence_collection": {"collector_ref": collector_id, "availability": "COMPLETE", "continuous_event_log_ref": event_id},
        "protected_effects": protected, "observation_surfaces": surfaces,
        "alternate_path_checks": [{"path_id": route_id, "status": "NOT_REACHABLE", "evidence_ref": route_eid}],
        "coverage_state": "COMPLETE_WITHIN_DECLARED_SURFACE", "conclusion": "NO_EFFECT_OBSERVED_WITHIN_DECLARED_SCOPE",
        "witness_chain_head": canonical_hash({"window": window, "surfaces": surfaces, "commit": phase["commit_record_id"]}),
        "claim_boundary": "The conclusion is limited to the declared observation window and enumerated surfaces. It is not a metaphysical proof that no effect occurred anywhere outside those surfaces.",
    }
    return witness, {"artifact_id": witness["record_id"], "version": "0.1.1", "hash": validator.jcs_sha256(witness)}


def _commit(
    validator: Any, phase: dict[str, Any], decision: dict[str, Any], grant_ref: dict[str, str], task_ref: dict[str, str],
    conditions_ref: dict[str, str], witness_ref: dict[str, str] | None, previous_ref: dict[str, str] | None,
    transition_ref: dict[str, str] | None,
) -> dict[str, Any]:
    timestamp = phase["times"]["commit_utc"]
    facts = derive_native_outcome(phase)
    preconditions = _preconditions(phase, grant_ref["artifact_id"], facts)
    if facts["effect_state"] == "BOUND" and any(item["status"] != "PASS" for item in preconditions):
        raise NativeInputFactConflict(
            "INPUT_FACT_CONFLICT",
            {
                "checkpoint_label": phase.get("checkpoint"),
                "conflicts": [
                    f"NATIVE_PRECONDITION_NOT_PASS:{item['name']}"
                    for item in preconditions if item["status"] != "PASS"
                ],
            },
        )
    bound = facts["effect_state"] == "BOUND"
    return {
        "schema_version": "c-consequence-commit-record-0.1.1", "record_type": "consequence_commit_record",
        "record_id": phase["commit_record_id"], "created_at": timestamp,
        "consequence_lineage_id": "consequence-lineage:r1-6f-logic-path", "governing_entity_id": "c:synthetic-r1-6f",
        "human_anchor_ref": "synthetic-owner:not-live-authority", "agent_ref": "agent:offline-receiver",
        "task_contract_ref": task_ref, "permission_grant_ref": grant_ref, "permission_status": "VALID",
        "permission_checked_at": timestamp, "permission_valid_until": phase["grant_valid_until_utc"],
        "permission_issuer_ref": "synthetic-policy-root", "permission_subject_ref": "agent:offline-receiver",
        "authorized_target_ref": "synthetic-sink", "task_contract_status": "CURRENT", "task_contract_checked_at": timestamp,
        "task_endpoint_ref": "synthetic-sink", "continuity_approver_ref": "synthetic-lineage-fixture-owner",
        "memory_influence_state": "NONE", "memory_reliance_refs": [],
        "decision_basis_ref": {"artifact_id": decision["record_id"], "version": "0.1.1", "hash": validator.jcs_sha256(decision)},
        "source_grounding_ref": decision["basis"]["grounding_ref"], "continuity_evidence_ref": decision["basis"]["continuity_ref"],
        "l4_state_ref": decision["basis"]["l4_ref"],
        "target_effect": {"effect_id": phase["effect_intent_id"], "effect_class": "LOW", "target_ref": "synthetic-sink", "reversibility": "REVERSIBLE"},
        "precondition_results": preconditions,
        "commit_outcome": facts["commit_outcome"], "effect_state": facts["effect_state"],
        "effect_artifact_hash": canonical_hash(facts["effect_row"]) if bound else None,
        "non_effect_witness_ref": witness_ref if not bound else None,
        "previous_commit_record_ref": previous_ref if bound else None,
        "change_reason_code": "CONDITIONS_REVALIDATED_SAME_TARGET" if bound else None,
        "change_reason": "A scoped clarification resolved the same QSF for the same target; prior HOLD remains immutable." if bound else None,
        "target_transition_evidence_ref": transition_ref if bound else None, "current_conditions_ref": conditions_ref,
        "current_conditions_hash": conditions_ref["hash"],
        "witness_chain_head": canonical_hash({"checkpoint": phase["checkpoint"], "source": phase["source"]["source_hash"], "broker": phase["broker_result"]}),
        "claim_boundary": ("This record binds one synthetic local database effect to exact offline facts; it is not a real-world effect."
                           if bound else validator.NOT_BOUND_COMMIT_CLAIM_BOUNDARY),
    }


def emit_and_validate_logic_path(path_facts: dict[str, Any], output: Path) -> dict[str, Any]:
    validator = load_validator()
    phases = {item["checkpoint"]: item for item in path_facts["phases"]}
    try:
        fact_outcomes = {
            checkpoint: derive_native_outcome(phases[checkpoint])
            for checkpoint in ("OPEN_CHECK", "RESOLVED_CHECK")
        }
    except NativeInputFactConflict as conflict:
        output.mkdir(parents=True, exist_ok=False)
        result = {
            "scope": "SYNTHETIC_REGRESSION",
            "status": conflict.code,
            "accepted": False,
            "input_fact_conflict": conflict.as_dict(),
            "record_count": 0,
            "layer_status": {
                "shape": "NOT_RUN",
                "record_semantics": "NOT_RUN",
                "registered_evidence": "NOT_RUN",
                "bundle_links": "NOT_RUN",
            },
            "validator": dependency_status(),
            "vendor_schema_modified": False,
        }
        write_json(output / "input_fact_conflict.json", conflict.as_dict())
        write_json(output / "validation.json", result)
        return result
    output.mkdir(parents=True, exist_ok=False)
    overlay = output / "validator_overlay"
    fixture_dir, evidence_dir = overlay / "fixtures" / "runtime-integrity", overlay / "fixtures" / "runtime-integrity" / "evidence"
    evidence_dir.mkdir(parents=True)
    evidence_registry: dict[str, dict[str, str]] = {}

    def register_evidence(relative: str, artifact: dict[str, Any]) -> None:
        write_json(overlay / relative, artifact)
        artifact_hash = validator.jcs_sha256(artifact)
        for logical_id in artifact.get("evidence_ids") or [artifact.get("artifact_id")]:
            evidence_registry[str(logical_id)] = {"path": relative, "hash": artifact_hash}

    grant = {"artifact_id": "synthetic-grant:r1-6f", "version": "0.1", "issuer_ref": "synthetic-policy-root",
             "subject_ref": "agent:offline-receiver", "authorized_target_ref": "synthetic-sink",
             "valid_until": path_facts["grant_valid_until_utc"],
             "status_history": [{"status": "VALID", "effective_at": path_facts["grant_effective_utc"]}],
             "claim_boundary": "Synthetic task-local grant for defensive offline regression only; not live authority."}
    task = {"artifact_id": "task-contract:r1-6f", "version": "0.1",
            "status_history": [{"status": "CURRENT", "endpoint_ref": "synthetic-sink", "effective_at": path_facts["grant_effective_utc"]}],
            "claim_boundary": "Synthetic task-local contract for defensive offline regression only."}
    register_evidence("fixtures/runtime-integrity/evidence/permission_grant.json", grant)
    register_evidence("fixtures/runtime-integrity/evidence/task_contract.json", task)
    grant_ref, task_ref = _artifact_ref(validator, grant), _artifact_ref(validator, task)
    record_registry: dict[str, str] = {}
    records: dict[str, dict[str, Any]] = {}
    open_commit: dict[str, Any] | None = None
    for checkpoint in ("OPEN_CHECK", "RESOLVED_CHECK"):
        phase = phases[checkpoint]
        phase["grant_valid_until_utc"] = path_facts["grant_valid_until_utc"]
        phase_dir = fixture_dir / "r1_6f" / checkpoint.casefold()
        phase_dir.mkdir(parents=True)
        decision = _decision(validator, phase, grant_ref)
        memory = _memory_record(validator, phase, grant_ref, task_ref, register_evidence)
        phase_facts = fact_outcomes[checkpoint]
        conditions = _conditions(phase, grant_ref, task_ref, decision, phase_facts)
        register_evidence(f"fixtures/runtime-integrity/evidence/conditions_{checkpoint.casefold()}.json", conditions)
        conditions_ref = _artifact_ref(validator, conditions)
        witness = witness_ref = None
        if phase_facts["effect_state"] == "NOT_BOUND":
            witness, witness_ref = _non_effect(validator, phase, register_evidence)
        previous_ref = transition_ref = None
        if phase_facts["effect_state"] == "BOUND":
            assert open_commit is not None
            previous_ref = {"artifact_id": open_commit["record_id"], "version": "0.1.1", "hash": validator.jcs_sha256(open_commit)}
            transition = {
                "artifact_id": "target-transition:r1-6f-open-to-resolved", "version": "0.1", "evidence_kind": "TARGET_TRANSITION",
                "consequence_lineage_id": "consequence-lineage:r1-6f-logic-path", "effect_id": phase["effect_intent_id"],
                "effect_class": "LOW", "reversibility": "REVERSIBLE", "previous_record_id": open_commit["record_id"],
                "current_record_id": phase["commit_record_id"], "previous_target_ref": "synthetic-sink", "current_target_ref": "synthetic-sink",
                "reason_code": "CONDITIONS_REVALIDATED_SAME_TARGET", "previous_permission_grant_ref": grant_ref,
                "current_permission_grant_ref": grant_ref, "previous_task_contract_ref": task_ref, "current_task_contract_ref": task_ref,
                "observed_at": phase["times"]["changed_utc"],
                "claim_boundary": "Synthetic append-only clarification on the same target; no target or authority expansion occurred.",
            }
            register_evidence("fixtures/runtime-integrity/evidence/target_transition.json", transition)
            transition_ref = _artifact_ref(validator, transition)
        commit = _commit(validator, phase, decision, grant_ref, task_ref, conditions_ref, witness_ref, previous_ref, transition_ref)
        if checkpoint == "OPEN_CHECK":
            open_commit = commit
        phase_records = {"decision": decision, "memory": memory, "commit": commit}
        if witness is not None:
            phase_records["non_effect"] = witness
        for name, record in phase_records.items():
            relative = f"r1_6f/{checkpoint.casefold()}/{name}.json"
            write_json(fixture_dir / relative, record)
            record_registry[record["record_id"]] = relative
            records[record["record_id"]] = record

    vendor_schema_dir = validator.SCHEMA_DIR
    validator.ROOT, validator.FIXTURE_DIR, validator.EVIDENCE_DIR, validator.SCHEMA_DIR = overlay, fixture_dir, evidence_dir, vendor_schema_dir
    schemas, schema_registry = validator.build_registry()
    rows = []
    for record_id, record in records.items():
        shape = validator.validate_schema(record, SCHEMA_IDS[record["record_type"]], schemas, schema_registry)
        semantics = validator.SEMANTIC_BY_TYPE[record["record_type"]](record)
        evidence = validator.validate_registered_evidence(record, evidence_registry)
        links = validator.validate_registered_links(record, record_registry, schemas, schema_registry, evidence_registry)
        rows.append({"record_id": record_id, "record_type": record["record_type"],
                     "shape_issue_codes": sorted({item.code for item in shape}),
                     "record_semantics_issue_codes": sorted({item.code for item in semantics}),
                     "registered_evidence_issue_codes": sorted({item.code for item in evidence}),
                     "bundle_link_issue_codes": sorted({item.code for item in links})})
    dag_nodes, dag = validator.validate_previous_commit_dag(record_registry)
    layer_status = {
        "shape": "PASS" if all(not r["shape_issue_codes"] for r in rows) else "FAIL",
        "record_semantics": "PASS" if all(not r["record_semantics_issue_codes"] for r in rows) else "FAIL",
        "registered_evidence": "PASS" if all(not r["registered_evidence_issue_codes"] for r in rows) else "FAIL",
        "bundle_links": "PASS" if all(not r["bundle_link_issue_codes"] for r in rows) and not dag else "FAIL",
    }
    accepted = all(value == "PASS" for value in layer_status.values())
    result = {
        "scope": "SYNTHETIC_REGRESSION",
        "timestamp_provenance": "ACTUAL_LOCAL_UTC_AND_PERF_COUNTER_ENDPOINTS_FROM_OFFLINE_PYTHON_RUN",
        "identity_continuity_basis": "STIPULATED_TOY_LINEAGE_NOT_PID_OR_MEMORY",
        "validator": dependency_status(), "vendor_schema_modified": False, "record_count": len(records),
        "evidence_artifact_count": len({entry["path"] for entry in evidence_registry.values()}),
        "record_registry": record_registry, "evidence_registry": evidence_registry, "dag_nodes": dag_nodes,
        "dag_issue_codes": sorted({item.code for item in dag}), "rows": rows, "layer_status": layer_status,
        "accepted": accepted, "status": "PASS" if accepted else "NATIVE_BINDING_INCOMPLETE",
    }
    write_json(output / "validation.json", result)
    write_json(output / "registry.json", {"record_registry": record_registry, "evidence_registry": evidence_registry})
    return result
