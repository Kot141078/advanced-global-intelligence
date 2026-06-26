# SRLM BGC Patch Notes v0.1.1

## Append-first correction record for `02_SRLM_Bounded_Growth_Contour_Profile_v0_1`

**Status:** patch notes / control-layer artifact  
**Date:** 2026-06-24  
**Patch ID:** `SRLM_BGC_PATCH_NOTES_v0_1_1`  
**Reviewed artifact:** `02_SRLM_Bounded_Growth_Contour_Profile_v0_1.md`  
**Corrected artifact:** `02_SRLM_Bounded_Growth_Contour_Profile_v0_1_1.md`  
**Review record:** `SRLM_BGC_REVIEW_RECORD_v0_1.md`  

This patch supersedes the reviewed v0.1 artifact by append-first correction. It does not delete or rewrite the review record.

## Source hashes

```text
old_sha256: 9befe126076f5f3b216ff3741e3191496526d5cb4b4aeda85bbbcca3445ea8af
review_sha256: 3077e3bed6ca08916ff0ddacb815a9f28e70ff823b6a66396ffe6760744d13ad
new_sha256: faee5682bb9463439923d7c7e7145c9f171d564622d9629820eb7c278cdd7de0
new_line_count: 2219
```

## Review findings addressed

| Finding | Class | Status | Correction |
|---|---|---|---|
| `SRLM-REV-F1` | must-fix | closed | Changed rollback-before-promotion from SHOULD to MUST in `SRLM-AX-10` and §18.1. |
| `SRLM-REV-F2` | should-fix | addressed | Added §8.4 crosswalk mapping C-SEG `SRLM-*` classes to SRLM-BGC operating states and `SRLM-C*` conformance levels; explicitly disambiguated namespaces. |
| `SRLM-REV-F3` | minor | addressed | Declared BGC blocked-prefix list as parent C-SEG list plus explicit SRLM-specific aliases; changed §35 example from named person to neutral `operator`. |

## Normative corrections

### Rollback requirement

Old wording:

```text
Promotion SHOULD write a rollback snapshot before policy change.
Before promotion, SRLM SHOULD write a rollback snapshot of the current policy.
```

New wording:

```text
Promotion MUST write a valid rollback snapshot before policy change.
Before promotion, SRLM MUST write a valid rollback snapshot of the current policy.
```

### Cross-profile interlock

New §8.4 defines:

```text
SRLM-*  = C-SEG routing class for a self-evo packet.
SRLM-C* = SRLM-BGC conformance level.
```

and gives a deterministic crosswalk between:

```text
C-SEG SRLM class
SRLM-BGC operating state
SRLM-BGC conformance floor
Gate result
```

### Blocked-prefix canonicalization

New §16.3 defines:

```text
SRLM-BGC blocked-prefix list = parent C-SEG blocked surface list + SRLM-specific explicit aliases.
```

The explicit SRLM-specific alias in v0.1.1 is:

```text
persona.core.
```

## Remaining watch items

- Schema extraction remains held until the corrected v0.1.1 profile receives re-review.
- `SRLM-C*` conformance levels and C-SEG `SRLM-*` classes should be represented in future schemas with distinct field names, for example `srlm_route_class` and `srlm_conformance_level`.
- Canary semantics remain future work unless C-SEG canary rules are formalized.

## Disposition

```text
Result: corrected draft ready for re-review.
No integration claim.
No conformance claim.
No deployment authorization.
```
