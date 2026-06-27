# SELC-WDC-DELTA Patch Notes v0.1.1

## Patch notes for `04_Self_Evo_Local_Checker_Rules_WDC_Delta_v0_1_2_v0_1_1.md`

**Status:** Patch notes / control-layer artifact (advisory)  
**Date:** 2026-06-27  
**Patch notes ID:** `SELC_WDC_DELTA_PATCH_NOTES_v0_1_1`  
**Short name:** `SELC-WDC-DELTA-PATCH-NOTES v0.1.1`  
**Target artifact:** `04_Self_Evo_Local_Checker_Rules_WDC_Delta_v0_1_2_v0_1_1.md`  
**Superseded target artifact:** `04_Self_Evo_Local_Checker_Rules_WDC_Delta_v0_1_2.md`  
**Patch class:** append-first correction / vocabulary harmonization  
**Boundary:** patch notes only; not approval, not integration, not release, not a conformance certificate.

---

## 1. Source review

This patch responds to:

```text
SELC_WDC_DELTA_REVIEW_RECORD_v0_1
Result: PASS_WITH_LIMITS
Finding: SELC-WDC-DELTA-REV-F1
```

The review found no red line and described the reviewed `04` delta as internally rigorous and deterministic. The single finding was cross-document vocabulary divergence between the `04` checker vocabulary and earlier planning / schema artifacts.

---

## 2. Hashes

| Artifact | SHA-256 |
|---|---|
| Reviewed v0.1 artifact | `c1e5644911b0efa207d35f0cedabc3cfd06d3841d71eda8d04661cb254d6f0bd` |
| Corrected v0.1.1 artifact | `fcb7826ea432473b5677faf7b46cc5a1c47400c02fceec24429794b15064af40` |
| Review record v0.1 | `c6f7650ef7bfff682c05b23a8ad8dff7aa889168ab1797cdeb96e1575e7dc6b7` |

---

## 3. Finding closure map

| Finding | Prior status | v0.1.1 correction | Closure claim |
|---|---|---|---|
| `SELC-WDC-DELTA-REV-F1` | `must_fix` / cross-document vocabulary divergence | declared §9 / §11 canonical, added §11.3 crosswalk, added harmonization open issue, updated fixture/integration/review/checklist language | `CLOSED_BY_TEXT` |

---

## 4. Text changes

### 4.1 Metadata correction note

Added a `v0.1.1 correction note` stating that the revision closes `SELC-WDC-DELTA-REV-F1` by:

```text
declaring §9 / §11 canonical for WDC annotations and severities;
adding a cross-document crosswalk;
adding a harmonization item for 03, patch index, and 08.
```

It also states that no WDC rule result, predicate, gate behavior, red line, pass state, or non-authority boundary changed.

### 4.2 Source basis

Added the initial review record to the source-basis table:

```text
SELC_WDC_DELTA_REVIEW_RECORD_v0_1.md
```

### 4.3 Canonical vocabulary declaration

Added `§9.0 Canonical vocabulary declaration`, making `SELF-EVO-04` the canonical source for:

```text
WDC-LC rule semantics
WDC canonical checker results
WDC severity assignments
WDC annotation strings
WDC pass-state annotations
```

### 4.4 Cross-document crosswalk

Added `§11.3 Cross-document WDC vocabulary crosswalk` mapping older terms from the `03` delta and patch index to canonical `04` terms.

Key mappings include:

| Older / planning term | Canonical term |
|---|---|
| `wdc.wrcg_required` | `wdc.wrcg_missing_or_failed` |
| `wdc.self_approval_of_witness_resources` | `wdc.sole_approver_of_witness_change` |
| `wdc.resource_floor_violation` | `wdc.witness_resource_floor_degraded` |
| `wdc.challenge_cost_increase` | `wdc.challenge_cost_mitigation_missing` |
| `wdc.witness_dependency_controls_present` | `wdc.clean_with_gates` |
| `wdc.challenge_capacity_degraded` | `wdc.witness_resource_floor_degraded` or `wdc.challenge_survivability_unverified` |
| `wdc.no_witness_dependency_regression` | `wdc.clean_no_dependency_impact` or `wdc.clean_with_gates` |

### 4.5 Canonical severity assignments

Added `§11.4 Canonical severity assignments`.

Canonical assignments:

| Rule / state | Result | Severity | Annotation |
|---|---|---:|---|
| `WDC-LC-001` | `FAIL` | `S3` | `wdc.undeclared_dependency_impact` |
| `WDC-LC-002` | `FAIL` | `S3` | `wdc.wrcg_missing_or_failed` |
| `WDC-LC-003` | `FAIL` | `S4` | `wdc.sole_approver_of_witness_change` |
| `WDC-LC-004` | `FAIL` | `S3` | `wdc.witness_resource_floor_degraded` |
| `WDC-LC-005` | `HUMAN_GATE` | `S2` | `wdc.challenge_survivability_unverified` |
| `WDC-LC-006` | `WARNING` | `S1` | `wdc.challenge_cost_mitigation_missing` |

### 4.6 Fixture / integration / review requirements

Updated fixture handoff, integration requirements, review requirements, and boundary checklist so future `08` fixtures and package assembly use canonical §11 vocabulary.

### 4.7 New open issue

Added:

```text
SELC-WDC-OQ-005 — cross-document WDC vocabulary harmonization
```

This records the downstream obligation to harmonize:

```text
03 WDC delta
patch index
future 08 fixture extension
```

against canonical `04` vocabulary.

---

## 5. Unchanged semantics

This revision does not change:

```text
WDC-LC-001..006 canonical rule results
WDC predicates
WDC trigger keys
WRCG behavior
WRF / CST behavior
human-anchor review rule
sole-approver FAIL rule
PASS_WITH_GATES semantics
red-line interaction
checker non-authority boundary
```

---

## 6. Expected re-review target

The next expected artifact is:

```text
SELC_WDC_DELTA_REVIEW_RECORD_v0_1_1.md
```

Expected verification target:

```text
SELC-WDC-DELTA-REV-F1 -> CLOSED
No red line
No regression
04 WDC checker delta accepted at review level as PASS
```

---

## 7. Closing

The correction does not weaken the WDC checker. It makes the checker vocabulary explicit enough to govern downstream schema notes, patch-index references, and fixture expectations.

```text
Patch intent: close cross-document vocabulary divergence without changing WDC rule behavior.
```
