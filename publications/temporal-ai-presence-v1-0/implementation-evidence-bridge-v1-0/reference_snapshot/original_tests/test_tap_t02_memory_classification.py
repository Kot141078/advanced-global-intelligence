import pytest

from tests.tap_test_support import assert_binding, assert_negative, assert_positive, fixture_cases

POSITIVE, NEGATIVE = fixture_cases("TAP-T02")


def test_tap_t02_positive_and_binding():
    assert_positive(POSITIVE)
    assert_binding("TAP-T02")


@pytest.mark.parametrize("case", NEGATIVE, ids=lambda case: case["fixture_id"])
def test_tap_t02_negative_fixtures_fail_closed(case):
    assert_negative("TAP-T02", POSITIVE["instance_key"], case)
