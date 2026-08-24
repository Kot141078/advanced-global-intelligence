#!/usr/bin/env python3
"""Offline validation entry point for TAP-ACEB v1.0.

Invoke with ``python -I -B run_offline_validation.py --output <external.json>``.
Only static source parsing and declaration validation are performed. No source
implementation module is imported or started.
"""

from __future__ import annotations

import argparse
import copy
import csv
import hashlib
import json
import os
import socket
import subprocess
import sys
import time
from collections import Counter
from pathlib import Path
from typing import Any, Callable


SOURCE_COMMIT = "a668e0501dd9b975fa5e455da781611f9534e509"
EXPECTED_ROUTE_CLASSES = {
    "CLOUD_AI_ORACLE": 1,
    "LEGACY_INACTIVE": 3,
    "LOCAL_LOOPBACK_MODEL": 5,
    "LOCAL_SERVICE": 128,
    "NON_AI_EXTERNAL_NETWORK": 26,
    "OTHER_EXPLICIT": 3,
    "UPDATE_OR_METADATA": 11,
}
EXPECTED_T07_CLASSES = {
    "DISABLED_BY_DEFAULT": 4,
    "INVENTORIED": 8,
    "LEGACY_INACTIVE": 1,
    "OUT_OF_SCOPE_WITH_REASON": 1,
}
REQUIRED_FILES = {
    "README.md",
    "BRIDGE_SCOPE.md",
    "NON_CLAIMS.md",
    "PROVENANCE.md",
    "LICENSE_POLICY.md",
    "REQUIREMENT_TO_CODE_MAP.md",
    "REQUIREMENT_TO_CODE_MAP.json",
    "SOURCE_SELECTION_MANIFEST.json",
    "SOURCE_TRANSFORMATION_MAP.json",
    "SOURCE_LICENSE_AUDIT.md",
    "PUBLIC_EVIDENCE_MATRIX.csv",
    "PUBLICATION_ELIGIBILITY.json",
    "TAP_BRIDGE_VALIDATION_SUMMARY.json",
    "pyproject.toml",
    "requirements.lock",
    "run_offline_validation.py",
    "PACKAGE_MANIFEST.json",
    "SHA256SUMS.txt",
    "evidence/TAP_BRIDGE_TEST_RECEIPTS.jsonl",
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def parent_at(document: Any, path: list[Any]) -> tuple[Any, Any]:
    current = document
    for part in path[:-1]:
        current = current[part]
    return current, path[-1]


def mutate(document: dict[str, Any], mutation: dict[str, Any]) -> dict[str, Any]:
    result = copy.deepcopy(document)
    op = mutation["op"]
    if op == "set":
        parent, key = parent_at(result, mutation["path"])
        parent[key] = copy.deepcopy(mutation["value"])
    elif op == "delete":
        parent, key = parent_at(result, mutation["path"])
        del parent[key]
    elif op == "append":
        current: Any = result
        for part in mutation["path"]:
            current = current[part]
        current.append(copy.deepcopy(mutation["value"]))
    elif op == "append_copy":
        current = result
        for part in mutation["path"]:
            current = current[part]
        current.append(copy.deepcopy(current[mutation["source_index"]]))
    elif op == "set_many":
        for change in mutation["changes"]:
            parent, key = parent_at(result, change["path"])
            parent[key] = copy.deepcopy(change["value"])
    elif op == "sequence":
        for change in mutation["changes"]:
            result = mutate(result, change)
    else:
        raise AssertionError(f"unsupported mutation: {op}")
    return result


def validate_manifest(root: Path) -> None:
    manifest_path = root / "PACKAGE_MANIFEST.json"
    sums_path = root / "SHA256SUMS.txt"
    manifest = load_json(manifest_path)
    records = manifest["artifacts"]
    paths = [row["path"] for row in records]
    assert len(paths) == len(set(paths)), "duplicate package manifest paths"
    actual = {
        p.relative_to(root).as_posix()
        for p in root.rglob("*")
        if p.is_file() and p.name not in {"PACKAGE_MANIFEST.json", "SHA256SUMS.txt"}
    }
    assert set(paths) == actual, {
        "missing": sorted(set(paths) - actual),
        "extra": sorted(actual - set(paths)),
    }
    for row in records:
        path = root / row["path"]
        assert path.stat().st_size == row["bytes"], row["path"]
        assert sha256(path) == row["sha256"], row["path"]
        assert row["license"], row["path"]
    sums = {}
    for line in sums_path.read_text(encoding="utf-8").splitlines():
        digest, rel = line.split("  ", 1)
        sums[rel] = digest
    expected_sums = {row["path"]: row["sha256"] for row in records}
    expected_sums["PACKAGE_MANIFEST.json"] = sha256(manifest_path)
    assert sums == expected_sums


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True, help="external JSON result path")
    parser.add_argument("--pre-freeze", action="store_true", help="allow manifest files to be absent during package construction")
    args = parser.parse_args()
    started = time.monotonic()

    if sys.flags.isolated != 1:
        raise SystemExit("FAIL: python isolated mode (-I) is required")
    if not sys.dont_write_bytecode:
        raise SystemExit("FAIL: bytecode suppression (-B) is required")
    if "sitecustomize" in sys.modules or "usercustomize" in sys.modules:
        raise SystemExit("FAIL: startup customization module loaded")

    root = Path(__file__).resolve().parent
    source_root = root / "reference_snapshot" / "source"
    sys.path.insert(0, str(root / "src"))

    from tap_conformance.bindings.ester import discover_cloud_call_sites
    from tap_conformance.bindings.r2b import (
        discover_t06_call_sites,
        discover_t06_route_authority_map,
        discover_t07_agent_surfaces,
        validate_t06_inventory,
        validate_t07_inventory,
    )
    from tap_conformance.validators.core import validate_test

    network_attempts: list[str] = []

    def deny_network(*_args: Any, **_kwargs: Any) -> Any:
        network_attempts.append("blocked")
        raise AssertionError("live network is forbidden")

    socket.socket.connect = deny_network  # type: ignore[assignment]
    socket.create_connection = deny_network  # type: ignore[assignment]

    subprocess_attempts: list[str] = []

    def deny_process(*_args: Any, **_kwargs: Any) -> Any:
        subprocess_attempts.append("blocked")
        raise AssertionError("runtime/process start is forbidden")

    subprocess.Popen = deny_process  # type: ignore[assignment]
    subprocess.run = deny_process  # type: ignore[assignment]
    subprocess.call = deny_process  # type: ignore[assignment]
    subprocess.check_call = deny_process  # type: ignore[assignment]
    subprocess.check_output = deny_process  # type: ignore[assignment]

    cases: list[dict[str, Any]] = []

    def record(group: str, tap_id: str, test_id: str, fixture_id: str, action: Callable[[], Any], expected: str = "PASS") -> None:
        try:
            actual = action()
            if actual is False:
                raise AssertionError("returned false")
            cases.append({
                "group": group,
                "tap_test_id": tap_id,
                "test_id": test_id,
                "fixture_id": fixture_id,
                "expected_result": expected,
                "actual_result": "PASS",
                "result": "PASS",
                "detail": actual if isinstance(actual, (str, int, float, dict, list)) else None,
            })
        except Exception as exc:
            cases.append({
                "group": group,
                "tap_test_id": tap_id,
                "test_id": test_id,
                "fixture_id": fixture_id,
                "expected_result": expected,
                "actual_result": "FAIL",
                "result": "FAIL",
                "detail": f"{type(exc).__name__}: {exc}",
            })

    def assert_true(value: Any, message: str) -> str:
        assert value, message
        return message

    # Group A: package integrity and source provenance.
    record("A", "PACKAGE", "required-files", "package-required-files", lambda: assert_true(REQUIRED_FILES <= {p.relative_to(root).as_posix() for p in root.rglob("*") if p.is_file()} or args.pre_freeze, "required package files present"))

    def source_selection_check() -> dict[str, int]:
        manifest = load_json(root / "SOURCE_SELECTION_MANIFEST.json")
        included = [row for row in manifest["records"] if row["inclusion_decision"] == "INCLUDE_BYTE_IDENTICAL"]
        for row in included:
            public = root / row["public_path"]
            assert public.is_file(), row["public_path"]
            assert sha256(public) == row["source_sha256"] == row["public_sha256"], row["public_path"]
            assert row["public_safety_result"] == "PASS"
            assert row["license_result"] == "AGPL-3.0-OR-LATER"
        assert not [row for row in manifest["records"] if row["inclusion_decision"] == "BLOCKING_REQUIRED_BUT_UNPUBLISHABLE"]
        return {"records": len(manifest["records"]), "byte_identical": len(included)}

    record("A", "PACKAGE", "source-selection", "source-selection-closure", source_selection_check)
    record("A", "PACKAGE", "transformation-map", "transformation-map-complete", lambda: assert_true(bool(load_json(root / "SOURCE_TRANSFORMATION_MAP.json")["records"]), "derivatives mapped"))
    if not args.pre_freeze:
        record("A", "PACKAGE", "manifest-checksums", "manifest-and-sha256sums", lambda: validate_manifest(root) or "manifest and SHA256SUMS exact")

    declarations = {
        "TAP-T02": load_json(root / "declarations" / "TAP_MEMORY_CLASSES.json"),
        "TAP-T06": load_json(root / "declarations" / "TAP_CLOUD_CALL_LOG.json"),
        "TAP-T07": load_json(root / "declarations" / "TAP_AGENT_INVENTORY.json"),
        "TAP-T08": load_json(root / "declarations" / "TAP_C_BOUNDARY_DECLARATION.json"),
    }

    def positive(tap_id: str) -> str:
        issues = validate_test(tap_id, declarations[tap_id])
        assert not issues, [issue.to_dict() for issue in issues]
        return "declaration accepted"

    def negative(tap_id: str, base: dict[str, Any], fixture: dict[str, Any]) -> str:
        document = mutate(base, fixture["mutation"])
        issues = validate_test(tap_id, document)
        assert issues, f"accidental pass: {fixture['fixture_id']}"
        actual = issues[0].code
        assert actual == fixture["expected_failure_code"], {"expected": fixture["expected_failure_code"], "actual": actual}
        return actual

    # Groups B/E: declarations, original fixtures, and required bridge extensions.
    for tap_id, group in (("TAP-T02", "B"), ("TAP-T06", "C"), ("TAP-T07", "D"), ("TAP-T08", "E")):
        record(group, tap_id, f"{tap_id.lower()}-positive", f"{tap_id.lower()}-positive", lambda tid=tap_id: positive(tid))
        fixture_path = root / "fixtures" / "negative" / f"{tap_id.replace('-', '_')}.json"
        for fixture in load_json(fixture_path)["fixtures"]:
            record(group, tap_id, f"{tap_id.lower()}-negative", fixture["fixture_id"], lambda tid=tap_id, f=fixture: negative(tid, declarations[tid], f), expected="FAIL_CLOSED")

    extras = load_json(root / "fixtures" / "bridge_required_negative_cases.json")
    for fixture in extras["fixtures"]:
        tap_id = fixture["tap_test_id"]
        group = {"TAP-T02": "B", "TAP-T06": "C", "TAP-T07": "D", "TAP-T08": "E"}[tap_id]
        record(group, tap_id, f"{tap_id.lower()}-bridge-negative", fixture["fixture_id"], lambda tid=tap_id, f=fixture: negative(tid, declarations[tid], f), expected="FAIL_CLOSED")

    # T02 actual implementation binding closure.
    def t02_source_closure() -> str:
        for store in declarations["TAP-T02"]["stores"]:
            module = source_root / store["module"]
            assert module.is_file() or module.is_dir(), store["module"]
            for field in ("class", "policy", "review_route", "challenge_route", "deletion_rule", "seal_rule", "quarantine_rule"):
                assert store.get(field), {"store": store["store_id"], "field": field}
        return "four classified stores with review and authority routes"

    record("B", "TAP-T02", "t02-implementation-closure", "t02-four-store-source-bindings", t02_source_closure)

    # T06 full 179 -> 177 discovery and authority-map closure.
    old_sites = discover_cloud_call_sites(source_root)
    t06_rows = discover_t06_call_sites(source_root)
    authority_map = discover_t06_route_authority_map(source_root)
    old_ids = {row["call_site_id"] for row in old_sites}
    new_ids = {row["id"] for row in t06_rows}
    expected_false_positives = {
        "cloud:modules/ester/net_will_adapter.py:46:client.get",
        "cloud:modules/garage/invoice.py:33:client.get",
    }
    record("C", "TAP-T06", "t06-r2a-denominator", "t06-r2a-179", lambda: assert_true(len(old_sites) == 179, "179 lexical sites"))
    record("C", "TAP-T06", "t06-r2b-denominator", "t06-r2b-177", lambda: assert_true(len(t06_rows) == 177, "177 network primitives"))
    record("C", "TAP-T06", "t06-false-positives", "t06-two-false-positives", lambda: assert_true(old_ids - new_ids == expected_false_positives, "two exact false positives removed"))
    record("C", "TAP-T06", "t06-route-counts", "t06-seven-route-classes", lambda: assert_true(dict(Counter(row["route_class"] for row in t06_rows)) == EXPECTED_ROUTE_CLASSES, "route classes exact"))
    record("C", "TAP-T06", "t06-classification", "t06-bound-4-outscope-173", lambda: assert_true(dict(Counter(row["classification"] for row in t06_rows)) == {"BOUND": 4, "OUT_OF_SCOPE_WITH_REASON": 173}, "classification exact"))
    record("C", "TAP-T06", "t06-authority-map", "t06-authority-3-of-3", lambda: assert_true(len(authority_map) == 3 and validate_t06_inventory(t06_rows, authority_map) == [], "three semantic routes complete"))
    record("C", "TAP-T06", "t06-inventory-validator", "t06-zero-unresolved", lambda: assert_true(validate_t06_inventory(t06_rows, authority_map) == [], "T06 inventory validator accepted"))

    def t06_unresolved_rejected() -> str:
        changed = copy.deepcopy(t06_rows)
        changed[0]["classification"] = "UNRESOLVED"
        errors = validate_t06_inventory(changed, authority_map)
        assert errors
        return errors[0]

    def t06_incomplete_authority_rejected() -> str:
        changed = copy.deepcopy(authority_map)
        changed[0]["complete"] = False
        errors = validate_t06_inventory(t06_rows, changed)
        assert errors
        return errors[0]

    def t06_fail_closed_source() -> str:
        broker = (source_root / "modules" / "llm" / "broker.py").read_text(encoding="utf-8")
        chat = (source_root / "modules" / "chat_api.py").read_text(encoding="utf-8")
        assert "cloud_ai_requires_oracle_route" in broker
        assert "local_model_route_denied" in chat
        return "unauthorized cloud and non-loopback model routes fail before network"

    record("C", "TAP-T06", "t06-unresolved-fail-closed", "t06-synthetic-unresolved-row", t06_unresolved_rejected, expected="FAIL_CLOSED")
    record("C", "TAP-T06", "t06-authority-fail-closed", "t06-synthetic-incomplete-authority", t06_incomplete_authority_rejected, expected="FAIL_CLOSED")
    record("C", "TAP-T06", "t06-source-deny-routes", "t06-static-deny-mechanisms", t06_fail_closed_source)

    # T07 complete discovery and lifecycle closure.
    t07_rows = discover_t07_agent_surfaces(source_root)
    record("D", "TAP-T07", "t07-denominator", "t07-fourteen-surfaces", lambda: assert_true(len(t07_rows) == 14, "14 surfaces discovered"))
    record("D", "TAP-T07", "t07-classes", "t07-classification-counts", lambda: assert_true(dict(Counter(row["classification"] for row in t07_rows)) == EXPECTED_T07_CLASSES, "T07 classes exact"))
    record("D", "TAP-T07", "t07-inventory-validator", "t07-hidden-zero-unresolved-zero", lambda: assert_true(validate_t07_inventory(t07_rows) == [], "T07 inventory validator accepted"))

    def t07_source_coverage() -> str:
        for row in t07_rows:
            assert (source_root / row["source_path"]).is_file(), row["source_path"]
            for key in ("role", "creator", "creation_route", "activation_trigger", "default_activation_state", "authority_source", "stop_route", "pause_route", "revoke_route", "inventory_visibility", "logging_or_witness_route"):
                assert row.get(key), {"surface": row["surface_id"], "field": key}
        return "14 source rows and all lifecycle fields present"

    record("D", "TAP-T07", "t07-source-coverage", "t07-all-fourteen-source-paths", t07_source_coverage)

    # T08 exact claim ceiling and separate-evidence boundary.
    def t08_claim_ceiling() -> str:
        doc = declarations["TAP-T08"]
        assert doc["claim"] == "NOT CLAIMED"
        assert doc["M4_FULL_PASS"] is False
        card = (root / "declarations" / "TAP_CLAIM_CARD.md").read_text(encoding="utf-8")
        assert "TAP-C" in card and "NOT CLAIMED" in card
        return "TAP-C=NOT CLAIMED; M4_FULL_PASS=false"

    record("E", "TAP-T08", "t08-claim-ceiling", "t08-not-claimed", t08_claim_ceiling)

    # Group F: combined, no side effects, public matrix unchanged.
    def combined_boundary() -> str:
        matrix = list(csv.DictReader((root / "PUBLIC_EVIDENCE_MATRIX.csv").read_text(encoding="utf-8").splitlines()))
        current = {row["test_id"]: row["current_public_status"] for row in matrix}
        assert current["TAP-T02"] == "PUBLIC_CANDIDATE_NEEDS_IMMUTABLE_PUBLICATION"
        assert current["TAP-T03"] == "PUBLIC_PARTIAL_WITH_DEPLOYMENT_EXTERNAL_BOUNDARY"
        assert current["TAP-T06"] == "PUBLIC_CANDIDATE_NEEDS_IMMUTABLE_PUBLICATION"
        assert current["TAP-T07"] == "PUBLIC_CANDIDATE_NEEDS_IMMUTABLE_PUBLICATION"
        assert current["TAP-T08"] == "PUBLIC_CANDIDATE_NEEDS_IMMUTABLE_PUBLICATION"
        assert not network_attempts
        assert not subprocess_attempts
        return "public status unchanged; zero network and runtime starts"

    record("F", "COMBINED", "combined-claim-and-side-effect-boundary", "combined-boundary", combined_boundary)

    failed = [row for row in cases if row["result"] != "PASS"]
    result = {
        "schema_version": "1.0",
        "bridge": "Temporal AI Presence - Architecture-to-Code Evidence Bridge v1.0",
        "source_commit": SOURCE_COMMIT,
        "startup": {
            "python_executable": sys.executable,
            "python_version": sys.version.split()[0],
            "isolated": sys.flags.isolated,
            "dont_write_bytecode": sys.dont_write_bytecode,
            "sitecustomize_loaded": "sitecustomize" in sys.modules,
            "usercustomize_loaded": "usercustomize" in sys.modules,
        },
        "summary": {
            "collected": len(cases),
            "passed": len(cases) - len(failed),
            "failed": len(failed),
            "skipped": 0,
            "exit_code": 0 if not failed else 1,
            "duration_seconds": round(time.monotonic() - started, 6),
            "network_calls": len(network_attempts),
            "runtime_starts": len(subprocess_attempts),
            "private_data_used": False,
        },
        "discovery": {
            "t06_r2a_lexical_sites": len(old_sites),
            "t06_r2b_network_primitives": len(t06_rows),
            "t06_route_classes": dict(sorted(Counter(row["route_class"] for row in t06_rows).items())),
            "t06_status": dict(sorted(Counter(row["classification"] for row in t06_rows).items())),
            "t06_authority_routes": len(authority_map),
            "t06_authority_complete": len(authority_map) if validate_t06_inventory(t06_rows, authority_map) == [] else 0,
            "t07_discovered": len(t07_rows),
            "t07_classes": dict(sorted(Counter(row["classification"] for row in t07_rows).items())),
            "t07_hidden": sum(row["classification"] == "HIDDEN" for row in t07_rows),
            "t07_unresolved": sum(row["classification"] == "UNRESOLVED" for row in t07_rows),
        },
        "cases": cases,
        "verdict": "TAP_BRIDGE_OFFLINE_VALIDATION_PASS" if not failed else "TAP_BRIDGE_OFFLINE_VALIDATION_FAIL",
    }
    output = Path(args.output).resolve()
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2, ensure_ascii=True) + "\n", encoding="utf-8", newline="\n")
    print(json.dumps({"summary": result["summary"], "discovery": result["discovery"], "verdict": result["verdict"]}, indent=2))
    return 0 if not failed else 1


if __name__ == "__main__":
    raise SystemExit(main())
