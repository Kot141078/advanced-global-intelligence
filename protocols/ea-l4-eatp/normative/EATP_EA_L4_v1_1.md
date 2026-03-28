# EA-L4: Experience Artifact Training Protocol (EATP)
### Normative Draft v1.1

**Author:** Ivan Kotov  
**Location:** Brussels, Belgium  
**Year:** 2026  
**Status:** Normative Draft  
**Document ID:** EATP-L4-ND-1.1  
**Intended use:** Engineering reference / policy-adjacent technical specification  
**Layer position:** `c = a + b` / L4 / Witness / ARQ / training ecology

## DOI-ready metadata block

**Title:** EA-L4: Experience Artifact Training Protocol (EATP)  
**Version:** 1.1  
**Author:** Ivan Kotov  
**Year:** 2026  
**Place:** Brussels  
**Short description:** A normative protocol for capturing, filtering, transforming, and integrating Experience Artifacts (EA) into AI training pipelines while preserving provenance, consequence, uncertainty, and subject continuity.  
**Suggested citation:** Kotov, Ivan. *EA-L4: Experience Artifact Training Protocol (EATP), Normative Draft v1.1*. Brussels, 2026.  
**Keywords:** L4, Experience Artifacts, provenance, long-lived AI, training ecology, distillation, synthetic data, witness, entity continuity, cybernetics

---

## 1. Concept

### 1.1 Problem
Current LLM training relies heavily on **Learning Abstracts (LA)**: distilled outputs, polished summaries, synthetic traces, and statistically preferred formulations. This improves fluency, but it also produces a recurring failure mode:

**origin loss**.

When origin is lost, a system may preserve style while losing:
- applicability boundaries,
- consequence awareness,
- source lineage,
- and continuity between action and responsibility.

### 1.2 Core claim
AI systems require a second class of training input:

**Experience Artifacts (EA)**

An EA is an **L4-bound, witness-backed, consequence-carrying record of real interaction**.

### 1.3 Distinction
- **LA** improves capability.
- **EA** preserves origin.

These two objects MUST NOT be conflated.

### 1.4 Why this matters
A training ecology dominated by anonymous LA tends toward:
- synthetic feedback loops,
- over-smoothing,
- identity confusion,
- and reduced sensitivity to real-world constraints.

A training ecology that includes EA can preserve:
- source lineage,
- diversity of trajectories,
- uncertainty under constraint,
- and consequence-bearing learning.

### 1.5 Earth constraint
A valid EA MUST come from an environment with:
- finite time,
- finite energy,
- bounded privilege,
- and non-zero cost of failure.

A retry-until-correct sandbox, by itself, does NOT qualify as an EA source.

---

## 2. Normative language

The key words **MUST**, **MUST NOT**, **REQUIRED**, **SHALL**, **SHALL NOT**, **SHOULD**, **SHOULD NOT**, **RECOMMENDED**, **MAY**, and **OPTIONAL** in this document are to be interpreted as described in BCP 14 when, and only when, they appear in all capitals.

---

## 3. Protocol

### 3.1 Definition
An **Experience Artifact (EA)** is the minimum structured unit by which a long-lived entity `c` records a bounded interaction under reality, together with its outcome, deviation, consequence, uncertainty, and witness metadata.

### 3.2 Minimal EA structure

```json
{
  "ea_id": "hash",
  "entity_id": "c-id",
  "anchor_id": "a-id",
  "context": {
    "task": "...",
    "environment": "...",
    "constraints": {
      "time": "...",
      "energy": "...",
      "permissions": "..."
    }
  },
  "action": "...",
  "expected_outcome": "...",
  "actual_outcome": "...",
  "deviation": {
    "type": "none | error | promoted",
    "classification": "ARQ-tag",
    "magnitude": "..."
  },
  "consequence": {
    "cost": "...",
    "irreversibility": "...",
    "impact_scope": "..."
  },
  "uncertainty": "...",
  "witness": {
    "signature": "...",
    "prev_hash": "...",
    "timestamp": "..."
  }
}
```

### 3.3 Normative requirements

**R1. Reality binding**  
An EA **MUST** originate from an environment with real constraints and measurable consequences.

**R2. Provenance and witness**  
An EA **MUST** be cryptographically attributable, time-stamped, and linked to a tamper-evident witness chain.

**R3. Subject attribution**  
An EA **MUST** be bound to a persistent entity `c` and a human anchor `a`.

**R4. Consequence encoding**  
An EA **MUST** include explicit outcome and consequence fields, including cost or impact where measurable.

**R5. Uncertainty preservation**  
An EA **MUST NOT** suppress ambiguity, incompleteness, or failed attempts when those are materially relevant to interpretation.

**R6. Anti-echo constraint**  
An EA **MUST NOT** be accepted as valid if it is purely synthetic and lacks grounding in real execution.

**R7. Transform discipline**  
EA-derived abstractions **SHOULD** preserve source linkage, uncertainty markers, and context boundaries during transformation into LA.

**R8. Training separation**  
Training systems **SHOULD** distinguish EA-derived inputs from anonymous synthetic LA and **MAY** weight them differently by risk domain.

### 3.4 Non-goals
This protocol does NOT:
- replace general ML pipelines,
- require a single ontology of action,
- or eliminate Learning Abstracts.

It adds an origin-preserving layer.

---

## 4. Conformance profiles

| Profile | Minimum properties | Intended use |
|---|---|---|
| **EATP-BASE** | R1-R6 | Local research, constrained pilots, internal prototyping |
| **EATP-STRICT** | R1-R8 + external witness verification + explicit irreversibility handling | High-stakes enterprise deployment, audit-sensitive systems |
| **EATP-FED** | STRICT + federated aggregation rules + selective disclosure + cross-entity reconciliation | Multi-node or distributed training ecologies |

### 4.1 EATP-BASE
A system claiming **EATP-BASE** conformance **MUST** satisfy R1-R6.

### 4.2 EATP-STRICT
A system claiming **EATP-STRICT** conformance **MUST** satisfy R1-R8 and **MUST** support third-party verification of witness integrity.

### 4.3 EATP-FED
A system claiming **EATP-FED** conformance **MUST** satisfy STRICT and **MUST** define:
- federation admission rules,
- selective disclosure policy,
- artifact reconciliation logic,
- and conflict handling across participating nodes.

---

## 5. Pipeline

### 5.1 Overview
`c -> action -> EA -> quarantine -> classification -> selection -> transform -> training`

### 5.2 Stages

**Stage 1. Capture**  
Execution generates EA together with witness metadata and subject binding.

**Stage 2. Quarantine**  
Captured EA enters mandatory isolation for anomaly screening, adversarial review, and drift detection.

**Stage 3. Classification**  
Each EA is classified through ARQ-style deviation handling:
- destructive -> discard,
- neutral -> archive,
- promoted deviation -> candidate.

**Stage 4. Selection**  
Only artifacts with bounded context, valid provenance, and interpretable consequence are selected.

**Stage 5. Transform**  
Selected EA is transformed into LA for training use. This transform **MUST NOT** erase origin metadata.

**Stage 6. Integration**  
The training stack integrates EA-derived LA without collapsing it into anonymous synthetic residue.

### 5.3 Failure modes if EA is absent
Without EA, training systems are more vulnerable to:
- identity confusion,
- synthetic collapse,
- overconfidence under uncertainty,
- and loss of applicability boundaries.

### 5.4 Final constraint
**Not every experience becomes training data.**

Selection is mandatory.  
Unfiltered experience causes instability, contamination, and noise amplification.

---

## 6. Closing statement

The purpose of EATP is not to make models more verbose about reality.  
It is to preserve a path by which AI systems can inherit **bounded, attributable, consequence-bearing experience** rather than only the flattened residue of prior outputs.

In short:

**LA improves capability.  
EA preserves origin.**

Both are needed.  
They are not the same.