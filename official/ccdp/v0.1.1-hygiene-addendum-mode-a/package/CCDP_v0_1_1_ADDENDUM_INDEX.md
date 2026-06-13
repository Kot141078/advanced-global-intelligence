# CCDP v0.1.1 ADDENDUM INDEX

## Mode A addendum-only registry, reading order, package boundary, and release checklist

**Author:** Kotov Ivan  
**Location:** Bruxelles, Belgium  
**Year:** 2026  
**DOI:** Reserved DOI: 10.5281/zenodo.20680938  

**Package:** Child-`c` Development Protocol  
**Baseline package:** CCDP v0.1 DOI-bound / release-bound corpus slice  
**Addendum package:** CCDP v0.1.1 hygiene addendum  
**Document ID:** `CCDP_v0_1_1_ADDENDUM_INDEX`  
**Short name:** `ADDENDUM_INDEX`  
**Status:** Draft addendum package-control registry  
**Date:** 2026-06-13  
**Selected patch mode:** `MODE_A_ADDENDUM_ONLY`  
**Layer:** CCDP / v0.1.1 hygiene / publication integrity / package control  
**Document class:** addendum index / reading order / release-control manifest  
**Assertion class:** `C-A10` control-layer artifact; does not upgrade child-safety, legal, clinical, psychological, or product-readiness claims  
**Primary rule:** this index governs the v0.1.1 addendum pack; it does not rewrite the DOI-bound v0.1 baseline.  

---

## 0. Executive summary

This document is the package-level registry for the CCDP v0.1.1 hygiene addendum.

The addendum exists because CCDP v0.1 needs release hygiene clarification, but the baseline artifacts may already be DOI-bound, PDF-paired, SHA-manifested, release-bound, or otherwise externally citable.

The selected patch strategy is:

```text
Mode A = addendum-only patching.
```

Therefore:

1. CCDP v0.1 baseline artifacts remain historically frozen;
2. no v0.1 source Markdown file is silently edited in place;
3. no paired v0.1 PDF is silently regenerated under the same identity;
4. v0.1.1 corrections are issued as addendum documents;
5. current operational reading is baseline plus addendum;
6. if a baseline statement conflicts with a v0.1.1 hygiene clarification, the addendum controls current interpretation without changing the historical baseline artifact.

Current core addendum documents already created:

```text
DOI_SAFE_PATCH_STRATEGY.md
CCDP_v0_1_1_Hygiene_Patch_APPLIED.md
OBSOLETE.md
CANONICAL_PRECEDENCE_RULE.md
RAW_EVIDENCE_EXCEPTION_CANONICAL.md
CCDP_v0_1_1_ADDENDUM_INDEX.md
```

Required next addendum documents before package release:

```text
TERMINOLOGY_AXIS_CLARIFICATION.md
PUBLIC_TECHNICAL_SENSITIVE_SPLIT.md
CLEAN_START_CLARIFICATION.md
SOFT_SAFETY_RED_BLACK_MUST_CLARIFICATION.md
TRACEABILITY_CONFORMANCE_DELTA_v0_1_1.md
RELEASE_NOTES_v0_1_1.md
ADDENDUM_MANIFEST.json
SHA256SUMS
```

Controlling formula:

```text
CCDP v0.1 historical citation = frozen baseline.
CCDP current operational reading = CCDP v0.1 baseline + CCDP v0.1.1 hygiene addendum.
```

---

## 1. Purpose

This index answers six package-control questions:

1. What documents belong to the v0.1.1 addendum?
2. Which documents already exist and which remain pending?
3. In what order should the addendum be read?
4. How does the addendum interact with DOI-bound baseline artifacts?
5. Which hygiene issues are mitigated, pending, or deferred?
6. What must Codex or any future patch agent avoid changing?

This document is not a new child-safety protocol.

It is a publication-control and corpus-navigation layer.

---

## 2. Scope

### 2.1 In scope

This index governs:

- the CCDP v0.1.1 addendum package;
- addendum document registry;
- addendum reading order;
- current operational interpretation of CCDP v0.1 through addendum clarifications;
- DOI-safe patch routing;
- future Codex-safe addendum work;
- issue mitigation mapping for v0.1.1 hygiene;
- addendum package readiness checks;
- addendum manifest and SHA requirements.

### 2.2 Out of scope

This index does **not**:

- mutate any DOI-bound v0.1 artifact;
- edit paired PDFs;
- create a new full v0.1.1 source release by itself;
- replace `CCDP_v0_1_R_Corpus_Aligned.md`;
- redefine `c = a + b`;
- redefine SER / SER-FED;
- redefine Beacon, CBE, AGL, ARL, ARQ / `c[q]`, VXCX, EA-L4 / EATP, Continuity Bundle, Cold Wake, or L4 Witness;
- create legal advice;
- create clinical advice;
- validate child psychology;
- validate jurisdictional compliance;
- certify product readiness;
- claim that baseline files were patched in place.

---

## 3. Corpus bridge set

### 3.1 Explicit bridge

In the `c = a + b` corpus, a continuity-bearing entity must preserve witness integrity. A DOI-bound protocol corpus must do the same.

A published baseline is a witness object:

```text
stable identity
stable content
stable citation boundary
explicit correction path
```

The v0.1.1 addendum is the correction path. It gives current readers a safe interpretation layer without falsifying the historical baseline.

### 3.2 Quiet bridge I — Ashby / requisite variety

The CCDP package now has multiple hygiene failure modes: obsolete drafts, precedence ambiguity, raw-evidence duplication, terminology collisions, Red / Black ambiguity, clean-start ambiguity, public/sensitive split ambiguity, and traceability drift.

One patch operation cannot safely address all of them. The addendum pack supplies enough control variety to handle each issue through a separate bounded document.

### 3.3 Quiet bridge II — information theory / channel stability

A DOI-bound document is a time-stamped signal. Silent mutation means two readers may cite the same object but receive different content. That corrupts the citation channel.

The addendum preserves channel stability:

```text
old signal stays fixed
new corrective signal is added
current reading composes both
```

### 3.4 Earth paragraph

A signed inspection report is not overwritten after the fact. If a defect is discovered, a correction sheet is attached and logged. The old report remains reconstructable; the correction becomes part of the current file. CCDP v0.1.1 follows the same engineering discipline: do not erase the old witness; attach the correction where future builders can see it.

---

## 4. Core interpretation rule

### 4.1 Historical citation

For historical, bibliographic, DOI, archival, or fixed-release citation, CCDP v0.1 means:

```text
CCDP v0.1 baseline artifact exactly as published / released / DOI-bound.
```

The v0.1.1 addendum does not alter that object.

### 4.2 Current operational reading

For current implementation, review, audit, packaging, or future release preparation, CCDP SHOULD be read as:

```text
CCDP v0.1 baseline
+ CCDP v0.1.1 hygiene addendum
```

### 4.3 Conflict between baseline and addendum

If a v0.1 baseline statement conflicts with a v0.1.1 hygiene clarification, the current operational rule is:

```text
v0.1.1 addendum controls current interpretation
without rewriting the v0.1 baseline artifact
```

This is a supersession relation, not an in-place source edit.

### 4.4 Safety floor

No addendum document may weaken:

- immediate child physical safety;
- lawful jurisdictional obligations;
- parent corpus mechanisms;
- minimal disclosure;
- state-not-content discipline;
- raw child life minimization;
- sealed-zone protection;
- Red / Black routing discipline;
- witness integrity;
- adult migration autonomy;
- human responsibility anchor `a`.

If an addendum appears to weaken any of these, the addendum MUST be held for review.

---

## 5. Addendum status vocabulary

| Status | Meaning |
|---|---|
| `CREATED` | File exists in the addendum working set. |
| `CURRENT` | This index file. |
| `PLANNED_REQUIRED` | Required before the v0.1.1 addendum pack may be called release-ready. |
| `PLANNED_RECOMMENDED` | Recommended before public release, but not a hard package-control blocker. |
| `DEFERRED_MODE_B` | Requires a full versioned source release or future major/minor version. |
| `DEFERRED_REVIEW` | Requires legal, developmental, clinical, security, or implementation review. |
| `NOT_IN_MODE_A` | Prohibited or intentionally excluded under addendum-only strategy. |

---

## 6. Addendum document registry

### 6.1 Core addendum controls

| Step | Document | Status | Role |
|---:|---|---|---|
| 0 | `CCDP_v0_1_1_ADDENDUM_INDEX.md` | `CURRENT` | Package registry, reading order, and addendum control surface. |
| 1 | `DOI_SAFE_PATCH_STRATEGY.md` | `CREATED` | Mode A publication-integrity strategy and Codex-safe patch boundary. |
| 2 | `CCDP_v0_1_1_Hygiene_Patch_APPLIED.md` | `CREATED` | Applied work-order for HP-001…HP-013. |
| 3 | `CANONICAL_PRECEDENCE_RULE.md` | `CREATED` | Package-wide current interpretation and conflict-resolution rule. |
| 4 | `OBSOLETE.md` | `CREATED` | Obsolete / non-canonical material registry and discoverability mitigation. |
| 5 | `RAW_EVIDENCE_EXCEPTION_CANONICAL.md` | `CREATED` | Central raw-evidence exception protocol and sidecar discipline. |

### 6.2 Required remaining addendum controls

| Step | Document | Status | Role |
|---:|---|---|---|
| 6 | `TERMINOLOGY_AXIS_CLARIFICATION.md` | `PLANNED_REQUIRED` | Separates child maturity `C0–C5`, conformance `CCDP-0…5`, assertion `C-A*`, memory `M*`, dependency `D*`, personality formation `PF-*`, and related axes. |
| 7 | `PUBLIC_TECHNICAL_SENSITIVE_SPLIT.md` | `PLANNED_REQUIRED` | Defines public, technical, restricted, sensitive, and internal distribution boundaries. |
| 8 | `CLEAN_START_CLARIFICATION.md` | `PLANNED_REQUIRED` | Clarifies clean start as adult active-continuity clean start, not unlawful destruction of minimal witness/legal records. |
| 9 | `SOFT_SAFETY_RED_BLACK_MUST_CLARIFICATION.md` | `PLANNED_REQUIRED` | Clarifies Red / Black `MUST` behavior under urgent thresholds and unsafe guardian routes. |
| 10 | `TRACEABILITY_CONFORMANCE_DELTA_v0_1_1.md` | `PLANNED_REQUIRED` | Records traceability and conformance deltas for late modules without mutating baseline matrices. |
| 11 | `RELEASE_NOTES_v0_1_1.md` | `PLANNED_REQUIRED` | Release summary for the addendum pack. |
| 12 | `ADDENDUM_MANIFEST.json` | `PLANNED_REQUIRED` | Machine-readable addendum registry. |
| 13 | `SHA256SUMS` | `PLANNED_REQUIRED` | Addendum package integrity manifest. |

### 6.3 Recommended addendum support

| Document | Status | Role |
|---|---|---|
| `README.md` inside addendum directory | `PLANNED_RECOMMENDED` | Human landing page for the addendum directory. |
| `CODEX_DOI_SAFE_PATCH_RUNBOOK.md` | `PLANNED_RECOMMENDED` | Future Codex instructions for Mode A and possible Mode B. |
| `ERRATA_v0_1_TO_v0_1_1.md` | `PLANNED_RECOMMENDED` | Compact errata table for readers who need a one-page list. |
| `ADDENDUM_CITATION_GUIDE.md` | `PLANNED_RECOMMENDED` | How to cite baseline plus addendum in papers, releases, and audits. |

### 6.4 Not included in Mode A

| Artifact | Status | Reason |
|---|---|---|
| Edited v0.1 Markdown source files | `NOT_IN_MODE_A` | Would silently mutate DOI-bound / release-bound baseline. |
| Regenerated v0.1 PDFs under the same identity | `NOT_IN_MODE_A` | Would corrupt paired PDF / source citation boundary. |
| Replacement historical `SHA256SUMS` | `NOT_IN_MODE_A` | Historical integrity manifests must not be overwritten. |
| Full v0.1.1 source package | `DEFERRED_MODE_B` | Requires Mode B versioned release workflow. |
| Full product conformance certification | `DEFERRED_REVIEW` | Requires implementation, audit, security, developmental, and jurisdictional review. |

---

## 7. Canonical addendum reading order

### 7.1 Minimal current-reading path

For a reader who already has CCDP v0.1 and only needs to know how to interpret it now:

1. `CCDP_v0_1_1_ADDENDUM_INDEX.md`
2. `DOI_SAFE_PATCH_STRATEGY.md`
3. `CCDP_v0_1_1_Hygiene_Patch_APPLIED.md`
4. `CANONICAL_PRECEDENCE_RULE.md`
5. `RAW_EVIDENCE_EXCEPTION_CANONICAL.md`
6. `OBSOLETE.md`
7. remaining required clarifications as they are created

### 7.2 Release-control path

For maintainers preparing a v0.1.1 addendum release:

1. `DOI_SAFE_PATCH_STRATEGY.md`
2. `CCDP_v0_1_1_ADDENDUM_INDEX.md`
3. `CCDP_v0_1_1_Hygiene_Patch_APPLIED.md`
4. `OBSOLETE.md`
5. `CANONICAL_PRECEDENCE_RULE.md`
6. `RAW_EVIDENCE_EXCEPTION_CANONICAL.md`
7. `TERMINOLOGY_AXIS_CLARIFICATION.md`
8. `PUBLIC_TECHNICAL_SENSITIVE_SPLIT.md`
9. `CLEAN_START_CLARIFICATION.md`
10. `SOFT_SAFETY_RED_BLACK_MUST_CLARIFICATION.md`
11. `TRACEABILITY_CONFORMANCE_DELTA_v0_1_1.md`
12. `RELEASE_NOTES_v0_1_1.md`
13. `ADDENDUM_MANIFEST.json`
14. `SHA256SUMS`

### 7.3 Codex path

For Codex or another patch agent:

1. read `DOI_SAFE_PATCH_STRATEGY.md`;
2. read this index;
3. confirm Mode A is active;
4. list baseline files and addendum files separately;
5. fail closed on any requested baseline mutation;
6. create missing addendum documents only;
7. generate addendum manifest and SHA for addendum files only;
8. report any baseline physical move / edit as prohibited unless Mode B is explicitly selected.

---

## 8. Recommended Mode A directory layout

Preferred repository layout:

```text
ccdp-v0.1.1-hygiene-addendum/
  README.md
  CCDP_v0_1_1_ADDENDUM_INDEX.md
  DOI_SAFE_PATCH_STRATEGY.md
  CCDP_v0_1_1_Hygiene_Patch_APPLIED.md
  OBSOLETE.md
  CANONICAL_PRECEDENCE_RULE.md
  RAW_EVIDENCE_EXCEPTION_CANONICAL.md
  TERMINOLOGY_AXIS_CLARIFICATION.md
  PUBLIC_TECHNICAL_SENSITIVE_SPLIT.md
  CLEAN_START_CLARIFICATION.md
  SOFT_SAFETY_RED_BLACK_MUST_CLARIFICATION.md
  TRACEABILITY_CONFORMANCE_DELTA_v0_1_1.md
  RELEASE_NOTES_v0_1_1.md
  manifest/
    ADDENDUM_MANIFEST.json
    SHA256SUMS
  codex/
    CODEX_DOI_SAFE_PATCH_RUNBOOK.md
```

If a repository cannot use this exact layout, it MUST preserve the logical boundary:

```text
baseline artifacts != addendum artifacts
```

---

## 9. Baseline corpus relation

The addendum interprets but does not rewrite the baseline CCDP v0.1 package.

### 9.1 Baseline root and package-control files

The following baseline files remain frozen under Mode A if DOI-bound or release-bound:

```text
README.md
INDEX.md
CANONICAL_READING_ORDER.md
RELEASE_NOTES.md
OPEN_ISSUES.md
CCDP_v0_1_R_Corpus_Aligned.md
CCDP_Traceability_Matrix_v0_1.md
CCDP_Conformance_Test_Matrix_v0_1.md
CCDP_Contradiction_Register_v0_1.md
CCDP_v0_1_1_Hygiene_Patch.md
```

### 9.2 Baseline child-facing profiles and schemas

The following baseline files remain frozen under Mode A if DOI-bound or release-bound:

```text
CCDP_Threat_Model_v0_1.md
Child_Beacon_Extension_v0_1.md
Guardian_Topology_ARL_Matrix_v0_1.md
Child_Memory_and_Adult_Migration_v0_1.md
Soft_Safety_State_Signaling_Profile_v0_1.md
CCDP_Witness_Event_Schema_v0_1.md
CCDP_Memory_Map_JSON_Schema_v0_1.md
CCDP_Adult_Migration_Checklist_v0_1.md
CCDP_Sealed_Zone_Profile_v0_1.md
Child_Dependency_Audit_Profile_v0_1.md
Child_Physical_Agent_Perimeter_v0_1.md
External_Agent_Handshake_for_CCDP_v0_1.md
Peer_C_Child_Exchange_Profile_v0_1.md
Child_Experience_Exchange_Profile_v0_1.md
Child_cq_Signal_Profile_v0_1.md
CCDP_School_Interface_Profile_v0_1.md
CCDP_Red_Black_Escalation_Profile_v0_1.md
CCDP_Jurisdictional_Handoff_Notes_v0_1.md
CCDP_Developmental_Psychology_Review_Notes_v0_1.md
CCDP_Red_Team_Playbook_v0_1.md
```

### 9.3 Obsolete baseline material

Known obsolete material:

```text
CCDP v0_1.md
CCDP%20v0_1.md
```

Under Mode A, this addendum may state that the obsolete draft is non-canonical and must not be used as authority.

Physical move / rename / header insertion must not be performed inside a DOI-bound baseline package unless one of the following is true:

1. the file is not part of the DOI-bound baseline; or
2. the operation occurs in a new versioned release copy under Mode B; or
3. the operation is recorded as a new repository state without claiming to mutate the historical DOI artifact.

---

## 10. Hygiene issue mitigation map

| Issue / Patch | Addendum document | Mode A status | Notes |
|---|---|---|---|
| `CR-001` / `OI-001` obsolete draft discoverability | `OBSOLETE.md` | `MITIGATED_ADDENDUM` | Physical move/header still requires repo-safe handling. |
| `HP-004` / `OI-004` canonical precedence | `CANONICAL_PRECEDENCE_RULE.md` | `MITIGATED_ADDENDUM` | Baseline files not edited; current interpretation clarified. |
| `HP-007` / `OI-005` raw-evidence exception centralization | `RAW_EVIDENCE_EXCEPTION_CANONICAL.md` | `MITIGATED_ADDENDUM` | Baseline duplicate wording not replaced under Mode A. |
| `HP-005` / `OI-006` clean-start clarification | `CLEAN_START_CLARIFICATION.md` | `PENDING_REQUIRED` | Must clarify active adult continuity vs witness/legal records. |
| `HP-006` / `OI-007` terminology disambiguation | `TERMINOLOGY_AXIS_CLARIFICATION.md` | `PENDING_REQUIRED` | Must separate C0–C5, CCDP-0…5, C-A*, M*, D*, PF*, etc. |
| `HP-008` Soft Safety Red / Black `MUST` | `SOFT_SAFETY_RED_BLACK_MUST_CLARIFICATION.md` | `PENDING_REQUIRED` | Must remove MAY/MUST ambiguity for urgent thresholds. |
| `HP-010` / `OI-012` public / technical / sensitive split | `PUBLIC_TECHNICAL_SENSITIVE_SPLIT.md` | `PENDING_REQUIRED` | Required before public packaging. |
| `HP-002` / `OI-002` traceability refresh | `TRACEABILITY_CONFORMANCE_DELTA_v0_1_1.md` | `PENDING_REQUIRED` | Mode A delta instead of editing matrix. |
| `HP-003` / `OI-003` conformance refresh | `TRACEABILITY_CONFORMANCE_DELTA_v0_1_1.md` | `PENDING_REQUIRED` | Mode A delta instead of editing matrix. |
| `HP-009` / `OI-009` jurisdictional handoff reminders | `CLEAN_START_CLARIFICATION.md` + `RAW_EVIDENCE_EXCEPTION_CANONICAL.md` + future annex | `PARTIAL_ADDENDUM` | Full local annex deferred. |
| `HP-011` / `OI-015` integrity manifest | `SHA256SUMS` | `PENDING_REQUIRED` | Addendum files only. |
| `OI-008` developmental psychology review | DPRN + future review pack | `DEFERRED_REVIEW` | Not solved by hygiene addendum. |
| `OI-010` schema extraction | future `.schema.json` files | `DEFERRED_MODE_B_OR_NEXT_PACK` | Not solved by current addendum. |
| `OI-013` PDF production | addendum PDFs optional; baseline PDFs frozen | `PENDING_DECISION` | Do not regenerate baseline PDFs. |
| `OI-014` cross-repo placement | addendum directory / future repo plan | `PARTIAL_ADDENDUM` | Needs real repo decision. |

---

## 11. Addendum conformance language

A reader, implementer, auditor, or future package maintainer may say:

```text
This implementation / review reads CCDP v0.1 together with the CCDP v0.1.1 hygiene addendum.
```

They MUST NOT say:

```text
The original CCDP v0.1 DOI-bound files have been patched.
```

unless a Mode B full versioned release has actually been created.

A valid Mode A claim is:

```text
CCDP-v0.1 + v0.1.1-addendum current-reading compatible.
```

An invalid Mode A claim is:

```text
CCDP-v0.1.1 source package patched in place.
```

---

## 12. Citation guidance

### 12.1 Historical citation

For fixed historical reference, cite the baseline DOI / release artifact only.

Example form:

```text
Child-c Development Protocol (CCDP) v0.1, baseline DOI/release artifact.
```

### 12.2 Current operational citation

For current interpretation after addendum release, cite both baseline and addendum.

Example form:

```text
Child-c Development Protocol (CCDP) v0.1, read with CCDP v0.1.1 Hygiene Addendum, Mode A addendum-only package.
```

### 12.3 Quoting corrected material

If quoting or applying a clarified rule, cite the addendum document that contains the current rule, not only the baseline file.

Examples:

```text
canonical precedence -> CANONICAL_PRECEDENCE_RULE.md
raw exception -> RAW_EVIDENCE_EXCEPTION_CANONICAL.md
obsolete draft status -> OBSOLETE.md
DOI-safe patching -> DOI_SAFE_PATCH_STRATEGY.md
```

---

## 13. Codex carry-forward rules

Any future Codex run touching CCDP v0.1.1 MUST obey this block.

```text
CODEX_MODE = MODE_A_ADDENDUM_ONLY

DO NOT:
- edit DOI-bound baseline Markdown files in place;
- edit paired baseline PDFs;
- overwrite historical SHA256SUMS;
- move or delete DOI-bound baseline material silently;
- claim baseline files were patched when only addenda were created.

DO:
- create missing addendum documents;
- update addendum-only index / manifest / release notes if not DOI-bound yet;
- generate SHA256SUMS for addendum files only;
- report baseline changes as prohibited unless Mode B is explicitly selected;
- preserve baseline/addendum separation in Git diff.
```

Codex preflight checklist:

```text
1. Identify target file.
2. Classify target as baseline or addendum.
3. If baseline and DOI-bound status unknown, treat as DOI-bound.
4. If operation would mutate baseline, stop.
5. If operation creates addendum document, proceed.
6. Record created file in ADDENDUM_MANIFEST.json.
7. Update SHA256SUMS only for addendum files.
```

---

## 14. Release gates

### 14.1 Draft addendum gate

The addendum may be called a draft working set when the following exist:

```text
DOI_SAFE_PATCH_STRATEGY.md
CCDP_v0_1_1_ADDENDUM_INDEX.md
CCDP_v0_1_1_Hygiene_Patch_APPLIED.md
OBSOLETE.md
CANONICAL_PRECEDENCE_RULE.md
RAW_EVIDENCE_EXCEPTION_CANONICAL.md
```

Current status:

```text
DRAFT ADDENDUM GATE: PASS
```

### 14.2 Release-ready addendum gate

The addendum may be called release-ready only when the following exist:

```text
TERMINOLOGY_AXIS_CLARIFICATION.md
PUBLIC_TECHNICAL_SENSITIVE_SPLIT.md
CLEAN_START_CLARIFICATION.md
SOFT_SAFETY_RED_BLACK_MUST_CLARIFICATION.md
TRACEABILITY_CONFORMANCE_DELTA_v0_1_1.md
RELEASE_NOTES_v0_1_1.md
ADDENDUM_MANIFEST.json
SHA256SUMS
```

Current status:

```text
RELEASE-READY ADDENDUM GATE: FAIL / PENDING
```

### 14.3 Mode B trigger gate

Switch from Mode A to Mode B only if one of the following is true:

1. baseline source text must be rewritten for current use;
2. paired PDFs must be regenerated;
3. traceability / conformance matrices must be fully refreshed as source artifacts;
4. JSON schemas must be extracted into the canonical source package;
5. public package release requires a clean versioned source set;
6. a DOI provider or repository policy requires a new version rather than addendum-only interpretation;
7. an architecture contradiction is discovered that cannot be safely clarified by addendum.

Until Mode B is explicitly selected:

```text
Mode A remains active.
```

---

## 15. Anti-washing rule

No project, vendor, school, parent dashboard, AI product, agent framework, child-facing system, or safety claim may cite the v0.1.1 addendum as proof of CCDP compatibility unless it also provides evidence appropriate to the CCDP Conformance Test Matrix or its future v0.1.1 delta.

The addendum clarifies reading.

It does not certify products.

Invalid claim:

```text
We cite the CCDP addendum; therefore we are child-safe.
```

Valid claim form:

```text
We read CCDP v0.1 with the v0.1.1 hygiene addendum and provide a separate conformance evidence bundle for the claimed profile.
```

---

## 16. Non-expansion rule

The v0.1.1 addendum MUST NOT become a stealth expansion of CCDP.

Allowed:

```text
clarify
route
index
centralize
warn
supersede interpretation
record errata
record distribution boundaries
```

Not allowed:

```text
new root ontology
new child-safety mechanism
new legal doctrine
new clinical claim
new personhood claim
new product certification
new emergency law
new parent-rights doctrine
```

If a proposed addendum begins to add new mechanism rather than clarify package hygiene, it must be moved to a future profile or Mode B release track.

---

## 17. Current addendum working-set status

```text
CREATED:
  CCDP_v0_1_1_ADDENDUM_INDEX.md
  DOI_SAFE_PATCH_STRATEGY.md
  CCDP_v0_1_1_Hygiene_Patch_APPLIED.md
  OBSOLETE.md
  CANONICAL_PRECEDENCE_RULE.md
  RAW_EVIDENCE_EXCEPTION_CANONICAL.md

PENDING_REQUIRED:
  TERMINOLOGY_AXIS_CLARIFICATION.md
  PUBLIC_TECHNICAL_SENSITIVE_SPLIT.md
  CLEAN_START_CLARIFICATION.md
  SOFT_SAFETY_RED_BLACK_MUST_CLARIFICATION.md
  TRACEABILITY_CONFORMANCE_DELTA_v0_1_1.md
  RELEASE_NOTES_v0_1_1.md
  ADDENDUM_MANIFEST.json
  SHA256SUMS

PENDING_RECOMMENDED:
  README.md
  CODEX_DOI_SAFE_PATCH_RUNBOOK.md
  ERRATA_v0_1_TO_v0_1_1.md
  ADDENDUM_CITATION_GUIDE.md
```

---

## 18. Machine-readable registry draft

A future `ADDENDUM_MANIFEST.json` SHOULD encode at least:

```json
{
  "package": "CCDP v0.1.1 hygiene addendum",
  "baseline": {
    "name": "CCDP v0.1",
    "status": "doi_bound_or_release_bound_baseline",
    "mutation_policy": "frozen_under_mode_a"
  },
  "patch_mode": "MODE_A_ADDENDUM_ONLY",
  "created_at": "2026-06-13",
  "current_reading_formula": "CCDP v0.1 baseline + CCDP v0.1.1 hygiene addendum",
  "controls": [
    {
      "file": "CCDP_v0_1_1_ADDENDUM_INDEX.md",
      "status": "current",
      "role": "addendum registry and reading order"
    },
    {
      "file": "DOI_SAFE_PATCH_STRATEGY.md",
      "status": "created",
      "role": "DOI-safe Mode A strategy"
    },
    {
      "file": "CCDP_v0_1_1_Hygiene_Patch_APPLIED.md",
      "status": "created",
      "role": "applied hygiene work-order"
    },
    {
      "file": "OBSOLETE.md",
      "status": "created",
      "role": "obsolete material registry"
    },
    {
      "file": "CANONICAL_PRECEDENCE_RULE.md",
      "status": "created",
      "role": "current interpretation precedence rule"
    },
    {
      "file": "RAW_EVIDENCE_EXCEPTION_CANONICAL.md",
      "status": "created",
      "role": "canonical raw-evidence exception protocol"
    }
  ],
  "pending_required": [
    "TERMINOLOGY_AXIS_CLARIFICATION.md",
    "PUBLIC_TECHNICAL_SENSITIVE_SPLIT.md",
    "CLEAN_START_CLARIFICATION.md",
    "SOFT_SAFETY_RED_BLACK_MUST_CLARIFICATION.md",
    "TRACEABILITY_CONFORMANCE_DELTA_v0_1_1.md",
    "RELEASE_NOTES_v0_1_1.md",
    "ADDENDUM_MANIFEST.json",
    "SHA256SUMS"
  ],
  "prohibited_under_mode_a": [
    "baseline_markdown_in_place_edits",
    "baseline_pdf_regeneration",
    "historical_sha_overwrite",
    "silent_obsolete_draft_mutation",
    "claims_that_baseline_was_patched"
  ]
}
```

---

## 19. Acceptance checklist

Before the v0.1.1 addendum pack is considered release-ready:

```text
[ ] Baseline DOI-bound artifacts remain unmodified.
[ ] DOI_SAFE_PATCH_STRATEGY.md exists.
[ ] CCDP_v0_1_1_ADDENDUM_INDEX.md exists.
[ ] CCDP_v0_1_1_Hygiene_Patch_APPLIED.md exists.
[ ] OBSOLETE.md exists.
[ ] CANONICAL_PRECEDENCE_RULE.md exists.
[ ] RAW_EVIDENCE_EXCEPTION_CANONICAL.md exists.
[ ] TERMINOLOGY_AXIS_CLARIFICATION.md exists.
[ ] PUBLIC_TECHNICAL_SENSITIVE_SPLIT.md exists.
[ ] CLEAN_START_CLARIFICATION.md exists.
[ ] SOFT_SAFETY_RED_BLACK_MUST_CLARIFICATION.md exists.
[ ] TRACEABILITY_CONFORMANCE_DELTA_v0_1_1.md exists.
[ ] RELEASE_NOTES_v0_1_1.md exists.
[ ] ADDENDUM_MANIFEST.json exists.
[ ] SHA256SUMS exists for addendum files only.
[ ] Codex-safe runbook exists or is explicitly deferred.
[ ] No document claims that DOI-bound baseline files were edited in place.
[ ] Obsolete draft status is discoverable through addendum.
[ ] Current operational reading formula is present in release notes.
[ ] Public / technical / sensitive distribution boundary is present.
[ ] All remaining validation gaps remain marked as review/deferred, not solved.
```

---

## 20. Next required documents

Recommended creation order after this index:

```text
1. TERMINOLOGY_AXIS_CLARIFICATION.md
2. CLEAN_START_CLARIFICATION.md
3. SOFT_SAFETY_RED_BLACK_MUST_CLARIFICATION.md
4. PUBLIC_TECHNICAL_SENSITIVE_SPLIT.md
5. TRACEABILITY_CONFORMANCE_DELTA_v0_1_1.md
6. RELEASE_NOTES_v0_1_1.md
7. ADDENDUM_MANIFEST.json
8. SHA256SUMS
```

Rationale:

```text
terminology first -> prevents class collisions
clean start next -> prevents adult migration misread
Red/Black next -> prevents Soft Safety emergency ambiguity
release split next -> prevents unsafe public packaging
traceability/conformance delta next -> prevents matrix drift under Mode A
release notes / manifest / SHA last -> only after content freeze
```

---

## 21. Closing rule

The addendum is a correction layer, not a time machine.

It must not pretend that old artifacts changed.

It must make current reading safer.

It must leave enough evidence for a future maintainer to reconstruct:

```text
what v0.1 said
what v0.1.1 clarified
why the clarification was needed
which artifact controls current interpretation
which artifacts remain historical witnesses
```

Compact rule:

```text
Do not rewrite the witness.
Index the correction.
Control current reading.
Prepare the next clean version only when Mode B is chosen.
```
