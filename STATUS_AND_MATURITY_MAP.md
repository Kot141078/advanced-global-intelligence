# Status and Maturity Map

## Purpose

This file fixes the status, maturity, and reading weight of the main load-bearing public artifacts in the corpus.
Use it when the question is not "which artifact holds the claim?" but "how mature is this artifact and how much doctrinal weight should I give it?"
Use `ASSERTION_STRENGTH_AND_BOUNDARIES.md` when the question is claim force rather than maturity or doctrinal weight.
Use `OPEN_QUESTIONS_AND_EXPLICIT_NON_CLAIMS.md` when the question is whether the corpus has deliberately left the territory open rather than how mature the nearby artifact is.
Use `CANONICAL_OWNERSHIP_AND_BOUNDARIES.md` when the question is which repo canonically owns the package rather than how mature the artifact is.
Use `PRECEDENCE_AND_RESOLUTION.md` when the question is which surface should govern an apparent overlap rather than how mature a surface is.
Use `AUDIENCE_PROFILES_AND_MINIMAL_READING_PATHS.md` when the remaining question is which bounded reader bundle should be used before maturity judgments are summarized outward.

## Reading rule

- not all artifacts carry the same normative weight
- `stable` != `draft`
- status / maturity != assertion force
- ownership != status / maturity
- precedence != status / maturity
- audience profile != status / maturity
- narrative companion != normative core
- reserved territory != mature doctrine
- executable skeleton != commercial product

## Canonical table

| Artifact ID | Artifact / Package | Repo | Status label | Maturity class | Role | Normative weight | Recommended use | Anti-confusion note |
|---|---|---|---|---|---|---|---|---|
| `S01` | AGI core framing (`README.md` + `MASTER_ENTRY.md`) | `advanced-global-intelligence` | `control-surface` | `corpus control layer` | corpus framing / package boundaries / serious-entry routing | `strong supporting` | start here for corpus role, package boundaries, and reading order | framing surface is not a substitute for narrower protocol citation |
| `S02` | `c = a + b` / `L4` protocol surface (`protocols/c_a_b_protocol_v1.1_L4_EN.md` + `ester-reality-bound/protocol/L4_reality_boundary_layer.md`) | `advanced-global-intelligence / ester-reality-bound` | `draft` | `active draft` | core ontology + feasibility boundary surface | `explicitly non-final` | read early for entity model and L4 constraint logic | core protocol surface is load-bearing but not a frozen final standard |
| `S03` | `Theoretical_Foundations_of_the_AGI_Ecosystem_EN.md` | `advanced-global-intelligence` | `observed` | `review companion` | ecosystem-wide theoretical synthesis | `strong supporting` | use for high-level synthesis after AGI entry | synthesis clarifies the stack but does not replace narrower normative sources |
| `S04` | `SER_v1.3` core | `sovereign-entity-recursion` | `stable` | `mature core` | stable continuity / sovereignty core | `primary` | read first for hard continuity and sovereignty claims | stable SER core does not make every adjacent package stable |
| `S05` | `SER-FED_v0.2_RFC_EN.md` | `sovereign-entity-recursion` | `draft` | `active draft` | federation / anti-oligarchy normative layer | `explicitly non-final` | cite for the current federation model and bounded authority logic | draft federation layer is not `SER v2` and not the mature core |
| `S06` | `L4 Witness Protocol v0.2` (`official/pdf/L4_Witness_Protocol_Normative_Draft_v0.2.pdf` + `official/pdf/03_L4_WITNESS_FIELDS.pdf`) | `advanced-global-intelligence` | `draft` | `active draft` | challengeable reality-binding evidence layer | `explicitly non-final` | use for the current witness lifecycle, records, and evidence model | witness draft is load-bearing but not a stabilized final standard |
| `S07` | `Continuity_Bundle_JSON_Schema_v0.1.md` | `advanced-global-intelligence` | `operational` | `bounded draft` | machine-readable continuity / cold-wake schema | `bounded supporting` | use for bundle structure and cold-wake report shape | schema supports continuity evidence; it does not itself prove continuity |
| `S08` | `Cold_Wake_Checklist_v0.1.md` | `advanced-global-intelligence` | `operational` | `bounded draft` | operator checklist for bounded wake and classification | `bounded supporting` | use for recovery procedure, audit trace, and fail-closed wake discipline | checklist guides wake operations; it does not by itself certify identity or legality |
| `S09` | `Pre_Lineage_Boundary_Note_v0.1.md` | `advanced-global-intelligence` | `reserved` | `reserved territory` | explicit boundary for not-yet-mature lineage territory | `explicitly non-final` | read to understand blocked territory, restraint, and non-claims | reserved territory is part of the corpus, not mature lineage doctrine |
| `S10` | `Economic_Layer_for_Experience_Artifacts_v0.1.md` | `advanced-global-intelligence` | `draft` | `bounded draft` | EA admissibility / provenance / restraint layer | `explicitly non-final` | use for the current EA economic model and restraint logic | economic layer is not open-market design and not bazaar logic |
| `S11` | `PROOF_OF_CLOSURE.md` | `ester-clean-code` | `operational` | `runtime proof` | executable proof-of-possibility / closure evidence | `strong supporting` | use to inspect implementation closure, review paths, and operational evidence | runtime proof closes the loop operationally but does not replace normative core |
| `S12` | `CORPUS_CONTEXT.md` | `qubit-of-hope-volume-i` | `companion` | `narrative bridge` | human-facing narrative / perception bridge | `non-normative companion` | use for human recognition, perception shift, and companion context | narrative companion is intentional and important, but not protocol evidence |
| `S13` | `CORPUS_PRIMER.json` + `STACK_LOCK_2026-04-12.json` + entry-layer canonical surfaces | `advanced-global-intelligence` | `control-surface` | `corpus control layer` | machine-first routing, lock state, and aligned reading entry | `control / routing only` | use first to orient reading and freeze stack state | control surfaces route serious reading; they do not themselves create doctrine |
| `S14` | `CANONICAL_DISTINCTIONS.md` + `OBJECTIONS_AND_REPLIES.md` + `CITATION_AND_VERIFICATION.md` + `CLAIMS_AND_EVIDENCE_MAP.md` | `advanced-global-intelligence` | `control-surface` | `corpus control layer` | anti-confusion, public reasoning, citation discipline, and claim crosswalk | `strong supporting` | use before serious citation, review, or audit to stabilize meaning and claim routing | these surfaces discipline interpretation; they do not replace underlying protocol sources |

## Notes on interpretation

- stable core should be read first for hard claims
- draft normative layers can still be cited, but should not be confused with mature core
- observed artifacts can be architecture-bearing without becoming stabilized standards
- narrative companion is intentional and important, but is not a substitute for normative artifacts
- reserved territory belongs to the corpus, but is not a claim of completed doctrine
- open question or explicit non-claim does not become mature doctrine by adjacency
- if a status row materially changes, review `CHANGE_CONTROL_AND_SYNC.md` before updating entry, citation, or claims surfaces
- status / maturity does not by itself decide whether a surface is current primary, retained historical, or superseded; use `SUPERSESSION_AND_DEPRECATION.md` for that distinction
- status / maturity does not by itself decide whether a statement is axiomatic, architectural, operational, draft normative, observed, runtime, narrative, reserved, or control-layer; use `ASSERTION_STRENGTH_AND_BOUNDARIES.md` for that distinction
- status / maturity does not by itself reassign canonical home; use `CANONICAL_OWNERSHIP_AND_BOUNDARIES.md` for ownership questions
- status / maturity does not by itself resolve overlapping surfaces; use `PRECEDENCE_AND_RESOLUTION.md` for precedence questions
- status / maturity does not by itself define which minimal bundle a given audience should read first; use `AUDIENCE_PROFILES_AND_MINIMAL_READING_PATHS.md` for that question

## Read next

- `CORPUS_PRIMER.json`
- `STACK_LOCK_2026-04-12.json`
- `CANONICAL_DISTINCTIONS.md`
- `OBJECTIONS_AND_REPLIES.md`
- `CITATION_AND_VERIFICATION.md`
- `CLAIMS_AND_EVIDENCE_MAP.md`
- `AUDIENCE_PROFILES_AND_MINIMAL_READING_PATHS.md`
- `ASSERTION_STRENGTH_AND_BOUNDARIES.md`
- `OPEN_QUESTIONS_AND_EXPLICIT_NON_CLAIMS.md`
- `CANONICAL_OWNERSHIP_AND_BOUNDARIES.md`
- `PRECEDENCE_AND_RESOLUTION.md`
- `CHANGE_CONTROL_AND_SYNC.md`
- `SUPERSESSION_AND_DEPRECATION.md`
- `qubit-of-hope-volume-i/CORPUS_CONTEXT.md`
