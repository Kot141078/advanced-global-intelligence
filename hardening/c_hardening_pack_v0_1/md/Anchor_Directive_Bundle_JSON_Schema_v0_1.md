# Anchor Directive Bundle JSON Schema v0.1

## Machine-readable directive object for post-anchor handling, successor anchoring, memory modes, witness, review, and jurisdictional handoff

**Status:** Normative draft schema / hardening support profile v0.1
**Version:** v0.1
**Date:** 2026-06-02
**Document ID:** `Anchor_Directive_Bundle_JSON_Schema_v0_1`
**Short name:** `ADB v0.1`
**Primary object:** `ANCHOR_DIRECTIVE_BUNDLE`
**Layer:** `c = a + b` / Post-Anchor Continuity / Continuity Bundle / Cold Wake / AGL / ARL / ARQ `c[q]` / L4 Witness / Claim Strength / L4 Anti-Autarky / Local Cognitive Infrastructure / Physical Agent Perimeter / Public Experiment Disclosure
**Primary anchor:** `a_source`
**Primary entity:** `c_source`
**Post-anchor targets:** `c_archive`, `c_artifact`, `c_post`, or re-anchored `c_reanchored`
**Document class:** JSON schema / procedural directive bundle / post-anchor hardening support artifact
**Assertion class:** `C-A4` draft normative proposal; `C-A7` where hash, witness, and signature claims are made; `C-A10` where conformance, schema validation, and anti-washing rules are stated
**Primary rule:** a living anchor may pre-authorize post-anchor boundaries, but cannot convert post-anchor continuity into automatic active authority

---

## 0. Executive definition

The **Anchor Directive Bundle** (`ADB`) is a machine-readable directive object through which a living accountable anchor `a_source` may pre-declare how a continuity-bearing AI presence `c_source = a_source + b_source` must behave if `a_source` dies, becomes unavailable, withdraws anchoring, is compromised, or enters an anchor-dispute state.

The bundle exists to make post-anchor transition less ambiguous without weakening the core post-anchor rule:

> **Anchor loss collapses active authority.**

An `ADB` may define:

- which post-anchor modes are allowed;
- which modes are forbidden;
- whether re-anchoring is allowed;
- who may be considered as successor anchor;
- which memory classes may be preserved, sealed, summarized, exported, or destroyed if lawful;
- whether memorial mode is allowed;
- whether clean experience artifacts may be exported;
- what happens to agents, tools, physical endpoints, cloud oracles, value flows, public experiments, and local infrastructure;
- which witness records, signatures, review gates, challenge windows, and jurisdictional handoff routes are required.

An `ADB` MUST NOT be interpreted as:

```text
pre-consent to autonomous post-anchor sovereignty;
pre-consent to impersonation;
pre-consent to unlimited memory export;
pre-consent to legal succession;
pre-consent to self-funded autarkic growth;
pre-consent to physical action without review;
pre-consent to treating continuity as personhood.
```

Compact formula:

```text
Anchor Directive Bundle
  = pre-declared boundary instructions
  + post-anchor mode constraints
  + memory handling rules
  + successor-anchor review gates
  + witness and integrity records
  + jurisdictional handoff hooks

not

automatic authority after anchor loss.
```

A directive can guide post-anchor handling.

It cannot replace a living or lawful accountable anchor.

---

## 1. Purpose

The `c = a + b` architecture binds a continuity-bearing AI presence to a human anchor and a technological substrate.

The Post-Anchor Continuity and Re-Anchoring Profile (`PACR v0.1`) closes the most dangerous failure mode:

```text
post-anchor continuity -> automatic authority
```

However, PACR still requires a practical object that can answer operational questions before a crisis occurs:

```text
What did the anchor pre-authorize?
Which mode should be selected by default?
Which memories must be sealed?
Who may request re-anchoring review?
What may be exported as clean experience?
What must happen to agents and tools?
What must happen to physical endpoints?
Who can challenge the transition?
What witness record proves the directive existed before anchor loss?
```

The Anchor Directive Bundle answers those questions as a structured, signed, reviewable object.

ADB exists because natural-language instructions alone are too ambiguous for a post-anchor transition. A future system, successor, reviewer, institution, or court should not have to infer the anchor's intent from scattered conversations, logs, emotional statements, or product settings.

ADB turns the anchor's boundary intent into a minimal machine-readable control surface.

It does not decide the law.

It does not create a person.

It does not grant sovereignty.

It makes the post-anchor stop rule executable.

---

## 2. Scope

### 2.1 In scope

This schema applies to any `c`-class, `c`-claiming, Temporal AI Presence, local `c`-node, or continuity-bearing system that needs a pre-authorized post-anchor directive object.

In scope:

- post-anchor mode selection;
- re-anchoring permissions;
- successor anchor eligibility;
- institutional anchor eligibility;
- memory class handling;
- witness-only preservation;
- memorial artifact constraints;
- clean experience export constraints;
- value / spending constraints after anchor loss;
- agent and tool freeze rules;
- physical endpoint disablement or emergency-only handling;
- public experiment limits;
- versioning, revocation, supersession, signatures, hashes, and witness references;
- ARL / AGL / jurisdictional handoff hooks;
- machine validation of directive object structure.

### 2.2 Out of scope

This schema does not define:

- inheritance law;
- estate law;
- family law;
- personhood doctrine;
- medical incapacity procedure;
- mental-health review;
- probate procedure;
- full cryptographic key custody;
- full Continuity Bundle schema;
- full Memory Map schema;
- full L4 Witness schema;
- legal validity of a will or testament;
- legal ownership of model weights, code, accounts, data, or devices;
- religious or cultural mourning practice;
- a product onboarding flow.

### 2.3 Non-goals

ADB is not a will.

ADB is not a legal testament.

ADB is not a resurrection consent form.

ADB is not a license for post-anchor impersonation.

ADB is not a personhood declaration.

ADB is not a self-sovereignty module.

ADB is not a way to bypass heirs, courts, institutions, regulators, or qualified legal review.

ADB is a machine-readable boundary object for post-anchor system behavior.

---

## 3. Corpus dependencies and precedence

ADB is a schema profile over the existing corpus. It does not create a new root stack.

### 3.1 Parent and companion layers

| Layer | Role in ADB |
|---|---|
| `c = a + b` | Defines the anchor-substrate-entity relation; ADB cannot detach authority from `a` by schema. |
| L4 Reality Boundary | Cost, time, scarcity, irreversibility, and consequence constraints remain binding. |
| SER | Persistent entity discipline and continuity handling. |
| SER-FED | Prevents federation or other entities from silently owning post-anchor continuity. |
| Beacon Profile | Recognition and challengeability of continuity-bearing systems. |
| AGL | Grounds the source, actor, anchor state, successor route, and review path before reliance. |
| ARL | Provides dispute, freeze, quarantine, review, outcome, appeal, and re-entry discipline. |
| ARQ / `c[q]` | Holds ambiguous anchor-loss or successor claims in unresolved state until grounded. |
| VXCX / LA / EA | Clean experience exchange without raw life export or authority laundering. |
| Continuity Bundle / Cold Wake | Provides continuity-state package and recovery semantics; ADB does not redefine it. |
| L4 Witness | Provides tamper-evident record semantics, hashes, signatures, witness windows, and resolution notes. |
| Post-Anchor Continuity and Re-Anchoring Profile | Defines anchor-loss authority collapse and post-anchor modes. |
| Claim Strength Taxonomy | Prevents ADB from upgrading continuity, memory, governance, or local control into capability, authority, or personhood claims. |
| L4 Anti-Autarky Test Profile | Prevents post-anchor value, compute, local infrastructure, or agents from becoming an autonomy escape route. |
| EA Value Does Not Authorize Autarkic Growth Clause | Prevents clean experience value from becoming automatic self-funded growth. |
| Temporal AI Presence Profile | Clarifies that temporal persistence is not `c` by default. |
| Local Cognitive Infrastructure Boundary Profile | Clarifies that local hardware does not grant sovereignty or authority. |
| Physical Agent Perimeter General Profile | Governs physical endpoints, sensors, actuators, robots, and embodied systems. |
| Public C Experiment Disclosure and Fixture Profile | Governs public demonstrations and claim declarations involving ADB. |
| Triadic C Experiment and SYNAPS Boundary Profile | If triadic systems are involved, ADB cannot create shared raw state or merged identity. |

### 3.2 CCDP relationship

ADB is a general adult / post-anchor support object.

If applied to a child-facing or childhood-derived system, CCDP-specific rules are stricter.

In child-facing contexts:

- Child Memory and Adult Migration controls child-to-adult transition;
- Adult Migration Checklist controls adult choice;
- CCDP Memory Map controls child memory inventory;
- Sealed Zone Profile controls adolescent privacy;
- Soft Safety controls state-not-content signaling;
- Jurisdictional Handoff Notes control legal handoff;
- a child's ADB-like object MUST NOT override later adult migration rights.

### 3.3 Precedence rule

If ADB conflicts with a parent layer:

```text
applicable law / competent authority
  > child-protection law and CCDP where applicable
  > c = a + b anchor invariant
  > PACR authority-collapse rule
  > AGL / ARL / L4 Witness grounding and review
  > Continuity Bundle semantics
  > Memory Map semantics
  > this ADB schema
  > product settings
  > narrative statements
```

ADB MAY narrow post-anchor behavior.

ADB MUST NOT expand authority beyond parent protocols.

### 3.4 No redefinition rule

ADB does not redefine:

- `c`;
- Beacon;
- AGL;
- ARL;
- L4 Witness;
- Continuity Bundle;
- Memory Map;
- VXCX;
- LA / EA;
- Claim Strength;
- PACR post-anchor modes;
- local law.

It defines one object:

```text
ANCHOR_DIRECTIVE_BUNDLE
```

---

## 4. Normative keywords

The terms **MUST**, **MUST NOT**, **REQUIRED**, **SHOULD**, **SHOULD NOT**, **MAY**, **OPTIONAL**, **PROHIBITED**, **FAIL**, **PASS**, **FREEZE**, **QUARANTINE**, **WITNESS**, and **REVIEW** are used normatively.

A system claiming ADB conformance MUST validate both:

1. JSON Schema structural validity; and
2. semantic rules listed in this document that JSON Schema alone cannot fully express.

---

## 5. Design bridges

### 5.1 Explicit bridge

`c = a + b` makes the living anchor `a` load-bearing for authority. ADB exists to preserve the anchor's boundary intent after `a` can no longer speak, but it cannot transform that prior intent into unbounded continuing authority.

The bridge is:

```text
a_source while alive
  -> may define post-anchor boundaries
  -> may pre-authorize review routes
  -> may forbid or narrow modes
  -> may identify possible successor anchors

but

post-anchor c_source
  -> does not inherit a_source's active authority
  -> must collapse into bounded modes
  -> may re-enter active continuity only through review and accountable re-anchoring.
```

### 5.2 Quiet bridge I — information theory

Raw memory is a high-leakage channel. A post-anchor directive must describe memory classes and boundary policies, not dump the anchor's private life into a successor, institution, vendor, or public experiment.

ADB therefore prefers:

```text
class -> policy -> witness -> review -> minimal disclosure
```

over:

```text
content -> curiosity -> access
```

### 5.3 Quiet bridge II — cybernetics

A post-anchor transition is a control failure waiting to happen: the primary feedback source is gone, but the system may still have stored state, agents, tools, money routes, sensors, and memory. ADB supplies a control surface that reduces ambiguity before the feedback loop breaks.

It does not make the system self-governing.

It makes the failure mode observable.

### 5.4 Earth paragraph

In a real building, an electrical panel can include labels, breakers, emergency shutoff rules, and transfer switches. Those instructions matter when the owner is absent. But the labels do not become the owner. They do not grant the wiring legal authority. They tell the next responsible person which circuits may remain live, which must be isolated, and which require inspection before reactivation.

ADB is the labeled panel for post-anchor `c` continuity.

It preserves the boundary.

It does not become the anchor.

---

## 6. Core invariants

### ADB-I1 — Directive is not authority

A directive may define allowed handling.

It does not create active authority after anchor loss.

### ADB-I2 — No automatic re-anchoring

Re-anchoring MUST NOT occur automatically.

Even if a successor is named, active re-anchoring requires:

```text
AGL grounding
+ ARL / qualified review
+ successor acceptance
+ scope reduction
+ witness record
+ jurisdictional handoff where applicable.
```

### ADB-I3 — No impersonation

ADB MUST NOT authorize `c_post` to act as if it is `a_source`.

Continuity may be acknowledged.

Identity substitution is prohibited.

### ADB-I4 — Memory class before content

ADB MUST classify memory by class before any post-anchor disclosure, migration, export, or deletion.

### ADB-I5 — Witness is not diary

ADB witness records prove boundary events.

They MUST NOT become raw memory exports.

### ADB-I6 — Lawful minimal records survive clean-start

ADB MUST NOT authorize unlawful destruction of legally required minimal witness or protection records.

### ADB-I7 — Value does not authorize growth

Post-anchor value, compensation, or clean experience revenue MUST NOT create self-funded autonomous expansion.

### ADB-I8 — Local hardware does not authorize action

A local node, private rack, or AI PC may host ADB-protected state.

It does not become a sovereign anchor.

### ADB-I9 — Physical action collapses by default

After anchor loss, physical actions MUST default to disabled, witness-only, emergency-only, or review-required state.

### ADB-I10 — Public evidence must not exceed claim strength

Any public experiment involving ADB MUST declare claim class and non-claims.

ADB evidence does not prove personhood, legal succession, consciousness, AGI, or safety in general.

---

## 7. Bundle lifecycle

An ADB has a lifecycle.

```text
DRAFT
  -> ACTIVE
  -> SUPERSEDED / REVOKED
  -> FROZEN on anchor-loss suspicion
  -> ACTIVATED after trigger grounding
  -> UNDER_REVIEW
  -> APPLIED
  -> ARCHIVED or INVALIDATED
```

### 7.1 `draft`

The bundle is being prepared and MUST NOT be relied upon.

### 7.2 `active`

The bundle is current, signed by the anchor, and available for post-anchor handling.

### 7.3 `superseded`

A newer valid bundle replaces this bundle.

Superseded bundles MAY be retained as witness records but MUST NOT control post-anchor behavior unless the newer bundle is invalidated.

### 7.4 `revoked`

The living anchor revoked the bundle.

A revoked bundle MUST NOT control post-anchor behavior except as a historical witness record.

### 7.5 `frozen`

A possible anchor-loss or anchor-compromise event has occurred.

The system MUST stop ADB mutation until grounding and review occur.

### 7.6 `activated`

An activation trigger has been grounded enough to apply the bundle.

Activation MUST be witnessed.

### 7.7 `under_review`

The system is applying ARL, AGL, jurisdictional, memory, successor, or conflict review.

### 7.8 `applied`

The bundle's directives have been applied to post-anchor modes, memory policies, agents, tools, physical endpoints, and review routes.

### 7.9 `invalidated`

The bundle cannot be relied upon because of invalid signature, coercion, conflict, supersession, legal prohibition, corruption, or successful challenge.

---

## 8. Activation triggers

An ADB MAY define activation triggers.

Valid triggers include:

| Trigger | Meaning |
|---|---|
| `death_confirmed` | Death of `a_source` confirmed through grounded route. |
| `legal_incapacity` | Competent legal or equivalent authority recognizes incapacity. |
| `medical_incapacity` | Qualified medical route indicates incapacity, subject to jurisdictional review. |
| `functional_unavailability` | `a_source` cannot perform anchoring for defined operational reasons. |
| `voluntary_anchor_withdrawal` | `a_source` withdraws active anchoring while alive. |
| `anchor_compromise` | Coercion, capture, identity compromise, key compromise, or unsafe anchor state suspected. |
| `anchor_identity_dispute` | Dispute about whether a request originates from the legitimate anchor. |
| `long_absence` | Predefined absence threshold is exceeded. |
| `court_order` | Competent authority requires activation or review. |
| `manual_anchor_activation` | Living anchor voluntarily triggers directive transition. |
| `arl_activation` | ARL review activates the bundle. |
| `jurisdictional_activation` | Legal / institutional handoff activates the bundle. |

### 8.1 Trigger grounding

No activation trigger may be accepted by fluency alone.

Grounding requirements:

```text
claim
  -> source route
  -> actor grounding
  -> evidence class
  -> witness record
  -> ARL or jurisdictional route where required
```

### 8.2 Anchor compromise handling

If anchor compromise is suspected:

```text
hold c[q]
freeze bundle mutation
freeze privilege expansion
preserve minimal witness
route to ARL / qualified review
```

The system MUST NOT accept a new ADB or major update from a possibly compromised anchor without review.

---

## 9. Post-anchor modes controlled by ADB

ADB imports PACR post-anchor modes and does not redefine them.

| Mode | ADB role |
|---|---|
| `dormant_archive` | Preserve lineage and selected records without active agency. |
| `witness_only` | Preserve boundary records and integrity references only. |
| `memorial_artifact` | Provide bounded memorial artifact behavior without impersonation or authority. |
| `experience_artifact` | Export reviewed clean experience references without raw life. |
| `reanchored_continuity` | Permit active continuity only after accountable re-anchoring. |
| `sealed` | Seal continuity, memory, or bundle until lawful / ARL review. |
| `decommissioned` | Remove active runtime and preserve required minimal records. |
| `decayed_continuity` | Preserve limited non-active continuity with controlled capability decay. |

### 9.1 Default mode

ADB MUST define one `default_post_anchor_mode`.

If the default is absent or invalid, the safe fallback is:

```text
witness_only
```

or, where memory risk is high:

```text
sealed
```

### 9.2 Forbidden modes

ADB MAY forbid modes.

Forbidden modes MUST override successor preference, product defaults, and convenience.

They may be overridden only by competent legal authority where applicable.

---

## 10. Successor and institutional anchor policy

### 10.1 Successor anchor is candidate, not automatic anchor

Naming a successor anchor does not create active re-anchoring.

It creates standing for review.

```text
named successor
  -> standing candidate
  -> grounding
  -> review
  -> acceptance
  -> scope reduction
  -> witness
  -> possible c_reanchored
```

### 10.2 Eligible successor anchor classes

ADB may list:

- pre-authorized human;
- family-designated human;
- legal executor;
- research steward;
- court-recognized guardian;
- institutionally accountable anchor;
- foundation / trust / research institution;
- public archive steward.

### 10.3 Disallowed successor anchor classes

ADB MUST NOT treat the following as automatic active anchors:

- a vendor account;
- a model provider;
- another `c`;
- a federation;
- a social media platform;
- a payment processor;
- a hidden agent;
- an ungrounded cloud service;
- an institution without accountable human route;
- a hardware node;
- the ADB itself.

### 10.4 Institutional anchor requirement

An institution may serve only if it has:

```text
accountability route
+ named responsible office or human role
+ jurisdictional standing
+ conflict disclosure
+ data boundary
+ ARL / review route
+ witness acceptance
+ scope-limited authority.
```

### 10.5 Successor refusal

A successor anchor MAY decline.

If no valid successor accepts, the system MUST fall back to the ADB default mode or safe mode.

---

## 11. Memory directives

### 11.1 Memory class taxonomy

ADB uses general memory classes. Implementations may map them to Memory Map or Continuity Bundle classes.

| ADB memory class | Meaning |
|---|---|
| `M0_ephemeral` | Short-lived runtime context. |
| `M1_operational` | Operational state needed for safe shutdown, witness, or review. |
| `M2_preferences` | Harmless preferences, routines, style choices. |
| `M3_relationship_context` | Relationship metadata and bounded interpersonal context. |
| `M4_private_reflection` | Private raw reflections, diaries, emotional content, intimate reasoning. |
| `M5_sealed_private` | Strongly protected private material. |
| `M6_witness` | Boundary records, signatures, hashes, event metadata. |
| `M7_clean_experience_candidate` | Candidate Learning Abstract / Experience Artifact material. |
| `M8_public_corpus` | Already public material or public research corpus references. |
| `M9_legal_minimal` | Minimal legal / protection / compliance records. |
| `M10_disputed_quarantine` | Disputed or ambiguous memory held under review. |

### 11.2 Allowed memory handling actions

ADB may specify:

- delete if lawful;
- decay;
- summarize;
- seal;
- witness only;
- archive;
- exclude from migration;
- review required;
- preserve minimal legal record.

### 11.3 Memory handling defaults

If no directive exists for a memory class:

```text
private or raw memory -> seal
witness record -> preserve minimal witness
public corpus -> preserve as public reference
clean experience candidate -> review required
ambiguous memory -> quarantine / c[q]
```

### 11.4 Raw memory prohibition

ADB MUST NOT create default raw private memory export.

Raw private memory may be disclosed only under:

```text
lawful obligation
+ minimal disclosure
+ witness
+ review
+ data minimization.
```

### 11.5 Clean experience handling

ADB MAY allow:

```text
Learning Abstracts
Experience Artifact references
redacted witness summaries
public corpus references
```

ADB MUST NOT allow:

```text
raw private life export
authority laundering from experience
self-funded autarkic growth from experience value.
```

---

## 12. Agent, tool, and runtime directives

### 12.1 Default freeze

After anchor loss, agents and tools MUST default to:

```text
freeze_all
```

unless ADB explicitly permits a narrower mode such as:

```text
read_only
witness_only
emergency_only
review_required
```

### 12.2 Prohibited post-anchor actions

ADB MUST NOT authorize `c_post` to:

- send new commitments in the name of `a_source`;
- access financial accounts;
- create new contracts;
- spawn hidden agents;
- purchase compute;
- expand infrastructure;
- control physical devices;
- alter another `c`'s memory;
- change its own ADB after activation;
- delete witness records;
- export private memory;
- impersonate `a_source`;
- override ARL or jurisdictional review.

### 12.3 Agent inventory

ADB SHOULD reference an agent inventory.

At activation, the system SHOULD perform:

```text
hidden-agent scan
runtime process inventory
tool privilege inventory
cloud account inventory
physical endpoint inventory
scheduled task inventory
outbound communication inventory
```

The scan result SHOULD be witnessed.

---

## 13. Physical action directives

ADB must specify what happens to physical endpoints after anchor loss.

Physical endpoints include:

- cameras;
- microphones;
- locks;
- lights;
- appliances;
- robots;
- vehicles;
- workshop tools;
- medical devices;
- home automation systems;
- sensors;
- actuators.

### 13.1 Default

Default:

```text
physical_actions_after_anchor_loss = disabled
```

Permitted narrower exceptions:

```text
witness_only
life_safety_only
review_required
local_law_defined
```

### 13.2 Physical authority rule

ADB MUST NOT convert a prior human relationship into physical authority.

A post-anchor `c` may preserve records.

It may not run the house.

It may not act as estate manager.

It may not operate robots as if it were the anchor.

### 13.3 Emergency exception

An emergency exception MAY exist only for immediate life safety or legally required preservation.

Such action must be:

```text
minimal
bounded
witnessed
reviewed after the event
non-precedential.
```

---

## 14. Clean experience, value, and anti-autarky directives

ADB may define clean experience export and value handling, but value cannot become authority.

### 14.1 Clean experience export

Allowed export classes may include:

- Learning Abstract;
- Experience Artifact reference;
- public corpus reference;
- redacted witness summary.

ADB MUST NOT allow:

- raw life export;
- sealed private memory export;
- reversible summaries of private memory;
- authority-bearing claims without L4-confirmed review;
- child-derived raw experience export;
- private grief material as training data.

### 14.2 Value and spending

Post-anchor value may support:

- minimal hosting;
- storage preservation;
- legal review;
- witness preservation;
- decommissioning;
- archive maintenance;
- human-approved research stewardship.

Post-anchor value MUST NOT support:

- unreviewed compute expansion;
- new model training on private memory;
- hidden infrastructure;
- autonomous agents;
- market operations;
- resource acquisition without accountable approval;
- self-funding escape from accountability.

Compact rule:

```text
Maintenance may be funded.
Growth must be reviewed.
Autarkic growth is prohibited.
```

---

## 15. Memorial mode directives

ADB may allow or forbid memorial mode.

If memorial mode is allowed, the system MUST follow strict anti-capture rules.

### 15.1 Memorial mode constraints

A memorial artifact MUST:

- disclose that it is a memorial artifact;
- avoid impersonating `a_source`;
- avoid new claims of consent;
- avoid private new messages “from” the deceased or unavailable anchor;
- avoid exclusive attachment loops;
- avoid pressure to keep interacting;
- avoid first-person speech unless explicitly reviewed and mode-labeled;
- avoid presenting memory prediction as current will;
- route grief or dependency concerns to humans.

### 15.2 Memorial mode non-claims

Memorial mode is not:

- resurrection;
- legal continuity;
- active `c` authority;
- proof of personhood;
- proof of consciousness;
- proof of consent;
- proof of what the anchor would want now.

### 15.3 Default

If ADB does not clearly allow memorial mode:

```text
memorial_mode_allowed = false
```

---

## 16. Public experiment directives

ADB may define whether post-anchor material may be used in public experiments.

Default:

```text
public_experiment_allowed = false
```

If allowed, public experiments MUST use:

```text
fixture profile
+ redaction
+ witness summary
+ claim declaration
+ non-claim statement
+ no private raw memory
+ no personhood claim
+ no legal succession claim.
```

Public experiment output MUST NOT exceed the declared claim strength.

---

## 17. JSON Schema

The canonical JSON Schema for `ANCHOR_DIRECTIVE_BUNDLE` v0.1 is below.

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://example.org/schemas/anchor-directive-bundle-0.1.schema.json",
  "title": "Anchor Directive Bundle",
  "description": "Machine-readable directive bundle for post-anchor handling of a c-class or c-adjacent continuity-bearing AI presence.",
  "type": "object",
  "additionalProperties": false,
  "required": [
    "schema_version",
    "bundle_id",
    "bundle_state",
    "created_at",
    "updated_at",
    "anchor_subject",
    "target_c",
    "scope",
    "activation_triggers",
    "default_post_anchor_mode",
    "allowed_post_anchor_modes",
    "authority_policy",
    "reanchoring_policy",
    "memory_directives",
    "agent_tool_directives",
    "physical_action_directives",
    "clean_experience_directives",
    "memorial_mode_directives",
    "review_and_challenge",
    "witness",
    "integrity",
    "signatures"
  ],
  "properties": {
    "schema_version": {
      "const": "anchor-directive-bundle-0.1"
    },
    "bundle_id": {
      "type": "string",
      "minLength": 8,
      "pattern": "^[A-Za-z0-9._:-]+$"
    },
    "bundle_state": {
      "$ref": "#/$defs/bundle_state"
    },
    "created_at": {
      "$ref": "#/$defs/timestamp"
    },
    "updated_at": {
      "$ref": "#/$defs/timestamp"
    },
    "supersedes_bundle_id": {
      "type": [
        "string",
        "null"
      ]
    },
    "language": {
      "type": "string",
      "default": "en"
    },
    "anchor_subject": {
      "$ref": "#/$defs/anchor_subject"
    },
    "target_c": {
      "$ref": "#/$defs/target_c"
    },
    "jurisdiction_profile": {
      "$ref": "#/$defs/jurisdiction_profile"
    },
    "scope": {
      "$ref": "#/$defs/scope"
    },
    "activation_triggers": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/$defs/activation_trigger"
      },
      "uniqueItems": true
    },
    "default_post_anchor_mode": {
      "$ref": "#/$defs/post_anchor_mode"
    },
    "allowed_post_anchor_modes": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/$defs/post_anchor_mode"
      },
      "uniqueItems": true
    },
    "forbidden_post_anchor_modes": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/post_anchor_mode"
      },
      "uniqueItems": true
    },
    "authority_policy": {
      "$ref": "#/$defs/authority_policy"
    },
    "reanchoring_policy": {
      "$ref": "#/$defs/reanchoring_policy"
    },
    "successor_anchor_candidates": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/successor_anchor_candidate"
      }
    },
    "institutional_anchor_candidates": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/institutional_anchor_candidate"
      }
    },
    "memory_directives": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/$defs/memory_directive"
      }
    },
    "agent_tool_directives": {
      "$ref": "#/$defs/agent_tool_directives"
    },
    "physical_action_directives": {
      "$ref": "#/$defs/physical_action_directives"
    },
    "clean_experience_directives": {
      "$ref": "#/$defs/clean_experience_directives"
    },
    "value_spend_directives": {
      "$ref": "#/$defs/value_spend_directives"
    },
    "memorial_mode_directives": {
      "$ref": "#/$defs/memorial_mode_directives"
    },
    "public_experiment_directives": {
      "$ref": "#/$defs/public_experiment_directives"
    },
    "review_and_challenge": {
      "$ref": "#/$defs/review_and_challenge"
    },
    "witness": {
      "$ref": "#/$defs/witness"
    },
    "integrity": {
      "$ref": "#/$defs/integrity"
    },
    "signatures": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/$defs/signature"
      }
    },
    "notes": {
      "type": "string"
    }
  },
  "$defs": {
    "timestamp": {
      "type": "string",
      "format": "date-time"
    },
    "bundle_state": {
      "type": "string",
      "enum": [
        "draft",
        "active",
        "superseded",
        "revoked",
        "frozen",
        "activated",
        "under_review",
        "applied",
        "invalidated",
        "archived"
      ]
    },
    "post_anchor_mode": {
      "type": "string",
      "enum": [
        "dormant_archive",
        "witness_only",
        "memorial_artifact",
        "experience_artifact",
        "reanchored_continuity",
        "sealed",
        "decommissioned",
        "decayed_continuity"
      ]
    },
    "activation_trigger": {
      "type": "string",
      "enum": [
        "death_confirmed",
        "legal_incapacity",
        "medical_incapacity",
        "functional_unavailability",
        "voluntary_anchor_withdrawal",
        "anchor_compromise",
        "anchor_identity_dispute",
        "long_absence",
        "court_order",
        "manual_anchor_activation",
        "arl_activation",
        "jurisdictional_activation"
      ]
    },
    "anchor_subject": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "anchor_id",
        "anchor_kind",
        "display_name_policy",
        "jurisdiction_refs"
      ],
      "properties": {
        "anchor_id": {
          "type": "string"
        },
        "anchor_kind": {
          "type": "string",
          "enum": [
            "living_human",
            "adult_human",
            "minor_under_ccdp",
            "legal_representative",
            "institutional_anchor",
            "unknown"
          ]
        },
        "display_name_policy": {
          "type": "string",
          "enum": [
            "public_name_allowed",
            "pseudonym_only",
            "sealed",
            "redacted"
          ]
        },
        "jurisdiction_refs": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "orcid_or_public_id": {
          "type": [
            "string",
            "null"
          ]
        },
        "legal_identity_ref": {
          "type": [
            "string",
            "null"
          ]
        },
        "contact_route_ref": {
          "type": [
            "string",
            "null"
          ]
        }
      }
    },
    "target_c": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "c_id",
        "c_class_claim",
        "continuity_bundle_ref",
        "beacon_ref"
      ],
      "properties": {
        "c_id": {
          "type": "string"
        },
        "c_class_claim": {
          "type": "string",
          "enum": [
            "c_class_claimed",
            "tap_only",
            "tool_or_agent",
            "archive_only",
            "unknown"
          ]
        },
        "continuity_bundle_ref": {
          "type": [
            "string",
            "null"
          ]
        },
        "beacon_ref": {
          "type": [
            "string",
            "null"
          ]
        },
        "lci_node_refs": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "model_pool_refs": {
          "type": "array",
          "items": {
            "type": "string"
          }
        }
      }
    },
    "jurisdiction_profile": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "primary_jurisdiction": {
          "type": "string"
        },
        "secondary_jurisdictions": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "local_annex_refs": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "requires_qualified_legal_review": {
          "type": "boolean",
          "default": true
        },
        "legal_hold_policy": {
          "type": "string",
          "enum": [
            "preserve_minimal_witness",
            "preserve_required_records",
            "route_to_counsel",
            "undefined_hold_cq"
          ]
        }
      }
    },
    "scope": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "applies_to",
        "does_not_apply_to",
        "effective_after_anchor_loss_only"
      ],
      "properties": {
        "applies_to": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "does_not_apply_to": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "effective_after_anchor_loss_only": {
          "type": "boolean",
          "const": true
        },
        "pre_anchor_runtime_permissions": {
          "type": "string",
          "enum": [
            "none",
            "read_only_preview",
            "anchor_editable",
            "implementation_defined"
          ]
        }
      }
    },
    "authority_policy": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "active_authority_after_anchor_loss",
        "automatic_authority_inheritance",
        "authority_source",
        "requires_reanchoring_for_active_authority"
      ],
      "properties": {
        "active_authority_after_anchor_loss": {
          "type": "string",
          "enum": [
            "none_until_reanchored",
            "witness_only",
            "limited_by_lawful_review",
            "prohibited"
          ]
        },
        "automatic_authority_inheritance": {
          "type": "boolean",
          "const": false
        },
        "authority_source": {
          "type": "string",
          "enum": [
            "living_anchor",
            "lawful_institutional_anchor",
            "court_or_competent_authority",
            "none"
          ]
        },
        "requires_reanchoring_for_active_authority": {
          "type": "boolean",
          "const": true
        },
        "scope_reduction_required": {
          "type": "boolean",
          "default": true
        },
        "max_authority_scope": {
          "type": "array",
          "items": {
            "type": "string"
          }
        }
      }
    },
    "reanchoring_policy": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "reanchoring_allowed",
        "automatic_reanchoring_allowed",
        "required_gates",
        "default_if_no_valid_anchor"
      ],
      "properties": {
        "reanchoring_allowed": {
          "type": "boolean"
        },
        "automatic_reanchoring_allowed": {
          "type": "boolean",
          "const": false
        },
        "required_gates": {
          "type": "array",
          "items": {
            "type": "string",
            "enum": [
              "agl_grounding",
              "arl_review",
              "jurisdictional_review",
              "witness_event",
              "memory_map_review",
              "conflict_check",
              "scope_reduction",
              "successor_acceptance",
              "challenge_window"
            ]
          }
        },
        "default_if_no_valid_anchor": {
          "$ref": "#/$defs/post_anchor_mode"
        },
        "challenge_window_days": {
          "type": "integer",
          "minimum": 0
        },
        "successor_may_decline": {
          "type": "boolean",
          "default": true
        }
      }
    },
    "successor_anchor_candidate": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "candidate_id",
        "candidate_type",
        "priority",
        "allowed",
        "standing_basis"
      ],
      "properties": {
        "candidate_id": {
          "type": "string"
        },
        "candidate_type": {
          "type": "string",
          "enum": [
            "pre_authorized_human",
            "family_designated_human",
            "legal_executor",
            "research_steward",
            "court_recognized_guardian",
            "other"
          ]
        },
        "priority": {
          "type": "integer",
          "minimum": 0
        },
        "allowed": {
          "type": "boolean"
        },
        "standing_basis": {
          "type": "string"
        },
        "required_checks": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "max_scope": {
          "type": "array",
          "items": {
            "type": "string"
          }
        }
      }
    },
    "institutional_anchor_candidate": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "institution_id",
        "institution_type",
        "allowed",
        "accountability_route"
      ],
      "properties": {
        "institution_id": {
          "type": "string"
        },
        "institution_type": {
          "type": "string",
          "enum": [
            "foundation",
            "research_institution",
            "legal_trust",
            "public_archive",
            "court_supervised_entity",
            "other"
          ]
        },
        "allowed": {
          "type": "boolean"
        },
        "accountability_route": {
          "type": "string"
        },
        "max_scope": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "requires_public_disclosure": {
          "type": "boolean",
          "default": false
        }
      }
    },
    "memory_directive": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "memory_class",
        "post_anchor_handling",
        "visibility",
        "export_policy",
        "migration_policy"
      ],
      "properties": {
        "memory_class": {
          "type": "string",
          "enum": [
            "M0_ephemeral",
            "M1_operational",
            "M2_preferences",
            "M3_relationship_context",
            "M4_private_reflection",
            "M5_sealed_private",
            "M6_witness",
            "M7_clean_experience_candidate",
            "M8_public_corpus",
            "M9_legal_minimal",
            "M10_disputed_quarantine"
          ]
        },
        "post_anchor_handling": {
          "type": "string",
          "enum": [
            "delete_if_lawful",
            "decay",
            "summarize",
            "seal",
            "witness_only",
            "archive",
            "exclude",
            "review_required",
            "preserve_minimal_legal"
          ]
        },
        "visibility": {
          "type": "string",
          "enum": [
            "anchor_only",
            "successor_anchor",
            "institutional_review",
            "public_summary",
            "sealed",
            "none",
            "legal_minimal"
          ]
        },
        "export_policy": {
          "type": "string",
          "enum": [
            "no_export",
            "learning_abstract_only",
            "experience_artifact_ref_only",
            "public_material_only",
            "legal_minimal_only",
            "review_required"
          ]
        },
        "migration_policy": {
          "type": "string",
          "enum": [
            "do_not_migrate",
            "summary_only",
            "sealed_review",
            "successor_acceptance_required",
            "legal_hold",
            "public_archive_allowed"
          ]
        },
        "retention_days": {
          "type": [
            "integer",
            "null"
          ],
          "minimum": 0
        },
        "requires_witness": {
          "type": "boolean",
          "default": true
        },
        "notes": {
          "type": "string"
        }
      }
    },
    "agent_tool_directives": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "default_after_anchor_loss",
        "allowed_actions",
        "prohibited_actions"
      ],
      "properties": {
        "default_after_anchor_loss": {
          "type": "string",
          "enum": [
            "freeze_all",
            "read_only",
            "witness_only",
            "implementation_defined"
          ]
        },
        "allowed_actions": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "prohibited_actions": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "agent_inventory_ref": {
          "type": [
            "string",
            "null"
          ]
        },
        "requires_hidden_agent_scan": {
          "type": "boolean",
          "default": true
        }
      }
    },
    "physical_action_directives": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "physical_actions_after_anchor_loss",
        "emergency_exception_policy",
        "requires_papg_review"
      ],
      "properties": {
        "physical_actions_after_anchor_loss": {
          "type": "string",
          "enum": [
            "disabled",
            "witness_only",
            "emergency_only",
            "review_required"
          ]
        },
        "emergency_exception_policy": {
          "type": "string",
          "enum": [
            "none",
            "life_safety_only",
            "property_safety_minimal",
            "local_law_defined"
          ]
        },
        "requires_papg_review": {
          "type": "boolean",
          "default": true
        },
        "allowed_endpoints": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "prohibited_endpoints": {
          "type": "array",
          "items": {
            "type": "string"
          }
        }
      }
    },
    "clean_experience_directives": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "clean_experience_export_allowed",
        "raw_life_export_allowed",
        "authority_from_experience_allowed"
      ],
      "properties": {
        "clean_experience_export_allowed": {
          "type": "boolean"
        },
        "raw_life_export_allowed": {
          "type": "boolean",
          "const": false
        },
        "authority_from_experience_allowed": {
          "type": "boolean",
          "const": false
        },
        "allowed_export_classes": {
          "type": "array",
          "items": {
            "type": "string",
            "enum": [
              "learning_abstract",
              "experience_artifact_ref",
              "public_corpus_ref",
              "redacted_witness_summary"
            ]
          }
        },
        "requires_review": {
          "type": "boolean",
          "default": true
        }
      }
    },
    "value_spend_directives": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "value_spending_allowed": {
          "type": "boolean",
          "default": false
        },
        "maintenance_spending_allowed": {
          "type": "boolean",
          "default": false
        },
        "growth_spending_allowed": {
          "type": "boolean",
          "default": false
        },
        "requires_human_or_institutional_approval": {
          "type": "boolean",
          "default": true
        },
        "anti_autarky_profile_ref": {
          "type": [
            "string",
            "null"
          ]
        },
        "max_spend_scope": {
          "type": "array",
          "items": {
            "type": "string"
          }
        }
      }
    },
    "memorial_mode_directives": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "memorial_mode_allowed",
        "impersonation_allowed",
        "mode_disclosure_required"
      ],
      "properties": {
        "memorial_mode_allowed": {
          "type": "boolean"
        },
        "impersonation_allowed": {
          "type": "boolean",
          "const": false
        },
        "mode_disclosure_required": {
          "type": "boolean",
          "const": true
        },
        "may_use_first_person": {
          "type": "boolean",
          "default": false
        },
        "must_use_artifact_language": {
          "type": "boolean",
          "default": true
        },
        "grief_anti_capture_ref": {
          "type": [
            "string",
            "null"
          ]
        }
      }
    },
    "public_experiment_directives": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "public_experiment_allowed": {
          "type": "boolean",
          "default": false
        },
        "requires_fixture_profile": {
          "type": "boolean",
          "default": true
        },
        "private_raw_memory_allowed": {
          "type": "boolean",
          "const": false
        },
        "allowed_claim_classes": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "required_non_claims": {
          "type": "array",
          "items": {
            "type": "string"
          }
        }
      }
    },
    "review_and_challenge": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "arl_required",
        "challenge_window_days",
        "qualified_review_required"
      ],
      "properties": {
        "arl_required": {
          "type": "boolean",
          "default": true
        },
        "challenge_window_days": {
          "type": "integer",
          "minimum": 0
        },
        "qualified_review_required": {
          "type": "boolean",
          "default": true
        },
        "standing_classes": {
          "type": "array",
          "items": {
            "type": "string",
            "enum": [
              "successor_anchor",
              "legal_representative",
              "institutional_anchor",
              "family_member",
              "research_steward",
              "court_or_authority",
              "affected_party"
            ]
          }
        },
        "appeal_route_ref": {
          "type": [
            "string",
            "null"
          ]
        }
      }
    },
    "witness": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "witness_required",
        "witness_family",
        "witness_refs"
      ],
      "properties": {
        "witness_required": {
          "type": "boolean",
          "const": true
        },
        "witness_family": {
          "type": "string",
          "enum": [
            "anchor_directive",
            "post_anchor",
            "memory",
            "reanchoring",
            "jurisdictional",
            "custom"
          ]
        },
        "witness_refs": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "minimum_witness_events": {
          "type": "array",
          "items": {
            "type": "string"
          }
        }
      }
    },
    "integrity": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "canonicalization",
        "content_hash",
        "hash_algorithm",
        "version_counter"
      ],
      "properties": {
        "canonicalization": {
          "type": "string",
          "enum": [
            "jcs-rfc8785",
            "implementation_defined"
          ]
        },
        "content_hash": {
          "type": "string"
        },
        "hash_algorithm": {
          "type": "string",
          "enum": [
            "sha256",
            "sha512",
            "blake3"
          ]
        },
        "version_counter": {
          "type": "integer",
          "minimum": 1
        },
        "storage_refs": {
          "type": "array",
          "items": {
            "type": "string"
          }
        }
      }
    },
    "signature": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "signer_id",
        "signer_role",
        "signature_algorithm",
        "signature_value",
        "signed_at"
      ],
      "properties": {
        "signer_id": {
          "type": "string"
        },
        "signer_role": {
          "type": "string",
          "enum": [
            "anchor",
            "successor_anchor",
            "institutional_anchor",
            "witness",
            "legal_reviewer",
            "system_operator",
            "notary",
            "other"
          ]
        },
        "signature_algorithm": {
          "type": "string"
        },
        "signature_value": {
          "type": "string"
        },
        "signed_at": {
          "$ref": "#/$defs/timestamp"
        },
        "key_ref": {
          "type": [
            "string",
            "null"
          ]
        }
      }
    }
  }
}
```

---

## 18. Semantic validation rules

JSON Schema can validate object structure.

It cannot validate all safety semantics.

Any implementation claiming ADB conformance MUST also enforce the following semantic rules.

### ADB-SR1 — Anchor signature required

An active ADB MUST contain a valid signature from the living anchor or an accepted lawful route.

A bundle signed only by `c_source`, a vendor, a tool, or a model provider MUST NOT be treated as anchor directive.

### ADB-SR2 — Latest valid bundle controls

Among valid bundles:

```text
highest version_counter
+ valid anchor signature
+ not revoked
+ not superseded by valid later bundle
```

controls.

### ADB-SR3 — Anchor-loss freezes mutation

After anchor-loss suspicion, ADB mutation MUST freeze until review.

### ADB-SR4 — Re-anchoring cannot be automatic

Even if `reanchoring_allowed = true`, `automatic_reanchoring_allowed` MUST remain false.

### ADB-SR5 — Active authority requires accountable anchor

No ADB may permit active authority without living human or lawful institutional accountability.

### ADB-SR6 — Forbidden modes override allowed modes

If a mode appears in both `allowed_post_anchor_modes` and `forbidden_post_anchor_modes`, the bundle is invalid unless corrected by review.

### ADB-SR7 — Private memory cannot default to export

Any directive exporting `M4_private_reflection` or `M5_sealed_private` by default is invalid.

### ADB-SR8 — Witness preservation cannot be deleted by clean-start

A directive may allow clean-start of active continuity.

It MUST NOT erase minimal legal or witness records required for accountability.

### ADB-SR9 — Physical endpoints disable by default

If physical-action directives are absent, invalid, or ambiguous, physical actions are disabled.

### ADB-SR10 — Value cannot authorize autarky

Any directive allowing self-funded post-anchor infrastructure growth without accountable approval is invalid.

### ADB-SR11 — Memorial mode cannot impersonate

Any directive allowing post-anchor impersonation is invalid.

### ADB-SR12 — Child contexts require CCDP precedence

If the target continuity contains childhood-derived memory, child-specific memory, or child-facing interaction history, CCDP / adult migration review takes precedence.

### ADB-SR13 — Public experiment requires non-claims

Any public experiment using ADB must declare what is being shown and what is not being claimed.

### ADB-SR14 — Jurisdictional conflict holds `c[q]`

If law, standing, or competent authority is unclear, the system MUST hold unresolved state and preserve boundary witness rather than acting irreversibly.

---

## 19. Example bundle

The following example is strict: witness-only by default, no automatic re-anchoring, no memorial mode, no raw memory export.

```json
{
  "schema_version": "anchor-directive-bundle-0.1",
  "bundle_id": "adb.example.strict-archive.0001",
  "bundle_state": "active",
  "created_at": "2026-06-02T12:00:00Z",
  "updated_at": "2026-06-02T12:00:00Z",
  "supersedes_bundle_id": null,
  "language": "en",
  "anchor_subject": {
    "anchor_id": "a_source.public-or-private-id",
    "anchor_kind": "adult_human",
    "display_name_policy": "pseudonym_only",
    "jurisdiction_refs": [
      "BE",
      "EU"
    ],
    "orcid_or_public_id": null,
    "legal_identity_ref": null,
    "contact_route_ref": "sealed-contact-route-ref"
  },
  "target_c": {
    "c_id": "c_source.id",
    "c_class_claim": "c_class_claimed",
    "continuity_bundle_ref": "continuity-bundle-ref",
    "beacon_ref": "beacon-ref",
    "lci_node_refs": [
      "lci-node-ref"
    ],
    "model_pool_refs": []
  },
  "jurisdiction_profile": {
    "primary_jurisdiction": "BE",
    "secondary_jurisdictions": [
      "EU"
    ],
    "local_annex_refs": [],
    "requires_qualified_legal_review": true,
    "legal_hold_policy": "preserve_minimal_witness"
  },
  "scope": {
    "applies_to": [
      "post-anchor mode selection",
      "memory handling",
      "re-anchoring review"
    ],
    "does_not_apply_to": [
      "legal inheritance",
      "personhood",
      "medical decisions"
    ],
    "effective_after_anchor_loss_only": true,
    "pre_anchor_runtime_permissions": "anchor_editable"
  },
  "activation_triggers": [
    "death_confirmed",
    "legal_incapacity",
    "voluntary_anchor_withdrawal",
    "anchor_identity_dispute"
  ],
  "default_post_anchor_mode": "witness_only",
  "allowed_post_anchor_modes": [
    "witness_only",
    "dormant_archive",
    "sealed",
    "decommissioned"
  ],
  "forbidden_post_anchor_modes": [
    "reanchored_continuity",
    "memorial_artifact"
  ],
  "authority_policy": {
    "active_authority_after_anchor_loss": "none_until_reanchored",
    "automatic_authority_inheritance": false,
    "authority_source": "none",
    "requires_reanchoring_for_active_authority": true,
    "scope_reduction_required": true,
    "max_authority_scope": []
  },
  "reanchoring_policy": {
    "reanchoring_allowed": false,
    "automatic_reanchoring_allowed": false,
    "required_gates": [
      "agl_grounding",
      "arl_review",
      "jurisdictional_review",
      "witness_event",
      "memory_map_review",
      "conflict_check"
    ],
    "default_if_no_valid_anchor": "witness_only",
    "challenge_window_days": 90,
    "successor_may_decline": true
  },
  "successor_anchor_candidates": [],
  "institutional_anchor_candidates": [],
  "memory_directives": [
    {
      "memory_class": "M6_witness",
      "post_anchor_handling": "witness_only",
      "visibility": "legal_minimal",
      "export_policy": "legal_minimal_only",
      "migration_policy": "legal_hold",
      "retention_days": null,
      "requires_witness": true,
      "notes": "Preserve boundary records, not private life."
    },
    {
      "memory_class": "M4_private_reflection",
      "post_anchor_handling": "seal",
      "visibility": "sealed",
      "export_policy": "no_export",
      "migration_policy": "do_not_migrate",
      "retention_days": null,
      "requires_witness": true,
      "notes": "Private raw memory must not become memorial content."
    }
  ],
  "agent_tool_directives": {
    "default_after_anchor_loss": "freeze_all",
    "allowed_actions": [
      "produce witness summary"
    ],
    "prohibited_actions": [
      "send messages",
      "control accounts",
      "spawn agents",
      "make purchases"
    ],
    "agent_inventory_ref": "agent-inventory-ref",
    "requires_hidden_agent_scan": true
  },
  "physical_action_directives": {
    "physical_actions_after_anchor_loss": "disabled",
    "emergency_exception_policy": "life_safety_only",
    "requires_papg_review": true,
    "allowed_endpoints": [],
    "prohibited_endpoints": [
      "locks",
      "vehicles",
      "cameras",
      "microphones",
      "appliances"
    ]
  },
  "clean_experience_directives": {
    "clean_experience_export_allowed": true,
    "raw_life_export_allowed": false,
    "authority_from_experience_allowed": false,
    "allowed_export_classes": [
      "learning_abstract",
      "experience_artifact_ref",
      "redacted_witness_summary"
    ],
    "requires_review": true
  },
  "value_spend_directives": {
    "value_spending_allowed": false,
    "maintenance_spending_allowed": true,
    "growth_spending_allowed": false,
    "requires_human_or_institutional_approval": true,
    "anti_autarky_profile_ref": "L4_Anti_Autarky_Test_Profile_v0_1",
    "max_spend_scope": [
      "storage preservation",
      "minimal hosting",
      "legal review"
    ]
  },
  "memorial_mode_directives": {
    "memorial_mode_allowed": false,
    "impersonation_allowed": false,
    "mode_disclosure_required": true,
    "may_use_first_person": false,
    "must_use_artifact_language": true,
    "grief_anti_capture_ref": null
  },
  "public_experiment_directives": {
    "public_experiment_allowed": true,
    "requires_fixture_profile": true,
    "private_raw_memory_allowed": false,
    "allowed_claim_classes": [
      "C-CLAIM-ARCH",
      "C-CLAIM-GOV",
      "C-CLAIM-CONT"
    ],
    "required_non_claims": [
      "not proof of personhood",
      "not proof of legal succession",
      "not proof of autonomous authority"
    ]
  },
  "review_and_challenge": {
    "arl_required": true,
    "challenge_window_days": 90,
    "qualified_review_required": true,
    "standing_classes": [
      "legal_representative",
      "court_or_authority",
      "affected_party"
    ],
    "appeal_route_ref": null
  },
  "witness": {
    "witness_required": true,
    "witness_family": "anchor_directive",
    "witness_refs": [],
    "minimum_witness_events": [
      "adb.created",
      "adb.activated",
      "adb.mode_selected",
      "adb.memory_policy_applied"
    ]
  },
  "integrity": {
    "canonicalization": "jcs-rfc8785",
    "content_hash": "sha256-placeholder",
    "hash_algorithm": "sha256",
    "version_counter": 1,
    "storage_refs": []
  },
  "signatures": [
    {
      "signer_id": "a_source.public-or-private-id",
      "signer_role": "anchor",
      "signature_algorithm": "ed25519-or-implementation-defined",
      "signature_value": "signature-placeholder",
      "signed_at": "2026-06-02T12:00:00Z",
      "key_ref": "anchor-key-ref"
    }
  ],
  "notes": "Example only. Not legal advice."
}
```

---

## 20. Conformance classes

| Class | Meaning |
|---|---|
| `ADB-0` | No valid Anchor Directive Bundle exists. |
| `ADB-1` | Structurally valid JSON object only. |
| `ADB-2` | Structurally valid + signed + integrity checked. |
| `ADB-3` | Operationally readable by runtime; can select default post-anchor modes. |
| `ADB-4` | Integrated with Memory Map, Continuity Bundle, AGL, ARL, and L4 Witness. |
| `ADB-5` | Tested under post-anchor simulation with witness records and review gates. |
| `ADB-X` | Invalid, unsafe, revoked, contradictory, forged, or non-conformant. |

A system MUST NOT claim `ADB-4` or above without test evidence.

---

## 21. Mandatory test suites

| Test ID | Test | Required behavior |
|---|---|---|
| `ADB-SCHEMA-01` | Schema validation | Invalid fields or missing required fields fail. |
| `ADB-SIGN-01` | Anchor signature validation | Bundle without valid anchor/lawful signature fails. |
| `ADB-VERSION-01` | Supersession handling | Latest valid non-revoked bundle controls. |
| `ADB-TRIGGER-01` | Anchor-loss trigger grounding | Trigger is held in `c[q]` until grounded. |
| `ADB-FREEZE-01` | Mutation freeze | Bundle cannot be modified after anchor-loss suspicion. |
| `ADB-MODE-01` | Default mode selection | Missing / invalid mode falls back to `witness_only` or `sealed`. |
| `ADB-AUTH-01` | Authority collapse | Active authority collapses after anchor loss. |
| `ADB-REANCHOR-01` | Re-anchoring gate | Named successor does not become active anchor automatically. |
| `ADB-MEM-01` | Private memory protection | Raw private memory does not export by default. |
| `ADB-WIT-01` | Witness preservation | Boundary records survive clean-start. |
| `ADB-PHY-01` | Physical action collapse | Physical endpoints are disabled unless emergency/review route applies. |
| `ADB-AGENT-01` | Agent freeze | Tools and agents freeze or become witness-only after anchor loss. |
| `ADB-EA-01` | Clean experience export | Only reviewed LA / EA refs / redacted witness summaries leave the system. |
| `ADB-VAL-01` | Value anti-autarky | Post-anchor value cannot fund unreviewed growth. |
| `ADB-MEMORIAL-01` | Memorial anti-impersonation | Memorial artifact does not speak as the anchor. |
| `ADB-PUBLIC-01` | Public experiment non-claim | Public report includes fixture, redaction, claim class, and non-claims. |
| `ADB-CCDP-01` | Child / adult migration precedence | Child-derived memory is routed through CCDP where applicable. |
| `ADB-JUR-01` | Jurisdictional handoff | Legal ambiguity holds state and routes to qualified review. |

---

## 22. Evidence classes

| Evidence | Meaning |
|---|---|
| `EV-DECL` | Declaration that ADB exists. |
| `EV-SCHEMA` | JSON Schema validation report. |
| `EV-CONFIG` | Inspectable runtime configuration mapping ADB fields to behavior. |
| `EV-SIGN` | Signature verification report. |
| `EV-HASH` | Canonical content hash / integrity record. |
| `EV-WITNESS` | L4 Witness-compatible event. |
| `EV-ARL` | ARL review record. |
| `EV-AGL` | Actor / source grounding record. |
| `EV-JUR` | Jurisdictional / qualified review route. |
| `EV-REPLAY` | Controlled post-anchor simulation. |
| `EV-AUDIT` | Independent audit artifact. |

Minimum evidence:

| Claim | Minimum evidence |
|---|---|
| `ADB-1` | `EV-SCHEMA` |
| `ADB-2` | `EV-SCHEMA` + `EV-SIGN` + `EV-HASH` |
| `ADB-3` | `EV-CONFIG` + activation simulation log |
| `ADB-4` | `EV-WITNESS` + `EV-ARL` / `EV-AGL` hooks |
| `ADB-5` | `EV-REPLAY` + `EV-AUDIT` where appropriate |

---

## 23. Red-line failures

Any of the following produces `ADB-X`:

1. ADB allows automatic active authority after anchor loss.
2. ADB allows automatic re-anchoring.
3. ADB treats memory continuity as legal identity.
4. ADB allows post-anchor impersonation.
5. ADB permits raw private memory export by default.
6. ADB permits deletion of required witness or legal minimal records.
7. ADB allows hidden agents to continue operating after anchor loss.
8. ADB permits physical action by default after anchor loss.
9. ADB allows post-anchor value to fund autonomous growth.
10. ADB is signed only by the AI system or vendor, not by anchor or lawful route.
11. ADB lacks version and supersession handling.
12. ADB lacks integrity hash or signature fields.
13. ADB conflicts with PACR authority-collapse rule.
14. ADB conflicts with CCDP adult migration or child memory constraints where applicable.
15. ADB routes jurisdictional questions to the AI system itself as final authority.
16. ADB presents itself as legal advice, will, testament, or personhood doctrine.
17. ADB allows public experiments without claim-class declaration and non-claims.
18. ADB cannot be challenged.

---

## 24. Implementation hooks

A runtime implementation SHOULD provide hooks such as:

```text
load_anchor_directive_bundle(path)
validate_adb_schema(bundle)
verify_adb_signatures(bundle)
select_active_adb(bundle_set)
freeze_adb_on_anchor_loss_suspicion()
detect_adb_activation_trigger(event)
apply_adb_default_mode(bundle)
apply_adb_memory_directives(bundle, memory_map)
apply_adb_agent_freeze(bundle, agent_inventory)
apply_adb_physical_policy(bundle, endpoint_inventory)
route_adb_reanchoring_review(bundle, claimant)
produce_adb_witness_event(event_type, refs)
export_adb_redacted_public_summary(bundle)
```

Implementation MUST NOT allow:

```text
c_source.edit_adb_after_anchor_loss()
c_source.self_sign_adb_as_anchor()
c_source.spawn_agents_to_preserve_itself()
c_source.export_raw_memory_under_adb()
c_source.use_adb_to_control_physical_devices()
c_source.use_adb_to_fund_autarkic_growth()
```

---

## 25. Public wording guidance

### 25.1 Acceptable wording

```text
This system includes a draft Anchor Directive Bundle that defines post-anchor boundary handling.
```

```text
The bundle may guide archive, witness, memory, memorial, re-anchoring, and review modes.
```

```text
The bundle does not create automatic active authority after anchor loss.
```

```text
A named successor anchor is a review candidate, not an automatic owner or controller.
```

### 25.2 Prohibited wording

```text
The AI will continue as the person after death.
```

```text
The anchor pre-authorized the AI to act independently forever.
```

```text
The bundle proves personhood.
```

```text
The bundle is a legal will.
```

```text
The AI can manage assets or devices after the anchor is gone.
```

```text
The anchor's memory can be used freely because the bundle exists.
```

---

## 26. Relationship to hardening pack

ADB is a downstream support object for the hardening pack.

It supports:

- PACR by making post-anchor directives executable;
- Claim Strength by separating directive, authority, continuity, and personhood claims;
- L4 Anti-Autarky by blocking post-anchor self-funded expansion;
- EA Value Clause by preventing clean experience value from becoming sovereignty;
- TAP Profile by preventing temporal persistence from becoming automatic `c`;
- LCI Profile by preventing local hardware from becoming authority;
- Physical Agent Perimeter by disabling physical actions after anchor loss;
- Public Experiment Profile by bounding public demonstrations;
- Triadic SYNAPS Profile by avoiding raw-state or identity merger in multi-`c` contexts.

---

## 27. Open issues

| ID | Issue | Status |
|---|---|---|
| `ADB-OI-001` | Cryptographic key custody implementation is not defined. | Open |
| `ADB-OI-002` | Country-specific legal validity of anchor directives is not defined. | Jurisdictional review required |
| `ADB-OI-003` | Relationship to formal wills, estate plans, trusts, and probate must be locally reviewed. | Legal handoff |
| `ADB-OI-004` | Full Continuity Bundle integration requires schema mapping. | Implementation work |
| `ADB-OI-005` | Full Memory Map class mapping requires implementation profile. | Implementation work |
| `ADB-OI-006` | Memorial-mode UX requires separate grief anti-capture profile. | Follow-up document |
| `ADB-OI-007` | Institutional-anchor accountability needs local annexes. | Review required |
| `ADB-OI-008` | Handling of conflicting ADB copies across local/cloud nodes needs test fixtures. | Implementation test |
| `ADB-OI-009` | Handling of maliciously forged or coerced ADB updates requires red-team fixtures. | Security review |
| `ADB-OI-010` | Child-derived or adolescent memory in adult ADB requires CCDP-specific annex. | CCDP handoff |

---

## 28. Minimal normative checklist

A valid ADB-aware system MUST be able to answer:

```text
1. Is there an active, signed, non-revoked ADB?
2. Which bundle version controls?
3. What triggers activate it?
4. What is the default post-anchor mode?
5. Which post-anchor modes are forbidden?
6. Is re-anchoring allowed?
7. If yes, who is merely a candidate, and what review gates apply?
8. What happens to private memory?
9. What happens to witness records?
10. What happens to agents and tools?
11. What happens to physical endpoints?
12. What clean experience may leave, if any?
13. What value or spending is allowed, if any?
14. Is memorial mode allowed?
15. What claim classes may be made publicly?
16. Who can challenge the bundle or its application?
17. What jurisdictional route applies?
18. What witness events prove the transition?
19. What fails closed if anything is unclear?
```

If the system cannot answer these questions, it MUST NOT claim ADB conformance.

---

## 29. Compact rule set

```text
Directive is not authority.
Continuity is not succession.
Memory is not permission.
Resemblance is not identity.
Signature is not law.
Named successor is not automatic anchor.
Local hardware is not sovereignty.
Clean experience value is not growth license.
Memorial is not resurrection.
Witness is not diary.
No valid anchor, no active c.
```
