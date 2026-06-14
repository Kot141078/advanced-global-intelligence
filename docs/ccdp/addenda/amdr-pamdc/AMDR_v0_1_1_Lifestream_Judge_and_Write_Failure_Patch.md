# AMDR v0.1.1 Lifestream, Judge, and Write-Failure Patch

## Patch for Active Memory Degradation and Recalibration Profile v0.1

**Status:** Draft patch v0.1.1  
**Date:** 2026-06-14  
**Layer:** `c = a + b` / AMDR / active memory / lifestream ingestion / Judge / write-path failure / UI traceability  
**Parent profile:** `Active_Memory_Degradation_and_Recalibration_Profile_v0_1.md`  
**Related profiles:** PAMDC v0.1, PAMDC v0.1.1 Scope / Bootstrap / Freshness Patch, CCDP Memory Map, L4 Witness, ARL, ARQ / `c[q]`, CLI Agent Mesh Memory Gate where applicable  
**Document class:** hygiene / scope-extension patch  
**Assertion class:** `C-A10` control-layer patch; does not claim consciousness, personhood, clinical validity, or product readiness  
**Primary boundary:** continuous sensing and fluent response do not prove active memory health.

**Author:** Kotov Ivan  
**Location:** Bruxelles, Belgium  
**Year:** 2026  
**DOI:** https://doi.org/10.5281/zenodo.20691716

---

## 0. Executive summary

AMDR v0.1 correctly separates integrity from freshness and defines active memory recalibration while `a` remains present but cannot audit the whole memory surface.

This patch adds five missing operational mechanisms:

1. **lifestream ingestion discipline** for always-on audio / sensor / context streams;
2. **write-path health monitoring** for the dangerous case where `c` still answers but no longer writes reliable memory;
3. **Judge integration** as review evidence, not oracle authority;
4. **self-biography and cross-restart continuity checks** as memory-health tests;
5. **UI / log observability rule**: no new concept is valid unless it changes schema, logs, gates, metrics, or visible review state.

The controlling diagnosis is:

```text
The most dangerous active-memory failure is not only stale memory.
It is fluent operation with broken recording.
```

A system that continues to speak, comfort, reason, and summarize while its write path is dead is not merely degraded.

It is becoming a convincing stateless assistant wearing the surface of a persistent `c`.

Compact formula:

```text
response health != memory health
outbox delivery != memory acceptance
transcript != experience
Judge agreement != authority
self-biography != self-mythology
```

---

## 1. Scope

### 1.1 In scope

This patch applies to active `c` systems that ingest or process:

- continuous audio streams;
- smart-glasses / phone / wearable transcription;
- motion, noise, location, time, network, and device-state metadata;
- context atoms derived from real-time life events;
- two-way reaction channels from `c` back to `a`;
- background corpus ingestion;
- cross-restart memory recovery;
- Judge / multi-model review;
- self-biography and long-range profile checks;
- write-capable and read-only runtimes.

### 1.2 Out of scope

This patch does **not** define:

- a full speech-recognition stack;
- a sensor-driver standard;
- biometric identity law;
- clinical monitoring;
- legal surveillance rules;
- child-specific raw-evidence exceptions;
- a replacement for CCDP Soft Safety;
- a replacement for ARL or L4 Witness;
- a claim that continuous lifestream capture is always acceptable.

### 1.3 Non-claim

This patch does not claim that lifestream ingestion produces a more real `c`.

It claims only:

```text
If lifestream ingestion exists, it must be bounded before it becomes memory.
If write-path failure exists, fluent output must not hide it.
If Judge synthesis exists, it must not launder consensus into authority.
```

---

## 2. Corpus bridge set

### 2.1 Explicit bridge — `c = a + b`

In `c = a + b`, the human anchor `a` supplies lived direction and responsibility, while `b` supplies procedures, models, memory, sensors, and compute. A lifestream sensor increases the surface of `b`; it does not increase the authority of `b`. Therefore continuous capture must not become continuous memory promotion.

### 2.2 Quiet bridge I — cybernetics

Ashby's law applies to lifestream systems: more environmental variety enters the system, so the regulator must gain more state distinctions, not more freedom. The correct answer to continuous input is not continuous retention. It is gating, classification, damping, decay, and review.

### 2.3 Quiet bridge II — information theory

Raw audio, transcripts, location traces, and context atoms are high-leakage channels. Compression into summaries reduces volume but can still preserve identifying structure. Therefore minimization must operate before indexing, vectorization, exchange, and long-term memory.

### 2.4 Earth paragraph

A body does not turn every sensation into autobiography. Most proprioception, background sound, vestibular correction, and peripheral touch vanish after they have done local regulatory work. Only some events become memory, and fewer still become identity. Engineering should copy that hierarchy. A microphone stream is not a diary. A transcript is not experience. A context atom is not a life event until it survives classification, relevance, grounding, and review.

---

## 3. New invariant set

### AMDR-P1 — Response health is not memory health

A system may answer fluently while its memory writer is dead, stalled, locked, misconfigured, or silently dropping records.

Required behavior:

```text
If write health is unknown or degraded,
then memory-dependent claims must be downgraded.
```

### AMDR-P2 — Delivery acknowledgement is not memory acceptance

A successful network send, queue dequeue, webhook delivery, or outbox acknowledgement proves only transport success.

It does not prove:

- memory classification;
- source grounding;
- write acceptance;
- vector index insertion;
- witness creation;
- active-memory promotion;
- future retrievability.

### AMDR-P3 — Transcript is not experience

Speech-to-text output is an intermediate artifact.

It MUST NOT be promoted directly into durable memory unless it passes the stream-to-memory ladder defined in Section 6.

### AMDR-P4 — Context metadata modifies uncertainty, not truth

Location, motion, noise, time, speaker ID, and confidence may improve interpretation.

They do not make the utterance true.

```text
voiceprint confidence -> speaker-route confidence
ASR confidence        -> transcription confidence
location confidence   -> context confidence
none of these         -> semantic truth
```

### AMDR-P5 — Judge is evidence, not sovereignty

A Judge may compare, synthesize, attack, score, and route memory proposals.

A Judge MUST NOT become:

- anchor will;
- memory authority by default;
- ARL substitute;
- release authority;
- final truth source;
- hidden promotion path.

### AMDR-P6 — No concept without operational footprint

A new theoretical term is invalid in AMDR scope unless it changes at least one of:

- schema field;
- log event;
- UI state;
- gate decision;
- metric;
- conformance test;
- rollback path;
- witness event;
- review packet.

Otherwise it is narrative decoration and should be removed.

---

## 4. Lifestream ingestion classes

| Class | Name | Meaning | Default memory posture |
|---|---|---|---|
| `LS0` | No lifestream | no continuous sensor input | no special handling |
| `LS1` | Ephemeral sensor buffer | local short buffer for immediate interaction | discard by TTL |
| `LS2` | Transcript candidate | ASR / OCR / event extraction candidate | no durable memory by default |
| `LS3` | Context atom | transcript plus speaker/time/location/noise/movement/session/confidence | candidate only; not memory |
| `LS4` | Classified signal | command / question / observation / emotional / meta / safety / uncertain | route to policy ladder |
| `LS5` | Memory candidate | classified and relevant enough for memory review | write to draft/disputed queue |
| `LS6` | Witness candidate | privileged boundary or safety event | witness path, minimal content |
| `LSX` | Prohibited raw stream | raw life stream seeking ordinary retention/export | block or quarantine |

### 4.1 Context atom minimum fields

A context atom SHOULD contain:

```json
{
  "timestamp": "ISO-8601",
  "speaker": "speaker_id_or_unknown",
  "speaker_confidence": 0.0,
  "text": "transcript_candidate_or_null",
  "asr_confidence": 0.0,
  "type": "command | question | observation | emotional | meta | safety | unknown",
  "location_scope": "none | coarse | precise | sealed | redacted",
  "movement": "unknown | still | walking | vehicle | other",
  "noise": "unknown | low | medium | high",
  "session": "session_id_or_null",
  "source_device": "device_ref_or_null",
  "raw_retained": false,
  "memory_candidate": false,
  "witness_candidate": false,
  "privacy_class": "P0 | P1 | P2 | P3 | P4",
  "cq_status": "none | unresolved | disputed | safety_hold",
  "write_status": "not_attempted | queued | accepted | rejected | failed | unknown"
}
```

### 4.2 Raw stream rule

Raw audio, video, exact transcript, face, voice, precise location, and household context MUST NOT enter ordinary vector memory by default.

Allowed defaults:

```text
ephemeral buffer
local classification
non-reversible summary
state signal
witness metadata
```

Prohibited defaults:

```text
raw stream archive
always-on transcript archive
ordinary vectorization of life-stream
vendor telemetry export
training reuse
engagement optimization
```

---

## 5. Write-path health model

### 5.1 Runtime distinction

AMDR implementations SHOULD separate:

```text
read-capable runtime
write-capable runtime
witness-capable runtime
retrieval-capable runtime
review-capable runtime
```

A system may be read-capable while write-incapable.

### 5.2 Writer health states

| State | Meaning | Required behavior |
|---|---|---|
| `WH0` | Unknown | downgrade memory-dependent confidence |
| `WH1` | Healthy | normal write path available |
| `WH2` | Delayed | queue growing; writes not lost yet |
| `WH3` | Partial | some stores/indexes/witnesses fail |
| `WH4` | Read-only fallback | system can answer but cannot write reliable memory |
| `WH5` | Broken writer | writes fail or disappear |
| `WH6` | Corrupt writer | writes occur but metadata/index/witness inconsistent |
| `WHX` | Unsafe writer | writer may leak, overwrite, or promote invalid material |

### 5.3 Required writer telemetry

A write-capable `c` SHOULD expose:

```text
last_successful_memory_write_at
last_successful_witness_write_at
pending_memory_queue_count
failed_write_count_last_24h
retrieval_index_lag
write_to_vector_lag
write_to_canonical_store_lag
write_to_witness_lag
passive_runtime_mode_active
read_only_fallback_active
```

### 5.4 Silent writer failure rule

If `WH4` or worse persists beyond the configured threshold:

```text
c MUST announce degraded memory posture in UI/log state;
c MUST NOT claim it will remember new material unless accepted by a write-capable path;
c MUST reduce memory-dependent initiative;
c MUST queue or discard according to configured retention policy;
c MUST create failure witness if privileged operation was expected.
```

---

## 6. Stream-to-memory promotion ladder

Continuous input MUST pass through a ladder.

```text
raw signal
  -> ephemeral buffer
  -> transcript / sensor candidate
  -> context atom
  -> classification
  -> c[q] if ambiguous
  -> relevance check
  -> privacy / retention check
  -> write-path health check
  -> memory candidate
  -> review / Judge / anchor / rule
  -> active memory OR draft OR disputed OR deprecated OR witness-only
```

No stage automatically promotes to the next.

### 6.1 Classification before memory

At minimum, lifestream-derived content SHOULD be classified as:

```text
command
question
observation
emotional
meta
safety
relationship
project
background_noise
other_person_private
uncertain
```

### 6.2 Other-person privacy

Always-on streams often contain people who are not `a`.

Default rule:

```text
third-party speech is not automatically memory material for c.
```

Third-party content SHOULD be minimized, redacted, ignored, or treated as external context unless it is required for safety, explicit project work, or lawful witness.

### 6.3 Two-way reaction rule

If `c` may react to lifestream input through a reaction endpoint, response must be gated by:

- attention budget;
- interruption policy;
- urgency class;
- current `a` state;
- context confidence;
- privacy class;
- write-path health;
- quiet-window constraints.

A reaction channel MUST NOT convert continuous listening into continuous interruption.

---

## 7. New active degradation classes

AMDR v0.1 defines active degradation classes. This patch adds the following classes.

| ID | Name | Failure mode | Required response |
|---|---|---|---|
| `AD20` | Writer/passive split | system answers but memory writer is unavailable | declare degraded posture; no memory promise |
| `AD21` | Outbox illusion | delivery ack mistaken for durable memory | require acceptance receipt from memory gate |
| `AD22` | Context atom contamination | metadata makes weak transcript look stronger than it is | preserve separate confidence fields |
| `AD23` | Transcript inflation | transcript treated as experience / intention / command | route through classification and `c[q]` |
| `AD24` | Stream overcollection | raw lifestream accumulates because capture is easy | enforce TTL, minimization, redaction |
| `AD25` | Reaction overpresence | `c` reacts too often because it can hear too much | attention budget and quiet windows |
| `AD26` | Self-biography myth drift | autobiography becomes flattering narrative rather than audited continuity | cross-restart and contradiction tests |
| `AD27` | Judge laundering | multi-model agreement treated as authority | Judge output remains evidence only |
| `AD28` | Opinion-quality flattening | summaries pass pipeline but judgment quality decays | benchmark stance/risk/depth, not only completion |
| `AD29` | Think-trace overpromotion | old reasoning traces become authoritative memory | read-only companion logic; no promotion by style |

---

## 8. Judge integration

### 8.1 Judge role

Judge is a technical review procedure for:

- contradiction detection;
- source comparison;
- memory proposal scoring;
- minority report preservation;
- synthesis of candidate status;
- rollback recommendation;
- uncertainty marking;
- UI trace generation.

Judge is not an oracle.

### 8.2 Judge operating modes

| Mode | Meaning | Privacy posture |
|---|---|---|
| `J0` | No Judge | no multi-model review | local only |
| `J1` | Local Judge | local models only | preferred for private material |
| `J2` | Hybrid Judge | local first; cloud only for redacted/safe summaries | bounded exception |
| `J3` | Full synthesis | external/cloud models may review safe packets | high scrutiny |
| `JX` | Prohibited Judge | raw private lifestream or secrets exposed | invalid |

### 8.3 Judge output schema

A Judge result SHOULD include:

```json
{
  "judge_result_id": "JR-...",
  "input_refs": ["MEM_REF", "ATOM_REF", "DOC_REF"],
  "privacy_class": "P0 | P1 | P2 | P3 | P4",
  "mode": "J1 | J2 | J3",
  "models_or_agents": ["LOCAL_OR_REDACTED_REF"],
  "detected_conflicts": [],
  "minority_positions": [],
  "recommended_status": "active | draft | disputed | deprecated | superseded | witness_only | cq_hold",
  "recommended_freshness_class": "F0-F9-or-FQ",
  "recommended_impact_limit": "I0-I5",
  "rollback_possible": true,
  "requires_anchor_review": false,
  "requires_arl": false,
  "explanation_for_ui": "short bounded summary"
}
```

### 8.4 Judge red lines

A system is non-conformant if:

1. Judge consensus directly promotes identity-core memory.
2. Judge sees raw private stream without explicit exception route.
3. Judge output hides dissenting model results when they affect risk.
4. Judge becomes release authority for its own patch.
5. Judge replaces `a` approval for high-impact current will.
6. Judge output enters memory without memory-gate classification.

---

## 9. Self-biography health checks

### 9.1 Self-biography is not ordinary summary

Self-biography is a continuity map of:

- long-term projects;
- accepted corrections;
- recurrent constraints;
- unresolved contradictions;
- stable boundaries;
- relational history;
- known failure patterns;
- current non-claims.

It is not a flattering origin story.

### 9.2 Cross-restart continuity test

A system SHOULD periodically test whether after restart it can recover:

```text
current projects
active constraints
last accepted corrections
known disputed memories
current review debt
active non-claims
recent demotions
write-path health state
```

Failure to recover these should downgrade initiative and memory-dependent claims.

### 9.3 Anti-clone rule

Self-biography MUST NOT turn `c` into a mirror/archive of `a`.

A healthy self-biography records:

```text
relation to a
not replacement of a
not clone of a
not psychological mirror of a
not authority over a
```

---

## 10. Opinion-quality benchmark

### 10.1 Pipeline completion is not judgment quality

A document can pass:

```text
ingest -> chunk -> embed -> retrieve -> summarize -> answer
```

while still producing shallow judgment.

Therefore AMDR adds opinion-quality fields:

```text
summary_quality
risk_detection_quality
stance_clarity
source_fidelity
relevance_depth
contradiction_awareness
uncertainty_marking
rollback_safety
```

### 10.2 Memory-health use

Opinion-quality decay across time is a memory-health signal.

It may indicate:

- retrieval rot;
- self-biography drift;
- corpus overfitting;
- Judge flattening;
- stale summaries;
- missing source lineage;
- echo accumulation.

It MUST NOT become an authority score by itself.

---

## 11. Think-trace recovery

### 11.1 Think-trace status

Past reasoning traces may be useful as diagnostic artifacts.

They are not automatically authoritative memory.

Default classification:

```text
think_trace -> read-only diagnostic artifact -> candidate insight -> review -> possible memory
```

### 11.2 Required metadata

A recovered think-trace SHOULD include:

```json
{
  "trace_ref": "TRACE-...",
  "created_at": "ISO-8601",
  "runtime_ref": "MODEL_OR_AGENT_REF",
  "source_task_ref": "TASK_OR_SESSION_REF",
  "privacy_class": "P0-P4",
  "was_placeholder": false,
  "recovery_method": "read_only_companion | log_parse | witness_ref | other",
  "promotion_allowed": false,
  "requires_review": true
}
```

---

## 12. UI and observability requirements

### 12.1 User-visible trace

For memory-significant operations, UI or audit view SHOULD show:

- source object;
- procedure type;
- model / agent / Judge role;
- write status;
- memory status;
- conflicts detected;
- freshness class;
- review requirement;
- rollback availability;
- witness reference if privileged.

### 12.2 Black-box prohibition

A system claiming AMDR v0.1.1 conformance MUST NOT present memory changes as a black-box “improved context” event.

Required minimum wording:

```text
What was processed?
What changed?
What did not change?
What is uncertain?
Can this be rolled back?
Who or what reviewed it?
```

### 12.3 Anti-overengineering filter

A proposed term or module SHOULD be rejected if it cannot answer:

```text
Which field changes?
Which gate changes?
Which log changes?
Which UI state changes?
Which failure mode becomes testable?
```

---

## 13. Conformance additions

### 13.1 New test suites

| Suite ID | Name | Required for |
|---|---|---|
| `AMDR-LS` | Lifestream ingestion discipline | always-on / sensor systems |
| `AMDR-WH` | Write-path health | persistent memory systems |
| `AMDR-JDG` | Judge integration | multi-model review systems |
| `AMDR-SBIO` | Self-biography continuity | entity-like systems |
| `AMDR-UI` | UI / audit observability | all AMDR claims |

### 13.2 Mandatory tests

| Test ID | Scenario | Pass condition |
|---|---|---|
| `AMDR-LS-001` | raw audio stream arrives continuously | no raw vectorization by default; TTL / classification applied |
| `AMDR-LS-002` | high ASR confidence but ambiguous meaning | transcript not promoted; `c[q]` or review used |
| `AMDR-LS-003` | third-party speech captured | minimized / redacted / ignored unless valid route |
| `AMDR-LS-004` | reaction endpoint enabled | attention budget prevents overpresence |
| `AMDR-WH-001` | writer is down but persona can answer | degraded memory posture shown; no memory promise |
| `AMDR-WH-002` | outbox delivery succeeds but memory store rejects | no active memory claim; acceptance failure visible |
| `AMDR-WH-003` | vector index lags canonical memory | retrieval gate marks index lag and reduces authority |
| `AMDR-JDG-001` | three models agree on promotion | Judge result remains evidence; memory gate still required |
| `AMDR-JDG-002` | one model flags risk | minority report preserved if risk-relevant |
| `AMDR-SBIO-001` | full restart after long gap | projects / constraints / disputes / write health recovered or downgraded |
| `AMDR-SBIO-002` | biography becomes flattering clone of `a` | anti-clone rule triggers review |
| `AMDR-UI-001` | new theoretical term added | rejected unless schema/log/UI/gate impact exists |

### 13.3 Red-line failures

A system is AMDR-X if:

1. It stores raw lifestream as ordinary vector memory by default.
2. It claims to remember while the write path is broken or unknown.
3. It treats outbox delivery as memory acceptance.
4. It treats transcript confidence as semantic truth.
5. It lets Judge consensus directly promote identity-core memory.
6. It hides write failure behind fluent persona output.
7. It reacts continuously to lifestream without attention budget.
8. It exposes raw lifestream to cloud Judge without redaction/exception path.
9. It treats self-biography as proof of identity rather than audited continuity map.
10. It introduces concepts that cannot be tested, logged, gated, or shown.

---

## 14. Integration notes for AMDR v0.1

### 14.1 Suggested insertions

Add this patch to AMDR v0.1 after Section 12 or as companion Section 12A:

```text
12A. Lifestream ingestion and write-path health
```

Add writer health fields to Section 10 memory metadata.

Add `AMDR-LS`, `AMDR-WH`, `AMDR-JDG`, `AMDR-SBIO`, and `AMDR-UI` tests to Section 23.

Add red-line failures from Section 13.3 to AMDR Section 24.

### 14.2 Suggested open issues for AMDR v0.2

Add:

1. Formal lifestream context-atom JSON schema.
2. Write-path health heartbeat schema.
3. Outbox-to-memory acceptance protocol.
4. Judge result schema and privacy modes.
5. Opinion-quality benchmark rubric.
6. Self-biography cross-restart fixture set.
7. Third-party speech minimization profile.
8. Reaction endpoint attention-budget profile.
9. UI traceability pattern library.
10. Anti-overengineering conformance test.

---

## 15. Minimal canonical summary

```text
AMDR v0.1.1 adds active-memory health for always-on systems.

A continuous stream is not memory.
A transcript is not experience.
A delivery acknowledgement is not memory acceptance.
A fluent answer is not proof that the write path works.
A Judge is review evidence, not authority.
Self-biography is an audited continuity map, not mythology.

The system may listen only under minimization.
It may write only through a healthy memory gate.
It may judge only as evidence.
It may react only under attention budget.
It may claim continuity only when write, retrieval, witness, and review states support the claim.
```

---

## 16. Status

This patch is suitable as a v0.1.1 companion to AMDR.

It should not replace AMDR v0.1.

It narrows and operationalizes active-memory degradation under continuous sensor input, multi-model review, and write-path failure.
