# SELF-EVO v0.1.2 Patch Index Patch Notes v0.1.1

## Append-first correction notes for `SELF_EVO_v0_1_2_PATCH_INDEX_v0_1_1.md`

**Status:** patch notes / package-control companion artifact  
**Date:** 2026-06-27  
**Patch notes ID:** `SELF_EVO_v0_1_2_PATCH_INDEX_PATCH_NOTES_v0_1_1`  
**Corrected artifact:** `SELF_EVO_v0_1_2_PATCH_INDEX_v0_1_1.md`  
**Corrected artifact SHA-256:** `ea2a485569b220d84d711ae520da779af2cabddcb7f1d8032afb2a9208d5108e`  
**Corrected artifact line count:** `811`  
**Superseded artifact:** `SELF_EVO_v0_1_2_PATCH_INDEX.md`  
**Superseded artifact SHA-256:** `5892e95aa92ccf7c8d2d8f8d47cc2d0395ff7071660935c6b46a88df1d2645c8`  
**Review driver:** `SELF_EVO_v0_1_2_PATCH_INDEX_REVIEW_RECORD_v0_1.md`  
**Review driver SHA-256:** `548f37575c5d51d6ed4abb1120551943afadd58bb41a43d6ad9df20188eee0a5`  
**Review result before correction:** `PASS_WITH_LIMITS`  
**Correction mode:** append-first; prior draft and review record are retained.

> Boundary: these notes do not release `v0.1.2`, do not mutate the DOI-bound `v0.1.1` package, do not authorize deployment, and do not convert review into authority.

---

## 1. Reason for patch

The v0.1 patch index was reviewed as `PASS_WITH_LIMITS`. The review found no red line and no safety regression, but identified three issues to close before a clean `PASS` convergence:

```text
PATCH-REV-F1 — missing corpus bridge set + earth paragraph
PATCH-REV-F2 — missing unaffected-artifact set and master-gate rationale
PATCH-REV-F3 — schema-vs-sketch mismatch for challenge_cost_mitigation_ref
```

This v0.1.1 correction closes those findings without changing the intended WDC patch scope.

---

## 2. Changes made

### 2.1 Closure of `PATCH-REV-F1`

Added `§2.2 Corpus bridge set for patching and versioning`, including:

```text
c = a + b bridge
information-theory bridge
cybernetics bridge
physiology bridge
earth paragraph
```

This aligns the patch index with the bridge discipline applied to accepted Self-Evo artifacts.

### 2.2 Closure of `PATCH-REV-F2`

Added `§5.3 Explicit unaffected-artifact set`, covering:

```text
01 / C_Self_Evolution_Gate_CGAM_TRIAD_SRLM_Profile_v0_1_1.md
02_SRLM_Bounded_Growth_Contour_Profile_v0_1_1.md
06_Self_Evo_Memory_Gate_and_EA_Profile_v0_1_1.md
```

The section states that these artifacts require no direct v0.1.2 text delta because WDC outcomes propagate through the `03` schema and `04` Local Checker aggregation into the existing gate stack.

### 2.3 Closure of `PATCH-REV-F3`

Added the missing schema field:

```yaml
challenge_cost_mitigation_ref: ""   # required when increases_challenge_cost = true
```

This reconciles the `§6` schema delta with the `§16` implementation-handoff sketch.

### 2.4 Checklist update

Added closed review items to `§17`:

```text
[x] Add corpus bridge set + earth paragraph to patch index.
[x] State unaffected artifacts 01/02/06 and master-gate inheritance rationale.
[x] Reconcile challenge_cost_mitigation_ref between schema and implementation sketch.
```

Added `§17.1 Patch-index review findings closed in v0.1.1`, mapping `PATCH-REV-F1/F2/F3` to the exact closure sections.

---

## 3. Non-changes

This correction does not:

```text
change the WDC control surface
change WDC-LC-001..006 semantics
change WDC-FIX-001..005 semantics
change SE-CONTRA-WDC-001
change SE-OI-WDC-001
release v0.1.2
modify the DOI-bound v0.1.1 package
perform package integration
claim conformance
claim deployment authorization
```

---

## 4. Expected re-review focus

A re-review should check only whether:

```text
PATCH-REV-F1 is closed by §2.2
PATCH-REV-F2 is closed by §5.3
PATCH-REV-F3 is closed by §6
no new red line or regression was introduced
```

---

## 5. Closing

```text
Patch notes verdict: correction prepared.
PATCH-REV-F1/F2/F3 addressed in the corrected patch index.
No integration performed.
No release performed.
Decision remains with c and a.
```
