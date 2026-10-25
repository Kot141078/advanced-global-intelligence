# Continuity Instrument v1.0.0 - English academic publication package

**Author: Ivan Kotov.** Independent researcher, Brussels, Belgium. ORCID: https://orcid.org/0009-0009-6002-9845.
Source version: 1.0.0, original build _02. Editorial edition: **academic-pdf-2**. Prepared: 25 October 2026.

## Start here: complete English reading route

English is the primary publication language. Start with [Understanding the Continuity Instrument](PDFs/01_CI_Explanatory_Paper_EN.pdf), a self-contained explanation of why CI was proposed, what evidence it uses, how the reference transformation works, and what its outputs can and cannot establish. It is a complete substantive English counterpart of the preserved Russian explanatory paper.

| Reading order | English document | Purpose |
|---|---|---|
| 1 | [01_CI_Explanatory_Paper_EN.pdf](PDFs/01_CI_Explanatory_Paper_EN.pdf) | Purpose, evidence, applications, worked example and limits of measurement |
| 2 | [03_CI_Technical_Specification_EN.pdf](PDFs/03_CI_Technical_Specification_EN.pdf) | Specification, observables, recognition profile and terminology |
| 3 | [04_CI_Implementation_and_Reproducibility_EN.pdf](PDFs/04_CI_Implementation_and_Reproducibility_EN.pdf) | Reference program, input/output contracts, reproducibility and known limitations |
| 4 | [05_CI_Evidence_Claims_and_Limitations_EN.pdf](PDFs/05_CI_Evidence_Claims_and_Limitations_EN.pdf) | Evidence status, claim boundaries and negative qualification results |
| 5 | [06_CI_Rights_and_Citation_EN.pdf](PDFs/06_CI_Rights_and_Citation_EN.pdf) | Authorship, component rights and citation |
| 6 | [07_CI_Publication_Guide_EN.pdf](PDFs/07_CI_Publication_Guide_EN.pdf) | Manual Zenodo deposit, record description and integrity checks |

All six English PDFs contain an academic title page, Ivan Kotov's authorship and ORCID, a table of contents and page numbering. The complete editable manuscripts, diagrams produced by the renderer, and all publication instructions support this English route.

## Preserved Russian supplement

[02_CI_Explanatory_Paper_RU.pdf](PDFs/02_CI_Explanatory_Paper_RU.pdf) is retained byte-for-byte, together with its editable manuscript. Its original academic-pdf-1 label remains visible because this document has not changed. It is an optional supplement to the primary English publication. See [EDITION_CHANGES.md](EDITION_CHANGES.md) for the scope of this revision.

## Source integrity and edition identity

source_original/ contains both the exact original ZIP (50765 bytes, SHA-256 be87dd926ed96e91e8de25bae2e18666f74ac738b173379ddc0092f98563f663) and its exact 22 extracted files. The source is unchanged. New PDFs are a reading/companion edition and do not patch the CLI or change the implementation version. The outer academic ZIP has its own externally supplied size and SHA-256.

editorial_sources/ contains the complete editable Markdown for all seven PDFs and the document metadata. examples/ contains one clearly synthetic 60-minute illustration and its checked output. verification/ contains the public review extract, package checks and the standard-library integrity verifier. build/ contains the PDF rendering script and build instructions.

## Verification

From this extracted package root: python verification/verify_package.py

On Linux, also run: sha256sum -c SHA256SUMS.txt

The outer manifest hashes all payload files except itself and SHA256SUMS.txt. SHA256SUMS.txt additionally hashes the manifest and excludes only itself. The outer ZIP checksum is supplied in a separate delivery sidecar; embedding a ZIP's own digest inside itself would create a circular dependency. `verification/LANGUAGE_COVERAGE.json` identifies the English publication route and the preserved Russian supplement.

## Scientific and rights boundary

R157 remains scoped open-synthetic evidence; R160 and R161 remain negative qualification attempts. No real-world continuity-age or identity result is established. The teaching example is illustrative only. Historical evidence archives and private corpus material are not included.

The author's scientific prose and descriptive metadata are CC BY 4.0. Original implementation, schemas and tests, and the new executable build/verification tools and example JSON, retain All Rights Reserved / no license grant. PDF 04 has explicit section-level mixed rights. FONT_LICENSE.txt preserves the embedded font terms. See PDF 06 and PACKAGE_MANIFEST.json for scopes; the package is not wholly open-source.

No Zenodo record was created or published in this preparation step. Use PDF 07, PUBLICATION_METADATA.json and ZENODO_DESCRIPTION.txt for the manual deposit with English as the primary language and two scoped rights entries. The intended deposit archive is `CI_CONTINUITY_INSTRUMENT_V1_0_0_ACADEMIC_EN_PACKAGE_20261025.zip`; it contains the preserved original _02 source and the Russian supplement.
