"""Structured fail-closed TAP validation errors."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, order=True)
class ValidationIssue:
    code: str
    path: str
    message: str

    def to_dict(self) -> dict[str, str]:
        return {"code": self.code, "path": self.path, "message": self.message}
