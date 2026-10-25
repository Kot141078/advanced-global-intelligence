# Continuity Instrument (CI): Evidence-Bound Measurement of Governed Continuity in Long-Lived AI Systems, v1.0

**Package version:** 1.0.0  
**Release candidate prepared:** 2026-10-25  
**Status:** source/reference package prepared for direct Zenodo deposit; no CI DOI assigned  
**Empirical qualification:** not established

## Purpose

The Continuity Instrument (CI) is a research-software specification and reference transformation for recording bounded continuity claims about long-lived AI systems. It binds a report to admitted evidence, an explicit branch and event history, separate memory/governance/witness/authority lineages, structured uncertainty, and a declared claim ceiling.

CI reports **evidence-bound continuity age**, also called **formation depth**, as a vector. The vector is not elapsed wall time and is not a decision about entity identity, consciousness, personhood, legal status, moral status, ownership, authority, or uninterrupted existence.

The vector records:

- the first and last admissible witnesses;
- cumulative verified participation intervals;
- known pauses and unexplained gaps;
- replay, fork, restore, and cold-wake events;
- preservation or change in memory, governance, witness, and authority lineage;
- confirmed irreversible transitions; and
- structured uncertainty and prohibited inferences.

## Evidence ledger and claim ceiling

This package includes no private corpus text and no frozen runtime evidence archives. It links and pins those objects for custody review.

| Evidence object | Bound identity | Result and allowed interpretation |
|---|---|---|
| R157 predecessor | Drive ID `16Koyf3ckIkKjSni5C8C97L9c4DiuhIdE`; 3,703,123 bytes; SHA-256 `fc8564656fb777b1266d763bea841af0dd5f13b03e2f727db6f3ec3689270c8a` | Terminal `OD11_TQ_R157_PASS_OPEN_SYNTHETIC_SEMANTIC_GATE_FIDELITY`. This is immutable open-synthetic predecessor evidence within its exact scope. |
| R160 local Ollama episode | Drive ID `1JmLtDLkL4aQhTSIFprGjsd-xZDN2XRqC`; 251,185 bytes; SHA-256 `8b80604a62aa7d5232bf9659b87009537951a3f3b89151bc8164b88d4387952b` | `REAL_LOCAL_OLLAMA_CORPUS_QUALIFICATION_NOT_ESTABLISHED`. Five requests were captured, but the frozen scorer could not parse the empty outer `response` field. Independent custody review verdict: `CONFIRMED_CONSUMED_NEGATIVE_RETURN`. |
| R161 local Ollama qwen2.5 episode | Drive ID `1m11yDfvrhbIQ0Zlp-amxKiMixzNgWv76`; 191,074 bytes; SHA-256 `56c586b665b83c3485c19c3186ed989b17cd03fbf21555d7642f1316bb48002f` | `REAL_LOCAL_OLLAMA_QWEN25_CORPUS_QUALIFICATION_NOT_ESTABLISHED`. Coverage was 5/5; schema and claim-boundary predicates were 5/5, role 4/5, class 3/5, evidence 0/5, and complete records 0/5. Independent custody review verdict: `CONFIRMED_CONSUMED_NEGATIVE_RETURN`. |

These results do not establish a real-world continuity-age measurement, entity identity, personhood, general evaluator quality, provider attestation, operational approval, project completion, or publication readiness. R160 and R161 are negative consumed attempts; this package does not reinterpret them as a favorable result.

## Package map

- `CI_SPECIFICATION.md` — measurement model, evidence admission, branch handling, and output contract.
- `TERMINOLOGY.md` — bounded definitions used throughout the package.
- `SCIENTIFIC_CLAIM_MAP.md` — specified, supported, failed, and excluded claims.
- `CONTINUITY_OBSERVABLES.md` — vector coordinates, evidence requirements, and uncertainty representation.
- `RECOGNITION_PROFILE.md` — portable recognition projection without identity or authority overclaim.
- `REPRODUCIBILITY.md` — reference implementation, evidence pins, and reproducibility boundary.
- `LIMITATIONS.md` — scientific and operational limits.
- `LICENSES_AND_THIRD_PARTY.md` — final component-level rights and third-party boundaries.
- `REFERENCE_IMPLEMENTATION/` — standard-library transformation and v1 JSON schemas.
- `tests/test_ci_profile.py` — deterministic behavior and boundary tests.
- `EVIDENCE_STATUS.json` — machine-readable evidence ledger.
- `PUBLICATION_CHECKLIST.md` — deposit readiness and exact publication steps.
- `ZENODO_DEPOSIT_INSTRUCTIONS.md` — exact two-entry rights setup and byte-preserving deposit steps.
- `PUBLICATION_MANIFEST.json` and `SHA256SUMS.txt` — byte-level release inventory.
- `CITATION.cff` and `.zenodo.json` — citation and draft Zenodo metadata without a CI DOI.

## Reference implementation boundary

`REFERENCE_IMPLEMENTATION/ci_profile.py` is an executable encoding of the v1 vector rules for caller-supplied records. It uses integer ticks on a declared time axis, unions eligible intervals without double-counting, computes unexplained gaps, preserves typed events and separate lineages, and emits deterministic canonical UTF-8 JSON.

It does not collect evidence, establish admissibility, prove that input records are true, measure a named real system by itself, or perform scientific qualification. Its passing tests support only the specified transformation behavior.

The output is designed so CI can later feed a separately defined BACON adapter. Any adapter must preserve branch distinctions, uncertainty, claim ceiling, schema identity, and source checksum. This release does not define or implement BACON and makes no BACON compatibility claim.

## Public research canon

These records are conceptual references. Citation does not transfer their evidence, validation, or rights into CI.

- **Theoretical Core** — https://doi.org/10.5281/zenodo.20679718 ; concept https://doi.org/10.5281/zenodo.20679717
- **Temporal AI Presence** — https://doi.org/10.5281/zenodo.22070960 ; concept https://doi.org/10.5281/zenodo.22070959
- **Personality Formation** — https://doi.org/10.5281/zenodo.20648731 ; concept https://doi.org/10.5281/zenodo.20648730
- **C-Calculus** — https://doi.org/10.5281/zenodo.21205427
- **Beacon** — https://doi.org/10.5281/zenodo.18933553
- **Entity vs Profile** — https://doi.org/10.5281/zenodo.21204415 ; concept https://doi.org/10.5281/zenodo.21204414

Author ORCID: https://orcid.org/0009-0009-6002-9845  
Public corpus map: https://ivankotov.eu/corpus-map/

## Rights and publication state

The scientific text and metadata are explicitly licensed under CC BY 4.0. Referenced evidence, repositories, models, runtimes, and source components retain their own rights. Qubit material is All Rights Reserved and is represented only by links and cryptographic or repository pins; no Qubit source text is reproduced.

The reference implementation, its schemas, and tests are distributed under the following custom rights statement: **Copyright © 2026 Ivan Kotov. All rights reserved. No license grant.** They do not inherit CC BY 4.0 by implication. The Zenodo record must contain two rights entries: CC BY 4.0 for scientific text/metadata, and the exact custom statement above for code/schemas/tests. No DOI has been assigned by this package-preparation step.
