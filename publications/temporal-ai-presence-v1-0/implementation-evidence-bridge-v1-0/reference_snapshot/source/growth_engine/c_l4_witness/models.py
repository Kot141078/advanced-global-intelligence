"""Data models for the C-L4 witness development layer."""

from __future__ import annotations

from dataclasses import asdict, dataclass, field, is_dataclass
from enum import Enum
from typing import Any, Dict, List, Mapping, Optional


class _StringEnum(str, Enum):
    def __str__(self) -> str:
        return self.value


class PermissionState(_StringEnum):
    PASS = "PASS"
    HOLD = "HOLD"
    ASK_OWNER = "ASK_OWNER"
    REFUSE = "REFUSE"
    FREEZE = "FREEZE"
    NO_BIND = "NO_BIND"
    IND = "IND"
    FAIL_CLOSED = "FAIL_CLOSED"
    REVALIDATE_REQUIRED = "REVALIDATE_REQUIRED"


class ReceiptType(_StringEnum):
    BIND = "BIND"
    HOLD = "HOLD"
    REFUSE = "REFUSE"
    REVOKE = "REVOKE"
    NFORM = "NFORM"
    IND = "IND"
    CORRECTED = "CORRECTED"


class EvidenceLevel(_StringEnum):
    C_E0_GENERATED = "C_E0_GENERATED"
    C_E1_STRUCTURAL_CHECKED = "C_E1_STRUCTURAL_CHECKED"
    C_E2_SOURCE_VERIFIED = "C_E2_SOURCE_VERIFIED"
    C_E3_OWNER_DISPOSITION = "C_E3_OWNER_DISPOSITION"
    C_E4_INDEPENDENT_REVIEWED = "C_E4_INDEPENDENT_REVIEWED"
    C_E5_EXTERNALLY_REPLAYED = "C_E5_EXTERNALLY_REPLAYED"
    C_E6_OPERATIONALLY_VALIDATED = "C_E6_OPERATIONALLY_VALIDATED"


class ContinuityClaimStatus(_StringEnum):
    CONTINUITY_SUPPORTED = "CONTINUITY_SUPPORTED"
    REPLAY_ONLY = "REPLAY_ONLY"
    ARCHIVE_ONLY = "ARCHIVE_ONLY"
    FORKED = "FORKED"
    RESTORE_PENDING_WITNESS = "RESTORE_PENDING_WITNESS"
    DECLARED_NOT_GROUNDED = "DECLARED_NOT_GROUNDED"
    REFUSE_CONTINUITY = "REFUSE_CONTINUITY"


class ProtectedConsequenceClass(_StringEnum):
    FILE_WRITE = "FILE_WRITE"
    FILE_OVERWRITE = "FILE_OVERWRITE"
    EMAIL_SEND = "EMAIL_SEND"
    API_CALL = "API_CALL"
    MEMORY_REWRITE = "MEMORY_REWRITE"
    CONFIG_CHANGE = "CONFIG_CHANGE"
    P2P_SYNC = "P2P_SYNC"
    PHYSICAL_ACTION = "PHYSICAL_ACTION"
    PAYMENT_OR_CAPITAL_MOVEMENT = "PAYMENT_OR_CAPITAL_MOVEMENT"
    PUBLICATION = "PUBLICATION"
    UNKNOWN = "UNKNOWN"


def _enum_or_default(enum_cls: type[_StringEnum], value: Any, default: _StringEnum) -> _StringEnum:
    if isinstance(value, enum_cls):
        return value
    if value is None:
        return default
    try:
        return enum_cls(str(value))
    except ValueError:
        return default


def _mapping(value: Any) -> Dict[str, Any]:
    if isinstance(value, Mapping):
        return dict(value)
    return {}


def _list(value: Any) -> List[Any]:
    if value is None:
        return []
    if isinstance(value, list):
        return value
    return [value]


@dataclass
class TransitionWitness:
    witness_id: str
    created_at: str
    actor_id: str
    principal_id: str
    proposed_movement: str
    protected_consequence_class: ProtectedConsequenceClass
    context: Dict[str, Any] = field(default_factory=dict)
    authority: Dict[str, Any] = field(default_factory=dict)
    evidence: Dict[str, Any] = field(default_factory=dict)
    scope: Dict[str, Any] = field(default_factory=dict)
    route: Dict[str, Any] = field(default_factory=dict)
    effector: Dict[str, Any] = field(default_factory=dict)
    unknowns: List[Any] = field(default_factory=list)
    permission_state: PermissionState = PermissionState.IND
    evidence_level: EvidenceLevel = EvidenceLevel.C_E0_GENERATED
    receipt: ReceiptType = ReceiptType.IND
    replay_anchor: Optional[str] = None
    correction_link: Optional[str] = None
    limitations: List[str] = field(default_factory=list)

    @classmethod
    def from_mapping(cls, data: Mapping[str, Any]) -> "TransitionWitness":
        return cls(
            witness_id=str(data.get("witness_id") or ""),
            created_at=str(data.get("created_at") or ""),
            actor_id=str(data.get("actor_id") or ""),
            principal_id=str(data.get("principal_id") or ""),
            proposed_movement=str(data.get("proposed_movement") or ""),
            protected_consequence_class=_enum_or_default(
                ProtectedConsequenceClass,
                data.get("protected_consequence_class"),
                ProtectedConsequenceClass.UNKNOWN,
            ),
            context=_mapping(data.get("context")),
            authority=_mapping(data.get("authority")),
            evidence=_mapping(data.get("evidence")),
            scope=_mapping(data.get("scope")),
            route=_mapping(data.get("route")),
            effector=_mapping(data.get("effector")),
            unknowns=_list(data.get("unknowns")),
            permission_state=_enum_or_default(
                PermissionState, data.get("permission_state"), PermissionState.IND
            ),
            evidence_level=_enum_or_default(
                EvidenceLevel, data.get("evidence_level"), EvidenceLevel.C_E0_GENERATED
            ),
            receipt=_enum_or_default(ReceiptType, data.get("receipt"), ReceiptType.IND),
            replay_anchor=data.get("replay_anchor"),
            correction_link=data.get("correction_link"),
            limitations=[str(item) for item in _list(data.get("limitations"))],
        )

    def to_dict(self) -> Dict[str, Any]:
        return to_plain_data(self)


@dataclass
class NonFormationReceipt:
    receipt_id: str
    witness_id: str
    created_at: str
    protected_consequence_class: ProtectedConsequenceClass
    refused_or_held_reason: str
    declared_routes_checked: List[str] = field(default_factory=list)
    declared_effectors_checked: List[str] = field(default_factory=list)
    queues_checked: List[str] = field(default_factory=list)
    retry_paths_checked: List[str] = field(default_factory=list)
    side_channels_checked: List[str] = field(default_factory=list)
    effect_formed: bool = False
    unknowns: List[Any] = field(default_factory=list)
    receipt_type: ReceiptType = ReceiptType.NFORM
    replay_anchor: Optional[str] = None
    limitations: List[str] = field(default_factory=list)

    @classmethod
    def from_mapping(cls, data: Mapping[str, Any]) -> "NonFormationReceipt":
        return cls(
            receipt_id=str(data.get("receipt_id") or ""),
            witness_id=str(data.get("witness_id") or ""),
            created_at=str(data.get("created_at") or ""),
            protected_consequence_class=_enum_or_default(
                ProtectedConsequenceClass,
                data.get("protected_consequence_class"),
                ProtectedConsequenceClass.UNKNOWN,
            ),
            refused_or_held_reason=str(data.get("refused_or_held_reason") or ""),
            declared_routes_checked=[str(item) for item in _list(data.get("declared_routes_checked"))],
            declared_effectors_checked=[
                str(item) for item in _list(data.get("declared_effectors_checked"))
            ],
            queues_checked=[str(item) for item in _list(data.get("queues_checked"))],
            retry_paths_checked=[str(item) for item in _list(data.get("retry_paths_checked"))],
            side_channels_checked=[str(item) for item in _list(data.get("side_channels_checked"))],
            effect_formed=bool(data.get("effect_formed")),
            unknowns=_list(data.get("unknowns")),
            receipt_type=_enum_or_default(ReceiptType, data.get("receipt_type"), ReceiptType.NFORM),
            replay_anchor=data.get("replay_anchor"),
            limitations=[str(item) for item in _list(data.get("limitations"))],
        )

    def to_dict(self) -> Dict[str, Any]:
        return to_plain_data(self)


@dataclass
class MaterialChangeEvent:
    event_id: str
    witness_id: str
    created_at: str
    changed_fields: List[str]
    reason: str
    previous_permission_state: PermissionState
    new_permission_state: PermissionState
    revalidation_required: bool
    correction_link: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        return to_plain_data(self)


@dataclass
class ContinuityResetAssessment:
    assessment_id: str
    created_at: str
    claim_type: str
    parent_witness: Optional[str]
    archive_reference: Optional[str]
    replay_reference: Optional[str]
    fork_reference: Optional[str]
    restoration_reference: Optional[str]
    status: ContinuityClaimStatus
    reason: str
    limitations: List[str] = field(default_factory=list)

    @classmethod
    def from_mapping(cls, data: Mapping[str, Any]) -> "ContinuityResetAssessment":
        return cls(
            assessment_id=str(data.get("assessment_id") or ""),
            created_at=str(data.get("created_at") or ""),
            claim_type=str(data.get("claim_type") or ""),
            parent_witness=data.get("parent_witness"),
            archive_reference=data.get("archive_reference"),
            replay_reference=data.get("replay_reference"),
            fork_reference=data.get("fork_reference"),
            restoration_reference=data.get("restoration_reference"),
            status=_enum_or_default(
                ContinuityClaimStatus,
                data.get("status"),
                ContinuityClaimStatus.DECLARED_NOT_GROUNDED,
            ),
            reason=str(data.get("reason") or ""),
            limitations=[str(item) for item in _list(data.get("limitations"))],
        )

    def to_dict(self) -> Dict[str, Any]:
        return to_plain_data(self)


def to_plain_data(value: Any) -> Any:
    if isinstance(value, Enum):
        return value.value
    if is_dataclass(value):
        return {key: to_plain_data(item) for key, item in asdict(value).items()}
    if isinstance(value, dict):
        return {str(key): to_plain_data(item) for key, item in value.items()}
    if isinstance(value, list):
        return [to_plain_data(item) for item in value]
    return value

