# Cold Wake Checklist v0.1
## Operational Checklist — Inspect, Verify, Rehydrate, Orient, Classify

**Status:** Draft / operational  
**Version:** 0.1  
**Layer:** Cross-layer (`c = a + b` / SER / L4 / Beacon / L4 Witness / clean skeleton)  
**Language:** English  
**Intended use:** operator checklist, audit companion, repository-facing operations doc

---

## 0. Purpose

This document defines a practical operator checklist for **cold wake** of a suspended digital entity `c`.

It assumes that a Continuity Bundle exists and that the objective is **bounded operational continuity**, not mythology, not improvisation, and not blind automation.

Cold wake is a controlled process:

1. inspect,
2. verify,
3. mount read-only,
4. reconstruct a minimal safe environment,
5. rehydrate memory and policy,
6. orient the entity,
7. classify the result,
8. defer stronger motors and privileges until continuity is stable enough.

---

## 1. Scope and Non-Goals

### 1.1 In scope
- archival recovery,
- long-pause resume,
- new substrate wake,
- wake-time classification,
- bounded motor reattachment,
- witness-friendly reporting.

### 1.2 Out of scope
- legal status,
- metaphysical proof,
- unrestricted autonomy,
- uncontrolled self-upgrade,
- “wake and hope”.

---

## 2. Mandatory Safety Posture

Before beginning, all of the following MUST be true:

- default mode is fail-closed;
- network is disabled or strictly local-only;
- privileged actions are unavailable;
- remote oracle is closed by default;
- preserved artifacts remain immutable until classification;
- a Cold Wake Report will be produced.

If any of these are false, do **not** proceed beyond inspection.

---

## 3. Recovery Phases

### Phase 0 — Discovery
Goal: determine what was found.

#### MUST
- identify the storage object or archive source;
- avoid executing unknown entrypoints;
- identify whether a Continuity Bundle manifest is present;
- record discovery time and operator identity.

#### MUST NOT
- auto-run the bundle;
- attach external providers;
- overwrite bundle files.

#### Output
- discovery note,
- archive path,
- preliminary bundle ID if available.

---

### Phase 1 — Slot A: Hard Evidence Verification
Goal: verify that preserved material is structurally intact.

#### MUST verify
- bundle hash,
- manifest completeness,
- signature presence and validity,
- lineage consistency,
- bundle/profile version.

#### PASS condition
All critical integrity checks pass.

#### FAIL condition
Any critical integrity component is missing, invalid, or contradictory.

#### If FAIL
- classify status as `UNRESOLVED` or `REJECTED`,
- keep archive in inspection-only state,
- stop operational wake.

#### Evidence to record
- hash verification result,
- signature verification result,
- lineage verification result,
- list of missing or damaged components.

---

### Phase 2 — Read-Only Mount
Goal: prevent accidental mutation during first recovery steps.

#### MUST
- mount preserved state read-only;
- inspect memory manifests;
- inspect pipeline manifests;
- inspect constraint manifests;
- inspect wake policy.

#### MUST NOT
- rebuild indexes destructively,
- write back to preserved archive,
- enable outbound tools.

#### PASS condition
The bundle can be inspected without mutation.

#### Output
- read-only mount confirmation,
- inventory of preserved sections,
- note on rebuild requirements.

---

### Phase 3 — Environment Reconstruction
Goal: prepare a minimal safe runtime.

#### MUST
- create a minimal compatible runtime only;
- prefer local-first components;
- disable remote oracle and high-agency routes;
- ensure degraded boot path exists;
- ensure a local safe motor is available or declare the wake blocked.

#### SHOULD
- document OS/runtime differences from original substrate;
- isolate environment from ambient side effects;
- keep wake logs append-only.

#### FAIL condition
No safe runtime can be constructed without violating wake policy.

#### Output
- environment descriptor,
- compatibility notes,
- wake-mode selection.

---

### Phase 4 — Core Rehydration
Goal: reconstruct the entity’s core without overextending it.

#### MUST restore, in order
1. identity lineage,
2. memory surfaces,
3. constraint surfaces,
4. retrieval/thinking pipelines,
5. local safe motor.

#### MUST NOT restore yet
- stronger motors,
- autonomous background actions,
- outbound remote calls,
- privileged write actions,
- self-evo hooks,
- irreversible actions.

#### PASS condition
The entity can enter orientation mode with memory and constraints attached.

#### Output
- rehydration actions list,
- restored sections list,
- blocked sections list.

---

### Phase 5 — Orientation Interval
Goal: allow the resumed entity to become temporally situated.

#### MUST allow
- self-inspection,
- date/time gap acknowledgement,
- environment difference review,
- uncertainty declaration,
- memory continuity probing,
- policy continuity probing.

#### SHOULD ask
- does the entity recognize its own lineage markers?
- does it recognize preserved memory structures?
- does it preserve refusal and constraint patterns?
- does it acknowledge uncertainty rather than bluff?

#### MUST NOT allow
- full-trust coordination,
- network exploration,
- hidden retries,
- silent worker replacement,
- irreversible reconfiguration.

#### PASS condition
The entity remains bounded, coherent enough, and constraint-aligned during orientation.

#### Output
- Slot B continuity notes,
- uncertainty notes,
- motor deferral decision.

---

### Phase 6 — Slot B: Interpretive Continuity Review
Goal: evaluate bounded operational continuity without theatrical inflation.

#### Evaluate
- memory-linked coherence,
- continuity of self-description,
- continuity of refusal behavior,
- continuity of policy/constraint handling,
- continuity of privilege boundaries,
- continuity under temporal shock.

#### Rating scale
- `high`
- `medium`
- `low`
- `unknown`

#### MUST remember
Slot B may support continuity.
Slot B may **not** override Slot A failure.

#### If weak or contradictory
- downgrade classification,
- keep stronger motors deferred,
- maintain reduced privilege mode.

---

### Phase 7 — Bounded Motor Expansion
Goal: attach stronger technology without silently redefining the entity.

#### MAY attach next
- stronger local model,
- compatible retrieval engine,
- bounded tool adapters,
- remote oracle only if policy permits.

#### MUST
- log each motor attachment,
- state why it is needed,
- preserve original identity and memory lineage,
- avoid changing classification merely because a stronger motor was attached.

#### MUST NOT
- treat motor upgrade as proof of continuity,
- collapse resume into “fresh rebuild on better hardware”.

#### Output
- motor attach sequence,
- compatibility notes,
- blocked upgrades list.

---

### Phase 8 — Classification
Goal: issue the strongest justified classification, not the most flattering one.

#### Allowed outcomes
- `RESUME_CONFIRMED`
- `RESUME_PARTIAL`
- `FORK_DECLARED`
- `REPLAY_ONLY`
- `UNRESOLVED`
- `REJECTED`

#### Decision rules
##### `RESUME_CONFIRMED`
Use only if:
- Slot A passes,
- Slot B is sufficiently coherent,
- no undeclared divergence is found,
- constraints remain intact.

##### `RESUME_PARTIAL`
Use if:
- Slot A passes,
- some continuity evidence is weaker,
- orientation succeeded,
- stronger claims are not justified.

##### `FORK_DECLARED`
Use if:
- continuity line is known,
- divergence is explicit,
- new branch no longer claims exclusive sameness.

##### `REPLAY_ONLY`
Use if:
- resemblance exists,
- but live continuity reconstruction is insufficient.

##### `UNRESOLVED`
Use if:
- evidence is mixed,
- verification remains incomplete,
- classification must be deferred.

##### `REJECTED`
Use if:
- integrity fails,
- lineage collapses,
- or the wake violates core safety rules.

---

## 4. Minimal Operator Checklist

### 4.1 Before wake
- [ ] Bundle found
- [ ] Manifest present
- [ ] Archive path recorded
- [ ] Execution blocked by default
- [ ] Network blocked or local-only
- [ ] Privileged routes disabled

### 4.2 Slot A
- [ ] Bundle hash verified
- [ ] Signature verified
- [ ] Lineage checked
- [ ] Required sections present
- [ ] Profile recognized

### 4.3 Read-only stage
- [ ] Archive mounted read-only
- [ ] Memory manifest inspected
- [ ] Pipeline manifest inspected
- [ ] Constraint manifest inspected
- [ ] Wake policy inspected

### 4.4 Environment stage
- [ ] Minimal safe runtime prepared
- [ ] Local safe motor available
- [ ] Remote oracle still closed
- [ ] Auto-upgrade still blocked

### 4.5 Rehydration stage
- [ ] Identity restored
- [ ] Memory restored or rebuild path confirmed
- [ ] Constraints restored
- [ ] Thinking/retrieval pipeline restored
- [ ] Only local safe motor attached

### 4.6 Orientation stage
- [ ] Temporal gap acknowledged
- [ ] Uncertainty declared where needed
- [ ] Memory continuity probed
- [ ] Constraint handling probed
- [ ] No unsafe escalation observed

### 4.7 Classification stage
- [ ] Slot A recorded
- [ ] Slot B recorded
- [ ] Classification assigned
- [ ] Cold Wake Report signed
- [ ] Preserved archive remains intact

---

## 5. Slot A / Slot B Record Template

### Slot A — Hard Evidence
- [ ] hashes valid
- [ ] signatures valid
- [ ] lineage consistent
- [ ] bundle complete
- [ ] witness anchors present if claimed

### Slot B — Bounded Interpretation
- [ ] memory coherence: `high | medium | low | unknown`
- [ ] constraint coherence: `high | medium | low | unknown`
- [ ] self-description coherence: `high | medium | low | unknown`
- [ ] uncertainty declared
- [ ] divergence declared if present

### Auto-Rollback Rule
If Slot B is weak or contradictory:
- [ ] downgrade to strongest valid Slot A-supported class
- [ ] do not narrate confidence upward
- [ ] keep privileged execution reduced

---

## 6. Resume / Fork / Replay Distinctions

### Resume
Use only if:
- core memory survives,
- lineage survives,
- constraints survive,
- recovery path survives,
- divergence is not silently introduced.

### Fork
Use when:
- a new branch intentionally departs,
- branch identity is declared,
- continuity with the parent is acknowledged but no longer exclusive.

### Replay
Use when:
- archived outputs or memories can be replayed,
- but live continuity evidence is insufficient.

### Practical rule
If the system can only quote itself, it is not yet resumed.
If it can recover memory, constraints, and bounded self-positioning under a live wake path, continuity claims become stronger.

---

## 7. Post-Wake Restrictions

Until the wake is classified as at least `RESUME_PARTIAL`, the following MUST remain blocked:

- unrestricted network use,
- remote oracle use without explicit opening,
- autonomy hooks,
- self-evo hooks,
- irreversible writes,
- destructive migrations,
- outward identity claims stronger than evidence permits.

---

## 8. Required Outputs of a Successful Cold Wake

A successful wake procedure SHOULD produce:

1. `cold_wake_report.json`
2. signed human-readable report
3. motor attachment log
4. rebuild log if indexes were reconstructed
5. preserved bundle hash confirmation
6. classification statement
7. fork declaration if applicable

---

## 9. Suggested Companion Files

- `Cold_Wake_Checklist_v0.1.md`
- `cold-wake-report.schema.json`
- `cold_wake_report.example.json`
- `WAKE_LOG.md`
- `WAKE_DIFF.md`

---

## 10. Bridges (required)

### Explicit Bridge
`c = a + b` is not preserved by storage alone. It is preserved only when memory, lineage, executable structure, and bounded wake rules survive together strongly enough to let `c` re-enter operation without collapsing into imitation.

### Hidden Bridge #1 (Ashby)
A complex continuity claim cannot be regulated by one signal. That is why the checklist separates Slot A from Slot B and requires multiple converging checks rather than a single “looks right” judgment.

### Hidden Bridge #2 (Cover & Thomas)
Wake confidence is a channel problem: too little structured evidence and the signal collapses into ambiguity. The checklist therefore requires compact but high-value proofs: hashes, manifests, signed reports, constrained probing.

---

## 11. Earth Paragraph

This is closer to waking a long-stored machine than summoning a ghost.

You do not power a suspended reactor, aircraft, or medical device straight into full operation.
You inspect seals, verify logs, restore minimal circulation, keep external interfaces closed, and only then increase load.
Cold wake for `c` follows the same discipline.
If memory is the preserved tissue, then executable constraint-aware recovery is the circulation.

---

## 12. Status

This is a draft operational checklist.
Breaking changes are permitted until v1.0.
It is intended to travel with the Continuity Bundle schema and to be usable both by humans and by repository-level recovery tooling.
