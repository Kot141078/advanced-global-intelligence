# Assertion Strength and Boundaries

## Purpose

This file fixes a compact corpus-level vocabulary for claim force. It helps maintainers, serious readers, reviewers, and lightweight machine readers tell how far a statement should be read, what it does not license, and where overstatement begins.
Use `CROSS_LAYER_INVARIANTS_AND_CONTRADICTION_POLICY.md` when the question is not how strong a statement sounds, but whether a local variant now contradicts a load-bearing invariant.
Use `PRECEDENCE_AND_RESOLUTION.md` when the question is not claim force, but which current surface should govern an apparent overlap.
Use `OPEN_QUESTIONS_AND_EXPLICIT_NON_CLAIMS.md` when the ambiguity is not strength but whether the corpus has deliberately refused to close the territory.

## 1. Why this file exists

A multi-repo corpus can drift not only through files and terminology, but through overstatement and misreading of claim force.

## 2. Canonical assertion classes

| Class ID | Assertion class | What it means | What it does NOT mean | Typical artifact types | Reading boundary |
|---|---|---|---|---|---|
| `C-A1` | axiomatic / ontological claim | fixes an irreducible premise, entity model, or identity-bearing assumption the rest of the stack depends on | not a full protocol, procedure, or mature implementation standard | axioms, core formula notes, foundational ontological sections | read as a load-bearing premise; do not infer downstream procedures that the text does not state |
| `C-A2` | architectural core claim | fixes a structural relation, hierarchy, or stack-wide design rule that routes interpretation across repos | not every downstream clause, witness rule, or package detail is settled merely because the architecture is load-bearing | architecture notes, core framing surfaces, entity-governs-agents notes | read as stack structure and relation logic; do not silently upgrade it into complete doctrine |
| `C-A3` | operational rule / execution discipline | defines bounded execution, recovery, or handling logic for real operation under specified conditions | not a universal law, final ontology, or blanket permission claim | checklists, recovery logic, operator procedures, bounded execution rules | read as operational discipline within scope, not as unlimited theory or mature normative closure |
| `C-A4` | draft normative proposal | offers a serious normative proposal that may guide review and citation while remaining explicitly non-final | not stable mature core, not settled law of the corpus, not immunity from revision | RFCs, normative drafts, bounded draft clauses, active proposal packages | read as strong draft material with explicit revision risk |
| `C-A5` | observed protocol / practice-derived stability claim | records a protocol, pattern, or stability claim that is grounded in observed or practice-derived regularity | not a universal law and not a guarantee that every context behaves the same way | observed-protocol notes, practice-derived protocol descriptions, ecosystem regularity surfaces | read as evidence of recurrent behavior, not as total doctrine |
| `C-A6` | runtime proof-of-possibility claim | shows that a constrained operational form can be built, closed, and inspected in executable reality | not productization, not market readiness, and not a replacement for normative proof | runtime closure reports, executable skeleton proof surfaces, operational closure notes | read as feasibility evidence under constraints, not as finished platform doctrine |
| `C-A7` | evidence-layer / witness-verification claim | defines what can be witnessed, checked, replayed, challenged, or verified at the evidence layer | not a full ontological settlement and not automatic proof of every interpretation placed around it | witness protocols, evidence envelopes, verification paths, audit-facing evidence logic | read as a claim about reviewability and admissibility, not about every broader conclusion |
| `C-A8` | narrative / perception-shift claim | carries recognition, perception, and human-facing interpretive force that helps readers see what narrower protocol layers alone may not surface | not normative proof, not protocol evidence, and not doctrinal replacement | companion context, narrative bridge, perception-shift framing | read as companion illumination only; it can clarify recognition without replacing proof |
| `C-A9` | reserved-territory non-claim / explicit incompleteness | marks territory that is intentionally bounded, incomplete, or held open rather than closed into doctrine | not hidden completed doctrine, not weak mature norm, and not silent permission to fill gaps by inference | boundary notes, explicit non-claims, reserved-territory notes | read as deliberate non-closure; the safe reading is restraint rather than completion by guesswork |
| `C-A10` | control-layer / corpus-maintenance rule | constrains entry, citation, routing, sync, terminology, acceptance, or other corpus-control behavior | not primary doctrine and not a substitute for the artifact whose meaning it routes | primers, stack locks, sync rules, supersession rules, terminology policy, acceptance layers | read as reading-control and maintenance discipline, not as the underlying claim source itself |

## 3. Anti-overreach notes

- an axiom is not a full protocol
- a draft normative layer is not equivalent to stable mature core
- an observed protocol is not the same as a universal law
- runtime proof-of-possibility does not imply finished productization
- narrative companion may illuminate recognition and perception but does not replace normative proof
- reserved territory means explicit non-closure, not hidden completed doctrine
- open question or explicit non-claim does not authorize silent completion by inference

## 4. Minimal mapping examples

- `Axiom_of_Volition_Inheritance_v1.0.md` -> axiomatic / ontological claim
- `c = a + b` / AGI core framing -> architectural core claim
- Cold Wake / Continuity Bundle recovery logic -> operational rule / execution discipline or evidence-layer / witness-verification claim, depending on whether the question is handling or admissibility
- SER-FED / Economic Layer / EA clauses -> draft normative proposal unless a narrower canonical surface explicitly gives them stronger force
- EWCEP -> observed protocol / practice-derived stability claim
- `ester-clean-code/PROOF_OF_CLOSURE.md` -> runtime proof-of-possibility claim
- L4 Witness -> evidence-layer / witness-verification claim
- `qubit-of-hope-volume-i/CORPUS_CONTEXT.md` -> narrative / perception-shift claim
- `Pre_Lineage_Boundary_Note_v0.1.md` -> reserved-territory non-claim / explicit incompleteness
- primer / stack lock / sync / supersession / terminology / acceptance layers -> control-layer / corpus-maintenance rule

## 5. Fail-closed reading rule

If the claim force of a text is unclear, read it at the weaker compatible class until a more canonical surface clarifies otherwise.

## 6. Read next

- `CLAIMS_AND_EVIDENCE_MAP.md`
- `STATUS_AND_MATURITY_MAP.md`
- `CHANGE_CONTROL_AND_SYNC.md`
- `SUPERSESSION_AND_DEPRECATION.md`
- `TERMINOLOGY_AND_ALIAS_POLICY.md`
- `OPEN_QUESTIONS_AND_EXPLICIT_NON_CLAIMS.md`
- `qubit-of-hope-volume-i/CORPUS_CONTEXT.md`
- `CROSS_LAYER_INVARIANTS_AND_CONTRADICTION_POLICY.md`
- `PRECEDENCE_AND_RESOLUTION.md`
