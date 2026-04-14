# Terminology and Alias Policy

## Purpose

This file fixes a small corpus-level vocabulary lock for load-bearing public terms.
Use it when the question is not which artifact is primary, but which words are canonical, which aliases remain acceptable, and where semantic drift becomes dangerous.

## 1. Why this file exists

A multi-repo corpus drifts first through vocabulary before it drifts through doctrine.
If load-bearing terms start sliding across README, MACHINE_ENTRY, metadata, and package surfaces, control layers become noisy before formal claims visibly change.

## 2. Canonical term table

| Term ID | Canonical term | Allowed aliases | Avoid / do not collapse into | Short meaning | Why drift here is dangerous |
|---|---|---|---|---|---|
| `T001` | `AGI = Advanced Global Intelligence` | `Advanced Global Intelligence`; `AGI` with explicit clarification | mainstream monolithic AGI; one-model superintelligence | ecosystem framing for `c = a + b`, SER, `L4`, and adjacent layers | naming drift collapses the stack into a false one-model claim |
| `T002` | `c = long-lived digital entity / entity c` | `entity c`; `continuity-bearing entity`; ``c`` | `agent`; chatbot; single worker/model | the continuity-bearing accountable entity layer | if `c` drifts into agent-language, authority and continuity drift with it |
| `T003` | `a = human anchor` | `anchor`; `responsible human anchor` | review layer; operator pool; arbiter | the accountable human anchor in `c = a + b` | anchor drift breaks responsibility and boundary reading |
| `T004` | `b = technological substrate / machine cognitive layer` | `technological substrate`; `machine cognitive layer`; `procedures, models, and constraints` | `a`; `agent`; product shell | the bounded machine-side substrate in `c = a + b` | if `b` becomes vague, the formula stops saying what is actually bounded |
| `T005` | `agent` | `bounded agent`; `runtime agent`; `worker` | `c`; entity core; anchor | subordinate bounded process/tool under `c` | agent/entity collapse silently rewrites control and continuity |
| `T006` | `oracle` | `oracle process`; `oracle surface`; `stateless oracle` | identity-bearing node; continuity core; `c` | stateless advisory or inference surface | oracle drift can smuggle identity into a non-identity layer |
| `T007` | `arbiter / review layer` | `review layer`; `arbitration layer`; `arbiter` | owner of continuity; entity core; anchor | examination and authorization layer, not identity core | review drift can hide continuity ownership in an oversight surface |
| `T008` | `continuity` | `operating continuity`; `continuity of c` | resemblance; tone match; copy | preserved operating identity conditions of `c` | continuity drift can authorize privilege carry-over on similarity alone |
| `T009` | `resemblance / copy / duplicate` | `similarity`; `look-alike`; `copy` | continuity; preserved identity | similarity without continuity guarantee | copy-language drift can counterfeit identity claims |
| `T010` | `L4 / Reality Boundary Layer` | `L4`; `Reality Boundary Layer`; `reality-bound layer` | permission layer; `L3`; legal allowance | feasibility and bounded operation under real constraints | if `L4` drifts into permission-language, feasibility and governance get conflated |
| `T011` | `Witness / witness trail / evidence envelope` | `witness trail`; `evidence envelope`; `witness-backed record` | narrative claim; mere rhetoric; unreviewed log | reviewable evidence surface for promotion, challenge, and accountability | witness drift replaces evidence with story |
| `T012` | `EA / Experience Artifact` | `EA`; `Experience Artifact` | `LA`; lineage artifact; generic capability gain | experience-derived artifact class | EA/LA drift breaks provenance and admissibility boundaries |
| `T013` | `LA / Learning Abstract` | `LA`; `Learning Abstract` | `EA`; Experience Artifact | learning abstraction distinct from EA | LA/EA drift collapses separable evidence classes |
| `T014` | `narrative companion` | `human-facing companion`; `companion layer`; `narrative layer` | normative core; protocol evidence | the book-facing perception and recognition layer | companion drift can make narrative look like doctrine |
| `T015` | `runtime proof-of-possibility / executable skeleton` | `runtime proof-of-possibility`; `executable operational skeleton`; `clean-code skeleton` | commercial product; finished platform | operational closure layer in `ester-clean-code` | product-language drift overstates what the runtime layer is claiming |
| `T016` | `reserved territory` | `explicit non-mature boundary`; `reserved boundary territory` | mature doctrine; completed constitution; stable core | explicit boundary for not-yet-mature doctrine | reserved-language drift can prematurely harden blocked territory into norm |
| `T017` | `stable snapshot / frozen reading surface` | `stable snapshot`; `frozen reading surface`; `tagged snapshot`; `locked public object` | moving repo; default branch; live main | frozen public reading surface tied to a tag or locked ref | snapshot drift breaks citation and verification discipline |
| `T018` | `primary / retained / superseded / historical-only / companion / control-surface` | `supersession state`; `reading-preference state` | status/maturity labels; doctrinal weight labels | corpus preference and routing states under evolution | if these states drift into status/maturity language, preference becomes semantically noisy |

## 3. Controlled language notes

- use `entity` for `c` in corpus-facing prose when precision matters
- do not silently replace `c` with `agent`
- do not use `AGI` in the mainstream monolithic sense without explicit clarification
- use `narrative companion` for the book layer
- use `runtime proof-of-possibility` or `executable operational skeleton` for `ester-clean-code`
- use `reserved territory` only where explicit non-mature boundary is intended

## 4. Anti-drift rule

When a new file introduces a new alias for a load-bearing term,
maintainer should first check whether it is:

- equivalent
- narrower
- broader
- misleading

If unclear, prefer the canonical term.

When the wording question also affects corpus-level acceptance,
use `ENTRY_ACCEPTANCE_AND_REGRESSION.md` to decide whether the touched layer still passes the minimum control-layer standard.
When the wording question turns out to be about claim force rather than vocabulary, use `ASSERTION_STRENGTH_AND_BOUNDARIES.md` instead of inferring strength from wording alone.

## 5. Read next

- `CANONICAL_DISTINCTIONS.md`
- `OBJECTIONS_AND_REPLIES.md`
- `CLAIMS_AND_EVIDENCE_MAP.md`
- `STATUS_AND_MATURITY_MAP.md`
- `CHANGE_CONTROL_AND_SYNC.md`
- `SUPERSESSION_AND_DEPRECATION.md`
- `ENTRY_ACCEPTANCE_AND_REGRESSION.md`
- `ASSERTION_STRENGTH_AND_BOUNDARIES.md`
