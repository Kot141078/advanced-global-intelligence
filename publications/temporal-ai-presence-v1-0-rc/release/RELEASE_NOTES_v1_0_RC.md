# Temporal AI Presence Profile v1.0 RC - Release Notes

## Status

This is a pre-publication release candidate. It has no standalone DOI and makes no full TAP conformance claim.

## What changed from v0.1

- Standalone canonicalization: the historical parent-profile is represented as a dedicated release-candidate package without modifying its bytes.
- Historical provenance: conceptual precursor, formal v0.1, parent publication, later corpus bridge, and RC custody are separated explicitly.
- Issue-state correction: `TAP-OI-001` through `TAP-OI-007` retain their identifiers but now record the R0 dispositions and actual artifacts.
- MOT-c downstream bridge: MOT-c v0.1 is linked as later adjacent theory, never as a TAP dependency or implementation proof.
- Evidence-state integration: the exact R0 `TAP-T01` through `TAP-T10` statuses and gaps are frozen in both the profile and a machine-readable evidence baseline.
- Machine-readable contract: a JSON normative instance and validating JSON Schema encode the TAP taxonomy, tests, evidence classes, relations, provenance, and claim ceiling.
- Citation metadata: standalone release-candidate `CITATION.cff` metadata is supplied without assigning a TAP DOI.
- Claim ceiling: the package explicitly limits current public implementation claims and preserves `M4_FULL_PASS=false`.

## What did not change

- `Temporal AI Presence = sustained bounded AI participation across time.`
- Temporal AI Presence is not `c` by default.
- All valid c-class systems are TAP; not all TAP systems are c.
- The core TAP taxonomy, memory classes, privilege classes, state machine, claim classes, conformance classes, evidence classes, and red-line failures remain intact.
- `TAP-T01` through `TAP-T10` remain the mandatory tests.
- Parent mechanisms retain precedence; the RC does not redefine `c`, L4, SER, L4 Witness, ARQ `c[q]`, SYNAPS, or Memory Custody.
- Non-personhood, non-consciousness, non-sovereignty, and authority boundaries remain explicit.

## What remains for R2 and R3

R2 remains responsible for implementation/evidence closure, the exact TAP-specific test suite, and especially the `TAP-T06` cloud-oracle implementation binding. It must not treat local unpublished Ester candidates as public evidence.

R3 remains responsible for the public evidence package, final publication metadata, standalone DOI deposition, and release publication. No DOI has been guessed or reserved here.
