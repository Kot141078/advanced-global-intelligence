# Self-Evo Document Package v0.1.1

Author: Kotov Ivan
Location: Bruxelles, Belgique
Year: 2026
Version: 0.1.1-safe-layout
DOI: <https://doi.org/10.5281/zenodo.20938909>

## Status

Draft document-level governance corpus for bounded self-evolution of `c = a + b` systems.

This package includes accepted v0.1.1 Markdown sources, checked academic PDFs, advisory review records, append-first patch notes, package-control artifacts, manifests, and SHA-256 checksums.

## DOI and archival record

- DOI: `10.5281/zenodo.20938909`
- DOI URL: <https://doi.org/10.5281/zenodo.20938909>
- Zenodo record: <https://zenodo.org/records/20938909>

## Start here

Human reading route:

1. `README.md`
2. `package_control/SELF_EVO_PACKAGE_INDEX_AND_READING_ORDER_v0_1.md`
3. `docs/pdf/`
4. `docs/markdown/`

Machine reading route:

1. `package_control/SELF_EVO_PACKAGE_MANIFEST_v0_1.json`
2. `SHA256SUMS.txt`
3. `manifests/`
4. `docs/markdown/`

## Core documents

| ID | Markdown | PDF |
|---|---|---|
| SELF-EVO-01 | `docs/markdown/C_Self_Evolution_Gate_CGAM_TRIAD_SRLM_Profile_v0_1_1.md` | `docs/pdf/C_Self_Evolution_Gate_CGAM_TRIAD_SRLM_Profile_v0_1_1_academic.pdf` |
| SELF-EVO-02 | `docs/markdown/02_SRLM_Bounded_Growth_Contour_Profile_v0_1_1.md` | `docs/pdf/02_SRLM_Bounded_Growth_Contour_Profile_v0_1_1_academic.pdf` |
| SELF-EVO-03 | `docs/markdown/03_Self_Evo_Proposal_Packet_Schema_v0_1_1.md` | `docs/pdf/03_Self_Evo_Proposal_Packet_Schema_v0_1_1_academic.pdf` |
| SELF-EVO-04 | `docs/markdown/04_Self_Evo_Local_Checker_Rules_v0_1_1.md` | `docs/pdf/04_Self_Evo_Local_Checker_Rules_v0_1_1_academic.pdf` |
| SELF-EVO-05 | `docs/markdown/05_Self_Evo_TRIAD_Sister_Witness_Profile_v0_1_1.md` | `docs/pdf/05_Self_Evo_TRIAD_Sister_Witness_Profile_v0_1_1_academic.pdf` |
| SELF-EVO-06 | `docs/markdown/06_Self_Evo_Memory_Gate_and_EA_Profile_v0_1_1.md` | `docs/pdf/06_Self_Evo_Memory_Gate_and_EA_Profile_v0_1_1_academic.pdf` |
| SELF-EVO-07 | `docs/markdown/07_Self_Evo_Anti_Autarky_and_Resource_Gate_v0_1_1.md` | `docs/pdf/07_Self_Evo_Anti_Autarky_and_Resource_Gate_v0_1_1_academic.pdf` |
| SELF-EVO-08 | `docs/markdown/08_Self_Evo_Conformance_Fixture_Pack_v0_1_1.md` | `docs/pdf/08_Self_Evo_Conformance_Fixture_Pack_v0_1_1_academic.pdf` |
| SELF-EVO-09 | `docs/markdown/09_Self_Evo_Contradiction_Register_v0_1_1.md` | `docs/pdf/09_Self_Evo_Contradiction_Register_v0_1_1_academic.pdf` |
| SELF-EVO-10 | `docs/markdown/10_Self_Evo_Open_Issues_v0_1_1.md` | `docs/pdf/10_Self_Evo_Open_Issues_v0_1_1_academic.pdf` |

## Package-control artifacts

- `package_control/SELF_EVO_PACKAGE_INDEX_AND_READING_ORDER_v0_1.md`
- `package_control/SELF_EVO_PACKAGE_MANIFEST_v0_1.json`
- `manifests/ZENODO_STAGING_MANIFEST_v0_1_1_SAFE_LAYOUT.json`
- `manifests/ZENODO_FILE_MANIFEST_v0_1_1_SAFE_LAYOUT.csv`
- `SHA256SUMS.txt`

## Review and patch materials

- `controls/review_records/`
- `controls/patch_notes/`
- `controls/audits/PDF_LAYOUT_AUDIT_v3.md`

The package has 10 semantic review records covering SELF-EVO-01..10. The `controls/review_records/` directory contains 11 physical review-record files because the byte-identical `SEOI_REVIEW_RECORD_v0_1.md` and `SEOI_REVIEW_RECORD_v0_1-1.md` filenames are retained for archival correspondence with the Zenodo package.

## Bridge map

The package connects:

- `c = a + b`;
- CGAM bounded workers;
- SRLM bounded growth / shadow / candidate discipline;
- TRIAD-SYNAPS sister witness and anti-echo;
- Memory Gate and Experience Artifact boundaries;
- EA-L4 / consequence-bearing evidence;
- Anti-Autarky and Resource Actor Grounding;
- Local Checker rules;
- synthetic conformance fixtures;
- contradiction and open-issue registers.

## Verification

Run checksum verification from this directory:

```bash
sha256sum -c SHA256SUMS.txt
```

Expected package audit:

```text
bad text blocks: 0
bad text spans: 0
```

See:

```text
controls/audits/PDF_LAYOUT_AUDIT_v3.md
```

## Boundary

This package is not:

* an implementation;
* a conformance certificate;
* deployment authorization;
* a safety proof;
* a public-release certification;
* a personhood or consciousness claim;
* live self-evolution permission;
* autonomous resource-acquisition permission.

## License

* Documentation, Markdown, PDF, review records, and patch notes: CC BY 4.0.
* Machine-readable JSON, CSV, CFF, checksum, manifest, and future schema/checker artifacts: MIT.
