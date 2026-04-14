# Public Correction and Errata Policy

## Purpose

This file fixes a compact corpus-level discipline for bounded public correction once something is already visible in public history. It is not a supersession file, promotion file, release-note file, changelog, or rollback script.

## 1. Why this file exists

A mature corpus must not only promote bounded public history,
but also correct it without silent rewriting or theatrical overreaction.

## 2. Core rule

Public-visible correction should be explicit, bounded, and typed.
Neither silent rewrite nor dramatic self-annulment should be default.

## 3. Canonical correction classes

| Correction ID | Correction class | Meaning | Use when | Must NOT be confused with |
|---|---|---|---|---|
| `EC01` | clarification note | explain a bounded ambiguity without changing the underlying claim or artifact state | wording invited misreading but the underlying surface still stands | erratum, bounded correction, or retraction |
| `EC02` | erratum | correct a bounded mistake that does not overturn the wider surface | a typo, narrow wording fault, or small factual slip is real and should be visible | supersession or full retraction |
| `EC03` | bounded correction | correct a mistake that changes part of the public reading but leaves other parts intact | some prior reading is no longer safe, but the whole surface is not void | total collapse or silent patching |
| `EC04` | supersession notice | mark that a newer governing surface now outranks an older public one | the public history needs explicit preferred-current routing rather than same-surface repair | erratum or retraction |
| `EC05` | retraction | withdraw a public-facing reading or surface that should no longer be relied on in its prior form | the earlier public reading is no longer trustworthy enough to leave as active guidance | bounded correction where most of the surface still stands |
| `EC06` | quarantine / do-not-use notice | mark a public-facing surface as unsafe to rely on until clarified or replaced | public use should pause because safety, boundary, or trust impact is unresolved | ordinary boundary class or rhetorical alarm language |
| `EC07` | pointer-fix / reference repair | repair path, link, raw pointer, or reference routing without silently implying doctrinal change | broken routing or stale refs need visible repair | claim correction unless claim/citation impact is real |
| `EC08` | non-correction / no-action case | record that apparent drift does not require a public correction step | the issue is only alias, formatting, or non-public noise with no public-reading impact | hidden correction by omission |

## 4. Minimal correction fields

| ID | Field | Minimum meaning |
|---|---|---|
| `CF01` | what is being corrected | Name the bounded surface, note, path, or reading that is under correction. |
| `CF02` | correction class | State which correction class governs this case. |
| `CF03` | what remains valid | Say which part of the earlier public reading still stands. |
| `CF04` | what is no longer safe to read as before | State the exact prior reading that should now stop. |
| `CF05` | whether claims/status/citation are affected | Say explicitly whether interpretive or evidentiary reading conditions changed. |
| `CF06` | whether manifests / refs changed | State yes/no and keep the scope bounded to touched repo-pattern surfaces. |
| `CF07` | what stronger or newer surface now governs | Name the current governing or replacement surface when relevant. |
| `CF08` | what this correction is NOT claiming | State the nearest overread that should be rejected. |

## 5. Correction anti-patterns

| ID | Anti-pattern | What goes wrong | Why it harms public trust |
|---|---|---|---|
| `CA01` | silent rewrite without visible correction signal | public history changes but readers never see that a correction happened | trust drops because chronology stops being auditable |
| `CA02` | using supersession where simple erratum is enough | a small bounded fix gets narrated as if a whole replacement occurred | public history becomes noisier and less precise than needed |
| `CA03` | using retraction where bounded correction is enough | a surface is withdrawn more aggressively than the actual mistake warrants | readers may infer wider collapse than the corpus supports |
| `CA04` | vague correction note that hides affected scope | the correction exists but does not say what exactly changed | readers cannot tell what to keep or stop relying on |
| `CA05` | correction note that implies whole-corpus collapse | a local correction is narrated like systemic failure of everything nearby | bounded public trust gets replaced by unnecessary theatrical doubt |
| `CA06` | pointer fix issued without checking claim/citation impact | a routing repair is announced as if it had no interpretive consequences when it might | broken citation or claims drift can survive under a cosmetic fix label |
| `CA07` | quarantine wording used as rhetorical overkill | do-not-use language is used where ordinary correction would suffice | strong safety language loses precision and credibility |
| `CA08` | correction note that does not state what remains valid | the note marks a problem but leaves surviving meaning implicit | readers over-discard or keep too much by guesswork |

## 6. Fail-closed correction rule

If maintainers cannot determine whether an issue is only wording, citation, claim, or public-safety relevant,
choose the stronger bounded correction class until clarified.

## 7. Read next

- `SUPERSESSION_AND_DEPRECATION.md`
- `PRECEDENCE_AND_RESOLUTION.md`
- `PUBLIC_HISTORY_ANNOTATION_AND_RELEASE_NOTE_POLICY.md`
- `CLAIMS_AND_EVIDENCE_MAP.md`
- `ENTRY_ACCEPTANCE_AND_REGRESSION.md`
- `CURRENT_CORPUS_STATE_AND_READINESS_SNAPSHOT.md`
- `PUBLIC_SAFE_BOUNDARY_AND_EXCLUSION_POLICY.md`
