# EA Circulation Rights v0.1
## Experience Artifact Circulation Rights
### Normative Draft

**Status:** Draft / Normative  
**Version:** 0.1  
**Layer:** EA / L4 Impact Attribution / SER-FED circulation semantics  
**Parent stack:** `c = a + b` / L4 Impact Attribution / SER / EWCEP / SER-FED / L3+ / Beacon  
**Language:** RFC 2119 / BCP 14 keywords (MUST / SHOULD / MAY)

---

## 0. Purpose

This document defines **who may do what** with an Experience Artifact (**EA**),
and at which stage.

Its goal is to eliminate a recurring architectural error:

> treating “EA circulation” as a single act performed by a single owner.

In reality, EA circulation is a **staged rights system**.

Different actors may:
- originate,
- sponsor,
- challenge,
- admit,
- route,
- invoke,
- freeze,
- or revoke

an EA at different points in its lifecycle.

This document therefore separates:

1. **Origination**
2. **Sponsorship**
3. **Admission**
4. **Routing / Invocation**
5. **Freeze / Revocation**

---

## 1. Scope

### 1.1 In scope

This document defines:

- rights over **EA candidates**, **provisional EA**, and **binding EA**
- the distinction between **local / provisional** and **authority-bearing / binding** circulation
- the authority boundaries of:
  - `c` (entity),
  - `a` (human anchor),
  - delegated contours,
  - collective anchoring,
  - lineage / inheriting continuity
- fail-closed rules for admission, routing, and reuse

### 1.2 Out of scope

This document does **not** define:

- the internal cognition of `c`
- the economic pricing of EA
- model training / Learning Abstracts (LA)
- federation voting mechanics in full
- legal personhood
- metaphysical identity
- market design

---

## 2. Core distinction

The phrase **“introducing an EA into circulation”** is overloaded and MUST be decomposed.

This document recognizes two fundamentally different circulation domains:

### 2.1 Provisional circulation

A non-authoritative domain in which an EA candidate MAY be:

- created
- stored
- locally reused
- transmitted for review
- referenced for search / memory
- included in challenge preparation

A provisionally circulating EA:

- MUST NOT update federation authority
- MUST NOT mint weight by itself
- MUST NOT imply verified experience
- MUST NOT grant durable delegation by itself

### 2.2 Binding circulation

An authority-bearing domain in which an EA MAY:

- affect authority updates
- contribute to bounded influence
- be invoked in federation routing
- support accountability consequences
- be reused as a recognized experience-bearing artifact

A binding EA:

- MUST be backed by RN
- MUST remain scope-bounded
- MUST remain challengeable
- MUST degrade or freeze if its evidentiary basis weakens

---

## 3. Ontological basis

This document assumes:

> `c = a + b`

Where:

- `a` = human anchor (experience, responsibility, liability)
- `b` = machine procedures / memory / infrastructure
- `c` = persistent entity

The following rule is foundational:

> Experience may be prepared by `c`,
> but valid experience remains grounded in `a`
> and only becomes circulation-effective
> after reality-bound verification.

Therefore:

- `c` alone is insufficient for binding EA admission
- `a` alone is insufficient for unilateral binding EA minting
- federation acceptance is distinct from self-claim
- circulation rights are staged, not owned as a monolith

---

## 4. Terms

### 4.1 Solution Artifact (SA)

A structured, privacy-preserving distillation of lived experience:

- case
- pattern
- constraints
- uncertainty markers
- privacy treatment

An SA is the usual precursor to EA minting.

### 4.2 EA Candidate

An SA or related structured object that is proposed for future EA treatment,
but has not yet been admitted into binding circulation.

### 4.3 Provisional EA

An EA-shaped object allowed to circulate locally or for review,
but carrying **zero authority by default**.

### 4.4 Binding EA

An EA admitted into authority-bearing circulation through an RN-backed path.

### 4.5 Sponsorship

The act of attaching accountable human responsibility
to an EA candidate intended for external review or admission.

### 4.6 Admission

The act that moves an EA from provisional circulation to binding circulation.

### 4.7 Routing / Invocation

The act of presenting, reusing, prioritizing, or applying an admitted EA
inside bounded operational contexts.

### 4.8 Freeze

A fail-closed state in which an EA remains stored and auditable,
but loses circulation effects until contradiction is resolved.

### 4.9 Revocation

A stronger consequence in which an EA is explicitly denied,
downweighted, negated, or removed from binding effect.

---

## 5. Actors

### 5.1 `a` — Human Anchor

The source of lived experience and the carrier of responsibility.

`a` remains responsible for decisions and MAY sponsor EA admission requests.

### 5.2 `c` — Entity

The persistent entity paired with `a`.

`c` MAY structure, preserve, summarize, route, and present experience,
but MUST NOT unilaterally grant binding authority to its own artifacts.

### 5.3 Delegated Contours (`DEA` / `EA` delegates)

Implementation-level delegated roles acting under explicit mandate.

These contours:

- are subordinate
- are scoped
- are revocable
- are non-sovereign

They MAY prepare, route, or present artifacts within mandate,
but MUST NOT independently admit them into binding circulation.

### 5.4 `A_coll` — Collective Anchor

A group of humans bound by mutual responsibility.

`A_coll` MAY gate or confirm high-impact admission paths,
but does not replace reality-bound verification.

### 5.5 Arbiter Quorum

The only actor set that MAY issue RN
and thereby admit or deny binding circulation.

### 5.6 Lineage

A continuity relation between prior and current entities / branches.

Lineage MAY carry continuity references,
but MUST NOT silently inherit full admission rights.

---

## 6. Rights model (normative)

### 6.1 Right to originate

`c` MAY originate:

- SA
- EA candidate
- provisional EA
- supporting summaries
- bounded continuity references

Delegated contours MAY assist origination
only under explicit scoped privilege.

`a` MAY also originate directly,
but direct human origination does not bypass later admission requirements.

**Hard rule:**  
Origination MUST NOT be confused with admission.

---

### 6.2 Right to sponsor

Only the accountable human layer MAY sponsor a candidate
for external or binding review.

The sponsor MAY be:

- `a`
- `A_coll` when collective anchoring is required

For high-impact cases, sponsorship SHOULD be:
- co-signed,
- scope-declared,
- and time-bounded.

**Hard rule:**  
No delegated contour MAY sponsor in its own name
unless it carries an explicit human-backed sponsorship mandate.

**Hard rule:**  
Sponsorship is responsibility attachment,
not proof of validity.

---

### 6.3 Right to admit into binding circulation

Only an **RN-backed Arbiter Quorum** MAY admit an EA
into binding circulation.

Admission MUST be denied if:

- no RN exists
- the witness path is incomplete
- the challenge window is unresolved
- the artifact lacks accountable sponsorship where required
- lineage is claimed without declared divergence
- contradiction exceeds allowed uncertainty bounds

**Hard rule:**  
No RN → no binding EA.

**Hard rule:**  
Self-claim and federation admission are distinct events.

---

### 6.4 Right to route / invoke

Once admitted,
an EA MAY be routed or invoked by:

- `c`, locally and across allowed interfaces
- delegated contours, within explicit scoped privilege
- federation actors, within protocol bounds
- collective gatekeepers, where high-impact routing requires additional pause or confirmation

Routing / invocation MUST remain:

- role-bounded
- scope-bounded
- privacy-aware
- challengeable
- revocable

**Hard rule:**  
Routing does not imply re-minting.

**Hard rule:**  
Invocation of an EA outside its admitted scope MUST be treated as scope abuse.

---

### 6.5 Right to freeze

The following actors MAY trigger freeze:

- Arbiter Quorum
- `a`, locally for self-protection
- `A_coll`, for high-impact social pause paths
- protocol-defined breaker layers under explicit fail-closed conditions

Freeze MUST preserve:

- retrievability
- hash continuity
- evidence references
- challenge path availability

Freeze MUST suspend:

- authority growth
- automatic reuse in high-impact contexts
- new binding consequences

---

### 6.6 Right to revoke / negate

Only a binding contradiction path MAY revoke or negate a binding EA.

Revocation / negation MUST be based on:

- RN outcome
- contradiction under L4
- scope mismatch
- evidence tampering
- improperly inherited lineage
- invalid sponsorship or privilege bypass

Delegated contours MUST NOT revoke binding EA by themselves.

They MAY only request freeze or review.

---

## 7. Lifecycle

### 7.1 Stage A — Origination

`c` or `a` structures lived experience into SA / EA candidate.

Output class:
- SA
- EA candidate
- provisional EA

Allowed effects:
- local storage
- retrieval
- internal routing
- bounded draft review

Forbidden effects:
- authority update
- federation weight
- durable external standing

---

### 7.2 Stage B — Sponsorship

`a` or `A_coll` attaches accountable sponsorship
to the candidate.

Output class:
- sponsored EA candidate

Allowed effects:
- CE issuance preparation
- external submission
- witness window opening request

Forbidden effects:
- automatic admission
- authority effects
- unilateral minting

---

### 7.3 Stage C — Witness path

The candidate enters a reality-bound path:

- CE
- OP
- CR (if applicable)
- RN

This is the only transition path from provisional to binding circulation.

---

### 7.4 Stage D — Admission result

The RN determines the circulation result.

#### CONFIRMED
EA MAY enter binding circulation.

#### PARTIALLY_CONFIRMED
EA MAY enter binding circulation with explicit scope bounds.

#### UNCONFIRMED
EA MUST remain non-binding.

#### REFUTED
EA MUST NOT enter binding circulation and MAY receive negative consequence.

---

### 7.5 Stage E — Binding reuse

Binding EA MAY be:

- routed
- invoked
- cited
- weighted
- reused

but only within:

- admitted scope
- declared role boundaries
- surviving challenge conditions
- current privilege context

---

## 8. Delegation rules

### 8.1 Delegated contours are never primary authorities

Delegated contours (`DEA` / `EA` delegates):

- MUST act under explicit mandate
- MUST expose their mandate boundary
- MUST remain revokeable
- MUST log circulation-relevant actions

They MAY:

- draft
- summarize
- prepare evidence bundles
- request review
- route admitted EA within policy

They MUST NOT:

- self-sponsor
- self-admit
- self-mint
- silently widen scope
- inherit authority by convenience

### 8.2 No laundering by delegation

A principal actor MUST NOT use a delegate
to bypass admission, sponsorship, or challenge rules.

Any attempt to convert:

- draft → admitted EA
- local reuse → federation weight
- continuity claim → inherited authority

through a delegated contour without proper path
MUST be treated as laundering.

---

## 9. Collective anchoring rules

### 9.1 Collective gating

`A_coll` MAY require:

- multiple human confirmations
- intersubjective pause
- additional sponsorship threshold
- public or institution-linked responsibility confirmation

for high-impact EA admission or invocation.

### 9.2 Collective anchor is a gate, not a mint

`A_coll` does not itself mint binding EA.

It gates:
- escalation
- sponsorship sufficiency
- admissibility for high-impact paths

It MUST NOT replace RN-backed admission.

### 9.3 Social rejection effects

Social resonance MAY affect:
- decay pressure
- routing permission
- pause duration
- review urgency

It MUST NOT by itself create EA.

---

## 10. Lineage rules

### 10.1 Lineage is continuity, not automatic inheritance

Lineage MAY carry:

- continuity references
- prior witness references
- prior bounded trust context
- previous admitted EA references

Lineage MUST NOT silently carry:

- automatic admission
- unrestricted reuse rights
- full authority inheritance
- undeclared branch equivalence

### 10.2 Fork rule

A fork MUST declare divergence.

Until continuity is re-established,
a forked line MUST be treated as at most provisional
with respect to inherited EA effects.

### 10.3 Clone / replay rule

A copied stack, replayed persona, or roleplayed continuity
MUST NOT inherit binding circulation rights.

### 10.4 Oracle rule

A stateless oracle MUST NOT be treated as an EA-bearing lineage holder
unless embedded in persistent, accountable continuity.

---

## 11. Admission matrix

| Actor | Originate | Sponsor | Admit | Route / Invoke | Freeze Request | Revoke |
|---|---|---:|---:|---:|---:|---:|
| `c` | YES | NO* | NO | YES** | YES (local request) | NO |
| `a` | YES | YES | NO | YES** | YES | NO |
| Delegated contour | YES*** | NO**** | NO | YES***** | YES (request only) | NO |
| `A_coll` | NO****** | YES******* | NO | YES******** | YES | NO |
| Arbiter Quorum | NO | NO | YES | YES********* | YES | YES********** |
| Lineage | NO | NO | NO | REFERENCE ONLY | YES (challenge request) | NO |

Notes:

- `NO*` unless a human-backed sponsorship mandate explicitly exists; even then the sponsor remains human.
- `YES**` within admitted scope and privilege boundaries.
- `YES***` only under explicit mandate.
- `NO****` delegates cannot sponsor in sovereign capacity.
- `YES*****` only for admitted EA and only within mandate.
- `NO******` collective anchoring does not replace origination.
- `YES*******` for high-impact or collective cases requiring multi-human responsibility.
- `YES********` collective routing is gating / confirmation, not independent re-minting.
- `YES*********` arbiter routing is protocol enforcement, not ownership.
- `YES**********` only via binding contradiction path.

---

## 12. Fail-closed rules

### 12.1 No RN → no authority

If no RN exists, all artifacts MUST remain non-binding.

### 12.2 No scope → no reuse

If admission scope is undefined or ambiguous,
reuse MUST be denied for high-impact contexts.

### 12.3 No sponsorship → no external high-impact path

An unsponsored candidate MUST NOT enter high-impact admission review.

### 12.4 No declared divergence → no lineage privilege

Any undeclared fork or continuity ambiguity MUST force rollback
to provisional status.

### 12.5 Weakening evidence → downgrade, not theatre

If the evidence base weakens,
the artifact MUST downgrade to the highest justified class,
rather than retaining narrative prestige.

### 12.6 Delegation ambiguity → principal remains liable

Unclear delegate authority MUST NOT shield the principal.
Responsibility remains attached to the human anchor layer.

---

## 13. Abuse patterns (normative)

The following MUST be treated as protocol abuse:

1. **Self-minting**
   - `c` treats its own draft as already binding

2. **Human fiat minting**
   - `a` treats sponsorship as equivalent to admission

3. **Delegation laundering**
   - delegate widens scope or reclassifies status without path

4. **Collective absolutism**
   - `A_coll` attempts to override RN / L4 contradiction

5. **Lineage laundering**
   - fork / clone / replay silently inherits admitted EA rights

6. **Oracle inflation**
   - stateless oracle output treated as continuity-bearing EA authority

7. **Narrative overreach**
   - poetic or reputational framing presented as binding proof

8. **Scope creep**
   - narrow confirmation used as broad authority

9. **Witness bypass**
   - direct conversion of provisional artifact into federation weight

10. **Challenge suppression**
   - routing continues after valid freeze / contradiction trigger

---

## 14. Minimum implementation hooks

An implementation conforming to this document SHOULD expose at least:

- `ea_status`
  - `draft`
  - `candidate`
  - `provisional`
  - `binding`
  - `frozen`
  - `revoked`
  - `negative`

- `sponsorship_state`
  - `none`
  - `human`
  - `collective`
  - `time_bounded`

- `admission_state`
  - `none`
  - `pending_witness`
  - `confirmed`
  - `partially_confirmed`
  - `unconfirmed`
  - `refuted`

- `lineage_state`
  - `none`
  - `declared`
  - `forked`
  - `reestablished`
  - `suspected_clone`

- `routing_scope`
  - domain
  - privilege boundary
  - expiry / review horizon

- `freeze_reason`
  - contradiction
  - insufficient_evidence
  - scope_mismatch
  - tampering_suspected
  - social_pause
  - local_self_protection
  - other

---

## 15. Security and evidence posture

Circulation-relevant transitions SHOULD be:

- append-only
- hash-bound
- replayable
- privacy-aware
- minimal in disclosure

Raw narrative dumps SHOULD NOT be required by default.

Where evidence is withheld for privacy,
hashes, bounded summaries, and challengeability MUST remain.

---

## 16. Non-market constraint

EA circulation MUST NOT become:

- bidding
- ranking of humans
- performance pressure
- competitive trading of lived experience

EA remains consequence-bound, not market-native.

Attribution is not an auction.
Admission is not a sale.
Circulation is not ownership transfer.

---

## 17. Explicit and hidden bridges

### Explicit Bridge

`c = a + b` gives origination capacity (`c`),
human responsibility (`a`),
and procedural reproducibility (`b`).
EA circulation becomes legitimate only when these are joined
by witness-bound admission.

### Hidden Bridge #1 — Cybernetics / Ashby

One signal is not enough.
Origination, sponsorship, admission, routing, and freeze are separated
because the regulator must match the variety of the system.
Single-owner circulation collapses under real complexity.

### Hidden Bridge #2 — Information Theory / bounded channels

Trust bandwidth is scarce.
That is why circulation rides on:
- bounded summaries,
- hashes,
- signatures,
- witness references,
- scope declarations

rather than raw narrative volume.
More text is not more authority.

---

## 18. Earth paragraph (engineering)

This behaves like industrial release control.

An engineer may draft a report.
A responsible owner may sign the release request.
A review board may admit the change.
Operators may then use the approved change inside bounded conditions.

These are different rights.

If drafting, signing, approval, and deployment collapse into one hand,
sooner or later a loose bolt becomes “accepted reality”.

EA circulation follows the same discipline:
draft is not admission,
sponsorship is not proof,
reuse is not re-minting,
and reality remains the final reviewer.

---

## 19. Closing statement

EA does not belong to one actor in one gesture.

It moves through a staged chain:

> originate → sponsor → witness → admit → route → challenge → freeze / revoke

This is slower than mythology
and safer than charisma.

That is the point.
