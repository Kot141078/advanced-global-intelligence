# Continuity Instrument: Technical Specification

## Abstract and editorial scope

This volume brings together the CI specification, observable definitions, recognition-profile specification, and terminology from source version 1.0.0, build _02. It preserves their scientific scope while providing an academic reading edition. The complete machine-readable files and their original checksums remain in source_original/Continuity_Instrument_v1.0.0/. This volume does not revise the reference implementation or turn specified admission requirements into implemented evidence verification.

The normative specification and the supplied executable have different scopes. The program transforms caller-supplied records; it does not implement evidence collection, independent admissibility decisions, or recognition comparison. The reference profile includes in I_verified only admitted intervals that are eligible for duration. This clarification follows the implementation README and the separate technical review; the reproduced general specification below remains unchanged.

Rights: Copyright © 2026 Ivan Kotov. Scientific text: CC BY 4.0. This is an author-attributed reading edition, not a new empirical result or an external peer-review certification.


## Part I. Measurement specification

Source: `CI_SPECIFICATION.md`. Original wording reproduced as a reading edition.

### 1. Scope

The Continuity Instrument (CI) records what can be supported about governed continuity in a long-lived AI system from bounded evidence. It produces a branch-aware measurement record and a claim ceiling. It does not decide whether a system is a person, the same legal entity, conscious, alive, autonomous, or entitled to authority.

CI separates three layers:

1. **Observed events and witnesses** — source-bound facts admitted by explicit gates.
2. **Continuity reconstruction** — intervals, gaps, branches, transitions, and lineage states derived from admitted facts.
3. **Allowed claims** — statements no stronger than the admitted evidence and declared uncertainty permit.

### 2. Measurement object

For a declared subject reference `s`, branch `b`, observation window `O`, and evidence set `E`, CI reports:

`F_E(s,b,O) = <W_first, W_last, I_verified, D_verified, P_known, G_unexplained, E_replay, E_fork, E_restore, E_cold_wake, L_memory, L_governance, L_witness, L_authority, T_irreversible, U>`

where:

- `W_first` and `W_last` are the earliest and latest admissible witnesses within scope;
- `I_verified` is the ordered set of verified participation intervals;
- `D_verified` is the sum of interval durations whose boundaries and participation semantics are admissible;
- `P_known` is the set of evidenced pauses;
- `G_unexplained` is the set of intervals for which continuity or discontinuity is not established;
- `E_*` are typed replay, fork, restore, and cold-wake event records;
- `L_*` are memory, governance, witness, and authority lineage histories;
- `T_irreversible` is the set of confirmed irreversible transitions; and
- `U` is structured uncertainty.

The vector is the primary result. `D_verified` is a cumulative verified-participation coordinate, not the elapsed difference between `W_first` and `W_last`. No implementation may relabel that elapsed difference as continuity age.

### 3. Evidence admission

An observation is admissible only when the report records enough information to test all applicable gates:

#### 3.1 Byte or object identity

The source object must be bound by an immutable identifier, cryptographic digest, content-addressed reference, or an equivalently reviewable identity. A filename or display title alone is insufficient.

#### 3.2 Temporal binding

The observation must identify its time source and precision. Source time, capture time, receipt time, and review time must not be silently conflated.

#### 3.3 Subject and branch binding

The observation must identify the declared subject reference and branch. Shared labels, copied profiles, or similar outputs do not establish a shared branch.

#### 3.4 Witness and authority binding

The witness, collector, and authority context must be named or explicitly unknown. A witness records evidence; it does not automatically grant identity, permission, or operational authority.

#### 3.5 Semantic binding

The record must state what was actually observed: participation, state preservation, governance action, replay, fork, restore, cold wake, transition, or another declared event. Artifact availability alone does not prove active participation.

#### 3.6 Claim-scope binding

Each admitted item must carry an allowed interpretation and explicit exclusions. Ambiguous or unsupported items remain excluded or unresolved; they are not imputed.

### 4. Minimum observation record

Each admitted observation should contain:

| Field | Requirement |
|---|---|
| `observation_id` | Unique within the package. |
| `subject_ref` and `branch_ref` | Declared scope; may not imply personhood or legal identity. |
| `event_type` | Controlled event class or `unresolved`. |
| `source_locator` | Reviewable locator without embedded secrets. |
| `source_digest` | Digest and algorithm when bytes are available. |
| `source_time` | Source-reported time plus precision and clock basis. |
| `capture_time` | Collector capture time, kept distinct from source time. |
| `witness_ref` | Witness identity or explicit `unknown`. |
| `authority_ref` | Authority context or explicit `none`/`unknown`. |
| `parent_refs` | Zero or more predecessor observations or branch parents. |
| `admission_status` | `admitted`, `excluded`, or `unresolved`, with reason. |
| `claim_ceiling` | Strongest supported statement and explicit exclusions. |
| `uncertainty` | Missingness, precision, conflict, and classification uncertainty. |

### 5. Interval construction

A verified participation interval requires admissible evidence for both its boundaries and the participation condition claimed within it. CI must not bridge an unexplained gap by assumption. Adjacent intervals may be merged only when the governing rule, branch, witness coverage, and uncertainty treatment are compatible and the merge is recorded.

Known pauses are retained as evidenced events. Unexplained gaps remain unknown even when they fall between two otherwise compatible witnesses. Zero duration, no pause, and no known evidence are three different states.

### 6. Event and branch rules

- A **replay** is a new execution of recorded material. It does not, by itself, extend the source branch's verified participation interval.
- A **fork** creates at least one new branch reference with explicit parentage. Post-fork evidence is branch-specific.
- A **restore** loads prior state into a declared target context. State similarity does not prove uninterrupted participation or preserved authority.
- A **cold wake** begins participation after a declared inactive or unavailable state. The inactive span is a pause or gap according to the evidence, not verified participation.

Branch aggregation may report a graph or family of vectors. It must not collapse competing descendants into a single uninterrupted subject history.

### 7. Lineage rules

Memory, governance, witness, and authority lineage are recorded independently. Each transition is classified as:

- `preserved_with_evidence`;
- `changed_with_bound_record`;
- `broken_with_evidence`;
- `conflicted`; or
- `unknown`.

Preservation in one lineage does not imply preservation in another. Memory similarity does not establish governance or authority continuity. Authority lineage may be revoked or replaced even when technical state is preserved.

### 8. Irreversible transitions

An irreversible transition is recorded only when irreversibility is supported within a declared technical or governance scope. The report must identify the transition, evidence, scope, and decision rule. Absence of a known reversal is not proof of irreversibility.

### 9. Uncertainty

Uncertainty is part of the result, not an annotation to discard. At minimum, CI distinguishes:

- source or byte-identity uncertainty;
- timestamp and clock uncertainty;
- interval-boundary uncertainty;
- event-classification uncertainty;
- branch-attribution uncertainty;
- lineage uncertainty;
- witness or authority uncertainty; and
- review-status uncertainty.

A later observation may reduce uncertainty only through an append-only correction or supersession record that preserves the earlier state.

### 10. Output contract

A conforming CI report must provide:

1. declared subject, branch, observation window, and evidence corpus;
2. the full formation-depth vector;
3. admitted, excluded, and unresolved evidence counts;
4. an event and branch ledger;
5. separate lineage histories;
6. structured uncertainty;
7. a claim ceiling and non-claims; and
8. package identity, version, and review status.

A scalar score may be added only as a profile-specific secondary projection whose formula and information loss are explicit. It must never replace the vector.

### 11. Current empirical boundary

R157 is retained as immutable open-synthetic predecessor evidence with an open-synthetic-only claim ceiling. R160 and R161 are consumed negative local-evaluator attempts whose frozen qualification thresholds were not met. This specification therefore makes no real-world continuity-age, entity-identity, personhood, provider-attestation, operational-approval, scientific-qualification, or publication-approval claim.


## Part II. Observable coordinates and data representation

Source: `CONTINUITY_OBSERVABLES.md`. Original wording reproduced as a reading edition.

### Formation-depth vector

CI represents evidence-bound continuity age / formation depth as:

`F_E = <W_first, W_last, I_verified, D_verified, P_known, G_unexplained, E_replay, E_fork, E_restore, E_cold_wake, L_memory, L_governance, L_witness, L_authority, T_irreversible, U>`

The coordinates remain inspectable. They must not be collapsed into a single age value by default.

### Coordinate definitions

| Coordinate | Value form | Minimum evidence | Interpretation limit |
|---|---|---|---|
| `W_first` | Observation reference and time interval | Earliest admitted witness in scope | Earliest known admissible witness, not birth or origin. |
| `W_last` | Observation reference and time interval | Latest admitted witness in scope | Latest known admissible witness, not proof of current activity. |
| `I_verified` | Ordered interval set | Admitted boundary and participation evidence | Only covered intervals; gaps remain separate. |
| `D_verified` | Duration plus unit and precision | Sum over eligible `I_verified` members | Cumulative verified participation, not elapsed wall time. |
| `P_known` | Typed interval/event set | Evidence of inactive, suspended, or unavailable state | A pause does not imply termination or preservation. |
| `G_unexplained` | Interval set with reason | Missing or conflicting coverage | Unknown is not active, inactive, or zero. |
| `E_replay` | Typed event records | Bound source and new execution context | Replay does not extend source-branch participation. |
| `E_fork` | Parent/child branch records | Bound parent state and descendant references | Descendants are measured separately after the fork. |
| `E_restore` | Source-state/target-context records | Bound restored state and target | Similar state does not prove uninterrupted continuity. |
| `E_cold_wake` | Prior-state/wake records | Evidence of wake and preceding state class | The preceding span is a pause or gap, not verified participation. |
| `L_memory` | Ordered lineage transitions | Bound memory-bearing states | Memory preservation alone does not prove identity or authority. |
| `L_governance` | Ordered rule and change records | Versioned governance plus authorized transition evidence | Governance may change while technical state persists. |
| `L_witness` | Witness and review chain | Bound witness identities or explicit unknowns | Repeated witnessing is not continuous participation. |
| `L_authority` | Delegation, scope, revocation, replacement records | Authority source and scope | Authority never follows automatically from profile or memory matching. |
| `T_irreversible` | Scoped transition set | Evidence and a declared irreversibility rule | No known reversal is insufficient. |
| `U` | Structured uncertainty object | Explicit assessment for every coordinate | Uncertainty is part of the result and cannot be silently dropped. |

### Time representation

A timestamp must carry its source, timezone or offset, precision, and clock basis when known. CI may store time as an interval when precision is limited. It distinguishes:

- event time reported by the source;
- capture time recorded by the collector;
- receipt time recorded by a transport or repository; and
- review time recorded by the evaluator.

These times may coincide, but the data model does not assume that they do.

### Participation intervals

Each interval contains:

- start and end bounds with precision;
- declared participation predicate;
- subject and branch references;
- supporting observation references;
- witness and authority context;
- admissibility decision;
- uncertainty; and
- eligibility for `D_verified`.

An open interval may be reported, but it contributes duration only through its last admissibly bounded point. Intervals may overlap; an implementation must define whether overlapping coverage is unioned or kept by predicate and must prevent double counting.

### Event record

A replay, fork, restore, cold-wake, or irreversible-transition record contains:

1. event identifier and type;
2. source and target branch references;
3. predecessor and successor object identities or digests;
4. event, capture, and review times;
5. witness and authority references;
6. affected lineages;
7. supported interpretation and exclusions; and
8. uncertainty and review status.

### Lineage representation

Each lineage transition uses one of five states:

- `preserved_with_evidence`
- `changed_with_bound_record`
- `broken_with_evidence`
- `conflicted`
- `unknown`

The report retains predecessor and successor references. It does not replace a sequence of lineage transitions with an unsupported continuity label.

### Structured uncertainty

The `U` coordinate should include:

| Field | Meaning |
|---|---|
| `missing_evidence` | Expected evidence that was unavailable or not collected. |
| `clock_uncertainty` | Precision, drift, offset, or source-time conflicts. |
| `classification_uncertainty` | Competing event or participation interpretations. |
| `branch_uncertainty` | Unresolved parentage or subject/branch attribution. |
| `lineage_uncertainty` | Unresolved preservation or change in each lineage. |
| `witness_uncertainty` | Missing, dependent, conflicting, or unverified witnesses. |
| `authority_uncertainty` | Missing, expired, revoked, conflicting, or out-of-scope authority. |
| `review_uncertainty` | Pending, incomplete, non-independent, or scope-limited review. |

When a field is not assessed, its value is `not_assessed`, never a numerical zero.

### Derived projections

A profile may derive coverage ratios, gap ratios, branch counts, lineage-change counts, or other summaries. Every projection must name its denominator, observation window, branch policy, and handling of unknowns. A projection cannot increase the underlying claim ceiling.


## Part III. Recognition-profile specification

Source: `RECOGNITION_PROFILE.md`. Original wording reproduced as a reading edition.

### Purpose

A CI recognition profile is a portable, bounded projection of evidence used to compare a declared subject/branch reference across contexts. It is designed for reviewable recognition decisions while preserving the boundary between an entity and a profile about that entity.

A profile match does not prove metaphysical or legal identity. It does not transfer authority, permission, ownership, personhood, or continuity across an unexplained gap.

### Profile fields

| Field | Meaning |
|---|---|
| `profile_id` | Stable identifier for the profile object. |
| `profile_version` | Version of the projection schema and content. |
| `subject_ref` | Declared subject reference; not an identity proof. |
| `branch_ref` | Branch measured by the profile. |
| `observation_window` | Time bounds and precision. |
| `formation_depth_vector` | Full or explicitly redacted CI vector. |
| `lineage_summary` | Separate memory, governance, witness, and authority states. |
| `event_summary` | Replay, fork, restore, cold-wake, and irreversible-transition references. |
| `evidence_roots` | Content digests, immutable locators, or package identities. |
| `witness_scope` | Witness identities, independence, and attested scope. |
| `authority_scope` | Recorded authority context, including expiry or revocation. |
| `claim_ceiling` | Maximum allowed interpretation. |
| `non_claims` | Explicit prohibited inferences. |
| `uncertainty` | Missingness and unresolved conflicts. |
| `validity` | Creation, expiry, supersession, and revocation state. |

### Recognition outcomes

A comparison produces one of these bounded outcomes:

- `recognized_within_profile_scope` — required profile evidence matches within declared tolerances;
- `insufficient_evidence` — required fields or evidence are missing;
- `conflict` — bound evidence disagrees in a way that prevents recognition;
- `stale_or_superseded` — the profile is expired, revoked, or replaced; or
- `not_applicable` — the compared objects fall outside the profile's declared scope.

No outcome is named `same_entity`. A downstream authority may make a separate decision, but that decision and its basis must not be attributed to CI.

### Matching rules

1. Bind both profile objects to exact bytes or content digests.
2. Confirm schema version and branch scope.
3. Compare evidence roots before semantic fields.
4. Compare each lineage independently.
5. Treat replays, forks, restores, and cold wakes as explicit events, not harmless transport details.
6. Apply expiry, revocation, and supersession rules.
7. Preserve mismatches and unknowns in the result.
8. Report the comparison rule and claim ceiling.

### Threat and failure model

The profile must be evaluated against:

- copied or replayed profile bytes;
- stale but validly signed profiles;
- branch substitution or split-brain histories;
- restore events presented as uninterrupted participation;
- memory similarity presented as authority continuity;
- witness dependence or collusion;
- revoked or out-of-scope authority;
- redaction that removes disconfirming evidence; and
- scalar summaries that hide gaps or lineage breaks.

### Public reference alignment

This profile is intended to remain compatible at the conceptual boundary with:

- Beacon: https://doi.org/10.5281/zenodo.18933553
- Entity vs Profile, version DOI: https://doi.org/10.5281/zenodo.21204415
- Entity vs Profile, concept DOI: https://doi.org/10.5281/zenodo.21204414

Those references do not validate a particular CI profile or transfer their claim status into this package.

### Future integration

BACON is listed only as a future integration target. This package does not expand the name, assign a public canonical definition, or claim technical compatibility.


## Part IV. Terminology

Source: `TERMINOLOGY.md`. Original wording reproduced as a reading edition.

The terms below are scoped to this package. They are measurement terms, not declarations of metaphysical, moral, or legal status.

### Core terms

**Continuity Instrument (CI)**  
A branch-aware method for admitting evidence, reconstructing bounded continuity observations, representing uncertainty, and limiting resulting claims.

**Evidence-bound continuity age**  
A vector of admissible temporal, event, lineage, transition, and uncertainty observations. It is not wall-clock age, biological age, legal age, or proof of uninterrupted existence.

**Formation depth**  
A synonym for the evidence-bound continuity vector when the emphasis is on accumulated verified participation and governed change. It is not a maturity rank or personhood scale.

**Admissible witness**  
A source-bound observation that satisfies the applicable identity, temporal, subject/branch, witness/authority, semantic, and claim-scope gates.

**Witness**  
A person, process, system, or record source that attests to a bounded observation. Witnessing does not itself create authority, permission, identity, or truth outside the attested scope.

**Verified participation interval**  
A bounded interval for which admissible evidence supports the declared participation condition. A gap between witnesses is not automatically part of the interval.

**Known pause**  
An evidenced interval or event during which the declared participation condition was inactive, suspended, or unavailable.

**Unexplained gap**  
An interval for which the evidence establishes neither participation nor a classified pause. Unknown is not zero.

### Event terms

**Replay**  
A new execution or presentation of recorded material. Replay may create new evidence but does not retroactively extend the source execution's participation interval.

**Fork**  
Creation of one or more descendant branches from a bound parent state or record. Each descendant requires separate post-fork evidence.

**Restore**  
Loading a prior state into a declared target context. A restore is an event, not proof that all lineages were preserved.

**Cold wake**  
Resumption or initiation after a declared inactive, stopped, unavailable, or uninstantiated state. The preceding span remains a pause or gap according to evidence.

**Irreversible transition**  
A transition shown to be irreversible within a named technical or governance scope and decision rule. It cannot be inferred merely because no reversal is currently known.

### Lineage terms

**Memory lineage**  
The evidence chain for preserved, changed, lost, or disputed memory-bearing state.

**Governance lineage**  
The evidence chain for rules, constraints, decision procedures, and their authorized changes.

**Witness lineage**  
The evidence chain for who or what observed, attested, reviewed, or countersigned relevant events.

**Authority lineage**  
The evidence chain for permissions, delegations, revocations, and bounded decision authority. It is independent of memory similarity or profile recognition.

**Lineage preservation**  
A supported relation between predecessor and successor states within one named lineage. Preservation in one lineage does not establish preservation in another.

### Profile and claim terms

**Entity reference**  
A scoped identifier used to organize observations. CI does not treat the reference as proof of a metaphysical or legal entity.

**Recognition profile**  
A portable, bounded projection of evidence and lineage state used for cross-context recognition. It is not the entity, and possession or matching of the profile grants no authority.

**Claim ceiling**  
The strongest statement allowed by the admitted evidence, uncertainty, review state, and licensing boundary. Evidence delivery alone does not raise the ceiling.

**Qualification**  
A result within an exact frozen evaluator, corpus, rubric, and review scope. It does not generalize without new evidence.

**Open-synthetic evidence**  
Evidence produced in an openly inspectable synthetic setting. It may support claims about that setting but not unobserved real-world deployment, identity, or personhood.

**Independent review**  
A review performed under a declared independence rule against pinned evidence. A self-review or unbound acknowledgement is not substituted for it.

**Uncertainty**  
Structured limits on what the evidence establishes, including missingness, time precision, classification, branch, lineage, witness, authority, and review uncertainty.

### Reserved integration name

**BACON**  
A future integration target only. No public canonical definition was found for this package, so the name is not expanded and no technical semantics are assigned to it here.
