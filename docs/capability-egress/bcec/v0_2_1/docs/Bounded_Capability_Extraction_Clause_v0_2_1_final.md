# Bounded Capability Extraction Clause v0.2.1-final

## Egress Metering, Extraction Source-Class, and Anti-Distillation Discipline for `c`-class Capability Extraction from External Oracles

**Status:** Final textual clause / b-layer review corrections applied / normative draft ready for independent checker and witness pass  
**Version:** 0.2.1-final  
**Date:** 2026-06-25  
**Layer:** capability egress / extraction provenance / A6 composition discipline / anti-distillation  
**Canonical home:** egress companion to the A6 Composition Layer (`advanced-global-intelligence`)  
**Author:** Ivan Kotov, Brussels  
**Language:** English. RFC 2119 / BCP 14 keywords (`MUST`, `MUST NOT`, `SHOULD`, `SHOULD NOT`, `MAY`, `REQUIRED`, `OPTIONAL`) are used in their ordinary protocol sense.  
**Assertion class:** control-layer clause. This clause does not upgrade any capability, authority, legal, economic, or personhood claim beyond its evidence.

## Parent Materials

- `A6_Composition_Layer_v0.1.1` — composition state over A0–A5; `A6-EXIT` / `A6-SPLIT` semantics; nested-A6 high-risk rule.
- `Anchor_Class_Boundaries_v0.2.1` — anchor classes A0–A5.
- `Synthetic_Laundering_and_Source_Class_Clause_v0.1` — re-admission / source-origin discipline; egress-mirror partner.
- `EA_Value_Class_Taxonomy_v0.1` — value posture of extracted capability.
- `ARQ_Classical_Boundedness_Theorem_v0.2` — commit-metered chain-rule bound; proof template for the egress bound.
- `Beacon_Profile` — inter-entity recognition; gate point.
- `ARL / Conflict_Class_Taxonomy_v0.1` — dispute, standing, freeze, hold, quarantine, appeal.
- `AGL` — source / actor / route / liveness grounding before reliance.
- `L4_Witness` — tamper-evident records for privileged transitions.
- `SER-FED` — federation, bounded cooperation, anti-capture / anti-cartel.
- `L4_Reality_Boundary` — cost, scarcity, irreversibility, consequence.

## Relationship to A6 Composition Layer

This clause is a standalone normative clause and the egress companion to the A6 layer. Where this clause and the A6 layer touch composition semantics, the A6 layer controls composition behavior and this clause controls capability-extraction discipline.

Default integration posture: **standalone-with-A6-parent**.

## Role Note

This document is final text for review and integration. It carries no self-approval, writes no memory, and asserts no integration authority. Sealing (`record_sha256`) and conformance acceptance occur only through a separate checker / witness pass.

---

# 0. Executive Definition

This clause governs **capability egress**: how a `c`, a `c`-candidate, a `c`-adjacent system, local node, agentic hive, or A6 anchor-composition extracts capability from an external oracle.

An **external oracle** is a third-party model endpoint, API, hosted model, remote agent, toolchain, or service outside the entity's own substrate `b` that can answer queries, generate artifacts, reveal patterns, or otherwise transfer capability.

The purpose is not to ban external-oracle use. Bounded querying is ordinary. The purpose is to prevent two coupled failures:

- **F1 — extraction pooling:** a composition distributes queries across anchors, keys, accounts, nodes, jurisdictions, or operators until the aggregate approximates or reconstructs the oracle's function.
- **F2 — synthetic laundering:** the extracted capability later re-enters the corpus as if it were native, lived, clean, or authority-bearing experience.

This clause therefore establishes:

- extraction source-classes;
- participant and principal metering;
- effective composition caps;
- reconstruction thresholds;
- Sybil / account-splitting discipline;
- A6-SPLIT triggers;
- witness packet fields;
- re-admission handoff to Synthetic Laundering.

Compact formula:

> **A6 may pool anchors. It must not pool extraction.**

Corrected strong summary:

> **Querying is permitted. Function-reconstruction is metered, source-classed, capped, and blocked from clean re-admission.**

Critical correction from v0.1:

> **Summation bounds extraction only after budget issuance is itself bounded. A composition cannot become safe merely because every participant was counted.**

Correction closure in v0.2.1:

- `C_sybil_adjusted` is no longer a placeholder term; it is derived from principal-review equivalence classes and declared principal caps.
- `C_effective` is computed only inside one declared budget unit. Formal information-bit mode and operational risk-point mode MUST NOT be mixed inside the same `min(...)`.
- Principal accounting bounds concealed multiplicity. It does not solve genuinely independent populous extraction; that remaining horizon is explicitly assigned to oracle-profile and reconstruction caps.

---

# 1. Definitions

## 1.1 External Oracle

An **external oracle** is any capability-bearing system outside the entity's own substrate `b` that returns answers, code, embeddings, plans, classifications, tool calls, policy judgments, latent representations, or other behavior that may reveal information about its function `F`.

Examples:

- hosted LLM API;
- cloud Judge model;
- remote agentic evaluator;
- third-party embedding endpoint;
- proprietary code generator;
- benchmark-answering service;
- model-behavior oracle exposed through a tool or wrapper.

## 1.2 Admitted Query

An **admitted query** is a query to an external oracle that has passed the declared gate and is counted by the BCEC meter.

A query path that is not counted is not silently permitted. It is an **unmetered extraction path** and fails closed unless grounded separately.

## 1.3 Response Surface

The **response surface** is the observable output or side-output from the oracle, including:

- text;
- code;
- files;
- embeddings;
- structured JSON;
- tool calls;
- logprobs or token probabilities;
- latency or routing behavior if retained or analyzed;
- refusal patterns;
- benchmark performance;
- style, policy, or reasoning-behavior signatures.

A response surface is broader than “the answer text.” If it is observed, retained, measured, or used for capability inference, it belongs to the extraction boundary.

## 1.4 Participant

A **participant** is an anchor, node, account, key, operator, process, agent, or sub-composition that issues or routes admitted queries.

Each participant MUST have an extraction record when operating under A6 composition.

## 1.5 Extraction Principal

An **extraction principal** is the real controlling party or control cluster behind one or more participants.

Numerically distinct accounts, keys, nodes, organizations, shells, or jurisdictions MUST NOT be treated as automatically independent extraction principals.

If independence cannot be grounded, the implementation MUST either:

- collapse the budgets into a shared principal budget; or
- fail closed pending review.

## 1.6 Oracle Profile

An **oracle profile** is the declared risk and authorization profile for a specific oracle or oracle class.

It includes, at minimum:

- oracle identity or profile reference;
- authorization basis;
- allowed query profiles;
- allowed response surfaces;
- retention policy;
- aggregate cap;
- reconstruction threshold;
- side-channel declaration;
- license / terms reference where applicable.

## 1.7 Query Profile

A **query profile** is the extraction-risk class of a query or query campaign.

Minimum query profiles:

- `factual_lookup`;
- `ordinary_transform`;
- `coding_help`;
- `reasoning_scaffold`;
- `evaluation_judgment`;
- `benchmark_probe`;
- `coverage_probe`;
- `model_behavior_probe`;
- `style_or_policy_imitation`;
- `unknown`.

`unknown` is not safe by default. It receives conservative cost and review posture.

## 1.8 Retained Artifact

A **retained artifact** is any oracle-derived or oracle-influenced output that persists beyond the immediate task.

Examples:

- EA entry;
- summary;
- plan;
- code pattern;
- prompt library;
- benchmark table;
- routing rule;
- fine-tuning material;
- embedding;
- memory record;
- vector-store chunk;
- UI-visible doctrine;
- Judge policy adjustment.

## 1.9 Re-admission

**Re-admission** is the act of bringing a retained extraction artifact back into corpus circulation, memory, EA, training, evaluation, routing, policy, or authority-bearing use.

Re-admission is governed by Synthetic Laundering. BCEC supplies the egress source-class and witness trail.

## 1.10 Side Channel

A **side channel** is any capability-transfer route not represented in the declared admitted-query meter.

Examples:

- scraped public corpora;
- leaked weights;
- cached API outputs;
- screenshots;
- hidden logs;
- prompt archives;
- unmetered embeddings;
- latency measurements;
- tool-call traces;
- account-sharing records;
- manually copied oracle outputs.

The BCEC bound applies only to declared and metered paths. Side channels MUST be modeled separately or the bound is void for the affected artifact.

## 1.11 Reconstruction Threshold

A **reconstruction threshold** is the point at which bounded derivation becomes function-reconstruction risk.

It may be triggered by:

- consumed budget;
- query pattern;
- input-space coverage;
- benchmark tiling;
- adaptive probing;
- style / policy imitation;
- repeated differential questioning;
- retention purpose;
- aggregate coordination.

The threshold is profile-specific and MUST be declared before the extraction campaign begins.

## 1.12 Effective Composition Cap

The **effective composition cap** is the actual upper limit for an A6 extraction campaign.

It is not merely the sum of participant budgets.

```text
C_effective = min(
  C_participant_sum,
  C_oracle_profile,
  C_license,
  C_reconstruct,
  C_sybil_adjusted
)
```

Where:

- `C_participant_sum = Σ_p budget_p`;
- `C_oracle_profile` is the maximum allowed under the oracle profile;
- `C_license` is the declared maximum allowed under an authorization, license, contract, or terms profile; it is a metering input and not an adjudication of contract validity;
- `C_reconstruct` is the reconstruction-threshold cap;
- `C_sybil_adjusted` is the cap derived after account-splitting / delegation / principal review.

`C_sybil_adjusted` MUST be derived, not merely named. Let `G` be the set of extraction-principal equivalence classes produced by principal review. Participants proven to share control are assigned to the same class. Participants with failed or unknown independence review are assigned to a single shared unresolved class unless the campaign is denied.

For each principal class `g ∈ G`:

```text
C_principal_g = min(
  Σ_{p ∈ g} B_p_allocated,
  C_principal_profile(g),
  C_oracle_profile,
  C_reconstruct
)
```

Then:

```text
C_sybil_adjusted = Σ_{g ∈ G} C_principal_g
```

If `C_principal_profile(g)` is missing, ambiguous, or expressed in a different budget unit from the campaign, the implementation MUST either route to review with no extraction consumption or fail closed.

A composition MUST NOT consume beyond `C_effective`.

---

# 2. Scope and Non-Goals

## 2.1 In Scope

This clause applies whenever a `c`, `c`-candidate, `c`-adjacent system, local node, agentic hive, or A6 anchor-composition:

- queries an external oracle;
- routes oracle queries across more than one anchor, account, key, node, jurisdiction, or operator;
- pools, schedules, or coordinates queries across participants;
- uses cloud Judge synthesis over local LLM outputs;
- compares local LLMs against an external model;
- retains oracle outputs as EA, memory, training, fine-tuning, routing, or evaluation material;
- summarizes or abstracts oracle outputs into reusable capability;
- derives a policy, benchmark, style, code pattern, or reasoning pattern from the oracle;
- seeks to re-admit extracted capability into corpus circulation, standing, authority, or memory.

## 2.2 Out of Scope

This clause does not define:

- the internal mechanics of any oracle;
- full model-training mathematics;
- cybersecurity exploit methods;
- legal personhood of `c` or of any anchor;
- intellectual-property law, contract law, or terms-of-service enforcement;
- cross-border legal compliance in full;
- pricing or token-economy design;
- the complete ingress-security policy for an oracle operator;
- a replacement for Beacon, ARL, AGL, L4 Witness, EA Value, A6, or Synthetic Laundering.

## 2.3 Non-Claims

This clause does not claim:

- that distillation is technically impossible;
- that a third-party oracle is protected against non-conformant actors;
- that metering replaces lawful authorization, consent, license, or terms compliance;
- that a positive extraction budget grants authority;
- that counted extraction is therefore clean extraction;
- that side channels outside the metered boundary are bounded;
- that `C_participant_sum` alone is sufficient for safety.

This is a self-discipline clause first. Its guarantee is internal: a conformant composition is not an unbounded, unwitnessed extraction fleet.

---

# 3. Core Principle

## 3.1 Canonical Rule

Composition may pool anchors. It MUST NOT pool extraction.

The aggregate extraction available to an A6 composition is bounded by the effective composition cap, not by informal cooperation, account proliferation, or unreviewed participant summation.

```text
Allowed:    bounded external-oracle use with source-class, meter, witness, and re-admission discipline.
Forbidden:  camouflaged aggregate extraction that reconstructs the oracle function or launders the result as native capability.
```

## 3.2 Hard Asymmetry

Capability obtained through:

```text
declared, scoped, authorized, bounded use of an oracle
```

has a different posture from capability obtained through:

```text
aggregate, coverage-shaped, reconstruction-directed, unmetered, or nonconformant extraction
```

The two MUST NOT be flattened.

Per-call acceptability does not automatically make the aggregate campaign acceptable. Direction, retention, coordination, and reconstruction purpose change the posture.

## 3.3 Seventh A6 Boundary Error

A6 Composition Layer prevents boundary errors where federation is mistaken for merged identity, shared infrastructure for shared authority, or cross-border composition for borderless control.

This clause names the seventh A6 boundary error:

> **Treating anchor composition as a license to pool capability extraction against a third-party oracle.**

A distillation fleet is not necessarily visible as one bad actor. It can emerge from many individually plausible participants whose pooled queries tile an oracle's input space. This is an A6 problem because the risk is created by composition.

---

# 4. Position in the Extraction Control Stack

| Control point | Question | Owner | BCEC role |
|---|---|---|---|
| Gate / recognition | Who may query the oracle? | Beacon | Not redefined; assumed upstream |
| Grounding | Is the actor / source / route live and reliable? | AGL | Not redefined; required before reliance |
| Egress / metering | How much capability flows out, from whom, toward what aggregate purpose? | BCEC | Defined here |
| Composition | Are anchors being pooled into an extraction fleet? | A6 | BCEC supplies the seventh boundary error and split trigger |
| Re-admission / laundering | May extracted capability return as clean EA? | Synthetic Laundering | Not redefined; handoff in §12 |
| Value posture | What kind of value is extracted capability? | EA Value Taxonomy | Mapped in §5.6 and §9 |
| Dispute / freeze | Who decides contested extraction? | ARL / Conflict Class | Not redefined; trigger in §10 |
| Witness | What evidence records the transition? | L4 Witness | Not replaced; packet extension in §11 |

BCEC MUST NOT redefine Beacon recognition classes, ARL standing, AGL grounding, L4 Witness core fields, EA value classes, Synthetic source-origin classes, or A6 composition semantics.

BCEC defines extraction discipline over them.

---

# 5. Extraction Source-Classes

Extraction source-classes are the egress mirror of Synthetic Laundering source-origin classes.

## 5.1 Marking Rule

Every retained extraction artifact MUST carry an extraction source-class.

Every external-oracle query under A6 composition SHOULD carry an extraction source-class.

Every query contributing to any of the following MUST carry an extraction source-class:

- EA;
- memory;
- vector-store entry;
- benchmark;
- model comparison;
- routing policy;
- fine-tuning;
- training data;
- prompt library;
- evaluation rule;
- capability claim;
- authority-bearing decision;
- model-behavior inference.

## 5.2 `EXTRACT_USE_BOUNDED`

Bounded, single-purpose use of oracle output within a declared scope.

Default conditions:

- no reconstruction intent;
- no adaptive coverage campaign;
- no retention beyond the immediate task, or only transient retention;
- authorization basis declared;
- response surface within oracle profile.

Default posture: lowest caution, but not native capability.

## 5.3 `EXTRACT_DERIVED_BOUNDED`

Bounded, declared derivation retained as an artifact.

Examples:

- summary;
- structured pattern;
- limited code snippet;
- localized explanation;
- task-specific plan;
- bounded comparison.

Required posture:

- explicit provenance;
- declared retention policy;
- no claim of native origin;
- no default authority parity;
- re-admission as synthetic-derived if retained.

## 5.4 `EXTRACT_MIXED`

Material combining oracle-derived capability with native, local, human, or other-sourced material.

Common and often legitimate, but the oracle-derived contribution MUST remain marked.

A mixed artifact MUST NOT become clean merely because the oracle contribution was rewritten, summarized, embedded, translated, or merged.

## 5.5 `EXTRACT_RECONSTRUCTIVE`

Aggregate extraction whose purpose, pattern, or effect approaches reconstruction of the oracle's function, distribution, policy surface, style, reasoning behavior, benchmark behavior, or reusable capability surface.

Signals include:

- systematic input-space tiling;
- repeated benchmark probing;
- differential prompt campaigns;
- style or policy imitation;
- behavior cloning;
- oracle-as-teacher training loops;
- high-volume retained outputs;
- coordinated participant querying;
- repeated queries whose value lies in coverage, not task completion.

Default posture: restricted. At A6 scale, this triggers threshold review and may trigger `A6-SPLIT`.

## 5.6 `EXTRACT_RESIDUE_NONCONFORMANT`

Extraction without sufficient source commitment or authorization grounding.

Examples:

- broken authorization chain;
- undisclosed proxying;
- fraudulent or farmed accounts;
- terms-bypassing route;
- geo-circumvention where prohibited by the authorization profile;
- unmetered delegated querying;
- hidden participant;
- unmodeled side channel used for retained capability.

Default posture: presumptively contaminated / quarantined.

Legacy alias:

```text
EXTRACT_RESIDUE_UNLAWFUL
```

from v0.1 is deprecated. It MUST be interpreted as `EXTRACT_RESIDUE_NONCONFORMANT` unless a competent legal process separately determines unlawfulness. BCEC is a technical conformance clause, not a court.

## 5.7 Value-Posture Mapping

| Extraction source-class | EA value posture on retention | Re-admission source-origin class |
|---|---|---|
| `EXTRACT_USE_BOUNDED` | Usually `OBSERVATIONAL_EA` or `OPERATIONAL_EA` if retained | `none` if not retained; otherwise `ORIGIN_SYNTHETIC_DERIVED` |
| `EXTRACT_DERIVED_BOUNDED` | `DERIVED_EA` | `ORIGIN_SYNTHETIC_DERIVED` |
| `EXTRACT_MIXED` | `DERIVED_EA` + native / other class | `ORIGIN_MIXED_SYNTHETIC` |
| `EXTRACT_RECONSTRUCTIVE` | `DERIVED_EA` → `CONTAMINATED_EA` → `QUARANTINED_EA` depending on threshold and authorization | `ORIGIN_SYNTHETIC_DERIVED` at best; `ORIGIN_SYNTHETIC_RESIDUE` if nonconformant |
| `EXTRACT_RESIDUE_NONCONFORMANT` | `CONTAMINATED_EA` / `QUARANTINED_EA` | `ORIGIN_SYNTHETIC_RESIDUE` |

---

# 6. Budget Model

BCEC has two compatible budget modes:

- **Formal Mode** — information-theoretic upper bound.
- **Operational Mode** — conservative extraction risk points.

An implementation MAY support Formal Mode. It MUST support at least Operational Mode unless a stricter external compliance regime replaces it.

## 6.1 Formal Mode: Information Bound

Let `F` be the oracle's input-output function or behavior distribution relevant to the extraction campaign.

Extracted capability is modeled as mutual information transferred from the oracle to the extracting party:

```text
extracted capability ≈ I(F ; responses observed by the party)
```

For each admitted query `q_i` under profile `profile_i`, let:

```text
b_extract,max(profile_i)
```

be the declared maximum informative contribution about `F` under that profile.

Then for participant `p` issuing admitted queries `Q_p`:

```text
I_p(F ; responses_p) ≤ Σ_{q_i ∈ Q_p} b_extract,max(profile_i)
```

For an A6 composition with participants `p ∈ P`:

```text
I_composition(F ; all_responses) ≤ Σ_{p ∈ P} Σ_{q_i ∈ Q_p} b_extract,max(profile_i)
```

This is the egress dual of the ARQ retained-commit chain-rule template.

## 6.2 Single-Unit Rule

All caps inside one `C_effective` computation MUST share one declared budget unit.

Allowed unit modes:

```text
risk_points
declared_information_bits
```

A `min(...)` over mixed units is invalid. Formal Mode and Operational Mode MAY both be recorded, but they MUST be computed as separate ledgers unless a witnessed conversion profile exists.

If both ledgers are active, an extraction is allowed only when every active ledger remains within its own effective cap. The system MUST NOT convert risk points into declared information bits, or declared information bits into risk points, by implication.

If any cap needed for `C_effective` is expressed in the wrong unit, the path fails closed or enters review before further extraction.

## 6.3 Calibration Rule

`b_extract,max` MUST be calibrated as a conservative upper bound under:

- adaptive querying;
- coordinated querying;
- coverage-shaped querying;
- retention and reuse;
- response-surface expansion;
- known side-channel declarations.

It MUST NOT be calibrated only on isolated benign use.

A ceiling calibrated only for ordinary single-task assistance is invalid for coordinated extraction.

## 6.4 Operational Mode: Risk Points

Where Formal Mode is unavailable, BCEC uses conservative extraction risk points.

The implementation MUST define a profile table. The following default table is the minimum recommended baseline. Query profile and retention are orthogonal axes: query profiles describe the kind of oracle interaction; retention is accounted for only by the retention multiplier in §6.5. A query profile name MUST NOT already include retention unless the profile explicitly says that no further retention multiplier applies.

| Event / query profile | Default risk points | Notes |
|---|---:|---|
| `factual_lookup` | 1 | Low-risk, task-bound lookup |
| `ordinary_transform` | 2 | Translation, formatting, local rewrite without model-behavior inference |
| `coding_help` | 5 | Retainable reusable capability; higher if systematic |
| `reasoning_scaffold` | 5 | Plans, decomposition, procedures retained for reuse |
| `evaluation_judgment` | 8 | External Judge output affecting local synthesis or routing |
| `benchmark_probe` | 20 | Benchmark-like model-behavior measurement |
| `coverage_probe` | 30 | Input-space tiling or systematic probing |
| `model_behavior_probe` | 40 | Policy, refusal, style, hidden preference, or distribution inference |
| `style_or_policy_imitation` | 50 | Behavior-cloning risk |
| `oracle_as_teacher_training_loop` | 100 | Presumptive reconstructive review |
| `unknown` | 50 | Conservative default until classified |
| `nonconformant_path` | immediate quarantine | Not just “expensive”; it is invalid pending review |

These numbers are not universal constants. They are a starting posture. Implementations MAY set stricter values, but SHOULD NOT weaken them without a witnessed calibration basis.

## 6.5 Retention Multiplier

A query's budget cost increases when the output is retained or reused.

Minimum multiplier:

| Retention policy | Multiplier |
|---|---:|
| `none` / transient only | 1× |
| `session_only` | 1.5× |
| `EA` | 2× |
| `vector_store` / memory | 3× |
| `evaluation` / routing policy | 4× |
| `training` / fine-tuning | 6× |
| `model_behavior_dataset` | 8× |
| `unknown` | 8× |

Operational consumed budget:

```text
B_consumed = Σ_i risk_points(query_i) × retention_multiplier_i × response_surface_multiplier_i
```

## 6.6 Response-Surface Multiplier

The larger the observed surface, the higher the extraction value.

Minimum multiplier:

| Response surface | Multiplier |
|---|---:|
| answer text only | 1× |
| text + code / file | 1.5× |
| structured outputs for reuse | 2× |
| embeddings | 3× |
| tool calls / routing behavior | 3× |
| logprobs / token probabilities | 5× |
| latency / refusal / policy traces retained for inference | 5× |
| multiple surfaces combined | highest applicable + 1× |

## 6.7 Participant Sum

For participant `p`:

```text
cost(query_i) ≡ risk_points(query_i)
  × retention_multiplier_i
  × response_surface_multiplier_i

B_p_consumed = Σ_i cost(query_i)
```

An implementation MUST NOT compute `B_p_consumed` from base risk points while ignoring retention or response-surface multipliers.

For the A6 composition:

```text
C_participant_sum = Σ_p B_p_allocated
B_composition_consumed = Σ_p B_p_consumed
```

The composition MUST NOT exceed its participant sum.

But this is not enough.

## 6.8 Effective Composition Cap

The enforceable cap is:

```text
C_effective = min(
  C_participant_sum,
  C_oracle_profile,
  C_license,
  C_reconstruct,
  C_sybil_adjusted
)
```

Rules:

- `B_composition_consumed` MUST NOT exceed `C_effective`.
- Every cap in this `min(...)` MUST be expressed in the same `budget_model.unit`.
- If `C_effective` cannot be computed, the extraction path fails closed.
- If any cap is unknown, it MUST be treated as `0` or routed to review, not ignored.
- A participant budget cannot expand the oracle-profile cap.
- A license cap cannot be bypassed through participant multiplication.
- A reconstruction cap cannot be bypassed by splitting queries across accounts, nodes, jurisdictions, or anchors.
- `C_sybil_adjusted` MUST be computed from principal equivalence classes as defined in §1.12.
- Participants with unknown or failed independence review MUST NOT increase the cap by numerical multiplication.

This is the central correction:

> **Counting every participant prevents hidden overrun. It does not by itself prevent lawful-looking mass reconstruction.**

### 6.8.1 Principal-Review Derivation of `C_sybil_adjusted`

Principal review produces an equivalence relation over participants:

```text
p ~ q  iff  p and q are controlled by the same extraction principal
```

The implementation does not need perfect social knowledge. It needs a conservative accounting state:

| Principal-review state | Accounting result |
|---|---|
| same principal grounded | collapse into one principal class |
| independence grounded | may remain separate principal classes |
| independence unknown | collapse into shared unresolved class or fail closed |
| review failed | collapse into shared unresolved class or fail closed |
| delegated querying | charge to the delegating principal unless independent authority is grounded |

For each principal class `g`, compute `C_principal_g` in the same budget unit as the campaign. Then sum those class caps to derive `C_sybil_adjusted`.

Principal classes are accounting objects, not identity claims. Passing principal review does not prove moral, legal, or institutional independence; it only permits a bounded metering treatment for this extraction campaign.

## 6.9 Warning Zones

Each oracle profile MUST define threshold zones.

Default zones:

| Consumption of `C_effective` | Status | Required action |
|---:|---|---|
| `0–60%` | normal | standard witness |
| `60–80%` | caution | increased witness detail; review query mix |
| `80–100%` | throttle | throttle or require explicit review |
| `>100%` | breach | freeze path; trigger `A6-SPLIT` if composition-scale |

Implementations MAY set stricter thresholds.

## 6.10 Reconstruction Threshold

Each oracle profile MUST define:

```text
T_reconstruct(profile)
```

The reconstruction cap is:

```text
C_reconstruct = T_reconstruct(profile)
```

A campaign enters reconstructive posture when either:

```text
B_composition_consumed ≥ T_reconstruct(profile)
```

or the query pattern independently indicates reconstruction risk.

Pattern-based reconstruction MAY trigger earlier than budget-based reconstruction.

Budget compliance is not a shield against obvious reconstructive intent.

## 6.11 Corrected No-Detection Property

The v0.1 proof shape remains useful but must be stated precisely.

Per-participant summation reduces dependence on detecting camouflaged collusion. If every controlled crossing is counted, the aggregate consumed budget can be bounded without proving that the participants are colluding.

However, this works only if:

- every query path is metered;
- participants are mapped to extraction principals;
- `b_extract,max` or risk points are conservatively calibrated;
- `C_effective` includes oracle-profile, license, reconstruction, and Sybil-adjusted caps;
- side channels are excluded or modeled separately.

Therefore:

> **BCEC does not need to detect every coalition to bound a conformant extraction campaign. But it does need valid caps, valid metering, and valid principal accounting.**

This statement has a hard limit. Principal accounting bounds concealed multiplicity: one controlling party split across many accounts, keys, nodes, or delegates. It does not bound genuine multiplicity by itself: many genuinely independent principals may still consume a large aggregate. In that case the binding limits are `C_oracle_profile` and `C_reconstruct`, not principal accounting alone.

## 6.12 What the Bound Does Not Prove

The bound does not prove:

- that distillation is impossible;
- that the oracle is protected from non-conformant outsiders;
- that a downstream model will or will not improve;
- that extracted capability is clean;
- that authorization exists;
- that side channels are covered;
- that a poorly calibrated cap is meaningful.

An overlarge cap makes the bound vacuous. An unmetered path voids the bound for the affected artifact.

---

# 7. Per-Participant and Principal Metering Rules

## BCEC-R1 — Participant Accounting

Every participant that queries an external oracle under A6 composition MUST have an extraction record containing:

- participant reference;
- anchor class A0–A5;
- extraction principal reference or principal-review status;
- oracle reference;
- query profile;
- response surface;
- retention policy;
- allocated budget;
- consumed budget;
- witness coverage.

## BCEC-R2 — Principal Accounting

Budgets MUST be issued to extraction principals, not merely to visible accounts.

Account splitting, key rotation, delegated querying, jurisdictional sharding, and operator shells MUST NOT create new extraction capacity unless independence is grounded.

## BCEC-R3 — No Pooling Beyond Effective Cap

A composition MUST NOT draw beyond `C_effective`.

One participant MUST NOT draw against another participant's budget without witnessed reallocation and principal review.

## BCEC-R4 — Hidden Participant

A querying participant without an extraction record is a hidden extraction path.

Hidden extraction paths fail closed until grounded.

## BCEC-R5 — Nested Composition

Nested A6 participation is high-risk because nesting can hide pooling.

Nested extraction budgets MUST be flattened to leaf participants and mapped to extraction principals before summation.

Unflattenable nesting fails closed.

## BCEC-R6 — Delegated Querying

Delegating queries to a third party does not remove BCEC obligations.

If a participant asks another party to query the oracle, the extraction must be counted against the controlling extraction principal unless a separate lawful and witnessed principal basis exists.

## BCEC-R7 — Cross-Jurisdiction Continuity

Jurisdictional movement does not reset extraction budget.

A query routed through another country, provider region, shell entity, or account family remains part of the same extraction campaign if controlled by the same principal or composition.

## BCEC-R8 — Side-Channel Declaration

Each extraction record MUST declare side-channel status:

```text
none_known | declared_separately | unmodeled_risk | side_channel_detected
```

`none_known` is an affirmative claim, not a default.

---

# 8. A6 Composition Rules

## BCEC-C1 — Composition Grants No Extraction Privilege

Connecting anchors under A6 does not create extraction capacity beyond the effective cap.

A6 may coordinate work. It does not manufacture oracle rights.

## BCEC-C2 — Oracle Access Is a Custodied Resource

The A6 Resource and Custodian Map MUST account for oracle access as a custodied resource.

Oracle accounts, API keys, hosted endpoints, Judge access, benchmark endpoints, and remote evaluators MUST NOT hide as generic infrastructure.

## BCEC-C3 — A6-SPLIT on Reconstructive Aggregate

When a composition crosses into `EXTRACT_RECONSTRUCTIVE` at aggregate scale, breaches `C_effective`, or cannot flatten nested extraction, the response is:

```text
A6-SPLIT
```

not ordinary:

```text
A6-EXIT
```

Reason: the breach may contaminate retained artifacts, budgets, source classes, and downstream memory. The affected compartment must be frozen and reviewed.

Unaffected compartments MAY continue within mapped scope under A6 rules.

## BCEC-C4 — No A6 Loophole Around A0–A5

A6 composition MUST NOT be used to convert weakly authorized, non-authorized, or non-grounded participants into a stronger extraction principal.

## BCEC-C5 — Anti-Cartel / Anti-Capture Continuity

SER-FED anti-capture discipline applies. A federation that coordinates extraction must remain able to prove bounded cooperation rather than cartelized distillation.

---

# 9. Authority and Value Ceiling Rules

## BCEC-A1 — No Native Parity

Extracted capability MUST NOT receive default authority parity with native, lived, or witness-bound capability.

It may be useful. It is not thereby origin-clean.

## BCEC-A2 — No Authority From Budget Alone

Budget compliance does not grant standing, authority, authorship, legal permission, or clean source posture.

A counted extraction can still be:

- synthetic;
- mixed;
- contaminated;
- nonconformant;
- unsuitable for authority-bearing use.

## BCEC-A3 — Reconstructive Ceiling

`EXTRACT_RECONSTRUCTIVE` material defaults to:

```text
CONTAMINATED_EA / QUARANTINED_EA
```

unless explicitly rehabilitated under Synthetic Laundering, ARL, and the relevant authorization basis.

## BCEC-A4 — No Sanitization by Packaging

Repackaging extracted capability into cleaner prose, code, schema, embedding, weight update, memory chunk, benchmark, or metadata does not erase its extraction source-class.

A polished artifact is not a clean artifact.

## BCEC-A5 — No Clean Re-entry by Compression

Compression can preserve capability while hiding provenance.

Therefore summaries, abstractions, embeddings, fine-tuning sets, and distilled prompts MUST preserve extraction source-class if derived from oracle material.

---

# 10. Trigger and Escalation

A breach is triggered by any of the following:

- `C_effective` exceeded;
- warning zone ignored;
- reconstruction threshold crossed;
- pattern-based reconstruction detected;
- hidden participant discovered;
- principal splitting unresolved;
- unflattenable nested A6 extraction;
- nonconformant source path;
- source-class / re-admission mismatch;
- side channel detected but unmodeled;
- witness packet missing or materially incomplete.

On breach:

1. Freeze the affected extraction path.
2. Trigger `A6-SPLIT` if the breach is composition-scale or artifact-contaminating.
3. Classify produced material as `CONTAMINATED_EA` or `QUARANTINED_EA` pending review.
4. Route the dispute via Conflict Class into ARL.
5. Record the transition through L4 Witness using the BCEC packet fields.
6. Block clean re-admission until Synthetic Laundering review resolves source posture.
7. Preserve hashes and retention records for audit.

Silence is not approval.

An unwitnessed extraction breach fails closed.

---

# 11. Witness Packet

The BCEC witness packet is a profile-level transport object. It does not replace L4 Witness or A6 witness schemas. It carries extraction-specific fields.

```json
{
  "schema_version": "bcec-0.2-final",
  "extraction_id": "string",
  "issued_at": "ISO-8601-UTC",
  "composition_ref": "a6:composition_id_or_null",
  "oracle_ref": {
    "oracle_id": "string",
    "oracle_profile_ref": "string",
    "provider_independent_claim": false,
    "authorization_basis": "licensed | tos_bound | consented | unauthorized | unknown | disputed",
    "license_ref": "string_or_null",
    "oracle_terms_ref": "string_or_null"
  },
  "purpose_declared": "string",
  "query_profile": "factual_lookup | ordinary_transform | coding_help | reasoning_scaffold | evaluation_judgment | benchmark_probe | coverage_probe | model_behavior_probe | style_or_policy_imitation | unknown",
  "retention_policy": "none | session_only | EA | vector_store | evaluation | routing_policy | training | fine_tuning | model_behavior_dataset | unknown",
  "response_surface": {
    "text": true,
    "code_or_file": false,
    "structured_output": false,
    "embeddings": false,
    "tool_calls": false,
    "logprobs": false,
    "latency_observed": false,
    "refusal_or_policy_trace": false,
    "hidden_reasoning_requested": false
  },
  "budget_model": {
    "unit": "risk_points | declared_information_bits",
    "formal_mode_available": false,
    "risk_profile_ref": "string",
    "b_extract_max_declared": 0,
    "single_unit_rule_satisfied": true,
    "mixed_unit_computation_used": false
  },
  "caps": {
    "participant_sum_cap": 0,
    "oracle_profile_cap": 0,
    "licensed_aggregate_cap": 0,
    "reconstruction_threshold_cap": 0,
    "sybil_adjusted_cap": 0,
    "effective_composition_cap": 0,
    "warning_threshold": 0,
    "hard_threshold": 0
  },
  "participants": [
    {
      "participant_ref": "string",
      "anchor_class": "A0 | A1 | A2 | A3 | A4 | A5",
      "extraction_principal_ref": "string_or_null",
      "principal_review": "not_required | passed | failed | unknown",
      "principal_class_ref": "string_or_null",
      "principal_class_cap": 0,
      "queries_admitted": 0,
      "budget_allocated": 0,
      "budget_consumed": 0,
      "witness_refs": ["wit:..."]
    }
  ],
  "composition_consumed_upper_bound": 0,
  "extraction_source_class": "EXTRACT_USE_BOUNDED | EXTRACT_DERIVED_BOUNDED | EXTRACT_MIXED | EXTRACT_RECONSTRUCTIVE | EXTRACT_RESIDUE_NONCONFORMANT",
  "value_posture": "OBSERVATIONAL_EA | OPERATIONAL_EA | DERIVED_EA | CONTAMINATED_EA | QUARANTINED_EA",
  "readmission_origin_class_on_retention": "ORIGIN_SYNTHETIC_DERIVED | ORIGIN_MIXED_SYNTHETIC | ORIGIN_SYNTHETIC_RESIDUE | none",
  "a6_split_triggered": false,
  "arl_refs": [],
  "side_channel_declaration": "none_known | declared_separately | unmodeled_risk | side_channel_detected",
  "sybil_review": "not_required | passed | failed | unknown",
  "retention_hashes": ["sha256:..."],
  "redaction_policy": "string_or_null",
  "algorithms": {
    "hash_alg": "sha256",
    "signature_alg": "string_or_null"
  },
  "payload_hash": "sha256:...",
  "signatures": ["sig:..."],
  "record_sha256": "PLACEHOLDER_SEALED_AT_INTEGRATION"
}
```

## 11.1 Packet Rules

The packet MUST:

- identify the oracle and oracle profile;
- identify authorization basis;
- declare purpose;
- declare query profile;
- declare retention policy;
- declare response surface;
- enumerate participants;
- map participants to extraction principals or record failed / unknown review;
- state all caps used to compute `C_effective`;
- state consumed upper bound;
- mark extraction source-class;
- mark value posture;
- mark re-admission origin-class if retained;
- declare side-channel status;
- preserve hashes for retained artifacts;
- leave `record_sha256` unsealed until independent witness pass.

If a required field is unknown, the packet MUST say `unknown`. It MUST NOT silently omit the field.

---

# 12. Re-Admission Binding

Any retained capability artifact produced by extraction MUST carry a source-origin class under Synthetic Laundering.

Mapping:

```text
EXTRACT_USE_BOUNDED          -> none if not retained; ORIGIN_SYNTHETIC_DERIVED if retained
EXTRACT_DERIVED_BOUNDED      -> ORIGIN_SYNTHETIC_DERIVED
EXTRACT_MIXED                -> ORIGIN_MIXED_SYNTHETIC
EXTRACT_RECONSTRUCTIVE       -> ORIGIN_SYNTHETIC_DERIVED at best; ORIGIN_SYNTHETIC_RESIDUE if nonconformant
EXTRACT_RESIDUE_NONCONFORMANT -> ORIGIN_SYNTHETIC_RESIDUE
```

The egress source-class and the re-admission origin-class MUST agree.

A disagreement is a laundering signal and is quarantined as:

```text
echo_suspect / contamination
```

A retained artifact without source-origin class cannot enter clean corpus circulation.

---

# 13. Anti-Echo Discipline

No extraction budget compliance SHALL be cited as proof that produced capability is clean, native, or authority-bearing.

No qualitative source-class SHALL silently substitute for the quantitative bound.

No quantitative bound SHALL silently substitute for source-class.

No polished restatement SHALL erase provenance.

Any circular pattern:

```text
BCEC -> A6 -> BCEC
BCEC -> Synthetic Laundering -> BCEC
BCEC -> Judge -> BCEC
```

MUST preserve an independent challenge point and MUST NOT collapse into self-confirmation.

A clean-looking artifact does not gain posture by eloquence, compression, or repetition.

---

# 14. Interpretation Discipline and Auto-Rollback

## 14.1 Slot A — Structural Reading

Slot A controls:

- definitions;
- source-class marking;
- participant and principal accounting;
- cap computation;
- witness requirements;
- re-admission handoff;
- A6-SPLIT trigger;
- forbidden claims.

Slot A MUST be sufficient to reject a category error, budget breach, laundering attempt, or hidden extraction path.

## 14.2 Slot B — Narrative Reading

Slot B contains explanatory analogies:

- extraction fleet;
- donor meter;
- contamination flag;
- trust premium;
- bounded channel.

Slot B is subordinate to Slot A.

## 14.3 Auto-Rollback

If a Slot B reading implies a stronger guarantee than Slot A grants, interpretation MUST auto-rollback to Slot A.

Examples of invalid over-reading:

```text
metered, therefore lawful
metered, therefore clean
counted, therefore non-reconstructive
summed, therefore safe
bounded, therefore authority-bearing
```

Over-claim arrives wearing a clean suit. BCEC does not let it through the gate.

---

# 15. Operational Implementation Sketch

A minimal conformant implementation SHOULD implement the following pipeline:

```text
external_oracle_request
  -> identify participant
  -> map extraction principal
  -> identify oracle profile
  -> classify query profile
  -> declare purpose
  -> declare response surface
  -> declare retention policy
  -> compute query cost
  -> check participant budget
  -> compute C_effective
  -> check warning / hard threshold
  -> write pre-call witness stub
  -> issue admitted query
  -> hash response / retained artifact
  -> update consumed budget
  -> mark extraction source-class
  -> mark value posture
  -> hand off retained artifact to Synthetic Laundering
  -> write sealed witness transition
```

Minimum UI exposure for a retained artifact:

```text
External oracle material: yes
Extraction source-class: EXTRACT_DERIVED_BOUNDED / EXTRACT_MIXED / ...
Retention policy: EA / vector_store / training / ...
Re-admission class: ORIGIN_SYNTHETIC_DERIVED / ORIGIN_MIXED_SYNTHETIC / ...
Authority parity: no by default
Budget status: normal / caution / throttle / breach
Witness: wit:...
```

For an Esther-like local architecture, this means:

- LMStudio / local LLM outputs remain local substrate unless influenced by oracle material;
- cloud Judge outputs are external-oracle material unless the Judge is inside the substrate boundary;
- vector DB entries must preserve extraction source-class;
- P2P synchronization must carry provenance tags, not just embeddings;
- autonomous folder processing must mark oracle-derived chunks before they enter memory.

---

# 16. Conformance Expectations

A conformant implementation MUST be able to answer, for any retained external-oracle extraction:

1. Which oracle was queried?
2. Under what authorization basis?
3. Which participant issued or routed the query?
4. Which extraction principal controlled the participant?
5. Which anchor class applied?
6. What was the declared purpose?
7. What query profile applied?
8. What response surface was observed?
9. What retention policy applied?
10. What was the query cost?
11. What participant budget was consumed?
12. What was `C_effective`?
13. Which cap limited `C_effective`?
14. Was any warning threshold crossed?
15. Was `A6-SPLIT` triggered?
16. What extraction source-class was assigned?
17. What EA value posture was assigned?
18. What re-admission origin-class was assigned?
19. What side-channel status was declared?
20. Which witness record seals the transition?

If these cannot be answered, the extraction is ungrounded and fails closed.

---

# 17. Minimal Hard Rules

1. Composition MUST NOT pool extraction beyond `C_effective`.
2. `C_effective` MUST be computed as the minimum of participant sum, oracle-profile cap, declared license/authorization cap, reconstruction cap, and derived Sybil-adjusted cap.
3. `C_sybil_adjusted` MUST be derived from principal-review equivalence classes; it MUST NOT remain a placeholder label.
4. Every cap in one `C_effective` computation MUST use one budget unit. Mixed-unit `min(...)` computations are invalid.
5. Participant budgets MUST be mapped to extraction principals.
6. Numerically distinct accounts, keys, nodes, or jurisdictions MUST NOT automatically create independent extraction capacity.
7. Every retained extraction artifact MUST carry extraction source-class.
8. Any query contributing to EA, memory, evaluation, routing, training, fine-tuning, benchmark, model-behavior inference, or authority-bearing use MUST carry extraction source-class.
9. `EXTRACT_RESIDUE_NONCONFORMANT` is presumptively contaminated and maps to `ORIGIN_SYNTHETIC_RESIDUE` on re-admission.
10. Extracted capability MUST NOT receive default parity with native, lived, or witness-bound capability.
11. Reconstructive aggregate extraction MUST trigger `A6-SPLIT`, not ordinary `A6-EXIT`.
12. Nested extraction budgets MUST be flattened to leaf participants and mapped to principals.
13. Egress source-class and re-admission origin-class MUST agree.
14. Disagreement between egress and re-admission classes MUST be quarantined.
15. Side channels MUST be declared and modeled separately or the bound is void for the affected artifact.
16. Budget compliance MUST NOT be cited as proof of cleanliness, authority, legality, or non-reconstruction by itself.
17. Missing witness data fails closed.

---

# 18. Failure Modes Prevented

| Failure mode | Prevented by |
|---|---|
| Composition pooling | `C_effective`, participant / principal metering |
| Lawful-looking mass reconstruction | oracle-profile, license, reconstruction, and Sybil-adjusted caps |
| Nested-A6 concealment | leaf flattening and fail-closed nesting |
| Account farming / Sybil expansion | extraction-principal accounting |
| Jurisdictional budget reset | cross-jurisdiction continuity rule |
| Egress laundering | source-class and re-admission binding |
| Authority inflation | no-native-parity and no-authority-from-budget rules |
| Detection dependence | metering at controlled boundary, not coalition detection |
| Compression laundering | no-clean-reentry-by-compression rule |
| Side-channel invisibility | side-channel declaration and void-bound rule |

---

# 19. Bridges

## 19.1 Explicit Bridge — A6 / Synthetic Laundering / EA Value / ARQ

A6 Composition Layer defines the anchor-composition that can become an extraction fleet. Synthetic Laundering blocks re-admission of synthetic-origin capability as clean. EA Value Class Taxonomy gives the value posture of extracted capability. ARQ Classical Boundedness supplies the chain-rule proof template.

BCEC binds these into an egress discipline:

```text
A6 composition creates the aggregate risk.
BCEC meters and caps the extraction boundary.
Synthetic Laundering blocks clean re-entry.
EA Value prevents authority inflation.
ARQ supplies the bounded-channel proof shape.
```

## 19.2 Hidden Bridge #1 — Ashby / Requisite Variety

Ashby's law says a regulator must match the variety of what it regulates.

A camouflaged coalition of extractors has high variety. Trying to detect every collusive pattern forces the regulator into a variety race it usually loses.

BCEC relocates regulation from the camouflage surface to the controlled boundary:

```text
count controlled crossings;
map participants to principals;
sum consumption;
cap the aggregate;
quarantine unmetered paths.
```

This satisfies requisite variety where it is cheap: at the boundary. It avoids chasing every possible coalition shape after the fact.

## 19.3 Hidden Bridge #2 — Information Theory / Channel Discipline

Distillation is capability transfer about an oracle function `F`.

The formal model describes this as:

```text
I(F ; responses)
```

The chain rule bounds accumulated information by the sum of per-query upper bounds. Operational risk points are the engineering fallback when the formal quantity cannot be measured directly.

Compression, summarization, and embeddings can preserve capability while hiding source. Therefore BCEC keeps two channels separate:

```text
quantitative channel: how much extraction occurred;
qualitative channel: what source-class the artifact carries.
```

Neither channel may erase the other.

---

# 20. Earth Paragraph

Think of a blood bank and a load-bearing repair shop combined.

In the blood bank, you do not try to prove that twenty-five thousand phlebotomists are not secretly one consortium. That detection problem is ugly. You meter each donor, log each draw, cap the aggregate, and mark provenance. Blood drawn without consent does not become clean because the vial is sterile and the label is pretty.

In the repair shop, a refurbished part may be useful. It may even be excellent. But it is not factory-new, and it does not go into a critical load-bearing slot without a repair passport, load rating, and inspection record.

Extracted capability is the same kind of object. It can be useful. It can be lawful. It can be worth retaining. But it is not native merely because it was rewritten well, compressed into an embedding, or passed through a local model.

BCEC is the donor meter, repair passport, load rating, and contamination flag for capability extraction.

---

# 21. Known Limits and Calibration Items

## 21.1 `b_extract,max` Calibration

The principal empirical knob remains calibration.

How much informative capability a response transfers depends on:

- oracle type;
- query profile;
- response surface;
- retention policy;
- adaptive context;
- whether outputs are reused for training, evaluation, routing, or memory.

Until empirical calibration exists, Operational Mode risk points are the safer default.

## 21.2 Reconstruction Thresholds

`T_reconstruct(profile)` requires profile-specific calibration.

The threshold should consider:

- volume;
- coverage shape;
- benchmark coverage;
- policy / style imitation;
- repeated differential probes;
- retention density;
- downstream training use.

Budget threshold and pattern threshold are independent. Either can trigger review.

## 21.3 Side-Channel Scope

BCEC does not automatically bound scraped corpora, leaked weights, cached outputs, screenshots, manual copying, or unmetered logs.

If such material affects a retained artifact, it must be declared or the bound is void for that artifact.

## 21.4 External-Adversary and Populous-Principal Horizon

This clause binds systems that execute this corpus. It does not stop non-conformant external actors.

Principal accounting bounds concealed multiplicity, not genuine multiplicity. If many principals are genuinely independent and each passes principal review, then `C_sybil_adjusted` may approach their true aggregate. In that case principal accounting is no longer the binding control. The binding controls are `C_oracle_profile`, `C_reconstruct`, and any declared provider-side aggregate access cap.

This is not a defect in the Sybil rule; it is the horizon of conformant-side accounting. A conformant system can refuse to launder concealed multiplicity. It cannot, by its own ledger alone, prove that a whole population of genuinely independent actors will not collectively approximate an oracle.

Its external value is therefore a trust premium: a provider can rationally grant stronger access to a composition that can prove bounded, witnessed, non-reconstructive extraction within declared oracle-profile and reconstruction caps.

## 21.5 A5 / A6 Operator-Modifier Question

Inherited from A6: whether A5 civic / institutional anchors behave as pure object anchors or operator-like modifiers can affect extraction-principal accounting.

This clause does not resolve that question. It requires conservative accounting until resolved.

## 21.6 Unit Conversion

Formal information-bit mode and Operational risk-point mode are both admissible, but they are not interchangeable. A future calibration profile MAY define a witnessed conversion between them. Until then, conversion is prohibited inside `C_effective`.

---

# 22. Register Handoff

| Target layer | What BCEC registers / exports | What BCEC MUST NOT assert |
|---|---|---|
| A6 Composition Layer | Seventh boundary error; `A6-SPLIT` trigger; oracle access as custodied resource; leaf flattening requirement | Redefinition of A6 composition or `EXIT` / `SPLIT` semantics |
| Synthetic Laundering | Egress-to-re-admission source-class mapping | Redefinition of source-origin classes |
| EA Value Taxonomy | Value-posture mapping of extracted capability | New value classes |
| ARL / Conflict Class | Extraction breach as standing-bearing dispute / quarantine / appeal case | Parallel court or evidence doctrine |
| L4 Witness | BCEC witness packet fields | Replacement of witness core fields |
| Beacon | No direct export; gate remains upstream | Recognition-class changes |
| AGL | Need for source / actor / route grounding before reliance | Replacement of grounding doctrine |
| SER-FED | Anti-cartel / anti-capture continuity for extraction federations | Ban on federation |

---

# 23. v0.2.1 Correction Record

This version applies the b-layer `PASS_WITH_LIMITS` review corrections without changing the core v0.2 thesis.

| Review item | Closure in v0.2.1 |
|---|---|
| D1 — `C_sybil_adjusted` not derived | Added principal-review equivalence-class derivation and fail-closed handling for missing principal caps. |
| D2 — populous-principal horizon not stated | Added explicit limit: principal accounting bounds concealed multiplicity, not genuine multiplicity. |
| D3 — retention double-encoded | Query profiles and retention multipliers are now explicitly orthogonal; `retained_summary` removed from baseline query-profile table. |
| D4 — `cost(query_i)` ambiguity | `cost(query_i)` is now defined as base risk points times retention and response-surface multipliers. |
| D5 — mixed-unit `min(...)` | Added single-unit rule; mixed Formal/Operational cap computations are invalid. |
| D6 — `C_license` ambiguity | Clarified that `C_license` is a declared metering ceiling, not legal adjudication. |

The correction remains append-first. It does not seal the witness record, approve integration, or write memory.

---

# 24. Closing Statement

A composition becomes stronger, not weaker, when its extraction boundary is metered and its source-classes are visible.

A federation that can prove it does not pool queries into reconstruction, cannot inflate participant counts into extraction capacity, and cannot launder what it extracts is more trustworthy than one that merely promises restraint.

Extraction is not forbidden.

Unbounded, camouflaged, reconstructive, or laundering extraction is forbidden.

Therefore:

```text
meter the participant;
map the principal;
cap the composition;
respect the oracle profile;
stop before reconstruction;
witness the transition;
mark the source-class;
block clean laundering on re-entry.
```

That is the extraction discipline of BCEC v0.2-final.

---

**Advisory integration note:** final textual clause only. No self-approval, no memory write, no integration authority. Sealing and conformance require a separate checker / witness pass.
