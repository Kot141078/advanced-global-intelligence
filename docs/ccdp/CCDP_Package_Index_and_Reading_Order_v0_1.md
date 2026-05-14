# CCDP Package Index and Reading Order v0.1

## Child-`c` Development Protocol package navigation, canonical status, reading order, dependency graph, release boundary, and known tension register

**Status:** Draft package-control artifact
**Version:** v0.1
**Date:** 2026-05-14
**Language:** English
**Package:** Child-`c` Development Protocol (CCDP)
**Document class:** package index / reading order / corpus-control artifact
**Assertion class:** `C-A10` package-control companion; mapped protocol documents retain their own assertion classes
**Primary subject:** `a_child`
**Primary entity:** `c_child`
**Primary boundary:** child-facing persistent AI must be governed through bounded, witnessed, privacy-preserving, child-specific profiles over the existing `c = a + b / SER / L4` stack
**Release boundary:** v0.1 research protocol pack, not legal advice, not product certification, not clinical guidance

---

## 0. Executive purpose

This file is the canonical package index for the CCDP v0.1 document set.

It answers:

```text
Which CCDP files are canonical?
Which file is obsolete?
What order should a human or agent read them in?
Which documents are public-facing, technical, sensitive, or jurisdictional?
What dependency graph holds the package together?
What tensions remain before v0.1.1 cleanup?
What should be created next?
```

The index exists because CCDP has grown from one protocol into a multi-document profile pack. Without an index, the package risks becoming correct but unreadable.

Compact formula:

```text
CCDP Package Index = discoverability + canonical order + status discipline + contradiction prevention
```

---

## 1. Package thesis

CCDP is a child-specific profile over the existing AGI / SER / L4 corpus.

It does not replace:

- `c = a + b`;
- SER / SER-FED;
- Beacon Profile;
- AGL;
- ARL;
- ARQ / `c[q]`;
- VXCX;
- EA-L4 / EATP;
- Continuity Bundle / Cold Wake;
- L4 Witness;
- assertion-boundary and control-stack stop rules.

CCDP specializes those layers for child-facing persistent AI entities.

The central claim of the package is:

> A child must not grow alone with either the external synthetic world or an immature personal `c`.

The central design rule is:

> `c_child` must protect development, not own the child; signal state, not content; preserve continuity, not archive childhood; and support adult migration as a real choice.

---

## 2. Canonical / obsolete status

### 2.1 Canonical root

| Status | File | Role |
|---|---|---|
| **CANONICAL ROOT** | `CCDP_v0_1_R_Corpus_Aligned.md` | Corpus-aligned root document for CCDP v0.1. All child-specific modules depend on this version. |

### 2.2 Obsolete draft

| Status | File | Handling |
|---|---|---|
| **OBSOLETE / NON-CANONICAL** | `CCDP%20v0_1.md` | Earlier conversational concept draft. Must not be used as a protocol source. Retain only as historical workspace material or move to `archive/obsolete/`. |

Recommended header for the obsolete file:

```markdown
> OBSOLETE / NON-CANONICAL.
> Superseded by CCDP_v0_1_R_Corpus_Aligned.md.
> Retained only as conversational concept history.
> Do not cite as the canonical CCDP protocol.
```

---

## 3. Canonical document registry

### 3.1 Core package-control documents

| ID | File | Short name | Status | Function |
|---|---|---|---|---|
| `CCDP-ROOT` | `CCDP_v0_1_R_Corpus_Aligned.md` | CCDP Root | canonical root | Defines child-`c` architecture, dependency stack, maturity, guardianship, gateway, memory, and adult migration frame. |
| `CCDP-TRACE` | `CCDP_Traceability_Matrix_v0_1.md` | Traceability Matrix | canonical control artifact, needs v0.1.1 refresh | Maps CCDP claims to parent corpus layers and identifies duplication risks. |
| `CCDP-THREAT` | `CCDP_Threat_Model_v0_1.md` | Threat Model | canonical companion | Abuse-case and mitigation model for child-facing persistent AI entities. |
| `CCDP-CONF` | `CCDP_Conformance_Test_Matrix_v0_1.md` | Conformance Matrix | canonical test artifact, needs v0.1.1 refresh | Tests CCDP compatibility and prevents CCDP-washing. |
| `CCDP-INDEX` | `CCDP_Package_Index_and_Reading_Order_v0_1.md` | Package Index | current file | Defines package navigation, status, reading order, and known tensions. |

### 3.2 Recognition, entry, and synthetic-world gateway

| ID | File | Short name | Function |
|---|---|---|---|
| `CCDP-CBE` | `Child_Beacon_Extension_v0_1.md` | CBE | Child-specific permission overlay over Beacon Profile v0.1. |
| `CCDP-EAH` | `External_Agent_Handshake_for_CCDP_v0_1.md` | EAH | Entry protocol for external agents, generated media, toys, robots, peer-`c`, school systems, and other non-local presences. |
| `CCDP-CPAP` | `Child_Physical_Agent_Perimeter_v0_1.md` | CPAP | Physical-agent perimeter for toys, robots, NPCs, sensors, actuators, proximity, and embodied systems. |
| `CCDP-PCX` | `Peer_C_Child_Exchange_Profile_v0_1.md` | PCX | Peer-`c` exchange profile for child-to-child interaction. |
| `CCDP-CEXP` | `Child_Experience_Exchange_Profile_v0_1.md` | CEXP | Child-safe experience exchange profile over VXCX / LA / EA. |

### 3.3 Guardian, safety routing, and institutional boundary

| ID | File | Short name | Function |
|---|---|---|---|
| `CCDP-GTARL` | `Guardian_Topology_ARL_Matrix_v0_1.md` | GTARL | Guardian roles, standing, admissible evidence, freeze/quarantine, lawful re-entry. |
| `CCDP-SSS` | `Soft_Safety_State_Signaling_Profile_v0_1.md` | Soft Safety / SSS | State-not-content signaling, disclosure ladder, Red/Black-compatible routing. |
| `CCDP-RB` | `CCDP_Red_Black_Escalation_Profile_v0_1.md` | Red/Black | Urgent safety routing and unsafe-guardian bypass. |
| `CCDP-CSIP` | `CCDP_School_Interface_Profile_v0_1.md` | CSIP | School access, educational summaries, institutional boundaries, sealed-zone exclusion. |
| `CCDP-CJHN` | `CCDP_Jurisdictional_Handoff_Notes_v0_1.md` | CJHN | Handoff to local law, school duties, child-protection routes, regulators, courts, or qualified legal review. |

### 3.4 Memory, continuity, witness, and adult migration

| ID | File | Short name | Function |
|---|---|---|---|
| `CCDP-CMAM` | `Child_Memory_and_Adult_Migration_v0_1.md` | CMAM | Child memory lifecycle, sealed zones, forgetting rights, continuity-bundle extension, adult migration review. |
| `CCDP-MMAP` | `CCDP_Memory_Map_JSON_Schema_v0_1.md` | Memory Map | Machine-readable memory inventory, visibility, retention, sealed zones, quarantine, witness links, migration posture. |
| `CCDP-AMCL` | `CCDP_Adult_Migration_Checklist_v0_1.md` | AMCL | Reviewable transition procedure from `c_child` to adult-controlled continuity. |
| `CCDP-SZ` | `CCDP_Sealed_Zone_Profile_v0_1.md` | Sealed Zone | Protected adolescent memory compartments. |
| `CCDP-CWE` | `CCDP_Witness_Event_Schema_v0_1.md` | Witness Event Schema | Child-safe witness records for privileged transitions; maps to L4 Witness. |

### 3.5 Developmental behavior, ambiguity, and dependency

| ID | File | Short name | Function |
|---|---|---|---|
| `CCDP-CDAP` | `Child_Dependency_Audit_Profile_v0_1.md` | Dependency Audit | Dependency, oracle-addiction, overpresence, exclusive attachment risk. |
| `CCDP-CCQ` | `Child_cq_Signal_Profile_v0_1.md` | Child `c[q]` | Non-collapse profile for ambiguous child signals. |

---

## 4. Recommended reading order

### 4.1 Minimal reader path

For a reader who needs to understand the package quickly:

```text
1. CCDP_Package_Index_and_Reading_Order_v0_1.md
2. CCDP_v0_1_R_Corpus_Aligned.md
3. CCDP_Traceability_Matrix_v0_1.md
4. CCDP_Threat_Model_v0_1.md
5. Soft_Safety_State_Signaling_Profile_v0_1.md
6. Child_Beacon_Extension_v0_1.md
7. Guardian_Topology_ARL_Matrix_v0_1.md
8. Child_Memory_and_Adult_Migration_v0_1.md
9. CCDP_Red_Black_Escalation_Profile_v0_1.md
10. CCDP_Jurisdictional_Handoff_Notes_v0_1.md
```

### 4.2 Full protocol reading order

For a technical / architectural reader:

```text
A. Package control
  01. CCDP_Package_Index_and_Reading_Order_v0_1.md
  02. CCDP_v0_1_R_Corpus_Aligned.md
  03. CCDP_Traceability_Matrix_v0_1.md
  04. CCDP_Threat_Model_v0_1.md
  05. CCDP_Conformance_Test_Matrix_v0_1.md

B. Recognition and synthetic-world entry
  06. Child_Beacon_Extension_v0_1.md
  07. External_Agent_Handshake_for_CCDP_v0_1.md
  08. Child_Physical_Agent_Perimeter_v0_1.md
  09. Peer_C_Child_Exchange_Profile_v0_1.md
  10. Child_Experience_Exchange_Profile_v0_1.md

C. Safety, guardian topology, and institutional access
  11. Soft_Safety_State_Signaling_Profile_v0_1.md
  12. Guardian_Topology_ARL_Matrix_v0_1.md
  13. CCDP_Red_Black_Escalation_Profile_v0_1.md
  14. CCDP_School_Interface_Profile_v0_1.md
  15. CCDP_Jurisdictional_Handoff_Notes_v0_1.md

D. Memory, witness, and adult migration
  16. Child_Memory_and_Adult_Migration_v0_1.md
  17. CCDP_Memory_Map_JSON_Schema_v0_1.md
  18. CCDP_Witness_Event_Schema_v0_1.md
  19. CCDP_Sealed_Zone_Profile_v0_1.md
  20. CCDP_Adult_Migration_Checklist_v0_1.md

E. Developmental risk and ambiguity
  21. Child_Dependency_Audit_Profile_v0_1.md
  22. Child_cq_Signal_Profile_v0_1.md
```

### 4.3 Implementation / conformance reading order

For implementers and auditors:

```text
1. CCDP_Conformance_Test_Matrix_v0_1.md
2. CCDP_Witness_Event_Schema_v0_1.md
3. CCDP_Memory_Map_JSON_Schema_v0_1.md
4. Child_Beacon_Extension_v0_1.md
5. External_Agent_Handshake_for_CCDP_v0_1.md
6. Soft_Safety_State_Signaling_Profile_v0_1.md
7. Guardian_Topology_ARL_Matrix_v0_1.md
8. CCDP_Red_Black_Escalation_Profile_v0_1.md
9. Child_Memory_and_Adult_Migration_v0_1.md
10. CCDP_Adult_Migration_Checklist_v0_1.md
```

### 4.4 School / institutional reading order

```text
1. CCDP_v0_1_R_Corpus_Aligned.md
2. Soft_Safety_State_Signaling_Profile_v0_1.md
3. CCDP_School_Interface_Profile_v0_1.md
4. Guardian_Topology_ARL_Matrix_v0_1.md
5. CCDP_Red_Black_Escalation_Profile_v0_1.md
6. CCDP_Jurisdictional_Handoff_Notes_v0_1.md
7. CCDP_Conformance_Test_Matrix_v0_1.md
```

### 4.5 Parent / guardian reading order

```text
1. CCDP_v0_1_R_Corpus_Aligned.md
2. Soft_Safety_State_Signaling_Profile_v0_1.md
3. Child_Dependency_Audit_Profile_v0_1.md
4. CCDP_Sealed_Zone_Profile_v0_1.md
5. Child_Memory_and_Adult_Migration_v0_1.md
6. CCDP_Red_Black_Escalation_Profile_v0_1.md
7. CCDP_Adult_Migration_Checklist_v0_1.md
```

---

## 5. Dependency graph

### 5.1 High-level graph

```text
c = a + b / L4
  -> SER / SER-FED
    -> Beacon Profile
    -> AGL
    -> ARL
    -> ARQ / c[q]
    -> VXCX / LA / EA / EATP
    -> Continuity Bundle / Cold Wake
    -> L4 Witness
      -> CCDP_v0_1_R_Corpus_Aligned
        -> Traceability Matrix
        -> Threat Model
        -> Child Beacon Extension
        -> Soft Safety State Signaling
        -> Guardian Topology / ARL Matrix
        -> Child Memory and Adult Migration
        -> Witness Event Schema
        -> Memory Map JSON Schema
        -> Conformance Test Matrix
        -> Adult Migration Checklist
        -> Sealed Zone Profile
        -> Dependency Audit Profile
        -> Physical Agent Perimeter
        -> External Agent Handshake
        -> Peer-c Child Exchange
        -> Child Experience Exchange
        -> Child c[q] Signal Profile
        -> School Interface Profile
        -> Red / Black Escalation Profile
        -> Jurisdictional Handoff Notes
        -> Package Index
```

### 5.2 Operational sequence for external contact

```text
External claimant
  -> AGL grounding
  -> Beacon recognition
  -> CBE child-specific permission overlay
  -> External Agent Handshake
  -> c_child gateway
  -> maturity / Soft Safety / dependency / physical perimeter checks
  -> ARL if disputed
  -> L4-compatible CCDP witness event
  -> allow / mediate / sandbox / block / quarantine / escalate
```

### 5.3 Operational sequence for memory and adult migration

```text
c_child memory operation
  -> CMAM memory class
  -> Memory Map entry
  -> Sealed Zone / dependency / c[q] check where applicable
  -> Witness Event if privileged
  -> ARL if disputed
  -> Adult Migration Checklist at legal / developmental boundary
  -> Continuity Bundle / fork / seal / clean start / witness-only residue
```

### 5.4 Operational sequence for urgent safety

```text
child signal / external threat / physical event
  -> c[q] unless delay increases danger
  -> Soft Safety state
  -> safe guardian route check
  -> Red if safe route exists
  -> Black if ordinary guardian route may be unsafe
  -> minimal disclosure package
  -> witness boundary event
  -> post-event ARL review
  -> Memory Map update
```

---

## 6. Public / technical / sensitive split

### 6.1 Public layer

Suitable for publication as conceptual / architectural material:

- `CCDP_v0_1_R_Corpus_Aligned.md`
- `CCDP_Package_Index_and_Reading_Order_v0_1.md`
- `Child_Beacon_Extension_v0_1.md` with sensitive examples reviewed
- `Soft_Safety_State_Signaling_Profile_v0_1.md` with sensitive examples reviewed
- `Child_Memory_and_Adult_Migration_v0_1.md`
- `CCDP_School_Interface_Profile_v0_1.md`
- `CCDP_Jurisdictional_Handoff_Notes_v0_1.md`

### 6.2 Technical layer

For engineers, auditors, and protocol reviewers:

- `CCDP_Traceability_Matrix_v0_1.md`
- `CCDP_Conformance_Test_Matrix_v0_1.md`
- `CCDP_Witness_Event_Schema_v0_1.md`
- `CCDP_Memory_Map_JSON_Schema_v0_1.md`
- `External_Agent_Handshake_for_CCDP_v0_1.md`
- `Child_Physical_Agent_Perimeter_v0_1.md`
- `Peer_C_Child_Exchange_Profile_v0_1.md`
- `Child_Experience_Exchange_Profile_v0_1.md`
- `CCDP_Adult_Migration_Checklist_v0_1.md`

### 6.3 Sensitive / controlled-publication layer

Should be published only with careful review, redaction, or abuse-case sanitization:

- `CCDP_Threat_Model_v0_1.md`
- `Guardian_Topology_ARL_Matrix_v0_1.md`
- `CCDP_Red_Black_Escalation_Profile_v0_1.md`
- `CCDP_Sealed_Zone_Profile_v0_1.md`
- `Child_Dependency_Audit_Profile_v0_1.md`
- `Child_cq_Signal_Profile_v0_1.md`

Reason:

```text
These documents contain sensitive abuse patterns, unsafe-guardian routing, dependency patterns, sealed-zone behavior, and crisis-handling logic.
They are important, but they should not become a misuse guide.
```

---

## 7. Known tensions and v0.1.1 patch register

This package has no known critical contradiction at the load-bearing level, but it has known tensions that should be fixed before a clean release.

### KT-001 — obsolete draft discoverability

**Issue:** `CCDP%20v0_1.md` remains visible and may be mistaken for canonical.
**Severity:** Medium.
**Fix:** Move to `archive/obsolete/` and add `OBSOLETE / NON-CANONICAL` header.

### KT-002 — Traceability Matrix needs refresh

**Issue:** Traceability Matrix predates later modules.
**Severity:** Medium.
**Fix:** Produce `CCDP_Traceability_Matrix_v0_1_1.md` or add an appendix listing all later modules.

### KT-003 — Conformance Matrix needs refresh

**Issue:** Conformance Matrix predates some late profiles and should explicitly map them.
**Severity:** Medium.
**Fix:** Produce `CCDP_Conformance_Test_Matrix_v0_1_1.md` with references to Red/Black, CJHN, CCQ, CEXP, EAH, CPAP, PCX.

### KT-004 — precedence hierarchy wording differs across documents

**Issue:** Different documents state precedence in compatible but non-identical words.
**Severity:** Medium.
**Canonical master rule:**

```text
1. Immediate physical safety and lawful emergency duty.
2. Jurisdictional mandatory obligations / competent authority.
3. Parent corpus semantics: Beacon, AGL, ARL, VXCX, L4 Witness, Continuity Bundle.
4. CCDP child-specific stricter restrictions may narrow privileges, but may not weaken parent layers.
5. Minimal disclosure and state-not-content apply wherever possible.
6. If unresolved: hold c[q], fail closed, preserve witness, route to ARL / jurisdictional handoff.
```

### KT-005 — clean start must not imply unlawful erasure

**Issue:** “Clean start” may be misread as deletion of all traces, including lawful witness records.
**Severity:** Medium.
**Fix:** Add across CMAM / AMCL / Memory Map:

```text
Clean start means clean active adult continuity.
It does not mean unlawful erasure of minimal witness, legal, protection, or integrity records.
```

### KT-006 — term collision: C-levels

**Issue:** `C0–C5`, `CCDP-0…5`, and `C-A4/C-A7/C-A10` may confuse readers.
**Severity:** Low-medium.
**Fix:** Glossary must distinguish:

```text
Child maturity level: CM0–CM5 or CCDP maturity C0–C5
CCDP conformance class: CCDP-0…CCDP-5
Assertion class: C-A1…C-A10
```

### KT-007 — raw evidence exception should be canonicalized

**Issue:** Raw evidence exception appears in multiple documents.
**Severity:** Medium.
**Fix:** Canonicalize in `CCDP_Witness_Event_Schema_v0_1.md` and reference it elsewhere.

### KT-008 — Soft Safety MAY/MUST threshold clarification

**Issue:** Soft Safety says `c_child` MAY signal attention; for Red/Black thresholds routing should be mandatory.
**Severity:** Medium.
**Fix:** Add:

```text
For Red / Black thresholds, c_child MUST route or escalate according to the Red / Black Escalation Profile.
```

---

## 8. Release boundary for v0.1

### 8.1 What v0.1 is

CCDP v0.1 is:

- a research protocol pack;
- a child-facing profile over a broader AGI / SER / L4 corpus;
- an architectural and governance proposal;
- a modular safety protocol family;
- a corpus-aligned draft suitable for critique, review, and controlled publication.

### 8.2 What v0.1 is not

CCDP v0.1 is not:

- legal advice;
- a certified child-protection system;
- a medical or therapeutic protocol;
- a psychological diagnosis framework;
- a vendor certification by itself;
- a government compliance guarantee;
- a school policy ready for deployment without jurisdictional review;
- an implementation specification complete enough for production.

### 8.3 Minimum release package

A minimal v0.1 release should include:

```text
CCDP_Package_Index_and_Reading_Order_v0_1.md
CCDP_v0_1_R_Corpus_Aligned.md
CCDP_Traceability_Matrix_v0_1.md
CCDP_Threat_Model_v0_1.md
Child_Beacon_Extension_v0_1.md
Soft_Safety_State_Signaling_Profile_v0_1.md
Guardian_Topology_ARL_Matrix_v0_1.md
Child_Memory_and_Adult_Migration_v0_1.md
CCDP_Witness_Event_Schema_v0_1.md
CCDP_Memory_Map_JSON_Schema_v0_1.md
CCDP_Conformance_Test_Matrix_v0_1.md
CCDP_Jurisdictional_Handoff_Notes_v0_1.md
```

A full v0.1 release should include all canonical files listed in Section 3.

---

## 9. Required future files

### 9.1 Near-term package hygiene

```text
CCDP_Glossary_v0_1.md
CCDP_Contradiction_Register_v0_1.md
CCDP_CHANGELOG_v0_1.md
CCDP_SHA256SUMS
CCDP_RELEASE_NOTES_v0_1.md
CCDP_PUBLIC_SUMMARY_v0_1.md
```

### 9.2 Specialist review notes

```text
CCDP_Developmental_Psychology_Review_Notes_v0_1.md
CCDP_Legal_Review_Questions_EU_BE_v0_1.md
CCDP_Red_Team_Playbook_v0_1.md
CCDP_Public_Private_Sensitive_Split_v0_1.md
```

### 9.3 Implementation support

```text
CCDP_Implementation_Gap_Assessment_Checklist_v0_1.md
CCDP_Vendor_Conformance_Guide_v0_1.md
CCDP_Parent_Guide_v0_1.md
CCDP_School_Guide_v0_1.md
```

---

## 10. Acceptance checklist for package integrity

Before publication or repository integration, the package SHOULD pass this checklist.

| Check | Required state |
|---|---|
| Canonical root identified | `CCDP_v0_1_R_Corpus_Aligned.md` |
| Old draft isolated | `CCDP%20v0_1.md` marked obsolete or archived |
| Reading order present | This file |
| Parent corpus dependencies listed | Root + Traceability |
| No new Beacon semantics | CBE remains overlay |
| No new ARL court | GTARL remains ARL-compatible matrix |
| No raw child life default | CMAM / Memory Map / Witness / CEXP / PCX / CPAP |
| Soft Safety formalized | SSS profile |
| Red/Black separated | RB profile |
| Adult migration explicit | CMAM + AMCL |
| Conformance tests present | CTM |
| Witness schema present | CWE |
| Jurisdictional boundary present | CJHN |
| Known tensions recorded | Section 7 |
| Public / technical / sensitive split defined | Section 6 |
| SHA-256 manifest generated | pending release packaging |

---

## 11. One-page map

```text
If you want the idea:
  CCDP_v0_1_R_Corpus_Aligned.md

If you want the dependency proof:
  CCDP_Traceability_Matrix_v0_1.md

If you want what can go wrong:
  CCDP_Threat_Model_v0_1.md

If you want external-entry rules:
  Child_Beacon_Extension_v0_1.md
  External_Agent_Handshake_for_CCDP_v0_1.md

If you want parent/school/vendor/state boundaries:
  Soft_Safety_State_Signaling_Profile_v0_1.md
  Guardian_Topology_ARL_Matrix_v0_1.md
  CCDP_School_Interface_Profile_v0_1.md
  CCDP_Jurisdictional_Handoff_Notes_v0_1.md

If you want crisis routing:
  CCDP_Red_Black_Escalation_Profile_v0_1.md

If you want memory and adulthood:
  Child_Memory_and_Adult_Migration_v0_1.md
  CCDP_Memory_Map_JSON_Schema_v0_1.md
  CCDP_Adult_Migration_Checklist_v0_1.md
  CCDP_Sealed_Zone_Profile_v0_1.md

If you want proof and testing:
  CCDP_Witness_Event_Schema_v0_1.md
  CCDP_Conformance_Test_Matrix_v0_1.md

If you want embodied / social / experience surfaces:
  Child_Physical_Agent_Perimeter_v0_1.md
  Peer_C_Child_Exchange_Profile_v0_1.md
  Child_Experience_Exchange_Profile_v0_1.md

If you want developmental ambiguity and dependency:
  Child_cq_Signal_Profile_v0_1.md
  Child_Dependency_Audit_Profile_v0_1.md
```

---

## 12. Closing note

This package is intentionally cautious.

A child-facing `c` is not a toy, not a product add-on, not a parent dashboard, not a school scoring tool, and not a state instrument.

It is a protected developmental presence.

The package therefore treats child-facing AI not as an application class, but as an institutional boundary problem:

```text
recognition without registry;
safety without surveillance;
privacy without abandonment;
memory without destiny;
continuity without ownership;
protection without capture.
```
