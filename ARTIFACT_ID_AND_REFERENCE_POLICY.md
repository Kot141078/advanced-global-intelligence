# Artifact ID and Reference Policy

## Purpose

This file fixes a compact corpus-level discipline for stable artifact identity. It helps maintainers, serious readers, reviewers, and machine readers refer to load-bearing artifacts by stable identifier rather than by path memory alone.
Use `PACKAGE_INTAKE_AND_INTEGRATION.md` when the open question is whether a candidate package should mint a new load-bearing artifact at all or remain pointer-only during intake.
Use `ATOMIC_PROMOTION_BUNDLES.md` when the open question is which coupled control surfaces should move together with an artifact-identity or supersession change.

## 1. Why this file exists

Paths and filenames may evolve; corpus-level reference discipline should not depend on path memory alone.

## 2. Core rule

Artifact ID is stable; path may change; canonical ownership and citation rules still apply.

## 3. ID format rule

- use compact human-readable IDs
- one stable ID per load-bearing artifact or surface
- prefer ID stability over path stability
- if an artifact is superseded, keep the old ID with explicit state instead of silently reusing it

## 4. Canonical artifact registry

| Artifact ID | Artifact | Repo | Current path | Artifact role | Reference state | Notes |
|---|---|---|---|---|---|---|
| `AID-001` | AGI main framing / manifesto-level core surface | `advanced-global-intelligence` | `README.md`<br>`MASTER_ENTRY.md` | corpus framing / public stack entry | `current` | framing identity survives local entry polish |
| `AID-002` | `c = a + b` / `L4` protocol surface | `advanced-global-intelligence` | `protocols/c_a_b_protocol_v1.1_L4_EN.md` | ontology + feasibility protocol surface | `current` | path drift must not break core-formula reference |
| `AID-003` | Theoretical Foundations of the AGI Ecosystem | `advanced-global-intelligence` | `manifesto/Theoretical_Foundations_of_the_AGI_Ecosystem_EN.md` | ecosystem theoretical synthesis | `current` | synthesis artifact, not control surface |
| `AID-004` | SER v1.3 core | `sovereign-entity-recursion` | `protocol/SER_v1.3_EN.md` | stable doctrinal core | `current` | stable core identity independent of repo-local restatement |
| `AID-005` | SER-FED v0.2 RFC | `sovereign-entity-recursion` | `protocol/ser-fed/SER-FED_v0.2_RFC_EN.md` | draft federation normative surface | `current` | draft state does not change artifact identity |
| `AID-006` | L4 Witness Protocol v0.2 | `advanced-global-intelligence` | `official/pdf/L4_Witness_Protocol_Normative_Draft_v0.2.pdf` | witness / verification artifact | `current` | evidence-layer artifact, not ontology source by itself |
| `AID-007` | Continuity Bundle JSON Schema v0.1 | `advanced-global-intelligence` | `protocols/continuity-bundle/Continuity_Bundle_JSON_Schema_v0.1.md` | continuity schema artifact | `current` | schema identity survives path cleanup |
| `AID-008` | Cold Wake Checklist v0.1 | `advanced-global-intelligence` | `protocols/continuity-bundle/Cold_Wake_Checklist_v0.1.md` | continuity recovery checklist | `current` | checklist path may move without becoming a new artifact |
| `AID-009` | Pre-Lineage Boundary Note v0.1 | `advanced-global-intelligence` | `manifesto/Pre_Lineage_Boundary_Note_v0.1.md` | reserved-territory boundary artifact | `current` | reserved territory still has stable reference identity |
| `AID-010` | Economic Layer core surface | `advanced-global-intelligence` | `docs/economic-layer/Economic_Layer_for_Experience_Artifacts_v0.1.md` | EA economic normative surface | `current` | bounded draft identity, not market index |
| `AID-011` | `ester-clean-code` / `PROOF_OF_CLOSURE` | `ester-clean-code` | `PROOF_OF_CLOSURE.md` | runtime proof-of-possibility surface | `current` | runtime proof gets stable reference without becoming doctrine |
| `AID-012` | `qubit-of-hope-volume-i` / `CORPUS_CONTEXT` | `qubit-of-hope-volume-i` | `CORPUS_CONTEXT.md` | narrative companion corpus context | `companion` | companion identity is stable without becoming normative core |
| `AID-013` | `CORPUS_PRIMER` | `advanced-global-intelligence` | `CORPUS_PRIMER.json` | machine-first corpus routing surface | `control-surface` | artifact ID != claim ID |
| `AID-014` | `STACK_LOCK_2026-04-12` | `advanced-global-intelligence` | `STACK_LOCK_2026-04-12.json` | frozen reading / lock surface | `control-surface` | lock identity remains stable even if later locks appear |
| `AID-015` | `CANONICAL_DISTINCTIONS` | `advanced-global-intelligence` | `CANONICAL_DISTINCTIONS.md` | anti-confusion surface | `control-surface` | distinction file is not package ownership map |
| `AID-016` | `OBJECTIONS_AND_REPLIES` | `advanced-global-intelligence` | `OBJECTIONS_AND_REPLIES.md` | public reasoning surface | `control-surface` | objections surface does not replace primary artifacts |
| `AID-017` | `CITATION_AND_VERIFICATION` | `advanced-global-intelligence` | `CITATION_AND_VERIFICATION.md` | citation / verification surface | `control-surface` | citation discipline is not artifact registry by itself |
| `AID-018` | `CLAIMS_AND_EVIDENCE_MAP` | `advanced-global-intelligence` | `CLAIMS_AND_EVIDENCE_MAP.md` | claim-to-artifact crosswalk | `control-surface` | claim map routes to artifact; it is not the artifact |
| `AID-019` | `STATUS_AND_MATURITY_MAP` | `advanced-global-intelligence` | `STATUS_AND_MATURITY_MAP.md` | status / maturity guidance | `control-surface` | artifact state != maturity class |
| `AID-020` | `CHANGE_CONTROL_AND_SYNC` | `advanced-global-intelligence` | `CHANGE_CONTROL_AND_SYNC.md` | sync / maintenance discipline | `control-surface` | sync discipline must check reference identity on path drift |
| `AID-021` | `SUPERSESSION_AND_DEPRECATION` | `advanced-global-intelligence` | `SUPERSESSION_AND_DEPRECATION.md` | supersession / retention discipline | `control-surface` | rename alone does not imply supersession |
| `AID-022` | `TERMINOLOGY_AND_ALIAS_POLICY` | `advanced-global-intelligence` | `TERMINOLOGY_AND_ALIAS_POLICY.md` | terminology lock surface | `control-surface` | alias drift must not masquerade as new artifact identity |
| `AID-023` | `ENTRY_ACCEPTANCE_AND_REGRESSION` | `advanced-global-intelligence` | `ENTRY_ACCEPTANCE_AND_REGRESSION.md` | entry acceptance discipline | `control-surface` | acceptance checks do not redefine artifact identity |
| `AID-024` | `ASSERTION_STRENGTH_AND_BOUNDARIES` | `advanced-global-intelligence` | `ASSERTION_STRENGTH_AND_BOUNDARIES.md` | claim-force discipline | `control-surface` | assertion class != artifact ID |
| `AID-025` | `CANONICAL_OWNERSHIP_AND_BOUNDARIES` | `advanced-global-intelligence` | `CANONICAL_OWNERSHIP_AND_BOUNDARIES.md` | ownership / package-home discipline | `control-surface` | ownership ID != artifact ID |
| `AID-026` | `CROSS_LAYER_INVARIANTS_AND_CONTRADICTION_POLICY` | `advanced-global-intelligence` | `CROSS_LAYER_INVARIANTS_AND_CONTRADICTION_POLICY.md` | invariant / contradiction discipline | `control-surface` | invariant break is different from path drift |
| `AID-027` | `PRECEDENCE_AND_RESOLUTION` | `advanced-global-intelligence` | `PRECEDENCE_AND_RESOLUTION.md` | precedence / resolution discipline | `control-surface` | precedence decides governing surface, not artifact registry state |
| `AID-028` | `PACKAGE_INTAKE_AND_INTEGRATION` | `advanced-global-intelligence` | `PACKAGE_INTAKE_AND_INTEGRATION.md` | package intake / integration discipline | `control-surface` | intake classification precedes wider routing and does not by itself create doctrine |

## 5. Rename / move / supersession rule

- path may update while the same artifact ID stays stable
- when path changes, review citation and claims/evidence surfaces
- old path references must not survive silently inside canonical surfaces
- artifact identity or supersession changes may widen the minimally coupled promotion bundle beyond the registry row itself
- superseded artifacts keep their ID and explicit state rather than vanishing by implication

## 6. Fail-closed reference rule

If maintainers cannot determine whether a path change preserves the same artifact identity, treat it as unresolved until the registry and affected canonical surfaces are reviewed.

## 7. Read next

- `CITATION_AND_VERIFICATION.md`
- `CLAIMS_AND_EVIDENCE_MAP.md`
- `CHANGE_CONTROL_AND_SYNC.md`
- `ATOMIC_PROMOTION_BUNDLES.md`
- `SUPERSESSION_AND_DEPRECATION.md`
- `CANONICAL_OWNERSHIP_AND_BOUNDARIES.md`
- `PRECEDENCE_AND_RESOLUTION.md`
- `PACKAGE_INTAKE_AND_INTEGRATION.md`
