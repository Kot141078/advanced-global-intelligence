# PDF Recommendations — AMDR / PAMDC Addendum v0.1.1

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

## Produce PDF for these two core profiles

```text
Active_Memory_Degradation_and_Recalibration_Profile_v0_1.md
Post_Anchor_Memory_Degradation_and_Continuity_Profile_v0_1.md
```

Reason: these are reader-facing, load-bearing profile documents.

## Produce audit PDFs for these two patches

```text
AMDR_v0_1_1_Lifestream_Judge_and_Write_Failure_Patch.md
PAMDC_v0_1_1_Scope_Bootstrap_and_Freshness_Patch.md
```

Reason: these are release-control / correction patches. PDF is useful for audit trail, but Markdown remains the canonical working format.

## Do not make PDFs for `_PACKAGE_CONTROL/` by default

Package-control files are placement guidance, manifests, and duplicate-avoidance notes. They can remain Markdown/CSV/JSON.

## Rule

If PDFs are generated later, regenerate:

```text
_PACKAGE_CONTROL/SHA256SUMS.txt
_PACKAGE_CONTROL/PACKAGE_MANIFEST.csv
_PACKAGE_CONTROL/PACKAGE_MANIFEST.json
```
