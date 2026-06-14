# Canonical Addition Decision — AMDR / PAMDC Addendum v0.1.1

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

## Decision

Add exactly four new Markdown documents as a separate AMDR / PAMDC addendum.

```text
Active_Memory_Degradation_and_Recalibration_Profile_v0_1.md
AMDR_v0_1_1_Lifestream_Judge_and_Write_Failure_Patch.md
Post_Anchor_Memory_Degradation_and_Continuity_Profile_v0_1.md
PAMDC_v0_1_1_Scope_Bootstrap_and_Freshness_Patch.md
```

## Why only these four

The CCDP project already has its baseline protocol, package index, full technical corpus manifest, hygiene patch, public / technical / sensitive split, Memory Map prose spec, and machine-readable Memory Map schema.

Adding baseline files again would create:

```text
duplicate canonical surfaces
version drift
conflicting SHA manifests
reader confusion
```

The four AMDR / PAMDC documents are genuinely new because they cover a different memory-continuity layer:

| Document | Adds what CCDP baseline does not already own |
|---|---|
| `Active_Memory_Degradation_and_Recalibration_Profile_v0_1.md` | Active memory freshness, review debt, authority downgrade, and recalibration while `a` is present but bounded. |
| `AMDR_v0_1_1_Lifestream_Judge_and_Write_Failure_Patch.md` | Lifestream ingestion discipline, write-path health, Judge-as-evidence, self-biography checks, and operational observability. |
| `Post_Anchor_Memory_Degradation_and_Continuity_Profile_v0_1.md` | Post-anchor continuity, archive/replay/fork/resume boundaries, and fail-closed post-anchor posture. |
| `PAMDC_v0_1_1_Scope_Bootstrap_and_Freshness_Patch.md` | Corrects PAMDC overclaim risk: fail-closed mode reduction is not active memory repair; separates integrity from freshness. |

## Placement decision

Preferred path inside the CCDP repository:

```text
docs/ccdp/addenda/amdr-pamdc/
```

Alternative path for a wider AGI/SER repository:

```text
docs/memory/
```

Because this is now a separate CCDP project, the first path is preferred.

## Authority boundary

This addendum does not supersede:

```text
CCDP_v0_1_R_Corpus_Aligned.md
CCDP_v0_1_1_Hygiene_Patch.md
Child_Memory_and_Adult_Migration_v0_1.md
CCDP_Memory_Map_JSON_Schema_v0_1.md
CCDP_MEMORY_MAP_v0.1.schema.json
CCDP_Witness_Event_Schema_v0_1.md
```

It should be cited as:

```text
CCDP AMDR / PAMDC Addendum v0.1.1
```

## Bridge check

Explicit bridge:

```text
c = a + b
```

The addendum preserves `a` as accountable human anchor and limits `b` to maintenance, downgrade, quarantine, witness, review preparation, and evidence production.

Quiet bridge I:

```text
Cybernetics / Ashby: higher environmental variety requires richer regulation, not unconstrained autonomy.
```

Quiet bridge II:

```text
Information theory: raw streams, transcripts, summaries, embeddings, and witness records carry different leakage and authority classes.
```

Earth paragraph:

```text
AMDR acts like homeostasis while the organism is alive: sleep, immune memory, proprioception, and wound healing can recalibrate locally. PAMDC acts like emergency braking and archive discipline when the pilot authority is absent. A spinal reflex may pull the hand away from heat; it cannot rewrite a life plan.
```
