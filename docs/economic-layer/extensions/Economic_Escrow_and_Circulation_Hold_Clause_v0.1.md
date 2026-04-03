# Economic Escrow and Circulation Hold Clause v0.1
## Pre-Dispute Circulation Restraint for Experience Artifacts in the Economic Layer

**Status:** Draft / Normative Clause  
**Version:** 0.1  
**Layer:** EA economic circulation / pre-dispute restraint / bounded release  
**Parent materials:** EA Circulation Rights v0.1, EA Transfer Modes v0.1, Institutional Emergence of EA Value v0.1, Property Status of EA v0.1, EA Non-Transferability Criteria v0.1, Synthetic Laundering and Source Class Clause v0.1, Jurisdiction-Bounded Interop Clause v0.1, ARL package  
**Language:** English  

---

## 0. Purpose

This clause defines a distinct economic-layer state in which an Experience Artifact (EA)
is **temporarily removed from circulation**
without yet being treated as a full Arbitration / Review Layer (ARL) dispute.

The purpose is to separate two different realities:

1. **circulation is not yet lawful, safe, complete, or combinatorially ready**,  
2. **a procedurally valid dispute has actually begun**.

This clause governs the first reality.

It introduces:

- `ECONOMIC_ESCROW`,
- `CIRCULATION_HOLD`,
- pre-dispute restraint triggers,
- release conditions,
- escalation conditions into ARL,
- and the principle that **value does not imply immediate circulation admissibility**.

---

## 1. Scope and Non-Goals

### 1.1 In Scope

This clause defines:

- economic-layer temporary non-circulation states,
- pre-dispute holding logic,
- circulation restraint without full dispute classification,
- combinational triggers,
- witness and provenance maturation windows,
- release, downgrade, and escalation semantics,
- and the boundary between economic restraint and ARL conflict.

### 1.2 Explicit Non-Goals

This clause does **not**:

- define final valuation or price,
- decide ARL standing or admissibility in full,
- declare that restrained EA lacks value,
- replace freeze/quarantine semantics inside ARL,
- or create an implicit market right for EA.

---

## 2. Core Principle

### 2.1 Canonical Rule

An EA may be valuable,
historically real,
and even partially witness-bound,
while still being **temporarily non-circulation-admissible**.

### 2.2 Strong Summary

> Value is broader than circulation.  
> Circulation is narrower than value.

### 2.3 Main Consequence

Removal from circulation is **not** by itself:
- denial of value,
- proof of defect,
- or proof of dispute.

It may simply mean:

> the EA is not yet ready, lawful, safe, or combinatorially fit for circulation.

---

## 3. Why Economic Escrow Exists

Without a distinct economic holding state,
the system collapses into a false binary:

- either the EA circulates,
- or a full ARL dispute has already begun.

That binary is too crude.

A serious system needs an intermediate discipline
for artifacts that are:

- not rejected,
- not worthless,
- not yet dispute-classified,
- but not ready for active circulation.

This is the role of economic escrow and circulation hold.

---

## 4. Canonical States

### 4.1 `ECONOMIC_ESCROW`
A bounded holding state in which the EA is temporarily removed
from assignment, payout, circulation escalation, or strong economic routing,
while remaining preserved, inspectable under policy, and potentially releasable.

Use when:
- the EA is economically relevant,
- but additional maturation, bundling, scope clarification, or condition satisfaction is needed.

### 4.2 `CIRCULATION_HOLD`
A narrower operational state in which the EA is blocked
from specific circulation actions
even though it remains present in the local or institutional economic layer.

Use when:
- a specific transfer, reuse, assignment, or disclosure path is not ready,
- but broader holding does not yet require full escrow semantics.

### 4.3 `ECONOMIC_RELEASE`
The state in which previously restrained EA
is cleared for the specific circulation modes allowed by current conditions.

### 4.4 `ESCALATED_TO_ARL`
The state in which economic restraint is no longer sufficient,
because the matter has become procedurally contested
and now requires full ARL dispute handling.

---

## 5. Core Distinction from ARL

### 5.1 Economic Escrow is Not Yet a Dispute
Economic escrow exists before, below, or outside full dispute classification.

It does not require by default:
- claimant,
- respondent,
- standing contest,
- formal conflict class,
- or ARL outcome state.

### 5.2 ARL Begins When Contest Exists
ARL becomes necessary when the restrained state becomes contested in a procedurally meaningful way,
for example when there is a live conflict over:

- release,
- circulation rights,
- attribution,
- precedence,
- re-entry,
- authority effect,
- lawful execution path,
- or disputed evidentiary sufficiency.

### 5.3 Canonical Summary

> Economic escrow restrains circulation.  
> ARL adjudicates contested legitimacy.

---

## 6. Pre-Dispute Trigger Classes

The following trigger classes MAY justify `ECONOMIC_ESCROW` or `CIRCULATION_HOLD`
without yet opening ARL.

### 6.1 Provenance / Witness Maturity Triggers
Use restraint when:
- provenance is incomplete,
- witness window is still open,
- source-origin class is unresolved,
- synthetic risk classification is unfinished,
- scar-bearing status is not yet stabilized,
- or witness-linked composition remains immature.

### 6.2 Scope / Mode Incompatibility Triggers
Use restraint when:
- transfer mode has not yet been lawfully selected,
- receiver mode is incompatible,
- disclosure surface is not safely defined,
- non-transferability pressure is present,
- derivative boundary is unclear,
- or circulation scope exceeds current admissibility.

### 6.3 Combination Triggers
Use restraint when the EA is not unsafe alone,
but becomes unstable or non-lawful in combination.

Examples:
- lineage-dense EA + economic routing,
- synthetic-derived EA + scar-bearing implication,
- bounded derivative + cross-jurisdiction transfer request,
- multiple partial artifacts that together recreate prohibited continuity density,
- mixed-origin artifact + authority-sensitive reuse path.

### 6.4 Scar / Density Triggers
Use restraint when:
- scar-bearing force is high,
- continuity density is too high for immediate circulation,
- or the EA risks turning from economic object into continuity-appropriable material.

### 6.5 Jurisdiction / Interop Triggers
Use restraint when:
- the route crosses uncertain jurisdictional boundaries,
- activation legality is not yet resolved,
- protocol compatibility exists without legal clarity,
- or export / reuse / relay would exceed local activation rights.

### 6.6 Allocation / Scarcity Triggers
Use restraint when:
- limited attribution pools exist,
- release windows are gated,
- multiple candidate claims compete for bounded allocation,
- bond / escrow sequencing matters,
- or the system must avoid premature commitment under scarcity.

---

## 7. Economic Escrow Effects

When an EA enters `ECONOMIC_ESCROW`,
the following SHOULD apply unless narrower policy states otherwise:

### 7.1 Allowed
- retention,
- bounded inspection,
- witness preservation,
- source-class review,
- bundling evaluation,
- economic maturation,
- release-condition tracking,
- deferred routing preparation.

### 7.2 Blocked
- assignment transfer,
- payout / attribution execution,
- circulation escalation,
- strong authority-bearing reuse,
- unresolved cross-boundary export,
- and any route that assumes full economic readiness.

### 7.3 Important Rule
Escrow is not destruction.
Escrow is not denial of worth.
Escrow is temporary non-circulation.

---

## 8. Circulation Hold Effects

When an EA enters `CIRCULATION_HOLD`,
a narrower restraint applies.

### 8.1 Allowed
- continued local holding,
- review of release conditions,
- bounded inspection,
- non-circulatory archival retention.

### 8.2 Blocked
Only the specific circulation path(s) that triggered the hold,
for example:
- one transfer mode,
- one receiver path,
- one jurisdictional route,
- one reuse upgrade,
- or one bundled allocation path.

### 8.3 Why This State Exists
Not every blocked circulation path requires full escrow.

Sometimes the problem is local, narrow, and temporary.

---

## 9. Release Conditions

### 9.1 General Rule
No EA should exit economic escrow or circulation hold
without explicit release conditions.

### 9.2 Release Conditions MAY Include
- provenance closure,
- witness maturity,
- source-class stabilization,
- completion of combination review,
- jurisdictional clearance,
- receiver-mode confirmation,
- allocation window opening,
- disclosure safety confirmation,
- synthetic-risk marking,
- or bounded release approval by the relevant authority.

### 9.3 No Silent Release Rule
Release MUST be explicit, logged, and mode-specific.
No EA should drift back into circulation by inertia.

---

## 10. Escalation to ARL

### 10.1 Core Rule
Economic restraint escalates into ARL
only when the matter becomes procedurally contested.

### 10.2 Typical Escalation Triggers
Escalation SHOULD occur when:
- a party contests the continued restraint,
- a release is demanded against the current conditions,
- conflicting claimants assert incompatible rights,
- standing is challenged,
- provenance contradiction becomes active conflict,
- lineage, authority, or continuity meaning is disputed,
- or economic release now requires adjudication of lawful basis.

### 10.3 Canonical Formula

> Not all restraint is dispute.  
> But contested restraint becomes dispute.

---

## 11. Witness and Logging Requirement

### 11.1 Rule
Economic escrow and circulation hold SHOULD remain witness-visible,
even when full ARL has not yet begun.

### 11.2 Minimum Log Concerns
At minimum, records SHOULD be able to preserve:
- EA identifier,
- state entered (`ECONOMIC_ESCROW` or `CIRCULATION_HOLD`),
- trigger class,
- affected circulation modes,
- current release conditions,
- timestamp,
- and responsible actor / rule surface.

### 11.3 Why This Matters
Otherwise the system will later rewrite:
- why restraint occurred,
- what was blocked,
- and whether the restraint was lawful or arbitrary.

---

## 12. No Value-Denial Rule

### 12.1 Core Rule
Economic restraint MUST NOT be interpreted as proof that the EA lacks value.

### 12.2 Correct Interpretation
The correct meaning is narrower:

> this EA is not yet admitted to the requested circulation path.

### 12.3 Why This Matters
The system must be able to affirm both:
- all experience may matter,
- and not all experience may circulate immediately.

---

## 13. No Hidden Pre-Judgment Rule

### 13.1 Rule
Economic escrow MUST NOT be used
to simulate an ARL verdict before ARL actually exists.

### 13.2 Forbidden Pattern
Bad pattern:
- hold the EA,
- silently treat it as guilty / invalid / disproven,
- but never open lawful dispute procedure.

### 13.3 Correct Pattern
Economic escrow may say:
- not ready,
- not yet clear,
- not combinatorially safe,
- not lawfully activated,
- or awaiting release conditions.

It must not silently say:
- false,
- rejected,
- or illegitimate,
unless ARL or another explicit lawful procedure actually did so.

---

## 14. Interaction with Non-Transferability

### 14.1 Rule
Non-transferability pressure is one of the strongest reasons
for economic restraint.

### 14.2 Consequence
An EA may enter escrow not because it is economically irrelevant,
but because immediate circulation would expose:

- continuity density,
- lineage risk,
- scar appropriation risk,
- or unsafe disclosure conditions.

### 14.3 Important Distinction
Non-transferable does not imply economically meaningless.
It implies economically restrained.

---

## 15. Interaction with Synthetic Laundering

### 15.1 Rule
Synthetic ambiguity is a major escrow trigger.

### 15.2 Consequence
If the source-origin class,
synthetic contribution,
or authority posture of a synthetic-derived artifact is unresolved,
economic release SHOULD wait.

### 15.3 Why
A synthetic-shaped artifact should not drift into economic circulation
before its source class and risk profile are visible.

---

## 16. Interaction with Historical vs Operative Truth

### 16.1 Rule
Economic restraint acts on operative circulation,
not on historical truth.

### 16.2 Consequence
An EA may remain:
- historically real,
- memory-bearing,
- and potentially important,

while still being:
- escrowed,
- held,
- or blocked from current economic movement.

This is not contradiction.
It is discipline.

---

## 17. Failure Modes Prevented

This clause is designed to prevent:

### 17.1 False Binary Collapse
Either “circulates now” or “already a full dispute.”

### 17.2 Premature Market Laundering
EA drifts into economic flow before provenance, source class, or combinations stabilize.

### 17.3 Hidden Procedural Judgment
Escrow quietly becomes a shadow verdict.

### 17.4 Combination Blindness
Artifacts are reviewed only one by one,
while dangerous or non-lawful combinations slip through.

### 17.5 Value Denial by Delay
Temporary restraint is misread as proof of worthlessness.

---

## 18. Minimal Hard Rules

1. Economic restraint is not equivalent to full ARL dispute.  
2. `ECONOMIC_ESCROW` and `CIRCULATION_HOLD` are lawful pre-dispute states.  
3. Value does not imply immediate circulation admissibility.  
4. Restraint may be triggered by provenance, scope, combination, jurisdiction, scar density, or scarcity conditions.  
5. Release must be explicit and condition-based.  
6. Contested restraint escalates into ARL.  
7. Economic escrow must not simulate hidden guilt, rejection, or falsehood before lawful adjudication.  

---

## 19. Bridges (Required)

### Explicit Bridge
EA value, circulation rights, and ARL dispute discipline can coexist
only if the system recognizes a middle state:
valuable enough to preserve,
not yet ready enough to circulate,
not yet contested enough to adjudicate.

### Hidden Bridge #1 (Ashby / Cybernetics)
A serious regulator needs more than “go” and “court”.
Economic escrow adds the missing control state
needed to absorb uncertainty before conflict hardens.

### Hidden Bridge #2 (Information Theory / Channel Readiness)
A signal may be meaningful before it is transmission-ready.
Economic escrow marks that gap:
the artifact exists,
but the channel conditions for lawful circulation are not yet satisfied.

---

## 20. Earth Paragraph (Engineering / Warehouse Logic)

In a real warehouse, a pallet may be genuine, valuable, and urgently needed,
yet still sit aside with a yellow tag: not because it is trash and not because a lawsuit has started,
but because the bundle is incomplete, the transport slot is not open, a linked shipment is unresolved,
or mixing this lot with another would create a bigger problem.
That is not a court.
That is circulation discipline.
Economic escrow is exactly that yellow tag.

---

## 21. Closing Statement

All experience may be valuable.

Not all valuable experience is immediately circulation-admissible.

Therefore a serious EA economy requires:

- a state for temporary non-circulation,
- explicit release conditions,
- witness-visible restraint,
- and a clean escalation path into ARL only when contest actually begins.

That is the economic escrow discipline of v0.1.
