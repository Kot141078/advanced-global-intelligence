# **EA-L4: Experience Artifact Training Protocol (EATP)**

## **Version 1.2 (Normative Draft)**

**Author:** Ivan Kotov
**Year:** 2026, Brussels

---

## **DOI METADATA (READY BLOCK)**

* **Title:** EA-L4: Experience Artifact Training Protocol (EATP)
* **Version:** v1.2
* **Author:** Ivan Kotov
* **Affiliation:** Independent Researcher, Brussels
* **License:** MIT (or specify)
* **Keywords:** AI Training, Data Provenance, L4, Experience Artifacts, AI Safety, Distillation, Synthetic Data
* **Related Work:** SER v1.3, L4 Witness Protocol v0.2, ARQ

---

## **ABSTRACT**

This document defines the **Experience Artifact Training Protocol (EATP)**, a normative framework for integrating **reality-bound, consequence-carrying experience** into AI training pipelines.

The protocol introduces **Experience Artifacts (EA)** as a complement to traditional **Learning Abstracts (LA)**, addressing critical failure modes including:

* origin loss
* synthetic feedback loops
* overconfidence under uncertainty
* identity drift

EATP establishes requirements for **provenance, consequence encoding, and bounded experience**, enabling AI systems to retain alignment with real-world constraints.

---

## **1. TERMINOLOGY (BCP14)**

The key words **MUST**, **MUST NOT**, **SHOULD**, **SHOULD NOT**, and **MAY** are to be interpreted as described in BCP14.

---

## **2. PROBLEM STATEMENT**

Current AI training pipelines are dominated by:

* distilled outputs
* synthetic data
* statistically optimized text

This leads to:

* loss of origin
* collapse of diversity
* absence of consequence modeling

Result:

> Systems remain fluent but become detached from reality.

---

## **3. CORE DISTINCTION**

| Property    | Learning Abstracts (LA) | Experience Artifacts (EA) |
| ----------- | ----------------------- | ------------------------- |
| Source      | text / models           | real execution            |
| Origin      | implicit / lost         | explicit                  |
| Consequence | none                    | mandatory                 |
| Structure   | flattened               | contextual                |
| Time        | stateless               | state-bound               |
| Reliability | inferred                | witnessed                 |

---

## **4. PRINCIPLE**

```text
LA improves capability
EA preserves origin
```

Both are required. They MUST remain distinct.

---

## **5. EXPERIENCE ARTIFACT (EA) DEFINITION**

An **Experience Artifact (EA)** is a structured, witness-backed record of an executed interaction under real-world constraints.

### **5.1 Minimal Structure**

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

---

## **6. NORMATIVE REQUIREMENTS**

### **R1 — Reality Binding (L4)**

EA **MUST** originate from environments with:

* finite resources
* non-zero cost of failure
* irreversible outcomes

---

### **R2 — Provenance (Witness)**

EA **MUST**:

* be cryptographically signed
* include hash-chain linkage
* be externally verifiable

---

### **R3 — Subject Attribution (c = a + b)**

EA **MUST** be bound to:

* a persistent entity (`c`)
* a human anchor (`a`)

---

### **R4 — Consequence Encoding**

EA **MUST** include:

* measurable outcome
* explicit consequence
* irreversibility indicator

---

### **R5 — Uncertainty Preservation**

EA **MUST NOT** remove:

* ambiguity
* incomplete context
* failed attempts

---

### **R6 — Anti-Echo Constraint**

EA **MUST NOT** be:

* purely synthetic
* derived exclusively from model outputs

---

### **R7 — Bounded Privilege**

EA generation **MUST** occur under:

* auditable permissions
* constrained execution scope

---

## **7. PIPELINE**

### **7.1 Flow**

```text
c → action → EA → quarantine → classification → selection → transformation → training
```

---

### **7.2 Stages**

#### **Capture**

* Generate EA during execution
* Attach witness metadata

---

#### **Quarantine**

* Mandatory isolation
* Detect anomalies and adversarial patterns

---

#### **Classification (ARQ)**

* destructive → discard
* neutral → archive
* promoted → candidate

---

#### **Selection**

EA **MUST** satisfy:

* reproducibility
* bounded context
* validated consequence

---

#### **Transformation**

EA → LA abstraction **MUST**:

* preserve origin metadata
* retain uncertainty
* maintain context boundaries

---

#### **Training Integration**

Training systems **MUST**:

* separate EA-derived data from synthetic LA
* prevent recursive self-distillation
* weight EA higher in high-risk domains

---

## **8. CONFORMANCE PROFILES**

### **BASE**

* EA capture
* basic provenance
* optional quarantine

---

### **STRICT**

* full witness chain
* mandatory quarantine
* ARQ classification required
* audit-ready

---

### **FED (Federated)**

* distributed EA storage
* cross-entity validation
* selective disclosure
* privacy-preserving aggregation

---

## **9. FAILURE MODES (IF NOT IMPLEMENTED)**

Systems lacking EA integration exhibit:

* identity confusion
* synthetic feedback collapse
* overconfidence under uncertainty
* loss of applicability boundaries

---

## **10. DEPLOYMENT MODEL**

Minimal viable architecture:

* local entities (`c`) generate EA
* append-only storage (vector DB / logs)
* periodic aggregation
* controlled exposure to training

---

## **11. EARTH CONSTRAINT (MANDATORY)**

```text
Not every experience becomes training data.
```

Unfiltered ingestion **WILL** lead to:

* noise amplification
* adversarial contamination
* instability

---

## **12. POSITIONING**

EATP does **NOT**:

* replace LLM training
* eliminate LA
* impose a fixed ontology

EATP **DOES**:

* restore origin
* encode consequence
* enable continuity

---

## **13. FINAL STATEMENT**

AI systems trained only on text approximate language.

AI systems trained on EA:

> approximate interaction with reality under constraints.

---

## **14. CITATION**

Kotov, I. (2026).
**EA-L4: Experience Artifact Training Protocol (EATP)**
Version 1.2

---

## **15. AUTHOR NOTE**

“The future is not an event. It is a process.”

---

