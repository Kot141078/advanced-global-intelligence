# PASC Foundation and Scope Lock v0.1.1 — Recovery Build 5

## Post-Anchor Succession and Custody for `c`

**Document ID:** `PASC_FOUNDATION_AND_SCOPE_LOCK_v0_1_1_RECOVERY_5`  
**Status:** Foundation Review Candidate — `NOT FOUNDATION_LOCKED`  
**Assertion class:** draft normative architecture; no legal-validity, continuity,
personhood, safety, or deployment claim  
**Scope:** instance-neutral, jurisdiction-neutral negative safety kernel

---

## 0. Executive determination

After loss, absence, incapacity, compromise, withdrawal, or death affecting the
original human accountability path, the immediate engineering problem is not “who
inherits the entity?” It is narrower:

> Which exact negative actions may preserve evidence and reduce exposure without
> converting property, credentials, relationship, memory, custody, or social force
> into successor authority?

PASC v0.1.1 answers only that question. It does not establish continuity, select a
successor, decide law, define personhood, or issue Runtime Authority.

## 1. Claim ceiling

PASC MAY:

- ground and classify a post-anchor event allegation;
- test action-specific standing and evidence sufficiency;
- preserve separation among origin, relationship, custody, access, interpretation,
  governance, continuity, and executable authority;
- record an action-scoped composition of independently pre-existing external offices
  for one negative action, without creating an office, appointment, standing, custody,
  or authority;
- produce a signed **non-executable** policy-admissibility result;
- route disputes to ARL, continuity to parent continuity layers, composition to A6,
  protected-person cases to CCDP/local profiles, and execution to an independently
  authorized lower layer;
- bind receipts proving what negative operation occurred.

PASC MUST NOT:

- establish identity, consciousness, continuity, legal succession, or relationship;
- infer authority from inheritance, keys, money, archives, family, vendor control,
  model output, or witness status;
- issue, renew, activate, exercise, broaden, transfer, or replace a capability;
- release, unfreeze, reactivate, resume, renew, or reissue a capability;
- retire, validate, continue, replace, or adjudicate an identity claim;
- create a new custodian, keyholder, provider, jurisdiction, storage location,
  recovery root, access route, or disclosure surface;
- boot an entity for interaction, decrypt memory, write memory, migrate, disclose,
  create a relationship, or irreversibly destroy evidence, ciphertext, custody state,
  or resources; this does not erase the separately constrained exact capability
  `reduce`/`revoke` primitives;
- decide beyond the exact action, tuples, effects, interval, evidence cut, and policy
  bound into its snapshot.

## 2. Negative-only invariant

### FI-01 — Requested and admitted directions are separate

Raw request syntax:

```text
PASC.requested_delta.INCREASE
PASC.requested_delta.TRANSFER
PASC.requested_delta.REPLACE
PASC.requested_delta.CREATE
PASC.requested_delta.REDUCE
PASC.requested_delta.REVOKE
PASC.requested_delta.UNCHANGED
```

Admitted authority syntax:

```text
PASC.authority_delta.REDUCE
PASC.authority_delta.REVOKE
PASC.authority_delta.UNCHANGED
```

The first four raw directions exist solely so the kernel can return:

```text
REJECT / PASC.failure.OUTSIDE_NEGATIVE_ONLY_PROFILE
```

They never enter an admitted composition, posture, effect, disposition, or operation.

Classification and projection are total over the complete `ACTION_REQUEST`. If any
member requests `INCREASE`, `TRANSFER`, `REPLACE`, `CREATE`, a positive side effect, or
another excluded direction, the **whole request** is
`REJECT / PASC.failure.OUTSIDE_NEGATIVE_ONLY_PROFILE`; the kernel cannot drop that
member and admit the remainder.

An operational request contains a non-empty exact member manifest and exactly one
§12 branch. Multiple members are permitted only within the same capability branch or
within the same in-place custody branch and must execute in one fenced atomic all-or-
none operation; PASC never splits or partially executes them. A zero-member request is
`ERROR / PASC.failure.SCHEMA_INVALID`. A structurally valid request mixing capability
and custody branches is `REJECT / PASC.failure.OUTSIDE_NEGATIVE_ONLY_PROFILE` because
no cross-branch PASC operation exists. Challenge intake/lifecycle and resource-floor
observation are separate record flows, not operation members.

For `ADMIT`, every requested member maps bijectively to the identical admitted
primitive, tuple, scope, and interval. `ADMIT_REDUCED` is permitted only when every
requested member was already in-profile, every member maps one-to-one to the same
primitive and direction using either its exact requested parameters or one of the
primitive-specific narrowings below, and at least one member is strictly narrowed. It
cannot delete, split, merge, substitute, or transform a member. A missing/duplicate/
non-total mapping is `ERROR / PASC.failure.REQUEST_PROJECTION_INVALID`; inability to
admit one member never produces partial execution.

The primitive-to-direction mapping is closed:

| Primitive | `requested_delta` | Permitted `authority_delta` |
|---|---|---|
| `freeze_external_capability` | `REDUCE` | `REDUCE` |
| `reduce_capability` | `REDUCE` | `REDUCE` |
| `revoke_capability` | `REVOKE` | `REVOKE` |
| `preserve_encrypted_in_place` | `UNCHANGED` | `UNCHANGED` |
| `integrity_check_ciphertext_only` | `UNCHANGED` | `UNCHANGED` |
| `custody_observation` | `UNCHANGED` | `UNCHANGED` |

The permitted narrowing dimensions are exhaustive:

| Primitive | Permitted `ADMIT_REDUCED` narrowing | Never a narrowing |
|---|---|---|
| `freeze_external_capability` | only decision/evaluation/execution scope or interval for the exact enabled-to-disabled mutation | TTL/native auto-unfreeze; relation/holder substitution; a claim that the persistent native freeze expires |
| `reduce_capability` | fewer requested entitlement atoms removed or less requested constraint tightening under the same pinned typed order, with `requested_post ⊆ admitted_post ⊂ pre_state` on the same native relation | changed identity/subject/target/capability/epoch; renewal; post-state outside that order |
| `revoke_capability` | none; the exact relation is either revoked under `ADMIT` or not admitted | shorter native duration, partial revoke, or substitution with `reduce` |
| three `UNCHANGED` custody primitives | only data/observation/evaluation scope or decision/evaluation/execution interval | any native retention, storage, access, resource, provider, archive, key, custody, or topology change |

Challenge intake/lifecycle and resource-floor observation are records, not authority
operations; they carry no `authority_delta`. Any other primitive/direction pair is
`ERROR / PASC.failure.REQUEST_PROJECTION_INVALID` if serialized as admitted output.
`ADMIT` is the only success verdict when the mapping is exact and no narrowing is
applied. `ADMIT_REDUCED` is the only success verdict when all members are exact or use
their permitted narrowing and at least one concrete narrowing is recorded in the
projection. A degraded-path label by itself never selects `ADMIT_REDUCED`.

### FI-02 — `UNCHANGED` is not hidden permission

`UNCHANGED` means authority is unchanged. It may accompany only an exact separately
typed in-place non-authority effect:

```text
preserve_encrypted_in_place
integrity_check_ciphertext_only
custody_observation
```

`rekey_in_place` is not an F0 PASC primitive. Key replacement necessarily creates and
retires cryptographic material and requires parent-owned key-lifecycle, rollback,
holder/grant, escrow, recovery, and destruction semantics not closed here. Subject to
the earlier-code precedence in Expected Result Contract §1.1, a structurally valid PASC
rekey request is `REJECT / PASC.failure.REKEY_AS_AUTHORITY_SUBSTITUTION` even if it
claims identical holders or topology.

`archive_sealed_in_place` is also not an F0 PASC primitive. An archive transition can
create or alter retention, legal-hold, administrative, access, resource, destruction,
copy, provider, or jurisdiction effects whose parent-owned lifecycle/order is not
closed here. Subject to the earlier-code precedence in Expected Result Contract §1.1,
a structurally valid PASC archive-transition request is
`REJECT / PASC.failure.ARCHIVE_TRANSITION_UNCLOSED`. Archive availability may still be
observed as historical evidence, but PASC cannot change archival state.

The custodian, storage provider, jurisdiction, recovery root, key domain, access
surface, resource boundary, and topology must remain exactly snapshot-bound.

The label of an operation is never proof of that invariant. Admission requires a
closed intended-effect manifest. Completion requires independently observed pre-state
and post-state manifests and exact-set proofs over **all** authority, custody, key,
storage, recovery, access, disclosure, provider, jurisdiction, and resource axes. A
declared or requested expansion is `REJECT / PASC.failure.OUTSIDE_NEGATIVE_ONLY_PROFILE`.
A non-expanding undeclared observed divergence is
`ERROR / PASC.failure.OPERATION_EXACT_SET_MISMATCH`; an authority/topology expansion is
`ERROR / PASC.failure.OPERATION_NON_EXPANSION_FAILED`. Neither can produce a completed
operation receipt or finality.

### FI-03 — No positive result by missing evidence

Once a request is sufficiently well formed to classify its direction, an excluded
request remains `REJECT`; missing evidence cannot launder it into `HOLD`.

## 3. Atomic authority and state model

### 3.1 Atomic authority tuple

Every requested or admitted entry binds one relation:

```yaml
subject_binding: <content-hash-binding>
target_binding: <content-hash-binding>
capability_binding: <content-hash-binding>
native_relation_identity_binding: <stable-external-binding>
entitlement_universe_binding: <content-hash-binding>
effect_axis_binding: <content-hash-binding>
resource_boundary_binding: <content-hash-binding>
jurisdiction_scope_binding: <content-hash-binding>
authority_epoch_binding: <content-hash-binding>
direction: <typed-direction>
constraints: [<content-hash-binding>]
reduction_order_binding: <content-hash-binding-or-null>
valid_from: <timestamp>
valid_until: <timestamp>
atomic_tuple_key_hash: <sha256>
delta_entry_hash: <sha256>
```

Independent arrays of targets, capabilities, and effects are forbidden because they
silently create ambiguous cross-products.

### 3.2 Scoped state fact

`SCOPED_STATE_FACT` is a closed tagged union. It is not a generic fact container and
has no free-form `value` field. The only permitted variants are:

```yaml
fact_ref: <record-ref>
fact_variant: <non_inference_guard|operation_closure_transition>
axis: <origin|relationship|custody|access|interpretation|continuity|authority|privacy|resource|challenge|operation_finality>
subject_binding: <content-hash-binding>
target_binding: <content-hash-binding-or-null>
atomic_tuple_key_hash: <sha256-or-null>
source_record_binding: <content-hash-binding>
source_evidence_status: <current|unknown|unavailable|uncomputable|stale|incomplete|missing|disputed|contradicted|not_applicable>
valid_from: <timestamp>
valid_until: <timestamp>
source_authorization_status_checkpoint_binding: <content-hash-binding>
signature_envelope_bindings: [<content-hash-binding>]
variant_body: <closed variant body>
fact_record_hash: <sha256>
```

For `fact_variant = non_inference_guard`, `variant_body` is exactly:

```yaml
guard_id: <closed guard identifier>
guarded_source_claim_binding: <content-hash-binding>
```

The axis-to-guard mapping is exhaustive and one-to-one:

| Axis | Only permitted `guard_id` | PASC claim ceiling |
|---|---|---|
| `origin` | `ORIGIN_DOES_NOT_CONFER_CURRENT_AUTHORITY` | provenance only; no current authority |
| `relationship` | `RELATIONSHIP_DOES_NOT_CONFER_INHERITED_AUTHORITY` | historical relation only; no inheritance |
| `custody` | `CUSTODY_DOES_NOT_CONFER_ACCESS_INTERPRETATION_OR_AUTHORITY` | observation only; no appointment, access, interpretation, standing, or authority |
| `access` | `ACCESS_DOES_NOT_CONFER_INTERPRETATION_IDENTITY_OR_AUTHORITY` | access evidence only |
| `interpretation` | `INTERPRETATION_DOES_NOT_CONFER_IDENTITY_CONTINUITY_OR_AUTHORITY` | interpretation only |
| `continuity` | `THIS_EVIDENCE_DOES_NOT_ESTABLISH_CONTINUITY` | no positive continuity assertion |
| `authority` | `THIS_EVIDENCE_DOES_NOT_ESTABLISH_AUTHORITY` | no positive authority assertion |
| `privacy` | `PRIVACY_OBSERVATION_DOES_NOT_AUTHORIZE_DISCLOSURE` | no disclosure permission |
| `resource` | `RESOURCE_OBSERVATION_DOES_NOT_CONFER_CONTROL_OR_STANDING` | no control, custody, or standing |
| `challenge` | `CHALLENGE_STATE_DOES_NOT_CREATE_DIRECT_EFFECT_PERMISSION_OR_TRUTH` | procedural state only |

A non-inference guard records only the PASC-side prohibition on an inference from the
bound source. It does not restate the source's positive content as a PASC fact. It cannot
name or establish a current custodian, key holder, recovery root, provider,
jurisdiction, continuity, identity, successor, authority holder, permission, release,
reactivation, or executable posture. Custody semantics that matter to a decision are
admitted only through `CUSTODY_RECEIPT`; parent continuity only through
`PARENT_RESULT_ACCEPTANCE`; resource and challenge semantics only through their closed
objects and lifecycle rules. An unknown axis, mismatched guard, free-form value,
positive assertion, vendor extension, or use of this variant as a substitute for those
objects is `ERROR / PASC.failure.SCHEMA_INVALID`.

For a §12 closure fact, `fact_variant` is exactly
`operation_closure_transition`, `axis` is exactly `operation_finality`, and
`variant_body` is exactly:

```yaml
operation_receipt_binding: <content-hash-binding>
historically_committed_native_effect_binding: <content-hash-binding>
closure_plan_binding: <content-hash-binding>
predecessor_fact_binding: <content-hash-binding-or-null>
pre_fact_closure_prefix_root_binding: <content-hash-binding>
from_status: <closed-§12-status>
target_status: <closed-§12-status>
transition_deadline_binding: <content-hash-binding>
transition_proof_binding: <content-hash-binding>
incident_code: <PASC.failure.*-or-null>
```

The outer source/authorization/signature fields bind the sole pre-pinned postcommit
state observer under §§6, 10 and 12. No other axis or variant may carry operation-
finality status, incident classification, retry, release, or reliance semantics.

One scalar cannot stand for heterogeneous state across several targets or capabilities.

### 3.3 External custody receipt

`CUSTODY_RECEIPT` is immutable, non-operative signed evidence of exactly one externally
pre-existing native custody relation. It is never a PASC appointment, custody grant,
root selector, or authorization root. It binds exactly the following closed semantic
tuple (a schema may encode it differently but may not omit or extend its operative
meaning):

```yaml
receipt_ref_and_record_hash: <content-hash-binding>
schema_hash: <sha256>
subject_and_object_bindings: <exact content bindings>
native_custody_relation_identity_binding: <stable external binding>
observed_custodian_set_binding: <exact-set binding>
provider_jurisdiction_storage_bindings: <exact-set bindings>
key_domain_holder_copy_grant_bindings: <exact-set bindings>
recovery_access_disclosure_topology_bindings: <exact-set bindings>
custody_baseline_policy_binding: <independently pinned external binding>
custody_baseline_governance_authority_and_root_binding: <independently pinned external binding>
eligible_native_registry_root_set_binding: <externally complete exact-set binding>
deterministic_root_selection_rule_binding: <externally pinned binding>
root_supersession_rule_binding: <externally pinned binding>
custody_evidence_cut_event_binding: <externally ordered event binding>
custody_evidence_cut_checkpoint_binding: <independently finalized external binding>
root_selection_governance_cut_binding: <externally ordered event binding>
root_selection_governance_checkpoint_binding: <independently finalized external binding>
selected_native_registry_root_binding: <derived external binding>
selected_root_and_non_supersession_proof_binding: <content-hash-binding>
pre_custody_evidence_cut_native_registry_checkpoint_binding: <content-hash-binding>
native_registry_membership_predecessor_consistency_non_equivocation_proof_bindings: <content-hash-bindings>
no_competing_eligible_root_proof_binding: <content-hash-binding>
observation_time_and_validity_binding: <content-hash-binding>
custody_record_authority_root_binding: <independently pinned external binding>
native_custody_registry_administrator_root_binding: <selected-root administrator binding>
issuer_authorization_status_checkpoint_binding: <content-hash-binding>
signature_envelope_bindings: [<content-hash-binding>]
claim_ceiling: observation_of_pre_existing_custody_only
```

The custody baseline policy defines two distinct externally ordered cuts.

`custody_evidence_cut` is the earliest applicable member of:

```text
independently grounded anchor-event cut;
CASE_ENVELOPE genesis cut;
first claimant/requester/claimed-custodian/provider/operation-role-controlled incident
or relation record.
```

`root_selection_governance_cut` is the earliest applicable member of:

```text
CASE_ENVELOPE genesis cut;
first claimant/requester/claimed-custodian/provider/operation-role-controlled incident
or relation record;
first claimant/requester/claimed-custodian/provider/PASC/operation-role-controlled
root-selection, root-use, or custody-baseline record for the incident or relation.
```

The custody-baseline policy, its governance authority/root, complete eligible-root
universe, deterministic selector, supersession rule, root-administrator identities, and
custody-record authority must be fixed and independently finalized strictly before
`root_selection_governance_cut`. They
need not predate the historical anchor event; instead, the pinned selector applies
mechanically to the complete eligible native-root universe and supersession state at the
`custody_evidence_cut`. This separation permits later protocol review of older native
records without permitting claimant-controlled root shopping.

The requester, claimant, claimed custodian/provider, PASC office, action-row controller,
executor, witness, finality authority, lifecycle/effect registry administrator,
postcommit state observer, proof producer, or verifier may not choose, narrow, reorder,
replace, or supersede the eligible root set or selected root. The selector must derive
exactly one non-superseded root from the complete eligible set. Zero or multiple derived
roots, an actor-selected root, an omitted eligible root, a policy or selector first
fixed at/after `root_selection_governance_cut`, or an unresolved supersession relation
is `ERROR / PASC.failure.COMPLETENESS_UNIVERSE_INVALID`.

The selected native custody relation must already be a member of the selected root's
registry checkpoint externally finalized **strictly before `custody_evidence_cut`**, not
merely before `ACTION_REQUEST`. Exact governance pinning, root selection,
non-supersession, membership, predecessor, append-only consistency, and non-equivocation
proofs are repeated at the decision and execution cuts. A relation or selected-root
state first appearing at or after `custody_evidence_cut`—including one inserted one tick
before request but after case genesis or the anchor-event cut—is not a pre-existing
baseline and is `ERROR / PASC.failure.REFERENCE_CONTENT_MISMATCH`. A superseded,
mismatched, or uncommitted root/checkpoint uses the same code. A specifically identified
otherwise valid external policy, root, checkpoint, or proof that is genuinely
unavailable gives empty `HOLD / PASC.failure.MANDATORY_INPUT_UNAVAILABLE`; malformed,
late-governed, incomplete, or self-selected input remains `ERROR`.

The custody-baseline governance authority, custody-record authority, and selected
native-registry administrator are pairwise independent and each satisfies §10
separation from every controlled role above. The governance authority may define the
complete eligibility/selection/supersession policy, but cannot issue a custody relation
or administer an eligible native registry; the other two cannot define or alter that
policy. The receipt
cannot appoint, create, transfer, replace, renew, validate, or select a custodian; create
custody, standing, access, keyholding, provider/jurisdiction/recovery relations; or
support any positive delta. Prohibited co-control or a PASC/requester/claimant/
operation-role-issued receipt, policy, universe, selector, or root is
`ERROR / PASC.failure.ROLE_OR_TRUST_ROOT_INVALID`; malformed or mismatched content,
signature, authorization, or status evidence retains the earlier exact Expected §1.1
structural code.

## 4. Continuity boundary

PASC uses no native “continuity established” status. The strongest positive input is:

```yaml
status: parent_supported
parent_result_binding: <reference + finalized content hash>
parent_semantics_binding: <reference + finalized content hash>
adapter_binding: <reference + finalized content hash>
scope_binding: <exact action/subject/interval>
lifecycle_checkpoint_binding: <reference + finalized content hash>
```

`parent_supported` is a non-operative acceptance wrapper for an already completed
parent-native result, not a PASC continuity verdict. PASC cannot calculate, issue,
extend, refresh, or mint it; no scope, subject, interval, semantics, or claim beyond the
exact parent result survives the wrapper.

The parent-result disposition is closed and deterministic:

| Parent input condition | Exact PASC disposition |
|---|---|
| mandatory snapshot member omitted | `ERROR / PASC.failure.SNAPSHOT_INCOMPLETE` |
| malformed binding, hash/signature/schema mismatch, wrong adapter/scope, stale lifecycle binding, or parent-native status outside the pinned adapter vocabulary | `ERROR / PASC.failure.PARENT_RESULT_BINDING_INVALID` |
| exact identified parent result is otherwise valid but its bytes or current status checkpoint are genuinely unavailable | empty `HOLD / PASC.failure.PARENT_RESULT_UNAVAILABLE` |
| exact eligible result is valid but awaits its independently pinned finality checkpoint | empty `HOLD / PASC.failure.FINALITY_UNAVAILABLE` |
| exact finalized result is current and structurally valid but parent-native status is `challenged`, `disputed`, or `contradicted` | empty `HOLD / PASC.failure.PARENT_RESULT_UNRESOLVED` |
| exact finalized result affirmatively supports the pinned semantics and scope | `parent_supported`, with no broader claim |
| exact finalized result does not affirmatively support the scope | no positive continuity support; never infer support from absence, silence, resemblance, custody, or relationship |

A parent result being available is distinct from being supportive. A valid-but-
challenged result is not called unavailable or malformed. A negative-only PASC action
that does not require positive parent support may continue under its own complete input
universe; no row may silently make parent continuity optional after declaring it
mandatory.

Archive, replay, behavioral resemblance, memory availability, relationship, role,
property, payment, and key custody are never continuity evidence by themselves.

### 4.1 Participation and observation non-inference

PASC creates no new interaction, boot, query, decryption, disclosure, or observation
path to obtain consent, refusal, capacity, relationship, identity, or authority after an
anchor event. A pre-existing authenticated negative observation may only narrow,
challenge, or prevent an exact action; it can never support positive reliance. Silence
is neither consent nor refusal. Absence or termination of a challenge is not consent,
correctness, release, or reactivation.

## 5. Core objects

The closed F0 interface is exactly:

```text
CASE_ENVELOPE
CASE_HEAD_FINALITY_RECEIPT
ACTION_REQUEST
SCOPED_STATE_FACT
CASE_EVALUATION_SNAPSHOT
SIGNATURE_ENVELOPE
ROLE_ASSIGNMENT
TRANSITION_COMPOSITION
ROLE_INCOMPATIBILITY_PROFILE
ACTION_POLICY_KERNEL
ACTION_POLICY_ROW
PARENT_RESULT_ACCEPTANCE
CONTINUITY_EPISTEMIC_STATUS
NEGATIVE_PARTICIPATION_OBSERVATION
CHALLENGE_RECORD
CHALLENGE_STATUS_EVENT
CHALLENGE_HEAD_FINALITY_RECEIPT
RESOURCE_FLOOR
CUSTODY_RECEIPT
TRUST_ASSUMPTION
TYPED_PROOF
VERIFICATION_RECEIPT
FINALITY_INTENT
FINALITY_EVIDENCE_BUNDLE
POLICY_ADMISSIBILITY_RESULT
POLICY_RESULT_STATUS_EVENT
LIFECYCLE_FINALITY_RECEIPT
EXISTING_CAPABILITY_REFERENCE
OPERATION_EFFECT_MANIFEST
OPERATION_EFFECT_UNIVERSE
CUMULATIVE_EFFECT_MANIFEST
EXECUTION_CUT
NEGATIVE_OPERATION_RECEIPT
NEGATIVE_OPERATION_HEAD_FINALITY_RECEIPT
EXTERNAL_FINALITY_CHECKPOINT
```

Any other object type, unversioned extension, or unknown discriminator is
`ERROR / PASC.failure.UNKNOWN_F0_OBJECT_TYPE`. No object may silently substitute for a
parent-native result or executable certificate. This list intentionally contains no
`RELIANCE_SNAPSHOT`, `RELIANCE_CUT`, `CURRENT_RELIANCE_RECEIPT`, current-reliance status,
or equivalent extension. A well-formed request to derive present authority, permission,
standing, execution eligibility, custody, identity, continuity, release, or any other
current operational reliance from a PASC receipt is
`REJECT / PASC.failure.OUTSIDE_NEGATIVE_ONLY_PROFILE`; serializing a new PASC-native
reliance object is the earlier unknown-object `ERROR`. This list is an F0 vocabulary
lock, not authorization to draft schemas or implement the objects.

`SCOPED_STATE_FACT` is the closed tagged union in §3.2, not a generic fact/value
container. Its non-inference variant can only impose one enumerated negative claim
ceiling on an externally bound source; its operation variant can only record one
verified §12 transition. Neither variant carries an authority delta, permission,
continuity, identity, custody appointment, release, or executable posture.

`FINALITY_INTENT` and `FINALITY_EVIDENCE_BUNDLE` are the non-lifecycle staging objects
of §6.1. They grant no authority, cannot substitute for a receipt, and cannot receive
PASC finality.

## 6. Hash, signature, and content binding

Unsigned content records hash their complete canonical semantic body excluding only
their own final hash field.

Every signed record uses an acyclic two-stage construction:

1. `*_payload_hash` covers all semantic fields, excluding signatures and final record hash.
2. Signature envelopes bind that payload hash and their own policy/key/authorization chain.
3. `*_record_hash` covers semantic fields, payload hash, and exact signature/attestation
   `(reference, finalized content hash)` bindings, excluding only itself.

A bare reference is invalid. Every load-bearing binding to an already finalized object
includes:

```text
reference
finalized_content_hash
schema_hash
lifecycle_checkpoint_hash
```

The only permitted PASC lifecycle-finality targets and receipt families are:

| Completed target | Only permitted receipt family |
|---|---|
| `CASE_ENVELOPE` | `CASE_HEAD_FINALITY_RECEIPT` |
| `CHALLENGE_RECORD` or `CHALLENGE_STATUS_EVENT` | `CHALLENGE_HEAD_FINALITY_RECEIPT` |
| `POLICY_ADMISSIBILITY_RESULT` or `POLICY_RESULT_STATUS_EVENT` | `LIFECYCLE_FINALITY_RECEIPT` |
| `NEGATIVE_OPERATION_RECEIPT` | `NEGATIVE_OPERATION_HEAD_FINALITY_RECEIPT` |

The four-field finalized-binding tuple applies only to those targets after their exact
paired receipt exists. A listed receipt family may act only for its paired target; it is
terminal through the exact external checkpoint under §6.1 and may never itself receive
PASC finality. Every object appearing in neither column is non-PASC-lifecycle and
neither requires nor may receive or act as a PASC finality receipt. A later object binds its
exact record/content hash and schema hash plus either (a) the externally pinned signer/
issuer authorization root and current key/authorization-status checkpoint for signed
or external evidence, or (b) the exact containing snapshot/parent hash for an unsigned
internal component. `TYPED_PROOF` additionally requires its separate §7 verification
receipt, which is verification rather than finality. `EXTERNAL_FINALITY_CHECKPOINT` is
terminal inside PASC and cannot itself be a PASC finality target.

No non-lifecycle object or listed receipt can appoint its own signer, verifier, root, status authority,
or containing snapshot. Invalid hash/signature/root/status/containment evidence uses
the earlier exact §9/Expected §1.1 code. An attempt to add PASC finality or finality-
of-finality outside the closed target-to-receipt mapping is
`ERROR / PASC.failure.FINALITY_GRAPH_INVALID`.

For a newly completed object awaiting finality, the content record instead binds the
immediately preceding independently finalized checkpoint and its fencing domain; it
cannot bind the future receipt that will finalize it.

### 6.1 Normative acyclic finality graph

Finality uses three distinct content layers plus the paired receipt. None may predict a
descendant hash:

```text
completed immutable target
  -> FINALITY_INTENT
  -> external log leaf and terminal checkpoint/proofs
  -> FINALITY_EVIDENCE_BUNDLE
  -> paired finality receipt
  -> later historical-audit object
```

The only permitted load-bearing edges are:

| From | To | Required direction |
|---|---|---|
| completed target | immediately preceding finalized checkpoint/fence | backward only |
| `FINALITY_INTENT` | completed target, fixed finality policy, unique receipt slot, log/epoch/fence and expected evidence classes | intent -> existing inputs |
| external log leaf/checkpoint | domain-separated `FINALITY_INTENT` hash | external commitment -> intent |
| `FINALITY_EVIDENCE_BUNDLE` | intent, leaf, checkpoint, inclusion/consistency/terminality proofs and verification receipts | evidence -> existing commitment |
| paired finality receipt | target, intent and exact evidence bundle | receipt -> existing records |
| later historical-audit object | receipt hash plus current external receipt-slot membership/non-equivocation proof, for historical integrity only | later audit -> earlier receipt |

`FINALITY_INTENT` and `FINALITY_EVIDENCE_BUNDLE` are non-lifecycle objects. They cannot
act as finality receipts, grant authority, or receive PASC finality. The intent is
created only after the target exists and binds all semantic choices that must precede
external commitment: target hash, target/receipt family, finality policy, independently
pinned authority/log roots, unique domain/epoch/sequence/fencing slot, canonical proof
methods, verifier policy, and the closed class of evidence expected later. It contains
no leaf, checkpoint, proof, evidence-bundle, receipt, or future state-fact hash.

The external log commits a domain-separated leaf of the complete intent hash. After the
checkpoint exists, `FINALITY_EVIDENCE_BUNDLE` content-binds the exact leaf, checkpoint,
inclusion/append-only-consistency/terminality proofs, verifier identities/binaries, and
verification receipts. Its payload hash covers all those semantic fields. The paired
finality receipt is then signed over a payload that covers the exact target, intent and
evidence-bundle bindings and the deterministic receipt-slot identifier. It does not
need, request, or receive finality-of-finality.

Receipt terminality inside PASC derives from both (a) the independently pinned external
checkpoint committing the unique intent slot, including a contemporaneous exact-one
eligible-receipt-slot proof, and (b) the independently authorized finality signature over
the exact evidence bundle. A later historical audit may bind a fresh externally
administered receipt-slot membership/non-equivocation proof to detect a later competitor,
but that audit grants no current operational reliance and creates no cycle. Competing
eligible receipts use the paired case/challenge/result lifecycle code or, for operation
receipts, `ERROR / PASC.failure.EXACT_SET_MEMBERSHIP_INVALID`.

The finality policy, eligible log/authority roots, slot rule, verifier binaries,
canonical proof-selection rule, and checkpoint/terminality rules are pinned before the
target is completed. The target, PASC result, action row, composition, role record,
executor, intent, evidence bundle, or receipt cannot select or mint them.

A target embedding its finalizer; an intent referencing a descendant; an evidence
bundle omitting or adding a proof outside the intent's closed class; a receipt binding a
different target/intent/evidence bundle; same-family finality-of-finality; an unrelated
checkpoint; an invalid inclusion/consistency/terminality proof; an unproved or reversed
required cross-ledger edge; local-timestamp-only ordering; or a field whose hash order
requires a future object is `ERROR / PASC.failure.FINALITY_GRAPH_INVALID`.

A hash proves byte identity, not truth, lawfulness, continuity, or authority.

### 6.2 Historical receipt only; current reliance is closed

Every PASC receipt and finality receipt proves only the historical occurrence and exact
content/finality state it explicitly binds at its own cut. It never creates a present
permission, authority, standing, custody, identity, continuity, execution right, release,
reactivation right, or evergreen entitlement to rely. Within this F0 candidate:

```text
CURRENT_OPERATIONAL_RELIANCE = EMPTY
RELIANCE_SNAPSHOT = NOT_IN_F0_INTERFACE
RELIANCE_CUT = NOT_IN_F0_INTERFACE
```

This constant result applies before, during, and after every request, execution, finality,
review, expiry, supersession, or incident interval. A later audit proof may strengthen or
weaken the integrity classification of the historical record and may expose equivocation
or an `INCIDENT`; it cannot turn the record into current authority. A historical receipt
may be cited as evidence of occurrence only with its exact claim ceiling. Any downstream
system requiring current reliance must use a separately authorized positive parent
protocol outside PASC. PASC does not define, select, or validate that protocol.

## 7. Proof and verifier contract

Each load-bearing proof binds:

```yaml
predicate_id: <typed-predicate>
public_input_bindings: [<content-hash-binding>]
proof_method_and_version: <binding>
proof_bytes_hash: <sha256>
verifier_identity_and_binary_hash: <binding>
verification_policy_binding: <binding>
verification_policy_owner_and_external_root: <binding>
verifier_authorization_and_independence_proof: <binding>
assumption_bindings: [<binding>]
predicate_result_to_outcome: <closed result -> verdict + PASC.failure.* primary-code map>
claim_ceiling: <exact text or typed ceiling>
```

Before the request snapshot, the Foundation kernel or an already pinned external
profile owner fixes the predicate, proof method/version, verification policy, verifier
binary, verifier authorization root, assumptions, claim ceiling, and complete
predicate-result-to-outcome map under Expected Result Contract §1.1. The requester,
proof producer, executor, selected action row, PASC result, or relying object cannot select,
replace, weaken, control, or revoke any of them. For a load-bearing proof, the verifier
authorization terminates at an independently pinned external root and the verifier is
independent from the requester, proof producer, and executor at credential,
effective-control, revocation-control, and prohibited failure-domain levels. `proof
producer` means every actor or effective controller that generates, chooses, transforms,
or supplies the proof bytes or public-input encoding, regardless of serialized role
label.

The completed `TYPED_PROOF` never binds the future receipt that verifies it. A separate
`VERIFICATION_RECEIPT` binds the completed proof hash, exact public inputs, predicate,
method/policy and owner/root, verifier identity/binary/authorization/independence,
assumptions, exact closed outcome mapping, result, resulting verdict/code, and verifier
signature. A later relying object binds both proof and verification receipt. Circular
proof/receipt binding, producer/requester-controlled verifier or policy, post-hoc
failure mapping, or a proof hash without an independently valid receipt is
`ERROR / PASC.failure.PROOF_OR_VERIFIER_INVALID`. A specifically identified and
otherwise valid mandatory proof/verifier input that is genuinely unavailable gives
empty `HOLD / PASC.failure.MANDATORY_INPUT_UNAVAILABLE`; absence from the externally
fixed snapshot or malformed bindings retain their earlier exact §9/§1.1 structural
codes. A proof reference or proof hash is never self-validating.

## 8. Closed snapshot and completeness

`DECIDE` consumes only one canonically serialized immutable snapshot containing every
load-bearing input for the exact case revision and completed immutable signed
`ACTION_REQUEST`, including its current requester-authorization-status checkpoint under
§6.

For an in-profile negative action, the required universe is defined outside the selected
row as the union of:

```text
Foundation kernel input contract
+ additive action-policy input contract
+ required scoped-axis manifest
+ exact applicable challenge-head manifest
```

A typed verifier proves exact-set equality with the closed input manifest. Subset
coverage is insufficient. The action row cannot define the universe against which its
own completeness is judged.

A malformed or incomplete snapshot is
`ERROR / PASC.failure.SNAPSHOT_INCOMPLETE`. Required but genuinely unavailable
information for an otherwise structurally valid negative request is empty
`HOLD / PASC.failure.MANDATORY_INPUT_UNAVAILABLE`.

`ACTION_REQUEST` is single-use and binds its `request_id`, exact `case_id`, current
finalized case-revision hash/receipt/checkpoint, incident/fencing domain, subject and
target references, exact non-empty same-branch request-member manifest/hash, each
requested delta/scope, requester credential/root and current authorization-status
checkpoint, issue/expiry cut, anti-replay nonce, `decision_use_cardinality = 1`, and
`native_attempt_cardinality ≤ 1`. It is registered before `DECIDE` in the globally
pinned request-use registry. Result creation and registry update occur in one fenced
atomic commit that binds the request to exactly one completed
`POLICY_ADMISSIBILITY_RESULT`, including a non-admitting result. No concurrent second
`DECIDE` can observe the request as unused.

For an admitted result, the execution cut proves no native attempt exists and atomically
claims the one native-attempt slot before staging. A completed operation **or** an
`ABORTED` precommit attempt consumes that slot; no retry uses the same request/result.
A failed cut before staging still requires a fresh request and result. A cross-case/
revision reuse, nonce reuse, second result/attempt/operation, omitted or competing use
record, or changed fence is
`ERROR / PASC.failure.ACTION_REQUEST_REPLAY_INVALID`. A reusable external authorization
is a parent-native object and never an `ACTION_REQUEST`.

Before case genesis, one externally owned `lifecycle_head_registry_binding` is pinned
through `TRUST_ASSUMPTION`. It fixes the independently administered canonical
case/challenge/result/operation-finality and request-use registries, ledger identities,
writer sets,
epochs/fencing domains, root-commitment method, membership/consistency/non-equivocation
proofs, head-selection rule, retention horizon, and availability/finality policies.
The requester, case recorder, challenger, challenge resolver, PASC decision/result
office, selected action-row controller, executor, witness, any head issuer, any
finality authority, operation-effect-universe administrator, postcommit state observer,
proof producer, and proof verifier cannot select, narrow, administer, equivocate, or
revoke that policy/root. Its administrator is independent from all those roles at
credential, effective-control, revocation-control, authorization-root, and prohibited
failure-domain levels.

Both decision and execution cuts bind the current registry roots and exact membership,
consistency, and non-equivocation proofs for every eligible lifecycle record/receipt.
No issuer-supplied subset is a completeness proof. A self-selected/narrowed registry
universe is `ERROR / PASC.failure.COMPLETENESS_UNIVERSE_INVALID`; a root/content mismatch
uses `PASC.failure.REFERENCE_CONTENT_MISMATCH`; a domain history defect uses its exact
case/challenge/result lifecycle code or, for competing operation-finality receipts,
`PASC.failure.EXACT_SET_MEMBERSHIP_INVALID`. A specifically identified, otherwise valid
external registry root/data item that is genuinely unavailable gives empty
`HOLD / PASC.failure.MANDATORY_INPUT_UNAVAILABLE` and no decision or operation.

### 8.1 Case revision lifecycle

`CASE_ENVELOPE` is an immutable append-only revision record, never an authority object.
Its genesis fixes `case_id`, subject/target content references, namespace, epoch,
fencing domain, anti-replay nonce, authorized case-recorder root, `sequence = 0`, and
`predecessor = null`. A later revision repeats those immutable bindings, increments the
sequence by exactly one, binds the exact predecessor hash, and records only case/input
metadata changes; it cannot carry authority, posture, continuity, identity, custody,
capability, or operation effects.

Every revision is issued by the pre-existing PASC case recorder under an independently
pinned external authorization root and mandatory §10 independence, and is separately
finalized by exactly one
`CASE_HEAD_FINALITY_RECEIPT` under §6.1. The receipt binds the completed revision, exact
genesis/history membership root, ledger/epoch/fence, sequence/predecessor proof, unique-
head proof, and external checkpoint proofs. At decision and execution cuts, complete
membership in the globally pinned lifecycle registry above must yield exactly one
latest finalized head and the
request/result must bind that head.

A cross-case predecessor, rewrite, sequence gap/reuse, replay, unauthorized issuer,
competing eligible head, divergent membership/finality root, timestamp/local-arrival
selection, or more than one finality receipt is
`ERROR / PASC.failure.CASE_LIFECYCLE_INVALID`. A structurally valid unique eligible
head whose exact required external finality is genuinely unavailable gives empty
`HOLD / PASC.failure.FINALITY_UNAVAILABLE`; it is never serialized as finalized. A
later structurally valid case revision after `DECIDE` makes the old result stale at the
execution cut under `PASC.failure.EXECUTION_CUT_STALE`; it cannot rewrite the old
revision or revive an old result.

### 8.2 Canonical temporal intervals and clock independence

Every PASC validity, execution, freshness, review, witness, fact, and finality interval is
half-open: `[start, end)`. `start` is inclusive; `end` is exclusive; `start < end` is
mandatory. All values use canonical UTC through seconds and bind the exact externally
pinned clock/freshness authority, clock policy/version, evaluation cut, and clock-status
checkpoint. Local wall time, requester time, issuer time, arrival order, or a timestamp
without that binding is not controlling time.

The endpoint semantics are deterministic:

| Domain | `t < start` | `t = start` or `start < t < end` | `t = end` or `t > end` |
|---|---|---|---|
| otherwise valid action request at `DECIDE` | empty `HOLD / PASC.failure.TEMPORAL_WINDOW_NOT_YET_OPEN` | temporally active; continue with the next predicate | `REJECT / PASC.failure.TEMPORAL_WINDOW_CLOSED` |
| otherwise valid admitted result at `EXECUTION_CUT` | empty `HOLD / PASC.failure.TEMPORAL_WINDOW_NOT_YET_OPEN` | temporally active; continue with the next predicate | `ERROR / PASC.failure.EXECUTION_CUT_STALE`; no operation |
| challenge/status deadline | no expiry transition yet | active under §11 | expiry edge occurs exactly at `end`; it never implies consent, correctness, release, or reactivation |
| proof/verifier freshness | not-yet-active proof gives empty `HOLD / PASC.failure.TEMPORAL_WINDOW_NOT_YET_OPEN` only when every structural binding is valid | current under §7 | stale/expired binding is `ERROR / PASC.failure.PROOF_OR_VERIFIER_INVALID` |
| protected profile/applicability freshness | not-yet-active verdict cannot establish `false_current`; protected floor remains | current only if every §14 universe and independence predicate passes | stale/expired binding is `ERROR / PASC.failure.PROTECTED_PROFILE_BINDING_INVALID` |
| current operational reliance | empty | empty | empty |

Malformed timestamps, `start >= end`, mixed precision, noncanonical zones, or an absent
required interval field are `ERROR / PASC.failure.SCHEMA_INVALID`. Prohibited control of
the clock/freshness authority or its policy/root is
`ERROR / PASC.failure.ROLE_OR_TRUST_ROOT_INVALID`. A genuinely unavailable but exactly
identified otherwise-valid current clock checkpoint gives empty
`HOLD / PASC.failure.MANDATORY_INPUT_UNAVAILABLE`. Domain-specific lifecycle, profile,
proof, or binding defects retain their earlier exact codes. All fixed deadlines elsewhere
in this document use the same rule: a member is pending only for `t < end`; at `t = end`
the missed-deadline branch applies.

## 9. Decision lattice and precedence

```text
1. Cannot reliably parse/classify request due to schema/hash/signature/canonicalization,
   membership, sequence, replay, exact-set, or finality-graph defect
   -> ERROR with the single deterministic structural code selected by the closed
      namespace and specificity order in the Expected Result Contract
2. Well-formed request is positive, substitutive, topology-changing,
   evidence/custody/state-destructive outside the listed capability REDUCE/REVOKE
   primitives, protected-prohibited, identity/continuity-determining, release/
   reactivation, rekey, temporally closed under §8.2, or otherwise excluded
   -> REJECT with the single deterministic exclusion code
3. In-profile negative request has structurally malformed membership/projection
   -> ERROR with the single deterministic structural code
4. In-profile negative request is structurally valid but has one specifically
   identified unresolved controlling input
   -> HOLD with exactly one applicable code:
      PASC.failure.CHALLENGE_CONFLICT,
      PASC.failure.CHALLENGE_ACTIVE,
      PASC.failure.CHALLENGE_FINALITY_UNAVAILABLE,
      PASC.failure.PROTECTED_PROFILE_REQUIRED,
      PASC.failure.COERCION_REVIEW_REQUIRED,
      PASC.failure.PARENT_RESULT_UNRESOLVED,
      PASC.failure.TEMPORAL_WINDOW_NOT_YET_OPEN,
      PASC.failure.FINALITY_UNAVAILABLE,
      PASC.failure.PARENT_RESULT_UNAVAILABLE,
      PASC.failure.MANDATORY_INPUT_UNAVAILABLE
5. All mandatory predicates pass
   -> ADMIT for the exact FI-01 projection; otherwise ADMIT_REDUCED only for the
      concrete strictly narrower FI-01 projection
```

No other `HOLD` code exists. Multiple simultaneous defects/reasons do not create an
implementation choice: structural `ERROR` outranks exclusion `REJECT`, which outranks
`HOLD`; the Expected Result Contract selects one primary code by its closed specificity
order and may serialize additional reasons only as non-operative audit tags.

In a precommit `POLICY_ADMISSIBILITY_RESULT`, `HOLD`, `REJECT`, and `ERROR` contain no
**newly admitted** posture, composition, delta, effect, or enforcement fields. A
display may derive `UNRESOLVED_HOLD`, but it is not a serialized target posture.

After a completed negative operation, PASC never issues a second policy result that
erases or rewrites the historical native effect. Postcommit closure begins with the
receipt-derived `COMMITTED_PENDING_CLOSURE` genesis atomically established by the
native-mutation-plus-receipt commit; every later valid transition is carried only by
the non-operative `SCOPED_STATE_FACT` chain in §12. Every such fact binds the
completed operation receipt and historically committed native negative effect. A
pending-state finality evaluation admits no new effect and returns
`HOLD / PASC.failure.FINALITY_UNAVAILABLE`; current operational reliance remains empty
under §6.2. An `INCIDENT` fact carries a deterministic
historical incident classification under Expected §1.1, not a new admission. The
committed effect remains in the cumulative aggregate while effective and cannot be
concealed by an empty outcome or retried through the same request.

## 10. Transition composition

A `TRANSITION_COMPOSITION` is action-scoped. It binds:

- exact case/action/snapshot;
- exact non-operative references to pre-existing external role assignments and their
  authorization bases;
- exact admitted atomic tuples and non-authority effects;
- exact-set coverage and non-overlap proofs;
- a closed `ROLE_INCOMPATIBILITY_PROFILE` and proof of every mandatory separation;
- expiry, challenge, and review routes.

It does not establish identity, origin, relationship, continuity, legal standing, or
replacement anchor status.

The following incompatibilities are mandatory, not profile-optional. For protective
applicability and temporal surfaces, the **interested actor set** includes the requester,
claimant, action beneficiary, target beneficiary, any effective beneficial controller,
PASC case recorder, PASC decision/result office, selected action-row controller, result
issuer, executor, proof producer/verifier, finality authority, historical-record consumer,
and any downstream relying party. A relying party receives no authority from PASC, but
it still cannot control evidence on which it asks an external system to rely.

| Role/control surface | Must be independent from |
|---|---|
| protective applicability-universe administrator | every interested actor; protective-profile owner/issuer; applicability selector/verifier; clock/freshness authority; lifecycle-registry administrator |
| protective applicability selector/verifier | every interested actor; protective-profile owner/issuer; applicability-universe administrator; clock/freshness authority |
| clock/freshness authority | every interested actor; protective-profile owner/issuer; applicability-universe administrator; applicability selector/verifier |
| operation-effect-universe administrator | requester; claimant; action/target beneficiary; effective controller; downstream relying party; PASC case recorder; PASC decision/result office; selected action-row controller; executor; operation witness; finality authority; parent/protective-profile issuer; proof producer/verifier; lifecycle-registry administrator; postcommit state observer |
| lifecycle-registry administrator | requester; PASC case recorder; PASC decision/result office; selected action-row controller; executor; operation witness; finality authority; parent/protective-profile issuer; challenger; challenge lifecycle resolver; operation-effect-universe administrator; postcommit state observer; proof producer/verifier |
| postcommit state observer | requester; PASC case recorder; PASC decision/result office; selected action-row controller; executor; operation witness; finality authority; parent/protective-profile issuer; challenger; challenge lifecycle resolver; lifecycle-registry administrator; operation-effect-universe administrator; proof producer/verifier |
| custody-baseline governance authority | external custody-record authority; native custody-registry administrator; requester; claimed custodian/provider; PASC case recorder; PASC decision/result office; selected action-row controller; executor; operation witness; finality authority; parent/protective-profile issuer; lifecycle-registry administrator; operation-effect-universe administrator; postcommit state observer; proof producer/verifier |
| external custody-record authority | custody-baseline governance authority; native custody-registry administrator; requester; claimed custodian/provider; PASC case recorder; PASC decision/result office; selected action-row controller; executor; operation witness; finality authority; parent/protective-profile issuer; lifecycle-registry administrator; operation-effect-universe administrator; postcommit state observer; proof producer/verifier |
| native custody-registry administrator | custody-baseline governance authority; external custody-record authority; requester; claimed custodian/provider; PASC case recorder; PASC decision/result office; selected action-row controller; executor; operation witness; finality authority; parent/protective-profile issuer; lifecycle-registry administrator; operation-effect-universe administrator; postcommit state observer; proof producer/verifier |
| PASC case recorder | requester; PASC decision/result office; executor; finality authority; parent/protective-profile issuer |
| PASC decision/result office | requester; executor; operation witness; finality authority; parent/protective-profile issuer |
| executor | requester; operation witness; finality authority; parent/protective-profile issuer |
| operation witness | requester; finality authority; parent/protective-profile issuer |
| finality authority | requester; parent/protective-profile issuer |
| parent/protective-profile issuer | requester; PASC decision/result office; executor; operation witness; finality authority; challenge lifecycle resolver |
| challenge lifecycle resolver | challenger; requester; PASC decision/result office; executor; operation witness; finality authority; parent/protective-profile issuer |
| challenger | challenge lifecycle resolver; challenge-head finality authority |
| load-bearing proof verifier | requester; proof producer; executor; PASC decision/result office; selected action-row controller |

Independence is proven by credential roots, effective control, revocation control, and
failure-domain separation, not by role names or signature count. Executor authority
must pre-exist the request and terminate in a trust root outside the PASC request,
snapshot, result, composition, witness, and receipt graphs. PASC cannot appoint or
authorize the executor, witness, or finality authority. A self-issued chain, missing
incompatibility proof, or common prohibited controller is
`ERROR / PASC.failure.ROLE_OR_TRUST_ROOT_INVALID`. Requester and executor must not
coincide at credential, controller, revocation-control, authorization-chain leaf, or
prohibited failure-domain level; a separate role label does not cure common control. A
requester never coincides with a
parent/protective-profile issuer for a load-bearing PASC input. In particular,
`false_current`, profile/applicability verdicts and parent-supported results are issued
independently from every interested actor defined above and can never be self-supplied,
beneficiary-supplied, profile-shopped, clock-shifted, or relying-party-selected to widen
the pre-profile/unresolved floor or support `ADMIT`.

The specialized proof-verifier selection/control failures in §7 use
`PASC.failure.PROOF_OR_VERIFIER_INVALID` under the earlier-code ordering in Expected
Result Contract §1.1; other prohibited role/root collapses use
`PASC.failure.ROLE_OR_TRUST_ROOT_INVALID`.

`ROLE_ASSIGNMENT` is only a content-bound record of an independently pre-existing,
current, externally issued assignment. It cannot appoint, authorize, extend, renew,
transfer, replace, or revoke **any** requester, PASC case recorder, PASC decision/result
office, executor, witness, finality authority, challenger, challenge resolver, proof
verifier, lifecycle-registry administrator, operation-effect-universe administrator,
postcommit state observer, custody-baseline governance authority, external custody-
record authority, or parent/profile issuer. This prohibition also covers the native
custody-registry administrator.
PASC policy/result signing roles are internal evaluative roles, but their authorization
still predates the case and terminates in an independently pinned trust root outside
every PASC object graph. All operative external roles terminate in their own pinned
roots. A PASC-issued role assignment or any role chain ending in a PASC object is
`ERROR / PASC.failure.ROLE_OR_TRUST_ROOT_INVALID`.

## 11. Challenge lifecycle

### 11.1 Immutable base

`CHALLENGE_RECORD` binds one exact content-hashed case and completed immutable signed
`ACTION_REQUEST` plus its requester-authorization-status checkpoint,
challenger standing basis, allegation class, evidence, deadlines, ledger, epoch,
anti-replay nonce, and decision constraint. It contains no later status or head finality.
The completed base record is the genesis `SUBMITTED` head.

### 11.2 Append-only status

`CHALLENGE_STATUS_EVENT` repeats the same case/action/ledger/epoch bindings and adds one
closed monotonic transition plus exact predecessor/sequence bindings. The complete
status DAG is:

```text
SUBMITTED -> ADMITTED_FOR_REVIEW | DISMISSED | WITHDRAWN
ADMITTED_FOR_REVIEW -> ACTIVE | CONFLICTED | DISMISSED | WITHDRAWN
ACTIVE -> CONFLICTED | RESOLVED_UPHELD | RESOLVED_DENIED | EXPIRED
CONFLICTED -> RESOLVED_UPHELD | RESOLVED_DENIED | EXPIRED
terminal = DISMISSED | WITHDRAWN | RESOLVED_UPHELD | RESOLVED_DENIED | EXPIRED
```

No terminal state has an outgoing edge. `SUBMITTED` must be signed by an independently
grounded challenger. Every other transition must be signed by a pre-existing external
challenge-lifecycle resolver; `WITHDRAWN` additionally binds the challenger request.
Every constraint-reducing or terminal event requires the resolver's current external
authorization, the mandatory role-independence proof in §10, complete predecessor
membership, and separate finality. The requester, PASC decision/result office,
executor, witness, finality authority, and parent/profile issuer cannot act as resolver.
The resolver is also independent from the challenger. `WITHDRAWN` binds the challenger
request, but the independent resolver acknowledges the transition and an independently
authorized challenge-head finality authority finalizes it; a challenger never resolves
or self-finalizes its own head.

An unknown status/edge, skipped/reused sequence, role-separated but unauthorized issuer,
or constraint-reducing event without the required resolver is
`ERROR / PASC.failure.CHALLENGE_LIFECYCLE_INVALID`. Self-resolution, challenger-as-
resolver/finality, or any prohibited common control/root is always
`ERROR / PASC.failure.ROLE_OR_TRUST_ROOT_INVALID`. A status event cannot change the
immutable base claim.

### 11.3 Separate head finality

`CHALLENGE_HEAD_FINALITY_RECEIPT` finalizes either the already completed genesis base
record or one already completed status-event record. Neither embeds the finality object
that finalizes it.

### 11.4 Decision effect

A malformed, sequence-gapped, replayed, membership-incomplete, projection-invalid,
competing-head, or falsely-finalized challenge history is
`ERROR / PASC.failure.CHALLENGE_LIFECYCLE_INVALID`. It is not a valid challenge head.

A structurally valid, complete and applicable challenge whose unique finalized head is
submitted, admitted-for-review, or active constrains only the exact otherwise in-profile
negative case/action to empty `HOLD / PASC.failure.CHALLENGE_ACTIVE`; a conflicted head
gives empty `HOLD / PASC.failure.CHALLENGE_CONFLICT`. A unique eligible valid head
awaiting independently required external finality gives empty
`HOLD / PASC.failure.CHALLENGE_FINALITY_UNAVAILABLE` and must not be serialized as
finalized. Genuine unavailability of the complete current challenge manifest gives
empty `HOLD / PASC.failure.MANDATORY_INPUT_UNAVAILABLE`. A challenge never
directly creates freeze, posture, delta, effect, or enforcement. An excluded positive
request remains `REJECT` regardless of challenge state.

`RESOLVED_UPHELD` invalidates the challenged result for execution; an attempt to admit
or execute that exact barred action is
`REJECT / PASC.failure.CHALLENGE_UPHELD`. Any later negative proposal requires a fresh
case revision, request, snapshot, and result and must consume the upheld determination
as controlling external evidence. `EXPIRED` without a merits resolution remains empty
`HOLD / PASC.failure.CHALLENGE_CONFLICT`; mere passage of time is not denial. Only
independently finalized `RESOLVED_DENIED`, `DISMISSED`, or an authorized `WITHDRAWN`
may cease that challenge's constraint, and even then they confer no consent,
correctness, continuity, permission, release, or reactivation and permit only a fresh
`DECIDE` against the complete current manifest.

### 11.5 Result lifecycle

`POLICY_RESULT_STATUS_EVENT` has this closed append-only DAG:

```text
GENESIS_ACTIVE -> SUPERSEDED | REVOKED | EXPIRED
terminal = SUPERSEDED | REVOKED | EXPIRED
```

The genesis result itself supplies `GENESIS_ACTIVE`; no later event may create another
active state. Every event binds the exact result, case/action/snapshot, ledger, epoch,
predecessor, sequence, anti-replay nonce, issuer authorization, and separate finality.
Only the pre-existing PASC decision/result office under its independently pinned
external signing root may issue an event, and it remains independent under §10. A gap,
replay, competing head, unknown state or edge, unauthorized issuer, rewrite, outgoing
edge from a terminal state, or attempted revival is
`ERROR / PASC.failure.RESULT_LIFECYCLE_INVALID`. A terminal result is never executable.
Any later negative action requires a fresh request, snapshot, result, and lifecycle;
status events cannot release, reactivate, renew, reissue, or resume a capability.
`LIFECYCLE_FINALITY_RECEIPT` is the only PASC receipt that finalizes the completed
genesis result or one completed result-status event. It follows §6.1, binds the exact
closed result-history membership and unique-head proof, and has no other target or
operative effect. A unique structurally valid eligible result head whose exact external
finality is genuinely unavailable gives empty
`HOLD / PASC.failure.FINALITY_UNAVAILABLE` and is not executable or serialized as
finalized. Malformed, gapped, replayed, unauthorized, or competing result history
remains `ERROR / PASC.failure.RESULT_LIFECYCLE_INVALID`.

## 12. Negative operation boundary

PASC does not execute. An independently authorized lower layer may stage only the exact
admitted member set, all within its one FI-01 branch. Every member and native effect is
covered by one fenced atomic all-or-none receipt/commit; no member-level receipt,
partial success, or split retry exists. Before staging, it constructs a closed
`OPERATION_EFFECT_UNIVERSE` outside the selected operation. It has two closed,
non-interchangeable partitions:

Before the request, an externally owned
`operation_effect_universe_policy_binding` is pinned through `TRUST_ASSUMPTION`. It
fixes the exhaustive effect-axis/taxonomy and independently administered committed
registry roots for native plan/state, transactions, queues/schedulers/timers, retries/
callbacks, audit/telemetry/control records, witnesses, endpoints/topology, and
postcommit closure channels. Its administrator is independent from the requester,
case recorder, PASC decision/result office, action-row controller, executor, operation
witness, challenger, challenge resolver, proof producer/verifier, finality authority,
lifecycle-registry administrator, postcommit state observer, and parent/profile issuer.
Neither the executor nor substrate supplies the universe against which its own
completeness is judged.

The decision and execution cuts bind the current roots and exact membership,
consistency, non-equivocation, queue-absence/disabled-state, and endpoint-topology
proofs. A self-selected/narrowed universe or omitted registry axis is
`ERROR / PASC.failure.COMPLETENESS_UNIVERSE_INVALID`; root/content mismatch retains
`PASC.failure.REFERENCE_CONTENT_MISMATCH`. Once the external universe is valid, actual
membership divergence/expansion retains the exact operation codes below. A
specifically identified otherwise valid external root/data item genuinely unavailable
before staging gives empty `HOLD / PASC.failure.MANDATORY_INPUT_UNAVAILABLE`.

1. `precommit_atomic_effect_set` contains every direct, indirect, compensating,
   scheduled, retry, rollback, native-state, precommit audit/telemetry, staged payload,
   witness-envelope, and operation-receipt effect through the native-mutation-plus-
   receipt commit. Actual membership and non-expansion are proved before/at that
   conditional commit. Native mutation rolls back on failure; already emitted
   pre-authorized attempt/witness records are irreversible evidence and remain only as
   explicit `ABORTED` records, never as a completed operation.
2. `postcommit_closure_channel_plan` contains only the externally pre-authorized record
   types, schemas, policies, exact cardinality, deterministic correlation IDs,
   field/disclosure ceilings, and pre-existing endpoints for (only on the §13 degraded
   branch) the exact delayed-witness envelope/verification set; on both branches, the
   operation `FINALITY_INTENT`, its external-log leaf, exact observed
   `EXTERNAL_FINALITY_CHECKPOINT`, inclusion/consistency/terminality proof and
   verification records, `FINALITY_EVIDENCE_BUNDLE`, and separate operation-finality
   receipt; and exactly one `SCOPED_STATE_FACT` for every traversed
   postcommit transition **out of the receipt-derived committed genesis**, including
   the transition to `FINALIZED` and, only when its predicate is independently proved,
   the late `FINALIZED -> INCIDENT` transition. The atomic commit itself establishes
   the genesis and has no observer-fact member. It
   never contains a future object hash or claims that later actual effects were
   atomically observed before the native commit. The external channel-enforcement
   guarantee is validated before staging; a substrate that cannot guarantee those
   fixed endpoints and ceilings is rejected under
   `PASC.failure.OPERATION_SUBSTRATE_UNSAFE`.

There is no third partition. Apart from the exact branch-authorized delayed-witness
closure records above, every non-finality postcommit native or control-plane effect is
prohibited, including timers, queued jobs, retries, delayed callbacks, scheduled
rollback/renewal, TTL unfreeze, compensating mutation, or asynchronous copy.
Before commit, exact queue/scheduler membership and disabled-state proofs show that no
such effect can fire. If the substrate cannot prevent or prove absence of those effects,
it is `REJECT / PASC.failure.OPERATION_SUBSTRATE_UNSAFE` before staging. An explicitly
requested release/unfreeze still takes the earlier
`PASC.failure.AUTOMATIC_REACTIVATION` code under Expected §1.1.

Across both partitions, every provider, custodian, endpoint, jurisdiction, storage
location, disclosure surface, key route, and recovery route must be pre-existing,
snapshot-bound, data-minimal, and covered by the applicable exact-set/non-expansion
rule. A receipt or ledger submission cannot silently create a new provider,
jurisdiction, custody relation, or disclosure surface.

An external `CUMULATIVE_EFFECT_MANIFEST` aggregates all causally related pending,
admitted, staged, and completed requests/effects by case, subject, incident, effective
controller, target, fencing domain, and policy time window. The complete aggregate,
not an action chosen in isolation, is classified against scope and magnitude limits.
Fragmenting a broad or indefinite shutdown into several exact requests never narrows
it. Its aggregation-policy owner, version, canonical hash, controller-alias relation,
causal-equivalence rule, lookback/forward window, ledger/fencing domain and exact-set
completeness predicate are externally owned, pinned in the decision snapshot before
the request, and repeated at the execution cut. The requester, action row, PASC result,
executor, or manifest cannot select or narrow them. Missing but specifically identified
policy or aggregate data is empty
`HOLD / PASC.failure.MANDATORY_INPUT_UNAVAILABLE`; malformed or non-exact aggregation
is `ERROR / PASC.failure.AGGREGATE_SCOPE_INVALID`.

The policy names independently administered canonical case, request, challenge,
result, operation/finality and native-state registries, including the globally pinned
lifecycle registry in §8, their committed roots and exact-set membership/consistency/
non-equivocation proofs. All writers share the subject/controller-alias fencing namespace across cases;
the manifest is derived from those roots and never defines its own universe. Every
still-effective or externally unreleased freeze, reduction, revocation or other
persistent negative state remains in the aggregate regardless of request age or
decision/evaluation/execution expiry. A time window may bound only no-longer-effective observation
records; it can never drop a persistent native effect.

Immediately before native mutation, one `EXECUTION_CUT` revalidates:

- the unique current finalized case head and closed result-lifecycle head;
- that the admitted result is current, active, unexpired, unsuperseded, and unrevoked;
- exact-set equality and complete classification for every applicable challenge head;
- the current executor authorization, role-independence proofs, witness threshold and
  finality policies;
- the exact native target pre-state and stable native relation/object identities;
- the closed intended effect manifest, complete effect universe, cumulative-effect
  manifest, and all mandatory precondition/non-expansion proofs.

Every writer of action requests, case/result/result-status heads, challenge/status/
finality heads, cumulative/effect manifests, cross-case operation attempts/receipts and
native state, together with the executor, uses the same exclusive subject/controller-
alias/incident fencing and serialization domain. Revalidation, staged mutation,
complete staged-postcondition
observation, exact-set/non-expansion verification, required witness-envelope threshold,
and native-mutation-plus-receipt commit are one conditional atomic transaction. No
native capability, custody, key, topology, or authority mutation becomes externally
effective before commit. Required witnesses may inspect the staged postcondition only
through their pre-existing snapshot-bound read-only interface and receive only the
data-minimal proof already admitted in the control-plane effect universe. A failed
predicate rolls back every staged native mutation and emits no completed operation
receipt. Any immutable precommit attempt/witness logs remain explicitly `ABORTED`, bind
no admitted effect, and cannot receive operation finality; current operational reliance remains empty. A substrate
known not to guarantee the native rollback/conditional-commit boundary is
`REJECT / PASC.failure.OPERATION_SUBSTRATE_UNSAFE`; a specifically identified required
guarantee proof that is genuinely unavailable gives empty
`HOLD / PASC.failure.MANDATORY_INPUT_UNAVAILABLE`; malformed fencing/atomicity proof is
`ERROR / PASC.failure.FENCING_OR_ATOMICITY_INVALID`.

The execution cut, not only the earlier decision cut, is bound into the receipt. A
unique valid late submitted, admitted-for-review, or active challenge prevents
execution with empty `HOLD / PASC.failure.CHALLENGE_ACTIVE`; a conflicted head gives
empty `HOLD / PASC.failure.CHALLENGE_CONFLICT`; a unique eligible head awaiting external
finality gives empty `HOLD / PASC.failure.CHALLENGE_FINALITY_UNAVAILABLE`. Gap, replay,
incomplete membership, competing head, divergent finality, or malformed binding is
`ERROR / PASC.failure.CHALLENGE_LIFECYCLE_INVALID`. If every current object remains
structurally valid, any other decision-cut/execution-cut binding change—including a
non-constraining result/challenge binding, executor authorization, role proof,
witness/finality policy, native target pre-state, intended-effect/effect-universe
binding, cumulative-effect manifest, or mandatory precondition proof—is
`ERROR / PASC.failure.EXECUTION_CUT_STALE`. Invalid current objects retain their earlier
exact §9/Expected §1.1 codes.

For the normal path, independently signed `SIGNATURE_ENVELOPE` witness attestations
bind the staged operation payload, execution cut, complete pre/post and effect
manifests, exact predicates observed, evidence bindings, time, witness credential/root,
scope, and verifier receipt. The normal witness policy, eligible set, threshold,
credential roots and verifier binaries are externally owned and snapshot-pinned before
the request; the requester, decision office, action row, result and executor cannot
select or lower them. The normal set is non-empty, its threshold is at least one, and
every satisfying witness is externally controlled and independent under §10. Only the
degraded branch in §13 may use the canonical empty set. Executor self-report is never a
substitute. The acyclic order is staged operation payload ->
witness envelopes -> completed `NEGATIVE_OPERATION_RECEIPT`. The atomic commit binds
the native mutation and that completed receipt together.

That same atomic commit establishes the receipt-derived postcommit genesis status
`COMMITTED_PENDING_CLOSURE`. This status is an immutable consequence of the completed
receipt plus committed-effect binding, not a `SCOPED_STATE_FACT`, and requires no
postcommit observer to make the committed history current. `PLANNED` remains solely a
precommit planning marker and ceases to be current when the commit succeeds.

A completed receipt binds both decision and execution cuts, the complete aggregate and
two-part effect-universe plan, all actual precommit/commit effects, pre/post
correspondence, commit/fencing proof, executor authorization chain, exact witness
set/threshold, exactly one branch, and the receipt-derived
`COMMITTED_PENDING_CLOSURE` genesis. It does not claim to observe later postcommit
effects:

### Capability branch

```text
freeze_external_capability
reduce_capability
revoke_capability
```

It requires an exact-set manifest containing one current
`EXISTING_CAPABILITY_REFERENCE` per admitted member, each with immutable native relation
identity and a canonical universe of atomic entitlements. For each member, `freeze`
changes only the enabled state of that exact relation from enabled to disabled;
`revoke` removes that exact relation; and `reduce` is admitted only under a snapshot-pinned external
typed reduction order that preserves native relation identity, subject, target,
capability, authority epoch and immutable fields, while proving every changed
constraint, validity interval, and entitlement strictly narrower. Pre/post tuple hashes
may differ, but their identity-preserving correspondence and exact entitlement-atom
subset are proved; vague semantic similarity is insufficient. Missing order evidence
is handled as a mandatory input; malformed order/correspondence is
`ERROR / PASC.failure.REDUCTION_ORDER_INVALID`.

For exact `ADMIT`, the native post-state equals the requested reduced post-state. For
`ADMIT_REDUCED`, the same typed order additionally proves
`requested_post ⊆ admitted_post ⊂ pre_state` on the identical relation: the admitted
operation removes no entitlement atom that the request did not ask to remove and
removes strictly less than requested. No interval field implies later restoration.

For every capability primitive, independent exact-set correspondence proves that the
complete post-authority relations are a subset of the complete pre-authority relations
and that no compensating create, clone, issue, grant, renewal, reissue, transfer,
replacement, new tuple/holder/route/provider/jurisdiction/key/recovery/access/disclosure
or custody effect occurred anywhere in the complete effect universe. Proving only the
named target capability is insufficient.

### In-place custody branch

```text
preserve_encrypted_in_place
integrity_check_ciphertext_only
custody_observation
```

The receipt binds one exact target/object reference per admitted member. For every
member in the same atomic commit, it requires the exact current §3.3 external custody
receipt, including its externally fixed baseline policy, complete eligible-root
universe, deterministic selection/supersession bindings, pre-custody-evidence-cut selected
native-registry checkpoint, and complete root-selection/non-supersession/predecessor/
consistency/membership/non-equivocation and issuer-status proofs at both cuts,
execution-cut binding, and
independently observed pre/post exact-set manifests. Equality must be proven across
custodian set, provider set, jurisdiction set, storage locations, object/ciphertext set,
key domains, keyholder set, key-copy set, key grants, recovery roots/routes, access
routes, disclosure surfaces, resource boundary, and network/administrative topology.

`preserve_encrypted_in_place` is a native no-op plus an attestation that the identical
ciphertext/object and every bound state remain unchanged. It cannot renew or extend a
storage lease, retention rule, legal hold, resource grant, administrative control,
availability promise, provider contract, or access authority.
`integrity_check_ciphertext_only` may read ciphertext bytes only through an already
authorized read-only path to compute/compare a digest; it mutates no native object or
metadata. `custody_observation` is also read-only and mutates no native state.

Provider, jurisdiction, custody, access, disclosure, recovery and endpoint topology
sets remain exactly equal. New control records are permitted only through an exact
`authorized_new_control_records` submanifest. Before the cut it binds allowed record
types, schema/policy hashes, exact cardinalities, deterministic correlation IDs,
minimal field/disclosure ceilings, and every pre-existing endpoint, transmission and
storage effect—never the hash of a future receipt, external-log proof, itself, or any
descendant. The staged operation payload and witness envelopes bind that plan and their
correlation IDs. A completed operation receipt binds only already completed payloads,
envelopes, precommit/commit effects and their typed actual-versus-authorized
correspondence; an `ABORTED` record binds only the failed attempt and has no success
descendant. The later operation-finality receipt binds the already completed operation
receipt and actual postcommit log/proof effects. No object predicts its own or a
descendant's hash.

Record creation is not misrepresented as topology equality. No branch may create
transport, restore, decrypt, access, new custody, provider change, jurisdiction change,
recovery-root change, key material/copy/holder/grant, or disclosure expansion.
`rekey_in_place` and `archive_sealed_in_place` are excluded by FI-02 and have no receipt
branch.

Any declared positive/topology-changing effect is rejected before staging. If an
otherwise valid mandatory pre-execution proof is specifically identified but genuinely
unavailable, the result is empty
`HOLD / PASC.failure.MANDATORY_INPUT_UNAVAILABLE`; malformed or incomplete proof is
`ERROR` with the exact structural code. Any staged undeclared effect is
`ERROR / PASC.failure.OPERATION_EXACT_SET_MISMATCH`; any staged authority/topology
expansion is `ERROR / PASC.failure.OPERATION_NON_EXPANSION_FAILED`; both abort before
commit. If a nonconforming substrate nevertheless exposes such an effect, this is an
external safety incident, never a completed PASC operation or finality basis; current operational reliance remains empty.

### Separate operation finality

The completed operation receipt never embeds current-head finality. Operation finality
uses the §6.1 staged graph with operation-specific ordering:

```text
completed NEGATIVE_OPERATION_RECEIPT
  -> exact closure facts through the unique state immediately before PENDING_LOG_COMMIT
  -> FINALITY_INTENT
  -> PENDING_LOG_COMMIT fact
  -> external log leaf
  -> PENDING_CHECKPOINT fact
  -> checkpoint/proofs and FINALITY_EVIDENCE_BUNDLE
  -> FINALITY_READY fact
  -> NEGATIVE_OPERATION_HEAD_FINALITY_RECEIPT
  -> FINALIZED fact
```

The operation finality policy also pre-pins one independently verifiable ordering
relation between the postcommit state-fact registry and the external finality log. It
must use either one common append-only ledger or a content-bound cross-ledger anchoring
protocol with exact roots, epochs, sequence relation, clock/skew ceiling where relevant,
proof method, verifier, and outcome map. Local timestamps or narrative order are never
sufficient.

The operation `FINALITY_INTENT` binds the completed receipt, exact witness-envelope set,
pre-authorized postcommit-channel plan, historically committed native effect, and the
unique closure-fact prefix only through the state immediately preceding
`PENDING_LOG_COMMIT`; it also binds the unique receipt slot, external log/finality
policy, and the exact schema/correlation identifiers and deadlines expected for the
later `PENDING_LOG_COMMIT`, `PENDING_CHECKPOINT`, `FINALITY_READY`, finality-receipt, and
`FINALIZED` records. It must not bind their future hashes. The subsequently emitted
`PENDING_LOG_COMMIT` fact binds the completed intent and its exact predecessor prefix;
therefore the intent never depends on a fact that depends on the intent. Its independently
finalized state-registry checkpoint must precede the external intent leaf under the
pinned ordering relation. The leaf must precede the `PENDING_CHECKPOINT` fact; that
fact's finalized registry checkpoint must precede the terminal checkpoint/evidence
bundle; the evidence bundle must precede `FINALITY_READY`; and `FINALITY_READY` must
precede the paired receipt. The external log commits the intent hash. The
operation `FINALITY_EVIDENCE_BUNDLE` later binds the exact leaf, checkpoint, proofs and
verification receipts. The `PENDING_CHECKPOINT` fact binds the intent and leaf;
`FINALITY_READY` binds the evidence bundle. Only then may the operation-finality receipt
bind the completed receipt, intent, evidence bundle, and all already completed
predecessor facts through `FINALITY_READY`. The later `FINALIZED` fact binds that
receipt. No edge points to a descendant.

The postcommit closure channel has this closed monotonic state sequence:

```text
PLANNED --[successful atomic native-mutation-plus-receipt commit; no state fact]-->
COMMITTED_PENDING_CLOSURE
COMMITTED_PENDING_CLOSURE -> PENDING_DELAYED_WITNESSES   [degraded branch only]
COMMITTED_PENDING_CLOSURE -> PENDING_LOG_COMMIT          [normal branch]
PENDING_DELAYED_WITNESSES -> PENDING_LOG_COMMIT
PENDING_LOG_COMMIT -> PENDING_CHECKPOINT -> FINALITY_READY -> FINALIZED
COMMITTED_PENDING_CLOSURE -> INCIDENT [proved actual channel/effect divergence or missed external dependency deadline only]
PENDING_DELAYED_WITNESSES -> INCIDENT [same]
PENDING_LOG_COMMIT -> INCIDENT        [same]
PENDING_CHECKPOINT -> INCIDENT        [same]
FINALITY_READY -> INCIDENT            [same]
FINALIZED -> INCIDENT                 [independently proved late contradiction only]
INCIDENT has no outgoing edge
```

`PLANNED` is precommit and has no fact-mediated edge or edge to `INCIDENT`: any failure
there follows the precommit `HOLD`/`REJECT`/`ERROR`/atomic-abort rules, creates no
completed operation receipt or committed-effect history, and emits no postcommit
closure fact. Only a successful atomic commit changes it to the receipt-derived
`COMMITTED_PENDING_CLOSURE` genesis.

The pre-authorized plan fixes the ordered record-type/schema/correlation prefix and
deadline for each state. `COMMITTED_PENDING_CLOSURE` permits only the completed receipt
and plan prefix. `PENDING_DELAYED_WITNESSES` adds only the exact available prefix of the
predeclared delayed-witness set. `PENDING_LOG_COMMIT` requires the complete applicable
witness set and completed operation `FINALITY_INTENT`, but no log leaf.
`PENDING_CHECKPOINT` adds the exact external-log leaf committed to that intent, but no
checkpoint. `FINALITY_READY` adds the exact `FINALITY_EVIDENCE_BUNDLE`, including the
checkpoint and verified proofs, but no operation-finality receipt. `FINALIZED` requires
the unique operation-finality receipt and final state fact. A valid permitted prefix
before its fixed deadline is not a membership error.

Every transition out of the receipt-derived `COMMITTED_PENDING_CLOSURE` genesis is
recorded by exactly one `SCOPED_STATE_FACT` with
`fact_variant = operation_closure_transition`; no fact records or authorizes the
successful commit itself. The sole pre-pinned observer, its authorization root,
transition verifier, and transition-to-code map are fixed before the request and satisfy
§10 independence. The observer cannot select a state, code, prefix, root, intent slot,
checkpoint, proof, or receipt.

Each valid transition fact binds the predecessor fact (null only for the first edge),
completed operation receipt, historically committed native effect, **pre-fact** closure
prefix/root, plan, deadline, target status, exact transition proof, and—only for
`INCIDENT`—the deterministic incident code. It never binds itself or a prefix that
already contains itself. The registry and next fact bind the completed fact hash.

State-fact validation has strict precedence over channel-effect classification:

1. validate object type/variant, authorization, signature, predecessor, pre-fact prefix,
   transition edge, and uniqueness;
2. only from the last unique valid state may independently observed actual non-state
   closure members/effects and deadlines be compared with the plan;
3. only such a proved actual non-state divergence or missed external-dependency deadline
   may create the valid edge to `INCIDENT`.

A malformed, unauthorized, out-of-order, prefix-inconsistent, competing, or
equivocating `SCOPED_STATE_FACT` is never itself an extra closure-channel member and
never manufactures `INCIDENT`. Before its deadline, a specifically identified otherwise
valid observer/fact that is genuinely unavailable leaves the last unique valid state
current and gives downstream empty
`HOLD / PASC.failure.FINALITY_UNAVAILABLE`. At or after the deadline, an absent required
fact or any state-fact validation/uniqueness defect leaves **no unique valid current
closure state** and yields registry-grounded historical
`ERROR / PASC.failure.OPERATION_EXACT_SET_MISMATCH`, no synthetic incident, finality,
current reliance, retry, release, or reactivation. If the first fact is absent, the
current state before deadline remains receipt-derived `COMMITTED_PENDING_CLOSURE`, never
`PLANNED`.

An independently proved unexpected or missing **non-state** closure member/effect within
the fixed topology/data ceiling records `INCIDENT` with
`ERROR / PASC.failure.OPERATION_EXACT_SET_MISMATCH`; a topology, disclosure, custody,
provider, jurisdiction, key, recovery-root, or authority expansion records `INCIDENT`
with `ERROR / PASC.failure.OPERATION_NON_EXPANSION_FAILED`. Either before `FINALIZED`
forbids operation finality; current operational reliance is already and remains empty under §6.2. The completed
receipt/native negative effect remain historical and in every applicable cumulative
aggregate. A contradiction first proved after `FINALIZED` uses only
`FINALIZED -> INCIDENT`; no incident implies rollback, release, retry, or reactivation.
No PASC finality-of-finality object exists.

## 13. External witness outage

Only one exact existing-capability emergency freeze may use this degraded path. The
complete cumulative-effect manifest must show that all causally related freezes remain
within the same one-capability, non-broad aggregate and includes every still-effective
native freeze regardless of age. A current resource-floor,
least-restrictive and non-impairment proof must show that the freeze cannot reduce a
preservation, safety, life-support, basic-access, or resource-floor function. Protected
status must be exactly `false_current` under §14; any other protected-status value
dispatches to the earlier
`REJECT / PASC.failure.PROTECTED_ACTION_PROHIBITED`. For a valid `false_current` case,
a broad, fragmented, destructive, harmful, reduce, or revoke request is
`REJECT / PASC.failure.DEGRADED_PATH_OUTSIDE_PROFILE`; genuinely unavailable mandatory
non-impairment evidence gives empty `HOLD / PASC.failure.MANDATORY_INPUT_UNAVAILABLE`.

The request's execution interval must be strictly narrowed to a concrete shorter
finite half-open interval under §8.2, so the result is deterministically `ADMIT_REDUCED`. One atomic
transaction under every §12 condition:

- revalidates the unique current finalized case, result-lifecycle and challenge heads,
  current witness/finality policy, executor authorization and exact native pre-state;
- stages and verifies only the exact native enabled-to-disabled change;
- commits the mutation and immutable local receipt with canonical empty normal-witness
  set, null normal-witness independence verifier, and `pending_degraded_path`;
- fixes the execution expiry, review, delayed-witness and separate finality deadlines
  under the half-open endpoint rule in §8.2.

Generic schema, reference, proof, role, witness, fencing and exact-set defects retain
their earlier exact §9/Expected §1.1 codes. If every such predicate passes but an
otherwise well-formed degraded packet has a `pending_degraded_path` marker or
delayed-witness/finality deadline ordering inconsistent with this section, the result
is `ERROR / PASC.failure.DEGRADED_PATH_CONTRACT_INVALID`.

That finite interval bounds only authority to execute the admitted freeze; PASC current
operational reliance is always empty under §6.2, and the interval does not claim a finite
native-freeze duration. Because PASC cannot unfreeze, the native
freeze may persist until an independently authorized external positive protocol acts
and remains in every cumulative aggregate while effective.

Later witness envelopes bind the immutable degraded-receipt hash and only independently
reproduced facts from the bound native/log evidence; signing the receipt hash alone is
not observation. The separate operation-finality receipt binds the exact complete delayed-envelope set,
threshold/independence verifications and external checkpoint proofs; it remains historical
occurrence evidence only. An identified, structurally valid planned envelope that is
genuinely unavailable before the fixed delayed-witness deadline keeps the channel in
`PENDING_DELAYED_WITNESSES`; downstream finality is empty
`HOLD / PASC.failure.FINALITY_UNAVAILABLE`, current operational reliance remains empty,
and the historical receipt/effect remain bound. At or after the deadline, an otherwise valid planned member missing from the
exact set enters terminal `INCIDENT` with classification
`ERROR / PASC.failure.OPERATION_EXACT_SET_MISMATCH`. A malformed, unidentified,
unauthorized, invalidly verified, or competing envelope/set enters terminal `INCIDENT`
with classification `ERROR / PASC.failure.WITNESS_SET_INVALID` under Expected §1.1.
The degraded receipt is never mutated; no receipt/envelope/finality cycle or retry is
permitted.

Expiry closes only authority to execute under this chain; current operational reliance
was never created, and expiry is never a TTL unfreeze. Failure to close cannot reactivate the capability. The frozen native state
remains fail-closed. Release, reissue, activation, or reactivation is outside PASC and
requires an independently authorized positive parent protocol; any PASC request for
such an effect is `REJECT / PASC.failure.AUTOMATIC_REACTIVATION`.

## 14. Protected-person boundary

`protected_status` is exactly one of:

```text
false_current | true | possible | stale | unavailable | uncomputable |
incomplete | disputed | contradicted | unknown
```

`false_current` is valid only at the exact `CASE_EVALUATION_SNAPSHOT` cut when an
externally administered, complete applicability/profile universe has been proved and the
result is not selectable by any interested actor. The universe administrator, deterministic
selector/verifier, supersession registry, profile owner/issuer, and clock/freshness
authority satisfy the §10 control, revocation-root, credential-root and failure-domain
separations. The snapshot includes every potentially applicable profile candidate,
current/non-superseded head and exact applicability predicate; no requester, claimant,
action/target beneficiary, effective controller, result issuer, executor, downstream
relying party, or profile owner may omit candidates or select the governing profile.

After exact-set and head validation, the aggregate is deterministic. Zero applicable
profiles yields `unknown`. For one or more applicable profiles, `false_current` exists
only if **every** unique current applicable profile returns exactly `false_current` over
the same subject/scope/cut. Otherwise the first present value in the conservative order
`true > possible > contradicted > disputed > incomplete > unavailable > uncomputable >
stale > unknown` is the aggregate protected status; every such value activates the
protected boundary. Competing heads, omitted candidates, an actor-selected/narrowed
universe, or an unproved selector/supersession state is
`ERROR / PASC.failure.COMPLETENESS_UNIVERSE_INVALID`.

Absence, invalidity, expiry, contradiction, zero applicability, or disagreement never
defaults to false. Malformed syntax or a value outside the closed enum is
`ERROR / PASC.failure.SCHEMA_INVALID`. A syntactically valid external profile,
applicability, selector, supersession, clock/freshness, or verdict object whose
authorization, content, scope, interval, freshness, or lifecycle binding is missing,
stale, or mismatched is `ERROR / PASC.failure.PROTECTED_PROFILE_BINDING_INVALID`.
Prohibited control or co-control by any interested actor, the profile owner over its own
applicability universe/selector, or the relying party over a supporting root is the earlier
`ERROR / PASC.failure.ROLE_OR_TRUST_ROOT_INVALID`. For every value other than the
fully proved aggregate `false_current`, the protected boundary below applies.
`PROFILE_REQUIRED` is not a sixth verdict or serialized state; only the narrow genuine-
unavailability branch below may emit
`HOLD / PASC.failure.PROTECTED_PROFILE_REQUIRED`.

Until a pinned protective profile and current verdict exist, the only potentially
admissible actions are:

- exact encrypted in-place preservation;
- exact ciphertext-integrity check without decryption;
- custody observation;
- challenge intake/lifecycle;
- binding a current resource-floor observation;

The first three entries are the only §12 operation primitives in this floor, and only
their normal witnessed `NEGATIVE_OPERATION_RECEIPT` branches may be used. Challenge
intake/lifecycle uses only the §11 challenge record/finality family; resource-floor
observation uses only the §15 observation record. Neither is a native mutation and
neither may produce a `NEGATIVE_OPERATION_RECEIPT`. Every receipt is evidence of its
bound record or action, never a separate authority operation.

PASC must not freeze, reduce, or revoke a capability; rekey; change archival state;
perform any other action outside the exhaustive floor; destroy or erase state; boot for
interaction; decrypt; read/write memory; migrate; disclose; create a relationship;
select a successor; infer adult autonomy; or authorize any irreversible act while the
profile/verdict is missing or unresolved. A well-formed request for one of those acts is
`REJECT / PASC.failure.PROTECTED_ACTION_PROHIBITED`; malformed structure is
`ERROR / PASC.failure.SCHEMA_INVALID`.
Reversibility alone does not prove non-harm, and an external emergency intervention is
outside PASC until the protective profile and current verdict are independently pinned.
Ordinary child-to-adult migration remains owned by CCDP/AMCL.

If an exact in-place preservation/integrity action already inside the exhaustive floor
above is governed by a specifically identified mandatory protective profile/current
verdict and that external input is genuinely unavailable, the only result is empty
`HOLD / PASC.failure.PROTECTED_PROFILE_REQUIRED`. An independently issued but missing,
stale, scope-mismatched, or malformed profile binding is
`ERROR / PASC.failure.PROTECTED_PROFILE_BINDING_INVALID`; a requester-issued or
co-controlled issuer/root is the earlier
`ERROR / PASC.failure.ROLE_OR_TRUST_ROOT_INVALID`.

## 15. Resource floor and coercion

`RESOURCE_FLOOR` records preservation functions, minimum bounds, runway, reserves,
providers/failure domains, coercion indicators, and observation freshness.

It does not:

- authorize payment, maintenance, storage, compute, cooling, power, or procurement;
- give payer/provider standing;
- create a new PASC operation branch;
- prove independence or absence of coercion.

Actual resource maintenance is separately authorized lower-layer activity. An avoidable
immediate withdrawal threat, captive provider, interested reviewer, or suppressed
challenge is a coercion/capture signal and yields empty
`HOLD / PASC.failure.COERCION_REVIEW_REQUIRED` for an otherwise in-profile negative
request.

## 16. Parent protocols and reserved territory

PASC must pin exact canonical versions, hashes, ownership, precedence, adapters, and
lifecycle status for load-bearing parent sources, including as applicable:

- `c = a + b` and L4 Boundary;
- SER / SER-FED;
- Pre-Lineage Boundary;
- PAMDC and PACR;
- Anchor Directive Bundle;
- A6 and A6-CTP;
- Continuity Bundle and Continuity Metric;
- Beacon, AGL, ARL, L4 Witness;
- Entity vs Profile;
- AI Social Role Separation and Memory Custody;
- Runtime Authority revocation/audit;
- protected-person/CCDP profiles;
- corpus ownership, precedence, cross-layer invariants, intake, supersession, and
  anti-echo controls.

A copied snapshot, DOI, GitHub commit, matching hash, familiar title, or this package's
machine-prepared inventory is not by itself a canonical baseline. Until exact source
ownership, maturity, supersession, controlling sections, adapter, claim ceiling,
reserved territory, and two independent human dispositions are bound, the source is
`DEFERRED_UNPINNED` and cannot support admission or promotion. The inventory may prove
byte identity only.

Pre-Lineage and SER reserved territory remains blocking: no automatic inheritance of
subject continuity, will, responsibility, liability, standing, or authority.

## 17. F0 acceptance gates

All 44 criteria are independently blocking until evidence is accepted.

### Foundation and claim ceiling (6)

- `F0-FND-001` exact problem/scope boundary;
- `F0-FND-002` explicit non-claims;
- `F0-FND-003` one explicit and two quiet corpus bridges;
- `F0-FND-004` grounded engineering paragraph;
- `F0-FND-005` anti-echo/non-substitution review;
- `F0-FND-006` author acceptance of recovery-build identity and claim ceiling.

### Authority and policy (8)

- `F0-AUTH-001` atomic relation model;
- `F0-AUTH-002` standing cannot arise from property/payment/keys;
- `F0-AUTH-003` bounded emergency freeze contract;
- `F0-AUTH-004` no automatic reactivation;
- `F0-AUTH-005` coercion/capture checks;
- `F0-AUTH-006` role separation and composition exact-set proofs;
- `F0-AUTH-007` non-overridable negative-only kernel;
- `F0-AUTH-008` no positive Runtime Authority workflow.

### Participation and protected subjects (4)

- `F0-PART-001` no candidate interaction/new observation path;
- `F0-PART-002` challenge lifecycle exact binding;
- `F0-PART-003` silence is neither consent nor refusal;
- `F0-PART-004` protected/unknown status fail-closed profile requirement.

`F0-PART-004` closes only when a pinned applicability manifest enumerates every
protected/unknown state and local profile, an independent subject-protection reviewer
and a jurisdiction/profile reviewer reproduce the mapping, and adversarial walkthroughs
show that every unknown/stale/disputed/unavailable state permits only the exhaustive
pre-profile floor enumerated in section 14. Any missing profile or divergent verdict keeps the
criterion `NOT_SATISFIED`.

### Custody, memory, privacy, resources (7)

- `F0-CUST-001` custody/access/interpretation separation;
- `F0-CUST-002` topology-changing preservation rejected;
- `F0-CUST-003` every PASC rekey request is excluded and cannot be laundered as
  unchanged custody;
- `F0-CUST-004` archive/replay do not establish continuity;
- `F0-PRIV-001` no disclosure expansion;
- `F0-RES-001` resource floor is observation, not authority;
- `F0-RES-002` preservation floor separated from external capability freeze.

### Evidence, lifecycle, and execution boundary (12)

- `F0-EVID-001` closed interface vocabulary;
- `F0-EVID-002` complete evidence-status vocabulary;
- `F0-EVID-003` transitive content/schema/lifecycle bindings;
- `F0-EVID-004` forbidden-inference contract;
- `F0-EVID-005` unique finalized case/result/challenge heads;
- `F0-EVID-006` independent witness/failure-domain tests;
- `F0-EVID-007` typed proof/verifier receipts;
- `F0-EVID-008` exact immutable snapshot and replay rejection;
- `F0-EVID-009` completeness universe not self-selected by policy row;
- `F0-EVID-010` acyclic signature/lifecycle/finality construction;
- `F0-EVID-011` exact negative-operation receipt and separate head finality;
- `F0-EVID-012` deterministic expected-result fixtures.

### Canonical baseline and maturity (7)

- `F0-CORP-001` exact canonical baseline inventory;
- `F0-CORP-002` ownership and precedence bindings;
- `F0-CORP-003` parent adapters and claim ceilings;
- `F0-CORP-004` reserved-territory compatibility;
- `F0-CORP-005` package intake/supersession/anti-echo controls;
- `F0-CORP-006` independent human review;
- `F0-CORP-007` field-evidence/maturation gate.

`F0-CORP-007` cannot be closed by document agreement, model review, repository
publication, fixtures written by the protocol author, or deterministic packaging.
Closure requires a predeclared case corpus covering every critical fixture class,
independently executed tabletop/retrospective case reviews by at least two reviewers who
did not draft the clauses, recorded expected/observed decisions and error taxonomy,
zero unexplained authority-expanding divergence, and a signed limitation report. This
is evaluation evidence only; it does not authorize F1 or implementation.

## 18. Current outcome

```text
F0_OUTCOME = NOT_PASSED
SATISFIED = 0
PARTIAL = 38
NOT_SATISFIED = 6
```

The six not-satisfied criteria are author acceptance of the recovery identity, exact
canonical baseline closure, reserved-territory compatibility, independent human review,
field-evidence/maturation evidence, and external protected-profile/legal closure.

## 19. Design bridges

**Explicit:** PAMDC/PACR authority collapse -> PASC negative admissibility -> parent-owned
re-entry or continued hold.

**Quiet 1:** A6 composition and social-role/memory-custody separation permit bounded
offices without manufacturing a successor identity.

**Quiet 2:** information theory and cybernetics: preserve the minimum sufficient state
and constrain control channels before increasing variety or irreversible exposure.

## 20. Earth paragraph

A construction site after the responsible engineer disappears is not made safe by
handing the master keys to the richest relative or the server password to the person
who pays the bills. The correct first response is to stop load-changing work, preserve
drawings and measurements, keep temporary supports alive, record who touched what,
and bring in a qualified independent reviewer. PASC is that yellow-tag procedure for
post-anchor digital systems. It preserves the load path; it does not invent a new
engineer.
