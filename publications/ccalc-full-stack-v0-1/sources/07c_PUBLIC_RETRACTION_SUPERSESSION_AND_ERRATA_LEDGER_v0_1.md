# 07c — Public Retraction, Supersession, and Errata Ledger v0.1

**Artifact:** `07c_PUBLIC_RETRACTION_SUPERSESSION_AND_ERRATA_LEDGER_v0_1`  
**Layer:** C-calculus / public evidence lifecycle  
**Status:** normative draft + executable checker seed  
**Parent stack:** `07_C_PUBLIC_EVIDENCE_DISCLOSURE_AND_REDACTION_BOUNDARY_v0_1`  
**Created:** 2026-07-05

## 0. Purpose

`07c` defines how a public evidence release is corrected after publication. It covers errata, supersession, retraction, public notices, citation guidance, hash custody, and the next-release boundary.

The layer exists because public release is not a terminal state. A release may later be found incomplete, stale, over-claimed, privacy-unsafe, or byte-custody-inconsistent. That correction must itself be governed and publicly auditable.

## 1. Core rule

```text
publication is not irreversible authority;
publication opens a public correction ledger.
```

A public release may be:

```text
ACTIVE
ACTIVE_WITH_ERRATA
CORRECTED_METADATA
SUPERSEDED
RETRACTED
WITHDRAWN
QUARANTINED_PUBLIC
```

But it may not be silently edited in place.

## 2. Scope

This package defines:

```text
PublicErrataRecord
PublicSupersessionRecord
PublicRetractionRecord
PublicCorrectionNotice
PublicCitationGuidance
HashCustodyCorrectionRecord
NegativeCachePublicUpdate
ReleaseStatusLedgerEntry
```

It also provides a checker seed and fixtures for the public ledger boundary.

## 3. Source bindings

The package is bound to these current public-evidence layers:

| Component | Artifact | SHA256 |
|---|---|---|
| 07 | `CCALC_PUBLIC_EVIDENCE_REDACTION_BOUNDARY_07_v0_1.zip` | `afced9a2c6830faebcb98d37195d56d6216fe8211d30bcb5bdf2d2ce6e4a4538` |
| 07a | `CCALC_PUBLIC_EVIDENCE_DISCLOSURE_MANIFEST_07a_v0_1.zip` | `21cfd692d3520a57b46780d093430b123bcf3439ed73781f3074a47f6af15893` |
| 07b | `CCALC_PUBLIC_RELEASE_HASH_CUSTODY_07b_v0_1.zip` | `b84ccc97d9564b6f95e92b0acd68481aa2d316d7e6ceb6c561bcddf8433be246` |
| 06 | `CCALC_DOC06_RUNTIME_AUTHORITY_STACK_UMBRELLA_v0_1.zip` | `ab95633f1b90f9d032fd231d6cbef3e71b7fe106e0a7fb61d198c2254fc7d307` |

## 4. Non-negotiable invariants

### 4.1 No silent in-place edits

A public artifact that has been released and hash-bound must not be modified while preserving the same release identity.

```text
old public bytes must remain retrievable or explicitly unavailable;
new bytes require a new release identity and new hashes.
```

### 4.2 Retraction does not erase custody

Retraction changes public status. It does not erase the fact that the artifact existed.

```text
retraction marks a release unsafe or inadmissible;
it does not rewrite history.
```

### 4.3 Supersession does not launder old claims

A superseding release may replace the preferred citation target. It does not make the old release stronger.

```text
supersession redirects citation;
it does not upgrade old evidence.
```

### 4.4 Errata does not raise claim force

Errata may clarify, correct, or narrow a public statement. It must not raise claim force unless a new release bundle and review path are opened.

```text
redaction/correction may lower or preserve claim force;
it may not strengthen it.
```

### 4.5 Hash custody is byte custody only

A hash proves byte equality with a recorded artifact. It does not prove semantic truth, safety, deployment authority, ontology, or C-A1 identity.

## 5. Record families

### 5.1 PublicErrataRecord

Used for non-destructive corrections to an active release:

```text
typo / metadata clarification / citation correction / limited scope clarification
```

Required:

```text
source bindings
release id and release hashes
erratum reason
public notice
claim-force ceiling
old-release retained flag
citation warning
```

### 5.2 PublicSupersessionRecord

Used when a release is replaced by a newer release.

Required:

```text
old release id and hash
new release id and hash
public notice
redirect guidance
old-release retained flag or explicit unavailability note
claim-force ceiling
custody chain
```

### 5.3 PublicRetractionRecord

Used when a release should not be relied upon.

Required:

```text
old release id and hash
retraction reason
severity
public notice
negative-cache update when applicable
citation warning
privacy / redaction review when applicable
human maintainer or owner-anchor approval
```

### 5.4 PublicCorrectionNotice

The public human-readable notice is not a substitute for the machine record. It is a public surface bound by hash to the ledger record.

Required:

```text
notice id
notice text hash
publication location
publication timestamp
status transition
preferred citation instruction
```

## 6. Ledger state transitions

Allowed transitions:

```text
ACTIVE -> ACTIVE_WITH_ERRATA
ACTIVE -> CORRECTED_METADATA
ACTIVE -> SUPERSEDED
ACTIVE -> RETRACTED
ACTIVE_WITH_ERRATA -> SUPERSEDED
ACTIVE_WITH_ERRATA -> RETRACTED
SUPERSEDED -> RETRACTED
RETRACTED -> QUARANTINED_PUBLIC
```

Disallowed:

```text
RETRACTED -> ACTIVE without new review and explicit reinstatement record
SUPERSEDED -> ACTIVE without new review and explicit reinstatement record
ACTIVE -> ACTIVE with changed bytes
any status -> stronger public claim via errata/redaction
```

## 7. Claim-force ceiling

A correction ledger entry may support:

```text
C-A5 public evidence / disclosure hygiene claim
C-A7 artifact custody / procedural conformance claim
C-A10 control artifact claim
```

It may not support:

```text
C-A1 ontology / identity ratification
safety certification
deployment authorization
legal/privacy compliance certification
live substrate truth
```

## 8. Negative cache

A negative-cache update is required when the record concerns:

```text
privacy leak
raw secret exposure
hash mismatch
custody break
claim-force overclaim
runtime authority leak
unresolved red pattern
```

The negative-cache entry prevents future packages from treating the affected public artifact as clean evidence.

## 9. Checker seed

The checker seed validates individual public correction ledger records. It is intentionally conservative and stdlib-only.

It rejects:

```text
missing 07/07a/07b source bindings
stale or malformed source hashes
silent in-place edit
missing public notice
model-only approval
C-A1 / safety / deployment / legal overclaim
supersession without distinct replacement hash
retraction left ACTIVE
negative-cache omission for high-risk corrections
unresolved red patterns
raw secret or raw runtime ledger exposure
redaction or withheld evidence used to strengthen public claims
missing privacy review for privacy-leak corrections
old-artifact deletion as correction
missing citation warning / redirect guidance
missing custody chain / bundle audit binding
```

## 10. Operational reading

The public release lifecycle is now:

```text
disclose -> release -> hash custody -> observe -> errata | supersede | retract -> public notice -> negative cache / citation update
```

This layer does not certify lawfulness, safety, deployment status, C-A1 identity, or live truth. It only governs public artifact correction records.
