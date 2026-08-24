import pytest

from tap_conformance.bindings.ester import discover_cloud_call_sites
from tests.tap_test_support import REPO_ROOT, assert_binding, assert_negative, assert_positive, fixture_cases, instance

POSITIVE, NEGATIVE = fixture_cases("TAP-T06")


def test_tap_t06_positive_binding_and_complete_call_site_classification():
    assert_positive(POSITIVE)
    assert_binding("TAP-T06")
    discovered = discover_cloud_call_sites(REPO_ROOT)
    declared = instance()["t06_inventory"]["call_sites"]
    assert declared == discovered
    assert all(row["status"] in {"BOUND", "EXPLICITLY_DISABLED", "OUT_OF_SCOPE_WITH_REASON", "UNRESOLVED"} for row in declared)


@pytest.mark.parametrize("case", NEGATIVE, ids=lambda case: case["fixture_id"])
def test_tap_t06_negative_fixtures_fail_closed(case):
    assert_negative("TAP-T06", POSITIVE["instance_key"], case)
