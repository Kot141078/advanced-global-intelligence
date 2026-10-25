# Continuity Instrument (CI) v1.0.0

**Ivan Kotov** · Independent researcher, Brussels, Belgium · [ORCID](https://orcid.org/0009-0009-6002-9845)  
Published 25 October 2026 · Source build `_02` · English academic edition `academic-pdf-2`

[Version DOI](https://doi.org/10.5281/zenodo.23651305) · [Zenodo record](https://zenodo.org/records/23651305) · [Author's explanation](https://ivankotov.eu/publications/continuity-instrument-v1-0-0/) · [Citation](CITATION.cff) · [Machine-readable publication record](PUBLICATION_RECORD.json)

CI provides a research specification and a small deterministic reference program for describing the evidence available about an AI system's participation over time. It keeps verified participation, known pauses, unexplained gaps, replay, restoration, forks, and changes of memory, governance, witnesses, and authority separate. Its purpose is to make a continuity report explicit about what was observed, how it was interpreted, and what remains unknown.

This directory is the canonical GitHub home for the published **CI v1.0.0 English academic package**. The complete deposit is mirrored without changing its bytes. The current publication identifiers and citation are supplied in the wrapper files at this directory's root. CI means **Continuity Instrument** throughout this package.

## Read or download

- **Start with the explanation:** [English PDF](package/PDFs/01_CI_Explanatory_Paper_EN.pdf) or [complete English article](package/editorial_sources/CI_EXPLAINED_EN.md).
- **Download the complete published package:** [ZIP](release/CI_CONTINUITY_INSTRUMENT_V1_0_0_ACADEMIC_EN_PACKAGE_20261025.zip) · [SHA-256 sidecar](release/CI_CONTINUITY_INSTRUMENT_V1_0_0_ACADEMIC_EN_PACKAGE_20261025.zip.sha256) · [direct Zenodo download](https://zenodo.org/records/23651305/files/CI_CONTINUITY_INSTRUMENT_V1_0_0_ACADEMIC_EN_PACKAGE_20261025.zip?download=1).
- **Browse the exact extracted package:** [package/](package/), including all original sources, schemas, tests, seven PDFs, editorial sources, manifests, and checksums.
- **Русское пояснение:** [PDF](package/PDFs/02_CI_Explanatory_Paper_RU.pdf) · [полный текст](package/editorial_sources/CI_EXPLAINED_RU.md). The Russian supplement is preserved from `academic-pdf-1`; the six English PDFs provide the complete reading route in `academic-pdf-2`.

### Academic reading map

| Document | What it explains | Pages |
|---|---|---:|
| [01 — Explanatory paper, English](package/PDFs/01_CI_Explanatory_Paper_EN.pdf) | Purpose, inputs, practical applications, interval example, and measurement limits | 15 |
| [02 — Explanatory paper, Russian](package/PDFs/02_CI_Explanatory_Paper_RU.pdf) | Preserved supplementary explanation in Russian | 15 |
| [03 — Technical specification](package/PDFs/03_CI_Technical_Specification_EN.pdf) | Specification, observables, recognition profile, and terminology | 15 |
| [04 — Implementation and reproducibility](package/PDFs/04_CI_Implementation_and_Reproducibility_EN.pdf) | Reference transformation, reproduction procedure, and its limits; mixed rights by section | 8 |
| [05 — Evidence, claims, and limitations](package/PDFs/05_CI_Evidence_Claims_and_Limitations_EN.pdf) | Preserved evidence status, permitted claims, negative results, and uncertainties | 10 |
| [06 — Rights and citation](package/PDFs/06_CI_Rights_and_Citation_EN.pdf) | Authorship and component rights; read the current DOI citation below alongside this preparation-time document | 7 |
| [07 — Publication guide](package/PDFs/07_CI_Publication_Guide_EN.pdf) | Package structure and the historical manual-deposit instructions | 8 |

For the original normative source, open [CI_SPECIFICATION.md](package/source_original/Continuity_Instrument_v1.0.0/CI_SPECIFICATION.md). The [input schema](package/source_original/Continuity_Instrument_v1.0.0/REFERENCE_IMPLEMENTATION/schemas/ci-profile-input-v1.schema.json), [output schema](package/source_original/Continuity_Instrument_v1.0.0/REFERENCE_IMPLEMENTATION/schemas/ci-profile-output-v1.schema.json), [implementation](package/source_original/Continuity_Instrument_v1.0.0/REFERENCE_IMPLEMENTATION/ci_profile.py), and [tests](package/source_original/Continuity_Instrument_v1.0.0/tests/test_ci_profile.py) are preserved under their original rights.

## What CI works with

The current reference implementation takes **prepared JSON records for one declared subject, branch, and observation window**. Its inputs include a time axis, witnesses, participation intervals, evidenced pauses, typed events, separate lineages, irreversible transitions, uncertainty, and a claim ceiling. The program checks the implemented structural and relational conditions, organizes the records deterministically, and calculates interval coverage. The full [English article](package/editorial_sources/CI_EXPLAINED_EN.md) explains the difference between the normative admission procedure and the narrower checks implemented in code.

Source observations must be collected and admitted outside the program. A study could prepare records from process logs, documented interactions, memory revisions, or operator decisions, provided the evidence supports the chosen participation predicate. This release supplies no universal importer or built-in connection to Ollama, a cloud API, an agent framework, or a monitoring service. Reference strings are retained; the program does not fetch the referenced objects or authenticate witnesses and authority.

This makes the package useful for designing a reproducible reporting procedure, inspecting continuity claims, and comparing carefully scoped histories. A model replacement, restored state, or fork can be represented without automatically treating every descendant or archived message as one uninterrupted history. The specification does not establish that an adapter, evidence source, or real deployment already satisfies these requirements.

## How the result should be read

The principal result is a sixteen-coordinate vector, called evidence-bound continuity age or formation depth in the specification. It retains witness boundaries, participation intervals and their union duration, pauses and gaps, replay/fork/restore/cold-wake events, four separate lineages, irreversible transitions, and uncertainty. These are structured observations and declared interpretations, not a biological age or a universal maturity score.

The published [sixty-minute teaching example](package/examples/README.md) illustrates the arithmetic. Participation intervals `[0,20)`, `[10,30)`, and `[50,60)` contribute **40 minutes** after overlap is removed. An evidenced pause `[30,40)` contributes 10 minutes. The remaining `[40,50)` is a 10-minute unexplained gap. This synthetic example is separate from every historical qualification episode. A hash of the resulting `formation_depth_vector` binds that vector's bytes; it does not attest to the entire report or the truth of its sources.

## Publication status and evidence limits

**Publication status: published. Empirical qualification: `NOT_ESTABLISHED`.** These are separate fields in [PUBLICATION_RECORD.json](PUBLICATION_RECORD.json).

- R157 is retained as a bounded **open-synthetic** predecessor result.
- R160 and R161 remain **negative, consumed qualification attempts**. Their no-replay boundary and the absence of real-system qualification are preserved.
- The [public source-review extract](package/verification/SOURCE_REVIEW_PUBLIC_EXTRACT.md) records eight focused tests that passed during the earlier bounded review. This GitHub integration does not rerun those tests or the historical evaluations.
- The same extract discloses the known unpaired-Unicode-surrogate error: canonical UTF-8 serialization can raise an uncaught `UnicodeEncodeError`, yielding exit 1 instead of the documented invalid-input exit 2. The frozen implementation is unchanged.

CI does not establish consciousness, personhood, identity preservation, lawful succession, provider attestation, operational approval, general evaluator validity, or BACON compatibility. Structured output and valid checksums cannot independently establish that the supplied events occurred. The [evidence and limitations PDF](package/PDFs/05_CI_Evidence_Claims_and_Limitations_EN.pdf) and original [EVIDENCE_STATUS.json](package/source_original/Continuity_Instrument_v1.0.0/EVIDENCE_STATUS.json) give the preserved account; private evidence archives and raw private corpus material are not included in this package.

## Publication identity and metadata precedence

| Object | Role |
|---|---|
| Version DOI `10.5281/zenodo.23651305` | Cite this exact published version |
| Concept DOI `10.5281/zenodo.23651304` | Identifies the Zenodo version family; use the version DOI for reproducible citation |
| Source version `1.0.0`, build `_02` | Identity of the original specification and reference implementation |
| Editorial edition `academic-pdf-2` | English academic reading package; does not increment the implementation version |
| `package/**` and `release/**` | Frozen deposited bytes, including preparation-time instructions and metadata |
| Root `CITATION.cff`, `PUBLICATION_RECORD.json`, `codemeta.json`, `schema.org.jsonld` | Current published identity, machine discovery, DOI, rights, and links |

The frozen files inside `package/` intentionally retain their original preparation-time statements such as `doi_assigned: false`, `doi_assigned_at_preparation: false`, and suggested prepublication citations. These describe the state when the deposit was assembled. They do not supersede the published DOI above. The historical `.zenodo.json` is not a new-deposit instruction and its single license field does not describe the rights of the whole package.

GitHub `main` is a moving discovery surface. The Zenodo version record and the exact archive digest identify the deposited object. For a fixed GitHub citation, use the commit-specific URL of the integration; do not equate a GitHub-generated repository ZIP with the deposited ZIP.

## Integrity

| Artifact | Bytes | SHA-256 |
|---|---:|---|
| Complete English academic ZIP | 1,097,821 | `0e97eb3b8b54b091a35c2a0cc0d702efa9f781e10d1ac0773d42796e1047a659` |
| Original CI source build `_02` ZIP | 50,765 | `be87dd926ed96e91e8de25bae2e18666f74ac738b173379ddc0092f98563f663` |

The extracted academic package contains **58 files**, including **7 PDFs / 78 pages** and all **22 original source files**. Its original [manifest](package/PACKAGE_MANIFEST.json) and [checksum list](package/SHA256SUMS.txt) remain unchanged. [MIRROR_MANIFEST.json](MIRROR_MANIFEST.json) and [SHA256SUMS.txt](SHA256SUMS.txt) additionally cover the GitHub wrapper and the mirrored archive.

To check downloaded bytes from this directory, run `sha256sum -c SHA256SUMS.txt`. To check only the original archive sidecar, run `sha256sum -c CI_CONTINUITY_INSTRUMENT_V1_0_0_ACADEMIC_EN_PACKAGE_20261025.zip.sha256` from `release/`. These commands verify integrity; they do not run the CI program or establish empirical qualification.

## Rights and authorship

Scientific author and copyright holder: **Ivan Kotov**. The author credits ChatGPT-assisted editorial preparation in the frozen rights document; this is not additional scientific authorship or independent human peer review.

The package has **component-specific rights**. Author scientific prose and descriptive metadata are CC BY 4.0. The original implementation directory, including its README and schemas, the original test file, new Python build and verification code, example JSON, and **PDF 04 Part I** retain **all rights reserved, no license grant**. PDF 04 Parts II and III and distinct editorial notes are CC BY 4.0. Embedded font material retains its separate terms. The new wrapper prose and descriptive metadata are CC BY 4.0.

Read [LICENSES.md](LICENSES.md) for the exact scope. The repository's general MIT license does not override these terms. Public access to code does not make the entire package open source.

## Citation

> Kotov, Ivan. (2026). *Continuity Instrument (CI): Evidence-Bound Measurement of Governed Continuity in Long-Lived AI Systems, v1.0 — English Academic Edition*. Source version 1.0.0, build `_02`; academic companion edition `academic-pdf-2`. Zenodo. https://doi.org/10.5281/zenodo.23651305

Machine readers should use the [current CFF](CITATION.cff), [publication record](PUBLICATION_RECORD.json), [CodeMeta](codemeta.json), or [Schema.org record](schema.org.jsonld). Each identifies the same published work and preserves the component-rights boundary.

## Related corpus reading

CI cites the [Theoretical Core](https://doi.org/10.5281/zenodo.20679718), [Temporal AI Presence](https://doi.org/10.5281/zenodo.22070960), [Personality Formation](https://doi.org/10.5281/zenodo.20648731), [C-Calculus](https://doi.org/10.5281/zenodo.21205427), [Beacon](https://doi.org/10.5281/zenodo.18933553), and [Entity vs Profile](https://doi.org/10.5281/zenodo.21204415). These are **References** relations. They do not make CI a replacement version, runtime implementation, or normative owner of those works. The local [Continuity Bundle / Cold Wake entry](../../protocols/continuity-bundle/README.md) remains a separate package.
