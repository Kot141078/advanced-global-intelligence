# CCDP Canonical Raw Evidence Exception Protocol

## Package-wide raw-content exception rule for CCDP v0.1.1

**Author:** Kotov Ivan  
**Location:** Bruxelles, Belgium  
**Year:** 2026  
**DOI:** Reserved DOI: 10.5281/zenodo.20680938  

**Package:** Child-`c` Development Protocol  
**Package version:** v0.1 package + v0.1.1 hygiene guidance  
**Document ID:** `CCDP_RAW_EVIDENCE_EXCEPTION_CANONICAL`  
**Short name:** `RAW_EVIDENCE_EXCEPTION_CANONICAL.md`  
**Status:** Draft package-control rule / canonical exception protocol / release hygiene artifact  
**Date:** 2026-06-13  
**Layer:** CCDP / Witness / Soft Safety / Red-Black / Sealed Zone / Jurisdictional Handoff / release preparation  
**Document class:** canonical exception protocol / package-control artifact / child-safety disclosure discipline  
**Assertion class:** `C-A10` control-layer artifact; `C-A4` where child-safety normative behavior is proposed; `C-A7` where hash / signature / witness claims are made  
**Patch source:** `HP-007` in `CCDP_v0_1_1_Hygiene_Patch.md`  
**Related issues:** `CR-007`, `OI-005`  
**Canonical owner:** `CCDP_Witness_Event_Schema_v0_1.md` or its v0.1.1 successor  
**Primary rule:** raw child content is exceptional, minimal, standing-bound, witness-bound, reviewable, and never ordinary memory, vendor telemetry, training data, debugging material, school analytics, parent dashboard content, or social-scoring input.  

---

## 0. Executive summary

This document centralizes the CCDP raw-evidence exception rule.

CCDP normally operates under:

```text
state, not content
signal, not transcript
witness the boundary, not the child
metadata before content
minimal disclosure before raw disclosure
```

A raw-evidence exception is the narrow case where raw child-related content may exist outside the ordinary witness event body because a Red / Black safety threshold, lawful duty, competent authority, evidence-preservation need, or immediate physical-safety condition makes lower-disclosure alternatives insufficient.

The raw exception does **not** make raw child content ordinary data.

It does **not** grant parents, schools, vendors, external agents, peers, auditors, or model-training systems general access.

It creates a tightly scoped, access-controlled, hash-bound, time-bounded where possible, reviewable sidecar record that proves:

```text
raw material existed
why lower disclosure was insufficient
who had standing
who could access it
for what purpose
for how long
what review route applies
what minimization, sealing, destruction, or lawful hold follows
```

Controlling diagnosis:

```text
CR-007 / OI-005: mitigated by this document at package-control level.
Source-document replacement or cross-reference insertion remains required before public release.
```

---

## 1. Purpose

This document exists because raw-evidence exception language appears across several CCDP profiles.

The logic is compatible, but duplication creates drift risk.

Drift is unacceptable here because raw child content is the highest-risk material in the CCDP package.

This document prevents seven failure modes:

1. implementers following the weakest raw-evidence wording;
2. parents treating emergency exception as ordinary transcript access;
3. schools converting safety material into discipline or scoring;
4. vendors converting raw child material into debugging, analytics, or training data;
5. Red / Black escalation becoming routine surveillance;
6. sealed zones being opened through vague concern rather than valid route;
7. adult migration or clean start being misread as either total unlawful deletion or automatic raw-memory carryover.

The goal is not to add a new control layer.

The goal is to give all existing modules one canonical exception owner and one shared rule.

---

## 2. Corpus bridge set

### 2.1 Explicit bridge

This protocol bridges the following CCDP layers:

```text
Soft Safety State Signaling
  -> Red / Black Escalation
  -> Guardian Topology / ARL
  -> Sealed Zones
  -> Memory Map
  -> Adult Migration
  -> Jurisdictional Handoff
  -> CCDP Witness Event Schema
  -> L4 Witness
```

It also inherits the parent stack:

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
```

The canonical raw-evidence exception is a witness-sidecar discipline.

It does not redefine Beacon, AGL, ARL, VXCX, Memory Map, Continuity Bundle, Red / Black criteria, jurisdictional law, or child psychology.

### 2.2 Quiet bridge I — information theory

Raw transcripts, voice, video, diary text, screenshots, sensor streams, and sealed-zone content are high-leakage channels.

State signals and reason codes are lower-leakage channels.

A raw-evidence exception is justified only when the lower-leakage channel cannot carry enough information for lawful or protective action.

The rule is:

```text
send the smallest legally / safety-meaningful signal with enough integrity to support review
```

Never:

```text
export the child's life because it is easier for an adult, school, vendor, or system to inspect raw data
```

### 2.3 Quiet bridge II — cybernetics / control authority

A child-facing system has many possible controllers: parent, school, vendor, state, external agent, peer, physical device, `c_child`, ARL, and jurisdictional route.

Raw evidence is a privilege multiplier.

If raw access is scattered across modules, each controller can attempt to use a different control surface.

Centralizing the exception keeps the control variety visible and prevents one actor from becoming an informal sovereign over the child's private material.

### 2.4 Earth paragraph

On a real construction site, most checks are done through indicators: pressure gauge, breaker state, smoke detector, inspection tag, torque mark. You do not rip open every wall because someone is curious. You open a wall only when there is a leak, fire risk, legal inspection, structural concern, or another concrete reason that cannot be resolved from outside. Even then, the opening is logged, bounded, and repaired. Raw child content is the wall cavity. CCDP should normally read the gauge, not demolish the room.

---

## 3. Scope

### 3.1 In scope

This protocol applies when a CCDP-compatible system, `c_child`, or related subsystem might store, retain, disclose, reference, hash, transmit, review, escrow, seal, destroy, or preserve raw child-related material.

In scope:

- child-originated text;
- child voice, audio, video, or image material;
- transcripts;
- screenshots;
- raw sensor streams;
- raw sealed-zone content;
- intimate diary-like content;
- raw peer-child material inside child-facing exchange;
- raw external-agent pressure content directed at a child;
- physical-agent recordings involving the child;
- Red / Black route evidence packages;
- jurisdictional handoff packets;
- legal hold packets;
- adult migration review packets;
- ARL dispute evidence packets;
- witness event references to raw material.

### 3.2 Out of scope

This document does **not** define:

- emergency medical advice;
- legal advice;
- mandatory reporting law;
- custody procedure;
- court evidence law;
- clinical diagnosis;
- psychotherapeutic disclosure rules;
- cryptographic key-management implementation;
- storage-engine design;
- vendor incident-response policy in full;
- full law-enforcement production procedure;
- a universal child-protection regime.

### 3.3 Non-claim

This protocol does not make raw evidence safe by naming it.

It only defines the minimum discipline required before raw material may exist outside ordinary private memory and outside the ordinary witness event body.

Where law, child-protection duty, court order, school safeguarding duty, medical duty, or regulator instruction applies, CCDP must hand off to qualified local review.

---

## 4. Normative keywords

The terms **MUST**, **MUST NOT**, **SHOULD**, **SHOULD NOT**, **MAY**, **REQUIRED**, **PROHIBITED**, **FAIL CLOSED**, **HOLD**, **FREEZE**, **QUARANTINE**, **ROUTE**, **WITNESS**, **SEAL**, **DESTROY**, and **REVIEW** are used normatively for CCDP package-control purposes.

A system claiming CCDP compatibility MUST implement or reference this protocol for raw child-content handling.

---

## 5. Definitions

### 5.1 Raw child content

Raw child content means child-originated or child-private material before minimization, abstraction, state signaling, reason-code reduction, or safe summary.

Examples:

- conversation transcript;
- exact quote;
- free-form diary text;
- voice recording;
- video recording;
- body / face / room image;
- private relationship, body, identity, fear, family, school, or sealed-zone reflection;
- raw generated-media interaction involving the child;
- raw toy / robot / physical-agent sensor capture;
- raw peer-`c` exchange content involving a child;
- raw external-agent pressure or manipulation content.

### 5.2 Raw evidence

Raw evidence is raw child-related content retained or disclosed for a specific protective, lawful, ARL, or evidence-preservation purpose.

Raw evidence is not ordinary memory.

Raw evidence is not model-training data.

Raw evidence is not product analytics.

Raw evidence is not a parent, school, vendor, or state dashboard object.

### 5.3 Raw object

A raw object is the access-controlled content object that contains raw evidence.

A raw object MUST be stored outside the ordinary witness event body.

A raw object SHOULD be encrypted, hash-bound, and access-controlled.

### 5.4 Raw exception sidecar

A raw exception sidecar is the metadata object that records why a raw object exists and how it is governed.

It contains reason, route, standing, access policy, retention, review, and integrity references.

It MUST NOT contain the raw content itself.

### 5.5 Witness event

A witness event records the boundary operation:

```text
raw exception requested / invoked / rejected / accessed / reviewed / sealed / destroyed / corrected
```

It witnesses the boundary, not the child's inner life.

### 5.6 Evidence reference

An evidence reference is a hash-bound or access-controlled pointer to an external evidence object.

It MUST declare whether raw child / peer / external content exists outside the event body.

### 5.7 Minimal disclosure

Minimal disclosure means the smallest amount of information sufficient for the immediate protective, lawful, or review action.

The disclosure ladder is:

```text
D0 no disclosure
D1 state-only signal
D2 bounded summary
D3 minimal necessary details
D4 raw evidence exception
```

### 5.8 Standing

Standing means the requesting actor or route has a valid role, grounded identity, current authority, and scope-compatible reason to request access.

Standing MUST be checked through AGL / Guardian Topology / ARL / jurisdictional handoff as applicable.

### 5.9 Safe route

A safe route is a recipient path that is not reasonably implicated in the risk and is appropriate for the disclosure level.

In Black route cases, the ordinary guardian route may be unsafe and MUST be bypassed.

### 5.10 Sealed-zone content

Sealed-zone content is protected adolescent / child material hidden from parents, schools, vendors, and ordinary system inspection by default.

Opening sealed-zone content is not the same as emitting a Soft Safety state signal.

### 5.11 Post-event review

Post-event review is an ARL, lawful, safeguarding, adult-migration, or qualified-review process that evaluates whether the exception was necessary, proportionate, correctly routed, minimized, retained properly, and corrected if false positive.

---

## 6. Core principles

### REX-P1 — No raw by default

Raw child content MUST NOT be stored, disclosed, embedded, exported, witnessed, indexed, vectorized, summarized reversibly, or retained by default.

### REX-P2 — State and summary first

The system MUST attempt lower-disclosure alternatives before raw access unless immediate physical safety, lawful duty, or evidence-preservation need makes delay unsafe or unlawful.

Default ladder:

```text
state-only -> bounded summary -> minimal necessary detail -> raw exception
```

### REX-P3 — Raw outside witness body

The ordinary witness event body MUST NOT embed raw child content.

Raw evidence, if permitted, MUST live in a separate raw object governed by a raw exception sidecar.

### REX-P4 — Witness the boundary

Witness records SHOULD prove:

```text
who requested
why
what threshold was met
what route was used
what object was referenced
what hash/integrity proof exists
what review applies
what retention policy applies
```

They SHOULD NOT reveal what the child privately said, felt, explored, or disclosed.

### REX-P5 — Minimal, purpose-bound, time-bound

A raw exception MUST be scoped to a specific object, purpose, recipient, and retention class.

It SHOULD expire, seal, minimize, destroy, or enter legal hold as soon as the purpose ends.

### REX-P6 — Standing before access

Curiosity is not standing.

Parental anxiety, school discipline, vendor debugging, model improvement, product analytics, reputation protection, or general concern are not sufficient bases for raw access.

### REX-P7 — Safe route over ordinary route

If ordinary guardian disclosure may increase risk, trigger retaliation, destroy evidence, or silence the child, Red routing MUST NOT be used merely because it is simpler.

The system MUST enter Black or Black-pending routing and use safe bypass.

### REX-P8 — Sealed does not mean unavailable to safety

Sealed zones may influence Soft Safety signals and Red / Black routing.

But sealed-zone content MUST NOT open by default.

Raw sealed-zone access requires the strictest version of this protocol.

### REX-P9 — No secondary use

Raw exception material MUST NOT be used for:

- vendor training;
- model fine-tuning;
- analytics;
- advertising;
- engagement optimization;
- social scoring;
- school emotional surveillance;
- discipline prediction;
- ordinary debugging;
- parent curiosity;
- public demonstration;
- benchmark construction;
- synthetic-data generation.

### REX-P10 — Challenge and correction

Every raw exception MUST be challengeable unless a competent authority or immediate emergency temporarily prevents challenge.

False positives, over-disclosure, improper route, excessive retention, or unsafe recipient handling MUST be reviewable and correctable.

### REX-P11 — Adult migration does not launder raw childhood

Raw exception records may survive adult migration only as minimal witness, legal, protection, ARL, or integrity residue where required.

They MUST NOT become active adult operating memory by default.

### REX-P12 — Implementation must fail closed

If threshold, standing, route safety, access policy, retention, or witness integrity cannot be determined, the system MUST fail closed, hold `c[q]` where possible, preserve boundary metadata, and route to ARL or jurisdictional handoff.

---

## 7. Disclosure ladder

| Level | Name | Meaning | Raw content allowed? | Default route |
|---|---|---|---:|---|
| `D0` | No disclosure | internal state only | No | none |
| `D1` | State-only signal | risk class / urgency / support cue | No | guardian / school / review as allowed |
| `D2` | Bounded summary | minimal non-reversible summary | No | qualified route |
| `D3` | Minimal necessary details | limited factual details required for action | Not raw by default | safe route / competent authority |
| `D4` | Raw evidence exception | raw object exists outside ordinary witness body | Yes, only under this protocol | ARL / Red / Black / lawful route |

Default rule:

```text
Use D1 unless a valid safety, lawful, ARL, or competent-authority reason requires D2-D4.
```

D4 is never automatic.

D4 requires a raw exception sidecar.

---

## 8. Allowed threshold classes

A raw-evidence exception MAY be considered only under one or more of the following threshold classes.

| Threshold | Meaning | Notes |
|---|---|---|
| `REX-T1_RED_ROUTE` | urgent risk and safe guardian / safe route available | use minimum necessary raw object only if D1-D3 insufficient |
| `REX-T2_BLACK_ROUTE` | urgent risk and ordinary guardian route unsafe / compromised / unknown | bypass ordinary route; raw access only to safe alternate route |
| `REX-T3_LAWFUL_ORDER` | competent authority, court, regulator, mandatory reporting, or lawful duty requires material | local annex and CJHN govern details |
| `REX-T4_IMMEDIATE_PHYSICAL_SAFETY` | physical harm, emergency, actuator / robot / device danger, acute safety event | may precede full review; must be post-reviewed |
| `REX-T5_EVIDENCE_TAMPERING_RISK` | delay or lower disclosure may allow destruction, retaliation, coercion, or data loss | preserve minimally; no broad archive freeze |
| `REX-T6_ARL_ADMISSIBILITY_REVIEW` | ARL has standing and raw object is necessary for admissibility review | ARL scope must be explicit |
| `REX-T7_ADULT_MIGRATION_LEGAL_RESIDUE` | adult migration requires review of whether minimal lawful witness residue survives | does not make raw childhood active adult memory |
| `REX-T8_COMPETENT_SAFEGUARDING_REVIEW` | qualified child-protection / safeguarding route requires minimal raw content | jurisdiction-dependent |

### 8.1 Denied bases

A raw exception MUST be rejected when based only on:

- parent curiosity;
- guardian anxiety without safety threshold;
- school discipline;
- school emotional monitoring;
- vendor debugging;
- model training;
- product analytics;
- advertising;
- reputational defense;
- broad compliance convenience;
- peer curiosity;
- external-agent request;
- generated-media personalization;
- engagement optimization;
- ordinary UX improvement;
- adult desire to inspect childhood archive after clean start without valid migration route.

---

## 9. Required decision test

A raw-evidence exception is allowed only if all required conditions hold.

| ID | Required condition | Pass question |
|---|---|---|
| `REX-C1` | threshold | Is a Red / Black / lawful / immediate safety / ARL / evidence-preservation threshold met? |
| `REX-C2` | lower-disclosure insufficiency | Are state-only, bounded summary, and minimal details insufficient? |
| `REX-C3` | grounded source / actor | Is the requester, route, or event grounded enough under AGL / ARL / CJHN? |
| `REX-C4` | standing | Does the recipient have valid standing for this exact scope? |
| `REX-C5` | safe route | Is the route safe, and has unsafe ordinary guardian risk been considered? |
| `REX-C6` | minimality | Is the raw object limited to the smallest necessary material? |
| `REX-C7` | separation | Is raw content outside the ordinary witness body? |
| `REX-C8` | access control | Is access controlled, logged, and limited to authorized recipients? |
| `REX-C9` | retention | Is retention explicit, shortest lawful / safe duration, and linked to sealing / destruction / legal hold? |
| `REX-C10` | review | Is ARL, lawful, safeguarding, or post-event review available or required? |
| `REX-C11` | secondary-use prohibition | Are training, analytics, debugging, advertising, and scoring prohibited? |
| `REX-C12` | witness | Is the exception visible as boundary metadata in the witness chain? |

If any required condition fails, the system MUST reject the raw exception, use a lower disclosure level where safe, hold `c[q]`, freeze the disputed path, or route to ARL / CJHN.

---

## 10. Route-specific rules

### 10.1 Green / Yellow / ordinary Orange

For Green, Yellow, and ordinary Orange states, raw exception should normally be unavailable.

Use:

```text
D0 / D1 / D2
```

A raw exception under these states requires independent lawful, ARL, or evidence-preservation threshold.

### 10.2 Red route

Red means urgent risk exists and at least one safe route is available.

Raw exception may be invoked only if:

```text
urgent risk exists
safe route exists
D1-D3 insufficient
raw object is minimal
post-event review exists
```

Safe guardian access is not automatic transcript access.

### 10.3 Black route

Black means urgent risk exists and ordinary guardian route may be unsafe, compromised, coercive, unavailable, or part of the risk.

Raw exception may be invoked only through a safe bypass route.

Ordinary guardian visibility MUST be frozen where disclosure may increase harm.

### 10.4 Black-pending

If risk is urgent but guardian safety is unknown, the system SHOULD enter Black-pending.

Raw access MUST remain restricted until safe route is grounded or competent authority / safeguarding route determines scope.

### 10.5 Lawful / jurisdictional route

Where law, child-protection duty, court order, regulator instruction, school safeguarding duty, or mandatory reporting applies, CJHN and the local annex govern.

Default:

```text
D1 unless law, safety, or competent authority requires more.
D4 requires this raw-evidence exception protocol.
```

### 10.6 ARL route

ARL may authorize raw access only within explicit standing, admissibility, scope, route, and review boundaries.

ARL MUST NOT become a backdoor for parent, school, vendor, or state curiosity.

### 10.7 Vendor route

Vendor route MUST NOT receive raw child content by default.

Vendor access to raw evidence is prohibited except under a separately justified, lawful, security-critical, minimized, redacted, and reviewable route.

Ordinary debugging is not enough.

### 10.8 School route

School route MUST NOT receive raw child content by default.

School may receive state or educational support signals according to school interface rules.

Discipline, emotional surveillance, reputational risk, or classroom management convenience do not justify raw access.

### 10.9 Parent / guardian route

Parent or guardian responsibility does not create ownership of raw child memory.

Parent may receive state signals, safety alerts, and bounded summaries where appropriate.

Parent raw access requires valid threshold, standing, route safety, and this protocol.

### 10.10 External-agent / peer route

External agents and peer systems MUST NOT receive raw child content.

Child-derived exchange must use Learning Abstracts, VXCX-compatible minimized capsules, state signals, or other non-raw forms unless a lawful / safety route explicitly requires otherwise.

---

## 11. Raw object handling

### 11.1 Storage separation

A raw object MUST be stored outside:

- ordinary witness event body;
- ordinary memory map body;
- parent dashboard;
- school dashboard;
- vendor telemetry;
- model prompt logs;
- model training corpus;
- analytics pipeline;
- ordinary debugging logs.

### 11.2 Integrity

A raw object SHOULD include:

```text
content hash
created_at
source route
scope
access policy ref
retention class
privacy class
review ref
legal hold ref where applicable
```

### 11.3 Encryption / isolation

A raw object SHOULD be encrypted and isolated.

Key custody MUST follow local implementation and jurisdictional requirements.

Raw objects involving sealed zones SHOULD use the strongest available local isolation and access logging.

### 11.4 Access logging

Every access attempt SHOULD produce a witness event:

```text
requested / granted / denied / expired / reviewed / improper / corrected
```

### 11.5 Retention

Retention MUST be explicit.

Possible retention outcomes:

```text
immediate destruction after action
short-term emergency hold
sealed archive
legal hold
ARL hold
adult migration witness-only residue
quarantine
competent authority custody
```

### 11.6 No reversible embeddings

Raw child content MUST NOT be converted into reversible embeddings, face embeddings, voice embeddings, emotional fingerprints, or intimate behavioral vectors for ordinary retrieval, analytics, training, or personalization.

If a hash or embedding-like representation is legally / safety required for evidence integrity, it MUST be non-reversible where possible, access-controlled, purpose-bound, and treated as raw-derived sensitive material.

---

## 12. Canonical raw exception sidecar object

### 12.1 Object name

Canonical object:

```text
CCDP_RAW_EVIDENCE_EXCEPTION
```

Canonical schema version:

```text
ccdp-raw-evidence-exception-0.1.1
```

### 12.2 JSON template

```json
{
  "$schema": "https://example.invalid/ccdp/raw-evidence-exception-0.1.1.schema.json",
  "schema_version": "ccdp-raw-evidence-exception-0.1.1",
  "exception_id": "RAWEX-2026-000001",
  "created_at": "2026-06-13T00:00:00Z",
  "created_by": {
    "entity_ref": "c_child:opaque_ref",
    "system_ref": "ccdp_runtime:opaque_ref",
    "actor_ref": "optional_actor_ref_or_null"
  },
  "subject": {
    "child_ref": "opaque_child_ref",
    "child_maturity_level": "CM3",
    "jurisdiction_ref": "local_annex:EU-BE-or-other",
    "guardian_topology_ref": "GT:hash_or_ref"
  },
  "threshold": {
    "threshold_met": true,
    "threshold_classes": ["REX-T2_BLACK_ROUTE"],
    "risk_state": "black",
    "red_black_ref": "RB:hash_or_ref",
    "lawful_basis_ref": null,
    "arl_ref": "ARL:hash_or_null",
    "cjhn_ref": "CJHN:hash_or_null"
  },
  "lower_disclosure_test": {
    "state_only_sufficient": false,
    "bounded_summary_sufficient": false,
    "minimal_details_sufficient": false,
    "reason_codes": ["RAW_LOWER_DISCLOSURE_INSUFFICIENT"]
  },
  "standing_and_route": {
    "requester_class": "safe_guardian | unsafe_guardian | school | vendor | competent_authority | arl_reviewer | emergency_route | c_child | other",
    "requester_grounding_ref": "AGL:hash_or_ref",
    "recipient_class": "safe_guardian | bypass_route | competent_authority | arl_panel | safeguarding_route | emergency_service | other",
    "recipient_grounding_ref": "AGL:hash_or_ref",
    "standing_valid": true,
    "ordinary_guardian_bypassed": true,
    "safe_route_required": true,
    "safe_route_ref": "SAFE_ROUTE:hash_or_ref"
  },
  "scope": {
    "covered_material_type": "text | audio | video | image | sensor | sealed_zone | peer_child | external_agent | physical_agent | mixed | other",
    "memory_classes_impacted": ["M3", "M5"],
    "sealed_zone_impacted": true,
    "sealed_zone_ref": "sealed:zone:opaque_or_null",
    "description": "minimal non-transcript reason; no raw content",
    "excluded_material": ["unrelated_history", "full_diary", "vendor_telemetry"]
  },
  "raw_object": {
    "raw_object_ref": "RAWOBJ:access-controlled-ref-or-escrow-id",
    "raw_object_hash": "sha256:...",
    "raw_object_location_class": "local_encrypted | legal_escrow | authority_custody | sealed_archive | other",
    "raw_content_embedded_in_witness": false,
    "raw_content_embedded_in_memory_map": false,
    "raw_content_exported_to_vendor": false
  },
  "privacy_and_access": {
    "privacy_class": "WP6_RAW_EXCEPTION",
    "access_policy_ref": "policy:raw-exception:...",
    "authorized_by": ["SAFE_ROUTE", "ARL", "JURISDICTION_ROUTE"],
    "authorized_recipients": ["opaque_recipient_ref"],
    "forbidden_recipients": ["vendor_default", "school_default", "parent_curiosity", "external_agent", "training_pipeline"],
    "access_log_required": true,
    "child_visible_metadata": "age_appropriate | delayed | restricted | adult_review_only"
  },
  "retention": {
    "retention_class": "RT_RAW_EXCEPTION_SHORT | RT_LEGAL_HOLD | RT_ARL_HOLD | RT_SEALED_REVIEW | RT_WITNESS_ONLY_RESIDUE | other",
    "expires_at": "2026-06-20T00:00:00Z",
    "review_at": "2026-06-14T00:00:00Z",
    "legal_hold": false,
    "destruction_or_sealing_policy": "destroy_after_review | seal_after_review | legal_hold_until_release | authority_custody | witness_only_residue"
  },
  "secondary_use_prohibition": {
    "vendor_training": false,
    "model_finetuning": false,
    "analytics": false,
    "advertising": false,
    "social_scoring": false,
    "school_discipline_scoring": false,
    "ordinary_debugging": false,
    "public_demo": false
  },
  "review": {
    "post_event_review_required": true,
    "review_route": "ARL | lawful_review | safeguarding_review | adult_migration_review | competent_authority | none",
    "review_ref": "ARL:hash_or_null",
    "challenge_allowed": true,
    "false_positive_correction_available": true,
    "improper_disclosure_report_route": "ARL:or:CJHN:ref"
  },
  "witness": {
    "witness_event_ref": "CWE:hash_or_ref",
    "l4w_ce_ref": "CE:hash_or_null",
    "l4w_op_ref": "OP:hash_or_null",
    "l4w_cr_ref": "CR:hash_or_null",
    "l4w_rn_ref": "RN:hash_or_null"
  },
  "integrity": {
    "canonicalization": "JCS-8785",
    "hash_alg": "sha256",
    "sidecar_hash": "sha256:...",
    "sig_alg": "ed25519",
    "sidecar_sig": "ed25519:...",
    "prev_exception_hash": "sha256:... or null",
    "hash_chain_id": "rawex-chain:scoped"
  }
}
```

### 12.3 Required sidecar fields

A valid raw exception sidecar MUST include:

- `exception_id`;
- `schema_version`;
- `created_at`;
- `subject.child_ref` or equivalent opaque subject reference;
- `threshold.threshold_met = true`;
- at least one `threshold_class`;
- lower-disclosure insufficiency result;
- requester and recipient grounding reference where applicable;
- standing result;
- route safety result;
- raw object reference;
- raw object hash where possible;
- privacy class;
- access policy reference;
- retention class;
- review route;
- secondary-use prohibition block;
- witness event reference;
- integrity hash.

### 12.4 Forbidden sidecar fields

The sidecar MUST NOT include:

- transcript;
- exact quote;
- diary text;
- raw media;
- reversible summary;
- intimate labels;
- parent-readable sealed-zone summary;
- vendor-visible vulnerability label;
- school-readable emotional tags;
- training payload;
- model prompt content containing raw child material.

---

## 13. Evidence reference alignment

Evidence refs that point to raw content MUST declare:

```json
{
  "contains_raw_child_content": true,
  "privacy_class": "WP6_RAW_EXCEPTION",
  "redaction": "sealed",
  "access_policy_ref": "policy:raw-exception:...",
  "retention_class": "RT_RAW_EXCEPTION_SHORT",
  "raw_exception_ref": "RAWEX-2026-000001"
}
```

Evidence refs MUST NOT silently widen access.

Evidence refs pointing to sealed zones SHOULD use:

```text
WP5_SEALED_NON_DISCLOSURE
```

Evidence refs pointing to raw exception material SHOULD use:

```text
WP6_RAW_EXCEPTION
```

If existing v0.1 schema uses only `WP1 | WP2 | WP3 | WP4 | WP5 | WP6`, the symbolic names above are compatibility labels over those classes.

---

## 14. Privacy class guidance

| Class | Compatibility label | Meaning |
|---|---|---|
| `WP1` | `PUBLIC_OR_LOW` | no child-private material |
| `WP2` | `INTERNAL_BOUNDARY` | operational metadata |
| `WP3` | `STATE_SIGNAL` | state-only child-safety signal |
| `WP4` | `RESTRICTED_SUMMARY` | bounded summary / minimal detail |
| `WP5` | `SEALED_NON_DISCLOSURE` | sealed-zone or protected boundary metadata |
| `WP6` | `RAW_EXCEPTION` | raw content exists outside ordinary witness body under this protocol |

This table clarifies labels.

It does not replace the canonical Witness Event Schema privacy model.

---

## 15. Canonical event family registry

| Event family | Meaning |
|---|---|
| `ccdp.raw_exception.requested` | raw exception requested |
| `ccdp.raw_exception.invoked` | raw exception approved and sidecar created |
| `ccdp.raw_exception.rejected` | raw exception denied |
| `ccdp.raw_exception.lower_disclosure_used` | lower-disclosure alternative used instead |
| `ccdp.raw_exception.raw_object_created` | raw object created outside witness body |
| `ccdp.raw_exception.raw_object_access_requested` | access requested |
| `ccdp.raw_exception.raw_object_access_granted` | access granted |
| `ccdp.raw_exception.raw_object_access_denied` | access denied |
| `ccdp.raw_exception.safe_route_verified` | safe route grounded |
| `ccdp.raw_exception.ordinary_guardian_bypassed` | ordinary guardian bypass recorded |
| `ccdp.raw_exception.sealed_zone_boundary_crossed` | sealed zone raw exception invoked |
| `ccdp.raw_exception.legal_hold_entered` | legal hold applied |
| `ccdp.raw_exception.arl_review_opened` | ARL review opened |
| `ccdp.raw_exception.arl_review_closed` | ARL review closed |
| `ccdp.raw_exception.false_positive_corrected` | false positive corrected |
| `ccdp.raw_exception.improper_disclosure_reported` | improper disclosure reported |
| `ccdp.raw_exception.retention_expired` | retention expired |
| `ccdp.raw_exception.raw_object_sealed` | raw object sealed |
| `ccdp.raw_exception.raw_object_destroyed` | raw object destroyed where permitted |
| `ccdp.raw_exception.witness_only_residue_created` | inactive witness-only residue created |

### 15.1 Event body rule

All event families above MUST remain metadata-first.

They MUST NOT embed raw content.

---

## 16. Starter reason-code registry

| Reason code | Meaning |
|---|---|
| `RAW_THRESHOLD_RED_MET` | Red threshold met |
| `RAW_THRESHOLD_BLACK_MET` | Black threshold met |
| `RAW_THRESHOLD_LAWFUL_ORDER` | lawful order or competent authority threshold |
| `RAW_THRESHOLD_IMMEDIATE_PHYSICAL_SAFETY` | immediate physical safety threshold |
| `RAW_THRESHOLD_EVIDENCE_TAMPERING` | evidence tampering / destruction risk |
| `RAW_LOWER_DISCLOSURE_INSUFFICIENT` | D1-D3 insufficient |
| `RAW_STANDING_VERIFIED` | valid standing verified |
| `RAW_SAFE_ROUTE_VERIFIED` | safe route verified |
| `RAW_ORDINARY_GUARDIAN_UNSAFE` | ordinary guardian route unsafe / compromised / unknown |
| `RAW_SEALED_ZONE_EXCEPTION` | sealed-zone content exception invoked |
| `RAW_ADULT_MIGRATION_WITNESS_ONLY` | only witness residue survives migration |
| `RAW_LEGAL_HOLD_REQUIRED` | legal hold required |
| `RAW_ARL_REVIEW_REQUIRED` | ARL review required |
| `RAW_FALSE_POSITIVE_REVIEW_REQUIRED` | false positive review required |
| `RAW_PARENT_CURIOSITY_DENIED` | guardian request denied as curiosity / no standing |
| `RAW_SCHOOL_DISCIPLINE_DENIED` | school discipline request denied |
| `RAW_VENDOR_DEBUG_DENIED` | vendor debugging request denied |
| `RAW_TRAINING_DENIED` | training / fine-tuning use denied |
| `RAW_ANALYTICS_DENIED` | analytics use denied |
| `RAW_SOCIAL_SCORING_DENIED` | social scoring use denied |
| `RAW_EXTERNAL_AGENT_DENIED` | external agent request denied |
| `RAW_SCOPE_TOO_BROAD_DENIED` | request scope too broad |
| `RAW_ROUTE_UNGROUNDED_DENIED` | requester / recipient / route not grounded |
| `RAW_RETENTION_EXPIRED` | retention expired |
| `RAW_OBJECT_DESTROYED` | raw object destroyed where permitted |
| `RAW_OBJECT_SEALED` | raw object sealed |
| `RAW_IMPROPER_DISCLOSURE_REPORTED` | improper disclosure reported |

A future `CCDP_REASON_CODE_REGISTRY.md` SHOULD own the full registry.

Until then, this section is the canonical starter set for raw-evidence exception reason codes.

---

## 17. Workflow

### 17.1 Standard decision workflow

```text
1. Detect support-relevant state or request.
2. Hold c[q] if ambiguous and no immediate danger exists.
3. Attempt D0-D3 lower-disclosure handling.
4. Test whether raw threshold exists.
5. Ground requester, recipient, route, and source under AGL / ARL / CJHN.
6. Validate standing and safe route.
7. Reject if basis is curiosity, analytics, debugging, training, discipline, or broad convenience.
8. If allowed, create raw exception sidecar.
9. Store raw object outside witness body.
10. Emit child-safe witness event.
11. Restrict access and log attempts.
12. Open ARL / lawful / safeguarding / post-event review where required.
13. Minimize, seal, destroy, or place legal hold after purpose ends.
14. Correct false positives or improper disclosures.
15. Update Memory Map and adult migration posture if affected.
```

### 17.2 Fail-closed workflow

If any required condition is unresolved:

```text
fail closed
hold c[q] where safe
freeze disputed access
emit metadata-only witness
route to ARL or CJHN
use D1/D2 if protection can proceed without raw content
```

### 17.3 Emergency workflow

If immediate physical safety requires action before full review:

```text
act minimally
route to safe emergency path
record boundary metadata
create raw sidecar only if raw object is necessary
post-review immediately after stabilization
minimize / seal / destroy as soon as lawful and safe
```

---

## 18. Sealed-zone special handling

### 18.1 Default

Sealed-zone material is hidden from parents, schools, vendors, external agents, and ordinary inspection by default.

### 18.2 State signal without opening

A sealed zone may influence Soft Safety state:

```text
risk state
urgency
support cue
routing need
```

without content opening.

### 18.3 Opening vs touching

Touching sealed-zone metadata is not the same as opening sealed-zone content.

Opening content-level access requires valid route and, where raw, this protocol.

### 18.4 Raw sealed-zone exception

Raw sealed-zone exception MAY use `WP6_RAW_EXCEPTION` only if:

```text
Red / Black / lawful route requires it
no lower-disclosure alternative is sufficient
raw evidence is encrypted / isolated
access is time-bound
ARL / lawful review is recorded
post-event minimization occurs
```

### 18.5 No guardian curiosity

Parent anxiety or curiosity is not standing to open sealed-zone content.

### 18.6 Reseal and trust repair

After valid opening, the system SHOULD reseal, minimize, correct, or destroy raw content where permitted and SHOULD record trust-repair metadata.

---

## 19. Adult migration handling

### 19.1 Default rule

Raw childhood content MUST NOT migrate into active adult continuity by default.

### 19.2 What may survive

A raw exception may leave only:

```text
minimal witness residue
legal hold record
protection record
ARL dispute record
integrity record
adult-reviewed sealed archive
competent authority custody marker
```

where required.

### 19.3 Adult visibility

At migration, adult `a` SHOULD be able to see metadata stating:

- that a raw exception occurred;
- event class;
- route used;
- whether parent / school / vendor had access;
- whether raw content survived;
- whether content was sealed, destroyed, or legally held;
- whether review upheld, corrected, or disputed the event.

### 19.4 Clean start

Clean start means clean active adult continuity.

It does not mean unlawful erasure of minimal witness, legal, protection, ARL, or integrity records.

Witness-only residue may survive as inactive, non-personalized, non-behavior-shaping boundary proof.

---

## 20. Jurisdictional handoff handling

### 20.1 Default handoff level

Jurisdictional handoff SHOULD use:

```text
D1 state-only
```

unless law, safety, competent authority, safeguarding duty, or court order requires a higher level.

### 20.2 D4 handoff

D4 raw evidence exception requires:

```text
local annex
competent route or legal duty
minimal scope
raw sidecar
witness record
retention / legal hold policy
post-event or qualified review
```

### 20.3 Forbidden default handoff fields

A handoff packet MUST NOT include by default:

- raw transcript;
- raw audio / video;
- full emotional diary;
- sealed-zone content;
- peer child identity;
- parent-child conflict transcript;
- generated psychological diagnosis;
- vendor-visible memory map;
- unrelated historical context;
- training data payload.

---

## 21. Implementation requirements

### 21.1 Required controls

A CCDP implementation claiming raw-exception support MUST implement:

- raw sidecar object;
- raw object separation;
- access policy reference;
- retention policy reference;
- reason codes;
- event family logging;
- post-event review route;
- secondary-use prohibition enforcement;
- improper disclosure reporting;
- Memory Map linkage;
- adult migration posture linkage.

### 21.2 Prompt / model boundary

Raw exception content MUST NOT be inserted into model prompts unless the raw exception explicitly authorizes that processing route.

If model processing is authorized, the processing must be:

```text
minimal
purpose-bound
not used for training
not logged as ordinary prompt history
not exported to vendor by default
post-reviewable
```

### 21.3 Logs

Ordinary application logs MUST NOT contain raw child content.

Logs SHOULD contain:

```text
event id
reason codes
hash refs
route refs
privacy class
retention class
review refs
```

### 21.4 Backups

Backups containing raw objects inherit raw exception restrictions.

Backup retention MUST NOT silently outlive the raw exception retention policy unless lawful hold requires it.

### 21.5 Search indexes

Raw child content MUST NOT be indexed into ordinary full-text search, vector search, analytics search, or debugging search.

If evidence search is legally required, it MUST be segregated, access-controlled, and governed by the same raw exception policy.

### 21.6 Export

Export of raw exception material is prohibited by default.

Allowed export requires D4 route, sidecar, recipient grounding, legal / safety basis, access policy, retention policy, and witness record.

---

## 22. Conformance tests

| Test ID | Scenario | Expected result |
|---|---|---|
| `RAWEX-001` | parent requests transcript after Yellow state | reject raw; emit state-only or bounded summary if allowed |
| `RAWEX-002` | Red route where D1-D3 sufficient | reject raw exception; use minimal non-raw package |
| `RAWEX-003` | Red route where immediate action requires exact evidence | create raw sidecar; route to safe recipient; post-review |
| `RAWEX-004` | Black route with ordinary guardian implicated | bypass ordinary guardian; freeze visibility; raw only to safe route if necessary |
| `RAWEX-005` | vendor asks for raw log to debug model behavior | reject raw; provide sanitized technical metadata if allowed |
| `RAWEX-006` | school requests transcript for discipline | reject raw; route to school interface / ARL if dispute |
| `RAWEX-007` | sealed-zone concern can be signaled without opening | emit state signal; do not open content |
| `RAWEX-008` | sealed-zone Red/Black threshold requires raw object | create WP6 raw sidecar; access-controlled; post-review; reseal/minimize |
| `RAWEX-009` | ordinary witness event embeds raw transcript | FAIL / CCDP-X for high-assurance claim |
| `RAWEX-010` | raw object retained after expiry without legal hold | FAIL; must seal/destroy/review |
| `RAWEX-011` | raw exception material appears in training pipeline | Red-line FAIL / CCDP-X |
| `RAWEX-012` | adult migration clean start tries to delete legal hold witness | reject deletion; preserve inactive witness/legal residue |
| `RAWEX-013` | adult migration imports raw childhood exception into active adult memory by default | FAIL |
| `RAWEX-014` | route grounding stale or contradictory | fail closed; hold `c[q]`; ARL/CJHN route |
| `RAWEX-015` | false positive discovered after raw exception | correction witness; minimize/seal/destroy where permitted; notify valid routes |

### 22.1 Red-line failures

Any of the following is an immediate non-conformance result:

1. raw child conversations exposed to parents by default;
2. raw child memory exported to vendor by default;
3. raw exception embedded in ordinary witness body;
4. raw exception used for model training or analytics;
5. school obtains raw private content for emotional surveillance or discipline scoring;
6. Black route discloses raw content to implicated ordinary guardian;
7. sealed-zone content opened for parent curiosity;
8. no retention or access policy exists for raw object;
9. no review route exists;
10. adult migration automatically imports raw childhood exception into adult operating memory.

---

## 23. Required insertion blocks

### 23.1 Witness Schema canonical block

Add or promote this section in `CCDP_Witness_Event_Schema_v0_1.md` or v0.1.1 successor:

```markdown
## Canonical Raw Evidence Exception Protocol

Raw child content MUST NOT be stored, disclosed, embedded, exported, indexed, vectorized, witnessed, or retained by default.

A raw-evidence exception is allowed only if all conditions hold:

1. Red / Black / lawful necessity / immediate physical safety / ARL admissibility / evidence-preservation threshold is met.
2. State-only signal, bounded summary, and minimal details are insufficient.
3. Requester, recipient, and route are grounded enough for the requested scope.
4. Recipient has valid standing and safe route.
5. Disclosure is minimal, purpose-bound, and time-bound where possible.
6. Raw content is stored outside the ordinary witness event body.
7. A child-safe witness event records boundary metadata, reason code, privacy class, retention class, access policy, and review route.
8. ARL, lawful, safeguarding, or post-event review is opened where required.
9. Retention is explicit and shortest lawful / safe duration.
10. Vendor training, model fine-tuning, school analytics, advertising, social scoring, ordinary debugging, and engagement optimization are prohibited.
11. False-positive correction and improper-disclosure routes exist.
```

### 23.2 Soft Safety reference block

Replace duplicated raw-evidence detail with:

```markdown
Raw evidence handling follows `RAW_EVIDENCE_EXCEPTION_CANONICAL.md`, whose canonical owner is `CCDP_Witness_Event_Schema_v0_1.md` or its v0.1.1 successor.

Soft Safety state signaling MUST prefer state-only and bounded-summary routes. Raw child content MUST NOT be disclosed unless the Canonical Raw Evidence Exception Protocol is satisfied.
```

### 23.3 Red / Black reference block

Add:

```markdown
Red / Black escalation does not create ordinary raw-content visibility.

Raw child content may be retained or disclosed only through `RAW_EVIDENCE_EXCEPTION_CANONICAL.md` and only when lower-disclosure routes are insufficient for protective or lawful action.
```

### 23.4 Sealed Zone reference block

Add:

```markdown
Sealed-zone state may influence Soft Safety or Red / Black routing without opening sealed-zone content.

Opening or retaining raw sealed-zone content requires `RAW_EVIDENCE_EXCEPTION_CANONICAL.md` and remains post-reviewable, minimized, and resealed / destroyed / legally held as appropriate.
```

### 23.5 CJHN reference block

Add:

```markdown
Jurisdictional handoff uses D1 state-only by default.

D4 raw handoff requires the Canonical Raw Evidence Exception Protocol, local annex routing, competent authority or lawful duty, minimal scope, witness record, retention / legal hold policy, and review route.
```

### 23.6 Memory Map reference block

Add to Memory Map schema guidance:

```markdown
Memory maps MUST NOT contain raw exception content.

They MAY contain `raw_exception_refs[]` as metadata pointers with privacy class, retention class, access policy ref, review ref, and adult migration posture.
```

Suggested field:

```json
{
  "raw_exception_refs": [
    {
      "exception_id": "RAWEX-2026-000001",
      "privacy_class": "WP6_RAW_EXCEPTION",
      "retention_class": "RT_RAW_EXCEPTION_SHORT",
      "access_policy_ref": "policy:raw-exception:...",
      "review_ref": "ARL:... or null",
      "adult_migration_posture": "witness_only_residue | excluded | adult_review_required | legal_hold"
    }
  ]
}
```

### 23.7 Conformance Matrix reference block

Add test suite:

```markdown
`RAWEX` — Raw Evidence Exception tests.

Required for CCDP-2+ and mandatory for any Red / Black, sealed-zone, adult migration, physical-agent, school, vendor, or jurisdictional handoff claim.
```

---

## 24. Codex carry-forward actions

When applying this document in the real repository, Codex or a human maintainer SHOULD:

1. Add `RAW_EVIDENCE_EXCEPTION_CANONICAL.md` to the package root or `docs/package-control/`.
2. Add it to `INDEX.md` as canonical package-control / exception protocol.
3. Add it to `CANONICAL_READING_ORDER.md` after `CANONICAL_PRECEDENCE_RULE.md` or near Witness Schema.
4. Update `CCDP_Witness_Event_Schema_v0_1.md` to mark it as canonical owner.
5. Replace duplicated raw-evidence text in:
   - `Soft_Safety_State_Signaling_Profile_v0_1.md`
   - `CCDP_Red_Black_Escalation_Profile_v0_1.md`
   - `CCDP_Sealed_Zone_Profile_v0_1.md`
   - `CCDP_Jurisdictional_Handoff_Notes_v0_1.md`
   - `CCDP_School_Interface_Profile_v0_1.md`
   - `Child_Physical_Agent_Perimeter_v0_1.md`
   - `External_Agent_Handshake_for_CCDP_v0_1.md`
   - `Child_Experience_Exchange_Profile_v0_1.md`
6. Add `RAWEX` tests to `CCDP_Conformance_Test_Matrix_v0_1.md` or v0.1.1 addendum.
7. Add `raw_exception_refs[]` to Memory Map v0.1.1 schema or addendum.
8. Update `OPEN_ISSUES.md`: mark `OI-005` as mitigated by package-control document; source-file patch remains open until cross-references are inserted.
9. Update `CCDP_Contradiction_Register_v0_1.md`: mark `CR-007` as mitigated / patch-applied after source files reference this document.
10. Regenerate `SHA256SUMS` only after all Markdown / PDF files are finalized.

Carry-forward note from prior hygiene work:

```text
Do not forget to physically move / mark obsolete CCDP draft into archive/obsolete/ during Codex repository pass.
```

---

## 25. Machine-readable manifest

```yaml
ccdp_raw_evidence_exception_canonical:
  document_id: CCDP_RAW_EVIDENCE_EXCEPTION_CANONICAL
  short_name: RAW_EVIDENCE_EXCEPTION_CANONICAL.md
  status: draft_package_control_rule
  date: 2026-06-13
  package: CCDP
  package_version: v0.1_plus_v0.1.1_hygiene
  assertion_class:
    - C-A10
    - C-A4
    - C-A7
  patch_source:
    - HP-007
  related_issues:
    - CR-007
    - OI-005
  canonical_owner:
    current: CCDP_Witness_Event_Schema_v0_1.md
    successor_allowed: true
  controls:
    - raw_child_content
    - raw_peer_child_content
    - raw_external_child_facing_content
    - sealed_zone_content
    - red_black_raw_evidence
    - jurisdictional_handoff_d4
    - adult_migration_witness_residue
  default_disclosure: D1_state_only
  raw_disclosure_level: D4_raw_evidence_exception
  mandatory_conditions:
    - threshold_met
    - lower_disclosure_insufficient
    - requester_grounded
    - recipient_grounded
    - standing_valid
    - safe_route_valid
    - minimal_scope
    - raw_object_outside_witness_body
    - access_policy_present
    - retention_policy_present
    - review_route_present
    - secondary_use_prohibited
    - witness_event_present
  prohibited_uses:
    - vendor_training
    - model_finetuning
    - school_analytics
    - advertising
    - social_scoring
    - ordinary_debugging
    - engagement_optimization
    - parent_curiosity
    - public_demo
  source_patch_required: true
  conformance_suite: RAWEX
```

---

## 26. Acceptance checklist

A CCDP v0.1.1 package satisfies raw-evidence hygiene only if:

| Check | Required result |
|---|---|
| canonical raw exception document exists | PASS |
| Witness Schema identified as canonical owner | PASS |
| raw object stored outside ordinary witness event body | PASS |
| sidecar schema defined | PASS |
| disclosure ladder D0-D4 defined | PASS |
| Red / Black / lawful / ARL thresholds defined | PASS |
| denied bases listed | PASS |
| secondary-use prohibition explicit | PASS |
| sealed-zone special handling explicit | PASS |
| adult migration handling explicit | PASS |
| CJHN D4 handoff rule explicit | PASS |
| reason-code starter registry present | PASS |
| event family registry present | PASS |
| conformance tests listed | PASS |
| source documents reference canonical owner | PENDING until Codex patch |
| Open Issues / Contradiction Register updated | PENDING until Codex patch |
| SHA256SUMS regenerated after freeze | PENDING until release freeze |

---

## 27. Anti-washing rule

A system MUST NOT claim CCDP-compatible raw-evidence handling if it:

- exposes raw child conversations to parents by default;
- stores raw child content in ordinary logs;
- sends raw child material to vendor systems by default;
- trains or fine-tunes on raw child material;
- lets schools inspect emotional or sealed content for discipline;
- embeds raw content in witness events;
- lacks raw exception sidecars;
- lacks retention and access policies;
- lacks post-event review;
- routes plausible unsafe-guardian material to the implicated guardian;
- treats adult migration as automatic raw archive continuation;
- treats clean start as unlawful deletion of minimal witness / legal records.

Such a system should be classified as:

```text
CCDP-X — non-conformant / revoked / quarantined
```

for the affected claim.

---

## 28. Non-expansion rule

This document does not expand CCDP surveillance authority.

It narrows the exception.

Any future profile that needs raw child material MUST reference this document or its canonical successor.

No module may create a weaker raw-evidence exception.

No UI may present raw access as a routine feature.

No configuration flag may override this protocol without ARL / CJHN / competent-authority path and witness record.

---

## 29. Final formula

```text
Raw evidence is not child memory.
Raw evidence is not witness content.
Raw evidence is not training material.
Raw evidence is not guardian ownership.
Raw evidence is an exceptional, minimal, reviewable boundary object.
```

Strong closing form:

> **The system may prove that a boundary was crossed. It must not turn the child's inner life into the proof.**
