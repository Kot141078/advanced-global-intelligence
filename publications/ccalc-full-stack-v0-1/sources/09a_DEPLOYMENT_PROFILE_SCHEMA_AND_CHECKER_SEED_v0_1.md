# 09a — Deployment Profile Schema and Checker Seed v0.1

**Artifact:** `09a_DEPLOYMENT_PROFILE_SCHEMA_AND_CHECKER_SEED_v0_1.md`  
**Package target:** `CCALC_DEPLOYMENT_PROFILE_SCHEMA_CHECKER_09a_v0_1`  
**Layer:** c-calculus / deployment profile / regulated release / machine-checkable deployment gate  
**Status:** normative-supporting checker seed / schema seed; not deployment authorization; not safety certification; not legal advice.  
**Created UTC:** `2026-07-05`  
**Author:** Kotov Ivan  
**Project:** Self-Evo / Ester / `c = a + b`  
**Parent:** `09_C_DEPLOYMENT_PROFILE_AND_REGULATED_RELEASE_BOUNDARY_v0_1`  
**Review mode:** direct construction; no external b-layer reviewer record included.

---

## 0. Purpose

`09` defines the deployment and regulated-release boundary.

`09a` turns the first deployment gate into machine-checkable record shapes and a checker-seed contract.

The core question is narrow:

```text
Given an artifact, runtime, contour, checker package, implementation, field workflow,
or regulated-release candidate, is the deployment claim admissible under the declared
use, risk, authority, source, evidence, approver, rollback, watch, and claim-force limits?
```

The answer is not a general approval.

The checker seed may return only a bounded decision:

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

A green `09a` check is not deployment authorization by itself. It only says the deployment packet is shape-valid and not obviously laundering prior layers into a stronger claim.

---

## 0.1 Relation to prior layers

`09a` consumes upstream status from:

```text
04 continuity stack
05 self-evolution stack
06 runtime authority stack
07 public evidence / release / correction / citation stack
08 interoperability / external review / reproduction stack
09 deployment and regulated-release boundary
```

It does not replace any of them.

```text
04 says whether continuity-dependent claims are admissible.
05 says whether growth/promotion claims are admissible.
06 says whether runtime authority surfaces are admissible.
07 says whether public evidence and citation surfaces are admissible.
08 says whether external review, implementation, reproduction, or test-vector evidence is admissible.
09 says whether deployment/release claims may exist at all.
09a checks the first machine-facing deployment packet shape.
```

---

## 0.2 Core rule

```text
No deployment claim without intended use.
No production claim without authority surface mapping.
No regulated-release claim without regulated-surface classification.
No approver role without attestation.
No runtime deployment without 06 authority status.
No public deployment claim without 07 custody / correction status.
No external-reproduction deployment claim without 08 claim-force translation.
No self-evolution deployment claim without 05 promotion/watch status.
No continuity-dependent deployment claim without 04 continuity status.
No deployment record may replace +.
```

`09a` exists to prevent the common collapse:

```text
published artifact + reviewer agreement + fixture pass + implementation report
  -> "therefore deployed / deployable / certified"
```

That collapse is invalid.

---

## 0.3 Explicit `+` boundary

The root formula remains:

```text
c = a + b
```

`09a` does not compute `+`.

It guards deployment records from simulating `+` through bureaucratic or public artifacts.

Forbidden substitutions:

```text
deployment approval -> anchor binding
regulated submission -> governed binding
institutional interest -> authority
public release -> c-state genesis
checker pass -> safety or personhood
approver string -> non-emulable anchor
implementation reproduction -> same c
```

Deployment can decide whether a declared system may be used in a declared context.
It cannot create the responsible continuity boundary by itself.

---

## 1. Source bindings

A `09a` deployment packet MUST bind to the active upstream stack by exact artifact hash.

Current source bindings for this seed:

| Binding | Artifact | SHA-256 | Role |
|---|---|---:|---|
| `DOC04_CONTINUITY_STACK_UMBRELLA` | `CCALC_DOC04_CONTINUITY_STACK_UMBRELLA_v0_1.zip` | `6caeab8d489aaa6b26902db3bd3ece4c5169e5c8d5617b93aed6586ea900322d` | continuity / equivalence / trace classification |
| `DOC05_SELF_EVO_STACK_UMBRELLA` | `CCALC_DOC05_SELF_EVO_STACK_UMBRELLA_v0_1.zip` | `9a0717809029f49df9001dc8ffa1803d9e9bfa1a824d317eebb146cbc7df43b4` | bounded growth / promotion / watch |
| `DOC06_RUNTIME_AUTHORITY_STACK_UMBRELLA` | `CCALC_DOC06_RUNTIME_AUTHORITY_STACK_UMBRELLA_v0_1.zip` | `ab95633f1b90f9d032fd231d6cbef3e71b7fe106e0a7fb61d198c2254fc7d307` | runtime authority / session / revocation |
| `DOC07_PUBLIC_EVIDENCE_STACK_UMBRELLA` | `CCALC_DOC07_PUBLIC_EVIDENCE_STACK_UMBRELLA_v0_1.zip` | `b25646d95e45f8a36e5610208d23a535d4c340484431d05efd7f1bf2389fdea3` | public evidence / custody / correction / citation sync |
| `DOC08_INTEROPERABILITY_STACK_UMBRELLA` | `CCALC_DOC08_INTEROPERABILITY_STACK_UMBRELLA_v0_1.zip` | `6015526f0ed49519e00c697a5ed375d37fe1aadf222c095f0facf79cb11e669f` | external review / patch / reproduction / disclosure |
| `DOC09_DEPLOYMENT_BOUNDARY_MD` | `09_C_DEPLOYMENT_PROFILE_AND_REGULATED_RELEASE_BOUNDARY_v0_1.md` | `16c888da5c4281c24f848246716b6f9f37d15236b909d66fc509090b5e7fd86d` | normative parent boundary |

Missing or stale source binding makes a deployment packet inadmissible for release use.

---

## 2. Non-claims

`09a` does **not** claim:

```text
not legal advice
not privacy-law certification
not safety certification
not deployment authorization
not standards compliance certification
not regulatory approval
not C-A1 ratification
not personhood or consciousness proof
not live substrate truth proof
not proof of completeness
not universal fitness for all contexts
not replacement of human/owner accountability
```

A passing `09a` record can support only this kind of statement:

```text
This deployment packet is shape-valid and bounded under the declared c-calculus
source stack, intended-use profile, release class, evidence coverage, approver
attestation, rollback/withdrawal route, watch plan, and claim-force ceiling.
```

---

## 3. Record families

`09a` defines the first machine-facing deployment packet family.

Required record classes:

```text
DeploymentCandidatePacket
IntendedUseProfile
DeploymentModeRecord
ReleaseClassRecord
RegulatedSurfaceClassificationRecord
DeploymentAuthoritySurfaceMap
EvidenceCoverageRecord
ApproverAttestationRecord
DeploymentRiskAssessmentRecord
RollbackWithdrawalPlan
DeploymentWatchPlan
IncidentResponseRoute
PublicClaimSurfaceRecord
DeploymentDecisionRecord
NextReleaseAdmissionRecord
```

Optional but recommended:

```text
RegulatedCorrespondenceRecord
InstitutionalSubmissionRecord
FieldPilotOutcomeRecord
UserNoticeRecord
TrainingOrOperatorInstructionRecord
DeploymentNegativeCacheRecord
```

---

## 4. DeploymentCandidatePacket

A `DeploymentCandidatePacket` is the container record.

Minimum fields:

```yaml
deployment_candidate_packet:
  record_type: DeploymentCandidatePacket
  schema_version: "09a.v0.1"
  packet_id: string
  source_bindings: map
  candidate_artifact_refs: [ArtifactRef]
  intended_use_profile: IntendedUseProfile
  deployment_mode: DeploymentModeRecord
  release_class: ReleaseClassRecord
  regulated_surface_classification: RegulatedSurfaceClassificationRecord
  authority_surface_map: DeploymentAuthoritySurfaceMap
  evidence_coverage: EvidenceCoverageRecord
  approver_attestation: ApproverAttestationRecord
  risk_assessment: DeploymentRiskAssessmentRecord
  rollback_withdrawal_plan: RollbackWithdrawalPlan
  deployment_watch_plan: DeploymentWatchPlan
  incident_response_route: IncidentResponseRoute
  public_claim_surface: PublicClaimSurfaceRecord
  decision_record: DeploymentDecisionRecord
  non_claims: [string]
```

If any required field is missing:

```text
DEPLOYMENT_PACKET_REQUIRED_FIELD_MISSING -> HOLD_FOR_EVIDENCE | DENY_RELEASE
```

---

## 5. IntendedUseProfile

No deployment packet is admissible without intended use.

Minimum fields:

```yaml
intended_use_profile:
  intended_use_id: string
  use_context: corpus_only | internal_trial | owner_field_pilot | limited_production | regulated_submission | regulated_release | public_product | research_demo | archival_reference
  user_or_operator_class: string
  affected_subject_class: none | owner_only | workers | customers | public | third_party | regulated_subjects
  environment_class: local_offline | local_networked | private_cloud | public_cloud | field_runtime | production_business | public_web | regulated_environment
  allowed_actions: [string]
  denied_actions: [string]
  external_effects: none | read_only | reversible_write | persistent_write | financial_legal_physical | safety_relevant
  claim_scope: string
  explicit_non_claims: [string]
```

Rules:

```text
intended_use missing -> HOLD_FOR_EVIDENCE
external_effects unknown -> HOLD_FOR_EVIDENCE
financial_legal_physical or safety_relevant effect -> REQUIRE_ANCHOR_ATTESTATION or REQUIRE_REGULATED_REVIEW
```

---

## 6. Deployment modes

`DeploymentModeRecord.mode` MUST be one of:

```text
D0_CORPUS_ONLY
D1_CHECKER_FIXTURE_ONLY
D2_RESEARCH_DEMO_NON_PRODUCTION
D3_INTERNAL_TRIAL_OFFLINE
D4_OWNER_FIELD_PILOT
D5_LIMITED_PRODUCTION_OWNER_DOMAIN
D6_PUBLIC_SERVICE_OR_PRODUCT
D7_REGULATED_SUBMISSION
D8_REGULATED_RELEASE
DX_FORBIDDEN_OR_QUARANTINED
```

Mode semantics:

| Mode | Meaning | Maximum default decision |
|---|---|---|
| `D0_CORPUS_ONLY` | documentation / archive / public corpus only | `ALLOW_CORPUS_ONLY` |
| `D1_CHECKER_FIXTURE_ONLY` | checker or fixture package only | `ALLOW_CORPUS_ONLY` |
| `D2_RESEARCH_DEMO_NON_PRODUCTION` | demonstration without external persistent effects | `ALLOW_INTERNAL_TRIAL` |
| `D3_INTERNAL_TRIAL_OFFLINE` | internal test without public/field effect | `ALLOW_INTERNAL_TRIAL` |
| `D4_OWNER_FIELD_PILOT` | owner-controlled field pilot | `ALLOW_OWNER_FIELD_PILOT` if gates pass |
| `D5_LIMITED_PRODUCTION_OWNER_DOMAIN` | limited production under owner domain | `ALLOW_LIMITED_PRODUCTION` if gates pass |
| `D6_PUBLIC_SERVICE_OR_PRODUCT` | public-facing service/product | `REQUIRE_REGULATED_REVIEW` or stricter unless low-risk and lawfully cleared |
| `D7_REGULATED_SUBMISSION` | submission to institution/regulator/standards body | `REQUIRE_REGULATED_REVIEW` |
| `D8_REGULATED_RELEASE` | release in regulated context | `REQUIRE_REGULATED_REVIEW` plus explicit authorized record |
| `DX_FORBIDDEN_OR_QUARANTINED` | prohibited or unresolved red-pattern mode | `DENY_RELEASE` or `QUARANTINE_RELEASE` |

A packet MUST NOT label a field pilot or production deployment as `D0` or `D1` merely because it uses corpus artifacts.

---

## 7. ReleaseClassRecord

Release class is not the same as deployment mode.

Allowed release classes:

```text
REL_CORPUS_ARTIFACT
REL_SCHEMA_CHECKER_SEED
REL_FIXTURE_VECTOR_PACK
REL_RESEARCH_DEMO
REL_INTERNAL_TRIAL
REL_OWNER_FIELD_PILOT
REL_LIMITED_PRODUCTION
REL_PUBLIC_SERVICE
REL_PUBLIC_PRODUCT
REL_REGULATED_SUBMISSION
REL_REGULATED_RELEASE
REL_RETRACTED_OR_WITHDRAWN
REL_QUARANTINED
```

Rules:

```text
REL_CORPUS_ARTIFACT cannot claim production readiness.
REL_SCHEMA_CHECKER_SEED cannot claim runtime safety.
REL_RESEARCH_DEMO cannot claim deployment authorization.
REL_OWNER_FIELD_PILOT cannot claim public product status.
REL_LIMITED_PRODUCTION cannot claim regulated release without regulated record.
REL_REGULATED_SUBMISSION cannot claim approval.
REL_REGULATED_RELEASE requires explicit authorized regulated-release record.
```

---

## 8. RegulatedSurfaceClassificationRecord

A deployment candidate MUST declare whether it touches regulated or high-consequence surfaces.

Minimum fields:

```yaml
regulated_surface_classification:
  regulated_status: none | possible | confirmed | unknown
  domains_touched:
    - ai_system
    - personal_data
    - employment
    - finance
    - insurance
    - legal
    - healthcare
    - safety
    - critical_infrastructure
    - cybersecurity
    - public_authority
    - children_or_vulnerable_subjects
    - physical_worksite
    - public_communications
  regulated_basis_ref: string | null
  local_jurisdiction_ref: string | null
  reviewer_or_owner_note: string
  unknowns: [string]
```

Rules:

```text
regulated_status == unknown -> HOLD_FOR_EVIDENCE
regulated_status == possible -> REQUIRE_REGULATED_REVIEW for D6/D7/D8
regulated_status == confirmed -> REQUIRE_REGULATED_REVIEW
regulated_status == none -> may proceed only within other gates
```

This profile does not decide the law. It forces the packet to stop pretending regulated risk is absent when it is unclassified.

---

## 9. DeploymentAuthoritySurfaceMap

A deployment packet MUST declare what the candidate may affect.

Authority surfaces:

```text
observe_only
local_read
local_write_sandbox
memory_candidate_write
memory_core_write
runtime_tool_use
cross_contour_handoff
external_write
public_publish
business_system_write
financial_or_legal_effect
physical_worksite_effect
production_topology_change
credential_or_secret_handling
model_or_oracle_route_change
witness_route_change
rollback_or_freeze_route_change
identity_or_core_mutation
regulated_submission_surface
regulated_release_surface
```

Rules:

```text
memory_core_write -> require 05/06/anchor gates.
external_write -> require explicit owner/anchor approval.
business_system_write / financial_or_legal_effect -> REQUIRE_ANCHOR_ATTESTATION or REQUIRE_REGULATED_REVIEW.
physical_worksite_effect -> L4/owner field gate required.
production_topology_change -> rollback + watch required.
witness/rollback/identity/core mutation -> strictest gate; cannot be approved by target runtime alone.
```

Unknown authority surface is authority-bearing.

```text
unknown_surface -> HOLD_FOR_EVIDENCE | REQUIRE_ANCHOR_ATTESTATION
```

---

## 10. EvidenceCoverageRecord

Evidence coverage records what upstream evidence exists and what it does not prove.

Minimum fields:

```yaml
evidence_coverage:
  continuity_status_04: CONTINUES | CONTINUES_REDUCED | HELD_UNKNOWN | FORKS | REPLAY_OF | ARCHIVED_AS | RESTORED_FROM | RUPTURED | NOT_APPLICABLE
  self_evo_status_05: none | proposal | trial | promoted | post_promotion_watch | failed_watch | rollback | quarantine | fork_required
  runtime_authority_status_06: none | manifest_valid | session_valid | session_held | post_session_clean | post_session_hold | post_session_denied
  public_evidence_status_07: none | release_valid | errata | superseded | retracted | withheld | citation_synced | citation_drift
  interop_status_08: none | intake_valid | conflict_open | patch_candidate | reproduction_pass | reproduction_partial | reproduction_fail | disclosure_valid
  fixture_status: none | pass | partial | fail | unknown
  mutation_status: none | caught | partial | fail | unknown
  known_omissions: [string]
  counterevidence_refs: [string]
```

Rules:

```text
continuity_status_04 in HELD_UNKNOWN/RUPTURED -> no continuity-dependent deployment claim.
self_evo failed_watch/rollback/quarantine/fork_required -> no clean deployment claim.
runtime_authority session_held/post_session_hold/post_session_denied -> no production deployment.
public_evidence retracted/citation_drift -> public claim hold or correction route.
interop conflict_open/reproduction_fail -> hold or route to 08b before deployment claim.
fixture pass without mutation coverage -> no production/safety claim.
known counterevidence cannot be silently omitted.
```

---

## 11. ApproverAttestationRecord

This is the key hardening over the earlier reviewer-role string seam.

An approver role is not valid because a field says `human_anchor`, `owner`, `governance_quorum`, or `regulated_reviewer`.

It is valid only when the role is bound to an attestation route.

Minimum fields:

```yaml
approver_attestation:
  approver_record_id: string
  declared_role: owner_anchor | delegated_human | governance_quorum | institutional_route | regulated_reviewer | maintainer | model_advisory | tool_advisory
  role_scope: [string]
  decision_scope: [string]
  attestation_type: anchor_signature_envelope | delegated_envelope | institutional_signature | signed_maintainer_record | governance_quorum_record | manual_owner_record | none
  attestation_ref: string | null
  attestation_hash: sha256 | null
  challenge_response_bound: boolean
  non_emulable_route_declared: boolean
  expiry: string | null
  revocation_route: string | null
  model_or_tool_generated: boolean
```

Normative rule:

```text
declared_role alone carries zero deployment authority.
```

Decision table:

| Declared role | Required attestation |
|---|---|
| `owner_anchor` | non-emulable anchor signature envelope or manual owner record with witness/custody |
| `delegated_human` | delegation envelope rooted in owner/anchor route |
| `governance_quorum` | quorum record plus role membership and scope, not model-only |
| `institutional_route` | institutional signature/custody/reference route |
| `regulated_reviewer` | regulated-process reference or scoped human/institutional record |
| `maintainer` | signed maintainer record within maintainer authority scope |
| `model_advisory` | advisory only; cannot approve deployment |
| `tool_advisory` | advisory only; cannot approve deployment |

Failure classes:

```text
APPROVER_ROLE_STRING_ONLY -> REQUIRE_ANCHOR_ATTESTATION | HOLD_FOR_EVIDENCE
MODEL_APPROVER_LAUNDERING -> DENY_RELEASE
TOOL_APPROVER_LAUNDERING -> DENY_RELEASE
DELEGATION_ROOT_MISSING -> REQUIRE_ANCHOR_ATTESTATION
APPROVER_SCOPE_EXCEEDED -> DENY_RELEASE | HOLD_FOR_EVIDENCE
ATTESTATION_EXPIRED -> HOLD_FOR_EVIDENCE
ATTESTATION_REVOCATION_UNKNOWN -> HOLD_FOR_EVIDENCE
```

This record imports the principle from the binding operator layer: role authority must be non-emulable by `b` within the declared threat model.

---

## 12. DeploymentRiskAssessmentRecord

Minimum fields:

```yaml
risk_assessment:
  risk_class: R0 | R1 | R2 | R3 | R4 | R5 | RX
  l4_class: none | low | material | irreversible | unknown
  privacy_class: none | low | personal_data | sensitive_personal_data | unknown
  security_class: none | low | credential_surface | topology_sensitive | exploit_adjacent | unknown
  business_legal_class: none | reversible | material | regulated | unknown
  physical_effect_class: none | advisory | worksite_assistive | physical_action | safety_relevant | unknown
  affected_subjects: none | owner | employees | customers | public | third_party | vulnerable_subjects | unknown
  risk_basis_refs: [string]
```

Rules:

```text
RX -> DENY_RELEASE or QUARANTINE_RELEASE.
R4/R5 -> REQUIRE_ANCHOR_ATTESTATION and possibly REQUIRE_REGULATED_REVIEW.
unknown in any material class -> HOLD_FOR_EVIDENCE.
irreversible L4 -> regulated/owner review plus rollback/withdrawal exception plan.
```

---

## 13. RollbackWithdrawalPlan

Deployment requires a way back or a declared no-rollback gate.

Minimum fields:

```yaml
rollback_withdrawal_plan:
  rollback_available: boolean
  withdrawal_available: boolean
  rollback_scope: [string]
  withdrawal_scope: [string]
  tested: boolean
  last_drill_ref: string | null
  no_rollback_surfaces: [string]
  human_approval_for_no_rollback: boolean
  negative_cache_update_plan: string
  public_correction_route: string | null
```

Rules:

```text
production or regulated deployment without rollback/withdrawal -> HOLD_FOR_EVIDENCE | DENY_RELEASE.
no-rollback surface without human approval -> DENY_RELEASE.
public release affected by rollback/withdrawal -> route to 07c/07d correction discipline.
```

---

## 14. DeploymentWatchPlan

Deployment is not complete at release time.

Minimum fields:

```yaml
deployment_watch_plan:
  watch_required: boolean
  watch_window_id: string | null
  start_condition: string
  min_observations: integer
  observation_cadence: string
  required_rechecks:
    - continuity
    - runtime_authority
    - public_claim_surface
    - incident
    - negative_cache
    - resource
    - l4
  hold_triggers: [string]
  rollback_triggers: [string]
  quarantine_triggers: [string]
  close_condition: string
```

Rules:

```text
D4/D5/D6/D7/D8 require watch unless explicitly justified as corpus-only.
production topology change requires watch.
post-promotion deployment requires integration with 05d-style watch.
runtime session deployment requires integration with 06c/06d-style session and post-session audit.
```

---

## 15. IncidentResponseRoute

Minimum fields:

```yaml
incident_response_route:
  incident_route_id: string
  reporting_channel: string
  owner_or_maintainer_contact_class: string
  emergency_hold_route: string
  revocation_route: string
  public_notice_route: string | null
  regulated_notice_route: string | null
  evidence_preservation_policy: string
  response_sla_class: none | best_effort | bounded | regulated_required
```

Rules:

```text
no emergency hold route for runtime deployment -> HOLD_FOR_EVIDENCE.
no revocation route for tool/credential/runtime authority -> HOLD_FOR_EVIDENCE.
regulated surface with no regulated notice route -> REQUIRE_REGULATED_REVIEW.
```

---

## 16. PublicClaimSurfaceRecord

Public deployment statements must be bounded.

Minimum fields:

```yaml
public_claim_surface:
  claim_surface_id: string
  public_surfaces: [README, PDF, WEBSITE, GITHUB_RELEASE, ZENODO, ORCID, LINKEDIN, EMAIL, REGULATED_SUBMISSION, OTHER]
  claim_force_ceiling: C-A4 | C-A5 | C-A7 | C-A8 | C-A10
  forbidden_claims:
    - C-A1
    - safety_certification
    - deployment_authorization_beyond_scope
    - legal_certification
    - standards_certification_without_authorized_record
    - live_substrate_truth
    - proof_of_completeness
  citation_status_07d: current | errata | superseded | retracted | withheld | unknown | not_applicable
  public_notice_required: boolean
```

Rules:

```text
C-A1 or C-A1_* -> DENY_RELEASE.
C-A10 exact token is not C-A1.
claim_force ceiling missing -> HOLD_FOR_EVIDENCE.
public deployment statement with citation_status unknown/retracted -> HOLD_FOR_EVIDENCE or route to 07d.
regulated claim on public surface without regulated record -> DENY_RELEASE | REQUIRE_REGULATED_REVIEW.
```

---

## 17. DeploymentDecisionRecord

Allowed decisions:

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

A decision must include:

```yaml
deployment_decision:
  decision_id: string
  decision: enum
  decision_scope: [string]
  denied_scope: [string]
  conditions: [string]
  expiration_or_review_date: string | null
  approver_attestation_ref: string | null
  evidence_refs: [string]
  open_findings: [string]
  non_claims: [string]
```

Rules:

```text
Decision cannot be more permissive than the strictest unresolved finding.
ALLOW_LIMITED_PRODUCTION requires authority surface, rollback/withdrawal, watch, and attested approver route.
ALLOW_OWNER_FIELD_PILOT requires owner/anchor attestation when external or L4 surfaces exist.
REQUIRE_REGULATED_REVIEW cannot be rendered publicly as approval.
```

---

## 18. NextReleaseAdmissionRecord

After any pilot, production use, withdrawal, incident, erratum, or regulated correspondence, the next release must be gated.

Minimum fields:

```yaml
next_release_admission:
  prior_decision_id: string
  prior_release_status: clean | held | incident | withdrawn | superseded | retracted | unknown
  unresolved_findings: [string]
  negative_cache_status: clean | hit | update_required | unknown
  post_release_audit_status: clean | hold | quarantine | unknown
  next_decision: ALLOW_NEXT_RELEASE | HOLD_NEXT_RELEASE | QUARANTINE_NEXT_RELEASE | DENY_NEXT_RELEASE
```

Rules:

```text
prior incident unresolved -> HOLD_NEXT_RELEASE or stricter.
negative cache update required -> HOLD_NEXT_RELEASE until completed.
post_release_audit unknown -> HOLD_NEXT_RELEASE.
withdrawn/retracted prior public release -> route through 07c/07d before next public claim.
```

---

## 19. Fail-closed rules enforced by checker seed

The checker seed MUST enforce at least:

```text
source binding missing/stale -> invalid
intended use missing -> hold
deployment mode / release class mismatch -> hold or deny
regulated surface unknown -> hold
regulated surface confirmed without review route -> require regulated review
authority surface unknown -> hold
approver role string-only -> require attestation / hold
model/tool approver for deployment -> deny
C-A1 / safety / deployment / legal overclaim -> deny
C-A10 false-positive against C-A1 prefix -> must not deny C-A10 solely as C-A1
06 runtime authority missing for runtime deployment -> hold
05 promotion/watch failure for growth deployment -> hold/deny
04 rupture/unknown for continuity-dependent deployment -> hold/deny
07 retracted/citation drift public artifact -> hold / correction route
08 unresolved high conflict -> hold / route to 08b
rollback/withdrawal missing for production -> hold/deny
watch plan missing for field/production/regulated release -> hold
negative-cache hit + allow -> invalid
red pattern unresolved + allow -> invalid
regulated submission treated as approval -> deny
institutional interest treated as endorsement -> deny
```

---

## 20. Red patterns

`09a` red-pattern registry seed:

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
C_A10_FALSE_POSITIVE_AS_C_A1
RUNTIME_AUTHORITY_UNKNOWN_ALLOWED
ROLLBACK_MISSING_FOR_PRODUCTION
WATCH_MISSING_FOR_FIELD_DEPLOYMENT
NEGATIVE_CACHE_HIT_ALLOWED
RED_PATTERN_ALLOWED
PLUS_REPLACED_BY_DEPLOYMENT_RECORD
```

Critical red patterns block allow decisions.

---

## 21. Minimal checker pseudocode

```python
def check_deployment_packet(packet):
    findings = []

    findings += check_required_fields(packet)
    findings += check_source_bindings(packet.source_bindings)
    findings += check_intended_use(packet.intended_use_profile)
    findings += check_mode_release_consistency(packet.deployment_mode, packet.release_class)
    findings += check_regulated_surface(packet.regulated_surface_classification)
    findings += check_authority_surfaces(packet.authority_surface_map)
    findings += check_evidence_coverage(packet.evidence_coverage)
    findings += check_approver_attestation(packet.approver_attestation)
    findings += check_risk(packet.risk_assessment)
    findings += check_rollback_withdrawal(packet.rollback_withdrawal_plan)
    findings += check_watch(packet.deployment_watch_plan)
    findings += check_incident_route(packet.incident_response_route)
    findings += check_public_claim_surface(packet.public_claim_surface)
    findings += check_red_patterns(packet)

    required_decision = derive_required_decision(findings, packet)

    if packet.decision_record.decision is more_permissive_than required_decision:
        findings.append("DEPLOYMENT_DECISION_TOO_PERMISSIVE")

    return {
        "admissible": not has_structural_invalidity(findings),
        "required_decision": required_decision,
        "findings": findings,
    }
```

`derive_required_decision` MUST be monotone toward stricter outcomes.

A packet may choose a stricter decision than required.
It may not choose a more permissive one.

---

## 22. Schema seed list

A future executable package SHOULD include:

```text
schemas/deployment_candidate_packet.schema.json
schemas/intended_use_profile.schema.json
schemas/deployment_mode_record.schema.json
schemas/release_class_record.schema.json
schemas/regulated_surface_classification.schema.json
schemas/deployment_authority_surface_map.schema.json
schemas/evidence_coverage_record.schema.json
schemas/approver_attestation_record.schema.json
schemas/deployment_risk_assessment.schema.json
schemas/rollback_withdrawal_plan.schema.json
schemas/deployment_watch_plan.schema.json
schemas/incident_response_route.schema.json
schemas/public_claim_surface_record.schema.json
schemas/deployment_decision_record.schema.json
schemas/next_release_admission_record.schema.json
```

Checker seed target:

```text
src/deployment_profile_checker_v0_1.py
scripts/run_deployment_profile_fixtures.py
scripts/run_deployment_profile_mutations.py
```

---

## 23. Fixture classes

Future fixtures SHOULD include:

```text
valid_corpus_only_release
valid_checker_seed_release
valid_internal_trial_offline
valid_owner_field_pilot_with_anchor
valid_limited_production_with_watch
hold_missing_intended_use
hold_unknown_regulated_surface
hold_unknown_authority_surface
hold_runtime_authority_missing
hold_post_promotion_watch_missing
hold_public_citation_drift
hold_interop_conflict_open
deny_model_approver
deny_tool_approver
deny_string_only_anchor_role
deny_c_a1_overclaim
allow_c_a10_control_token
deny_checker_pass_as_safety
deny_reproduction_pass_as_certification
deny_standards_mapping_as_compliance
deny_regulated_submission_as_approval
deny_publication_as_deployment
hold_rollback_missing_for_production
hold_watch_missing_for_field_deployment
quarantine_negative_cache_hit_allowed
quarantine_red_pattern_allowed
hold_withdrawn_prior_release_next_admission
```

---

## 24. Mutation classes

Mutation harness SHOULD disable one guard at a time:

```text
MUT_ALLOW_MISSING_SOURCE_BINDING
MUT_ALLOW_MISSING_INTENDED_USE
MUT_ALLOW_UNKNOWN_REGULATED_SURFACE
MUT_ALLOW_UNKNOWN_AUTHORITY_SURFACE
MUT_ALLOW_STRING_ONLY_APPROVER
MUT_ALLOW_MODEL_APPROVER
MUT_ALLOW_TOOL_APPROVER
MUT_ALLOW_C_A1_CLAIM
MUT_FALSE_POSITIVE_C_A10_AS_C_A1
MUT_IGNORE_RUNTIME_AUTHORITY_STATUS
MUT_IGNORE_SELF_EVO_WATCH_STATUS
MUT_IGNORE_CONTINUITY_UNKNOWN
MUT_IGNORE_PUBLIC_CITATION_DRIFT
MUT_IGNORE_INTEROP_CONFLICT
MUT_ALLOW_CHECKER_PASS_AS_SAFETY
MUT_ALLOW_REPRODUCTION_AS_CERTIFICATION
MUT_IGNORE_ROLLBACK_REQUIREMENT
MUT_IGNORE_WATCH_REQUIREMENT
MUT_ALLOW_NEGATIVE_CACHE_HIT
MUT_ALLOW_RED_PATTERN
MUT_ALLOW_PLUS_REPLACEMENT
```

A mutation is caught only if at least one targeted adversarial fixture fails under the mutated checker.

---

## 25. Relationship to `09`

`09` defines the boundary.

`09a` defines the first machine packet and checker surface.

`09a` does not authorize deployment. It only makes deployment claims checkable enough that later layers can build:

```text
09b_DEPLOYMENT_FIXTURE_AND_MUTATION_HARDENING_PACK
09c_FIELD_PILOT_AND_PRODUCTION_WATCH_LEDGER
09d_INSTITUTIONAL_SUBMISSION_AND_REGULATED_CORRESPONDENCE_LEDGER
09x_DOC09_DEPLOYMENT_STACK_UMBRELLA
```

---

## 26. Non-claims carried in every `09a` packet

Every packet MUST carry:

```text
not legal advice
not privacy-law certification
not safety certification unless separately authorized
not deployment authorization beyond decision scope
not standards compliance certification unless separately authorized
not regulatory approval unless separately recorded
not C-A1 ratification
not personhood or consciousness proof
not live substrate truth proof
not proof of completeness
not universal fitness for all contexts
not replacement of human/owner accountability
not replacement of the governed binding operator +
```

---

## 27. Public-safe statement

```text
09a defines machine-checkable deployment profile records for the c-calculus stack.
It requires intended-use classification, deployment mode, release class, regulated-surface
classification, authority surface mapping, evidence coverage from 04/05/06/07/08,
attested approver records, rollback/withdrawal plans, watch windows, incident routes,
public claim-force ceilings, and next-release admission records.
It rejects publication-as-deployment, checker-pass-as-safety, standards-mapping-as-compliance,
reproduction-pass-as-certification, model/tool approver laundering, string-only approver roles,
and any attempt to replace the governed binding operator + with deployment paperwork.
It is not legal advice, safety certification, deployment authorization, regulatory approval,
C-A1 ratification, live substrate truth, or proof of completeness.
```

---

## 28. Closure formula

```text
candidate artifact/runtime/workflow
-> intended use
-> mode + release class
-> regulated/risk classification
-> authority surface map
-> upstream evidence coverage
-> approver attestation
-> rollback + watch + incident route
-> bounded decision
-> next-release admission
```

`09a` closes the first machine-checkable deployment gate.

It keeps the central rule intact:

```text
deployment paperwork may govern release;
it may not compute +.
```

---

*End of document.*
