# Precedence and Resolution

## Purpose

This file fixes a compact corpus-level precedence discipline for apparent tension between canonical surfaces. It helps maintainers, serious readers, reviewers, and machine readers distinguish primary source from explanation, routing, context, implementation evidence, and retained history.
Use `ARTIFACT_ID_AND_REFERENCE_POLICY.md` when the apparent tension is really path drift or rename drift around the same artifact rather than a true authority conflict.
Use `PACKAGE_INTAKE_AND_INTEGRATION.md` when the remaining question is whether a candidate package or surface should enter corpus-visible routing at all before precedence is even applied.
Use `AUDIENCE_PROFILES_AND_MINIMAL_READING_PATHS.md` when the remaining question is which bounded reader bundle should be taken before precedence questions are generalized outward.
Use `PUBLIC_CORRECTION_AND_ERRATA_POLICY.md` when the conflict is already public-facing and the remaining question is which explicit correction class should be issued rather than only which surface governs.

## 1. Why this file exists

A mature multi-repo corpus needs explicit precedence rules.
Without them, overlap turns into ambiguity and explanatory text can start acting like silent override.

## 2. Core rule

A surface may explain, contextualize, route, summarize, or operationalize.
It must not silently override a stronger canonical source.

## 3. Canonical precedence table

Default reading: lower precedence level means stronger current authority for override questions.
Apply the table to the actual question under review rather than as a blunt universal ranking for every sentence.

| Precedence ID | Surface type | Precedence level | What it may do | What it may NOT do | Typical examples |
|---|---|---:|---|---|---|
| `P01` | Primary canonical artifact | `1` | carry the designated primary meaning for the claim, package, or question at hand | be displaced by summaries, pointers, or companions without explicit corpus-level change | `protocols/c_a_b_protocol_v1.1_L4_EN.md`<br>`sovereign-entity-recursion/protocol/SER_v1.3_EN.md` |
| `P02` | Stable doctrinal core surface | `2` | define mature stable doctrine for a core layer | be read as optional commentary or be silently outranked by weaker drafts | `sovereign-entity-recursion/protocol/SER_v1.3_EN.md` |
| `P03` | Draft normative surface | `3` | state serious current proposals and bounded draft norms | imply mature finality or outrank stable core by repetition alone | `sovereign-entity-recursion/protocol/ser-fed/SER-FED_v0.2_RFC_EN.md`<br>`docs/economic-layer/Economic_Layer_for_Experience_Artifacts_v0.1.md` |
| `P04` | Observed protocol / practice-derived surface | `4` | record recurrent behavior, practice-derived stability, or observed protocol shape | silently become universal law, ontology, or mature doctrine | observed protocol notes<br>practice-derived stability surfaces |
| `P05` | Evidence / witness verification surface | `5` | verify operational trace, admissibility, replayability, and tamper-evident review paths | by itself redefine ontology, ownership, or mature doctrine | `official/pdf/L4_Witness_Protocol_Normative_Draft_v0.2.pdf`<br>`hashes/SHA256SUMS_*.txt` |
| `P06` | Corpus control surface | `6` | route reading, lock state, stabilize terminology, map claims/status, classify intake, define bounded audience bundles, and discipline sync/supersession/acceptance/assertion/ownership/invariants/precedence | replace the underlying doctrinal source or create new doctrine by summary | `CORPUS_PRIMER.json`<br>`STACK_LOCK_2026-04-12.json`<br>`CLAIMS_AND_EVIDENCE_MAP.md`<br>`PRECEDENCE_AND_RESOLUTION.md`<br>`PACKAGE_INTAKE_AND_INTEGRATION.md`<br>`AUDIENCE_PROFILES_AND_MINIMAL_READING_PATHS.md` |
| `P07` | Implementation / runtime proof surface | `7` | prove constrained buildability, operational closure, and feasibility under implementation conditions | by itself define ontology, mature doctrine, or canonical package ownership | `ester-clean-code/PROOF_OF_CLOSURE.md` |
| `P08` | Narrative companion surface | `8` | illuminate recognition, perception, and human-facing interpretation | override normative, evidence, or stronger doctrinal layers | `qubit-of-hope-volume-i/CORPUS_CONTEXT.md` |
| `P09` | Pointer / contextual repo-level surface | `9` | orient readers, hand off to canonical homes, and provide repo-local context | silently restate adjacent doctrine as local canon | `README.md`<br>`MACHINE_ENTRY.md`<br>`START_HERE.md` |
| `P10` | Historical retained surface | `10` | preserve citation history, retained drafts, and visible evolution trace | silently regain current primacy over an explicitly designated newer source | retained prior drafts<br>historical release surfaces |

## 4. Resolution rules

| Rule ID | Rule | What it means | Why it matters |
|---|---|---|---|
| `R-P1` | Primary artifact beats explanatory summary | If a summary, map, README, or companion diverges from the designated primary artifact, the primary artifact governs. | Prevents secondary explanation from becoming silent canon. |
| `R-P2` | Canonical owner beats adjacent restatement | When the same package is described in multiple repos, the canonical owner repo governs package meaning. | Prevents convenience duplication from turning into parallel doctrine. |
| `R-P3` | Stable core beats draft when they diverge | A draft may guide and matter, but it does not outrank stable mature core unless the corpus explicitly reclassifies it. | Prevents drift-by-implication from draft repetition. |
| `R-P4` | Evidence/witness surface verifies operational trace but does not redefine ontology by itself | Witness and verification can prove that something happened or was reviewable; they do not alone settle what the thing is. | Keeps audit evidence from silently becoming metaphysics. |
| `R-P5` | Control surfaces organize reading but do not replace doctrinal sources | Primers, locks, maps, intake policies, audience bundles, and other control surfaces tell readers how to navigate and classify the corpus; they do not replace the narrower artifact they point to. | Preserves routing and organizing surfaces as control surfaces rather than doctrine generators. |
| `R-P6` | Implementation surface proves possibility but does not by itself define mature doctrine | Runtime closure can show that constrained execution is possible; it does not alone settle ontology, ownership, or final normative authority. | Keeps implementation proof bounded to implementation proof. |
| `R-P7` | Narrative companion may illuminate recognition/perception but cannot override normative or evidence layers | The companion can clarify what readers perceive and recognize, but not overrule doctrine or witness surfaces. | Keeps the narrative bridge valid without letting it become silent replacement. |
| `R-P8` | Historical retained surface remains citable, but does not silently regain primacy over current designated primary | Older retained artifacts remain part of the trace and may still be cited historically, but current designated primary stays primary until explicitly changed. | Preserves history without reopening canon by accident. |

## 5. Fail-closed resolution rule

If two surfaces appear to conflict and precedence is unclear, prefer the stronger compatible source and mark the issue unresolved until corpus-level review.

## 6. Read next

- `CLAIMS_AND_EVIDENCE_MAP.md`
- `STATUS_AND_MATURITY_MAP.md`
- `CHANGE_CONTROL_AND_SYNC.md`
- `SUPERSESSION_AND_DEPRECATION.md`
- `CANONICAL_OWNERSHIP_AND_BOUNDARIES.md`
- `CROSS_LAYER_INVARIANTS_AND_CONTRADICTION_POLICY.md`
- `ASSERTION_STRENGTH_AND_BOUNDARIES.md`
- `ARTIFACT_ID_AND_REFERENCE_POLICY.md`
- `PACKAGE_INTAKE_AND_INTEGRATION.md`
- `AUDIENCE_PROFILES_AND_MINIMAL_READING_PATHS.md`
- `PUBLIC_HISTORY_ANNOTATION_AND_RELEASE_NOTE_POLICY.md`
- `PUBLIC_CORRECTION_AND_ERRATA_POLICY.md`
