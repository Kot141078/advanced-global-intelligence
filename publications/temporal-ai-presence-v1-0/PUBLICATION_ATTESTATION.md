# Temporal AI Presence Profile v1.0 Publication Attestation

## Publication Identity

- Title: Temporal AI Presence Profile v1.0
- Publication date: 2026-08-23
- Version DOI: [10.5281/zenodo.22070960](https://doi.org/10.5281/zenodo.22070960)
- Concept DOI: [10.5281/zenodo.22070959](https://doi.org/10.5281/zenodo.22070959)
- Zenodo status: Published
- R3C pre-publication freeze commit: `092ceec806626f7a41ff95ede7f7508b4bf94751`
- Canonical public Git release commit: `897cdf7fe517c9137bb7dfa20e37e32644c5a4fe`
- Canonical release tag: `temporal-ai-presence-v1.0`

The Version DOI identifies the specific immutable v1.0 record. The Concept DOI is the Zenodo all-versions identifier. The Version DOI remains the primary citation DOI for v1.0.

## Byte Attestation

- Canonical PDF SHA-256: `04e3f33a96690a8801e4a8fc398b555f67bf1abffe0cf9d5c8662c404dc18db8`
- Canonical Markdown SHA-256: `eb90c28e4f3f564fccd6a9f5f7c87246eac0cf687917330523561af12e287ce9`
- Canonical Zenodo ZIP SHA-256: `f36fb08749f66693a00def4b739b867a9640db8bd7945ce5998c428baaa53671`
- Zenodo public upload identity: `8/8 PASS`
- Inner 38-file release payload identity: `38/38 PASS`

## Git Byte-Alignment Disclosure

The R3C pre-publication Git commit stored one evidence text file with LF line endings while the frozen and published Zenodo package preserved ten CRLF line endings. The text content was otherwise identical. Before the first GitHub push, a dedicated byte-alignment commit changed the Git blob to the exact published bytes and added a tracked `.gitattributes` policy. No substantive TAP theory, evidence value, test result, or claim was changed.

Files under `release/` are immutable after the public Git byte-alignment commit.

## Evidence Ceiling

- TAP-T03 remains partial with an explicit deployment-external boundary.
- `M4_FULL_PASS=false`
- `TAP-C=NOT CLAIMED`

No sufficient public immutable implementation-code reference was added by this alignment. TAP-T02, TAP-T06, TAP-T07, and TAP-T08 therefore retain their conservative public-candidate status.
