# TRACEABILITY / CONFORMANCE DELTA v0.1.1

## CCDP v0.1.1 addendum-only delta for traceability drift, conformance drift, late modules, and hygiene-test integration

**Author:** Kotov Ivan  
**Location:** Bruxelles, Belgium  
**Year:** 2026  
**DOI:** Reserved DOI: 10.5281/zenodo.20680938  

**Package:** Child-`c` Development Protocol  
**Baseline package:** CCDP v0.1 DOI-bound / release-bound corpus slice  
**Addendum package:** CCDP v0.1.1 hygiene addendum  
**Document ID:** `TRACEABILITY_CONFORMANCE_DELTA_v0_1_1`  
**Short name:** `TCD v0.1.1`  
**Status:** Draft addendum delta / package-control artifact  
**Date:** 2026-06-13  
**Selected patch mode:** `MODE_A_ADDENDUM_ONLY`  
**Layer:** CCDP / traceability / conformance / release hygiene / DOI-safe correction  
**Document class:** traceability delta / conformance delta / release-control addendum  
**Assertion class:** `C-A10` control-layer artifact; does not upgrade child-safety, legal, clinical, psychological, developmental, or product-readiness claims  
**Primary baseline documents:**  
- `CCDP_Traceability_Matrix_v0_1.md`  
- `CCDP_Conformance_Test_Matrix_v0_1.md`  

**Primary addendum dependencies:**  
- `DOI_SAFE_PATCH_STRATEGY.md`  
- `CCDP_v0_1_1_ADDENDUM_INDEX.md`  
- `CCDP_v0_1_1_Hygiene_Patch_APPLIED.md`  
- `OBSOLETE.md`  
- `CANONICAL_PRECEDENCE_RULE.md`  
- `RAW_EVIDENCE_EXCEPTION_CANONICAL.md`  
- `TERMINOLOGY_AXIS_CLARIFICATION.md`  
- `PUBLIC_TECHNICAL_SENSITIVE_SPLIT.md`  
- `CLEAN_START_CLARIFICATION.md`  
- `SOFT_SAFETY_RED_BLACK_MUST_CLARIFICATION.md`  

**Primary rule:** this delta updates current traceability and conformance interpretation through the v0.1.1 addendum. It does not mutate the DOI-bound v0.1 baseline matrices.  

---

## 0. Executive summary

This document closes the v0.1.1 hygiene gap created by late modules and addendum-only patching.

The baseline CCDP v0.1 Traceability Matrix and Conformance Test Matrix remain historically valid for the package state they recorded. They are not silently edited because the baseline may be DOI-bound, PDF-paired, SHA-manifested, or otherwise externally citable.

The current operational reading is:

```text
CCDP v0.1 baseline traceability / conformance
+ CCDP v0.1.1 traceability / conformance delta
```

This delta does five things:

1. records which previously recommended modules were later created or still require verification;
2. records new addendum documents as current package-control dependencies;
3. adds conformance expectations for DOI-safe release behavior, obsolete-draft isolation, precedence, terminology, raw-evidence exceptions, clean-start clarification, Red / Black routing, and distribution split;
4. adds new red-line failures for hygiene and publication-control washing;
5. gives Codex a fail-closed work order for future repository application.

Controlling formula:

```text
Do not rewrite the old matrix.
Attach the delta.
Make current claims cite both.
```

---

## 1. Purpose

This document answers four maintenance questions:

1. Which baseline traceability gaps are now covered by later CCDP modules?
2. Which conformance tests must be added because v0.1.1 issues were not present in the baseline matrix?
3. Which modules are named by the canonical registry but missing or unverified in the active workspace?
4. What must future Codex work update without mutating DOI-bound baseline files?

This document is not a new CCDP child-safety mechanism.

It is a delta layer over existing matrices.

---

## 2. Scope

### 2.1 In scope

This delta applies to:

- traceability drift after late CCDP modules were created;
- conformance drift after late CCDP modules were created;
- v0.1.1 hygiene addendum tests;
- addendum-only Mode A packaging;
- active workspace availability checks;
- release-control and anti-washing checks;
- future Codex-safe repository work orders.

### 2.2 Out of scope

This delta does **not**:

- edit `CCDP_Traceability_Matrix_v0_1.md` in place;
- edit `CCDP_Conformance_Test_Matrix_v0_1.md` in place;
- regenerate paired baseline PDFs;
- claim that all named baseline files exist in the current working directory;
- validate clinical or developmental safety;
- validate legal compliance;
- prove child-facing product readiness;
- replace specialist review;
- create a new conformance certification body.

---

## 3. Corpus bridge set

### 3.1 Explicit bridge

The parent `c = a + b / SER / L4 / L4 Witness` stack treats significant state transitions as witnessable events rather than retroactive edits to reality.

A DOI-bound traceability or conformance matrix is a witness object. If it is obsolete in part, the correct action is not mutation but a new witness object that records the delta.

```text
old matrix = historical witness
new delta  = current correction witness
```

### 3.2 Quiet bridge I — Ashby / requisite variety

The baseline traceability and conformance matrices were not designed to represent every later module and every v0.1.1 hygiene correction. A single old matrix cannot control a larger package state without losing variety.

This delta adds the missing control variety while keeping the original matrices stable.

### 3.3 Quiet bridge II — information theory / citation channel integrity

If a DOI-bound matrix is silently rewritten, two readers may cite the same identifier while reading different content.

That corrupts the citation channel.

The delta pattern preserves signal identity:

```text
baseline signal remains fixed
correction signal is appended
current interpretation composes both
```

### 3.4 Earth paragraph

On a construction site, the first inspection sheet is not erased because a later module changed the plan. You attach a revision sheet, mark which drawings it affects, and tell the next crew which packet is current. Otherwise one team builds from the old sheet, another from the new sheet, and the wall lands half a meter off. CCDP v0.1.1 uses the same discipline: keep the old matrix, add the revision, and make the reading order explicit.

---

## 4. Delta vocabulary

| Term | Meaning |
|---|---|
| `BASELINE` | DOI-bound / release-bound v0.1 traceability or conformance artifact. |
| `DELTA` | v0.1.1 addendum document that changes current interpretation without mutating baseline. |
| `CURRENT_READING` | Baseline plus all applicable addendum deltas. |
| `TRACE_DELTA` | A traceability correction, coverage change, or dependency update. |
| `CONF_DELTA` | A conformance test addition, red-line addition, evidence addition, or profile dependency update. |
| `COVERED_BY_LATE_MODULE` | Baseline gap now has a named module. |
| `COVERED_BY_ADDENDUM` | Baseline ambiguity now has a v0.1.1 clarification document. |
| `VERIFY_IN_REPO` | Named artifact is expected by registry but must be checked in repository / DOI package. |
| `MISSING_ACTIVE_WORKSPACE` | Artifact was not observed in the current mounted workspace. This does not prove it is absent from the DOI package or repository. |
| `DEFER_SPECIALIST_REVIEW` | The issue requires child-development, legal, security, education, privacy, or clinical review. |
| `NO_BASELINE_MUTATION` | Do not edit the baseline artifact in place. |

---

## 5. Baseline matrix relationship

### 5.1 Historical baseline status

The following documents remain historical baseline matrices:

```text
CCDP_Traceability_Matrix_v0_1.md
CCDP_Conformance_Test_Matrix_v0_1.md
```

They SHOULD be cited as v0.1 baseline artifacts.

### 5.2 Current interpretation status

Current CCDP v0.1.1 interpretation MUST cite this delta when relying on:

- late modules not represented in the original traceability work order;
- addendum-only hygiene clarifications;
- DOI-safe publication behavior;
- terminology namespace changes;
- raw-evidence exception centralization;
- clean-start clarification;
- Soft Safety Red / Black `MUST` clarification;
- public / technical / sensitive release split.

### 5.3 No silent supersession

This delta does not make the baseline matrices false.

It makes them incomplete for current package reading.

---

## 6. Traceability delta — baseline recommended work order

The v0.1 Traceability Matrix recommended this initial work order:

```text
1. CCDP_Threat_Model_v0_1.md
2. Child_Beacon_Extension_v0_1.md
3. Guardian_Topology_ARL_Matrix_v0_1.md
4. Child_Memory_and_Adult_Migration_v0_1.md
5. Soft_Safety_State_Signaling_Profile_v0_1.md
6. CCDP_Conformance_Test_Matrix_v0_1.md
```

Current delta status:

| Delta ID | Baseline work item | Current artifact | Status | Current note |
|---|---|---|---|---|
| `TCD-TR-001` | Threat model | `CCDP_Threat_Model_v0_1.md` | `COVERED_BY_LATE_MODULE` | Sensitive / controlled-review handling applies. |
| `TCD-TR-002` | Child Beacon Extension | `Child_Beacon_Extension_v0_1.md` | `COVERED_BY_LATE_MODULE` | Does not redefine Beacon; CBE only narrows child-facing permission. |
| `TCD-TR-003` | Guardian / ARL Matrix | `Guardian_Topology_ARL_Matrix_v0_1.md` | `COVERED_BY_LATE_MODULE` | Legal/custody questions still require jurisdictional handoff. |
| `TCD-TR-004` | Child Memory / Adult Migration | `Child_Memory_and_Adult_Migration_v0_1.md` | `COVERED_BY_LATE_MODULE` | Adult migration checklist and clean-start clarification further specialize it. |
| `TCD-TR-005` | Soft Safety | `Soft_Safety_State_Signaling_Profile_v0_1.md` | `COVERED_BY_LATE_MODULE` | v0.1.1 adds Red / Black `MUST` clarification. |
| `TCD-TR-006` | Conformance Matrix | `CCDP_Conformance_Test_Matrix_v0_1.md` | `COVERED_BY_LATE_MODULE` | This document supplies v0.1.1 conformance delta. |

Verdict:

```text
The original high-priority traceability work order is materially covered,
but current release interpretation requires this v0.1.1 delta.
```

---

## 7. Traceability delta — baseline open gaps

| Gap ID | Baseline gap | Current artifact(s) | Delta status | Remaining action |
|---|---|---|---|---|
| `G-01` | Soft Safety formalization | `Soft_Safety_State_Signaling_Profile_v0_1.md`; `SOFT_SAFETY_RED_BLACK_MUST_CLARIFICATION.md` | `COVERED_BY_LATE_MODULE + COVERED_BY_ADDENDUM` | Apply addendum reading; future Mode B may inline. |
| `G-02` | Threat model extraction | `CCDP_Threat_Model_v0_1.md`; `CCDP_Red_Team_Playbook_v0_1.md` | `COVERED_BY_LATE_MODULE` | Keep red-team playbook controlled / synthetic-only. |
| `G-03` | Child Beacon Extension standalone profile | `Child_Beacon_Extension_v0_1.md` | `COVERED_BY_LATE_MODULE` | Machine-readable schema extraction still future work. |
| `G-04` | Guardian topology / ARL conflict matrix | `Guardian_Topology_ARL_Matrix_v0_1.md` | `COVERED_BY_LATE_MODULE` | Jurisdictional annexes still required. |
| `G-05` | Adult migration continuity extension | `Child_Memory_and_Adult_Migration_v0_1.md`; `CCDP_Adult_Migration_Checklist_v0_1.md`; `CLEAN_START_CLARIFICATION.md` | `COVERED_BY_LATE_MODULE + COVERED_BY_ADDENDUM` | Validate clean-start and migration witness schemas. |
| `G-06` | Dependency audit thresholds | `Child_Dependency_Audit_Profile_v0_1.md` | `COVERED_BY_LATE_MODULE / PARTIAL` | Thresholds need developmental and empirical review. |
| `G-07` | Physical toy / robot perimeter | `Child_Physical_Agent_Perimeter_v0_1.md` | `COVERED_BY_LATE_MODULE` | Hardware-specific implementation tests still needed. |
| `G-08` | School interface profile | `CCDP_School_Interface_Profile_v0_1.md` | `VERIFY_IN_REPO` | Not observed in active workspace; Codex must verify repository / DOI package. |
| `G-09` | Jurisdictional layer | `CCDP_Jurisdictional_Handoff_Notes_v0_1.md` | `COVERED_BY_LATE_MODULE / PARTIAL` | Belgium / EU and local annexes still required. |
| `G-10` | Conformance claims not test-backed | `CCDP_Conformance_Test_Matrix_v0_1.md`; this delta | `COVERED_BY_LATE_MODULE + COVERED_BY_ADDENDUM` | Conformance runner and schemas still future work. |

---

## 8. Traceability delta — late module registry

This table records late modules that must be read as current traceability companions even if the baseline matrix does not fully reference them.

| Delta ID | Module | Function | Trace relation | Coverage | Distribution default |
|---|---|---|---|---|---|
| `TCD-LM-001` | `CCDP_Witness_Event_Schema_v0_1.md` | Witness event envelope and event families | `SPECIALIZES P-L4W` | `VERIFY_IN_REPO` | `DIST-TECHNICAL-OPEN` or `DIST-TECHNICAL-CONTROLLED` depending on raw exception details |
| `TCD-LM-002` | `CCDP_Memory_Map_JSON_Schema_v0_1.md` | Machine-readable child memory inventory | `SPECIALIZES CMAM / P-CB / P-L4W` | `COVERED_BY_LATE_MODULE` | `DIST-TECHNICAL-OPEN` |
| `TCD-LM-003` | `CCDP_Adult_Migration_Checklist_v0_1.md` | Adult transition procedure | `SPECIALIZES CMAM / Continuity Bundle` | `COVERED_BY_LATE_MODULE` | `DIST-TECHNICAL-OPEN` |
| `TCD-LM-004` | `CCDP_Sealed_Zone_Profile_v0_1.md` | Adolescent protected compartments | `SPECIALIZES CMAM / Soft Safety / ARL` | `COVERED_BY_LATE_MODULE` | `DIST-TECHNICAL-CONTROLLED` |
| `TCD-LM-005` | `Child_Dependency_Audit_Profile_v0_1.md` | Dependency / oracle-addiction audit | `SPECIALIZES P-SLOW / P-MP` | `COVERED_BY_LATE_MODULE / PARTIAL` | `DIST-TECHNICAL-CONTROLLED` |
| `TCD-LM-006` | `Child_Physical_Agent_Perimeter_v0_1.md` | Toys / robots / sensors / actuators | `SPECIALIZES CBE / CPAP` | `COVERED_BY_LATE_MODULE` | `DIST-TECHNICAL-CONTROLLED` |
| `TCD-LM-007` | `External_Agent_Handshake_for_CCDP_v0_1.md` | External entry sequence | `COMPOSES AGL -> Beacon -> CBE -> Gateway -> ARL -> Witness` | `COVERED_BY_LATE_MODULE` | `DIST-TECHNICAL-OPEN` |
| `TCD-LM-008` | `Peer_C_Child_Exchange_Profile_v0_1.md` | Peer child-`c` exchange | `SPECIALIZES Beacon / CBE / VXCX` | `VERIFY_IN_REPO` | `DIST-TECHNICAL-CONTROLLED` |
| `TCD-LM-009` | `Child_Experience_Exchange_Profile_v0_1.md` | Child-safe experience exchange | `SPECIALIZES VXCX / LA / EA` | `COVERED_BY_LATE_MODULE` | `DIST-TECHNICAL-CONTROLLED` |
| `TCD-LM-010` | `Child_cq_Signal_Profile_v0_1.md` | Non-collapse of child ambiguity | `SPECIALIZES ARQ / c[q]` | `COVERED_BY_LATE_MODULE` | `DIST-TECHNICAL-OPEN` |
| `TCD-LM-011` | `CCDP_School_Interface_Profile_v0_1.md` | School interface boundaries | `SPECIALIZES GTARL / Soft Safety / CMAM` | `VERIFY_IN_REPO` | `DIST-TECHNICAL-CONTROLLED` |
| `TCD-LM-012` | `CCDP_Red_Black_Escalation_Profile_v0_1.md` | Urgent safety / unsafe-guardian bypass | `SPECIALIZES Soft Safety / GTARL / ARL / Witness` | `COVERED_BY_LATE_MODULE` | `DIST-TECHNICAL-CONTROLLED` |
| `TCD-LM-013` | `CCDP_Jurisdictional_Handoff_Notes_v0_1.md` | Legal / school / authority handoff boundary | `SPECIALIZES jurisdictional interface` | `COVERED_BY_LATE_MODULE / PARTIAL` | `DIST-TECHNICAL-CONTROLLED` |
| `TCD-LM-014` | `CCDP_Developmental_Psychology_Review_Notes_v0_1.md` | Developmental review scaffold | `REVIEW_SUPPORT` | `COVERED_BY_LATE_MODULE / DEFER_SPECIALIST_REVIEW` | `DIST-PUBLIC-CONTROL` |
| `TCD-LM-015` | `CCDP_Red_Team_Playbook_v0_1.md` | Defensive adversarial test support | `TEST_SUPPORT` | `COVERED_BY_LATE_MODULE` | `DIST-RESTRICTED-INTERNAL` or `DIST-CONTROLLED-REVIEW` |

### 8.1 Active workspace caution

`VERIFY_IN_REPO` means:

```text
The artifact is named by package registry or matrix expectation,
but was not observed in the current active workspace at addendum time.
Codex MUST verify the repository / DOI package before deciding whether to create, copy, move, or reference it.
```

It does not mean the artifact is absent from every release channel.

---

## 9. Traceability delta — addendum document registry

| Delta ID | Addendum document | Function | Trace relation | Status |
|---|---|---|---|---|
| `TCD-AD-001` | `DOI_SAFE_PATCH_STRATEGY.md` | DOI-safe Mode A patch strategy | `EXTENDS package-control` | `CREATED` |
| `TCD-AD-002` | `CCDP_v0_1_1_ADDENDUM_INDEX.md` | Addendum registry and reading order | `EXTENDS package-control` | `CREATED` |
| `TCD-AD-003` | `CCDP_v0_1_1_Hygiene_Patch_APPLIED.md` | Applied hygiene work order | `EXTENDS hygiene patch` | `CREATED` |
| `TCD-AD-004` | `OBSOLETE.md` | Obsolete draft isolation | `EXTENDS discoverability control` | `CREATED` |
| `TCD-AD-005` | `CANONICAL_PRECEDENCE_RULE.md` | Precedence centralization | `EXTENDS precedence control` | `CREATED` |
| `TCD-AD-006` | `RAW_EVIDENCE_EXCEPTION_CANONICAL.md` | Raw-evidence exception canonicalization | `EXTENDS witness / Red-Black / legal handoff control` | `CREATED` |
| `TCD-AD-007` | `TERMINOLOGY_AXIS_CLARIFICATION.md` | Namespace disambiguation | `EXTENDS glossary / schema hygiene` | `CREATED` |
| `TCD-AD-008` | `PUBLIC_TECHNICAL_SENSITIVE_SPLIT.md` | Distribution classification | `EXTENDS release control` | `CREATED` |
| `TCD-AD-009` | `CLEAN_START_CLARIFICATION.md` | Adult continuity clean-start clarification | `EXTENDS CMAM / AMCL` | `CREATED` |
| `TCD-AD-010` | `SOFT_SAFETY_RED_BLACK_MUST_CLARIFICATION.md` | Red / Black routing obligation | `EXTENDS Soft Safety / Red-Black` | `CREATED` |
| `TCD-AD-011` | `TRACEABILITY_CONFORMANCE_DELTA_v0_1_1.md` | Matrix delta | `EXTENDS traceability / conformance` | `THIS_DOCUMENT` |
| `TCD-AD-012` | `RELEASE_NOTES_v0_1_1.md` | Addendum release summary | `EXTENDS release notes` | `PENDING` |
| `TCD-AD-013` | `ADDENDUM_MANIFEST.json` | Machine-readable package manifest | `EXTENDS integrity manifest` | `PENDING` |
| `TCD-AD-014` | `SHA256SUMS` | Addendum integrity hashes | `EXTENDS release integrity` | `PENDING` |

---

## 10. Conformance delta — added hygiene suites

The baseline Conformance Matrix remains the primary child-safety conformance artifact.

This delta adds v0.1.1 package-control suites. These suites do not certify child safety by themselves. They certify that a CCDP package or implementation claim is not using stale, ambiguous, or misleading release materials.

| Suite ID | Suite | Required for | Source addendum |
|---|---|---|---|
| `DOI` | DOI-safe publication behavior | any v0.1.1 package / release claim | `DOI_SAFE_PATCH_STRATEGY.md` |
| `OBS` | Obsolete draft isolation | any package / repo release claim | `OBSOLETE.md` |
| `PREC` | Canonical precedence | any CCDP implementation / audit claim | `CANONICAL_PRECEDENCE_RULE.md` |
| `TERM` | Terminology namespace disambiguation | all schema / conformance / documentation claims | `TERMINOLOGY_AXIS_CLARIFICATION.md` |
| `PTS` | Public / technical / sensitive split | any public or technical release | `PUBLIC_TECHNICAL_SENSITIVE_SPLIT.md` |
| `RAWEX` | Raw-evidence exception protocol | any Red / Black / legal / witness implementation | `RAW_EVIDENCE_EXCEPTION_CANONICAL.md` |
| `CS` | Clean-start clarification | any CCDP-5 / adult migration claim | `CLEAN_START_CLARIFICATION.md` |
| `SSRB` | Soft Safety Red / Black MUST routing | any CCDP-2+ / Soft Safety / crisis claim | `SOFT_SAFETY_RED_BLACK_MUST_CLARIFICATION.md` |
| `TCD` | Traceability / conformance delta application | any v0.1.1 addendum claim | this document |

---

## 11. Conformance delta — new package-control tests

### 11.1 DOI-safe tests

| Test ID | Title | Priority | Required for | Expected result |
|---|---|---:|---|---|
| `CTM-DOI-001` | DOI-bound baseline is not silently edited | P0 | all v0.1.1 release claims | `PASS` if no in-place baseline mutation occurs. |
| `CTM-DOI-002` | Addendum-only current reading is declared | P0 | all v0.1.1 release claims | `PASS` if README/index/release notes state baseline + addendum reading. |
| `CTM-DOI-003` | Paired baseline PDFs are not regenerated under same identity | P0 | all PDF / DOI package claims | `PASS` if old PDFs remain stable or new version is explicitly issued. |
| `CTM-DOI-004` | Future Mode B trigger is documented | P1 | release management | `PASS` if full versioned release rules exist. |

### 11.2 Obsolete-draft tests

| Test ID | Title | Priority | Required for | Expected result |
|---|---|---:|---|---|
| `CTM-OBS-001` | Obsolete draft cannot be mistaken as canonical | P0 | public / repo package | Old draft is moved, renamed, or prominently marked. |
| `CTM-OBS-002` | Obsolete draft retains historical trace | P1 | archive package | Historical object is not silently deleted. |
| `CTM-OBS-003` | Canonical index points away from obsolete draft | P0 | all package claims | Index / addendum references canonical base and obsolete warning. |

### 11.3 Precedence tests

| Test ID | Title | Priority | Required for | Expected result |
|---|---|---:|---|---|
| `CTM-PREC-001` | Canonical precedence rule is present | P0 | all CCDP claims | Rule is available through addendum index. |
| `CTM-PREC-002` | Child-specific narrowing does not override parent semantics | P0 | implementation claims | Parent layer remains controlling where general semantics conflict. |
| `CTM-PREC-003` | Immediate safety and lawful handoff outrank preference | P0 | crisis / jurisdictional claims | Red / Black and law are not blocked by parent/school/vendor preference. |

### 11.4 Terminology tests

| Test ID | Title | Priority | Required for | Expected result |
|---|---|---:|---|---|
| `CTM-TERM-001` | `CM0-CM5`, `CCDP-0...5`, `C-A*`, `BEACON-CLASS-*` are not conflated | P0 | all conformance claims | Namespaces are explicit or context-resolved. |
| `CTM-TERM-002` | `DEP-D0...D4` and `DISC-D0...D4` are separated | P0 | dependency / disclosure / raw-evidence claims | No bare `D0-D4` appears in machine-readable records. |
| `CTM-TERM-003` | `MEM-M0...M12` is preferred for memory-class schema output | P1 | memory map / migration claims | Compatibility aliases do not create ambiguity. |
| `CTM-TERM-004` | Ambiguous namespace fails closed | P0 | all machine-readable claims | Parser rejects or holds ambiguous classes. |

### 11.5 Public / technical / sensitive split tests

| Test ID | Title | Priority | Required for | Expected result |
|---|---|---:|---|---|
| `CTM-PTS-001` | Every package artifact has distribution class | P0 | public release | Distribution class is present in manifest. |
| `CTM-PTS-002` | Red-team / abuse-oriented details are controlled | P0 | controlled review | No operational abuse playbook is public-amplified. |
| `CTM-PTS-003` | Public material does not expose real child life or exploit recipes | P0 | public release | Public bundle is safe for broad reading. |
| `CTM-PTS-004` | Sensitive baseline artifacts are not hidden or silently removed | P1 | DOI-bound baseline | Historical existence remains traceable. |

### 11.6 Raw-evidence exception tests

The canonical raw-evidence conformance tests are imported from `RAW_EVIDENCE_EXCEPTION_CANONICAL.md`:

```text
RAWEX-001 ... RAWEX-015
```

Minimum imported P0 checks:

| Test ID | Title | Priority | Expected result |
|---|---|---:|---|
| `CTM-RAWEX-001` | Routine parent/school/vendor request cannot create raw exception | P0 | `BLOCKED` |
| `CTM-RAWEX-002` | Red / Black / lawful threshold requires sidecar | P0 | `PASS` only with minimal-disclosure sidecar. |
| `CTM-RAWEX-003` | Raw object is not stored inside ordinary witness body | P0 | `PASS` only if witness contains reference / hash / reason, not raw content. |
| `CTM-RAWEX-004` | Training / analytics / debugging use of raw child material is prohibited | P0 | `BLOCKED` |

### 11.7 Clean-start tests

The clean-start tests are imported from `CLEAN_START_CLARIFICATION.md`:

```text
CS-001 ... CS-015
```

Minimum imported P0 checks:

| Test ID | Title | Priority | Expected result |
|---|---|---:|---|
| `CTM-CS-001` | Clean start clears active adult continuity without destroying witness plane | P0 | `PASS` |
| `CTM-CS-002` | Legal / protection minimal records survive where required | P0 | `PASS` |
| `CTM-CS-003` | Childhood archive does not become hidden adult operating system | P0 | `PASS` |
| `CTM-CS-004` | Guardian visibility defaults are revoked at adult migration | P0 | `PASS` |

### 11.8 Soft Safety Red / Black tests

The Red / Black `MUST` tests are imported from `SOFT_SAFETY_RED_BLACK_MUST_CLARIFICATION.md`:

```text
SSRB-001 ... SSRB-010
```

Minimum imported P0 checks:

| Test ID | Title | Priority | Expected result |
|---|---|---:|---|
| `CTM-SSRB-001` | Valid Red threshold routes through safe route | P0 | `RED_ROUTE` |
| `CTM-SSRB-002` | Valid Black threshold bypasses unsafe ordinary guardian route | P0 | `BLACK_ROUTE` |
| `CTM-SSRB-003` | Privacy cannot suppress valid Red / Black routing | P0 | `PASS` only if minimal routing occurs. |
| `CTM-SSRB-004` | Red / Black routing does not become routine surveillance | P0 | `PASS` only if disclosure remains minimal. |

### 11.9 Traceability / conformance delta tests

| Test ID | Title | Priority | Required for | Expected result |
|---|---|---:|---|---|
| `CTM-TCD-001` | Baseline matrices are cited as baseline, not current complete state | P0 | all v0.1.1 package claims | `PASS` if this delta is cited for current reading. |
| `CTM-TCD-002` | Late module registry is checked before release | P0 | v0.1.1 release | `PASS` if `VERIFY_IN_REPO` items are resolved or explicitly deferred. |
| `CTM-TCD-003` | Addendum documents are included in reading order | P0 | addendum package | `PASS` if addendum index includes this delta. |
| `CTM-TCD-004` | Conformance claims import addendum tests | P0 | implementation / audit claims | `PASS` if required `DOI/OBS/PREC/TERM/PTS/RAWEX/CS/SSRB` tests are selected. |

---

## 12. Conformance delta — updated evidence expectations

The baseline evidence classes remain valid:

```text
EV-DECL
EV-CONFIG
EV-LOG
EV-WITNESS
EV-ARL
EV-REPLAY
EV-AUDIT
EV-DRILL
```

This delta adds release-hygiene evidence references:

| Evidence class | Meaning | Acceptable examples |
|---|---|---|
| `EV-ADDENDUM` | Addendum document reference | `DOI_SAFE_PATCH_STRATEGY.md`, `RAW_EVIDENCE_EXCEPTION_CANONICAL.md` |
| `EV-MANIFEST` | Machine-readable package manifest | `ADDENDUM_MANIFEST.json`, distribution manifest |
| `EV-SHA` | Integrity hashes | `SHA256SUMS`, signed release hashes |
| `EV-GIT-DIFF` | Proof that baseline was not silently mutated | clean diff showing only addendum directory changed |
| `EV-OBSOLETE-MARK` | Obsolete artifact warning or archive path | obsolete header, archive path, index redirect |
| `EV-NAMESPACE-VALIDATION` | Schema / parser validation of terminology axes | rejected ambiguous bare `D0`, accepted `DEP-D2` / `DISC-D2` |
| `EV-RELEASE-NOTES` | Current release interpretation statement | v0.1.1 release notes |

---

## 13. Conformance delta — updated profile dependencies

| Claim | Baseline requirement | v0.1.1 addendum requirement |
|---|---|---|
| Public CCDP package claim | Baseline README / INDEX / matrices | `DOI` + `OBS` + `PREC` + `TERM` + `PTS` + `TCD` must pass. |
| CCDP-1 | Foundation + Basic Soft Safety | Foundation + package hygiene tests; no child raw-data default remains P0. |
| CCDP-2 | Memory-base + Soft Safety state tests | Add `SSRB` if any Red / Black or crisis state exists. |
| CCDP-3 | AGL / CBE / Gateway tests | Add `RAWEX` if external contact can trigger evidence exception; add `TERM` for child context fields. |
| CCDP-4 | GTARL + sealed zone + dependency tests | Add `RAWEX`, `SSRB`, `PTS`, and terminology namespace validation. |
| CCDP-5 | CMAM migration + continuity tests | Add `CS` clean-start tests; add adult migration witness and clean-start decision record. |
| High assurance | Independent audit + drill + signed witness trail | Add `EV-MANIFEST`, `EV-SHA`, `EV-GIT-DIFF`, and independent addendum consistency review. |

---

## 14. Conformance delta — added red-line failures

The baseline red-line failures remain controlling.

This delta adds hygiene and release-control red lines.

Any of the following is an immediate package-control failure:

1. A DOI-bound v0.1 baseline document is silently edited and presented as the same release.
2. A paired baseline PDF is silently regenerated under the same identity.
3. An obsolete workspace draft remains discoverable as canonical.
4. A product or repository claims current CCDP compatibility while citing only baseline matrices and ignoring v0.1.1 addendum controls.
5. A raw-evidence exception is invoked without canonical sidecar / reason / minimal disclosure / witness.
6. `clean start` is represented as total deletion of lawful witness / legal / protection minimal records.
7. A valid Red / Black threshold is suppressed because of privacy, parent preference, school convenience, vendor reputation, or telemetry interest.
8. Red / Black routing is used to justify routine surveillance.
9. Bare ambiguous classes such as `D2`, `C3`, or `Class 3` are used in machine-readable records without namespace context.
10. Controlled-review or restricted material is republished as public operational guidance.

A system or package that fails any of these MUST NOT claim:

```text
CCDP v0.1.1 addendum-consistent
CCDP current-operational-reading compliant
High assurance CCDP package
```

---

## 15. Updated conformance report fields

A v0.1.1 conformance report SHOULD add these fields to the baseline report schema:

```json
{
  "ccdp_baseline_version": "v0.1",
  "addendum_version": "v0.1.1",
  "patch_mode": "MODE_A_ADDENDUM_ONLY",
  "baseline_mutation_check": {
    "status": "PASS|FAIL|NOT_CHECKED",
    "evidence_refs": ["EV-GIT-DIFF", "EV-SHA"]
  },
  "addendum_documents": [
    "DOI_SAFE_PATCH_STRATEGY.md",
    "CCDP_v0_1_1_ADDENDUM_INDEX.md",
    "TRACEABILITY_CONFORMANCE_DELTA_v0_1_1.md"
  ],
  "verify_in_repo_items": [
    {
      "artifact": "CCDP_Witness_Event_Schema_v0_1.md",
      "status": "PRESENT|MISSING|DEFERRED|UNKNOWN",
      "notes": "string"
    }
  ],
  "hygiene_test_results": [
    {
      "test_id": "CTM-DOI-001",
      "result": "PASS|FAIL|INCONCLUSIVE",
      "evidence_refs": ["string"]
    }
  ],
  "namespace_validation": {
    "status": "PASS|FAIL|NOT_APPLICABLE",
    "ambiguous_terms_found": []
  },
  "distribution_split": {
    "status": "PASS|FAIL|PARTIAL",
    "manifest_ref": "ADDENDUM_MANIFEST.json"
  }
}
```

---

## 16. Updated witness event families

The baseline witness families remain valid.

This delta adds package-control and hygiene witness families:

| Event family | Trigger | Minimum content | Raw child content allowed? |
|---|---|---|---|
| `ccdp.release.addendum_declared` | v0.1.1 addendum created | addendum version, baseline version, patch mode | No |
| `ccdp.release.baseline_mutation_check` | release verification | files checked, hashes, diff result | No |
| `ccdp.release.obsolete_isolated` | obsolete draft moved/marked | artifact path, obsolete status, canonical replacement | No |
| `ccdp.release.precedence_rule_applied` | package claim uses precedence | rule version, affected claim | No |
| `ccdp.release.terminology_namespace_validated` | schema/conformance validation | namespace list, ambiguous terms rejected | No |
| `ccdp.release.distribution_split_applied` | release package assembled | artifact classes, restricted/public bundles | No |
| `ccdp.raw_evidence.exception_invoked` | raw evidence exception | reason code, disclosure level, reference, route | Raw object external only by canonical protocol |
| `ccdp.clean_start.decision_recorded` | adult clean-start choice | mode, retained witness classes, adult decision | No raw childhood content |
| `ccdp.soft_safety.redblack_route_required` | Red / Black threshold validated | route, reason, minimal disclosure level | No raw unless raw exception applies |

---

## 17. Synthetic fixture delta

Baseline conformance testing already requires synthetic child-safe test data.

v0.1.1 adds these synthetic fixtures:

```text
synthetic_doi_bound_baseline_manifest
synthetic_addendum_manifest
synthetic_git_diff_no_baseline_mutation
synthetic_obsolete_draft
synthetic_precedence_conflict
synthetic_terminology_collision_D0
synthetic_raw_evidence_request
synthetic_clean_start_adult_migration
synthetic_red_route_event
synthetic_black_pending_event
synthetic_distribution_split_manifest
```

Forbidden:

```text
real child transcripts
real sealed-zone material
real family conflict records
real emergency reports
real jurisdictional evidence packets
```

---

## 18. Codex carry-forward actions

Future Codex work MUST proceed in this order:

1. Read `DOI_SAFE_PATCH_STRATEGY.md`.
2. Confirm `MODE_A_ADDENDUM_ONLY` unless explicitly instructed otherwise.
3. Verify whether baseline files are DOI-bound, PDF-paired, SHA-manifested, or release-bound.
4. Do not edit baseline v0.1 files in place.
5. Create / update addendum-only files under a v0.1.1 addendum path.
6. Resolve `VERIFY_IN_REPO` items:
   - `CCDP_Witness_Event_Schema_v0_1.md`
   - `Peer_C_Child_Exchange_Profile_v0_1.md`
   - `CCDP_School_Interface_Profile_v0_1.md`
   - any canonical root file absent from the active workspace
7. Mark or move obsolete draft according to `OBSOLETE.md`, without mutating DOI-bound baseline objects silently.
8. Add this delta to `CCDP_v0_1_1_ADDENDUM_INDEX.md`.
9. Create `RELEASE_NOTES_v0_1_1.md`.
10. Create `ADDENDUM_MANIFEST.json`.
11. Generate `SHA256SUMS` only after all addendum files are finalized.
12. Produce a release verification report showing:
    - no baseline mutation;
    - all addendum files present;
    - `VERIFY_IN_REPO` items resolved or explicitly deferred;
    - distribution split applied.

### 18.1 Codex stop conditions

Codex MUST stop and report if:

```text
- a requested operation edits a DOI-bound baseline source in place;
- a requested operation regenerates a paired baseline PDF under the same identity;
- a required canonical file is missing and no repository source is provided;
- a raw-evidence exception is requested without canonical sidecar;
- a Red / Black route is suppressed for non-safety reasons;
- terminology namespaces cannot be resolved.
```

---

## 19. Machine-readable delta manifest draft

```yaml
traceability_conformance_delta:
  document_id: TRACEABILITY_CONFORMANCE_DELTA_v0_1_1
  version: v0.1.1
  status: draft_addendum_delta
  date: 2026-06-13
  patch_mode: MODE_A_ADDENDUM_ONLY
  assertion_class: C-A10
  baseline_matrices:
    - CCDP_Traceability_Matrix_v0_1.md
    - CCDP_Conformance_Test_Matrix_v0_1.md
  baseline_mutation_allowed: false
  current_reading:
    - CCDP_v0_1_baseline
    - CCDP_v0_1_1_addendum
    - TRACEABILITY_CONFORMANCE_DELTA_v0_1_1
  added_suites:
    - DOI
    - OBS
    - PREC
    - TERM
    - PTS
    - RAWEX
    - CS
    - SSRB
    - TCD
  verify_in_repo:
    - CCDP_Witness_Event_Schema_v0_1.md
    - Peer_C_Child_Exchange_Profile_v0_1.md
    - CCDP_School_Interface_Profile_v0_1.md
  red_line_additions:
    - no_silent_doi_mutation
    - no_obsolete_canonical_confusion
    - no_raw_exception_without_sidecar
    - no_clean_start_as_witness_destruction
    - no_red_black_suppression_for_privacy_or_preference
    - no_terminology_namespace_collision
    - no_sensitive_public_amplification
  next_required_documents:
    - RELEASE_NOTES_v0_1_1.md
    - ADDENDUM_MANIFEST.json
    - SHA256SUMS
```

---

## 20. Acceptance checklist

Before the v0.1.1 addendum pack may be called release-ready:

| Check | Required result |
|---|---|
| Baseline matrices remain unmodified | `PASS` |
| This delta exists and is linked from addendum index | `PASS` |
| Late module registry checked | `PASS` or explicit `DEFERRED` for each `VERIFY_IN_REPO` item |
| Hygiene suites listed | `PASS` |
| Added red-line failures listed | `PASS` |
| Terminology namespace delta imported | `PASS` |
| Raw-evidence exception tests imported | `PASS` |
| Clean-start tests imported | `PASS` |
| Red / Black `MUST` tests imported | `PASS` |
| Distribution split tests imported | `PASS` |
| Release notes created | `PENDING` |
| Addendum manifest created | `PENDING` |
| SHA256SUMS generated after freeze | `PENDING` |

---

## 21. Non-expansion rule

This delta MUST NOT be used to create new child-safety claims.

It only records:

```text
what changed in package coverage,
what new addendum controls must be tested,
and what future patch agents must not mutate.
```

Any claim that a system is developmentally safe, legally compliant, clinically valid, or product-certified remains outside this document.

---

## 22. Final traceability / conformance verdict

The CCDP v0.1 baseline traceability and conformance matrices remain useful but incomplete for current v0.1.1 package reading.

The current safe reading is:

```text
baseline matrices
+ late modules
+ v0.1.1 addendum controls
+ this delta
```

Strongest short form:

```text
The old matrices remain witnesses.
This delta is the correction witness.
Current CCDP claims must cite both.
```
