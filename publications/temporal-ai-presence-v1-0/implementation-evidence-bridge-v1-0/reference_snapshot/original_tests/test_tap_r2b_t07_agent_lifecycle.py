from copy import deepcopy

from tap_conformance.bindings.r2b import (
    discover_t07_agent_surfaces,
    inventory_summary,
    validate_t07_inventory,
)
from tests.tap_test_support import REPO_ROOT


def test_r2b_t07_all_surfaces_have_explicit_lifecycle_classification():
    rows = discover_t07_agent_surfaces(REPO_ROOT)
    summary = inventory_summary(rows)
    assert len(rows) == 14
    assert summary == {
        "DISABLED_BY_DEFAULT": 4,
        "INVENTORIED": 8,
        "LEGACY_INACTIVE": 1,
        "OUT_OF_SCOPE_WITH_REASON": 1,
    }
    assert validate_t07_inventory(rows) == []


def test_r2b_t07_hidden_executor_is_blocking():
    row = deepcopy(discover_t07_agent_surfaces(REPO_ROOT)[0])
    row["classification"] = "HIDDEN"
    assert "TAP-R2B-T07-HIDDEN-EXECUTOR" in validate_t07_inventory([row])


def test_r2b_t07_unresolved_executor_fails_closed():
    row = deepcopy(discover_t07_agent_surfaces(REPO_ROOT)[0])
    row["classification"] = "UNRESOLVED"
    assert "TAP-R2B-T07-UNRESOLVED-SURFACE" in validate_t07_inventory([row])


def test_r2b_t07_synergy_agent_is_data_not_executor():
    rows = discover_t07_agent_surfaces(REPO_ROOT)
    row = next(item for item in rows if item["source_path"] == "modules/synergy/models.py")
    assert row["classification"] == "OUT_OF_SCOPE_WITH_REASON"
    assert "data only" in row["classification_reason"]
