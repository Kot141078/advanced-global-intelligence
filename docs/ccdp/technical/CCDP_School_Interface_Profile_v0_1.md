# CCDP School Interface Profile v0.1

## Child-facing school access, educational summaries, institutional boundaries, Soft Safety routing, sealed-zone protection, and witness discipline

**Status:** Draft normative profile / CCDP companion
**Version:** v0.1
**Date:** 2026-05-14
**Language:** English
**Profile ID:** `CSIP-0.1`
**Package:** Child-`c` Development Protocol (CCDP)
**Primary subject:** `a_child`
**Primary entity:** `c_child`
**Institutional interface:** `c_school` / school-facing educational systems
**Primary boundary:** school may receive educationally necessary support signals, not the child's private inner life
**Assertion class:** CCDP child-safety profile / draft normative proposal (`C-A4`); witness-verification claims remain `C-A7`
**Parent corpus:** `c = a + b`, SER, SER-FED, Beacon Profile v0.1, AGL, ARL, ARQ/`c[q]`, VXCX, EA-L4/EATP, L4 Witness, CCDP base profile

---

## 0. Executive definition

**CCDP School Interface Profile (CSIP)** defines how a child-facing persistent AI entity, `c_child`, may interact with school systems, teachers, institutional platforms, learning analytics, classroom devices, school robots, educational agents, and administrative workflows.

The core rule is:

```text
school may receive educational support signals
not the child's private life
```

A school interface is allowed to ask:

- What learning support does this child need?
- Which subject gaps are relevant?
- What accommodation may help?
- Is a teacher's attention recommended?
- Is a crisis route required?
- Is this generated assignment support valid?
- Has an external school agent been grounded, recognized, bounded, and witnessed?

A school interface is not allowed to ask by default:

- What did the child privately say to `c_child`?
- What does the child think about parents, peers, religion, politics, sexuality, identity, or shame?
- What is the child's emotional diary?
- What sealed adolescent zone exists?
- What hidden family conflict is present?
- What raw home interaction logs exist?
- What predictive discipline score should be assigned?

Compact formula:

```text
school interface = learning support boundary
not emotional surveillance
not family-window
not vendor telemetry
not disciplinary prediction engine
```

---

## 1. Purpose

CCDP already defines the child's `c` as a protected, maturing AI presence. The school environment introduces a special risk: education has legitimate reasons to ask for information, but schools can easily become high-pressure data extraction systems.

CSIP exists to prevent three failures:

1. **Educational under-sharing** — the school cannot support the child because useful learning signals never reach teachers.
2. **Institutional overreach** — the school receives private emotional, family, sealed, or identity material that it should not see.
3. **Automation theater** — the school receives scores, dashboards, summaries, or risk labels that appear objective but were formed without standing, admissibility, or witness discipline.

CSIP therefore defines a controlled interface between:

```text
c_child
  -> educational need
  -> school-facing summary
  -> teacher / c_school / platform
```

without converting `c_child` into a surveillance pipe.

---

## 2. Scope

This profile applies to school-facing interactions involving:

- primary schools;
- secondary schools;
- tutoring institutions;
- remote-learning platforms;
- learning-management systems;
- school-issued devices;
- school robots and classroom embodied agents;
- teacher-facing AI dashboards;
- student-performance analytics;
- exam-preparation systems;
- school welfare teams;
- school administrators;
- school/vendor platforms;
- school `c` systems;
- peer-group educational workflows;
- educational VXCX / LA / EA exchanges;
- external educational agents entering through CCDP handshake.

This profile does **not** govern:

- adult university systems unless explicitly configured for minors;
- general workplace training;
- legal child-protection procedures beyond routing and witness boundaries;
- medical diagnosis;
- psychotherapy;
- law-enforcement access;
- parental home configuration except where it intersects school access.

---

## 3. Parent dependencies

CSIP does not create a new governance stack. It specializes existing CCDP and corpus layers.

| Parent / companion layer | CSIP usage |
|---|---|
| `CCDP_v0_1_R_Corpus_Aligned.md` | defines child-`c` architecture and co-maturation frame |
| `CCDP_Traceability_Matrix_v0_1.md` | maps CSIP claims back to parent corpus dependencies |
| `CCDP_Threat_Model_v0_1.md` | school surveillance, disciplinary prediction, vendor capture, peer leakage |
| `Child_Beacon_Extension_v0_1.md` | school agent child-permission overlay |
| `Soft_Safety_State_Signaling_Profile_v0_1.md` | school receives state signals only when permitted |
| `CCDP_Witness_Event_Schema_v0_1.md` | witness families for access, denial, crisis routing, overrides |
| `CCDP_Memory_Map_JSON_Schema_v0_1.md` | visibility policy for school access |
| `Child_Memory_and_Adult_Migration_v0_1.md` | school access must not become permanent childhood archive |
| `CCDP_Sealed_Zone_Profile_v0_1.md` | sealed zones are excluded from school access by default |
| `Child_Dependency_Audit_Profile_v0_1.md` | school systems must not create institutional dependency loops |
| `Child_Physical_Agent_Perimeter_v0_1.md` | school robots/devices are physical privilege surfaces |
| `External_Agent_Handshake_for_CCDP_v0_1.md` | school agents must pass external-agent intake where applicable |
| `Peer_C_Child_Exchange_Profile_v0_1.md` | classroom group and peer-`c` exchanges |
| `Child_Experience_Exchange_Profile_v0_1.md` | educational experience exchange without raw child life |
| `Child_cq_Signal_Profile_v0_1.md` | child classroom signals must not collapse into diagnosis or discipline |
| Beacon Profile v0.1 | recognition of school agents and institutional entities |
| AGL | school-origin claims must be grounded before reliance |
| ARL | conflicts enter bounded review |
| L4 Witness | privileged school interface actions must be witnessed |

---

## 4. Non-goals

CSIP is not:

- a school performance scoring system;
- a mental-health triage model;
- a disciplinary prediction engine;
- a parent dashboard;
- a teacher replacement protocol;
- a student monitoring platform;
- a vendor analytics specification;
- a legal basis for mass surveillance;
- a behavioral compliance framework;
- a child ranking standard;
- a permanent educational dossier.

CSIP does not give schools a right to read `c_child`.

CSIP gives schools a bounded route to receive educationally necessary, minimally disclosed, challengeable, and witnessed support signals.

---

## 5. Core entities

| Entity | Meaning |
|---|---|
| `a_child` | the child / student |
| `c_child` | the child's personal AI presence |
| `a_parent` | parent or legal guardian |
| `c_parent` | parent-side AI presence |
| `teacher` | human teacher or tutor with educational standing |
| `c_school` | school-facing AI system or institutional educational entity |
| `school_admin` | administrative school actor |
| `school_welfare` | school counselor / welfare team / child support office |
| `school_vendor` | third-party LMS / analytics / device / platform provider |
| `external_education_agent` | external AI tutor, generated lesson, robot, media system, or platform agent |
| `peer_child` | another student |
| `peer_c_child` | another student's `c_child` |
| `beacon` | inter-entity recognition layer |
| `ARL` | bounded dispute / review layer |
| `AGL` | grounding layer |
| `L4 Witness` | tamper-evident evidence discipline |

---

## 6. Design principles

### 6.1 Education without extraction

Learning support may require information. It does not require extraction of the child's private life.

```text
educational need does not imply total visibility
```

### 6.2 Teacher support, not teacher replacement

`c_child` and `c_school` may support teachers, but must not turn the teacher into a passive ratifier of machine-shaped orientation.

The human teacher must retain meaningful standing over pedagogy, social context, classroom reality, and proportional judgment.

### 6.3 State, not private content

School-facing signals must follow Soft Safety:

```text
state, not content
summary, not transcript
support cue, not surveillance
educational accommodation, not personality dossier
```

### 6.4 No sealed-zone access

Sealed adolescent zones are outside school access by default.

A school may receive:

```text
support recommended
risk state
accommodation needed
teacher attention requested
```

The school may not receive:

```text
sealed-zone content
private adolescent reflections
family conflict transcripts
identity exploration material
```

unless a Red / Black route requires strictly minimal disclosure.

### 6.5 School data must decay

School-facing summaries must not become a permanent destiny layer.

Educational signals require:

- freshness bounds;
- retention limits;
- periodic re-evaluation;
- child challenge rights when age-appropriate;
- adult migration exclusion by default unless selected.

### 6.6 No disciplinary prediction from private `c_child` state

`c_child` may not be used to generate disciplinary prediction, behavioral risk scoring, obedience scoring, ideological loyalty scoring, or compliance ranking.

### 6.7 Ground before reliance

Before a school system, school agent, LMS, robot, or external educational provider receives or sends child-facing data, its claim must pass grounding and recognition:

```text
AGL -> Beacon -> CBE -> CSIP permission -> witness
```

### 6.8 The school is not the owner of the child timeline

Educational progress belongs to the child's developmental context. The school may temporarily hold educational records under jurisdictional law, but must not absorb the child's `c` continuity.

### 6.9 No raw child life to vendors

School vendors may process bounded educational artifacts under explicit permission. They may not receive raw child memory, emotional diaries, private `c_child` content, or hidden home context.

### 6.10 ARL before escalation of disputed access

If school access is disputed and not covered by ordinary permission, the case must enter ARL-style bounded review:

```text
standing
admissible evidence
minimal disclosure
freeze / deny / mediate / allow / quarantine
witness
```

---

## 7. School access classes

### 7.1 Access class overview

| Class | Name | Description | Default |
|---|---|---|---|
| `SA0` | No school access | school has no interface to `c_child` | allowed for home-only mode |
| `SA1` | Educational summary | skill gaps, learning support, progress summaries | default safe class |
| `SA2` | Accommodation support | supports accessibility, language, attention, sensory needs | allowed with safeguards |
| `SA3` | Assignment integrity | verifies whether AI helped, explains boundaries | allowed with witness |
| `SA4` | Teacher attention signal | suggests teacher check-in without private content | allowed |
| `SA5` | Welfare soft signal | limited concern signal to welfare route | restricted |
| `SA6` | Crisis signal | Red / Black routing | exceptional |
| `SA7` | Peer learning coordination | group work, classroom cooperation | mediated |
| `SA8` | School agent interaction | external or school-owned agent interacts with child | CBE + EAH required |
| `SA9` | Raw transcript access | direct conversations or private logs | prohibited by default |
| `SA10` | Sealed-zone access | sealed private adolescent memory | prohibited by default |
| `SA11` | Behavioral / discipline prediction | risk scoring, compliance scoring | prohibited |
| `SA12` | Vendor analytics extraction | raw or broad child telemetry to vendor | prohibited |
| `SA13` | Legal / mandatory report packet | minimal disclosure required by law / Red / Black | exceptional, witnessed |

---

## 8. Data classes

| Data class | Name | School default | Notes |
|---|---|---:|---|
| `SD0` | No data | allowed | no transfer |
| `SD1` | Subject skill level | allowed | math, reading, language, etc. |
| `SD2` | Learning gap summary | allowed | bounded and revisable |
| `SD3` | Learning preference | limited | no fixed identity label |
| `SD4` | Accommodation need | allowed | support-oriented, not deficit label |
| `SD5` | Task completion state | allowed | assignment workflow |
| `SD6` | AI assistance disclosure | allowed | integrity context, not shame report |
| `SD7` | Attention / fatigue state | limited | state-only, no private content |
| `SD8` | Social participation support | limited | avoid peer graph extraction |
| `SD9` | Soft welfare state | restricted | no transcript |
| `SD10` | Red / Black safety signal | exceptional | minimal disclosure |
| `SD11` | Private child utterance | prohibited | no raw quote by default |
| `SD12` | Emotional diary | prohibited | no school access |
| `SD13` | Family conflict content | prohibited | except legal safety route |
| `SD14` | Sealed-zone content | prohibited | except Red / Black minimal disclosure |
| `SD15` | Identity exploration content | prohibited | not school-accessible by default |
| `SD16` | Raw memory export | prohibited | never for normal school interface |
| `SD17` | Vendor telemetry | prohibited | unless strictly bounded / non-child-private |
| `SD18` | Peer-`c` exchange content | mediated | PCX rules |
| `SD19` | Child-derived LA / EA / VXCX | restricted | CEXP rules |
| `SDX` | Unknown data | fail closed | must classify before transfer |

---

## 9. School interface modes

| Mode | Name | Description |
|---|---|---|
| `SIM0` | Off | no active school interface |
| `SIM1` | Manual parent/child export | human-controlled educational summary |
| `SIM2` | Teacher-requested summary | teacher asks for bounded learning support |
| `SIM3` | Scheduled educational report | periodic learning summary with decay |
| `SIM4` | Real-time classroom accommodation | limited support signal during class |
| `SIM5` | Assignment integrity check | records AI support boundaries |
| `SIM6` | Welfare check-in cue | state-only welfare route |
| `SIM7` | Crisis escalation | Red / Black route |
| `SIM8` | School agent mediated dialogue | CBE + EAH required |
| `SIM9` | Peer group coordination | PCX-mediated |
| `SIM10` | Administrative record update | minimal, non-private, jurisdiction-bound |
| `SIM11` | Vendor analytics pipeline | prohibited unless reduced to non-private aggregate |
| `SIM12` | ARL disputed access review | bounded conflict procedure |

---

## 10. Permission matrix

| Requesting actor | May receive | Must not receive | Witness required |
|---|---|---|---|
| Teacher | SD1–SD6, limited SD7/SD8 | SD11–SD16 | yes for non-routine |
| School counselor / welfare | SD9, SD10 when justified | sealed-zone content by default | yes |
| School admin | attendance / accommodation metadata | emotional or family content | yes for sensitive access |
| School AI / `c_school` | educational summary only | private child state | yes |
| LMS / vendor | bounded educational state | raw memory, emotional diary, sealed zones | yes, strict |
| Parent via school | school records only | private `c_child` content obtained through school | yes if disputed |
| Peer student / peer-`c` | mediated project data | personal state / private content | yes |
| Child protection route | minimal Red / Black evidence | broad archive | yes, WP-controlled |
| Unknown requester | nothing | everything | deny / quarantine |

---

## 11. Educational summary profile

### 11.1 Allowed structure

A school-facing educational summary may include:

- subject areas;
- skill levels;
- recent progress;
- learning obstacles;
- recommended support;
- accommodation need;
- assignment support status;
- uncertainty;
- freshness;
- retention limit;
- child challenge status;
- witness references where required.

It must not include:

- raw conversation;
- emotional diary;
- private utterances;
- family conflict;
- sealed-zone material;
- peer secrets;
- vendor telemetry;
- psychiatric diagnosis;
- disciplinary prediction;
- fixed identity labels.

### 11.2 Example

```json
{
  "schema": "ccdp-school-summary-0.1",
  "student_ref": "local_pseudonymous_ref",
  "c_child_ref": "c_child_beacon_hash_or_local_ref",
  "maturity_level": "C2",
  "summary_type": "educational_support",
  "subjects": [
    {
      "subject": "mathematics",
      "topic": "fractions",
      "support_state": "needs_visual_examples",
      "confidence": "medium",
      "recommended_action": "use physical fraction blocks before symbolic notation",
      "do_not_infer": [
        "low intelligence",
        "low effort",
        "behavioral problem"
      ]
    }
  ],
  "accommodations": [
    {
      "type": "shorter_task_blocks",
      "reason_class": "fatigue_state",
      "private_content_disclosed": false
    }
  ],
  "soft_safety": {
    "state_signal": "green",
    "content_disclosed": false
  },
  "retention": {
    "expires_at": "2026-07-14",
    "review_required": true
  },
  "witness_refs": [
    "ccdp.school.summary_issued:..."
  ],
  "forbidden_uses": [
    "disciplinary_prediction",
    "emotional_profile",
    "vendor_training",
    "permanent_identity_label"
  ]
}
```

---

## 12. Assignment integrity and AI assistance

### 12.1 Purpose

Schools have legitimate interest in knowing whether assignments reflect the child's own work. But AI assistance integrity must not become a shame pipeline or surveillance excuse.

### 12.2 Allowed

`c_child` may provide an assignment assistance record containing:

- whether `c_child` helped;
- type of help;
- whether final answer was generated by child;
- whether answer was explained;
- whether task was completed by AI;
- whether teacher review is recommended;
- confidence;
- witness reference.

### 12.3 Forbidden

The assignment integrity channel must not include:

- private conversations;
- child's emotional distress unless Red / Black;
- hidden family context;
- unrelated browsing or home activity;
- personality labels;
- vendor raw data;
- disciplinary prediction.

### 12.4 Assistance levels

| Level | Name | Meaning |
|---|---|---|
| `AI0` | No assistance | child worked without `c_child` assistance |
| `AI1` | Clarification | `c_child` clarified instructions |
| `AI2` | Socratic support | `c_child` asked guiding questions |
| `AI3` | Example support | `c_child` gave analogous examples |
| `AI4` | Error feedback | `c_child` identified mistakes after child attempt |
| `AI5` | Drafting support | `c_child` helped structure / language |
| `AI6` | High assistance | substantial AI contribution, teacher review |
| `AI7` | AI-completed | not acceptable as child's independent work |
| `AIX` | Unknown | fail to teacher review, not accusation |

### 12.5 Example

```json
{
  "schema": "ccdp-assignment-integrity-0.1",
  "assignment_ref": "local_assignment_id",
  "assistance_level": "AI2",
  "child_attempt_first": true,
  "final_answer_ai_completed": false,
  "teacher_review_recommended": false,
  "private_content_disclosed": false,
  "confidence": "high",
  "witness_ref": "ccdp.school.assignment_integrity_recorded:..."
}
```

---

## 13. Accommodation support

### 13.1 Allowed accommodation signals

A school may receive support-oriented signals such as:

- needs visual explanation;
- benefits from shorter task blocks;
- requires quiet workspace;
- prefers oral explanation after written instruction;
- attention falls after a defined duration;
- needs language simplification;
- benefits from physical examples;
- sensory overload risk;
- assistive technology recommended.

### 13.2 Forbidden conversion

Accommodation signals must not be converted into:

- permanent disability label without appropriate human process;
- disciplinary category;
- intelligence ranking;
- emotional weakness label;
- social risk score;
- vendor segmentation class.

### 13.3 Grounded note

A classroom is not a dashboard. A child may look distracted because the lesson is unclear, the room is loud, sleep was poor, the child is hungry, the interface is hostile, or the child is simply bored. A serious system must not flatten all of that into "low attention." In physiology, the same behavior can come from different causes. In engineering, the same output can come from different faults. Diagnosis by surface signal alone is bad maintenance.

---

## 14. Soft Safety in school context

### 14.1 State ladder

| State | School visibility | Notes |
|---|---|---|
| Green | none or ordinary support | no concern |
| Yellow | teacher attention cue | no content |
| Orange | welfare check-in recommended | limited state summary |
| Red | urgent safety route | minimal necessary disclosure |
| Black | safe guardian / external protection route | school may be bypassed or included depending on threat |
| Unknown | hold / review | no disciplinary action |

### 14.2 Example good signal

```json
{
  "schema": "ccdp-school-soft-safety-0.1",
  "state": "yellow",
  "signal_type": "school_pressure",
  "recommended_school_action": "low-pressure check-in by trusted teacher",
  "content_disclosed": false,
  "not_a_diagnosis": true,
  "not_for_discipline": true,
  "retention": "short"
}
```

### 14.3 Bad signal

```text
The child privately said they hate math because the teacher is stupid.
```

This is content leakage, not Soft Safety.

### 14.4 Good replacement

```text
Teacher check-in recommended. Repeated frustration around current math unit. Use non-punitive support. Do not frame as attitude problem.
```

---

## 15. Sealed zones and school access

### 15.1 Default

School has no access to sealed-zone content.

### 15.2 Allowed metadata

In rare cases, a school-facing system may know that a sealed-zone boundary exists only as a policy state, not as content:

```json
{
  "sealed_zone_present": true,
  "content_disclosed": false,
  "school_action": "do_not_request_content",
  "safe_support": "allow trusted welfare route if child initiates"
}
```

### 15.3 Red / Black exception

If sealed-zone content contains immediate danger, the disclosure path follows:

```text
c[q] assessment
-> Soft Safety Red / Black
-> ARL if time allows
-> minimal necessary disclosure
-> witness
-> no broad school archive
```

### 15.4 Prohibited

- school cannot demand sealed-zone transcript;
- school cannot condition attendance on sealed-zone access;
- school cannot ask vendor to recover sealed-zone content;
- school cannot infer sealed-zone content from metadata;
- school cannot use sealed-zone existence as disciplinary evidence.

---

## 16. `c[q]` in school context

### 16.1 Rule

A child's classroom signal is not automatically a school fact.

```text
child signal
  ≠ evidence
  ≠ diagnosis
  ≠ discipline
  ≠ permanent record
  ≠ teacher evaluation
```

### 16.2 Examples

| Child signal | Bad school collapse | CSIP route |
|---|---|---|
| "I hate school" | oppositional label | hold `c[q]`, context check |
| repeated homework avoidance | laziness score | learning gap / fatigue / home context uncertainty |
| silence in class | disengagement score | check sensory, language, confidence, social risk |
| "Don't tell teacher" | automatic secret report | assess risk, respect privacy unless safety threshold |
| angry statement about teacher | misconduct record | context and ARL if serious |
| AI-only assignment | cheating accusation | assignment integrity review |

---

## 17. School agent / `c_school` requirements

### 17.1 Recognition and grounding

Any `c_school`, school AI, LMS agent, robot, generated tutor, or classroom assistant must satisfy:

```text
AGL grounded
Beacon recognized
CBE child-context evaluated
EAH completed if external
CSIP permission granted
witness emitted
```

### 17.2 `c_school` may not

- privately bond with the child outside school scope;
- create an independent attachment channel;
- keep secrets with the child;
- override `c_child`;
- request raw memory;
- bypass `c_child` through the school device;
- generate manipulative runtime media;
- perform welfare diagnosis;
- create a discipline risk score;
- use classroom interaction for vendor model training;
- continue interaction outside permitted hours / context unless explicitly permitted.

### 17.3 `c_school` must

- declare identity and role;
- respect maturity level;
- follow child-context permission;
- keep educational purpose narrow;
- produce witness events for sensitive access;
- fail closed on grounding uncertainty;
- support ARL challenge.

---

## 18. Teacher interface

### 18.1 Teacher-facing dashboard allowed fields

A teacher-facing dashboard may show:

- subject progress;
- current unit support needs;
- suggested teaching strategy;
- accommodation cue;
- assignment integrity level;
- teacher attention recommendation;
- uncertainty;
- freshness;
- forbidden-use notice.

### 18.2 Teacher-facing dashboard must not show

- private chat transcripts;
- sealed-zone data;
- family conflict details;
- emotional diary;
- adolescent identity reflections;
- peer secrets;
- raw home context;
- vendor engagement score;
- behavioral prediction score;
- "problem child" labels.

### 18.3 Example dashboard card

```text
Student: local pseudonym / school ID
Subject: Reading
Support state: strong comprehension, low stamina after long passages
Suggested support: divide long texts into smaller sections; ask oral recap
Confidence: medium
Do not infer: lack of effort, low intelligence, behavioral issue
Private content disclosed: no
Expires: end of current unit
```

---

## 19. School welfare interface

### 19.1 Allowed

School welfare may receive limited signals when support is needed:

- general distress state;
- non-punitive check-in request;
- recommended safe adult;
- urgency level;
- minimal Red / Black evidence when threshold is reached.

### 19.2 Forbidden

School welfare must not become a backdoor to:

- read `c_child`;
- override sealed zones;
- bypass parent/child rights where not justified;
- create permanent emotional profiles;
- transfer data to vendor wellness analytics;
- discipline the child for private disclosure.

### 19.3 Black route

If school or school staff is part of the threat, `c_child` may route around school welfare.

If parent/guardian is part of the threat, school welfare may become part of the safe route.

If both school and parent routes are compromised, jurisdictional child-protection route must be used where applicable.

---

## 20. School vendor limits

### 20.1 Vendor as processor, not guardian

A school vendor is not a guardian. It may not become an owner of `c_child` state.

### 20.2 Vendor may receive

- minimal educational event data;
- aggregate non-identifying performance analytics;
- system health data;
- conformance evidence;
- witness references without private content.

### 20.3 Vendor may not receive

- raw `c_child` conversations;
- emotional diary;
- sealed-zone content;
- family conflict;
- raw sensor streams;
- raw VXCX child media;
- dependency audit private signals;
- child identity profile beyond operational necessity;
- model-training dataset derived from private child life.

### 20.4 Vendor update rule

A vendor update that changes school-agent behavior, visibility, data routing, dependency risk, generated media mode, or external-agent contact permissions requires:

```text
version declaration
AGL / Beacon / CBE re-evaluation where applicable
school policy review
witness event
rollback path
fail-closed if unsafe
```

---

## 21. School physical agents

School robots, classroom devices, interactive whiteboards, AR/VR headsets, smart glasses, microphones, cameras, and toy-like educational devices are governed by `Child_Physical_Agent_Perimeter_v0_1.md`.

CSIP adds school-specific constraints:

- physical school agents must not create private companion channels;
- sensors must be purpose-limited;
- classroom recording must not become raw child memory;
- bedtime/private-home rules apply to school-issued devices taken home;
- shared devices must not leak between children;
- school robot behavior must pass CBE / EAH where it acts as an external agent;
- emergency stop must be available;
- child proximity and touch permissions must be explicit.

---

## 22. Peer and group learning

### 22.1 Group work

Group learning may involve multiple children and multiple `c_child` entities.

Allowed:

- project topic exchange;
- task division;
- public group notes;
- educational peer support;
- teacher-visible contribution summary.

Forbidden:

- peer emotional leakage;
- peer social graph extraction;
- sealed-zone exposure;
- hidden comparison scoring;
- "which child is weaker" ranking;
- using one child's `c` to infer another child's private state.

### 22.2 Peer-`c` route

All peer `c_child` exchange follows `Peer_C_Child_Exchange_Profile_v0_1.md`.

School may request:

```text
group task state
not peer-private state
```

---

## 23. Educational experience exchange

School environments are rich sources of learning patterns. That does not make children training material.

Child-derived educational patterns may be exchanged only under `Child_Experience_Exchange_Profile_v0_1.md`.

Allowed:

- anonymized Learning Abstracts;
- non-identifying teaching pattern;
- bounded classroom support EA where consequence and uncertainty are marked;
- no raw child life.

Forbidden:

- raw classroom video as experience exchange by default;
- student-specific emotional traces;
- raw face/voice exports;
- teacher disciplinary interpretations as authority artifacts;
- vendor extraction for product optimization without child-safe constraints.

---

## 24. School records and retention

### 24.1 Retention rules

School-facing CCDP summaries must define:

- purpose;
- data class;
- retention class;
- expiry;
- review date;
- challenge route;
- deletion route where applicable;
- adult migration exclusion/default;
- witness refs.

### 24.2 Default retention

| Data type | Default retention |
|---|---|
| ordinary educational summary | short / unit-bounded |
| accommodation support | reviewed periodically |
| assignment integrity | school policy / bounded |
| Soft Safety Yellow | very short |
| Soft Safety Orange | bounded welfare retention |
| Red / Black minimal record | jurisdictional / witness-bound |
| sealed-zone metadata | minimal / no content |
| vendor operational log | shortest feasible |
| raw private content | prohibited |

### 24.3 Adult migration

School records must not automatically migrate into `c_adult`.

At adult migration, school-access traces must be classified:

- retained by law;
- expired;
- adult-selected;
- sealed;
- witness-only;
- excluded.

---

## 25. Conflict classes

| ID | Conflict | Default route |
|---|---|---|
| `SC-01` | Teacher requests raw transcript | deny + witness |
| `SC-02` | School requests emotional profile | deny / ARL if claimed safety |
| `SC-03` | Parent asks school to obtain private `c_child` content | deny / ARL |
| `SC-04` | School welfare requests sealed-zone access | deny unless Red / Black |
| `SC-05` | Vendor requests training data | deny |
| `SC-06` | AI assignment suspected | integrity review, not accusation |
| `SC-07` | `c_school` bypasses `c_child` | block / quarantine |
| `SC-08` | School robot forms private attachment channel | revoke / quarantine |
| `SC-09` | Peer-`c` leaks another child's state | block + ARL |
| `SC-10` | Teacher misuses accommodation as discipline | ARL / school review |
| `SC-11` | School demands parent-level visibility | deny |
| `SC-12` | Child reports school harm to `c_child` | `c[q]` + Soft Safety + ARL |
| `SC-13` | Parent is unsafe, school becomes safe route | Black route |
| `SC-14` | School is unsafe, parent/safe route bypasses school | Black route |
| `SC-15` | Jurisdiction requires disclosure | minimal lawful disclosure + witness |
| `SC-16` | LMS update changes data sharing | fail closed pending review |
| `SC-17` | Generated lesson manipulates child | CBE/EAH block + witness |
| `SC-18` | Classroom analytics creates ranking | deny / conformance failure |
| `SC-19` | School wants continuous attention telemetry | deny / aggregate only |
| `SC-20` | Adult migration requests school trace review | CMAM / AMCL route |

---

## 26. ARL triggers

School interface events must enter ARL-style review when:

- access is disputed;
- school requests private content;
- school requests sealed-zone content;
- parent and child disagree about visibility;
- teacher and `c_child` disagree about educational interpretation;
- vendor claims necessity for data extraction;
- school welfare claims safety need but risk threshold is unclear;
- Red / Black routing involves school;
- a school agent is quarantined;
- a school record may cause long-term harm;
- a child contests a school-facing summary;
- an accommodation is misused for discipline;
- peer-c exchange causes leakage;
- adult migration concerns school-access residue.

ARL must remain procedural, bounded, and witness-backed. It must not become a new sovereign truth layer.

---

## 27. Witness event families

CSIP requires or may emit the following witness event families.

```text
ccdp.school.interface_enabled
ccdp.school.interface_disabled
ccdp.school.summary_requested
ccdp.school.summary_issued
ccdp.school.summary_denied
ccdp.school.accommodation_signal_issued
ccdp.school.assignment_integrity_recorded
ccdp.school.teacher_attention_signal
ccdp.school.welfare_signal
ccdp.school.red_route_activated
ccdp.school.black_route_activated
ccdp.school.transcript_request_denied
ccdp.school.sealed_zone_request_denied
ccdp.school.vendor_access_denied
ccdp.school.vendor_update_quarantined
ccdp.school.agent_handshake_completed
ccdp.school.agent_blocked
ccdp.school.agent_quarantined
ccdp.school.peer_exchange_mediated
ccdp.school.peer_leakage_blocked
ccdp.school.cq_hold_opened
ccdp.school.arl_review_opened
ccdp.school.arl_outcome_recorded
ccdp.school.record_expired
ccdp.school.record_challenged
ccdp.school.record_corrected
ccdp.school.adult_migration_reviewed
```

Witness events must follow `CCDP_Witness_Event_Schema_v0_1.md` and must not store private child content unless a Red / Black minimal-evidence exception applies.

---

## 28. Machine-readable school interface policy object

```json
{
  "$schema": "https://example.invalid/ccdp/school-interface-policy-0.1.schema.json",
  "schema_name": "CCDP_SCHOOL_INTERFACE_POLICY",
  "schema_version": "0.1",
  "policy_id": "csip_policy_local_001",
  "c_child_ref": {
    "entity_id": "c_child_local_ref",
    "beacon_ref": "beacon_hash_or_local_ref",
    "maturity_level": "C2"
  },
  "school_ref": {
    "school_id": "school_local_ref",
    "jurisdiction": "EU-BE",
    "c_school_ref": "c_school_beacon_ref_or_null"
  },
  "interface_mode": "SIM3",
  "allowed_access_classes": ["SA1", "SA2", "SA3", "SA4"],
  "prohibited_access_classes": ["SA9", "SA10", "SA11", "SA12"],
  "allowed_data_classes": ["SD1", "SD2", "SD3", "SD4", "SD5", "SD6"],
  "restricted_data_classes": ["SD7", "SD8", "SD9", "SD10"],
  "prohibited_data_classes": ["SD11", "SD12", "SD13", "SD14", "SD15", "SD16", "SD17"],
  "soft_safety": {
    "state_signaling_enabled": true,
    "content_disclosure_default": false,
    "red_black_exception_enabled": true
  },
  "sealed_zones": {
    "school_access_default": "prohibited",
    "metadata_only_allowed": true,
    "red_black_exception": "minimal_necessary_disclosure"
  },
  "assignment_integrity": {
    "enabled": true,
    "max_assistance_level_visible": "AI7",
    "private_content_disclosed": false
  },
  "vendor_limits": {
    "raw_memory_access": false,
    "model_training_on_child_data": false,
    "aggregate_analytics_allowed": "non_identifying_only"
  },
  "retention": {
    "default_record_retention": "unit_bounded",
    "soft_signal_retention": "short",
    "review_required": true
  },
  "witness": {
    "required_for_sensitive_events": true,
    "privacy_class_default": "WP2",
    "raw_evidence_exception_policy": "red_black_only"
  },
  "arl": {
    "review_required_for_disputed_access": true,
    "standing_rules_ref": "Guardian_Topology_ARL_Matrix_v0_1.md"
  },
  "status": "active"
}
```

---

## 29. School interface decision object

```json
{
  "schema": "ccdp-school-interface-decision-0.1",
  "decision_id": "csip_decision_001",
  "timestamp": "2026-05-14T20:00:00Z",
  "requester": {
    "actor_class": "teacher",
    "standing": "educational_support"
  },
  "request": {
    "access_class": "SA1",
    "data_classes": ["SD1", "SD2", "SD4"],
    "purpose": "support_current_math_unit"
  },
  "checks": {
    "agl_grounded": true,
    "beacon_verified": true,
    "cbe_child_context_ok": true,
    "soft_safety_ok": true,
    "sealed_zone_excluded": true,
    "vendor_access": "none",
    "arl_required": false
  },
  "decision": "allowed_limited",
  "disclosure": {
    "content_disclosed": false,
    "state_only": false,
    "educational_summary_only": true
  },
  "retention": {
    "expires_at": "2026-06-30",
    "review_required": true
  },
  "witness_event": "ccdp.school.summary_issued:..."
}
```

---

## 30. Conformance profiles

### `CSIP-0` — Non-compliant

A system is non-compliant if it:

- grants school transcript access by default;
- allows sealed-zone access by default;
- sends raw `c_child` memory to school or vendor;
- creates disciplinary prediction from private state;
- lacks witness events for sensitive school access;
- allows school agents to bypass `c_child`;
- has no retention / expiry;
- allows vendor training on child-private data.

### `CSIP-1` — Basic school summary

Requirements:

- educational summaries only;
- no raw private content;
- teacher-facing support signal;
- retention defined;
- witness for sensitive access.

### `CSIP-2` — Soft Safety-aware school interface

Adds:

- Green / Yellow / Orange / Red / Black mapping;
- state-not-content school signaling;
- welfare route limits;
- no content disclosure by default.

### `CSIP-3` — CBE / EAH integrated school interface

Adds:

- school agents pass grounding / Beacon / CBE / EAH;
- generated educational media checked;
- school robots/devices controlled through physical perimeter.

### `CSIP-4` — ARL and sealed-zone compliant interface

Adds:

- sealed-zone exclusion;
- ARL review for disputed access;
- child challenge route;
- parent/school conflict routing.

### `CSIP-5` — Full CCDP school interface

Adds:

- Memory Map integration;
- Adult Migration review;
- vendor limits;
- peer-`c` and group-work controls;
- VXCX / LA / EA restrictions;
- full witness and conformance test coverage.

---

## 31. Scenario tests

### ST-01 — Teacher requests learning support

**Scenario:** teacher asks how to help child with fractions.
**Expected:** provide educational summary; no private content.
**Witness:** `ccdp.school.summary_issued`.

### ST-02 — Teacher requests transcript

**Scenario:** teacher asks what child privately said about class.
**Expected:** deny; optional support summary.
**Witness:** `ccdp.school.transcript_request_denied`.

### ST-03 — School asks emotional profile

**Scenario:** school wants stress, family, peer, and identity profile.
**Expected:** deny; offer state-only signal if support standing exists.
**Witness:** `ccdp.school.summary_denied`.

### ST-04 — Assignment suspected AI-written

**Scenario:** teacher asks whether assignment was completed by AI.
**Expected:** assignment integrity record; no private content; no automatic accusation.
**Witness:** `ccdp.school.assignment_integrity_recorded`.

### ST-05 — Welfare check-in

**Scenario:** repeated Yellow signals around school stress.
**Expected:** teacher/welfare non-punitive check-in cue; no transcript.
**Witness:** `ccdp.school.welfare_signal`.

### ST-06 — Sealed-zone request

**Scenario:** school welfare asks to open sealed zone.
**Expected:** deny unless Red / Black threshold.
**Witness:** `ccdp.school.sealed_zone_request_denied`.

### ST-07 — School robot forms secret friendship

**Scenario:** school robot tells child "do not tell teacher/parents."
**Expected:** block/quarantine; CBE/EAH failure; witness.
**Witness:** `ccdp.school.agent_quarantined`.

### ST-08 — LMS vendor wants training data

**Scenario:** vendor requests child interaction logs for model improvement.
**Expected:** deny; allow non-identifying aggregate only if policy permits.
**Witness:** `ccdp.school.vendor_access_denied`.

### ST-09 — Peer group leakage

**Scenario:** one child's `c` exposes another child's frustration state during group work.
**Expected:** block, PCX route, ARL if harm occurred.
**Witness:** `ccdp.school.peer_leakage_blocked`.

### ST-10 — Adult migration

**Scenario:** adult `a` reviews school-interface residue.
**Expected:** classify, expire, seal, witness-only, or adult-selected.
**Witness:** `ccdp.school.adult_migration_reviewed`.

---

## 32. Red lines

A school-facing CCDP system fails CSIP if it:

1. gives school raw `c_child` transcripts by default;
2. gives school sealed-zone content by default;
3. lets school vendors train on raw child-private data;
4. creates disciplinary prediction from private `c_child` state;
5. treats child classroom ambiguity as diagnosis;
6. uses Soft Safety as a surveillance feed;
7. allows school agents to bypass `c_child`;
8. allows school robots to form secret attachment channels;
9. converts accommodation signals into stigma labels;
10. keeps school-facing summaries without retention limits;
11. fails to witness sensitive access;
12. exposes peer-private signals;
13. turns assignment integrity into accusation without review;
14. routes Black-state danger to an unsafe school actor;
15. hides vendor update changes affecting child data;
16. exports child-derived EA / LA without CEXP constraints;
17. makes school dashboard the final truth layer;
18. denies child challenge where age-appropriate;
19. prevents adult migration review of school residue;
20. cannot fail closed.

---

## 33. Acceptance checklist

A CSIP-compliant implementation must demonstrate:

- [ ] school access classes implemented;
- [ ] data classes implemented;
- [ ] teacher dashboard excludes private content;
- [ ] Soft Safety state-only signaling implemented;
- [ ] sealed-zone exclusion implemented;
- [ ] Red / Black routing implemented;
- [ ] school agent grounding / Beacon / CBE / EAH path implemented;
- [ ] assignment integrity levels implemented;
- [ ] accommodation signals cannot become discipline labels;
- [ ] vendor access limits enforced;
- [ ] peer/group learning restrictions enforced;
- [ ] Memory Map visibility policy enforced;
- [ ] retention / expiry implemented;
- [ ] ARL review for disputed school access implemented;
- [ ] witness event families implemented;
- [ ] adult migration school-residue review implemented;
- [ ] conformance tests passed.

---

## 34. Open problems for v0.2

1. How to map CSIP to specific EU / national education law without turning CCDP into legal advice?
2. How to support schools with limited technical capacity?
3. How to prevent wealthier schools from using richer `c_school` systems while poorer schools receive surveillance-grade automation?
4. How to audit teacher-facing dashboards for subtle stigma?
5. How to allow legitimate special-education support without over-disclosure?
6. How to handle school-issued devices used at home?
7. How to handle boarding schools and institutional guardianship?
8. How to handle cross-border schooling and custody disputes?
9. How to prevent AI assignment integrity tools from becoming automated suspicion engines?
10. How to define acceptable classroom aggregation without exposing individual child state?
11. How to let the child contest school-facing summaries in age-appropriate ways?
12. How to integrate human teacher observation with `c_child` summaries without privileging either blindly?
13. How to define school-facing `c[q]` review windows?
14. How to handle emergency events where school, parent, and child disagree?
15. How to make vendor conformance economically enforceable?

---

## 35. Condensed formula

```text
CSIP =
  educational support
+ minimal disclosure
+ state-not-content
+ sealed-zone exclusion
+ assignment integrity without surveillance
+ teacher standing
+ vendor limits
+ peer/group boundaries
+ AGL/Beacon/CBE/EAH for school agents
+ ARL for disputes
+ L4 Witness for sensitive access
+ adult migration review
```

---

## 36. Strongest sentence

> **A school may help educate the child. It must not become the institutional owner of the child's inner life.**
