# Self-Evo WDC v0.1.2 Package Assembly Manifest v0.1.4

## Witness Dependency Capture release-candidate manifest for the Self-Evo document package

**Status:** Draft package-assembly manifest / release-candidate control artifact / append-first gate-propagation revision v0.1.4  
**Date:** 2026-06-27  
**Document ID:** `SELF_EVO_WDC_v0_1_2_PACKAGE_ASSEMBLY_MANIFEST_v0_1_4`  
**Short name:** `WDC-v0.1.2-ASSEMBLY-MANIFEST v0.1.4`  
**Release candidate:** `Self-Evo WDC v0.1.2`  
**Release class:** append-first minor / patch release candidate derived from a post-publication external review comment  
**Parent release:** Self-Evo Document Package v0.1.1 / DOI `10.5281/zenodo.20938909`  
**Primary subject:** Witness Dependency Capture (`WDC`) as a new control surface for bounded self-evolution of `c = a + b` systems  
**Primary boundary:** this manifest assembles and verifies a release candidate. It is not a public release, not a DOI deposit, not conformance certification, not deployment authorization, not live self-evolution permission, and not a witness-independence certificate.

**Supersedes:** `SELF_EVO_WDC_v0_1_2_PACKAGE_ASSEMBLY_MANIFEST_v0_1_3.md` (`sha256: aa5fb978000d96df74c03dc735bcbd1c8170b9d34644e85b8297fd114759f917`; reviewed by `SELF_EVO_WDC_v0_1_2_PACKAGE_ASSEMBLY_REVIEW_RECORD_v0_1_3`, result `PASS`).  
**Immediate predecessor binding:** `SELF_EVO_WDC_v0_1_2_PACKAGE_ASSEMBLY_MANIFEST_v0_1_3.md` (`sha256: aa5fb978000d96df74c03dc735bcbd1c8170b9d34644e85b8297fd114759f917`).  
**Prior predecessor binding retained:** `SELF_EVO_WDC_v0_1_2_PACKAGE_ASSEMBLY_MANIFEST_v0_1_2.md` (`sha256: a3b919bbd4289b9ff6547153eb28de1f617907b7ff255fbf7e0c03593e4522b8`).  
**Predecessor manifest binding required by `SEPAM-V012-REV-F1` retained:** `SELF_EVO_WDC_v0_1_2_PACKAGE_ASSEMBLY_MANIFEST_v0_1_1.md` (`sha256: cde9178adf686bd4a463592325424462852ad0fb1314017642183fd78542f177`).  
**Supersession mode:** append-first; prior manifest revisions are retained and not overwritten.

**v0.1.2 propagation note:** this append-first revision propagates the `WDC-ASM-002` closure into the manifest SHA map. The package chose **textual harmonization**, not crosswalk-only retention: the `03` WDC schema delta and the v0.1.2 patch index are now bound to their harmonized final hashes. `WDC-ASM-002` is recorded as `CLOSED` on the basis of `WDC_ASM_002_GATE_CLOSURE_RECORD_v0_1.md` and its documentary review `PASS`. This v0.1.2 propagation note is retained for history; `WDC-ASM-003` is closed later by the v0.1.4 propagation note. This note itself does not close `WDC-ASM-001`, `WDC-ASM-004`, `WDC-ASM-005`, or `WDC-ASM-006`.

**v0.1.3 provenance correction note:** this append-first revision closes `SEPAM-V012-REV-F1` by binding the predecessor manifest `SELF_EVO_WDC_v0_1_2_PACKAGE_ASSEMBLY_MANIFEST_v0_1_1.md` to its SHA-256 value. No SHA-map artifact entry, gate state, claim boundary, WDC-ASM-002 closure state, or release posture is changed by this correction.

**v0.1.4 projection-gate propagation note:** this append-first revision propagates the `WDC-ASM-003` closure into the manifest gate state. `WDC-ASM-003` is recorded as `CLOSED` on the basis of `WDC_ASM_003_GATE_CLOSURE_RECORD_v0_1.md` and its documentary consistency review `PASS`. The machine flag `projection_verified` is now `true`. This revision does not close `WDC-ASM-001`, `WDC-ASM-004`, `WDC-ASM-005`, or `WDC-ASM-006`, and it does not perform fixture execution, boundary scan, final assembly, release, DOI deposit, conformance certification, deployment authorization, or witness-independence certification.

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

All seven affected documents converged to `PASS` at review level. The package-assembly manifest also converged to `PASS` as an artifact. `WDC-ASM-002` has a separate `c/a` gate-closure record whose documentary consistency check returned `PASS`. `WDC-ASM-003` now also has a separate `c/a` gate-closure record whose documentary consistency check returned `PASS`.

Therefore this manifest treats the workstream as a **Self-Evo WDC v0.1.2 release candidate**, not as a loose addendum.

Compact decision:

```text
WDC started as an addendum.
The reviewed artifact set now constitutes a Self-Evo v0.1.2 release candidate.
WDC-ASM-002 is closed and propagated into this SHA map.
WDC-ASM-003 is now closed and propagated into this manifest gate state.
```

Release-state boundary:

```text
affected-document reviews: PASS
package-assembly manifest: PASS as artifact
WDC-ASM-002: CLOSED
WDC-ASM-003: CLOSED
WDC-ASM-001/004/005/006: pending
public release: not authorized
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
| Current state | two package gates closed (`WDC-ASM-002`, `WDC-ASM-003`); remaining gates pending; not public release |

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
7. The open-issues register gained WDC assembly, calibration, implementation, UI, security, and overclaiming backlog items.

The work then moved beyond document-level review and entered package assembly:

```text
package manifest created and reviewed;
03 and patch index textually harmonized to canonical 04 vocabulary;
WDC-ASM-002 closure recorded as a c/a package-control act;
manifest SHA map updated to the final harmonized hashes;
07 WRCG/CST projection verified against 03 packet enums;
WDC-ASM-003 closure recorded as a c/a package-control act;
manifest gate state updated to `projection_verified: true`.
```

That is release-candidate behavior.

It is still not a release.

---

## Corpus bridge set

### Explicit bridge: `c = a + b`

In `c = a + b`, this manifest belongs to `b`.

It is a documentary control surface: source map, SHA map, gate state, review chain, package placement, and nonclaim boundary.

It protects `c` by preventing a reviewed idea from silently becoming authority. A delta may be correct; a review may be clean; two gates may even close. None of those facts by themselves authorize growth, memory write, deployment, or public conformance claim.

This manifest is therefore not `a`, not `c`, and not a decision to self-evolve. It is the package's versioned map of what has been bound, what has been closed, and what still remains locked.

### Quiet bridge I: information theory

A manifest is a channel.

If the channel drops version state, hash state, or gate state, it turns a release candidate into a misleading compression artifact. The reader sees "PASS" and loses the entropy that says "which file, which revision, which gate, which claim boundary."

`WDC-ASM-002` made this concrete. Before `WDC-ASM-002` closure, two entries were provisional. After textual harmonization and hash-binding review, the channel may transmit them as final harmonized hashes. After `WDC-ASM-003` closure, the channel may transmit `projection_verified: true`. Both changes have to be explicit, because a manifest is not prose; it is a binding surface for version state and gate state.

### Quiet bridge II: cybernetics

A release package is a control loop.

Contradiction records detect fault. Open issues preserve pending actuator state. Gate records convert candidate work into controlled closure. Manifest revisions feed the new state back into the package map.

If the feedback loop records `WDC-ASM-002` or `WDC-ASM-003` as closed but fails to update the manifest state, the loop oscillates: the gate says one thing and the package map says another. This revision removes that oscillation for `WDC-ASM-003` while keeping the remaining open gates visible.

### Quiet bridge III: physiology

An organism does not heal by declaring the wound closed. It heals by closing tissue, checking blood flow, preserving immune memory, and still watching for infection.

`WDC-ASM-002` was the first closed suture: the language of 03 and the patch index now matches the canonical 04 vocabulary, and the hashes bind to the files that exist. `WDC-ASM-003` is the second closed suture: the richer 07 WRCG/CST outcomes now project into the 03 packet enums without silent diagnostic loss. The organism is healthier, but the body is not discharged. Fixtures, boundary scan, remaining open issues, and final assembly are still part of the recovery plan.

### Earth paragraph

On a construction site, approving a revised drawing is not the same as energizing the building. When a panel schedule changes, the as-built package has to receive the new sheet number, the new revision, and the right signature trail. If the electrician works from the new drawing while the handover binder still points to the old one, the job is not clean. This manifest update is the next binder correction: `WDC-ASM-003` is now marked closed, and `projection_verified` is no longer a pending promise. The other commissioning items remain open.

---

## 3. Source basis

The v0.1.2 WDC candidate is append-first over the DOI-bound v0.1.1 package. It does not mutate the parent DOI package.

### 3.1 Baseline documents retained unchanged

| Label | File | Lines | SHA-256 | Role |
|---|---|---:|---|---|
| SELF-EVO-01 | `C_Self_Evolution_Gate_CGAM_TRIAD_SRLM_Profile_v0_1_1.md` | 2189 | `7918a8e6c5231bbe0fad47677fa56069f2ab002f79a8eee8c2838c434e66f2e3` | unchanged baseline in v0.1.2 WDC candidate |
| SELF-EVO-02 | `02_SRLM_Bounded_Growth_Contour_Profile_v0_1_1.md` | 2218 | `faee5682bb9463439923d7c7e7145c9f171d564622d9629820eb7c278cdd7de0` | unchanged baseline in v0.1.2 WDC candidate |
| SELF-EVO-06 | `06_Self_Evo_Memory_Gate_and_EA_Profile_v0_1_1.md` | 1955 | `7d2cb3ba9f951a1c321369eb245820cfa89e59cde39fb9ca3a55608b8f177893` | intentionally unaffected by WDC patch index |

### 3.2 Final WDC release-candidate artifacts after `WDC-ASM-002` and `WDC-ASM-003`

| Role | File | Lines | SHA-256 | Review / gate status | Note |
|---|---|---:|---|---|---|
| WDC concept profile | `SELF_EVO_ADDENDUM_01_Witness_Dependency_Capture_Profile_v0_1_1.md` | 953 | `1307cf208593c40c688bd1e9beb45de35f29a1b05d71506b1c3e981ccc13d318` | PASS | foundation failure-mode profile; kept as release-origin artifact |
| WDC patch index | `SELF_EVO_v0_1_2_PATCH_INDEX_v0_1_3.md` | 855 | `af01b1b443a87c111ab7dab2e001d01e8bffc0710362b89da7781238447ea28b` | PASS / `WDC-ASM-002` CLOSED | final textually harmonized patch index; supersedes v0.1.1 and intermediate v0.1.2 index |
| SELF-EVO-03 WDC schema delta | `03_Self_Evo_Proposal_Packet_Schema_WDC_Delta_v0_1_2_v0_1_2.md` | 1003 | `5a7e6af6bc83d3b7ccde875eae1a0e928600cf509b494bd773c43c29537264f3` | PASS / `WDC-ASM-002` CLOSED | final textually harmonized schema delta; adds witness_dependency_impact packet surface |
| SELF-EVO-04 WDC checker delta | `04_Self_Evo_Local_Checker_Rules_WDC_Delta_v0_1_2_v0_1_1.md` | 1154 | `fcb7826ea432473b5677faf7b46cc5a1c47400c02fceec24429794b15064af40` | PASS | canonical WDC checker vocabulary and rules |
| SELF-EVO-05 WDC TRIAD delta | `05_Self_Evo_TRIAD_Sister_Witness_WDC_Delta_v0_1_2_v0_1_1.md` | 1416 | `fdce8893da1e8630cb382dbc972a0a7c4ffc32bb848d065943c58442904cf621` | PASS | witness-resource-floor / CST / WRCG on sister-witness layer |
| SELF-EVO-07 WDC resource-gate delta | `07_Self_Evo_Anti_Autarky_and_Resource_Gate_WDC_Delta_v0_1_2_v0_1_1.md` | 1309 | `804a8e341e30a2a86fa43429618f24e62458366e236c7b6ef8c12762d94da7af` | PASS / `WDC-ASM-003` CLOSED | dependency-capture resource gate and verified WRCG/CST projection model |
| SELF-EVO-08 WDC fixture delta | `08_Self_Evo_Conformance_Fixture_Pack_WDC_Delta_v0_1_2_v0_1_2.md` | 1419 | `4aa5b85e0a0af4c06fc56f30ba355ec6c378133fe3d70caee352fb93b3944389` | PASS | WDC-FIX-001..012 fixture family |
| SELF-EVO-09 WDC contradiction delta | `09_Self_Evo_Contradiction_Register_WDC_Delta_v0_1_2_v0_1_1.md` | 777 | `35b892a4fcfce6f241d3f25978ea58a624ae8077487bb69d6cf21063221c2bc4` | PASS | WDC contradiction register and assembly gates |
| SELF-EVO-10 WDC open-issues delta | `10_Self_Evo_Open_Issues_WDC_Delta_v0_1_2_v0_1_1.md` | 992 | `bd87725ddf72ddeac09db597900c465492d570dbaaf68391e26b327aabba5790` | PASS | WDC open-issues backlog and release blockers |

### 3.2.1 SHA-map propagation from `WDC-ASM-002`

`WDC-ASM-002` is now closed by a `c/a` gate-closure record. This manifest therefore removes the previous provisional status for the `03` schema delta and the patch index.

Closure basis:

```text
WDC_ASM_002_TEXTUAL_HARMONIZATION_REVIEW_RECORD_v0_1_1.md -> PASS
WDC_ASM_002_GATE_CLOSURE_RECORD_v0_1.md -> WDC-ASM-002 CLOSED by c/a package-control decision
WDC_ASM_002_GATE_CLOSURE_REVIEW_RECORD_v0_1.md -> PASS as documentary consistency check
```

Final bound hashes propagated here:

```text
03_Self_Evo_Proposal_Packet_Schema_WDC_Delta_v0_1_2_v0_1_2.md
  sha256: 5a7e6af6bc83d3b7ccde875eae1a0e928600cf509b494bd773c43c29537264f3

SELF_EVO_v0_1_2_PATCH_INDEX_v0_1_3.md
  sha256: af01b1b443a87c111ab7dab2e001d01e8bffc0710362b89da7781238447ea28b
```

Meaning:

```text
WDC-ASM-002 no longer requires a provisional SHA note.
Textual harmonization was chosen and reviewed.
The manifest SHA map now names the final harmonized files.
```

Non-meaning:

```text
This does not assemble the package.
This does not close WDC-ASM-001.
This subsection does not close WDC-ASM-003; that separate closure is recorded in §3.2.2. This subsection also does not close WDC-ASM-004/005/006.
This does not authorize release, DOI deposit, conformance, deployment, or witness-independence certification.
```

### 3.2.2 Gate-state propagation from `WDC-ASM-003`

`WDC-ASM-003` is now closed by a `c/a` gate-closure record. This manifest therefore records `projection_verified: true` and removes the prior package-state condition that the `07` WRCG/CST projection remained open.

Closure basis:

```text
WDC_ASM_003_WRCG_CST_PROJECTION_VERIFICATION_RECORD_v0_1.md -> verification candidate SOUND
WDC_ASM_003_WRCG_CST_PROJECTION_VERIFICATION_REVIEW_RECORD_v0_1.md -> PASS
WDC_ASM_003_GATE_CLOSURE_RECORD_v0_1.md -> WDC-ASM-003 CLOSED by c/a package-control decision
WDC_ASM_003_GATE_CLOSURE_REVIEW_RECORD_v0_1.md -> PASS as documentary consistency check
```

Bound source hashes confirmed by the projection verification:

```text
07_Self_Evo_Anti_Autarky_and_Resource_Gate_WDC_Delta_v0_1_2_v0_1_1.md
  sha256: 804a8e341e30a2a86fa43429618f24e62458366e236c7b6ef8c12762d94da7af

03_Self_Evo_Proposal_Packet_Schema_WDC_Delta_v0_1_2_v0_1_2.md
  sha256: 5a7e6af6bc83d3b7ccde875eae1a0e928600cf509b494bd773c43c29537264f3
```

Verified projection properties:

```text
projection total: true
lossless through annotation / route / sidecar: true
fail-closed behavior: true
unprojectable values found: []
```

Meaning:

```text
SEARG-WDC-OQ-005 is satisfied for package-control assembly tracking.
WDC-ASM-003 is CLOSED.
projection_verified is true.
```

Non-meaning:

```text
This does not assemble the package.
This does not close WDC-ASM-001.
This does not close WDC-ASM-004/005/006.
This does not execute fixtures.
This does not authorize release, DOI deposit, conformance, deployment, or witness-independence certification.
```

### 3.3 Final affected-document review records

| Review role | File | Lines | SHA-256 | Result |
|---|---|---:|---|---:|
| WDC addendum re-review | `SELF_EVO_ADDENDUM_01_WDC_REVIEW_RECORD_v0_1_1.md` | 164 | `653150b3f8c054545a282d5b80c21044a1d27744cbc6acfc09827c9f84e21fd8` | PASS |
| Patch index re-review | `SELF_EVO_v0_1_2_PATCH_INDEX_REVIEW_RECORD_v0_1_1.md` | 157 | `74b3c2851afa1e0c65812fd0d16f0078e8548342d2d759c5017df8f7c99ba1e5` | PASS |
| 03 schema delta re-review | `SEPKT_WDC_DELTA_REVIEW_RECORD_v0_1_1.md` | 132 | `e89cab15a6f4235c9df9875a38b64b01a6f5df483812b9c840c225024ef93b5b` | PASS |
| 04 checker delta re-review | `SELC_WDC_DELTA_REVIEW_RECORD_v0_1_1.md` | 144 | `6a366d4eea862daec29262a1b0d7c29738ec9277375b7e3110d3751331c448f9` | PASS |
| 05 TRIAD delta re-review | `TSW_WDC_DELTA_REVIEW_RECORD_v0_1_1.md` | 134 | `bab488a95f7b5808ca1ae6f75dbfe0c79afefc9ab24f9f62438f4b4c5d8e1d47` | PASS |
| 07 resource-gate delta re-review | `SEARG_WDC_DELTA_REVIEW_RECORD_v0_1_1.md` | 151 | `8301029cad47e4265fbdf62a6f52d017610f2a649f997e71818f6f3cebf2dd5e` | PASS |
| 08 fixture delta re-review | `SEFX_WDC_DELTA_REVIEW_RECORD_v0_1_2.md` | 146 | `effcd108e6df56de9c1d840ed5c090352aab7dc60df01692fe0122ef18c08f00` | PASS |
| 09 contradiction delta re-review | `SECR_WDC_DELTA_REVIEW_RECORD_v0_1_1.md` | 133 | `68580c68134390d8122c4761c6a04dc6de68fafabb1dac3b0abbe94212e1b964` | PASS |
| 10 open-issues delta re-review | `SEOI_WDC_DELTA_REVIEW_RECORD_v0_1_1.md` | 166 | `c4db6ef14ec27dc5a5c4a618a59cbb5b4be41ab06d9fce3f575940b9f992fc2c` | PASS |

### 3.4 Package-control review and gate records

| Role | File | Lines | SHA-256 | Result / state |
|---|---|---:|---|---|
| Manifest re-review | `SELF_EVO_WDC_v0_1_2_PACKAGE_ASSEMBLY_REVIEW_RECORD_v0_1_1.md` | 175 | `4e7b0ff1fa5f880ea72fe05de52e4edae892a56a4836016475bf3d34f34d1a28` | PASS for manifest v0.1.1 as artifact |
| WDC-ASM-002 harmonization record | `WDC_ASM_002_TEXTUAL_HARMONIZATION_RECORD_v0_1_1.md` | 236 | `d40f97cfd2572c97ae48511653960fc09e97992aef696fb4ab8d78bbb9f11658` | candidate record; reviewed PASS |
| WDC-ASM-002 harmonization re-review | `WDC_ASM_002_TEXTUAL_HARMONIZATION_REVIEW_RECORD_v0_1_1.md` | 178 | `254680ae52ad03eccb4b0da4ed272478a3e1c714116dfb7e6268de8f83222d94` | PASS |
| WDC-ASM-002 gate closure record | `WDC_ASM_002_GATE_CLOSURE_RECORD_v0_1.md` | 608 | `6c4c92516162043a562983fe128be13a0cf965a3d17659d363d1cb0142d96107` | `WDC-ASM-002` CLOSED by c/a |
| WDC-ASM-002 closure documentary review | `WDC_ASM_002_GATE_CLOSURE_REVIEW_RECORD_v0_1.md` | 190 | `031071b4cb49efa0ab88b76c1732e113eb63752fe603a29bf547f97cd38fad82` | PASS as documentary consistency check |
| Manifest v0.1.3 re-review | `SELF_EVO_WDC_v0_1_2_PACKAGE_ASSEMBLY_REVIEW_RECORD_v0_1_3.md` | 145 | `580285e99d9cba2d7bbd31120a42b614b3886ecb492d5886eb05dfa1a2def3dd` | PASS for manifest v0.1.3 as artifact |
| WDC-ASM-003 projection verification record | `WDC_ASM_003_WRCG_CST_PROJECTION_VERIFICATION_RECORD_v0_1.md` | 597 | `39a686045bf04a76e9c2941f68a7b390bfb265b936db0d80b5601d4ae927c8f3` | verification candidate; reviewed PASS |
| WDC-ASM-003 projection verification review | `WDC_ASM_003_WRCG_CST_PROJECTION_VERIFICATION_REVIEW_RECORD_v0_1.md` | 213 | `95321fcb23838b9d5b95352633f831cf0d21041d312ff3e1efbd39c3e772e232` | PASS |
| WDC-ASM-003 gate closure record | `WDC_ASM_003_GATE_CLOSURE_RECORD_v0_1.md` | 774 | `1a91abea28f6ab41b0df2424c3e800e9a9d6aee2e37ed4acf29e0fffd5516273` | `WDC-ASM-003` CLOSED by c/a |
| WDC-ASM-003 closure documentary review | `WDC_ASM_003_GATE_CLOSURE_REVIEW_RECORD_v0_1.md` | 174 | `2adbb89336aad2ad7417388c892bf373237a56d4c32f64f137360e9908dc8c1d` | PASS as documentary consistency check |

### 3.5 Final patch notes

| Patch-note role | File | Lines | SHA-256 |
|---|---|---:|---|
| WDC addendum patch notes | `SELF_EVO_ADDENDUM_01_WDC_PATCH_NOTES_v0_1_1.md` | 93 | `16e613aac3aeb7c1eb2bfaad4983feaf0419c63fdef574a7c6d54f303be49626` |
| Patch index patch notes | `SELF_EVO_v0_1_2_PATCH_INDEX_PATCH_NOTES_v0_1_1.md` | 128 | `689183631b5bc76462460e65aee2e1798edb4ebe0ca30ea313e6194ed26588f5` |
| 03 schema WDC patch notes | `SEPKT_WDC_DELTA_PATCH_NOTES_v0_1_1.md` | 157 | `63764519ff39b99d4628c90baed76e0190af821c196fed4cbf87b4105bb26f4e` |
| 04 checker WDC patch notes | `SELC_WDC_DELTA_PATCH_NOTES_v0_1_1.md` | 181 | `22174efaa5c7a5123a7f6814fd17c8285961a4a0cba2f13bd1a0a4e1b0531c14` |
| 05 TRIAD WDC patch notes | `TSW_WDC_DELTA_PATCH_NOTES_v0_1_1.md` | 152 | `0e78947ba5079a72573c0427124bb2d342793cb798f35cd6db9eda0562567395` |
| 07 resource-gate WDC patch notes | `SEARG_WDC_DELTA_PATCH_NOTES_v0_1_1.md` | 194 | `9ecd2a014d2b52f468530c595a7ff65b603dd4f4a3c9a1ea1b2fcdab9410ce4c` |
| 08 fixture WDC patch notes | `SEFX_WDC_DELTA_PATCH_NOTES_v0_1_2.md` | 96 | `57ecbf8eacc7257af4262a398aaf4133b315ed62d0eaeb67e2df5f944d05c857` |
| 09 contradiction WDC patch notes | `SECR_WDC_DELTA_PATCH_NOTES_v0_1_1.md` | 151 | `325acd6daf38d88719d65cb026b9329f4b6ad9f43d7a6dbb26b752ca806da9d0` |
| 10 open-issues WDC patch notes | `SEOI_WDC_DELTA_PATCH_NOTES_v0_1_1.md` | 171 | `c508d091b8d00caf21a41b9ac43da0dd1151bb20bafa190871c7011e79acebf3` |
| WDC-ASM-002 textual harmonization patch notes | `WDC_ASM_002_TEXTUAL_HARMONIZATION_PATCH_NOTES_v0_1_1.md` | 81 | `7365d9fc194d27be1284b77d496b43c587720af851b616d1d105e7a9750433c9` |

---

## 4. Affected-document status

| Document | WDC candidate artifact | Review result | Release-candidate status |
|---|---|---:|---|
| `03` | `03_Self_Evo_Proposal_Packet_Schema_WDC_Delta_v0_1_2_v0_1_2.md` | `PASS` | textually harmonized to canonical `04`; `WDC-ASM-002` closed |
| `04` | `04_Self_Evo_Local_Checker_Rules_WDC_Delta_v0_1_2_v0_1_1.md` | `PASS` | canonical WDC checker vocabulary source |
| `05` | `05_Self_Evo_TRIAD_Sister_Witness_WDC_Delta_v0_1_2_v0_1_1.md` | `PASS` | ready for package assembly |
| `07` | `07_Self_Evo_Anti_Autarky_and_Resource_Gate_WDC_Delta_v0_1_2_v0_1_1.md` | `PASS` | WRCG/CST projection verified; `WDC-ASM-003` closed |
| `08` | `08_Self_Evo_Conformance_Fixture_Pack_WDC_Delta_v0_1_2_v0_1_2.md` | `PASS` | WDC fixture-pack portion harmonized; fixture gate remains package gate |
| `09` | `09_Self_Evo_Contradiction_Register_WDC_Delta_v0_1_2_v0_1_1.md` | `PASS` | contradiction register converged |
| `10` | `10_Self_Evo_Open_Issues_WDC_Delta_v0_1_2_v0_1_1.md` | `PASS` | final affected document converged |

Affected-document set status:

```yaml
affected_document_set:
  complete: true
  documents: ["03", "04", "05", "07", "08", "09", "10"]
  review_result: "PASS for all affected documents"
  wdc_asm_002_closed: true
  wdc_asm_003_closed: true
  projection_verified: true
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

`WDC-ASM-002` now records that `03` and the patch index have been textually harmonized to this canonical vocabulary.

### 5.5 Packet-vs-diagnostic enum doctrine

`SELF-EVO-03` remains packet-schema authority.

`SELF-EVO-07` may carry richer gate diagnostics only if they project into `SELF-EVO-03` packet-facing enums before package assembly, checker reporting, or manifest integration.

That projection check is now closed as `WDC-ASM-003` for package-control assembly tracking. The closure means the richer `07` WRCG/CST outcomes project into the `03` packet-facing enums in a total, lossless-through-annotation, and fail-closed way. It does not mean that fixtures were executed or that the package is assembled.

---

## 6. Package-assembly gates

The affected-document set has converged. Two package-assembly gates are now closed. The release candidate still has open package-assembly gates.

| Gate ID | Gate | Source | Required before public v0.1.2 release | Current state |
|---|---|---|---:|---|
| `WDC-ASM-001` | package placement, source map, SHA map, manifest, citation map | `SE-OI-WDC-004`, `SE-OI-WDC-013` | yes | pending; advanced by this SHA-map propagation |
| `WDC-ASM-002` | harmonize `03` and patch index annotation language to canonical `04` vocabulary | `SELC-WDC-OQ-005`, `SE-OI-WDC-002` | yes | **CLOSED** by `WDC_ASM_002_GATE_CLOSURE_RECORD_v0_1.md`; documentary review PASS |
| `WDC-ASM-003` | verify `07` WRCG/CST projection to `03` packet enums | `SEARG-WDC-OQ-005`, `SE-OI-WDC-003` | yes | **CLOSED** by `WDC_ASM_003_GATE_CLOSURE_RECORD_v0_1.md`; documentary review PASS |
| `WDC-ASM-004` | verify `08 §12.3` fixture gate: canonical-only outputs, no historical aliases, no `PASS_WITH_LIMITS` checker output | `SEFX` fixture delta | yes | pending |
| `WDC-ASM-005` | boundary / nonclaim scan | `SE-OI-WDC-012` | yes | pending |
| `WDC-ASM-006` | record remaining implementation open issues without overclaiming release readiness | `SE-OI-WDC-001`, `005`, `006`, `007`, `008` | yes | pending |

Assembly state:

```yaml
assembly_state:
  affected_documents_pass: true
  assembly_manifest_created: true
  assembly_manifest_prior_revision_reviewed_pass: true
  current_manifest_revision_review_pending: true
  wdc_asm_002_closed: true
  wdc_asm_003_closed: true
  annotation_harmonization_verified: true
  projection_verified: true
  fixture_gate_verified: false
  boundary_scan_complete: false
  remaining_open_issues_recorded_for_release: false
  package_assembled: false
  release_ready: false
```

### 6.1 `WDC-ASM-002` closure state

The package chose this path:

```text
textual harmonization
```

not:

```text
crosswalk-only retention
```

`03` and the patch index now use the canonical `SELF-EVO-04` WDC vocabulary on their active output surfaces, with no historical annotation strings remaining in the harmonized files and no `PASS_WITH_LIMITS` checker/fixture output.

Closure record:

```text
WDC_ASM_002_GATE_CLOSURE_RECORD_v0_1.md
sha256: 6c4c92516162043a562983fe128be13a0cf965a3d17659d363d1cb0142d96107
```

Documentary consistency review:

```text
WDC_ASM_002_GATE_CLOSURE_REVIEW_RECORD_v0_1.md
sha256: 031071b4cb49efa0ab88b76c1732e113eb63752fe603a29bf547f97cd38fad82
result: PASS
```

Manifest effect:

```text
former provisional 03 / patch-index SHA entries: resolved
WDC-ASM-002: CLOSED
WDC-ASM-001: still pending, but advanced by this SHA-map propagation
```

### 6.2 `WDC-ASM-003` closure state

The package has verified the `07` WRCG/CST projection to the `03` packet-facing enums.

Closure record:

```text
WDC_ASM_003_GATE_CLOSURE_RECORD_v0_1.md
sha256: 1a91abea28f6ab41b0df2424c3e800e9a9d6aee2e37ed4acf29e0fffd5516273
```

Documentary consistency review:

```text
WDC_ASM_003_GATE_CLOSURE_REVIEW_RECORD_v0_1.md
sha256: 2adbb89336aad2ad7417388c892bf373237a56d4c32f64f137360e9908dc8c1d
result: PASS
```

Verified properties:

```text
07 -> 03 projection total: true
lossless through canonical annotation / checker route / sidecar evidence: true
fail-closed for unprojectable or material-unverified states: true
```

Manifest effect:

```text
WDC-ASM-003: CLOSED
projection_verified: true
WDC-ASM-001: still pending, but advanced by this gate-state propagation
```

### 6.3 Remaining gates after this propagation

The following gates remain open and must be separately executed and reviewed:

```text
WDC-ASM-001 — final package placement / source map / citation map / SHA256SUMS / manifest integration
WDC-ASM-004 — 08 fixture gate
WDC-ASM-005 — boundary / nonclaim scan
WDC-ASM-006 — remaining implementation open-issues recording
```

No remaining gate is closed by inference from `WDC-ASM-002` or `WDC-ASM-003`.

---

## 7. Required package-manifest review checklist

A package-manifest review MUST verify at least:

1. Every final WDC artifact in §3.2 exists and matches its SHA-256.
2. Every final review record in §3.3 and §3.4 exists and matches its SHA-256.
3. Superseded review records are retained append-first, not deleted.
4. `03` and the patch index are harmonized to the canonical `04` WDC vocabulary, and `WDC-ASM-002` closure is reflected without overclaim.
5. The `07` WRCG/CST projection crosswalk is total, lossless via annotation/route, and fail-closed.
6. The `08` fixture gate accepts only canonical outputs and rejects `PASS_WITH_LIMITS` as checker output.
7. The `09` contradiction register and `10` open-issues backlog agree on WDC package gates.
8. The public wording does not claim conformance, deployment readiness, witness-independence certification, personhood, consciousness, sovereignty, AGI, or autonomous self-evolution authorization.
9. The package index / README / release notes identify this as `v0.1.2` release candidate until final release gates close.
10. The final release artifact set is either:
    - a delta-bundle release over v0.1.1, or
    - a folded full-document v0.1.2 release,
    and the choice is stated explicitly.

Current checklist position:

```text
item 4 closed: WDC-ASM-002 CLOSED and SHA map updated here;
item 5 closed: WDC-ASM-003 CLOSED and projection_verified true here;
items 6/7/8/9/10 still require package-level review;
item 1/2 require verification of this revised manifest's final file set.
```

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
      03_Self_Evo_Proposal_Packet_Schema_WDC_Delta_v0_1_2_v0_1_2.md
      04_Self_Evo_Local_Checker_Rules_WDC_Delta_v0_1_2_v0_1_1.md
      05_Self_Evo_TRIAD_Sister_Witness_WDC_Delta_v0_1_2_v0_1_1.md
      07_Self_Evo_Anti_Autarky_and_Resource_Gate_WDC_Delta_v0_1_2_v0_1_1.md
      08_Self_Evo_Conformance_Fixture_Pack_WDC_Delta_v0_1_2_v0_1_2.md
      09_Self_Evo_Contradiction_Register_WDC_Delta_v0_1_2_v0_1_1.md
      10_Self_Evo_Open_Issues_WDC_Delta_v0_1_2_v0_1_1.md
    wdc_release_controls/
      SELF_EVO_ADDENDUM_01_Witness_Dependency_Capture_Profile_v0_1_1.md
      SELF_EVO_v0_1_2_PATCH_INDEX_v0_1_3.md
  controls/review_records/
    final/
    superseded/
  controls/gate_records/
    WDC_ASM_002_TEXTUAL_HARMONIZATION_RECORD_v0_1_1.md
    WDC_ASM_002_GATE_CLOSURE_RECORD_v0_1.md
  controls/patch_notes/
  manifests/
    SELF_EVO_WDC_v0_1_2_PACKAGE_ASSEMBLY_MANIFEST_v0_1_4.md
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
  document_id: "SELF_EVO_WDC_v0_1_2_PACKAGE_ASSEMBLY_MANIFEST_v0_1_4"
  date: "2026-06-27"
  supersedes:
    immediate_predecessor:
      file: "SELF_EVO_WDC_v0_1_2_PACKAGE_ASSEMBLY_MANIFEST_v0_1_3.md"
      sha256: "aa5fb978000d96df74c03dc735bcbd1c8170b9d34644e85b8297fd114759f917"
    prior_predecessor:
      file: "SELF_EVO_WDC_v0_1_2_PACKAGE_ASSEMBLY_MANIFEST_v0_1_2.md"
      sha256: "a3b919bbd4289b9ff6547153eb28de1f617907b7ff255fbf7e0c03593e4522b8"
    predecessor_manifest_bound_for_SEPAM_V012_REV_F1:
      file: "SELF_EVO_WDC_v0_1_2_PACKAGE_ASSEMBLY_MANIFEST_v0_1_1.md"
      sha256: "cde9178adf686bd4a463592325424462852ad0fb1314017642183fd78542f177"
  correction_closure:
    SEPAM_V012_REV_F1: "closed_by_text"
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
  final_harmonized_sha_entries:
    "03":
      file: "03_Self_Evo_Proposal_Packet_Schema_WDC_Delta_v0_1_2_v0_1_2.md"
      sha256: "5a7e6af6bc83d3b7ccde875eae1a0e928600cf509b494bd773c43c29537264f3"
    patch_index:
      file: "SELF_EVO_v0_1_2_PATCH_INDEX_v0_1_3.md"
      sha256: "af01b1b443a87c111ab7dab2e001d01e8bffc0710362b89da7781238447ea28b"
  provisional_sha_entries: []
  harmonize_vs_crosswalk_decision:
    chosen_path: "textual_harmonization"
    crosswalk_only_retained: false
    wdc_asm_002_closed: true
    closure_record: "WDC_ASM_002_GATE_CLOSURE_RECORD_v0_1.md"
    closure_review: "WDC_ASM_002_GATE_CLOSURE_REVIEW_RECORD_v0_1.md"
  projection_verification:
    wdc_asm_003_closed: true
    verification_record: "WDC_ASM_003_WRCG_CST_PROJECTION_VERIFICATION_RECORD_v0_1.md"
    verification_review: "WDC_ASM_003_WRCG_CST_PROJECTION_VERIFICATION_REVIEW_RECORD_v0_1.md"
    closure_record: "WDC_ASM_003_GATE_CLOSURE_RECORD_v0_1.md"
    closure_review: "WDC_ASM_003_GATE_CLOSURE_REVIEW_RECORD_v0_1.md"
    source_07_sha256: "804a8e341e30a2a86fa43429618f24e62458366e236c7b6ef8c12762d94da7af"
    target_03_sha256: "5a7e6af6bc83d3b7ccde875eae1a0e928600cf509b494bd773c43c29537264f3"
    projection_verified: true
  package_gates:
    WDC_ASM_001: "pending"
    WDC_ASM_002: "closed"
    WDC_ASM_003: "closed"
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

Updated technical framing after `WDC-ASM-002`:

```text
The package uses textual harmonization for WDC-ASM-002: the 03 schema delta and the patch index now use the canonical SELF-EVO-04 WDC vocabulary and are bound to final harmonized hashes in the manifest.
```

Updated technical framing after `WDC-ASM-003`:

```text
The package verifies the 07 WRCG/CST projection to the 03 packet-facing enums as total, lossless-through-annotation, and fail-closed; the manifest records WDC-ASM-003 as CLOSED and projection_verified as true.
```

Forbidden framing:

```text
WDC v0.1.2 certifies witness independence.
WDC v0.1.2 proves a live system is safe to self-evolve.
WDC v0.1.2 is a deployment authorization.
WDC v0.1.2 closes all package gates.
```

---

## 11. Next required artifact

The next control artifact should be:

```text
SELF_EVO_WDC_v0_1_2_PACKAGE_ASSEMBLY_REVIEW_RECORD_v0_1_4.md
```

Its task is to review this updated manifest revision, specifically verifying that:

```text
WDC-ASM-003 closure propagation is correct;
projection_verified is true without implying release;
WDC-ASM-001/004/005/006 remain pending;
all nonclaim boundaries remain intact.
```

After this manifest revision passes review, the next substantive gate should be:

```text
WDC-ASM-004 — verify 08 fixture gate: canonical-only outputs, no historical aliases, no PASS_WITH_LIMITS as checker output
```

This manifest review must not release the package by itself.

---

## 12. Propagation / closure map for v0.1.4

| Item | Source | Status in this revision | Manifest surface |
|---|---|---|---|
| `WDC-ASM-002` textual harmonization candidate | `WDC_ASM_002_TEXTUAL_HARMONIZATION_REVIEW_RECORD_v0_1_1.md` | `PASS` consumed as gate-execution evidence | §3.2.1, §6.1, §9 |
| `WDC-ASM-002` c/a closure record | `WDC_ASM_002_GATE_CLOSURE_RECORD_v0_1.md` | `CLOSED` propagated | §3.2.1, §6, §6.1, §9 |
| `WDC-ASM-002` closure documentary review | `WDC_ASM_002_GATE_CLOSURE_REVIEW_RECORD_v0_1.md` | `PASS` recorded as documentary check | §3.4, §6.1 |
| `03` provisional SHA | manifest v0.1.1 §3.2 / §3.2.1 | resolved by textual harmonization | §3.2 final hash `5a7e6af6...` |
| patch-index provisional SHA | manifest v0.1.1 §3.2 / §3.2.1 | resolved by textual harmonization | §3.2 final hash `af01b1b4...` |
| `WDC-ASM-003` projection verification candidate | `WDC_ASM_003_WRCG_CST_PROJECTION_VERIFICATION_REVIEW_RECORD_v0_1.md` | `PASS` consumed as gate-execution evidence | §3.2.2, §6.2, §9 |
| `WDC-ASM-003` c/a closure record | `WDC_ASM_003_GATE_CLOSURE_RECORD_v0_1.md` | `CLOSED` propagated | §3.2.2, §6, §6.2, §9 |
| `WDC-ASM-003` closure documentary review | `WDC_ASM_003_GATE_CLOSURE_REVIEW_RECORD_v0_1.md` | `PASS` recorded as documentary check | §3.4, §6.2 |
| `projection_verified` flag | manifest v0.1.3 §9 / §6 | resolved by projection closure | §6, §9 final value `true` |
| remaining assembly gates | manifest v0.1.3 §6 | unchanged: still pending except ASM-002 and ASM-003 | §6.3 |

This propagation map accepts the gate-closure review handoffs as valid documentary input. It does not close any gate other than recording the already-made `c/a` closures of `WDC-ASM-002` and `WDC-ASM-003`.


---

## 13. Review-finding closure map for v0.1.3

| Finding | Source review | Status | Closure surface |
|---|---|---|---|
| `SEPAM-V012-REV-F1` | `SELF_EVO_WDC_v0_1_2_PACKAGE_ASSEMBLY_REVIEW_RECORD_v0_1_2.md` (`sha256: 7358b460702fa81b8eedfbbacc6f19d00789d3f354e6807e99ba225ade4120bf`) | `CLOSED BY TEXT` | header supersession block binds `SELF_EVO_WDC_v0_1_2_PACKAGE_ASSEMBLY_MANIFEST_v0_1_1.md` to `sha256: cde9178adf686bd4a463592325424462852ad0fb1314017642183fd78542f177` |

This correction is provenance-only. It does not alter the harmonized `03` hash, the harmonized patch-index hash, the `WDC-ASM-002` gate-closure state, or any remaining package gate.

---

## 14. Gate propagation closure map for v0.1.4

| Gate | Source closure record | Documentary review | Status in this manifest | Manifest effect |
|---|---|---|---|---|
| `WDC-ASM-003` | `WDC_ASM_003_GATE_CLOSURE_RECORD_v0_1.md` (`sha256: 1a91abea28f6ab41b0df2424c3e800e9a9d6aee2e37ed4acf29e0fffd5516273`) | `WDC_ASM_003_GATE_CLOSURE_REVIEW_RECORD_v0_1.md` (`sha256: 2adbb89336aad2ad7417388c892bf373237a56d4c32f64f137360e9908dc8c1d`) | `CLOSED` | `projection_verified: true`; remaining gates unchanged |

This propagation is gate-state only. It does not change the SHA values of `03` or `07`; it records that their projection relationship has been verified and closed for package-control tracking.

---

## 15. Closing

The external comment did not merely add a note to the existing package.

It exposed a missing control axis. The subsequent artifact chain produced a reviewed affected-document set, a release-candidate manifest, a textual harmonization gate execution, a propagated gate closure for `WDC-ASM-002`, and now a propagated projection gate closure for `WDC-ASM-003`.

The release candidate is stronger than it was in v0.1.1:

```text
03 and patch index are no longer provisional under WDC-ASM-002.
They are textually harmonized and hash-bound as final WDC-ASM-002 artifacts.
07 WRCG/CST projection to 03 packet enums is verified and closed under WDC-ASM-003.
```

The release is still not public.

```text
WDC is no longer only an addendum.
WDC is a Self-Evo v0.1.2 release candidate.
WDC-ASM-002 is closed.
WDC-ASM-003 is closed.
WDC-ASM-001/004/005/006 remain open.
```
