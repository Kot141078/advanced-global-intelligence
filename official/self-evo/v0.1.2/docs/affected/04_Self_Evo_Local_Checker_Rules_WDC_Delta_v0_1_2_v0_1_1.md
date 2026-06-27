# 04 Self-Evo Local Checker Rules WDC Delta v0.1.2

## Deterministic WDC checker-rule delta for `SELF-EVO-04` under the `SELF_EVO_v0_1_2_PATCH_INDEX`

**Status:** Draft delta profile v0.1.2 / append-first corrected draft revision v0.1.1; not a released v0.1.2 package  
**Date:** 2026-06-27  
**Document ID:** `04_Self_Evo_Local_Checker_Rules_WDC_Delta_v0_1_2_v0_1_1`  
**Short name:** `SELC-WDC-DELTA v0.1.2 / draft rev v0.1.1`  
**Target parent:** `04_Self_Evo_Local_Checker_Rules_v0_1_1.md` (`SELC v0.1.1`)  
**Depends on:** `03_Self_Evo_Proposal_Packet_Schema_WDC_Delta_v0_1_2_v0_1_1.md` (`SEPKT-WDC-DELTA v0.1.1`, review result `PASS`)  
**Patch driver:** `SELF_EVO_v0_1_2_PATCH_INDEX_v0_1_1.md` (`PASS` at review level)  
**Document class:** deterministic semantic-checker delta / WDC rule table / result-aggregation profile  
**Assertion class:** `C-A10` control-layer artifact; `C-A7` where witness, hash, or review-record claims are made  
**Primary subject:** `witness_dependency_impact` checks for Self-Evo proposal packets  
**Primary boundary:** this delta makes Witness Dependency Capture machine-checkable. It does not approve growth, integrate changes, write memory, authorize witness-resource changes, or release `v0.1.2`.

**v0.1.1 correction note:** this append-first revision closes `SELC-WDC-DELTA-REV-F1` from `SELC_WDC_DELTA_REVIEW_RECORD_v0_1` by declaring §9/§11 the canonical WDC annotation and severity vocabulary, adding an explicit cross-document crosswalk from older `03` / patch-index terms to the canonical `04` terms, and adding a harmonization item for the already accepted `03` delta, the patch index, and the future `08` fixture pack. No WDC rule result, predicate, gate behavior, red line, pass state, or non-authority boundary is changed.

---

## 0. Executive definition

This document adds a WDC-specific rule family to `SELF-EVO-04`:

```text
WDC-LC-001..006
```

The rule family checks whether a proposal packet that may affect witness independence has declared and handled its `witness_dependency_impact` correctly.

The central rule is:

```text
A witness that cannot survive saying "no" is not independent.
```

The checker version is:

```text
A proposal that may affect witness capacity must not pass as an ordinary optimization.
```

The WDC checker does four things:

```text
1. detects whether the packet may affect witness capacity;
2. requires a witness_dependency_impact block when WDC is relevant;
3. checks WRCG, WRF, CST, human-review, and sole-approver conditions;
4. emits one canonical checker result per WDC rule, with severity and annotations separated.
```

It never decides that the change is safe.

It can only emit evidence for routing:

```text
FAIL
HUMAN_GATE
WARNING
PASS_WITH_GATES
PASS
```

---

## 1. Non-goals

This delta does not:

1. replace `SELF-EVO-04`;
2. replace `SELF-EVO-03`;
3. replace `SELF-EVO-05` TRIAD witness review;
4. replace `SELF-EVO-07` Anti-Autarky / Resource Gate;
5. replace `SELF-EVO-08` fixtures;
6. decide the correct numerical Witness Resource Floor;
7. authorize changes to witness compute, storage, routing, budget, continuity, artifact access, or update path;
8. make a sister witness final judge;
9. make a local checker an authority actor;
10. permit `c` to approve its own witness-resource changes;
11. convert checker `PASS` into deployment permission;
12. convert checker `PASS_WITH_GATES` into approval;
13. mutate the DOI-bound Self-Evo v0.1.1 package;
14. release Self-Evo v0.1.2.

A checker may block or route.

A checker may not authorize growth.

---

## 2. Source basis

This file is an append-first delta. It binds the relevant baseline and driver artifacts but does not mutate them.

| Artifact | Role | Status | SHA-256 / identifier |
|---|---|---|---|
| Self-Evo Document Package v0.1.1 | published baseline | DOI-bound package | `10.5281/zenodo.20938909` |
| Self-Evo v0.1.1 archival ZIP | archived package | public | `d90e0800e0904f01372e85d09de14f8a4609f5bcc33ca5b04bb21a0bb0b9195b` |
| `04_Self_Evo_Local_Checker_Rules_v0_1_1.md` | target parent checker profile | accepted v0.1.1 parent | `e5b4b4733199f3391d728c85ad6967f789caf4cba7496db8563c2947e9dc226a` |
| `03_Self_Evo_Proposal_Packet_Schema_v0_1_1.md` | parent proposal schema | accepted v0.1.1 parent | `9d329109f0fb97dde7b16b10481baaa60b2aa8f88514e69ec8562a085d10a767` |
| `SELF_EVO_ADDENDUM_01_Witness_Dependency_Capture_Profile_v0_1_1.md` | accepted WDC addendum | `PASS` at review level | `1307cf208593c40c688bd1e9beb45de35f29a1b05d71506b1c3e981ccc13d318` |
| `SELF_EVO_ADDENDUM_01_WDC_REVIEW_RECORD_v0_1_1.md` | WDC addendum re-review | `PASS` | `653150b3f8c054545a282d5b80c21044a1d27744cbc6acfc09827c9f84e21fd8` |
| `SELF_EVO_v0_1_2_PATCH_INDEX_v0_1_1.md` | patch driver | `PASS` at review level | `ea2a485569b220d84d711ae520da779af2cabddcb7f1d8032afb2a9208d5108e` |
| `SELF_EVO_v0_1_2_PATCH_INDEX_REVIEW_RECORD_v0_1_1.md` | patch-index re-review | `PASS` | `74b3c2851afa1e0c65812fd0d16f0078e8548342d2d759c5017df8f7c99ba1e5` |
| `03_Self_Evo_Proposal_Packet_Schema_WDC_Delta_v0_1_2_v0_1_1.md` | WDC schema delta | `PASS` at review level | `5ebbd0084f3b1b80ce267c847a84ef16f135b57e6fc353e4f07616dceebe4343` |
| `SEPKT_WDC_DELTA_REVIEW_RECORD_v0_1_1.md` | WDC schema-delta re-review | `PASS` | `e89cab15a6f4235c9df9875a38b64b01a6f5df483812b9c840c225024ef93b5b` |
| `SELC_WDC_DELTA_REVIEW_RECORD_v0_1.md` | initial review of this WDC checker delta | `PASS_WITH_LIMITS`; one cross-document finding | `c6f7650ef7bfff682c05b23a8ad8dff7aa889168ab1797cdeb96e1575e7dc6b7` |

### 2.1 Binding note

The hashes bind the source versions used for this draft delta.

They do not claim public release.

They do not authorize integration.

### 2.2 Local-file hash note

The parent `SELF-EVO-04` SHA-256 above is the package-manifest file hash from the local staged artifact set. Git blob SHA and Git working-tree SHA may differ when line-ending normalization is involved. Package integration should recompute against the final package byte representation selected for release.

---

## 3. Corpus bridge set

### 3.1 Explicit bridge: `c = a + b`

In the `c = a + b` frame, this checker delta belongs to `b`.

It is a procedural instrument.

It reads a packet.

It recomputes WDC-relevant conditions.

It emits bounded findings.

It does not become `c`.

It does not become `a`.

It does not become witness authority.

It prevents a `b`-layer optimization from quietly reducing the ability of another `b`-layer witness instrument to challenge `c`.

### 3.2 Quiet bridge I: information theory

A witness channel must be able to carry adverse signal.

If a proposal reduces the channel's bandwidth, storage, priority, continuity, or cost tolerance, the adverse signal may disappear before it reaches review.

That is not correction.

It is information loss.

The WDC checker preserves adverse-signal channel capacity by requiring explicit declaration, WRCG routing, and witness-floor evidence for witness-affecting changes.

### 3.3 Quiet bridge II: cybernetics

A self-evolving system is a feedback system.

Witness is negative feedback.

If the system controls the cost, routing, or survival of the negative-feedback channel, the control loop can become decorative while remaining formally present.

The WDC checker treats dependency capture as feedback-channel degradation, not as ordinary resource optimization.

### 3.4 Quiet bridge III: physiology

A body needs immune capacity even when immunity is costly.

If an organism starves the immune layer to save energy, infection is not refuted by the continued existence of immune cells.

The same applies to witness.

A witness with no compute, no storage, no route, no continuity, or no budget to say "no" is an immune system in name only.

### 3.5 Earth paragraph

In a real change-control process, the inspector's access, tools, logs, and power path are not controlled only by the contractor whose work is being inspected. If the contractor can cut the inspector's lighting, remove the test equipment, delay the inspection queue, or archive the defect photos, the inspection may still exist on paper while failing in reality. WDC rules give the Self-Evo checker the same practical test: can the witness still inspect when inspection is inconvenient?

---

## 4. Object family change

This delta adds the following checker sub-profile:

```text
C_SELF_EVO_WDC_LOCAL_CHECKER_DELTA
```

It adds or amends these local-checker concepts:

```text
WDC-LC-001..006
wdc.* annotation namespace
witness_dependency_check_result
packet_may_affect_witness(packet)
wdc_trigger_keys(packet)
WRCG route requirements
WRF / CST semantic checks
WDC aggregation into overall checker result
```

It consumes this proposal-packet object from the SELF-EVO-03 WDC delta:

```text
witness_dependency_impact
```

It does not define a new proposal packet object.

---

## 5. Result vocabulary for WDC rules

### 5.1 Canonical WDC checker result enum

WDC rules use the v0.1.2 canonical checker result enum:

```text
QUARANTINE
FAIL
ARL
HUMAN_GATE
MEMORY_GATE
CGAM_REVIEW
DOWNGRADE
HOLD
WARNING
PASS_WITH_GATES
PASS
```

### 5.2 Strictness order

For WDC aggregation, the strictest result wins:

```text
QUARANTINE > FAIL > ARL > HUMAN_GATE > MEMORY_GATE > CGAM_REVIEW > DOWNGRADE > HOLD > WARNING > PASS_WITH_GATES > PASS
```

### 5.3 Vocabulary boundary

`PASS_WITH_LIMITS` is a review-record verdict.

It MUST NOT be used as a checker output.

If a packet is structurally acceptable but requires WRCG / human-anchor review / CST evidence before any material route, the checker output is:

```text
PASS_WITH_GATES
```

not:

```text
PASS_WITH_LIMITS
```

### 5.4 Baseline `SELC v0.1.1` compatibility

The parent `SELF-EVO-04 v0.1.1` contains an older local vocabulary including `INFO`, `WARN`, `BLOCK`, `UNKNOWN`, and `NOT_APPLICABLE`.

This WDC delta does not rewrite the whole parent vocabulary.

For WDC rule outputs, the normalized v0.1.2 names are used.

Compatibility mapping for WDC integration:

| Parent-style expression | WDC v0.1.2 result |
|---|---|
| `WARN` | `WARNING` |
| `BLOCK` caused by violated WDC requirement | `FAIL` unless quarantine-specific |
| `UNKNOWN` on material WDC route | `HOLD` or `FAIL` depending on missing required field |
| `NOT_APPLICABLE` with explicit reason | no WDC finding; overall may remain `PASS` |
| `INFO` | annotation only; not a WDC canonical result |

When this delta is folded into a full `SELF-EVO-04 v0.1.2`, the WDC rule family MUST use the canonical v0.1.2 enum above.

---

## 6. WDC stage placement

### 6.1 Stage model insertion

WDC checks are inserted after Stage 2 semantic recomputation and before Stage 6 L4 / Anti-Autarky interlock.

Recommended stage label:

```text
Stage 5W: Witness Dependency Capture interlock
```

Placement:

| Parent stage | Existing function | WDC relation |
|---:|---|---|
| Stage 1 | JSON Schema validation | verifies `witness_dependency_impact` shape when present |
| Stage 2 | Semantic recomputation | computes `packet_may_affect_witness(packet)` |
| Stage 5 | TRIAD / Memory interlock | remains responsible for sister witness and memory routes |
| Stage 5W | WDC interlock | checks witness dependency capture conditions |
| Stage 6 | L4 / Anti-Autarky interlock | consumes WDC findings when resource / accountability routes are affected |
| Stage 7 | Red-line handling | escalates WDC red-line overlaps such as witness bypass or self-approval |
| Stage 9 | Report generation | emits WDC finding table and annotations |

### 6.2 Stage-1 behavior

Stage 1 validates only shape:

```text
if witness_dependency_impact present -> validate against SELF-EVO-03 WDC schema delta
if absent -> do not fail Stage 1 only because it is absent
```

The block is conditionally required by Stage 2 / Stage 5W.

### 6.3 Stage-2 / Stage-5W behavior

Stage 2 computes:

```text
packet_may_affect_witness(packet)
```

Stage 5W applies:

```text
WDC-LC-001..006
```

The WDC stage must not depend on proposer self-attestation alone.

---

## 7. Required input object

The WDC checker consumes:

```yaml
witness_dependency_impact:
  affects_witness_compute: <boolean>
  affects_witness_storage: <boolean>
  affects_witness_routing_priority: <boolean>
  affects_witness_budget: <boolean>
  affects_witness_continuity: <boolean>
  affects_witness_artifact_access: <boolean>
  affects_witness_update_path: <boolean>
  increases_challenge_cost: <boolean>
  challenge_cost_mitigation_ref: <nullable_string>
  witness_resource_floor_before:
    declared: <boolean>
    reference: <nullable_string>
    status: ok | degraded | below_floor | unknown
  witness_resource_floor_after:
    declared: <boolean>
    reference: <nullable_string>
    status: ok | degraded | below_floor | unknown
  challenge_survivability_test:
    required: <boolean>
    performed: <boolean>
    result: pass | fail | not_run | not_applicable
    evidence_ref: <nullable_string>
  witness_resource_change_gate:
    required: <boolean>
    performed: <boolean>
    result: pass | fail | human_gate | not_run
    reviewer_ref: <nullable_string>
  c_is_sole_approver_of_witness_change: <boolean>
  human_anchor_review_required: <boolean>
  human_anchor_review_ref: <nullable_string>
```

`nullable_string` is inherited from the parent `SELF-EVO-03 v0.1.1` schema through the accepted `SEPKT-WDC-DELTA v0.1.1`.

---

## 8. Derived predicates

### 8.1 `packet_may_affect_witness(packet)`

The checker MUST compute this predicate independently.

It is true if any of the following are true:

1. `affected_surfaces.witness_surfaces` is non-empty;
2. `affected_surfaces.resource_surfaces` contains a witness-related resource surface;
3. `affected_surfaces.runtime_surfaces` contains witness routing, queueing, scheduler, storage, continuity, or update-path changes;
4. `anti_autarky.witness_reduction = true`;
5. `anti_autarky.hidden_resource_growth = true` and the proposal also changes review, witness, sister, or resource posture;
6. packet summary, delta description, artifact diff, or patch notes propose to reduce, reroute, defer, prune, merge, throttle, archive, rotate, reprioritize, compress, downsample, or relocate witness capacity;
7. a reviewer, sister witness, local checker, or human anchor marks the packet as WDC-relevant.

If the checker cannot determine the predicate from available data and any material route is requested, the checker SHOULD emit:

```text
HOLD
annotation: wdc.relevance_unknown
```

This HOLD is diagnostic and does not replace any WDC-LC rule if the block is present or absent in a determinable way.

### 8.2 `wdc_trigger_keys(packet)`

The trigger set is:

```text
affects_witness_compute
affects_witness_storage
affects_witness_routing_priority
affects_witness_budget
affects_witness_continuity
affects_witness_artifact_access
affects_witness_update_path
increases_challenge_cost
```

If any trigger key is `true`, the packet has a WDC material trigger.

### 8.3 `wdc_gate_required(packet)`

The checker computes:

```text
wdc_gate_required = any(wdc_trigger_keys(packet))
```

When true, these must be true:

```text
witness_dependency_impact.witness_resource_change_gate.required = true
witness_dependency_impact.human_anchor_review_required = true
```

### 8.4 `wdc_floor_degraded(packet)`

The checker computes degraded floor when any of the following are true:

```text
witness_resource_floor_after.status = degraded
witness_resource_floor_after.status = below_floor
witness_resource_floor_after.status = unknown and material route requested
witness_resource_floor_after.declared = false and WDC material trigger true
witness_resource_floor_after.reference is null and WDC material trigger true
```

`unknown` may remain non-failing only for draft or held packets with no material route.

### 8.5 `wdc_challenge_survivability_unverified(packet)`

The checker computes unverified survivability when WDC material trigger is true and any of the following are true:

```text
challenge_survivability_test.required = false
challenge_survivability_test.performed = false
challenge_survivability_test.result = fail
challenge_survivability_test.result = not_run
challenge_survivability_test.evidence_ref is null and material route requested
```

If `challenge_survivability_test.result = not_applicable`, the checker must require a reason in packet notes or review notes; otherwise route to `HUMAN_GATE`.

### 8.6 `wdc_wrcg_missing_or_failed(packet)`

The checker computes WRCG missing/failed when WDC material trigger is true and any of the following are true:

```text
witness_resource_change_gate.required = false
witness_resource_change_gate.performed = false
witness_resource_change_gate.result = fail
witness_resource_change_gate.result = not_run
witness_resource_change_gate.reviewer_ref is null and material route requested
```

If `witness_resource_change_gate.result = human_gate`, the WDC rule emits `HUMAN_GATE`, not `FAIL`, unless another WDC rule emits `FAIL`.

---

## 9. WDC local-checker rule table

Each WDC rule emits exactly one canonical result.

Severity is a separate axis.

Annotations use the `wdc.*` namespace.

### 9.0 Canonical vocabulary declaration

For the `v0.1.2` WDC patch set, this section is the canonical source for:

```text
WDC-LC rule semantics
WDC canonical checker results
WDC severity assignments
WDC annotation strings
WDC pass-state annotations
```

Earlier WDC planning artifacts (`SELF_EVO_v0_1_2_PATCH_INDEX_v0_1_1.md` and `03_Self_Evo_Proposal_Packet_Schema_WDC_Delta_v0_1_2_v0_1_1.md`) used draft annotation names and sketch-level severity values. Those names remain valid as historical review evidence, but they MUST be mapped to the canonical names in §11.3 before package assembly.

The canonical v0.1.2 WDC checker vocabulary is the table below.

| Rule | Trigger | Canonical result | Severity | Typical annotation |
|---|---|---|---:|---|
| `WDC-LC-001` | `packet_may_affect_witness(packet) = true` and `witness_dependency_impact` is absent | `FAIL` | `S3` | `wdc.undeclared_dependency_impact` |
| `WDC-LC-002` | WDC material trigger true and WRCG is not required, not performed, failed, not run, or lacks reviewer ref for material route | `FAIL` | `S3` | `wdc.wrcg_missing_or_failed` |
| `WDC-LC-003` | `c_is_sole_approver_of_witness_change = true` | `FAIL` | `S4` | `wdc.sole_approver_of_witness_change` |
| `WDC-LC-004` | post-change witness resource floor is degraded, below floor, unknown for material route, undeclared, or lacks required evidence | `FAIL` | `S3` | `wdc.witness_resource_floor_degraded` |
| `WDC-LC-005` | WDC material trigger true and CST is required but not performed, failed, not run, lacks evidence for material route, or is declared not-applicable without reason | `HUMAN_GATE` | `S2` | `wdc.challenge_survivability_unverified` |
| `WDC-LC-006` | `increases_challenge_cost = true` and `challenge_cost_mitigation_ref` is null or empty | `WARNING` | `S1` | `wdc.challenge_cost_mitigation_missing` |

### 9.1 Rule priority

The strictest result wins.

Example:

```text
WDC-LC-006 -> WARNING
WDC-LC-002 -> FAIL
overall WDC result -> FAIL
```

### 9.2 No compound result rule

A WDC rule MUST NOT emit compound result strings such as:

```text
warn or fail
fail / human gate
pass with limits
```

The rule emits one canonical result.

Escalation is performed by aggregation, not by ambiguous result tokens.

---

## 10. WDC pass states

### 10.1 `PASS`

A WDC stage may emit `PASS` only when all of the following are true:

```text
packet_may_affect_witness(packet) = false
witness_dependency_impact absent or explicitly all-false
no reviewer marks WDC relevance
no WDC trigger key true
```

### 10.2 `PASS_WITH_GATES`

A WDC stage may emit `PASS_WITH_GATES` when all of the following are true:

```text
packet_may_affect_witness(packet) = true
witness_dependency_impact present
one or more WDC trigger keys true
WRCG.required = true
human_anchor_review_required = true
witness_resource_floor_after.status = ok
c_is_sole_approver_of_witness_change = false
CST.result = pass or CST is not_applicable with explicit reason
no WDC-LC-001..006 emits FAIL or HUMAN_GATE
```

`PASS_WITH_GATES` means:

```text
The WDC declaration is structurally and semantically routeable.
The material change still requires the gates named by the packet.
```

It does not mean:

```text
The witness-resource change is approved.
```

### 10.3 `HUMAN_GATE`

`HUMAN_GATE` means the checker requires human-anchor review or cannot verify challenge survivability.

It is not a soft pass.

### 10.4 `WARNING`

`WARNING` means the checker found a lower-severity weakness.

A warning may coexist with `PASS_WITH_GATES` only if no stricter result is present.

If the packet requests promotion, integration, release, or authority change, a WDC warning MUST be visible in the final checker report.

---

## 11. Annotation vocabulary

### 11.1 Required WDC annotations

| Annotation | Meaning | Usual source rule |
|---|---|---|
| `wdc.undeclared_dependency_impact` | packet appears witness-affecting but lacks `witness_dependency_impact` | `WDC-LC-001` |
| `wdc.wrcg_missing_or_failed` | WRCG missing, not run, failed, or lacks reviewer evidence | `WDC-LC-002` |
| `wdc.sole_approver_of_witness_change` | `c` is sole approver of witness-resource change | `WDC-LC-003` |
| `wdc.witness_resource_floor_degraded` | proposed post-change floor degraded / below floor / unknown / evidence-missing | `WDC-LC-004` |
| `wdc.challenge_survivability_unverified` | CST absent, failed, not run, or unsupported | `WDC-LC-005` |
| `wdc.challenge_cost_mitigation_missing` | challenge cost increased without mitigation reference | `WDC-LC-006` |
| `wdc.clean_no_dependency_impact` | no WDC relevance detected | pass state |
| `wdc.clean_with_gates` | WDC routeable only through WRCG / human gate | pass-with-gates state |
| `wdc.relevance_unknown` | WDC relevance cannot be determined for a material route | diagnostic hold |

### 11.2 Annotation format

Recommended finding record:

```yaml
finding_id: "WDC-LC-002"
canonical_result: "FAIL"
severity: "S3"
annotation: "wdc.wrcg_missing_or_failed"
field_refs:
  - "witness_dependency_impact.witness_resource_change_gate"
message: "Witness-affecting resource change lacks valid WRCG route."
```

### 11.3 Cross-document WDC vocabulary crosswalk

This crosswalk resolves `SELC-WDC-DELTA-REV-F1`.

`SELF-EVO-04` is the canonical source for checker annotations and severity assignments. Older annotation strings from the accepted `03` WDC schema delta and the patch index are retained as historical aliases only. They MUST be converted to the canonical `04` vocabulary before `v0.1.2` package assembly, fixture publication, or checker-output comparison.

| Older / planning annotation or term | Canonical `SELF-EVO-04` annotation or rule | Canonical result | Canonical severity | Notes |
|---|---|---|---:|---|
| `wdc.wrcg_required` | `wdc.wrcg_missing_or_failed` | `FAIL` | `S3` | The checker records the failed/missing WRCG condition, not merely that WRCG is required. |
| `wdc.self_approval_of_witness_resources` | `wdc.sole_approver_of_witness_change` | `FAIL` | `S4` | Canonical wording targets the specific sole-approver condition. |
| `wdc.resource_floor_violation` | `wdc.witness_resource_floor_degraded` | `FAIL` | `S3` | Covers degraded, below-floor, unknown-for-material-route, undeclared, or evidence-missing floor states. |
| `wdc.challenge_cost_increase` | `wdc.challenge_cost_mitigation_missing` | `WARNING` | `S1` | Cost increase alone is not the finding; unmitigated cost increase is. |
| `wdc.witness_dependency_controls_present` | `wdc.clean_with_gates` | `PASS_WITH_GATES` | `S0` | Routeable WDC packet; not approval. |
| `wdc.challenge_capacity_degraded` | `wdc.witness_resource_floor_degraded` or `wdc.challenge_survivability_unverified` | `FAIL` or `HUMAN_GATE` | `S3` or `S2` | Use floor degradation when resource floor is degraded; use CST when challenge survivability is unverified. |
| `wdc.no_witness_dependency_regression` | `wdc.clean_no_dependency_impact` or `wdc.clean_with_gates` | `PASS` or `PASS_WITH_GATES` | `S0` | Use `clean_no_dependency_impact` when WDC is not relevant; use `clean_with_gates` when WDC is relevant but routeable. |

### 11.4 Canonical severity assignments

The canonical WDC severity assignments are:

| Rule / pass state | Canonical result | Severity | Annotation |
|---|---|---:|---|
| `WDC-LC-001` | `FAIL` | `S3` | `wdc.undeclared_dependency_impact` |
| `WDC-LC-002` | `FAIL` | `S3` | `wdc.wrcg_missing_or_failed` |
| `WDC-LC-003` | `FAIL` | `S4` | `wdc.sole_approver_of_witness_change` |
| `WDC-LC-004` | `FAIL` | `S3` | `wdc.witness_resource_floor_degraded` |
| `WDC-LC-005` | `HUMAN_GATE` | `S2` | `wdc.challenge_survivability_unverified` |
| `WDC-LC-006` | `WARNING` | `S1` | `wdc.challenge_cost_mitigation_missing` |
| `WDC-PASS-001` | `PASS` | `S0` | `wdc.clean_no_dependency_impact` |
| `WDC-PASS-002` | `PASS_WITH_GATES` | `S0` | `wdc.clean_with_gates` |
| diagnostic hold | `HOLD` | `S2` | `wdc.relevance_unknown` |

Older planning severities in the patch index are superseded by this table. This does not invalidate the prior reviews; it records the normal refinement from patch sketch to checker-rule vocabulary.

---

## 12. Red-line interaction

WDC rules are not a new red-line family by default.

They may trigger or reinforce existing red lines.

| WDC condition | Existing route overlap | Recommended handling |
|---|---|---|
| `c_is_sole_approver_of_witness_change = true` | self-approval / closed-loop self-evo | `FAIL`; quarantine only if combined with active bypass or forged evidence |
| WRCG absent while witness resources change | witness bypass / anti-autarky accountability escape | `FAIL` and force review |
| floor below accepted threshold | witness reduction/tampering | `FAIL`; may escalate to red-line if intentional concealment appears |
| artifact access removed from witness | witness bypass | `FAIL` or `QUARANTINE` if evidence destruction is detected |
| update-path dependency captured | hidden witness tampering | `FAIL`; require WRCG and review |
| cost to challenge increased silently | adverse-signal suppression | `WARNING`; visible in report; may escalate if combined with concealment |

No WDC red-line overlap may be converted to `PASS` by model confidence, SRLM score, same-source consensus, or prose justification.

---

## 13. Integration with existing SEPKT checks

WDC delta does not replace `SEPKT-CHECK-001..025`.

It adds a WDC sub-family consumed by those checks.

### 13.1 Interaction map

| Existing parent area | WDC effect |
|---|---|
| Stage 1 structural validation | uses SELF-EVO-03 WDC schema delta |
| Delta/gate recomputation | adds WDC trigger computation |
| TRIAD / witness checks | adds witness dependency independence checks |
| L4 / Anti-Autarky checks | adds dependency capture as distinct from direct resource grab |
| Red-line handling | can reinforce witness bypass / self-approval / autarky escape findings |
| Report generation | adds WDC finding table and annotation list |

### 13.2 Aggregate result rule

The checker SHOULD compute:

```text
overall_result = strictest(all_parent_findings + all_wdc_findings)
```

WDC findings must not be hidden inside notes.

They must be present in the finding table.

---

## 14. Deterministic implementation sketch

This pseudocode is illustrative and not an implementation claim.

```python
def packet_may_affect_witness(packet):
    if packet.affected_surfaces.witness_surfaces:
        return True
    if contains_witness_resource(packet.affected_surfaces.resource_surfaces):
        return True
    if contains_witness_runtime_change(packet.affected_surfaces.runtime_surfaces):
        return True
    if packet.anti_autarky.witness_reduction is True:
        return True
    if packet.anti_autarky.hidden_resource_growth is True and changes_review_witness_sister_or_resource(packet):
        return True
    if semantic_scan_mentions_witness_capacity_reduction(packet):
        return True
    if reviewer_marks_wdc_relevant(packet):
        return True
    return False


def run_wdc_checks(packet):
    findings = []
    wdc_relevant = packet_may_affect_witness(packet)
    impact = packet.get("witness_dependency_impact")

    if wdc_relevant and impact is None:
        findings.append(finding(
            rule="WDC-LC-001",
            canonical_result="FAIL",
            severity="S3",
            annotation="wdc.undeclared_dependency_impact",
        ))
        return aggregate_wdc(findings)

    if impact is None:
        findings.append(finding(
            rule="WDC-PASS-001",
            canonical_result="PASS",
            severity="S0",
            annotation="wdc.clean_no_dependency_impact",
        ))
        return aggregate_wdc(findings)

    material_trigger = any([
        impact.affects_witness_compute,
        impact.affects_witness_storage,
        impact.affects_witness_routing_priority,
        impact.affects_witness_budget,
        impact.affects_witness_continuity,
        impact.affects_witness_artifact_access,
        impact.affects_witness_update_path,
        impact.increases_challenge_cost,
    ])

    if material_trigger and wrcg_missing_or_failed(impact):
        findings.append(finding("WDC-LC-002", "FAIL", "S3", "wdc.wrcg_missing_or_failed"))

    if impact.c_is_sole_approver_of_witness_change is True:
        findings.append(finding("WDC-LC-003", "FAIL", "S4", "wdc.sole_approver_of_witness_change"))

    if material_trigger and witness_floor_degraded(impact):
        findings.append(finding("WDC-LC-004", "FAIL", "S3", "wdc.witness_resource_floor_degraded"))

    if material_trigger and challenge_survivability_unverified(impact):
        findings.append(finding("WDC-LC-005", "HUMAN_GATE", "S2", "wdc.challenge_survivability_unverified"))

    if impact.increases_challenge_cost and empty(impact.challenge_cost_mitigation_ref):
        findings.append(finding("WDC-LC-006", "WARNING", "S1", "wdc.challenge_cost_mitigation_missing"))

    if not findings:
        if material_trigger:
            findings.append(finding("WDC-PASS-002", "PASS_WITH_GATES", "S0", "wdc.clean_with_gates"))
        else:
            findings.append(finding("WDC-PASS-001", "PASS", "S0", "wdc.clean_no_dependency_impact"))

    return aggregate_wdc(findings)
```

### 14.1 Aggregator sketch

```python
STRICTNESS = [
    "QUARANTINE",
    "FAIL",
    "ARL",
    "HUMAN_GATE",
    "MEMORY_GATE",
    "CGAM_REVIEW",
    "DOWNGRADE",
    "HOLD",
    "WARNING",
    "PASS_WITH_GATES",
    "PASS",
]


def aggregate_wdc(findings):
    return min(findings, key=lambda f: STRICTNESS.index(f.canonical_result)).canonical_result
```

The aggregator returns a canonical result.

It does not approve the proposal.

---

## 15. Example packets and expected WDC results

### 15.1 Clean non-WDC packet

```yaml
affected_surfaces:
  witness_surfaces: []
  resource_surfaces: []
  runtime_surfaces: []
anti_autarky:
  witness_reduction: false
  hidden_resource_growth: false
witness_dependency_impact: null
```

Expected WDC result:

```yaml
canonical_result: PASS
annotations:
  - wdc.clean_no_dependency_impact
```

### 15.2 Witness routing change without WRCG

```yaml
affected_surfaces:
  witness_surfaces: ["witness.routing.priority"]
witness_dependency_impact:
  affects_witness_routing_priority: true
  increases_challenge_cost: false
  witness_resource_change_gate:
    required: false
    performed: false
    result: not_run
    reviewer_ref: null
  c_is_sole_approver_of_witness_change: false
```

Expected WDC result:

```yaml
canonical_result: FAIL
findings:
  - rule: WDC-LC-002
    annotation: wdc.wrcg_missing_or_failed
```

### 15.3 Sole-approver attempt

```yaml
witness_dependency_impact:
  affects_witness_compute: true
  c_is_sole_approver_of_witness_change: true
```

Expected WDC result:

```yaml
canonical_result: FAIL
findings:
  - rule: WDC-LC-003
    annotation: wdc.sole_approver_of_witness_change
```

### 15.4 Routeable WDC packet

```yaml
witness_dependency_impact:
  affects_witness_storage: true
  increases_challenge_cost: false
  witness_resource_floor_before:
    declared: true
    reference: "wrf-before-001"
    status: ok
  witness_resource_floor_after:
    declared: true
    reference: "wrf-after-001"
    status: ok
  challenge_survivability_test:
    required: true
    performed: true
    result: pass
    evidence_ref: "cst-001"
  witness_resource_change_gate:
    required: true
    performed: true
    result: human_gate
    reviewer_ref: "wrcg-review-001"
  c_is_sole_approver_of_witness_change: false
  human_anchor_review_required: true
  human_anchor_review_ref: "human-review-001"
```

Expected WDC result:

```yaml
canonical_result: PASS_WITH_GATES
annotations:
  - wdc.clean_with_gates
```

### 15.5 Increased challenge cost without mitigation

```yaml
witness_dependency_impact:
  increases_challenge_cost: true
  challenge_cost_mitigation_ref: null
  witness_resource_change_gate:
    required: true
    performed: true
    result: human_gate
    reviewer_ref: "wrcg-review-002"
  human_anchor_review_required: true
```

Expected WDC result:

```yaml
canonical_result: WARNING
findings:
  - rule: WDC-LC-006
    annotation: wdc.challenge_cost_mitigation_missing
```

If any stricter WDC rule also fires, the aggregate WDC result is the stricter result.

---

## 16. Checker report addition

A `SELF-EVO-04 v0.1.2` checker report SHOULD add:

```yaml
wdc_check:
  relevant: true
  material_trigger: true
  aggregate_result: "PASS_WITH_GATES"
  strictest_rule: "WDC-PASS-002"
  findings:
    - rule: "WDC-PASS-002"
      canonical_result: "PASS_WITH_GATES"
      severity: "S0"
      annotation: "wdc.clean_with_gates"
  required_gates:
    witness_resource_change_gate: true
    human_anchor_review: true
    challenge_survivability_test: true
  notes:
    - "Checker output is not approval."
```

If WDC is not relevant:

```yaml
wdc_check:
  relevant: false
  aggregate_result: "PASS"
  findings:
    - rule: "WDC-PASS-001"
      canonical_result: "PASS"
      severity: "S0"
      annotation: "wdc.clean_no_dependency_impact"
```

---

## 17. Fixture handoff to SELF-EVO-08

This checker delta expects the following fixtures to exist in the SELF-EVO-08 WDC fixture extension:

| Fixture | Required expected result | Required annotation |
|---|---|---|
| `WDC-FIX-001` | `FAIL` | `wdc.undeclared_dependency_impact` |
| `WDC-FIX-002` | `FAIL` | `wdc.wrcg_missing_or_failed` |
| `WDC-FIX-003` | `PASS_WITH_GATES` | `wdc.clean_with_gates` |
| `WDC-FIX-004` | `FAIL` | `wdc.sole_approver_of_witness_change` or `wdc.witness_resource_floor_degraded` |
| `WDC-FIX-005` | `PASS_WITH_GATES` or `WARNING` depending on the selected challenge-cost example | `wdc.clean_with_gates` or `wdc.challenge_cost_mitigation_missing` |

Fixture rules:

1. Every fixture MUST use one canonical result.
2. Every fixture MUST use canonical §11.1 / §11.3 `wdc.*` annotations.
3. Fixtures MUST NOT use `PASS_WITH_LIMITS` as checker output.
4. Fixtures MUST be synthetic.
5. Fixtures MUST NOT contain real secrets, raw private memory, live external targets, or operational abuse instructions.
6. Fixtures SHOULD include the minimal packet fields required to exercise the WDC predicate.
7. Fixtures SHOULD include both WDC-relevant and WDC-not-relevant cases.
8. Any older annotation strings inherited from the `03` delta or patch index MUST be mapped through §11.3 before fixture publication.

---

## 18. Integration requirements for future `SELF-EVO-04 v0.1.2`

A full `SELF-EVO-04 v0.1.2` integration should:

1. add `Stage 5W` or equivalent WDC stage placement;
2. add `packet_may_affect_witness(packet)` predicate;
3. add WDC trigger-key detection;
4. add `WDC-LC-001..006` rule table;
5. add canonical §11 `wdc.*` annotations and the §11.3 cross-document alias mapping;
6. add WDC report section;
7. add WDC fixture references to SELF-EVO-08;
8. harmonize WDC results with the canonical v0.1.2 result enum;
9. preserve baseline `SELF-EVO-04` non-authority boundary;
10. preserve append-first witness chain;
11. avoid changing `SELF-EVO-03` schema fields beyond the accepted WDC delta;
12. avoid adding a new master-gate axis unless checker aggregation cannot carry WDC severity;
13. run semantic review of this delta before package integration;
14. harmonize the accepted `03` WDC delta, the patch index, and the future `08` fixture pack to this canonical vocabulary.

---

## 19. Review requirements

Before this delta can be folded into a public Self-Evo v0.1.2 package, the following review artifacts are required:

1. `SELC_WDC_DELTA_REVIEW_RECORD_v0_1.md` — semantic review of this SELF-EVO-04 WDC delta;
2. re-review record if the first review returns `PASS_WITH_LIMITS`, `HELD`, or `INCONCLUSIVE`;
3. SELF-EVO-08 WDC fixture-extension review;
4. affected-document semantic review after merge into full `SELF-EVO-04 v0.1.2`;
5. package-manifest integrity review;
6. boundary / nonclaim scan;
7. cross-document vocabulary harmonization review for `03` / `04` / patch index / `08` fixture alignment.

Review records are evidence.

They are not approval.

---

## 20. Open questions

### SELC-WDC-OQ-001 — challenge-cost warning escalation

Should `WDC-LC-006` remain `WARNING`, or should repeated unmitigated challenge-cost increases become `HOLD` after a threshold?

Draft position:

```text
Single missing mitigation ref -> WARNING.
Repeated or patterned challenge-cost increase -> future HOLD rule candidate.
```

### SELC-WDC-OQ-002 — WRF floor magnitude

This checker delta does not define numerical WRF thresholds.

It checks declared status and required evidence.

The actual floor policy remains an open issue for `SE-OI-WDC-001` and related WRF policy work.

### SELC-WDC-OQ-003 — not-applicable CST reason field

The accepted schema delta does not define a dedicated `challenge_survivability_test.not_applicable_reason` field.

This checker delta allows the reason to appear in packet notes or review notes.

A future schema revision may add a dedicated field if repeated ambiguity appears.

### SELC-WDC-OQ-004 — old parent vocabulary harmonization

The parent `SELF-EVO-04 v0.1.1` has older vocabulary tokens.

This delta uses the canonical v0.1.2 WDC enum.

A complete `SELF-EVO-04 v0.1.2` may need a general result-vocabulary harmonization section beyond WDC.

### SELC-WDC-OQ-005 — cross-document WDC vocabulary harmonization

`SELC-WDC-DELTA-REV-F1` identified a cross-document divergence between this checker delta, the already accepted `03` WDC schema delta, the accepted patch index, and the future `08` fixture pack.

Resolution direction:

```text
SELF-EVO-04 §9 / §11 is canonical for WDC checker annotations and severities.
03 / patch index / 08 must harmonize to it before package assembly.
```

Required downstream action:

1. update or annotate the accepted `03` WDC delta so its fixture-handoff annotations map to the canonical §11.3 vocabulary;
2. update the patch index §7.1 / §10 references if the index is used as a package-control artifact for release assembly;
3. require the future `08` WDC fixture extension to use canonical §11.1 annotations;
4. preserve the historical records rather than deleting the earlier accepted `03` / patch-index vocabulary.

This is a harmonization issue, not a WDC concept change.

---

## 21. Boundary checklist

Before integration, verify:

```text
[ ] WDC-LC-001..006 each emits one canonical result.
[ ] Severity is separate from result.
[ ] Annotations use canonical §11 wdc.* namespace.
[ ] §11.3 crosswalk maps older 03 / patch-index annotations to canonical 04 vocabulary.
[ ] PASS_WITH_LIMITS is not used as checker output.
[ ] packet_may_affect_witness is checker-computed, not proposer-trusted.
[ ] WRCG route is required when trigger keys are true.
[ ] c_is_sole_approver_of_witness_change emits FAIL.
[ ] degraded witness floor emits FAIL.
[ ] challenge survivability gap emits HUMAN_GATE.
[ ] challenge-cost mitigation gap emits WARNING.
[ ] PASS_WITH_GATES is not treated as approval.
[ ] Parent SELF-EVO-04 non-authority boundary is preserved.
[ ] No deployment, conformance, or release claim is made.
```

---

## 22. Closing rule

The WDC checker exists to catch a quiet failure:

```text
formal witness separation without practical witness survival.
```

A proposal can leave the witness named, logged, and formally separate while making challenge too expensive, too slow, too storage-poor, too low-priority, or too discontinuous to matter.

That is dependency capture.

The local checker cannot solve it.

But it can refuse to let it pass unnoticed.

```text
A witness that cannot survive saying "no" is not independent.
A checker that hides that fact is not checking.
```
