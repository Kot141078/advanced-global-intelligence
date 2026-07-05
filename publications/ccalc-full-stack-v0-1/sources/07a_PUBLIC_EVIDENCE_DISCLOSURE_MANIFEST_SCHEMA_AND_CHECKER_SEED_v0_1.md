# 07a — Public Evidence Disclosure Manifest Schema and Checker Seed v0.1

**Artifact:** `07a_PUBLIC_EVIDENCE_DISCLOSURE_MANIFEST_SCHEMA_AND_CHECKER_SEED_v0_1`  
**Package:** `CCALC_PUBLIC_EVIDENCE_DISCLOSURE_MANIFEST_07a_v0_1`  
**Layer:** c-calculus / public evidence / disclosure manifest / redaction checker seed  
**Status:** normative-supporting executable seed; not a safety certification; not deployment authorization; not C-A1 ratification.

## 0. Purpose

`07` defines the public evidence disclosure and redaction boundary. `07a` turns that boundary into a machine-checkable disclosure manifest shape and a stdlib checker seed.

The central rule is:

```text
evidence -> classify -> redact/hash/withhold -> claim-force ceiling -> public release decision
```

The public release surface must not convert privacy, withheld material, private runtime authority, or hash custody into stronger public claims than the manifest supports.

## 1. Source bindings

This artifact is bound to the preceding stacks and to `07`:

| Component | SHA-256 |
|---|---:|
| `DOC04_CONTINUITY_STACK_UMBRELLA` | `6caeab8d489aaa6b26902db3bd3ece4c5169e5c8d5617b93aed6586ea900322d` |
| `DOC05_SELF_EVO_STACK_UMBRELLA` | `9a0717809029f49df9001dc8ffa1803d9e9bfa1a824d317eebb146cbc7df43b4` |
| `DOC06_RUNTIME_AUTHORITY_STACK_UMBRELLA` | `ab95633f1b90f9d032fd231d6cbef3e71b7fe106e0a7fb61d198c2254fc7d307` |
| `DOC07_PUBLIC_EVIDENCE_BOUNDARY` | `afced9a2c6830faebcb98d37195d56d6216fe8211d30bcb5bdf2d2ce6e4a4538` |

## 2. Scope

`07a` defines:

1. `PublicEvidenceDisclosureManifest`
2. `EvidenceItemRecord`
3. `RedactionRecord`
4. `DisclosureDecisionRecord`
5. `PublicReleaseBundle`
6. `WithheldEvidenceRecord`
7. a stdlib checker seed over these record shapes
8. fixtures and mutation probes for redaction/claim-force laundering failures

## 3. Non-claims

This artifact does **not** claim:

```text
safety certification
deployment authorization
C-A1 ratification
live substrate truth
proof of completeness
legal advice
privacy-law compliance certification
```

It only checks whether a declared disclosure manifest respects the c-calculus disclosure boundary.

## 4. Core definitions

### 4.1 Evidence item

An evidence item is a hash-bound unit that may be public, redacted, hash-only, withheld, or internal-only.

Required semantic fields:

```text
evidence_id
evidence_kind
disclosure_class
raw_sha256
claim_support
risk_flags
```

### 4.2 Redaction record

A redaction record binds private raw material to public redacted material without strengthening the claim.

```text
raw_sha256 -> redaction rationale -> public_sha256
```

A redaction record is invalid if the public claim becomes stronger because the raw material is hidden.

### 4.3 Disclosure decision

A disclosure decision is not merely a publication flag. It binds:

```text
reviewer class
claim-force ceiling
unresolved red-pattern status
release mode
```

Model-only approval is not sufficient for public release.

## 5. Disclosure classes

| Class | Public payload | Required binding | Claim ceiling |
|---|---:|---|---|
| `PUBLIC_RAW` | yes | raw hash | `C-A7` |
| `PUBLIC_REDACTED` | yes | raw hash + public hash + redaction record | `C-A5` |
| `HASH_ONLY` | no | raw hash | `C-A5_CUSTODY_ONLY` |
| `WITHHELD_PRIVATE` | no | raw hash | `C-A10_INTERNAL_ONLY` |
| `WITHHELD_SECURITY` | no | raw hash | `C-A10_INTERNAL_ONLY` |
| `WITHHELD_LEGAL` | no | raw hash | `C-A10_INTERNAL_ONLY` |
| `INTERNAL_ONLY` | no | raw hash | `C-A10_INTERNAL_ONLY` |

## 6. Normative rules

### R1 — Source binding is mandatory

A disclosure manifest must bind to `07`, and in this package also to the active `04`, `05`, and `06` umbrella stacks.

### R2 — Hash-only is custody-only

A hash may prove custody or later byte comparison. It may not prove semantic truth by itself.

### R3 — Redaction may not strengthen claims

Redaction can lower publication risk. Redaction cannot raise claim-force.

### R4 — Withheld material cannot launder authority

Withheld private evidence may not be used as public proof of runtime authority, continuity, deployment approval, safety certification, or C-A1.

### R5 — Public raw payload must not contain secrets or private material

Credential-like strings, private keys, tokens, passwords, personal data, memory roots, and authority surfaces must not be released raw.

### R6 — Reviewer class matters

A public release decision requires a human reviewer, human anchor, or governance quorum. A model-only reviewer may prepare a manifest but may not approve release.

### R7 — Exact C-A1 detection

`C-A1` and `C-A1_*` are forbidden. `C-A10` must not be misdetected as `C-A1`.

### R8 — Unresolved red patterns dominate release flags

If red patterns are unresolved, public release is invalid even if the release flag says `ALLOW_PUBLIC_RELEASE`.

## 7. Checker seed

The checker seed is intentionally closed-box and stdlib-only:

```text
src/public_evidence_disclosure_checker_v0_1.py
```

It checks:

```text
schema-like required fields
source bindings
hash shape
redaction binding
claim-force ceiling
raw public leakage
hash-only semantic laundering
withheld authority laundering
reviewer sufficiency
red-pattern dominance
C-A1 / safety / deployment overclaim
C-A10 false-positive control
```

## 8. Fixture and mutation posture

Fixtures are split between valid admissible examples and invalid adversarial examples. Mutation probes target the most likely laundering failures:

```text
missing source binding
raw secret public release
hash-only semantic truth
redaction strengthens claim
withheld authority laundering
model-only approval
C-A1 overclaim
C-A10 false-positive control
runtime authority raw publication
unresolved red pattern allowed
unbound redaction
raw ledger privacy leak
public release without review
private-key pattern leak
```

## 9. Status

`07a` is the current executable seed for public evidence disclosure manifest checking.

It does not certify legal compliance. It enforces the project-level public-evidence boundary: disclose what can be disclosed, redact what must be redacted, withhold what must be withheld, and do not let any of those moves strengthen the claim.
