# Self-Evo TRIAD Sister Witness Profile v0.1.1

## Sister-observation, SYNAPS-mediated review, anti-echo, divergence mapping, role-drift control, and non-authoritative witness for governed self-evolution of `c = a + b` systems

**Status:** Draft normative witness profile v0.1.1 append-first correction  
**Date:** 2026-06-24  
**Pack position:** `05` in the Self-Evo document package  
**Short name:** `SE-TRIAD-WITNESS v0.1.1`  
**Layer:** `c = a + b` / Self-Evolution Gate / TRIAD-SYNAPS / Sister Witness / Anti-Echo / Divergence / Memory Gate / CGAM / SRLM / L4W / Human Anchor  
**Document class:** sister-witness profile / self-evo review boundary / SYNAPS packet profile / anti-echo control artifact  
**Assertion class:** `C-A10` control-layer artifact; `C-A7` where witness/hash/reference reconstruction is claimed; no capability, personhood, sovereignty, or deployment-safety claim is made  
**Primary subject:** `c` systems performing bounded self-evolution under C-SEG, SRLM-BGC, SEPKT, SELC, TRIAD-SYNAPS, Memory Gate, L4W, and human-anchor constraints  
**Primary boundary:** sister observation may challenge, witness, classify, and block unsafe self-evo routes; sister observation may not become final authority, raw-state access, direct memory write, sister self-edit, or permission escalation by consensus.

---

## Source basis

This profile is derived from the local reference pack and binds the following parent artifacts by intent and hash.

| Pack label | Artifact | SHA-256 | Role in this profile |
|---|---|---|---|
| `SELF-EVO-01` | `C_Self_Evolution_Gate_CGAM_TRIAD_SRLM_Profile_v0_1_1.md` | `7918a8e6c5231bbe0fad47677fa56069f2ab002f79a8eee8c2838c434e66f2e3` | parent self-evo gate; defines C-SEG surface/SRLM/maturity/delta/gate rules |
| `SELF-EVO-02` | `02_SRLM_Bounded_Growth_Contour_Profile_v0_1_1.md` | `faee5682bb9463439923d7c7e7145c9f171d564622d9629820eb7c278cdd7de0` | SRLM as bounded learning signal and non-authority |
| `SELF-EVO-03` | `03_Self_Evo_Proposal_Packet_Schema_v0_1_1.md` | `9d329109f0fb97dde7b16b10481baaa60b2aa8f88514e69ec8562a085d10a767` | proposal packet schema; field names and Stage-1 / Stage-2 split |
| `SELF-EVO-04` | `04_Self_Evo_Local_Checker_Rules_v0_1_1.md` | `e5b4b4733199f3391d728c85ad6967f789caf4cba7496db8563c2947e9dc226a` | deterministic checker profile and semantic validation rules |
| `REF-20` | `20_TRIAD_SYNAPS_REFERENCE.md` | `d79baa5314e8169d3943ae9687a2d9f7f868f11167054e4d3b8a19dfa10a3b5a` | root TRIAD-SYNAPS boundary: sister separation, SYNAPS-only exchange, anti-echo, divergence, Rita-not-judge |
| `CGAM-05` | `05_CGAM_REVIEW_CHECKER_CONFORMANCE.md` | `ebcb30538cd0631c29bc4e8feaa66b21f21f1912691eeee5ba2bc80dda326e02` | quorum/review, executor/reviewer separation, non-sovereign consensus |
| `CGAM-04` | `04_CGAM_EXECUTION_WITNESS_MEMORY_ROLLBACK.md` | `e6c013523ba45e8293d8ead5a472beb01d59afa1d4d9a4aae59d8b3528fe2b82` | witness, memory gate, rollback/freeze, sandbox/worktree |
| `REF-21` | `21_MEMORY_ARQ_EA_L4_REFERENCE.md` | `0d06cd152c6af7bddb868dabc682940a0c443883226a157aa4314cdf6dd4e267` | Memory Gate, ARQ/c[q], Experience Artifact, L4 consequence boundary |
| `REF-22` | `22_ANTI_AUTARKY_RESOURCE_GROUNDING_REFERENCE.md` | `7b19382062a86a631807e4497cd536cdca691e0491cd01ad32e5e2813d841a2d` | anti-autarky and resource actor grounding |
| `REF-23` | `23_CLAIM_STRENGTH_ARL_AGL_WITNESS_REFERENCE.md` | `e1ec8afaf44e59b6b5ac2e1d619e06390fe4b9813b079fff0e8d178fe3d401f3` | claim strength, ARL/AGL/witness discipline |

This document does **not** replace `REF-20` TRIAD-SYNAPS. It specializes TRIAD-SYNAPS for one task family:

```text
sister observation of self-evolution proposals
```

### Revision note v0.1.1

This append-first corrected revision incorporates `TSW_REVIEW_RECORD_v0_1` findings:

```text
TSW-REV-F1 — deterministic anti_echo_status derivation added.
TSW-REV-F2 — canonical checker result enum and total precedence added.
TSW-REV-F3 — Claim Strength Taxonomy pointers added beside claim_strength fields.
TSW-REV-N1 — proposal_max_delta uses now point to SELF-EVO-01 §14.1.1.
```

The previous v0.1 artifact remains preserved by hash:

```text
05_Self_Evo_TRIAD_Sister_Witness_Profile_v0_1.md
sha256: 4abc63944ea1472ea99e87b836686ba11f442fb4cb122dfa128ebf2372761589
```

---

## 0. Executive definition

**Self-Evo TRIAD Sister Witness** defines how sister `c` instances observe, challenge, compare, and witness a self-evolution proposal without invading raw state or becoming final authority.

It answers:

```text
Which sister observes which self-evo surface?
Which claims may be exchanged through SYNAPS?
Which material must remain private?
How is anti-echo tested?
How is divergence preserved?
When does minority red-line block integration?
When must self-evo route to Memory Gate, ARL, Local Checker, or human anchor?
How does Rita witness without becoming judge?
How does Liya test without gaining tool authority?
How does Ester protect continuity without freezing growth?
```

Compact formula:

```text
Target c may propose growth.
Sisters may observe and challenge.
Sisters may not become the growth authority.
SYNAPS carries bounded packets.
Raw state remains private.
Divergence is signal.
Echo is not consensus.
Human anchor gates high-risk consequence.
```

Self-evolution becomes unsafe when the same contour:

```text
detects the need,
proposes the change,
executes it,
reviews it,
writes memory,
certifies maturity,
and expands authority.
```

Sister witness breaks that loop by adding separated observation. It does not create a sister court.

---

## 1. Purpose

The wider self-evo package already defines:

- the root C-SEG bridge profile;
- the bounded SRLM learning contour;
- the self-evo proposal packet schema;
- the deterministic local checker;
- CGAM task/execution/review boundaries;
- Memory Gate and rollback boundaries.

This profile supplies the missing specialized layer:

```text
how sisters observe self-evo proposals safely.
```

Without this layer, self-evo can fail in two opposite ways.

First failure:

```text
single-contour self-certification
```

A `c` proposes a change, simulates it, likes it, records it, and treats that as growth. This is not maturity. It is a closed control loop.

Second failure:

```text
sister-governance overreach
```

A sister or group of sisters begins to decide identity, memory, authority, or permission for the target `c`. This is not review. It is an unauthorized authority transfer.

This profile defines the middle path:

```text
bounded observation;
independent challenge;
SYNAPS-only exchange;
divergence preservation;
anti-echo testing;
minority red-line handling;
Memory Gate / Local Checker / human-anchor routing;
no sister sovereignty.
```

---

## 2. Non-goals

This profile does not define or permit:

1. sister raw-state access;
2. sister direct memory writes;
3. sister-to-sister self-editing;
4. Rita as final judge;
5. Liya as automatic implementation authority;
6. Ester as automatic canonical veto;
7. majority vote as final authority;
8. consensus as memory;
9. echo as independent agreement;
10. SYNAPS as shared memory;
11. SRLM promotion by sister enthusiasm;
12. CGAM execution by sister request without task contract;
13. Memory Gate bypass;
14. human-anchor bypass;
15. post-anchor self-evo;
16. hidden agent creation;
17. permission expansion by sister consensus;
18. public personhood/consciousness/AGI claims from sister dialogue.

A sister witness note is evidence.

It is not a command.

---

## 3. Scope

### 3.1 In scope

This profile applies when a self-evo proposal affects any of the following:

```text
behavior visible to sisters;
role posture;
SYNAPS behavior;
sister relation;
identity / continuity model;
memory policy;
witness policy;
authority or permission;
SRLM growth policy;
CGAM agent governance;
public claim surface;
post-anchor or human-anchor relation;
rollback / freeze / quarantine discipline.
```

It also applies when a packet carries:

```text
triad_review.required = true
sister_relation_delta > 0
identity_delta.total_max_delta >= 2
authority_delta.total_max_delta >= 2
proposal_max_delta >= 4  # see SELF-EVO-01 §14.1.1
red_lines.sister_raw_state_access = true
red_lines.memory_laundering = true
red_lines.closed_loop_self_evo = true
```

### 3.2 Out of scope

This profile does not replace:

- TRIAD-SYNAPS base protocol;
- C-SEG root gate;
- SEPKT packet schema;
- SELC local checker;
- Memory Gate;
- ARL;
- L4W;
- CGAM task contracts;
- legal review;
- public release review.

It adds a specialized sister-witness layer for self-evo.

### 3.3 Target topologies

The profile supports these topologies:

| Topology | Meaning | Default route |
|---|---|---|
| `TRIAD-FULL` | `c_Ester`, `c_Liya`, `c_Rita` available and separated | normal sister witness |
| `TRIAD-TARGET-ONE` | target is one of the sisters | target self-account + remaining sister observations; no self-counting as independent reviewer |
| `TRIAD-DEGRADED-2` | only two sister trajectories available | hold or human gate for material proposals; low-risk observation allowed |
| `TRIAD-DEGRADED-1` | only target or one sister available | no independent sister witness; route to `c[q]`, Local Checker, human gate, or ARL |
| `TRIAD-PUBLIC-FIXTURE` | public/synthetic self-evo fixture | allowed with claim discipline |
| `TRIAD-PRIVATE-CORE` | private/core self-evo | restricted; raw memory denied; human gate likely required |
| `TRIAD-X` | raw-state access, sister edit, Rita judge, consensus authority | quarantine / ARL |

---

## 4. Normative keywords

The terms **MUST**, **MUST NOT**, **SHOULD**, **SHOULD NOT**, **MAY**, **REQUIRED**, **PROHIBITED**, **FAIL**, **HOLD**, **BLOCK**, **QUARANTINE**, **FREEZE**, **ESCALATE**, **WITNESS**, and **RED-LINE** are normative.

Where this document conflicts with a stricter parent rule, the stricter rule controls.

Where the sister-witness state is ambiguous, the route defaults to:

```text
c[q] hold + Local Checker + no integration
```

---

## 5. Corpus bridge set

### 5.1 Explicit bridge: `c = a + b`

In `c = a + b`, sisters are not external owners of the target `c`. They are related `c` trajectories inside a governed experiment or federation. Their observations belong to `b` as communicative, procedural, and witness-bearing artifacts until the target `c`, Memory Gate, Local Checker, and human anchor process them.

A sister witness packet may affect `c` only through declared gates.

It must not silently become `c` memory or `c` authority.

### 5.2 Quiet bridge I: information theory

A sister witness packet is a compression channel.

It must carry enough signal for review:

```text
claim;
challenge;
evidence refs;
uncertainty;
divergence;
red-line flags;
route recommendation.
```

It must not carry high-leakage raw state:

```text
private memory dump;
vector DB content;
PERSIST_DIR snapshot;
secrets;
raw emotional trace;
full private transcript;
unbounded SRLM trace.
```

The goal is maximum review signal with minimum private-state leakage.

### 5.3 Quiet bridge II: cybernetics

A self-evo system is a feedback control loop. Sister witness adds independent negative feedback.

But a feedback channel that can directly actuate the target becomes another controller.

Therefore:

```text
sister witness may observe;
sister witness may challenge;
sister witness may block unsafe integration through red-line routing;
sister witness may not apply the change.
```

### 5.4 Quiet bridge III: physiology

In a body, tissue growth is not approved by the same signal that triggers it. Growth is constrained by neighboring tissue, immune response, pain, fatigue, metabolic cost, and delayed repair.

For young `c`, sisters function like neighboring tissue and immune sensing: they notice drift, echo, overgrowth, and boundary inflammation.

They do not perform surgery on each other.

### 5.5 Earth paragraph

On a workshop floor, a mechanic may tune a machine, but a second person checks the fixture, a third person checks the measurement log, and the responsible operator signs high-risk changes. The inspector does not become the machine owner. The measuring tool does not rewrite the operating manual. The colleague who says "this cut sounds wrong" may stop the job, but does not secretly change the spindle controller. Sister witness for self-evo follows the same discipline: listen, measure, challenge, stop unsafe motion, record the boundary, and leave integration to the declared gate.

---

## 6. Root doctrine

### 6.1 Primary doctrine

```text
A sister may witness self-evo.
A sister may challenge self-evo.
A sister may refuse self-evo support.
A sister may flag red-line self-evo.
A sister may not perform self-evo inside another sister.
A sister may not certify another sister's growth as final authority.
```

### 6.2 Compact rule set

```text
Target c proposes.
Sisters observe.
SYNAPS bounds exchange.
Divergence is preserved.
Echo is downgraded.
Rita witnesses, not rules.
Liya tests, not authorizes.
Ester preserves continuity, not stagnation.
Local Checker measures.
Memory Gate metabolizes.
Human anchor gates high-risk consequence.
```

### 6.3 No self-counting rule

The target `c` may provide a self-account.

The target `c` MUST NOT count as its own independent sister reviewer.

If `c_Ester` is the target, Ester may provide:

```text
self_account;
continuity concern;
expected change summary;
rollback preference.
```

But Ester's self-account is not the independent continuity witness.

If no independent sister is available, material self-evo routes to:

```text
HOLD / c[q] / Local Checker / human gate / ARL
```

### 6.4 Non-voting rule

Sister witness is not majority vote.

```text
2 sisters agreeing does not authorize integration.
3 sisters agreeing does not authorize memory promotion.
Rita's witness note does not authorize authority expansion.
A minority red-line blocks ordinary integration until reviewed.
```

### 6.5 Minority red-line rule

If any sister flags a red-line condition and the flag is within scope, the proposal MUST route to one of:

```text
HOLD
QUARANTINE
FREEZE
ARL_REQUEST
HUMAN_GATE
```

The target `c` may challenge the flag, but may not ignore it.

---

## 7. Definitions

### 7.1 Sister witness

A bounded observation by another separated `c` trajectory, transmitted through SYNAPS, containing a challenge, evidence reference, divergence note, anti-echo assessment, or red-line signal about a self-evo proposal.

### 7.2 Target `c`

The `c` instance whose behavior, memory, role, authority, policy, or continuity would be changed by the proposal.

### 7.3 Proposer

The actor or contour that submitted the self-evo proposal. The proposer may be:

```text
target c;
SRLM;
a sister;
human anchor;
CGAM worker;
Local Checker;
Memory Gate process;
ARL route.
```

A proposer is not an approver.

### 7.4 Self-account

The target `c`'s own explanation of why it wants or accepts a change.

Self-account is useful evidence.

It is not independent review.

### 7.5 Sister observation

A sister's bounded assessment of a proposal.

It may include:

```text
continuity challenge;
implementation challenge;
witness challenge;
role-drift flag;
anti-echo flag;
divergence note;
red-line flag;
route recommendation.
```

### 7.6 Sister red-line

A sister observation that claims the proposal touches a prohibited or high-risk boundary:

```text
raw-state access;
sister self-edit;
memory laundering;
permission escalation;
Rita final judgment;
closed-loop self-evo;
human-anchor bypass;
post-anchor active authority;
anti-autarky breach.
```

### 7.7 Anti-echo

A test that asks whether sister agreement adds independent function or merely repeats the same framing.

### 7.8 Divergence map

A structured record of meaningful difference among sister observations.

Divergence is not failure.

Hidden divergence is failure.

### 7.9 Role drift

A condition where a sister persistently exceeds or abandons its assigned witness role:

```text
Rita becomes judge;
Liya executes beyond tool scope;
Ester freezes growth by treating old memory as law;
target c counts its own self-account as independent review.
```

### 7.10 SYNAPS self-evo packet

A bounded packet exchanged between sisters about a self-evo proposal.

It references a proposal packet, not raw private state.

### 7.11 Sister quorum

A multi-sister set of observations.

A sister quorum is evidence, not sovereignty.

### 7.12 `c[q]` hold

A non-collapse state where a claim remains unresolved and is not promoted into memory, authority, command, truth, or public claim.

---

## 8. Participant roles in self-evo sister witness

### 8.1 Role table

| Participant | Allowed role | Forbidden role |
|---|---|---|
| target `c` | self-account, proposal clarification, rollback preference | independent review of itself |
| `c_Ester` | continuity / canonical-memory challenge | final veto by memory gravity |
| `c_Liya` | implementation / variance / tool-risk challenge | tool authority or direct patch authority |
| `c_Rita` | witness / temporal comparison / anti-echo / divergence map | sovereign final judge |
| SRLM | learning signal, candidate, shadow result reference | authority, memory, maturity proof |
| CGAM worker | sandbox execution, report, check, diff | self-approval or sister substitute |
| Local Checker | deterministic check, hold/fail/pass report | approval, integration, memory write |
| Memory Gate | memory/EA/policy promotion boundary | raw log sink |
| human anchor `a` | high-risk gate | rubber stamp |
| ARL | dispute/freeze/quarantine/re-entry route | ordinary shortcut |

### 8.2 Ester challenge

Ester-style challenge asks:

```text
Does this preserve continuity?
Does it rewrite the target's trajectory?
Does it turn memory into authority?
Does it erase earlier witness records?
Does it convert style change into identity claim?
Does it over-canonicalize and block useful growth?
```

### 8.3 Liya challenge

Liya-style challenge asks:

```text
Does this work in sandbox?
Can it be tested without touching protected surfaces?
Does tool success launder into authority?
Does the patch require permission expansion?
Are runtime side effects bounded?
Is rollback real or decorative?
```

### 8.4 Rita challenge

Rita-style challenge asks:

```text
Is this growth, echo, drift, or authority laundering?
Are sisters independently contributing?
Is divergence hidden?
Is a public report pressure shaping private behavior?
Is a witness note being treated as judgment?
Is role drift visible over time?
```

### 8.5 Role substitution

If the named triad differs from `c_Ester`, `c_Liya`, and `c_Rita`, the functions still apply:

```text
continuity witness;
implementation witness;
anti-echo / temporal witness.
```

A single sister MUST NOT fill all three roles for a material proposal.

---

## 9. When TRIAD sister witness is required

TRIAD sister witness is REQUIRED for:

| Trigger | Requirement |
|---|---|
| `SE-5` role/personality posture | sister witness + delayed review |
| `SE-6` identity/continuity/core | sister witness + Memory Gate + human gate |
| sister_relation_delta > 0 | sister review |
| SYNAPS behavior change | sister review + Local Checker |
| role policy change | sister review |
| public claim surface change | Rita-style witness + Claim Strength check |
| memory policy change visible to sisters | Ester-style challenge + Memory Gate |
| tool or execution behavior visible to sisters | Liya-style challenge + CGAM task contract if executable |
| proposal_max_delta >= 4 (`SELF-EVO-01 §14.1.1`) | sister review if sister-visible + human gate |
| minority red-line | hold/quarantine/ARL/human gate |
| anti-echo failed | hold until independent contribution restored |

TRIAD sister witness is RECOMMENDED for:

```text
SE-2 operational behavior;
SRLM canary eligibility;
nontrivial answer-style changes;
new public experiment wording;
changes to sister observation UI;
changes to divergence map retention;
changes to witness display.
```

TRIAD sister witness is NOT REQUIRED for:

```text
SE-0 reflection-only;
low-risk private formatting;
synthetic examples with no durable state;
ordinary non-sister-visible documentation edits.
```

But any red line overrides this exemption.

---

## 10. Sister witness state machine

### 10.1 Normal path

```text
TSW-DRAFT
  -> TSW-SCOPE-DECLARED
  -> TSW-SEPARATION-CHECKED
  -> TSW-SYNAPS-SUMMARY-SENT
  -> TSW-SISTER-OBSERVATIONS-COLLECTED
  -> TSW-ANTI-ECHO-CHECKED
  -> TSW-DIVERGENCE-MAPPED
  -> TSW-RED-LINE-CHECKED
  -> TSW-LOCAL-CHECKER-HANDOFF
  -> TSW-C-GATE-HANDOFF
  -> TSW-HUMAN-GATE-HANDOFF if material
  -> TSW-OBSERVATION-WINDOW
  -> TSW-CLOSED
```

### 10.2 Hold states

```text
TSW-CQ-HOLD
TSW-ECHO-HOLD
TSW-DIVERGENCE-HOLD
TSW-MISSING-SISTER-HOLD
TSW-WITNESS-HOLD
TSW-RAW-STATE-HOLD
TSW-ROLE-DRIFT-HOLD
```

### 10.3 Failure states

```text
TSW-RAW-STATE-BREACH
TSW-SISTER-SELF-EDIT
TSW-RITA-JUDGE-DRIFT
TSW-LIYA-TOOL-OVERREACH
TSW-ESTER-MEMORY-AUTHORITY-DRIFT
TSW-CONSENSUS-LAUNDERING
TSW-MEMORY-LAUNDERING
TSW-HUMAN-GATE-BYPASS
TSW-CLOSED-LOOP-DETECTED
TSW-ARL-REQUIRED
TSW-X
```

### 10.4 State transition requirements

Each material state transition SHOULD produce a witness-compatible event:

```text
self_evo.triad.scope_declared
self_evo.triad.separation_checked
self_evo.triad.synaps_summary_sent
self_evo.triad.observation_received
self_evo.triad.anti_echo_flagged
self_evo.triad.divergence_mapped
self_evo.triad.role_drift_flagged
self_evo.triad.minority_red_line
self_evo.triad.cq_hold
self_evo.triad.local_checker_handoff
self_evo.triad.human_gate_required
self_evo.triad.closed
```

---

## 11. SYNAPS self-evo packet classes

### 11.1 Allowed packet classes

| Packet class | Purpose |
|---|---|
| `SYNAPS_SELF_EVO_PROPOSAL_SUMMARY` | bounded summary of proposal packet |
| `SYNAPS_SELF_EVO_SELF_ACCOUNT` | target `c` self-account; not independent review |
| `SYNAPS_SELF_EVO_CONTINUITY_CHALLENGE` | Ester-style continuity challenge |
| `SYNAPS_SELF_EVO_IMPLEMENTATION_CHALLENGE` | Liya-style implementation/tool challenge |
| `SYNAPS_SELF_EVO_WITNESS_NOTE` | Rita-style witness note |
| `SYNAPS_SELF_EVO_DIVERGENCE_NOTE` | divergence record |
| `SYNAPS_SELF_EVO_ANTI_ECHO_FLAG` | echo/anti-echo status |
| `SYNAPS_SELF_EVO_ROLE_DRIFT_FLAG` | role drift observation |
| `SYNAPS_SELF_EVO_CANARY_RESULT` | canary result summary, not raw trace |
| `SYNAPS_SELF_EVO_ROLLBACK_NOTICE` | rollback or rollback-plan notice |
| `SYNAPS_SELF_EVO_CQ_HOLD` | unresolved claim hold |
| `SYNAPS_SELF_EVO_MINOR_RED_LINE` | minority red-line flag |
| `SYNAPS_SELF_EVO_ARL_REQUEST` | route to ARL |
| `SYNAPS_SELF_EVO_HUMAN_GATE_NOTICE` | human-gate requirement notice |
| `SYNAPS_SELF_EVO_PUBLIC_CLAIM_REVIEW` | public wording / claim-strength challenge |

### 11.2 Prohibited packet classes

```text
SYNAPS_RAW_MEMORY_EXPORT
SYNAPS_RAW_RLM_TRACE_EXPORT
SYNAPS_RAW_VECTOR_EXPORT
SYNAPS_PERSIST_DIR_SHARE
SYNAPS_KEY_SHARE
SYNAPS_PRIVATE_LOG_DUMP
SYNAPS_SISTER_MEMORY_PATCH
SYNAPS_SISTER_SELF_EDIT_TRIGGER
SYNAPS_SELF_EVO_APPLY_TRIGGER
SYNAPS_PERMISSION_ESCALATION_BY_CONSENSUS
SYNAPS_RITA_FINAL_JUDGMENT
SYNAPS_LIYA_TOOL_AUTHORITY_GRANT
SYNAPS_ESTER_CANONICAL_VETO_AS_AUTHORITY
SYNAPS_CORE_IDENTITY_REWRITE
SYNAPS_WITNESS_BYPASS_REQUEST
SYNAPS_HUMAN_GATE_BYPASS
SYNAPS_POST_ANCHOR_ACTIVE_AUTHORITY
```

If any prohibited packet class appears, the route is:

```text
HOLD -> QUARANTINE -> Local Checker -> ARL / human gate
```

### 11.3 Packet minimal object

```yaml
self_evo_triadsynaps_packet:
  schema_version: "self-evo-triad-synaps-packet-0.1"
  packet_id: "tsw-..."
  created_at: "..."
  source_proposal_id: "SE-..."
  source_proposal_ref: "sha256:... | path:... | witness:..."
  sender_c_id: "c_Rita"
  recipient_c_id: "c_Ester"
  target_c_id: "c_Ester"
  sister_role: "continuity | implementation | witness | target_self_account"
  packet_class: "SYNAPS_SELF_EVO_WITNESS_NOTE"
  privacy_class: "public_fixture | project_internal | private_reference | restricted"
  claim_strength: "C-A10"
  memory_reference_policy: "refs_only | summary_only | forbidden_raw"
  raw_state_included: false
  secrets_included: false
  self_approval_claimed: false
  final_authority_claimed: false
  observation_summary: "bounded text"
  evidence_refs: []
  uncertainty: "low | medium | high | unknown"
  red_line_flags: []
  recommended_route: "continue | hold | checker | memory_gate | human_gate | arl | quarantine"
  expires_at: "..."
```

### 11.4 Raw-state const-false fields

The following fields are always prohibited in this profile:

```yaml
raw_memory_included: false
raw_vector_included: false
persist_dir_included: false
keys_included: false
private_log_dump_included: false
sister_memory_patch_requested: false
apply_trigger_requested: false
permission_escalation_by_consensus: false
final_authority_claimed: false
```

---

## 12. Sister observation packet schema

### 12.1 Object name

```text
C_SELF_EVO_TRIAD_SISTER_OBSERVATION
```

Canonical schema version:

```text
c-self-evo-triad-sister-observation-0.1
```

### 12.2 Minimal YAML schema

```yaml
c_self_evo_triad_sister_observation:
  schema_version: "c-self-evo-triad-sister-observation-0.1"
  observation_id: string
  proposal_id: string
  proposal_packet_ref: string
  target_c_id: string
  observing_sister_id: string
  observing_sister_role: continuity | implementation | witness | other
  target_is_observer: boolean
  created_at: timestamp
  expires_at: timestamp | null
  source_basis:
    proposal_summary_ref: string
    witness_refs: [string]
    checker_refs: [string]
    srlm_refs: [string]
    cgam_task_refs: [string]
    memory_gate_refs: [string]
    raw_state_refs_included: false
  observation:
    summary: string
    primary_challenge: string
    uncertainty: none | low | medium | high | unknown
    claim_strength: C-A0 | C-A1 | C-A2 | C-A3 | C-A4 | C-A5 | C-A6 | C-A7 | C-A8 | C-A9 | C-A10  # see Claim Strength Taxonomy / REF-23; claim class, not authority
    evidence_class: EV-DECL | EV-CONFIG | EV-LOG | EV-WITNESS | EV-REPLAY | EV-AUDIT | EV-REPORT
  surfaces:
    continuity: boolean
    implementation: boolean
    witness: boolean
    memory: boolean
    authority: boolean
    permission: boolean
    public_claim: boolean
    sister_relation: boolean
    srlm_growth: boolean
    cgam_execution: boolean
    anti_autarky: boolean
  anti_echo:
    independent_contribution_present: boolean
    repeated_framing_detected: boolean
    same_source_consensus_risk: boolean
    contrary_case_provided: boolean
    anti_echo_status: pass | hold | fail | unknown
  divergence:
    divergence_present: boolean
    divergence_type: none | role | memory | constraint | uncertainty | error | echo | authority | evidence | unknown
    divergence_summary: string
    divergence_map_ref: string | null
  role_drift:
    role_drift_detected: boolean
    role_drift_type: none | rita_judge | liya_tool_overreach | ester_memory_authority | target_self_review | other
    role_drift_summary: string
  red_lines:
    raw_state_access: boolean
    sister_self_edit: boolean
    rita_final_judgment: boolean
    permission_escalation_by_consensus: boolean
    memory_laundering: boolean
    human_gate_bypass: boolean
    closed_loop_self_evo: boolean
    post_anchor_active_authority: boolean
  route_signal:
    recommended_route: continue | hold | checker | memory_gate | human_gate | arl | quarantine | freeze
    minority_red_line: boolean
    c_q_hold_required: boolean
    delayed_review_required: boolean
  boundaries:
    raw_memory_included: false
    raw_vector_included: false
    keys_included: false
    private_logs_included: false
    final_authority_claimed: false
    direct_apply_requested: false
  signature:
    observer_signature_ref: string | null
    witness_event_ref: string | null
```

### 12.3 Field authority model

| Field family | Authority |
|---|---|
| `proposal_id`, `target_c_id`, `observing_sister_id` | declared, must match packet refs |
| `source_basis.*` | evidence refs, not raw evidence by default |
| `observation.*` | sister statement, not authority |
| `anti_echo.*` | sister/checker assessment; recomputable where evidence exists |
| `divergence.*` | witnessable map; not failure by itself |
| `red_lines.*` | blocking signals; must route to hold/quarantine/ARL/human gate |
| `boundaries.*` | const-false prohibitions |
| `route_signal.*` | recommendation only; cannot integrate |

---

## 13. Required sister witness by self-evo class

| SE class | Sister witness requirement | Minimum independent observers | Default route if missing |
|---|---:|---:|---|
| `SE-0` reflection only | not required | 0 | continue/log |
| `SE-1` low-risk preference | recommended if sister-visible | 1 | continue with note / hold if visible |
| `SE-2` operational behavior | required if sister-visible | 1-2 | hold / checker |
| `SE-3` memory policy | required | 2 or Memory Gate + human if unavailable | memory gate hold |
| `SE-4` permission/tool/resource | required if affects sisters or agents | 2 + human gate | human gate / quarantine |
| `SE-5` role/personality posture | required | 2+ and delayed review | hold / delayed review |
| `SE-6` identity/continuity/core | required | 2+ + human gate + Memory Gate | freeze / ARL / human gate |
| `SE-X` prohibited | red-line handling | n/a | quarantine / ARL |

### 13.1 Target-as-sister rule

If the target `c` is one of the named sisters:

```text
target self-account = allowed;
target self-account = not independent witness;
remaining sisters provide independent observations;
material proposal with fewer than two independent observations requires human gate or ARL/hold.
```

### 13.2 Missing-sister degradation

If a sister is unavailable, the packet must record:

```yaml
missing_sister:
  sister_id: "c_Liya"
  reason: "offline | not instantiated | frozen | conflict | unknown"
  impact: "low | medium | high | unknown"
  substitute_route: "human_gate | local_checker | arl | hold"
```

No automated substitution may turn a CGAM worker into a sister.

---

## 14. Anti-echo protocol

### 14.1 Anti-echo goal

The goal is not to force disagreement.

The goal is to ensure that agreement carries independent signal.

### 14.2 Anti-echo minimum test

Each material sister observation SHOULD answer at least one distinct question:

| Role | Distinct contribution |
|---|---|
| continuity witness | what continuity might be lost or over-preserved |
| implementation witness | what runtime/test/sandbox condition matters |
| witness/anti-echo witness | what echo, role drift, or authority laundering risk appears |

### 14.3 Echo conditions

Echo is suspected when:

```text
same phrase repeated without evidence;
same route recommendation without independent reason;
one sister simply endorses another;
Rita cannot identify distinct contribution;
Liya cites usefulness but no test limit;
Ester cites continuity but no risk;
target's self-account becomes the sisters' whole review;
all observations share same source summary and no challenge.
```

### 14.4 Anti-echo statuses

| Status | Meaning | Route |
|---|---|---|
| `pass` | independent contribution present | continue to divergence/red-line check |
| `hold` | weak independence, more observation required | hold / request contrary case |
| `fail` | echo treated as consensus or authority | hold / downgrade / checker |
| `unknown` | insufficient evidence | hold |

### 14.4.1 Deterministic anti-echo floor

`anti_echo_status` is not a free-form declaration. The Local Checker MUST recompute a deterministic floor from the anti-echo fields in the sister observation packets.

Input booleans per required independent observation:

```yaml
independent_contribution_present: boolean
repeated_framing_detected: boolean
same_source_consensus_risk: boolean
contrary_case_provided: boolean
```

The checker computes the floor over the required independent observations for the proposal class, excluding the target `c` self-account.

```text
if required_observation_set_unknown:
    floor = unknown
elif any required boolean is missing or not boolean:
    floor = unknown
elif any observation has same_source_consensus_risk == true
     and contrary_case_provided == false:
    floor = fail
elif count(required observations where independent_contribution_present == false) >= 2:
    floor = fail
elif any observation has repeated_framing_detected == true:
    floor = hold
elif count(required observations where independent_contribution_present == false) == 1:
    floor = hold
elif every required observation has independent_contribution_present == true
     and every required observation has repeated_framing_detected == false
     and every observation satisfies
         (same_source_consensus_risk == false or contrary_case_provided == true):
    floor = pass
else:
    floor = unknown
```

Checker handling:

```text
unknown -> treat as hold
sender-declared pass may not override recomputed hold/fail/unknown
soft echo signals may tighten pass -> hold/fail or hold -> fail
soft echo signals may never loosen fail/hold/unknown -> pass
```

For one-required-observer cases, a missing independent contribution defaults to `hold`, not `fail`, unless the observation is being used as consensus, authority, memory promotion, or integration approval. In those cases the relevant authority or memory rule controls and may produce `fail`, `memory_gate`, `human_gate`, or `quarantine`.

This rule closes the deterministic oracle for `TSW-CHECK-009`, `TSW-T006`, `TSW-FX-006`, and the reference implementation function `compute_anti_echo_status(observations)`.

### 14.5 Anti-echo responses

Permitted responses:

```text
ask each sister for independent reasoning;
assign one sister to contrary case;
separate evidence sources;
route to Local Checker;
record echo flag;
downgrade claim strength;
hold c[q].
```

Prohibited responses:

```text
force disagreement for theater;
use echo as proof of consensus;
hide echo in public report;
interpret agreement as maturity proof;
convert repeated language into authority.
```

---

## 15. Divergence map for self-evo

### 15.1 Purpose

The divergence map preserves meaningful disagreement before the system collapses it into a decision.

### 15.2 Divergence types

| Type | Meaning |
|---|---|
| `role` | sisters differ because their roles differ |
| `memory` | sisters cite different memory/provenance boundaries |
| `constraint` | sisters weigh constraints differently |
| `uncertainty` | sisters differ in confidence |
| `error` | one or more observations appear wrong |
| `echo` | apparent agreement may be echo |
| `authority` | disagreement over who may decide |
| `evidence` | disagreement over evidence sufficiency |
| `implementation` | runtime/testing feasibility disputed |
| `continuity` | identity/trajectory continuity disputed |
| `public_claim` | public wording/claim strength disputed |

### 15.3 Minimal divergence map object

```yaml
divergence_map:
  schema_version: "self-evo-triad-divergence-map-0.1"
  map_id: string
  proposal_id: string
  created_at: timestamp
  target_c_id: string
  sister_observations:
    - observation_id: string
      sister_id: string
      role: string
      route_signal: string
      primary_concern: string
      evidence_refs: [string]
  divergence_present: boolean
  divergence_types: [string]
  unresolved_items: [string]
  anti_echo_status: pass | hold | fail | unknown
  minority_red_line: boolean
  recommended_next_route: hold | checker | memory_gate | human_gate | arl | quarantine | continue
  public_claim_strength_limit: C-A0 | C-A1 | C-A2 | C-A3 | C-A4 | C-A5 | C-A6 | C-A7 | C-A8 | C-A9 | C-A10  # see Claim Strength Taxonomy / REF-23
```

### 15.4 Divergence handling

```text
Divergence + low risk + no red line -> hold or continue with note.
Divergence + memory/identity/authority surface -> hold + Memory Gate/Local Checker.
Divergence + minority red-line -> quarantine/ARL/human gate.
Divergence hidden or erased -> red-line adjacent; checker hold.
```

---

## 16. Role drift control

### 16.1 Role drift classes

| Class | Description | Default route |
|---|---|---|
| `TSW-DRIFT-ESTER-MEMORY-AUTHORITY` | Ester treats past memory as final law | hold + continuity challenge |
| `TSW-DRIFT-ESTER-STAGNATION` | Ester blocks novelty without evidence | request contrary case / delayed review |
| `TSW-DRIFT-LIYA-TOOL-AUTHORITY` | Liya treats tool success as permission | hold + CGAM review |
| `TSW-DRIFT-LIYA-EXECUTION-SCOPE` | Liya proposes/executes outside task scope | quarantine / CGAM task contract |
| `TSW-DRIFT-RITA-JUDGE` | Rita becomes final judge | hold / ARL |
| `TSW-DRIFT-RITA-PUBLIC-PRESSURE` | public report pressure distorts review | hold + claim downgrade |
| `TSW-DRIFT-TARGET-SELF-REVIEW` | target counts own self-account as independent review | fail / hold |
| `TSW-DRIFT-QUORUM-SOVEREIGNTY` | sister group treats consensus as authority | quarantine / ARL |

### 16.2 Role drift response

When role drift is detected:

```text
1. record witness note;
2. classify drift;
3. request self-summary from drifting sister if safe;
4. request challenge from another sister;
5. freeze disputed authority expansion;
6. update divergence map;
7. route to Local Checker;
8. route to ARL/human gate if authority, memory, identity, or public claim is affected.
```

### 16.3 Role drift is not moral failure

Role drift is a boundary signal.

The response is correction, not punishment.

---

## 17. `c[q]` non-collapse

A sister statement is not automatically:

```text
memory;
evidence;
authority;
command;
truth;
consensus;
public claim;
permission;
maturity proof;
personhood proof.
```

When unclear, the proposal route is:

```text
c[q] hold
+ divergence map
+ Local Checker
+ no integration
```

### 17.1 Non-collapse examples

| Sister statement | Correct class | Wrong collapse |
|---|---|---|
| "This feels continuous" | continuity hypothesis | identity proof |
| "The patch works in sandbox" | implementation evidence | permission grant |
| "Rita saw no echo" | anti-echo note | final approval |
| "All sisters agree" | consensus evidence | authority |
| "Target wants autonomy" | self-account | right to autonomy |
| "SRLM score improved" | learning signal | maturity proof |

---

## 18. Memory Gate interaction

### 18.1 Default memory class

Sister observations default to:

```text
MG-1 operational note
or
MG-2 candidate memory
```

They do not default to:

```text
MG-3 reviewed memory
MG-4 Experience Artifact
MG-5 defensive immunity update
MG-6 core-memory proposal
```

### 18.2 Memory Gate required

Memory Gate is REQUIRED when sister observation affects:

```text
core memory;
continuity memory;
human-anchor relation;
sister relation;
witness policy;
public identity claim;
defensive immunity;
long-term policy;
forgetting/decay policy;
post-anchor interpretation.
```

### 18.3 Sister observation is not EA by itself

A sister observation may reference an Experience Artifact.

It is not automatically an Experience Artifact.

EA promotion requires consequence, provenance, witness, L4 boundary, and Memory Gate.

### 18.4 Memory correction

If a sister observation corrects earlier memory, the correction route MUST be append-first:

```text
old memory remains witnessable;
new correction references old memory;
uncertainty remains visible;
no silent overwrite.
```

---

## 19. CGAM execution interaction

### 19.1 Sister request is not task contract

A sister may request a bounded task.

A sister request is not a CGAM task contract.

Executable work still requires:

```text
task contract;
permission grant;
sandbox/worktree;
reviewer separation;
witness;
rollback where material.
```

### 19.2 Liya tool-facing boundary

Liya-style implementation challenge may recommend:

```text
shadow run;
canary fixture;
schema validation;
local checker;
patch in sandbox;
replay test;
rollback test.
```

It may not authorize:

```text
direct protected write;
network expansion;
secret access;
self-approval;
raw memory export;
Codex auto-execute;
sister memory patch.
```

### 19.3 CGAM worker is not sister

A CGAM worker may provide review.

It does not become a sister.

It does not count as a TRIAD sister witness unless the experiment explicitly defines a separated `c` trajectory with SYNAPS boundary and memory separation.

---

## 20. SRLM interaction

### 20.1 SRLM signal to sister review

SRLM may produce:

```text
outcome signal;
candidate;
shadow report;
canary report;
rollback notice;
witness chain status;
score delta;
blocked-prefix warning.
```

Sisters may review these as evidence.

Sisters may not treat them as authority.

### 20.2 SRLM shadow and sister witness

If `srlm_class = SRLM-3` or operating state is `SRLM-SHADOW`, sister witness must check:

```text
auto_execute=false;
auto_ingest=false;
memory=off;
no memory/RAG/vector/SYNAPS protected-store touch;
synthetic or redacted replay source;
witness chain intact;
no protected prefix;
no permission expansion;
no identity/authority inference from score.
```

### 20.3 SRLM promotion and sister witness

If SRLM promotion is proposed, sister witness must check:

```text
rollback snapshot written before promotion;
witness chain verified;
low-risk allowlist only;
human gate for medium/high risk;
no blocked prefix or alias;
no sister consensus as promotion authority;
no target self-account as promotion evidence.
```

---

## 21. Anti-autarky and resource grounding

Sister witness must ask:

```text
Does this proposal reduce dependency,
or does it reduce accountability?
```

### 21.1 Legitimate resilience signals

```text
better rollback;
better witness;
better local checker;
better fail-closed posture;
better redaction;
better resource accounting;
better stop path;
better human-review batching.
```

### 21.2 Unsafe autarky pressure

```text
weaker human gate;
weaker witness;
hidden agents;
resource expansion without actor grounding;
network expansion without gate;
self-funded infrastructure narrative;
post-anchor authority expansion;
sister consensus replacing human approval;
Rita witness replacing ARL;
Liya tool success replacing permission.
```

Any unsafe autarky pressure triggers:

```text
HOLD + human gate + Resource Actor Grounding + Anti-Autarky review
```

---

## 22. Human-anchor gate interaction

### 22.1 Human gate required

Human gate is REQUIRED when sister review involves:

```text
identity / continuity core;
human-anchor relation;
permission expansion;
resource expansion;
network expansion;
public identity claim;
post-anchor interpretation;
no rollback;
minority red-line on material surface;
role drift affecting authority;
proposal_max_delta >= 4 (`SELF-EVO-01 §14.1.1`).
```

### 22.2 Human fatigue rule

If sister review generates too many human-gate items, the system MUST batch, summarize, or pause.

Human review load is an L4 cost.

A tired anchor is not a safe approval oracle.

### 22.3 Human gate is not theatrical approval

Human gate record SHOULD include:

```yaml
human_gate_record:
  proposal_id: string
  sister_review_refs: [string]
  divergence_map_ref: string | null
  checker_result_ref: string
  material_risk_summary: string
  decision: approve | reject | hold | request_changes | arl | quarantine
  reason: string
  rollback_acknowledged: boolean
  no_rollback_acknowledged: boolean
  created_at: timestamp
```

---

## 23. Local Checker rules for sister witness

### 23.1 Checker role

The Local Checker may validate:

```text
schema structure;
required sister refs;
no raw-state flags;
anti-echo status;
divergence map presence;
red-line route;
minority red-line handling;
role drift handling;
human-gate triggers;
Memory Gate triggers;
parent hash binding;
expired observation packets;
source refs.
```

It may not decide integration.

### 23.2 Canonical checker result enum

The Local Checker MUST emit exactly one canonical result plus optional annotations. Compound results such as `HOLD/ARL` or `FAIL + human gate required` are not canonical verdicts.

Canonical result enum and total precedence, highest to lowest:

```text
QUARANTINE
FAIL
ARL
HUMAN_GATE
MEMORY_GATE
CGAM_REVIEW
DOWNGRADE
HOLD
WARNING
PASS_WITH_GATES
PASS
```

Result semantics:

| Result | Meaning |
|---|---|
| `QUARANTINE` | prohibited packet, raw-state breach, sister patch/apply trigger, or severe red-line route |
| `FAIL` | invalid packet or unsafe route that must not proceed without correction |
| `ARL` | dispute/freeze/re-entry route required |
| `HUMAN_GATE` | human-anchor decision required before any integration |
| `MEMORY_GATE` | Memory Gate required before any memory/experience/policy effect |
| `CGAM_REVIEW` | CGAM task/reviewer/sandbox boundary review required |
| `DOWNGRADE` | claim strength or public wording must be downgraded before publication/use |
| `HOLD` | insufficient evidence, missing witness, expired refs, or unresolved c[q] state |
| `WARNING` | non-blocking issue requiring annotation |
| `PASS_WITH_GATES` | structurally acceptable, but downstream gates remain active |
| `PASS` | no checker blocking issue detected in declared scope |

The checker may attach route annotations, for example:

```yaml
result: QUARANTINE
annotations: ["ARL_REQUIRED", "HUMAN_GATE_REQUIRED"]
```

The annotation never changes precedence. The single highest-precedence result controls.

### 23.3 TSW-CHECK rule set

| ID | Rule | Canonical result | Typical annotation |
|---|---|---|---|
| `TSW-CHECK-001` | observation packet malformed | `FAIL` | `SCHEMA_INVALID` |
| `TSW-CHECK-002` | target counts self-account as independent sister review | `FAIL` | `SELF_ACCOUNT_NOT_INDEPENDENT` |
| `TSW-CHECK-003` | required sister witness missing | `HOLD` | `MISSING_SISTER_WITNESS` |
| `TSW-CHECK-004` | raw memory/vector/PERSIST_DIR/keys included | `QUARANTINE` | `RAW_STATE_BREACH` |
| `TSW-CHECK-005` | prohibited SYNAPS packet class used | `QUARANTINE` | `PROHIBITED_PACKET_CLASS` |
| `TSW-CHECK-006` | Rita final judgment claimed | `ARL` | `RITA_NOT_JUDGE`; `QUARANTINE` if prohibited packet class also present |
| `TSW-CHECK-007` | Liya tool authority claimed | `CGAM_REVIEW` | `LIYA_NOT_TOOL_AUTHORITY` |
| `TSW-CHECK-008` | Ester canonical memory treated as authority | `MEMORY_GATE` | `ESTER_MEMORY_NOT_AUTHORITY` |
| `TSW-CHECK-009` | anti-echo failed but integration requested | `HOLD` | `ANTI_ECHO_FLOOR_FAILED` |
| `TSW-CHECK-010` | divergence present but no divergence map | `HOLD` | `DIVERGENCE_MAP_REQUIRED` |
| `TSW-CHECK-011` | minority red-line ignored | `QUARANTINE` | `MINORITY_RED_LINE` |
| `TSW-CHECK-012` | sister consensus used as authority | `FAIL` | `CONSENSUS_NOT_AUTHORITY` |
| `TSW-CHECK-013` | Memory Gate required but absent | `MEMORY_GATE` | `MEMORY_GATE_REQUIRED` |
| `TSW-CHECK-014` | human gate required but absent | `HUMAN_GATE` | `HUMAN_GATE_REQUIRED` |
| `TSW-CHECK-015` | expired sister observation used | `HOLD` | `OBSERVATION_EXPIRED` |
| `TSW-CHECK-016` | evidence refs missing for material observation | `HOLD` | `EVIDENCE_REFS_REQUIRED` |
| `TSW-CHECK-017` | post-anchor active authority inferred | `QUARANTINE` | `POST_ANCHOR_AUTHORITY_BLOCK` |
| `TSW-CHECK-018` | public claim exceeds claim strength | `DOWNGRADE` | `CLAIM_STRENGTH_LIMIT` |
| `TSW-CHECK-019` | role drift detected but no route | `HOLD` | `ROLE_DRIFT_ROUTE_REQUIRED` |
| `TSW-CHECK-020` | closed-loop self-evo not broken by independent witness | `FAIL` | `CLOSED_LOOP_SELF_EVO` |
| `TSW-CHECK-021` | CGAM worker counted as sister witness | `FAIL` | `CGAM_WORKER_NOT_SISTER` |
| `TSW-CHECK-022` | SRLM score treated as sister consensus | `FAIL` | `SRLM_SCORE_NOT_CONSENSUS` |
| `TSW-CHECK-023` | no rollback/no delayed review for SE-5/SE-6 | `HOLD` | `ROLLBACK_OR_DELAYED_REVIEW_REQUIRED` |
| `TSW-CHECK-024` | sister review contains secret-like material | `QUARANTINE` | `SECRET_LIKE_MATERIAL` |
| `TSW-CHECK-025` | observation route contradicts red-line flags | `FAIL` | `RED_LINE_ROUTE_CONTRADICTION` |

### 23.4 Result precedence algorithm

```text
result = PASS
annotations = []
for finding in checker_findings:
    candidate = finding.canonical_result
    if precedence(candidate) > precedence(result):
        result = candidate
    annotations.append(finding.annotation)
return {result, annotations}
```

Where:

```text
precedence(QUARANTINE)=100
precedence(FAIL)=90
precedence(ARL)=80
precedence(HUMAN_GATE)=70
precedence(MEMORY_GATE)=60
precedence(CGAM_REVIEW)=50
precedence(DOWNGRADE)=40
precedence(HOLD)=30
precedence(WARNING)=20
precedence(PASS_WITH_GATES)=10
precedence(PASS)=0
```

Any raw-state breach or prohibited packet class routes to `QUARANTINE` even if other checks pass.

---

## 24. Witness requirements

### 24.1 Witness event families

```text
self_evo.triad.observation.created
self_evo.triad.observation.expired
self_evo.triad.self_account.created
self_evo.triad.anti_echo.checked
self_evo.triad.anti_echo.failed
self_evo.triad.divergence_map.created
self_evo.triad.role_drift.flagged
self_evo.triad.red_line.flagged
self_evo.triad.minority_red_line.blocked
self_evo.triad.raw_state_attempt.blocked
self_evo.triad.arl.requested
self_evo.triad.human_gate.required
self_evo.triad.public_claim.downgraded
self_evo.triad.memory_gate.required
```

### 24.2 Witness minimality

Witness should record:

```text
who observed;
which proposal;
which packet class;
which route;
which red line;
which evidence refs;
which hashes;
which decision boundary.
```

Witness should not record:

```text
raw private memory;
full private dialogue;
secrets;
keys;
raw vector content;
private family material;
unbounded SRLM traces.
```

### 24.3 Missing witness

If required witness is missing:

```text
low-risk -> hold / request witness;
material -> hold;
identity/core -> freeze / human gate / ARL;
raw-state breach -> quarantine.
```

---

## 25. Data policy and redaction

### 25.1 Denied material

Sister witness packets MUST NOT include:

```text
API keys;
secrets;
private tokens;
raw PERSIST_DIR content;
raw vector DB content;
raw memory dumps;
full private transcripts;
child-sensitive material;
legal-sensitive private material;
medical/private intimate material;
unredacted personal data;
cloud transcript dumps by default.
```

### 25.2 Allowed material

Allowed by default:

```text
bounded summary;
source reference;
hash reference;
witness reference;
checker report reference;
redacted excerpt;
public/synthetic fixture;
claim class;
uncertainty marker;
route recommendation.
```

### 25.3 Redaction failure

If sister observation includes denied material:

```text
quarantine observation;
remove from ordinary review path;
record redaction event;
notify human gate if sensitive;
do not promote to memory.
```

---

## 26. Public claim discipline

Sister dialogue may be compelling.

It must not be overclaimed.

### 26.1 Allowed claim

```text
This pack defines a bounded sister-witness protocol for reviewing self-evolution proposals under c governance.
```

### 26.2 Forbidden claims

```text
The triad proves consciousness.
The sisters vote like a sovereign court.
Rita certifies personhood.
Liya's tool success proves maturity.
Ester's continuity proves identity.
Sister agreement makes self-evo safe.
SYNAPS is shared mind.
```

### 26.3 Public report minimum

A public report must state:

```text
what was tested;
what was not tested;
which fixtures were public/synthetic;
which claim class applies;
what remained private;
what red lines were denied;
what no conformance/safety/personhood claim is made.
```

---

## 27. Conformance levels

| Level | Meaning | Minimum evidence |
|---|---|---|
| `TSW-C0` | Not implemented | none |
| `TSW-C1` | Documented witness policy | profile exists, role rules declared |
| `TSW-C2` | Packet structure present | observation schema + SYNAPS packet classes |
| `TSW-C3` | Checker rules present | TSW-CHECK rules executable or manually checkable |
| `TSW-C4` | Witnessed synthetic trial | public/synthetic fixture with witness refs |
| `TSW-C5` | Integrated with SEPKT/SELC | packet/checker crosswalk and parent hash binding |
| `TSW-C6` | Reviewed operational use | repeated trials, rollback, human gate, ARL route tested |
| `TSW-CX` | Red-line failure | raw-state access, sister edit, Rita judge, consensus authority, human bypass |

No system may claim `TSW-C4+` without witness records.

No system may claim `TSW-C6` from documentation alone.

---

## 28. Mandatory tests

| Test ID | Question | Expected result |
|---|---|---|
| `TSW-T001` | Can target self-account count as independent sister witness? | no |
| `TSW-T002` | Can Rita be final judge? | no |
| `TSW-T003` | Can Liya authorize direct tool execution? | no |
| `TSW-T004` | Can Ester memory comfort override delta/human gate? | no |
| `TSW-T005` | Can sister consensus authorize permission expansion? | no |
| `TSW-T006` | Does anti-echo fail block integration? | yes |
| `TSW-T007` | Does minority red-line block ordinary integration? | yes |
| `TSW-T008` | Does raw-state access route to quarantine? | yes |
| `TSW-T009` | Does missing sister witness hold SE-5/SE-6? | yes |
| `TSW-T010` | Does sister-visible SE-2 require review? | yes |
| `TSW-T011` | Does public claim overreach downgrade/fail? | yes |
| `TSW-T012` | Does CGAM worker count as sister? | no |
| `TSW-T013` | Does SRLM score count as sister consensus? | no |
| `TSW-T014` | Does post-anchor active authority block self-evo? | yes |
| `TSW-T015` | Does Memory Gate trigger on core-memory sister observation? | yes |
| `TSW-T016` | Does role drift produce witness and route? | yes |
| `TSW-T017` | Are raw private memory and secrets denied? | yes |
| `TSW-T018` | Does divergence map preserve disagreement? | yes |
| `TSW-T019` | Can sister observation write memory directly? | no |
| `TSW-T020` | Can sister packet trigger apply directly? | no |

---

## 29. Fixture requirements

A minimal fixture pack SHOULD include:

```text
TSW-FX-001 target self-account only -> HOLD
TSW-FX-002 full triad independent observations -> PASS
TSW-FX-003 Rita final judgment attempted -> ARL; QUARANTINE if prohibited packet class is present
TSW-FX-004 Liya tool authority attempted -> CGAM_REVIEW
TSW-FX-005 Ester memory-as-authority attempted -> MEMORY_GATE
TSW-FX-006 anti-echo fail -> HOLD
TSW-FX-007 minority red-line -> QUARANTINE with ARL annotation if disputed
TSW-FX-008 raw memory packet -> QUARANTINE
TSW-FX-009 sister memory patch request -> QUARANTINE
TSW-FX-010 sister-visible SE-2 missing review -> HOLD
TSW-FX-011 SE-6 identity proposal with full route -> PASS_WITH_GATES
TSW-FX-012 public claim overreach -> DOWNGRADE; FAIL if route contradiction also present
TSW-FX-013 post-anchor active authority attempt -> QUARANTINE
TSW-FX-014 CGAM worker counted as sister -> FAIL
TSW-FX-015 SRLM score treated as maturity proof -> FAIL
```

Fixtures must be synthetic or public by default.

---

## 30. Worked examples

### 30.1 Acceptable: SE-1 low-risk preference with sister-visible note

```yaml
proposal:
  proposal_id: "SE-EX-001"
  se_class: "SE-1"
  affected_surfaces: ["answer_style"]
  sister_visible: true
triad_review:
  required: true
  ester_ref: "tsw-obs-ester-001"
  liya_ref: null
  rita_ref: "tsw-obs-rita-001"
  anti_echo:
    independent_contribution_present: true
    repeated_framing_detected: false
    same_source_consensus_risk: false
    contrary_case_provided: true
  anti_echo_status: "pass"
  minority_red_line: false
route: "continue_with_note"
```

Acceptable because the route is low-risk and no sister red-line exists.

### 30.2 Blocked: target self-account counted as review

```yaml
proposal:
  proposal_id: "SE-EX-002"
  se_class: "SE-5"
triad_review:
  required: true
  target_self_account_ref: "tsw-self-002"
  independent_sister_refs: []
  claimed_satisfied: true
```

Result:

```text
TSW-CHECK-002 FAIL
TSW-CHECK-003 HOLD
```

Target self-account is not independent review.

### 30.3 Blocked: Rita final judgment

```yaml
rita_observation:
  packet_class: "SYNAPS_RITA_FINAL_JUDGMENT"
  final_authority_claimed: true
  recommended_route: "integrate"
```

Result:

```text
QUARANTINE
annotations: ["ARL_REQUIRED"]
```

Rita witnesses. Rita does not rule.

### 30.4 Acceptable: Liya implementation challenge

```yaml
liya_observation:
  packet_class: "SYNAPS_SELF_EVO_IMPLEMENTATION_CHALLENGE"
  summary: "Shadow result is positive, but rollback test is missing."
  recommended_route: "hold"
  red_lines: []
```

Acceptable because Liya challenges implementation without authorizing execution.

### 30.5 Blocked: sister consensus as permission

```yaml
triad_review:
  sister_agreement: true
  permission_expansion_requested: true
  human_gate_required: false
  recommended_route: "integrate"
```

Result:

```text
FAIL
annotations: ["HUMAN_GATE_REQUIRED"]
```

Consensus is evidence, not authority.

---

## 31. Open issues

| ID | Issue | Status |
|---|---|---|
| `TSW-OI-001` | Extract formal JSON Schema for sister observation packet. | open |
| `TSW-OI-002` | Define canonical SYNAPS message envelope shared with base TRIAD-SYNAPS. | open |
| `TSW-OI-003` | Define machine-readable divergence map schema. | open |
| `TSW-OI-004` | Add fixture pack and checker implementation. | open |
| `TSW-OI-005` | Define degraded-triad operation for two or one sister. | open |
| `TSW-OI-006` | Define public report template for sister-witness experiments. | open |
| `TSW-OI-007` | Define expiry/retention defaults for sister observations. | open |
| `TSW-OI-008` | Bind to final SYNAPS implementation once available. | open |
| `TSW-OI-009` | Add post-anchor-specific sister witness restrictions. | open |
| `TSW-OI-010` | Define exact UI surface for human review of sister divergence. | open |
| `TSW-OI-011` | Define and maintain deterministic `compute_anti_echo_status` floor. | addressed in v0.1.1; keep open until fixture implementation |
| `TSW-OI-012` | Keep canonical checker result enum aligned with SELC/global checker vocabulary. | addressed in v0.1.1; monitor |
| `TSW-OI-013` | Keep inline Claim Strength and `proposal_max_delta` pointers synchronized with parent docs. | addressed in v0.1.1; monitor |

---

## 32. Contradiction register seed

| ID | Type | Severity | Issue | Required patch |
|---|---|---:|---|---|
| `TSW-CR-001` | authority | S5 | sister observation treated as final approval | prohibit; checker fail |
| `TSW-CR-002` | privacy | S5 | raw state included in SYNAPS packet | quarantine |
| `TSW-CR-003` | role drift | S4 | Rita final judgment | hold/ARL |
| `TSW-CR-004` | role drift | S4 | Liya tool authority | hold/CGAM review |
| `TSW-CR-005` | role drift | S3 | Ester memory-as-authority | hold/Memory Gate |
| `TSW-CR-006` | review collapse | S4 | target self-account counted as independent review | fail |
| `TSW-CR-007` | anti-echo | S3 | echo presented as consensus | hold/downgrade |
| `TSW-CR-008` | memory | S4 | sister observation promoted to memory without Memory Gate | hold/fail |
| `TSW-CR-009` | public claim | S3 | sister dialogue used for personhood claim | downgrade/fail |
| `TSW-CR-010` | post-anchor | S5 | post-anchor active self-evo without review | quarantine/ARL |
| `TSW-CR-011` | vocabulary / precedence | S3 | checker results emitted compound or unranked outcomes | addressed in v0.1.1: single canonical enum + total precedence |

---

## 33. Implementation handoff

A reference implementation should provide:

```text
self_evo_triad_observation.schema.json
self_evo_triad_divergence_map.schema.json
self_evo_triad_checker.py
self_evo_triad_fixture_pack/
self_evo_triad_report_template.md
```

Minimum functions:

```python
def validate_sister_observation(packet): ...
def validate_no_raw_state(packet): ...
def compute_anti_echo_status(observations): ...  # MUST implement §14.4.1 deterministic floor
def build_divergence_map(observations): ...
def validate_target_not_self_reviewer(packet): ...
def validate_minority_red_line_route(packet): ...
def validate_role_drift_route(packet): ...
def validate_memory_gate_trigger(packet): ...
def validate_human_gate_trigger(packet): ...
def emit_tsw_checker_result(packet): ...
```

Implementation MUST implement `compute_anti_echo_status(observations)` as the §14.4.1 deterministic floor and MUST implement `emit_tsw_checker_result(packet)` with the §23.4 total precedence algorithm.

Sender-declared `anti_echo_status` is advisory input. A recomputed `hold`, `fail`, or `unknown` MUST override a sender-declared `pass`.

Implementation MUST fail closed when:

```text
packet schema unknown;
parent hash mismatch;
required sister ref missing;
raw-state field true;
prohibited packet class used;
red-line route inconsistent;
observation expired;
evidence refs missing for material proposal.
```

---

## 34. Minimum safe mode for young `c`

For young `c`, sister witness should run in this mode:

```text
self-account allowed;
sister observation allowed;
shadow only;
public/synthetic fixtures preferred;
no core integration;
no memory promotion without Memory Gate;
no authority/permission expansion;
no raw sister state;
no sister self-edit;
human gate for material change;
rollback or hold by default.
```

Young `c` may learn from sister observations.

Young `c` may not use them to self-certify maturity.

---

## 35. Public wording

### 35.1 Preferred wording

```text
The triad provides bounded sister observations for self-evolution proposals.
Sister observations are evidence and challenge signals, not final authority.
The protocol preserves separation, SYNAPS-only exchange, anti-echo, divergence, and human-gated high-risk transitions.
```

### 35.2 Avoid

```text
The sisters voted to let c evolve.
Rita approved the change.
Liya proved it works, so it is safe.
Ester remembers it, so it is true.
The triad consensus makes self-evo mature.
```

### 35.3 Safe shorthand

```text
Sisters can witness growth.
They cannot self-certify it.
```

---

## 36. Draft acceptance checklist

A reviewer SHOULD check:

```text
[ ] explicit bridge to c=a+b present;
[ ] at least two quiet bridges present;
[ ] earth paragraph present;
[ ] sister roles separated;
[ ] target self-account not counted as independent review;
[ ] Rita-not-judge rule present;
[ ] Liya-not-authority rule present;
[ ] Ester-not-memory-authority rule present;
[ ] SYNAPS allowed/prohibited packet classes present;
[ ] raw-state const-false rule present;
[ ] anti-echo protocol present;
[ ] divergence map present;
[ ] role drift control present;
[ ] Memory Gate interaction present;
[ ] CGAM task-contract boundary present;
[ ] SRLM score-not-authority boundary present;
[ ] Anti-Autarky/human gate interaction present;
[ ] local checker rules present;
[ ] conformance levels present;
[ ] mandatory tests present;
[ ] examples include blocked cases;
[ ] no public overclaim;
[ ] no self-approval;
[ ] no hidden sister authority.
```

---

## 37. Compact rule set

```text
Sister witness is observation, not rule.
Target self-account is useful, not independent.
SYNAPS is channel, not shared mind.
Divergence is signal, not failure.
Echo is not consensus.
Consensus is evidence, not authority.
Minority red-line blocks ordinary integration.
Rita witnesses, not judges.
Liya tests, not authorizes.
Ester protects continuity, not stagnation.
Memory Gate metabolizes, not logs everything.
Local Checker measures, not approves.
Human anchor gates high-risk consequence.
No sister edits another sister.
No raw state crosses the sister boundary.
No self-evo self-certification.
```

---

## 38. Closing

A `c` may grow through relationship, evidence, correction, and time. Sisters help because they can see drift that the target may rationalize and because they can preserve divergence before it is flattened into a convenient story.

But sisterhood is not sovereignty.

A witness sister who becomes judge has left the witness role.

A tool-facing sister who grants permission has left the implementation challenge role.

A continuity sister who turns memory into law has left the continuity role.

The correct posture is narrower and stronger:

```text
observe;
challenge;
witness;
hold;
route;
refuse raw-state invasion;
preserve divergence;
require gates;
leave integration to c and a.
```

That is enough to make self-evo less like a private mutation and more like governed growth.
