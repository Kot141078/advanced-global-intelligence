# Final QA report - MOT-c v0.1

**DOI:** `10.5281/zenodo.22060517`  
**Build status:** `PASS - READY_FOR_ZENODO_UPLOAD`  
**Review date:** 2026-08-22

## Canonical-source checks

- English Foundation Theory Markdown complete through section 24, appendices, references, and authorial premises.
- Russian Foundation Theory Markdown complete through section 24, appendices, references, and authorial premises.
- English/Russian numbered-section parity confirmed.
- Markdown code fences balanced.
- Figure references resolve to language-specific PNG files.
- DOI and CC BY 4.0 appear consistently in public metadata and rendered PDFs.

## PDF build and visual review

All PDFs were regenerated directly from their Markdown sources through Pandoc HTML5 plus WeasyPrint paged-media rendering. The publication PDFs are searchable, unencrypted, non-scanned A4 documents.

| PDF | Pages | Visual review |
|---|---:|---|
| `MOT_c_Foundation_Theory_v0_1_EN.pdf` | 51 | PASS |
| `MOT_c_Foundation_Theory_v0_1_RU.pdf` | 52 | PASS |
| `MOT_c_FORMAL_CORE_v0_1_EN.pdf` | 10 | PASS |
| `MOT_c_FORMAL_CORE_v0_1_RU.pdf` | 11 | PASS |
| `MOT_c_COMPARATIVE_LANDSCAPE_v0_1.pdf` | 8 | PASS |

**Total visually reviewed:** 132 pages.

The review confirmed:

- no unintended blank pages;
- no heading stranded above a large unused page area;
- no broken or flattened Markdown tables;
- table continuation across pages remains legible;
- no clipped text or overlapping elements;
- no missing Cyrillic or Latin glyphs;
- figures remain within the page frame and captions remain attached;
- headers, footers, DOI, license, and page numbering are consistent;
- cover and contents pages use deliberate white space only.

## PDF preflight

All five PDFs opened successfully, were unencrypted, were detected as text documents rather than scanned images, and produced no preflight warnings.

## Machine-readable artifacts

- all JSON files parse;
- schemas use JSON Schema Draft 2020-12;
- synthetic examples validate against their corresponding schemas;
- `.zenodo.json`, `CITATION.cff`, and `ZENODO_METADATA.md` agree on title, author, DOI, version, date, resource type, and license.

## Deposit boundary

Canonical source-of-record files are Markdown. PDF files are the verified reader renderings. DOCX files are deliberately excluded from the Zenodo package because they are not canonical and were not needed for the public deposit.
