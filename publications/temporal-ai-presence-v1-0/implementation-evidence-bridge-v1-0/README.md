# Temporal AI Presence — Architecture-to-Code Evidence Bridge v1.0

Short identifier: **TAP-ACEB v1.0**

This release candidate makes four implementation-evidence chains inspectable:

`TAP requirement -> architecture -> selected source -> validator -> synthetic fixture -> receipt -> immutable public code candidate`

The normative source is *Temporal AI Presence Profile v1.0*, Version DOI [10.5281/zenodo.22070960](https://doi.org/10.5281/zenodo.22070960); Concept DOI [10.5281/zenodo.22070959](https://doi.org/10.5281/zenodo.22070959). One local reference implementation candidate supplied the implementation source used for this public evidence bridge. It does not define TAP.

## Scope

- TAP-T02: classified persistent memory, policies, review routes, and selected read/write source.
- TAP-T06: 179 lexical sites reduced to 177 network primitives, seven route classes, 4 bound / 173 out-of-scope rows, and 3/3 semantic cloud-AI authority routes.
- TAP-T07: 14 agent/executor-like surfaces, with 8 inventoried, 4 disabled by default, 1 legacy inactive, 1 out of scope, 0 hidden, and 0 unresolved.
- TAP-T08: `TAP-C=NOT CLAIMED`, `M4_FULL_PASS=false`, and deterministic rejection of prohibited c inferences.

Current public status is unchanged in R3E-A-R1. `PUBLICATION_ELIGIBILITY.json` states only the maximum supportable status after a later reviewed R3E-B publication.

## Offline validation

From the extracted bridge directory, write results outside the package:

```text
python -I -B run_offline_validation.py --output <external-result.json>
```

The harness uses the Python standard library only. It imports validators and static AST discovery adapters, never imports the implementation snapshot, denies socket and subprocess use, and fails closed on missing paths, hashes, rows, fixtures, or manifest entries.

## Reading order

1. `BRIDGE_SCOPE.md`
2. `NON_CLAIMS.md`
3. `REQUIREMENT_TO_CODE_MAP.md`
4. `SOURCE_SELECTION_MANIFEST.json`
5. `SOURCE_TRANSFORMATION_MAP.json`
6. `PUBLIC_EVIDENCE_MATRIX.csv`
7. `evidence/TAP_BRIDGE_TEST_RECEIPTS.jsonl`
8. `PACKAGE_MANIFEST.json` and `SHA256SUMS.txt`

## Engineering grounding

A temporal presence is not established by abstract persistence alone. Process restart and backup restoration test continuity and T02 memory governance; model replacement and hardware migration test identity/authority boundaries rather than model sameness; storage failure tests classified retention and recovery policy; network loss and cloud-oracle denial test T06 fail-closed behavior; compute-budget change tests L4 control without proving c; permission revocation and agent disablement test T07 pause/revoke custody. Deployment activation remains the explicit TAP-T03 boundary.

## License

Bridge documentation and evidence maps are CC BY 4.0. Selected implementation source, validators, fixtures, tests, and derivative executable harness are AGPL-3.0-or-later. See `LICENSE_POLICY.md` and `SOURCE_CODE_LICENSE_AGPL-3.0.txt`.
