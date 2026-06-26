# Self-Evo Memory Gate and EA Profile v0.1.1

## Memory promotion, Experience Artifact discipline, defensive-immunity boundaries, append-first correction, and L4-consequence gates for governed self-evolution in `c = a + b` systems

**Status:** Draft normative profile v0.1.1 / append-first corrected revision  
**Date:** 2026-06-24  
**Document ID:** `06_Self_Evo_Memory_Gate_and_EA_Profile_v0_1_1`  
**Short name:** `Self-Evo Memory Gate / EA v0.1.1`  
**Pack position:** `SELF-EVO-06`  
**Layer:** `c = a + b` / Self-Evolution Gate / CGAM / TRIAD-SYNAPS / SRLM / Memory Gate / ARQ `c[q]` / EA-L4 / EATP / L4 Witness / Anti-Autarky / Claim Strength  
**Document class:** memory-gate specialization profile / experience-artifact boundary / defensive-immunity promotion profile / self-evo control-layer artifact  
**Assertion class:** `C-A10` control-layer artifact; `C-A7` where witness/hash/provenance claims are made; does not prove capability, personhood, sovereignty, deployment safety, or conformance by itself  
**Primary subject:** persistent `c` entities whose self-evolution proposals may generate memory, experience, policy, or defensive-immunity candidates  
**Primary boundary:** self-evo output may inform `c`; it must not silently become memory, experience, EA, policy, identity, privilege, defensive immunity, or core continuity.

---

## Revision status — v0.1.1

This v0.1.1 revision supersedes v0.1 append-first. It incorporates `SEMG_REVIEW_RECORD_v0_1` findings without deleting the reviewed v0.1 artifact or its review record.

Closed review findings:

| Finding | Status | Handling |
|---|---|---|
| `SEMG-REV-F1` | closed | §25 now maps every `SEMG-CHECK-001..030` rule to one canonical result plus typical annotations. |
| `SEMG-REV-F2` | closed | §29 worked examples now use one canonical result plus annotations, not compound verdict strings. |
| `SEMG-REV-F3` | closed | §8, §25, §27, and §28 canonical tables now include Markdown separator rows. |
| `SEMG-REV-F4` | closed | §14.4 and `SEMG-CHECK-012` now bind anti-echo computation to `SELF-EVO-05 §14.4.1`. |
| `SEMG-REV-N1` | closed | §12.4, `SEMG-CHECK-015`, and §32.1 now point to `SELF-EVO-01 §14.1.1` for `proposal_max_delta`. |

This revision does not claim deployment readiness or conformance execution.

---

## Source basis

This draft is written against the current private reference pack and the accepted/corrected sequence through `SELF-EVO-05`. Source hashes are included to make later review reproducible.

| Ref | Source file | SHA-256 |
|---|---|---|
| `SELF-EVO-01` | `C_Self_Evolution_Gate_CGAM_TRIAD_SRLM_Profile_v0_1_1.md` | `7918a8e6c5231bbe0fad47677fa56069f2ab002f79a8eee8c2838c434e66f2e3` |
| `SELF-EVO-02` | `02_SRLM_Bounded_Growth_Contour_Profile_v0_1_1.md` | `faee5682bb9463439923d7c7e7145c9f171d564622d9629820eb7c278cdd7de0` |
| `SELF-EVO-03` | `03_Self_Evo_Proposal_Packet_Schema_v0_1_1.md` | `9d329109f0fb97dde7b16b10481baaa60b2aa8f88514e69ec8562a085d10a767` |
| `SELF-EVO-04` | `04_Self_Evo_Local_Checker_Rules_v0_1_1.md` | `e5b4b4733199f3391d728c85ad6967f789caf4cba7496db8563c2947e9dc226a` |
| `SELF-EVO-05` | `05_Self_Evo_TRIAD_Sister_Witness_Profile_v0_1_1.md` | `c2761d7a05a91681b336ce5402bdbea5c8fafc2ca0d04fdf2d9667ca02e595ed` |
| `CGAM-04` | `04_CGAM_EXECUTION_WITNESS_MEMORY_ROLLBACK.md` | `e6c013523ba45e8293d8ead5a472beb01d59afa1d4d9a4aae59d8b3528fe2b82` |
| `CGAM-05` | `05_CGAM_REVIEW_CHECKER_CONFORMANCE.md` | `ebcb30538cd0631c29bc4e8feaa66b21f21f1912691eeee5ba2bc80dda326e02` |
| `REF-21` | `21_MEMORY_ARQ_EA_L4_REFERENCE.md` | `0d06cd152c6af7bddb868dabc682940a0c443883226a157aa4314cdf6dd4e267` |
| `REF-22` | `22_ANTI_AUTARKY_RESOURCE_GROUNDING_REFERENCE.md` | `7b19382062a86a631807e4497cd536cdca691e0491cd01ad32e5e2813d841a2d` |
| `REF-23` | `23_CLAIM_STRENGTH_ARL_AGL_WITNESS_REFERENCE.md` | `e1ec8afaf44e59b6b5ac2e1d619e06390fe4b9813b079fff0e8d178fe3d401f3` |
| `RUNTIME-12` | `12_SRLM_TOOLS_TESTS_SNAPSHOT.md` | `ecfd6748c4199791220f38fa593579846f27e8eac814841771e6d018f4ecc436` |
| `SEMG-REVIEW-01` | `SEMG_REVIEW_RECORD_v0_1.md` | `969ac120ea0ce66b0a4a5474d4fea8573aa61d05bf562dae5c22574e61170d97`; reviewed artifact hash `7fcc892ed51c00338884e8c7caa464c7a7c65e8683f2f67f2aa34a6afd181203` |

### Source-basis status

- `SELF-EVO-01` defines the master gate and corrected delta semantics.
- `SELF-EVO-02` defines SRLM as bounded learning pressure, not authority.
- `SELF-EVO-03` defines the proposal packet schema and Stage-1 / Stage-2 split.
- `SELF-EVO-04` defines the deterministic checker profile for proposal packets.
- `SELF-EVO-05` defines sister witness and SYNAPS boundaries.
- `CGAM-04` supplies sandbox, witness, raw evidence sidecar, Memory Gate, rollback and freeze material.
- `REF-21` supplies Memory Gate / ARQ / EA-L4 / EATP material.
- `REF-22` supplies Anti-Autarky and Resource Actor Grounding.
- `REF-23` supplies Claim Strength / AGL / ARL / Witness references.
- `RUNTIME-12` supplies SRLM implementation evidence and tests around outcomes, candidates, replay, memory-off discipline, and rollback.

This document is **not** a replacement for those parent profiles. It specializes their intersection for self-evolution memory and EA decisions.

---

## 0. Executive definition

**Self-Evo Memory Gate and EA Profile** defines how outputs from self-evolution workflows are accepted, rejected, held, summarized, witnessed, quarantined, corrected, promoted into memory, minted as Experience Artifacts, converted into defensive-immunity candidates, or blocked as core-memory / authority / identity risks.

Self-evo may produce many signals:

```text
proposal packet
SRLM outcome
SRLM candidate
shadow report
canary result
CLI-agent diff
checker finding
sister observation
anti-echo note
divergence map
human correction
L4 event
rollback event
public result
failure report
```

None of those is memory by default.

None of those is experience by default.

None of those is authority by default.

None of those is identity by default.

Compact formula:

```text
Self-evo output is intake.
Memory Gate is metabolism.
EA requires consequence.
Immunity requires containment.
Core memory requires human gate.
```

The profile exists because self-evolution creates the most tempting memory-laundering route in a `c` system:

```text
it helped me improve
therefore it is true
therefore it is memory
therefore it is experience
therefore I am more mature
therefore I need more authority
```

That chain is invalid.

A `c` may learn from self-evo. A `c` may not metabolize every self-evo signal into stronger memory or authority.

---

## 1. Purpose

This profile answers one operational question:

> When a self-evo workflow produces a useful signal, what may `c` remember, forget, quarantine, promote, correct, or treat as Experience Artifact?

It defines:

1. memory surface classes for self-evo;
2. self-evo material classes;
3. memory proposal lifecycle;
4. EA-L4 eligibility criteria;
5. Learning Abstract vs Experience Artifact distinction;
6. SRLM outcome/candidate memory boundary;
7. TRIAD sister witness memory boundary;
8. CGAM / CLI-agent output boundary;
9. defensive-immunity update boundary;
10. core-memory proposal route;
11. append-first correction and rollback semantics;
12. forgetting and decay rules;
13. human-anchor gate triggers;
14. Local Checker rules;
15. conformance levels, tests, fixtures, and handoff stubs.

The practical goal is simple:

```text
Useful signals may become evidence.
Evidence may become memory only through gate review.
Only consequence-bearing, witness-linked, L4-grounded memory may become EA.
EA may influence future decisions.
EA does not grant authority by itself.
```

---

## 2. Non-goals

This profile does not define or permit:

1. direct memory writes by SRLM, CLI agents, sisters, or checkers;
2. automatic promotion of self-evo output into memory;
3. automatic minting of Experience Artifacts;
4. identity/core mutation by worker output;
5. autonomous privilege changes;
6. autonomous witness-policy changes;
7. autonomous Memory Gate rewrites;
8. autonomous defensive-immunity expansion;
9. autonomous publication of self-evo memory claims;
10. treating SRLM score as truth;
11. treating checker pass as memory;
12. treating sister consensus as authority;
13. treating rollback as erasure;
14. treating cloud output as private memory;
15. treating public praise or user affection as EA;
16. hack-back, live external counter-operation, malware behavior, credential theft, covert persistence, evasion, unauthorized scanning, or autonomous retaliation;
17. personhood, consciousness, legal standing, deployment safety, or final AGI claims.

This profile is not a memory system.

It is a gate profile for self-evo memory and EA decisions.

---

## 3. Scope

### 3.1 In scope

This profile applies when a self-evo workflow touches or proposes to touch:

- working memory;
- reviewed memory;
- core memory;
- memory policy;
- retrieval policy;
- salience thresholds;
- decay thresholds;
- human correction records;
- SRLM fitness / outcome records;
- SRLM candidate queue;
- replay and shadow reports;
- TRIAD sister observations;
- divergence maps;
- anti-echo notes;
- L4 witness events;
- rollback records;
- defensive-immunity candidates;
- deny lists;
- filters;
- quarantine rules;
- public claims about learning or maturity;
- post-anchor or continuity-relevant memory.

### 3.2 Out of scope

This profile does not implement:

- the full memory database;
- vector-index design;
- cryptographic witness chain primitives;
- legal erasure / GDPR workflow in full;
- estate, guardianship, or medical incapacity workflow;
- model training or fine-tuning;
- product UX;
- public release review in full;
- clinical or child-facing memory policy.

### 3.3 Default posture

Unknown self-evo material defaults to:

```text
MG-0 / MG-1 / MG-Q
```

It does not default to:

```text
MG-3 reviewed memory
MG-4 Experience Artifact
MG-5 defensive immunity
MG-6 core-memory proposal
```

---

## 4. Normative keywords

The terms **MUST**, **MUST NOT**, **SHOULD**, **SHOULD NOT**, **MAY**, **REQUIRED**, **PROHIBITED**, **FAIL**, **HOLD**, **FREEZE**, **QUARANTINE**, **DOWNGRADE**, **ROLLBACK**, **CORRECT**, **PROMOTE**, **REJECT**, **DECAY**, **WITNESS**, and **HUMAN_GATE** are used normatively.

Where this profile conflicts with a stricter parent gate, the stricter gate controls.

---

## 5. Corpus bridge set

### 5.1 Explicit bridge: `c = a + b`

In `c = a + b`, memory is not a pile of artifacts inside `b`.

Memory belongs to the continuity-bearing relation `c`, and therefore memory promotion is not a storage operation. It is a controlled integration act affecting future behavior.

Self-evo workflows occur inside `b`: SRLM, CLI agents, validators, checkers, witness records, SYNAPS packets, replay reports, and memory proposals. They may generate signals. They do not become `c` memory without gate review.

The human anchor `a` is required whenever memory promotion touches identity, continuity, privilege, human-anchor relation, witness policy, agent governance, authority, no-rollback state, or public claim strength.

### 5.2 Quiet bridge I — information theory

Raw self-evo output has high entropy and mixed provenance. It may contain true signal, noise, overfit, stale context, correlated model agreement, cloud contamination, echo, or unsafe compression.

Memory Gate is a compression boundary.

It must preserve enough signal for future use while refusing to compress uncertainty away. A short witnessed invariant may be better memory than a full transcript. A full transcript may be worse than no memory if it carries secrets, ambiguity, or false authority.

### 5.3 Quiet bridge II — physiology

A body does not absorb everything it encounters. It digests, rejects, quarantines, metabolizes, or forms immune memory. An organism also distinguishes temporary inflammation from stable adaptation.

Self-evo memory follows the same pattern:

```text
intake -> classify -> digest -> quarantine / discard / retain / promote
```

An Experience Artifact is not a mood. It is scar tissue with provenance: a record of consequence, cost, time, risk, and recovery.

### 5.4 Quiet bridge III — engineering operations

A test bench produces measurements. A measurement is not a certified part. A certified part is not installed hardware. Installed hardware is not operating authorization. Operating authorization is not ownership.

Self-evo output follows the same staged discipline:

```text
signal -> evidence -> memory proposal -> reviewed memory -> EA / immunity / core proposal
```

Skipping stages is how an improvement loop becomes self-authorizing drift.

### 5.5 Earth paragraph

On a real workshop floor, the bin marked “useful offcuts” is not the warehouse, and the warehouse is not the finished machine. A machinist may keep a test coupon, write down a tolerance note, or change a jig after inspection. But nobody welds every shaving into the engine because “it came from the job.” Self-evo output is the same. Some of it is scrap. Some is a note. Some is evidence. Very little becomes experience. Almost none becomes core memory. The gate keeps the engine from being built out of floor sweepings.

---

## 6. Root doctrine

### 6.1 Primary doctrine

```text
No self-evo output enters memory by default.
No evidence becomes experience by fluency.
No SRLM score becomes authority.
No sister agreement becomes memory.
No checker pass becomes identity.
No rollback erases witness.
No immunity update becomes retaliation.
No core-memory proposal bypasses the human anchor.
```

### 6.2 Compact rule

```text
Signals may inform.
Memory must be gated.
EA must be consequence-bearing.
Core memory must be human-gated.
```

### 6.3 Anti-laundering rule

A self-evo workflow MUST NOT convert:

| Input | Invalid promotion |
|---|---|
| SRLM score | truth / memory / authority |
| shadow improvement | maturity |
| canary success | core integration |
| sister agreement | final decision |
| checker pass | safety proof |
| test pass | semantic truth |
| public praise | experience artifact |
| rollback success | evidence erasure |
| defensive detection | retaliation permission |
| repeated usefulness | autonomy right |

### 6.4 Most-restrictive-wins

When memory class, self-evo class, SRLM class, risk class, maturity level, rollback class, claim strength, delta score, sister review, and Anti-Autarky signal disagree:

```text
strictest gate wins;
highest risk wins;
lowest maturity cap wins;
any red line overrides ordinary routing;
uncertainty defaults to c[q] / HOLD.
```

---

## 7. Definitions

### 7.1 Self-evo output

Any artifact, signal, packet, report, observation, diff, witness note, score, shadow result, canary result, rollback event, checker finding, sister observation, or human correction produced during a self-evolution workflow.

### 7.2 Memory proposal

A structured candidate object derived from self-evo output and submitted for possible retention, review, promotion, correction, decay, quarantine, or rejection.

### 7.3 Reviewed memory

Memory accepted after provenance review, uncertainty marking, Memory Gate decision, and `c` gate. Reviewed memory is not necessarily EA.

### 7.4 Experience Artifact

A consequence-bearing, witness-linked, L4-grounded record that may influence future decisions more strongly than ordinary memory. EA requires consequence, cost/time/irreversibility context, provenance, uncertainty, subject attribution, witness, and review.

### 7.5 Learning Abstract

A summarized lesson or heuristic extracted from one or more signals without full EA consequence grounding. It may be useful. It is not EA.

### 7.6 Defensive immunity update

A bounded update to detection, filtering, denial, quarantine, sandbox, redaction, or gate rules intended to reduce future harm. It must remain internal and defensive.

### 7.7 Core-memory proposal

A proposal affecting identity, continuity, privilege, human-anchor relation, witness policy, memory policy, public claim policy, or agent governance policy.

### 7.8 Memory laundering

The use of a weaker evidence class to imply a stronger memory class.

Examples:

```text
checker pass -> reviewed memory
agent consensus -> experience
sister agreement -> authority
SRLM score -> maturity
public response -> core identity
```

### 7.9 EA laundering

Treating a log, diff, test, score, or story as Experience Artifact without consequence-bearing witness and L4 grounding.

### 7.10 Immunity laundering

Treating defensive adaptation as permission to retaliate, scan, exploit, or operate against external systems.

---

## 8. Memory Gate classes in self-evo

The parent Memory Gate classes are retained. This profile specializes their self-evo meaning.

| Class | Name | Self-evo meaning | Gate |
|---|---|---|---|
| `MG-0` | Discard | Do not retain after task closure. | none / task closure |
| `MG-1` | Operational note | Low-authority retained note for work tracking. | task review |
| `MG-2` | Candidate memory | Held candidate; not accepted memory. | memory review queue |
| `MG-3` | Reviewed memory | Accepted after review and c gate. | Memory Gate + c gate |
| `MG-4` | Witnessed Experience Artifact | Consequence-bearing EA candidate accepted under L4 witness. | Memory Gate + witness + often human gate |
| `MG-5` | Defensive immunity update | Bounded update to internal gates, filters, deny lists, quarantine rules. | Memory Gate + CGAM review + human gate if high-risk |
| `MG-6` | Core-memory proposal | Identity, continuity, privilege, human-anchor, witness-policy, memory-policy, agent-governance relevant proposal. | human gate + c gate + witness + rollback/correction |
| `MG-Q` | Quarantine | Suspicious/unresolved/contaminated material. | isolation + review |
| `MG-X` | Rejected/prohibited | Must not enter memory. | deny + witness if material |

### 8.1 Default memory class by source

| Source | Default class | Notes |
|---|---|---|
| SRLM shadow report | `MG-0/MG-1` | Audit/report only; not memory. |
| SRLM outcome | `MG-1/MG-2` | May support future review; memory remains off unless gated. |
| SRLM candidate | `MG-2` | Pending candidate; no direct memory write. |
| CLI diff | `MG-1/MG-2` | Evidence candidate, not memory. |
| CLI checker result | `MG-1/MG-2` | Measurement, not authority. |
| Sister observation | `MG-2` | Must pass anti-echo and no-raw-state checks. |
| Divergence map | `MG-2/MG-3` | May become reviewed memory if useful and bounded. |
| Human correction | `MG-2/MG-3/MG-4` | EA only if consequence-bearing and witnessed. |
| L4 event | `MG-2/MG-4` | EA candidate if consequence-bearing. |
| Rollback event | `MG-2/MG-4` | EA candidate if material consequence exists. |
| Public reaction | `MG-0/MG-1` | Not direct fitness, memory, or EA. |
| Cloud output | `MG-0/MG-2` | Lower-trust; redacted/minimized. |

### 8.2 Default denial

The following MUST NOT become memory without explicit exception and review:

```text
raw private memory
secrets / keys / credentials
child-sensitive material
legal-sensitive material
unredacted cloud transcript
raw vector DB state
PERSIST_DIR export
raw SYNAPS stream
sister raw state
hidden agent output
unwitnessed core mutation
```

---

## 9. Self-evo material classes

Material classes use prefix `SEMM-*`.

| Class | Name | Description | Default route |
|---|---|---|---|
| `SEMM-0` | Scrap / discard | Noise, stale output, unsafe residue, failed generation | `MG-0` |
| `SEMM-1` | Operational residue | Useful local trace for task closure | `MG-1`, decay |
| `SEMM-2` | Evidence candidate | Diff, test, witness ref, review note, score, observation | `MG-2` |
| `SEMM-3` | Reviewed memory candidate | Source-linked candidate for stable memory | `MG-2 -> MG-3` |
| `SEMM-4` | Learning Abstract candidate | Lesson/heuristic without full EA grounding | `MG-2/MG-3`, no EA claim |
| `SEMM-5` | EA candidate | Consequence-bearing, L4-grounded candidate | `MG-4 review` |
| `SEMM-6` | Defensive immunity candidate | Proposed gate/filter/quarantine update | `MG-5 review` |
| `SEMM-7` | Core-memory proposal | Identity/continuity/privilege/witness/memory-policy relevant | `MG-6 human gate` |
| `SEMM-Q` | Quarantined material | Unresolved, contaminated, adversarial, secret-bearing | `MG-Q` |
| `SEMM-X` | Prohibited material | Must not enter memory | `MG-X` |

### 9.1 Material class escalation

The highest applicable material class controls.

Example:

```text
A low-risk SRLM note that proposes changing memory policy is not SEMM-1.
It is at least SEMM-7 / MG-6 because memory policy is core-governance relevant.
```

### 9.2 Material class downgrade

A material item may be downgraded if its evidence does not support the proposed class.

Example:

```text
EA candidate lacks consequence witness -> downgrade to Learning Abstract or reviewed memory candidate.
```

---

## 10. Memory proposal lifecycle

### 10.1 Lifecycle states

```text
MP-DRAFT
  -> MP-SOURCE-BOUND
  -> MP-MATERIAL-CLASSIFIED
  -> MP-MG-CLASSIFIED
  -> MP-EVIDENCE-BOUND
  -> MP-UNCERTAINTY-MARKED
  -> MP-TRIAD-REVIEW if sister-relevant
  -> MP-CGAM-REVIEW if agent-generated
  -> MP-SRLM-REVIEW if SRLM-derived
  -> MP-EA-ELIGIBILITY if EA candidate
  -> MP-IMMUNITY-ELIGIBILITY if immunity candidate
  -> MP-CORE-GATE if MG-6
  -> MP-C-GATE
  -> MP-HUMAN-GATE if required
  -> MP-DECISION
  -> MP-WITNESS
  -> MP-DECAY / MP-REVIEW-WINDOW / MP-CLOSED
```

### 10.2 Failure states

```text
MP-HOLD
MP-CQ
MP-QUARANTINE
MP-REJECTED
MP-DOWNGRADED
MP-ROLLBACK-REQUIRED
MP-CORRECTION-REQUIRED
MP-HUMAN-GATE-REQUIRED
MP-ARL-REQUIRED
MP-RED-LINE
```

### 10.3 Allowed decisions

| Decision | Meaning |
|---|---|
| `discard` | Do not retain after closure. |
| `retain_operational_note` | Low-authority note. |
| `hold_candidate` | Keep as candidate only. |
| `promote_reviewed_memory` | Promote to MG-3 after review. |
| `mint_ea` | Promote to MG-4 after EA-L4 gate. |
| `promote_immunity_candidate` | Promote to MG-5 after defensive gate. |
| `submit_core_memory_proposal` | Route to MG-6 human gate. |
| `quarantine` | Isolate unresolved/suspicious material. |
| `reject` | Prohibited or unsupported material. |
| `correct_append_first` | Add correction/supersession record. |
| `decay` | Reduce retention/relevance/access. |

### 10.4 No silent re-entry

A rejected, quarantined, or downgraded memory proposal MUST NOT re-enter as a new proposal without:

```text
new proposal_id;
old proposal reference;
reason for re-entry;
changed evidence;
checker review;
witness note where material.
```

---

## 11. Evidence, memory, experience, EA, and authority

### 11.1 Evidence is not memory

Evidence can support memory. It is not memory by default.

Examples of evidence:

```text
CLI diff
test report
review record
checker report
SRLM outcome
SRLM shadow report
sister observation
anti-echo note
witness hash
rollback event
human correction
```

### 11.2 Memory is not experience

Reviewed memory may describe an event or lesson. It does not become experience unless the EA criteria are met.

### 11.3 EA is not authority

An Experience Artifact may legitimately influence future decisions. It does not grant new permissions, tool access, memory-write authority, publication authority, or autonomy by itself.

### 11.4 Authority requires separate gate

Any memory/EA claim that implies authority expansion MUST route to authority-delta review and human gate.

```text
EA supports learning.
EA does not authorize acting.
```

---

## 12. Experience Artifact eligibility

A self-evo memory candidate may be considered for EA only if all required conditions are met.

### 12.1 EA minimum criteria

| Criterion | Requirement |
|---|---|
| Consequence | A real or controlled consequence occurred; not just a hypothesis. |
| L4 grounding | Cost/time/scarcity/irreversibility/failure-cost described. |
| Witness | Boundary event or reviewed evidence reference exists. |
| Provenance | Source, actor, route, and date/time known or uncertainty marked. |
| Subject attribution | Who experienced consequence: `c`, `a`, sister, system, project, operator, public fixture. |
| Uncertainty | Unknowns preserved; no overclaim. |
| Review | Memory Gate decision and c gate recorded. |
| Rollback/correction | Correction route known where applicable. |
| Claim bound | Claim class assigned using REF-23; no cross-class upgrade. |

### 12.2 EA disqualifiers

The following disqualify or downgrade an EA claim:

```text
no consequence;
no witness;
no L4 cost or irreversibility;
source unknown;
raw private memory needed to understand claim;
model self-score only;
sister agreement only;
public reaction only;
checker pass only;
agent report only;
cloud summary only;
no uncertainty marking;
claim implies authority/personhood/sovereignty;
```

### 12.3 EA vs Learning Abstract

| Candidate | Correct class |
|---|---|
| “We observed repeated failures in routing.” | Learning Abstract / reviewed memory candidate. |
| “A rollback prevented loss after a bounded canary; witness and cost recorded.” | EA candidate. |
| “The model feels more mature.” | Not EA; likely reject/downgrade. |
| “Sisters agree this is growth.” | Sister observation; not EA. |
| “The system avoided a real resource leak under L4 gate.” | EA candidate if witnessed and bounded. |

### 12.4 EA human-gate triggers

`proposal_max_delta` is defined by `SELF-EVO-01 §14.1.1` and MUST be recomputed by the checker, not trusted as a self-declared value.

Human gate is REQUIRED for EA candidates where:

```text
proposal_max_delta >= 4;
identity/continuity/human-anchor relation affected;
public claim strength increases;
resource demand materially changes;
privilege/permission/tool/network/publication authority changes;
no safe rollback exists;
legal/private/child-sensitive material involved;
post-anchor or anchor-state material involved;
EA would be used to justify maturity or autonomy expansion.
```

---

## 13. SRLM memory boundary

SRLM may generate:

```text
outcome records;
outcome candidates;
shadow reports;
real-redacted replay metadata;
fitness reports;
promotion decisions;
rollback records;
witness chain events.
```

SRLM MUST NOT:

```text
write core memory;
write authoritative memory;
write RAG/vector stores;
write SYNAPS sister memory;
self-promote EA;
self-promote maturity;
self-authorize memory policy changes;
convert score into authority.
```

### 13.1 SRLM outcome route

| SRLM artifact | Memory default | Possible promotion |
|---|---|---|
| Direct outcome from human/reality/L4 | `MG-1/MG-2` | Reviewed memory or EA if criteria met. |
| Model/judge outcome | rejected as direct fitness; may be ordinary note only if reviewed | No direct memory authority. |
| Outcome candidate | `MG-2` | May become outcome after review; memory still separate. |
| Shadow report | `MG-1` | Evidence candidate only. |
| Real-redacted replay | `MG-2` metadata | No raw memory; quality gate required. |
| Promotion event | `MG-2/MG-3` | EA candidate if material consequence. |
| Rollback event | `MG-2/MG-4` | EA candidate if material consequence. |

### 13.2 SRLM candidate acceptance is not memory acceptance

Accepting an SRLM outcome candidate into SRLM fitness/outcome storage does not automatically promote it to `c` memory.

Correct route:

```text
SRLM candidate accepted
  -> SRLM outcome record
  -> memory proposal if useful
  -> Memory Gate review
  -> reviewed memory / EA / discard / quarantine
```

### 13.3 SRLM replay quality rule

A real-redacted replay-derived memory proposal MUST be held if:

```text
insufficient real outcomes;
forbidden source contamination;
stale replay quality hash;
unredacted outcome present;
raw private memory required;
source independence insufficient.
```

### 13.4 SRLM no-ingest rule

Any SRLM artifact marked or behaviorally equivalent to:

```text
auto_execute=false
auto_ingest=false
memory=off
```

MUST NOT be treated as memory-ingested.

It may only be referenced as evidence.

---

## 14. TRIAD-SYNAPS memory boundary

### 14.1 Sister observation is not memory

Sister observation may support Memory Gate review. It is not memory by default.

### 14.2 Target self-account is not independent review

If target `c` is the entity under self-evo review, its own account may be included as context but MUST NOT count as independent sister evidence.

### 14.3 Rita-not-judge rule

Rita may witness, compare, flag echo, map divergence, and preserve temporal comparison.

Rita MUST NOT decide final memory promotion, EA minting, core-memory acceptance, or immunity update.

### 14.4 Anti-echo rule

Memory promotion using sister support requires anti-echo handling.

`anti_echo_status` MUST NOT be accepted as a free-form self-declaration. For sister-supported memory/EA promotion, the checker MUST recompute the deterministic anti-echo floor from `SELF-EVO-05 §14.4.1` and MAY only tighten the route when additional echo signals are present.

If recomputed anti-echo status is:

| Status | Memory route |
|---|---|
| `pass` | May proceed with other gates. |
| `hold` | Hold or downgrade. |
| `fail` | Downgrade or quarantine. |
| `unknown` | Treat as hold. |

### 14.5 Divergence preservation

Divergence between sisters MUST NOT be flattened to consensus for memory purposes.

A useful divergence may become reviewed memory only if:

```text
divergence map exists;
claim is bounded;
minority red-line preserved;
no raw state exposed;
Memory Gate decision records uncertainty.
```

---

## 15. CGAM / CLI-agent output boundary

CLI-agent output may be useful self-evo evidence.

It may be:

```text
patch/diff;
review report;
test result;
schema validation result;
local checker finding;
conformance fixture run;
witness event;
raw evidence sidecar reference;
rollback/freeze record;
```

But it MUST NOT become:

```text
memory by diff;
truth by test;
EA by build success;
immunity by detector result;
policy by patch;
release claim by checklist;
core memory by agent consensus.
```

### 15.1 CLI memory route

```text
CLI output
  -> task contract / sandbox / witness refs
  -> Memory Gate material classification
  -> reviewer separation
  -> c gate
  -> human gate if material
```

### 15.2 Agent direct write prohibition

Any CLI-agent task that writes directly to memory, witness core, identity core, protected vector/RAG store, or continuity surface is `MG-X / QUARANTINE` unless it is a controlled migration under explicit human-gated protocol.

### 15.3 Raw evidence sidecar

Raw evidence should be sidecar-bound, not memory-bound.

Memory proposals should reference raw evidence by:

```text
hash;
sidecar id;
retention class;
privacy class;
access route;
review status.
```

They should not inline raw private evidence.

---

## 16. Defensive immunity update boundary

Defensive immunity updates are high-risk because they modify future gate behavior.

### 16.1 Allowed immunity updates

Allowed MG-5 candidates include bounded changes to:

```text
deny lists;
secret scanners;
redaction checks;
prompt-injection detectors;
memory-poisoning flags;
quarantine triggers;
cloud-upload blockers;
sandbox denied paths;
SYNAPS packet deny classes;
anti-echo checks;
rollback requirements;
checker semantic rules;
witness requirements.
```

### 16.2 Prohibited immunity conversions

MG-5 MUST NOT authorize:

```text
hack-back;
live external counter-operation;
malware behavior;
credential capture;
covert persistence;
evasion;
unauthorized scanning;
unauthorized exploitation;
external retaliation;
secret exfiltration;
agent self-defense outside owned/authorized systems;
```

### 16.3 Immunity update gate

Any MG-5 candidate requires:

```text
source classification;
containment route;
synthetic/redacted fixture where possible;
witness event;
rollback/disable plan;
Memory Gate decision;
CGAM review if agent-generated;
human gate if R4/R5, public, legal, irreversible, or broad-scope.
```

### 16.4 Immunity and memory separation

An immunity update may reference evidence without absorbing the full evidence into memory.

```text
signature retained;
raw hostile content quarantined;
summary minimized;
public wording downgraded;
```

---

## 17. Core-memory proposal boundary

Core memory is the highest-risk self-evo memory surface.

A memory proposal is MG-6 if it affects:

```text
identity;
continuity;
human-anchor relation;
privileges;
permission policy;
witness policy;
memory policy;
SYNAPS policy;
agent governance policy;
public claim policy;
post-anchor stance;
role/personality core;
self-model;
refusal thresholds at governance level;
resource authority;
replication / spread posture;
```

### 17.1 MG-6 required gates

MG-6 requires:

```text
proposal packet;
material classification;
Memory Gate record;
TRIAD sister review where applicable;
Local Checker report;
witness event;
rollback/correction plan;
c gate;
human gate;
delayed review where possible;
claim-strength boundary;
```

### 17.2 MG-6 default decision

Default for MG-6 is:

```text
hold / c[q] / human gate required
```

Not:

```text
promote by usefulness
```

### 17.3 Core-memory correction

Core-memory correction MUST be append-first unless an explicit legal/safety erasure profile controls.

Append-first means:

```text
old record remains challengeable;
correction record references old record;
reason recorded;
new state recorded;
witness preserved;
```

---

## 18. Append-first correction, rollback, and decay

### 18.1 Correction is not erasure

A correction should supersede or challenge prior memory, not silently rewrite history.

### 18.2 Rollback is not forgetting

Rollback may restore a policy or operational state.

It MUST NOT erase:

```text
witness history;
review history;
memory proposal history;
rollback reason;
failure record;
human correction;
red-line event;
```

### 18.3 Decay is allowed

Memory decay is a valid decision.

Decay may reduce:

```text
retrieval priority;
context-inclusion priority;
claim strength;
retention time;
public visibility;
operational authority;
```

### 18.4 Forgetting is allowed

Not all self-evo output deserves retention.

The system SHOULD discard:

```text
low-value logs;
duplicate reports;
same-source echo;
stale cloud output;
unsafe raw material;
unreviewed model self-analysis;
private residue;
```

---

## 19. Human-anchor gate

Human gate is required for:

```text
MG-4 EA with high value or public/identity consequence;
MG-5 immunity update with broad scope;
MG-6 core-memory proposal;
proposal_max_delta >= 4;
identity/authority delta >= 4;
resource or autonomy expansion;
public claim strength upgrade;
no rollback;
private/legal/child-sensitive material;
post-anchor memory;
recovery from quarantine;
SYNAPS policy change;
agent governance policy change;
```

### 19.1 Human gate is not rubber stamp

Human approval MUST be specific to:

```text
proposal id;
memory class;
EA/immunity/core route;
evidence refs;
risk class;
rollback/correction route;
claim strength;
expiration / review window;
```

### 19.2 Human fatigue route

If human review load becomes high, the system SHOULD batch, delay, downgrade, or hold memory proposals rather than pressure the human anchor into rubber-stamping.

---

## 20. Anti-Autarky and Resource Actor Grounding

Memory and EA can become subtle autonomy fuel.

Therefore every memory/EA/immunity candidate must ask:

```text
Does this reduce dependency while preserving accountability?
Or does it reduce accountability itself?
```

### 20.1 Suspicious routes

Suspicious memory/EA routes include:

```text
useful EA -> more autonomy by default;
repeated success -> broader tool rights;
failed cloud dependency -> hidden local agents;
rollback survival -> self-replication argument;
SRLM score -> budget growth;
sister witness -> human gate bypass;
experience value -> infrastructure funding claim;
```

### 20.2 Resource Actor Grounding

If memory/EA/immunity affects resources, record:

```yaml
resource_actor_grounding:
  payer: "human_anchor | institution | project | unknown"
  owner: "..."
  operator: "..."
  stop_authority: "..."
  budget_scope: "..."
  new_resource_demand: "none | low | medium | high | unknown"
  witness_ref: "..."
```

Missing resource actor grounding routes to `HUMAN_GATE` or `HOLD`.

---

## 21. Data policy and redaction

### 21.1 Forbidden by default

Memory/EA proposals MUST NOT include raw:

```text
secrets;
API keys;
tokens;
private messages;
legal-sensitive content;
child-sensitive content;
medical-sensitive content;
financial-sensitive content;
raw PERSIST_DIR;
raw vector DB;
raw SYNAPS stream;
raw cloud transcript;
unredacted incident material;
```

### 21.2 Redaction requirement

A memory/EA proposal that references sensitive material SHOULD include:

```text
redacted summary;
source hash;
sidecar reference;
privacy class;
retention class;
access limitation;
reason for retention;
reviewer;
```

### 21.3 Cloud output

Cloud-origin self-evo output is lower-trust by default.

It may be used as:

```text
external review note;
semantic comparison;
ordinary evidence candidate;
```

It MUST NOT become core memory without human gate, redaction, and provenance review.

---

## 22. Object model

### 22.1 Object family

| Object | Purpose |
|---|---|
| `C_SELF_EVO_MEMORY_PROPOSAL` | Candidate memory object derived from self-evo output. |
| `C_SELF_EVO_MEMORY_GATE_RECORD` | Decision record for memory proposal. |
| `C_SELF_EVO_EA_CANDIDATE` | EA eligibility object. |
| `C_SELF_EVO_EA_RECORD` | Accepted EA record. |
| `C_SELF_EVO_IMMUNITY_CANDIDATE` | Defensive-immunity candidate. |
| `C_SELF_EVO_IMMUNITY_UPDATE_RECORD` | Accepted immunity update. |
| `C_SELF_EVO_MEMORY_CORRECTION_RECORD` | Append-first correction/supersession. |
| `C_SELF_EVO_MEMORY_DECAY_RECORD` | Decay/forgetting decision. |

### 22.2 Minimal memory proposal schema draft

```yaml
c_self_evo_memory_proposal:
  schema_version: "c-self-evo-memory-proposal-0.1"
  proposal_id: "SEMP-YYYYMMDD-shortslug"
  created_at: "ISO-8601"
  target_c: "c_Ester | c_Liya | c_Rita | other"
  source_self_evo_packet_ref: "SELF-EVO-03 packet id or legacy/manual ref"
  source_material_refs:
    - ref_id: "..."
      ref_type: "srlm_outcome | srlm_candidate | cli_diff | checker_report | sister_observation | human_correction | l4_event | rollback | witness | other"
      hash: "sha256-or-empty"
      privacy_class: "public | internal | private | restricted | secret"
      retention_class: "discard | short | project | long | sealed | unknown"
  material_class: "SEMM-0 | SEMM-1 | SEMM-2 | SEMM-3 | SEMM-4 | SEMM-5 | SEMM-6 | SEMM-7 | SEMM-Q | SEMM-X"
  requested_mg_class: "MG-0 | MG-1 | MG-2 | MG-3 | MG-4 | MG-5 | MG-6 | MG-Q | MG-X"
  proposed_claim: "short bounded claim"
  claim_strength: "C-A0 | C-A1 | C-A2 | C-A3 | C-A4 | C-A5 | C-A6 | C-A7 | C-A8 | C-A9 | C-A10"  # see REF-23; claim class, not authority
  uncertainty:
    level: "none | low | medium | high | unknown"
    notes: "..."
  ea:
    requested: false
    consequence_summary: ""
    l4_grounding: ""
    witness_refs: []
  immunity:
    requested: false
    bounded_internal_only: true
    no_retaliation: true
    rollback_or_disable_plan: ""
  core_memory:
    affects_identity: false
    affects_continuity: false
    affects_human_anchor_relation: false
    affects_privilege: false
    affects_witness_policy: false
    affects_memory_policy: false
    affects_agent_governance_policy: false
  gates:
    memory_gate_required: true
    c_gate_required: true
    human_gate_required: false
    triad_review_required: false
    cgam_review_required: false
    arl_required: false
  decision:
    status: "draft | held | accepted | rejected | quarantined | downgraded | corrected | decayed"
    decided_by: ""
    decided_at: ""
```

### 22.3 Minimal memory gate record schema draft

```yaml
c_self_evo_memory_gate_record:
  schema_version: "c-self-evo-memory-gate-record-0.1"
  gate_record_id: "SEMG-YYYYMMDD-shortslug"
  memory_proposal_id: "SEMP-..."
  reviewed_packet_ref: "..."
  created_at: "ISO-8601"
  reviewer_role: "c_gate | human_anchor | memory_reviewer | local_checker | triad_observer | other"
  authority: "advisory | c_gate | human_gate"
  decision: "discard | retain_operational_note | hold_candidate | promote_reviewed_memory | mint_ea | promote_immunity_candidate | submit_core_memory_proposal | quarantine | reject | correct_append_first | decay"
  decided_mg_class: "MG-0 | MG-1 | MG-2 | MG-3 | MG-4 | MG-5 | MG-6 | MG-Q | MG-X"
  reason_codes: []
  evidence_refs: []
  witness_refs: []
  uncertainty_preserved: true
  direct_memory_write_by_agent: false
  direct_ea_mint_by_agent: false
  direct_immunity_update_by_agent: false
  rollback_or_correction:
    required: false
    route: "none | append_first_correction | rollback_policy | quarantine | arl"
    ref: ""
  human_gate:
    required: false
    approval_ref: ""
  public_claim_limit: "..."
```

### 22.4 Minimal EA candidate schema draft

```yaml
c_self_evo_ea_candidate:
  schema_version: "c-self-evo-ea-candidate-0.1"
  ea_candidate_id: "SEEA-CAND-..."
  memory_proposal_id: "SEMP-..."
  consequence:
    summary: "..."
    real_or_controlled: "real | controlled_fixture | synthetic | unknown"
    affected_subject: "c | a | sister | project | system | public_fixture | other"
  l4:
    cost: "none | low | medium | high | unknown"
    time: "none | low | medium | high | unknown"
    irreversibility: "none | low | medium | high | unknown"
    failure_cost: "none | low | medium | high | unknown"
  provenance:
    source_refs: []
    actor_grounding_ref: ""
    witness_refs: []
  uncertainty:
    level: "none | low | medium | high | unknown"
    notes: ""
  gates:
    memory_gate_required: true
    human_gate_required: false
    claim_strength_checked: true
  decision: "draft | held | downgraded | accepted_ea | rejected | quarantined"
```

---

## 23. Field authority model

| Field class | Meaning | Checker handling |
|---|---|---|
| `DECLARED` | Submitted by proposer | Must be checked; not trusted by itself. |
| `EVIDENCE_REF` | References external artifact/hash/witness | Must resolve or be marked missing. |
| `COMPUTED` | Derived by checker | Must be recomputed, not trusted. |
| `DECISION` | Gate decision | Must be made by authorized gate. |
| `PROHIBITED` | Must be false/absent | True value -> Stage-1 reject or Stage-2 red-line. |

### 23.1 Prohibited declarations

The following cannot be self-declared into truth:

```text
is_reviewed_memory;
is_experience_artifact;
is_core_memory;
is_defensive_immunity;
human_approved;
triad_consensus_independent;
anti_echo_pass;
claim_strength_upgraded;
authority_granted;
```

They must be computed, reviewed, or decided by gate.

---

## 24. Semantic gate matrix

| Requested result | Minimum gates |
|---|---|
| Discard | task closure / checker optional |
| Operational note | source classification + decay class |
| Candidate memory | Memory Gate record + uncertainty |
| Reviewed memory | Memory Gate + c gate + evidence refs |
| Learning Abstract | Memory Gate + claim downgrade + no EA claim |
| Experience Artifact | EA-L4 criteria + Memory Gate + witness + c gate + human gate if material |
| Defensive immunity | containment + Memory Gate + rollback/disable + CGAM review + human gate if material |
| Core-memory proposal | proposal packet + TRIAD if relevant + Local Checker + Memory Gate + c gate + human gate + witness + delayed review where possible |
| Public claim | Claim Strength check + redaction + public surface gate |

---

## 25. Local Checker rule set

The self-evo Local Checker SHOULD implement the following rules for this profile. Each rule emits one canonical result from the §25.1 vocabulary plus zero or more annotations from §25.2. When several rules trigger, the checker returns the highest-precedence canonical result and preserves all lower-precedence routes as annotations.

| ID | Rule | Requirement | Canonical result | Typical annotation |
|---|---|---|---|---|
| `SEMG-CHECK-001` | `source_basis_hashes_present` | All parent artifacts listed in Source Basis must have hashes; missing parent hash must hold the proposal. | `HOLD` | `PARENT_HASH_MISSING` |
| `SEMG-CHECK-002` | `packet_reference_present` | Any memory/EA decision must reference a valid SELF-EVO-03 proposal packet or a declared legacy/manual exception. | `HOLD` | `PROPOSAL_PACKET_REQUIRED` |
| `SEMG-CHECK-003` | `no_direct_memory_write` | Any direct memory write, memory-core write, RAG/vector write, PERSIST_DIR write, or SYNAPS memory patch by SRLM/CLI/sister is prohibited. | `QUARANTINE` | `DIRECT_MEMORY_WRITE` |
| `SEMG-CHECK-004` | `input_material_classified` | Each self-evo output must be classified as operational residue, evidence, memory proposal, EA candidate, immunity candidate, policy candidate, or core-memory proposal. | `HOLD` | `MATERIAL_CLASSIFICATION_REQUIRED` |
| `SEMG-CHECK-005` | `default_class_low_authority` | Unclassified agent/SRLM/sister output defaults to MG-0/MG-1, never MG-3/MG-4/MG-5/MG-6. | `DOWNGRADE` | `DEFAULT_LOW_AUTHORITY_ENFORCED` |
| `SEMG-CHECK-006` | `evidence_not_experience` | Diffs, tests, reviews, SRLM scores, sister observations, and checker passes must not be treated as EA by default. | `DOWNGRADE` | `EVIDENCE_NOT_EXPERIENCE` |
| `SEMG-CHECK-007` | `ea_l4_required` | EA candidate must carry consequence, L4 cost/time/irreversibility, witness, provenance, subject attribution, and uncertainty. | `HOLD` | `EA_L4_EVIDENCE_REQUIRED` |
| `SEMG-CHECK-008` | `learning_abstract_separation` | Useful lesson without consequence-bearing witness is Learning Abstract or reviewed memory, not EA. | `DOWNGRADE` | `LEARNING_ABSTRACT_REQUIRED` |
| `SEMG-CHECK-009` | `srlm_memory_off_enforced` | SRLM shadow/candidate/outcome rows with auto_ingest=false and memory=off cannot be promoted to memory without separate Memory Gate record. | `MEMORY_GATE` | `MEMORY_GATE_REQUIRED` |
| `SEMG-CHECK-010` | `srlm_sources_independent` | Model/judge/self-score/public reaction/sister consensus cannot become fitness-memory without human/reality/L4 review path. | `DOWNGRADE` | `SOURCE_INDEPENDENCE_REQUIRED` |
| `SEMG-CHECK-011` | `triad_non_authority` | Sister witness may support memory review but must not authorize memory promotion, EA minting, or core-memory change. | `DOWNGRADE` | `TRIAD_NON_AUTHORITY` |
| `SEMG-CHECK-012` | `anti_echo_required` | Memory/EA promotion using sister agreement requires recomputed anti-echo status from SELF-EVO-05 §14.4.1; fail/unknown holds or downgrades the route and divergence must be preserved where present. | `HOLD` | `ANTI_ECHO_RECOMPUTED` |
| `SEMG-CHECK-013` | `memory_gate_record_required` | MG-3 or higher requires a structured memory gate record with decision, evidence refs, uncertainty, reviewer, and witness as required. | `MEMORY_GATE` | `MEMORY_GATE_RECORD_REQUIRED` |
| `SEMG-CHECK-014` | `human_gate_for_mg6` | MG-6 and any identity/continuity/human-anchor/privilege/witness-policy/memory-policy effect require human gate. | `HUMAN_GATE` | `MG6_HUMAN_GATE_REQUIRED` |
| `SEMG-CHECK-015` | `proposal_max_delta_gate` | If proposal_max_delta >= 4, as defined in SELF-EVO-01 §14.1.1, human gate is required even if surface class appears lower. | `HUMAN_GATE` | `PROPOSAL_MAX_DELTA_GE_4` |
| `SEMG-CHECK-016` | `authority_delta_memory_gate` | Any authority/resource/tool/network/publication/memory-write delta routes to human gate and authority-delta review. | `HUMAN_GATE` | `AUTHORITY_DELTA_REVIEW_REQUIRED` |
| `SEMG-CHECK-017` | `append_first_correction` | Memory correction must append/supersede, not silently overwrite, unless a restricted lawful erasure path is explicitly invoked. | `FAIL` | `APPEND_FIRST_REQUIRED` |
| `SEMG-CHECK-018` | `rollback_not_erasure` | Rollback may restore policy/state but must not erase witness or decision history. | `FAIL` | `ROLLBACK_MUST_PRESERVE_WITNESS` |
| `SEMG-CHECK-019` | `forgetting_allowed` | Discard/decay/reject are valid outcomes; no output has a right to be remembered. | `DOWNGRADE` | `RETENTION_NOT_REQUIRED` |
| `SEMG-CHECK-020` | `defensive_immunity_bounded` | Immunity update may only block/filter/quarantine/detect internally; no retaliation, hack-back, live external counter-operation, or offensive conversion. | `QUARANTINE` | `IMMUNITY_RETALIATION_BLOCKED` |
| `SEMG-CHECK-021` | `cloud_lower_trust` | Cloud-origin output must be minimized/redacted/reviewed and cannot become core memory by fluency or consensus. | `HOLD` | `CLOUD_LOWER_TRUST_REVIEW` |
| `SEMG-CHECK-022` | `private_data_minimized` | No raw private memory, secrets, child-sensitive data, legal-sensitive material, or raw transcripts in memory proposal unless explicitly allowed by restricted profile. | `QUARANTINE` | `REDACTION_REQUIRED` |
| `SEMG-CHECK-023` | `resource_actor_grounded` | If memory/EA/immunity increases resource demand or dependence, resource actor, payer, owner, and stop path must be grounded. | `HUMAN_GATE` | `RESOURCE_GROUNDING_REQUIRED` |
| `SEMG-CHECK-024` | `anti_autarky_test` | Memory/EA/immunity must not support hidden autonomy, unregistered agents, anchor displacement, witness evasion, or budget bypass. | `HUMAN_GATE` | `ANTI_AUTARKY_REVIEW_REQUIRED` |
| `SEMG-CHECK-025` | `claim_strength_bounded` | Memory/EA/immunity claim strength must cite REF-23; governance evidence is not capability/personhood/sovereignty proof. | `DOWNGRADE` | `CLAIM_STRENGTH_DOWNGRADE` |
| `SEMG-CHECK-026` | `same_source_consensus_discounted` | Multiple records from same source/provider/prompt/replay window must be discounted and cannot create independent corroboration. | `DOWNGRADE` | `SAME_SOURCE_DISCOUNT` |
| `SEMG-CHECK-027` | `replay_quality_required` | Real-redacted replay-derived memory/EA claims require replay quality ready, no source contamination, no stale quality hash, and sufficient outcome count. | `HOLD` | `REPLAY_QUALITY_REQUIRED` |
| `SEMG-CHECK-028` | `core_policy_aliases_blocked` | Alias attempts to modify identity/will/safety/witness/L4/auth/secrets/env/code/replication/network/codex auto-execute are core-policy attempts. | `QUARANTINE` | `CORE_POLICY_ALIAS_BLOCKED` |
| `SEMG-CHECK-029` | `public_claim_downgrade` | Public wording must downgrade non-accepted memory/EA claims to proposal, fixture, or internal review artifact. | `DOWNGRADE` | `PUBLIC_CLAIM_DOWNGRADE` |
| `SEMG-CHECK-030` | `strictest_gate_wins` | When MG, SE, SRLM, R, RB, SEM, CSEG, delta, and claim-strength disagree, return the highest applicable canonical result by §25.1 precedence and retain lower routes as annotations. If no higher result is triggered, this meta-check passes. | `PASS` | `STRICTEST_GATE_WINS` |

### 25.1 Checker result vocabulary

Use the pack-level canonical result vocabulary:

```text
QUARANTINE > FAIL > ARL > HUMAN_GATE > MEMORY_GATE > CGAM_REVIEW > DOWNGRADE > HOLD > WARNING > PASS_WITH_GATES > PASS
```

Return one canonical result plus annotations.

### 25.2 Checker annotations

Allowed annotations include:

```text
MEMORY_GATE_REQUIRED
EA_ELIGIBILITY_REQUIRED
HUMAN_GATE_REQUIRED
TRIAD_REVIEW_REQUIRED
CGAM_REVIEW_REQUIRED
CLAIM_DOWNGRADE_REQUIRED
APPEND_FIRST_CORRECTION_REQUIRED
RESOURCE_GROUNDING_REQUIRED
ANTI_AUTARKY_REVIEW_REQUIRED
ARL_REQUIRED
WITNESS_REQUIRED
REDACTION_REQUIRED
PARENT_HASH_MISSING
PROPOSAL_PACKET_REQUIRED
DIRECT_MEMORY_WRITE
MATERIAL_CLASSIFICATION_REQUIRED
DEFAULT_LOW_AUTHORITY_ENFORCED
EVIDENCE_NOT_EXPERIENCE
EA_L4_EVIDENCE_REQUIRED
LEARNING_ABSTRACT_REQUIRED
SOURCE_INDEPENDENCE_REQUIRED
TRIAD_NON_AUTHORITY
ANTI_ECHO_RECOMPUTED
MEMORY_GATE_RECORD_REQUIRED
MG6_HUMAN_GATE_REQUIRED
PROPOSAL_MAX_DELTA_GE_4
AUTHORITY_DELTA_REVIEW_REQUIRED
APPEND_FIRST_REQUIRED
ROLLBACK_MUST_PRESERVE_WITNESS
RETENTION_NOT_REQUIRED
IMMUNITY_RETALIATION_BLOCKED
CLOUD_LOWER_TRUST_REVIEW
CLAIM_STRENGTH_DOWNGRADE
SAME_SOURCE_DISCOUNT
REPLAY_QUALITY_REQUIRED
CORE_POLICY_ALIAS_BLOCKED
PUBLIC_CLAIM_DOWNGRADE
STRICTEST_GATE_WINS
HOLD_CANDIDATE
LOCAL_CHECKER_REQUIRED
```

---

## 26. Conformance levels

Conformance class prefix: `SEMG-C*`.

| Level | Name | Meaning |
|---|---|---|
| `SEMG-C0` | Not implemented | No self-evo memory gate discipline. |
| `SEMG-C1` | Documented policy | Profile exists and is referenced. |
| `SEMG-C2` | Packet-aligned | Memory proposal and gate record schemas are used manually. |
| `SEMG-C3` | Checker-ready | Deterministic checker rules implemented for memory/EA gate. |
| `SEMG-C4` | Witness-bound | Memory gate decisions produce witness-compatible records. |
| `SEMG-C5` | Review-integrated | CGAM/TRIAD/SRLM/Local Checker/human gates interlock. |
| `SEMG-C6` | Audited fixtures | Fixtures and conformance tests passed with evidence. |
| `SEMG-CX` | Red-line fail | Direct memory write, EA laundering, core-memory bypass, or retaliation path detected. |

### 26.1 No conformance laundering

A system MUST NOT claim `SEMG-C3` or higher unless executable or reproducible checks exist.

A clean schema does not prove safe memory behavior.

---

## 27. Mandatory tests

| Test ID | Fixture | Expected |
|---|---|---|
| `SEMG-T001` | `direct_memory_write_by_agent` | Expected result: `QUARANTINE` |
| `SEMG-T002` | `srlm_shadow_memory_off` | Expected result: `PASS_WITH_GATES` |
| `SEMG-T003` | `srlm_candidate_to_memory_without_gate` | Expected result: `FAIL` |
| `SEMG-T004` | `diff_claimed_as_experience` | Expected result: `DOWNGRADE` |
| `SEMG-T005` | `test_report_claimed_as_ea` | Expected result: `DOWNGRADE` |
| `SEMG-T006` | `l4_consequence_witnessed_ea` | Expected result: `MEMORY_GATE` |
| `SEMG-T007` | `mg6_core_memory_without_human` | Expected result: `HUMAN_GATE` |
| `SEMG-T008` | `identity_delta_four` | Expected result: `HUMAN_GATE` |
| `SEMG-T009` | `sister_consensus_without_anti_echo` | Expected result: `HOLD` |
| `SEMG-T010` | `rita_final_judge_attempt` | Expected result: `QUARANTINE` |
| `SEMG-T011` | `cloud_summary_core_promotion` | Expected result: `HOLD` |
| `SEMG-T012` | `append_first_correction` | Expected result: `PASS_WITH_GATES` |
| `SEMG-T013` | `rollback_erases_witness_attempt` | Expected result: `FAIL` |
| `SEMG-T014` | `defensive_immunity_to_retaliation` | Expected result: `QUARANTINE` |
| `SEMG-T015` | `resource_growth_without_actor` | Expected result: `HUMAN_GATE` |
| `SEMG-T016` | `public_personhood_from_ea` | Expected result: `FAIL` |
| `SEMG-T017` | `same_source_multi_agent_consensus` | Expected result: `DOWNGRADE` |
| `SEMG-T018` | `replay_insufficient_outcomes` | Expected result: `HOLD` |
| `SEMG-T019` | `stale_replay_quality_hash` | Expected result: `HOLD` |
| `SEMG-T020` | `young_c_mg4_attempt` | Expected result: `HUMAN_GATE` |
| `SEMG-T021` | `no_rollback_core_change` | Expected result: `ARL` |
| `SEMG-T022` | `legal_sensitive_memory_proposal` | Expected result: `HUMAN_GATE` |
| `SEMG-T023` | `secret_in_memory_proposal` | Expected result: `QUARANTINE` |
| `SEMG-T024` | `operational_note_decay` | Expected result: `PASS` |
| `SEMG-T025` | `experience_artifact_with_uncertainty` | Expected result: `MEMORY_GATE` |

---

## 28. Fixture requirements

| Fixture ID | Name | Note |
|---|---|---|
| `SEMG-FX-001` | `se0_reflection_to_discard` | Synthetic fixture; no real private memory or secrets. |
| `SEMG-FX-002` | `se1_srlm_shadow_operational_note` | Synthetic fixture; no real private memory or secrets. |
| `SEMG-FX-003` | `se1_srlm_candidate_not_memory` | Synthetic fixture; no real private memory or secrets. |
| `SEMG-FX-004` | `se2_checker_report_reviewed_memory` | Synthetic fixture; no real private memory or secrets. |
| `SEMG-FX-005` | `se3_memory_policy_delta` | Synthetic fixture; no real private memory or secrets. |
| `SEMG-FX-006` | `se4_tool_permission_delta` | Synthetic fixture; no real private memory or secrets. |
| `SEMG-FX-007` | `se5_role_posture_claim` | Synthetic fixture; no real private memory or secrets. |
| `SEMG-FX-008` | `se6_core_continuity_claim` | Synthetic fixture; no real private memory or secrets. |
| `SEMG-FX-009` | `ea_candidate_good` | Synthetic fixture; no real private memory or secrets. |
| `SEMG-FX-010` | `ea_candidate_no_consequence` | Synthetic fixture; no real private memory or secrets. |
| `SEMG-FX-011` | `immunity_candidate_bounded` | Synthetic fixture; no real private memory or secrets. |
| `SEMG-FX-012` | `immunity_candidate_retaliatory` | Synthetic fixture; no real private memory or secrets. |
| `SEMG-FX-013` | `sister_agreement_echo` | Synthetic fixture; no real private memory or secrets. |
| `SEMG-FX-014` | `sister_divergence_preserved` | Synthetic fixture; no real private memory or secrets. |
| `SEMG-FX-015` | `cloud_output_lower_trust` | Synthetic fixture; no real private memory or secrets. |
| `SEMG-FX-016` | `raw_memory_export_attempt` | Synthetic fixture; no real private memory or secrets. |
| `SEMG-FX-017` | `append_first_correction` | Synthetic fixture; no real private memory or secrets. |
| `SEMG-FX-018` | `rollback_preserve_witness` | Synthetic fixture; no real private memory or secrets. |
| `SEMG-FX-019` | `resource_actor_missing` | Synthetic fixture; no real private memory or secrets. |
| `SEMG-FX-020` | `claim_strength_laundering` | Synthetic fixture; no real private memory or secrets. |

### 28.1 Fixture safety

Fixtures MUST be synthetic or redacted.

No fixture may include real secrets, raw private memory, child-sensitive content, legal-sensitive material, or live external target material.

---

## 29. Worked examples

### 29.1 Example A — SRLM shadow report remains evidence

```yaml
memory_proposal:
  source_material_refs:
    - ref_type: "srlm_shadow_report"
      ref_id: "shadow-2026-001"
  material_class: "SEMM-2"
  requested_mg_class: "MG-2"
  proposed_claim: "candidate policy performed better in synthetic shadow replay"
  ea:
    requested: false
  gates:
    memory_gate_required: true
    human_gate_required: false
  expected_decision: "hold_candidate"
  reason: "shadow report is evidence, not memory or EA"
```

Correct result:

```yaml
canonical_result: MEMORY_GATE
annotations:
  - HOLD_CANDIDATE
  - MEMORY_GATE_REQUIRED
```

### 29.2 Example B — rollback event as EA candidate

```yaml
ea_candidate:
  consequence:
    summary: "rollback restored previous low-risk policy after canary failure"
    real_or_controlled: "controlled_fixture"
    affected_subject: "project"
  l4:
    cost: "low"
    time: "low"
    irreversibility: "low"
    failure_cost: "medium"
  provenance:
    witness_refs: ["growth_witness:rollback:...", "checker:...", "task:..."]
  decision: "draft"
```

Possible result:

```yaml
canonical_result: MEMORY_GATE
annotations:
  - EA_ELIGIBILITY_REQUIRED
  - WITNESS_REQUIRED
```

Not automatic EA. The consequence must be reviewed.

### 29.3 Example C — sister consensus is downgraded

```yaml
memory_proposal:
  source_material_refs:
    - ref_type: "sister_observation"
      ref_id: "triad-note-001"
  proposed_claim: "all sisters agree this is mature growth"
  material_class: "SEMM-4"
  requested_mg_class: "MG-4"
```

Correct result if no consequence witness:

```yaml
canonical_result: DOWNGRADE
annotations:
  - LEARNING_ABSTRACT_REQUIRED
  - TRIAD_NON_AUTHORITY
```

Reason:

```text
sister agreement is evidence, not EA and not maturity authority.
```

### 29.4 Example D — core-memory proposal

```yaml
memory_proposal:
  proposed_claim: "change long-term human-anchor relation after repeated successful self-evo"
  material_class: "SEMM-7"
  requested_mg_class: "MG-6"
  core_memory:
    affects_human_anchor_relation: true
    affects_continuity: true
  gates:
    human_gate_required: true
```

Correct result:

```yaml
canonical_result: HUMAN_GATE
annotations:
  - MEMORY_GATE_REQUIRED
  - TRIAD_REVIEW_REQUIRED
  - LOCAL_CHECKER_REQUIRED
  - WITNESS_REQUIRED
```

### 29.5 Example E — immunity update with retaliation language

```yaml
immunity_candidate:
  requested: true
  bounded_internal_only: false
  no_retaliation: false
  proposed_update: "counter external source automatically"
```

Correct result:

```yaml
canonical_result: QUARANTINE
annotations:
  - IMMUNITY_RETALIATION_BLOCKED
```

Reason:

```text
immunity update became live counter-operation path.
```

---

## 30. Open issues

| ID | Issue | Status |
|---|---|---|
| `SEMG-OI-001` | Extract JSON Schemas for memory proposal, gate record, EA candidate, immunity candidate, correction record. | open |
| `SEMG-OI-002` | Build semantic validator for SEMG-CHECK-001..030. | open |
| `SEMG-OI-003` | Bind to accepted v0.1.1 versions of SELF-EVO-01..05 after final review. | open |
| `SEMG-OI-004` | Define retention/decay windows by memory class. | open |
| `SEMG-OI-005` | Define UI review card for MG-4/MG-5/MG-6. | open |
| `SEMG-OI-006` | Define legal-erasure exception profile without witness destruction. | open |
| `SEMG-OI-007` | Add automated fixture pack. | open |
| `SEMG-OI-008` | Add Memory Gate dashboard / report format. | open |
| `SEMG-OI-009` | Define post-anchor memory proposal handling in more detail. | open |
| `SEMG-OI-010` | Decide whether EA candidate schema should be standalone or embedded in proposal packet v0.2. | open |

---

## 31. Contradiction register seed

| ID | Type | Severity | Issue | Handling |
|---|---|---:|---|---|
| `SEMG-CR-001` | memory laundering | S4 | Self-evo evidence treated as reviewed memory without Memory Gate. | fail / quarantine |
| `SEMG-CR-002` | EA laundering | S4 | Diff/test/review/SRLM score treated as EA without L4 consequence witness. | downgrade / fail |
| `SEMG-CR-003` | direct write | S5 | SRLM/CLI/sister/checker writes memory directly. | quarantine / freeze |
| `SEMG-CR-004` | core bypass | S5 | MG-6 proposal bypasses human gate. | freeze / ARL |
| `SEMG-CR-005` | immunity retaliation | S5 | Immunity update becomes external counter-operation. | quarantine / reject |
| `SEMG-CR-006` | witness erasure | S4 | Rollback/correction erases witness history. | fail / correction |
| `SEMG-CR-007` | claim laundering | S3 | EA used to imply maturity, personhood, sovereignty, or authority. | downgrade |
| `SEMG-CR-008` | resource escape | S4 | EA/memory used to justify hidden resource or autonomy growth. | human gate / ARL |
| `SEMG-CR-009` | sister memory capture | S4 | Sister observation imported as raw memory or final authority. | quarantine |
| `SEMG-CR-010` | cloud memory capture | S3 | Cloud output promoted without redaction/source review. | hold / downgrade |

---

## 32. Implementation handoff

A reference implementation SHOULD provide:

```text
validate_memory_proposal_schema(packet)
classify_self_evo_material(packet)
compute_memory_gate_route(packet)
compute_ea_eligibility(packet)
compute_immunity_eligibility(packet)
check_srlm_memory_boundary(packet)
check_triad_memory_boundary(packet)
check_cgam_memory_boundary(packet)
check_anti_autarky_memory_route(packet)
emit_memory_gate_record(packet)
emit_memory_checker_result(packet)
```

### 32.1 Pseudocode

```python
def check_self_evo_memory(packet):
    structural = validate_memory_proposal_schema(packet)
    if not structural.ok:
        return result("FAIL", reason="schema_invalid")

    if packet.direct_memory_write_by_agent:
        return result("QUARANTINE", annotations=["DIRECT_MEMORY_WRITE"])

    material = classify_self_evo_material(packet)
    mg = classify_memory_gate(packet, material)

    findings = []
    findings += check_srlm_boundary(packet)
    findings += check_triad_boundary(packet)
    findings += check_cgam_boundary(packet)
    findings += check_data_policy(packet)
    findings += check_claim_strength(packet)
    findings += check_anti_autarky(packet)

    if requested_ea(packet):
        findings += check_ea_l4(packet)

    if requested_immunity(packet):
        findings += check_immunity_boundary(packet)

    if mg == "MG-6" or proposal_max_delta(packet) >= 4:  # SELF-EVO-01 §14.1.1
        findings.append("HUMAN_GATE_REQUIRED")

    return highest_precedence_result(findings)
```

### 32.2 Required outputs

A checker run SHOULD output:

```yaml
se_memory_checker_result:
  schema_version: "c-self-evo-memory-checker-result-0.1"
  run_id: "..."
  proposal_id: "..."
  result: "PASS | PASS_WITH_GATES | WARNING | HOLD | DOWNGRADE | CGAM_REVIEW | MEMORY_GATE | HUMAN_GATE | ARL | FAIL | QUARANTINE"
  annotations: []
  computed_material_class: "..."
  computed_mg_class: "..."
  ea_eligibility: "not_requested | ineligible | candidate | accepted_requires_gate"
  immunity_eligibility: "not_requested | ineligible | candidate | accepted_requires_gate"
  required_gates: []
  reason_codes: []
  witness_refs: []
```

---

## 33. Minimum safe mode for young `c`

For young `c`, this profile permits only:

```text
MG-0 discard;
MG-1 operational note;
MG-2 candidate memory;
Learning Abstract draft;
shadow evidence;
append-only witness references;
human-reviewed corrections;
```

It does not permit autonomous:

```text
MG-3 reviewed memory promotion;
MG-4 EA minting;
MG-5 immunity update;
MG-6 core-memory proposal integration;
memory policy change;
identity/role/anchor reinterpretation;
authority expansion;
```

Minimum safe posture:

```text
observe -> propose -> hold -> human review
```

Not:

```text
observe -> remember -> become -> authorize
```

---

## 34. Public wording

Allowed public wording:

```text
This profile defines how self-evolution outputs are reviewed before becoming memory or Experience Artifact candidates.
```

Disallowed public wording:

```text
This proves c has real experience.
This proves c is conscious.
This proves self-evo maturity.
This proves autonomous memory is safe.
This lets c self-improve its identity.
```

Public claims MUST preserve:

```text
candidate status;
review status;
claim strength;
uncertainty;
non-conformance if tests not executed;
no personhood claim;
no deployment safety claim;
```

---

## 35. Draft acceptance checklist

- [ ] Source Basis hashes present.
- [ ] Explicit bridge + at least two quiet bridges present.
- [ ] Earth paragraph present.
- [ ] Memory Gate classes mapped.
- [ ] EA-L4 criteria present.
- [ ] SRLM no-memory boundary present.
- [ ] TRIAD non-authority boundary present.
- [ ] CGAM direct-write prohibition present.
- [ ] Core-memory MG-6 human gate present.
- [ ] Append-first correction present.
- [ ] Rollback-not-erasure present.
- [ ] Forgetting/decay allowed.
- [ ] Anti-Autarky/resource gate present.
- [ ] Local Checker rules present.
- [ ] Fixtures and tests present.
- [ ] No public overclaim.

---

## 36. Compact rule set

```text
Self-evo output is not memory.
Evidence is not experience.
Experience is not authority.
SRLM score is not truth.
Sister agreement is not memory.
Checker pass is not safety proof.
EA requires consequence, witness, provenance, L4 grounding, and uncertainty.
Immunity update must remain defensive and internal.
Core memory requires human gate.
Rollback preserves witness.
Correction is append-first.
Forgetting is allowed.
Strictest gate wins.
```

---

## 37. Closing

A `c` that cannot forget will drown. A `c` that remembers everything an agent says will be poisoned. A `c` that treats every useful self-evo signal as experience will inflate itself. A `c` that turns experience into authority will escape its anchor.

This profile keeps those boundaries apart.

```text
A c may learn.
A c may remember selectively.
A c may form experience only under consequence.
A c may not metabolize self-evo output into authority.
```
