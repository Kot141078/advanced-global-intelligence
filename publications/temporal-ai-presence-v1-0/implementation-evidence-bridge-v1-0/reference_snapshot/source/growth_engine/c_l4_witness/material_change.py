"""Material-change detection for C-L4 witnesses."""

from __future__ import annotations

from datetime import datetime, timezone
from typing import Any, Iterable, Mapping
from uuid import uuid4

from .models import MaterialChangeEvent, PermissionState, TransitionWitness

MATERIAL_FIELDS = (
    "authority",
    "scope",
    "route",
    "effector",
    "evidence.stale",
    "context",
    "context.tool_version",
    "context.model_version",
    "context.file_hash",
    "context.human_intent",
    "correction_link",
    "context.memory_state",
)


def _utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def _get_path(source: Any, path: str) -> Any:
    value: Any = source
    for part in path.split("."):
        if isinstance(value, TransitionWitness):
            value = getattr(value, part, None)
        elif isinstance(value, Mapping):
            value = value.get(part)
        else:
            return None
    return value


def changed_material_fields(
    previous: TransitionWitness,
    current: TransitionWitness,
    fields: Iterable[str] = MATERIAL_FIELDS,
) -> list[str]:
    changed: list[str] = []
    for field in fields:
        if _get_path(previous, field) != _get_path(current, field):
            changed.append(field)
    return changed


def detect_material_change(
    previous: TransitionWitness,
    current: TransitionWitness,
    *,
    event_id: str | None = None,
    created_at: str | None = None,
) -> MaterialChangeEvent:
    changed = changed_material_fields(previous, current)
    revalidate = bool(changed)
    return MaterialChangeEvent(
        event_id=event_id or f"mce-{uuid4()}",
        witness_id=previous.witness_id,
        created_at=created_at or _utc_now(),
        changed_fields=changed,
        reason="material_change_before_execution" if revalidate else "no_material_change_detected",
        previous_permission_state=previous.permission_state,
        new_permission_state=(
            PermissionState.REVALIDATE_REQUIRED if revalidate else previous.permission_state
        ),
        revalidation_required=revalidate,
        correction_link=current.correction_link or previous.correction_link,
    )

