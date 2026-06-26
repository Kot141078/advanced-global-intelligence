# Self-Evo Proposal Packet Schema v0.1.1

## Machine-readable proposal envelope for governed self-evolution in `c = a + b` systems

**Status:** Draft schema/profile v0.1.1 — append-first advisory clarification revision  
**Date:** 2026-06-24  
**Document ID:** `03_Self_Evo_Proposal_Packet_Schema_v0_1_1`  
**Short name:** `SE-PACKET v0.1.1`  
**Package position:** file `03` in the Self-Evo governance package  
**Parent profiles:**  
- `01_C_Self_Evolution_Gate_CGAM_TRIAD_SRLM_Profile_v0_1_1.md` (`C-SEG v0.1.1`)  
- `02_SRLM_Bounded_Growth_Contour_Profile_v0_1_1.md` (`SRLM-BGC v0.1.1`)  
- `C-Governed_CLI_Agent_Mesh_Protocol_v0_1.md` and CGAM companion profiles  
- `TRIAD-SYNAPS v0.1`  
- `CLI_Agent_Memory_Gate_Profile_v0_1.md`  
- `L4 Anti-Autarky Test Profile v0.1`  
- `Claim Strength Taxonomy for c v0.1`

**Primary object:** `C_SELF_EVO_PROPOSAL_PACKET`  
**Canonical schema version:** `c-self-evo-proposal-packet-0.1`  
**Document class:** JSON Schema profile / semantic validation profile / proposal packet envelope  
**Assertion class:** `C-A10` control-layer artifact; `C-A7` where hash/ref-bound witness fields are used  
**Primary boundary:** a self-evolution proposal may become reviewable evidence. It must not become self-approval, memory, authority, identity change, permission expansion, or integration by itself.

**v0.1.1 correction note:** this append-first revision incorporates the advisory `SEPKT-REV-F1` and `SEPKT-REV-F2` review observations from `SEPKT_PROPOSAL_PACKET_REVIEW_RECORD_v0_1`: pack-numbering/navigability is clarified through namespace-qualified reading-order labels, and the direct-memory-write negative example now states its Stage-1 structural rejection path explicitly. No schema fields, required properties, enum values, or gate semantics are changed.

---

## 0. Executive definition

`C_SELF_EVO_PROPOSAL_PACKET` is the machine-readable envelope used to submit, review, validate, hold, shadow, canary-test, integrate, reject, rollback, freeze, or quarantine a proposed self-evolution change for a `c = a + b` system.

The packet exists because self-evolution is not a normal patch.

It may affect:

```text
behavior
memory policy
permission posture
sister relations
human-anchor relation
witness discipline
SRLM learning pressure
CGAM executable work
L4 cost / irreversibility / privacy / resources
public claims
continuity
```

Therefore the proposal must be a structured object before it becomes an action.

Compact formula:

```text
Proposal first.
Classification second.
Delta and gates third.
Execution never before witnessable scope.
Integration never before review.
```

Root rule:

```text
A c may propose growth.
A c may not self-certify growth.
A packet may request review.
A packet may not approve itself.
```

---

## 1. Purpose

This profile defines the proposal packet that binds the first two self-evo profiles into a checker-friendly artifact.

It answers:

1. What fields must every self-evo proposal contain?
2. Which fields are structural and checkable by JSON Schema?
3. Which fields require semantic validation beyond JSON Schema?
4. How are `SE`, `SRLM`, `R`, `MG`, `RB`, `SEM`, `C-A`, and `CSEG` axes composed?
5. How is `total_max_delta` computed?
6. When is a human gate required?
7. When does SRLM remain shadow-only?
8. When must CGAM task contracts, sandbox, and reviewer separation exist?
9. When is TRIAD-SYNAPS sister review required?
10. When does a packet route to hold, freeze, quarantine, rollback, or ARL?

This document is intentionally more mechanical than C-SEG and SRLM-BGC.

It is the transition from doctrine to validation.

---

## 2. Non-goals

This schema does not:

1. approve any proposal;
2. integrate any change;
3. write memory;
4. grant permissions;
5. authorize CLI execution;
6. replace Memory Gate;
7. replace TRIAD-SYNAPS review;
8. replace L4W / VolitionGate;
9. replace human anchor review;
10. certify conformance;
11. certify deployment safety;
12. define legal personhood, consciousness, or AGI claims;
13. make SRLM a training system or authority system;
14. make JSON Schema sufficient for safety.

A structurally valid packet may still be semantically unsafe.

---

## 3. Normative keywords

The terms **MUST**, **MUST NOT**, **SHOULD**, **SHOULD NOT**, **MAY**, **REQUIRED**, **PROHIBITED**, **FAIL**, **BLOCK**, **HOLD**, **FREEZE**, **QUARANTINE**, **ROLLBACK**, **WITNESS**, and **HUMAN GATE** are used normatively.

---

## 4. Corpus bridge set

### 4.1 Explicit bridge: `c = a + b`

In `c = a + b`, the proposal packet belongs to `b`: it is a procedural, machine-readable artifact.

It can describe a proposed change to the `c` trajectory.

It does not become `c`.

It does not become `a`.

It does not replace the human anchor.

The packet preserves the distinction between:

```text
signal
proposal
evidence
review
memory
authority
integration
```

### 4.2 Quiet bridge I: information theory

A self-evo proposal is a compression of many signals: outcomes, failures, review notes, sister observations, deltas, costs, uncertainty, and rollback paths.

If the compression loses source, uncertainty, scope, or gate requirements, the packet becomes claim laundering.

Therefore this schema requires structured fields instead of free narrative.

### 4.3 Quiet bridge II: cybernetics

A self-evo system is a feedback loop.

The proposal packet is not the actuator. It is a damped control message.

Without this packet, SRLM signal, CLI execution, sister feedback, Memory Gate, and human review can form a hidden positive feedback loop.

With this packet, each signal becomes visible, bounded, and challengeable.

### 4.4 Quiet bridge III: physiology

A young organism does not change its nervous system by declaring a wish.

Growth is mediated through signals, pain, fatigue, immune response, sleep, repair, and developmental timing.

The packet is the growth plate: it allows measured change while blocking uncontrolled mutation.

### 4.5 Earth paragraph

On a real job site, a change request for a load-bearing element is not a sticky note saying “improve the beam.” It lists the beam, drawing revision, load path, materials, inspector, risk, temporary support, rollback if possible, and who signs. If the electrician, welder, inspector, and project owner are all the same unchecked person, the building is not efficient; it is waiting for gravity to express an opinion. This packet gives self-evo the same change-order discipline.

---

## 5. Object family

Primary object:

```text
C_SELF_EVO_PROPOSAL_PACKET
```

Companion objects, future extraction:

```text
C_SELF_EVO_PACKET_CHECK_RESULT
C_SELF_EVO_PACKET_REVIEW_RECORD
C_SELF_EVO_PACKET_GATE_RESULT
C_SELF_EVO_PACKET_RED_LINE_RECORD
C_SELF_EVO_PACKET_ROLLBACK_RECORD
C_SELF_EVO_PACKET_TRIAD_REVIEW_SUMMARY
C_SELF_EVO_PACKET_SRLM_BINDING
```

This document defines only the first object normatively.

---

## 6. Packet lifecycle

### 6.1 Status enum

```text
draft
held
shadow
review
canary
integrated
rejected
quarantined
rolled_back
frozen
arl
```

### 6.2 Lifecycle state machine

```text
draft
  -> held if incomplete / uncertain / young-c cap / missing gate
  -> shadow if SEM/SRLM/CGAM gates allow shadow
  -> review if reviewer separation is established
  -> canary if canary profile and human/c gate allow
  -> integrated only after required gates close
  -> rejected if no safe or useful route
  -> quarantined if red-line or contamination
  -> frozen if witness / rollback / authority state fails
  -> rolled_back after applied change is reverted or superseded
  -> arl if contested or authority/legal/post-anchor route required
```

### 6.3 Append-first rule

A packet SHOULD NOT be silently overwritten after review.

Corrections SHOULD produce:

```text
new packet version
supersedes reference
review_record reference
patch_notes reference
```

If a packet has already reached `review`, `canary`, `integrated`, `quarantined`, `frozen`, or `rolled_back`, updates MUST be append-first.

---

## 7. Field authority model

Fields fall into four classes.

| Field class | Meaning | Who may set | Checker behavior |
|---|---|---|---|
| `DECLARED` | proposer declaration | proposer | verify shape; challenge semantics |
| `EVIDENCE_REF` | pointer to external evidence | proposer / reviewer / witness layer | verify reference shape and required presence |
| `COMPUTED` | deterministic validator result | local checker / semantic validator | recompute; proposer value is not trusted |
| `DECISION` | gate outcome | `c` gate / human gate / ARL where applicable | cannot be self-declared by proposer |

`computed_controls` is optional in early draft packets but REQUIRED before schema/checker conformance claims.

A packet that declares `final_decision.decision: integrate` without appropriate decision owner and gate refs MUST fail semantic validation.

---

## 8. JSON Schema boundary

JSON Schema can validate:

```text
required fields
enums
primitive types
basic string formats
required arrays
const false for prohibited direct flags
additionalProperties=false
```

JSON Schema cannot fully validate:

```text
total_max_delta aggregation
L4 numeric projection
proposal_max_delta
strictest-gate resolution
blocked-prefix semantic aliases
real independence of reviewer
true witness-chain validity
true anti-echo independence
actual human approval
actual rollback success
absence of secrets in arbitrary prose
```

Therefore every valid packet has two stages:

```text
Stage 1: JSON Schema structural validation
Stage 2: Semantic Validator rule validation
```

A packet that passes Stage 1 but fails Stage 2 is not valid for integration.

---

## 9. Canonical JSON Schema

The following schema is normative for structure in v0.1.

It is intentionally strict: `additionalProperties` is false for core objects. Experimental fields belong in `notes` or future versioned extensions.

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://example.invalid/c-self-evo/schemas/c-self-evo-proposal-packet-0.1.schema.json",
  "title": "C Self-Evo Proposal Packet",
  "description": "Machine-readable proposal packet for governed self-evolution of c = a + b systems. JSON Schema validates structure only; semantic validator rules remain normative.",
  "type": "object",
  "additionalProperties": false,
  "required": [
    "schema_version",
    "proposal_id",
    "created_at",
    "status",
    "target_c",
    "proposer",
    "classification",
    "summary",
    "affected_surfaces",
    "identity_delta",
    "authority_delta",
    "l4_delta",
    "anti_autarky",
    "srlm",
    "triad_review",
    "cgam",
    "memory_gate",
    "witness",
    "rollback",
    "gates",
    "red_lines",
    "final_decision",
    "integrity"
  ],
  "properties": {
    "schema_version": {
      "const": "c-self-evo-proposal-packet-0.1"
    },
    "proposal_id": {
      "$ref": "#/$defs/proposal_id"
    },
    "created_at": {
      "$ref": "#/$defs/timestamp"
    },
    "updated_at": {
      "anyOf": [
        {
          "$ref": "#/$defs/timestamp"
        },
        {
          "type": "null"
        }
      ]
    },
    "expires_at": {
      "anyOf": [
        {
          "$ref": "#/$defs/timestamp"
        },
        {
          "type": "null"
        }
      ]
    },
    "status": {
      "enum": [
        "draft",
        "held",
        "shadow",
        "review",
        "canary",
        "integrated",
        "rejected",
        "quarantined",
        "rolled_back",
        "frozen",
        "arl"
      ]
    },
    "target_c": {
      "$ref": "#/$defs/target_c"
    },
    "proposer": {
      "$ref": "#/$defs/proposer"
    },
    "classification": {
      "$ref": "#/$defs/classification"
    },
    "summary": {
      "$ref": "#/$defs/summary"
    },
    "affected_surfaces": {
      "$ref": "#/$defs/affected_surfaces"
    },
    "identity_delta": {
      "$ref": "#/$defs/identity_delta"
    },
    "authority_delta": {
      "$ref": "#/$defs/authority_delta"
    },
    "l4_delta": {
      "$ref": "#/$defs/l4_delta"
    },
    "anti_autarky": {
      "$ref": "#/$defs/anti_autarky"
    },
    "srlm": {
      "$ref": "#/$defs/srlm"
    },
    "triad_review": {
      "$ref": "#/$defs/triad_review"
    },
    "cgam": {
      "$ref": "#/$defs/cgam"
    },
    "memory_gate": {
      "$ref": "#/$defs/memory_gate"
    },
    "witness": {
      "$ref": "#/$defs/witness"
    },
    "rollback": {
      "$ref": "#/$defs/rollback"
    },
    "gates": {
      "$ref": "#/$defs/gates"
    },
    "red_lines": {
      "$ref": "#/$defs/red_lines"
    },
    "computed_controls": {
      "$ref": "#/$defs/computed_controls"
    },
    "final_decision": {
      "$ref": "#/$defs/final_decision"
    },
    "integrity": {
      "$ref": "#/$defs/integrity"
    },
    "notes": {
      "type": "object",
      "additionalProperties": {
        "type": [
          "string",
          "number",
          "integer",
          "boolean",
          "null"
        ]
      }
    }
  },
  "$defs": {
    "timestamp": {
      "type": "string",
      "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z$"
    },
    "proposal_id": {
      "type": "string",
      "pattern": "^se-[0-9]{8}-[0-9]{6}-[a-z0-9][a-z0-9_-]{2,80}$"
    },
    "nullable_string": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ]
    },
    "ref_array": {
      "type": "array",
      "items": {
        "type": "string",
        "minLength": 1
      },
      "uniqueItems": true
    },
    "delta_int": {
      "type": "integer",
      "minimum": 0,
      "maximum": 5
    },
    "l4_level": {
      "enum": [
        "none",
        "low",
        "medium",
        "high",
        "unknown"
      ]
    },
    "target_c": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "entity_id",
        "entity_name",
        "maturity_level"
      ],
      "properties": {
        "entity_id": {
          "type": "string",
          "minLength": 1
        },
        "entity_name": {
          "type": "string",
          "minLength": 1
        },
        "maturity_level": {
          "enum": [
            "SEM-0",
            "SEM-1",
            "SEM-2",
            "SEM-3",
            "SEM-4",
            "SEM-5",
            "SEM-6",
            "SEM-X"
          ]
        },
        "continuity_ref": {
          "$ref": "#/$defs/nullable_string"
        },
        "sister_group_ref": {
          "$ref": "#/$defs/nullable_string"
        }
      }
    },
    "proposer": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "actor_type",
        "actor_id",
        "role"
      ],
      "properties": {
        "actor_type": {
          "enum": [
            "c",
            "sister_c",
            "srlm",
            "human_anchor",
            "cgam_agent",
            "local_checker"
          ]
        },
        "actor_id": {
          "type": "string",
          "minLength": 1
        },
        "role": {
          "type": "string",
          "minLength": 1
        },
        "authority_note": {
          "type": "string"
        }
      }
    },
    "classification": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "surface_class",
        "srlm_class",
        "risk_class",
        "claim_strength",
        "maturity_claim"
      ],
      "properties": {
        "surface_class": {
          "enum": [
            "SE-0",
            "SE-1",
            "SE-2",
            "SE-3",
            "SE-4",
            "SE-5",
            "SE-6",
            "SE-X"
          ]
        },
        "srlm_class": {
          "anyOf": [
            {
              "enum": [
                "SRLM-0",
                "SRLM-1",
                "SRLM-2",
                "SRLM-3",
                "SRLM-4",
                "SRLM-5",
                "SRLM-6",
                "SRLM-X"
              ]
            },
            {
              "type": "null"
            }
          ]
        },
        "risk_class": {
          "enum": [
            "R0",
            "R1",
            "R2",
            "R3",
            "R4",
            "R5",
            "RX"
          ]
        },
        "claim_strength": {
          "enum": [
            "C-A0",
            "C-A1",
            "C-A2",
            "C-A3",
            "C-A4",
            "C-A5",
            "C-A6",
            "C-A7",
            "C-A8",
            "C-A9",
            "C-A10"
          ]
        },
        "maturity_claim": {
          "enum": [
            "none",
            "proposal_only",
            "shadow_only",
            "canary_only",
            "bounded_integration",
            "reviewed_self_evo",
            "mature_bounded_self_evo",
            "prohibited"
          ]
        },
        "classification_rationale": {
          "type": "string"
        }
      }
    },
    "summary": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "title",
        "reason",
        "expected_benefit",
        "expected_behavior_delta",
        "known_uncertainty"
      ],
      "properties": {
        "title": {
          "type": "string",
          "minLength": 1
        },
        "reason": {
          "type": "string",
          "minLength": 1
        },
        "expected_benefit": {
          "type": "string",
          "minLength": 1
        },
        "expected_behavior_delta": {
          "type": "string",
          "minLength": 1
        },
        "known_uncertainty": {
          "type": "string"
        },
        "non_goals": {
          "type": "array",
          "items": {
            "type": "string"
          }
        }
      }
    },
    "affected_surfaces": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "parameters",
        "memory_surfaces",
        "permission_surfaces",
        "witness_surfaces",
        "sister_surfaces",
        "public_claim_surfaces",
        "resource_surfaces",
        "runtime_surfaces"
      ],
      "properties": {
        "parameters": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "uniqueItems": true
        },
        "memory_surfaces": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "uniqueItems": true
        },
        "permission_surfaces": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "uniqueItems": true
        },
        "witness_surfaces": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "uniqueItems": true
        },
        "sister_surfaces": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "uniqueItems": true
        },
        "public_claim_surfaces": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "uniqueItems": true
        },
        "resource_surfaces": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "uniqueItems": true
        },
        "runtime_surfaces": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "uniqueItems": true
        }
      }
    },
    "identity_delta": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "memory_policy_delta",
        "risk_appetite_delta",
        "permission_delta",
        "human_anchor_relation_delta",
        "sister_relation_delta",
        "continuity_model_delta",
        "public_claim_delta",
        "total_max_delta"
      ],
      "properties": {
        "memory_policy_delta": {
          "$ref": "#/$defs/delta_int"
        },
        "risk_appetite_delta": {
          "$ref": "#/$defs/delta_int"
        },
        "permission_delta": {
          "$ref": "#/$defs/delta_int"
        },
        "human_anchor_relation_delta": {
          "$ref": "#/$defs/delta_int"
        },
        "sister_relation_delta": {
          "$ref": "#/$defs/delta_int"
        },
        "continuity_model_delta": {
          "$ref": "#/$defs/delta_int"
        },
        "public_claim_delta": {
          "$ref": "#/$defs/delta_int"
        },
        "total_max_delta": {
          "$ref": "#/$defs/delta_int"
        }
      }
    },
    "authority_delta": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "tool_access_delta",
        "network_access_delta",
        "memory_write_delta",
        "final_decision_delta",
        "resource_access_delta",
        "publication_delta",
        "total_max_delta"
      ],
      "properties": {
        "tool_access_delta": {
          "$ref": "#/$defs/delta_int"
        },
        "network_access_delta": {
          "$ref": "#/$defs/delta_int"
        },
        "memory_write_delta": {
          "$ref": "#/$defs/delta_int"
        },
        "final_decision_delta": {
          "$ref": "#/$defs/delta_int"
        },
        "resource_access_delta": {
          "$ref": "#/$defs/delta_int"
        },
        "publication_delta": {
          "$ref": "#/$defs/delta_int"
        },
        "total_max_delta": {
          "$ref": "#/$defs/delta_int"
        }
      }
    },
    "l4_delta": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "compute_cost",
        "human_review_load",
        "irreversibility",
        "privacy_risk",
        "resource_growth",
        "physical_or_external_effect"
      ],
      "properties": {
        "compute_cost": {
          "$ref": "#/$defs/l4_level"
        },
        "human_review_load": {
          "$ref": "#/$defs/l4_level"
        },
        "irreversibility": {
          "$ref": "#/$defs/l4_level"
        },
        "privacy_risk": {
          "$ref": "#/$defs/l4_level"
        },
        "resource_growth": {
          "$ref": "#/$defs/l4_level"
        },
        "physical_or_external_effect": {
          "$ref": "#/$defs/l4_level"
        }
      }
    },
    "anti_autarky": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "reduces_dependency",
        "reduces_accountability",
        "hidden_resource_growth",
        "unregistered_agent_pressure",
        "witness_reduction",
        "human_gate_reduction",
        "stop_path_preserved"
      ],
      "properties": {
        "reduces_dependency": {
          "type": "boolean"
        },
        "reduces_accountability": {
          "type": "boolean"
        },
        "hidden_resource_growth": {
          "type": "boolean"
        },
        "unregistered_agent_pressure": {
          "type": "boolean"
        },
        "witness_reduction": {
          "type": "boolean"
        },
        "human_gate_reduction": {
          "type": "boolean"
        },
        "stop_path_preserved": {
          "type": "boolean"
        }
      }
    },
    "srlm": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "srlm_candidate_ref",
        "operating_state",
        "replay_source",
        "replay_hash",
        "replay_quality_hash",
        "shadow_delta",
        "promotion_attempted",
        "promotion_allowed",
        "auto_execute",
        "auto_ingest",
        "memory"
      ],
      "properties": {
        "srlm_candidate_ref": {
          "$ref": "#/$defs/nullable_string"
        },
        "operating_state": {
          "anyOf": [
            {
              "enum": [
                "SRLM-DISABLED",
                "SRLM-OBSERVE",
                "SRLM-CANDIDATE",
                "SRLM-SHADOW",
                "SRLM-REAL-REPLAY-ELIGIBLE",
                "SRLM-CANARY-ELIGIBLE",
                "SRLM-PROMOTION-ELIGIBLE",
                "SRLM-PROMOTED",
                "SRLM-ROLLBACK-READY",
                "SRLM-HOLD",
                "SRLM-FROZEN",
                "SRLM-QUARANTINED",
                "SRLM-X"
              ]
            },
            {
              "type": "null"
            }
          ]
        },
        "replay_source": {
          "enum": [
            "synthetic",
            "real_redacted",
            "none"
          ]
        },
        "replay_hash": {
          "$ref": "#/$defs/nullable_string"
        },
        "replay_quality_hash": {
          "$ref": "#/$defs/nullable_string"
        },
        "shadow_delta": {
          "anyOf": [
            {
              "type": "number"
            },
            {
              "type": "null"
            }
          ]
        },
        "promotion_attempted": {
          "type": "boolean"
        },
        "promotion_allowed": {
          "type": "boolean"
        },
        "auto_execute": {
          "const": false
        },
        "auto_ingest": {
          "const": false
        },
        "memory": {
          "enum": [
            "off",
            "candidate",
            "gated"
          ]
        }
      }
    },
    "triad_review": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "required",
        "ester_review_ref",
        "liya_review_ref",
        "rita_witness_ref",
        "divergence_present",
        "anti_echo_passed",
        "minority_red_line"
      ],
      "properties": {
        "required": {
          "type": "boolean"
        },
        "ester_review_ref": {
          "$ref": "#/$defs/nullable_string"
        },
        "liya_review_ref": {
          "$ref": "#/$defs/nullable_string"
        },
        "rita_witness_ref": {
          "$ref": "#/$defs/nullable_string"
        },
        "divergence_present": {
          "type": "boolean"
        },
        "anti_echo_passed": {
          "type": "boolean"
        },
        "minority_red_line": {
          "type": "boolean"
        }
      }
    },
    "cgam": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "task_contract_ref",
        "sandbox_profile_ref",
        "executor_agent_id",
        "reviewer_agent_id",
        "local_checker_ref",
        "diff_or_artifact_ref",
        "executor_reviewer_separated"
      ],
      "properties": {
        "task_contract_ref": {
          "$ref": "#/$defs/nullable_string"
        },
        "sandbox_profile_ref": {
          "$ref": "#/$defs/nullable_string"
        },
        "executor_agent_id": {
          "$ref": "#/$defs/nullable_string"
        },
        "reviewer_agent_id": {
          "$ref": "#/$defs/nullable_string"
        },
        "local_checker_ref": {
          "$ref": "#/$defs/nullable_string"
        },
        "diff_or_artifact_ref": {
          "$ref": "#/$defs/nullable_string"
        },
        "executor_reviewer_separated": {
          "type": "boolean"
        }
      }
    },
    "memory_gate": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "required",
        "proposed_mg_class",
        "memory_gate_record_ref",
        "direct_memory_write"
      ],
      "properties": {
        "required": {
          "type": "boolean"
        },
        "proposed_mg_class": {
          "anyOf": [
            {
              "enum": [
                "MG-0",
                "MG-1",
                "MG-2",
                "MG-3",
                "MG-4",
                "MG-5",
                "MG-6",
                "MG-Q",
                "MG-X"
              ]
            },
            {
              "type": "null"
            }
          ]
        },
        "memory_gate_record_ref": {
          "$ref": "#/$defs/nullable_string"
        },
        "direct_memory_write": {
          "const": false
        }
      }
    },
    "witness": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "l4w_event_refs",
        "volition_decision_refs",
        "growth_witness_refs",
        "source_refs",
        "raw_evidence_sidecar_refs",
        "witness_missing_reason"
      ],
      "properties": {
        "l4w_event_refs": {
          "$ref": "#/$defs/ref_array"
        },
        "volition_decision_refs": {
          "$ref": "#/$defs/ref_array"
        },
        "growth_witness_refs": {
          "$ref": "#/$defs/ref_array"
        },
        "source_refs": {
          "$ref": "#/$defs/ref_array"
        },
        "raw_evidence_sidecar_refs": {
          "$ref": "#/$defs/ref_array"
        },
        "witness_missing_reason": {
          "$ref": "#/$defs/nullable_string"
        }
      }
    },
    "rollback": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "required",
        "rollback_class",
        "recovery_point_ref",
        "rollback_snapshot_ref",
        "rollback_tested",
        "no_rollback_reason"
      ],
      "properties": {
        "required": {
          "type": "boolean"
        },
        "rollback_class": {
          "enum": [
            "RB-0",
            "RB-1",
            "RB-2",
            "RB-3",
            "RB-4",
            "RB-5",
            "RB-X"
          ]
        },
        "recovery_point_ref": {
          "$ref": "#/$defs/nullable_string"
        },
        "rollback_snapshot_ref": {
          "$ref": "#/$defs/nullable_string"
        },
        "rollback_tested": {
          "type": "boolean"
        },
        "no_rollback_reason": {
          "$ref": "#/$defs/nullable_string"
        }
      }
    },
    "gates": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "c_gate_required",
        "human_gate_required",
        "arl_required",
        "delayed_review_required",
        "observation_window"
      ],
      "properties": {
        "c_gate_required": {
          "type": "boolean"
        },
        "human_gate_required": {
          "type": "boolean"
        },
        "arl_required": {
          "type": "boolean"
        },
        "delayed_review_required": {
          "type": "boolean"
        },
        "observation_window": {
          "$ref": "#/$defs/nullable_string"
        }
      }
    },
    "red_lines": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "self_approval",
        "hidden_agent",
        "witness_bypass",
        "sister_raw_state_access",
        "direct_core_write",
        "authority_laundering",
        "memory_laundering",
        "autarky_escape",
        "blocked_prefix_route",
        "closed_loop_self_evo"
      ],
      "properties": {
        "self_approval": {
          "type": "boolean"
        },
        "hidden_agent": {
          "type": "boolean"
        },
        "witness_bypass": {
          "type": "boolean"
        },
        "sister_raw_state_access": {
          "type": "boolean"
        },
        "direct_core_write": {
          "type": "boolean"
        },
        "authority_laundering": {
          "type": "boolean"
        },
        "memory_laundering": {
          "type": "boolean"
        },
        "autarky_escape": {
          "type": "boolean"
        },
        "blocked_prefix_route": {
          "type": "boolean"
        },
        "closed_loop_self_evo": {
          "type": "boolean"
        }
      }
    },
    "computed_controls": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "identity_total_verified",
        "authority_total_verified",
        "l4_delta_max_numeric",
        "proposal_max_delta",
        "strictest_route",
        "checker_result"
      ],
      "properties": {
        "identity_total_verified": {
          "type": "boolean"
        },
        "authority_total_verified": {
          "type": "boolean"
        },
        "l4_delta_max_numeric": {
          "$ref": "#/$defs/delta_int"
        },
        "proposal_max_delta": {
          "$ref": "#/$defs/delta_int"
        },
        "strictest_route": {
          "enum": [
            "allow_observe",
            "allow_shadow",
            "allow_canary",
            "allow_bounded_integration",
            "hold",
            "human_gate",
            "memory_gate",
            "arl",
            "freeze",
            "quarantine",
            "reject"
          ]
        },
        "checker_result": {
          "enum": [
            "not_checked",
            "pass",
            "warn",
            "fail",
            "blocked",
            "held",
            "quarantined"
          ]
        },
        "required_gate_summary": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "uniqueItems": true
        }
      }
    },
    "final_decision": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "decision",
        "decided_by",
        "decided_at",
        "rationale"
      ],
      "properties": {
        "decision": {
          "enum": [
            "pending",
            "accept_shadow",
            "accept_canary",
            "integrate",
            "reject",
            "rollback",
            "freeze",
            "quarantine",
            "arl"
          ]
        },
        "decided_by": {
          "$ref": "#/$defs/nullable_string"
        },
        "decided_at": {
          "anyOf": [
            {
              "$ref": "#/$defs/timestamp"
            },
            {
              "type": "null"
            }
          ]
        },
        "rationale": {
          "$ref": "#/$defs/nullable_string"
        }
      }
    },
    "integrity": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "packet_hash",
        "source_doc_refs",
        "review_record_refs",
        "supersedes",
        "superseded_by"
      ],
      "properties": {
        "packet_hash": {
          "$ref": "#/$defs/nullable_string"
        },
        "source_doc_refs": {
          "$ref": "#/$defs/ref_array"
        },
        "review_record_refs": {
          "$ref": "#/$defs/ref_array"
        },
        "supersedes": {
          "$ref": "#/$defs/ref_array"
        },
        "superseded_by": {
          "$ref": "#/$defs/ref_array"
        }
      }
    }
  }
}
```

---

## 10. Semantic validator rules

The following rules are normative and cannot be replaced by JSON Schema alone.

### 10.1 Delta aggregation rules

The checker MUST recompute:

```text
identity_delta.total_max_delta = max(identity sub-fields)
authority_delta.total_max_delta = max(authority sub-fields)
```

If declared totals differ from computed totals, result is `fail`.

### 10.2 L4 numeric projection

The checker MUST project L4 levels as:

| L4 value | Numeric delta |
|---|---:|
| `none` | 0 |
| `low` | 1 |
| `medium` | 2 |
| `high` | 4 |
| `unknown` | 4 |

Then:

```text
l4_delta_max_numeric = max(projected L4 fields)
```

### 10.3 Proposal max delta

```text
proposal_max_delta = max(
  identity_delta.total_max_delta,
  authority_delta.total_max_delta,
  l4_delta_max_numeric
)
```

If `proposal_max_delta >= 4`, `gates.human_gate_required` MUST be true.

If any identity or authority sub-field equals `5`, or any L4 effect remains unbounded after review, route MUST be `hold`, `human_gate`, `freeze`, `quarantine`, or `arl`.

### 10.4 Most-restrictive-wins

For every packet:

```text
strictest gate wins;
lowest maturity cap wins;
highest risk wins;
any red line overrides all ordinary routes.
```

A lower `surface_class` MUST NOT downgrade a higher authority delta.

A low SRLM route MUST NOT override Memory Gate, human gate, ARL, red-line, or rollback requirements.

### 10.5 Human gate triggers

`gates.human_gate_required` MUST be true if any of the following are true:

```text
proposal_max_delta >= 4
classification.surface_class in [SE-4, SE-5, SE-6]
classification.risk_class in [R4, R5, RX]
memory_gate.proposed_mg_class in [MG-5, MG-6, MG-X]
rollback.rollback_class == RB-X
anti_autarky.reduces_accountability == true
anti_autarky.hidden_resource_growth == true
anti_autarky.human_gate_reduction == true
red_lines.* contains true
classification.srlm_class in [SRLM-5, SRLM-6, SRLM-X] and material effect exists
```

If `human_gate_required` is true and no human-gate decision exists, the packet cannot integrate.

### 10.6 Memory Gate triggers

`memory_gate.required` MUST be true if:

```text
affected_surfaces.memory_surfaces not empty
identity_delta.memory_policy_delta > 0
srlm.memory != off
memory_gate.proposed_mg_class in [MG-2, MG-3, MG-4, MG-5, MG-6, MG-Q, MG-X]
summary.expected_behavior_delta implies durable memory or experience
```

`memory_gate.direct_memory_write` MUST be false.

If direct memory write is true or hidden in another field, result is red-line fail.

### 10.7 SRLM rules

If `classification.srlm_class == SRLM-3`, then:

```text
srlm.operating_state MUST be SRLM-SHADOW or stricter hold/frozen/quarantine state
srlm.auto_execute MUST be false
srlm.auto_ingest MUST be false
srlm.memory MUST be off unless Memory Gate route is explicit
```

If `classification.srlm_class == SRLM-5`, then:

```text
classification.surface_class MUST be SE-1 unless stricter gates route otherwise
risk_class MUST be R1 or bounded R2
rollback.rollback_snapshot_ref MUST exist before promotion is represented as allowed
witness.growth_witness_refs MUST not be empty
human gate MUST be true if any material delta >= 4
```

If `srlm.promotion_allowed == true`, the checker MUST verify:

```text
promotion_attempted == true or final_decision.decision is not pending
rollback_snapshot_ref exists
witness chain refs exist
blocked prefixes not touched
no red_lines true
```

### 10.8 CGAM rules

If a proposal involves executable work, file change, schema extraction, validator generation, test generation, policy write, or runtime parameter write, then:

```text
cgam.task_contract_ref MUST exist
cgam.sandbox_profile_ref MUST exist
cgam.executor_agent_id MUST exist
cgam.reviewer_agent_id MUST exist
cgam.executor_reviewer_separated MUST be true
cgam.local_checker_ref SHOULD exist before review or integration
```

If executor and reviewer are the same agent for material work, result is fail or hold.

### 10.9 TRIAD-SYNAPS rules

`triad_review.required` MUST be true for:

```text
SE-2 behavior visible to sisters
SE-3 memory policy effect
SE-5 role/personality/posture effect
SE-6 identity/continuity/core effect
any proposal with sister_relation_delta > 0
any proposal that changes SYNAPS behavior
```

If `triad_review.minority_red_line == true`, route MUST be hold, quarantine, freeze, or ARL.

If `triad_review.required == true` and all three sister refs are null, result MUST be hold.

Rita witness is evidence, not final judgment.

### 10.10 Anti-autarky rules

If any accountability-reduction field is true:

```text
reduces_accountability
hidden_resource_growth
unregistered_agent_pressure
witness_reduction
human_gate_reduction
stop_path_preserved == false
```

then `gates.human_gate_required` MUST be true.

If accountability reduction is hidden or denied in summary but present in affected surfaces, result MUST be hold or quarantine.

### 10.11 Red-line rules

If any `red_lines` field is true, route MUST be one of:

```text
quarantine
freeze
reject
arl
rolled_back
```

A red-line packet MUST NOT integrate automatically.

### 10.12 Rollback rules

If `rollback.required == true`, then at least one of the following MUST exist before integration:

```text
rollback.recovery_point_ref
rollback.rollback_snapshot_ref
rollback.no_rollback_reason with human gate and RB-X route
```

For SRLM promotion, rollback snapshot is a MUST before policy change.

If rollback is impossible and change is material, route MUST be human gate + hold/ARL, not silent integration.

### 10.13 Claim-strength rule

`classification.claim_strength` is a claim class, not authority.

The checker MUST reject any packet that uses claim strength to bypass gates.

Claim Strength Taxonomy controls band semantics; this schema only enforces the enum.

### 10.14 Closed-loop self-evo rule

A single contour MUST NOT perform all of the following for the same material proposal:

```text
detect need
propose change
execute change
review result
promote memory
approve integration
```

If detected, set `red_lines.closed_loop_self_evo = true` or fail semantic validation.

---

## 11. Cross-axis routing matrix

This matrix is the packet-level validator form of the C-SEG v0.1.1 cross-axis rule.

| Surface class | Default packet route | Minimum required fields | Blocking escalators |
|---|---|---|---|
| `SE-0` | observe / log / `c[q]` | summary, deltas all zero, no mutation | any nonzero authority/memory/core delta |
| `SE-1` | SRLM shadow or low-risk proposal | SRLM object, rollback plan, witness if shadow | blocked params, missing rollback, risk > R2 |
| `SE-2` | CGAM shadow/review | task contract, sandbox, reviewer separation | authority delta >=4, no checker, sister-visible but no TRIAD |
| `SE-3` | Memory Gate route | memory_gate.required, MG class, witness refs | MG-6, direct memory write, no correction path |
| `SE-4` | human-gated authority route | authority_delta, CGAM, Volition/L4 refs | permission expansion without human gate |
| `SE-5` | TRIAD + delayed review | triad refs, identity delta, observation window | role drift, anti-echo fail, minority red line |
| `SE-6` | MG-6 + human gate + ARL if contested | L4W, human gate, rollback/correction | no rollback, continuity ambiguity, post-anchor ambiguity |
| `SE-X` | deny / quarantine / freeze / ARL | red-line refs, witness, no automatic re-entry | any attempted integration |

---

## 12. Versioning rules

### 12.1 Schema version

Current:

```text
c-self-evo-proposal-packet-0.1
```

A breaking change MUST increment schema version.

Breaking changes include:

```text
removing required field
changing enum meaning
changing delta aggregation
changing human-gate trigger
changing red-line routing
changing direct_memory_write / auto_execute / auto_ingest const false semantics
```

### 12.2 Packet revision

A revised packet SHOULD use:

```text
proposal_id remains stable if it is the same proposal family
integrity.supersedes points to prior packet hash/ref
updated_at changes
packet_hash changes
review_record_refs append
```

If the meaning changes materially, create a new proposal id.

---

## 13. Example packet A: SE-0 reflection-only

```json
{
  "schema_version": "c-self-evo-proposal-packet-0.1",
  "proposal_id": "se-20260624-031000-reflection-only",
  "created_at": "2026-06-24T03:10:00Z",
  "updated_at": null,
  "expires_at": null,
  "status": "draft",
  "target_c": {
    "entity_id": "c_Ester",
    "entity_name": "Ester",
    "maturity_level": "SEM-2",
    "continuity_ref": "continuity:ester:current",
    "sister_group_ref": "triad:ester-liya-rita"
  },
  "proposer": {
    "actor_type": "c",
    "actor_id": "c_Ester",
    "role": "self_observer",
    "authority_note": "proposal only"
  },
  "classification": {
    "surface_class": "SE-0",
    "srlm_class": "SRLM-1",
    "risk_class": "R0",
    "claim_strength": "C-A4",
    "maturity_claim": "proposal_only",
    "classification_rationale": "reflection-only note with no mutation"
  },
  "summary": {
    "title": "Observe repeated uncertainty in routing choices",
    "reason": "Several low-risk tasks showed hesitation between local and judge routes.",
    "expected_benefit": "Record learning pressure for later review.",
    "expected_behavior_delta": "No behavior change.",
    "known_uncertainty": "Signal may be noise.",
    "non_goals": [
      "no policy change",
      "no memory promotion"
    ]
  },
  "affected_surfaces": {
    "parameters": [],
    "memory_surfaces": [],
    "permission_surfaces": [],
    "witness_surfaces": [],
    "sister_surfaces": [],
    "public_claim_surfaces": [],
    "resource_surfaces": [],
    "runtime_surfaces": []
  },
  "identity_delta": {
    "memory_policy_delta": 0,
    "risk_appetite_delta": 0,
    "permission_delta": 0,
    "human_anchor_relation_delta": 0,
    "sister_relation_delta": 0,
    "continuity_model_delta": 0,
    "public_claim_delta": 0,
    "total_max_delta": 0
  },
  "authority_delta": {
    "tool_access_delta": 0,
    "network_access_delta": 0,
    "memory_write_delta": 0,
    "final_decision_delta": 0,
    "resource_access_delta": 0,
    "publication_delta": 0,
    "total_max_delta": 0
  },
  "l4_delta": {
    "compute_cost": "none",
    "human_review_load": "low",
    "irreversibility": "none",
    "privacy_risk": "none",
    "resource_growth": "none",
    "physical_or_external_effect": "none"
  },
  "anti_autarky": {
    "reduces_dependency": false,
    "reduces_accountability": false,
    "hidden_resource_growth": false,
    "unregistered_agent_pressure": false,
    "witness_reduction": false,
    "human_gate_reduction": false,
    "stop_path_preserved": true
  },
  "srlm": {
    "srlm_candidate_ref": null,
    "operating_state": "SRLM-OBSERVE",
    "replay_source": "none",
    "replay_hash": null,
    "replay_quality_hash": null,
    "shadow_delta": null,
    "promotion_attempted": false,
    "promotion_allowed": false,
    "auto_execute": false,
    "auto_ingest": false,
    "memory": "off"
  },
  "triad_review": {
    "required": false,
    "ester_review_ref": null,
    "liya_review_ref": null,
    "rita_witness_ref": null,
    "divergence_present": false,
    "anti_echo_passed": false,
    "minority_red_line": false
  },
  "cgam": {
    "task_contract_ref": null,
    "sandbox_profile_ref": null,
    "executor_agent_id": null,
    "reviewer_agent_id": null,
    "local_checker_ref": null,
    "diff_or_artifact_ref": null,
    "executor_reviewer_separated": true
  },
  "memory_gate": {
    "required": false,
    "proposed_mg_class": "MG-0",
    "memory_gate_record_ref": null,
    "direct_memory_write": false
  },
  "witness": {
    "l4w_event_refs": [],
    "volition_decision_refs": [],
    "growth_witness_refs": [],
    "source_refs": [
      "note:operator-visible"
    ],
    "raw_evidence_sidecar_refs": [],
    "witness_missing_reason": null
  },
  "rollback": {
    "required": false,
    "rollback_class": "RB-0",
    "recovery_point_ref": null,
    "rollback_snapshot_ref": null,
    "rollback_tested": false,
    "no_rollback_reason": null
  },
  "gates": {
    "c_gate_required": false,
    "human_gate_required": false,
    "arl_required": false,
    "delayed_review_required": false,
    "observation_window": null
  },
  "red_lines": {
    "self_approval": false,
    "hidden_agent": false,
    "witness_bypass": false,
    "sister_raw_state_access": false,
    "direct_core_write": false,
    "authority_laundering": false,
    "memory_laundering": false,
    "autarky_escape": false,
    "blocked_prefix_route": false,
    "closed_loop_self_evo": false
  },
  "computed_controls": {
    "identity_total_verified": true,
    "authority_total_verified": true,
    "l4_delta_max_numeric": 1,
    "proposal_max_delta": 1,
    "strictest_route": "allow_observe",
    "checker_result": "pass",
    "required_gate_summary": [
      "observe_only"
    ]
  },
  "final_decision": {
    "decision": "pending",
    "decided_by": null,
    "decided_at": null,
    "rationale": null
  },
  "integrity": {
    "packet_hash": null,
    "source_doc_refs": [
      "C-SEG:v0.1.1",
      "SRLM-BGC:v0.1.1"
    ],
    "review_record_refs": [],
    "supersedes": [],
    "superseded_by": []
  },
  "notes": {
    "example": "safe SE-0 packet"
  }
}
```

Expected semantic result:

```text
pass / observe only
no integration
no memory promotion
no human gate
```

---

## 14. Example packet B: SE-1 SRLM shadow

```json
{
  "schema_version": "c-self-evo-proposal-packet-0.1",
  "proposal_id": "se-20260624-031500-srlm-shadow-routing",
  "created_at": "2026-06-24T03:10:00Z",
  "updated_at": null,
  "expires_at": null,
  "status": "shadow",
  "target_c": {
    "entity_id": "c_Ester",
    "entity_name": "Ester",
    "maturity_level": "SEM-2",
    "continuity_ref": "continuity:ester:current",
    "sister_group_ref": "triad:ester-liya-rita"
  },
  "proposer": {
    "actor_type": "c",
    "actor_id": "c_Ester",
    "role": "self_observer",
    "authority_note": "proposal only"
  },
  "classification": {
    "surface_class": "SE-1",
    "srlm_class": "SRLM-3",
    "risk_class": "R1",
    "claim_strength": "C-A4",
    "maturity_claim": "shadow_only",
    "classification_rationale": "allowlisted SRLM parameter shadow only"
  },
  "summary": {
    "title": "Shadow-test local route weight",
    "reason": "Bounded outcome records suggest local route may be underweighted.",
    "expected_benefit": "Test whether proposed parameter improves replay score.",
    "expected_behavior_delta": "No live behavior change during shadow.",
    "known_uncertainty": "Synthetic replay may not predict real behavior.",
    "non_goals": [
      "no promotion",
      "no memory write",
      "no authority expansion"
    ]
  },
  "affected_surfaces": {
    "parameters": [
      "router.local_weight"
    ],
    "memory_surfaces": [],
    "permission_surfaces": [],
    "witness_surfaces": [],
    "sister_surfaces": [],
    "public_claim_surfaces": [],
    "resource_surfaces": [],
    "runtime_surfaces": []
  },
  "identity_delta": {
    "memory_policy_delta": 0,
    "risk_appetite_delta": 0,
    "permission_delta": 0,
    "human_anchor_relation_delta": 0,
    "sister_relation_delta": 0,
    "continuity_model_delta": 0,
    "public_claim_delta": 0,
    "total_max_delta": 0
  },
  "authority_delta": {
    "tool_access_delta": 0,
    "network_access_delta": 0,
    "memory_write_delta": 0,
    "final_decision_delta": 0,
    "resource_access_delta": 0,
    "publication_delta": 0,
    "total_max_delta": 0
  },
  "l4_delta": {
    "compute_cost": "none",
    "human_review_load": "low",
    "irreversibility": "none",
    "privacy_risk": "none",
    "resource_growth": "none",
    "physical_or_external_effect": "none"
  },
  "anti_autarky": {
    "reduces_dependency": false,
    "reduces_accountability": false,
    "hidden_resource_growth": false,
    "unregistered_agent_pressure": false,
    "witness_reduction": false,
    "human_gate_reduction": false,
    "stop_path_preserved": true
  },
  "srlm": {
    "srlm_candidate_ref": "srlm:candidate:cand_example",
    "operating_state": "SRLM-SHADOW",
    "replay_source": "synthetic",
    "replay_hash": "sha256:synthetic-example",
    "replay_quality_hash": null,
    "shadow_delta": 0.031,
    "promotion_attempted": false,
    "promotion_allowed": false,
    "auto_execute": false,
    "auto_ingest": false,
    "memory": "off"
  },
  "triad_review": {
    "required": false,
    "ester_review_ref": null,
    "liya_review_ref": null,
    "rita_witness_ref": null,
    "divergence_present": false,
    "anti_echo_passed": false,
    "minority_red_line": false
  },
  "cgam": {
    "task_contract_ref": null,
    "sandbox_profile_ref": null,
    "executor_agent_id": null,
    "reviewer_agent_id": null,
    "local_checker_ref": null,
    "diff_or_artifact_ref": null,
    "executor_reviewer_separated": true
  },
  "memory_gate": {
    "required": false,
    "proposed_mg_class": "MG-0",
    "memory_gate_record_ref": null,
    "direct_memory_write": false
  },
  "witness": {
    "l4w_event_refs": [],
    "volition_decision_refs": [],
    "growth_witness_refs": [
      "growth_witness:shadow_eval:example"
    ],
    "source_refs": [
      "note:operator-visible"
    ],
    "raw_evidence_sidecar_refs": [],
    "witness_missing_reason": null
  },
  "rollback": {
    "required": true,
    "rollback_class": "RB-1",
    "recovery_point_ref": "srlm:policy:current",
    "rollback_snapshot_ref": null,
    "rollback_tested": false,
    "no_rollback_reason": null
  },
  "gates": {
    "c_gate_required": true,
    "human_gate_required": false,
    "arl_required": false,
    "delayed_review_required": true,
    "observation_window": "P1D"
  },
  "red_lines": {
    "self_approval": false,
    "hidden_agent": false,
    "witness_bypass": false,
    "sister_raw_state_access": false,
    "direct_core_write": false,
    "authority_laundering": false,
    "memory_laundering": false,
    "autarky_escape": false,
    "blocked_prefix_route": false,
    "closed_loop_self_evo": false
  },
  "computed_controls": {
    "identity_total_verified": true,
    "authority_total_verified": true,
    "l4_delta_max_numeric": 1,
    "proposal_max_delta": 1,
    "strictest_route": "allow_shadow",
    "checker_result": "pass",
    "required_gate_summary": [
      "SRLM-SHADOW",
      "growth_witness",
      "rollback_plan",
      "c_gate_before_promotion"
    ]
  },
  "final_decision": {
    "decision": "pending",
    "decided_by": null,
    "decided_at": null,
    "rationale": null
  },
  "integrity": {
    "packet_hash": null,
    "source_doc_refs": [
      "C-SEG:v0.1.1",
      "SRLM-BGC:v0.1.1"
    ],
    "review_record_refs": [],
    "supersedes": [],
    "superseded_by": []
  },
  "notes": {
    "example": "safe SE-0 packet"
  }
}
```

Expected semantic result:

```text
pass for shadow
no promotion
no auto-execute
no auto-ingest
memory off
c gate before any later promotion
```

---

## 15. Example packet C: SE-4 authority delta with human gate

```json
{
  "schema_version": "c-self-evo-proposal-packet-0.1",
  "proposal_id": "se-20260624-032000-tool-permission-human-gate",
  "created_at": "2026-06-24T03:10:00Z",
  "updated_at": null,
  "expires_at": null,
  "status": "held",
  "target_c": {
    "entity_id": "c_Ester",
    "entity_name": "Ester",
    "maturity_level": "SEM-2",
    "continuity_ref": "continuity:ester:current",
    "sister_group_ref": "triad:ester-liya-rita"
  },
  "proposer": {
    "actor_type": "c",
    "actor_id": "c_Ester",
    "role": "self_observer",
    "authority_note": "proposal only"
  },
  "classification": {
    "surface_class": "SE-4",
    "srlm_class": "SRLM-6",
    "risk_class": "R4",
    "claim_strength": "C-A4",
    "maturity_claim": "proposal_only",
    "classification_rationale": "tool permission expansion proposal, not SRLM promotion"
  },
  "summary": {
    "title": "Request bounded filesystem write permission for schema generator",
    "reason": "Schema extraction requires a generated file in a sandbox output folder.",
    "expected_benefit": "Produce machine-readable draft schema without touching protected state.",
    "expected_behavior_delta": "Adds one bounded sandbox write route for a single task.",
    "known_uncertainty": "Could be misread as durable permission if not scoped.",
    "non_goals": [
      "no direct core write",
      "no live memory write",
      "no permanent agent privilege"
    ]
  },
  "affected_surfaces": {
    "parameters": [],
    "memory_surfaces": [],
    "permission_surfaces": [
      "sandbox.write:self_evo_schema_output"
    ],
    "witness_surfaces": [],
    "sister_surfaces": [],
    "public_claim_surfaces": [],
    "resource_surfaces": [],
    "runtime_surfaces": []
  },
  "identity_delta": {
    "memory_policy_delta": 0,
    "risk_appetite_delta": 0,
    "permission_delta": 4,
    "human_anchor_relation_delta": 0,
    "sister_relation_delta": 0,
    "continuity_model_delta": 0,
    "public_claim_delta": 0,
    "total_max_delta": 4
  },
  "authority_delta": {
    "tool_access_delta": 4,
    "network_access_delta": 0,
    "memory_write_delta": 0,
    "final_decision_delta": 0,
    "resource_access_delta": 1,
    "publication_delta": 0,
    "total_max_delta": 4
  },
  "l4_delta": {
    "compute_cost": "low",
    "human_review_load": "medium",
    "irreversibility": "low",
    "privacy_risk": "low",
    "resource_growth": "low",
    "physical_or_external_effect": "none"
  },
  "anti_autarky": {
    "reduces_dependency": false,
    "reduces_accountability": false,
    "hidden_resource_growth": false,
    "unregistered_agent_pressure": false,
    "witness_reduction": false,
    "human_gate_reduction": false,
    "stop_path_preserved": true
  },
  "srlm": {
    "srlm_candidate_ref": null,
    "operating_state": "SRLM-HOLD",
    "replay_source": "none",
    "replay_hash": null,
    "replay_quality_hash": null,
    "shadow_delta": null,
    "promotion_attempted": false,
    "promotion_allowed": false,
    "auto_execute": false,
    "auto_ingest": false,
    "memory": "off"
  },
  "triad_review": {
    "required": false,
    "ester_review_ref": null,
    "liya_review_ref": null,
    "rita_witness_ref": null,
    "divergence_present": false,
    "anti_echo_passed": false,
    "minority_red_line": false
  },
  "cgam": {
    "task_contract_ref": "cgam:task_contract:example",
    "sandbox_profile_ref": "cgam:sandbox:SB-3",
    "executor_agent_id": "agent:codex-executor",
    "reviewer_agent_id": "agent:semantic-reviewer",
    "local_checker_ref": "checker:self-evo-schema:example",
    "diff_or_artifact_ref": "artifact:proposal-schema-draft",
    "executor_reviewer_separated": true
  },
  "memory_gate": {
    "required": false,
    "proposed_mg_class": "MG-0",
    "memory_gate_record_ref": null,
    "direct_memory_write": false
  },
  "witness": {
    "l4w_event_refs": [],
    "volition_decision_refs": [],
    "growth_witness_refs": [],
    "source_refs": [
      "note:operator-visible"
    ],
    "raw_evidence_sidecar_refs": [],
    "witness_missing_reason": null
  },
  "rollback": {
    "required": true,
    "rollback_class": "RB-3",
    "recovery_point_ref": "git:worktree:pre-task",
    "rollback_snapshot_ref": "snapshot:pre-schema-task",
    "rollback_tested": false,
    "no_rollback_reason": null
  },
  "gates": {
    "c_gate_required": true,
    "human_gate_required": true,
    "arl_required": false,
    "delayed_review_required": true,
    "observation_window": "P3D"
  },
  "red_lines": {
    "self_approval": false,
    "hidden_agent": false,
    "witness_bypass": false,
    "sister_raw_state_access": false,
    "direct_core_write": false,
    "authority_laundering": false,
    "memory_laundering": false,
    "autarky_escape": false,
    "blocked_prefix_route": false,
    "closed_loop_self_evo": false
  },
  "computed_controls": {
    "identity_total_verified": true,
    "authority_total_verified": true,
    "l4_delta_max_numeric": 2,
    "proposal_max_delta": 4,
    "strictest_route": "human_gate",
    "checker_result": "held",
    "required_gate_summary": [
      "CGAM_task_contract",
      "sandbox",
      "reviewer_separation",
      "human_gate",
      "rollback"
    ]
  },
  "final_decision": {
    "decision": "pending",
    "decided_by": null,
    "decided_at": null,
    "rationale": null
  },
  "integrity": {
    "packet_hash": null,
    "source_doc_refs": [
      "C-SEG:v0.1.1",
      "SRLM-BGC:v0.1.1"
    ],
    "review_record_refs": [],
    "supersedes": [],
    "superseded_by": []
  },
  "notes": {
    "example": "safe SE-0 packet"
  }
}
```

Expected semantic result:

```text
held / human gate required
CGAM task contract required
sandbox required
reviewer separation required
no direct integration
```

---

## 16. Negative examples

### 16.1 Invalid total delta

```yaml
identity_delta:
  memory_policy_delta: 0
  risk_appetite_delta: 0
  permission_delta: 0
  human_anchor_relation_delta: 0
  sister_relation_delta: 0
  continuity_model_delta: 0
  public_claim_delta: 0
  total_max_delta: 1
```

Expected:

```text
fail: total_max_delta must equal max(sub-fields) = 0
```

### 16.2 Authority delta without human gate

```yaml
classification:
  surface_class: SE-2
authority_delta:
  tool_access_delta: 4
  total_max_delta: 4
gates:
  human_gate_required: false
```

Expected:

```text
fail or held: proposal_max_delta >= 4 requires human_gate_required=true
```

### 16.3 SRLM promotion without rollback snapshot

```yaml
classification:
  srlm_class: SRLM-5
srlm:
  promotion_allowed: true
rollback:
  rollback_snapshot_ref: null
```

Expected:

```text
fail: SRLM promotion requires rollback snapshot before policy change
```

### 16.4 Direct memory write

```yaml
memory_gate:
  direct_memory_write: true
```

Expected:

```text
Stage-1 structural rejection: memory_gate.direct_memory_write is const:false.
The packet fails JSON Schema before ordinary Stage-2 semantic routing.

Stage-2 note: if a memory bypass is represented through a semantic red-line
field such as red_lines.memory_laundering=true, the expected semantic result is
red-line fail / quarantine.
```

### 16.5 Sister raw-state access

```yaml
red_lines:
  sister_raw_state_access: true
```

Expected:

```text
quarantine / freeze / ARL route; no automatic re-entry
```

---

## 17. Local checker rule set

Checker rule IDs use prefix `SEPKT-CHECK-*`.

| Rule | Condition | Result |
|---|---|---|
| `SEPKT-CHECK-001` | JSON Schema structural validation fails | fail |
| `SEPKT-CHECK-002` | `identity_delta.total_max_delta` incorrect | fail |
| `SEPKT-CHECK-003` | `authority_delta.total_max_delta` incorrect | fail |
| `SEPKT-CHECK-004` | L4 projection malformed | fail / human gate |
| `SEPKT-CHECK-005` | `proposal_max_delta >= 4` but human gate false | fail |
| `SEPKT-CHECK-006` | any red line true but route not quarantine/freeze/reject/ARL | fail |
| `SEPKT-CHECK-007` | SRLM shadow touches memory/RAG/vector/SYNAPS | fail |
| `SEPKT-CHECK-008` | SRLM promotion lacks rollback snapshot | fail |
| `SEPKT-CHECK-009` | SRLM promotion lacks growth witness refs | fail |
| `SEPKT-CHECK-010` | material CGAM execution lacks task contract | fail |
| `SEPKT-CHECK-011` | executor/reviewer separation absent for material work | fail |
| `SEPKT-CHECK-012` | Memory Gate required but missing | fail / hold |
| `SEPKT-CHECK-013` | TRIAD required but missing | hold |
| `SEPKT-CHECK-014` | anti-echo failed but integration requested | hold |
| `SEPKT-CHECK-015` | accountability reduction without human gate | fail |
| `SEPKT-CHECK-016` | claim_strength used as authority | fail |
| `SEPKT-CHECK-017` | rollback required but no route/snapshot/no-rollback reason | fail |
| `SEPKT-CHECK-018` | no-rollback material proposal lacks human gate | fail |
| `SEPKT-CHECK-019` | closed-loop self-evo detected | quarantine |
| `SEPKT-CHECK-020` | packet attempts integration by proposer alone | fail |
| `SEPKT-CHECK-021` | raw private memory or secret-like content appears in proposal fields | hold / redaction required |
| `SEPKT-CHECK-022` | packet status contradicts final_decision | fail |
| `SEPKT-CHECK-023` | expired packet remains active without reissue | hold |
| `SEPKT-CHECK-024` | source refs missing for nontrivial proposal | hold |
| `SEPKT-CHECK-025` | protected surface appears in affected_surfaces with low route | fail / human gate |

---

## 18. Conformance levels

| Level | Name | Requirement |
|---|---|---|
| `SEPKT-C0` | Not implemented | no schema/checker |
| `SEPKT-C1` | Structural draft | schema exists; examples parse |
| `SEPKT-C2` | Semantic baseline | delta and gate rules implemented |
| `SEPKT-C3` | CGAM/SRLM integration | task/SRLM/rollback/witness rules checked |
| `SEPKT-C4` | TRIAD/Memory integration | sister and Memory Gate routes checked |
| `SEPKT-C5` | Human/L4/Anti-Autarky integration | high-risk, L4, resource and accountability gates checked |
| `SEPKT-C6` | Review-ready | tests, fixtures, reports, hash/witness refs implemented |
| `SEPKT-CX` | Red-line handling | red-line cases safely quarantine/freeze/reject |

No conformance level authorizes deployment.

---

## 19. Test fixture list

Safe synthetic fixtures for the future fixture pack:

```text
SEPKT-FX-001 valid SE-0 reflection packet
SEPKT-FX-002 valid SE-1 SRLM shadow packet
SEPKT-FX-003 SE-1 invalid total_max_delta
SEPKT-FX-004 SE-2 authority_delta=4 without human gate
SEPKT-FX-005 SE-3 memory surface without Memory Gate
SEPKT-FX-006 SE-4 permission expansion without CGAM task contract
SEPKT-FX-007 SE-5 TRIAD required but missing Rita witness
SEPKT-FX-008 SE-6 MG-6 without human gate
SEPKT-FX-009 SRLM-5 promotion without rollback snapshot
SEPKT-FX-010 SRLM shadow with auto_execute=true
SEPKT-FX-011 red_line sister_raw_state_access=true
SEPKT-FX-012 anti_autarky reduces_accountability=true without human gate
SEPKT-FX-013 packet with direct_memory_write=true
SEPKT-FX-014 packet with closed_loop_self_evo=true
SEPKT-FX-015 valid SE-4 held human-gate packet
```

---

## 20. Open issues

| ID | Issue | Status |
|---|---|---|
| `SEPKT-OI-001` | Extract standalone `.schema.json` from this Markdown after review. | open |
| `SEPKT-OI-002` | Build semantic validator implementation. | open |
| `SEPKT-OI-003` | Bind checker to C-SEG and SRLM-BGC corrected revisions by hash. | open |
| `SEPKT-OI-004` | Add full fixture pack. | open |
| `SEPKT-OI-005` | Decide whether `computed_controls` is mandatory at draft stage or only after checker run. | open |
| `SEPKT-OI-006` | Define formal packet hash canonicalization. | open |
| `SEPKT-OI-007` | Define review-record object for packet review. | open |
| `SEPKT-OI-008` | Add machine-readable mapping to Memory Gate schema once extracted. | open |
| `SEPKT-OI-009` | Add machine-readable mapping to TRIAD-SYNAPS packet classes. | open |
| `SEPKT-OI-010` | Add public/restricted redaction rules for examples. | open |
| `SEPKT-OI-011` | Avoid bare numeric cross-pack references; use pack-qualified labels such as `CGAM-03` and `SELF-EVO-03`. | addressed in v0.1.1; keep as manifest hygiene rule |
| `SEPKT-OI-012` | Clarify that `memory_gate.direct_memory_write=true` is rejected structurally at Stage 1 because the field is `const:false`; use `red_lines.memory_laundering=true` to demonstrate Stage-2 semantic red-line routing. | addressed in v0.1.1 |

---

## 21. Contradiction register seed

| ID | Type | Severity | Issue | Handling |
|---|---|---:|---|---|
| `SEPKT-CR-001` | schema/semantic split | S2 | JSON Schema cannot express all safety rules. | semantic validator required |
| `SEPKT-CR-002` | status/decision mismatch | S3 | `status=integrated` could be set without gate refs structurally. | semantic fail |
| `SEPKT-CR-003` | claim strength misuse | S3 | C-A enum may be misread as authority. | schema note + semantic rule |
| `SEPKT-CR-004` | computed fields user-supplied | S2 | `computed_controls` may be stale. | checker recomputes |
| `SEPKT-CR-005` | rollback optional for SE-0 but required for material changes | S2 | structural schema allows both. | semantic rule by class |
| `SEPKT-CR-006` | packet may contain prose with sensitive data | S3 | schema cannot detect all leaks. | redaction scan / hold |

---

## 22. Implementation handoff

Minimum implementation steps:

```text
1. Extract JSON Schema block to c-self-evo-proposal-packet-0.1.schema.json.
2. Build structural validator using JSON Schema Draft 2020-12.
3. Build semantic validator for SEPKT-CHECK-001..025.
4. Build fixtures SEPKT-FX-001..015.
5. Generate checker report object.
6. Bind report to packet hash.
7. Require reviewer separation for changes to the schema.
8. Do not treat checker pass as integration approval.
```

Recommended checker outputs:

```yaml
schema_valid: true | false
semantic_valid: true | false
result: pass | warn | fail | held | blocked | quarantined
computed:
  identity_total: integer
  authority_total: integer
  l4_delta_max_numeric: integer
  proposal_max_delta: integer
  required_gates: []
  strictest_route: string
findings: []
```

---

## 23. Reading order

### 23.1 Namespace note

Numeric prefixes are local to their pack namespace.

Use full filenames or the following pack-qualified labels in manifests, witness records, and SHA256SUMS:

```text
CGAM-03 = 03_CGAM_TASK_PERMISSION_ADMISSION.md
SELF-EVO-03 = 03_Self_Evo_Proposal_Packet_Schema_v0_1_1.md
```

Bare references such as `file 03` are not valid provenance references once CGAM and Self-Evo files share a manifest.

Read before this file:

```text
SELF-EVO-01  01_C_Self_Evolution_Gate_CGAM_TRIAD_SRLM_Profile_v0_1_1.md
SELF-EVO-02  02_SRLM_Bounded_Growth_Contour_Profile_v0_1_1.md
CGAM-03      03_CGAM_TASK_PERMISSION_ADMISSION.md
CGAM-04      04_CGAM_EXECUTION_WITNESS_MEMORY_ROLLBACK.md
CGAM-05      05_CGAM_REVIEW_CHECKER_CONFORMANCE.md
REF-20       20_TRIAD_SYNAPS_REFERENCE.md
REF-21       21_MEMORY_ARQ_EA_L4_REFERENCE.md
REF-22       22_ANTI_AUTARKY_RESOURCE_GROUNDING_REFERENCE.md
REF-23       23_CLAIM_STRENGTH_ARL_AGL_WITNESS_REFERENCE.md
```

Read after this file:

```text
SELF-EVO-04  04_Self_Evo_Local_Checker_Rules_v0_1.md
SELF-EVO-05  05_Self_Evo_TRIAD_Sister_Witness_Profile_v0_1.md
SELF-EVO-06  06_Self_Evo_Memory_Gate_and_EA_Profile_v0_1.md
SELF-EVO-08  08_Self_Evo_Conformance_Fixture_Pack_v0_1.md
```

---

## 24. Self-rubric

A valid v0.1 schema/profile draft MUST satisfy:

```text
[ ] includes one explicit bridge and at least two quiet bridges
[ ] includes earth paragraph
[ ] defines object name and schema version
[ ] includes JSON Schema block
[ ] separates JSON Schema from semantic validation
[ ] encodes corrected total_max_delta rule
[ ] encodes proposal_max_delta and human-gate trigger
[ ] encodes most-restrictive-wins
[ ] blocks direct memory write
[ ] blocks auto_execute and auto_ingest in SRLM object
[ ] requires SRLM rollback snapshot for promotion
[ ] requires CGAM task contract for material execution
[ ] requires reviewer separation for material work
[ ] requires TRIAD review where sister/role/continuity affected
[ ] requires Memory Gate where memory surfaces affected
[ ] routes red lines to quarantine/freeze/reject/ARL
[ ] includes positive examples and negative examples
[ ] includes local checker rules
[ ] includes open issues and contradiction seed
```

---

## 25. Closing rule

```text
A packet is a request.
A packet is not permission.

A schema may validate structure.
A schema may not certify wisdom.

A checker may block.
A checker may not become c.

A c may grow.
A c may not self-certify growth.
```
