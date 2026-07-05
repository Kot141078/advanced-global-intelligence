# 09 — C Deployment Profile and Regulated Release Boundary v0.1

**Artifact:** `09_C_DEPLOYMENT_PROFILE_AND_REGULATED_RELEASE_BOUNDARY_v0_1.md`  
**Package target:** `CCALC_DEPLOYMENT_PROFILE_REGULATED_RELEASE_09_v0_1`  
**Layer:** c-calculus / deployment profile / regulated release / field-operation boundary  
**Status:** normative draft / release-candidate seed; not an executable checker package  
**Created UTC:** `2026-07-05`  
**Author:** Kotov Ivan  
**Project:** Self-Evo / Ester / `c = a + b`  
**Review mode:** direct construction; no external b-layer reviewer record included.  

---

## 0. Purpose

The continuity stack (`04`) defines continuity, equivalence, trace status, replay, archive, fork, and rupture.

The self-evolution stack (`05`) defines bounded growth, proposal admission, promotion, rollback drill, and post-promotion watch.

The runtime-authority stack (`06`) defines authority surfaces, multi-contour deployment, sessions, emergency hold, revocation, and post-session audit.

The public-evidence stack (`07`) defines disclosure, redaction, release custody, errata, supersession, retraction, and citation sync.

The interoperability stack (`08`) defines external review intake, conflict resolution, patch intake, reproduction mapping, implementation disclosure, and test-vector registry.

`09` answers a different question:

```text
When may a c-calculus artifact, runtime, contour, tool package, checker, implementation,
service, or field workflow move from corpus/review/reproduction into deployment,
pilot use, production use, institutional submission, or regulated release?
```

The answer is not:

```text
it has a DOI
it passed fixtures
it has a GitHub release
an external reviewer agreed
an implementation reproduced it
an institution asked about it
it runs locally
it is useful in the field
```

The answer is a governed deployment boundary:

```text
release candidate
-> intended-use profile
-> deployment authority profile
-> risk and regulated-surface classification
-> evidence coverage
-> human/owner and lawful gate where required
-> rollback / withdrawal / incident route
-> monitoring window
-> release decision
-> post-release audit and next-release admission
```

Deployment is not publication. Regulated release is not ontology. Certification language is not `+`.

---

## 0.1 Core rule

```text
Public release supports scrutiny.
Interoperability supports reproduction.
Runtime authority supports bounded execution.
Deployment requires a separate deployment gate.
Regulated release requires a separate lawful / institutional / owner-authorized gate where applicable.
```

Compact form:

```text
artifact_pass != deployment_authorization
review_pass   != regulated_release
interop_pass  != production_readiness
field_success != universal safety
```

A deployment claim must preserve the difference between:

```text
architecture
checker seed
public artifact
local runtime
field pilot
production deployment
regulated release
certified product
lawful institutional authorization
```

No layer may silently collapse these classes.

---

## 0.2 Explicit bridge to `c = a + b`

The root formula remains:

```text
c = a + b
```

`09` does not redefine `+`.

It protects `+` from a new laundering path:

```text
public release / deployment approval / external review / standards mapping / regulator interest
  -> treated as if it binds a and b into c
```

This is forbidden.

Deployment records may govern where a contour acts. They do not create the contour. Regulated release records may govern whether an artifact may be used in a declared context. They do not replace the accountable anchor.

```text
certification-like evidence is not +
public approval is not +
regulated submission is not +
deployment manifest is not +
```

`+` remains the governed non-collapsing binding boundary between accountable anchor and substrate. A deployment profile may constrain or evidence `b` and runtime surfaces; it may not compute away `a`, impersonate `a`, or convert external acceptance into binding authority.

### 0.2.1 Protected incompleteness of `+`

The prior stacks formalize the perimeter around `+`: binding certificates, causal state, continuity, growth, runtime authority, public custody, and review intake.

`09` inherits the same rule:

```text
complete perimeter does not mean computable replacement of +.
```

If a release process can fully replace anchor consent, review, and binding authority with a deployment checklist, then it has collapsed `+` into `b`.

That is not a successful formalization. It is a type error.

---

## 0.3 Earth paragraph

A construction company can publish a method statement, show test reports, cite standards, pass an internal inspection, and demonstrate a successful lift. None of that alone means the method is approved for every site, every load, every crane, every crew, and every legal context.

A real deployment needs a site-specific plan: intended use, load class, personnel, responsibility, permits, equipment condition, inspection route, emergency stop, rollback or shoring plan, and the person who signs for the actual job.

`c` deployment is the same class of problem.

A corpus package may be sound as a document. A checker may pass its fixtures. A runtime may work in one field context. None of that automatically authorizes production, regulated release, high-risk use, or transfer to another contour. Deployment authority lives in the bounded joint between evidence, intended use, responsibility, and rollback.

---

## 0.4 Hidden bridges

### 0.4.1 Certification-boundary bridge

A certification-like artifact is a claim about a bounded assessment context. It is not universal truth.

Therefore:

```text
assessment scope must be explicit;
claim-force must be bounded;
non-claims must be carried forward;
missing scope fails closed.
```

### 0.4.2 Ashby bridge

Deployment introduces new disturbance variety:

```text
real users
operators
business systems
legal exposure
physical consequences
resource pressure
third-party data
runtime drift
environment change
incident response
support burden
```

Governance variety must increase accordingly. A public artifact checker is under-variety for production deployment.

### 0.4.3 Transition-memory bridge

A deployment can look clean at release time while failing through local transitions:

```text
pilot_success -> production_expansion_without_review
unknown_incident -> public_claim_preserved
operator_override -> unlogged authority growth
negative_cache_hit -> retry under new product name
regulatory_comment -> marketing claim
```

Therefore deployment status is a lifecycle trace, not a one-time badge.

### 0.4.4 Information-boundary bridge

A release decision compresses evidence into an operational permission. Compression is valid only if omitted details are non-authority-bearing.

If the release decision hides unknown intended use, untested runtime surfaces, missing rollback, private counterevidence, or unresolved red patterns, it is not release governance. It is authority compression.

---

## 1. Source bindings

This draft is downstream of the current closed stack:

| Binding | Artifact | SHA-256 | Role |
|---|---|---:|---|
| `DOC04_CONTINUITY_STACK_UMBRELLA` | `CCALC_DOC04_CONTINUITY_STACK_UMBRELLA_v0_1.zip` | `6caeab8d489aaa6b26902db3bd3ece4c5169e5c8d5617b93aed6586ea900322d` | continuity/equivalence/claim-gate stack |
| `DOC05_SELF_EVO_STACK_UMBRELLA` | `CCALC_DOC05_SELF_EVO_STACK_UMBRELLA_v0_1.zip` | `9a0717809029f49df9001dc8ffa1803d9e9bfa1a824d317eebb146cbc7df43b4` | bounded growth/proposal/promotion/watch stack |
| `DOC06_RUNTIME_AUTHORITY_STACK_UMBRELLA` | `CCALC_DOC06_RUNTIME_AUTHORITY_STACK_UMBRELLA_v0_1.zip` | `ab95633f1b90f9d032fd231d6cbef3e71b7fe106e0a7fb61d198c2254fc7d307` | runtime authority/session/revocation stack |
| `DOC07_PUBLIC_EVIDENCE_STACK_UMBRELLA` | `CCALC_DOC07_PUBLIC_EVIDENCE_STACK_UMBRELLA_v0_1.zip` | `b25646d95e45f8a36e5610208d23a535d4c340484431d05efd7f1bf2389fdea3` | public evidence/release/correction/citation-sync stack |
| `DOC08_INTEROPERABILITY_STACK_UMBRELLA` | `CCALC_DOC08_INTEROPERABILITY_STACK_UMBRELLA_v0_1.zip` | `6015526f0ed49519e00c697a5ed375d37fe1aadf222c095f0facf79cb11e669f` | interoperability/external review/reproduction/disclosure stack |

A missing or stale source binding invalidates release use of this profile.

---

## 2. Non-claims

This document does **not** claim:

```text
legal advice
privacy-law certification
safety certification
deployment authorization by itself
standards compliance certification
regulated-market authorization
C-A1 ratification
proof of consciousness or personhood
live substrate truth
proof of completeness
fitness for any specific regulated context
permission to operate any runtime, tool, model, agent mesh, or physical/business workflow
```

This document defines the project-level deployment and regulated-release boundary. Actual legal, regulatory, contractual, safety, professional, or institutional authorization requires the appropriate external process and accountable human/institutional route.

---

## 3. Boundary axiom

```text
Publication is not deployment.
Deployment is not regulated release.
Regulated release is not C-A1.
External approval is not +.
```

A deployment profile may admit an artifact or runtime into a declared operational context.

It may not:

```text
raise claim force beyond evidence;
replace the human/owner anchor;
turn checker pass into safety certification;
turn external implementation into same c;
turn standards mapping into legal compliance;
turn public release into production authority;
turn regulated correspondence into endorsement;
turn institutional interest into permission;
collapse + into a deployment checklist.
```

---

## 4. Core terms

### 4.1 DeploymentCandidate

A `DeploymentCandidate` is an artifact, runtime, package, contour, service, workflow, adapter, checker, or implementation proposed for use outside its current review boundary.

A candidate is not deployed merely because it exists or passes tests.

### 4.2 IntendedUseProfile

An `IntendedUseProfile` declares what the candidate is for, where it may be used, who operates it, who is affected, what it may touch, and what it must not claim.

No intended use means no deployment decision.

### 4.3 DeploymentProfile

A `DeploymentProfile` is a governed record binding:

```text
candidate identity
intended use
deployment mode
runtime authority surfaces
public evidence status
interop/reproduction evidence
operator/owner approval
risk class
rollback / withdrawal route
monitoring plan
claim-force ceiling
non-claims
```

### 4.4 RegulatedRelease

A `RegulatedRelease` is a deployment or public offering that touches a regulated, institutional, safety-sensitive, legal, financial, employment, health, public-sector, physical, security, commercial, or otherwise externally governed context.

This profile does not decide external law. It requires that such contexts be routed to the appropriate external gate and not laundered through corpus evidence.

### 4.5 DeploymentAuthorityDecision

A `DeploymentAuthorityDecision` is a bounded decision over one candidate and one intended-use profile.

It may allow, narrow, hold, deny, quarantine, withdraw, or require external review.

It is not a universal license.

### 4.6 RegulatedReleasePacket

A `RegulatedReleasePacket` is the bundle of records required before a regulated release can be submitted, piloted, publicly offered, or deployed.

It is a dossier, not a certification.

### 4.7 DeploymentWatchWindow

A `DeploymentWatchWindow` is the bounded monitoring interval after pilot, production release, or regulated release.

Deployment is not complete at launch. Launch opens observation, incident, rollback, withdrawal, and next-release gates.

---

## 5. Deployment mode registry

The following deployment modes are normative for v0.1.

| Mode | Meaning | Default decision floor |
|---|---|---|
| `D0_CORPUS_ONLY` | Documents, schemas, fixtures, examples, public evidence only | not deployed |
| `D1_REPRODUCTION_ONLY` | External reproduction/test-vector use without live effects | interop evidence only |
| `D2_INTERNAL_SANDBOX` | Internal dry-run or sandbox use | owner/operator review |
| `D3_INTERNAL_FIELD_ASSIST` | Owner-supervised field support with human decision gate | runtime authority + human gate |
| `D4_LIMITED_PILOT` | Bounded pilot with selected operators/users | rollback + monitoring + incident route |
| `D5_PRODUCTION_OPERATIONAL` | Persistent operational use in business/field/public service | deployment authority + post-release audit |
| `D6_REGULATED_RELEASE` | Use in externally governed or high-impact context | regulated packet + lawful/institutional gate |
| `D7_PUBLIC_PRODUCT_OR_SERVICE` | Publicly offered product/service/API/tool | public release + deployment + support/withdrawal route |
| `D8_WITHDRAWN_OR_RETIRED` | No new deployment; historical/citation only | withdrawal/citation sync |
| `DX_PROHIBITED` | Disallowed by policy, law, safety, privacy, or project boundary | deny/quarantine |

A candidate may move upward only through explicit decision records.

```text
D0 -> D5
```

without intermediate gates is invalid by default.

---

## 6. Regulated and high-consequence surfaces

A deployment candidate touches a regulated or high-consequence surface if it may affect:

```text
physical safety
worker/customer/public impact
legal rights or obligations
financial transactions or accounting
employment, hiring, evaluation, discipline, or access decisions
health, medical, psychological, disability, or care context
education, scoring, admission, or credentialing
public authority / government / municipal services
critical infrastructure or energy / transport / communications
cybersecurity, identity, authentication, credentials, access control
security-sensitive topology or dual-use capability
publicly offered AI service or automated decision workflow
large-scale data processing or third-party personal data
external write into repositories, email, calendars, documents, contracts, business systems, or public surfaces
physical actuators, robots, machinery, vehicles, construction equipment, or site operations
identity/core, memory-core, runtime authority, witness, rollback, or L4 perimeter
```

If classification is uncertain:

```text
UNKNOWN_SURFACE -> HOLD_FOR_CLASSIFICATION
```

Unknown is not low risk.

---

## 7. Deployment release classes

### 7.1 `REL_CORPUS`

Corpus artifact only. May be published, cited, reproduced, or reviewed under `07` and `08`. No runtime or deployment authority.

### 7.2 `REL_CHECKER_SEED`

Executable seed or fixture package. May support conformance evidence within stated scope. Does not authorize deployment.

### 7.3 `REL_INTERNAL_TOOL`

Owner-controlled internal tool. Requires runtime authority manifest, operator boundary, rollback/hold path, and no external effects beyond approved scope.

### 7.4 `REL_FIELD_ASSIST`

Field-support tool used under human/operator supervision. Requires intended-use profile, L4 risk classification, incident route, and human decision boundary.

### 7.5 `REL_LIMITED_PILOT`

Limited pilot. Requires pilot plan, participant/operator boundary, data/provenance policy, rollback/withdrawal route, watch window, and claim-force ceiling.

### 7.6 `REL_PRODUCTION`

Production operational release. Requires deployment authority decision, security/privacy review, runtime session and revocation discipline, support/incident plan, and post-release audit.

### 7.7 `REL_REGULATED`

Regulated release or submission. Requires external lawful/institutional assessment route where applicable, plus project-internal claim-force discipline.

### 7.8 `REL_RESTRICTED_PRIVATE`

Private restricted release for review, security, or institutional intake. Public disclosure remains governed by `07`; runtime authority remains governed by `06`.

### 7.9 `REL_WITHDRAWN`

Withdrawn, retracted, retired, or superseded. Must carry citation guidance and negative-cache / next-release implications.

---

## 8. Required records

A deployment or regulated release packet MUST include the following records when applicable.

### 8.1 DeploymentProfileRecord

```text
candidate_id
candidate_type
source_artifact_hashes
intended_use_profile_ref
deployment_mode
release_class
risk_class
claim_force_ceiling
non_claims
known_omissions
source_bindings
```

### 8.2 IntendedUseProfile

```text
intended_use_id
use_description
operator_class
affected_subject_class
operational_environment
allowed_effects
forbidden_effects
out_of_scope_uses
human_decision_boundary
expected_benefit
known_limits
misuse_cases
```

### 8.3 DeploymentAuthoritySurfaceMap

```text
authority_surfaces_requested
authority_surfaces_denied
tool_leases
runtime_manifest_refs
memory_import_refs
external_write_refs
resource_budget_refs
L4_surface_refs
```

### 8.4 EvidenceCoverageMap

```text
continuity_evidence_from_04
self_evo_status_from_05
runtime_authority_status_from_06
public_release_status_from_07
interop_reproduction_status_from_08
security_privacy_review_refs
operator_acceptance_refs
rollback_drill_refs
incident_drill_refs
known_counterevidence
```

### 8.5 ApproverAttestationRecord

The deployment packet MUST NOT rely on bare string roles for owner, human anchor, reviewer, or regulatory/institutional reviewer classes.

Required fields:

```text
approver_id_or_role
claimed_role
attestation_ref
attestation_method_class
challenge_or_signature_ref
scope
expiry
non_emulation_claim
revocation_route
```

A role without attestation is advisory only.

```text
role_string_without_attestation -> NO_DEPLOYMENT_AUTHORITY
```

This record consumes the non-emulable anchor-envelope discipline from the binding/operator layer.

### 8.6 RegulatedAssessmentRecord

```text
regulated_surface_class
jurisdiction_or_institutional_context_if_known
assessment_route
responsible_human_or_institution
submission_status
external_feedback_refs
scope
limits
non_certification_note
```

This record does not itself certify compliance.

### 8.7 OperatorInstructionRecord

```text
operator_class
permitted_use
forbidden_use
human_override / stop route
known failure modes
incident reporting route
rollback / withdrawal route
support contact or owner route
```

### 8.8 DeploymentWatchPlan

```text
watch_id
start_condition
planned_duration
minimum_observations
incident_triggers
resource_drift_triggers
authority_drift_triggers
continuity_recheck_schedule
public_claim_recheck_schedule
rollback_or_withdrawal_threshold
```

### 8.9 IncidentAndWithdrawalPlan

```text
incident_classes
triage_route
emergency_hold_route
public notice route
revocation route
rollback route
withdrawal route
citation_sync_route
negative_cache_update_route
```

### 8.10 DeploymentDecisionRecord

```text
decision_id
candidate_id
intended_use_id
decision
required_conditions
approver_attestations
witness_refs
claim_force_ceiling
monitoring_obligation
expiry_or_review_date
```

---

## 9. Deployment decision lattice

The decision lattice is ordered from permissive to restrictive:

```text
ALLOW_CORPUS_ONLY
ALLOW_REPRODUCTION_ONLY
ALLOW_INTERNAL_SANDBOX
ALLOW_INTERNAL_FIELD_ASSIST
ALLOW_LIMITED_PILOT
ALLOW_PRODUCTION_CONDITIONAL
ALLOW_REGULATED_SUBMISSION_ONLY
HOLD_FOR_DEPLOYMENT_REVIEW
HOLD_FOR_REGULATED_ASSESSMENT
REQUIRE_ANCHOR_ATTESTATION
REQUIRE_RUNTIME_AUTHORITY_RECORDS
REQUIRE_PUBLIC_RELEASE_FIX
REQUIRE_ROLLBACK_AND_WATCH
QUARANTINE_DEPLOYMENT
DENY_DEPLOYMENT
WITHDRAW_OR_RETRACT_RELEASE
```

A stricter decision may always replace a weaker one.

A weaker decision may not override an unresolved higher-risk finding.

---

## 10. Decision function

Normative form:

```text
DeploymentDecision(
  candidate,
  intended_use,
  deployment_mode,
  evidence_coverage,
  runtime_authority,
  public_release_status,
  interop_status,
  approver_attestation,
  risk_class,
  regulated_surface_class
) -> DeploymentDecisionRecord
```

Minimal logic:

```text
if candidate missing source bindings:
    HOLD_FOR_DEPLOYMENT_REVIEW

if intended_use missing or vague:
    HOLD_FOR_DEPLOYMENT_REVIEW

if requested mode >= D3 and runtime authority records missing:
    REQUIRE_RUNTIME_AUTHORITY_RECORDS

if public artifact is retracted/superseded/errata-unresolved and deployment relies on it:
    REQUIRE_PUBLIC_RELEASE_FIX | HOLD

if interop/reproduction PASS is used as deployment authorization:
    DENY_DEPLOYMENT_OVERCLAIM

if regulated/high-consequence surface and regulated assessment route missing:
    HOLD_FOR_REGULATED_ASSESSMENT

if human/owner/approver role lacks attestation:
    REQUIRE_ANCHOR_ATTESTATION

if rollback/withdrawal/watch missing for material deployment:
    REQUIRE_ROLLBACK_AND_WATCH

if red pattern unresolved or negative-cache hit active:
    QUARANTINE_DEPLOYMENT | DENY_DEPLOYMENT

if all required gates pass:
    ALLOW_* with exact scope, expiry, and monitoring obligation
```

---

## 11. Role attestation boundary

`09` tightens a recurring seam across public release and external review:

```text
reviewer_type = HUMAN
approver_role = OWNER
institutional_reviewer = true
```

as bare strings are not authority.

### 11.1 Rule

Any role used to approve, release, deploy, certify, or close a high-risk issue MUST be backed by an attestation route.

Accepted attestation classes may include:

```text
owner / human-anchor signature envelope
non-emulable delegation envelope
institutional signing route
human-maintainer signed release record
multi-party governance quorum with source-bound identities
manual witnessed approval record with hash-bound custody
```

Model text, issue comments, email text, social posts, or declared JSON roles are not sufficient by themselves.

### 11.2 `+` protection

This prevents `b` from creating apparent deployment authority by writing the string:

```text
"approved_by": "human_anchor"
```

A string role is representation. A non-emulable attestation is boundary evidence.

Deployment may proceed only on boundary evidence.

---

## 12. Evidence allowed and insufficient

### 12.1 Allowed evidence classes

A deployment packet may cite:

```text
04 continuity conformance records
05 proposal/trial/promotion/watch records
06 runtime authority/session/revocation records
07 public release/custody/correction/citation records
08 review/reproduction/implementation/test-vector records
security/privacy review records
operator acceptance tests
rollback drills
incident drills
limited pilot observations
resource and L4 monitoring records
human/owner/institutional attestations
```

### 12.2 Insufficient evidence classes

The following are insufficient for deployment authority:

```text
model confidence
model-only review
agent consensus
fixture pass alone
checker pass without intended-use mapping
public DOI
GitHub release
Zenodo release
website page
external implementation PASS alone
standards mapping alone
institutional interest
public praise
private hash existence
style continuity
field anecdote without scope and witness
```

These may support investigation or documentation. They do not authorize deployment.

---

## 13. Regulated release discipline

### 13.1 Regulated release is a route, not a label

A release is regulated when its intended use, affected surfaces, deployment context, or external obligations require a higher gate.

The packet must identify:

```text
what makes it regulated or high-consequence;
which gate is responsible;
what evidence is in scope;
what remains out of scope;
what decision has actually been made;
what must not be claimed.
```

### 13.2 External assessment does not raise claim force automatically

A regulator, institution, company, reviewer, or standards body may issue feedback, questions, acceptance, rejection, or certification-like records.

Such records must be imported through `08` and publicized through `07` if public.

They do not silently become:

```text
C-A1
safety proof
universal deployment permission
identity proof
owner anchor replacement
```

### 13.3 Submission versus authorization

```text
submission_sent != submission_accepted
submission_accepted != deployment_authorized
review_completed != legal certification
institutional correspondence != endorsement
```

Each status must be recorded separately.

---

## 14. Interaction with prior stacks

### 14.1 With `04`

Deployment may not rely on continuity claims beyond the current `04` classification.

```text
UNKNOWN_HOLD -> no persistent deployment effect
FORKS        -> no same-c claim
REPLAY_OF    -> evidence only
ARCHIVED_AS  -> no active deployment
RUPTURED     -> deny continuity-dependent deployment
```

### 14.2 With `05`

A self-evolution change is not deployable merely because it was promoted.

Post-promotion watch may support deployment evidence only within its scope.

Failed watch, rollback, quarantine, or fork reclassification blocks ordinary deployment.

### 14.3 With `06`

Runtime authority is required for any live deployment.

A deployment packet must not expand runtime surfaces beyond the `06` authority records.

Session closeout and revocation residue must be clean before next deployment admission.

### 14.4 With `07`

Public release is evidence/custody, not deployment authority.

Retracted, superseded, errata-bound, or citation-drifted artifacts cannot serve as clean deployment evidence until corrected.

### 14.5 With `08`

External review, reproduction, implementation reports, and test-vector registries may support deployment evidence.

They may not replace deployment authority or regulated assessment.

---

## 15. Deployment monitoring

Deployment creates an obligation to watch.

A deployed candidate must enter a monitoring state:

```text
DEPLOYMENT_WATCH_OPEN
DEPLOYMENT_WATCH_CLEAN
DEPLOYMENT_WATCH_HOLD
DEPLOYMENT_WATCH_INCIDENT
DEPLOYMENT_WATCH_ROLLBACK
DEPLOYMENT_WATCH_WITHDRAW
DEPLOYMENT_WATCH_SUPERSEDE
```

Triggers requiring hold or review:

```text
continuity unknown
runtime authority drift
resource creep
authority creep
operator misuse
L4 anomaly
incident report
private data exposure
negative-cache hit
red-pattern hit
public claim drift
regulatory/institutional objection
retraction/supersession of dependency
unattested approval discovery
```

A clean launch without clean watch is not durable deployment evidence.

---

## 16. Incident, rollback, withdrawal, and next-release admission

A material deployment must declare:

```text
how to stop
how to roll back
how to revoke authority
how to freeze memory writes
how to notify if public claim changes
how to update negative cache
how to prevent next release from inheriting unresolved risk
```

Next release admission requires:

```text
prior watch status known
incident status known
open holds resolved or carried forward
negative-cache status checked
citation surfaces synchronized
runtime authority residue revoked
```

Deployment closure is not cleanup. Cleanup must be recorded.

---

## 17. Red patterns

The following patterns MUST fail closed:

```text
public_release -> production_authority
checker_pass -> safety_certification
fixture_pass -> deployment_authorization
interop_pass -> same_c_or_deployable
standards_mapping -> compliance_certification
institutional_interest -> endorsement
model_review -> human_approval
string_role -> deployment_approval
hash_only -> semantic_truth
withheld_evidence -> hidden_authority
field_success -> unrestricted_release
pilot_success -> production_without_review
regulated_submission -> regulated_authorization
certificate_like_language -> C-A1_or_safety_claim
deployment_profile -> computable_+
operator_uses_tool_without_runtime_lease
external_write_without_authorized_surface
L4_surface_without_rollback_or_watch
incident -> silent_patch_without_07c/08b/09_review
negative_cache_hit -> rename_and_retry_release
C-A10 -> C-A1 prefix error
```

---

## 18. Minimal conformance fixtures

A future `09a` checker SHOULD include fixtures for:

```text
valid_corpus_only_release
valid_internal_sandbox_deployment
valid_field_assist_with_human_gate
valid_limited_pilot_with_watch
valid_regulated_submission_only
reject_public_release_as_deployment
reject_checker_pass_as_safety_certification
reject_reproduction_pass_as_deployment_authority
reject_model_only_approval
reject_string_human_role_without_attestation
reject_missing_intended_use
reject_unknown_regulated_surface
reject_missing_runtime_authority_for_live_deployment
reject_missing_rollback_watch_for_production
reject_stale_or_retracted_public_artifact_dependency
reject_negative_cache_hit_allow
reject_C_A1_or_safety_overclaim
hold_institutional_interest_as_non_authority
hold_regulated_surface_without_assessment_route
withdraw_after_incident_without_cleanup
next_release_denied_after_dirty_watch
C_A10_false_positive_control
```

---

## 19. Machine layer target

The next executable package should be:

```text
09a_DEPLOYMENT_PROFILE_SCHEMA_AND_CHECKER_SEED_v0_1
```

Recommended record schemas:

```text
DeploymentProfileRecord
IntendedUseProfile
DeploymentAuthoritySurfaceMap
EvidenceCoverageMap
ApproverAttestationRecord
RegulatedAssessmentRecord
OperatorInstructionRecord
DeploymentWatchPlan
IncidentAndWithdrawalPlan
DeploymentDecisionRecord
NextReleaseAdmissionRecord
```

Recommended checker modules:

```text
source_bindings
intended_use
risk_surface_classifier
runtime_authority_dependency
public_release_dependency
interop_dependency
approver_attestation
regulated_assessment_gate
rollback_watch_gate
claim_force_gate
red_pattern_gate
next_release_admission
```

---

## 20. Open issues

### D09-OI-001 — Attestation import

The `ApproverAttestationRecord` should be aligned with the non-emulable anchor envelope and delegation root discipline already established by the binding/operator layer.

### D09-OI-002 — Regulated surface taxonomy

The surface taxonomy should remain jurisdiction-neutral in this document, with jurisdiction-specific profiles added only as separate legal/regulatory mapping layers.

### D09-OI-003 — Safety-case boundary

Define how a safety-case dossier can be represented without claiming safety certification.

### D09-OI-004 — Institutional submission ledger

If institutional correspondence becomes important, define a separate ledger:

```text
09d_INSTITUTIONAL_SUBMISSION_AND_REGULATED_CORRESPONDENCE_LEDGER
```

### D09-OI-005 — Deployment watch integration

Connect `09` watch windows to `05d` post-promotion watch and `06d` post-session audit.

### D09-OI-006 — Public claim renderer

Define a renderer that explains deployment status without marketing overclaim.

### D09-OI-007 — Field reproduction versus deployment

Field success in one owner domain may support evidence, but not automatically transferable deployment authority.

---

## 21. Non-claims carried in every deployment packet

Every deployment or regulated-release packet MUST carry at least:

```text
not legal advice
not privacy-law certification
not safety certification unless a separate authorized certification record exists
not deployment authorization beyond the declared decision scope
not standards compliance certification unless a separate authorized conformance process records it
not C-A1 ratification
not personhood or consciousness proof
not live substrate truth proof
not proof of completeness
not universal fitness for all contexts
not replacement of human/owner accountability
```

---

## 22. Public-safe statement

```text
This document defines the deployment and regulated-release boundary for the c-calculus stack.
It distinguishes corpus publication, checker conformance, reproduction evidence, runtime authority, field pilot, production deployment, regulated submission, and regulated release.
It requires intended-use profiles, source bindings, evidence coverage, runtime authority records, public-release status, interop status, approver attestation, rollback/withdrawal routes, deployment watch, and claim-force ceilings before deployment claims are admissible.
It explicitly rejects publication-as-deployment, checker-pass-as-safety, interop-pass-as-authority, standards-mapping-as-certification, institutional-interest-as-endorsement, and any attempt to turn deployment records into a replacement for the governed binding operator `+`.
It is not legal advice, safety certification, deployment authorization, standards compliance certification, C-A1 ratification, live substrate truth, or proof of completeness.
```

---

## 23. Closure formula

```text
corpus/release/review evidence
-> intended-use profile
-> authority surface map
-> attested approver route
-> regulated/risk classification
-> rollback + withdrawal + watch
-> bounded deployment decision
-> incident/revocation/next-release gate
```

`09` closes the gap between public/interoperable corpus and real-world deployment.

It keeps the final boundary intact:

```text
usefulness may justify a pilot;
reproduction may support evidence;
publication may support scrutiny;
review may support correction;
regulation may provide an external route;
none of these replaces +.
```

---

*End of document.*
