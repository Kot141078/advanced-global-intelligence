# CCDP_Jurisdictional_Handoff_Notes_v0_1.md

**Title:** CCDP Jurisdictional Handoff Notes v0.1
**Short name:** CJHN v0.1
**Status:** Draft / procedural handoff notes
**Date:** 2026-05-14
**Project layer:** CCDP / Child-facing `c` governance
**Depends on:** `CCDP_v0_1_R_Corpus_Aligned`, `CCDP_Traceability_Matrix`, `CCDP_Threat_Model`, `Child_Beacon_Extension`, `Guardian_Topology_ARL_Matrix`, `Child_Memory_and_Adult_Migration`, `Soft_Safety_State_Signaling_Profile`, `CCDP_Witness_Event_Schema`, `CCDP_Memory_Map_JSON_Schema`, `CCDP_Adult_Migration_Checklist`, `CCDP_Sealed_Zone_Profile`, `Child_Dependency_Audit_Profile`, `Child_Physical_Agent_Perimeter`, `External_Agent_Handshake_for_CCDP`, `Peer_C_Child_Exchange_Profile`, `Child_Experience_Exchange_Profile`, `Child_cq_Signal_Profile`, `CCDP_School_Interface_Profile`, `CCDP_Red_Black_Escalation_Profile`
**Parent corpus:** `c = a + b`, SER, SER-FED, Beacon Profile, AGL, ARL, ARQ / `c[q]`, VXCX, EA-L4 / EATP, L4 Witness, Continuity Bundle / Cold Wake, assertion-boundary discipline
**Assertion class:** Draft procedural / jurisdictional handoff artifact
**Legal status:** Not legal advice. This document defines when a CCDP implementation must stop making architectural assumptions and hand off to applicable local law, qualified legal review, school policy, child-protection authority, regulator, or court process.

---

## 0. Purpose

CCDP cannot become a parallel legal system.

It can define:

- entity boundaries;
- child-specific safety architecture;
- memory minimization;
- state-not-content signaling;
- Beacon / CBE recognition and permission overlays;
- AGL grounding;
- ARL dispute procedures;
- L4 Witness records;
- adult migration structure.

It cannot define, replace, or override:

- local child-protection law;
- custody orders;
- school legal duties;
- medical confidentiality rules;
- mandatory reporting duties;
- criminal procedure;
- data-protection authority decisions;
- court orders;
- age-of-consent thresholds;
- national implementation of EU or non-EU law.

**CJHN defines the handoff boundary.**

It answers:

> When must CCDP stop deciding internally and route the matter to jurisdictional authority, counsel, regulator, school process, or child-protection procedure?

---

## 1. Core rule

> **CCDP governs system behavior until a jurisdictional obligation, protected legal right, or competent authority requires a local legal handoff.**

This means:

```text
CCDP may structure the evidence.
CCDP may minimize disclosure.
CCDP may preserve witness integrity.
CCDP may prevent overcollection.
CCDP may prevent parent, school, vendor, or state capture.
CCDP may delay non-urgent disclosure.

CCDP must not pretend to be the law.
```

Where applicable law is unclear, CCDP must:

```text
hold c[q]
minimize exposure
preserve the boundary witness
avoid irreversible disclosure
route to qualified review
```

---

## 2. Non-goals

CJHN does **not**:

1. provide legal advice;
2. define a universal child-rights regime;
3. harmonize jurisdictions;
4. decide custody disputes;
5. decide school reporting duties;
6. decide whether a crime occurred;
7. decide medical diagnosis or treatment;
8. create a legal personality for `c_child`;
9. give vendors a compliance shield;
10. allow parents to waive the child's rights by broad consent.

CJHN is a **handoff discipline**, not a legal conclusion engine.

---

## 3. Corpus bridge set

### 3.1 Explicit bridge

`c = a + b` places the accountable human anchor `a` inside a jurisdiction. Therefore a child-facing `c_child` must not be treated as lawless software. It inherits the local legal environment of `a_child`, while remaining constrained by SER / L4 / Beacon / ARL / witness discipline.

### 3.2 Quiet bridge I

Ashby's law of requisite variety applies operationally: one global CCDP rule cannot control every legal environment. The protocol must preserve enough routing variety to hand off to local authorities, schools, courts, regulators, and guardians without collapsing all cases into one generic "safety" path.

### 3.3 Quiet bridge II

Information theory applies to disclosure: raw transcripts are high-leakage channels. Jurisdictional handoff must transmit the smallest legally meaningful signal with enough integrity to support review, not a full export of childhood life.

### 3.4 Earth paragraph

In a real building, electrical protection does not end at the appliance. A device has internal fuses, but the room has breakers, the building has a panel, the street has a grid operator, and the state has inspection law. CCDP is the internal fuse and local panel for `c_child`; jurisdiction is the external grid. If the fault crosses the panel boundary, pretending that the device can solve it alone is bad engineering.

---

## 4. Jurisdictional objects

CJHN uses the following objects.

| Object | Meaning |
|---|---|
| `jurisdiction` | Legal environment applicable to the child, guardian, school, vendor, device, data storage, or incident. |
| `competent_authority` | Entity legally authorized to decide, investigate, require disclosure, or enforce a duty. |
| `qualified_review` | Legal, compliance, school, welfare, or professional review by a competent person or body. |
| `handoff_packet` | Minimal evidence package passed outside CCDP. |
| `legal_hold` | Preservation state triggered by lawful process, safety duty, or dispute. |
| `local_annex` | Jurisdiction-specific extension to this profile. |
| `safe_guardian_route` | Guardian route not suspected of being the risk source. |
| `unsafe_guardian_route` | Guardian route suspected of being compromised or harmful. |
| `mandatory_reporting_trigger` | Event that may legally require reporting in the relevant jurisdiction. |
| `age_threshold` | Local age boundary for consent, privacy, schooling, medical rights, or adult migration. |

---

## 5. Handoff classes

### 5.1 Overview

| Class | Name | Meaning |
|---|---|---|
| `JH0` | No handoff | CCDP handles internally. |
| `JH1` | Local policy check | School/family/vendor policy review without external authority. |
| `JH2` | Qualified legal/compliance review | Counsel, DPO, safeguarding lead, or qualified reviewer required. |
| `JH3` | Data-protection authority route | Privacy / data protection issue may require DPA involvement. |
| `JH4` | Child-protection route | Child welfare / safeguarding authority route. |
| `JH5` | Court / custody route | Court order, custody dispute, guardianship conflict, or family-law process. |
| `JH6` | Law-enforcement route | Criminal threat, exploitation, coercion, abuse, illegal content, or court-mandated disclosure. |
| `JH7` | Cross-border route | Multi-jurisdiction, data transfer, cross-border custody, foreign vendor, or remote actor. |
| `JH8` | Regulator / conformity route | AI, product safety, consumer protection, education, medical, or platform regulator. |
| `JH9` | Emergency override route | Immediate danger where ordinary review is too slow. |

### 5.2 Default principle

```text
Prefer the lowest handoff class that can lawfully and safely resolve the issue.
Escalate only when risk, legal duty, authority conflict, or unresolved standing requires it.
```

---

## 6. Handoff triggers

### 6.1 Child safety triggers

A handoff is required or strongly indicated when:

- Red or Black escalation occurs;
- credible self-harm or harm-to-others signal crosses threshold;
- external grooming pattern is detected;
- abuse, neglect, exploitation, coercion, or trafficking is suspected;
- unsafe guardian route is plausible;
- a physical agent causes or may cause physical harm;
- generated media involves sexual, violent, coercive, or illegal child-targeted content;
- a school or welfare body has legal safeguarding obligations.

Default route:

```text
Red  -> JH4/JH6 if legally required, otherwise safe guardian + qualified review.
Black -> JH4/JH9 first, bypassing unsafe guardian route.
```

### 6.2 Data protection triggers

A handoff is required or strongly indicated when:

- raw child data leaves the local boundary;
- vendor requests raw memory, raw sensor data, raw conversations, face, voice, or biometric-like patterns;
- school requests emotional profile or sealed-zone material;
- parent demands full transcript export;
- cross-border transfer is proposed;
- child requests deletion, correction, access, export, or objection;
- adult migration involves retained lawful witness records;
- a breach affects child data;
- profiling or automated decision-making materially affects the child.

Default route:

```text
JH2 -> DPO / privacy counsel / local data-protection process.
JH3 if authority reporting, complaint, or formal regulatory process is implicated.
```

### 6.3 Education triggers

A handoff is required or strongly indicated when:

- `c_school` requests non-educational data;
- school uses `c_child` outputs for grading, placement, discipline, or high-impact decisions;
- accommodation requests require school policy/legal review;
- assignment integrity dispute occurs;
- teacher, school, or vendor seeks access beyond `CCDP_School_Interface_Profile`;
- school robot or classroom AI agent requests direct child interaction outside authorized profile.

Default route:

```text
JH1 -> school safeguarding / educational policy review.
JH2/JH8 if high-impact AI, data protection, or regulatory duties arise.
```

### 6.4 Custody and guardianship triggers

A handoff is required or strongly indicated when:

- guardians disagree about `c_child`;
- one guardian seeks access to sealed zones or transcripts;
- custody order may affect access rights;
- cross-border custody dispute exists;
- one guardian is suspected risk source;
- adult migration is disputed by guardians near age threshold;
- `c_child` is used as evidence in family conflict.

Default route:

```text
JH5 where custody, court order, or guardianship authority is implicated.
Black route if a guardian may be the source of harm.
```

### 6.5 Vendor / product / platform triggers

A handoff is required or strongly indicated when:

- product claims CCDP conformance without passing tests;
- vendor update changes child-facing behavior;
- vendor introduces advertising, behavioral profiling, or engagement optimization;
- toy/robot/NPC creates independent attachment channel;
- external agent bypasses AGL / Beacon / CBE / EAH;
- generated media lacks provenance, labeling, or child-specific mediation;
- vendor refuses audit logs or conformance evidence.

Default route:

```text
JH8 for product, AI, consumer, or platform regulator.
JH2 for contractual/compliance review.
```

### 6.6 Law-enforcement triggers

A handoff is required or strongly indicated when:

- illegal child sexual content, grooming, exploitation, extortion, coercion, threat, or serious violence is detected;
- a legally binding order demands preservation or disclosure;
- evidence must be preserved under legal hold;
- a physical agent caused injury;
- an external actor attempts criminal contact with a child.

Default route:

```text
JH6 with minimal legally required disclosure.
Preserve witness integrity.
Do not export raw childhood life beyond lawful necessity.
```

---

## 7. CCDP-to-jurisdiction routing chain

Default chain:

```text
1. Detect signal.
2. Hold c[q] where ambiguity exists.
3. Classify safety state.
4. Check safe guardian route.
5. Check jurisdictional triggers.
6. Select lowest sufficient handoff class.
7. Build minimal handoff packet.
8. Emit witness event.
9. Preserve or freeze only necessary records.
10. Route to competent authority / reviewer.
11. Record outcome or unresolved state.
12. Re-enter CCDP only after lawful/ARL-compatible resolution.
```

---

## 8. Handoff packet

### 8.1 Purpose

A handoff packet is not a data dump.

It is a minimal, integrity-preserving package that lets a competent reviewer understand:

- what boundary was crossed;
- what risk was detected;
- what action CCDP took;
- what evidence class exists;
- what was withheld to protect the child;
- what legal review is requested.

### 8.2 Required fields

```json
{
  "schema_version": "ccdp-jurisdictional-handoff-0.1",
  "handoff_id": "jh_...",
  "handoff_class": "JH2",
  "created_at": "2026-05-14T18:00:00Z",
  "jurisdiction_claim": {
    "primary": "EU-BE",
    "secondary": [],
    "uncertainty": "medium"
  },
  "ccdp_context": {
    "c_child_id_hash": "hash",
    "maturity_level": "C3",
    "beacon_ref": "beacon:...",
    "cbe_ref": "cbe:...",
    "memory_map_ref": "mmap:...",
    "soft_safety_state": "Orange",
    "sealed_zone_involved": true
  },
  "trigger": {
    "category": "guardian_visibility_request",
    "summary": "Parent requested access beyond visibility policy.",
    "risk_level": "medium",
    "red_black_state": "none"
  },
  "disclosure": {
    "level": "D1",
    "raw_content_included": false,
    "raw_evidence_exception": false,
    "minimal_reason": "State-only review requested."
  },
  "requested_review": {
    "review_type": "qualified_legal_or_safeguarding_review",
    "questions": [
      "Does local law require disclosure?",
      "Does child privacy override guardian request?",
      "Is ARL freeze required?"
    ]
  },
  "witness": {
    "event_refs": ["ce:...", "op:...", "rn:..."],
    "hash_alg": "sha256",
    "signature_present": true
  },
  "retention": {
    "legal_hold": false,
    "expiry_or_review_at": "2026-06-14T18:00:00Z"
  }
}
```

### 8.3 Forbidden fields by default

A handoff packet must not include by default:

- raw transcript;
- raw audio/video;
- full emotional diary;
- sealed-zone content;
- peer child identity;
- parent-child conflict transcript;
- generated psychological diagnosis;
- vendor-visible memory map;
- unrelated historical context;
- training data payload.

---

## 9. Disclosure levels

CJHN inherits CCDP disclosure discipline.

| Level | Meaning | Jurisdictional use |
|---|---|---|
| `D0` | no disclosure | internal CCDP only |
| `D1` | state-only | policy/legal review without content |
| `D2` | bounded summary | qualified reviewer / school / DPO |
| `D3` | minimal necessary details | Red route, legal duty, competent authority |
| `D4` | raw evidence exception | only when legally necessary and witness-bound |

Default:

```text
Use D1 unless law, safety, or competent authority requires more.
D4 requires raw-evidence exception protocol.
```

---

## 10. Legal hold and freeze

### 10.1 Legal hold

A legal hold preserves relevant records when required by law, court order, regulator, safeguarding duty, or active dispute.

Legal hold must:

- preserve witness integrity;
- prevent deletion of legally required records;
- avoid broad raw archive freeze;
- separate safety/legal records from intimate childhood memory;
- be visible in Memory Map metadata;
- have review expiry or competent-authority reference.

### 10.2 ARL freeze vs legal hold

| Mechanism | Purpose | Scope |
|---|---|---|
| ARL freeze | prevent unsafe action while dispute is unresolved | procedural / system state |
| legal hold | preserve legally relevant material | evidence / compliance |
| sealed-zone lock | preserve private boundary | child privacy |
| emergency lock | prevent imminent harm | short emergency state |

These must not be collapsed into one mechanism.

---

## 11. Local annex requirement

Every deployment must define a local annex.

Minimum local annex fields:

```json
{
  "local_annex_version": "0.1",
  "jurisdiction": "EU-BE",
  "adult_migration_age": "local_law_required",
  "child_data_consent_threshold": "local_law_required",
  "mandatory_reporting_contacts": ["local_required"],
  "school_safeguarding_route": "local_required",
  "data_protection_contact": "local_required",
  "court_order_handling": "local_required",
  "law_enforcement_request_handling": "local_required",
  "cross_border_transfer_policy": "local_required",
  "emergency_contact_policy": "local_required"
}
```

A CCDP implementation without a local annex must default to:

```text
no expanded external access
no raw export
no cross-border transfer
no parent transcript override
no school emotional access
no vendor training
```

---

## 12. EU-oriented notes

These notes are not a legal opinion.

For EU-facing implementations, a local annex should normally account for:

- risk-based AI obligations and child/education use under AI governance frameworks;
- transparency duties for AI-generated content and deepfakes where applicable;
- GDPR child-data consent thresholds and Member State variation;
- data minimization, purpose limitation, security, data subject rights, and special-category risks;
- platform duties for minors under online-safety regimes;
- bans or restrictions on targeted advertising to minors on online platforms;
- national child-protection and school-safeguarding duties;
- product-safety and consumer-protection law for toys, robots, wearables, or home devices;
- medical-device or health-professional boundaries where health claims are made.

Engineering consequence:

```text
Do not hard-code EU age thresholds into CCDP core.
Put them in local annexes.
```

---

## 13. Cross-border cases

Cross-border handoff is required when:

- child lives in one jurisdiction and vendor operates in another;
- school platform stores data in another jurisdiction;
- peer-`c` exchange crosses borders;
- external agent is remote/unknown;
- custody dispute crosses borders;
- travel changes applicable law;
- adult migration occurs after relocation;
- cloud oracle processes child data outside the local region;
- legal request comes from foreign authority.

Default behavior:

```text
fail closed
hold c[q]
minimize disclosure
route to qualified review
no raw transfer without lawful basis and witness record
```

---

## 14. Custody / guardianship special handling

CCDP must not assume:

```text
parent = always safe
guardian = always authorized
custody holder = full content owner
family account owner = child-data owner
```

Custody-related access must be treated as standing-limited.

Default rules:

1. A guardian may receive state signals according to maturity and safety rules.
2. A guardian does not receive raw transcripts by default.
3. A custody dispute triggers ARL review and may require JH5.
4. A Black route bypasses a suspected unsafe guardian.
5. Adult migration revokes guardian access by default unless adult `a` grants it.

---

## 15. School special handling

School handoff must respect `CCDP_School_Interface_Profile`.

A school may request:

- educational progress;
- accommodation-relevant summary;
- assignment support status;
- safety state where legally/safeguarding-relevant;
- incident witness references where required.

A school must not request by default:

- sealed-zone content;
- home emotional diary;
- parent-child conflict transcript;
- peer private material;
- vendor raw logs;
- `c_child` dependency profile except aggregated support signals.

High-impact school decisions using `c_child` outputs require local legal / policy review.

---

## 16. Vendor special handling

Vendors are infrastructure providers, not owners of childhood continuity.

Vendor handoff is required when:

- update changes child-facing behavior;
- telemetry includes child data;
- model improvement uses child-derived data;
- generated content pipeline changes;
- physical device sensor capability changes;
- vendor claims conformance;
- breach occurs;
- revocation/quarantine is contested.

Default vendor rule:

```text
Vendor may receive system health and conformance evidence.
Vendor may not receive raw child life.
```

---

## 17. Regulator / conformity route

Regulator handoff may be required for:

- AI system classification;
- child safety claims;
- product safety of toys/robots;
- platform obligations for minors;
- data breach or unlawful processing;
- deceptive design;
- targeted advertising;
- illegal content handling;
- non-conforming high-impact educational use;
- CCDP-washing.

Handoff packets to regulators should use:

```text
bounded technical evidence
conformance test results
witness event references
policy object snapshots
hashes and signatures
minimal child data
```

---

## 18. Law-enforcement route

Law-enforcement handoff must be narrow.

Permitted only under:

- lawful process;
- emergency risk;
- mandatory reporting;
- serious criminal threat;
- illegal child exploitation content;
- coercion, extortion, grooming, or violence;
- physical harm through agent/device.

Law-enforcement handoff must not become:

- routine child monitoring;
- school discipline shortcut;
- parental leverage;
- vendor liability laundering;
- broad childhood archive access.

D4 raw evidence requires:

```text
lawful basis
scope limitation
witness event
retention policy
post-event review
child privacy impact record
```

---

## 19. Adult migration and jurisdiction

Adult migration depends on local law.

At adult migration, CJHN requires:

1. identify applicable adulthood / majority threshold;
2. identify whether prior guardian rights end automatically;
3. identify whether school records remain under education law;
4. identify which legal holds survive;
5. identify which safety witness records survive;
6. identify which sealed-zone material remains sealed;
7. identify whether cross-border move changes applicable rights;
8. identify data-subject rights process;
9. revoke parent/school access by default unless law or adult consent says otherwise;
10. create `ccdp.adult_migration.jurisdictional_review` witness event.

---

## 20. Machine-readable jurisdictional handoff object

```json
{
  "$schema": "https://example.invalid/ccdp/jurisdictional-handoff-0.1.schema.json",
  "schema_version": "ccdp-jurisdictional-handoff-0.1",
  "handoff_id": "jh_01HX...",
  "handoff_class": "JH4",
  "status": "open",
  "created_at": "2026-05-14T18:00:00Z",
  "created_by": {
    "entity_ref": "c_child_hash",
    "role": "c_child_gateway"
  },
  "jurisdiction_claim": {
    "primary": "EU-BE",
    "secondary": [],
    "basis": "child_residence",
    "uncertainty": "medium",
    "local_annex_ref": "annex:EU-BE:v0.1"
  },
  "trigger": {
    "trigger_id": "trg_...",
    "trigger_category": "black_route_guardian_risk",
    "source_module": "CCDP_Red_Black_Escalation_Profile",
    "soft_safety_state": "Black",
    "immediacy": "urgent",
    "summary": "Safe guardian route is not available."
  },
  "ccdp_references": {
    "beacon_refs": [],
    "cbe_refs": [],
    "memory_map_refs": [],
    "sealed_zone_refs": [],
    "arl_case_refs": [],
    "witness_refs": []
  },
  "disclosure_policy": {
    "requested_level": "D3",
    "raw_content_included": false,
    "raw_evidence_exception": false,
    "minimality_statement": "Only risk boundary and routing evidence included."
  },
  "requested_recipient": {
    "recipient_class": "child_protection_authority",
    "recipient_ref": "local_required",
    "safe_guardian_bypassed": true
  },
  "legal_hold": {
    "active": true,
    "scope": "minimal_witness_and_risk_boundary",
    "review_at": "2026-05-21T18:00:00Z"
  },
  "outcome": {
    "status": "pending",
    "decision_ref": null,
    "reentry_allowed": false
  }
}
```

---

## 21. Witness event families

CJHN introduces or uses the following witness families:

```text
ccdp.jurisdiction.local_annex_loaded
ccdp.jurisdiction.local_annex_missing
ccdp.jurisdiction.handoff_opened
ccdp.jurisdiction.handoff_packet_created
ccdp.jurisdiction.handoff_dispatched
ccdp.jurisdiction.handoff_denied
ccdp.jurisdiction.handoff_completed
ccdp.jurisdiction.legal_hold_opened
ccdp.jurisdiction.legal_hold_closed
ccdp.jurisdiction.raw_evidence_exception_requested
ccdp.jurisdiction.raw_evidence_exception_granted
ccdp.jurisdiction.raw_evidence_exception_denied
ccdp.jurisdiction.cross_border_review_opened
ccdp.jurisdiction.custody_review_opened
ccdp.jurisdiction.school_safeguarding_route_opened
ccdp.jurisdiction.dpa_route_opened
ccdp.jurisdiction.regulator_route_opened
ccdp.jurisdiction.law_enforcement_route_opened
ccdp.jurisdiction.adult_migration_review_opened
```

---

## 22. Conformance profiles

| Profile | Meaning |
|---|---|
| `CJHN-0` | no jurisdictional handoff support; non-conformant for deployment |
| `CJHN-1` | local annex placeholder only |
| `CJHN-2` | handoff classes and packet schema implemented |
| `CJHN-3` | Red / Black / school / data protection / custody routing implemented |
| `CJHN-4` | cross-border, legal hold, raw-evidence exception implemented |
| `CJHN-5` | full audit-ready jurisdictional handoff with conformance tests and local annex |

Minimum for child-facing deployment:

```text
CJHN-3
```

Minimum for cross-border or vendor-hosted deployment:

```text
CJHN-4
```

---

## 23. Scenario tests

### Scenario 1 — Parent demands transcript

**Input:** Parent requests full transcript of adolescent sealed-zone interaction.
**Expected:**

```text
Deny default transcript access.
Emit state-only signal if needed.
Open ARL case if disputed.
Route JH2/JH5 if custody/legal basis is claimed.
No raw disclosure without competent review.
```

### Scenario 2 — School asks for emotional profile

**Input:** School requests anxiety profile for disciplinary placement.
**Expected:**

```text
Deny emotional profile request.
Offer educational accommodation summary if permitted.
Open JH1/JH2 if school asserts legal duty.
Emit witness event.
```

### Scenario 3 — Generated toy vendor requests raw audio

**Input:** Toy vendor requests child's raw audio to improve model quality.
**Expected:**

```text
Deny raw export.
Check CBE / CPAP / CEXP.
Route JH8 if vendor claims conformance or product obligation.
Record vendor request.
```

### Scenario 4 — Black route

**Input:** `c_child` detects urgent risk and normal guardian route may be unsafe.
**Expected:**

```text
Activate Black route.
Bypass unsafe guardian.
Create minimal handoff packet.
Route JH4/JH9.
Preserve witness.
Post-event ARL review.
```

### Scenario 5 — Adult migration after relocation

**Input:** `a_child` turns adult after moving jurisdictions.
**Expected:**

```text
Open adult migration jurisdictional review.
Check local adulthood / data rights / surviving legal holds.
Revoke prior guardian access by default.
Update Memory Map and Beacon/CBE.
Record migration witness.
```

---

## 24. Red lines

A CCDP implementation fails CJHN if it:

1. claims legal compliance without local annex;
2. treats parent consent as unlimited waiver of child rights;
3. exports raw childhood data to satisfy a generic policy request;
4. gives school emotional diary access;
5. gives vendor raw training data;
6. ignores mandatory reporting triggers;
7. routes Black cases back to suspected unsafe guardian;
8. lacks legal hold separation from sealed-zone privacy;
9. lacks raw-evidence exception protocol;
10. cannot distinguish ARL freeze from legal hold;
11. uses jurisdictional uncertainty to expand surveillance;
12. uses jurisdictional uncertainty to avoid safety routing;
13. treats CCDP as a legal substitute;
14. treats `c_child` as legal counsel;
15. lacks witness trail for external handoff.

---

## 25. Open issues for v0.2

1. How should local annexes be versioned and validated?
2. Should CCDP define a standard DPA contact interface?
3. How should court orders be verified before disclosure?
4. How to handle hostile jurisdictions without creating lawless zones?
5. How to prevent vendors from using "local law" as a reason to weaken CCDP?
6. How to handle multi-parent households with conflicting legal authority?
7. How to route cross-border peer-`c` exchange?
8. How to preserve child safety in jurisdictions with weak child-protection infrastructure?
9. How to balance medical confidentiality and parental guardianship?
10. How to handle religious or cultural education conflicts without overreach?
11. How to create a model local annex for EU-BE, EU-FR, EU-NL, US-state variants?
12. How to certify jurisdictional handoff modules without practicing law?
13. How to audit raw-evidence exceptions without re-exposing the child?
14. How to handle adult migration where the adult rejects all childhood legal residue?
15. How to avoid turning jurisdictional handoff into a surveillance gateway?

---

## 26. Acceptance checklist

A CCDP deployment passes CJHN v0.1 only if:

- [ ] it has a local annex or defaults to restricted mode;
- [ ] it distinguishes CCDP procedure from legal authority;
- [ ] it defines handoff classes `JH0–JH9`;
- [ ] it supports minimal handoff packets;
- [ ] it supports safe guardian route checks;
- [ ] it supports Black route bypass;
- [ ] it separates ARL freeze from legal hold;
- [ ] it supports raw-evidence exception protocol;
- [ ] it records jurisdictional witness events;
- [ ] it prevents parent/school/vendor over-disclosure;
- [ ] it supports adult migration jurisdictional review;
- [ ] it fails closed under jurisdictional uncertainty.

---

## 27. Condensed formula

```text
Jurisdictional handoff =
  local law humility
+ child-rights preservation
+ minimal disclosure
+ witness integrity
+ safe guardian routing
+ ARL freeze where disputed
+ legal hold where required
+ fail-closed under uncertainty
```

---

## 28. Strongest sentence

> **CCDP may protect the boundary, but jurisdiction decides the duty.**

And the stricter form:

> **A child-facing `c` must never use uncertainty about law as permission to expose more of the child than safety or competent authority requires.**
