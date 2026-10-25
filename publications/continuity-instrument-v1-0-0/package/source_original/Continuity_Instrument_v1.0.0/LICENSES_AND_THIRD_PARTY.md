# Licenses and third-party boundaries

## CI scientific text and metadata

Copyright © 2026 Ivan Kotov.

The scientific text and metadata created for this publication package are licensed under the **Creative Commons Attribution 4.0 International license (CC BY 4.0)**:

https://creativecommons.org/licenses/by/4.0/

This grant covers the following scientific-text and metadata files as prepared in this package:

- `README.md`
- `CI_SPECIFICATION.md`
- `TERMINOLOGY.md`
- `SCIENTIFIC_CLAIM_MAP.md`
- `CONTINUITY_OBSERVABLES.md`
- `RECOGNITION_PROFILE.md`
- `REPRODUCIBILITY.md`
- `LIMITATIONS.md`
- `LICENSES_AND_THIRD_PARTY.md`
- `CITATION.cff`
- `.zenodo.json`
- `EVIDENCE_STATUS.json`
- `PUBLICATION_CHECKLIST.md`
- `PUBLICATION_MANIFEST.json`
- `SHA256SUMS.txt`
- `STATIC_VERIFICATION.json`
- `ZENODO_DEPOSIT_INSTRUCTIONS.md`

## Component boundaries

| Component | Included in this draft? | Rights treatment |
|---|---|---|
| CI scientific prose and metadata listed above | Yes | CC BY 4.0. |
| `REFERENCE_IMPLEMENTATION/` (including schemas) and `tests/test_ci_profile.py` | Yes | **Copyright © 2026 Ivan Kotov. All rights reserved. No license grant.** These files do not inherit CC BY 4.0 by implication. |
| Frozen R160/R161 runner and scoring sources outside this package | Referenced, not copied | Retain their existing component or repository license; this package does not relicense them. |
| R157 evidence archive | Referenced, not copied | Retains its original rights and access controls. The Drive ID and SHA-256 are custody metadata, not a license grant. |
| R160/R161 evidence archives | Linked and pinned, not copied | Retain their original rights and access controls. This package reports only custody metadata and bounded terminal results. |
| Ollama runtime | Not distributed | Governed by the runtime publisher's license and terms. Pins identify the evaluated bytes only. |
| `qwen3-vl:32b` and `qwen2.5:32b` model files | Not distributed | Governed by the model files' accompanying licenses and applicable terms. Pins do not grant redistribution rights. |
| Referenced public-canon DOI records | Linked, not incorporated | Governed by each record's own license and rights statement. Citation does not import its content or license. |
| Qubit material | Linked and pinned only | **All Rights Reserved.** No raw Qubit text is included or licensed by this package. |

## Qubit boundary

The only Qubit information included in this draft is repository and integrity metadata:

- Repository: https://github.com/Kot141078/qubit-of-hope-volume-i
- Commit: `88b582579ace4a330ce4d53b07d7ec4e98cb4eeb`
- Tree: `9d251575e2b0d3c75bfd1fe7782c562f1de64a38`
- Rights posture: All Rights Reserved.

No Qubit narrative, excerpt, holdout text, translation, or derivative content is reproduced.

## Final component rights for deposit

The package uses two non-overlapping rights entries:

1. **Scientific text and metadata:** Creative Commons Attribution 4.0 International (`CC-BY-4.0`).
2. **Reference implementation, schemas, and tests:** `Copyright © 2026 Ivan Kotov. All rights reserved. No license grant.`

The second entry preserves the existing no-grant posture and does not create new code rights. In the Zenodo web UI, add both entries and associate their scopes in the record description. The `.zenodo.json` `cc-by-4.0` field represents the scientific-text/metadata entry only; it must not be interpreted as relicensing code, schemas, or tests.

## Public-canon references

The following are external citations, not bundled works:

- Theoretical Core: https://doi.org/10.5281/zenodo.20679718 and https://doi.org/10.5281/zenodo.20679717
- Temporal AI Presence: https://doi.org/10.5281/zenodo.22070960 and https://doi.org/10.5281/zenodo.22070959
- Personality Formation: https://doi.org/10.5281/zenodo.20648731 and https://doi.org/10.5281/zenodo.20648730
- C-Calculus: https://doi.org/10.5281/zenodo.21205427
- Beacon: https://doi.org/10.5281/zenodo.18933553
- Entity vs Profile: https://doi.org/10.5281/zenodo.21204415 and https://doi.org/10.5281/zenodo.21204414

A depositor must review the rights statement of any external material before copying it into a later release.

## No rights inference

A hash, DOI, URL, citation, repository pin, evaluator output, or witness record does not grant a copyright license, access permission, model license, data-processing right, operational authority, or right to publish. Those permissions must be established separately for each component.
