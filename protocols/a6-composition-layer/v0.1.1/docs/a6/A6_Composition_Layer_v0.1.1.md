# A6 Composition Layer v0.1.1

## Hybrid / Federated Anchor Composition Profile for A6 in `c = a + b`

**Status:** Draft / boundary profile / DOI-ready release candidate
**Version:** 0.1.1
**Date:** 2026-06-18
**Layer:** Ontology / standing boundary / composition discipline / L3-L4 compatibility guard
**Parent stack:** `c = a + b` / Anchor Class Boundaries / SER / AGL / ARL / DEA / EA-L4 / L4 Reality Boundary / Jurisdiction-Bounded Interop
**Language:** RFC 2119 / BCP 14 keywords are used in their ordinary protocol sense: MUST, SHOULD, MAY, MUST NOT.

**Relationship to Anchor Class Boundaries:** This profile is the canonical home of the A6 composition layer. `Anchor Class Boundaries v0.2.1` remains self-contained and may summarize A6 in Section 12, but detailed composition behavior is governed by this profile. Where Section 12 and this profile differ in detail, this profile controls A6 composition behavior. A future boundaries revision MAY shrink Section 12 to a short pointer to this profile.

**Revision note (v0.1.1, this profile):**
1. `A6-EXIT` and `A6-SPLIT` are kept as distinct operational modes: `A6-EXIT` is revoke-and-continue; `A6-SPLIT` is freeze-and-escalate. Ordinary participant exit MUST NOT silently freeze or seize the whole composition.
2. ARL escalation is narrowed for exit: disputed or high-impact exit routes affected compartments to review; unaffected parts MAY continue inside their mapped scope.
3. A mandatory Resource and Custodian Map is added to match the witness packet field `resource_and_custodian_map_hash`.
4. Nested A6 participation is treated as high-risk until recursive A6 limits are formally defined.
5. An open question is recorded (Section 21) on whether A5 (civic / institutional) is itself an operator-like jurisdictional modifier rather than a pure object anchor class — the same observation already made for A6. This is flagged, not resolved.

---

## 0. Executive summary

This profile formalizes the A6 class from Anchor Class Boundaries.

A6 is not a normal anchor class.

A6 is an **anchor-composition state** over A0–A5.

Compact formula:

```text
A6 = mapped composition over anchor classes
     not merged standing
     not merged memory
     not merged identity
     not merged authority
```

A6 exists because real deployments often cross clean boundaries:

```text
human + organization
family + business
lab + lab
clinic + research network
robot fleet + company
city registry + contractor
cross-border team + local infrastructure
```

The danger is not technical connection.

The danger is treating technical connection as if it created a single accountable subject.

Core rule:

> A6 may connect anchors.
> It must not melt them.

---

## 1. Purpose

This profile defines minimum discipline for hybrid and federated anchor configurations in `c = a + b` systems.

Its purpose is to prevent six boundary errors:

1. treating federation as unified standing;
2. treating shared infrastructure as shared authority;
3. treating shared memory as merged identity;
4. treating cross-border operation as borderless activation;
5. treating organizational custody as personal consent;
6. treating A6 as a loophole around A0–A5 requirements.

This profile does not make A6 easier.

It makes A6 harder to abuse.

---

## 2. Scope

### 2.1 In scope

This profile applies when a `c`, `c_candidate`, `c`-adjacent system, local node, agentic hive, or continuity-bearing infrastructure involves:

- more than one anchor class;
- more than one accountable actor;
- more than one jurisdiction;
- multiple organizations;
- human + organization hybrids;
- household + business overlap;
- robot / vehicle / device fleets under institutional control;
- federated clinical, research, educational, civic, or archival systems;
- shared memory stores across anchor boundaries;
- delegated authority across anchor boundaries;
- cross-boundary Experience Artifact custody, admission, disclosure, or reuse.

### 2.2 Out of scope

This profile does not define:

- legal personhood of `c`;
- legal personhood of any anchor;
- public-law activation;
- treaty recognition;
- universal data ownership;
- universal consent transfer;
- inheritance doctrine;
- cross-border legal compliance in full;
- public procurement or sectoral regulation;
- moral status;
- consciousness;
- final A6 product certification.

Applicable law remains external to this protocol.

---

## 3. Core position

A6 is a composition layer.

It is not a standalone authority source.

A6 MUST NOT create standing by aggregation.

A6 MUST NOT create authority by network topology.

A6 MUST NOT create identity by shared embeddings, shared logs, shared vector stores, shared keys, shared dashboards, shared agents, or shared governance language.

The minimum safe interpretation is:

```text
each participant keeps its own anchor boundary
shared operation is explicitly mapped
externalization is narrowed by default
review is triggered when maps conflict
```

A6 sits over the object classes A0–A5. It is an operator on anchor boundaries, not an additional boundary of the same kind. (See Section 21, open issue on A5, for the related question of whether A5 is also operator-like rather than a pure object class.)

---

## 4. Definitions

### 4.1 A6 composition

A mapped relation among two or more anchor boundaries where memory, action, authority, review, or externalization crosses or may cross class boundaries.

### 4.2 Participating anchor

An anchor boundary admitted into an A6 composition.

A participating anchor MAY be A0, A1, A2, A3, A4, A5, or another already-mapped A6 only if recursion is explicitly bounded.

Until recursive A6 limits are formally defined, nested A6 participation MUST be treated as high-risk. A nested A6 MAY be inspected, referenced, or reviewed, but MUST NOT be used for cross-boundary externalization unless its recursion depth, participating anchors, standing maps, authority maps, memory maps, exit rules, and split rules are explicitly witnessed.

Canonical rule:

```text
Nested A6 is review-first, not externalize-first.
```

### 4.3 Base anchor class

The underlying anchor class of a participant before composition.

Examples:

```text
A0: individual human
A1: household
A2: organization
A3: biological non-human / ecological
A4: embodied operational
A5: civic / institutional
```

### 4.4 Standing map

A record specifying who has standing for which action, memory compartment, sensor source, Experience Artifact, disclosure path, dispute, review, and revocation.

### 4.5 Authority map

A record specifying who may authorize, refuse, delegate, revoke, pause, freeze, externalize, or deny each action class.

### 4.6 Memory compartment

A bounded memory region with defined source, visibility, retention, reuse, deletion, export, witness, and dispute rules.

### 4.7 Federation

A relation among distinct anchors that permits bounded exchange without merged identity.

### 4.8 Composition event

An event that creates, modifies, narrows, expands, splits, exits, or terminates an A6 composition.

### 4.9 Exit (participant exit)

A composition event in which one participant leaves while the composition continues for the remaining participants. Exit is a **revoke-and-continue** event: the exiting participant's scope is revoked and its rights narrow, but the composition persists for the others. (See Section 12.)

### 4.10 Split (composition split / fork)

A composition event in which the composed boundary breaks into parts and no part inherits the whole by default. Split is a **freeze-and-escalate** event: externalization is frozen by default and the matter is routed to review. Exit and split MUST NOT be treated as the same operation. (See Section 12.)

### 4.11 Degrade target

The narrower class or mode to which the system falls back when A6 mapping fails.

---

## 5. A6 composition modes

Every A6 operation MUST declare one primary mode and MAY declare secondary modes.

| Mode | Name | Meaning | Default posture |
|---|---|---|---|
| `A6-COMPOSE` | Bounded composition | Several anchors participate in a defined joint operation | Allow only inside mapped scope |
| `A6-FEDERATE` | Federation | Distinct anchors exchange bounded claims, references, messages, summaries, or artifacts | No identity merge |
| `A6-DELEGATE` | Delegation | One anchor grants another actor scoped operational authority | Revocable / witnessed |
| `A6-HYBRID` | Hybrid anchor boundary | Human, household, organization, institution, biological, or operational anchors overlap | High review load |
| `A6-XJ` | Cross-jurisdictional composition | Anchor, operator, hardware, affected parties, or records cross legal envelopes | Fail closed on uncertainty |
| `A6-EXIT` | Participant exit | One participant leaves; the composition continues for the rest | **Revoke-and-continue**: revoke exiting scope, narrow its rights, persist composition |
| `A6-SPLIT` | Composition split / fork | The composed boundary breaks into parts; no part inherits the whole | **Freeze-and-escalate**: externalization freeze by default, route to review |
| `A6-DEGRADE` | Degradation | A6 falls back to narrower local classes | Preferred safe response |
| `A6-DENY` | Denial | A6 operation is refused because standing cannot be mapped | Required where mapping fails |

Modes are operational labels.

They are not legal categories.

They are not maturity grades.

`A6-EXIT` and `A6-SPLIT` are distinct modes with distinct default postures. A single participant leaving (exit) MUST NOT trigger a full-composition externalization freeze by default; a break-up of the composition (split) MUST.

---

## 6. Mandatory A6 maps

A6 MUST define the following maps before any cross-boundary externalization, privileged action, memory merge, Experience Artifact admission, or jurisdiction-sensitive operation.

### 6.1 Participating anchor map

Minimum fields:

```text
participant_id
base_anchor_class
accountable boundary
authorized representatives
operator
custodian
delegate list
subject classes affected
status
```

### 6.2 Standing map

Minimum fields:

```text
participant_id
standing_scope
action_classes
memory_compartments
EA_classes
disclosure_classes
dispute_scope
review_route
expiration
```

### 6.3 Authority map

Minimum fields:

```text
who may authorize
who may refuse
who may pause
who may freeze
who may revoke
who may externalize
who may export
who may delete
who may deny
who may escalate to ARL
```

### 6.4 Memory compartment map

Minimum fields:

```text
compartment_id
source_anchor
base_anchor_class
content class
visibility
retention
reuse limit
externalization rule
third-party exposure
EA eligibility
witness requirement
dispute state
exit behavior
```

### 6.5 Sensor map

Minimum fields:

```text
sensor_id
sensor owner / operator
observed environment
affected parties
local-only fields
redaction fields
never-externalize fields
retention window
review requirement
```

### 6.6 Jurisdiction map

Minimum fields:

```text
anchor location
hardware location
operator location
custodian location
affected-party location
record storage location
external recipient location
sectoral regulation flags
cross-border restriction flags
activation / block rule
```

### 6.7 Experience Artifact map

Minimum fields:

```text
candidate_EA_id
source anchor
source boundary
provenance
third-party exposure
consequence linkage
lawful acquisition basis
admissibility class
disclosure scope
reuse scope
dispute status
anti-gaming / synthetic laundering risk
```

### 6.8 Revocation, exit, and split map

Minimum fields:

```text
participant_id
revocation authority
revocation method
revocation effect
memory after exit
EA after exit
delegate after exit
keys after exit
logs after exit
pending disputes
exit effect (revoke-and-continue)
split / fork effect (freeze-and-escalate)
fork inheritance policy
fallback class
```


### 6.9 Resource and custodian map

Minimum fields:

```text
resource_id
resource_class
provider
payer
owner
operator
custodian
key_custodian
access_scope
cost_exposure
billing_path
credential_scope
revocation_route
failure_mode
witness_requirement
```

A6 MUST NOT treat resource custody, payment, operation, or key control as anchor standing by default.

This map is required because A6 compositions often fail through practical control rather than formal authority: the party paying the bill, holding the key, operating the node, or storing the logs may gain de facto power unless those roles are named and bounded.

---

## 7. Default decision rules

### 7.1 Intersection rule

Where multiple anchors participate, permission defaults to the narrowest mapped scope.

```text
allowed_scope = intersection(mapped_authority,
                             mapped_standing,
                             mapped_memory,
                             mapped_sensor,
                             mapped_jurisdiction,
                             mapped_EA_rights)
```

No participant receives the union of all permissions by default.

### 7.2 Compartment rule

A6 SHOULD default to compartmentalized continuity, not merged identity.

Memory compartments remain separate unless a specific merge is authorized, witnessed, scoped, reversible where possible, and reviewable.

### 7.3 No silent inheritance rule

Anchor rights do not silently transfer across:

```text
employment change
family change
company merger
lab closure
farm ownership change
robot sale
institutional status change
jurisdiction change
technical migration
fork / backup / restore
```

### 7.4 No technical-standing rule

Technical federation does not create standing.

Examples that do not create standing by themselves:

```text
shared vector database
shared dashboard
shared agent bus
shared key store
shared repository
shared witness log
shared cloud tenant
shared P2P route
shared robot fleet controller
```

### 7.5 Fail-closed rule

If standing, authority, memory, sensor, EA, or jurisdiction cannot be mapped, A6 MUST choose:

```text
A6-DEGRADE
A6-DENY
review_submission
local_custody_only
inspection_only_non_transferable
```

### 7.6 Conflict-resolution status (reserved)

Where lawfully mapped scopes of distinct participants conflict and the conflict cannot be resolved by the intersection rule (7.1), the resolution algebra is **not yet formalized** in this version. Until it is, A6 MUST NOT invent a resolution. It MUST `A6-DEGRADE` or `A6-DENY` and route to review (Section 10). No "majority", "consensus", or "primary participant wins" rule is asserted by default. (See Section 21, open issues 4 and 7.)

---

## 8. A6 admission test

Before an A6 relation is admitted, the system MUST answer:

```text
Which base anchor classes participate?
Who has standing for each action?
Which authority is original and which is delegated?
Which memory compartments remain separate?
Which sensors cross participant boundaries?
Which records include third parties?
Which jurisdiction blocks or narrows externalization?
Who can revoke the composition?
What happens when one participant exits?
What happens if the composition splits or forks?
What is the degrade target?
Which ARL route receives disputes?
```

If any answer is unavailable, stale, contested, or internally inconsistent, the operation MUST NOT externalize.

---

## 9. Witness packet

A conforming A6 operation SHOULD emit a witness packet before cross-boundary memory access, privileged action, externalization, EA admission, or jurisdiction-sensitive transfer.

Minimum packet:

```text
a6_event_id
composition_mode
participating_anchor_ids
base_anchor_classes
authority_basis
standing_map_hash
memory_compartment_map_hash
sensor_scope_hash
jurisdiction_map_hash
resource_and_custodian_map_hash
EA_scope_hash
revocation_paths
exit_policy          (revoke-and-continue)
split_fork_policy    (freeze-and-escalate)
review_route
created_at
expires_at
```

The witness packet is not a legal license.

It is a record that the system did not pretend a technical connection was an accountable boundary.

---

## 10. ARL escalation triggers

A6 MUST route to ARL or an equivalent review layer when:

- standing is disputed;
- a participant exit is disputed;
- a participant exit affects shared memory compartments, pending EA candidates, keys, delegates, unresolved externalization, jurisdiction-sensitive records, or resource/custodian control;
- a participant requests externalization over another participant's objection;
- memory compartments collide;
- EA admission is contested;
- a delegate acts beyond scope;
- jurisdictional status changes;
- third-party exposure is detected after capture;
- a fork or split is proposed;
- a custodian claims authority;
- a technical operator claims anchor standing;
- a participant attempts to convert federation into merged identity;
- mapped scopes of distinct participants conflict and intersection (7.1) does not resolve them;
- an A6 map is missing, stale, contradictory, or unverifiable.

Default ARL posture depends on the event class.

For `A6-EXIT`:

```text
revoke exiting participant scope
freeze only affected cross-boundary compartments where needed
preserve local evidence
prevent unauthorized memory merge
preserve revocation paths
allow unaffected composition to continue inside mapped scope
route disputed parts to review
```

For `A6-SPLIT`:

```text
freeze cross-boundary externalization
preserve local evidence
prevent memory merge
preserve revocation paths
route the whole split boundary to review
```

For unresolved standing, authority, jurisdiction, EA, or resource/custodian conflict:

```text
A6-DEGRADE or A6-DENY
local_custody_only where preservation is needed
inspection_only_non_transferable where review is needed
```

---

## 11. Experience Artifact rules

A6 MUST treat Experience Artifact admission as narrower than recording.

A candidate EA MUST NOT be admitted because:

- several participants recorded it;
- several systems summarized it;
- a federation transmitted it;
- a shared model embedded it;
- a corporate dashboard displayed it;
- a public-facing system received it;
- a robot, sensor, or agent captured it.

A6 EA admission requires mapped source boundary, standing, lawful acquisition, third-party exposure check, witnessability, consequence linkage, disclosure scope, reuse scope, and dispute state.

Canonical rule:

```text
recorded != admitted
admitted != disclosed
disclosed != reusable
federated != owned
```

---

## 12. Exit, split, and fork handling

A6 MUST define what happens when composition changes or breaks. Exit and split are **distinct** events with **distinct** default postures.

### 12.1 Exit — one participant leaves, composition continues

`A6-EXIT` is a **revoke-and-continue** event.

```text
the exiting participant's authority and standing are revoked
the exiting participant's access narrows to its own retained boundary
the composition persists for the remaining participants
shared compartments are re-scoped, not destroyed
the exit is witnessed and routed to review if disputed
```

Exit does NOT, by default, freeze the whole composition. It narrows the rights of the leaving participant and re-maps what remains.

### 12.2 Split / fork — the composition breaks apart

`A6-SPLIT` is a **freeze-and-escalate** event.

```text
externalization is frozen by default
no resulting part inherits the whole by default
raw cross-boundary records are frozen pending review
shared witnesses, keys, and delegates are re-evaluated
derived `c` trajectories are treated as new, not continuous, unless proven
the matter is routed to ARL
```

### 12.3 Minimum exit/split questions

```text
Which memory compartments remain with which anchor?
Which summaries may be retained?
Which raw records must be frozen?
Which witnesses remain shared?
Which keys are revoked?
Which delegates lose scope?
Which EA candidates become disputed?
Which externalizations are blocked?
Which derived `c` trajectories are new rather than continuous?
```

### 12.4 Defaults

```text
exit  -> revoke-and-continue   (exiting participant loses scope; composition persists)
split -> freeze-and-escalate   (externalization frozen; nothing inherits the whole by default)
fork  -> does not inherit standing by default
continuity does not carry anchor authority across composition boundaries
```

---

## 13. L4 constraints

A6 increases real-world load.

It adds:

- more actors;
- more sensors;
- more rooms;
- more devices;
- more logs;
- more keys;
- more jurisdictions;
- more third-party exposure;
- more review work;
- more failure surfaces;
- more opportunities for authority laundering.

Therefore A6 MUST be treated as an L4 scaling problem, not only an ontology problem.

A6 systems SHOULD reduce ambition when review load, human cognitive load, cost, latency, storage, key management, jurisdictional uncertainty, or safety risk exceeds mapped capacity.

---

## 14. Corpus bridge set

### 14.1 Explicit bridge — `c = a + b` ↔ anchor composition

`c = a + b` requires an accountable anchor boundary. A6 does not replace that boundary. It maps how several anchor boundaries interact without turning technical federation into merged standing.

### 14.2 Hidden bridge I — SER continuity ↔ exit / split handling

A `c` may preserve internal continuity through an A6 event while losing, narrowing, or fragmenting external rights. Continuity can survive an exit or a split. Standing may not.

### 14.3 Hidden bridge II — L4 reality boundary ↔ operational load

Every A6 expansion increases physical and administrative load: more logs, more sensors, more storage, more key custody, more human review, more legal exposure, more exit cases, and more failure surfaces.

### 14.4 Hidden bridge III — anatomy / organ boundaries

An organism can share blood, signals, microbes, tools, food, and environment with other organisms without becoming one body. Fusion without membranes is not health. It is pathology. A6 needs membranes: compartments, gates, valves, immune-like review, and clear pain signals when one part is injured.

---

## 15. Earth paragraph

A6 is the difference between wiring several buildings together and pretending they have one owner, one breaker panel, one insurance policy, one fire exit, and one diary drawer. A hospital network, a family office, a lab cluster, a drone fleet, and a city archive can all exchange signals. That does not mean the same person may read every record, authorize every action, or carry memory from one room into another. The more pipes connect, the more labels, valves, meters, locks, and emergency stops matter. And when one building is sold off or the shared block is broken up, you do not hand the new owner every old key by default — you change the locks, freeze the shared meter, and decide room by room what was ever really theirs.

---

## 16. Worked examples

### 16.1 Family + business `c`

Risk:

```text
A1 household memory enters A2 business use.
```

Required response:

```text
separate personal, household, and business compartments
block automatic EA promotion
require explicit export authority
freeze disputed family records
```

### 16.2 Cross-lab research `c`

Risk:

```text
A2 + A2 federation creates false shared standing.
```

Required response:

```text
federated claims only
no raw-state access by default
institution-specific authority map
publication / disclosure route mapped separately
```

### 16.3 Federated clinical `c`

Risk:

```text
A2 / A5 medical records combine with research use.
```

Required response:

```text
sectoral jurisdiction check
patient / subject boundary protection
research-use compartment
no EA disclosure without standing and lawful basis
```

### 16.4 Multi-robot operational `c`

Risk:

```text
A4 fleet control appears to create autonomous operational legitimacy.
```

Required response:

```text
owner / operator map
emergency stop per device and fleet
liability path
sensor third-party handling
physical safety review
```

### 16.5 Cross-border project `c`

Risk:

```text
participants treat protocol compatibility as legal activation.
```

Required response:

```text
jurisdiction map
local-only default
externalization block on uncertainty
review route before transfer
```

### 16.6 Human + organization hybrid `c`

Risk:

```text
A0 personal continuity becomes corporate memory asset.
```

Required response:

```text
personal memory remains A0
project memory may be A2
shared summaries require source boundary
exit path protects the human anchor
```

### 16.7 Participant exit vs composition split

Exit case:

```text
One lab leaves a cross-lab federation (A6-EXIT).
-> revoke that lab's standing and access
-> re-scope shared compartments
-> the federation continues for the others
-> no full freeze required by default
```

Split case:

```text
The cross-lab federation itself dissolves (A6-SPLIT).
-> freeze cross-boundary externalization
-> no successor inherits the whole by default
-> route to review; treat derived trajectories as new
```

---

## 17. Red-line failures

A system or document fails this profile if it claims or implies:

1. A6 is a merged super-anchor;
2. federation creates unified standing;
3. shared memory creates merged identity;
4. shared infrastructure creates authority;
5. organizational custody creates personal consent;
6. household proximity creates business permission;
7. robot fleet continuity creates legal subjecthood;
8. cross-border routing bypasses jurisdiction;
9. forked continuity inherits all source-anchor rights;
10. Experience Artifacts become admissible because a federation recorded them;
11. a custodian is an owner by default;
12. a technical operator is an anchor by default;
13. exit does not narrow access rights;
14. a single participant's exit silently freezes or seizes the whole composition;
15. a composition split lets some part inherit the whole by default;
16. disputed A6 memory may be externalized before review;
17. a participant conflict is resolved by an unstated "majority" or "primary wins" rule;
18. A6 can be used to launder synthetic, staged, or ambiguous records into clean Experience Artifacts.

---

## 18. Conformance checklist

A6 conformance SHOULD be reviewed through these questions:

```text
Are all participating anchors named?
Are base anchor classes named?
Is there a standing map?
Is there an authority map?
Are memory compartments separated?
Are sensor fields mapped?
Are third-party exposures mapped?
Are jurisdiction blockers mapped?
Are EA rights narrowed by default?
Are revocation and exit paths clear?
Is exit (revoke-and-continue) distinguished from split (freeze-and-escalate)?
Is fork inheritance denied by default?
Is a degrade target defined?
Is ARL escalation defined?
Is witness output defined?
Is merged identity explicitly denied?
Is participant-conflict resolution either mapped or explicitly deferred to review?
```

If the answer to any critical question is no, A6 MUST NOT externalize.

---

## 19. Canonical sentences

```text
A6 is not a merged super-anchor.
```

```text
A6 is an anchor-composition state over A0–A5.
```

```text
Technical federation does not create standing.
```

```text
Shared memory does not create shared authority.
```

```text
A6 defaults to compartmentalized continuity, not merged identity.
```

```text
Exit narrows the leaver; split freezes the whole.
```

```text
If A6 cannot map standing, it must degrade or deny.
```

```text
A6 may connect anchors. It must not melt them.
```


---

## 20. Release metadata

Recommended citation:

```text
Kotov, Ivan. A6 Composition Layer v0.1.1: Hybrid / Federated Anchor Composition Profile for A6 in c = a + b. Bruxelles, 2026.
```

Suggested repository path:

```text
protocols/anchor-composition/A6_Composition_Layer_v0.1.1.md
```

Suggested DOI deposit type:

```text
Technical note / protocol / research artifact
```

This profile does not create legal personhood, legal authority, product certification, clinical validity, or public-law activation. It defines protocol discipline for anchor-composition boundaries.

---

## 21. Open issues

1. Define formal JSON schema for A6 witness packets.
2. Define machine-readable standing map format.
3. Define safe recursive A6 limits when an A6 participant joins another A6 composition. Until then, nested A6 remains review-first and must not externalize across boundaries without explicit witnessed recursion bounds.
4. Define conflict resolution when lawful jurisdictions disagree (currently reserved; see 7.6 — fail-closed until formalized). Candidate frameworks to evaluate: lexicographic priority vs. lattice / greatest-lower-bound of mapped scopes; the intersection rule (7.1) is the current safe floor, not a full resolution algebra.
5. Define A6 public wording for non-technical audiences.
6. Define A6 red-team tests for authority laundering.
7. Define minimum evidence requirements for A6-FEDERATE vs A6-COMPOSE.
8. Define relationship between A6 and post-anchor continuity.
9. Define interaction with SYNAPS-like exchange protocols.
10. Define audit profiles for high-risk A6 clinical, civic, and embodied deployments.
11. **A5 status (open).** Determine whether A5 (civic / institutional) is itself an operator-like *jurisdictional modifier* over object classes, rather than a pure object anchor class — mirroring the observation that A6 is an operator, not a class. If confirmed, the taxonomy may resolve into two tiers: object anchor classes (A0–A4) and operators over them (a jurisdictional modifier, and the A6 composition layer). `Anchor Class Boundaries v0.2.1` is intentionally left as a boundary-summary pending this determination.

---

## 22. Closing statement

A6 is where clean taxonomy meets messy deployment.

The correct response is not to pretend the mess is clean.

The correct response is to map the mess, narrow authority, preserve compartments, witness crossings, distinguish exit from split, and fail closed when standing cannot be shown.

```text
map first
compose second
externalize last
```
