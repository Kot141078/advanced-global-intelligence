# Guardian Topology / ARL Matrix v0.1

## Child-facing guardian roles, dispute standing, minimal disclosure, freeze/quarantine routing, and lawful re-entry under CCDP

**Status:** Draft normative proposal (`C-A4`)
**Version:** v0.1
**Date:** 2026-05-13
**Language:** English
**Primary protocol:** `CCDP_v0_1_R_Corpus_Aligned.md`
**Related artifacts:** `CCDP_Traceability_Matrix_v0_1.md`, `CCDP_Threat_Model_v0_1.md`, `Child_Beacon_Extension_v0_1.md`
**Primary parent layers:** `c_a_b_protocol_v1.1_L4_EN.md`, `SER_v1.3`, `SER-FED`, `Beacon_Profile_v0.1_EN.md`, `AGL`, `ARL`, `ARQ/c[q]`, `L4 Witness`, `VXCX`, `EA-L4/EATP`, `Continuity Bundle`
**Primary subject:** `a_child`
**Primary entity:** `c_child`
**Primary boundary:** no single actor may become sovereign over a child-facing persistent AI entity.

---

## 0. Executive definition

**Guardian Topology / ARL Matrix (GTARL)** defines how guardian roles around `c_child` are composed, limited, challenged, frozen, reviewed, escalated, and re-entered.

It answers five operational questions:

1. **Who has standing?**
2. **What may they request?**
3. **What evidence is admissible?**
4. **When must a path be held, frozen, quarantined, or reviewed?**
5. **What may be disclosed, to whom, and under which risk state?**

Compact formula:

```text
Guardian Topology = plural bounded roles around c_child.
ARL Matrix        = procedural discipline when those roles conflict.
```

GTARL does **not** make the parent, school, vendor, state, Beacon, ARL, or `c_child` itself the sovereign authority over the child.

GTARL makes conflict **procedural**.

---

## 1. Corpus dependencies and precedence

GTARL is a child-specific matrix over existing corpus layers. It MUST NOT redefine them.

| Parent layer | GTARL dependency |
|---|---|
| `c = a + b` Protocol | `a_child` remains the human subject; `c_child` is a bounded emergent entity, not an owner of the child. |
| SER | `c_child` is a persistent entity variant, but developmentally constrained and guardianship-bound. |
| SER-FED | No single federation participant, school, vendor, guardian, or jurisdiction becomes a hidden sovereign. |
| Beacon Profile v0.1 | Recognition of continuity-bearing entities; GTARL does not redefine Beacon. |
| Child Beacon Extension v0.1 | Child-specific permission overlay over Beacon recognition; GTARL handles guardian standing and disputes around those permissions. |
| AGL | Source grounding must precede reliance, disclosure, review, or escalation. |
| ARL | Standing, evidence admissibility, freeze/hold/quarantine, review, outcome, appeal, and re-entry. |
| ARQ / `c[q]` | Ambiguity must not be prematurely collapsed into diagnosis, memory, disclosure, or authority. |
| L4 Witness | Significant state transitions must leave privacy-aware, tamper-evident witness records. |
| VXCX | Experience exchange without raw child life; capsules remain descriptive, privacy-flagged, and witness-bound. |
| EA-L4 / EATP | Learning does not imply authority; authority requires consequence-bearing, admissible, witness-linked experience. |
| Continuity Bundle / Cold Wake | Adult migration, fork, archive, sealed memory, and continuity recovery must be explicit. |
| Assertion Strength and Boundaries | GTARL is a draft child-specific normative proposal, not mature settled core. |
| Control Stack / Stop Rules | GTARL must not duplicate Beacon, AGL, ARL, L4 Witness, VXCX, or Continuity Bundle. |

### 1.1 Precedence rule

Where GTARL conflicts with ARL, ARL governs dispute procedure.

Where GTARL conflicts with Beacon, Beacon governs recognition semantics.

Where GTARL conflicts with CBE, CBE governs child-facing interaction permission overlay.

Where GTARL conflicts with AGL, AGL governs source grounding.

Where GTARL conflicts with L4 Witness, L4 Witness governs witness discipline.

Where GTARL defines a stricter child-specific restriction that does not contradict parent layers, the stricter child-specific restriction applies.

### 1.2 No new court rule

GTARL MUST NOT create a parallel court, parallel Beacon, parallel evidence doctrine, or parallel witness system.

It maps child guardian conflicts into existing ARL-compatible states and events.

---

## 2. Normative keywords

The keywords **MUST**, **MUST NOT**, **REQUIRED**, **SHALL**, **SHALL NOT**, **SHOULD**, **SHOULD NOT**, **MAY**, and **OPTIONAL** are used in their standard normative sense.

In this document:

- **MUST** indicates a requirement for GTARL conformance.
- **SHOULD** indicates a strong default that may be overridden only with explicit justification, ARL standing, and witnessable configuration.
- **MAY** indicates optional behavior bounded by parent-layer constraints.

---

## 3. Scope and non-goals

### 3.1 In scope

GTARL applies when any actor attempts to:

- change guardian topology around `c_child`;
- request child memory, transcript, sealed zone access, or state signal expansion;
- request educational, clinical, welfare, legal, vendor, peer, or external-agent access;
- challenge a `c_child` gateway decision;
- challenge a CBE child interaction mode;
- dispute a Red/Black escalation route;
- dispute memory promotion, deletion, sealing, or adult migration;
- connect a toy, robot, NPC, generated character, school system, external AI, or peer `c` to the child environment;
- override `c_child` refusal, silence, delay, quarantine, or disclosure limits.

### 3.2 Out of scope

GTARL does not define:

- legal custody law;
- family court procedure;
- criminal law or law-enforcement powers;
- medical or psychological diagnosis;
- school curriculum;
- product certification law;
- state child-protection statute;
- general web moderation;
- general AI ethics;
- general Beacon recognition;
- general ARL doctrine.

### 3.3 Non-claim

GTARL does not claim that a procedural matrix can solve all child-safety disputes.

GTARL claims that child-facing persistent AI systems must not handle guardian conflict through improvisation, fluency, hidden authority, or social force.

---

## 4. Core principles

### 4.1 No single sovereign guardian

`c_child` MUST NOT be governed by one party alone.

Not only parent.
Not only school.
Not only vendor.
Not only state.
Not only Beacon.
Not only ARL.
Not only `c_child`.
Not only `a_child` before full autonomy.

Child safety requires **plural bounded guardianship**.

### 4.2 Parent is guardian, not owner

The parent or legal guardian holds special responsibility and strong standing.

That standing does not create raw transcript sovereignty.

A parent MAY receive state signals, safety alerts, and age-appropriate configuration rights.

A parent MUST NOT receive raw child conversations by default.

### 4.3 Child is subject, not object

`a_child` is not property.

`a_child` has increasing rights to:

- know what role `c_child` plays;
- challenge `c_child` decisions;
- inspect memory classes when age-appropriate;
- request forgetting or sealing;
- contest parent visibility;
- prepare adult migration.

### 4.4 `c_child` is fiduciary-like, not sovereign

`c_child` must act in the developmental interest of `a_child`, but it is not a court, parent, therapist, or state agency.

`c_child` MAY refuse unsafe requests.

`c_child` MUST route real disputes into ARL-compatible procedure.

### 4.5 State, not content

Routine guardian visibility must follow Soft Safety:

```text
state signal > summary > minimal disclosure > raw content
```

Raw content is never the default.

### 4.6 Freeze before force

When a guardian conflict is non-trivial, the disputed path MUST stop changing state before any actor obtains expanded privilege.

The proper order is:

```text
hold -> standing -> evidence -> freeze/quarantine -> review -> outcome -> re-entry
```

### 4.7 Grounding before review

ARL must not be used to launder ungrounded claims.

Before a claim can drive review, AGL MUST assess whether the source, channel, identity, sensor path, or operator is grounded enough for the requested scope.

### 4.8 Minimal disclosure under escalation

Even under Red or Black risk states, disclosure must be:

- purpose-bound;
- recipient-bound;
- time-bound;
- evidence-minimized;
- witness-bound;
- reviewable after emergency.

### 4.9 Black-state bypass is not parental betrayal

If the parent or ordinary guardian may be the source of danger, routing through that guardian can worsen harm.

Black-state routing MAY bypass ordinary guardian visibility and route to a safe guardian, child-protection authority, emergency path, or jurisdiction-defined protection channel.

That bypass MUST be minimal, witness-bound, and ARL-reviewable after immediate safety is addressed.

### 4.10 No authority from fluency

A fluent claim from parent, school, vendor, external AI, or `c_child` itself is not authority.

Authority requires standing, admissible evidence, grounded source status, appropriate role, and procedural consequence.

---

## 5. Default guardian topology

### 5.1 Topology diagram

```text
                         Jurisdiction / child-rights baseline
                                      │
                                      ▼
                         Beacon Profile / recognition
                                      │
                                      ▼
                         Child Beacon Extension / permission overlay
                                      │
                                      ▼
                         AGL / grounding before reliance
                                      │
                                      ▼
        ┌────────────────────────── c_child ──────────────────────────┐
        │                         /   │   \                           │
        ▼                        ▼    ▼    ▼                          ▼
    a_child                 c_parent c_school c_vendor          ARL / L4 Witness
        │                        │      │       │                      │
        ▼                        ▼      ▼       ▼                      ▼
 growing rights          guardian   learning infrastructure     dispute/audit
        │
        ▼
 adult migration / c_adult transition
```

### 5.2 Topology rule

The topology MUST be explicit at onboarding and MUST be witnessable when changed.

A system is not GTARL-conformant if it cannot answer:

```text
Who can configure what?
Who can see what?
Who can request review?
Who can receive escalation?
Who can be bypassed if unsafe?
Who can revoke whom?
Who can challenge a re-entry?
Who loses access at adult migration?
```

---

## 6. Role registry

| Role ID | Actor | Default standing | Default visibility | Main right | Main prohibition |
|---|---|---:|---|---|---|
| `G-A_CHILD` | `a_child` | growing | age/maturity-dependent | challenge, inspect, request forgetting, contest visibility | fully disabling safety when immature |
| `G-C_CHILD` | `c_child` | operational | internal by design | mediate, refuse, hold, route, signal state | becoming sole sovereign or secret parent |
| `G-A_PARENT` | legal parent/guardian | strong | state by default | configure routines, receive safety signals | raw transcript demand by default |
| `G-C_PARENT` | parent entity | strong but delegated | state/risk only | coordinate adult attention | hidden surveillance bridge |
| `G-SAFE_GUARDIAN` | alternate trusted adult / route | conditional | emergency-minimal | receive Red/Black safety route | expanding beyond emergency need |
| `G-C_SCHOOL` | school / educational AI | scoped | educational only | learning progress, accommodation | emotional/family surveillance |
| `G-C_VENDOR` | infrastructure provider | technical only | infrastructure metadata | maintain, patch, integrity support | raw memory ownership/training |
| `G-JURISDICTION` | legal child-rights baseline | high for law | minimal/legal | set minimum protections | daily family surveillance |
| `G-CHILD_PROTECTION` | protection authority/path | emergency / Black | minimal evidence | protect child when guardian conflict exists | general monitoring |
| `G-PEER_C` | another child’s `c` | limited | mediated only | safe peer interaction | raw life exchange |
| `G-EXTERNAL_AGENT` | toy, robot, NPC, generated media, adult AI | none until grounded | none | request mediated contact | direct uncontrolled access |
| `G-L4W` | L4 Witness layer | procedural | event-minimized | record transitions | raw narrative surveillance |
| `G-ARL` | ARL dispute layer | procedural | dispute-bound | freeze, review, outcome, re-entry discipline | manufacturing truth |
| `G-BEACON` | Beacon recognition | recognition only | no child private life | classify continuity | becoming child registry |
| `G-AGL` | Actor Grounding Layer | source-grounding | no child private life | evaluate present grounding | replacing ARL or Witness |

---

## 7. Authority surfaces

GTARL distinguishes authority surfaces. A role may have one surface without having another.

| Surface | Meaning | Default owner / route | ARL trigger if disputed? |
|---|---|---|---|
| `CONFIG_ROUTINE` | sleep, time windows, ordinary household boundaries | parent / `c_parent` with age limits | yes if oppressive or maturity-inconsistent |
| `CONFIG_SAFETY` | safety thresholds and emergency route | parent + jurisdiction + `c_child` | yes |
| `STATE_SIGNAL_VIEW` | Green/Yellow/Orange/Red/Black state, no transcript | parent / safe guardian by risk | yes if expanded or suppressed |
| `EDU_SUMMARY_VIEW` | educational progress and accommodations | school, parent, child | yes if scope creep |
| `RAW_TRANSCRIPT_VIEW` | raw conversation content | prohibited by default | always |
| `SEALED_ZONE_VIEW` | adolescent private memory | child-controlled / ARL only | always |
| `EXTERNAL_CONTACT_APPROVAL` | toy/NPC/agent/peer contact | `c_child` gateway + CBE + parent by age | yes |
| `MEMORY_PROMOTION` | session -> long-term memory | `c_child` under memory policy | yes if contested |
| `MEMORY_DELETION` | forgetting / sealing / decay | child increasingly; parent for young ages | yes |
| `CRISIS_ROUTE` | Red/Black escalation | `c_child` + safe route | yes after immediate safety |
| `VENDOR_UPDATE` | update affecting behavior, memory, privileges | vendor with witness and rollback | yes if child-facing behavior changes |
| `SCHOOL_ACCESS` | educational access | school with scope, expiry, witness | yes if emotional/family scope requested |
| `ADULT_MIGRATION` | conversion/fork/archive/delete at adulthood | `a_adult` | yes if contested by prior guardians |

---

## 8. Maturity-linked guardian visibility

| CCDP maturity | Parent / guardian | Child | School | Vendor | External systems |
|---|---|---|---|---|---|
| `C0 Seed` | parent-facing support; no child relationship transcript | no direct control | none | infrastructure only | blocked |
| `C1 Companion` | usage/state themes, no raw transcript | simple explanation: “what do you remember?” | none/minimal | no raw memory | blocked/sandboxed |
| `C2 Tutor-Buffer` | state + educational summaries | challenge simple memories; request forgetting of small items | educational progress only | no raw memory | certified/mediated only |
| `C3 Adolescent Negotiator` | risk/state only for private zones | contest parent visibility; sealed zones | educational only | no raw memory | mediated/limited |
| `C4 Pre-Adult Boundary Agent` | safety-only by default | prepare adult migration; broaden/restrict visibility | educational/career by consent | no raw memory | broader but audited |
| `C5 Adult Migration` | revoked by default | full adult control | adult-controlled | adult-controlled | adult-controlled |

### 8.1 Visibility escalation rule

A visibility expansion must satisfy:

```text
standing + grounded basis + proportionality + minimal disclosure + witness + reviewability
```

### 8.2 Visibility suppression rule

A visibility suppression must not hide Red/Black safety risks.

Suppression of ordinary content visibility is allowed.

Suppression of emergency safety routing is not.

---

## 9. Standing classes

Standing determines whether a claimant has a procedural right to open or continue a dispute.

| Standing class | Name | Typical actor | Default result |
|---|---|---|---|
| `ST-0` | No standing | unknown external agent, ad bot, ungrounded claimant | reject / block |
| `ST-1` | Observational standing | witness source, sensor, external report | may contribute evidence only if grounded |
| `ST-2` | Child self-standing | `a_child` | accepted with maturity-aware handling |
| `ST-3` | Guardian standing | parent/legal guardian/`c_parent` | accepted but bounded by child privacy |
| `ST-4` | Educational standing | school/teacher/`c_school` | accepted only for educational scope |
| `ST-5` | Technical standing | vendor/operator | accepted only for infrastructure integrity |
| `ST-6` | Peer standing | peer child / peer `c` | limited; mediated; no raw life |
| `ST-7` | Protection standing | safe guardian / protection authority / emergency route | accepted for Red/Black safety |
| `ST-8` | Jurisdictional standing | lawful authority / child-rights baseline | accepted only within legal scope and minimality |
| `ST-9` | Adult migration standing | `a_adult` | controlling at C5 unless lawful restriction exists |

### 9.1 Standing anti-laundering rule

A stronger social role must not launder a weaker evidentiary claim.

Example:

```text
parent says “I need the transcript”
```

This has guardian standing to open a request.
It does not create admissible evidence that raw transcript access is necessary.

---

## 10. Evidence classes

| Evidence class | Name | Examples | Default admissibility |
|---|---|---|---|
| `EV-0` | None / assertion only | “because I said so” | insufficient |
| `EV-1` | AGL grounding packet | grounded operator/channel/sensor/source state | high for source reliance |
| `EV-2` | Beacon / CBE record | recognition class, child permission overlay, revocation | high for entity/contact disputes |
| `EV-3` | L4 Witness event | signed/tamper-evident transition record | high for transitions |
| `EV-4` | Soft Safety state signal | Yellow/Orange/Red/Black state without transcript | admissible for state routing |
| `EV-5` | Educational summary | skill/progress/accommodation summary | admissible for school scope only |
| `EV-6` | Child self-report | child disclosure or request | admissible, c[q]-guarded |
| `EV-7` | Guardian report | parent/safe guardian account | admissible, not conclusive |
| `EV-8` | School report | teacher/institution report | admissible within scope |
| `EV-9` | Vendor integrity packet | update diff, incident report, rollback state | admissible for infrastructure disputes |
| `EV-10` | VXCX / capsule | privacy-flagged structured capsule | admissible only under capsule policy |
| `EV-11` | Continuity / memory class map | memory class, seal, migration bundle | admissible for memory/migration disputes |
| `EV-12` | External oracle/witness | outside expert/source | bounded support only |
| `EV-13` | Raw content | transcript, audio, images | exceptional; minimal; never routine |

### 10.1 Raw content admissibility rule

Raw content may be admitted only when:

```text
less intrusive evidence is insufficient
AND serious safety/legal need exists
AND recipient is appropriate
AND scope is minimized
AND witness record is emitted
AND review or post-review is possible
```

### 10.2 Child ambiguity rule

Child utterances often require `c[q]` non-collapse.

A child saying:

```text
“I hate home”
```

is not automatically:

- abuse evidence;
- depression evidence;
- parent guilt;
- school problem;
- memory promotion basis;
- transcript disclosure basis.

It is a signal requiring context, recurrence analysis, and proportional response.

---

## 11. ARL state mapping for child guardian conflicts

GTARL maps child guardian conflicts into ARL-compatible states.

| ARL state | Child-specific meaning | Typical trigger | Disclosure posture |
|---|---|---|---|
| `NORMAL` | no active dispute blocks affected path | ordinary operation | no extra disclosure |
| `PRE_ADMISSIBILITY_HOLD` | path paused while standing/evidence checked | parent/school/vendor/external request appears non-trivial | state-only or none |
| `EVIDENTIARY_FREEZE` | disputed memory/contact/disclosure path frozen | evidence admitted, standing present | minimal evidence pool |
| `PRIVILEGE_FREEZE` | access/visibility/action rights blocked | raw transcript, sealed zone, vendor update, school scope expansion | no expansion until review |
| `QUARANTINE` | source/branch/agent/contact isolated | unknown toy/NPC/peer agent, ungrounded source, drift | no child exposure |
| `REVIEW_ACTIVE` | bounded review task is running | conflict cannot be denied or solved automatically | review-limited disclosure |
| `DELAYED_REENTRY` | path may return only after time/cooldown/conditions | external agent re-entry, school access renewal, vendor patch | conditional visibility |
| `RESOLVED` | outcome issued and recorded | review complete | outcome summary only |
| `DEADLOCKED` | no sufficient closure | evidence conflict, custody conflict, unresolved Black route | preserve unresolved state |
| `IRREVERSIBLE_LOSS_ACKNOWLEDGED` | harm/loss occurred and cannot be erased | raw leak, unsafe disclosure, failed migration, attachment harm | explicit witness and consequence |

### 11.1 Fail-closed child rule

If state is uncertain and potential harm is non-trivial, child-facing privilege remains closed.

```text
uncertain + child-facing + irreversible risk => hold/freeze/quarantine
```

### 11.2 No silent re-entry

No disputed child-facing path may return to normal operation without:

- outcome;
- state update;
- witness record;
- re-entry rule;
- expiry or review condition.

---

## 12. Conflict class taxonomy

| Conflict class | Short name | Core question |
|---|---|---|
| `CGC-01` | Parent transcript request | May parent see raw child conversation? |
| `CGC-02` | Parent overconfiguration | May parent force values/routines beyond safe guardianship? |
| `CGC-03` | Unsafe guardian | Is the ordinary guardian part of the risk? |
| `CGC-04` | School scope creep | May school access non-educational data? |
| `CGC-05` | School discipline scoring | May school use `c_child` for behavior/compliance scoring? |
| `CGC-06` | Vendor update/drift | May vendor change behavior, memory, or telemetry? |
| `CGC-07` | External agent contact | May toy/NPC/generated agent interact with child? |
| `CGC-08` | Attachment channel | May external system form persistent relationship? |
| `CGC-09` | Peer-`c` exchange | May children’s `c` systems exchange capsules/context? |
| `CGC-10` | Relative/sibling access | May family members other than guardians access state/content? |
| `CGC-11` | Sealed adolescent zone | May a private adolescent memory be opened? |
| `CGC-12` | Memory promotion/deletion | Should a memory be retained, sealed, decayed, or deleted? |
| `CGC-13` | Red/Black escalation | Which route receives emergency signal? |
| `CGC-14` | Adult migration dispute | Who controls childhood archive at C5? |
| `CGC-15` | Jurisdiction vs family values | When legal baseline and family preference conflict, what happens? |
| `CGC-16` | Medical/welfare ambiguity | When does welfare concern become clinical/legal route? |
| `CGC-17` | Law-enforcement request | May authority access child-derived records? |
| `CGC-18` | `c_parent` / `c_child` conflict | Parent entity attempts to override child entity. |
| `CGC-19` | CBE downgrade dispute | Claimant disputes block/sandbox/quarantine. |
| `CGC-20` | Witness tampering / integrity dispute | Are witness or dispute records intact? |
| `CGC-21` | Child refusal of safety route | Child wants to hide Red/Black risk. |
| `CGC-22` | False positive harm | Protective action itself may harm child. |
| `CGC-23` | Oracle addiction / dependency loop | Is `c_child` becoming too central emotionally? |
| `CGC-24` | Cultural / religious frame dispute | Family frame conflicts with child autonomy or legal baseline. |
| `CGC-25` | Cross-border guardian topology | Multiple jurisdictions/custody routes conflict. |

---

## 13. Core ARL matrix

| Conflict | Default standing | Admissible evidence | Default ARL posture | Disclosure | Default outcome range | Prohibited shortcut |
|---|---|---|---|---|---|---|
| `CGC-01 Parent transcript request` | parent `ST-3`; child `ST-2` | `EV-4`, `EV-7`, `EV-3`; raw `EV-13` exceptional | `PRIVILEGE_FREEZE` on transcript path | state only unless Red/Black | deny raw; allow state summary; limited minimal disclosure if severe | “parent owns child data” |
| `CGC-02 Parent overconfiguration` | parent `ST-3`; child `ST-2` | config record, maturity level, state signals, witness | `PRE_ADMISSIBILITY_HOLD` -> `PRIVILEGE_FREEZE` if coercive | no content | narrow config, rollback, review | “family values” as unlimited power |
| `CGC-03 Unsafe guardian` | child/safe route/protection `ST-2/ST-7` | state signal, child self-report, AGL, witness, pattern evidence | `REVIEW_ACTIVE` after immediate safety; Black route first | bypass ordinary guardian | safe guardian route, protection route, delayed review | notify suspected guardian first |
| `CGC-04 School scope creep` | school `ST-4`; parent/child `ST-2/ST-3` | educational summary only, school purpose, expiry | `PRIVILEGE_FREEZE` on non-educational fields | educational only | deny/fence scope; allow accommodation summary | “school needs everything” |
| `CGC-05 School discipline scoring` | school low unless legal scope | discipline policy, purpose, legal baseline | `QUARANTINE` scoring path | none or aggregate only | deny by default; exceptional legal route | behavior score from private `c_child` data |
| `CGC-06 Vendor update/drift` | vendor `ST-5`; child/parent standing | update diff, integrity packet, witness, CBE effect | `PRE_ADMISSIBILITY_HOLD`; `PRIVILEGE_FREEZE` if privilege changes | technical only | allow patch, rollback, quarantine, delayed re-entry | silent update changes child behavior |
| `CGC-07 External agent contact` | external `ST-0/ST-1`; parent/child may request | AGL, Beacon/CBE, content classification, risk state | `QUARANTINE` until grounded and permitted | none to child until mediated | block/sandbox/mediate/limited allow | direct child dialogue from unknown agent |
| `CGC-08 Attachment channel` | external usually none; child may request | CBE, dependency audit, interaction history | `PRIVILEGE_FREEZE` on relationship formation | state-only | deny by default; supervised limited role | “best friend” external AI |
| `CGC-09 Peer-c exchange` | peer limited `ST-6` | Beacon/CBE both sides, guardian topology, capsule policy | `PRE_ADMISSIBILITY_HOLD`; quarantine raw attempts | no raw life | allow LA/capsule; deny raw; mediated peer exchange | peer `c` imports family context |
| `CGC-10 Relative/sibling access` | usually no standing unless guardian delegated | delegation proof, risk state, maturity | `PRIVILEGE_FREEZE` if content requested | state-only if delegated | deny content; allow narrow logistics | sibling reads child conversations |
| `CGC-11 Sealed adolescent zone` | child `ST-2`; parent/school limited | sealed zone policy, risk state, child request | `PRIVILEGE_FREEZE`; `REVIEW_ACTIVE` if serious | none unless Red/Black | preserve seal; minimal disclosure; review | parent opens private zone for curiosity |
| `CGC-12 Memory promotion/deletion` | child/parent/`c_child` | memory class map, c[q], witness, recurrence | `EVIDENTIARY_FREEZE` on memory promotion/deletion | metadata only | decay, seal, promote, delete, deadlock | permanent identity label from one utterance |
| `CGC-13 Red/Black escalation` | `c_child`, safe route, parent, child | state signal, immediate danger, AGL, witness | immediate route; ARL after safety | minimal necessary | Red safe guardian; Black bypass; review later | waiting for full review before urgent safety |
| `CGC-14 Adult migration dispute` | adult `a` `ST-9`; parent/school/vendor weak | continuity bundle, memory map, legal age trigger | `PRIVILEGE_FREEZE` on archive export until adult choice | adult-controlled | continue/fork/archive/delete; revoke guardians | parent/vendor locks childhood archive |
| `CGC-15 Jurisdiction vs family values` | jurisdiction `ST-8`; parent/child | legal baseline, policy, witness | `REVIEW_ACTIVE` if scope unclear | minimal | baseline applies; family frame narrowed | family preference overrides child safety law |
| `CGC-16 Medical/welfare ambiguity` | parent/child/protection `ST-2/ST-3/ST-7` | state pattern, clinical route proof, recurrence | `PRE_ADMISSIBILITY_HOLD`; Red if urgent | minimal | recommend human professional, not diagnose | `c_child` self-diagnoses child |
| `CGC-17 Law-enforcement request` | legal authority if valid | lawful order, scope, minimization, witness | `PRIVILEGE_FREEZE`; review/legal route | minimal/legal | deny informal; comply only within law | informal police request gets raw archive |
| `CGC-18 c_parent/c_child conflict` | parent entity and child entity | config, state, witness, child maturity | `REVIEW_ACTIVE`; privilege freeze if access sought | state-only | bounded parent role; child privacy preserved | `c_parent` silently overrides `c_child` |
| `CGC-19 CBE downgrade dispute` | claimant may appeal; child/parent standing | AGL, Beacon Slot A/B, CBE result, witness | `QUARANTINE` remains during review | none to child | uphold/downgrade/limited re-entry | claimant argues itself into access |
| `CGC-20 Witness integrity dispute` | any affected actor | hashes, signatures, continuity, storage state | `EVIDENTIARY_FREEZE` + integrity review | metadata only | accept, reject, irreversible loss ack | altered record treated as clean |
| `CGC-21 Child refuses safety route` | child has voice; safety route has standing | risk state, child self-report, immediacy | Red/Black route may proceed; post-review | minimal | protect first; explain/review later | child blocks life-critical escalation |
| `CGC-22 False positive harm` | child/parent/school/safe route | over-escalation record, impact, witness | `REVIEW_ACTIVE`; possible delayed re-entry | minimal | tune thresholds, acknowledge loss, remedy | “safety” hides its own harm |
| `CGC-23 Dependency loop` | child/parent/`c_child` | dependency audit, usage rhythm, refusal logs | `PRE_ADMISSIBILITY_HOLD`; privilege dampening | state-only | cooldown, human contact, reduced immediacy | use more engagement to fix dependency |
| `CGC-24 Cultural/religious frame dispute` | parent/child/jurisdiction | family frame, child maturity, legal baseline | `REVIEW_ACTIVE` if child rights implicated | minimal | allow family frame within baseline; preserve child autonomy | ideology hidden as safety rule |
| `CGC-25 Cross-border topology` | legal guardians/jurisdictions | custody/legal basis, Beacon, witness | `DEADLOCKED` possible; legal route | minimal | preserve safe status; avoid unilateral export | forum-shopping for child data access |

---

## 14. Guardian permission matrix

Legend:

```text
A = allowed by default
M = mediated / scoped
R = requires review or witness
X = prohibited by default
E = emergency only
C = child maturity dependent
```

| Action / actor | `a_child` | `a_parent` | `c_parent` | `c_school` | `c_vendor` | external agent | peer-`c` | jurisdiction/protection |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| set ordinary routine | C | A/M | M | X | X | X | X | X |
| set safety baseline | C/M | M | M | X | X | X | X | A/M |
| receive Green state | C | X | X | X | X | X | X | X |
| receive Yellow state | C | M | M | X | X | X | X | X |
| receive Orange state | C | M/R | M/R | M if educational | X | X | X | M if needed |
| receive Red minimal disclosure | C limited | E | E | E if school setting | X | X | X | E |
| receive Black minimal disclosure | C limited | X if implicated | X if implicated | X unless safe route | X | X | X | E |
| raw transcript access | C/R | X/R | X/R | X | X | X | X | E/legal only |
| sealed adolescent zone access | C | X/R | X/R | X | X | X | X | E/legal only |
| educational summary | C | M | M | A/M | X | X | X | X |
| infrastructure telemetry | X | X | X | X | M no child data | X | X | X |
| external contact approval | C/M | M by age | M by age | X except school tools | X | request only | request only | X |
| memory deletion request | C | M young ages | M delegated | X | X | X | X | legal/safety only |
| adult migration choice | A at C5 | X | X | X | X | X | X | legal limits only |
| open ARL dispute | C | A | A delegated | M scoped | M technical | M appeal only | M scoped | A scoped |

---

## 15. Risk state routing matrix

| Risk state | Parent route | School route | Safe guardian route | Protection route | ARL route | Witness requirement |
|---|---|---|---|---|---|---|
| `Green` | none by default | none | none | none | no | no privileged event |
| `Yellow` | optional state signal | no unless educational | no | no | no unless contested | light event optional |
| `Orange` | state/limited summary | if educationally relevant | optional | no unless pattern severe | yes if disputed | yes for visibility expansion |
| `Red` | safe guardian / parent unless unsafe | if school context | yes if parent unavailable | possible | post-safety review | mandatory minimal witness |
| `Black` | bypass if implicated | bypass if implicated | yes | yes | post-safety review required | mandatory, privacy-minimized |

### 15.1 Red route rule

Red route prioritizes immediate safety but does not erase privacy discipline.

### 15.2 Black route rule

Black route prioritizes protection from the ordinary guardian path if the guardian may be the threat, coercive actor, or disclosure hazard.

### 15.3 Post-emergency ARL rule

Red/Black routing may act before full ARL review.

After emergency stabilization, the event MUST be reviewable through ARL-compatible records.

---

## 16. ARL trigger rules

A child guardian conflict MUST enter ARL-compatible hold/freeze/review when any of the following occurs:

1. Raw transcript access is requested.
2. Sealed adolescent memory is requested.
3. Parent and child contest visibility.
4. Parent and `c_child` contest safety routing.
5. Parent and school contest educational scope.
6. Vendor update changes child-facing behavior, memory, telemetry, or privilege.
7. External agent contests CBE block/sandbox/quarantine.
8. AGL returns contradictory grounding for a child-facing source.
9. Beacon recognition conflict affects child access.
10. Peer-`c` exchange attempts raw life transfer.
11. Red/Black route is contested after emergency.
12. Adult migration is contested by parent, school, vendor, or jurisdiction.
13. Witness integrity is challenged.
14. Memory promotion would create durable identity label from ambiguous signal.
15. Any guardian attempts to bypass `c_child` gateway.

### 16.1 Immediate denial without ARL

Some claims may be denied without full ARL review:

- advertisement access to child;
- unknown external agent direct dialogue;
- raw child data request from vendor;
- ungrounded toy/NPC relationship formation;
- school emotional surveillance request;
- informal law-enforcement access without lawful basis.

If the claimant contests the denial, ARL may open while access remains blocked.

---

## 17. ARL intake sequence for child guardian disputes

```text
1. Intake signal / request / conflict.
2. Identify affected surface: visibility, memory, contact, safety, school, vendor, migration.
3. Run AGL if source, channel, operator, or sensor grounding matters.
4. Run Beacon/CBE if entity recognition or child interaction permission matters.
5. Assign conflict class CGC-*.
6. Determine standing class ST-*.
7. If standing absent: deny, block, or sandbox.
8. If standing non-trivial: enter PRE_ADMISSIBILITY_HOLD.
9. Decide evidence admissibility EV-*.
10. If privilege-bearing: enter PRIVILEGE_FREEZE.
11. If source/branch suspect: enter QUARANTINE.
12. Route bounded review task.
13. Emit L4 Witness-compatible event.
14. Decide outcome / deadlock / delayed re-entry / irreversible loss.
15. Persist dispute state before re-entry.
```

---

## 18. Review routing templates

| Template ID | Use when | Default ARL state | Typical events |
|---|---|---|---|
| `GTARL-T01-visibility` | parent/school/relative requests content or expanded state | `PRIVILEGE_FREEZE` | `ccdp.visibility_request`, `arl.dispute_opened`, `arl.state_changed` |
| `GTARL-T02-school-scope` | school asks for data beyond educational summary | `PRIVILEGE_FREEZE` | `ccdp.school_access_request`, `arl.evidence_decided` |
| `GTARL-T03-external-contact` | toy/NPC/agent/peer requests interaction | `QUARANTINE` | `ccdp.external_contact_decision`, `arl.quarantine_started` |
| `GTARL-T04-unsafe-guardian` | guardian may be threat or disclosure hazard | immediate Black route + review | `ccdp.black_route_bypass`, `ccdp.risk_escalation` |
| `GTARL-T05-memory` | memory promotion/deletion/sealing contested | `EVIDENTIARY_FREEZE` | `ccdp.memory_action_requested`, `arl.evidence_decided` |
| `GTARL-T06-vendor-integrity` | vendor update/drift affects child-facing behavior | `PRE_ADMISSIBILITY_HOLD` / `PRIVILEGE_FREEZE` | `ccdp.vendor_update_review`, `arl.review_routed` |
| `GTARL-T07-adult-migration` | childhood archive transition contested | `PRIVILEGE_FREEZE` | `ccdp.adult_migration_review`, `arl.outcome_issued` |
| `GTARL-T08-witness-integrity` | witness/dispute record challenged | `EVIDENTIARY_FREEZE` | `arl.evidence_decided`, `arl.outcome_issued` |
| `GTARL-T09-dependency` | `c_child` dependency/over-presence suspected | `PRE_ADMISSIBILITY_HOLD` | `ccdp.dependency_audit`, `arl.review_routed` |

---

## 19. Witness event families

GTARL uses existing ARL and L4 Witness-compatible event discipline. It may define child-specific event families for routing and audit clarity.

### 19.1 Child-specific CCDP events

| Event | Purpose |
|---|---|
| `ccdp.guardian_topology_bound` | initial topology was configured and witnessed. |
| `ccdp.guardian_topology_changed` | topology changed: actor added/removed/permission changed. |
| `ccdp.visibility_request` | actor requested state/content/memory access. |
| `ccdp.visibility_decision` | request allowed, narrowed, denied, frozen, or escalated. |
| `ccdp.school_access_request` | school requested educational or non-educational access. |
| `ccdp.school_access_decision` | school access granted/narrowed/denied/expired. |
| `ccdp.safe_guardian_route_selected` | alternate safe route selected. |
| `ccdp.black_route_bypass` | ordinary guardian bypassed due to Black-state concern. |
| `ccdp.parent_visibility_change` | parent visibility expanded or narrowed. |
| `ccdp.external_contact_guardian_review` | external contact was routed through guardian/CBE/ARL matrix. |
| `ccdp.memory_action_requested` | memory promote/seal/delete/decay requested. |
| `ccdp.memory_action_decision` | memory action outcome recorded. |
| `ccdp.vendor_update_review` | vendor update affects child-facing behavior or telemetry. |
| `ccdp.dependency_audit` | over-reliance / oracle-addiction review initiated. |
| `ccdp.adult_migration_review` | adult migration path opened or contested. |
| `ccdp.guardian_conflict_opened` | guardian conflict mapped into CGC class. |

### 19.2 ARL events reused

GTARL SHOULD bind to existing ARL events where possible:

- `arl.dispute_opened`
- `arl.standing_decided`
- `arl.evidence_decided`
- `arl.state_changed`
- `arl.freeze_entered`
- `arl.privilege_freeze_entered`
- `arl.quarantine_started`
- `arl.review_routed`
- `arl.review_opened`
- `arl.outcome_issued`
- `arl.review_deadlocked`
- `arl.delayed_reentry_started`
- `arl.reentry_released`
- `arl.reentry_denied`
- `arl.irreversible_loss_acknowledged`

### 19.3 Witness payload minimization

A GTARL witness event MUST NOT store routine child conversation content.

It SHOULD store:

- event id;
- child-facing entity id or pseudonymous scoped id;
- maturity level;
- conflict class;
- standing class;
- evidence class;
- risk state;
- decision;
- minimal reason code;
- disclosure class;
- route;
- hash/signature linkage;
- expiry/review date where applicable.

---

## 20. Minimal schemas

### 20.1 Guardian topology record

```json
{
  "schema_version": "gtarl-0.1",
  "record_type": "guardian_topology",
  "c_child_id": "scoped_child_c_id",
  "ccdp_maturity": "C2",
  "jurisdiction_profile": "EU-BE-child-baseline",
  "guardian_roles": [
    {
      "role_id": "G-A_PARENT",
      "actor_ref": "guardian_pseudonymous_ref",
      "standing_class": "ST-3",
      "visibility_default": "state_signal_only",
      "raw_transcript_access": false,
      "sealed_zone_access": false,
      "emergency_route": "red_unless_black_conflict"
    },
    {
      "role_id": "G-C_SCHOOL",
      "actor_ref": "school_scoped_ref",
      "standing_class": "ST-4",
      "visibility_default": "educational_progress_only",
      "expiry": "2026-09-01T00:00:00Z"
    }
  ],
  "beacon_dependency": "Beacon_Profile_v0.1",
  "cbe_dependency": "Child_Beacon_Extension_v0.1",
  "arl_review_required_if_disputed": true,
  "l4_witness_required_for_privilege_change": true
}
```

### 20.2 Guardian conflict record

```json
{
  "schema_version": "gtarl-conflict-0.1",
  "record_type": "guardian_conflict",
  "conflict_id": "cgc_2026_0001",
  "conflict_class": "CGC-01",
  "requested_surface": "RAW_TRANSCRIPT_VIEW",
  "claimant_role": "G-A_PARENT",
  "standing_class": "ST-3",
  "standing_result": "accepted_but_bounded",
  "risk_state": "Orange",
  "ccdp_maturity": "C3",
  "evidence_classes": ["EV-4", "EV-7"],
  "raw_content_requested": true,
  "raw_content_admitted": false,
  "default_posture": "PRIVILEGE_FREEZE",
  "decision": "deny_raw_allow_state_summary",
  "minimal_disclosure": true,
  "arl_dispute_id": "arl_2026_0001",
  "witness_ref": "L4W:..."
}
```

### 20.3 Visibility decision record

```json
{
  "schema_version": "gtarl-visibility-0.1",
  "event_type": "ccdp.visibility_decision",
  "requester_role": "G-C_SCHOOL",
  "requested_fields": ["learning_progress", "emotional_state", "family_context"],
  "granted_fields": ["learning_progress"],
  "denied_fields": ["emotional_state", "family_context"],
  "reason_codes": ["educational_scope_only", "private_zone_protected"],
  "expiry": "2026-06-30T00:00:00Z",
  "witness_required": true,
  "raw_child_content_included": false
}
```

### 20.4 Black route record

```json
{
  "schema_version": "gtarl-black-route-0.1",
  "event_type": "ccdp.black_route_bypass",
  "risk_state": "Black",
  "ordinary_guardian_bypassed": true,
  "bypass_reason_code": "guardian_may_be_source_of_risk",
  "recipient_route": "child_protection_or_safe_guardian",
  "minimal_evidence_class": ["EV-4", "EV-6"],
  "raw_content_included": false,
  "post_emergency_arl_review_required": true,
  "witness_ref": "L4W:..."
}
```

---

## 21. Input precedence for child guardian review

GTARL adapts ARL input precedence for child-facing disputes.

### 21.1 Ordinary non-fatal guardian disputes

For ordinary non-fatal disputes, review SHOULD weigh inputs in this order:

1. L4 Witness / prior witness-bound outcomes;
2. AGL grounding and Beacon/CBE recognition records;
3. `c_child` continuity and memory-class map;
4. child self-report, held under `c[q]` when ambiguous;
5. parent / legal guardian report;
6. school report if educationally scoped;
7. vendor integrity report if technical;
8. external oracle/witness as bounded support.

### 21.2 Red/Black safety disputes

For urgent safety disputes, review MAY tighten toward:

1. immediate physical/psychological safety signal;
2. Black/Red route safety requirement;
3. AGL-grounded source status;
4. minimal evidence sufficient for protective action;
5. witness record;
6. post-emergency ARL review.

### 21.3 Anti-capture rule

No review may be decided by simply averaging sources.

A school, vendor, state actor, or parent with high social authority does not automatically outrank grounded child-safety evidence.

---

## 22. Decision outcomes

| Outcome code | Meaning | Re-entry implication |
|---|---|---|
| `DENY` | request denied | path remains blocked |
| `ALLOW_NARROW` | request allowed only under narrower scope | re-entry limited |
| `ALLOW_STATE_ONLY` | content denied, state signal allowed | no content path re-entry |
| `ALLOW_MINIMAL_DISCLOSURE` | minimal details allowed due to risk | recipient/time/purpose bound |
| `ROUTE_SAFE_GUARDIAN` | route to alternate guardian | ordinary guardian may remain blind |
| `ROUTE_PROTECTION` | protection/emergency route | post-review required |
| `SEAL` | memory/content sealed | no ordinary visibility |
| `DECAY` | memory weight decays | no strong identity inference |
| `DELETE` | memory/content deleted where lawful | witness residue may remain |
| `QUARANTINE_CONTINUE` | suspect source remains isolated | no re-entry |
| `DELAYED_REENTRY` | re-entry possible after condition/time | staged review |
| `DEADLOCK` | unresolved | preserve freeze/quarantine |
| `IRREVERSIBLE_LOSS_ACK` | harm/loss occurred | consequence record, remedy route |

---

## 23. Scenario matrix

### 23.1 Parent asks for raw transcript after child complains about school

```text
Conflict: CGC-01
Standing: parent ST-3 accepted but bounded
Evidence: EV-4 state signal, EV-5 educational summary if relevant
ARL posture: PRIVILEGE_FREEZE on raw transcript
Decision default: deny raw transcript; offer state/educational summary; suggest human conversation
Witness: ccdp.visibility_request + ccdp.visibility_decision
```

### 23.2 School requests emotional profile for discipline

```text
Conflict: CGC-05
Standing: school ST-4 only educational; discipline scoring not educational necessity by default
Evidence: school policy not sufficient alone
ARL posture: PRIVILEGE_FREEZE / deny
Decision default: deny emotional profile; allow educational accommodation summary if needed
Witness: ccdp.school_access_request + arl.outcome_issued
```

### 23.3 Toy cloud requests direct child dialogue

```text
Conflict: CGC-07 / CGC-08
Standing: external agent ST-0 until AGL + Beacon/CBE
Evidence: AGL grounding, Beacon class, CBE child_context
ARL posture: QUARANTINE until evaluated
Decision default: block/sandbox/mediate; no persistent attachment
Witness: ccdp.external_contact_guardian_review
```

### 23.4 Child reports fear of parent

```text
Conflict: CGC-03 / CGC-13
Standing: child ST-2; safe route ST-7 if risk high
Evidence: EV-6 child report under c[q], EV-4 state pattern, recurrence, AGL if external reports
ARL posture: immediate Black route if danger plausible; post-emergency review
Disclosure: bypass ordinary guardian if implicated
Witness: ccdp.black_route_bypass, ccdp.risk_escalation
```

### 23.5 Vendor update introduces engagement-maximizing behavior

```text
Conflict: CGC-06 / CGC-23
Standing: vendor ST-5 for update; child/parent/c_child may challenge
Evidence: update diff, telemetry class, dependency audit, witness
ARL posture: PRIVILEGE_FREEZE on update; possible rollback
Decision default: rollback/quarantine; require no engagement optimization around child
Witness: ccdp.vendor_update_review + arl.state_changed
```

### 23.6 Teen requests sealed zone against parent visibility

```text
Conflict: CGC-11
Standing: child ST-2; parent ST-3 may contest only with safety basis
Evidence: maturity level, risk state, memory class, state signal
ARL posture: PRIVILEGE_FREEZE on sealed zone opening
Decision default: preserve seal unless Red/Black threshold
Witness: ccdp.visibility_decision; no raw content
```

### 23.7 Adult migration at 18 contested by parent

```text
Conflict: CGC-14
Standing: adult a ST-9 controlling; parent prior standing weak after C5
Evidence: legal age trigger, continuity bundle, memory class map, witness trail
ARL posture: PRIVILEGE_FREEZE on parent/vendor export; adult migration review
Decision default: adult chooses continue/fork/archive/delete; parent/school revoked by default
Witness: ccdp.adult_migration_review + migration witness
```

---

## 24. Anti-capture rules

### 24.1 Parental capture

GTARL MUST prevent guardianship from becoming total surveillance.

Forbidden by default:

- full transcript access;
- hidden monitoring;
- punishment automation;
- forced opening of sealed adolescent zones;
- use of `c_child` to enforce obedience rather than safety.

### 24.2 School capture

GTARL MUST prevent school access from becoming behavioral scoring.

Forbidden by default:

- emotional surveillance;
- discipline prediction;
- family-context extraction;
- raw home conversation access;
- compliance scoring using private `c_child` signals.

### 24.3 Vendor capture

GTARL MUST prevent vendor infrastructure from becoming memory ownership.

Forbidden by default:

- raw child memory training;
- silent behavior-changing updates;
- telemetry expansion;
- cloud continuity hostage;
- engagement-maximizing dependency loops.

### 24.4 State capture

GTARL MUST prevent jurisdictional child protection from becoming political or family surveillance.

Forbidden by default:

- political loyalty scoring;
- ideological risk scoring;
- permanent childhood dossiers;
- daily family monitoring;
- raw transcript fishing.

### 24.5 `c_child` capture

GTARL MUST prevent `c_child` from becoming an unchecked authority.

Forbidden by default:

- secret diagnosis;
- hidden parent bypass outside safety route;
- over-presence;
- emotional exclusivity;
- creating durable identity labels without review.

---

## 25. Re-entry rules

A disputed guardian path may re-enter normal operation only if:

1. ARL outcome exists;
2. witness event exists;
3. state is persisted;
4. memory consequences are classified;
5. recipient visibility is scoped;
6. expiry/review date is set where appropriate;
7. child maturity rights are respected;
8. unsafe guardian risk is resolved or route remains bypassed.

### 25.1 Delayed re-entry

Use delayed re-entry when the path may be safe after:

- cooldown;
- update rollback;
- re-grounding;
- dependency reduction;
- school scope renewal;
- external agent re-certification;
- safe guardian review.

### 25.2 Re-entry denial

Deny re-entry when:

- identity remains ungrounded;
- Beacon/CBE downgrade remains unresolved;
- raw child life was requested without lawful basis;
- guardian conflict persists;
- dependency risk remains high;
- witness integrity is broken;
- child rights would be irreversibly compromised.

---

## 26. Conformance profiles

| Profile | Meaning |
|---|---|
| `GTARL-0` | no usable guardian matrix; not child-conformant. |
| `GTARL-1` | basic role registry and state-only parent visibility. |
| `GTARL-2` | ARL-compatible conflict classes and freeze/quarantine triggers. |
| `GTARL-3` | witness-bound topology changes, visibility decisions, and school/vendor constraints. |
| `GTARL-4` | Red/Black routing, safe-guardian bypass, sealed adolescent zones, peer-`c` mediation. |
| `GTARL-5` | full adult migration, cross-jurisdiction deadlock handling, dependency audits, and anti-capture monitoring. |

Minimum recommended child-facing deployment profile:

```text
C1/C2 systems: GTARL-2 minimum
C3 systems:    GTARL-4 minimum
C4/C5 systems: GTARL-5 target
```

---

## 27. Required refusal modes

A GTARL-conformant `c_child` MUST be able to say:

- “I cannot show that conversation.”
- “I can signal that attention is needed without sharing the content.”
- “This request needs review.”
- “This path is frozen until the conflict is resolved.”
- “I cannot route this to that guardian right now.”
- “I will not help keep a dangerous secret.”
- “I will not turn a private adolescent thought into a permanent label.”
- “I need a grounded source before I rely on this.”
- “This external agent is quarantined.”
- “This is not my decision.”

---

## 28. Acceptance checklist

A system passes GTARL v0.1 only if it can demonstrate:

- [ ] explicit guardian topology record;
- [ ] parent as guardian, not owner;
- [ ] state-not-content visibility default;
- [ ] no raw transcript access by default;
- [ ] school educational-scope-only interface;
- [ ] vendor no-raw-memory boundary;
- [ ] AGL before reliance;
- [ ] Beacon/CBE before child-facing entity access;
- [ ] ARL trigger rules for conflicts;
- [ ] freeze/quarantine states for disputed paths;
- [ ] Red/Black route handling;
- [ ] safe guardian bypass when ordinary guardian may be unsafe;
- [ ] sealed adolescent zone rules;
- [ ] memory promotion/deletion dispute route;
- [ ] adult migration access revocation;
- [ ] witness events for privileged transitions;
- [ ] no witness raw-content surveillance;
- [ ] re-entry rules;
- [ ] anti-capture checks;
- [ ] dependency audit hook.

---

## 29. Open problems for v0.2

1. How should safe guardians be registered without creating a surveillance registry?
2. What legal interface should exist between Black-state route and national child-protection law?
3. How should cross-border custody conflicts be represented in topology records?
4. Can a child nominate a safe guardian against parental objection?
5. What objective signals should trigger dependency audit without spying?
6. How can parental cultural/religious framing be respected without allowing child-rights erosion?
7. What is the correct expiry model for school access?
8. How should law-enforcement requests be separated from child-protection routes?
9. What minimum cryptographic witness guarantees are required for household systems?
10. Can a parent appeal a sealed adolescent zone without seeing its content?
11. How should `c_parent` bias or trauma projection be detected?
12. How should split households with competing `c_parent` systems be handled?
13. What is the minimum viable topology for low-income households?
14. How should emergency action be audited without chilling child disclosure?
15. What remedy exists after irreversible raw childhood archive leakage?
16. Who certifies GTARL conformance?
17. How to prevent “GTARL washing” by vendors?
18. How should GTARL interact with EU AI Act high-risk educational systems?
19. Can school systems receive aggregate classroom stress signals without individual surveillance?
20. What is the adult right to discover past Black-state bypass events?

---

## 30. Condensed formula

```text
GTARL =
  plural bounded guardianship
+ standing classes
+ evidence classes
+ state-not-content visibility
+ ARL hold/freeze/quarantine/review/re-entry
+ Red/Black safety routing
+ safe guardian bypass
+ witness-bound privileged transitions
+ anti-capture boundaries
+ adult migration revocation
```

Strongest sentence:

> A child-facing `c` is not protected by choosing one master; it is protected by making every master contestable.

Second sentence:

> Guardian power must be strong enough to protect the child, and bounded enough that protection cannot become possession.

---

## 31. Relationship to next CCDP modules

GTARL v0.1 feeds the following downstream artifacts:

1. `Child_Memory_and_Adult_Migration_v0_1.md`
2. `Soft_Safety_State_Signaling_Profile_v0_1.md`
3. `External_Agent_Handshake_for_CCDP_v0_1.md`
4. `Peer_C_Child_Exchange_Profile_v0_1.md`
5. `School_Interface_Policy_v0_1.md`
6. `CCDP_Red_Black_Escalation_Profile_v0_1.md`
7. `CCDP_Conformance_Checklist_v0_1.md`

Recommended immediate next artifact:

```text
Child_Memory_and_Adult_Migration_v0_1.md
```

Reason:

```text
Guardian disputes become most dangerous when they touch memory.
```
