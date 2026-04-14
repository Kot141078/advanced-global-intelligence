# Local to Public Promotion Policy

## Purpose

This file fixes a compact corpus-level vocabulary for promotion from local corpus work into public-facing history.
It distinguishes promotion state from status/maturity, supersession state, ownership, public-safe boundary class, and contradiction class.
Use `ATOMIC_PROMOTION_BUNDLES.md` when the remaining question is not promotion state but which minimally coupled surfaces must move together if public-history promotion is later attempted.
Use `PROMOTION_SEQUENCE_AND_RELEASE_TRANCHES.md` when the remaining question is not promotion state or bundle scope, but which supporting tranche should come earlier in future public history.
Use `BOOTSTRAP_CUTOVER_AND_PUBLIC_HISTORY_CANDIDATE_SETS.md` when the remaining question is which bounded candidate set could reasonably contain a future first public-history cutover step.
Use `PUBLIC_HISTORY_ANNOTATION_AND_RELEASE_NOTE_POLICY.md` when the remaining question is how a bounded future public step should be explained once promotion is actually visible.
Use `LOCAL_PROMOTION_DOCKET_AND_BLOCKER_REGISTRY.md` when the remaining question is which already-present local surfaces are concretely in play now, which staging group they sit in, and what short blocker still holds them locally.

## 1. Why this file exists

A mature corpus needs not only creation and validation rules,
but also explicit discipline for when local control-layer work may become public history.

## 2. Core rule

Local existence and local acceptance are not yet public promotion.
Promotion requires explicit bounded readiness, not just accumulated work.

## 3. Canonical promotion states

| State ID | Promotion state | Meaning | What is true at this state | What is NOT yet true | Allowed use |
|---|---|---|---|---|---|
| `PS01` | local working state | in-progress local corpus work | local edits or draft surfaces exist | acceptance, validation, commit-readiness, and public-facing status are not yet established | local drafting, iteration, and bounded private review inside the allowed workspace |
| `PS02` | local accepted state | a bounded local result accepted for continued local use | the current local pass accepts the layer as usable for further local work | promotion review is not complete and public history is not yet justified | local baseline for the next bounded pass in the same allowed workspace |
| `PS03` | locally validated state | a local state that cleared the required checks for the current pass | required refs, IDs, path hygiene, and manifest updates for the pass have been checked locally | commit-ready and public-facing promotion are still separate questions | candidate for promotion review, not yet public-history truth |
| `PS04` | commit-ready state | a local state that cleared bounded promotion review | blockers are resolved, affected control surfaces are aligned, and required repo-pattern manifests are updated | the state is not yet public-facing committed history or automatically external-reference-ready | candidate for explicit public git-history promotion after human review |
| `PS05` | public-facing committed state | a state already present in public-facing committed repo history | the relevant public repo history now contains the state and the visible control layer reflects it | snapshot/release/DOI/export-readiness is not automatically implied | public reading and public-history reference inside the live repo state |
| `PS06` | publishable / external-reference-ready state | a public-facing state safe for outward reference or bounded external handoff | outward enough-for / not-enough-for boundaries are clear and public-safe/citation/export wording is aligned | whole-corpus closure, universal readiness, or frozen-object status are not implied | external reference, bounded handoff, or publication routing where the current repo-pattern supports it |

## 4. Promotion blockers

| Blocker ID | Promotion blocker | What blocks promotion | Why it matters |
|---|---|---|---|
| `PB01` | unresolved corpus-control contradiction | touched surfaces still conflict with load-bearing control-layer rules or each other | public history should not capture unresolved control-layer drift as if it were settled |
| `PB02` | broken discoverability of canonical surfaces | a serious reader or machine can no longer find required canonical surfaces from AGI control entry points | public promotion without discoverability breaks routing and later review |
| `PB03` | stale refs / path drift in control layer | canonical paths, raw links, or file references are stale, broken, or inconsistent | outward-facing history should not preserve false routing or brittle pointers |
| `PB04` | status/assertion/ownership mismatch | promotion would preserve mismatched maturity, claim force, or canonical-home wording | public readers may import authority the corpus did not grant |
| `PB05` | public-safe boundary uncertainty | it is still unclear whether touched material is public-safe, pointer-only, or excluded | uncertain boundary class is a stop signal for public-facing promotion |
| `PB06` | unresolved package classification | the touched addition still lacks stable role, scope, or control-surface classification | unclassified local material should not harden into public canon by inertia |
| `PB07` | missing manifest / integrity update where required by repo-pattern | the current repo pattern expects manifest alignment and it is still stale or absent | public history should not claim integrity discipline it does not actually reflect |
| `PB08` | unclear enough-for / not-enough-for boundary in outward-facing bundle | outward-facing wording still overclaims what a promoted state or bundle is sufficient for | promotion without bounded outward claims invites later misreading and overreach |

## 5. Minimal promotion review

Before local corpus work is treated as commit-ready, review MUST consider:

- `ATOMIC_PROMOTION_BUNDLES.md` to identify the minimally coupled bundle before treating a state as `PS04`
- `PROMOTION_SEQUENCE_AND_RELEASE_TRANCHES.md` if the remaining question is whether a commit-ready local layer still belongs to a later tranche
- `BOOTSTRAP_CUTOVER_AND_PUBLIC_HISTORY_CANDIDATE_SETS.md` if the remaining question is whether the first public cutover set is being overpacked
- `PUBLIC_HISTORY_ANNOTATION_AND_RELEASE_NOTE_POLICY.md` if the remaining question is whether a future public-history note can stay truthful, dry, and scope-limited
- `ENTRY_ACCEPTANCE_AND_REGRESSION.md`
- `CANONICAL_OWNERSHIP_AND_BOUNDARIES.md`
- `PRECEDENCE_AND_RESOLUTION.md`
- `PUBLIC_SAFE_BOUNDARY_AND_EXCLUSION_POLICY.md`
- `ARTIFACT_ID_AND_REFERENCE_POLICY.md`
- `CITATION_AND_VERIFICATION.md`
- manifests only where the current repo-pattern requires them
- `EXPORT_PROFILES_AND_HANDOFF_BUNDLES.md` if outward-facing sharing is affected
- `OPEN_QUESTIONS_AND_EXPLICIT_NON_CLAIMS.md` if unresolved territory is affected

## 6. Fail-closed promotion rule

If maintainers cannot determine whether a local state is truly commit-ready,
it remains local accepted or locally validated only until clarified.

## 7. Read next

- `CURRENT_LOCAL_CONTROL_STACK_STAGING_MAP.md`
- `LOCAL_PROMOTION_DOCKET_AND_BLOCKER_REGISTRY.md`
- `CURRENT_CORPUS_STATE_AND_READINESS_SNAPSHOT.md`
- `ENTRY_ACCEPTANCE_AND_REGRESSION.md`
- `CHANGE_CONTROL_AND_SYNC.md`
- `ATOMIC_PROMOTION_BUNDLES.md`
- `PROMOTION_SEQUENCE_AND_RELEASE_TRANCHES.md`
- `BOOTSTRAP_CUTOVER_AND_PUBLIC_HISTORY_CANDIDATE_SETS.md`
- `PUBLIC_HISTORY_ANNOTATION_AND_RELEASE_NOTE_POLICY.md`
- `SUPERSESSION_AND_DEPRECATION.md`
- `PUBLIC_SAFE_BOUNDARY_AND_EXCLUSION_POLICY.md`
- `ARTIFACT_ID_AND_REFERENCE_POLICY.md`
- `EXPORT_PROFILES_AND_HANDOFF_BUNDLES.md`
- `PACKAGE_INTAKE_AND_INTEGRATION.md`
- `OPEN_QUESTIONS_AND_EXPLICIT_NON_CLAIMS.md`
