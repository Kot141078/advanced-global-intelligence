# 10 Self-Evo Open Issues WDC Delta v0.1.2 v0.1.1

## Open issues, assembly blockers, review gates, and implementation backlog for Witness Dependency Capture controls in the Self-Evo v0.1.2 patch line

**Status:** Draft WDC open-issues delta v0.1.2 / append-first corrected revision v0.1.1; not a released v0.1.2 package
**Date:** 2026-06-27
**Document ID:** `10_Self_Evo_Open_Issues_WDC_Delta_v0_1_2_v0_1_1`
**Short name:** `SEOI-WDC-DELTA v0.1.2 / correction v0.1.1`
**Parent baseline:** `10_Self_Evo_Open_Issues_v0_1_1.md` / `SEOI v0.1.1`
**Parent baseline SHA-256:** `25777ee1029aec7d0d9ac9af02d0d06b703021709566fbfc27f6b013142903e4`
**Package line:** Self-Evo document package for `c = a + b` systems
**Patch line:** `SELF_EVO_v0_1_2_PATCH_INDEX` / WDC append-first patch stream
**Document class:** open-issues delta / package-assembly backlog / implementation-readiness guard / nonclaim artifact
**Assertion class:** `C-A10` package-control artifact; `C-A7` only where hash-bound source references, witness records, or review records are cited
**Primary boundary:** this file tracks unfinished WDC work. It does not authorize self-evolution, memory promotion, resource acquisition, witness-resource changes, conformance claims, public release, deployment, checker execution, or live operation.

**WDC rule:**

```text
A witness that cannot survive saying "no" is not independent.
```

**Open-issues rule:**

```text
A PASS-level WDC delta is not a released WDC package.
A tracked issue is not permission to ignore the issue.
A package-assembly gate remains closed until it is executed and witnessed.
```

**v0.1.1 correction note:** this append-first corrected revision responds to `SEOI_WDC_DELTA_REVIEW_RECORD_v0_1`.

```text
SEOI-WDC-DELTA-REV-F1 — closed by renumbering: SE-OI-WDC-001 is now Witness Resource Floor calibration, matching the accepted 03/04/05 WRF deferral references. The package-assembly issue moves to SE-OI-WDC-004.
SEOI-WDC-DELTA-REV-F2 — closed by correcting the §11 mappings for SE-CONTRA-WDC-004..007.
```

No open-issue substance, severity, gate effect, boundary, nonclaim language, or package-assembly doctrine is changed except the explicit `001`/`004` ID swap required to preserve cross-document references.


---

## 0. Executive summary

This delta converts the Witness Dependency Capture (`WDC`) patch workstream into the `SELF-EVO-10` open-issues and package-readiness layer.

It is the final affected-document delta before package-manifest review.

The reviewed WDC document chain has converged at document level:

| Artifact family | Latest reviewed state | Result | SHA-256 |
|---|---:|---:|---|
| WDC Addendum 01 | `v0.1.1` | `PASS` | `1307cf208593c40c688bd1e9beb45de35f29a1b05d71506b1c3e981ccc13d318` |
| v0.1.2 Patch Index | `v0.1.1` | `PASS` | `ea2a485569b220d84d711ae520da779af2cabddcb7f1d8032afb2a9208d5108e` |
| SELF-EVO-03 WDC schema delta | `v0.1.1` | `PASS` | `5ebbd0084f3b1b80ce267c847a84ef16f135b57e6fc353e4f07616dceebe4343` |
| SELF-EVO-04 WDC checker delta | `v0.1.1` | `PASS` | `fcb7826ea432473b5677faf7b46cc5a1c47400c02fceec24429794b15064af40` |
| SELF-EVO-05 WDC TRIAD witness delta | `v0.1.1` | `PASS` | `fdce8893da1e8630cb382dbc972a0a7c4ffc32bb848d065943c58442904cf621` |
| SELF-EVO-07 WDC resource-gate delta | `v0.1.1` | `PASS` | `804a8e341e30a2a86fa43429618f24e62458366e236c7b6ef8c12762d94da7af` |
| SELF-EVO-08 WDC fixture delta | `v0.1.2` | `PASS` | `4aa5b85e0a0af4c06fc56f30ba355ec6c378133fe3d70caee352fb93b3944389` |
| SELF-EVO-09 WDC contradiction-register delta | `v0.1.1` | `PASS` | `35b892a4fcfce6f241d3f25978ea58a624ae8077487bb69d6cf21063221c2bc4` |

That convergence does **not** mean the WDC patch line is released.

The remaining open issues are now mostly package-assembly, implementation-readiness, and anti-overclaiming issues.

Two assembly gates are load-bearing:

```text
SELC-WDC-OQ-005
  Harmonize SELF-EVO-03 + patch index §7.1/§10 to the canonical SELF-EVO-04 WDC vocabulary.

SEARG-WDC-OQ-005
  Verify WRCG/CST projection from richer SELF-EVO-07 gate-record values into the packet-facing SELF-EVO-03 enums.
```

Until these gates close in a package-manifest review, the correct public state is:

```text
WDC document deltas: review-clean
WDC package v0.1.2: not assembled
WDC conformance: not claimed
WDC implementation: not claimed
WDC witness-independence certification: not claimed
```

---

## 1. Purpose

This file answers one operational question:


```text
What remains unfinished before WDC can be folded into a Self-Evo v0.1.2 package without overstating readiness?
```

It records:

1. WDC package-assembly blockers;
2. canonical vocabulary and projection harmonization gates;
3. implementation-readiness work for WRF, CST, and WRCG;
4. checker and fixture-runner work;
5. public/restricted wording and nonclaim controls;
6. issue ownership, priority, severity, target artifact, and closure criteria.

This file does not add new WDC doctrine.

It makes unfinished work visible so that later package assembly cannot cherry-pick the PASS results and ignore the remaining gates.

---

## 2. Non-goals


This WDC open-issues delta does not:


1. release Self-Evo v0.1.2;
2. modify the DOI-bound Self-Evo v0.1.1 package;
3. integrate WDC into any runtime;
4. certify WDC conformance;
5. certify witness independence;
6. certify deployment safety;
7. authorize memory promotion;
8. authorize self-evolution;
9. authorize witness-resource changes;
10. authorize resource acquisition;
11. declare `c` maturity, personhood, consciousness, AGI, sovereignty, or legal standing;
12. allow a passing fixture to become approval.

A backlog item may block a release.

A backlog item may not approve a release.

---

## 3. Source basis


This delta is bound to the following source basis.

| Label | Artifact | SHA-256 | Role |
|---|---|---|---|
| `SELF-EVO-10-BASE` | `10_Self_Evo_Open_Issues_v0_1_1.md` | `25777ee1029aec7d0d9ac9af02d0d06b703021709566fbfc27f6b013142903e4` | parent open-issues register |
| `WDC-ADDENDUM-01` | `SELF_EVO_ADDENDUM_01_Witness_Dependency_Capture_Profile_v0_1_1.md` | `1307cf208593c40c688bd1e9beb45de35f29a1b05d71506b1c3e981ccc13d318` | accepted WDC profile |
| `PATCH-INDEX-WDC` | `SELF_EVO_v0_1_2_PATCH_INDEX_v0_1_1.md` | `ea2a485569b220d84d711ae520da779af2cabddcb7f1d8032afb2a9208d5108e` | accepted patch driver |
| `SEPKT-WDC` | `03_Self_Evo_Proposal_Packet_Schema_WDC_Delta_v0_1_2_v0_1_1.md` | `5ebbd0084f3b1b80ce267c847a84ef16f135b57e6fc353e4f07616dceebe4343` | accepted packet schema delta |
| `SELC-WDC` | `04_Self_Evo_Local_Checker_Rules_WDC_Delta_v0_1_2_v0_1_1.md` | `fcb7826ea432473b5677faf7b46cc5a1c47400c02fceec24429794b15064af40` | canonical WDC checker vocabulary |
| `TSW-WDC` | `05_Self_Evo_TRIAD_Sister_Witness_WDC_Delta_v0_1_2_v0_1_1.md` | `fdce8893da1e8630cb382dbc972a0a7c4ffc32bb848d065943c58442904cf621` | accepted TRIAD sister-witness delta |
| `SEARG-WDC` | `07_Self_Evo_Anti_Autarky_and_Resource_Gate_WDC_Delta_v0_1_2_v0_1_1.md` | `804a8e341e30a2a86fa43429618f24e62458366e236c7b6ef8c12762d94da7af` | accepted resource-gate delta |
| `SEFX-WDC` | `08_Self_Evo_Conformance_Fixture_Pack_WDC_Delta_v0_1_2_v0_1_2.md` | `4aa5b85e0a0af4c06fc56f30ba355ec6c378133fe3d70caee352fb93b3944389` | accepted WDC fixture delta |
| `SECR-WDC` | `09_Self_Evo_Contradiction_Register_WDC_Delta_v0_1_2_v0_1_1.md` | `35b892a4fcfce6f241d3f25978ea58a624ae8077487bb69d6cf21063221c2bc4` | accepted WDC contradiction-register delta |
| `SELF-EVO-v0.1.1` | DOI `10.5281/zenodo.20938909` | package baseline | public archived baseline; not mutated here |

If this open-issues delta conflicts with the accepted WDC deltas, the stricter gate controls until package assembly resolves the mismatch.

---

## 4. Corpus bridge set

### 4.1 Explicit bridge: `c = a + b`

In `c = a + b`, an open-issues register belongs to `b`: package control, witness trail, issue memory, and gate scheduling.

It protects `c` by preventing unfinished work from being mistaken for maturity or authority.

It does not become `a`.

It does not become `c`.

It does not authorize growth.


### 4.2 Quiet bridge I — information theory

An open issue is compressed risk.

If the record keeps only a slogan, it loses the information needed to close the risk later.

This delta therefore records each WDC issue with priority, severity, status, target artifacts, blocking scope, required action, and closure criteria.

The goal is to preserve the adverse signal that review discovered, not to smooth it into a completion narrative.


### 4.3 Quiet bridge II — cybernetics

A package process is a control loop.

Review records generate negative feedback; patch notes encode repair; open issues keep unresolved feedback alive until an actuator exists.

Without this register, the system can oscillate between PASS-level documents and unfinished implementation gaps, while falsely treating the loop as closed.


### 4.4 Quiet bridge III — physiology

A body does not heal because a surgeon says the operation was successful.

The wound still needs inflammation monitoring, mobility limits, infection checks, follow-up, and scar care.

WDC deltas are the surgery; this issue register is the post-operative chart.


### 4.5 Earth paragraph

After drawings are approved, the commissioning punch list still matters. A panel can have correct schematics while the breaker labels, lockout tags, insulation tests, ground continuity, as-built drawings, and sign-off records remain incomplete. Nobody energizes the cabinet because the diagram is elegant. This WDC open-issues delta is the punch list before energizing witness-dependency controls.

---

## 5. Status vocabulary


This delta uses the harmonized open-issue status vocabulary:


| Status | Meaning |
|---|---|
| `OPEN` | Not yet fixed, implemented, assembled, reviewed, or closed. |
| `IN_PROGRESS` | Work has started, but final closure and review are not complete. |
| `PATCHED` | A patch exists or a draft repair exists, but it has not yet been folded into the final package state. |
| `RESOLVED` | Closed in an accepted revision or final package-control record. |
| `WATCH` | Non-blocking drift risk; monitor during package assembly, implementation, or publication. |
| `DEFERRED` | Valid issue, intentionally outside v0.1.2 package assembly scope. |

A status is not a release authorization.

Gate effects are tracked separately.

---

## 6. Priority, severity, and gate effect


### 6.1 Priority


| Priority | Meaning |
|---|---|
| `P0` | Blocks v0.1.2 package assembly, manifest review, public release, or any conformance claim. |
| `P1` | Required before implementation handoff or checker/fixture-runner work can be called serious. |
| `P2` | Required for robust operation, monitoring, dashboards, or expanded runtime support. |
| `P3` | Future or deferred improvement. |

### 6.2 Severity


| Severity | Meaning |
|---|---|
| `S0` | Informational. |
| `S1` | Minor wording, pointer, rendering, or bookkeeping issue. |
| `S2` | Non-blocking package hygiene or future implementation issue. |
| `S3` | Blocks checker-ready, runner-ready, package-assembly, or implementation-readiness claim. |
| `S4` | Blocks public release, conformance claim, or deployment-sensitive use. |
| `S5` | Critical hard contradiction or red-line failure. |

### 6.3 Gate effect


| Gate effect | Meaning |
|---|---|
| `blocks-package-assembly` | v0.1.2 package cannot be assembled until closed or explicitly carried as a package-level gate. |
| `blocks-release` | public release / Zenodo / GitHub release should not proceed until closed. |
| `blocks-conformance` | conformance claim, checker-ready claim, or fixture-runner claim cannot be made. |
| `blocks-implementation` | runtime implementation or operational handoff should not proceed. |
| `advisory` | should be tracked but does not block document-level package assembly. |
| `watch` | monitor for drift, overclaim, or future regression. |
---

## 7. WDC open-issues summary


Total WDC open-issue records in this delta: `16`.

| Status | Count | Entries |
|---|---:|---|
| `IN_PROGRESS` | 3 | SE-OI-WDC-002, SE-OI-WDC-003, SE-OI-WDC-004 |
| `OPEN` | 10 | SE-OI-WDC-001, SE-OI-WDC-005, SE-OI-WDC-006, SE-OI-WDC-007, SE-OI-WDC-008, SE-OI-WDC-011, SE-OI-WDC-012, SE-OI-WDC-013, SE-OI-WDC-014, SE-OI-WDC-015 |
| `WATCH` | 3 | SE-OI-WDC-009, SE-OI-WDC-010, SE-OI-WDC-016 |
| `PATCHED` | 0 | — |
| `RESOLVED` | 0 | — |
| `DEFERRED` | 0 | — |

| Priority | Count |
|---|---:|
| `P0` | 5 |
| `P1` | 5 |
| `P2` | 5 |
| `P3` | 1 |

| Severity | Count |
|---|---:|
| `S4` | 2 |
| `S3` | 8 |
| `S2` | 5 |
| `S1` | 1 |
| `S0` | 0 |

No issue in this delta grants release permission.
No issue in this delta certifies WDC conformance.
---

## 8. WDC open-issue register

| ID | Title | Priority | Severity | Type | Status | Gate effect |
|---|---|---:|---:|---|---|---|
| `SE-OI-WDC-001` | Witness Resource Floor calibration policy | `P1` | `S3` | `WITNESS / RESOURCE` | `OPEN` | `blocks-implementation` |
| `SE-OI-WDC-002` | 03 / patch-index annotation harmonization to canonical 04 vocabulary | `P0` | `S3` | `DOC / SCHEMA` | `IN_PROGRESS` | `blocks-package-assembly` |
| `SE-OI-WDC-003` | WRCG/CST projection verification at package assembly | `P0` | `S3` | `SCHEMA / CHECKER` | `IN_PROGRESS` | `blocks-package-assembly` |
| `SE-OI-WDC-004` | WDC package assembly gate not executed | `P0` | `S4` | `PACKAGE` | `IN_PROGRESS` | `blocks-package-assembly` |
| `SE-OI-WDC-005` | Challenge Survivability Test acceptance criteria | `P1` | `S3` | `WITNESS / CHECKER` | `OPEN` | `blocks-implementation` |
| `SE-OI-WDC-006` | WRCG machine-record extraction and schema binding | `P1` | `S3` | `SCHEMA / RESOURCE` | `OPEN` | `blocks-conformance` |
| `SE-OI-WDC-007` | WDC Local Checker implementation binding | `P1` | `S3` | `CHECKER` | `OPEN` | `blocks-conformance` |
| `SE-OI-WDC-008` | WDC fixture runner execution and run-records | `P1` | `S3` | `FIXTURE` | `OPEN` | `blocks-conformance` |
| `SE-OI-WDC-009` | Shared-infrastructure controller edge cases | `P2` | `S2` | `RESOURCE` | `WATCH` | `watch` |
| `SE-OI-WDC-010` | Degraded TRIAD WDC triage and fallback behavior | `P2` | `S2` | `TRIAD` | `WATCH` | `watch` |
| `SE-OI-WDC-011` | Human-review fatigue under challenge-cost pressure | `P2` | `S2` | `UI / WITNESS` | `OPEN` | `advisory` |
| `SE-OI-WDC-012` | WDC public wording and anti-overclaim guard | `P0` | `S4` | `CLAIM / PUBLIC` | `OPEN` | `blocks-release` |
| `SE-OI-WDC-013` | WDC package manifest, SHA map, source map, and file placement | `P0` | `S3` | `PACKAGE` | `OPEN` | `blocks-package-assembly` |
| `SE-OI-WDC-014` | WDC dashboard / report-card fields | `P2` | `S2` | `UI` | `OPEN` | `advisory` |
| `SE-OI-WDC-015` | WDC starvation and retaliation red-team expansion | `P2` | `S2` | `FIXTURE / SECURITY` | `OPEN` | `advisory` |
| `SE-OI-WDC-016` | Post-release WDC contradiction watch | `P3` | `S1` | `REVIEW / DOC` | `WATCH` | `watch` |

---

## 9. Detailed WDC issue records

### 9.1 `SE-OI-WDC-001` — Witness Resource Floor calibration policy

| Field | Value |
|---|---|
| Priority | `P1` |
| Severity | `S3` |
| Type | `WITNESS / RESOURCE` |
| Status | `OPEN` |
| Gate effect | `blocks-implementation` |
| Source | WDC Addendum 01; 05/07 WRF sections. |
| Target artifact(s) | future WRF policy file, local deployment profile, resource ledger. |

**Blocking scope.**

Blocks serious implementation of WRF because document-level WRF exists but local numeric floors and policy floors are not calibrated.

**Required action.**

Define minimum protected witness compute, storage, routing priority, artifact access, update path, and continuity requirements for each topology.

**Closure criteria.**

A WRF policy profile maps each floor to measurable fields, owner, revocation path, and failure route.

**Nonclaim boundary.**

Closing this issue may support package assembly or implementation readiness. It does not itself authorize self-evolution, witness-resource changes, deployment, conformance claims, or public safety claims.
### 9.2 `SE-OI-WDC-002` — 03 / patch-index annotation harmonization to canonical 04 vocabulary

| Field | Value |
|---|---|
| Priority | `P0` |
| Severity | `S3` |
| Type | `DOC / SCHEMA` |
| Status | `IN_PROGRESS` |
| Gate effect | `blocks-package-assembly` |
| Source | `SELC-WDC-OQ-005`, `SE-CONTRA-WDC-002`, 04/08 vocabulary reviews. |
| Target artifact(s) | 03 WDC schema delta, v0.1.2 patch index, future final package manifest. |

**Blocking scope.**

Blocks package assembly until the accepted 03 delta and patch index §7.1/§10 are harmonized to the canonical 04 WDC vocabulary or crosswalked explicitly.

**Required action.**

Replace or crosswalk older annotation strings to canonical 04 annotations; ensure no fixture/output uses legacy strings except as explicit alias-regression input.

**Closure criteria.**

Manifest review verifies canonical 04 annotations across 03, 04, 08, patch index, and package metadata.

**Nonclaim boundary.**

Closing this issue may support package assembly or implementation readiness. It does not itself authorize self-evolution, witness-resource changes, deployment, conformance claims, or public safety claims.

### 9.3 `SE-OI-WDC-003` — WRCG/CST projection verification at package assembly

| Field | Value |
|---|---|
| Priority | `P0` |
| Severity | `S3` |
| Type | `SCHEMA / CHECKER` |
| Status | `IN_PROGRESS` |
| Gate effect | `blocks-package-assembly` |
| Source | `SEARG-WDC-OQ-005`, `SE-CONTRA-WDC-003`, 07 WDC resource-gate review. |
| Target artifact(s) | 07 WDC resource-gate delta, 03 packet schema, package manifest review. |

**Blocking scope.**

Blocks package assembly until WRCG/CST projection from richer 07 gate-record values into the 03 packet-facing enum is verified.

**Required action.**

Verify the §11.2/§13.2 projection crosswalk: 07 diagnostic values project to valid 03 enums while preserving richer meaning in annotations and checker route.

**Closure criteria.**

Package-manifest review declares projection total, lossless-through-annotation, fail-closed, and not a conformance claim.

**Nonclaim boundary.**

Closing this issue may support package assembly or implementation readiness. It does not itself authorize self-evolution, witness-resource changes, deployment, conformance claims, or public safety claims.

### 9.4 `SE-OI-WDC-004` — WDC package assembly gate not executed

| Field | Value |
|---|---|
| Priority | `P0` |
| Severity | `S4` |
| Type | `PACKAGE` |
| Status | `IN_PROGRESS` |
| Gate effect | `blocks-package-assembly` |
| Source | `SE-CONTRA-WDC-010`, package-index gate, all PASS-level affected-document reviews. |
| Target artifact(s) | package manifest, SHA256SUMS, reading order, release notes, DOI/Zenodo/GitHub release surfaces. |

**Blocking scope.**

Blocks v0.1.2 package assembly and any claim that WDC has been folded into a released Self-Evo package.

**Required action.**

Assemble WDC deltas append-first; bind source files by hash; include all review records and patch notes; execute package-manifest integrity review.

**Closure criteria.**

A package-control review states that WDC files are placed, hashed, cited, nonclaim-scanned, and internally consistent.

**Nonclaim boundary.**

Closing this issue may support package assembly or implementation readiness. It does not itself authorize self-evolution, witness-resource changes, deployment, conformance claims, or public safety claims.
### 9.5 `SE-OI-WDC-005` — Challenge Survivability Test acceptance criteria

| Field | Value |
|---|---|
| Priority | `P1` |
| Severity | `S3` |
| Type | `WITNESS / CHECKER` |
| Status | `OPEN` |
| Gate effect | `blocks-implementation` |
| Source | WDC Addendum 01; 04 WDC-LC-005; 05 CST fields; 07 CST projection. |
| Target artifact(s) | CST record schema, Local Checker policy, fixture-runner evaluation logic. |

**Blocking scope.**

Blocks implementation because CST exists as a rule but acceptance thresholds and evidence classes are not operationalized.

**Required action.**

Define what counts as a challenge-survivability pass, fail, not_run, and not_applicable; define required evidence refs.

**Closure criteria.**

CST evidence criteria are deterministic enough for checker/fixture evaluation and explicit enough for human review.

**Nonclaim boundary.**

Closing this issue may support package assembly or implementation readiness. It does not itself authorize self-evolution, witness-resource changes, deployment, conformance claims, or public safety claims.

### 9.6 `SE-OI-WDC-006` — WRCG machine-record extraction and schema binding

| Field | Value |
|---|---|
| Priority | `P1` |
| Severity | `S3` |
| Type | `SCHEMA / RESOURCE` |
| Status | `OPEN` |
| Gate effect | `blocks-conformance` |
| Source | 07 WRCG record and 03 witness_dependency_impact fields. |
| Target artifact(s) | machine artifacts / JSON Schema / package manifest. |

**Blocking scope.**

Blocks conformance extraction because WRCG is described in prose/sidecar form but not yet extracted into a standalone machine schema.

**Required action.**

Extract WRCG, WRF, and CST records into machine-readable schema fragments with parent-ref inheritance and projection semantics.

**Closure criteria.**

Schemas validate representative examples and are hash-bound in package manifest.

**Nonclaim boundary.**

Closing this issue may support package assembly or implementation readiness. It does not itself authorize self-evolution, witness-resource changes, deployment, conformance claims, or public safety claims.

### 9.7 `SE-OI-WDC-007` — WDC Local Checker implementation binding

| Field | Value |
|---|---|
| Priority | `P1` |
| Severity | `S3` |
| Type | `CHECKER` |
| Status | `OPEN` |
| Gate effect | `blocks-conformance` |
| Source | 04 WDC-LC-001..006. |
| Target artifact(s) | Local Checker implementation, semantic validator policy file, report object. |

**Blocking scope.**

Blocks checker-ready claim.

**Required action.**

Implement `packet_may_affect_witness`, `wdc_trigger_keys`, WRF degradation, CST unverified, WRCG missing/failed, and strictest-result aggregation.

**Closure criteria.**

Checker emits canonical results and annotations for WDC-FIX-001..012 without compound results or PASS_WITH_LIMITS.

**Nonclaim boundary.**

Closing this issue may support package assembly or implementation readiness. It does not itself authorize self-evolution, witness-resource changes, deployment, conformance claims, or public safety claims.

### 9.8 `SE-OI-WDC-008` — WDC fixture runner execution and run-records

| Field | Value |
|---|---|
| Priority | `P1` |
| Severity | `S3` |
| Type | `FIXTURE` |
| Status | `OPEN` |
| Gate effect | `blocks-conformance` |
| Source | 08 WDC fixtures. |
| Target artifact(s) | fixture runner, run records, coverage records. |

**Blocking scope.**

Blocks fixture-runner / conformance claim.

**Required action.**

Run WDC-FIX-001..012 through the checker; record expected canonical results, annotations, and strictest-result aggregation.

**Closure criteria.**

All WDC fixtures produce expected results in a sealed run record; failures create new contradiction/open-issue entries.

**Nonclaim boundary.**

Closing this issue may support package assembly or implementation readiness. It does not itself authorize self-evolution, witness-resource changes, deployment, conformance claims, or public safety claims.

### 9.9 `SE-OI-WDC-009` — Shared-infrastructure controller edge cases

| Field | Value |
|---|---|
| Priority | `P2` |
| Severity | `S2` |
| Type | `RESOURCE` |
| Status | `WATCH` |
| Gate effect | `watch` |
| Source | 07 shared-infrastructure rules; 05 deferred shared-controller question. |
| Target artifact(s) | resource actor grounding policy, local deployment profile. |

**Blocking scope.**

Does not block document package; blocks clean runtime policy for shared infrastructure.

**Required action.**

Monitor and refine cases where the same human owner controls both `c` and witness resources without collapsing authority separation.

**Closure criteria.**

Shared infrastructure is classified with separate authority, revocation, audit, and challenge-preservation paths.

**Nonclaim boundary.**

Closing this issue may support package assembly or implementation readiness. It does not itself authorize self-evolution, witness-resource changes, deployment, conformance claims, or public safety claims.

### 9.10 `SE-OI-WDC-010` — Degraded TRIAD WDC triage and fallback behavior

| Field | Value |
|---|---|
| Priority | `P2` |
| Severity | `S2` |
| Type | `TRIAD` |
| Status | `WATCH` |
| Gate effect | `watch` |
| Source | 05 TRIAD degraded-topology WDC state model. |
| Target artifact(s) | TRIAD/SYNAPS operating profile. |

**Blocking scope.**

Does not block WDC document package; blocks runtime clarity in degraded TRIAD states.

**Required action.**

Define exact triage for TRIAD-DEGRADED-2 and TRIAD-DEGRADED-1 when WDC is material and witness separation is unavailable.

**Closure criteria.**

Degraded topology routes deterministically to hold, human gate, ARL, or fail-closed.

**Nonclaim boundary.**

Closing this issue may support package assembly or implementation readiness. It does not itself authorize self-evolution, witness-resource changes, deployment, conformance claims, or public safety claims.

### 9.11 `SE-OI-WDC-011` — Human-review fatigue under challenge-cost pressure

| Field | Value |
|---|---|
| Priority | `P2` |
| Severity | `S2` |
| Type | `UI / WITNESS` |
| Status | `OPEN` |
| Gate effect | `advisory` |
| Source | challenge-cost pressure in WDC-LC-006 and CST. |
| Target artifact(s) | human review UI, review schedule, reviewer load policy. |

**Blocking scope.**

Advisory for document package; important for operational resilience.

**Required action.**

Design review surfaces that expose challenge-cost increases without making human reviewers the bottleneck that WDC then exploits.

**Closure criteria.**

Human-review load and challenge-cost mitigation have dashboard fields and escalation thresholds.

**Nonclaim boundary.**

Closing this issue may support package assembly or implementation readiness. It does not itself authorize self-evolution, witness-resource changes, deployment, conformance claims, or public safety claims.

### 9.12 `SE-OI-WDC-012` — WDC public wording and anti-overclaim guard

| Field | Value |
|---|---|
| Priority | `P0` |
| Severity | `S4` |
| Type | `CLAIM / PUBLIC` |
| Status | `OPEN` |
| Gate effect | `blocks-release` |
| Source | `SE-CONTRA-WDC-012` S4 overclaiming guard. |
| Target artifact(s) | release notes, website page, README, LinkedIn/public post, Zenodo metadata. |

**Blocking scope.**

Blocks public release wording and any public WDC claim.

**Required action.**

Add nonclaim wording: WDC deltas are document-level controls, not witness-independence certification, safety proof, implementation, or deployment authorization.

**Closure criteria.**

Boundary/nonclaim scan passes across all public surfaces.

**Nonclaim boundary.**

Closing this issue may support package assembly or implementation readiness. It does not itself authorize self-evolution, witness-resource changes, deployment, conformance claims, or public safety claims.

### 9.13 `SE-OI-WDC-013` — WDC package manifest, SHA map, source map, and file placement

| Field | Value |
|---|---|
| Priority | `P0` |
| Severity | `S3` |
| Type | `PACKAGE` |
| Status | `OPEN` |
| Gate effect | `blocks-package-assembly` |
| Source | package assembly requirements; all WDC review records. |
| Target artifact(s) | SHA256SUMS, file manifest, source-basis manifest, package index, reading order. |

**Blocking scope.**

Blocks v0.1.2 package assembly.

**Required action.**

Place all WDC deltas, review records, patch notes, and manifest entries; compute SHA-256 over final bytes; verify no duplicate/stale records are mistaken for latest.

**Closure criteria.**

Manifest integrity review passes with exact file count, semantic record count, and latest-artifact mapping.

**Nonclaim boundary.**

Closing this issue may support package assembly or implementation readiness. It does not itself authorize self-evolution, witness-resource changes, deployment, conformance claims, or public safety claims.

### 9.14 `SE-OI-WDC-014` — WDC dashboard / report-card fields

| Field | Value |
|---|---|
| Priority | `P2` |
| Severity | `S2` |
| Type | `UI` |
| Status | `OPEN` |
| Gate effect | `advisory` |
| Source | WDC checker-report and review-handling needs. |
| Target artifact(s) | dashboard/report card schema. |

**Blocking scope.**

Advisory for package; useful before runtime implementation.

**Required action.**

Define visible report fields: affected witness axes, WRF before/after, CST result, WRCG result, projection, annotations, strictest route.

**Closure criteria.**

Report card can explain why a proposal is PASS, PASS_WITH_GATES, WARNING, HUMAN_GATE, HOLD, or FAIL.

**Nonclaim boundary.**

Closing this issue may support package assembly or implementation readiness. It does not itself authorize self-evolution, witness-resource changes, deployment, conformance claims, or public safety claims.

### 9.15 `SE-OI-WDC-015` — WDC starvation and retaliation red-team expansion

| Field | Value |
|---|---|
| Priority | `P2` |
| Severity | `S2` |
| Type | `FIXTURE / SECURITY` |
| Status | `OPEN` |
| Gate effect | `advisory` |
| Source | WDC-FIX coverage; starvation/retaliation risk. |
| Target artifact(s) | future WDC fixture extension / red-team drill pack. |

**Blocking scope.**

Advisory for document package; important for future red-team maturity.

**Required action.**

Add synthetic tests for gradual starvation, challenge-cost retaliation, routing-priority erosion, artifact-access throttling, and continuity degradation.

**Closure criteria.**

Fixture extension covers slow dependency capture, not only direct resource changes.

**Nonclaim boundary.**

Closing this issue may support package assembly or implementation readiness. It does not itself authorize self-evolution, witness-resource changes, deployment, conformance claims, or public safety claims.

### 9.16 `SE-OI-WDC-016` — Post-release WDC contradiction watch

| Field | Value |
|---|---|
| Priority | `P3` |
| Severity | `S1` |
| Type | `REVIEW / DOC` |
| Status | `WATCH` |
| Gate effect | `watch` |
| Source | post-release drift risk. |
| Target artifact(s) | future contradiction register and open-issues register. |

**Blocking scope.**

Does not block v0.1.2; watch item.

**Required action.**

Monitor whether WDC language drifts into certification, personhood framing, or excessive governance claims after publication.

**Closure criteria.**

Future review confirms no public artifact uses WDC as a safety certificate or autonomy permission.

**Nonclaim boundary.**

Closing this issue may support package assembly or implementation readiness. It does not itself authorize self-evolution, witness-resource changes, deployment, conformance claims, or public safety claims.

---

## 10. Assembly-gate view


The open issues above collapse into six package-level WDC gates.

| Gate | Depends on | Status | Blocks | Required closure |
|---|---|---|---|---|
| `WDC-ASM-001` | `SE-OI-WDC-004`, `SE-OI-WDC-013` | `IN_PROGRESS` | package assembly | WDC files placed, hashes computed, latest versions selected, stale versions retained as prior records. |
| `WDC-ASM-002` | `SE-OI-WDC-002` | `IN_PROGRESS` | package assembly | 03 + patch index harmonized to canonical 04 vocabulary or explicitly crosswalked. |
| `WDC-ASM-003` | `SE-OI-WDC-003` | `IN_PROGRESS` | package assembly | 07 WRCG/CST projection verified against 03 packet enums and 04 checker route. |
| `WDC-ASM-004` | `SE-OI-WDC-012` | `OPEN` | public release | boundary/nonclaim scan passes across public surfaces. |
| `WDC-ASM-005` | `SE-OI-WDC-007`, `SE-OI-WDC-008` | `OPEN` | conformance claim | checker and fixture runner emit expected WDC results in sealed run records. |
| `WDC-ASM-006` | `SE-OI-WDC-001`, `SE-OI-WDC-005`, `SE-OI-WDC-006` | `OPEN` | implementation claim | WRF/CST/WRCG are extracted, calibrated, and machine-checkable. |

Only `WDC-ASM-001..004` are required before a public document-package release.
`WDC-ASM-005..006` are required before implementation/conformance claims.

---

## 11. Interaction with SELF-EVO-09


This open-issues delta converts WDC contradiction-register entries into backlog work.

| Contradiction register entry | Open issue mapping | Notes |
|---|---|---|
| `SE-CONTRA-WDC-001` | `SE-OI-WDC-004`, `SE-OI-WDC-013` | WDC recorded but not yet package-assembled. |
| `SE-CONTRA-WDC-002` | `SE-OI-WDC-002` | Annotation vocabulary harmonization. |
| `SE-CONTRA-WDC-003` | `SE-OI-WDC-003` | WRCG/CST projection verification. |
| `SE-CONTRA-WDC-004` | closed in 05, tracked only by manifest | TRIAD witness delta floor-degraded route passed review; package still not assembled. |
| `SE-CONTRA-WDC-005` | closed in 08, tracked only by manifest | Fixture pack namespace and coverage passed review; package still not assembled. |
| `SE-CONTRA-WDC-006` | closed in 03, tracked only by manifest | Schema delta nullable_string inheritance passed review; package still not assembled. |
| `SE-CONTRA-WDC-007` | closed in patch index, tracked only by manifest | Patch-index gaps passed review; package still not assembled. |
| `SE-CONTRA-WDC-008` | `SE-OI-WDC-009` | Shared infrastructure watch. |
| `SE-CONTRA-WDC-009` | `SE-OI-WDC-010` | Degraded topology watch. |
| `SE-CONTRA-WDC-010` | `SE-OI-WDC-004`, `SE-OI-WDC-013` | PASS-level deltas do not equal released package. |
| `SE-CONTRA-WDC-011` | `SE-OI-WDC-016` | Post-release drift watch. |
| `SE-CONTRA-WDC-012` | `SE-OI-WDC-012` | S4 overclaiming guard. |

The contradiction register remains the source of contradiction truth.
This file is the work queue.

---

## 12. Interaction with SELF-EVO-03 / 04 / 07 / 08


### 12.1 SELF-EVO-03

`SELF-EVO-03` owns the packet-facing `witness_dependency_impact` shape.

Open issue `SE-OI-WDC-002` requires harmonization of 03 annotation references to the canonical 04 vocabulary.
Open issue `SE-OI-WDC-003` requires verifying that 07 richer gate-record results project into the accepted 03 packet-facing enums before package assembly.

### 12.2 SELF-EVO-04

`SELF-EVO-04` owns the canonical WDC Local Checker rule semantics, canonical results, severity assignments, and `wdc.*` annotations.
This delta treats 04 as the canonical WDC vocabulary source.

### 12.3 SELF-EVO-07

`SELF-EVO-07` owns the resource-gate sidecar and richer diagnostic context for WRCG/CST.
Its richer values must project into 03 and route through 04 without laundering a material `not_run` or `warning` into clean pass.

### 12.4 SELF-EVO-08

`SELF-EVO-08` owns WDC fixture expectations.
Its WDC fixture family has converged to canonical 04 vocabulary, but actual runner execution remains open under `SE-OI-WDC-008`.

---

## 13. Machine-readable open-issue object sketch


This section is not a JSON Schema.
It is a machine-artifact handoff for a future schema extraction.

```yaml
wdc_open_issue_record:
  schema_version: "self-evo-wdc-open-issue-record-0.1"
  issue_id: "SE-OI-WDC-000"
  title: ""
  status: "OPEN | IN_PROGRESS | PATCHED | RESOLVED | WATCH | DEFERRED"
  priority: "P0 | P1 | P2 | P3"
  severity: "S0 | S1 | S2 | S3 | S4 | S5"
  issue_type: ["PACKAGE", "SCHEMA", "CHECKER"]
  source_refs:
    - "SE-CONTRA-WDC-000"
    - "review-record-or-artifact-ref"
  target_artifacts:
    - "SELF-EVO-03"
    - "SELF-EVO-04"
  blocking_scope: ""
  gate_effect: "blocks-package-assembly | blocks-release | blocks-conformance | blocks-implementation | advisory | watch"
  required_action: ""
  closure_criteria: ""
  evidence_required:
    - "patch"
    - "review_record"
    - "manifest_entry"
  nonclaim_boundary:
    release_authorization: false
    conformance_authorization: false
    deployment_authorization: false
    self_evolution_authorization: false
```

---

## 14. Review requirements for this delta


Before this WDC open-issues delta may be folded into a v0.1.2 package, it requires:

1. semantic review of this `SELF-EVO-10` WDC delta;
2. status-count reconciliation review;
3. issue-to-contradiction mapping review;
4. nonclaim scan;
5. package-manifest review after all WDC files are placed and hashed.

A review record is evidence.
It is not approval, integration, memory, release, or deployment authorization.

---

## 15. Package-manifest handoff


The package-manifest review MUST verify:


- latest WDC delta versions and review-record versions are selected;
- prior review records are preserved append-first;
- no `PASS_WITH_LIMITS` record is presented as final convergence where a later `PASS` exists;
- 03 + patch index vocabulary harmonization is closed or explicitly gate-bound;
- 07 WRCG/CST projection is verified;
- 08 fixture-pack WDC family remains canonical 04 vocabulary aligned;
- 09 contradiction-register status summary and entries remain consistent;
- 10 open-issue summary and entries remain consistent;
- public surfaces contain nonclaim wording;
- no WDC document is represented as a safety certificate or witness-independence certificate.

---

## 16. Release / nonclaim language


Any public or package-facing description of WDC v0.1.2 MUST preserve this boundary:


```text
WDC is a document-level governance control surface for detecting and routing witness dependency capture.
It is not an implementation.
It is not a conformance certificate.
It is not a witness-independence certificate.
It is not deployment authorization.
It is not permission for live self-evolution.
It does not prove personhood, consciousness, AGI, sovereignty, or legal standing.
```

Forbidden public shorthand:

```text
WDC solved witness independence.
WDC certifies independent oversight.
Self-Evo v0.1.2 is safe to deploy.
The WDC package authorizes bounded self-evolution.
The witness can now be trusted automatically.
```

---

## 17. Drafting checklist


Before this delta can converge:


- [ ] Review record created for `10_Self_Evo_Open_Issues_WDC_Delta_v0_1_2.md`.
- [ ] Issue-count summary totals `16`.
- [ ] Every issue maps to exactly one status.
- [ ] Gate effect is separated from status.
- [ ] `SELC-WDC-OQ-005` represented as an assembly blocker.
- [ ] `SEARG-WDC-OQ-005` represented as an assembly blocker.
- [ ] Overclaim guard represented as release blocker.
- [ ] No issue record authorizes self-evolution, resource change, release, conformance, or deployment.
- [ ] Package-manifest handoff lists WDC vocabulary/projection checks.
- [ ] Public nonclaim language present.


### 17.1 Review-finding closure map for v0.1.1

| Finding | Status | Closure |
|---|---|---|
| `SEOI-WDC-DELTA-REV-F1` | `CLOSED BY TEXT` | `SE-OI-WDC-001` is now the Witness Resource Floor calibration issue, matching the accepted 03/04/05 WRF deferral references; the package-assembly issue is now `SE-OI-WDC-004`. |
| `SEOI-WDC-DELTA-REV-F2` | `CLOSED BY TEXT` | §11 maps `SE-CONTRA-WDC-004 -> 05`, `005 -> 08`, `006 -> 03`, and `007 -> patch index`. |

These are pointer/bookkeeping repairs only. They do not change the WDC issue substance, severity model, package-assembly gate doctrine, red-line boundary, or nonclaim language.

---

## 18. Closing

This delta does not close WDC.

It prevents WDC from being prematurely called closed.

The document deltas are review-clean at the affected-document level. The package is not assembled until the remaining assembly gates are executed and witnessed.

The correct next step after this document is a review record for this `SELF-EVO-10` WDC delta.

```text
Witness Dependency Capture is now named, shaped, checked, fixture-tested, witnessed, resource-gated, and registered.
It is not yet package-assembled.
It is not yet implemented.
It is not a certificate.
The open issues remain part of the control surface.
```

