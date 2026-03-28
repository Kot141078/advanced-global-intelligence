# Integrity Manifests

This directory contains SHA-256 integrity manifests for the Advanced Global Intelligence stack.

## Files

- `SHA256SUMS_v1.1.txt`
  Canonical integrity manifest for release v1.1.

- `SHA256SUMS_v1.1_addendum_2026-01-20.txt`
  Post-release architectural additions (non-normative).

- `SHA256SUMS_stack_v2.0.txt`
  Cross-repository integrity manifest covering the full SER / AGI architectural stack.

- `SHA256SUMS_beacon_v0.1_2026-03-10.txt`
  Beacon Profile v0.1 integrity manifest (`protocols/beacon/`).

- `SHA256SUMS_arq_crosslinks_2026-03-25.txt`
  Additive cross-repo discoverability links from AGI to the canonical ARQ entry in SER.

- `SHA256SUMS_ea_l4_eatp_2026-03-28.txt`
  Canonical EA-L4 / EATP package manifest for `protocols/ea-l4-eatp/`.

- `SHA256SUMS_ea_l4_eatp_root_entry_2026-03-28.txt`
  Root-entry polish manifest for `START_HERE.md`, `MACHINE_ENTRY.md`, and aligned AGI navigation files.

## Notes

- Hashes follow the standard format:  
  `<sha256>  <relative path>`

- Cross-repository paths are canonical and stable.
- Stack manifests do not alter normative scope of prior releases.
