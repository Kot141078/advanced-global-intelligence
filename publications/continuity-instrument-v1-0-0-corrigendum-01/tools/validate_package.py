#!/usr/bin/env python3
# Copyright (c) 2026 Ivan Kotov. All rights reserved.
# Frozen source artifacts retain their original rights.
"""Check sibling-package integrity and regenerate its frozen-source derivatives offline.

Usage: python3 -B tools/validate_package.py [--package-root PATH]
No repository mutation, network request, CI runtime or evaluator invocation is performed.
Temporary outputs are created outside the package and removed after the check.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path

EXPECTED_SPEC_SHA256 = "9ac75661c364d139c8f4c2f3656a285d63fa89d6e34aac6786b4d72ad6e065dd"


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def verify_checksums(root: Path) -> int:
    names = set()
    for line in (root / "SHA256SUMS.txt").read_text(encoding="utf-8").splitlines():
        match = re.fullmatch(r"([0-9a-f]{64})  (.+)", line)
        require(match is not None, "invalid SHA256SUMS row")
        expected, name = match.groups()
        relative = Path(name)
        require(not relative.is_absolute() and ".." not in relative.parts, f"unsafe checksum path: {name}")
        require(name != "SHA256SUMS.txt" and name not in names, f"duplicate or circular checksum path: {name}")
        target = root / relative
        require(target.resolve().is_relative_to(root), f"checksum path leaves the package: {name}")
        require(target.is_file() and digest(target) == expected, f"checksum mismatch: {name}")
        names.add(name)
    actual = {path.relative_to(root).as_posix() for path in root.rglob("*") if path.is_file()}
    actual.discard("SHA256SUMS.txt")
    require(names == actual, "SHA256SUMS coverage mismatch: " + str(sorted(names ^ actual)))
    return len(names)


def execute(script: Path, *args: Path) -> None:
    result = subprocess.run([sys.executable, "-B", str(script), *map(str, args)],
                            capture_output=True, text=True, timeout=60)
    require(result.returncode == 0,
            f"{script.name} failed: {(result.stderr or result.stdout).strip()}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--package-root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    root = args.package_root.resolve()
    spec_path = root / "patches/corrections.json"
    require(digest(spec_path) == EXPECTED_SPEC_SHA256, "correction specification identity mismatch")
    checksum_count = verify_checksums(root)
    spec = json.loads(spec_path.read_bytes())
    source = root / "source_snapshots"
    agi = source / "advanced-global-intelligence"
    site = source / "kot141078.github.io"
    with tempfile.TemporaryDirectory(prefix="ci-corrigendum-") as temporary:
        tmp = Path(temporary)
        rebuilt_spec = tmp / "corrections.json"
        execute(root / "build/build_spec.py", agi, site, rebuilt_spec)
        require(rebuilt_spec.read_bytes() == spec_path.read_bytes(), "regenerated spec differs")
        rebuilt_en = tmp / "CORRIGENDUM_EN.md"
        execute(root / "build/render_corrigendum.py", root / "build/CORRIGENDUM_EN.template.md",
                spec_path, rebuilt_en)
        require(rebuilt_en.read_bytes() == (root / "CORRIGENDUM_EN.md").read_bytes(),
                "regenerated EN corrigendum differs")
        output = tmp / "corrected"
        result = subprocess.run([sys.executable, "-B", str(root / "tools/apply_corrections.py"),
                                 "--agi-root", str(agi), "--site-root", str(site), "--output", str(output)],
                                capture_output=True, text=True, timeout=60)
        require(result.returncode == 0, f"correction regeneration failed: {result.stderr.strip()}")
        for item in spec["corrected_files"]:
            relative = Path(item["repo"]) / item["path"]
            require((output / relative).read_bytes() == (root / "corrected_text" / relative).read_bytes(),
                    f"corrected copy differs: {relative}")
        for repo in ("advanced-global-intelligence", "kot141078.github.io"):
            name = repo + ".diff"
            require((output / name).read_bytes() == (root / "patches" / name).read_bytes(),
                    f"historical comparison diff differs: {name}")
        require((output / "APPLY_REPORT.json").read_bytes() == (root / "evidence/APPLY_REPORT.json").read_bytes(),
                "regenerated apply report differs")
    for binding in spec["source_bindings"]:
        target = source / binding["repo"] / binding["path"]
        require(target.stat().st_size == binding["size_bytes"] and digest(target) == binding["sha256"],
                f"frozen input changed: {binding['repo']}/{binding['path']}")
    print(json.dumps({"status": "PASS", "scope": "offline package maintenance only",
                      "checksum_files": checksum_count, "spec_sha256": EXPECTED_SPEC_SHA256,
                      "spec_regeneration": "BYTE_EQUAL", "en_regeneration": "BYTE_EQUAL",
                      "corrected_files_byte_equal": len(spec["corrected_files"]),
                      "comparison_diffs_byte_equal": 2, "apply_report": "BYTE_EQUAL",
                      "frozen_input_hashes_match": len(spec["source_bindings"]),
                      "ci_runtime_or_evaluator_invoked": False}, indent=2))
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (OSError, UnicodeError, ValueError, KeyError, TypeError, subprocess.SubprocessError) as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        sys.exit(1)
