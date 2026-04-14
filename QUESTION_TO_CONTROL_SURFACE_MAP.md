# Question to Control-Surface Map

## Purpose

Provide one compact corpus-level triage map so maintainers, reviewers, Codex,
and serious readers can route a question to the right primary control surface,
then read only the shortest adjacent surfaces needed for bounded clarity.

## 1. Why this file exists

A mature corpus should not require maintainers and reviewers to rediscover the
same surface-routing logic every time a new question appears.

## 2. Core rule

Start with the primary control surface for the question family, then read only
the minimum adjacent surfaces required for bounded clarity.

## 3. Canonical question map

| Question ID | Question family | Primary control surface | Typical secondary surfaces | Enough for | Not enough for |
| --- | --- | --- | --- | --- | --- |
| `Q01` | What is this corpus, at the highest level? | `CORPUS_PRIMER.json` | `MASTER_ENTRY.md`; `README.md`; `CANONICAL_DISTINCTIONS.md` | first bounded orientation to corpus role, repo set, and core formula | claim force, maturity, or promotion status |
| `Q02` | What does the corpus actually claim? | `CLAIMS_AND_EVIDENCE_MAP.md` | `STATUS_AND_MATURITY_MAP.md`; `ASSERTION_STRENGTH_AND_BOUNDARIES.md`; `CITATION_AND_VERIFICATION.md` | canonical claim carrier and preferred artifact path | whole-domain closure or mature status by itself |
| `Q03` | What does the corpus explicitly not claim or leave open? | `OPEN_QUESTIONS_AND_EXPLICIT_NON_CLAIMS.md` | `STATUS_AND_MATURITY_MAP.md`; `ASSERTION_STRENGTH_AND_BOUNDARIES.md` | bounded non-closure and explicit non-claim reading | the full positive claim set |
| `Q04` | What is stable, what is draft, and what is companion-only? | `STATUS_AND_MATURITY_MAP.md` | `ASSERTION_STRENGTH_AND_BOUNDARIES.md`; `CANONICAL_OWNERSHIP_AND_BOUNDARIES.md` | maturity, weight, and bounded artifact class | citation path or public-promotion readiness |
| `Q05` | How should I cite and verify a specific artifact? | `CITATION_AND_VERIFICATION.md` | `CLAIMS_AND_EVIDENCE_MAP.md`; `ARTIFACT_ID_AND_REFERENCE_POLICY.md`; `STACK_LOCK_2026-04-12.json` | correct public object choice and verification route | whether the artifact settles the wider question by itself |
| `Q06` | Which repo canonically owns which layer/package? | `CANONICAL_OWNERSHIP_AND_BOUNDARIES.md` | `PRECEDENCE_AND_RESOLUTION.md`; `PACKAGE_INTAKE_AND_INTEGRATION.md` | canonical home and allowed non-owner role | claim maturity or evidence weight |
| `Q07` | What should be treated as public-safe, pointer-only, or excluded? | `PUBLIC_SAFE_BOUNDARY_AND_EXCLUSION_POLICY.md` | `PACKAGE_INTAKE_AND_INTEGRATION.md`; `LOCAL_TO_PUBLIC_PROMOTION_POLICY.md` | boundary class and allowed public treatment | commit-readiness or tranche order |
| `Q08` | What depends on what, and what requires co-review? | `CONTROL_SURFACE_DEPENDENCY_AND_COUPLING_MAP.md` | `CHANGE_CONTROL_AND_SYNC.md`; `ATOMIC_PROMOTION_BUNDLES.md` | co-review and bounded dependency routing | auto-edit authority or canonical ownership by itself |
| `Q09` | How should a new package enter the corpus? | `PACKAGE_INTAKE_AND_INTEGRATION.md` | `CANONICAL_OWNERSHIP_AND_BOUNDARIES.md`; `STATUS_AND_MATURITY_MAP.md`; `PUBLIC_SAFE_BOUNDARY_AND_EXCLUSION_POLICY.md` | intake gate, classification, and minimum required checks | release-note wording or promotion execution |
| `Q10` | What is the current local state of the control stack? | `CURRENT_CORPUS_STATE_AND_READINESS_SNAPSHOT.md` | `CURRENT_LOCAL_CONTROL_STACK_STAGING_MAP.md`; `LOCAL_PROMOTION_DOCKET_AND_BLOCKER_REGISTRY.md` | bounded local current-state picture and main blockers | clean public-history readiness by itself |
| `Q11` | What blocks cleaner public promotion? | `LOCAL_PROMOTION_DOCKET_AND_BLOCKER_REGISTRY.md` | `CURRENT_CORPUS_STATE_AND_READINESS_SNAPSHOT.md`; `LOCAL_TO_PUBLIC_PROMOTION_POLICY.md` | concrete local blocker families and where they currently sit | what should move together or in what sequence |
| `Q12` | What should move together in future public-history promotion? | `ATOMIC_PROMOTION_BUNDLES.md` | `LOCAL_TO_PUBLIC_PROMOTION_POLICY.md`; `CONTROL_SURFACE_DEPENDENCY_AND_COUPLING_MAP.md` | minimally coupled promotion bundle logic | tranche order or actual public authorization |
| `Q13` | In what order should bounded public-history promotion happen? | `PROMOTION_SEQUENCE_AND_RELEASE_TRANCHES.md` | `BOOTSTRAP_CUTOVER_AND_PUBLIC_HISTORY_CANDIDATE_SETS.md`; `LOCAL_TO_PUBLIC_PROMOTION_POLICY.md` | bounded outward sequence and earlier-vs-later logic | a publish command or exercised public history |
| `Q14` | How should future public-history notes be written? | `PUBLIC_HISTORY_ANNOTATION_AND_RELEASE_NOTE_POLICY.md` | `LOCAL_TO_PUBLIC_PROMOTION_POLICY.md`; `BOOTSTRAP_CUTOVER_AND_PUBLIC_HISTORY_CANDIDATE_SETS.md` | bounded note fields and note type selection | whether the step itself is justified |
| `Q15` | How should public corrections / errata be handled? | `PUBLIC_CORRECTION_AND_ERRATA_POLICY.md` | `PUBLIC_HISTORY_ANNOTATION_AND_RELEASE_NOTE_POLICY.md`; `SUPERSESSION_AND_DEPRECATION.md` | typed correction class and bounded correction scope | first-time promotion or initial release routing |
| `Q16` | When should a new control layer NOT be created? | `CONTROL_LAYER_MINIMALITY_AND_DEDUPLICATION_POLICY.md` | `CONTROL_STACK_COMPLETENESS_AND_STOP_RULE.md`; `CONTROL_SURFACE_DEPENDENCY_AND_COUPLING_MAP.md`; `PACKAGE_INTAKE_AND_INTEGRATION.md` | whether an existing layer should absorb the function instead, or whether the current stack is already sufficient enough to stop adding layers | canonical owner or question-routing sufficiency once a layer already exists |

## 4. Anti-overread notes

- question routing is not doctrinal replacement
- a primary surface may answer the first question without settling the whole domain
- one surface rarely covers claims + status + public-safe + promotion at once
- when in doubt, prefer bounded reading over synthetic certainty

## 5. Fail-closed triage rule

If maintainers cannot map a question to one primary control surface and a short
secondary list, they should prefer the more foundational surface first rather
than inventing a new route.

## 6. Read next

- `CORPUS_PRIMER.json`
- `CLAIMS_AND_EVIDENCE_MAP.md`
- `STATUS_AND_MATURITY_MAP.md`
- `OPEN_QUESTIONS_AND_EXPLICIT_NON_CLAIMS.md`
- `CONTROL_SURFACE_DEPENDENCY_AND_COUPLING_MAP.md`
- `CONTROL_STACK_COMPLETENESS_AND_STOP_RULE.md`
- `CURRENT_LOCAL_CONTROL_STACK_STAGING_MAP.md`
