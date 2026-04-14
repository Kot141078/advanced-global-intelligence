# Export Profiles and Handoff Bundles

## Purpose

This file fixes compact canonical export and handoff bundle profiles for bounded external sharing of the public corpus.
It helps maintainers, reviewers, and external evaluators distinguish a sufficient public-safe bundle from an overclaiming or underspecified handoff.
Use `LOCAL_TO_PUBLIC_PROMOTION_POLICY.md` when the question is not which bundle fits, but whether the touched state is ready for public-facing promotion at all.

## 1. Why this file exists

Public corpus sharing fails when either too much is handed out ad hoc,
or too little is handed out while pretending it is enough.
This file fixes bounded export profiles.

## 2. Core rule

A handoff bundle must be task-bounded, public-safe, and explicit about what it is enough for and what it is not.

## 3. Canonical export profile table

| Export ID | Profile | Primary use | Minimal bundle contents | Optional deepening | Enough for | Not enough for | Public-safe note |
|---|---|---|---|---|---|---|---|
| `XP01` | corpus orientation bundle | bounded first external orientation | `CORPUS_PRIMER.json`<br>`CANONICAL_DISTINCTIONS.md`<br>`CLAIMS_AND_EVIDENCE_MAP.md`<br>`STATUS_AND_MATURITY_MAP.md`<br>`PUBLIC_SAFE_BOUNDARY_AND_EXCLUSION_POLICY.md` | `MASTER_ENTRY.md`<br>`OBJECTIONS_AND_REPLIES.md`<br>`STACK_LOCK_2026-04-12.json` | first serious orientation, anti-confusion boundaries, claim overview, and public-safe scoping | doctrinal sign-off, audit review, or runtime judgment | contains only public-safe control surfaces and no private/runtime-sensitive material |
| `XP02` | research / theory bundle | bounded architecture and theory handoff | `MASTER_ENTRY.md`<br>`protocols/c_a_b_protocol_v1.1_L4_EN.md`<br>`sovereign-entity-recursion/protocol/SER_v1.3_EN.md`<br>`ester-reality-bound/protocol/L4_reality_boundary_layer.md`<br>`manifesto/Theoretical_Foundations_of_the_AGI_Ecosystem_EN.md` | `protocols/dea/README.md`<br>`protocols/ea-l4-eatp/README.md`<br>`CLAIMS_AND_EVIDENCE_MAP.md` | theoretical architecture review across AGI, SER, and `L4` | evidence/compliance sign-off, runtime closure review, or bounded partner scoping by itself | uses only public doctrinal and theoretical artifacts already published in the corpus |
| `XP03` | audit / evidence / compliance bundle | bounded audit-oriented external review | `CITATION_AND_VERIFICATION.md`<br>`CLAIMS_AND_EVIDENCE_MAP.md`<br>`STATUS_AND_MATURITY_MAP.md`<br>`STACK_LOCK_2026-04-12.json`<br>`official/pdf/L4_Witness_Protocol_Normative_Draft_v0.2.pdf`<br>`ester-clean-code/PROOF_OF_CLOSURE.md` | `sovereign-entity-recursion/protocol/SER_v1.3_EN.md`<br>`official/pdf/03_L4_WITNESS_FIELDS.pdf` | citable claim carriers, evidence posture, verification route, and frozen-reading discipline | whole-corpus philosophical understanding or companion interpretation | limited to public citable and verification-bearing artifacts; no private operational traces are included |
| `XP04` | runtime proof / implementation bundle | bounded runtime proof-of-possibility handoff | `CORPUS_PRIMER.json`<br>`ester-clean-code/MACHINE_ENTRY.md`<br>`ester-clean-code/PROOF_OF_CLOSURE.md`<br>`ester-reality-bound/protocol/L4_reality_boundary_layer.md`<br>`PUBLIC_SAFE_BOUNDARY_AND_EXCLUSION_POLICY.md` | `PRECEDENCE_AND_RESOLUTION.md`<br>`CANONICAL_OWNERSHIP_AND_BOUNDARIES.md`<br>`CLAIMS_AND_EVIDENCE_MAP.md` | runtime role clarity, closure evidence, and `L4` constraint context | doctrinal completeness, governance review, or whole-corpus authority claims | bounded to public skeleton and proof surfaces; it does not expose live runtime or unsafe code |
| `XP05` | maintainer / corpus-control bundle | bounded external handoff for maintainers, reviewers, or corpus stewards | `EXPORT_PROFILES_AND_HANDOFF_BUNDLES.md`<br>`CORPUS_PRIMER.json`<br>`STACK_LOCK_2026-04-12.json`<br>`PUBLIC_SAFE_BOUNDARY_AND_EXCLUSION_POLICY.md`<br>`PRECEDENCE_AND_RESOLUTION.md`<br>`PACKAGE_INTAKE_AND_INTEGRATION.md`<br>`CHANGE_CONTROL_AND_SYNC.md` | `ARTIFACT_ID_AND_REFERENCE_POLICY.md`<br>`ENTRY_ACCEPTANCE_AND_REGRESSION.md`<br>`CLAIMS_AND_EVIDENCE_MAP.md` | bounded corpus-routing, handoff selection, and control-layer review | creating new doctrine, bypassing primary artifacts, or reclassifying unsafe material by implication | consists only of public corpus-control surfaces and explicit boundary rules |
| `XP06` | narrative / human-recognition bundle | bounded companion-facing handoff | `qubit-of-hope-volume-i/CORPUS_CONTEXT.md`<br>`CORPUS_PRIMER.json`<br>`CANONICAL_DISTINCTIONS.md`<br>`OBJECTIONS_AND_REPLIES.md`<br>`STATUS_AND_MATURITY_MAP.md` | `CLAIMS_AND_EVIDENCE_MAP.md`<br>`MASTER_ENTRY.md` | companion-bounded human recognition, narrative role clarity, and anti-confusion context | normative verification, audit evidence, or runtime certification | uses only public companion and control surfaces and keeps the companion explicitly bounded |
| `XP07` | institutional evaluation / partner bundle | bounded partnership or institutional scoping handoff | `README.md`<br>`CLAIMS_AND_EVIDENCE_MAP.md`<br>`STATUS_AND_MATURITY_MAP.md`<br>`CITATION_AND_VERIFICATION.md`<br>`ester-clean-code/PROOF_OF_CLOSURE.md`<br>`PUBLIC_SAFE_BOUNDARY_AND_EXCLUSION_POLICY.md` | `MASTER_ENTRY.md`<br>`docs/economic-layer/README.md`<br>`sovereign-entity-recursion/README.md` | partnership scoping, maturity/evidence orientation, and proof-of-possibility context | full compliance sign-off, deep doctrinal arbitration, or whole-corpus philosophical completeness | all included artifacts are already public-safe and suitable for bounded public evaluation |
| `XP08` | skeptical / adversarial review bundle | bounded pressure-testing without straw interpretation | `CANONICAL_DISTINCTIONS.md`<br>`OBJECTIONS_AND_REPLIES.md`<br>`CLAIMS_AND_EVIDENCE_MAP.md`<br>`CITATION_AND_VERIFICATION.md`<br>`STATUS_AND_MATURITY_MAP.md`<br>`PRECEDENCE_AND_RESOLUTION.md`<br>`PUBLIC_SAFE_BOUNDARY_AND_EXCLUSION_POLICY.md` | `protocols/c_a_b_protocol_v1.1_L4_EN.md`<br>`sovereign-entity-recursion/protocol/SER_v1.3_EN.md`<br>`CROSS_LAYER_INVARIANTS_AND_CONTRADICTION_POLICY.md` | targeted skeptical review, objection routing, and non-straw challenge setup | replacing canonical reading order or declaring whole-corpus invalid without primary-artifact review | keeps criticism within public-safe control and doctrinal surfaces and excludes unsafe/off-limits domains |

## 4. Anti-overclaim notes

- an audience profile is a reading route; an export profile is a bounded handoff set
- bundle sufficiency is task-bounded, not doctrinal completeness
- an orientation bundle is not a doctrinal review bundle
- a runtime-proof bundle is not enough for full ontological or governance review
- a narrative bundle is not enough for normative verification
- an audit bundle is not enough for whole-corpus philosophical understanding
- a skeptic bundle is for pressure-testing, not for replacing canonical reading order
- a public-safe bundle is not the whole corpus by default
- a handoff bundle does not quietly include excluded or quarantined material
- export-ready bundle wording does not by itself make a local state public-facing committed history
- outward-ready handoff does not imply the whole corpus is fully settled

## 5. Handoff fail-closed rule

If maintainers cannot determine which export profile fits a request,
default to the smaller public-safe bundle and state the limit explicitly.

## 6. Read next

- `PUBLIC_SAFE_BOUNDARY_AND_EXCLUSION_POLICY.md`
- `AUDIENCE_PROFILES_AND_MINIMAL_READING_PATHS.md`
- `CITATION_AND_VERIFICATION.md`
- `CLAIMS_AND_EVIDENCE_MAP.md`
- `CANONICAL_OWNERSHIP_AND_BOUNDARIES.md`
- `LOCAL_TO_PUBLIC_PROMOTION_POLICY.md`
