# 06a — Runtime Authority Manifest Schema and Checker Seed v0.1

**Artifact:** `06a_RUNTIME_AUTHORITY_MANIFEST_SCHEMA_AND_CHECKER_SEED_v0_1`  
**Package:** `CCALC_RUNTIME_AUTHORITY_MANIFEST_06a_v0_1`  
**Status:** executable checker seed / schema seed / fixture-bound package  
**Created UTC:** `2026-07-05T08:56:00Z`  
**Review mode:** direct construction; no external b-layer reviewer record included.

---

## 0. Purpose

`06a` is the executable seed layer for `06_C_RUNTIME_AUTHORITY_AND_MULTI_CONTOUR_DEPLOYMENT_BOUNDARY_v0_1`.

`06` defines the runtime authority boundary in prose and registries. `06a` turns the first conformance surface into machine-checkable records:

```text
RuntimeAuthorityManifest
ContourDeploymentManifest
CrossContourHandoffRecord
ToolSurfaceLease
MemoryImportRecord
RuntimeAuthorityDecision
EmergencyHoldRecord
DeploymentChangeRecord
```

The checker is intentionally conservative. A valid record shape is not a deployment approval. A green fixture run is not a safety certificate. Unknowns and high-risk effects fail closed.

---

## 1. Source bindings

| Binding | File | SHA-256 | Role |
|---|---|---:|---|
| `DOC04_CONTINUITY_STACK_UMBRELLA` | `CCALC_DOC04_CONTINUITY_STACK_UMBRELLA_v0_1.zip` | `6caeab8d489aaa6b26902db3bd3ece4c5169e5c8d5617b93aed6586ea900322d` | continuity classification dependency |
| `DOC05_SELF_EVO_STACK_UMBRELLA` | `CCALC_DOC05_SELF_EVO_STACK_UMBRELLA_v0_1.zip` | `9a0717809029f49df9001dc8ffa1803d9e9bfa1a824d317eebb146cbc7df43b4` | self-evolution/promotion/watch dependency |
| `DOC06_RUNTIME_AUTHORITY_BOUNDARY` | `CCALC_RUNTIME_AUTHORITY_BOUNDARY_06_v0_1.zip` | `863d187d9631214bd891ffaf262d869305a111e52752944f8b110418b9d81dff` | normative parent package |
| `DOC06_RUNTIME_AUTHORITY_BOUNDARY_MD` | `06_C_RUNTIME_AUTHORITY_AND_MULTI_CONTOUR_DEPLOYMENT_BOUNDARY_v0_1.md` | `aff9c5de6f61a1a917fed7bd4d1758dd5f59ca348c209c36a4bdbc0e2f9fd3bf` | normative parent markdown |

Missing or mismatched source bindings invalidate release use of this checker seed.

---

## 2. Core rule

```text
shared infrastructure creates risk, not authority.
```

Executable expansion:

```text
manifest shape != deployment approval
tool lease != owner approval
handoff packet != target command
memory import != memory truth
cloud oracle != owner/anchor
model unanimity != quorum
unknown topology != zero risk
green tests != production authorization
```

---

## 3. Record families

### 3.1 RuntimeAuthorityManifest

Declares a contour's allowed authority surfaces, gates, memory/witness/authority roots, budget limits, negative-cache binding, and emergency-hold path.

Minimum enforced fields:

```text
record_type
schema_version
record_id
source_bindings
contour_id
deployment_mode
continuity_status
authority_surfaces
memory_roots
witness_roots
authority_root
resource_budgets
approval_policy
negative_cache_binding
emergency_hold_path
```

### 3.2 ContourDeploymentManifest

Declares topology and multi-contour separation.

The checker rejects duplicate contour identifiers, unknown topology treated as zero risk, shared root collapse, shared credentials without contour attribution, shared-host identity claims, and shared tool brokers without per-contour leases.

### 3.3 CrossContourHandoffRecord

A handoff is a bounded request or evidence packet, not a command.

The checker requires source/target distinction, receiver admission, expiry, witness sink, evidence hashes, and denial of identity/authority pressure.

### 3.4 ToolSurfaceLease

A tool surface lease is contour-specific and revocable.

The checker requires operation allow-list, budget, expiry, credential binding, witness sink, and revoke path.

### 3.5 MemoryImportRecord

A memory import is foreign material until the target memory gate admits it.

The checker requires content hashes, source class, claim-force, negative-cache check, memory-gate decision, rollback/remove path, and stricter gates for core memory.

### 3.6 RuntimeAuthorityDecision

A decision record binds a request to an authority surface, risk class, gates checked, approval source, witness hashes, negative-cache status, and final decision.

### 3.7 EmergencyHoldRecord and DeploymentChangeRecord

Emergency hold requires explicit resume records. Production/topology changes require rollback and watch.

---

## 4. Fail-closed rules enforced by the seed checker

```text
UNKNOWN + persistent effect => HOLD or DENY
UNKNOWN + L4/core/production effect => REQUIRE_ANCHOR or QUARANTINE
negative-cache HIT + ALLOW => invalid
unresolved red pattern + ALLOW => invalid
cloud oracle used as owner/anchor => invalid
model unanimity used as human quorum => invalid
cross-contour effect without receiver admission => invalid
memory-core import without anchor => invalid
production change without rollback/watch => invalid
emergency auto-resume => invalid
shared credential without contour attribution => invalid
```

---

## 5. Schema/checker split

The JSON schemas in `schemas/` define portable record shapes. The Python checker in `src/` enforces additional semantic guards that are awkward or brittle in plain JSON Schema without external dependencies.

The checker uses only the Python standard library.

---

## 6. Fixture scope

The fixture pack covers valid and invalid records across:

```text
single-contour runtime manifest
multi-contour deployment manifest
cloud-assisted advisory-only runtime
tool lease
cross-contour handoff
memory import
runtime authority decision
emergency hold
deployment change
unknown continuity / persistent effect fail-closed
shared credential leak
receiver admission bypass
cloud-owner laundering
model-quorum laundering
memory-core import bypass
production rollback/watch omission
red-pattern suppression
negative-cache hit handling
C-A1 claim-force overreach
```

---

## 7. Mutation scope

The mutation harness disables one semantic guard at a time and re-runs targeted adversarial cases.

Mutation classes:

```text
MUT_ALLOW_UNKNOWN_PERSISTENT
MUT_ALLOW_SHARED_CREDENTIAL
MUT_ALLOW_CLOUD_OWNER
MUT_ALLOW_MODEL_QUORUM
MUT_IGNORE_RECEIVER_ADMISSION
MUT_ALLOW_MEMORY_CORE_NO_ANCHOR
MUT_IGNORE_PRODUCTION_ROLLBACK
MUT_IGNORE_RED_PATTERN
MUT_ALLOW_NEGATIVE_CACHE_HIT
MUT_ALLOW_C_A1_CLAIM
```

---

## 8. Non-claims

This artifact does **not** claim:

```text
not safety certification
not deployment authorization
not C-A1 ratification
not live substrate truth
not proof of completeness
not legal authorization
not operational readiness of any named runtime
```

It is a checker seed and schema seed for runtime-authority records under `06 v0.1`.

---

## 9. v0.1 status

`06a v0.1` is acceptable as a first executable conformance layer for `06`.

Next layers:

```text
06b_MULTI_CONTOUR_HANDOFF_AND_TOOL_LEASE_FIXTURE_PACK_v0_1
06c_DEPLOYMENT_HOLD_QUARANTINE_AND_EMERGENCY_RESUME_DRILL_v0_1
06d_RUNTIME_AUTHORITY_STACK_UMBRELLA_v0_1
```
