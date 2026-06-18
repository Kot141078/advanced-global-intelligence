# Anchor Class Boundaries v0.2.1

## Protocol-facing taxonomy for `a` in `c = a + b`

**Status:** Draft / boundary note
**Version:** 0.2.1
**Date:** 2026-06-18
**Layer:** Ontology / standing boundary / L3-L4 compatibility guard
**Parent stack:** `c = a + b` / SER / L4 Reality Boundary / AGL / ARL / DEA / EA-L4 / EATP / Jurisdiction-Bounded Interop
**Language:** RFC 2119 / BCP 14 keywords are used in their ordinary protocol sense: MUST, SHOULD, MAY, MUST NOT.

**Revision note v0.2.1:** Section 12 is reduced to a stable A6 summary and pointer. Detailed A6 operational behavior is governed by `A6 Composition Layer v0.1.1`. This revision distinguishes `A6-EXIT` from `A6-SPLIT` and does not create legal personhood, public authority, merged identity, or post-anchor sovereignty.

---

## 0. Purpose

This document defines a compact taxonomy of possible anchor classes for `a` in the formula:

```text
c = a + b
```

Its purpose is not to expand legal claims, create new rights, or define public law.

Its purpose is to prevent a boundary error:

> treating every possible `a` as if it had the same standing, authority,
> sensor boundary, liability exposure, and continuity consequences as an
> individual human anchor.

The original formula identifies `a` as the experiential, limiting, memory-bearing, responsible side of the `c = a + b` relation. In the narrow case, `a` is an individual human. In broader deployments, `a` MAY appear as a household, organization, institution, biological subject, machine-embodied operational subject, or hybrid accountable boundary.

This document gives names to those cases so that they can be reviewed without confusion.

---

## 1. Core position

Anchor class determines the protocol-facing boundary of `c`.

It affects:

- who may authorize;
- who may stop;
- who bears consequence;
- whose memory is in scope;
- what sensor perimeter exists;
- what third-party exposure is created;
- which jurisdictional envelope applies;
- how Experience Artifacts may be admitted, held, disclosed, or refused.

**Hard rule:**

> A change in anchor class is not a cosmetic change.
> It is a standing, authority, memory, and jurisdictional event.

---

## 2. Out of scope

This document does **not** define:

- legal personhood of `c`;
- legal personhood of non-human anchors;
- post-anchor sovereignty;
- inheritance doctrine;
- universal clone / fork / descendant taxonomy;
- public regulation of AI systems;
- rights against states;
- corporate duties;
- treaty design;
- cross-border legal recognition;
- universal ownership of Experience Artifacts.

This document classifies anchor classes for internal protocol discipline only.

Applicable law remains external to this protocol.

---

## 3. Anchor, operator, delegate, and subject

The following roles MUST NOT be collapsed.

| Term | Meaning | Boundary warning |
|---|---|---|
| `a` / anchor | The accountable experiential or continuity boundary from which `c` is formed | Not every user, device, owner, or operator is automatically `a` |
| Operator | The person or process running infrastructure for `c` | Operation does not automatically create anchor standing |
| Delegate | A bounded agent, service, tool, or process acting under scoped authority | Delegation does not create sovereignty |
| Subject | A person, organism, organization, machine, or collective affected by observation or action | Being affected does not automatically make the subject the anchor |
| Custodian | A party holding memory, logs, keys, artifacts, or infrastructure | Custody is not ownership and not standing by default |

**Hard rule:**

> Anchor standing, operational control, data custody, and delegated execution are distinct.

---

## 4. Minimum anchor test

A proposed anchor class MUST be tested against five boundaries before a `c` relation is treated as valid.

### 4.1 Accountable boundary

There MUST be a defined accountable boundary capable of receiving consequence, review, and lawful exposure.

Questions:

```text
Who can be addressed?
Who can be notified?
Who can answer?
Who can be sanctioned or constrained where law applies?
```

### 4.2 Authority boundary

There MUST be a defined authority path for permission, refusal, delegation, and stop.

Questions:

```text
Who may authorize memory writes?
Who may authorize external action?
Who may pause or freeze operation?
Who may revoke a delegate?
Who may deny disclosure?
```

### 4.3 Memory boundary

There MUST be a defined memory perimeter.

Questions:

```text
Whose continuity is being preserved?
Whose history is in scope?
Which records are private?
Which records are shared?
Which records are third-party exposure?
```

### 4.4 Sensor boundary

There MUST be a defined sensor perimeter.

Questions:

```text
Which devices feed c?
Which environments are observed?
Who else may be captured?
What is local-only?
What may be redacted?
What may never be externalized by default?
```

### 4.5 Jurisdiction boundary

There MUST be a defined jurisdictional envelope.

Questions:

```text
Where does the anchor exist?
Where is the hardware?
Where are operators located?
Where are affected parties located?
Which legal envelope activates or blocks externalization?
```

If any boundary is unclear, the system SHOULD fail closed to the narrowest local mode.

Recommended defaults:

```text
local_custody_only
inspection_only_non_transferable
review_submission
deny
```

---

## 5. Anchor class taxonomy

This taxonomy is protocol-facing. It does not assert that every class is equally mature, equally lawful, or equally deployable in every jurisdiction.

| Class | Name | Typical form | Default maturity | Main risk |
|---|---|---|---|---|
| A0 | Individual human anchor | One human `a` | Canonical / primary | Overreach from assistance into hidden control |
| A1 | Household or family anchor | Shared domestic continuity boundary | Draft / bounded | Conflicting members, children, guests, private rooms |
| A2 | Organizational anchor | Company, lab, school, clinic, team | Draft / bounded | Bureaucratic hiding of responsibility |
| A3 | Biological non-human or ecological anchor | Animal, colony, ecosystem, farm organism set | Reserved / experimental | Anthropomorphic standing, weak consent, proxy abuse |
| A4 | Embodied operational anchor | Vehicle, robot, station, vessel, industrial line | Reserved / operational | Confusing machine custody with accountable anchorhood |
| A5 | Civic or institutional anchor | City office, public archive, hospital, museum, registry | Reserved / jurisdiction-heavy | Protocol language drifting into public law |
| A6 | Hybrid or federated anchor-composition state | Multi-party, cross-device, cross-entity boundary | Reserved / high-risk | Standing ambiguity, jurisdiction conflict, identity merge, fork-like drift |

---

## 6. A0 — Individual human anchor

A0 is the primary and least ambiguous anchor class.

```text
A0 = one accountable human anchor
```

In A0, `c` is bound to the memory, limits, responsibility, consent, and continuity of an individual human `a`.

A0 MAY support:

- personal memory;
- personal agent delegation;
- personal documents;
- local witness logs;
- private decision support;
- bounded disclosure;
- verified Experience Artifact preparation;
- lawful externalization under the applicable jurisdiction.

A0 MUST preserve:

- explicit privilege boundaries;
- human stop authority;
- local raw-data protection by default;
- witnessability of high-impact actions;
- fail-closed behavior under unclear authority.

A0 MUST NOT be silently expanded into household, employer, institutional, or state-level standing.

---

## 7. A1 — Household or family anchor

A1 covers shared domestic continuity.

Examples:

```text
family c
household c
shared home memory c
domestic infrastructure c
```

A1 is not just A0 with more users.

A1 introduces conflicts between:

- adult members;
- children;
- guests;
- private rooms;
- shared devices;
- shared expenses;
- shared documents;
- household sensors.

A1 MUST define:

```text
member roles
private zones
shared zones
child/minor handling
guest exposure rules
sensor minimization
who can stop household-level functions
who can access shared memory
who can export anything outside the household
```

A1 SHOULD default to compartmentalization:

```text
personal memory remains personal
shared memory remains explicitly shared
third-party exposure remains local-only or redacted by default
```

A1 MUST NOT treat family proximity as universal consent.

---

## 8. A2 — Organizational anchor

A2 covers organizations such as companies, laboratories, schools, clinics, research groups, or teams.

A2 is an accountable institutional boundary, not a biological subject.

A2 MAY support:

- project continuity;
- document processing;
- operational memory;
- team agent supervision;
- internal review;
- bounded external disclosure;
- institutional Experience Artifact custody.

A2 MUST define:

```text
legal entity or accountable body
responsible officers or maintainers
role-based privileges
employee/member boundaries
client/patient/student data boundaries
termination and transfer rules
audit and retention policies
externalization authority
```

A2 MUST NOT use `c` language to hide ordinary responsibility.

A company, lab, school, or clinic MAY operate a `c`-like continuity system, but it MUST NOT use the ambiguity of `c` to evade responsibility for decisions, records, or harm.

**Hard rule:**

> Institutional anchoring increases the need for audit.
> It does not reduce accountability.

---

## 9. A3 — Biological non-human or ecological anchor

A3 covers cases where `a` is not an individual human but remains biological.

Examples:

```text
animal care c
farm organism-set c
colony / hive monitoring c
ecosystem restoration c
wildlife protection c
```

A3 is reserved / experimental.

A3 MAY be useful where machine cognition supports:

- care;
- monitoring;
- environmental continuity;
- welfare assessment;
- ecological memory;
- long-term observation.

A3 MUST NOT claim that non-human biological anchoring automatically creates legal personhood, consent equivalence, or human-like standing.

A3 requires a proxy authority path.

That path MAY involve:

- owner / guardian;
- caretaker;
- institution;
- regulator;
- conservation body;
- research ethics process;
- lawful local equivalent.

A3 MUST treat welfare, observation, and extraction as separate questions.

A3 MUST NOT convert biological presence into marketable Experience Artifacts by default.

---

## 10. A4 — Embodied operational anchor

A4 covers machine-embodied operational systems.

Examples:

```text
robot c
vehicle c
vessel c
drone fleet c
factory line c
remote station c
satellite / habitat operational c
```

A4 is not a claim that the machine is a legal subject.

A4 describes an operational continuity boundary where `c` maintains state, memory, constraints, privileges, and action discipline for a physical or cyber-physical system.

A4 MUST define:

```text
owner / operator
maintenance authority
emergency stop
physical perimeter
action envelope
safety limits
human override
liability path
sensor boundary
jurisdiction of operation
```

A4 MUST NOT treat autonomous operation as autonomous legitimacy.

A4 SHOULD be strongly L4-bound:

```text
energy
heat
wear
latency
safety
repair
physical damage
human injury risk
infrastructure failure
```

A4 requires stronger stop and containment rules than ordinary text-facing `c` deployments.

---

## 11. A5 — Civic or institutional anchor

A5 covers public or quasi-public continuity systems.

Examples:

```text
city archive c
public registry c
hospital continuity c
museum memory c
school district c
public infrastructure c
```

A5 is jurisdiction-heavy.

A5 MUST be treated as high-risk because it approaches public law, public records, public services, and collective exposure.

A5 MUST NOT be introduced as a private protocol substitute for:

- public law;
- public procurement;
- administrative procedure;
- public accountability;
- official records law;
- sectoral regulation.

A5 MAY use protocol language for internal discipline, but activation, authority, and disclosure remain governed by the applicable institution and jurisdiction.

**Hard rule:**

> A civic `c` is not a shadow government.
> It is an accountable information and continuity system inside an existing jurisdiction.

---

## 12. A6 — Hybrid or federated anchor-composition state

A6 covers multi-party and multi-boundary cases.

Examples:

```text
family + business c
cross-lab research c
federated clinical c
multi-robot operational c
cross-border project c
human + organization hybrid c
```

A6 is the highest ambiguity class in this taxonomy. It is also different from A0-A5 in kind.

A0-A5 describe anchor classes.

A6 describes an **anchor-composition state** over one or more underlying anchor classes.

Compact rule:

```text
A6 is not a merged super-anchor.
A6 is a mapped composition over A0-A5.
```

Detailed A6 composition behavior is governed by:

```text
A6 Composition Layer v0.1.1
Hybrid / Federated Anchor Composition Profile for A6 in c = a + b
```

This section is a boundary-summary only. Where this section and the A6 Composition Layer differ in operational detail, the A6 Composition Layer controls A6 behavior.

### 12.1 A6 summary rules

A6 MAY compose, federate, delegate between, or temporarily bind existing anchor classes.

A6 MUST NOT create unified standing, unified memory, unified identity, or unified authority merely because systems, databases, agents, organizations, or devices are technically connected.

Default summary rules:

```text
technical federation does not create standing
shared infrastructure does not create shared identity
shared memory does not create shared authority
shared sensor field does not create consent
shared project does not create EA rights
silence does not create delegation
absence does not create inheritance
continuity does not carry anchor rights across class boundaries
```

### 12.2 Exit and split

A6 MUST distinguish participant exit from composition split.

```text
A6-EXIT  = revoke-and-continue
A6-SPLIT = freeze-and-escalate
```

Exit narrows the leaving participant's authority and access; it does not freeze the whole composition by default.

Split breaks the composed boundary; cross-boundary externalization is frozen by default and no part inherits the whole by default.

### 12.3 Mandatory summary maps

Before any cross-boundary externalization, privileged action, memory merge, Experience Artifact admission, or jurisdiction-sensitive operation, A6 MUST define at least:

```text
participating anchors and base classes
standing map
authority map
memory compartment map
sensor map
jurisdiction map
Experience Artifact map
revocation, exit, and split map
resource and custodian map
degrade target
ARL escalation route
minimum witness packet
```

A6 MUST NOT proceed on the basis of a single global permission.

Permissions MUST be action-scoped, memory-scoped, sensor-scoped, jurisdiction-scoped, resource-scoped, and time-scoped.

### 12.4 A6 fail-closed rule

If any required map is missing, stale, disputed, internally inconsistent, or unverifiable, the system MUST choose one of:

```text
A6-DEGRADE
A6-DENY
review_submission
local_custody_only
inspection_only_non_transferable
```

### 12.5 A6 hard rule

> A6 may connect anchors.
> It must not melt them.

---

## 13. Class transition rules

Anchor class transitions MUST be explicit.

Examples of transition events:

```text
A0 → A1: a personal c becomes household-shared
A0 → A2: a personal c is imported into workplace context
A2 → A6: an organization joins a federation
A4 → A2: a robot/line becomes part of corporate operational memory
A1 → A0: a household member extracts personal memory
A2 → A5: an institutional system enters public-service use
```

A transition MUST trigger review of:

- authority;
- memory scope;
- disclosure scope;
- sensor scope;
- standing;
- jurisdiction;
- third-party exposure;
- EA custody;
- stop authority;
- audit obligations.

**Hard rule:**

> Continuity of `c` does not imply continuity of anchor rights across class transitions.

---

## 14. Anchor composition changes

Some anchors change composition.

Examples:

```text
family member leaves household
employee leaves company
company merges
lab project ends
robot is sold
farm changes owner
institution changes legal status
cross-border team dissolves
```

Composition change MUST NOT silently preserve old access rights.

A conforming system SHOULD emit a composition-change record when the anchor boundary changes.

Minimum record:

```text
old anchor class
new anchor class or modified composition
authority basis
memory compartments affected
externalization rights affected
review requirement
operator / custodian affected
timestamp
```

Where the change is disputed, the system SHOULD freeze externalization and route the issue to review.

---

## 15. Sensor and third-party implications

Anchor class directly affects sensor handling.

A0 may capture private human context.
A1 may capture household members and guests.
A2 may capture employees, clients, patients, students, vendors, or visitors.
A3 may capture animals, environments, caretakers, and researchers.
A4 may capture public roads, workplaces, homes, infrastructure, or bystanders.
A5 may capture public-service data and civil records.
A6 may combine several of these risks.

**Hard rule:**

> Being inside the sensor field of an anchor does not automatically make a person, organism, document, or event available for externalization.

A conforming system SHOULD distinguish:

```text
captured
logged
processed
remembered
abstracted
admitted as EA
disclosed
reused
transferred
```

These are separate states.

---

## 16. Experience Artifact implications

Anchor class affects EA admissibility.

A candidate EA MUST NOT be admitted only because a `c` recorded it.

EA admission SHOULD check:

```text
anchor class
anchor authority
source boundary
third-party exposure
provenance
witnessability
consequence linkage
lawful acquisition
disclosure scope
reuse scope
dispute status
anti-gaming / synthetic laundering risk
```

A class expansion from A0 to A1/A2/A5/A6 SHOULD narrow EA disclosure by default until standing and authority are clear.

**Hard rule:**

> Anchor expansion does not expand EA rights by default.

---

## 17. Jurisdiction and locality

`c` is not a borderless subject.

Anchor class must be read together with jurisdictional exposure.

Relevant factors MAY include:

```text
location of a
location of hardware
location of operator
location of custodian
location of affected parties
location of stored records
location of external recipient
sectoral regulation
cross-border restrictions
```

A conforming system MUST NOT infer legal activation from protocol compatibility.

If jurisdictional status is unclear, the system SHOULD fail closed to:

```text
local_custody_only
inspection_only_non_transferable
review_submission
deny
```

---

## 18. Standing and review

Anchor class informs standing, but does not settle all standing disputes.

Standing MUST be checked when:

- externalization is requested;
- memory access is disputed;
- EA admission is contested;
- a delegate acts beyond scope;
- anchor composition changes;
- a third party is affected;
- cross-border operation is attempted;
- a class transition occurs;
- a system claims authority from ambiguity.

ARL or an equivalent review layer SHOULD treat unclear anchor class as a threshold issue.

**Hard rule:**

> Review cannot assume the actor before the anchor boundary is known.

---

## 19. Failure modes blocked by this document

This document is intended to block:

- treating `a` as always one human when the deployment is not one human;
- treating every organization as if it were a human anchor;
- hiding responsibility inside a corporate or institutional `c`;
- treating technical custody as authority;
- treating sensor capture as consent;
- treating family proximity as permission;
- treating machine autonomy as legal legitimacy;
- treating protocol compatibility as public-law activation;
- treating anchor expansion as EA expansion;
- treating federated memory as merged identity;
- treating A6 as a merged super-anchor;
- treating participant exit as composition split;
- treating composition split as clean inheritance;
- laundering synthetic or staged records through ambiguous anchor classes.

---

## 20. Recommended canonical phrasing

### 20.1 Short form

> Anchor class determines the accountability boundary of `c`.

### 20.2 Public-safe form

> `c = a + b` does not require every `a` to be an individual human, but every non-trivial anchor class must define authority, memory, sensor, standing, and jurisdiction boundaries before expansion is allowed.

### 20.3 Anti-overclaim form

> Anchor taxonomy is not legal personhood. It is protocol discipline.

### 20.4 Fail-closed form

> If the anchor boundary is unclear, do not externalize.

---

## 21. Bridges

### Explicit bridge — `c = a + b` ↔ ARL / EA

The class of `a` changes the conditions under which memory, action, and Experience Artifacts may be reviewed. A personal `c`, a household `c`, an organizational `c`, and an embodied operational `c` may share protocol vocabulary, but they do not share identical standing, disclosure, or EA-admission conditions.

### Hidden bridge #1 — SER continuity ↔ jurisdiction-bounded interop

Continuity may remain internal while external rights change. A `c` can preserve its internal history across a move, merger, sale, family change, or organizational transition, while losing or narrowing externalization rights under the applicable jurisdictional envelope.

### Hidden bridge #2 — L4 reality boundary ↔ sensor economics

Anchor expansion increases real-world variety: more sensors, more people, more rooms, more devices, more legal exposure, more possible harm. This is not just an ontology problem. It is an L4 scaling problem. Every expanded anchor class increases cost, heat, storage, review load, trust risk, and failure surface.

---

## 22. Earth paragraph

A personal notebook, a family photo album, a company archive, a hospital record system, a tractor telemetry log, and a city registry are all “memory” in a loose sense. But nobody sane handles them under one rule. The paper may look similar, the database rows may look similar, and the embeddings may look identical to a vector store. The body knows the difference: a private diary, a child’s medical record, a factory fault log, and a public registry produce different consequences when exposed. Anchor class is the protocol’s way of not confusing a kitchen drawer with a court archive.

---

## 23. Read next

Recommended adjacent surfaces:

```text
advanced-global-intelligence/protocols/c_a_b_protocol_v1.1_L4_EN.md
advanced-global-intelligence/protocols/anchor-composition/A6_Composition_Layer_v0.1.1.md
advanced-global-intelligence/OPEN_QUESTIONS_AND_EXPLICIT_NON_CLAIMS.md
advanced-global-intelligence/CANONICAL_OWNERSHIP_AND_BOUNDARIES.md
advanced-global-intelligence/PRECEDENCE_AND_RESOLUTION.md
ester-reality-bound/protocol/identity_and_privileges.md
ester-reality-bound/docs/actor-grounding-layer/Actor_Grounding_Layer_v0.1.md
sovereign-entity-recursion/docs/arbitration-review-layer/Evidence_Admissibility_and_Standing_v0.1.md
advanced-global-intelligence/docs/economic-layer/README.md
advanced-global-intelligence/docs/economic-layer/Disclosure_Privacy_and_Reusability_Boundaries_v0.1.md
advanced-global-intelligence/docs/economic-layer/extensions/Jurisdiction_Bounded_Interop_Clause_v0.1.md
```

---

## 24. Closing statement

This document does not expand `c` into a legal person, a political actor, or a supranational subject.

It defines the minimum discipline required when `a` is not treated as a single individual human by default.

The stable rule is:

```text
anchor first
standing second
authority third
memory fourth
externalization last
```

Where the anchor class is unclear, the system should not become creative.

It should become quiet.
