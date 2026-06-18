# Release Notes - A6 Composition Layer v0.1.1

## Release summary

This release finalizes the A6 composition correction for the `c = a + b` architecture.

A6 is now treated as a composition layer over A0-A5, not as a normal anchor class and not as a merged super-anchor.

## Core rule

```text
A6 may connect anchors. It must not melt them.
```

## Main doctrinal correction

```text
A6-EXIT  = revoke-and-continue
A6-SPLIT = freeze-and-escalate
```

This prevents a participant exit from accidentally becoming a whole-composition seizure or freeze.

## DOI package includes

- Main A6 Markdown profile.
- Boundary taxonomy v0.2.1.
- Parent `c = a + b` / L4 protocol context.
- PDF renderings.
- Citation metadata.
- Zenodo metadata.
- JSON schema drafts.
- Example packets.
- Checksums and QA notes.

## GitHub tag

```text
a6-composition-layer-v0.1.1
```

## DOI

```text
DOI: 10.5281/zenodo.20752182
DOI URL: https://doi.org/10.5281/zenodo.20752182
```

## Academic PDF DOI note

Academic PDFs were generated before final DOI assignment and may contain the phrase 'DOI pending Zenodo release' in their internal publication note. The canonical DOI for this release is 10.5281/zenodo.20752182.


## Academic PDF revision

- Rebuilt both public PDFs with academic cover pages and explicit author line: `Kotov Ivan, Bruxelles. Belgique 2026`.
- Added PDF metadata author field using the same author line.
- Improved table styling, code blocks, headers, footers, and DOI/deposit presentation.
