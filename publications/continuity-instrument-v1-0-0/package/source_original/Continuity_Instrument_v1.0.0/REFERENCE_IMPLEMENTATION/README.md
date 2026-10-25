# CI reference implementation

`ci_profile.py` is a standard-library-only, inert reference transformation for the Continuity Instrument (CI) evidence-bound continuity-age / formation-depth vector. It accepts caller-supplied records, validates the v1 structural and relational contract, and emits canonical JSON. Importing the module has no side effects. Running it reads only the named input and writes only standard output or an explicitly named output path.

The implementation does not collect evidence, decide whether evidence is true or admissible, inspect a host, call a model, use a network, launch a process, or modify a CI/R160 evidence area. It does not establish personhood, metaphysical or legal identity, wall-clock age, biological age, uninterrupted existence, authority, scientific validity, qualification, or publication readiness.

## Versioned contracts

- Input schema: `schemas/ci-profile-input-v1.schema.json`
- Input schema version: `ci-profile-input/v1`
- Output schema: `schemas/ci-profile-output-v1.schema.json`
- Output schema version: `ci-profile-output/v1`
- Implementation version: `ci-profile-reference/1.0.0`

Both schemas use JSON Schema Draft 2020-12. The Python implementation also checks constraints that JSON Schema does not conveniently express here: ordered bounds, containment in the observation window, identifier uniqueness, duration eligibility only for admitted intervals, mandatory non-claim tokens, and the absence of overlap between admitted duration intervals and known pauses.

## Invocation

From `publication_draft/`:

```text
python REFERENCE_IMPLEMENTATION/ci_profile.py INPUT.json
python REFERENCE_IMPLEMENTATION/ci_profile.py INPUT.json --output OUTPUT.json
```

Success returns exit code `0`. Invalid input or an I/O error returns `2` and writes one diagnostic to standard error. Output is UTF-8 canonical JSON with sorted object keys, compact separators, and one trailing line feed. Duplicate JSON object keys are rejected.

## Deterministic policies

- Time is represented as integer ticks on the caller-declared `time_axis`. The implementation never reads a system clock or converts ticks into a biological or wall-clock age.
- Participation and pause intervals are closed-open: `[start, end)`.
- `W_first` is ordered by lower bound ascending, upper bound ascending, then identifier. `W_last` is ordered by upper bound descending, lower bound descending, then identifier. The selected witnesses must be admitted.
- `I_verified` contains only admitted intervals marked eligible for duration.
- `D_verified` is the length of the union of eligible intervals. Overlap is counted once.
- `P_known` retains evidenced pause records. An admitted eligible interval that overlaps a known pause is rejected as contradictory input.
- `G_unexplained` is the complement, inside the declared observation window, of the union of `I_verified` coverage and known-pause coverage. A computed gap is unknown; it is not active time, inactive time, or zero.
- Replay, fork, restore, and cold-wake records are partitioned into separate coordinates and ordered by time bounds then identifier.
- Memory, governance, witness, and authority lineages remain separate and are ordered by time bounds then identifier.
- Irreversible transitions remain scoped records with their decision rule and evidence references. Lack of a known reversal is not calculated as irreversibility.
- Structured uncertainty is preserved. `not_assessed` is distinct from an empty or zero value.
- The claim ceiling is emitted separately from the vector. The implementation validates structure and mandatory prohibited inferences; it does not judge the truth of free-text allowed claims and cannot raise the supplied evidence ceiling.

`formation_depth_vector_sha256` is SHA-256 over the UTF-8 canonical JSON bytes of the `formation_depth_vector` object, without a trailing line feed. It is a reproducibility checksum, not an evidence-truth or identity attestation.

## BACON boundary

The output is designed so that CI can later be mapped into BACON through an explicit, versioned adapter. Such an adapter would need to preserve every vector coordinate, branch distinction, uncertainty value, claim ceiling, schema version, and source checksum. This draft does not implement that adapter, expand the BACON name, assign semantics to BACON, or claim compatibility with it.

## Tests and dependency boundary

Run the focused tests from `publication_draft/`:

```text
python -m unittest tests.test_ci_profile
```

The implementation and tests import only Python standard-library modules. The schemas are data files and do not require a runtime schema package. Passing the tests establishes only the behavior exercised by those tests; it is not CI qualification, R160 evidence, scientific validation, security review, or conformance certification.
