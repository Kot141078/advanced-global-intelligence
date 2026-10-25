# Continuity observables

## Formation-depth vector

CI represents evidence-bound continuity age / formation depth as:

`F_E = <W_first, W_last, I_verified, D_verified, P_known, G_unexplained, E_replay, E_fork, E_restore, E_cold_wake, L_memory, L_governance, L_witness, L_authority, T_irreversible, U>`

The coordinates remain inspectable. They must not be collapsed into a single age value by default.

## Coordinate definitions

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

## Time representation

A timestamp must carry its source, timezone or offset, precision, and clock basis when known. CI may store time as an interval when precision is limited. It distinguishes:

- event time reported by the source;
- capture time recorded by the collector;
- receipt time recorded by a transport or repository; and
- review time recorded by the evaluator.

These times may coincide, but the data model does not assume that they do.

## Participation intervals

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

## Event record

A replay, fork, restore, cold-wake, or irreversible-transition record contains:

1. event identifier and type;
2. source and target branch references;
3. predecessor and successor object identities or digests;
4. event, capture, and review times;
5. witness and authority references;
6. affected lineages;
7. supported interpretation and exclusions; and
8. uncertainty and review status.

## Lineage representation

Each lineage transition uses one of five states:

- `preserved_with_evidence`
- `changed_with_bound_record`
- `broken_with_evidence`
- `conflicted`
- `unknown`

The report retains predecessor and successor references. It does not replace a sequence of lineage transitions with an unsupported continuity label.

## Structured uncertainty

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

## Derived projections

A profile may derive coverage ratios, gap ratios, branch counts, lineage-change counts, or other summaries. Every projection must name its denominator, observation window, branch policy, and handling of unknowns. A projection cannot increase the underlying claim ceiling.
