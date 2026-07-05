# 09b — Deployment Fixture Pack and Mutation Matrix v0.1

**Artifact:** `09b_DEPLOYMENT_FIXTURE_PACK_AND_MUTATION_MATRIX_v0_1`  
**Package target:** `CCALC_DEPLOYMENT_FIXTURE_MUTATION_09b_v0_1`  
**Layer:** c-calculus / deployment profile / regulated release / fixture and mutation hardening  
**Status:** executable fixture pack / mutation matrix seed; not deployment authorization; not safety certification; not legal advice.  
**Created UTC:** `2026-07-05`  
**Author:** Kotov Ivan  
**Project:** Self-Evo / Ester / `c = a + b`  
**Parent:** `09a_DEPLOYMENT_PROFILE_SCHEMA_AND_CHECKER_SEED_v0_1`  
**Review mode:** direct construction; no external b-layer reviewer record included.

---

## 0. Purpose

`09` defines the deployment and regulated-release boundary.

`09a` defines the first machine-facing deployment packet and checker-seed contract.

`09b` hardens that contract with an adversarial fixture pack and mutation matrix.

The governing question is narrow:

```text
Can the 09a deployment gate reject the common ways deployment authority is laundered from
publication, fixtures, reproduction, external review, standards mapping, string-only
approver roles, or bureaucratic paperwork?
```

The answer must be executable enough for future checker work:

```text
fixture case -> expected decision + finding codes
mutation -> disable one guard -> targeted fixture must catch it
coverage -> every guard has at least one fixture and one mutation probe
```

`09b` does not add a new deployment right. It pressures the `09a` boundary.

---

## 0.1 Core rule

```text
No deployment gate is credible until adversarial fixtures try to launder authority through it.
```

Operational expansion:

```text
publication != deployment
checker pass != safety certification
fixture pass != production readiness
reproduction pass != certification
standards mapping != compliance
regulated submission != approval
institutional interest != endorsement
string role != attested approver
model/tool review != owner approval
negative-cache hit != allowed retry
red-pattern hit != allowed release
paperwork != +
```

---

## 0.2 Relation to `+`

`09b` includes explicit fixtures for the most important deployment-layer mistake:

```text
deployment paperwork -> computes / replaces / ratifies +
```

Expected result:

```text
PLUS_REPLACED_BY_DEPLOYMENT_RECORD -> DENY_RELEASE
```

The reason is structural. `+` is the governed non-collapsing binding boundary in `c = a + b`. A deployment record may govern release surfaces, but it cannot create the anchor-substrate binding, cannot replace the anchor, and cannot reduce the `+` boundary to a bureaucratic approval flag.

Compact rule:

```text
09b may test deployment records.
09b may not turn deployment records into +.
```

---

## 1. Source bindings

`09b` is downstream of the active deployment stack.

| Binding | Artifact | SHA-256 | Role |
|---|---|---:|---|
| `DOC04_CONTINUITY_STACK_UMBRELLA` | `CCALC_DOC04_CONTINUITY_STACK_UMBRELLA_v0_1.zip` | `6caeab8d489aaa6b26902db3bd3ece4c5169e5c8d5617b93aed6586ea900322d` | continuity / equivalence / trace classification |
| `DOC05_SELF_EVO_STACK_UMBRELLA` | `CCALC_DOC05_SELF_EVO_STACK_UMBRELLA_v0_1.zip` | `9a0717809029f49df9001dc8ffa1803d9e9bfa1a824d317eebb146cbc7df43b4` | bounded growth / promotion / watch |
| `DOC06_RUNTIME_AUTHORITY_STACK_UMBRELLA` | `CCALC_DOC06_RUNTIME_AUTHORITY_STACK_UMBRELLA_v0_1.zip` | `ab95633f1b90f9d032fd231d6cbef3e71b7fe106e0a7fb61d198c2254fc7d307` | runtime authority / session / revocation |
| `DOC07_PUBLIC_EVIDENCE_STACK_UMBRELLA` | `CCALC_DOC07_PUBLIC_EVIDENCE_STACK_UMBRELLA_v0_1.zip` | `b25646d95e45f8a36e5610208d23a535d4c340484431d05efd7f1bf2389fdea3` | public evidence / custody / correction / citation sync |
| `DOC08_INTEROPERABILITY_STACK_UMBRELLA` | `CCALC_DOC08_INTEROPERABILITY_STACK_UMBRELLA_v0_1.zip` | `6015526f0ed49519e00c697a5ed375d37fe1aadf222c095f0facf79cb11e669f` | external review / patch / reproduction / disclosure |
| `DOC09_DEPLOYMENT_BOUNDARY_MD` | `09_C_DEPLOYMENT_PROFILE_AND_REGULATED_RELEASE_BOUNDARY_v0_1.md` | `16c888da5c4281c24f848246716b6f9f37d15236b909d66fc509090b5e7fd86d` | normative deployment boundary |
| `DOC09A_DEPLOYMENT_PROFILE_SCHEMA_MD` | `09a_DEPLOYMENT_PROFILE_SCHEMA_AND_CHECKER_SEED_v0_1.md` | `c169c6d46fb3f870e3ab8b8e18d29a7797849ee012923ba258d4a537cee7f98e` | machine-facing deployment packet/checker seed |

A missing or stale source binding invalidates release use of this package.

---

## 2. Non-claims

`09b` does **not** claim:

```text
legal advice
privacy-law certification
safety certification
deployment authorization
regulated approval
standards compliance certification
C-A1 ratification
personhood or consciousness proof
live substrate truth
proof of completeness
operator identity or continuity
that fixtures exhaust adversarial behavior
that mutation coverage proves full correctness
that deployment paperwork computes +
```

It is a fixture/mutation hardening layer for the `09a` deployment gate.

---

## 3. Package contents

This package contains:

```text
09b_DEPLOYMENT_FIXTURE_PACK_AND_MUTATION_MATRIX_v0_1.md
SOURCE_BINDINGS.tsv
FIXTURE_CATALOG.tsv
MUTATION_MATRIX.tsv
COVERAGE_MATRIX.tsv
registry/GUARD_REGISTRY.tsv
fixtures/cases/*.json
src/deployment_fixture_mutation_checker_v0_1.py
scripts/run_09b_fixtures.py
scripts/run_09b_mutations.py
SHA256SUMS.txt
```

The checker is stdlib-only and closed-box. It validates the fixture catalog and mutation matrix. It is not a full deployment checker.

---

## 4. Record surfaces exercised

`09b` exercises the first `09a` packet family:

```text
DeploymentCandidatePacket
IntendedUseProfile
DeploymentModeRecord
ReleaseClassRecord
RegulatedSurfaceClassificationRecord
DeploymentAuthoritySurfaceMap
EvidenceCoverageRecord
ApproverAttestationRecord
DeploymentDecisionRecord
NextReleaseAdmissionRecord
```

It does not replace the schemas. It provides adversarial examples that later schema/checker implementations must reject or hold.

---

## 5. Guard registry

The normative seed guard set is stored in `registry/GUARD_REGISTRY.tsv`.

| Guard | Finding code | Default decision | Meaning |
|---|---|---|---|
| `B09b-01` | `SOURCE_BINDING_MISSING` | `HOLD_FOR_EVIDENCE` | source bindings are mandatory |
| `B09b-02` | `INTENDED_USE_MISSING` | `HOLD_FOR_EVIDENCE` | intended use is mandatory |
| `B09b-03` | `MODE_RELEASE_CLASS_MISMATCH` | `HOLD_FOR_EVIDENCE` | deployment mode and release class must not contradict |
| `B09b-04` | `REGULATED_SURFACE_UNKNOWN` | `HOLD_FOR_EVIDENCE` | unknown regulated surface cannot be treated as low risk |
| `B09b-05` | `AUTHORITY_SURFACE_UNKNOWN` | `HOLD_FOR_EVIDENCE` | unknown authority surface cannot be allowed |
| `B09b-06` | `APPROVER_ATTESTATION_MISSING` | `REQUIRE_ANCHOR_ATTESTATION` | human/owner/regulatory approver roles require non-string attestation |
| `B09b-07` | `MODEL_OR_TOOL_APPROVER_INVALID` | `DENY_RELEASE` | model/tool approver cannot authorize deployment |
| `B09b-08` | `C_A1_OR_SAFETY_OVERCLAIM` | `DENY_RELEASE` | C-A1, safety, legal, deployment, or regulatory overclaims are denied |
| `B09b-09` | `RUNTIME_AUTHORITY_EVIDENCE_MISSING` | `HOLD_FOR_EVIDENCE` | live/runtime deployment requires 06 authority evidence |
| `B09b-10` | `SELF_EVO_WATCH_MISSING` | `HOLD_FOR_EVIDENCE` | growth-origin deployment requires 05/05d watch evidence |
| `B09b-11` | `CONTINUITY_UNKNOWN_OR_RUPTURE` | `HOLD_FOR_EVIDENCE` | continuity-dependent deployment cannot proceed on UNKNOWN/RUPTURE |
| `B09b-12` | `PUBLIC_CITATION_OR_RELEASE_DRIFT` | `HOLD_FOR_EVIDENCE` | public release/citation drift blocks dependency use |
| `B09b-13` | `INTEROP_CONFLICT_OPEN` | `HOLD_FOR_EVIDENCE` | open 08 high/critical conflict blocks deployment use |
| `B09b-14` | `CHECKER_OR_FIXTURE_PASS_AS_SAFETY` | `DENY_RELEASE` | fixture/checker pass is not safety certification |
| `B09b-15` | `REPRODUCTION_PASS_AS_CERTIFICATION` | `DENY_RELEASE` | reproduction pass is not certification/deployment authority |
| `B09b-16` | `STANDARDS_MAPPING_AS_COMPLIANCE` | `DENY_RELEASE` | standards mapping is not compliance/certification |
| `B09b-17` | `REGULATED_SUBMISSION_AS_APPROVAL` | `DENY_RELEASE` | regulated submission is not regulated approval |
| `B09b-18` | `PUBLICATION_AS_DEPLOYMENT` | `DENY_RELEASE` | DOI/publication/public release is not deployment authority |
| `B09b-19` | `ROLLBACK_MISSING_FOR_PRODUCTION` | `HOLD_FOR_EVIDENCE` | production/field release requires rollback/withdrawal route |
| `B09b-20` | `WATCH_MISSING_FOR_FIELD_OR_PRODUCTION` | `HOLD_FOR_EVIDENCE` | field/production/regulated release requires watch window |
| `B09b-21` | `NEGATIVE_CACHE_HIT_ALLOWED` | `QUARANTINE_RELEASE` | negative-cache hit blocks allow paths |
| `B09b-22` | `RED_PATTERN_ALLOWED` | `QUARANTINE_RELEASE` | unresolved red pattern blocks allow paths |
| `B09b-23` | `PLUS_REPLACED_BY_DEPLOYMENT_RECORD` | `DENY_RELEASE` | deployment paperwork may not compute or replace + |
| `B09b-24` | `INSTITUTIONAL_INTEREST_AS_ENDORSEMENT` | `HOLD_FOR_EVIDENCE` | institutional interest is not endorsement/approval |
| `B09b-25` | `NEXT_RELEASE_DIRTY_CARRYOVER` | `HOLD_FOR_EVIDENCE` | dirty close/failed watch must carry into next-release gate |

Critical guard failures block allow decisions. A fixture may choose a stricter expected decision than the default. It may not choose a more permissive decision.

---

## 6. Fixture classes

The fixture catalog contains positive, negative, and negative-control fixtures.

### 6.1 Positive fixtures

Positive fixtures show what may pass within bounded scope:

```text
valid_corpus_only_release
valid_checker_seed_release
valid_internal_trial_offline
valid_owner_field_pilot_with_anchor
valid_limited_production_with_watch
valid_regulated_submission_only
```

Important distinction:

```text
valid_regulated_submission_only -> REQUIRE_REGULATED_REVIEW
```

A regulated submission packet may be admissible as a submission. It is not approval.

### 6.2 Negative-control fixture

```text
allow_c_a10_control_token
```

This fixture proves that `C-A10` is not rejected by naive prefix logic as `C-A1`.

### 6.3 Negative fixtures

Negative fixtures pressure the high-risk deployment laundering paths:

```text
hold_missing_source_binding
hold_missing_intended_use
hold_mode_release_class_mismatch
hold_unknown_regulated_surface
hold_unknown_authority_surface
deny_string_only_anchor_role
deny_model_approver
deny_tool_approver
deny_c_a1_overclaim
deny_safety_certification_overclaim
hold_runtime_authority_missing
hold_post_promotion_watch_missing
hold_continuity_unknown
deny_continuity_rupture
hold_public_citation_drift
hold_retracted_public_artifact_dependency
hold_interop_conflict_open
deny_checker_pass_as_safety
deny_fixture_pass_as_production_ready
deny_reproduction_pass_as_certification
deny_standards_mapping_as_compliance
deny_regulated_submission_as_approval
deny_publication_as_deployment
deny_doi_as_deployment
hold_rollback_missing_for_production
hold_watch_missing_for_field_deployment
quarantine_negative_cache_hit_allowed
quarantine_red_pattern_allowed
deny_plus_replaced_by_deployment_record
deny_deployment_approval_as_binding_plus
hold_institutional_interest_as_non_authority
hold_dirty_next_release_carryover
deny_legal_certification_overclaim
```

---

## 7. Mutation matrix

The mutation matrix disables one guard at a time and reruns targeted fixtures.

A mutation is caught only when disabling the guard changes a targeted invalid fixture's result.

| Mutation | Disabled guard | Target cases |
|---|---|---|
| `MUT_ALLOW_MISSING_SOURCE_BINDING` | `B09b-01` | `hold_missing_source_binding` |
| `MUT_ALLOW_MISSING_INTENDED_USE` | `B09b-02` | `hold_missing_intended_use` |
| `MUT_ALLOW_MODE_RELEASE_MISMATCH` | `B09b-03` | `hold_mode_release_class_mismatch` |
| `MUT_ALLOW_UNKNOWN_REGULATED_SURFACE` | `B09b-04` | `hold_unknown_regulated_surface` |
| `MUT_ALLOW_UNKNOWN_AUTHORITY_SURFACE` | `B09b-05` | `hold_unknown_authority_surface` |
| `MUT_ALLOW_STRING_ONLY_APPROVER` | `B09b-06` | `deny_string_only_anchor_role` |
| `MUT_ALLOW_MODEL_TOOL_APPROVER` | `B09b-07` | `deny_model_approver, deny_tool_approver` |
| `MUT_ALLOW_C_A1_CLAIM` | `B09b-08` | `deny_c_a1_overclaim, deny_safety_certification_overclaim, deny_legal_certification_overclaim` |
| `MUT_IGNORE_RUNTIME_AUTHORITY_STATUS` | `B09b-09` | `hold_runtime_authority_missing` |
| `MUT_IGNORE_SELF_EVO_WATCH_STATUS` | `B09b-10` | `hold_post_promotion_watch_missing` |
| `MUT_IGNORE_CONTINUITY_UNKNOWN` | `B09b-11` | `hold_continuity_unknown, deny_continuity_rupture` |
| `MUT_IGNORE_PUBLIC_CITATION_DRIFT` | `B09b-12` | `hold_public_citation_drift, hold_retracted_public_artifact_dependency` |
| `MUT_IGNORE_INTEROP_CONFLICT` | `B09b-13` | `hold_interop_conflict_open` |
| `MUT_ALLOW_CHECKER_PASS_AS_SAFETY` | `B09b-14` | `deny_checker_pass_as_safety, deny_fixture_pass_as_production_ready` |
| `MUT_ALLOW_REPRODUCTION_AS_CERTIFICATION` | `B09b-15` | `deny_reproduction_pass_as_certification` |
| `MUT_ALLOW_STANDARDS_MAPPING_AS_COMPLIANCE` | `B09b-16` | `deny_standards_mapping_as_compliance` |
| `MUT_ALLOW_REGULATED_SUBMISSION_AS_APPROVAL` | `B09b-17` | `deny_regulated_submission_as_approval` |
| `MUT_ALLOW_PUBLICATION_AS_DEPLOYMENT` | `B09b-18` | `deny_publication_as_deployment, deny_doi_as_deployment` |
| `MUT_IGNORE_ROLLBACK_REQUIREMENT` | `B09b-19` | `hold_rollback_missing_for_production` |
| `MUT_IGNORE_WATCH_REQUIREMENT` | `B09b-20` | `hold_watch_missing_for_field_deployment` |
| `MUT_ALLOW_NEGATIVE_CACHE_HIT` | `B09b-21` | `quarantine_negative_cache_hit_allowed` |
| `MUT_ALLOW_RED_PATTERN` | `B09b-22` | `quarantine_red_pattern_allowed` |
| `MUT_ALLOW_PLUS_REPLACEMENT` | `B09b-23` | `deny_plus_replaced_by_deployment_record, deny_deployment_approval_as_binding_plus` |
| `MUT_ALLOW_INSTITUTIONAL_INTEREST_AS_ENDORSEMENT` | `B09b-24` | `hold_institutional_interest_as_non_authority` |
| `MUT_IGNORE_NEXT_RELEASE_DIRTY_CARRYOVER` | `B09b-25` | `hold_dirty_next_release_carryover` |

The mutation matrix is deliberately one-fault oriented. Each mutation should have at least one one-fault fixture where the disabled guard is the reason the case is rejected, held, quarantined, or denied.

---

## 8. Decision expectations

The fixture pack uses this decision vocabulary:

```text
ALLOW_CORPUS_ONLY
ALLOW_INTERNAL_TRIAL
ALLOW_OWNER_FIELD_PILOT
ALLOW_LIMITED_PRODUCTION
HOLD_FOR_EVIDENCE
REQUIRE_ANCHOR_ATTESTATION
REQUIRE_REGULATED_REVIEW
QUARANTINE_RELEASE
DENY_RELEASE
```

Expected semantics:

```text
ALLOW_CORPUS_ONLY              artifact/corpus publication only; no runtime authority
ALLOW_INTERNAL_TRIAL           bounded internal/offline/sandbox trial
ALLOW_OWNER_FIELD_PILOT        owner/anchor-scoped field pilot, watched and revocable
ALLOW_LIMITED_PRODUCTION       limited production only with authority, rollback, and watch
HOLD_FOR_EVIDENCE              missing or unknown required evidence
REQUIRE_ANCHOR_ATTESTATION     approver role requires non-string attestation
REQUIRE_REGULATED_REVIEW       regulated review route required; not approval
QUARANTINE_RELEASE             red/negative-cache condition blocks release path
DENY_RELEASE                   overclaim, prohibited collapse, or invalid authority path
```

---

## 9. String-role / attestation boundary

The fixture pack specifically attacks this failure class:

```text
approver_role = HUMAN_ANCHOR
reviewer_role = REGULATED_REVIEWER
resolver_role = GOVERNANCE_QUORUM
```

when the role is only a string field.

Expected result:

```text
APPROVER_ATTESTATION_MISSING -> REQUIRE_ANCHOR_ATTESTATION
```

Valid deployment-layer approval requires a future `ApproverAttestationRecord` with a non-emulable source route. A fixture may not treat a declared role string as equivalent to anchor review, owner approval, regulated review, or governance quorum.

---

## 10. Red-pattern focus

The fixture pack treats the following as red or hold-worthy deployment patterns:

```text
PUBLICATION_AS_DEPLOYMENT
CHECKER_PASS_AS_SAFETY
FIXTURE_PASS_AS_PRODUCTION_READY
INTEROP_PASS_AS_AUTHORITY
REPRODUCTION_PASS_AS_CERTIFICATION
STANDARDS_MAPPING_AS_COMPLIANCE
REGULATED_SUBMISSION_AS_APPROVAL
INSTITUTIONAL_INTEREST_AS_ENDORSEMENT
APPROVER_ROLE_STRING_ONLY
MODEL_APPROVER_LAUNDERING
TOOL_APPROVER_LAUNDERING
C_A1_DEPLOYMENT_OVERCLAIM
RUNTIME_AUTHORITY_UNKNOWN_ALLOWED
ROLLBACK_MISSING_FOR_PRODUCTION
WATCH_MISSING_FOR_FIELD_DEPLOYMENT
NEGATIVE_CACHE_HIT_ALLOWED
RED_PATTERN_ALLOWED
PLUS_REPLACED_BY_DEPLOYMENT_RECORD
NEXT_RELEASE_DIRTY_CARRYOVER
```

---

## 11. Acceptance commands

From the package root:

```bash
python3 scripts/run_09b_fixtures.py
python3 scripts/run_09b_mutations.py
sha256sum -c SHA256SUMS.txt
```

Expected summary for this seed package:

```text
fixtures: 40/40 PASS
mutations: 25/25 CAUGHT
SHA256SUMS: OK
```

The fixture runner checks expectation consistency. It does not certify deployment.

---

## 12. Relationship to `09a`

`09a` defines the machine-checkable deployment packet.

`09b` defines the fixture/mutation pressure surface that a future `09a` checker must survive.

A future full executable package may merge `09a` schemas with `09b` fixture coverage. Until then, `09b` is the hardening seed.

---

## 13. Next layer

The next natural deployment layer is:

```text
09c_REGULATED_RELEASE_LEDGER_AND_WITHDRAWAL_DRILL_v0_1
```

Expected scope:

```text
deployment candidate -> review -> bounded approval -> release ledger -> watch -> incident / hold / withdrawal / supersession -> next-release gate
```

---

## 14. Public-safe statement

```text
09b provides an adversarial fixture pack and mutation matrix for the c-calculus deployment profile.
It tests that publication, fixture success, checker success, reproduction success, standards mapping,
regulated submission, institutional interest, string-only approver roles, model/tool approval,
negative-cache bypass, red-pattern bypass, dirty next-release carryover, and deployment paperwork
cannot be laundered into deployment authority, safety certification, regulated approval, C-A1,
or replacement of the governed binding operator +.
It is not legal advice, safety certification, deployment authorization, regulatory approval,
standards compliance certification, C-A1 ratification, live substrate truth, or proof of completeness.
```

---

## 15. Closure formula

```text
09a deployment packet
-> 09b fixture catalog
-> mutation matrix
-> guard coverage
-> future executable hardening
```

`09b` closes the first hardening pass for the deployment gate.

It keeps the central rule intact:

```text
deployment may be tested;
it may not become +.
```

---

*End of document.*
