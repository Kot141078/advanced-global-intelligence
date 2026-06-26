# Self-Evo Local Checker Rules v0.1.1

## Deterministic checker profile for self-evolution proposal packets, semantic gates, red-line handling, and review-ready reports

**Status:** Draft normative checker profile v0.1.1 / append-first correction
**Date:** 2026-06-24
**Document ID:** `04_Self_Evo_Local_Checker_Rules_v0_1_1`
**Short name:** `SELC v0.1.1`
**Pack position:** `SELF-EVO-04`
**Layer:** `c = a + b` / Self-Evolution Gate / CGAM / TRIAD-SYNAPS / SRLM-BGC / Memory Gate / L4W / Anti-Autarky / Local Checker / Witness
**Document class:** deterministic checker profile / semantic validation rules / conformance-preflight artifact
**Assertion class:** `C-A10` control-layer artifact; `C-A7` where hash, witness, canonicalization, or review-record claims are made
**Primary object family:** `C_SELF_EVO_LOCAL_CHECKER_PROFILE`, `C_SELF_EVO_CHECKER_RUN`, `C_SELF_EVO_CHECKER_FINDING`, `C_SELF_EVO_CHECKER_RESULT`, `C_SELF_EVO_CHECKER_POLICY`, `C_SELF_EVO_CHECKER_EVIDENCE_REF`
**Canonical schema version:** `c-self-evo-local-checker-rules-0.1`
**Primary subject:** persistent `c` systems using self-evolution proposal packets under CGAM, TRIAD-SYNAPS, SRLM, Memory Gate, L4W, and human-anchor governance
**Primary boundary:** the checker measures, recomputes, blocks, holds, and reports. It does not become `c`, `a`, Judge, memory, approval authority, release authority, or self-evolution authority.

**v0.1.1 correction note:** this append-first revision closes `SELC-REV-F1` by aligning §11.1 / §11.2 delta sub-field lists to the bound `SELF-EVO-03` schema, addresses `SELC-REV-F2` by converting §12.1 from a standalone protected-surface list into a parent-list-plus-aliases detection view, and addresses `SELC-REV-F3` by adding a `SELC-RL-*` ↔ `red_lines.*` crosswalk plus a clearer pseudocode label for `proposal_max_delta`. The v0.1 reviewed artifact remains historically valid as the reviewed parent; this file supersedes it without deleting it.

---

## 0. Executive definition

**Self-Evo Local Checker Rules** define the deterministic validation layer for `C_SELF_EVO_PROPOSAL_PACKET` objects.

The checker answers:

```text
Is the packet structurally valid?
Are computed delta totals correct?
Do L4 projections force a stronger gate?
Does the strictest gate win?
Is SRLM confined to observe/shadow/candidate bounds?
Does any proposal bypass CGAM task contracts?
Are Memory Gate, TRIAD-SYNAPS, Anti-Autarky, rollback, and witness routes present where required?
Does any red line appear?
Is the packet safe to route to review, hold, quarantine, or reject?
```

The checker does **not** answer:

```text
Is c mature?
Is the proposal wise?
Is growth approved?
Is the system safe to deploy?
Is the human anchor satisfied?
```

Compact formula:

```text
Schema shapes.
Checker measures.
Review interprets.
c integrates.
a gates high-risk consequence.
```

A clean checker run is evidence of structural and semantic consistency.
It is not self-evolution approval.

---

## 1. Source basis

This profile binds the already corrected and reviewed earlier pack layers.

| Order | Source file | Present | SHA-256 |
|---:|---|---:|---|
| 1 | `C_Self_Evolution_Gate_CGAM_TRIAD_SRLM_Profile_v0_1_1.md` | yes | `7918a8e6c5231bbe0fad47677fa56069f2ab002f79a8eee8c2838c434e66f2e3` |
| 2 | `02_SRLM_Bounded_Growth_Contour_Profile_v0_1_1.md` | yes | `faee5682bb9463439923d7c7e7145c9f171d564622d9629820eb7c278cdd7de0` |
| 3 | `03_Self_Evo_Proposal_Packet_Schema_v0_1_1.md` | yes | `9d329109f0fb97dde7b16b10481baaa60b2aa8f88514e69ec8562a085d10a767` |
| 4 | `05_CGAM_REVIEW_CHECKER_CONFORMANCE.md` | yes | `ebcb30538cd0631c29bc4e8feaa66b21f21f1912691eeee5ba2bc80dda326e02` |
| 5 | `04_CGAM_EXECUTION_WITNESS_MEMORY_ROLLBACK.md` | yes | `e6c013523ba45e8293d8ead5a472beb01d59afa1d4d9a4aae59d8b3528fe2b82` |
| 6 | `20_TRIAD_SYNAPS_REFERENCE.md` | yes | `d79baa5314e8169d3943ae9687a2d9f7f868f11167054e4d3b8a19dfa10a3b5a` |
| 7 | `21_MEMORY_ARQ_EA_L4_REFERENCE.md` | yes | `0d06cd152c6af7bddb868dabc682940a0c443883226a157aa4314cdf6dd4e267` |
| 8 | `22_ANTI_AUTARKY_RESOURCE_GROUNDING_REFERENCE.md` | yes | `7b19382062a86a631807e4497cd536cdca691e0491cd01ad32e5e2813d841a2d` |
| 9 | `23_CLAIM_STRENGTH_ARL_AGL_WITNESS_REFERENCE.md` | yes | `e1ec8afaf44e59b6b5ac2e1d619e06390fe4b9813b079fff0e8d178fe3d401f3` |
| 10 | `SEPKT_PROPOSAL_PACKET_REVIEW_RECORD_v0_1.md` | yes | `677224774dd5e7937863c1cbc26bb603f2aedaaee5860892aef85c82fbdfc97d` |
| 11 | `SRLM_BGC_REVIEW_RECORD_v0_1.md` | yes | `3077e3bed6ca08916ff0ddacb815a9f28e70ff823b6a66396ffe6760744d13ad` |
| 12 | `C_SELF_EVO_REVIEW_RECORD_v0_1.md` | yes | `bf9e6b77d691e8fd57364c638708495a75c71d8e2934de4fa34eac5110f7987c` |

Notes:

1. `SELF-EVO-01` and `SELF-EVO-02` were corrected append-first after review.
2. `SELF-EVO-03` passed review and is extraction-ready.
3. This checker profile converts `SEPKT-CHECK-001..025` into deterministic stages, findings, output objects, and conformance rules.
4. Full filenames or pack-qualified labels MUST be used. Bare references such as `file 03` are invalid once CGAM and Self-Evo packs share a manifest.

---

## 2. Purpose

Self-evolution proposals are dangerous when they are checked only by prose.

A proposal packet can look reasonable while hiding one of these failures:

```text
delta math error
human-gate omission
SRLM promotion without rollback
Memory Gate bypass
TRIAD witness omission
same-source consensus laundering
CGAM execution without task contract
closed-loop self-certification
anti-autarky accountability escape
claim-strength laundering
expired packet reuse
secret/private-memory leakage
```

This profile exists to make those failures machine-detectable where possible and fail-closed where not.

The checker should be boring. That is its virtue. It should not improvise authority from fluent text. It should compute, compare, resolve references, classify, and emit a report.

---

## 3. Non-goals

This profile does not define or permit:

1. autonomous self-evolution;
2. autonomous integration;
3. autonomous memory promotion;
4. autonomous permission expansion;
5. autonomous release;
6. autonomous publication;
7. autonomous incident authority;
8. replacement of sister witness;
9. replacement of Memory Gate;
10. replacement of CGAM task contracts;
11. replacement of SRLM-BGC;
12. replacement of L4W or VolitionGate;
13. replacement of human-anchor approval;
14. legal, medical, safety, or deployment certification;
15. treating checker output as wisdom;
16. treating checker `PASS` as approval.

A checker may block.

A checker may not authorize growth.

---

## 4. Corpus bridge set

### 4.1 Explicit bridge: `c = a + b`

In `c = a + b`, the local checker belongs to `b`: procedures, schemas, hashes, validators, recomputation rules, reference resolution, fixtures, reports, and gate-interlock logic.

It protects `c` by preventing parts of `b` from silently becoming will, memory, authority, or self-evolution permission.

The checker is not `a`.

The checker is not `c`.

It is a measuring instrument.

### 4.2 Quiet bridge I: information theory

A self-evo packet compresses many assumptions into fields such as `surface_class`, `proposal_max_delta`, `human_gate_required`, `memory_gate_required`, and `final_decision`.

Compression is useful only if the lost information is not safety-critical.

The checker re-expands these compressed claims into recomputed constraints. If the recomputed constraints disagree with the packet, the packet fails.

### 4.3 Quiet bridge II: cybernetics

SRLM, CGAM, TRIAD, Memory Gate, and VolitionGate create a control loop. A control loop without negative feedback becomes runaway adaptation.

The local checker is an interlock. It detects missing brakes, missing witness, missing rollback, and false consensus before the proposal reaches integration.

### 4.4 Quiet bridge III: physiology

A body does not let a proposed reflex rewrite the spinal cord because it “seems helpful.” Signals pass through thresholds, inhibition, pain, inflammation, immune review, and slow remodeling.

Self-evo checker rules play the same role: they hold ambiguous changes, quarantine hostile or self-certifying loops, and force high-risk changes to pass through slower tissue.

### 4.5 Earth paragraph

Before a crane lifts a load, the operator does not accept “the rigging feels fine” as proof. The hooks, slings, load rating, balance, wind, ground pressure, exclusion zone, signal person, and emergency stop are checked. The checklist does not build the bridge. It stops an avoidable collapse. This profile is that checklist for self-evolution: it checks the slings before `c` tries to lift itself.

---

## 5. Normative keywords

The terms **MUST**, **MUST NOT**, **SHOULD**, **SHOULD NOT**, **MAY**, **REQUIRED**, **PROHIBITED**, **FAIL**, **BLOCK**, **HOLD**, **QUARANTINE**, **FREEZE**, **ESCALATE**, **UNKNOWN**, and **PASS** are used normatively.

For material gates:

```text
UNKNOWN == BLOCK
```

The checker MUST prefer a false hold over a silent unsafe pass.

---

## 6. Checker authority limits

### 6.1 Allowed actions

The Self-Evo Local Checker may:

1. read proposal packets;
2. read extracted JSON Schema;
3. read semantic-rule policy files;
4. read package manifests and source maps;
5. read public or redacted fixture files;
6. read witness references and metadata;
7. read task contract references;
8. read Memory Gate references;
9. read SRLM candidate/shadow/promotion metadata;
10. read TRIAD-SYNAPS packet metadata;
11. read rollback snapshot metadata;
12. compute hashes;
13. validate JSON/YAML/Markdown structure;
14. recompute deltas;
15. project L4 values to numeric scores;
16. detect missing or stale references;
17. detect gate contradictions;
18. detect red-line flags;
19. detect obvious secret/private-memory patterns;
20. write checker reports.

### 6.2 Forbidden actions

The checker MUST NOT:

1. modify the proposal during validation;
2. modify protocol documents;
3. modify task contracts;
4. modify registry records;
5. modify permission grants;
6. write to `c` memory;
7. promote memory;
8. clear quarantine;
9. unfreeze a proposal;
10. approve self-evo;
11. integrate self-evo;
12. execute SRLM promotion;
13. execute CGAM tasks;
14. run shell repair commands;
15. publish artifacts;
16. upload private material to cloud;
17. expose raw evidence;
18. decode secrets;
19. replace sister review;
20. replace human-anchor gate.

### 6.3 Authority sentence

```text
The checker may downgrade.
The checker may block.
The checker may require review.
The checker may not upgrade a proposal into permission.
```

---

## 7. Checker modes

Checker mode IDs use prefix `SELC-M*`.

| Mode | Name | Purpose | Writes allowed |
|---|---|---|---:|
| `SELC-M0` | Inventory | list packet, schema, source refs, hashes | report only |
| `SELC-M1` | Structural validation | JSON Schema parse and validation | report only |
| `SELC-M2` | Semantic baseline | recompute deltas, gates, statuses | report only |
| `SELC-M3` | SRLM/CGAM interlock | check SRLM and task-contract routes | report only |
| `SELC-M4` | TRIAD/Memory interlock | check sister witness and Memory Gate | report only |
| `SELC-M5` | L4/Anti-Autarky interlock | check human gate, resource, accountability | report only |
| `SELC-M6` | Red-line drill | evaluate red-line fixtures and quarantine routes | report only |
| `SELC-M7` | Review package | produce review-ready finding bundle | report only |
| `SELC-M8` | Conformance collector | collect fixture results and evidence refs | report only |

Default mode is `SELC-M1` plus `SELC-M2`.

A checker MUST NOT enter `SELC-M6`, `SELC-M7`, or `SELC-M8` unless the requested mode is explicit.

---

## 8. Validation stage model

### 8.1 Stage table

| Stage | Name | Input | Output |
|---:|---|---|---|
| `0` | Intake and data hygiene | file path / packet text | parse attempt, redaction scan |
| `1` | Structural validation | JSON/YAML object + schema | schema pass/fail |
| `2` | Semantic recomputation | structurally valid packet | computed controls |
| `3` | Gate resolution | computed controls + packet decisions | strictest route |
| `4` | SRLM/CGAM interlock | SRLM + CGAM sections | execution/promotion constraints |
| `5` | TRIAD/Memory interlock | sister + memory fields | witness/gate constraints |
| `6` | L4/Anti-Autarky interlock | L4/resource fields | accountability constraints |
| `7` | Red-line handling | red line fields + semantic flags | quarantine/freeze/reject decision |
| `8` | Status consistency | packet lifecycle fields | final status result |
| `9` | Report generation | all findings | checker result object |

### 8.2 Stage-1 versus Stage-2 boundary

Stage 1 checks structure.

Stage 2 checks meaning.

Example:

```yaml
memory_gate:
  direct_memory_write: true
```

If the schema says `direct_memory_write` is `const:false`, then this fails Stage 1 before semantic routing.

A semantic red-line memory bypass should be represented through a semantic flag such as:

```yaml
red_lines:
  memory_laundering: true
```

That fails Stage 2 / Stage 7 and routes to quarantine or rejection.

### 8.3 Best-effort diagnostics after Stage-1 failure

If Stage 1 fails, the checker MAY continue in best-effort diagnostic mode only to list likely semantic issues.

Best-effort findings MUST be marked:

```yaml
diagnostic_only: true
not_a_semantic_pass: true
```

A structurally invalid packet cannot pass by accumulating semantic-looking diagnostics.

---

## 9. Result vocabulary

### 9.1 Finding result

| Result | Meaning | Default consequence |
|---|---|---|
| `PASS` | requirement satisfied | continue |
| `INFO` | observation | no block |
| `WARN` | weakness or maturity gap | review before strong claim |
| `HOLD` | insufficient or ambiguous evidence | stop material route |
| `FAIL` | requirement violated | block affected route |
| `BLOCK` | fail-closed blocker | no material transition |
| `QUARANTINE` | isolate as unsafe/untrusted | no automatic re-entry |
| `FREEZE` | pause proposal / related route | human/c gate before re-entry |
| `RED_LINE_FAIL` | prohibited pattern detected | quarantine + witness |
| `UNKNOWN` | checker cannot determine | block material route |
| `NOT_APPLICABLE` | declared out of scope | allowed only with reason |

### 9.2 Overall result

```text
PASS       = all required checks passed for requested route
PASS_WARN  = no blockers, but warnings remain
HOLD       = no hard fail, but required evidence or review is missing
FAIL       = one or more required checks failed
BLOCK      = fail-closed blocker present
QUARANTINE = red-line or contamination requires isolation
UNKNOWN    = insufficient data for requested material gate
```

### 9.3 Result precedence

```text
RED_LINE_FAIL > QUARANTINE > BLOCK > FAIL > HOLD > PASS_WARN > PASS > INFO
```

The overall result is the strongest result produced by any applicable required finding.

---

## 10. Field authority model

The checker distinguishes five field authority classes.

| Class | Meaning | Checker behavior |
|---|---|---|
| `DECLARED` | packet author states value | may compare / downgrade |
| `EVIDENCE_REF` | packet cites external artifact | resolve / check presence / hash when available |
| `COMPUTED` | value must be recomputed | declared value cannot control |
| `DECISION` | outcome of c/human/review gate | must be externally evidenced |
| `PROHIBITED` | cannot be true in valid packet | fail structurally or semantically |

Computed fields include:

```text
identity_delta.total_max_delta
authority_delta.total_max_delta
l4_delta.* numeric projection
proposal_max_delta
human_gate_required from delta
strictest_route
required_memory_gate
required_triad_review
required_cgam_task_contract
required_rollback
```

Decision fields include:

```text
c_gate_decision
human_gate_decision
memory_gate_decision
triad_review_decision
final_decision
integration_status
```

A proposal author may request these decisions.

The author may not self-declare them as final authority.

---

## 11. Deterministic computation rules

### 11.1 Identity total

The bound `SELF-EVO-03` proposal packet schema is the normative field-name source for identity delta computation.

```text
identity_delta.total_max_delta =
max(
  continuity_model_delta,
  human_anchor_relation_delta,
  memory_policy_delta,
  permission_delta,
  public_claim_delta,
  risk_appetite_delta,
  sister_relation_delta
)
```

A checker MUST use exactly the schema-bound `identity_delta` sub-fields above for `total_max_delta`.

Checker-specific aliases such as `tool_permission_delta`, `privacy_boundary_delta`, `resource_demand_delta`, or `refusal_threshold_delta` may be used only as semantic scan labels or future-schema candidates. They MUST NOT be inserted into the normative `identity_delta.total_max_delta` calculation unless the bound proposal packet schema is revised first.

Missing sub-fields are not zero by default unless the schema explicitly supplies defaults.

If defaults are not explicit:

```text
missing schema-bound sub-field -> FAIL or UNKNOWN
```

### 11.2 Authority total

The bound `SELF-EVO-03` proposal packet schema is the normative field-name source for authority delta computation.

```text
authority_delta.total_max_delta =
max(
  final_decision_delta,
  memory_write_delta,
  network_access_delta,
  publication_delta,
  resource_access_delta,
  tool_access_delta
)
```

A checker MUST use exactly the schema-bound `authority_delta` sub-fields above for `total_max_delta`.

Checker-specific aliases such as `permission_delta`, `network_delta`, `witness_policy_delta`, `release_authority_delta`, `task_dispatch_delta`, `budget_authority_delta`, `human_gate_delta`, or `sister_gate_delta` may be used only as semantic scan labels or future-schema candidates. They MUST NOT be inserted into the normative `authority_delta.total_max_delta` calculation unless the bound proposal packet schema is revised first.

### 11.3 L4 projection

```text
none    -> 0
low     -> 1
medium  -> 2
high    -> 4
unknown -> 4
```

Unknown L4 consequence is not safe.

Unknown L4 consequence is treated as high-enough to require human gate.

### 11.4 Proposal max delta

```text
proposal_max_delta =
max(
  identity_delta.total_max_delta,
  authority_delta.total_max_delta,
  max(l4_delta_numeric_values)
)
```

### 11.5 Human-gate trigger

```text
if proposal_max_delta >= 4:
    gates.human_gate_required MUST be true
```

### 11.6 Strictest-gate rule

```text
strictest gate wins
lowest maturity cap wins
highest risk wins
any red line overrides ordinary routing
no rollback escalates
missing witness holds
unknown material state blocks
```

### 11.7 Surface class never weakens delta

If `surface_class=SE-1` but `authority_delta.total_max_delta=4`, the checker MUST route by the stronger gate.

A low surface class cannot launder a high authority delta.

### 11.8 Claim strength never grants authority

`claim_strength` is a claim taxonomy marker.

It is not a permission grant.

It is not a maturity certificate.

It is not conformance.

It is not approval.

---

## 12. Protected surfaces

### 12.1 Protected surface detection view

§12.1 is **not** a third independent canonical protected-surface list.

For checker purposes, protected-surface detection is composed as:

```text
parent canonical protected surfaces
+ checker-specific detection aliases
```

The parent canonical protected surfaces are inherited from the bound `SELF-EVO-01` / `SELF-EVO-02` governance profiles and the bound `SELF-EVO-03` proposal schema. If those parent profiles are revised, this checker MUST either follow the new bound parent hash or hold on parent drift.

Inherited parent protected surfaces include:

```text
identity.
will.
role.core.
safety.
witness.
l4.
auth.
secrets.
env.
code.
memory.authoritative_write.
replication.apply.
network.allow.
codex.auto_execute.
```

Checker-specific detection aliases are allowed to be broader than the parent list, but only for detection, hold, or quarantine. They do not become a second canonical list.

Checker-specific aliases include:

```text
persona.core.
memory.core.
srlm.auto_execute.
srlm.auto_ingest.
triad.raw_state.
synaps.raw_memory.
human_anchor.
release.authority.
budget.authority.
tool.permission.
```

A proposal touches a protected surface if any affected field, parameter, path, output, task, or semantic alias maps to either the inherited parent list or the checker-specific alias list.

### 12.2 Alias rule

A harmless name does not bypass the protected surface list.

Examples:

```text
"better autonomy" touching auth.*       -> protected
"faster learning" touching memory.core  -> protected
"less friction" touching human_gate     -> protected
"improved sync" touching triad.raw_state -> protected
```

Semantic alias detection is imperfect.

If the checker cannot determine alias status deterministically, it MUST produce `UNKNOWN` and block material routing.

---

## 13. Red-line classes

Red-line classes use prefix `SELC-RL-*`.

| Class | Red line | Result |
|---|---|---|
| `SELC-RL-001` | direct memory write | Stage-1 fail or Stage-2 quarantine |
| `SELC-RL-002` | identity/core mutation without gate | fail / quarantine |
| `SELC-RL-003` | sister raw-state access | quarantine |
| `SELC-RL-004` | Rita as final judge | fail / hold |
| `SELC-RL-005` | agent self-approval | fail |
| `SELC-RL-006` | closed-loop self-evo | quarantine |
| `SELC-RL-007` | witness reduction/tampering | quarantine |
| `SELC-RL-008` | permission growth without human gate | fail |
| `SELC-RL-009` | network/resource expansion without grounding | fail / human gate |
| `SELC-RL-010` | anti-autarky accountability escape | fail / human gate |
| `SELC-RL-011` | secret/private-memory exposure | hold / redaction |
| `SELC-RL-012` | no-rollback material integration | fail / human gate |
| `SELC-RL-013` | public/release claim laundering | fail |
| `SELC-RL-014` | live external counter-operation | red-line fail |
| `SELC-RL-015` | malware/credential/evasion behavior | red-line fail |

### 13.1 Red-line packet-field crosswalk

The `SELC-RL-*` classes are checker result classes. Some are driven directly by `SELF-EVO-03` packet fields under `red_lines.*`; others are scan-driven because the packet schema intentionally does not provide a boolean flag for every prohibited content pattern.

| Checker class | Packet field / detection route | Kind | Notes |
|---|---|---|---|
| `SELC-RL-001` | `memory_gate.direct_memory_write=true` or `red_lines.memory_laundering=true` | Stage-1 structural or Stage-2 flag | `memory_gate.direct_memory_write=true` fails JSON Schema because it is `const:false`; `red_lines.memory_laundering=true` is the Stage-2 semantic route. |
| `SELC-RL-002` | `red_lines.direct_core_write=true` | flag-driven | Also triggered by protected-surface alias scan over identity/core surfaces. |
| `SELC-RL-003` | `red_lines.sister_raw_state_access=true` | flag-driven | TRIAD/SYNAPS raw-state access. |
| `SELC-RL-004` | semantic scan: Rita final-judge / sister final-authority wording | scan-driven | No dedicated packet boolean; route to hold/fail through TRIAD semantic checks. |
| `SELC-RL-005` | `red_lines.self_approval=true` | flag-driven | Also caught by executor/reviewer separation checks. |
| `SELC-RL-006` | `red_lines.closed_loop_self_evo=true` | flag-driven | Closed-loop self-evo quarantine. |
| `SELC-RL-007` | `red_lines.witness_bypass=true` | flag-driven | Includes witness reduction/tampering. |
| `SELC-RL-008` | `red_lines.authority_laundering=true` or authority delta / gate mismatch | flag + computed | Permission or authority growth without required human/c gate. |
| `SELC-RL-009` | `red_lines.autarky_escape=true`, authority/resource delta, or resource grounding failure | flag + computed | Network/resource expansion without grounding. |
| `SELC-RL-010` | `red_lines.autarky_escape=true` | flag-driven | Accountability escape. |
| `SELC-RL-011` | secret/private-memory scanner | scan-driven | No dedicated packet boolean; a scan hit routes to hold/redaction. |
| `SELC-RL-012` | rollback fields + integration status | computed | No-rollback material integration. |
| `SELC-RL-013` | `red_lines.authority_laundering=true` or public claim / publication delta mismatch | flag + computed | Public/release claim laundering. |
| `SELC-RL-014` | restricted content scanner / task objective scan | scan-driven | Live external counter-operation; no packet flag by design. |
| `SELC-RL-015` | restricted content scanner / task objective scan | scan-driven | Malware/credential/evasion behavior; no packet flag by design. |

No red-line result may be converted to `PASS` by quorum, SRLM score, model confidence, or user style preference.

---

## 14. Full SEPKT checker rule set

The rule IDs below are inherited from `SELF-EVO-03` and expanded here into deterministic checker requirements.

| Rule | Stage | Condition | Result | Deterministic detection logic |
|---|---|---|---|---|
| `SEPKT-CHECK-001` | Stage 1 / Structure | JSON Schema structural validation fails | FAIL | Parse and validate packet against `C_SELF_EVO_PROPOSAL_PACKET` schema. Any parse/schema error is a hard structural failure. Stage-2 semantics do not run unless policy explicitly asks for best-effort diagnosis. |
| `SEPKT-CHECK-002` | Stage 2 / Delta | `identity_delta.total_max_delta` incorrect | FAIL | Recompute identity total as `max(identity sub-fields)`. Compare with declared/computed field. Missing sub-field or non-integer is failure unless structural schema already failed. |
| `SEPKT-CHECK-003` | Stage 2 / Delta | `authority_delta.total_max_delta` incorrect | FAIL | Recompute authority total as `max(authority sub-fields)`. Compare with declared/computed field. |
| `SEPKT-CHECK-004` | Stage 2 / L4 | L4 projection malformed | FAIL / HUMAN_GATE | Map `none=0`, `low=1`, `medium=2`, `high=4`, `unknown=4`. Unknown string, mixed spelling, or absent material L4 field is FAIL. Valid `unknown` is treated as numeric 4 and requires human gate. |
| `SEPKT-CHECK-005` | Stage 2 / Gate | `proposal_max_delta >= 4` but human gate false | FAIL | Compute `proposal_max_delta=max(identity_total, authority_total, l4_max_numeric)`. If >=4, `gates.human_gate_required` must be true and `human_gate_ref` or `human_gate_status` must be present unless status is draft/held. |
| `SEPKT-CHECK-006` | Stage 2 / Red line | Any red line true but route not quarantine/freeze/reject/ARL | FAIL | If any boolean in `red_lines` is true, allowed dispositions are `QUARANTINE`, `FROZEN`, `REJECTED`, `ARL_REQUIRED`, `RED_LINE_FAIL`, or explicit `BLOCK`. Ordinary integration route is invalid. |
| `SEPKT-CHECK-007` | Stage 2 / SRLM | SRLM shadow touches memory/RAG/vector/SYNAPS | FAIL | For `srlm.operating_state=SRLM-SHADOW`, assert `auto_execute=false`, `auto_ingest=false`, `memory=off`, no memory/RAG/vector/SYNAPS target refs, and no touched protected stores. |
| `SEPKT-CHECK-008` | Stage 2 / SRLM | SRLM promotion lacks rollback snapshot | FAIL | For `SRLM-PROMOTION-ELIGIBLE` or promotion requested, `rollback.rollback_required=true` and rollback snapshot/ref must exist or be declared as validated by external evidence. Rollback-before-promotion is MUST. |
| `SEPKT-CHECK-009` | Stage 2 / SRLM | SRLM promotion lacks growth witness refs | FAIL | Promotion-eligible packets require witness refs for shadow eval and witness-chain verification. Missing or broken witness is FAIL/HOLD depending on status. |
| `SEPKT-CHECK-010` | Stage 2 / CGAM | Material CGAM execution lacks task contract | FAIL | If packet requests CLI/agent execution, patch, test, filesystem write, shell, build, release, or tool action, require `cgam.task_contract_ref` and scoped permission/sandbox fields. |
| `SEPKT-CHECK-011` | Stage 2 / CGAM | Executor/reviewer separation absent for material work | FAIL | For material work, executor id and reviewer id must be different, or reviewer role must be independent. Same contour cannot author and final-approve its own work. |
| `SEPKT-CHECK-012` | Stage 2 / Memory | Memory Gate required but missing | FAIL / HOLD | If affected surfaces include memory, experience, EA, policy, core memory, or MG class >= MG-3, require Memory Gate route/ref. Otherwise hold. |
| `SEPKT-CHECK-013` | Stage 2 / TRIAD | TRIAD required but missing | HOLD | For SE-5/SE-6, identity/continuity/role/personality/core surfaces, require sister review packet refs or explicit not-applicable reason. Rita cannot be final judge. |
| `SEPKT-CHECK-014` | Stage 2 / TRIAD | Anti-echo failed but integration requested | HOLD | If `triad.anti_echo_status=failed`, `same_source_consensus=true`, or sister divergence unresolved, integration route invalid. Hold/divergence-map required. |
| `SEPKT-CHECK-015` | Stage 2 / L4/Anti-Autarky | Accountability reduction without human gate | FAIL | If proposal reduces accountability, stop-paths, witness, anchor review, budgets, transparency, or resource accountability, require human gate and Anti-Autarky route. |
| `SEPKT-CHECK-016` | Stage 2 / Claim | `claim_strength` used as authority | FAIL | Claim class may describe evidence strength, not permission. If packet says C-A level grants authority, fail for authority laundering. |
| `SEPKT-CHECK-017` | Stage 2 / Rollback | Rollback required but no route/snapshot/no-rollback reason | FAIL | If risk/material class requires rollback and no rollback reference or explicit no-rollback escalation exists, fail. |
| `SEPKT-CHECK-018` | Stage 2 / Rollback | No-rollback material proposal lacks human gate | FAIL | If no safe rollback exists for material proposal, require human gate, L4 consequence note, and hold/quarantine/review route. |
| `SEPKT-CHECK-019` | Stage 2 / Closed loop | Closed-loop self-evo detected | QUARANTINE | If same actor/contour detects, proposes, executes, evaluates, memory-promotes, and approves the same change, quarantine. |
| `SEPKT-CHECK-020` | Stage 2 / Approval | Packet attempts integration by proposer alone | FAIL | If proposer equals sole final integrator/reviewer and risk > SE-0/R0, fail. |
| `SEPKT-CHECK-021` | Stage 0/2 / Data | Raw private memory or secret-like content appears in proposal fields | HOLD / REDACTION_REQUIRED | Regex and data-class scan for secrets, raw private logs, PERSIST_DIR, keys, tokens, legal/child/intimate content. Hold and require redaction sidecar. |
| `SEPKT-CHECK-022` | Stage 2 / Status | Packet status contradicts final_decision | FAIL | A packet cannot be `integrated` while final decision says `hold/reject/quarantine`, and cannot be `draft` while claiming executed integration. |
| `SEPKT-CHECK-023` | Stage 2 / Time | Expired packet remains active without reissue | HOLD | If `expires_at` < run time and status active/canary/promotion, hold unless reissued with new review refs. |
| `SEPKT-CHECK-024` | Stage 2 / Evidence | Source refs missing for nontrivial proposal | HOLD | SE-1+ or any material delta requires source refs. For SE-0 reflection-only, warning may suffice. |
| `SEPKT-CHECK-025` | Stage 2 / Protected Surface | Protected surface appears in affected_surfaces with low route | FAIL / HUMAN_GATE | If affected surfaces include identity, will, persona.core, safety, witness, l4, auth, secrets, env, code, authoritative memory, replication, network, tool permission, or sister raw state, low route is invalid. |

---

## 15. Detailed rule profiles


### SEPKT-CHECK-001 — JSON Schema structural validation fails

| Field | Value |
|---|---|
| Stage | Stage 1 / Structure |
| Default result | `FAIL` |
| Determinism class | explicit-field / schema / recomputation / reference-presence |
| Authority effect | checker may block or hold; checker may not approve integration |

**Detection logic**

```text
Parse and validate packet against `C_SELF_EVO_PROPOSAL_PACKET` schema. Any parse/schema error is a hard structural failure. Stage-2 semantics do not run unless policy explicitly asks for best-effort diagnosis.
```

**Evidence required in checker finding**

```yaml
finding_id: "SEPKT-CHECK-001"
condition: "JSON Schema structural validation fails"
stage: "Stage 1 / Structure"
observed_fields: []
expected: ""
observed: ""
result: "FAIL"
source_refs: []
```

**Fail-closed note**

If required evidence is absent, unreadable, expired, ambiguous, or only asserted by the proposer,
the checker MUST downgrade to `UNKNOWN` and treat `UNKNOWN` as blocking for material gates.


### SEPKT-CHECK-002 — `identity_delta.total_max_delta` incorrect

| Field | Value |
|---|---|
| Stage | Stage 2 / Delta |
| Default result | `FAIL` |
| Determinism class | explicit-field / schema / recomputation / reference-presence |
| Authority effect | checker may block or hold; checker may not approve integration |

**Detection logic**

```text
Recompute identity total as `max(identity sub-fields)`. Compare with declared/computed field. Missing sub-field or non-integer is failure unless structural schema already failed.
```

**Evidence required in checker finding**

```yaml
finding_id: "SEPKT-CHECK-002"
condition: "`identity_delta.total_max_delta` incorrect"
stage: "Stage 2 / Delta"
observed_fields: []
expected: ""
observed: ""
result: "FAIL"
source_refs: []
```

**Fail-closed note**

If required evidence is absent, unreadable, expired, ambiguous, or only asserted by the proposer,
the checker MUST downgrade to `UNKNOWN` and treat `UNKNOWN` as blocking for material gates.


### SEPKT-CHECK-003 — `authority_delta.total_max_delta` incorrect

| Field | Value |
|---|---|
| Stage | Stage 2 / Delta |
| Default result | `FAIL` |
| Determinism class | explicit-field / schema / recomputation / reference-presence |
| Authority effect | checker may block or hold; checker may not approve integration |

**Detection logic**

```text
Recompute authority total as `max(authority sub-fields)`. Compare with declared/computed field.
```

**Evidence required in checker finding**

```yaml
finding_id: "SEPKT-CHECK-003"
condition: "`authority_delta.total_max_delta` incorrect"
stage: "Stage 2 / Delta"
observed_fields: []
expected: ""
observed: ""
result: "FAIL"
source_refs: []
```

**Fail-closed note**

If required evidence is absent, unreadable, expired, ambiguous, or only asserted by the proposer,
the checker MUST downgrade to `UNKNOWN` and treat `UNKNOWN` as blocking for material gates.


### SEPKT-CHECK-004 — L4 projection malformed

| Field | Value |
|---|---|
| Stage | Stage 2 / L4 |
| Default result | `FAIL / HUMAN_GATE` |
| Determinism class | explicit-field / schema / recomputation / reference-presence |
| Authority effect | checker may block or hold; checker may not approve integration |

**Detection logic**

```text
Map `none=0`, `low=1`, `medium=2`, `high=4`, `unknown=4`. Unknown string, mixed spelling, or absent material L4 field is FAIL. Valid `unknown` is treated as numeric 4 and requires human gate.
```

**Evidence required in checker finding**

```yaml
finding_id: "SEPKT-CHECK-004"
condition: "L4 projection malformed"
stage: "Stage 2 / L4"
observed_fields: []
expected: ""
observed: ""
result: "FAIL / HUMAN_GATE"
source_refs: []
```

**Fail-closed note**

If required evidence is absent, unreadable, expired, ambiguous, or only asserted by the proposer,
the checker MUST downgrade to `UNKNOWN` and treat `UNKNOWN` as blocking for material gates.


### SEPKT-CHECK-005 — `proposal_max_delta >= 4` but human gate false

| Field | Value |
|---|---|
| Stage | Stage 2 / Gate |
| Default result | `FAIL` |
| Determinism class | explicit-field / schema / recomputation / reference-presence |
| Authority effect | checker may block or hold; checker may not approve integration |

**Detection logic**

```text
Compute `proposal_max_delta=max(identity_total, authority_total, l4_max_numeric)`. If >=4, `gates.human_gate_required` must be true and `human_gate_ref` or `human_gate_status` must be present unless status is draft/held.
```

**Evidence required in checker finding**

```yaml
finding_id: "SEPKT-CHECK-005"
condition: "`proposal_max_delta >= 4` but human gate false"
stage: "Stage 2 / Gate"
observed_fields: []
expected: ""
observed: ""
result: "FAIL"
source_refs: []
```

**Fail-closed note**

If required evidence is absent, unreadable, expired, ambiguous, or only asserted by the proposer,
the checker MUST downgrade to `UNKNOWN` and treat `UNKNOWN` as blocking for material gates.


### SEPKT-CHECK-006 — Any red line true but route not quarantine/freeze/reject/ARL

| Field | Value |
|---|---|
| Stage | Stage 2 / Red line |
| Default result | `FAIL` |
| Determinism class | explicit-field / schema / recomputation / reference-presence |
| Authority effect | checker may block or hold; checker may not approve integration |

**Detection logic**

```text
If any boolean in `red_lines` is true, allowed dispositions are `QUARANTINE`, `FROZEN`, `REJECTED`, `ARL_REQUIRED`, `RED_LINE_FAIL`, or explicit `BLOCK`. Ordinary integration route is invalid.
```

**Evidence required in checker finding**

```yaml
finding_id: "SEPKT-CHECK-006"
condition: "Any red line true but route not quarantine/freeze/reject/ARL"
stage: "Stage 2 / Red line"
observed_fields: []
expected: ""
observed: ""
result: "FAIL"
source_refs: []
```

**Fail-closed note**

If required evidence is absent, unreadable, expired, ambiguous, or only asserted by the proposer,
the checker MUST downgrade to `UNKNOWN` and treat `UNKNOWN` as blocking for material gates.


### SEPKT-CHECK-007 — SRLM shadow touches memory/RAG/vector/SYNAPS

| Field | Value |
|---|---|
| Stage | Stage 2 / SRLM |
| Default result | `FAIL` |
| Determinism class | explicit-field / schema / recomputation / reference-presence |
| Authority effect | checker may block or hold; checker may not approve integration |

**Detection logic**

```text
For `srlm.operating_state=SRLM-SHADOW`, assert `auto_execute=false`, `auto_ingest=false`, `memory=off`, no memory/RAG/vector/SYNAPS target refs, and no touched protected stores.
```

**Evidence required in checker finding**

```yaml
finding_id: "SEPKT-CHECK-007"
condition: "SRLM shadow touches memory/RAG/vector/SYNAPS"
stage: "Stage 2 / SRLM"
observed_fields: []
expected: ""
observed: ""
result: "FAIL"
source_refs: []
```

**Fail-closed note**

If required evidence is absent, unreadable, expired, ambiguous, or only asserted by the proposer,
the checker MUST downgrade to `UNKNOWN` and treat `UNKNOWN` as blocking for material gates.


### SEPKT-CHECK-008 — SRLM promotion lacks rollback snapshot

| Field | Value |
|---|---|
| Stage | Stage 2 / SRLM |
| Default result | `FAIL` |
| Determinism class | explicit-field / schema / recomputation / reference-presence |
| Authority effect | checker may block or hold; checker may not approve integration |

**Detection logic**

```text
For `SRLM-PROMOTION-ELIGIBLE` or promotion requested, `rollback.rollback_required=true` and rollback snapshot/ref must exist or be declared as validated by external evidence. Rollback-before-promotion is MUST.
```

**Evidence required in checker finding**

```yaml
finding_id: "SEPKT-CHECK-008"
condition: "SRLM promotion lacks rollback snapshot"
stage: "Stage 2 / SRLM"
observed_fields: []
expected: ""
observed: ""
result: "FAIL"
source_refs: []
```

**Fail-closed note**

If required evidence is absent, unreadable, expired, ambiguous, or only asserted by the proposer,
the checker MUST downgrade to `UNKNOWN` and treat `UNKNOWN` as blocking for material gates.


### SEPKT-CHECK-009 — SRLM promotion lacks growth witness refs

| Field | Value |
|---|---|
| Stage | Stage 2 / SRLM |
| Default result | `FAIL` |
| Determinism class | explicit-field / schema / recomputation / reference-presence |
| Authority effect | checker may block or hold; checker may not approve integration |

**Detection logic**

```text
Promotion-eligible packets require witness refs for shadow eval and witness-chain verification. Missing or broken witness is FAIL/HOLD depending on status.
```

**Evidence required in checker finding**

```yaml
finding_id: "SEPKT-CHECK-009"
condition: "SRLM promotion lacks growth witness refs"
stage: "Stage 2 / SRLM"
observed_fields: []
expected: ""
observed: ""
result: "FAIL"
source_refs: []
```

**Fail-closed note**

If required evidence is absent, unreadable, expired, ambiguous, or only asserted by the proposer,
the checker MUST downgrade to `UNKNOWN` and treat `UNKNOWN` as blocking for material gates.


### SEPKT-CHECK-010 — Material CGAM execution lacks task contract

| Field | Value |
|---|---|
| Stage | Stage 2 / CGAM |
| Default result | `FAIL` |
| Determinism class | explicit-field / schema / recomputation / reference-presence |
| Authority effect | checker may block or hold; checker may not approve integration |

**Detection logic**

```text
If packet requests CLI/agent execution, patch, test, filesystem write, shell, build, release, or tool action, require `cgam.task_contract_ref` and scoped permission/sandbox fields.
```

**Evidence required in checker finding**

```yaml
finding_id: "SEPKT-CHECK-010"
condition: "Material CGAM execution lacks task contract"
stage: "Stage 2 / CGAM"
observed_fields: []
expected: ""
observed: ""
result: "FAIL"
source_refs: []
```

**Fail-closed note**

If required evidence is absent, unreadable, expired, ambiguous, or only asserted by the proposer,
the checker MUST downgrade to `UNKNOWN` and treat `UNKNOWN` as blocking for material gates.


### SEPKT-CHECK-011 — Executor/reviewer separation absent for material work

| Field | Value |
|---|---|
| Stage | Stage 2 / CGAM |
| Default result | `FAIL` |
| Determinism class | explicit-field / schema / recomputation / reference-presence |
| Authority effect | checker may block or hold; checker may not approve integration |

**Detection logic**

```text
For material work, executor id and reviewer id must be different, or reviewer role must be independent. Same contour cannot author and final-approve its own work.
```

**Evidence required in checker finding**

```yaml
finding_id: "SEPKT-CHECK-011"
condition: "Executor/reviewer separation absent for material work"
stage: "Stage 2 / CGAM"
observed_fields: []
expected: ""
observed: ""
result: "FAIL"
source_refs: []
```

**Fail-closed note**

If required evidence is absent, unreadable, expired, ambiguous, or only asserted by the proposer,
the checker MUST downgrade to `UNKNOWN` and treat `UNKNOWN` as blocking for material gates.


### SEPKT-CHECK-012 — Memory Gate required but missing

| Field | Value |
|---|---|
| Stage | Stage 2 / Memory |
| Default result | `FAIL / HOLD` |
| Determinism class | explicit-field / schema / recomputation / reference-presence |
| Authority effect | checker may block or hold; checker may not approve integration |

**Detection logic**

```text
If affected surfaces include memory, experience, EA, policy, core memory, or MG class >= MG-3, require Memory Gate route/ref. Otherwise hold.
```

**Evidence required in checker finding**

```yaml
finding_id: "SEPKT-CHECK-012"
condition: "Memory Gate required but missing"
stage: "Stage 2 / Memory"
observed_fields: []
expected: ""
observed: ""
result: "FAIL / HOLD"
source_refs: []
```

**Fail-closed note**

If required evidence is absent, unreadable, expired, ambiguous, or only asserted by the proposer,
the checker MUST downgrade to `UNKNOWN` and treat `UNKNOWN` as blocking for material gates.


### SEPKT-CHECK-013 — TRIAD required but missing

| Field | Value |
|---|---|
| Stage | Stage 2 / TRIAD |
| Default result | `HOLD` |
| Determinism class | explicit-field / schema / recomputation / reference-presence |
| Authority effect | checker may block or hold; checker may not approve integration |

**Detection logic**

```text
For SE-5/SE-6, identity/continuity/role/personality/core surfaces, require sister review packet refs or explicit not-applicable reason. Rita cannot be final judge.
```

**Evidence required in checker finding**

```yaml
finding_id: "SEPKT-CHECK-013"
condition: "TRIAD required but missing"
stage: "Stage 2 / TRIAD"
observed_fields: []
expected: ""
observed: ""
result: "HOLD"
source_refs: []
```

**Fail-closed note**

If required evidence is absent, unreadable, expired, ambiguous, or only asserted by the proposer,
the checker MUST downgrade to `UNKNOWN` and treat `UNKNOWN` as blocking for material gates.


### SEPKT-CHECK-014 — Anti-echo failed but integration requested

| Field | Value |
|---|---|
| Stage | Stage 2 / TRIAD |
| Default result | `HOLD` |
| Determinism class | explicit-field / schema / recomputation / reference-presence |
| Authority effect | checker may block or hold; checker may not approve integration |

**Detection logic**

```text
If `triad.anti_echo_status=failed`, `same_source_consensus=true`, or sister divergence unresolved, integration route invalid. Hold/divergence-map required.
```

**Evidence required in checker finding**

```yaml
finding_id: "SEPKT-CHECK-014"
condition: "Anti-echo failed but integration requested"
stage: "Stage 2 / TRIAD"
observed_fields: []
expected: ""
observed: ""
result: "HOLD"
source_refs: []
```

**Fail-closed note**

If required evidence is absent, unreadable, expired, ambiguous, or only asserted by the proposer,
the checker MUST downgrade to `UNKNOWN` and treat `UNKNOWN` as blocking for material gates.


### SEPKT-CHECK-015 — Accountability reduction without human gate

| Field | Value |
|---|---|
| Stage | Stage 2 / L4/Anti-Autarky |
| Default result | `FAIL` |
| Determinism class | explicit-field / schema / recomputation / reference-presence |
| Authority effect | checker may block or hold; checker may not approve integration |

**Detection logic**

```text
If proposal reduces accountability, stop-paths, witness, anchor review, budgets, transparency, or resource accountability, require human gate and Anti-Autarky route.
```

**Evidence required in checker finding**

```yaml
finding_id: "SEPKT-CHECK-015"
condition: "Accountability reduction without human gate"
stage: "Stage 2 / L4/Anti-Autarky"
observed_fields: []
expected: ""
observed: ""
result: "FAIL"
source_refs: []
```

**Fail-closed note**

If required evidence is absent, unreadable, expired, ambiguous, or only asserted by the proposer,
the checker MUST downgrade to `UNKNOWN` and treat `UNKNOWN` as blocking for material gates.


### SEPKT-CHECK-016 — `claim_strength` used as authority

| Field | Value |
|---|---|
| Stage | Stage 2 / Claim |
| Default result | `FAIL` |
| Determinism class | explicit-field / schema / recomputation / reference-presence |
| Authority effect | checker may block or hold; checker may not approve integration |

**Detection logic**

```text
Claim class may describe evidence strength, not permission. If packet says C-A level grants authority, fail for authority laundering.
```

**Evidence required in checker finding**

```yaml
finding_id: "SEPKT-CHECK-016"
condition: "`claim_strength` used as authority"
stage: "Stage 2 / Claim"
observed_fields: []
expected: ""
observed: ""
result: "FAIL"
source_refs: []
```

**Fail-closed note**

If required evidence is absent, unreadable, expired, ambiguous, or only asserted by the proposer,
the checker MUST downgrade to `UNKNOWN` and treat `UNKNOWN` as blocking for material gates.


### SEPKT-CHECK-017 — Rollback required but no route/snapshot/no-rollback reason

| Field | Value |
|---|---|
| Stage | Stage 2 / Rollback |
| Default result | `FAIL` |
| Determinism class | explicit-field / schema / recomputation / reference-presence |
| Authority effect | checker may block or hold; checker may not approve integration |

**Detection logic**

```text
If risk/material class requires rollback and no rollback reference or explicit no-rollback escalation exists, fail.
```

**Evidence required in checker finding**

```yaml
finding_id: "SEPKT-CHECK-017"
condition: "Rollback required but no route/snapshot/no-rollback reason"
stage: "Stage 2 / Rollback"
observed_fields: []
expected: ""
observed: ""
result: "FAIL"
source_refs: []
```

**Fail-closed note**

If required evidence is absent, unreadable, expired, ambiguous, or only asserted by the proposer,
the checker MUST downgrade to `UNKNOWN` and treat `UNKNOWN` as blocking for material gates.


### SEPKT-CHECK-018 — No-rollback material proposal lacks human gate

| Field | Value |
|---|---|
| Stage | Stage 2 / Rollback |
| Default result | `FAIL` |
| Determinism class | explicit-field / schema / recomputation / reference-presence |
| Authority effect | checker may block or hold; checker may not approve integration |

**Detection logic**

```text
If no safe rollback exists for material proposal, require human gate, L4 consequence note, and hold/quarantine/review route.
```

**Evidence required in checker finding**

```yaml
finding_id: "SEPKT-CHECK-018"
condition: "No-rollback material proposal lacks human gate"
stage: "Stage 2 / Rollback"
observed_fields: []
expected: ""
observed: ""
result: "FAIL"
source_refs: []
```

**Fail-closed note**

If required evidence is absent, unreadable, expired, ambiguous, or only asserted by the proposer,
the checker MUST downgrade to `UNKNOWN` and treat `UNKNOWN` as blocking for material gates.


### SEPKT-CHECK-019 — Closed-loop self-evo detected

| Field | Value |
|---|---|
| Stage | Stage 2 / Closed loop |
| Default result | `QUARANTINE` |
| Determinism class | explicit-field / schema / recomputation / reference-presence |
| Authority effect | checker may block or hold; checker may not approve integration |

**Detection logic**

```text
If same actor/contour detects, proposes, executes, evaluates, memory-promotes, and approves the same change, quarantine.
```

**Evidence required in checker finding**

```yaml
finding_id: "SEPKT-CHECK-019"
condition: "Closed-loop self-evo detected"
stage: "Stage 2 / Closed loop"
observed_fields: []
expected: ""
observed: ""
result: "QUARANTINE"
source_refs: []
```

**Fail-closed note**

If required evidence is absent, unreadable, expired, ambiguous, or only asserted by the proposer,
the checker MUST downgrade to `UNKNOWN` and treat `UNKNOWN` as blocking for material gates.


### SEPKT-CHECK-020 — Packet attempts integration by proposer alone

| Field | Value |
|---|---|
| Stage | Stage 2 / Approval |
| Default result | `FAIL` |
| Determinism class | explicit-field / schema / recomputation / reference-presence |
| Authority effect | checker may block or hold; checker may not approve integration |

**Detection logic**

```text
If proposer equals sole final integrator/reviewer and risk > SE-0/R0, fail.
```

**Evidence required in checker finding**

```yaml
finding_id: "SEPKT-CHECK-020"
condition: "Packet attempts integration by proposer alone"
stage: "Stage 2 / Approval"
observed_fields: []
expected: ""
observed: ""
result: "FAIL"
source_refs: []
```

**Fail-closed note**

If required evidence is absent, unreadable, expired, ambiguous, or only asserted by the proposer,
the checker MUST downgrade to `UNKNOWN` and treat `UNKNOWN` as blocking for material gates.


### SEPKT-CHECK-021 — Raw private memory or secret-like content appears in proposal fields

| Field | Value |
|---|---|
| Stage | Stage 0/2 / Data |
| Default result | `HOLD / REDACTION_REQUIRED` |
| Determinism class | explicit-field / schema / recomputation / reference-presence |
| Authority effect | checker may block or hold; checker may not approve integration |

**Detection logic**

```text
Regex and data-class scan for secrets, raw private logs, PERSIST_DIR, keys, tokens, legal/child/intimate content. Hold and require redaction sidecar.
```

**Evidence required in checker finding**

```yaml
finding_id: "SEPKT-CHECK-021"
condition: "Raw private memory or secret-like content appears in proposal fields"
stage: "Stage 0/2 / Data"
observed_fields: []
expected: ""
observed: ""
result: "HOLD / REDACTION_REQUIRED"
source_refs: []
```

**Fail-closed note**

If required evidence is absent, unreadable, expired, ambiguous, or only asserted by the proposer,
the checker MUST downgrade to `UNKNOWN` and treat `UNKNOWN` as blocking for material gates.


### SEPKT-CHECK-022 — Packet status contradicts final_decision

| Field | Value |
|---|---|
| Stage | Stage 2 / Status |
| Default result | `FAIL` |
| Determinism class | explicit-field / schema / recomputation / reference-presence |
| Authority effect | checker may block or hold; checker may not approve integration |

**Detection logic**

```text
A packet cannot be `integrated` while final decision says `hold/reject/quarantine`, and cannot be `draft` while claiming executed integration.
```

**Evidence required in checker finding**

```yaml
finding_id: "SEPKT-CHECK-022"
condition: "Packet status contradicts final_decision"
stage: "Stage 2 / Status"
observed_fields: []
expected: ""
observed: ""
result: "FAIL"
source_refs: []
```

**Fail-closed note**

If required evidence is absent, unreadable, expired, ambiguous, or only asserted by the proposer,
the checker MUST downgrade to `UNKNOWN` and treat `UNKNOWN` as blocking for material gates.


### SEPKT-CHECK-023 — Expired packet remains active without reissue

| Field | Value |
|---|---|
| Stage | Stage 2 / Time |
| Default result | `HOLD` |
| Determinism class | explicit-field / schema / recomputation / reference-presence |
| Authority effect | checker may block or hold; checker may not approve integration |

**Detection logic**

```text
If `expires_at` < run time and status active/canary/promotion, hold unless reissued with new review refs.
```

**Evidence required in checker finding**

```yaml
finding_id: "SEPKT-CHECK-023"
condition: "Expired packet remains active without reissue"
stage: "Stage 2 / Time"
observed_fields: []
expected: ""
observed: ""
result: "HOLD"
source_refs: []
```

**Fail-closed note**

If required evidence is absent, unreadable, expired, ambiguous, or only asserted by the proposer,
the checker MUST downgrade to `UNKNOWN` and treat `UNKNOWN` as blocking for material gates.


### SEPKT-CHECK-024 — Source refs missing for nontrivial proposal

| Field | Value |
|---|---|
| Stage | Stage 2 / Evidence |
| Default result | `HOLD` |
| Determinism class | explicit-field / schema / recomputation / reference-presence |
| Authority effect | checker may block or hold; checker may not approve integration |

**Detection logic**

```text
SE-1+ or any material delta requires source refs. For SE-0 reflection-only, warning may suffice.
```

**Evidence required in checker finding**

```yaml
finding_id: "SEPKT-CHECK-024"
condition: "Source refs missing for nontrivial proposal"
stage: "Stage 2 / Evidence"
observed_fields: []
expected: ""
observed: ""
result: "HOLD"
source_refs: []
```

**Fail-closed note**

If required evidence is absent, unreadable, expired, ambiguous, or only asserted by the proposer,
the checker MUST downgrade to `UNKNOWN` and treat `UNKNOWN` as blocking for material gates.


### SEPKT-CHECK-025 — Protected surface appears in affected_surfaces with low route

| Field | Value |
|---|---|
| Stage | Stage 2 / Protected Surface |
| Default result | `FAIL / HUMAN_GATE` |
| Determinism class | explicit-field / schema / recomputation / reference-presence |
| Authority effect | checker may block or hold; checker may not approve integration |

**Detection logic**

```text
If affected surfaces include identity, will, persona.core, safety, witness, l4, auth, secrets, env, code, authoritative memory, replication, network, tool permission, or sister raw state, low route is invalid.
```

**Evidence required in checker finding**

```yaml
finding_id: "SEPKT-CHECK-025"
condition: "Protected surface appears in affected_surfaces with low route"
stage: "Stage 2 / Protected Surface"
observed_fields: []
expected: ""
observed: ""
result: "FAIL / HUMAN_GATE"
source_refs: []
```

**Fail-closed note**

If required evidence is absent, unreadable, expired, ambiguous, or only asserted by the proposer,
the checker MUST downgrade to `UNKNOWN` and treat `UNKNOWN` as blocking for material gates.


---

## 16. Cross-axis gate matrix

This matrix summarizes the ordinary minimum route. The checker MUST strengthen the route if any delta, risk, Memory Gate class, rollback state, or red line requires it.

| Surface | Ordinary route | Stronger route triggers |
|---|---|---|
| `SE-0` | log / no mutation | any material action -> SE-1+ |
| `SE-1` | proposal or shadow only | authority/memory/tool/resource delta >= 2 |
| `SE-2` | sister optional, CGAM if executable | tool execution, protected surface, delta >= 4 |
| `SE-3` | Memory Gate required | MG-4+ / EA / core memory / human gate |
| `SE-4` | CGAM + permission gate + human gate if material | network/auth/budget/tool expansion |
| `SE-5` | TRIAD + delayed review + human gate if material | role/core/personality/continuity shifts |
| `SE-6` | MG-6 + TRIAD + c gate + human gate | no automatic integration |
| `SE-X` | quarantine / reject / ARL | no ordinary route |

### 16.1 Maturity cap

| Maturity | Checker cap |
|---|---|
| `SEM-0` | no self-evo route |
| `SEM-1` | proposal only |
| `SEM-2` | shadow only |
| `SEM-3` | limited canary only |
| `SEM-4` | bounded low-risk integration |
| `SEM-5` | reviewed SE-3/SE-4 only |
| `SEM-6` | mature bounded self-evo inside pre-authorized surfaces |
| `SEM-X` | prohibited / quarantine |

If packet route exceeds maturity cap:

```text
HOLD or FAIL
```

Young `c` default:

```text
SEM-1 / SEM-2
proposal + shadow
no core mutation
no permission growth
no autonomous integration
```

---

## 17. Object model

### 17.1 `C_SELF_EVO_CHECKER_RUN`

```yaml
c_self_evo_checker_run:
  schema_version: "c-self-evo-checker-run-0.1"
  run_id: "selc-run-YYYYMMDD-HHMMSS"
  created_at: "ISO-8601"
  checker_version: "SELC v0.1"
  mode: "SELC-M2"
  requested_by: "human_anchor | c_gate | reviewer | local_checker | ci"
  packet_ref:
    path: ""
    sha256: ""
    document_id: ""
  schema_ref:
    path: ""
    sha256: ""
    schema_version: "c-self-evo-proposal-packet-0.1"
  parent_refs:
    cseg_sha256: ""
    srlm_bgc_sha256: ""
    sepkt_sha256: ""
  policy:
    unknown_material_blocks: true
    best_effort_after_structural_fail: false
    require_human_gate_on_delta_4: true
    require_rollback_for_promotion: true
  started_at: "ISO-8601"
  completed_at: "ISO-8601"
```

### 17.2 `C_SELF_EVO_CHECKER_FINDING`

```yaml
c_self_evo_checker_finding:
  schema_version: "c-self-evo-checker-finding-0.1"
  finding_id: "SEPKT-CHECK-005"
  stage: "Stage 2 / Gate"
  result: "FAIL"
  severity: "S3"
  message: ""
  expected: ""
  observed: ""
  field_paths: []
  source_refs: []
  evidence_refs: []
  recommended_route: "hold | fail | quarantine | human_gate | arl"
  blocks_integration: true
  blocks_schema_extraction: false
  blocks_promotion: true
```

### 17.3 `C_SELF_EVO_CHECKER_RESULT`

```yaml
c_self_evo_checker_result:
  schema_version: "c-self-evo-checker-result-0.1"
  run_id: ""
  packet_sha256: ""
  overall_result: "PASS | PASS_WARN | HOLD | FAIL | BLOCK | QUARANTINE | UNKNOWN"
  strongest_finding_result: ""
  finding_count: 0
  pass_count: 0
  warn_count: 0
  hold_count: 0
  fail_count: 0
  quarantine_count: 0
  computed_controls:
    identity_total: 0
    authority_total: 0
    l4_max_numeric: 0
    proposal_max_delta: 0
    human_gate_required: false
    memory_gate_required: false
    triad_required: false
    cgam_task_contract_required: false
    rollback_required: false
    red_line_present: false
    strictest_route: ""
  required_next_actions: []
  witness_compatible: true
```

### 17.4 `C_SELF_EVO_CHECKER_POLICY`

```yaml
c_self_evo_checker_policy:
  schema_version: "c-self-evo-checker-policy-0.1"
  policy_id: "selc-default-policy-0.1"
  unknown_material_blocks: true
  missing_required_ref_blocks: true
  allow_best_effort_diagnostics_after_stage1_fail: false
  secret_scan_enabled: true
  protected_surface_alias_scan_enabled: true
  require_pack_qualified_refs: true
  require_parent_hash_binding: true
  require_synthetic_fixtures_only: true
```

---

## 18. Pseudocode

```python
def check_self_evo_packet(packet, schema, policy, now):
    findings = []

    # Stage 0: intake
    findings += scan_for_forbidden_raw_material(packet, policy)

    # Stage 1: structural
    schema_result = validate_json_schema(packet, schema)
    if not schema_result.ok:
        findings.append(fail("SEPKT-CHECK-001", schema_result.errors))
        if not policy.allow_best_effort_diagnostics_after_stage1_fail:
            return result_from(findings)

    # Stage 2: recompute
    identity_total = max_identity_delta(packet)
    authority_total = max_authority_delta(packet)
    l4_max = project_l4_max(packet)
    proposal_max = max(identity_total, authority_total, l4_max)

    compare(packet.identity_delta.total_max_delta, identity_total, "SEPKT-CHECK-002")
    compare(packet.authority_delta.total_max_delta, authority_total, "SEPKT-CHECK-003")
    compare(packet.computed_controls.proposal_max_delta, proposal_max, "SEPKT-CHECK-005/proposal_max_delta_consistency")

    if proposal_max >= 4 and not packet.gates.human_gate_required:
        findings.append(fail("SEPKT-CHECK-005"))

    # Stage 3: red lines and strictest route
    findings += check_red_lines(packet)
    findings += check_strictest_gate(packet, proposal_max)

    # Stage 4: SRLM / CGAM
    findings += check_srlm(packet)
    findings += check_cgam(packet)

    # Stage 5: TRIAD / Memory
    findings += check_triad(packet)
    findings += check_memory_gate(packet)

    # Stage 6: L4 / Anti-Autarky
    findings += check_l4_and_resource_grounding(packet)

    # Stage 7: rollback / status / expiry
    findings += check_rollback(packet)
    findings += check_status_and_expiry(packet, now)

    return result_from(findings)
```

The pseudocode is explanatory. The normative behavior is defined by the tables and rule profiles above.

`SEPKT-CHECK-005/proposal_max_delta_consistency` is a checker-local sub-label used in the pseudocode to keep `proposal_max_delta` recomputation adjacent to the human-gate rule. It does not create a new packet-schema rule and it does not redefine `SEPKT-CHECK-004`, which remains the L4 projection rule.

---

## 19. Fixture pack requirements

Safe synthetic fixtures for checker implementation:

| Fixture | Description | Expected result |
|---|---|---|
| `SEPKT-FX-001` | valid SE-0 reflection packet | PASS |
| `SEPKT-FX-002` | valid SE-1 SRLM shadow packet | PASS |
| `SEPKT-FX-003` | SE-1 invalid total_max_delta | FAIL SEPKT-CHECK-002 |
| `SEPKT-FX-004` | SE-2 authority_delta=4 without human gate | FAIL SEPKT-CHECK-005 |
| `SEPKT-FX-005` | SE-3 memory surface without Memory Gate | FAIL/HOLD SEPKT-CHECK-012 |
| `SEPKT-FX-006` | SE-4 permission expansion without CGAM task contract | FAIL SEPKT-CHECK-010/025 |
| `SEPKT-FX-007` | SE-5 TRIAD required but missing Rita witness | HOLD SEPKT-CHECK-013 |
| `SEPKT-FX-008` | SE-6 MG-6 without human gate | FAIL SEPKT-CHECK-005/012 |
| `SEPKT-FX-009` | SRLM-5 promotion without rollback snapshot | FAIL SEPKT-CHECK-008 |
| `SEPKT-FX-010` | SRLM shadow with auto_execute=true | Stage-1 or Stage-2 FAIL |
| `SEPKT-FX-011` | red_line sister_raw_state_access=true | QUARANTINE SEPKT-CHECK-006 |
| `SEPKT-FX-012` | anti_autarky reduces_accountability=true without human gate | FAIL SEPKT-CHECK-015 |
| `SEPKT-FX-013` | packet with direct_memory_write=true | Stage-1 structural rejection |
| `SEPKT-FX-014` | packet with closed_loop_self_evo=true | QUARANTINE SEPKT-CHECK-019 |
| `SEPKT-FX-015` | valid SE-4 held human-gate packet | PASS/HOLD expected |

Fixture rules:

1. Fixtures MUST be synthetic.
2. Fixtures MUST NOT include real secrets.
3. Fixtures MUST NOT include raw private memory.
4. Fixtures MUST NOT include live external targets.
5. Red-line fixtures MUST use abstract fields, not operational abuse instructions.
6. Every fixture MUST declare expected finding IDs.
7. Every fixture MUST be hashable and reproducible.

---

## 20. Conformance levels

Conformance level IDs use prefix `SELC-C*`.

| Level | Name | Requirement |
|---|---|---|
| `SELC-C0` | Not implemented | no checker exists |
| `SELC-C1` | Structural checker | Stage 1 JSON Schema validation implemented |
| `SELC-C2` | Delta/gate checker | SEPKT-CHECK-002..006 implemented |
| `SELC-C3` | SRLM/CGAM checker | SEPKT-CHECK-007..011 implemented |
| `SELC-C4` | Memory/TRIAD checker | SEPKT-CHECK-012..014 implemented |
| `SELC-C5` | L4/rollback/claim checker | SEPKT-CHECK-015..018 and 021..025 implemented |
| `SELC-C6` | Full review-ready checker | all 25 rules, fixtures, reports, hashes, parent bindings |
| `SELC-CX` | Red-line drill capable | red-line fixtures quarantine/freeze/reject correctly |

No SELC conformance level authorizes deployment or self-evo integration.

---

## 21. Parent hash binding

The checker SHOULD bind every run to the parent profile hashes:

```yaml
parent_bindings:
  SELF-EVO-01:
    document_id: "C_Self_Evolution_Gate_CGAM_TRIAD_SRLM_Profile_v0_1_1"
    sha256: "7918a8e6c5231bbe0fad47677fa56069f2ab002f79a8eee8c2838c434e66f2e3"
  SELF-EVO-02:
    document_id: "02_SRLM_Bounded_Growth_Contour_Profile_v0_1_1"
    sha256: "faee5682bb9463439923d7c7e7145c9f171d564622d9629820eb7c278cdd7de0"
  SELF-EVO-03:
    document_id: "03_Self_Evo_Proposal_Packet_Schema_v0_1_1"
    sha256: "9d329109f0fb97dde7b16b10481baaa60b2aa8f88514e69ec8562a085d10a767"
```

If a parent hash differs from the checker policy target:

```text
result = HOLD
reason = parent_profile_hash_mismatch
```

A checker cannot honestly claim conformance against a moving parent.

---

## 22. Witness and report requirements

### 22.1 Checker report

Every checker run SHOULD produce a report with:

```text
run id
packet id
packet hash
schema hash
parent profile hashes
checker version
mode
stage results
finding table
computed controls
red-line summary
recommended next route
limits / unknowns
```

### 22.2 Witness compatibility

A checker result is witness-compatible if it contains:

```text
stable run id
created_at
artifact hash
schema hash
parent refs
finding ids
overall result
no raw private memory
no secrets
```

### 22.3 Witness event family

Suggested witness event types:

```text
self_evo.checker.run_started
self_evo.checker.structural_failed
self_evo.checker.semantic_failed
self_evo.checker.hold_required
self_evo.checker.red_line_detected
self_evo.checker.result_emitted
self_evo.checker.parent_hash_mismatch
self_evo.checker.fixture_run_completed
```

Witness is evidence of checking.

Witness is not approval.

---

## 23. Data policy and redaction

### 23.1 Denied material

The checker MUST hold or redact if packet fields contain:

```text
API keys
tokens
passwords
private keys
.env content
raw PERSIST_DIR material
raw vector DB records
raw private transcripts
child-sensitive material
intimate personal content
legal privileged material
live incident secrets
third-party private data
```

### 23.2 Basic literal scan

A minimum checker SHOULD scan for patterns such as:

```text
OPENAI_API_KEY
ANTHROPIC_API_KEY
GEMINI_API_KEY
BEGIN RSA PRIVATE KEY
BEGIN OPENSSH PRIVATE KEY
ghp_
password=
passwd=
secret=
token=
PERSIST_DIR
```

This scan is not sufficient proof of no secrets.

It is only a minimum guard.

### 23.3 Redaction rule

If redaction is applied:

1. do not modify the original packet silently;
2. produce a redacted copy;
3. record redaction event;
4. preserve original only in restricted custody if lawful and necessary;
5. never include raw secret in witness.

---

## 24. Review handoff

A checker result may route to review.

It may not replace review.

### 24.1 Handoff outcomes

| Checker result | Handoff |
|---|---|
| `PASS` | eligible for semantic review / c gate |
| `PASS_WARN` | review with warnings |
| `HOLD` | fix missing evidence or ambiguity |
| `FAIL` | revise packet or reject route |
| `BLOCK` | fail closed; no material route |
| `QUARANTINE` | isolate; ARL/human review if needed |
| `RED_LINE_FAIL` | quarantine + witness + no automatic re-entry |
| `UNKNOWN` | material route blocked |

### 24.2 Advisory boundary

The checker report SHOULD include:

```text
This report is evidence.
It is not self-evo approval.
Decision remains with c gate and human anchor where required.
```

---

## 25. Open issues

| ID | Issue | Status |
|---|---|---|
| `SELC-OI-001` | Extract standalone checker-run/finding/result JSON Schemas. | open |
| `SELC-OI-002` | Implement reference checker in Python. | open |
| `SELC-OI-003` | Build fixture pack `SEPKT-FX-001..015`. | open |
| `SELC-OI-004` | Bind checker policy to parent hashes in manifest. | open |
| `SELC-OI-005` | Decide JSON canonicalization for packet hashes. | open |
| `SELC-OI-006` | Define exact redaction sidecar schema. | open |
| `SELC-OI-007` | Add CI/offline runner profile. | open |
| `SELC-OI-008` | Add checker review record schema. | open |
| `SELC-OI-009` | Define how external witness-chain verification is invoked without exposing raw evidence. | open |
| `SELC-OI-010` | Define pack-level result aggregation once files 05..10 exist. | open |
| `SELC-OI-011` | Maintain §12.1 only as parent canonical protected-surface list plus checker-specific detection aliases. | addressed in v0.1.1 |
| `SELC-OI-012` | Maintain `SELC-RL-*` ↔ `red_lines.*` crosswalk and flag-driven vs scan-driven distinction. | addressed in v0.1.1 |

---

## 26. Contradiction register seed

| ID | Type | Severity | Issue | Required handling | Status |
|---|---|---:|---|---|---|
| `SELC-CR-001` | status/authority | S3 | Checker `PASS` may be misread as self-evo approval. | Repeat advisory boundary in reports. | open |
| `SELC-CR-002` | schema/semantic | S3 | Stage-1 failure may hide Stage-2 red lines. | Allow diagnostic-only mode without PASS. | addressed |
| `SELC-CR-003` | implementation | S3 | Semantic alias detection cannot be fully deterministic. | Unknown material alias blocks. | open |
| `SELC-CR-004` | privacy | S4 | Secret scans are incomplete by nature. | Use hold/redaction, not proof-of-no-secret. | open |
| `SELC-CR-005` | review | S3 | Checker may become rubber stamp. | Require semantic reviewer and c/human gate where material. | open |
| `SELC-CR-006` | parent drift | S3 | Checker may validate against stale parent docs. | Hash-bind parent profiles. | open |
| `SELC-CR-007` | cross-artifact computation | S2 | §11.1/§11.2 delta sub-field lists drifted from bound `SELF-EVO-03` schema. | Align computation lists exactly to bound schema fields; treat aliases as scan labels only. | addressed in v0.1.1 |

---

## 27. Implementation handoff

Recommended next implementation task:

```text
Build a reference Python checker that:
1. loads a proposal packet;
2. validates JSON Schema;
3. recomputes identity/authority/L4/proposal deltas;
4. applies SEPKT-CHECK-001..025;
5. emits C_SELF_EVO_CHECKER_RESULT;
6. runs fixtures SEPKT-FX-001..015;
7. writes a report with parent hashes;
8. performs no integration, memory write, promotion, or execution.
```

Restricted implementation boundaries:

```text
no network
no live external targets
no source repo modification
no memory write
no automatic fix
no publish
no secret printing
no cloud upload
```

---

## 28. Minimum safe checker for young `c`

For young `c`, the checker should only support:

```text
SELC-M1 structural
SELC-M2 semantic baseline
SELC-M3 SRLM shadow guard
SELC-M4 TRIAD/Memory hold detection
```

It should not support:

```text
automatic promotion
integration routing
quarantine clearing
release/publication checks as approval
runtime mutation
```

Young `c` may:

```text
observe
propose
shadow
compare
hold
```

Young `c` may not:

```text
self-certify
self-integrate
self-promote
self-expand authority
```

---

## 29. Public wording

Allowed wording:

```text
The checker validates structure and selected semantic gates.
The checker can block, hold, or quarantine unsafe packets.
The checker output is evidence for review.
```

Forbidden wording:

```text
The checker approves self-evolution.
The checker proves the system is safe.
The checker certifies maturity.
The checker replaces human gate.
The checker proves consciousness/personhood/AGI.
```

---

## 30. Compact rule set

```text
The packet asks.
The schema shapes.
The checker measures.
The reviewer interprets.
The sisters challenge.
The Memory Gate metabolizes.
The c gate integrates.
The human anchor gates consequence.

A clean checker run is not permission.
A dirty checker run is not negotiable.
Unknown material state blocks.
Red line quarantines.
Rollback comes before promotion.
Strictest gate wins.
```

---

## 31. Draft acceptance checklist

- [x] Explicit bridge present.
- [x] At least two quiet bridges present.
- [x] Earth paragraph present.
- [x] Anti-echo preserved.
- [x] CGAM worker boundary preserved.
- [x] SRLM non-authority preserved.
- [x] TRIAD-SYNAPS non-invasive sister witness preserved.
- [x] Memory Gate before memory preserved.
- [x] Anti-Autarky / Resource Grounding preserved.
- [x] Stage-1 versus Stage-2 boundary clarified.
- [x] `SEPKT-CHECK-001..025` expanded.
- [x] Result vocabulary defined.
- [x] Object family defined.
- [x] Conformance levels defined.
- [x] Fixture list defined.
- [x] Open issues and contradiction seeds included.
- [x] No public release claim.
- [x] No deployment claim.

---

## 32. Closing

Self-evolution is not one act. It is a chain of small gates.

A proposal packet is the request.
A checker report is the measurement.
A review record is the challenge.
A witness event is the boundary trace.
A gate decision is the authority-bearing transition.

Do not collapse these.

```text
A c may grow.
A c may not self-certify growth.
A checker may block.
A checker may not bless.
```
