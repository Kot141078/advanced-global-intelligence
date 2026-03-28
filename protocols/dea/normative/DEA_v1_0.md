# Document → Experience Artifact (DEA)
## Normative Draft v1.0 (Generalized)

**Author:** Ivan Kotov  
**Year:** 2026  
**Location:** Brussels  

---

## Status

This document defines a normative framework for transforming arbitrary inputs into **Domain Experience Artifacts (DEA)** within long-lived AI systems.

---

## Conformance Language

The key words **"MUST"**, **"MUST NOT"**, **"REQUIRED"**, **"SHALL"**, **"SHALL NOT"**, **"SHOULD"**, **"SHOULD NOT"**, **"RECOMMENDED"**, **"MAY"**, and **"OPTIONAL"** in this document are to be interpreted as described in **BCP 14** (RFC 2119, RFC 8174).

---

## 1. Scope

This specification applies to **any informational input** capable of influencing a long-lived system.

Applicable input types include, but are not limited to:

- Documents (PDF, Markdown, HTML, etc.)
- Messages (dialogue, instructions)
- Source code and configuration files
- Sensor data and telemetry
- Logs and execution traces
- API responses
- Human interaction events
- Internal system reflections

---

## 2. Core Principle

```text
Input is not defined by format.
Input is defined by its ability to alter continuity.
````

---

## 3. Definitions

### 3.1 I0 — Raw Input

Data that has been received but not yet interpreted or integrated.

---

### 3.2 I1 — Interpreted Input

Data that has been:

* parsed
* structured
* summarized
* classified

This stage does NOT constitute experience.

---

### 3.3 I2 — Integrated Input Candidate

Input that has:

* modified interpretation, or
* altered internal state, or
* introduced constraints

---

### 3.4 I3 — Domain Experience Artifact (DEA)

An input-derived artifact that:

* persists across time
* influences future cognition or action
* is linked to consequences
* is attributable via a witness mechanism

---

## 4. Normative Requirement

An input **MUST NOT** be treated as a Domain Experience Artifact (DEA) solely because it has been:

* received
* parsed
* stored
* embedded
* indexed
* retrieved

An input **MAY** be classified as a DEA only if it satisfies:

* integration
* temporal persistence
* consequence linkage

---

## 5. Integration Criteria

An input **MUST** satisfy at least one of the following to be considered a DEA candidate:

### 5.1 Interpretive Shift

The input changes how future inputs are interpreted.

---

### 5.2 State Re-weighting

The input changes the relative importance or priority of existing memory.

---

### 5.3 Constraint Injection

The input introduces new operational constraints or rules.

---

### 5.4 Behavioral Change

The input alters decision-making, routing, or execution behavior.

---

### 5.5 Consequence Binding

The input is later linked to:

* success
* failure
* refusal
* escalation
* correction

Without consequence binding, experience is not established.

---

## 6. DEA Structure (Minimal)

```json
{
  "dea_id": "hash",
  "input_type": "document | message | sensor | code | log | internal",
  "source_hash": "sha256",

  "entity_id": "c-id",
  "anchor_id": "a-id",

  "ingestion": {
    "timestamp": "...",
    "channel": "...",
    "parser": "..."
  },

  "integration_effect": {
    "type": "interpretive_shift | reweighting | constraint | behavior | consequence",
    "description": "...",
    "affected_state": [],
    "affected_processes": []
  },

  "temporal_persistence": {
    "observed_across_cycles": true,
    "decay": "none | bounded | high"
  },

  "evidence": {
    "downstream_effects": [],
    "decision_links": [],
    "traceable": true
  },

  "witness": {
    "signature": "...",
    "prev_hash": "...",
    "timestamp": "..."
  }
}
```

---

## 7. Processing Pipeline

### 7.1 Stage 1 — Ingestion

The system receives input via any supported channel.

---

### 7.2 Stage 2 — Interpretation

The system performs:

* parsing
* summarization
* classification

This stage does NOT establish experience.

---

### 7.3 Stage 3 — Binding

The input is linked to:

* existing memory
* entity identity (`c`)
* active constraints

At this stage, the input MAY become a DEA candidate.

---

### 7.4 Stage 4 — Temporal Persistence

The input influences:

* retrieval
* synthesis
* planning
* constraint enforcement

across multiple cycles.

---

### 7.5 Stage 5 — Consequence Verification

The system demonstrates that:

* decisions changed
* errors were avoided or escalated
* constraints were enforced

Only at this stage does a DEA fully exist.

---

## 8. Non-Qualifying Conditions

The following **DO NOT** qualify as DEA formation:

* vectorization without behavioral impact
* embedding storage alone
* one-time summarization
* transient dialogue usage
* retrieval without state change
* caching mechanisms

These are data operations, not experience formation.

---

## 9. Earth Constraint

```text
If nothing changes after input, nothing was learned.
```

---

## 10. Practical Test

A system operator SHOULD ask:

> Did this input change anything after processing?

If the answer is limited to:

* storage
* indexing
* retrieval

then no DEA exists.

If the answer includes:

* altered decisions
* modified priorities
* enforced constraints
* changed interpretation

then DEA formation has occurred.

---

## 11. Relation to ARQ

DEA is REQUIRED for meaningful error evaluation.

Without DEA:

* errors are corrected but not understood

With DEA:

* errors contribute to adaptive learning
* deviation can be promoted under bounded conditions

---

## 12. Relation to c = a + b

```text
Experience requires a subject.
```

DEA formation **REQUIRES**:

* persistent entity (`c`)
* continuity across time
* accountable anchor (`a`)

Without these, inputs remain stateless transformations.

---

## 13. Final Statement

A system does not gain experience when it receives input.

A system gains experience when its future behavior remains altered because of that input.

---


