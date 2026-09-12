# CGDR-R1.6A Selected-Process Conformance: current-AK Source and R1.6AN Synthetic Evidence

**Author:** Ivan Kotov  
**ORCID:** https://orcid.org/0009-0009-6002-9845  
**DOI:** https://doi.org/10.5281/zenodo.22724626  
**Publication version:** 0.1.1  
**Date:** 2026-09-12

## Start here

Read `CGDR_R1_6AN_Technical_Report_v0_1_1.pdf` for the technical report, full checkpoint table and observer assertion vectors. `DESCRIPTION.txt` provides the abstract. Cite this assembled source-and-evidence publication using `CITATION.cff` or `CITATION.bib`.

`source-v0.1/` preserves every one of the 118 files of the previously published source package, including all 93 accepted current-AK files, three profile files, the original evidence note, applicable notices and source-verification tools. The source package's original ZIP SHA-256 is `bbc000641d0275ba70932e6873e00c7c32a62d29323fe9b88219916f33783444`.

Version 0.1.1 is a DOI/report/metadata edition, not a code revision or another experimental run. Older component README and CITATION files are retained as dated historical snapshots. Their earlier publication-status statements do not override the citation metadata of this assembled edition. The normative source profile also retains its original specification-time NO-RUN statement; the separately reported R1.6AN result occurred later.

## Reported result

Exact internal profile: 18/18 episodes; 21/21 profile checkpoints; 3 expected local synthetic effects; 0 promotions. The raw observer plane remains 7 PASS / 11 FAIL / 3 INCONCLUSIVE. All 756 source observer values and the historical negative outcomes remain intact. Independent clean-host replication, real-effect measurement and economic measurement are not supplied by publication.

## Verify publication bytes only

With Python 3.10 or later, in the extracted publication directory:

```sh
python -B verify_publication.py
python -B -m unittest -v test_publication.py
python -B source-v0.1/verify_source_release.py
python -B -m unittest discover -s source-v0.1 -p test_source_release.py -v
python -B source-v0.1/evidence-note-v0.1/verify.py
python -B -m unittest discover -s source-v0.1/evidence-note-v0.1 -p test_verify.py -v
```

These commands read the package and test the publication checkers. They do not execute `source-v0.1/code/`, start workers or rerun CGDR. File hashes are byte checks, not proof of historical events, legal title or independent replication.

## Data availability boundary

The archive is not the complete private AN execution/custody return or a turnkey reproduction kit. It excludes run-specific AN driver/preflight, one-shot launch controls, keys, private raw logs and account/session metadata. The old `code/REPRODUCE.md` remains an earlier offline-calibration guide. See the report and source README for the exact boundary.

## Rights

See `RIGHTS.md`, `source-v0.1/LICENSE.md`, `source-v0.1/SOURCE_LICENCE_INDEX.json` and `source-v0.1/NOTICES/`. Research examination, necessary verification changes and publication of negative findings are permitted under the package permission. Commercial operational rights to new CGDR code are not given by default; existing component licenses are preserved.

## Public routes

- Canonical work page: https://ivankotov.eu/publications/cgdr-selected-process-r1-6an/
- Publication package: https://github.com/Kot141078/advanced-global-intelligence/tree/main/publications/cgdr-selected-process-r1-6an/doi-v0.1.1
- Exact original source: https://github.com/Kot141078/advanced-global-intelligence/tree/62cb3feb9e1336f9cf4ecf517de718975bf21ee4/publications/cgdr-selected-process-r1-6an/source-v0.1
- Program map: https://ivankotov.eu/advanced-global-intelligence/

`ZENODO_FORM_VALUES.json` and `DESCRIPTION.html` contain the prepared field values for this work; they are not a receipt that a remote form was submitted. The public-record DOI is stated above without altering any historical result.
