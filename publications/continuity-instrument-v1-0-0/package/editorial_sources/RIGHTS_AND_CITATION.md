# Continuity Instrument: Authorship, Rights and Citation

## 1. Authorship and bibliographic identity

Scientific author: **Ivan Kotov**. Independent researcher, Brussels, Belgium. ORCID: https://orcid.org/0009-0009-6002-9845. Author's corpus: https://ivankotov.eu/corpus-map/.

The underlying research-software specification is Continuity Instrument (CI): Evidence-Bound Measurement of Governed Continuity in Long-Lived AI Systems, v1.0. Source and implementation version: 1.0.0. Original source build: _02. This accompanying academic edition is identified separately as academic-pdf-2, prepared on 25 October 2026. Its PDF files are explanatory or typeset reading editions, not a new implementation release. English is the primary publication language. The Russian explanatory PDF is retained unchanged from academic-pdf-1 as a supplement; its original edition label remains visible.

Suggested citation before assignment of a CI DOI:

> Kotov, Ivan. (2026). Continuity Instrument (CI): Evidence-Bound Measurement of Governed Continuity in Long-Lived AI Systems, v1.0. Source version 1.0.0, build _02; academic PDF companion edition academic-pdf-2. Research-software specification and reference package.

No DOI for CI is invented or borrowed from a cited work. After publication, append the actual version DOI of the verified deposit to the citation. The original CITATION.cff remains unchanged in source_original/Continuity_Instrument_v1.0.0/.

## 2. Rights of the academic edition

Copyright © 2026 Ivan Kotov.

The new explanatory text, Russian companion, editorial notes, publication guide, and descriptive metadata are CC BY 4.0, consistent with the scientific-text posture of the source publication. This statement does not relicense any original code, schemas, tests, or third-party material.

| Component | Rights scope |
|---|---|
| PDFs 01, 02, 03, 05, 06 and 07; corresponding new prose and descriptive metadata | CC BY 4.0 for the author's text and metadata; third-party citations retain their own rights |
| PDF 04, Part I; the corresponding reproduced implementation README in editorial_sources/IMPLEMENTATION_AND_REPRODUCIBILITY.md | Copyright © 2026 Ivan Kotov. All rights reserved. No license grant. |
| PDF 04, Part II; its distinct editorial notes and Part III | CC BY 4.0 |
| Original REFERENCE_IMPLEMENTATION/ directory, including its README and schemas; original tests/test_ci_profile.py | Copyright © 2026 Ivan Kotov. All rights reserved. No license grant. |
| New `build/*.py`, verification/verify_package.py, and `examples/*.json` | Copyright © 2026 Ivan Kotov. All rights reserved. No license grant. |
| Original source ZIP and its extracted files | Original component rights preserved exactly; the archive as a whole is mixed-rights |
| DejaVu font glyphs embedded in the PDFs | The font's existing Bitstream Vera/DejaVu terms; the complete accompanying notice is FONT_LICENSE.txt |
| External evidence, models, runtimes, repositories and cited publications | Their own rights and access conditions; not relicensed or redistributed by this edition |

A CC BY label for scientific prose is not a grant of rights over the restricted implementation. The package is publicly readable under the stated component conditions; it is not offered as wholly open-source software. The no-grant statements are preserved here, not silently replaced with an inferred permissive code licence.

The PDF text uses embedded DejaVu fonts for reliable English, Cyrillic, and symbol rendering. Font binaries are not separately redistributed. Their existing notice accompanies the package. ReportLab and Pandoc are build-time tools and are not bundled as executables.

## 3. Editorial preparation and review attribution

The scientific authorship belongs to Ivan Kotov. Editorial drafting, translation, typesetting and mechanical checks were assisted by ChatGPT at the author's request. That assistance is not presented as additional scientific authorship, external peer review, or independent empirical replication. Separate automated review findings are attributed to the public extract in verification/SOURCE_REVIEW_PUBLIC_EXTRACT.md.

## 4. Original source rights statement

The following source text is reproduced under its existing CC BY 4.0 grant. Its original file-level scope remains authoritative for the unchanged source build. Read the new edition scopes above alongside it.


<!-- PAGEBREAK -->

## Original LICENSES_AND_THIRD_PARTY.md

Source: `LICENSES_AND_THIRD_PARTY.md`. Original wording reproduced as a reading edition.

### CI scientific text and metadata

Copyright © 2026 Ivan Kotov.

The scientific text and metadata created for this publication package are licensed under the **Creative Commons Attribution 4.0 International license (CC BY 4.0)**:

https://creativecommons.org/licenses/by/4.0/

This grant covers the following scientific-text and metadata files as prepared in this package:

- `README.md`
- `CI_SPECIFICATION.md`
- `TERMINOLOGY.md`
- `SCIENTIFIC_CLAIM_MAP.md`
- `CONTINUITY_OBSERVABLES.md`
- `RECOGNITION_PROFILE.md`
- `REPRODUCIBILITY.md`
- `LIMITATIONS.md`
- `LICENSES_AND_THIRD_PARTY.md`
- `CITATION.cff`
- `.zenodo.json`
- `EVIDENCE_STATUS.json`
- `PUBLICATION_CHECKLIST.md`
- `PUBLICATION_MANIFEST.json`
- `SHA256SUMS.txt`
- `STATIC_VERIFICATION.json`
- `ZENODO_DEPOSIT_INSTRUCTIONS.md`

### Component boundaries

| Component | Included in this draft? | Rights treatment |
|---|---|---|
| CI scientific prose and metadata listed above | Yes | CC BY 4.0. |
| `REFERENCE_IMPLEMENTATION/` (including schemas) and `tests/test_ci_profile.py` | Yes | **Copyright © 2026 Ivan Kotov. All rights reserved. No license grant.** These files do not inherit CC BY 4.0 by implication. |
| Frozen R160/R161 runner and scoring sources outside this package | Referenced, not copied | Retain their existing component or repository license; this package does not relicense them. |
| R157 evidence archive | Referenced, not copied | Retains its original rights and access controls. The Drive ID and SHA-256 are custody metadata, not a license grant. |
| R160/R161 evidence archives | Linked and pinned, not copied | Retain their original rights and access controls. This package reports only custody metadata and bounded terminal results. |
| Ollama runtime | Not distributed | Governed by the runtime publisher's license and terms. Pins identify the evaluated bytes only. |
| `qwen3-vl:32b` and `qwen2.5:32b` model files | Not distributed | Governed by the model files' accompanying licenses and applicable terms. Pins do not grant redistribution rights. |
| Referenced public-canon DOI records | Linked, not incorporated | Governed by each record's own license and rights statement. Citation does not import its content or license. |
| Qubit material | Linked and pinned only | **All Rights Reserved.** No raw Qubit text is included or licensed by this package. |

### Qubit boundary

The only Qubit information included in this draft is repository and integrity metadata:

- Repository: https://github.com/Kot141078/qubit-of-hope-volume-i
- Commit: `88b582579ace4a330ce4d53b07d7ec4e98cb4eeb`
- Tree: `9d251575e2b0d3c75bfd1fe7782c562f1de64a38`
- Rights posture: All Rights Reserved.

No Qubit narrative, excerpt, holdout text, translation, or derivative content is reproduced.

### Final component rights for deposit

The package uses two non-overlapping rights entries:

1. **Scientific text and metadata:** Creative Commons Attribution 4.0 International (`CC-BY-4.0`).
2. **Reference implementation, schemas, and tests:** `Copyright © 2026 Ivan Kotov. All rights reserved. No license grant.`

The second entry preserves the existing no-grant posture and does not create new code rights. In the Zenodo web UI, add both entries and associate their scopes in the record description. The `.zenodo.json` `cc-by-4.0` field represents the scientific-text/metadata entry only; it must not be interpreted as relicensing code, schemas, or tests.

### Public-canon references

The following are external citations, not bundled works:

- Theoretical Core: https://doi.org/10.5281/zenodo.20679718 and https://doi.org/10.5281/zenodo.20679717
- Temporal AI Presence: https://doi.org/10.5281/zenodo.22070960 and https://doi.org/10.5281/zenodo.22070959
- Personality Formation: https://doi.org/10.5281/zenodo.20648731 and https://doi.org/10.5281/zenodo.20648730
- C-Calculus: https://doi.org/10.5281/zenodo.21205427
- Beacon: https://doi.org/10.5281/zenodo.18933553
- Entity vs Profile: https://doi.org/10.5281/zenodo.21204415 and https://doi.org/10.5281/zenodo.21204414

A depositor must review the rights statement of any external material before copying it into a later release.

### No rights inference

A hash, DOI, URL, citation, repository pin, evaluator output, or witness record does not grant a copyright license, access permission, model license, data-processing right, operational authority, or right to publish. Those permissions must be established separately for each component.


## 5. Record metadata and the final deposit

The public Zenodo record's metadata is governed separately by Zenodo's CC0 policy. It is distinct from .json, .cff, and .md files inside the deposited archive. Use the publication guide to state both component-rights entries in the record description; do not import the original global licence field as though it relicensed every component.

Primary platform sources: https://help.zenodo.org/docs/deposit/describe-records/licenses/ and https://about.zenodo.org/policies/.
