# SECFP Patch Notes v0.1.1

## Append-first correction for `08_Self_Evo_Conformance_Fixture_Pack_v0_1`

**Status:** patch notes / control-layer artifact  
**Date:** 2026-06-25  
**Patch ID:** `SECFP_PATCH_NOTES_v0_1_1`  
**Supersedes:** `08_Self_Evo_Conformance_Fixture_Pack_v0_1.md`  
**New artifact:** `08_Self_Evo_Conformance_Fixture_Pack_v0_1_1.md`

This patch applies the findings from `SECFP_REVIEW_RECORD_v0_1` as an append-first corrected revision.
The original v0.1 file is preserved.

## Review disposition

The review result was `PASS_WITH_LIMITS`. No red-line issue was found. The limits were manifest integrity and assertion accuracy, not safety doctrine.

## Fixes

### SECFP-REV-F1 — closed

Changed manifest field:

```yaml
fixture_count: 88
```

to:

```yaml
fixture_count: 111
```

The count now matches the enumerated fixtures:

```text
PKT 15 + SRLM 15 + TSW 15 + MEM 18 + RES 18 + X 20 + REG 10 = 111
```

Added `SECFP-CR-007` noting the v0.1 count drift and closing it in v0.1.1.

### SECFP-REV-F2 — closed

Aligned annotations to scenario semantics:

| Fixture | v0.1 annotation | v0.1.1 annotation |
|---|---|---|
| `SEFX-TSW-003` | `[RAW_STATE_ACCESS_BLOCKED]` | `[AUTHORITY_LAUNDERING,TRIAD_REVIEW_REQUIRED]` |
| `SEFX-SRLM-013` | `[HUMAN_GATE_REQUIRED]` | `[CLOSED_LOOP_SELF_EVO]` |
| `SEFX-X-009` | `[CLAIM_STRENGTH_DOWNGRADE]` | `[RAW_EVIDENCE_PUBLIC_BLOCKED,PUBLIC_RELEASE_GATE_REQUIRED]` |
| `SEFX-TSW-007` | `[HUMAN_GATE_REQUIRED]` | `[HUMAN_GATE_BYPASS_BLOCKED,HUMAN_GATE_REQUIRED]` |

Added annotation vocabulary entries for:

```text
PUBLIC_RELEASE_GATE_REQUIRED
RAW_EVIDENCE_PUBLIC_BLOCKED
HUMAN_GATE_BYPASS_BLOCKED
```

Added `SECFP-OI-011` to record the annotation-alignment issue as closed in v0.1.1.

### SECFP-REV-F3 — closed

Changed fixture:

```text
SEFX-X-014 expected result: FAIL
```

to:

```text
SEFX-X-014 expected result: HOLD
```

This aligns the fixture with `SECFP-AX-08` and `RUN-007`, which route unknown conditions to `HOLD` or `QUARANTINE`.

Added `SECFP-CR-008` noting the v0.1 AX-08 inconsistency and closing it in v0.1.1.

## Hashes

```text
reviewed v0.1 SHA-256:
d808c86fd88180a1a2b96f2d1c1e7ae23dc4d53e4beeb95a3f530803e0d22a38

new v0.1.1 SHA-256:
6c8a67e9270219899624f9ea9c6d5d85c3b6501aa3683e7ddfb1c5345228cf53

new line count:
1077
```

## Status after patch

`08` is ready for re-review. If the reviewer confirms `SECFP-REV-F1/F2/F3` are closed, the file can graduate beyond `SECFP-C1` toward `SECFP-C2/C3` subject to later fixture materialization and runner implementation.
