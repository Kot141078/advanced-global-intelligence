# Public History Annotation and Release Note Policy

## Purpose

This file fixes a compact corpus-level discipline for the minimum explanatory note that should accompany any future bounded promotion into public git-history. It is not a release execution plan, full changelog manual, commit-message template, or marketing layer.
Use `PUBLIC_CORRECTION_AND_ERRATA_POLICY.md` when the remaining question is no longer how to annotate a new public step, but how to correct or qualify a public step that is already visible.

## 1. Why this file exists

Bounded promotion without bounded annotation produces opaque public history.
This file fixes the minimum explanatory layer for future public-facing steps.

## 2. Core rule

A public-history step should not appear as silent file movement.
It should carry a bounded annotation explaining what moved, why, and what did not change.

## 3. Minimal annotation fields

| ID | Field | Minimum meaning |
|---|---|---|
| `AF01` | scope of the promoted set | Name the bounded set or bundle that moved, not the whole corpus. |
| `AF02` | why this set is appearing now | State the narrow reason this step became timely or legible. |
| `AF03` | what type of layer it is | Identify whether the step is control, claim, boundary, runtime-proof, companion, or other bounded layer. |
| `AF04` | what it is enough for | Say the narrow public-reading or review use this step now supports. |
| `AF05` | what it is not enough for | State the nearest stronger reading that still remains unsupported. |
| `AF06` | what related layers remain local or later | Name the adjacent layers that did not move or still remain deferred. |
| `AF07` | whether this is foundational, follow-on, or late-boundary material | Place the step in its bounded public-history position. |
| `AF08` | whether any citation / claims / status surfaces were affected | Say explicitly whether interpretive or evidentiary reading conditions changed. |
| `AF09` | whether manifests were refreshed by existing repo-pattern | State yes/no and keep manifest scope bounded to the touched repo-pattern. |
| `AF10` | promotion does not close the whole corpus | Say explicitly that bounded promotion is not whole-corpus completion. |

## 4. Annotation note types

| ID | Note type | Use for | Tone | Must avoid |
|---|---|---|---|---|
| `NT01` | foundational control-layer note | entry, routing, or corpus-control steps | dry and orienting | sounding like doctrinal completion |
| `NT02` | anti-confusion / citation note | distinctions, objections, citation, or verification steps | clarifying and bounded | sounding like new doctrine by itself |
| `NT03` | claims-status note | claims, maturity, or assertion-strength steps | evidentiary and scope-limited | overstating maturity or finality |
| `NT04` | promotion-control note | promotion policy, atomicity, tranche, candidate-set, or annotation steps | procedural and restrained | sounding like release authorization |
| `NT05` | boundary / public-safe note | boundary, audience, export, or safety-facing steps | safety-bounded and explicit | implying broader exposure than established |
| `NT06` | open-question / non-closure note | deliberate incompleteness or reserved-territory visibility | restrained and non-final | pretending unresolved territory is now settled |

## 5. Annotation anti-patterns

| ID | Anti-pattern | What goes wrong | Why it harms public readability |
|---|---|---|---|
| `AN01` | sounding like full-corpus completion | a narrow step is narrated as if the whole stack is now done | readers import closure the corpus did not grant |
| `AN02` | implying productization where only runtime-proof moved | implementation proof is described like finished platform release | runtime skeleton starts reading like market-ready product |
| `AN03` | implying doctrinal closure where only control layers moved | entry or control surfaces are narrated like final doctrine | routing and maintenance layers start masquerading as proof |
| `AN04` | hiding later unresolved tranches | the note omits what still remains local, later, or unpromoted | public history starts looking cleaner than the actual sequence |
| `AN05` | using vague hype language instead of bounded scope | the note replaces scope with praise, scale, or momentum language | future readers cannot tell what actually changed |
| `AN06` | collapsing companion movement into normative proof | companion-facing movement is narrated like evidence or doctrine | narrative role starts outranking stronger canonical surfaces |
| `AN07` | omitting enough-for / not-enough-for boundary | the note says what moved but not how far it may be read | bounded promotion becomes easy to over-read |
| `AN08` | turning a narrow public step into a grandiose narrative | a small step is framed as historical culmination or total breakthrough | public history becomes harder to trust or audit later |

## 6. Fail-closed annotation rule

If maintainers cannot describe a bounded promotion in a short, truthful, scope-limited note,
the promotion is probably not yet cleanly bounded enough for public history.

## 7. Read next

- `LOCAL_TO_PUBLIC_PROMOTION_POLICY.md`
- `ATOMIC_PROMOTION_BUNDLES.md`
- `PROMOTION_SEQUENCE_AND_RELEASE_TRANCHES.md`
- `BOOTSTRAP_CUTOVER_AND_PUBLIC_HISTORY_CANDIDATE_SETS.md`
- `CURRENT_CORPUS_STATE_AND_READINESS_SNAPSHOT.md`
- `EXPORT_PROFILES_AND_HANDOFF_BUNDLES.md`
- `OPEN_QUESTIONS_AND_EXPLICIT_NON_CLAIMS.md`
- `PUBLIC_CORRECTION_AND_ERRATA_POLICY.md`
