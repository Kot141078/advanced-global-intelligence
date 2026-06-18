# A6 Composition Layer v0.1.1

Hybrid / Federated Anchor Composition Profile for A6 in `c = a + b`.

This release finalizes the A6 correction: A6 is not a normal anchor class and not a merged super-anchor. It is an anchor-composition state over A0-A5.

DOI: [10.5281/zenodo.20752182](https://doi.org/10.5281/zenodo.20752182)

```text
A6 = mapped composition over anchor classes
     not merged standing
     not merged memory
     not merged identity
     not merged authority
```

## Canonical rule

```text
A6 may connect anchors. It must not melt them.
```

## Academic PDF revision

The PDFs in this package have been rebuilt in an academic layout with cover pages, publication-note pages, improved tables, headers/footers, PDF metadata, and the visible author line: `Kotov Ivan, Bruxelles. Belgique 2026`.

## Release contents

| Path | Role |
|---|---|
| `docs/a6/A6_Composition_Layer_v0.1.1.md` | Main A6 profile, canonical for A6 operational behavior. |
| `docs/anchor/ANCHOR_CLASS_BOUNDARIES_v0.2.1.md` | Boundary taxonomy with A6 reduced to a stable summary and pointer. |
| `docs/core/c_a_b_protocol_v1.1_L4_EN.md` | Parent `c = a + b` / L4 protocol context. |
| `pdf/A6_Composition_Layer_v0.1.1_academic.pdf` | DOI-friendly academic PDF rendering of the main profile. |
| `pdf/ANCHOR_CLASS_BOUNDARIES_v0.2.1_academic.pdf` | DOI-friendly academic PDF rendering of the boundary taxonomy. |
| `schemas/` | Draft JSON schemas for witness and resource/custodian records. |
| `examples/` | Example witness and resource/custodian packets. |
| `CITATION.cff` | GitHub citation metadata. |
| `.zenodo.json` | Zenodo deposit metadata. |
| `metadata/doi_deposit_metadata.json` | Human-readable DOI deposit metadata copy. |
| `quality_control/PACKAGE_QA.md` | Package QA notes and render checks. |

## Main corrections in v0.1.1

- Fixed the A6-EXIT / A6-SPLIT ambiguity.
- Defined `A6-EXIT` as revoke-and-continue.
- Defined `A6-SPLIT` as freeze-and-escalate.
- Added the missing Resource and Custodian Map required by the witness packet.
- Added a temporary high-risk rule for nested A6 recursion.
- Reduced `Anchor Class Boundaries` Section 12 to a stable summary and pointer, avoiding duplicate operational doctrine.

## Minimal citation

```text
Kotov, Ivan. A6 Composition Layer v0.1.1: Hybrid / Federated Anchor Composition Profile for A6 in c = a + b. Bruxelles. Belgique, 2026.
```

## DOI workflow

1. Push this package to GitHub.
2. Create a tagged release: `a6-composition-layer-v0.1.1`.
3. Attach the release ZIP, ZIP SHA256 sidecar, and academic PDFs.
4. Use canonical DOI URL: https://doi.org/10.5281/zenodo.20752182.

## Non-claims

This release does not create legal personhood, legal authority, product certification, clinical validity, public-law activation, post-anchor sovereignty, or merged identity.
