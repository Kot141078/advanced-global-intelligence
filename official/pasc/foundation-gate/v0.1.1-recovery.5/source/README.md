# Post-Anchor Succession and Custody (PASC) Foundation Gate

**Version:** v0.1.1-recovery.5  
**Author:** Ivan Kotov  
**ORCID:** 0009-0009-6002-9845  
**Affiliation:** Independent Researcher, Brussels, Belgium  
**Language:** English

## 1. Overview

This release presents the PASC Foundation Gate as a public technical research package.
PASC addresses a narrow post-anchor governance question: which exact negative actions may
preserve evidence and reduce exposure without converting property, credentials, custody,
relationship, archive access, provider control, or institutional force into successor
authority.

The release is a research candidate. It is not a conformance certificate, legal instrument,
implementation specification, deployment authorization, or claim that F0 has passed.

## 2. Scope and claim ceiling

PASC is negative-only. It may evaluate exact requests to reduce, revoke, or perform tightly
bounded in-place preservation and integrity operations. It does not establish identity,
continuity, personhood, succession, legal standing, custody authority, keyholding authority,
provider authority, jurisdiction, recovery roots, release, reactivation, or Runtime Authority.

Current release status:

```text
F0_OUTCOME = NOT_PASSED
FOUNDATION_SEMANTICS_LOCKED = false
F1_DRAFTING = PROHIBITED
FORMALIZATION_OR_VALIDATOR = PROHIBITED
IMPLEMENTATION_OR_DEPLOYMENT = PROHIBITED
```

## 3. Package contents

- `PASC_FOUNDATION_GATE_v0_1_1_RECOVERY_5.pdf` - primary academic publication PDF.
- `PASC_CANONICAL_BASELINE_INVENTORY_v0_1_1_RECOVERY_5.pdf` - human-readable inventory supplement.
- `package/` - the eight English Markdown research documents and the canonical JSON inventory.
- `PASC_RELEASE_STATUS_v0_1_1_RECOVERY_5.md` - public release status and limitations.
- `PASC_FOUNDATION_GATE_MANIFEST_v0_1_1_RECOVERY_5.json` - closed member inventory.
- `SHA256SUMS.txt` - SHA-256 values for every package file except itself.
- `.zenodo.json` and `CITATION.cff` - machine-readable publication and citation metadata.
- `LICENSE.md`, `RELEASE_NOTES.md`, and `REPRODUCIBILITY.md` - rights, release delta, and verification method.

Internal decision sheets, cold-review working files, deposition instructions, and superseded
historical archives are intentionally excluded from this public release.

## 4. Source-of-record and PDF relation

The UTF-8 Markdown and JSON members under `package/` are the machine-readable sources of
record. The PDFs are citable human-readable renderings with title pages, authorship,
publication metadata, stable chapter order, and bookmarks. If a typographic line break or
PDF text extraction creates ambiguity, the corresponding UTF-8 source controls.

Administrative files such as this README, the license, release notes, and integrity records
are not duplicated as PDFs.

## 5. Integrity verification

From the package root:

```bash
sha256sum -c SHA256SUMS.txt
```

The external release checksum file distributed beside the ZIP binds the ZIP and the two
standalone PDFs uploaded to Zenodo. The standalone PDFs must be byte-identical to the copies
inside the ZIP.

## 6. Citation

Use the metadata in `CITATION.cff`. Until a DOI is assigned, cite the title, author, version,
release date, and exact external SHA-256 values.

## 7. License

Unless a file states otherwise, this release is licensed under
CC BY-NC-ND 4.0. See `LICENSE.md`.
