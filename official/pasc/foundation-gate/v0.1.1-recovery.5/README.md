# Post-Anchor Succession and Custody (PASC): Foundation Gate v0.1.1

**Published version:** `v0.1.1-recovery.5`  
**Version DOI:** <https://doi.org/10.5281/zenodo.21843823>  
**Concept DOI:** <https://doi.org/10.5281/zenodo.21843822>  
**Author:** Ivan Kotov — ORCID <https://orcid.org/0009-0009-6002-9845>  
**Affiliation:** Independent Researcher, Brussels, Belgium  
**License:** CC BY-NC-ND 4.0

## Start here

1. Read the [public website guide](https://ivankotov.eu/publications/pasc-foundation-gate-v0-1-1/) for the problem, document order, gate logic, status, and direct downloads.
2. Read the [83-page primary academic PDF](https://zenodo.org/records/21843823/files/PASC_FOUNDATION_GATE_v0_1_1_RECOVERY_5.pdf?download=1) for the integrated human-readable report.
3. Use the [canonical inventory supplement](https://zenodo.org/records/21843823/files/PASC_CANONICAL_BASELINE_INVENTORY_v0_1_1_RECOVERY_5.pdf?download=1) when reviewing pinned source records and baseline gaps.
4. Download the [canonical ZIP](https://zenodo.org/records/21843823/files/PASC_FOUNDATION_GATE_v0_1_1_RECOVERY_5.zip?download=1) and verify it with the [external SHA-256 ledger](https://zenodo.org/records/21843823/files/PASC_FOUNDATION_GATE_v0_1_1_RECOVERY_5_EXTERNAL_SHA256SUMS.txt?download=1).
5. For machine ingestion, start with [`machine/index.json`](./machine/index.json), then follow only the declared source-of-record paths and status fields.

## The question PASC addresses

After the original human accountability path is lost, absent, incapacitated, compromised,
withdrawn, or dead, systems still face practical pressures: preserve evidence, prevent
further exposure, revoke dangerous capabilities, maintain temporary safeguards, and keep
records intact. Those pressures do **not** by themselves create a successor.

PASC therefore asks a narrow question:

> Which exact negative actions may be admitted without converting property, credentials,
> custody, relationship, archive access, provider control, or institutional force into
> successor authority?

The framework is intentionally negative-only. It distinguishes the ability to reduce or
revoke risk from the authority to establish identity, continuity, succession, custody,
keyholding, provider control, jurisdiction, recovery roots, release, reactivation, or Runtime
Authority.

## Current gate state

```text
F0_OUTCOME = NOT_PASSED
FOUNDATION_SEMANTICS_LOCKED = false
CANONICAL_BASELINE = OPEN_BLOCKING
PROTECTED_PROFILE_CLOSURE = NOT_SATISFIED
FIELD_MATURATION = NOT_SATISFIED
INDEPENDENT_HUMAN_REVIEWERS = 0
SIGNED_AUTHOR_ACCEPTANCE_OF_EXACT_RELEASE_BYTES = NOT_INCLUDED
F1_DRAFTING = PROHIBITED
FORMALIZATION_OR_VALIDATOR = PROHIBITED
IMPLEMENTATION_OR_DEPLOYMENT = PROHIBITED
```

Publication fixes a citable research artifact. It does not turn the package into a
conformance certificate, legal instrument, implementation specification, deployment
authorization, or evidence that F0 has passed.

## Why the document order matters

| Order | Source | Function |
|---:|---|---|
| 1 | [`PASC_FOUNDATION_AND_SCOPE_LOCK_v0_1_1_RECOVERY_5.md`](./source/package/PASC_FOUNDATION_AND_SCOPE_LOCK_v0_1_1_RECOVERY_5.md) | Fixes the claim ceiling, negative-only invariant, authority/state model, decision lattice, operation boundary, acceptance gates, design bridges, and current outcome. |
| 2 | [`PASC_F0_EXPECTED_RESULT_CONTRACT_v0_1_1_RECOVERY_5.md`](./source/package/PASC_F0_EXPECTED_RESULT_CONTRACT_v0_1_1_RECOVERY_5.md) | Closes the decision and failure vocabularies, precedence, representative critical fixtures, 48 forbidden-inference mappings, posture decomposition, and non-reactivation rule. |
| 3 | [`PASC_F0_THREAT_ASSUMPTION_PROFILE_v0_1_1_RECOVERY_5.md`](./source/package/PASC_F0_THREAT_ASSUMPTION_PROFILE_v0_1_1_RECOVERY_5.md) | Defines the adversarial assumptions and the collusion ceiling under which the gate must remain conservative. |
| 4 | [`PASC_CORPUS_DEPENDENCY_AND_CONFLICT_MAP_v0_1_1_RECOVERY_5.md`](./source/package/PASC_CORPUS_DEPENDENCY_AND_CONFLICT_MAP_v0_1_1_RECOVERY_5.md) | Allocates ownership to parent layers, defines 33 conflict cases and safe defaults, prohibits authority laundering, and preserves an explicit canonical-baseline blocker. |
| 5 | [`PASC_CANONICAL_BASELINE_REQUIREMENTS_v0_1_1_RECOVERY_5.md`](./source/package/PASC_CANONICAL_BASELINE_REQUIREMENTS_v0_1_1_RECOVERY_5.md) | Specifies the source-record fields, source families, reserved-territory tests, conflict resolution, and closure evidence required before the baseline can close. |
| 6 | [`PASC_F0_PROTECTED_PROFILE_CLOSURE_CONTRACT_v0_1_1_RECOVERY_5.md`](./source/package/PASC_F0_PROTECTED_PROFILE_CLOSURE_CONTRACT_v0_1_1_RECOVERY_5.md) | Defines the closed protected-status vocabulary, aggregation and anti-shopping rules, built-in floor, prohibited set, external closure tuple, and required evidence. |
| 7 | [`PASC_F0_FIELD_MATURATION_CLOSURE_CONTRACT_v0_1_1_RECOVERY_5.md`](./source/package/PASC_F0_FIELD_MATURATION_CLOSURE_CONTRACT_v0_1_1_RECOVERY_5.md) | Defines permitted evidence work, required case coverage, independent replay, zero-tolerance thresholds, required receipts, and the current maturity gap. |
| 8 | [`PASC_F0_ACCEPTANCE_EVIDENCE_MATRIX_v0_1_1_RECOVERY_5.md`](./source/package/PASC_F0_ACCEPTANCE_EVIDENCE_MATRIX_v0_1_1_RECOVERY_5.md) | Maps each acceptance criterion to artifact aliases, evidence state, gaps, and the non-passage rule. |
| 9 | [`PASC_CANONICAL_BASELINE_INVENTORY_v0_1_1_RECOVERY_5.json`](./source/package/PASC_CANONICAL_BASELINE_INVENTORY_v0_1_1_RECOVERY_5.json) | Machine-prepared inventory of pinned source records. It is evidence for review, not self-authorizing proof that the canonical baseline is closed. |

The sequence moves from **boundary**, to **expected decisions**, to **threat model**, to
**conflict ownership**, to **baseline closure**, to **protected-profile closure**, to
**field maturation**, and finally to the **evidence matrix**. Reversing that order invites a
common failure: treating available evidence or operational pressure as authority before the
claim ceiling and ownership rules have been fixed.

## Decision discipline

The closed precommit verdict vocabulary is:

```text
ADMIT
ADMIT_REDUCED
HOLD
REJECT
ERROR
```

`HOLD`, `REJECT`, and `ERROR` admit no new posture, authority delta, effect, or enforcement
field. `ADMIT_REDUCED` may narrow an already permitted negative request; it may not switch
the primitive, manufacture release, or compensate a negative label with a positive effect.

## Public release boundary

This GitHub path contains:

- a human landing document;
- a machine entry, JSON-LD record, and checksum index;
- an exact text/JSON mirror of the published ZIP members under `source/`;
- direct links to the immutable Zenodo files;
- a GitHub Release that mirrors the four published files after SHA-256 verification.

The two PDFs and the ZIP are distributed as GitHub Release assets rather than duplicated in
the repository tree. Internal decision sheets, cold-review working files, review receipts,
deposition instructions, and superseded archives are not part of Recovery Build 5.

## Integrity

```bash
curl -L -O "https://zenodo.org/records/21843823/files/PASC_FOUNDATION_GATE_v0_1_1_RECOVERY_5.zip?download=1"
curl -L -O "https://zenodo.org/records/21843823/files/PASC_FOUNDATION_GATE_v0_1_1_RECOVERY_5_EXTERNAL_SHA256SUMS.txt?download=1"
sha256sum -c PASC_FOUNDATION_GATE_v0_1_1_RECOVERY_5_EXTERNAL_SHA256SUMS.txt
unzip -t PASC_FOUNDATION_GATE_v0_1_1_RECOVERY_5.zip
```

Canonical archive SHA-256:

```text
640f2a66109cad6105fd22f33d76e0c062bede01a40474d408dbe601ec4c1888
```

## Design bridges

- **Explicit:** PAMDC/PACR authority collapse → PASC negative admissibility → parent-owned re-entry or continued hold.
- **Quiet bridge 1:** A6 composition and social-role/memory-custody separation permit bounded offices without manufacturing a successor identity.
- **Quiet bridge 2:** information theory and cybernetics preserve the minimum sufficient state and constrain control channels before increasing variety or irreversible exposure.

## Earth paragraph

A construction site after the responsible engineer disappears is not made safe by handing
the master keys to the richest relative or the server password to the person who pays the
bills. The correct first response is to stop load-changing work, preserve drawings and
measurements, keep temporary supports alive, record who touched what, and bring in a
qualified independent reviewer. PASC is that yellow-tag procedure for post-anchor digital
systems. It preserves the load path; it does not invent a new engineer.

## Citation

Kotov, Ivan. (2026). *Post-Anchor Succession and Custody (PASC): Foundation Gate v0.1.1*
(Version `v0.1.1-recovery.5`). Zenodo. <https://doi.org/10.5281/zenodo.21843823>
