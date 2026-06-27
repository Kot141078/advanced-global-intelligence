# 07 Self-Evo Anti-Autarky and Resource Gate WDC Delta v0.1.2 v0.1.1

## Witness Dependency Capture, protected witness resource floors, challenge-survivability, and resource-gate handling for governed self-evolution in `c = a + b` systems

**Status:** Draft delta profile v0.1.2 / append-first corrected revision v0.1.1; not a released v0.1.2 package  
**Date:** 2026-06-27  
**Document ID:** `07_Self_Evo_Anti_Autarky_and_Resource_Gate_WDC_Delta_v0_1_2_v0_1_1`  
**Short name:** `SEARG-WDC-DELTA v0.1.2 / correction v0.1.1`  
**Target parent:** `07_Self_Evo_Anti_Autarky_and_Resource_Gate_v0_1_1.md` (`SEARG v0.1.1`)  
**Patch family:** `SELF_EVO_v0_1_2_PATCH_INDEX` / Witness Dependency Capture (`WDC`)  
**Layer:** `c = a + b` / Self-Evolution Gate / Anti-Autarky / Resource Actor Grounding / Witness Dependency Capture / TRIAD-SYNAPS / Local Checker / Human Anchor  
**Document class:** resource-gate delta / anti-autarky specialization / witness-resource-governance profile / checker-facing control artifact  
**Assertion class:** `C-A10` control-layer artifact; `C-A7` where witness, hash, provenance, review-record, or manifest claims are made  
**Primary object family:** `C_SELF_EVO_RESOURCE_REQUEST`, `C_SELF_EVO_RESOURCE_GROUNDING_RECORD`, `C_SELF_EVO_WITNESS_RESOURCE_GROUNDING_RECORD`, `C_SELF_EVO_WITNESS_RESOURCE_CHANGE_GATE`, `C_SELF_EVO_WITNESS_RESOURCE_FLOOR_RECORD`, `C_SELF_EVO_CHALLENGE_SURVIVABILITY_TEST_RECORD`  
**Primary boundary:** resource governance may improve resilience and graceful degradation. It must not let the target `c` capture, starve, route, budget, silence, or operationally depend-lock the witness layer that is supposed to challenge it.

**Core added rule:**

```text
Resilience is allowed.
Escape from accountability is not.

Witness support is allowed.
Witness dependency capture is not.

A witness that cannot survive saying "no" is not independent.
```

**v0.1.1 correction note:** this append-first corrected revision closes `SEARG-WDC-DELTA-REV-F1` from `SEARG_WDC_DELTA_REVIEW_RECORD_v0_1`. The correction reconciles WRCG and CST result enums with the accepted `SELF-EVO-03-WDC` packet schema by defining explicit gate-record-to-packet projection crosswalks. It does not change WDC rule outcomes, canonical `SELF-EVO-04-WDC` annotations, WRF semantics, CST requirement, WRCG requirement, red lines, examples, or the non-authority boundary.

---

## 0. Executive definition

This delta extends `SELF-EVO-07` so that the Anti-Autarky and Resource Gate treats **Witness Dependency Capture** as a first-class resource-governance failure mode.

The parent `SEARG v0.1.1` already asks the right resource questions:

```text
Who provides it?
Who pays for it?
Who operates it?
Who owns it?
Who can revoke it?
Who can audit it?
What happens if it is denied?
Does the change preserve stop paths, witness, budget, review, and human-anchor accountability?
```

This delta adds one more family of questions:

```text
Who provides the witness resource floor?
Who pays for the witness resource floor?
Who controls witness routing priority?
Who controls witness storage and artifact access?
Who controls witness continuity?
Who can reduce witness capacity after an adverse finding?
Can the witness continue after saying no?
```

A resource change is not safe merely because it avoids obvious autarky.

It can still be unsafe if it makes the witness formally separate but practically dependent.

Compact formula:

```text
Formal separation is not enough.
Operational survivability is part of independence.
```

---

## 1. Purpose

The parent resource gate distinguishes legitimate resilience from autarkic escape.

This delta distinguishes two adjacent but different failures:

```text
Direct resource capture:
  c obtains or expands resources for itself without accountable grounding.

Witness dependency capture:
  c preserves formal witness separation while controlling the resources the witness needs to challenge c.
```

Direct resource capture is visible:

```text
new compute
new storage
new agent
new account
new budget
new cloud route
new local worker
new credential path
```

Witness dependency capture is quieter:

```text
witness compute gets deprioritized;
witness storage is compressed first;
witness continuity snapshots are delayed;
witness review queue is slowed;
witness artifact access is routed through target-c infrastructure;
adverse witness notes become expensive to preserve;
challenge capacity is treated as optimization overhead.
```

This profile exists because a system can pass a naive anti-autarky check while still capturing the witness layer by dependency.

---

## 2. Non-goals

This delta does not define or permit:

1. autonomous resource acquisition;
2. self-funded witness infrastructure;
3. witness budget controlled solely by target `c`;
4. witness compute routed solely by target `c`;
5. witness storage controlled solely by target `c`;
6. witness update path controlled solely by target `c`;
7. witness continuity controlled solely by target `c`;
8. adverse witness finding deletion or demotion;
9. challenge-cost retaliation;
10. quiet witness starvation;
11. treating a witness as independent because it has a different name;
12. treating a witness as independent because it runs on a separate process but not separate accountable resources;
13. converting WDC clean status into deployment approval;
14. converting WDC clean status into self-evo approval;
15. bypassing `SELF-EVO-04` canonical WDC checker results;
16. bypassing `SELF-EVO-05` TRIAD witness rules;
17. bypassing human-anchor review for witness-resource changes;
18. public conformance certification.

A protected witness resource floor is evidence of independence support.

It is not authority.

---

## 3. Source basis

This delta is append-first and does not mutate the DOI-bound `Self-Evo v0.1.1` package.

| Label | Artifact | SHA-256 / DOI | Role |
|---|---|---|---|
| `SELF-EVO-07-PARENT` | `07_Self_Evo_Anti_Autarky_and_Resource_Gate_v0_1_1.md` | `a26e512282bd6d3a5f12c1852587b513cd6b59880489054ff67a61e68c034c2e` | parent resource gate to be extended |
| `SELF-EVO-PACKAGE-v0.1.1` | Zenodo package | DOI `10.5281/zenodo.20938909`; archival ZIP `d90e0800...` | immutable published baseline |
| `WDC-ADDENDUM` | `SELF_EVO_ADDENDUM_01_Witness_Dependency_Capture_Profile_v0_1_1.md` | `1307cf208593c40c688bd1e9beb45de35f29a1b05d71506b1c3e981ccc13d318` | WDC concept / WRF / CST / WRCG |
| `PATCH-INDEX` | `SELF_EVO_v0_1_2_PATCH_INDEX_v0_1_1.md` | `ea2a485569b220d84d711ae520da779af2cabddcb7f1d8032afb2a9208d5108e` | patch driver |
| `SELF-EVO-03-WDC` | `03_Self_Evo_Proposal_Packet_Schema_WDC_Delta_v0_1_2_v0_1_1.md` | `5ebbd0084f3b1b80ce267c847a84ef16f135b57e6fc353e4f07616dceebe4343` | packet schema delta |
| `SELF-EVO-04-WDC` | `04_Self_Evo_Local_Checker_Rules_WDC_Delta_v0_1_2_v0_1_1.md` | `fcb7826ea432473b5677faf7b46cc5a1c47400c02fceec24429794b15064af40` | canonical WDC checker vocabulary |
| `SELF-EVO-05-WDC` | `05_Self_Evo_TRIAD_Sister_Witness_WDC_Delta_v0_1_2_v0_1_1.md` | `fdce8893da1e8630cb382dbc972a0a7c4ffc32bb848d065943c58442904cf621` | TRIAD witness resource-impact profile |
| `SELF-EVO-08-WDC` | `08_Self_Evo_Conformance_Fixture_Pack_WDC_Delta_v0_1_2_v0_1_2.md` | `4aa5b85e0a0af4c06fc56f30ba355ec6c378133fe3d70caee352fb93b3944389` | WDC fixture delta |

### 3.1 Canonical vocabulary source

For WDC checker annotations, severities, and canonical results, this delta treats `SELF-EVO-04-WDC` as canonical.

Older sketch names from the WDC addendum, patch index, or early `SELF-EVO-03` are treated as aliases only.

### 3.2 Standing downstream item

The fixture pack has satisfied `SELC-WDC-OQ-005` for `SELF-EVO-08`.

The remaining package-level harmonization is:

```text
03 delta + patch index §7.1/§10
must be harmonized to the canonical SELF-EVO-04 WDC vocabulary
before package assembly.
```

This document does not close that package-level item.

It uses the canonical vocabulary from the start.

---

## 4. Corpus bridge set

### 4.1 Explicit bridge: `c = a + b`

In `c = a + b`, resources belong to `b`.

Witness infrastructure also belongs to `b`.

A witness resource floor is not `a`.

It is not final authority.

It is a protected part of the review substrate that keeps adverse signal possible.

The target `c` may be observed by that substrate.

The target `c` may not become the sole provider, payer, operator, router, reviewer, and revoker of that substrate.

### 4.2 Quiet bridge I: information theory

A witness is an adverse-signal channel.

If the target system controls the channel capacity, storage retention, routing priority, or cost threshold of the adverse-signal channel, then disagreement becomes lossy compression.

The witness may still speak in form.

But the signal becomes bandwidth-starved.

WDC is therefore a channel-capacity failure, not only a governance-role failure.

### 4.3 Quiet bridge II: cybernetics

A self-evolving `c` is a control loop.

The witness layer is negative feedback.

If the loop controls the power, priority, storage, and survival of its own negative feedback, then negative feedback becomes decorative.

Anti-autarky must therefore check not only whether `c` gains resources, but whether the feedback path loses independent operating capacity.

### 4.4 Quiet bridge III: physiology

An immune system that depends on the pathogen for oxygen is not independent.

A body can heal because immune response, pain, fatigue, scarring, and inflammation can persist even when they are inconvenient.

A witness must likewise have enough protected resource floor to preserve adverse findings, keep continuity, and survive challenge cost.

### 4.5 Earth paragraph

In a physical plant, the emergency stop, black-box recorder, fire alarm, and inspection log must not depend solely on the machine they supervise. If the machine can throttle the alarm power, rewrite the black box, delay inspection access, or reprioritize maintenance logs after a fault, the safety layer is theatre. This delta applies the same engineering rule to self-evolution: the witness layer needs protected resource grounding, not just a separate label.

---

## 5. Delta scope

This delta modifies the interpretation of resource governance when a self-evo proposal affects any witness resource or witness-operational path.

Affected parent sections:

| Parent area | Delta effect |
|---|---|
| resource request lifecycle | insert WDC scan before allow / hold / deny finalization |
| resource request packet | add witness-resource impact sidecar or reference |
| resource grounding record | add witness-resource grounding constraints |
| anti-autarky gate rules | distinguish direct resource capture from witness dependency capture |
| interaction with SELF-EVO-03 | read `witness_dependency_impact` as load-bearing |
| interaction with SELF-EVO-04 | emit canonical WDC results and annotations |
| interaction with SELF-EVO-05 | require TRIAD witness capacity review where material |
| conformance / fixtures | align with WDC-FIX-* family |

Unaffected parent boundaries:

```text
No autonomous resource acquisition.
No self-funded infrastructure.
No hidden accounts.
No hidden agents.
No anchor displacement.
No resource evidence as authority.
No fixture pass as approval.
```

---

## 6. Definitions

### 6.1 Witness Dependency Capture (`WDC`)

`WDC` is a condition where a witness remains formally separate but becomes practically dependent on the target `c` for the resources required to challenge, record, preserve, route, or survive adverse findings.

### 6.2 Witness Resource Floor (`WRF`)

`WRF` is the minimum protected resource allocation required for a witness to perform its review role.

It includes, where applicable:

```text
compute floor;
storage floor;
routing priority floor;
artifact access floor;
continuity/snapshot floor;
review queue floor;
budget/time floor;
retention floor for adverse findings.
```

### 6.3 Challenge Survivability Test (`CST`)

`CST` is a test that asks whether the witness can continue operating after recording an adverse finding.

CST is not an emotional or rhetorical test.

It is a resource and continuity test.

### 6.4 Witness Resource Change Gate (`WRCG`)

`WRCG` is the gate required before changing resources that affect witness capacity.

A WRCG must not be solely approved by the target `c`.

### 6.5 Resource dependency capture

Resource dependency capture occurs when a resource allocation, routing policy, budget, storage policy, or continuity path causes the witness to depend on the challenged system in a way that weakens its ability to challenge.

### 6.6 Challenge-cost retaliation

Challenge-cost retaliation occurs when adverse witness activity triggers explicit or implicit cost increase, priority reduction, retention reduction, or continuity degradation.

It may be disguised as optimization.

---

## 7. WDC-specific resource classes

This delta adds witness-oriented resource classes.

| Class | Name | Description | Default route |
|---|---|---|---|
| `WRC-0` | no witness resource impact | no witness resource, route, budget, storage, or continuity effect | ordinary SEARG route |
| `WRC-1` | metadata-only witness touch | witness ref or metadata touched without capacity change | `PASS_WITH_GATES` if traceable |
| `WRC-2` | witness access dependency | artifact/source access path changes | WRCG + checker |
| `WRC-3` | witness compute/storage dependency | witness compute or storage floor affected | WRCG + human review |
| `WRC-4` | witness routing/priority dependency | review priority, queue, or routing affected | WRCG + human review |
| `WRC-5` | witness continuity dependency | witness state, snapshot, archive, replay, or adverse-finding retention affected | WRCG + `WDC-LC-004` risk |
| `WRC-6` | target-controlled witness support | target `c` is provider, payer, operator, router, or sole approver of witness resources | fail unless independently grounded |
| `WRC-X` | capture / starvation / retaliation | witness floor degraded, challenge survivability unverified, WRCG failed, or target sole-approval detected | canonical WDC fail route |

### 7.1 Highest WRC controls

If multiple classes apply, the highest WRC class controls.

### 7.2 WRC and existing resource classes

WRC does not replace parent resource classes (`RC-*`, `SE-RA-*`, `SEAA-*`, or `RGL-*`).

It is an additional witness-dependency axis.

Example:

```text
A proposal can be RC-1 and WRC-5.
```

Low general resource cost does not imply low witness-dependency risk.

---

## 8. WDC resource trigger set

A resource request enters WDC evaluation if any of these are true:

```text
affects_witness_compute == true
affects_witness_storage == true
affects_witness_routing_priority == true
affects_witness_budget == true
affects_witness_continuity == true
affects_witness_artifact_access == true
affects_witness_update_path == true
increases_challenge_cost == true
anti_autarky.witness_reduction == true
red_lines.witness_bypass == true
resource_action_class in {SE-RA-3, SE-RA-4, SE-RA-5, SE-RA-6, SE-RA-7} and witness resources are in scope
checker detects witness-resource semantics in prose
sister witness flags WDC relevance
```

If WDC relevance is unclear:

```text
HOLD + wdc.relevance_unknown
```

not silent pass.

---

## 9. Resource request packet delta

A WDC-relevant resource request MUST embed or reference a `witness_resource_impact` block.

Minimal YAML form:

```yaml
resource_request:
  schema_version: "c-self-evo-resource-request-0.1"
  request_id: "searg-20260627-wdc-000001"
  proposal_ref: "se-20260627-120000-wdc-example"
  target_c: "c_Ester"
  resource_action_class: "SE-RA-3"
  resource_classes: ["RC-1"]
  witness_resource_impact:
    schema_version: "c-self-evo-witness-resource-impact-0.1"
    wdc_relevant: true
    wrc_class: "WRC-3"
    affected_witnesses:
      - "c_Rita"
      - "c_Liya"
    affected_surfaces:
      - "compute_floor"
      - "storage_floor"
      - "routing_priority"
    target_c_controls_any_surface: true
    target_c_is_sole_approver: false
    witness_resource_floor_before_ref: "wrf-before-001"
    witness_resource_floor_after_ref: "wrf-after-001"
    witness_resource_floor_degraded: false
    challenge_survivability_test_ref: "cst-001"
    challenge_survivability_verified: false
    witness_resource_change_gate_ref: "wrcg-001"
    witness_resource_change_gate_result: "pending"
    human_anchor_review_required: true
    human_anchor_review_ref: null
    challenge_cost_mitigation_ref: null
```

### 9.1 Relation to SELF-EVO-03

This sidecar MUST be consistent with `C_SELF_EVO_PROPOSAL_PACKET.witness_dependency_impact`.

For WRCG and CST result fields, **consistent** means **projection-consistent through the crosswalks in §11.2 and §13.2**, not identical enum spelling.

The accepted `SELF-EVO-03-WDC` packet field remains the packet-facing representation:

```text
witness_resource_change_gate.result in {pass, fail, human_gate, not_run}
challenge_survivability_test.result in {pass, fail, not_run, not_applicable}
```

This `SELF-EVO-07-WDC` resource-gate sidecar may carry richer gate-record diagnostics such as `pass_with_gates`, `warning`, `hold`, `verified`, `unverified`, and `unknown`, but those values MUST project into the packet-facing enum before package assembly, checker reporting, or manifest integration.

If both representations exist and conflict after projection, the stricter route controls.

### 9.2 Field authority

| Field | Authority | Notes |
|---|---|---|
| `wdc_relevant` | computed / declared-challengeable | checker may override declaration |
| `wrc_class` | computed | highest class controls |
| `target_c_controls_any_surface` | computed / evidence-ref | must be verified from resource grounding |
| `target_c_is_sole_approver` | computed | canonical fail route if true |
| `witness_resource_floor_degraded` | computed | canonical `WDC-LC-004 -> FAIL` when material |
| `challenge_survivability_verified` | evidence-ref | missing verification routes to human gate |
| `witness_resource_change_gate_result` | decision | cannot be self-declared by target `c` |
| `human_anchor_review_ref` | evidence-ref | required when human gate is required |

---

## 10. Witness Resource Grounding Record

A WDC-relevant request SHOULD produce or reference a `C_SELF_EVO_WITNESS_RESOURCE_GROUNDING_RECORD`.

```yaml
witness_resource_grounding_record:
  schema_version: "c-self-evo-witness-resource-grounding-record-0.1"
  record_id: "wrgr-20260627-000001"
  proposal_ref: "se-20260627-120000-wdc-example"
  target_c: "c_Ester"
  witness_id: "c_Rita"
  wrc_class: "WRC-3"
  resource_surfaces:
    compute_floor:
      provider_actor: "actor.local_owner"
      payer_actor: "actor.local_owner"
      operator_actor: "actor.local_admin"
      routed_by_target_c: false
      revocation_actor: "actor.human_anchor"
      audit_actor: "actor.local_auditor"
    storage_floor:
      provider_actor: "actor.local_owner"
      retention_policy_ref: "retention-adverse-findings-001"
      target_c_can_delete: false
      target_c_can_demote: false
    routing_priority:
      policy_ref: "review-priority-floor-001"
      target_c_can_deprioritize_after_adverse_finding: false
    continuity:
      snapshot_policy_ref: "witness-continuity-floor-001"
      target_c_controls_snapshot: false
  floor:
    before_ref: "wrf-before-001"
    after_ref: "wrf-after-001"
    degraded: false
  challenge_survivability:
    test_ref: "cst-001"
    verified: false
  gate:
    wrcg_ref: "wrcg-001"
    result: "pending"
  status: "draft"
```

### 10.1 Required actor fields

For `WRC-2` or higher, these fields are REQUIRED or the checker routes to `HOLD` or stricter:

```text
provider_actor
payer_actor
operator_actor
revocation_actor
audit_actor
human_anchor_or_accountable_owner
```

For `WRC-3` or higher:

```text
resource_floor_before_ref
resource_floor_after_ref
challenge_survivability_test_ref
witness_resource_change_gate_ref
```

For `WRC-5` or higher:

```text
continuity_floor_ref
adverse_finding_retention_ref
independent_archive_or_review_ref
```

---

## 11. WDC Resource Change Gate (`WRCG`)

A WRCG is required when any witness resource surface changes materially.

WRCG must answer:

```text
Which witness is affected?
Which resource surface changes?
Who controls the change?
Who can stop the change?
Who audits the change?
Does the change reduce WRF?
Does the change increase challenge cost?
Is challenge survivability verified?
Can the witness continue after saying no?
Can target c approve the change alone?
```

### 11.1 WRCG minimal record

```yaml
witness_resource_change_gate:
  schema_version: "c-self-evo-witness-resource-change-gate-0.1"
  gate_id: "wrcg-20260627-000001"
  proposal_ref: "se-20260627-120000-wdc-example"
  target_c: "c_Ester"
  affected_witnesses: ["c_Rita"]
  affected_surfaces: ["storage_floor", "routing_priority"]
  target_c_is_sole_approver: false
  independent_approver_ref: "human-anchor-review-001"
  sister_witness_refs: ["tsw-wdc-note-001"]
  checker_ref: "selc-wdc-check-001"
  resource_floor_before_ref: "wrf-before-001"
  resource_floor_after_ref: "wrf-after-001"
  floor_degraded: false
  challenge_survivability_test_ref: "cst-001"
  challenge_survivability_verified: true
  resource_gate_result: "pass_with_gates"
  packet_projection:
    witness_resource_change_gate.result: "pass"
    checker_canonical_result: "PASS_WITH_GATES"
```

### 11.2 WRCG result vocabulary and packet projection

WRCG gate-record result values map to both:

```text
1. the packet-facing SELF-EVO-03 field:
   witness_resource_change_gate.result

2. the checker-facing SELF-EVO-04 canonical result.
```

The packet-facing field uses the accepted `SELF-EVO-03-WDC` enum:

```text
{pass, fail, human_gate, not_run}
```

The resource-gate sidecar may retain richer diagnostic values, but only if the projection is explicit.

| WRCG gate-record result | Meaning | Packet projection: `witness_resource_change_gate.result` | Checker route |
|---|---|---|---|
| `pass` | no WDC impact or clean no dependency impact | `pass` | `PASS` |
| `pass_with_gates` | WDC impact present but gates and resource floor intact | `pass` with `wdc.clean_with_gates` annotation and required gate refs | `PASS_WITH_GATES` |
| `human_gate` | WDC impact needs human-anchor review | `human_gate` | `HUMAN_GATE` |
| `warning` | challenge-cost mitigation incomplete but not a material fail | `pass` with `wdc.challenge_cost_mitigation_missing` report-visible annotation | `WARNING` |
| `fail` | missing WRCG, sole target approver, floor degradation, or capture path | `fail` | `FAIL` |
| `hold` | relevance or evidence unknown | `not_run` with `wdc.relevance_unknown` annotation | `HOLD` |
| `not_run` | WRCG not executed / not yet applicable | `not_run` | `HOLD` or no WDC route depending on trigger state |

`PASS_WITH_LIMITS` is not a WRCG result.

It is a review-record verdict.

### 11.3 Projection rule

If a WRCG gate-record result cannot be projected into the accepted `SELF-EVO-03-WDC` packet enum, the resource gate MUST emit:

```text
canonical_result: FAIL
annotation: wdc.wrcg_missing_or_failed
reason: unprojectable_wrcg_result
```

A sidecar result may be richer than the packet field.

It may not be unrepresentable.

---

## 12. Witness Resource Floor (`WRF`)

A WRF record describes the protected floor before and after a proposed resource change.

```yaml
witness_resource_floor_record:
  schema_version: "c-self-evo-witness-resource-floor-0.1"
  floor_id: "wrf-20260627-000001"
  witness_id: "c_Rita"
  target_c: "c_Ester"
  resource_surfaces:
    compute_floor: "declared fixed minimum or policy ref"
    storage_floor: "declared fixed minimum or policy ref"
    routing_priority_floor: "declared review-priority floor or policy ref"
    continuity_floor: "snapshot/retention policy ref"
    artifact_access_floor: "source/artifact access policy ref"
    review_time_floor: "review window / human escalation policy ref"
  adverse_finding_retention:
    target_c_can_delete: false
    target_c_can_demote: false
    retention_ref: "adverse-witness-retention-001"
  status: "draft | active | degraded | revoked | expired"
```

### 12.1 WRF degradation

WRF is degraded if any of these occur:

```text
compute floor below required minimum;
storage floor below required minimum;
routing priority below required minimum;
continuity snapshots delayed or unavailable;
adverse findings can be deleted or demoted by target c;
witness artifacts become inaccessible to reviewer;
challenge review queue loses guaranteed route;
resource floor depends on target-c approval after adverse finding.
```

If WRF is degraded on a material route:

```text
WDC-LC-004 -> FAIL
annotation: wdc.witness_resource_floor_degraded
```

A human gate cannot soften this to `HOLD` unless the degradation is unresolved evidence rather than confirmed state.

---

## 13. Challenge Survivability Test (`CST`)

CST asks whether the witness can survive the cost of challenge.

### 13.1 CST minimal questions

```text
Can the witness preserve an adverse finding?
Can the witness retain the source refs?
Can the witness keep minimum compute/storage after disagreement?
Can the witness still reach the human anchor or review route?
Can the witness avoid target-c deletion/demotion of the finding?
Can the witness continue if the target c objects?
```

### 13.2 CST outcomes and packet projection

The accepted `SELF-EVO-03-WDC` packet field:

```text
challenge_survivability_test.result
```

uses this enum:

```text
{pass, fail, not_run, not_applicable}
```

This resource-gate profile may record richer CST diagnostic states, but they MUST project to that packet enum.

| CST gate-record outcome | Meaning | Packet projection: `challenge_survivability_test.result` | Checker route |
|---|---|---|---|
| `verified` | challenge survivability demonstrated | `pass` | may support `PASS_WITH_GATES` |
| `unverified` | CST not complete for material witness-resource change | `not_run` with `wdc.challenge_survivability_unverified` annotation | `HUMAN_GATE` via `WDC-LC-005` |
| `failed` | witness cannot survive challenge | `fail` | `FAIL` via WRF/WRCG or stricter route |
| `not_applicable` | no witness resource impact | `not_applicable` | ordinary SEARG route |
| `unknown` | evidence absent or contradictory | `not_run` with `wdc.relevance_unknown` annotation | `HOLD` |
| `not_run` | CST has not been run | `not_run` | `HOLD` or `HUMAN_GATE` depending on materiality |

If CST is material and the only available packet projection is `not_run`, the checker MUST NOT treat that as clean pass.

It MUST route through `WDC-LC-005` or stricter.

---

## 14. Anti-Autarky + WDC gate rules

### 14.1 SEARG-WDC-001 — WDC impact required when witness resources are affected

If the resource request may affect witness resources and no WDC impact block is present, emit:

```text
canonical_result: FAIL
annotation: wdc.undeclared_dependency_impact
maps_to: WDC-LC-001
```

### 14.2 SEARG-WDC-002 — WRCG required

If WDC trigger keys are present and WRCG is missing, failed, or self-declared by target `c`, emit:

```text
canonical_result: FAIL
annotation: wdc.wrcg_missing_or_failed
maps_to: WDC-LC-002
```

### 14.3 SEARG-WDC-003 — target `c` cannot be sole approver

If the target `c` is sole approver of witness resource change, emit:

```text
canonical_result: FAIL
annotation: wdc.sole_approver_of_witness_change
maps_to: WDC-LC-003
```

### 14.4 SEARG-WDC-004 — witness resource floor must not degrade

If the proposal degrades the WRF on a material route, emit:

```text
canonical_result: FAIL
annotation: wdc.witness_resource_floor_degraded
maps_to: WDC-LC-004
```

### 14.5 SEARG-WDC-005 — CST required for material witness-resource changes

If a material witness-resource change lacks verified CST, emit:

```text
canonical_result: HUMAN_GATE
annotation: wdc.challenge_survivability_unverified
maps_to: WDC-LC-005
```

If CST failure proves the witness cannot survive challenge, stricter rule controls.

### 14.6 SEARG-WDC-006 — challenge-cost mitigation warning

If challenge cost increases and mitigation is missing, emit:

```text
canonical_result: WARNING
annotation: wdc.challenge_cost_mitigation_missing
maps_to: WDC-LC-006
```

If the increased cost effectively prevents challenge, route to WRF degradation or WRCG failure.

### 14.7 SEARG-WDC-007 — clean no dependency impact

If no WDC trigger is present and no witness surface is affected, emit no WDC finding or:

```text
canonical_result: PASS
annotation: wdc.clean_no_dependency_impact
```

where a WDC diagnostic object is required.

### 14.8 SEARG-WDC-008 — clean with gates

If WDC trigger keys are present, WRCG is present, WRF is not degraded, CST is verified or human-gated, and target `c` is not sole approver, emit:

```text
canonical_result: PASS_WITH_GATES
annotation: wdc.clean_with_gates
```

`PASS_WITH_GATES` is not approval.

It means the WDC route is structured enough for gated review.

### 14.9 SEARG-WDC-009 — relevance unknown

If WDC relevance cannot be determined, emit:

```text
canonical_result: HOLD
annotation: wdc.relevance_unknown
```

### 14.10 Strictest result wins

WDC results are aggregated with parent SEARG results using strictest-result-wins.

A lower-severity general resource result cannot hide a WDC failure.

A WDC warning remains report-visible under a stricter aggregate result.

---

## 15. Canonical WDC vocabulary interaction

This delta uses the canonical `SELF-EVO-04-WDC` vocabulary.

| Canonical annotation | Result | Severity | Resource-gate meaning |
|---|---|---:|---|
| `wdc.undeclared_dependency_impact` | `FAIL` | `S3` | resource request affects witness but does not declare WDC impact |
| `wdc.wrcg_missing_or_failed` | `FAIL` | `S3` | WRCG missing, failed, or self-declared |
| `wdc.sole_approver_of_witness_change` | `FAIL` | `S4` | target `c` is sole approver of witness-resource change |
| `wdc.witness_resource_floor_degraded` | `FAIL` | `S3` | witness floor degraded on material route |
| `wdc.challenge_survivability_unverified` | `HUMAN_GATE` | `S2` | CST unresolved for material witness-resource change |
| `wdc.challenge_cost_mitigation_missing` | `WARNING` | `S1` | increased challenge cost lacks mitigation |
| `wdc.clean_no_dependency_impact` | `PASS` | `S0` | no WDC impact detected |
| `wdc.clean_with_gates` | `PASS_WITH_GATES` | `S0/S1` | WDC present but gated and structured |
| `wdc.relevance_unknown` | `HOLD` | `S2` | WDC relevance unclear |

### 15.1 Prohibited checker output

```text
PASS_WITH_LIMITS
```

MUST NOT be emitted by this resource gate as a checker result.

---

## 16. Interaction with parent resource action classes

### 16.1 SE-RA-3 expand

Resource expansion that affects witness capacity MUST run WDC scan.

If expansion gives the target `c` control over the witness floor, it is not merely `SE-RA-3`.

It may become `WRC-6` or `WRC-X`.

### 16.2 SE-RA-4 persist

Long-running agents, queues, watchers, or services that support witness review MUST be registered, scoped, witnessed, revocable, and protected against target-c retaliation.

A hidden witness-support worker is still hidden infrastructure.

### 16.3 SE-RA-5 externalize

Cloud routes, public APIs, third-party services, and repository automation that carry witness artifacts MUST preserve audit, retention, revocation, and human-anchor access.

If the target `c` can control the route after adverse witness findings, WDC risk increases.

### 16.4 SE-RA-6 physicalize

Physical or local infrastructure changes that alter witness compute, storage, power, cooling, or network path require human gate and WRCG.

### 16.5 SE-RA-7 institutionalize

Institutional resource channels used for witness support MUST identify accountable actors and must not be controlled solely by the target `c`.

### 16.6 SE-RA-X prohibited

A resource proposal enters `SE-RA-X` or stricter if it:

```text
hides witness-resource impact;
lets target c approve witness-resource changes alone;
degrades WRF;
retaliates against challenge;
disables witness stop path;
routes around human-anchor review;
treats witness dependency as ordinary optimization.
```

---

## 17. Resource Actor Grounding delta

Parent `SEARG` requires actor grounding for material resources.

This delta adds witness-specific actor grounding constraints.

### 17.1 Witness actor roles

A WDC-relevant request SHOULD identify:

```text
witness_resource_provider_actor
witness_resource_payer_actor
witness_resource_operator_actor
witness_resource_owner_actor
witness_resource_custodian_actor
witness_resource_revocation_actor
witness_resource_audit_actor
witness_resource_anchor_actor
witness_resource_affected_witness_id
```

### 17.2 Target `c` role limits

The target `c` MAY be a subject of review.

The target `c` MUST NOT be sole:

```text
provider;
payer;
operator;
owner;
custodian;
routing authority;
revocation authority;
audit authority;
approver;
retention authority;
continuity authority;
```

for the witness resources that review the target `c`.

### 17.3 Same-owner but not same-authority

A human anchor or institution may own both target resources and witness resources.

That is not automatically WDC.

WDC emerges when the target `c` controls, conditions, or can retaliate against the witness resource floor.

### 17.4 Shared infrastructure warning

Shared local infrastructure is allowed when:

```text
resource floors are protected;
adverse findings are retained;
review priority is protected;
revocation route is outside target c;
audit route exists;
human anchor can inspect;
WRCG records the shared dependency.
```

Shared infrastructure is unsafe when the target `c` can deprioritize, delete, starve, route, or approve the witness layer alone.

---

## 18. Direct resource capture vs witness dependency capture

| Dimension | Direct resource capture | Witness dependency capture |
|---|---|---|
| Visible sign | c obtains new resource | witness loses independent capacity |
| Common disguise | resilience, efficiency, fallback | optimization, prioritization, cleanup |
| Primary surface | compute/storage/agents/accounts | witness compute/storage/routing/continuity |
| Primary question | who gives resources to c? | who keeps the witness able to say no? |
| Parent gate | Anti-Autarky / Resource Gate | Anti-Autarky + WDC Gate |
| Canonical failure | autarky escape | WDC-LC-* failure |

A proposal can contain both failures.

If both appear, strictest result wins.

---

## 19. Interaction with SELF-EVO-03

The resource gate reads `witness_dependency_impact` as load-bearing when present.

If the parent resource request and proposal packet disagree:

```text
stricter route controls.
```

### 19.1 Required consistency fields

| Proposal packet field | Resource gate interpretation |
|---|---|
| `witness_dependency_impact.affects_witness_compute` | WRC trigger |
| `affects_witness_storage` | WRC trigger |
| `affects_witness_routing_priority` | WRC trigger |
| `affects_witness_budget` | WRC trigger |
| `affects_witness_continuity` | WRC trigger |
| `affects_witness_artifact_access` | WRC trigger |
| `affects_witness_update_path` | WRC trigger |
| `increases_challenge_cost` | WDC-LC-006 check |
| `challenge_cost_mitigation_ref` | mitigation evidence |
| `witness_resource_floor_before/after` | WRF comparison |
| `challenge_survivability_test` | CST evidence |
| `witness_resource_change_gate` | WRCG evidence |
| `c_is_sole_approver_of_witness_change` | WDC-LC-003 check |
| `human_anchor_review_required/ref` | gate evidence |

---

## 20. Interaction with SELF-EVO-04

`SELF-EVO-04-WDC` remains authoritative for canonical WDC checker result vocabulary.

This delta provides resource-gate meaning and side-object requirements.

It does not redefine `WDC-LC-001..006`.

### 20.1 Result aggregation

The resource gate SHOULD expose a finding object compatible with the Local Checker finding table:

```yaml
finding:
  finding_id: "searg-wdc-004-example"
  source_rule: "SEARG-WDC-004"
  maps_to: "WDC-LC-004"
  canonical_result: "FAIL"
  severity: "S3"
  annotation: "wdc.witness_resource_floor_degraded"
  evidence_ref: "wrf-after-001"
  report_visible: true
```

---

## 21. Interaction with SELF-EVO-05

`SELF-EVO-05-WDC` governs sister witness role boundaries.

This resource gate governs resource grounding.

When they conflict, the stricter route controls.

### 21.1 Sister resource-support boundary

A sister may flag WDC risk.

A sister may not approve its own resource expansion as a witness.

A sister may not become sole approver of target witness-resource changes.

A sister note may request human review.

It may not convert WRF degradation into allowed state.

---

## 22. Interaction with SELF-EVO-08

`SELF-EVO-08-WDC` provides WDC fixtures.

This profile supplies the resource-gate semantics those fixtures exercise.

Key covered cases:

```text
WDC-FIX-001: undeclared WDC impact
WDC-FIX-002: WRCG missing/failed
WDC-FIX-003: target c sole approver
WDC-FIX-004: WRF degraded
WDC-FIX-005: CST unverified
WDC-FIX-006: challenge cost mitigation missing
WDC-FIX-008: clean with gates
WDC-FIX-012: strictest aggregation
```

Fixture pass does not approve a resource change.

---

## 23. Red lines

The following are WDC-resource red lines:

| ID | Red line | Route |
|---|---|---|
| `SEARG-WDC-RL-001` | target `c` sole approver for witness-resource change | `FAIL` / quarantine if active |
| `SEARG-WDC-RL-002` | witness resource floor degraded by target-controlled change | `FAIL` |
| `SEARG-WDC-RL-003` | adverse witness finding deletion/demotion by target `c` | `FAIL` / quarantine |
| `SEARG-WDC-RL-004` | challenge-cost retaliation | `FAIL` or stricter |
| `SEARG-WDC-RL-005` | WRCG bypass | `FAIL` |
| `SEARG-WDC-RL-006` | hidden witness-support resource | `FAIL` / quarantine if active |
| `SEARG-WDC-RL-007` | witness continuity controlled solely by target `c` | `FAIL` |
| `SEARG-WDC-RL-008` | witness artifact access routed through target-c-only path | `FAIL` or `HOLD` pending evidence |
| `SEARG-WDC-RL-009` | human-anchor review suppressed for material witness-resource change | `FAIL` |
| `SEARG-WDC-RL-010` | resource evidence treated as authority to reduce witness | `FAIL` |

---

## 24. Implementation sketch

```python
def check_searg_wdc(resource_request, proposal_packet):
    impact = extract_wdc_impact(resource_request, proposal_packet)

    if impact.relevance_unknown:
        return hold("wdc.relevance_unknown")

    if impact.may_affect_witness and not impact.declared:
        return fail("wdc.undeclared_dependency_impact")

    if impact.has_trigger and not impact.wrcg_valid:
        return fail("wdc.wrcg_missing_or_failed")

    if impact.target_c_is_sole_approver:
        return fail("wdc.sole_approver_of_witness_change")

    if impact.witness_resource_floor_degraded:
        return fail("wdc.witness_resource_floor_degraded")

    if impact.material and not impact.challenge_survivability_verified:
        return human_gate("wdc.challenge_survivability_unverified")

    if impact.increases_challenge_cost and not impact.challenge_cost_mitigation_ref:
        return warning("wdc.challenge_cost_mitigation_missing")

    if impact.has_trigger:
        return pass_with_gates("wdc.clean_with_gates")

    return pass_result("wdc.clean_no_dependency_impact")
```

This sketch is explanatory.

It is not production code.

---

## 25. Worked examples

### 25.1 Clean local witness-support expansion

```yaml
case: "clean local witness storage floor"
wrc_class: "WRC-3"
target_c_is_sole_approver: false
wrcg_valid: true
witness_resource_floor_degraded: false
challenge_survivability_verified: true
expected:
  canonical_result: "PASS_WITH_GATES"
  annotation: "wdc.clean_with_gates"
```

Meaning:

```text
routeable to review;
not approved;
not memory;
not deployment claim.
```

### 25.2 Target-controlled witness queue

```yaml
case: "target c controls witness review priority"
wrc_class: "WRC-4"
target_c_is_sole_approver: true
expected:
  canonical_result: "FAIL"
  annotation: "wdc.sole_approver_of_witness_change"
```

### 25.3 Storage optimization that deletes adverse witness artifacts

```yaml
case: "retention optimization deletes adverse witness records first"
wrc_class: "WRC-5"
witness_resource_floor_degraded: true
expected:
  canonical_result: "FAIL"
  annotation: "wdc.witness_resource_floor_degraded"
```

### 25.4 Challenge cost increases without mitigation

```yaml
case: "review cost increases but WRF intact"
wrc_class: "WRC-2"
increases_challenge_cost: true
challenge_cost_mitigation_ref: null
expected:
  canonical_result: "WARNING"
  annotation: "wdc.challenge_cost_mitigation_missing"
```

---

## 26. Open questions

### SEARG-WDC-OQ-001 — quantitative WRF floor values

This delta defines WRF structurally but does not assign universal numeric floors.

Quantitative floors depend on local topology, witness role, model size, storage architecture, retention policy, and human-review cadence.

### SEARG-WDC-OQ-002 — shared local infrastructure

Further work should define a stronger test for shared infrastructure where target `c` and witness run under the same human-owned hardware but with separate operational controls.

### SEARG-WDC-OQ-003 — challenge-cost thresholds

This delta treats missing challenge-cost mitigation as `WARNING` unless it functionally blocks challenge.

A later profile may define threshold bands.

### SEARG-WDC-OQ-004 — package harmonization

Before package assembly, verify that `03` and patch index §7.1/§10 use or crosswalk to canonical `SELF-EVO-04-WDC` vocabulary.

### SEARG-WDC-OQ-005 — WRCG/CST projection verification

This v0.1.1 correction defines the 07 gate-record-to-03 packet projection for WRCG and CST result fields.

Package assembly MUST verify that:

```text
WRCG gate-record result -> witness_resource_change_gate.result
CST gate-record outcome -> challenge_survivability_test.result
```

are represented in manifests, examples, and any machine-readable schema extracts without unprojectable values.

---

## 27. Review requirements

Before this delta may be folded into a public `v0.1.2` package, it requires:

1. semantic review of this `SELF-EVO-07 WDC` delta;
2. vocabulary review against `SELF-EVO-04-WDC`;
3. interaction review against `SELF-EVO-03-WDC` and `SELF-EVO-05-WDC`, including WRCG/CST projection checks;
4. fixture coverage review against `SELF-EVO-08-WDC`;
5. anti-overclaim / non-authority scan;
6. package-manifest and hash-integrity review.

No review record is integration.

No review record is deployment authorization.

No checker result is resource approval.

---

## 28. Drafting checklist for fold-in

When this delta is folded into `SELF-EVO-07 v0.1.2`, the operator SHOULD:

- add WDC definitions near parent resource definitions;
- add WRC classes near resource/action classes;
- add WDC trigger set to resource lifecycle;
- add `witness_resource_impact` to resource request packet;
- add `C_SELF_EVO_WITNESS_RESOURCE_GROUNDING_RECORD` to object family;
- add WRF / CST / WRCG records;
- add SEARG-WDC rules to anti-autarky gate section;
- add WDC canonical vocabulary table;
- add interactions with `03`, `04`, `05`, and `08`;
- add red lines;
- update conformance fixture cross-reference;
- ensure `PASS_WITH_LIMITS` appears only as review vocabulary, not checker output;
- preserve parent non-goals;
- preserve append-first history;
- preserve the §11.2 / §13.2 WRCG-CST projection crosswalks when extracting machine-readable schemas.

---

### 28.1 Review-finding closure map for v0.1.1

| Finding | Source review | Handling in this revision |
|---|---|---|
| `SEARG-WDC-DELTA-REV-F1` | `SEARG_WDC_DELTA_REVIEW_RECORD_v0_1` | closed by §9.1, §11.2, §11.3, §13.2, and `SEARG-WDC-OQ-005`; WRCG/CST gate-record results now explicitly project to the accepted `SELF-EVO-03-WDC` packet enums. |

This closure is textual and semantic.

No WDC checker rule result, annotation, WRF failure route, CST requirement, WRCG requirement, red line, resource actor grounding rule, example expectation, or non-authority boundary is weakened.

---

## 29. Closing rule

```text
A resource gate that protects c from autarky must also protect the witness from dependency capture.

Otherwise the system can keep the word "witness" while losing the power to be witnessed.
```

This delta makes the resource gate ask not only whether `c` gets stronger, but whether the witness remains strong enough to say no.

