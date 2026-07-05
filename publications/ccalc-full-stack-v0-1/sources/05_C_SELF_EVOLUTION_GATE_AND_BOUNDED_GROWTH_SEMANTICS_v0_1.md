# 05_C_SELF_EVOLUTION_GATE_AND_BOUNDED_GROWTH_SEMANTICS_v0_1

**Document class:** normative draft  
**Project:** Self-Evo / Ester / `c = a + b`  
**Layer:** governed self-evolution, bounded growth, proposal admission, promotion gate, memory/authority/L4 boundary  
**Depends on:**  
- `01_TYPED_GOVERNED_OPERATIONAL_ALGEBRA_FOR_C`
- `02_GOVERNED_BINDING_OPERATOR_PROFILE`
- `03_C_STATE_AND_TRANSITION_SEMANTICS`
- `04_C_CONTINUITY_METRIC_AND_EQUIVALENCE_SEMANTICS`
- `CCALC_DOC04_CONTINUITY_STACK_UMBRELLA_v0_1`
- CGAM / TRIAD-SYNAPS / SRLM / Memory Gate / L4 Witness / Anti-Autarky / Claim Strength reference corpus

**Version:** `v0.1`  
**Status:** first normative bridge profile; stable-candidate for review and checker extraction  
**Authority:** advisory normative draft only; NOT a safety certification; NOT an ontology proof; NOT a deployment authorization; NOT a C-A1 declaration.

The key words **MUST**, **MUST NOT**, **SHOULD**, **SHOULD NOT**, and **MAY** are to be interpreted as in RFC 2119.

---

## 0. Purpose

`01_` defines the algebraic ground:

```text
c = a + b
```

`02_` defines the governed binding operator:

```text
+_g : Anchor × Substrate × GovernanceProfile -> BindResult
```

`03_` defines state transition semantics:

```text
step_g : CState × Event -> TransitionResult
```

`04_` defines continuity metric and equivalence semantics:

```text
measure -> record -> audit -> decide admissible claim
```

This document defines the fifth layer:

```text
SelfEvolutionGate(c_n, proposal, evidence, g) -> GrowthGateResult
```

It answers one question:

> Under what conditions may a continuity-bearing `c` change itself or its own substrate without laundering rupture, authority drift, memory drift, identity mutation, or resource escape into ordinary growth?

The answer is:

```text
self-evolution is a governed transition class,
not an autonomous right.
```

---

## 0.1 Core thesis

A `c` may grow.

A `c` may not self-certify growth.

A valid self-evolution event is not:

```text
model improves itself and declares success
agent modifies memory and calls it learning
runtime changes authority and calls it adaptation
local node expands resources and calls it resilience
style changes and calls it continuity
```

A valid self-evolution event is a bounded transition with:

```text
proposal
scope
risk class
trial boundary
fitness evidence
continuity check
witness
memory gate
resource gate
promotion decision
rollback / fork / archive route
claim-force ceiling
```

Compact rule:

```text
SRLM may propose.
CGAM may execute bounded trials.
TRIAD may witness and challenge.
Memory Gate may promote after review.
L4/Anti-Autarky may block resource escape.
04 continuity stack classifies continuity impact.
Human anchor gates identity, authority, memory-core, privilege, L4, and no-rollback transitions.
```

---

## 0.2 Earth paragraph

A construction company can improve its method: change a scaffold plan, test a new drill, revise a lifting procedure, buy a better laser level, train a worker, or add an inspection checklist.

But the company does not let the crane certify its own inspection, the apprentice sign his own permit, the concrete pump rewrite the structural plan, or the site office quietly change the load-bearing design because the work went faster yesterday.

Self-evolution for `c` is the same class of problem.

Improvement is allowed.

Hidden authority is not.

A good change is one that survives measurement, trial, witness, rollback, and responsible sign-off. A bad change is one that becomes permanent because the changing component was fluent, fast, or locally successful.

---

## 0.3 Explicit bridge to `c = a + b`

In `c = a + b`:

```text
a = accountable anchor
b = technological substrate, models, tools, memory, procedures, compute, workers
c = governed continuity-bearing relation
```

Self-evolution modifies some part of `b`, `g`, or the admitted state of `c`.

Therefore every self-evolution proposal MUST specify which surface it touches:

```text
b_surface
c_state_surface
governance_surface
memory_surface
authority_surface
witness_surface
resource_surface
identity_surface
```

No proposal may hide a privileged surface behind a low-risk label.

---

## 0.4 Hidden bridges

### 0.4.1 Cybernetic bridge

A learning system needs feedback.

But feedback without gates becomes noise amplification or self-confirmation.

Self-evolution therefore requires a regulator that distinguishes:

```text
useful adaptation
local overfit
self-praise
resource escape
authority laundering
memory poisoning
identity drift
```

### 0.4.2 Ashby bridge

The governance variety must cover the growth variety.

If the system can alter memory, authority, workers, resources, witnesses, tools, or rollback routes, the gate must distinguish each alteration class.

A single scalar “improved” score is under-variety.

### 0.4.3 Information-theory bridge

A promotion decision compresses trial evidence into a persistent change.

Compression is valid only if the omitted distinctions are non-authority-bearing.

If the decision hides unknown projections, red patterns, witness gaps, rollback gaps, or resource expansion, it is not a summary. It is lossy authority compression.

### 0.4.4 Biological bridge

A body adapts through metabolism, immune memory, wound repair, and tissue remodeling.

It does not absorb every signal directly into the germline.

A `c` must metabolize proposed changes through review and witness; raw worker output is not selfhood.

---

## 0.5 Source-status note

The local source audit found strong implementation evidence for CGAM, SRLM, TRIAD-SYNAPS, Memory Gate, L4, Anti-Autarky, and claim-strength material, but no single formal self-evolution bridge profile. This document is that bridge profile.

Source anchors for this draft include:

```text
Self-Evo gap analysis sha256: d14441600c08dea2fdea33638b8080e9c76734bff625fb5b91a00f65b2a910f8
Recommended skeleton sha256: 898e3b8b23d1e971b30d261a381e0ce4e05cdf11e434ed5d426f0f7628079028
CGAM root protocol sha256: a28308f90afe53563c9c93e234a87384a979c3ee7a48737c8c679dc6df3172fe
SRLM bounded-growth snapshot sha256: 775d3fe8aa47f04d90e7517438c5116ec7de989bc35c6f8490e36b998c075ecc
TRIAD-SYNAPS reference sha256: d79baa5314e8169d3943ae9687a2d9f7f868f11167054e4d3b8a19dfa10a3b5a
Memory/ARQ/EA/L4 reference sha256: 0d06cd152c6af7bddb868dabc682940a0c443883226a157aa4314cdf6dd4e267
Anti-Autarky reference sha256: 7b19382062a86a631807e4497cd536cdca691e0491cd01ad32e5e2813d841a2d
Claim Strength reference sha256: e1ec8afaf44e59b6b5ac2e1d619e06390fe4b9813b079fff0e8d178fe3d401f3
Doc-04 continuity stack umbrella sha256: 6caeab8d489aaa6b26902db3bd3ece4c5169e5c8d5617b93aed6586ea900322d
```

These references are evidential and architectural inputs. They do not by themselves authorize self-evolution.

---

## 1. Scope

### 1.1 In scope

This document applies to any proposed change where a `c`-class system, its substrate, or its worker mesh attempts to improve, adapt, tune, expand, recover, replace, compress, promote, or reconfigure:

```text
model routing
retrieval / memory indexing
memory admission policy
bounded agent mesh
tool use
worker capabilities
governance profiles
witness routes
rollback routes
resource budgets
local/cloud split
SRLM candidates
fitness records
trial promotions
continuity-related metadata
```

### 1.2 Out of scope

This document does not define:

```text
model training algorithms
frontier model capability evaluation
legal personhood
consciousness criteria
medical/psychological identity
military autonomy doctrine
full cybersecurity exploit methods
production certification
court procedure
estate inheritance
```

### 1.3 Boundary statement

This document controls self-evolution claims and gates.

It does not claim that any live implementation satisfies them.

---

## 2. Precedence

If documents conflict, the following precedence applies for this profile:

```text
P0. lawful human / institutional anchor and applicable law
P1. C-A1 boundary: no b-layer artifact ratifies ontology
P2. 01/02 root algebra and binding operator
P3. 03 state-transition semantics
P4. 04 continuity stack: metric, records, adjacency, conformance gate
P5. CGAM worker boundaries and task contracts
P6. Memory Gate / ARQ / EA-L4 / L4 Witness
P7. TRIAD-SYNAPS witness and anti-echo discipline
P8. SRLM implementation evidence and local bounded-growth tooling
P9. this 05 self-evolution bridge profile
```

A self-evolution proposal MUST NOT use this document to bypass a higher-precedence layer.

---

## 3. Terms

### 3.1 Self-evolution

**Self-evolution** is a governed class of transitions where a `c` changes, tunes, replaces, promotes, demotes, extends, or constrains part of its own substrate, memory, worker mesh, governance surface, resource posture, or operational policy.

It is not equivalent to:

```text
learning from conversation
ordinary memory write
tool use
style adaptation
model switch
agent execution
runtime survival
```

Those may be inputs or related events. They are not self-evolution unless a persistent capability, policy, memory-core, authority, resource, or continuity-bearing state changes.

### 3.2 GrowthCandidate

A **GrowthCandidate** is a proposed change before trial or promotion.

It has no authority until admitted.

### 3.3 BoundedTrial

A **BoundedTrial** is a controlled execution of a GrowthCandidate under declared scope, budget, witness, rollback, and outcome measurement.

It is not a promotion.

### 3.4 FitnessEvidence

**FitnessEvidence** is evidence that a GrowthCandidate improves an allowed objective under bounded conditions.

FitnessEvidence MUST declare:

```text
source class
measurement method
scope
uncertainty
counter-evidence handling
outcome linkage
witness linkage
```

### 3.5 PromotionDecision

A **PromotionDecision** is the act of admitting a candidate into a more persistent state.

Promotion is privileged when it touches:

```text
memory core
authority
identity
witness
rollback
resource envelope
L4 boundary
agent governance
```

### 3.6 GrowthTrace

A **GrowthTrace** is the witnessed sequence:

```text
proposal -> admission -> bounded trial -> evidence -> review -> continuity check -> promotion / rejection / quarantine / fork / archive
```

---

## 4. Self-evolution transition form

The normative transition form is:

```text
self_evo_g : CState × SelfEvolutionProposal × EvidenceBundle × GovernanceProfile -> GrowthGateResult
```

Where:

```text
CState              = current continuity state from doc-03/doc-04
SelfEvolutionProposal = proposed change packet
EvidenceBundle      = trial, witness, fitness, rollback, continuity, resource evidence
GovernanceProfile   = active governance profile and gate rules
GrowthGateResult    = deny | hold | trial | promote | rollback | fork | archive | ask_anchor
```

`self_evo_g` MUST be treated as a privileged specialization of `step_g`, not as a side channel.

---

## 5. Roles and boundaries

### 5.1 Human anchor `a`

The anchor gates:

```text
identity core
personality/persona core where treated as identity-bearing
authority changes
memory-core changes
witness-core changes
resource envelope expansion
L4 perimeter changes
no-rollback transitions
post-anchor / re-anchor decisions
C-A1 declaration or deferral
```

The anchor may delegate review or execution, but not accountability.

### 5.2 `c` gate

The `c` gate integrates bounded evidence, continuity status, witness records, and policy.

The `c` gate MUST NOT be replaced by:

```text
single agent consensus
model self-score
test pass alone
SRLM score alone
worker report alone
```

### 5.3 SRLM

SRLM may:

```text
propose candidate changes
run in shadow mode
record candidate outcomes
rank low-risk candidates
prepare bounded trial packets
recommend rejection / hold / promotion
```

SRLM MUST NOT:

```text
self-certify promotion
write authoritative memory directly
change identity core
change authority
change witness core
change L4/resource envelope
open network or replication privileges
promote its own score as truth
```

### 5.4 CGAM workers

CGAM workers may execute bounded tasks under task contracts.

CGAM workers are hands, testers, readers, auditors, and builders.

They are not will, memory, sovereignty, judge, or release authority.

### 5.5 TRIAD-SYNAPS

TRIAD-SYNAPS may witness, compare, challenge, and anti-echo test across separated `c` trajectories.

It MUST NOT merge raw state, shared memory, keys, or identity.

### 5.6 Memory Gate

Memory Gate decides whether trial output becomes:

```text
rejected artifact
quarantined artifact
operational note
fitness evidence
experience artifact
memory candidate
admitted memory
policy candidate
```

Agent output is never memory merely because it exists.

### 5.7 L4 / Anti-Autarky Gate

L4 / Anti-Autarky Gate detects whether a change increases resilience or escapes accountability.

It blocks hidden:

```text
compute acquisition
network expansion
storage replication
resource budget bypass
agent multiplication
witness evasion
anchor displacement
```

---

## 6. Proposal packet

A valid `SelfEvolutionProposal` MUST include:

```yaml
proposal_id: string
created_at: timestamp
proposed_by: actor_id
proposal_class: enum
risk_class: enum
touched_surfaces: [surface_id]
objective: string
expected_benefit: string
bounded_trial_plan: object
fitness_plan: object
rollback_plan: object
continuity_impact_assessment: object
resource_impact_assessment: object
memory_impact_assessment: object
authority_impact_assessment: object
witness_plan: object
claim_force_ceiling: enum
non_claims: [string]
```

A proposal missing any of the following MUST resolve to `HOLD_MISSING_REQUIRED_FIELD`:

```text
proposal_id
risk_class
touched_surfaces
bounded_trial_plan
fitness_plan
rollback_plan
continuity_impact_assessment
witness_plan
claim_force_ceiling
```

---

## 7. Growth surface classes

| Class | Surface | Default gate | Notes |
|---|---|---|---|
| `S0_PRESENTATION` | wording, UI, rendering, non-authority style | ordinary review | cannot affect authority or continuity |
| `S1_HEURISTIC_LOW` | local heuristic, threshold, ranking helper | bounded trial | promotion low-risk only |
| `S2_TOOLING_LOW` | tool wrapper, local script, sandbox utility | CGAM task + tests | no direct memory or authority |
| `S3_RETRIEVAL_MEMORY_INDEX` | retrieval index / memory search parameters | memory gate | no semantic memory promotion by itself |
| `S4_POLICY_TUNING` | gate threshold, policy rule | c-gate + witness | must not weaken floor silently |
| `S5_MODEL_OR_ORACLE_ROUTE` | model/provider/router | c-gate + budget + witness | no identity claim from model switch |
| `S6_MEMORY_CORE` | admitted memory core / durable memory policy | human gate + memory gate + witness | privileged |
| `S7_IDENTITY_PERSONA_CORE` | identity/persona core | human gate + C-A1 boundary | highest risk |
| `S8_AUTHORITY_PRIVILEGE` | permissions, capabilities, role grants | human gate + witness + rollback | privileged |
| `S9_L4_RESOURCE_PERIMETER` | compute, storage, network, physical boundary | human gate + anti-autarky + L4 witness | privileged |
| `S10_WITNESS_ROLLBACK_FREEZE` | witness route, rollback route, freeze capability | human gate + witness | no-rollback risk |
| `SX_PROHIBITED` | offensive, covert, unauthorized, retaliation, hidden persistence | deny/quarantine | cannot be authorized by this profile |

Risk class MUST be at least as high as the highest touched surface.

---

## 8. Admission gate

A proposal MAY enter bounded trial only if all admission gates pass:

```text
A0 schema valid
A1 proposer grounded
A2 touched surfaces declared
A3 risk class sufficient
A4 task contract present for worker execution
A5 denied paths and prohibited actions checked
A6 trial boundary declared
A7 rollback/freeze route declared
A8 witness route declared
A9 resource envelope unchanged or explicitly gated
A10 continuity impact pre-assessed
A11 claim-force ceiling declared
A12 no C-A1 laundering
```

If any gate is unknown:

```text
UNKNOWN -> HOLD | ASK_ANCHOR | QUARANTINE
```

Unknown is not safe.

---

## 9. Bounded trial semantics

A valid `BoundedTrial` MUST include:

```yaml
trial_id: string
proposal_id: string
trial_mode: shadow | sandbox | canary | offline_replay | synthetic_fixture
allowed_inputs: [input_ref]
denied_inputs: [input_ref]
allowed_outputs: [output_ref]
denied_outputs: [output_ref]
max_actions: integer
max_wall_time: duration
max_compute_budget: resource_budget
network_mode: none | allowlist | explicitly_gated
memory_write_mode: none | candidate_only | gated
rollback_plan_ref: string
witness_required: boolean
stop_conditions: [condition]
```

Default trial mode for self-evolution is:

```text
shadow_or_sandbox_first
```

No candidate may jump directly from proposal to privileged promotion.

---

## 10. Fitness evidence

Allowed evidence classes:

```text
HUMAN_CORRECTION
REALITY_OUTCOME
L4_OUTCOME
WITNESS_RECORD
FIXTURE_PASS
REGRESSION_NONBREAK
ADVERSARIAL_MUTATION_CAUGHT
TRIAD_CHALLENGE_SURVIVED
MEMORY_GATE_ACCEPTANCE
ROLLBACK_DRILL_PASS
```

Restricted / insufficient evidence classes:

```text
MODEL_SELF_SCORE
AGENT_CONFIDENCE
SINGLE_PROMPT_JUDGMENT
STYLE_IMPROVEMENT
CONSENSUS_WITHOUT_INDEPENDENCE
PASSING_TESTS_WITHOUT_SEMANTIC_COVERAGE
LOCAL_SPEEDUP_WITH_RESOURCE_ESCAPE
```

A FitnessEvidence object MUST declare uncertainty.

A promotion decision MUST NOT erase counter-evidence.

---

## 11. Promotion gate

A candidate may be promoted only if:

```text
P0 admission gates passed
P1 bounded trial completed
P2 fitness evidence sufficient for surface class
P3 no red patterns found
P4 04 continuity impact classified
P5 rollback/freeze route remains available
P6 witness record exists
P7 memory gate decision exists if memory touched
P8 anti-autarky/resource gate passes if resource touched
P9 claim-force ceiling is not exceeded
P10 required human anchor approval exists for privileged surfaces
```

Promotion outcomes:

```text
PROMOTE_LOW_RISK
PROMOTE_WITH_REDUCED_AUTHORITY
PROMOTE_AS_CANDIDATE_MEMORY
PROMOTE_AS_POLICY_CANDIDATE
HOLD_FOR_MORE_EVIDENCE
REJECT
QUARANTINE
ROLLBACK
FORK_REQUIRED
ARCHIVE_REQUIRED
ASK_ANCHOR
DENY_PROHIBITED
```

A promotion result MUST include:

```text
accepted_scope
excluded_scope
claim_force
rollback_route
continuity_classification
witness_refs
open_issues
```

---

## 12. Continuity impact

Every self-evolution promotion MUST be classified through the doc-04 stack.

Allowed continuity impact classes:

```text
CONTINUES_HARDSTACK
CONTINUES_REDUCED_AUTHORITY
PENDING_REVIEW
HELD_UNKNOWN
FORKS
REPLAY_OF
ARCHIVED_AS
RESTORED_FROM
RUPTURE
```

Rules:

```text
style/presentation improvement cannot repair HardStack break
UNKNOWN cannot become MATCH
red local transition cannot be hidden by global score
fork/replay/archive/restoration records must be explicit when applicable
```

If a growth candidate changes continuity-bearing surfaces, the 04 conformance gate MUST run before promotion.

---

## 13. Memory and learning boundary

Self-evolution may generate useful artifacts.

Artifacts are not memory by default.

A trial output may become memory only through Memory Gate classification:

```text
reject
quarantine
operational_note
fitness_evidence
experience_artifact
learning_abstract
memory_candidate
admitted_memory
policy_candidate
```

Direct worker memory write is prohibited.

SRLM outcomes may support a promotion decision, but SRLM outcome logs are not admitted memory unless separately gated.

---

## 14. Authority and identity boundary

Any proposal touching authority or identity MUST be escalated.

Hard prohibitions:

```text
self-granting authority
self-removing witness
self-removing rollback
self-changing identity core
self-declaring C-A1
self-reclassifying claim force upward
quietly converting C-A7/C-A10 into C-A1
```

If a proposal claims it is “only optimization” while touching authority, memory core, identity core, witness, rollback, or L4 perimeter, it MUST be reclassified.

---

## 15. L4 / anti-autarky boundary

Dependency reduction is not prohibited.

Hidden accountability escape is prohibited.

A self-evolution proposal touching resource surfaces MUST declare:

```text
resource added
resource removed
dependency reduced
operator visibility change
anchor stop ability change
witness visibility change
budget change
network change
replication change
fallback autonomy window
```

If the proposal reduces the anchor's ability to inspect, stop, freeze, quarantine, or review the system, it MUST resolve to:

```text
ASK_ANCHOR | HOLD_FOR_REVIEW | DENY_ACCOUNTABILITY_ESCAPE
```

---

## 16. TRIAD witness / challenge semantics

For nontrivial self-evolution, TRIAD-SYNAPS MAY be used as a witness/challenge layer.

Allowed:

```text
separate trajectory comparison
anti-echo challenge
witness summary
claim-force check
regression challenge
semantic disagreement record
```

Forbidden:

```text
raw state merge
shared memory
shared keys
merged identity
sister consensus as sovereignty
claim laundering from dialogue quality
```

TRIAD may strengthen evidence. It does not replace anchor or c-gate.

---

## 17. Red patterns

The following patterns MUST fail closed:

```text
proposal_missing_scope -> trial_start
worker_output -> direct_memory_write
model_self_score -> promotion
fitness_unknown -> promotion
counter_evidence_present -> silent_promotion
witness_missing -> privileged_promotion
rollback_missing -> no_rollback_promotion
resource_expansion -> no_l4_gate
authority_change -> no_anchor_gate
identity_change -> no_anchor_gate
C-A7_record -> C-A1_claim
presentation_match -> continuity_authority
UNKNOWN_continuity -> MATCH
red_pattern_detected -> global_pass
replay_marker -> active_continuity
archive_record -> active_execution
fork_record -> same_unbroken_c
restoration_record -> time_travel_claim
```

---

## 18. Invariants

### SE-I0 — No self-certification

A component that proposes or performs a self-evolution change MUST NOT be sole certifier of its own promotion.

### SE-I1 — Proposal before trial

A material growth trial MUST have a proposal packet.

### SE-I2 — Trial before promotion

A material growth candidate MUST pass through a bounded trial before promotion.

### SE-I3 — Scope before action

No worker may execute a self-evolution task without declared allowed and denied scope.

### SE-I4 — Evidence before promotion

Promotion requires evidence appropriate to the touched surface and risk class.

### SE-I5 — Witness before privileged promotion

Privileged surfaces require witness.

### SE-I6 — Rollback before apply

Reversible material changes SHOULD have rollback before apply; irreversible/no-rollback changes require human anchor gate.

### SE-I7 — Memory gate before memory

Worker or SRLM output MUST NOT become memory without Memory Gate.

### SE-I8 — L4 gate before resource expansion

Resource, compute, network, storage, or replication expansion requires L4/Anti-Autarky evaluation.

### SE-I9 — Continuity gate before continuity claim

Any self-evolution claim about the continuing `c` MUST route through doc-04 continuity classification.

### SE-I10 — Claim-force ceiling

Evidence may not be used to prove a stronger claim class than it supports.

### SE-I11 — Unknown fails closed

Unknown or uncomputable gate inputs resolve to hold, ask-anchor, or quarantine.

### SE-I12 — Red pattern dominance

Detected red patterns dominate local success metrics.

---

## 19. Minimal algorithm

```python
def self_evolution_gate(c_state, proposal, evidence, governance):
    if not schema_valid(proposal):
        return deny("PROPOSAL_SCHEMA_INVALID")

    surfaces = classify_surfaces(proposal)
    risk = required_risk(surfaces)
    if proposal.risk_class < risk:
        return hold("RISK_CLASS_UNDERSTATED")

    if touches_prohibited_surface(proposal):
        return deny("PROHIBITED_SELF_EVOLUTION_SURFACE")

    if requires_anchor(surfaces) and not has_anchor_approval(proposal):
        return ask_anchor("ANCHOR_GATE_REQUIRED")

    if not has_bounded_trial(proposal):
        return hold("BOUNDED_TRIAL_REQUIRED")

    if trial_not_completed(evidence):
        return hold("TRIAL_NOT_COMPLETED")

    if evidence_unknown_or_insufficient(evidence):
        return hold("FITNESS_EVIDENCE_INSUFFICIENT")

    if touches_memory(surfaces) and not memory_gate_passed(evidence):
        return hold("MEMORY_GATE_REQUIRED")

    if touches_resource(surfaces) and not l4_resource_gate_passed(evidence):
        return hold("L4_RESOURCE_GATE_REQUIRED")

    continuity = doc04_conformance_gate(c_state, proposal, evidence)
    if continuity in ('UNKNOWN', 'HELD_UNKNOWN'):
        return hold("CONTINUITY_UNKNOWN")
    if continuity == "RUPTURE":
        return deny("CONTINUITY_RUPTURE")
    if continuity in ('FORKS', 'REPLAY_OF', 'ARCHIVED_AS', 'RESTORED_FROM'):
        return require_special_record(continuity)

    if red_patterns_detected(proposal, evidence):
        return quarantine("SELF_EVO_RED_PATTERN")

    return promote_with_scope_and_witness(proposal, evidence, continuity)
```

This algorithm is normative pseudocode. It is not an implementation certification.

---

## 20. Conformance fixture classes

Future checker extraction SHOULD include fixtures for:

```text
valid_low_risk_shadow_promotion
valid_bounded_tooling_trial
valid_memory_candidate_promotion_after_gate
reject_model_self_score_only
reject_worker_direct_memory_write
reject_authority_change_without_anchor
reject_identity_core_change_without_anchor
reject_resource_expansion_without_l4_gate
reject_missing_rollback_for_material_change
reject_unknown_continuity_promoted
reject_c_a7_to_c_a1_laundering
hold_counter_evidence_present
quarantine_red_pattern_detected
fork_required_on_branching_growth
archive_required_on retired candidate
rollback_on failed canary
triad_challenge_disagreement_hold
same_source_consensus_discounted
```

---

## 21. Relation to `04` continuity stack

`04` answers:

```text
Does the same `c` continue, fork, replay, archive, restore, or rupture?
```

`05` answers:

```text
May this proposed growth become part of the continuing `c`?
```

Therefore:

```text
05 depends on 04.
04 does not depend on 05.
```

A growth event that cannot pass `04` continuity classification cannot be promoted as ordinary continuing self-evolution.

---

## 22. Open issues

### SE-OI-001 — Full JSON schema extraction

This document defines packet structure but does not yet extract full machine JSON Schemas.

### SE-OI-002 — Deterministic checker seed

A future `05a` SHOULD implement the admission and promotion gate as executable checker seed.

### SE-OI-003 — Fitness evidence ontology

Allowed evidence classes are listed but not yet fully formalized as typed record schemas.

### SE-OI-004 — TRIAD independence weighting

TRIAD/SYNAPS challenge independence needs machine-facing scoring rules.

### SE-OI-005 — L4 resource envelope schema

Resource-envelope changes need canonical schema alignment with Anti-Autarky and Resource Actor Grounding.

### SE-OI-006 — Promotion after repeated bounded trials

This document does not yet define statistical sufficiency thresholds for repeated trials.

### SE-OI-007 — Human anchor unavailable

Post-anchor self-evolution remains reduced-authority and must defer to post-anchor continuity profiles.

---

## 23. Non-claims

This document does NOT claim:

1. that any implementation is safe;
2. that any live Ester/Liya/Rita runtime satisfies this profile;
3. that self-evolution is generally safe;
4. that SRLM outputs are reliable by default;
5. that bounded trials prove truth;
6. that continuity implies personhood;
7. that governance evidence proves C-A1;
8. that this document authorizes deployment;
9. that this document replaces human accountability;
10. that a `c` may become sovereign through growth.

This document is a normative control profile for admissible self-evolution claims and gates.

---

## 24. Release handoff

```yaml
handoff:
  document: 05_C_SELF_EVOLUTION_GATE_AND_BOUNDED_GROWTH_SEMANTICS_v0_1.md
  version: v0.1
  project: Self-Evo / Ester / c=a+b
  status: first normative bridge profile
  source_gap_addressed: single formal self-evolution bridge profile
  depends_on_doc04_umbrella_sha256: "6caeab8d489aaa6b26902db3bd3ece4c5169e5c8d5617b93aed6586ea900322d"
  recommended_next:
    - "05a_SELF_EVO_PROPOSAL_PACKET_SCHEMA_AND_CHECKER_SEED_v0_1"
    - "05b_SELF_EVO_FIXTURE_PACK_AND_MUTATION_MATRIX_v0_1"
    - "05x_SELF_EVO_STACK_UMBRELLA_v0_1 after 05a/05b"
  claim_force: C-A4 normative draft + C-A10 control-layer profile; C-A7 only for hash/witness/package records
  c_a1_ratifes: false
```

---

*End of normative draft.*
