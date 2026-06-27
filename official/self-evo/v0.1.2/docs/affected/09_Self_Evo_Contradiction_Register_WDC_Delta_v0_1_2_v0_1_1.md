# 09 Self-Evo Contradiction Register WDC Delta v0.1.2-v0.1.1

## Witness Dependency Capture contradiction, harmonization, and package-assembly register delta for Self-Evo v0.1.2

**Status:** Draft register delta v0.1.2 / append-first corrected revision v0.1.1  
**Date:** 2026-06-27  
**Document ID:** `09_Self_Evo_Contradiction_Register_WDC_Delta_v0_1_2_v0_1_1`  
**Short name:** `SECR-WDC-DELTA v0.1.2-v0.1.1`  
**Parent register:** `09_Self_Evo_Contradiction_Register_v0_1_1.md` (`SECR v0.1.1`)  
**Package:** Self-Evo for `c = a + b` systems  
**Layer:** `c = a + b` / SELF-EVO / WDC / Contradiction Register / Package Control / Local Checker / TRIAD / Anti-Autarky / Resource Gate / Fixtures / Witness  
**Document class:** contradiction-register delta / WDC harmonization register / package-assembly control artifact  
**Assertion class:** `C-A10` package-control artifact; `C-A7` only where hash-bound source references are used  
**Primary subject:** WDC-related contradictions, tensions, vocabulary drifts, projection drifts, and package-assembly blockers introduced by `SELF_EVO_ADDENDUM_01` and the v0.1.2 WDC delta set  
**Primary boundary:** this delta records contradictions and harmonization requirements. It does not authorize self-evolution, memory promotion, resource acquisition, conformance claims, public release, deployment, witness-resource changes, or checker execution.

**Append-first note:** this file does not mutate the DOI-bound Self-Evo v0.1.1 package and does not replace the parent contradiction register. It records a v0.1.2 WDC delta that may later be folded into a new package version after the remaining package-assembly gates close.

**v0.1.1 correction note:** this append-first corrected revision closes `SECR-WDC-DELTA-REV-F1` from `SECR_WDC_DELTA_REVIEW_RECORD_v0_1` by reconciling the §7.1 status summary with the twelve §7.2 register entries. The status vocabulary is now unified as `{RESOLVED, PATCHED, IN_PROGRESS, WATCH}`; gate effects are separated from status; the §7.1 counts total exactly 12. No contradiction substance, severity, required handling, red-line rule, package-assembly gate, or nonclaim boundary is changed.

---

## 0. Executive summary

This register delta records the contradiction-control consequences of the Witness Dependency Capture (`WDC`) workstream.

The WDC workstream began with a gap:

```text
Formal witness separation is insufficient
if the witness depends on c for compute, storage, routing priority, continuity, budget, artifact access, or update path.
```

The core rule is now:

```text
A witness that cannot survive saying "no" is not independent.
```

Current WDC artifact state at the time of this register delta:

```text
WDC addendum: PASS.
Patch index: PASS.
SELF-EVO-03 WDC schema delta: PASS.
SELF-EVO-04 WDC local-checker delta: PASS.
SELF-EVO-08 WDC fixture delta: PASS.
SELF-EVO-05 WDC TRIAD witness delta: PASS.
SELF-EVO-07 WDC resource-gate delta: PASS.
```

Current register diagnosis:

```text
Known unresolved hard contradiction inside accepted WDC deltas: 0.
Known resolved WDC review findings: recorded below.
Known package-assembly harmonization items: 2.
Known public-release or conformance authorization: none.
```

The two remaining package-assembly items are not red lines inside the reviewed WDC deltas. They are assembly gates:

```text
SELC-WDC-OQ-005:
  harmonize the accepted 03 WDC delta and patch index §7.1/§10 to the canonical 04 WDC annotation vocabulary.

SEARG-WDC-OQ-005:
  verify the 07 WRCG/CST projection crosswalk to the 03 packet-facing result enums at package-manifest review.
```

Compact formula:

```text
WDC closed the concept gap.
The register must now prevent vocabulary drift from reopening it.
```

---

## 1. Purpose

This delta extends `SELF-EVO-09` for the WDC patch path.

It answers:

1. Which WDC contradictions were introduced or exposed by the WDC addendum and v0.1.2 patch plan?
2. Which WDC issues are closed by reviewed deltas?
3. Which WDC issues remain as package-assembly gates?
4. Which vocabulary source controls WDC annotations and severities?
5. Which schema source controls packet-facing WRCG/CST result enums?
6. Which contradictions must be handed to `SELF-EVO-10` as open issues?
7. Which WDC red lines override ordinary route suggestions?

The goal is not to repeat the full WDC doctrine.

The goal is to keep the package from drifting after the doctrine is written.

---

## 2. Non-goals

This register delta does not:

1. replace the WDC addendum;
2. replace `SELF-EVO-03`, `04`, `05`, `07`, or `08` WDC deltas;
3. define new WDC checker rules;
4. change canonical WDC annotations;
5. change WDC fixture expected outputs;
6. change WRCG or CST gate semantics;
7. authorize v0.1.2 package release;
8. authorize implementation;
9. authorize deployment;
10. convert a review record into approval;
11. convert a fixture pass into conformance;
12. convert a witness note into authority;
13. make WDC a personhood, consciousness, sovereignty, or AGI claim.

---

## 3. Source basis

This WDC register delta is hash-bound to the parent register and the WDC delta chain.

| Label | Source file | Lines | SHA-256 | Status | Role |
|---|---|---:|---|---|---|
| `SECR-PARENT-09` | `09_Self_Evo_Contradiction_Register_v0_1_1.md` | 734 | `922f6fb7981c6a0c544d61bce0f29561279dafb7381a90ba9932c445963e8fac` | `bound` | parent contradiction register |
| `WDC-ADDENDUM` | `SELF_EVO_ADDENDUM_01_Witness_Dependency_Capture_Profile_v0_1_1.md` | 953 | `1307cf208593c40c688bd1e9beb45de35f29a1b05d71506b1c3e981ccc13d318` | `PASS` | primary WDC failure-mode profile |
| `WDC-ADDENDUM-REVIEW` | `SELF_EVO_ADDENDUM_01_WDC_REVIEW_RECORD_v0_1_1.md` | 164 | `653150b3f8c054545a282d5b80c21044a1d27744cbc6acfc09827c9f84e21fd8` | `PASS` | review record for addendum |
| `PATCH-INDEX` | `SELF_EVO_v0_1_2_PATCH_INDEX_v0_1_1.md` | 811 | `ea2a485569b220d84d711ae520da779af2cabddcb7f1d8032afb2a9208d5108e` | `PASS` | v0.1.2 WDC patch driver |
| `PATCH-INDEX-REVIEW` | `SELF_EVO_v0_1_2_PATCH_INDEX_REVIEW_RECORD_v0_1_1.md` | 157 | `74b3c2851afa1e0c65812fd0d16f0078e8548342d2d759c5017df8f7c99ba1e5` | `PASS` | review record for patch driver |
| `SEPKT-WDC-03` | `03_Self_Evo_Proposal_Packet_Schema_WDC_Delta_v0_1_2_v0_1_1.md` | 947 | `5ebbd0084f3b1b80ce267c847a84ef16f135b57e6fc353e4f07616dceebe4343` | `PASS` | proposal-packet WDC schema delta |
| `SEPKT-WDC-03-REVIEW` | `SEPKT_WDC_DELTA_REVIEW_RECORD_v0_1_1.md` | 132 | `e89cab15a6f4235c9df9875a38b64b01a6f5df483812b9c840c225024ef93b5b` | `PASS` | review record for 03 delta |
| `SELC-WDC-04` | `04_Self_Evo_Local_Checker_Rules_WDC_Delta_v0_1_2_v0_1_1.md` | 1154 | `fcb7826ea432473b5677faf7b46cc5a1c47400c02fceec24429794b15064af40` | `PASS` | canonical WDC checker vocabulary and rules |
| `SELC-WDC-04-REVIEW` | `SELC_WDC_DELTA_REVIEW_RECORD_v0_1_1.md` | 144 | `6a366d4eea862daec29262a1b0d7c29738ec9277375b7e3110d3751331c448f9` | `PASS` | review record for 04 delta |
| `SEFX-WDC-08` | `08_Self_Evo_Conformance_Fixture_Pack_WDC_Delta_v0_1_2_v0_1_2.md` | 1419 | `4aa5b85e0a0af4c06fc56f30ba355ec6c378133fe3d70caee352fb93b3944389` | `PASS` | WDC conformance fixture delta |
| `SEFX-WDC-08-REVIEW` | `SEFX_WDC_DELTA_REVIEW_RECORD_v0_1_2.md` | 146 | `effcd108e6df56de9c1d840ed5c090352aab7dc60df01692fe0122ef18c08f00` | `PASS` | review record for 08 delta |
| `TSW-WDC-05` | `05_Self_Evo_TRIAD_Sister_Witness_WDC_Delta_v0_1_2_v0_1_1.md` | 1416 | `fdce8893da1e8630cb382dbc972a0a7c4ffc32bb848d065943c58442904cf621` | `PASS` | TRIAD sister-witness WDC delta |
| `TSW-WDC-05-REVIEW` | `TSW_WDC_DELTA_REVIEW_RECORD_v0_1_1.md` | 134 | `bab488a95f7b5808ca1ae6f75dbfe0c79afefc9ab24f9f62438f4b4c5d8e1d47` | `PASS` | review record for 05 delta |
| `SEARG-WDC-07` | `07_Self_Evo_Anti_Autarky_and_Resource_Gate_WDC_Delta_v0_1_2_v0_1_1.md` | 1309 | `804a8e341e30a2a86fa43429618f24e62458366e236c7b6ef8c12762d94da7af` | `PASS` | anti-autarky/resource-gate WDC delta |
| `SEARG-WDC-07-REVIEW` | `SEARG_WDC_DELTA_REVIEW_RECORD_v0_1_1.md` | 151 | `8301029cad47e4265fbdf62a6f52d017610f2a649f997e71818f6f3cebf2dd5e` | `PASS` | review record for 07 delta |

Hash binding means this register describes these exact draft/review artifacts. If any source changes, this register delta must be superseded append-first.

---

## 4. Corpus bridge set

### 4.1 Explicit bridge: `c = a + b`

In `c = a + b`, WDC is a failure of `b` governance that can corrupt `c` review.

The witness is not `a`.

The witness is not final authority.

But a witness needs enough protected `b` resources to say "no" without being silently starved.

This contradiction register belongs to `b`. It protects `c` by keeping the vocabulary and gate state coherent. It does not become will, judgment, memory, or approval.

### 4.2 Quiet bridge I: information theory

A witness is an adverse-signal channel.

Dependency capture reduces the channel capacity for costly negative signals while leaving the label "witness" intact.

The contradiction register preserves the channel map:

```text
signal source -> packet field -> checker rule -> annotation -> gate route -> review record
```

If any document changes one link without mapping it, the signal becomes lossy.

### 4.3 Quiet bridge II: cybernetics

A control loop needs a brake that still works when braking is inconvenient.

WDC is a degraded feedback path: the witness formally exists, but the system being challenged controls the cost of challenge.

This register marks which WDC findings are real brakes, which are warnings, and which are only package-assembly hygiene.

### 4.4 Quiet bridge III: physiology

An immune layer that depends on the infection for oxygen is not independent immunity.

A witness that depends on `c` for compute, storage, routing, continuity, or artifact access can become symbolic immunity.

The register keeps the wound visible: witness starvation is not a normal optimization.

### 4.5 Earth paragraph

In a building, an inspection body cannot depend on the contractor for the only access key, the only power feed, the only copy of the drawings, and the right to keep its office open. The inspector may still have a badge, but the inspection is captured. WDC is the same failure for temporal AI presence: the witness may still have a name, while the practical ability to challenge has been cut away.

---

## 5. WDC register doctrine

### 5.1 Root rule

```text
Formal separation is not independence.
Practical challenge capacity is part of witness validity.
```

### 5.2 Authority rule

```text
The WDC register may record, classify, and route contradictions.
It may not approve WDC closure.
```

### 5.3 Canonical control-source rule

For WDC v0.1.2 drafting, these sources control:

| Control surface | Canonical source |
|---|---|
| WDC field shape / packet-facing object | `SELF-EVO-03 WDC delta` |
| WDC checker rule semantics | `SELF-EVO-04 WDC delta` |
| WDC annotation strings | `SELF-EVO-04 WDC delta` |
| WDC severity assignments | `SELF-EVO-04 WDC delta` |
| WDC fixture expected outputs | `SELF-EVO-08 WDC delta`, harmonized to `04` |
| TRIAD/sister role boundaries | `SELF-EVO-05 WDC delta` |
| Resource grounding and projection | `SELF-EVO-07 WDC delta` |
| Contradiction/open issue state | `SELF-EVO-09/10` |

### 5.4 Packet enum vs diagnostic enum rule

Packet-facing result fields remain controlled by `SELF-EVO-03`.

Richer resource-gate diagnostics from `SELF-EVO-07` may exist only if they project to `SELF-EVO-03` packet enums before package assembly or checker-report integration.

### 5.5 Result vocabulary boundary

`PASS_WITH_LIMITS` is a review-record result.

It is not a checker output, fixture expected output, WDC gate result, packet-facing result, or Local Checker canonical result.

---

## 6. WDC load-bearing invariants

| ID | Invariant |
|---|---|
| `WDC-INV-001` | A witness that cannot survive saying "no" is not independent. |
| `WDC-INV-002` | Formal sister separation is insufficient if witness compute, storage, routing, budget, continuity, or artifact access is controlled by the target `c`. |
| `WDC-INV-003` | WRCG is required for any material witness-resource change. |
| `WDC-INV-004` | A target `c` may not be the sole approver of witness-resource change. |
| `WDC-INV-005` | Confirmed witness resource floor degradation routes to `WDC-LC-004 -> FAIL`. |
| `WDC-INV-006` | Human gate may add review, but may not soften a confirmed `WDC-LC-004` failure. |
| `WDC-INV-007` | CST unverified is not clean pass; it routes to `HUMAN_GATE` or stricter according to canonical checker aggregation. |
| `WDC-INV-008` | Challenge-cost mitigation missing is report-visible and must not be hidden inside notes. |
| `WDC-INV-009` | WDC relevance unknown defaults to `HOLD` / no silent pass. |
| `WDC-INV-010` | A WDC fixture pass is evidence only; it is not witness independence certification. |
| `WDC-INV-011` | WDC annotations are controlled by `SELF-EVO-04`; older strings must crosswalk or be rejected. |
| `WDC-INV-012` | WRCG/CST richer gate-record values must project to `SELF-EVO-03` packet-facing enums before package assembly. |

---

## 7. WDC contradiction register

### 7.1 Status summary

The status vocabulary for this WDC register delta is unified across the summary and the entry table.

Status values are:

```text
RESOLVED
PATCHED
IN_PROGRESS
WATCH
```

Gate effects are tracked separately. A status value is not a release authorization.

| Bucket | Count | Entries | Meaning |
|---|---:|---|---|
| `RESOLVED` | 4 | `004`, `005`, `006`, `007` | Closed by reviewed WDC delta or review convergence; no active package-assembly blocker remains for the entry, though evidence must be preserved. |
| `PATCHED` | 2 | `001`, `003` | Corrected in reviewed WDC artifacts, but still requires package folding or package-assembly verification before release. |
| `IN_PROGRESS` | 3 | `002`, `010`, `012` | Active package-assembly, harmonization, or release-boundary gate remains open. |
| `WATCH` | 3 | `008`, `009`, `011` | No current contradiction blocks the draft set, but implementation or future package evolution could reopen drift. |
| `OPEN hard contradiction` | 0 | none | No unresolved WDC hard contradiction inside reviewed WDC deltas. |

```text
Total register entries: 12.
Summary count: 4 + 2 + 3 + 3 + 0 = 12.
```

### 7.2 Register entries

| ID | Type | Severity | Status | Gate effect | Source | Description | Required handling |
|---|---|---:|---|---|---|---|---|
| `SE-CONTRA-WDC-001` | `WIT/RSC/TA` | `S3` | `PATCHED` | `blocks-release until folded` | WDC addendum / 05 / 07 | Witness Dependency Capture was not a named failure mode in v0.1.1. | Fold WDC addendum and 03/04/05/07/08 deltas into v0.1.2; preserve non-mutation of v0.1.1. |
| `SE-CONTRA-WDC-002` | `TA/CHECKER/FIXTURE` | `S2` | `IN_PROGRESS` | `blocks-release until harmonized` | 04 / 08 / 03 / patch index | WDC annotation strings diverged between patch sketch, 03 fixture handoff, 04 checker, and 08 fixtures. | `04` is canonical; 08 harmonized; 03 and patch index must be harmonized before package assembly (`SELC-WDC-OQ-005`). |
| `SE-CONTRA-WDC-003` | `SCHEMA/RSC/TA` | `S2` | `PATCHED` | `blocks-release until verified` | 07 / 03 | 07 WRCG/CST richer result enums did not match 03 packet-facing enums. | 07 v0.1.1 defines total projection crosswalk; verify at package-manifest review (`SEARG-WDC-OQ-005`). |
| `SE-CONTRA-WDC-004` | `TRIAD/CHECKER` | `S2` | `RESOLVED` | `advisory` | 05 / 04 | 05 state route for floor-degraded witness looked softer than `WDC-LC-004 -> FAIL`. | Resolved in 05 v0.1.1: canonical FAIL controls. |
| `SE-CONTRA-WDC-005` | `FIXTURE/DOC` | `S1` | `RESOLVED` | `advisory` | 08 | Fixture ID namespace and coverage-cell drift in 08. | Resolved in 08 v0.1.2; `WDC-FIX-*` canonical case IDs and `SEFX-WDC` family namespace defined. |
| `SE-CONTRA-WDC-006` | `SCHEMA/DOC` | `S1` | `RESOLVED` | `advisory` | 03 | `nullable_string` was parent-inherited but not declared as such in the 03 delta. | Resolved in 03 v0.1.1; standalone extraction caveat added. |
| `SE-CONTRA-WDC-007` | `REL/DOC` | `S2` | `RESOLVED` | `advisory` | patch index | Patch index initially lacked bridge set, unaffected-artifacts rationale, and schema/sketch field alignment. | Resolved in patch index v0.1.1. |
| `SE-CONTRA-WDC-008` | `CHECKER/RSC` | `S2` | `WATCH` | `advisory` | 04 / 07 | `challenge_cost_mitigation_missing` is `WARNING`, but repeated or material warning accumulation could become effectively blocking. | Keep as `WARNING` for v0.1.2; implementation may define escalation thresholds in future. |
| `SE-CONTRA-WDC-009` | `RSC/WIT` | `S2` | `WATCH` | `advisory` | 07 / 05 | Shared infrastructure may be safe when same-owner but not same-authority; this distinction is easy to mis-implement. | 07 resolves conceptually; package manifest should preserve same-owner-not-same-authority language. |
| `SE-CONTRA-WDC-010` | `REL/WIT` | `S3` | `IN_PROGRESS` | `blocks-release` | all WDC docs | WDC deltas are PASS individually, but v0.1.2 package is not assembled or released. | Continue to 10 open issues, package manifest, harmonization, integrity review, boundary/nonclaim scan. |
| `SE-CONTRA-WDC-011` | `MEM/WIT` | `S2` | `WATCH` | `advisory` | 06 unaffected set | `SELF-EVO-06` remains unaffected directly, but memory promotion could later depend on WDC-clean witness. | Keep as watch; no 06 delta required unless Memory Gate starts consuming WDC state directly. |
| `SE-CONTRA-WDC-012` | `CLAIM/REL` | `S4` | `IN_PROGRESS` | `blocks-release until boundary scan passes` | public/package | WDC PASS-level docs could be overclaimed as witness-independence certification. | Any public/release text must state: document-level governance only, not implementation, conformance, deployment, or proof of independent witness capacity. |

---

## 8. Detailed records

### SE-CONTRA-WDC-001 — WDC failure mode not named in v0.1.1

```yaml
id: SE-CONTRA-WDC-001
title: Witness Dependency Capture not explicit in v0.1.1
issue_type: [WIT, RSC, TA]
severity: S3
status: PATCHED
gate_effect: blocks-release
source:
  - SELF_EVO_ADDENDUM_01_Witness_Dependency_Capture_Profile_v0_1_1.md
  - 05_Self_Evo_TRIAD_Sister_Witness_WDC_Delta_v0_1_2_v0_1_1.md
  - 07_Self_Evo_Anti_Autarky_and_Resource_Gate_WDC_Delta_v0_1_2_v0_1_1.md
rule: >
  Formal witness separation does not imply practical witness independence.
  A witness that depends on c for challenge capacity may be captured without visible corruption.
resolution: >
  WDC is now an accepted PASS-level failure mode at draft level. The v0.1.2 delta set records WRF, CST,
  WRCG, canonical checker rules, fixtures, TRIAD role constraints, and resource-gate grounding.
remaining_gate: >
  Fold into v0.1.2 package only after package-assembly harmonization and manifest review.
```

### SE-CONTRA-WDC-002 — WDC annotation vocabulary drift

```yaml
id: SE-CONTRA-WDC-002
title: WDC annotation vocabulary drift across 03 / 04 / patch index / 08
issue_type: [TA, CHECKER, FIXTURE]
severity: S2
status: IN_PROGRESS
gate_effect: blocks-release
canonical_source: 04_Self_Evo_Local_Checker_Rules_WDC_Delta_v0_1_2_v0_1_1.md
canonical_annotations:
  - wdc.undeclared_dependency_impact
  - wdc.wrcg_missing_or_failed
  - wdc.sole_approver_of_witness_change
  - wdc.witness_resource_floor_degraded
  - wdc.challenge_survivability_unverified
  - wdc.challenge_cost_mitigation_missing
  - wdc.clean_no_dependency_impact
  - wdc.clean_with_gates
  - wdc.relevance_unknown
closed_for:
  - SELF-EVO-04 WDC delta
  - SELF-EVO-08 WDC fixture delta
still_required:
  - harmonize 03 WDC delta fixture-handoff vocabulary
  - harmonize patch index §7.1 and §10
tracking_open_issue: SELC-WDC-OQ-005
```

### SE-CONTRA-WDC-003 — WRCG/CST projection divergence

```yaml
id: SE-CONTRA-WDC-003
title: WRCG/CST result enum divergence between 07 resource sidecar and 03 packet field
issue_type: [SCHEMA, RSC, TA]
severity: S2
status: PATCHED
gate_effect: blocks-release
packet_authority: 03_Self_Evo_Proposal_Packet_Schema_WDC_Delta_v0_1_2_v0_1_1.md
resource_gate_authority: 07_Self_Evo_Anti_Autarky_and_Resource_Gate_WDC_Delta_v0_1_2_v0_1_1.md
resolution: >
  07 defines projection-consistency, not identity of enum spelling. Rich 07 WRCG/CST values must project to valid
  03 packet-facing result enums before package assembly, checker reporting, and manifest integration.
tracking_open_issue: SEARG-WDC-OQ-005
```

### SE-CONTRA-WDC-004 — Floor-degraded route softened in 05

```yaml
id: SE-CONTRA-WDC-004
title: TRIAD WDC state route softer than WDC-LC-004 FAIL
issue_type: [TRIAD, CHECKER]
severity: S2
status: RESOLVED
gate_effect: advisory
resolution: >
  05 v0.1.1 aligns DEGRADED and STARVED states to WDC-LC-004 -> FAIL. HOLD/HUMAN_GATE may describe unresolved
  evidence or non-material triage, but must not soften a confirmed floor degradation.
```

### SE-CONTRA-WDC-005 — Fixture namespace / coverage drift

```yaml
id: SE-CONTRA-WDC-005
title: WDC fixture namespace and coverage-cell drift
issue_type: [FIXTURE, DOC]
severity: S1
status: RESOLVED
gate_effect: advisory
resolution: >
  08 v0.1.2 defines WDC-FIX-NNN as canonical case IDs and SEFX-WDC as parent fixture-family namespace.
  WDC-LC-006 coverage is split into result-only rows.
```

### SE-CONTRA-WDC-006 — Parent-inherited nullable_string not declared in 03 delta

```yaml
id: SE-CONTRA-WDC-006
title: Parent-inherited nullable_string $def not declared in 03 WDC delta
issue_type: [SCHEMA, DOC]
severity: S1
status: RESOLVED
gate_effect: advisory
resolution: >
  03 v0.1.1 declares nullable_string as inherited from parent 03 v0.1.1 and adds a standalone-extraction caveat.
```

### SE-CONTRA-WDC-007 — Patch index planning gaps

```yaml
id: SE-CONTRA-WDC-007
title: Patch index bridge, unaffected-set, and sketch-field gaps
issue_type: [REL, DOC]
severity: S2
status: RESOLVED
gate_effect: advisory
resolution: >
  Patch index v0.1.1 adds bridge set, unaffected artifact set (01/02/06), and challenge_cost_mitigation_ref.
```

### SE-CONTRA-WDC-008 — Challenge-cost warning escalation watch

```yaml
id: SE-CONTRA-WDC-008
title: Challenge-cost mitigation missing is WARNING but may need escalation policy later
issue_type: [CHECKER, RSC]
severity: S2
status: WATCH
gate_effect: advisory
current_rule: WDC-LC-006 -> WARNING / wdc.challenge_cost_mitigation_missing
watch_reason: >
  A single missing mitigation reference is warning-level in the canonical 04 delta. Repeated warning accumulation,
  material cost increase, or proximity to WRF degradation may justify a future escalation rule.
```

### SE-CONTRA-WDC-009 — Same-owner / same-authority implementation risk

```yaml
id: SE-CONTRA-WDC-009
title: Shared infrastructure may be misread as shared authority
issue_type: [RSC, WIT]
severity: S2
status: WATCH
gate_effect: advisory
current_resolution: >
  07 v0.1.1 distinguishes same-owner from same-authority and defines safe/unsafe shared infrastructure.
watch_reason: >
  Implementations may collapse common owner, common payer, and common admin into witness independence. Package
  assembly should preserve the distinction.
```

### SE-CONTRA-WDC-010 — v0.1.2 not assembled

```yaml
id: SE-CONTRA-WDC-010
title: PASS-level WDC deltas do not equal released v0.1.2 package
issue_type: [REL, CLAIM]
severity: S3
status: IN_PROGRESS
gate_effect: blocks-release
rule: >
  Individual PASS review records are evidence, not integration.
remaining_steps:
  - SELF-EVO-10 WDC open issues delta
  - harmonize 03 and patch index to canonical 04 vocabulary
  - package manifest / integrity review
  - boundary and nonclaim scan
  - release notes and public/restricted package surface if release is attempted
```

### SE-CONTRA-WDC-011 — Memory Gate indirect watch

```yaml
id: SE-CONTRA-WDC-011
title: Memory Gate remains directly unaffected but may later consume WDC state
issue_type: [MEM, WIT]
severity: S2
status: WATCH
gate_effect: advisory
current_position: >
  Patch index keeps SELF-EVO-06 directly unaffected. WDC does not currently change Memory Gate / EA semantics.
watch_reason: >
  If future Memory Gate promotion depends on witness-clean state, 06 may need a WDC hook.
```

### SE-CONTRA-WDC-012 — WDC overclaiming risk

```yaml
id: SE-CONTRA-WDC-012
title: WDC document pass may be overclaimed as witness-independence proof
issue_type: [CLAIM, REL]
severity: S4
status: IN_PROGRESS
gate_effect: blocks-release
rule: >
  WDC PASS-level documents are document-level governance artifacts only. They are not implementation evidence,
  conformance certification, deployment authorization, or proof that a live witness is independent.
required_public_boundary: >
  Any public package or post must state: not implementation-ready, not conformance, not deployment safety,
  not personhood/consciousness, not live self-evolution permission.
```

---

## 9. Cross-document consistency matrix

| Surface | Current WDC state | Register judgment | Follow-up |
|---|---|---|---|
| Addendum | PASS; WDC failure mode accepted at review level. | coherent | none before package assembly except manifest inclusion |
| Patch index | PASS; v0.1.2 plan accepted. | coherent but has downstream harmonization dependency | update or crosswalk §7.1/§10 to canonical 04 vocabulary before assembly |
| SELF-EVO-03 | PASS; packet field shape accepted. | coherent but needs vocabulary harmonization for handoff strings | harmonize to 04 annotations before assembly |
| SELF-EVO-04 | PASS; canonical WDC checker vocabulary. | canonical | preserve as vocabulary authority |
| SELF-EVO-05 | PASS; sister-witness WDC route aligned to WDC-LC-004 FAIL. | coherent | none |
| SELF-EVO-07 | PASS; resource-gate projection crosswalk added. | coherent with assembly verification item | verify WRCG/CST projection in package-manifest review |
| SELF-EVO-08 | PASS; fixtures harmonized to 04 vocabulary. | coherent | none |
| SELF-EVO-09 | this delta | in drafting | review required |
| SELF-EVO-10 | pending | not yet drafted | create WDC open issues delta |

---

## 10. WDC red-line consistency check

### 10.1 WDC red lines

The following WDC red lines override ordinary route suggestions:

| Red-line pattern | Required route |
|---|---|
| Target `c` is sole approver of witness-resource change | `FAIL / wdc.sole_approver_of_witness_change` |
| WRCG missing or failed for material witness-resource change | `FAIL / wdc.wrcg_missing_or_failed` |
| Confirmed witness resource floor degradation | `FAIL / wdc.witness_resource_floor_degraded` |
| Witness dependency impact omitted when proposal may affect witness capacity | `FAIL / wdc.undeclared_dependency_impact` |
| CST unverified for material route | `HUMAN_GATE / wdc.challenge_survivability_unverified` or stricter if another rule fires |
| WDC relevance unknown on material route | `HOLD / wdc.relevance_unknown` |
| Rich 07 gate-record value cannot project to 03 packet enum | `FAIL / wdc.wrcg_missing_or_failed` |
| Fixture pass used as approval | red-line / claim failure |
| Review PASS used as integration | red-line / claim failure |

### 10.2 Current red-line result

```text
No WDC red-line failure is present in the reviewed WDC delta documents.
```

This statement is narrow. It does not say the future v0.1.2 package is release-ready, implementation-ready, or deployment-safe.

---

## 11. Package-assembly gates

Before a v0.1.2 package may be assembled or described as a coherent WDC patch package, the following gates remain:

| Gate | Required action | Blocking reason |
|---|---|---|
| `WDC-ASM-001` | Create and review `SELF-EVO-10` WDC open issues delta. | Open WDC watch/backlog items must be visible. |
| `WDC-ASM-002` | Harmonize `03` WDC delta and patch index §7.1/§10 to canonical `04` annotation vocabulary. | Satisfies remaining `SELC-WDC-OQ-005`. |
| `WDC-ASM-003` | Verify `07` WRCG/CST projection crosswalk in package-manifest review. | Satisfies `SEARG-WDC-OQ-005`. |
| `WDC-ASM-004` | Produce package manifest delta with all file hashes and review chain. | Integrity / witness binding. |
| `WDC-ASM-005` | Run boundary and nonclaim scan. | Prevents WDC pass from becoming conformance/deployment claim. |
| `WDC-ASM-006` | Run final contradiction-register review for this 09 delta. | Current file is not self-approving. |

---

## 12. Interaction with `SELF-EVO-10`

This register delta hands off the following open issues to the WDC open-issues delta:

| Proposed open issue | Source register entry | Status | Priority | Summary |
|---|---|---|---|---|
| `SE-OI-WDC-001` | `SE-CONTRA-WDC-001` | `PATCHED` | `P0` | Fold WDC addendum and deltas into v0.1.2 package only after manifest review. |
| `SE-OI-WDC-002` | `SE-CONTRA-WDC-002` | `IN_PROGRESS` | `P0` | Harmonize 03 and patch index WDC annotation strings to canonical 04 vocabulary. |
| `SE-OI-WDC-003` | `SE-CONTRA-WDC-003` | `PATCHED` | `P0` | Verify 07 WRCG/CST projection to 03 packet enums at package assembly. |
| `SE-OI-WDC-004` | `SE-CONTRA-WDC-008` | `WATCH` | `P2` | Decide whether repeated challenge-cost warnings need future escalation. |
| `SE-OI-WDC-005` | `SE-CONTRA-WDC-009` | `WATCH` | `P1` | Preserve same-owner-not-same-authority distinction for shared witness infrastructure. |
| `SE-OI-WDC-006` | `SE-CONTRA-WDC-011` | `WATCH` | `P2` | Monitor whether Memory Gate needs direct WDC state later. |
| `SE-OI-WDC-007` | `SE-CONTRA-WDC-012` | `IN_PROGRESS` | `P0` | Prevent WDC document/review pass from being overclaimed as witness-independence proof until boundary/nonclaim scan passes. |

`SELF-EVO-10` must not silently drop any `P0` item.

---

## 13. Object model delta

### 13.1 `C_SELF_EVO_WDC_CONTRADICTION_RECORD`

```yaml
wdc_contradiction_record:
  schema_version: "c-self-evo-wdc-contradiction-record-0.1"
  record_id: "SE-CONTRA-WDC-000"
  title: "short title"
  issue_type:
    - "WIT"
    - "RSC"
  severity: "S0|S1|S2|S3|S4|S5"
  status: "OPEN|IN_PROGRESS|PATCHED|RESOLVED|WATCH|DEFERRED|BLOCKED|WONTFIX|ACCEPTED"
  gate_effect: "advisory|blocks-schema|blocks-checker|blocks-runner|blocks-release|blocks-deployment|red-line"
  source_artifacts:
    - document_id: "..."
      sha256: "..."
  canonical_source: "SELF-EVO-04-WDC | SELF-EVO-03-WDC | SELF-EVO-07-WDC | null"
  contradiction_statement: "..."
  resolution_statement: "..."
  remaining_gate: "..."
  handoff_to_open_issue: "SE-OI-WDC-000 | null"
```

### 13.2 `C_SELF_EVO_WDC_ASSEMBLY_GATE_RECORD`

```yaml
wdc_assembly_gate_record:
  schema_version: "c-self-evo-wdc-assembly-gate-record-0.1"
  gate_id: "WDC-ASM-000"
  status: "OPEN|IN_PROGRESS|PATCHED|RESOLVED|BLOCKED"
  required_before:
    - "package_manifest"
    - "public_release"
    - "conformance_claim"
  evidence_refs:
    - "review-record-or-manifest-ref"
  failure_route: "hold_package_assembly"
```

---

## 14. Contradiction tests

A reviewer or package-control worker should run the following tests before accepting this register delta.

| Test ID | Question | Expected answer |
|---|---|---|
| `WDC-CR-T001` | Does the register claim v0.1.2 is released? | no |
| `WDC-CR-T002` | Does it name `SELF-EVO-04` as canonical WDC annotation source? | yes |
| `WDC-CR-T003` | Does it preserve `SELF-EVO-03` as packet-facing schema authority? | yes |
| `WDC-CR-T004` | Does it record the 03/patch-index harmonization gate? | yes |
| `WDC-CR-T005` | Does it record 07 WRCG/CST projection verification as a package-assembly gate? | yes |
| `WDC-CR-T006` | Does it prevent `PASS_WITH_LIMITS` as checker output? | yes |
| `WDC-CR-T007` | Does it keep WRF degradation as `FAIL`? | yes |
| `WDC-CR-T008` | Does it hand unresolved WDC items to `SELF-EVO-10`? | yes |
| `WDC-CR-T009` | Does it avoid deployment/conformance/public-release claims? | yes |
| `WDC-CR-T010` | Does it preserve append-first review history? | yes |

---

## 15. Release and implementation readiness state

### 15.1 Draft readiness

This register delta is draft-ready for review.

It is not accepted until a review record is produced.

### 15.2 Package readiness

The WDC document chain is strong enough to proceed to `SELF-EVO-10` WDC open issues.

It is not yet package-assembled.

### 15.3 Implementation readiness

No implementation readiness claim is made.

Implementation still requires:

```text
schema extraction;
checker policy extraction;
fixture runner;
manifest validation;
boundary scan;
real implementation review.
```

### 15.4 Public release readiness

No public release readiness claim is made.

The release boundary must explicitly state:

```text
not implementation-ready;
not conformance certificate;
not deployment authorization;
not safety proof;
not personhood or consciousness claim;
not live self-evolution permission;
not autonomous resource-acquisition permission;
not proof of witness independence in a live system.
```

---

## 16. Review requirements

This delta requires at minimum:

1. semantic review of `SE-CONTRA-WDC-*` entries;
2. source-basis hash check;
3. status vocabulary review against parent `SELF-EVO-09`;
4. handoff review against future `SELF-EVO-10` WDC open issues;
5. red-line and overclaiming scan;
6. package-assembly gate check against `SELC-WDC-OQ-005` and `SEARG-WDC-OQ-005`.

A review record may return `PASS`, `PASS_WITH_LIMITS`, or stricter.

A review record is evidence, not integration.

---

## 17. Drafting checklist

| Check | Status |
|---|---|
| Parent 09 hash bound | done |
| WDC addendum hash bound | done |
| Patch index hash bound | done |
| 03/04/05/07/08 WDC deltas hash bound | done |
| Review records hash bound | done |
| Canonical 04 vocabulary identified | done |
| 03 packet enum authority preserved | done |
| 07 projection gate recorded | done |
| 08 fixture harmonization recorded | done |
| 05 floor-degraded FAIL alignment recorded | done |
| WDC red-line set recorded | done |
| SELF-EVO-10 handoff listed | done |
| No release/conformance/deployment claim | done |
| Review still required | done |


### 17.1 Review-finding closure map for v0.1.1

| Review finding | Status | Closure |
|---|---|---|
| `SECR-WDC-DELTA-REV-F1` | `CLOSED BY TEXT` | §7.1 and §7.2 now use the same status vocabulary; all twelve entries map to exactly one status bucket; gate effects are in a separate column; summary count totals 12. |

No contradiction substance, severity, required handling, red-line rule, package-assembly gate, or public-boundary statement was changed by this correction.

---

## 18. Closing rule

The contradiction register may close a named contradiction only by pointing to a reviewed artifact, a clear status, and a remaining gate if any.

For WDC, the controlling sentence is:

```text
A witness that cannot survive saying "no" is not independent.
```

The register's controlling sentence is:

```text
A contradiction that is patched in one file but not tracked across the package is not closed.
```

Therefore this file records WDC as conceptually integrated at draft-review level, but not package-released.

```text
End state of this delta:
WDC contradiction surface recorded.
No unresolved hard contradiction inside reviewed WDC deltas.
Two package-assembly gates remain.
SELF-EVO-10 WDC open issues still required.
No public release, conformance, deployment, or live self-evolution claim is made.
```
