#!/usr/bin/env python3
# Copyright (c) 2026 Ivan Kotov. All rights reserved.
# Frozen source artifacts retain their original rights.
"""Author the CI v1.0.0 Corrigendum 01 correction spec (patches/corrections.json).

Reads the exact predecessor bytes from local checkouts, applies each edit once in memory to
confirm the expected occurrence counts, and records predecessor and corrected SHA-256.
Usage: python3 -I build_spec.py AGI_ROOT SITE_ROOT OUT_JSON
"""
import argparse
import hashlib
import json
import os
import sys
from pathlib import Path

EXPECTED_SPEC_SHA256 = "9ac75661c364d139c8f4c2f3656a285d63fa89d6e34aac6786b4d72ad6e065dd"
COMMITS = {"advanced-global-intelligence": "bb062414b598afae970bef37ce7489433a51868d",
           "kot141078.github.io": "f77956b4dc45583d4b271c0f4499f0bbdab41e16"}
B = "publications/continuity-instrument-v1-0-0/"
SRC = B + "package/source_original/Continuity_Instrument_v1.0.0/"
ED = B + "package/editorial_sources/"
REF = "Beacon (Beacon Profile v0.1, DOI 10.5281/zenodo.18933553)"
AGI, SITE = "advanced-global-intelligence", "kot141078.github.io"

ONLY_TARGET_OLD = "BACON is only a future integration target. No public canonical definition or compatibility result is claimed."
ONLY_TARGET_NEW = f"{REF} is only a future integration target. No CI-to-Beacon adapter or compatibility result is claimed."
LISTED_OLD = ("BACON is listed only as a future integration target. This package does not expand the name, "
              "assign a public canonical definition, or claim technical compatibility.")
LISTED_NEW = f"{REF} is listed only as a future integration target. This package defines no CI-to-Beacon mapping and claims no technical compatibility."
GLOSS_OLD = ("**BACON**  \nA future integration target only. No public canonical definition was found for this package, "
             "so the name is not expanded and no technical semantics are assigned to it here.")
GLOSS_NEW = ("**Beacon**  \nBeacon Profile v0.1, a separately published recognition profile (DOI 10.5281/zenodo.18933553), "
             "named here as a conceptual alignment and a future integration target only. This package defines no "
             "CI-to-Beacon mapping and assigns no Beacon semantics to any CI field.")
MAPPED_OLD = "The output is designed so that CI can later be mapped into BACON through an explicit, versioned adapter."
MAPPED_NEW = f"The output is designed so that CI can later be mapped into {REF} through an explicit, versioned adapter."
DRAFT_OLD = "This draft does not implement that adapter, expand the BACON name, assign semantics to BACON, or claim compatibility with it."
DRAFT_NEW = "This draft does not implement that adapter, assign Beacon semantics to any CI field, or claim compatibility with Beacon."
CLAIM_OLD = ("| CI is compatible with BACON. | A separately defined, versioned adapter and acceptance evidence. | "
             "Not established. | BACON remains a future integration boundary. |")
CLAIM_NEW = CLAIM_OLD.replace("BACON", "Beacon")

PATCHES = [
    (AGI, B + "README.md", "token", "general evaluator validity, or BACON compatibility.", "general evaluator validity, or Beacon compatibility."),
    (AGI, B + "package/ZENODO_DESCRIPTION.txt", "token", "scientific qualification or BACON compatibility.", "scientific qualification or Beacon compatibility."),
    (AGI, ED + "CI_EXPLAINED_EN.md", "token", "The source package also names BACON as a future integration target.",
     f"The source package also names {REF} as a future integration target."),
    (AGI, ED + "EVIDENCE_CLAIMS_AND_LIMITATIONS.md", "token", CLAIM_OLD, CLAIM_NEW),
    (AGI, ED + "EVIDENCE_CLAIMS_AND_LIMITATIONS.md", "meaning", ONLY_TARGET_OLD, ONLY_TARGET_NEW),
    (AGI, ED + "EVIDENCE_CLAIMS_AND_LIMITATIONS.md", "token", "\n- BACON compatibility\n", "\n- Beacon compatibility\n"),
    (AGI, ED + "IMPLEMENTATION_AND_REPRODUCIBILITY.md", "token", "### BACON boundary", "### Beacon boundary"),
    (AGI, ED + "IMPLEMENTATION_AND_REPRODUCIBILITY.md", "token", MAPPED_OLD, MAPPED_NEW),
    (AGI, ED + "IMPLEMENTATION_AND_REPRODUCIBILITY.md", "meaning", DRAFT_OLD, DRAFT_NEW),
    (AGI, ED + "PUBLICATION_GUIDE_EN.md", "token", "operational approval, or BACON compatibility is established.",
     "operational approval, or Beacon compatibility is established."),
    (AGI, ED + "TECHNICAL_SPECIFICATION.md", "meaning", LISTED_OLD, LISTED_NEW),
    (AGI, ED + "TECHNICAL_SPECIFICATION.md", "meaning", "### Reserved integration name\n\n" + GLOSS_OLD,
     "### Future integration target\n\n" + GLOSS_NEW),
    (AGI, SRC + "EVIDENCE_STATUS.json", "token", '"BACON compatibility"', '"Beacon compatibility"'),
    (AGI, SRC + "LIMITATIONS.md", "meaning", ONLY_TARGET_OLD, ONLY_TARGET_NEW),
    (AGI, SRC + "PUBLICATION_CHECKLIST.md", "token", "general scientific validity, or BACON compatibility.",
     "general scientific validity, or Beacon compatibility."),
    (AGI, SRC + "README.md", "token", "The output is designed so CI can later feed a separately defined BACON adapter.",
     "The output is designed so CI can later feed a separately defined CI-to-Beacon adapter (Beacon Profile v0.1, DOI 10.5281/zenodo.18933553)."),
    (AGI, SRC + "README.md", "meaning", "This release does not define or implement BACON and makes no BACON compatibility claim.",
     "This release does not implement that adapter and makes no Beacon compatibility claim."),
    (AGI, SRC + "RECOGNITION_PROFILE.md", "meaning", LISTED_OLD, LISTED_NEW),
    (AGI, SRC + "REFERENCE_IMPLEMENTATION/README.md", "token", "## BACON boundary", "## Beacon boundary"),
    (AGI, SRC + "REFERENCE_IMPLEMENTATION/README.md", "token", MAPPED_OLD, MAPPED_NEW),
    (AGI, SRC + "REFERENCE_IMPLEMENTATION/README.md", "meaning", DRAFT_OLD, DRAFT_NEW),
    (AGI, SRC + "SCIENTIFIC_CLAIM_MAP.md", "token", CLAIM_OLD, CLAIM_NEW),
    (AGI, SRC + "TERMINOLOGY.md", "meaning", "## Reserved integration name\n\n" + GLOSS_OLD,
     "## Future integration target\n\n" + GLOSS_NEW),
    (SITE, B + "index.html", "token", "BACON is a prospective integration target; no adapter or compatibility result is included.",
     f"{REF} is a prospective integration target; no adapter or compatibility result is included. "
     '(Corrected 19 November 2026: the deposited v1.0.0 files misspell this name as "BACON".)'),
    (SITE, B + "publication.json", "token", "No BACON adapter or demonstrated compatibility; BACON is a prospective integration target.",
     f"No CI-to-Beacon adapter or demonstrated compatibility; {REF} is a prospective integration target."),
]


def sha(blob: bytes) -> str:
    return hashlib.sha256(blob).hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("agi_root", type=Path)
    parser.add_argument("site_root", type=Path)
    parser.add_argument("out_json", type=Path)
    args = parser.parse_args()
    roots = {"advanced-global-intelligence": args.agi_root, "kot141078.github.io": args.site_root}
    output = args.out_json
    if output.exists():
        raise ValueError(f"output {output} exists; refusing to overwrite")
    if any(output.resolve().is_relative_to(root.resolve()) for root in roots.values()):
        raise ValueError("output must be outside the frozen source roots")
    files: dict = {}
    for repo, path, _cls, _old, _new in PATCHES:
        key = (repo, path)
        if key not in files:
            raw = open(os.path.join(roots[repo], path), "rb").read()
            files[key] = {"before": raw, "text": raw.decode("utf-8")}
    patches = []
    for number, (repo, path, cls, old, new) in enumerate(PATCHES, 1):
        text = files[(repo, path)]["text"]
        count = text.count(old)
        if count != 1:
            raise SystemExit(f"E{number:02d} {path}: expected 1 occurrence, found {count}")
        files[(repo, path)]["text"] = text.replace(old, new, 1)
        patches.append({"finding": f"CI-C01-E{number:02d}", "repo": repo, "path": path, "class": cls,
                        "expected_occurrences": 1, "old": old, "new": new})
    bindings, corrected = [], []
    tokens_before = tokens_after = 0
    for (repo, path), data in files.items():
        after = data["text"].encode("utf-8")
        tokens_before += data["before"].decode("utf-8").count("BACON")
        tokens_after += data["text"].count("BACON")
        bindings.append({"repo": repo, "commit": COMMITS[repo], "path": path, "sha256": sha(data["before"]),
                         "size_bytes": len(data["before"]),
                         "source_url": f"https://github.com/Kot141078/{repo}/blob/{COMMITS[repo]}/{path}"})
        corrected.append({"repo": repo, "path": path, "sha256": sha(after), "size_bytes": len(after)})
    spec = {"artifact": "CI_V1_0_0_CORRIGENDUM_01", "status": "PREPARED_FOR_OWNER_AUTHORIZATION",
            "correction_date": "2026-11-19",
            "subject": {"title": "Continuity Instrument (CI) v1.0.0", "version_doi": "10.5281/zenodo.23651305",
                        "concept_doi": "10.5281/zenodo.23651304"},
            "correction": "The future integration target written 'BACON' is Beacon (Beacon Profile v0.1, DOI 10.5281/zenodo.18933553).",
            "source_bindings": bindings, "patches": patches, "corrected_files": corrected,
            "counts": {"files": len(files), "edits": len(patches),
                       "meaning_edits": sum(1 for p in patches if p["class"] == "meaning"),
                       "token_BACON_before": tokens_before, "token_BACON_after": tokens_after}}
    payload = (json.dumps(spec, ensure_ascii=False, indent=1) + "\n").encode("utf-8")
    actual = sha(payload)
    if actual != EXPECTED_SPEC_SHA256:
        raise ValueError(f"generated spec differs from the reviewed specification: {actual}")
    with output.open("xb") as fh:
        fh.write(payload)
    print(json.dumps(spec["counts"]))


if __name__ == "__main__":
    try:
        main()
    except (OSError, UnicodeError, ValueError) as exc:
        print(f"REFUSED: {exc}", file=sys.stderr)
        sys.exit(2)
