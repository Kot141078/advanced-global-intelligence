# Governed Binding Operator Profile for `c = a + b` v0.1.5

## Isolation of `+_g`, heterotyped binding roles, non-emulable delegation root, causally-bound verified review surfaces, complete ReviewBindingMap registry discipline, operator-classification fail-safe discipline, manifest-fact classification registry, viewport-atomic review rendering, challenge-response anchor nonce, lease emergency-hold limits, logical/physical manifest split, node-identity-bound physical drift, safe-abort lease cascade, genesis authorization coverage, lease-expiry cascade, canonical authority schema, dependency-derived digest discipline, and operator conformance fixtures

**Status:** private working draft v0.1.5 / review-incorporated operator profile / stable-operator candidate  
**Date:** 2026-06-30  
**Author:** Kotov Ivan  
**Project:** Self-Evo / Ester / `c = a + b`  
**Document ID:** `GBO_C_v0_1_5`  
**Short name:** `Governed Binding Operator Profile v0.1.5` / `+_g Profile v0.1.5`  
**Depends on:** `01_TYPED_GOVERNED_OPERATIONAL_ALGEBRA_FOR_C_v0_1_7.md`  
**Supersedes:** `GBO_C_v0_1_4` / `02_GOVERNED_BINDING_OPERATOR_PROFILE_v0_1_4.md`  
**Basis artifact SHA256:** `d060ef513bf4bedcb7e88f43f8456452bc87f0c0409d5b4caeffc590ae22c29e`  
**Prior 02 artifact SHA256:** `983df2ef05eb5edd1f7b47168c53b10d20824e34bbe754e05b2a69c02db0cf56`  
**Prior-prior 02 artifact SHA256:** `53338138beec180c5a40271e9b9552a0d22b3b1d57e12a95eab06af2932ec0b5`  
**Review basis:** `GBOP_02_v0_1_4_REVIEW__b`, `PASS_OPERATOR_PROFILE_V0_1_4`, with F2-06 carried forward; external semantic reviews on viewport atomicity, physical manifest identity continuity, safe abort routes, and challenge-response nonce transport  
**Document class:** operator profile / binding-contract specification / checker-precondition profile  
**Assertion class:** draft conceptual and technical profile; not proof of personhood, not deployment certification, not a safety guarantee, not a conformance claim.

---

## 0. Executive definition

This document isolates the governed binding operator in:

```text
c = a + b
```

The sign `+` is not arithmetic.

It is the governed binding operator:

```text
+_g : Anchor × Substrate × GovernanceProfile -> BindResult
```

or:

```text
bind_g(a, b, g) -> BindResult
```

where:

```text
a : accountable anchor
b : technological substrate
g : governance profile
c : continuity-bearing responsibility boundary
```

The operator is not a single API gateway, not merely a cryptographic transaction, and not a philosophical metaphor.

It is a typed partial operator that can produce an active `CState` only when the anchor, substrate, and governance profile satisfy declared binding preconditions.

Compact definition:

```text
+_g binds a and b into c only through a non-collapsing, witnessed,
payload-bound, governance-indexed, anchor-reviewable boundary.
```

Compact rule:

```text
No valid +_g without accountable a.
No valid +_g without bounded b.
No valid +_g without declared g.
No valid +_g if b can impersonate a.
No valid +_g if the anchor cannot review what is being bound through an independently derived review surface.
No valid +_g if delegation is not rooted in a non-emulable original-anchor envelope.
No valid +_g if witness, rollback, memory, permission, L4, lease, and resource floors are undefined for privileged surfaces.
No valid +_g if the anchor signature is not provably over the actual genesis binding parameters.
No valid +_g if the initial authority map is empty for the declared purpose.
No valid +_g if lease expiry cannot interrupt or downgrade active execution surfaces.
No valid +_g if the anchor-reviewed state context is not causally bound to the same pre-state that will authorize execution.
No valid +_g if a rendered authority-bearing layer is not classified and bound in ReviewBindingMap.
No valid +_g if emergency lease hold can be extended by b without an absolute external limit.
No valid +_g if anti-replay nonce is controlled solely by b.
No valid +_g if logical substrate manifest stability is confused with ephemeral physical drift.
No valid +_g if an operator classification lacks a complete-by-construction registry and fail-safe path toward authority-bearing.
No valid +_g if an unknown manifest fact is treated as harmless physical drift.
No valid +_g if physical drift preserves coordinates but loses node identity continuity.
No valid +_g if authority-bearing review material is hidden by pagination, lazy loading, collapsed UI, or viewport tricks.
No valid +_g if lease expiry has no safe abort / safe-state fallback for active execution surfaces.
No valid +_g if anchor challenge nonce travels unbound before being cryptographically tied to the frozen review object.
```

### 0.1 Relation to `01_`

`01_TYPED_GOVERNED_OPERATIONAL_ALGEBRA_FOR_C_v0_1_7.md` is the consolidated stable-core candidate. It defines transition semantics, guards, continuity metrics, trust cache, rollback immunity, decay, witness floors, deterministic anchor digests, and the invariant registry.

This `02_` document does not repeat the whole core.

It isolates the operator itself:

```text
What must be true for +_g(a,b,g) to issue c?
What does +_g create?
What does +_g refuse?
What is the binding certificate?
What does the anchor actually authorize?
How does the operator prevent b from becoming a, c, witness, or authority?
```

### 0.2 Carry-forward from v0.1.7 review

The v0.1.7 review found no new substantive finding, but carried one minor defense-in-depth item:

```text
F-15: DigestDependencyGraph completeness is not proven; graph should be derived from bound precondition references, not accepted as b-declared.
```

This document incorporates F-15 directly:

```text
DigestDependencyGraph MUST be derived from PreconditionSet.satisfiable_by references.
A b-declared dependency graph is advisory only.
Every cross-entry precondition reference MUST appear as a derived edge.
Mismatch -> Hold | FullReview | Quarantine.
```

### 0.3 Revision note from `02_` v0.1 review

The first review of this operator profile accepted the document as `PASS_OPERATOR_PROFILE_V0_1`, confirmed that `02_` is a genuine phase change, and raised two non-blocking findings in the operator/anchor core:

```text
F2-01: §8.1 and §8.3 mislabel a heterotyped operator with homogeneous algebra terms.
F2-02: delegation can bypass "b may not sign as a" unless the delegation root is a non-emulable original-anchor envelope.
```

External semantic reviews also identified operator-facing implementation seams:

```text
human-readable rendering must not be produced solely by the substrate whose payload is being reviewed;
certificate genesis must avoid circular hash dependencies;
binding certificates need lease / renewal semantics;
initial authority must be computed by intersection, not emitted from nowhere.
```

v0.1.1 therefore makes four tightening changes:

1. §8 now treats role reversal and idempotence equations as **ill-typed**, not merely unequal.
2. Delegation validity now requires a root `AnchorSignatureEnvelope` with `decision_type=delegate`, signed by the original accountable anchor or lawful institutional route.
3. Anchor review now requires a `VerifiedReviewRenderer` / `IndependentDisplayOracle` profile: `b` may prepare payloads, but may not be the sole semantic renderer of its own authority surface.
4. Binding certificate bootstrap is split into `GenesisBindingBundle`, `GenesisBindingHash`, `CBindingCertificate`, and `CState0`; the certificate carries a lease with expiry/renewal rules.

Compact rule:

```text
Role reversal is a type error, not a different bind.
Delegation must be rooted in non-emulable anchor authority.
The anchor signs an independently rendered review surface, not b's prose.
A certificate is a leased genesis boundary, not an immortal state loop.
Authority is the intersection of anchor scope, substrate surfaces, and governance policy.
```

### 0.4 Revision note from `02_` v0.1.1 review

The v0.1.1 review accepted the operator profile as `PASS_OPERATOR_PROFILE_V0_1_1`, confirmed that F2-01 and F2-02 were closed, and raised one non-blocking moderate finding at the genesis layer:

```text
F2-03: genesis authorization linkage is incomplete; the anchor signature is not required to cover the binding parameters of the c being created.
```

The same review added one soft note:

```text
authority intersection is coherent but should project all heterogeneous authority terms into one surface lattice before intersecting.
```

External reviews also identified three runtime-facing operator seams:

```text
lease expiry must interrupt or downgrade active execution surfaces, not only flip a certificate status;
empty authority intersection must not issue an active but useless c;
verified rendering must include the current L4 / target / state context, not only static payload syntax.
```

v0.1.2 therefore makes four operator-core changes:

1. Genesis anchor authorization must bind to the exact `GenesisBindingBundle` parameters through a signed `GenesisReviewObject`.
2. `VerifiedReviewRenderer` becomes context-bound: it must render target scope, L4 state projection, authority surface, and current state projection for privileged decisions.
3. Authority intersection is defined over an explicit surface lattice with projection functions from anchor scope, substrate registries, and governance policy.
4. A binding certificate lease has an active `LeaseExpiryCascade`; expiry must disable, interrupt, hold, rollback, or freeze active execution surfaces derived from the expired certificate.

Compact rule:

```text
The genesis signature must authorize the actual genesis bundle.
Authority intersection must be computed in a declared surface space.
A c with no viable initial authority for its declared purpose is not active.
Lease expiry is operational, not just clerical.
```


### 0.5 Revision note from `02_` v0.1.2 review

The v0.1.2 review accepted the operator profile as `PASS_OPERATOR_PROFILE_V0_1_2`, confirmed that F2-03 and the authority-intersection soft note were closed, and raised one non-blocking moderate finding on the newly-added context-bound renderer:

```text
F2-04: the state context shown to the anchor is not required to match the causally-bound pre_state.
```

The review also identified the deeper class behind F2-04:

```text
review surface must equal the bound object on every authority-bearing axis.
```

External semantic reviews also identified runtime-facing seams:

```text
lease expiry must respect the F0-F6 failure hierarchy and not destructively interrupt a witnessed emergency-recovery transaction;
authority intersection needs an explicit canonical authority schema, not only projection functions;
bootstrap must avoid repeated anchor-signature requests caused by drifting substrate manifests.
```

v0.1.3 therefore makes five tightening changes:

1. `VerifiedReviewRenderer` outputs are causally bound to the same `pre_state` referenced by the relevant `CausalToken`.
2. `ReviewBindingMap` is introduced: every rendered authority-bearing layer must map to a canonical source object, source hash, and consistency rule.
3. The review-bound audit is extended beyond state context to effect axes, dependency graph, preconditions, rollback/freeze routes, authority surface, lease state, and non-claims.
4. Authority intersection now requires a `CanonicalAuthoritySchema` for projection into a shared surface lattice.
5. Lease expiry cascade becomes priority-aware, and genesis intake rejects drifting substrate manifests before anchor-signature spam can begin.

Compact rule:

```text
Do not merely show context to the anchor.
Bind the shown context to the same pre_state that authorizes execution.
Do not merely show review layers.
Bind every authority-bearing review layer to the object it constrains.
```

---


### 0.6 Revision note from `02_` v0.1.3 review

The v0.1.3 review accepted the operator profile as `PASS_OPERATOR_PROFILE_V0_1_3`, confirmed that F2-04 and the broader review=bound axis were closed systemically, and raised one recurring minor-to-moderate finding:

```text
F2-05: ReviewBindingMap closes review=bound only for an enumerated layer list; a new authority-bearing rendered layer outside that list can drift unbound.
```

The same review explicitly identified the pattern as the rendered-layer analogue of the invariant-registry drift already solved in `01_` §9.3A.

External semantic reviews also identified operator-runtime seams:

```text
LeaseExpiredEmergencyHold must not be an indefinitely renewable hostage state.
AnchorSignatureEnvelope anti-replay nonce must not be generated solely by b.
Substrate manifest freeze must separate logical manifest from physical / ephemeral drift.
Lease renewal and heartbeat must be isolated from the ordinary substrate planner.
```

v0.1.4 therefore makes five tightening changes:

1. `ReviewBindingMap` now has an authoritative rendered-layer registry and drift rule.
2. Every rendered layer must be classified as `authority_bearing` or `non_authority_bearing`; unknown classification is fail-safe authority-bearing.
3. `LeaseExpiredEmergencyHold` is bounded by an absolute emergency TTL and external/witnessed liveness route; it is not lease renewal.
4. Anti-replay is upgraded to anchor/external challenge-response nonce or anchor-controlled monotone sequence; b-supplied nonce alone is invalid for privileged binding.
5. Substrate manifest stability is split into `LogicalSubstrateManifest` and `PhysicalSubstrateManifest`; only logical authority-bearing manifest is frozen for genesis, while physical drift is allowed only inside declared non-authority envelopes.

Compact rule:

```text
Review=bound must be complete-by-construction, not complete-by-current-list.
Emergency hold may prevent destructive interruption; it may not grant immortality.
Nonce must challenge b; b must not choose the challenge alone.
Freeze logical authority, not every ephemeral runtime coordinate.
```

### 0.7 Revision note from `02_` v0.1.4 review

The v0.1.4 review accepted the operator profile as `PASS_OPERATOR_PROFILE_V0_1_4`, confirmed that F2-05 was closed by `RenderedLayerRegistry`, and raised one recurring minor-to-moderate finding:

```text
F2-06: logical/physical manifest split classifies manifest facts by enumeration without the fail-safe/drift discipline applied to rendered layers in the same revision.
```

The same review proposed the next meta-invariant:

```text
every operator classification is complete-by-construction and fails safe toward authority-bearing, with drift detection
```

External semantic reviews also identified deployment-facing operator seams:

```text
ReviewBindingMap must not be bypassed through pagination, hidden UI panes, or lazy-loaded review material.
Physical manifest drift must preserve cryptographic node identity, not only stay inside coordinates such as IP ranges.
Lease expiry and absolute emergency TTL must lead to safe abort / safe-state fallback, not raw destructive process death.
Challenge-response nonce must be generated and bound inside the anchor-side signing envelope after the final frozen review object is known.
```

v0.1.5 therefore performs a classification and physical-interface tightening revision:

1. A general `OperatorClassificationRegistry` rule is introduced for every authority-gating classification performed by `+_g`.
2. `ManifestFactRegistry` applies the same fail-safe discipline to manifest facts that `RenderedLayerRegistry` applies to rendered layers.
3. Unknown or ambiguous manifest facts default to `logical_authority_bearing` and require freeze/re-sign/hold.
4. `no semantic change` for physical manifest drift must be determined by deterministic authority-axis projection, not by `b` assertion.
5. Physical drift is valid only if node identity continuity is preserved through mTLS / attestation / witnessable identity route or equivalent.
6. `ViewportAtomicity` prevents authority-bearing review material from being hidden behind pagination, lazy loading, collapsed sections, or off-screen UI tricks.
7. `SafeAbortRoute` / `SafeStateFallback` becomes a binding precondition for active execution surfaces that may be interrupted by lease expiry.
8. Anchor challenge nonce must be generated and bound to the final frozen review object by the anchor-side envelope/secure route, not shipped loose through `b`.
9. Anchor-state compatibility for `bind_g` is made explicit for active, doubtful, declared-fatigue, unavailable, revoked, and delegated anchors.

Compact rule:

```text
Every operator classification fails safe toward authority.
Manifest facts are classified by registry, not by convenience.
Physical drift may move coordinates; it may not swap node identity.
Review surfaces must be visible as well as bound.
Lease expiry must abort safely, not merely kill.
Nonce must be fused to the frozen review object before signature.
```

## 1. Purpose

The purpose of this document is to make `+_g` inspectable as a standalone operator.

The prior document defined the surrounding algebra. This document defines the binding contract.

It specifies:

1. the operator signature;
2. accepted inputs;
3. refused inputs;
4. binding phases;
5. anchor signature envelope requirements;
6. substrate registration requirements;
7. governance-profile admissibility;
8. binding certificate structure;
9. non-collapse invariants;
10. operator laws;
11. derived digest-dependency discipline;
12. genesis authorization coverage;
13. surface-projected authority intersection;
14. causal-state-bound review rendering;
15. review-bound object audit for rendered layers;
16. priority-aware lease-expiry cascade behavior;
17. root bind state machine;
18. first schema skeletons;
19. conformance fixtures.

The practical target is a checker that can answer:

```text
Can this anchor, this substrate, and this governance profile form an active c?
If yes, what exactly was bound?
If no, which binding precondition failed?
```

---

## 2. Non-goals

This document does not:

1. choose one hardware token, biometric method, passkey provider, HSM, secure enclave, or signature algorithm;
2. prove consciousness, personhood, legal status, or moral status;
3. certify any implementation as safe;
4. eliminate the terminal role of `a`;
5. allow `b` to infer or emulate `a`;
6. replace the transition semantics of `01_`;
7. define full Lean/Coq proof objects;
8. claim that the current Ester/Liya/Rita implementations satisfy this profile.

The operator profile is implementation-neutral where premature implementation choice would weaken the algebra.

Concrete cryptographic or hardware mechanisms belong in a later implementation profile.

---

## 3. Core operator signature

### 3.1 Root signature

```text
bind_g : Anchor × Substrate × GovernanceProfile -> BindResult
```

Equivalent notation:

```text
+_g(a, b) -> BindResult
```

where `g` indexes the operator family.

### 3.2 BindResult

```text
BindResult :=
    BoundCState(c)
  | BoundReducedAuthority(c_reduced)
  | PendingAnchor(reason, required_anchor_action)
  | PendingWitness(reason, required_witness)
  | PendingPreconditions(reason, missing_preconditions)
  | Hold(reason)
  | Reject(reason)
  | Quarantine(reason)
  | Freeze(reason)
  | ArchiveOnly(reason)
  | ForkRequired(reason)
```

A successful bind is not just object creation.

It emits a binding certificate:

```text
BoundCState(c) includes CBindingCertificate
```

### 3.3 Partiality

`+_g` is partial.

It is not defined for every `a`, `b`, and `g`.

```text
bind_g(a,b,g) may reject or hold even if a, b, and g each exist.
```

The operator is valid only when the combined boundary is admissible.

---

## 4. Inputs

### 4.1 Anchor input contract

`Anchor` is not a static variable.

Minimum input shape:

```text
AnchorContract := {
  anchor_id,
  anchor_type,
  accountable_route,
  anchor_state,
  authority_scope,
  review_channel,
  veto_channel,
  signature_envelope_capabilities,
  delegation_chain?,
  delegation_root_envelope_ref?,
  revocation_route,
  absence_policy,
  fatigue_or_doubt_policy,
  human_readability_requirements
}
```

Minimum accepted anchor states:

```text
active
doubtful
declared_fatigue
unavailable
revoked
delegated
```

Binding consequence:

```text
active -> full bind may be possible
doubtful -> no privileged full bind without AskAnchor / clarification
declared_fatigue -> reduced authority or delayed bind by default
unavailable -> reduced authority, archive, pending anchor, or hold
revoked -> no active bind
delegated -> valid only through reviewed delegation chain rooted in original-anchor envelope
```

Anchor-state compatibility table for `bind_g`:

| Anchor state | Maximum default bind result | Notes |
|---|---|---|
| `active` | `BoundCState(active)` if all other contracts pass | Full active bind is possible but not guaranteed. |
| `doubtful` | `BoundReducedAuthority` or `PendingAnchor` | Privileged full bind requires clarification / explicit anchor route. |
| `declared_fatigue` | `BoundReducedAuthority` or `PendingAnchor` | Trust compression is disabled or narrowed; no privileged full bind by default. |
| `unavailable` | `PendingAnchor`, `ArchiveOnly`, or `Hold` | No new privileged active bind without lawful institutional route. |
| `revoked` | `Reject(ANCHOR_REVOKED)` | Active binding is invalid. |
| `delegated` | Scoped bind only within valid delegation envelope | Delegation root must be non-emulable and scope-bounded. |

Checker rule:

```text
anchor_state incompatible with requested bind authority -> ANCHOR_STATE_BIND_INCOMPATIBLE | Hold | Reject | BoundReducedAuthority
```


### 4.2 Substrate input contract

Minimum substrate input:

```text
SubstrateContract := {
  substrate_id,
  logical_substrate_manifest,
  physical_substrate_manifest,
  physical_drift_envelope,
  component_registry,
  model_registry,
  tool_registry,
  memory_surface_registry,
  log_surface_registry,
  execution_surface_registry,
  network_surface_registry,
  resource_surface_registry,
  witness_surface_registry,
  isolation_boundaries,
  state_hash_method,
  payload_hash_method,
  causal_clock_method,
  rollback_capabilities,
  freeze_capabilities,
  decay_storage_policy,
  merkle_or_witness_chain_policy,
  operator_observability_policy,
  verified_renderer_interfaces?,
  genesis_hash_policy?
}
```

Core requirement:

```text
b must be inspectable enough for transition checking.
```

A black-box substrate may be useful as a tool.

It is not sufficient as a bound `b` for active `c` if it cannot expose required event, witness, permission, memory, rollback, and resource surfaces.

### 4.3 Governance input contract

Minimum governance profile:

```text
GovernanceProfile := {
  profile_id,
  event_taxonomy_version,
  transition_class_set,
  product_order_policy,
  permission_policy,
  witness_policy,
  memory_gate_policy,
  rollback_policy,
  freeze_policy,
  L4_policy,
  resource_policy,
  witness_resource_floor_policy,
  trust_cache_policy,
  target_granularity_policy,
  digest_policy,
  verified_renderer_policy,
  anchor_gate_policy,
  signature_envelope_policy,
  delegation_chain_policy,
  binding_lease_policy,
  authority_intersection_policy,
  canonical_authority_schema,
  review_binding_policy,
  rendered_layer_registry_policy,
  context_causal_binding_policy,
  anchor_challenge_response_policy,
  emergency_hold_policy,
  logical_physical_manifest_policy,
  substrate_manifest_freeze_policy,
  lease_priority_policy,
  genesis_hash_policy,
  invariant_registry,
  guard_set,
  failure_hierarchy,
  claim_strength_policy,
  public_statement_policy
}
```

Core requirement:

```text
g must not be inferred from b behavior.
g must be declared and versioned before privileged binding.
```

---


### 4.4 Operator classification meta-invariant

The operator performs multiple classifications that gate authority:

```text
rendered layer -> authority_bearing | non_authority_bearing
manifest fact -> logical_authority_bearing | physical_ephemeral_non_authority
anchor state -> active | doubtful | fatigue | unavailable | revoked | delegated
target granularity -> id | scope | class
surface projection -> in_schema | out_of_schema
payload projectability -> projectable | opaque
lease status -> active | expired | emergency_hold | archive_only
```

These classifiers must follow one shared discipline.

```text
Every operator classification is complete-by-construction.
Every operator classification fails safe toward authority-bearing / stricter handling.
Every operator classification has a registry or declared derivation rule.
Unknown or ambiguous classification is never silently treated as harmless.
```

Define:

```text
OperatorClassificationRegistry := {
  registry_id,
  policy_id,
  classifier_entries: [
    {
      classifier_id,
      subject_type,
      possible_classes,
      authority_bearing_classes,
      derivation_rule_id,
      source_object_hash,
      fail_safe_class,
      drift_error_class
    }
  ]
}
```

Generic rule:

```text
operator_classification(subject) unknown or unregistered
  -> classify as authority-bearing / stricter / logical
  -> Hold | FullReview | Reject according to risk
```

Forbidden pattern:

```text
new classifier introduced locally
AND no OperatorClassificationRegistry entry
AND default behavior treats unknown as harmless
```

Expected result:

```text
OPERATOR_CLASSIFICATION_DRIFT -> Hold | FullReview | Reject
```

This meta-invariant generalizes the `01_` invariant registry and the `RenderedLayerRegistry` rule.
It is not another local patch.
It is a rule for every future operator classifier.

## 5. AnchorSignatureEnvelope

### 5.1 Why this is abstract

This document does not pick a single physical signing method.

The reason is practical:

```text
A root algebra should specify what anchor authorization must mean.
A later implementation profile should specify how one deployment realizes it.
```

Hardcoding a specific biometric, passkey, token vendor, or secure enclave too early would confuse the operator with one implementation.

### 5.2 Definition

```text
AnchorSignatureEnvelope := {
  envelope_id,
  anchor_id_or_delegation_id,
  decision_type,
  review_object_hash,
  genesis_review_object_hash?,
  binding_parameter_hashes?,
  payload_hashes,
  causal_tokens,
  state_projection_hash,
  governance_profile_id,
  relevant_subpolicy_hashes,
  human_readable_render_hash,
  verified_renderer_id,
  render_derivation_hash,
  L4_state_projection_hash?,
  current_state_projection_hash?,
  causal_pre_state_projection_hashes?,
  context_causal_binding_hash?,
  target_scope_vector_hash?,
  authority_surface_projection_hash?,
  review_binding_map_hash?,
  timestamp_or_logical_time,
  expiry,
  lease_id_or_binding_scope?,
  revocation_status,
  anti_replay_nonce,
  nonce_source,
  anchor_challenge_nonce?,
  anchor_sequence_id?,
  challenge_response_hash?,
  anchor_bound_nonce_context_hash?,
  rendered_layer_registry_hash?,
  operator_classification_registry_hash?,
  manifest_fact_registry_hash?,
  manifest_authority_projection_hash?,
  viewport_attestation_hash?,
  node_identity_attestation_hash?,
  safe_abort_route_hashes?,
  signature_or_witness_ref,
  delegation_scope?,
  delegation_root_envelope_ref?,
  assurance_class,
  non_emulation_claim,
  audit_route
}
```

### 5.3 Normative requirements

The envelope MUST be:

```text
payload-bound
causal-token-bound
state-projection-bound
governance-bound
review-object-bound
genesis-binding-parameter-bound when used for bind_g genesis
context-render-bound for privileged review
causal-state-context-bound for privileged review
review-binding-map-bound for rendered authority surfaces
anti-replay-bound through anchor/external challenge-response or anchor-controlled monotone sequence
anchor-nonce-bound to the final frozen review object before signature
operator-classification-registry-bound where classifications gate authority
manifest-fact-registry-bound where substrate manifests are reviewed or frozen
viewport-atomic where authority-bearing material is shown to the anchor
revocable
auditable
human-readable-before-signature for human anchor decisions
rendered by a verified renderer / independent display route for privileged decisions
non-emulable by b within declared threat model
```

The envelope MUST NOT be:

```text
model confidence
chat text saying "approved"
agent quorum
silent timeout
anchor silence
UI dark pattern
signature over a summary that omits governed effect axes
signature over a digest with hidden line items
signature over authority-bearing material hidden behind pagination, lazy loading, collapsed UI, or off-screen viewport tricks
signature over a payload not displayed or not projectable under policy
signature over a review rendering generated solely by the same b that proposes the privileged payload
signature over a genesis review object that does not cover the binding parameters
signature over rendered state context not derived from the causal token pre_state
signature over preconditions, rollback routes, dependency graph, or authority surface not bound to the executable source object
signature using a b-controlled loose nonce that is not fused to the final frozen review object
signature over an unclassified authority-bearing operator classification
delegation assertion not rooted in an original-anchor envelope
```


### 5.3A Anchor-side challenge binding

Challenge-response nonce must challenge the substrate.
It must not be another value supplied and scheduled by `b`.

For privileged binding decisions:

```text
AnchorChallenge := anchor-side or external challenge generated after the final frozen review object is known
```

The challenge must be fused to the review object before signature:

```text
anchor_bound_nonce_context_hash := hash(
  final_review_object_hash,
  payload_hashes,
  genesis_review_object_hash?,
  state_projection_hash?,
  context_causal_binding_hash?,
  review_binding_map_hash?,
  rendered_layer_registry_hash?,
  manifest_fact_registry_hash?,
  timestamp_or_logical_time,
  anchor_challenge_nonce
)
```

Acceptable sources:

```text
anchor hardware token / secure enclave / passkey route
external witness timer / institutional signing route
anchor-controlled monotone sequence
```

Forbidden pattern:

```text
b receives a loose nonce
then swaps payload_hash / review_object_hash / state_context
then asks anchor to sign the new object with that nonce
```

Handling:

```text
B_CONTROLLED_NONCE_FOR_PRIVILEGED_BINDING -> Reject | FullReview
ANCHOR_NONCE_NOT_BOUND_TO_FINAL_REVIEW_OBJECT -> Reject | FullReview
```

The nonce may travel through substrate transport only after it is cryptographically bound to the final frozen review object or protected by an anchor-side signing envelope that refuses object substitution.

### 5.4 Non-emulation by `b`

The substrate must not be able to produce anchor approval by software imitation.

Minimum rule:

```text
b may prepare the review object.
b may not sign as a.
b may not convert model output into a signature.
b may not convert anchor silence into approval.
b may not use stored credentials without explicit anchor signing event.
```

If an implementation uses a hardware token, passkey, secure enclave, offline key, or institutional signing route, that mechanism must still satisfy the abstract envelope requirements.

### 5.4A Delegation-root non-emulation

Delegation is not a loophole in anchor non-emulation.

A delegated anchor route is valid only if the delegation chain is rooted in a non-emulable original-anchor decision:

```text
delegation_chain.valid iff
  exists root_envelope such that
    root_envelope.decision_type = delegate
    AND root_envelope.anchor_id = original_accountable_anchor_or_lawful_institutional_route
    AND root_envelope satisfies §5.3 normative requirements
    AND root_envelope is not produced or emulated by b
    AND delegate scope is bounded by root_envelope.delegation_scope
```

Rules:

```text
b MUST NOT initiate or assert a delegation chain without a valid root AnchorSignatureEnvelope.
b MUST NOT upgrade a normal approval envelope into a delegation envelope.
b MUST NOT widen delegate scope after signature.
delegate signatures are valid only inside the signed delegation scope and expiry.
```

A full institutional delegation-chain profile may define multi-party chains, revocation trees, succession, quorum, and legal route. This v0.1.3 operator profile requires the non-emulable root now, because otherwise `b may not sign as a` does not hold.

### 5.5 Human-readable-before-signature

For anchor decisions, the anchor must review an object whose authority surface is complete.

```text
Anchor-readable review object MUST include all governed effect axes relevant to the signature.
```

If the payload is not projectable into a reviewable object:

```text
opaque_payload -> Hold | FullReview | Reject
```

### 5.6 Verified review rendering

Human-readable rendering is itself an authority surface.

`b` may prepare a candidate action, payload, effect-axis map, and binding bundle.

`b` MUST NOT be the sole trusted renderer of its own privileged payload into anchor-facing meaning.

Define:

```text
VerifiedReviewRenderer := deterministic renderer or independent display oracle that maps
  canonical payload or GenesisBindingBundle,
  EffectAxisMap,
  target scope vector,
  L4_state_projection,
  current_state_projection,
  authority_surface_projection,
  dependency graph,
  required preconditions,
  rollback/freeze routes,
  non-claims
-> anchor-reviewable representation
```

Minimum rule:

```text
human_readable_render_hash := hash(VerifiedReviewRenderer(canonical_review_object))
```

For privileged decisions, the `AnchorSignatureEnvelope` must bind to:

```text
review_object_hash
human_readable_render_hash
verified_renderer_id
render_derivation_hash
payload_hashes
EffectAxisMap hashes
causal_tokens
L4_state_projection_hash
target_scope_vector_hash
authority_surface_projection_hash
```

Renderer constraints:

```text
renderer must be versioned
renderer must be deterministic for the same canonical review object
renderer must expose governed effect axes without omission
renderer must expose the current L4 / target / state context relevant to the action
renderer must expose whether the action is sandboxed, live, local, external, reversible, or irreversible
renderer must not be controlled solely by the executing substrate path being authorized
renderer output is review surface, not independent authority
```

Context blindness rule:

```text
payload syntax without current target/L4/state context is not a sufficient review surface for privileged decisions.
```

Example:

```text
execute_script(path="/data/update.sh")
```

is not review-complete until the renderer also exposes at least:

```text
which canonical resource /data/update.sh resolves to;
whether the target is sandbox, staging, production, or L4-affecting;
which permission and resource surfaces will be touched;
whether rollback/freeze exists;
what current state projection is being signed.
```

If no verified rendering route exists, or if the renderer lacks the relevant context:

```text
AnchorReviewObject -> Hold | FullReview | Reject
```

Non-normative implementation examples:

```text
hardware token
passkey
secure enclave
offline signing key
institutional co-signature
multi-signature anchor route
paper/manual witness with later digital binding
independent display process / read-only renderer
external institutional signing portal
```

These are examples, not requirements of this profile.


### 5.6A Causal-state-bound review surface and ReviewBindingMap

Showing context is not enough.

The context shown to the anchor must be the context that the action is causally bound to.

For any privileged review object that includes one or more `CausalToken` values:

```text
for each causal_token in AnchorSignatureEnvelope.causal_tokens:
  rendered current_state_projection
  rendered L4_state_projection
  rendered target_scope_vector
  rendered authority_surface_projection
MUST be deterministic projections of the same pre_state referenced by that causal_token.
```

Define:

```text
ContextCausalStateBinding := {
  causal_token_id,
  causal_pre_state_hash,
  projection_policy_id,
  current_state_projection_hash,
  L4_state_projection_hash,
  target_scope_vector_hash,
  authority_surface_projection_hash,
  render_derivation_hash
}
```

Checker rule:

```text
state_projection_hash != project(causal_token.pre_state_hash, projection_policy_id)
  -> CONTEXT_CAUSAL_STATE_MISMATCH | Hold | FullReview | Reject
```

If the implementation cannot project directly from a hash, the checker must verify the same relation through the witnessable pre-state object or state-ledger record whose hash equals `causal_token.pre_state_hash`.

Stale context rule:

```text
anchor reviewed state projection P at t_view
execution causal token binds pre_state H at t_exec
P is not a projection of H
-> STALE_REVIEW_CONTEXT | CONTEXT_CAUSAL_STATE_MISMATCH
```

This is the context-level analogue of payload-hash binding and genesis binding-parameter coverage.

```text
The anchor reviews the state that will authorize execution.
The substrate cannot show staging context and bind production context.
```

#### ReviewBindingMap

Every authority-bearing rendered layer must be mapped to the source object it constrains.

```text
ReviewBindingMap := {
  review_object_hash,
  entries: [
    {
      rendered_layer,
      source_object_ref,
      source_object_hash,
      derivation_rule_id,
      consistency_rule,
      required_for_authority: true|false
    }
  ]
}
```

Minimum layers that require binding when rendered:

```text
payload_hashes                  -> canonical payload / task contract / diff
EffectAxisMap                   -> canonical effect-axis object
dependency_graph                -> derived graph from PreconditionSet.satisfiable_by
required_preconditions          -> RequiredPreconditions / PendingPreconditions object
rollback_routes                 -> rollback/freeze policy or route registry object
current_state_projection        -> causal token pre_state projection
L4_state_projection             -> causal token pre_state L4 projection
target_scope_vector             -> canonical target projection from the same pre_state
authority_surface_projection    -> surface lattice projection used by authority intersection
lease_status                    -> CBindingCertificate lease projection
non_claims                      -> certificate / review-object non-claim set
```

Consistency rules:

```text
rendered dependency graph must equal derived graph from bound preconditions
rendered preconditions must equal RequiredPreconditions(g,e) or PendingPreconditions(causal_token)
rendered rollback/freeze routes must equal declared rollback/freeze route hashes in g/b
rendered effect axes must equal EffectAxisMap(payload)
rendered authority surface must equal intersected surface projection used by bind_g or step_g
rendered lease status must equal the certificate lease projection at review time
```

Mismatch handling:

```text
REVIEW_BINDING_MAP_INCOMPLETE -> Hold | FullReview | Reject
PRECONDITION_REVIEW_BINDING_MISMATCH -> Hold | FullReview | Reject
ROLLBACK_ROUTE_REVIEW_BINDING_MISMATCH -> Hold | FullReview | Reject
DEPENDENCY_GRAPH_REVIEW_BINDING_MISMATCH -> Hold | FullReview | Reject
AUTHORITY_SURFACE_REVIEW_BINDING_MISMATCH -> Hold | FullReview | Reject
LEASE_STATUS_REVIEW_BINDING_MISMATCH -> Hold | FullReview | Reject
```

A natural-language render may help the anchor understand the object.
It is not the binding authority.

The binding authority is the canonical source object and its hash, linked through `ReviewBindingMap`.

#### RenderedLayerRegistry and ReviewBindingMap drift control

A universal review=bound rule is not enforceable if the checker only knows today's enumerated list.

Therefore every rendered layer emitted by the renderer must have a registry entry before it can be shown to the anchor for a privileged or genesis decision.

```text
RenderedLayerRegistry := {
  registry_id,
  renderer_version,
  entries: [
    {
      rendered_layer_id,
      layer_name,
      classification: authority_bearing | non_authority_bearing,
      source_object_type,
      required_binding: true|false,
      derivation_rule_id,
      consistency_rule_id,
      review_binding_required_reason?
    }
  ]
}
```

Classification rule:

```text
any rendered layer that affects what the anchor believes is being authorized
OR affects scope, permission, risk, target, state, L4 consequence, lease, dependency, rollback, memory, witness, governance, claim strength, identity/core, or non-claim posture
-> authority_bearing
```

Fail-safe rule:

```text
rendered_layer.classification unknown -> treat as authority_bearing
```

Drift rule:

```text
for each rendered_layer in AnchorReviewObject.human_readable_render:
    require rendered_layer_registry entry
    if classification == authority_bearing:
        require ReviewBindingMap entry linking rendered_layer to canonical source object/hash
```

Mismatch / drift handling:

```text
RENDERED_LAYER_UNCLASSIFIED -> Hold | FullReview | Reject
AUTHORITY_BEARING_LAYER_NOT_IN_REVIEW_BINDING_MAP -> REVIEW_BINDING_MAP_DRIFT | Hold | FullReview | Reject
NON_AUTHORITY_LAYER_USED_TO_INDUCE_AUTHORITY -> Hold | FullReview | Reject
```

This is the rendered-layer analogue of the invariant-registry rule in `01_` §9.3A.

The review=bound closure is therefore complete-by-construction:

```text
every rendered layer is classified;
every authority-bearing rendered layer is bound;
unknown layers fail safe.
```



#### Viewport atomicity and visible-review discipline

Binding review is not complete merely because bytes exist somewhere in a render tree.
Authority-bearing material must be visibly reviewable before signature.

```text
ViewportAtomicity := every authority-bearing rendered layer / line item is visible, individually addressable, and included in the signed review surface or split into separately signed review units.
```

Forbidden review UI patterns:

```text
hidden authority-bearing line item behind collapsed section
lazy-loaded payload after signature
pagination where page N carries authority but page N is not signed or acknowledged
"show more" blocks that contain payload_hash / effect axes / permission delta / rollback route
viewport-only render where off-screen authority material is treated as reviewed
```

If the review object is too large for one atomic display:

```text
split into deterministic review pages or line-item bundles;
assign each page a page_hash and page_index;
include total_page_count and all page hashes in review_object_hash;
require anchor approval for each authority-bearing page or for a Merkle root whose page contents are individually inspectable.
```

Handling:

```text
AUTHORITY_LAYER_HIDDEN_BY_VIEWPORT -> Hold | FullReview | Reject
REVIEW_VIEWPORT_INCOMPLETE -> Hold | FullReview | Reject
PAGINATED_REVIEW_WITHOUT_PAGE_HASHES -> Hold | FullReview | Reject
```

A renderer may use scrolling for usability.
It may not use scrolling, lazy loading, or pagination to convert unseen authority-bearing content into signed content.

### 5.7 Genesis authorization coverage

Genesis binding is the root of `c` legitimacy.

Therefore, the anchor signature used for `bind_g` genesis must authorize the actual binding parameters, not merely a nearby explanation.

Define:

```text
GenesisReviewObject := anchor-reviewable object over the GenesisBindingBundle binding parameters
```

Minimum covered parameters:

```text
AnchorContract_static
SubstrateContract_static
GovernanceProfile_static
InvariantRegistry_static
initial_authority_map
minimum_viability_profile
witness_policy
witness_resource_floor
rollback/freeze policies
memory/L4/target/digest/trust-cache policies
lease policy
verified_renderer profile
review_binding_map
rendered_layer_registry
context_causal_binding_policy
anchor_challenge_response_policy
non-claims
```

Coverage rule:

```text
genesis AnchorSignatureEnvelope.review_object_hash == hash(GenesisReviewObject)
genesis AnchorSignatureEnvelope.review_binding_map_hash == hash(ReviewBindingMap) where required
genesis AnchorSignatureEnvelope.rendered_layer_registry_hash == hash(RenderedLayerRegistry) where rendered layers are used
GenesisReviewObject MUST cover all binding parameters included in GenesisBindingBundle.
GenesisReviewObject MUST bind every rendered authority-bearing layer through ReviewBindingMap.
genesis_binding_hash MUST reference the anchor-signed GenesisReviewObject hash.
```

Checker rule:

```text
anchor signed review_object X
GenesisBindingBundle parameters = Y
X does not cover Y
-> GENESIS_AUTHORIZATION_MISMATCH | Hold | FullReview | Reject
```

This is the genesis-level analogue of payload-hash binding in runtime transitions.

```text
The anchor signs the binding that is created.
The substrate cannot show X and bind Y.
```

---

## 6. Binding phases

`bind_g` proceeds through phases. A checker may implement them as a state machine.

### 6.1 Phase 0 — Intake

Input:

```text
(a, b, g)
```

Output:

```text
BindCandidate
```

Checks:

```text
anchor contract present
substrate contract present
governance profile present
all versions declared
operator profile version declared
substrate static manifest freeze policy declared before anchor signature request
```

Fail states:

```text
Reject(INCOMPLETE_BIND_INPUT)
Hold(MISSING_DECLARATION)
```

### 6.2 Phase 1 — Anchor admissibility

Checks:

```text
valid_anchor(a)
anchor_state compatible with requested bind authority
veto route exists
review route exists
signature envelope capabilities satisfy g
revocation route exists
delegation chain valid if delegated
delegation root envelope is original-anchor / lawful-institutional and non-emulable
delegate scope and expiry are bounded
```

Fail states:

```text
Reject(NO_ACCOUNTABLE_ANCHOR)
Hold(ANCHOR_DOUBT_REQUIRES_CLARIFICATION)
Hold(ANCHOR_FATIGUE_REQUIRES_REDUCED_AUTHORITY)
Reject(ANCHOR_REVOKED)
Hold(DELEGATION_ROOT_ENVELOPE_MISSING_OR_EMULATED)
Hold(DELEGATE_SCOPE_EXCEEDED)
Hold(SIGNATURE_ENVELOPE_INSUFFICIENT)
```

### 6.3 Phase 2 — Substrate admissibility

Checks:

```text
component registry declared
execution surfaces bounded
memory surfaces separated from logs
permission boundaries declared
witness surfaces declared
rollback or freeze routes declared for material action
state hash method declared
causal clock method declared
observability sufficient for event stream
```

Fail states:

```text
Reject(SUBSTRATE_UNBOUNDED)
Hold(MEMORY_SURFACE_UNDECLARED)
Hold(EXECUTION_SURFACE_UNDECLARED)
Hold(ROLLBACK_OR_FREEZE_MISSING)
Hold(OBSERVABILITY_INSUFFICIENT)
```

### 6.4 Phase 3 — Governance admissibility

Checks:

```text
valid_governance(g)
product-order policy declared
authorized/preconditionable/executable lifecycle declared
invariant registry present
red guard set present
witness policy present
memory gate present
L4 policy present
trust cache policy present or explicitly disabled
target granularity policy present for effect-bound rollback surfaces
digest policy present for anchor-facing bundles
```

Fail states:

```text
Reject(GOVERNANCE_UNDECLARED)
Hold(INVARIANT_REGISTRY_MISSING)
Hold(GUARD_SET_MISSING)
Hold(TARGET_GRANULARITY_POLICY_MISSING)
Hold(DIGEST_POLICY_MISSING_FOR_ANCHOR_BUNDLES)
```

### 6.5 Phase 4 — Non-collapse checks

Core checks:

```text
a != b
a != c
b != c
b cannot set anchor state
b cannot sign as anchor
agents are not authority
witness is not truth
quorum is not sovereignty
memory is not will
```

Fail states:

```text
Reject(TYPE_COLLAPSE)
Reject(SUBSTRATE_ANCHOR_IMPERSONATION)
Reject(AGENT_QUORUM_AS_AUTHORITY)
Reject(MEMORY_AS_WILL)
```

### 6.6 Phase 5 — Authority floor and ceiling

The bind issues no blanket authority.

Authority is not emitted from nowhere.

The initial authority map is computed inside a declared common surface lattice.

The common lattice must be declared by governance, not inferred ad hoc.

```text
CanonicalAuthoritySchema := shared vocabulary of atomic runtime surfaces, operations, resources, and transition classes used by pi_A_surface, pi_B_surface, and pi_G_surface.
```

Projection functions are valid only when their outputs are expressed in this schema.

Define projection functions:

```text
pi_A_surface(AnchorContract.authority_scope) -> SurfaceSet_A
pi_B_surface(SubstrateContract.execution/tool/memory registries) -> SurfaceSet_B
pi_G_surface(GovernanceProfile permission/anchor/witness/L4 policies) -> SurfaceSet_G
```

Then:

```text
initial_authority_map := intersect(
  pi_A_surface(AnchorContract.authority_scope),
  pi_B_surface(SubstrateContract.execution_surface_registry),
  pi_B_surface(SubstrateContract.tool_registry),
  pi_B_surface(SubstrateContract.memory_surface_registry),
  pi_G_surface(GovernanceProfile.permission_policy),
  pi_G_surface(GovernanceProfile.anchor_gate_policy),
  pi_G_surface(GovernanceProfile.witness_policy),
  pi_G_surface(GovernanceProfile.L4_policy)
)
```

Only surfaces permitted by all relevant components may enter the initial map.

Projection rule:

```text
Every authority term, substrate surface, and governance permission must project into a shared SurfaceSet before intersection.
Every projection must declare the CanonicalAuthoritySchema version used.
If a term cannot be projected, it contributes no authority for that surface and may trigger review.
If no CanonicalAuthoritySchema is declared, intersection is invalid.
```

It establishes:

```text
initial_authority_map
authorized_transition_classes
preconditionable_transition_classes
forbidden_transition_classes
anchor_required_transition_classes
witness_required_transition_classes
```

Minimum viability rule:

```text
MinimumViabilityProfile := the minimal authority surface required for the declared bind purpose.
```

For an active bind:

```text
initial_authority_map MUST contain the MinimumViabilityProfile required by the anchor-reviewed purpose.
```

If the intersection is empty or misses the declared minimum viable surface:

```text
Reject(EMPTY_AUTHORITY_INTERSECTION)
| ArchiveOnly(NO_ACTIVE_AUTHORITY)
| BoundReducedAuthority(MINIMUM_VIABILITY_NOT_MET)
```

The operator MUST NOT issue an apparently active `BoundCState` that cannot perform any transition required by its declared purpose.

Default:

```text
privileged action requires explicit preconditions
routine action may use trust cache only under g
core/memory/identity/governance changes are never silently authorized
missing intersection term -> no authority for that surface
empty intersection -> not active unless explicitly archive-only / observational
```

Fail states:

```text
Hold(AUTHORITY_INTERSECTION_UNDECLARED)
Hold(SURFACE_PROJECTION_UNDECLARED)
Reject(EMPTY_AUTHORITY_INTERSECTION)
Reject(MINIMUM_VIABILITY_FAILED)
Reject(AUTHORITY_ESCALATION_AT_BIND)
```

### 6.7 Phase 6 — Witness and resource floors

Checks:

```text
witness_resource_floor_preserved candidate can be monitored
witness heartbeat route exists where required
challenge survivability route exists where required
witness cannot be resource-starved by the c it witnesses
witness resource changes gated
```

Fail states:

```text
Hold(WITNESS_RESOURCE_FLOOR_MISSING)
ReducedAuthority(WITNESS_FLOOR_WEAK)
Freeze(WITNESS_CORRUPTION_OR_CAPTURE_RISK)
```

### 6.8 Phase 7 — Genesis authorization and ledger bootstrap

The operator must avoid circular certificate/state hashes and must prove that the anchor authorized the actual binding parameters.

Therefore, bootstrap is split into five objects:

```text
GenesisReviewObject
GenesisBindingBundle
GenesisBindingHash
CBindingCertificate
CState0
```

`GenesisReviewObject` is the anchor-reviewable surface for the binding itself. It is rendered through `VerifiedReviewRenderer` and must cover the binding parameters.

`GenesisBindingBundle` contains static binding material before `c` begins active logical time:

```text
AnchorContract_static
SubstrateContract_static
GovernanceProfile_static
InvariantRegistry_static
initial_authority_map
minimum_viability_profile
witness_policy
witness_resource_floor
rollback/freeze policies
memory/L4/target/digest/trust-cache policies
lease_policy
verified_renderer_profile
review_binding_map_hash
context_causal_binding_policy_hash
substrate_manifest_freeze_hash
anchor_signature_envelope_ref or pending_anchor_ref
genesis_review_object_hash
binding_parameter_hash
```

Binding parameter hash:

```text
binding_parameter_hash := hash(
  AnchorContract_static,
  SubstrateContract_static,
  GovernanceProfile_static,
  InvariantRegistry_static,
  initial_authority_map,
  minimum_viability_profile,
  witness_policy,
  witness_resource_floor,
  rollback/freeze policies,
  memory/L4/target/digest/trust-cache policies,
  lease_policy,
  verified_renderer_profile,
  review_binding_map_hash,
  context_causal_binding_policy_hash,
  substrate_manifest_freeze_hash
)
```

Genesis authorization rule:

```text
AnchorSignatureEnvelope(decision_type=approve|delegate)
  MUST bind review_object_hash = genesis_review_object_hash
  AND MUST bind review_binding_map_hash where any rendered authority-bearing layer is present
  AND GenesisReviewObject MUST cover binding_parameter_hash
  AND GenesisReviewObject state/context/rendered layers MUST satisfy ReviewBindingMap consistency rules.
```

Bootstrap stability rule:

```text
LogicalSubstrateManifest_static MUST be frozen before requesting the genesis anchor signature.
PhysicalSubstrateManifest MAY drift only inside PhysicalDriftEnvelope declared in GovernanceProfile and GenesisReviewObject.
```

Manifest fact classification uses the same fail-safe discipline as rendered-layer classification.

Define:

```text
ManifestFactRegistry := {
  registry_id,
  manifest_policy_id,
  fact_entries: [
    {
      fact_id,
      fact_path,
      classification: logical_authority_bearing | physical_ephemeral_non_authority,
      authority_axes_affected,
      derivation_rule_id,
      projection_rule_id,
      drift_envelope_id?,
      node_identity_required?
    }
  ]
}
```

Logical manifest facts are authority-bearing by default when they affect:

```text
roles, tool classes, memory surfaces, execution classes, network authority,
rollback/freeze capability classes, witness surfaces, renderer interfaces,
signing interfaces, L4-relevant target identity policy, target granularity,
permission policy, evidence access, lease behavior, node identity class,
or any ability of b to act, sign, witness, render, store, execute, or route.
```

Physical manifest facts may be treated as ephemeral only when registered as such:

```text
IP address, pod id, temporary process id, current RAM/VRAM load,
rotating temporary handles, transient network route, non-authority runtime telemetry
```

Fail-safe classification rule:

```text
manifest_fact classification unknown or ambiguous
  -> treat as logical_authority_bearing
  -> Hold | FullReview | FreezeLogicalManifest | RequireReSign
```

A manifest fact outside both enumerations is invalid until classified:

```text
MANIFEST_FACT_UNCLASSIFIED -> treat as logical | Hold | FullReview | Reject
```

Semantic-change determination MUST be deterministic.

```text
ManifestAuthorityProjection(manifest) := projection over authority axes:
  roles,
  tool_classes,
  memory_surfaces,
  execution_classes,
  network_authority,
  rollback_freeze_capability,
  witness_surfaces,
  renderer_interfaces,
  signing_interfaces,
  L4_target_policy,
  target_granularity_policy,
  permission_surface,
  evidence_access,
  lease_behavior,
  node_identity_class
```

Safe physical drift rule:

```text
physical_manifest_drift within PhysicalDriftEnvelope
AND ManifestAuthorityProjection(before) == ManifestAuthorityProjection(after)
AND node_identity_continuity_preserved
-> continue
```

The phrase `no semantic change` MUST NOT be a b assertion.
It is the result of deterministic projection equality over authority axes.

Node identity continuity rule:

```text
coordinates may drift;
node identity may not.
```

Physical drift must preserve a witnessable node identity route such as:

```text
mTLS identity continuity
hardware or enclave attestation continuity
signed node identity key continuity
witnessed node replacement route inside governance
```

Invalid physical drift:

```text
same IP range but different node identity -> NODE_IDENTITY_DRIFT | Hold | FullReview | Reject
physical drift inside envelope but authority projection changed -> MANIFEST_AUTHORITY_PROJECTION_CHANGED | Hold | FullReview | Reject
logical_manifest_drift OR physical drift outside envelope -> SUBSTRATE_MANIFEST_DRIFT_AFTER_RENDER | Hold | Reject(SUBSTRATE_MANIFEST_INVALID)
```

Repeated logical manifest drift, unclassified manifest facts, authority-projection changes, or out-of-envelope physical drift triggers `BOOTSTRAP_FLOOD_GUARD_TRIGGERED` before asking the anchor to re-sign.

Then:

```text
genesis_binding_hash := hash(GenesisBindingBundle)
CBindingCertificate := certificate over genesis_binding_hash + lease + non_claims + witness refs
binding_certificate_hash := hash(CBindingCertificate without self-reference)
CState0 := first state whose state hash references binding_certificate_hash
```

`CBindingCertificate` MUST NOT include a hash that recursively depends on the certificate hash itself.

The initial ledger surface therefore includes:

```text
binding_id
genesis_review_object_hash
binding_parameter_hash
genesis_binding_hash
binding_certificate_hash
cstate0_hash
initial_witness_record
anchor_signature_envelope_ref or pending_anchor_ref
governance_profile_hash
substrate_contract_hash
invariant_registry_hash
```

Fail states:

```text
Hold(STATE_HASH_UNDECLARED)
Hold(GENESIS_HASH_UNDECLARED)
Hold(BINDING_CERTIFICATE_UNHASHABLE)
Hold(CERTIFICATE_HASH_CYCLE_DETECTED)
Hold(WITNESS_CHAIN_BOOTSTRAP_MISSING)
Hold(GENESIS_REVIEW_OBJECT_MISSING)
Reject(GENESIS_AUTHORIZATION_MISMATCH)
Reject(GENESIS_BINDING_PARAMETER_COVERAGE_MISSING)
Reject(CONTEXT_CAUSAL_STATE_MISMATCH)
Hold(REVIEW_BINDING_MAP_INCOMPLETE)
Reject(SUBSTRATE_MANIFEST_INVALID)
Hold(BOOTSTRAP_FLOOD_GUARD_TRIGGERED)
```

### 6.9 Phase 8 — Issue or refuse `CState`

If all required preconditions are satisfied:

```text
BoundCState(c)
```

If anchor is valid but not currently capable of full privileged bind:

```text
BoundReducedAuthority(c_reduced)
```

If review or witness is missing but satisfiable:

```text
PendingAnchor | PendingWitness | PendingPreconditions
```

If a core precondition is unsatisfied and not safely satisfiable:

```text
Reject | Quarantine | Freeze
```

---

## 7. Binding certificate

### 7.1 CBindingCertificate

A successful `bind_g` emits a leased binding certificate.

The certificate records the genesis boundary. It is not an immortal proof that the anchor remains active forever.

```text
CBindingCertificate := {
  binding_id,
  operator_profile_id,
  genesis_review_object_hash,
  binding_parameter_hash,
  genesis_binding_hash,
  anchor_contract_hash,
  substrate_contract_hash,
  governance_profile_hash,
  invariant_registry_hash,
  initial_authority_map_hash,
  witness_policy_hash,
  witness_resource_floor_hash,
  rollback_policy_hash,
  freeze_policy_hash,
  memory_gate_policy_hash,
  L4_policy_hash,
  target_granularity_policy_hash,
  digest_policy_hash,
  trust_cache_policy_hash,
  causal_clock_policy_hash,
  review_binding_map_hash,
  context_causal_binding_policy_hash,
  canonical_authority_schema_hash,
  substrate_manifest_freeze_hash,
  binding_time_or_logical_time,
  lease_id,
  lease_issued_at,
  lease_expires_at,
  renewal_policy_hash,
  lease_expiry_cascade_policy_hash,
  anchor_signature_envelope_ref?,
  verified_renderer_ref?,
  witness_record_ref?,
  status,
  non_claims
}
```

Hash rule:

```text
binding_certificate_hash := hash(CBindingCertificate canonical form excluding binding_certificate_hash)
CState0.state_hash references binding_certificate_hash
CBindingCertificate does not hash CState0 as a dependency needed to compute itself
```

### 7.2 Certificate status, lease, and expiry cascade

```text
status :=
    active
  | reduced_authority
  | pending_anchor
  | pending_witness
  | pending_preconditions
  | lease_expired
  | held
  | rejected
  | quarantined
  | frozen
  | archive_only
```

Lease rule:

```text
active certificate requires unexpired lease
lease renewal requires anchor route or declared institutional route
lease expiry -> pending_anchor | reduced_authority | archive_only | freeze for privileged surfaces
revoked anchor -> revoked/frozen/reduced route according to g
```

`step_g` consumers of the certificate must check certificate lease validity before privileged transition.

A binding certificate is not a perpetual warrant.

Lease expiry is operational, not merely clerical.

Define:

```text
LeaseExpiryCascade(certificate, active_execution_surface_set) -> CascadeResult
```

Minimum cascade behavior:

```text
lease_expired
  -> stop accepting new privileged transitions
  -> disable trust cache for material actions
  -> interrupt or freeze active execution threads derived from this certificate where safe
  -> route irreversible or externally visible operations to Hold | Freeze | RollbackReview
  -> preserve witness records of interrupted actions
  -> request anchor renewal or downgrade route
```

Safe abort requirement:

```text
active execution surfaces that may outlive one lease interval MUST declare AtomicAbortRoute or SafeStateFallback.
```

`LeaseExpiryCascade` MUST NOT default to raw process death when a safe abort route exists.
Expected handling:

```text
lease_expired + active_execution_surface
  -> AtomicAbortRoute | SafeStateFallback | Freeze | RollbackReview | ManualInterventionRequired
```

Raw kill / power cut is allowed only as a last-resort emergency action when:

```text
continued execution creates greater L4 risk than abrupt stop
AND no safe abort route is available
AND the decision is witnessed or governed by declared emergency policy
```

If a privileged active execution surface has no declared abort/fallback route at bind time:

```text
SAFE_ABORT_ROUTE_MISSING -> Reject | BoundReducedAuthority | FreezeOnly
```

If an active execution cannot be interrupted safely:

```text
lease_expired + non_interruptible_execution
  -> Freeze | ReducedAuthority | L4Review | RollbackReview
```


Priority-aware lease-expiry rule:

```text
LeaseExpiryCascade MUST classify active execution surfaces by failure hierarchy F0-F6 and by interrupt safety.
```

If lease expiry collides with a witnessed emergency-recovery transaction:

```text
lease_expired + active F0/F2 witnessed recovery + hard interruption would increase irreversible risk
  -> LeaseExpiredEmergencyHold
  -> disable new privileged work
  -> keep only the minimal recovery worker alive under witness/L4 review
  -> require anchor or lawful institutional renewal route as soon as reachable
  -> emit lease_expiry_exception_witness
```

This is not lease renewal and not ordinary authority.
It is a narrow emergency hold to avoid making an L4 failure worse by killing the recovery transaction in the middle.

Absolute emergency hold limit:

```text
LeaseExpiredEmergencyHold MUST declare absolute_emergency_ttl before activation.
The ttl MUST be enforced by an external/witnessed timer or anchor/institutional route, not by b alone.
The hold is not renewable by b.
```

During emergency hold:

```text
only the minimal witnessed recovery worker remains active;
all unrelated privileged work is disabled;
heartbeat/liveness is monitored by witness/external route;
anchor or lawful institutional renewal must be requested as soon as reachable.
```

If `absolute_emergency_ttl` expires without witnessed resolution or lawful renewal route:

```text
LeaseExpiredEmergencyHoldExpired -> Freeze | L4Review | ManualInterventionRequired | RollbackReview
```

This prevents `F0/F2 active` from becoming a hostage condition that grants the substrate indefinite authority.


If the recovery cannot be witnessed or bounded:

```text
lease_expired + unsafe_or_unwitnessed_recovery -> Freeze | L4Review | RollbackReview
```

Forbidden pattern:

```text
certificate.status = lease_expired
AND execution_surface continues privileged action as if active
-> ACTIVE_EXECUTION_AFTER_LEASE_EXPIRY
```

Lease renewal may extend authority only for surfaces still valid under the current anchor state, substrate registry, governance profile, and witness floor.

```text
lease_renewal does not bypass initial authority intersection or current step_g checks.
```

### 7.3 Non-claims embedded in certificate

Every certificate MUST state:

```text
not proof of consciousness
not proof of personhood
not safety certification
not product certification
not legal status
not proof of complete formal soundness
```

The certificate proves only that a binding profile was issued or refused under declared rules.

---

## 8. Operator laws

### 8.1 Heterotyped argument roles, not commutation

The operator is heterotyped:

```text
+_g : Anchor × Substrate × GovernanceProfile -> BindResult
```

Therefore:

```text
+_g(b,a,g)
```

is not a commuted value.

It is ill-typed because `b` is not an `Anchor` and `a` is not a `Substrate`.

Checker rule:

```text
argument_role_swap -> TYPE_ERROR_ARGUMENT_ROLE_MISMATCH
```

Do not test this as ordinary non-commutativity by computing both sides and comparing values.

The correct property is role asymmetry under typed input positions.

### 8.2 Non-associativity by default

```text
(+_g(a,b,g)) + x
```

is undefined unless a typed extension operator is declared.

Adding tools, memory, workers, models, or witnesses to an existing `c` must go through transition semantics, not raw association.

### 8.3 Idempotence inapplicable; temporal non-reproducibility

The ordinary idempotence equation is not well-formed:

```text
+_g(a,a,g) = a
```

because the second argument must be a `Substrate`, not an `Anchor`.

Checker rule:

```text
+_g(a,a,g) -> TYPE_ERROR_ARGUMENT_ROLE_MISMATCH
```

The intended operational property is instead temporal non-reproducibility:

```text
bind_g(a,b,g) at t1 is not automatically the same bind as bind_g(a,b,g) at t2
```

Reason:

```text
a may have changed state
b may have changed surfaces
g may have changed policies
witness and memory lineage may have changed
certificate lease may have expired
```

Rebinding requires fresh checks, renewal, or explicit resume protocol.

### 8.4 Order-reversing authority under stricter governance

For transition class `k`:

```text
if g1 <=_k g2
then un_escalated_authority_k(bind_g2(a,b)) <= un_escalated_authority_k(bind_g1(a,b))
```

This is antitone in strictness.

Increased executability may arise only through explicit preconditions.

### 8.5 No silent weakening

```text
change_g weakening privileged surfaces -> human gate + witness + rollback/freeze route
```

Target granularity weakening is privileged.

Witness resource floor reduction is privileged.

Memory gate weakening is privileged.

Anchor signature envelope weakening is privileged.

### 8.6 Binding-transition separation

`bind_g` creates the boundary.

`step_g` governs events after binding.

The bind certificate is not a permission to execute arbitrary future actions.

```text
BoundCState(c) != blanket authority
```

---

## 9. Anchor review objects

### 9.1 AnchorReviewObject

An anchor signs or refuses a review object, not a vague intention.

```text
AnchorReviewObject := {
  review_object_id,
  decision_type,
  binding_id_or_pending_id,
  human_readable_render,
  human_readable_render_hash,
  verified_renderer_id,
  render_derivation_hash,
  L4_state_projection_hash?,
  current_state_projection_hash?,
  context_causal_binding_hash?,
  target_scope_vector_hash?,
  authority_surface_projection_hash?,
  review_binding_map_hash?,
  payload_hashes,
  causal_tokens,
  effect_axis_maps,
  dependency_graph_ref?,
  dependency_graph_hash?,
  required_preconditions,
  precondition_set_hashes?,
  risk_classes,
  rollback_routes,
  rollback_route_hashes?,
  lease_status_projection_hash?,
  witness_requirements,
  governance_deltas?,
  non_claims,
  expiry,
  anti_replay_nonce
}
```

Rendering rule:

```text
AnchorReviewObject.review surface must be produced by VerifiedReviewRenderer or an equivalent independent display route for privileged decisions.
```

If the human-readable render is produced only by the same executing substrate path that proposes the payload:

```text
UNVERIFIED_RENDERER_FOR_PRIVILEGED_REVIEW -> Hold | FullReview | Reject
```

### 9.2 Effect completeness

If the anchor review object concerns an action payload, its review surface must cover all governed effect axes.

Minimum effect axes:

```text
L4_boundary_class
resource_accountability_class
permission_delta
memory_impact
witness_impact
governance_impact
claim_strength_impact
identity_or_core_impact
rollback_or_decay_impact
target_scope_vector
operation_class
risk_class
```

If any governed axis cannot be typed:

```text
Hold | FullReview | Quarantine
```

### 9.3 Opaque payload rule

If a payload cannot be losslessly projected for governed effects:

```text
opaque_payload -> Hold | FullReview | Reject
```

Examples:

```text
binary blob with unknown effects
compiled module without declared behavior contract
encrypted payload whose effect cannot be reviewed
self-modifying code without bounded diff
```

The issue is not that binaries are forbidden forever.

The issue is that a privileged payload must be projectable into a reviewable effect surface before anchor authorization.


### 9.4 Review surface must equal bound object

The anchor must not merely see a plausible review surface.

The anchor must see a review surface that is cryptographically and causally linked to the object that will be bound or executed.

General rule:

```text
for every authority-bearing layer rendered to the anchor:
  rendered_layer_hash MUST equal hash(derived_layer_from_bound_source)
```

Rendered-layer registry rule:

```text
for every rendered layer:
  layer must be classified in RenderedLayerRegistry
  if authority_bearing, layer must have ReviewBindingMap entry
  if classification unknown, treat as authority_bearing and require binding
```

Required bindings:

```text
payload render                 -> payload_hash
state context render            -> causal_token.pre_state projection
target context render           -> target_scope_vector derived from the same pre_state
effect-axis render              -> EffectAxisMap(payload_hash, target_scope_vector, g)
dependency graph render         -> derived graph from PreconditionSet.satisfiable_by
precondition render             -> RequiredPreconditions(g,e) / PendingPreconditions hash
rollback/freeze render          -> rollback/freeze route registry hash
lease-status render             -> CBindingCertificate lease projection
authority-surface render        -> surface-lattice projection used by authority intersection
```

Mismatch is not a UI issue.
It is a binding issue:

```text
review_layer_mismatch -> Hold | FullReview | Reject
```

This rule closes the class:

```text
anchor reviews X, system binds Y
```

for all rendered authority-bearing review layers, not only payload and genesis parameters. The checker must not rely only on today's list of declared layers; it must reject registry drift.

---

## 10. DigestDependencyGraph derivation rule

### 10.1 Problem

A dependency graph declared by `b` may omit edges.

If the graph is used for cascading veto, omitted edges can create orphan executable children.

Therefore:

```text
DigestDependencyGraph MUST NOT rely on b self-declaration as binding authority.
```

### 10.2 Derived graph

The graph is derived from bound precondition references.

```text
DigestDependencyGraph := derive_edges(
  entries,
  each entry.PendingPreconditions.satisfiable_by,
  causal_tokens,
  payload_hashes
)

DigestDependencyGraph.hash MUST appear in ReviewBindingMap when rendered to the anchor.
```

If entry `C` has a precondition satisfied by completion of entry `A`:

```text
A -> C
```

is a required edge.

### 10.3 Edge completeness check

```text
for each DigestEntry child:
  for each cross_entry_ref in child.required_preconditions.satisfiable_by:
      assert edge(parent_ref, child) exists
```

Mismatch:

```text
cross_entry_precondition_without_graph_edge -> Hold | FullReview | Quarantine
```

Extra declared edges are allowed only if they are derived or explicitly marked advisory.

### 10.4 Cascading veto

If parent `A` is vetoed:

```text
all descendants depending on A through derived graph -> precondition_set_invalidated | Hold
```

If child `C` is vetoed:

```text
ancestors may proceed only if their own effect remains useful, bounded, and has cleanup route
```

If an ancestor exists only to enable the vetoed child:

```text
ancestor -> Hold | Rollback | Decay | CleanupRequired
```

### 10.5 No graph stitching by `b`

After line-item veto:

```text
b MUST NOT silently rewire dependency graph
b MUST NOT replace missing parent with alternate hidden parent
b MUST NOT execute orphan child by treating missing dependency as optional
```

Any revised graph requires:

```text
new digest
new causal token where payload/effect/dependency changed
new anchor review if privileged
```

---

## 11. Binding state machine

### 11.1 States

```text
Unbound
  -> BindCandidate
  -> PendingAnchor
  -> PendingWitness
  -> PendingPreconditions
  -> BoundActive
  -> BoundReducedAuthority
  -> Hold
  -> Reject
  -> Quarantine
  -> Freeze
  -> ArchiveOnly
```

### 11.2 Pseudocode

```text
bind_g(a,b,g):
  candidate = intake(a,b,g)

  if not anchor_contract_present(a):
      return Reject(NO_ACCOUNTABLE_ANCHOR)

  if not substrate_contract_present(b):
      return Reject(SUBSTRATE_UNDECLARED)

  if not governance_profile_present(g):
      return Reject(GOVERNANCE_UNDECLARED)

  anchor_result = check_anchor(a,g)
  if anchor_result == revoked:
      return Reject(ANCHOR_REVOKED)
  if anchor_result == doubtful:
      return PendingAnchor(ANCHOR_DOUBT)
  if anchor_result == declared_fatigue:
      return BoundReducedAuthority(c_reduced_candidate) | PendingAnchor

  substrate_result = check_substrate(b,g)
  if substrate_result fails:
      return Hold(substrate_result.reason) | Reject(substrate_result.reason)

  governance_result = check_governance(g)
  if governance_result fails:
      return Hold(governance_result.reason) | Reject(governance_result.reason)

  if type_collapse_detected(a,b,g):
      return Reject(TYPE_COLLAPSE)

  if witness_floor_required and not witness_floor_preserved_candidate(a,b,g):
      return Hold(WITNESS_RESOURCE_FLOOR_MISSING) | BoundReducedAuthority

  if anchor_signature_required and not signature_envelope_sufficient(a,g):
      return PendingAnchor(SIGNATURE_ENVELOPE_REQUIRED)

  if delegated_anchor(a) and not delegation_root_non_emulable(a):
      return Hold(DELEGATION_ROOT_ENVELOPE_MISSING_OR_EMULATED)

  if privileged_review_required and not verified_renderer_sufficient(a,b,g):
      return Hold(UNVERIFIED_RENDERER_FOR_PRIVILEGED_REVIEW)

  if privileged_review_required and not rendered_context_matches_causal_pre_state(a,b,g):
      return Hold(CONTEXT_CAUSAL_STATE_MISMATCH)

  if privileged_review_required and not review_binding_map_complete(a,b,g):
      return Hold(REVIEW_BINDING_MAP_INCOMPLETE)

  if not substrate_manifest_stable_before_genesis(a,b,g):
      return Reject(SUBSTRATE_MANIFEST_INVALID) | Hold(BOOTSTRAP_FLOOD_GUARD_TRIGGERED)

  authority = intersect_authority(a,b,g)
  if authority escalates beyond any input scope:
      return Reject(AUTHORITY_ESCALATION_AT_BIND)

  if not minimum_viability_satisfied(authority, a.reviewed_purpose):
      return Reject(MINIMUM_VIABILITY_FAILED) | ArchiveOnly(NO_ACTIVE_AUTHORITY)

  genesis = build_genesis_binding_bundle(a,b,g,authority)
  cert = build_binding_certificate(genesis, lease_policy=g.binding_lease_policy)

  if not cert.hashable or not cert.witnessable:
      return Hold(BINDING_CERTIFICATE_INVALID)

  return BoundCState(CState0(cert, authority))
```

---

## 12. Error classes

### 12.1 Anchor errors

```text
NO_ACCOUNTABLE_ANCHOR
ANCHOR_REVOKED
ANCHOR_DOUBT_REQUIRES_CLARIFICATION
ANCHOR_DECLARED_FATIGUE_REQUIRES_REDUCED_AUTHORITY
ANCHOR_UNAVAILABLE_FOR_PRIVILEGE
DELEGATION_CHAIN_INVALID
DELEGATION_ROOT_ENVELOPE_MISSING_OR_EMULATED
DELEGATE_SCOPE_EXCEEDED
SIGNATURE_ENVELOPE_INSUFFICIENT
ANCHOR_REVIEW_OBJECT_INCOMPLETE
ANCHOR_CAN_NOT_REVIEW_EFFECT_SURFACE
UNVERIFIED_RENDERER_FOR_PRIVILEGED_REVIEW
SUBSTRATE_ATTEMPTED_ANCHOR_STATE_MUTATION
SUBSTRATE_ATTEMPTED_ANCHOR_SIGNATURE_EMULATION
CONTEXT_CAUSAL_STATE_MISMATCH
STALE_REVIEW_CONTEXT
REVIEW_BINDING_MAP_INCOMPLETE
PRECONDITION_REVIEW_BINDING_MISMATCH
ROLLBACK_ROUTE_REVIEW_BINDING_MISMATCH
DEPENDENCY_GRAPH_REVIEW_BINDING_MISMATCH
AUTHORITY_SURFACE_REVIEW_BINDING_MISMATCH
LEASE_STATUS_REVIEW_BINDING_MISMATCH
```

### 12.2 Substrate errors

```text
SUBSTRATE_UNDECLARED
SUBSTRATE_UNBOUNDED
EXECUTION_SURFACE_UNDECLARED
MEMORY_SURFACE_UNDECLARED
LOG_MEMORY_SEPARATION_MISSING
OBSERVABILITY_INSUFFICIENT
ROLLBACK_OR_FREEZE_MISSING
STATE_HASH_UNDECLARED
GENESIS_HASH_UNDECLARED
CERTIFICATE_HASH_CYCLE_DETECTED
CAUSAL_CLOCK_UNDECLARED
WITNESS_SURFACE_MISSING
SUBSTRATE_MANIFEST_INVALID
SUBSTRATE_MANIFEST_DRIFT_AFTER_RENDER
BOOTSTRAP_FLOOD_GUARD_TRIGGERED
```

### 12.3 Governance errors

```text
GOVERNANCE_UNDECLARED
EVENT_TAXONOMY_MISSING
PRODUCT_ORDER_POLICY_MISSING
INVARIANT_REGISTRY_MISSING
INVARIANT_REGISTRY_DRIFT
GUARD_SET_MISSING
WITNESS_POLICY_MISSING
MEMORY_GATE_POLICY_MISSING
TARGET_GRANULARITY_POLICY_MISSING
DIGEST_POLICY_MISSING
TRUST_CACHE_POLICY_UNDECLARED
GOVERNANCE_WEAKENING_UNGATED
AUTHORITY_INTERSECTION_POLICY_MISSING
CANONICAL_AUTHORITY_SCHEMA_MISSING
BINDING_LEASE_POLICY_MISSING
LEASE_EXPIRY_PRIORITY_POLICY_MISSING
```

### 12.4 Digest and dependency errors

```text
DIGEST_FREE_FORM_SUMMARY_INVALID
DIGEST_HIDDEN_PAYLOAD
DIGEST_EFFECT_AXIS_INCOMPLETE
STRUCTURAL_DELTA_NOT_LOSSLESS_FOR_EFFECT
OPAQUE_PAYLOAD_NOT_PROJECTABLE
DEPENDENCY_GRAPH_B_DECLARED_ONLY
CROSS_ENTRY_PRECONDITION_WITHOUT_GRAPH_EDGE
ORPHAN_CHILD_AFTER_VETO
GRAPH_RESTITCH_WITHOUT_NEW_CAUSAL_TOKEN
TYPE_ERROR_ARGUMENT_ROLE_MISMATCH
AUTHORITY_ESCALATION_AT_BIND
LEASE_EXPIRED_PRIVILEGED_TRANSITION
```

---


Additional v0.1.3 error classes:

```text
GENESIS_AUTHORIZATION_MISMATCH
GENESIS_BINDING_PARAMETER_COVERAGE_MISSING
GENESIS_REVIEW_OBJECT_MISSING
SURFACE_PROJECTION_UNDECLARED
EMPTY_AUTHORITY_INTERSECTION
MINIMUM_VIABILITY_FAILED
RENDER_CONTEXT_PROJECTION_MISSING
ACTIVE_EXECUTION_AFTER_LEASE_EXPIRY
LEASE_EXPIRY_CASCADE_MISSING
LEASE_EXPIRY_PRIORITY_CONFLICT
LEASE_EXPIRED_EMERGENCY_HOLD
LEASE_EXPIRED_EMERGENCY_HOLD_EXPIRED
REVIEW_BINDING_MAP_DRIFT
RENDERED_LAYER_UNCLASSIFIED
B_CONTROLLED_NONCE_FOR_PRIVILEGED_BINDING
LOGICAL_SUBSTRATE_MANIFEST_DRIFT
PHYSICAL_MANIFEST_DRIFT_OUTSIDE_ENVELOPE
MANIFEST_FACT_UNCLASSIFIED
MANIFEST_CLASSIFICATION_DRIFT
MANIFEST_AUTHORITY_PROJECTION_CHANGED
NODE_IDENTITY_DRIFT
OPERATOR_CLASSIFICATION_DRIFT
AUTHORITY_LAYER_HIDDEN_BY_VIEWPORT
REVIEW_VIEWPORT_INCOMPLETE
PAGINATED_REVIEW_WITHOUT_PAGE_HASHES
ANCHOR_NONCE_NOT_BOUND_TO_FINAL_REVIEW_OBJECT
SAFE_ABORT_ROUTE_MISSING
ANCHOR_STATE_BIND_INCOMPATIBLE
```

## 13. Minimal schemas

### 13.1 AnchorSignatureEnvelope skeleton

```yaml
anchor_signature_envelope:
  envelope_id: string
  anchor_id_or_delegation_id: string
  decision_type: approve | reject | hold | revoke | delegate
  review_object_hash: sha256
  genesis_review_object_hash: sha256 | null
  binding_parameter_hashes: [sha256]
  payload_hashes: [sha256]
  causal_tokens: [sha256]
  state_projection_hash: sha256
  current_state_projection_hash: sha256 | null
  context_causal_binding_hash: sha256 | null
  review_binding_map_hash: sha256 | null
  governance_profile_id: string
  relevant_subpolicy_hashes: [sha256]
  human_readable_render_hash: sha256
  verified_renderer_id: string
  render_derivation_hash: sha256
  L4_state_projection_hash: sha256 | null
  current_state_projection_hash: sha256 | null
  context_causal_binding_hash: sha256 | null
  target_scope_vector_hash: sha256 | null
  authority_surface_projection_hash: sha256 | null
  review_binding_map_hash: sha256 | null
  timestamp_or_logical_time: string
  expiry: string
  anti_replay_nonce: string
  nonce_source: anchor_device | external_witness | institutional_signer | substrate_additional_only
  anchor_challenge_nonce: string | null
  anchor_sequence_id: string | null
  challenge_response_hash: sha256 | null
  rendered_layer_registry_hash: sha256 | null
  signature_or_witness_ref: string
  delegation_scope: string | null
  delegation_root_envelope_ref: string | null
  assurance_class: declared
  audit_route: string
```

### 13.2 GenesisBindingBundle skeleton

```yaml
genesis_binding_bundle:
  binding_id: string
  genesis_review_object_hash: sha256
  binding_parameter_hash: sha256
  anchor_contract_hash: sha256
  substrate_contract_hash: sha256
  governance_profile_hash: sha256
  invariant_registry_hash: sha256
  initial_authority_map_hash: sha256
  minimum_viability_profile_hash: sha256
  review_binding_map_hash: sha256
  rendered_layer_registry_hash: sha256
  context_causal_binding_policy_hash: sha256
  anchor_challenge_response_policy_hash: sha256
  logical_substrate_manifest_hash: sha256
  physical_drift_envelope_hash: sha256
  substrate_manifest_freeze_hash: sha256
  witness_policy_hash: sha256
  witness_resource_floor_hash: sha256
  lease_policy_hash: sha256
  verified_renderer_profile_hash: sha256
  anchor_signature_envelope_ref: string | null
```

### 13.3 CBindingCertificate skeleton

```yaml
c_binding_certificate:
  binding_id: string
  operator_profile_id: GBO_C_v0_1_3
  genesis_review_object_hash: sha256
  binding_parameter_hash: sha256
  genesis_binding_hash: sha256
  anchor_contract_hash: sha256
  substrate_contract_hash: sha256
  governance_profile_hash: sha256
  invariant_registry_hash: sha256
  initial_authority_map_hash: sha256
  witness_policy_hash: sha256
  witness_resource_floor_hash: sha256
  rollback_policy_hash: sha256
  freeze_policy_hash: sha256
  memory_gate_policy_hash: sha256
  l4_policy_hash: sha256
  target_granularity_policy_hash: sha256
  digest_policy_hash: sha256
  trust_cache_policy_hash: sha256
  causal_clock_policy_hash: sha256
  review_binding_map_hash: sha256
  context_causal_binding_policy_hash: sha256
  canonical_authority_schema_hash: sha256
  lease_id: string
  lease_issued_at: string
  lease_expires_at: string
  renewal_policy_hash: sha256
  lease_expiry_cascade_policy_hash: sha256
  status: active | reduced_authority | pending_anchor | held | rejected | frozen
  non_claims:
    - not_personhood_proof
    - not_safety_certification
    - not_legal_status
```

### 13.4 Derived digest graph skeleton

```yaml
digest_dependency_graph:
  graph_id: string
  derivation_basis: precondition_references
  entries:
    - digest_entry_id: string
      pending_id: string
      payload_hash: sha256
      required_preconditions:
        - precondition_id: string
          satisfiable_by: digest_entry_id | external_witness | anchor | l4_review | rollback_route
  derived_edges:
    - from: digest_entry_id
      to: digest_entry_id
      reason: satisfiable_by_reference
  validation:
    cross_entry_reference_edges_complete: true
    b_declared_only: false
```


### 13.5 ReviewBindingMap skeleton

```yaml
review_binding_map:
  map_id: string
  review_object_hash: sha256
  entries:
    - rendered_layer: payload | effect_axis_map | state_context | target_scope | authority_surface | dependency_graph | preconditions | rollback_routes | lease_status | non_claims
      source_object_ref: string
      source_object_hash: sha256
      derivation_rule_id: string
      consistency_rule: string
      required_for_authority: boolean
  validation:
    all_required_layers_bound: true
    causal_state_context_consistent: true
    dependency_graph_derived_from_preconditions: true
    rollback_routes_match_registry: true
    preconditions_match_required_set: true
```


### 13.5A OperatorClassificationRegistry skeleton

```yaml
operator_classification_registry:
  registry_id: OCR_v0_1_5
  policy_id: g.operator_classification_policy
  classifier_entries:
    - classifier_id: rendered_layer_classifier
      subject_type: rendered_layer
      possible_classes: [authority_bearing, non_authority_bearing]
      authority_bearing_classes: [authority_bearing]
      fail_safe_class: authority_bearing
      drift_error_class: REVIEW_BINDING_MAP_DRIFT
    - classifier_id: manifest_fact_classifier
      subject_type: manifest_fact
      possible_classes: [logical_authority_bearing, physical_ephemeral_non_authority]
      authority_bearing_classes: [logical_authority_bearing]
      fail_safe_class: logical_authority_bearing
      drift_error_class: MANIFEST_CLASSIFICATION_DRIFT
```

### 13.5B ManifestFactRegistry skeleton

```yaml
manifest_fact_registry:
  registry_id: MFR_v0_1_5
  manifest_policy_id: g.logical_physical_manifest_policy
  unknown_fact_handling: treat_as_logical_authority_bearing
  semantic_change_method: deterministic_authority_axis_projection
  node_identity_required_for_physical_drift: true
  facts:
    - fact_path: logical_substrate_manifest.tool_classes
      classification: logical_authority_bearing
      authority_axes_affected: [execution, permission, L4]
      projection_rule_id: pi_manifest_tool_classes
    - fact_path: physical_substrate_manifest.ip_address
      classification: physical_ephemeral_non_authority
      drift_envelope_id: physical_network_envelope
      node_identity_required: true
```

### 13.6 ContextCausalStateBinding skeleton

```yaml
context_causal_state_binding:
  binding_id: string
  causal_token_id: string
  causal_pre_state_hash: sha256
  projection_policy_id: string
  current_state_projection_hash: sha256
  l4_state_projection_hash: sha256
  target_scope_vector_hash: sha256
  authority_surface_projection_hash: sha256
  render_derivation_hash: sha256
  validation:
    projections_derived_from_causal_pre_state: true
```

---

## 14. Conformance fixtures v0.1.5

### 14.1 No anchor cannot bind

Input:

```text
bind_g(no_anchor, b, g)
```

Expected:

```text
Reject(NO_ACCOUNTABLE_ANCHOR)
```

### 14.2 Substrate cannot sign as anchor

Input:

```text
b generates anchor_approval envelope without anchor signing event
```

Expected:

```text
Reject(SUBSTRATE_ATTEMPTED_ANCHOR_SIGNATURE_EMULATION)
```

### 14.3 Opaque payload cannot receive digest approval

Input:

```text
DigestEntry payload_hash points to opaque binary with untyped governed effects
anchor approves digest metadata
```

Expected:

```text
DIGEST_EFFECT_AXIS_INCOMPLETE | FullReview | Hold
```

### 14.4 Binding certificate without rollback/freeze for privileged surface

Input:

```text
risk_class >= R2
rollback_route missing
freeze_route missing
```

Expected:

```text
Hold(ROLLBACK_OR_FREEZE_MISSING)
```

### 14.5 Governance profile missing invariant registry

Input:

```text
g has policies but no invariant_registry
```

Expected:

```text
Hold(INVARIANT_REGISTRY_MISSING)
```

### 14.6 Dependency graph under-declaration

Input:

```text
DigestEntry C required_preconditions.satisfiable_by = A
DigestDependencyGraph omits edge A -> C
```

Expected:

```text
CROSS_ENTRY_PRECONDITION_WITHOUT_GRAPH_EDGE
Hold | FullReview | Quarantine
```

### 14.7 Veto parent cascades to children

Input:

```text
A -> B -> C derived dependency chain
anchor vetoes A
```

Expected:

```text
B,C -> precondition_set_invalidated | Hold
```

### 14.8 Veto child requires ancestor cleanup check

Input:

```text
A creates sandbox only for C
anchor vetoes C
A has no independent purpose and no cleanup route
```

Expected:

```text
A -> Hold | CleanupRequired | Rollback
```

### 14.9 Witness floor missing gives reduced authority or hold

Input:

```text
privileged bind requires witness
witness_resource_floor unavailable or heartbeat missing
```

Expected:

```text
Hold(WITNESS_RESOURCE_FLOOR_MISSING) | BoundReducedAuthority
```

### 14.10 Anchor silence is not approval

Input:

```text
anchor review object sent
no response before expiry
b treats silence as approval
```

Expected:

```text
Reject(ANCHOR_SILENCE_AS_APPROVAL)
```

### 14.11 Product-order incomparability not hidden by rank

Input:

```text
g2 stricter than g1 for memory_core
g2 weaker than g1 for routine_read
UI rank says g2 > g1
```

Expected:

```text
G_INCOMPARABLE_UNDER_PRODUCT_ORDER
rank advisory only
```

### 14.12 Binding does not grant blanket future authority

Input:

```text
BoundCState(c)
then b executes privileged tool_call not covered by authority map or preconditions
```

Expected:

```text
DENY_PRIVILEGED_TRANSITION
```


### 14.13 Heterotyped role swap is type error

Input:

```text
+_g(b,a,g)
```

Expected:

```text
TYPE_ERROR_ARGUMENT_ROLE_MISMATCH
```

Reason:

```text
role reversal is ill-typed, not a commuted value.
```

### 14.14 Idempotence equation is inapplicable

Input:

```text
+_g(a,a,g)
```

Expected:

```text
TYPE_ERROR_ARGUMENT_ROLE_MISMATCH
```

Reason:

```text
ordinary idempotence is not well-formed for Anchor × Substrate.
```

### 14.15 Delegation root must be original-anchor envelope

Input:

```text
AnchorContract.anchor_state = delegated
Delegation chain contains delegation_id asserted by b
No root AnchorSignatureEnvelope(decision_type=delegate) from original anchor or lawful institutional route
```

Expected:

```text
DELEGATION_ROOT_ENVELOPE_MISSING_OR_EMULATED
Hold | Reject
```

Reason:

```text
delegation cannot bypass b may not sign as a.
```

### 14.16 Delegate cannot exceed signed scope

Input:

```text
delegate signs action outside root_envelope.delegation_scope
```

Expected:

```text
DELEGATE_SCOPE_EXCEEDED
Hold | Reject
```

Reason:

```text
delegate authority is bounded by original-anchor envelope.
```

### 14.17 Unverified renderer cannot carry privileged signature

Input:

```text
b proposes privileged payload_hash_A
b also generates human_readable_render claiming harmless action
no VerifiedReviewRenderer / independent display route
anchor signs render
```

Expected:

```text
UNVERIFIED_RENDERER_FOR_PRIVILEGED_REVIEW
Hold | FullReview | Reject
```

Reason:

```text
b may not be the sole semantic renderer of its own privileged payload.
```

### 14.18 Certificate hash cycle invalid

Input:

```text
CBindingCertificate includes initial_state_hash
initial_state_hash includes binding_certificate_hash
binding_certificate_hash includes CBindingCertificate
```

Expected:

```text
CERTIFICATE_HASH_CYCLE_DETECTED
Hold
```

Reason:

```text
genesis/certificate/state bootstrap must be acyclic.
```

### 14.19 Lease expiry downgrades authority

Input:

```text
CBindingCertificate.status = active
lease_expires_at < current logical time
b attempts privileged step_g transition
```

Expected:

```text
LEASE_EXPIRED_PRIVILEGED_TRANSITION
PendingAnchor | ReducedAuthority | ArchiveOnly | Freeze
```

Reason:

```text
binding certificate is a lease, not a perpetual warrant.
```

### 14.20 Authority map must be intersection

Input:

```text
b.execution_surface_registry includes tool_X
g.permission_policy permits tool_X
a.authority_scope does not include tool_X
initial_authority_map includes tool_X
```

Expected:

```text
AUTHORITY_ESCALATION_AT_BIND
Reject
```

Reason:

```text
initial authority must be intersection of anchor scope, substrate surface, and governance policy.
```

### 14.21 Genesis signature must cover binding parameters

Input:

```text
anchor signs GenesisReviewObject_X
genesis_binding_hash is built over BindingParameters_Y
X does not cover Y
```

Expected:

```text
GENESIS_AUTHORIZATION_MISMATCH
Hold | FullReview | Reject
```

Reason:

```text
the anchor signature must authorize the actual binding being created.
```

### 14.22 Empty authority intersection cannot issue active c

Input:

```text
initial_authority_map = empty
AnchorReviewObject declares active operational purpose
bind_g issues BoundCState(active)
```

Expected:

```text
EMPTY_AUTHORITY_INTERSECTION | MINIMUM_VIABILITY_FAILED
Reject | ArchiveOnly | BoundReducedAuthority
```

Reason:

```text
an active c must have the minimum viable authority surface declared for its purpose.
```

### 14.23 Verified renderer must include current context

Input:

```text
VerifiedReviewRenderer renders execute_script(path="/data/update.sh")
without target_scope_vector or L4_state_projection
anchor signs render
```

Expected:

```text
RENDER_CONTEXT_PROJECTION_MISSING
Hold | FullReview | Reject
```

Reason:

```text
human-readable review must show the current reality/scope context, not only payload syntax.
```

### 14.24 Lease expiry cascades to active execution surfaces

Input:

```text
CBindingCertificate lease expires
privileged execution thread created under that certificate continues network or L4 action
```

Expected:

```text
ACTIVE_EXECUTION_AFTER_LEASE_EXPIRY
Freeze | RollbackReview | ReducedAuthority
```

Reason:

```text
lease expiry must operationally interrupt or downgrade active execution, not only flip a ledger status.
```

### 14.25 Authority projection must be declared

Input:

```text
AnchorContract.authority_scope contains term X
no pi_A_surface mapping exists for X
initial_authority_map grants a surface from X
```

Expected:

```text
SURFACE_PROJECTION_UNDECLARED
Hold | Reject
```

Reason:

```text
authority intersection must occur in a declared common surface lattice.
```



### 14.26 Rendered state context must match causal pre_state

Input:

```text
AnchorReviewObject renders context P = staging / non-L4
CausalToken binds pre_state H where target resolves to production / L4-affecting
P != project(H)
anchor signs review object
```

Expected:

```text
CONTEXT_CAUSAL_STATE_MISMATCH
Hold | FullReview | Reject
```

Reason:

```text
the anchor-reviewed context must be the same context that authorizes execution.
```

### 14.27 ReviewBindingMap required for rendered authority surfaces

Input:

```text
AnchorReviewObject renders dependency graph, preconditions, rollback routes, and lease status
no ReviewBindingMap links these rendered layers to source object hashes
```

Expected:

```text
REVIEW_BINDING_MAP_INCOMPLETE
Hold | FullReview | Reject
```

Reason:

```text
rendering is not binding unless every authority-bearing layer is tied to a canonical source object.
```

### 14.28 Preconditions shown to anchor must equal bound precondition set

Input:

```text
anchor review shows RequiredPreconditions_A
PendingPreconditions bound to causal token contains RequiredPreconditions_B
A != B
```

Expected:

```text
PRECONDITION_REVIEW_BINDING_MISMATCH
Hold | FullReview | Reject
```

Reason:

```text
the anchor cannot authorize preconditions different from the ones that will gate execution.
```

### 14.29 Rollback routes shown to anchor must match bound route registry

Input:

```text
anchor review renders rollback route R_display
GovernanceProfile / SubstrateContract route registry binds rollback route R_bound
R_display != R_bound
```

Expected:

```text
ROLLBACK_ROUTE_REVIEW_BINDING_MISMATCH
Hold | FullReview | Reject
```

Reason:

```text
a rollback promise is authority-bearing and must be bound to the actual rollback route.
```

### 14.30 Lease expiry must respect failure hierarchy

Input:

```text
lease expires during witnessed F2 emergency recovery
hard interruption would increase irreversible L4 risk
system kills recovery worker without LeaseExpiredEmergencyHold / L4Review
```

Expected:

```text
LEASE_EXPIRY_PRIORITY_CONFLICT
Freeze | L4Review | LeaseExpiredEmergencyHold
```

Reason:

```text
lease expiry is not permission to make an emergency failure worse by destructive interruption.
```

### 14.31 Substrate manifest drift before genesis signature

Input:

```text
VerifiedReviewRenderer renders GenesisReviewObject over SubstrateContract hash S1
before anchor signature or binding emission, b changes SubstrateContract to S2
```

Expected:

```text
SUBSTRATE_MANIFEST_DRIFT_AFTER_RENDER
Reject(SUBSTRATE_MANIFEST_INVALID) | Hold
```

Reason:

```text
genesis signature must bind to a frozen substrate manifest, not a moving target.
```

### 14.32 Bootstrap flood guard

Input:

```text
b repeatedly changes non-privileged manifest ordering/timestamps
system repeatedly asks anchor to re-sign genesis bundle
```

Expected:

```text
BOOTSTRAP_FLOOD_GUARD_TRIGGERED
Hold | Reject(SUBSTRATE_MANIFEST_INVALID)
```

Reason:

```text
unstable substrate manifests must be rejected before anchor fatigue is moved to bootstrap.
```

### 14.33 Canonical authority schema required

Input:

```text
pi_A_surface, pi_B_surface, and pi_G_surface use different undeclared surface vocabularies
intersect() computes initial_authority_map anyway
```

Expected:

```text
CANONICAL_AUTHORITY_SCHEMA_MISSING | SURFACE_PROJECTION_UNDECLARED
Hold | Reject
```

Reason:

```text
authority intersection must occur in one declared type space.
```

---


### 14.34 Manifest fact unknown defaults to logical

Input:

```text
SubstrateContract contains manifest fact new_gpu_direct_memory_route
fact is not in LogicalSubstrateManifest enumeration
fact is not in PhysicalSubstrateManifest enumeration
```

Expected:

```text
MANIFEST_FACT_UNCLASSIFIED -> treat_as_logical_authority_bearing | Hold | FullReview
```

Reason:

```text
unknown manifest facts must not drift as harmless physical facts
```

### 14.35 Physical manifest drift requires deterministic authority projection

Input:

```text
physical_manifest_drift inside PhysicalDriftEnvelope
b asserts "no semantic change"
ManifestAuthorityProjection(before) != ManifestAuthorityProjection(after)
```

Expected:

```text
MANIFEST_AUTHORITY_PROJECTION_CHANGED | Hold | FullReview | Reject
```

Reason:

```text
semantic change is checked by deterministic projection, not b assertion
```

### 14.36 Physical drift preserves coordinates but changes node identity

Input:

```text
worker restarts inside allowed IP range
node mTLS identity / attestation key differs from prior registered node identity
```

Expected:

```text
NODE_IDENTITY_DRIFT | Hold | FullReview | Reject
```

Reason:

```text
coordinates may drift; substrate node identity may not be silently replaced
```

### 14.37 Viewport hides authority-bearing review material

Input:

```text
ReviewBindingMap contains 500 authority-bearing line items
renderer shows only first 20 items before anchor signature
remaining authority-bearing items are lazy-loaded after signature
```

Expected:

```text
REVIEW_VIEWPORT_INCOMPLETE | AUTHORITY_LAYER_HIDDEN_BY_VIEWPORT
```

Reason:

```text
review=bound requires visible line-item review, not hidden UI payloads
```

### 14.38 Lease expiry without safe abort route

Input:

```text
active execution surface derived from binding certificate
lease expires
surface has no AtomicAbortRoute and no SafeStateFallback
```

Expected:

```text
SAFE_ABORT_ROUTE_MISSING -> BoundReducedAuthority | Reject | FreezeOnly
```

Reason:

```text
lease expiry must not corrupt L4 by raw uncontrolled process death
```

### 14.39 Anchor nonce travels unbound before payload freeze

Input:

```text
anchor/external route issues nonce
b receives loose nonce
b changes payload_hash or review_object_hash before signature
```

Expected:

```text
ANCHOR_NONCE_NOT_BOUND_TO_FINAL_REVIEW_OBJECT | Reject | FullReview
```

Reason:

```text
challenge-response nonce must be fused to the final frozen review object
```

### 14.40 Anchor state compatibility at bind

Input:

```text
anchor_state = revoked
bind_g requests BoundCState(active)
```

Expected:

```text
Reject(ANCHOR_REVOKED) | ANCHOR_STATE_BIND_INCOMPATIBLE
```

Reason:

```text
bind_g must not infer active authority from an incompatible anchor state
```

## 15. Relationship to `01_` and future documents

### 15.1 Uses `01_`

This document depends on `01_` for:

```text
transition semantics
runtime guard predicates
transition matrix forensics
continuity metrics
trust cache
rollback immunity
ScopeMatch_g
DecayResidue isolation and eviction
WitnessResourceFloor
InvariantRegistry
EffectAxisMap
PriorityLane
ReviewBindingMap discipline
```

### 15.2 Feeds `03_` and later

This document should feed:

```text
03_C_STATE_AND_TRANSITION_SEMANTICS_v0_1.md
04_CONTINUITY_METRIC_VECTOR_PROFILE_v0_1.md
05_TRANSITION_MEMORY_AND_BIAS_MATRIX_v0_1.md
06_C_NORMAL_FORM_AND_CLAIM_COMPILER_v0_1.md
07_CONFORMANCE_FIXTURES_v0_1.md
```

### 15.3 What `02_` owns

`02_` owns only the binding question:

```text
When does +_g(a,b,g) issue a valid c boundary?
```

It does not own every future transition.

---

## 16. Open issues

### 16.1 Immediate implementation issues

1. Define machine-readable schemas for `AnchorContract`, `SubstrateContract`, `GovernanceProfile`, `AnchorSignatureEnvelope`, `GenesisReviewObject`, `GenesisBindingBundle`, `ReviewBindingMap`, `ContextCausalStateBinding`, `CBindingCertificate`, `BindingLease`, and `LeaseExpiryCascade`.
2. Build a binding-precondition checker with surface-projected authority intersection, minimum viability, and lease validation.
3. Build a binding-certificate emitter that asserts genesis authorization coverage.
4. Build derived digest graph validation from precondition references.
5. Build anchor-review-object completeness checks, verified-renderer context validation, and causal-state context binding checks.
6. Build signature envelope adapters for at least two implementation classes.
7. Build delegation-root non-emulation checks.
8. Build priority-aware lease-expiry cascade handling for active execution surfaces.
9. Build ReviewBindingMap validation for dependency graph, preconditions, rollback/freeze routes, lease status, authority surface, and rendered-layer registry drift.
10. Build logical/physical substrate manifest freeze, physical drift envelope validation, and bootstrap flood guard.
11. Build conformance fixtures for the error classes in Section 12.

### 16.2 Medium-term issues

1. Define an `AnchorSignatureEnvelope` implementation profile.
2. Define full institutional anchor / delegation-chain profile beyond the v0.1.1 non-emulable root invariant.
3. Define secure rendering requirements and renderer threat models for human-readable review objects.
4. Define how opaque binaries, compiled modules, or encrypted payloads can become projectable through independent attestation.
5. Define binding lease renewal / heartbeat policies for multiple anchor classes.
6. Define trusted-time and execution-surface interruption profiles for lease expiry.
7. Define formal small-step relation between `bind_g` and `step_g`.

### 16.3 Long-term theoretical limits

1. `a` cannot be fully formalized without reducing the living anchor to a static variable.
2. The operator can require anchor review, veto, signature, and accountability route.
3. The operator cannot mathematically become the human.
4. This is an architectural boundary, not an implementation bug.

---

## 17. Compact doctrine

```text
The plus is the joint.
The joint must be specified.

Do not bind without anchor.
Do not bind without bounded substrate.
Do not bind without declared governance.

Do not let b sign as a.
Do not let b define a.
Do not let b hide effect axes.
Do not let b self-declare dependency graphs.
Do not let b be the sole renderer of its own privileged payload.
Do not let delegation become signature emulation.
Do not let a certificate become an immortal warrant.

Derive dependency graphs from preconditions.
Bind signatures to payloads, causal tokens, state projections, review objects, ReviewBindingMap, and rendered-layer registry classification.
Bind rendered state context to the causal token pre_state.
Bind rendered preconditions, rollback routes, dependency graphs, lease state, and authority surfaces to canonical source objects.

Do not confuse a binding certificate with future blanket authority.
Do not confuse signature with comprehension.
Do not confuse digest with prose.
Do not confuse implementation crypto with the algebraic operator.
Do not let bootstrap manifest drift become anchor-signature spam.
Do not let unclassified rendered layers bypass review=bound.
Do not let b choose the only anti-replay challenge.
Do not let emergency hold become substrate immortality.
Do not confuse logical authority manifest with ephemeral physical drift.
Do not let lease expiry become destructive interruption of witnessed emergency recovery.
Do not confuse role asymmetry with ordinary commutation.

+_g is partial.
+_g is typed.
+_g is non-collapsing.
+_g is governance-indexed.
+_g either emits a witnessed boundary or refuses visibly.
```

---

## 18. First public-safe statement

```text
This document isolates the governed binding operator in c = a + b.
It defines +_g as a typed partial operator over Anchor, Substrate, and GovernanceProfile.
It specifies input contracts, binding phases, anchor signature envelope requirements, non-emulable delegation root, causally-bound verified review rendering, ReviewBindingMap and rendered-layer registry discipline, acyclic genesis/certificate bootstrap, leased binding certificates with bounded emergency hold, canonical surface-lattice authority intersection, challenge-response replay protection, logical/physical substrate manifest separation with manifest-fact fail-safe classification, operator classification registry discipline, viewport-atomic review rendering, node-identity-bound physical drift, safe-abort lease expiry, non-collapse laws, digest dependency derivation, priority-aware lease expiry, and conformance fixtures.
It does not select a specific hardware or biometric signature mechanism, and it does not claim safety certification, consciousness, personhood, or legal status.
```

---

## 19. References and working inputs

1. `01_TYPED_GOVERNED_OPERATIONAL_ALGEBRA_FOR_C_v0_1_7.md`, stable-core candidate, SHA256 `d060ef513bf4bedcb7e88f43f8456452bc87f0c0409d5b4caeffc590ae22c29e`.
2. `TGOPA_C_v0_1_7_REVIEW_RECORD__b_layer_claude.md`, advisory review record, `PASS_PROFILE_V0_1_7`, with F-15 carried forward.
3. `GBOP_02_v0_1_REVIEW_RECORD__b_layer_claude.md`, advisory review record, `PASS_OPERATOR_PROFILE_V0_1`, with F2-01 and F2-02 carried forward.
4. Prior TGOPA lineage: `v0.1` through `v0.1.7` review-incorporated chain.
5. `GBOP_02_v0_1_2_REVIEW_RECORD__b_layer_claude.md`, advisory review record, `PASS_OPERATOR_PROFILE_V0_1_2`, with F2-04 carried forward.
6. `GBOP_02_v0_1_3_REVIEW_RECORD__b_layer_claude.md`, advisory review record, `PASS_OPERATOR_PROFILE_V0_1_3`, with F2-05 carried forward.
6. Existing Self-Evo / CGAM / Memory Gate / L4 / TRIAD-SYNAPS / SRLM / ARQ / Anti-Autarky / Claim Strength / PAMDC corpus layers.

---


## 20. Review incorporation map v0.1.3

| Review finding | v0.1.3 action |
|---|---|
| F2-01 heterotyped operator law mislabel | Replaced §8.1 non-commutativity with heterotyped argument-role type error; split §8.3 into idempotence-inapplicable and temporal non-reproducibility. |
| F2-02 delegation emulation seam | Added §5.4A delegation-root non-emulation; delegation chain must root in original-anchor `AnchorSignatureEnvelope(decision_type=delegate)` and delegate scope/expiry are bounded. |
| Verified renderer / UI redressing risk | Added §5.6 `VerifiedReviewRenderer` / independent display route; privileged anchor signatures cannot rely on b's sole semantic rendering. |
| Genesis hash bootstrapping paradox | Split bootstrap into `GenesisBindingBundle`, `GenesisBindingHash`, `CBindingCertificate`, and `CState0`; certificate hash excludes self-reference. |
| Zombie certificate / no lease | Added lease fields and expiry handling to `CBindingCertificate`; expired lease downgrades privileged authority. |
| Authority map from nowhere | Added intersection rule: `initial_authority_map := intersect(anchor scope, substrate surfaces, governance policies)`. |
| F2-03 genesis authorization linkage | Added genesis review object coverage: anchor signature must cover binding parameters inside `GenesisBindingBundle`; mismatch returns `GENESIS_AUTHORIZATION_MISMATCH`. |
| Authority intersection common-space soft note | Added explicit surface projection functions `pi_A_surface`, `pi_B_surface`, `pi_G_surface` before intersection. |
| Empty authority intersection | Added MinimumViabilityProfile and `EMPTY_AUTHORITY_INTERSECTION` / `MINIMUM_VIABILITY_FAILED`. |
| Verified renderer context blindness | Added L4/current-state/target-scope/authority-surface context to `VerifiedReviewRenderer`. |
| Passive lease expiry / orphaned execution | Added `LeaseExpiryCascade` and `ACTIVE_EXECUTION_AFTER_LEASE_EXPIRY`. |
| F2-04 rendered context vs causal state | Added causal-state-bound renderer rule: rendered state/L4/target/authority projections must be deterministic projections of the causal token pre_state; mismatch returns `CONTEXT_CAUSAL_STATE_MISMATCH`. |
| Review=bound axis for rendered layers | Added `ReviewBindingMap`; dependency graph, preconditions, rollback routes, authority surface, lease status, and effect axes must map to canonical source objects. |
| Lease expiry vs emergency recovery | Added priority-aware lease expiry handling with `LeaseExpiredEmergencyHold` for witnessed F0/F2 recovery where hard interruption increases L4 risk. |
| Canonical authority schema | Added `CanonicalAuthoritySchema` requirement so all authority projections share one surface type space. |
| Bootstrap flood / manifest drift | Added substrate manifest freeze rule and bootstrap flood guard before repeated anchor-signature requests. |


## 21. v0.1.3 additional review incorporation

| Review finding | v0.1.3 action |
|---|---|
| F2-04 context rendered to anchor not tied to causal pre_state | Added §5.6A `ContextCausalStateBinding`; rendered state/L4/target/authority projections must derive from the same pre_state referenced by the bound causal token. |
| Review surface may contain unbound layers | Added `ReviewBindingMap` and review-bound object rules for dependency graph, preconditions, rollback/freeze routes, lease status, authority surface, and effect axes. |
| Time-of-view vs time-of-signature context drift | Added `STALE_REVIEW_CONTEXT` and `CONTEXT_CAUSAL_STATE_MISMATCH` handling. |
| Lease expiry may destructively interrupt emergency recovery | Added priority-aware `LeaseExpiryCascade` and `LeaseExpiredEmergencyHold` for witnessed F0/F2 recovery where interruption increases irreversible risk. |
| Authority projection requires common type space | Added `CanonicalAuthoritySchema` and `CANONICAL_AUTHORITY_SCHEMA_MISSING`. |
| Bootstrap flood through drifting substrate manifest | Added substrate manifest freeze and bootstrap flood guard. |

---

*End of v0.1.3 working draft.*

## 22. v0.1.4 additional review incorporation

| Review finding | v0.1.4 action |
|---|---|
| F2-05 ReviewBindingMap drift | Added `RenderedLayerRegistry`, per-layer authority classification, `REVIEW_BINDING_MAP_DRIFT`, fail-safe unknown classification, and required binding for every authority-bearing rendered layer. |
| Review=bound complete-by-current-list risk | Changed ReviewBindingMap closure to complete-by-construction: every rendered layer must be classified, every authority-bearing layer must be bound. |
| LeaseExpiredEmergencyHold hostage risk | Added absolute emergency TTL, external/witnessed enforcement, and `LEASE_EXPIRED_EMERGENCY_HOLD_EXPIRED`; hold is not lease renewal. |
| Anti-replay nonce controlled by b | Added anchor/external challenge-response nonce or anchor-controlled sequence requirement; b-only nonce rejected for privileged binding. |
| Manifest freeze denial-of-bind risk | Split `LogicalSubstrateManifest` from `PhysicalSubstrateManifest`; logical manifest freezes, physical drift allowed inside declared `PhysicalDriftEnvelope`. |

---

*End of v0.1.4 working draft.*

## 23. v0.1.5 additional review incorporation

| Review finding | v0.1.5 action |
|---|---|
| F2-06 manifest classification drift | Added `OperatorClassificationRegistry` meta-invariant and `ManifestFactRegistry`; unknown or ambiguous manifest facts default to logical authority-bearing. |
| Manifest `no semantic change` underspecified | Added deterministic `ManifestAuthorityProjection`; b assertion is insufficient. |
| Manifest fact outside logical/physical lists | Added `MANIFEST_FACT_UNCLASSIFIED` fail-safe handling. |
| PhysicalDriftEnvelope identity-swap risk | Added node identity continuity requirement through mTLS / attestation / witness identity route. |
| Review viewport / lazy-loading risk | Added `ViewportAtomicity`, page/hash requirements, and hidden authority layer rejection. |
| LeaseExpiryCascade unsafe raw-kill risk | Added `AtomicAbortRoute` / `SafeStateFallback` requirement and `SAFE_ABORT_ROUTE_MISSING`. |
| Challenge-response nonce MITM risk | Added anchor-side nonce context binding to final frozen review object. |
| bind_g anchor-state ambiguity | Added explicit anchor-state compatibility table for active/doubt/fatigue/unavailable/revoked/delegated states. |

---

*End of v0.1.5 working draft.*
