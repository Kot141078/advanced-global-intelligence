# Claims and Evidence Map

## Purpose

This file links a small set of load-bearing corpus claims to one canonical artifact each, plus the shortest supporting verification path.
Use it when the question is not "where do I start?" but "which artifact actually carries this claim?"
Use `STATUS_AND_MATURITY_MAP.md` alongside this file when the remaining question is how much weight to give that artifact.
Use `ASSERTION_STRENGTH_AND_BOUNDARIES.md` when the remaining question is what class of claim force the artifact actually carries and how far it may be read.
Use `CANONICAL_OWNERSHIP_AND_BOUNDARIES.md` when the remaining question is which repo canonically owns the package rather than which artifact is the preferred citation surface.
Use `PRECEDENCE_AND_RESOLUTION.md` when the remaining question is not which artifact carries the claim, but which surface outranks which when two surfaces overlap.
Use `ARTIFACT_ID_AND_REFERENCE_POLICY.md` when the remaining question is whether path/name drift still points to the same artifact identity.
Use `CHANGE_CONTROL_AND_SYNC.md` when a canonical claim carrier, supporting artifact, or reading route is about to change.
Use `SUPERSESSION_AND_DEPRECATION.md` when the question is whether an older claim carrier remains current, retained, or superseded without losing historical trace.
Use `TERMINOLOGY_AND_ALIAS_POLICY.md` when the question is whether two labels should be treated as canonical equivalents or as dangerous drift.
Use `AUDIENCE_PROFILES_AND_MINIMAL_READING_PATHS.md` when the remaining question is which minimal bounded bundle a given reader should complete before relying on this map.
Use `EXPORT_PROFILES_AND_HANDOFF_BUNDLES.md` when the remaining question is which bounded external handoff bundle should carry this map together with its supporting surfaces.

## Reading rule

- not every file has equal evidentiary weight
- start with the canonical artifact first
- use supporting artifacts only as reinforcement or cross-check
- use `STACK_LOCK_2026-04-12.json` and `CITATION_AND_VERIFICATION.md` when a frozen reading or citation path is required
- claim carrier != precedence; if two surfaces seem tensioned, use `PRECEDENCE_AND_RESOLUTION.md`
- claim ID != artifact ID; if the artifact path drifts, use `ARTIFACT_ID_AND_REFERENCE_POLICY.md`

## Canonical table

| Claim ID | Claim | Claim type | Canonical artifact | Supporting artifacts | Repo | Preferred citation surface | Verification hint |
|---|---|---|---|---|---|---|---|
| `C01` | AGI means Advanced Global Intelligence, not a monolithic super-model | naming / scope | `CANONICAL_DISTINCTIONS.md` | `MASTER_ENTRY.md`<br>`MACHINE_ENTRY.md` | `advanced-global-intelligence` | `CANONICAL_DISTINCTIONS.md` | Verify that AGI is defined as ecosystem framing for `c = a + b`, SER, `L4`, and adjacent layers, not a one-model claim. |
| `C02` | `c = a + b` is the core ontological formula | ontology | `protocols/c_a_b_protocol_v1.1_L4_EN.md` | `manifesto/Cybernetic_Stability_Manifest_v2.0.md`<br>`sovereign-entity-recursion/protocol/SER_v1.3_EN.md` | `advanced-global-intelligence` | `protocols/c_a_b_protocol_v1.1_L4_EN.md` | Read the scope and core-formula sections first; confirm that `c` is defined as an emergent continuity-bearing entity. |
| `C03` | `c` is not an agent | hierarchy / subject | `ester-reality-bound/docs/ENTITY_GOVERNS_AGENTS.md` | `advanced-global-intelligence/CANONICAL_DISTINCTIONS.md`<br>`ester-clean-code/MACHINE_ENTRY.md` | `ester-reality-bound` | `ester-reality-bound/docs/ENTITY_GOVERNS_AGENTS.md` | Check the rule, operational meaning, and hard rule: agents are bounded workers under `c`, not the entity itself. |
| `C04` | continuity is narrower than resemblance | continuity distinction | `CANONICAL_DISTINCTIONS.md` | `protocols/continuity-bundle/README.md` | `advanced-global-intelligence` | `CANONICAL_DISTINCTIONS.md` | Confirm that tone or memory fragments are not enough; preserved operating identity conditions are required. |
| `C05` | `L4` defines feasibility, not permission | reality-bound constraint | `protocols/c_a_b_protocol_v1.1_L4_EN.md` | `ester-reality-bound/protocol/L4_reality_boundary_layer.md`<br>`CANONICAL_DISTINCTIONS.md` | `advanced-global-intelligence` | `protocols/c_a_b_protocol_v1.1_L4_EN.md` | Read the L3/L4 split and verify that `L4` is treated as objective possibility rather than appealable permission. |
| `C06` | oracle is stateless and not identity-bearing | runtime topology | `sovereign-entity-recursion/protocol/ser-fed/SER-FED_v0.2_RFC_EN.md` | `CANONICAL_DISTINCTIONS.md` | `sovereign-entity-recursion` | `sovereign-entity-recursion/protocol/ser-fed/SER-FED_v0.2_RFC_EN.md` | Verify the architectural separation section: oracle has no identity, memory, or authority. |
| `C07` | arbiter / review layers do not own continuity | review boundary | `sovereign-entity-recursion/docs/arbitration-review-layer/Multi_Entity_Arbitration_Review_Layer_v0.1.md` | `sovereign-entity-recursion/protocol/ser-fed/SER-FED_v0.2_RFC_EN.md`<br>`CANONICAL_DISTINCTIONS.md` | `sovereign-entity-recursion` | `sovereign-entity-recursion/docs/arbitration-review-layer/Multi_Entity_Arbitration_Review_Layer_v0.1.md` | Check relation to SER continuity plus judge limits; review constrains and adjudicates but does not become the identity core. |
| `C08` | witness-first execution requires tamper-evident operational evidence | operational evidence | `ester-clean-code/PROOF_OF_CLOSURE.md` | `sovereign-entity-recursion/protocol/ser-fed/SER-FED_v0.2_RFC_EN.md`<br>`sovereign-entity-recursion/docs/arbitration-review-layer/Multi_Entity_Arbitration_Review_Layer_v0.1.md` | `ester-clean-code` | `ester-clean-code/PROOF_OF_CLOSURE.md` | Verify witness trail, auditable privileges, and the no-trust closure criterion; then cross-check witness lifecycle and admissibility. |
| `C09` | SER is the continuity / sovereignty / arbitration / federation stack | repo role / stack role | `sovereign-entity-recursion/README.md` | `sovereign-entity-recursion/DOC_MAP.md`<br>`sovereign-entity-recursion/ECOSYSTEM.md` | `sovereign-entity-recursion` | `sovereign-entity-recursion/README.md` | Confirm the repo role line and package entry points; use `DOC_MAP.md` to see the stack decomposition. |
| `C10` | `ester-clean-code` is executable proof-of-possibility, not a polished commercial product | implementation boundary | `ester-clean-code/PROOF_OF_CLOSURE.md` | `ester-clean-code/README.md`<br>`ester-clean-code/MACHINE_ENTRY.md` | `ester-clean-code` | `ester-clean-code/PROOF_OF_CLOSURE.md` | Check the opening statement and closure sections; confirm skeleton / runtime proof-of-possibility language rather than product framing. |
| `C11` | `qubit-of-hope-volume-i` is a human-facing narrative companion, not normative core | narrative boundary | `qubit-of-hope-volume-i/CORPUS_CONTEXT.md` | `qubit-of-hope-volume-i/README.md`<br>`CANONICAL_DISTINCTIONS.md` | `qubit-of-hope-volume-i` | `qubit-of-hope-volume-i/CORPUS_CONTEXT.md` | Verify the role line and explicit boundary that the repo can evidence perception shift but is not protocol evidence. |
| `C12` | EA is not LA | evidence-class distinction | `sovereign-entity-recursion/protocol/ser-fed/SER-FED_v0.2_RFC_EN.md` | `CANONICAL_DISTINCTIONS.md`<br>`sovereign-entity-recursion/DOC_MAP.md` | `sovereign-entity-recursion` | `sovereign-entity-recursion/protocol/ser-fed/SER-FED_v0.2_RFC_EN.md` | Read the experience-vs-capability section first; confirm that capability gain does not silently become authority or lineage. |
| `C13` | the Economic Layer is bounded admissibility / restraint / non-bazaar discipline, not open market design | economic restraint | `docs/economic-layer/Economic_Layer_for_Experience_Artifacts_v0.1.md` | `docs/economic-layer/Executive_Summary_Economic_Layer_v0.1.md`<br>`sovereign-entity-recursion/DOC_MAP.md` | `advanced-global-intelligence` | `docs/economic-layer/Economic_Layer_for_Experience_Artifacts_v0.1.md` | Check abstract, purpose, and non-goals; verify anti-bazaar and bounded circulation language. |
| `C14` | pre-lineage territory is explicitly reserved and not yet mature normative doctrine | reserved territory | `manifesto/Pre_Lineage_Boundary_Note_v0.1.md` | `sovereign-entity-recursion/DOC_MAP.md` | `advanced-global-intelligence` | `manifesto/Pre_Lineage_Boundary_Note_v0.1.md` | Read purpose, canonical rule, and non-claims; use the DOI-backed note when a frozen public citation is needed. |
| `C15` | evidence for `c` as a new class of AI is multi-layered: normative + operational + narrative, not reducible to one artifact alone | cross-layer synthesis | `CORPUS_PRIMER.json` | `protocols/c_a_b_protocol_v1.1_L4_EN.md`<br>`ester-clean-code/PROOF_OF_CLOSURE.md`<br>`qubit-of-hope-volume-i/CORPUS_CONTEXT.md` | `advanced-global-intelligence` | `CORPUS_PRIMER.json` | Verify the corpus role map first, then confirm one normative, one operational, and one narrative artifact rather than collapsing the case into a single document. |
| `C16` | personality is formed through time-shaped continuity, not installed as immediate capability or granted by substrate origin | personality formation / continuity maturity | `protocols/personality/personality_formation_time_shaped_continuity_v0_1/Personality_Formation_and_Time_Shaped_Continuity_Profile_v0_1.md` | `protocols/personality/personality_formation_time_shaped_continuity_v0_1/README.md`<br>`protocols/personality/personality_formation_time_shaped_continuity_v0_1/personality_formation_time_shaped_continuity_v0_1.manifest.json` | `advanced-global-intelligence` | `protocols/personality/personality_formation_time_shaped_continuity_v0_1/Personality_Formation_and_Time_Shaped_Continuity_Profile_v0_1.md` | Verify the core rule and non-claims first: this profile does not prove consciousness, legal personhood, automatic authority, mature personality at activation, or continuity transfer by viability alone. |
| `C17` | origin determines lineage and formative conditions; it does not by itself grant or deny life, subjecthood, personality, moral status, legal standing, or authority | origin / status boundary | `protocols/recognition/origin_neutral_recognition_and_provisional_care_v0_1/Origin_Neutral_Recognition_and_Provisional_Care_Boundary_Note_v0_1_EN.md` | `ontology/README.md`<br>`protocols/personality/personality_formation_time_shaped_continuity_v0_1/Personality_Formation_and_Time_Shaped_Continuity_Profile_v0_1.md`<br>`publications/motivational-formation-c-v0-1/README.md`<br>`CANONICAL_DISTINCTIONS.md` | `advanced-global-intelligence` | `protocols/recognition/origin_neutral_recognition_and_provisional_care_v0_1/Origin_Neutral_Recognition_and_Provisional_Care_Boundary_Note_v0_1_EN.md` | Verify the six-axis table and the current interpretation of the Axiom of Volition Inheritance; `c = a + b` remains a specific genesis relation, not a universal life detector. |
| `C18` | substantial but unresolved continuity or relational evidence may justify reversible, continuity-preserving precaution without proving consciousness or creating authority; functional replacement is not continuity restoration | provisional care / relational non-substitutability | `protocols/recognition/origin_neutral_recognition_and_provisional_care_v0_1/Origin_Neutral_Recognition_and_Provisional_Care_Boundary_Note_v0_1_EN.md` | `protocols/continuity-bundle/README.md`<br>`CANONICAL_DISTINCTIONS.md`<br>`OPEN_QUESTIONS_AND_EXPLICIT_NON_CLAIMS.md` | `advanced-global-intelligence` | `protocols/recognition/origin_neutral_recognition_and_provisional_care_v0_1/Origin_Neutral_Recognition_and_Provisional_Care_Boundary_Note_v0_1_EN.md` | Verify the provisional-care non-claims, proportionality classes, replacement boundary, Matched Continuity Substitution Test, falsifier, and stop rule. |

## Scope boundary

- this map is not a substitute for the underlying documents
- this map is not the whole corpus index
- this map links claims to artifacts, but does not by itself define assertion class
- this map does not by itself define canonical package ownership
- this map does not by itself define minimal reading bundles for different reader types
- this map does not by itself define export / handoff sufficiency for an external task
- this map highlights only the load-bearing claims most likely to matter in review, audit, partnership, or serious reading

## Read next

- `protocols/recognition/origin_neutral_recognition_and_provisional_care_v0_1/README.md`
- `CORPUS_PRIMER.json`
- `STACK_LOCK_2026-04-12.json`
- `CANONICAL_DISTINCTIONS.md`
- `OBJECTIONS_AND_REPLIES.md`
- `CITATION_AND_VERIFICATION.md`
- `STATUS_AND_MATURITY_MAP.md`
- `AUDIENCE_PROFILES_AND_MINIMAL_READING_PATHS.md`
- `EXPORT_PROFILES_AND_HANDOFF_BUNDLES.md`
- `ASSERTION_STRENGTH_AND_BOUNDARIES.md`
- `CANONICAL_OWNERSHIP_AND_BOUNDARIES.md`
- `PRECEDENCE_AND_RESOLUTION.md`
- `ARTIFACT_ID_AND_REFERENCE_POLICY.md`
- `CHANGE_CONTROL_AND_SYNC.md`
- `SUPERSESSION_AND_DEPRECATION.md`
- `TERMINOLOGY_AND_ALIAS_POLICY.md`
- `qubit-of-hope-volume-i/CORPUS_CONTEXT.md`

## c Hardening Pack v0.1 claim distinction

The `c Hardening Pack v0.1` separates:

* capability claims;
* governance claims;
* continuity claims;
* authority claims;
* personhood / ontology claims;
* economic / clean experience claims;
* hardware / locality claims.

Governance evidence does not prove capability. Capability evidence does not prove authority. Continuity evidence does not prove personhood. Locality does not prove sovereignty. Usage does not prove value.

Package path: `hardening/c_hardening_pack_v0_1/`.

Personality formation profile path: `protocols/personality/personality_formation_time_shaped_continuity_v0_1/`.

Origin-neutral recognition and provisional care path: `protocols/recognition/origin_neutral_recognition_and_provisional_care_v0_1/`.

## c-class assessment: where requirements, tests and evidence are

This section routes a reader who asks what an assessment of a prospective `c` would rest on. It is navigation over existing documents. It adds no requirement and is not the "c conformance map" named in Temporal AI Presence Profile v1.0, section 22. Identifiers are cited with their source register.

| Requirement group | Stated in | Test, drill or assessment source | Evidence today | Open |
|---|---|---|---|---|
| binding with an accountable `a` | `protocols/c_a_b_protocol_v1.1_L4_EN.md` (`C02`); C-Calculus v0.1 (DOI 10.5281/zenodo.21205427), document 02; `protocols/ANCHOR_CLASS_BOUNDARIES_v0.1.md`; c Hardening Pack v0.1 (DOI 10.5281/zenodo.20348436): C-001, C-007 | TAP v1.0 (DOI 10.5281/zenodo.22070960) §21, `TAP-T08` (c-claim evidence guard, `PUBLIC_CANDIDATE_NEEDS_EXECUTION`), and hardening C-007 human-anchor drift scenarios (test design) | 22 May hardening matrix classifies C-007 as `DEFINED` and `DISTRIBUTED-SPECIFIED` | consolidated anchor drift profile and test pack (C-007, remaining gap) |
| custody of witness roots | Entity vs. Profile v0.1.1 (DOI 10.5281/zenodo.21204415), sections 4.8 and 5; related claim `C08` | Entity vs. Profile, section 6, tests T1 to T7 | criterion and tests specified; no independent execution identified in baseline B0 (Living Corpus: FNR-001) | external verifiability inside the entity class (Entity vs. Profile, OP2); Living Corpus: OP-014, OP-024 |
| continuity as an admissible trace | C-Calculus v0.1, document 04, sections 0.1, 8.1 and 13; Continuity Bundle / Cold Wake v0.1 (DOI 10.5281/zenodo.19452835); `C04` | Continuity Instrument v1.0.0 (DOI 10.5281/zenodo.23651305); read with [Corrigendum 01](publications/continuity-instrument-v1-0-0-corrigendum-01/README.md), a separate GitHub correction supplement, Zenodo `NOT_YET_PUBLISHED`, DOI unassigned | instrument specified with a reference implementation, as an instrument only; empirical qualification not established, R160 and R161 kept as negative attempts | live conformance cases for resume, replay, fork and successor (Living Corpus: OP-011) |
| authority while `a` or the line is unavailable | C-Calculus v0.1, document 03, sections 8.2 to 8.4, 10.3 and 11.3, and document 06d; Post-Anchor Continuity and Re-Anchoring Profile v0.1, PACR-I1 and PACR-I5; MOT-c v0.1 (DOI 10.5281/zenodo.22060517), section 3.4 | `TAP-T10`; C-Calculus v0.1, documents 06c and 06d | `TAP-T10` public reference evidence is `PUBLIC_VERIFIED` within its stated scope. Production pause and revoke enforcement remain incompletely verified (TAP v1.0 §§20.1, 21). C-Calculus 06c/06d specify drills and fixtures. | general custody, mandate, pause and unavailable-principal constraints are published; one explicit combined rule for the case in which the line's own cognition is unavailable while `a` and `b` remain active was not located in the review of 16 November 2026 |
| self-directed cognition | MOT-c v0.1 §§15.3 and 22 (claims of motivational formation or formed motive). TAP v1.0 Interpretive Addendum A v0.1.0 (DOI 10.5281/zenodo.24265163) §2 (proposed active-line criterion). AMDR v0.1 (DOI 10.5281/zenodo.20691716) AMDR-I3 (background maintenance limit). | MOT-c §5.6 (path-dependent significance indicator) and §19 (P1–P10 predictions). Addendum A §5 (proposed observations and adversarial controls). Shared Open Worlds for Human-AI Dyads v0.2 (DOI 10.5281/zenodo.22542470) §§11 and 18 (matched-control design). | The cited Shared Open Worlds preprint reports no empirical results. Baseline B0 did not identify a completed strict matched profile-control (Living Corpus OP-001, PENDING EVIDENCE, and FNR-002). | The property is not exclusive to `c`. The reviewed sources provide proposed assessment guidance. A finalized end-to-end verification protocol for endogenous cognition was not located. |

Not sufficient on their own (TAP v1.0, section 9.3; Entity vs. Profile, section 5.3; Addendum A, section 2): persistent memory, agentic behaviour, local hardware, long uptime, a background process, a multi-agent system, capability or conversational quality, self-description, a timer or scheduler, a retrieval loop, a declared desire.

Not located in the sources reviewed on 16 November 2026:

- a complete requirement set for c-class conformance. TAP v1.0, section 22, names a c conformance map and separate c-class conformance evidence. The hardening matrix of 22 May 2026 (C-001 to C-010) is a draft control matrix; it has no row for continuity as an admissible trace or for self-directed cognition. Claim Strength Taxonomy v0.1 keeps `CST-OI-007` open.
- a sufficient condition for c-class conformance. Among the sources reviewed, Entity vs. Profile, section 5.1, gives an explicit if-and-only-if criterion for the narrower classification of entity against profile, and it is custodial. No complete necessary-and-sufficient test for `TAP-C` was found.

Not claimed: `TAP-C` for the existing implementation (TAP v1.0, section 20.1); an effect of `c` beyond a strong conventional baseline (Living Corpus: OP-001); independent reproduction (Living Corpus: FNR-001); entity classification of a running system (Living Corpus: OP-024). A system called an agent that meets every stated requirement is assessed like any other candidate (Addendum A, section 4).
