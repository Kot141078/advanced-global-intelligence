# TAP v1.0 RC Package Architecture

## Chosen location

```text
publications/temporal-ai-presence-v1-0-rc/release/
```

## Precedent

The primary precedent is `publications/motivational-formation-c-v0-1/release/`, fixed in the synchronized repository at commit `5ffe01445b18d2efac0316b0a791fa27030a4f12`. It establishes a publication directory with canonical Markdown, reader PDF, `README.md`, `CITATION.cff`, provenance, release notes, machine-readable schemas, `manifest.json`, and `SHA256SUMS`.

The c Hardening Pack remains the parent-publication precedent for historical TAP custody under `hardening/c_hardening_pack_v0_1/`. R1 does not duplicate or alter that package.

## Architecture decision

| Component | RC path | Governing rule |
|---|---|---|
| Canonical normative source | `Temporal_AI_Presence_Profile_v1_0_RC.md` | Governs the PDF and machine projection. |
| Reader rendering | `Temporal_AI_Presence_Profile_v1_0_RC.pdf` | Pre-publication rendering; Markdown prevails on conflict. |
| Citation metadata | `CITATION.cff` | No top-level standalone DOI until publication. |
| Provenance | `PROVENANCE.md` | Exact commits and relationship types; no universal first-use claim. |
| Boundary map | `TAP_CLAIM_AND_BOUNDARY_MAP_v1_0.md` | References parent mechanisms without redefining them. |
| Normative machine instance | `temporal_ai_presence_v1_0.json` | Complete structured projection of the profile. |
| Validation schema | `temporal_ai_presence_v1_0.schema.json` | JSON Schema Draft 2020-12. |
| Evidence baseline | `TAP_EVIDENCE_BASELINE_v1_0.json` | Frozen R0 evidence state; no R1 promotion. |
| Package inventory | `manifest.json` | Hashes content artifacts while excluding recursive integrity files. |
| Byte custody | `SHA256SUMS` | Hashes every artifact except itself. |

## Deliberate exclusions

- No `.zenodo.json`, because R1 is not DOI publication.
- No release ZIP, because the current RC can be validated directly and no repository convention requires a pre-review ZIP.
- No website, sitemap, JSON-LD, release, tag, DNS, or OVH integration.
- No TAP implementation or Ester source changes.

## Rendering convention

The repository's recent DOI-bound MOT-c package records the sequence Markdown to paged HTML to PDF to raster inspection. R1 follows the same document intent using a deterministic local ReportLab renderer because Pandoc and WeasyPrint executables are unavailable in the current environment. The render command, page count, and raster QA are recorded in the external R1 report.
