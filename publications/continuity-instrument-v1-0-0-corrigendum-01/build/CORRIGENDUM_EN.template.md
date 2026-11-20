# Corrigendum 01: Continuity Instrument (CI) v1.0.0

## The future integration target written "BACON" is Beacon

**Author:** Ivan Kotov  
**ORCID:** 0009-0009-6002-9845  
**Correction date:** 19 November 2026  
**Publication class:** text corrigendum; no change to the implementation, schemas, tests or evidence status  
**Candidate prepared:** 20 November 2026  
**Status:** GitHub publication candidate; Zenodo NOT_YET_PUBLISHED; no corrigendum DOI assigned  
**Corrects:** Continuity Instrument (CI) v1.0.0, English Academic Edition academic-pdf-2, version DOI `10.5281/zenodo.23651305`, concept DOI `10.5281/zenodo.23651304`, Zenodo record 23651305, published 25 October 2026.

### Publication relationship

This corrigendum corrects one name in the CI v1.0.0 texts without replacing the deposited files. The deposited archives stay as they are: the original source build `CI_CONTINUITY_INSTRUMENT_V1_0_0.zip` (50,765 bytes, SHA-256 `be87dd926ed96e91e8de25bae2e18666f74ac738b173379ddc0092f98563f663`) and the academic package `CI_CONTINUITY_INSTRUMENT_V1_0_0_ACADEMIC_EN_PACKAGE_20261025.zip` (1,097,821 bytes, SHA-256 `0e97eb3b8b54b091a35c2a0cc0d702efa9f781e10d1ac0773d42796e1047a659`). The predecessor texts are bound by exact bytes to the public mirror commits in `SOURCE_BINDINGS.json` and `patches/corrections.json`.

## CI-C01: name of the future integration target

**Error.** The CI v1.0.0 texts name a future integration target "BACON". This is the author's typing error for **Beacon**, the inter-entity recognition profile published as Beacon Profile v0.1 (DOI `10.5281/zenodo.18933553`). The same package already cites Beacon under that DOI as a conceptual alignment (`RECOGNITION_PROFILE.md`, `README.md`, `LICENSES_AND_THIRD_PARTY.md`), and the site record already lists "no … Beacon conformance". The error therefore gave one object two names, one of them undefined.

**Extent.** The correction addresses 31 uppercase occurrences of "BACON" in 17 bound text files: 15 files of the repository mirror and two files of the site record. The corrected copies retain one occurrence in the site's explanatory correction note. PDFs 01, 03, 04, 05 and 07 and both archived packages contain the original spelling; PDFs 02 (Russian) and 06 do not. Historical source snapshots, old sides of patches and the v1.0.0 mirror and deposited files retain the original spelling for provenance. The frozen CI publication record also retains the legacy key `capability_boundaries.bacon_compatibility_established` with the value `false`. This corrigendum identifies the intended referent without renaming that key or changing its value.

**What the error changed in meaning.** Sixteen edits correct the name and, where needed, add its citation or a correction note. Nine edits also revise the surrounding boundary statements. The statements that no public canonical definition had been found are withdrawn because the intended referent is the published Beacon Profile v0.1. The revised wording identifies that referent while preserving the absence of a CI-to-Beacon mapping, adapter or compatibility result.

**Corrected forms.**

- Glossary entry (TERMINOLOGY, Technical Specification): **Beacon** — Beacon Profile v0.1, a separately published recognition profile (DOI 10.5281/zenodo.18933553), named here as a conceptual alignment and a future integration target only. This package defines no CI-to-Beacon mapping and assigns no Beacon semantics to any CI field. The section heading "Reserved integration name" becomes "Future integration target".
- Boundary statement (LIMITATIONS, Evidence Claims and Limitations): Beacon (Beacon Profile v0.1, DOI 10.5281/zenodo.18933553) is only a future integration target. No CI-to-Beacon adapter or compatibility result is claimed.
- Listing statement (Recognition Profile, Technical Specification): Beacon (Beacon Profile v0.1, DOI 10.5281/zenodo.18933553) is listed only as a future integration target. This package defines no CI-to-Beacon mapping and claims no technical compatibility.
- Adapter boundary (README, reference implementation README, Implementation and Reproducibility): the output is designed for possible future use by an explicit, versioned CI-to-Beacon adapter. This release does not implement that adapter, assign Beacon semantics to any CI field, or claim compatibility with Beacon.

**What does not change.** CI v1.0.0 contains no CI-to-Beacon adapter, mapping or compatibility result, and "Beacon compatibility" stays in every list of claims that are not established. The formation-depth vector, schemas, reference implementation (`ci_profile.py`, SHA-256 `2ee799e9a423b4aa128cd2f4ca75424c6122ac46fb7df51d588d009cac96b5f4`), tests, the R157, R160 and R161 evidence status, the claim ceilings and the rights statement are unchanged. This corrigendum makes no claim that CI and Beacon are compatible.

**DOI role.** The site record of Beacon Profile v0.1 lists DOI `10.5281/zenodo.18933553` with its role (version or concept) unresolved. This corrigendum cites the DOI exactly as the CI package already does and asserts no role. Reader navigation: [Beacon publication page](https://ivankotov.eu/publications/beacon-profile-v0-1/). Exact source: [Beacon Profile v0.1 at the pinned repository commit](https://github.com/Kot141078/advanced-global-intelligence/blob/bb062414b598afae970bef37ce7489433a51868d/protocols/beacon/Beacon_Profile_v0.1_EN.md).

## Affected files

Predecessor and corrected SHA-256 (first 16 hex digits; full values in `patches/corrections.json`). Edit classes: T = naming, citation or correction-note edit; M = surrounding boundary-statement revision. The original machine class values remain unchanged. Of the 16 T edits, 10 are literal name substitutions and six also adjust references, adapter naming or the correction notice.

<!--CORRECTION_TABLE-->

Derived artifacts that carry the term and remain unchanged under this correction's preservation policy (current SHA-256, first 16 hex digits):

| Artifact | SHA-256 | Action in a corrected version |
|---|---|---|
| `package/PDFs/01_CI_Explanatory_Paper_EN.pdf` | `651839185c6ac621` | rebuild |
| `package/PDFs/03_CI_Technical_Specification_EN.pdf` | `c01f2a0a5df71b38` | rebuild |
| `package/PDFs/04_CI_Implementation_and_Reproducibility_EN.pdf` | `0831884ad3bd17c6` | rebuild |
| `package/PDFs/05_CI_Evidence_Claims_and_Limitations_EN.pdf` | `ab47e3b6a7e49bf5` | rebuild |
| `package/PDFs/07_CI_Publication_Guide_EN.pdf` | `0438227ebcb7f0f7` | rebuild |
| `package/source_original/CI_CONTINUITY_INSTRUMENT_V1_0_0.zip` | `be87dd926ed96e91` | keep; a corrected source build gets a new name |
| `release/CI_CONTINUITY_INSTRUMENT_V1_0_0_ACADEMIC_EN_PACKAGE_20261025.zip` | `0e97eb3b8b54b091` | keep; a corrected edition gets a new archive |

## Publication sequence

The selected route is a separate corrigendum plus a narrow notice in the original record. The sequence is GitHub, then owner publication on Zenodo, then the site update. This candidate records that sequence; it does not report those actions as completed. Preservation of the v1.0.0 files is a requirement of this correction, not a claim that Zenodo prohibits every post-publication file change.

**Do not apply `patches/advanced-global-intelligence.diff` to the frozen `publications/continuity-instrument-v1-0-0/` tree.** It records historical differences for isolated corrected copies or a separately chosen future edition. The entire old tree, including its README, `PUBLICATION_RECORD.json` and `MIRROR_MANIFEST.json`, stays unchanged.

1. **GitHub candidate.** Add this supplement at the sibling path `publications/continuity-instrument-v1-0-0-corrigendum-01/`. Update the applicable human and machine entry points outside the frozen v1.0.0 tree. At this stage the corrigendum DOI is absent. Add an assigned DOI only after the owner confirms it; keep the Zenodo status `NOT_YET_PUBLISHED` until actual publication.
2. **Separate Zenodo corrigendum.** The owner creates the record and supplies its assigned DOI. Prepare the final Markdown, academic PDF, metadata and checksums with that exact identifier, then verify the owner's Preview. The owner uploads and publishes. Use `isSupplementTo` with the exact CI version DOI `10.5281/zenodo.23651305`; this is not CI v1.0.1 or a new version under CI's concept DOI.
3. **Original-record notice.** After the corrigendum is published and verified, the owner applies the agreed narrow description correction and adds its actual link. The screenshot-based candidate `ZENODO_DESCRIPTION_CORRECTED.txt` preserves the existing paragraph explaining preparation before DOI reservation. Preserve that paragraph in its existing Description or Notes field, without duplication, and retain all unrelated text and existing CI component rights.
4. **Site update.** Revalidate the two site files against their current bytes, preserve later unrelated edits, and update the visible notice and machine entry with the actual published corrigendum link. The historical site diff is not an instruction to overwrite a later site revision. A full corrected CI edition remains a separate future decision.

## Reproduce

Python 3.10 or later, standard library only; Git is needed for patch-applicability checks. From the assembled package root:

```sh
python3 -B tools/validate_package.py
```

For manual inspection against both repositories at the bound commits:

```sh
python3 -B tools/apply_corrections.py --agi-root ../advanced-global-intelligence --site-root ../kot141078.github.io --output ../ci-corrigendum-output
python3 -B tools/test_regressions.py --agi-root ../advanced-global-intelligence --site-root ../kot141078.github.io
```

The output directory must not exist; it is outside the package and may be removed after inspection. Altered predecessor bytes, repeated application and overwriting are refused. Inputs are never modified. The independent review of 19 November 2026 ran the submitted ZIP suite with 74 PASS, 0 FAIL and 2 SKIP, then separately passed both skipped `git apply --check` predicates on the real pinned checkouts. This was not one monolithic 76/0/0 run. The archived `evidence/REGRESSION_TESTS.txt` is the preparer's earlier report and remains attributed preparation evidence. These checks concern the correction package, not CI scientific qualification.

## Rights

Copyright © 2026 Ivan Kotov. All rights reserved. No license grant.

This statement applies to the new corrigendum text and maintenance tools, including `tools/` and `build/`, as confirmed by the owner on 20 November 2026. Corrected copies and source snapshots retain their original component rights; this statement does not relicense them. In particular, the original CI scientific prose remains under its existing CC BY 4.0 terms, while reserved reference-implementation material retains its existing All Rights Reserved statement. See `RIGHTS.md` for scope.
