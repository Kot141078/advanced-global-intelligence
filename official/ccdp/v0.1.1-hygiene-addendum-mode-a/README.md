# CCDP v0.1.1 Hygiene Addendum — Mode A DOI-Safe Patch Pack

**Version:** v0.1.1
**Release date:** 2026-06-13
**Author:** Kotov Ivan
**Location:** Bruxelles, Belgium
**DOI:** 10.5281/zenodo.20680938
**Zenodo record:** https://zenodo.org/records/20680938
**License:** MIT License
**Patch mode:** Mode A / addendum-only

## Purpose

This folder mirrors the Zenodo-published CCDP v0.1.1 Hygiene Addendum for the Child-c Development Protocol corpus.

The package uses Mode A / addendum-only patching. It does not mutate, rewrite, or replace the DOI-bound CCDP v0.1 baseline artifacts. Instead, it provides a controlled hygiene addendum defining how the CCDP v0.1 baseline should be read together with v0.1.1 release-control corrections.

Current operational reading:

```text
CCDP v0.1 baseline + CCDP v0.1.1 Hygiene Addendum
```

## Contents

* `package/` — extracted addendum package with Markdown, PDFs, manifest, checksums, and LICENSE.
* `zenodo/` — exact Zenodo ZIP package and ZIP checksum file.

## Integrity

Final Zenodo ZIP SHA-256:

```text
4f1b574d769ecccfc74561288df2c285663f522177eb57628db308b328d594ff  CCDP_v0_1_1_Hygiene_Addendum_Mode_A_WITH_PDF.zip
```

The package contains:

* 12 Markdown files
* 12 matching academic PDFs
* `ADDENDUM_MANIFEST.json`
* `SHA256SUMS`
* `LICENSE`

## DOI-safe patching rule

This addendum does not edit the DOI-bound CCDP v0.1 baseline. It must be read as a correction / hygiene layer next to the frozen v0.1 corpus.

Do not silently mutate the baseline witness. Attach the correction and make current readers follow it.

## Citation

Kotov Ivan. *CCDP v0.1.1 Hygiene Addendum — Mode A DOI-Safe Patch Pack*. Zenodo, 2026. DOI: 10.5281/zenodo.20680938.

## Distribution note

This is a corpus-control and release-hygiene artifact. It does not introduce a new child-safety mechanism, does not replace legal / clinical / jurisdictional review, and does not modify the previously published baseline documents.
