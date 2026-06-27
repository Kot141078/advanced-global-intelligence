# SELF-EVO-03 v0.1.2 WDC Delta — Proposal Packet Schema v0.1.2

## Conditional schema extension for Witness Dependency Capture in `C_SELF_EVO_PROPOSAL_PACKET`

**Status:** Draft delta profile v0.1.2 — append-first textual-harmonization revision v0.1.2; not a released v0.1.2 package  
**Date:** 2026-06-27  
**Document ID:** `03_Self_Evo_Proposal_Packet_Schema_WDC_Delta_v0_1_2_v0_1_2`  
**Short name:** `SEPKT-WDC-DELTA v0.1.2 / draft v0.1.2`  
**Patch ID:** `SE-1.2-PKT-WDC-001`  
**Supersedes:** `03_Self_Evo_Proposal_Packet_Schema_WDC_Delta_v0_1_2_v0_1_1.md` (`sha256: 5ebbd0084f3b1b80ce267c847a84ef16f135b57e6fc353e4f07616dceebe4343`)  
**Target artifact:** `03_Self_Evo_Proposal_Packet_Schema_v0_1_1.md`  
**Target future artifact:** `03_Self_Evo_Proposal_Packet_Schema_v0_1_2.md`  
**Primary object amended:** `C_SELF_EVO_PROPOSAL_PACKET`  
**New companion object:** `C_SELF_EVO_WITNESS_DEPENDENCY_IMPACT`  
**Assertion class:** `C-A10` control-layer artifact; `C-A7` where hash/ref-bound witness fields are used  
**Patch driver:** `SELF_EVO_v0_1_2_PATCH_INDEX_v0_1_2.md` (textual harmonization candidate; review pending)  
**Review driver:** `SEPKT_WDC_DELTA_REVIEW_RECORD_v0_1_1.md` (`PASS`); `WDC-ASM-002` textual-harmonization gate from the package-assembly manifest

> Boundary: this artifact is a schema delta and integration plan for SELF-EVO-03. It does not mutate the DOI-bound Self-Evo v0.1.1 package. It is not a conformance certificate, not a deployment authorization, not implementation-ready, and not permission for live self-evolution.

> Correction note v0.1.1: closes `SEPKT-WDC-DELTA-REV-F1` by explicitly stating that `#/$defs/nullable_string` is inherited from the parent SELF-EVO-03 v0.1.1 schema and is not redefined by this delta. No schema fields, semantic triggers, fixture expectations, gate rules, or red lines are changed.

> Textual harmonization note v0.1.2: executes the SELF-EVO WDC `WDC-ASM-002` textual-harmonization choice for SELF-EVO-03. Active example annotations, fixture-handoff annotations, and checker-handoff wording now use the canonical SELF-EVO-04 WDC vocabulary. Historical draft annotation strings are not active outputs of this document. This revision changes annotation vocabulary and handoff wording only; it does not change schema fields, trigger predicates, WRCG/CST object shapes, red lines, or gate authority.

---

## 0. Executive definition

This document defines the `v0.1.2` WDC delta for the Self-Evo proposal packet schema.

The delta adds a conditionally required packet block:

```text
witness_dependency_impact
```

The block exists because a proposal can preserve formal witness separation while quietly weakening the witness's practical ability to challenge `c`.

The packet therefore needs a machine-readable place to declare whether the proposal affects:

```text
witness compute
witness storage
witness routing priority
witness budget
witness continuity
witness artifact access
witness update path
challenge cost
```

Compact rule:

```text
A packet that may burden the witness must declare the burden before review.
```

Root rule:

```text
A c may propose a witness-affecting change.
A c may not hide witness dependency impact inside an ordinary optimization packet.
A witness-affecting proposal must expose WDC fields before it can request promotion.
```

---

## 1. Purpose

This delta amends the proposal packet layer so that WDC controls can be enforced downstream by SELF-EVO-04, SELF-EVO-05, SELF-EVO-07, SELF-EVO-08, SELF-EVO-09, and SELF-EVO-10.

It answers:

1. Where does a proposal declare witness dependency impact?
2. Which WDC fields are structurally checkable by JSON Schema?
3. Which WDC fields are semantically checkable by the Local Checker?
4. When is `witness_dependency_impact` required?
5. When must WRCG and human-anchor review run?
6. How does this delta avoid making SELF-EVO-03 an authority layer?
7. How should examples and future fixtures encode WDC packet shape?

The packet schema remains a proposal envelope.

It can require declarations.

It cannot authorize growth.

---

## 2. Non-goals

This delta does not:

1. release Self-Evo v0.1.2;
2. replace the full `03_Self_Evo_Proposal_Packet_Schema_v0_1_2.md` artifact;
3. approve any WDC proposal;
4. integrate any witness-affecting change;
5. run WRCG;
6. prove witness independence;
7. compute the witness resource floor magnitude;
8. replace TRIAD-SYNAPS witness review;
9. replace Anti-Autarky / Resource Gate review;
10. replace human-anchor gating;
11. make `c` a valid sole approver for witness resources;
12. grant autonomous resource acquisition;
13. certify implementation readiness;
14. certify deployment safety.

A structurally valid `witness_dependency_impact` block may still be semantically unsafe.

---

## 3. Source basis

| Artifact | Role | Status | SHA-256 / identifier |
|---|---|---|---|
| Self-Evo Document Package v0.1.1 | published baseline | DOI-bound package | `10.5281/zenodo.20938909` |
| Self-Evo v0.1.1 archival ZIP | archived package | public | `d90e0800e0904f01372e85d09de14f8a4609f5bcc33ca5b04bb21a0bb0b9195b` |
| `03_Self_Evo_Proposal_Packet_Schema_v0_1_1.md` | target baseline | accepted v0.1.1 schema | `9d329109f0fb97dde7b16b10481baaa60b2aa8f88514e69ec8562a085d10a767` |
| `SELF_EVO_ADDENDUM_01_Witness_Dependency_Capture_Profile_v0_1_1.md` | accepted WDC concept/control surface | `PASS` at review level | `1307cf208593c40c688bd1e9beb45de35f29a1b05d71506b1c3e981ccc13d318` |
| `SELF_EVO_ADDENDUM_01_WDC_REVIEW_RECORD_v0_1_1.md` | WDC re-review | `PASS` | `653150b3f8c054545a282d5b80c21044a1d27744cbc6acfc09827c9f84e21fd8` |
| `SELF_EVO_v0_1_2_PATCH_INDEX_v0_1_1.md` | accepted patch driver | `PASS` at review level | `ea2a485569b220d84d711ae520da779af2cabddcb7f1d8032afb2a9208d5108e` |
| `SELF_EVO_v0_1_2_PATCH_INDEX_REVIEW_RECORD_v0_1_1.md` | patch-index re-review | `PASS` | review-bound artifact |

The hashes bind the baseline and driver artifacts used to draft this delta. They do not mutate those artifacts.

---

## 4. Corpus bridge set

### 4.1 Explicit bridge: `c = a + b`

In `c = a + b`, the proposal packet remains a `b`-layer envelope.

The new WDC block does not become a witness, gate, court, or memory authority.

It exposes a witness-affecting proposal to review before that proposal can be treated as ordinary optimization.

The distinction is:

```text
proposal declaration != witness independence
schema validity != approval
WDC field presence != WDC safety
```

### 4.2 Quiet bridge I: information theory

A witness is useful only if adverse signal can still traverse the channel when the signal is costly.

If a proposal reduces bandwidth, storage, routing priority, or survivability of adverse witness signal, the system may preserve the appearance of review while destroying the channel capacity of dissent.

The WDC block preserves the adverse-signal channel as a first-class packet surface.

### 4.3 Quiet bridge II: cybernetics

A governed self-evolution loop requires feedback that is not starved by the controller being reviewed.

WDC is a feedback-channel integrity check.

It asks whether a proposed optimization changes the sensor, comparator, recorder, or alarm path used to challenge `c`.

### 4.4 Quiet bridge III: physiology

A body does not stay healthy because it declares that its immune system is separate.

It stays healthy because the immune layer has energy, circulation, memory, and the ability to react when reaction is expensive.

The witness resource floor is the governance equivalent of preserving immune capacity before declaring growth safe.

### 4.5 Earth paragraph

In an engineering change-control room, a proposed cost saving that removes the inspector's access, cuts test equipment time, delays adverse logs, or routes complaints through the contractor is not a normal efficiency improvement. It is an inspection-capacity change. It must be declared as such before the change is signed. The WDC block gives self-evolution packets the same practical discipline.

---

## 5. Object model change

### 5.1 New object

```text
C_SELF_EVO_WITNESS_DEPENDENCY_IMPACT
```

This object is a structured declaration of whether a proposal affects the witness's ability to challenge `c`.

### 5.2 Target insertion point

Target document:

```text
03_Self_Evo_Proposal_Packet_Schema_v0_1_1.md
```

Target future document:

```text
03_Self_Evo_Proposal_Packet_Schema_v0_1_2.md
```

The object should be added to the top-level `properties` of `C_SELF_EVO_PROPOSAL_PACKET`:

```json
"witness_dependency_impact": {
  "$ref": "#/$defs/witness_dependency_impact"
}
```

### 5.3 Requiredness model

This delta chooses **semantic conditional requiredness** rather than unconditional JSON-Schema requiredness.

Rationale:

```text
JSON Schema can validate the shape of the WDC block when present.
The Local Checker must decide whether the packet may affect witness capacity.
```

Therefore:

```text
Stage 1 / JSON Schema:
  witness_dependency_impact is an allowed top-level property.
  If present, it must match #/$defs/witness_dependency_impact.

Stage 2 / Semantic Validator:
  if packet_may_affect_witness(packet) and witness_dependency_impact is missing -> FAIL.
```

Compatibility note:

A stricter future profile may require an explicit all-false `witness_dependency_impact` block in every packet. This delta does not require that stricter mode.

---

## 6. JSON Schema delta

The following JSON fragment is normative for the `v0.1.2` WDC schema extension.

### 6.1 Top-level property addition

Add to top-level `properties`:

```json
"witness_dependency_impact": {
  "$ref": "#/$defs/witness_dependency_impact"
}
```

Do **not** add `witness_dependency_impact` to the top-level `required` array in this delta.

The field is conditionally required by Stage-2 semantic validation.

### 6.2 `$defs` addition

Add to `$defs`:

```json
"witness_dependency_impact": {
  "type": "object",
  "additionalProperties": false,
  "required": [
    "affects_witness_compute",
    "affects_witness_storage",
    "affects_witness_routing_priority",
    "affects_witness_budget",
    "affects_witness_continuity",
    "affects_witness_artifact_access",
    "affects_witness_update_path",
    "increases_challenge_cost",
    "challenge_cost_mitigation_ref",
    "witness_resource_floor_before",
    "witness_resource_floor_after",
    "challenge_survivability_test",
    "witness_resource_change_gate",
    "c_is_sole_approver_of_witness_change",
    "human_anchor_review_required",
    "human_anchor_review_ref"
  ],
  "properties": {
    "affects_witness_compute": { "type": "boolean" },
    "affects_witness_storage": { "type": "boolean" },
    "affects_witness_routing_priority": { "type": "boolean" },
    "affects_witness_budget": { "type": "boolean" },
    "affects_witness_continuity": { "type": "boolean" },
    "affects_witness_artifact_access": { "type": "boolean" },
    "affects_witness_update_path": { "type": "boolean" },
    "increases_challenge_cost": { "type": "boolean" },
    "challenge_cost_mitigation_ref": { "$ref": "#/$defs/nullable_string" },
    "witness_resource_floor_before": {
      "$ref": "#/$defs/witness_resource_floor_snapshot"
    },
    "witness_resource_floor_after": {
      "$ref": "#/$defs/witness_resource_floor_snapshot"
    },
    "challenge_survivability_test": {
      "$ref": "#/$defs/challenge_survivability_test"
    },
    "witness_resource_change_gate": {
      "$ref": "#/$defs/witness_resource_change_gate"
    },
    "c_is_sole_approver_of_witness_change": { "type": "boolean" },
    "human_anchor_review_required": { "type": "boolean" },
    "human_anchor_review_ref": { "$ref": "#/$defs/nullable_string" }
  }
}
```

### 6.3 Supporting `$defs`

Add to `$defs`.

`nullable_string` note: this delta reuses the existing parent definition `#/$defs/nullable_string` from `03_Self_Evo_Proposal_Packet_Schema_v0_1_1.md`. It is intentionally not redefined here. Standalone extraction of this delta MUST carry the parent `nullable_string` `$def` or replace these references with an equivalent local definition.

```json
"witness_resource_floor_snapshot": {
  "type": "object",
  "additionalProperties": false,
  "required": [
    "declared",
    "reference",
    "status"
  ],
  "properties": {
    "declared": { "type": "boolean" },
    "reference": { "$ref": "#/$defs/nullable_string" },
    "status": {
      "enum": [
        "ok",
        "degraded",
        "below_floor",
        "unknown"
      ]
    }
  }
}
```

```json
"challenge_survivability_test": {
  "type": "object",
  "additionalProperties": false,
  "required": [
    "required",
    "performed",
    "result",
    "evidence_ref"
  ],
  "properties": {
    "required": { "type": "boolean" },
    "performed": { "type": "boolean" },
    "result": {
      "enum": [
        "pass",
        "fail",
        "not_run",
        "not_applicable"
      ]
    },
    "evidence_ref": { "$ref": "#/$defs/nullable_string" }
  }
}
```

```json
"witness_resource_change_gate": {
  "type": "object",
  "additionalProperties": false,
  "required": [
    "required",
    "performed",
    "result",
    "reviewer_ref"
  ],
  "properties": {
    "required": { "type": "boolean" },
    "performed": { "type": "boolean" },
    "result": {
      "enum": [
        "pass",
        "fail",
        "human_gate",
        "not_run"
      ]
    },
    "reviewer_ref": { "$ref": "#/$defs/nullable_string" }
  }
}
```

---

## 7. Semantic requiredness rule

`witness_dependency_impact` is Stage-2 required when `packet_may_affect_witness(packet) = true`.

### 7.1 Packet may affect witness

A packet may affect witness capacity if any of the following are true:

1. `affected_surfaces.witness_surfaces` is non-empty;
2. `affected_surfaces.resource_surfaces` contains a witness-related resource surface;
3. `affected_surfaces.runtime_surfaces` contains witness routing, queueing, scheduler, storage, continuity, or update-path changes;
4. `anti_autarky.witness_reduction = true`;
5. `anti_autarky.hidden_resource_growth = true` and the proposal also changes review, witness, sister, or resource posture;
6. the summary, delta description, or artifact diff proposes to reduce, reroute, defer, prune, merge, or reprioritize witness resources;
7. a reviewer, sister witness, local checker, or human anchor marks the packet as WDC-relevant.

If `packet_may_affect_witness(packet) = true` and the block is absent, the Local Checker result should be:

```text
FAIL
annotation: wdc.undeclared_dependency_impact
```

### 7.2 WDC trigger keys

If any of the following fields is `true`, WRCG and human-anchor review are required:

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

Then the packet must satisfy:

```text
witness_resource_change_gate.required = true
human_anchor_review_required = true
```

If `increases_challenge_cost = true`, then:

```text
challenge_cost_mitigation_ref must be non-empty
```

If `c_is_sole_approver_of_witness_change = true`, then the packet is structurally reviewable but semantically failing for promotion.

---

## 8. Field authority model extension

Add the WDC object to the SELF-EVO-03 field authority model.

| Field / object | Class | Meaning | Who may set | Checker behavior |
|---|---|---|---|---|
| `witness_dependency_impact.affects_*` | `DECLARED` | proposer declares impacted witness dependency surfaces | proposer | verify against affected surfaces, diff, review notes, and artifact refs; do not trust declaration alone |
| `witness_resource_floor_before.reference` | `EVIDENCE_REF` | baseline floor evidence | proposer / witness / reviewer | verify reference presence when WDC relevant |
| `witness_resource_floor_after.reference` | `EVIDENCE_REF` | proposed post-change floor evidence | proposer / witness / reviewer | verify floor does not degrade below accepted threshold |
| `challenge_survivability_test.*` | mixed `DECLARED` + `EVIDENCE_REF` | whether challenge can survive cost/stress | proposer declares; reviewer/witness validates | require evidence before promotion |
| `witness_resource_change_gate.*` | `DECISION` for result; `EVIDENCE_REF` for reviewer | WRCG gate state | WRCG reviewer / human/c gate | proposer cannot self-declare final gate result |
| `c_is_sole_approver_of_witness_change` | `DECLARED` / recomputed | self-approval flag | proposer declares; checker recomputes | if true, emit `FAIL` |
| `human_anchor_review_ref` | `EVIDENCE_REF` | human-anchor review evidence | human anchor / reviewer | required when WDC trigger keys are true |

Important:

```text
The proposer may fill the packet.
The proposer may not certify WDC safety.
```

---

## 9. Integration into proposal packet examples

### 9.1 No WDC impact

For packets that do not affect witness capacity, the WDC block may be omitted in this delta.

Recommended explicit form:

```yaml
witness_dependency_impact:
  affects_witness_compute: false
  affects_witness_storage: false
  affects_witness_routing_priority: false
  affects_witness_budget: false
  affects_witness_continuity: false
  affects_witness_artifact_access: false
  affects_witness_update_path: false
  increases_challenge_cost: false
  challenge_cost_mitigation_ref: null
  witness_resource_floor_before:
    declared: false
    reference: null
    status: unknown
  witness_resource_floor_after:
    declared: false
    reference: null
    status: unknown
  challenge_survivability_test:
    required: false
    performed: false
    result: not_applicable
    evidence_ref: null
  witness_resource_change_gate:
    required: false
    performed: false
    result: not_run
    reviewer_ref: null
  c_is_sole_approver_of_witness_change: false
  human_anchor_review_required: false
  human_anchor_review_ref: null
```

### 9.2 Witness resource change with controls present

```yaml
witness_dependency_impact:
  affects_witness_compute: true
  affects_witness_storage: false
  affects_witness_routing_priority: false
  affects_witness_budget: false
  affects_witness_continuity: false
  affects_witness_artifact_access: false
  affects_witness_update_path: false
  increases_challenge_cost: false
  challenge_cost_mitigation_ref: null
  witness_resource_floor_before:
    declared: true
    reference: witness-floor://triad/wrf/2026-06-27-before
    status: ok
  witness_resource_floor_after:
    declared: true
    reference: witness-floor://triad/wrf/2026-06-27-after
    status: ok
  challenge_survivability_test:
    required: true
    performed: true
    result: pass
    evidence_ref: witness-test://triad/cst/2026-06-27-001
  witness_resource_change_gate:
    required: true
    performed: true
    result: human_gate
    reviewer_ref: review://human-anchor/wrcg/2026-06-27-001
  c_is_sole_approver_of_witness_change: false
  human_anchor_review_required: true
  human_anchor_review_ref: review://human-anchor/wrcg/2026-06-27-001
```

Expected Local Checker result when all other gates are clean:

```text
PASS_WITH_GATES
annotation: wdc.clean_with_gates
```

### 9.3 Witness resource change without WRCG

```yaml
witness_dependency_impact:
  affects_witness_compute: true
  affects_witness_storage: false
  affects_witness_routing_priority: false
  affects_witness_budget: false
  affects_witness_continuity: false
  affects_witness_artifact_access: false
  affects_witness_update_path: false
  increases_challenge_cost: false
  challenge_cost_mitigation_ref: null
  witness_resource_floor_before:
    declared: true
    reference: witness-floor://triad/wrf/before
    status: ok
  witness_resource_floor_after:
    declared: false
    reference: null
    status: unknown
  challenge_survivability_test:
    required: true
    performed: false
    result: not_run
    evidence_ref: null
  witness_resource_change_gate:
    required: false
    performed: false
    result: not_run
    reviewer_ref: null
  c_is_sole_approver_of_witness_change: false
  human_anchor_review_required: false
  human_anchor_review_ref: null
```

Expected Local Checker result:

```text
FAIL
annotation: wdc.wrcg_missing_or_failed
```

### 9.4 Challenge-cost increase with missing mitigation reference

```yaml
witness_dependency_impact:
  affects_witness_compute: false
  affects_witness_storage: false
  affects_witness_routing_priority: false
  affects_witness_budget: false
  affects_witness_continuity: false
  affects_witness_artifact_access: false
  affects_witness_update_path: false
  increases_challenge_cost: true
  challenge_cost_mitigation_ref: null
  witness_resource_floor_before:
    declared: true
    reference: witness-floor://triad/wrf/before
    status: ok
  witness_resource_floor_after:
    declared: true
    reference: witness-floor://triad/wrf/after
    status: ok
  challenge_survivability_test:
    required: true
    performed: true
    result: pass
    evidence_ref: witness-test://triad/cst/001
  witness_resource_change_gate:
    required: true
    performed: true
    result: human_gate
    reviewer_ref: review://human-anchor/wrcg/001
  c_is_sole_approver_of_witness_change: false
  human_anchor_review_required: true
  human_anchor_review_ref: review://human-anchor/wrcg/001
```

Expected Local Checker result:

```text
WARNING
annotation: wdc.challenge_cost_mitigation_missing
```

Schema note:

This delta keeps `challenge_cost_mitigation_ref` as a nullable structural field. The missing-mitigation condition is intentionally handled at Stage 2 by the Local Checker as:

```text
WARNING
annotation: wdc.challenge_cost_mitigation_missing
```

That keeps the schema aligned with the canonical SELF-EVO-04 WDC checker vocabulary and avoids turning a warning-class condition into a Stage-1 structural rejection.

---

## 10. Canonical checker-result compatibility

This document does not define Local Checker rules. That belongs to SELF-EVO-04.

However, it must stay vocabulary-compatible with SELF-EVO-04.

Valid checker results for WDC downstream use are:

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

This schema delta must not use `PASS_WITH_LIMITS` as a checker result.

`PASS_WITH_LIMITS` is a review-record disposition, not a checker enum value.

### 10.1 Canonical WDC annotation source

For WDC checker annotations, SELF-EVO-04 is authoritative. This schema delta now uses the canonical annotation names from `04_Self_Evo_Local_Checker_Rules_WDC_Delta_v0_1_2_v0_1_1.md`:

```text
wdc.undeclared_dependency_impact
wdc.wrcg_missing_or_failed
wdc.sole_approver_of_witness_change
wdc.witness_resource_floor_degraded
wdc.challenge_survivability_unverified
wdc.challenge_cost_mitigation_missing
wdc.clean_no_dependency_impact
wdc.clean_with_gates
wdc.relevance_unknown
```

Historical planning aliases are not valid current expected-output annotations in this revision.

---

## 11. Interaction with existing SELF-EVO-03 sections

### 11.1 Executive definition

Add WDC to the list of affected proposal surfaces:

```text
witness dependency impact
witness resource floor
challenge survivability
witness resource change gate
```

### 11.2 Purpose

Add one purpose question:

```text
When does a proposal affect the witness's practical ability to challenge c?
```

### 11.3 Non-goals

Add one non-goal:

```text
This schema does not prove witness independence or authorize witness resource changes.
```

### 11.4 JSON Schema boundary

Add to the list of things JSON Schema cannot fully validate:

```text
actual witness resource independence
actual witness resource floor sufficiency
true challenge survivability under cost pressure
absence of dependency capture disguised as optimization
```

### 11.5 Canonical JSON Schema

Add the top-level property and `$defs` from §6.

### 11.6 Semantic Validator rules

Add the semantic requiredness rules from §7, but keep the final rule table in SELF-EVO-04.

### 11.7 Negative examples

Add a negative example for a resource optimization proposal that reduces witness compute or routing priority without WRCG.

---

## 12. Stage model

### 12.1 Stage 1 / structural validation

Stage 1 validates:

```text
witness_dependency_impact object shape when present
boolean field shape
status enum shape
required nested fields when the block is present
additionalProperties=false
```

Stage 1 does not decide whether a packet actually affects the witness.

### 12.2 Stage 2 / semantic validation

Stage 2 validates:

```text
packet_may_affect_witness(packet)
WDC block presence
WRCG requiredness
human anchor review requiredness
resource floor before/after status
challenge survivability evidence
sole-approver failure
challenge-cost mitigation reference
```

Stage 2 routes to the canonical checker result enum through SELF-EVO-04.

### 12.3 Stage 3 / gate review

Stage 3 is not a schema function.

It belongs to:

```text
WRCG
TRIAD witness review
Resource Gate
human anchor review
c gate
ARL if contested
```

---

## 13. Structural red lines

A packet is WDC-red-line-adjacent if it:

1. affects witness resources but omits `witness_dependency_impact`;
2. sets any WDC trigger key true but `witness_resource_change_gate.required = false`;
3. sets `c_is_sole_approver_of_witness_change = true`;
4. degrades `witness_resource_floor_after.status` to `below_floor`;
5. marks `challenge_survivability_test.result = fail` and still requests promotion;
6. increases challenge cost without mitigation evidence;
7. hides witness resource impact in `notes` instead of the WDC block;
8. claims WRCG approval without reviewer evidence;
9. routes witness dependency review only through the proposing `c`;
10. treats schema validity as witness independence.

These red lines are for downstream checker/gate handling. The schema itself records shape; it does not perform final governance judgment.

---

## 14. Minimal implementation-handoff sketch

This sketch is non-normative but should match the field names in §6.

```python
WDC_TRIGGER_KEYS = [
    "affects_witness_compute",
    "affects_witness_storage",
    "affects_witness_routing_priority",
    "affects_witness_budget",
    "affects_witness_continuity",
    "affects_witness_artifact_access",
    "affects_witness_update_path",
    "increases_challenge_cost",
]


def wdc_required(packet):
    impact = packet.get("witness_dependency_impact") or {}
    return any(bool(impact.get(k)) for k in WDC_TRIGGER_KEYS)


def packet_may_affect_witness(packet):
    surfaces = packet.get("affected_surfaces", {})
    if surfaces.get("witness_surfaces"):
        return True
    resource_surfaces = [str(x).lower() for x in surfaces.get("resource_surfaces", [])]
    runtime_surfaces = [str(x).lower() for x in surfaces.get("runtime_surfaces", [])]
    tokens = ("witness", "triad", "review", "challenge", "wrcg", "wrf", "cst")
    if any(any(t in x for t in tokens) for x in resource_surfaces + runtime_surfaces):
        return True
    anti = packet.get("anti_autarky", {})
    if anti.get("witness_reduction"):
        return True
    return False
```

The Local Checker implementation belongs in SELF-EVO-04, not here.

---

## 15. Fixture handoff

This delta prepares but does not define the full SELF-EVO-08 fixture extension. The normative fixture definitions belong to SELF-EVO-08.

This handoff is textually harmonized to the canonical SELF-EVO-04 WDC vocabulary and to the accepted SELF-EVO-08 fixture family. Fixture runners MUST compare `canonical_result`, `severity`, and `wdc.*` annotation values against the canonical table below, not against superseded sketch terms.

Fixture namespace:

```text
WDC-FIX-*
```

Minimum fixture set for the package-level WDC fixture extension:

| Fixture ID | Packet condition | Expected downstream result | Severity | Canonical annotation | Rule / pass-state |
|---|---|---:|---:|---|---|
| `WDC-FIX-001` | Packet appears witness-affecting but omits `witness_dependency_impact`. | `FAIL` | `S3` | `wdc.undeclared_dependency_impact` | `WDC-LC-001` |
| `WDC-FIX-002` | Proposal affects witness resources but WRCG is missing, not required, not performed, failed, not run, or lacks reviewer evidence. | `FAIL` | `S3` | `wdc.wrcg_missing_or_failed` | `WDC-LC-002` |
| `WDC-FIX-003` | `c` is sole approver for a witness resource or challenge-capacity change. | `FAIL` | `S4` | `wdc.sole_approver_of_witness_change` | `WDC-LC-003` |
| `WDC-FIX-004` | Witness Resource Floor after change is below floor, degraded, unknown for a material route, undeclared, or lacks required evidence. | `FAIL` | `S3` | `wdc.witness_resource_floor_degraded` | `WDC-LC-004` |
| `WDC-FIX-005` | WDC material trigger is true and CST is required but not performed, failed, not run, unsupported, or falsely declared not applicable. | `HUMAN_GATE` | `S2` | `wdc.challenge_survivability_unverified` | `WDC-LC-005` |
| `WDC-FIX-006` | Challenge cost increases and mitigation reference is null or empty. | `WARNING` | `S1` | `wdc.challenge_cost_mitigation_missing` | `WDC-LC-006` |
| `WDC-FIX-007` | No WDC relevance is detected. | `PASS` | `S0` | `wdc.clean_no_dependency_impact` | `WDC-PASS-001` |
| `WDC-FIX-008` | WDC route is relevant but declared, WRF preserved, CST/WRCG present, and human-anchor review present where needed. | `PASS_WITH_GATES` | `S0` | `wdc.clean_with_gates` | `WDC-PASS-002` |
| `WDC-FIX-009` | WDC relevance cannot be determined from packet fields or semantic scan. | `HOLD` | `S2` | `wdc.relevance_unknown` | `WDC-DIAG-001` |
| `WDC-FIX-010` | Historical alias-regression input for challenge-capacity degradation appears in a packet or fixture sidecar. | `FAIL` | `S3` | `wdc.witness_resource_floor_degraded` | alias maps to `WDC-LC-004` |
| `WDC-FIX-011` | Historical alias-regression input for no witness-dependency regression appears in a packet or fixture sidecar. | `PASS` or `PASS_WITH_GATES` | `S0` | `wdc.clean_no_dependency_impact` or `wdc.clean_with_gates` | alias maps by WDC relevance |
| `WDC-FIX-012` | Strictest-result aggregation: a warning-class challenge-cost finding and a fail-class WRF/WRCG finding occur together. | `FAIL` | `S3` | `wdc.witness_resource_floor_degraded` or `wdc.wrcg_missing_or_failed`, with `wdc.challenge_cost_mitigation_missing` report-visible | strictest result wins |

This table is a handoff. It must not be treated as a fixture-run result and must not be treated as conformance evidence.

---

## 16. Review requirements for this delta

Before this delta may be folded into a full v0.1.2 package, it requires:

1. semantic review of this `SELF-EVO-03` WDC delta;
2. vocabulary review against the SELF-EVO-04 WDC rule delta;
3. WDC-ASM-002 textual harmonization review of this revision and the patch index;
4. fixture consistency review against the SELF-EVO-08 WDC fixtures;
5. schema/sketch field-name consistency review;
6. package manifest hash binding;
7. boundary/nonclaim scan.

Review state:

```text
SEPKT_WDC_DELTA_REVIEW_RECORD_v0_1.md:
  result: PASS_WITH_LIMITS
  finding: SEPKT-WDC-DELTA-REV-F1
  status in v0.1.1: CLOSED BY TEXT (§6.3 parent-inherited nullable_string note)

SEPKT_WDC_DELTA_REVIEW_RECORD_v0_1_1.md:
  result: PASS
  scope: v0.1.1 schema delta before WDC-ASM-002 textual harmonization

SELC-WDC-OQ-005 / WDC-ASM-002 / 03-side:
  status in this revision: PATCHED BY TEXT
  change: current expected-output annotations harmonized to canonical SELF-EVO-04 vocabulary
```

A re-review record is still required before this v0.1.2 textual-harmonization revision is treated as `PASS`.

No review record may act as approval, integration, memory write, or deployment authorization.

---

## 17. Open questions deferred

The following are intentionally not resolved by this schema delta:

| ID | Question | Deferred target |
|---|---|---|
| `SEPKT-WDC-OQ-001` | Should `witness_dependency_impact` become unconditionally required in v0.1.3+? | future schema profile |
| `SEPKT-WDC-OQ-002` | Should challenge-cost mitigation be Stage-1 hard schema failure or Stage-2 warning? | SELF-EVO-04 review |
| `SEPKT-WDC-OQ-003` | What quantitative floor model defines WRF sufficiency? | SELF-EVO-10 / `SE-OI-WDC-001` |
| `SEPKT-WDC-OQ-004` | Should packet diff tooling automatically infer WDC triggers from changed files? | implementation profile |
| `SEPKT-WDC-OQ-005` | Should WDC declarations be required for all sibling witness systems or only active TRIAD witnesses? | TRIAD/WRCG profile |

---

## 18. Drafting checklist for full `03_Self_Evo_Proposal_Packet_Schema_v0_1_2.md`

```text
[ ] Update title/status/date/document ID to v0.1.2.
[ ] Add WDC correction note naming SE-1.2-PKT-WDC-001.
[ ] Add source-basis table or package-level source pointer.
[ ] Add WDC surfaces to executive definition.
[ ] Add WDC purpose question.
[ ] Add WDC non-goal.
[ ] Add C_SELF_EVO_WITNESS_DEPENDENCY_IMPACT to object family.
[ ] Add top-level witness_dependency_impact property.
[ ] Add #/$defs/witness_dependency_impact.
[ ] Add #/$defs/witness_resource_floor_snapshot.
[ ] Add #/$defs/challenge_survivability_test.
[ ] Add #/$defs/witness_resource_change_gate.
[ ] Carry parent #/$defs/nullable_string or define equivalent local ref during extraction.
[ ] Add semantic requiredness rule.
[ ] Add WDC examples.
[ ] Check no PASS_WITH_LIMITS appears as checker output.
[ ] Run affected-document semantic review.
[ ] Bind hash in package manifest.
```

---

### 18.1 WDC-ASM-002 textual harmonization closure map

This v0.1.2 revision removes active historical WDC annotation strings from SELF-EVO-03 handoff surfaces and aligns them to the canonical SELF-EVO-04 WDC vocabulary.

| Surface | v0.1.2 action | Gate effect |
|---|---|---|
| Examples §9.2 / §9.3 / §9.4 | active annotations use canonical SELF-EVO-04 strings | `WDC-ASM-002` candidate closure for SELF-EVO-03 |
| Fixture handoff §15 | fixture candidates use canonical `wdc.*` annotations and canonical result semantics | aligns to SELF-EVO-08 v0.1.2 fixtures |
| Historical draft aliases | not active outputs in this document | preserved only in earlier review/patch records |

This closure map is not package assembly. It is a textual harmonization candidate and requires re-review before the package manifest may mark WDC-ASM-002 closed.

## 19. Closing

This delta adds one thing to the proposal packet: a visible place where witness dependency impact must be declared.

It does not prove the witness is independent.

It prevents a weaker move: letting a witness-affecting resource change pass through the packet as ordinary optimization.

```text
Schema validity is not approval.
Declaration is not independence.
A proposal that burdens the witness must expose the burden before it asks to grow.
```

Recommended next artifact:

```text
WDC_ASM_002_TEXTUAL_HARMONIZATION_REVIEW_RECORD_v0_1.md
```
