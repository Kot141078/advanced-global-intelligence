# Change Control and Sync

## Purpose

This file fixes the minimum corpus-level maintenance rules for the canonical layer that now spans multiple repos.
Use it when a future edit may change reading order, citation paths, claim routing, status/maturity classification, or cross-repo discoverability.
Use `SUPERSESSION_AND_DEPRECATION.md` alongside this file when the same change may also alter what is primary, retained, superseded, or historical-only.
Use `TERMINOLOGY_AND_ALIAS_POLICY.md` when a future edit introduces a new alias or wording shift for a load-bearing corpus term.
Use `ENTRY_ACCEPTANCE_AND_REGRESSION.md` when the question is whether the touched corpus layer still clears the minimum acceptance standard after the change.
Use `LOCAL_TO_PUBLIC_PROMOTION_POLICY.md` when the question is whether a local accepted or locally validated state may be treated as commit-ready or public-facing history.
Use `ATOMIC_PROMOTION_BUNDLES.md` when the question is which minimally coupled surfaces must move together if public-history promotion is later attempted.
Use `PROMOTION_SEQUENCE_AND_RELEASE_TRANCHES.md` when the question is whether a later tranche is being promoted ahead of an earlier supporting tranche.
Use `ASSERTION_STRENGTH_AND_BOUNDARIES.md` when a future edit changes how strong a claim sounds or how far it may be read.
Use `CANONICAL_OWNERSHIP_AND_BOUNDARIES.md` when a future edit changes where a package canonically lives or how a non-owner repo may mention it.
Use `CROSS_LAYER_INVARIANTS_AND_CONTRADICTION_POLICY.md` when a future edit may weaken or reverse a load-bearing invariant under local convenience wording.
Use `PRECEDENCE_AND_RESOLUTION.md` when a future edit may let a weaker surface act like override even though the stronger source did not change.
Use `ARTIFACT_ID_AND_REFERENCE_POLICY.md` when a future edit may change path or filename while preserving artifact identity, or may create doubt about whether the artifact is still the same one.
Use `PUBLIC_SAFE_BOUNDARY_AND_EXCLUSION_POLICY.md` when a future edit may blur public-safe material, pointer-only references, excluded classes, or quarantined trees.
Use `PACKAGE_INTAKE_AND_INTEGRATION.md` when a candidate package, layer, repo, or control surface has not yet earned corpus-visible routing and still needs first classification.

## 1. Why this file exists

The canonical layer no longer lives in one file or one repo.
Future edits need predictable sync rules so entry, citation, claims, status, and companion surfaces do not drift apart.

## 2. Canonical surfaces under sync discipline

- `CORPUS_PRIMER.json`
- `STACK_LOCK_2026-04-12.json`
- `CANONICAL_DISTINCTIONS.md`
- `OBJECTIONS_AND_REPLIES.md`
- `CITATION_AND_VERIFICATION.md`
- `CLAIMS_AND_EVIDENCE_MAP.md`
- `STATUS_AND_MATURITY_MAP.md`
- `LOCAL_TO_PUBLIC_PROMOTION_POLICY.md`
- `ATOMIC_PROMOTION_BUNDLES.md`
- `PROMOTION_SEQUENCE_AND_RELEASE_TRANCHES.md`
- `SUPERSESSION_AND_DEPRECATION.md`
- `TERMINOLOGY_AND_ALIAS_POLICY.md`
- `ENTRY_ACCEPTANCE_AND_REGRESSION.md`
- `ASSERTION_STRENGTH_AND_BOUNDARIES.md`
- `CANONICAL_OWNERSHIP_AND_BOUNDARIES.md`
- `CROSS_LAYER_INVARIANTS_AND_CONTRADICTION_POLICY.md`
- `PRECEDENCE_AND_RESOLUTION.md`
- `ARTIFACT_ID_AND_REFERENCE_POLICY.md`
- `PUBLIC_SAFE_BOUNDARY_AND_EXCLUSION_POLICY.md`
- `PACKAGE_INTAKE_AND_INTEGRATION.md`
- `MASTER_ENTRY.md` / `REPO_INDEX.md` / `REPO_INDEX.json` / `MACHINE_ENTRY.md`
- `qubit-of-hope-volume-i/CORPUS_CONTEXT.md`

JSON companions follow the same sync discipline when they exist.

## 3. What counts as repo-local vs corpus-level change

- repo-local change only: a local edit that does not alter corpus reading routes, citation paths, claim routing, status/maturity classification, or cross-repo pointers
- corpus-visible change: an edit that changes how another repo or reader should understand a repo role, package boundary, or entry path
- citation-affecting change: a change to a tag, DOI-backed object, locked ref, preferred citation surface, or verification rule
- claims-affecting change: a change to the canonical artifact, supporting artifact, or routing logic for a load-bearing claim
- status/maturity-affecting change: a change to whether an artifact should be read as `stable`, `draft`, `observed`, `operational`, `companion`, `reserved`, or `control-surface`
- promotion-state-affecting change: a change to whether local work should still be treated as working, accepted, validated, commit-ready, or public-facing
- companion-layer-only change: a change that affects the narrative companion role or its corpus pointers without changing the normative core

## 4. Required sync triggers

| Trigger | What changed | What must be reviewed | What must not be forgotten |
|---|---|---|---|
| `T01` | new canonical package added | `PACKAGE_INTAKE_AND_INTEGRATION.md`; `CORPUS_PRIMER.json`; `STACK_LOCK_2026-04-12.json`; `MASTER_ENTRY.md`; `REPO_INDEX.md`; `REPO_INDEX.json`; `STATUS_AND_MATURITY_MAP.md`; `CLAIMS_AND_EVIDENCE_MAP.md` if claim-bearing | repo role boundary; negative definition; cross-repo pointers |
| `T02` | new stable snapshot / tag / public object added | `CITATION_AND_VERIFICATION.md`; `STACK_LOCK_2026-04-12.json`; `REPO_INDEX.md`; `REPO_INDEX.json`; manifests only where current repo pattern requires them | moving repo != frozen object; GitHub archive != integrity source |
| `T03` | canonical artifact path moved or renamed | `REPO_INDEX.md`; `REPO_INDEX.json`; `MASTER_ENTRY.md`; `CLAIMS_AND_EVIDENCE_MAP.md`; `STATUS_AND_MATURITY_MAP.md`; cross-repo raw pointers | raw URLs; hash manifests; old path may still exist in reports or notes |
| `T04` | claim status materially changes | `CLAIMS_AND_EVIDENCE_MAP.md`; `CITATION_AND_VERIFICATION.md`; `OBJECTIONS_AND_REPLIES.md` or `CANONICAL_DISTINCTIONS.md` only if interpretation changed | citation target may stay narrow even when claim wording shifts |
| `T05` | draft becomes mature core or reserved territory status changes | `STATUS_AND_MATURITY_MAP.md`; `CLAIMS_AND_EVIDENCE_MAP.md` if evidentiary weight changes; `STACK_LOCK_2026-04-12.json` if frozen reading guidance changes | do not silently upgrade adjacent surfaces with it |
| `T06` | narrative companion role changes | `qubit-of-hope-volume-i/CORPUS_CONTEXT.md`; `STATUS_AND_MATURITY_MAP.md`; `CANONICAL_DISTINCTIONS.md`; `OBJECTIONS_AND_REPLIES.md` if public confusion risk changes | narrative companion != normative core unless explicitly reclassified |
| `T07` | new repo enters corpus-level canonical reading path | `PACKAGE_INTAKE_AND_INTEGRATION.md`; `CORPUS_PRIMER.json`; `STACK_LOCK_2026-04-12.json`; `MASTER_ENTRY.md`; `REPO_INDEX.md`; `REPO_INDEX.json`; `STATUS_AND_MATURITY_MAP.md`; cross-repo machine pointers | repo role line; what the new repo is not; where it sits in reading order |
| `T08` | citation / DOI / hash policy changes | `CITATION_AND_VERIFICATION.md`; `STACK_LOCK_2026-04-12.json` if ref policy changes; `REPO_INDEX.md`; `REPO_INDEX.json`; relevant manifests | verification policy must stay aligned with public download wording |
| `T09` | entry surface rewritten in a way that may break discoverability | `README.md`; `MACHINE_ENTRY.md`; `MASTER_ENTRY.md`; `REPO_INDEX.md`; `REPO_INDEX.json`; smoke report | primer, stack lock, citation, claims, status, and book context must remain findable |
| `T10` | supporting artifact becomes canonical, or canonical artifact is superseded | `CLAIMS_AND_EVIDENCE_MAP.md`; `STATUS_AND_MATURITY_MAP.md`; `CITATION_AND_VERIFICATION.md`; `OBJECTIONS_AND_REPLIES.md` or `CANONICAL_DISTINCTIONS.md` if interpretation boundary changes | leave a visible trace of supersession rather than silently swapping meaning |

## 5. Minimal sync checklist

- entry: confirm `README.md`, `MACHINE_ENTRY.md`, `MASTER_ENTRY.md`, and `REPO_INDEX.*` still point to the right corpus-control surfaces
- citation: confirm `CITATION_AND_VERIFICATION.md` still matches the actual public object, tag, DOI, and manifest reality
- claims map: confirm `CLAIMS_AND_EVIDENCE_MAP.md` still points to the right canonical artifact
- status map: confirm `STATUS_AND_MATURITY_MAP.md` still classifies the artifact correctly
- stack lock: update `STACK_LOCK_2026-04-12.json` when the frozen reading state actually changes
- integrity manifests: update only where the current repo pattern already expects them
- cross-repo pointers: confirm raw links and short repo-to-repo pointers still resolve
- terminology lock: confirm no new alias silently rewrites a load-bearing corpus term
- acceptance review: confirm `ENTRY_ACCEPTANCE_AND_REGRESSION.md` still describes the touched corpus state truthfully
- assertion force: confirm `ASSERTION_STRENGTH_AND_BOUNDARIES.md` still matches how the touched surfaces should be read
- ownership home: confirm touched repo text still points to the canonical owner instead of silently re-owning the layer
- invariant safety: confirm touched text does not silently reverse a load-bearing corpus invariant
- precedence safety: confirm a weaker or contextual surface did not start acting like override
- artifact identity safety: confirm path/name drift did not silently create a new artifact identity
- public-safe boundary: confirm touched material is still clearly public-safe, pointer-only, or excluded, and that quarantined trees were not used
- intake review: confirm `PACKAGE_INTAKE_AND_INTEGRATION.md` still classifies new package/repo/control-surface additions before they spread
- promotion review: confirm `LOCAL_TO_PUBLIC_PROMOTION_POLICY.md` still matches the real local/public state when outward promotion is being considered
- promotion bundle scope: confirm the minimally coupled bundle in `ATOMIC_PROMOTION_BUNDLES.md` is identified before outward promotion
- promotion sequencing: confirm an earlier supporting tranche is not being skipped by `PROMOTION_SEQUENCE_AND_RELEASE_TRANCHES.md` logic
- smoke check: confirm a serious reader or machine can still find primer, stack lock, citation, claims, status, public-safe boundary, package intake, terminology policy, and companion context

## 6. Fail-closed rule

If a maintainer cannot establish whether a change is repo-local or corpus-level,
treat it as corpus-level until clarified.

Do not rely on memory, intent, or "probably local" guesswork when canonical routing may be affected.

## 7. Read next

- `CONTROL_SURFACE_DEPENDENCY_AND_COUPLING_MAP.md`
- `CORPUS_PRIMER.json`
- `STACK_LOCK_2026-04-12.json`
- `CITATION_AND_VERIFICATION.md`
- `CLAIMS_AND_EVIDENCE_MAP.md`
- `STATUS_AND_MATURITY_MAP.md`
- `LOCAL_TO_PUBLIC_PROMOTION_POLICY.md`
- `ATOMIC_PROMOTION_BUNDLES.md`
- `PROMOTION_SEQUENCE_AND_RELEASE_TRANCHES.md`
- `SUPERSESSION_AND_DEPRECATION.md`
- `TERMINOLOGY_AND_ALIAS_POLICY.md`
- `ENTRY_ACCEPTANCE_AND_REGRESSION.md`
- `ASSERTION_STRENGTH_AND_BOUNDARIES.md`
- `CANONICAL_OWNERSHIP_AND_BOUNDARIES.md`
- `CROSS_LAYER_INVARIANTS_AND_CONTRADICTION_POLICY.md`
- `PRECEDENCE_AND_RESOLUTION.md`
- `ARTIFACT_ID_AND_REFERENCE_POLICY.md`
- `PUBLIC_SAFE_BOUNDARY_AND_EXCLUSION_POLICY.md`
- `PACKAGE_INTAKE_AND_INTEGRATION.md`
