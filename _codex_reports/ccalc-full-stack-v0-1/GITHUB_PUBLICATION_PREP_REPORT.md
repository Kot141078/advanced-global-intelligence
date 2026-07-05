# GitHub publication prep report

Contract: `CODEX_ITERATION_GITHUB_PUBLICATION_03.md`

Repository: `Kot141078/advanced-global-intelligence`
Branch: `release/ccalc-full-stack-v0.1-zenodo-21205427`
Publication folder: `publications/ccalc-full-stack-v0-1`
DOI: <https://doi.org/10.5281/zenodo.21205427>

## Actions

- Created GitHub publication surface for the DOI-bound clean package.
- Copied the clean package ZIP and sidecar.
- Copied 29 PDFs, 29 source Markdown files, and 45 component ZIPs with 45 corrected sidecars.
- Copied compact release evidence and sanitized checker summary package paths.
- Updated copied metadata/manifests from pre-publication DOI wording to published DOI wording for this GitHub surface.
- Added narrow `.gitattributes` rules for stable publication-folder line endings and binary ZIP/PDF preservation.
- Generated bridge readmes, release notes draft, reproducibility notes, integrity notes, `SHA256SUMS.txt`, `.zenodo.json`, `CITATION.cff`, and `PUBLICATION_RECORD.json`.
- Updated the root `README.md` with one compact publication entry.

## Verification

- Clean ZIP SHA256: `8281cc61d83623133319aa00c7cab85a03d2e6b08ec205363e3afbdface64f26`
- Expected SHA256: `8281cc61d83623133319aa00c7cab85a03d2e6b08ec205363e3afbdface64f26`
- ZIP readable: `True`
- SHA256SUMS verification: `PASS`
- CFF/DOI/license check: `True`
- Zenodo JSON DOI/license/parse check: `True / True`
- Publication record JSON parse: `True`
- Path leak scan: `PASS (0 hits)`
- Secret scan: `PASS (0 hits)`
- Pre-publication DOI wording scan: `PASS (0 hits)`
- Non-claims exact sentence present: `True`
- Plus-boundary exact sentence present: `True`

## Counts

- Publication files hashed: 192
- Clean package ZIP members: 492
- Academic PDFs: 29
- Source Markdown files: 29
- Component ZIPs: 45
- Corrected component ZIP sidecars: 45
- Release evidence files: 8

## GitHub controls

- Pushed: false
- GitHub Release created: false
- Commit SHA: pending until local commit

## Diff summary

- Added `publications/ccalc-full-stack-v0-1/`.
- Added `_codex_reports/ccalc-full-stack-v0-1/` prep report files.
- Updated root `README.md` only with a compact publication entry.
- Updated `.gitattributes` with narrow publication-folder rules.

## Open issues / human decisions

- none

Manual decisions remain required before push or GitHub Release creation.
