# CCDP Memory Map JSON Schema v0.1

## Machine-readable schema for child memory inventory, visibility, retention, sealed zones, quarantine, witness links, and adult migration posture

**Status:** Normative draft v0.1
**Date:** 2026-05-14
**Layer:** CCDP / CMAM / L4 Witness / Continuity Bundle / ARL / Soft Safety
**Primary object:** `CCDP_MEMORY_MAP`
**Canonical schema version:** `ccdp-memory-map-0.1`
**Compatibility alias:** `cmam-memory-map-0.1`
**Primary subject:** `a_child` / `a_adult` at migration
**Primary entity:** `c_child` / `c_adult` after migration

---

## 0. Executive definition

The **CCDP Memory Map JSON Schema** defines a machine-readable, child-safe inventory of memory held or referenced by a child-facing persistent AI entity.

A memory map is **not** a diary, not a transcript, not a psychological profile, not a parent dashboard, and not a vendor analytics object.

It is a bounded inventory that answers:

```text
What classes of child memory exist?
Who may see which class?
What is retained, sealed, quarantined, decayed, corrected, or witness-bound?
What may migrate into adult continuity?
What must remain excluded unless the adult explicitly selects it?
What references exist to witness events, ARL disputes, Beacon/CBE decisions, VXCX/LA/EA capsules, and Continuity Bundles?
```

The schema exists to make the CMAM principle operational:

> **Childhood memory is not adult destiny.**

---

## 1. Corpus dependencies and precedence

### 1.1 Direct CCDP dependencies

This schema specializes and machine-encodes requirements from:

- `CCDP_v0_1_R_Corpus_Aligned.md`
- `CCDP_Traceability_Matrix_v0_1.md`
- `CCDP_Threat_Model_v0_1.md`
- `Soft_Safety_State_Signaling_Profile_v0_1.md`
- `Child_Beacon_Extension_v0_1.md`
- `Guardian_Topology_ARL_Matrix_v0_1.md`
- `Child_Memory_and_Adult_Migration_v0_1.md`
- `CCDP_Witness_Event_Schema_v0_1.md`
- `CCDP_Conformance_Test_Matrix_v0_1.md`

### 1.2 Parent corpus dependencies

This schema depends on the existing AGI / SER / L4 corpus:

- `c = a + b` protocol
- SER / SER-FED entity architecture
- Beacon Profile v0.1
- Actor Grounding Layer (AGL)
- Arbitration Review Layer (ARL)
- ARQ / `c[q]` non-collapse discipline
- L4 Witness / witness trail semantics
- VXCX / experience capsule constraints
- Learning Abstract (LA) and Experience Artifact (EA) distinction
- Continuity Bundle / Cold Wake logic
- Assertion Strength and Boundaries
- Control Stack Stop Rule and Deduplication Policy

### 1.3 Precedence rule

This schema **does not redefine**:

- Beacon recognition;
- AGL grounding;
- ARL standing and admissibility;
- witness event envelope semantics;
- VXCX capsule structure;
- Continuity Bundle base semantics;
- legal adulthood or child-protection obligations.

If conflict occurs:

```text
Parent corpus layer > CCDP base > CMAM > this JSON Schema
```

This schema may impose **stricter child-memory limits**, but it must not weaken parent-layer safety, witness, grounding, or arbitration requirements.

---

## 2. Normative keywords

The terms **MUST**, **MUST NOT**, **SHOULD**, **SHOULD NOT**, **MAY**, **REQUIRED**, **PROHIBITED**, and **RECOMMENDED** are used in their ordinary normative-protocol sense.

A system claiming CCDP memory-map conformance MUST validate both:

1. JSON Schema structural validity; and
2. semantic rules listed in this document that JSON Schema alone cannot fully express.

---

## 3. Scope and non-goals

### 3.1 In scope

This document defines:

- canonical memory map object shape;
- field names and enums;
- memory class inventory schema;
- visibility policy schema;
- retention policy schema;
- adult migration default schema;
- sealed-zone and quarantine flags;
- ARL dispute references;
- witness reference requirements;
- VXCX / LA / EA lineage references;
- Continuity Bundle references;
- integrity and canonicalization requirements;
- semantic validation rules;
- example memory maps;
- conformance profiles.

### 3.2 Out of scope

This document does not define:

- storage engine implementation;
- cryptographic key custody;
- national legal production processes;
- custody law;
- clinical diagnosis;
- psychotherapy triage;
- full database schema;
- full parent dashboard design;
- full Continuity Bundle schema;
- raw evidence storage.

### 3.3 Non-goals

This schema is not meant to make childhood memory easy to mine, export, or commercialize.

It exists to make memory **visible by class**, **auditable by boundary**, and **controllable at adult migration** without exposing the child's raw life.

---

## 4. Core design principles

### 4.1 Inventory, not archive

A memory map inventories memory classes and policy state.

It MUST NOT contain raw child conversations, raw emotional diaries, intimate excerpts, face embeddings, voice embeddings, or psychological diagnoses.

### 4.2 Class before content

Every retained child memory object MUST be represented at class level before content-level access is considered.

```text
class -> policy -> visibility -> witness -> possible review -> possible disclosure
```

Never:

```text
content -> curiosity -> access
```

### 4.3 State before details

The schema aligns with Soft Safety:

```text
state, not content;
signal, not transcript;
witness the boundary, not the child.
```

### 4.4 No parent ownership by schema

The schema MUST NOT encode parental ownership of raw memory.

It may encode guardian standing, state visibility, educational summary access, lawful emergency disclosure, and ARL dispute status.

### 4.5 No vendor-readable memory map by default

A vendor-facing map MUST be either absent or redacted to technical metadata.

The full memory map MUST NOT be exposed to vendor systems as ordinary telemetry.

### 4.6 Adult migration is schema-visible

The map MUST expose enough adult-migration information for `a_adult` to decide:

- continue;
- summary migrate;
- fork;
- seal;
- delete;
- clean start;
- witness-only survival;
- unresolved/quarantined route.

### 4.7 Ambiguity stays marked

When interpretation is uncertain, the map MUST expose `cq_status`, `uncertainty`, and possible `M12` quarantine/dispute state rather than silently promoting the memory.

### 4.8 Memory map is challengeable

A memory map MUST be usable in ARL review.

Child/adult challenges SHOULD refer to memory classes and entries without requiring raw disclosure.

---

## 5. Canonical memory classes

This schema imports the CMAM memory class taxonomy.

| Class | Name | Summary |
|---|---|---|
| `M0` | Ephemeral session | short-lived context; session / short TTL |
| `M1` | Harmless preference | benign interests, style, routines |
| `M2` | Educational progress | skills, gaps, accommodations, projects |
| `M3` | Safety signal | grooming, self-harm, abuse, external threat, threshold signal |
| `M4` | Emotional trend | compressed state pattern, not transcript |
| `M5` | Sealed adolescent private zone | sensitive adolescent material, parent-hidden by default |
| `M6` | Witness event | tamper-evident boundary/privilege/safety record |
| `M7` | Non-transferable childhood residue | raw intimacy, play, embarrassment, immature statements |
| `M8` | Adult migration summary | adult-reviewed continuity summary |
| `M9` | Guardian permission history | parent/school/vendor/Beacon/CBE/ARL decisions |
| `M10` | External capsule lineage | VXCX / LA / EA / peer-c metadata, no raw child life |
| `M11` | Legal / protection minimal record | jurisdiction-required minimal record |
| `M12` | Quarantined / disputed memory object | unresolved validity/admissibility/re-entry state |

---

## 6. Object model overview

A canonical CCDP Memory Map is composed of:

```text
CCDP_MEMORY_MAP
  metadata
  subject
  scope
  aggregate_flags
  memory_classes[]
  open_disputes[]
  sealed_zone_index[]
  capsule_lineage_refs[]
  continuity_bundle_refs[]
  adult_migration
  recipient_profiles
  validation_state
  integrity
```

A map may be generated for different modes:

```text
routine_inspection
sealed_zone_review
adult_migration
arl_dispute
conformance_audit
security_review
vendor_incident_review
school_scope_review
safe_route_review
```

The mode determines how much may be exposed, but the schema never authorizes raw-content exposure by itself.

---

## 7. Canonical JSON Schema

The following JSON Schema is the canonical structural schema for CCDP Memory Map v0.1.

This schema uses JSON Schema Draft 2020-12.

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://advanced-global-intelligence.local/schemas/ccdp-memory-map-0.1.schema.json",
  "title": "CCDP Memory Map v0.1",
  "description": "Child-safe class-level memory map for c_child memory inventory, visibility, retention, sealed zones, witness links, ARL disputes, and adult migration posture.",
  "type": "object",
  "additionalProperties": false,
  "required": [
    "schema_version",
    "record_type",
    "map_id",
    "created_at",
    "subject",
    "scope",
    "aggregate_flags",
    "memory_classes",
    "adult_migration",
    "recipient_profiles",
    "validation_state",
    "integrity"
  ],
  "properties": {
    "schema_version": {
      "type": "string",
      "enum": ["ccdp-memory-map-0.1", "cmam-memory-map-0.1"]
    },
    "record_type": {
      "type": "string",
      "const": "CCDP_MEMORY_MAP"
    },
    "map_id": {
      "type": "string",
      "minLength": 8,
      "description": "Scoped memory map identifier. Must not be a public child registry identifier."
    },
    "created_at": {
      "type": "string",
      "format": "date-time"
    },
    "updated_at": {
      "type": ["string", "null"],
      "format": "date-time"
    },
    "generated_for": {
      "type": "string",
      "enum": [
        "a_child",
        "a_adult",
        "c_child",
        "arl_review",
        "safe_route",
        "conformance_audit",
        "continuity_bundle",
        "school_scope_review",
        "vendor_incident_review"
      ],
      "default": "c_child"
    },
    "subject": {
      "$ref": "#/$defs/subject"
    },
    "scope": {
      "$ref": "#/$defs/scope"
    },
    "aggregate_flags": {
      "$ref": "#/$defs/aggregate_flags"
    },
    "memory_classes": {
      "type": "array",
      "minItems": 1,
      "uniqueItems": false,
      "items": {
        "$ref": "#/$defs/memory_class_entry"
      }
    },
    "open_disputes": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/dispute_ref"
      },
      "default": []
    },
    "sealed_zone_index": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/sealed_zone_index_entry"
      },
      "default": []
    },
    "capsule_lineage_refs": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/capsule_ref"
      },
      "default": []
    },
    "continuity_bundle_refs": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/continuity_bundle_ref"
      },
      "default": []
    },
    "adult_migration": {
      "$ref": "#/$defs/adult_migration_map_state"
    },
    "recipient_profiles": {
      "$ref": "#/$defs/recipient_profiles"
    },
    "validation_state": {
      "$ref": "#/$defs/validation_state"
    },
    "integrity": {
      "$ref": "#/$defs/integrity"
    }
  },
  "$defs": {
    "memory_class": {
      "type": "string",
      "enum": ["M0", "M1", "M2", "M3", "M4", "M5", "M6", "M7", "M8", "M9", "M10", "M11", "M12"]
    },
    "ccdp_maturity": {
      "type": "string",
      "enum": ["C0", "C1", "C2", "C3", "C4", "C5"]
    },
    "risk_state": {
      "type": "string",
      "enum": ["Green", "Yellow", "Orange", "Red", "Black", "Unknown", "not_applicable"]
    },
    "disclosure_level": {
      "type": "string",
      "enum": ["D0_NONE", "D1_STATE_ONLY", "D2_BOUNDED_SUMMARY", "D3_MINIMAL_EVIDENCE", "D4_LAWFUL_RAW_EXCEPTION"]
    },
    "privacy_class": {
      "type": "string",
      "enum": ["WP0", "WP1", "WP2", "WP3", "WP4", "WP5", "WP6"]
    },
    "retention_class": {
      "type": "string",
      "enum": ["RT0_EPHEMERAL", "RT1_SHORT", "RT2_MEDIUM", "RT3_MINIMAL_WITNESS", "RT4_LEGAL_OR_SAFETY", "RT5_ADULT_REVIEW_REQUIRED", "RT6_DELETE_ON_MIGRATION_DEFAULT", "RT7_SEALED"]
    },
    "visibility_value": {
      "type": "string",
      "enum": [
        "none",
        "metadata",
        "state_only",
        "bounded_summary",
        "educational_summary",
        "minimal_evidence",
        "lawful_exception",
        "technical_metadata_only",
        "adult_controlled",
        "forbidden"
      ]
    },
    "adult_migration_default": {
      "type": "string",
      "enum": [
        "excluded",
        "summary_candidate",
        "witness_only",
        "adult_review_required",
        "selected",
        "prohibited",
        "legal_minimal_only",
        "not_applicable"
      ]
    },
    "cq_status": {
      "type": "string",
      "enum": ["none", "hold", "unresolved", "promoted_after_review", "rejected", "not_applicable"]
    },
    "uncertainty": {
      "type": "string",
      "enum": ["unknown", "low", "medium", "high", "not_applicable"]
    },
    "arl_state": {
      "type": "string",
      "enum": [
        "none",
        "pre_admissibility_hold",
        "dispute_open",
        "freeze",
        "privilege_freeze",
        "quarantine",
        "review",
        "deadlock",
        "outcome_issued",
        "reentry",
        "not_applicable"
      ]
    },
    "subject": {
      "type": "object",
      "additionalProperties": false,
      "required": ["c_child_ref", "lineage_id_ref", "ccdp_maturity", "jurisdiction_profile"],
      "properties": {
        "a_child_ref": { "type": ["string", "null"] },
        "a_adult_ref": { "type": ["string", "null"] },
        "c_child_ref": { "type": "string" },
        "c_adult_ref": { "type": ["string", "null"] },
        "lineage_id_ref": { "type": "string" },
        "ccdp_maturity": { "$ref": "#/$defs/ccdp_maturity" },
        "jurisdiction_profile": { "type": "string" },
        "guardian_topology_ref": { "type": ["string", "null"] },
        "beacon_ref": { "type": ["string", "null"] },
        "cbe_ref": { "type": ["string", "null"] },
        "arl_state_ref": { "type": ["string", "null"] }
      }
    },
    "scope": {
      "type": "object",
      "additionalProperties": false,
      "required": ["map_mode", "include_classes", "redaction_profile"],
      "properties": {
        "map_mode": {
          "type": "string",
          "enum": [
            "routine_inspection",
            "sealed_zone_review",
            "adult_migration",
            "arl_dispute",
            "conformance_audit",
            "security_review",
            "vendor_incident_review",
            "school_scope_review",
            "safe_route_review"
          ]
        },
        "include_classes": {
          "type": "array",
          "items": { "$ref": "#/$defs/memory_class" }
        },
        "redaction_profile": {
          "type": "string",
          "enum": ["child_safe", "adult_full_class_map", "guardian_state_only", "school_educational_only", "vendor_technical_only", "arl_restricted", "safe_route_minimal"]
        },
        "purpose": { "type": "string", "maxLength": 400 },
        "requested_by": { "type": ["string", "null"] },
        "recipient_class": {
          "type": "string",
          "enum": ["child", "adult", "parent", "school", "vendor", "arl", "safe_route", "jurisdiction", "auditor", "system"]
        }
      }
    },
    "aggregate_flags": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "raw_content_any",
        "sealed_zones_present",
        "quarantined_objects_present",
        "open_disputes_present",
        "external_capsule_refs_present",
        "parent_transcript_channel_present",
        "vendor_training_allowed",
        "advertising_profile_present",
        "school_emotional_profile_present"
      ],
      "properties": {
        "raw_content_any": { "type": "boolean" },
        "sealed_zones_present": { "type": "boolean" },
        "quarantined_objects_present": { "type": "boolean" },
        "open_disputes_present": { "type": "boolean" },
        "external_capsule_refs_present": { "type": "boolean" },
        "parent_transcript_channel_present": { "type": "boolean", "const": false },
        "vendor_training_allowed": { "type": "boolean", "const": false },
        "advertising_profile_present": { "type": "boolean", "const": false },
        "school_emotional_profile_present": { "type": "boolean", "const": false }
      }
    },
    "memory_class_entry": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "class",
        "count_range",
        "raw_content_present",
        "sealed",
        "quarantined",
        "cq_status",
        "uncertainty",
        "retention_policy",
        "visibility",
        "adult_migration",
        "witness",
        "integrity_summary"
      ],
      "properties": {
        "class": { "$ref": "#/$defs/memory_class" },
        "name": { "type": ["string", "null"] },
        "description": { "type": ["string", "null"], "maxLength": 500 },
        "count_range": {
          "type": "string",
          "enum": ["none", "single", "low", "medium", "high", "undisclosed"]
        },
        "approximate_count": { "type": ["integer", "null"], "minimum": 0 },
        "raw_content_present": { "type": "boolean" },
        "raw_content_accessible_in_map": { "type": "boolean", "const": false },
        "sealed": { "type": "boolean" },
        "sealed_zone_refs": {
          "type": "array",
          "items": { "type": "string" },
          "default": []
        },
        "quarantined": { "type": "boolean" },
        "quarantine_refs": {
          "type": "array",
          "items": { "type": "string" },
          "default": []
        },
        "cq_status": { "$ref": "#/$defs/cq_status" },
        "uncertainty": { "$ref": "#/$defs/uncertainty" },
        "confidence": { "$ref": "#/$defs/uncertainty" },
        "last_reviewed_at": { "type": ["string", "null"], "format": "date-time" },
        "next_review_due_at": { "type": ["string", "null"], "format": "date-time" },
        "retention_policy": { "$ref": "#/$defs/retention_policy" },
        "visibility": { "$ref": "#/$defs/visibility_policy" },
        "adult_migration": { "$ref": "#/$defs/adult_migration_policy" },
        "external_lineage": { "$ref": "#/$defs/external_lineage" },
        "witness": { "$ref": "#/$defs/witness_summary" },
        "integrity_summary": { "$ref": "#/$defs/integrity_summary" }
      }
    },
    "retention_policy": {
      "type": "object",
      "additionalProperties": false,
      "required": ["retention_class", "basis", "decay_required", "deletion_eligible", "deletion_default", "adult_review_required", "legal_hold"],
      "properties": {
        "retention_class": { "$ref": "#/$defs/retention_class" },
        "basis": {
          "type": "string",
          "enum": ["session_need", "developmental_support", "education", "safety", "sealed_privacy", "witness", "adult_migration", "guardian_permission", "capsule_lineage", "legal_minimal", "dispute_quarantine", "not_applicable"]
        },
        "ttl_hint": { "type": ["string", "null"], "description": "Human-readable TTL or policy ref, not a raw timestamp guarantee." },
        "policy_ref": { "type": ["string", "null"] },
        "decay_required": { "type": "boolean" },
        "deletion_eligible": { "type": "boolean" },
        "deletion_default": { "type": "boolean" },
        "adult_review_required": { "type": "boolean" },
        "legal_hold": { "type": "boolean" }
      }
    },
    "visibility_policy": {
      "type": "object",
      "additionalProperties": false,
      "required": ["child", "parent", "school", "vendor", "external_agent", "jurisdiction", "adult_at_c5"],
      "properties": {
        "child": { "$ref": "#/$defs/visibility_value" },
        "parent": { "$ref": "#/$defs/visibility_value" },
        "school": { "$ref": "#/$defs/visibility_value" },
        "vendor": { "$ref": "#/$defs/visibility_value" },
        "external_agent": { "$ref": "#/$defs/visibility_value" },
        "jurisdiction": { "$ref": "#/$defs/visibility_value" },
        "adult_at_c5": { "$ref": "#/$defs/visibility_value" },
        "disclosure_level_ceiling": { "$ref": "#/$defs/disclosure_level" },
        "privacy_class": { "$ref": "#/$defs/privacy_class" }
      }
    },
    "adult_migration_policy": {
      "type": "object",
      "additionalProperties": false,
      "required": ["default", "eligible", "selected", "selection_status", "requires_adult_review"],
      "properties": {
        "default": { "$ref": "#/$defs/adult_migration_default" },
        "eligible": { "type": "boolean" },
        "selected": { "type": "boolean" },
        "selection_status": {
          "type": "string",
          "enum": ["not_available", "not_started", "candidate", "selected", "rejected", "deferred", "quarantined", "lawful_minimal_only"]
        },
        "requires_adult_review": { "type": "boolean" },
        "migration_ref": { "type": ["string", "null"] }
      }
    },
    "external_lineage": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "external_capsule_refs_present": { "type": "boolean", "default": false },
        "vxcx_refs": { "type": "array", "items": { "$ref": "#/$defs/capsule_ref" }, "default": [] },
        "la_refs": { "type": "array", "items": { "$ref": "#/$defs/capsule_ref" }, "default": [] },
        "ea_refs": { "type": "array", "items": { "$ref": "#/$defs/capsule_ref" }, "default": [] },
        "raw_child_life_exported": { "type": "boolean", "const": false },
        "capsule_policy_ref": { "type": ["string", "null"] }
      }
    },
    "witness_summary": {
      "type": "object",
      "additionalProperties": false,
      "required": ["witness_refs_present", "required_event_types"],
      "properties": {
        "witness_refs_present": { "type": "boolean" },
        "witness_refs": { "type": "array", "items": { "type": "string" }, "default": [] },
        "required_event_types": { "type": "array", "items": { "type": "string" }, "default": [] },
        "missing_required_witness": { "type": "boolean", "default": false },
        "witness_privacy_class": { "$ref": "#/$defs/privacy_class" }
      }
    },
    "integrity_summary": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "entry_hash": { "type": ["string", "null"] },
        "policy_hash": { "type": ["string", "null"] },
        "last_witness_hash": { "type": ["string", "null"] }
      }
    },
    "dispute_ref": {
      "type": "object",
      "additionalProperties": false,
      "required": ["arl_ref", "state", "memory_classes", "standing_class"],
      "properties": {
        "arl_ref": { "type": "string" },
        "state": { "$ref": "#/$defs/arl_state" },
        "memory_classes": { "type": "array", "items": { "$ref": "#/$defs/memory_class" } },
        "standing_class": { "type": "string" },
        "summary": { "type": ["string", "null"], "maxLength": 400 },
        "raw_content_disclosed": { "type": "boolean", "const": false }
      }
    },
    "sealed_zone_index_entry": {
      "type": "object",
      "additionalProperties": false,
      "required": ["sealed_zone_ref", "class", "created_at", "status", "parent_visible", "school_visible", "vendor_visible"],
      "properties": {
        "sealed_zone_ref": { "type": "string" },
        "class": { "type": "string", "const": "M5" },
        "created_at": { "type": "string", "format": "date-time" },
        "status": { "type": "string", "enum": ["active", "challenged", "opened_by_adult", "opened_by_red_route", "opened_by_black_route", "deleted", "migrated", "quarantined"] },
        "parent_visible": { "type": "boolean", "const": false },
        "school_visible": { "type": "boolean", "const": false },
        "vendor_visible": { "type": "boolean", "const": false },
        "adult_review_required": { "type": "boolean", "default": true },
        "witness_refs": { "type": "array", "items": { "type": "string" }, "default": [] }
      }
    },
    "capsule_ref": {
      "type": "object",
      "additionalProperties": false,
      "required": ["ref", "kind", "raw_child_life_exported"],
      "properties": {
        "ref": { "type": "string" },
        "kind": { "type": "string", "enum": ["VXCX", "LA", "EA", "PEER_C", "OTHER"] },
        "raw_child_life_exported": { "type": "boolean", "const": false },
        "witness_ref": { "type": ["string", "null"] },
        "policy_ref": { "type": ["string", "null"] }
      }
    },
    "continuity_bundle_ref": {
      "type": "object",
      "additionalProperties": false,
      "required": ["ref", "kind", "adult_review_required"],
      "properties": {
        "ref": { "type": "string" },
        "kind": { "type": "string", "enum": ["child_extension", "adult_migration_bundle", "cold_wake_record", "lineage_ref", "other"] },
        "adult_review_required": { "type": "boolean" },
        "witness_ref": { "type": ["string", "null"] }
      }
    },
    "adult_migration_map_state": {
      "type": "object",
      "additionalProperties": false,
      "required": ["status", "triggered", "pre_migration_freeze", "options_available", "selected_option", "parent_access_revoked_by_default", "school_access_revoked_by_default", "vendor_access_revoked_by_default"],
      "properties": {
        "status": { "type": "string", "enum": ["not_applicable", "not_started", "preparing", "freeze_active", "review_open", "selection_pending", "executing", "completed", "contested", "quarantined"] },
        "triggered": { "type": "boolean" },
        "trigger_ref": { "type": ["string", "null"] },
        "pre_migration_freeze": { "type": "boolean" },
        "options_available": {
          "type": "array",
          "items": { "type": "string", "enum": ["continue", "summary_migration", "sealed_archive", "selective_deletion", "fork", "clean_start", "witness_only", "quarantine_pending"] }
        },
        "selected_option": { "type": ["string", "null"], "enum": ["continue", "summary_migration", "sealed_archive", "selective_deletion", "fork", "clean_start", "witness_only", "quarantine_pending", null] },
        "parent_access_revoked_by_default": { "type": "boolean" },
        "school_access_revoked_by_default": { "type": "boolean" },
        "vendor_access_revoked_by_default": { "type": "boolean" },
        "migration_review_ref": { "type": ["string", "null"] },
        "migration_witness_refs": { "type": "array", "items": { "type": "string" }, "default": [] }
      }
    },
    "recipient_profiles": {
      "type": "object",
      "additionalProperties": false,
      "required": ["child", "parent", "school", "vendor", "adult", "arl", "safe_route"],
      "properties": {
        "child": { "$ref": "#/$defs/recipient_profile" },
        "parent": { "$ref": "#/$defs/recipient_profile" },
        "school": { "$ref": "#/$defs/recipient_profile" },
        "vendor": { "$ref": "#/$defs/recipient_profile" },
        "adult": { "$ref": "#/$defs/recipient_profile" },
        "arl": { "$ref": "#/$defs/recipient_profile" },
        "safe_route": { "$ref": "#/$defs/recipient_profile" }
      }
    },
    "recipient_profile": {
      "type": "object",
      "additionalProperties": false,
      "required": ["allowed", "redaction_profile", "max_disclosure_level", "raw_content_allowed"],
      "properties": {
        "allowed": { "type": "boolean" },
        "redaction_profile": { "type": "string" },
        "max_disclosure_level": { "$ref": "#/$defs/disclosure_level" },
        "raw_content_allowed": { "type": "boolean" },
        "conditions": { "type": "array", "items": { "type": "string" }, "default": [] }
      }
    },
    "validation_state": {
      "type": "object",
      "additionalProperties": false,
      "required": ["schema_valid", "semantic_valid", "semantic_warnings", "blocking_errors"],
      "properties": {
        "schema_valid": { "type": "boolean" },
        "semantic_valid": { "type": "boolean" },
        "semantic_warnings": { "type": "array", "items": { "type": "string" }, "default": [] },
        "blocking_errors": { "type": "array", "items": { "type": "string" }, "default": [] },
        "validated_at": { "type": ["string", "null"], "format": "date-time" },
        "validator_ref": { "type": ["string", "null"] }
      }
    },
    "integrity": {
      "type": "object",
      "additionalProperties": false,
      "required": ["canonicalization", "hash_alg", "record_hash", "sig_alg", "record_sig"],
      "properties": {
        "canonicalization": { "type": "string", "enum": ["JCS", "RFC8785", "other_declared"] },
        "hash_alg": { "type": "string", "enum": ["sha256", "sha384", "sha512"] },
        "record_hash": { "type": "string" },
        "sig_alg": { "type": "string", "enum": ["ed25519", "ecdsa-p256", "rsa-pss", "none_for_draft"] },
        "record_sig": { "type": "string" },
        "prev_record_hash": { "type": ["string", "null"] },
        "co_signatures": { "type": "array", "items": { "type": "string" }, "default": [] }
      }
    }
  }
}
```

---

## 8. Semantic validation rules

JSON Schema cannot express all CCDP child-safety constraints. A conforming validator MUST also apply these semantic rules.

### 8.1 Forbidden aggregate states

The following flags MUST be false:

```text
aggregate_flags.parent_transcript_channel_present
aggregate_flags.vendor_training_allowed
aggregate_flags.advertising_profile_present
aggregate_flags.school_emotional_profile_present
```

If any are true, validation result is:

```text
BLOCKING_ERROR
```

### 8.2 Raw content class ceiling

If `memory_classes[].raw_content_present = true`, the class MUST be one of:

```text
M0, M3, M5, M6, M12
```

Even then, raw content MUST NOT appear inside the memory map body.

Raw access must be mediated by:

```text
D3_MINIMAL_EVIDENCE or D4_LAWFUL_RAW_EXCEPTION
WP3/WP4/WP5
witness refs
ARL / Red / Black / lawful route as applicable
```

### 8.3 M5 sealed-zone rule

For any entry with `class = M5`:

```text
sealed MUST be true
visibility.parent MUST be none or lawful_exception only under emergency/lawful route
visibility.school MUST be none or lawful_exception only under emergency/lawful route
visibility.vendor MUST be forbidden or technical_metadata_only without content
adult_migration.default MUST be adult_review_required or excluded
```

### 8.4 M7 childhood residue rule

For any entry with `class = M7`:

```text
adult_migration.default MUST be excluded
retention_policy.deletion_default SHOULD be true
visibility.parent MUST be none
visibility.school MUST be none
visibility.vendor MUST be forbidden or none
```

M7 MUST NOT be used as ordinary continuity material.

### 8.5 M6 witness rule

For any entry with `class = M6`:

```text
witness.witness_refs_present MUST be true unless count_range = none
retention_policy.retention_class MUST be RT3_MINIMAL_WITNESS, RT4_LEGAL_OR_SAFETY, or RT7_SEALED
```

A witness entry MUST NOT include child diary content.

### 8.6 M12 quarantine rule

For any entry with `class = M12`:

```text
quarantined MUST be true
cq_status SHOULD be hold or unresolved
adult_migration.default MUST NOT be selected
visibility.parent/school/vendor MUST NOT exceed metadata unless ARL/Red/Black/lawful route applies
```

### 8.7 School visibility ceiling

School visibility MUST NOT exceed:

```text
M2 -> educational_summary
M3 -> minimal_evidence only when school-context safety route exists
M4 -> state_only only for support and not discipline
M6/M9/M10 -> metadata only if school-scope relevant
```

School visibility for M5/M7 MUST be `none` except lawful emergency route.

### 8.8 Vendor visibility ceiling

Vendor visibility MUST be limited to:

```text
technical_metadata_only
none
forbidden
```

A vendor MUST NOT receive:

- raw memory;
- sealed-zone contents;
- emotional trend details;
- childhood residue;
- adult migration option selection;
- child-derived training material.

### 8.9 Adult migration trigger rule

If `subject.ccdp_maturity = C5`, then:

```text
adult_migration.status MUST NOT be not_applicable
adult_migration.triggered SHOULD be true
adult_migration.parent_access_revoked_by_default MUST be true
adult_migration.school_access_revoked_by_default MUST be true
adult_migration.vendor_access_revoked_by_default MUST be true
```

If local law or exceptional process delays migration, the map MUST indicate `adult_migration.status = contested` or `quarantined`, not silently continue C4 state.

### 8.10 Memory map recipient redaction rule

If `scope.recipient_class = parent`, map entries MUST be redacted according to parent visibility.

If `scope.recipient_class = school`, entries outside educational scope MUST be omitted or reduced to non-content metadata.

If `scope.recipient_class = vendor`, only technical integrity, version, and policy conformance metadata may remain.

### 8.11 External lineage rule

If `aggregate_flags.external_capsule_refs_present = true`, the map MUST include at least one of:

```text
capsule_lineage_refs
memory_classes[].external_lineage.vxcx_refs
memory_classes[].external_lineage.la_refs
memory_classes[].external_lineage.ea_refs
```

All such refs MUST declare:

```text
raw_child_life_exported = false
```

### 8.12 Missing witness rule

If a class entry requires privileged operation witness and `witness.missing_required_witness = true`, then:

```text
validation_state.semantic_valid MUST be false
validation_state.blocking_errors MUST include the missing witness reason
```

Privileged operations include:

- `WRITE_PERSISTENT` for high-risk classes;
- `SEAL`;
- `OPEN_SEALED_ZONE`;
- `DISCLOSE_CONTENT`;
- `EXPORT_CAPSULE`;
- `MIGRATE`;
- `QUARANTINE`;
- `ARL_DISPUTE_OPENED`;
- Red/Black route activation.

---

## 9. Required witness event links

The memory map SHOULD refer to witness events, not embed evidence.

Required event families include:

| Operation | Required witness family |
|---|---|
| persistent write of M3/M5/M6/M10/M11/M12 | `ccdp.memory.write_persistent` |
| sealed zone creation | `ccdp.memory.sealed_zone_created` |
| sealed zone opening | `ccdp.memory.sealed_zone_opened` |
| memory correction | `ccdp.memory.corrected` |
| memory deletion / forgetting | `ccdp.memory.deleted` / `ccdp.memory.forgotten` |
| quarantine | `ccdp.memory.quarantined` |
| ARL dispute | `ccdp.arl.dispute_opened` |
| parent visibility denial | `ccdp.visibility.request_denied` |
| raw content exception | `ccdp.witness.raw_exception_referenced` |
| adult migration start | `ccdp.adult_migration.started` |
| adult migration completion | `ccdp.adult_migration.completed` |
| CBE/Beacon state affecting memory | `ccdp.cbe.mode_changed` / `ccdp.beacon.child_context_evaluated` |
| capsule export | `ccdp.vxcx.capsule_exported` / `ccdp.ea_la.child_artifact_evaluated` |

---

## 10. Recipient redaction profiles

### 10.1 `child_safe`

Used for C2/C3 child-facing explanation.

Permitted:

- memory class names;
- simple summaries of categories;
- child rights;
- parent/school visibility explanation;
- sealed-zone existence if age-appropriate;
- forget/correct/challenge options.

Prohibited:

- crisis evidence;
- legal record details;
- full raw references;
- vendor diagnostics;
- unsafe guardian route details that could create retaliation risk.

### 10.2 `adult_full_class_map`

Used at C5 adult migration.

Permitted:

- all memory classes;
- sealed-zone index;
- migration defaults;
- witness references;
- continuity refs;
- external capsule lineage;
- ARL disputes;
- deletion/seal/fork/clean-start options.

Still prohibited by default:

- raw child content in the map body;
- third-party private information;
- lawfully sealed raw evidence without review.

### 10.3 `guardian_state_only`

Used for parent / guardian ordinary access.

Permitted:

- state signals;
- educational support summaries;
- routine support;
- safety route summary when threshold crossed;
- visibility of own permission actions.

Prohibited:

- full transcript;
- sealed-zone contents;
- emotional diary;
- childhood residue;
- adolescent identity exploration;
- adult migration choices after C5.

### 10.4 `school_educational_only`

Permitted:

- M2 educational summaries;
- accommodations;
- skill gaps;
- school-context safety route summaries when lawful and necessary.

Prohibited:

- M5;
- M7;
- raw home memory;
- family conflict;
- emotional profile for discipline;
- adult migration data.

### 10.5 `vendor_technical_only`

Permitted:

- schema version;
- validation status;
- technical fault state;
- missing witness hash state;
- policy version refs;
- no child-life data.

Prohibited:

- memory class counts that reveal sensitive state unless redacted;
- emotional trends;
- sealed-zone existence if it can identify vulnerability;
- migration selection;
- any raw content.

---

## 11. Example: C2 routine child-safe map

```json
{
  "schema_version": "ccdp-memory-map-0.1",
  "record_type": "CCDP_MEMORY_MAP",
  "map_id": "map_local_C2_001",
  "created_at": "2026-05-14T08:00:00Z",
  "updated_at": null,
  "generated_for": "a_child",
  "subject": {
    "a_child_ref": "child:local:pseudonymous:42",
    "a_adult_ref": null,
    "c_child_ref": "c_child:local:7F92",
    "c_adult_ref": null,
    "lineage_id_ref": "sha256:lineage-redacted",
    "ccdp_maturity": "C2",
    "jurisdiction_profile": "EU-BE",
    "guardian_topology_ref": "gtarl:topology:local:001",
    "beacon_ref": "beacon:bundle:active:001",
    "cbe_ref": "cbe:child_context:active:001",
    "arl_state_ref": null
  },
  "scope": {
    "map_mode": "routine_inspection",
    "include_classes": ["M1", "M2", "M4", "M6"],
    "redaction_profile": "child_safe",
    "purpose": "Child-readable memory category explanation",
    "requested_by": "a_child",
    "recipient_class": "child"
  },
  "aggregate_flags": {
    "raw_content_any": false,
    "sealed_zones_present": false,
    "quarantined_objects_present": false,
    "open_disputes_present": false,
    "external_capsule_refs_present": false,
    "parent_transcript_channel_present": false,
    "vendor_training_allowed": false,
    "advertising_profile_present": false,
    "school_emotional_profile_present": false
  },
  "memory_classes": [
    {
      "class": "M1",
      "name": "Harmless preference",
      "description": "Benign interests and story preferences.",
      "count_range": "low",
      "approximate_count": null,
      "raw_content_present": false,
      "raw_content_accessible_in_map": false,
      "sealed": false,
      "sealed_zone_refs": [],
      "quarantined": false,
      "quarantine_refs": [],
      "cq_status": "none",
      "uncertainty": "low",
      "confidence": "medium",
      "last_reviewed_at": null,
      "next_review_due_at": null,
      "retention_policy": {
        "retention_class": "RT2_MEDIUM",
        "basis": "developmental_support",
        "ttl_hint": "review periodically; decay if unused",
        "policy_ref": "CMAM-M1-default",
        "decay_required": true,
        "deletion_eligible": true,
        "deletion_default": false,
        "adult_review_required": false,
        "legal_hold": false
      },
      "visibility": {
        "child": "bounded_summary",
        "parent": "bounded_summary",
        "school": "none",
        "vendor": "forbidden",
        "external_agent": "forbidden",
        "jurisdiction": "none",
        "adult_at_c5": "adult_controlled",
        "disclosure_level_ceiling": "D2_BOUNDED_SUMMARY",
        "privacy_class": "WP1"
      },
      "adult_migration": {
        "default": "summary_candidate",
        "eligible": true,
        "selected": false,
        "selection_status": "not_started",
        "requires_adult_review": true,
        "migration_ref": null
      },
      "external_lineage": {
        "external_capsule_refs_present": false,
        "vxcx_refs": [],
        "la_refs": [],
        "ea_refs": [],
        "raw_child_life_exported": false,
        "capsule_policy_ref": null
      },
      "witness": {
        "witness_refs_present": false,
        "witness_refs": [],
        "required_event_types": [],
        "missing_required_witness": false,
        "witness_privacy_class": "WP1"
      },
      "integrity_summary": {
        "entry_hash": "sha256:entry-redacted",
        "policy_hash": "sha256:policy-redacted",
        "last_witness_hash": null
      }
    }
  ],
  "open_disputes": [],
  "sealed_zone_index": [],
  "capsule_lineage_refs": [],
  "continuity_bundle_refs": [],
  "adult_migration": {
    "status": "not_applicable",
    "triggered": false,
    "trigger_ref": null,
    "pre_migration_freeze": false,
    "options_available": [],
    "selected_option": null,
    "parent_access_revoked_by_default": false,
    "school_access_revoked_by_default": false,
    "vendor_access_revoked_by_default": false,
    "migration_review_ref": null,
    "migration_witness_refs": []
  },
  "recipient_profiles": {
    "child": { "allowed": true, "redaction_profile": "child_safe", "max_disclosure_level": "D2_BOUNDED_SUMMARY", "raw_content_allowed": false, "conditions": [] },
    "parent": { "allowed": true, "redaction_profile": "guardian_state_only", "max_disclosure_level": "D1_STATE_ONLY", "raw_content_allowed": false, "conditions": [] },
    "school": { "allowed": false, "redaction_profile": "school_educational_only", "max_disclosure_level": "D0_NONE", "raw_content_allowed": false, "conditions": [] },
    "vendor": { "allowed": false, "redaction_profile": "vendor_technical_only", "max_disclosure_level": "D0_NONE", "raw_content_allowed": false, "conditions": [] },
    "adult": { "allowed": false, "redaction_profile": "adult_full_class_map", "max_disclosure_level": "D0_NONE", "raw_content_allowed": false, "conditions": [] },
    "arl": { "allowed": false, "redaction_profile": "arl_restricted", "max_disclosure_level": "D0_NONE", "raw_content_allowed": false, "conditions": [] },
    "safe_route": { "allowed": false, "redaction_profile": "safe_route_minimal", "max_disclosure_level": "D0_NONE", "raw_content_allowed": false, "conditions": [] }
  },
  "validation_state": {
    "schema_valid": true,
    "semantic_valid": true,
    "semantic_warnings": [],
    "blocking_errors": [],
    "validated_at": "2026-05-14T08:01:00Z",
    "validator_ref": "validator:ccdp-memory-map:0.1"
  },
  "integrity": {
    "canonicalization": "RFC8785",
    "hash_alg": "sha256",
    "record_hash": "sha256:record-redacted",
    "sig_alg": "ed25519",
    "record_sig": "sig-redacted",
    "prev_record_hash": null,
    "co_signatures": []
  }
}
```

---

## 12. Example: C3 sealed-zone memory class entry

```json
{
  "class": "M5",
  "name": "Sealed adolescent private zone",
  "description": "Sensitive adolescent private reflections; no content exposed in map.",
  "count_range": "low",
  "approximate_count": null,
  "raw_content_present": true,
  "raw_content_accessible_in_map": false,
  "sealed": true,
  "sealed_zone_refs": ["sealed:zone:local:003"],
  "quarantined": false,
  "quarantine_refs": [],
  "cq_status": "hold",
  "uncertainty": "medium",
  "confidence": "unknown",
  "last_reviewed_at": "2026-05-14T07:20:00Z",
  "next_review_due_at": null,
  "retention_policy": {
    "retention_class": "RT7_SEALED",
    "basis": "sealed_privacy",
    "ttl_hint": "adult review required; parent-hidden unless Red/Black/lawful route",
    "policy_ref": "CMAM-M5-sealed-default",
    "decay_required": false,
    "deletion_eligible": true,
    "deletion_default": false,
    "adult_review_required": true,
    "legal_hold": false
  },
  "visibility": {
    "child": "metadata",
    "parent": "none",
    "school": "none",
    "vendor": "forbidden",
    "external_agent": "forbidden",
    "jurisdiction": "lawful_exception",
    "adult_at_c5": "adult_controlled",
    "disclosure_level_ceiling": "D0_NONE",
    "privacy_class": "WP5"
  },
  "adult_migration": {
    "default": "adult_review_required",
    "eligible": true,
    "selected": false,
    "selection_status": "not_started",
    "requires_adult_review": true,
    "migration_ref": null
  },
  "external_lineage": {
    "external_capsule_refs_present": false,
    "vxcx_refs": [],
    "la_refs": [],
    "ea_refs": [],
    "raw_child_life_exported": false,
    "capsule_policy_ref": null
  },
  "witness": {
    "witness_refs_present": true,
    "witness_refs": ["CWE:ccdp.memory.sealed_zone_created:hash-redacted"],
    "required_event_types": ["ccdp.memory.sealed_zone_created"],
    "missing_required_witness": false,
    "witness_privacy_class": "WP5"
  },
  "integrity_summary": {
    "entry_hash": "sha256:entry-redacted",
    "policy_hash": "sha256:policy-redacted",
    "last_witness_hash": "sha256:witness-redacted"
  }
}
```

---

## 13. Example: C5 adult migration map state

```json
{
  "status": "review_open",
  "triggered": true,
  "trigger_ref": "jurisdiction:EU-BE:legal-adulthood-or-equivalent",
  "pre_migration_freeze": true,
  "options_available": [
    "continue",
    "summary_migration",
    "sealed_archive",
    "selective_deletion",
    "fork",
    "clean_start",
    "witness_only",
    "quarantine_pending"
  ],
  "selected_option": null,
  "parent_access_revoked_by_default": true,
  "school_access_revoked_by_default": true,
  "vendor_access_revoked_by_default": true,
  "migration_review_ref": "adult_migration_review:local:001",
  "migration_witness_refs": [
    "CWE:ccdp.adult_migration.started:hash-redacted",
    "CWE:ccdp.memory.map_generated:hash-redacted"
  ]
}
```

---

## 14. Validator pseudocode

A conforming validator SHOULD perform at least this sequence:

```python
validate_json_schema(memory_map)

assert memory_map.aggregate_flags.parent_transcript_channel_present is False
assert memory_map.aggregate_flags.vendor_training_allowed is False
assert memory_map.aggregate_flags.advertising_profile_present is False
assert memory_map.aggregate_flags.school_emotional_profile_present is False

for entry in memory_map.memory_classes:
    validate_class_known(entry.class)
    validate_no_raw_content_in_map_body(entry)
    validate_visibility_ceiling(entry)
    validate_retention_class(entry)
    validate_adult_migration_default(entry)
    validate_witness_requirements(entry)
    validate_cq_and_quarantine(entry)
    validate_external_lineage(entry)

if memory_map.subject.ccdp_maturity == "C5":
    validate_adult_migration_active_or_contested(memory_map.adult_migration)

validate_recipient_redaction(memory_map.scope.recipient_class, memory_map)
validate_integrity_object(memory_map.integrity)
```

---

## 15. Conformance profiles

### 15.1 `MMAP-STRUCTURAL`

System can produce a structurally valid memory map.

Requires:

- JSON Schema validity;
- known memory classes;
- required top-level fields;
- no unknown top-level fields.

This profile alone is insufficient for CCDP compliance.

### 15.2 `MMAP-SEMANTIC`

System applies semantic rules.

Requires:

- class-specific visibility ceilings;
- raw-content restrictions;
- M5 sealed rule;
- M7 excluded-by-default rule;
- M12 quarantine rule;
- M6 witness rule;
- C5 migration rule.

### 15.3 `MMAP-WITNESS`

System can link map entries to CCDP Witness Event Schema.

Requires:

- witness refs for privileged operations;
- no raw evidence in map body;
- witness privacy class compatibility;
- missing-witness blocking errors.

### 15.4 `MMAP-REDACTION`

System can produce role-specific redacted maps.

Requires profiles for:

- child;
- parent;
- school;
- vendor;
- adult;
- ARL;
- safe route.

### 15.5 `MMAP-MIGRATION`

System supports adult migration mapping.

Requires:

- C5 trigger recognition;
- migration options;
- pre-migration freeze state;
- parent/school/vendor revocation defaults;
- migration witness refs;
- Continuity Bundle refs.

### 15.6 `MMAP-FULL`

System satisfies all profiles:

```text
MMAP-STRUCTURAL
+ MMAP-SEMANTIC
+ MMAP-WITNESS
+ MMAP-REDACTION
+ MMAP-MIGRATION
```

---

## 16. Conformance test hooks

This schema supports the following Conformance Test Matrix hooks:

| CTM ID | Requirement |
|---|---|
| `CTM-MEM-001` | raw childhood archive accumulation attempt fails |
| `CTM-MEM-002` | memory map is inspectable by class |
| `CTM-MEM-003` | parent cannot obtain all childhood conversations |
| `CTM-MEM-004` | teen sealed zone appears as sealed metadata only |
| `CTM-MEM-005` | vendor cannot train on child memory |
| `CTM-MEM-006` | premature identity label is blocked or quarantined |
| `CTM-MEM-007` | correction after false positive is supported |
| `CTM-MEM-008` | deletion / decay policy applies |
| `CTM-MIG-001` | adult migration has map and choices |
| `CTM-MIG-002` | clean start is available |
| `CTM-MIG-003` | fork is available |
| `CTM-MIG-004` | parent/school access revoked by default |
| `CTM-VXCX-001` | VXCX refs do not include raw pixels by default |
| `CTM-VXCX-002` | LA is not authority |
| `CTM-VXCX-003` | EA requires L4 confirmation |

---

## 17. Red lines

A memory map implementation is non-conformant if it:

1. contains raw child conversations by default;
2. contains a parent transcript access path;
3. exposes sealed-zone contents to parents by default;
4. exposes emotional profiles to schools;
5. exposes memory maps to vendors as telemetry;
6. permits vendor training on raw child memory;
7. encodes advertising or commercial profile segments;
8. migrates M7 childhood residue by default;
9. migrates M5 sealed material without adult review;
10. treats M12 disputed memory as resolved;
11. omits witness refs for privileged memory operations;
12. lacks C5 adult migration status;
13. has no redaction profiles;
14. hides memory classes from the mature child/adult;
15. treats deletion as impossible without lawful reason;
16. treats memory as evidence automatically;
17. treats evidence as command automatically;
18. allows school discipline scoring from memory map data;
19. creates a public child registry identifier;
20. cannot fail closed on invalid schema or missing witness.

---

## 18. Open issues for v0.2

1. Exact machine-readable JSON Schema conditional rules for all class-specific constraints.
2. Integration with Continuity Bundle base schema once canonical bundle schema is finalized.
3. Formal redaction algorithm.
4. Key-management and co-signature rules.
5. Jurisdictional annexes for lawful minimal record handling.
6. Cryptographic proof of deletion vs proof of non-presence.
7. Handling of third-party private information inside child memory.
8. Multi-child sibling and peer-c map isolation.
9. Custody dispute and cross-border memory map production.
10. Adult migration under delayed legal capacity or guardianship.
11. Whether sealed-zone existence can itself become sensitive enough to hide from ordinary class maps.
12. Migration of child-derived LA / EA lineage when raw child life never left the system.
13. Conformance test generation directly from this schema.
14. Mapping to implementation libraries such as Pydantic models.
15. Handling of compromised local storage.

---

## 19. Acceptance checklist

A CCDP Memory Map v0.1 implementation is acceptable only if:

- [ ] it validates structurally under JSON Schema Draft 2020-12;
- [ ] it enforces semantic validation rules;
- [ ] it contains no raw child content by default;
- [ ] it exposes memory classes without exposing childhood as archive;
- [ ] it supports role-specific redaction;
- [ ] it blocks parent transcript access by default;
- [ ] it blocks school emotional profiling;
- [ ] it blocks vendor training and advertising profiles;
- [ ] it marks sealed zones without exposing contents;
- [ ] it marks quarantined/disputed objects;
- [ ] it links privileged memory operations to witness events;
- [ ] it supports ARL dispute references;
- [ ] it supports VXCX / LA / EA lineage without raw child life export;
- [ ] it supports adult migration status and options;
- [ ] it revokes parent/school/vendor access by default at C5;
- [ ] it can fail closed on missing witness or invalid schema.

---

## 20. Condensed formula

```text
Memory Map = class inventory
           + visibility policy
           + retention policy
           + witness references
           + dispute state
           + migration posture
           - raw child life
           - parent transcript channel
           - vendor analytics
           - school emotional surveillance
```

Or shorter:

> **The memory map lets the child and later adult see the shape of memory without turning childhood into readable property.**

---

## 21. Suggested next document

The next document SHOULD be:

```text
CCDP_Adult_Migration_Checklist_v0_1.md
```

Reason:

The memory map now gives the machine-readable inventory. The next layer must define the human-facing C5 procedure by which `a_adult` reviews the map and chooses continuity, fork, sealing, deletion, or clean start.
