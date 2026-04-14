# Package Intake and Integration

## Purpose

This file fixes a compact corpus-level intake discipline for new packages, layers, bundles, repos, and corpus-control surfaces before they enter corpus-visible routing.
Use `CHANGE_CONTROL_AND_SYNC.md` when intake has already become a live cross-repo sync task.
Use `CANONICAL_OWNERSHIP_AND_BOUNDARIES.md` when the remaining question is where the package canonically lives.
Use `ARTIFACT_ID_AND_REFERENCE_POLICY.md` when intake may require a new stable artifact identity or may only describe a path-stable restatement.
Use `PUBLIC_SAFE_BOUNDARY_AND_EXCLUSION_POLICY.md` when the first question is whether candidate material is public-safe, pointer-only, or excluded before intake can proceed.
Use `ENTRY_ACCEPTANCE_AND_REGRESSION.md` when the package is already entering entry surfaces and the question is whether discoverability and boundary clarity still hold.
Use `PRECEDENCE_AND_RESOLUTION.md` when the package already exists but the governing source is unclear.
Use `AUDIENCE_PROFILES_AND_MINIMAL_READING_PATHS.md` when a newly admitted package may change which bounded bundle a given audience should read first.
Use `OPEN_QUESTIONS_AND_EXPLICIT_NON_CLAIMS.md` when the candidate touches territory the corpus has deliberately kept open or explicitly non-claimed.

## 1. Why this file exists

New package language often appears before ownership, status, citation posture, and corpus role are fixed.
Without explicit intake, a local note can start behaving like silent canon.

## 2. Core rule

No new package, layer, bundle, repo-level addition, or corpus-control artifact should enter corpus-visible routing until owner, scope, status, reference posture, and public-safe boundary class are classified.

## 3. Intake classes

| Intake ID | Intake class | What it is | Minimum required surfaces | Typical repo home | Common failure mode |
|---|---|---|---|---|---|
| `N01` | new doctrinal / normative package | a new package that may carry primary or stable normative meaning | `CANONICAL_OWNERSHIP_AND_BOUNDARIES.md`; `STATUS_AND_MATURITY_MAP.md`; `CLAIMS_AND_EVIDENCE_MAP.md`; `PRECEDENCE_AND_RESOLUTION.md` | `advanced-global-intelligence` or `sovereign-entity-recursion` | local framing text starts sounding like mature doctrine before owner, status, and precedence are fixed |
| `N02` | new draft normative package | a serious draft package that may later mature but is not yet stable core | `STATUS_AND_MATURITY_MAP.md`; `CLAIMS_AND_EVIDENCE_MAP.md`; `SUPERSESSION_AND_DEPRECATION.md`; `PRECEDENCE_AND_RESOLUTION.md` | `advanced-global-intelligence`; `sovereign-entity-recursion`; `ester-reality-bound` | draft wording quietly inflates into stable core by repetition or adjacency |
| `N03` | new observed protocol / practice-derived package | a package that records observed recurrent practice or protocol shape rather than mature doctrine | `STATUS_AND_MATURITY_MAP.md`; `ASSERTION_STRENGTH_AND_BOUNDARIES.md`; `PRECEDENCE_AND_RESOLUTION.md` | `ester-reality-bound` or adjacent operational surface | practice note gets misread as universal normative rule |
| `N04` | new evidence / witness / verification package | a package centered on verification, witness, auditability, manifests, or replayable evidence | `CITATION_AND_VERIFICATION.md`; `CLAIMS_AND_EVIDENCE_MAP.md`; `ARTIFACT_ID_AND_REFERENCE_POLICY.md`; `PRECEDENCE_AND_RESOLUTION.md` | `advanced-global-intelligence` or `ester-reality-bound` | verification surface starts acting like ontology or ownership source by itself |
| `N05` | new runtime / implementation-facing package | a package that proves buildability, execution constraints, or implementation closure | `CANONICAL_OWNERSHIP_AND_BOUNDARIES.md`; `STATUS_AND_MATURITY_MAP.md`; `PRECEDENCE_AND_RESOLUTION.md`; `ENTRY_ACCEPTANCE_AND_REGRESSION.md` | `ester-clean-code` | implementation convenience silently becomes doctrinal ownership |
| `N06` | new companion / narrative / human-facing package | a package whose role is recognition, narrative bridge, or human-facing context | `STATUS_AND_MATURITY_MAP.md`; `ASSERTION_STRENGTH_AND_BOUNDARIES.md`; `ENTRY_ACCEPTANCE_AND_REGRESSION.md`; `PRECEDENCE_AND_RESOLUTION.md` | `qubit-of-hope-volume-i` | companion illumination starts reading like normative proof or witness evidence |
| `N07` | new corpus-control surface | a new primer, map, policy, lock, registry, or discipline file that organizes corpus reading | `CHANGE_CONTROL_AND_SYNC.md`; `ENTRY_ACCEPTANCE_AND_REGRESSION.md`; `ARTIFACT_ID_AND_REFERENCE_POLICY.md`; `PRECEDENCE_AND_RESOLUTION.md` | `advanced-global-intelligence` | a control surface starts creating doctrine instead of routing or classifying it |
| `N08` | new boundary note / reserved territory note | a bounded note marking incomplete, protected, or not-yet-settled territory | `STATUS_AND_MATURITY_MAP.md`; `SUPERSESSION_AND_DEPRECATION.md`; `ASSERTION_STRENGTH_AND_BOUNDARIES.md` | `advanced-global-intelligence` | incomplete territory is read as completed doctrine because reservation stayed implicit |
| `N09` | new extension / satellite clause set | an addendum, clause family, extension pack, or adjacent satellite surface | `CANONICAL_OWNERSHIP_AND_BOUNDARIES.md`; `CLAIMS_AND_EVIDENCE_MAP.md`; `SUPERSESSION_AND_DEPRECATION.md`; `PRECEDENCE_AND_RESOLUTION.md` | canonical owner repo of the parent package | extension text quietly forks the parent package into parallel canon |
| `N10` | new frozen public object / snapshot-backed package | a package whose public identity depends on tag, release, DOI, manifest, or frozen snapshot wording | `CITATION_AND_VERIFICATION.md`; `ARTIFACT_ID_AND_REFERENCE_POLICY.md`; `CHANGE_CONTROL_AND_SYNC.md`; `ENTRY_ACCEPTANCE_AND_REGRESSION.md` | canonical owner repo with release or DOI surface | moving repo and frozen public object get treated as interchangeable |

## 4. Minimal intake requirements

- declared role
- declared canonical home
- declared status / maturity
- citation / verification posture
- claims impact assessment
- artifact identity decision
- public-safe boundary classification
- open-question / explicit-non-claim interaction assessment
- discoverability decision
- ownership / pointer decision
- what-it-is-not line when confusion risk is non-trivial
- confirmation that the package does not silently outrank stronger existing sources

## 5. Canonical layers to check during intake

- `CORPUS_PRIMER.json`
- `STACK_LOCK_2026-04-12.json`
- `CLAIMS_AND_EVIDENCE_MAP.md`
- `STATUS_AND_MATURITY_MAP.md`
- `CANONICAL_OWNERSHIP_AND_BOUNDARIES.md`
- `ARTIFACT_ID_AND_REFERENCE_POLICY.md`
- `PUBLIC_SAFE_BOUNDARY_AND_EXCLUSION_POLICY.md`
- `CHANGE_CONTROL_AND_SYNC.md`
- `SUPERSESSION_AND_DEPRECATION.md`
- `ENTRY_ACCEPTANCE_AND_REGRESSION.md`
- `ASSERTION_STRENGTH_AND_BOUNDARIES.md`
- `OPEN_QUESTIONS_AND_EXPLICIT_NON_CLAIMS.md`
- `PRECEDENCE_AND_RESOLUTION.md`
- `AUDIENCE_PROFILES_AND_MINIMAL_READING_PATHS.md`

Not every new package updates every layer, but every intake must explicitly consider them.

## 6. Fail-closed intake rule

If maintainers cannot fix the package class, canonical home, claim impact, or public-safe boundary class,
the candidate should remain local or pointer-only until clarified and must not enter corpus-visible routing by implication.

## 7. Read next

- `CONTROL_LAYER_MINIMALITY_AND_DEDUPLICATION_POLICY.md`
- `CHANGE_CONTROL_AND_SYNC.md`
- `CANONICAL_OWNERSHIP_AND_BOUNDARIES.md`
- `STATUS_AND_MATURITY_MAP.md`
- `ARTIFACT_ID_AND_REFERENCE_POLICY.md`
- `PUBLIC_SAFE_BOUNDARY_AND_EXCLUSION_POLICY.md`
- `ENTRY_ACCEPTANCE_AND_REGRESSION.md`
- `PRECEDENCE_AND_RESOLUTION.md`
- `AUDIENCE_PROFILES_AND_MINIMAL_READING_PATHS.md`
- `OPEN_QUESTIONS_AND_EXPLICIT_NON_CLAIMS.md`
