# Temporal AI Presence Profile v1.0 Release Candidate

This directory is the standalone source package for the Temporal AI Presence Profile v1.0 release candidate.

## Status

```text
publication_status = release-candidate
doi = null
implementation_conformance = not claimed
```

The package is ready for owner and independent source review. It is not a published DOI release, a TAP conformance certificate, a website deployment, or an implementation-closure result.

## Canonical source

`Temporal_AI_Presence_Profile_v1_0_RC.md` is the governing human-readable source. The PDF is a rendered reader copy. If the two differ, the Markdown controls.

The canonical definition remains:

```text
Temporal AI Presence = sustained bounded AI participation across time.
```

## Reading order

1. `Temporal_AI_Presence_Profile_v1_0_RC.md`
2. `TAP_CLAIM_AND_BOUNDARY_MAP_v1_0.md`
3. `PROVENANCE.md`
4. `TAP_EVIDENCE_BASELINE_v1_0.json`
5. `temporal_ai_presence_v1_0.json`
6. `RELEASE_NOTES_v1_0_RC.md`

## Package map

| Artifact | Function |
|---|---|
| `Temporal_AI_Presence_Profile_v1_0_RC.md` | Canonical normative profile source. |
| `Temporal_AI_Presence_Profile_v1_0_RC.pdf` | Pre-publication reader rendering. |
| `CITATION.cff` | Standalone release-candidate citation metadata. |
| `PROVENANCE.md` | Commit-bound historical and publication lineage. |
| `TAP_CLAIM_AND_BOUNDARY_MAP_v1_0.md` | Compact claim and inference boundaries. |
| `TAP_EVIDENCE_BASELINE_v1_0.json` | Frozen R0 evidence-state projection. |
| `temporal_ai_presence_v1_0.json` | Machine-readable normative instance. |
| `temporal_ai_presence_v1_0.schema.json` | JSON Schema for the normative instance. |
| `RELEASE_NOTES_v1_0_RC.md` | Changes, invariants, and remaining work. |
| `TAP_V1_PACKAGE_ARCHITECTURE.md` | Package-layout precedent and custody rules. |
| `TAP_V1_ANTI_ECHO_AUDIT.md` | Cross-file duplication and theory-boundary audit. |
| `manifest.json` | Machine-readable package inventory. |
| `SHA256SUMS` | Byte-level integrity manifest. |

## Relationships

- The historical TAP v0.1 profile remains immutable inside `c Hardening Pack v0.1`, DOI `10.5281/zenodo.20532198`.
- MOT-c v0.1, DOI `10.5281/zenodo.22060517`, is a later downstream/adjacent theory of motivational formation inside continuing c-class lines. It is not a replacement definition or implementation proof for TAP.

## Integrity rule

`manifest.json` inventories package artifacts except itself and `SHA256SUMS` to avoid recursive hashing. `SHA256SUMS` hashes every package artifact except itself, including `manifest.json`.
