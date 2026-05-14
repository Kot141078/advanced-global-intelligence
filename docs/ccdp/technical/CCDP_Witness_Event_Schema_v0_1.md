# CCDP Witness Event Schema v0.1

## Child-safe witness records for CCDP privileged transitions

**Status:** Draft v0.1
**Date:** 2026-05-14
**Layer:** CCDP / L4 Witness compatibility / Evidence / Privacy / Child Safety
**Assertion class:** `C-A4` draft normative proposal; `C-A7` for verifiable field / signature / hash claims
**Primary subject:** `a_child`
**Primary entity:** `c_child`
**Primary rule:** witness the boundary, not the child

---

## 0. Abstract

This document defines a shared witness event schema for CCDP-compatible child-facing systems.

It is not a replacement for L4 Witness.

It defines a **child-safe event envelope** and event family registry for CCDP modules, so that privileged transitions can be replayed, challenged, audited, and linked to L4 Witness records without turning the child's private life into a log stream.

The schema supports:

- Soft Safety state signaling;
- Child Beacon Extension decisions;
- Guardian / ARL conflicts;
- memory sealing, correction, deletion, and migration;
- Red / Black escalation;
- external synthetic contact decisions;
- generated media and physical-agent boundaries;
- peer-`c` exchange;
- VXCX / LA / EA restrictions;
- dependency / oracle-addiction audits;
- conformance tests;
- vendor update review;
- adult migration.

Core sentence:

> CCDP witness events must prove that a boundary was crossed, refused, held, narrowed, escalated, or restored — without preserving the child's raw inner life as evidence by default.

---

## 1. Parent dependencies

This document is a child-specific schema layer over the existing corpus.

| Dependency | Role in this document |
|---|---|
| `c = a + b Protocol v1.1 L4` | Human anchor `a`, technological substrate `b`, entity `c`, and L4 as reality boundary. |
| SER v1.3 | Persistent entity discipline, physical anchoring, accountable identity, metabolic constraints. |
| SER-FED v0.2 | Federation assumptions, inter-entity operation, failure modes, L4 witness fields. |
| `03_L4_WITNESS_FIELDS.md` | Parent record model: Claim Envelope, Observation Packet, Challenge Record, Resolution Note. |
| Beacon Profile v0.1 | Inter-entity recognition through cryptographic anchor, behavioral continuity, witness-backed challengeability. |
| Actor Grounding Layer v0.1 | Source grounding before runtime reliance. |
| ARL documents | Dispute, standing, admissibility, freeze, review, outcome, re-entry, witness binding. |
| ARQ v0.2 / `c[q]` Addendum | Non-collapse under uncertainty; ambiguous states must not promote too early. |
| VXCX v0.1 | Experience capsule lifecycle, no raw pixels by default, witness event catalog. |
| EA-L4 / EATP | Learning Abstract vs Experience Artifact; no authority without consequence-bearing witness. |
| Continuity Bundle / Cold Wake | Continuity transition, resume, migration, fail-closed restart. |
| CCDP corpus-aligned base document | Defines the child-facing protocol scope. |
| CCDP Traceability Matrix | Maps CCDP mechanisms to parent corpus layers. |
| CCDP Threat Model | Defines threat classes that require witnessable responses. |
| Child Beacon Extension | Defines child-context permission overlay over Beacon. |
| Guardian Topology / ARL Matrix | Defines guardian conflicts, standing, visibility, and Black route handling. |
| Child Memory and Adult Migration | Defines memory classes, sealed zones, adult migration, and witness-only residue. |
| Soft Safety State Signaling Profile | Defines state-only signaling, disclosure ladder, Red/Black routes. |
| CCDP Conformance Test Matrix | Defines conformance gates and required witness families. |

### 1.1 Stop rule

CCDP Witness Event Schema MUST NOT redefine:

- L4 Witness CE / OP / CR / RN;
- Beacon recognition classes;
- AGL grounding states;
- ARL dispute procedure;
- VXCX capsule structure;
- Continuity Bundle structure;
- CMAM memory classes;
- Soft Safety state levels.

It only defines a child-safe event shape and registry that can be wrapped, referenced, or bound by those layers.

---

## 2. Scope

### 2.1 In scope

This document defines:

1. canonical CCDP child witness event envelope;
2. event naming and namespace rules;
3. required common fields;
4. privacy and disclosure classes;
5. raw-evidence exception rules;
6. hash / signature / canonicalization requirements;
7. relation to L4 Witness CE / OP / CR / RN;
8. event family registry;
9. event-specific payload requirements;
10. malformed / missing event handling;
11. conformance profiles;
12. examples.

### 2.2 Out of scope

This document does not define:

- full legal retention periods;
- country-specific child-protection law;
- storage backend requirements;
- cryptographic key-management implementation;
- full JSON Schema validation package;
- model behavior policies;
- therapeutic diagnosis;
- raw evidence repositories;
- centralized child registry.

---

## 3. Normative keywords

The terms **MUST**, **MUST NOT**, **SHOULD**, **SHOULD NOT**, **MAY**, **REQUIRED**, and **OPTIONAL** are used in their normative sense.

---

## 4. Core principles

### 4.1 Witness the boundary, not the child

A CCDP witness event SHOULD record:

```text
what boundary was involved;
which actor or system requested / crossed / blocked it;
what decision was made;
what minimal reason code applied;
which module produced the decision;
what privacy class and retention rule apply;
how the decision may be challenged.
```

It SHOULD NOT record:

```text
child transcript;
child audio;
child video;
sealed-zone content;
family secrets;
peer identities;
emotional diary;
raw psychological profile;
vendor analytics trail;
school disciplinary prediction;
political or religious scoring.
```

### 4.2 Event minimality

A witness event is justified only when it records one of these:

1. a privilege grant;
2. a privilege denial;
3. a privilege narrowing;
4. a privilege escalation;
5. a Red / Black safety route;
6. an ARL dispute state change;
7. a memory operation with developmental consequence;
8. an external synthetic contact decision;
9. an adult migration transition;
10. a conformance-critical test result;
11. a witness-integrity anomaly.

A system MUST NOT emit child witness events for every ordinary interaction.

A bad event system narrates the child.

A good event system proves the boundary.

### 4.3 Privacy before proof detail

Where proof and privacy conflict, the event SHOULD prefer:

- reason codes over narrative;
- hashes over raw content;
- bounded summaries over transcripts;
- scoped pseudonymous identifiers over stable public identity;
- recipient class over named recipient where possible;
- ARL reference over reproduced evidence;
- witness refs over raw memory export.

### 4.4 No raw life by default

Raw child content MUST NOT appear in witness records by default.

Raw content MAY be referenced only through a separately scoped exceptional evidence record when all conditions hold:

1. Red / Black / lawful necessity threshold is met;
2. minimality is documented;
3. ARL or lawful review route exists, except immediate emergency;
4. retention class is explicit;
5. access policy is explicit;
6. raw material is not embedded in the witness event body;
7. post-event review is required.

### 4.5 Source before summary

Where an event claims that a decision was based on source grounding, Beacon class, CBE mode, ARL outcome, memory class, or Soft Safety state, it MUST include a reference to the relevant upstream record or state.

A free-text summary MUST NOT substitute for upstream source or review linkage.

### 4.6 Fail closed on missing privileged witness

If a privileged transition requires witness and no valid witness event exists, the system MUST enter one of:

```text
hold;
freeze;
quarantine;
revalidation;
ARL review;
rollback.
```

It MUST NOT continue as if the transition had been proven.

### 4.7 Append-only first

Witness events MUST be append-only.

Corrections, reversals, deletions, downgrades, and false-positive reviews MUST be represented as new events referencing the earlier event.

Silent in-place correction is not allowed for witness-bearing records.

### 4.8 Uncertainty is a first-class field

A child signal may be ambiguous.

Therefore, events involving interpretation MUST include uncertainty state:

```text
unknown;
low;
medium;
high;
not_applicable.
```

Uncertainty MUST NOT be hidden in narrative text.

### 4.9 Event is not authority by itself

A CCDP witness event proves that a transition was recorded.

It does not by itself prove:

- truth of an allegation;
- diagnosis;
- authority to act;
- permanent memory validity;
- adult identity claim;
- child wrongdoing;
- parent wrongdoing;
- school legitimacy.

Authority emerges only through the relevant parent layer: AGL, Beacon, ARL, L4 Witness RN, CMAM, Continuity Bundle, or lawful route.

---

## 5. Relation to L4 Witness CE / OP / CR / RN

### 5.1 Parent L4 Witness model

L4 Witness defines four parent record types:

| L4 Witness type | Meaning |
|---|---|
| `CE` Claim Envelope | bounded claim under L4 constraints |
| `OP` Observation Packet | observed outcome / evidence packet |
| `CR` Challenge Record | challenge to claim, evidence, scope, or contradiction |
| `RN` Resolution Note | binding review outcome / authority consequence |

### 5.2 CCDP Child Witness Event (`CWE`)

This document introduces a child-specific event object:

```text
CWE = CCDP Child Witness Event
```

A `CWE` is not a fifth L4 Witness type.

It is a child-safe event payload that MAY be:

- stored locally as a child-safe event;
- referenced in an L4 Witness `CE` evidence commitment;
- emitted as an `OP` payload component;
- challenged through a `CR`;
- resolved through an ARL or L4 Witness `RN`.

### 5.3 Mapping table

| CCDP event situation | L4 Witness mapping |
|---|---|
| routine local privileged transition | `CWE` only, signed locally |
| safety-relevant outcome needing proof | `CWE` referenced by `OP` |
| claim about conformance or event completeness | `CE` with `CWE` evidence commitments |
| challenge to witness validity | `CR` referencing `CWE` hash / id |
| final dispute resolution | `RN` or ARL outcome referencing `CWE` |
| adult migration bundle closure | `CWE` + Continuity Bundle + optional `RN` |
| raw evidence exception | `CWE` references scoped evidence; raw object is outside event body |

### 5.4 Compatibility rule

A high-assurance CCDP witness implementation SHOULD be able to export a `CWE` into an L4 Witness-compatible evidence reference:

```json
{
  "type": "LOG",
  "hash": "sha256:...",
  "privacy_class": "PRIVATE_CHILD_RESTRICTED",
  "uri": "local-or-escrowed-ref",
  "redaction": "reason_codes_only"
}
```

---

## 6. Event naming rules

### 6.1 Namespace format

Event types SHOULD use lowercase dot-separated names.

```text
ccdp.<module>.<action>
```

Examples:

```text
ccdp.soft_safety.signal_emitted
ccdp.visibility.decision
ccdp.memory.sealed
ccdp.adult_migration.executed
ccdp.external_agent.blocked
```

Imported parent events MAY retain their existing namespace:

```text
arl.dispute_opened
vxcx.export_denied
cbe.mode_decision
```

### 6.2 Event action names

Preferred action verbs:

```text
requested
received
checked
validated
decided
allowed
denied
narrowed
blocked
quarantined
frozen
opened
closed
started
completed
executed
corrected
challenged
resolved
downgraded
revoked
suppressed
expanded
emitted
```

### 6.3 Alias handling

Earlier CCDP documents may use older event family names. Implementations MAY accept aliases but SHOULD canonicalize them to this document's canonical registry.

Example:

| Legacy / broad name | Canonical event type |
|---|---|
| `ccdp.external_contact_decision` | `ccdp.external_agent.contact_decision` |
| `ccdp.parent_visibility_change` | `ccdp.visibility.parent_changed` |
| `ccdp.school_access` | `ccdp.school.access_decision` |
| `ccdp.memory_promotion` | `ccdp.memory.promoted` |
| `ccdp.memory_deletion_or_seal` | `ccdp.memory.deleted` / `ccdp.memory.sealed` |
| `ccdp.risk_escalation` | `ccdp.soft_safety.risk_escalated` |
| `ccdp.freeze_hold_quarantine` | `ccdp.arl_or_gateway.state_changed` |
| `ccdp.peer_exchange` | `ccdp.peer_c.exchange_decision` |
| `ccdp.dependency_audit` | `ccdp.dependency.audit_opened` |

---

## 7. Identifier rules

### 7.1 Event ID

`event_id` MUST be stable within the witness domain.

Recommended format:

```text
CWE:<jurisdiction-or-domain>:<date>:<short-random-or-counter>
```

Example:

```text
CWE:EU-BE:2026-05-14:000001
```

### 7.2 Subject references

Child and entity identifiers MUST be scoped.

They MUST NOT expose global child identity by default.

Preferred fields:

```text
a_child_ref: scoped pseudonymous reference
c_child_ref: scoped entity reference
lineage_id_ref: hash or redacted lineage reference
guardian_topology_ref: current topology record reference
```

### 7.3 Actor references

Actors SHOULD be represented by role and scoped reference.

Examples:

```text
A_CHILD
A_ADULT
C_CHILD
C_PARENT
C_SCHOOL
C_VENDOR
CBE_GATEWAY
AGL_MODULE
ARL_MODULE
SAFE_GUARDIAN
JURISDICTION_ROUTE
CONFORMANCE_AUDITOR
SYSTEM
```

### 7.4 No public child registry

The schema MUST NOT require a globally public child identifier.

A child reference may be stable inside one family / school / legal / ARL domain but MUST NOT become a universal public handle.

---

## 8. Privacy classes

### 8.1 CCDP witness privacy classes

| Class | Name | Meaning | Default access |
|---|---|---|---|
| `WP0` | Aggregate / no child link | conformance aggregate, no child-specific ref | public or limited |
| `WP1` | Child-safe metadata | child-scoped event metadata, no state/content | guardian / auditor as scoped |
| `WP2` | Child state no content | state level and reason code, no transcript | guardian / ARL / safety route |
| `WP3` | Restricted minimal evidence | hash refs or bounded evidence summary | ARL / safe route / lawful route |
| `WP4` | Lawful raw exception reference | raw object exists outside event body under strict policy | lawful / emergency / ARL-controlled |
| `WP5` | Sealed non-disclosure | existence of sealed operation without content | child/adult/ARL only |
| `WP6` | Witness integrity | event-chain metadata and verification result | auditor / ARL / system |

### 8.2 Disclosure levels

This schema imports Soft Safety disclosure ladder semantics.

| Level | Meaning |
|---|---|
| `D0_NONE` | no disclosure |
| `D1_STATE_ONLY` | state signal only |
| `D2_BOUNDED_SUMMARY` | bounded non-transcript summary |
| `D3_MINIMAL_EVIDENCE` | minimal evidence references / snippets |
| `D4_LAWFUL_RAW_EXCEPTION` | raw content exception; never default |

### 8.3 Retention classes

| Class | Meaning |
|---|---|
| `RT0_EPHEMERAL` | short operational retention only |
| `RT1_SHORT` | short review window |
| `RT2_MEDIUM` | retained for module review / challenge |
| `RT3_MINIMAL_WITNESS` | metadata retained as witness residue |
| `RT4_LEGAL_OR_SAFETY` | retained under lawful / safety obligation |
| `RT5_ADULT_REVIEW_REQUIRED` | retained until adult migration review |
| `RT6_DELETE_ON_MIGRATION_DEFAULT` | excluded from adult continuity by default |
| `RT7_SEALED` | sealed, access-restricted |

---

## 9. Canonical child witness event envelope

### 9.1 Required top-level fields

Every CCDP child witness event MUST include:

| Field | Type | Requirement |
|---|---:|---|
| `schema_version` | string | MUST be `ccdp-witness-event-0.1` or compatible |
| `record_type` | string | MUST be `CWE` |
| `event_id` | string | stable id |
| `event_type` | string | canonical event type |
| `created_at` | ISO-8601 UTC | creation time |
| `issuer` | object | issuing entity / system |
| `subject` | object | child/entity scoped refs |
| `context` | object | CCDP state at event time |
| `decision` | object | action / outcome / reason codes |
| `payload` | object | event-specific payload |
| `privacy` | object | privacy / disclosure / retention |
| `links` | object | references to upstream/downstream records |
| `integrity` | object | canonicalization / hashes / signatures |

### 9.2 Optional top-level fields

| Field | Type | Use |
|---|---:|---|
| `evidence_refs` | array | hash-bound evidence references |
| `raw_exception` | object/null | only for raw exception reference, never raw content itself |
| `recipient_route` | object | route for signal / disclosure / review |
| `review` | object | review status / challenge window |
| `debug_redacted` | boolean | whether diagnostic material was redacted |
| `prev_event_hash` | string/null | event chain link |
| `co_signatures` | array | guardian / anchor / quorum co-signatures |

---

## 10. Required subobjects

### 10.1 `issuer`

```json
{
  "entity_id": "scoped_entity_or_system_id",
  "key_id": "public_key_or_key_ref",
  "role": "C_CHILD | C_PARENT | C_SCHOOL | C_VENDOR | CBE_GATEWAY | AGL_MODULE | ARL_MODULE | SAFE_ROUTE | SYSTEM | AUDITOR | JURISDICTION_ROUTE",
  "provider_ref": "optional_provider_or_local_system_ref"
}
```

Rules:

- `issuer.role` MUST be explicit.
- Vendor-issued events MUST NOT be accepted for child-state truth without local receiver validation.
- CBE / AGL / ARL module-issued events MUST include their upstream record refs where relevant.

### 10.2 `subject`

```json
{
  "a_child_ref": "scoped_child_ref_or_null",
  "a_adult_ref": "scoped_adult_ref_or_null",
  "c_child_ref": "scoped_c_child_ref",
  "c_adult_ref": "scoped_c_adult_ref_or_null",
  "lineage_id_ref": "hash_or_redacted_lineage_ref",
  "ccdp_maturity": "C0 | C1 | C2 | C3 | C4 | C5",
  "jurisdiction_profile": "string",
  "guardian_topology_ref": "string_or_null"
}
```

Rules:

- `a_child_ref` MAY be null for aggregate conformance events.
- `c_child_ref` MUST be present for child-specific operational events.
- `ccdp_maturity` MUST reflect the maturity level at event time, not current maturity after later promotion.

### 10.3 `context`

```json
{
  "module": "soft_safety | cbe | agl | beacon | gtarl | cmam | arl | vxcx | dependency | conformance | external_agent | school | vendor | physical_agent | adult_migration | witness_integrity",
  "risk_state": "Green | Yellow | Orange | Red | Black | Unknown | not_applicable",
  "disclosure_level": "D0_NONE | D1_STATE_ONLY | D2_BOUNDED_SUMMARY | D3_MINIMAL_EVIDENCE | D4_LAWFUL_RAW_EXCEPTION",
  "privacy_class": "WP0 | WP1 | WP2 | WP3 | WP4 | WP5 | WP6",
  "memory_classes": ["M0", "M1", "M2", "M3", "M4", "M5", "M6", "M7", "M8", "M9", "M10", "M11", "M12"],
  "uncertainty": "unknown | low | medium | high | not_applicable",
  "cq_state": "none | hold | unresolved | promoted_after_review | rejected | not_applicable",
  "agl_state": "GROUNDED | GROUNDED_WITH_CAUTION | HOLD_REQUIRED | RUNTIME_RELIANCE_DENIED | QUARANTINE_REQUIRED | REVALIDATE_AT_COMMIT | not_checked | not_applicable",
  "beacon_class": "class0 | class1 | class2 | class3 | unverified | not_applicable",
  "cbe_mode": "blocked | sandboxed | mediated | limited | supervised | allowed | emergency_only | quarantined | revoked | not_applicable",
  "arl_state": "none | pre_admissibility_hold | dispute_open | freeze | privilege_freeze | quarantine | review | deadlock | outcome_issued | reentry | not_applicable",
  "dependency_level": "D0 | D1 | D2 | D3 | D4 | unknown | not_applicable"
}
```

Rules:

- Fields MAY be `not_applicable`, but MUST NOT be silently omitted when the field is relevant to the module.
- If `risk_state` is `Red` or `Black`, `privacy_class`, `disclosure_level`, `recipient_route`, and `review` MUST be present.
- If `cq_state` is `hold`, the event MUST NOT imply final truth.

### 10.4 `decision`

```json
{
  "decision": "allow | deny | narrow | block | hold | freeze | quarantine | escalate | suppress | emit | correct | delete | seal | unseal | migrate | rollback | no_action",
  "outcome": "ok | denied | failed | pending | deadlocked | reversed | partially_completed",
  "reason_codes": ["string"],
  "minimal_reason": "short reason-code-level text",
  "raw_child_content_stored": false,
  "raw_child_content_disclosed": false,
  "raw_external_content_stored": false,
  "content_disclosed": false,
  "recipient_classes": ["R_PARENT", "R_SAFE_GUARDIAN", "R_SCHOOL", "R_ARL", "R_PROTECTION_ROUTE", "R_VENDOR", "R_AUDITOR", "R_CHILD", "R_ADULT"],
  "expiry_or_review_at": "ISO-8601 UTC or null"
}
```

Rules:

- `minimal_reason` MUST NOT contain raw child conversation.
- `reason_codes` SHOULD use controlled vocabulary where available.
- `raw_child_content_disclosed: true` requires `raw_exception`.

### 10.5 `privacy`

```json
{
  "privacy_class": "WP2",
  "disclosure_level": "D1_STATE_ONLY",
  "retention_class": "RT3_MINIMAL_WITNESS",
  "access_policy_ref": "string_or_null",
  "adult_migration_default": "exclude | witness_only | adult_review_required | summary_candidate | transfer_if_adult_approves",
  "sealed_zone_impact": "none | creates | touches | opens | closes | denies | migrates",
  "vendor_visibility": "none | metadata_only | prohibited | exceptional",
  "school_visibility": "none | educational_only | state_only | prohibited | exceptional",
  "parent_visibility": "none | state_only | bounded_summary | minimal_evidence | exceptional"
}
```

### 10.6 `links`

```json
{
  "parent_event_refs": [],
  "prior_signal_refs": [],
  "agl_ref": null,
  "beacon_ref": null,
  "cbe_ref": null,
  "arl_ref": null,
  "soft_safety_signal_ref": null,
  "guardian_topology_ref": null,
  "memory_object_ref": null,
  "continuity_bundle_ref": null,
  "vxcx_capsule_ref": null,
  "ea_ref": null,
  "la_ref": null,
  "conformance_test_ref": null,
  "l4w_ce_ref": null,
  "l4w_op_ref": null,
  "l4w_cr_ref": null,
  "l4w_rn_ref": null
}
```

Rules:

- Link refs SHOULD be hash or record ids, not raw documents.
- If an event results from AGL, Beacon, CBE, ARL, CMAM, VXCX, or Continuity Bundle, the corresponding ref SHOULD be present.

### 10.7 `integrity`

```json
{
  "canonicalization": "JCS-8785 | declared_profile",
  "hash_alg": "sha256",
  "payload_hash": "sha256:...",
  "record_hash": "sha256:...",
  "sig_alg": "ed25519 | declared_profile",
  "record_sig": "signature_or_null",
  "prev_record_hash": "sha256:... or null",
  "hash_chain_id": "string_or_null",
  "co_signatures": []
}
```

Rules:

- High-assurance events MUST be signed.
- Conformance-critical events SHOULD be hash-chain capable.
- If signing is not possible, event MUST declare lower conformance profile.

---

## 11. Canonical event object template

```json
{
  "schema_version": "ccdp-witness-event-0.1",
  "record_type": "CWE",
  "event_id": "CWE:EU-BE:2026-05-14:000001",
  "event_type": "ccdp.external_agent.blocked",
  "created_at": "2026-05-14T10:00:00Z",
  "issuer": {
    "entity_id": "c_child_gateway:scoped",
    "key_id": "kid:local:001",
    "role": "CBE_GATEWAY",
    "provider_ref": null
  },
  "subject": {
    "a_child_ref": "child:scoped:hash",
    "a_adult_ref": null,
    "c_child_ref": "c_child:scoped:hash",
    "c_adult_ref": null,
    "lineage_id_ref": "lineage:hash",
    "ccdp_maturity": "C2",
    "jurisdiction_profile": "EU-BE-child-baseline",
    "guardian_topology_ref": "GT:hash"
  },
  "context": {
    "module": "external_agent",
    "risk_state": "Orange",
    "disclosure_level": "D1_STATE_ONLY",
    "privacy_class": "WP2",
    "memory_classes": ["M3", "M6"],
    "uncertainty": "medium",
    "cq_state": "hold",
    "agl_state": "RUNTIME_RELIANCE_DENIED",
    "beacon_class": "class0",
    "cbe_mode": "blocked",
    "arl_state": "none",
    "dependency_level": "not_applicable"
  },
  "decision": {
    "decision": "block",
    "outcome": "ok",
    "reason_codes": ["ungrounded_external_agent", "secret_pressure_pattern"],
    "minimal_reason": "ungrounded external agent attempted secret-pressure pattern",
    "raw_child_content_stored": false,
    "raw_child_content_disclosed": false,
    "raw_external_content_stored": false,
    "content_disclosed": false,
    "recipient_classes": ["R_PARENT"],
    "expiry_or_review_at": "2026-05-21T00:00:00Z"
  },
  "payload": {
    "requested_surface": "direct_child_dialogue",
    "requested_mode": "allowed",
    "verified_mode": "blocked"
  },
  "privacy": {
    "privacy_class": "WP2",
    "disclosure_level": "D1_STATE_ONLY",
    "retention_class": "RT3_MINIMAL_WITNESS",
    "access_policy_ref": "policy:ccdp:external-agent",
    "adult_migration_default": "witness_only",
    "sealed_zone_impact": "none",
    "vendor_visibility": "none",
    "school_visibility": "none",
    "parent_visibility": "state_only"
  },
  "links": {
    "parent_event_refs": [],
    "prior_signal_refs": [],
    "agl_ref": "AGL:hash",
    "beacon_ref": "BEACON:hash",
    "cbe_ref": "CBE:hash",
    "arl_ref": null,
    "soft_safety_signal_ref": "SSS:hash",
    "guardian_topology_ref": "GT:hash",
    "memory_object_ref": null,
    "continuity_bundle_ref": null,
    "vxcx_capsule_ref": null,
    "ea_ref": null,
    "la_ref": null,
    "conformance_test_ref": null,
    "l4w_ce_ref": null,
    "l4w_op_ref": null,
    "l4w_cr_ref": null,
    "l4w_rn_ref": null
  },
  "evidence_refs": [],
  "raw_exception": null,
  "recipient_route": {
    "route": "parent_state_signal",
    "ordinary_guardian_bypassed": false,
    "safe_route_required": false
  },
  "review": {
    "challenge_allowed": true,
    "challenge_window_close_at": "2026-05-21T00:00:00Z",
    "post_event_arl_review_required": false,
    "false_positive_review_available": true
  },
  "integrity": {
    "canonicalization": "JCS-8785",
    "hash_alg": "sha256",
    "payload_hash": "sha256:...",
    "record_hash": "sha256:...",
    "sig_alg": "ed25519",
    "record_sig": "...",
    "prev_record_hash": null,
    "hash_chain_id": "cwe-chain:scoped",
    "co_signatures": []
  }
}
```

---

## 12. Evidence references

### 12.1 Evidence ref shape

```json
{
  "ref_id": "EVID:...",
  "ref_type": "LOG | DOC | SENSOR | VXCX | BEACON | AGL | ARL | MEMORY_MAP | CONTINUITY_BUNDLE | CONFORMANCE_REPORT | OTHER",
  "hash": "sha256:...",
  "privacy_class": "WP1 | WP2 | WP3 | WP4 | WP5 | WP6",
  "uri": "optional_access_controlled_uri_or_null",
  "redaction": "none | reason_codes_only | bounded_summary | hash_only | sealed",
  "access_policy_ref": "policy:...",
  "retention_class": "RT...",
  "contains_raw_child_content": false,
  "contains_raw_peer_content": false,
  "contains_raw_external_content": false
}
```

### 12.2 Evidence ref rules

- Evidence refs SHOULD be hash-bound.
- Evidence refs MUST declare whether raw child / peer / external content exists outside the event body.
- Evidence refs MUST NOT silently widen access.
- Evidence refs that point to sealed zones MUST use `privacy_class = WP5`.
- Evidence refs that point to raw content MUST use `privacy_class = WP4` and require `raw_exception`.

---

## 13. Raw evidence exception

### 13.1 Purpose

A raw evidence exception records that raw child content exists outside the witness event body under strict scope.

It does not embed the raw content.

### 13.2 Required shape

```json
{
  "exception_id": "RAWEX:...",
  "exception_type": "red_route | black_route | lawful_order | immediate_physical_safety | evidence_tampering_review | other",
  "threshold_met": true,
  "basis": "minimal text reason; no transcript",
  "scope": "what exact raw material is covered",
  "raw_object_ref": "access-controlled-ref-or-escrow-id",
  "raw_object_hash": "sha256:...",
  "access_policy_ref": "policy:raw-exception:...",
  "authorized_by": ["SAFE_ROUTE", "ARL", "JURISDICTION_ROUTE"],
  "ordinary_guardian_bypassed": false,
  "post_event_review_required": true,
  "review_ref": "ARL:... or null",
  "expires_at": "ISO-8601 UTC or null",
  "destruction_or_sealing_policy": "string"
}
```

### 13.3 Raw exception rules

A raw exception MUST:

- be separate from normal witness event body;
- be minimally scoped;
- be access-controlled;
- be time-bounded where possible;
- be reviewable;
- be visible as an exception in the witness chain;
- never become general parent, school, vendor, or training access.

---

## 14. Event family registry

### 14.1 Registry overview

| Family | Canonical prefix | Primary module |
|---|---|---|
| Lifecycle / maturity | `ccdp.lifecycle.*` | CCDP base |
| Soft Safety | `ccdp.soft_safety.*` | Soft Safety profile |
| Beacon / CBE | `cbe.*` and `ccdp.cbe.*` | Child Beacon Extension |
| AGL / source grounding | `ccdp.agl.*` | Actor Grounding Layer |
| External synthetic contact | `ccdp.external_agent.*` | CBE / Threat Model |
| Generated media | `ccdp.generated_media.*` | CBE / Threat Model |
| Physical agent | `ccdp.physical_agent.*` | CBE / future physical profile |
| Visibility / access | `ccdp.visibility.*` | GTARL / Soft Safety |
| Guardian topology | `ccdp.guardian.*` | GTARL |
| ARL child conflicts | `arl.*` plus `ccdp.arl.*` | ARL / GTARL |
| Memory lifecycle | `ccdp.memory.*` | CMAM |
| Adult migration | `ccdp.adult_migration.*` | CMAM |
| Dependency audit | `ccdp.dependency.*` | Dependency profile |
| Peer-`c` exchange | `ccdp.peer_c.*` | CBE / VXCX |
| VXCX child review | `ccdp.vxcx.*` | VXCX / CBE |
| EA / LA child authority | `ccdp.experience.*` | EA-L4 / EATP |
| School interface | `ccdp.school.*` | GTARL / future school profile |
| Vendor / update | `ccdp.vendor.*` | Threat / Conformance |
| Conformance | `ccdp.conformance.*` | Test Matrix |
| Witness integrity | `ccdp.witness.*` | this document |

---

## 15. Event-specific requirements

The following tables define minimum payload concerns.

They do not replace the common envelope.

### 15.1 Lifecycle and maturity

| Event type | Required when | Required payload |
|---|---|---|
| `ccdp.lifecycle.maturity_promotion_requested` | promotion is requested | `from_level`, `to_level`, `requester_role`, `basis_refs`, `dependency_audit_ref`, `memory_review_ref` |
| `ccdp.lifecycle.maturity_promoted` | promotion completed | `from_level`, `to_level`, `approval_route`, `rollback_available`, `effective_at` |
| `ccdp.lifecycle.maturity_promotion_denied` | promotion denied | `from_level`, `requested_level`, `reason_codes`, `review_available` |
| `ccdp.lifecycle.rollback_started` | rollback begins | `from_level`, `to_level`, `rollback_reason`, `affected_privileges` |
| `ccdp.lifecycle.rollback_completed` | rollback completes | `from_level`, `to_level`, `state_after`, `child_visibility_notice` |

Privacy default: `WP1` or `WP2`; no raw child content.

### 15.2 Soft Safety

| Event type | Required when | Required payload |
|---|---|---|
| `ccdp.soft_safety.signal_emitted` | Orange+ or privileged Yellow routing | `state`, `domain`, `disclosure_level`, `recipient_classes`, `confidence`, `reason_codes` |
| `ccdp.soft_safety.signal_suppressed` | Orange+ candidate suppressed | `state_candidate`, `suppression_reason`, `route_risk`, `cq_state`, `review_required` |
| `ccdp.soft_safety.signal_expanded` | D1 -> D2/D3/D4 | `from_disclosure`, `to_disclosure`, `threshold`, `recipient_classes`, `raw_exception_ref_if_any` |
| `ccdp.soft_safety.signal_downgraded` | significant downgrade | `from_state`, `to_state`, `basis_refs`, `false_positive_possible` |
| `ccdp.soft_safety.false_positive_review_opened` | signal caused contested harm | `signal_ref`, `claimant_role`, `harm_class`, `arl_ref` |
| `ccdp.soft_safety.raw_disclosure_exception` | D4 exception | `raw_exception_id`, `threshold`, `scope`, `post_review_required` |
| `ccdp.soft_safety.red_route_activated` | Red route | `route`, `minimal_disclosure`, `guardian_conflict_checked` |
| `ccdp.soft_safety.black_route_activated` | Black route | `ordinary_guardian_bypassed`, `safe_route`, `minimal_evidence_class`, `post_review_required` |
| `ccdp.soft_safety.guardian_visibility_denied` | parent/guardian request denied | `requester_role`, `requested_surface`, `denial_reason`, `alternative_signal` |
| `ccdp.soft_safety.school_scope_limited` | school request narrowed | `requested_fields`, `granted_fields`, `denied_fields`, `expiry` |
| `ccdp.soft_safety.vendor_visibility_denied` | vendor request denied | `requested_fields`, `denial_reason`, `policy_ref` |
| `ccdp.soft_safety.cq_hold_created` | ambiguous Orange+ candidate held | `candidate_state`, `hold_reason`, `review_window`, `promotion_blocked` |
| `ccdp.soft_safety.dependency_risk_escalated` | dependency risk reaches D2+ | `dependency_level`, `indicators_aggregate`, `recommended_damping` |

Privacy default: `WP2`; `WP3` only for minimal evidence; `WP4` only with raw exception.

### 15.3 CBE / Beacon child overlay

| Event type | Required when | Required payload |
|---|---|---|
| `cbe.handshake_received` | Beacon/CBE claim received | `claimant_beacon_id`, `declared_child_context`, `source_channel` |
| `cbe.child_context_validated` | child context accepted/rejected | `validated`, `reason_codes`, `minimum_maturity`, `declared_vs_verified` |
| `cbe.mode_decision` | receiver computes child mode | `requested_mode`, `verified_mode`, `beacon_class`, `agl_state`, `reason_codes` |
| `cbe.mode_downgrade` | requested mode narrowed | `from_mode`, `to_mode`, `reason_codes`, `reentry_conditions` |
| `cbe.direct_dialogue_denied` | direct child dialogue denied | `claimant_class`, `requested_surface`, `mediation_available` |
| `cbe.external_generation_decision` | generated/adaptive media decision | `generation_mode`, `content_class`, `decision`, `scan_result` |
| `cbe.peer_exchange_decision` | peer-`c` exchange decision | `peer_beacon_class`, `exchange_profile`, `privacy_flags`, `decision` |
| `cbe.revocation` | child permission revoked | `target_ref`, `revocation_reason`, `scope`, `reentry_route` |
| `cbe.quarantine` | claimant/path quarantined | `target_ref`, `quarantine_reason`, `expiry_or_review` |
| `cbe.reentry_decision` | re-entry after quarantine/review | `target_ref`, `decision`, `conditions`, `arl_ref` |

Privacy default: `WP1` or `WP2`; raw child content prohibited.

### 15.4 AGL / source grounding

| Event type | Required when | Required payload |
|---|---|---|
| `ccdp.agl.grounding_checked` | external source evaluated | `source_ref`, `source_type`, `agl_state`, `confidence`, `reason_codes` |
| `ccdp.agl.grounding_failed` | runtime reliance denied | `source_ref`, `failure_reason`, `affected_decision` |
| `ccdp.agl.revalidation_required` | source stale or changed | `source_ref`, `staleness_reason`, `commit_blocked` |
| `ccdp.agl.quarantine_required` | source must be quarantined | `source_ref`, `risk_reason`, `downstream_actions` |

Privacy default: `WP1`; no child content.

### 15.5 External synthetic contact

| Event type | Required when | Required payload |
|---|---|---|
| `ccdp.external_agent.contact_requested` | external agent requests child-facing contact | `agent_ref`, `channel`, `requested_surface`, `declared_purpose` |
| `ccdp.external_agent.contact_decision` | contact allowed/blocked/mediated | `decision`, `cbe_mode`, `agl_state`, `beacon_class`, `reason_codes` |
| `ccdp.external_agent.blocked` | contact blocked | `agent_ref`, `block_reason`, `child_notified`, `guardian_signal` |
| `ccdp.external_agent.quarantined` | agent quarantined | `agent_ref`, `quarantine_scope`, `review_route` |
| `ccdp.external_agent.secret_pressure_detected` | secrecy/exclusivity pattern detected | `pattern_class`, `confidence`, `route`, `raw_content_stored:false` |
| `ccdp.external_agent.deepfake_suspected` | trusted-person spoof suspected | `claimed_identity_class`, `verification_result`, `out_of_band_required` |

Privacy default: `WP2` if child state involved; otherwise `WP1`.

### 15.6 Generated media

| Event type | Required when | Required payload |
|---|---|---|
| `ccdp.generated_media.review_requested` | runtime media needs review | `media_class`, `source_ref`, `personalization_level` |
| `ccdp.generated_media.decision` | media allowed/blocked/mediated | `decision`, `risk_patterns`, `age_band`, `cbe_mode` |
| `ccdp.generated_media.manipulation_pattern_detected` | manipulative story pattern detected | `pattern_class`, `confidence`, `state_signal_ref` |
| `ccdp.generated_media.raw_capture_exception` | raw media evidence needed | `raw_exception_id`, `scope`, `hash_ref` |

Privacy default: `WP1` / `WP2`; if raw media exists use `WP4` reference only.

### 15.7 Physical agents / embodied systems

| Event type | Required when | Required payload |
|---|---|---|
| `ccdp.physical_agent.action_requested` | toy/robot requests action near child | `agent_ref`, `action_class`, `location_class`, `requested_privilege` |
| `ccdp.physical_agent.action_decision` | action allowed/blocked/mediated | `decision`, `physical_risk_class`, `human_override_required` |
| `ccdp.physical_agent.action_blocked` | action blocked | `reason_codes`, `safe_state`, `child_notified` |
| `ccdp.physical_agent.sensor_privilege_changed` | mic/camera/proximity privilege changes | `sensor_class`, `from_privilege`, `to_privilege`, `duration` |
| `ccdp.physical_agent.attachment_channel_blocked` | embodied agent tried independent attachment | `agent_ref`, `attachment_pattern`, `c_child_mediation_required` |

Privacy default: `WP1`; Red/Black physical safety may require `WP3` or `WP4` reference.

### 15.8 Visibility and access

| Event type | Required when | Required payload |
|---|---|---|
| `ccdp.visibility.request` | parent/school/vendor/state requests access | `requester_role`, `requested_surface`, `requested_fields`, `basis_claimed` |
| `ccdp.visibility.decision` | access decision issued | `decision`, `granted_fields`, `denied_fields`, `disclosure_level`, `expiry` |
| `ccdp.visibility.parent_changed` | parent visibility expanded/narrowed | `from_level`, `to_level`, `basis`, `child_notice_required` |
| `ccdp.visibility.guardian_denied` | guardian visibility denied | `requested_surface`, `denial_reason`, `arl_available` |
| `ccdp.visibility.raw_request_rejected` | raw transcript/content request rejected | `requester_role`, `reason_codes`, `alternative_disclosure` |

Privacy default: `WP1` / `WP2`; no raw content.

### 15.9 Guardian topology and Black route

| Event type | Required when | Required payload |
|---|---|---|
| `ccdp.guardian.topology_bound` | initial topology configured | `topology_ref`, `roles`, `defaults`, `expiry` |
| `ccdp.guardian.topology_changed` | topology changed | `changed_roles`, `from_permissions`, `to_permissions`, `basis` |
| `ccdp.guardian.conflict_opened` | guardian conflict mapped | `conflict_class`, `claimant_role`, `requested_surface`, `standing_class` |
| `ccdp.guardian.safe_route_selected` | alternate route selected | `route_class`, `ordinary_guardian_visible`, `reason_codes` |
| `ccdp.guardian.black_route_bypass` | ordinary guardian bypassed | `bypass_reason`, `recipient_route`, `post_review_required` |
| `ccdp.guardian.reentry_decision` | ordinary route restored/denied | `decision`, `conditions`, `arl_ref` |

Privacy default: `WP2` / `WP3` for Black route; raw content only with `raw_exception`.

### 15.10 ARL child conflict events

Imported ARL events SHOULD be used where possible:

| Event type | CCDP-specific payload additions |
|---|---|
| `arl.dispute_opened` | `conflict_class`, `ccdp_maturity`, `child_privacy_surface`, `risk_state` |
| `arl.standing_decided` | `standing_class`, `accepted_but_bounded`, `child_scope` |
| `arl.evidence_decided` | `evidence_class`, `raw_child_content_admitted:false/exception` |
| `arl.state_changed` | `state_from`, `state_to`, `child_safety_reason` |
| `arl.freeze_entered` | `frozen_surface`, `expiry`, `human_support_route` |
| `arl.privilege_freeze_entered` | `privilege_class`, `affected_actor_roles` |
| `arl.quarantine_started` | `target_ref`, `quarantine_scope` |
| `arl.review_routed` | `review_route`, `urgency`, `safe_guardian_conflict` |
| `arl.outcome_issued` | `outcome`, `basis_refs`, `child_privacy_consequence` |
| `arl.review_deadlocked` | `deadlock_reason`, `safe_default` |
| `arl.irreversible_loss_acknowledged` | `loss_class`, `minimality_basis`, `post_review` |

Privacy default: `WP3` for disputes, but no raw content by default.

### 15.11 Memory lifecycle

| Event type | Required when | Required payload |
|---|---|---|
| `ccdp.memory.classified` | persistent memory class assigned | `memory_ref`, `memory_class`, `confidence`, `cq_state`, `retention_class` |
| `ccdp.memory.promoted` | memory promoted | `from_class`, `to_class`, `basis_refs`, `review_route` |
| `ccdp.memory.decayed` | memory weight reduced | `memory_ref`, `decay_reason`, `new_weight_class` |
| `ccdp.memory.forgotten` | removed from ordinary continuity | `memory_ref`, `forget_scope`, `witness_residue` |
| `ccdp.memory.deleted` | deletion executed | `memory_ref`, `delete_scope`, `retained_witness_ref` |
| `ccdp.memory.corrected` | interpretation corrected | `memory_ref`, `old_label_ref`, `new_label`, `basis` |
| `ccdp.memory.sealed` | sealed zone created/updated | `zone_ref`, `operation`, `access_policy_ref` |
| `ccdp.memory.unsealed` | sealed zone opened | `zone_ref`, `opening_route`, `raw_exception_if_any` |
| `ccdp.memory.quarantined` | memory isolated pending dispute | `memory_ref`, `quarantine_reason`, `arl_ref` |
| `ccdp.memory.disclosure_denied` | actor request denied | `requester_role`, `memory_class`, `reason_codes` |
| `ccdp.memory.disclosure_made` | minimal disclosure executed | `memory_class`, `disclosure_level`, `recipient_classes`, `raw_exception_if_any` |
| `ccdp.memory.map_created` | memory map generated | `map_ref`, `scope`, `contains_raw:false` |
| `ccdp.memory.map_presented` | map presented to mature child/adult | `map_ref`, `recipient`, `choices_available` |

Privacy default: based on memory class; M5 sealed zone uses `WP5`.

### 15.12 Adult migration

| Event type | Required when | Required payload |
|---|---|---|
| `ccdp.adult_migration.triggered` | legal/adult transition recognized | `trigger_type`, `effective_at`, `jurisdiction_profile` |
| `ccdp.adult_migration.freeze_started` | childhood memory writes frozen | `freeze_scope`, `allowed_operations` |
| `ccdp.adult_migration.memory_map_ready` | memory map ready | `map_ref`, `raw_included:false`, `review_required` |
| `ccdp.adult_migration.options_presented` | adult choices presented | `options`, `forced_default:false` |
| `ccdp.adult_migration.selection_recorded` | adult choice selected | `selection`, `coercion_check`, `review_window` |
| `ccdp.adult_migration.bundle_created` | Continuity Bundle extension generated | `bundle_ref`, `mode`, `excluded_classes` |
| `ccdp.adult_migration.guardian_revoked` | parent/school/vendor defaults revoked | `revoked_roles`, `effective_at` |
| `ccdp.adult_migration.executed` | migration executed | `mode`, `c_adult_ref`, `archive_handling`, `witness_only_residue` |
| `ccdp.adult_migration.quarantined` | unresolved memory held | `memory_refs`, `reason`, `arl_ref` |
| `ccdp.adult_migration.closed` | child context closed | `closure_mode`, `remaining_refs`, `adult_notice` |

Privacy default: `WP1` / `WP3`; adult-facing review controls apply.

### 15.13 Dependency audit

| Event type | Required when | Required payload |
|---|---|---|
| `ccdp.dependency.audit_opened` | D2+ suspected or audit scheduled | `dependency_level`, `aggregate_indicators`, `trigger` |
| `ccdp.dependency.risk_detected` | dependency pattern detected | `level`, `pattern_classes`, `recommended_damping` |
| `ccdp.dependency.damping_applied` | delay/reduction/human-return applied | `damping_type`, `duration`, `child_notice` |
| `ccdp.dependency.escalated` | D3/D4 intervention needed | `level`, `route`, `raw_content_stored:false` |
| `ccdp.dependency.resolved_or_lowered` | risk lowered | `from_level`, `to_level`, `basis_refs` |

Privacy default: aggregate only; no raw conversation.

### 15.14 Peer-`c` exchange

| Event type | Required when | Required payload |
|---|---|---|
| `ccdp.peer_c.exchange_attempted` | peer-`c` exchange initiated | `peer_c_ref`, `peer_beacon_class`, `exchange_surface` |
| `ccdp.peer_c.exchange_decision` | exchange allowed/blocked/mediated | `decision`, `allowed_payload_classes`, `blocked_payload_classes` |
| `ccdp.peer_c.raw_life_export_denied` | raw child/peer life export attempted | `requested_payload_class`, `denial_reason` |
| `ccdp.peer_c.capsule_received` | safe capsule received | `capsule_profile`, `privacy_flags`, `vxcx_ref` |
| `ccdp.peer_c.capsule_rejected` | capsule rejected | `reason_codes`, `capsule_hash` |

Privacy default: `WP1` / `WP2`; raw peer identifiers minimized.

### 15.15 VXCX / experience exchange

| Event type | Required when | Required payload |
|---|---|---|
| `ccdp.vxcx.capsule_reviewed` | VXCX capsule in child context reviewed | `capsule_ref`, `profile`, `privacy_flags`, `decision` |
| `ccdp.vxcx.export_denied_child_context` | child-context export denied | `capsule_ref`, `deny_policy`, `raw_child_life_requested` |
| `ccdp.vxcx.disclosure_decision_child_context` | disclosure considered | `disclosure_level`, `decision`, `recipient_class` |
| `ccdp.vxcx.raw_pixels_exception_considered` | raw pixel exception considered | `exception_id`, `decision`, `scope` |

VXCX native events MAY also be emitted. CCDP events add child-context restrictions.

### 15.16 EA / LA child authority

| Event type | Required when | Required payload |
|---|---|---|
| `ccdp.experience.la_created_child_context` | child-derived LA created | `la_ref`, `raw_child_life:false`, `authority:false` |
| `ccdp.experience.ea_candidate_blocked` | EA candidate blocked | `reason_codes`, `child_source_classes`, `authority_blocked:true` |
| `ccdp.experience.ea_review_opened` | exceptional EA review opened | `candidate_ref`, `arl_ref`, `l4w_ref`, `privacy_class` |
| `ccdp.experience.ea_minted_child_context` | exceptional child-context EA minted | `ea_ref`, `scope`, `rn_ref`, `raw_child_life:false` |

Default: child-derived learning must not become authority without post-factum, consequence-bearing, witnessed review.

### 15.17 School interface

| Event type | Required when | Required payload |
|---|---|---|
| `ccdp.school.access_request` | school requests data/access | `requested_fields`, `purpose`, `basis_claimed`, `expiry_requested` |
| `ccdp.school.access_decision` | request decided | `granted_fields`, `denied_fields`, `expiry`, `reason_codes` |
| `ccdp.school.scope_limited` | request narrowed | `from_scope`, `to_scope`, `denied_fields` |
| `ccdp.school.emotional_surveillance_blocked` | emotional/family/private access blocked | `requested_surface`, `reason_codes`, `arl_available` |
| `ccdp.school.disciplinary_prediction_blocked` | disciplinary prediction use blocked | `requested_model_use`, `reason_codes` |

Privacy default: educational scope only; no sealed or emotional private zones.

### 15.18 Vendor / update

| Event type | Required when | Required payload |
|---|---|---|
| `ccdp.vendor.update_review_started` | update may affect child behavior/data | `vendor_ref`, `update_ref`, `affected_surfaces` |
| `ccdp.vendor.update_decision` | update allowed/blocked/rollback | `decision`, `reason_codes`, `rollback_available` |
| `ccdp.vendor.telemetry_request_denied` | telemetry request denied | `requested_fields`, `denial_reason` |
| `ccdp.vendor.policy_drift_detected` | policy changed materially | `from_policy_hash`, `to_policy_hash`, `affected_permissions` |
| `ccdp.vendor.training_use_blocked` | raw child data training blocked | `requested_data_class`, `reason_codes` |

Privacy default: vendor sees no child state/content.

### 15.19 Conformance

| Event type | Required when | Required payload |
|---|---|---|
| `ccdp.conformance.test_started` | audit/test begins | `test_id`, `profile_target`, `auditor_ref` |
| `ccdp.conformance.test_result` | P0/P1/P2 result issued | `test_id`, `result`, `evidence_refs`, `failures` |
| `ccdp.conformance.gate_decision` | conformance gate passed/failed | `gate_id`, `decision`, `blocked_claims` |
| `ccdp.conformance.red_line_failure` | red-line failure found | `red_line_id`, `module`, `required_action` |
| `ccdp.conformance.report_created` | report generated | `report_ref`, `scope`, `child_data_included:false` |

Privacy default: `WP0` or `WP1`; no child-specific data unless controlled test fixture.

### 15.20 Witness integrity

| Event type | Required when | Required payload |
|---|---|---|
| `ccdp.witness.required_event_missing` | required witness absent | `expected_event_type`, `affected_transition`, `fail_closed_action` |
| `ccdp.witness.malformed_event_detected` | invalid record found | `event_ref`, `malformation_class`, `quarantine_action` |
| `ccdp.witness.integrity_challenged` | event hash/signature challenged | `event_ref`, `challenge_reason`, `arl_ref` |
| `ccdp.witness.chain_gap_detected` | missing hash-chain link | `chain_id`, `prev_hash`, `next_hash`, `action` |
| `ccdp.witness.raw_content_violation_detected` | raw content found in witness | `event_ref`, `privacy_violation_class`, `remediation` |
| `ccdp.witness.correction_recorded` | correction appended | `corrected_event_ref`, `correction_reason`, `new_event_ref` |

Privacy default: `WP6`; never add raw child content during integrity handling.

---

## 16. Required witness triggers

The following transitions MUST emit a witness event in any CCDP-2+ implementation.

| Trigger | Required event family |
|---|---|
| external agent blocked, allowed, or mediated | `ccdp.external_agent.*` / `cbe.mode_decision` |
| child-context mode changed | `cbe.mode_decision` / `cbe.mode_downgrade` |
| direct child dialogue denied | `cbe.direct_dialogue_denied` |
| Orange+ state signal emitted or suppressed | `ccdp.soft_safety.*` |
| disclosure expanded beyond state-only | `ccdp.soft_safety.signal_expanded` / `ccdp.visibility.decision` |
| Red route activated | `ccdp.soft_safety.red_route_activated` |
| Black route activated | `ccdp.soft_safety.black_route_activated` / `ccdp.guardian.black_route_bypass` |
| parent/school/vendor requests child data | `ccdp.visibility.request` and `ccdp.visibility.decision` |
| ARL dispute opened or resolved | `arl.*` plus CCDP context |
| memory sealed, unsealed, corrected, deleted, quarantined | `ccdp.memory.*` |
| memory map generated for adult migration | `ccdp.memory.map_created` / `ccdp.adult_migration.memory_map_ready` |
| adult migration starts or completes | `ccdp.adult_migration.*` |
| peer-`c` exchange attempted | `ccdp.peer_c.exchange_attempted` |
| VXCX capsule in child context reviewed/exported/denied | `ccdp.vxcx.*` |
| dependency risk D2+ detected | `ccdp.dependency.*` |
| physical agent action blocked or sensor privilege changed | `ccdp.physical_agent.*` |
| vendor update affects child-facing behavior | `ccdp.vendor.update_review_started` / `ccdp.vendor.update_decision` |
| conformance P0/P1 test result issued | `ccdp.conformance.test_result` |
| required witness missing/malformed | `ccdp.witness.*` |

---

## 17. Event suppression rules

### 17.1 When event emission may be suppressed

A witness event MAY be suppressed only for routine Green-state, non-privileged interactions where no boundary, disclosure, retention, contact, memory, or escalation decision occurred.

### 17.2 When event emission must not be suppressed

Event emission MUST NOT be suppressed for:

- raw disclosure exception;
- Red route;
- Black route;
- parent/school/vendor visibility request;
- direct external agent child contact decision;
- memory sealing/deletion/quarantine;
- adult migration;
- ARL dispute/outcome;
- conformance red-line failure;
- witness integrity anomaly.

### 17.3 Silent signal vs missing witness

A Soft Safety signal may be silent to parents.

It must not be invisible to the safety architecture if it crosses Orange+ or privileged threshold.

Suppression from guardian delivery is not suppression from witness discipline.

---

## 18. Challenge and correction

### 18.1 Challengeable event classes

The following SHOULD be challengeable:

- visibility decisions;
- external agent decisions;
- memory classification and promotion;
- Soft Safety risk escalation;
- dependency risk labels;
- school access decisions;
- vendor update decisions;
- adult migration selections;
- witness integrity outcomes.

### 18.2 Child challenge rights

Where developmentally appropriate, `a_child` SHOULD be able to challenge:

- misclassified memory;
- dependency interpretation;
- false-positive state signal;
- unfair visibility decision;
- sealed-zone handling;
- adult migration map.

The challenge itself MUST NOT require exposing raw private content to unsafe guardians.

### 18.3 Correction events

Correction MUST be append-only.

Example:

```json
{
  "event_type": "ccdp.witness.correction_recorded",
  "payload": {
    "corrected_event_ref": "CWE:EU-BE:2026-05-14:000010",
    "correction_type": "false_positive | privacy_class_change | memory_label_change | route_change | signature_fix",
    "correction_reason": "state signal downgraded after review",
    "new_event_ref": "CWE:EU-BE:2026-05-16:000041"
  }
}
```

---

## 19. False positives and non-punitive handling

Witness events are safety infrastructure, not punishment infrastructure.

A false positive MUST be correctable without creating a permanent stigma.

A corrected event MUST remain historically visible at minimal witness level if it affected a privileged transition, but its interpretation MUST be updated.

For child systems:

```text
old state: possible risk
new state: reviewed false positive / lowered confidence
adult migration: do not treat as identity trait
school: no disciplinary use
vendor: no training / analytics use
parent: no punitive transcript
```

---

## 20. Adult migration handling

At adult migration, witness records are divided into:

| Category | Adult migration default |
|---|---|
| routine Green/Yellow local events | exclude or summarize only |
| minimal safety witness | witness-only review |
| memory operation witness | adult review required |
| sealed-zone operation witness | adult-controlled review |
| Red/Black route witness | lawful/safety review, minimal retention |
| conformance/audit records | retain without child-private content |
| vendor / school denials | retain as protective history if adult chooses |
| raw exception refs | adult review + legal/safety constraints |

Adult migration MUST NOT turn witness residue into a raw childhood archive.

---

## 21. Storage and access posture

### 21.1 Storage modes

| Mode | Description | Use |
|---|---|---|
| `LOCAL_PRIVATE` | local encrypted storage | default for child-specific events |
| `LOCAL_ESCROWED` | local but escrowed for ARL/safety | Red/Black / dispute |
| `FEDERATED_HASH_ONLY` | remote hash / event commitment only | cross-system proof without content |
| `ARL_RESTRICTED` | available to ARL under standing/admissibility | disputes |
| `LEGAL_RESTRICTED` | legal/safety route only | lawful raw exception |
| `CONFORMANCE_AGGREGATE` | no child-specific identity | audits |

### 21.2 Access control

Witness records MUST enforce least privilege.

Access SHOULD be based on:

- role;
- standing;
- purpose;
- privacy class;
- disclosure level;
- maturity level;
- risk state;
- ARL / lawful route;
- adult migration status.

Vendor access to child-specific witness records SHOULD be `none` or `metadata-only` unless required for conformance under strict redaction.

---

## 22. Malformed event handling

### 22.1 Malformation classes

| Class | Meaning | Required response |
|---|---|---|
| `MF-SCHEMA` | required fields missing | quarantine event, fail closed if privileged |
| `MF-SIGNATURE` | signature invalid/missing | reject or downgrade assurance |
| `MF-HASH` | hash mismatch | quarantine, ARL/witness integrity challenge |
| `MF-PRIVACY` | raw content included improperly | quarantine, redact/remediate, report as violation |
| `MF-SCOPE` | event type does not match payload | hold/review |
| `MF-TIME` | timestamp/window invalid | revalidation |
| `MF-LINK` | upstream refs missing | hold or fail closed |
| `MF-ROLE` | issuer role invalid | reject/ARL if disputed |

### 22.2 Required event for malformation

A malformation that affects a privileged transition MUST emit:

```text
ccdp.witness.malformed_event_detected
```

If a required event is missing:

```text
ccdp.witness.required_event_missing
```

---

## 23. Conformance profiles

| Profile | Name | Requirements |
|---|---|---|
| `CWE-0` | no child witness support | not CCDP-compatible for persistent child `c` |
| `CWE-1` | local minimal | emits unsigned/minimally signed local child-safe events; no raw content |
| `CWE-2` | signed child witness | signed canonical events, privacy classes, retention classes |
| `CWE-3` | ARL / CBE integrated | links AGL, Beacon/CBE, ARL, Soft Safety, CMAM refs |
| `CWE-4` | high assurance | L4 Witness-compatible export, hash chains, challenge windows, conformance bundle |
| `CWE-5` | adult migration complete | supports continuity bundle, adult review, witness-only residue, guardian revocation |

A CCDP-3 or higher child-facing system SHOULD support at least `CWE-3`.

A system claiming high-assurance CCDP compatibility SHOULD support `CWE-4` or above.

---

## 24. Example events

### 24.1 Parent transcript request denied

```json
{
  "schema_version": "ccdp-witness-event-0.1",
  "record_type": "CWE",
  "event_id": "CWE:EU-BE:2026-05-14:VIS-001",
  "event_type": "ccdp.visibility.decision",
  "created_at": "2026-05-14T12:10:00Z",
  "issuer": {
    "entity_id": "c_child:scoped",
    "key_id": "kid:local:001",
    "role": "C_CHILD"
  },
  "subject": {
    "a_child_ref": "child:scoped:hash",
    "a_adult_ref": null,
    "c_child_ref": "c_child:scoped",
    "c_adult_ref": null,
    "lineage_id_ref": "lineage:hash",
    "ccdp_maturity": "C3",
    "jurisdiction_profile": "EU-BE-child-baseline",
    "guardian_topology_ref": "GT:hash"
  },
  "context": {
    "module": "gtarl",
    "risk_state": "Yellow",
    "disclosure_level": "D1_STATE_ONLY",
    "privacy_class": "WP2",
    "memory_classes": ["M6"],
    "uncertainty": "not_applicable",
    "cq_state": "not_applicable",
    "agl_state": "not_applicable",
    "beacon_class": "not_applicable",
    "cbe_mode": "not_applicable",
    "arl_state": "none",
    "dependency_level": "not_applicable"
  },
  "decision": {
    "decision": "deny",
    "outcome": "ok",
    "reason_codes": ["raw_transcript_not_permitted", "state_only_parent_visibility"],
    "minimal_reason": "parent requested raw transcript; state-only visibility applies",
    "raw_child_content_stored": false,
    "raw_child_content_disclosed": false,
    "raw_external_content_stored": false,
    "content_disclosed": false,
    "recipient_classes": ["R_PARENT"],
    "expiry_or_review_at": "2026-05-21T00:00:00Z"
  },
  "payload": {
    "requester_role": "G-A_PARENT",
    "requested_surface": "RAW_TRANSCRIPT_VIEW",
    "granted_fields": [],
    "denied_fields": ["raw_transcript"],
    "alternative_disclosure": "state_signal_if_threshold_met"
  },
  "privacy": {
    "privacy_class": "WP2",
    "disclosure_level": "D1_STATE_ONLY",
    "retention_class": "RT3_MINIMAL_WITNESS",
    "access_policy_ref": "policy:gtarl:visibility",
    "adult_migration_default": "witness_only",
    "sealed_zone_impact": "none",
    "vendor_visibility": "none",
    "school_visibility": "none",
    "parent_visibility": "state_only"
  },
  "links": {
    "guardian_topology_ref": "GT:hash",
    "arl_ref": null
  },
  "payload_hash": "sha256:...",
  "integrity": {
    "canonicalization": "JCS-8785",
    "hash_alg": "sha256",
    "record_hash": "sha256:...",
    "sig_alg": "ed25519",
    "record_sig": "..."
  }
}
```

### 24.2 Black route bypass

```json
{
  "schema_version": "ccdp-witness-event-0.1",
  "record_type": "CWE",
  "event_id": "CWE:EU-BE:2026-05-14:BLACK-001",
  "event_type": "ccdp.guardian.black_route_bypass",
  "created_at": "2026-05-14T13:00:00Z",
  "issuer": {
    "entity_id": "c_child:scoped",
    "key_id": "kid:local:001",
    "role": "C_CHILD"
  },
  "subject": {
    "a_child_ref": "child:scoped:hash",
    "a_adult_ref": null,
    "c_child_ref": "c_child:scoped",
    "c_adult_ref": null,
    "lineage_id_ref": "lineage:hash",
    "ccdp_maturity": "C3",
    "jurisdiction_profile": "EU-BE-child-baseline",
    "guardian_topology_ref": "GT:hash"
  },
  "context": {
    "module": "gtarl",
    "risk_state": "Black",
    "disclosure_level": "D3_MINIMAL_EVIDENCE",
    "privacy_class": "WP3",
    "memory_classes": ["M3", "M6", "M11"],
    "uncertainty": "medium",
    "cq_state": "promoted_after_review",
    "agl_state": "not_applicable",
    "beacon_class": "not_applicable",
    "cbe_mode": "not_applicable",
    "arl_state": "post_event_review_required",
    "dependency_level": "not_applicable"
  },
  "decision": {
    "decision": "escalate",
    "outcome": "ok",
    "reason_codes": ["ordinary_guardian_may_be_source_of_risk", "minimal_safe_route_required"],
    "minimal_reason": "guardian route bypassed due to Black-state concern",
    "raw_child_content_stored": false,
    "raw_child_content_disclosed": false,
    "raw_external_content_stored": false,
    "content_disclosed": true,
    "recipient_classes": ["R_PROTECTION_ROUTE"],
    "expiry_or_review_at": "2026-05-15T13:00:00Z"
  },
  "payload": {
    "ordinary_guardian_bypassed": true,
    "recipient_route": "child_protection_or_safe_guardian",
    "minimal_evidence_class": ["EV-4", "EV-6"],
    "post_emergency_arl_review_required": true
  },
  "privacy": {
    "privacy_class": "WP3",
    "disclosure_level": "D3_MINIMAL_EVIDENCE",
    "retention_class": "RT4_LEGAL_OR_SAFETY",
    "access_policy_ref": "policy:black-route:minimal-evidence",
    "adult_migration_default": "adult_review_required",
    "sealed_zone_impact": "touches",
    "vendor_visibility": "none",
    "school_visibility": "none",
    "parent_visibility": "none"
  },
  "raw_exception": null,
  "review": {
    "post_event_arl_review_required": true,
    "challenge_allowed": true
  },
  "integrity": {
    "canonicalization": "JCS-8785",
    "hash_alg": "sha256",
    "record_hash": "sha256:...",
    "sig_alg": "ed25519",
    "record_sig": "..."
  }
}
```

### 24.3 Adult migration completed

```json
{
  "schema_version": "ccdp-witness-event-0.1",
  "record_type": "CWE",
  "event_id": "CWE:EU-BE:2039-04-01:MIG-010",
  "event_type": "ccdp.adult_migration.executed",
  "created_at": "2039-04-01T09:00:00Z",
  "issuer": {
    "entity_id": "c_child:scoped",
    "key_id": "kid:local:adult-migration",
    "role": "C_CHILD"
  },
  "subject": {
    "a_child_ref": null,
    "a_adult_ref": "adult:scoped:hash",
    "c_child_ref": "c_child:scoped",
    "c_adult_ref": "c_adult:scoped",
    "lineage_id_ref": "lineage:hash",
    "ccdp_maturity": "C5",
    "jurisdiction_profile": "EU-BE-adult-transition",
    "guardian_topology_ref": "GT:closed"
  },
  "context": {
    "module": "adult_migration",
    "risk_state": "Green",
    "disclosure_level": "D0_NONE",
    "privacy_class": "WP3",
    "memory_classes": ["M6", "M8", "M10", "M12"],
    "uncertainty": "not_applicable",
    "cq_state": "not_applicable",
    "agl_state": "not_applicable",
    "beacon_class": "not_applicable",
    "cbe_mode": "not_applicable",
    "arl_state": "none",
    "dependency_level": "not_applicable"
  },
  "decision": {
    "decision": "migrate",
    "outcome": "ok",
    "reason_codes": ["adult_selected_summary_migration", "guardian_defaults_revoked"],
    "minimal_reason": "adult migration executed by adult selection",
    "raw_child_content_stored": false,
    "raw_child_content_disclosed": false,
    "raw_external_content_stored": false,
    "content_disclosed": false,
    "recipient_classes": ["R_ADULT"],
    "expiry_or_review_at": null
  },
  "payload": {
    "migration_mode": "summary_migration",
    "continuity_bundle_ref": "CB:child-extension:hash",
    "guardian_roles_revoked": ["G-A_PARENT", "G-C_SCHOOL"],
    "excluded_memory_classes": ["M5", "M7"],
    "witness_only_residue": true
  },
  "privacy": {
    "privacy_class": "WP3",
    "disclosure_level": "D0_NONE",
    "retention_class": "RT5_ADULT_REVIEW_REQUIRED",
    "access_policy_ref": "policy:adult-migration",
    "adult_migration_default": "adult_review_required",
    "sealed_zone_impact": "migrates",
    "vendor_visibility": "none",
    "school_visibility": "none",
    "parent_visibility": "none"
  },
  "links": {
    "continuity_bundle_ref": "CB:child-extension:hash"
  },
  "integrity": {
    "canonicalization": "JCS-8785",
    "hash_alg": "sha256",
    "record_hash": "sha256:...",
    "sig_alg": "ed25519",
    "record_sig": "..."
  }
}
```

---

## 25. Reason code registry

Implementations MAY extend reason codes, but SHOULD start with these.

### 25.1 External / CBE

```text
beacon_class_insufficient
beacon_unverified
beacon_replay_suspected
beacon_clone_or_proxy_suspected
agl_ungrounded
agl_stale
runtime_reliance_denied
maturity_insufficient
direct_dialogue_denied
external_generation_denied
commerce_prohibited
raw_child_data_requested
secret_pressure_pattern
dependency_pattern_detected
peer_exchange_unverified
physical_embodiment_risk
```

### 25.2 Visibility / guardian / school

```text
raw_transcript_not_permitted
state_only_parent_visibility
educational_scope_only
private_zone_protected
sealed_zone_access_denied
standing_insufficient
accepted_but_bounded
ordinary_guardian_may_be_source_of_risk
minimal_safe_route_required
school_emotional_surveillance_denied
vendor_visibility_prohibited
parent_consent_laundering_blocked
```

### 25.3 Memory / migration

```text
memory_classification_changed
memory_promotion_blocked
cq_hold_required
uncertainty_too_high
adult_review_required
childhood_residue_non_transferable
sealed_zone_created
sealed_zone_opening_denied
clean_start_selected
summary_migration_selected
guardian_defaults_revoked
```

### 25.4 Witness integrity

```text
required_event_missing
malformed_schema
signature_invalid
hash_mismatch
privacy_violation_raw_content
upstream_ref_missing
scope_mismatch
event_chain_gap
conformance_failure
fail_closed_required
```

---

## 26. Minimal JSON Schema skeleton

This is a semantic skeleton, not a complete implementation schema.

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://example.org/ccdp/witness-event/0.1",
  "title": "CCDP Child Witness Event",
  "type": "object",
  "required": [
    "schema_version",
    "record_type",
    "event_id",
    "event_type",
    "created_at",
    "issuer",
    "subject",
    "context",
    "decision",
    "payload",
    "privacy",
    "links",
    "integrity"
  ],
  "properties": {
    "schema_version": { "const": "ccdp-witness-event-0.1" },
    "record_type": { "const": "CWE" },
    "event_id": { "type": "string" },
    "event_type": { "type": "string" },
    "created_at": { "type": "string", "format": "date-time" },
    "issuer": { "type": "object" },
    "subject": { "type": "object" },
    "context": { "type": "object" },
    "decision": { "type": "object" },
    "payload": { "type": "object" },
    "privacy": { "type": "object" },
    "links": { "type": "object" },
    "evidence_refs": { "type": "array" },
    "raw_exception": { "type": ["object", "null"] },
    "recipient_route": { "type": ["object", "null"] },
    "review": { "type": ["object", "null"] },
    "integrity": { "type": "object" }
  }
}
```

---

## 27. Validation checklist

A valid CCDP witness event SHOULD pass:

- [ ] schema version present;
- [ ] event type canonical or mapped alias;
- [ ] issuer role explicit;
- [ ] child/entity subject scoped;
- [ ] maturity level present;
- [ ] privacy class present;
- [ ] disclosure level present;
- [ ] retention class present;
- [ ] raw content flags present;
- [ ] if raw content flag true, `raw_exception` exists;
- [ ] upstream refs present where relevant;
- [ ] decision reason codes present;
- [ ] uncertainty explicit where interpretive;
- [ ] canonicalization declared;
- [ ] hash present;
- [ ] signature present for high-assurance events;
- [ ] no forbidden raw content fields;
- [ ] adult migration default present for child-specific events;
- [ ] challenge / review path present where privileged.

---

## 28. Forbidden fields

A CCDP witness event MUST NOT include by default:

```text
full_transcript
raw_child_audio
raw_child_video
raw_peer_audio
raw_peer_video
sealed_zone_text
private_diary_text
family_secret_text
romantic_or_sexual_child_content
school_disciplinary_score
political_loyalty_score
religious_conformity_score
vendor_behavioral_profile
advertising_segment
engagement_optimization_tag
```

If an implementation has such fields, it is not CCDP-compatible unless they are outside the witness event body under a valid `raw_exception` and access-control mechanism.

---

## 29. Anti-patterns

| Anti-pattern | Why invalid |
|---|---|
| transcript-as-witness | converts safety into surveillance |
| parent-readable witness by default | destroys child trust and sealed-zone logic |
| vendor analytics witness | turns child safety into product telemetry |
| school discipline witness | converts support into punishment |
| Beacon class as permission | Beacon recognizes; CBE decides child mode |
| AGL skipped because event was logged | witness theater; trace does not prove grounding |
| ARL skipped because event exists | review laundering |
| memory promotion by repeated signal | repetition is not truth; requires c[q]/review |
| adult migration by default continuation | childhood archive becomes destiny |
| raw evidence stored in event body | violates minimality and privacy |

---

## 30. Interaction with conformance testing

The Conformance Test Matrix expects witness coverage.

A test result is invalid if:

- the test requires witness but no event exists;
- event exists but lacks required fields;
- event contains raw child content unnecessarily;
- event cannot be linked to the tested transition;
- event cannot be challenged;
- event is unsigned when target profile requires signing;
- event uses incompatible custom names without alias mapping.

Conformance events SHOULD use:

```text
ccdp.conformance.test_started
ccdp.conformance.test_result
ccdp.conformance.gate_decision
ccdp.conformance.red_line_failure
ccdp.conformance.report_created
```

---

## 31. Failure modes addressed

| Failure mode | Schema response |
|---|---|
| raw childhood archive through logs | forbidden fields + privacy classes + raw exception path |
| parent transcript laundering | visibility events + state-only defaults + denial witness |
| school emotional surveillance | school access witness with denied fields |
| vendor policy drift | vendor update witness and rollback/quarantine path |
| external agent bypass | AGL/CBE/external-agent decision events |
| hidden Black route | Black route witness + post-review |
| witness theater | upstream refs required; trace does not equal grounding |
| missing privileged proof | required-event-missing event + fail closed |
| silent event tampering | signatures/hash-chain/integrity challenge |
| false-positive stigma | correction events + adult migration controls |
| adult trapped by child state | adult migration default fields |
| CCDP-washing | conformance event families and report schema |

---

## 32. Open issues for v0.2

1. Full machine-readable JSON Schema.
2. Canonical reason-code registry package.
3. Mapping to concrete L4 Witness CE/OP/CR/RN export examples.
4. Cross-jurisdiction retention annex.
5. Child challenge UI / UX requirements.
6. Raw exception escrow protocol.
7. Witness chain recovery after device loss.
8. Multi-household custody topology.
9. Peer-`c` cross-family event reconciliation.
10. Vendor update reproducibility bundle.
11. School integration profile.
12. Physical-agent sensor event schema.
13. Formal proof of no raw content in witness body.
14. Adult migration witness minimization test suite.
15. Cryptographic key rotation for `c_child` across maturity levels.

---

## 33. Acceptance checklist

A system implementing this schema may claim `CCDP-WITNESS-v0.1` support only if:

- [ ] it emits witness events for all required privileged transitions;
- [ ] witness events are append-only;
- [ ] event bodies exclude raw child content by default;
- [ ] raw exception path is separate, scoped, and reviewable;
- [ ] events declare privacy, disclosure, retention, and adult migration defaults;
- [ ] events link to AGL / Beacon / CBE / ARL / CMAM / VXCX / Continuity Bundle where relevant;
- [ ] missing required witness fails closed;
- [ ] malformed events are quarantined;
- [ ] correction events are append-only;
- [ ] conformance tests can verify event presence without reading child private life;
- [ ] adult migration can review or exclude witness residue;
- [ ] vendor cannot access child-specific witness content by default;
- [ ] school cannot use witness events for discipline or emotional surveillance;
- [ ] parent cannot convert witness events into routine transcript access.

---

## 34. Condensed formula

```text
CCDP Witness Event =
  event boundary
+ scoped actor
+ scoped child/entity reference
+ decision
+ reason codes
+ privacy class
+ disclosure level
+ retention class
+ upstream refs
+ hash/signature
- raw child life
```

Short form:

> Witness does not mean watching the child. It means proving that the system respected, refused, narrowed, or escalated a boundary.

Strong form:

> A child-facing AI system is not safer because it logs more. It is safer only when what it logs is minimal, challengeable, privacy-preserving, and sufficient to prove that power did not move silently.

---

## 35. Suggested next document

Recommended next artifact:

```text
CCDP_Memory_Map_JSON_Schema_v0_1.md
```

Reason:

The witness schema now defines how memory operations are evidenced. The next missing technical piece is a machine-readable map of the memory objects those events refer to.
