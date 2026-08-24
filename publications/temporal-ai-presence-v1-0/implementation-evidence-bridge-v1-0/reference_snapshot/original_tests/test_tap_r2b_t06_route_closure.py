from copy import deepcopy

from tap_conformance.bindings.ester import discover_cloud_call_sites
from tap_conformance.bindings.r2b import (
    discover_t06_call_sites,
    discover_t06_route_authority_map,
    inventory_summary,
    validate_t06_inventory,
)
from tests.tap_test_support import REPO_ROOT


def test_r2b_t06_stricter_denominator_has_explained_delta():
    old = {row["call_site_id"] for row in discover_cloud_call_sites(REPO_ROOT)}
    new = {row["id"] for row in discover_t06_call_sites(REPO_ROOT)}
    assert len(old) == 179
    assert len(new) == 177
    assert old - new == {
        "cloud:modules/ester/net_will_adapter.py:46:client.get",
        "cloud:modules/garage/invoice.py:33:client.get",
    }
    assert new <= old


def test_r2b_t06_routes_and_authority_map_are_complete():
    rows = discover_t06_call_sites(REPO_ROOT)
    authority = discover_t06_route_authority_map(REPO_ROOT)
    assert validate_t06_inventory(rows, authority) == []
    assert inventory_summary(rows).get("UNRESOLVED", 0) == 0
    assert all(row["route_class"] and row["classification_reason"] for row in rows)
    assert len(authority) == 3
    assert sum(route["status"] == "BOUND" for route in authority) == 1
    assert sum(route["status"] == "EXPLICITLY_DISABLED" for route in authority) == 2


def test_r2b_t06_direct_cloud_broker_route_fails_before_network(monkeypatch):
    from modules.llm import broker

    attempted = []
    monkeypatch.setattr(broker.urllib.request, "urlopen", lambda *a, **k: attempted.append((a, k)))
    result = broker._http_json("https://api.openai.com/v1/chat/completions", {"prompt": "synthetic"}, {})
    assert result["ok"] is False
    assert result["error"] == "cloud_ai_requires_oracle_route"
    assert result["network_attempted"] is False
    assert attempted == []


def test_r2b_t06_chat_api_rejects_non_loopback_model_route(monkeypatch):
    from modules import chat_api

    attempted = []
    monkeypatch.setattr(chat_api, "LMSTUDIO_URL", "https://example.invalid/v1/chat/completions")
    monkeypatch.setattr(chat_api.requests, "post", lambda *a, **k: attempted.append((a, k)))
    text, error = chat_api._call_llm("synthetic", [{"role": "user", "content": "fixture"}], temperature=0.0)
    assert text == ""
    assert error == "local_model_route_denied"
    assert attempted == []


def test_r2b_t06_unresolved_site_fails_closed():
    row = deepcopy(discover_t06_call_sites(REPO_ROOT)[0])
    row["classification"] = "UNRESOLVED"
    errors = validate_t06_inventory([row], discover_t06_route_authority_map(REPO_ROOT))
    assert "TAP-R2B-T06-UNRESOLVED-SITE" in errors


def test_r2b_t06_incomplete_authority_map_fails_closed():
    rows = discover_t06_call_sites(REPO_ROOT)
    authority = deepcopy(discover_t06_route_authority_map(REPO_ROOT))
    authority[0].pop("deny_path")
    assert "TAP-R2B-T06-INCOMPLETE-AUTHORITY-MAP" in validate_t06_inventory(rows, authority)
