# Local Promotion Docket and Blocker Registry

## Purpose

Provide one compact corpus-level docket for already-present local canonical
surfaces: what family of files is in play now, which staging group it belongs
to, what its current local posture is, and what short blocker still prevents
cleaner future public-history movement.

## 1. Why this file exists

Current staging groups are useful, but maintainers also need a more concrete
local docket showing which already-present canonical surfaces sit where and
what still blocks cleaner promotion.

## 2. Core rule

A docket entry is a practical local planning record, not a staging group, not a
publish command, not a promotion state, and not proof of readiness by itself.

## 3. Canonical docket table

| Docket ID | File / Surface | Repo | Staging group | Current local posture | Main blocker | Promotion note |
| --- | --- | --- | --- | --- | --- | --- |
| `DG01` | `CORPUS_PRIMER.json`, `STACK_LOCK_2026-04-12.json`, `README.md`, `MACHINE_ENTRY.md`, `MASTER_ENTRY.md`, `REPO_INDEX.md`, `REPO_INDEX.json` | AGI | `SG01` | `locally-routed` | cumulative dirty workspace still spans the control baseline | foundational routing is usable locally, but still not a clean public-history boundary |
| `DG02` | `CANONICAL_DISTINCTIONS.md`, `OBJECTIONS_AND_REPLIES.md`, `CITATION_AND_VERIFICATION.md`, `CLAIMS_AND_EVIDENCE_MAP.md`, `STATUS_AND_MATURITY_MAP.md`, `ASSERTION_STRENGTH_AND_BOUNDARIES.md`, `OPEN_QUESTIONS_AND_EXPLICIT_NON_CLAIMS.md` | AGI | `SG02 + SG03` | `locally-validated` | no clean public-history commit boundary yet | interpretive and claim surfaces are assembled, but local validation is not yet public movement |
| `DG03` | `CANONICAL_OWNERSHIP_AND_BOUNDARIES.md`, `PRECEDENCE_AND_RESOLUTION.md`, `CROSS_LAYER_INVARIANTS_AND_CONTRADICTION_POLICY.md`, `CONTROL_LAYER_MINIMALITY_AND_DEDUPLICATION_POLICY.md`, `CONTROL_SURFACE_DEPENDENCY_AND_COUPLING_MAP.md`, `ARTIFACT_ID_AND_REFERENCE_POLICY.md`, `SUPERSESSION_AND_DEPRECATION.md`, `PACKAGE_INTAKE_AND_INTEGRATION.md` | AGI | `SG04 + SG05` | `local-present` | foundational routing is still ahead of stronger outward sequencing | these governance surfaces are operational locally, but cleaner promotion still depends on earlier control framing becoming cleaner first |
| `DG04` | `PUBLIC_SAFE_BOUNDARY_AND_EXCLUSION_POLICY.md`, `AUDIENCE_PROFILES_AND_MINIMAL_READING_PATHS.md`, `EXPORT_PROFILES_AND_HANDOFF_BUNDLES.md` | AGI | `SG06` | `locally-routed` | outward-safe routing remains local-only | these files already bound audience and handoff locally, but still depend on cleaner earlier public control framing |
| `DG05` | `CURRENT_CORPUS_STATE_AND_READINESS_SNAPSHOT.md`, `CURRENT_LOCAL_CONTROL_STACK_STAGING_MAP.md`, `LOCAL_PROMOTION_DOCKET_AND_BLOCKER_REGISTRY.md`, `LOCAL_TO_PUBLIC_PROMOTION_POLICY.md`, `ATOMIC_PROMOTION_BUNDLES.md`, `PROMOTION_SEQUENCE_AND_RELEASE_TRANCHES.md`, `BOOTSTRAP_CUTOVER_AND_PUBLIC_HISTORY_CANDIDATE_SETS.md`, `PUBLIC_HISTORY_ANNOTATION_AND_RELEASE_NOTE_POLICY.md`, `PUBLIC_CORRECTION_AND_ERRATA_POLICY.md` | AGI | `SG07` | `local-only` | promotion sequencing is still doctrine, not exercised clean public history | this is the planning stack for later movement, not evidence that such movement already happened |
| `DG06` | ERB / SER / clean / book `MACHINE_ENTRY.md`; book `CORPUS_CONTEXT.md` | ERB / SER / clean / book | `SG08` | `adjacent-support-only` | adjacent repo pointers still remain local-only | cross-repo routing support is intentional, but these surfaces remain companion planning support rather than primary AGI doctrine |
| `DG07` | AGI `hashes/SHA256SUMS_main_temporal_presence_2026-04-12.txt`; ERB / SER / clean `hashes/SHA256SUMS_main_temporal_presence_2026-04-12.txt`; book `hashes/SHA256SUMS.metadata-only.txt`, `hashes/SHA256SUMS.repo-all.txt` | all five repos | `SG08` | `adjacent-support-only` | manifest refresh remains local-only | manifests support verification of the local stack, but do not themselves create public-history settlement |

## 4. Blocker classes

| Blocker ID | What it means | Why it blocks cleaner promotion |
| --- | --- | --- |
| `BK01` | cumulative dirty workspace | a wider dirty local stack makes it harder to isolate one clean future public step |
| `BK02` | missing clean public-history commit boundary | local presence alone does not show a bounded outward history step |
| `BK03` | not yet promoted foundational routing | later control surfaces read worse if stable public entry routing is still absent |
| `BK04` | adjacent repo pointers still local-only | companion repo routing remains support context until cleaner outward alignment exists |
| `BK05` | manifest refresh still local-only | integrity traces can confirm local state, but not public-history settlement |
| `BK06` | public-history annotation not yet exercised in practice | later outward notes remain doctrinal until an actual bounded public step exists |
| `BK07` | promotion sequencing still only local doctrine | tranche and cutover logic remain planning discipline rather than public execution |
| `BK08` | wider public consolidation still intentionally deferred | the corpus is still keeping larger outward cleanup and consolidation out of scope |

## 5. Fail-closed docket rule

If maintainers cannot place a local file or surface into a bounded docket entry
with one short blocker note, it should remain outside the docket until its role
is clarified.

## 6. Read next

- `CURRENT_LOCAL_CONTROL_STACK_STAGING_MAP.md`
- `CURRENT_CORPUS_STATE_AND_READINESS_SNAPSHOT.md`
- `LOCAL_TO_PUBLIC_PROMOTION_POLICY.md`
- `ATOMIC_PROMOTION_BUNDLES.md`
- `PROMOTION_SEQUENCE_AND_RELEASE_TRANCHES.md`
- `BOOTSTRAP_CUTOVER_AND_PUBLIC_HISTORY_CANDIDATE_SETS.md`
