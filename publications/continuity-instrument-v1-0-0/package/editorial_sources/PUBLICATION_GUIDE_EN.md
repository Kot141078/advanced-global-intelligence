# Continuity Instrument v1.0.0: English Publication and Reading Guide

**Author: Ivan Kotov**  
ORCID: https://orcid.org/0009-0009-6002-9845  
**Editorial edition:** `academic-pdf-2`  
**Underlying implementation:** `1.0.0`, original source build `_02`  
**Status at preparation:** no CI DOI assigned; empirical qualification not established.

This editorial companion was prepared at the author's request. It provides a complete English reading route through six English PDFs and retains the Russian explanatory paper as a supplement. The English explanatory paper is the full counterpart of the Russian paper. Editorial edition `academic-pdf-2` corrects the language presentation and completeness of the academic companion; it does not change source version `1.0.0`, original build `_02`, the reference code, or the evidence. The separately performed publication-readiness review is identified below and is not attributed to Ivan Kotov as an independent reviewer.

## 1. Reading map

All PDFs are in `PDFs/`. Read the six English volumes in the order below for a complete account of the contribution, technical contract, implementation, evidence limits, rights, and publication procedure. Reading Russian is not required. The two language versions explain the same contribution and do not provide separate experimental confirmations.

| File | Purpose and source relationship |
|---|---|
| `01_CI_Explanatory_Paper_EN.pdf` | Full English counterpart of the Russian explanatory paper: problem, instrument, operational interpretation, examples, and evidence limits. Start here. |
| `03_CI_Technical_Specification_EN.pdf` | English presentation of `CI_SPECIFICATION.md`, `CONTINUITY_OBSERVABLES.md`, `RECOGNITION_PROFILE.md`, and `TERMINOLOGY.md`. |
| `04_CI_Implementation_and_Reproducibility_EN.pdf` | English implementation and reproduction volume. Part I: original implementation README; Part II: original `REPRODUCIBILITY.md`; Part III and separately labelled editorial notes provide accompanying guidance. Component rights differ between these parts. |
| `05_CI_Evidence_Claims_and_Limitations_EN.pdf` | English claim map, limitations, and human-readable rendering of `EVIDENCE_STATUS.json`; preserves the negative R160/R161 results. |
| `06_CI_Rights_and_Citation_EN.pdf` | English component-rights statement, bibliographic identity, citation instructions, and external-material boundaries. |
| `07_CI_Publication_Guide_EN.pdf` | This guide: reading order, version identity, known issues, and manual deposit instructions. |
| `02_CI_Explanatory_Paper_RU.pdf` | Optional Russian supplement, preserved byte-for-byte from `academic-pdf-1`. Its original edition-1 front matter is deliberately retained. |

The retained Russian PDF remains an edition-1 document within the `academic-pdf-2` package; its title-page edition number is not an inconsistency or a claim that it was revised. The outer manifest records the current package identity. The complete original machine-readable material remains in `source_original/`; editable editorial Markdown is in `editorial_sources/`. Integrity utilities and receipts belong in `verification/`.

## 2. File precedence and source identity

The original `_02` archive is the byte-level reference for the source release. Its exact extracted 22 files retain their original content and rights. The source files define the published implementation and contracts; PDFs are reading editions. If an editorial rendering or translation disagrees with a source file, use the source file, report the discrepancy, and preserve the original. A known issue disclosed here does not silently amend the source.

| Original source object | Exact value |
|---|---|
| Path | `source_original/CI_CONTINUITY_INSTRUMENT_V1_0_0.zip` |
| Bytes | `50765` |
| SHA-256 | `be87dd926ed96e91e8de25bae2e18666f74ac738b173379ddc0092f98563f663` |
| Extracted root | `source_original/Continuity_Instrument_v1.0.0/` |
| Original files | `22` |

The enclosing academic package is `CI_CONTINUITY_INSTRUMENT_V1_0_0_ACADEMIC_EN_PACKAGE_20261025.zip`. It necessarily has a different size and checksum from the source ZIP and the first academic package. Its exact checksum is supplied outside that ZIP in the delivery sidecar. Never use the `_02` checksum for the enclosing academic package.

The outer `PACKAGE_MANIFEST.json` identifies this editorial edition and its contents. The outer `SHA256SUMS.txt` covers every payload file and the outer manifest, excluding itself. The original nested manifest and checksum index retain their original scope. Checksums establish byte consistency; they do not authenticate scientific assertions or prove the truth of supplied records.

## 3. Evidence ceiling and known issues

CI transforms caller-supplied records under documented admission, duration, branch, lineage, and uncertainty rules. It does not itself establish input truth or admissibility. R157 supplies bounded open-synthetic predecessor evidence. R160 and R161 remain consumed negative local-evaluator attempts; neither achieved its frozen qualification threshold. No historical qualification attempt is reopened by this edition.

The separate review [R1] reported the following nonblocking findings for the limited source/reference publication. They remain visible here without modifying `_02`:

| Finding | Exact limitation and reading instruction |
|---|---|
| F-01: CLI Unicode handling | An input containing an unpaired Unicode surrogate can raise an uncaught `UnicodeEncodeError`, return exit status `1`, and produce no output file, instead of the documented controlled invalid-input exit `2`. This is an error-handling defect, not a successful result. |
| F-02: machine-readable licence scope | `.zenodo.json` contains one global `cc-by-4.0` licence field. Its prose notes describe component boundaries, but that field does not encode them. Use the two rights entries and explicit public description below for the manual deposit; do not treat this JSON as an unrestricted automatic-import recipe. |
| F-03: stale working-directory instruction | The implementation README names `publication_draft/`, which is absent from the archive. The actual working directory is `Continuity_Instrument_v1.0.0/`. The main reproducibility document supplies the discovery command shown below. The alternative module command passed in the review environment, but can be shadowed by an installed package named `tests`. |
| F-04: duration-eligible participation | For this reference implementation, `I_verified` contains intervals that are both admitted and `eligible_for_duration=true`. An admitted, duration-ineligible record remains in admission counts but does not contribute to `I_verified`, duration, or coverage of unexplained gaps. Read the general specification together with this documented implementation policy. |

The review reported eight focused tests passing on Python 3.12.14/Linux. Those are bounded implementation checks, not eight scientific experiments or a new historical Windows/KOT qualification. From the extracted source root, the documented discovery command is:

```text
python -m unittest discover -s tests -p "test_*.py" -v
```

The source rights statement grants no general code-reuse licence. Describing a reproduction procedure does not extend that grant. Historical evidence archives, private corpus text, runtime binaries, and model files are not redistributed in this edition; their hashes do not provide access to their contents. No identity, consciousness, personhood, general evaluator validity, operational approval, or BACON compatibility is established.

## 4. Rights and public-description text

Retain two separately scoped rights entries in Zenodo: CC BY 4.0 and the custom statement `Copyright © 2026 Ivan Kotov. All rights reserved. No license grant.` Zenodo supports multiple licences and custom rights [Z1]. The new explanatory prose is CC BY 4.0. Original component rights remain unchanged.

Use the following text in the public Description, together with the scientific abstract:

> This is the English academic PDF companion edition `academic-pdf-2` of Continuity Instrument (CI) source version 1.0.0, build _02. Six English PDFs provide a complete reading route, including a full English counterpart of the explanatory paper. A seventh PDF preserves the Russian paper byte-for-byte, with its original edition-1 front matter, as a supplement. The package also includes editorial sources, the unchanged original source archive and its exact extracted files, and integrity metadata. Edition 2 is a language and editorial correction; it does not change the reference code or evidence. R157 is bounded open-synthetic predecessor evidence; R160 and R161 remain negative qualification attempts. Scientific qualification is not established.
>
> Component rights: New explanatory prose, the retained Russian paper, and the original scientific-text and metadata files listed in LICENSES_AND_THIRD_PARTY.md are licensed under CC BY 4.0. Original REFERENCE_IMPLEMENTATION/ files, including its README and schemas, and tests/test_ci_profile.py are Copyright © 2026 Ivan Kotov. All rights reserved. No license grant. The new `build/*.py`, `verification/verify_package.py`, and `examples/*.json` also retain this no-grant code/data posture. These restrictions also apply to the reproduction of the original implementation README in Part I of PDF 04. Part II of PDF 04, reproducing REPRODUCIBILITY.md, Part III, and its separately identified editorial notes remain CC BY 4.0. The presence of a CC BY entry does not relicense the implementation, schemas, tests, or restricted README. Referenced external material retains its own rights. The software is publicly readable but is not offered under an open-source reuse licence.
>
> The historical R157/R160/R161 evidence archives remain separately controlled and are not included. The unchanged source retains a known CLI limitation: an unpaired Unicode surrogate can cause an uncaught UnicodeEncodeError and exit status 1 rather than the documented invalid-input status 2. This edition neither repairs that defect nor raises the qualification status.
>
> Zenodo record metadata is available under Zenodo's CC0 metadata policy, separately from the rights of the deposited files.

CC0 for the public record metadata does not place the source archive or PDFs in the public domain [Z2].

## 5. Manual Zenodo metadata and citation

| Field | Value or instruction |
|---|---|
| Resource type | Software: a mixed source/reference and explanatory publication package. |
| Title | Continuity Instrument (CI): Evidence-Bound Measurement of Governed Continuity in Long-Lived AI Systems, v1.0 - English Academic Edition |
| Version | `1.0.0`; state editorial edition `academic-pdf-2` separately in Description. |
| Creator | Family name: `Kotov`; given name: `Ivan`. |
| ORCID | `0009-0009-6002-9845`. |
| Language | English is the primary reading language; Russian is retained as a supplementary paper. The original source documents are English. |
| Publication date | Actual date of first public availability, not an inferred earlier research date. |
| Visibility | Public, preserving the component rights above. |
| Rights | Two entries with the exact scopes in section 4. |
| Keywords and related records | Preserve the original `.zenodo.json` keywords and `references` relations; do not use a cited work's DOI as this package's DOI. |
| Upload | The final academic package with its externally supplied checksum. |

No CI DOI has been assigned during preparation. If none exists at deposit time, select the corresponding “No” option and let Zenodo reserve or assign one. A reserved DOI becomes registered on publication [Z3]. After publication, download and verify the deposited ZIP and record the version DOI, concept DOI, public URL, byte length, and SHA-256. Do not rebuild a frozen archive merely to insert its DOI.

Suggested citation before DOI assignment:

> Kotov, Ivan. (2026). *Continuity Instrument (CI): Evidence-Bound Measurement of Governed Continuity in Long-Lived AI Systems, v1.0*. Source version 1.0.0, build _02; English academic PDF companion edition academic-pdf-2. Research-software specification and reference package.

Add the assigned **version DOI** to this citation after deposit verification. The original `CITATION.cff` continues to describe the source release. The papers are not described as journal-accepted or externally peer-reviewed.

<!-- PAGEBREAK -->

## 6. Integrity verification

After extracting the outer package, run from its root. On Linux:

```bash
set -eu
sha256sum -c SHA256SUMS.txt
python3 verification/verify_package.py
sha256sum source_original/CI_CONTINUITY_INSTRUMENT_V1_0_0.zip
wc -c < source_original/CI_CONTINUITY_INSTRUMENT_V1_0_0.zip
```

The last two results must equal the `_02` hash and `50765` bytes in section 2. On PowerShell:

```powershell
$ErrorActionPreference = 'Stop'
$sourceRelative = 'source_original/CI_CONTINUITY_INSTRUMENT_V1_0_0.zip'
$sourceArchive = Join-Path $PWD $sourceRelative
$expectedSha256 = 'be87dd926ed96e91e8de25bae2e18666f74ac738b173379ddc0092f98563f663'
if ((Get-Item -LiteralPath $sourceArchive).Length -ne 50765) {
    throw 'Original source ZIP size mismatch'
}
$actualHash = Get-FileHash -LiteralPath $sourceArchive -Algorithm SHA256
$actualSha256 = $actualHash.Hash.ToLowerInvariant()
if ($actualSha256 -ne $expectedSha256) {
    throw 'Original source ZIP SHA-256 mismatch'
}
python verification/verify_package.py
if ($LASTEXITCODE -ne 0) { throw 'Academic package verification failed' }
```

Also compare the outer ZIP's SHA-256 with its external delivery sidecar before extraction or upload. Stop on a mismatch; do not substitute another build or repair the evidence silently.

## Sources

**[R1] Review findings source:** *Independent publication-readiness review of CI v1.0.0 build _02*, ChatGPT-assisted review, 25 October 2026; file `CI_V1_0_0_BUILD_02_PUBLICATION_REVIEW_20261025.md`, sections 6 and 11. SHA-256: `147bc8c365833fb77164013dde0a6068f7a320d73f86e9a28dbabe7b2a000e2d`. A public findings extract is included as verification/SOURCE_REVIEW_PUBLIC_EXTRACT.md. This guide attributes the findings to that separate review. The full review contains private operational material and is not redistributed; only the bounded findings reproduced here are included.

**[Z1] Zenodo rights:** https://help.zenodo.org/docs/deposit/describe-records/licenses/ and https://help.zenodo.org/docs/about/whats-new/

**[Z2] Zenodo metadata policy:** https://about.zenodo.org/policies/

**[Z3] Zenodo DOI procedure:** https://help.zenodo.org/docs/deposit/describe-records/reserve-doi/
