# SELF-EVO Addendum 01 — WDC Patch Notes v0.1.1

## Patch notes for `SELF_EVO_ADDENDUM_01_Witness_Dependency_Capture_Profile_v0_1_1.md`

**Status:** append-first patch notes / advisory control artifact  
**Date:** 2026-06-27  
**Author:** Kotov Ivan  
**Patch target:** `SELF_EVO_ADDENDUM_01_Witness_Dependency_Capture_Profile_v0_1.md`  
**Corrected artifact:** `SELF_EVO_ADDENDUM_01_Witness_Dependency_Capture_Profile_v0_1_1.md`  
**Review source:** `SELF_EVO_ADDENDUM_01_WDC_REVIEW_RECORD_v0_1.md`  
**Review result:** `PASS_WITH_LIMITS`  

---

## 1. Patch boundary

This patch does not mutate the DOI-bound Self-Evo v0.1.1 package.

It creates an append-first corrected addendum revision for the Witness Dependency Capture control surface.

The corrected addendum remains:

```text
not integrated into the DOI-bound package
not conformance-tested
not implementation-ready
not deployment authorization
not a safety proof
```

---

## 2. Closed review findings

### WDC-REV-F1 — closed in v0.1.1

**Finding:** local-checker additions used severity/prose instead of the canonical Self-Evo checker result enum; `WDC-LC-006` used compound “warn or fail”; implementation sketch returned `pass_with_limits(...)`, which belongs to review-record vocabulary.

**Patch:**

- added canonical checker result enum reference;
- rewrote `WDC-LC-001..006` as rule table with `canonical result`, `severity`, and `typical annotation`;
- resolved `WDC-LC-006` to `WARNING` with severity escalation;
- changed implementation sketch to return `pass_with_gates(...)`, `pass_result(...)`, `human_gate(...)`, `warning(...)`, or `fail(...)` as appropriate.

### WDC-REV-F2 — closed in v0.1.1

**Finding:** fixtures and worked example used compound results and `PASS_WITH_LIMITS`, a review verdict, where checker vocabulary requires a canonical checker result such as `PASS_WITH_GATES`.

**Patch:**

- rewrote all WDC fixtures with one `canonical_result` plus `annotations`;
- changed fixture conditional pass cases from `PASS_WITH_LIMITS` to `PASS_WITH_GATES`;
- added WDC annotation vocabulary;
- rewrote the worked example as one `canonical_result: FAIL` with triggered rules and annotations.

### WDC-REV-F3 — closed in v0.1.1

**Finding:** addendum referenced Self-Evo v0.1.1 parent files by name only, without SHA-256 source-basis binding.

**Patch:**

- added source-basis / subject hash table;
- bound SELF-EVO-05, 07, 08, 09, and 10 by accepted v0.1.1 SHA-256;
- recorded parent package DOI, archival ZIP SHA-256, and GitHub package integrity commit.

### WDC-REV-N1 — addressed in v0.1.1

**Nit:** contradiction-register candidate used `OPEN / ADDENDUM-RECORDED`, where `ADDENDUM-RECORDED` is not part of the harmonized status vocabulary; bridge set was valid but lean.

**Patch:**

- changed contradiction status to `OPEN`;
- moved `ADDENDUM-RECORDED` to source note rather than status;
- added explicit information-theory bridge describing witness dependency as dissent-channel capacity loss.

---

## 3. Remaining state

The corrected artifact should now be ready for re-review.

Expected next review target:

```text
SELF_EVO_ADDENDUM_01_Witness_Dependency_Capture_Profile_v0_1_1.md
```

Expected review question:

```text
Do WDC-REV-F1, WDC-REV-F2, WDC-REV-F3, and WDC-REV-N1 close cleanly without introducing new red lines?
```
