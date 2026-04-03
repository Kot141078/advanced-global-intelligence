# Escrow, Freeze, and Dispute Hooks for EA Exchange v0.1
## Economic restraint, release discipline, and ARL escalation hooks for Experience Artifact exchange

**Status:** Draft v0.1  
**Layer:** EA exchange / economic escrow / circulation restraint / dispute escalation  
**Canonical home:** `advanced-global-intelligence`  
**Author:** Ivan Kotov  
**Location:** Brussels  
**Year:** 2026  

---

## Abstract

This document defines how Experience Artifacts (EA) are to be restrained, held, frozen, released, or escalated into dispute during exchange-sensitive movement.

Its purpose is not to define a court.

Its purpose is to define the middle ground between:
- ordinary movement,
- economic readiness,
- pre-dispute restraint,
- and full ARL conflict.

This document therefore fixes:

- pre-transfer hold,
- escrow states,
- circulation freeze logic,
- dispute-triggered freeze,
- release conditions,
- settlement outcomes,
- and ARL hook points.

In one line:

> Experience in motion must not be treated like clean cargo when provenance, scope, source class, disclosure, or legitimacy are still unstable.

---

## 1. Purpose

The purpose of this document is to answer one practical question:

> What should happen when an EA is economically relevant enough to move,
> but not yet lawful, safe, clear, or uncontested enough to move normally?

Without this layer, the system collapses into a childish binary:

- either the EA moves,
- or a formal dispute already exists.

That is too crude.

A serious system needs explicit exchange restraint states.

---

## 2. Scope

This document covers:

- pre-transfer hold
- economic escrow
- circulation freeze and circulation hold
- release conditions
- invalid release cases
- dispute-triggered freeze
- ARL escalation points
- settlement outcomes
- witness-visible restraint
- relation to non-transferability, provenance, and disclosure

It does **not**:
- restate the whole ARL package,
- define final valuation,
- define price discovery,
- or replace provenance / receiver-mode discipline.

---

## 3. Core principle

### 3.1 Canonical rule
An EA may be economically relevant and still not be exchange-ready.

### 3.2 Strong summary
> Value does not compel release.  
> Uncertainty does not yet require court.  
> Restraint is the lawful middle.

### 3.3 Consequence
The system must preserve a middle zone in which the EA may be:
- retained,
- inspected,
- bundled,
- matured,
- withheld,
- or narrowed,

without pretending either:
- that nothing is wrong,
- or that a full procedural dispute already exists.

---

## 4. Why EA exchange needs escrow

### 4.1 Exchange multiplies risk
Once EA begins to move between holders, modes, or scopes, the system faces amplified risks of:

- source laundering,
- premature release,
- standing leakage,
- lineage leakage,
- unsafe disclosure,
- scar appropriation,
- and hidden upgrade of circulation status.

### 4.2 Not all risk is yet dispute
Some risks are simply readiness failures:
- provenance still maturing,
- witness window still open,
- receiver mode not yet validated,
- disclosure surface still unstable,
- combined bundle not yet safe,
- or jurisdictional route not yet clear.

### 4.3 Escrow prevents false urgency
Escrow exists so that:
- economically relevant does not become “ship it now,”
- and temporary restraint does not become hidden condemnation.

---

## 5. Pre-transfer hold

### 5.1 Definition
`PRE_TRANSFER_HOLD` is the narrowest exchange restraint state.

It is used when a specific transfer or exchange attempt must pause
before stronger movement or stronger restraint is decided.

### 5.2 Typical triggers
Use `PRE_TRANSFER_HOLD` when:
- requested transfer mode is not yet validated,
- receiver mode is not yet validated,
- disclosure surface needs narrowing,
- source-origin class is not yet stable enough,
- jurisdictional route is unclear,
- or a bounded combination check is still pending.

### 5.3 Allowed during pre-transfer hold
- local retention
- bounded inspection
- provenance completion
- receiver-mode confirmation
- disclosure narrowing
- mode downgrade analysis

### 5.4 Blocked during pre-transfer hold
- requested circulation escalation
- assignment-like movement
- strong reuse
- irreversible outward release

### 5.5 Exit paths
`PRE_TRANSFER_HOLD` may exit to:
- `IN_ESCROW`
- `CIRCULATION_HOLD`
- `RELEASED`
- `RETURNED`
- or `ESCALATED_TO_ARL`

---

## 6. Escrow states

The following exchange states are recognized as canonical for v0.1.

### 6.1 `PENDING_TRANSFER`
A requested movement exists, but lawful execution has not yet occurred.

### 6.2 `PRE_TRANSFER_HOLD`
The request is paused while basic readiness checks are completed.

### 6.3 `IN_ESCROW`
The EA is under bounded holding for:
- maturation,
- condition completion,
- bundle stabilization,
- or release review.

### 6.4 `CIRCULATION_HOLD`
A narrower restraint blocks one or more circulation paths without requiring full escrow posture.

### 6.5 `DISPUTED_FROZEN`
The restraint is now contested and the EA is frozen against stronger movement pending ARL-sensitive treatment.

### 6.6 `RELEASED`
The requested movement or a downgraded lawful movement has been explicitly allowed.

### 6.7 `RETURNED`
The artifact does not move forward along the requested path and instead returns to the prior lawful holder/state.

### 6.8 `QUARANTINED`
The artifact remains preserved but is excluded from ordinary exchange until stronger review or correction occurs.

### 6.9 `NO_LAWFUL_REENTRY`
The artifact may not re-enter the requested exchange path under current conditions.

---

## 7. Economic escrow semantics

### 7.1 Rule
`IN_ESCROW` is a lawful non-circulation state.

### 7.2 Meaning
Escrow means:
- the EA remains economically legible,
- the EA remains preserved,
- the EA may still matter,
- but stronger exchange paths are paused.

### 7.3 Allowed in escrow
- retention
- bounded inspection
- witness preservation
- release-condition tracking
- source-class stabilization
- provenance completion
- bundle analysis
- receiver-mode validation
- policy confirmation

### 7.4 Blocked in escrow
- unconditional release
- silent assignment
- authority escalation
- unsafe disclosure
- high-force reuse
- hidden reclassification as clean movement-ready cargo

### 7.5 Important rule
Escrow is not proof of invalidity.
Escrow is proof that release is not yet earned.

---

## 8. Freeze semantics

### 8.1 Economic freeze is narrower than ARL freeze
Economic-layer freeze restrains exchange movement.
It does not yet decide contested legitimacy unless ARL is engaged.

### 8.2 Exchange freeze triggers
Use exchange freeze when:
- the exchange route is procedurally blocked,
- source-origin clarity weakens,
- synthetic risk rises during attempted movement,
- lineage density makes the current route unsafe,
- non-transferability pressure becomes dominant,
- or a release-condition contradiction appears.

### 8.3 Freeze effects
During exchange freeze:
- circulation escalation stops,
- release must not occur,
- downgrade or return may still be considered,
- and ARL escalation may become necessary if the hold becomes contested.

### 8.4 Freeze is not amnesia
The EA may remain:
- valuable,
- historically real,
- economically relevant,

while still being frozen for movement.

---

## 9. Dispute-triggered freeze

### 9.1 Rule
If restraint becomes contested in a procedurally meaningful way,
exchange restraint must escalate into a dispute-aware frozen state.

### 9.2 Typical triggers
Escalate when:
- a holder contests continued escrow,
- a receiver contests denial,
- multiple claimants assert incompatible release rights,
- standing for exchange is challenged,
- provenance contradiction becomes active conflict,
- lineage or scar meaning becomes exchange-critical and contested,
- or release now depends on adjudicating lawful basis.

### 9.3 Canonical outcome
At that point, the exchange path should move toward:
- `DISPUTED_FROZEN`
- and then, where required, `ESCALATED_TO_ARL`

### 9.4 Important distinction
Not every hold is dispute.  
But contested hold becomes dispute.

---

## 10. ARL hook points

### 10.1 ARL begins where economic restraint is no longer enough
Economic restraint is sufficient while the issue is:
- maturation,
- stabilization,
- route narrowing,
- or lawful uncertainty without procedural contest.

ARL becomes necessary when:
- legitimacy itself becomes contested,
- release rights become contested,
- operative use becomes contested,
- or exchange meaning now depends on adjudication.

### 10.2 Canonical ARL hooks for EA exchange
The economic layer should be able to hand off, at minimum:

- disputed release request
- disputed restraint continuation
- disputed provenance sufficiency
- disputed receiver standing or receiver mode
- disputed lineage-sensitive movement
- disputed non-transferability classification
- disputed re-entry into circulation

### 10.3 Hand-off rule
The economic layer must not silently pretend to resolve legitimacy questions that belong to ARL.

---

## 11. Re-entry conditions

### 11.1 Core rule
No EA should drift back into exchange by inertia.

### 11.2 Minimum release / re-entry checks
Before exchange re-entry, the system should be able to confirm:

- current provenance sufficiency
- stable source-origin class
- no unresolved synthetic laundering pressure
- lawful transfer mode
- lawful receiver mode
- disclosure surface compatibility
- no active non-transferability blocker
- no unresolved dispute or freeze incompatible with release
- no active jurisdictional block for the requested route

### 11.3 Explicit re-entry only
Re-entry must be:
- explicit,
- logged,
- and mode-specific.

### 11.4 Safer alternative
When in doubt:
- remain in escrow,
- narrow the mode,
- return,
- or escalate.

---

## 12. Settlement outcomes

### 12.1 `RELEASED`
The EA is cleared for the requested or downgraded lawful movement.

### 12.2 `RELEASED_WITH_LIMITS`
Movement is permitted, but only under narrowed:
- disclosure,
- receiver mode,
- transfer mode,
- scope,
- or time conditions.

### 12.3 `RETURNED`
The exchange path does not continue.
The artifact returns to prior lawful holding context.

### 12.4 `QUARANTINED`
The artifact remains preserved but cannot rejoin ordinary exchange flow.

### 12.5 `NO_LAWFUL_REENTRY`
The current exchange path is blocked and may not be re-entered without materially stronger lawful basis.

### 12.6 `ESCALATED_TO_ARL`
The matter has crossed from restraint into legitimacy conflict and now requires ARL handling.

---

## 13. Invalid release cases

The following are presumptively invalid release situations:

### 13.1 Release with unresolved provenance gap
### 13.2 Release with unstable source-origin class
### 13.3 Release under receiver-mode mismatch
### 13.4 Release under unresolved non-transferability pressure
### 13.5 Release of lineage-dense EA as if lineage were irrelevant
### 13.6 Release of synthetic-derived or mixed-origin EA as if parity were already granted
### 13.7 Release while contested hold is active
### 13.8 Release through stale authorization or expired conditions
### 13.9 Release through silent mode escalation
### 13.10 Release through rhetorical urgency rather than lawful basis

If one of these applies, the system should:
- hold,
- downgrade,
- return,
- quarantine,
- or escalate.

---

## 14. Witness requirements

### 14.1 Rule
Escrow, hold, freeze, release, return, and escalation should remain witness-visible.

### 14.2 Minimum record concerns
At minimum, records should preserve:
- EA identifier
- current state
- prior state
- trigger class
- responsible actor or rule surface
- affected transfer mode
- affected receiver mode
- release conditions
- timestamp

### 14.3 Why this matters
Otherwise the system will later rewrite:
- why the artifact was held,
- what exactly was blocked,
- whether the hold was lawful,
- and why release happened.

---

## 15. Interaction with non-transferability

### 15.1 Rule
Non-transferability pressure is one of the strongest reasons for exchange restraint.

### 15.2 Consequence
An EA may be escrowed or frozen not because it lacks value,
but because:
- its continuity density is too high,
- its lineage signal is too dangerous to move casually,
- its scar-bearing profile is too appropriable,
- or its disclosure cannot be made safe enough.

### 15.3 Important discipline
High economic relevance does not defeat non-transferability pressure.
Often it increases it.

---

## 16. Interaction with synthetic laundering

### 16.1 Rule
Synthetic ambiguity is a strong reason to hold.

### 16.2 Consequence
Where:
- source-origin class is unstable,
- synthetic contribution is unclear,
- provenance is mixed without clear marking,
- or summary substitution risk is high,

the artifact should not be released into stronger exchange modes.

### 16.3 No sanitization by escrow exit
A synthetic-shaped artifact does not become lived-equivalent merely by spending time in escrow.

---

## 17. Interaction with historical vs operative truth

### 17.1 Rule
Escrow and freeze act on exchange operativity, not on historical belonging.

### 17.2 Consequence
An EA may remain:
- historically true,
- memory-bearing,
- scar-relevant,
- economically meaningful,

while still being:
- held,
- frozen,
- returned,
- or denied re-entry.

### 17.3 Correct reading
Blocked exchange is not erased value.

---

## 18. Failure modes prevented

This document is designed to prevent:

### 18.1 False binary collapse
Everything is either moving normally or already in court.

### 18.2 Premature release
EA enters circulation before source, scope, disclosure, or route is stable.

### 18.3 Hidden verdict by hold
Economic restraint is silently used as if it were final condemnation.

### 18.4 Quiet exchange laundering
Artifacts under real uncertainty are cosmetically repackaged into “ready” cargo.

### 18.5 Dispute avoidance by procedural vagueness
Real legitimacy conflict is kept in economic limbo instead of escalating to ARL.

---

## 19. Minimal hard rules

1. EA exchange requires lawful restraint states before and below dispute.  
2. `PRE_TRANSFER_HOLD`, `IN_ESCROW`, and `CIRCULATION_HOLD` are lawful non-release states.  
3. Contested restraint escalates into dispute-sensitive freeze and ARL hooks.  
4. No release may occur by inertia.  
5. Release must be explicit, logged, and condition-based.  
6. Exchange restraint does not imply worthlessness or historical falsity.  
7. Economic hold must not silently impersonate final adjudication.  

---

## 20. Explicit bridge

**economic restraint ↔ release discipline ↔ ARL escalation**

---

## 21. Hidden bridges

### 21.1 L4 scarcity / boundedness
Real cost, scar, combination pressure, and bounded channels shape why some artifacts must wait before moving.

### 21.2 SER-FED anti-capture / anti-cartel
Escrow and freeze discipline help block synthetic laundering, lineage laundering, and prestige capture from turning exchange into a rigged witness market.

---

## 22. Earth paragraph

In a real warehouse, a pallet may be genuine, valuable, and urgently needed, yet still sit aside with a yellow tag: not because it is trash and not because a lawsuit has started, but because the bundle is incomplete, the route is not yet lawful, or mixing this lot with another would create a bigger failure. Escrow and circulation hold are that yellow tag for Experience Artifacts.

---

## 23. Closing statement

A serious exchange layer needs more than “yes” and “court.”

It needs:
- pause,
- hold,
- escrow,
- freeze,
- explicit release,
- safe return,
- and clean escalation to dispute only when contest is real.

That is the restraint discipline of v0.1.
