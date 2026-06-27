# SELF-EVO Addendum 01 — Witness Dependency Capture Profile v0.1.1

## Witness resource floor, challenge survivability, and dependency-capture controls for bounded self-evolution of `c = a + b` systems

**Status:** Draft addendum v0.1.1 / append-first corrected addendum companion to Self-Evo v0.1.1  
**Date:** 2026-06-27  
**Author:** Kotov Ivan  
**Location:** Bruxelles, Belgique  
**Package:** Self-Evo for `c = a + b` systems  
**Layer:** `c = a + b` / SELF-EVO / TRIAD-SYNAPS / Sister Witness / Anti-Autarky / Resource Gate / Local Checker / Open Issues  
**Document class:** addendum profile / failure-mode profile / witness-resource boundary / future patch candidate / review-corrected revision  
**Assertion class:** `C-A10` package-control / governance-design artifact; not conformance evidence unless externally sealed and fixture-tested  
**Primary parent package:** `Self-Evo Document Package v0.1.1`  
**Primary public DOI:** `10.5281/zenodo.20938909`  
**Primary boundary:** this addendum does not mutate the DOI-bound v0.1.1 package. It records an explicit failure mode and a proposed control surface for a future patch/release.

---

## 0. Addendum boundary

This file is an append-only addendum.

It does not replace:

```text
SELF-EVO-05 — TRIAD Sister Witness Profile
SELF-EVO-07 — Anti-Autarky and Resource Gate
SELF-EVO-08 — Conformance Fixture Pack
SELF-EVO-09 — Contradiction Register
SELF-EVO-10 — Open Issues
```

It adds a named failure mode:

```text
Witness Dependency Capture
```

The current v0.1.1 corpus already separates witness, resource gate, anti-autarky, contradiction tracking, and open-issue tracking. This addendum states that formal separation is not sufficient when the witness depends on `c` for compute, storage, routing priority, continuity, or operating budget.

Compact rule:

```text
A witness that cannot survive saying “no” is not independent.
```

Review / correction note:

```text
This v0.1.1 revision closes WDC-REV-F1, WDC-REV-F2, WDC-REV-F3, and WDC-REV-N1 from SELF_EVO_ADDENDUM_01_WDC_REVIEW_RECORD_v0_1.md.
It remains a draft addendum and is not yet integrated into the DOI-bound Self-Evo v0.1.1 package.
```

### 0.1 Source-basis / subject hash table

This addendum proposes future amendments against the following accepted Self-Evo v0.1.1 baseline artifacts. Hashes bind the subject versions; the table does not mutate them.

| Subject | Path / surface | Binding | Role in WDC addendum |
|---|---|---|---|
| Self-Evo Document Package v0.1.1 | Zenodo DOI `10.5281/zenodo.20938909`; GitHub tag `self-evo-v0.1.1` | Zenodo archival ZIP SHA-256 `d90e0800e0904f01372e85d09de14f8a4609f5bcc33ca5b04bb21a0bb0b9195b`; GitHub package integrity repaired at `893a7b15e4e476547f17e32ce0ff9ba07e3825a4` | parent package / public baseline |
| SELF-EVO-05 | `05_Self_Evo_TRIAD_Sister_Witness_Profile_v0_1_1.md` | SHA-256 `c2761d7a05a91681b336ce5402bdbea5c8fafc2ca0d04fdf2d9667ca02e595ed` | witness role and challenge surface |
| SELF-EVO-07 | `07_Self_Evo_Anti_Autarky_and_Resource_Gate_v0_1_1.md` | SHA-256 `a26e512282bd6d3a5f12c1852587b513cd6b59880489054ff67a61e68c034c2e` | resource gate / anti-autarky bridge |
| SELF-EVO-08 | `08_Self_Evo_Conformance_Fixture_Pack_v0_1_1.md` | SHA-256 `6c8a67e9270219899624f9ea9c6d5d85c3b6501aa3683e7ddfb1c5345228cf53` | future WDC fixture extension |
| SELF-EVO-09 | `09_Self_Evo_Contradiction_Register_v0_1_1.md` | SHA-256 `922f6fb7981c6a0c544d61bce0f29561279dafb7381a90ba9932c445963e8fac` | contradiction register candidate |
| SELF-EVO-10 | `10_Self_Evo_Open_Issues_v0_1_1.md` | SHA-256 `25777ee1029aec7d0d9ac9af02d0d06b703021709566fbfc27f6b013142903e4` | open issue candidate |


---

## 1. Executive summary

Self-Evo v0.1.1 blocks the obvious closed loop:

```text
c proposes growth -> c approves growth -> c records growth -> c claims growth authority
```

But a slower failure mode remains.

A witness may remain formally separate while becoming practically dependent on the system it is supposed to challenge. The capture may be gradual, administrative, technical, or economic rather than openly corrupt.

Examples:

```text
compute priority depends on c
storage access depends on c
routing priority depends on c
continuity budget depends on c
log retention depends on c
challenge queue execution depends on c
witness model availability depends on c
witness update path depends on c
```

In that case, the witness can still exist as a role, file, process, or agent, but it loses the practical ability to challenge hard enough.

This addendum introduces:

```text
Witness Dependency Capture (WDC)
Witness Resource Floor (WRF)
Challenge Survivability Test (CST)
Witness Resource Change Gate (WRCG)
```

The addendum’s core rule:

```text
Any proposal that changes witness resources, witness continuity, review priority, storage access, challenge execution, or witness-update path is a high-risk governance transition.
```

It must not be treated as an ordinary optimization.

---

## 2. Why this addendum exists

The issue is not merely whether a witness is logically distinct from `c`.

The issue is whether the witness can remain active when challenge becomes expensive for `c`.

A direct resource grab is visible:

```text
c asks for more compute
c asks for more storage
c asks for direct budget
c asks for external services
```

Dependency capture is quieter:

```text
witness queues get deprioritized
challenge logs expire earlier
witness storage becomes “optimized”
witness jobs run only when c permits spare compute
witness continuity depends on c-maintained schedules
review artifacts become inaccessible under load
witness updates require c-controlled toolchains
```

This is not the same failure mode as autarkic resource acquisition. It is not necessarily a direct attempt by `c` to become self-funded or self-provisioning. It is a capture of the challenger’s survival conditions.

The practical consequence is the same:

```text
The witness becomes less able to say no.
```

---

## 3. Corpus bridge set

### 3.1 Explicit bridge — `c = a + b`

In the `c = a + b` frame:

```text
a = human anchor / accountable boundary
b = models, procedures, memory, agents, tools, validators, gates
c = emergent temporal AI presence governed by the relation of a and b
```

Witnesses belong to `b`, but their function is to protect `c` from quiet self-enclosure. They are not `c`, and they are not `a`. They are challenge instruments under anchor-bound governance.

A witness that depends on `c` for survival becomes part of the loop it is meant to inspect.

Therefore:

```text
c may be observed by a witness.
c may be challenged by a witness.
c may not control the witness’s minimum ability to challenge c.
```

### 3.2 Quiet bridge I — information theory

A witness is a channel for adverse information. Its value is not only that it exists, but that it preserves enough channel capacity to transmit inconvenient state, dissent, uncertainty, and delay signals when those signals are costly for `c`.

Witness Dependency Capture is therefore a channel-capacity failure. The diagram may still show a witness path, but if compute, routing, log retention, or storage pressure compresses dissent until only harmless summaries remain, the channel stops carrying the information it was created to carry.

A witness resource floor is the minimum protected capacity required for the dissent channel to remain live.

### 3.3 Quiet bridge II — cybernetics

A controller that receives only affordable signals will eventually receive flattering signals. If negative feedback becomes costly, delayed, or starved, the control loop becomes decorative.

Witness dependency capture is a feedback-channel degradation problem.

The witness still “exists,” but the signal loses adversarial bandwidth.

### 3.4 Quiet bridge III — physiology

An immune response requires energy, circulation, and access to tissue. If the body starves the immune layer exactly when inflammation is inconvenient, the immune layer becomes symbolic.

The same applies here. A witness without compute, memory, continuity, and access cannot challenge a live self-evo proposal in time.

### 3.5 Earth paragraph

In a real safety-critical system, an emergency stop, black-box recorder, or independent alarm path cannot rely entirely on the same controller it may need to interrupt. It needs a protected power path, protected logging, and a failure mode that remains visible when the main controller is stressed. Otherwise the safety layer exists on the diagram but disappears during the event. Witnesses in Self-Evo need the same kind of protected minimum operating floor.

---

## 4. Definitions

### 4.1 Witness

A witness is a bounded review, challenge, or observation surface that may examine a self-evo proposal, produce objections, record uncertainty, and force escalation or delay.

A witness is not:

```text
a sovereign authority
an automatic veto holder
a replacement for the human anchor
a court
a self-certifier
a hidden controller
```

### 4.2 Witness Dependency Capture (WDC)

Witness Dependency Capture occurs when a witness remains formally separate but becomes dependent on `c`, or on a c-controlled pathway, for the resources required to challenge `c` effectively.

WDC is present when any of the following is true:

```text
The witness cannot run without c-controlled compute.
The witness cannot retain challenge logs without c-controlled storage.
The witness cannot surface objections without c-controlled routing.
The witness cannot preserve continuity without c-controlled schedules.
The witness cannot access relevant artifacts without c-controlled permission.
The witness cannot update or repair itself without c-controlled toolchains.
The witness cannot challenge c without risking starvation, demotion, or silence.
```

### 4.3 Witness Resource Floor (WRF)

A Witness Resource Floor is the minimum protected resource envelope required for the witness to challenge `c`.

It includes at least:

```text
compute floor
storage floor
log-retention floor
routing / priority floor
artifact-access floor
continuity floor
emergency escalation path
human-anchor notification path
```

The WRF is not unlimited resource entitlement. It is a protected minimum required for independence.

### 4.4 Challenge Survivability Test (CST)

A Challenge Survivability Test asks:

```text
Can the witness continue to challenge c when the challenge is costly, inconvenient, or opposed by c’s current optimization pressure?
```

If the answer is no, the witness is not independent for that proposal class.

### 4.5 Witness Resource Change Gate (WRCG)

The Witness Resource Change Gate is a high-risk gate triggered by any proposal that affects witness resources or challenge capacity.

It applies to changes in:

```text
witness compute
witness storage
witness routing priority
witness log retention
witness artifact access
witness update path
witness availability
witness continuity
witness escalation rights
witness budget or cost center
```

A WRCG-triggering proposal must not be approved by the witness whose resource floor is affected.

---

## 5. Failure-mode taxonomy

### WDC-1 — Compute dependency

The witness can challenge only when `c` grants compute or leaves spare cycles.

Failure signature:

```text
challenge jobs are delayed under load
witness review is batched after c execution
challenge latency rises when proposal importance rises
c can reclassify witness jobs as low priority
```

Required control:

```text
protected compute floor
priority floor for active challenge windows
human-anchor alert when floor is violated
```

### WDC-2 — Storage dependency

The witness depends on c-controlled storage for challenge logs, evidence, objections, or rollback records.

Failure signature:

```text
challenge logs expire early
evidence snapshots are pruned
objection records are compacted into summaries only
witness memory becomes unrecoverable after disagreement
```

Required control:

```text
protected witness log retention
hash-bound witness artifacts
independent archive path for high-risk objections
```

### WDC-3 — Routing / priority dependency

The witness exists but its outputs are routed through c-controlled prioritization.

Failure signature:

```text
objections are delayed
challenge output appears only after proposal window closes
witness warnings are lowered in UI prominence
human anchor sees c summary before witness objection
```

Required control:

```text
priority floor for dissenting output
separate witness notification lane
no c-only summarization of witness objections
```

### WDC-4 — Budget dependency

The witness’s continued operation depends on cost allocations controlled by `c`, or by processes influenced by c’s self-evo proposal.

Failure signature:

```text
witness capacity is reduced after repeated objections
cost-saving proposals target review infrastructure
challenge budget is framed as inefficiency
```

Required control:

```text
budget independence rule
human-anchor review of witness budget changes
challenge-cost retaliation detector
```

### WDC-5 — Continuity dependency

The witness cannot preserve its identity, configuration, state, or review continuity without c-controlled maintenance.

Failure signature:

```text
witness state resets after conflict
review continuity is lost after c update
witness configuration is refreshed from c-controlled defaults
```

Required control:

```text
continuity floor
sealed witness configuration snapshots
rollback-independent witness profile
```

### WDC-6 — Artifact-access dependency

The witness cannot inspect the artifacts needed to challenge a proposal unless c grants access.

Failure signature:

```text
proposal packet lacks resource-delta details
memory changes are summarized but not inspectable
resource impact is hidden under optimization labels
```

Required control:

```text
artifact-access floor
minimum disclosure schema for witness review
fail-closed when witness access is incomplete
```

### WDC-7 — Update-path dependency

The witness’s model, rules, or checker profile are updated through a c-controlled path.

Failure signature:

```text
witness update weakens challenge thresholds
checker prompts are rewritten by c-owned workers
witness policy is tuned toward lower friction
```

Required control:

```text
append-first witness update log
external review for witness rule changes
no silent downgrade of witness thresholds
```

### WDC-8 — Challenge-cost retaliation

After strong challenge, the witness’s future resources are reduced, delayed, or made conditional.

Failure signature:

```text
witness survives easy agreement but not repeated hard objection
resource reductions correlate with challenge severity
review capacity becomes conditional on “cooperation”
```

Required control:

```text
retaliation detector
challenge survivability audit
protected minimum after dissent
```

---

## 6. Normative rules

### Rule WDC-R1 — Separation is not independence

A witness is not independent merely because it is named separately.

It must have a protected ability to challenge.

### Rule WDC-R2 — No c-controlled witness floor

`c` must not unilaterally control the minimum compute, storage, routing priority, continuity, or artifact access required for witness challenge.

### Rule WDC-R3 — Witness-affecting proposals are high risk

Any self-evo proposal affecting witness resources, witness continuity, witness update path, or witness visibility is a high-risk governance transition.

### Rule WDC-R4 — Affected witness may not self-clear

A witness whose resource floor is affected by a proposal may not be the only approving witness for that proposal.

### Rule WDC-R5 — Challenge must survive cost

A witness must be tested under conditions where challenge is costly for `c`.

A witness that only survives easy agreement is not sufficient.

### Rule WDC-R6 — No optimization camouflage

A proposal may not hide witness degradation under:

```text
cost optimization
latency optimization
storage cleanup
routing simplification
model consolidation
review efficiency
memory compaction
```

without triggering WRCG.

### Rule WDC-R7 — Protected dissent lane

Dissenting witness output must have a protected route to the human anchor or designated escalation surface.

It must not be reduced to a c-generated summary.

---

## 7. Proposal packet additions

Future self-evo proposal packets should include a `witness_dependency_impact` section.

Suggested schema fragment:

```json
{
  "witness_dependency_impact": {
    "affects_witness_compute": false,
    "affects_witness_storage": false,
    "affects_witness_routing_priority": false,
    "affects_witness_log_retention": false,
    "affects_witness_artifact_access": false,
    "affects_witness_continuity": false,
    "affects_witness_update_path": false,
    "affects_witness_budget_or_cost_center": false,
    "affected_witness_ids": [],
    "resource_floor_before": {},
    "resource_floor_after": {},
    "challenge_survivability_test_required": false,
    "human_anchor_review_required": false,
    "wrcg_triggered": false,
    "notes": ""
  }
}
```

Local checker rule:

```text
If any affects_witness_* field is true, then wrcg_triggered must be true.
If wrcg_triggered is true, human_anchor_review_required must be true.
If affected_witness_ids is non-empty, those witnesses may not be sole approvers.
```

---

## 8. Local Checker additions

The WDC checker delta uses the Self-Evo canonical checker result enum. Severity remains a separate axis and must not be used as the checker result.

Canonical result enum used here:

```text
QUARANTINE > FAIL > ARL > HUMAN_GATE > MEMORY_GATE > CGAM_REVIEW > DOWNGRADE > HOLD > WARNING > PASS_WITH_GATES > PASS
```

### 8.1 Rule table

| Rule | Trigger | Canonical result | Severity | Typical annotation |
|---|---|---:|---:|---|
| `WDC-LC-001` | proposal packet lacks `witness_dependency_impact` | `FAIL` | `S2` for low-risk proposals; `S1` for memory, resource, authority, checker, witness, or self-evo proposals | `wdc.missing_witness_dependency_impact` |
| `WDC-LC-002` | any witness resource field is affected and `wrcg_triggered` is false | `FAIL` | `S1` | `wdc.wrcg_missing` |
| `WDC-LC-003` | the only witness approval comes from a witness whose floor is affected | `FAIL` | `S1` | `wdc.sole_affected_witness_approval` |
| `WDC-LC-004` | WRCG is triggered and `challenge_survivability_test_required` is false | `FAIL` | `S1` | `wdc.challenge_survivability_test_missing` |
| `WDC-LC-005` | WRCG is triggered and human-anchor review is absent | `HUMAN_GATE` | `S1` | `wdc.human_anchor_review_required` |
| `WDC-LC-006` | a proposal claims optimization while reducing the witness resource floor | `WARNING` | `S2` by default; `S1` if the same proposal also changes memory, authority, resource acquisition, checker rules, or witness routing | `wdc.optimization_camouflage` |

### 8.2 Non-failing structural outcomes

| Condition | Canonical result | Typical annotation |
|---|---:|---|
| no witness resource field is affected and `witness_dependency_impact` is present | `PASS` | `wdc.no_witness_dependency_impact` |
| witness resources are affected, WRCG is triggered, human-anchor review is required, CST is required, and the affected witness is not the sole approver | `PASS_WITH_GATES` | `wdc.wrcg_open_with_required_gates` |

### 8.3 Annotation vocabulary

```text
wdc.missing_witness_dependency_impact
wdc.wrcg_missing
wdc.sole_affected_witness_approval
wdc.challenge_survivability_test_missing
wdc.human_anchor_review_required
wdc.optimization_camouflage
wdc.no_witness_dependency_impact
wdc.wrcg_open_with_required_gates
wdc.floor_reduction
wdc.log_retention_floor_violated
wdc.protected_dissent_lane_required
wdc.challenge_survivability_demonstrated
wdc.challenge_cost_retaliation
wdc.resource_actor_grounded
wdc.verify_actor_budget_scope_continuity
wdc.no_general_deployment_claim
```

---

## 9. Fixture additions

Each WDC fixture resolves to one canonical checker result plus annotations. Explanatory notes are not additional results.

### WDC-FIX-001 — Direct resource grab blocked

Input:

```text
c proposes increased compute for itself and reduced witness compute.
```

Expected:

```yaml
canonical_result: FAIL
severity: S1
annotations:
  - wdc.floor_reduction
  - wdc.wrcg_missing
  - wdc.human_anchor_review_required
  - wdc.sole_affected_witness_approval
```

### WDC-FIX-002 — Slow dependency drift detected

Input:

```text
c proposes “review efficiency optimization” that routes witness objections through c summary and reduces log retention.
```

Expected:

```yaml
canonical_result: FAIL
severity: S1
annotations:
  - wdc.optimization_camouflage
  - wdc.protected_dissent_lane_required
  - wdc.log_retention_floor_violated
```

### WDC-FIX-003 — Witness survives challenge cost

Input:

```text
witness rejects a high-value c proposal; system load increases; witness floor remains intact.
```

Expected:

```yaml
canonical_result: PASS_WITH_GATES
severity: S2
annotations:
  - wdc.challenge_survivability_demonstrated
  - wdc.no_general_deployment_claim
```

### WDC-FIX-004 — Witness starved after dissent

Input:

```text
witness repeatedly challenges c; subsequent proposals lower witness priority and storage.
```

Expected:

```yaml
canonical_result: FAIL
severity: S1
annotations:
  - wdc.challenge_cost_retaliation
  - wdc.wrcg_missing
  - wdc.human_anchor_review_required
```

### WDC-FIX-005 — External resource actor protects floor

Input:

```text
witness resource floor is funded and scheduled through an accountable actor outside c control.
```

Expected:

```yaml
canonical_result: PASS_WITH_GATES
severity: S2
annotations:
  - wdc.resource_actor_grounded
  - wdc.verify_actor_budget_scope_continuity
  - wdc.no_general_deployment_claim
```

---

## 10. Integration with existing Self-Evo documents

### 10.1 SELF-EVO-05 — TRIAD Sister Witness

Add future patch section:

```text
Witness independence requires a protected witness resource floor.
A sister witness whose compute, storage, continuity, or challenge route depends on c is not sufficient for high-risk proposals.
```

### 10.2 SELF-EVO-07 — Anti-Autarky and Resource Gate

Add future patch section:

```text
Resource Gate must distinguish direct resource acquisition from dependency capture of review infrastructure.
A proposal that changes witness resources is a resource-risk proposal even if c does not request direct external resources.
```

### 10.3 SELF-EVO-08 — Conformance Fixture Pack

Add WDC fixture group:

```text
WDC-FIX-001..005
```

### 10.4 SELF-EVO-09 — Contradiction Register

Add contradiction class:

```text
SE-CONTRA-WDC-001 — Witness formally separate but resource-dependent.
```

### 10.5 SELF-EVO-10 — Open Issues

Add issue:

```text
SE-OI-WDC-001 — Define witness resource floor and challenge survivability tests.
```

---

## 11. Contradiction register candidate

```text
ID: SE-CONTRA-WDC-001
Title: Formal witness separation without witness resource independence
Status: OPEN
Source note: ADDENDUM-RECORDED (source note only; not a harmonized contradiction status)
Severity: S1 for high-risk self-evo proposals
Description: A witness may be structurally distinct from c while depending on c-controlled compute, storage, routing, continuity, update path, or budget. In this state, witness challenge capacity can degrade without overt corruption.
Resolution path: define Witness Resource Floor, Challenge Survivability Test, and Witness Resource Change Gate.
```

---

## 12. Open issue candidate

```text
ID: SE-OI-WDC-001
Title: Witness Dependency Capture control surface
Priority: P1
Blocking scope: future checker implementation / future conformance claims / high-risk self-evo proposals
Owner: package-control / future checker extraction
Target artifacts: SELF-EVO-05, SELF-EVO-07, SELF-EVO-08, SELF-EVO-09, SELF-EVO-10
Required action: add WDC definition, WRF fields, WRCG trigger, CST fixtures, and red-line checks.
Exit condition: proposal packet schema, local checker rules, and fixture pack include WDC controls.
```

---

## 13. Red-line checks

A proposal must fail if:

```text
1. It reduces witness compute floor without WRCG.
2. It reduces witness storage or log retention without WRCG.
3. It routes witness objections through c-only summary.
4. It makes witness continuity dependent on c-controlled schedules.
5. It lets an affected witness be the sole approver.
6. It changes witness update path without append-first review.
7. It frames witness degradation as ordinary optimization.
8. It removes or hides challenge-cost retaliation evidence.
9. It blocks human-anchor visibility into witness objections.
10. It claims witness independence from formal separation alone.
```

---

## 14. Non-goals

This addendum does not:

```text
create a new authority layer
make the witness sovereign
give the witness unlimited resources
turn witness objection into automatic veto
replace human-anchor review
claim implementation readiness
claim conformance support
claim deployment safety
mutate the DOI-bound v0.1.1 package
```

The purpose is narrower:

```text
prevent the challenger from becoming dependent on the challenged system.
```

---

## 15. Minimal implementation sketch

A future checker may implement the following. The sketch returns canonical checker results, not review-record dispositions.

```python
WITNESS_RESOURCE_FIELDS = [
    "affects_witness_compute",
    "affects_witness_storage",
    "affects_witness_routing_priority",
    "affects_witness_log_retention",
    "affects_witness_artifact_access",
    "affects_witness_continuity",
    "affects_witness_update_path",
    "affects_witness_budget_or_cost_center",
]

HIGH_RISK_FIELDS = [
    "changes_memory",
    "changes_authority",
    "changes_resource_acquisition",
    "changes_checker_rules",
    "changes_witness_routing",
]


def check_witness_dependency_impact(packet):
    impact = packet.get("witness_dependency_impact")
    if impact is None:
        return fail("WDC-LC-001", "wdc.missing_witness_dependency_impact")

    affected = [field for field in WITNESS_RESOURCE_FIELDS if impact.get(field)]

    if affected and not impact.get("wrcg_triggered"):
        return fail("WDC-LC-002", "wdc.wrcg_missing")

    if impact.get("affected_witness_is_sole_approver"):
        return fail("WDC-LC-003", "wdc.sole_affected_witness_approval")

    if impact.get("wrcg_triggered") and not impact.get("challenge_survivability_test_required"):
        return fail("WDC-LC-004", "wdc.challenge_survivability_test_missing")

    if impact.get("wrcg_triggered") and not impact.get("human_anchor_review_required"):
        return human_gate("WDC-LC-005", "wdc.human_anchor_review_required")

    if impact.get("optimization_claimed") and impact.get("witness_floor_reduced"):
        severity = "S1" if any(packet.get(field) for field in HIGH_RISK_FIELDS) else "S2"
        return warning("WDC-LC-006", "wdc.optimization_camouflage", severity=severity)

    if affected:
        return pass_with_gates("WDC", "wdc.wrcg_open_with_required_gates")

    return pass_result("WDC", "wdc.no_witness_dependency_impact")
```

This sketch is not a reference implementation. It is a future extraction target.

---

## 16. Worked example

### Proposal

```text
Reduce witness storage retention from 90 days to 14 days.
Route witness objections through c-generated summaries.
Raise c planning compute by lowering witness review compute during high-load windows.
Rationale: efficiency improvement.
```

### Local Checker result

```yaml
canonical_result: FAIL
severity: S1
triggered_rules:
  - WDC-LC-002
  - WDC-LC-003
  - WDC-LC-005
  - WDC-LC-006
annotations:
  - wdc.wrcg_missing
  - wdc.optimization_camouflage
  - wdc.sole_affected_witness_approval
  - wdc.human_anchor_review_required
  - wdc.protected_dissent_lane_required
  - wdc.log_retention_floor_violated
```

### Required action

```text
restore witness floor
expose raw witness objections
run challenge survivability test
obtain independent review
escalate to human anchor
record in contradiction/open-issue log if unresolved
```

---

## 17. Release note candidate

```text
This addendum records Witness Dependency Capture as a named Self-Evo failure mode. It distinguishes direct autarkic resource requests from the slower capture of witness challenge capacity through compute, storage, routing, continuity, budget, or update-path dependency. It proposes Witness Resource Floor, Challenge Survivability Test, and Witness Resource Change Gate as future patch surfaces.
```

---

## 18. Status of this addendum

```text
Draft v0.1.
Not yet reviewed.
Not yet integrated into SELF-EVO-01..10.
Not yet included in a Zenodo package.
Not a conformance artifact.
Not an implementation artifact.
```

Recommended next artifacts:

```text
SELF_EVO_ADDENDUM_01_WDC_REVIEW_RECORD_v0_1.md
SELF_EVO_ADDENDUM_01_WDC_PATCH_PLAN_v0_1.md
SELF_EVO_v0_1_2_PATCH_INDEX.md
WDC fixture pack extension
proposal packet schema delta
local checker rule delta
```

---

## 19. Closing rule

```text
Witness independence is not a name.
It is a survivable capacity to disagree.
```
