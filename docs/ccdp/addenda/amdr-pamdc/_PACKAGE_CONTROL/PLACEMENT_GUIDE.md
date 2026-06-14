# Placement Guide — AMDR / PAMDC Addendum v0.1.1

## Package metadata

```text
Package title: CCDP AMDR/PAMDC Addendum v0.1.1
Addendum DOI: 10.5281/zenodo.20691716
DOI URL: https://doi.org/10.5281/zenodo.20691716
Author: Kotov Ivan
Location: Bruxelles, Belgium
Year: 2026
Canonical placement: docs/ccdp/addenda/amdr-pamdc/
```

## Recommended repository layout

Copy this directory into the CCDP repository:

```text
docs/ccdp/addenda/amdr-pamdc/
  Active_Memory_Degradation_and_Recalibration_Profile_v0_1.md
  AMDR_v0_1_1_Lifestream_Judge_and_Write_Failure_Patch.md
  Post_Anchor_Memory_Degradation_and_Continuity_Profile_v0_1.md
  PAMDC_v0_1_1_Scope_Bootstrap_and_Freshness_Patch.md
```

Keep `_PACKAGE_CONTROL/` outside the canonical protocol path or place it under a release asset / packaging directory. It is not itself a normative protocol layer.

## Minimal repository update

At minimum, add a short entry to `INDEX.md` or `CANONICAL_READING_ORDER.md`:

```markdown
### Addenda

- `docs/ccdp/addenda/amdr-pamdc/Active_Memory_Degradation_and_Recalibration_Profile_v0_1.md` — AMDR v0.1, active memory degradation and recalibration while `a` remains present but review bandwidth is finite.
- `docs/ccdp/addenda/amdr-pamdc/AMDR_v0_1_1_Lifestream_Judge_and_Write_Failure_Patch.md` — AMDR v0.1.1 patch for lifestream ingestion, Judge integration, write-path failure, self-biography, and UI/log observability.
- `docs/ccdp/addenda/amdr-pamdc/Post_Anchor_Memory_Degradation_and_Continuity_Profile_v0_1.md` — PAMDC v0.1, post-anchor memory degradation and continuity profile.
- `docs/ccdp/addenda/amdr-pamdc/PAMDC_v0_1_1_Scope_Bootstrap_and_Freshness_Patch.md` — PAMDC v0.1.1 patch for scope, bootstrap authority, and freshness correction.
```

## Reading order recommendation

For CCDP readers:

```text
1. CCDP root / index / memory / witness baseline
2. Child_Memory_and_Adult_Migration_v0_1.md
3. CCDP_Memory_Map_JSON_Schema_v0_1.md
4. CCDP_Witness_Event_Schema_v0_1.md
5. Active_Memory_Degradation_and_Recalibration_Profile_v0_1.md
6. AMDR_v0_1_1_Lifestream_Judge_and_Write_Failure_Patch.md
7. Post_Anchor_Memory_Degradation_and_Continuity_Profile_v0_1.md
8. PAMDC_v0_1_1_Scope_Bootstrap_and_Freshness_Patch.md
```

Reason: AMDR governs active-memory freshness while `a` remains present. PAMDC governs post-anchor fail-closed continuity. Do not read PAMDC as a substitute for AMDR.

## Release note wording

Use:

```text
Added AMDR / PAMDC Addendum v0.1.1: four memory-continuity documents covering active memory degradation, write-path/lifestream/Judge failure modes, post-anchor continuity, and PAMDC scope/freshness correction.
```

Do not use:

```text
Replaced CCDP memory layer.
Solved child-memory degradation.
Added new child-safety standard.
Created post-human continuity.
```
