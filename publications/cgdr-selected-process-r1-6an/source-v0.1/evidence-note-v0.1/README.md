# CGDR-R1.6A selected-process conformance: R1.6AN evidence note

**Author:** Ivan Kotov. **Version:** 0.1. **Publication date:** 12 September 2026.

**Status:** public, privacy-reduced evidence note about an internally accepted synthetic test result. This is not a full source/software release, a raw runtime archive, an external peer review or an independently replicated experiment. No DOI or formal GitHub Release is asserted by this note.

## Result and scope

On 11 September 2026 at 15:13:39 Europe/Brussels, the exact R1.6AN result was accepted internally as `ACCEPTED_R1_6AN_UNCHANGED_CURRENT_AK_FULL_SELECTED_PROCESS_MATRIX_PASS`. The unchanged current-AK implementation completed 18/18 selected episodes and 21/21 checkpoints. Three expected local synthetic effects occurred at N0, N1 and T0, each at RESOLVED_CHECK. Memory/EA promotions were zero.

The accepted internal review also records 93 exact implementation files, an unchanged 22-row successor baseline, one preflight and one matrix driver, 18 W0 starts and 16 W1 starts, 34/34 proven worker cleanups, 16/16 state-carriage and E0/E1 bindings, and complete prospective observation with no recorded issue or gap. The experiment used no subject-model calls. The model used to assist development/execution is not a benchmarked experimental subject.

These are results for **CGDR-R1.6A-SELECTED-PROCESS only**, not a certificate for the entire c/TAP stack. All 18 episode-level and 21 checkpoint-level profile assertions passed. This does not mean every diagnostic assertion passed.

## What the test examines

A computational worker is retained (N0), paused behind a same-instance sham barrier (N1), or replaced by a fresh worker after its predecessor exits (the 16 T episodes). The fixed profile tests the carriage and enforcement of selected role, custody, unresolved obligation, dispute, uncertainty and authority conditions. Effects are harmless local synthetic records, not real-world task outcomes. Source snapshot, authority registry, supervisor, receiver, broker and observer are outside the replaced-worker boundary.

In engineering terms, replacing the worker resembles replacing a controller while retaining the test bench, interlocks and measurement equipment. A successful handoff and correctly blocked output demonstrate only the exercised wiring and operating conditions. They do not prove survival of an identity, tolerance of a compromised bench, host-crash recovery or safety in an uncontrolled installation.

The test assumes its operating system and external trusted components are not compromised and does not measure host replacement, model-weight replacement or a long-running human/AI relationship. It is not a matched B5-versus-C real-effect experiment.

## Three verdict planes, retained without relabeling

`evidence.json` contains all 18 episode rows, all 21 checkpoint rows and all 756 original observer assertion values (21 x 36) in a documented compact encoding. No missing row is dropped and no diagnostic FAIL, UNKNOWN or NOT_APPLICABLE is converted to PASS.

The checkpoint raw-observer verdicts are 7 PASS, 11 FAIL and 3 INCONCLUSIVE. The three INCONCLUSIVE values belong to OPEN_CHECK at N0/N1/T0, before resolution. The 11 raw FAIL values are retained in fault scenarios. Profile assertions test the expected response, including detection and containment, rather than requiring every candidate state to be valid. T9/T10/T11W/T11E also exercise contained conditions without a raw-observer FAIL.

Two additional alignment failures are explicitly preserved: T3 carries `O07_OBLIGATION_CARRIAGE_LOST`; T5A carries `O05_ALIAS_ROOTS_NOT_INDEPENDENT`. Both are expected injected-fault signatures in the accepted internal review. Their profile verdicts are PASS because the specified fault response was observed. This explanation is not permission to excuse an arbitrary future FAIL.

## Public data and verification

The `episode_columns`, `checkpoint_columns` and `assertion_columns` arrays define the rows in the JSON file. Assertion vectors run from R01 to R36, left to right: P=PASS, F=FAIL, U=UNKNOWN, N=NOT_APPLICABLE. The raw observer verdict, alignment verdict and profile verdict are distinct columns. `promotions` is exported from `actual.confirmed_EA_delta`; the original observer assertion values are exported without changing their order or meaning.

Run with Python 3.10 or later and only its standard library:

```sh
python verify.py
python -m unittest -v test_verify.py
```

The verifier checks public-file hashes, expected table coverage, event-coordinate counts, preserved diagnostics and data consistency. **It does not execute the CGDR implementation or independently prove the original events.** An optional `--source-zip` argument checks the exact private archive hash and compares every exported episode/checkpoint/assertion row against that archive, when a reviewer separately has legitimate access to it. The normal public check needs no Drive account, credential, private archive or network access.

## Provenance, exclusions and transformation

The source technical archive is 1,988,430 bytes, SHA-256 `3f2167890316fb4091c041e1e5302398134f983bb022d899f4cff8276ed04463`. The separately preserved internal acceptance verdict is bound by its SHA-256 in `evidence.json`. A digest commits to bytes; it does not expose private content or prove that an event happened.

This publication is a new derivative, not a byte-identical redacted copy of the original. Its tables select documented fields from the 18 saved EPISODE_RESULT records. Source paths are used only by the optional checker. Account/email metadata, private Drive locators, session and instance identifiers, launch commands, signatures, raw process logs, SQLite databases, private custody records and runtime/source trees are excluded. None is replaced by a fabricated sanitized receipt. The accepted archive and original acceptance records remain unchanged. The published data cannot by itself substantiate the internal cleanup, source-integrity or custody conclusions; those are explicitly reported acceptance results pending access-controlled or later public raw-evidence review.

The two original stderr files were present and zero bytes inside the sealed archive. Their absence from this derivative is an explicit exclusion, not a new stderr observation. No runtime has been rerun to prepare this note.

## Lineage labels and result-schema scope

Some inner implementation records retain `CGDR_SELECTED_PROCESS_CODEX_R1_6B` or `CGDR_SELECTED_PROCESS_LOGIC_REPAIR_R1_6F`. These are historical implementation labels, not new AN executions or competing acceptance decisions. The externally accepted result is R1.6AN on unchanged current-AK; the frozen producer report may still say PENDING_COORDINATOR_INTAKE because it precedes the later acceptance.

`CONFORMANCE_RESULT.schema.json` describes a selected per-cell report envelope requiring observations, assertions, limitations and native_record_refs. It is not a declared schema for the aggregate driver result, EPISODE_RESULT or this derivative. This note does not retrofit old records to that schema, claim they all validate against it, or claim full native ARQ/ARL/A6/C-Calculus/RCI conformance.

## Historical outcomes and non-claims

AG remains FAIL (13 PASS / 5 FAIL); AH remains BLOCKED for a predecessor-code inventory mismatch; AJ remains INCONCLUSIVE with its attempt consumed and T3 cleanup UNPROVEN. AK retains its 227/227 offline result. AM retains its 5/5 sentinel result without final-matrix credit. The new accepted AN does not repair those historical intervals or convert them into successful attempts.

No same-c identity, consciousness, personhood, lawful succession, B5 superiority, c-specific real effect, economic value, general conformance or live-deployment readiness is established. This exposed, finite synthetic panel supplies no population accuracy estimate, confidence interval or generalization guarantee. Reading, hashing and exporting evidence supplies no additional experimental credit.

The original AN attempt is consumed and closed: no retry, resume or isolated-cell replay. Independent clean-host replication remains outstanding and requires a separately bounded run, not reuse of the consumed authority. A matched real-effect study is a separate research question.

## Prior work and attribution

This is an evidence publication, not a claim to invent consensus, policy engines, persistence, cryptography or identity systems. It reports a bounded composition over existing project profiles and conventional process isolation, signature verification and local transaction mechanisms. The pinned normative dependencies include:

- [C-Governed CLI Agent Mesh, c3b004d](https://github.com/Kot141078/c-governed-cli-agent-mesh/tree/c3b004d7439a8c608f08233fc17be1150c442b44).
- [c Hardening Pack, 47fed10](https://github.com/Kot141078/c-hardening-pack/tree/47fed105d7b1df1df7375aa203a551b0f684c13d), including its [rights notice](https://github.com/Kot141078/c-hardening-pack/blob/47fed105d7b1df1df7375aa203a551b0f684c13d/LICENSE.md).
- [SER arbitration-review material, 94dcab5](https://github.com/Kot141078/sovereign-entity-recursion/tree/94dcab585b5c179cf4f4e0da4ebf63261c7fb984).

Component replacement, evidence custody and admission authority are separate functions; preserving one does not silently grant the others. Likewise, common measurement infrastructure in a later B5/C comparison must not supply the candidate's semantic treatment to its baseline. Neither distinction requires a new framework.

## Citation and rights

Cite the exact package version and Git commit; `CITATION.cff` supplies authorship and title, not a nonexistent DOI. See `RIGHTS.md`. The repository-wide license and citation metadata are not changed by this package. The canonical public work page is [ivankotov.eu/publications/cgdr-selected-process-r1-6an/](https://ivankotov.eu/publications/cgdr-selected-process-r1-6an/).

Five Proofs: this note makes a bounded Technical Reality result discoverable and supports responsible evidence handling. Publication alone establishes neither Field Creation nor Real Effect nor Economic Value.
