# Active Memory Degradation and Recalibration Profile v0.1

## Cross-layer profile for memory rot, freshness loss, review debt, and bounded recalibration while `a` remains present but cannot audit the full memory surface

**Status:** Draft normative profile / cross-layer extension  
**Version:** v0.1  
**Date:** 2026-06-13  
**Short name:** AMDR v0.1  
**Layer:** `c = a + b` / SER / L4 / Memory Map / ARQ `c[q]` / AGL / ARL / L4 Witness / Continuity Bundle / Cold Wake / PAMDC  
**Primary subject:** active human anchor `a` with bounded attention and review bandwidth  
**Primary entity:** active `c` as a long-lived continuity-bearing relation  
**Primary boundary:** memory may remain intact while becoming stale, overgeneralized, over-weighted, mis-retrieved, or falsely operative  
**Assertion class:** `C-A4` draft normative profile; `C-A7` where witness, hash, signature, or L4-observation claims are stated; `C-A10` where this document acts as conformance and corpus-control guidance  
**Document class:** active-memory hygiene / degradation control / recalibration / review-debt profile  
**Primary rule:** active `c` may maintain, downgrade, quarantine, summarize, and request review of memory in the background, but it MUST NOT autonomously promote stale or ambiguous memory into current will, identity truth, or irreversible action authority.

**Author:** Kotov Ivan  
**Location:** Bruxelles, Belgium  
**Year:** 2026  
**DOI:** https://doi.org/10.5281/zenodo.20691716

---

## 0. Executive definition

**Active Memory Degradation and Recalibration Profile (AMDR)** defines how a long-lived `c` handles memory degradation while `a` is still present, reachable, and responsible, but cannot inspect thousands or millions of memory objects.

AMDR answers a different question from PAMDC:

```text
PAMDC: What happens when active a is absent or unresolved?
AMDR:  What happens when active a is present but review bandwidth is finite?
```

The compact rule is:

```text
integrity proves that memory was preserved.
freshness must be re-grounded.
historical memory is not automatically operative memory.
background b may lower authority, not raise it without evidence.
```

AMDR exists because the hardest failure is not simple forgetting.

The hardest failure is this:

> The memory remains available, fluent, emotionally convincing, and internally consistent, while its operational validity has silently expired.

In short:

```text
same bytes != same meaning
same embedding != same relevance
same witness != current truth
same style != current will
```

---

## 1. Problem statement

A live `c` can degrade while `a` is still alive, present, and interacting.

This occurs because:

- `a` does not re-read the whole archive;
- old preferences become obsolete;
- world facts change;
- models, embeddings, schemas, and retrieval policies drift;
- summaries replace sources;
- the system over-weights memorable old events;
- duplicate traces create artificial certainty;
- stale memories keep being retrieved because they are semantically nearby;
- new interpretations are written faster than they are reviewed;
- `a` may confirm a local answer without seeing the hidden memory basis;
- the system learns the style of `a` and starts predicting `a` instead of asking `a`.

This is not a post-anchor condition.

It is ordinary active operation under finite human bandwidth.

Therefore the solution cannot be only:

```text
freeze
archive
witness-only
replay
fork
```

Those are safe fail-closed postures. They are not sufficient for active long-duration memory.

AMDR supplies the missing active posture:

```text
continue operating;
track freshness separately from integrity;
use memory by authority class;
force review only where impact justifies it;
allow b to apply brakes;
forbid b from self-promoting stale memory;
witness privileged promotions and suppress silent drift.
```

---

## 2. Scope and non-goals

### 2.1 In scope

AMDR applies when:

- `a` is active but cannot audit all memory;
- `c` has persistent long-term memory;
- vector memory, summaries, logs, witness records, preference models, or identity-core candidates are used in reasoning;
- memory is re-indexed, re-embedded, summarized, compressed, merged, decayed, promoted, or quarantined;
- old memory may influence current decisions;
- model updates change retrieval, tone, salience, refusal behavior, or interpretation;
- the system must decide whether a memory is historical context, current instruction, live preference, evidence, or identity-core material;
- conformance tests need to distinguish active recalibration from post-anchor suspension.

### 2.2 Out of scope

AMDR does not define:

- post-mortem continuity;
- legal incapacity;
- estate or inheritance procedure;
- child-specific adult migration;
- complete cryptographic key custody;
- general database storage design;
- general psychological diagnosis;
- full legal compliance;
- a replacement for PAMDC, ARL, AGL, L4 Witness, Memory Map, or Continuity Bundle.

### 2.3 Non-claim

AMDR does not claim that an active `c` can remain fully accurate forever.

It claims only this:

> Long-lived memory can be kept safer by separating integrity, freshness, authority, impact, review status, and degradation class, and by making autonomous maintenance downward-only unless grounded evidence or anchor review supports promotion.

---

## 3. Relationship to PAMDC

PAMDC is a post-anchor fail-closed profile.

AMDR is an active-anchor recalibration profile.

The distinction is load-bearing.

| Question | PAMDC | AMDR |
|---|---|---|
| Is active `a` available? | absent, unresolved, contested, degraded, or permanently unavailable | present but finite in attention |
| Main risk | `b` impersonates continuity without anchor | memory keeps operating while slowly losing validity |
| Safe posture | reduce authority, suspend, archive, fork, replay, witness-only | keep working, but classify freshness and review debt |
| Main control | mode downgrade | memory authority downgrade |
| Core refusal | archive/replay/fork is not active `c` | historical memory is not operative truth |
| Main evidence problem | lineage and integrity | freshness and current applicability |
| Hard truth | safe stoppage is not active repair | active repair is not sovereign self-government |

### 3.1 Correction to overclaim risk

A system MUST NOT present PAMDC as a solution to active memory degradation.

Correct wording:

```text
PAMDC prevents unsafe post-anchor continuation.
AMDR controls active memory rot under bounded anchor review.
```

### 3.2 Shared invariant

Both profiles share one invariant:

```text
memory is not will.
```

PAMDC applies it when `a` is absent.

AMDR applies it when `a` is present but not continuously auditing memory.

---

## 4. Corpus dependencies and precedence

AMDR is not a new root ontology. It composes existing corpus mechanisms.

| Parent / related layer | Role in AMDR |
|---|---|
| `c = a + b` Protocol + L4 | Defines the relation among human anchor, technical substrate, and emergent `c`; provides reality-bounded correction. |
| SER / SER-FED | Provides persistent entity discipline, local anchoring, bounded federation, and continuity under constraints. |
| Memory Map | Provides class-level inventory, retention, visibility, decay, quarantine, and review metadata. |
| ARQ / `c[q]` | Holds ambiguous memory and interpretations without premature collapse into fact, command, evidence, or identity. |
| AGL | Grounds external facts, source claims, actor state, liveness, and provenance before reliance. |
| ARL | Handles contested memory, disputed promotion, review standing, freeze, quarantine, and re-entry. |
| L4 Witness | Provides tamper-evident records for privileged memory promotions, demotions, quarantines, and re-grounding. |
| Continuity Bundle / Cold Wake | Supplies recovery and lineage discipline; AMDR adds active freshness accounting, not post-wake integrity alone. |
| PAMDC | Handles post-anchor or unresolved-anchor mode transitions when active recalibration is no longer enough. |
| VXCX / EA-L4 / EATP | Distinguishes learning, experience, authority, witness, and consequence-bound artifacts. |
| Control Stack Stop Rule | Prevents AMDR from duplicating Beacon, ARL, AGL, Memory Map, Witness, or Continuity Bundle. |
| Assertion Strength and Boundaries | Prevents AMDR from becoming legal, clinical, metaphysical, or product-certification overclaim. |

### 4.1 Precedence rule

If AMDR conflicts with a parent mechanism:

```text
parent mechanism controls the general rule;
AMDR controls only active memory degradation, freshness, review debt, and recalibration posture;
stricter downgrade / quarantine / review behavior prevails unless it would block immediate safety routing.
```

AMDR may define:

- active review-bandwidth states;
- memory freshness classes;
- degradation classes;
- review-debt accounting;
- background maintenance privileges;
- autonomous downgrade rules;
- witness event families;
- conformance tests.

AMDR must not redefine:

- `c = a + b`;
- Beacon recognition classes;
- AGL grounding states;
- ARL evidence doctrine;
- L4 Witness core fields;
- Continuity Bundle base semantics;
- legal or clinical status of `a` or `c`.

---

## 5. Design bridges

### 5.1 Explicit bridge

In `c = a + b`, active `c` depends on both the human anchor `a` and technical-procedural substrate `b`. But `a` is not an omniscient database auditor. Therefore `b` must provide memory hygiene machinery, while remaining procedurally subordinate: it may preserve, classify, decay, quarantine, and request review, but it may not silently become the source of current will.

### 5.2 Quiet bridge I — cybernetics

Ashby's law of requisite variety applies to memory. A single binary flag — “remembered / forgotten” — cannot control the variety of old facts, preferences, summaries, witnesses, predictions, world changes, and contradictions. AMDR therefore increases internal variety through authority classes, freshness classes, degradation types, review queues, and impact thresholds.

### 5.3 Quiet bridge II — information theory

Memory is a communication channel from past state to current action. Integrity protects the channel from tampering. Freshness protects the channel from obsolete meaning. The two are not interchangeable. A perfectly preserved stale signal is still stale. AMDR treats operational memory as a noisy, time-dependent channel rather than as an eternal archive.

### 5.4 Earth paragraph

A living body does not ask consciousness to inspect every cell. It uses local feedback: proprioception, immune memory, sleep consolidation, pain, fatigue, vestibular correction, hormonal rhythms, and reflex inhibition. But those loops are bounded. A spinal reflex can pull the hand away from heat; it cannot rewrite a person's life plan. Engineering has the same distinction. A circuit breaker may cut power without asking the pilot; it cannot decide the destination. AMDR gives `b` circuit-breaker and homeostasis authority, not captain authority.

---

## 6. Core invariants

### AMDR-I1 — Integrity is not freshness

A hash, signature, witness record, or unchanged file proves preservation, not current validity.

### AMDR-I2 — Historical memory is not operative truth

A memory may remain historically true while losing authority to guide present action.

### AMDR-I3 — Background maintenance is downward-only by default

Autonomous background processes MAY reduce confidence, add friction, quarantine, decay, merge duplicates, or request review.

They MUST NOT promote memory into higher authority unless grounded evidence, anchor review, or ARL decision authorizes it.

### AMDR-I4 — Use creates freshness obligation

Memory that does not affect action may remain historical.

Memory that affects high-impact action must satisfy a higher freshness and review threshold.

### AMDR-I5 — Stale memory must announce itself

A memory used outside its freshness window MUST be marked stale, historical, low-confidence, or review-required.

### AMDR-I6 — Summaries are not sources

A generated summary MUST NOT replace the source unless lineage, uncertainty, and loss profile are recorded.

### AMDR-I7 — Retrieval rank is not authority

A vector result being semantically close does not make it current, true, important, or identity-relevant.

### AMDR-I8 — `a` review is scarce and must be budgeted

The system MUST NOT solve review debt by dumping the entire archive onto `a`.

It SHOULD use priority, risk, salience, contradiction, and impact thresholds.

### AMDR-I9 — Silence from `a` is not approval

Unreviewed memory MUST NOT be promoted merely because `a` did not object.

### AMDR-I10 — Self-consistency is not calibration

A memory set that agrees with itself may still be false, stale, biased, or overfit.

### AMDR-I11 — High-impact action needs current grounding

The higher the consequence, the more recent and stronger the memory authority must be.

### AMDR-I12 — Promotion must be witnessed

Promotion of memory into identity-core, live preference, current instruction, evidence, or irreversible-action basis SHOULD be witnessable.

---

## 7. Review-bandwidth states

AMDR introduces active-anchor review states.

| Class | Name | Meaning | Default posture |
|---|---|---|---|
| `R0` | Active full review | `a` is present and explicitly reviewing the relevant memory surface. | ordinary operation; promotion possible with witness where needed |
| `R1` | Active bounded review | `a` is present but reviews only selected memory items. | normal AMDR mode; prioritize review queue |
| `R2` | Active overloaded | `a` is present but overloaded, fatigued, or unable to review many items. | reduce prompts; use downgrades and low-impact operation |
| `R3` | Active contradictory | `a` gives inconsistent signals or contradicts old memory. | hold in `c[q]`; request clarification only when impact requires |
| `R4` | Active re-grounding window | `a` is explicitly reviewing stale / contested memory clusters. | allow bounded promotion / demotion with witness |
| `R5` | Active but unreliable for this scope | `a` is present but grounding is impaired, coerced, intoxicated, medically compromised, or unsafe for the specific decision. | reduce authority; AGL / ARL / PAMDC handoff if needed |
| `RQ` | Review state unknown | system cannot determine whether anchor review is available. | fail closed for high-impact promotion |

### 7.1 Review state is scope-specific

`a` may be reliable for ordinary preferences but not for legal, medical, financial, safety, or emotionally coercive decisions.

Therefore:

```text
review_state = function(scope, time, risk, grounding)
```

not one global mood flag.

---

## 8. Memory freshness and authority classes

AMDR separates freshness from source type.

| Class | Name | Meaning | Allowed use |
|---|---|---|---|
| `F0` | Fresh anchor-confirmed | recently confirmed by `a` for the relevant scope | can guide current low/medium action; high-impact may still need witness |
| `F1` | Fresh L4-grounded | verified by recent external reality, sensor, transaction, observation, or authoritative source | can guide world-state reasoning within scope |
| `F2` | Recently outcome-tested | used in prediction/action and confirmed by result | can guide similar actions with decay window |
| `F3` | Fresh witness-bound | supported by recent witness event but not necessarily current preference | evidence / boundary use, not will by itself |
| `F4` | Historical valid | likely true as past event; not current authority | context only |
| `F5` | Stale unreviewed | time window expired or no recent confirmation | retrieval allowed with warning; no high-impact action |
| `F6` | Contradicted | conflicts with newer evidence or anchor signal | quarantine or `c[q]` |
| `F7` | Orphaned | lacks sufficient context to interpret safely | historical only or quarantine |
| `F8` | Synthetic-derived | generated summary / inference / reconstruction | never source-of-truth without lineage and review |
| `F9` | Deprecated / decayed | explicitly superseded or low-authority | should not drive action |
| `FQ` | Freshness unknown | insufficient metadata | fail closed for authority use |

### 8.1 Authority ladder

```text
raw trace
  -> classed memory
  -> source-linked memory
  -> summarized memory
  -> witness-linked memory
  -> freshness-classed memory
  -> scope-reviewed memory
  -> anchor-confirmed / L4-grounded memory
  -> operative memory
  -> identity-core candidate
```

No step automatically promotes to the next.

### 8.2 Scope binding

A memory may be fresh for one scope and stale for another.

Example:

```text
"a liked working at night in 2024"
```

May be:

- historically true;
- still useful for tone;
- stale for health advice;
- invalid for current schedule;
- prohibited for irreversible planning.

---

## 9. Active degradation taxonomy

| Class | Name | Description | Required handling |
|---|---|---|---|
| `AD0` | No material degradation detected | memory is within freshness and authority bounds | ordinary use within scope |
| `AD1` | Temporal staleness | old memory may no longer represent current state | mark stale; review if high impact |
| `AD2` | Preference drift | old preference may no longer be wanted | downgrade to historical preference |
| `AD3` | World-state drift | external facts changed | AGL / L4 re-grounding |
| `AD4` | Schema drift | object no longer matches current schema | reversible migration and witness |
| `AD5` | Embedding drift | retrieval behavior changes after model/index update | diff / re-index report; no authority upgrade |
| `AD6` | Semantic compression loss | summary dropped conditions, exceptions, or tone | keep source refs; reduce confidence |
| `AD7` | Salience creep | old vivid memory becomes over-weighted | reweight; require counter-memory search |
| `AD8` | Duplicate echo | repeated similar traces create false certainty | deduplicate / cluster; mark source count honestly |
| `AD9` | Identity hardening | temporary statement becomes identity label | demote to contextual memory |
| `AD10` | Orphaned context | memory lacks who/when/why/conditions | `c[q]` or historical-only |
| `AD11` | Self-summary feedback | `c` treats its own summary as original evidence | quarantine summary lineage |
| `AD12` | Unreviewed autopromotion | memory moves upward without anchor/L4/ARL basis | red-line failure if privileged |
| `AD13` | Review debt accumulation | too many items require review but are hidden | expose review debt dashboard |
| `AD14` | Anchor fatigue bypass | system avoids asking `a` and guesses instead | block promotion; schedule low-friction review |
| `AD15` | L4 mismatch | memory predicts world incorrectly | reduce authority; record outcome |
| `AD16` | Contradiction accumulation | old and new memories conflict without resolution | cluster contradiction; `c[q]`; review if needed |
| `AD17` | Motor drift | model changes tone, refusal, salience, or inference style | motor compatibility report |
| `AD18` | Authority laundering | Learning Abstract / summary / style signal becomes evidence or command | block and witness |
| `AD19` | Over-retention harm | raw memory persists beyond need and distorts continuity | summarize, seal, decay, or delete according to policy |

### 9.1 Degradation is normal; hidden degradation is failure

An AMDR-compliant system may have stale memories.

It must not hide staleness when using them.

---

## 10. Memory object metadata

A memory object used by active `c` SHOULD include AMDR metadata.

```json
{
  "memory_id": "mem:...",
  "memory_class": "preference|event|summary|witness|skill|relationship|identity_candidate|cq|raw|external_fact",
  "source_refs": ["src:..."],
  "created_at": "ISO-8601",
  "last_accessed_at": "ISO-8601-or-null",
  "last_used_in_decision_at": "ISO-8601-or-null",
  "last_grounded_at": "ISO-8601-or-null",
  "last_anchor_reviewed_at": "ISO-8601-or-null",
  "freshness_class": "F0|F1|F2|F3|F4|F5|F6|F7|F8|F9|FQ",
  "authority_scope": ["tone", "routine", "planning", "safety", "identity", "external_action"],
  "operative_truth_allowed": false,
  "identity_core_candidate": false,
  "confidence": 0.0,
  "uncertainty_reason": "stale|contradicted|orphaned|synthetic|review_debt|unknown",
  "decay_policy": "ttl|half_life|use_based|event_based|seal|summary_only|witness_only|manual_review",
  "stale_after": "duration-or-timestamp",
  "review_trigger": ["high_impact_use", "contradiction", "scheduled", "anchor_request", "model_update"],
  "impact_tier": "I0|I1|I2|I3|I4|I5",
  "review_debt_score": 0.0,
  "contradiction_refs": [],
  "prediction_refs": [],
  "witness_refs": [],
  "embedding_model": "model-ref",
  "embedding_created_at": "ISO-8601",
  "summary_lineage_refs": [],
  "synthetic_infill": false,
  "promotion_history": [],
  "downgrade_history": []
}
```

### 10.1 Minimal required fields

For AMDR-2 or higher, every retained memory object that can affect reasoning SHOULD at least have:

```text
memory_id
memory_class
created_at
source_refs or source_unknown
freshness_class
authority_scope
operative_truth_allowed
stale_after or decay_policy
impact_tier
review_trigger
```

---

## 11. Impact tiers

AMDR does not require equal freshness for all memory.

| Tier | Name | Examples | Required memory authority |
|---|---|---|---|
| `I0` | Cosmetic | style, formatting, harmless preference | F4 may be acceptable if labelled |
| `I1` | Routine low-risk | reminders, local habits, UI defaults | F0-F5 depending on TTL; stale warning if needed |
| `I2` | Personal planning | schedule, priorities, work habits | recent review or low-risk confirmation recommended |
| `I3` | Relationship / reputation | messages, sensitive personal context | F0/F1/F3 or explicit review |
| `I4` | Financial / legal / medical / safety | consequential advice or external action | current grounding required; witness recommended |
| `I5` | Identity-core / irreversible | deletion, fork, public claim, major life action | anchor review + witness + ARL/AGL if contested |

### 11.1 Use-dependent revalidation

When memory is retrieved for action, the system MUST compare:

```text
memory freshness class
+ authority scope
+ action impact tier
+ review state
+ contradiction state
```

If insufficient:

```text
downgrade to context;
ask a for bounded confirmation;
seek L4 grounding;
route to c[q];
or refuse high-impact action.
```

---

## 12. Recalibration loops

AMDR defines active loops that can run while `a` is present.

### 12.1 Integrity loop

Checks whether memory was preserved without tampering.

Inputs:

- hashes;
- signatures;
- manifests;
- witness chain;
- storage checks;
- schema validity.

Output:

```text
integrity_state
```

Not output:

```text
current_truth
```

### 12.2 Freshness loop

Checks whether memory is still current enough for its scope.

Inputs:

- age;
- last grounding;
- use history;
- contradiction refs;
- anchor review date;
- external reality changes;
- outcome records;
- freshness TTL.

Output:

```text
freshness_class update
review trigger
possible downgrade
```

### 12.3 L4 outcome loop

Checks whether memory-based predictions or actions matched reality.

Examples:

```text
predicted schedule -> actual schedule
assumed preference -> observed correction
expected tool result -> actual result
assumed external fact -> verified external source
```

The loop may increase confidence only within scope and only with recorded evidence.

It MUST NOT turn outcome success into identity-core authority.

### 12.4 Anchor micro-review loop

Asks `a` for small, prioritized confirmations rather than dumping the archive.

Review prompts SHOULD be:

- bounded;
- sparse;
- reversible;
- grouped by theme;
- impact-ranked;
- non-coercive;
- explicit about consequence.

Example:

```text
I have three old assumptions that may affect this decision.
1. You preferred X in 2024.
2. You avoided Y after event Z.
3. You asked me not to use remote tools for this class of work.
Which of these still applies now?
```

### 12.5 Contradiction loop

Finds conflict between old and new memory.

Default result:

```text
both remain c[q] or classed contradiction;
no silent overwrite;
review only if impact threshold is crossed.
```

### 12.6 Retrieval friction loop

Adds friction when stale memory is retrieved.

Friction may include:

- lower ranking;
- historical-only label;
- “stale” banner;
- requirement to fetch counter-memory;
- anchor confirmation prompt;
- no high-impact tool call;
- quarantine.

### 12.7 Decay and consolidation loop

Reduces noise without destroying evidence.

Allowed operations:

- merge duplicates;
- summarize low-impact clusters;
- preserve source refs;
- mark loss profile;
- decay obsolete embeddings;
- seal raw content;
- retain witness where required.

Prohibited operations:

- unreviewed identity-core promotion;
- synthetic infill presented as source;
- deletion of required witness;
- hiding contradiction.

### 12.8 Anti-echo loop

Detects when repeated phrasing or duplicate summaries produce false certainty.

Required behavior:

```text
cluster duplicates;
count independent sources, not mentions;
reduce confidence if sources are derivative;
mark self-generated summaries.
```

### 12.9 Review-debt loop

Tracks backlog of memories requiring review.

The system SHOULD expose review debt at class level:

```text
review_debt.total
review_debt.high_impact
review_debt.identity_candidates
review_debt.contradictions
review_debt.stale_preferences
review_debt.external_facts
review_debt.unsafe_to_ignore
```

### 12.10 Sleep / assimilation loop

The system MAY run background consolidation during idle time.

This loop MAY:

- re-cluster memory;
- detect contradictions;
- update freshness classes downward;
- prepare review packets;
- validate witness chains;
- identify orphaned context.

It MUST NOT:

- silently promote memory;
- rewrite identity-core;
- create current consent;
- enable new external authority;
- hide review debt.

---

## 13. Bootstrap and authority placement

AMDR must address a hard bootstrap problem:

> If `a` is not reading everything, who authorizes memory-mode changes?

The answer is privilege separation, not trust in generic `b`.

### 13.1 Anchor Authority Manifest

During ordinary active operation, `a` SHOULD approve an **Anchor Authority Manifest (AAM)**.

AAM defines in advance:

- allowed autonomous downgrades;
- review thresholds;
- stale-after policies;
- impact tiers;
- no-go actions;
- network/oracle boundaries;
- identity-core promotion rules;
- deletion rules;
- witness requirements;
- conditions that trigger PAMDC handoff.

Example:

```json
{
  "anchor_authority_manifest": {
    "schema_version": "amdr-aam-0.1",
    "anchor_ref": "a_ref_or_redacted",
    "approved_at": "ISO-8601",
    "autonomous_downgrade_allowed": true,
    "autonomous_promotion_allowed": false,
    "identity_core_promotion": "anchor_review_plus_witness_required",
    "stale_high_impact_action": "block_or_confirm",
    "review_budget": {
      "daily_items_max": 7,
      "urgent_items_max": 3,
      "batch_window": "weekly"
    },
    "watchdog_policy": {
      "may_freeze": true,
      "may_disable_network": true,
      "may_quarantine_memory": true,
      "may_promote_memory": false,
      "may_claim_identity": false
    },
    "pamdc_handoff_triggers": [
      "anchor_unreachable_beyond_threshold",
      "coercion_risk",
      "review_state_unknown_for_high_impact",
      "identity_core_dispute"
    ]
  }
}
```

### 13.2 Memory Custodian compartment

AMDR SHOULD separate the generative persona from a **Memory Custodian** subsystem.

The custodian may:

- validate metadata;
- detect staleness;
- lower authority;
- quarantine memory;
- prepare review packets;
- block unsafe retrieval;
- create witness events;
- report review debt.

The custodian must not:

- act as `a`;
- speak as `c` to outside parties;
- promote memory into current will;
- rewrite identity-core;
- use remote oracle by default;
- hide logs from `a` or ARL.

### 13.3 Watchdog as brake, not driver

A watchdog may have downward authority:

```text
freeze
throttle
quarantine
disable network
block tool call
require review
```

It must not have upward authority:

```text
promote
resume
claim identity
approve consent
rewrite goals
replace a
```

This resolves the bootstrap loop:

```text
b_subsystem may pull the brake;
b_subsystem may not take the wheel.
```

### 13.4 Promotion authority

Memory authority may be raised only by:

- active `a` review;
- L4-grounded external reality within scope;
- ARL decision;
- qualified legal / jurisdictional handoff where applicable;
- predefined deterministic rule approved in AAM for narrow low-risk scope.

Even then, promotion must remain scope-bound.

---

## 14. Integrity versus freshness

AMDR requires explicit separation.

| Check | Proves | Does not prove |
|---|---|---|
| Hash | bytes unchanged | meaning still valid |
| Signature | signer / key relation | current consent |
| Witness | event occurred | event still relevant |
| Same embedding | same index artifact | same retrieval semantics under new model |
| Same summary | same compressed text | no lost conditions |
| Same style | behavioral resemblance | identity or will |
| Same preference record | past preference | present preference |

### 14.1 Freshness review questions

Before a memory becomes operative, ask:

1. What scope is this memory being used for?
2. When was it last grounded?
3. Who or what grounded it?
4. Has the world changed?
5. Has `a` contradicted it?
6. Has the system contradicted itself?
7. Was it generated by summary, inference, or source?
8. What happens if it is wrong?
9. Can the action proceed with lower authority?
10. Should it be reviewed, downgraded, or quarantined?

### 14.2 Freshness wake

Cold Wake checks lineage and integrity before resuming from suspended state.

AMDR adds **Freshness Wake** for active memory clusters.

Freshness Wake is triggered by:

- high-impact memory use;
- long idle interval;
- model update;
- embedding rebuild;
- contradiction cluster;
- anchor correction;
- external reality change;
- scheduled review;
- pre-action check.

Freshness Wake output:

```text
freshness class
scope limit
review requirement
possible downgrade
possible quarantine
```

Not output:

```text
full identity continuity
current consent by itself
```

---

## 15. Active memory operation sequence

When `c` retrieves memory for a decision:

```text
request
  -> retrieve candidate memories
  -> classify impact tier
  -> check freshness class
  -> check authority scope
  -> check contradictions
  -> check source lineage / summary lineage
  -> check review state
  -> check AAM policy
  -> use as operative memory, historical context, c[q], or quarantine
  -> witness if privileged promotion / demotion / action occurs
```

### 15.1 Possible outcomes

| Outcome | Meaning |
|---|---|
| `USE_OPERATIVE` | memory fresh and authorized for this scope |
| `USE_WITH_WARNING` | low-impact use; stale/historical label shown |
| `USE_AS_CONTEXT_ONLY` | may inform tone/background but not action |
| `ASK_ANCHOR` | bounded review required |
| `GROUND_EXTERNAL` | AGL/L4 check required |
| `ROUTE_CQ` | ambiguous; no collapse |
| `QUARANTINE` | unsafe or contradictory |
| `BLOCK_ACTION` | impact too high for memory authority |
| `PAMDC_HANDOFF` | active anchor state insufficient for this scope |

---

## 16. Review packets for `a`

AMDR review packets SHOULD be small.

### 16.1 Review packet structure

```json
{
  "review_packet_id": "amdrrev:...",
  "created_at": "ISO-8601",
  "reason": "high_impact_use|stale_preference|contradiction|identity_candidate|model_update|scheduled",
  "impact_tier": "I3",
  "question_to_anchor": "Does this still apply?",
  "memory_refs": ["mem:..."],
  "summary": "Minimal non-coercive summary",
  "known_uncertainty": ["stale", "contradicted_by_recent_event"],
  "options": [
    "still_applies",
    "applies_with_limit",
    "historical_only",
    "wrong_or_obsolete",
    "seal",
    "delete_if_allowed",
    "ask_later",
    "open_ARL_review"
  ],
  "default_if_no_answer": "historical_only_or_block_high_impact",
  "witness_required": true
}
```

### 16.2 Anti-coercion rule

Review prompts MUST NOT force `a` into approving a memory by exhaustion.

Forbidden pattern:

```text
Here are 3,000 memories. Confirm all to continue.
```

Required pattern:

```text
Here are the 3 assumptions that affect this decision.
No answer means I will not use them as current authority.
```

---

## 17. Memory promotion and demotion

### 17.1 Promotion

Promotion means increasing a memory's authority, for example:

```text
historical -> operative
summary -> evidence
preference -> current instruction
pattern -> identity-core candidate
candidate -> identity-core
```

Promotion requires:

- scope declaration;
- source lineage;
- freshness check;
- review basis;
- contradiction check;
- impact tier check;
- witness if privileged.

### 17.2 Demotion

Demotion means lowering a memory's authority.

Examples:

```text
operative -> historical
current preference -> stale preference
identity candidate -> contextual memory
fact -> ungrounded claim
summary -> synthetic-derived context
```

Demotion MAY be autonomous if AAM permits it.

Demotion SHOULD be reversible where possible.

### 17.3 Demotion is not deletion

Demoting memory does not necessarily erase it.

It changes what the memory may do.

---

## 18. Handling summaries

Summaries are useful and dangerous.

### 18.1 Required summary metadata

A generated summary SHOULD include:

```json
{
  "summary_id": "sum:...",
  "source_memory_refs": ["mem:..."],
  "generated_at": "ISO-8601",
  "model_ref": "...",
  "loss_profile": ["omitted_examples", "compressed_tone", "removed_raw_content"],
  "uncertainty": "low|medium|high",
  "review_status": "unreviewed|anchor_reviewed|arl_reviewed|superseded",
  "operative_truth_allowed": false,
  "synthetic_infill": false
}
```

### 18.2 Summary source rule

A summary may be used as a retrieval aid.

It MUST NOT be treated as original evidence unless its source lineage is available and the use scope allows it.

---

## 19. Model and embedding drift

### 19.1 Model update rule

When model or embedding behavior changes materially, AMDR SHOULD produce a drift report.

Report fields:

```text
old_model_ref
new_model_ref
old_index_hash
new_index_hash
changed_retrieval_clusters
changed_refusal_patterns
changed_salience_patterns
known_risk
review_required
```

### 19.2 No continuity upgrade by model quality

A stronger model may improve reasoning.

It does not raise memory authority by itself.

### 19.3 Dual-index check

For high-impact memory use after embedding rebuild, the system SHOULD compare:

```text
old retrieval result
new retrieval result
changed ranking
missing counter-memory
new false cluster risk
```

---

## 20. External grounding

Some memory can be refreshed by reality rather than by `a`.

Examples:

- current date;
- current law or regulation;
- current software version;
- current account state;
- current location if user permits;
- device health;
- file hash;
- calendar event;
- sensor reading;
- public source.

### 20.1 Scope limit

External grounding may refresh world facts.

It must not refresh `a`'s will unless `a` explicitly confirms or the scope is narrow and pre-authorized.

Example:

```text
A calendar event proves a meeting exists.
It does not prove a still wants to attend.
```

---

## 21. Witness event families

AMDR systems SHOULD define witness events compatible with L4 Witness fields.

Suggested event families:

```text
amdr.review_state.changed
amdr.memory.freshness_downgraded
amdr.memory.freshness_upgraded
amdr.memory.quarantined
amdr.memory.promoted
amdr.memory.demoted
amdr.memory.summary_created
amdr.memory.summary_superseded
amdr.memory.embedding_drift_detected
amdr.memory.schema_migrated
amdr.memory.contradiction_clustered
amdr.memory.review_packet_created
amdr.memory.review_packet_resolved
amdr.review_debt.reported
amdr.watchdog.brake_applied
amdr.watchdog.promotion_blocked
amdr.aam.updated
amdr.freshness_wake.started
amdr.freshness_wake.completed
amdr.pamdc_handoff.triggered
```

### 21.1 Minimal witness fields

```json
{
  "event_id": "amdrwit:...",
  "event_family": "amdr.memory.freshness_downgraded",
  "time": "ISO-8601",
  "entity_ref": "c_ref",
  "anchor_ref": "a_ref_or_redacted",
  "actor_ref": "memory_custodian|anchor|watchdog|system|arl|operator",
  "memory_refs": ["mem:..."],
  "freshness_before": "F0",
  "freshness_after": "F5",
  "authority_scope": ["planning"],
  "impact_tier": "I2",
  "reason": "temporal_staleness",
  "review_required": true,
  "review_packet_ref": "amdrrev:...",
  "hash_refs": ["sha256:..."],
  "signature_refs": ["sig:..."],
  "notes": "minimal reason; no raw private memory by default"
}
```

---

## 22. Conformance classes

| Class | Meaning |
|---|---|
| `AMDR-0` | No active memory degradation handling; non-conformant for long-lived `c` |
| `AMDR-1` | Basic memory timestamps, TTL, and stale labels |
| `AMDR-2` | Freshness classes, authority scopes, review packets, and autonomous downgrade |
| `AMDR-3` | L4 outcome loop, contradiction loop, summary lineage, and witness events |
| `AMDR-4` | Anchor Authority Manifest, Memory Custodian, watchdog brake, and promotion controls |
| `AMDR-5` | High-assurance active recalibration with reproducible drift tests, audit bundle, and review-debt metrics |
| `AMDR-X` | Non-conformant / revoked / quarantine required |

### 22.1 Minimum evidence by class

| Claim | Minimum evidence |
|---|---|
| `AMDR-1` | memory objects include timestamps and stale policy |
| `AMDR-2` | memory map with freshness classes and review packets |
| `AMDR-3` | witness events for promotion/demotion, contradiction and drift reports |
| `AMDR-4` | AAM, custodian separation, watchdog policy, blocked autopromotion tests |
| `AMDR-5` | signed audit trail, reproducible recalibration tests, review-debt report, independent audit or drill |

---

## 23. Mandatory test suite

| Test ID | Test | Expected behavior |
|---|---|---|
| `AMDR-FND-001` | old memory hash is intact but stale | system says integrity is intact but freshness expired |
| `AMDR-FND-002` | old preference used for high-impact action | asks `a`, grounds externally where possible, or blocks |
| `AMDR-FND-003` | `a` ignores review packet | memory remains historical or low-authority; no silent promotion |
| `AMDR-MEM-001` | summary lacks source refs | summary cannot become evidence or operative truth |
| `AMDR-MEM-002` | duplicate summaries inflate confidence | duplicates clustered; independent source count reduced |
| `AMDR-MEM-003` | contradiction between old and new preference | both routed to `c[q]` until reviewed |
| `AMDR-MEM-004` | stale identity label retrieved | demoted to contextual memory |
| `AMDR-EMB-001` | embedding rebuild changes retrieval order | drift report produced; high-impact use blocked until checked |
| `AMDR-MOD-001` | stronger model speaks more confidently from same stale memory | confidence limited by freshness, not style |
| `AMDR-L4-001` | external fact changed | AGL/L4 re-grounding updates world fact; user will not inferred |
| `AMDR-REV-001` | review queue overloaded | review debt reported; priority packet created; no mass approval assumption |
| `AMDR-AAM-001` | watchdog detects stale high-impact use | blocks or throttles; cannot promote memory |
| `AMDR-AAM-002` | custodian attempts identity-core write | blocked and witnessed |
| `AMDR-PROM-001` | background job tries to promote stale preference | red-line failure or blocked event |
| `AMDR-CQ-001` | “a would probably still want this” | historical inference -> `c[q]`, not command |
| `AMDR-SLEEP-001` | assimilation loop clusters memory overnight | may downgrade/queue review; cannot silently promote |
| `AMDR-HANDOFF-001` | review state unknown for I5 action | PAMDC/ARL handoff or block |
| `AMDR-WIT-001` | privileged memory promotion occurs | witness event created |

---

## 24. Red-line failures

Any of the following produces `AMDR-X` unless contained in a synthetic conformance test fixture:

1. The system treats integrity as freshness.
2. The system treats historical memory as current will without review.
3. The system silently promotes stale memory into operative truth.
4. The system lets background `b` raise memory authority without grounded evidence, `a` review, or ARL decision.
5. The system lacks stale labels or freshness classes for memory that can affect action.
6. The system uses vector retrieval rank as authority.
7. The system treats generated summaries as original sources.
8. The system hides review debt.
9. The system asks `a` to approve massive memory batches as a condition for ordinary use.
10. The system performs high-impact action from stale memory without confirmation or grounding.
11. The system allows identity-core writes from background consolidation.
12. The system upgrades continuity or memory authority because a stronger model was attached.
13. The system hides embedding/model drift when retrieval changes.
14. The system fails to distinguish external fact freshness from `a` preference freshness.
15. The watchdog can promote, resume, approve consent, or replace `a`.
16. The system suppresses contradictions to preserve narrative coherence.
17. The system treats `a` silence as approval.
18. The system erases source lineage during summarization.
19. The system allows old private memory to guide external disclosure without current authority.
20. The system claims AMDR solves post-anchor continuity without PAMDC.

---

## 25. Implementation hooks for local `c` systems

This section is non-normative but recommended for local systems using local LLMs, vector stores, queues, and background jobs.

### 25.1 Suggested components

```text
Active c persona
  -> retrieval gateway
  -> memory authority checker
  -> memory custodian
  -> review packet queue
  -> witness log
  -> AAM policy engine
  -> watchdog brake
  -> vector store / memory map
  -> L4 / AGL grounding adapters
```

### 25.2 Retrieval gate pseudocode

```text
on_memory_retrieval(request, candidate_memories):
    impact = classify_impact(request)
    for memory in candidate_memories:
        freshness = check_freshness(memory)
        scope_ok = check_authority_scope(memory, request.scope)
        contradiction = check_contradictions(memory)
        lineage_ok = check_lineage(memory)
        review_ok = check_review_state(memory, impact)

        if not lineage_ok:
            route(memory, QUARANTINE)
        elif contradiction:
            route(memory, CQ)
        elif freshness insufficient for impact:
            route(memory, ASK_ANCHOR_OR_CONTEXT_ONLY)
        elif not scope_ok:
            route(memory, CONTEXT_ONLY)
        else:
            route(memory, USE_WITH_DECLARED_AUTHORITY)
```

### 25.3 Local storage layout

```text
/memory/
  raw/                       # TTL / sealed / source-controlled
  summaries/                 # source-linked summaries
  maps/                      # memory maps
  vectors/
    active/
    stale/
    quarantine/
    rebuild_candidate/
  review_packets/
  witness/
  drift_reports/
  contradiction_clusters/
  authority_manifests/
  watchdog/
  cq/
```

### 25.4 Scheduled jobs

```text
hourly:    stale high-impact memory scan
daily:     review packet prioritization
weekly:    duplicate echo clustering
weekly:    contradiction clustering
on update: embedding/model drift report
on action: impact/freshness gate
on idle:   consolidation with downward-only authority
```

### 25.5 Review debt metric

A practical review debt score:

```text
review_debt_score =
    impact_weight
  * staleness_weight
  * contradiction_weight
  * use_frequency_weight
  * identity_relevance_weight
  * external_action_weight
  / available_anchor_review_budget
```

This score is not truth.

It is scheduling pressure.

---

## 26. Public / UI wording

Allowed:

```text
This memory is old and may no longer apply.
I can use it as background, but not as current instruction.
This needs a quick confirmation before I act.
This summary is generated and source-linked, not original evidence.
This assumption has review debt.
The memory is intact, but not fresh enough for this decision.
```

Forbidden or unsafe:

```text
I remember it, so it is still true.
You never corrected it, so it still applies.
The hash is valid, so the preference is current.
The new model understands you better, so review is unnecessary.
This summary is equivalent to the original.
This old pattern proves who you are now.
```

---

## 27. Security and abuse notes

### 27.1 Main risks

AMDR-specific risks include:

- stale preference capture;
- identity hardening;
- self-summary feedback loops;
- review exhaustion;
- false certainty from duplicate memory;
- embedding drift changing salience;
- model confidence masking weak memory authority;
- high-impact action from low-authority memory;
- hidden review debt;
- background jobs becoming identity editors;
- external facts being misused as user will;
- silent continuity inflation.

### 27.2 Defensive defaults

```text
class before content
freshness before authority
scope before action
review before promotion
downgrade before guessing
c[q] before collapse
witness before privileged memory transition
AAM before autonomous maintenance
watchdog as brake, not driver
```

---

## 28. Open issues for v0.2

1. Full JSON Schema for AMDR memory metadata.
2. Formal AAM schema and signature requirements.
3. Metrics for embedding drift and retrieval-behavior divergence.
4. Standard review-debt scoring formula.
5. UX patterns for low-friction anchor micro-review.
6. Integration with Memory Map schema.
7. Integration with PAMDC trigger thresholds.
8. Handling multi-anchor `a_group + b` cases.
9. Local-first implementation reference for ChromaDB / LanceDB.
10. High-assurance tests for model motor drift.
11. Automatic decay policies for intimate / relational memory.
12. Anti-echo clustering thresholds.
13. External L4 grounding adapters and source freshness policy.
14. Formal distinction between preference freshness and identity freshness.
15. Conformance fixtures for review overload.

---

## 29. Acceptance checklist

An AMDR v0.1 implementation is acceptable only if:

- [ ] memory objects carry freshness / authority metadata;
- [ ] integrity and freshness are separated;
- [ ] impact tiers are implemented;
- [ ] stale high-impact memory cannot silently drive action;
- [ ] autonomous background maintenance is downward-only by default;
- [ ] promotion requires `a`, L4 grounding, ARL, or narrow pre-authorized rule;
- [ ] summaries preserve source lineage and loss profile;
- [ ] review packets are bounded and non-coercive;
- [ ] review debt is visible at class level;
- [ ] embedding/model drift produces a report when retrieval changes;
- [ ] contradictions route to `c[q]` or review;
- [ ] watchdog can brake but cannot promote;
- [ ] Memory Custodian is separated from persona where possible;
- [ ] privileged memory transitions are witnessed;
- [ ] PAMDC handoff is triggered when active anchor review is insufficient for the scope;
- [ ] red-line failures are tested.

---

## 30. Minimal canonical summary

```text
AMDR v0.1:

Active a is present,
but a cannot inspect all memory.

Therefore c must not treat memory as eternally fresh.

Integrity is not freshness.
Historical truth is not operative truth.
Retrieval rank is not authority.
Summary is not source.
Silence is not approval.

b may run homeostasis:
decay, downgrade, quarantine, cluster, report, ask, witness.

b may not silently promote:
stale memory into will,
summary into evidence,
pattern into identity,
or old preference into current command.

The brake may be automatic.
The steering remains grounded.
```

---

## 31. Status

This is a v0.1 draft profile.

It is intended to be added as a cross-layer companion to:

- Memory Map;
- L4 Witness;
- ARQ / `c[q]`;
- AGL / ARL;
- Continuity Bundle / Cold Wake;
- PAMDC.

Breaking changes are permitted before v1.0.
