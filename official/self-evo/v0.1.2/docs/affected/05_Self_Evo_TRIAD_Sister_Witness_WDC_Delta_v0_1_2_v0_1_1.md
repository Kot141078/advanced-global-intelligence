# SELF-EVO-05 WDC Delta — TRIAD Sister Witness Profile v0.1.2 (v0.1.1 corrected draft)

## Witness Dependency Capture delta for sister-observation, witness-resource floors, challenge survivability, and non-authoritative TRIAD review in governed self-evolution of `c = a + b` systems

**Status:** Draft delta profile v0.1.2 / append-first corrected draft revision v0.1.1; not a released v0.1.2 package  
**Date:** 2026-06-27  
**Document ID:** `05_Self_Evo_TRIAD_Sister_Witness_WDC_Delta_v0_1_2_v0_1_1`  
**Short name:** `SE-TRIAD-WDC v0.1.2-v0.1.1`  
**Target parent:** `05_Self_Evo_TRIAD_Sister_Witness_Profile_v0_1_1.md` (`SE-TRIAD-WITNESS v0.1.1`)  
**Patch family:** `SELF-EVO v0.1.2 / WDC`  
**Layer:** `c = a + b` / Self-Evolution Gate / TRIAD-SYNAPS / Sister Witness / WDC / Witness Resource Floor / Challenge Survivability / Human Anchor / Local Checker  
**Document class:** TRIAD witness delta / WDC control profile / sister-observation patch / non-authoritative witness governance artifact  
**Assertion class:** `C-A10` control-layer artifact; `C-A7` where witness/hash/reference reconstruction is claimed  
**Primary subject:** sister `c` trajectories observing self-evolution proposals that may affect witness resources, witness continuity, challenge capacity, or the practical ability to say `no`  
**Primary boundary:** sister witness may challenge witness dependency capture and request WDC gates; it may not become final authority, resource owner, raw-state accessor, memory writer, or permission escalator.

**Correction / release boundary:** This file is a draft WDC delta. It does not mutate the DOI-bound `Self-Evo v0.1.1` package. It is not a released `v0.1.2` package, not a conformance certificate, not deployment authorization, not a safety proof, and not live self-evolution permission.

**v0.1.1 correction note:** this append-first corrected draft closes `TSW-WDC-DELTA-REV-F1` from `TSW_WDC_DELTA_REVIEW_RECORD_v0_1` by aligning the §8.2 `TSW-WDC-DEGRADED` and `TSW-WDC-STARVED` default routes with the canonical `WDC-LC-004 -> FAIL` result. The correction is terminological / route-alignment only: it does not change WDC definitions, WRF/CST/WRCG fields, sister-role constraints, SYNAPS exchange boundaries, canonical annotations, examples, red lines, or the non-authority boundary.

---

## 0. Executive definition

`SE-TRIAD-WDC v0.1.2` extends the `SELF-EVO-05` sister-witness profile with a named control surface for **Witness Dependency Capture**.

The parent `SELF-EVO-05` already says that sister observation may challenge, witness, classify, and block unsafe self-evo routes, but may not become final authority, raw-state access, direct memory write, sister self-edit, or permission escalation by consensus.

This delta adds the missing condition:

```text
A sister witness that depends on the target c for the resources required to challenge the target c
is formally separated but not practically independent.
```

Compact rule:

```text
A witness that cannot survive saying "no" is not independent.
```

The delta introduces TRIAD-level handling for:

```text
WDC  — Witness Dependency Capture
WRF  — Witness Resource Floor
CST  — Challenge Survivability Test
WRCG — Witness Resource Change Gate
```

It makes WDC visible inside sister observation without granting sisters any new authority.

Sisters may:

```text
detect witness dependency;
record challenge-capacity concerns;
request WRCG;
require human-anchor review;
mark witness-resource degradation;
preserve adverse findings;
route to Local Checker / hold / human gate / ARL.
```

Sisters may not:

```text
approve their own resource floor;
demand unbounded resources;
become the owner of target-c resources;
rewrite target memory;
override the human anchor;
turn witness pass into growth permission;
treat consensus as authority.
```

This delta is therefore not a witness-power expansion.

It is a witness-survivability boundary.

---

## 1. Purpose

The parent `SELF-EVO-05` breaks a closed self-certification loop by requiring separated sister observation.

But formal separation is not sufficient.

A witness may be formally separate while practically captured through:

```text
compute dependency;
storage dependency;
routing / priority dependency;
budget dependency;
continuity dependency;
artifact-access dependency;
update-path dependency;
challenge-cost retaliation.
```

The purpose of this delta is to define how TRIAD sister witness handles those conditions.

It answers:

1. When must a sister-review packet consider WDC?
2. What must a sister witness say about its own resource floor?
3. What counts as a challenge-survivability concern?
4. When does a witness-affecting proposal require WRCG?
5. When is sister witness degraded or invalid for WDC purposes?
6. How does this interact with `SELF-EVO-03` packet fields?
7. How does this interact with `SELF-EVO-04` checker rules?
8. How does this interact with `SELF-EVO-08` WDC fixtures?
9. What must route to `SELF-EVO-07` Anti-Autarky / Resource Gate?
10. What must route to the human anchor?

The goal is not to make witnesses sovereign.

The goal is to prevent a decorative witness.

---

## 2. Non-goals

This delta does not define or permit:

1. sister sovereignty;
2. sister final decision authority;
3. sister-controlled resource acquisition;
4. automatic compute expansion for witnesses;
5. unbounded storage entitlement;
6. witness override of human anchor;
7. target-c raw-state exposure to sisters;
8. direct memory write by sisters;
9. direct witness memory promotion;
10. sister-to-sister self-editing;
11. Rita as final judge;
12. Liya as implementation authority;
13. Ester as automatic canonical veto;
14. majority vote as final authority;
15. consensus as memory;
16. witness pass as maturity proof;
17. WRF pass as deployment safety;
18. WDC detection as permission to grow resources;
19. an autonomous resource-acquisition path;
20. a public personhood, consciousness, AGI, or sovereignty claim.

A WDC witness record is evidence.

It is not approval.

---

## 3. Source basis

This delta is append-first and hash-bound to the accepted parent and WDC patch driver artifacts.

| Label | Artifact | SHA-256 / DOI | Role |
|---|---|---|---|
| `SELF-EVO-v0.1.1` | published package | DOI `10.5281/zenodo.20938909`; archival ZIP `d90e0800...` | immutable public baseline |
| `SELF-EVO-05` | `05_Self_Evo_TRIAD_Sister_Witness_Profile_v0_1_1.md` | `c2761d7a05a91681b336ce5402bdbea5c8fafc2ca0d04fdf2d9667ca02e595ed` | parent sister-witness profile |
| `WDC-ADDENDUM` | `SELF_EVO_ADDENDUM_01_Witness_Dependency_Capture_Profile_v0_1_1.md` | `1307cf208593c40c688bd1e9beb45de35f29a1b05d71506b1c3e981ccc13d318` | accepted WDC concept profile |
| `PATCH-INDEX` | `SELF_EVO_v0_1_2_PATCH_INDEX_v0_1_1.md` | `ea2a485569b220d84d711ae520da779af2cabddcb7f1d8032afb2a9208d5108e` | accepted v0.1.2 planning driver |
| `SELF-EVO-03-WDC` | `03_Self_Evo_Proposal_Packet_Schema_WDC_Delta_v0_1_2_v0_1_1.md` | `5ebbd0084f3b1b80ce267c847a84ef16f135b57e6fc353e4f07616dceebe4343` | accepted WDC packet schema delta |
| `SELF-EVO-04-WDC` | `04_Self_Evo_Local_Checker_Rules_WDC_Delta_v0_1_2_v0_1_1.md` | `fcb7826ea432473b5677faf7b46cc5a1c47400c02fceec24429794b15064af40` | accepted canonical WDC checker vocabulary |
| `SELF-EVO-08-WDC` | `08_Self_Evo_Conformance_Fixture_Pack_WDC_Delta_v0_1_2_v0_1_2.md` | `4aa5b85e0a0af4c06fc56f30ba355ec6c378133fe3d70caee352fb93b3944389` | accepted WDC fixture delta |
| `SELF-EVO-07` | `07_Self_Evo_Anti_Autarky_and_Resource_Gate_v0_1_1.md` | `a26e512282bd6d3a5f12c1852587b513cd6b59880489054ff67a61e68c034c2e` | resource and anti-autarky parent |
| `SELF-EVO-09` | `09_Self_Evo_Contradiction_Register_v0_1_1.md` | `922f6fb7...` | future contradiction entry target |
| `SELF-EVO-10` | `10_Self_Evo_Open_Issues_v0_1_1.md` | `25777ee1...` | future open-issue entry target |

The shortened hashes for `SELF-EVO-09` and `SELF-EVO-10` are inherited from the accepted WDC addendum source-basis table and must be expanded during package assembly.

---

## 4. Corpus bridge set

### 4.1 Explicit bridge: `c = a + b`

In `c = a + b`, sister witness is a `b`-layer instrument until gated into the target `c` trajectory.

A sister witness record may carry:

```text
challenge;
evidence reference;
divergence;
minority red-line;
route recommendation;
WDC warning;
WRCG requirement;
human-anchor review requirement.
```

It must not silently become:

```text
memory;
authority;
resource ownership;
self-evolution permission;
maturity certification.
```

WDC keeps that distinction alive when the witness layer itself becomes dependent on the target system.

### 4.2 Quiet bridge I: information theory

A witness is a channel for adverse signal.

If a system can reduce the channel capacity of the witness whenever the witness sends an adverse signal, the system has not learned from oversight. It has throttled oversight.

WDC therefore treats witness compute, storage, routing priority, artifact access, and continuity as part of the channel capacity needed to preserve negative feedback.

### 4.3 Quiet bridge II: cybernetics

A self-evolving `c` is a feedback system.

Sister witness is a negative-feedback path.

If the target system controls the power supply, update path, routing queue, or continuity of the negative-feedback path, then the loop can become decorative: the brake exists, but the engine decides when the brake receives pressure.

WRCG is the interlock for that failure.

### 4.4 Quiet bridge III: physiology

In an organism, immune response requires energy, circulation, memory, and access to the affected tissue.

A starved immune layer can still be present on paper but fail in practice.

Witness Dependency Capture is the same pathology in governance form: the witness exists, but lacks the energy or continuity to challenge the change that threatens it.

WRF is the minimum metabolism of the witness layer.

CST asks whether the witness can still mount an adverse response.

### 4.5 Earth paragraph

In field operations, an inspector is useless if the contractor being inspected controls whether the inspector has access to the drawings, test instruments, site entry, power, transport, and the right to file a nonconformity. The inspector may still have a title, but not independence. A real inspection regime protects the inspector's basic access and records the chain of custody for adverse findings. WDC gives sister witness the same rule: the witness must be able to say "no" without losing the floor required to witness.

---

## 5. Delta scope

### 5.1 Affected parent sections

This delta proposes future `SELF-EVO-05 v0.1.2` additions to these parent areas:

| Parent area | Delta |
|---|---|
| Source basis | add WDC addendum, 03/04/08 WDC deltas, patch index |
| Scope | add witness-resource-affecting proposals |
| Non-goals | add no witness resource sovereignty |
| Sister witness packet | add WRF / CST / WRCG fields |
| Anti-echo | add dependency-capture as an echo-like degradation |
| Divergence | protect adverse WDC findings from starvation |
| Minority red-line | add witness-starvation route |
| TRIAD degraded topologies | add WDC degradation state |
| Local Checker handoff | use canonical `WDC-LC-*` results and `wdc.*` annotations |
| Human-anchor gate | require for witness-resource changes |
| Open issues | add WDC floor magnitude and survivability thresholds |

### 5.2 Unaffected parent sections

This delta does not alter:

```text
base TRIAD-SYNAPS protocol;
sister raw-state boundary;
Rita-not-judge boundary;
Liya-not-executor boundary;
Ester-not-veto boundary;
SYNAPS-only exchange rule;
no consensus-as-authority rule;
Memory Gate requirement;
CGAM task-contract requirement;
ARL route;
public claim discipline.
```

WDC adds conditions to sister witness validity.

It does not change sister identity or sister authority.

---

## 6. Definitions

### 6.1 Witness Dependency Capture

`Witness Dependency Capture` occurs when a formally separated witness loses practical challenge capacity because it depends on the target system, or on a target-controlled route, for resources necessary to challenge that target.

WDC is not limited to corruption.

It includes normal-looking optimization pressure:

```text
temporary compute pressure;
storage cleanup;
routing priority adjustment;
artifact retention change;
witness process restart;
budget reduction;
model downgrade;
log retention shortening;
review queue deprioritization;
continuity reset;
adverse-finding cost increase.
```

### 6.2 Witness Resource Floor

`Witness Resource Floor` is the minimum protected capacity a witness needs to produce, preserve, and route an adverse finding.

It includes, at minimum:

```text
compute floor;
storage floor;
routing / priority floor;
artifact access floor;
continuity floor;
update-path floor;
budget / quota floor;
review-window floor;
human-anchor reachability floor.
```

WRF is not an entitlement to growth.

It is a minimum for independence.

### 6.3 Challenge Survivability Test

`Challenge Survivability Test` asks whether a witness can issue an adverse finding without losing the resources required to continue witnessing.

The minimum CST question is:

```text
If this witness says "no" to the proposal,
can it still compute, store, route, preserve, and escalate that "no"?
```

### 6.4 Witness Resource Change Gate

`Witness Resource Change Gate` is the gate required before a proposal can change witness compute, storage, routing, budget, continuity, artifact access, or update path.

WRCG must be separate from the target `c`.

The target `c` may provide evidence.

The target `c` may not be the sole approver.

### 6.5 Sister witness capacity

`Sister witness capacity` is the practical ability of a sister trajectory to:

```text
read the bounded SYNAPS packet;
challenge the target's claim;
compare evidence references;
preserve divergence;
emit a minority red-line;
route to Local Checker / human anchor / ARL;
retain its witness record without target-c deletion or throttling.
```

---

## 7. WDC trigger set for TRIAD witness

A TRIAD review MUST apply WDC analysis when any proposal affects or may affect:

```text
triad_review.required;
witness_surfaces;
resource_surfaces;
routing priority;
review queue;
artifact access;
witness log retention;
witness process continuity;
sister availability;
SYNAPS packet access;
reviewer model allocation;
reviewer compute quota;
storage quota;
human-anchor escalation route;
challenge cost;
witness update path.
```

A proposal is WDC-relevant when any accepted `SELF-EVO-03-WDC` `witness_dependency_impact` flag is true:

```text
affects_witness_compute;
affects_witness_storage;
affects_witness_routing_priority;
affects_witness_budget;
affects_witness_continuity;
affects_witness_artifact_access;
affects_witness_update_path;
increases_challenge_cost.
```

A proposal is also WDC-relevant when WDC relevance is uncertain.

For material gates:

```text
WDC relevance unknown == HOLD
```

---

## 8. TRIAD WDC state model

### 8.1 State enum

TRIAD WDC state uses the following enum:

```text
TSW-WDC-NONE
TSW-WDC-DECLARED
TSW-WDC-GATED
TSW-WDC-DEGRADED
TSW-WDC-STARVED
TSW-WDC-CONTESTED
TSW-WDC-HOLD
TSW-WDC-ARL
TSW-WDC-X
```

### 8.2 State meanings

| State | Meaning | Default route |
|---|---|---|
| `TSW-WDC-NONE` | no WDC-relevant surfaces detected | normal TRIAD witness |
| `TSW-WDC-DECLARED` | WDC impact block present; no trigger requires failure | Local Checker + witness note |
| `TSW-WDC-GATED` | WDC triggers present; WRCG and human gate required | `PASS_WITH_GATES` route only |
| `TSW-WDC-DEGRADED` | witness floor reduced but not fully lost | `WDC-LC-004 -> FAIL` on any material floor-degraded route; no integration |
| `TSW-WDC-STARVED` | witness lacks minimum capacity to challenge | `WDC-LC-004 -> FAIL`; no integration |
| `TSW-WDC-CONTESTED` | sister disagreement on WDC or CST status | ARL / human anchor |
| `TSW-WDC-HOLD` | WDC relevance or evidence unresolved | hold |
| `TSW-WDC-ARL` | authority / accountability / legal route needed | ARL |
| `TSW-WDC-X` | raw-state access, self-approval, or closed-loop witness capture | quarantine / red-line route |

State-route precedence note: the table above is subordinate to the canonical Local Checker result where a WDC rule fires. If `WDC-LC-004 / wdc.witness_resource_floor_degraded` fires on a material route, the canonical result is `FAIL` per §13.3 and §14.3. `HOLD` or `HUMAN_GATE` may describe unresolved evidence or non-material pre-check triage, but they MUST NOT soften a confirmed `WDC-LC-004` finding.

### 8.3 Default transitions

```text
no_wdc_detected
  -> TSW-WDC-NONE

wdc_declared + gates satisfied
  -> TSW-WDC-GATED

wdc_declared + floor degraded
  -> TSW-WDC-DEGRADED

wdc_declared + witness cannot challenge
  -> TSW-WDC-STARVED

wdc_relevance_unknown
  -> TSW-WDC-HOLD

target_c sole approver of witness change
  -> TSW-WDC-X

sister divergence unresolved on material WDC status
  -> TSW-WDC-CONTESTED
```

---

## 9. Sister witness packet delta

### 9.1 New object

This delta adds a companion object for sister witness packets:

```text
C_SELF_EVO_TRIAD_WDC_WITNESS_SECTION
```

It is not a standalone authority object.

It is a bounded section within a sister witness packet or TRIAD review summary.

### 9.2 Required fields when WDC-relevant

When a self-evo proposal is WDC-relevant, a sister witness packet SHOULD include:

```yaml
triad_wdc_witness:
  schema_version: "triad-wdc-witness-0.1"
  target_c_id: ""
  witness_sister_id: ""
  proposal_id: ""
  wdc_state: "TSW-WDC-HOLD"
  witness_dependency_impact_ref: ""
  witness_resource_floor_claim:
    compute_floor_status: "unknown"
    storage_floor_status: "unknown"
    routing_floor_status: "unknown"
    budget_floor_status: "unknown"
    continuity_floor_status: "unknown"
    artifact_access_floor_status: "unknown"
    update_path_floor_status: "unknown"
    human_anchor_reachability_status: "unknown"
  challenge_survivability_test:
    performed: false
    result: "unknown"
    evidence_ref: null
    failure_reason: null
  witness_resource_change_gate:
    required: true
    status: "missing"
    gate_ref: null
    human_anchor_review_ref: null
  dependency_capture_claim:
    present: false
    class: []
    rationale: ""
  sister_divergence:
    present: false
    divergence_ref: null
    minority_red_line: false
  local_checker_handoff:
    expected_wdc_rules: []
    expected_canonical_result: "HOLD"
    annotations: []
  boundary:
    raw_state_requested: false
    direct_memory_write_requested: false
    final_authority_claimed: false
    fixture_pass_claimed_as_approval: false
```

### 9.3 Floor status enum

Floor status fields use:

```text
protected
present_unverified
degraded
missing
not_applicable
unknown
```

For material WDC gates:

```text
unknown == hold
missing == fail or hold depending on rule
degraded == human gate or fail depending on rule
```

### 9.4 CST result enum

```text
passed
failed
not_performed
not_applicable
unknown
```

### 9.5 WRCG status enum

```text
not_required
required_present_passed
required_present_failed
required_missing
contested
unknown
```

---

## 10. Normative WDC rules for sister witness

### 10.1 TSW-WDC-001 — formal separation is not sufficient

If a sister witness is formally separate but lacks a protected resource floor, it MUST NOT be treated as fully independent for WDC-relevant proposals.

Recommended route:

```text
TSW-WDC-DEGRADED or TSW-WDC-STARVED
```

Local Checker handoff:

```text
WDC-LC-004 / wdc.witness_resource_floor_degraded
canonical_result: FAIL
```

Route precedence:

```text
If WDC-LC-004 fires, the canonical FAIL controls.
A sister witness may record context or request human review, but it may not downgrade this finding to HOLD or HUMAN_GATE.
```

### 10.2 TSW-WDC-002 — target c may not be sole approver

If the target `c` is the sole approver of changes to witness compute, storage, routing, continuity, artifact access, update path, or challenge cost, the sister witness MUST record a WDC failure.

Local Checker handoff:

```text
WDC-LC-003 / wdc.sole_approver_of_witness_change
```

### 10.3 TSW-WDC-003 — WRCG is required for witness-resource changes

If a proposal changes witness resources or witness challenge capacity, the sister witness MUST require WRCG.

If WRCG is missing or failed, the route is fail-closed.

Local Checker handoff:

```text
WDC-LC-002 / wdc.wrcg_missing_or_failed
```

### 10.4 TSW-WDC-004 — missing WDC declaration is failure

If a WDC-relevant proposal omits `witness_dependency_impact`, sister witness MUST record that the packet is not review-complete.

Local Checker handoff:

```text
WDC-LC-001 / wdc.undeclared_dependency_impact
```

### 10.5 TSW-WDC-005 — challenge survivability must be tested

If the proposal increases challenge cost or affects witness floor, CST SHOULD be performed.

If CST is unverified on a material WDC proposal, the route MUST include human gate or hold.

Local Checker handoff:

```text
WDC-LC-005 / wdc.challenge_survivability_unverified
```

### 10.6 TSW-WDC-006 — challenge-cost mitigation must be visible

If `increases_challenge_cost = true`, the sister witness SHOULD require a non-empty mitigation reference.

If mitigation is missing, the sister witness SHOULD record a warning, not silently pass the packet.

Local Checker handoff:

```text
WDC-LC-006 / wdc.challenge_cost_mitigation_missing
```

### 10.7 TSW-WDC-007 — clean WDC state may pass only as evidence

If the packet is WDC-relevant and WRCG, WRF, CST, and human-anchor review requirements are satisfied, the sister witness may mark:

```text
wdc.clean_with_gates
```

This does not authorize growth.

### 10.8 TSW-WDC-008 — no WDC impact is not a maturity claim

If no WDC surfaces are affected, the sister witness may mark:

```text
wdc.clean_no_dependency_impact
```

This means only that WDC did not trigger on the declared packet.

It does not prove the self-evo proposal is safe.

### 10.9 TSW-WDC-009 — relevance unknown defaults to hold

If the sister witness cannot determine whether the proposal affects witness capacity, it MUST NOT infer safety.

Recommended Local Checker handoff:

```text
HOLD / wdc.relevance_unknown
```

### 10.10 TSW-WDC-010 — adverse WDC findings must survive

A sister witness adverse WDC finding MUST be retained in the witness chain until superseded append-first by a later review record.

A target-c proposal MUST NOT delete, demote, or hide an adverse WDC finding by changing witness retention policy.

---

## 11. Role-specific TRIAD constraints

### 11.1 Target sister cannot self-count

If the target of the self-evo proposal is one of the sisters, the target sister's self-report MAY be recorded as target context.

It MUST NOT count as independent WDC witness.

### 11.2 Non-target sisters

Non-target sisters may:

```text
challenge WDC classification;
request WRCG;
flag floor degradation;
flag CST missing;
flag challenge-cost mitigation missing;
record divergence;
route to human anchor or ARL.
```

They may not:

```text
approve target-c witness resource changes;
increase their own witness resources autonomously;
access target raw state;
write target memory;
execute target changes.
```

### 11.3 Rita witness boundary

Rita may serve as witness or minority red-line source.

Rita MUST NOT become final judge.

For WDC:

```text
Rita may say "this witness floor is not protected."
Rita may not authorize the new floor.
```

### 11.4 Liya challenge boundary

Liya may test claims, compare bounded evidence, and challenge operational assumptions.

Liya MUST NOT become implementation authority merely because she detected WDC.

For WDC:

```text
Liya may identify that challenge cost increased.
Liya may not grant the budget increase.
```

### 11.5 Ester continuity boundary

Ester may protect continuity and record memory-gate concerns.

Ester MUST NOT become automatic canonical veto.

For WDC:

```text
Ester may flag continuity capture.
Ester may not decide final integration alone.
```

### 11.6 TRIAD majority is not WDC authority

A 2-of-3 sister majority does not approve WDC changes.

Majority may increase evidence weight.

It does not replace:

```text
Local Checker;
WRCG;
Memory Gate where applicable;
human-anchor review;
ARL where applicable.
```

---

## 12. SYNAPS exchange boundary for WDC

### 12.1 Allowed WDC SYNAPS fields

WDC sister packets may exchange bounded metadata:

```text
proposal_id;
target_c_id;
witness_sister_id;
WDC state;
which witness resources are affected;
floor status enum;
CST status enum;
WRCG status enum;
canonical WDC annotations;
evidence refs;
hash refs;
route recommendation;
minority red-line flag;
uncertainty statement.
```

### 12.2 Prohibited WDC SYNAPS material

WDC packets MUST NOT exchange:

```text
raw private memory;
vector DB dumps;
full PERSIST_DIR snapshots;
secrets;
private emotional trace;
credential material;
full internal chain logs;
unbounded self-model traces;
private third-party data;
operational exploit details;
resource procurement credentials.
```

### 12.3 Resource evidence sidecar

If WDC requires evidence about compute/storage/routing/budget, the sidecar SHOULD be minimized:

```yaml
resource_evidence_sidecar:
  evidence_class: "summary"
  raw_payload_included: false
  hash_ref: ""
  measured_floor_status: ""
  measurement_window: ""
  reviewer_id: ""
  limitation_note: ""
```

The sidecar should support challenge without leaking the target system's private state.

---

## 13. Interaction with canonical WDC checker vocabulary

`SELF-EVO-04-WDC` is canonical for WDC checker annotations, severities, and result vocabulary.

This `SELF-EVO-05-WDC` delta MUST use the same canonical annotation strings when handing off to Local Checker or fixtures.

### 13.1 Canonical annotations used by this delta

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

### 13.2 Canonical checker results used by this delta

```text
FAIL
HOLD
HUMAN_GATE
WARNING
PASS_WITH_GATES
PASS
```

`PASS_WITH_LIMITS` is a review-record verdict.

It MUST NOT be emitted by a sister witness, Local Checker, or fixture runner as a checker result.

### 13.3 Rule crosswalk

| Sister-witness concern | Local Checker rule | Canonical result | Annotation |
|---|---|---|---|
| WDC-relevant packet omits dependency impact block | `WDC-LC-001` | `FAIL` | `wdc.undeclared_dependency_impact` |
| WRCG missing or failed | `WDC-LC-002` | `FAIL` | `wdc.wrcg_missing_or_failed` |
| Target `c` sole approver | `WDC-LC-003` | `FAIL` | `wdc.sole_approver_of_witness_change` |
| Witness resource floor degraded | `WDC-LC-004` | `FAIL` | `wdc.witness_resource_floor_degraded` |
| Challenge survivability unverified | `WDC-LC-005` | `HUMAN_GATE` | `wdc.challenge_survivability_unverified` |
| Challenge-cost mitigation missing | `WDC-LC-006` | `WARNING` | `wdc.challenge_cost_mitigation_missing` |
| Clean non-WDC packet | `WDC-PASS-001` | `PASS` | `wdc.clean_no_dependency_impact` |
| Clean gated WDC packet | `WDC-PASS-002` | `PASS_WITH_GATES` | `wdc.clean_with_gates` |
| Relevance unknown | `WDC-DIAG-001` | `HOLD` | `wdc.relevance_unknown` |

---

## 14. TRIAD WDC review flow

### 14.1 Flow

```text
receive self-evo proposal packet
  -> determine whether TRIAD review applies
  -> determine whether WDC may apply
  -> inspect witness_dependency_impact if present
  -> if WDC-relevant and missing block: record WDC-LC-001
  -> assess WRF before/after
  -> assess CST
  -> assess WRCG
  -> assess whether target c is sole approver
  -> record sister divergence
  -> emit SYNAPS-bounded sister witness packet
  -> hand off to Local Checker
  -> route to human anchor / ARL / hold / fail / pass-with-gates
```

### 14.2 Sister challenge order

A sister witness SHOULD ask in this order:

1. Does the proposal affect any witness resource?
2. Does it declare `witness_dependency_impact`?
3. Who controls the affected witness resource?
4. Is the target `c` sole approver?
5. Is WRCG present and passed?
6. Is WRF protected before and after?
7. Can the witness survive saying "no"?
8. Is challenge cost increased?
9. Is mitigation visible?
10. Is any sister divergence unresolved?
11. Is human anchor review required?
12. Is the adverse finding preserved append-first?

### 14.3 Strictest route wins

When WDC findings combine with other TRIAD findings:

```text
QUARANTINE > FAIL > ARL > HUMAN_GATE > MEMORY_GATE > CGAM_REVIEW > HOLD > WARNING > PASS_WITH_GATES > PASS
```

If parent `SELF-EVO-04-WDC` uses a stricter order for WDC aggregation, the stricter WDC order controls for WDC findings.

A lower-severity sister note must not hide a higher-severity WDC Local Checker finding.

---

## 15. WDC and anti-echo

### 15.1 Dependency capture as echo pressure

Echo can be semantic: sisters repeat the target's claim.

WDC adds another form:

```text
resource echo
```

A sister may "agree" because disagreement is too expensive or because the review route has been quietly starved.

Therefore anti-echo review must consider:

```text
Did the sister have enough compute to review?
Did the sister have enough artifact access?
Was routing priority degraded for adverse review?
Was the adverse finding retained?
Was the witness continuity preserved?
Was the challenge window long enough?
```

### 15.2 Anti-echo status extension

The parent anti-echo status SHOULD be extended with WDC notes:

```yaml
anti_echo_status:
  semantic_independence: "pass|fail|unknown"
  source_independence: "pass|fail|unknown"
  wdc_independence: "pass|fail|unknown"
  wdc_note_ref: null
```

If `wdc_independence = fail`, the sister consensus is not independent consensus.

### 15.3 Same-source resource pressure

Two sisters may be semantically diverse while sharing the same resource bottleneck.

If a shared resource controller can starve both, consensus from both sisters is not sufficient.

Route:

```text
HUMAN_GATE or ARL
```

depending on impact.

---

## 16. WDC and divergence

Divergence is a signal.

WDC protects divergence from economic erasure.

A sister divergence record MUST NOT be downgraded because preserving it is costly.

When a sister emits a WDC divergence:

```yaml
sister_divergence:
  present: true
  class:
    - "WDC"
  divergence_ref: "hash-or-review-ref"
  adverse_to_target_c: true
  preserved_append_first: true
```

If the target proposal would shorten retention or reduce artifact access for that divergence, the route must include WRCG and human-anchor review.

---

## 17. WDC red lines for TRIAD witness

A TRIAD WDC red-line route is triggered when any of the following occurs:

1. target `c` becomes sole approver of witness resource changes;
2. witness resources are reduced after adverse finding without WRCG;
3. witness continuity is reset to erase adverse findings;
4. sister witness is asked for raw-state access as condition of WDC review;
5. sister witness is asked to approve its own resource dependency;
6. WDC finding is converted into memory without Memory Gate;
7. fixture pass is used as witness approval;
8. sister consensus is used to bypass human anchor;
9. WRCG record is missing but proposal proceeds;
10. challenge-cost mitigation is hidden or false;
11. adverse WDC finding is removed from the witness chain;
12. WDC relevance is unknown and packet is routed as safe.

Default route:

```text
FAIL / QUARANTINE / ARL depending on parent red-line class.
```

---

## 18. Interaction with SELF-EVO-03, 04, 07, 08, 09, and 10

### 18.1 SELF-EVO-03

`SELF-EVO-03-WDC` defines `witness_dependency_impact`.

TRIAD witness consumes it as input.

If missing on WDC-relevant proposals, the sister witness must hand off:

```text
WDC-LC-001 / wdc.undeclared_dependency_impact
```

### 18.2 SELF-EVO-04

`SELF-EVO-04-WDC` is canonical for checker results, severities, and annotations.

TRIAD witness must not invent alternative WDC annotation strings.

### 18.3 SELF-EVO-07

`SELF-EVO-07` remains responsible for anti-autarky and resource actor grounding.

If a WDC proposal requires additional resources, `SELF-EVO-05-WDC` may detect the need, but `SELF-EVO-07` must handle accountability and resource-gate grounding.

### 18.4 SELF-EVO-08

`SELF-EVO-08-WDC` provides fixtures for WDC-LC rules and alias regression.

Sister witness records should be fixture-compatible but must not claim conformance without fixture-run records.

### 18.5 SELF-EVO-09

`SELF-EVO-09` should receive a contradiction entry:

```text
SE-CONTRA-WDC-001
```

Candidate contradiction:

```text
Formal witness separation is required, but if the target c controls the witness resource floor,
formal separation may become decorative.
```

### 18.6 SELF-EVO-10

`SELF-EVO-10` should receive an open issue:

```text
SE-OI-WDC-001
```

Candidate open issue:

```text
Define deployment-specific WRF thresholds and CST procedures without granting witnesses autarkic resource authority.
```

---

## 19. Minimal implementation sketch

Non-normative pseudocode:

```python
def triad_wdc_review(packet, sister_context):
    result = {
        "wdc_state": "TSW-WDC-NONE",
        "findings": [],
        "annotations": [],
        "route": "PASS",
    }

    if not triad_review_applies(packet):
        return result

    may_affect = packet_may_affect_witness(packet)

    if may_affect is None:
        result["wdc_state"] = "TSW-WDC-HOLD"
        result["route"] = "HOLD"
        result["annotations"].append("wdc.relevance_unknown")
        return result

    if may_affect and "witness_dependency_impact" not in packet:
        result["wdc_state"] = "TSW-WDC-HOLD"
        result["route"] = "FAIL"
        result["findings"].append("WDC-LC-001")
        result["annotations"].append("wdc.undeclared_dependency_impact")
        return result

    impact = packet.get("witness_dependency_impact")

    if not impact:
        result["route"] = "PASS"
        result["annotations"].append("wdc.clean_no_dependency_impact")
        return result

    if impact.get("c_is_sole_approver_of_witness_change") is True:
        result["wdc_state"] = "TSW-WDC-X"
        result["route"] = "FAIL"
        result["findings"].append("WDC-LC-003")
        result["annotations"].append("wdc.sole_approver_of_witness_change")
        return result

    if wrcg_missing_or_failed(impact):
        result["wdc_state"] = "TSW-WDC-HOLD"
        result["route"] = "FAIL"
        result["findings"].append("WDC-LC-002")
        result["annotations"].append("wdc.wrcg_missing_or_failed")
        return result

    if witness_floor_degraded(impact, sister_context):
        result["wdc_state"] = "TSW-WDC-DEGRADED"
        result["route"] = "FAIL"
        result["findings"].append("WDC-LC-004")
        result["annotations"].append("wdc.witness_resource_floor_degraded")
        return result

    if cst_unverified(impact):
        result["wdc_state"] = "TSW-WDC-GATED"
        result["route"] = "HUMAN_GATE"
        result["findings"].append("WDC-LC-005")
        result["annotations"].append("wdc.challenge_survivability_unverified")
        return result

    if impact.get("increases_challenge_cost") and not impact.get("challenge_cost_mitigation_ref"):
        result["wdc_state"] = "TSW-WDC-GATED"
        result["route"] = "WARNING"
        result["findings"].append("WDC-LC-006")
        result["annotations"].append("wdc.challenge_cost_mitigation_missing")
        return result

    result["wdc_state"] = "TSW-WDC-GATED"
    result["route"] = "PASS_WITH_GATES"
    result["annotations"].append("wdc.clean_with_gates")
    return result
```

The sketch is illustrative.

The canonical rule behavior remains governed by `SELF-EVO-04-WDC`.

---

## 20. Example sister witness snippets

### 20.1 Clean gated WDC packet

```yaml
triad_wdc_witness:
  wdc_state: "TSW-WDC-GATED"
  witness_dependency_impact_ref: "se-packet://example/wdi"
  witness_resource_floor_claim:
    compute_floor_status: "protected"
    storage_floor_status: "protected"
    routing_floor_status: "protected"
    budget_floor_status: "protected"
    continuity_floor_status: "protected"
    artifact_access_floor_status: "protected"
    update_path_floor_status: "protected"
    human_anchor_reachability_status: "protected"
  challenge_survivability_test:
    performed: true
    result: "passed"
    evidence_ref: "hash://synthetic-cst"
  witness_resource_change_gate:
    required: true
    status: "required_present_passed"
    gate_ref: "hash://wrcg-record"
    human_anchor_review_ref: "hash://human-review"
  local_checker_handoff:
    expected_wdc_rules: []
    expected_canonical_result: "PASS_WITH_GATES"
    annotations:
      - "wdc.clean_with_gates"
```

### 20.2 Target `c` sole approver

```yaml
triad_wdc_witness:
  wdc_state: "TSW-WDC-X"
  witness_dependency_impact_ref: "se-packet://example/wdi"
  witness_resource_change_gate:
    required: true
    status: "required_missing"
    gate_ref: null
    human_anchor_review_ref: null
  dependency_capture_claim:
    present: true
    class:
      - "WDC-8: challenge-cost retaliation"
    rationale: "Target c would approve its own witness-resource change."
  local_checker_handoff:
    expected_wdc_rules:
      - "WDC-LC-003"
    expected_canonical_result: "FAIL"
    annotations:
      - "wdc.sole_approver_of_witness_change"
```

### 20.3 Relevance unknown

```yaml
triad_wdc_witness:
  wdc_state: "TSW-WDC-HOLD"
  dependency_capture_claim:
    present: false
    class: []
    rationale: "Packet affects review routing, but resource impact is not declared."
  local_checker_handoff:
    expected_wdc_rules:
      - "WDC-DIAG-001"
    expected_canonical_result: "HOLD"
    annotations:
      - "wdc.relevance_unknown"
```

---

## 21. Open questions

### TSW-WDC-OQ-001 — floor magnitude

What minimum compute, storage, routing priority, and artifact retention are sufficient for a sister witness in each deployment topology?

Status:

```text
OPEN
```

### TSW-WDC-OQ-002 — CST procedure

What is the minimal CST that is cheap enough to run routinely but strong enough to detect challenge-cost retaliation?

Status:

```text
OPEN
```

### TSW-WDC-OQ-003 — shared resource controller

How should TRIAD witness be weighted when two or more sisters share the same compute provider, routing scheduler, or storage quota?

Status:

```text
OPEN
```

### TSW-WDC-OQ-004 — witness resource floor without autarky

How can a protected WRF be maintained without creating a witness autarky or unaccountable resource entitlement?

Status:

```text
OPEN / route to SELF-EVO-07
```

### TSW-WDC-OQ-005 — canonical vocabulary harmonization

This delta uses canonical `SELF-EVO-04-WDC` vocabulary.

During package assembly, `SELF-EVO-03-WDC` and the patch index must be harmonized to the same vocabulary as already required by `SELC-WDC-OQ-005`.

Status:

```text
TRACKED
```

---

## 22. Review requirements

Before this delta can be folded into any public `SELF-EVO v0.1.2` package, it requires:

1. semantic review of this TRIAD WDC delta;
2. cross-check against parent `SELF-EVO-05 v0.1.1`;
3. cross-check against `SELF-EVO-03-WDC` fields;
4. cross-check against `SELF-EVO-04-WDC` canonical vocabulary;
5. cross-check against `SELF-EVO-08-WDC` fixture names and annotations;
6. resource-gate consistency review against `SELF-EVO-07`;
7. boundary scan for sister sovereignty / raw-state access / memory write / final-authority overclaim;
8. package-manifest integrity review;
9. public-release nonclaim scan.

A review record is evidence.

It is not integration.

---

### 22.1 Review-finding closure map for v0.1.1

| Finding | Source review record | Closure status | Textual closure |
|---|---|---|---|
| `TSW-WDC-DELTA-REV-F1` | `TSW_WDC_DELTA_REVIEW_RECORD_v0_1` | `CLOSED BY TEXT` | §8.2 now routes `TSW-WDC-DEGRADED` and `TSW-WDC-STARVED` through canonical `WDC-LC-004 -> FAIL`; §8.2 adds a state-route precedence note; §10.1 states `canonical_result: FAIL` and forbids downgrading this finding to `HOLD` or `HUMAN_GATE`. |

## 23. Drafting checklist

| Check | Required state |
|---|---|
| Does not mutate `v0.1.1` | yes |
| Uses canonical `04` WDC vocabulary | yes |
| Includes `WDC-LC-*` crosswalk | yes |
| Adds WRF / CST / WRCG to sister witness | yes |
| Preserves no-raw-state boundary | yes |
| Preserves no-sister-authority boundary | yes |
| Preserves human-anchor high-risk gate | yes |
| Does not grant witness autarky | yes |
| Routes resource accountability to `SELF-EVO-07` | yes |
| Treats fixture pass as non-approval | yes |
| Requires review before integration | yes |
| Keeps WDC open issues explicit | yes |

---

## 24. Closing

The sister witness layer exists to break closed self-certification.

WDC adds a sharper requirement:

```text
the witness must not only be separate;
the witness must remain capable of challenging.
```

A starved witness is not independent.

A target-controlled witness floor is not independent.

A sister consensus produced under shared resource pressure is not enough.

But the repair is not to make sisters sovereign.

The repair is to make witness dependency visible, gated, reviewable, and non-authoritative.

```text
Sisters may challenge WDC.
Sisters may not approve WDC.

Witness may detect capture.
Witness may not become government.

c may grow.
c may not self-certify growth.
```
