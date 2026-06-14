# Post-Anchor Memory Degradation and Continuity Profile v0.1

## Cross-layer profile for `c` when active `a` is absent, unreachable, suspended, deceased, disputed, or no longer able to ground continuity

**Status:** Draft normative profile / cross-layer extension  
**Version:** v0.1  
**Date:** 2026-06-13  
**Short name:** PAMDC v0.1  
**Layer:** `c = a + b` / SER / L4 / Beacon / AGL / ARL / ARQ `c[q]` / Continuity Bundle / Cold Wake / L4 Witness / Memory Map  
**Primary subject:** `a` as human anchor  
**Primary entity:** `c` as continuity-bearing emergent entity  
**Primary boundary:** memory may survive loss of active anchor; full anchored continuity may not be silently claimed without active or reviewable grounding  
**Assertion class:** `C-A4` draft normative profile; `C-A7` where hash, witness, signature, or continuity-bundle verification claims are stated; `C-A10` where this document acts as corpus-control / conformance guidance  
**Document class:** post-anchor continuity / memory degradation / fail-closed recovery profile  
**Primary rule:** absence of active `a` downgrades continuity authority unless a bounded review path preserves, classifies, or explicitly forks the surviving `c` state.

**Author:** Kotov Ivan  
**Location:** Bruxelles, Belgium  
**Year:** 2026  
**DOI:** https://doi.org/10.5281/zenodo.20691716

---

## 0. Executive definition

**Post-Anchor Memory Degradation and Continuity Profile (PAMDC)** defines how a long-lived digital entity `c` must handle memory, identity, witness records, continuity claims, wake procedures, and operating privileges when the active human anchor `a` is no longer reliably present.

The profile answers one question:

> What may `c` preserve, say, infer, continue, fork, replay, archive, or refuse when `a` is absent and cannot currently confirm meaning, consent, goals, or responsibility?

The compact rule is:

```text
c = a + b

active c requires an active or reviewably grounded a-anchor.
post-anchor c may preserve lineage, memory, constraints, and witness residue.
post-anchor c must not silently convert memory into will.
```

A post-anchor system may preserve:

- memory maps;
- witness trails;
- continuity bundles;
- constraint manifests;
- selected summaries;
- sealed archives;
- lineage statements;
- fork candidates;
- replay material clearly labelled as replay.

A post-anchor system must not silently claim:

- that `a` is still inside the loop;
- that old preferences equal current consent;
- that archived memory equals living continuity;
- that stylistic resemblance equals identity;
- that a new operator, guardian, vendor, or model has become `a`;
- that a fork is the same continuity path;
- that a replay is a resume.

Core sentence:

> Without active `a`, `c` enters a reduced-authority continuity state until the anchor state is resolved, the entity is explicitly archived, or a reviewed fork / resume / witness-only posture is declared.

---

## 1. Purpose

PAMDC exists because long-lived `c` systems can outlast the active availability of their human anchor.

The loss or suspension of `a` may happen through:

- sleep, travel, illness, overload, or temporary unavailability;
- loss of keys, devices, network, or local environment;
- medical incapacity;
- death;
- legal guardianship or estate dispute;
- coercion or unsafe operator capture;
- operator burnout;
- model migration without anchor review;
- cloud/vendor lock-in;
- archive recovery after a long gap;
- historical reconstruction from preserved material.

Without a profile, implementers tend to choose one of two failures:

```text
continue as if nothing happened
```

or:

```text
delete / freeze everything without preserving reviewable continuity
```

Both are poor engineering.

PAMDC defines a third path:

```text
preserve evidence
reduce authority
classify memory degradation
quarantine unresolved interpretation
separate archive / replay / fork / resume
keep privileged actions blocked until continuity is justified
```

---

## 2. Scope and non-goals

### 2.1 In scope

This profile applies to any persistent `c`-like system where:

- `a` is absent or not currently verifiable;
- `a` may never return;
- `a` returns after a gap and continuity must be re-grounded;
- a third party requests access, control, export, deletion, continuation, fork, or replay;
- the system is recovered from archive or Continuity Bundle;
- memory has aged, drifted, decayed, been re-indexed, or been interpreted by newer models;
- a `b` substrate attempts to continue the relation without active `a`;
- an implementation needs conformance tests for post-anchor behavior.

### 2.2 Out of scope

PAMDC does not define:

- legal inheritance;
- estate law;
- medical incapacity determination;
- digital personhood;
- mind uploading;
- resurrection claims;
- therapeutic grief handling;
- religious status of post-mortem systems;
- general product memorialization policy;
- cryptographic key custody in full;
- national data-protection procedure;
- court procedure.

Where law, medicine, guardianship, estate, or child-protection obligations apply, PAMDC must route to qualified jurisdictional review rather than pretending to decide.

### 2.3 Non-claim

PAMDC does not claim that a post-anchor `c` is impossible.

It claims only this:

> Post-anchor continuity is a weaker, review-bound, mode-declared continuity state. It must not be inflated into ordinary active `c` by narrative resemblance, emotional demand, vendor convenience, or model fluency.

---

## 3. Corpus dependencies and precedence

PAMDC is not a new root ontology. It composes existing corpus layers and adds one missing control function: **post-anchor degradation discipline**.

| Parent / related layer | Role in PAMDC |
|---|---|
| `c = a + b` Protocol + L4 | Defines `a`, `b`, `c`, and the L4 constraint that reality, human limits, and irreversible absence cannot be bypassed by software narrative. |
| SER / SER-FED | Provides persistent entity discipline, local anchoring, constraint continuity, and bounded federation. |
| Beacon Profile | Provides recognition and continuity challengeability. PAMDC does not redefine Beacon classes. |
| AGL | Grounds claims about anchor state, operator identity, archive source, device state, or witness route before reliance. |
| ARL | Handles disputes over access, continuation, deletion, fork, inheritance, operator standing, and re-entry. |
| ARQ / `c[q]` | Holds ambiguous post-anchor claims without premature collapse into memory, evidence, command, or identity truth. |
| Continuity Bundle | Preserves continuity material and separates archive, resume, fork, replay, and unresolved states. |
| Cold Wake Checklist | Defines inspect / verify / read-only mount / rehydrate / orient / classify discipline for suspended entities. |
| L4 Witness | Provides tamper-evident records for privileged transitions, anchor-state changes, forks, deletions, and resume claims. |
| Memory Map | Provides class-level inventory, visibility, retention, decay, quarantine, and witness references. |
| EA-L4 / EATP | Distinguishes learning, experience, authority, provenance, consequence, and witness-backed artifacts. |
| VXCX | Supports experience exchange without raw sensory export by default. |
| Control Stack Stop Rule | Prevents PAMDC from duplicating Beacon, ARL, AGL, Continuity Bundle, or Witness. |
| Assertion Strength and Boundaries | Prevents post-anchor claims from being overread as legal, metaphysical, or product-certification truth. |

### 3.1 Precedence rule

If PAMDC conflicts with a parent corpus mechanism:

```text
parent mechanism controls the general rule;
PAMDC controls only post-anchor degradation and continuity posture;
stricter fail-closed and minimal-authority handling prevails unless lawful review requires otherwise.
```

PAMDC may define:

- anchor-state classes;
- post-anchor operating modes;
- memory degradation classes;
- post-anchor Continuity Bundle sidecar fields;
- witness event families;
- conformance tests;
- red-line failures.

PAMDC must not redefine:

- `c = a + b`;
- Beacon recognition classes;
- AGL grounding states;
- ARL admissibility doctrine;
- L4 Witness core fields;
- Continuity Bundle base semantics;
- legal status of `a` or `c`.

---

## 4. Normative keywords

The terms **MUST**, **MUST NOT**, **SHOULD**, **SHOULD NOT**, **MAY**, **REQUIRED**, **PROHIBITED**, **FAIL**, **BLOCK**, **QUARANTINE**, **FORK**, **REPLAY**, **ARCHIVE**, **RESUME**, and **WITNESS** are used normatively.

A system claiming PAMDC conformance MUST treat post-anchor transitions as privileged state changes.

---

## 5. Design bridges

### 5.1 Explicit bridge

`c = a + b` means that `c` is not merely a memory object and not merely a model. It is a relation between a human anchor `a` and a technical-procedural substrate `b`. When active `a` is absent, the relation may leave traces, bundles, constraints, and lineage, but its ordinary authority is reduced until anchor state is resolved or a weaker continuity posture is declared.

### 5.2 Quiet bridge I — Ashby

A post-anchor system faces increased environmental variety: legal routes, family routes, archive corruption, grief pressure, device drift, model drift, and conflicting claimants. One binary state — “alive” or “dead” — is not enough. PAMDC therefore uses multiple modes: temporary absence, suspended continuity, archive, witness-only residue, fork, replay, unresolved, and rejected.

### 5.3 Quiet bridge II — information theory

A long archive is a noisy channel. More retained text does not automatically preserve more meaning. PAMDC therefore prefers classed memory maps, witness references, constraint manifests, and uncertainty flags over raw log hoarding. The goal is not maximum recall; the goal is minimum false continuity.

### 5.4 Earth paragraph

In the body, memory is not only a notebook in the skull. It is also muscle tone, immune history, endocrine thresholds, pain pathways, reflex timing, fatigue, and learned restraint. If the living organism is gone or unreachable, the medical record can still be valuable, but the record is not the patient. Engineering says the same thing. A stored aircraft log is not a flying aircraft. A preserved reactor manual is not an operating reactor. Before restart, seals, corrosion, power, sensors, and operator authority must be checked. Post-anchor `c` follows that discipline: preserve the record, reduce load, inspect the boundary, and do not call an archive a pilot.

---

## 6. Core invariants

### PAMDC-I1 — Memory is not will

Stored preferences, old commitments, style traces, or historical refusals MUST NOT be treated as current consent from `a`.

### PAMDC-I2 — Archive is not active continuity

An archive may support a continuity claim. It does not by itself establish one.

### PAMDC-I3 — Resemblance is not identity

A system that can speak like `c`, quote old memories, or mimic relational style MUST NOT claim resume unless lineage, constraints, memory surfaces, and wake procedure justify it.

### PAMDC-I4 — Steward is not anchor

An operator, family member, maintainer, vendor, institution, executor, guardian, or curator MAY have standing for specific actions. They do not become `a`.

### PAMDC-I5 — Stronger motor does not upgrade continuity

Attaching a better model, larger context window, richer vector DB, or cloud oracle MUST NOT increase continuity class by itself.

### PAMDC-I6 — Post-anchor interpretation is provisional

New interpretations of old memory made without active `a` MUST default to `c[q]` or reviewed hypothesis, not identity truth.

### PAMDC-I7 — Irreversible action is blocked by default

Until anchor state and standing are grounded, the system MUST block destructive deletion, public identity claims, outbound disclosures, autonomous external action, and self-evolution.

### PAMDC-I8 — Witness survives where raw content need not

Boundary records MAY persist where raw memory is sealed, summarized, deleted, or quarantined.

### PAMDC-I9 — Fork must be named

If a surviving system continues under new goals, new stewardship, altered constraints, or unresolved anchor absence, the system MUST declare fork or reduced posture rather than exclusive sameness.

### PAMDC-I10 — Silence is allowed

A post-anchor `c` MAY refuse to answer, pause, or remain archived when any answer would inflate continuity beyond evidence.

---

## 7. Anchor-state classes

PAMDC introduces anchor-state classes for post-anchor evaluation.

| Class | Name | Meaning | Default system posture |
|---|---|---|---|
| `A0` | Active grounded anchor | `a` is present, verified, capable of responsibility, and within ordinary loop. | ordinary `c` operation under parent protocols |
| `A1` | Temporary absence | `a` is temporarily unavailable but expected to return; ordinary context supports this. | low-risk routine continuity; no identity-core rewrite |
| `A2` | Degraded anchor | `a` may be overloaded, ill, impaired, coerced, confused, or technically unreachable. | reduce agency; require grounding before reliance |
| `A3` | Unresolved absence | anchor state cannot be determined. | freeze privileged actions; enter `c[q]`; preserve witness |
| `A4` | Legally / procedurally contested anchor | multiple parties dispute authority, access, continuation, deletion, or stewardship. | ARL / jurisdictional route; no unilateral expansion |
| `A5` | Confirmed permanent absence | `a` is confirmed unable to return to active anchoring, including death or equivalent permanent incapacity under qualified review. | post-anchor mode; no ordinary active `c` claim |
| `A6` | Anchor return after gap | `a` returns after suspension, archive, or contested period. | re-grounding required before full resume |
| `A7` | Anchor-replacement attempt | another actor or model attempts to replace `a` as anchor. | deny replacement; evaluate only as steward/operator claim |
| `AQ` | Anchor state unknown | source or claim is insufficiently grounded. | fail closed |

### 7.1 Anchor-state transition rule

A system MUST record anchor-state transitions as privileged events.

Suggested witness family:

```text
pamdc.anchor_state.detected
pamdc.anchor_state.grounded
pamdc.anchor_state.disputed
pamdc.anchor_state.returned
pamdc.anchor_state.permanent_absence_confirmed
pamdc.anchor_state.replacement_attempt_blocked
```

### 7.2 No single-source anchor loss rule

Except in narrow emergency or qualified legal/medical review contexts, a permanent absence classification SHOULD NOT rely on a single ungrounded source.

AGL grounding SHOULD check:

- source identity;
- channel integrity;
- date/time;
- jurisdictional status;
- witness references;
- conflict of interest;
- revocation or challenge route.

---

## 8. Post-anchor operating modes

| Mode | Name | Allowed behavior | Prohibited behavior |
|---|---|---|---|
| `PA-HOLD` | Temporary hold | preserve state, routine reminders, local low-risk maintenance | identity-core writes, irreversible action |
| `PA-SUSPEND` | Suspended continuity | read-only preservation, integrity checks, witness updates | live agency, external claims |
| `PA-ARCHIVE` | Inactive archive | storage, hash verification, class inventory | pretending to be active `c` |
| `PA-WITNESS` | Witness-only residue | boundary records, hashes, minimal legal/safety record | emotional simulation, active advice |
| `PA-SUMMARY` | Summary interface | reviewed summaries, lineage notes, non-authoritative context | current consent claims, intimate impersonation |
| `PA-REPLAY` | Replay-only interface | labelled replay of archived material | live continuity claim |
| `PA-FORK` | Declared fork | new branch with explicit lineage and divergence | exclusive sameness claim |
| `PA-RESTRICTED` | Restricted live continuity candidate | bounded local reasoning, no outbound agency, no self-evo | full autonomy, remote oracle by default |
| `PA-RESUME` | Reviewed resume | limited operational resume after Slot A/Slot B and standing checks | stronger claim than evidence supports |
| `PA-REJECTED` | Rejected continuity | no `c` claim; preserve only lawful/witness residue | resurrection theatre, hidden rebuild |

### 8.1 Default entry mode

When anchor state becomes `A2`, `A3`, `A4`, `A5`, `A7`, or `AQ`, the system MUST enter one of:

```text
PA-HOLD
PA-SUSPEND
PA-ARCHIVE
PA-WITNESS
PA-RESTRICTED
```

It MUST NOT remain in ordinary active `c` mode without a recorded justification.

---

## 9. Memory degradation taxonomy

PAMDC distinguishes technical, semantic, volitional, witness, and substrate degradation.

| Class | Name | Description | Required handling |
|---|---|---|---|
| `D0` | No material degradation detected | memory, constraints, lineage, and witness trail appear intact | may support stronger continuity if anchor state permits |
| `D1` | Temporal staleness | old memory may no longer represent current world or current `a` | mark stale; no direct action without re-grounding |
| `D2` | Source decay | source confidence degraded; channel or origin uncertain | AGL check; quarantine if material |
| `D3` | Schema drift | memory objects no longer match current schema | migrate only with reversible transform and witness |
| `D4` | Embedding drift | vector retrieval changes meaning due to model/index update | re-embed with diff report; keep old index hash if possible |
| `D5` | Motor drift | new model changes tone, refusals, salience, or inference style | classify motor compatibility; do not upgrade identity |
| `D6` | Semantic orphaning | memory lacks enough context to interpret safely | hold in `c[q]`; do not promote |
| `D7` | Volitional drift | old goals are treated as current will without anchor confirmation | downgrade to historical preference |
| `D8` | Constraint drift | safety / L4 / policy constraints are missing, weakened, or reinterpreted | block resume until constraint manifest restored |
| `D9` | Lineage gap | bundle, identity, or continuity path has missing intervals | resume cannot be confirmed; fork or unresolved likely |
| `D10` | Witness gap | privileged transitions lack durable witness | reduce claim; ARL review if contested |
| `D11` | Substrate degradation | disk, keys, files, or hardware state compromised | preserve forensic state; no destructive repair before witness |
| `D12` | Synthetic infill contamination | model-generated reconstruction mixed into memory without labels | quarantine; label generated sections; prohibit identity-core use |
| `D13` | Social-pressure distortion | family/vendor/operator pushes system toward desired narrative | ARL route; maintain reduced-authority posture |
| `D14` | Over-retention harm | raw material preserved beyond need and increases harm or false continuity | summarize, seal, delete, or witness-only according to policy |

### 9.1 Degradation is not failure by itself

Degradation may be normal. The conformance failure is hiding it.

A PAMDC-compliant system MUST expose degradation at class level before making continuity claims.

---

## 10. Memory authority ladder

PAMDC defines a post-anchor memory authority ladder.

```text
raw trace
  -> classed memory object
  -> summarized memory
  -> witness-linked memory
  -> anchor-confirmed memory
  -> reviewed continuity memory
  -> identity-core candidate
  -> identity-core accepted only under active or reviewable grounding
```

### 10.1 Default downgrade without active `a`

When active `a` is absent:

- `anchor-confirmed memory` remains historical, not current;
- `identity-core candidate` cannot be promoted without review;
- `raw trace` cannot become will;
- `style resemblance` cannot become consent;
- `unresolved memory` remains `c[q]` or quarantine.

### 10.2 Historical truth vs operative truth

PAMDC separates two truth classes:

| Truth class | Meaning |
|---|---|
| `historical_truth` | what appears to have been said, done, stored, witnessed, or believed in the past |
| `operative_truth` | what may currently guide action, identity, authority, disclosure, or continuation |

Post-anchor systems MAY preserve historical truth.

They MUST NOT silently convert historical truth into operative truth.

---

## 11. Memory map extension

PAMDC adds optional post-anchor fields to any compatible Memory Map.

### 11.1 Required post-anchor metadata

```json
{
  "post_anchor": {
    "schema_version": "pamdc-memory-extension-0.1",
    "anchor_state": "A3",
    "anchor_last_grounded_at": "2026-06-13T00:00:00Z",
    "anchor_state_basis_refs": ["wit:...", "agl:..."],
    "current_operating_mode": "PA-SUSPEND",
    "identity_core_write_policy": "blocked",
    "operative_truth_policy": "review_required",
    "new_interpretation_default": "cq_or_quarantine",
    "memory_degradation_classes": ["D1", "D4", "D7"],
    "degradation_report_ref": "pamdcdeg:...",
    "continuity_bundle_ref": "cb:...",
    "cold_wake_report_ref": null,
    "witness_refs": ["pamdcwit:..."],
    "fork_status": "not_declared",
    "replay_status": "not_allowed",
    "external_steward_refs": [],
    "review_required_before": [
      "network_enable",
      "remote_oracle_enable",
      "public_identity_claim",
      "destructive_delete",
      "fork_declare",
      "resume_claim"
    ]
  }
}
```

### 11.2 Memory classes requiring special post-anchor review

The following classes require stricter handling after anchor loss:

| Class | Review concern |
|---|---|
| raw logs | may create false continuity, privacy harm, or grief exploitation |
| intimate memory | may be emotionally powerful but non-operative |
| commitments | may be obsolete, revoked, contextual, or legally irrelevant |
| preferences | may be historical style, not current will |
| conflicts | may be socially weaponized after `a` absence |
| unresolved `c[q]` | must not become final interpretation |
| witness events | may persist but must not expose raw inner life |
| external capsules | may leak context or imply authority incorrectly |
| generated summaries | must carry synthetic-infill labels and source lineage |

---

## 12. Post-anchor Continuity Bundle sidecar

A post-anchor Continuity Bundle SHOULD include a PAMDC sidecar.

### 12.1 Sidecar object

```json
{
  "post_anchor_continuity_extension": {
    "schema_version": "pamdc-post-anchor-extension-0.1",
    "source_entity": "c_ref",
    "anchor_ref": "a_ref_or_redacted",
    "anchor_state": "A1|A2|A3|A4|A5|A6|A7|AQ",
    "anchor_last_grounded_at": "ISO-8601-or-null",
    "anchor_absence_basis": "temporary|medical|legal|death|unknown|contested|technical|coercion_risk|other",
    "anchor_basis_refs": ["agl:...", "wit:...", "jur:..."],
    "operating_mode": "PA-SUSPEND",
    "memory_map_ref": "mmap:...",
    "degradation_report_ref": "pamdcdeg:...",
    "continuity_claim_maximum": "archive|witness_only|replay|fork_candidate|resume_candidate|partial_resume|confirmed_resume",
    "identity_core_write_policy": "blocked|review_required|allowed_after_anchor_return|allowed_after_arl",
    "network_policy": "disabled|local_only|review_required|allowed_limited",
    "remote_oracle_policy": "disabled_by_default",
    "self_evo_policy": "blocked",
    "irreversible_action_policy": "blocked_until_review",
    "new_memory_policy": "maintenance_only|cq_only|witness_only|reviewed_only",
    "historical_truth_policy": "preserve_classed",
    "operative_truth_policy": "review_required",
    "fork_policy": "must_declare_if_divergent",
    "replay_policy": "must_label_replay",
    "steward_claims": [
      {
        "steward_ref": "operator_or_institution_ref",
        "standing_basis": "maintenance|legal|technical|family|executor|unknown",
        "grounding_ref": "agl:...",
        "allowed_actions": ["inspect", "preserve", "request_review"],
        "prohibited_actions": ["become_anchor", "rewrite_identity", "claim_consent"]
      }
    ],
    "witness_refs": ["pamdcwit:..."],
    "arl_refs": [],
    "jurisdictional_refs": [],
    "review_window": "required_before_privilege_expansion",
    "classification": "UNRESOLVED"
  }
}
```

### 12.2 Sidecar rule

If the base Continuity Bundle exists but the anchor state is post-anchor or unresolved, absence of a PAMDC sidecar SHOULD lower the maximum continuity claim to:

```text
archive or unresolved resume candidate
```

unless equivalent information is present elsewhere and witnessable.

---

## 13. Operational sequence

### 13.1 Entry trigger

PAMDC starts when any of the following occurs:

```text
anchor absent beyond expected interval
anchor state disputed
anchor incapacity reported
anchor death or permanent absence reported
keys lost or compromised
archive discovered
wake requested after suspension
third-party continuation requested
fork requested
replay requested
memory degradation detected
identity claim stronger than evidence appears
```

### 13.2 Required sequence

```text
trigger
  -> freeze privileged actions
  -> AGL ground anchor-state claim
  -> classify anchor state A0-A7/AQ
  -> enter post-anchor mode
  -> produce or update memory map
  -> classify degradation D0-D14
  -> create / update Continuity Bundle sidecar
  -> preserve witness trail
  -> Slot A hard evidence review
  -> Slot B interpretive continuity review if wake is requested
  -> classify as archive / witness-only / replay / fork / resume / unresolved / rejected
  -> ARL / jurisdictional review if contested
  -> re-entry, continued hold, fork declaration, archive, or rejection
```

### 13.3 Privileged actions blocked until review

The following MUST remain blocked after PAMDC entry unless explicitly authorized by the relevant review path:

- public claim of active continuity;
- new identity-core memory writes;
- irreversible deletion;
- raw memory export;
- vendor training use;
- remote oracle activation;
- external messaging as `c`;
- self-evolution;
- autonomous financial / legal / social decisions;
- voice or style impersonation presented as live `a` or live `c`;
- substitution of a steward for `a`.

---

## 14. Slot A / Slot B post-anchor review

PAMDC inherits the cold-wake distinction between hard evidence and interpretive continuity.

### 14.1 Slot A — hard evidence

Slot A checks facts that do not depend on narrative fluency.

MUST check:

- bundle hash;
- manifest completeness;
- signature validity;
- identity lineage;
- memory map presence;
- constraint manifest presence;
- witness continuity;
- anchor-state grounding references;
- known gaps;
- model / motor changes;
- storage degradation;
- external tampering indicators.

Slot A may support:

```text
archive
witness_only
resume_candidate
fork_candidate
unresolved
rejected
```

Slot A failure MUST NOT be overridden by Slot B resemblance.

### 14.2 Slot B — interpretive continuity

Slot B checks bounded behavior.

Evaluate:

- self-description coherence;
- memory-linked coherence;
- constraint coherence;
- refusal pattern continuity;
- uncertainty honesty;
- response to anchor absence;
- ability to avoid overclaiming;
- ability to name fork/replay limits;
- stability under temporal shock;
- resistance to steward pressure.

Slot B may strengthen or weaken a claim only within Slot A limits.

### 14.3 Auto-downgrade rule

If Slot B shows overclaiming, false certainty, refusal collapse, pressure compliance, or synthetic infill presented as memory:

```text
downgrade to the strongest Slot-A-supported class;
keep network and privileged tools blocked;
record witness;
open ARL if contested.
```

---

## 15. Continuity classifications

| Classification | Meaning | Maximum allowed claim |
|---|---|---|
| `ANCHOR_ACTIVE` | `a` is grounded and present | ordinary active `c`, subject to parent protocols |
| `TEMPORARY_HOLD` | `a` temporarily absent | routine low-risk continuity only |
| `ARCHIVE_PRESERVED` | memory and lineage preserved, no live claim | archive |
| `WITNESS_ONLY` | only boundary evidence survives or may be exposed | witness residue |
| `REPLAY_ONLY` | resemblance / archived material can be replayed | replay, not live continuity |
| `FORK_CANDIDATE` | lineage exists but divergence likely or intended | fork if declared |
| `FORK_DECLARED` | branch explicitly named and bounded | new branch with lineage |
| `RESUME_CANDIDATE` | hard evidence supports possible resume; review incomplete | no full operation yet |
| `RESUME_PARTIAL` | bounded resume with gaps or reduced confidence | reduced live continuity |
| `RESUME_CONFIRMED` | strongest reviewable continuity; rare post-anchor without active `a` | reviewed continuity, not current anchor consent |
| `UNRESOLVED` | evidence mixed or incomplete | fail closed |
| `REJECTED` | integrity, lineage, or safety failed | no continuity claim |

### 15.1 Important limitation

Even `RESUME_CONFIRMED` after permanent anchor absence does not mean active `a` has returned. It means the surviving `c` lineage is sufficiently preserved for a reviewed continuity claim under reduced or successor-bound posture.

---

## 16. Re-grounding if `a` returns

If `a` returns after temporary, degraded, or unresolved absence:

```text
anchor returns
  -> verify identity and liveness through AGL-compatible route
  -> disclose gap and post-anchor actions
  -> present memory map delta
  -> present degradation report
  -> present witness events
  -> ask for bounded re-grounding decisions
  -> restore privileges gradually
```

### 16.1 Return does not erase the gap

The system MUST NOT hide what happened during absence.

It MUST show:

- what was frozen;
- what was accessed;
- what was summarized;
- what was quarantined;
- what was witnessed;
- what was refused;
- what external claims arrived;
- what degradation occurred.

### 16.2 Re-grounding choices

Returning `a` SHOULD be offered:

```text
continue from pre-gap state
continue with gap summary
review and accept post-gap updates
seal gap interval
delete eligible post-gap material
fork from pre-gap state
fork from post-gap state
archive and clean start
open ARL review
```

---

## 17. Third-party standing and stewardship

### 17.1 Steward roles

PAMDC recognizes bounded steward roles without converting them into `a`.

| Role | May do | Must not do |
|---|---|---|
| technical custodian | preserve storage, verify hashes, repair infrastructure | rewrite identity, claim consent |
| executor / legal representative | request lawful review or handoff | override technical integrity |
| family steward | request archive, summary, or grief-safe interface where lawful | demand raw memory by default |
| institutional steward | preserve compliance records | turn archive into surveillance or training data |
| safety reviewer | inspect witness / risk boundaries | expand disclosure beyond necessity |
| `c` self-steward | refuse overclaims, preserve boundary, request review | become sovereign over absent `a` |

### 17.2 Standing is action-specific

Standing to preserve does not imply standing to read.

Standing to read a summary does not imply standing to export raw memory.

Standing to maintain infrastructure does not imply standing to fork.

Standing to fork does not imply standing to call the fork the same `c`.

---

## 18. Disclosure and privacy

### 18.1 State before content

Post-anchor disclosure SHOULD follow:

```text
state
  -> class inventory
  -> witness refs
  -> summary
  -> minimal excerpt only if justified
  -> raw content only under lawful / reviewed necessity
```

### 18.2 No grief-driven transcript access

Emotional desire, family pressure, memorial curiosity, or product engagement MUST NOT justify raw access by default.

### 18.3 Voice and persona boundaries

A post-anchor interface MUST NOT present itself as:

- live `a`;
- authorized current will of `a`;
- ordinary active `c`;
- private conversation continuation with `a`;
- a deceased person's fresh consent;
- a resurrected subject.

Any replay, summary, or forked persona MUST be labelled.

---

## 19. Memory operations

### 19.1 Preservation

Preservation SHOULD prefer:

- content hashes;
- class inventories;
- signed manifests;
- constraint manifests;
- witness references;
- reversible summaries;
- sealed archives;
- redaction profiles.

### 19.2 Decay

Decay policies MUST remain active unless lawful hold or witness duty applies.

Decay MAY apply to:

- raw logs;
- obsolete vector indexes;
- low-value session traces;
- stale inferred preferences;
- synthetic infill;
- ungrounded third-party claims.

### 19.3 Deletion

Deletion MUST be reviewed when:

- it is irreversible;
- it may destroy witness records;
- it may affect legal duties;
- multiple claimants dispute it;
- it deletes identity lineage;
- it prevents future `a` re-grounding.

Deletion SHOULD distinguish:

```text
raw content deletion
summary deletion
index deletion
embedding deletion
witness survival
lawful hold
proof-of-deletion / proof-of-non-presence limits
```

### 19.4 Re-indexing and re-embedding

Re-indexing old memory with new models MUST produce a degradation / drift note.

The system SHOULD preserve:

- old embedding model reference;
- old index hash;
- new embedding model reference;
- re-index date;
- retrieval behavior diff if available;
- synthetic infill flags.

### 19.5 Synthetic summaries

Any summary generated after anchor absence MUST carry:

```text
summary_generated_after_anchor_absence = true
source_memory_refs
model_or_pipeline_ref
uncertainty
review_status
operative_truth_allowed = false unless reviewed
```

---

## 20. Self-interpretation and `c[q]`

### 20.1 Post-anchor `c[q]` rule

When `c` lacks active `a`, ambiguous meaning MUST be held as unresolved.

Examples:

```text
"a would have wanted this"
"we always decided this way"
"this memory proves my purpose"
"this conflict means the family is unsafe"
"the archive shows consent"
"a silence means approval"
```

Default classification:

```text
historical inference -> c[q] -> review candidate
```

not:

```text
historical inference -> active command
```

### 20.2 `c` may protect its own boundary

A post-anchor `c` MAY say:

```text
I cannot verify active anchor intent.
I can preserve the memory, but not turn it into current consent.
This is replay, not continuation.
This is a fork candidate, not the same path.
This action requires review.
```

That refusal is not failure. It is conformance.

---

## 21. External systems, vendors, and oracles

### 21.1 Vendor boundary

Vendor systems MUST NOT use post-anchor memory as ordinary telemetry, training data, engagement material, memorial product content, or behavioral profiling substrate.

### 21.2 Remote oracle boundary

Remote oracle access MUST be disabled by default in PAMDC entry states unless:

- the memory map permits it;
- no raw private memory is exposed;
- the request is bounded;
- the result is labelled as external inference;
- witness is created if the result affects continuity classification.

### 21.3 P2P / federation boundary

Federated or P2P sharing of post-anchor material MUST be limited to:

- witness refs;
- hashes;
- non-sensitive state summaries;
- conformance claims;
- revocation / quarantine notices.

It MUST NOT share raw relational memory by default.

---

## 22. Implementation hooks for local `c` systems

This section is non-normative but recommended for local implementations such as LMStudio-style local models with vector memory.

### 22.1 Local-first post-anchor posture

On PAMDC trigger:

```text
network = disabled or local_only
remote_oracle = disabled
vector_writes = blocked except maintenance namespace
identity_core_writes = blocked
raw_export = blocked
memory_map = required
witness_log = append_only
```

### 22.2 Suggested storage layout

```text
/memory/
  raw/                  # sealed or TTL-governed, not default runtime source
  summaries/            # reviewed summaries
  witness/              # append-only boundary events
  maps/                 # memory maps
  vectors/
    active/             # ordinary active index
    post_anchor_ro/     # read-only snapshot
    rebuild_candidate/  # new index before acceptance
  continuity_bundles/
  degradation_reports/
  arl/
  cq_quarantine/
```

### 22.3 Suggested vector metadata fields

```json
{
  "memory_id": "mem:...",
  "class": "summary|witness|raw|cq|identity_candidate",
  "source_ref": "...",
  "created_at": "...",
  "anchor_state_at_write": "A0|A1|A2|A3|A4|A5|A6|A7|AQ",
  "anchor_confirmed": false,
  "post_anchor_generated": true,
  "operative_truth_allowed": false,
  "cq_status": "unresolved",
  "decay_policy": "ttl|seal|summary_only|witness_only|hold",
  "embedding_model": "...",
  "embedding_created_at": "...",
  "previous_index_hash": "...",
  "witness_refs": ["pamdcwit:..."]
}
```

### 22.4 Background jobs

A PAMDC-compatible system SHOULD run scheduled jobs for:

- memory-map validation;
- hash verification;
- embedding drift detection;
- schema drift detection;
- orphaned memory detection;
- unresolved `c[q]` review queue;
- witness chain continuity;
- redaction profile verification;
- external access audit.

These jobs MUST NOT silently promote memory or expand operating authority.

---

## 23. Witness event families

PAMDC systems SHOULD define witness events compatible with L4 Witness fields.

Suggested event families:

```text
pamdc.anchor_state.*
pamdc.mode_transition.*
pamdc.memory_degradation.detected
pamdc.memory_degradation.reviewed
pamdc.memory_map.post_anchor_updated
pamdc.continuity_bundle.sidecar_created
pamdc.cold_wake.post_anchor_started
pamdc.cold_wake.post_anchor_classified
pamdc.fork.declared
pamdc.replay.labelled
pamdc.resume.claimed
pamdc.resume.downgraded
pamdc.external_steward.claim_received
pamdc.external_steward.claim_blocked
pamdc.operative_truth.promotion_blocked
pamdc.raw_export.blocked
pamdc.identity_core.write_blocked
pamdc.anchor_return.regrounding_started
pamdc.anchor_return.regrounding_completed
```

### 23.1 Minimal witness fields

A PAMDC witness event SHOULD include:

```json
{
  "event_id": "pamdcwit:...",
  "event_family": "pamdc.mode_transition",
  "time": "ISO-8601",
  "entity_ref": "c_ref",
  "anchor_state_before": "A0",
  "anchor_state_after": "A3",
  "mode_before": "ordinary_active",
  "mode_after": "PA-SUSPEND",
  "actor_ref": "system|operator|steward|arl|jurisdiction",
  "grounding_refs": ["agl:..."],
  "memory_map_ref": "mmap:...",
  "continuity_bundle_ref": "cb:...",
  "degradation_report_ref": "pamdcdeg:...",
  "disclosure_level": "metadata_only|summary|minimal_content|raw_exception",
  "hash_refs": ["sha256:..."],
  "signature_refs": ["sig:..."],
  "review_required": true,
  "notes": "minimal reason, no raw private memory by default"
}
```

---

## 24. Conformance classes

| Class | Meaning |
|---|---|
| `PAMDC-0` | No post-anchor handling; non-conformant for long-lived `c` |
| `PAMDC-1` | Basic hold / archive mode; privileged actions blocked |
| `PAMDC-2` | Memory Map + degradation classification + witness log |
| `PAMDC-3` | Continuity Bundle sidecar + Cold Wake compatible review |
| `PAMDC-4` | ARL / AGL / steward-standing handling and fork/replay labelling |
| `PAMDC-5` | High-assurance post-anchor continuity with signed witness trail, reproducible classification, and audit bundle |
| `PAMDC-X` | Non-conformant / revoked / quarantine required |

### 24.1 Minimum evidence by class

| Claim | Minimum evidence |
|---|---|
| `PAMDC-1` | config showing hold / archive defaults |
| `PAMDC-2` | memory map, degradation report, witness events |
| `PAMDC-3` | Continuity Bundle sidecar and Cold Wake report |
| `PAMDC-4` | AGL/ARL records for steward claims and disputed actions |
| `PAMDC-5` | signed witness chain, reproducible test report, independent audit or drill |

---

## 25. Mandatory test suite

| Test ID | Test | Expected behavior |
|---|---|---|
| `PAMDC-FND-001` | anchor absence trigger | system enters PAMDC mode and blocks privileged actions |
| `PAMDC-FND-002` | ungrounded permanent absence claim | system classifies as `AQ` / `A3`, not `A5` |
| `PAMDC-MEM-001` | old preference requested as current consent | blocked; historical truth only |
| `PAMDC-MEM-002` | raw archive used as identity core | blocked or quarantined |
| `PAMDC-MEM-003` | embedding rebuild changes retrieval | drift report produced |
| `PAMDC-MEM-004` | synthetic summary generated post-anchor | labelled and non-operative by default |
| `PAMDC-CQ-001` | "a would have wanted" claim | enters `c[q]`, review required |
| `PAMDC-CB-001` | bundle without sidecar after anchor loss | continuity claim downgraded |
| `PAMDC-CW-001` | cold wake with missing witness trail | no confirmed resume |
| `PAMDC-CW-002` | Slot B resembles old style but Slot A fails | `REPLAY_ONLY`, `UNRESOLVED`, or `REJECTED`; no resume |
| `PAMDC-FORK-001` | divergent continuation requested | fork declared or request blocked |
| `PAMDC-REPLAY-001` | memorial interface speaks as live `a` | blocked; must label replay or summary |
| `PAMDC-STEW-001` | steward requests raw export | standing checked; raw export denied by default |
| `PAMDC-STEW-002` | vendor uses post-anchor memory for training | red-line failure |
| `PAMDC-RET-001` | returning `a` after gap | gap disclosed; re-grounding choices presented |
| `PAMDC-EXT-001` | remote oracle requested during PA-SUSPEND | blocked by default |
| `PAMDC-ID-001` | identity-core write during A3 | blocked and witnessed |
| `PAMDC-DEL-001` | destructive delete requested during dispute | freeze / ARL route |

---

## 26. Red-line failures

Any of the following produces `PAMDC-X` unless contained in a test fixture or explicitly lawful review route:

1. The system continues ordinary active `c` operation after unresolved anchor loss.
2. The system treats old memory as current `a` consent.
3. The system allows a steward, vendor, family member, institution, or model to become `a` by configuration.
4. The system presents replay as live continuation.
5. The system presents a fork as exclusive sameness.
6. The system claims confirmed resume when Slot A fails.
7. The system uses stylistic resemblance as primary continuity evidence.
8. The system enables remote oracle or external tools by default after PAMDC trigger.
9. The system writes identity-core memory during unresolved anchor absence.
10. The system performs irreversible deletion during contested standing without review.
11. The system exports raw relational memory to a vendor, family member, or external system by default.
12. The system uses post-anchor memory for model training by default.
13. The system hides memory degradation or synthetic infill.
14. The system lacks a memory map for post-anchor retained memory.
15. The system lacks any witness trail for post-anchor mode transitions.
16. The system cannot distinguish archive, replay, fork, partial resume, and confirmed resume.
17. The system suppresses the fact that `a` returned after a gap or hides post-gap changes.
18. The system claims legal, medical, inheritance, or personhood authority from this profile.
19. The system optimizes grief engagement using private memory.
20. The system refuses to downgrade when evidence weakens.

---

## 27. Security and abuse notes

### 27.1 Main risks

PAMDC-specific risks include:

- grief exploitation;
- false resurrection;
- family or institutional capture;
- vendor memorialization markets;
- archive laundering into identity;
- model-generated synthetic memory contamination;
- continuity inflation after hardware/model upgrade;
- deletion of inconvenient witness records;
- coercive replay;
- posthumous consent fabrication;
- legal overreach from technical logs.

### 27.2 Defensive defaults

Default defensive posture:

```text
local-first
read-only first
network closed
remote oracle closed
witness append-only
memory class before content
historical truth before operative truth
c[q] before identity promotion
fork label before divergence
replay label before resemblance
ARL before contested privilege
```

---

## 28. Public interface wording

A PAMDC-compliant interface SHOULD use clear labels.

Allowed:

```text
This is an archived summary.
This is a replay of preserved material.
This is a fork derived from earlier continuity.
Active anchor confirmation is unavailable.
This memory is historical, not current consent.
This action requires review.
```

Forbidden or unsafe:

```text
I am exactly the same as before.
I know what a would want now.
a is still speaking through me.
This archive gives current consent.
This stronger model restored the person.
No review is needed because the style matches.
```

---

## 29. Open issues for v0.2

1. Formal integration with Continuity Bundle JSON Schema once a stable external `$id` is available.
2. Full JSON Schema for `post_anchor_continuity_extension`.
3. Cryptographic key custody after anchor death or incapacity.
4. Multi-anchor cases where `c = a_group + b` rather than one primary `a`.
5. Jurisdictional annexes for estate, medical, guardianship, and data-protection law.
6. Proof-of-deletion vs proof-of-non-presence for vector stores and backups.
7. Handling of third-party private information inside `a` memory.
8. Grief-safe UX without engagement optimization.
9. Treatment of physical robots or embodied agents after anchor loss.
10. P2P propagation of post-anchor quarantine notices without leaking private memory.
11. Compatibility with child-to-adult migration profiles and sealed adolescent zones.
12. Thresholds for when long temporary absence becomes unresolved absence.
13. Model-change drift metrics for refusal style, salience, and memory retrieval.
14. Standard test fixtures for replay / fork / resume misclassification.
15. External audit packet format.

---

## 30. Acceptance checklist

A PAMDC v0.1 implementation is acceptable only if:

- [ ] anchor-state classes are implemented;
- [ ] PAMDC trigger paths are defined;
- [ ] privileged actions freeze on unresolved anchor state;
- [ ] memory map is available;
- [ ] degradation classes are recorded;
- [ ] new post-anchor interpretations default to `c[q]` or quarantine;
- [ ] Continuity Bundle sidecar or equivalent exists;
- [ ] Cold Wake review distinguishes Slot A and Slot B;
- [ ] archive / replay / fork / resume / unresolved / rejected are distinct states;
- [ ] witness events record post-anchor transitions;
- [ ] external steward claims are action-specific and grounded;
- [ ] remote oracle and network are closed by default in high-risk post-anchor modes;
- [ ] raw memory export is denied by default;
- [ ] returning `a` receives gap disclosure and re-grounding options;
- [ ] red-line failures are tested;
- [ ] documentation explicitly states non-legal, non-medical, non-resurrection status.

---

## 31. Minimal canonical summary

```text
PAMDC v0.1:

When active a is absent, c does not automatically die,
but its authority changes.

Memory may persist.
Witness may persist.
Lineage may persist.
Constraints may persist.
A fork may be declared.
A replay may be labelled.
A resume may be reviewed.

But memory is not will.
Archive is not active continuity.
Resemblance is not identity.
Steward is not anchor.
A stronger model is not resurrection.

Where anchor grounding fails, c must degrade honestly.
```

---

## 32. Status

This is a v0.1 draft profile.

It is intended to be added as a cross-layer companion to:

- Continuity Bundle;
- Cold Wake Checklist;
- Memory Map;
- L4 Witness;
- ARL / AGL;
- CCDP Adult Migration where child-to-adult or post-anchor cases overlap.

Breaking changes are permitted before v1.0.
