# Current Local Control-Stack Staging Map

## Purpose

Provide one bounded current-state staging view of the locally present corpus
control stack so future clean promotion planning can point to concrete grouped
local surfaces instead of relying only on abstract promotion logic.

## 1. Why this file exists

The corpus now has enough local control surfaces that future promotion planning
should reference concrete locally present staging groups, not only abstract
tranche logic.

## 2. Core rule

A staging group is a practical bounded set of currently present local surfaces;
it is not yet a command to commit or publish. For concrete file-level local
planning, use `LOCAL_PROMOTION_DOCKET_AND_BLOCKER_REGISTRY.md`; staging groups
remain broader than docket entries.

## 3. Canonical staging table

| Stage ID | Staging group | Current local surfaces | Adjacent repo touches | Why grouped this way | Main blocker to cleaner promotion |
| --- | --- | --- | --- | --- | --- |
| `SG01` | foundational local entry / control group | `CORPUS_PRIMER.json`, `STACK_LOCK_2026-04-12.json`, `README.md`, `MACHINE_ENTRY.md`, `MASTER_ENTRY.md`, `REPO_INDEX.md`, `REPO_INDEX.json` | ERB/SER/clean/book `MACHINE_ENTRY.md`; AGI temporal manifest | this is the root local entry and control-routing baseline | cumulative dirty workspace still spans all participating repos |
| `SG02` | anti-confusion / citation / bounded-reading group | `CANONICAL_DISTINCTIONS.md`, `OBJECTIONS_AND_REPLIES.md`, `CITATION_AND_VERIFICATION.md`, `AUDIENCE_PROFILES_AND_MINIMAL_READING_PATHS.md` | book `CORPUS_CONTEXT.md`; AGI temporal manifest | these surfaces bound interpretation before stronger doctrinal reading | still local and not yet cleaned into future public sequence |
| `SG03` | claims / status / assertion / open-questions group | `CLAIMS_AND_EVIDENCE_MAP.md`, `STATUS_AND_MATURITY_MAP.md`, `ASSERTION_STRENGTH_AND_BOUNDARIES.md`, `OPEN_QUESTIONS_AND_EXPLICIT_NON_CLAIMS.md` | book `CORPUS_CONTEXT.md`; AGI temporal manifest | claims need maturity, assertion force, and non-closure guardrails together | commit-ready grouping is not yet globally established |
| `SG04` | ownership / precedence / invariants / coupling group | `CANONICAL_OWNERSHIP_AND_BOUNDARIES.md`, `PRECEDENCE_AND_RESOLUTION.md`, `CROSS_LAYER_INVARIANTS_AND_CONTRADICTION_POLICY.md`, `CONTROL_SURFACE_DEPENDENCY_AND_COUPLING_MAP.md` | ERB/SER/clean/book `MACHINE_ENTRY.md`; AGI temporal manifest | governing-source, repo-boundary, contradiction, and co-review rules reinforce each other | stronger review still needed before any clean outward sequencing |
| `SG05` | artifact identity / intake / minimality group | `ARTIFACT_ID_AND_REFERENCE_POLICY.md`, `SUPERSESSION_AND_DEPRECATION.md`, `PACKAGE_INTAKE_AND_INTEGRATION.md`, `CONTROL_LAYER_MINIMALITY_AND_DEDUPLICATION_POLICY.md` | AGI temporal manifest; book `MACHINE_ENTRY.md` where pointer-only routing matters | reference continuity, intake discipline, and anti-duplication belong in one bounded planning set | current local stack remains large and still needs cleaner de-dup aware staging |
| `SG06` | public-safe / audience / export group | `PUBLIC_SAFE_BOUNDARY_AND_EXCLUSION_POLICY.md`, `AUDIENCE_PROFILES_AND_MINIMAL_READING_PATHS.md`, `EXPORT_PROFILES_AND_HANDOFF_BUNDLES.md` | book `MACHINE_ENTRY.md`, `CORPUS_CONTEXT.md`; repo manifests where outward routing is surfaced | outward-facing reading and handoff need public-safe boundary guardrails | future public sharing still depends on cleaner support from earlier control groups |
| `SG07` | promotion / atomic / tranche / cutover / annotation / correction group | `CURRENT_CORPUS_STATE_AND_READINESS_SNAPSHOT.md`, `LOCAL_TO_PUBLIC_PROMOTION_POLICY.md`, `ATOMIC_PROMOTION_BUNDLES.md`, `PROMOTION_SEQUENCE_AND_RELEASE_TRANCHES.md`, `BOOTSTRAP_CUTOVER_AND_PUBLIC_HISTORY_CANDIDATE_SETS.md`, `PUBLIC_HISTORY_ANNOTATION_AND_RELEASE_NOTE_POLICY.md`, `PUBLIC_CORRECTION_AND_ERRATA_POLICY.md` | ERB/SER/clean/book `MACHINE_ENTRY.md`; participating temporal manifests | practical future promotion planning needs current-state, bundling, sequencing, and later-note discipline together | this remains planning logic only, with cumulative local dirt still blocking cleaner promotion |
| `SG08` | cross-repo pointer + manifest support group | `CHANGE_CONTROL_AND_SYNC.md`, `ENTRY_ACCEPTANCE_AND_REGRESSION.md`, AGI `hashes/SHA256SUMS_main_temporal_presence_2026-04-12.txt` | ERB/SER/clean `hashes/SHA256SUMS_main_temporal_presence_2026-04-12.txt`; book `hashes/SHA256SUMS.metadata-only.txt`, `hashes/SHA256SUMS.repo-all.txt`; book `CORPUS_CONTEXT.md` | sync, acceptance, routing, and integrity support the staged local stack without becoming the whole theory | manifest refresh alone still cannot make the grouped local stack promotion-clean |

## 4. Staging anti-patterns

| Anti-pattern ID | What goes wrong | Why it harms future clean promotion |
| --- | --- | --- |
| `ST01` | the whole local stack is treated as one stage | later promotion cannot stay bounded or reviewable |
| `ST02` | theory-facing layers are staged without their routing companions | future readers get policy without enough entry support |
| `ST03` | claims and status move without assertion or open-question guardrails | staged meaning starts reading stronger than intended |
| `ST04` | promotion-control layers move before enough earlier control framing exists | later public steps look procedurally advanced but conceptually under-supported |
| `ST05` | cross-repo pointer refresh moves without corresponding AGI control update | routing starts pointing at an incoherent control picture |
| `ST06` | manifest refresh is staged without coherent surface grouping | integrity traces can make a bad grouping look more settled than it is |
| `ST07` | companion pointers are staged as if they were independent doctrinal layers | support surfaces begin to look like parallel canon |
| `ST08` | staging is driven by file-count convenience instead of semantic grouping | clean future promotion loses bounded meaning and review discipline |

## 5. Fail-closed staging rule

If maintainers cannot explain in one short line why a local file belongs to a
given staging group, it should remain outside that group until clarified.

## 6. Read next

- `LOCAL_PROMOTION_DOCKET_AND_BLOCKER_REGISTRY.md`
- `CURRENT_CORPUS_STATE_AND_READINESS_SNAPSHOT.md`
- `LOCAL_TO_PUBLIC_PROMOTION_POLICY.md`
- `ATOMIC_PROMOTION_BUNDLES.md`
- `PROMOTION_SEQUENCE_AND_RELEASE_TRANCHES.md`
- `BOOTSTRAP_CUTOVER_AND_PUBLIC_HISTORY_CANDIDATE_SETS.md`
- `CONTROL_SURFACE_DEPENDENCY_AND_COUPLING_MAP.md`
