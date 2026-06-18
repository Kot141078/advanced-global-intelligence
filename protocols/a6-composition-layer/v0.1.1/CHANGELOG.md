# Changelog

## v0.1.1 - 2026-06-18

### Fixed

- Corrected the A6-EXIT / ARL escalation ambiguity.
- Ordinary participant exit is now treated as `revoke-and-continue`.
- Composition split remains `freeze-and-escalate`.
- ARL review now freezes only affected cross-boundary compartments for exit, while preserving unaffected mapped operation.

### Added

- Section 6.9 Resource and Custodian Map.
- Temporary fail-closed rule for nested A6 recursion.
- Release metadata section in the A6 profile.
- JSON schema drafts for witness packets and resource/custodian maps.
- Example witness and resource/custodian packets.
- DOI/GitHub metadata: `CITATION.cff`, `.zenodo.json`, release notes, QA notes, manifest, and checksums.

### Changed

- `Anchor Class Boundaries` moved to v0.2.1.
- Section 12 in `Anchor Class Boundaries` is now a stable A6 summary and pointer to `A6 Composition Layer v0.1.1`.
- A6 operational detail is no longer duplicated inside the boundary taxonomy.

### Non-claims

- No legal personhood.
- No public-law activation.
- No post-anchor sovereignty.
- No merged identity.
- No product, clinical, or safety certification.
