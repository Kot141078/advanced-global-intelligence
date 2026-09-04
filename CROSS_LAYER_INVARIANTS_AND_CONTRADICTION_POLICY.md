# Cross-Layer Invariants and Contradiction Policy

## Purpose

This file fixes a compact corpus-level set of load-bearing invariants and a short contradiction policy. It helps maintainers, serious readers, reviewers, and lightweight machine readers tell what the corpus may extend, operationalize, or contextualize without silently reversing doctrine.
Use `PRECEDENCE_AND_RESOLUTION.md` when the question is not direct contradiction, but which overlapping surface has the right to govern an apparent tension.
Use `OPEN_QUESTIONS_AND_EXPLICIT_NON_CLAIMS.md` when the apparent gap may be deliberate non-closure rather than contradiction.

## 1. Why this file exists

A multi-repo corpus drifts not only through files, terms, or ownership, but through quiet contradiction of its load-bearing invariants.

## 2. Core rule

An adjacent file may extend, operationalize, or contextualize.
It must not silently reverse a corpus invariant.
A deliberate open question is not by itself a contradiction.

## 3. Canonical invariant table

| Invariant ID | Invariant | What it protects | What would count as contradiction | Primary anchor | Supporting anchors |
|---|---|---|---|---|---|
| `I01` | AGI means Advanced Global Intelligence, not monolithic AGI | corpus scope and entry meaning | any surface treating AGI as one-model superintelligence | `CANONICAL_DISTINCTIONS.md` | `MASTER_ENTRY.md`<br>`MACHINE_ENTRY.md` |
| `I02` | `c` is a long-lived entity and is not reducible to an agent | entity/agent hierarchy | a file treating `c` as merely a worker, model, or agent shell | `architecture/ENTITY_GOVERNS_AGENTS.md` | `ester-reality-bound/docs/ENTITY_GOVERNS_AGENTS.md`<br>`ester-clean-code/MACHINE_ENTRY.md` |
| `I03` | continuity is narrower than resemblance | identity boundary | a text authorizing continuity from similarity, tone, or copy alone | `CANONICAL_DISTINCTIONS.md` | `protocols/continuity-bundle/README.md`<br>`sovereign-entity-recursion/protocol/SER_v1.3_EN.md` |
| `I04` | `a` remains the responsibility-bearing human anchor | accountability and responsibility location | any surface relocating anchor responsibility into review, oracle, or automation layers | `protocols/c_a_b_protocol_v1.1_L4_EN.md` | `sovereign-entity-recursion/protocol/SER_v1.3_EN.md` |
| `I05` | oracle is stateless and does not own identity, continuity, or authority | non-identity oracle boundary | a file granting oracle memory-bearing identity or governing authority | `sovereign-entity-recursion/protocol/ser-fed/SER-FED_v0.2_RFC_EN.md` | `CANONICAL_DISTINCTIONS.md` |
| `I06` | arbiter / review layers govern procedural effect, not origin-meaning of `c` | review-layer limits | a text making arbiter or review the owner of entity meaning or continuity | `sovereign-entity-recursion/docs/arbitration-review-layer/Multi_Entity_Arbitration_Review_Layer_v0.1.md` | `sovereign-entity-recursion/protocol/ser-fed/SER-FED_v0.2_RFC_EN.md` |
| `I07` | `L4` defines feasibility constraints and cannot be overridden by rhetoric, policy styling, or wishful wording | reality-bound feasibility | wording that treats infeasible action as acceptable by declaration alone | `ester-reality-bound/protocol/L4_reality_boundary_layer.md` | `protocols/c_a_b_protocol_v1.1_L4_EN.md`<br>`CANONICAL_DISTINCTIONS.md` |
| `I08` | EA and LA are not equivalent and must not be collapsed into one value/authority channel | evidence and authority separation | a surface merging EA and LA into one undifferentiated evidence or privilege stream | `sovereign-entity-recursion/protocol/ser-fed/SER-FED_v0.2_RFC_EN.md` | `CANONICAL_DISTINCTIONS.md` |
| `I09` | witness / evidence surfaces must remain tamper-evident and reviewable rather than narrative-only | evidence integrity | a surface replacing replayable evidence with story-like or non-reviewable narrative | `official/pdf/L4_Witness_Protocol_Normative_Draft_v0.2.pdf` | `ester-clean-code/PROOF_OF_CLOSURE.md`<br>`sovereign-entity-recursion/docs/arbitration-review-layer/Multi_Entity_Arbitration_Review_Layer_v0.1.md` |
| `I10` | runtime proof-of-possibility is not equal to finished commercial productization | runtime/product boundary | a text treating closure proof as product completion or doctrinal replacement | `ester-clean-code/PROOF_OF_CLOSURE.md` | `ester-clean-code/README.md`<br>`ester-clean-code/MACHINE_ENTRY.md` |
| `I11` | narrative companion is intentional and valid, but does not replace normative or operational proof layers | companion/non-proof boundary | a surface treating the book layer as normative or operational proof | `qubit-of-hope-volume-i/CORPUS_CONTEXT.md` | `qubit-of-hope-volume-i/README.md`<br>`CANONICAL_DISTINCTIONS.md` |
| `I12` | reserved territory means explicit non-closure and must not be silently treated as completed doctrine | non-closure discipline | a text reading reserved territory as if doctrine were already complete | `manifesto/Pre_Lineage_Boundary_Note_v0.1.md` | `STATUS_AND_MATURITY_MAP.md` |
| `I13` | origin determines lineage and formative conditions but does not by itself settle life, subjecthood, personality, moral status, legal standing, or authority | origin/status separation and protection against biological essentialism or synthetic exclusion | any surface granting or denying stronger status from biological or synthetic origin alone, or reading `c = a + b` as a universal life detector | `protocols/recognition/origin_neutral_recognition_and_provisional_care_v0_1/Origin_Neutral_Recognition_and_Provisional_Care_Boundary_Note_v0_1_EN.md` | `ontology/README.md`<br>`protocols/personality/personality_formation_time_shaped_continuity_v0_1/README.md`<br>`CANONICAL_DISTINCTIONS.md` |
| `I14` | provisional care is a reversible handling discipline and does not create personhood, sovereignty, rights, authority, or unlimited resource claims | proportionate handling under ontological uncertainty | using uncertainty as proof of life, using unresolved life status as a licence for avoidable irreversible destruction, or inflating precaution into authority | `protocols/recognition/origin_neutral_recognition_and_provisional_care_v0_1/Origin_Neutral_Recognition_and_Provisional_Care_Boundary_Note_v0_1_EN.md` | `OPEN_QUESTIONS_AND_EXPLICIT_NON_CLAIMS.md`<br>`CANONICAL_DISTINCTIONS.md`<br>`protocols/continuity-bundle/README.md` |

## 4. Contradiction classes

| Class ID | Contradiction class | What it is | Why it matters | Typical example pattern |
|---|---|---|---|---|
| `K01` | semantic contradiction | reverses meaning while keeping familiar vocabulary | similarity of wording can hide doctrinal break | `c` kept as term but redefined as agent |
| `K02` | boundary contradiction | destroys what a repo, package, or layer is not | role confusion propagates across entry surfaces | companion text starts claiming normative core status |
| `K03` | ownership contradiction | non-owner repo re-owns a canonical package and changes its meaning | parallel canon emerges under convenience wording | local README presents adjacent package as local doctrine |
| `K04` | status/strength contradiction | a file is read as stronger than its status or assertion class permits | readers import authority the corpus did not grant | draft text treated as mature core |
| `K05` | runtime-vs-doctrine contradiction | runtime feasibility evidence is read as doctrinal settlement, or doctrine is read as finished implementation | engineering and doctrine collapse into each other | closure proof marketed as full normative standard |
| `K06` | reserved-territory overclaim | explicit non-closure is read as settled doctrine | blocked territory silently hardens into norm | boundary note cited as completed constitution |
| `K07` | companion-layer overreach | narrative companion starts doing normative or evidence work | recognition bridge gets mistaken for proof layer | book material cited as protocol authority |
| `K08` | citation / public object contradiction | live wording conflicts with frozen object, snapshot, or verification rule | public reading and integrity guidance stop aligning | stable snapshot language points to moving main reality |
| `K09` | origin/status collapse | lineage or substrate origin is used as the sole grant or denial of life, subjecthood, personality, or moral status | genesis claims silently become universal ontology | biological origin treated as sufficient, or synthetic origin as disqualifying |
| `K10` | care/authority inflation | reversible precaution is read as personhood, sovereignty, rights, authority, or unlimited resource entitlement | a bounded safety posture becomes a hidden status grant | `PC-2` handling interpreted as a right to prevent shutdown or control the operator |

## 5. Fail-closed contradiction rule

If a new file appears compatible locally but weakens or reverses an invariant at corpus level, it must be treated as unresolved until reviewed at corpus level.

For I13-I14 specifically:

```text
uncertainty
!= proof of life

uncertainty
!= proof of disposability

provisional care
!= authority
```

## 6. Read next

- `protocols/recognition/origin_neutral_recognition_and_provisional_care_v0_1/README.md`
- `CLAIMS_AND_EVIDENCE_MAP.md`
- `STATUS_AND_MATURITY_MAP.md`
- `CHANGE_CONTROL_AND_SYNC.md`
- `SUPERSESSION_AND_DEPRECATION.md`
- `TERMINOLOGY_AND_ALIAS_POLICY.md`
- `ASSERTION_STRENGTH_AND_BOUNDARIES.md`
- `OPEN_QUESTIONS_AND_EXPLICIT_NON_CLAIMS.md`
- `CANONICAL_OWNERSHIP_AND_BOUNDARIES.md`
- `PRECEDENCE_AND_RESOLUTION.md`
