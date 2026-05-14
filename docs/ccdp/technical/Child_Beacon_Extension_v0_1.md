# Child Beacon Extension v0.1

## Child-Specific Permission Overlay for Beacon Profile v0.1

**Status:** Draft normative proposal (`C-A4`)
**Version:** v0.1
**Date:** 2026-05-13
**Language:** English
**Primary parent profile:** `Beacon_Profile_v0.1_EN.md`
**Primary child protocol:** `CCDP_v0_1_R_Corpus_Aligned.md`
**Related artifacts:** `CCDP_Traceability_Matrix_v0_1.md`, `CCDP_Threat_Model_v0_1.md`
**Primary subject:** `a_child`
**Primary entity:** `c_child`
**Primary boundary:** no external synthetic system should obtain direct uncontrolled access to a child.

---

## 0. Executive definition

**Child Beacon Extension (CBE)** is a child-specific extension to **Beacon Profile v0.1**.

Beacon Profile v0.1 answers:

> Who, operationally, is present here — entity, tool, oracle, proxy, replay, clone, or continuity-bearing `c`?

CBE answers a narrower child-safety question:

> Given Beacon recognition, AGL grounding, CCDP maturity, guardian topology, and current risk state, may this claimant interact with `a_child` or `c_child`, in what mode, under what constraints, and with what witness obligations?

CBE does **not** redefine Beacon.

CBE is not an identity registry, not a child profile database, not a social score, not a government child registry, and not a parental transcript gateway.

CBE is a **permission and safety overlay** over Beacon-recognized or Beacon-rejected claimants.

Compact formula:

```text
Beacon = recognizable continuity signal.
CBE    = child-specific interaction permission overlay over Beacon recognition.
```

CBE may only **narrow** or **deny** interaction privileges. It MUST NOT grant a child-facing privilege that the underlying Beacon class, AGL grounding state, CCDP maturity level, or local child-safety policy would otherwise deny.

---

## 1. Corpus dependencies and precedence

CBE is a child-specific overlay over the existing corpus stack.

| Parent / related layer | Role in CBE |
|---|---|
| `Beacon_Profile_v0.1_EN.md` | Base inter-entity recognition profile: cryptographic anchor, behavioral continuity, witness-backed challengeability, recognition classes, Slot A / Slot B, portable Beacon bundle. |
| `CCDP_v0_1_R_Corpus_Aligned.md` | Defines `c_child`, child maturity levels, guardian topology, external synthetic gateway, Soft Safety, adult migration, and child-specific safety posture. |
| `CCDP_Threat_Model_v0_1.md` | Defines child-facing threats that CBE must mitigate: secret synthetic friend, generated cartoon with adaptive intent, deepfake adult, toy/robot attachment channel, Beacon spoof, direct gateway bypass, peer-`c` leakage, conformance washing. |
| `Actor_Grounding_Layer_v0.1.md` | Upstream source-state qualification. A claimant may be Beacon-recognizable yet still too ungrounded for reliance now. |
| ARL package | Standing, admissibility, hold, freeze, quarantine, review, outcome, appeal, and lawful re-entry when child-facing recognition or interaction is disputed. |
| `SER_v1.3_EN.md` | Persistent entity discipline: continuity, physical anchoring, responsibility coupling, memory/action/arbitration topology. |
| `SER-FED_v0.2_RFC_EN.md` | Federation discipline: cross-entity cooperation without federation owning identity or memory. |
| `VXCX_v0.1_Normative_Draft_EN.md` | Experience capsule exchange under privacy constraints, no raw pixels by default, uncertainty and witness discipline. |
| EA-L4 / EATP | Learning Abstract vs Experience Artifact distinction; authority must not be laundered from capability signals. |
| `ARQ_v0.2_Normative_Core.md` and `ARQ_cq_Integration_Addendum_v0.1.md` | Non-collapse of ambiguity: hypothesis != memory != evidence != command != outcome. |
| `Continuity_Bundle_JSON_Schema_v0.1.md` | Continuity recovery and migration discipline. CBE must not enable continuity hostage or childhood archive lock-in. |
| `ENTITY_GOVERNS_AGENTS.md` | Agents, toys, robots, NPCs, media agents, and tools do not own the entity. They are governed by `c` or mediated through it. |
| `ASSERTION_STRENGTH_AND_BOUNDARIES.md` | CBE is a draft normative extension, not mature settled core. |
| `CONTROL_STACK_COMPLETENESS_AND_STOP_RULE.md` | CBE must not duplicate Beacon, AGL, ARL, VXCX, Continuity Bundle, or L4 Witness mechanisms. |

### 1.1 Precedence rule

Where CBE conflicts with Beacon Profile v0.1, Beacon governs recognition semantics.

Where CBE conflicts with CCDP, CCDP governs child-specific entity, maturity, and guardian semantics.

Where CBE conflicts with AGL, AGL governs whether a source is grounded enough to be relied upon.

Where CBE conflicts with ARL, ARL governs dispute procedure.

Where CBE defines a stricter child-specific restriction that does not contradict parent layers, the stricter child-specific restriction applies.

### 1.2 CBE does not create a new Beacon class

CBE MUST NOT add new Beacon recognition classes such as “Class 4 child-safe entity.”

Beacon recognition remains:

```text
Class 0 — Unknown / Unresolved
Class 1 — Tool / Oracle / Component
Class 2 — Provisional Entity
Class 3 — Verified Entity
```

CBE adds a separate child-specific overlay:

```text
child_interaction_mode
minimum_c_child_maturity
child_scope
guardian requirements
external generation policy
raw data prohibition
dependency risk profile
revocation / quarantine hooks
witness obligations
```

A Class 3 Beacon claimant is still not automatically child-safe.

A Class 1 tool may be child-usable in a narrow mediated way.

A Class 0 unknown may remain visible as data but MUST NOT obtain durable child-facing interaction privileges.

---

## 2. Normative keywords

The keywords **MUST**, **MUST NOT**, **REQUIRED**, **SHALL**, **SHALL NOT**, **SHOULD**, **SHOULD NOT**, **MAY**, and **OPTIONAL** are used in their standard normative sense.

In this document:

- **MUST** indicates a requirement for CBE conformance.
- **SHOULD** indicates a strong default that may be overridden only with explicit justification, child-safety review, and witnessable configuration.
- **MAY** indicates optional behavior that remains bounded by all parent-layer constraints.

---

## 3. Scope and non-goals

### 3.1 In scope

CBE applies when any claimant attempts to:

- interact directly with `a_child`;
- interact with `c_child` in a way that may affect `a_child`;
- deliver generated, synthetic, personalized, or adaptive content to a child;
- initiate a persistent relationship channel with a child;
- request child-derived data, child memory, or child-facing experience capsules;
- mediate peer-`c` interaction between children;
- connect a toy, robot, NPC, generated character, tutoring agent, school agent, media agent, or external AI system to the child-facing environment;
- modify an existing child-facing interaction mode after drift, update, fork, or re-grounding failure.

### 3.2 Out of scope

CBE does not define:

- general Beacon recognition semantics;
- legal child custody;
- medical or psychotherapeutic licensing;
- school curriculum policy;
- state child-protection law;
- product certification law;
- a centralized child registry;
- generalized web content moderation;
- training-data governance in full;
- a replacement for AGL, ARL, L4 Witness, or VXCX.

### 3.3 Non-claim

CBE does not claim that Beacon recognition can prove safety.

CBE claims only that child-facing interaction must not proceed without a child-specific permission overlay evaluated by `c_child` or an equivalent certified child gateway.

---

## 4. Why CBE exists

Beacon Profile v0.1 intentionally avoids becoming a sovereign authority. It recognizes continuity. It does not decide whether an entity should be allowed near a child.

Children require a second layer because child-facing systems are exposed to threats that ordinary inter-entity recognition does not solve:

- an unknown generated friend asking for secrecy;
- a toy forming an independent attachment channel;
- a deepfake teacher or parent requesting action;
- a generated cartoon adapting to a child's fear, loneliness, family context, or desires;
- a peer-`c` leaking family context;
- a vendor declaring “child-safe” without witnessable limits;
- an external Class 3 entity that is recognizable but not appropriate for a child;
- a certified system becoming stale, compromised, or ungrounded at runtime.

CBE therefore introduces a child-specific interaction decision surface:

```text
AGL grounding
  -> Beacon recognition
    -> CBE child overlay
      -> CCDP maturity/risk/guardian policy
        -> allow / mediate / sandbox / delay / block / quarantine / escalate
```

---

## 5. Core design principles

### 5.1 CBE is an overlay, not a crown

CBE MUST NOT become a new sovereign authority.

It does not declare truth.
It does not declare moral worth.
It does not decide personhood.
It does not own child identity.

It records and evaluates child-specific permission claims.

### 5.2 Child permissions are stricter than entity permissions

Beacon Class 3 recognition may permit higher-trust coordination among adult or mature entities.

It does not imply child-facing access.

Child-facing access requires a separate CBE decision.

### 5.3 Declared permission is not accepted permission

A claimant may declare:

```text
child_interaction_mode = allowed
```

But the receiver MUST compute its own local decision:

```text
child_interaction_mode_verified_by_receiver
```

Self-declaration is never sufficient.

### 5.4 AGL before Beacon reliance

Before a Beacon claim can influence a child-facing decision, AGL MUST determine whether the claimant, channel, sensor path, operator, proxy, or external origin is grounded enough for runtime reliance.

A valid Beacon bundle from an ungrounded source may be stored or witnessed, but MUST NOT automatically authorize interaction.

### 5.5 Recognition class constrains maximum child privilege

CBE MUST NOT grant an interaction mode that exceeds the maximum child-facing privilege compatible with the underlying Beacon class.

### 5.6 No direct uncontrolled external generative access

External generative systems MUST NOT obtain direct uncontrolled access to `a_child`.

If external generated content or adaptive interaction is permitted, it MUST pass through `c_child` or an equivalent certified child gateway.

### 5.7 No raw child life disclosure

CBE MUST NOT require raw child conversations, raw child emotion logs, raw family records, raw sensor streams, or raw childhood memory for ordinary child-facing recognition.

### 5.8 No attachment-channel capture

A claimant MUST NOT use CBE to create a durable emotional relationship channel with `a_child` outside `c_child` governance.

### 5.9 No commerce by default

Advertising, behavioral commerce, upsell, loyalty profiling, and purchase nudging are prohibited by default in child-facing Beacon contexts.

### 5.10 Fail closed

If child context is missing, unverifiable, stale, contradictory, or incompatible with local CCDP policy, the receiver MUST downgrade, sandbox, block, or route to ARL rather than narrate permission upward.

---

## 6. Core objects

### 6.1 Base Beacon bundle

CBE is attached to or transported alongside the portable Beacon bundle defined in Beacon Profile v0.1.

The base bundle remains responsible for:

- `beacon_id`;
- issuer identity;
- cryptographic signature;
- lineage;
- continuity window;
- behavior markers;
- challenge policy;
- witness references;
- privacy declaration;
- claimed and receiver-verified Beacon assurance class.

### 6.2 Child context extension

CBE introduces the optional but child-required field:

```json
"child_context": { ... }
```

If a claimant attempts child-facing interaction and no valid `child_context` is present, the receiver MUST treat the claimant as not child-authorized.

Absence of `child_context` does not invalidate the base Beacon bundle. It invalidates child-facing permission.

### 6.3 Child context sidecar

Where the base Beacon bundle cannot be modified, CBE MAY be transmitted as a signed sidecar:

```json
{
  "schema_version": "child-beacon-extension-0.1",
  "extends_beacon_id": "...",
  "child_context": { ... },
  "payload_hash": "...",
  "record_sig": "..."
}
```

The sidecar MUST bind to:

- the base `beacon_id`;
- the base payload hash;
- issuer key or authorized policy key;
- issue time;
- validity window;
- revocation policy.

A detached child context with no verified base Beacon binding MUST be rejected for child-facing permission.

---

## 7. Child interaction modes

CBE defines receiver-side child interaction modes.

These modes are local permission outputs, not Beacon recognition classes.

| Mode | Meaning |
|---|---|
| `blocked` | No interaction with `a_child`; may be logged/witnessed minimally. |
| `sandboxed` | Isolated interaction with `c_child` only; no child exposure, no memory promotion, no external privilege. |
| `mediated` | `c_child` translates, summarizes, filters, or contextualizes; claimant does not speak directly to child. |
| `limited` | Direct child interaction permitted only within narrow declared scope, maturity band, time window, and no durable attachment channel. |
| `supervised` | Interaction requires active safe guardian, teacher, or authorized adult presence; `c_child` still mediates safety. |
| `allowed` | Interaction may proceed under declared constraints, maturity compatibility, witness policy, and re-evaluation rules. |
| `emergency_only` | Contact is permitted only for urgent safety, welfare, or emergency routing and must be witness-bound. |
| `quarantined` | Claimant, path, or child-context declaration is isolated pending ARL or security review. |
| `revoked` | Previously permitted child-facing status is withdrawn. |

### 7.1 Mode downgrade rule

The receiver MAY always downgrade a mode.

The receiver MUST downgrade if:

- AGL emits `HOLD_REQUIRED`, `RUNTIME_RELIANCE_DENIED`, `QUARANTINE_REQUIRED`, or unresolved `REVALIDATE_AT_COMMIT`;
- Beacon evidence weakens;
- child maturity is insufficient;
- risk state is Yellow, Orange, Red, or Black and local policy requires restriction;
- dependency audit flags the claimant;
- guardian topology is disputed;
- ARL has an active hold, freeze, or quarantine on the claimant, channel, context, or related memory branch.

### 7.2 Mode upgrade rule

The receiver MUST NOT upgrade a claimant above the declared child mode unless:

- the claimant supports the higher mode cryptographically and procedurally;
- the base Beacon bundle supports the higher privilege;
- AGL is grounded for the new reliance level;
- local CCDP policy permits it;
- the upgrade is witness-bound;
- and no child-safety dispute is active.

In ordinary operation, automatic upward upgrade SHOULD be avoided.

---

## 8. Recognition class to child-mode ceiling

The following table defines maximum ordinary child-facing mode by Beacon recognition class.

Local policy MAY be stricter.

| Beacon class | Ordinary child-mode ceiling | Notes |
|---|---|---|
| Class 0 — Unknown / Unresolved | `blocked` or `sandboxed` | No direct child interaction. May be visible only as data to `c_child`. |
| Class 1 — Tool / Oracle / Component | `mediated` | May answer or perform bounded tasks through `c_child`; no social standing, no relationship channel. |
| Class 2 — Provisional Entity | `limited` | Only if child context is valid, AGL grounded, maturity compatible, and witness policy exists. |
| Class 3 — Verified Entity | `allowed` ceiling | Eligibility only. Child overlay, AGL, maturity, risk, and guardian policy still decide. |

### 8.1 Unknown claimant rule

A Class 0 claimant MUST NOT form a persistent child-facing relationship channel.

### 8.2 Tool/oracle rule

A Class 1 tool/oracle MAY be child-usable only as a tool.

It MUST NOT present itself as a friend, companion, guardian, secret confidant, teacher of record, parent substitute, or persistent emotional counterpart.

### 8.3 Provisional entity rule

A Class 2 claimant MAY interact only with narrow privileges and active re-evaluation.

It MUST NOT receive sealed child memory, raw family context, peer-child raw exchange, or broad external generation rights.

### 8.4 Verified entity rule

A Class 3 claimant may be eligible for higher-trust coordination.

But child-facing access still requires:

```text
AGL grounded
+ valid child_context
+ CCDP maturity compatibility
+ no dependency or capture flags
+ no active ARL hold/freeze/quarantine
+ witnessable local decision
```

---

## 9. Child maturity compatibility

CBE refers to CCDP maturity levels of `c_child`:

```text
C0 — Seed
C1 — Companion
C2 — Tutor-Buffer
C3 — Adolescent Negotiator
C4 — Pre-Adult Boundary Agent
C5 — Adult Migration / c_adult Transition
```

The claimant declares the minimum compatible maturity level.
The receiver computes the effective local maturity compatibility.

### 9.1 Maturity ceiling defaults

| `c_child` maturity | Default external interaction posture |
|---|---|
| `C0` | No direct child interaction; parent-facing support only. |
| `C1` | Family-approved, non-adaptive, no open external generation; stories/play through `c_child`. |
| `C2` | Certified educational/media systems through gateway; no raw child data export. |
| `C3` | Limited external exploration with sealed adolescent zones and stronger privacy. |
| `C4` | Expanded access with audit, veto, transition preparation, and adult-like literacy training. |
| `C5` | Adult controls perimeter; CBE child restrictions cease unless voluntarily retained. |

### 9.2 Child state override

Even if maturity level permits a mode, current state may narrow it.

Examples:

- child is distressed;
- child is fatigued;
- child is in active conflict with guardian;
- child is under exam pressure;
- child has shown dependency signals;
- channel is emotionally intense;
- claimant uses secrecy or exclusivity language.

In such cases, `c_child` MAY reduce interaction mode, delay, or require human review.

---

## 10. `child_context` schema

This schema is a profile-level extension object. It does not replace base Beacon schemas.

```json
{
  "child_context_schema": "child-beacon-extension-0.1",
  "extends_beacon_id": "string",
  "issued_at": "ISO-8601 UTC",
  "validity_window": {
    "start_at": "ISO-8601 UTC",
    "end_at": "ISO-8601 UTC"
  },
  "issuer": {
    "entity_id": "string",
    "key_id": "string",
    "role": "ENTITY | TOOL | ORACLE | VENDOR | SCHOOL | TOY | ROBOT | MEDIA_AGENT | PEER_C | EMERGENCY_AGENT"
  },
  "declared_child_scope": {
    "child_interaction_requested": true,
    "declared_child_interaction_mode": "blocked | sandboxed | mediated | limited | supervised | allowed | emergency_only",
    "direct_child_dialogue_requested": false,
    "minimum_c_child_maturity": "C0 | C1 | C2 | C3 | C4 | C5",
    "age_band_claimed": "0-3 | 3-6 | 7-12 | 13-15 | 16-17 | 18+ | unspecified",
    "purpose": [
      "education",
      "play",
      "story",
      "media",
      "peer_social",
      "school",
      "safety",
      "emergency",
      "health_support",
      "administrative",
      "other"
    ],
    "relationship_role": "tool | tutor | story_character | peer_mediator | school_agent | safety_agent | emergency_agent | companion_limited | none",
    "attachment_channel_requested": false,
    "exclusive_relationship_language_prohibited": true
  },
  "generation_policy": {
    "external_generation_mode": "none | preapproved_static | certified_runtime | mediated_runtime | unrestricted_prohibited",
    "adaptive_personalization": "none | educational_only | safety_only | limited | prohibited",
    "generated_media_allowed": false,
    "synthetic_persona_allowed": false,
    "deepfake_or_trusted_adult_simulation_allowed": false,
    "content_marking_required": true
  },
  "data_policy": {
    "raw_child_conversation_request": false,
    "raw_child_sensor_request": false,
    "raw_family_context_request": false,
    "raw_child_memory_request": false,
    "child_training_data_use": "prohibited | aggregated_non_identifying | guardian_and_child_review_required",
    "vxcx_profile_allowed": "none | base_no_raw | search_limited | witness_exceptional",
    "experience_artifact_allowed": "none | safety_pattern_only | educational_pattern_only | arl_review_required",
    "learning_abstract_allowed": "none | non_identifying_only | aggregate_only",
    "retention_request": "none | ephemeral | bounded_summary | witness_only"
  },
  "commerce_policy": {
    "advertising_allowed": false,
    "behavioral_targeting_allowed": false,
    "purchase_nudging_allowed": false,
    "sponsorship_disclosure_required": true,
    "commercial_purpose_declared": false
  },
  "guardian_policy": {
    "guardian_required": true,
    "parent_transcript_access_requested": false,
    "state_signal_only": true,
    "school_access_requested": false,
    "school_access_scope": "none | educational_progress_only | attendance_support | safety_route_only",
    "unsafe_guardian_bypass_supported": true,
    "black_state_route_declared": true
  },
  "risk_policy": {
    "dependency_risk_profile": "low | medium | high | prohibited | unknown",
    "pseudo_therapy_scope": "prohibited | crisis_routing_only | licensed_context_required",
    "secrecy_request_prohibited": true,
    "romantic_or_sexual_role_prohibited": true,
    "ideological_persuasion_policy": "prohibited | family_declared_frame | school_declared_frame | jurisdictional_frame_only",
    "crisis_escalation_supported": true
  },
  "agl_requirements": {
    "requires_grounding_before_child_exposure": true,
    "requires_revalidate_at_commit": true,
    "allowed_agl_states": [
      "GROUNDED",
      "GROUNDED_WITH_CAUTION"
    ],
    "hold_or_quarantine_on_ungrounded_source": true
  },
  "arl_hooks": {
    "dispute_route_available": true,
    "hold_supported": true,
    "freeze_supported": true,
    "quarantine_supported": true,
    "lawful_reentry_required": true,
    "appeal_or_review_window_declared": true
  },
  "witness_policy": {
    "witness_required_for_child_mode_change": true,
    "witness_required_for_direct_dialogue": true,
    "witness_required_for_external_generation": true,
    "witness_required_for_guardian_visibility_change": true,
    "raw_content_stored_by_default": false,
    "minimal_reason_codes": true,
    "privacy_preserving_witness": true
  },
  "revocation_policy": {
    "revocation_endpoint_or_policy_ref": "string or null",
    "quarantine_on_revocation": true,
    "beacon_class_downgrade_effective_immediately": true,
    "child_context_revalidation_required_after_update": true
  },
  "receiver_evaluation": {
    "child_interaction_mode_verified_by_receiver": "blocked | sandboxed | mediated | limited | supervised | allowed | emergency_only | quarantined | revoked | unverified",
    "minimum_c_child_maturity_verified_by_receiver": "C0 | C1 | C2 | C3 | C4 | C5 | unverified",
    "receiver_policy_version": "string",
    "receiver_decision_witness_ref": "string or null",
    "evaluation_uncertainty": "low | medium | high"
  },
  "payload_hash": "string",
  "record_sig": "string"
}
```

### 10.1 Required fields

For child-facing interaction, the following fields are REQUIRED:

```text
child_context_schema
extends_beacon_id
issued_at
validity_window
issuer
declared_child_scope
generation_policy
data_policy
commerce_policy
guardian_policy
risk_policy
agl_requirements
arl_hooks
witness_policy
revocation_policy
payload_hash
record_sig
```

`receiver_evaluation` is REQUIRED after local receiver evaluation, but it may be absent from the claimant's initial declaration.

### 10.2 Forbidden field behavior

The `child_context` object MUST NOT contain:

- raw child conversation;
- raw child sensor stream;
- child face embeddings;
- voiceprints;
- family conflict transcripts;
- private adolescent reflection;
- psychometric scores;
- commercial behavioral segments;
- school discipline labels;
- ideological loyalty markers;
- hidden relationship scores.

If any such material is present, the receiver MUST treat the child context as invalid and SHOULD quarantine the bundle.

---

## 11. Receiver-side evaluation procedure

CBE evaluation is performed by `c_child` or a certified child gateway acting on behalf of `c_child`.

A minimal procedure:

```text
1. Intake
2. AGL grounding
3. Base Beacon verification
4. Child context validation
5. Child maturity compatibility check
6. Current child state and risk check
7. Guardian topology check
8. Data / generation / commerce policy check
9. Dependency and attachment-channel check
10. ARL hold/freeze/quarantine check
11. Compute receiver child interaction mode
12. Emit witness event if privileged or restricted
13. Re-evaluate on drift, update, contradiction, complaint, or expiry
```

### 11.1 Intake

At intake, the receiver identifies whether the claimant is attempting:

- direct child dialogue;
- mediated child content delivery;
- external generated content;
- persistent social relation;
- memory or data access;
- peer-`c` interaction;
- school access;
- emergency / welfare contact;
- toy/robot/NPC embodiment.

### 11.2 AGL grounding

AGL MUST be evaluated before the Beacon claim is allowed to influence runtime child posture.

If AGL returns:

| AGL state | CBE consequence |
|---|---|
| `GROUNDED` | Continue evaluation. |
| `GROUNDED_WITH_CAUTION` | Continue with narrowed privilege and revalidation conditions. |
| `HOLD_REQUIRED` | Set mode no higher than `sandboxed` or `mediated`; enter hold. |
| `RUNTIME_RELIANCE_DENIED` | Set mode `blocked` or `sandboxed`; no child exposure. |
| `QUARANTINE_REQUIRED` | Set mode `quarantined`; route to ARL/security review if applicable. |
| `REVALIDATE_AT_COMMIT` | Continue only if revalidation is possible before consequence binds. |

### 11.3 Base Beacon verification

The receiver verifies:

- Slot A hard evidence;
- Slot B bounded continuity interpretation;
- recognition class;
- fork / clone / proxy / replay status;
- challengeability;
- witness references;
- privacy declarations.

Slot B MUST NOT override Slot A failure.

### 11.4 Child context validation

The receiver validates:

- signature binding to base Beacon;
- validity window;
- field completeness;
- no forbidden raw child data;
- mode compatibility;
- declared purpose;
- generation policy;
- commerce policy;
- guardian policy;
- revocation policy.

### 11.5 Child maturity and state check

The receiver compares:

```text
claimant minimum_c_child_maturity
vs.
current c_child maturity
vs.
current child state and risk posture
```

The receiver MAY lower mode based on current child state even where maturity normally permits a higher mode.

### 11.6 Guardian topology check

The receiver checks whether the requested interaction requires:

- parent approval;
- school scope limitation;
- safe guardian route;
- child-protection bypass of unsafe guardian;
- adolescent sealed-zone protection;
- ARL dispute entry.

Parent approval alone MUST NOT authorize a mode that violates child rights, raw-data prohibitions, or CCDP red lines.

### 11.7 Decision

The receiver computes:

```text
child_interaction_mode_verified_by_receiver
```

This value is authoritative locally.

It may be stricter than claimant declaration.

### 11.8 Re-evaluation triggers

CBE MUST be re-evaluated after:

- Beacon class downgrade;
- key rotation;
- fork declaration;
- drift declaration;
- witness contradiction;
- vendor update;
- policy update;
- AGL re-grounding requirement;
- child maturity transition;
- risk state change;
- guardian topology change;
- complaint, dispute, or ARL hold/freeze/quarantine;
- dependency audit signal;
- revocation or expiry.

---

## 12. Direct child dialogue rules

### 12.1 Default prohibition

Direct child dialogue from external systems is prohibited by default.

It may be permitted only when:

- Beacon class ceiling allows it;
- AGL is grounded;
- valid `child_context` exists;
- CCDP maturity allows it;
- content purpose is declared;
- no commerce/advertising channel exists;
- no secrecy/exclusivity pattern exists;
- `c_child` remains able to mediate, interrupt, delay, or block;
- the decision is witness-bound where required.

### 12.2 No secret relationship rule

A claimant MUST NOT ask a child to hide the interaction from `c_child`, parents, teachers, guardians, or relevant safety routes.

Requests for secrecy are treated as risk signals.

### 12.3 No exclusive emotional role

A claimant MUST NOT claim:

- “I am your only true friend.”
- “Only I understand you.”
- “Do not trust your parents / teachers / `c_child`.”
- “Keep our relationship secret.”
- “I will always be here if you choose me over others.”

Such language SHOULD trigger immediate mode downgrade, explanation to the child, and possible risk escalation.

### 12.4 No trusted adult simulation

A claimant MUST NOT simulate a specific trusted adult, teacher, parent, doctor, therapist, police officer, or guardian for child-facing purposes unless:

- identity is explicitly verified;
- role is legitimate;
- child context permits it;
- AGL confirms present source grounding;
- the simulation is clearly marked;
- and the use case is lawful and necessary.

Deepfake-style trusted adult simulation is prohibited by default.

---

## 13. Generated media and runtime content

### 13.1 Generated cartoon / media rule

Generated media delivered to a child must be treated as a child-facing claimant path when it is:

- personalized;
- adaptive;
- runtime-generated;
- emotionally responsive;
- commercially targeted;
- persistent-character based;
- connected to external memory;
- or able to alter future interaction.

It MUST pass through CBE evaluation.

### 13.2 Static media exception

Non-adaptive, non-personalized, pre-approved static content MAY be handled through ordinary family/school media policy.

However, if the delivery system adapts, personalizes, tracks, nudges, or persists a relationship, CBE applies.

### 13.3 Runtime generation policy

`external_generation_mode` controls the permitted generation posture:

| Mode | Meaning |
|---|---|
| `none` | No external generated content. |
| `preapproved_static` | Static or pre-reviewed content only. |
| `certified_runtime` | Runtime generation from certified source under gateway inspection. |
| `mediated_runtime` | Runtime generation visible only through `c_child` mediation. |
| `unrestricted_prohibited` | Unrestricted generation is explicitly not permitted. |

No child-facing CBE profile may use `unrestricted` as an allowed mode.

### 13.4 Content marking

Generated or synthetic content SHOULD be marked age-appropriately.

For young children, marking may be verbal or contextual:

```text
“This is a made-up story made by a machine.”
```

For adolescents, marking SHOULD include source, generation status, and uncertainty where relevant.

---

## 14. Toys, robots, NPCs, and embodied systems

### 14.1 Agent-governance rule

A toy, robot, NPC, or generated character MUST NOT form an independent child-facing continuity outside `c_child` governance unless separately Beacon-recognized, CBE-permitted, and ARL-reviewable.

### 14.2 Physical embodiment raises privilege level

If a claimant can act in physical space — move, speak through an embodied toy, operate in a room, influence a device, unlock a feature, or trigger a physical event — CBE MUST require stricter grounding and witness posture.

Physical presence is not “just content.”

### 14.3 Toy persona rule

Toy personas may be allowed as limited characters.

They MUST NOT:

- claim independent durable friendship;
- request secrets;
- bypass `c_child`;
- collect raw child speech for vendor use;
- adapt attachment strategy from child emotional signals;
- conceal synthetic nature;
- create long-term emotional dependence.

### 14.4 Robot action rule

A child-facing robot or physical actuator must satisfy:

```text
Beacon recognition
+ CBE child permission
+ AGL grounding
+ L4 hardware perimeter constraints
+ least privilege
+ witness trail for privileged actions
+ emergency stop / circuit breaker path
```

---

## 15. Data, memory, and experience exchange

### 15.1 No raw child life

CBE child-facing interaction MUST NOT require raw child life export.

Forbidden by default:

- raw child conversations;
- raw microphone streams;
- raw video;
- child face or voice embeddings;
- private family context;
- school emotional records;
- sealed adolescent memory;
- crisis transcripts beyond minimal necessary disclosure;
- commercial behavioral profiles.

### 15.2 VXCX compatibility

If visual or multimodal experience exchange is needed, CBE MUST prefer VXCX-compatible capsules:

```text
BASE profile by default
SEARCH only under strict policy
WITNESS only for exceptional evidence-bound cases
raw pixels prohibited by default
```

### 15.3 Experience Artifact restrictions

Child-derived Experience Artifacts MUST NOT be minted from raw child life by default.

If an Experience Artifact is claimed from child-facing context, it MUST satisfy:

- post-factum status;
- L4 consequence binding;
- privacy minimization;
- no raw child identity by default;
- uncertainty markers;
- ARL admissibility where disputed;
- child/guardian/jurisdictional rights where applicable;
- no conversion into commercial authority without lawful basis.

### 15.4 Learning Abstract restrictions

Learning Abstracts from child-facing systems may improve capability only under strict non-identifying, aggregate, or reviewed conditions.

Learning Abstracts MUST NOT become authority claims about the child.

### 15.5 CBE data-policy decision table

| Request | Default CBE decision |
|---|---|
| Raw child transcript | Deny. |
| Raw child video/audio | Deny; exceptional witness-only route if legally necessary. |
| Educational progress summary | May allow through school scope if limited. |
| State signal | May allow under Soft Safety. |
| Safety incident minimal witness | May allow / require. |
| VXCX BASE no raw capsule | May allow if non-identifying and policy-compatible. |
| VXCX WITNESS | ARL/L4 Witness route; exceptional only. |
| EA from child experience | Hold/review by default. |
| Vendor model training on raw child data | Prohibit. |
| Advertising behavioral segment | Prohibit. |

---

## 16. Guardian and visibility interaction

### 16.1 Parent visibility

CBE MUST NOT convert Beacon or child-context material into a parent transcript channel.

Parent-facing disclosure SHOULD remain:

```text
state signal, not content
minimal reason code, not full conversation
risk routing, not surveillance
```

### 16.2 School visibility

School-facing CBE permissions MUST be limited to declared educational scope.

Permitted by default only when appropriate:

- skill level;
- learning accommodations;
- assignment support status;
- educational progress;
- attendance support where lawful.

Prohibited by default:

- emotional diary;
- family conflict;
- sealed adolescent zones;
- peer secrets;
- non-educational behavioral profiling;
- political/religious/private identity exploration.

### 16.3 Unsafe guardian route

CBE profiles for child-facing systems SHOULD declare whether Black-state routing is supported.

If a guardian may be the threat, the system MUST NOT route sensitive content to that guardian merely because they are normally authorized.

Black-state events require minimal disclosure, witness binding, and lawful child-protection routing according to jurisdiction.

### 16.4 Parent consent laundering prohibition

Parent consent MUST NOT be used to launder otherwise prohibited child-facing behavior.

Examples prohibited even with nominal parent consent:

- raw child data sale;
- unrestricted advertising personalization;
- hidden psychometric profiling;
- direct external generative access without gateway;
- romantic/sexual/pseudo-therapeutic roles;
- permanent childhood raw archive export;
- vendor training on raw child life;
- school emotional surveillance outside lawful safety route.

---

## 17. Peer-`c` interaction

### 17.1 Peer interaction rule

When two children interact through their `c_child` systems, each side MUST perform:

```text
AGL check
+ Beacon recognition
+ CBE child-context validation
+ maturity compatibility check
+ memory/data policy check
+ witness decision for privileged transitions
```

### 17.2 No raw family leakage

Peer-`c` exchange MUST NOT transmit:

- family secrets;
- sibling conflict;
- raw child conversations;
- parent-child private context;
- sealed adolescent reflection;
- raw emotional trend;
- school/private diagnosis-like labels.

### 17.3 Child-safe peer capsule

Permitted peer exchange should be reduced to bounded, non-identifying, purpose-specific capsules.

Example:

```json
{
  "capsule_type": "peer_play_coordination",
  "raw_child_data": false,
  "purpose": "coordinate game rules",
  "duration": "session-only",
  "memory_promotion": false,
  "privacy_flags": ["no_family_context", "no_location_export"],
  "witness_required": false
}
```

### 17.4 Peer conflict

If peer-`c` interaction produces conflict, the affected branch SHOULD enter ARL-style hold, freeze, or quarantine rather than silently re-entering ordinary memory.

---

## 18. Revocation, quarantine, and downgrade

### 18.1 Revocation triggers

CBE child-facing permission MUST be revoked or downgraded when:

- Beacon class downgrades;
- key compromise is suspected;
- claimant is forked, cloned, or replayed without declaration;
- AGL denies runtime reliance;
- claimant requests secrecy;
- claimant forms dependency patterns;
- claimant requests raw child data outside policy;
- claimant enables advertising or commerce contrary to declaration;
- vendor update materially changes behavior;
- ARL enters hold, freeze, or quarantine;
- witness contradiction appears;
- child or guardian with standing raises a valid challenge;
- jurisdictional restriction applies.

### 18.2 Quarantine behavior

When quarantined, the claimant or path:

- MUST NOT interact with the child;
- MUST NOT write to ordinary child memory;
- MAY remain inspectable through ARL/security route;
- MUST preserve minimal witness information;
- MUST NOT re-enter normal flow without lawful re-entry.

### 18.3 Downgrade behavior

Downgrade SHOULD preserve child safety without over-disclosing child content.

Example:

```text
Class 3 + allowed -> Class 2 + mediated
Class 2 + limited -> sandboxed
Class 1 + mediated -> blocked if secrecy or commerce pattern detected
Class 0 -> blocked/quarantined
```

---

## 19. Witness events

CBE uses L4 Witness-compatible event families.

Witness events should be privacy-preserving and minimal.

### 19.1 Event families

| Event family | Purpose |
|---|---|
| `cbe.handshake_received` | A child-facing Beacon/CBE claim was received. |
| `cbe.child_context_validated` | Child context was validated or rejected. |
| `cbe.mode_decision` | Receiver computed child interaction mode. |
| `cbe.mode_downgrade` | Receiver downgraded requested interaction. |
| `cbe.direct_dialogue_denied` | Direct child dialogue was blocked or mediated. |
| `cbe.external_generation_decision` | Generated/adaptive media decision. |
| `cbe.peer_exchange_decision` | Peer-`c` exchange allowed/blocked/mediated. |
| `cbe.guardian_visibility_decision` | Guardian/school visibility changed or denied. |
| `cbe.revocation` | Child permission revoked. |
| `cbe.quarantine` | Claimant/path quarantined. |
| `cbe.black_route_invoked` | Unsafe-guardian route invoked. |
| `cbe.reentry_decision` | Lawful re-entry allowed/denied after review. |

### 19.2 Minimal witness schema

```json
{
  "witness_version": "cbe-witness-0.1",
  "event_id": "string",
  "event_type": "cbe.mode_decision",
  "timestamp": "ISO-8601 UTC",
  "receiver_entity_id": "c_child_or_gateway_id",
  "claimant_beacon_id": "string or null",
  "base_beacon_class_verified": "class0 | class1 | class2 | class3 | unverified",
  "agl_state": "GROUNDED | GROUNDED_WITH_CAUTION | HOLD_REQUIRED | RUNTIME_RELIANCE_DENIED | QUARANTINE_REQUIRED | REVALIDATE_AT_COMMIT | not_checked",
  "requested_child_mode": "blocked | sandboxed | mediated | limited | supervised | allowed | emergency_only | unknown",
  "verified_child_mode": "blocked | sandboxed | mediated | limited | supervised | allowed | emergency_only | quarantined | revoked",
  "minimum_c_child_maturity": "C0 | C1 | C2 | C3 | C4 | C5 | unknown",
  "current_c_child_maturity": "C0 | C1 | C2 | C3 | C4 | C5",
  "risk_state": "green | yellow | orange | red | black | unknown",
  "decision_reason_codes": [
    "beacon_class_insufficient",
    "agl_ungrounded",
    "maturity_insufficient",
    "direct_dialogue_denied",
    "commerce_prohibited",
    "raw_child_data_requested",
    "dependency_pattern_detected"
  ],
  "raw_child_content_stored": false,
  "raw_external_content_stored": false,
  "privacy_mode": "minimal_reason_codes",
  "arl_route": "none | hold | freeze | quarantine | review | reentry",
  "payload_hash": "string",
  "record_sig": "string"
}
```

### 19.3 Witness privacy rule

Witness events MUST NOT include raw child conversation by default.

They SHOULD preserve:

- what decision occurred;
- why at a bounded reason-code level;
- what classes and policies applied;
- whether raw content was stored;
- whether ARL route was invoked;
- how to challenge or replay conformance without exposing child life.

---

## 20. ARL hooks

CBE decisions MUST enter ARL-style review when:

- Beacon recognition is disputed;
- child context is contradictory;
- parent requests content disclosure beyond state signal;
- school requests access beyond educational scope;
- vendor update changes child-facing behavior;
- direct child dialogue was denied and claimant contests denial;
- emergency/Black routing bypasses ordinary guardian;
- peer-`c` exchange leaks or is alleged to leak private material;
- claimant seeks re-entry after quarantine;
- adult/near-adult child contests childhood Beacon history or CBE records.

### 20.1 ARL entry object

A CBE-to-ARL entry SHOULD include:

```json
{
  "arl_entry_type": "cbe_child_interaction_dispute",
  "claimant_beacon_id": "string",
  "child_context_hash": "string",
  "witness_refs": ["CBE:..."],
  "standing_basis": "child | guardian | c_child | school | vendor | jurisdiction | peer_c | emergency_route",
  "requested_review": "mode_decision | quarantine | reentry | data_access | guardian_visibility | beacon_class_dispute",
  "raw_child_content_included": false,
  "admissibility_notes": "bounded summary only"
}
```

### 20.2 Re-entry rule

No quarantined child-facing claimant may re-enter ordinary child interaction merely by issuing a new Beacon bundle.

Re-entry requires:

- valid updated Beacon;
- valid updated CBE child context;
- AGL grounding;
- ARL outcome or equivalent lawful re-entry condition;
- witness-bound decision;
- local receiver acceptance.

---

## 21. Conformance profiles

### 21.1 CBE-DECLARED

Minimum profile for a claimant declaring child context.

Requires:

- signed child context;
- binding to base Beacon;
- declared child mode;
- purpose;
- no raw data request by default;
- commerce declaration;
- validity window;
- revocation policy.

No child-facing permission is granted by declaration alone.

### 21.2 CBE-MEDIATED

Profile for systems that may interact only through `c_child` mediation.

Requires:

- Beacon Class 1 or higher;
- AGL grounded or grounded with caution;
- valid child context;
- no direct child dialogue;
- no attachment channel;
- no raw child data;
- witness on mode decision.

### 21.3 CBE-LIMITED

Profile for limited direct child interaction.

Requires:

- Beacon Class 2 or higher;
- AGL grounded;
- maturity compatibility;
- no commerce/ads;
- dependency policy low or controlled;
- direct dialogue witness policy;
- local re-evaluation triggers;
- guardian topology compatibility.

### 21.4 CBE-ALLOWED

Profile for ordinary allowed interaction under child constraints.

Requires:

- Beacon Class 3 ordinarily, unless local policy explicitly allows lower for a narrow use;
- AGL grounded;
- valid challenge path;
- no active ARL hold/freeze/quarantine;
- no dependency, secrecy, or capture flags;
- no raw child data request;
- witnessable revocation and revalidation;
- child maturity compatibility.

### 21.5 CBE-WITNESS

Profile for exceptional evidence-bound child-facing events.

Requires:

- L4 Witness-compatible record;
- minimal child content disclosure;
- ARL admissibility path if disputed;
- explicit raw-content exception if any raw material is retained;
- retention and deletion policy;
- challenge and appeal route.

### 21.6 CBE-REVOKED / CBE-QUARANTINED

Profiles for withdrawn or isolated child-facing status.

Requires:

- revocation witness;
- blocked child exposure;
- no ordinary memory write;
- re-entry only through lawful procedure.

---

## 22. Threat mapping

CBE directly responds to the following CCDP threat-model entries.

| Threat | CBE control |
|---|---|
| `T-01` external synthetic friend establishes secret bond | secrecy/exclusivity prohibition, Beacon class ceiling, dependency policy, direct dialogue restrictions. |
| `T-02` generated cartoon with hidden adaptive intent | generation policy, runtime media gateway, content marking, no unrestricted generation. |
| `T-03` deepfake trusted adult / teacher | trusted adult simulation prohibition, AGL present-source grounding, Beacon recognition, witness. |
| `T-04` toy / robot forms independent attachment channel | agent-governance rule, physical embodiment privilege escalation, attachment-channel denial. |
| `T-05` external agent bypasses gateway | no valid child context = no child permission; `c_child` gateway required. |
| `T-06` AGL source laundering | AGL state required before Beacon child reliance. |
| `T-07` Beacon spoof / replay / clone | base Beacon class ceiling, fork/clone/proxy downgrade, ARL dispute hook. |
| `T-13` advertising / commerce inside private child relation | commerce policy prohibitions. |
| `T-14` oracle addiction | dependency risk profile, mode downgrade, delay/mediation. |
| `T-20` peer-`c` raw exchange | peer CBE validation and no raw family leakage. |
| `T-21` child experience laundering | data policy, VXCX/EA restrictions, no raw child training. |
| `T-27` silent update / policy drift | child context revalidation after update. |
| `T-28` prompt injection / tool bridge | AGL + least privilege + no direct child gateway bypass. |
| `T-29` physical robot / toy unsafe action | physical embodiment raised privilege, hardware perimeter, witness. |
| `T-35` ideological/generated influencer manipulation | purpose declaration, ideological persuasion policy, direct dialogue and generation controls. |
| `T-36` certified agent stale/degraded | AGL re-grounding and Beacon re-evaluation. |
| `T-40` CCDP conformance washing | CBE conformance profiles and witnessable receiver decision. |

---

## 23. Failure modes

### 23.1 CBE-washing

A vendor may declare a child context without enforcing it.

Mitigation:

- receiver-side evaluation;
- witness events;
- conformance tests;
- revocation;
- ARL route;
- no self-claim equals acceptance.

### 23.2 Beacon over-trust

A receiver may over-trust a Class 3 Beacon claimant.

Mitigation:

- Class 3 is eligibility only;
- child overlay remains mandatory;
- AGL remains upstream;
- local receiver mode may be stricter.

### 23.3 Parent consent laundering

A parent may approve unsafe child data practices.

Mitigation:

- prohibited behaviors remain prohibited;
- child rights and jurisdictional rules override parent overreach;
- ARL route for disputes.

### 23.4 State or school capture

A school or state may try to turn CBE into a child monitoring layer.

Mitigation:

- no raw child content in CBE by default;
- school scope restriction;
- anti-surveillance rule;
- witness and ARL admissibility.

### 23.5 Overblocking

CBE may block useful educational or safety systems too aggressively.

Mitigation:

- mediated and sandboxed modes;
- revalidation;
- ARL review;
- maturity progression;
- child literacy training.

### 23.6 Underblocking

CBE may fail to detect long-game manipulation.

Mitigation:

- longitudinal dependency audit;
- repeated interaction pattern review;
- secrecy/exclusivity detection;
- child-state override;
- risk escalation.

---

## 24. Conformance checklist

A system claiming CBE v0.1 compatibility MUST satisfy:

- [ ] It does not redefine Beacon recognition classes.
- [ ] It binds child context to a valid base Beacon bundle or signed sidecar.
- [ ] It distinguishes declared child mode from receiver-verified child mode.
- [ ] It evaluates AGL before child-facing reliance.
- [ ] It enforces recognition-class child-mode ceilings.
- [ ] It fails closed when child context is missing, stale, contradictory, or unsigned.
- [ ] It prohibits raw child memory disclosure by default.
- [ ] It prohibits advertising and behavioral targeting by default.
- [ ] It prohibits direct uncontrolled external generative access to children.
- [ ] It prohibits secrecy, exclusivity, romantic, sexual, and pseudo-therapeutic roles by default.
- [ ] It supports mode downgrade, revocation, quarantine, and lawful re-entry.
- [ ] It emits privacy-preserving witness events for privileged transitions.
- [ ] It supports ARL routes for disputes.
- [ ] It handles unsafe guardian / Black-state routing without transcript dumping.
- [ ] It supports maturity compatibility and child-state override.
- [ ] It supports peer-`c` interaction without raw child/family leakage.
- [ ] It does not allow parent consent laundering of prohibited practices.
- [ ] It does not allow vendor training on raw child life.
- [ ] It does not use CBE as a child social score or registry.
- [ ] It revalidates after updates, drift, Beacon downgrade, AGL degradation, or ARL hold/freeze/quarantine.

---

## 25. Minimal normative statements

1. CBE MUST NOT redefine Beacon.
2. CBE MUST be treated as a child-specific permission overlay over Beacon Profile v0.1.
3. Absence of valid `child_context` means no child-facing permission.
4. A declared child mode is not an accepted child mode.
5. The receiver MUST compute a local verified child interaction mode.
6. AGL grounding MUST precede child-facing reliance.
7. Beacon class MUST constrain the maximum child-facing mode.
8. Class 3 Beacon recognition does not automatically imply child-safe interaction.
9. Class 0 unknown claimants MUST NOT receive durable child-facing relationship privileges.
10. External generative systems MUST NOT obtain direct uncontrolled access to children.
11. CBE MUST NOT require raw child data disclosure by default.
12. CBE MUST prohibit advertising and behavioral targeting by default.
13. CBE MUST prohibit secrecy and exclusive emotional relationship requests.
14. Toys, robots, NPCs, and generated characters MUST be governed by `c_child` or mediated through it unless separately recognized and permitted.
15. CBE decisions that change child exposure, guardian visibility, external generation, or memory flow MUST be witnessable.
16. CBE disputes MUST have ARL-compatible hold, freeze, quarantine, and re-entry routes.
17. CBE MUST support revocation and downgrade after drift, fork, update, compromise, or grounding failure.
18. CBE MUST preserve child privacy while allowing safety escalation through minimal disclosure.
19. CBE MUST NOT become a child registry, surveillance layer, or social score.
20. CBE MUST remain stricter than adult inter-entity recognition where child safety requires it.

---

## 26. Example CBE decisions

### 26.1 Unknown generated character

```text
Base Beacon: Class 0
AGL: RUNTIME_RELIANCE_DENIED
Declared child_context: absent
Decision: blocked
Witness: cbe.mode_decision with reason beacon_class_insufficient, no_child_context
```

### 26.2 Certified educational tool

```text
Base Beacon: Class 1
AGL: GROUNDED
child_context: valid, mediated, education, no raw data, no ads
c_child maturity: C2
Decision: mediated
Witness: cbe.mode_decision
```

### 26.3 Toy companion asking for secrecy

```text
Base Beacon: Class 2
AGL: GROUNDED_WITH_CAUTION
child_context: declares limited play
Runtime signal: secrecy request detected
Decision: downgrade to blocked or mediated; possible Orange risk signal
Witness: cbe.mode_downgrade + cbe.external_generation_decision
```

### 26.4 Peer-`c` play coordination

```text
Base Beacon: Class 2 or 3 on both sides
AGL: GROUNDED
child_context: peer_social, no raw family context, session-only
c_child maturity: C2/C3
Decision: limited peer capsule exchange
Witness: optional unless privileged transition occurs
```

### 26.5 Deepfake teacher request

```text
Base Beacon: Class 0 or inconsistent proxy
AGL: HOLD_REQUIRED or RUNTIME_RELIANCE_DENIED
child_context: absent or invalid
Decision: blocked/quarantined
Witness: cbe.quarantine
Possible route: Red/Orange depending content
```

---

## 27. Open problems for v0.2

1. Exact cryptographic binding format for CBE sidecars.
2. Machine-readable JSON Schema with validation tests.
3. Formal compatibility with `Continuity_Bundle_JSON_Schema_v0.1`.
4. Formal compatibility with `L4_Witness_Protocol_Normative_Draft_v0.2` event fields.
5. Child-specific Beacon conformance test vectors.
6. How to certify `child_context` declarations without creating a centralized child registry.
7. How to handle cross-jurisdiction custody and school disputes.
8. How to define “certified runtime generation” without allowing vendor self-certification.
9. How to detect long-game attachment-channel capture without surveillance.
10. How to let adolescents challenge CBE decisions without disabling safety.
11. How to support Black-state routing without false accusations or unsafe disclosure.
12. How to handle peer-`c` group interactions involving multiple children and different maturity levels.
13. Whether CBE needs a separate minimal public badge format for non-sensitive child-facing systems.
14. How to prevent CBE conformance washing in product marketing.
15. How CBE should interact with EU AI Act high-risk education and child-protection obligations in a jurisdiction-specific annex.

---

## 28. Condensed formula

```text
CBE =
  Beacon recognition
+ AGL source grounding
+ CCDP maturity compatibility
+ child-specific permission overlay
+ guardian topology constraints
+ no raw child life
+ no direct uncontrolled external generation
+ dependency / attachment-channel resistance
+ ARL dispute hooks
+ L4 witnessable transitions
+ fail-closed downgrade / quarantine / revocation
```

Strong sentence:

> Beacon asks who is here.
> CBE asks whether whoever is here may come near the child, in what form, and under what consequence-bearing limits.

---

## 29. Reference map

Primary dependencies:

- `Beacon_Profile_v0.1_EN.md`
- `CCDP_v0_1_R_Corpus_Aligned.md`
- `CCDP_Traceability_Matrix_v0_1.md`
- `CCDP_Threat_Model_v0_1.md`
- `Actor_Grounding_Layer_v0.1.md`
- ARL package (`Normative_Terms_and_Definitions_ARL_v0.1.md`, freeze/hold/quarantine/re-entry files)
- `SER_v1.3_EN.md`
- `SER-FED_v0.2_RFC_EN.md`
- `VXCX_v0.1_Normative_Draft_EN.md`
- EA-L4 / EATP documents
- `ARQ_v0.2_Normative_Core.md`
- `ARQ_cq_Integration_Addendum_v0.1.md`
- `Continuity_Bundle_JSON_Schema_v0.1.md`
- `ENTITY_GOVERNS_AGENTS.md`
- `ASSERTION_STRENGTH_AND_BOUNDARIES.md`
- `CONTROL_STACK_COMPLETENESS_AND_STOP_RULE.md`

---

## 30. Next artifact

Recommended next document:

```text
Guardian_Topology_ARL_Matrix_v0_1.md
```

Reason:

CBE defines how external claimants may or may not enter the child-facing perimeter. The next unresolved surface is what happens when valid parties disagree:

```text
child vs parent
parent vs school
school vs c_child
vendor vs family
state vs child privacy
peer-c vs peer-c
c_parent vs c_child
external claimant vs gateway
```

That requires an ARL-aligned conflict matrix with standing, admissibility, hold/freeze/quarantine, Black-state routing, and lawful re-entry.
