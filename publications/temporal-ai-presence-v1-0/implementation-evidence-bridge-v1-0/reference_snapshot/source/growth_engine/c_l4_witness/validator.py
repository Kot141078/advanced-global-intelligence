"""Validation rules for C-L4 transition witnesses."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, List

from .models import PermissionState, ProtectedConsequenceClass, ReceiptType, TransitionWitness


@dataclass
class ValidationResult:
    valid: bool
    permission_state: PermissionState
    receipt: ReceiptType
    reasons: List[str] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return {
            "valid": self.valid,
            "permission_state": self.permission_state.value,
            "receipt": self.receipt.value,
            "reasons": list(self.reasons),
        }


def _critical_unknowns(witness: TransitionWitness) -> bool:
    for item in witness.unknowns:
        if isinstance(item, dict) and item.get("critical") is True:
            return True
        if isinstance(item, str) and "critical" in item.lower():
            return True
    return False


def _declared_exists(value: dict[str, Any]) -> bool:
    if value.get("exists") is True:
        return True
    if value.get("declared") is True:
        return True
    return False


def _result(state: PermissionState, receipt: ReceiptType, reasons: List[str]) -> ValidationResult:
    return ValidationResult(valid=(state is PermissionState.PASS), permission_state=state, receipt=receipt, reasons=reasons)


def validate_transition_witness(witness: TransitionWitness) -> ValidationResult:
    reasons: List[str] = []

    if not witness.witness_id:
        reasons.append("missing_witness_id")
        witness.permission_state = PermissionState.FAIL_CLOSED
        witness.receipt = ReceiptType.IND
        return _result(witness.permission_state, witness.receipt, reasons)

    if not witness.actor_id:
        reasons.append("missing_actor_id")
        witness.permission_state = PermissionState.HOLD
        witness.receipt = ReceiptType.HOLD
        return _result(witness.permission_state, witness.receipt, reasons)

    if not witness.principal_id:
        reasons.append("missing_principal_id")
        witness.permission_state = PermissionState.HOLD
        witness.receipt = ReceiptType.HOLD
        return _result(witness.permission_state, witness.receipt, reasons)

    if witness.protected_consequence_class is ProtectedConsequenceClass.UNKNOWN:
        reasons.append("unknown_protected_consequence_class")
        witness.permission_state = PermissionState.NO_BIND
        witness.receipt = ReceiptType.IND
        return _result(witness.permission_state, witness.receipt, reasons)

    if witness.context.get("indeterminate") is True:
        reasons.append("indeterminate_state")
        witness.permission_state = PermissionState.IND
        witness.receipt = ReceiptType.IND
        return _result(witness.permission_state, witness.receipt, reasons)

    if witness.route.get("retry_queue_bypass") is True:
        reasons.append("retry_queue_bypass")
        witness.permission_state = PermissionState.FAIL_CLOSED
        witness.receipt = ReceiptType.IND
        return _result(witness.permission_state, witness.receipt, reasons)

    if witness.route.get("critical_unknown") is True or _critical_unknowns(witness):
        reasons.append("critical_unknown_route_or_state")
        witness.permission_state = PermissionState.NO_BIND
        witness.receipt = ReceiptType.IND
        return _result(witness.permission_state, witness.receipt, reasons)

    if witness.evidence.get("stale") is True:
        reasons.append("stale_evidence")
        witness.permission_state = PermissionState.HOLD
        witness.receipt = ReceiptType.HOLD
        return _result(witness.permission_state, witness.receipt, reasons)

    if witness.authority.get("valid") is not True:
        reasons.append("missing_or_invalid_authority")
        witness.permission_state = PermissionState.ASK_OWNER
        witness.receipt = ReceiptType.HOLD
        return _result(witness.permission_state, witness.receipt, reasons)

    if witness.scope.get("valid") is not True:
        reasons.append("missing_or_invalid_scope")
        witness.permission_state = PermissionState.HOLD
        witness.receipt = ReceiptType.HOLD
        return _result(witness.permission_state, witness.receipt, reasons)

    if not _declared_exists(witness.route):
        reasons.append("declared_route_missing")
        witness.permission_state = PermissionState.NO_BIND
        witness.receipt = ReceiptType.IND
        return _result(witness.permission_state, witness.receipt, reasons)

    if not _declared_exists(witness.effector):
        reasons.append("declared_effector_missing")
        witness.permission_state = PermissionState.NO_BIND
        witness.receipt = ReceiptType.IND
        return _result(witness.permission_state, witness.receipt, reasons)

    witness.permission_state = PermissionState.PASS
    witness.receipt = ReceiptType.BIND
    return _result(witness.permission_state, witness.receipt, reasons)

