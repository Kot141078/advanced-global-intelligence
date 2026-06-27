# Self-Evo WDC v0.1.2 Package Assembly Manifest v0.1.1

## Witness Dependency Capture release-candidate manifest for the Self-Evo document package

**Status:** Draft package-assembly manifest / release-candidate control artifact / append-first corrected revision v0.1.1  
**Date:** 2026-06-27  
**Document ID:** `SELF_EVO_WDC_v0_1_2_PACKAGE_ASSEMBLY_MANIFEST_v0_1_1`  
**Short name:** `WDC-v0.1.2-ASSEMBLY-MANIFEST v0.1.1`  
**Release candidate:** `Self-Evo WDC v0.1.2`  
**Release class:** append-first minor / patch release candidate derived from a post-publication external review comment  
**Parent release:** Self-Evo Document Package v0.1.1 / DOI `10.5281/zenodo.20938909`  
**Primary subject:** Witness Dependency Capture (`WDC`) as a new control surface for bounded self-evolution of `c = a + b` systems  
**Primary boundary:** this manifest assembles and verifies a release candidate. It is not a public release, not a DOI deposit, not conformance certification, not deployment authorization, not live self-evolution permission, and not a witness-independence certificate.

**v0.1.1 correction note:** this append-first corrected revision responds to `SELF_EVO_WDC_v0_1_2_PACKAGE_ASSEMBLY_REVIEW_RECORD_v0_1`: `SEPAM-REV-F1` is closed by adding a full corpus bridge set, and `SEPAM-REV-F2` is closed by marking the `03` schema delta and patch-index SHA entries as provisional pending `WDC-ASM-002`, with an explicit harmonize-vs-crosswalk decision rule. No package-assembly gate is closed by this correction; all `WDC-ASM-*` gates remain pending.

---

## 0. Executive decision

The WDC workstream is no longer a single addendum.

It began as an addendum after an external comment identified a missing failure mode:

```text
formal witness separation is insufficient
if the witness depends on c for compute, storage, routing, continuity, budget, or artifact access
```

The resulting work produced a complete affected-document set across the Self-Evo package:

```text
03 Proposal Packet Schema
04 Local Checker Rules
05 TRIAD Sister Witness
07 Anti-Autarky and Resource Gate
08 Conformance Fixture Pack
09 Contradiction Register
10 Open Issues
```

All seven affected documents have converged to `PASS` at review level. Therefore this manifest treats the workstream as a **v0.1.2 release candidate**, not as a loose addendum.

Compact decision:

```text
WDC started as an addendum.
The reviewed artifact set now constitutes a Self-Evo v0.1.2 release candidate.
```

Release-state boundary:

```text
affected-document reviews: PASS
package assembly: not yet complete
public release: not yet authorized
conformance claim: not allowed
implementation claim: not allowed
```

---

## 1. Release identity

| Field | Value |
|---|---|
| Release candidate | `Self-Evo WDC v0.1.2` |
| Trigger | external review comment after v0.1.1 publication |
| Failure mode | `Witness Dependency Capture` |
| Release type | append-first package successor / patch release candidate |
| Parent package | `Self-Evo v0.1.1` |
| Parent DOI | `10.5281/zenodo.20938909` |
| Affected documents | `03`, `04`, `05`, `07`, `08`, `09`, `10` |
| Intentionally unaffected | `01`, `02`, `06` |
| Core result | all affected documents reached `PASS` review level |
| Current state | ready for package-manifest review, not public release |

---

## 2. Why this is a release candidate, not merely an addendum

An addendum would have recorded one new concept and stopped there.

This workstream changed the package-control surface in seven places:

1. The packet schema gained a place to declare witness dependency impact.
2. The local checker gained deterministic WDC rules.
3. TRIAD witness gained WRF / CST / WRCG handling.
4. The resource gate gained dependency-capture semantics distinct from direct autarky.
5. Fixtures gained a WDC regression family.
6. The contradiction register gained WDC contradiction records and package gates.
7. The open-issues register gained WDC assembly, calibration, implementation, UI, security, and overclaiming items.

That is a release scope.

The correct public framing is therefore:

```text
Self-Evo v0.1.2 WDC release candidate
```

not:

```text
small addendum to v0.1.1
```

---

## Corpus bridge set

### Explicit bridge: `c = a + b`

In `c = a + b`, a package-assembly manifest belongs to `b`: it is a documentary control surface that binds files, hashes, review records, patch notes, gate states, release posture, and nonclaim boundaries.

The manifest does not become `c`.

It does not become `a`.

It does not authorize growth, memory promotion, resource acquisition, implementation, release, deployment, or witness-independence certification.

Its function is to keep the release-candidate state legible:

```text
what exists;
what passed review;
which hashes are bound;
which gates remain pending;
which claims are still prohibited.
```

### Quiet bridge I: information theory

A package manifest is a compression of an artifact graph.

If the compression drops version state, hash provenance, pending gates, or provisional entries, the manifest becomes a lossy channel in the dangerous direction: it can make an unfinished candidate look finished.

For WDC v0.1.2, the load-bearing signal is not only that seven affected documents reached `PASS`. The manifest must also preserve the remaining uncertainty:

```text
03 / patch-index harmonization still pending;
07 WRCG/CST projection still pending verification;
08 fixture gate still pending assembly verification;
public release and conformance claims still prohibited.
```

### Quiet bridge II: cybernetics

A release process is a control loop over documents.

The affected-document reviews are feedback about individual parts. The package-assembly manifest is feedback about the whole loop: whether the reviewed parts are correctly wired together and whether any gate is being skipped by the appearance of completion.

A manifest that marks pending gates as pending is negative feedback. A manifest that turns `PASS` documents into a release without assembly review is positive feedback toward self-certification.

### Quiet bridge III: physiology

After a fracture is stabilized, the body still needs integration: alignment, load-bearing checks, inflammation markers, rehabilitation limits, and follow-up imaging.

The WDC deltas are the repaired tissues. This manifest is the clinical chart that says which parts are healed enough for the next review and which joints must not yet carry weight.

It is not the return-to-duty certificate.

### Earth paragraph

On a real engineering project, a set of approved drawings does not energize the building. Someone still checks the as-built index, revision table, test sheets, breaker labels, commissioning signatures, punch-list closures, and the red-line drawings. If a drawing is still provisional, the manifest must say so before anyone signs the handover pack. This WDC manifest plays the same role: it binds the reviewed documents, marks provisional entries, and keeps the remaining gates visible before release.

---

## 3. Source basis

The v0.1.2 WDC candidate is append-first over the DOI-bound v0.1.1 package. It does not mutate the parent DOI package.

### 3.1 Baseline documents retained unchanged

| Label | File | Lines | SHA-256 | Role |
|---|---|---|---|---|
| SELF-EVO-01 | `C_Self_Evolution_Gate_CGAM_TRIAD_SRLM_Profile_v0_1_1.md` | 2189 | `7918a8e6c5231bbe0fad47677fa56069f2ab002f79a8eee8c2838c434e66f2e3` | unchanged baseline in v0.1.2 WDC candidate |
| SELF-EVO-02 | `02_SRLM_Bounded_Growth_Contour_Profile_v0_1_1.md` | 2218 | `faee5682bb9463439923d7c7e7145c9f171d564622d9629820eb7c278cdd7de0` | unchanged baseline in v0.1.2 WDC candidate |
| SELF-EVO-06 | `06_Self_Evo_Memory_Gate_and_EA_Profile_v0_1_1.md` | 1955 | `7d2cb3ba9f951a1c321369eb245820cfa89e59cde39fb9ca3a55608b8f177893` | intentionally unaffected by WDC patch index |

### 3.2 Final WDC release-candidate artifacts

| Role | File | Lines | SHA-256 | Review status | Note |
|---|---|---|---|---|---|
| WDC concept profile | `SELF_EVO_ADDENDUM_01_Witness_Dependency_Capture_Profile_v0_1_1.md` | 953 | `1307cf208593c40c688bd1e9beb45de35f29a1b05d71506b1c3e981ccc13d318` | PASS | foundation failure-mode profile; kept as release-origin artifact |
| WDC patch index | `SELF_EVO_v0_1_2_PATCH_INDEX_v0_1_1.md` | 811 | `ea2a485569b220d84d711ae520da779af2cabddcb7f1d8032afb2a9208d5108e` | PASS / provisional pending `WDC-ASM-002` | release driver / affected-document plan; SHA entry is provisional until annotation harmonization or explicit crosswalk verification closes |
| SELF-EVO-03 WDC schema delta | `03_Self_Evo_Proposal_Packet_Schema_WDC_Delta_v0_1_2_v0_1_1.md` | 947 | `5ebbd0084f3b1b80ce267c847a84ef16f135b57e6fc353e4f07616dceebe4343` | PASS / provisional pending `WDC-ASM-002` | adds witness_dependency_impact packet surface; SHA entry is provisional until annotation harmonization or explicit crosswalk verification closes |
| SELF-EVO-04 WDC checker delta | `04_Self_Evo_Local_Checker_Rules_WDC_Delta_v0_1_2_v0_1_1.md` | 1154 | `fcb7826ea432473b5677faf7b46cc5a1c47400c02fceec24429794b15064af40` | PASS | canonical WDC checker vocabulary and rules |
| SELF-EVO-05 WDC TRIAD delta | `05_Self_Evo_TRIAD_Sister_Witness_WDC_Delta_v0_1_2_v0_1_1.md` | 1416 | `fdce8893da1e8630cb382dbc972a0a7c4ffc32bb848d065943c58442904cf621` | PASS | witness-resource-floor / CST / WRCG on sister-witness layer |
| SELF-EVO-07 WDC resource-gate delta | `07_Self_Evo_Anti_Autarky_and_Resource_Gate_WDC_Delta_v0_1_2_v0_1_1.md` | 1309 | `804a8e341e30a2a86fa43429618f24e62458366e236c7b6ef8c12762d94da7af` | PASS | dependency-capture resource gate and projection model |
| SELF-EVO-08 WDC fixture delta | `08_Self_Evo_Conformance_Fixture_Pack_WDC_Delta_v0_1_2_v0_1_2.md` | 1419 | `4aa5b85e0a0af4c06fc56f30ba355ec6c378133fe3d70caee352fb93b3944389` | PASS | WDC-FIX-001..012 fixture family |
| SELF-EVO-09 WDC contradiction delta | `09_Self_Evo_Contradiction_Register_WDC_Delta_v0_1_2_v0_1_1.md` | 777 | `35b892a4fcfce6f241d3f25978ea58a624ae8077487bb69d6cf21063221c2bc4` | PASS | WDC contradiction register and assembly gates |
| SELF-EVO-10 WDC open-issues delta | `10_Self_Evo_Open_Issues_WDC_Delta_v0_1_2_v0_1_1.md` | 992 | `bd87725ddf72ddeac09db597900c465492d570dbaaf68391e26b327aabba5790` | PASS | WDC open-issues backlog and release blockers |

### 3.2.1 Provisional SHA entries under `WDC-ASM-002`

The following SHA entries are accurate for the current reviewed release candidate, but **provisional** until `WDC-ASM-002` closes:

```text
SELF_EVO_v0_1_2_PATCH_INDEX_v0_1_1.md
03_Self_Evo_Proposal_Packet_Schema_WDC_Delta_v0_1_2_v0_1_1.md
```

Reason:

```text
WDC-ASM-002 still requires package-level verification that 03 and the patch index are harmonized or explicitly crosswalked to the canonical SELF-EVO-04 WDC vocabulary.
```

Current manifest choice:

```text
crosswalk-first release-candidate posture
```

This means the present hashes may remain final **only if** package-assembly review verifies that the existing 03 and patch-index texts are sufficiently crosswalked to the canonical 04 vocabulary without text mutation.

If actual textual harmonization is chosen instead, then 03 and the patch index MUST receive append-first corrected revisions, their SHA-256 values MUST change, and this manifest SHA map MUST be updated before final assembly.

No release, DOI deposit, package-integrity claim, or final source map may treat these two entries as final before `WDC-ASM-002` is closed.

### 3.3 Final review records

| Review role | File | Lines | SHA-256 | Result |
|---|---|---|---|---|
| WDC addendum re-review | `SELF_EVO_ADDENDUM_01_WDC_REVIEW_RECORD_v0_1_1.md` | 164 | `653150b3f8c054545a282d5b80c21044a1d27744cbc6acfc09827c9f84e21fd8` | PASS |
| Patch index re-review | `SELF_EVO_v0_1_2_PATCH_INDEX_REVIEW_RECORD_v0_1_1.md` | 157 | `74b3c2851afa1e0c65812fd0d16f0078e8548342d2d759c5017df8f7c99ba1e5` | PASS |
| 03 schema delta re-review | `SEPKT_WDC_DELTA_REVIEW_RECORD_v0_1_1.md` | 132 | `e89cab15a6f4235c9df9875a38b64b01a6f5df483812b9c840c225024ef93b5b` | PASS |
| 04 checker delta re-review | `SELC_WDC_DELTA_REVIEW_RECORD_v0_1_1.md` | 144 | `6a366d4eea862daec29262a1b0d7c29738ec9277375b7e3110d3751331c448f9` | PASS |
| 05 TRIAD delta re-review | `TSW_WDC_DELTA_REVIEW_RECORD_v0_1_1.md` | 134 | `bab488a95f7b5808ca1ae6f75dbfe0c79afefc9ab24f9f62438f4b4c5d8e1d47` | PASS |
| 07 resource-gate delta re-review | `SEARG_WDC_DELTA_REVIEW_RECORD_v0_1_1.md` | 151 | `8301029cad47e4265fbdf62a6f52d017610f2a649f997e71818f6f3cebf2dd5e` | PASS |
| 08 fixture delta re-review | `SEFX_WDC_DELTA_REVIEW_RECORD_v0_1_2.md` | 146 | `effcd108e6df56de9c1d840ed5c090352aab7dc60df01692fe0122ef18c08f00` | PASS |
| 09 contradiction delta re-review | `SECR_WDC_DELTA_REVIEW_RECORD_v0_1_1.md` | 133 | `68580c68134390d8122c4761c6a04dc6de68fafabb1dac3b0abbe94212e1b964` | PASS |
| 10 open-issues delta re-review | `SEOI_WDC_DELTA_REVIEW_RECORD_v0_1_1.md` | 166 | `c4db6ef14ec27dc5a5c4a618a59cbb5b4be41ab06d9fce3f575940b9f992fc2c` | PASS |

### 3.4 Final patch notes

| Patch-note role | File | Lines | SHA-256 |
|---|---|---|---|
| WDC addendum patch notes | `SELF_EVO_ADDENDUM_01_WDC_PATCH_NOTES_v0_1_1.md` | 93 | `16e613aac3aeb7c1eb2bfaad4983feaf0419c63fdef574a7c6d54f303be49626` |
| Patch index patch notes | `SELF_EVO_v0_1_2_PATCH_INDEX_PATCH_NOTES_v0_1_1.md` | 128 | `689183631b5bc76462460e65aee2e1798edb4ebe0ca30ea313e6194ed26588f5` |
| 03 schema WDC patch notes | `SEPKT_WDC_DELTA_PATCH_NOTES_v0_1_1.md` | 157 | `63764519ff39b99d4628c90baed76e0190af821c196fed4cbf87b4105bb26f4e` |
| 04 checker WDC patch notes | `SELC_WDC_DELTA_PATCH_NOTES_v0_1_1.md` | 181 | `22174efaa5c7a5123a7f6814fd17c8285961a4a0cba2f13bd1a0a4e1b0531c14` |
| 05 TRIAD WDC patch notes | `TSW_WDC_DELTA_PATCH_NOTES_v0_1_1.md` | 152 | `0e78947ba5079a72573c0427124bb2d342793cb798f35cd6db9eda0562567395` |
| 07 resource-gate WDC patch notes | `SEARG_WDC_DELTA_PATCH_NOTES_v0_1_1.md` | 194 | `9ecd2a014d2b52f468530c595a7ff65b603dd4f4a3c9a1ea1b2fcdab9410ce4c` |
| 08 fixture WDC patch notes | `SEFX_WDC_DELTA_PATCH_NOTES_v0_1_2.md` | 96 | `57ecbf8eacc7257af4262a398aaf4133b315ed62d0eaeb67e2df5f944d05c857` |
| 09 contradiction WDC patch notes | `SECR_WDC_DELTA_PATCH_NOTES_v0_1_1.md` | 151 | `325acd6daf38d88719d65cb026b9329f4b6ad9f43d7a6dbb26b752ca806da9d0` |
| 10 open-issues WDC patch notes | `SEOI_WDC_DELTA_PATCH_NOTES_v0_1_1.md` | 171 | `c508d091b8d00caf21a41b9ac43da0dd1151bb20bafa190871c7011e79acebf3` |

---

## 4. Affected-document status

| Document | WDC candidate artifact | Review result | Release-candidate status |
|---|---|---:|---|
| `03` | `03_Self_Evo_Proposal_Packet_Schema_WDC_Delta_v0_1_2_v0_1_1.md` | `PASS` | provisional pending `WDC-ASM-002`; ready for final assembly only if crosswalk verification closes without revision, or if a revised artifact replaces this SHA |
| `04` | `04_Self_Evo_Local_Checker_Rules_WDC_Delta_v0_1_2_v0_1_1.md` | `PASS` | canonical WDC checker vocabulary source |
| `05` | `05_Self_Evo_TRIAD_Sister_Witness_WDC_Delta_v0_1_2_v0_1_1.md` | `PASS` | ready for package assembly |
| `07` | `07_Self_Evo_Anti_Autarky_and_Resource_Gate_WDC_Delta_v0_1_2_v0_1_1.md` | `PASS` | ready for package assembly; projection check remains package gate |
| `08` | `08_Self_Evo_Conformance_Fixture_Pack_WDC_Delta_v0_1_2_v0_1_2.md` | `PASS` | WDC fixture-pack portion harmonized |
| `09` | `09_Self_Evo_Contradiction_Register_WDC_Delta_v0_1_2_v0_1_1.md` | `PASS` | contradiction register converged |
| `10` | `10_Self_Evo_Open_Issues_WDC_Delta_v0_1_2_v0_1_1.md` | `PASS` | final affected document converged |

Affected-document set status:

```yaml
affected_document_set:
  complete: true
  documents: ["03", "04", "05", "07", "08", "09", "10"]
  review_result: "PASS for all affected documents"
  package_assembled: false
  public_release_authorized: false
```

---

## 5. Release-candidate doctrine

### 5.1 Core WDC rule

```text
A witness that cannot survive saying no is not independent.
```

### 5.2 WDC distinction

```text
Direct resource capture:
  c obtains or expands resources for itself without accountable grounding.

Witness dependency capture:
  c preserves formal witness separation while controlling or starving the resources the witness needs to challenge c.
```

### 5.3 WDC control surface

```text
WRF  = Witness Resource Floor
CST  = Challenge Survivability Test
WRCG = Witness Resource Change Gate
```

### 5.4 Canonical vocabulary owner

`SELF-EVO-04 WDC delta` is the canonical source for:

```text
WDC-LC rule semantics
WDC canonical checker results
WDC severity assignments
WDC annotation strings
WDC pass-state annotations
```

### 5.5 Packet-vs-diagnostic enum doctrine

`SELF-EVO-03` remains packet-schema authority.

`SELF-EVO-07` may carry richer gate diagnostics only if they project into `SELF-EVO-03` packet-facing enums before package assembly, checker reporting, or manifest integration.

---

## 6. Package-assembly gates

The affected-document set has converged. The release candidate still has open package-assembly gates.

| Gate ID | Gate | Source | Required before public v0.1.2 release | Current state |
|---|---|---|---:|---|
| `WDC-ASM-001` | package placement, source map, SHA map, manifest, citation map | `SE-OI-WDC-004`, `SE-OI-WDC-013` | yes | pending |
| `WDC-ASM-002` | harmonize `03` and patch index annotation language to canonical `04` vocabulary | `SELC-WDC-OQ-005`, `SE-OI-WDC-002` | yes | pending |
| `WDC-ASM-003` | verify `07` WRCG/CST projection to `03` packet enums | `SEARG-WDC-OQ-005`, `SE-OI-WDC-003` | yes | pending |
| `WDC-ASM-004` | verify `08 §12.3` fixture gate: canonical-only outputs, no historical aliases, no `PASS_WITH_LIMITS` checker output | `SEFX` fixture delta | yes | pending |
| `WDC-ASM-005` | boundary / nonclaim scan | `SE-OI-WDC-012` | yes | pending |
| `WDC-ASM-006` | record remaining implementation open issues without overclaiming release readiness | `SE-OI-WDC-001`, `005`, `006`, `007`, `008` | yes | pending |

Assembly state:

```yaml
assembly_state:
  affected_documents_pass: true
  assembly_manifest_created: true
  assembly_manifest_reviewed: false
  annotation_harmonization_verified: false
  projection_verified: false
  fixture_gate_verified: false
  boundary_scan_complete: false
  release_ready: false
```

### 6.1 Harmonize-vs-crosswalk decision for `WDC-ASM-002`

`WDC-ASM-002` is not closed by this manifest.

The manifest adopts this decision rule:

```text
If the package is assembled as a delta-bundle release:
  explicit crosswalk verification may close WDC-ASM-002 without changing 03 or the patch index.

If the package is assembled as folded full v0.1.2 documents:
  textual harmonization is required, and 03 / patch index SHA values must be updated.
```

Until the assembly mode is chosen and `WDC-ASM-002` is reviewed, the 03 and patch-index SHA entries remain provisional.

The package-manifest review MUST explicitly record which path was used:

```text
crosswalk-only: current 03 / patch-index hashes may remain;
textual harmonization: new 03 / patch-index artifacts and hashes required.
```

---

## 7. Required package-manifest review checklist

A package-manifest review MUST verify at least:

1. Every final WDC artifact in §3.2 exists and matches its SHA-256.
2. Every final review record in §3.3 exists and matches its SHA-256.
3. Superseded review records are retained append-first, not deleted.
4. `03` and the patch index are harmonized or explicitly crosswalked to the canonical `04` WDC vocabulary.
5. The `07` WRCG/CST projection crosswalk is total, lossless via annotation/route, and fail-closed.
6. The `08` fixture gate accepts only canonical outputs and rejects `PASS_WITH_LIMITS` as checker output.
7. The `09` contradiction register and `10` open-issues backlog agree on WDC package gates.
8. The public wording does not claim conformance, deployment readiness, witness-independence certification, personhood, consciousness, sovereignty, AGI, or autonomous self-evolution authorization.
9. The package index / README / release notes identify this as `v0.1.2` release candidate until final release gates close.
10. The final release artifact set is either:
    - a delta-bundle release over v0.1.1, or
    - a folded full-document v0.1.2 release,
    and the choice is stated explicitly.

---

## 8. Recommended file placement

Recommended repository placement if assembled as a WDC patch release:

```text
official/self-evo/v0.1.2/
  README.md
  STATUS.md
  CITATION.cff
  LICENSE.md
  docs/markdown/
    01..10 full baseline-or-folded documents
    wdc_deltas/
      03_Self_Evo_Proposal_Packet_Schema_WDC_Delta_v0_1_2_v0_1_1.md
      04_Self_Evo_Local_Checker_Rules_WDC_Delta_v0_1_2_v0_1_1.md
      05_Self_Evo_TRIAD_Sister_Witness_WDC_Delta_v0_1_2_v0_1_1.md
      07_Self_Evo_Anti_Autarky_and_Resource_Gate_WDC_Delta_v0_1_2_v0_1_1.md
      08_Self_Evo_Conformance_Fixture_Pack_WDC_Delta_v0_1_2_v0_1_2.md
      09_Self_Evo_Contradiction_Register_WDC_Delta_v0_1_2_v0_1_1.md
      10_Self_Evo_Open_Issues_WDC_Delta_v0_1_2_v0_1_1.md
  controls/review_records/
    final/
    superseded/
  controls/patch_notes/
  manifests/
    SELF_EVO_WDC_v0_1_2_PACKAGE_ASSEMBLY_MANIFEST.md
    SHA256SUMS.txt
    FILE_MANIFEST.csv
    SOURCE_MAP.md
```

Recommended website framing:

```text
Self-Evo WDC v0.1.2 — Witness Dependency Capture release candidate / package update
```

not:

```text
Addendum 01 only
```

---

## 9. Machine-readable manifest summary

```yaml
self_evo_wdc_v0_1_2_assembly_manifest:
  schema_version: "wdc-package-assembly-manifest-0.1"
  document_id: "SELF_EVO_WDC_v0_1_2_PACKAGE_ASSEMBLY_MANIFEST"
  date: "2026-06-27"
  parent_release:
    name: "Self-Evo Document Package v0.1.1"
    doi: "10.5281/zenodo.20938909"
  release_candidate:
    name: "Self-Evo WDC v0.1.2"
    class: "append-first minor / patch release candidate"
    trigger: "external review comment identifying Witness Dependency Capture"
    primary_failure_mode: "Witness Dependency Capture"
  affected_documents:
    complete: true
    pass_level: true
    set: ["03", "04", "05", "07", "08", "09", "10"]
  unaffected_documents:
    - "01"
    - "02"
    - "06"
  canonical_sources:
    packet_schema: "03"
    checker_vocabulary: "04"
    triad_witness_boundary: "05"
    resource_gate_projection: "07"
    fixture_family: "08"
    contradiction_register: "09"
    open_issue_backlog: "10"
  provisional_sha_entries:
    - "SELF_EVO_v0_1_2_PATCH_INDEX_v0_1_1.md"
    - "03_Self_Evo_Proposal_Packet_Schema_WDC_Delta_v0_1_2_v0_1_1.md"
  harmonize_vs_crosswalk_decision:
    current_manifest_posture: "crosswalk-first release candidate"
    textual_harmonization_if_folded_release: "required; update SHA map before final assembly"
    crosswalk_only_if_delta_bundle: "allowed only after WDC-ASM-002 verification"
  package_gates:
    WDC_ASM_001: "pending"
    WDC_ASM_002: "pending"
    WDC_ASM_003: "pending"
    WDC_ASM_004: "pending"
    WDC_ASM_005: "pending"
    WDC_ASM_006: "pending"
  claims:
    public_release: false
    conformance_certificate: false
    deployment_authorization: false
    implementation_claim: false
    live_self_evolution_permission: false
    witness_independence_certification: false
```

---

## 10. Release / nonclaim language

Any public release note or website page for this candidate MUST preserve this boundary:

```text
This release records and reviews a document-level WDC control surface.
It does not certify that any live system is witness-independent.
It does not authorize self-evolution.
It does not authorize resource acquisition.
It does not certify deployment safety.
It does not claim implementation conformance.
```

Acceptable short framing:

```text
Self-Evo WDC v0.1.2 adds a reviewed control surface for Witness Dependency Capture: the risk that a witness remains formally separate while becoming practically unable to challenge c because its compute, storage, routing, continuity, budget, or artifact access depends on the system being witnessed.
```

---

## 11. Next required artifact

The next control artifact should be:

```text
SELF_EVO_WDC_v0_1_2_PACKAGE_ASSEMBLY_REVIEW_RECORD_v0_1_1.md
```

Its task is to decide whether this manifest is internally consistent and whether package-assembly gates are correctly represented.

It must not release the package by itself.

---

## Review-finding closure map for v0.1.1

| Finding | Review source | Status in this revision | Closure surface |
|---|---|---|---|
| `SEPAM-REV-F1` | `SELF_EVO_WDC_v0_1_2_PACKAGE_ASSEMBLY_REVIEW_RECORD_v0_1.md` | `CLOSED BY TEXT` | Corpus bridge set added before §3: explicit `c = a + b`, information theory, cybernetics, physiology, and earth paragraph. |
| `SEPAM-REV-F2` | `SELF_EVO_WDC_v0_1_2_PACKAGE_ASSEMBLY_REVIEW_RECORD_v0_1.md` | `CLOSED BY TEXT` | §3.2 marks 03 and patch-index entries provisional pending `WDC-ASM-002`; §3.2.1 and §6.1 state the harmonize-vs-crosswalk decision rule and SHA-map update requirement. |

This closure map accepts the review findings as valid. It does not close any package-assembly gate.

---

## 12. Closing

The external comment did not merely add a note to the existing package.

It exposed a missing control axis. The subsequent artifact chain produced a reviewed affected-document set. That is enough to justify treating the workstream as a v0.1.2 release candidate.

The release candidate is real.

The release is not yet public.

```text
WDC is no longer only an addendum.
WDC is a Self-Evo v0.1.2 release candidate.
Package assembly review is now the next gate.
```
