# Optional Index Patch Snippet

This file contains optional Markdown snippets. Apply manually after reviewing the local repository structure.

## `INDEX.md` snippet

```markdown
## AMDR / PAMDC Addendum v0.1.1

The CCDP corpus includes an optional memory-continuity addendum for general `c = a + b` memory degradation and post-anchor continuity discipline.

| File | Role | Status |
|---|---|---|
| `docs/ccdp/addenda/amdr-pamdc/Active_Memory_Degradation_and_Recalibration_Profile_v0_1.md` | Active memory degradation and recalibration while `a` remains present but review bandwidth is finite. | Addendum profile |
| `docs/ccdp/addenda/amdr-pamdc/AMDR_v0_1_1_Lifestream_Judge_and_Write_Failure_Patch.md` | Lifestream, Judge, write-path failure, self-biography, and UI/log observability patch. | Addendum patch |
| `docs/ccdp/addenda/amdr-pamdc/Post_Anchor_Memory_Degradation_and_Continuity_Profile_v0_1.md` | Post-anchor memory degradation and continuity fail-closed profile. | Addendum profile |
| `docs/ccdp/addenda/amdr-pamdc/PAMDC_v0_1_1_Scope_Bootstrap_and_Freshness_Patch.md` | PAMDC scope, bootstrap, and freshness correction patch. | Addendum patch |
```

## `CHANGELOG.md` snippet

```markdown
### Added

- AMDR / PAMDC Addendum v0.1.1 as a delta-only memory-continuity extension.
- `Active_Memory_Degradation_and_Recalibration_Profile_v0_1.md`.
- `AMDR_v0_1_1_Lifestream_Judge_and_Write_Failure_Patch.md`.
- `Post_Anchor_Memory_Degradation_and_Continuity_Profile_v0_1.md`.
- `PAMDC_v0_1_1_Scope_Bootstrap_and_Freshness_Patch.md`.

### Not changed

- CCDP v0.1 root protocol is not superseded.
- CCDP v0.1.1 Hygiene Patch is not superseded.
- CCDP Memory Map schema is not replaced.
- CCDP Witness Event Schema is not replaced.
```

## `RELEASE_NOTES.md` snippet

```markdown
## AMDR / PAMDC Addendum v0.1.1

This release adds a four-document addendum for memory-continuity governance:

- AMDR v0.1: active memory degradation and recalibration while `a` remains present.
- AMDR v0.1.1 patch: lifestream ingestion, Judge integration, write-path health, self-biography, and UI/log observability.
- PAMDC v0.1: post-anchor memory degradation and continuity discipline.
- PAMDC v0.1.1 patch: scope, bootstrap authority, and integrity-vs-freshness correction.

The addendum does not replace CCDP, CMAM, Memory Map, Witness Event Schema, ARL, Soft Safety, or the v0.1.1 Hygiene Patch.
```
