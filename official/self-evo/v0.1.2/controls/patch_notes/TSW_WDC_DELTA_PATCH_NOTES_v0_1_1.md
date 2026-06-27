# TSW-WDC Delta Patch Notes v0.1.1

## Patch notes for `05_Self_Evo_TRIAD_Sister_Witness_WDC_Delta_v0_1_2_v0_1_1`

**Status:** Patch notes / control-layer artifact (advisory)  
**Date:** 2026-06-27  
**Patch notes ID:** `TSW_WDC_DELTA_PATCH_NOTES_v0_1_1`  
**Patch family:** `SELF-EVO v0.1.2 / WDC`  
**Target artifact:** `05_Self_Evo_TRIAD_Sister_Witness_WDC_Delta_v0_1_2.md`  
**Corrected artifact:** `05_Self_Evo_TRIAD_Sister_Witness_WDC_Delta_v0_1_2_v0_1_1.md`  
**Trigger review record:** `TSW_WDC_DELTA_REVIEW_RECORD_v0_1.md`  
**Trigger review result:** `PASS_WITH_LIMITS`  

---

## 1. Provenance

| Artifact | SHA-256 |
|---|---|
| Prior draft `05_Self_Evo_TRIAD_Sister_Witness_WDC_Delta_v0_1_2.md` | `c142d51a70c7f5ed5f60c324d430f823706a6ac41b6204a8cb4b1c6305450ef6` |
| Review record `TSW_WDC_DELTA_REVIEW_RECORD_v0_1.md` | `172179761559270f1969e849bbb8eb48b983a25b0d61929d2a447966d516bd45` |
| Corrected draft `05_Self_Evo_TRIAD_Sister_Witness_WDC_Delta_v0_1_2_v0_1_1.md` | `fdce8893da1e8630cb382dbc972a0a7c4ffc32bb848d065943c58442904cf621` |

---

## 2. Review finding addressed

### `TSW-WDC-DELTA-REV-F1` — CLOSED BY TEXT

The review found an internal route-vs-result mismatch:

```text
§8.2 TSW-WDC-DEGRADED / TSW-WDC-STARVED routes were softer than the canonical WDC-LC-004 result.
```

The correction aligns the TRIAD WDC state model with the canonical Local Checker result:

```text
WDC-LC-004 / wdc.witness_resource_floor_degraded -> FAIL
```

---

## 3. Textual changes

### 3.1 Metadata correction note

Added a `v0.1.1 correction note` stating that the revision closes `TSW-WDC-DELTA-REV-F1` and does not change WDC definitions, fields, role constraints, SYNAPS boundaries, annotations, examples, red lines, or the non-authority boundary.

### 3.2 §8.2 state-route alignment

Changed the `TSW-WDC-DEGRADED` and `TSW-WDC-STARVED` default routes.

Before:

```text
TSW-WDC-DEGRADED -> human gate / hold
TSW-WDC-STARVED  -> FAIL or HOLD; no integration
```

After:

```text
TSW-WDC-DEGRADED -> WDC-LC-004 -> FAIL on any material floor-degraded route; no integration
TSW-WDC-STARVED  -> WDC-LC-004 -> FAIL; no integration
```

### 3.3 §8.2 state-route precedence note

Added a note that the §8.2 table is subordinate to the canonical Local Checker result:

```text
If WDC-LC-004 / wdc.witness_resource_floor_degraded fires on a material route,
the canonical result is FAIL per §13.3 and §14.3.
```

`HOLD` or `HUMAN_GATE` may describe unresolved evidence or non-material pre-check triage, but they may not soften a confirmed `WDC-LC-004` finding.

### 3.4 §10.1 canonical result declaration

Added:

```text
canonical_result: FAIL
```

and an explicit route-precedence note:

```text
If WDC-LC-004 fires, the canonical FAIL controls.
A sister witness may record context or request human review,
but it may not downgrade this finding to HOLD or HUMAN_GATE.
```

### 3.5 §22.1 closure map

Added a review-finding closure map:

```text
TSW-WDC-DELTA-REV-F1 — CLOSED BY TEXT
```

---

## 4. No-change statement

This patch does not change:

```text
WDC definitions
WRF / CST / WRCG field set
TRIAD WDC trigger set
canonical SELF-EVO-04 vocabulary
canonical annotations
SYNAPS exchange boundary
role-specific TRIAD constraints
Rita / Liya / Ester boundaries
anti-echo logic
divergence preservation
example semantics
red-line set
implementation sketch route logic
checker non-authority boundary
```

---

## 5. Expected next review

Recommended next artifact:

```text
TSW_WDC_DELTA_REVIEW_RECORD_v0_1_1.md
```

Expected review target:

```text
Verify that TSW-WDC-DELTA-REV-F1 is closed and no route-vs-result regression remains.
```

Expected convergence target:

```text
PASS
```

---

## 6. Boundary

These patch notes are evidence of an append-first correction. They do not integrate the delta, do not release a `v0.1.2` package, do not approve self-evolution, and do not authorize deployment or live memory/resource changes.
