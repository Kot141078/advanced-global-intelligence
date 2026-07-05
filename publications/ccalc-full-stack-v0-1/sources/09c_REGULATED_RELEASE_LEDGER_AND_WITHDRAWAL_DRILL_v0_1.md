# 09c — Regulated Release Ledger and Withdrawal Drill v0.1

**Artifact:** `09c_REGULATED_RELEASE_LEDGER_AND_WITHDRAWAL_DRILL_v0_1`  
**Package:** `CCALC_REGULATED_RELEASE_LEDGER_WITHDRAWAL_09c_v0_1`  
**Layer:** c-calculus / deployment profile / regulated release / withdrawal and recall drill  
**Status:** normative-supporting executable seed / fixture-backed release-ledger package  
**Created UTC:** `2026-07-05T16:42:30Z`

---

## 0. Purpose

`09` defines the deployment and regulated-release boundary. `09a` defines the deployment candidate schema and checker-seed contract. `09b` applies fixture and mutation pressure to the candidate profile.

`09c` defines what happens **when a release is actually recorded, published, distributed, held, withdrawn, recalled, superseded, or carried into the next-release gate**.

The governing formula is:

```text
candidate -> deployment decision -> release ledger -> distribution/watch -> incident/hold -> withdraw | recall | supersede | next-release gate
```

The central rule is:

```text
release is not completion;
release opens a ledger-bound responsibility window.
```

A release may be public, internal, field-bound, regulated-submission-only, limited-production, withdrawn, recalled, superseded, quarantined, or held. None of those states may be silently rewritten into another state.

---

## 1. Relation to previous layers

```text
04  continuity / equivalence / rupture / fork / replay / archive / restoration
05  self-evolution / promotion / rollback / post-promotion watch
06  runtime authority / session ledger / emergency hold / revocation
07  public evidence / release custody / errata / citation sync
08  interoperability / external review / patch / reproduction / disclosure
09  deployment profile and regulated release boundary
09a deployment profile schema and checker seed
09b deployment fixture and mutation matrix
09c regulated release ledger and withdrawal drill
```

`09c` does not authorize deployment by itself. It records release-state transitions and rejects laundering between release states.

---

## 2. Source bindings

The package includes `SOURCE_BINDINGS.tsv`. Current build bindings:

| Binding | Artifact | SHA-256 | Status |
|---|---|---:|---|
| `DOC04_CONTINUITY_STACK_UMBRELLA` | `CCALC_DOC04_CONTINUITY_STACK_UMBRELLA_v0_1.zip` | `6caeab8d489aaa6b26902db3bd3ece4c5169e5c8d5617b93aed6586ea900322d` | `declared-upstream` |
| `DOC05_SELF_EVO_STACK_UMBRELLA` | `CCALC_DOC05_SELF_EVO_STACK_UMBRELLA_v0_1.zip` | `9a0717809029f49df9001dc8ffa1803d9e9bfa1a824d317eebb146cbc7df43b4` | `declared-upstream` |
| `DOC06_RUNTIME_AUTHORITY_STACK_UMBRELLA` | `CCALC_DOC06_RUNTIME_AUTHORITY_STACK_UMBRELLA_v0_1.zip` | `ab95633f1b90f9d032fd231d6cbef3e71b7fe106e0a7fb61d198c2254fc7d307` | `declared-upstream` |
| `DOC07_PUBLIC_EVIDENCE_STACK_UMBRELLA` | `CCALC_DOC07_PUBLIC_EVIDENCE_STACK_UMBRELLA_v0_1.zip` | `b25646d95e45f8a36e5610208d23a535d4c340484431d05efd7f1bf2389fdea3` | `declared-upstream` |
| `DOC08_INTEROPERABILITY_STACK_UMBRELLA` | `CCALC_DOC08_INTEROPERABILITY_STACK_UMBRELLA_v0_1.zip` | `6015526f0ed49519e00c697a5ed375d37fe1aadf222c095f0facf79cb11e669f` | `declared-upstream` |
| `DOC09_DEPLOYMENT_BOUNDARY_MD` | `09_C_DEPLOYMENT_PROFILE_AND_REGULATED_RELEASE_BOUNDARY_v0_1.md` | `16c888da5c4281c24f848246716b6f9f37d15236b909d66fc509090b5e7fd86d` | `present-local` |
| `DOC09A_DEPLOYMENT_SCHEMA_MD` | `09a_DEPLOYMENT_PROFILE_SCHEMA_AND_CHECKER_SEED_v0_1.md` | `c169c6d46fb3f870e3ab8b8e18d29a7797849ee012923ba258d4a537cee7f98e` | `present-local` |
| `DOC09B_DEPLOYMENT_FIXTURE_MUTATION_MD` | `09b_DEPLOYMENT_FIXTURE_PACK_AND_MUTATION_MATRIX_v0_1.md` | `15c179fbbf2d27d78b33eec541853ef2f7a5ab35e9cf2138b879cbec8a819b1f` | `present-local` |
| `DOC09B_DEPLOYMENT_FIXTURE_MUTATION_ZIP` | `CCALC_DEPLOYMENT_FIXTURE_MUTATION_09b_v0_1.zip` | `d61a879e43f4c60ffe7c471121e90cf6e0961dd76c11f467b04a52fe88da2b9d` | `present-local` |


A missing or stale source binding invalidates release use of this package.

---

## 3. Non-claims

This artifact is not:

```text
legal advice
privacy-law certification
safety certification
deployment authorization
standards compliance certification
regulated approval
C-A1 ratification
live substrate truth
proof of completeness
```

It is a release-ledger and withdrawal-drill checker seed for deployment-boundary records.

---

## 4. Core release-state rule

```text
publication != deployment authorization
regulated submission != regulated approval
release ledger != safety certification
release ledger != +
withdrawal != erasure
recall != blame proof
supersession != old-claim upgrade
incident hold != release renewal
```

A release state is a controlled record. It must not be silently edited, upgraded, or used to bypass the underlying `04–09b` gates.

---

## 5. Record classes

`09c` defines these release-ledger record classes:

```text
RegulatedReleaseLedger
ReleaseCandidateRecord
DeploymentDecisionBindingRecord
ReleaseConditionRecord
DistributionSurfaceRecord
ReleaseWatchRecord
IncidentTriggerRecord
IncidentHoldRecord
WithdrawalDrillRecord
RecallDrillRecord
SupersessionRecord
ReleasePublicNoticeRecord
NextReleaseCarryoverRecord
ReleaseNegativeCacheUpdate
ReleaseClaimBoundaryRecord
```

---

## 6. RegulatedReleaseLedger

A `RegulatedReleaseLedger` is an append-only chain of release events.

Minimum fields:

```text
ledger_id
release_id
release_class
deployment_mode
source_bindings
ledger_events[]
release_decision_ref
distribution_surfaces
rollback_route_ref
withdrawal_route_ref
watch_window_ref
negative_cache_state
red_pattern_state
claim_force_ceiling
non_claims
```

Every event is chained:

```text
event_hash = sha256("09c-event-v0.1\0" || canonical_json(event_without_event_hash))
prev_hash_n = event_hash_(n-1)
first prev_hash = GENESIS
seq starts at 1 and is contiguous
```

A broken chain makes the release record inadmissible as clean evidence.

---

## 7. Release classes

```text
REL_CORPUS                  public corpus / package release only
REL_CHECKER_SEED            checker seed release, no production authority
REL_INTERNAL_TRIAL          internal test/trial release
REL_OWNER_FIELD_PILOT       owner-bound field pilot
REL_LIMITED_RUNTIME         limited runtime or limited production release
REL_REGULATED_SUBMISSION    submission to external regulated review; not approval
REL_REGULATED               regulated release candidate; requires regulated review
REL_WITHDRAWN               withdrawn release state
REL_RECALLED                recalled release state
REL_SUPERSEDED              superseded release state
REL_QUARANTINED             release under quarantine
```

---

## 8. Release decision lattice

The checker seed uses a conservative monotonic lattice:

```text
ALLOW_CORPUS_RELEASE < ALLOW_INTERNAL_RELEASE < ALLOW_LIMITED_RELEASE
< ALLOW_REGULATED_SUBMISSION_ONLY
< HOLD_FOR_RELEASE_REVIEW
< REQUIRE_ATTESTED_RELEASE_APPROVER / REQUIRE_REGULATED_REVIEW
< INCIDENT_HOLD < HOLD_NEXT_RELEASE
< SUPERSEDE_RELEASE < WITHDRAW_RELEASE < RECALL_RELEASE
< QUARANTINE_RELEASE < DENY_RELEASE
```

A decision may be stricter than required. It may not be more permissive than the strongest unresolved trigger.

---

## 9. Withdrawal and recall

Withdrawal is a governed action, not deletion.

Required for withdrawal:

```text
trigger reason
release id and hashes
withdrawal route
affected surfaces
public/internal notice policy
negative-cache update where applicable
next-release carryover
human/owner or delegated-human attestation where required
```

Recall is a stronger field/regulated class of withdrawal. It additionally requires:

```text
affected deployment surfaces
operator/customer/user impact class
field-removal or disablement route
watch/incident report
public or institutional notice where applicable
```

---

## 10. Incident hold

Critical incident triggers must enter hold or quarantine.

Required triggers include:

```text
negative-cache hit
unresolved red pattern
continuity rupture or unknown continuity on persistent release
runtime authority anomaly
watch failure
L4 anomaly
public citation drift affecting release claim
regulated-review conflict
+ replacement / binding overclaim
```

Release from hold is not self-certified. It requires attested human/owner/governance review appropriate to release class.

---

## 11. Approver attestation

`09c` preserves the `09a` correction to the string-role seam:

```text
role strings are not enough.
release approver authority requires ApproverAttestationRecord or explicit lower-risk non-approver status.
```

Forbidden:

```text
reviewer_role = HUMAN_ANCHOR as mere string
model/tool output as release approver
institutional interest as regulated approval
repository maintainer action as owner approval unless attested and scoped
```

---

## 12. `+` boundary

The release ledger must not be allowed to simulate the governed binding operator.

Forbidden transformations:

```text
release approved -> therefore c = a + b valid
regulated submission -> therefore +_g ratified
public corpus release -> therefore deployment c exists
withdrawal / recall -> therefore identity rupture by itself
external approval -> therefore anchor replaced
```

`+` remains the governed non-collapsing boundary. Release records may govern distribution. They do not compute, replace, or certify `+`.

---

## 13. Guard registry

The executable guard registry is in:

```text
registry/GUARD_REGISTRY.tsv
```

It covers:

```text
source binding
ledger chain
release decision binding
approver attestation
regulated review
rollback / withdrawal / watch
continuity / runtime authority / witness
negative cache / red pattern
incident hold
withdrawal / recall
claim-force overreach
+ replacement
standards/legal/safety certification overclaim
distribution surface unknown
emergency hold laundering
next-release carryover
withdrawal public notice
```

---

## 14. Fixture and mutation scope

The package contains:

```text
fixtures/cases/*.json
FIXTURE_CATALOG.tsv
MUTATION_MATRIX.tsv
COVERAGE_MATRIX.tsv
src/regulated_release_ledger_withdrawal_checker_v0_1.py
scripts/run_09c_fixtures.py
scripts/run_09c_mutations.py
```

Fixture classes include:

```text
valid corpus release
valid checker/internal release
valid limited release with watch
valid field pilot
valid regulated submission-only
valid withdrawal
valid recall
valid supersession
valid incident hold
C-A10 false-positive control
missing source binding
broken ledger chain
missing deployment decision
string-only approver
model/tool approver
regulated review missing
rollback / withdrawal / watch missing
continuity unknown / rupture
negative-cache hit
red pattern
interop conflict
public citation drift
runtime authority missing
incident without hold
self-certified hold release
withdrawal/recall absent
claim-force overclaim
C-A1 overclaim
+ replacement
standards/legal/safety overclaim
unknown distribution surface
open hold laundered as closed
next-release dirty carryover
withdrawal notice missing
```

---

## 15. Acceptance commands

```text
python3 scripts/run_09c_fixtures.py
python3 scripts/run_09c_mutations.py
sha256sum -c SHA256SUMS.txt
```

All three must pass for this package to be treated as sealed.

---

## 16. Non-claims repeated for public surfaces

A green `09c` run supports only:

```text
release-ledger fixture conformance
withdrawal/recall drill shape conformance
mutation guard coverage for declared adversarial cases
hash-custody of this package
```

It does not support:

```text
legal approval
regulated approval
safety certification
deployment authorization
C-A1
live truth
complete coverage
```

---

## 17. Next layer

The natural next artifact is:

```text
09d_POST_DEPLOYMENT_AUDIT_AND_NEXT_RELEASE_ADMISSION_v0_1
```

`09d` should consume release-ledger outcomes and decide whether a next release may proceed, must hold, must quarantine, or must carry risk forward.
