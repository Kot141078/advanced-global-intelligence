# Duplicate Avoidance Check — AMDR / PAMDC Addendum v0.1.1

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

## Result

PASS: this pack is delta-only.

It includes only:

```text
Active_Memory_Degradation_and_Recalibration_Profile_v0_1.md
AMDR_v0_1_1_Lifestream_Judge_and_Write_Failure_Patch.md
Post_Anchor_Memory_Degradation_and_Continuity_Profile_v0_1.md
PAMDC_v0_1_1_Scope_Bootstrap_and_Freshness_Patch.md
```

## Do not include baseline CCDP files in this addendum

The existing CCDP project already contains the baseline protocol and corpus-control files. Re-adding them here would create duplicate authority.

Do not include:

```text
README.md
INDEX.md
GLOSSARY.md
CANONICAL_READING_ORDER.md
RELEASE_NOTES.md
CHANGELOG.md
OPEN_ISSUES.md
FULL_TECHNICAL_CORPUS.md
PACKAGE_MANIFEST_CCDP_v0.1.json
PACKAGE_MANIFEST_CCDP_FULL_TECHNICAL_v0.1.json
CITATION.cff
CITATION_FULL_TECHNICAL.cff
CCDP_v0_1_R_Corpus_Aligned.md
CCDP_v0_1_1_Hygiene_Patch.md
CCDP_Package_Index_and_Reading_Order_v0_1.md
CCDP_Traceability_Matrix_v0_1.md
CCDP_Conformance_Test_Matrix_v0_1.md
CCDP_Witness_Event_Schema_v0_1.md
CCDP_Memory_Map_JSON_Schema_v0_1.md
CCDP_MEMORY_MAP_v0.1.schema.json
```

## About `CCDP_MEMORY_MAP_v0.1.schema.json`

This schema belongs to the existing CCDP baseline schema surface. It should live at:

```text
docs/ccdp/schemas/CCDP_MEMORY_MAP_v0.1.schema.json
```

It is not part of the AMDR / PAMDC addendum unless the repository is missing the baseline schema entirely. If it is missing, add it to `schemas/`, not to `addenda/amdr-pamdc/`.

## About source notes

Do not include:

```text
Оформление_вопроса_в_Markdown_формате.txt
Посты.txt
```

These are source / narrative / working materials, not canonical addendum files.

## Previous broad pack status

Do not publish or reuse broad placement packs that include CCDP baseline files. They are superseded by this delta-only pack.
