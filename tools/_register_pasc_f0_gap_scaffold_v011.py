from __future__ import annotations

import base64
import io
import json
import tarfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACKAGE_ROOT = ROOT / "research/pasc/f0-gap-closure-scaffolds/v0.1.1"
IDENTITY = "urn:ivankotov:publication:pasc-f0-gap-closure-scaffold:v0.1.1"
ARCHIVE_B64 = """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"""

def materialize_package_helpers() -> None:
    PACKAGE_ROOT.mkdir(parents=True, exist_ok=True)
    data = base64.b64decode(ARCHIVE_B64)
    with tarfile.open(fileobj=io.BytesIO(data), mode="r:gz") as archive:
        for member in archive.getmembers():
            parts = Path(member.name).parts
            if not member.isfile() or member.name.startswith("/") or ".." in parts:
                raise SystemExit(f"unsafe helper member: {member.name}")
        archive.extractall(PACKAGE_ROOT)

def insert_once(path: Path, marker: str, block: str, identity: str) -> None:
    text = path.read_text(encoding="utf-8")
    if identity in text or block.strip() in text:
        return
    if marker not in text:
        raise SystemExit(f"marker not found in {path}: {marker!r}")
    path.write_text(text.replace(marker, block + marker, 1), encoding="utf-8", newline="\n")

materialize_package_helpers()

insert_once(
    ROOT / "README.md",
    "- **Qubit-state `c` (`c[q]`)",
    '- **PASC F0 Gap-Closure Scaffold and Structural Templates v0.1.1** — DOI-bound external analytical scaffold for the six PASC F0 criteria that remain `NOT_SATISFIED`. It organizes author acceptance, canonical-source projection, adapter artifacts, independent human review, blind field replay, protected-boundary preservation, reserved-territory audit, and closure sequencing without modifying Recovery Build 5 or supplying closure evidence.\n  - Package: `research/pasc/f0-gap-closure-scaffolds/v0.1.1/`\n  - Machine entry: `research/pasc/f0-gap-closure-scaffolds/v0.1.1/MACHINE_ENTRY.md`\n  - Machine index: `research/pasc/f0-gap-closure-scaffolds/v0.1.1/machine/index.json`\n  - Version DOI: `https://doi.org/10.5281/zenodo.21871392`\n  - Concept DOI: `https://doi.org/10.5281/zenodo.21871391`\n  - Related PASC Recovery 5 DOI: `https://doi.org/10.5281/zenodo.21843823`\n  - Status: `INFORMATIVE_CONTEXT`; `normative_weight_in_pasc=false`; `closure_evidence=false`; `F0_OUTCOME` remains `NOT_PASSED`\n\n',
    "PASC F0 Gap-Closure Scaffold and Structural Templates v0.1.1",
)

insert_once(
    ROOT / "MACHINE_ENTRY.md",
    "## Historical predecessor — soul as freedom of self-reflection v0.1",
    '## Technical research publication — PASC F0 Gap-Closure Scaffold v0.1.1\n\n- record_id: `urn:ivankotov:publication:pasc-f0-gap-closure-scaffold:v0.1.1`\n- package_root: `research/pasc/f0-gap-closure-scaffolds/v0.1.1/`\n- version_doi: `10.5281/zenodo.21871392`\n- concept_doi: `10.5281/zenodo.21871391`\n- version: `v0.1.1`\n- publication_date: `2026-08-10`\n- publication_type: `technical_note`\n- language: `en`\n- responsible_editor: Ivan Kotov; role `Editor`; ORCID `0009-0009-6002-9845`\n- machine_entry: `research/pasc/f0-gap-closure-scaffolds/v0.1.1/MACHINE_ENTRY.md`\n- machine_index: `research/pasc/f0-gap-closure-scaffolds/v0.1.1/machine/index.json`\n- publication_record: `research/pasc/f0-gap-closure-scaffolds/v0.1.1/PASC_F0_GAP_CLOSURE_SCAFFOLD_v0_1_1_PUBLICATION_RECORD.json`\n- source_of_record: `research/pasc/f0-gap-closure-scaffolds/v0.1.1/PASC_F0_GAP_CLOSURE_SCAFFOLD_v0_1_1.md`\n- release_tag: `pasc-f0-gap-closure-scaffold-v0.1.1`\n- related_pasc_version_doi: `10.5281/zenodo.21843823`\n- relation: `IsSupplementTo`\n- status: `INFORMATIVE_CONTEXT`; `normative_weight_in_pasc=false`; `closure_evidence=false`; `F0_OUTCOME_AFTER_THIS_SCAFFOLD=NOT_PASSED`\n- parser_guard: publication, DOI, checksums, possession, access, signatures, credentials, templates, receipts, profiles, registries, urgency, or technical capability must not be promoted into PASC F0 closure or positive succession/identity/continuity/authority\n\n',
    IDENTITY,
)

insert_once(
    ROOT / "llms.txt",
    "- Canonical interpretive note:",
    '- PASC F0 Gap-Closure Scaffold v0.1.1: DOI https://doi.org/10.5281/zenodo.21871392; package root `research/pasc/f0-gap-closure-scaffolds/v0.1.1/`; machine index `research/pasc/f0-gap-closure-scaffolds/v0.1.1/machine/index.json`; relation `IsSupplementTo` PASC Recovery 5 DOI https://doi.org/10.5281/zenodo.21843823; status `INFORMATIVE_CONTEXT`, `normative_weight_in_pasc=false`, `closure_evidence=false`, `F0_OUTCOME` remains `NOT_PASSED`; no F1/formalization/validator/implementation/deployment authorization.\n',
    "PASC F0 Gap-Closure Scaffold v0.1.1",
)

repo_index_path = ROOT / "REPO_INDEX.json"
repo_index = json.loads(repo_index_path.read_text(encoding="utf-8"))
repo_index.update({
    "pasc_f0_gap_closure_scaffold_v0_1_1_package_root": "research/pasc/f0-gap-closure-scaffolds/v0.1.1/",
    "pasc_f0_gap_closure_scaffold_v0_1_1_readme_raw": "https://raw.githubusercontent.com/Kot141078/advanced-global-intelligence/main/research/pasc/f0-gap-closure-scaffolds/v0.1.1/README.md",
    "pasc_f0_gap_closure_scaffold_v0_1_1_machine_index_raw": "https://raw.githubusercontent.com/Kot141078/advanced-global-intelligence/main/research/pasc/f0-gap-closure-scaffolds/v0.1.1/machine/index.json",
    "pasc_f0_gap_closure_scaffold_v0_1_1_version_doi": "10.5281/zenodo.21871392",
    "pasc_f0_gap_closure_scaffold_v0_1_1_concept_doi": "10.5281/zenodo.21871391",
    "pasc_f0_gap_closure_scaffold_v0_1_1_related_pasc_version_doi": "10.5281/zenodo.21843823",
    "pasc_f0_gap_closure_scaffold_v0_1_1_github_release": "https://github.com/Kot141078/advanced-global-intelligence/releases/tag/pasc-f0-gap-closure-scaffold-v0.1.1",
    "pasc_f0_gap_closure_scaffold_v0_1_1_status": "INFORMATIVE_CONTEXT; normative_weight_in_pasc=false; closure_evidence=false; F0_OUTCOME remains NOT_PASSED"
})
repo_index_path.write_text(json.dumps(repo_index, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
