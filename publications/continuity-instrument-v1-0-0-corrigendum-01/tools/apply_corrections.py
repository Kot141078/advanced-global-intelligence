#!/usr/bin/env python3
# Copyright (c) 2026 Ivan Kotov. All rights reserved.
# Frozen source artifacts retain their original rights.
"""Apply CI v1.0.0 Corrigendum 01 to copies of the predecessor files.

Standard library only. Inputs are never modified. The output directory must not exist.
Every predecessor must match its recorded SHA-256 and size; every edit must match exactly the
expected number of occurrences; every corrected file must match its recorded SHA-256. Any
mismatch stops the run before anything is written.

Output:
  OUTPUT/<repo>/<path>            corrected copies
  OUTPUT/<repo>.diff              historical comparison evidence; do not apply to the v1.0.0 mirror
  OUTPUT/APPLY_REPORT.json        what was checked and written

The deposited v1.0.0 mirror remains immutable. A generated diff is not deployment authority.

Usage:
  python3 tools/apply_corrections.py --agi-root PATH --site-root PATH --output DIR [--spec patches/corrections.json]
"""
from __future__ import annotations

import argparse
import difflib
import hashlib
import json
import os
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
DEFAULT_SPEC = HERE.parent / "patches" / "corrections.json"
REPO_ARGS = {"advanced-global-intelligence": "agi_root", "kot141078.github.io": "site_root"}


class CorrectionError(RuntimeError):
    pass


def sha256(blob: bytes) -> str:
    return hashlib.sha256(blob).hexdigest()


def load_spec(path: Path) -> dict:
    try:
        spec = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise CorrectionError(f"cannot read spec {path}: {exc}") from exc
    for key in ("source_bindings", "patches", "corrected_files"):
        if not isinstance(spec.get(key), list) or not spec[key]:
            raise CorrectionError(f"spec field {key} missing or empty")
    return spec


def compute(spec: dict, roots: dict[str, Path]) -> dict[tuple[str, str], tuple[bytes, bytes]]:
    """Return {(repo, path): (before, after)} after all checks; raises on any mismatch."""
    expected_after = {(c["repo"], c["path"]): c for c in spec["corrected_files"]}
    result: dict[tuple[str, str], list] = {}
    for binding in spec["source_bindings"]:
        repo, rel = binding["repo"], binding["path"]
        if repo not in roots:
            raise CorrectionError(f"no root given for repository {repo}")
        source = roots[repo] / rel
        try:
            before = source.read_bytes()
        except OSError as exc:
            raise CorrectionError(f"cannot read {source}: {exc}") from exc
        if len(before) != binding["size_bytes"] or sha256(before) != binding["sha256"]:
            raise CorrectionError(f"predecessor bytes differ for {repo}/{rel} (already corrected or changed upstream)")
        result[(repo, rel)] = [before, before.decode("utf-8")]
    for patch in spec["patches"]:
        key = (patch["repo"], patch["path"])
        if key not in result:
            raise CorrectionError(f"{patch['finding']}: file not bound in source_bindings")
        text = result[key][1]
        found = text.count(patch["old"])
        if found != patch["expected_occurrences"]:
            raise CorrectionError(f"{patch['finding']}: expected {patch['expected_occurrences']} occurrence(s), found {found}")
        result[key][1] = text.replace(patch["old"], patch["new"])
    final: dict[tuple[str, str], tuple[bytes, bytes]] = {}
    for key, (before, text) in result.items():
        after = text.encode("utf-8")
        want = expected_after.get(key)
        if want is None or len(after) != want["size_bytes"] or sha256(after) != want["sha256"]:
            raise CorrectionError(f"corrected bytes for {key[0]}/{key[1]} do not match the spec")
        final[key] = (before, after)
    if set(final) != set(expected_after):
        raise CorrectionError("corrected_files and source_bindings cover different files")
    return final


def unified(repo_files: list[tuple[str, bytes, bytes]]) -> str:
    chunks = []
    for rel, before, after in sorted(repo_files):
        diff = difflib.unified_diff(before.decode("utf-8").splitlines(keepends=True),
                                    after.decode("utf-8").splitlines(keepends=True),
                                    fromfile=f"a/{rel}", tofile=f"b/{rel}", n=2)
        lines = list(diff)
        if lines:
            chunks.append(f"diff --git a/{rel} b/{rel}\n")
            for line in lines:
                chunks.append(line if line.endswith("\n") else line + "\n\\ No newline at end of file\n")
    return "".join(chunks)


def run(spec_path: Path, roots: dict[str, Path], output: Path) -> dict:
    if output.exists():
        raise CorrectionError(f"output {output} already exists; refusing to overwrite")
    spec = load_spec(spec_path)
    final = compute(spec, roots)
    for repo, root in roots.items():
        if output.resolve().is_relative_to(root.resolve()):
            raise CorrectionError(f"output must be outside the input repository {repo}")
    output.mkdir(parents=True)
    by_repo: dict[str, list] = {}
    for (repo, rel), (before, after) in final.items():
        target = output / repo / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(after)
        by_repo.setdefault(repo, []).append((rel, before, after))
    diffs = {}
    for repo, items in by_repo.items():
        text = unified(items)
        (output / f"{repo}.diff").write_text(text, encoding="utf-8")
        diffs[repo] = {"file": f"{repo}.diff", "sha256": sha256(text.encode("utf-8")), "files": len(items)}
    report = {"artifact": spec.get("artifact"), "spec_sha256": sha256(spec_path.read_bytes()),
              "files_corrected": len(final), "edits_applied": len(spec["patches"]), "diffs": diffs,
              "corrected": [{"repo": r, "path": p, "sha256": sha256(a)} for (r, p), (_, a) in sorted(final.items())]}
    (output / "APPLY_REPORT.json").write_text(json.dumps(report, indent=1) + "\n", encoding="utf-8")
    return report


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--agi-root", required=True, type=Path, help="checkout of Kot141078/advanced-global-intelligence")
    parser.add_argument("--site-root", required=True, type=Path, help="checkout of Kot141078/kot141078.github.io")
    parser.add_argument("--output", required=True, type=Path, help="new directory for corrected copies and diffs")
    parser.add_argument("--spec", type=Path, default=DEFAULT_SPEC)
    args = parser.parse_args(argv)
    roots = {repo: getattr(args, attr) for repo, attr in REPO_ARGS.items()}
    try:
        report = run(args.spec, roots, args.output)
    except CorrectionError as exc:
        print(f"REFUSED: {exc}", file=sys.stderr)
        return 2
    print(json.dumps({k: report[k] for k in ("files_corrected", "edits_applied", "diffs")}, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main())
