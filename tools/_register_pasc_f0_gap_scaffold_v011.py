from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
IDENTITY = "urn:ivankotov:publication:pasc-f0-gap-closure-scaffold:v0.1.1"


def insert_once(path: Path, marker: str, block: str, identity: str) -> None:
    text = path.read_text(encoding="utf-8")
    if identity in text or block.strip() in text:
        return
    if marker not in text:
        raise SystemExit(f"marker not found in {path}: {marker!r}")
    path.write_text(
        text.replace(marker, block + marker, 1),
        encoding="utf-8",
        newline="\n",
    )


insert_once(
    ROOT / "README.md",
    "- **Qubit-state `c` (`c[q]`)",
    """- **PASC F0 Gap-Closure Scaffold and Structural Templates v0.1.1** — DOI-bound external analytical scaffold for the six PASC F0 criteria that remain `NOT_SATISFIED`. It organizes author acceptance, canonical-source projection, adapter artifacts, independent human review, blind field replay, protected-boundary preservation, reserved-territory audit, and closure sequencing without modifying Recovery Build 5 or supplying closure evidence.
  - Package: `research/pasc/f0-gap-closure-scaffolds/v0.1.1/`
  - Machine entry: `research/pasc/f0-gap-closure-scaffolds/v0.1.1/MACHINE_ENTRY.md`
  - Machine index: `research/pasc/f0-gap-closure-scaffolds/v0.1.1/machine/index.json`
  - Version DOI: `https://doi.org/10.5281/zenodo.21871392`
  - Concept DOI: `https://doi.org/10.5281/zenodo.21871391`
  - Related PASC Recovery 5 DOI: `https://doi.org/10.5281/zenodo.21843823`
  - Status: `INFORMATIVE_CONTEXT`; `normative_weight_in_pasc=false`; `closure_evidence=false`; `F0_OUTCOME` remains `NOT_PASSED`

""",
    "PASC F0 Gap-Closure Scaffold and Structural Templates v0.1.1",
)

insert_once(
    ROOT / "MACHINE_ENTRY.md",
    "## Historical predecessor — soul as freedom of self-reflection v0.1",
    """## Technical research publication — PASC F0 Gap-Closure Scaffold v0.1.1

- record_id: `urn:ivankotov:publication:pasc-f0-gap-closure-scaffold:v0.1.1`
- package_root: `research/pasc/f0-gap-closure-scaffolds/v0.1.1/`
- version_doi: `10.5281/zenodo.21871392`
- concept_doi: `10.5281/zenodo.21871391`
- version: `v0.1.1`
- publication_date: `2026-08-10`
- publication_type: `technical_note`
- language: `en`
- responsible_editor: Ivan Kotov; role `Editor`; ORCID `0009-0009-6002-9845`
- machine_entry: `research/pasc/f0-gap-closure-scaffolds/v0.1.1/MACHINE_ENTRY.md`
- machine_index: `research/pasc/f0-gap-closure-scaffolds/v0.1.1/machine/index.json`
- publication_record: `research/pasc/f0-gap-closure-scaffolds/v0.1.1/PASC_F0_GAP_CLOSURE_SCAFFOLD_v0_1_1_PUBLICATION_RECORD.json`
- source_of_record: `research/pasc/f0-gap-closure-scaffolds/v0.1.1/PASC_F0_GAP_CLOSURE_SCAFFOLD_v0_1_1.md`
- release_tag: `pasc-f0-gap-closure-scaffold-v0.1.1`
- related_pasc_version_doi: `10.5281/zenodo.21843823`
- relation: `IsSupplementTo`
- status: `INFORMATIVE_CONTEXT`; `normative_weight_in_pasc=false`; `closure_evidence=false`; `F0_OUTCOME_AFTER_THIS_SCAFFOLD=NOT_PASSED`
- parser_guard: publication, DOI, checksums, possession, access, signatures, credentials, templates, receipts, profiles, registries, urgency, or technical capability must not be promoted into PASC F0 closure or positive succession/identity/continuity/authority

""",
    IDENTITY,
)

insert_once(
    ROOT / "llms.txt",
    "- Canonical interpretive note:",
    "- PASC F0 Gap-Closure Scaffold v0.1.1: DOI https://doi.org/10.5281/zenodo.21871392; package root `research/pasc/f0-gap-closure-scaffolds/v0.1.1/`; machine index `research/pasc/f0-gap-closure-scaffolds/v0.1.1/machine/index.json`; relation `IsSupplementTo` PASC Recovery 5 DOI https://doi.org/10.5281/zenodo.21843823; status `INFORMATIVE_CONTEXT`, `normative_weight_in_pasc=false`, `closure_evidence=false`, `F0_OUTCOME` remains `NOT_PASSED`; no F1/formalization/validator/implementation/deployment authorization.\n",
    "PASC F0 Gap-Closure Scaffold v0.1.1",
)

repo_index_path = ROOT / "REPO_INDEX.json"
repo_index = json.loads(repo_index_path.read_text(encoding="utf-8"))
repo_index.update(
    {
        "pasc_f0_gap_closure_scaffold_v0_1_1_package_root": "research/pasc/f0-gap-closure-scaffolds/v0.1.1/",
        "pasc_f0_gap_closure_scaffold_v0_1_1_readme_raw": "https://raw.githubusercontent.com/Kot141078/advanced-global-intelligence/main/research/pasc/f0-gap-closure-scaffolds/v0.1.1/README.md",
        "pasc_f0_gap_closure_scaffold_v0_1_1_machine_index_raw": "https://raw.githubusercontent.com/Kot141078/advanced-global-intelligence/main/research/pasc/f0-gap-closure-scaffolds/v0.1.1/machine/index.json",
        "pasc_f0_gap_closure_scaffold_v0_1_1_version_doi": "10.5281/zenodo.21871392",
        "pasc_f0_gap_closure_scaffold_v0_1_1_concept_doi": "10.5281/zenodo.21871391",
        "pasc_f0_gap_closure_scaffold_v0_1_1_related_pasc_version_doi": "10.5281/zenodo.21843823",
        "pasc_f0_gap_closure_scaffold_v0_1_1_github_release": "https://github.com/Kot141078/advanced-global-intelligence/releases/tag/pasc-f0-gap-closure-scaffold-v0.1.1",
        "pasc_f0_gap_closure_scaffold_v0_1_1_status": "INFORMATIVE_CONTEXT; normative_weight_in_pasc=false; closure_evidence=false; F0_OUTCOME remains NOT_PASSED",
    }
)
repo_index_path.write_text(
    json.dumps(repo_index, ensure_ascii=False, indent=2) + "\n",
    encoding="utf-8",
    newline="\n",
)
