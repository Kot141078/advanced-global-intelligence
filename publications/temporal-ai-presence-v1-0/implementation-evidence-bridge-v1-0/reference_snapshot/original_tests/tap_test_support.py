"""Shared deterministic fixture mechanics for the exact TAP test suite."""

from __future__ import annotations

import copy
import json
from functools import lru_cache
from pathlib import Path
from typing import Any

from tap_conformance.bindings.ester import validate_binding_map
from tap_conformance.loader import load_instance
from tap_conformance.validators.core import validate_test

REPO_ROOT = Path(__file__).resolve().parents[1]
INSTANCE_DIR = REPO_ROOT / "tap_conformance" / "instances" / "ester_candidate"
FIXTURE_DIR = REPO_ROOT / "tap_conformance" / "fixtures"


@lru_cache(maxsize=1)
def instance() -> dict[str, Any]:
    return load_instance(INSTANCE_DIR)


def fixture_cases(test_id: str) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    filename = test_id.replace("-", "_") + ".json"
    positive = json.loads((FIXTURE_DIR / "positive" / filename).read_text(encoding="utf-8"))
    negative = json.loads((FIXTURE_DIR / "negative" / filename).read_text(encoding="utf-8"))
    return positive, list(negative["fixtures"])


def base_document(instance_key: str) -> dict[str, Any]:
    return copy.deepcopy(instance()[instance_key])


def _parent(document: Any, path: list[Any]) -> tuple[Any, Any]:
    current = document
    for part in path[:-1]:
        current = current[part]
    return current, path[-1]


def _set(document: Any, path: list[Any], value: Any) -> None:
    parent, key = _parent(document, path)
    parent[key] = copy.deepcopy(value)


def apply_mutation(document: dict[str, Any], mutation: dict[str, Any]) -> dict[str, Any]:
    result = copy.deepcopy(document)
    op = mutation["op"]
    if op == "set":
        _set(result, mutation["path"], mutation["value"])
    elif op == "delete":
        parent, key = _parent(result, mutation["path"])
        del parent[key]
    elif op == "append":
        parent = result
        for part in mutation["path"]:
            parent = parent[part]
        parent.append(copy.deepcopy(mutation["value"]))
    elif op == "append_copy":
        parent = result
        for part in mutation["path"]:
            parent = parent[part]
        parent.append(copy.deepcopy(parent[mutation["source_index"]]))
    elif op == "set_many":
        for change in mutation["changes"]:
            _set(result, change["path"], change["value"])
    else:
        raise AssertionError(f"unsupported fixture mutation: {op}")
    return result


def assert_positive(positive: dict[str, Any]) -> None:
    document = base_document(positive["instance_key"])
    issues = validate_test(positive["test_id"], document)
    assert issues == [], [issue.to_dict() for issue in issues]


def assert_negative(test_id: str, instance_key: str, case: dict[str, Any]) -> None:
    document = apply_mutation(base_document(instance_key), case["mutation"])
    issues = validate_test(test_id, document)
    assert issues, f"expected fail-closed rejection for {case['fixture_id']}"
    assert issues[0].code == case["expected_failure_code"], [issue.to_dict() for issue in issues]
    registry = json.loads((REPO_ROOT / "tap_conformance" / "TAP_FAILURE_CODES.json").read_text(encoding="utf-8"))
    registered = {row["code"] for row in registry["failure_codes"]}
    assert case["expected_failure_code"] in registered


def assert_binding(test_id: str) -> None:
    binding_map = instance()["binding_map"]
    errors = validate_binding_map(REPO_ROOT, binding_map)
    assert errors == [], errors
    row = next(item for item in binding_map["bindings"] if item["test_id"] == test_id)
    for key in ("declaration_artifact", "positive_test", "negative_fixtures"):
        assert (REPO_ROOT / row[key]).is_file(), f"missing bound path: {row[key]}"
