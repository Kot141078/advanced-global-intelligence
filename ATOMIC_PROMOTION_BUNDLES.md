# Atomic Promotion Bundles

## Purpose

This file fixes a compact corpus-level discipline for bounded atomic promotion into public git-history. It states which minimally coupled canonical surfaces should move together when promotion happens, without redefining promotion state, ownership, repo-pattern integrity, or public-safe boundary class.
Use `PROMOTION_SEQUENCE_AND_RELEASE_TRANCHES.md` when the remaining question is not what moves together, but in which order such bundles should ideally appear in public history.
Use `BOOTSTRAP_CUTOVER_AND_PUBLIC_HISTORY_CANDIDATE_SETS.md` when the remaining question is which bounded candidate set should contain a bundle during eventual public-history cutover.
Use `PUBLIC_HISTORY_ANNOTATION_AND_RELEASE_NOTE_POLICY.md` when the remaining question is how a bounded promoted bundle should be described once it appears in public history.

## 1. Why this file exists

Public history should not receive half-promoted corpus layers.
When one load-bearing control surface is promoted, the related surfaces that carry its routing, status, reference, or boundary meaning should be considered together.

## 2. Core rule

If one file in a canonical layer is promoted, all minimally coupled files for that layer must be considered together.
No silent partial promotion.

## 3. Canonical bundle table

| Bundle ID | Bundle name | Primary trigger | Minimum files / surfaces | Why atomicity matters | What must be checked before promotion |
|---|---|---|---|---|---|
| `AB01` | entry/control surface bundle | a canonical layer is added, renamed, removed, or rerouted | `README.md`; `MACHINE_ENTRY.md`; `MASTER_ENTRY.md`; `REPO_INDEX.md`; `REPO_INDEX.json` where relevant | public readers and machines should keep finding the same control layer without a second search step | confirm discoverability and routing stay coherent across entry/control surfaces |
| `AB02` | citation / reference bundle | citation target, verification wording, or preferred public object changes | `CITATION_AND_VERIFICATION.md` plus affected citation-facing entry or index surfaces | citation drift can turn public history into a false reference map | confirm citation target, verification wording, and outward download wording still describe the same object |
| `AB03` | claims / status / assertion bundle | claim wording, evidentiary routing, maturity class, or claim force changes | `CLAIMS_AND_EVIDENCE_MAP.md`; `STATUS_AND_MATURITY_MAP.md`; `ASSERTION_STRENGTH_AND_BOUNDARIES.md` where coupled | a promoted claim should not outrun its status class or permitted reading force | confirm canonical artifact, maturity class, and assertion strength still agree |
| `AB04` | ownership / precedence / invariants bundle | canonical home, governing source, or invariant wording changes | `CANONICAL_OWNERSHIP_AND_BOUNDARIES.md`; `PRECEDENCE_AND_RESOLUTION.md`; `CROSS_LAYER_INVARIANTS_AND_CONTRADICTION_POLICY.md` where coupled | public history should not preserve a boundary shift without its governing and invariant context | confirm ownership, governing precedence, and invariant wording do not contradict each other |
| `AB05` | sync / acceptance / promotion discipline bundle | maintenance rules, acceptance standard, or promotion-state discipline changes | `CHANGE_CONTROL_AND_SYNC.md`; `ENTRY_ACCEPTANCE_AND_REGRESSION.md`; `LOCAL_TO_PUBLIC_PROMOTION_POLICY.md` | promotion discipline should not drift away from sync and acceptance discipline | confirm acceptance threshold, sync obligations, and promotion-state wording still fit the same maintenance reality |
| `AB06` | artifact identity / supersession bundle | a stable artifact ID is added, moved, renamed, retained, or superseded | `ARTIFACT_ID_AND_REFERENCE_POLICY.md`; `SUPERSESSION_AND_DEPRECATION.md`; affected maps where identity state matters | reference identity and supersession state should not be promoted as separate stories | confirm the artifact is still the same one, or that the new state and retained trace are explicit |
| `AB07` | public-safe / export / audience bundle | outward handoff wording, audience path, or public-safe boundary class changes | `PUBLIC_SAFE_BOUNDARY_AND_EXCLUSION_POLICY.md`; `EXPORT_PROFILES_AND_HANDOFF_BUNDLES.md`; `AUDIENCE_PROFILES_AND_MINIMAL_READING_PATHS.md` | outward-facing routing should not overclaim bundle safety or audience sufficiency | confirm boundary class, enough-for wording, and audience path remain aligned and bounded |
| `AB08` | open-question / reserved-boundary bundle | unresolved territory, explicit non-claim, or reserved boundary wording changes | `OPEN_QUESTIONS_AND_EXPLICIT_NON_CLAIMS.md` plus affected boundary or status surfaces | unresolved territory should not look settled because only one surface was promoted | confirm open questions remain open and reserved territory is not silently upgraded |
| `AB09` | package-intake / new-package bundle | a new package, repo, or control surface enters corpus-visible routing | `PACKAGE_INTAKE_AND_INTEGRATION.md` plus ownership, status, claims, or artifact-id surfaces as needed | public routing should not harden an unclassified package into canon by inertia | confirm role, owner, status, and citation/reference posture are fixed before promotion |
| `AB10` | repo-pattern integrity bundle | touched files require integrity refresh under the current repo pattern | only the manifests already required by the touched repo set | manifest churn should not become a fake substitute for canonical coherence | confirm manifest scope stays bounded to the existing repo pattern and matches the touched surfaces |

## 4. Non-atomic anti-patterns

| ID | Anti-pattern | What goes wrong | Why partial promotion is dangerous |
|---|---|---|---|
| `APB01` | claims map updated without status/assertion review | claim routing changes while maturity class or reading force stays stale | public history can preserve stronger meaning than the corpus actually granted |
| `APB02` | new canonical layer added without routing/discoverability refresh | the new layer exists but control surfaces do not route readers or machines to it | a canonical file becomes effectively hidden and later review starts from stale entry points |
| `APB03` | artifact ID introduced without reference-state / supersession review | a new identifier appears without clear continuity or retained-state handling | later readers cannot tell whether promotion preserved identity or silently replaced it |
| `APB04` | export bundle changed without public-safe boundary review | outward bundle wording expands while boundary class stays unreviewed | public-safe drift can turn bounded handoff into accidental overexposure or overclaim |
| `APB05` | promotion policy changed without acceptance/sync review | commit-readiness language changes but local checks and sync duties do not | public-history promotion starts using a rule the rest of the control layer does not support |
| `APB06` | ownership changed without precedence review | canonical-home wording changes while governing-source rules stay stale | a weaker or non-owner surface can start behaving like override in public history |
| `APB07` | open-question layer changed without boundary/status review | unresolved territory wording moves but reserved or status surfaces do not | public readers may import closure or maturity that the corpus still withholds |
| `APB08` | manifest updated without corresponding canonical surface coherence check | hashes refresh while the logical control bundle is still inconsistent | integrity traces can make a broken half-promotion look more settled than it is |

## 5. Fail-closed promotion-bundle rule

If maintainers cannot determine whether a change belongs to a larger atomic bundle, promotion should pause until the minimally coupled bundle is identified.

## 6. Read next

- `CONTROL_SURFACE_DEPENDENCY_AND_COUPLING_MAP.md`
- `LOCAL_TO_PUBLIC_PROMOTION_POLICY.md`
- `PROMOTION_SEQUENCE_AND_RELEASE_TRANCHES.md`
- `BOOTSTRAP_CUTOVER_AND_PUBLIC_HISTORY_CANDIDATE_SETS.md`
- `PUBLIC_HISTORY_ANNOTATION_AND_RELEASE_NOTE_POLICY.md`
- `CHANGE_CONTROL_AND_SYNC.md`
- `ENTRY_ACCEPTANCE_AND_REGRESSION.md`
- `ARTIFACT_ID_AND_REFERENCE_POLICY.md`
- `SUPERSESSION_AND_DEPRECATION.md`
- `PUBLIC_SAFE_BOUNDARY_AND_EXCLUSION_POLICY.md`
