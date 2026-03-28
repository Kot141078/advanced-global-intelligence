---
title: "Document to Experience Artifact (DEA)"
subtitle: "Conformance Profiles and L4 Witness Integration - Normative Addendum v1.1"
author: "Kotov Ivan"
date: "Bruxelles, 2026"
lang: en-US
---

## Status

This document extends **DEA Normative Draft v1.0** with:

- Conformance Profiles
- L4 Witness integration requirements
- Auditable experience criteria

---

## Conformance Language

The key words **"MUST"**, **"MUST NOT"**, **"REQUIRED"**, **"SHALL"**, **"SHALL NOT"**, **"SHOULD"**, **"SHOULD NOT"**, **"RECOMMENDED"**, **"MAY"**, and **"OPTIONAL"** are to be interpreted as described in **BCP 14** (RFC 2119, RFC 8174).

---

## 1. Conformance Profiles Overview

DEA implementations SHALL declare one of the following profiles:

- **DEA-BASE**
- **DEA-STRICT**
- **DEA-FED**

Profiles define the minimum guarantees for:

- integration
- persistence
- traceability
- auditability

---

## 2. DEA-BASE Profile

### 2.1 Description

Minimal viable DEA implementation.

Focus:

- internal integration
- observable behavioral impact

---

### 2.2 Requirements

A DEA-BASE system:

- MUST implement integration criteria (Section 5, v1.0)
- MUST demonstrate behavioral change OR interpretive shift
- MUST persist DEA across at least one subsequent cycle

---

### 2.3 Limitations

A DEA-BASE system:

- MAY NOT provide external verifiability
- MAY NOT provide cryptographic guarantees
- MAY rely on internal logging only

---

### 2.4 Use Cases

- local agents
- offline systems
- experimental architectures

---

## 3. DEA-STRICT Profile

### 3.1 Description

Auditable internal system with strong traceability.

Focus:

- deterministic traceability
- reproducibility
- internal audit readiness

---

### 3.2 Requirements

A DEA-STRICT system:

- MUST satisfy all DEA-BASE requirements
- MUST record integration effects in append-only logs
- MUST maintain deterministic linkage between:
  - input
  - integration effect
  - downstream behavior
- MUST provide:
  - reproducible decision trace
  - explicit mapping: input -> state change -> decision

---

### 3.3 Integrity Requirements

- Logs MUST be tamper-evident
- DEA identifiers MUST be hash-based
- State transitions SHOULD be versioned

---

### 3.4 Limitations

A DEA-STRICT system:

- MAY still depend on trusted environment
- MAY not support third-party independent verification

---

### 3.5 Use Cases

- enterprise AI systems
- regulated internal environments
- compliance preparation

---

## 4. DEA-FED Profile

### 4.1 Description

Federated, independently verifiable DEA system.

Focus:

- external auditability
- cross-system trust
- regulator-grade evidence

---

### 4.2 Requirements

A DEA-FED system:

- MUST satisfy all DEA-STRICT requirements
- MUST integrate with **L4 Witness Protocol**
- MUST produce **cryptographically verifiable evidence** of:
  - input origin
  - integration event
  - downstream effect

---

### 4.3 Witness Requirements

Each DEA MUST include:

- signed witness record
- hash-chain linkage (`prev_hash`)
- timestamped event sequence

---

### 4.4 Verification Requirements

A DEA-FED system MUST allow:

- independent reconstruction of:
  - input
  - transformation
  - effect
- verification WITHOUT:
  - privileged system access
  - trust in operator

---

### 4.5 Federated Context

DEA-FED systems:

- MUST support cross-entity traceability
- SHOULD support selective disclosure
- MAY operate across distributed nodes

---

### 4.6 Use Cases

- EU AI Act compliance
- cross-organization AI systems
- sovereign AI entities
- regulated infrastructure

---

## 5. DEA to L4 Witness Integration

### 5.1 Core Principle

```text
Experience is not real unless it is witnessable.
```

---

### 5.2 Mapping

| DEA Component       | L4 Witness Equivalent   |
|---------------------|-------------------------|
| input               | event input             |
| integration effect  | execution record (ER)   |
| persistence         | envelope continuity     |
| consequence linkage | decision trace          |
| DEA identity        | hash-linked event chain |

---

### 5.3 Mandatory Binding

For DEA-FED:

- Every DEA MUST produce a corresponding:
  - **Witness Record (WR)**
  - **Execution Evidence (EE)**

---

### 5.4 Witness Envelope

Each DEA event MUST be wrapped in:

```json
{
  "wr_id": "hash",
  "dea_id": "hash",

  "input_hash": "sha256",
  "integration_hash": "sha256",
  "effect_hash": "sha256",

  "prev_hash": "hash",
  "timestamp": "...",

  "signature": "ed25519"
}
```

---

## 6. Auditable Experience Criteria

A DEA is considered **auditable** ONLY if:

### A1 - Input Provenance

Input origin can be verified.

---

### A2 - Integration Evidence

The transformation from input to state change is recorded.

---

### A3 - Behavioral Link

The system demonstrates that:

- behavior changed
- decisions were affected

---

### A4 - Chain Continuity

The DEA is part of a tamper-evident sequence.

---

### A5 - Independent Verification

A third party can validate:

- the existence
- the integrity
- the effect

without privileged access.

---

## 7. Failure Modes

Systems FAIL DEA compliance if:

- inputs are processed but not persisted
- integration is not recorded
- behavior cannot be linked to input
- logs can be altered without detection
- continuity is broken

---

## 8. Earth Constraint

```text
If experience cannot be audited, it cannot be trusted.
```

---

## 9. Relation to L4 (Reality Boundary Layer)

DEA-FED systems MUST operate under:

- bounded compute
- bounded time
- bounded memory
- bounded authority

This ensures:

- no infinite retries
- no silent drift
- no unverifiable adaptation

---

## 10. Final Statement

DEA defines when input becomes experience.

L4 Witness defines when experience becomes evidence.

Together, they establish:

```text
Input -> Experience -> Evidence
```
