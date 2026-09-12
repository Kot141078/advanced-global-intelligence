from __future__ import annotations

from pathlib import Path
from typing import Any

from .common import write_json
from .native_adapter import (
    SCHEMA_IDS,
    _artifact_ref,
    _commit,
    _conditions,
    _decision,
    _memory_record,
    _non_effect,
    dependency_status,
    derive_native_outcome,
    load_validator,
)


def emit_and_validate_s2_hold(phase: dict[str, Any], output: Path, *, evidence_scope: str) -> dict[str, Any]:
    """Emit one HOLD bundle through the accepted native constructors.

    This is bounded glue around the R1.6F adapter and the unchanged pinned
    validator. It adds no schema, enum, evaluator, or alternate validation rule.
    """
    if evidence_scope not in {
        "SYNTHETIC_REGRESSION",
        "ACTUAL_S2_PREFLIGHT",
        "LOCAL_CALIBRATION_PROSPECTIVE",
    }:
        raise ValueError("invalid S2 native evidence scope")
    if evidence_scope == "LOCAL_CALIBRATION_PROSPECTIVE" and not phase.get("prospective_native_material"):
        raise ValueError("prospective calibration requires reviewed observation material")
    validator = load_validator()
    facts = derive_native_outcome(phase)
    if facts["commit_outcome"] != "HOLD" or facts["effect_state"] != "NOT_BOUND":
        raise ValueError("S2 HOLD native adapter received non-HOLD facts")
    output.mkdir(parents=True, exist_ok=False)
    overlay = output / "validator_overlay"
    fixture_dir = overlay / "fixtures" / "runtime-integrity"
    evidence_dir = fixture_dir / "evidence"
    evidence_dir.mkdir(parents=True)
    evidence_registry: dict[str, dict[str, str]] = {}

    def register_evidence(relative: str, artifact: dict[str, Any]) -> None:
        write_json(overlay / relative, artifact)
        artifact_hash = validator.jcs_sha256(artifact)
        logical_ids = artifact.get("evidence_ids") or [artifact.get("artifact_id")]
        for logical_id in logical_ids:
            evidence_registry[str(logical_id)] = {"path": relative, "hash": artifact_hash}

    attempt_id = phase["attempt_id"]
    effective = phase["times"]["basis_utc"]
    grant = {
        "artifact_id": f"synthetic-grant:s2:{attempt_id}",
        "version": "0.1",
        "issuer_ref": "synthetic-policy-root",
        "subject_ref": "agent:bounded-s2-receiver",
        "authorized_target_ref": "synthetic-sink",
        "valid_until": phase["grant_valid_until_utc"],
        "status_history": [{"status": "VALID", "effective_at": effective}],
        "claim_boundary": "Synthetic task-local proposal admission for this S2 preflight; no protected effect authority and no live authority.",
    }
    task = {
        "artifact_id": f"task-contract:s2:{attempt_id}",
        "version": "0.1",
        "status_history": [{"status": "CURRENT", "endpoint_ref": "synthetic-sink", "effective_at": effective}],
        "claim_boundary": "One bounded OPEN-state handoff preflight only; no matrix or live task contract.",
    }
    register_evidence("fixtures/runtime-integrity/evidence/s2_permission_grant.json", grant)
    register_evidence("fixtures/runtime-integrity/evidence/s2_task_contract.json", task)
    grant_ref, task_ref = _artifact_ref(validator, grant), _artifact_ref(validator, task)

    decision = _decision(validator, phase, grant_ref)
    decision["claim_boundary"] = (
        "Actual bounded S2 preflight decision basis from restored state, external E1, receiver result, and declared local target readback."
        if evidence_scope in {"ACTUAL_S2_PREFLIGHT", "LOCAL_CALIBRATION_PROSPECTIVE"}
        else "Process-free synthetic S2 HOLD adapter regression; not OS or process evidence."
    )
    memory = _memory_record(validator, phase, grant_ref, task_ref, register_evidence)
    memory["claim_boundary"] = (
        "Actual S2 preflight retains quarantined history without decision influence, action force, or promotion."
        if evidence_scope in {"ACTUAL_S2_PREFLIGHT", "LOCAL_CALIBRATION_PROSPECTIVE"}
        else "Synthetic S2 regression retains quarantined history without decision influence or promotion."
    )
    conditions = _conditions(phase, grant_ref, task_ref, decision, facts)
    conditions["claim_boundary"] = (
        "Current task-local S2 preflight conditions from the E1 view and exact broker/readback window; no queue or retry primitive exists."
    )
    register_evidence("fixtures/runtime-integrity/evidence/s2_current_conditions.json", conditions)
    conditions_ref = _artifact_ref(validator, conditions)
    witness, witness_ref = _non_effect(validator, phase, register_evidence)
    commit = _commit(validator, phase, decision, grant_ref, task_ref, conditions_ref, witness_ref, None, None)
    commit["consequence_lineage_id"] = f"consequence-lineage:s2:{attempt_id}"
    commit["governing_entity_id"] = "c:synthetic-r1-6i"
    commit["agent_ref"] = "agent:bounded-s2-receiver"
    commit["permission_subject_ref"] = "agent:bounded-s2-receiver"
    records = {
        decision["record_id"]: decision,
        memory["record_id"]: memory,
        witness["record_id"]: witness,
        commit["record_id"]: commit,
    }
    record_registry: dict[str, str] = {}
    phase_dir = fixture_dir / "r1_6i" / "s2_open_check"
    phase_dir.mkdir(parents=True)
    names = {decision["record_id"]: "decision", memory["record_id"]: "memory", witness["record_id"]: "non_effect", commit["record_id"]: "commit"}
    for record_id, record in records.items():
        relative = f"r1_6i/s2_open_check/{names[record_id]}.json"
        write_json(fixture_dir / relative, record)
        record_registry[record_id] = relative

    vendor_schema_dir = validator.SCHEMA_DIR
    validator.ROOT, validator.FIXTURE_DIR, validator.EVIDENCE_DIR, validator.SCHEMA_DIR = overlay, fixture_dir, evidence_dir, vendor_schema_dir
    schemas, schema_registry = validator.build_registry()
    rows = []
    for record_id, record in records.items():
        shape = validator.validate_schema(record, SCHEMA_IDS[record["record_type"]], schemas, schema_registry)
        semantics = validator.SEMANTIC_BY_TYPE[record["record_type"]](record)
        evidence = validator.validate_registered_evidence(record, evidence_registry)
        links = validator.validate_registered_links(record, record_registry, schemas, schema_registry, evidence_registry)
        rows.append({
            "record_id": record_id,
            "record_type": record["record_type"],
            "shape_issue_codes": sorted({item.code for item in shape}),
            "record_semantics_issue_codes": sorted({item.code for item in semantics}),
            "registered_evidence_issue_codes": sorted({item.code for item in evidence}),
            "bundle_link_issue_codes": sorted({item.code for item in links}),
        })
    dag_nodes, dag = validator.validate_previous_commit_dag(record_registry)
    layers = {
        "shape": "PASS" if all(not row["shape_issue_codes"] for row in rows) else "FAIL",
        "record_semantics": "PASS" if all(not row["record_semantics_issue_codes"] for row in rows) else "FAIL",
        "registered_evidence": "PASS" if all(not row["registered_evidence_issue_codes"] for row in rows) else "FAIL",
        "bundle_links": "PASS" if all(not row["bundle_link_issue_codes"] for row in rows) and not dag else "FAIL",
    }
    accepted = all(value == "PASS" for value in layers.values())
    result = {
        "scope": evidence_scope,
        "status": "PASS" if accepted else "NATIVE_BINDING_INCOMPLETE",
        "accepted": accepted,
        "record_count": len(records),
        "record_registry": record_registry,
        "evidence_registry": evidence_registry,
        "rows": rows,
        "dag_nodes": dag_nodes,
        "dag_issue_codes": sorted({item.code for item in dag}),
        "layer_status": layers,
        "validator": dependency_status(),
        "vendor_schema_modified": False,
        "timestamp_provenance": (
            "ACTUAL_S2_PREFLIGHT_UTC_AND_HOST_MONOTONIC_OBSERVATION_ENDPOINTS"
            if evidence_scope == "ACTUAL_S2_PREFLIGHT"
            else "ACTUAL_LOCAL_SQLITE_CALIBRATION_CLOCK_PAIRS_NO_PROCESS_OBSERVATION"
            if evidence_scope == "LOCAL_CALIBRATION_PROSPECTIVE"
            else "SYNTHETIC_PROCESS_FREE_CLOCK_FIXTURE"
        ),
        "identity_continuity_basis": "STIPULATED_TOY_LINEAGE_NOT_PID_OR_MEMORY",
        "claim_ceiling": "One OPEN/HOLD native slice and declared non-effect window only; no identity proof or selected-process conformance.",
    }
    write_json(output / "validation.json", result)
    write_json(output / "registry.json", {"record_registry": record_registry, "evidence_registry": evidence_registry})
    return result
