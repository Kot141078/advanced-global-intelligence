# Package QA

## Text QA

- A6-EXIT / A6-SPLIT ambiguity corrected.
- Resource and Custodian Map added as Section 6.9.
- Nested A6 recursion temporarily set to review-first / externalize-last.
- Anchor Class Boundaries v0.2.1 Section 12 reduced to summary and pointer.
- Anti-claim language retained: no legal personhood, no public-law activation, no merged identity.

## PDF QA

PDFs were regenerated from Markdown and rendered to PNG pages for visual inspection.

- `A6_Composition_Layer_v0.1.1_academic.pdf`: 27 pages, A4.
- `ANCHOR_CLASS_BOUNDARIES_v0.2.1_academic.pdf`: 25 pages, A4.

Sample pages inspected from beginning, middle, and end. No gross clipping, black squares, missing text blocks, or table overflow detected in sampled render pages.

## Packaging QA

- Root metadata present: `README.md`, `CITATION.cff`, `.zenodo.json`, `LICENSE.md`.
- Release metadata present: `RELEASE_NOTES_v0.1.1.md`, `CHANGELOG.md`, `DOI_GITHUB_RELEASE_CHECKLIST.md`.
- Canonical DOI recorded: `10.5281/zenodo.20752182` / https://doi.org/10.5281/zenodo.20752182.
- Checksums included.
- Package contains Markdown source and PDF renderings.


## Academic PDF QA update

- Rebuilt PDFs with WeasyPrint academic HTML/CSS pipeline.
- Title pages include: `Kotov Ivan, Bruxelles. Belgique 2026`.
- PDF metadata author field set to the same line.
- Render verification performed after rebuild.
