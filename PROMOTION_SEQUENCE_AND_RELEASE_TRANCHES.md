# Promotion Sequence and Release Tranches

## Purpose

This file fixes a compact corpus-level sequencing discipline for bounded future promotion of local canonical layers into public git-history. It says in which order minimally coupled promotion bundles should ideally appear, without becoming a release calendar, commit script, or execution instruction.
Use `BOOTSTRAP_CUTOVER_AND_PUBLIC_HISTORY_CANDIDATE_SETS.md` when the remaining question is not tranche order, but which bounded candidate set should reasonably be used for a future first or later public-history cutover step.
Use `PUBLIC_HISTORY_ANNOTATION_AND_RELEASE_NOTE_POLICY.md` when the remaining question is not sequence, but how the bounded public-history step should be explained once visible.

## 1. Why this file exists

Atomic bundles say what must move together.
This file says in which order such bundles should ideally be promoted so public history stays legible, bounded, and non-chaotic.

## 2. Core rule

Not every commit-ready local layer should be promoted immediately.
Sequence matters because later control surfaces often presuppose earlier routing, anti-confusion, and boundary framing.

## 3. Canonical tranche table

| Tranche ID | Tranche name | Goal | Minimum surfaces | Why this tranche comes here | What should not be promoted before it |
|---|---|---|---|---|---|
| `TR01` | entry-and-orientation tranche | establish bounded first-pass routing and frozen-reading basics | `CORPUS_PRIMER.json`; `STACK_LOCK_2026-04-12.json`; first machine-entry cleanup; `qubit-of-hope-volume-i/CORPUS_CONTEXT.md` basics | later control layers are harder to read if baseline routing and corpus role boundaries do not already exist | later anti-confusion, claim, or promotion-history surfaces should not appear before orientation exists |
| `TR02` | anti-confusion tranche | prevent early public misreading of terms, scope, and objections | `CANONICAL_DISTINCTIONS.md`; `OBJECTIONS_AND_REPLIES.md`; `CITATION_AND_VERIFICATION.md` | claims and status are easier to read once confusion and citation posture are already bounded | later claim, ownership, or handoff surfaces should not precede anti-confusion control |
| `TR03` | claim-and-status tranche | expose what the corpus claims and how strongly or maturely it should be read | `CLAIMS_AND_EVIDENCE_MAP.md`; `STATUS_AND_MATURITY_MAP.md`; `ASSERTION_STRENGTH_AND_BOUNDARIES.md` | public readers need claims, maturity, and reading force together before later governance layers make sense | later open-question, handoff, or promotion-history layers should not outrun claim/status framing |
| `TR04` | control-discipline tranche | establish maintenance and reading-discipline rules for the visible public layer | `CHANGE_CONTROL_AND_SYNC.md`; `SUPERSESSION_AND_DEPRECATION.md`; `TERMINOLOGY_AND_ALIAS_POLICY.md`; `ENTRY_ACCEPTANCE_AND_REGRESSION.md` | once claims are public, the maintenance rules for keeping them coherent should become visible | promotion-history or later boundary planning should not precede this control discipline |
| `TR05` | ownership-and-precedence tranche | fix canonical home, governing-source order, and invariant safety | `CANONICAL_OWNERSHIP_AND_BOUNDARIES.md`; `CROSS_LAYER_INVARIANTS_AND_CONTRADICTION_POLICY.md`; `PRECEDENCE_AND_RESOLUTION.md` | boundary and authority questions are clearer after orientation, anti-confusion, claims, and maintenance rules already exist | artifact, handoff, or later promotion-planning layers should not precede governing-source clarification |
| `TR06` | artifact-and-intake tranche | stabilize artifact identity and the path for new package admission | `ARTIFACT_ID_AND_REFERENCE_POLICY.md`; `PACKAGE_INTAKE_AND_INTEGRATION.md` | identity and intake decisions are easier to read once ownership and precedence are already visible | later promotion-history and outward handoff layers should not precede identity and intake discipline |
| `TR07` | boundary-and-handoff tranche | bound public-safe exposure, audience paths, and outward bundle sufficiency | `PUBLIC_SAFE_BOUNDARY_AND_EXCLUSION_POLICY.md`; `AUDIENCE_PROFILES_AND_MINIMAL_READING_PATHS.md`; `EXPORT_PROFILES_AND_HANDOFF_BUNDLES.md` | outward-facing routing should come after earlier framing, authority, and identity layers are already public | promotion-history or companion-facing handoff should not outrun public-safe boundary logic |
| `TR08` | promotion-and-history tranche | make local/public history discipline explicit once earlier supporting control surfaces already exist | `LOCAL_TO_PUBLIC_PROMOTION_POLICY.md`; `ATOMIC_PROMOTION_BUNDLES.md` | promotion-state and atomic-bundle rules are safer once the earlier control layer can already support them | these history-facing rules should not appear before the supporting control surfaces they depend on |
| `TR09` | open-questions tranche | show deliberate incompleteness without letting it masquerade as silent closure | `OPEN_QUESTIONS_AND_EXPLICIT_NON_CLAIMS.md` | open territory is easier to read once claims, status, authority, and boundary framing are already public | unresolved-territory wording should not appear before stronger framing explains what is already claimed and what is not |
| `TR10` | future optional consolidation tranche | allow later cleanup, index tightening, or bounded consolidation after prior tranches are already public | short later cleanup or consolidation pass only after prior tranche visibility exists | consolidation is least misleading once the earlier public-history layers are already visible in order | noisy mixed cleanup should not be used as a substitute for the earlier tranche sequence |

## 4. Sequencing anti-patterns

| ID | Anti-pattern | What goes wrong | Why it harms public history readability |
|---|---|---|---|
| `SQ01` | promoting late control layers before basic entry orientation exists | public history starts with downstream control wording but no stable first-pass route | later readers meet conclusions before they can even identify the corpus map |
| `SQ02` | promoting claims/status without citation and routing clarity | claims appear before citation posture and anti-confusion framing are visible | public readers cannot tell what the claims point to or how narrowly they should be read |
| `SQ03` | promoting ownership/precedence without earlier anti-confusion control | authority and canonical-home language appears before confusion boundaries are fixed | public history begins to look like internal re-ordering without the framing needed to interpret it |
| `SQ04` | promoting handoff/export before public-safe boundary exists | outward bundle logic appears before safety and exclusion classes are public | readers may infer that outward sharing rules are broader or safer than the corpus actually established |
| `SQ05` | promoting promotion policy before acceptance/sync layer exists | local/public state language appears before the maintenance rules that justify it | public history can look procedurally authoritative without the earlier control discipline |
| `SQ06` | promoting open-question layer before stronger claims/status framing exists | unresolved territory appears before the corpus shows what is already claimed and how mature it is | non-closure becomes harder to interpret and may look like vagueness rather than deliberate restraint |
| `SQ07` | promoting later tranches in isolation so public history appears conceptually backward | later history-facing or boundary-facing layers arrive without their earlier supports | the visible sequence starts to misrepresent conceptual dependence inside the corpus |
| `SQ08` | mixing unrelated tranche content into one noisy undifferentiated promotion step | public history receives too many unrelated control moves at once | reviewers lose the ability to see what changed first, why, and which layer actually depends on which |

## 5. Fail-closed sequencing rule

If maintainers cannot determine whether a local layer belongs to an earlier or later tranche, default to the earlier supporting tranche logic before promotion.

## 6. Read next

- `LOCAL_TO_PUBLIC_PROMOTION_POLICY.md`
- `ATOMIC_PROMOTION_BUNDLES.md`
- `BOOTSTRAP_CUTOVER_AND_PUBLIC_HISTORY_CANDIDATE_SETS.md`
- `PUBLIC_HISTORY_ANNOTATION_AND_RELEASE_NOTE_POLICY.md`
- `CHANGE_CONTROL_AND_SYNC.md`
- `ENTRY_ACCEPTANCE_AND_REGRESSION.md`
- `PUBLIC_SAFE_BOUNDARY_AND_EXCLUSION_POLICY.md`
