#!/usr/bin/env python3
# Copyright (c) 2026 Ivan Kotov. All rights reserved.
# Frozen source artifacts retain their original rights.
"""Regression checks for CI v1.0.0 Corrigendum 01. Standard library only (git optional).

These are offline maintenance checks, not CI runtime or evaluator qualification.
Usage: python3 -B tools/test_regressions.py --agi-root PATH --site-root PATH
"""
from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parent))
import apply_corrections as ac  # noqa: E402

RESIDUAL_ALLOWED = {("kot141078.github.io", "publications/continuity-instrument-v1-0-0/index.html"): 1}
FORBIDDEN_AFTER = ("No public canonical definition", "does not expand the name", "expand the BACON name",
                   "assign semantics to BACON", "Reserved integration name")


def check(condition: bool, label: str, results: list) -> None:
    results.append(("PASS" if condition else "FAIL", label))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--agi-root", required=True, type=Path)
    parser.add_argument("--site-root", required=True, type=Path)
    args = parser.parse_args()
    roots = {"advanced-global-intelligence": args.agi_root, "kot141078.github.io": args.site_root}
    spec = ac.load_spec(ac.DEFAULT_SPEC)
    results: list = []
    with tempfile.TemporaryDirectory() as tmp:
        out = Path(tmp) / "out"
        report = ac.run(ac.DEFAULT_SPEC, roots, out)
        check(report["files_corrected"] == 17 and report["edits_applied"] == 25, "17 files, 25 edits", results)
        for item in spec["corrected_files"]:
            data = (out / item["repo"] / item["path"]).read_bytes()
            check(ac.sha256(data) == item["sha256"], f"corrected hash {item['path']}", results)
            text = data.decode("utf-8")
            allowed = RESIDUAL_ALLOWED.get((item["repo"], item["path"]), 0)
            check(text.count("BACON") == allowed, f"residual BACON={allowed} in {item['path']}", results)
            check(not any(phrase in text for phrase in FORBIDDEN_AFTER), f"no void phrases in {item['path']}", results)
            if item["path"].endswith(".json"):
                try:
                    json.loads(text)
                    ok = True
                except json.JSONDecodeError:
                    ok = False
                check(ok, f"valid JSON {item['path']}", results)
        meaning = [p for p in spec["patches"] if p["class"] == "meaning"]
        check(all("10.5281/zenodo.18933553" in p["new"] or "adapter" in p["new"] for p in meaning),
              "meaning edits cite Beacon DOI or the adapter boundary", results)
        # inputs untouched
        for binding in spec["source_bindings"]:
            data = (roots[binding["repo"]] / binding["path"]).read_bytes()
            check(ac.sha256(data) == binding["sha256"], f"input untouched {binding['path']}", results)
        # second application on corrected copies is refused
        corrected_roots = {repo: out / repo for repo in roots}
        try:
            ac.run(ac.DEFAULT_SPEC, corrected_roots, Path(tmp) / "again")
            check(False, "re-application refused", results)
        except ac.CorrectionError:
            check(True, "re-application refused", results)
        # existing output refused
        try:
            ac.run(ac.DEFAULT_SPEC, roots, out)
            check(False, "existing output refused", results)
        except ac.CorrectionError:
            check(True, "existing output refused", results)
        # diffs apply cleanly to the predecessor trees (read-only check)
        git = shutil.which("git")
        for repo, root in roots.items():
            diff = out / f"{repo}.diff"
            if git and (root / ".git").exists():
                proc = subprocess.run([git, "-C", str(root), "apply", "--check", str(diff)],
                                      capture_output=True, text=True)
                check(proc.returncode == 0, f"git apply --check {repo}.diff", results)
            else:
                results.append(("SKIP", f"git apply --check {repo}.diff (no git checkout)"))
    for status, label in results:
        print(f"{status} {label}")
    failed = sum(1 for status, _ in results if status == "FAIL")
    print(f"SUMMARY pass={sum(1 for s, _ in results if s == 'PASS')} fail={failed} "
          f"skip={sum(1 for s, _ in results if s == 'SKIP')}")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
