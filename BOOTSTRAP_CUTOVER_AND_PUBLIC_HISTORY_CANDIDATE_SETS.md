# Bootstrap Cutover and Public History Candidate Sets

## Purpose

This file fixes a compact corpus-level discipline for bounded candidate sets that could later support public-history cutover from the already-built local canonical stack. It is not a release execution plan, but a grouping rule for how future public history could stay legible and bounded.
Use `PUBLIC_HISTORY_ANNOTATION_AND_RELEASE_NOTE_POLICY.md` when the remaining question is not which bounded set should move, but how that step should be annotated once it appears.

## 1. Why this file exists

The corpus now contains a substantial local canonical layer.
This file defines how that layer could later be promoted in bounded candidate sets instead of one noisy undifferentiated public jump.

## 2. Core rule

Candidate set planning is not public execution.
It is a bounded grouping discipline for eventual public history. Use
`LOCAL_PROMOTION_DOCKET_AND_BLOCKER_REGISTRY.md` when the remaining question is
not cutover-set design, but concrete file-level local placement and blocker
tracking inside the already-present local stack.

## 3. Candidate set table

| Cutover ID | Candidate set | Goal | Minimum surfaces | Why bounded this way | What should stay out of this set |
|---|---|---|---|---|---|
| `CS01` | foundational entry/control baseline set | establish a bounded first public control baseline | `CORPUS_PRIMER.json`; `STACK_LOCK_2026-04-12.json`; `README.md`; `MACHINE_ENTRY.md`; `MASTER_ENTRY.md`; `REPO_INDEX.md`; `REPO_INDEX.json`; `qubit-of-hope-volume-i/CORPUS_CONTEXT.md` basics | public history first needs routing, role clarity, and a stable corpus map | later claim maps, promotion-control layers, and outward handoff logic should stay out |
| `CS02` | anti-confusion and citation set | bound interpretation before later authority layers appear | `CANONICAL_DISTINCTIONS.md`; `OBJECTIONS_AND_REPLIES.md`; `CITATION_AND_VERIFICATION.md` | early public history becomes easier to read when confusion and citation guardrails are visible | claim/status packages, ownership layers, and promotion-control layers should stay out |
| `CS03` | claims/status/assertion set | expose what the corpus claims, how mature those claims are, and how strongly they should be read | `CLAIMS_AND_EVIDENCE_MAP.md`; `STATUS_AND_MATURITY_MAP.md`; `ASSERTION_STRENGTH_AND_BOUNDARIES.md` | claim carriers read more cleanly once routing, anti-confusion, and citation posture already exist | promotion-control layers, handoff profiles, and open-question framing should stay out |
| `CS04` | ownership/precedence/invariant set | fix canonical home, governing-source order, and invariant protection | `CANONICAL_OWNERSHIP_AND_BOUNDARIES.md`; `CROSS_LAYER_INVARIANTS_AND_CONTRADICTION_POLICY.md`; `PRECEDENCE_AND_RESOLUTION.md` | authority and boundary discipline should appear together rather than as isolated later patches | export/handoff layers, promotion-control layers, and open-question framing should stay out |
| `CS05` | public-safe / audience / export set | make outward-safe routing and bounded handoff logic explicit | `PUBLIC_SAFE_BOUNDARY_AND_EXCLUSION_POLICY.md`; `AUDIENCE_PROFILES_AND_MINIMAL_READING_PATHS.md`; `EXPORT_PROFILES_AND_HANDOFF_BUNDLES.md` | outward-facing logic is clearest after earlier orientation, claims, and authority framing are already visible | promotion-control layers, open-question framing, and unrelated artifact/intake layers should stay out |
| `CS06` | promotion-control set | make local/public cutover discipline explicit once earlier supports already exist | `LOCAL_TO_PUBLIC_PROMOTION_POLICY.md`; `ATOMIC_PROMOTION_BUNDLES.md`; `PROMOTION_SEQUENCE_AND_RELEASE_TRANCHES.md` | policy, atomicity, and sequence are more legible after foundational, interpretive, and boundary framing is already public | unrelated claim/status material and open-question framing should stay out |
| `CS07` | open-questions / bounded non-closure set | show deliberate incompleteness without making the first public step conceptually noisy | `OPEN_QUESTIONS_AND_EXPLICIT_NON_CLAIMS.md` | non-closure reads best once earlier framing already shows what is claimed, bounded, and routable | earlier foundational or promotion-control layers should not be mixed back into this late set |

## 4. Cutover anti-patterns

| ID | Anti-pattern | What goes wrong | Why it harms future public history |
|---|---|---|---|
| `CP01` | first public cutover includes too many unrelated control layers | the first public step becomes an undifferentiated mass of routing, claims, boundaries, and promotion logic | reviewers cannot tell what the initial public baseline was supposed to establish |
| `CP02` | anti-confusion surfaces missing from early public history | later public layers appear before distinctions, objections, and citation guardrails are visible | readers inherit later control wording without the framing needed to interpret it safely |
| `CP03` | claims/status exported before their interpretive guardrails | claims and maturity classes appear before citation and anti-confusion context | public history starts sounding stronger or clearer than the visible guardrails justify |
| `CP04` | public-safe/export surfaces published without boundary context | outward bundle logic appears before safety classes are explicit | readers may infer that export logic is broader or safer than the corpus actually established |
| `CP05` | promotion-control surfaces published before enough earlier framing exists | policy, atomicity, or sequencing language appears before the public baseline they depend on | public history can look procedurally sophisticated while still conceptually under-framed |
| `CP06` | open-question layer published without earlier claim/status framing | explicit non-closure appears before the corpus shows what is already claimed and how mature it is | later readers cannot tell whether openness is deliberate restraint or just missing structure |
| `CP07` | one repo appears fully current while adjacent repos still lack minimal routing | public history looks lopsided across repos and the stack starts reading as unevenly canonized | cross-repo readers lose the bounded corpus map and start over-reading whichever repo looks most complete |
| `CP08` | candidate set treated as command to publish immediately | bounded grouping guidance is mistaken for actual release authorization | planning language gets misread as execution, readiness, or promise |

## 5. Fail-closed cutover rule

If maintainers cannot determine whether a local layer belongs in an earlier or later candidate set, default to the smaller earlier bounded set and delay wider promotion.

## 6. Read next

- `CURRENT_LOCAL_CONTROL_STACK_STAGING_MAP.md`
- `LOCAL_PROMOTION_DOCKET_AND_BLOCKER_REGISTRY.md`
- `LOCAL_TO_PUBLIC_PROMOTION_POLICY.md`
- `CURRENT_CORPUS_STATE_AND_READINESS_SNAPSHOT.md`
- `ATOMIC_PROMOTION_BUNDLES.md`
- `PROMOTION_SEQUENCE_AND_RELEASE_TRANCHES.md`
- `ENTRY_ACCEPTANCE_AND_REGRESSION.md`
- `PUBLIC_SAFE_BOUNDARY_AND_EXCLUSION_POLICY.md`
- `PUBLIC_HISTORY_ANNOTATION_AND_RELEASE_NOTE_POLICY.md`
