# Current Corpus State and Readiness Snapshot

## Purpose

Provide one bounded current-state snapshot for the assembled corpus control layer:
what exists now, what is locally assembled, what remains local, what is enough for
serious bounded reading, and what still blocks a cleaner public-history cutover.

## 1. Why this file exists

The corpus already has claim, status, ownership, promotion, correction, and export
surfaces. This file does not replace them. It provides one compact current-state
snapshot so a reader does not have to infer present condition from many separate
policy files.

## 2. Snapshot date and scope

- Snapshot date: `2026-04-12`
- Scope: local accepted corpus workspace only
- This file is not a release note
- This file is not proof that public-history promotion already exists
- This file is not a substitute for `STATUS_AND_MATURITY_MAP.md`
- This file is not a substitute for `LOCAL_TO_PUBLIC_PROMOTION_POLICY.md`
- This file is not a docket / blocker registry
- This file is not a question-to-surface triage map
- This file is not a completeness / stop-rule surface
- This file is a consumer of other control layers, not their owner
- This file is not a staging map or publish command

## 3. Canonical snapshot table

| Snapshot ID | Layer / Surface family | Current local condition | Public-history condition | Why it matters | Main blocker / note |
| --- | --- | --- | --- | --- | --- |
| `SNP01` | foundational entry / control surfaces | present locally; routing in place | public-history not yet established | readers can enter the corpus without reconstructing the stack ad hoc | cumulative dirty workspace remains |
| `SNP02` | anti-confusion / citation surfaces | present locally; locally validated | public-history not yet established | naming, citation, and verification remain bounded instead of drifting by inference | bounded but still local |
| `SNP03` | claims / status / assertion surfaces | present locally; routing in place | public-history not yet established | readers can tell what is claimed, how mature it is, and how strongly to read it | commit-ready not yet established globally |
| `SNP04` | ownership / precedence / invariant surfaces | present locally; locally validated | public-history not yet established | cross-layer overread is constrained before stronger surfaces are contradicted | cumulative dirty workspace remains |
| `SNP05` | artifact identity / intake surfaces | present locally; bounded but still local | public-history not yet established | references stay stable and new package mentions remain bounded | cleaner public sequencing still pending |
| `SNP06` | public-safe / audience / export surfaces | present locally; routing in place | public-history not yet established | serious bounded reading and handoff are possible without pretending to export the whole corpus | external bundle logic stays local until cleaner cutover |
| `SNP07` | promotion / atomic / tranche / cutover surfaces | present locally; locally validated | public-history not yet established | promotion planning is explicit instead of being confused with execution | promotion planning is not release authorization |
| `SNP08` | correction / errata / open-question surfaces | present locally; routing in place | public-history not yet established | unresolved territory and later fixes remain typed and non-theatrical | local non-closure remains real rather than hidden |
| `SNP09` | cross-repo pointer hygiene condition | routing in place | public-history not yet established | entry surfaces point across the stack without Windows-style traversal confusion | cumulative dirty workspace remains |
| `SNP10` | manifest / integrity refresh condition | integrity refreshed per repo-pattern | public-history not yet established | verification stays possible while local control layers continue to accumulate | manifest presence is not public-history completion |

## 4. Minimal readiness notes

- The corpus is no longer conceptually raw.
- The control layer is substantial and internally routed.
- The current local state is enough for bounded serious reading of the corpus control logic.
- Public-history promotion remains a later and distinct step.
- The main cleaner public sequencing blocker is cumulative dirty local state across the participating repos.
- Local completeness of control logic does not equal public-history completion.

## 5. Fail-closed snapshot rule

If maintainers cannot determine whether a surface is only present locally,
locally validated, or already supported by clean public-history treatment,
default to the weaker local reading until clarified.

## 6. Read next

- `CURRENT_LOCAL_CONTROL_STACK_STAGING_MAP.md`
- `LOCAL_PROMOTION_DOCKET_AND_BLOCKER_REGISTRY.md`
- `QUESTION_TO_CONTROL_SURFACE_MAP.md`
- `CONTROL_STACK_COMPLETENESS_AND_STOP_RULE.md`
- `CONTROL_SURFACE_DEPENDENCY_AND_COUPLING_MAP.md`
- `STATUS_AND_MATURITY_MAP.md`
- `LOCAL_TO_PUBLIC_PROMOTION_POLICY.md`
- `BOOTSTRAP_CUTOVER_AND_PUBLIC_HISTORY_CANDIDATE_SETS.md`
- `PUBLIC_HISTORY_ANNOTATION_AND_RELEASE_NOTE_POLICY.md`
- `PUBLIC_CORRECTION_AND_ERRATA_POLICY.md`
