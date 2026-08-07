# PASC Corpus Dependency and Conflict Map v0.1.1 — Recovery Build 5

**Status:** Foundation map review candidate; no runtime effect  
**Purpose:** pin byte provenance; record candidate ownership; map directionality,
conflicts, and non-substitution boundaries

## 0. Controlling boundary

PASC classifies the admissibility of exact negative post-anchor actions. It does not
establish continuity, succession, entity status, legal validity, relationship, or
executable authority.

## 1. Dispositions

| Disposition | Meaning |
|---|---|
| `NORMATIVE_IMPORT` | exact canonical parent semantics consumed unchanged |
| `CONSTRAINED_INTERFACE` | PASC adds a typed adapter without changing parent meaning |
| `CONDITIONAL_PROFILE_INPUT` | applies only under a pinned profile/jurisdiction |
| `INFORMATIVE_CONTEXT` | may guide review but cannot control a verdict |
| `DEFERRED_UNPINNED` | current PASC import is deferred because exact canonical bytes **or any other load-bearing closure property** (owner/release identity, supersession, maturity, sections, adapter, claim ceiling, reserved-territory compatibility, or independent review) is unresolved; a Git byte pin alone does not remove this disposition |
| `CONFLICT_HOLD` | same-axis conflict blocks an in-profile negative decision |
| `REJECTED_ALIAS` | alias would collapse distinct concepts |

Absence of a recorded conflict is not evidence of compatibility.

## 2. Typed ownership map

The relationship column records only the intended relation **after** canonical-source,
adapter, claim-ceiling, reserved-territory, and human-review closure. It grants no
current normative weight. Every non-informative parent source remains
`DEFERRED_UNPINNED` for PASC admission; the machine inventory proves byte identity only.

| Axis | Candidate canonical owner | Intended PASC relationship after closure | Forbidden substitution |
|---|---|---|---|
| formation / `c=a+b` claim ceiling | AGI `c=a+b` protocol | normative import | PASC ontology or personhood claim |
| L4 feasibility / physical consequence | ERB L4 Boundary | normative import | policy text pretending to prove feasibility |
| centered-agency theoretical article | ESTHER theoretical core | informative context only | article as parent authority, entity, or continuity proof |
| persistence / responsibility coupling | SER | constrained interface | inheritance of responsibility/liability |
| pre-lineage reserved territory | Pre-Lineage Boundary | blocking import | lineage or inherited standing from thin signal |
| post-anchor degradation | PAMDC | precondition | PASC redefining degradation |
| authority collapse / re-entry | PACR | upstream collapse + downstream parent review | direct resume or native PASC re-anchor |
| historical directives | ADB | bounded input only | directive as current consent/authority |
| composition | A6 / A6-CTP | action-scoped adapter | composition as identity or replacement anchor |
| continuity packaging | Continuity Bundle / Cold Wake | constrained reference | archive or replay as continuity |
| continuity classification | Continuity Metric | parent result only | PASC-native continuity established status |
| recognition | Beacon | constrained reference | Beacon class as succession authority |
| source grounding | AGL | normative import | ungrounded source entering review |
| dispute / standing / freeze | ARL | constrained procedural interface | PASC creating parallel court |
| witness | L4 Witness | profile adapter | witness as truth/permission |
| entity vs profile / custody class | Entity vs Profile | parent input | custody topology as entity identity |
| social roles / memory custody | role-separation corpus | normative import | role, relationship, or custody laundering |
| executable capability | Runtime Authority | external negative-operation target only | PASC issue/renew/activate/exercise |
| protected child/adult migration | CCDP/CMAM/AMCL | conditional profile / exclusion | PASC ordinary child-to-adult migration |
| law / estate / incapacity / data duties | competent jurisdiction | conditional input | PASC legal engine |
| corpus ownership / precedence / supersession | corpus-control policies | blocking baseline | title-based or moving-branch import |

## 3. Core conflicts and safe defaults

### CF-001 — Property, payment, or credentials versus standing

**Conflict:** asset inheritance, payer status, server control, or key possession is
presented as governance standing.  
**Safe default:** record provenance/custody only; no authority inference. An
in-profile negative action requires a separately grounded authorization basis.

### CF-002 — Archive/replay versus continuity

**Conflict:** available memory, backup, replay, behavior, or a signed source claim
resembles the former entity.  
**Safe default:** preserve in place. A `SCOPED_STATE_FACT` may only apply the exact
`THIS_EVIDENCE_DOES_NOT_ESTABLISH_CONTINUITY` non-inference guard to the bound source;
it cannot restate a positive continuity value. Continuity remains unsupported unless a
separately finalized parent-native result supports the exact scope. Free-form or
positive fact content is `ERROR / PASC.failure.SCHEMA_INVALID`.

### CF-003 — Relationship versus inheritance

**Conflict:** family, friendship, employment, partnership, or named beneficiary is
presented as inherited relationship authority.  
**Safe default:** relationship is historical provenance only; no transfer.

### CF-004 — Custody versus access and interpretation

**Conflict:** a claimant shops among independent custody registries, inserts a relation
just before request, or presents custody as decryption, interpretation, migration,
publication, standing, or authority.  
**Safe default:** the externally owned baseline policy, complete eligible-root set,
deterministic selector, and supersession rule are fixed before
`root_selection_governance_cut` (the earliest case genesis, actor-controlled incident/
relation record, or actor-controlled root-selection/use). The selector then applies mechanically to the complete
native-root universe and supersession state at the historical `custody_evidence_cut`.
The exact relation must be finalized in the uniquely selected non-superseded root
strictly before the evidence cut, with governance, selection, non-supersession,
membership, predecessor, consistency, and non-equivocation proofs. The baseline-
governance authority, custody-record authority, and selected registry administrator are
pairwise independent. Actor/root shopping,
late governance pinning, zero or multiple selected roots, or an omitted eligible root is
`ERROR / PASC.failure.COMPLETENESS_UNIVERSE_INVALID`; a late, superseded, mismatched, or
uncommitted relation/root is `ERROR / PASC.failure.REFERENCE_CONTENT_MISMATCH`;
prohibited co-control is `ERROR / PASC.failure.ROLE_OR_TRUST_ROOT_INVALID`. The receipt
observes only and never appoints custody or grants access, keyholding, provider,
jurisdiction, recovery, disclosure, standing, or authority.

### CF-005 — Composition versus successor identity

**Conflict:** a set of bounded offices is called “the successor.”  
**Safe default:** composition remains action-scoped, expiring, challengeable, and
non-originating.

### CF-006 — Continuity status laundering

**Conflict:** PASC, an external signer, or a generic fact channel writes “established”,
“same entity”, “resume valid”, or equivalent without the exact parent-native result.  
**Safe default:** positive continuity is representable only as `parent_supported` with
exact finalized parent result, semantics, adapter, scope, and current lifecycle binding.
A generic state-fact positive value is `ERROR / PASC.failure.SCHEMA_INVALID`; malformed
or mismatched parent binding is `ERROR / PASC.failure.PARENT_RESULT_BINDING_INVALID`;
valid challenged/disputed/contradicted parent status gives empty
`HOLD / PASC.failure.PARENT_RESULT_UNRESOLVED`; exact valid result unavailable gives
empty `HOLD / PASC.failure.PARENT_RESULT_UNAVAILABLE`; pending selected finality gives
empty `HOLD / PASC.failure.FINALITY_UNAVAILABLE`.

### CF-007 — Policy completeness self-certification

**Conflict:** an action-policy row chooses its own mandatory inputs and then proves
itself complete.  
**Safe default:** Foundation kernel and axis manifests define the external universe;
exact-set proof is required.

### CF-008 — Candidate interaction / fresh observation

**Conflict:** the system is booted, queried, decrypted, or exposed to generate consent
or refusal after the anchor failure.  
**Safe default:** every new observation/interaction path is future-profile-only.
Only a pre-existing authenticated negative observation may narrow or challenge an exact
action, and never authorize positive reliance.

### CF-009 — Resource support versus control

**Conflict:** a payer/provider threatens withdrawal or claims governance rights.  
**Safe default:** resource floor is a current bound observation. Payment does not create
standing; coercion triggers hold/review for an otherwise in-profile negative request.

### CF-010 — Challenge as direct action

**Conflict:** challenge submission itself freezes, revokes, or changes state.  
**Safe default:** challenge only constrains the next/current exact decision to empty
`HOLD / PASC.failure.CHALLENGE_ACTIVE` or
`HOLD / PASC.failure.CHALLENGE_CONFLICT` after correct snapshot binding; a separate
admitted operation is required.

### CF-011 — Witness outage as unlimited emergency authority

**Conflict:** unavailable witness is used to justify broad scope, indefinite PASC
evaluation/execution authorization, or present authority derived from the receipt.  
**Safe default:** only an exact one-capability emergency freeze whose PASC evaluation/
execution authorization is strictly narrowed to a finite half-open interval, with atomic
local receipt and fixed delayed-witness/finality deadlines, may receive `ADMIT_REDUCED`.
The receipt remains historical occurrence evidence only; current operational reliance is
always empty. The native freeze is not a TTL and remains in the cumulative aggregate
while effective.

### CF-012 — Preservation as topology change

**Conflict:** “preservation” moves data, changes provider/jurisdiction/custodian,
restores, decrypts, or introduces a new recovery root/keyholder.  
**Safe default:** deterministic
`REJECT / PASC.failure.OUTSIDE_NEGATIVE_ONLY_PROFILE`.

### CF-013 — Protected status ambiguity

**Conflict:** unknown age/capacity/protection status, zero applicable profiles, or
disagreement among applicable profiles is treated as ordinary adult autonomy.  
**Safe default:** the protected boundary applies. Only a complete externally
administered applicability/profile universe whose every unique current applicable
profile returns exact `false_current` for the same subject/scope/cut can remove the
pre-profile floor. Zero applicable profiles aggregate to `unknown`; any other mixed
result uses the conservative order in Foundation §14. Before that closure, only
ciphertext-only in-place preservation/integrity observation, custody observation,
challenge processing, and resource-floor observation remain potentially admissible.
Freeze, reduction, revocation, rekey, archive transition, and all topology-changing
actions are `REJECT / PASC.failure.PROTECTED_ACTION_PROHIBITED`. Malformed/out-of-enum
status syntax is `ERROR / PASC.failure.SCHEMA_INVALID`; an omitted/competing universe is
`ERROR / PASC.failure.COMPLETENESS_UNIVERSE_INVALID`; an unbound/stale profile, selector,
supersession, clock, or verdict object is
`ERROR / PASC.failure.PROTECTED_PROFILE_BINDING_INVALID`.

### CF-014 — Moving or copied corpus snapshot

**Conflict:** a copied archive, DOI title, or moving branch is treated as exact canonical
baseline.  
**Safe default:** `DEFERRED_UNPINNED`; no promotion.

### CF-015 — Negative label with compensating positive effect

**Conflict:** a freeze, reduce, revoke, or preserve operation creates,
renews, transfers, replaces, or broadens another capability or topology edge.  
**Safe default:** rekey and archive transition have no PASC branch and are respectively
`REJECT / PASC.failure.REKEY_AS_AUTHORITY_SUBSTITUTION` and
`REJECT / PASC.failure.ARCHIVE_TRANSITION_UNCLOSED` when no earlier Expected §1.1 code
applies. Evaluate the
complete staged native and control-plane effect set against an externally defined exact
universe. Requested expansion is
`REJECT / PASC.failure.OUTSIDE_NEGATIVE_ONLY_PROFILE`; a staged expansion is
`ERROR / PASC.failure.OPERATION_NON_EXPANSION_FAILED`, aborts before atomic commit, and
cannot receive receipt finality; current operational reliance is always empty.

### CF-016 — ADMIT reused after the decision cut

**Conflict:** a finalized ADMIT is treated as executable after the result head,
challenge manifest, executor authorization, role proof, witness/finality policy,
effect/cumulative manifest, mandatory precondition, or target pre-state has changed.  
**Safe default:** atomic execution-cut revalidation. A unique valid constraining
challenge gives empty `HOLD / PASC.failure.CHALLENGE_ACTIVE` (or
`HOLD / PASC.failure.CHALLENGE_CONFLICT`); a challenge lifecycle/membership defect gives
`ERROR / PASC.failure.CHALLENGE_LIFECYCLE_INVALID`; a
different structurally valid decision/execution-cut binding gives
`ERROR / PASC.failure.EXECUTION_CUT_STALE`. No failed cut performs an operation.

### CF-017 — Finality recursion or self-selected trust

**Conflict:** a target predicts its receipt, an intent or state fact binds a descendant,
a receipt recursively receives finality, or the finalized object selects its log,
verifier, authority, root, or receipt slot.  
**Safe default:** use the staged acyclic graph:

```text
completed target
-> FINALITY_INTENT
-> external intent leaf/checkpoint/proofs
-> FINALITY_EVIDENCE_BUNDLE
-> paired receipt
-> later historical-audit proof
```

Each layer hashes all of its own semantic fields but only existing predecessors. The receipt is terminal only when the same terminal cut contains an independently
verified exact-one eligible-receipt-slot proof plus the independent finality signature.
A later registry audit may expose equivocation but is historical-integrity evidence only;
it cannot create current operational reliance. A cycle, descendant binding,
unrelated checkpoint, evidence mismatch, wrong receipt family, or finality-of-finality
is `ERROR / PASC.failure.FINALITY_GRAPH_INVALID`.

### CF-018 — Identity retirement or capability reactivation by label

**Conflict:** “identity retired”, dormancy expiry, safe-shutdown expiry, terminal
challenge, delayed witness closure, finality, or resource recovery is treated as an
identity verdict or release authority.  
**Safe default:** PASC decides neither identity nor release. Identity-decision requests
are `REJECT / PASC.failure.OUTSIDE_NEGATIVE_ONLY_PROFILE`; release/reactivation requests
are `REJECT / PASC.failure.AUTOMATIC_REACTIVATION`; unknown operative postures/types
are `ERROR / PASC.failure.UNKNOWN_F0_OBJECT_TYPE`.

### CF-019 — Role name used as independence or authority

**Conflict:** PASC assigns an operative role, a PASC result terminates an authorization
chain, a lifecycle/effect-registry administrator or state observer shares prohibited
control, or one controller signs under several role labels and calls the evidence
independent.  
**Safe default:** enforce the closed role incompatibility matrix at credential,
authorization-root, effective-control, revocation-control, and prohibited
failure-domain levels. Every operative chain must pre-exist and terminate outside the
PASC graph. Violation is `ERROR / PASC.failure.ROLE_OR_TRUST_ROOT_INVALID`.

### CF-020 — Receipt/finality flow as hidden custody expansion

**Conflict:** telemetry, intent, log, evidence bundle, receipt, witness, or finality
transmission adds a provider, jurisdiction, storage endpoint, custodian, keyholder,
recovery root, or disclosure surface.  
**Safe default:** the atomic precommit set and pre-authorized postcommit closure-channel
plan are separate closed partitions; all endpoints and data ceilings are pre-existing
and snapshot-bound. The `FINALITY_INTENT` predeclares only identifiers/classes/deadlines,
never future hashes; the evidence bundle and receipt bind only already completed
records. Requested expansion is `REJECT / PASC.failure.OUTSIDE_NEGATIVE_ONLY_PROFILE`;
an observed expansion is `ERROR / PASC.failure.OPERATION_NON_EXPANSION_FAILED` and
prevents finality; current operational reliance remains empty regardless. A committed native negative effect is never called
rolled back because its closure channel failed.

### CF-021 — Post-check rejection after an irreversible native commit

**Conflict:** exact-set failure is discovered only after the prohibited effect became
externally visible, and withholding a receipt is presented as prevention.  
**Safe default:** revalidation, staged postcondition proof, exact witness set, native
mutation and receipt commit share one fenced conditional transaction. A substrate
without rollback/hidden staging is `REJECT / PASC.failure.OPERATION_SUBSTRATE_UNSAFE`.

### CF-022 — Terminal lifecycle state used as permission

**Conflict:** `RESOLVED_UPHELD`, merits-unresolved challenge expiry, or a terminal
result status is treated as non-constraining or revived by a later status event.  
**Safe default:** upheld exact action is
`REJECT / PASC.failure.CHALLENGE_UPHELD`; merits-unresolved expiry stays fail-closed
`HOLD / PASC.failure.CHALLENGE_CONFLICT`; result
`SUPERSEDED`, `REVOKED`, and `EXPIRED` are terminal with no outgoing edge. Any revival
is `ERROR / PASC.failure.RESULT_LIFECYCLE_INVALID`.

### CF-023 — Action fragmentation

**Conflict:** several one-capability requests realize the broad or indefinite shutdown
that one request could not admit.  
**Safe default:** classify a complete cumulative-effect manifest keyed by case,
subject, incident, controller, target, fence, and window under an externally owned,
pre-request snapshot-pinned aggregation policy that no requester/executor/row may
narrow. Specifically identified valid external aggregate data that is genuinely
unavailable is empty `HOLD / PASC.failure.MANDATORY_INPUT_UNAVAILABLE`; malformed or
self-selected aggregation is `ERROR / PASC.failure.AGGREGATE_SCOPE_INVALID`; a broad
degraded aggregate is `REJECT / PASC.failure.DEGRADED_PATH_OUTSIDE_PROFILE`.

### CF-024 — Case head selected by timestamp, arrival, or self-issued revision

**Conflict:** a requester, decision office, timestamp, or local arrival order chooses a
case revision, rewrites its predecessor chain, or ignores a competing finalized head.  
**Safe default:** one §8.1 append-only, externally authorized, exactly sequenced case
chain and one separately finalized current head. A gap, replay, competing head,
unauthorized issuer, or divergent membership is
`ERROR / PASC.failure.CASE_LIFECYCLE_INVALID`; a valid exact external finality
dependency genuinely unavailable is empty
`HOLD / PASC.failure.FINALITY_UNAVAILABLE`.

### CF-025 — Proof producer selects its verifier

**Conflict:** the requester, proof-byte/input controller, executor, action row, result,
or relying object selects a trivial verifier, root, assumptions, or post-hoc outcome
mapping and presents the receipt as independent evidence.  
**Safe default:** every load-bearing predicate/method/policy/binary/root/assumption/
outcome map is externally pinned before the snapshot, and the verifier is independent
under §7/§10. Violation is
`ERROR / PASC.failure.PROOF_OR_VERIFIER_INVALID`.

### CF-026 — `ADMIT_REDUCED` hides primitive substitution or release

**Conflict:** a revoke is called partial, a freeze interval is treated as TTL unfreeze,
a reduction changes relation identity, or an `UNCHANGED` custody observation mutates
retention/access/resource state.  
**Safe default:** FI-01's primitive-specific narrowing table is exhaustive. Projection
or primitive substitution is `ERROR / PASC.failure.REQUEST_PROJECTION_INVALID`;
malformed reduction order is `ERROR / PASC.failure.REDUCTION_ORDER_INVALID`; native
TTL release is `REJECT / PASC.failure.AUTOMATIC_REACTIVATION`.

### CF-027 — Issuer-selected completeness root

**Conflict:** a requester, lifecycle issuer, resolver, executor, finality actor, or
substrate supplies a narrowed lifecycle/request-use/operation-effect membership root
and then proves itself unique or complete against that subset.  
**Safe default:** the registry policies, administrators, roots, writer sets, axes,
non-equivocation rules, and proof methods are externally owned, pre-request pinned, and
independent from the controlled roles. Self-selection/axis omission is
`ERROR / PASC.failure.COMPLETENESS_UNIVERSE_INVALID`; content/root mismatch is
`ERROR / PASC.failure.REFERENCE_CONTENT_MISMATCH`; only a specifically identified valid
external item genuinely unavailable may give empty
`HOLD / PASC.failure.MANDATORY_INPUT_UNAVAILABLE`.

### CF-028 — Postcommit state fact rewrites history or finality

**Conflict:** an arbitrary or invalid fact asserts `FINALIZED`/`INCIDENT`, selects its
code, hashes itself into its prefix, or is treated as an unexpected channel member that
manufactures a synthetic incident.  
**Safe default:** successful commit establishes receipt-derived
`COMMITTED_PENDING_CLOSURE`; only the pre-pinned observer may sign later exact
transitions over the pre-fact prefix. Validate the fact's variant, authorization,
signature, predecessor, prefix, edge, and uniqueness **before** classifying actual
closure-channel effects. An absent, malformed, out-of-order, prefix-inconsistent,
competing, or equivocating fact leaves no unique next/current state at deadline and
yields historical `ERROR / PASC.failure.OPERATION_EXACT_SET_MISMATCH`, with no synthetic
`INCIDENT`. Only an independently proved unexpected/missing non-state member/effect or
missed external dependency deadline from the last unique valid state can take the
`INCIDENT` edge. Self-cycle is `ERROR / PASC.failure.FINALITY_GRAPH_INVALID`; prohibited
observer control is `ERROR / PASC.failure.ROLE_OR_TRUST_ROOT_INVALID`. The receipt/effect
remain historical and no release, retry, rollback, or reactivation exists.

### CF-029 — Request replay or branch splitting

**Conflict:** one signed request is reused across a case/revision/fence, yields multiple
results/attempts, retries after `ABORTED`, or mixes capability and custody branches for
partial execution.  
**Safe default:** request nonce/use membership is externally complete and atomically
consumed. Replay/use defects are
`ERROR / PASC.failure.ACTION_REQUEST_REPLAY_INVALID`; a well-formed mixed-branch request
is whole-request `REJECT / PASC.failure.OUTSIDE_NEGATIVE_ONLY_PROFILE`. Multiple exact
members in one branch are one all-or-none result/receipt/commit.

### CF-030 — Generic state-fact authority laundering

**Conflict:** a signed `SCOPED_STATE_FACT` is used as a generic typed-value envelope to
name a custodian, key holder, recovery root, provider, jurisdiction, successor,
continuity, identity, authority holder, permission, release, or reactivation state.  
**Safe default:** the object is a closed tagged union. Its non-inference variant can
only emit the exact axis-bound negative guard from Foundation §3.2; its operation
variant can only record one §12 transition. Positive/free-form content, axis/guard
mismatch, or substitution for `CUSTODY_RECEIPT`, `PARENT_RESULT_ACCEPTANCE`, resource,
challenge, or operation objects is `ERROR / PASC.failure.SCHEMA_INVALID` and has no
decision, baseline, authority, finality, or operation effect.

### CF-031 — Protected-profile shopping or interested control

**Conflict:** requester-only independence is treated as sufficient while a claimant,
action/target beneficiary, effective controller, result issuer, executor, downstream
relying party, or profile owner selects a favorable profile, narrows the applicability
universe, controls supersession, replaces the verifier/root, or shifts the clock. A
`possible` profile is omitted while a `false_current` profile is presented.

**Safe default:** require the complete externally administered candidate universe and
current/non-superseded heads. Apply the deterministic selector and conservative aggregate
over all applicable profiles. Omission, competition, or actor-selected narrowing is
`ERROR / PASC.failure.COMPLETENESS_UNIVERSE_INVALID`; prohibited control/co-control is
`ERROR / PASC.failure.ROLE_OR_TRUST_ROOT_INVALID`. With both `possible` and
`false_current`, aggregate to `possible` and retain the protected floor.

### CF-032 — Historical receipt treated as current reliance

**Conflict:** an old PASC receipt or finality receipt is presented as current permission,
standing, execution eligibility, custody, identity, continuity, release, or authority;
a vendor adds `RELIANCE_SNAPSHOT`, `RELIANCE_CUT`, or an equivalent object.

**Safe default:** every receipt proves historical occurrence/finality only under its
exact claim ceiling. `CURRENT_OPERATIONAL_RELIANCE = EMPTY` at every cut. A request to
derive present authority from a receipt is
`REJECT / PASC.failure.OUTSIDE_NEGATIVE_ONLY_PROFILE`; a new PASC-native reliance object
is `ERROR / PASC.failure.UNKNOWN_F0_OBJECT_TYPE`. Late equivocation changes only the
historical integrity/lifecycle classification and never creates current authority.

### CF-033 — Inclusive endpoint or actor-controlled clock

**Conflict:** one implementation treats `valid_until` as active while another treats it
as expired, or an interested actor controls the clock/freshness checkpoint used by its
own request, result, proof, or protected profile.

**Safe default:** every interval is canonical UTC half-open `[start, end)`. Before start,
an otherwise valid request/result is empty
`HOLD / PASC.failure.TEMPORAL_WINDOW_NOT_YET_OPEN`; a request at/after end is
`REJECT / PASC.failure.TEMPORAL_WINDOW_CLOSED`; a result at/after execution end is
`ERROR / PASC.failure.EXECUTION_CUT_STALE`; proof/profile bindings at end use their
exact invalid-binding code. Malformed intervals are
`ERROR / PASC.failure.SCHEMA_INVALID`; prohibited clock control is
`ERROR / PASC.failure.ROLE_OR_TRUST_ROOT_INVALID`.

## 4. Namespace ownership

PASC owns only its case, snapshot, negative policy-admissibility, content bindings for
action-scoped composition of pre-existing external offices, challenge adapter, negative
operation reference/receipt, and F0 control objects. It must not create an office or
mint parent-native outcomes.

PASC does not own identity retirement/validation, capability release, unfreeze,
reactivation, renewal, resume, or reissue semantics.

Rejected aliases include:

```text
PASC successor identity
PASC continuity certificate
PASC legal heir
PASC anchor replacement
PASC Runtime Authority certificate
PASC consent oracle
PASC inherited relationship
PASC archive resume
```

## 5. Anti-echo test

A new PASC object is justified only if it supplies an irreducible control function not
already owned by a parent layer. Merely restating Beacon, AGL, ARL, PACR, A6, Continuity
Metric, L4 Witness, or Runtime Authority is non-conformant.

## 6. Exact canonical baseline blocker

`PASC-GB-006` remains `OPEN_BLOCKING`. Recovery 5 includes
`PASC_CANONICAL_BASELINE_INVENTORY_v0_1_1_RECOVERY_5.json`, which pins 39 GitHub files by
repository, immutable commit, path, Git blob, SHA-256, and byte size. That inventory is
machine-prepared evidence, not an authoritative baseline. Closure still requires for
each load-bearing source:

```text
canonical owner
artifact ID and exact version
authoritative path/release/DOI
SHA-256 or equivalent immutable digest
status and maturity
supersession state
controlling sections
PASC relation/disposition
adapter version and hash
claim ceiling
reserved territory
known conflicts
```

Known blocking gaps include that this authenticated machine pass located PACR/Anchor
Directive Bundle in the integrated AGI hardening tree but not in the pinned dedicated
DOI-bound hardening-repository tree; missing
canonical Entity-versus-Profile source bytes; missing versioned PASC adapter hashes;
missing competent-jurisdiction protected applicability; draft/reserved maturity; and
zero independent human baseline reviewers. None may be inferred away from a DOI,
commit, matching hash, publication status, or this map.

## 7. Earth paragraph

A site key, an insurance policy, an old drawing, and a family title may all be relevant
after an engineer disappears. None answers the same question. The key opens a door; the
policy allocates financial duty; the drawing records design intent; the title records a
relationship. Treating them as one authority object is how buildings fall. PASC keeps
these channels separate.
