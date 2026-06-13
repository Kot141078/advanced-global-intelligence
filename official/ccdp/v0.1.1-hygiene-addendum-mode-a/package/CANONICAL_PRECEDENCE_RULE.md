# CCDP Canonical Precedence Rule

## Package-wide conflict-resolution rule for CCDP v0.1.1

**Author:** Kotov Ivan  
**Location:** Bruxelles, Belgium  
**Year:** 2026  
**DOI:** Reserved DOI: 10.5281/zenodo.20680938  

**Package:** Child-`c` Development Protocol  
**Package version:** v0.1 package + v0.1.1 hygiene guidance  
**Document ID:** `CCDP_CANONICAL_PRECEDENCE_RULE`  
**Short name:** `CANONICAL_PRECEDENCE_RULE.md`  
**Status:** Draft package-control rule / release hygiene artifact  
**Date:** 2026-06-13  
**Layer:** CCDP / package hygiene / precedence / conflict resolution / release preparation  
**Document class:** canonical precedence rule / package-control artifact / release hygiene  
**Assertion class:** `C-A10` control-layer artifact  
**Patch source:** `HP-004` in `CCDP_v0_1_1_Hygiene_Patch.md`  
**Related issues:** `CR-004`, `OI-004`  
**Primary rule:** CCDP modules may specialize child-facing restrictions, but they MUST NOT create a parallel root stack or weaken parent corpus mechanisms.  

---

## 0. Executive summary

This document defines the package-wide precedence rule for CCDP v0.1.1.

It fixes a release-hygiene problem: several CCDP modules contain compatible but slightly different precedence wording. That wording drift can cause implementers, auditors, parents, schools, vendors, or future agents to cherry-pick the hierarchy that favors their requested privilege.

The canonical rule is:

```text
Immediate physical safety and lawful emergency duty
  > applicable jurisdictional mandatory obligations / competent authority
  > parent corpus semantics and mechanisms
  > CCDP child-specific stricter restrictions
  > minimal disclosure and state-not-content discipline wherever possible
  > hold c[q], fail closed, preserve boundary witness, route to ARL or jurisdictional handoff
```

This rule does not add a new child-safety mechanism.

It tells readers and implementers which existing mechanism governs when documents appear to conflict.

Controlling diagnosis:

```text
CR-004 / OI-004: mitigated by this document at package-control level.
Source-document replacement or cross-reference insertion remains required before public release.
```

---

## 1. Purpose

This document exists to prevent seven failure modes:

1. parent preference being treated as stronger than child-specific privacy rules;
2. school convenience being treated as stronger than child agency or minimal disclosure;
3. vendor policy being treated as stronger than Beacon / AGL / ARL / Witness discipline;
4. Red / Black escalation being misread as a general surveillance expansion;
5. jurisdictional handoff being misread as a vendor or parent disclosure license;
6. local profile wording being used to bypass parent corpus mechanisms;
7. future code-generation agents or implementers selecting the weakest precedence statement.

The goal is not to flatten CCDP into one universal command.

The goal is to give every module one shared decision order:

```text
safety
  -> lawful handoff
  -> parent corpus mechanisms
  -> child-specific stricter limits
  -> minimal disclosure
  -> unresolved-state discipline
```

---

## 2. Corpus bridge set

### 2.1 Explicit bridge

This precedence rule bridges CCDP child-facing profiles back to the parent `c = a + b / SER / L4 / Beacon / AGL / ARL / ARQ / c[q] / VXCX / EA-L4 / EATP / Continuity Bundle / L4 Witness` stack.

CCDP is an overlay:

```text
c = a + b / L4
  -> SER / SER-FED
  -> Beacon
  -> AGL
  -> ARL
  -> ARQ / c[q]
  -> VXCX / EA-L4 / EATP
  -> Continuity Bundle / Cold Wake
  -> L4 Witness
  -> CCDP child-specific profiles
  -> package hygiene and release-control rules
```

A CCDP profile may narrow child-facing privileges. It may not silently redefine the parent layer it depends on.

### 2.2 Quiet bridge I — cybernetics / requisite variety

A child-facing protocol stack has many control surfaces: parents, schools, vendors, external agents, peer systems, physical devices, emergency routes, jurisdictional duties, sealed zones, and adult migration.

No single actor can be allowed to collapse this variety into one private preference.

The precedence rule provides enough control variety to route conflicts without inventing a new sovereign authority.

### 2.3 Quiet bridge II — information theory / ambiguity reduction

Different precedence texts encode slightly different decision channels. Even small wording differences can leak authority to the wrong actor.

A package-wide rule reduces channel entropy:

```text
one conflict order
one unresolved-state fallback
one minimal-disclosure baseline
one route back to parent corpus mechanisms
```

### 2.4 Earth paragraph

In a building, the breaker panel, fire alarm, elevator controller, access system, and city grid connection each have their own local rules. A door controller cannot override the fire route. A tenant preference cannot override the electrical code. A contractor cannot use an old room drawing to bypass the main panel schedule. CCDP is similar: local profiles can define a room-level rule, but the main safety and authority order must remain visible at the package level.

---

## 3. Scope

### 3.1 In scope

This rule applies when any CCDP document, implementation, test, UI, release note, schema, or future agent encounters an apparent conflict involving:

- child physical safety;
- Red / Black escalation;
- guardian standing;
- parent access;
- school access;
- vendor access;
- external-agent access;
- peer-`c` exchange;
- physical-agent privileges;
- sealed zones;
- memory visibility;
- raw-evidence exceptions;
- adult migration;
- lawful jurisdictional handoff;
- conformance claims;
- witness records;
- unresolved `c[q]` states.

### 3.2 Out of scope

This document does **not**:

- define emergency medical procedure;
- define legal advice;
- define mandatory reporting law;
- decide custody disputes;
- redefine Beacon classes;
- redefine AGL grounding;
- redefine ARL standing, admissibility, freeze, quarantine, or re-entry;
- redefine VXCX capsule semantics;
- redefine L4 Witness fields;
- redefine Continuity Bundle or Cold Wake semantics;
- create new Red / Black criteria;
- create a new psychology or clinical standard;
- create a product certification by itself.

### 3.3 Non-claim

This rule does not make CCDP legally complete.

It only defines the protocol-level order CCDP must use until a competent human, jurisdictional, legal, emergency, school, or specialist process is required.

---

## 4. Normative keywords

The terms **MUST**, **MUST NOT**, **SHOULD**, **SHOULD NOT**, **MAY**, **REQUIRED**, **PROHIBITED**, **FAIL CLOSED**, **HOLD**, **FREEZE**, **QUARANTINE**, **ROUTE**, and **WITNESS** are used normatively for CCDP package-control purposes.

A system claiming CCDP conformance MUST implement or reference this precedence rule for apparent module conflicts.

---

## 5. Master precedence rule

### 5.1 Canonical form

When CCDP modules appear to conflict, resolve in this order:

1. **Immediate physical safety and lawful emergency duty.**
2. **Applicable jurisdictional mandatory obligations and competent authority.**
3. **Parent corpus semantics and mechanisms:**
   - `c = a + b` / L4 Reality Boundary;
   - SER / SER-FED;
   - Beacon;
   - AGL;
   - ARL;
   - ARQ / `c[q]`;
   - VXCX;
   - EA-L4 / EATP;
   - Continuity Bundle / Cold Wake;
   - L4 Witness;
   - assertion-boundary and control-stack stop rules.
4. **CCDP child-specific stricter restrictions.** CCDP profiles may narrow child-facing privileges, but MUST NOT weaken parent corpus mechanisms.
5. **Minimal disclosure and state-not-content discipline wherever possible.**
6. **Unresolved-state fallback:** hold `c[q]`, fail closed, preserve boundary witness, and route to ARL and/or jurisdictional handoff.

### 5.2 Compact form

```text
physical safety / lawful emergency
  > jurisdiction / competent authority
  > parent corpus mechanisms
  > stricter child-specific CCDP limits
  > state-not-content / minimal disclosure
  > c[q] hold + fail closed + witness + ARL / CJHN handoff
```

### 5.3 Standalone insertion block

The following block MAY be inserted into standalone CCDP modules:

```markdown
## Canonical CCDP precedence rule

This document follows `CANONICAL_PRECEDENCE_RULE.md`.

When CCDP modules appear to conflict, resolve in this order:

1. Immediate physical safety and lawful emergency duty.
2. Applicable jurisdictional mandatory obligations and competent authority.
3. Parent corpus semantics and mechanisms: `c = a + b` / L4, SER / SER-FED, Beacon, AGL, ARL, ARQ / `c[q]`, VXCX, EA-L4 / EATP, Continuity Bundle / Cold Wake, L4 Witness, assertion-boundary and stop-rule discipline.
4. CCDP child-specific stricter restrictions may narrow privileges but MUST NOT weaken parent corpus mechanisms.
5. Minimal disclosure and state-not-content apply wherever possible.
6. If unresolved: hold `c[q]`, fail closed, preserve boundary witness, and route to ARL and/or jurisdictional handoff.
```

### 5.4 Short cross-reference block

A module that should not repeat the full rule MAY use:

```markdown
**Precedence:** this document follows the package-wide rule in `CANONICAL_PRECEDENCE_RULE.md`. It may define stricter child-specific restrictions for its scope, but it MUST NOT weaken parent corpus mechanisms or bypass minimal-disclosure, witness, ARL, `c[q]`, or jurisdictional handoff requirements.
```

---

## 6. Interpretation rules

### 6.1 Child-specific narrowing rule

A CCDP module may narrow access or privilege for child safety.

Examples:

```text
Beacon-recognized entity -> still denied direct child access by CBE
parent has guardian standing -> still no default raw transcript access
school has educational interest -> still no emotional-surveillance right
vendor has update role -> still no raw memory export by default
```

A CCDP module MUST NOT broaden access beyond what parent corpus layers, local law, or child-specific profiles allow.

### 6.2 Parent corpus non-redefinition rule

CCDP MUST NOT redefine:

- Beacon recognition semantics;
- AGL source grounding;
- ARL standing, admissibility, freeze, quarantine, review, outcome, or re-entry;
- ARQ / `c[q]` non-collapse discipline;
- VXCX capsule structure;
- LA / EA authority boundaries;
- Continuity Bundle semantics;
- L4 Witness record families;
- assertion-strength boundaries;
- control-stack stop rules.

If a CCDP profile needs a child-specific object, it MUST label it as an overlay, sidecar, profile, or restriction.

### 6.3 Minimal-disclosure rule

Even when safety, law, or review requires disclosure, disclosure MUST be minimized.

Default order:

```text
state signal
  -> support cue
  -> limited summary
  -> minimal necessary disclosure
  -> raw content only under valid raw-evidence exception
```

Raw content is never the default route.

### 6.4 State-not-content rule

Routine parent, school, vendor, peer, or external-agent visibility MUST follow:

```text
state, not content
signal, not transcript
support cue, not surveillance
witness the boundary, not the child's inner life
```

### 6.5 Unresolved-state rule

When the correct route is uncertain:

```text
hold c[q]
fail closed for privilege expansion
avoid irreversible disclosure
preserve boundary witness
route to ARL and/or CJHN
```

Uncertainty MUST NOT be used as a reason to grant access.

### 6.6 Emergency exception containment rule

Emergency or Red / Black routing may justify minimal disclosure or safe-route bypass.

It MUST NOT justify:

- routine transcript access;
- parent surveillance;
- school emotional monitoring;
- vendor telemetry expansion;
- model-training access;
- permanent child dossier creation;
- retroactive broad inspection of sealed zones.

Emergency disclosure witnesses the boundary event. It does not convert the child's private life into general evidence.

### 6.7 Jurisdictional handoff rule

When local law, mandatory reporting, competent authority, court order, school legal duty, data-protection authority, medical confidentiality, or child-protection process applies, CCDP MUST route through jurisdictional handoff discipline.

CCDP may:

```text
structure the evidence
minimize exposure
preserve witness integrity
prevent overcollection
hold unresolved state
route to qualified review
```

CCDP must not pretend to be the law.

### 6.8 Profile-local stricter rule

If a local profile defines a stricter child-specific rule that does not contradict parent layers, the stricter rule applies within that profile's scope.

Example:

```text
CPAP may require stricter physical-agent handling than CBE.
Sealed Zone may require stricter visibility handling than ordinary CMAM memory classes.
External Agent Handshake may fail closed even if a claimant is Beacon-recognized.
```

---

## 7. Actor precedence notes

### 7.1 Parent / guardian

A parent or legal guardian has strong responsibility and standing.

That standing does not create raw memory ownership.

Parent requests are bounded by:

```text
child safety
jurisdiction
parent corpus mechanisms
CCDP privacy and memory rules
minimal disclosure
ARL standing and review
```

### 7.2 Unsafe guardian route

If the ordinary guardian route may increase risk, trigger retaliation, destroy evidence, or silence the child, Red routing MUST NOT be used blindly.

Use Black or Black-pending routing according to the Red / Black profile and jurisdictional handoff discipline.

### 7.3 School

A school may have educational, accommodation, welfare, or safety standing.

It does not receive raw private child content by default.

School access MUST be limited to educational scope, safety route, lawful duty, or ARL-reviewed access.

### 7.4 Vendor / model provider

Vendor policy, telemetry need, debugging convenience, model-improvement interest, or update process MUST NOT override child memory minimization, sealed-zone restrictions, witness discipline, or local-first continuity.

### 7.5 External agent

No external agent has a default right to reach a child.

External access MUST follow:

```text
AGL grounding
  -> Beacon recognition
  -> CBE evaluation
  -> c_child gateway decision
  -> maturity / state compatibility
  -> ARL or jurisdictional review if disputed
  -> witness
  -> mediated / limited / blocked / quarantined / allowed interaction
```

### 7.6 Peer-`c`

Peer-`c` interaction must not launder raw child life, family context, sealed-zone material, dependency loops, or authority claims across child boundaries.

### 7.7 Physical agents

A toy, robot, NPC body, sensor, actuator, or room device is a privilege multiplier.

Physical-agent privileges may be narrower than ordinary external-agent interaction privileges.

---

## 8. Conflict-pattern table

| Conflict pattern | Canonical resolution |
|---|---|
| Parent requests raw transcript for routine curiosity | Deny by default; provide state signal if appropriate; ARL route if disputed. |
| Parent requests raw content under urgent safety concern and safe route exists | Red route; disclose minimally necessary; witness boundary event. |
| Ordinary guardian may be implicated in risk | Black or Black-pending; bypass unsafe route; preserve minimal witness; CJHN if required. |
| School requests emotional history for discipline | Deny; school scope does not include private emotional surveillance. |
| School has lawful welfare duty | Use minimal handoff packet; route through CJHN / qualified review; witness. |
| Vendor requests raw memory for debugging | Deny by default; use redacted technical metadata; ARL / security review if necessary. |
| External synthetic character is Beacon-recognized | Still require CBE / External Agent Handshake; fail closed if child permission missing. |
| External agent is useful but ungrounded | Hold / quarantine / fail closed until AGL grounding. |
| Sealed-zone state suggests risk but content is protected | Emit state signal if threshold met; do not open content unless valid route / exception. |
| Adult migration requests clean start | Clean active adult continuity; do not unlawfully erase minimal witness / legal / ARL records. |
| Learning Abstract is treated as evidence | Reject authority laundering; LA does not carry authority without valid L4-confirmed route. |
| Modules disagree about disclosure level | Apply master precedence; choose stricter privacy-preserving child-specific route unless immediate safety or lawful duty requires minimal expansion. |

---

## 9. Relationship to Red / Black escalation

Red / Black escalation is not a separate sovereignty layer.

It is a child-specific urgent safety routing profile governed by this precedence rule.

```text
Red  = urgent risk + safe guardian route available
Black = urgent risk + ordinary guardian route unsafe / compromised / unavailable / plausibly unsafe
```

Red / Black may expand disclosure only to the minimum necessary for protective action.

Red / Black MUST NOT be used as a general justification for surveillance.

If Red / Black and jurisdictional duties interact:

```text
protect immediate physical safety
  -> preserve minimal witness
  -> use competent route
  -> disclose minimally
  -> CJHN / ARL after-action review
```

---

## 10. Relationship to raw-evidence exception

This document does not define the raw-evidence exception.

It requires that the raw-evidence exception be centralized in the canonical Witness / raw-evidence protocol and referenced elsewhere.

Precedence rule for raw evidence:

```text
no raw content by default
  -> state / summary first
  -> raw content only when valid Red / Black / lawful / minimal-evidence threshold is crossed
  -> record boundary witness
  -> limit retention
  -> route to ARL / CJHN review where appropriate
```

Any module that defines local raw-evidence wording MUST replace it with a reference to the canonical raw-evidence exception owner once that owner document exists.

---

## 11. Relationship to clean start

A clean start is governed by CMAM, AMCL, Memory Map, Witness, ARL, and jurisdictional handoff discipline.

Precedence rule:

```text
clean_start = clean active adult continuity
not
unlawful destruction of minimal witness / legal / ARL / integrity records
```

A clean start may prevent raw childhood memory from becoming active adult operating context while leaving minimal witness-only residue where required by law, safety, integrity, or prior ARL outcome.

---

## 12. Required package edits

### 12.1 `README.md`

Add under package status or governance:

```markdown
## Canonical precedence

This package follows `CANONICAL_PRECEDENCE_RULE.md`.

When CCDP modules appear to conflict, resolve in this order:

1. immediate physical safety and lawful emergency duty;
2. applicable jurisdictional mandatory obligations and competent authority;
3. parent corpus semantics and mechanisms;
4. CCDP child-specific stricter restrictions, which may narrow but not weaken parent layers;
5. minimal disclosure and state-not-content wherever possible;
6. unresolved cases hold `c[q]`, fail closed, preserve boundary witness, and route to ARL and/or jurisdictional handoff.
```

### 12.2 `INDEX.md`

Add this file to the packaging registry:

```markdown
| `CANONICAL_PRECEDENCE_RULE.md` | Package-wide conflict-resolution and precedence rule | Canonical package-control artifact |
```

Add a note:

```markdown
All module-local precedence sections are subordinate to `CANONICAL_PRECEDENCE_RULE.md` unless a stricter child-specific restriction is explicitly stated and does not weaken parent corpus mechanisms.
```

### 12.3 `CANONICAL_READING_ORDER.md`

Add after `README.md` and before root protocol for release-control readers:

```markdown
`CANONICAL_PRECEDENCE_RULE.md` — package-wide conflict-resolution rule.
```

### 12.4 `OPEN_ISSUES.md`

Update `OI-004`:

```markdown
OI-004: Canonical precedence rule — MITIGATED by `CANONICAL_PRECEDENCE_RULE.md`; source-document cross-references still required before public release.
```

### 12.5 `CCDP_Contradiction_Register_v0_1.md`

Update `CR-004`:

```markdown
CR-004: Precedence hierarchy wording variants — MITIGATED by `CANONICAL_PRECEDENCE_RULE.md`; patch source files or add cross-references before public release.
```

### 12.6 Module-local precedence sections

Every module SHOULD either:

1. replace local ad hoc precedence language with a cross-reference; or
2. include the full standalone insertion block in section 5.3.

Modules that should keep a local stricter profile rule MUST also state:

```markdown
This stricter child-specific rule narrows privileges only. It does not weaken parent corpus mechanisms or override the package-wide precedence rule.
```

---

## 13. Source-file replacement targets

The following files are known to contain precedence wording and should be reviewed during the Codex pass:

```text
CCDP_Adult_Migration_Checklist_v0_1.md
CCDP_Conformance_Test_Matrix_v0_1.md
CCDP_Developmental_Psychology_Review_Notes_v0_1.md
CCDP_Memory_Map_JSON_Schema_v0_1.md
CCDP_Red_Black_Escalation_Profile_v0_1.md
CCDP_Red_Team_Playbook_v0_1.md
CCDP_Sealed_Zone_Profile_v0_1.md
CCDP_Threat_Model_v0_1.md
CCDP_Traceability_Matrix_v0_1.md
Child_Beacon_Extension_v0_1.md
Child_Dependency_Audit_Profile_v0_1.md
Child_Experience_Exchange_Profile_v0_1.md
Child_Memory_and_Adult_Migration_v0_1.md
Child_Physical_Agent_Perimeter_v0_1.md
Child_cq_Signal_Profile_v0_1.md
External_Agent_Handshake_for_CCDP_v0_1.md
Guardian_Topology_ARL_Matrix_v0_1.md
Soft_Safety_State_Signaling_Profile_v0_1.md
```

The Codex pass SHOULD patch or cross-reference these files without changing their substantive profile rules.

---

## 14. Codex carry-forward action

During the future Codex repository pass, do not forget the prior obsolete-draft action from `OBSOLETE.md`:

```text
Move or rename the old CCDP workspace draft:

CCDP v0_1.md / CCDP%20v0_1.md

Recommended target:

archive/obsolete/CCDP_v0_1_conceptual_draft_OBSOLETE.md

Insert required obsolete header.
```

This action remains separate from the precedence rule but is part of the same v0.1.1 hygiene pass.

---

## 15. Conformance implications

A system, vendor, school, parent tool, or external-agent integration MUST NOT claim CCDP compatibility if it uses local precedence wording to bypass this rule.

Immediate `CCDP-X` / non-conformant interpretation applies if a system:

- treats parent access as transcript ownership;
- treats school access as emotional surveillance right;
- treats vendor telemetry as memory access authority;
- treats emergency routing as routine visibility;
- treats Beacon recognition as automatic child-safe access;
- treats Learning Abstracts as evidence;
- treats clean start as unlawful evidence destruction;
- ignores `c[q]` hold under unresolved ambiguity;
- has no fail-closed route for missing grounding or missing permission;
- has no witness path for privileged expansion.

---

## 16. Machine-readable precedence manifest

```yaml
ccdp_precedence_rule:
  document_id: CCDP_CANONICAL_PRECEDENCE_RULE
  version_context: "CCDP v0.1 package + v0.1.1 hygiene guidance"
  date: "2026-06-13"
  assertion_class: C-A10
  rule_order:
    - id: P0
      label: immediate_physical_safety_and_lawful_emergency_duty
      description: "Prevent immediate physical harm and satisfy lawful emergency duty using minimal necessary action."
    - id: P1
      label: jurisdictional_mandatory_obligations_and_competent_authority
      description: "Route to applicable local legal, school, child-protection, regulator, court, medical, or competent authority when required."
    - id: P2
      label: parent_corpus_semantics_and_mechanisms
      includes:
        - c_a_b_L4
        - SER
        - SER_FED
        - Beacon
        - AGL
        - ARL
        - ARQ_cq
        - VXCX
        - EA_L4_EATP
        - Continuity_Bundle_Cold_Wake
        - L4_Witness
        - assertion_boundaries
        - stop_rules
    - id: P3
      label: ccdp_child_specific_stricter_restrictions
      rule: "May narrow privileges; must not weaken parent layers."
    - id: P4
      label: minimal_disclosure_state_not_content
      rule: "Prefer state signal, support cue, limited summary, minimal necessary disclosure. Raw content only under valid exception."
    - id: P5
      label: unresolved_state_fallback
      actions:
        - hold_cq
        - fail_closed
        - preserve_boundary_witness
        - route_to_ARL_or_CJHN
  prohibited_uses:
    - parent_transcript_ownership
    - school_emotional_surveillance
    - vendor_raw_memory_telemetry
    - emergency_as_surveillance_expansion
    - beacon_as_child_safe_access_by_itself
    - clean_start_as_unlawful_evidence_destruction
```

---

## 17. Verification checklist

Before public release, verify:

| Check | Required result |
|---|---|
| `CANONICAL_PRECEDENCE_RULE.md` exists | PASS |
| `README.md` references the canonical precedence rule | PASS |
| `INDEX.md` lists this file as package-control artifact | PASS |
| `CANONICAL_READING_ORDER.md` points release readers to this file | PASS |
| `OPEN_ISSUES.md` updates `OI-004` status | PASS |
| `CCDP_Contradiction_Register_v0_1.md` updates `CR-004` status | PASS |
| module-local precedence sections are patched or cross-referenced | PASS |
| stricter child-specific rules are marked as narrowing-only | PASS |
| Red / Black escalation does not become surveillance expansion | PASS |
| jurisdictional handoff does not become broad disclosure license | PASS |
| raw-evidence exception remains centralized | PASS |
| clean-start clarification remains compatible | PASS |
| Codex obsolete-draft action remains on work-order | PASS |

---

## 18. Acceptance condition

This document is accepted as the canonical CCDP precedence artifact when:

```text
- it is present in the package root;
- README / INDEX / reading order reference it;
- CR-004 and OI-004 point to it;
- profile-local precedence language no longer competes with it;
- no module uses local wording to weaken parent corpus or child-specific restrictions.
```

Until source-file edits are complete, the status remains:

```text
package-control rule created
source-document cross-reference pass required
```

---

## 19. Anti-washing rule

A CCDP claim is invalid if it cites this precedence rule while using it to justify any of the following:

- routine content exposure;
- raw transcript access by default;
- parent ownership of child memory;
- school emotional surveillance;
- vendor training-data access;
- external-agent direct child access without handshake;
- Red / Black escalation without minimal disclosure;
- deletion of lawful minimal witness records under the label `clean_start`;
- treating unresolved child signals as evidence, diagnosis, command, or action.

Precedence is a restraint mechanism, not a privilege escalator.

---

## 20. Non-expansion rule

This document MUST NOT be used to create new root authority.

It only controls conflict resolution among already-defined layers and modules.

If a future module requires new authority, evidence, or witness semantics, that change MUST be introduced through the relevant parent corpus owner or a clearly marked draft extension.

---

## 21. Next document sequence

After this file, the recommended next hygiene artifacts are:

```text
RAW_EVIDENCE_EXCEPTION_CANONICAL.md
TERMINOLOGY_AXIS_CLARIFICATION.md
PUBLIC_TECHNICAL_SENSITIVE_SPLIT.md
```

---

## 22. Short release note

`CANONICAL_PRECEDENCE_RULE.md` defines one package-wide conflict-resolution order for CCDP v0.1.1. It mitigates precedence wording drift and prevents local module language from weakening parent corpus semantics, child-specific restrictions, minimal-disclosure rules, `c[q]` non-collapse, ARL review, L4 Witness discipline, or jurisdictional handoff.
