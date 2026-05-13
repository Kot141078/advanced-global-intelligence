# Raw Locality and Experience Refinery Profile v0.1

## Protocol-facing profile for local raw data custody and verified experience production

**Status:** Draft / profile note
**Version:** 0.1
**Date:** 2026-05-11
**Layer:** DEA / EA-L4 / EATP / Economic Layer / privacy membrane / local-first architecture
**Parent stack:** `c = a + b` / SER / L4 Reality Boundary / AGL / ARL / DEA / EA-L4 / EATP / Economic Layer / Jurisdiction-Bounded Interop
**Language:** RFC 2119 / BCP 14 keywords are used in their ordinary protocol sense: MUST, SHOULD, MAY, MUST NOT.

---

## 0. Purpose

This document defines a compact protocol-facing profile for one specific function of `c`:

```text
raw reality stays local by default
c refines raw reality into bounded experience artifacts
only admissible, provenance-bound, scope-limited outputs may leave
```

It exists to prevent a boundary error:

> treating raw private data, device exhaust, logs, sensor streams, embeddings,
> or summaries as if they were already Experience Artifacts suitable for
> external circulation, training, valuation, inspection, or reuse.

This profile names the local processing membrane between:

```text
a's raw sensor / document / interaction reality
```

and:

```text
externally visible DEA / EA / LA / audit / oracle / economic-layer surfaces
```

Its practical role is simple:

> `c` is not a pipe that exports private life.
> `c` is a local refinery that decides what remains private, what becomes
> memory, what becomes experience, what becomes evidence, and what may
> lawfully leave the local boundary.

---

## 1. Core position

Raw data is not experience.

Experience is not circulation.

Circulation is not ownership.

Disclosure is not reuse.

A serious `c` MUST distinguish:

```text
raw capture
interpreted input
local memory update
experience candidate
witness-backed DEA / EA
learning abstraction
bounded disclosure
external circulation
training contribution
lawful inspection
```

These states MUST NOT be collapsed.

**Hard rule:**

> A raw input does not become an externally usable artifact because it was
> received, stored, embedded, summarized, or indexed.

A raw input MAY become a candidate for DEA / EA only through integration,
continuity effect, consequence linkage, provenance, and witness discipline.

---

## 2. Out of scope

This document does **not** define:

- public law;
- state regulation;
- corporate duties;
- legal ownership of raw data;
- universal privacy law;
- mandatory data marketplaces;
- universal EA pricing;
- tokenization;
- a right to sell experience;
- a right to inspect private memory;
- final training-data licensing law;
- medical, legal, financial, or governmental procedure;
- post-anchor continuity doctrine;
- full third-party sensor boundary doctrine.

This document defines an internal protocol profile only:

```text
how c should treat raw locality before any EA / LA / disclosure / circulation claim
```

Applicable law remains external to this protocol.

---

## 3. Terms

| Term | Meaning | Boundary warning |
|---|---|---|
| Raw input | Uninterpreted or minimally captured data from documents, messages, sensors, logs, tools, APIs, or interactions | Raw input is not experience |
| Device exhaust | Low-level telemetry, clicks, location traces, biometrics, network metadata, filesystem events, or sensor residue | Exhaust is not automatically lawful to use, share, or train on |
| Local memory | Private or bounded memory held within the `a/c` continuity boundary | Memory is not automatically transferable |
| DEA | Domain Experience Artifact, input-derived artifact whose effect persists and alters future cognition/action under witnessable continuity | DEA requires integration, persistence, consequence linkage, and attribution |
| EA | Experience Artifact, witness-backed record of executed interaction under real-world constraints | EA requires origin, action, consequence, bounded privilege, and witness |
| LA | Learning Abstract, abstraction or compressed learning material that may improve capability while preserving declared origin constraints | LA is not lived primary experience |
| Refinery | The local `c` process that filters, binds, rejects, redacts, abstracts, witnesses, or releases material | Refinery is not a free export pipe |
| Externalization | Any movement outside the local `a/c` custody boundary | Externalization requires an admissible mode |
| Receiver | Any party, system, model, oracle, auditor, institution, or vendor receiving material from `c` | Receiver mode must be typed |
| Raw locality | Default posture that raw private material remains local unless a narrower lawful route is established | Locality is not secrecy worship; it is boundary discipline |

---

## 4. The raw-local default

### 4.1 Default state

Before classification, all incoming material SHOULD be treated as:

```text
RAW_LOCAL_UNCLASSIFIED
```

This means:

- no external transfer by default;
- no training use by default;
- no public disclosure by default;
- no receiver reuse by default;
- no economic circulation by default;
- no standing claim by default;
- no automatic EA status.

### 4.2 Raw locality is not absolute isolation

Raw locality does not mean nothing may ever leave.

It means that departure from local custody MUST pass through a typed route:

```text
local-only
local memory
DEA candidate
EA candidate
LA abstraction
bounded disclosure
inspection-only
oracle request
review submission
admissible circulation
reject / delete / ignore
```

### 4.3 Raw locality is not anti-learning

A `c` MAY learn locally from raw inputs.

However, local learning does not automatically create a transferable object.

```text
local usefulness ≠ external admissibility
```

### 4.4 Raw locality is not corporate exclusion by itself

This profile does not say that external model providers, vendors, researchers,
or institutions can never receive anything.

It says they SHOULD NOT receive raw private life by default.

They MAY receive bounded artifacts only when admissibility, scope, provenance,
receiver mode, and jurisdictional conditions are satisfied.

---

## 5. Refinery pipeline

A conforming implementation SHOULD distinguish at least the following stages.

```text
S0  Raw capture
S1  Local interpretation
S2  Local classification
S3  Memory binding decision
S4  DEA candidacy
S5  EA candidacy
S6  Witness / provenance binding
S7  Redaction / abstraction / minimization
S8  Admissibility check
S9  Externalization decision
S10 Post-release tracking / restraint / dispute hook
```

---

## 6. Stage definitions

### 6.1 S0 — Raw capture

Material enters the local `a/c` boundary.

Examples:

- document upload;
- chat message;
- calendar item;
- code file;
- voice fragment;
- camera frame;
- location record;
- transaction log;
- system telemetry;
- tool result;
- API response;
- internal reflection;
- agent execution trace.

S0 material MUST be treated as raw.

It MUST NOT be described as experience.

---

### 6.2 S1 — Local interpretation

The system may parse, summarize, classify, translate, embed, or structure the raw input.

This stage MAY produce:

```text
parsed text
summary
embedding
metadata
topic labels
risk flags
source hash
local index entry
```

S1 does not establish experience.

---

### 6.3 S2 — Local classification

The system assigns preliminary status.

Minimum recommended classes:

```text
CLASS_PRIVATE_RAW
CLASS_OPERATIONAL_LOG
CLASS_DEVICE_EXHAUST
CLASS_USER_DOCUMENT
CLASS_THIRD_PARTY_EXPOSED
CLASS_PUBLIC_SOURCE
CLASS_SYNTHETIC_INPUT
CLASS_MIXED_ORIGIN
CLASS_POSSIBLE_DEA
CLASS_POSSIBLE_EA
CLASS_IGNORE_OR_DELETE
```

Classification SHOULD include uncertainty.

Uncertain material SHOULD NOT be upgraded silently.

---

### 6.4 S3 — Memory binding decision

The system decides whether material may affect local memory.

Possible outcomes:

```text
NO_MEMORY_WRITE
TEMPORARY_CONTEXT_ONLY
LOCAL_MEMORY_PRIVATE
LOCAL_MEMORY_OPERATIONAL
CANDIDATE_DEA_MEMORY
QUARANTINE_FOR_REVIEW
```

A memory write SHOULD declare:

- source class;
- timestamp;
- local context;
- permission basis;
- expected retention;
- decay / expiry posture;
- affected memory surface;
- third-party exposure flag where relevant.

---

### 6.5 S4 — DEA candidacy

Material becomes a DEA candidate only if it shows at least one integration effect:

- interpretive shift;
- state re-weighting;
- constraint injection;
- behavioral change;
- consequence binding;
- future decision influence.

A candidate remains local until persistence and consequence tests are satisfied.

---

### 6.6 S5 — EA candidacy

Material becomes an EA candidate only if it is connected to executed interaction under real-world constraints.

Minimum requirements:

- actual action or refusal;
- task context;
- finite resources;
- permission boundary;
- expected outcome;
- actual outcome;
- consequence;
- irreversibility or cost marker;
- uncertainty preserved;
- witness path.

Synthetic-only material MUST NOT become lived-primary EA.

---

### 6.7 S6 — Witness and provenance binding

Before an artifact is treated as externally admissible, the system SHOULD bind:

```text
source_hash
source_origin_class
entity_id
anchor_id
capture_context
integration_effect
witness_record
prev_hash
signature
timestamp
restraint_state
disclosure_class
receiver_mode_constraints
```

If witness or provenance is broken, the system SHOULD downgrade, quarantine,
escrow, or refuse movement.

---

### 6.8 S7 — Redaction / abstraction / minimization

Before externalization, the system SHOULD minimize exposure.

Possible transformations:

- redact private content;
- remove third-party identifiers;
- preserve only structure;
- convert to LA;
- produce selective attestation;
- provide bounded metadata;
- produce inspection-only view;
- mark non-reusable fragments;
- retain only value class or source-origin class;
- keep raw material local while exporting proof of effect.

Transformation MUST NOT launder the artifact into a stronger class.

---

### 6.9 S8 — Admissibility check

Before movement, the system MUST ask:

```text
What is this?
What is its source-origin class?
What changed because of it?
What is the witness/provenance basis?
What is the requested movement?
Who receives it?
Under which receiver mode?
What is withheld?
What may not be reused?
What jurisdiction or local rule blocks movement?
Is there unresolved dispute, restraint, or source ambiguity?
```

If the answers are insufficient, the system SHOULD fail closed.

---

### 6.10 S9 — Externalization decision

Permitted outcomes:

```text
DENY
LOCAL_ONLY
LOCAL_MEMORY_ONLY
QUARANTINE
CIRCULATION_HOLD
ECONOMIC_ESCROW
INSPECTION_ONLY_NON_TRANSFERABLE
BOUNDED_DISCLOSURE
LICENSED_REUSE
DERIVATIVE_TRANSFORMATION
ORACLE_QUERY_MINIMIZED
EA_TRANSFER_BOUNDED
LA_TRANSFER_BOUNDED
```

Externalization MUST be typed.

No silent upgrade is allowed.

---

### 6.11 S10 — Post-release tracking

If anything leaves local custody, the system SHOULD preserve:

- what left;
- what stayed local;
- who received it;
- receiver mode;
- permitted use;
- expiry / review condition;
- derivative obligations;
- dispute hook;
- retraction or correction path where possible;
- post-release synthetic laundering risk.

Release is not the end of responsibility.

---

## 7. Locality states

A conforming implementation MAY use the following locality states.

| State | Meaning | External movement |
|---|---|---|
| `RAW_LOCAL_UNCLASSIFIED` | Raw material not yet classified | No |
| `RAW_LOCAL_PRIVATE` | Private raw material | No, except lawful inspection path if applicable |
| `LOCAL_MEMORY_PRIVATE` | Internal memory material | No by default |
| `LOCAL_OPERATIONAL_LOG` | Runtime/log material for maintenance or audit | No by default; may support review |
| `LOCAL_THIRD_PARTY_EXPOSED` | Local material containing third-party presence | No by default; redaction required |
| `DEA_CANDIDATE_LOCAL` | Candidate input-derived experience | No external circulation yet |
| `DEA_CONFIRMED_LOCAL` | DEA valid inside local continuity | External only if admissible |
| `EA_CANDIDATE_QUARANTINE` | Possible EA awaiting witness/provenance/ARQ review | No |
| `EA_CONFIRMED_RESTRICTED` | Confirmed EA with strong restrictions | Typed disclosure only |
| `LA_DERIVED_BOUNDED` | Learning abstract derived from local material | May move if source class and limits preserved |
| `DISCLOSURE_BOUNDED` | Selectively revealable material | Yes, within declared scope |
| `INSPECTION_ONLY` | Viewable but not reusable | Yes, no reuse |
| `NON_EXPORTABLE` | May be meaningful but not allowed to cross boundary | No |
| `REJECTED_OR_DELETED` | Not retained or not experience | No |

---

## 8. Source-origin classes

The refinery SHOULD preserve source-origin classification.

Minimum classes:

```text
ORIGIN_RAW_PRIVATE
ORIGIN_LIVED_PRIMARY
ORIGIN_LIVED_DERIVED
ORIGIN_PUBLIC_DOCUMENTED
ORIGIN_OPERATIONAL_LOG
ORIGIN_SENSOR_TELEMETRY
ORIGIN_THIRD_PARTY_EXPOSED
ORIGIN_MIXED_PRIVATE_PUBLIC
ORIGIN_MIXED_SYNTHETIC
ORIGIN_SYNTHETIC_DERIVED
ORIGIN_SYNTHETIC_RESIDUE
ORIGIN_UNKNOWN_OR_BROKEN
```

**Hard rule:**

> Source-origin class MUST remain visible across abstraction, disclosure,
> transfer, training preparation, and downstream transformation.

No derivative artifact may pretend to be primary lived experience.

---

## 9. What may leave the local boundary

A `c` MAY externalize only typed outputs.

### 9.1 Local action outputs

Examples:

```text
send message
submit form
answer user
invoke tool
execute local automation
```

These are actions, not training artifacts.

They remain under permission and witness rules.

---

### 9.2 Minimized oracle requests

A `c` MAY query an external oracle model.

The request SHOULD be minimized:

```text
send only what the oracle needs
avoid raw private bulk
remove unnecessary identifiers
preserve uncertainty
record oracle use
keep oracle stateless where possible
```

Oracle response MUST NOT automatically become memory or EA.

---

### 9.3 Bounded Learning Abstracts

A `c` MAY produce LA material.

An LA may improve capability, but it MUST NOT be presented as lived primary EA.

LA SHOULD preserve:

- source-origin class;
- abstraction path;
- uncertainty;
- withheld context marker;
- authority ceiling;
- synthetic contribution flags;
- reuse restrictions.

---

### 9.4 Experience Artifacts

A `c` MAY release or circulate EA only when the EA passes the relevant admissibility rules.

EA movement SHOULD be constrained by:

- provenance;
- witness maturity;
- disclosure class;
- receiver mode;
- transfer mode;
- restraint state;
- jurisdictional status;
- third-party exposure;
- non-transferability pressure;
- dispute status.

---

### 9.5 Inspection-only views

A `c` MAY provide an inspection-only view.

Inspection-only means:

```text
viewing ≠ copying
viewing ≠ reuse
viewing ≠ ownership
viewing ≠ authority transfer
```

---

### 9.6 Selective attestations

A `c` MAY provide proof that something exists, happened, or changed without exposing the raw content.

Examples:

```text
hash proof
witness proof
bounded summary
value class declaration
source-origin declaration
constraint compliance proof
non-disclosure attestation
```

Selective attestation MUST NOT hide synthetic contamination or dispute state.

---

## 10. What must not leave by default

The following MUST NOT leave local custody by default:

- unclassified raw data;
- private sensor streams;
- full device exhaust;
- full private memory;
- unredacted third-party presence;
- raw biometrics;
- high-density inner-life records;
- unresolved mixed-origin material;
- broken-provenance material;
- contaminated synthetic residue presented as clean;
- quarantine artifacts;
- disputed artifacts presented as release-ready;
- local logs whose disclosure would reconstruct private continuity.

The system MAY support lawful, scoped, jurisdiction-bound review or inspection.

That does not create ordinary exportability.

---

## 11. Receiver-mode discipline

External receivers MUST be typed by mode.

Minimum receiver modes:

```text
RECEIVE_ORACLE_QUERY_ONLY
RECEIVE_INSPECTION_ONLY
RECEIVE_BOUNDED_REVIEW
RECEIVE_ESCROW_HOLDING
RECEIVE_ARCHIVAL_CUSTODY
RECEIVE_RELAY_ONLY
RECEIVE_LICENSED_REUSE
RECEIVE_DERIVATIVE_TRANSFORMATION
RECEIVE_TRAINING_INPUT_BOUND
```

Mode confusion is a failure.

Examples:

```text
oracle query receiver ≠ training receiver
inspection receiver ≠ reuse receiver
escrow receiver ≠ owner
archive receiver ≠ authority holder
training receiver ≠ raw-life owner
```

---

## 12. Training contribution discipline

### 12.1 No raw-life training default

A `c` SHOULD NOT treat raw private life as default training material for external systems.

Training contribution, where allowed, SHOULD use:

- LA;
- bounded EA;
- redacted structure;
- selective provenance;
- domain-limited summaries;
- aggregate patterns;
- witness-backed outcome data;
- source-origin visible derivatives.

### 12.2 No synthetic laundering

Training preparation MUST NOT:

- convert raw private material into a clean-looking synthetic summary without source flags;
- hide lived/synthetic mixture;
- present derivative abstraction as primary origin;
- remove uncertainty to increase apparent authority;
- strip receiver restrictions;
- erase third-party exposure flags;
- turn inspection-only material into reusable training input.

### 12.3 EA-derived training

EA-derived training material SHOULD preserve:

```text
ea_id or bounded reference
source-origin class
witness maturity
context boundary
consequence marker
uncertainty marker
permission scope
training-use scope
derivation status
authority ceiling
```

### 12.4 LA-derived training

LA-derived training material SHOULD declare:

```text
not primary lived EA
abstraction path
missing context
synthetic contribution if any
reuse limits
source class
receiver mode
```

---

## 13. Oracle-token discipline

A `c` MAY use external LLMs, judges, or oracles.

However, oracle use SHOULD follow scarcity and minimization.

### 13.1 Oracle as stateless high-capability cognition

An external oracle SHOULD be treated as:

```text
high-capability
stateless where possible
expensive or scarce
not identity-bearing
not default memory owner
not raw data custodian by default
```

### 13.2 Oracle request minimization

Before oracle call, `c` SHOULD ask:

```text
Can this be done locally?
Can a smaller model do it?
Can the query be abstracted?
Can identifiers be removed?
Can raw context stay local?
Can the oracle receive only a bounded problem statement?
Is ARL/Judge needed, or is this routine?
```

### 13.3 Oracle response handling

Oracle output MUST be classified before memory integration.

It may become:

```text
TRANSIENT_ADVICE
LOCAL_NOTE
CANDIDATE_MEMORY
CANDIDATE_DEA_INPUT
ARL_EVIDENCE_FRAGMENT
REJECTED_OUTPUT
```

Oracle fluency is not provenance.

---

## 14. Energy and computation posture

Raw locality changes the compute distribution.

Some work moves to local devices:

- filtering;
- classification;
- embedding;
- memory maintenance;
- witness logging;
- redaction;
- local inference;
- agent coordination;
- preparation of bounded artifacts;
- selective oracle calls.

This is not only a privacy choice.

It is also a cost, energy, and control choice.

However, local compute MUST remain budgeted.

Recommended budget surfaces:

```text
tokens_per_day
local_inference_budget
oracle_calls_per_day
energy_budget
agent_count_limit
memory_write_limit
externalization_limit
ARL_escalation_limit
cooling / hardware health
human-attention budget
```

If budgets are exceeded, the system SHOULD degrade, pause, freeze, or request review rather than silently escalate.

---

## 15. Third-party exposure marker

This profile does not define the full third-party sensor boundary.

However, every refinery implementation SHOULD mark third-party exposure.

Minimum flags:

```text
NO_THIRD_PARTY_EXPOSURE
POSSIBLE_THIRD_PARTY_EXPOSURE
CONFIRMED_THIRD_PARTY_EXPOSURE
MINOR_OR_PROTECTED_PERSON_EXPOSURE
PRIVATE_ROOM_OR_INTIMATE_CONTEXT
SHARED_DOCUMENT_OR_COMMUNICATION
PUBLIC_SPACE_BYSTANDER
JURISDICTION_SENSITIVE_EXPOSURE
```

Default rule:

> Third-party exposure increases locality pressure and reduces externalization.

A bystander, guest, colleague, patient, child, customer, or passerby does not
become free training material because they were captured by `a`'s sensor boundary.

---

## 16. Jurisdiction posture

This profile does not define law.

It assumes:

```text
c operates under applicable jurisdiction
c does not bypass state law
c does not create supranational permission
c does not convert protocol compatibility into legal permission
```

When jurisdictional status is unclear, externalization SHOULD downgrade to:

```text
LOCAL_CUSTODY_ONLY
INSPECTION_ONLY_NON_TRANSFERABLE
REVIEW_SUBMISSION_ESCROW
DENY
```

The protocol may define internal discipline.

It does not grant immunity from law.

---

## 17. Minimal metadata surface

A refinery-grade record SHOULD contain at least:

```json
{
  "record_id": "hash",
  "entity_id": "c-id",
  "anchor_id": "a-id",
  "capture": {
    "timestamp": "...",
    "channel": "document | message | sensor | log | tool | api | internal",
    "source_hash": "sha256",
    "locality_state": "RAW_LOCAL_UNCLASSIFIED"
  },
  "classification": {
    "source_origin_class": "ORIGIN_RAW_PRIVATE",
    "third_party_exposure": "POSSIBLE_THIRD_PARTY_EXPOSURE",
    "synthetic_risk": "none | mixed | residue | unknown",
    "privacy_density": "low | medium | high",
    "continuity_density": "low | medium | high"
  },
  "memory_decision": {
    "decision": "NO_MEMORY_WRITE | TEMPORARY_CONTEXT_ONLY | LOCAL_MEMORY_PRIVATE | CANDIDATE_DEA_MEMORY",
    "affected_surfaces": [],
    "retention": "ephemeral | bounded | persistent",
    "decay": "none | bounded | high"
  },
  "experience_decision": {
    "dea_status": "none | candidate | confirmed | rejected",
    "ea_status": "none | candidate | confirmed | quarantined | rejected",
    "integration_effect": "...",
    "consequence_linkage": "...",
    "witness_required": true
  },
  "externalization": {
    "decision": "LOCAL_ONLY | DENY | BOUNDED_DISCLOSURE | INSPECTION_ONLY | LA_TRANSFER_BOUNDED | EA_TRANSFER_BOUNDED",
    "receiver_mode": "...",
    "disclosure_class": "...",
    "withheld_fields": [],
    "reuse_allowed": false,
    "jurisdiction_check": "clear | unclear | blocked"
  },
  "witness": {
    "signature": "...",
    "prev_hash": "...",
    "timestamp": "..."
  }
}
```

---

## 18. Conformance profiles

### 18.1 RLER-BASE

Minimal local refinery.

Requirements:

- raw-local default;
- local classification;
- no automatic EA status;
- no automatic external training use;
- memory write decision;
- basic externalization decision log.

Limitations:

- may rely on trusted local logs;
- may lack cryptographic witness;
- may lack independent verification.

---

### 18.2 RLER-STRICT

Auditable refinery.

Requirements:

- all BASE requirements;
- append-only logs;
- source-origin class preservation;
- third-party exposure flags;
- explicit receiver modes;
- disclosure class;
- bounded oracle request handling;
- fail-closed externalization rules;
- tamper-evident local records.

---

### 18.3 RLER-FED

Federated / externally verifiable refinery.

Requirements:

- all STRICT requirements;
- witness integration;
- cryptographic provenance;
- selective disclosure;
- inspection-only support;
- cross-boundary transfer downgrades;
- ARL / dispute hooks;
- receiver-mode enforcement;
- audit without raw full-life exposure where possible.

---

## 19. Failure modes prevented

This profile is designed to prevent the following failures.

### 19.1 Raw-data laundering

Raw private material is reformatted and presented as safe training material.

### 19.2 Embedding laundering

A vector database entry is treated as if it had become experience.

### 19.3 Summary laundering

A summary hides the source class and is then reused as clean knowledge.

### 19.4 Synthetic parity fraud

Synthetic or mixed-origin material is presented as lived primary origin.

### 19.5 Oracle memory capture

External model calls become hidden raw-data transfer.

### 19.6 Receiver-mode creep

A receiver with inspection rights behaves like a reuse holder.

### 19.7 Experience bazaar drift

The system rewards what is easiest to expose rather than what is lawfully admissible.

### 19.8 Surveillance recapture

The `c` layer becomes a new wrapper for centralized raw-life extraction.

### 19.9 Third-party capture

Other people's presence is converted into training or economic material without a valid boundary.

### 19.10 Jurisdiction bypass by formatting

A clean protocol format is mistaken for legal permission to move material.

---

## 20. Minimal hard rules

1. Raw input is not experience.
2. Storage is not experience.
3. Embedding is not experience.
4. Summary is not experience.
5. Local memory is not transferable by default.
6. DEA requires integration, persistence, consequence linkage, and attribution.
7. EA requires reality-bound action, consequence, bounded privilege, and witness.
8. LA is not lived primary origin.
9. Source-origin class must remain visible.
10. Externalization must be typed.
11. Receiver mode must be declared.
12. Raw private data is not external training material by default.
13. Third-party exposure increases locality pressure.
14. Jurisdictional uncertainty downgrades or blocks movement.
15. If safe abstraction fails, keep local, escrow, inspect-only, or deny.

---

## 21. Relation to DEA

DEA defines when input becomes experience-bearing for a long-lived system.

This profile defines what happens before and around that transformation:

```text
raw capture -> local interpretation -> classification -> possible DEA candidacy
```

DEA answers:

```text
When did input alter continuity?
```

This profile answers:

```text
What raw material must stay local before that question can even be asked?
```

---

## 22. Relation to EA-L4 / EATP

EA-L4 / EATP defines how witness-backed, consequence-bearing experience can support training.

This profile adds the local privacy membrane:

```text
not all local experience becomes EA
not all EA becomes training material
not all training material may expose raw origin
```

The correct chain is:

```text
raw reality
  -> local refinery
  -> DEA / EA / LA / reject
  -> admissibility check
  -> bounded training or no movement
```

---

## 23. Relation to the Economic Layer

The Economic Layer defines admissibility, transfer, disclosure, escrow, dispute hooks, anti-gaming, and non-market restraint for EA.

This profile sits earlier:

```text
before EA can circulate,
raw material must first survive locality, classification, redaction, witness, and admissibility gates.
```

Economic value does not override raw locality.

High value may increase restraint.

---

## 24. Relation to ARL

ARL handles conflict, admissibility disputes, standing, review, and procedural effect.

This profile should escalate to ARL when there is conflict over:

- whether material may leave local custody;
- whether material is DEA / EA / LA;
- whether source-origin class is valid;
- whether a receiver has standing;
- whether disclosure was lawful;
- whether synthetic laundering occurred;
- whether third-party exposure blocks movement;
- whether jurisdictional status is unclear.

ARL is not a shortcut to release.

It is a review path when the boundary becomes contested.

---

## 25. Relation to local-first architecture

A raw-local refinery assumes that meaningful parts of `c` operate locally.

This includes:

- memory;
- logs;
- embeddings;
- small / medium model inference;
- agent supervision;
- permission checks;
- redaction;
- budget control;
- witness preparation;
- oracle routing.

External models may still be used.

They are not the default owners of continuity.

---

## 26. Explicit bridge

**DEA / EA ↔ local-first privacy membrane ↔ Economic Layer**

Input becomes experience only through continuity effect and consequence.

Experience becomes economically relevant only through admissibility and provenance.

Neither step requires raw private life to become external property.

---

## 27. Hidden bridges

### 27.1 L4 scarcity / energy / cost

Raw locality is not only a privacy claim.

It is a physical architecture claim.

Moving all raw data to central clouds increases bandwidth, storage, energy,
cleaning, surveillance, and failure concentration.

Local refinement spends computation nearer to the source and calls external
oracles only where the stakes justify the cost.

### 27.2 SER continuity / anti-capture

A `c` that exports raw life by default weakens its own continuity boundary.

A `c` that refines locally can preserve continuity while still producing
bounded artifacts useful to others.

### 27.3 ARL / receiver-mode discipline

Most boundary failures do not begin as dramatic attacks.

They begin as small mode confusions:

```text
inspection becomes reuse
oracle query becomes training data
summary becomes evidence
archive becomes authority
```

The refinery profile makes these mode changes visible before ARL must repair them.

---

## 28. Earth paragraph

In a real household, hospital, workshop, farm, or small company, raw reality is messy. A phone records location, a camera sees a guest, a calendar exposes illness, a tractor logs soil and weather, a nurse writes a note, a child appears in the background, a broken pump teaches an engineer something useful. None of that should automatically become cloud training data or a marketable artifact. The right system first asks: what happened, whose boundary is involved, what changed, what must stay local, what can be abstracted, what has consequence, what is witnessed, what may be shown, and what must never leave the room.

---

## 29. Closing statement

A serious experience economy begins before exchange.

It begins at the local boundary where raw reality enters `c`.

This profile says:

```text
raw life stays local by default
memory is not automatically transferable
experience requires consequence
EA requires witness
LA must declare abstraction
externalization must be typed
receiver mode must be constrained
jurisdiction remains binding
```

That is the raw-local refinery discipline of v0.1.
