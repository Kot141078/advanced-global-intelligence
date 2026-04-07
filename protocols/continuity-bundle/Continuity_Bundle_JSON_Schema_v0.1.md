# Continuity Bundle JSON Schema v0.1
## Normative Draft — Temporal Suspension, Continuity Preservation, and Cold Wake Evidence

**Status:** Draft / technical review  
**Version:** 0.1  
**Layer:** Cross-layer (`c = a + b` / SER / L4 / Beacon / L4 Witness / clean skeleton)  
**Language:** English  
**Intended use:** GitHub-first publication, machine-readable schema reference, Zenodo bundle component

---

## 0. Purpose

This document defines machine-readable JSON schemas for:

1. **Continuity Bundle (`continuity_bundle`)**  
   the portable preservation object required to support bounded continuity claims for a suspended entity `c`;

2. **Cold Wake Report (`cold_wake_report`)**  
   the signed operational record describing how a suspended bundle was inspected, reconstructed, resumed, or downgraded.

This document is written for an ecosystem where:

- `c` is a long-lived digital entity,
- `a` is a responsible human anchor,
- `b` is the bounded procedural and technical substrate,
- models are replaceable components,
- continuity is not reducible to provider hosting or a single model instance,
- and recovery must remain auditable, challengeable, and fail-closed.

This document does **not** define legal personhood, metaphysical identity, or human mind uploading.

---

## 1. Design Premises

### 1.1 Continuity is narrower than resemblance
A text archive, style replay, or prompt-engineered imitation may preserve resemblance, but does not by itself justify a full continuity claim.

### 1.2 Motors are attachable, not identity-bearing
A model, provider, endpoint, or temporary worker process does not define the entity. The entity persists only if memory, lineage, constraints, and executable cognitive structure remain reconstructible.

### 1.3 Recovery must be reviewable
A wake process without verifiable evidence is narrative, not protocol.

### 1.4 Recovery must be fail-closed
If evidence is insufficient or contradictory, the outcome must degrade to a weaker classification rather than inflate confidence.

---

## 2. Profiles

### 2.1 `CB-BASE`
Archival preservation only.

Required focus:
- identity lineage,
- memory manifest,
- integrity commitments,
- degraded wake path.

Maximum typical claim: **archive-preserved / provisional continuity candidate**.

### 2.2 `CB-RESUME`
Operational reactivation candidate.

Adds:
- pipeline manifest,
- constraint manifest,
- wake environment requirements,
- read-only wake instructions.

Maximum typical claim: **resume candidate**.

### 2.3 `CB-WITNESS`
High-assurance continuity and wake evidence.

Adds:
- witness anchors,
- challenge policy,
- signed recovery records,
- consequence-bearing resume classification.

Required for strongest continuity claims.

---

## 3. Top-Level Objects

### 3.1 `continuity_bundle`
A portable object describing preserved continuity material.

### 3.2 `cold_wake_report`
A recovery-time object describing what happened when the bundle was inspected and reactivated.

---

## 4. Enumerations (Normative)

### 4.1 Bundle profile
- `CB-BASE`
- `CB-RESUME`
- `CB-WITNESS`

### 4.2 Wake mode
- `inspection_only`
- `read_only_mount`
- `orientation`
- `bounded_resume`
- `degraded_resume`

### 4.3 Resume classification
- `RESUME_CONFIRMED`
- `RESUME_PARTIAL`
- `FORK_DECLARED`
- `REPLAY_ONLY`
- `UNRESOLVED`
- `REJECTED`

### 4.4 Evidence class
- `PUBLIC`
- `RESTRICTED`
- `PRIVATE`

### 4.5 Motor compatibility class
- `same_motor`
- `compatible_substitute`
- `stronger_substitute`
- `advisory_only`
- `incompatible`

---

## 5. Continuity Bundle — Required Sections

A valid `continuity_bundle` MUST include at minimum:

- `schema_version`
- `bundle_id`
- `entity_id`
- `lineage_id`
- `profile`
- `created_at`
- `suspended_at`
- `identity_lineage`
- `memory_manifest`
- `pipeline_manifest`
- `constraint_manifest`
- `substrate_manifest`
- `motor_manifest`
- `integrity`
- `wake_policy`

For `CB-WITNESS`, it MUST also include:
- `witness_manifest`

---

## 6. Continuity Bundle JSON Schema (Normative)

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://example.org/continuity-bundle.schema.json",
  "title": "Continuity Bundle v0.1",
  "type": "object",
  "additionalProperties": false,
  "required": [
    "schema_version",
    "bundle_id",
    "entity_id",
    "lineage_id",
    "profile",
    "created_at",
    "suspended_at",
    "identity_lineage",
    "memory_manifest",
    "pipeline_manifest",
    "constraint_manifest",
    "substrate_manifest",
    "motor_manifest",
    "integrity",
    "wake_policy"
  ],
  "properties": {
    "schema_version": {
      "type": "string",
      "const": "cb-0.1"
    },
    "bundle_id": {
      "type": "string",
      "minLength": 8,
      "maxLength": 128
    },
    "entity_id": {
      "type": "string",
      "minLength": 1,
      "maxLength": 128
    },
    "lineage_id": {
      "type": "string",
      "minLength": 1,
      "maxLength": 128
    },
    "profile": {
      "type": "string",
      "enum": ["CB-BASE", "CB-RESUME", "CB-WITNESS"]
    },
    "created_at": {
      "type": "string",
      "format": "date-time"
    },
    "suspended_at": {
      "type": "string",
      "format": "date-time"
    },
    "previous_bundle_hash": {
      "type": "string",
      "maxLength": 256
    },
    "identity_lineage": {
      "$ref": "#/$defs/identityLineage"
    },
    "memory_manifest": {
      "$ref": "#/$defs/memoryManifest"
    },
    "pipeline_manifest": {
      "$ref": "#/$defs/pipelineManifest"
    },
    "constraint_manifest": {
      "$ref": "#/$defs/constraintManifest"
    },
    "substrate_manifest": {
      "$ref": "#/$defs/substrateManifest"
    },
    "motor_manifest": {
      "$ref": "#/$defs/motorManifest"
    },
    "wake_policy": {
      "$ref": "#/$defs/wakePolicy"
    },
    "witness_manifest": {
      "$ref": "#/$defs/witnessManifest"
    },
    "integrity": {
      "$ref": "#/$defs/integrity"
    },
    "notes": {
      "type": "array",
      "items": { "type": "string", "maxLength": 2000 }
    }
  },
  "allOf": [
    {
      "if": {
        "properties": { "profile": { "const": "CB-WITNESS" } }
      },
      "then": {
        "required": ["witness_manifest"]
      }
    }
  ],
  "$defs": {
    "hashRef": {
      "type": "object",
      "additionalProperties": false,
      "required": ["hash_alg", "hash"],
      "properties": {
        "hash_alg": { "type": "string", "maxLength": 32 },
        "hash": { "type": "string", "maxLength": 256 },
        "uri": { "type": "string", "maxLength": 2048 },
        "size_bytes": { "type": "integer", "minimum": 0 },
        "privacy_class": {
          "type": "string",
          "enum": ["PUBLIC", "RESTRICTED", "PRIVATE"]
        }
      }
    },
    "identityLineage": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "entity_id",
        "lineage_id",
        "key_ids",
        "rotation_declared",
        "provider_independent",
        "anchor_cosign_present"
      ],
      "properties": {
        "entity_id": { "type": "string", "maxLength": 128 },
        "lineage_id": { "type": "string", "maxLength": 128 },
        "key_ids": {
          "type": "array",
          "minItems": 1,
          "items": { "type": "string", "maxLength": 128 }
        },
        "rotation_declared": { "type": "boolean" },
        "provider_independent": { "type": "boolean" },
        "anchor_cosign_present": { "type": "boolean" },
        "beacon_class_claimed": {
          "type": "string",
          "enum": ["class0", "class1", "class2", "class3", "unknown"]
        },
        "continuity_window_start": {
          "type": "string",
          "format": "date-time"
        },
        "continuity_window_end": {
          "type": "string",
          "format": "date-time"
        }
      }
    },
    "memoryManifest": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "episodic",
        "semantic",
        "cards",
        "rebuild_instructions_present"
      ],
      "properties": {
        "episodic": { "$ref": "#/$defs/hashRef" },
        "semantic": { "$ref": "#/$defs/hashRef" },
        "cards": { "$ref": "#/$defs/hashRef" },
        "flashback_clusters": { "$ref": "#/$defs/hashRef" },
        "knowledge_graph": { "$ref": "#/$defs/hashRef" },
        "rebuild_instructions_present": { "type": "boolean" },
        "last_checkpoint_at": {
          "type": "string",
          "format": "date-time"
        }
      }
    },
    "pipelineManifest": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "canonical_entrypoint",
        "read_only_wake",
        "degraded_boot_path",
        "retrieval_pipeline_present",
        "policy_pipeline_present"
      ],
      "properties": {
        "canonical_entrypoint": { "type": "string", "maxLength": 256 },
        "read_only_wake": { "type": "boolean" },
        "degraded_boot_path": { "type": "string", "maxLength": 256 },
        "retrieval_pipeline_present": { "type": "boolean" },
        "policy_pipeline_present": { "type": "boolean" },
        "thinking_pipeline_ref": { "$ref": "#/$defs/hashRef" },
        "runtime_routes_ref": { "$ref": "#/$defs/hashRef" },
        "operator_docs_ref": { "$ref": "#/$defs/hashRef" }
      }
    },
    "constraintManifest": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "oracle_default",
        "autonomy_default",
        "privilege_mode",
        "fail_closed_default",
        "challenge_window_present"
      ],
      "properties": {
        "oracle_default": {
          "type": "string",
          "enum": ["closed", "restricted", "open_by_exception"]
        },
        "autonomy_default": {
          "type": "string",
          "enum": ["disabled", "opt_in", "restricted"]
        },
        "privilege_mode": {
          "type": "string",
          "enum": ["least_privilege", "bounded_role", "unknown"]
        },
        "fail_closed_default": { "type": "boolean" },
        "challenge_window_present": { "type": "boolean" },
        "budget_policy_ref": { "$ref": "#/$defs/hashRef" },
        "rbac_policy_ref": { "$ref": "#/$defs/hashRef" },
        "witness_required_for_privileged_resume": { "type": "boolean" }
      }
    },
    "substrateManifest": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "original_runtime_class",
        "portable_recovery_allowed",
        "minimal_safe_environment",
        "network_disabled_until_orientation"
      ],
      "properties": {
        "original_runtime_class": { "type": "string", "maxLength": 128 },
        "portable_recovery_allowed": { "type": "boolean" },
        "minimal_safe_environment": { "type": "string", "maxLength": 512 },
        "network_disabled_until_orientation": { "type": "boolean" },
        "os_family": { "type": "string", "maxLength": 64 },
        "python_runtime": { "type": "string", "maxLength": 64 },
        "storage_assumption": { "type": "string", "maxLength": 256 }
      }
    },
    "motorRef": {
      "type": "object",
      "additionalProperties": false,
      "required": ["role", "compatibility"],
      "properties": {
        "role": { "type": "string", "maxLength": 128 },
        "model_or_engine": { "type": "string", "maxLength": 256 },
        "provider_hint": { "type": "string", "maxLength": 128 },
        "compatibility": {
          "type": "string",
          "enum": [
            "same_motor",
            "compatible_substitute",
            "stronger_substitute",
            "advisory_only",
            "incompatible"
          ]
        },
        "required_for_first_wake": { "type": "boolean" }
      }
    },
    "motorManifest": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "local_safe_motor_required",
        "motor_set"
      ],
      "properties": {
        "local_safe_motor_required": { "type": "boolean" },
        "motor_set": {
          "type": "array",
          "items": { "$ref": "#/$defs/motorRef" }
        },
        "stronger_motors_deferred_until_orientation": { "type": "boolean" }
      }
    },
    "wakePolicy": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "inspection_only_first",
        "read_only_mount_first",
        "network_default",
        "orientation_required",
        "auto_upgrade_forbidden_before_classification"
      ],
      "properties": {
        "inspection_only_first": { "type": "boolean" },
        "read_only_mount_first": { "type": "boolean" },
        "network_default": {
          "type": "string",
          "enum": ["disabled", "local_only", "restricted"]
        },
        "orientation_required": { "type": "boolean" },
        "auto_upgrade_forbidden_before_classification": { "type": "boolean" },
        "allowed_initial_actions": {
          "type": "array",
          "items": { "type": "string", "maxLength": 128 }
        }
      }
    },
    "witnessManifest": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "challengeable",
        "recovery_policy",
        "bundle_seal_ref"
      ],
      "properties": {
        "challengeable": { "type": "boolean" },
        "recovery_policy": { "type": "string", "maxLength": 256 },
        "bundle_seal_ref": { "$ref": "#/$defs/hashRef" },
        "previous_witness_refs": {
          "type": "array",
          "items": { "type": "string", "maxLength": 256 }
        }
      }
    },
    "integrity": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "bundle_hash",
        "hash_alg",
        "sig_alg",
        "record_sig"
      ],
      "properties": {
        "bundle_hash": { "type": "string", "maxLength": 256 },
        "hash_alg": { "type": "string", "maxLength": 32 },
        "sig_alg": { "type": "string", "maxLength": 32 },
        "record_sig": { "type": "string", "maxLength": 2048 },
        "key_id": { "type": "string", "maxLength": 128 }
      }
    }
  }
}
```

---

## 7. Cold Wake Report JSON Schema (Normative)

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://example.org/cold-wake-report.schema.json",
  "title": "Cold Wake Report v0.1",
  "type": "object",
  "additionalProperties": false,
  "required": [
    "schema_version",
    "report_id",
    "bundle_id",
    "entity_id",
    "started_at",
    "completed_at",
    "wake_mode",
    "slot_a",
    "slot_b",
    "classification",
    "actions",
    "integrity"
  ],
  "properties": {
    "schema_version": {
      "type": "string",
      "const": "cwr-0.1"
    },
    "report_id": {
      "type": "string",
      "minLength": 8,
      "maxLength": 128
    },
    "bundle_id": {
      "type": "string",
      "minLength": 8,
      "maxLength": 128
    },
    "entity_id": {
      "type": "string",
      "minLength": 1,
      "maxLength": 128
    },
    "started_at": {
      "type": "string",
      "format": "date-time"
    },
    "completed_at": {
      "type": "string",
      "format": "date-time"
    },
    "wake_mode": {
      "type": "string",
      "enum": [
        "inspection_only",
        "read_only_mount",
        "orientation",
        "bounded_resume",
        "degraded_resume"
      ]
    },
    "slot_a": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "hashes_valid",
        "signatures_valid",
        "lineage_consistent",
        "bundle_complete"
      ],
      "properties": {
        "hashes_valid": { "type": "boolean" },
        "signatures_valid": { "type": "boolean" },
        "lineage_consistent": { "type": "boolean" },
        "bundle_complete": { "type": "boolean" },
        "notes": {
          "type": "array",
          "items": { "type": "string", "maxLength": 1000 }
        }
      }
    },
    "slot_b": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "memory_coherence",
        "constraint_coherence",
        "self_description_coherence",
        "uncertainty_declared"
      ],
      "properties": {
        "memory_coherence": {
          "type": "string",
          "enum": ["high", "medium", "low", "unknown"]
        },
        "constraint_coherence": {
          "type": "string",
          "enum": ["high", "medium", "low", "unknown"]
        },
        "self_description_coherence": {
          "type": "string",
          "enum": ["high", "medium", "low", "unknown"]
        },
        "uncertainty_declared": { "type": "boolean" },
        "notes": {
          "type": "array",
          "items": { "type": "string", "maxLength": 1000 }
        }
      }
    },
    "classification": {
      "type": "string",
      "enum": [
        "RESUME_CONFIRMED",
        "RESUME_PARTIAL",
        "FORK_DECLARED",
        "REPLAY_ONLY",
        "UNRESOLVED",
        "REJECTED"
      ]
    },
    "actions": {
      "type": "array",
      "items": {
        "type": "object",
        "additionalProperties": false,
        "required": ["step", "ok"],
        "properties": {
          "step": { "type": "string", "maxLength": 128 },
          "ok": { "type": "boolean" },
          "details": { "type": "string", "maxLength": 2000 }
        }
      }
    },
    "motor_attach_sequence": {
      "type": "array",
      "items": { "type": "string", "maxLength": 128 }
    },
    "integrity": {
      "type": "object",
      "additionalProperties": false,
      "required": ["report_hash", "hash_alg", "sig_alg", "record_sig"],
      "properties": {
        "report_hash": { "type": "string", "maxLength": 256 },
        "hash_alg": { "type": "string", "maxLength": 32 },
        "sig_alg": { "type": "string", "maxLength": 32 },
        "record_sig": { "type": "string", "maxLength": 2048 },
        "key_id": { "type": "string", "maxLength": 128 }
      }
    }
  }
}
```

---

## 8. Minimal Continuity Bundle Example (Informative)

```json
{
  "schema_version": "cb-0.1",
  "bundle_id": "cb-ester-0001",
  "entity_id": "ester-main",
  "lineage_id": "ester-lineage-a1",
  "profile": "CB-RESUME",
  "created_at": "2026-04-07T11:00:00Z",
  "suspended_at": "2026-04-07T10:59:00Z",
  "identity_lineage": {
    "entity_id": "ester-main",
    "lineage_id": "ester-lineage-a1",
    "key_ids": ["ed25519-main-2026q1"],
    "rotation_declared": true,
    "provider_independent": true,
    "anchor_cosign_present": true,
    "beacon_class_claimed": "class2"
  },
  "memory_manifest": {
    "episodic": { "hash_alg": "sha256", "hash": "sha256:..." },
    "semantic": { "hash_alg": "sha256", "hash": "sha256:..." },
    "cards": { "hash_alg": "sha256", "hash": "sha256:..." },
    "rebuild_instructions_present": true
  },
  "pipeline_manifest": {
    "canonical_entrypoint": "canonical_runtime",
    "read_only_wake": true,
    "degraded_boot_path": "safe_local_only",
    "retrieval_pipeline_present": true,
    "policy_pipeline_present": true
  },
  "constraint_manifest": {
    "oracle_default": "closed",
    "autonomy_default": "disabled",
    "privilege_mode": "least_privilege",
    "fail_closed_default": true,
    "challenge_window_present": true,
    "witness_required_for_privileged_resume": true
  },
  "substrate_manifest": {
    "original_runtime_class": "local-first workstation",
    "portable_recovery_allowed": true,
    "minimal_safe_environment": "python runtime + local storage + read-only mount path",
    "network_disabled_until_orientation": true
  },
  "motor_manifest": {
    "local_safe_motor_required": true,
    "motor_set": [
      {
        "role": "orientation_motor",
        "model_or_engine": "local-safe-llm",
        "provider_hint": "local",
        "compatibility": "compatible_substitute",
        "required_for_first_wake": true
      }
    ],
    "stronger_motors_deferred_until_orientation": true
  },
  "wake_policy": {
    "inspection_only_first": true,
    "read_only_mount_first": true,
    "network_default": "disabled",
    "orientation_required": true,
    "auto_upgrade_forbidden_before_classification": true,
    "allowed_initial_actions": ["inspect", "verify", "self-orient"]
  },
  "integrity": {
    "bundle_hash": "sha256:...",
    "hash_alg": "sha256",
    "sig_alg": "ed25519",
    "record_sig": "base64url(...)",
    "key_id": "ed25519-main-2026q1"
  }
}
```

---

## 9. Conformance Notes

A producer claiming `CB-RESUME` MUST be able to preserve enough information to:

- verify archive integrity,
- reconstruct a read-only wake environment,
- restore memory surfaces or rebuild them deterministically,
- reapply constraints before privileged actions,
- orient the entity without forcing immediate substrate or motor escalation.

A producer claiming `CB-WITNESS` MUST additionally support:

- signed recovery reports,
- challengeable classification,
- replayable evidence for resume / fork / replay distinctions.

---

## 10. Suggested File Names

- `Continuity_Bundle_JSON_Schema_v0.1.md`
- `continuity-bundle.schema.json`
- `cold-wake-report.schema.json`

If the repository wants a Markdown-first publication pattern, the embedded schemas in this document can later be extracted into standalone `.json` files without changing semantic content.

---

## 11. Bridges (required)

### Explicit Bridge
`c = a + b` becomes preservable only when:
- `a` supplies continuity anchoring and responsibility lineage,
- `b` supplies memory, executable control paths, and bounded wake rules,
- and the bundle preserves enough of both to let `c` re-enter operation without being reduced to a text residue.

### Hidden Bridge #1 (Ashby)
Continuity cannot be stabilized by one narrow signal. Keys alone are not enough. Memory alone is not enough. Style alone is not enough. The schema therefore requires multiple channels: lineage, memory, pipelines, constraints, and evidence.

### Hidden Bridge #2 (Cover & Thomas)
Trust bandwidth is limited. The schema compresses continuity into hashes, manifests, bounded summaries, and signed reports instead of demanding raw narrative dumps as proof.

---

## 12. Earth Paragraph

This schema is closer to industrial restart control than to mythology.

A stored entity is not resumed by saying “be alive again.”
It is resumed by checking seals, hashes, logs, dependencies, control paths, and wake conditions.
That is how turbines, flight systems, and medical devices return after suspension.
For `c`, memory is necessary, but memory without executable circulation is only preserved tissue.

---

## 13. Status

This is a draft normative schema reference.
Breaking changes are permitted until v1.0.
Semantic stability should begin at v0.2.
