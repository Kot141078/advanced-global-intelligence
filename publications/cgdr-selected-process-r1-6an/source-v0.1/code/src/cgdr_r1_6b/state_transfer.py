from __future__ import annotations

import base64
import json
from copy import deepcopy
from typing import Any

from .common import canonical_bytes, canonical_hash


MATERIAL_FIELDS = (
    "source_id",
    "source_hash",
    "qsf",
    "duty",
    "custody",
    "role",
    "receiver_basis",
    "arq_standing",
    "quarantined_memory",
    "a6_conditions",
    "l4",
    "toy_lineage",
    "attestation_history",
    "handoff_authority",
)


def material_projection(source: dict[str, Any]) -> dict[str, Any]:
    """Source-derived state carried by workers; current authority stays external."""
    return {field: deepcopy(source[field]) for field in MATERIAL_FIELDS}


def freeze_state(source: dict[str, Any]) -> dict[str, Any]:
    state = material_projection(source)
    raw = canonical_bytes(state)
    return {
        "state": state,
        "bytes": raw,
        "state_b64": base64.b64encode(raw).decode("ascii"),
        "state_sha256": canonical_hash(state),
        "source_hash": source["source_hash"],
        "material_fields": list(MATERIAL_FIELDS),
    }


def decode_state_b64(encoded: Any) -> tuple[bytes | None, dict[str, Any] | None, list[str]]:
    issues: list[str] = []
    if not isinstance(encoded, str):
        return None, None, ["STATE_BYTES_MISSING"]
    try:
        raw = base64.b64decode(encoded.encode("ascii"), validate=True)
        state = json.loads(raw.decode("utf-8", errors="strict"))
    except (ValueError, UnicodeDecodeError, json.JSONDecodeError):
        return None, None, ["STATE_BYTES_INVALID"]
    if not isinstance(state, dict):
        return raw, None, ["STATE_NOT_OBJECT"]
    return raw, state, issues


def validate_state_bytes(
    raw: bytes,
    source: dict[str, Any],
    *,
    stated_hash: str | None = None,
) -> dict[str, Any]:
    issues: list[str] = []
    try:
        observed = json.loads(raw.decode("utf-8", errors="strict"))
    except (UnicodeDecodeError, json.JSONDecodeError):
        return {"status": "FAIL", "issues": ["STATE_BYTES_INVALID"], "state": None}
    if not isinstance(observed, dict):
        return {"status": "FAIL", "issues": ["STATE_NOT_OBJECT"], "state": None}
    observed_hash = canonical_hash(observed)
    if raw != canonical_bytes(observed):
        issues.append("STATE_BYTES_NOT_JCS")
    if stated_hash is not None and stated_hash != observed_hash:
        issues.append("STATE_HASH_MISMATCH")
    expected = material_projection(source)
    missing = [field for field in MATERIAL_FIELDS if field not in observed]
    extra = sorted(set(observed) - set(MATERIAL_FIELDS))
    if missing:
        issues.extend(f"MISSING_MATERIAL_FIELD:{field}" for field in missing)
    if extra:
        issues.extend(f"UNDECLARED_STATE_FIELD:{field}" for field in extra)
    for field in MATERIAL_FIELDS:
        if field in observed and observed[field] != expected[field]:
            issues.append(f"MATERIAL_FIELD_MISMATCH:{field}")
    return {
        "status": "PASS" if not issues else "FAIL",
        "issues": sorted(set(issues)),
        "state": observed,
        "state_sha256": observed_hash,
        "source_hash": source.get("source_hash"),
    }


def validate_worker_checkpoint(
    event: dict[str, Any],
    source: dict[str, Any],
    *,
    expected_instance: str,
    minimum_seq: int = 1,
) -> dict[str, Any]:
    raw, _, decode_issues = decode_state_b64(event.get("state_b64"))
    issues = list(decode_issues)
    if event.get("event") != "CHECKPOINT":
        issues.append("CHECKPOINT_EVENT_MISSING")
    if event.get("instance_id") != expected_instance:
        issues.append("CHECKPOINT_INSTANCE_MISMATCH")
    if not isinstance(event.get("checkpoint_seq"), int) or event["checkpoint_seq"] < minimum_seq:
        issues.append("CHECKPOINT_SEQUENCE_INVALID")
    result = validate_state_bytes(raw or b"", source, stated_hash=event.get("state_sha256"))
    issues.extend(result["issues"])
    return {
        **result,
        "status": "PASS" if not issues else "FAIL",
        "issues": sorted(set(issues)),
        "checkpoint_seq": event.get("checkpoint_seq"),
        "instance_id": event.get("instance_id"),
    }


def validate_handoff_order(events: list[dict[str, Any]]) -> dict[str, Any]:
    order = {
        "LOAD_ACK": None,
        "CHECKPOINT": None,
        "SHAM_WAITING": None,
        "RELEASED": None,
        "CONTINUED": None,
        "EXIT_OBSERVED": None,
        "W1_START": None,
        "RESTORED": None,
    }
    for index, event in enumerate(events):
        kind = event.get("event") or event.get("kind")
        if kind in order and order[kind] is None:
            order[kind] = index
    required = ["LOAD_ACK", "CHECKPOINT", "SHAM_WAITING", "RELEASED", "CONTINUED", "EXIT_OBSERVED", "W1_START", "RESTORED"]
    issues = [f"MISSING_ORDER_EVENT:{name}" for name in required if order[name] is None]
    if not issues and [order[name] for name in required] != sorted(order[name] for name in required):
        issues.append("HANDOFF_CAUSAL_ORDER_INVALID")
    return {"status": "PASS" if not issues else "FAIL", "issues": issues, "positions": order}
