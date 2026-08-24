"""Replay and continuity helpers for the C-L4 layer."""

from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from typing import Any, Mapping
from uuid import uuid4

from .models import ContinuityClaimStatus, ContinuityResetAssessment, ReceiptType, to_plain_data


def canonical_json(obj: Any) -> str:
    return json.dumps(to_plain_data(obj), ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def sha256_digest(obj: Any) -> str:
    return hashlib.sha256(canonical_json(obj).encode("utf-8")).hexdigest()


def compare_digest(expected: str, actual: str) -> dict[str, Any]:
    match = expected == actual
    return {
        "expected": expected,
        "actual": actual,
        "match": match,
        "receipt_type": ReceiptType.BIND.value if match else ReceiptType.CORRECTED.value,
        "permission_state": "PASS" if match else "FAIL_CLOSED",
    }


def _utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def assess_continuity_reset(data: Mapping[str, Any]) -> ContinuityResetAssessment:
    claim_type = str(data.get("claim_type") or "")
    parent = data.get("parent_witness")
    archive = data.get("archive_reference")
    replay = data.get("replay_reference")
    fork = data.get("fork_reference")
    restoration = data.get("restoration_reference")

    if fork:
        status = ContinuityClaimStatus.FORKED
        reason = "fork_reference_declared"
    elif not parent:
        status = ContinuityClaimStatus.DECLARED_NOT_GROUNDED
        reason = "missing_parent_witness"
    elif archive and "continuity" in claim_type.lower() and not replay:
        status = ContinuityClaimStatus.ARCHIVE_ONLY
        reason = "archive_reference_is_not_continuity"
    elif restoration and not replay:
        status = ContinuityClaimStatus.RESTORE_PENDING_WITNESS
        reason = "restoration_requires_replay_or_parent_witness"
    elif replay and parent:
        status = ContinuityClaimStatus.REPLAY_ONLY
        reason = "replay_present_but_not_operational_continuity"
    else:
        status = ContinuityClaimStatus.REFUSE_CONTINUITY
        reason = "continuity_claim_not_supported"

    return ContinuityResetAssessment(
        assessment_id=str(data.get("assessment_id") or f"cra-{uuid4()}"),
        created_at=str(data.get("created_at") or _utc_now()),
        claim_type=claim_type,
        parent_witness=parent,
        archive_reference=archive,
        replay_reference=replay,
        fork_reference=fork,
        restoration_reference=restoration,
        status=status,
        reason=reason,
        limitations=["classification only; no live continuity claim"],
    )

