# CCDP AMDR / PAMDC Addendum v0.1.1 — polished delta pack

**Built:** 2026-06-14T16:52:37Z  
**Package type:** delta-only addendum / no CCDP baseline duplication  
**Recommended repository path:** `docs/ccdp/addenda/amdr-pamdc/`  
**Status:** placement-ready Markdown pack

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

## Purpose

This archive contains only the four new AMDR / PAMDC documents that extend the existing CCDP corpus with active-memory degradation, write-path failure, lifestream/Judge integration, and post-anchor continuity discipline.

It is not a replacement for CCDP v0.1, CCDP v0.1.1 Hygiene Patch, the full technical corpus, the Memory Map schema, or the existing public / technical / sensitive split.

## Add exactly these four documents

```text
Active_Memory_Degradation_and_Recalibration_Profile_v0_1.md
AMDR_v0_1_1_Lifestream_Judge_and_Write_Failure_Patch.md
Post_Anchor_Memory_Degradation_and_Continuity_Profile_v0_1.md
PAMDC_v0_1_1_Scope_Bootstrap_and_Freshness_Patch.md
```

## Do not add again

```text
CCDP_v0_1_R_Corpus_Aligned.md
CCDP_v0_1_1_Hygiene_Patch.md
CCDP_Traceability_Matrix_v0_1.md
CCDP_Conformance_Test_Matrix_v0_1.md
CCDP_Witness_Event_Schema_v0_1.md
CCDP_Memory_Map_JSON_Schema_v0_1.md
CCDP_MEMORY_MAP_v0.1.schema.json
FULL_TECHNICAL_CORPUS.md
INDEX.md
README.md
RELEASE_NOTES.md
CHANGELOG.md
GLOSSARY.md
OPEN_ISSUES.md
```

Those are baseline or package-control files already belonging to the CCDP corpus. Re-adding them here would create duplicate authority surfaces.

## Suggested relation to CCDP

```text
CCDP v0.1 full technical corpus
+ CCDP v0.1.1 Hygiene Patch
+ AMDR / PAMDC Addendum v0.1.1
```

AMDR / PAMDC are not child-specific replacements for CMAM, Soft Safety, Memory Map, ARL, or Witness. They are wider memory-continuity profiles that CCDP may reference as an addendum.

## Contents

See:

- `_PACKAGE_CONTROL/PACKAGE_MANIFEST.csv`
- `_PACKAGE_CONTROL/PACKAGE_MANIFEST.json`
- `_PACKAGE_CONTROL/SHA256SUMS.txt`
- `_PACKAGE_CONTROL/PLACEMENT_GUIDE.md`
- `_PACKAGE_CONTROL/DUPLICATE_AVOIDANCE_CHECK.md`
- `_PACKAGE_CONTROL/PDF_RECOMMENDATIONS.md`
