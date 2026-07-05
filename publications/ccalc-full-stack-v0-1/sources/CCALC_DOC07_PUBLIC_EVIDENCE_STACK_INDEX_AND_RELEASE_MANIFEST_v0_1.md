# CCALC Doc07 Public Evidence Stack — Index and Release Manifest v0.1

**Artifact:** `CCALC_DOC07_PUBLIC_EVIDENCE_STACK_UMBRELLA_v0_1`  
**Generated UTC:** `2026-07-05T12:16:34Z`  
**Status:** `CURRENT_DOC07_PUBLIC_EVIDENCE_STACK_UMBRELLA`

## 1. Purpose

This umbrella closes the current `07` layer as a packaged public-evidence disclosure, redaction, release, correction, and citation-surface stack.

The stack's operational formula is:

```text
evidence -> classify -> redact/hash/withhold -> claim-force ceiling -> release -> correction ledger -> citation-surface sync
```

The core rule is:

```text
public release supports scrutiny, not authority transfer.
```

## 2. Included Components

| Layer | Role | Package SHA256 | Executable status |
|---|---|---:|---|
| `07` | public evidence disclosure / redaction boundary | `afced9a2c6830faebcb98d37195d56d6216fe8211d30bcb5bdf2d2ce6e4a4538` | normative package; no executable fixtures expected |
| `07a` | public evidence disclosure manifest schema + checker seed | `21cfd692d3520a57b46780d093430b123bcf3439ed73781f3074a47f6af15893` | fixtures 85/85 PASS; mutations 15/15 CAUGHT |
| `07b` | public release bundle + hash custody audit | `b84ccc97d9564b6f95e92b0acd68481aa2d316d7e6ceb6c561bcddf8433be246` | fixtures 82/82 PASS; mutations 21/21 CAUGHT |
| `07c` | public retraction / supersession / errata ledger | `d191c3202c1463cf741f82c978d8414041432174cdff891947e515e32358eec3` | fixtures 78/78 PASS; mutations 18/18 CAUGHT |
| `07d` | public corpus index + citation surface sync | `3c22108b7305ff755d236de08e73bbacf4f34c8a8f6bcbef11ed8d41272db512` | fixtures 90/90 PASS; mutations 21/21 CAUGHT |

## 3. Upstream Source Bindings

| Source | Role | SHA256 |
|---|---|---:|
| `doc04_continuity_stack` | continuity metric/equivalence/checker/record/audit/claim-gate stack | `6caeab8d489aaa6b26902db3bd3ece4c5169e5c8d5617b93aed6586ea900322d` |
| `doc05_self_evo_stack` | bounded growth/proposal/hardening/promotion/watch stack | `9a0717809029f49df9001dc8ffa1803d9e9bfa1a824d317eebb146cbc7df43b4` |
| `doc06_runtime_authority_stack` | runtime authority/multi-contour/session/revocation stack | `ab95633f1b90f9d032fd231d6cbef3e71b7fe106e0a7fb61d198c2254fc7d307` |

## 4. Claim Boundary

Allowed:

- public evidence classification architecture;
- redaction/hash/withhold boundary semantics;
- public release-bundle custody evidence;
- errata/supersession/retraction ledger discipline;
- citation-surface synchronization discipline;
- schema/checker-seed evidence, fixture evidence, and mutation evidence.

Forbidden:

- C-A1 ratification;
- legal or privacy-law certification;
- safety certification;
- deployment authorization;
- live substrate truth;
- proof of completeness.

## 5. Closed Layer Summary

```text
07   public evidence disclosure / redaction boundary
07a  disclosure manifest schema + checker seed
07b  public release bundle + hash custody audit
07c  public retraction / supersession / errata ledger
07d  public corpus index + citation surface sync
```

## 6. Release Integrity

See:

- `COMPONENT_REGISTRY.tsv`
- `SOURCE_BINDINGS.tsv`
- `EXECUTABLE_RERUN_SUMMARY.tsv`
- `UMBRELLA_VERIFICATION_LOG.md`
- `SHA256SUMS.txt`
