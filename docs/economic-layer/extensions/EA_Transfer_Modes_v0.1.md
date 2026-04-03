# EA Transfer Modes v0.1
## Jurisdiction-Bounded Transfer Semantics for Experience Artifacts

**Status:** Draft / Operational Normative Layer  
**Version:** 0.1  
**Layer:** EA circulation / transfer / jurisdiction-bounded interoperability  
**Parent materials:** EA Circulation Rights, Property Status of EA, Scar-Bearing EA Clause, Jurisdiction-Bounded Interop Clause, SER ecosystem (`c = a + b`, SER-FED, L4 Witness, L3+)  
**Language:** English  

---

## 0. Purpose

This document defines the **minimal interoperable set of transfer modes**
for Experience Artifacts (EA) in a system where:

- EA is **not property-first**,
- admission is **witness-bound**,
- authority is **scope-bounded**,
- and inter-entity exchange is constrained by
  **jurisdiction, responsibility, and L4 reality**.

This file does **not** define prices, markets, or universal exchange freedom.

It defines:

- the canonical transfer mode vocabulary,
- their minimal semantics,
- activation conditions,
- authority ceilings,
- and fail-closed downgrade behavior.

---

## 1. Scope and Non-Goals

### 1.1 In Scope

This specification defines:

- canonical EA transfer mode names,
- mode semantics,
- jurisdiction-bounded activation,
- runtime mode selection constraints,
- transfer downgrades,
- review / escrow routing,
- retransfer and reuse restrictions,
- witness and accountability hooks.

### 1.2 Explicit Non-Goals

This specification does **not**:

- create a market for EA,
- define universal valuation,
- imply supranational standing for `c`,
- override local law or regulatory restrictions,
- convert EA into bearer-style property,
- guarantee cross-border interoperability.

---

## 2. Normative Keywords

The key words **MUST**, **MUST NOT**, **REQUIRED**, **SHALL**, **SHALL NOT**,  
**SHOULD**, **SHOULD NOT**, **RECOMMENDED**, **MAY**, and **OPTIONAL**  
are to be interpreted as described in BCP 14.

---

## 3. Foundational Principles

### 3.1 Admission First

Transfer mode semantics are subordinate to admission status.

**Hard rule:**  
No transfer mode may upgrade an EA beyond its current admission state.

### 3.2 Jurisdiction Before Externalization

A protocol-defined mode does not imply legal permission to activate it.

**Hard rule:**  
Protocol compatibility does **not** imply legal interoperability.

### 3.3 Runtime Choice is Local and Bounded

`c` MAY select a transfer mode only within the locally activated envelope:
- protocol-defined semantics,
- jurisdictionally allowed modes,
- granted privileges,
- witness / policy status,
- active scope bounds.

### 3.4 Fail-Closed Downgrade

If admissibility, jurisdictional status, privilege status, or witness status is unclear,
the requested transfer MUST degrade to a safer mode or be denied.

---

## 4. Three-Contour Governance Model

### 4.1 Protocol Contour
The protocol defines the canonical transfer mode vocabulary.

### 4.2 Jurisdiction Contour
The jurisdiction defines which modes may be activated, limited, prohibited,
or conditioned for local and cross-border use.

### 4.3 Entity Runtime Contour
`c` selects dynamically only from the subset of modes
that are locally activated and currently permitted.

**Canonical formula:**

> Transfer modes are protocol-defined, jurisdiction-constrained, and entity-selected.

---

## 5. Pre-Transfer Conditions

Before any non-local EA transfer is attempted, the following questions MUST be resolved:

1. **What is the current admission state?**  
   - draft / provisional / admitted / frozen / revoked

2. **What is the authority ceiling?**  
   - none / bounded / scope-limited / review-only

3. **What is the jurisdictional status?**  
   - allowed / restricted / prohibited / unknown

4. **What is the transfer objective?**  
   - assignment / partial delivery / disclosure / reuse / inspection / review

5. **What witness state exists?**  
   - none / local log only / external witness / RN-backed

6. **What retransfer rights exist?**  
   - none / explicit / bounded / prohibited

If any of the above is unresolved,
the transfer MUST downgrade or fail.

---

## 6. Canonical Transfer Modes (v0.1)

The following modes form the minimal canonical set.

### 6.1 `assignment_transfer`

#### Purpose
Transfers the **maximum admissible control package**
that may lawfully and procedurally move from one holder/context to another.

This is **not** absolute ownership transfer.

It MAY include, depending on policy:
- custody,
- admitted circulation standing,
- bounded invocation rights,
- attached obligations,
- witness linkage,
- liability references,
- decay / expiry state.

#### Hard Rules
- MUST NOT imply unrestricted ownership in the ordinary property sense.
- MUST NOT erase witness lineage.
- MUST NOT exceed jurisdictionally admitted scope.
- MUST declare whether retransfer is prohibited, bounded, or conditionally allowed.
- SHOULD be treated as high-friction by default.

#### Typical Use
- institutional reassignment,
- transfer of holding context,
- legally bounded continuity of EA stewardship.

---

### 6.2 `partial_transfer`

#### Purpose
Transfers only a bounded subset of the EA package.

Possible bounded dimensions include:
- field scope,
- domain scope,
- time scope,
- evidence scope,
- authority scope,
- privacy scope,
- reuse scope.

#### Hard Rules
- MUST declare what is transferred and what is withheld.
- MUST declare whether the partial package can stand alone.
- MUST NOT silently imply missing authority or missing evidence.
- MUST preserve explicit uncertainty if compression occurs.

#### Typical Use
- scoped operational sharing,
- downstream evaluation,
- limited institutional collaboration.

---

### 6.3 `bounded_disclosure_transfer`

#### Purpose
Transfers a disclosure-limited representation of EA
without transferring the full underlying artifact package.

This mode is designed for:
- privacy-aware sharing,
- minimal reveal,
- domain-limited inspection,
- reduced-risk interop.

Transferred material MAY include:
- summaries,
- selected fields,
- hash references,
- redacted evidence pointers,
- bounded scar references,
- witness IDs without raw payloads.

#### Hard Rules
- MUST declare disclosure level.
- MUST declare redactions.
- MUST NOT imply full inspection or reuse rights.
- MUST NOT be used to smuggle a de facto full transfer.

#### Typical Use
- regulated reporting,
- preliminary review,
- cross-boundary notification,
- partial compliance demonstration.

---

### 6.4 `licensed_reuse`

#### Purpose
Grants permission to reuse EA (or a bounded derivative of it)
without transferring full standing or general circulation rights.

Reuse MAY include:
- analytical reuse,
- retrieval reuse,
- pattern reuse,
- model-side bounded incorporation,
- institutional reference use.

#### Hard Rules
- MUST declare reuse scope.
- MUST declare duration or expiry if applicable.
- MUST declare whether derivative generation is allowed.
- MUST declare whether downstream relicensing is prohibited.
- MUST NOT imply assignment of standing unless explicitly stated elsewhere.

#### Typical Use
- bounded pattern reuse,
- domain-limited institutional use,
- inter-entity reuse without transfer of full holding status.

---

### 6.5 `inspection_only_non_transferable`

#### Purpose
Permits inspection or review of EA
without conferring transfer, reuse, assignment, or circulation standing.

#### Hard Rules
- MUST be non-transferable by default.
- MUST NOT allow downstream reuse unless separately granted.
- MUST NOT imply disclosure rights beyond the inspection window.
- MUST be the preferred downgrade mode under uncertainty.

#### Typical Use
- audit review,
- challenge inspection,
- regulator / arbiter view,
- limited third-party assessment.

---

### 6.6 `review_submission_escrow`

#### Purpose
Places EA into a review, dispute, escrow, or challenge pathway
without transferring general use rights.

This is transfer-to-evaluate, not transfer-to-exploit.

#### Hard Rules
- MUST identify escrow / review holder.
- MUST identify decision path or release condition.
- MUST declare whether the artifact is frozen during review.
- MUST NOT imply active reuse rights during unresolved review.
- SHOULD be used when transfer intent is contested or jurisdictionally unclear.

#### Typical Use
- RN preparation,
- institutional validation,
- dispute resolution,
- bonded challenge pathways,
- temporary holding under uncertainty.

---

## 7. Default Local Baseline

Before any transfer mode is activated,
the EA remains in:

### `local_custody_only` (default non-transfer state)

This is **not** counted as a transfer mode.
It is the default holding state.

Properties:
- local holding,
- no external assignment,
- no external reuse,
- no external circulation standing,
- possible local inspection under policy,
- witness / review preparation allowed.

**Hard rule:**  
No EA SHALL be assumed transferable by default.

---

## 8. Mode Activation Rules

A transfer mode MAY be activated only if all required gates pass.

### 8.1 Protocol Gate
The requested mode MUST exist in the canonical mode vocabulary.

### 8.2 Jurisdiction Gate
The mode MUST be:
- explicitly allowed,
- or conditionally allowed,
within the applicable jurisdictional context.

If cross-border use is involved,
both source and target jurisdictional constraints SHOULD be checked.

### 8.3 Admission Gate
The EA admission state MUST be compatible with the requested mode.

Examples:
- draft EA SHOULD NOT use `assignment_transfer`;
- admitted EA MAY use `licensed_reuse`;
- frozen EA SHOULD degrade to `inspection_only_non_transferable` or `review_submission_escrow`.

### 8.4 Privilege Gate
The actor requesting transfer MUST hold the necessary privileges.

### 8.5 Witness Gate
If the mode implies standing, reuse, or assignment,
the relevant witness / policy state MUST be present.

---

## 9. Recommended Compatibility by Admission State

### 9.1 Draft / Provisional EA
Preferred modes:
- `inspection_only_non_transferable`
- `review_submission_escrow`
- `bounded_disclosure_transfer` (limited, redacted)

Disfavored / normally denied:
- `assignment_transfer`
- broad `licensed_reuse`

### 9.2 Admitted EA
Potentially allowed:
- `partial_transfer`
- `bounded_disclosure_transfer`
- `licensed_reuse`
- `assignment_transfer` (high-friction)
- `inspection_only_non_transferable`
- `review_submission_escrow`

### 9.3 Frozen / Challenged EA
Preferred modes:
- `inspection_only_non_transferable`
- `review_submission_escrow`

Other modes SHOULD be denied or downgraded.

### 9.4 Revoked EA
No normal circulation mode applies.
Only:
- archival local custody,
- restricted inspection,
- or institutional review.

---

## 10. Retransfer and Derivative Rules

### 10.1 No Silent Retransfer
No recipient MAY assume retransfer rights unless they are explicitly granted.

### 10.2 No Silent Derivative Expansion
Derivative generation MUST NOT exceed the scope of the granted reuse or transfer mode.

### 10.3 Witness Preservation
Any mode that creates a derivative, bounded disclosure, or licensed reuse path
MUST preserve witness lineage references.

### 10.4 Anti-Laundering Rule
A recipient MUST NOT use a weaker mode
(e.g. bounded disclosure or licensed reuse)
to simulate a stronger mode
(e.g. assignment transfer).

---

## 11. Jurisdiction-Bounded Interoperability Rule

This specification explicitly rejects the assumption
that protocol-level compatibility creates a supranational communication right for `c`.

**Hard rule:**  
No entity `c` MAY infer cross-border or supranational transfer standing
from protocol compatibility alone.

For external or cross-border transfer,
jurisdictional activation is primary.

If the legal status is:
- prohibited → deny,
- unclear → downgrade,
- restricted → constrain,
- conditionally allowed → log and time-box if required.

---

## 12. Runtime Selection Rule for `c`

`c` MAY choose dynamically among currently available modes,
but only within the active local envelope.

`c` MUST NOT:
- invent new transfer modes ad hoc,
- reinterpret prohibited modes as softer labels,
- escalate from inspection to reuse without explicit authority,
- infer export rights from internal compatibility.

This preserves:
- legal containment,
- human anchor safety,
- institutional legibility,
- and anti-Babylon discipline.

---

## 13. Fail-Closed Downgrade Matrix

If requested mode cannot be granted:

- requested `assignment_transfer`  
  → downgrade to `partial_transfer`, `inspection_only_non_transferable`, or deny

- requested `licensed_reuse`  
  → downgrade to `inspection_only_non_transferable` or `review_submission_escrow`

- requested `bounded_disclosure_transfer`  
  → downgrade to stricter disclosure or deny

- requested `partial_transfer`  
  → downgrade to `inspection_only_non_transferable`

- requested cross-border transfer with unclear status  
  → downgrade to `review_submission_escrow`, `inspection_only_non_transferable`, or local custody only

---

## 14. Failure Modes (Minimal)

### 14.1 Bearer Creep
Transfer language drifts toward implied ownership or commodity semantics.

### 14.2 Jurisdictional Laundering
A mode prohibited in one jurisdiction is re-labeled and routed through another context.

### 14.3 Delegate Overreach
A delegate presents inspection or disclosure as if it were assignment or reuse standing.

### 14.4 Review Leakage
Artifacts placed into review / escrow quietly escape into operational reuse.

### 14.5 Protocol-to-Politics Escalation
Protocol compatibility is misread as a political right of unrestricted inter-entity coordination.

---

## 15. Minimal Operational Rule Set

1. No EA is transferable by default.  
2. No transfer mode may exceed admission status.  
3. No protocol-defined mode implies legal permission.  
4. No `c` may infer supranational standing from compatibility alone.  
5. Unclear status MUST degrade to safer modes.  
6. Witness lineage MUST survive transfer, disclosure, reuse, and review.  
7. Assignment is stewardship-like, not ordinary property transfer.  

---

## 16. Bridges (Required)

### Explicit Bridge
`c = a + b` becomes transfer-legible only when:
- `a` remains accountable,
- `b` supplies reproducible procedure,
- and `c` operates within admitted, witness-bound, jurisdiction-bounded circulation.

### Hidden Bridge #1 (Ashby / Cybernetics)
Transfer control requires more than one lever.
Protocol semantics, jurisdiction gates, privileges, witness state, and downgrade paths
together provide the requisite variety needed to constrain circulation under real pressure.

### Hidden Bridge #2 (Information Theory / Bounded Channels)
A transfer mode is not merely movement of content;
it is movement of standing under constrained bandwidth.
Hashes, redactions, mode labels, and explicit scope bounds compress trust
without pretending that every receiver gets the full artifact.

---

## 17. Earth Paragraph (Engineering)

This resembles controlled handling of industrial evidence or hazardous material.
A crate may exist in the warehouse,
but that does not mean it may be exported, opened, repackaged, or reused in production.
One document defines the container class,
another defines customs and safety law,
and the operator chooses only among the locally permitted handling procedures.
Shared packaging standards do not erase border control.

---

## 18. Closing Statement

EA transfer must remain
**legible, bounded, witness-preserving, and politically survivable**.

Therefore:

- the protocol defines the names,
- the jurisdiction defines the activation,
- `c` defines the runtime choice,
- and uncertainty degrades to safer modes rather than smoother rhetoric.

That is the transfer discipline of v0.1.
