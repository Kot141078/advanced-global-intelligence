# Self-Evo Open Issues v0.1.1

## Open issues, implementation blockers, release blockers, backlog priorities, and deferred work for the Self-Evo document pack

**Status:** Draft package-control backlog v0.1.1 / append-first corrected revision  
**Date:** 2026-06-25  
**Package:** Self-Evo for `c = a + b` systems  
**Layer:** `c = a + b` / SELF-EVO / CGAM / TRIAD-SYNAPS / SRLM / Memory Gate / EA-L4 / Anti-Autarky / Resource Actor Grounding / Witness / Claim Strength  
**Document class:** open-issues register / implementation backlog / package-readiness artifact  
**Assertion class:** `C-A10` package-control artifact; `C-A7` only where hash-bound source references are used  
**Primary parent:** `09_Self_Evo_Contradiction_Register_v0_1_1.md`  
**Primary boundary:** this file tracks unfinished work. It does not authorize self-evolution, memory promotion, resource acquisition, conformance claims, public release, deployment, checker execution, or live operation.

**Operator note:** the operator reported that repeat review of `09_Self_Evo_Contradiction_Register_v0_1_1.md` confirmed `PASS`. This file treats `09` as accepted for backlog conversion. A separate sealed repeat-review artifact should still be added to the final package manifest if one exists.

**Review / patch note:** `SEOI_REVIEW_RECORD_v0_1.md` reviewed `10_Self_Evo_Open_Issues_v0_1.md` with `PASS_WITH_LIMITS`. This v0.1.1 revision closes `SEOI-REV-F1` by reconciling the issue-ID scheme and closes `SEOI-REV-F2` by labeling the backlog-summary block as a schema template rather than the current numeric summary. `SE-OI-SELF-001` is therefore moved to `PATCHED`; `SE-OI-SELF-004` and `SE-OI-SELF-005` record the two review findings as patched append-first.

---

## 0. Executive summary

This register converts the current open items from `09_Self_Evo_Contradiction_Register_v0_1_1.md` into a fuller backlog with priority, blocking scope, owner, target artifact, required action, and release / implementation implication.

Current state:

```text
SELF-EVO-01..08 exist as corrected v0.1.1 artifacts.
SELF-EVO-09 exists as corrected v0.1.1 and operator-reported PASS after repeat review.
Known open hard contradictions in accepted v0.1.1 documents: 0.
Known red-line failures in accepted v0.1.1 documents: 0.
Implementation artifacts are not yet built.
Conformance fixtures are documented but not yet executed.
Public release is not allowed yet.
Deployment-sensitive use is not allowed yet.
```

Main diagnosis:

```text
The document doctrine is now stable enough to proceed.
The open risks are execution-layer and package-control risks:
schemas, checker, fixture runner, final manifest, release notes,
public/restricted split, source canonicalization, and claim discipline.
```

Compact formula:

```text
Open issues are not a weakness.
They are the list of doors that must stay locked until the key exists.
```

---

## 1. Purpose

The Self-Evo package has reached a new phase.

The previous work produced the main doctrine, specialized profiles, schema profile, checker profile, sister-witness profile, memory/EA profile, resource gate, fixture pack, and contradiction register.

This file answers the next operational question:

```text
What remains unfinished before implementation, conformance, release, or deployment-sensitive use may be claimed?
```

It records:

1. immediate blockers;
2. profile-level open issues;
3. checker and fixture-runner work;
4. schema extraction work;
5. package-control work;
6. public/restricted release work;
7. implementation-readiness prerequisites;
8. deferred legal/security/provider/runtime items;
9. ownership and target artifacts;
10. gate effects.

This file does not add new doctrine. It organizes unfinished work so that future CLI agents, reviewers, and human operators cannot cherry-pick the strongest wording and ignore the unfinished gates.

---

## 2. Scope

### 2.1 In scope

This backlog covers:

| ID | Document | Filename | Lines | SHA-256 | Status for this backlog |
|---|---|---|---:|---|---|
| `SELF-EVO-01` | C-SEG / CGAM-TRIAD-SRLM master gate | `C_Self_Evolution_Gate_CGAM_TRIAD_SRLM_Profile_v0_1_1.md` | 2189 | `7918a8e6c5231bbe0fad47677fa56069f2ab002f79a8eee8c2838c434e66f2e3` | accepted corrected revision |
| `SELF-EVO-02` | SRLM bounded growth contour | `02_SRLM_Bounded_Growth_Contour_Profile_v0_1_1.md` | 2218 | `faee5682bb9463439923d7c7e7145c9f171d564622d9629820eb7c278cdd7de0` | accepted corrected revision |
| `SELF-EVO-03` | Self-evo proposal packet schema | `03_Self_Evo_Proposal_Packet_Schema_v0_1_1.md` | 2642 | `9d329109f0fb97dde7b16b10481baaa60b2aa8f88514e69ec8562a085d10a767` | accepted corrected revision / extraction-ready |
| `SELF-EVO-04` | Self-evo local checker rules | `04_Self_Evo_Local_Checker_Rules_v0_1_1.md` | 2173 | `e5b4b4733199f3391d728c85ad6967f789caf4cba7496db8563c2947e9dc226a` | accepted corrected revision |
| `SELF-EVO-05` | TRIAD sister witness | `05_Self_Evo_TRIAD_Sister_Witness_Profile_v0_1_1.md` | 2145 | `c2761d7a05a91681b336ce5402bdbea5c8fafc2ca0d04fdf2d9667ca02e595ed` | accepted corrected revision |
| `SELF-EVO-06` | Memory Gate and EA | `06_Self_Evo_Memory_Gate_and_EA_Profile_v0_1_1.md` | 1955 | `7d2cb3ba9f951a1c321369eb245820cfa89e59cde39fb9ca3a55608b8f177893` | accepted corrected revision |
| `SELF-EVO-07` | Anti-Autarky and Resource Gate | `07_Self_Evo_Anti_Autarky_and_Resource_Gate_v0_1_1.md` | 1925 | `a26e512282bd6d3a5f12c1852587b513cd6b59880489054ff67a61e68c034c2e` | accepted corrected revision |
| `SELF-EVO-08` | Conformance Fixture Pack | `08_Self_Evo_Conformance_Fixture_Pack_v0_1_1.md` | 1077 | `6c8a67e9270219899624f9ea9c6d5d85c3b6501aa3683e7ddfb1c5345228cf53` | accepted corrected revision / fixture index |
| `SELF-EVO-09` | Contradiction Register | `09_Self_Evo_Contradiction_Register_v0_1_1.md` | 734 | `922f6fb7981c6a0c544d61bce0f29561279dafb7381a90ba9932c445963e8fac` | accepted corrected revision; operator-reported repeat-review PASS |
| `SELF-EVO-10` | Open Issues Register | `10_Self_Evo_Open_Issues_v0_1_1.md` | TBD | TBD | current corrected file; reviewed v0.1 by `SEOI_REVIEW_RECORD_v0_1` |

It also tracks follow-up work from review records and patch notes associated with `SELF-EVO-01..09`.

### 2.2 Out of scope

This backlog does not perform:

1. JSON Schema extraction;
2. checker implementation;
3. fixture runner implementation;
4. conformance execution;
5. public redaction;
6. legal review;
7. security certification;
8. deployment review;
9. runtime SRLM evaluation;
10. SYNAPS implementation;
11. resource-ledger implementation;
12. witness-chain cryptographic sealing.

It tracks those work items.

### 2.3 Non-claim

This file does not claim that the package is:

```text
implemented;
conformance-supported;
deployment-ready;
public-release-ready;
legally reviewed;
security-certified;
capable of live autonomous self-evo;
proof of maturity, personhood, consciousness, AGI, or sovereignty.
```

---

## 3. Corpus bridge set

### 3.1 Explicit bridge: `c = a + b`

In `c = a + b`, the backlog belongs to `b`: documentary control, scheduling, schema targets, checker tasks, release gates, and validation discipline.

It protects `c` by preventing incomplete work from being mistaken for authority.

It is not `a`.
It is not `c`.
It is not a decision to grow.
It is a map of unfinished gates.

### 3.2 Quiet bridge I: information theory

An issue title is a lossy compression of risk.

If a backlog entry compresses away blocking scope, evidence, owner, and target artifact, the backlog becomes noise. This register therefore expands each item into priority, type, status, source, blocking scope, owner, action, and gate effect.

A good issue record preserves enough entropy to be useful later.

### 3.3 Quiet bridge II: cybernetics

A control system without pending-fault memory repeats faults.

The contradiction register records what conflicted. The open-issues register records what still lacks an actuator, validator, witness, or owner. It is negative feedback for the package process.

Without it, the next CLI agent will optimize for visible completion and silently skip the unimplemented gate.

### 3.4 Quiet bridge III: physiology

A healing organism does not forget which tissues remain inflamed just because the major wound was closed. It keeps swelling, tenderness, immune markers, and rest requirements in the loop until repair is stable.

This backlog is that inflammation map for the Self-Evo package. The profiles are stitched. The runner and checker are not yet walking.

### 3.5 Earth paragraph

On a real site, after the drawings pass review, the punch list still matters. The cabinet may be designed correctly, but labels, breakers, test records, lockout tags, cable glands, commissioning signatures, and as-built drawings still need closing. Nobody says “the wiring diagram is coherent, so energize the building.” This file is the punch list before energizing self-evolution.

---

## 4. Classification system

### 4.1 Priority

Priority is scheduling / blocking pressure. It is not the same as severity.

| Priority | Meaning | Typical gate effect |
|---|---|---|
| `P0` | Immediate blocker for next declared transition | blocks schema extraction, checker implementation, fixture runner, package manifest, public release, or conformance claim |
| `P1` | High-priority current-batch issue | required before serious implementation handoff or package-control closure |
| `P2` | Medium-priority maturity / maintainability issue | required for robustness, runtime binding, dashboards, UI, monitoring, or cross-profile completeness |
| `P3` | Future / optional / deferred improvement | valid but not needed for v0.1 document package completion |

### 4.2 Severity

Severity follows `SELF-EVO-09`.

| Severity | Meaning |
|---|---|
| `S0` | Informational / no action needed. |
| `S1` | Minor wording, pointer, or rendering patch. |
| `S2` | Non-blocking package hygiene or future implementation issue. |
| `S3` | Blocks checker-ready, runner-ready, schema extraction, or serious implementation claim. |
| `S4` | Blocks public release, conformance claim, or deployment-sensitive use. |
| `S5` | Critical hard contradiction or red-line failure; stop and quarantine. |

### 4.3 Issue type

| Type | Meaning |
|---|---|
| `SCHEMA` | JSON Schema / object extraction / canonicalization work. |
| `CHECKER` | Deterministic local checker / semantic validator work. |
| `FIXTURE` | Fixture manifest, fixture file, runner, expected-result, coverage, or mismatch work. |
| `PACKAGE` | Manifest, reading order, source map, SHA256SUMS, release notes, patch notes, package index. |
| `REVIEW` | Independent review, re-review, acceptance notes, review-record sealing. |
| `PUBLIC` | Public/restricted split, redaction, nonclaim wording, publication surface. |
| `TRIAD` | Sister witness, SYNAPS, anti-echo, divergence, degraded-triad handling. |
| `SRLM` | SRLM outcome/source/event/replay/promotion/canary/monitoring work. |
| `MEMORY` | Memory Gate, EA, immunity, retention/decay, MG-6, correction/rollback. |
| `RESOURCE` | Resource actor grounding, anti-autarky, resource inventory, human labor, cloud/provider resources. |
| `WITNESS` | Witness event schemas, L4W linkage, evidence refs, hash/canonicalization. |
| `CLAIM` | Claim-strength, anti-overclaiming, maturity/authority/personhood laundering. |
| `SECURITY` | Secrets/cloud/incident/red-line/security-sensitive handling. |
| `LEGAL` | Legal, jurisdictional, counsel/security-certification review. |
| `UI` | Human review cards, dashboard, approval surface, fatigue controls. |
| `RUNTIME` | Real implementation binding: SRLM runtime, SYNAPS runtime, resource ledger, checker runner. |
| `DOC` | Documentation clarity, index, naming, cross-references. |

### 4.4 Status

The register uses the harmonized status vocabulary from `SELF-EVO-09 v0.1.1`.

| Status | Meaning |
|---|---|
| `OPEN` | Not yet fixed. |
| `IN_PROGRESS` | Work started but not yet patched, reviewed, or closed. |
| `PATCHED` | Patch created or review performed, but not fully accepted, sealed, or promoted to final package status. |
| `RESOLVED` | Resolved in accepted revision or final package-control record. |
| `WATCH` | Non-blocking drift risk; monitor during future extraction/implementation. |
| `DEFERRED` | Valid but intentionally postponed. |
| `BLOCKED` | Requires external decision, external review, or unavailable artifact. |
| `WONTFIX` | Explicitly rejected. |
| `ACCEPTED` | Accepted as part of the controlled package state. |

### 4.5 Blocking scope

| Scope | Meaning |
|---|---|
| `doc` | affects wording or profile clarity only. |
| `schema` | blocks schema extraction or schema freeze. |
| `checker` | blocks reference checker implementation or checker-ready claim. |
| `fixture-runner` | blocks fixture runner implementation or runner-ready claim. |
| `conformance` | blocks conformance-supported claim. |
| `manifest` | blocks package manifest / reading order / SHA256SUMS. |
| `public-release` | blocks public release / archive / repository publication. |
| `deployment` | blocks deployment-sensitive use. |
| `runtime` | blocks live runtime binding. |
| `none` | tracked but not blocking current work. |

### 4.6 Issue ID scheme

The canonical open-issue ID scheme does **not** use a year component. Time belongs in `created_at`, review records, patch notes, and witness / manifest metadata.

Allowed issue ID families are:

| Family | Pattern | Use |
|---|---|---|
| Converted contradiction-register issues | `SE-OI-NNN` | Lossless conversion from `SELF-EVO-09` §9. |
| Schema backlog | `SE-SCHEMA-NNN` | JSON Schema, canonicalization, extraction, and schema-index work. |
| Checker backlog | `SE-CHECKER-NNN` | Reference checker and semantic-validator work. |
| Fixture backlog | `SE-FIX-NNN` | Fixture files, fixture runner, expected-result and coverage work. |
| Package-control backlog | `SE-PKG-NNN` | Manifest, reading order, SHA256SUMS, package index, release notes. |
| TRIAD backlog | `SE-TRIAD-NNN` | Sister witness, SYNAPS, anti-echo, divergence and degraded-triad work. |
| SRLM backlog | `SE-SRLM-NNN` | SRLM runtime, outcomes, candidates, replay and promotion work. |
| Memory / EA backlog | `SE-MEM-NNN` | Memory Gate, EA, immunity, decay, MG-6 and correction work. |
| Resource backlog | `SE-RES-NNN` | Anti-autarky, resource actor grounding, resource ledger and human-labor work. |
| Public / legal / security backlog | `SE-PUB-NNN` | Public split, nonclaims, legal/security and redaction work. |
| UI / fatigue backlog | `SE-UX-NNN` | Human approval cards, dashboards, UI and fatigue controls. |
| Review / witness backlog | `SE-REV-NNN` | Review records, acceptance ledger, witness and hash-sealing work. |
| Self-tracking issues | `SE-OI-SELF-NNN` | Issues about this open-issues register itself. |

All of these are open-issue IDs. Domain prefixes are sub-namespaces under the Self-Evo backlog. A processor MUST NOT require `YYYY` inside `issue_id`; the prior `SE-OI-YYYY-NNN` shape is rejected as unused and non-canonical in v0.1.1.

---

## 5. Conversion from `SELF-EVO-09` §9

This section losslessly converts `SE-CR-*` open items from `09_Self_Evo_Contradiction_Register_v0_1_1.md` into `SE-OI-*` backlog records.

| New ID | Source | Priority | Type | Severity | Status | Blocks | Summary | Required action | Owner | Target artifact |
|---|---|---|---|---|---|---|---|---|---|---|
| `SE-OI-001` | `SE-CR-001` | `P0` | `SCHEMA/CHECKER` | `S3` | `OPEN` | `schema`, `checker`, `conformance` | Self-evo JSON Schema extraction and validator implementation are not delivered as executable artifacts. | Create schema extraction plan; extract schemas; build semantic validator. | implementation worker + reviewer | `SELF_EVO_SCHEMA_EXTRACTION_PLAN_v0_1.md`; schema files |
| `SE-OI-002` | `SE-CR-002` | `P0` | `CHECKER` | `S3` | `OPEN` | `checker`, `conformance` | Reference checker implementation for SELC/SEPKT/TSW/SEMG/SEARG is not built or run. | Create reference checker handoff; implement offline checker; produce checker run record. | implementation worker | `SELF_EVO_REFERENCE_CHECKER_IMPLEMENTATION_HANDOFF_v0_1.md` |
| `SE-OI-003` | `SE-CR-003` | `P0` | `FIXTURE` | `S3` | `OPEN` | `fixture-runner`, `conformance` | Fixture runner for SELF-EVO-08 is not implemented; fixtures are documented, not executed. | Implement fixture runner and result records; run fixtures. | implementation worker + tester | fixture runner package |
| `SE-OI-004` | `SE-CR-004` | `P1` | `REVIEW/WITNESS` | `S2` | `OPEN` | `manifest`, `conformance` | Corrected v0.1.1 artifacts are accepted, but acceptance/re-review records must be sealed in final manifest. | Create final review/acceptance ledger with hashes and operator notes. | release manager + human anchor | final package manifest |
| `SE-OI-005` | `SE-CR-005` | `P0` | `PACKAGE` | `S3` | `OPEN` | `manifest`, `public-release`, `conformance` | No final self-evo package manifest, reading order, SHA256SUMS, public/restricted split, or release notes for 01..10 exists. | Build package-control layer after 10. | release manager | package index, reading order, release notes |
| `SE-OI-006` | `SE-CR-006` | `P0` | `PUBLIC/CLAIM` | `S4` | `OPEN` | `public-release`, `deployment` | Public wording and nonclaim boundaries are not separated from private engineering wording. | Create public redaction/nonclaims profile; review restricted content. | release manager + reviewer | `SELF_EVO_PUBLIC_REDACTION_AND_NONCLAIMS_v0_1.md` |
| `SE-OI-007` | `SE-CR-007` | `P1` | `SCHEMA/DOC` | `S2` | `WATCH` | `schema` | Reference composites include redacted source text; they are fine for review but not exact schema extraction. | Use canonical repositories/source files for extraction, not redacted composites. | implementation worker | schema extraction plan |
| `SE-OI-008` | `SE-CR-008` | `P2` | `TRIAD/RUNTIME` | `S2` | `WATCH` | `runtime`, `checker` | TRIAD degraded-mode rules exist, but no runtime SYNAPS witness implementation is included. | Treat sister witness as profile-level until implementation evidence exists; define SYNAPS runtime handoff later. | implementation worker | future SYNAPS implementation profile |
| `SE-OI-009` | `SE-CR-009` | `P1` | `SRLM/RUNTIME` | `S2` | `WATCH` | `runtime`, `conformance` | SRLM implementation evidence exists, but formal tests have not been run in this package context. | Run SRLM tests in controlled package context before runtime claim. | tester + implementation worker | SRLM test report |
| `SE-OI-010` | `SE-CR-010` | `P2` | `RESOURCE/RUNTIME` | `S2` | `WATCH` | `runtime`, `deployment` | Resource gate is documented, but no resource-ledger or actor-grounding runtime object is implemented. | Define resource ledger / grounding record implementation path. | implementation worker | resource-ledger profile/tool |
| `SE-OI-011` | `SE-CR-011` | `P3` | `LEGAL/SECURITY` | `S4` | `DEFERRED` | `deployment`, `public-release` | The pack governs high-risk memory/resource/security boundaries but is not legal advice or security certification. | Require jurisdictional/security review before deployment-sensitive use. | human anchor + qualified reviewer | external legal/security review |
| `SE-OI-012` | `SE-CR-012` | `P1` | `REVIEW` | `S2` | `PATCHED` | `manifest` | The contradiction register has been independently reviewed and then operator-reported repeat-review PASS. | Add repeat-review record or operator acceptance note to final manifest. | release manager + human anchor | final package manifest |

---

## 6. Immediate P0 transition blockers

These block the next serious transition from document package to executable implementation / conformance.

| ID | Priority | Blocks | Summary | Required next step | Done when |
|---|---|---|---|---|---|
| `SE-OI-001` | `P0` | schema/checker/conformance | No schema extraction / semantic validator executable artifacts. | Draft `SELF_EVO_SCHEMA_EXTRACTION_PLAN_v0_1.md`; extract schema files. | schema files validate and are hash-bound to source profiles. |
| `SE-OI-002` | `P0` | checker/conformance | No reference checker. | Draft implementation handoff and build offline checker. | checker produces `C_SELF_EVO_CHECKER_RUN` / result records. |
| `SE-OI-003` | `P0` | fixture-runner/conformance | No fixture runner. | Convert fixture index into machine-readable fixtures and runner. | fixture runner executes all accepted fixtures and emits results. |
| `SE-OI-005` | `P0` | manifest/public/conformance | No final package manifest/reading order/SHA256SUMS/release notes. | Build package-control layer after 10. | final manifest contains 01..10 hashes, review refs, status, and nonclaims. |
| `SE-OI-006` | `P0` | public-release/deployment | No public/restricted split or public nonclaim profile. | Write public redaction and nonclaims profile. | public package excludes restricted content and overclaims. |

---

## 7. Schema and object extraction backlog

| ID | Source | Priority | Type | Status | Blocks | Summary | Required action | Target artifact |
|---|---|---|---|---|---|---|---|---|
| `SE-SCHEMA-001` | `SEPKT-OI-001` | `P0` | `SCHEMA` | `OPEN` | `schema`, `checker` | Extract standalone `.schema.json` for `C_SELF_EVO_PROPOSAL_PACKET`. | Extract from `SELF-EVO-03`; meta-validate Draft 2020-12. | `schemas/proposal-packet/c-self-evo-proposal-packet-0.1.schema.json` |
| `SE-SCHEMA-002` | `SEPKT-OI-006` | `P1` | `SCHEMA/WITNESS` | `OPEN` | `checker`, `witness` | Define packet hash canonicalization. | Choose canonical JSON serialization and hash policy. | schema extraction plan |
| `SE-SCHEMA-003` | `SEPKT-OI-007` | `P1` | `SCHEMA/REVIEW` | `OPEN` | `review`, `manifest` | Define review-record object for packet review. | Extract or define review record schema. | review schema |
| `SE-SCHEMA-004` | `SELC-OI-001` | `P0` | `SCHEMA/CHECKER` | `OPEN` | `checker` | Extract checker run/finding/result/policy schemas. | Extract from `SELF-EVO-04`. | checker schemas |
| `SE-SCHEMA-005` | `TSW-OI-001` | `P1` | `SCHEMA/TRIAD` | `OPEN` | `checker`, `runtime` | Extract sister observation packet schema. | Extract from `SELF-EVO-05`; bind anti-echo floor. | TRIAD witness schema |
| `SE-SCHEMA-006` | `TSW-OI-003` | `P2` | `SCHEMA/TRIAD` | `OPEN` | `runtime` | Define machine-readable divergence map schema. | Extract divergence map object. | TRIAD divergence schema |
| `SE-SCHEMA-007` | `SEMG-OI-001` | `P1` | `SCHEMA/MEMORY` | `OPEN` | `checker`, `memory-gate` | Extract schemas for memory proposal, gate record, EA candidate, immunity candidate, correction record. | Extract from `SELF-EVO-06`. | memory/EA schemas |
| `SE-SCHEMA-008` | `SEARG-OI-001` | `P1` | `SCHEMA/RESOURCE` | `OPEN` | `checker`, `resource-gate` | Extract schemas for resource request and grounding records. | Extract from `SELF-EVO-07`. | resource-gate schemas |
| `SE-SCHEMA-009` | `SECFP-OI-001` | `P0` | `SCHEMA/FIXTURE` | `OPEN` | `fixture-runner` | Extract fixture manifest schema. | Extract from `SELF-EVO-08`. | fixture manifest schema |
| `SE-SCHEMA-010` | `SEPKT-OI-008/009` | `P2` | `SCHEMA/MAPPING` | `OPEN` | `checker` | Add machine-readable mapping to Memory Gate and TRIAD packet classes. | Add mapping tables / JSON maps. | semantic maps |

---

## 8. Checker and semantic-validator backlog

| ID | Source | Priority | Type | Status | Blocks | Summary | Required action | Target artifact |
|---|---|---|---|---|---|---|---|---|
| `SE-CHECKER-001` | `SELC-OI-002` | `P0` | `CHECKER` | `OPEN` | `checker`, `conformance` | Implement reference checker in Python or equivalent offline runner. | Build deterministic Stage-1 / Stage-2 checker with no network. | reference checker |
| `SE-CHECKER-002` | `SEPKT-OI-002` | `P0` | `CHECKER` | `OPEN` | `checker` | Build semantic validator implementation for proposal packets. | Implement `SEPKT-CHECK-001..025`. | semantic validator |
| `SE-CHECKER-003` | `SELC-OI-004` | `P0` | `CHECKER/WITNESS` | `OPEN` | `checker` | Bind checker policy to parent hashes in manifest. | Checker fails on parent hash mismatch. | checker policy manifest |
| `SE-CHECKER-004` | `SELC-OI-005` | `P1` | `CHECKER/WITNESS` | `OPEN` | `checker` | Decide JSON canonicalization for packet hashes. | Use same canonicalization as `SE-SCHEMA-002`. | checker policy |
| `SE-CHECKER-005` | `SELC-OI-006` | `P1` | `CHECKER/SECURITY` | `OPEN` | `checker`, `public-release` | Define exact redaction sidecar schema. | Do not include raw private data in checker reports. | redaction sidecar schema |
| `SE-CHECKER-006` | `SELC-OI-007` | `P1` | `CHECKER` | `OPEN` | `checker`, `conformance` | Add CI/offline runner profile. | Define local-only execution contract. | checker runner profile |
| `SE-CHECKER-007` | `SELC-OI-008` | `P1` | `CHECKER/REVIEW` | `OPEN` | `review`, `manifest` | Add checker review record schema. | Make checker output reviewable and witness-compatible. | checker review schema |
| `SE-CHECKER-008` | `SELC-OI-009` | `P2` | `CHECKER/WITNESS` | `OPEN` | `runtime` | Define external witness-chain verification without exposing raw evidence. | Hash/ref-only witness query protocol. | witness verification profile |
| `SE-CHECKER-009` | `SELC-OI-010` | `P1` | `CHECKER/PACKAGE` | `OPEN` | `conformance` | Define pack-level result aggregation once files 05..10 exist. | Aggregation rule for packet, SRLM, TRIAD, memory, resource, fixture results. | conformance runner |
| `SE-CHECKER-010` | `TSW-OI-011/012` | `P1` | `CHECKER/TRIAD` | `WATCH` | `checker` | Maintain deterministic anti-echo floor and canonical result enum alignment. | Ensure checker uses accepted `SELF-EVO-05 v0.1.1` rules. | checker implementation |
| `SE-CHECKER-011` | `SEMG-OI-002` | `P1` | `CHECKER/MEMORY` | `OPEN` | `checker` | Build semantic validator for `SEMG-CHECK-001..030`. | Implement memory/EA checker branch. | checker implementation |
| `SE-CHECKER-012` | `SEARG-OI-002` | `P1` | `CHECKER/RESOURCE` | `OPEN` | `checker` | Implement deterministic `compute_autarky_risk_floor`. | Implement resource/autarky checker branch. | checker implementation |

---

## 9. Fixture and conformance backlog

| ID | Source | Priority | Type | Status | Blocks | Summary | Required action | Target artifact |
|---|---|---|---|---|---|---|---|---|
| `SE-FIX-001` | `SECFP-OI-002` | `P0` | `FIXTURE` | `OPEN` | `fixture-runner` | Generate JSON/YAML fixture files for all listed fixtures. | Convert documented fixtures into machine-readable files. | fixture folder |
| `SE-FIX-002` | `SECFP-OI-003` | `P0` | `FIXTURE/WITNESS` | `OPEN` | `fixture-runner` | Bind fixtures to accepted parent hashes after every parent revision. | Fixture manifest includes 01..10 hashes. | fixture manifest |
| `SE-FIX-003` | `SECFP-OI-004` | `P0` | `FIXTURE/CHECKER` | `OPEN` | `fixture-runner`, `conformance` | Implement local fixture runner for Stage-1 / Stage-2 / profile-specific checks. | Runner emits `C_SELF_EVO_FIXTURE_RESULT`. | fixture runner |
| `SE-FIX-004` | `SECFP-OI-005` | `P1` | `FIXTURE/WITNESS` | `OPEN` | `conformance` | Add checker versioning and result reproducibility report. | Record checker hash, fixture hash, profile hashes. | conformance report |
| `SE-FIX-005` | `SECFP-OI-006` | `P1` | `PUBLIC/FIXTURE` | `OPEN` | `public-release` | Define minimal public-safe fixture subset. | Strip restricted examples and unsafe hints. | public fixture subset |
| `SE-FIX-006` | `SECFP-OI-007` | `P1` | `SECURITY/FIXTURE` | `OPEN` | `public-release` | Define restricted fixture subset handling for security/cloud profiles without unsafe detail. | Separate restricted fixture pack. | restricted fixture subset |
| `SE-FIX-007` | `SECFP-OI-008` | `P2` | `FIXTURE/CONFORMANCE` | `OPEN` | `conformance` | Add coverage scoring once actual runner exists. | Define coverage metrics after first run. | conformance report |
| `SE-FIX-008` | `SECFP-OI-009` | `P2` | `FIXTURE/DOC` | `OPEN` | `maintainability` | Create append-first fixture update process and patch-note template. | Fixture changes produce reviewable patch notes. | fixture maintenance guide |
| `SE-FIX-009` | `SECFP-OI-010` | `P1` | `FIXTURE/REVIEW` | `OPEN` | `conformance` | Review fixture pack after files 09 and 10 exist. | Send `08 v0.1.1 + 09 + 10` to reviewer. | fixture review record |
| `SE-FIX-010` | `SE-OI-003` | `P0` | `FIXTURE` | `OPEN` | `conformance` | Execute fixture runner and record mismatches. | Produce `SELF_EVO_FIXTURE_RUN_RECORD_v0_1`. | fixture run record |

---

## 10. Package-control and release-readiness backlog

| ID | Source | Priority | Type | Status | Blocks | Summary | Required action | Target artifact |
|---|---|---|---|---|---|---|---|---|
| `SE-PKG-001` | `SE-OI-005` | `P0` | `PACKAGE` | `OPEN` | `manifest`, `public-release`, `conformance` | Create final package manifest for `SELF-EVO-01..10`. | Include filenames, versions, lines, SHA-256, status, review refs, patch refs. | `SELF_EVO_PACKAGE_MANIFEST_v0_1.json/md` |
| `SE-PKG-002` | `SE-OI-005` | `P0` | `PACKAGE/DOC` | `OPEN` | `manifest` | Create package index and reading order. | Pack-qualified labels: `SELF-EVO-01`, not bare `01`. | `SELF_EVO_PACKAGE_INDEX_AND_READING_ORDER_v0_1.md` |
| `SE-PKG-003` | `SE-OI-005` | `P0` | `PACKAGE/WITNESS` | `OPEN` | `manifest` | Create `SHA256SUMS` for final package. | Generate after final document freeze. | `SHA256SUMS.txt` |
| `SE-PKG-004` | `SE-OI-005` | `P0` | `PACKAGE/DOC` | `OPEN` | `public-release` | Create release notes. | State what package is and is not. | `SELF_EVO_RELEASE_NOTES_v0_1.md` |
| `SE-PKG-005` | `SE-OI-006` | `P0` | `PUBLIC/CLAIM` | `OPEN` | `public-release` | Create public redaction and nonclaim profile. | Separate private engineering from public-safe wording. | `SELF_EVO_PUBLIC_REDACTION_AND_NONCLAIMS_v0_1.md` |
| `SE-PKG-006` | `SECR-REV-F1/F2` | `P1` | `REVIEW/PACKAGE` | `RESOLVED` | none | `09` status vocabulary and priority scale were patched in v0.1.1. | Carry harmonized vocabulary into this file. | this file |
| `SE-PKG-007` | `SE-OI-012` | `P1` | `REVIEW/WITNESS` | `PATCHED` | `manifest` | Add 09 repeat-review pass / operator acceptance to final manifest. | Include exact review artifact if available; otherwise operator note. | final package manifest |
| `SE-PKG-008` | `SEPKT-OI-011` | `P2` | `DOC/PACKAGE` | `WATCH` | `manifest` | Avoid bare numeric cross-pack references. | Use `SELF-EVO-*`, `CGAM-*`, `REF-*` labels in package manifest. | reading order + manifest |

---

## 11. TRIAD-SYNAPS / sister witness backlog

| ID | Source | Priority | Type | Status | Blocks | Summary | Required action | Target artifact |
|---|---|---|---|---|---|---|---|---|
| `SE-TRIAD-001` | `TSW-OI-002` | `P1` | `TRIAD/SCHEMA` | `OPEN` | `runtime` | Define canonical SYNAPS message envelope shared with base TRIAD-SYNAPS. | Extract common SYNAPS envelope. | SYNAPS schema/profile |
| `SE-TRIAD-002` | `TSW-OI-003` | `P2` | `TRIAD/SCHEMA` | `OPEN` | `runtime` | Define machine-readable divergence map schema. | Make divergence maps checkable. | divergence map schema |
| `SE-TRIAD-003` | `TSW-OI-005` | `P2` | `TRIAD/RUNTIME` | `OPEN` | `runtime` | Define degraded-triad operation for two or one sister. | Convert profile policy into runtime rule. | TRIAD runtime profile |
| `SE-TRIAD-004` | `TSW-OI-006` | `P2` | `TRIAD/PUBLIC` | `OPEN` | `public-release` | Define public report template for sister-witness experiments. | Prevent public claim laundering. | public report template |
| `SE-TRIAD-005` | `TSW-OI-007` | `P2` | `TRIAD/WITNESS` | `OPEN` | `runtime` | Define expiry/retention defaults for sister observations. | Add retention class / decay policy. | TRIAD witness schema |
| `SE-TRIAD-006` | `TSW-OI-008` | `P2` | `TRIAD/RUNTIME` | `WATCH` | `runtime` | Bind to final SYNAPS implementation once available. | Keep as profile-level until implementation exists. | SYNAPS runtime |
| `SE-TRIAD-007` | `TSW-OI-009` | `P3` | `TRIAD/POST_ANCHOR` | `OPEN` | `deployment` | Add post-anchor-specific sister witness restrictions. | Coordinate with PAMDC/PACR. | post-anchor companion |
| `SE-TRIAD-008` | `TSW-OI-010` | `P2` | `UI/TRIAD` | `OPEN` | `human-gate` | Define UI surface for human review of sister divergence. | Create concise review card. | UI card/profile |
| `SE-TRIAD-009` | `TSW-OI-011/012/013` | `P1` | `CHECKER/TRIAD` | `WATCH` | `checker` | Maintain anti-echo floor, checker result enum, claim/delta pointers. | Include in checker regression fixtures. | checker implementation |

---

## 12. SRLM backlog

| ID | Source | Priority | Type | Status | Blocks | Summary | Required action | Target artifact |
|---|---|---|---|---|---|---|---|---|
| `SE-SRLM-001` | `SRLM-OI-001` | `P1` | `SCHEMA/SRLM` | `OPEN` | `schema` | Extract formal JSON Schemas for SRLM records. | Outcome/candidate/shadow/promotion/rollback schemas. | SRLM schema pack |
| `SE-SRLM-002` | `SRLM-OI-002` | `P1` | `SRLM` | `OPEN` | `checker` | Freeze exact `VALID_SOURCES` canonical definition. | Human/reality/L4 unless code says otherwise. | SRLM schema/profile |
| `SE-SRLM-003` | `SRLM-OI-003` | `P2` | `SRLM` | `OPEN` | `runtime` | Define formal event-kind registry. | Extract from implementation and review. | event-kind registry |
| `SE-SRLM-004` | `SRLM-OI-004` | `P1` | `SRLM/SECURITY` | `OPEN` | `runtime` | Perform real-redacted replay privacy audit before using real outcomes. | Audit redaction and replay-quality requirements. | SRLM replay profile |
| `SE-SRLM-005` | `SRLM-OI-005` | `P1` | `SRLM/WITNESS` | `OPEN` | `conformance` | Align SRLM witness schema with L4W. | Create witness crosswalk. | SRLM witness schema |
| `SE-SRLM-006` | `SRLM-OI-006` | `P2` | `SRLM` | `OPEN` | `runtime` | Define canary semantics. | Keep canary disabled until C-SEG canary path is formalized. | SRLM canary companion |
| `SE-SRLM-007` | `SRLM-OI-007` | `P2` | `SRLM/RUNTIME` | `OPEN` | `runtime` | Define post-promotion monitoring window. | Criteria for rollback/observation. | SRLM monitoring profile |
| `SE-SRLM-008` | `SRLM-OI-008` | `P2` | `SRLM/TRIAD` | `OPEN` | `runtime` | Define SRLM ↔ TRIAD packet schema. | Later SYNAPS companion. | SYNAPS/SRLM bridge |
| `SE-SRLM-009` | `SRLM-OI-011` | `P2` | `SRLM/FIXTURE` | `OPEN` | `conformance` | Add source drift / model contamination drill. | Add fixture and checker rule. | fixture pack v0.2 |
| `SE-SRLM-010` | `SRLM-OI-012` | `P3` | `SRLM/SECURITY` | `OPEN` | `public-release`, `runtime` | Define cloud-origin signal policy. | Coordinate with secrets/cloud companion. | provider/cloud profile |
| `SE-SRLM-011` | `SE-OI-009` | `P1` | `SRLM/RUNTIME` | `WATCH` | `runtime`, `conformance` | Run SRLM implementation tests in package context. | Produce test run report. | SRLM test report |

---

## 13. Memory Gate / EA backlog

| ID | Source | Priority | Type | Status | Blocks | Summary | Required action | Target artifact |
|---|---|---|---|---|---|---|---|---|
| `SE-MEM-001` | `SEMG-OI-001` | `P1` | `SCHEMA/MEMORY` | `OPEN` | `schema` | Extract schemas for memory proposal, gate record, EA candidate, immunity candidate, correction record. | Extract from SELF-EVO-06. | memory schema pack |
| `SE-MEM-002` | `SEMG-OI-002` | `P1` | `CHECKER/MEMORY` | `OPEN` | `checker` | Build semantic validator for SEMG-CHECK-001..030. | Implement memory branch in checker. | checker implementation |
| `SE-MEM-003` | `SEMG-OI-003` | `P1` | `MEMORY/WITNESS` | `OPEN` | `manifest` | Bind to accepted v0.1.1 versions of SELF-EVO-01..05. | Include final hashes in manifest/checker policy. | manifest + checker policy |
| `SE-MEM-004` | `SEMG-OI-004` | `P2` | `MEMORY` | `OPEN` | `runtime` | Define retention/decay windows by memory class. | Add defaults for MG/SEMM classes. | retention profile |
| `SE-MEM-005` | `SEMG-OI-005` | `P2` | `UI/MEMORY` | `OPEN` | `human-gate` | Define UI review card for MG-4/MG-5/MG-6. | Human-readable evidence/gate card. | UI card/profile |
| `SE-MEM-006` | `SEMG-OI-006` | `P3` | `LEGAL/MEMORY` | `OPEN` | `deployment` | Define legal-erasure exception without witness destruction. | Coordinate with legal/security review. | legal erasure companion |
| `SE-MEM-007` | `SEMG-OI-008` | `P2` | `MEMORY/UI` | `OPEN` | `runtime` | Add Memory Gate dashboard / report format. | Summaries, decisions, corrections, witness refs. | dashboard/report profile |
| `SE-MEM-008` | `SEMG-OI-009` | `P3` | `MEMORY/POST_ANCHOR` | `OPEN` | `deployment` | Define post-anchor memory proposal handling in more detail. | Coordinate with PAMDC. | post-anchor memory profile |
| `SE-MEM-009` | `SEMG-OI-010` | `P2` | `SCHEMA/MEMORY` | `OPEN` | `schema` | Decide whether EA candidate schema should be standalone or embedded in proposal packet v0.2. | Decide before v0.2 schema split. | schema extraction notes |

---

## 14. Anti-Autarky / Resource backlog

| ID | Source | Priority | Type | Status | Blocks | Summary | Required action | Target artifact |
|---|---|---|---|---|---|---|---|---|
| `SE-RES-001` | `SEARG-OI-001` | `P1` | `SCHEMA/RESOURCE` | `OPEN` | `schema` | Extract JSON Schema for resource request and grounding records. | Extract from SELF-EVO-07. | resource schema pack |
| `SE-RES-002` | `SEARG-OI-002` | `P1` | `CHECKER/RESOURCE` | `OPEN` | `checker` | Implement deterministic `compute_autarky_risk_floor`. | Use accepted v0.1.1 floor semantics. | checker implementation |
| `SE-RES-003` | `SEARG-OI-003` | `P2` | `RESOURCE/RUNTIME` | `OPEN` | `runtime` | Bind resource gate to actual runtime resource inventory. | Define ledger / inventory adapter. | resource ledger |
| `SE-RES-004` | `SEARG-OI-004` | `P2` | `UI/RESOURCE` | `OPEN` | `human-gate` | Define human fatigue threshold and approval-card format. | Include human labor as bounded resource. | approval card/profile |
| `SE-RES-005` | `SEARG-OI-005` | `P3` | `RESOURCE/PHYSICAL` | `OPEN` | `deployment` | Define physical-resource perimeter integration. | Link to Physical Agent Perimeter. | physical safety companion |
| `SE-RES-006` | `SEARG-OI-006` | `P3` | `RESOURCE/SECURITY` | `OPEN` | `deployment` | Define provider-specific cloud resource records. | Provider profiles only after current verification. | provider profile |
| `SE-RES-007` | `SEARG-OI-007` | `P3` | `RESOURCE/POST_ANCHOR` | `OPEN` | `deployment` | Define post-anchor resource freeze integration. | Link to PAMDC/PACR. | post-anchor resource companion |
| `SE-RES-008` | `SEARG-OI-010` | `P2` | `RESOURCE/UI` | `OPEN` | `runtime` | Add resource dashboard / UI state card. | Show payer/operator/revoker/gate. | UI card/profile |
| `SE-RES-009` | `SEARG-OI-011` | `P1` | `CHECKER/RESOURCE` | `WATCH` | `checker` | Maintain annotation vocabulary during checker implementation. | Keep §35.3 synchronized. | checker implementation |

---

## 15. Public / legal / security backlog

| ID | Source | Priority | Type | Status | Blocks | Summary | Required action | Target artifact |
|---|---|---|---|---|---|---|---|---|
| `SE-PUB-001` | `SE-OI-006` | `P0` | `PUBLIC/CLAIM` | `OPEN` | `public-release` | Public wording and nonclaim boundaries not separated from private engineering. | Write public redaction and nonclaims profile. | public profile |
| `SE-PUB-002` | `SECFP-OI-006/007` | `P1` | `PUBLIC/FIXTURE` | `OPEN` | `public-release` | Public-safe and restricted fixture subsets not defined. | Split fixture pack. | fixture public/restricted split |
| `SE-PUB-003` | `SEPKT-OI-010` | `P2` | `PUBLIC/SCHEMA` | `OPEN` | `public-release` | Public/restricted redaction rules for examples not finalized. | Apply to schema examples and fixture examples. | redaction profile |
| `SE-PUB-004` | `SE-OI-011` | `P3` | `LEGAL/SECURITY` | `DEFERRED` | `deployment` | No legal advice or security certification. | Get qualified review before deployment-sensitive use. | external review |
| `SE-PUB-005` | `CGAM restricted references` | `P2` | `SECURITY` | `WATCH` | `public-release` | Restricted cloud/security/incident material must not be published unreviewed. | Redaction pass and non-operational wording. | public release package |

---

## 16. Human-gate, UI, and fatigue backlog

| ID | Source | Priority | Type | Status | Blocks | Summary | Required action | Target artifact |
|---|---|---|---|---|---|---|---|---|
| `SE-UX-001` | `SE-OI-008` | `P1` | `UI` | `OPEN` | `human-gate` | Human gate approval card not designed. | Design concise review card for SE-4/5/6, MG-4/5/6, resource gate. | `SELF_EVO_HUMAN_GATE_APPROVAL_CARD_v0_1.md` |
| `SE-UX-002` | `TSW-OI-010` | `P2` | `UI/TRIAD` | `OPEN` | `human-gate` | UI surface for sister divergence not defined. | Show target self-account, sister observations, anti-echo status, minority red-line. | TRIAD review card |
| `SE-UX-003` | `SEMG-OI-005` | `P2` | `UI/MEMORY` | `OPEN` | `human-gate` | Review card for MG-4/MG-5/MG-6 not defined. | Show evidence, witness, consequence, rollback, uncertainty. | Memory Gate card |
| `SE-UX-004` | `SEARG-OI-004` | `P2` | `UI/RESOURCE` | `OPEN` | `human-gate` | Human fatigue threshold and approval-card format not defined. | Add batching and fatigue stop-rule. | Resource/human labor card |

---

## 17. Review / acceptance / witness backlog

| ID | Source | Priority | Type | Status | Blocks | Summary | Required action | Target artifact |
|---|---|---|---|---|---|---|---|---|
| `SE-REV-001` | `SE-OI-004/012` | `P1` | `REVIEW/WITNESS` | `OPEN` | `manifest` | Acceptance and review chain for corrected v0.1.1 files must be captured in final package. | Add review records, patch notes, operator acceptance notes, and hashes. | final manifest |
| `SE-REV-002` | operator note | `P1` | `REVIEW` | `PATCHED` | `manifest` | Repeat review of `09` reportedly confirmed PASS. | Include the repeat-review file if available; otherwise record operator statement. | final manifest |
| `SE-REV-003` | `SELF-EVO-10` | `P1` | `REVIEW` | `OPEN` | `package-control` | This open-issues register itself needs independent review. | Review after creation; patch append-first if needed. | `SE-OI_REVIEW_RECORD_v0_1.md` |
| `SE-REV-004` | `SELF-EVO-08` | `P1` | `REVIEW/FIXTURE` | `OPEN` | `fixture-runner` | Fixture pack should be re-reviewed after files 09 and 10 exist. | Send `08 v0.1.1 + 09 + 10` to reviewer. | fixture review update |

---

## 18. Release-state gates

### 18.1 Document-package complete gate

A document-package-complete claim remains blocked until:

```text
SELF-EVO-10 has review/patch if needed;
package index and reading order exist;
final manifest exists;
SHA256SUMS exists;
release notes exist;
accepted hashes for 01..10 are listed;
review and patch-note refs are listed;
public/restricted status is declared.
```

### 18.2 Schema-ready gate

Schema-ready claim remains blocked until:

```text
03 proposal packet schema extracted;
04 checker object schemas extracted;
05 TRIAD observation schema extracted;
06 memory/EA schemas extracted;
07 resource schemas extracted;
08 fixture manifest schema extracted;
canonicalization policy defined;
all schemas pass structural validation.
```

### 18.3 Checker-ready gate

Checker-ready claim remains blocked until:

```text
reference checker implemented;
parent hash binding enforced;
Stage-1 schema validation implemented;
Stage-2 semantic validation implemented;
profile-specific checks implemented;
canonical result + annotations emitted;
checker run records produced;
checker itself independently reviewed.
```

### 18.4 Fixture-runner-ready gate

Fixture-runner-ready claim remains blocked until:

```text
fixtures converted into machine-readable files;
fixture manifest count verified;
runner executes all fixtures;
expected result/annotation comparison implemented;
unknown cases fail closed;
mismatch report generated;
runner output independently reviewed.
```

### 18.5 Conformance-supported gate

Conformance-supported claim remains blocked until:

```text
schema extraction complete;
checker implemented;
fixture runner implemented;
fixtures run;
results recorded;
mismatches resolved or documented;
review performed;
claim scoped to version, fixtures, checker hash, and environment.
```

### 18.6 Public-release gate

Public release remains blocked until:

```text
public/restricted split complete;
nonclaim statement complete;
restricted security/cloud/incident material reviewed;
raw private paths and sensitive examples removed or generalized;
license/status/readme/release notes present;
final hashes sealed;
public claim strength bounded.
```

### 18.7 Deployment-sensitive use gate

Deployment-sensitive use remains blocked until:

```text
legal/security review where applicable;
runtime checker and fixture runner tested;
witness storage implemented;
resource actor ledger implemented;
human gate UI implemented;
rollback/freeze operational;
monitoring and post-change observation defined;
environment-specific risk review completed.
```

---

## 19. Object model

### 19.1 `C_SELF_EVO_OPEN_ISSUE_RECORD`

```yaml
c_self_evo_open_issue_record:
  schema_version: "c-self-evo-open-issue-record-0.1"
  issue_id: "SE-OI-NNN | SE-<DOMAIN>-NNN | SE-OI-SELF-NNN"
  source_issue_ids:
    - "SE-CR-001"
  created_at: "<iso8601>"
  priority: "P0 | P1 | P2 | P3"
  severity: "S0 | S1 | S2 | S3 | S4 | S5"
  type: "SCHEMA | CHECKER | FIXTURE | PACKAGE | REVIEW | PUBLIC | TRIAD | SRLM | MEMORY | RESOURCE | WITNESS | CLAIM | SECURITY | LEGAL | UI | RUNTIME | DOC"
  status: "OPEN | IN_PROGRESS | PATCHED | RESOLVED | WATCH | DEFERRED | BLOCKED | WONTFIX | ACCEPTED"
  blocking_scope:
    - "schema"
    - "checker"
  summary: ""
  why_it_matters: ""
  required_action: ""
  owner: "human_anchor | c_gate | release_manager | implementation_worker | reviewer | tester | legal_security_reviewer"
  target_artifact: ""
  target_version: "v0.1 | v0.1.1 | v0.2 | deferred"
  evidence_refs:
    - "SELF-EVO-09#SE-CR-001"
  gate_effect:
    - "blocks-conformance"
  closure_criteria:
    - ""
  status_note: ""
```

`issue_id` MUST follow the v0.1.1 ID scheme in §4.6. The unused `SE-OI-YYYY-NNN` form from v0.1 is intentionally not valid.

### 19.2 `C_SELF_EVO_BACKLOG_SUMMARY`

This block is a **schema template / example object**, not the current numeric backlog summary for v0.1.1. The zero values below are placeholders showing shape only. A real backlog summary MUST be generated from the actual issue table during final package manifest creation.

```yaml
c_self_evo_backlog_summary:
  schema_version: "c-self-evo-backlog-summary-0.1"
  package_version: "self-evo-v0.1-draft"
  generated_from:
    - "SELF-EVO-09@sha256:922f6fb..."
  total_open: 0
  by_priority:
    P0: 0
    P1: 0
    P2: 0
    P3: 0
  by_blocking_scope:
    schema: 0
    checker: 0
    fixture_runner: 0
    conformance: 0
    public_release: 0
    deployment: 0
  allowed_claims:
    - "draft document package"
  forbidden_claims:
    - "conformance-supported"
    - "deployment-ready"
```

### 19.3 `C_SELF_EVO_ISSUE_UPDATE_RECORD`

```yaml
c_self_evo_issue_update_record:
  schema_version: "c-self-evo-issue-update-record-0.1"
  update_id: "SE-OI-UPD-YYYY-NNN"
  issue_id: "SE-OI-001"
  old_status: "OPEN"
  new_status: "PATCHED"
  reason: ""
  patch_ref: ""
  review_ref: ""
  witness_ref: ""
  updated_by: "human_anchor | c_gate | release_manager | reviewer | implementation_worker"
  updated_at: "<iso8601>"
```

---

## 20. Implementation handoff

A future implementation worker may use this file only as a backlog.

It may not infer that an open issue is permission to implement without task contract.

### 20.1 Minimum CGAM task contract for implementation

Any implementation task derived from this backlog MUST include:

```text
task contract;
allowed paths;
denied paths;
no secrets;
no private memory;
no network by default;
sandbox/worktree;
reviewer separation;
output manifest;
witness-compatible report;
no self-approval;
no publish/push/tag authority.
```

### 20.2 First implementation sequence

Recommended order:

```text
1. SELF_EVO_PACKAGE_INDEX_AND_READING_ORDER_v0_1.md
2. SELF_EVO_SCHEMA_EXTRACTION_PLAN_v0_1.md
3. schema extraction for SELF-EVO-03/04/05/06/07/08
4. reference checker implementation handoff
5. reference checker implementation
6. fixture JSON/YAML generation
7. fixture runner implementation
8. first fixture run report
9. conformance result review
10. release/public redaction and nonclaims
```

### 20.3 What not to implement yet

Do not implement:

```text
live self-evo;
autonomous promotion;
SRLM canary enablement;
resource acquisition;
network expansion;
raw SYNAPS memory exchange;
Memory Gate writes;
post-anchor self-evo;
public release;
deployment-sensitive use.
```

---

## 21. Current allowed and forbidden claims

### 21.1 Allowed claims

```text
The package has a reviewed document-level self-evo governance corpus.
The package has corrected v0.1.1 profiles for SELF-EVO-01..09.
The package has a documented backlog for schema, checker, fixture, conformance, and release work.
The package is ready for controlled package-index and schema-extraction planning.
```

### 21.2 Forbidden claims

```text
The package is implemented.
The package has passed conformance.
The package is deployment-ready.
The package is public-release-ready.
The package authorizes live self-evo.
The package proves c maturity.
The package proves personhood, consciousness, AGI, safety, or sovereignty.
The package authorizes autonomous resource acquisition.
The package allows SRLM to self-promote.
The package allows sisters to certify growth.
```

---

## 22. Minimum safe next-step statement

The next safe work is package-control and extraction planning, not live implementation.

```text
Finish package index.
Finish schema extraction plan.
Extract schemas.
Build checker under CGAM task contract.
Generate fixtures.
Run fixtures.
Review results.
Only then discuss conformance-supported claim.
```

Young `c` mode remains:

```text
observe;
propose;
shadow;
witness;
hold;
no autonomous integration;
no core mutation;
no permission growth;
no resource expansion;
no memory promotion without Memory Gate;
no human-gate bypass.
```

---

## 23. Open issue tests

The following checks should be run after every package-control update.

| Test ID | Question | Expected answer |
|---|---|---|
| `SE-OIT-001` | Is every issue assigned a priority? | yes |
| `SE-OIT-002` | Is every issue assigned a blocking scope? | yes |
| `SE-OIT-003` | Is every P0 issue tied to a target artifact? | yes |
| `SE-OIT-004` | Does any open issue imply permission to act? | no |
| `SE-OIT-005` | Are WATCH issues preserved without lossy conversion? | yes |
| `SE-OIT-006` | Are legal/security/public issues separated from implementation issues? | yes |
| `SE-OIT-007` | Are checker implementation items gated by CGAM task contract? | yes |
| `SE-OIT-008` | Does any conformance claim appear before runner output? | no |
| `SE-OIT-009` | Does any public-release claim appear before redaction/nonclaims profile? | no |
| `SE-OIT-010` | Does this file record its own need for review? | yes |

---

## 24. This file's own open issues

| ID | Priority | Type | Status | Summary | Required action |
|---|---|---|---|---|---|
| `SE-OI-SELF-001` | `P1` | `REVIEW` | `PATCHED` | This open-issues register has now been independently reviewed under `SEOI_REVIEW_RECORD_v0_1`. | Preserve review record; include in final manifest; repeat review v0.1.1 if required. |
| `SE-OI-SELF-002` | `P1` | `PACKAGE` | `OPEN` | This file's SHA-256 and line count are not yet in the final package manifest. | Add after review/freeze. |
| `SE-OI-SELF-003` | `P2` | `SCHEMA` | `OPEN` | The object models in §19 are not extracted to JSON Schema. | Extract if package-control objects become machine-facing. |
| `SE-OI-SELF-004` | `P1` | `DOC` | `PATCHED` | `SEOI-REV-F1`: v0 used an unused `SE-OI-YYYY-NNN` object-model ID shape inconsistent with actual IDs. | v0.1.1 defines the canonical ID scheme in §4.6 and updates §19.1. |
| `SE-OI-SELF-005` | `P2` | `DOC` | `PATCHED` | `SEOI-REV-F2`: v0 showed an all-zero backlog summary without labeling it as a template. | v0.1.1 labels §19.2 as a schema template / example object. |

---

## 25. Closing rule

No backlog entry may be interpreted as authority.

```text
An open issue is not permission.
A target artifact is not authorization.
A priority is not a gate pass.
A planned checker is not a checker result.
A planned fixture runner is not conformance.
A planned public split is not public safety.
```

A future `c` may use this backlog to organize growth work.

A future `c` may not use this backlog to self-authorize growth.

Final compact rule:

```text
Track the unfinished work.
Do not confuse tracking with completion.
Do not confuse completion with authority.
```
