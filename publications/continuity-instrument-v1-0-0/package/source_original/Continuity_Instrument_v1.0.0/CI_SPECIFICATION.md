# CI specification

## 1. Scope

The Continuity Instrument (CI) records what can be supported about governed continuity in a long-lived AI system from bounded evidence. It produces a branch-aware measurement record and a claim ceiling. It does not decide whether a system is a person, the same legal entity, conscious, alive, autonomous, or entitled to authority.

CI separates three layers:

1. **Observed events and witnesses** — source-bound facts admitted by explicit gates.
2. **Continuity reconstruction** — intervals, gaps, branches, transitions, and lineage states derived from admitted facts.
3. **Allowed claims** — statements no stronger than the admitted evidence and declared uncertainty permit.

## 2. Measurement object

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

## 3. Evidence admission

An observation is admissible only when the report records enough information to test all applicable gates:

### 3.1 Byte or object identity

The source object must be bound by an immutable identifier, cryptographic digest, content-addressed reference, or an equivalently reviewable identity. A filename or display title alone is insufficient.

### 3.2 Temporal binding

The observation must identify its time source and precision. Source time, capture time, receipt time, and review time must not be silently conflated.

### 3.3 Subject and branch binding

The observation must identify the declared subject reference and branch. Shared labels, copied profiles, or similar outputs do not establish a shared branch.

### 3.4 Witness and authority binding

The witness, collector, and authority context must be named or explicitly unknown. A witness records evidence; it does not automatically grant identity, permission, or operational authority.

### 3.5 Semantic binding

The record must state what was actually observed: participation, state preservation, governance action, replay, fork, restore, cold wake, transition, or another declared event. Artifact availability alone does not prove active participation.

### 3.6 Claim-scope binding

Each admitted item must carry an allowed interpretation and explicit exclusions. Ambiguous or unsupported items remain excluded or unresolved; they are not imputed.

## 4. Minimum observation record

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

## 5. Interval construction

A verified participation interval requires admissible evidence for both its boundaries and the participation condition claimed within it. CI must not bridge an unexplained gap by assumption. Adjacent intervals may be merged only when the governing rule, branch, witness coverage, and uncertainty treatment are compatible and the merge is recorded.

Known pauses are retained as evidenced events. Unexplained gaps remain unknown even when they fall between two otherwise compatible witnesses. Zero duration, no pause, and no known evidence are three different states.

## 6. Event and branch rules

- A **replay** is a new execution of recorded material. It does not, by itself, extend the source branch's verified participation interval.
- A **fork** creates at least one new branch reference with explicit parentage. Post-fork evidence is branch-specific.
- A **restore** loads prior state into a declared target context. State similarity does not prove uninterrupted participation or preserved authority.
- A **cold wake** begins participation after a declared inactive or unavailable state. The inactive span is a pause or gap according to the evidence, not verified participation.

Branch aggregation may report a graph or family of vectors. It must not collapse competing descendants into a single uninterrupted subject history.

## 7. Lineage rules

Memory, governance, witness, and authority lineage are recorded independently. Each transition is classified as:

- `preserved_with_evidence`;
- `changed_with_bound_record`;
- `broken_with_evidence`;
- `conflicted`; or
- `unknown`.

Preservation in one lineage does not imply preservation in another. Memory similarity does not establish governance or authority continuity. Authority lineage may be revoked or replaced even when technical state is preserved.

## 8. Irreversible transitions

An irreversible transition is recorded only when irreversibility is supported within a declared technical or governance scope. The report must identify the transition, evidence, scope, and decision rule. Absence of a known reversal is not proof of irreversibility.

## 9. Uncertainty

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

## 10. Output contract

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

## 11. Current empirical boundary

R157 is retained as immutable open-synthetic predecessor evidence with an open-synthetic-only claim ceiling. R160 and R161 are consumed negative local-evaluator attempts whose frozen qualification thresholds were not met. This specification therefore makes no real-world continuity-age, entity-identity, personhood, provider-attestation, operational-approval, scientific-qualification, or publication-approval claim.
