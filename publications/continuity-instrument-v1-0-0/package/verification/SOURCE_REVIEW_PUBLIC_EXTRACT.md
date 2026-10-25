# Public extract: source build _02 technical review

Review date: 25 October 2026. Review performed by ChatGPT at the author's request. Scientific author and source copyright holder: Ivan Kotov. The reviewer is not described as an external human peer reviewer, and this extract is not a new empirical qualification.

Original complete review: CI_V1_0_0_BUILD_02_PUBLICATION_REVIEW_20261025.md.
Original complete review SHA-256: 147bc8c365833fb77164013dde0a6068f7a320d73f86e9a28dbabe7b2a000e2d.
The complete review includes private operational context and is not redistributed here. This public extract preserves the artifact checks, findings, and limitations needed to assess the publication; private journals, correspondence and historical evidence bytes are omitted.

## Exact source identity

- Original ZIP: CI_CONTINUITY_INSTRUMENT_V1_0_0.zip.
- Bytes: 50765.
- SHA-256: be87dd926ed96e91e8de25bae2e18666f74ac738b173379ddc0092f98563f663.
- ZIP member count: 22; CRC: 22/22 PASS.
- Original manifest payload members: 20/20 byte length and SHA-256 PASS.
- Original SHA256SUMS entries: 21/21 PASS, including the manifest.
- Independent deterministic ZIP rebuild: byte-equal.

## Verified technical observations

The review parsed all six JSON files and both Python files. Both Draft 2020-12 schemas passed meta-schema validation; a representative input and actual output passed schema validation. CITATION.cff passed the official CFF 1.2.0 schema. Eight focused test cases passed on Python 3.12.14/Linux. A normal CLI invocation returned 0 and created its output. These are observations of the published reference transformation, not empirical tests of a named AI subject's continuity.

The exact R157, R160 and R161 evidence archives were checked against their pinned byte lengths, SHA-256 values, CRC and complete member manifests. Their stored terminal records agreed with the source package: R157 bounded open-synthetic success; R160 and R161 negative qualification results. Historical code was not rerun, historical attempts were not rescored, and a byte audit was not treated as independent observation of the original processes.

Ten DOI identifiers listed in source metadata returned matching official Zenodo and DataCite metadata; this establishes the referenced records' identity, not the truth of every claim in those publications. ORCID checksum validation does not prove control of the author's account.

## Open findings

1. F-01, low severity: a string containing an unpaired Unicode surrogate can raise an uncaught UnicodeEncodeError at canonical UTF-8 serialization. Observed exit: 1 with traceback; expected documented invalid-input exit: 2. No output file was created. The error is not a successful result or a demonstrated incorrect interval total.
2. F-02, manual-deposit condition: the single global cc-by-4.0 licence field in the original .zenodo.json does not encode the original component rights. The final manual card must show two rights entries and explicit scopes. New mixed-rights materials in this edition require the scopes in PDF 06 and PDF 07 as well.
3. F-03, low severity: the implementation README names a non-existent publication_draft/ working directory. Use the extracted source root and the unittest discovery command from REPRODUCIBILITY.md. The alternate module command passed in the reviewed environment; an installed tests package could shadow it elsewhere.
4. F-04, low severity: read the general I_verified wording together with the specific reference policy: only admitted, duration-eligible records enter that coordinate and its coverage calculation. Admission counts retain admitted records that are not duration-eligible.

## Disposition and boundaries

Source review status: READY_FOR_MANUAL_PUBLICATION_WITH_NONBLOCKING_FINDINGS, for a bounded specification/reference publication with accurate rights and limitations. No source patch, publication, DOI assignment, scientific qualification, same-entity proof, consciousness claim, or operational approval follows from this status. Private evidence access remains separate. The academic edition adds explanations and typesetting without changing these results.

New package-specific PDF, example and checksum checks are recorded separately in BUILD_VERIFICATION.json and PDF_INVENTORY.json after they actually complete. They are not attributed retroactively to the original source review.
