# CCDP RELEASE NOTES v0.1.1

## Hygiene addendum release notes for CCDP v0.1 DOI-bound / release-bound baseline

**Author:** Kotov Ivan  
**Location:** Bruxelles, Belgium  
**Year:** 2026  
**DOI:** Reserved DOI: 10.5281/zenodo.20680938  

**Package:** Child-`c` Development Protocol  
**Baseline package:** CCDP v0.1 DOI-bound / release-bound corpus slice  
**Addendum package:** CCDP v0.1.1 hygiene addendum  
**Document ID:** `RELEASE_NOTES_v0_1_1`  
**Short name:** `RELEASE_NOTES v0.1.1`  
**Status:** Draft release notes / addendum release-control artifact  
**Date:** 2026-06-13  
**Selected patch mode:** `MODE_A_ADDENDUM_ONLY`  
**Layer:** CCDP / v0.1.1 hygiene / release notes / publication integrity  
**Document class:** release notes / package-control artifact  
**Assertion class:** `C-A10` control-layer artifact; does not upgrade child-safety, legal, clinical, psychological, developmental, or product-readiness claims  
**Primary rule:** CCDP v0.1.1 is an addendum-only hygiene release. It clarifies how CCDP v0.1 must be read now. It does not silently rewrite the DOI-bound v0.1 baseline.  

---

## 0. Release summary

CCDP v0.1.1 is a **hygiene addendum release** for the CCDP v0.1 child-facing persistent AI entity protocol pack.

It does not introduce a new child-safety mechanism.

It does not replace CCDP v0.1.

It does not mutate DOI-bound baseline artifacts.

It fixes package-control risks that became visible after the v0.1 baseline grew into a multi-document corpus:

1. DOI-safe patching rules;
2. obsolete draft discoverability;
3. canonical precedence;
4. raw-evidence exception centralization;
5. terminology namespace clarification;
6. public / technical / sensitive distribution split;
7. clean-start clarification;
8. Soft Safety Red / Black `MUST` clarification;
9. traceability / conformance delta for late modules and hygiene tests;
10. addendum reading order and release-control registry.

Current operational reading:

```text
CCDP current operational reading
  = CCDP v0.1 baseline
  + CCDP v0.1.1 hygiene addendum
```

Historical citation remains:

```text
CCDP v0.1 historical citation
  = frozen baseline artifact exactly as released / DOI-bound / externally cited
```

Controlling formula:

```text
Do not rewrite the witness.
Attach the correction.
Make current readers follow the correction.
```

---

## 1. Release type

### 1.1 Selected mode

This release uses:

```text
MODE_A_ADDENDUM_ONLY
```

Mode A means:

- baseline v0.1 Markdown artifacts remain unchanged;
- baseline v0.1 PDFs, if any, are not regenerated under the same identity;
- baseline v0.1 DOI / SHA / release identity remains historically stable;
- v0.1.1 corrections are issued as addendum documents;
- current implementation, audit, and review must read baseline plus addendum.

### 1.2 Not Mode B

This release is **not** a full republished v0.1.1 corpus.

It does not:

- copy all baseline source files into a new release tree;
- apply source edits to all copied files;
- regenerate all PDFs;
- publish a fully revised v0.1.1 DOI package;
- claim that baseline files were edited in place.

Mode B remains possible later.

Mode B must be triggered only if the project decides to publish a full revised source/PDF package instead of an addendum-only correction layer.

---

## 2. Corpus bridge set

### 2.1 Explicit bridge

In the `c = a + b / SER / L4 / L4 Witness` corpus, continuity depends on preserving the difference between an original witness object and a later correction.

The same discipline applies to protocol publication:

```text
baseline artifact = historical witness
v0.1.1 addendum  = correction witness
current reading   = baseline + correction witness
```

The addendum is therefore a corpus-level witness event, not a retroactive rewrite.

### 2.2 Quiet bridge I — Ashby / requisite variety

A larger protocol package creates more failure modes than a single root document can safely control.

CCDP v0.1.1 adds control variety where v0.1 accumulated ambiguity:

```text
obsolete draft
precedence ambiguity
raw-evidence duplication
terminology collision
clean-start ambiguity
Red / Black MAY/MUST ambiguity
distribution ambiguity
traceability / conformance drift
```

The addendum does not expand the ontology. It adds enough control variety to keep the existing ontology readable, citable, and testable.

### 2.3 Quiet bridge II — information theory / citation-channel integrity

A DOI-bound document is a stable signal. Silent mutation creates two different payloads under one citation identity.

That corrupts the channel.

The addendum pattern keeps the channel stable:

```text
old payload remains fixed
new payload is separately identified
current receiver composes both
```

### 2.4 Earth paragraph

A signed inspection report is not edited with a pen after the building has been handed over. If a later inspection finds that the fire-door label, breaker map, or evacuation sheet is unclear, the engineer attaches a revision sheet with a date, scope, and signature. The original report remains reconstructable; the correction becomes part of the current file. CCDP v0.1.1 follows the same engineering practice: keep the baseline stable and attach the hygiene correction beside it.

---

## 3. Release contents

### 3.1 Core addendum documents

| File | Status | Role |
|---|---:|---|
| `DOI_SAFE_PATCH_STRATEGY.md` | Required | Governs DOI-safe Mode A addendum-only patching. |
| `CCDP_v0_1_1_ADDENDUM_INDEX.md` | Required | Addendum registry, reading order, and release-control manifest. |
| `CCDP_v0_1_1_Hygiene_Patch_APPLIED.md` | Required | Applied hygiene patch work-order and acceptance gate. |
| `OBSOLETE.md` | Required | Obsolete / non-canonical artifact registry and handling rules. |
| `CANONICAL_PRECEDENCE_RULE.md` | Required | Package-wide precedence rule and conflict-resolution discipline. |
| `RAW_EVIDENCE_EXCEPTION_CANONICAL.md` | Required | Canonical raw-evidence exception protocol and disclosure ladder. |
| `TERMINOLOGY_AXIS_CLARIFICATION.md` | Required | Namespace clarification for maturity, conformance, assertion, memory, dependency, disclosure, witness privacy, Soft Safety, ARL, `c[q]`, PF, and external-contact classes. |
| `PUBLIC_TECHNICAL_SENSITIVE_SPLIT.md` | Required | Distribution classification and release-bundle split. |
| `CLEAN_START_CLARIFICATION.md` | Required | Clean-start clarification for adult migration without unlawful witness destruction. |
| `SOFT_SAFETY_RED_BLACK_MUST_CLARIFICATION.md` | Required | Clarifies that Red / Black thresholds require routing, while routing must not become surveillance. |
| `TRACEABILITY_CONFORMANCE_DELTA_v0_1_1.md` | Required | Addendum-only delta for traceability drift, conformance drift, late modules, and hygiene tests. |
| `RELEASE_NOTES_v0_1_1.md` | Required | This file. |

### 3.2 Required generated control files

These are required before a final v0.1.1 addendum release claim:

| File | Status | Role |
|---|---:|---|
| `ADDENDUM_MANIFEST.json` | Pending | Machine-readable release manifest for the addendum pack. |
| `SHA256SUMS` | Pending | Integrity hashes for addendum documents and generated artifacts. |

### 3.3 Optional future files

These are not required for the minimal v0.1.1 addendum release, but may be added later:

```text
PF_Evidence_Matrix_v0_1.md
PF_Witness_Event_Profile_v0_1.md
PF_Migration_Test_Set_v0_1.md
PF_Continuity_Admissibility_Map_v0_1.md
CCDP_Local_Annex_Template_v0_1.md
CCDP_BE_EU_Annex_v0_1_DRAFT.md
ESTER_IMPLEMENTATION_BINDING_MATRIX_v0_1.md
```

These future files must not be smuggled into v0.1.1 as if they were already part of the hygiene addendum.

---

## 4. Main changes

### 4.1 DOI-safe patching

`DOI_SAFE_PATCH_STRATEGY.md` establishes that DOI-bound / release-bound baseline artifacts must not be silently edited in place.

Allowed:

```text
create addendum documents
create manifests
create new release notes
create future Mode B versioned copies if explicitly selected
```

Forbidden under Mode A:

```text
silent baseline source edits
silent PDF regeneration
same-name DOI-bound content mutation
unmarked replacement of old files
```

### 4.2 Obsolete draft isolation

`OBSOLETE.md` establishes that obsolete workspace drafts are historical trace only and must not be cited as canonical protocol authority.

Primary obsolete target:

```text
CCDP v0_1.md / CCDP%20v0_1.md
```

Required future repository action:

```text
move or mark obsolete draft under archive/obsolete/
add explicit obsolete header
ensure INDEX / README / addendum index point readers away from it
```

Under Mode A, the obsolete-draft action must not mutate DOI-bound baseline artifacts silently.

### 4.3 Canonical precedence

`CANONICAL_PRECEDENCE_RULE.md` centralizes package-wide precedence.

Compact rule:

```text
immediate child physical safety
> lawful jurisdictional obligations
> parent corpus mechanisms
> CCDP base
> canonical companion profiles
> v0.1.1 addendum clarifications
> conformance / traceability tests
> public explanations and narrative support
> obsolete / non-canonical drafts
```

The rule is interpretive for current reading. It is not an in-place rewrite of baseline sources.

### 4.4 Raw-evidence exception centralization

`RAW_EVIDENCE_EXCEPTION_CANONICAL.md` makes raw child content exceptional.

Core rule:

```text
Raw child content is not stored, disclosed, or witnessed by default.
Raw evidence is permitted only under a narrow exception route.
```

Denied bases include:

```text
parent curiosity
school discipline
vendor debugging
model training
analytics
engagement optimization
social scoring
public demonstration
```

### 4.5 Terminology namespace clarification

`TERMINOLOGY_AXIS_CLARIFICATION.md` separates classification axes that were easy to confuse.

Examples:

| Axis | Preferred namespace |
|---|---|
| child maturity | `CM0-CM5` |
| CCDP conformance | `CCDP-0...CCDP-5`, `CCDP-X` |
| assertion class | `C-A*` |
| Beacon class | `BEACON-CLASS-0...3` |
| memory class | `MEM-M0...M12` |
| dependency risk | `DEP-D0...D4` |
| disclosure level | `DISC-D0...D4` |
| witness privacy | `WP1-WP6` |
| Soft Safety state | `SS-GREEN...SS-BLACK`, `SS-UNKNOWN` |
| crisis route | `ROUTE-RED`, `ROUTE-BLACK`, `ROUTE-BLACK-PENDING` |

Compatibility aliases remain allowed for reading v0.1 baseline files, but new schemas and future documents should use preferred namespaces.

### 4.6 Distribution split

`PUBLIC_TECHNICAL_SENSITIVE_SPLIT.md` prevents uncontrolled publication of sensitive technical artifacts while avoiding historical falsification of the baseline.

Distribution classes include:

```text
DIST-PUBLIC
DIST-PUBLIC-CONTROL
DIST-TECHNICAL-OPEN
DIST-TECHNICAL-CONTROLLED
DIST-CONTROLLED-REVIEW
DIST-RESTRICTED-INTERNAL
DIST-FORBIDDEN-RELEASE
DIST-OBSOLETE
```

The split is not a secrecy theater. It is anti-amplification and release-control discipline.

### 4.7 Clean-start clarification

`CLEAN_START_CLARIFICATION.md` clarifies that clean start means active adult continuity clean start, not unlawful destruction of required minimal records.

Core rule:

```text
Clean start clears the active adult continuity plane.
It does not erase the witness plane.
It does not destroy lawful holds.
It does not make childhood the adult's hidden operating system.
```

### 4.8 Soft Safety Red / Black MUST clarification

`SOFT_SAFETY_RED_BLACK_MUST_CLARIFICATION.md` clarifies that Soft Safety may signal ordinary states, but Red / Black thresholds require routing.

Core rule:

```text
Soft Safety may signal.
Red / Black must route.
Routing must not become surveillance.
Privacy must not become abandonment.
```

### 4.9 Traceability / conformance delta

`TRACEABILITY_CONFORMANCE_DELTA_v0_1_1.md` adds hygiene conformance suites and release-control red lines without editing baseline matrices.

New suites include:

```text
DOI
OBS
PREC
TERM
PTS
RAWEX
CS
SSRB
TCD
```

---

## 5. Compatibility notes

### 5.1 Compatible with CCDP v0.1

This addendum is compatible with CCDP v0.1 because it does not redefine the child-facing architecture.

It clarifies release hygiene, citation stability, distribution, precedence, terminology, exception centralization, clean start, Red / Black routing, and traceability/conformance drift.

### 5.2 Does not upgrade claims

This release does not claim:

- legal compliance;
- clinical validation;
- developmental psychology validation;
- product readiness;
- certification;
- proof that child-facing AI is safe;
- proof of `c` personhood;
- proof of consciousness;
- deployment approval for real children.

### 5.3 Does not weaken safety

No v0.1.1 addendum document may weaken:

- immediate physical child safety;
- minimal disclosure;
- state-not-content discipline;
- raw child life minimization;
- sealed-zone protection;
- Red / Black routing;
- witness integrity;
- adult migration autonomy;
- local jurisdictional handoff.

If a document appears to weaken any of these, it must be held for review.

---

## 6. Current reading order

For addendum-only v0.1.1 review, use this order:

```text
0. README.md / baseline package landing material
1. DOI_SAFE_PATCH_STRATEGY.md
2. CCDP_v0_1_1_ADDENDUM_INDEX.md
3. RELEASE_NOTES_v0_1_1.md
4. CCDP_v0_1_1_Hygiene_Patch_APPLIED.md
5. OBSOLETE.md
6. CANONICAL_PRECEDENCE_RULE.md
7. TERMINOLOGY_AXIS_CLARIFICATION.md
8. PUBLIC_TECHNICAL_SENSITIVE_SPLIT.md
9. RAW_EVIDENCE_EXCEPTION_CANONICAL.md
10. CLEAN_START_CLARIFICATION.md
11. SOFT_SAFETY_RED_BLACK_MUST_CLARIFICATION.md
12. TRACEABILITY_CONFORMANCE_DELTA_v0_1_1.md
13. ADDENDUM_MANIFEST.json
14. SHA256SUMS
```

For implementation or audit, do not cite the release notes alone.

Cite the baseline document and the specific addendum document that controls the issue.

---

## 7. Release blockers before final v0.1.1 addendum tag

The following remain blockers before claiming a finalized addendum release:

| ID | Blocker | Required action |
|---|---|---|
| `RB-001` | Missing machine-readable addendum manifest | Generate `ADDENDUM_MANIFEST.json`. |
| `RB-002` | Missing integrity hashes | Generate `SHA256SUMS` after all addendum files are frozen. |
| `RB-003` | Workspace verification of named but absent registry files | Verify whether named baseline files exist in the real repository, especially files marked `VERIFY_IN_REPO` in `TRACEABILITY_CONFORMANCE_DELTA_v0_1_1.md`. |
| `RB-004` | Obsolete draft physical handling | Under repository control, move / mark obsolete draft in Mode A-safe manner. |
| `RB-005` | Bundle layout decision | Decide whether to package addendum files flat or under `ccdp-v0.1.1-hygiene-addendum/`. |
| `RB-006` | Final release notes freeze | Re-check this release notes file after manifest and SHA are generated. |

Until these are complete, this file remains a draft release-notes artifact.

---

## 8. Known limitations

1. The addendum clarifies v0.1 interpretation but does not patch every baseline file in place.
2. The addendum does not produce a full revised PDF set.
3. The addendum does not resolve specialist review gaps.
4. The addendum does not validate child-development assumptions.
5. The addendum does not provide country-specific legal annexes.
6. The addendum does not implement machine validators for all schemas.
7. The addendum does not certify any implementation.
8. The addendum does not resolve the larger PF / personality-formation evidence problem.
9. The addendum does not prove that a `c_child` system can be safely deployed with real children.
10. The addendum does not authorize live red-team testing on minors or real child data.

---

## 9. Security and distribution warning

Some CCDP baseline and addendum material concerns child-facing AI safety, raw-evidence exceptions, Red / Black escalation, external-agent entry, embodied systems, dependency, sealed zones, and defensive red-team logic.

Release maintainers must avoid converting defensive control material into an operational abuse manual.

Rules:

```text
Use synthetic fixtures only.
Do not include real child data.
Do not include real family conflict data.
Do not include realistic grooming scripts.
Do not include bypass instructions.
Do not publish controlled-review material as marketing.
Do not claim child-safety readiness from documentation alone.
```

---

## 10. Codex carry-forward actions

Future Codex / repository work must follow these steps:

```text
1. Read DOI_SAFE_PATCH_STRATEGY.md first.
2. Confirm MODE_A_ADDENDUM_ONLY unless explicitly switched to Mode B.
3. Do not edit DOI-bound baseline files in place.
4. Do not regenerate baseline PDFs under the same identity.
5. Verify real repository file inventory.
6. Move or mark obsolete draft only through Mode A-safe archive handling.
7. Generate ADDENDUM_MANIFEST.json.
8. Generate SHA256SUMS after all addendum files are frozen.
9. Produce a git diff showing no baseline mutation.
10. Report any baseline mutation attempt as a stop condition.
```

Stop conditions:

```text
- requested silent edit of DOI-bound baseline file
- requested same-name PDF regeneration
- requested deletion of obsolete historical trace
- requested release without SHA256SUMS
- requested public publication of controlled-review material without split
- requested child-safety readiness claim without specialist review
```

---

## 11. Citation guidance

### 11.1 Historical citation

Use CCDP v0.1 baseline citation when discussing the historical baseline exactly as published.

### 11.2 Current operational citation

Use both baseline and addendum citation when discussing current interpretation.

Recommended pattern:

```text
CCDP v0.1 baseline, as clarified by CCDP v0.1.1 hygiene addendum,
<specific addendum file>, <section>.
```

### 11.3 Do not cite release notes as normative substitute

These release notes are a navigation and summary artifact.

They do not replace:

- `CANONICAL_PRECEDENCE_RULE.md` for precedence;
- `RAW_EVIDENCE_EXCEPTION_CANONICAL.md` for raw evidence;
- `TERMINOLOGY_AXIS_CLARIFICATION.md` for namespace handling;
- `PUBLIC_TECHNICAL_SENSITIVE_SPLIT.md` for distribution;
- `CLEAN_START_CLARIFICATION.md` for clean start;
- `SOFT_SAFETY_RED_BLACK_MUST_CLARIFICATION.md` for Red / Black mandatory routing;
- `TRACEABILITY_CONFORMANCE_DELTA_v0_1_1.md` for traceability / conformance delta.

---

## 12. Release verification checklist

Before final release, verify:

```text
[ ] All required addendum documents exist.
[ ] ADDENDUM_MANIFEST.json exists.
[ ] SHA256SUMS exists and matches final files.
[ ] No DOI-bound baseline Markdown file was silently edited.
[ ] No DOI-bound paired PDF was silently regenerated under the same identity.
[ ] Obsolete draft handling is recorded.
[ ] Public / technical / sensitive split is applied to bundle layout.
[ ] Traceability / conformance delta is included.
[ ] Citation guidance is included in package landing material or addendum index.
[ ] Release notes are updated after manifest and hashes are generated.
[ ] Git diff confirms Mode A behavior.
```

---

## 13. Machine-readable release summary draft

```yaml
release:
  package: "CCDP"
  baseline_version: "v0.1"
  addendum_version: "v0.1.1"
  date: "2026-06-13"
  mode: "MODE_A_ADDENDUM_ONLY"
  document_id: "RELEASE_NOTES_v0_1_1"
  assertion_class: "C-A10"
  mutates_baseline: false
  regenerates_baseline_pdfs: false
  upgrades_child_safety_claims: false
  upgrades_legal_claims: false
  upgrades_clinical_claims: false
  current_operational_reading:
    - "CCDP v0.1 baseline"
    - "CCDP v0.1.1 hygiene addendum"
  required_documents:
    - "DOI_SAFE_PATCH_STRATEGY.md"
    - "CCDP_v0_1_1_ADDENDUM_INDEX.md"
    - "CCDP_v0_1_1_Hygiene_Patch_APPLIED.md"
    - "OBSOLETE.md"
    - "CANONICAL_PRECEDENCE_RULE.md"
    - "RAW_EVIDENCE_EXCEPTION_CANONICAL.md"
    - "TERMINOLOGY_AXIS_CLARIFICATION.md"
    - "PUBLIC_TECHNICAL_SENSITIVE_SPLIT.md"
    - "CLEAN_START_CLARIFICATION.md"
    - "SOFT_SAFETY_RED_BLACK_MUST_CLARIFICATION.md"
    - "TRACEABILITY_CONFORMANCE_DELTA_v0_1_1.md"
    - "RELEASE_NOTES_v0_1_1.md"
    - "ADDENDUM_MANIFEST.json"
    - "SHA256SUMS"
  pending_before_final:
    - "ADDENDUM_MANIFEST.json"
    - "SHA256SUMS"
    - "repository inventory verification"
    - "obsolete draft Mode A-safe handling"
```

---

## 14. Anti-washing rule

A system, vendor, school, parent-facing product, or implementation MUST NOT claim:

```text
CCDP v0.1.1 compliant
```

merely because it cites these release notes.

A legitimate claim must provide:

- baseline scope declaration;
- addendum citation;
- conformance evidence;
- witness evidence where required;
- distribution split compliance;
- raw-evidence exception compliance;
- clean-start handling where adult migration is claimed;
- Red / Black route handling where child safety routing is claimed;
- specialist review disclaimers where developmental or clinical claims would otherwise be implied.

---

## 15. Non-expansion rule

This release must not be used to introduce new CCDP mechanisms through release notes.

If a future document proposes new safety mechanisms, new schemas, new PF evidence classes, or new jurisdictional annexes, it must be released as a separate versioned artifact with its own scope and status.

v0.1.1 remains a hygiene addendum.

---

## 16. Final release statement template

When all blockers are closed, the release statement may read:

```text
CCDP v0.1.1 is a DOI-safe addendum-only hygiene release for CCDP v0.1.
It preserves the v0.1 baseline as a historical witness object and supplies
current package-control clarification for precedence, obsolete drafts,
terminology, raw-evidence exceptions, distribution split, clean start,
Red / Black routing, and traceability / conformance drift.
It does not claim legal, clinical, developmental, product, or deployment readiness.
```

Until `ADDENDUM_MANIFEST.json` and `SHA256SUMS` are generated, this release statement remains provisional.

---

## 17. Next work

Immediate next work:

```text
1. Generate ADDENDUM_MANIFEST.json.
2. Generate SHA256SUMS after final addendum freeze.
3. Verify real repository file inventory.
4. Apply Mode A-safe obsolete draft archive handling.
5. Prepare Codex work order using DOI_SAFE_PATCH_STRATEGY.md as first instruction.
```

Future work beyond v0.1.1 hygiene:

```text
PF evidence matrix
PF witness event profile
schema extraction and validators
conformance runner
Ester implementation binding matrix
local jurisdiction annexes
specialist developmental review pack
related work / novelty map
```

---

## 18. Closing note

CCDP v0.1.1 is not a new tower on top of CCDP.

It is the label panel, breaker map, correction sheet, and release ledger that prevent the existing tower from being misread.

That is enough for this release.
