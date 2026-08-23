# Temporal AI Presence Profile v1.0

**Author:** Ivan Kotov  
**ORCID:** https://orcid.org/0009-0009-6002-9845  
**Version:** 1.0  
**Date:** 2026-08-23  
**Publication state:** `final_zenodo_deposit_package`
**Zenodo version DOI:** 10.5281/zenodo.22070960
**Concept DOI:** pending first publication

> Temporal AI Presence = sustained bounded AI participation across time.

Temporal AI Presence is not `c` by default. All valid `c`-class systems are Temporal AI Presences. Not all Temporal AI Presences are `c`-class systems.

## Source of record

`Temporal_AI_Presence_Profile_v1_0.md` is the governing source. The PDF is its human-readable rendering. This directory is the final Zenodo deposit package, not yet a published DOI record. The DOI `10.5281/zenodo.22070960` is reserved by Zenodo for this version and is registered when the corresponding Zenodo record is published. The Zenodo Concept DOI will be recorded after the first version is published and Zenodo exposes the exact all-versions identifier.

## Reading order

1. `README.md`
2. `Temporal_AI_Presence_Profile_v1_0.pdf`
3. `Temporal_AI_Presence_Profile_v1_0.md`
4. `NON_CLAIMS.md`
5. `TAP_PUBLIC_EVIDENCE_MATRIX_v1_0.csv`
6. `TAP_IMPLEMENTATION_CROSSWALK_v1_0.md`
7. `TAP_T03_DEPLOYMENT_BOUNDARY_v1_0.md`
8. `PROVENANCE.md`
9. `temporal_ai_presence_v1_0.json`, its schema, and the evidence indexes
10. `PACKAGE_MANIFEST.json`
11. `SHA256SUMS.txt`

## Evidence status

Public historical evidence and the public TAP-SEC reference remain distinct from one local reference implementation candidate. TAP-T03 is publicly documented as partial with an explicit deployment-external boundary. The local R2B code bundle is excluded, so T02, T06, T07, and T08 remain conservative publication candidates rather than publicly verified code bindings.

`M4_FULL_PASS=false`. `TAP-C=NOT CLAIMED`.

## Package inventory

| Layer | Artifacts |
|---|---|
| Canonical profile | `Temporal_AI_Presence_Profile_v1_0.md`, `Temporal_AI_Presence_Profile_v1_0.pdf` |
| Citation and deposit | `CITATION.cff`, `.zenodo.json`, `PROVENANCE.md`, `RELEASE_NOTES.md` |
| Boundaries and licenses | `NON_CLAIMS.md`, `LICENSE.md`, `LICENSE_POLICY.md`, `TAP_T03_DEPLOYMENT_BOUNDARY_v1_0.md` |
| Machine contract | `temporal_ai_presence_v1_0.json`, `temporal_ai_presence_v1_0.schema.json`, `TAP_EVIDENCE_BASELINE_v1_0.json` |
| Evidence projection | `TAP_PUBLIC_EVIDENCE_MATRIX_v1_0.csv`, `TAP_EVIDENCE_INDEX_v1_0.json`, `TAP_IMPLEMENTATION_CROSSWALK_v1_0.md`, `TAP_VALIDATION_SUMMARY_v1_0.json`, `TAP_CODE_REFERENCES_v1_0.json`, `TAP_EVIDENCE_DERIVATIVE_MAP_v1_0.json` |
| Public-safe R2B evidence | Sixteen files under `evidence/`, individually indexed and hash-bound; nine are byte-identical approved artifacts and seven are normalized derivatives. One R2C-approved report was normalized at R3A because it quoted a forbidden machine-specific path literal. |
| Integrity | `PACKAGE_MANIFEST.json`, `SHA256SUMS.txt` |

## Provenance and related work

The historical TAP v0.1 profile is integrated in the parent c Hardening Pack v0.1, DOI `10.5281/zenodo.20532198`. That DOI is not the standalone TAP v1.0 DOI. Public TAP-SEC M4 v0.3.2, DOI `10.5281/zenodo.21688521`, is a partial implementation reference with `M4_FULL_PASS=false`. MOT-c v0.1, DOI `10.5281/zenodo.22060517`, and World Intelligence, DOI `10.5281/zenodo.21497098`, are context-only relations and satisfy no TAP-T01 through TAP-T10 requirement.

## Citation

Cite this version using DOI `10.5281/zenodo.22070960` together with the title, author, version, and date. The parent DOI remains a related identifier, not the standalone TAP v1.0 DOI.

## Verification

From the release directory, verify every line of `SHA256SUMS.txt` against the corresponding relative path. `PACKAGE_MANIFEST.json` contains the same paths, byte sizes, hashes, roles, sources, media types, and licenses. The deterministic ZIP is validated separately before Zenodo upload.

## Deposit instruction

Upload exactly the eight files in the validated `final_upload/` custody set, enter the generated Zenodo form values, save the draft, validate, preview, and do not publish until owner review.
