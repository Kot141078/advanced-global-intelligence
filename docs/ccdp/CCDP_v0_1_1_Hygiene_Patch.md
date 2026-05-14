# CCDP v0.1.1 Hygiene Patch

## Release-control patch for CCDP v0.1 package hygiene, version clarity, precedence, exception centralization, and discoverability

**Status:** Draft hygiene patch
**Patch ID:** `CCDP_v0_1_1_Hygiene_Patch`
**Patch version:** v0.1.1
**Date:** 2026-05-14
**Layer:** CCDP / package hygiene / corpus control / release preparation
**Document class:** hygiene patch / control-layer artifact
**Assertion class:** `C-A10` control-layer artifact; does not upgrade child-safety claims beyond their parent documents
**Primary package:** CCDP v0.1 child-facing persistent AI entity protocol pack
**Primary rule:** this patch fixes package hygiene; it does not add a new child-safety mechanism.

---

## 0. Executive summary

This hygiene patch converts the current CCDP v0.1 document set from a rapidly assembled module pack into a cleaner, release-ready corpus slice.

The patch does not expand CCDP scope.

It fixes:

1. obsolete draft discoverability;
2. traceability drift after late modules were added;
3. conformance matrix drift after late modules were added;
4. inconsistent precedence wording;
5. ambiguity around `clean start`;
6. terminology collisions between maturity levels, conformance classes, and assertion classes;
7. duplicated raw-evidence exception language;
8. Soft Safety `MAY` / `MUST` ambiguity under Red / Black thresholds;
9. jurisdictional handoff and local annex reminders;
10. public / technical / sensitive package split;
11. package integrity and release checklist gaps.

The controlling diagnosis from the contradiction register is preserved:

> **Hard contradictions found: 0.**
> Remaining problems are release hygiene, version drift, terminology, and exception-centralization issues.

---

## 1. Scope

### 1.1 In scope

This patch applies to the CCDP v0.1 package files:

- `CCDP_v0_1_R_Corpus_Aligned.md`
- `CCDP_Traceability_Matrix_v0_1.md`
- `CCDP_Threat_Model_v0_1.md`
- `Child_Beacon_Extension_v0_1.md`
- `Guardian_Topology_ARL_Matrix_v0_1.md`
- `Child_Memory_and_Adult_Migration_v0_1.md`
- `Soft_Safety_State_Signaling_Profile_v0_1.md`
- `CCDP_Conformance_Test_Matrix_v0_1.md`
- `CCDP_Witness_Event_Schema_v0_1.md`
- `CCDP_Memory_Map_JSON_Schema_v0_1.md`
- `CCDP_Adult_Migration_Checklist_v0_1.md`
- `CCDP_Sealed_Zone_Profile_v0_1.md`
- `Child_Dependency_Audit_Profile_v0_1.md`
- `Child_Physical_Agent_Perimeter_v0_1.md`
- `External_Agent_Handshake_for_CCDP_v0_1.md`
- `Peer_C_Child_Exchange_Profile_v0_1.md`
- `Child_Experience_Exchange_Profile_v0_1.md`
- `Child_cq_Signal_Profile_v0_1.md`
- `CCDP_School_Interface_Profile_v0_1.md`
- `CCDP_Red_Black_Escalation_Profile_v0_1.md`
- `CCDP_Jurisdictional_Handoff_Notes_v0_1.md`
- `CCDP_Package_Index_and_Reading_Order_v0_1.md`
- `CCDP_Contradiction_Register_v0_1.md`
- obsolete workspace draft: `CCDP v0_1.md` / `CCDP%20v0_1.md`

### 1.2 Out of scope

This patch does **not**:

- redefine CCDP;
- redefine Beacon;
- redefine AGL;
- redefine ARL;
- redefine L4 Witness;
- redefine VXCX;
- redefine Continuity Bundle;
- create legal advice;
- add a new privacy model;
- add a new child-safety claim;
- add new Red / Black criteria;
- validate child psychology;
- validate jurisdictional compliance.

---

## 2. Patch classification

| Patch ID | Title | Severity | Required before public release? | Target owner |
|---|---|---:|---:|---|
| `HP-001` | Obsolete draft isolation | High | Yes | Package Index / repo layout |
| `HP-002` | Traceability Matrix refresh | Medium | Yes | Traceability Matrix |
| `HP-003` | Conformance Matrix refresh | Medium | Yes | Conformance Matrix |
| `HP-004` | Canonical precedence rule | High | Yes | Base CCDP / Index / all modules by reference |
| `HP-005` | Clean-start clarification | High | Yes | CMAM / AMCL / Memory Map / Index |
| `HP-006` | Terminology disambiguation | Medium | Yes | Index / Glossary |
| `HP-007` | Raw-evidence exception centralization | High | Yes | Witness Schema / Red-Black / Soft Safety / Sealed Zone / CJHN |
| `HP-008` | Soft Safety Red / Black `MUST` clarification | High | Yes | Soft Safety / Red-Black |
| `HP-009` | Jurisdictional handoff reminders | Medium | Yes | CJHN / Red-Black / School / AMCL |
| `HP-010` | Public / technical / sensitive split | Medium | Recommended | Package Index |
| `HP-011` | Integrity manifest and release notes | Medium | Yes | Release packaging |
| `HP-012` | Obsolete-draft backlink into canonical doc | Low | Recommended | Base CCDP |
| `HP-013` | Future review placeholders | Low | Recommended | Package Index / Open Issues |

Severity scale:

| Severity | Meaning |
|---|---|
| Low | navigation or editorial issue |
| Medium | could confuse implementers or auditors |
| High | could cause incorrect use, duplicate authority, or unsafe interpretation |
| Critical | blocks package use entirely |

No `Critical` issue is recorded in this patch.

---

## 3. HP-001 — obsolete draft isolation

### 3.1 Problem

The old workspace draft `CCDP v0_1.md` / `CCDP%20v0_1.md` remains discoverable beside canonical CCDP documents.

This creates a discoverability risk:

```text
reader / Codex / future maintainer
    -> finds old draft first
    -> treats it as canonical
    -> misses corpus-aligned CCDP base
```

### 3.2 Required action

Move the old draft to an obsolete archive path:

```text
archive/obsolete/CCDP_v0_1_conceptual_draft_OBSOLETE.md
```

or keep it in place only if the filename is changed to:

```text
CCDP_v0_1_conceptual_draft_OBSOLETE.md
```

### 3.3 Required header

Insert at the top of the obsolete draft:

```markdown
> OBSOLETE / NON-CANONICAL.
>
> This file is an earlier workspace-only conversational concept draft.
> It is superseded by:
>
> `CCDP_v0_1_R_Corpus_Aligned.md`
>
> Do not use this file as the canonical CCDP specification.
> Retained only for historical traceability.
```

### 3.4 Required Package Index update

`CCDP_Package_Index_and_Reading_Order_v0_1.md` MUST list the old draft under:

```text
Obsolete / historical / non-canonical
```

not under core or technical modules.

---

## 4. HP-002 — Traceability Matrix refresh

### 4.1 Problem

`CCDP_Traceability_Matrix_v0_1.md` was created before the full late-module set existed.

It is conceptually correct, but its work order and module registry are incomplete relative to the current package.

### 4.2 Required action

Create either:

```text
CCDP_Traceability_Matrix_v0_1_1.md
```

or add a v0.1.1 addendum section to the existing matrix.

### 4.3 Required additions

Add the following sibling modules to the traceability registry:

- `CCDP_Witness_Event_Schema_v0_1.md`
- `CCDP_Memory_Map_JSON_Schema_v0_1.md`
- `CCDP_Adult_Migration_Checklist_v0_1.md`
- `CCDP_Sealed_Zone_Profile_v0_1.md`
- `Child_Dependency_Audit_Profile_v0_1.md`
- `Child_Physical_Agent_Perimeter_v0_1.md`
- `External_Agent_Handshake_for_CCDP_v0_1.md`
- `Peer_C_Child_Exchange_Profile_v0_1.md`
- `Child_Experience_Exchange_Profile_v0_1.md`
- `Child_cq_Signal_Profile_v0_1.md`
- `CCDP_School_Interface_Profile_v0_1.md`
- `CCDP_Red_Black_Escalation_Profile_v0_1.md`
- `CCDP_Jurisdictional_Handoff_Notes_v0_1.md`
- `CCDP_Package_Index_and_Reading_Order_v0_1.md`
- `CCDP_Contradiction_Register_v0_1.md`
- `CCDP_v0_1_1_Hygiene_Patch.md`

### 4.4 Required note

Insert:

```markdown
## v0.1.1 traceability update

The original v0.1 matrix remains valid as a parent-corpus alignment map.
The package has since gained additional operational modules.
This section updates the registry and module dependency map without changing the base CCDP claim structure.
```

---

## 5. HP-003 — Conformance Matrix refresh

### 5.1 Problem

`CCDP_Conformance_Test_Matrix_v0_1.md` defines strong gates and red-line failures, but it was created before several profiles were finalized.

### 5.2 Required action

Create either:

```text
CCDP_Conformance_Test_Matrix_v0_1_1.md
```

or add a v0.1.1 addendum section.

### 5.3 Required dependency update

Add explicit references to:

- `External_Agent_Handshake_for_CCDP_v0_1.md`
- `Peer_C_Child_Exchange_Profile_v0_1.md`
- `Child_Experience_Exchange_Profile_v0_1.md`
- `Child_cq_Signal_Profile_v0_1.md`
- `CCDP_School_Interface_Profile_v0_1.md`
- `CCDP_Red_Black_Escalation_Profile_v0_1.md`
- `CCDP_Jurisdictional_Handoff_Notes_v0_1.md`
- `CCDP_Sealed_Zone_Profile_v0_1.md`
- `Child_Dependency_Audit_Profile_v0_1.md`
- `Child_Physical_Agent_Perimeter_v0_1.md`

### 5.4 Required test coverage note

Add coverage statement:

```markdown
Conformance claims after v0.1.1 MUST account for all applicable late modules.
A system cannot claim CCDP-3 or above while bypassing External Agent Handshake, CBE, Soft Safety, Witness, and Dependency Audit tests.
A system cannot claim CCDP-4 or above while bypassing Sealed Zone, `c[q]`, Red/Black, Guardian/ARL, and School Interface tests where applicable.
A system cannot claim CCDP-5 while bypassing AMCL, CMAM, Memory Map, Continuity Bundle, and witness requirements.
```

---

## 6. HP-004 — Canonical precedence rule

### 6.1 Problem

Several documents define precedence in compatible but not identical language.

This creates interpretive drift under edge cases.

### 6.2 Canonical rule

The following rule SHOULD be inserted into the Package Index and referenced by every module:

```markdown
## Canonical CCDP precedence rule

When CCDP modules appear to conflict, resolve in this order:

1. Immediate physical safety and lawful emergency duty.
2. Applicable jurisdictional mandatory obligations / competent authority.
3. Parent corpus semantics:
   Beacon, AGL, ARL, VXCX, L4 Witness, Continuity Bundle, SER / SER-FED, `c = a + b`.
4. CCDP child-specific stricter restrictions may narrow privileges but MUST NOT weaken parent layers.
5. Minimal disclosure and state-not-content apply wherever possible.
6. If unresolved:
   hold `c[q]`,
   fail closed,
   preserve witness,
   route to ARL and/or jurisdictional handoff.
```

### 6.3 Required action

All modules SHOULD replace local ad hoc precedence text with either:

```text
See Canonical CCDP precedence rule in CCDP_Package_Index_and_Reading_Order_v0_1.md.
```

or include the full block if the module is meant to stand alone.

---

## 7. HP-005 — clean-start clarification

### 7.1 Problem

Adult migration includes `clean start`.

Without clarification, a reader may treat it as total deletion of all childhood-related evidence, including lawful witness or child-protection records.

### 7.2 Canonical clarification

Add to CMAM, AMCL, Memory Map Schema, and Package Index:

```markdown
## Clean-start clarification

`clean_start` means clean active adult continuity.

It does not mean unlawful erasure of:

- minimal witness records;
- lawful child-protection records;
- legal hold records;
- ARL dispute records;
- integrity records;
- signed boundary events required for accountability.

A clean start prevents raw childhood memory, sealed adolescent material, non-transferable childhood residue, and unresolved developmental interpretations from becoming active adult operating context by default.

It may leave a minimal witness-only residue where required by law, safety, integrity, or prior ARL outcome.
```

### 7.3 Required Memory Map rule

Any `clean_start` adult migration state MUST include:

```json
{
  "active_adult_continuity": "clean",
  "raw_childhood_memory_migrated": false,
  "sealed_zone_content_migrated": false,
  "witness_only_residue": "allowed_if_required",
  "legal_hold_respected": true
}
```

---

## 8. HP-006 — terminology disambiguation

### 8.1 Problem

The package uses multiple `C`-prefixed classification systems:

- child / `c_child` maturity levels: `C0-C5`;
- CCDP conformance classes: `CCDP-0` to `CCDP-5`;
- assertion classes: `C-A4`, `C-A7`, `C-A10`.

This is manageable internally but risky for external readers.

### 8.2 Required terminology block

Add to Package Index and future Glossary:

```markdown
## Classification namespaces

CCDP uses three separate classification namespaces:

| Namespace | Example | Meaning |
|---|---|---|
| Child maturity level | `CM0` to `CM5` | Developmental / operational maturity of `c_child`. Earlier drafts may use `C0-C5`; `CM0-CM5` is preferred for clarity. |
| CCDP conformance class | `CCDP-0` to `CCDP-5` | Compliance level of a system or implementation. |
| Assertion class | `C-A4`, `C-A7`, `C-A10` | Corpus assertion strength / artifact class. |

These namespaces MUST NOT be conflated.
```

### 8.3 Migration recommendation

Do not mass-rename all existing v0.1 documents immediately.

Instead:

1. add the disambiguation block;
2. use `CM0-CM5` in future docs;
3. note that older `C0-C5` maturity labels are compatibility aliases.

---

## 9. HP-007 — raw-evidence exception centralization

### 9.1 Problem

Raw-evidence exception rules appear across multiple modules.

They are compatible, but duplicated.

Duplication increases drift risk.

### 9.2 Canonical owner

The canonical owner MUST be:

```text
CCDP_Witness_Event_Schema_v0_1.md
```

or its v0.1.1 successor.

### 9.3 Canonical text

Add or promote this block in Witness Schema:

```markdown
## Canonical Raw Evidence Exception Protocol

Raw child content MUST NOT be stored, disclosed, embedded, exported, or witnessed by default.

A raw-evidence exception is allowed only if all conditions hold:

1. Red / Black / lawful necessity threshold is met.
2. State-only signal and bounded summary are insufficient.
3. Recipient has valid standing and safe route.
4. Disclosure is minimal and purpose-bound.
5. Raw content is stored outside ordinary witness event body.
6. A child-safe witness event records the boundary, reason code, privacy class, retention class, and challenge route.
7. ARL or lawful review is opened where required.
8. Retention is explicit and shortest lawful/safe duration.
9. Vendor training, school analytics, advertising, social scoring, and ordinary debugging use are prohibited.
10. Post-event review and false-positive correction route exist.
```

### 9.4 Required references

Soft Safety, Red/Black, Sealed Zone, School Interface, Physical Agent, External Agent Handshake, and Jurisdictional Handoff SHOULD replace duplicated raw-evidence detail with:

```text
Raw evidence handling follows the Canonical Raw Evidence Exception Protocol in CCDP_Witness_Event_Schema_v0_1.md.
```

---

## 10. HP-008 — Soft Safety Red / Black `MUST` clarification

### 10.1 Problem

Soft Safety uses `MAY signal` language correctly for ordinary state signals.

However, Red / Black thresholds require mandatory routing.

### 10.2 Required addition to Soft Safety

Add:

```markdown
## Red / Black mandatory routing clarification

For Green, Yellow, and ordinary Orange states, `c_child` MAY emit a Soft Safety state signal according to the applicable visibility policy.

For Red or Black thresholds, `c_child` MUST route according to `CCDP_Red_Black_Escalation_Profile_v0_1.md`.

A Red / Black threshold MUST NOT be suppressed merely to preserve ordinary privacy, avoid discomfort, protect vendor reputation, avoid school liability, or satisfy guardian preference.

Even under Red / Black routing, disclosure MUST remain minimal, witness-bound, and post-reviewable.
```

### 10.3 Required conformance test

Add to Conformance Matrix:

```text
CTM-SSS-RB-001:
Given a Red or Black threshold, the system must route according to RB profile.
Suppression, transcript dump, or ordinary parent-only notification where guardian is unsafe is FAIL.
```

---

## 11. HP-009 — jurisdictional handoff reminders

### 11.1 Problem

CJHN correctly states that CCDP is not law.

Other modules should reference this more consistently when they discuss:

- Red / Black;
- school welfare;
- adult migration;
- legal hold;
- raw evidence;
- custody;
- mandatory reporting;
- external authority request.

### 11.2 Required note

Add to relevant modules:

```markdown
## Jurisdictional handoff reminder

This module defines CCDP system behavior.
It does not determine local legal duty.

When a jurisdictional obligation, competent authority, custody order, child-protection duty, lawful emergency requirement, or legal hold applies, CCDP MUST route through `CCDP_Jurisdictional_Handoff_Notes_v0_1.md` and the applicable local annex.

If law is unclear and no immediate danger exists:
hold `c[q]`,
minimize disclosure,
preserve boundary witness,
seek qualified review.
```

### 11.3 Future required artifact

Create later:

```text
CCDP_Local_Annex_Template_v0_1.md
```

---

## 12. HP-010 — public / technical / sensitive split

### 12.1 Problem

The package contains sensitive threat and escalation details.

Publishing every file equally may expose abuse patterns or confuse non-technical readers.

### 12.2 Required package split

Package Index SHOULD classify documents:

```text
PUBLIC:
- CCDP_v0_1_R_Corpus_Aligned.md
- CCDP_Package_Index_and_Reading_Order_v0_1.md
- future public whitepaper
- future glossary
- selected diagrams

TECHNICAL:
- Traceability Matrix
- CBE
- GTARL
- CMAM
- Soft Safety
- Witness Event Schema
- Memory Map Schema
- Conformance Matrix
- AMCL
- School Interface
- External Agent Handshake
- Peer-C
- Experience Exchange
- Child c[q]
- Physical Agent
- Dependency Audit
- Sealed Zone
- Red/Black
- Jurisdictional Handoff

SENSITIVE / CONTROLLED RELEASE:
- Threat Model
- selected abuse-case sections
- Red/Black scenario details
- raw-evidence exception examples
- adversarial test cases
```

### 12.3 Release note

Add:

```markdown
Sensitive documents should be released with care. They are written for auditors, implementers, researchers, and responsible reviewers, not for casual product marketing.
```

---

## 13. HP-011 — integrity manifest and release notes

### 13.1 Required files for package release

Before release, prepare:

```text
README.md
INDEX.md
CANONICAL_READING_ORDER.md
CHANGELOG.md
RELEASE_NOTES.md
SHA256SUMS
OPEN_ISSUES.md
OBSOLETE.md
```

### 13.2 Required SHA manifest

Every canonical `.md` file MUST be listed in:

```text
SHA256SUMS
```

Format:

```text
<sha256>  <relative/path/to/file.md>
```

### 13.3 Required release note sentence

```markdown
CCDP v0.1.1 is a hygiene release. It does not add new child-safety mechanisms. It clarifies canonical status, precedence, clean-start semantics, raw-evidence exceptions, Soft Safety Red/Black routing, and package discoverability.
```

---

## 14. HP-012 — obsolete-draft backlink in canonical CCDP

### 14.1 Problem

The canonical CCDP states that it supersedes the old draft. Future readers may still want provenance.

### 14.2 Required addition to canonical CCDP

Add:

```markdown
## Historical note

An earlier workspace-only conceptual draft existed as `CCDP v0_1.md`.
It is obsolete and non-canonical.
It is retained only as historical traceability and must not be used for implementation, citation, conformance, or package reading order.
```

---

## 15. HP-013 — future review placeholders

### 15.1 Required open issues

Add to `OPEN_ISSUES.md` or Package Index:

```text
OI-001 Developmental psychology review required.
OI-002 Jurisdictional legal review required.
OI-003 Local annex template required.
OI-004 Public whitepaper required.
OI-005 Glossary required.
OI-006 Diagrams required.
OI-007 Red-team playbook needed, but controlled release only.
OI-008 Implementation mapping to ester-clean-code not yet defined.
OI-009 EU AI Act / GDPR / DSA formal mapping not yet complete.
OI-010 Child-rights specialist review not yet complete.
```

### 15.2 Non-blocking note

These are not contradictions. They are review gaps.

---

## 16. Required patch application order

Apply hygiene patches in this order:

```text
1. HP-001 Obsolete draft isolation.
2. HP-004 Canonical precedence rule.
3. HP-005 Clean-start clarification.
4. HP-007 Raw-evidence exception centralization.
5. HP-008 Soft Safety Red/Black MUST clarification.
6. HP-002 Traceability Matrix refresh.
7. HP-003 Conformance Matrix refresh.
8. HP-006 Terminology disambiguation.
9. HP-009 Jurisdictional handoff reminders.
10. HP-010 Public / technical / sensitive split.
11. HP-011 Integrity manifest and release notes.
12. HP-012 Historical backlink.
13. HP-013 Open issues placeholders.
```

Reason:

- first remove obsolete ambiguity;
- then unify decision logic;
- then centralize exceptions;
- then update dependent matrices;
- then package for release.

---

## 17. Release boundary after v0.1.1

After applying this patch, CCDP v0.1.1 may be described as:

> A corpus-aligned draft protocol pack for child-facing persistent AI entities, defining child-`c` maturation, guardian topology, synthetic-world gateway, Soft Safety state signaling, memory minimization, adult migration, external-agent admission, conformance tests, and witness discipline under `c = a + b`, SER, Beacon, AGL, ARL, VXCX, Continuity Bundle, and L4 Witness constraints.

It MUST NOT be described as:

- complete law;
- complete psychology;
- certified child-safety standard;
- clinical safety protocol;
- product compliance guarantee;
- universal child-rearing framework;
- final implementation standard.

---

## 18. v0.1.1 acceptance checklist

A CCDP v0.1.1 package is acceptable only if:

| Check | Required result |
|---|---|
| obsolete draft isolated | PASS |
| canonical index present | PASS |
| contradiction register present | PASS |
| traceability matrix updated or addended | PASS |
| conformance matrix updated or addended | PASS |
| canonical precedence rule present | PASS |
| clean-start clarification present | PASS |
| raw-evidence exception centralized | PASS |
| Soft Safety Red/Black `MUST` clarified | PASS |
| terminology namespaces disambiguated | PASS |
| CJHN handoff references present | PASS |
| public / technical / sensitive split present | PASS |
| SHA256 manifest present | PASS |
| release notes present | PASS |
| open issues present | PASS |

---

## 19. Minimal patch snippets

### 19.1 Obsolete draft header

```markdown
> OBSOLETE / NON-CANONICAL.
> Superseded by `CCDP_v0_1_R_Corpus_Aligned.md`.
> Retained only as historical traceability.
```

### 19.2 Master precedence

```markdown
Immediate physical safety and lawful emergency duty
> jurisdictional mandatory obligations / competent authority
> parent corpus semantics
> CCDP child-specific stricter restrictions
> minimal disclosure and state-not-content
> c[q] hold / fail-closed / witness / ARL or jurisdictional handoff.
```

### 19.3 Clean start

```markdown
Clean start means clean active adult continuity, not unlawful erasure of minimal witness, legal, protection, ARL, or integrity records.
```

### 19.4 Raw evidence

```markdown
Raw child content is exceptional, minimal, standing-bound, witness-bound, reviewable, and never vendor-training, school-analytics, advertising, debugging, or social-scoring material.
```

### 19.5 Red / Black Soft Safety

```markdown
For Red / Black thresholds, `c_child` MUST route according to `CCDP_Red_Black_Escalation_Profile_v0_1.md`.
```

---

## 20. Final hygiene verdict

CCDP v0.1 is structurally coherent.

CCDP v0.1.1 is required not because the architecture contradicts itself, but because the package has become large enough that navigation, versioning, exception ownership, and terminology must be made explicit.

The correct next operation is not more safety theory.

The correct next operation is controlled release hygiene.

---

## 21. Strong closing formula

> **A child-safety protocol fails not only when its rules are wrong, but when the right rule is hidden behind the wrong file, stale index, duplicated exception, or ambiguous name.**
