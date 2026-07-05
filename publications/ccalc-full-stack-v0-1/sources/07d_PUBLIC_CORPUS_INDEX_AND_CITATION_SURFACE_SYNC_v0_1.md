# 07d — Public Corpus Index and Citation Surface Sync v0.1

**Document id:** `07d_PUBLIC_CORPUS_INDEX_AND_CITATION_SURFACE_SYNC_v0_1`  
**Package id:** `CCALC_PUBLIC_CORPUS_CITATION_SYNC_07d_v0_1`  
**Author:** Kotov Ivan  
**Status:** normative draft + checker seed package  
**Parent layer:** `07_C_PUBLIC_EVIDENCE_DISCLOSURE_AND_REDACTION_BOUNDARY_v0_1`

## 1. Purpose

`07d` defines how public corpus indexes and citation surfaces stay synchronized after a release, supersession, erratum, retraction, or withholding decision.

It closes the publication-side gap left after `07`, `07a`, `07b`, and `07c`:

```text
evidence -> disclosure manifest -> release bundle -> correction ledger -> corpus index / citation surface sync
```

The layer is not concerned with proving that a private event happened. It is concerned with keeping public citation surfaces honest about what may be cited, what has been superseded, what has been retracted, and what remains withheld.

## 2. Core formula

```text
public release is not just a ZIP;
public release creates citation surfaces that must remain synchronized.
```

Operational form:

```text
artifact hash -> corpus item record -> citation surface records -> sync decision -> public index update | hold | supersede | retract | quarantine
```

## 3. Source bindings

| Component | SHA-256 |
|---|---:|
| `DOC04_CONTINUITY_STACK_UMBRELLA` | `6caeab8d489aaa6b26902db3bd3ece4c5169e5c8d5617b93aed6586ea900322d` |
| `DOC05_SELF_EVO_STACK_UMBRELLA` | `9a0717809029f49df9001dc8ffa1803d9e9bfa1a824d317eebb146cbc7df43b4` |
| `DOC06_RUNTIME_AUTHORITY_STACK_UMBRELLA` | `ab95633f1b90f9d032fd231d6cbef3e71b7fe106e0a7fb61d198c2254fc7d307` |
| `DOC07_PUBLIC_EVIDENCE_BOUNDARY` | `afced9a2c6830faebcb98d37195d56d6216fe8211d30bcb5bdf2d2ce6e4a4538` |
| `DOC07A_DISCLOSURE_MANIFEST` | `21cfd692d3520a57b46780d093430b123bcf3439ed73781f3074a47f6af15893` |
| `DOC07B_RELEASE_HASH_CUSTODY` | `b84ccc97d9564b6f95e92b0acd68481aa2d316d7e6ceb6c561bcddf8433be246` |
| `DOC07C_RETRACTION_SUPERSESSION_ERRATA` | `d191c3202c1463cf741f82c978d8414041432174cdff891947e515e32358eec3` |

## 4. Public citation surfaces

The default citation-sync set is:

```text
README_INDEX
CITATION_CFF
ZENODO_METADATA
GITHUB_RELEASE
WEBSITE_PUBLICATION_PAGE
LLMS_TXT
SITEMAP_XML
```

Optional surfaces include:

```text
ORCID_WORKS
DOI_LANDING_PAGE
```

A surface is not authoritative merely because it is public. A surface is admissible only when it carries the same artifact hash, status, claim-force ceiling, and correction guidance as the governing corpus item record.

## 5. Status propagation

| Status | Citation rule |
|---|---|
| `CURRENT` | May be cited as current only when all required surfaces agree on hash and status. |
| `SUPERSEDED` | Must carry a replacement artifact hash and public supersession notice. |
| `RETRACTED` | Must carry `do_not_cite_as_current` guidance on every public surface. |
| `ERRATA` | Must carry an errata notice on every public surface. |
| `WITHHELD` | May expose only a placeholder; withheld evidence cannot strengthen claims. |

## 6. Claim-force ceiling

`07d` may support public citation and public custody claims. It must not lift claims into ontology, safety certification, deployment authorization, legal certification, or live-substrate truth.

Forbidden examples:

```text
hash matches -> therefore semantic truth
redacted evidence exists -> therefore stronger claim
withheld evidence exists -> therefore hidden authority
public DOI exists -> therefore deployment authorization
C-A10 -> parse as C-A1 by prefix
```

`C-A10` is handled as an exact claim-force token and is not treated as `C-A1`.

## 7. Checker seed

The checker seed is:

```text
src/public_corpus_citation_sync_checker_v0_1.py
```

It checks:

```text
source bindings
human/citation/privacy review presence
negative-cache and red-pattern blocks
corpus item IDs and artifact hashes
required citation surfaces
surface hash/status/DOI consistency
claim-force ceilings
supersession / retraction / errata propagation
raw secret / private key / raw runtime ledger leakage
hash-only semantic-truth laundering
redaction and withheld-evidence authority laundering
C-A1 / deployment / safety / legal overclaims
```

## 8. Fixture and mutation coverage

This package contains `90` fixture cases and a mutation harness.

The intended high-risk failure classes are:

```text
missing source binding
stale source hash
model-only release/citation review
negative-cache ignored
red-pattern ignored
required surface missing
surface hash drift
DOI divergence
C-A1 or deployment overclaim
hash-only semantic-truth laundering
redaction strengthens claim
withheld evidence strengthens claim
raw secret/private key/runtime ledger public
superseded item still marked current
retracted item still citable
errata notice missing
withheld item exposed as public surface
C-A10 false-positive against C-A1 prefix logic
```

## 9. Non-claims

This package is not:

```text
legal advice
privacy-law certification
safety certification
deployment authorization
C-A1 ratification
live substrate truth
proof of completeness
```

## 10. Reading order

```text
07 -> 07a -> 07b -> 07c -> 07d
```

`07d` is the public-corpus synchronization capstone for the `07` public evidence layer.
