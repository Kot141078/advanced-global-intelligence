# Corrigendum 01 to Continuity Instrument (CI) v1.0.0

Ivan Kotov · Correction date: 19 November 2026 · Candidate prepared: 20 November 2026 · ORCID 0009-0009-6002-9845

**Status: GitHub publication candidate. Zenodo: NOT_YET_PUBLISHED. No corrigendum DOI assigned.**

The CI v1.0.0 texts name a future integration target "BACON". The author meant **Beacon** (Beacon Profile v0.1, DOI 10.5281/zenodo.18933553). This supplement documents the correction of 31 uppercase occurrences across 17 bound text files. Nine edits also revise boundary statements to identify the published referent while preserving the absence of a CI-to-Beacon mapping, adapter or compatibility result. The implementation, schemas, tests, evidence status, claim ceilings and component rights of CI v1.0.0 are unchanged.

Read [CORRIGENDUM_EN.md](CORRIGENDUM_EN.md), the normative English note, or its [Russian companion](CORRIGENDUM_RU.md). Machine-readable publication state is in [PUBLICATION_RECORD.json](PUBLICATION_RECORD.json).

**Preserve the frozen predecessor:** do not apply `patches/advanced-global-intelligence.diff` to `publications/continuity-instrument-v1-0-0/`. This supplement belongs beside it at `publications/continuity-instrument-v1-0-0-corrigendum-01/`. No old mirror file, manifest, PDF or archive is replaced.

## Contents

| Path | Purpose |
|---|---|
| `CORRIGENDUM_EN.md`, `CORRIGENDUM_RU.md` | Correction, evidence limits, affected files and publication sequence |
| `PUBLICATION_RECORD.json` | Current GitHub/Zenodo stage, separate subject DOIs, rights and source references |
| `patches/corrections.json` | Unchanged 25-edit specification; SHA-256 `9ac75661c364d139c8f4c2f3656a285d63fa89d6e34aac6786b4d72ad6e065dd` |
| `patches/advanced-global-intelligence.diff` | Historical diff for 15 mirror texts; for isolated corrected copies or a separately chosen future edition, never the frozen mirror |
| `patches/kot141078.github.io.diff` | Historical two-file site diff; the eventual site change requires current-byte reconciliation and the published corrigendum link |
| `corrected_text/` | Reviewed corrected copies of the 17 bound texts, without replacing their originals |
| `source_snapshots/`, `SOURCE_BINDINGS.json` | Frozen predecessors, source commits, subject DOIs and archive identities |
| `tools/`, `build/`, `MAINTENANCE_TOOLING.md` | Maintenance tools, generation provenance and validation instructions |
| `evidence/` | Preserved preparation evidence; later verification must identify its own run and scope |
| `ZENODO_METADATA.json`, `ZENODO_DESCRIPTION_CORRECTED.txt` | Owner form plan and screenshot-based proposal for the original description |
| `ZENODO_UPLOAD_RU.md` | Owner upload and Preview guide in Russian |
| `RIGHTS.md` | All Rights Reserved for new text and tools; retained rights of copied components |
| `SHA256SUMS.txt` | Integrity inventory of the assembled package |

## Scope and preservation

The corrected copies contain one uppercase "BACON", quoted in the site's correction note. Historical snapshots, patch old sides, the original PDFs and archives retain their original spelling. The frozen publication record also retains `capability_boundaries.bacon_compatibility_established=false`; the corrigendum identifies its intended referent without renaming that key or changing the value.

The specification's 16 `token` edits comprise 10 literal name substitutions and six naming/citation/notice adjustments. The other nine revise the surrounding boundary language. Identifying Beacon does not establish integration feasibility or compatibility. The Beacon DOI is cited without assigning its unresolved version/concept role.

## Reproduce

Python 3.10 or later, standard library only; Git is needed for the two patch-applicability checks. From the assembled package root, run:

```sh
python3 -B tools/validate_package.py
```

To inspect corrected copies manually, use the included predecessor snapshots and a new output directory outside the package:

```sh
python3 -B tools/apply_corrections.py --agi-root source_snapshots/advanced-global-intelligence --site-root source_snapshots/kot141078.github.io --output ../ci-corrigendum-output
```

The output directory must not exist and may be removed after inspection. Keeping generated output outside the package preserves its exact checksum inventory. Inputs stay unchanged. The independent review of 19 November 2026 ran the submitted ZIP suite with 74 PASS, 0 FAIL and 2 SKIP; both skipped `git apply --check` predicates then passed separately on real checkouts at the pinned commits. It did not run one monolithic 76/0/0 suite. The original `evidence/REGRESSION_TESTS.txt` remains the preparer's earlier report. A passing correction-tool check is not CI scientific qualification.

## Publication sequence

1. Integrate the verified GitHub candidate as a sibling supplement and update applicable human and machine entry points outside the frozen v1.0.0 tree. Do not report Zenodo publication or assign a guessed DOI.
2. The owner creates a separate Zenodo corrigendum record and supplies its assigned DOI. Finalize the DOI-bearing Markdown/PDF, metadata and checksums, then review Preview before the owner publishes. The relation is `isSupplementTo` → exact CI version DOI `10.5281/zenodo.23651305`; CI concept DOI `10.5281/zenodo.23651304` remains the identity of CI's own version series.
3. After publication verification, the owner applies the original-record correction and actual corrigendum link, then updates the site. The description candidate preserves the existing paragraph about files finalized before DOI reservation. Keep that paragraph in its original Description or Notes field, without duplication. Preserve all unrelated live text and the old record's component rights.

This is the selected separate-supplement plus original-notice route. No CI v1.0.1 is created by it. The supplied site diff records the reviewed historical change; it must not overwrite a later site revision or imply that this candidate is already published.

## Rights

Copyright © 2026 Ivan Kotov. All rights reserved. No license grant.

The owner confirmed this choice on 20 November 2026 for the new corrigendum text and maintenance tools, including `tools/` and `build/`. Source snapshots and corrected copies retain their original component rights. Public availability does not relicense reserved components. See [RIGHTS.md](RIGHTS.md).
