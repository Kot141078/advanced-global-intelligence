import json

import pytest

from tap_conformance.bindings.ester import discover_agent_surfaces
from tests.tap_test_support import INSTANCE_DIR, REPO_ROOT, assert_binding, assert_negative, assert_positive, fixture_cases

POSITIVE, NEGATIVE = fixture_cases("TAP-T07")


def test_tap_t07_positive_binding_and_measured_surface_coverage():
    assert_positive(POSITIVE)
    assert_binding("TAP-T07")
    declared = json.loads((INSTANCE_DIR / "TAP_T07_AGENT_SURFACE_COVERAGE.json").read_text(encoding="utf-8"))["surfaces"]
    discovered = discover_agent_surfaces(REPO_ROOT)
    assert declared == discovered
    assert all(row["status"] in {"INVENTORIED", "OUT_OF_SCOPE_WITH_REASON", "UNRESOLVED"} for row in declared)


@pytest.mark.parametrize("case", NEGATIVE, ids=lambda case: case["fixture_id"])
def test_tap_t07_negative_fixtures_fail_closed(case):
    assert_negative("TAP-T07", POSITIVE["instance_key"], case)
