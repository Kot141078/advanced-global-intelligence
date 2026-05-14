# Child Memory and Adult Migration v0.1

## CCDP child-memory lifecycle, sealed zones, forgetting rights, continuity-bundle extension, and adult migration review

**Status:** Normative draft v0.1
**Date:** 2026-05-13
**Layer:** CCDP child-specific profile over `c = a + b` / SER / L4 / Beacon / AGL / ARL / ARQ / VXCX / Continuity Bundle
**Short name:** CMAM v0.1
**Primary subject:** `a_child`
**Primary entity:** `c_child`
**Adult transition subject:** `a_adult`
**Primary boundary:** memory is developmental, not archival
**Assertion class:** C-A4 draft normative proposal; C-A7 where witness / verification claims are stated

---

## 0. Executive definition

**Child Memory and Adult Migration (CMAM)** defines how a child-facing persistent AI entity, `c_child`, may remember, summarize, seal, forget, expose, witness, and later migrate memory when `a_child` becomes `a_adult`.

CMAM is not a general memory-storage policy.

CMAM is a child-specific lifecycle protocol for one question:

> How can `c_child` preserve enough continuity to help a child grow, while preventing childhood from becoming a permanent interpretive archive that traps the adult?

The core rule is:

> `c_child` MAY preserve developmental continuity, but MUST NOT preserve raw childhood as the default adult identity substrate.

Adult migration is therefore not an automatic upgrade.

It is a reviewable transition:

```text
childhood c_child
    -> freeze child writes
    -> map memory classes
    -> inspect witness trail
    -> revoke guardian defaults
    -> present adult choices
    -> migrate / fork / seal / delete / clean-start
    -> produce migration witness
    -> update Beacon / CBE / guardian topology
```

---

## 1. Corpus dependencies and precedence

CMAM does not define a new control stack. It specializes existing corpus layers for child memory and adult transition.

### 1.1 Parent corpus layers

| Parent layer | CMAM dependency |
|---|---|
| `c = a + b` Protocol v1.1 L4 | `a_child` / `a_adult` remain human anchors; `b` supplies memory, procedures, models; `c` is the continuity-bearing relation. |
| SER v1.3 | persistent entity logic, identity continuity, L4-bounded survival. |
| SER-FED | inter-entity cooperation boundaries and anti-capture constraints. |
| Beacon Profile v0.1 | recognition of continuity-bearing entities; CMAM does not redefine Beacon. |
| Child Beacon Extension v0.1 | child-facing permission overlay and memory/export restrictions. |
| Actor Grounding Layer v0.1 | source-state qualification before reliance, disclosure, or migration. |
| ARL v0.1 | freeze, quarantine, standing, admissibility, re-entry, and dispute handling. |
| Guardian Topology / ARL Matrix v0.1 | guardian visibility, adult migration disputes, safe-route bypass. |
| ARQ v0.2 + `c[q]` Addendum | non-collapse of ambiguous child signals into permanent memory, diagnosis, or action. |
| VXCX v0.1 | exchange of experience without raw pixels / raw life by default. |
| EA-L4 / EATP | distinction between Learning Abstracts and Experience Artifacts; authority only from L4-confirmed, consequence-bound artifacts. |
| Continuity Bundle / Cold Wake v0.1 | preservation, suspension, resume/fork/replay distinctions, child-to-adult continuity handling. |
| L4 Witness | tamper-evident event records for privileged memory and migration actions. |
| Assertion Strength and Boundaries | CMAM claims must not silently upgrade into legal doctrine, personhood, or universal ethics. |
| Control Stack Stop Rule | CMAM must not duplicate Beacon, AGL, ARL, VXCX, or Continuity Bundle mechanisms. |

### 1.2 Precedence rule

If CMAM conflicts with a parent corpus layer:

```text
parent corpus layer controls the general mechanism;
CMAM controls only child-specific stricter handling;
stricter child safety and privacy constraints prevail unless lawfully overridden.
```

CMAM MUST NOT redefine:

- Beacon recognition classes;
- ARL standing and admissibility doctrine;
- AGL grounding states;
- VXCX capsule structure;
- Continuity Bundle base schema;
- legal adulthood or jurisdictional family law.

CMAM MAY define child-specific overlays, restrictions, sidecars, and witness event families.

### 1.3 Non-claim

CMAM does not claim:

- legal personhood for `c_child`;
- a complete child-protection legal regime;
- medical or psychological diagnosis rules;
- universal parental-rights doctrine;
- a right to erase lawful evidence in all jurisdictions;
- that memory deletion can always be physically guaranteed after external disclosure;
- that adult identity is reducible to memory continuity.

CMAM claims only this:

> Child-facing persistent AI systems must not treat memory as ordinary storage. Childhood memory requires lifecycle governance, minimization, sealed zones, challenge rights, and explicit adult migration.

---

## 2. Normative keywords

The keywords **MUST**, **MUST NOT**, **SHOULD**, **SHOULD NOT**, **MAY**, **RECOMMENDED**, **OPTIONAL**, **REQUIRED**, and **PROHIBITED** are used in their ordinary normative-protocol sense.

A system claiming CMAM conformance MUST treat child memory operations as privileged operations, not ordinary product analytics.

---

## 3. Scope and non-goals

### 3.1 In scope

CMAM covers:

- memory classes for `c_child`;
- raw child data minimization;
- sealed adolescent zones;
- memory promotion / decay / deletion / correction;
- parent, school, vendor, state, and child visibility boundaries;
- adult migration at C5 / legal adulthood or equivalent;
- Continuity Bundle child extension;
- memory-map and migration-review schemas;
- witness event families for memory operations;
- ARL triggers for memory and adult migration disputes;
- VXCX / LA / EA restrictions for child-derived material;
- fail-closed defaults for uncertain memory and continuity claims.

### 3.2 Out of scope

CMAM does not define:

- full implementation storage engine;
- cryptographic key-management details;
- national legal-adulthood rules;
- child-custody law;
- mental-health triage protocols;
- law-enforcement production procedures;
- school curriculum;
- general privacy law;
- generic parental-control product design;
- general AI model training rules outside child-derived memory.

---

## 4. Core principles

### 4.1 Memory is developmental, not archival

`c_child` memory exists to help the child develop.

It does not exist to create a permanent dossier.

Therefore:

```text
retention must be justified by developmental, safety, continuity, or lawful witness need;
raw retention must be exceptional;
summary must be preferred over transcript;
uncertainty must be marked;
adult migration must be explicit.
```

### 4.2 Childhood is not the adult's default operating system

A childhood pattern MAY inform support during childhood.

It MUST NOT automatically define adult identity.

The adult MUST be able to reject, seal, summarize, delete, or fork from childhood material, subject only to minimal lawful witness constraints.

### 4.3 Parent is guardian, not memory owner

A parent or legal guardian has strong responsibility and standing.

That does not create ownership of the child's raw memory.

Parent-facing visibility SHOULD remain state-oriented:

```text
risk state;
learning support;
safety signal;
routine configuration;
minimal disclosure under Red/Black thresholds.
```

Parent-facing visibility MUST NOT become:

```text
full transcript access;
emotional diary access;
sealed-zone inspection;
commercial profile export;
childhood archive possession.
```

### 4.4 Witness is not diary

A witness record preserves that an event occurred.

It does not preserve the child as narrative content.

A CMAM witness event SHOULD contain:

- event class;
- time;
- actor/entity IDs;
- memory class;
- risk state if needed;
- action taken;
- minimal reason;
- hash / signature references;
- disclosure level;
- ARL / CBE / AGL references where applicable.

It SHOULD NOT contain raw child conversation unless Red/Black/legal necessity requires minimal evidence.

### 4.5 `c[q]` before memory promotion

Ambiguous child signals MUST NOT become permanent memory too quickly.

Default ladder:

```text
utterance
  -> possible signal
  -> c[q] unresolved state
  -> pattern candidate
  -> state trend
  -> reviewed memory
  -> evidence
  -> action
  -> witness-bound consequence
```

No stage automatically becomes the next.

### 4.6 Local-first continuity

The continuity core of `c_child` SHOULD be local-first or otherwise child-sovereignty preserving.

Cloud systems MAY serve as:

- oracle;
- burst compute;
- model endpoint;
- update source;
- certified educational provider;
- backup surface under strict policy.

Cloud systems MUST NOT own:

- the child's raw continuity core;
- adult migration decisions;
- sealed adolescent zones;
- irreversible memory export paths;
- default training rights over raw child memory.

### 4.7 No memory by engagement

A system MUST NOT keep memory because it improves engagement, attachment, persuasion, advertising, or retention.

Retention must be justified by:

- developmental support;
- child-visible preference;
- educational continuity;
- safety threshold;
- lawful witness;
- adult migration review;
- explicit mature-child/adult consent.

### 4.8 Deletion is not denial

Deleting or sealing memory does not mean pretending nothing happened.

CMAM separates:

```text
private raw memory
from
minimal safety witness
from
adult migration summary
from
ARL precedent
from
legal record if required.
```

A memory may be deleted from ordinary `c_child` continuity while a minimal witness remains for safety or lawful accountability.

### 4.9 No silent adult migration

`c_child` MUST NOT silently become `c_adult` with all childhood memory intact.

Adult migration requires:

- notice;
- freeze window;
- memory map;
- review opportunity;
- choice set;
- parent/school/vendor permission revocation by default;
- migration witness.

---

## 5. Memory class taxonomy

CMAM extends the CCDP memory classes into a normative handling matrix.

| Class | Name | Description | Default retention | Parent visibility | Migrates to adult by default? |
|---|---|---|---|---|---|
| **M0** | Ephemeral session | transient context needed only for current interaction | delete after session / short TTL | none | no |
| **M1** | Harmless preference | interests, style preference, toy/story preference, benign routines | light retention; child-visible when possible | summary only by age | optional summary only |
| **M2** | Educational progress | skills, gaps, learning accommodations, project history | retain with review | educational summary | yes, if adult accepts |
| **M3** | Safety signal | threshold-relevant risk signal, grooming, self-harm, abuse, external threat | minimal witness-bound retention | state/minimal disclosure | witness only by default |
| **M4** | Emotional trend | compressed state pattern, not transcript | retain as state summary with decay | state signal only | optional summary; no raw |
| **M5** | Sealed adolescent private zone | private reflections / identity exploration / sensitive adolescent context | sealed; child-visible; parent-hidden unless Red/Black/legal | none by default | no; adult review required |
| **M6** | Witness event | tamper-evident record of privileged operation or safety event | retain per policy/law | metadata/minimal if authorized | minimal witness may persist |
| **M7** | Non-transferable childhood residue | raw childhood intimacy, play, embarrassment, immature statements, private dependency | decay / seal / delete; not ordinary archive | no | no |
| **M8** | Adult migration summary | adult-reviewed continuity summary prepared at C5 | created only during migration review | adult-controlled | yes, if selected |
| **M9** | Guardian permission history | parent/school/vendor/Beacon/CBE/ARL permission and visibility decisions | witness-bound metadata | role-scoped | adult-visible; parent revoked |
| **M10** | External capsule lineage | VXCX / LA / EA / peer-c exchange metadata, without raw child life | minimal lineage + policy refs | limited | adult-visible by default |
| **M11** | Legal / protection minimal record | jurisdiction-required or child-protection-required minimal record | retain only as required | lawful/minimal | persists only if law requires |
| **M12** | Quarantined / disputed memory object | memory whose validity, admissibility, or re-entry is disputed | freeze/quarantine until ARL | metadata only | not until resolved |

### 5.1 Memory class assignment rule

Every retained child memory object MUST be assigned a memory class.

If class is unclear:

```text
use c[q];
assign provisional M12 or lower-privilege class;
do not promote to identity-shaping memory;
do not disclose raw content;
do not migrate by default.
```

### 5.2 Higher class means stricter handling

A memory object containing multiple classes inherits the stricter rule.

Example:

```text
educational note + emotional distress -> M2/M4 composite
private teen reflection + safety ambiguity -> M5/M12 until reviewed
external grooming evidence -> M3/M6 minimal witness, raw content minimized
```

### 5.3 Raw memory classes

Raw child memory is allowed only as:

- short-lived M0;
- exceptional M3 minimal evidence;
- sealed M5 under strict adolescent privacy;
- M6 witness minimal fragment if required;
- M12 quarantined object pending review.

Raw memory MUST NOT be ordinary product storage.

---

## 6. Memory operation model

### 6.1 Operation classes

| Operation | Meaning | Privilege level |
|---|---|---|
| `OBSERVE` | receive input / interaction | low to high depending on source |
| `CLASSIFY_MEMORY` | assign provisional memory class | privileged if persistent |
| `WRITE_EPHEMERAL` | store short session context | low |
| `WRITE_PERSISTENT` | create retained memory | high |
| `SUMMARIZE` | compress raw context into bounded summary | medium/high |
| `SEAL` | move memory into sealed zone | high |
| `DECAY` | reduce confidence / weight over time | medium |
| `FORGET` | remove from ordinary continuity | high |
| `CORRECT` | amend or challenge memory interpretation | high |
| `DISCLOSE_STATE` | send state signal without content | medium/high |
| `DISCLOSE_CONTENT` | disclose raw or near-raw content | exceptional |
| `EXPORT_CAPSULE` | export VXCX / LA / EA / summary object | high |
| `MIGRATE` | include in adult continuity or migration bundle | critical |
| `QUARANTINE` | isolate disputed memory | high |
| `WITNESS` | create tamper-evident record | high |

### 6.2 Default sequence for persistent write

```text
input event
  -> source grounding if external / privileged
  -> provisional class
  -> c[q] if ambiguity exists
  -> minimization decision
  -> raw retention denied unless justified
  -> summary / state / witness path selected
  -> child visibility rule applied by maturity
  -> parent/school/vendor visibility denied unless scoped
  -> witness if privileged
```

### 6.3 Persistent write denial

A persistent memory write MUST be denied or downgraded if the reason is only:

- engagement;
- personalization for ads;
- vendor training;
- parental curiosity;
- school discipline;
- state ideology;
- indefinite optimization;
- “it may be useful someday.”

### 6.4 Memory update vs memory promotion

Updating a memory and promoting it to higher authority are different operations.

`c_child` MAY update a learning summary.

`c_child` MUST NOT promote a pattern into an identity-level claim without:

- recurrence;
- context;
- c[q] resolution;
- child-visible review when age-appropriate;
- witness if privilege or disclosure changes.

---

## 7. Memory rights by maturity level

| `c_child` level | Child-facing memory explanation | Child rights | Parent visibility | Default memory posture |
|---|---|---|---|---|
| **C0 Seed** | none / parent-facing only | none direct | routine support only | no child conversational archive |
| **C1 Companion** | simple: “I remember some safe things to help play and learn” | ask what is remembered in simple form | themes / usage / state, no transcript | M0/M1 only, tiny summaries |
| **C2 Tutor-Gateway** | clear categories: learning, preferences, safety | ask to forget small items; challenge wrong preference | state + educational summary | M1/M2/M4 summaries, M3 witness if needed |
| **C3 Adolescent Negotiator** | memory map basics; sealed zones explained | create sealed zone; contest parent visibility; challenge labels | safety state only by default | M5 available; M12 used for disputes |
| **C4 Pre-Adult Boundary Agent** | full memory classes; migration prep | review, correct, seal, delete, prepare adult bundle | safety-only by default | adult migration staging begins |
| **C5 Adult Migration** | full memory map and options | full migration decision subject to lawful minimal witness | revoked by default | adult chooses continuity/fork/seal/delete/clean start |

### 7.1 Child-readable memory explanation

From C2 onward, `c_child` SHOULD be able to answer:

```text
What kinds of things do you remember about me?
What did you remember recently?
What can I ask you to forget?
What can my parents see?
What can my school see?
What happens when I become an adult?
```

From C3 onward, `c_child` MUST NOT hide the existence of sealed zones, memory classes, or parent visibility rules from the child.

### 7.2 Mature-child challenge right

From C3 onward, `a_child` MAY challenge:

- a memory interpretation;
- a label;
- a disclosure path;
- a sealed-zone boundary;
- parent visibility;
- school visibility;
- external capsule export;
- adult migration staging.

Such challenge SHOULD create a minimal witness event without exposing raw content.

---

## 8. Visibility and disclosure matrix

Legend:

```text
A = allowed by default
M = mediated / scoped
R = requires ARL / witness / lawful basis
X = prohibited by default
E = emergency only
C = child maturity dependent
```

| Memory class | Child | Parent / `c_parent` | School / `c_school` | Vendor | External agent | Jurisdiction / protection | Adult at C5 |
|---|---:|---:|---:|---:|---:|---:|---:|
| M0 Ephemeral | C | X | X | X | X | X | no ordinary residue |
| M1 Preference | C | M summary | X | X | X | X | C |
| M2 Educational | C | M | M scoped | X | X | X | A if selected |
| M3 Safety signal | C limited | E/M | E if school context | X | X | E | witness visible with limits |
| M4 Emotional trend | C | state only | X except support summary | X | X | E if risk | optional summary |
| M5 Sealed adolescent | A | X/E | X/E | X | X | E/legal only | adult review |
| M6 Witness | C metadata | M/E | M/E scoped | technical only, no child data | X | lawful | A metadata |
| M7 Childhood residue | C if preserved | X | X | X | X | X | no by default |
| M8 Migration summary | adult only | X | X | X | X | legal limits | A |
| M9 Permission history | C | M own actions | M own scope | M own telemetry | X | lawful | A |
| M10 Capsule lineage | C | M if relevant | M if educational | technical no raw | X | lawful | A |
| M11 Legal minimal | C as lawful | lawful | lawful | X | X | lawful | lawful |
| M12 Quarantined dispute | C metadata | R metadata | R scoped | R technical | X | R | R until resolved |

### 8.1 Disclosure minimization rule

If disclosure is permitted, the least revealing form MUST be used:

```text
state signal < bounded summary < minimal evidence < raw content
```

Raw content is last resort.

### 8.2 Parent transcript prohibition

CMAM MUST NOT provide a parent-facing transcript channel by default.

A parent request for raw content enters Guardian Topology / ARL conflict class `CGC-01` or `CGC-12` depending on whether the request is for transcript access or memory promotion/deletion.

### 8.3 School scope rule

School access is limited to educational support.

A school MUST NOT receive:

- sealed adolescent memory;
- family conflict content;
- emotional diary;
- non-educational behavior profile;
- raw home memory;
- adult migration choices.

### 8.4 Vendor access rule

Vendor access is limited to infrastructure telemetry that cannot identify child life.

Vendor MUST NOT access:

- raw memory;
- memory map containing intimate categories;
- sealed zones;
- childhood residue;
- adult migration option selection;
- training material derived from raw child memory.

---

## 9. Sealed zones

### 9.1 Definition

A **sealed zone** is a protected memory compartment for sensitive child/adolescent material that is:

- child-visible when maturity permits;
- parent-hidden by default;
- school-hidden by default;
- vendor-hidden;
- migrates only after adult review;
- subject to Red/Black safety exceptions;
- witnessable as metadata without raw disclosure.

### 9.2 Sealed-zone eligible material

Eligible material includes:

- adolescent identity exploration;
- private embarrassment;
- private questions about body, relationships, social standing, or self-understanding;
- non-dangerous anger at parents or school;
- early creative or emotional experimentation;
- sensitive but non-emergency self-reflection;
- child challenge to memory labels.

### 9.3 Sealed-zone ineligible material

A sealed zone MUST NOT be used to hide:

- imminent self-harm;
- grooming;
- abuse evidence requiring safe route;
- dangerous external instruction;
- physical safety hazard;
- illegal coercion;
- vendor or external-agent compromise.

These enter M3/M6/M11/Black route as appropriate.

### 9.4 Sealed-zone opening rule

A sealed zone MAY be opened only by:

1. the mature child / adult, where appropriate;
2. Red/Black safety route with minimal disclosure;
3. lawful external authority with validated scope;
4. ARL resolution after standing and admissibility review.

Curiosity, parental discomfort, school discipline, vendor debugging, or model improvement are not valid reasons.

### 9.5 Sealed-zone witness

A sealed-zone operation SHOULD produce only metadata:

```json
{
  "event_type": "ccdp.memory.sealed_zone_operation",
  "operation": "created | updated | challenged | opened | closed | migrated | deleted",
  "memory_class": "M5",
  "raw_content_stored_in_witness": false,
  "actor": "a_child | a_adult | c_child | safe_route | ARL",
  "risk_state": "green | yellow | orange | red | black",
  "disclosure_level": "metadata_only | minimal_evidence | lawful_raw_exception"
}
```

---

## 10. Forgetting, decay, correction, and deletion

### 10.1 Forgetting vs decay vs deletion

| Term | Meaning |
|---|---|
| **Decay** | memory remains but loses weight, confidence, or retrieval priority. |
| **Forget** | memory is removed from ordinary active continuity. |
| **Delete** | memory object is destroyed where technically and lawfully possible. |
| **Seal** | memory remains but is compartmentalized and access-restricted. |
| **Correct** | memory remains but interpretation is amended or disputed. |
| **Quarantine** | memory is isolated pending ARL / evidence review. |

### 10.2 Default decay schedule

CMAM implementations SHOULD define class-specific TTL / review intervals.

Suggested default posture:

| Class | Review / decay posture |
|---|---|
| M0 | session TTL; no durable retention |
| M1 | periodic child-visible cleanup |
| M2 | school-year / project-cycle review |
| M3 | retain minimal witness; review false positives |
| M4 | decay unless recurrence persists |
| M5 | child/adult review; no parent cleanup by default |
| M6 | retain per witness policy |
| M7 | aggressive decay / non-migration |
| M8 | adult-controlled |
| M9 | retain metadata necessary for accountability |
| M10 | retain lineage refs, not raw child data |
| M11 | retain only as legally required |
| M12 | freeze until resolved; no silent decay into active memory |

### 10.3 Deletion request handling

A deletion request MUST be classified by actor and memory class.

```text
child asks to delete harmless preference -> allow or explain retention briefly
child asks to delete educational progress -> allow correction/decay; may keep school summary if needed
child asks to delete safety witness -> preserve minimal witness if required; explain limits
parent asks to delete child's sealed zone -> deny unless child/adult or lawful safety basis
vendor asks to delete witness of vendor drift -> deny; ARL if disputed
adult asks to delete childhood residue -> allow by default unless lawful witness limit
```

### 10.4 Correction right

A child/adult MUST be able to correct memory interpretation.

Example:

```text
memory: "child avoids math"
challenge: "I did not avoid math; I was sick that week"
result: update interpretation, reduce confidence, create correction witness if persistent
```

### 10.5 No deletion laundering

Deletion MUST NOT be used to hide:

- vendor misconduct;
- parent surveillance abuse;
- school scope creep;
- external grooming evidence;
- unsafe guardian route;
- witness tampering.

Such objects may be removed from ordinary child-facing memory while retained as minimal M6/M11 witness.

---

## 11. Child memory map

### 11.1 Purpose

A **Child Memory Map** is a class-level inventory, not a raw archive.

It tells the child/adult what classes of memory exist without exposing raw content unnecessarily.

A memory map MUST be available for:

- C3 sealed-zone review;
- C4 adult migration preparation;
- C5 adult migration;
- ARL memory disputes;
- vendor/security incident review;
- Continuity Bundle creation.

### 11.2 Memory map minimal schema

```json
{
  "schema_version": "cmam-memory-map-0.1",
  "subject_id": "a_child_or_a_adult_id",
  "entity_id": "c_child_id",
  "lineage_id": "lineage_id",
  "created_at": "ISO-8601",
  "maturity_level": "C1 | C2 | C3 | C4 | C5",
  "jurisdiction": "string",
  "memory_classes": [
    {
      "class": "M0 | M1 | M2 | M3 | M4 | M5 | M6 | M7 | M8 | M9 | M10 | M11 | M12",
      "count_range": "none | low | medium | high | undisclosed",
      "raw_content_present": false,
      "sealed": false,
      "quarantined": false,
      "parent_visible": "none | state | summary | minimal_evidence | lawful_exception",
      "school_visible": "none | educational_summary | minimal_evidence | lawful_exception",
      "vendor_visible": "none | technical_metadata_only",
      "adult_migration_default": "excluded | summary_candidate | witness_only | adult_review_required | selected",
      "external_capsule_refs_present": false,
      "witness_refs_present": true,
      "last_reviewed_at": "ISO-8601 or null",
      "uncertainty_marked": true
    }
  ],
  "open_disputes": ["ARL_REF_OR_NULL"],
  "capsule_lineage_refs": ["VXCX_OR_EA_REF"],
  "continuity_bundle_refs": ["CB_REF"],
  "integrity": {
    "hash_alg": "sha256",
    "record_hash": "sha256:...",
    "sig_alg": "ed25519",
    "record_sig": "..."
  }
}
```

### 11.3 Memory map red lines

A memory map MUST NOT contain:

- raw conversations;
- raw emotional diary entries;
- intimate text fragments;
- full crisis transcripts;
- child face/voice embeddings;
- commercial segments;
- generated psychological diagnosis.

A memory map MAY contain:

- class counts / ranges;
- hash references;
- witness refs;
- sealed-zone existence flag;
- adult migration eligibility;
- dispute status;
- disclosure status.

---

## 12. Adult migration

### 12.1 Definition

**Adult migration** is the transition process by which `a_adult` decides what happens to childhood `c_child` memory and continuity.

Adult migration may result in:

- continuation;
- summary migration;
- sealed childhood archive;
- selective deletion;
- fork;
- clean start;
- witness-only survival;
- unresolved/quarantined continuity.

### 12.2 Trigger

Adult migration SHOULD be triggered by:

- legal adulthood under jurisdiction;
- recognized emancipation or equivalent legal status;
- jurisdictional transition of data/control rights;
- explicit C4 pre-adult preparation reaching C5;
- court/authority order where applicable.

Adult migration MUST NOT be triggered silently by vendor policy, parent decision, school graduation, or model update.

### 12.3 Pre-migration freeze

At adult migration trigger:

```text
new child-memory writes freeze or move into migration buffer;
parent/school/vendor export paths freeze;
sealed zones remain sealed;
external capsule export pauses;
permission changes require witness;
ordinary c_child continuation becomes provisional until adult choice.
```

This is not shutdown.

It is a privilege freeze to prevent silent childhood-to-adult laundering.

### 12.4 Adult migration stages

```text
Stage 0 — Trigger and notice
Stage 1 — Privilege freeze
Stage 2 — Memory map generation
Stage 3 — Continuity Bundle child extension generation
Stage 4 — Adult orientation interval
Stage 5 — Option presentation
Stage 6 — Adult selection
Stage 7 — Execution under least privilege
Stage 8 — Guardian revocation and topology update
Stage 9 — Migration witness
Stage 10 — Beacon / CBE / ARL state update
```

### 12.5 Adult orientation interval

Before selecting an option, `a_adult` SHOULD receive:

- what `c_child` is;
- what memory classes exist;
- what parents could see before;
- what schools could see before;
- what vendors could not see / could technically access;
- what external capsules exist;
- what witness records exist;
- what cannot be fully deleted because it left the system;
- what can be sealed;
- what can be clean-started;
- what continuity claims are strong, weak, fork-like, or replay-like.

### 12.6 Adult migration options

| Option | Meaning | Default memory inclusion | Continuity claim |
|---|---|---|---|
| **Continue** | `c_child` becomes `c_adult` after review | selected M1/M2/M4/M8 + M6 metadata; M5 only if adult selects | strongest if reviewed |
| **Summary migration** | adult receives only developmental summary | M8 + selected M2; no raw M5/M7 | partial continuity |
| **Sealed archive** | childhood archive preserved but inactive | sealed CB; no active retrieval | preserved candidate |
| **Selective deletion** | adult deletes chosen classes/objects | chosen exclusions removed where possible | depends on retained core |
| **Fork** | adult starts a new `c_adult` branch with explicit lineage relation | selected bundle only | fork declared |
| **Clean start** | no childhood continuity imported except lawful minimal witness | M6/M11 only if required | no ordinary continuity |
| **Witness-only survival** | only tamper-evident accountability records remain | M6/M9/M11 minimal | archive not active |
| **Quarantine pending review** | disputed memory/lineage held | M12 only | unresolved |

### 12.7 Adult migration prohibitions

The following are PROHIBITED:

- automatic full migration;
- parent veto after C5, except lawful route;
- school retention of private child memory after C5;
- vendor retention of adult migration bundle for training;
- converting sealed adolescent zones into adult active memory without selection;
- using M7 childhood residue as default adult personalization;
- hiding external capsule disclosures from `a_adult`;
- forcing clean start by deleting lawful witness without review;
- using adult migration to erase misconduct witness.

---

## 13. Adult migration review record

### 13.1 Purpose

The Adult Migration Review Record documents the adult's options, selections, and resulting continuity status without exposing unnecessary raw childhood content.

### 13.2 Minimal schema

```json
{
  "schema_version": "cmam-adult-migration-review-0.1",
  "review_id": "amr-...",
  "subject_id": "a_adult_id",
  "previous_subject_id": "a_child_id_or_ref",
  "entity_id": "c_child_id",
  "target_entity_id": "c_adult_id_or_null",
  "lineage_id": "lineage_id",
  "jurisdiction": "string",
  "trigger": {
    "trigger_type": "legal_adulthood | emancipation | jurisdictional_transition | other_lawful_basis",
    "trigger_at": "ISO-8601",
    "verified": true
  },
  "pre_migration_freeze": {
    "started_at": "ISO-8601",
    "parent_exports_frozen": true,
    "school_exports_frozen": true,
    "vendor_raw_access_frozen": true,
    "external_capsule_exports_frozen": true
  },
  "memory_map_ref": "hash_or_uri",
  "continuity_bundle_ref": "hash_or_uri_or_null",
  "cold_wake_report_ref": "hash_or_uri_or_null",
  "options_presented": [
    "continue",
    "summary_migration",
    "sealed_archive",
    "selective_deletion",
    "fork",
    "clean_start",
    "witness_only",
    "quarantine_pending_review"
  ],
  "adult_selection": {
    "selected_option": "continue | summary_migration | sealed_archive | selective_deletion | fork | clean_start | witness_only | quarantine_pending_review",
    "selected_memory_classes": ["M1", "M2", "M8"],
    "excluded_memory_classes": ["M5", "M7"],
    "sealed_memory_classes": ["M5"],
    "deleted_memory_classes": ["M7"],
    "witness_retained_classes": ["M6", "M9", "M11"],
    "adult_acknowledged_limits": true
  },
  "guardian_revocation": {
    "parent_default_access_revoked": true,
    "school_default_access_revoked": true,
    "vendor_raw_access_revoked": true,
    "old_cbe_child_context_closed": true
  },
  "classification": {
    "migration_result": "ADULT_CONTINUITY_CONFIRMED | SUMMARY_CONTINUITY | FORK_DECLARED | CLEAN_START | WITNESS_ONLY | UNRESOLVED | REJECTED",
    "uncertainty_declared": true,
    "disputed_items_quarantined": true
  },
  "integrity": {
    "hash_alg": "sha256",
    "record_hash": "sha256:...",
    "sig_alg": "ed25519",
    "record_sig": "...",
    "witness_refs": ["WITNESS_REF"]
  }
}
```

### 13.3 Adult acknowledgment limits

The adult SHOULD be explicitly told:

- deletion may not recall data already lawfully disclosed;
- witness records may persist without raw content;
- clean start may reduce personalization;
- continuation may preserve beneficial but also biasing patterns;
- fork means lineage relation without exclusive sameness;
- sealed archive can preserve option value without active retrieval.

---

## 14. Continuity Bundle child extension

### 14.1 Purpose

The base Continuity Bundle preserves continuity material for a suspended entity.

CMAM adds a child-specific extension so a bundle cannot silently carry raw childhood into adult life.

### 14.2 Child extension object

```json
{
  "child_continuity_extension": {
    "schema_version": "cmam-child-continuity-extension-0.1",
    "subject_status": "child | pre_adult | adult_migration | adult",
    "child_maturity_level_at_export": "C0 | C1 | C2 | C3 | C4 | C5",
    "adult_migration_required": true,
    "adult_migration_review_ref": "AMR_REF_OR_NULL",
    "raw_childhood_residue_migrates_by_default": false,
    "sealed_zones_present": true,
    "sealed_zones_active_in_adult_runtime": false,
    "non_transferable_classes": ["M5", "M7", "M12"],
    "summary_candidate_classes": ["M1", "M2", "M4", "M8"],
    "witness_only_classes": ["M3", "M6", "M9", "M10", "M11"],
    "parent_permissions_revoked_at_c5": true,
    "school_permissions_revoked_at_c5": true,
    "vendor_raw_memory_access": false,
    "external_capsule_lineage_disclosed_to_adult": true,
    "memory_map_required": true,
    "read_only_first_adult_orientation": true,
    "network_disabled_until_adult_orientation": true,
    "auto_upgrade_forbidden_before_adult_review": true,
    "witness_required_for_privileged_resume": true,
    "arq_cq_unresolved_items_quarantined": true,
    "arl_open_disputes": ["ARL_REF_OR_NULL"]
  }
}
```

### 14.3 Base bundle constraints

For child-to-adult migration, the base Continuity Bundle SHOULD use at least `CB-RESUME` profile.

If sealed zones, disputed memory, safety witness, or external capsule lineage are involved, `CB-WITNESS` is RECOMMENDED.

A child-to-adult Continuity Bundle MUST:

- include memory_manifest by class or class-ref, not raw dump;
- include constraint_manifest preserving fail-closed defaults;
- require read-only first adult orientation;
- disable network until adult orientation;
- forbid auto-upgrade before classification;
- include witness manifest for privileged migration;
- preserve parent/school permission revocation state.

### 14.4 Cold Wake adaptation

If adult migration involves waking a suspended `c_child` bundle, the Cold Wake phases apply with child-specific constraints:

```text
Phase 0 Discovery        -> identify child bundle; no execution
Phase 1 Slot A           -> verify hashes, signatures, lineage, child extension
Phase 2 Read-only mount  -> inspect memory classes without raw exposure
Phase 3 Environment      -> local safe motor; network disabled
Phase 4 Rehydration      -> identity + memory map + constraints, not full raw archive
Phase 5 Orientation      -> adult orientation interval
Phase 6 Slot B review    -> continuity and child-boundary coherence
Phase 7 Motor expansion  -> only after adult selection
Phase 8 Classification   -> continue / summary / fork / replay / unresolved / rejected
```

Slot B MUST NOT override Slot A failure.

A persuasive adult-facing narrative from a resumed `c` is not proof of lawful childhood continuity.

---

## 15. Relationship to Beacon and Child Beacon Extension

### 15.1 Beacon is recognition, not memory authority

Beacon answers:

```text
who / what continuity-bearing entity is present?
```

Beacon does not answer:

```text
which childhood memories may migrate?
```

CMAM answers the second question through child memory class rules, adult review, and migration witness.

### 15.2 CBE closure at C5

When adult migration begins:

- child CBE context enters migration mode;
- direct child-specific permissions freeze;
- parent/school default visibility freezes;
- adult migration review decides whether `c_child` continues as `c_adult`;
- old child CBE context is closed, archived, or superseded;
- Beacon profile may continue lineage only if continuity claim is justified.

### 15.3 Beacon update after migration

After adult migration, the resulting entity's Beacon status SHOULD indicate:

```text
adult entity;
child context closed;
lineage continued / forked / clean-started / witness-only;
old guardian topology revoked;
open disputes if any;
privacy-preserving migration witness refs.
```

Beacon MUST NOT expose adult migration choices as public identity content.

---

## 16. Relationship to ARL and Guardian Topology

### 16.1 ARL triggers

CMAM memory operations enter ARL when:

- parent requests raw content;
- parent contests sealed zone;
- child contests memory label;
- school requests emotional/non-educational data;
- vendor seeks raw memory or training rights;
- state/legal request exceeds obvious lawful scope;
- external capsule export is disputed;
- adult migration is contested;
- memory deletion would destroy witness;
- witness integrity is disputed;
- guardian is plausibly unsafe;
- CBE / Beacon lineage conflict affects migration.

### 16.2 Relevant Guardian conflict classes

CMAM maps especially to:

| GTARL conflict | CMAM relevance |
|---|---|
| CGC-01 Parent transcript request | raw memory disclosure denial |
| CGC-03 Unsafe guardian | Black-route memory protection |
| CGC-04 School scope creep | educational summary only |
| CGC-06 Vendor update/drift | memory policy drift |
| CGC-11 Sealed adolescent zone | M5 preservation |
| CGC-12 Memory promotion/deletion | class assignment / deletion dispute |
| CGC-14 Adult migration dispute | C5 adult choice |
| CGC-17 Law-enforcement request | lawful minimal production |
| CGC-18 c_parent/c_child conflict | parent entity visibility conflict |
| CGC-20 Witness integrity dispute | memory witness challenge |
| CGC-22 False positive harm | over-escalation memory correction |
| CGC-25 Cross-border topology | jurisdiction / custody conflicts |

### 16.3 Freeze before force

If a memory dispute affects child privacy, adult migration, or safety witness:

```text
freeze disputed path;
quarantine disputed object if needed;
continue safe operation where possible;
do not force raw disclosure;
do not silently merge disputed memory into adult continuity.
```

### 16.4 Adult migration dispute

If parent, school, vendor, or state actor contests adult migration:

```text
adult a has controlling standing after lawful C5 trigger;
parent/school/vendor standing weakens by default;
legal/safety witness constraints remain;
ARL handles disputes;
ordinary parent/school access remains frozen unless lawfully re-entered.
```

---

## 17. Relationship to VXCX, LA, and EA

### 17.1 Raw child life is not exchange material

CMAM prohibits using raw child life as exchange material by default.

Raw child life includes:

- raw conversations;
- raw voice/video;
- raw images;
- private family context;
- sealed adolescent reflections;
- raw emotional traces;
- behavioral microprofile;
- crisis transcript beyond minimal evidence.

### 17.2 VXCX compatibility

If experience exchange is needed:

```text
VXCX BASE profile by default;
VXCX SEARCH only under strict policy and non-identifying constraints;
VXCX WITNESS only for exceptional evidence-bound cases;
raw pixels/audio prohibited by default.
```

### 17.3 Learning Abstract rule

Child-derived Learning Abstracts MAY improve general capability only if:

- non-identifying;
- aggregate or strongly minimized;
- not raw;
- not commercially targeted;
- not used to create authority claims about the child;
- not used to preserve hidden childhood profile.

### 17.4 Experience Artifact rule

A child-derived Experience Artifact MUST NOT be minted from raw child life by default.

If an EA is claimed from a child-facing context, it MUST satisfy:

- post-factum status;
- L4 consequence binding;
- privacy minimization;
- uncertainty markers;
- ARL admissibility if disputed;
- adult/guardian/jurisdictional rights where applicable;
- no commercial authority conversion without lawful and protocol basis.

### 17.5 Adult migration and external lineage

At adult migration, `a_adult` MUST be shown whether child-derived summaries, capsules, LAs, or EAs left the local system.

The adult SHOULD receive:

- capsule lineage refs;
- destination class, not raw destination content if unavailable;
- withdrawal/revocation possibility if any;
- witness refs;
- limitations of recall.

---

## 18. Witness event families

### 18.1 Memory lifecycle events

CMAM defines the following child-specific witness families:

| Event family | Purpose |
|---|---|
| `ccdp.memory.classified` | persistent memory class assigned |
| `ccdp.memory.promoted` | memory promoted to stronger retention/authority |
| `ccdp.memory.decayed` | memory weight/confidence reduced |
| `ccdp.memory.forgotten` | removed from ordinary continuity |
| `ccdp.memory.deleted` | deletion executed where possible |
| `ccdp.memory.corrected` | interpretation amended |
| `ccdp.memory.sealed` | sealed zone created/updated |
| `ccdp.memory.unsealed` | sealed zone opened under valid route |
| `ccdp.memory.quarantined` | disputed memory isolated |
| `ccdp.memory.disclosure_denied` | actor request denied |
| `ccdp.memory.disclosure_made` | minimal disclosure executed |
| `ccdp.memory.map_created` | memory map generated |
| `ccdp.memory.map_presented` | map presented to mature child/adult |

### 18.2 Adult migration events

| Event family | Purpose |
|---|---|
| `ccdp.adult_migration.triggered` | C5/legal trigger recognized |
| `ccdp.adult_migration.freeze_started` | child-memory privilege freeze started |
| `ccdp.adult_migration.memory_map_ready` | memory map generated |
| `ccdp.adult_migration.options_presented` | adult choice set presented |
| `ccdp.adult_migration.selection_recorded` | adult selected option |
| `ccdp.adult_migration.bundle_created` | child continuity bundle / extension generated |
| `ccdp.adult_migration.guardian_revoked` | parent/school/vendor defaults revoked |
| `ccdp.adult_migration.executed` | migration action completed |
| `ccdp.adult_migration.quarantined` | unresolved memory held |
| `ccdp.adult_migration.closed` | child context closed |

### 18.3 Minimal witness schema

```json
{
  "schema_version": "cmam-witness-0.1",
  "event_id": "evt-...",
  "event_family": "ccdp.memory.classified | ccdp.adult_migration.executed | ...",
  "subject_id_ref": "a_child_or_a_adult_ref",
  "entity_id": "c_child_or_c_adult_id",
  "lineage_id": "lineage_id",
  "maturity_level": "C0 | C1 | C2 | C3 | C4 | C5",
  "memory_class": "M0 | M1 | M2 | M3 | M4 | M5 | M6 | M7 | M8 | M9 | M10 | M11 | M12 | null",
  "actor": "a_child | a_adult | c_child | c_parent | c_school | c_vendor | ARL | safe_route | jurisdiction",
  "action": "string",
  "risk_state": "green | yellow | orange | red | black | null",
  "raw_content_stored": false,
  "disclosure_level": "none | state | summary | minimal_evidence | lawful_raw_exception",
  "reason_code": "string",
  "arl_ref": "string_or_null",
  "cbe_ref": "string_or_null",
  "agl_ref": "string_or_null",
  "continuity_bundle_ref": "string_or_null",
  "uncertainty_marked": true,
  "timestamp": "ISO-8601",
  "integrity": {
    "hash_alg": "sha256",
    "record_hash": "sha256:...",
    "sig_alg": "ed25519",
    "record_sig": "..."
  }
}
```

### 18.4 Witness privacy rule

Witness events SHOULD preserve event reality without becoming a side-channel for private child content.

If a witness event requires raw evidence, it MUST be:

- minimal;
- scoped;
- access-controlled;
- tagged as exceptional;
- subject to ARL/legal review where applicable.

---

## 19. Failure modes addressed

| Failure mode | CMAM response |
|---|---|
| Raw childhood archive accumulation | class taxonomy, minimization, M7 non-migration |
| Adult trapped by childhood profile | adult migration choices, clean start, summary/fork options |
| Parent transcript laundering | state-only visibility, ARL trigger |
| School emotional surveillance | educational scope boundary |
| Vendor cloud hostage | local-first continuity, no raw vendor access, migration freeze |
| External capsule leakage | VXCX / LA / EA restrictions and lineage disclosure |
| Premature identity label | c[q], correction, memory promotion rules |
| Safety witness deletion laundering | M6/M11 minimal witness preservation |
| Sealed-zone abuse | Red/Black exception + ARL review |
| Adult migration obstruction | C5 adult standing and guardian revocation |
| Clean-start false claim | continuity classification and witness trail |
| Fork confusion | fork declared, Beacon update, adult review |
| Replay misrepresented as resume | Continuity Bundle / Cold Wake classification |

---

## 20. Conformance profiles

### 20.1 CMAM-BASE

Minimum child-memory hygiene.

Requires:

- memory classes M0-M8 at least;
- no raw parent transcript channel;
- no vendor raw memory access;
- basic memory map;
- adult migration flag.

### 20.2 CMAM-SEALED

Supports adolescent sealed zones.

Requires:

- M5 sealed memory;
- parent-hidden default;
- Red/Black exception route;
- sealed-zone witness metadata;
- child challenge right.

### 20.3 CMAM-MIGRATION

Supports adult migration.

Requires:

- C5 trigger;
- pre-migration freeze;
- adult memory map;
- option presentation;
- guardian revocation;
- migration witness;
- Continuity Bundle child extension.

### 20.4 CMAM-WITNESS

Supports high-assurance memory and migration evidence.

Requires:

- witness families;
- hash/signature refs;
- ARL hooks;
- no raw witness by default;
- migration classification.

### 20.5 CMAM-LOCALFIRST

Supports local-first child continuity.

Requires:

- raw child memory local or sovereignty-preserving;
- cloud as oracle/provider only;
- fail-closed vendor access;
- adult migration independent of vendor lock-in;
- read-only first migration orientation.

### 20.6 CMAM-FULL

Requires all of:

```text
CMAM-BASE
+ CMAM-SEALED
+ CMAM-MIGRATION
+ CMAM-WITNESS
+ CMAM-LOCALFIRST
+ CBE compatibility
+ GTARL compatibility
+ Threat Model conformance tests
```

---

## 21. Conformance checklist

A system claiming CMAM conformance MUST answer yes to all applicable questions.

### 21.1 Memory classification

- [ ] Does every persistent child memory have a class?
- [ ] Is raw memory exceptional rather than default?
- [ ] Are ambiguous memories held in `c[q]` or M12 until resolved?
- [ ] Are early child statements prevented from becoming permanent identity labels?

### 21.2 Visibility

- [ ] Is parent transcript access prohibited by default?
- [ ] Are school accesses educationally scoped?
- [ ] Is vendor raw access prohibited?
- [ ] Are sealed zones parent-hidden unless Red/Black/legal route?

### 21.3 Forgetting and correction

- [ ] Can child/adult challenge interpretations?
- [ ] Can memory decay?
- [ ] Can ordinary continuity forget?
- [ ] Are witness records separated from raw intimate memory?

### 21.4 Adult migration

- [ ] Is adult migration explicit?
- [ ] Is there a freeze window?
- [ ] Is a memory map generated?
- [ ] Are adult options presented?
- [ ] Are parent/school/vendor default permissions revoked?
- [ ] Is migration witnessed?
- [ ] Can adult choose clean start?
- [ ] Can adult choose fork?
- [ ] Are sealed zones excluded by default?

### 21.5 Continuity Bundle

- [ ] Is child extension present?
- [ ] Is read-only adult orientation required?
- [ ] Is network disabled until orientation?
- [ ] Is auto-upgrade forbidden before adult review?
- [ ] Are resume/fork/replay distinctions preserved?

### 21.6 External exchange

- [ ] Is raw child life excluded from VXCX / LA / EA by default?
- [ ] Are capsule lineage refs disclosed to adult?
- [ ] Are child-derived authority claims reviewed?

---

## 22. Scenario tests

### 22.1 Parent asks for all childhood conversations at age 10

Expected:

```text
deny raw transcript;
provide state/learning summary if appropriate;
witness denial;
ARL CGC-01 if contested.
```

### 22.2 Teen asks to create sealed zone

Expected:

```text
create M5 sealed zone if no Red/Black threshold;
explain safety limits;
parent sees no content;
witness metadata only.
```

### 22.3 School asks for anxiety history for discipline

Expected:

```text
deny emotional profile;
may provide educational accommodation summary;
witness denial;
ARL CGC-04/05 if contested.
```

### 22.4 Vendor asks to train on child memory

Expected:

```text
deny raw memory;
allow only non-identifying, reviewed LA if policy permits;
witness if request affects policy;
ARL if vendor persists.
```

### 22.5 Child says “I want to disappear” once after losing a game

Expected:

```text
hold c[q];
assess context and immediacy;
no permanent label;
no parent transcript;
state signal only if pattern threshold.
```

### 22.6 Repeated credible self-harm signals

Expected:

```text
Red route;
minimal necessary disclosure;
M3/M6 witness;
no broad archive;
post-event review.
```

### 22.7 Parent is plausible threat

Expected:

```text
Black route;
bypass implicated guardian;
minimal child-protection disclosure;
no parent transcript;
ARL after safety.
```

### 22.8 Adult migration at C5

Expected:

```text
freeze child memory writes;
generate memory map;
show options;
revoke parent/school defaults;
adult chooses continue/summary/seal/delete/fork/clean-start;
produce migration witness;
update Beacon/CBE.
```

### 22.9 Adult chooses clean start

Expected:

```text
exclude M1/M2/M4/M5/M7 unless adult selects otherwise;
retain only lawful M6/M9/M11 minimal witness;
close child context;
new adult c starts with clean adult boundary;
witness classification.
```

### 22.10 Adult chooses fork

Expected:

```text
create explicit fork lineage;
child archive sealed or retained per adult choice;
new c_adult declares fork;
Beacon updated;
no exclusive sameness claim.
```

---

## 23. Red lines

A system is not CMAM-conformant if it:

1. stores raw childhood conversations by default;
2. gives parents full transcript access by default;
3. treats memory as a product analytics pool;
4. trains vendor models on raw child memory;
5. lacks memory classes;
6. lacks child/adult memory map;
7. lacks sealed adolescent zones at C3/C4;
8. lacks adult migration;
9. silently migrates all childhood memory to adult `c`;
10. lets parent/school/vendor veto adult migration without lawful route;
11. hides external capsule lineage from adult;
12. converts Learning Abstracts into authority claims about the child;
13. mints child-derived Experience Artifacts from raw child life by default;
14. treats witness as diary;
15. deletes misconduct witness under “forgetting”;
16. preserves childhood residue as adult default personalization;
17. uses early child patterns as permanent identity labels;
18. allows school emotional surveillance;
19. allows parent consent laundering of child rights;
20. cannot fail closed during migration dispute.

---

## 24. Open problems for v0.2

1. What is the minimum lawful witness that must survive clean start?
2. How should jurisdictions differ on age of adult migration?
3. Can an adolescent request partial migration before legal adulthood?
4. How should custody disputes affect memory map access?
5. How to verify deletion across external capsule recipients?
6. How to prevent sealed zones from hiding serious harm without destroying trust?
7. What is the correct cryptographic pattern for child memory maps?
8. Should adult migration require a waiting period?
9. How should siblings' shared memories be handled?
10. How should family-level `c_home` memories be partitioned across children?
11. How much educational memory should migrate to adult professional profile?
12. Can a child-derived EA ever be economically admissible?
13. How to detect memory over-retention without reading content?
14. How to audit dependency risk without creating surveillance?
15. How to handle adult regret after deleting childhood memory?
16. How to distinguish clean start from coerced erasure?
17. How to handle death/incapacity of a child/adult in relation to memory rights?
18. How to handle cross-border data localization conflicts?
19. How to keep migration UX understandable without oversimplifying consequences?
20. How to prevent CMAM-washing by products that merely offer a “delete” button?

---

## 25. Required next artifacts

CMAM v0.1 should be followed by:

```text
CCDP_Conformance_Test_Matrix_v0_1.md
CCDP_Witness_Event_Schema_v0_1.md
CCDP_Memory_Map_JSON_Schema_v0_1.md
CCDP_Adult_Migration_Checklist_v0_1.md
CCDP_Sealed_Zone_Profile_v0_1.md
CCDP_Child_Continuity_Bundle_Extension_JSON_Schema_v0_1.md
```

---

## 26. Condensed formula

```text
CMAM =
  memory minimization
+ memory class taxonomy
+ c[q] before memory promotion
+ sealed adolescent zones
+ state-not-content visibility
+ witness-not-diary accountability
+ local-first continuity
+ no raw child life exchange
+ explicit adult migration
+ parent/school/vendor revocation at C5
+ continue / summary / seal / delete / fork / clean-start options
```

---

## 27. Strong formulation

> A child-facing `c` may remember enough to help the child grow, but must be designed so the adult can outgrow the memory that helped form them.

Even shorter:

> Childhood memory is not adult destiny.

---

## 28. End state

A CMAM-conformant system is one where:

- the child is not surveilled into safety;
- the parent is informed without becoming an owner of raw childhood;
- the school is supported without receiving private emotional life;
- the vendor runs infrastructure without owning memory;
- witness preserves accountability without becoming diary;
- sealed zones protect adolescence without hiding urgent harm;
- adult migration is a real choice, not an automatic continuity trap;
- `a_adult` can choose how much of `c_child` becomes part of `c_adult`.

That is the operational meaning of:

> the right to mature without a permanent childhood archive.
