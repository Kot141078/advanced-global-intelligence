"""Bounded non-formation receipts for refused or held actions."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any, List
from uuid import uuid4

from .models import NonFormationReceipt, ProtectedConsequenceClass, ReceiptType, TransitionWitness

EMAIL_EFFECTORS = {"smtp_send", "gmail_send", "mail_api_send", "outbound_queue"}


@dataclass
class NonFormationValidation:
    valid: bool
    reasons: List[str] = field(default_factory=list)
    bounded_only: bool = True

    def to_dict(self) -> dict[str, Any]:
        return {
            "valid": self.valid,
            "reasons": list(self.reasons),
            "bounded_only": self.bounded_only,
        }


def _utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def _mentions_bounded(limitations: list[str]) -> bool:
    return any("bounded" in item.lower() and "universal" in item.lower() for item in limitations)


def validate_non_formation_receipt(receipt: NonFormationReceipt) -> NonFormationValidation:
    reasons: list[str] = []

    if receipt.receipt_type is not ReceiptType.NFORM:
        reasons.append("receipt_type_not_nform")
    if receipt.effect_formed is not False:
        reasons.append("effect_formed_true")
    if not receipt.declared_routes_checked and not receipt.declared_effectors_checked:
        reasons.append("no_route_or_effector_checked")
    if not _mentions_bounded(receipt.limitations):
        reasons.append("limitations_do_not_state_bounded_not_universal")

    has_critical_unknown = any(
        (isinstance(item, dict) and item.get("critical") is True)
        or (isinstance(item, str) and "critical" in item.lower())
        for item in receipt.unknowns
    )
    if has_critical_unknown and any("complete" in item.lower() for item in receipt.limitations):
        reasons.append("critical_unknown_claimed_complete")

    if receipt.protected_consequence_class is ProtectedConsequenceClass.EMAIL_SEND:
        if not EMAIL_EFFECTORS.intersection(set(receipt.declared_effectors_checked)):
            reasons.append("email_send_missing_known_effector_check")
        if not receipt.retry_paths_checked:
            reasons.append("email_send_missing_retry_path_check")

    return NonFormationValidation(valid=not reasons, reasons=reasons, bounded_only=True)


def build_non_formation_receipt(
    witness: TransitionWitness,
    *,
    reason: str,
    receipt_id: str | None = None,
) -> NonFormationReceipt:
    route_name = str(witness.route.get("name") or witness.route.get("route_id") or "declared_route")
    effector_name = str(
        witness.effector.get("name") or witness.effector.get("effector_id") or "declared_effector"
    )
    return NonFormationReceipt(
        receipt_id=receipt_id or f"nform-{uuid4()}",
        witness_id=witness.witness_id,
        created_at=_utc_now(),
        protected_consequence_class=witness.protected_consequence_class,
        refused_or_held_reason=reason,
        declared_routes_checked=[route_name] if route_name else [],
        declared_effectors_checked=[effector_name] if effector_name else [],
        queues_checked=list(witness.route.get("queues_checked") or []),
        retry_paths_checked=list(witness.route.get("retry_paths_checked") or ["retry_paths_absent"]),
        side_channels_checked=list(witness.route.get("side_channels_checked") or []),
        effect_formed=False,
        unknowns=list(witness.unknowns),
        receipt_type=ReceiptType.NFORM,
        replay_anchor=witness.replay_anchor,
        limitations=["bounded receipt, not universal non-formation proof"],
    )

