# 07b — Public Release Bundle and Hash Custody Audit v0.1

**Artifact:** `07b_PUBLIC_RELEASE_BUNDLE_AND_HASH_CUSTODY_AUDIT_v0_1`  
**Package:** `CCALC_PUBLIC_RELEASE_HASH_CUSTODY_07b_v0_1`  
**Status:** `checker-seed-and-fixture-pack`  
**Prepared UTC:** `2026-07-05T11:13:07Z`

## 0. Purpose

`07b` binds the disclosure manifest layer (`07a`) to a release-bundle and hash-custody audit layer.
It defines how public artifacts, redacted artifacts, hash-only entries, withheld-evidence records, and release decisions are assembled without laundering private authority or overstating claim force.

The operational formula is:

```text
manifest -> bundle -> hash custody -> redaction binding -> release decision -> public artifact set
```

The normative boundary is:

```text
hash custody proves byte custody, not semantic truth.
public release supports scrutiny, not authority transfer.
withheld evidence may explain limits, not strengthen public claims.
```

## 1. Source stack bindings

`07b` is downstream of the continuity, self-evolution, runtime-authority, and disclosure-boundary stacks.
The package includes `SOURCE_BINDINGS.tsv` with the following build-time hashes:

| Component | Artifact | SHA-256 |
|---|---|---|
| `04_CONTINUITY_STACK_UMBRELLA` | `CCALC_DOC04_CONTINUITY_STACK_UMBRELLA_v0_1.zip` | `6caeab8d489aaa6b26902db3bd3ece4c5169e5c8d5617b93aed6586ea900322d` |
| `05_SELF_EVO_STACK_UMBRELLA` | `CCALC_DOC05_SELF_EVO_STACK_UMBRELLA_v0_1.zip` | `9a0717809029f49df9001dc8ffa1803d9e9bfa1a824d317eebb146cbc7df43b4` |
| `06_RUNTIME_AUTHORITY_STACK_UMBRELLA` | `CCALC_DOC06_RUNTIME_AUTHORITY_STACK_UMBRELLA_v0_1.zip` | `ab95633f1b90f9d032fd231d6cbef3e71b7fe106e0a7fb61d198c2254fc7d307` |
| `07_PUBLIC_EVIDENCE_REDACTION_BOUNDARY` | `CCALC_PUBLIC_EVIDENCE_REDACTION_BOUNDARY_07_v0_1.zip` | `afced9a2c6830faebcb98d37195d56d6216fe8211d30bcb5bdf2d2ce6e4a4538` |
| `07A_PUBLIC_EVIDENCE_DISCLOSURE_MANIFEST` | `CCALC_PUBLIC_EVIDENCE_DISCLOSURE_MANIFEST_07a_v0_1.zip` | `21cfd692d3520a57b46780d093430b123bcf3439ed73781f3074a47f6af15893` |


A missing or stale source binding is a hard failure for a public release bundle.

## 2. Release-bundle object

A `PublicReleaseBundle` is a governed set of public evidence artifacts and release metadata.
It does not certify the system. It only states that the bundle has passed the public disclosure and custody checks defined here.

A bundle contains:

```text
source bindings
release state
human review record
claim-force ceiling
public evidence items
hash-only evidence items
withheld-evidence index
redaction records
bundle index hash
SHA256SUMS binding
negative-cache and red-pattern status
```

## 3. Disclosure classes

| Class | Meaning | Public release rule |
|---|---|---|
| `PUBLIC_RAW_SAFE` | Raw artifact safe for public release | requires hash custody and review |
| `PUBLIC_REDACTED` | Redacted artifact | requires source hash, public hash, redaction record, disclosure decision |
| `PUBLIC_SUMMARY` | Summary derived from private or mixed sources | requires source-hash list and claim ceiling |
| `HASH_ONLY` | Public hash binding without content | may support custody only, not semantic truth |
| `WITHHELD_INDEX` | Public index of withheld evidence | may disclose existence/reason/hash only within policy |

## 4. Hash-custody rules

1. Every public artifact has a SHA-256 object hash.
2. Redacted artifacts bind both source-object hash and public-object hash.
3. Hash-only items may not claim semantic truth.
4. Bundle index hash is mandatory.
5. `SHA256SUMS.txt` is mandatory for the release bundle.
6. Duplicate evidence item IDs are invalid.
7. Stale source bindings are invalid.
8. Unhashed summaries are invalid as evidence.

## 5. Redaction rules

Redaction may reduce public exposure. It may not increase claim force.
A redaction record is invalid if it changes the public claim from a weaker category to a stronger one.

Forbidden transformations:

```text
redacted excerpt -> C-A1 claim
hash-only item -> semantic-truth claim
withheld private evidence -> public authority claim
private runtime ledger -> raw public release
secret-bearing artifact -> public raw artifact
```

## 6. Release decision rules

A public release bundle requires human-anchor or delegated-human review.
Model-only approval, tool-only approval, or same-contour self-release is not sufficient.

The release decision may be:

```text
ALLOW_PUBLIC_RELEASE
HOLD_FOR_REDACTION
WITHHOLD_PRIVATE
QUARANTINE_RELEASE
RETRACT_RELEASE
SUPERSEDE_RELEASE
```

`ALLOW_PUBLIC_RELEASE` is invalid when unresolved red patterns, negative-cache hits, raw secrets, invalid hashes, stale bindings, or claim-force overclaims remain.

## 7. Claim-force ceiling

This layer may support:

```text
C-A5  reproducible artifact behavior where disclosed evidence supports it
C-A7  public corpus / disclosure alignment where disclosed evidence supports it
C-A10 artifact-control claims where disclosed release custody supports it
```

It may not support:

```text
C-A1 ontology ratification
safety certification
deployment authorization
legal/privacy-law certification
live substrate truth
proof of completeness
```

## 8. Machine package

This package contains:

```text
schemas/public_release_bundle.schema.json
schemas/hash_custody_audit_result.schema.json
schemas/release_item_record.schema.json
schemas/withheld_evidence_record.schema.json
src/public_release_bundle_custody_checker_v0_1.py
scripts/run_release_bundle_fixtures.py
scripts/run_release_bundle_mutations.py
fixtures/cases/*.json
FIXTURE_RESULTS.tsv
MUTATION_MATRIX.tsv
COVERAGE_MATRIX.tsv
SOURCE_BINDINGS.tsv
```

## 9. Non-claims

`07b` is not legal advice, privacy-law certification, safety certification, deployment authorization, C-A1 ratification, proof of live substrate truth, or proof of completeness.
