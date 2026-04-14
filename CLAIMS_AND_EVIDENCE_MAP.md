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

## Scope boundary

- this map is not a substitute for the underlying documents
- this map is not the whole corpus index
- this map links claims to artifacts, but does not by itself define assertion class
- this map does not by itself define canonical package ownership
- this map does not by itself define minimal reading bundles for different reader types
- this map does not by itself define export / handoff sufficiency for an external task
- this map highlights only the load-bearing claims most likely to matter in review, audit, partnership, or serious reading

## Read next

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
