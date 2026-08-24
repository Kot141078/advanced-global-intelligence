"""JSONL append helper for C-L4 local smoke outputs."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from .models import to_plain_data


def append_jsonl(path: str | Path, record: Any) -> None:
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    with target.open("a", encoding="utf-8", newline="\n") as handle:
        handle.write(json.dumps(to_plain_data(record), ensure_ascii=False, sort_keys=True))
        handle.write("\n")

