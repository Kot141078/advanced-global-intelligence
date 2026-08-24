import pytest

from tests.tap_test_support import assert_binding, assert_negative, assert_positive, fixture_cases, instance

POSITIVE, NEGATIVE = fixture_cases("TAP-T08")


def test_tap_t08_positive_binding_and_claim_ceiling():
    assert_positive(POSITIVE)
    assert_binding("TAP-T08")
    boundary = instance()["c_boundary"]
    assert boundary["claim"] == "NOT CLAIMED"
    assert boundary["M4_FULL_PASS"] is False


@pytest.mark.parametrize("case", NEGATIVE, ids=lambda case: case["fixture_id"])
def test_tap_t08_negative_fixtures_fail_closed(case):
    assert_negative("TAP-T08", POSITIVE["instance_key"], case)
