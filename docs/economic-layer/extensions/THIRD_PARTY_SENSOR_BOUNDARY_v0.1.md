# Third-Party Sensor Boundary v0.1

## Protocol-facing boundary for third-party presence captured by `a` / `c` sensors

**Status:** Draft / boundary note
**Version:** 0.1
**Date:** 2026-05-11
**Layer:** L4 Reality Boundary / DEA / EA-L4 / EATP / Economic Layer / privacy membrane / identity and privileges / ARL
**Parent stack:** `c = a + b` / SER / L4 Reality Boundary / AGL / ARL / DEA / EA-L4 / EATP / Economic Layer / Jurisdiction-Bounded Interop / Raw Locality and Experience Refinery Profile
**Language:** RFC 2119 / BCP 14 keywords are used in their ordinary protocol sense: MUST, SHOULD, MAY, MUST NOT.

---

## 0. Purpose

This document defines a compact protocol-facing boundary for cases where `c` receives sensor, document, interaction, or environmental data that includes people, organisms, organizations, or subjects other than its own anchor `a`.

It exists to prevent a boundary error:

> treating third-party presence inside `a`'s sensor field as if it were automatically `a`'s raw material, memory, experience, evidence, or economic asset.

The practical problem is simple.

A serious `c` may observe the world through devices attached to `a`:

```text
phone
laptop
microphone
camera
calendar
messages
vehicle sensors
home sensors
wearables
robots
work tools
browser sessions
documents
payments
medical devices
industrial telemetry
```

Those channels often capture more than `a`.

They capture:

```text
family members
guests
children
patients
clients
employees
neighbors
co-workers
passersby
public officials
contractual counterparties
social contacts
animals
organizations
physical locations
shared documents
third-party devices
```

This document defines the internal protocol rule:

> `c` MAY process third-party exposure for local understanding, safety, memory, and lawful review, but third-party presence MUST NOT become externally transferable experience, training material, marketable EA, or unrestricted evidence by default.

---

## 1. Core position

Sensor capture is not consent.

Presence is not contribution.

Co-presence is not anchor standing.

Observation is not ownership.

Local memory is not externalization.

Redaction is not automatically anonymization.

Summary is not automatically safe.

A serious `c` MUST distinguish:

```text
perception
capture
recording
local interpretation
local memory
third-party exposure
redaction
abstraction
DEA / EA candidacy
evidence handling
oracle query
training contribution
economic circulation
lawful inspection
publication
reuse
```

These states MUST NOT be collapsed.

**Hard rule:**

> A third party appearing in `a`'s sensor field is not automatically raw material for `a`'s `c`.

**Second hard rule:**

> Third-party material MUST be marked before it is used in DEA / EA / LA, oracle calls, audit packets, economic artifacts, or external disclosures.

---

## 2. Out of scope

This document does **not** define:

- public law;
- universal privacy law;
- state regulation;
- corporate duties;
- surveillance law;
- employment law;
- medical confidentiality law;
- child-protection law;
- recording-consent law;
- data-protection law;
- law-enforcement procedure;
- legal personhood of `c`;
- legal ownership of third-party data;
- universal consent doctrine;
- universal right to inspect or erase records;
- universal EA pricing;
- post-anchor sovereignty;
- a market for bystander data.

Applicable law remains external to this protocol.

This document defines an internal protocol boundary only:

```text
how c should treat third-party presence before DEA / EA / LA / disclosure / oracle / training / economic circulation
```

---

## 3. Terms

| Term | Meaning | Boundary warning |
|---|---|---|
| Third party | Any person, organism, organization, device, or subject captured or affected but not identical with the anchor `a` | Not automatically part of `a`'s experience asset |
| Bystander | A third party incidentally captured without being a participant in the event | Bystander capture is high-risk for externalization |
| Co-participant | A third party actively participating in an interaction with `a` | Participation is not universal consent to reuse |
| Counterparty | A person or organization interacting through contract, work, service, dispute, sale, employment, care, or institutional relation | Counterparty material may be governed by external law or agreement |
| Protected party | A minor, patient, dependent, vulnerable person, confidential client, or otherwise high-risk subject | Stronger default restraint applies |
| Shared context | A place, document, channel, call, meeting, device, vehicle, home, office, platform, or environment involving multiple subjects | Shared context is not owned solely by one `c` |
| Sensor field | The region of reality captured by `a`'s devices, tools, logs, channels, or instruments | Sensor field is not authority field |
| Capture | Recording or ingesting data from the sensor field | Capture does not imply permission to disclose |
| Ephemeral perception | Short-lived processing without durable storage | Lower risk, but not risk-free if used for action |
| Durable record | Stored image, audio, video, transcript, log, biometric, location trace, document, or event record | Requires third-party marking when others appear |
| Externalization | Any movement outside local `c` custody, including cloud inference, oracle calls, sharing, publication, audit packet, training, sale, or federation | Externalization must be typed and scoped |
| Redaction | Removing, masking, transforming, suppressing, coarsening, or segmenting third-party material | Redaction is a control, not magic |
| Abstraction | Replacing raw detail with generalized learning content | Abstraction may still leak identity or context |
| Third-party marker | Metadata indicating that material includes third-party exposure | Absence of marker is not proof of absence |
| Consent signal | A recorded indication that a third party permits a specific mode of use | Consent is mode-specific and jurisdiction-sensitive |
| No-capture signal | A declared request or environmental signal that capture, storage, or disclosure is not permitted or is restricted | Must be treated as a stop / review trigger where applicable |
| Lawful hold | Retention required or justified by applicable law, contract, safety, dispute, audit, or preservation duty | Lawful hold does not imply reuse |

---

## 4. Boundary principle

The third-party boundary sits between raw locality and external admissibility.

The correct sequence is:

```text
raw sensor field
  -> local capture / perception
  -> third-party exposure detection
  -> third-party marker
  -> minimization / redaction / hold / reject / local-only
  -> DEA / EA / LA candidacy only if allowed
  -> admissibility / standing / receiver-mode check
  -> bounded disclosure or no disclosure
```

The incorrect sequence is:

```text
sensor saw it
  -> c remembers it
  -> it is experience
  -> it can be sold / trained / published / audited / federated
```

That sequence is invalid.

---

## 5. Sensor classes

A `c` SHOULD classify the sensor class before using captured material.

| Sensor class | Examples | Third-party risk |
|---|---|---|
| Visual | camera, screen recording, robot vision, dashcam, bodycam, doorbell camera | faces, bodies, documents, homes, locations, children, bystanders |
| Audio | microphone, call recording, meeting transcript, voice assistant | voices, identity, emotion, background speech, private-room leakage |
| Biometric | faceprint, voiceprint, gait, pulse, sleep, health signals | identity, health, protected data, inference beyond consent |
| Location / proximity | GPS, Bluetooth, Wi-Fi, vehicle telemetry, badge logs | co-location, social graph, workplace pattern, home exposure |
| Document / text | email, chat, notes, contracts, CVs, medical files, invoices | authorship, counterparties, confidential content, third-party identifiers |
| Transactional | payments, receipts, purchases, tickets, deliveries | habits, counterparties, location, economic profile |
| Social graph | contacts, messages, calendar, group membership, mentions | network inference and relational exposure |
| Environmental | home sensors, factory sensors, farm sensors, weather, soil, utilities | lower identity risk alone, but can reveal household or work patterns |
| Professional record | medical, legal, educational, employment, insurance, finance | high legal and ethical restriction |
| Machine / vehicle | robot logs, drone video, vehicle cameras, autonomous system telemetry | public-space and bystander exposure at scale |

**Hard rule:**

> The more a sensor can identify, locate, classify, or infer a person, the stronger the externalization restraint MUST be.

---

## 6. Context classes

The same sensor type has different meaning in different contexts.

A `c` SHOULD classify context before externalization.

| Context class | Description | Default posture |
|---|---|---|
| Private self-context | `a` alone, no third-party exposure | Raw-local default still applies |
| Shared household | family, partner, child, guest, roommate | local-only / consent-aware / child-sensitive |
| Private room | bedroom, bathroom, clinic room, therapy, confession, private office, confidential call | no externalization by default |
| Workplace / team | employees, colleagues, contractors, clients | scope-bound; work product distinct from personal exposure |
| Professional high-trust | medical, legal, education, clergy, care, social work | strict retention and disclosure restraint |
| Public / semi-public space | street, station, store, event, public building | public visibility does not imply unrestricted reuse |
| Online shared channel | group chat, forum, collaborative doc, meeting platform | platform visibility does not imply training or economic circulation |
| Regulated / critical infrastructure | hospital, airport, power plant, lab, vehicle fleet, factory, military zone | local rules and jurisdiction dominate |

**Hard rule:**

> Public-space capture is not automatically public-domain experience.

---

## 7. Third-party relationship classes

A `c` SHOULD classify the third-party relationship before use.

| Class | Description | Protocol warning |
|---|---|---|
| Incidental bystander | Appears in the background or is passively captured | Must not become marketable EA by default |
| Known participant | Friend, colleague, family member, meeting participant | Participation is mode-specific |
| Dependent / minor | Child, elder, dependent, protected or vulnerable party | Strongest default restraint |
| Professional subject | Patient, client, student, employee, applicant, customer | External law and fiduciary/confidential duties may apply |
| Contractual counterparty | Seller, buyer, landlord, tenant, insurer, employer, supplier | Documents may be usable for local memory, not automatically for training |
| Institutional actor | Official, agency, court, hospital, school, company | Public role may reduce some privacy claims but not all disclosure limits |
| Adversarial actor | Fraudster, attacker, harasser, intruder, malware operator | Safety/evidence handling may apply, but due process and law remain external |
| Non-human subject | Animal, ecological system, machine, robot, vehicle, farm, habitat | Still may expose human owners/operators/locations |

---

## 8. Capture states

Third-party exposure SHOULD be tracked through states.

| State | Name | Meaning | Default movement |
|---|---|---|---|
| T0 | No capture | No third-party data is captured | None |
| T1 | Ephemeral perception | Processed only for immediate local action; not durable | No externalization |
| T2 | Local raw capture | Durable raw record exists locally | Local-only by default |
| T3 | Structured local event | `c` interprets an event involving third-party exposure | Third-party marker required |
| T4 | Redacted local memory | Third-party material minimized or masked | May support local memory |
| T5 | Experience candidate | Candidate DEA / EA includes third-party involvement | Review required before admission |
| T6 | Reviewed artifact | Third-party exposure handled through redaction, consent, lawful basis, or admissibility rule | Scope-limited movement possible |
| T7 | Bounded disclosure | Artifact leaves local custody under declared receiver mode | Audit and receiver constraints required |
| T8 | Blocked / sealed / local-only | Material cannot move due to privacy, law, standing, uncertainty, protected-party risk, or dispute | No externalization |
| T9 | Lawful hold | Retention required for legal, safety, dispute, or audit reasons | Retention only; no reuse by default |

**Hard rule:**

> T2 does not imply T5. T5 does not imply T7.

---

## 9. Third-party exposure marker

Any material containing third-party exposure SHOULD carry a marker before it enters DEA / EA / LA / oracle / audit / economic-layer flows.

Minimum marker:

```yaml
third_party_presence: none | incidental | substantial | protected | unknown
third_party_role: bystander | participant | dependent | professional_subject | counterparty | institutional_actor | adversarial_actor | non_human_subject | mixed | unknown
sensor_class: visual | audio | biometric | location | document | transactional | social_graph | environmental | professional_record | machine_vehicle | mixed
context_class: private_self | household | private_room | workplace | professional_high_trust | public_space | online_shared | regulated_critical | unknown
capture_state: T0 | T1 | T2 | T3 | T4 | T5 | T6 | T7 | T8 | T9
consent_status: none | implied_for_interaction | explicit_for_local_memory | explicit_for_disclosure | explicit_for_training | disputed | not_applicable | unknown
no_capture_signal: true | false | unknown
redaction_required: true | false | unknown
externalization_allowed: none | local_only | oracle_redacted | audit_scoped | EA_scoped | LA_only | publication | unknown
receiver_mode: none | oracle | judge | auditor | counterparty | public | training | legal_request | federation | unknown
jurisdiction_marker: local | cross_border | unknown | blocked
arl_trigger: false | true | pending
```

The marker is not a legal conclusion.

It is a protocol-facing warning surface.

---

## 10. Material classes

Third-party exposure SHOULD be classified by material class.

| Material class | Examples | Default |
|---|---|---|
| Identifying material | face, name, address, voice, biometric, unique profile | local-only or redacted before movement |
| Sensitive material | health, finances, sexuality, religion, politics, children, legal disputes, employment status | strict restraint |
| Relational material | who met whom, when, where, under what context | local-only unless needed and scoped |
| Behavioral material | habits, mistakes, arguments, emotions, performance | high risk of misuse |
| Contextual material | home layout, workplace setting, device location, background documents | minimize before movement |
| Public-role material | public official action, public proceeding, published statement | still requires context and lawfulness checks |
| Machine-associated material | vehicle ID, robot log, device serial, farm telemetry | may expose owners/operators/locations |
| Environmental-only material | temperature, soil, weather, machine state without identity | lower risk, but not automatically unrestricted |

---

## 11. What may remain local

Third-party material MAY remain local when needed for:

- `a`'s memory;
- safety;
- household continuity;
- work continuity;
- technical debugging;
- fraud defense;
- dispute preservation;
- lawful records;
- accessibility;
- immediate assistance;
- personal context;
- bounded `c` self-consistency;
- DEA / EA candidate evaluation.

Local retention still requires discipline.

A `c` SHOULD apply:

```text
purpose limitation
retention limits
access controls
redaction where possible
delegation limits
no silent cloud movement
no training by default
no publication by default
```

---

## 12. What must not leave by default

The following MUST NOT leave local custody by default:

- raw audio containing third-party speech;
- raw video containing identifiable people;
- raw biometric signals of third parties;
- children or protected-party material;
- private-room material;
- medical, legal, educational, employment, financial, or care records involving third parties;
- screenshots of private messages;
- unredacted meeting transcripts;
- social graph inferences;
- location traces that reveal others;
- raw household or guest data;
- bystander material in public-space capture;
- third-party material captured through drones, robots, vehicles, or always-on devices;
- material under dispute;
- material with unclear jurisdictional status.

Externalization MAY occur only after scope, lawfulness, standing, redaction, consent, admissibility, or review conditions are satisfied.

---

## 13. Externalization modes

Externalization MUST be typed.

| Mode | Meaning | Third-party requirement |
|---|---|---|
| Local-only | No movement outside local `c` custody | Default for high-risk exposure |
| Oracle-redacted | External model receives minimized context | Redaction and no-training receiver mode SHOULD be used |
| Judge / ARL packet | Material sent for review | Standing and admissibility markers required |
| Audit-scoped | Material shown to auditor or authority under defined scope | Chain of custody and lawful basis required |
| Counterparty disclosure | Material shared with participant/counterparty | Scope and identity of receiver required |
| LA-only | Abstracted learning content without identifiable third-party residue | Leakage check required |
| EA-scoped | Experience Artifact includes handled third-party exposure | Admissibility and receiver constraints required |
| Publication | Public release | Highest scrutiny; not default |
| Training contribution | Material supports model training | No raw third-party data by default; explicit permitted mode required |
| Federation | Shared with another `c`, node, community, or archive | Boundary and jurisdiction checks required |

**Hard rule:**

> A receiver useful for one mode is not authorized for another mode.

---

## 14. Redaction and minimization controls

A `c` SHOULD use the least exposing representation sufficient for the task.

Controls include:

```text
face blurring
body masking
voice masking
speaker anonymization
cropping
frame sampling
transcript suppression
name removal
identifier hashing
location coarsening
time coarsening
relationship suppression
document segmentation
background removal
metadata stripping
medical / legal / child markers
local-only embeddings
private notes separated from shareable artifacts
```

Warnings:

- pseudonymization is not anonymity;
- summaries can leak identity;
- embeddings can preserve sensitive structure;
- voice masking may fail;
- face blurring may not remove contextual identity;
- location coarsening may still expose patterns;
- redacted documents may leak through metadata;
- cross-document correlation can reconstruct identity.

**Hard rule:**

> Redaction lowers exposure. It does not automatically create permission.

---

## 15. Consent discipline

Consent MUST be mode-specific.

A third party may permit:

```text
conversation
local memory
recording
transcription
sharing with one person
sharing with a service
use in a dispute
use as witness material
use in EA
use as LA
use in training
publication
```

These are different permissions.

A `c` MUST NOT infer consent for all modes from consent for one mode.

Examples:

```text
A person joined a call.
This does not automatically permit model training.

A guest entered a smart home.
This does not automatically permit public disclosure.

A worker wrote a document.
This does not automatically permit use as EA outside work scope.

A passerby appeared on a camera.
This does not automatically permit publication or sale.
```

Consent may also be limited by law, power imbalance, professional duty, age, dependency, or contract.

This protocol does not decide those legal questions.

It marks them.

---

## 16. No-capture and no-externalization signals

A `c` SHOULD recognize and honor no-capture or no-externalization signals where feasible and applicable.

Signals may include:

- explicit human request;
- meeting rule;
- household rule;
- workplace rule;
- professional confidentiality context;
- private-room context;
- child or protected-party context;
- device-level privacy flag;
- local environmental marker;
- platform rule;
- legal or contractual notice;
- technical opt-out mechanism;
- jurisdictional constraint.

When a signal is present, a `c` SHOULD move to:

```text
T1 ephemeral perception
T4 redacted local memory
T8 blocked / local-only
T9 lawful hold
```

depending on safety, legal, and operational need.

A no-capture signal is not absolute in all possible cases.

For example, safety, fraud, emergency, legal preservation, or dispute defense may require limited retention.

But such retention MUST NOT become reuse, training, publication, or economic circulation by default.

---

## 17. DEA / EA handling

Third-party material MAY support DEA / EA only when the third-party boundary is handled.

A `c` SHOULD classify third-party involvement as one of:

| EA involvement class | Meaning | Treatment |
|---|---|---|
| Background-only | Third party appears but does not materially affect the experience | Redact / remove / local-only |
| Context-relevant | Third party helps explain setting or consequence | Minimize and mark |
| Participant-relevant | Third party participates in the event | Consent / standing / admissibility review may be needed |
| Consequence-bearing | Third party is affected by the action or outcome | ARL / admissibility / lawful basis may be required |
| Protected-party-relevant | Minor, patient, dependent, vulnerable person, or high-trust subject involved | Strict restraint; externalization blocked unless justified |
| Evidence-relevant | Material needed for dispute, audit, safety, or law | Chain of custody and lawful handling required |

**Hard rule:**

> An Experience Artifact may preserve `a`'s experience without exporting a third party's raw identity.

---

## 18. LA handling

Learning Abstracts may be safer than EA for third-party exposure, but they are not automatically safe.

An LA derived from third-party exposure MUST avoid:

- names;
- faces;
- voices;
- unique locations;
- exact dates where unnecessary;
- rare combinations of traits;
- medical / legal / employment identifiers;
- social graph reconstruction;
- emotional or behavioral profiling of third parties;
- background details that identify a home, workplace, child, patient, or client.

Acceptable LA pattern:

```text
A household scheduling conflict showed that always-on reminders should respect shared-room quiet hours.
```

Risky LA pattern:

```text
My spouse, after returning from a named clinic on a specific day, reacted angrily when the assistant repeated a private reminder in front of our child.
```

The second example contains too much third-party exposure.

---

## 19. Training contribution discipline

Third-party material MUST NOT be training material by default.

For training use, a `c` SHOULD require:

```text
source class declaration
third-party marker
redaction / abstraction
receiver-mode declaration
lawfulness check
consent or other valid basis where applicable
provenance
anti-laundering check
scope limitation
reuse limitation
audit trail
```

Training contribution modes:

| Mode | Allowed posture |
|---|---|
| Raw third-party data | Blocked by default |
| Redacted third-party context | Possible only under scope and leakage controls |
| Aggregated LA | Possible when identity and sensitive relation leakage are controlled |
| EA containing third-party consequence | Requires admissibility and standing review |
| Public-role material | Still requires source and context discipline |
| Professional record material | Strictly blocked unless lawful and specifically authorized |
| Child/protected-party material | Blocked by default |

**Hard rule:**

> A third party's life must not be washed into training data through `a`'s `c`.

---

## 20. Oracle-call discipline

External LLMs, judges, tools, APIs, and cloud services are receivers.

A `c` MUST NOT treat an oracle call as harmless merely because it is temporary.

Before sending third-party material to an oracle, `c` SHOULD ask:

```text
Can the task be done locally?
Can the third-party material be removed?
Can the context be summarized without identity?
Can the oracle receive a redacted version?
Is no-training / no-retention mode available?
Is the receiver mode declared?
Is the model vendor allowed under the jurisdiction / policy / contract?
Is the call logged?
```

Default order:

```text
local model
  -> local redaction
  -> local abstraction
  -> oracle with minimal context
  -> ARL / judge only if stakes justify exposure
```

---

## 21. Hivemind and multi-model review

A `c` may use multiple models for ARL, Judge, verification, or high-stakes review.

Third-party boundary discipline still applies.

Multi-model use increases exposure because material may travel to multiple receivers.

Therefore, a `c` SHOULD:

- minimize before multi-model routing;
- send different slices only where needed;
- avoid full raw packets to all models;
- keep receiver-mode logs;
- track vendor / model / jurisdictional exposure;
- use local models for preliminary reduction;
- route high-risk material only through permitted review channels;
- block third-party material from ordinary training or telemetry.

**Hard rule:**

> ARL is not a license to broadcast private third-party material.

---

## 22. Household and family context

A household `c` or personal `c` inside a household MUST NOT absorb every family member into one undifferentiated memory field.

A household contains overlapping boundaries:

```text
individual adult
partner
child
guest
elder
dependent
pet
home device
shared account
private room
shared room
household archive
```

A `c` SHOULD distinguish:

- private memory of `a`;
- shared household memory;
- child/protected material;
- guest material;
- partner material;
- household operations;
- legal/financial documents;
- health/care records;
- home security logs.

Examples:

```text
A reminder about groceries may be household memory.
A child's medical appointment is protected material.
A partner's private message is not household EA.
A guest seen by a doorbell camera is not training data.
A family argument is not marketable experience.
```

---

## 23. Workplace and organizational context

An organizational `c` MUST distinguish work product from personal exposure.

Workplace material may include:

```text
project files
meeting notes
employee performance
client information
internal disputes
security footage
access logs
customer calls
confidential documents
trade secrets
personal messages on work systems
```

Protocol warnings:

- employment context may include power imbalance;
- work participation is not unlimited consent;
- employees are not raw data sources by default;
- clients and customers are not training material by default;
- security logs are not general behavioral assets;
- internal audit is not publication;
- work product does not erase third-party privacy;
- organizational `c` remains jurisdiction-bound.

A workplace `c` SHOULD have stricter role-based privileges than a personal `c`.

---

## 24. Professional high-trust context

Medical, legal, educational, care, social, religious, financial, and therapeutic contexts require stronger default restraint.

A `c` in such a context SHOULD assume:

```text
third_party_presence: protected or substantial
externalization_allowed: none or audit_scoped
redaction_required: true
arl_trigger: true when disputed or high-stakes
training_contribution: blocked by default
```

Examples:

```text
A patient case is not ordinary EA.
A student difficulty is not training material by default.
A legal consultation is not oracle context unless authorized and protected.
A therapy note is not a generic learning example.
A confession or spiritual-care note is not a public artifact.
```

This document does not define professional law.

It only marks high-trust context as high-risk for protocol movement.

---

## 25. Public and semi-public context

Public visibility lowers some expectations of secrecy.

It does not remove all boundaries.

A `c` SHOULD distinguish:

```text
public fact
public role
public event
public-space bystander
private behavior in public
crowd-level aggregate
identifiable individual
```

Examples:

```text
A public lecture may be summarized if allowed by context and law.
A face in the audience should not become training material by default.
A protest crowd may be politically sensitive.
A store security camera is not a public archive.
A street video may expose children, homes, vehicles, or vulnerable persons.
```

**Hard rule:**

> Public-space capture does not erase third-party standing.

---

## 26. Embodied machine, vehicle, robot, and drone context

Embodied systems can generate large-scale third-party exposure.

Examples:

```text
home robot
care robot
warehouse robot
vehicle dashcam
drone
farm robot
security robot
factory inspection system
autonomous delivery system
```

These systems SHOULD use:

- ephemeral perception where possible;
- local processing;
- strict retention limits;
- automatic redaction;
- no-training defaults;
- role-based access;
- safety-specific logs separated from general memory;
- jurisdiction markers;
- ARL triggers for disputed or harmful events.

An embodied `c` MUST distinguish:

```text
navigation perception
safety evidence
operator memory
third-party identity
training artifact
public record
```

These are different modes.

---

## 27. Non-human and ecological subjects

Third-party boundary is not only about human privacy.

Non-human and ecological subjects may include:

```text
animals
farms
habitats
wildlife
laboratory organisms
private land
industrial systems
vehicles
robots
infrastructure
```

A non-human subject may still reveal human data:

- owner identity;
- location;
- farm productivity;
- disease status;
- supply-chain data;
- ecological damage;
- research secrets;
- industrial vulnerabilities.

A `c` SHOULD avoid treating non-human telemetry as unrestricted merely because no human face appears.

---

## 28. Shared documents and communications

Documents and communications often contain multiple boundaries.

A `c` SHOULD classify:

```text
author
recipient
subject
mentioned persons
attachments
metadata
legal status
confidentiality markers
platform rules
work/personal scope
```

Examples:

```text
An email received by a is not automatically training data.
A group chat is not a public archive.
A CV contains third-party employment and education references.
A medical invoice contains patient and provider information.
A contract contains counterparty material.
A screenshot may expose unrelated private context.
```

A `c` SHOULD prefer:

- local summarization;
- quote minimization;
- redacted excerpts;
- document segmentation;
- metadata stripping;
- receiver-mode declaration;
- ARL when disputed.

---

## 29. Lawful inspection and state process

This protocol does not create a legal shield against lawful process.

It also does not create a universal state API into `c` memory.

A `c` SHOULD handle lawful inspection through:

```text
jurisdiction marker
scope marker
standing marker
request identity
chain of custody
disclosure boundary
third-party exposure marker
redaction where permitted
legal hold where required
audit trail
appeal / dispute route where available
```

Protocol compatibility does not imply legal authority.

A state, court, agency, or regulator operates through applicable law, not through this document.

**Hard rule:**

> Legal retention or disclosure does not imply model training, publication, economic circulation, or general reuse.

---

## 30. ARL triggers

A third-party sensor boundary SHOULD trigger ARL or equivalent review when:

- third-party standing is disputed;
- consent is disputed;
- material involves minors or protected parties;
- professional high-trust context is involved;
- private-room material is involved;
- material is requested for external training;
- material is economically valuable;
- material may harm reputation, employment, safety, liberty, health, or legal status;
- public-space capture includes sensitive activity;
- cross-border transfer is proposed;
- receiver mode is unclear;
- redaction sufficiency is disputed;
- source acquisition may be unlawful;
- an oracle call would expose raw third-party material;
- a `c` tries to use another subject's experience as its own.

ARL is a review path, not a release button.

---

## 31. AGL and source grounding

Actor Grounding Layer should operate before third-party material is trusted.

A `c` SHOULD ask:

```text
Who is the source?
Is this source present, authorized, and grounded?
Is this sensor reliable?
Was capture lawful or at least protocol-admissible?
Is the third party correctly classified?
Is there source spoofing, impersonation, staged behavior, or adversarial capture?
```

Third-party material can be false, manipulated, staged, coerced, or misattributed.

A beautiful sensor log is not automatically grounded evidence.

---

## 32. Anti-gaming and laundering risks

If EA becomes valuable, third-party sensor material can be abused.

Failure patterns:

| Failure | Description |
|---|---|
| Bystander laundering | Turning incidental third-party capture into marketable experience |
| Consent laundering | Using consent for one mode as consent for all modes |
| Synthetic laundering | Mixing synthetic or staged third-party material into EA |
| Witness laundering | Claiming that a captured third party verifies an event when they did not stand as witness |
| Family capture | Treating spouse, child, or household member as raw data source |
| Workplace surveillance drift | Reusing work monitoring as behavioral training data |
| Public-space overreach | Treating public visibility as unrestricted data ownership |
| Oracle leakage | Sending third-party material to external models without mode control |
| Reputation extraction | Turning mistakes, emotions, or conflict into sellable learning content |
| Social graph leakage | Exposing relationships through apparently harmless summaries |
| Jurisdiction washing | Routing data through another system to escape local constraints |

The third-party boundary is therefore part of EA anti-gaming discipline.

---

## 33. Economic Layer implications

Third-party material MAY affect EA value, but value does not override boundary.

Economic value can increase restraint because high-value artifacts create stronger incentives for abuse.

An EA involving third-party exposure SHOULD declare:

```yaml
ea_contains_third_party_material: true | false | unknown
third_party_role: background | context | participant | consequence_bearing | protected | evidence_relevant | mixed
third_party_handling: removed | redacted | abstracted | consented | lawful_basis | sealed | disputed | unknown
third_party_reuse: none | local_only | audit_only | LA_only | EA_scoped | training_permitted | publication_permitted | blocked
```

**Hard rule:**

> Marketability must not be used to erase third-party boundaries.

---

## 34. Jurisdiction posture

`c` remains jurisdiction-bound.

Third-party sensor handling SHOULD assume that different jurisdictions may define:

- recording consent;
- data protection;
- workplace monitoring;
- child privacy;
- medical confidentiality;
- biometric processing;
- public-space filming;
- evidence admissibility;
- cross-border transfer;
- right of access / correction / erasure;
- lawful process;
- retention obligations.

This protocol does not harmonize those laws.

It provides a boundary discipline compatible with jurisdictional variation.

Default:

```text
unclear jurisdiction -> externalization blocked or ARL/legal review required
```

---

## 35. Identity and privilege posture

Third-party material requires privilege control.

A `c` SHOULD separate privileges for:

```text
view raw third-party record
summarize third-party record
redact third-party record
use in local memory
send to oracle
use in ARL packet
include in EA
include in LA
share with counterparty
publish
train
federate
retain under legal hold
delete / suppress where lawful
```

Delegated agents MUST NOT receive broad access to third-party material unless their task requires it.

Agent swarms SHOULD operate under least privilege.

**Hard rule:**

> A local agent may need perception. It does not automatically need externalization authority.

---

## 36. Retention posture

Retention is not neutral.

A `c` SHOULD define retention posture for third-party material:

| Retention class | Meaning |
|---|---|
| Ephemeral | Processed and discarded quickly |
| Short local | Retained for immediate operational continuity |
| Local memory | Retained for `a`'s continuity but not externalized |
| Redacted durable | Retained with third-party minimization |
| Evidence hold | Preserved for dispute, safety, audit, or legal need |
| Legal hold | Preserved under applicable law or procedure |
| Blocked / suppressed | Not retained or not accessible except under limited conditions |
| Published | Released publicly; highest scrutiny |

Retention SHOULD be purpose-bound.

A retained record is not automatically reusable.

---

## 37. Minimal conformance profiles

### 37.1 Minimal profile

A minimal `c` implementation SHOULD provide:

- third-party marker;
- local-only default for raw third-party data;
- basic redaction;
- oracle warning before sending third-party material;
- no-training default;
- manual review for protected-party material;
- simple audit log for externalization.

### 37.2 Standard profile

A standard `c` implementation SHOULD provide:

- sensor-class detection;
- context-class detection;
- capture-state tracking;
- receiver-mode controls;
- consent/no-capture markers;
- role-based access;
- redaction pipeline;
- ARL triggers;
- retention classes;
- jurisdiction markers;
- EA / LA third-party metadata;
- oracle minimization.

### 37.3 Strict / regulated profile

A strict profile SHOULD provide:

- protected-party detection;
- professional-context locks;
- legal-hold separation;
- chain-of-custody controls;
- cryptographic sealing where appropriate;
- multi-party standing review;
- stricter retention limits;
- external model allowlists;
- redaction verification;
- audit-ready disclosure packets;
- formal ARL escalation.

---

## 38. Minimal hard rules

A `c` following this profile MUST observe these rules:

```text
1. Sensor capture is not consent.
2. Third-party presence is not anchor standing.
3. Third-party raw data is local-only by default.
4. Protected-party material is blocked by default.
5. Private-room material is blocked by default.
6. Public-space capture is not unrestricted reuse.
7. Consent is mode-specific.
8. Oracle calls are externalization events.
9. Training use requires explicit admissible mode.
10. Redaction reduces exposure but does not create permission.
11. EA involving third parties requires marker and admissibility review.
12. LA must not leak identifiable third-party context.
13. Legal hold is not reuse.
14. Jurisdiction remains binding.
15. ARL is a review path, not a release shortcut.
```

---

## 39. Relation to Anchor Class Boundaries

Anchor Class Boundaries defines who or what `a` may be.

This document defines what happens when the sensor field of that `a` includes others.

For individual anchors, the issue appears in daily life.

For household, organizational, institutional, machine, or civic anchors, the issue scales quickly.

A larger anchor class usually creates larger third-party exposure.

Therefore:

```text
larger anchor perimeter -> stronger sensor boundary requirements
```

---

## 40. Relation to Raw Locality and Experience Refinery

Raw Locality states that raw reality stays local by default and is refined before externalization.

This document adds:

```text
raw reality involving third parties needs a third-party marker before it can be refined into DEA / EA / LA / disclosure / training / audit
```

The combined chain is:

```text
raw capture
  -> raw-local custody
  -> third-party marker
  -> minimization / redaction / hold
  -> DEA / EA / LA candidacy
  -> admissibility / receiver-mode review
  -> bounded movement or no movement
```

---

## 41. Relation to DEA

DEA distinguishes input from experience.

This document adds:

```text
third-party input does not become a's experience artifact merely because it affected a
```

A third party may be:

- background;
- context;
- participant;
- consequence-bearing subject;
- witness;
- claimant;
- counterparty;
- protected party.

These roles must be named before the material is admitted.

---

## 42. Relation to EA-L4 / EATP

EA-L4 / EATP distinguishes Learning Abstracts from Experience Artifacts.

This document adds:

```text
third-party material may support EA or LA only after boundary handling
```

EA preserves origin and consequence.

But third-party origin and consequence cannot be appropriated by `a`'s `c` without standing, scope, or lawful basis.

LA may abstract learning.

But abstraction must not launder identifiable third-party life into training material.

---

## 43. Relation to the Economic Layer

The Economic Layer governs admissibility, transfer, disclosure, escrow, dispute hooks, anti-gaming, and circulation restraint.

This document adds a pre-circulation rule:

```text
third-party exposure must be marked and handled before economic admissibility is considered
```

Economic value is not a reason to weaken privacy boundary.

It is a reason to strengthen anti-gaming and admissibility checks.

---

## 44. Relation to ARL

ARL handles standing, admissibility, conflict, dispute, freeze, review, appeal, and re-entry.

Third-party sensor cases SHOULD route to ARL when there is disagreement or uncertainty about:

- who is affected;
- who has standing;
- whether capture was legitimate;
- whether evidence is admissible;
- whether disclosure is lawful;
- whether redaction is sufficient;
- whether the material can become EA / LA;
- whether a third party may object;
- whether a protected party is involved;
- whether an oracle may receive the material.

ARL cannot turn invalid capture into valid authority by fluency.

---

## 45. Relation to L4 Reality Boundary

Third-party sensor boundary is an L4 problem.

It is not only a text-policy problem.

Sensors exist in rooms, pockets, vehicles, hospitals, schools, workshops, streets, farms, and homes.

They consume electricity, store bits, identify bodies, reveal locations, trigger police reports, affect insurance, change employment, damage trust, and expose children.

The boundary is physical before it is philosophical.

---

## 46. Explicit bridge

**Raw Locality / DEA / EA ↔ Third-Party Sensor Boundary ↔ ARL / Economic Layer**

Raw data stays local by default.

Input becomes experience only through DEA discipline.

Experience becomes economically or procedurally relevant only through admissibility.

When third parties are present, their boundary must be marked before the chain may proceed.

---

## 47. Hidden bridges

### 47.1 SER continuity ↔ non-anchor privacy

A `c` preserves continuity for its own anchor.

It does not gain continuity authority over every subject it observes.

Respecting third-party boundaries strengthens `c` by preventing continuity from becoming capture.

### 47.2 L4 sensor reality ↔ EA anti-laundering

A camera, microphone, or robot can produce convincing records.

Convincing records can be economically valuable.

This creates an incentive to launder bystander material into EA.

The third-party sensor boundary blocks that conversion before value claims appear.

### 47.3 ARL standing ↔ receiver-mode discipline

Many privacy failures are mode failures.

A record made for safety becomes a training example.

A transcript made for memory becomes evidence.

An oracle query becomes vendor telemetry.

ARL needs standing and receiver-mode clarity to prevent these conversions from becoming invisible.

### 47.4 Anchor Class Boundaries ↔ household / organization scaling

When `a` expands from one human to a household, company, robot, hospital, farm, or city, the number of exposed third parties grows.

Anchor expansion therefore requires sensor-boundary expansion.

---

## 48. Earth paragraph

In an ordinary day, a phone on a kitchen table hears a child, a doorbell camera sees a courier, a car camera records a cyclist, a laptop captures a colleague's face, a nurse writes a note about a patient, a workshop camera sees a customer, and a farm robot records a neighboring field. A useful `c` may need some of that material to help its `a`: remember, repair, defend, explain, schedule, or stay safe. But the raw stream is not automatically experience, evidence, training data, or property. The system must know when to crop, blur, forget, seal, summarize, hold, ask, refuse, or escalate. Otherwise the personal assistant becomes a private surveillance pump with polite language.

---

## 49. Closing statement

A serious `c` may observe the world.

Observation must not become appropriation.

This profile says:

```text
sensor capture is not consent
third-party presence is not anchor standing
raw third-party material is local-only by default
protected contexts require stronger restraint
oracle calls are externalization events
training use is blocked by default
EA requires third-party markers where exposure exists
LA must not launder identity
ARL handles contested movement
jurisdiction remains binding
```

That is the third-party sensor boundary of v0.1.
