# Temporal AI Presence Profile v1.0 - Deposit Candidate Notes

## Publication state

This package is `deposit-ready`. Its standalone version DOI and concept DOI are unassigned. It is not yet a published Zenodo or GitHub release.

## Finalized from R1

- Removed release-candidate naming while preserving the normative sections 0 through 32.
- Added Zenodo-ready citation and deposit metadata with null DOI fields.
- Added public/local evidence separation and an explicit TAP-T03 deployment boundary.
- Included the smallest R2C-authorized public-safe R2B evidence set: ten byte-identical artifacts and six normalized derivatives.
- Excluded local Git bundles, forensic scratch, runtime state, deployment evidence, credentials, and private data.
- Added deterministic package, checksum, PDF, and ZIP validation surfaces.

## Unchanged doctrine

The canonical TAP definition, TAP versus `c` boundary, TAP-0 through TAP-6, TAP-C, TAP-X, memory classes, tool privilege classes, state machine, claim classes, conformance classes, TAP-T01 through TAP-T10, evidence classes, red-line failures, corpus bridges, Earth grounding, and non-collapse boundary are unchanged in substance.

## Evidence ceiling

TAP-T03 remains partial. T02, T06, T07, and T08 remain conservative publication candidates because the reviewed local implementation bundle is not distributed as a public immutable code reference. `M4_FULL_PASS=false`; `TAP-C=NOT CLAIMED`.

## Next publication step

Create a Zenodo draft, reserve the version DOI, record the concept DOI, do not publish, and run R3B to bind those identifiers and regenerate all dependent hashes and final assets.
