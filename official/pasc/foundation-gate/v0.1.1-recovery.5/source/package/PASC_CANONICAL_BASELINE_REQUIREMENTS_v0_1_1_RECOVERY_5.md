# PASC Canonical Baseline Requirements v0.1.1 — Recovery Build 5

## 0. Status

`PASC-GB-006 = OPEN_BLOCKING`.

This document defines what must be known before any parent source can carry normative
weight in PASC. The accompanying machine inventory pins 39 GitHub files at immutable
commits, but does not declare the current corpus baseline closed.

## 1. Required source record

Each load-bearing source requires one
`PASC_CANONICAL_SOURCE_RECORD_v0_1_1_RECOVERY_5`. The machine inventory implements this
contract now, but every unresolved value is an explicit typed state rather than an
omitted key. A record is admissible only with
`record_completeness=CLOSURE_COMPLETE`; every current record is
`CLOSURE_INCOMPLETE` and grants no normative weight.

```yaml
source_record_schema_id: PASC_CANONICAL_SOURCE_RECORD_v0_1_1_RECOVERY_5
source_id: <stable-id>
family: <closed-family>
canonical_owner: {candidate: <person/project/repository>, verification_status: <typed>}
artifact_id: {candidate: <stable-artifact-id>, verification_status: <typed>}
version: {candidate: <exact-version-or-marker>, verification_status: <typed>}
authoritative_locator:
  candidate_github_byte_locator: <immutable-commit-url>
  release_doi: <doi-or-null>
  verification_status: <typed>
repository: <owner/repository>
immutable_commit_or_release: <exact>
path: <exact-repository-path>
git_blob_sha1: <exact-or-not-applicable>
content_hash_sha256: <sha256>
size_bytes: <integer>
schema_hash: {value: <sha256-or-null>, status: <typed>}
status:
  class: <stable|draft|experimental|obsolete|withdrawn>
  declared_status: <exact-source-claim>
  verification_status: <typed>
maturity: {candidate: <declared-level>, verification_status: <typed>}
supersedes: [<bindings>]
superseded_by: [<bindings>]
supersession_review_status: <typed>
controlling_sections: [<section-bindings>]
controlling_sections_review_status: <typed>
pasc_relation_class: <NORMATIVE_IMPORT|CONSTRAINED_INTERFACE|CONDITIONAL_PROFILE_INPUT|INFORMATIVE_CONTEXT|PARENT_RESULT_ONLY|EXTERNAL_NEGATIVE_OPERATION_TARGET_ONLY|BLOCKING_NONCLAIM_ONLY|BASELINE_CONTROL_INPUT>
pasc_relation_scope: <exact-bounded-candidate-scope>
current_disposition: <INFORMATIVE_CONTEXT|DEFERRED_UNPINNED>
byte_pin_status: <PINNED_GITHUB_BYTES|BYTE_UNPINNED>
canonical_admission_status: <OPEN_BLOCKING|ADMITTED>
adapter_binding: {binding: <reference+hash-or-null>, status: <typed>}
claim_ceiling: {candidate_scope: <typed-ceiling>, status: <typed>}
reserved_territory: [<typed-area>]
reserved_territory_review_status: <typed>
known_conflicts: [<conflict-id>]
known_conflicts_review_status: <typed>
verified_at: <timestamp>
verification_scope: <typed>
verification_receipt_binding: {binding: <binding-or-null>, status: <typed>}
independent_reviewer_dispositions: [<exactly two or more bindings>]
record_completeness: <CLOSURE_COMPLETE|CLOSURE_INCOMPLETE>
unresolved_required_fields: [<exact-field-name>]
gap_ids: [<BASE-GAP-* identifiers>]
normative_weight_in_pasc: <boolean>
```

An empty array never means “verified none” when its companion review status is
`UNRESOLVED_*`. `byte_pin_status=PINNED_GITHUB_BYTES` proves only the exact retrieved
bytes; it is orthogonal to `canonical_admission_status`. The legacy disposition label
`DEFERRED_UNPINNED` means canonical admission is unclosed and may coexist with a byte
pin; it must not be parsed as `BYTE_UNPINNED`.

A title, URL, copied snapshot, citation, or repository branch alone is insufficient.
An immutable commit and matching hash establish byte identity, not ownership truth,
supersession, maturity, compatibility, adapter correctness, authority, or continuity.

## 2. Minimum source families

1. `c=a+b` / Theoretical Core / L4 Boundary.
2. SER and SER-FED.
3. Pre-Lineage Boundary.
4. PAMDC and PACR.
5. Anchor Directive Bundle.
6. A6 and A6-CTP.
7. Continuity Bundle, Cold Wake, Continuity Metric/equivalence semantics.
8. Beacon.
9. AGL.
10. ARL standing/admissibility/freeze/quarantine/re-entry.
11. L4 Witness.
12. Entity vs Profile and custody/recovery classification.
13. AI Social Role Separation and Memory Custody.
14. Runtime Authority revocation and audit.
15. CCDP/CMAM/AMCL and protected-person profiles.
16. Assertion-strength, canonical ownership, precedence, cross-layer invariants,
    intake, supersession, deprecation, and anti-echo policies.

## 3. Reserved territory tests

The baseline review must demonstrate that PASC does not:

- create lineage where Pre-Lineage reserves judgment;
- transfer human responsibility or liability contrary to SER;
- mint PACR re-entry or Continuity Metric outcomes;
- convert A6 composition into identity;
- convert Beacon recognition into child/succession permission;
- replace ARL or jurisdictional process;
- issue executable Runtime Authority;
- override CCDP adult migration or protected-person rules.

## 4. Conflict resolution

Conflicts are resolved by typed axis, not by one global document ranking. A newer or
more specific file does not automatically control another axis. If ownership,
precedence, compatibility, or adapter semantics remain unresolved, the source is
`DEFERRED_UNPINNED` and cannot support an admission.

## 5. Closure evidence

Closure requires two independent reviewers to reproduce the inventory, hash every
source, inspect supersession and reserved territory, and agree on every disposition and
claim ceiling. Model-assisted review may prepare the inventory but does not satisfy
independent-human-review criteria.

Each reviewer must independently retrieve every source from its immutable locator,
recompute content hashes, verify the candidate canonical owner and package-specific
release/DOI, inspect all supersession/deprecation records and controlling sections,
reproduce every adapter mapping and claim ceiling, and issue a content-bound disposition.
Reviewer independence must be proven at credential, effective-control, revocation-
control, and prohibited failure-domain levels. Disagreement, missing source bytes, a
draft/reserved ambiguity, or an absent adapter keeps the source `DEFERRED_UNPINNED`.

## 6. Recovery 5 machine-inventory result

`PASC_CANONICAL_BASELINE_INVENTORY_v0_1_1_RECOVERY_5.json` records exact GitHub byte
bindings across all 16 required families. It also records six blocking gaps:

1. this authenticated machine pass located PACR and Anchor Directive Bundle in the
   integrated AGI hardening tree but not in the pinned dedicated DOI-bound
   `c-hardening-pack` tree; this is not an independent absence receipt;
2. Entity-versus-Profile GitHub content is a metadata bridge, not the canonical source;
3. versioned PASC adapter objects/hashes and claim ceilings remain absent;
4. no competent-jurisdiction protected-person applicability record is pinned;
5. draft/RFC/research/reserved sources cannot be promoted by commit/DOI alone;
6. independent human baseline reviewers equal zero.

Therefore every candidate normative/constrained/conditional relation in the inventory
has `normative_weight_in_pasc=false`, and `PASC-GB-006` remains `OPEN_BLOCKING`.
