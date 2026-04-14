# Control Surface Dependency and Coupling Map

## Purpose

Provide one compact canonical map for how the existing corpus control surfaces
depend on each other, when co-review is usually required, and when adjacent
surfaces should remain untouched unless a real dependency is triggered.
Use `QUESTION_TO_CONTROL_SURFACE_MAP.md` when the remaining question is not
dependency or co-review, but which control surface should answer a question
first. Use `CONTROL_STACK_COMPLETENESS_AND_STOP_RULE.md` when the remaining
question is whether the present stack already has enough bounded control
coverage.

## 1. Why this file exists

Once a corpus has many control layers, maintainers need to know not only what
exists, but what is logically coupled to what.

## 2. Core rule

A change to one control surface does not imply touching all others, but some
surfaces have bounded dependency and should be reviewed together. Coupling is
not ownership, co-review is not auto-edit, and atomic promotion remains a
separate question from ordinary dependency review.

## 3. Canonical coupling table

| Coupling ID | Surface | Primary dependency | Typical secondary dependencies | Coupling strength | What usually triggers co-review | What should NOT be auto-touched |
| --- | --- | --- | --- | --- | --- | --- |
| `CD01` | `CORPUS_PRIMER.json` | canonical entry routing | `STACK_LOCK_2026-04-12.json`, `MASTER_ENTRY.md`, `REPO_INDEX.json` | `moderate` | repo set, canonical route, or layer-order wording changes | deeper policy surfaces should not move for primer-only polish |
| `CD02` | `STACK_LOCK_2026-04-12.json` | corpus primer and canonical repo set | `REPO_INDEX.json`, `CURRENT_CORPUS_STATE_AND_READINESS_SNAPSHOT.md` | `strong` | lock date, repo composition, or canonical raw target changes | claims and status layers should not be rewritten for a pure lock refresh |
| `CD03` | `CANONICAL_DISTINCTIONS.md` / `OBJECTIONS_AND_REPLIES.md` | terminology boundary and anti-confusion framing | `CITATION_AND_VERIFICATION.md`, `OPEN_QUESTIONS_AND_EXPLICIT_NON_CLAIMS.md` | `moderate` | anti-confusion scope or settled objection boundary changes | promotion or ownership layers should not move for rhetorical cleanup alone |
| `CD04` | `CITATION_AND_VERIFICATION.md` | `ARTIFACT_ID_AND_REFERENCE_POLICY.md` | `CLAIMS_AND_EVIDENCE_MAP.md`, `PUBLIC_HISTORY_ANNOTATION_AND_RELEASE_NOTE_POLICY.md`, `PUBLIC_CORRECTION_AND_ERRATA_POLICY.md` | `strong` | stable reference rule, citation path, or verification expectation changes | audience or export surfaces should not be touched unless citation behavior really changes |
| `CD05` | `CLAIMS_AND_EVIDENCE_MAP.md` | `CITATION_AND_VERIFICATION.md` | `STATUS_AND_MATURITY_MAP.md`, `ASSERTION_STRENGTH_AND_BOUNDARIES.md`, `PUBLIC_CORRECTION_AND_ERRATA_POLICY.md` | `strong` | claim meaning, evidence anchor, or claim-to-artifact mapping changes | ownership and tranche layers should not auto-move for claim phrasing alone |
| `CD06` | `STATUS_AND_MATURITY_MAP.md` / `ASSERTION_STRENGTH_AND_BOUNDARIES.md` | `CLAIMS_AND_EVIDENCE_MAP.md` | `OPEN_QUESTIONS_AND_EXPLICIT_NON_CLAIMS.md`, `CURRENT_CORPUS_STATE_AND_READINESS_SNAPSHOT.md`, `ENTRY_ACCEPTANCE_AND_REGRESSION.md` | `strong` | maturity class, assertion force, or confidence boundary changes | artifact ID and export surfaces should not be auto-touched without a real downstream consequence |
| `CD07` | `CHANGE_CONTROL_AND_SYNC.md` / `ENTRY_ACCEPTANCE_AND_REGRESSION.md` | corpus-control review discipline | `ATOMIC_PROMOTION_BUNDLES.md`, `CURRENT_CORPUS_STATE_AND_READINESS_SNAPSHOT.md`, this file | `strong` | sync trigger, acceptance gate, or review-order rule changes | claims text should not be rewritten because review discipline moved |
| `CD08` | `SUPERSESSION_AND_DEPRECATION.md` / `ARTIFACT_ID_AND_REFERENCE_POLICY.md` | continuity of reference state | `PRECEDENCE_AND_RESOLUTION.md`, `PUBLIC_CORRECTION_AND_ERRATA_POLICY.md`, `PUBLIC_HISTORY_ANNOTATION_AND_RELEASE_NOTE_POLICY.md` | `strong` | rename, move, deprecation, retained-reference, or supersession state changes | primer and narrative routing should not be touched unless the target reference really changed |
| `CD09` | `CANONICAL_OWNERSHIP_AND_BOUNDARIES.md` / `PRECEDENCE_AND_RESOLUTION.md` / `CROSS_LAYER_INVARIANTS_AND_CONTRADICTION_POLICY.md` | canonical home and governing-source hierarchy | `CHANGE_CONTROL_AND_SYNC.md`, `PACKAGE_INTAKE_AND_INTEGRATION.md`, `PUBLIC_SAFE_BOUNDARY_AND_EXCLUSION_POLICY.md` | `strong` | owner repo, override rule, or invariant statement changes | weakly adjacent wording surfaces should not be rewritten by habit |
| `CD10` | `PACKAGE_INTAKE_AND_INTEGRATION.md` | `CANONICAL_OWNERSHIP_AND_BOUNDARIES.md` | `PUBLIC_SAFE_BOUNDARY_AND_EXCLUSION_POLICY.md`, `STATUS_AND_MATURITY_MAP.md`, `ARTIFACT_ID_AND_REFERENCE_POLICY.md` | `moderate` | new package mention, intake class, or provisional routing change | the full promotion stack should not be touched before the package becomes a real canonical surface |
| `CD11` | `PUBLIC_SAFE_BOUNDARY_AND_EXCLUSION_POLICY.md` / `AUDIENCE_PROFILES_AND_MINIMAL_READING_PATHS.md` / `EXPORT_PROFILES_AND_HANDOFF_BUNDLES.md` | public-safe boundary classes | `PACKAGE_INTAKE_AND_INTEGRATION.md`, `CURRENT_CORPUS_STATE_AND_READINESS_SNAPSHOT.md` | `strong` | boundary class, audience route, or export scope changes | doctrinal claim surfaces should not be rewritten for outward packaging alone |
| `CD12` | `LOCAL_TO_PUBLIC_PROMOTION_POLICY.md` / `ATOMIC_PROMOTION_BUNDLES.md` / `PROMOTION_SEQUENCE_AND_RELEASE_TRANCHES.md` / `BOOTSTRAP_CUTOVER_AND_PUBLIC_HISTORY_CANDIDATE_SETS.md` / `PUBLIC_HISTORY_ANNOTATION_AND_RELEASE_NOTE_POLICY.md` / `PUBLIC_CORRECTION_AND_ERRATA_POLICY.md` | `ENTRY_ACCEPTANCE_AND_REGRESSION.md` and `CHANGE_CONTROL_AND_SYNC.md` | `CURRENT_CORPUS_STATE_AND_READINESS_SNAPSHOT.md`, `PUBLIC_SAFE_BOUNDARY_AND_EXCLUSION_POLICY.md`, `ARTIFACT_ID_AND_REFERENCE_POLICY.md` | `strong` | promotion gate, bundle boundary, tranche order, cutover set, annotation rule, or correction class changes | non-promotion control layers should not be auto-edited unless public-history meaning actually shifts |
| `CD13` | `OPEN_QUESTIONS_AND_EXPLICIT_NON_CLAIMS.md` | `STATUS_AND_MATURITY_MAP.md` and `ASSERTION_STRENGTH_AND_BOUNDARIES.md` | `CLAIMS_AND_EVIDENCE_MAP.md`, `CURRENT_CORPUS_STATE_AND_READINESS_SNAPSHOT.md`, `PUBLIC_CORRECTION_AND_ERRATA_POLICY.md` | `moderate` | question closure, reserved territory wording, or explicit non-claim boundary changes | ownership and atomic-bundle surfaces should not be touched unless non-closure changes review consequence |
| `CD14` | `CURRENT_CORPUS_STATE_AND_READINESS_SNAPSHOT.md` | current corpus-control layer state | `STATUS_AND_MATURITY_MAP.md`, `LOCAL_TO_PUBLIC_PROMOTION_POLICY.md`, `PUBLIC_CORRECTION_AND_ERRATA_POLICY.md`, this file | `moderate` | blocker wording, local readiness statement, or current-state routing changes | upstream owner surfaces should not be rewritten from snapshot edits; the snapshot is a consumer, not an owner |

## 4. Co-review anti-patterns

| Anti-pattern ID | What goes wrong | Why it matters |
| --- | --- | --- |
| `DC01` | too many control layers are touched by habit instead of dependency | maintenance turns sprawling and makes real review harder |
| `DC02` | a strong dependency changes without reviewing its coupled surfaces | the corpus can become locally inconsistent while still looking orderly |
| `DC03` | weak coupling is treated as strong coupling | bounded surfaces get over-expanded and accumulate unnecessary churn |
| `DC04` | routing surfaces change without claims or citation awareness | readers can be redirected into stale meaning or stale evidence paths |
| `DC05` | artifact ID or reference state changes without supersession awareness | continuity and retained-reference state become ambiguous |
| `DC06` | promotion-layer edits happen without snapshot or readiness awareness | planning language can overrun actual current state and blockers |
| `DC07` | boundary or export edits happen without public-safe review | outward-facing scope can drift beyond what the corpus safely intends |
| `DC08` | open-question edits happen without assertion or status awareness | unresolved territory can start sounding settled or stronger than intended |

## 5. Fail-closed coupling rule

If maintainers cannot tell whether a control-layer change has strong or weak
coupling, default to co-review of the stronger likely dependent surfaces, but
do not auto-edit them unless review shows a real need.

## 6. Read next

- `CURRENT_LOCAL_CONTROL_STACK_STAGING_MAP.md`
- `QUESTION_TO_CONTROL_SURFACE_MAP.md`
- `CONTROL_STACK_COMPLETENESS_AND_STOP_RULE.md`
- `CONTROL_LAYER_MINIMALITY_AND_DEDUPLICATION_POLICY.md`
- `CHANGE_CONTROL_AND_SYNC.md`
- `ENTRY_ACCEPTANCE_AND_REGRESSION.md`
- `ATOMIC_PROMOTION_BUNDLES.md`
- `ARTIFACT_ID_AND_REFERENCE_POLICY.md`
- `CANONICAL_OWNERSHIP_AND_BOUNDARIES.md`
- `CURRENT_CORPUS_STATE_AND_READINESS_SNAPSHOT.md`
