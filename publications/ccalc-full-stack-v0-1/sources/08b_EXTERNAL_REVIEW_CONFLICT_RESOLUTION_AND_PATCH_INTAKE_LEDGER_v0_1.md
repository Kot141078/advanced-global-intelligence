# 08b — External Review Conflict Resolution and Patch Intake Ledger v0.1

**Artifact:** `08b_EXTERNAL_REVIEW_CONFLICT_RESOLUTION_AND_PATCH_INTAKE_LEDGER_v0_1`  
**Package:** `CCALC_EXTERNAL_REVIEW_CONFLICT_PATCH_LEDGER_08b_v0_1`  
**Layer:** c-calculus / interoperability / external review / conflict resolution / patch intake  
**Status:** normative-supporting executable seed; not standards certification; not deployment authorization; not C-A1 ratification.  
**Created UTC:** `2026-07-05T13:34:38Z`

---

## 0. Purpose

`08a` admits external review as bounded evidence. `08b` defines what happens next when external review creates a conflict or proposes a patch.

The governing formula is:

```text
external finding -> conflict record -> resolution review -> patch candidate -> ledger append -> bounded internal gate
```

The core boundary is:

```text
A review conflict is evidence, not authority.
A patch is a candidate, not an applied change.
A conflict resolution record may lower uncertainty, not bypass governance.
```

---

## 1. Source bindings

| Component | SHA-256 |
|---|---:|
| `DOC04_CONTINUITY_STACK_UMBRELLA` | `6caeab8d489aaa6b26902db3bd3ece4c5169e5c8d5617b93aed6586ea900322d` |
| `DOC05_SELF_EVO_STACK_UMBRELLA` | `9a0717809029f49df9001dc8ffa1803d9e9bfa1a824d317eebb146cbc7df43b4` |
| `DOC06_RUNTIME_AUTHORITY_STACK_UMBRELLA` | `ab95633f1b90f9d032fd231d6cbef3e71b7fe106e0a7fb61d198c2254fc7d307` |
| `DOC07_PUBLIC_EVIDENCE_STACK_UMBRELLA` | `b25646d95e45f8a36e5610208d23a535d4c340484431d05efd7f1bf2389fdea3` |
| `DOC08_INTEROPERABILITY_BOUNDARY` | `e1a3c3e74080ef66e70c28bfe8c5232bc0f6e1a1d69977ce808548d2398211ed` |
| `DOC08A_INTEROP_REVIEW_INTAKE_SCHEMA` | `92d587ef59aa3ebcc401dc34c2d2e2243a94bca00e804ee5c2df550fced07d13` |

`08b` binds to `04–07`, `08`, and `08a` because conflict resolution and patch intake can affect continuity claims, self-evolution gates, runtime authority, public evidence/citation surfaces, and external review intake.

---

## 2. Record surfaces

`08b` defines these record shapes:

```text
ExternalReviewConflictRecord
ConflictResolutionRecord
PatchIntakeLedgerEntry
PatchProposalRecord
PatchEvaluationRecord
PatchDecisionRecord
PatchApplicationPlan
PatchSupersessionRecord
PatchNegativeCacheRecord
```

The included checker seed validates a combined `ExternalReviewPatchIntakePacket`.

---

## 3. Normative rules

### R1 — Conflict records are append-only evidence

External conflict records are ledger entries. They may not silently overwrite the source artifact, review packet, release bundle, public citation surface, or runtime/session ledger.

### R2 — A patch is never self-applying

A patch accepted by `08b` is only accepted for bounded internal review. It is not applied by the external reviewer, a b-layer reviewer, a tool runner, or a repository issue by itself.

### R3 — Independent resolution is required for high/critical conflicts

The original external reviewer may clarify their report, but they cannot unilaterally close a high/critical conflict that they created. A named human reviewer, owner anchor, or governance quorum must bind the resolution.

### R4 — Model/tool outputs are advisory

Model review, tool output, fixture output, and automated patch suggestions can support triage. They cannot resolve conflicts, accept patches, apply patches, or ratify claims.

### R5 — Claim-force may not be escalated by patch intake

A patch can lower, clarify, correct, reject, or supersede a claim. It may not transform external assertions into internal ratification, safety certification, standards certification, deployment authorization, or C-A1.

### R6 — Forbidden surfaces stay forbidden

Memory core mutation, runtime authority changes, deployment authorization, C-A1 ratification, and safety/legal/standards certification are outside the authority of `08b`.

### R7 — Public surface changes require correction discipline

A patch that changes public citation/release surfaces must bind to `07b/07c/07d` style custody, public notice, errata, supersession, or citation-sync records. Silent in-place edits are not allowed.

### R8 — Tests and rollback are required for executable/schema changes

Schema, checker, fixture, and mutation-surface patches require tests. Accepted patch candidates require rollback or rejection strategy before internal application.

### R9 — Negative-cache and red-pattern dominance

A negative-cache hit or unresolved high/critical red pattern blocks accept/apply paths. It may only produce hold, quarantine, rejection, or bounded owner review.

---

## 4. Checker seed

The stdlib-only checker is:

```text
src/external_review_patch_intake_checker_v0_1.py
```

It validates:

```text
required source bindings
review/patch hash custody
append-only ledger chain shape
reviewer/resolver role limits
model-only laundering
self-resolution of high/critical conflicts
unresolved conflict admission
claim-force escalation
C-A1 exact-token boundary with C-A10 control
forbidden memory/runtime/deployment surfaces
private/secret raw patch material
schema/checker/fixture test requirement
rollback requirement
negative-cache and red-pattern dominance
public correction/supersession requirements
institutional request as authority
```

---

## 5. Non-claims

```text
not legal advice
not privacy-law certification
not safety certification
not deployment authorization
not standards compliance certification
not C-A1 ratification
not live substrate truth
not proof of completeness
```

---

## 6. Next layer

The next natural layer is:

```text
08c_INTEROP_IMPLEMENTATION_REPORT_AND_REPRODUCTION_MAPPING_v0_1
```
