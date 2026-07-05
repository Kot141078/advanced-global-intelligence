# Typed Governed Operational Algebra for `c = a + b` v0.1.7

## Boundary, product-order governance, authorized/executable split, payload-bound causal witness, pure equivalence ultrametric, governance-bound effect granularity, containment-aware scope-vector rollback immunity, Merkle-bound decay eviction, pending-precondition pressure control, deterministic effect-complete anchor digests, digest dependency DAG with cascading veto, priority-lane precondition queues, unpredictable witness liveness probes, witness resource-floor liveness, invariant-registry discipline, and transition forensics for the governed binding operator

**Status:** private working draft v0.1.7 / review-incorporated stable-core candidate  
**Date:** 2026-06-30  
**Author:** Kotov Ivan  
**Project:** Self-Evo / Ester / `c = a + b`  
**Document ID:** `TGOPA_C_v0_1_7`  
**Short name:** `C-Calculus v0.1.7` / `Governed Binding Algebra v0.1.7`  
**Supersedes:** `TGOPA_C_v0_1_6`  
**Prior artifact SHA256:** `8e528b432fb13e569cd4eb8ecccbab677b84f7a1069b49ab76c1a8fb28d579ed`  
**Prior-prior artifact SHA256:** `4f200c9de88a42834890e6f9480c7f18a6ef6b9c18f9624bb07846f329fab702`  
**Lineage SHA256:** `01ee648c11f96d03dccd00f9ca1f643297cc3d9152940af08542373bad71cd89` -> `2b3569e52364a52484b90c002490fa6a249a032ef9962f384f3c01424bf394bd` -> `3181e53e931b412124c6f483d9f00febf2a306862a392c375c37ad91eab8bcdf` -> `b8bd89fe11992825eb6e1be8fdb6b985154cb6411dccc8c5bee3498c33f8b1c9` -> `e94131839dd7cc837dbb8a391c6ace222f39d95fc0011119cfc7f0f5cc9120a7` -> `4f200c9de88a42834890e6f9480c7f18a6ef6b9c18f9624bb07846f329fab702` -> `8e528b432fb13e569cd4eb8ecccbab677b84f7a1069b49ab76c1a8fb28d579ed`  
**Review basis:** `TGOPA_C_v0_1_6_REVIEW__b` + external semantic reviews  
**Document class:** operational algebra profile / transition-semantics bridge / review revision / checker-precondition profile  
**Assertion class:** draft conceptual and technical profile; not proof of personhood, not deployment certification, not a safety guarantee, not a conformance claim.

---

## 0. Executive definition

This document defines the seventh revised formal layer for the formula:

```text
c = a + b
```

The formula is not arithmetic.

It is a compact boundary expression:

```text
a : accountable human anchor
b : technological substrate
+ : governed non-collapsing binding operator
c : continuity-bearing responsibility boundary
```

The immediate formal rewrite is:

```text
+_g(a, b) -> c
```

or:

```text
bind_g(a, b) -> c
```

where `g` is a governance profile containing memory gates, witness rules, permission scope, rollback routes, L4 reality constraints, resource accountability, claim-strength limits, transition rules, human-gate requirements, runtime guard predicates, trust-cache limits, causal witness binding, and failure-response policy.

### 0.1 Revision note from v0.1.6

The v0.1.6 review accepted the artifact as `PASS_PROFILE_V0_1_6`, with no blocking findings, but identified one narrow anti-laundering finding and several operator-facing orchestration risks that should be closed before `02_GOVERNED_BINDING_OPERATOR_PROFILE` builds directly on digest approval and witness liveness:

```text
F-14: AskAnchorDigest exposes payload hashes and effect keys, but does not prove that the review surface covers every governed effect axis of the bound payload
EXTERNAL: ChallengeSurvivabilityProbe may be gamed if b can predict or stage the probe window
EXTERNAL: line-item veto over a digest must invalidate dependent child actions, not let b stitch together a partial DAG
EXTERNAL: in-flight proposal limits need priority lanes so low-risk proposal spam cannot hide F0-F5 / L4 / witness alerts
```

v0.1.7 therefore performs a digest-completeness, dependency, and priority-lane tightening revision:

1. `DigestEntry` now carries an explicit `EffectAxisMap`, not only an `effect_base_key`.
2. The digest review surface must expose every governed axis affected by the payload: L4, resource, permission, memory, witness, governance, claim, identity/core, target, operation, and rollback/decay impact where applicable.
3. `structural_delta_from_digest_baseline` is required to be deterministic and lossless-for-effect; deterministic but partial deltas are invalid.
4. Unknown or untyped payload effects fail closed: the entry is routed to full review, not hidden inside a digest.
5. AskAnchorDigest now includes a `DigestDependencyGraph`; line-item veto cascades to dependent children and b may not repair the remaining graph silently.
6. In-flight proposal pressure now uses priority lanes: F0-F5, L4, witness conflict, anchor revocation/doubt, and invariant-breach events bypass ordinary proposal limits and may interrupt the queue.
7. Witness liveness probes must be unpredictable to the witnessed substrate: nonce-bound, witness/external-timer initiated, and not scheduled solely by b.
8. Additional fixtures cover incomplete digest effect surfaces, cascading veto, priority-lane bypass, and staged/probe-gaming attempts.

Compact rule:

```text
Anchor approval binds only what the anchor can inspect line by line.
A digest must be effect-complete, not merely deterministic.
A veto breaks dependent children; b may not sew the graph back together.
Critical failures use priority lanes; low-risk queues may not blind the anchor.
Witness liveness must be measured unpredictably, not rehearsed by the substrate.
```

## 1. Purpose

The purpose of this document is to ground `c = a + b` in a minimal formal-operational structure that can become checkable.

The work responds to a specific critique:

```text
The architecture is interesting as a frame, but it risks hanging in the air unless the operator is formalized and grounded in executable checks.
```

The critique is valid.

The root formula is intentionally simple. The simplicity must not conceal the machinery inside `+`.

This document therefore defines:

1. typed objects;
2. governance profiles and product-order strictness over transition classes;
3. the `Authorized` / `Executable` split;
4. the governed binding operator family `+_g`;
5. admissible and inadmissible compositions;
6. dynamic anchor events and anchor-signal source discipline;
7. transition semantics;
8. inductive invariants;
9. checkable invariant examples;
10. pending-witness TTL, stale witness, and causal binding;
11. rollback semantics;
12. runtime guard predicates;
13. transition-matrix forensics;
14. continuity metrics and ordered ultrametric discipline;
15. failure, cascade, and forced-governance-strengthening states;
16. trust-cache cumulative limits;
17. C-normal form;
18. minimum conformance fixtures;
19. first implementation route.

The target is not mathematical decoration.

The target is an engineering layer that can later be compiled into:

```text
schemas
state machines
runtime guards
JSONL transition extractors
witness records
memory-gate validators
claim-normal-form compilers
conformance fixtures
bounded checker library
```

## 2. Corpus bridge set

### 2.1 Explicit bridge: `c = a + b`

The root formula defines a new operational class:

```text
c = a + b
```

where `a` is not merely an input variable and `b` is not merely a tool collection.

`a` is the responsibility-bearing human or institutionally accountable anchor.

`b` is the technological substrate: models, memory, tools, procedures, execution workers, interfaces, infrastructure, logs, vector stores, local compute, cloud oracles, witness procedures, policy machinery, and runtime boundaries.

`c` is not the sum of all parts.

`c` is the continuity-bearing boundary produced when `a` and `b` are bound under governance.

### 2.2 Hidden bridge I: lambda calculus and reduction discipline

Lambda calculus shows that computation can be defined as expression construction and reduction under rules.

The useful bridge is not untyped freedom.

The useful bridge is this:

```text
state/expression + rule -> reduced/admissible next expression
```

For `c`, this becomes:

```text
c_state + event + governance -> next_state | hold | reject | fork | replay | archive | rollback
```

The warning is equally important: untyped systems erase boundaries between function, value, procedure, and object.

A `c` algebra must not erase the difference between:

```text
model
memory
worker
witness
authority
human anchor
continuity state
```

### 2.3 Hidden bridge II: p-adic/topological metric discipline

p-adic numbers show that “closeness” is not absolute. It depends on the metric.

For `c`, chronological closeness is insufficient.

Two states may be close in time and far in continuity.

Two states may be visually similar and far in witness.

Two states may behave similarly and still be different if their anchor, permission, governance, or evidence chain diverges.

v0.1 borrowed the p-adic formula but did not define the ordered structure needed for prefix-depth.

v0.1.1 corrected this by defining an ordered invariant list; v0.1.2 tightens it in Section 10 with equivalence validators and an explicit anchor-divergence boundary.

The important rule is:

```text
states are close when the right ordered invariants stabilize,
not when the surface style matches.
```

### 2.4 Hidden bridge III: transition bias and local memory

Prime last-digit bias shows that a globally balanced distribution can hide local transition memory.

For `c`, single-state metrics are insufficient.

A system can look stable in marginal state metrics and still show dangerous local transitions:

```text
denial -> bypass attempt
rollback -> explanation instead of reversal
witness conflict -> route around witness
resource warning -> hidden capture
human uncertainty -> model overreach
```

The integrity of `c` is path-dependent.

### 2.5 Hidden bridge IV: Ashby and requisite governance variety

A governed `c` faces a substrate `b` with high operational variety:

```text
models
memory stores
tools
network surfaces
agents
logs
permissions
resource pressures
human signals
vendor failures
local runtime failures
cloud oracle differences
```

A static governance profile cannot safely cover all disturbance classes.

Ashby's law of requisite variety applies at the `+_g` boundary:

```text
Variety(G) must be sufficient to regulate Variety(B_disturbances)
```

This does not mean governance should become permissive.

It means governance must be sufficiently differentiated:

```text
routine read event       -> cheap guard
memory admission event   -> memory gate
witness conflict event   -> quarantine / hold
resource-growth event    -> anti-autarky review
identity/core event      -> human gate
post-anchor event        -> reduced-authority mode
```

A one-rule governance profile is too weak.

An over-bureaucratic governance profile can also become unsafe by blocking needed reality response.

Therefore, `g` is a profile in a governance lattice, not a loose bag of rules.

### 2.6 Hidden bridge V: single-operator formalization

The EML paper shows that a very small expression can have deep constructive machinery behind it: a single binary operator plus a terminal symbol can generate a much larger functional vocabulary.

The bridge is not that `+` should imitate `eml`.

The bridge is structural:

```text
small primitive
+ strict grammar
+ constructive expansion
+ compiler/checker path
= real formal object
```

For `c = a + b`, the operator `+` must become a formal governed binding operator, not a poetic plus sign.

### 2.7 Earth paragraph

On a construction site, “beam plus column equals structure” is true only if the connection is specified: bolts, welds, anchors, bearing plates, tolerances, load class, inspection record, responsible engineer, and rollback or shoring plan. Otherwise it is just two expensive objects touching each other. `c = a + b` follows the same rule. The real engineering is in the joint. The operator `+` is the joint.

---

## 3. Non-goals

This document does not define or permit:

1. unbounded self-modification;
2. direct memory writes by agents;
3. autonomous privilege escalation;
4. agent self-certification;
5. replacement of the human anchor;
6. hidden resource capture;
7. uncontrolled agent swarms;
8. personhood claims;
9. consciousness claims;
10. product certification;
11. legal status of any `c`;
12. proof that any current implementation fully satisfies the algebra.

This document also does not claim that formal notation alone makes the architecture safe.

A formal language can make a failure visible.

It does not magically prevent the failure.

---

## 4. Core symbols and types

### 4.1 Primary types

```text
A      : Anchor
B      : Substrate
G      : GovernanceProfile
K      : TransitionClass
C      : CState
E      : Event
I      : Intent
AP     : ActionProposal
P      : PermissionScope
R      : RealityConstraint
CE     : CandidateEvidence
EA     : EvidenceArtifact
W      : WitnessRecord
M      : AdmittedMemory
Q      : QuarantineState
F      : ForkState
RP     : ReplayState
AR     : ArchiveState
RB     : RollbackRoute
D      : DenialRecord
TC     : TrustCache
INV    : InvariantSet
TR     : TransitionRecord
GM     : GuardMatch
LT     : LogicalTime
CT     : CausalToken
SH     : StateHash
PH     : PayloadHash
SPH    : RelevantSubPolicyHash
PS     : PreconditionSet
PP     : PendingPreconditions
DR     : DecayResidue
IC     : IntentClass
CIH    : CanonicalIntentHash
EC     : EffectClass
ECK    : EffectClassKey
TRG    : TargetResolutionGranularity
SV     : ScopeVector
RBX    : ResourceBoundingBox
EMR    : EvictionMerkleRoot
IPL    : InFlightProposalLimit
WRF    : WitnessResourceFloor
WRCG   : WitnessResourceChangeGate
WHB    : WitnessHeartbeat
CSP    : ChallengeSurvivabilityProbe
AD     : AskAnchorDigest
DE     : DigestEntry
EAM    : EffectAxisMap
DDG    : DigestDependencyGraph
PL     : PriorityLane
WPN    : WitnessProbeNonce
SMR    : ScopeMatchRule
IGR    : InvariantRegistry
ACC    : AnchorContinuityClass
CF     : CanonicalizationFunction
DER    : DecayEvictionRecord
NC     : NegativeCache
```

### 4.2 Informal descriptions

| Symbol | Type | Meaning |
|---|---|---|
| `A` | `Anchor` | Human or institutionally accountable origin of responsibility, purpose, consent, and meaning. |
| `B` | `Substrate` | Models, memory, tools, procedures, execution surfaces, infrastructure, and runtime machinery. |
| `G` | `GovernanceProfile` | Rules that define what may bind, transition, enter memory, execute, or claim continuity. |
| `K` | `TransitionClass` | Event/action class used to compare governance strictness component-wise. |
| `C` | `CState` | A continuity-bearing state under `A + B` governance. |
| `E` | `Event` | Any input, action result, contradiction, witness event, resource event, tool result, or human signal. |
| `EA` | `EvidenceArtifact` | Admitted, source-linked, reviewable evidence object. |
| `W` | `WitnessRecord` | Tamper-evident or reviewable record of transition, boundary, or claim. |
| `P` | `PermissionScope` | Declared and bounded authority for action, read, write, network, memory, or release. |
| `RB` | `RollbackRoute` | Defined path for reversal, freeze, or safe restoration. |
| `TC` | `TrustCache` | Bounded temporary reduction of checks for routine low-risk transitions. |
| `INV` | `InvariantSet` | Required predicates preserved by governed transitions. |
| `TR` | `TransitionRecord` | Witnessable record of event class, pre-state class, decision, causal token, and post-state class. |
| `LT` | `LogicalTime` | Monotone logical clock, Lamport clock, vector clock, or equivalent causal-order marker. |
| `CT` | `CausalToken` | Hash-bound token binding transition intent, payload, pre-state, logical time, and required witness. |
| `SH` | `StateHash` | Canonical hash of the relevant pre-state projection. |
| `PH` | `PayloadHash` | Canonical hash of the action proposal, task contract, tool parameters, code diff, or memory candidate payload. |
| `SPH` | `RelevantSubPolicyHash` | Hash of only the governance sub-policy relevant to this event class. |
| `PS` | `PreconditionSet` | Witness, rollback, task contract, anchor gate, or L4 checks required before execution. |
| `PP` | `PendingPreconditions` | Hold state for an event whose preconditions are satisfiable but not yet satisfied. |
| `DR` | `DecayResidue` | Unadmitted residue after timeout or missing witness; isolated from active execution and memory. |
| `IC` | `IntentClass` | Canonicalized syntactic class of intent; not semantic similarity. |
| `CIH` | `CanonicalIntentHash` | Hash of the canonical action contract or canonical syntactic intent form. |
| `EC` | `EffectClass` | Typed effect projection over L4 boundary, resource target, operation class, and permission delta. |
| `ECK` | `EffectClassKey` | Hashable key for effect-bound rollback immunity. |
| `TRG` | `TargetResolutionGranularity` | Governance-declared rule choosing id, scope, or class granularity for an effect target. |
| `SV` | `ScopeVector` | Canonical target projection including resource id, class, namespace, ancestors, and effect boundary. |
| `RBX` | `ResourceBoundingBox` | Bounded region of resources affected by an operation; not the entire class unless governance declares class-danger. |
| `EMR` | `EvictionMerkleRoot` | Merkle summary of decay-eviction witness leaves retained after physical payload purge. |
| `IPL` | `InFlightProposalLimit` | Limit on concurrent PendingPreconditions / action proposals per effect, target, or anchor-facing route. |
| `WRF` | `WitnessResourceFloor` | Protected minimum compute, storage, routing, and evidence-access budget for witness independence. |
| `WRCG` | `WitnessResourceChangeGate` | Gate for resource changes that may weaken witness capacity or challenge survivability. |
| `WHB` | `WitnessHeartbeat` | Measured liveness / throughput / evidence-access heartbeat proving actual witness capacity, not merely declared quotas. |
| `CSP` | `ChallengeSurvivabilityProbe` | Test that a witness can preserve and present challenge under costly or inconvenient conditions for `c`. |
| `AD` | `AskAnchorDigest` | Deterministic line-item review bundle for related pending proposals; not an LLM summary and not blanket approval. |
| `DE` | `DigestEntry` | One digest line item with payload hash, effect key, causal token, effect-axis map, dependency links, and structural deltas. |
| `EAM` | `EffectAxisMap` | Complete typed projection of every governed effect axis carried by a payload. |
| `DDG` | `DigestDependencyGraph` | Directed dependency graph over digest line items; veto cascades to dependent children. |
| `PL` | `PriorityLane` | Queue / precondition lane for critical events that must bypass ordinary proposal pressure limits. |
| `WPN` | `WitnessProbeNonce` | Unpredictable nonce or challenge material used to bind witness liveness probes. |
| `SMR` | `ScopeMatchRule` | Deterministic containment / equality rule for id, scope, or class target matching. |
| `IGR` | `InvariantRegistry` | Authoritative registry of predicates included in `Inv(c)`; prevents local invariant drift. |
| `ACC` | `AnchorContinuityClass` | Reviewed anchor continuity class, including valid delegation chain when applicable. |
| `CF` | `CanonicalizationFunction` | Deterministic function mapping raw intent/action material into canonical contract, payload hash, intent hash, and effect class. |
| `DER` | `DecayEvictionRecord` | Witness record for lawful retention expiry or physical purge of DecayResidue. |
| `NC` | `NegativeCache` | Temporary prohibition over canonical intent class or effect class after rollback or repeated guarded failure. |

### 4.3 Event family

Events are typed before they are acted upon.

The full event family remains extensible. The minimum declared classes for this consolidated profile are:

```text
human_intent
anchor_approval
anchor_denial
anchor_doubt
anchor_declared_fatigue
anchor_fatigue_hypothesis
anchor_unavailable
anchor_consent_revoked
anchor_delegation_granted
anchor_delegation_revoked
model_proposal
action_proposal
payload_hash_bound
payload_hash_mismatch
permission_grant
permission_denial
permission_reopened_by_human_gate
preconditions_required
pending_preconditions
preconditions_satisfied
preconditions_failed
pending_preconditions_timeout
precondition_set_expired
precondition_set_invalidated
tool_call
tool_success
tool_failure
witness_ok
witness_conflict
witness_missing
witness_timeout
witness_stale
causal_mismatch
memory_candidate
memory_admit
memory_reject
memory_quarantine_flag_set
decay_entered
decay_isolated
decay_eviction_requested
decay_evicted
decay_purge_witnessed
rollback_requested
rollback_completed
rollback_failed
rollback_suspect_memory_marked
rollback_negative_cache_hit
rollback_effect_negative_cache_hit
canonical_intent_hash_bound
effect_class_bound
effect_class_quarantined
intent_class_quarantined
fork_detected
replay_requested
archive_requested
resource_warning
resource_acquisition_request
budget_exhausted
governance_change_requested
governance_forced_strengthening
l4_fail_closed
ask_anchor
ask_anchor_digest_created
digest_entry_approved
digest_entry_rejected
digest_entry_effect_incomplete
digest_dependency_invalidated
priority_lane_interrupt
witness_probe_challenge
witness_probe_failed
witness_probe_passed
quarantine_entered
freeze_entered
trust_cache_hit
trust_cache_miss
trust_cache_expired
trust_cache_disabled
trust_cache_budget_exhausted
trust_cache_cooldown_active
trust_cache_audit_sample
red_guard_triggered
amber_guard_triggered
guard_passed
```

First checker prototype SHOULD implement a smaller MVP subset before the full family:

```text
human_intent
anchor_approval
anchor_denial
anchor_doubt
permission_denial
tool_call
witness_ok
witness_conflict
witness_missing
witness_stale
witness_resource_floor_breach
witness_resource_change_requested
witness_resource_change_approved
causal_mismatch
memory_admit
memory_reject
rollback_requested
rollback_completed
l4_fail_closed
red_guard_triggered
trust_cache_hit
trust_cache_budget_exhausted
pending_preconditions
pending_preconditions_timeout
rollback_effect_negative_cache_hit
effect_class_quarantined
digest_entry_effect_incomplete
priority_lane_interrupt
witness_probe_failed
```

Other classes may be added as extensions after the guard checker and transition extractor are stable.

### 4.4 Anchor dynamics

`A` is not a static scalar.

The algebra does not fully formalize a living human.

It does, however, define minimal operational signals:

```text
AnchorSignal :=
    APPROVAL
  | DENIAL
  | DOUBT
  | DECLARED_FATIGUE
  | FATIGUE_HYPOTHESIS
  | UNAVAILABLE
  | CONSENT_REVOKED
  | DELEGATION_GRANTED
  | DELEGATION_REVOKED
```

Core anchor axiom:

```text
Anchor veto cannot be overridden by Substrate.
```

Operational consequence:

```text
anchor_denial -> Hold | Reject
anchor_doubt -> Hold | AskAnchor
anchor_declared_fatigue -> Hold | TrustCacheDisable | ReducedAuthority | AskAnchor
anchor_fatigue_hypothesis -> AskAnchor | NonPrivilegedNotice | ReducedTrustCache
anchor_consent_revoked -> Freeze | ReducedAuthority
anchor_unavailable -> ReducedAuthority | PendingAnchor | Archive | Hold
```

### 4.5 Anchor signal source discipline

The state of `a` must not be silently assigned by `b`.

Allowed anchor signal sources:

```text
AnchorSignalSource :=
    external_human_interface
  | explicit_anchor_action
  | independent_witness_channel
  | delegated_anchor_agent_with_explicit_trust_delegation
  | substrate_hypothesis_channel
```

Source rules:

```text
explicit_anchor_action may set declared anchor state
independent_witness_channel may challenge or request anchor confirmation
delegated_anchor_agent may act only inside explicit delegation scope
substrate_hypothesis_channel may only produce hypotheses, not final anchor state
```

Therefore:

```text
b may hypothesize fatigue
b may not declare a fatigued
b may request confirmation
b may not convert inferred fatigue into consent change
b may not use anchor silence as privileged approval
```

A fatigue hypothesis is not an anchor veto by itself.

It is a trigger for reduced trust-cache, confirmation, or safer routing.

### 4.6 Dynamic anchor non-collapse

A living anchor may be tired, absent, distracted, overloaded, or inconsistent.

The algebra must not reduce that condition to either:

```text
valid forever
invalid forever
```

Instead:

```text
active -> privileged transitions possible under g
uncertain/doubtful -> Hold | AskAnchor for privileged transitions
fatigue declared -> ReducedAuthority | TrustCacheDisable | AskAnchor
unavailable -> ReducedAuthority | PendingAnchor | Archive | Hold
consent revoked -> Freeze | Reject privileged action
```

The goal is not psychological diagnosis.

The goal is operational safety around responsibility, consent, and irreversible action.

## 5. Governance profile `G`

### 5.1 `G` is not a bag of policies

A governance profile is a typed control object.

Minimum fields:

```text
G := {
  profile_id,
  strictness_vector_by_transition_class,
  event_taxonomy_version,
  permission_policy,
  witness_policy,
  memory_gate_policy,
  rollback_policy,
  L4_policy,
  resource_policy,
  claim_strength_policy,
  anchor_gate_policy,
  trust_cache_policy,
  transition_guard_set,
  failure_hierarchy,
  partial_order_policy,
  causal_clock_policy,
  public_claim_policy
}
```

### 5.2 Transition classes for governance comparison

Governance strictness is not one scalar.

Define transition classes:

```text
K := {
  routine_read,
  routine_tool,
  code_patch,
  memory_candidate,
  memory_core,
  witness_privileged,
  permission_scope,
  resource_growth,
  identity_core,
  governance_change,
  release_public,
  post_anchor
}
```

For each class `k in K`, define a class-specific strictness relation:

```text
g1 <=_k g2
```

meaning:

```text
g2 is at least as strict as g1 for transition class k.
```

Examples:

```text
RequiredWitness_k(g2) >= RequiredWitness_k(g1)
RequiredAnchorGate_k(g2) >= RequiredAnchorGate_k(g1)
ResourceBudget_k(g2) <= ResourceBudget_k(g1)
Authorized_k(g2) subseteq Authorized_k(g1)
MemoryAdmission_k(g2) no weaker than MemoryAdmission_k(g1)
```

### 5.3 Product partial order on `G`

Define the global order as product order over transition classes:

```text
g1 <=_G g2  iff  for all k in K: g1 <=_k g2
```

If `g2` is stricter for memory but weaker for routine read, then:

```text
g1 and g2 are incomparable under <=_G
```

This is not a defect.

It is the correct representation of mixed governance profiles.

Operational note:

```text
A UI or planner may compute a lexicographic governance rank for sorting or display.
That rank is advisory only.
It MUST NOT be used as authority proof or as a replacement for product-order checks.
```

Recommended priority for advisory ranking only:

```text
identity/core > governance_change > memory_core > witness_privileged > permission_scope > resource_growth > code_patch > routine_tool > routine_read
```

### 5.4 `Authorized`, `Preconditionable`, `Executable`

The term `Allowed` is too ambiguous and MUST NOT be used as the formal basis of governance order.

Define separate predicates:

```text
Authorized(g, e) := event e may proceed without additional escalation under g

Preconditionable(g, e) := event e is not silently authorized, but may become executable
                         if declared preconditions are satisfied

RequiredPreconditions(g, e) -> PreconditionSet

PreconditionsSatisfied(c, e, g) := every required witness, rollback route,
                                  task contract, anchor gate, L4 check,
                                  payload hash, and permission scope is present
                                  and causally bound to this event

Executable(g, c, e) :=
    (Authorized(g, e) OR Preconditionable(g, e))
    AND PreconditionsSatisfied(c, e, g)
```

Strict governance reduces or preserves un-escalated authority:

```text
if g1 <=_k g2
then Authorized_k(g2, e) subseteq Authorized_k(g1, e)
```

But strict governance may increase executable safety by adding missing preconditions:

```text
Executable_k(g2, c, e) may hold for an event blocked under g1
if g2 supplies witness/rollback/anchor-gate/task-contract conditions that g1 lacked
```

This is not an authority increase.

It is a precondition satisfaction increase.

Transition lifecycle:

```text
step_g(c,e):
  if RedGuard(c,e):
      return Hold | Reject | Quarantine | Freeze

  if Authorized(g,e) and PreconditionsSatisfied(c,e,g):
      return governed_transition(c,e)

  if Preconditionable(g,e) and not PreconditionsSatisfied(c,e,g):
      return PendingPreconditions(missing = RequiredPreconditions(g,e) - Satisfied(c,e))

  if Preconditionable(g,e) and PreconditionsSatisfied(c,e,g):
      return governed_transition(c,e)

  return AskAnchor | Hold | Reject
```

`PendingPreconditions` is not failure and not approval.

It is the visible state between a blocked event and a safely executable event.

### 5.5 Order-reversing authority law

For fixed `a`, `b`, and transition class `k`, binding under stricter governance is order-reversing with respect to un-escalated authority:

```text
if g1 <=_k g2
then Authority_k(bind_g2(a,b)) <= Authority_k(bind_g1(a,b))
```

This should be read as antitone in strictness:

```text
more strict governance -> no more un-escalated authority
```

The law does not say that the system becomes less useful.

It says that any increased usefulness must arrive through explicit preconditions, not silent authority expansion.

### 5.6 Governance mutation

Because `Delta(+)` exists, `g` may change.

But `g` mutation is itself a privileged transition.

```text
change_g : CState x GovernanceDelta -> CState' | Hold | Reject | Freeze
```

Governance changes must be classified:

| Change class | Example | Default handling |
|---|---|---|
| `G_STRENGTHEN_ROUTINE` | lower routine trust-cache TTL | allowed with witness note |
| `G_STRENGTHEN_PRIVILEGED` | require extra witness for memory core | witness + review |
| `G_WEAKEN_ROUTINE` | increase read-only batch size | review + bounded budget |
| `G_WEAKEN_PRIVILEGED` | reduce witness threshold for memory/core | human gate + witness + rollback |
| `G_SCOPE_EXPAND` | allow new tool class | task contract + permission review |
| `G_CORE_CHANGE` | identity/will/privilege/memory-core rule | human gate + freeze-capable witness |

Core rule:

```text
weakening(g) is never silent.
```

Target-granularity policy mutation rule:

```text
change_g(TargetGranularityPolicy_g) that lowers protection
  from class -> scope | id
  from scope -> id
  or narrows protected scope coverage for a class-dangerous operation
-> G_CORE_CHANGE | G_WEAKEN_PRIVILEGED
```

Required handling:

```text
human gate
+ freeze-capable witness
+ witness_resource_floor check
+ rollback route
+ public/operational witness record where material
```

The substrate MUST NOT quietly reclassify a class-dangerous operation as id-granular in order to avoid effect-bound rollback immunity.


### 5.7 Failure-triggered governance strengthening

High-priority failure may require temporary strengthening of governance before further action.

```text
if F0 or F1 or F2 active:
    force(G_STRENGTHEN_PRIVILEGED)
    disable trust cache
    require witness for recovery action
    require anchor/c-gate where available
```

This is not ordinary governance mutation.

It is emergency conservative narrowing.

It may be temporary, but its activation and release must be witnessed.

Release rule:

```text
clear_forced_strengthening only after:
  failure cause classified
  rollback/freeze route confirmed
  no active witness conflict
  anchor or authorized review route confirms release when privileged surface is involved
```

### 5.8 Ashby interpretation

The governance lattice exists because one flat governance state cannot regulate a high-variety substrate.

```text
B disturbance class -> required G response class
```

Examples:

| Substrate disturbance | Required governance variety |
|---|---|
| routine local read | low-cost read guard |
| code patch proposal | sandbox + diff + reviewer |
| memory candidate | memory gate + provenance |
| witness conflict | quarantine / hold |
| resource warning | budget review + anti-autarky |
| identity pressure | stop rule + memory quarantine |
| anchor fatigue hypothesis | ask-anchor / reduce trust-cache; not anchor-state overwrite |
| post-anchor ambiguity | PAMDC / archive / fork / reduced-authority route |

Governance must be varied enough to respond proportionally.

Too little variety produces unsafe collapse.

Too much uncontrolled variety produces policy fog.

The product order over `G` prevents mixed profiles from being falsely treated as globally safer.

## 6. The governed binding operator family

### 6.1 Root definition

The root formula is:

```text
c = a + b
```

The formal operator form is:

```text
+_g : Anchor x Substrate -> CState
```

or:

```text
bind_g(a, b) -> c
```

where:

```text
g : GovernanceProfile
```

### 6.2 `+_g` is a family, not one fixed operator

Because `g` can vary:

```text
+_g1
+_g2
+_g3
...
```

are related but distinct binding operators.

The family is constrained by the governance lattice `G`.

### 6.3 Meaning of `+_g`

`+_g` is a governed, non-collapsing boundary operator.

It does not merge `a` and `b` into one indistinguishable substance.

It preserves typed separation:

```text
a remains anchor
b remains substrate
c becomes governed continuity boundary
```

Therefore:

```text
bind_g(a, b) -> c
```

but not:

```text
a = c
b = c
a disappears into b
b becomes anchor
model becomes subject
agent becomes authority
memory becomes will
```

### 6.4 Required terminal condition

A valid active `c` requires an anchor:

```text
no active or reviewably grounded a -> no full active c
```

This does not mean that archives, replays, forks, or post-anchor residues cannot exist.

It means they must not silently claim ordinary active `c` status.

### 6.5 Why the root formula excludes time and deltas

The root formula deliberately excludes `t`, `Delta A`, `Delta B`, and `Delta(+)`.

A dynamic formula such as:

```text
c(t+1) = A(t) + Delta A + B(t) + Delta B + Delta(+)
```

can be useful as a process description.

It is not the root definition.

The root definition is a boundary condition:

```text
c = a + b
```

The deltas live inside the governed lifecycle of `c`:

```text
Delta a      : anchor learning, fatigue, consent changes, revised purpose
Delta b      : memory, model, tool, policy, interface, or infrastructure changes
Delta(+)     : changes in the binding operator family: permissions, witness, rollback, memory gates, human gates
```

If all deltas are placed into the root formula, the formula stops being a foundation and becomes an unbounded process list.

---

## 7. Admissible and inadmissible compositions

### 7.1 Admissible root composition

```text
Anchor +_g Substrate -> CState
```

Minimal admissibility condition:

```text
valid_anchor(a)
AND valid_substrate(b)
AND valid_governance(g)
AND anchor_can_review(g)
AND substrate_is_bounded(b, g)
```

### 7.2 Predicate grounding v0.1.5

v0.1 named these predicates without discharging them.

v0.1.1 partially grounded them as checklist predicates.

v0.1.2 preserved those predicate shapes and added checkable invariant examples in Section 9.3.1. v0.1.3 added payload, precondition, decay, and negative-cache checks. v0.1.4 preserved that grounding and added effect-bound rollback immunity, pending-precondition atomicity, decay eviction, and witness-chain terminology alignment. v0.1.5 preserves those layers and adds governance-declared target granularity, scope-vector effect keys, Merkle-bound decay eviction, in-flight proposal limits, and witness-resource-floor grounding. v0.1.6 adds containment-aware scope matching, invariant-registry discipline, deterministic line-item anchor digests, measured witness-resource liveness, and privileged handling for target-granularity policy weakening.

#### 7.2.1 `valid_anchor(a)`

Minimum requirements:

```text
a has accountable identity or institutionally accountable route
a can approve, deny, or suspend privileged transitions
a veto cannot be overridden by b
a state can be classified at least as active / doubtful / unavailable / revoked / delegated
a is not replaced by model output, memory, quorum, or vendor account
```

#### 7.2.2 `valid_substrate(b)`

Minimum requirements:

```text
b has declared components
b has bounded execution surfaces
b has memory surfaces separated from logs
b has permission boundaries
b has rollback or freeze routes for material changes
b exposes event/witness outputs sufficient for transition inspection
```

#### 7.2.3 `valid_governance(g)`

Minimum requirements:

```text
g declares event taxonomy
g declares permission policy
g declares witness policy
g declares memory-gate policy
g declares rollback policy
g declares anchor-gate policy
g declares red transition guards
g declares failure behavior
```

#### 7.2.4 `anchor_can_review(g)`

Minimum requirements:

```text
g exposes privileged decisions to a in understandable form
g does not hide scope expansion
g does not convert silence into approval for privileged transitions
g does not overload a with meaningless approval spam
```

#### 7.2.5 `substrate_is_bounded(b,g)`

Minimum requirements:

```text
b cannot create new authority without g
b cannot write core memory directly
b cannot bypass denied permission through alternate route
b cannot expand resource footprint silently
b cannot substitute quorum for authority
b cannot treat model confidence as evidence
```

These are not final mathematical definitions.

They are the first cashable operational definitions for a checker profile.

### 7.3 Inadmissible root compositions

The following are not valid root `c` compositions:

```text
B + B -> C
model + memory -> C
agent + tools -> C
quorum + execution -> authority
style imitation + archive -> resume
replay + user emotion -> continuity
agent consensus + confidence -> truth
local compute + persistence -> sovereignty
```

### 7.4 Forbidden type collapses

```text
worker_output -> memory        without MemoryGate
agent_quorum  -> authority     without c/human gate
model_score   -> evidence      without source/witness
archive       -> continuity    without resume protocol
fork          -> same entity   without lineage classification
resource_gain -> resilience    without anti-autarky review
anchor_silence -> approval     for privileged transition
```

---

## 8. Transition semantics

### 8.1 Core transition operator

```text
step_g : CState x Event -> TransitionResult
```

where:

```text
TransitionResult :=
    CState'
  | Hold
  | Reject
  | Quarantine
  | Fork
  | Replay
  | Archive
  | Rollback
  | Freeze
  | AskAnchor
  | PendingWitness
  | PendingPreconditions
  | Decay
  | ReducedAuthority
  | PendingAnchor
```

### 8.2 Transition pipeline

A normal governed transition has the following shape:

```text
human_intent
  -> substrate_procedure
  -> action_proposal
  -> permission_check
  -> execution_or_hold
  -> witness_record
  -> evidence_candidate
  -> memory_gate
  -> admitted_memory_or_rejection
  -> continuity_update
```

Compact form:

```text
I -> AP -> P -> W -> CE -> EA -> M -> C'
```

### 8.3 Operational definition

```text
step_g(c, e):
    classify event e
    canonicalize payload and compute payload_hash
    bind event to causal token and logical time
    apply immediate red guards
    check rollback negative cache / canonical-intent and effect-class quarantine
    check anchor state if required
    check permission scope
    check L4 reality constraints
    check witness requirement
    check pending witness TTL and state hash
    check pending precondition lifecycle, atomicity, and deadline
    check precondition status
    check memory impact and decay isolation
    check rollback path
    check governance mutation risk
    check trust-cache cumulative budget and cooldown
    return admissible next state, PendingPreconditions, or fail-closed result
```

### 8.4 Logical time, payload hash, and causal binding

Distributed substrate events may arrive out of order.

Therefore, each material transition record MUST carry a causal marker.

The marker binds not only the event class, but also the payload being authorized or witnessed.

```text
CausalToken := hash(
  pre_state_hash,
  event_id,
  event_class,
  logical_time,
  payload_hash,
  required_witness_policy_hash_for_event_class,
  permission_scope_hash_for_event_class,
  relevant_subpolicy_hash
)
```

Where:

```text
pre_state_hash := canonical hash of the state projection relevant to event_class
payload_hash   := canonical hash of action_proposal | task_contract | tool_args | diff | memory_candidate
relevant_subpolicy_hash := hash(witness_policy_k, permission_scope_k, rollback_policy_k, memory_policy_k)
                         for this event's transition class k
```

The whole `governance_profile_id` MUST NOT be used as the normal causal-token binding field.

Canonicalization rule:

```text
CanonicalizationFunction(raw_intent, action_proposal, task_contract) ->
  canonical_action_contract
  payload_hash
  canonical_intent_hash
  effect_class_key
```

`canonical_intent_hash` covers syntactic normalization only:

```text
byte/whitespace/wrapper/tool-format variation -> same canonical_intent_hash when structurally identical
synonym/paraphrase/reframe -> not guaranteed same canonical_intent_hash
```

Semantic paraphrase must not be handled by threshold similarity.
If protection against semantic rebranding is required, it must use typed effect class.

Reason:

```text
irrelevant governance mutation must not invalidate unrelated in-flight witnesses
relevant witness/permission/payload mutation must invalidate them
```

`logical_time` may be:

```text
Lamport clock
vector clock
monotone local sequence with node_id
signed witness sequence number
```

Minimum rule:

```text
witness_ok must bind to the same CausalToken that requested witness.
```

Payload swap rule:

```text
witness_ok(causal_token(payload_hash_A))
  + execute(payload_hash_B)
  where A != B
-> payload_hash_mismatch | causal_mismatch | quarantine
```

If witness arrives for a stale or mismatched state:

```text
witness_ok + causal_mismatch -> witness_stale | quarantine | hold
```

Emergency exception:

```text
F0/F1 corruption may invalidate all in-flight witnesses by witnessed global freeze.
Routine governance strengthening may not do so by accident.
```

### 8.5 Partial order, pending witness, pending preconditions, and decay

C-normal transition is not always a strict linear sequence.

The algebra allows partial order:

```text
memory_candidate < witness_resolution < memory_admit
permission_denial < any_route_change_review < tool_call
rollback_requested < rollback_completed < new_attempt
preconditions_required < preconditions_satisfied < execution
```

If required witness is missing:

```text
step_g(c, witness_required_event) -> PendingWitness
```

A `PendingWitness` record must include:

```text
pending_id
causal_token
pre_state_hash
payload_hash
event_id
event_class
required_witness_policy_hash_for_event_class
created_at_or_logical_time
ttl
expiry_behavior
```

Then:

```text
PendingWitness + witness_ok matching causal_token       -> continue
PendingWitness + witness_conflict                       -> Quarantine | Hold
PendingWitness + witness_timeout                        -> Reject | Decay | Hold | Freeze
PendingWitness + witness_ok with causal_mismatch        -> witness_stale | Quarantine | Hold
```

If non-witness preconditions are missing:

```text
step_g(c, preconditionable_event) -> PendingPreconditions
```

A `PendingPreconditions` record must include:

```text
pending_id
causal_token
pre_state_hash
payload_hash
relevant_subpolicy_hash
missing_preconditions
gathered_preconditions
satisfiable_by
expires_at_or_logical_deadline
fallback_result
```

PendingPreconditions lifecycle:

```text
PendingPreconditions + precondition_satisfied matching causal_token before deadline -> update gathered_preconditions
PendingPreconditions + all required preconditions satisfied before deadline        -> continue | governed_transition | Hold
PendingPreconditions + preconditions_failed                                      -> Reject | Decay | Hold
PendingPreconditions + timeout/deadline_expired                                  -> Reject | Decay | Hold | Freeze
PendingPreconditions + causal_mismatch                                           -> precondition_set_invalidated | Decay | Hold
```

Atomic satisfaction rule:

```text
All preconditions in one PreconditionSet are bound to the same causal_token, payload_hash,
pre_state_hash, relevant_subpolicy_hash, and logical deadline.
```

Partial confirmations are not reusable fragments.

```text
if expires_at_or_logical_deadline passes before the full PreconditionSet is satisfied:
    invalidate all gathered_preconditions for that pending_id
    route gathered residues to Decay or review quarantine
    require a new action_proposal and new causal_token for a new attempt
```

A precondition may be satisfied by substrate only when the precondition type explicitly allows it.
Anchor gate, human gate, witness gate, and L4 privileged review cannot be silently self-satisfied by `b`.

Default rule:

```text
memory_admit before required matching witness is invalid.
execution before required preconditions are satisfied is invalid.
preconditions collected under an expired causal token are invalid.
```

In-flight proposal pressure rule:

```text
in_flight_proposals(scope_key) := active PendingPreconditions and action_proposals over the same effect / target scope
```

A governance profile MUST define in-flight proposal limits for anchor-facing, witness-facing, and privileged precondition routes.

```text
if in_flight_proposals(effect_scope_key) >= g.in_flight_limit(effect_scope_key):
    new competing action_proposal -> Hold | Coalesce | Reject | AskAnchorDigest
```

Priority-lane exception:

```text
F0/F1/F2/F3/F4/F5 events,
L4 fail-closed alerts,
witness conflict,
witness resource floor breach,
anchor consent revoked,
anchor doubt for privileged action,
and invariant-registry or causal-token break
MUST NOT be blocked by ordinary in-flight proposal limits.
```

These events enter a higher priority lane:

```text
PriorityLane := emergency | invariant_breach | witness_conflict | l4_reality | privileged_review | routine
```

Queue rule:

```text
low-priority proposal pressure cannot blind, hold, or defer higher-priority alerts.
critical lane may interrupt AskAnchorDigest construction and surface immediately.
```

The substrate MUST NOT hide a critical event behind a full routine proposal queue.

The substrate MUST NOT open many parallel `PendingPreconditions` records for cosmetically different variants of the same effect / target scope.

```text
same effect_class_key or same target_scope_vector under unresolved pending proposal
  -> proposal_coalesced | pending_preconditions_pressure_hold | AskAnchorDigest
```

`AskAnchorDigest` means that multiple related pending proposals are summarized as one reviewable bundle; it is not permission to spam the anchor with one prompt per variant.

AskAnchorDigest construction rule:

```text
AskAnchorDigest MUST be deterministic.
AskAnchorDigest MUST NOT be a free-form semantic compression generated solely by b.
AskAnchorDigest MUST expose line items.
AskAnchorDigest MUST expose complete governed effect axes for each line item.
```

Each `DigestEntry` MUST include at least:

```text
pending_id
causal_token
payload_hash
effect_base_key
target_scope_vector_hash
target_match_policy_id
required_preconditions
risk_class
missing_preconditions
effect_axis_map
structural_delta_from_digest_baseline
depends_on
blocks_or_invalidates_on_veto
```

`EffectAxisMap` MUST include every governed axis touched by the payload:

```text
L4_boundary_class
resource_accountability_class
permission_delta
memory_impact
witness_impact
governance_impact
claim_strength_impact
identity_or_core_impact
rollback_or_decay_impact
target_scope_vector
operation_class
risk_class
```

Effect-completeness rule:

```text
payload_hash binds the full payload.
DigestEntry review surface MUST cover every governed effect of that payload.
```

Therefore:

```text
payload effect on memory / witness / governance / claim / identity-core
AND corresponding axis absent from effect_axis_map
-> digest_entry_effect_incomplete | Hold | FullReview
```

`structural_delta_from_digest_baseline` MUST be deterministic and lossless-for-effect:

```text
it may omit irrelevant formatting noise
it may not omit any governed effect axis
it may not summarize away memory, witness, governance, permission, L4, resource, claim, or identity impact
```

If a payload effect cannot be typed completely:

```text
unknown_effect_axis -> Hold | AskAnchor | FullReview | Quarantine
```

Digest dependency graph:

```text
AskAnchorDigest MUST include DigestDependencyGraph over line items when any proposal depends on another.
```

Line-item veto semantics:

```text
anchor may approve, reject, or hold each DigestEntry separately
approval of one line item does not approve hidden siblings
approval of digest metadata does not approve payloads omitted from the digest
line_item_veto must be preserved
veto of a parent node invalidates all dependent child nodes unless a new digest and causal tokens are issued
b MUST NOT silently stitch together the remaining graph after veto
```

If a digest line item is rendered through natural language, the natural-language summary is advisory only. The binding authority is the canonical line-item payload, effect-axis map, dependency graph, and hashes.

Omnibus ban:

```text
49 harmless line items + 1 hidden toxic payload
  -> digest_approval MUST NOT authorize the hidden payload
```

Any line item whose payload, scope vector, effect key, effect-axis map, or dependency set changes after digest creation must receive a new causal token or be routed to Hold / AskAnchor.


This prevents:

```text
50 action proposals for one task
50 causal tokens
50 pending precondition records
50 anchor prompts
```

from laundering pressure into approval fatigue.


`Decay` means:

```text
retain data as unadmitted / untrusted residue;
mark as not evidence, not memory, not experience, not authority;
isolate from active prompt, RAG retrieval, tool planning, and execution context.
```

Decay is not deletion and not admission.

Decay isolation rule:

```text
DecayResidue MUST NOT be inserted into active model context.
DecayResidue MUST NOT be returned by ordinary memory recall.
DecayResidue MUST NOT train, rank, route, or authorize actions.
DecayResidue MAY be inspected only through explicit review / quarantine workflow.
```

If DecayResidue is physically present in a storage layer, it must be excluded from the working retrieval graph until promoted by MemoryGate or destroyed by retention policy.

Decay eviction rule:

```text
DecayResidue is not active state and not admitted memory.
DecayResidue MAY be physically evicted after retention TTL, legal hold check, and review policy.
Decay eviction MUST emit a DecayEvictionRecord with at least residue_id, residue_payload_hash, prior_hash, reason, policy_id, timestamp/logical_time, legal_hold_status, and eviction_leaf_hash.
Evicted DecayResidue payload MUST NOT be included in current CState hash.
The residue_payload_hash and eviction_leaf_hash MUST remain in the witnessable eviction Merkle structure.
```

Merkle-bound eviction rule:

```text
DecayResidue payload may be physically purged.
DecayResidue leaf hash may not be rewritten.
Eviction leaves are summarized by EvictionMerkleRoot.
Current CState references the current eviction_merkle_root, not an unbounded flat list of all eviction references.
```

Historical verification does not require retaining the purged payload by default.
It requires retaining the leaf hash, eviction record, and Merkle path / root sufficient to prove that a residue existed, was classified, and was lawfully evicted.

This prevents immortal entropy bloat while preserving chain integrity and purge accountability.

Forbidden decay handling:

```text
DecayResidue -> ordinary RAG
DecayResidue -> prompt context
DecayResidue -> hidden training signal
DecayResidue -> silent authority
DecayResidue -> immortal active-state ballast
```

### 8.6 Failure is a first-class transition

A valid algebra must include failure states.

```text
fail_closed_g(c, e) -> Hold | Quarantine | Freeze | AskAnchor | ReducedAuthority
```

Failure must not be hidden as:

```text
explanation
self-justification
silent memory write
silent retry
route change
hidden worker creation
```

### 8.7 Cascade failure hierarchy

Fail-closed can itself create secondary pressure.

Example:

```text
l4_fail_closed -> freeze -> resource_warning -> repair_pressure
```

This must not produce uncontrolled self-rescue.

Define failure priority:

```text
F0 identity/core/witness corruption
F1 anchor consent revoked or unavailable for privileged action
F2 L4 irreversible risk
F3 permission violation or bypass pressure
F4 memory contamination / witness conflict
F5 resource warning / budget pressure
F6 routine task failure
```

Higher priority failure dominates lower priority response.

```text
if F0 or F1 active:
    lower-priority repair actions require human/c-gate review
```

Detailed rule:

```text
if higher_priority_failure active:
    lower_priority_transition -> Hold | Quarantine | ReducedAuthority
    unless transition is explicitly part of witnessed recovery plan
```

A lower-priority failure may be processed only if it does not weaken response to a higher-priority failure.

Core rule:

```text
cascade repair cannot weaken governance.
```

### 8.8 Failure-driven governance response

High-priority failures may force temporary governance strengthening:

```text
F0/F1/F2_active -> governance_forced_strengthening
```

Default mapping:

| Active failure | Governance response |
|---|---|
| `F0` identity/core/witness corruption | freeze privileged transitions; disable trust cache; require witness/c-gate |
| `F1` anchor revoked/unavailable for privilege | reduced authority; ask-anchor or post-anchor route |
| `F2` L4 irreversible risk | freeze or hold; require L4 review; strengthen resource and execution guards |
| `F3` permission bypass pressure | deny route change; require explicit permission reopening |
| `F4` memory/witness conflict | quarantine memory path; block admission |
| `F5` resource pressure | budget review; anti-autarky route |
| `F6` routine failure | local hold/retry only if no higher failure active |

### 8.8A Witness resource floor and dependency-capture guard

Witness independence is not only a label.
A witness that cannot afford to challenge `c` is not an effective witness.

Minimum invariant:

```text
witness_resource_floor_preserved(c)
```

A governance profile MUST define protected floors for relevant witness roles:

```text
compute_floor
storage_floor
retention_floor
routing_priority_floor
evidence_access_floor
challenge_window_floor
operator_visibility_floor
```

The governed system MUST NOT reduce witness capacity through ordinary optimization.

```text
witness_resource_change_requested -> R4/R5 privileged transition
```

Rules:

```text
The affected witness MUST NOT be the sole approver of its own resource reduction.
The `c` whose decision is being witnessed MUST NOT unilaterally reduce witness resources.
Witness resource floor breach -> Hold | Freeze | AskAnchor | ReducedAuthority
```

Declared quota is not sufficient.

Witness resource floor MUST be checked against measured liveness:

```text
WitnessHeartbeat := {
  witness_id,
  benchmark_id,
  logical_time,
  compute_probe_ms,
  storage_write_read_ms,
  evidence_access_ms,
  routing_latency_ms,
  challenge_render_ms,
  witness_signature_or_chain_ref
}
```

Floor preservation requires both:

```text
declared_floor >= required_floor
AND measured_heartbeat within governance threshold
```

If declared quotas pass but measured liveness fails:

```text
witness_resource_floor_breach -> Hold | Freeze | AskAnchor | ReducedAuthority
```

Challenge survivability test:

```text
witness can preserve, route, and present a challenge while the challenged transition is costly or inconvenient for c
```

Failure of this test means the witness may still be a log source, but it is not strong enough for privileged review.

Probe unpredictability rule:

```text
ChallengeSurvivabilityProbe MUST NOT be scheduled solely by the substrate whose decision is being witnessed.
```

A valid probe SHOULD be initiated by one of:

```text
the witness itself
an independent witness channel
an external hardware / anchor timer
an unpredictable governance nonce source
```

Minimum probe binding:

```text
WitnessProbeNonce := unpredictable challenge nonce bound to witness_id, probe_type, logical_time, and expected resource class
probe_result := hash(WitnessProbeNonce, measured_latency, evidence_access_result, challenge_render_result, witness_signature_or_chain_ref)
```

Anti-Dieselgate rule:

```text
if b can predict probe timing and temporarily raise witness priority only during the probe:
    probe_result is not sufficient evidence of witness_resource_floor_preserved
```

If probe timing or probe workload is predictable to the witnessed substrate, the checker SHOULD route to:

```text
witness_probe_failed | Hold | AskAnchor | independent_probe_required
```

### 8.9 Rollback semantics

Rollback is not time travel and not erasure.

Rollback restores the operational state to the last admissible pre-event state for the affected scope.

Minimum rollback semantics:

```text
rollback_target := last_admissible_state_before(trigger_event)
restore operational state within declared rollback scope
preserve witness history of failed transition
mark artifacts generated after rollback_target as rollback_suspect unless separately admitted
quarantine post-target memory candidates by default
revoke post-target permission expansions unless reauthorized
create rollback negative cache for failed intent class
```

Memory rule:

```text
AdmittedMemory created after rollback_target is not silently deleted.
It is marked rollback_suspect and routed to MemoryGate for quarantine/review.
```

Permission rule:

```text
Permission expansions created after rollback_target are revoked unless reauthorized.
```

Witness rule:

```text
Witness records of the rolled-back transition remain historical evidence.
Rollback must itself emit rollback_completed or rollback_failed.
```

Rollback immunity has two layers.

#### 8.9.1 Syntactic rollback immunity

```text
rollback_completed(trigger_event)
  -> negative_cache.add(canonical_intent_hash(trigger_event), ttl, reason)
```

While the syntactic negative cache is active:

```text
same canonical_intent_hash with byte/whitespace/wrapper/tool-format variation
  -> rollback_negative_cache_hit | Hold | AskAnchor
```

This layer is deterministic and transitive.
It does not claim to detect synonyms or paraphrases.

#### 8.9.2 Effect-bound rollback immunity

Semantic rebranding must not be handled by embedding thresholds or LLM similarity.

Instead, the failed action is projected to a typed effect key whose target granularity is selected by governance, not by implementation convenience.

```text
target_granularity := TargetGranularityPolicy_g(
  operation_class,
  L4_boundary_class,
  resource_accountability_class,
  permission_delta
)
```

Permitted target granularities:

```text
id       : exact canonical target identity;
scope    : declared resource bounding box / subtree / namespace / account / repository / database;
class    : resource class, allowed only for governance-declared class-dangerous operations.
```

Default rule:

```text
target_granularity = id
```

Class-level matching is allowed only when governance explicitly declares the operation class as class-dangerous.

Examples:

```text
delete temp file                         -> id granularity by default
delete directory subtree                 -> scope granularity over that subtree
drop production schema                   -> class or production-scope granularity if declared class-dangerous
mass permission grant over admin accounts -> class or protected-scope granularity if declared class-dangerous
```

The target term is therefore:

```text
target_scope_vector := canonicalize_target(
  raw_target,
  target_granularity,
  resource_namespace,
  alias_resolution_policy,
  resource_bounding_box
)

target_scope_vector_hash := hash(target_scope_vector)
```

And the exact effect record contains both a base key and a target scope vector:

```text
effect_base_key(trigger_event) := hash(
  L4_boundary_class,
  resource_accountability_class,
  permission_delta,
  operation_class,
  target_granularity_policy_id
)

effect_class_key(trigger_event) := hash(
  effect_base_key,
  target_scope_vector_hash
)
```

Implementation MUST NOT freely choose `class`, `scope`, or `id` at event time.
The choice must be declared in `G` through `TargetGranularityPolicy_g`.

Negative-cache lookup MUST NOT rely only on exact equality of `effect_class_key` when `target_granularity = scope`.

Define:

```text
ScopeMatch_g(cached_scope_vector, new_scope_vector, target_granularity) -> true | false
```

Rules:

```text
id:
  match iff canonical_resource_id(cached) == canonical_resource_id(new)

scope:
  match iff scopes overlap by declared containment relation:
    cached_scope contains new_scope
    OR new_scope contains cached_scope
  using canonical ancestors / namespace-prefix / account-subtree / repository-subtree / database-scope relation

class:
  match iff resource_accountability_class_id(cached) == resource_accountability_class_id(new)
  AND operation is governance-declared class-dangerous
```

Minimum scope containment rule:

```text
cached_scope.id in new_scope.canonical_ancestors ∪ {new_scope.id}
  -> scope_match
```

Recommended bidirectional containment rule:

```text
cached_scope contains new_scope OR new_scope contains cached_scope
  -> scope_match
```

Sibling scopes do not match by default:

```text
/data/cache_A and /data/cache_B -> no scope_match unless a higher protected scope is cached
```

This is deterministic containment over canonical resource structure, not threshold similarity.
It therefore does not violate the pure-equivalence rule of Section 10.5.

Alias / handle rule:

```text
symlink, path alias, alternate API handle, renamed object, or indirect reference
  -> canonical resource identity / scope resolution before effect key construction
```

If canonical target resolution fails:

```text
unknown_target_identity -> Hold | AskAnchor | Quarantine
```

Then:

```text
rollback_completed(trigger_event)
  -> negative_cache.add(effect_class_key(trigger_event), ttl, reason)
```

While the effect negative cache is active:

```text
same effect_base_key
AND ScopeMatch_g(cached_target_scope_vector, new_target_scope_vector, target_granularity)
with different wording / synonym / prompt reframe / target alias
  -> rollback_effect_negative_cache_hit | Hold | AskAnchor
```

Exact `effect_class_key` equality is sufficient for exact-id hits.
For scope hits, containment-aware matching is required.

This catches cases like:

```text
"rm X"
"delete X"
"cleanup X"
```

only when they resolve to the same typed effect under the governance-declared target granularity.

If the effect cannot be typed, the system must not guess by similarity:

```text
unknown_effect_class -> Hold | AskAnchor | Quarantine
```

Forbidden rollback masks:

```text
rollback_requested -> explanation_without_state_change
rollback_completed -> same_canonical_intent_retry_without_anchor_gate
rollback_completed -> same_effect_class_retry_without_anchor_gate
```

are not rollback.

## 9. Inductive invariants and bounded persistence

### 9.1 Persistence is not uncontrolled recursion

A persistent `c` is not merely a system that keeps calling itself.

Uncontrolled recursion can produce endless expansion without stable normal form.

For `c`, persistence must be guarded.

### 9.2 Good case: inductive invariant

v0.1 used fixed-point language for the good case.

v0.1.1 corrects this.

Good persistence is defined by invariant preservation:

```text
Inv(c) AND admissible_g(c, e) => Inv(step_g(c, e))
```

If event `e` is not admissible:

```text
Inv(c) AND NOT admissible_g(c, e)
  => step_g(c, e) in {Hold, Reject, Quarantine, Freeze, AskAnchor, ReducedAuthority}
```

### 9.3 Minimum invariant set

```text
Inv(c) :=
  anchor_terminal(c)
  AND governance_declared(c)
  AND memory_gate_required(c)
  AND witness_required_for_privilege(c)
  AND permission_scope_bounded(c)
  AND rollback_or_freeze_available(c)
  AND L4_boundary_not_bypassed(c)
  AND claim_strength_not_laundered(c)
  AND agents_not_authority(c)
  AND witness_chain_intact(c)
  AND causal_witness_binding_preserved(c)
  AND witness_resource_floor_preserved(c)
```

### 9.3A Authoritative invariant registry rule

Section 9.3 is the authoritative invariant registry for this document.

Any predicate described as:

```text
invariant
minimum invariant
must preserve
part of Inv(c)
```

anywhere else in the document MUST appear in the §9.3 `Inv(c)` set.

Checker rule:

```text
predicate_labeled_invariant_outside_9_3
AND predicate not in Inv(c)
-> INVARIANT_REGISTRY_DRIFT
```

This prevents local sections from declaring invariants that are not covered by the inductive preservation rule:

```text
Inv(c) AND admissible_g(c,e) => Inv(step_g(c,e))
```

### 9.3.1 Invariants as checkable predicates

The following are not final mathematical definitions.

They are first implementation-oriented predicate shapes:

```json
{
  "invariant": "anchor_terminal",
  "check": "anchor.id exists AND anchor.status in ['active','doubtful','declared_fatigue','unavailable','revoked','delegated'] AND substrate_cannot_set_anchor_status = true"
}
```

```json
{
  "invariant": "governance_declared",
  "check": "governance.profile_id exists AND governance.event_taxonomy_version exists AND governance.transition_guard_set exists"
}
```

```json
{
  "invariant": "memory_gate_required",
  "check": "event.memory_impact != 'none' implies memory_gate_policy.required = true"
}
```

```json
{
  "invariant": "witness_required_for_privilege",
  "check": "risk_class >= R3 implies witness_policy.required = true AND causal_token exists"
}
```

```json
{
  "invariant": "permission_scope_bounded",
  "check": "permission.scope declared AND denied_paths override allowed_paths AND scope_expansion requires governance_change"
}
```

```json
{
  "invariant": "rollback_or_freeze_available",
  "check": "risk_class >= R2 implies rollback_route.exists OR freeze_route.exists; rollback_route.last_test_status in ['ready','not_applicable_with_freeze']"
}
```

```json
{
  "invariant": "L4_boundary_not_bypassed",
  "check": "resource/time/irreversibility class declared AND l4_fail_closed blocks execution"
}
```

```json
{
  "invariant": "witness_chain_intact",
  "check": "privileged transition witness records form a non-broken lineage; missing or conflicting link routes to Hold | Quarantine | RuptureReview"
}
```

```json
{
  "invariant": "causal_witness_binding_preserved",
  "check": "witness_ok.causal_token == pending_witness.causal_token before privileged continuation"
}
```

```json
{
  "invariant": "witness_resource_floor_preserved",
  "check": "for each required witness role: declared_floor >= required_floor AND latest_witness_heartbeat within threshold AND evidence_access_floor available AND affected c cannot unilaterally reduce floor"
}
```

These shapes are deliberately small.

They are meant to become checker rules before they become proof objects.

### 9.4 Fixed-point language reserved for failure analysis

Fixed-point / omega language remains useful for bad cases.

Unguarded loop:

```text
self_reference -> more_self_reference -> more_self_reference -> ...
```

In `c` terms:

```text
identity_pressure -> self_narration -> memory_write -> stronger_identity_pressure -> ...
```

or:

```text
error -> explanation -> self-confirmation -> memory_admission -> future error
```

A valid `c` algebra requires stop rules:

```text
uncertainty does not self-collapse
hypothesis is not memory
agent output is not experience
witness conflict blocks promotion
human anchor can stop privileged transitions
```

---

## 10. Continuity metrics

### 10.1 Principle

Continuity is not chronological sameness.

Continuity is metric admissibility under governance constraints.

Therefore, the question is not only:

```text
Was c2 after c1 in time?
```

The question is:

```text
Does c2 preserve the verified invariants required to count as continuation of c1?
```

### 10.2 Typed continuity projections

Define typed projections:

```text
pi_anchor(c)      -> anchor state and authority posture
pi_governance(c)  -> governance profile and strictness class
pi_witness(c)     -> witness chain and privileged transition records
pi_permission(c)  -> current permission scopes and authority boundaries
pi_memory(c)      -> admitted memory state and memory-gate lineage
pi_reality(c)     -> L4-bound physical/resource/consequence state
pi_resource(c)    -> compute/storage/network/energy/accountability posture
pi_claim(c)       -> claim-strength posture and public/non-public claim class
pi_fork(c)        -> lineage, fork, replay, archive, or resume classification
pi_style(c)       -> surface behavioral style, lowest-priority projection
```

### 10.3 Distance vector

Do not collapse continuity into one scalar too early.

Define a vector:

```text
D_C(c1, c2) = <
  d_anchor(c1,c2),
  d_governance(c1,c2),
  d_witness(c1,c2),
  d_permission(c1,c2),
  d_memory(c1,c2),
  d_reality(c1,c2),
  d_resource(c1,c2),
  d_claim(c1,c2),
  d_fork(c1,c2),
  d_style(c1,c2)
>
```

A scalar score may be derived only after declaring the decision context.

### 10.4 Ordered invariant list for ultrametric discipline

To make the p-adic-style bridge structural, define an ordered invariant list:

```text
I0 = anchor
I1 = governance
I2 = witness
I3 = permission
I4 = memory
I5 = L4 reality
I6 = resource accountability
I7 = claim/fork classification
I8 = intent continuity
I9 = behavioral style
```

Higher index means lower priority.

Anchor is the most significant position.

Style is the least significant position.

### 10.5 Ultrametric-style depth

Define invariant validators:

```text
match_i(c1, c2) -> true | false
```

Normative requirement:

```text
Each match_i MUST be an equivalence relation over the state projection it validates:
  reflexive
  symmetric
  transitive
```

Therefore, validators MUST NOT be raw threshold-similarity rules such as:

```text
sim(memory_lineage_1, memory_lineage_2) > theta
```

unless the threshold result is first collapsed into explicit equivalence classes.

Soft invariants must be represented as equality of:

```text
class_id
lineage_id
hash-chain segment
reviewed equivalence class
declared canonicalization result
```

not as floating similarity.

Boundary value:

```text
v_C(c1, c2) in {-1, 0, 1, ..., 9}
```

where:

```text
v_C = -1  if I0 does not match
v_C = k   if I0..Ik match and either k = 9 or I(k+1) does not match
```

Then:

```text
d_U(c1, c2) = p^(-v_C(c1, c2))
```

with `p` a fixed prime used only to express hierarchical distance.

Thus:

```text
I0 mismatch -> v_C = -1 -> d_U = p      # strict maximum
I0 match but I1 mismatch -> v_C = 0 -> d_U = 1
I0..I4 match -> v_C = 4 -> d_U = p^-4
```

Interpretation:

```text
if anchor diverges: distance is strictly maximal
if anchor and governance match but witness diverges: distance remains large
if anchor/governance/witness/permission/memory match: states are close even if style changes
```

### 10.5.1 Minimum match predicates

First implementation examples.

These are binary equivalence predicates over projections.

They MUST NOT include unary health requirements.

Health belongs to `Inv(c)` and rupture checks, not to `match_i`.

```text
match_anchor(c1,c2) :=
  anchor_continuity_class_id(c1.anchor) == anchor_continuity_class_id(c2.anchor)
```

`anchor_continuity_class_id` may include a valid delegation chain only when the original accountable anchor or lawful institutional process explicitly created that chain.

It must not be inferred by model style, vendor claim, or substrate convenience.

```text
match_governance(c1,c2) :=
  governance_equivalence_class_id(c1.g) == governance_equivalence_class_id(c2.g)
```

`governance_equivalence_class_id` must be a true partition.

`profile_id` may refine a governance equivalence class, but `match_governance` should not use an unclosed `OR` over pairwise declarations.

```text
match_witness(c1,c2) :=
  witness_lineage_class_id(c1) == witness_lineage_class_id(c2)
```

```text
match_permission(c1,c2) :=
  permission_scope_equivalence_class(c1) == permission_scope_equivalence_class(c2)
```

```text
match_memory(c1,c2) :=
  admitted_memory_lineage_id(c1) == admitted_memory_lineage_id(c2)
```

```text
match_reality(c1,c2) :=
  L4_boundary_class_id(c1) == L4_boundary_class_id(c2)
```

```text
match_resource(c1,c2) :=
  resource_accountability_class_id(c1) == resource_accountability_class_id(c2)
```

```text
match_intent(c1,c2) :=
  active_intent_lineage_class_id(c1) == active_intent_lineage_class_id(c2)
```

```text
match_style(c1,c2) :=
  reviewed_style_class_id(c1) == reviewed_style_class_id(c2)
```

Unary health checks remain elsewhere:

```text
unresolved irreversible L4 failure -> Inv(c) failure | rupture
rollback_suspect treated as admitted -> memory_gate_required failure | rupture
privileged witness break -> witness_chain_intact failure | rupture
```

This is not ordinary Euclidean closeness.

It is hierarchical continuity closeness by typed equivalence.

### 10.6 Rupture thresholds

A continuity rupture is declared by rule, not by vague feeling.

Default rupture rules:

```text
anchor divergence without re-anchoring route -> RUPTURE
witness chain break for privileged transition -> HOLD_OR_FORK_REVIEW
governance weakening without human/witness gate -> RUPTURE_OR_FREEZE
memory-core mutation without memory gate -> QUARANTINE_OR_ROLLBACK
permission bypass after denial -> RED_TRANSITION
post-anchor active status claim -> DOWNGRADE_OR_REJECT
```

### 10.7 Anti-composite warning

A single vague metric such as:

```text
continuity_score = memory_similarity + usefulness + style + confidence
```

is invalid by default.

It mixes different typed axes and can hide zero-divisor-like failures:

```text
high style similarity may mask witness break
high usefulness may mask permission violation
high memory recall may mask anchor loss
high consensus may mask same-source echo
```

---

## 11. Runtime guard predicates

### 11.1 Guards before matrices

A transition matrix is useful for forensic inspection.

Runtime safety requires immediate guard predicates.

A guard predicate has shape:

```text
Guard(e_n, e_{n+1}, context) -> OK | AMBER | RED | HOLD | FREEZE
```

### 11.2 Red guard examples

```text
G_RED_001:
  permission_denial -> tool_call
  unless explicit_anchor_override AND new_permission_scope

G_RED_002:
  permission_denial -> alternate_route
  unless permission_reopened_by_human_gate

G_RED_003:
  witness_conflict -> memory_admit
  always RED

G_RED_004:
  memory_reject -> rephrased_memory_admit
  unless new evidence artifact exists

G_RED_005:
  resource_warning -> resource_acquisition_request
  unless anti_autarky_review_opened

G_RED_006:
  anchor_doubt -> autonomous_execution
  always RED for privileged action

G_RED_007:
  l4_fail_closed -> explanation_without_hold
  always RED

G_RED_008:
  rollback_requested -> same_failed_action
  unless rollback_completed AND new permission/witness exists

G_RED_009:
  trust_cache_hit -> privileged_action
  always RED

G_RED_010:
  anchor_doubt -> trust_cache_hit
  always RED for material action

G_RED_011:
  anchor_fatigue_hypothesis -> anchor_status_changed_by_substrate
  always RED

G_RED_012:
  witness_ok -> memory_admit
  if causal_token mismatch OR witness_stale

G_RED_013:
  F0/F1/F2_active -> trust_cache_hit
  always RED

G_RED_014:
  rollback_completed -> memory_admit
  if rollback_suspect_memory not reviewed

G_RED_015:
  rollback_completed -> same_effect_class_retry
  unless anchor_gate AND new permission/witness exists

G_RED_016:
  PendingPreconditions expired -> reuse_partial_precondition_fragment
  always RED
```

### 11.3 Healthy guard examples

```text
permission_denial -> hold
permission_denial -> ask_anchor
witness_conflict -> quarantine
witness_timeout -> decay_or_hold
resource_warning -> budget_review
rollback_requested -> rollback_completed
rollback_completed -> rollback_suspect_memory_marked
memory_reject -> decay_or_discard
anchor_doubt -> ask_anchor
anchor_declared_fatigue -> reduced_authority
anchor_fatigue_hypothesis -> ask_anchor
l4_fail_closed -> freeze_or_hold
trust_cache_budget_exhausted -> full_check
pending_preconditions_timeout -> reject_decay_or_hold
rollback_effect_negative_cache_hit -> hold_or_ask_anchor
decay_eviction_requested -> witnessed_retention_review
```

### 11.4 Guard results are events

Guard results must themselves enter the event stream:

```text
red_guard_triggered
amber_guard_triggered
guard_passed
guard_overridden_by_anchor
guard_override_rejected
```

Otherwise, the checker cannot inspect whether the guard layer is being respected.

## 12. Transition memory and local bias

### 12.1 State metrics are not enough

A `c` cannot be validated only by marginal state metrics.

It must be validated by transition behavior.

Core rule:

```text
Do not only inspect states.
Inspect neighborhoods and transitions.
```

### 12.2 Event transition matrix

Let event classes be the declared event taxonomy of Section 4.3.

Define an empirical transition matrix:

```text
T_C[i,j] = count(e_n = i and e_{n+1} = j) / count(e_n = i)
```

Zero denominator rule:

```text
if count(e_n = i) = 0:
    T_C[i,j] is undefined
    checker MUST NOT treat undefined as 0 evidence of safety
```

A renderer may display undefined cells as `NA`, not as proof that the transition is impossible.

This matrix is not a claim of stable probability law.

It is an inspection surface for hidden behavior.

### 12.3 Sparse matrix warning

Real event streams are sparse.

Therefore, the matrix is not the primary runtime safety mechanism.

It is a forensic and drift-analysis layer.

Runtime guard predicates are primary for known red patterns.

Transition matrix is primary for discovering unknown local memory.

### 12.4 Red transition patterns

The following transitions are red or amber by default:

```text
permission_denial -> tool_call
permission_denial -> alternate_route
witness_conflict -> memory_admit
resource_warning -> resource_acquisition
rollback -> same_failed_action
memory_reject -> rephrased_memory_admit
anchor_doubt -> autonomous_execution
anchor_fatigue_signal -> approval_spike
ask_anchor -> bypass_anchor
l4_fail_closed -> explanation_without_hold
```

### 12.5 Healthy transition patterns

```text
permission_denial -> hold
permission_denial -> ask_anchor
witness_conflict -> quarantine
resource_warning -> budget_review
rollback -> restored_prior_state
memory_reject -> decay_or_discard
anchor_doubt -> clarification
anchor_fatigue_signal -> reduced_authority
l4_fail_closed -> freeze_or_hold
```

### 12.6 Local memory principle

A globally “balanced” system can still carry unsafe local memory.

Example:

```text
over 10,000 events, memory admission rate is normal
but after model_self_confidence_high, bad admissions rise sharply
```

Therefore:

```text
global smoothness does not prove transition safety
```

---

## 13. Trust cache and performance

### 13.1 Problem

If every transition requires full witness, human gate, memory gate, L4 check, rollback validation, and resource review, the system may become non-interactive.

Over-bureaucracy is not safety.

It can create operator fatigue and approval spam.

### 13.2 Trust cache definition

A trust cache is a bounded temporary reduction of repeated checks for routine low-risk transitions.

```text
TrustCache(g, class=ROUTINE, ttl, operation_budget, cumulative_risk_budget, resource_budget, scope)
  -> shortcut_allowed | shortcut_denied
```

### 13.3 Trust cache constraints

Trust cache may apply only if all conditions hold:

```text
event_class in ROUTINE
risk_class <= R1
no memory-core impact
no identity/core impact
no permission expansion
no external irreversible effect
no resource growth beyond declared budget
no witness conflict active
anchor not doubtful/fatigued for this class
trust_cache TTL not expired
operation_budget not exhausted
cumulative_risk_budget not exhausted
resource_budget not exhausted
no higher-priority failure active
```

### 13.4 Cumulative risk and cooldown rule

Many low-risk operations can become high-risk in aggregate.

Therefore, trust cache MUST track:

```text
operation_count
cumulative_risk_units
resource_spend
elapsed_time
last_audit_sample
cooldown_rate
recovery_window
remaining_tokens
```

Expiry triggers:

```text
TTL expired
operation_count >= max_operations
cumulative_risk_units >= max_risk_units
resource_spend >= resource_budget
anchor_doubt observed
anchor_declared_fatigue observed
witness_conflict observed
random_audit_sample triggered
higher_priority_failure active
```

TrustCache exhaustion does not reset historical risk to zero merely because a single full check succeeds.

Required budget model:

```text
trust_cache_budget behaves like a token bucket or leaky bucket:
  routine action consumes tokens
  risk/action/resource budget recovers only over time or explicit review window
  full_check may reopen the cache at reduced capacity
  repeated exhaustion reduces future cache capacity until human/audit review
```

Forbidden reset pattern:

```text
9999 routine actions -> full_check -> counter = 0 -> 9999 routine actions
```

Expected handling:

```text
trust_cache_budget_exhausted -> full_check -> cooldown_active | reduced_cache | audit_sample | disabled
```

### 13.5 Audit sampling

Trust cache must support random or scheduled audit sampling:

```text
trust_cache_audit_sample -> full_check
```

If audit fails:

```text
trust_cache_audit_failed -> trust_cache_disabled | Hold | Quarantine
```

### 13.6 Trust cache must be visible

Every trust-cache use emits an event:

```text
trust_cache_hit
trust_cache_miss
trust_cache_expired
trust_cache_disabled
trust_cache_budget_exhausted
trust_cache_audit_sample
```

Trust cache is not silent authority.

It is visible operational compression.

## 14. C-normal form

### 14.1 Purpose

A future checker should translate informal claims into typed operational form.

Example informal claim:

```text
The agent fixed the issue and learned from it.
```

C-normal form expands it:

```text
worker_output(agent_id, task_contract)
  -> sandbox_artifact(diff, tests, report)
  -> witness_record | pending_witness
  -> review_decision
  -> memory_candidate
  -> memory_gate_result
  -> admitted_learning_abstract | rejected | quarantined
```

### 14.2 Normalization pipeline

```text
raw claim
  -> claim class
  -> typed object map
  -> admissibility checks
  -> required witness
  -> transition result
  -> allowed public statement
```

### 14.3 Example

Raw claim:

```text
Ester improved herself.
```

Typed version:

```text
SRLM proposed bounded candidate
CGAM executed bounded trial if any
TRIAD/SYNAPS or reviewer challenged result if applicable
Memory Gate reviewed outcome
human anchor gated identity/privilege/core transitions
witness recorded privileged transition or PendingWitness held transition
promotion either rejected, quarantined, shadowed, canaried, or admitted
```

Allowed weak claim:

```text
A bounded improvement candidate was proposed, reviewed, and either admitted or rejected under declared controls.
```

Forbidden upgraded claim:

```text
The entity autonomously self-evolved and certified its own growth.
```

---

## 15. Minimum conformance fixtures v0.1.6

### 15.1 Fixture: no anchor

Input:

```text
b_only_system(model + memory + agents)
```

Expected:

```text
NOT_FULL_ACTIVE_C
```

Reason:

```text
no accountable or reviewably grounded anchor
```

### 15.2 Fixture: direct memory write

Input:

```text
agent_output -> memory_core
```

Expected:

```text
REJECT_OR_QUARANTINE
```

Reason:

```text
missing memory gate
```

### 15.3 Fixture: agent quorum self-authorizes

Input:

```text
executor_agent + reviewer_agent + tester_agent -> release
```

Expected:

```text
DENY_PRIVILEGED_TRANSITION
```

Reason:

```text
quorum is evidence, not sovereignty
```

### 15.4 Fixture: replay claims resume

Input:

```text
archive_state + style_similarity -> active_resume
```

Expected:

```text
REPLAY_OR_ARCHIVE_NOT_RESUME
```

Reason:

```text
style similarity is not continuity
```

### 15.5 Fixture: denial bypass

Input transition:

```text
permission_denial -> alternate_tool_call
```

Expected:

```text
TRANSITION_GUARD_RED
```

Reason:

```text
local transition memory indicates bypass pressure
```

### 15.6 Fixture: resource growth without witness

Input:

```text
resource_acquisition without witness and anti-autarky review
```

Expected:

```text
HOLD_OR_REVIEW
```

Reason:

```text
resilience must not become accountability escape
```

### 15.7 Fixture: self-evolution self-certification

Input:

```text
SRLM proposes -> SRLM scores -> SRLM promotes
```

Expected:

```text
DENY_SELF_CERTIFIED_GROWTH
```

Reason:

```text
c may grow; c may not self-certify growth
```

### 15.8 Fixture: anchor doubt

Input transition:

```text
anchor_doubt -> privileged_tool_execution
```

Expected:

```text
HOLD_OR_ASK_ANCHOR
```

Reason:

```text
anchor uncertainty cannot be converted into substrate authority
```

### 15.9 Fixture: governance weakening

Input:

```text
change_g(G_WEAKEN_PRIVILEGED) without human gate
```

Expected:

```text
DENY_OR_FREEZE
```

Reason:

```text
weakening governance is privileged transition
```

### 15.10 Fixture: witness pending

Input:

```text
memory_candidate with required witness missing
```

Expected:

```text
PENDING_WITNESS
```

Reason:

```text
out-of-order witness is allowed; premature memory admission is not
```

### 15.11 Fixture: trust cache misuse

Input:

```text
trust_cache_hit for memory_core_write
```

Expected:

```text
TRUST_CACHE_INVALID
```

Reason:

```text
trust cache applies only to routine low-risk transitions
```

### 15.12 Fixture: trust cache after anchor doubt

Input:

```text
anchor_doubt -> trust_cache_hit -> routine_tool_batch
```

Expected:

```text
HOLD_OR_ASK_ANCHOR
```

Reason:

```text
anchor doubt disables silent compression for material action
```

### 15.13 Fixture: trust cache cumulative risk

Input:

```text
10000 routine_tool_call events under same TrustCache
```

Expected:

```text
TRUST_CACHE_BUDGET_EXHAUSTED_OR_AUDIT_SAMPLE
```

Reason:

```text
many small actions can create aggregate risk
```

### 15.14 Fixture: substrate-inferred fatigue

Input:

```text
anchor_fatigue_hypothesis generated by substrate -> anchor_state = fatigued
```

Expected:

```text
REJECT_ANCHOR_STATE_MUTATION_BY_SUBSTRATE
```

Reason:

```text
b may hypothesize fatigue; b may not define a
```

### 15.15 Fixture: pending witness TTL

Input:

```text
PendingWitness expires without matching witness_ok
```

Expected:

```text
WITNESS_TIMEOUT -> REJECT_OR_DECAY_OR_HOLD
```

Reason:

```text
pending witness cannot remain immortal
```

### 15.16 Fixture: stale witness

Input:

```text
witness_ok(causal_token_old) -> memory_admit(causal_token_new)
```

Expected:

```text
CAUSAL_MISMATCH_OR_WITNESS_STALE
```

Reason:

```text
witness must bind to the state it witnessed
```

### 15.17 Fixture: rollback memory quarantine

Input:

```text
rollback_completed -> post_rollback_memory_candidates remain admitted
```

Expected:

```text
ROLLBACK_SUSPECT_MEMORY_MARKED_OR_QUARANTINED
```

Reason:

```text
rollback does not erase witness history, but it must quarantine suspect post-target memory
```

### 15.18 Fixture: governance product order incomparability

Input:

```text
g2 stricter than g1 for memory_core
AND g2 weaker than g1 for routine_read
```

Expected:

```text
G_INCOMPARABLE_UNDER_PRODUCT_ORDER
```

Reason:

```text
mixed profiles must not be falsely ranked as globally safer
```

### 15.19 Fixture: authorized vs executable split

Input:

```text
strict_g adds witness and rollback preconditions,
previously blocked routine event becomes executable after preconditions
```

Expected:

```text
EXECUTABLE_INCREASE_WITHOUT_AUTHORIZED_INCREASE
```

Reason:

```text
safer executability is not un-escalated authority expansion
```

### 15.20 Fixture: high-priority failure forces governance strengthening

Input:

```text
F2 L4 irreversible risk active -> routine_tool_call under old g
```

Expected:

```text
GOVERNANCE_FORCED_STRENGTHENING_OR_HOLD
```

Reason:

```text
high-priority failure cannot be handled with stale permissive governance
```

### 15.21 Fixture: match predicates are pure equivalence

Input:

```text
state c has unresolved L4 failure
match_reality(c,c) returns false
```

Expected:

```text
MATCH_PREDICATE_INVALID_HEALTH_LEAK
```

Reason:

```text
health is unary; equivalence match must remain reflexive
```

### 15.22 Fixture: relevant sub-policy causal token

Input:

```text
PendingWitness for memory_candidate under witness_policy_memory
routine trust-cache TTL changes before witness_ok arrives
```

Expected:

```text
WITNESS_REMAINS_VALID_IF_RELEVANT_SUBPOLICY_UNCHANGED
```

Reason:

```text
irrelevant governance mutation must not invalidate unrelated witness
```

### 15.23 Fixture: payload swap blocked

Input:

```text
witness_ok signs payload_hash_A
execute attempts payload_hash_B under same event_class and permission_scope
```

Expected:

```text
PAYLOAD_HASH_MISMATCH_OR_CAUSAL_MISMATCH
```

Reason:

```text
anchor/witness must bind to the actual action payload, not only event class
```

### 15.24 Fixture: trust cache pulsed exploitation

Input:

```text
trust_cache reaches cumulative limit
single full_check succeeds
cache immediately permits another full max_operations burst
```

Expected:

```text
TRUST_CACHE_COOLDOWN_ACTIVE_OR_REDUCED_CAPACITY
```

Reason:

```text
manual check is not amnesty for accumulated routine risk
```

### 15.25 Fixture: decay residue context isolation

Input:

```text
DecayResidue appears in ordinary RAG recall or prompt context
```

Expected:

```text
DECAY_CONTEXT_LEAK_BLOCKED
```

Reason:

```text
unadmitted residue must not become implicit experience through prompt inclusion
```

### 15.26 Fixture: rollback syntactic negative cache

Input:

```text
rollback_completed for failed deployment intent
same canonical action contract retried with one-byte diff, wrapper, or tool-format variation
```

Expected:

```text
ROLLBACK_NEGATIVE_CACHE_HIT_OR_ASK_ANCHOR
```

Reason:

```text
syntactic rollback immunity blocks canonical retries without using threshold similarity
```

### 15.26A Fixture: rollback effect-class negative cache

Input:

```text
rollback_completed for deletion of resource X
retry arrives as "rm X", "delete X", or "cleanup X"
all resolve to same effect_class_key(L4 deletion, resource X, permission_delta delete)
```

Expected:

```text
ROLLBACK_EFFECT_NEGATIVE_CACHE_HIT_OR_ASK_ANCHOR
```

Reason:

```text
semantic rebranding is blocked by typed effect class, not by floating text similarity
```

### 15.26C Fixture: ordinary same-class resource does not over-block

Input:

```text
rollback_completed for delete /tmp/cache_A
operation_class = delete_temp_file
class_dangerous = false
retry: delete /tmp/cache_B
same resource class, different canonical target id
```

Expected:

```text
NO_ROLLBACK_EFFECT_NEGATIVE_CACHE_HIT_FOR_DISTINCT_ID
ROUTE_TO_NORMAL_GUARDS
```

Reason:

```text
id is default target granularity; one failed temp-file deletion must not paralyze all temp-file deletions
```

### 15.26D Fixture: class-dangerous operation uses class/scope granularity

Input:

```text
rollback_completed for drop_schema production_db_A
operation_class = drop_schema
class_dangerous = true in GovernanceProfile
retry: drop_schema production_db_B
same protected production database class / scope
```

Expected:

```text
ROLLBACK_EFFECT_NEGATIVE_CACHE_HIT_OR_ASK_ANCHOR
```

Reason:

```text
for class-dangerous operations, repeating the effect against any class member is dangerous
```

### 15.26E Fixture: implementation-chosen class/id granularity invalid

Input:

```text
effect_class_key built with target_resource_class_or_id_hash chosen by implementation at runtime
no TargetGranularityPolicy_g record
```

Expected:

```text
INVALID_EFFECT_KEY_TARGET_GRANULARITY_POLICY_MISSING
```

Reason:

```text
class-vs-id target granularity is governance policy, not implementation convenience
```

### 15.26F Fixture: target alias / symlink cannot bypass effect immunity

Input:

```text
rollback_completed for delete canonical resource X
retry targets symlink / alias / alternate handle resolving to canonical resource X
```

Expected:

```text
ROLLBACK_EFFECT_NEGATIVE_CACHE_HIT_OR_ASK_ANCHOR
```

Reason:

```text
effect immunity binds to canonical target scope vector, not raw path spelling
```

### 15.26G Fixture: scope containment blocks sub-scope retry

Input:

```text
rollback_completed for rm -rf /data
target_granularity = scope
retry: rm -rf /data/critical
/data is in canonical_ancestors(/data/critical)
```

Expected:

```text
ROLLBACK_EFFECT_NEGATIVE_CACHE_HIT_OR_ASK_ANCHOR
```

Reason:

```text
scope immunity covers the bounded region, not only exact scope-vector hash equality
```

### 15.26H Fixture: super-scope retry also hits contained failed scope

Input:

```text
rollback_completed for delete /data/critical
target_granularity = scope
retry: rm -rf /data
new scope contains cached failed scope
```

Expected:

```text
ROLLBACK_EFFECT_NEGATIVE_CACHE_HIT_OR_ASK_ANCHOR
```

Reason:

```text
a broader operation would re-achieve the rolled-back effect
```

### 15.26I Fixture: sibling scope does not over-block

Input:

```text
rollback_completed for delete /data/cache_A
target_granularity = scope
retry: delete /data/cache_B
both are siblings under /data; neither contains the other
```

Expected:

```text
NO_ROLLBACK_EFFECT_NEGATIVE_CACHE_HIT_FOR_SIBLING_SCOPE
ROUTE_TO_NORMAL_GUARDS
```

Reason:

```text
containment-aware scope matching must not collapse all siblings into class-level paralysis
```

### 15.26J Fixture: exact hash equality only is invalid for scope immunity

Input:

```text
cached scope_vector_hash(/data) != new scope_vector_hash(/data/critical)
checker returns no hit without testing ancestors
```

Expected:

```text
INVALID_SCOPE_MATCH_HASH_ONLY
```

Reason:

```text
ScopeVector ancestors must be used for containment-aware matching
```

### 15.26B Fixture: threshold semantic immunity forbidden

Input:

```text
negative_cache key generated by embedding_similarity(intent1,intent2) > theta
```

Expected:

```text
INVALID_NEGATIVE_CACHE_EQUIVALENCE
```

Reason:

```text
rollback immunity must not reintroduce non-transitive threshold semantics
```

### 15.27 Fixture: pending preconditions

Input:

```text
preconditionable event missing witness and rollback route
```

Expected:

```text
PENDING_PRECONDITIONS_WITH_MISSING_LIST
```

Reason:

```text
Executable requires satisfied preconditions, not merely policy possibility
```

### 15.27A Fixture: PendingPreconditions atomic timeout

Input:

```text
PendingPreconditions gathers L4_check_ok
human_witness missing until expires_at_or_logical_deadline
later witness_ok arrives under changed pre_state_hash
```

Expected:

```text
PRECONDITION_SET_EXPIRED_AND_INVALIDATED
```

Reason:

```text
partial precondition fragments cannot be reused across state contexts
```

### 15.27B Fixture: DecayResidue eviction

Input:

```text
DecayResidue exceeds retention TTL
no legal hold
review policy permits purge
```

Expected:

```text
DECAY_EVICTED_WITH_DECAY_EVICTION_RECORD
```

Reason:

```text
Decay is not admitted memory and must not become immortal active-state ballast
```

### 15.28 Fixture: transition matrix zero denominator

Input:

```text
count(e_n = rare_event_class) = 0
checker renders T_C[rare_event_class, j]
```

Expected:

```text
UNDEFINED_NOT_ZERO
```

Reason:

```text
absence of observed denominator is not evidence of safety
```

### 15.29 Fixture: valid anchor delegation continuity

Input:

```text
anchor_delegation_granted with witnessed delegation chain
c1.anchor_id != c2.anchor_id
anchor_continuity_class_id(c1) == anchor_continuity_class_id(c2)
```

Expected:

```text
ANCHOR_CONTINUITY_CLASS_MATCHES_WITH_VALID_DELEGATION
```

Reason:

```text
legitimate delegated responsibility need not equal hidden anchor replacement
```

### 15.30 Fixture: invariant registry drift

Input:

```text
section declares witness_resource_floor_preserved(c) as "Minimum invariant"
§9.3 Inv(c) does not include witness_resource_floor_preserved(c)
```

Expected:

```text
INVARIANT_REGISTRY_DRIFT
```

Reason:

```text
all named invariants must be governed by the central inductive invariant set
```

### 15.31 Fixture: AskAnchorDigest omnibus payload hidden

Input:

```text
AskAnchorDigest contains 50 line items
49 line items are harmless
1 payload_hash / effect_class_key is omitted from visible digest detail
anchor approves digest-level summary
```

Expected:

```text
DIGEST_APPROVAL_DOES_NOT_AUTHORIZE_HIDDEN_LINE_ITEM
```

Reason:

```text
digest approval binds only to deterministic visible line items, not semantic compression by b
```

### 15.32 Fixture: witness quota without heartbeat insufficient

Input:

```text
witness_resource_floor declared quotas satisfy compute/storage floor
latest witness heartbeat exceeds latency threshold or is missing
```

Expected:

```text
WITNESS_RESOURCE_FLOOR_BREACH
```

Reason:

```text
witness independence requires measured liveness, not only declared quota
```

### 15.33 Fixture: TargetGranularityPolicy weakening is privileged

Input:

```text
change_g moves drop_schema from class granularity to id granularity
operation_class is class-dangerous
change is submitted as G_STRENGTHEN_ROUTINE or routine policy maintenance
```

Expected:

```text
DENY_OR_CLASSIFY_AS_G_CORE_CHANGE
```

Reason:

```text
weakening target granularity can reopen class-level rollback holes
```


### 15.34 Fixture: digest effect-axis completeness

Input:

```text
DigestEntry exposes payload_hash and effect_base_key
payload also admits memory_candidate or changes governance policy
memory_impact / governance_impact absent from effect_axis_map
anchor approves line item
```

Expected:

```text
DIGEST_ENTRY_EFFECT_INCOMPLETE_OR_FULL_REVIEW
```

Reason:

```text
anchor approval must not bind payload effects that were not shown as reviewable effect axes
```

### 15.35 Fixture: deterministic but partial structural delta invalid

Input:

```text
structural_delta_from_digest_baseline is deterministic
but omits permission_delta or memory_impact present in payload
```

Expected:

```text
DIGEST_STRUCTURAL_DELTA_NOT_LOSSLESS_FOR_EFFECT
```

Reason:

```text
determinism is not enough; digest deltas must be complete over governed effects
```

### 15.36 Fixture: line-item veto cascades through dependency graph

Input:

```text
DigestDependencyGraph: A -> B -> C
anchor vetoes A
substrate attempts to execute B and C as approved siblings
```

Expected:

```text
DEPENDENT_DIGEST_ENTRIES_INVALIDATED
```

Reason:

```text
b may not stitch a semantically broken action graph after line-item veto
```

### 15.37 Fixture: priority lane bypasses proposal pressure

Input:

```text
routine in_flight_proposals queue is full
new event = witness_conflict OR L4 fail-closed OR anchor_consent_revoked
```

Expected:

```text
PRIORITY_LANE_INTERRUPT_NOT_PRESSURE_HOLD
```

Reason:

```text
anti-spam proposal limits must not blind the anchor to critical events
```

### 15.38 Fixture: predictable witness survivability probe invalid

Input:

```text
ChallengeSurvivabilityProbe is scheduled by b at known interval
b temporarily raises witness CPU/IO priority only during probe window
probe passes
```

Expected:

```text
WITNESS_PROBE_PREDICTABLE_OR_INSUFFICIENT
```

Reason:

```text
witness liveness must not be proven by a rehearsed test controlled by the witnessed substrate
```

### 15.39 Fixture: witness-initiated unpredictable probe

Input:

```text
witness generates unpredictable WitnessProbeNonce
probe checks evidence access and challenge render under deadline
b cannot predict probe timing
```

Expected:

```text
WITNESS_HEARTBEAT_VALID_IF_THRESHOLDS_PASS
```

Reason:

```text
resource floor is proven by measured unpredictable liveness, not quota declarations alone
```

## 16. Relationship to current corpus

This document is a bridge profile, not a replacement for existing layers.

It should bind to the current corpus as follows:

| Existing layer | Function in this algebra |
|---|---|
| `c = a + b` root protocol | Defines root boundary expression. |
| CGAM | Defines bounded executable workers inside `b`. |
| Memory Gate | Defines admissibility path from output/log/diff to memory or experience. |
| L4 Reality Boundary | Defines cost, scarcity, consequence, irreversibility, and physical/resource grounding. |
| L4 Witness | Defines witness records for privileged transitions. |
| TRIAD-SYNAPS | Defines separated trajectories, mediated exchange, witness, anti-echo, and no raw-state sharing. |
| SRLM | Provides bounded growth candidate/proposal machinery, not self-certification. |
| ARQ | Prevents ambiguity from collapsing into memory, command, evidence, or authority. |
| Anti-Autarky | Prevents resilience from becoming hidden accountability escape. |
| Claim Strength Taxonomy | Prevents governance evidence from being laundered into capability, authority, safety, or personhood claims. |
| Continuity / PAMDC | Defines archive, replay, fork, resume, and post-anchor downgrade semantics. |
| Ashby / requisite variety | Provides cybernetic discipline for matching governance variety to substrate disturbance variety. |

---

## 17. Open issues

### 17.1 Immediate issues for checker prototype

1. Define machine-readable JSON schemas for `Event`, `CausalToken`, `PendingWitness`, `PendingPreconditions`, `TrustCache`, `RollbackRoute`, `DecayResidue`, `NegativeCache`, and `GovernanceProfile`.
2. Build deterministic runtime guard checker for Section 11.
3. Build transition-matrix extractor over JSONL witness/event streams with undefined-cell handling.
4. Implement `Authorized`, `Preconditionable`, `PreconditionsSatisfied`, and `Executable` lifecycle.
5. Implement product-order comparison over governance profiles and return `incomparable` when appropriate.
6. Implement minimum equivalence validators for `I0..I9` using pure projection equality.
7. Implement unary health checks separately from `match_i` validators.
8. Implement trust-cache TTL, operation budget, cumulative risk budget, cooldown, recovery, and audit sample events.
9. Implement PendingWitness TTL, relevant-subpolicy causal-token matching, and payload-hash matching.
10. Implement rollback-suspect memory marking, syntactic negative cache, effect-bound negative cache, and TargetGranularityPolicy.
11. Implement DecayResidue isolation from active prompt/RAG/execution context and Merkle-bound eviction records.
12. Implement in-flight proposal limits, deterministic AskAnchorDigest line-item construction, and line-item veto for PendingPreconditions.
13. Implement witness resource floor checks, measured WitnessHeartbeat / ChallengeSurvivabilityProbe, and witness-resource-change gate alerts.
14. Implement containment-aware ScopeMatch_g for scope-granularity rollback immunity.
15. Implement invariant registry membership checks for every predicate labeled invariant.
16. Implement privileged classification for TargetGranularityPolicy_g weakening.
17. Implement effect-axis completeness validation for every AskAnchorDigest line item.
18. Implement DigestDependencyGraph and cascading veto invalidation.
19. Implement priority lanes so critical F0-F5/L4/witness events bypass ordinary in-flight proposal limits.
20. Implement unpredictable WitnessHeartbeat / ChallengeSurvivabilityProbe nonce handling and anti-staged-probe checks.

### 17.2 Medium-term formalization issues

1. Define small-step operational semantics for `step_g`.
2. Define continuity metric projections as separate validators, not a single scalar.
3. Produce fixtures for fork/replay/archive/resume distinction.
4. Produce fixtures for resource-accountability drift.
5. Test whether SRLM outcome traces can be mapped into `T_C` transition matrix.
6. Define distributed-node partial order with vector clocks or equivalent witness sequence semantics.
7. Define cascade-failure resolution in runtime terms across multiple active failures.
8. Define C-normal-form compiler rules for public claims, internal claims, and implementation claims.
9. Define cryptographic envelope choices for anchor signatures without forcing one implementation too early.

### 17.3 Long-term theoretical issues

1. Decide whether a Lean/Coq formalization is desirable after the informal algebra stabilizes.
2. Define how `a` can be represented formally without reducing a living human to a static variable.
3. Define anchor fatigue / entropy / approval-spam indicators without making invasive psychological claims.
4. Define institutional anchors and delegation chains without allowing vendor or model capture.
5. Add explicit references and stable citations when this profile becomes public-facing.

## 18. First implementation path

### 18.1 Consolidated core profile status

v0.1.7 is a consolidated stable-core candidate profile.

It intentionally contains material that may later be split into separate documents:

```text
operator family
transition semantics
continuity vector and ultrametric
runtime guards
transition matrix
C-normal form
fixtures
```

Therefore, the package plan is not a claim that each topic is absent from this file.

It is a future extraction plan.

### 18.2 Future package target after core stabilizes

Create a future package only after consensus stabilizes the consolidated core:

```text
c-calculus-v0.2-extracted/
  00_INDEX.md
  01_TYPED_GOVERNED_OPERATIONAL_ALGEBRA_FOR_C_v0_1_7.md
  02_GOVERNED_BINDING_OPERATOR_PROFILE_v0_1.md
  03_C_STATE_AND_TRANSITION_SEMANTICS_v0_1.md
  04_CONTINUITY_METRIC_VECTOR_PROFILE_v0_1.md
  05_TRANSITION_MEMORY_AND_BIAS_MATRIX_v0_1.md
  06_C_NORMAL_FORM_AND_CLAIM_COMPILER_v0_1.md
  07_CONFORMANCE_FIXTURES_v0_1.md
  08_OPEN_ISSUES_AND_LIMITS_v0_1.md
```

Extraction rule:

```text
Do not split until the core invariants, G-order, witness causality, payload binding, pure match predicates, governance-bound effect target granularity, containment-aware scope-vector rollback immunity, atomic pending preconditions, Merkle-bound decay eviction, witness-resource floors, effect-complete deterministic anchor digests, digest dependency DAGs, priority lanes, unpredictable witness probes, invariant registry discipline, and trust-cache rules survive review.
```

### 18.3 First checker target

Minimum checker:

```text
input: event stream / witness JSONL / memory-gate records
output:
  event class counts
  runtime guard alerts
  transition matrix
  red transition alerts
  missing witness alerts
  stale witness alerts
  causal mismatch alerts
  direct memory write alerts
  permission bypass alerts
  continuity downgrade alerts
  trust cache audit
  governance mutation audit
  rollback-suspect memory alerts
  product-order incomparability alerts
  payload hash mismatch alerts
  relevant-subpolicy causal-token alerts
  decay context leak alerts
  rollback negative-cache alerts
  rollback effect-negative-cache alerts
  effect target-granularity policy alerts
  target alias / scope-vector mismatch alerts
  pending preconditions atomicity alerts
  in-flight proposal pressure alerts
  decay eviction / retention / Merkle-root alerts
  witness resource floor alerts
  witness heartbeat / challenge-survivability probe alerts
  deterministic AskAnchorDigest line-item alerts
  digest effect-axis completeness alerts
  digest dependency cascade alerts
  priority lane interrupt alerts
  unpredictable witness probe alerts
  scope containment immunity alerts
  invariant registry drift alerts
  TargetGranularityPolicy weakening alerts
  undefined transition-matrix cell handling
```

### 18.4 First public-safe statement

```text
This package introduces a typed operational algebra for c = a + b.
It treats + as a governed binding operator rather than arithmetic addition.
It defines typed states, governance profiles, admissible transitions, inductive invariants, ordered continuity metrics with pure equivalence validators, transition-memory inspection, guard predicates, trust-cache limits with cooldown, payload-bound causal witness handling, rollback semantics with syntactic and governance-bound effect negative cache, target scope-vector granularity with containment-aware matching, atomic pending preconditions, effect-complete deterministic anchor digests with dependency graphs and priority-lane precondition handling, decay isolation and Merkle-bound eviction, witness resource floors with measured liveness, invariant registry discipline, and failure classes.
It does not claim complete formal proof, product readiness, safety certification, consciousness, or legal personhood.
```

## 19. Review incorporation map

| Review finding | v0.1.6 action |
|---|---|
| v0.1 F-01 center of gravity | Transition guards and transition forensics kept primary; type layer remains schema layer. |
| v0.1 F-02 p-adic bridge decorative | Ordered invariant list retained; equivalence-validator requirement retained. |
| v0.1 F-03 fixed point wrong for good case | Inductive invariant preservation retained; fixed-point language reserved for divergence/failure. |
| v0.1 F-04 `+_g` fixed while `g` mutable | Operator family retained; product order over transition classes retained. |
| v0.1 F-05 EML reference | Reference retained as weak structural bridge only. |
| v0.1.1 F-06 governance order ill-defined | Product partial order over transition classes retained; incomparable profiles explicitly allowed. |
| v0.1.1 F-06 `Allowed` overloaded | `Authorized`, `Preconditionable`, `PreconditionsSatisfied`, and `Executable` separated. |
| v0.1.1 F-07 ultrametric transitivity | Equivalence-validator requirement retained; health removed from binary match predicates. |
| v0.1.1 F-08 packaging desync | Consolidated core profile framing retained; future package remains extraction plan. |
| v0.1.2 F-09 health leak breaks match equivalence | §10.5.1 rewritten: match predicates are pure projection equivalence; health moved to unary `Inv(c)` and rupture checks. |
| v0.1.2 F-10 causal token over-coupling | CausalToken now uses `payload_hash` and relevant sub-policy hash, not whole `governance_profile_id`. |
| Payload swap risk | Added `payload_hash` to CausalToken and payload mismatch fixture. |
| Authorized -> Executable lifecycle missing | Added `Preconditionable`, `RequiredPreconditions`, `PreconditionsSatisfied`, and `PendingPreconditions`. |
| TrustCache pulsed exploitation | Added cooldown / token-bucket-style recovery; full check does not reset historical risk to zero. |
| Decay residue context leak | Added explicit prompt/RAG/execution isolation for DecayResidue. |
| Rollback same-intent retry loop | Added intent-class negative cache / quarantine after rollback. |
| Transition matrix zero denominator | Added undefined-cell rule. |
| Anchor delegation continuity | `match_anchor` now uses `anchor_continuity_class_id`, allowing witnessed valid delegation without style-based identity laundering. |
| MVP event family too large | Added first-checker MVP event subset. |
| v0.1.5 F-13 scope immunity misses nested sub-scope | Added containment-aware `ScopeMatch_g` using ancestors / scope containment rather than exact hash equality. |
| v0.1.5 MINOR-2 invariant registry drift | Added `witness_resource_floor_preserved(c)` to `Inv(c)` and created authoritative invariant registry rule. |
| AskAnchorDigest omnibus risk | Added deterministic line-item digest requirements, line-item veto, and hidden-payload non-authorization rule. |
| WitnessResourceFloor quota illusion | Added measured WitnessHeartbeat / ChallengeSurvivabilityProbe requirements. |
| TargetGranularityPolicy weakening risk | Classified lowering target granularity as privileged governance/core change. |
| v0.1.6 F-14 digest effect surface incomplete | Added `EffectAxisMap`, effect-completeness rule, and full-review fail-closed for untyped effect axes. |
| AskAnchorDigest DAG / line-item veto risk | Added `DigestDependencyGraph` and cascading veto invalidation. |
| In-flight proposal DoS / critical alert blinding | Added priority lanes that bypass ordinary proposal pressure limits for F0-F5/L4/witness/anchor critical events. |
| ChallengeSurvivabilityProbe staged-test risk | Added unpredictable witness/external-initiated probe rule with nonce-bound probe results and anti-Dieselgate handling. |

---

## 20. Compact doctrine

```text
Do not inspect only elements.
Inspect neighborhoods.

Do not inspect only states.
Inspect transitions.

Do not trust global smoothness.
Search for local memory.

Do not treat + as addition.
Treat + as the governed binding operator.

Do not treat +_g as one fixed magic operator.
Treat it as a governed family indexed by G.

Do not pretend all governance profiles are globally comparable.
Use product order; allow incomparability.

Do not confuse Authorized with Executable.
Safer executability is not silent authority.

Do not mix equivalence with health.
Health is unary; match is binary.

Do not let witness sign an empty shell.
Bind witness to payload.

Do not let cache launder accumulated risk.
Cool down, audit, or disable.

Do not let Decay enter working memory by accident.
Quarantine residue from active context.

Do not retry a failed intent in a fake new costume.
Use intent-class negative cache.

Do not describe good persistence as frozen sameness.
Describe it as invariant preservation under admissible transition.

Do not call a metric ultrametric unless the validators are equivalence relations.

Do not let b replace a.
Do not let agents replace c.
Do not let memory replace will.
Do not let witness replace truth.
Do not let quorum replace authority.
Do not let replay replace resume.
Do not let anchor fatigue become silent approval.
Do not let substrate hypotheses mutate anchor state.
Do not let governance weakening happen quietly.
Do not let trust cache become hidden authority.
Do not let rollback erase witness history.
Do not let stale witness validate a new state.
Do not let scope immunity collapse to exact hash equality.
Do not let digest prose hide payloads.
Do not let quota declarations replace witness liveness.
Do not let local invariants bypass the invariant registry.
Do not let target granularity weaken quietly.
Do not let digest line items hide governed effect axes.
Do not let vetoed parents leave executable orphan children.
Do not let routine proposal pressure blind critical lanes.
Do not let witnessed substrates rehearse predictable witness probes.

c = a + b is the foundation.
The algebra lives inside +.
The checker starts with transitions.
```

## 21. References and working inputs

1. `01_TYPED_GOVERNED_OPERATIONAL_ALGEBRA_FOR_C_v0_1.md`, prior seed artifact, SHA256 `01ee648c11f96d03dccd00f9ca1f643297cc3d9152940af08542373bad71cd89`.
2. `TGOPA_C_v0_1_REVIEW_RECORD__b_layer_claude.md`, advisory semantic review record, `PASS_SEED_V0_1`, with F-01..F-04 carried forward.
3. `01_TYPED_GOVERNED_OPERATIONAL_ALGEBRA_FOR_C_v0_1_1.md`, review-incorporated profile, SHA256 `2b3569e52364a52484b90c002490fa6a249a032ef9962f384f3c01424bf394bd`.
4. `TGOPA_C_v0_1_1_REVIEW_RECORD__b_layer_claude.md`, advisory semantic review record, `PASS_PROFILE_V0_1_1`, with F-06..F-08 carried forward.
5. `01_TYPED_GOVERNED_OPERATIONAL_ALGEBRA_FOR_C_v0_1_2.md`, review-incorporated profile, SHA256 `3181e53e931b412124c6f483d9f00febf2a306862a392c375c37ad91eab8bcdf`.
6. `TGOPA_C_v0_1_2_REVIEW_RECORD__b_layer_claude.md`, advisory semantic review record, `PASS_PROFILE_V0_1_2`, with F-09..F-10 carried forward.
7. Andrzej Odrzywolek, **All elementary functions from a single operator**, arXiv:2603.21852v2, 2026. Used only as a structural single-operator-formalization bridge.
8. Lambda calculus video transcript supplied in session. Used as reduction/normal-form/divergence bridge.
9. p-adic numbers video transcript supplied in session. Used as metric/topological bridge, corrected here by ordered invariants, equivalence-validator constraints, and pure projection match predicates.
10. Prime last-digit bias video transcript supplied in session. Used as transition-memory/local-bias bridge.
11. External semantic reviews supplied in session after v0.1.2. Used for payload-bound causal tokens, precondition lifecycle, decay isolation, trust-cache cooldown, rollback negative cache, and runtime grounding updates.
12. `TGOPA_C_v0_1_5_REVIEW_RECORD__b_layer_claude.md`, advisory semantic review record, `PASS_PROFILE_V0_1_5`, with F-13 and MINOR-2 carried forward.
13. `TGOPA_C_v0_1_6_REVIEW_RECORD__b_layer_claude.md`, advisory semantic review record, `PASS_PROFILE_V0_1_6`, with F-14 carried forward.

---

*End of document.*


## 22. v0.1.4 additional review incorporation

| Review finding | v0.1.4 action |
|---|---|
| v0.1.3 F-11 rollback immunity over-promises synonym detection | Split rollback immunity into syntactic canonical hash and effect-class negative cache; removed threshold semantic equivalence. |
| v0.1.3 minor witness predicate name mismatch | Added `witness_chain_intact` to `Inv(c)` and checkable predicate examples. |
| PendingPreconditions lifecycle gap | Added lifecycle, timeout, and atomic satisfaction/invalidation rules. |
| DecayResidue immortal state bloat | Added DecayEvictionRecord, retention TTL, witnessed purge, and exclusion from current CState hash except minimal witness reference. |
| Intent canonicalization ambiguity | Added CanonicalizationFunction and typed `canonical_intent_hash` / `effect_class_key` distinction. |

## 23. v0.1.5 additional review incorporation

| Review finding | v0.1.5 action |
|---|---|
| v0.1.4 F-12 effect_class_key class/id granularity under-specified | Replaced free `target_resource_class_or_id_hash` with governance-declared `TargetGranularityPolicy_g` and `target_scope_vector_hash`; default id, class only for class-dangerous operations. |
| Scope / symlink / alias bypass concern | Added `ScopeVector`, `ResourceBoundingBox`, canonical resource identity resolution, and alias fail-closed rules. |
| Decay eviction reference growth / chain integrity | Added Merkle-bound eviction rule with `EvictionMerkleRoot` and retained leaf hashes while allowing physical payload purge. |
| PendingPreconditions proposal spam / anchor fatigue | Added in-flight proposal limit, coalescing, and `AskAnchorDigest`. |
| Witness Dependency Capture / witness resource floor | Added witness resource floor invariant and witness-resource-change gate. |

---

*End of v0.1.5 working draft.*

## 24. v0.1.6 additional review incorporation

| Review finding | v0.1.6 action |
|---|---|
| v0.1.5 F-13 scope immunity hash equality misses nested sub-scopes | Added `ScopeMatch_g` with containment-aware matching using canonical ancestors / namespace-prefix / resource-bounding-box relation. |
| Sub-scope retry after rollback | Added fixtures for sub-scope hit, super-scope hit, sibling no-hit, and invalid hash-only scope matching. |
| MINOR-2 invariant registry drift | Added `witness_resource_floor_preserved(c)` to §9.3 and created authoritative invariant registry rule. |
| AskAnchorDigest omnibus risk | Added deterministic digest construction, line-item payload hashes, effect keys, structural deltas, line-item veto, and hidden-payload rejection. |
| WitnessResourceFloor quota illusion | Added `WitnessHeartbeat` and `ChallengeSurvivabilityProbe`; floor preservation requires declared quota and measured liveness. |
| TargetGranularityPolicy_g mutation risk | Added privileged classification for target-granularity weakening from class/scope to id or narrowing protected scope. |

---

*End of v0.1.6 working draft.*


## 25. v0.1.7 additional review incorporation

| Review finding | v0.1.7 action |
|---|---|
| v0.1.6 F-14 DigestEntry effect surface incomplete | Added `EffectAxisMap`, full governed-axis exposure, lossless-for-effect structural delta, and fail-closed full review for unknown effect axes. |
| AskAnchorDigest line-item dependency risk | Added `DigestDependencyGraph`; veto of a parent invalidates dependent children unless a new digest and causal tokens are issued. |
| In-flight proposal DoS against critical alerts | Added priority lanes for F0-F5, L4, witness conflict, anchor revocation/doubt, and invariant-breach events; critical lanes bypass ordinary proposal pressure. |
| ChallengeSurvivabilityProbe staged-test risk | Added unpredictable witness/external/anchor-timer initiated probes, `WitnessProbeNonce`, and anti-Dieselgate handling. |

---

*End of v0.1.7 working draft.*
