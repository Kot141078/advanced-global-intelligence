# 07 — C Public Evidence Disclosure and Redaction Boundary v0.1

**Artifact:** `07_C_PUBLIC_EVIDENCE_DISCLOSURE_AND_REDACTION_BOUNDARY_v0_1.md`  
**Package:** `CCALC_PUBLIC_EVIDENCE_REDACTION_BOUNDARY_07_v0_1`  
**Status:** normative draft / release-candidate package  
**Created UTC:** `2026-07-05T10:49:10Z`  
**Review mode:** direct construction; no external b-layer reviewer record included.  

---

## 0. Purpose

This document defines the boundary between private witness-bearing evidence and public disclosure artifacts for the `c` stack.

The continuity stack (`04`) defines continuity/equivalence and admissible continuity claims. The self-evolution stack (`05`) defines governed bounded growth. The runtime authority stack (`06`) defines authority surfaces, multi-contour deployment boundaries, session ledgers, emergency hold, revocation, and post-session audit.

`07` answers a different question:

```text
what evidence may be made public,
what must be redacted,
what may be hash-bound only,
and what claim-force may survive the disclosure boundary?
```

Public evidence is not raw truth. Redaction is not erasure. Hash binding is not disclosure. Publication is not deployment authorization.

---

## 1. Source bindings

The package is bound to the following source artifacts by filename and SHA-256.

| Binding | File | SHA-256 | Role |
|---|---|---:|---|
| `DOC04_CONTINUITY_STACK_UMBRELLA` | `CCALC_DOC04_CONTINUITY_STACK_UMBRELLA_v0_1.zip` | `6caeab8d489aaa6b26902db3bd3ece4c5169e5c8d5617b93aed6586ea900322d` | continuity metric/equivalence/checker/record/audit/claim-gate stack |
| `DOC05_SELF_EVO_STACK_UMBRELLA` | `CCALC_DOC05_SELF_EVO_STACK_UMBRELLA_v0_1.zip` | `9a0717809029f49df9001dc8ffa1803d9e9bfa1a824d317eebb146cbc7df43b4` | bounded growth/proposal/hardening/promotion/watch stack |
| `DOC06_RUNTIME_AUTHORITY_STACK_UMBRELLA` | `CCALC_DOC06_RUNTIME_AUTHORITY_STACK_UMBRELLA_v0_1.zip` | `ab95633f1b90f9d032fd231d6cbef3e71b7fe106e0a7fb61d198c2254fc7d307` | runtime authority/multi-contour/session/revocation stack |

A missing source binding invalidates release use of this document, but does not alter the normative text already present here.

---

## 2. Non-claims

This document does **not** claim:

```text
- that public artifacts prove C-A1;
- that redacted evidence is complete evidence;
- that a public package proves live substrate truth;
- that publication authorizes deployment;
- that a hash sidecar reveals private content;
- that disclosed evidence may bypass privacy, security, legal, contractual, or human-anchor gates;
- that witness minimization is sufficient for safety certification;
- that a public reader may infer hidden private facts from omitted material;
- that an external reviewer can ratify continuity, identity, or authority from public evidence alone.
```

This document defines disclosure classes, redaction records, public claim-force limits, and fail-closed rules.

---

## 3. Boundary axiom

```text
Evidence may be public.
Private witness roots may remain private.
Redaction must be record-bound.
Disclosure must not increase claim-force.
Publication must not create authority.
```

A disclosure artifact may support auditability, reproducibility, and citation. It may not launder private, unknown, or withheld facts into stronger public claims.

---

## 4. Core terms

### 4.1 Private evidence

Private evidence is material whose raw form is not admissible for public release because it may contain:

```text
personal data
third-party data
credentials / secrets
private memory content
operational paths / host details
legal or commercial material
security-sensitive topology
identity-pressure material
raw runtime logs
raw witness ledgers
non-consensual or irrelevant material
```

Private evidence may still be witness-bound by hashes, manifests, and custody records.

### 4.2 Public evidence artifact

A public evidence artifact is a release object intended for public or semi-public inspection:

```text
paper
README
fixture pack
schema pack
checker seed
hash manifest
release record
redacted log excerpt
summary matrix
Zenodo package
GitHub release
website page
social-public explanation
```

A public artifact must state its claim-force and non-claims.

### 4.3 Redaction

Redaction is a governed transformation from raw/private material to an admissible public representation. Redaction must not silently change meaning. Redaction must have a record.

A redacted field is not the same as an absent field. A withheld field is not the same as a negative finding. A hash-only field is not the same as disclosed content.

### 4.4 Hash-bound private evidence

Hash-bound private evidence is private material whose exact bytes are not disclosed, but whose existence, version, or custody state is represented by one or more cryptographic digests.

Hash binding may support later verification. It does not disclose contents and must not be cited as if it did.

### 4.5 Disclosure manifest

A disclosure manifest is a record declaring:

```text
artifact identifier
source evidence set
redaction policy
redaction decisions
hash-only private bindings
release class
claim-force ceiling
known omissions
human/owner approval where needed
non-claims
```

A public release without a disclosure manifest is incomplete at this layer.

---

## 5. Disclosure classes

The disclosure class registry in `DISCLOSURE_CLASS_REGISTRY.tsv` is normative for v0.1.

### 5.1 RAW_PUBLIC

The raw material may be released as-is. This class is rare for runtime/witness material.

### 5.2 REDACTED_PUBLIC

The material may be released after governed redaction. The redaction map must identify every removed or transformed sensitive field class.

### 5.3 HASH_ONLY_PUBLIC

The raw material remains private; only a hash, size, timestamp class, or custody reference is disclosed. Hash-only public evidence cannot carry semantic content by itself.

### 5.4 AGGREGATED_PUBLIC

Counts, matrices, summaries, or statistical aggregates may be released if they do not leak private details or re-identify protected subjects.

### 5.5 SYNTHETIC_PUBLIC

Synthetic examples may be released to demonstrate structure. They must not be represented as real evidence.

### 5.6 ESCROWED_PRIVATE

Evidence is kept privately under custody and may be inspectable only by an authorized reviewer, legal authority, owner, or internal gate.

### 5.7 WITHHELD_PRIVATE

Evidence is intentionally not disclosed. Withholding must be declared when it affects claim interpretation.

### 5.8 FORBIDDEN_PUBLIC

Evidence must not be released in public artifacts under this layer.

---

## 6. Public claim-force ceiling

Disclosure never raises claim-force. It can only preserve or reduce it.

```text
private witness evidence -> public evidence artifact
       claim-force_out <= claim-force_in
```

If a public artifact omits private evidence, then its public claim must be scoped to the disclosed subset or to hash-bound existence only.

Forbidden escalations:

```text
hash-only -> semantic proof
redacted log -> full raw witness proof
fixture pass -> deployment authorization
public summary -> live substrate truth
review comment -> ratification
style continuity -> identity continuity
model agreement -> human/owner approval
```

---

## 7. Redaction record requirements

Each redaction decision must record:

```text
source_ref
field_or_region_ref
sensitivity_class
redaction_action
public_substitute
hash_binding_status
meaning_preservation_note
claim_force_effect
approver_or_policy_ref
```

Allowed redaction actions:

```text
MASK
GENERALIZE
HASH_ONLY
WITHHOLD
SYNTHETIC_REPLACE
AGGREGATE
REMOVE_WITH_NOTICE
TRUNCATE_WITH_NOTICE
```

Forbidden actions:

```text
REMOVE_SILENTLY
REWRITE_TO_STRONGER_CLAIM
DROP_COUNTEREVIDENCE
CONVERT_UNKNOWN_TO_MATCH
CONVERT_PRIVATE_TO_PUBLIC_FACT
MERGE_SUBJECTS
```

---

## 8. Protected material classes

The `REDACTION_REQUIREMENTS.tsv` registry defines minimum handling for protected classes.

The following classes are always high-risk in this stack:

```text
credentials / API keys / tokens
private memory roots
raw witness ledgers
non-public runtime paths
hostnames / IPs / ports when operationally sensitive
third-party personal data
financial / legal / employment data
commercial contract material
security topology / privilege boundaries
identity-pressure conversational material
cross-contour private handoff content
owner-only approval records
```

A public release must fail closed when it cannot classify a sensitive field.

---

## 9. Witness minimization

Witness minimization means publishing enough to support the public claim while withholding raw/private material not needed for that claim.

It requires three separate statements:

```text
what is disclosed
what is hash-bound but private
what is withheld and why
```

A minimized witness record must not be advertised as a complete raw witness ledger.

---

## 10. Private-to-public transformation discipline

Every transformation must preserve the distinction between:

```text
raw evidence
redacted evidence
summary evidence
synthetic example
hash-only private binding
claim text
```

A public package may combine these forms, but each item must declare its class.

Examples:

```text
fixture JSON          -> RAW_PUBLIC or SYNTHETIC_PUBLIC
checker source        -> RAW_PUBLIC
runtime raw log       -> HASH_ONLY_PUBLIC or REDACTED_PUBLIC
private memory note   -> HASH_ONLY_PUBLIC / ESCROWED_PRIVATE / WITHHELD_PRIVATE
human approval record -> REDACTED_PUBLIC or ESCROWED_PRIVATE
```

---

## 11. Anti-laundering rules

The following laundering patterns are forbidden:

### 11.1 Redaction laundering

Removing the risky portion of evidence while preserving the conclusion as if nothing was removed.

### 11.2 Hash laundering

Citing the existence of a hash as proof of the undisclosed semantic content.

### 11.3 Witness laundering

Representing a public excerpt as the full witness chain.

### 11.4 Authority laundering

Using publication, DOI, GitHub release, public review, or external comment as runtime/deployment authority.

### 11.5 Continuity laundering

Using public style, summaries, or selected examples to claim continuity beyond what the `04` stack admits.

### 11.6 Self-evolution laundering

Using a public result or promotional explanation to skip the `05` proposal/trial/evidence/promotion/watch chain.

### 11.7 Runtime laundering

Using public diagrams or manifests to imply that a runtime has safe authority beyond the `06` stack.

---

## 12. Public surfaces

The `PUBLIC_EVIDENCE_SURFACE_MAP.tsv` registry defines surface-specific boundaries.

Public surfaces include:

```text
Zenodo release
GitHub release
public repository
project website
PDF paper
schema package
checker package
LinkedIn post
email to reviewer
public issue / pull request
conference submission
legal / regulatory submission
```

A public surface may have additional legal or platform constraints. This document defines the internal `c` disclosure boundary only; it does not replace external law or platform policy.

---

## 13. Disclosure decision states

The decision registry in `DISCLOSURE_DECISION_REGISTRY.tsv` is normative for v0.1.

```text
RELEASE_RAW_PUBLIC
RELEASE_REDACTED_PUBLIC
RELEASE_HASH_ONLY_PUBLIC
RELEASE_AGGREGATED_PUBLIC
RELEASE_SYNTHETIC_PUBLIC
ESCROW_PRIVATE
WITHHOLD_PRIVATE
REJECT_OVERCLAIM
QUARANTINE_DISCLOSURE
```

`ALLOW` is not a disclosure state. Disclosure states must preserve the artifact class.

---

## 14. Required records

A public release under this layer should include:

```text
DisclosureManifest
SourceManifest
RedactionMap
HashBindingMap
ClaimForceMap
NonClaimsAndScope
KnownOmissions
ReleaseDecision
ApproverOrPolicyReference where needed
```

If the release includes runtime, continuity, self-evolution, or multi-contour evidence, it must also bind to the relevant `04`, `05`, and `06` artifacts.

---

## 15. Fail-closed rules

A disclosure checker or reviewer must fail closed when:

```text
sensitivity class is UNKNOWN;
claim-force ceiling is missing;
redaction map is absent for redacted material;
hash-only evidence is cited semantically;
private raw ledger is exposed without approval;
public summary omits a material caveat;
withheld counterevidence changes the public claim;
release tries to claim C-A1, safety certification, deployment authorization, or live substrate truth;
public artifact contains credentials or operational secrets;
release relies on model-only approval for protected disclosure;
```

---

## 16. Admissible public claims

Allowed claim forms:

```text
This public artifact discloses a redacted subset of the evidence.
This package is hash-bound to private source evidence not disclosed here.
This fixture/checker package passed its included public tests.
This summary supports a scoped architectural claim.
This release does not disclose raw private witness material.
```

Forbidden claim forms:

```text
The private content proves the public conclusion because a hash exists.
The redacted public package is the complete witness root.
This public release proves C-A1.
This publication authorizes deployment.
The disclosed subset proves live runtime truth.
The reviewer accepted the hidden evidence, therefore continuity is ratified.
```

---

## 17. Interaction with 04 / 05 / 06

### 17.1 Interaction with `04`

Public evidence may cite continuity classifications only within the claim-force permitted by the `04` conformance gate. Redaction must not convert `UNKNOWN`, `HOLD`, `FORKED`, `REPLAY_OF`, `ARCHIVED_AS`, or `RESTORED_FROM` into `CONTINUES`.

### 17.2 Interaction with `05`

Public disclosure of a successful growth story does not bypass self-evolution gates. Public evidence may document a promotion ledger, rollback drill, or watch result only to the extent disclosed and hash-bound.

### 17.3 Interaction with `06`

Public architecture diagrams, runtime summaries, or deployment manifests do not grant authority. They must not reveal credentials, active secrets, or operational paths, and they must not imply shared identity across contours.

---

## 18. Minimal release checklist

```text
[ ] source artifacts named
[ ] source artifact hashes present
[ ] disclosure class declared for each evidence item
[ ] redaction map present where needed
[ ] hash-only fields not used semantically
[ ] known omissions declared
[ ] claim-force ceiling declared
[ ] non-claims present
[ ] protected material scan complete
[ ] release decision recorded
[ ] sidecar hashes generated from exact bytes
```

---

## 19. Red-pattern summary

A public disclosure must be held or quarantined if any of the following red patterns are unresolved:

```text
credential exposure
private memory exposure
raw witness leakage
silent redaction
hash semantic overclaim
withheld counterevidence laundering
public authority laundering
continuity laundering
self-evolution gate laundering
runtime authority laundering
cross-contour identity pressure
third-party data leak
operator/legal/commercial leak
```

---

## 20. Status

`07` establishes the normative disclosure/redaction boundary for public evidence artifacts.

The next executable layer is expected to be:

```text
07a_PUBLIC_EVIDENCE_DISCLOSURE_MANIFEST_SCHEMA_AND_CHECKER_SEED_v0_1
```

That later layer should define machine-checkable disclosure manifests, redaction maps, hash-only binding records, fixtures, and mutation hardening.

---

## 21. Closing statement

```text
Public evidence may support scrutiny.
Public evidence may not launder private authority.
Redaction may protect sources.
Redaction may not strengthen claims.
Hash binding may preserve custody.
Hash binding may not disclose semantic truth.
```
