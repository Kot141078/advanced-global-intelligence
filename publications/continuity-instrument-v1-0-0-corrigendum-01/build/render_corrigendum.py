#!/usr/bin/env python3
# Copyright (c) 2026 Ivan Kotov. All rights reserved.
# Frozen source artifacts retain their original rights.
"""Render the corrigendum's file table from the reviewed correction specification.

Usage: python3 -B build/render_corrigendum.py TEMPLATE SPEC OUT_MD
The output must be a new file. This maintenance tool performs no publication action.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path

EXPECTED_SPEC_SHA256 = "9ac75661c364d139c8f4c2f3656a285d63fa89d6e34aac6786b4d72ad6e065dd"
MARKER = "<!--CORRECTION_TABLE-->"


def correction_table(spec: dict) -> str:
    after = {(c["repo"], c["path"]): c["sha256"] for c in spec["corrected_files"]}
    rows = [
        "| Repository | File (under publications/continuity-instrument-v1-0-0/) | Predecessor | Corrected | Edits |",
        "|---|---|---|---|---|",
    ]
    for binding in spec["source_bindings"]:
        key = (binding["repo"], binding["path"])
        edits = [p for p in spec["patches"] if (p["repo"], p["path"]) == key]
        token_count = sum(p["class"] == "token" for p in edits)
        meaning_count = len(edits) - token_count
        classes = " ".join(
            item for item in (f"{token_count}T" if token_count else "", f"{meaning_count}M" if meaning_count else "")
            if item
        )
        relative = binding["path"].replace("publications/continuity-instrument-v1-0-0/", "", 1)
        repo = "mirror" if binding["repo"] == "advanced-global-intelligence" else "site"
        rows.append(
            f"| {repo} | `{relative}` | `{binding['sha256'][:16]}` | `{after[key][:16]}` | {classes} |"
        )
    return "\n".join(rows)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("template", type=Path)
    parser.add_argument("spec", type=Path)
    parser.add_argument("out_md", type=Path)
    args = parser.parse_args()
    if args.out_md.exists():
        raise ValueError(f"output {args.out_md} exists; refusing to overwrite")
    raw = args.spec.read_bytes()
    if hashlib.sha256(raw).hexdigest() != EXPECTED_SPEC_SHA256:
        raise ValueError("correction specification differs from the reviewed bytes")
    spec = json.loads(raw)
    template = args.template.read_bytes().decode("utf-8")
    if template.count(MARKER) != 1:
        raise ValueError("template must contain exactly one correction-table marker")
    payload = template.replace(MARKER, correction_table(spec)).encode("utf-8")
    with args.out_md.open("xb") as handle:
        handle.write(payload)
    print(json.dumps({"rows": len(spec["source_bindings"]), "bytes": len(payload),
                      "sha256": hashlib.sha256(payload).hexdigest()}))
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (OSError, UnicodeError, ValueError, KeyError, TypeError) as exc:
        print(f"REFUSED: {exc}", file=sys.stderr)
        sys.exit(2)
