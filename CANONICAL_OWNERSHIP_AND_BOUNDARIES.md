# Canonical Ownership and Boundaries

## Purpose

This file fixes a short corpus-level ownership map for packages, layers, and control surfaces. It tells maintainers, serious readers, reviewers, and lightweight machine readers where a thing canonically lives, what adjacent repos may do, and where dangerous duplication begins.
Use `CROSS_LAYER_INVARIANTS_AND_CONTRADICTION_POLICY.md` when ownership drift turns into an actual invariant break rather than a mere package-home question.
Use `PRECEDENCE_AND_RESOLUTION.md` when ownership is already known but the remaining question is which current surface actually governs.
Use `ARTIFACT_ID_AND_REFERENCE_POLICY.md` when ownership is stable but the path of the owned artifact may drift.
Use `PACKAGE_INTAKE_AND_INTEGRATION.md` when a new package or layer has not yet been classified strongly enough for ownership to be fixed.

## 1. Why this file exists

Multi-repo corpora drift first through duplicated explanations and blurred ownership.
This file fixes canonical home and boundary discipline.

## 2. Core rule

- one layer or package should have one canonical home
- adjacent repos may point, contextualize, or implement
- pointer is not ownership
- companion is not normative replacement
- duplication must not silently create parallel canon

## 3. Canonical ownership table

| Ownership ID | Layer / Package / Surface | Canonical home repo | Typical adjacent repos | Allowed non-owner role | Disallowed drift | Read next |
|---|---|---|---|---|---|---|
| `O01` | AGI ecosystem framing / corpus-level canonical entry | `advanced-global-intelligence` | `sovereign-entity-recursion`; `ester-reality-bound`; `ester-clean-code`; `qubit-of-hope-volume-i` | pointer; corpus-context mention; machine hop | another repo silently presenting itself as whole-corpus home | `MASTER_ENTRY.md` |
| `O02` | `c = a + b` / AGI core ontological framing | `advanced-global-intelligence` | `ester-reality-bound`; `sovereign-entity-recursion` | contextual restatement; interpretive clarification; implementation bridge | local convenience text forking the formula or relocating ontological ownership | `protocols/c_a_b_protocol_v1.1_L4_EN.md` |
| `O03` | `L4` / reality-bound operational layer | `ester-reality-bound` | `advanced-global-intelligence`; `sovereign-entity-recursion`; `ester-clean-code` | pointer; contextual framing; runtime dependency mention | AGI or clean-code silently becoming doctrinal owner of L4 operations | `protocol/L4_reality_boundary_layer.md` |
| `O04` | SER continuity / sovereignty / arbitration core | `sovereign-entity-recursion` | `advanced-global-intelligence`; `ester-reality-bound`; `ester-clean-code` | pointer; contextual mention; implementation dependency mention | adjacent repos presenting SER core as locally owned doctrine | `protocol/SER_v1.3_EN.md` |
| `O05` | SER-FED / federation layer | `sovereign-entity-recursion` | `advanced-global-intelligence`; `ester-reality-bound` | pointer; contextual mention; status note | adjacent repos restating SER-FED as independent local canon | `protocol/ser-fed/README.md` |
| `O06` | L4 Witness / evidence layer | `advanced-global-intelligence` | `ester-reality-bound`; `sovereign-entity-recursion`; `ester-clean-code` | pointer; verification support; operational use mention | evidence-layer use elsewhere re-owning witness doctrine | `official/pdf/L4_Witness_Protocol_Normative_Draft_v0.2.pdf` |
| `O07` | Continuity Bundle / Cold Wake continuity recovery surfaces | `advanced-global-intelligence` | `sovereign-entity-recursion`; `ester-clean-code` | pointer; implementation bridge; verification support | SER or clean-code silently re-owning continuity recovery package home | `protocols/continuity-bundle/README.md` |
| `O08` | Economic Layer for Experience Artifacts | `advanced-global-intelligence` | `sovereign-entity-recursion`; `ester-reality-bound` | pointer; contextual mention; downstream use mention | adjacent repo presenting EA economic layer as its local normative owner | `docs/economic-layer/README.md` |
| `O09` | ARL / EA conflict semantics / continuity precedence cluster | `sovereign-entity-recursion` | `advanced-global-intelligence`; `ester-reality-bound`; `ester-clean-code` | pointer; implementation bridge; contextual cross-reference | AGI or clean-code silently forking arbitration ownership or continuity precedence semantics | `docs/arbitration-review-layer/README.md` |
| `O10` | `ester-clean-code` executable skeleton / runtime proof-of-possibility | `ester-clean-code` | `advanced-global-intelligence`; `ester-reality-bound`; `sovereign-entity-recursion` | pointer; contextual mention; doctrinal dependency note | implementation repo being re-read as doctrinal owner of adjacent theory packages | `PROOF_OF_CLOSURE.md` |
| `O11` | `qubit-of-hope-volume-i` narrative companion / perception bridge | `qubit-of-hope-volume-i` | `advanced-global-intelligence`; `sovereign-entity-recursion`; `ester-reality-bound`; `ester-clean-code` | companion; contextual bridge; recognition support | companion surfaces silently re-owning normative core or evidence layers | `CORPUS_CONTEXT.md` |
| `O12` | corpus-control surfaces (`primer`, `stack lock`, `distinctions`, `objections`, `citation`, `claims`, `status`, `sync`, `supersession`, `terminology`, `acceptance`, `assertion`, `ownership`, `invariants`, `precedence`, `artifact-id`, `intake`) | `advanced-global-intelligence` | `sovereign-entity-recursion`; `ester-reality-bound`; `ester-clean-code`; `qubit-of-hope-volume-i` | pointer; repo-local convenience mention; machine hop | non-owner repo forking corpus-control canon through parallel local rule sets | `CORPUS_PRIMER.json` |

## 4. Boundary rules

- contextual mention is allowed
- canonical restatement must not silently fork meaning
- implementation-facing bridge is not canonical doctrinal ownership
- narrative illumination is not normative reassignment
- repo-local README convenience text must not redefine corpus-level ownership
- ownership drift is not automatically contradiction, but it can become contradiction when it reverses a load-bearing invariant
- ownership ID != artifact ID

## 5. Fail-closed ownership rule

If maintainers cannot determine whether a package is canonically owned here or elsewhere, treat the local file as pointer or context-only until ownership is clarified.

## 6. Read next

- `CONTROL_LAYER_MINIMALITY_AND_DEDUPLICATION_POLICY.md`
- `CORPUS_PRIMER.json`
- `CLAIMS_AND_EVIDENCE_MAP.md`
- `STATUS_AND_MATURITY_MAP.md`
- `CHANGE_CONTROL_AND_SYNC.md`
- `SUPERSESSION_AND_DEPRECATION.md`
- `PRECEDENCE_AND_RESOLUTION.md`
- `ARTIFACT_ID_AND_REFERENCE_POLICY.md`
- `PACKAGE_INTAKE_AND_INTEGRATION.md`
- `qubit-of-hope-volume-i/CORPUS_CONTEXT.md`
- `CROSS_LAYER_INVARIANTS_AND_CONTRADICTION_POLICY.md`
