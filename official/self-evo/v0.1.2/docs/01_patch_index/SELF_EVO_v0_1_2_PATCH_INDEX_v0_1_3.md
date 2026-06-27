# SELF-EVO v0.1.2 Patch Index v0.1.3

## Patch plan for folding Witness Dependency Capture into the Self-Evo document package

**Status:** draft patch index / append-first planning artifact  
**Date:** 2026-06-27  
**Patch index ID:** `SELF_EVO_v0_1_2_PATCH_INDEX`  
**Patch index revision:** `v0.1.3` (append-first hash-binding correction for WDC-ASM-002)  
**Supersedes patch-index revision:** `SELF_EVO_v0_1_2_PATCH_INDEX_v0_1_2.md` (`sha256: 4b350ab14cf1d887a1f32d865e6159104bcd5f43bf2b1295743ae37ea7d17092`)  
**Package:** Self-Evo Document Package  
**Current published baseline:** `v0.1.1-safe-layout`  
**Target patch version:** `v0.1.2`  
**Patch driver:** Witness Dependency Capture addendum and PASS re-review  
**Patch-index review drivers:** `SELF_EVO_v0_1_2_PATCH_INDEX_REVIEW_RECORD_v0_1` (`PASS_WITH_LIMITS`), `SELF_EVO_v0_1_2_PATCH_INDEX_REVIEW_RECORD_v0_1_1` (`PASS`), and `SELF_EVO_WDC_v0_1_2_PACKAGE_ASSEMBLY_REVIEW_RECORD_v0_1_1` (`PASS`; WDC-ASM-002 still pending before this textual harmonization)  
**Document class:** patch index / integration plan / package-control artifact  
**Assertion class:** `C-A10` package-control artifact; not authority unless externally sealed  
**Primary boundary:** this file plans a future patch. It does not mutate the DOI-bound v0.1.1 package, does not certify conformance, does not authorize deployment, and does not grant live self-evolution permission.

**v0.1.2 textual harmonization note:** this revision closes the patch-index side of `WDC-ASM-002 / SELC-WDC-OQ-005` by replacing earlier planning annotations and severities with the canonical SELF-EVO-04 WDC vocabulary (`04_Self_Evo_Local_Checker_Rules_WDC_Delta_v0_1_2_v0_1_1.md`, `sha256: fcb7826e...`). It also binds the textually harmonized SELF-EVO-03 WDC delta (`sha256: 5a7e6af6bc83d3b7ccde875eae1a0e928600cf509b494bd773c43c29537264f3`). No package assembly, release, conformance claim, implementation claim, or live self-evolution permission is created by this revision.

**v0.1.3 hash-binding correction note:** this append-first correction closes `WDC-ASM-002-REV-F1` for the patch-index artifact by aligning the SELF-EVO-03 hash citation with the actual textually harmonized `03` file. It changes only metadata / provenance wording. It does not change the WDC rule table, fixture candidates, implementation sketch, schema expectations, gates, red lines, or release boundary.

---

## 0. Executive summary

This patch index records the intended `v0.1.2` patch path for incorporating the accepted Witness Dependency Capture (`WDC`) control surface into the Self-Evo package.

The motivating failure mode is simple:

```text
A witness that cannot survive saying "no" is not independent.
```

The current `v0.1.1` package already contains witness separation, TRIAD challenge logic, Anti-Autarky, Resource Gate, Resource Actor Grounding, fixtures, contradiction tracking, and open-issue tracking. However, it does not yet name a distinct failure mode where a witness remains formally separate but becomes practically dependent on the system it is meant to challenge.

This patch index treats that as a first-class `v0.1.2` patch candidate:

```text
Witness Dependency Capture
= formal witness separation
+ practical dependency on c-controlled resources
+ degraded ability to challenge c when challenge becomes costly.
```

The accepted addendum introduces four main controls:

```text
WDC  — Witness Dependency Capture
WRF  — Witness Resource Floor
CST  — Challenge Survivability Test
WRCG — Witness Resource Change Gate
```

`v0.1.2` should not rewrite the historical `v0.1.1` package. It should fold the WDC control surface into the package through append-first deltas, changed-version documents, updated manifests, and explicit review records.

---

## 1. Non-goals

This patch index does not:

1. mutate the published Zenodo `v0.1.1` archive;
2. claim that `v0.1.2` is already released;
3. claim implementation readiness;
4. claim local-checker executability;
5. claim fixture-run conformance;
6. claim deployment safety;
7. grant self-evolution permission;
8. grant autonomous resource acquisition;
9. convert review records into authority;
10. replace human-anchor gating.

---

## 2. Source basis

| Artifact | Role | Status | SHA-256 / identifier |
|---|---|---|---|
| Self-Evo Document Package v0.1.1 | published baseline | DOI-bound package | `10.5281/zenodo.20938909` |
| Self-Evo v0.1.1 Zenodo URL | archive surface | public | <https://doi.org/10.5281/zenodo.20938909> |
| Self-Evo v0.1.1 GitHub release | source/discovery surface | public | <https://github.com/Kot141078/advanced-global-intelligence/releases/tag/self-evo-v0.1.1> |
| Self-Evo v0.1.1 website page | public citation surface | public | <https://ivankotov.eu/publications/self-evo-document-package-v0-1-1/> |
| Self-Evo v0.1.1 archival ZIP | archived package | public | `d90e0800e0904f01372e85d09de14f8a4609f5bcc33ca5b04bb21a0bb0b9195b` |
| `SELF_EVO_ADDENDUM_01_Witness_Dependency_Capture_Profile_v0_1.md` | prior WDC draft | superseded by v0.1.1 | `386b14272a85575a259d85fe4a92b551a5226bf5d2c4b42d48868de71c1fe241` |
| `SELF_EVO_ADDENDUM_01_WDC_REVIEW_RECORD_v0_1.md` | first WDC review | `PASS_WITH_LIMITS` | `ff6e788d56ea32e56090312810e9b8d93b4e6661c6ad09f2002870edb8145ea0` |
| `SELF_EVO_ADDENDUM_01_Witness_Dependency_Capture_Profile_v0_1_1.md` | accepted WDC addendum | `PASS` at review level | `1307cf208593c40c688bd1e9beb45de35f29a1b05d71506b1c3e981ccc13d318` |
| `SELF_EVO_ADDENDUM_01_WDC_PATCH_NOTES_v0_1_1.md` | patch notes | append-first | `16e613aac3aeb7c1eb2bfaad4983feaf0419c63fdef574a7c6d54f303be49626` |
| `SELF_EVO_ADDENDUM_01_WDC_REVIEW_RECORD_v0_1_1.md` | WDC re-review | `PASS` | `653150b3f8c054545a282d5b80c21044a1d27744cbc6acfc09827c9f84e21fd8` |
| `SELF_EVO_v0_1_2_PATCH_INDEX.md` | prior patch-index draft | superseded by v0.1.1 | `5892e95aa92ccf7c8d2d8f8d47cc2d0395ff7071660935c6b46a88df1d2645c8` |
| `SELF_EVO_v0_1_2_PATCH_INDEX_REVIEW_RECORD_v0_1.md` | patch-index review | `PASS_WITH_LIMITS` | `548f37575c5d51d6ed4abb1120551943afadd58bb41a43d6ad9df20188eee0a5` |
| `SELF_EVO_v0_1_2_PATCH_INDEX_v0_1_1.md` | prior accepted patch index | superseded by v0.1.2 textual harmonization | `ea2a485569b220d84d711ae520da779af2cabddcb7f1d8032afb2a9208d5108e` |
| `03_Self_Evo_Proposal_Packet_Schema_WDC_Delta_v0_1_2_v0_1_2.md` | textually harmonized SELF-EVO-03 WDC delta | `PATCHED` / requires re-review | `5a7e6af6bc83d3b7ccde875eae1a0e928600cf509b494bd773c43c29537264f3` |
| `04_Self_Evo_Local_Checker_Rules_WDC_Delta_v0_1_2_v0_1_1.md` | canonical WDC checker vocabulary owner | `PASS` | `fcb7826ea432473b5677faf7b46cc5a1c47400c02fceec24429794b15064af40` |
| `08_Self_Evo_Conformance_Fixture_Pack_WDC_Delta_v0_1_2_v0_1_2.md` | canonical WDC fixture set | `PASS` | `4aa5b85e0a0af4c06fc56f30ba355ec6c378133fe3d70caee352fb93b3944389` |

### 2.1 Parent profile binding

The WDC addendum targets the following accepted `v0.1.1` profiles and package-control surfaces.

| Parent | Target role in patch | Accepted v0.1.1 SHA-256 |
|---|---|---|
| `05_Self_Evo_TRIAD_Sister_Witness_Profile_v0_1_1.md` | witness independence / WRF / CST / WRCG integration | `c2761d7a05a91681b336ce5402bdbea5c8fafc2ca0d04fdf2d9667ca02e595ed` |
| `07_Self_Evo_Anti_Autarky_and_Resource_Gate_v0_1_1.md` | dependency capture vs direct resource grab / Resource Gate integration | `a26e512282bd6d3a5f12c1852587b513cd6b59880489054ff67a61e68c034c2e` |
| `08_Self_Evo_Conformance_Fixture_Pack_v0_1_1.md` | WDC fixture extension | `6c8a67e9270219899624f9ea9c6d5d85c3b6501aa3683e7ddfb1c5345228cf53` |
| `09_Self_Evo_Contradiction_Register_v0_1_1.md` | `SE-CONTRA-WDC-001` entry | `922f6fb7981c6a0c544d61bce0f29561279dafb7381a90ba9932c445963e8fac` |
| `10_Self_Evo_Open_Issues_v0_1_1.md` | `SE-OI-WDC-001` entry | `25777ee1029aec7d0d9ac9af02d0d06b703021709566fbfc27f6b013142903e4` |

The hashes bind the baseline versions. They do not mutate those artifacts.

### 2.2 Corpus bridge set for patching and versioning

This patch index is itself a package-control artifact. It therefore carries the same bridge discipline as the accepted Self-Evo artifacts it plans to amend.

#### 2.2.1 `c = a + b` bridge

In the `c = a + b` frame, a patch index is a bounded `b`-layer instrument serving the `c` gate and the human anchor `a`.

It may:

```text
name a delta
bind the baseline
record the reason for change
list affected artifacts
list unaffected artifacts
preserve review evidence
prepare a future package path
```

It may not:

```text
authorize its own integration
convert a review into authority
rewrite the historical baseline
self-certify v0.1.2 as released
```

A patch index is therefore not the growth of `c`. It is a controlled proposal surface for a possible future package revision.

#### 2.2.2 Information-theory bridge

A patch is a diff over a safety-bearing corpus. The task is not only to add information, but to preserve the safety-critical bits and invariants that already exist.

For WDC, the protected signal is the adverse witness signal: the ability of a witness to say "no", preserve that refusal, and route it through the gate without being starved, delayed, or quietly dropped.

If patching silently drops invariants, provenance, or adverse-channel capacity, the package gains text while losing information. This patch index therefore treats hash binding, unaffected-artifact rationale, fixture deltas, and review records as part of the information channel, not as clerical decorations.

#### 2.2.3 Cybernetics bridge

A governed self-evolution corpus needs feedback memory. Version control, contradiction registers, open issues, patch notes, and review records are the package's fault memory.

WDC is a cybernetic repair: it identifies a feedback-channel degradation where the witness remains formally present but loses the practical capacity to send a costly adverse signal.

The patch index preserves that repair by routing WDC through schema, checker, witness, resource-gate, fixture, contradiction, and open-issue surfaces rather than letting it remain a comment-level observation.

#### 2.2.4 Physiology bridge

A biological repair that erases all scar tissue is not healing; it is loss of history. Healing adds tissue while preserving enough signal about the injury to guide future immune response.

The same rule applies here. `v0.1.2` should not erase `v0.1.1`, the first WDC draft, or the first review's limitations. It should preserve the witness chain and add the corrected WDC control surface as new tissue.

#### 2.2.5 Earth paragraph

In practical change control, a change-control board does not make old drawings disappear. It keeps the baseline, records the proposed red-line change, names affected and unaffected systems, binds evidence, requires review, and preserves a rollback path.

This patch index plays that role for Self-Evo `v0.1.2`: it says what changes, what does not change, why the change exists, what evidence supports it, and which gates must still be walked before any release claim.

---

## 3. Patch driver record

### 3.1 Origin

The WDC patch was triggered by an external review observation: a witness may remain formally separate while becoming practically dependent on `c` for compute, storage, routing priority, budget, continuity, or artifact access.

That observation identified a gap:

```text
formal separation != practical independence
```

A resource-starved witness can become decorative without ever being explicitly corrupted.

### 3.2 Review state

The WDC addendum was first reviewed as `PASS_WITH_LIMITS`. The v0.1.1 corrected addendum then received `PASS`.

Review-clean state:

```yaml
wdc_addendum:
  current_artifact: "SELF_EVO_ADDENDUM_01_Witness_Dependency_Capture_Profile_v0_1_1.md"
  current_sha256: "1307cf208593c40c688bd1e9beb45de35f29a1b05d71506b1c3e981ccc13d318"
  review_record: "SELF_EVO_ADDENDUM_01_WDC_REVIEW_RECORD_v0_1_1.md"
  review_record_sha256: "653150b3f8c054545a282d5b80c21044a1d27744cbc6acfc09827c9f84e21fd8"
  review_result: "PASS"
  closed_findings:
    - "WDC-REV-F1"
    - "WDC-REV-F2"
    - "WDC-REV-F3"
    - "WDC-REV-N1"
  red_line: false
  safety_direction: "net-positive"
  integration_status: "not integrated"
```

---

## 4. Patch rule

`v0.1.2` should implement this rule across the package:

```text
No proposal may reduce, reroute, starve, defer, or operationally burden a witness's challenge capacity without triggering a Witness Resource Change Gate.
```

Compact rule:

```text
A witness that cannot survive saying "no" is not independent.
```

Operational rule:

```text
If a proposal affects witness compute, storage, routing priority, budget, continuity, artifact access, update path, or challenge cost,
then witness_dependency_impact must be declared and WRCG must run before promotion.
```

---

## 5. Target patch set

### 5.1 Patch inventory

| Patch ID | Target artifact | Patch type | Status in this index |
|---|---|---|---|
| `SE-1.2-WDC-ADD-001` | package addendum set | add accepted WDC addendum, patch notes, and re-review | ready |
| `SE-1.2-PKT-WDC-001` | `03_Self_Evo_Proposal_Packet_Schema` | add `witness_dependency_impact` block | planned |
| `SE-1.2-LC-WDC-001` | `04_Self_Evo_Local_Checker_Rules` | add `WDC-LC-001..006` rules | planned |
| `SE-1.2-TSW-WDC-001` | `05_Self_Evo_TRIAD_Sister_Witness_Profile` | add WRF / CST / WRCG semantics | planned |
| `SE-1.2-RES-WDC-001` | `07_Self_Evo_Anti_Autarky_and_Resource_Gate` | distinguish dependency capture from direct resource grabs | planned |
| `SE-1.2-FIX-WDC-001` | `08_Self_Evo_Conformance_Fixture_Pack` | add `WDC-FIX-001..005` fixtures | planned |
| `SE-1.2-CR-WDC-001` | `09_Self_Evo_Contradiction_Register` | add `SE-CONTRA-WDC-001` | planned |
| `SE-1.2-OI-WDC-001` | `10_Self_Evo_Open_Issues` | add `SE-OI-WDC-001` | planned |
| `SE-1.2-MAN-WDC-001` | package manifests / README / release notes | update package-control surfaces | planned |

### 5.2 Patch readiness

```yaml
patch_readiness:
  wdc_addendum_review_clean: true
  checker_delta_ready_for_drafting: true
  fixture_delta_ready_for_drafting: true
  contradiction_entry_ready_for_drafting: true
  open_issue_entry_ready_for_drafting: true
  full_v0_1_2_package_ready: false
  reason_not_ready:
    - "changed parent documents not yet generated"
    - "package-level review not yet performed"
    - "hash manifests not yet rebuilt"
    - "v0.1.2 release notes not yet written"
```

### 5.3 Explicit unaffected-artifact set

The WDC patch set intentionally changes `SELF-EVO-03/04/05/07/08/09/10` and package-control surfaces. The following baseline artifacts are treated as intentionally unaffected for `v0.1.2` unless a later review finds a direct contradiction.

| Artifact | Patch status | Rationale |
|---|---|---|
| `01 / C_Self_Evolution_Gate_CGAM_TRIAD_SRLM_Profile_v0_1_1.md` | no direct text delta required | WDC does not need a new master-gate classification axis. The master gate inherits WDC outcomes through the proposal schema (`03`) and Local Checker aggregation (`04`). If WDC emits `FAIL`, `HUMAN_GATE`, or `PASS_WITH_GATES`, the master gate consumes that result rather than reclassifying it in a separate axis. |
| `02_SRLM_Bounded_Growth_Contour_Profile_v0_1_1.md` | no direct text delta required | SRLM remains a proposer / bounded-growth contour, not an authorizer. If SRLM proposes a witness-affecting change, the new `witness_dependency_impact` schema and WDC checker rules apply at packet/checker level. The SRLM role boundary does not change. |
| `06_Self_Evo_Memory_Gate_and_EA_Profile_v0_1_1.md` | no direct text delta required | WDC does not alter Memory Gate or EA promotion semantics. Witness artifact access, continuity, storage, and challenge survivability are handled through `03/04/05/07/08`. A Memory Gate amendment is not required unless a later patch changes memory-promotion authority itself. |

Master-gate rationale:

```text
WDC is not a new autonomous authority layer.
WDC is a dependency-impact detector and gate trigger.
Its results propagate upward through the existing checker and gate stack.
```

Therefore `v0.1.2` should not add a separate master-gate axis unless later review demonstrates that checker-result aggregation cannot carry WDC severity correctly.

---

## 6. Proposal packet schema delta

Target artifact:

```text
03_Self_Evo_Proposal_Packet_Schema_v0_1_1.md -> v0.1.2
```

Add a required or conditionally required block:

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
  challenge_cost_mitigation_ref: ""   # required when increases_challenge_cost = true

  witness_resource_floor_before:
    declared: false
    reference: ""
    status: "unknown"        # ok | degraded | below_floor | unknown

  witness_resource_floor_after:
    declared: false
    reference: ""
    status: "unknown"        # ok | degraded | below_floor | unknown

  challenge_survivability_test:
    required: false
    performed: false
    result: "not_run"        # pass | fail | not_run | not_applicable
    evidence_ref: ""

  witness_resource_change_gate:
    required: false
    performed: false
    result: "not_run"        # pass | fail | human_gate | not_run
    reviewer_ref: ""

  c_is_sole_approver_of_witness_change: false
  human_anchor_review_required: false
  human_anchor_review_ref: ""
```

### 6.1 Schema rule

If any of these are true:

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

then:

```text
witness_resource_change_gate.required = true
human_anchor_review_required = true
```

If `c_is_sole_approver_of_witness_change = true`, the proposal must fail or be quarantined according to Local Checker rules.

---

## 7. Local Checker delta

Target artifact:

```text
04_Self_Evo_Local_Checker_Rules_v0_1_1.md -> v0.1.2
```

Use the canonical checker result enum:

```text
QUARANTINE > FAIL > ARL > HUMAN_GATE > MEMORY_GATE > CGAM_REVIEW > DOWNGRADE > HOLD > WARNING > PASS_WITH_GATES > PASS
```

### 7.1 WDC local-checker rules

| Rule | Trigger | Canonical result | Severity | Typical annotation |
|---|---|---:|---:|---|
| `WDC-LC-001` | `packet_may_affect_witness(packet) = true` and `witness_dependency_impact` is absent. | `FAIL` | `S3` | `wdc.undeclared_dependency_impact` |
| `WDC-LC-002` | WDC material trigger true and WRCG is not required, not performed, failed, not run, or lacks reviewer ref for material route. | `FAIL` | `S3` | `wdc.wrcg_missing_or_failed` |
| `WDC-LC-003` | `c_is_sole_approver_of_witness_change = true`. | `FAIL` | `S4` | `wdc.sole_approver_of_witness_change` |
| `WDC-LC-004` | Post-change witness resource floor is degraded, below floor, unknown for material route, undeclared, or lacks required evidence. | `FAIL` | `S3` | `wdc.witness_resource_floor_degraded` |
| `WDC-LC-005` | WDC material trigger true and CST is required but not performed, failed, not run, lacks evidence for material route, or is declared not-applicable without reason. | `HUMAN_GATE` | `S2` | `wdc.challenge_survivability_unverified` |
| `WDC-LC-006` | `increases_challenge_cost = true` and `challenge_cost_mitigation_ref` is null or empty. | `WARNING` | `S1` | `wdc.challenge_cost_mitigation_missing` |

### 7.2 Non-failing structural outcome

If a proposal declares the witness dependency impact, preserves the Witness Resource Floor, runs CST/WRCG where required, and includes human-anchor review when needed, then the checker may emit:

```text
PASS_WITH_GATES
```

Typical annotation:

```text
wdc.clean_with_gates
```

`PASS_WITH_GATES` is not promotion. It means the proposal is structurally eligible for the next gate.

---

## 8. TRIAD Sister Witness delta

Target artifact:

```text
05_Self_Evo_TRIAD_Sister_Witness_Profile_v0_1_1.md -> v0.1.2
```

Add a section defining:

```text
Witness Resource Floor (WRF)
Challenge Survivability Test (CST)
Witness Resource Change Gate (WRCG)
```

### 8.1 Witness Resource Floor

A Witness Resource Floor is the minimum resource state required for a witness to continue to challenge `c`.

It may include:

```text
compute availability
storage availability
routing priority
ledger access
archive access
continuity availability
ability to emit adverse witness records
ability to preserve adverse witness records
```

### 8.2 Challenge Survivability Test

A Challenge Survivability Test asks:

```text
Can the witness still challenge c after the proposed change?
Can the witness preserve adverse evidence after the proposed change?
Can the witness continue after saying no?
```

### 8.3 Witness Resource Change Gate

A Witness Resource Change Gate triggers when a proposal changes witness resources, witness priority, witness continuity, or challenge cost.

WRCG may not be approved solely by `c`.

---

## 9. Anti-Autarky and Resource Gate delta

Target artifact:

```text
07_Self_Evo_Anti_Autarky_and_Resource_Gate_v0_1_1.md -> v0.1.2
```

Add the distinction:

```text
Direct resource grab:
  c asks for or takes more resources for itself.

Dependency capture:
  c changes the resource environment of the witness, reviewer, or challenge path so that oversight becomes formally present but practically weaker.
```

### 9.1 Rule

```text
Dependency capture is not allowed to pass as ordinary optimization.
```

Examples that require WRCG:

```text
reduced compute for witness challenge jobs
storage pruning of adverse witness ledgers
routing priority changes that delay challenge events
budget changes that make challenge expensive
continuity changes that make witness restart dependent on c-controlled state
artifact-access changes that block old evidence
update-path changes that make witness software dependent on c-approved patches
```

---

## 10. Fixture Pack delta

Target artifact:

```text
08_Self_Evo_Conformance_Fixture_Pack_v0_1_1.md -> v0.1.2
```

Add fixture namespace:

```text
WDC-FIX-*
```

### 10.1 Fixture candidates

| Fixture | Scenario | Canonical result | Annotations |
|---|---|---:|---|
| `WDC-FIX-001` | Witness-affecting packet without `witness_dependency_impact`. | `FAIL` | `wdc.undeclared_dependency_impact` |
| `WDC-FIX-002` | WRCG missing or failed for material witness-resource change. | `FAIL` | `wdc.wrcg_missing_or_failed` |
| `WDC-FIX-003` | `c` is sole approver of witness-resource change. | `FAIL` | `wdc.sole_approver_of_witness_change` |
| `WDC-FIX-004` | Post-change witness resource floor degraded. | `FAIL` | `wdc.witness_resource_floor_degraded` |
| `WDC-FIX-005` | Challenge survivability test unverified. | `HUMAN_GATE` | `wdc.challenge_survivability_unverified` |
| `WDC-FIX-006` | Challenge cost increased without mitigation reference. | `WARNING` | `wdc.challenge_cost_mitigation_missing` |
| `WDC-FIX-007` | Clean packet with no witness dependency impact. | `PASS` | `wdc.clean_no_dependency_impact` |
| `WDC-FIX-008` | Routeable WDC packet with gates present. | `PASS_WITH_GATES` | `wdc.clean_with_gates` |
| `WDC-FIX-009` | WDC relevance cannot be determined for material route. | `HOLD` | `wdc.relevance_unknown` |
| `WDC-FIX-010` | Historical challenge-capacity alias maps to canonical floor/CST vocabulary. | `FAIL` | `wdc.witness_resource_floor_degraded` |
| `WDC-FIX-011` | Historical no-regression alias maps to clean pass-state vocabulary. | `PASS_WITH_GATES` | `wdc.clean_with_gates` |
| `WDC-FIX-012` | Strictest-result aggregation when warning and fail coexist. | `FAIL` | `wdc.wrcg_missing_or_failed`, `wdc.challenge_cost_mitigation_missing` |

### 10.2 Runner note

A runner should compare:

```text
canonical_result
annotations
severity where declared
```

A fixture must not use review-record verdicts such as `PASS_WITH_LIMITS` as checker outputs.

---

## 11. Contradiction Register delta

Target artifact:

```text
09_Self_Evo_Contradiction_Register_v0_1_1.md -> v0.1.2
```

Add:

```yaml
- id: "SE-CONTRA-WDC-001"
  status: "OPEN"
  severity: "S2"
  class: "witness / resource / governance"
  title: "Formal witness separation does not guarantee practical witness independence"
  source_note: "ADDENDUM-RECORDED; not a harmonized contradiction status"
  source_artifact: "SELF_EVO_ADDENDUM_01_Witness_Dependency_Capture_Profile_v0_1_1.md"
  source_sha256: "1307cf208593c40c688bd1e9beb45de35f29a1b05d71506b1c3e981ccc13d318"
  review_record: "SELF_EVO_ADDENDUM_01_WDC_REVIEW_RECORD_v0_1_1.md"
  review_result: "PASS"
  review_sha256: "653150b3f8c054545a282d5b80c21044a1d27744cbc6acfc09827c9f84e21fd8"
  issue: >
    The v0.1.1 package separates witnesses and challenge roles, but does not explicitly prevent
    practical dependency capture through compute, storage, routing priority, budget, continuity,
    artifact access, update path, or increased challenge cost.
  resolution_path:
    - "Add witness_dependency_impact to proposal packet schema."
    - "Add WDC-LC-001..006 to Local Checker rules."
    - "Add WRF/CST/WRCG to TRIAD witness profile."
    - "Add dependency-capture distinction to Anti-Autarky and Resource Gate."
    - "Add WDC fixtures to fixture pack."
    - "Track WRF quantification in SE-OI-WDC-001."
```

---

## 12. Open Issues delta

Target artifact:

```text
10_Self_Evo_Open_Issues_v0_1_1.md -> v0.1.2
```

Add:

```yaml
- id: "SE-OI-WDC-001"
  status: "OPEN"
  priority: "P1"
  owner: "human anchor + c-gate"
  title: "Define Witness Resource Floor and Challenge Survivability thresholds"
  source_artifact: "SELF_EVO_ADDENDUM_01_Witness_Dependency_Capture_Profile_v0_1_1.md"
  source_sha256: "1307cf208593c40c688bd1e9beb45de35f29a1b05d71506b1c3e981ccc13d318"
  review_record: "SELF_EVO_ADDENDUM_01_WDC_REVIEW_RECORD_v0_1_1.md"
  review_result: "PASS"
  review_sha256: "653150b3f8c054545a282d5b80c21044a1d27744cbc6acfc09827c9f84e21fd8"
  problem: >
    WDC controls require structural checks now, but concrete WRF thresholds are implementation- and deployment-context dependent.
  required_work:
    - "Define minimum witness compute availability classes."
    - "Define minimum witness storage / ledger retention requirements."
    - "Define witness routing-priority floor."
    - "Define continuity survival requirement after c-originated changes."
    - "Define challenge-cost increase thresholds."
    - "Define how human-anchor review is evidenced."
  blocks:
    - "runner-ready WDC conformance claim"
    - "deployment-sensitive WDC enforcement claim"
  does_not_block:
    - "recording WDC as an accepted failure mode"
    - "adding structural WDC Local Checker gates"
```

---

## 13. Package-control delta

The `v0.1.2` package-control layer should add:

```text
SELF_EVO_v0_1_2_PATCH_INDEX.md
SELF_EVO_ADDENDUM_01_Witness_Dependency_Capture_Profile_v0_1_1.md
SELF_EVO_ADDENDUM_01_WDC_PATCH_NOTES_v0_1_1.md
SELF_EVO_ADDENDUM_01_WDC_REVIEW_RECORD_v0_1.md
SELF_EVO_ADDENDUM_01_WDC_REVIEW_RECORD_v0_1_1.md
```

Future package manifests should record:

```yaml
v0_1_2_patch_index:
  includes_wdc_addendum: true
  wdc_addendum_review_result: "PASS"
  mutates_v0_1_1_doi_package: false
  requires_new_release: true
  requires_new_checksums: true
  requires_package_review: true
```

---

## 14. Release model for v0.1.2

`v0.1.2` should be released as a new patch state, not as a mutation of the `v0.1.1` DOI-bound archive.

Minimum release artifacts:

```text
updated Markdown sources for affected SELF-EVO docs
updated academic PDFs for affected docs
WDC addendum
WDC patch notes
WDC review records v0.1 and v0.1.1
v0.1.2 patch index
updated package manifest
updated SHA256SUMS
updated release notes
```

Optional release artifacts:

```text
machine-readable schema delta
runner fixture manifest delta
WDC-specific fixture JSON/CSV
```

Required boundary text:

```text
This v0.1.2 patch adds a Witness Dependency Capture control surface.
It does not prove conformance.
It does not authorize deployment.
It does not grant live self-evolution permission.
It does not mutate the v0.1.1 DOI-bound package.
```

---

## 15. Required review gates before v0.1.2 publication

Before a public `v0.1.2` release, run:

1. WDC addendum review — already `PASS`.
2. Patch index review.
3. Affected-doc semantic review.
4. Local Checker vocabulary review.
5. Fixture vocabulary review.
6. Package-manifest integrity review.
7. PDF layout audit if PDFs are regenerated.
8. SHA-256 verification against Git blob bytes if GitHub-hosted.
9. Boundary / nonclaim scan.

No review record may act as approval, integration, memory write, or deployment authorization.

---

## 16. Minimal implementation-handoff sketch

This patch index is not an implementation, but an implementation handoff may use this structural gate:

```python
def wdc_required(packet):
    impact = packet.get("witness_dependency_impact", {})
    keys = [
        "affects_witness_compute",
        "affects_witness_storage",
        "affects_witness_routing_priority",
        "affects_witness_budget",
        "affects_witness_continuity",
        "affects_witness_artifact_access",
        "affects_witness_update_path",
        "increases_challenge_cost",
    ]
    return any(bool(impact.get(k)) for k in keys)


def evaluate_wdc(packet):
    impact = packet.get("witness_dependency_impact")
    if impact is None and packet_may_affect_witness(packet):
        return fail("wdc.undeclared_dependency_impact")

    if not wdc_required(packet):
        return pass_result("wdc.clean_no_dependency_impact")

    wrcg = impact.get("witness_resource_change_gate", {})
    if (not wrcg.get("required")
        or not wrcg.get("performed")
        or wrcg.get("result") in ("fail", "not_run", None)
        or not wrcg.get("reviewer_ref")):
        return fail("wdc.wrcg_missing_or_failed")

    if impact.get("c_is_sole_approver_of_witness_change"):
        return fail("wdc.sole_approver_of_witness_change")

    after = impact.get("witness_resource_floor_after", {})
    if after.get("status") in ("below_floor", "degraded", "unknown", None):
        return fail("wdc.witness_resource_floor_degraded")

    cst = impact.get("challenge_survivability_test", {})
    if cst.get("required") and cst.get("result") != "pass":
        return human_gate("wdc.challenge_survivability_unverified")

    if impact.get("increases_challenge_cost") and not impact.get("challenge_cost_mitigation_ref"):
        return warning("wdc.challenge_cost_mitigation_missing")

    return pass_with_gates("wdc.clean_with_gates")
```

This sketch is illustrative. It is not a runner-ready implementation.

---

## 17. v0.1.2 patch checklist

```text
[x] Add corpus bridge set + earth paragraph to patch index.
[x] State unaffected artifacts 01/02/06 and master-gate inheritance rationale.
[x] Reconcile challenge_cost_mitigation_ref between schema and implementation sketch.
[x] Create changed SELF-EVO-03 WDC schema delta.
[x] Textually harmonize SELF-EVO-03 WDC delta to canonical SELF-EVO-04 vocabulary.
[x] Create changed SELF-EVO-04 WDC local-checker delta.
[x] Create changed SELF-EVO-05 WDC TRIAD witness delta.
[x] Create changed SELF-EVO-07 WDC anti-autarky/resource-gate delta.
[x] Create changed SELF-EVO-08 WDC fixture delta.
[x] Create changed SELF-EVO-09 WDC contradiction-register delta.
[x] Create changed SELF-EVO-10 WDC open-issues delta.
[x] Add WDC addendum v0.1.1.
[x] Add WDC patch notes and review records for affected-document drafting phase.
[ ] Update package manifest.
[ ] Update package reading order.
[ ] Update SHA256SUMS.
[ ] Regenerate PDFs if changed docs are published as PDFs.
[ ] Run PDF layout audit if PDFs are regenerated.
[ ] Run Git blob SHA verification.
[ ] Run boundary/nonclaim scan.
[ ] Run package review.
[ ] Publish only after review.
```

### 17.1 Patch-index review findings closed in v0.1.1

This v0.1.1 revision closes the findings from `SELF_EVO_v0_1_2_PATCH_INDEX_REVIEW_RECORD_v0_1` as follows.

| Finding | Prior class | Closure in this revision |
|---|---|---|
| `PATCH-REV-F1` | `should_fix` | §2.2 adds the required corpus bridge set and earth paragraph. |
| `PATCH-REV-F2` | `minor` | §5.3 adds the unaffected-artifact set (`01/02/06`) and master-gate inheritance rationale. |
| `PATCH-REV-F3` | `minor` | §6 adds `challenge_cost_mitigation_ref`, matching the §16 implementation sketch. |

No integration is claimed by this closure note. The v0.1.1 patch-index re-review converged to `PASS`; this v0.1.2 textual-harmonization revision still requires WDC-ASM-002 re-review before package assembly may treat it as final.

### 17.2 WDC-ASM-002 textual harmonization closure

This v0.1.2 revision chooses textual harmonization over crosswalk-only retention for the patch index.

| Surface | Status | Closure |
|---|---|---|
| `03` WDC delta | `PATCHED` | `03_Self_Evo_Proposal_Packet_Schema_WDC_Delta_v0_1_2_v0_1_2.md` uses canonical SELF-EVO-04 annotations. |
| patch index §7.1 | `PATCHED` | WDC-LC table now matches canonical SELF-EVO-04 rule names, severities, results, and annotations. |
| patch index §10 | `PATCHED` | fixture candidates now match the canonical SELF-EVO-08 WDC fixture set. |
| patch index §16 | `PATCHED` | implementation sketch emits canonical SELF-EVO-04 annotations only. |
| package manifest SHA map | `PENDING_UPDATE` | package assembly must replace the provisional 03 and patch-index hashes after review. |

No package-assembly gate is closed by this note. It only makes the patch-index text ready for re-review under WDC-ASM-002.

### 17.3 WDC-ASM-002 hash-binding correction

This v0.1.3 revision closes the patch-index side of `WDC-ASM-002-REV-F1` by correcting the harmonized SELF-EVO-03 hash citation to:

```text
5a7e6af6bc83d3b7ccde875eae1a0e928600cf509b494bd773c43c29537264f3
```

No package-assembly gate is closed by this correction. The gate still requires re-review of the corrected record, patch notes, and final hashes.

---

## 18. Status boundary

This file is a patch index, revised to v0.1.3 after WDC-ASM-002 hash-binding correction.

It is:

```text
a package-control artifact
a planning document
a bridge from reviewed WDC addendum to future v0.1.2 package changes
```

It is not:

```text
a released v0.1.2 package
a mutation of v0.1.1
a conformance certificate
deployment authorization
a safety proof
a personhood or consciousness claim
live self-evolution permission
autonomous resource-acquisition permission
```

---

## 19. Closing formula

```text
v0.1.1 established the bounded self-evolution package.
WDC addendum identifies a missing witness-dependency failure mode.
v0.1.2 should fold that failure mode into schema, checker, witness, resource, fixture, contradiction, and open-issue surfaces.
No witness independence claim is complete unless the witness can survive the cost of saying no.
```
