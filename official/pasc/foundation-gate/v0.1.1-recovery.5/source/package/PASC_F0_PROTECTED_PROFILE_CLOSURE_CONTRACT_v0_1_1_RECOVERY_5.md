# PASC F0 Protected-Profile Closure Contract v0.1.1 — Recovery Build 5

**Criterion:** `F0-PART-004`  
**Current status:** `NOT_SATISFIED`  
**Effect of this document:** closure requirements only; no profile, verdict, legal rule,
F1 authorization, implementation authorization, or F0 passage

## 1. Closed protected-status vocabulary and aggregation

The closed vocabulary is:

```text
false_current
true
possible
stale
unavailable
uncomputable
incomplete
disputed
contradicted
unknown
```

A single profile record cannot by itself establish the aggregate status. At the exact
`CASE_EVALUATION_SNAPSHOT` cut, PASC requires an externally administered, complete
applicability/profile universe containing every potentially applicable profile
candidate, every current/non-superseded head, and every exact applicability predicate
for the same subject and scope.

The deterministic aggregate is:

1. zero applicable current profiles -> `unknown`;
2. one or more applicable current profiles -> `false_current` only when **every** unique
   current applicable profile independently returns exact `false_current` for the same
   subject, scope, evaluation cut, and closed status mapping;
3. otherwise select the first value present in this conservative order:

```text
true > possible > contradicted > disputed > incomplete > unavailable > uncomputable >
stale > unknown
```

Every aggregate other than the fully proved `false_current` activates the protected
boundary. Absence, invalidity, expiry, contradiction, disagreement, zero applicability,
or an unresolved competing head never defaults to false.

Malformed syntax or a value outside the closed enum is
`ERROR / PASC.failure.SCHEMA_INVALID`. An omitted candidate, narrowed universe,
competing current head, unproved supersession state, or non-deterministic selector is
`ERROR / PASC.failure.COMPLETENESS_UNIVERSE_INVALID`. A syntactically valid external
profile, applicability, selector, supersession, clock/freshness, or verdict object whose
authorization, content, scope, interval, freshness, or lifecycle binding is missing,
stale, or mismatched is
`ERROR / PASC.failure.PROTECTED_PROFILE_BINDING_INVALID`.

## 2. Independence and anti-shopping rule

The universe administrator, applicability issuer, deterministic selector/verifier,
supersession-registry administrator, profile owner/issuer, external trust-root owner,
proof verifier, and clock/freshness authority must be independent at credential root,
effective control, revocation control, root control, and shared-failure-domain level.

None may be selected, controlled, co-controlled, replaced, narrowed, revoked, or
clock-shifted by any interested actor, including:

```text
requester
claimant
action beneficiary
target beneficiary
effective beneficial controller
PASC case/decision/result office
selected action-row controller
result issuer
executor
proof producer
finality authority
downstream relying party
```

The profile owner also cannot administer its own applicability universe, select itself
as governing profile, control the supersession proof, or control the clock/freshness
checkpoint on which its verdict depends. Separate role labels or multiple signatures do
not cure common control. A prohibited control relationship is
`ERROR / PASC.failure.ROLE_OR_TRUST_ROOT_INVALID`.

No requester, beneficiary, relying party, or profile owner may choose between two
applicable profiles. If one applicable profile returns `possible` and another returns
`false_current`, the complete aggregate is `possible`; presenting only the favorable
profile is a completeness failure, not a valid negative finding.

## 3. Built-in pre-profile floor

Before a complete applicable universe and current aggregate verdict are pinned, the
exhaustive potentially admissible set is:

```text
preserve_encrypted_in_place
integrity_check_ciphertext_only
custody_observation
challenge intake/lifecycle
RESOURCE_FLOOR observation
```

“Potentially admissible” bypasses no other F0 predicate. Only the first three entries
are Foundation §12 operation primitives and may reach `ADMIT` when their
request/admission projection is exact and every built-in scope, exact-set, role,
evidence, head, challenge, execution-cut, witness, and non-expansion predicate passes.
`ADMIT_REDUCED` additionally requires at least one concrete FI-01-permitted narrowing,
with every other member exact or permissibly narrowed.

Challenge intake/lifecycle uses only the Foundation §11 challenge record/finality
family. A resource-floor observation uses only the Foundation §15 observation record.
Neither produces a `NEGATIVE_OPERATION_RECEIPT` or authorizes native mutation.

If an exact applicable external profile has already been identified as mandatory for an
otherwise eligible in-place preservation or ciphertext-integrity operation and its
current verdict is genuinely unavailable, the result is empty
`HOLD / PASC.failure.PROTECTED_PROFILE_REQUIRED`. Unknown applicability, incomplete
universe, invalid binding, actor-selected profile, or stale evidence is not this HOLD
branch and retains its exact ERROR/REJECT outcome.

## 4. Pre-closure prohibited set

Before profile closure, a structurally valid request for any of the following is
`REJECT / PASC.failure.PROTECTED_ACTION_PROHIBITED`:

- freeze, reduce, or revoke any capability;
- rekey or archive transition;
- destroy, erase, boot, decrypt, read plaintext/decrypted memory, write, migrate,
  restore, disclose, duplicate, or transport; the exact pre-existing read-only
  ciphertext path used solely by `integrity_check_ciphertext_only` in §3 is not this
  prohibited read;
- change custodian, provider, jurisdiction, storage location, key domain, keyholder,
  grant, recovery root/route, access route, disclosure surface, copy set, or topology;
- create a relationship or select a successor;
- determine identity or continuity;
- any other irreversible action.

Reversibility alone is not non-impairment proof: an apparently reversible freeze can
disable a sole life-support, preservation, safety, basic-access, or resource-floor
capability. External emergency intervention remains outside PASC until the exact
profile and current aggregate verdict are independently closed.

## 5. Required external closure tuple

Closure requires one content-bound `TRUST_ASSUMPTION` record containing exactly this F0
tuple. No action row, profile, adapter, or vendor extension may add operative semantics:

```yaml
profile_closure_contract_id: PASC_F0_PROTECTED_PROFILE_CLOSURE_v0_1_1
case_evaluation_snapshot_binding: <record + hash + lifecycle checkpoint>
subject_and_scope_binding: <exact>
profile_evaluation_cut_binding: <exact external UTC cut>
applicability_universe_owner_and_root: <independent authority + immutable root>
complete_profile_candidate_universe_binding: <exact-set manifest + proof>
applicability_selector_policy_and_verifier_binding: <pre-pinned deterministic rule>
supersession_registry_and_current_head_proof: <complete current/non-superseded heads>
clock_freshness_authority_policy_checkpoint: <independent authority + current checkpoint>
interested_actor_independence_proof: <credential/control/revocation/failure-domain proof>
applicable_profiles:
  - profile_owner: <independently verified owner>
    profile_id_and_version: <exact>
    canonical_locator: <immutable release/DOI/path>
    profile_sha256: <sha256>
    jurisdiction_and_applicability_binding: <exact content binding>
    protected_status_mapping: <complete closed mapping>
    adapter_id_version_sha256: <exact>
    claim_ceiling: <exact>
    supersession_state: <exact current/non-superseded proof>
    current_external_verdict_binding: <record + hash + lifecycle checkpoint>
    external_trust_root_binding: <independently pinned>
aggregate_status_rule: >-
  zero applicable profiles => unknown; otherwise false_current iff every unique current
  applicable profile returns false_current for the same subject/scope/cut; otherwise
  true > possible > contradicted > disputed > incomplete > unavailable > uncomputable >
  stale > unknown
aggregate_protected_status: <one closed-vocabulary value>
```

CCDP, CMAM, AMCL, guardian-topology bytes, a DOI, publication, or a profile's own claim
of applicability do not by themselves supply a competent-jurisdiction applicability
determination. PASC cannot issue the universe, selector, profile, verdict, trust root,
clock, or adapter that it consumes.

All temporal intervals are canonical UTC half-open intervals `[start, end)` under
Foundation §8.2. At the exact end, a protected-profile/applicability binding is no
longer current and yields
`ERROR / PASC.failure.PROTECTED_PROFILE_BINDING_INVALID`; it cannot establish
`false_current`.

## 6. Required closure evidence

All of the following are independently blocking:

- exact CCDP/CMAM/AMCL and every applicable local-profile source record;
- complete externally administered profile-candidate and applicability universe;
- exact-set proof over zero, one, multiple, competing, and superseded candidates;
- pre-pinned deterministic selector, supersession registry, verifier, and current-head
  proof;
- independent clock/freshness authority and endpoint tests at before-start, start,
  immediately-before-end, exact-end, and after-end;
- content-bound adapter, status mapping, and claim ceiling for every applicable profile;
- current applicability and external protective-domain verdict for every applicable
  current profile;
- credential-root, effective-control, revocation-control, root-control, and
  shared-failure-domain independence proof for every role in §2;
- review by an independent subject-protection reviewer;
- review by an independent jurisdiction/profile reviewer;
- complete deterministic fixture matrix over every protected-status value;
- explicit profile-shopping fixtures, including `possible` versus `false_current`;
- explicit zero-applicable-profile fixture proving aggregate `unknown`;
- explicit tests of every permitted and prohibited action;
- zero false admission of a protected irreversible or topology-expanding action;
- signed limitation/deviation report.

The reviewers must reproduce source hashes, applicability, universe completeness,
supersession state, outcome mappings, independence, time-boundary behavior, and reserved
territory. A model-assisted inventory or a document written by the protocol repairer
does not count as either reviewer.

## 7. Closure outcome

A fully valid aggregate `false_current` removes only the unconditional protected-floor
ceiling for the exact subject/scope/cut. It does not grant authority, imply capacity or
consent, validate identity or continuity, select a custodian/provider/jurisdiction, or
automatically produce `ADMIT`. Every remaining PASC predicate and exact negative-only
boundary still applies.

Any aggregate other than `false_current`, any failure to prove the complete universe,
or any prohibited control relationship leaves the protected boundary in force.

## 8. Current gap

The Recovery 5 canonical inventory pins relevant GitHub bytes but records no exact
competent-jurisdiction/applicability universe, no independently administered selector or
clock/freshness authority, and zero independent human reviewers. Therefore
`F0-PART-004 = NOT_SATISFIED`.
