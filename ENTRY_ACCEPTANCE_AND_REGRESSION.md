# Entry Acceptance and Regression

## Purpose

This file fixes the minimum corpus-level acceptance standard for the canonical control layer. It gives maintainers, serious readers, and lightweight machine readers one short place to check whether a corpus-level edit preserved routing, semantic stability, citation clarity, and cross-repo coherence.
Use `ASSERTION_STRENGTH_AND_BOUNDARIES.md` when the remaining question is not acceptance but how strong a touched statement should be read.
Use `CROSS_LAYER_INVARIANTS_AND_CONTRADICTION_POLICY.md` when the remaining question is whether the touched text now weakens or reverses a load-bearing invariant.
Use `PACKAGE_INTAKE_AND_INTEGRATION.md` when a new package or control surface is still at intake stage and has not yet earned corpus-visible acceptance.
Use `LOCAL_TO_PUBLIC_PROMOTION_POLICY.md` when the remaining question is whether an accepted or locally validated state may be treated as commit-ready or public-facing.
Use `ATOMIC_PROMOTION_BUNDLES.md` when the remaining question is whether the accepted local change still belongs to a larger minimally coupled promotion bundle.
Use `PROMOTION_SEQUENCE_AND_RELEASE_TRANCHES.md` when the remaining question is whether the accepted local change still belongs to a later public-history tranche rather than an earlier supporting one.
Use `BOOTSTRAP_CUTOVER_AND_PUBLIC_HISTORY_CANDIDATE_SETS.md` when the remaining question is whether a future first public step is being overloaded with too many unrelated control layers.
Use `PUBLIC_CORRECTION_AND_ERRATA_POLICY.md` when the remaining question is whether a public-facing issue now needs explicit clarification, erratum, correction, retraction, or quarantine notice.

## 1. Why this file exists

Once the corpus has a canonical control layer, future edits should be checked against explicit acceptance criteria rather than intuition alone.

## 2. Acceptance rule

A corpus-level change is not accepted merely because files exist.
It must preserve discoverability, semantic stability, citation clarity, and cross-repo coherence.
Acceptance is necessary for promotion review, but it is not by itself public-history readiness.
Acceptance may still be locally true while atomic promotion scope remains incomplete.
Acceptance may also be locally true while public-history sequencing still points to an earlier tranche.
Acceptance may also be locally true while the candidate set for a first public cutover is still too large or conceptually noisy.

## 3. Canonical acceptance checks

| Check | What is being protected | Failure symptom | Minimal check |
|---|---|---|---|
| `A01` | first-screen role clarity | the touched repo starts sounding like the whole corpus, the runtime layer, or the normative core when it is not | read the first screen and confirm the repo role sentence still matches the corpus map |
| `A02` | first-screen boundary clarity | a serious reader can no longer tell what the repo is not | confirm explicit non-replacement / non-collapse wording still exists on the touched entry surface |
| `A03` | next-hop clarity | a surface states role but no longer shows where the reader should go next | confirm the next-hop pointer still resolves to the correct corpus route |
| `A04` | canonical surfaces discoverability from AGI control surfaces | a maintainer needs a second search step to find primer, stack lock, citation, claims, status, sync, supersession, terminology, acceptance, or intake | traverse AGI control surfaces and confirm those files remain visible |
| `A05` | narrative companion still distinguishable from normative core | the companion starts reading like protocol evidence or mature doctrine | confirm companion-facing surfaces still mark the book as companion and non-replacement |
| `A06` | citation / snapshot / frozen object wording remains coherent | a moving repo, frozen snapshot, DOI object, or manifest rule starts sounding interchangeable | compare citation, stack-lock, and download wording for the same public object |
| `A07` | claims/evidence crosswalk remains path-valid | the claims map points to stale, missing, or wrongly promoted artifacts | verify the canonical and supporting artifact paths still exist |
| `A08` | status/maturity labels remain bounded and coherent | draft, reserved, companion, or control-surface language gets silently inflated or blurred | compare touched surfaces against the bounded status / maturity vocabulary |
| `A09` | supersession/deprecation wording remains non-ambiguous | retained or still-citable surfaces start sounding current-primary by accident | confirm preference state wording still distinguishes primary, retained, superseded, historical-only, companion, and control-surface |
| `A10` | terminology / alias discipline remains intact | a new alias quietly replaces a canonical term for `AGI`, `c`, `L4`, the companion, or the runtime layer | scan touched surfaces against `TERMINOLOGY_AND_ALIAS_POLICY.md` |
| `A11` | machine-facing path hygiene remains clean | drive paths or brittle backslash traversal enter machine-facing surfaces | grep touched files for drive-letter paths and backslash-style relative traversal |
| `A12` | manifests follow existing repo-patterns only | a required manifest stays stale or a new unnecessary manifest ritual appears | update only manifests already expected by that repo and avoid binary overreach |

## 4. Regression patterns to watch

| Pattern | What goes wrong | Why it matters |
|---|---|---|
| `R01` | pointer-maze returns and the reader needs multiple hops to find the canonical control layer | serious readers and machine readers lose reliable first-pass orientation |
| `R02` | canonical and supporting artifacts blur together | citation, claims, and review weight become ambiguous |
| `R03` | a draft starts sounding like mature core | non-final material inherits authority it has not earned |
| `R04` | the narrative companion starts reading like normative proof | companion evidence and protocol evidence collapse into each other |
| `R05` | a repo-local edit silently becomes corpus-level drift | cross-repo surfaces fall out of sync without explicit review |
| `R06` | alias drift replaces a canonical term | vocabulary drift starts rewriting semantics before claims visibly change |
| `R07` | stale refs or moved paths survive in control surfaces | routing and claim verification become brittle or false |
| `R08` | integrity or citation wording drifts away from stack-lock reality | frozen-reading, download, and verification guidance stop referring to the same thing |

## 5. Minimal post-change review order

- `CORPUS_PRIMER.json`
- `STACK_LOCK_2026-04-12.json`
- `CITATION_AND_VERIFICATION.md`
- `CLAIMS_AND_EVIDENCE_MAP.md`
- `STATUS_AND_MATURITY_MAP.md`
- `CHANGE_CONTROL_AND_SYNC.md`
- `LOCAL_TO_PUBLIC_PROMOTION_POLICY.md`
- `ATOMIC_PROMOTION_BUNDLES.md`
- `PROMOTION_SEQUENCE_AND_RELEASE_TRANCHES.md`
- `BOOTSTRAP_CUTOVER_AND_PUBLIC_HISTORY_CANDIDATE_SETS.md`
- `PUBLIC_CORRECTION_AND_ERRATA_POLICY.md`
- `PACKAGE_INTAKE_AND_INTEGRATION.md`
- `SUPERSESSION_AND_DEPRECATION.md`
- `TERMINOLOGY_AND_ALIAS_POLICY.md`
- `ENTRY_ACCEPTANCE_AND_REGRESSION.md`
- relevant repo entry surface

## 6. Fail-closed rule

If maintainers cannot establish that the acceptance checks still hold, the change should remain unresolved until the affected surfaces are re-reviewed.

## 7. Read next

- `CONTROL_LAYER_MINIMALITY_AND_DEDUPLICATION_POLICY.md`
- `CONTROL_SURFACE_DEPENDENCY_AND_COUPLING_MAP.md`
- `CHANGE_CONTROL_AND_SYNC.md`
- `LOCAL_TO_PUBLIC_PROMOTION_POLICY.md`
- `ATOMIC_PROMOTION_BUNDLES.md`
- `PROMOTION_SEQUENCE_AND_RELEASE_TRANCHES.md`
- `BOOTSTRAP_CUTOVER_AND_PUBLIC_HISTORY_CANDIDATE_SETS.md`
- `PUBLIC_CORRECTION_AND_ERRATA_POLICY.md`
- `SUPERSESSION_AND_DEPRECATION.md`
- `TERMINOLOGY_AND_ALIAS_POLICY.md`
- `CLAIMS_AND_EVIDENCE_MAP.md`
- `CITATION_AND_VERIFICATION.md`
- `ASSERTION_STRENGTH_AND_BOUNDARIES.md`
- `CROSS_LAYER_INVARIANTS_AND_CONTRADICTION_POLICY.md`
- `PACKAGE_INTAKE_AND_INTEGRATION.md`
