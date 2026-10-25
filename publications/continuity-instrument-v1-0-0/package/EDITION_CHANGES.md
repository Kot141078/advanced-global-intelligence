# English academic edition: changes and continuity

**Author: Ivan Kotov.** ORCID: https://orcid.org/0009-0009-6002-9845. Prepared 25 October 2026.

Editorial edition: **academic-pdf-2**. Underlying CI source version: **1.0.0**, original build **_02**.

## Purpose of this revision

This revision makes English the primary publication language for an international readership. It provides a complete English reading route, from the explanatory paper to the technical specification, implementation and reproducibility, evidence and limitations, rights and citation, and the manual publication guide. The English explanatory paper covers every substantive section of the retained Russian paper. Its English captions, diagrams, references and teaching example are included in the same volume.

The package README, publication description, metadata, reading map and instructions are in English. All six English PDF filenames explicitly end in `_EN.pdf`. Each English volume has an academic title page, Ivan Kotov's authorship and ORCID, a table of contents, references or source attribution, and page numbers.

## Preserved Russian supplement

`PDFs/02_CI_Explanatory_Paper_RU.pdf` and its Markdown manuscript are retained without changes. The PDF's SHA-256 is `8d608445e44e88845eb121b5fbe541e677d112090959475214c74fb63ef5ea0f`. Its original `academic-pdf-1` label is intentional. This retained label identifies the unchanged supplement; the enclosing package and the six English volumes are `academic-pdf-2`.

The Russian supplement is optional for English readers. No substantive content requires knowledge of Russian to use the English publication route.

## Preserved source and scientific status

The original ZIP is retained at `source_original/CI_CONTINUITY_INSTRUMENT_V1_0_0.zip`: **50,765 bytes**, SHA-256 `be87dd926ed96e91e8de25bae2e18666f74ac738b173379ddc0092f98563f663`. All 22 extracted original files are byte-identical to that archive. The superseded source build _01 is not part of this edition.

This is a language and editorial revision. It introduces no implementation change, historical qualification replay, new empirical result or new rights grant. R157 remains scoped open-synthetic evidence; R160 and R161 remain negative qualification attempts. Empirical qualification remains `NOT_ESTABLISHED`.

The preceding academic-pdf-1 outer ZIP is a separate editorial predecessor: 1,079,078 bytes, SHA-256 `c695909423256e977fd7db9d4fd7bfed79c8797d208e4459643317ed6e6ec747`. It is not the current manual-deposit package. The present edition has its own manifest, checksum index and external ZIP checksum sidecar.

## Rights and verification

Component rights remain unchanged. The author's scientific prose and descriptive metadata are CC BY 4.0; reserved implementation, schema, test, utility and example components retain their stated no-grant terms. PDF 04 has section-specific mixed rights. See PDF 06 and `PACKAGE_MANIFEST.json`.

`verification/LANGUAGE_COVERAGE.json` records the English reading route and the preserved Russian supplement. `verification/PDF_INVENTORY.json` records the final PDF identities. Run `python verification/verify_package.py` from the extracted package to check the complete byte inventory. Byte consistency does not establish scientific validity or authorship authentication.
