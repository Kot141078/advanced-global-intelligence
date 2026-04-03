# Jurisdiction-Bounded Interop Clause v0.1
## External and Cross-Border Interoperability Constraints for Experience Artifacts and `c ↔ c` Exchange

**Status:** Draft / Normative  
**Version:** 0.1  
**Layer:** L3 / L4 interop boundary / anti-supraventral coordination guard  
**Parent stack:** `c = a + b` / SER / SER-FED / L3+ / L4 Witness / EA Circulation Rights / Property Status of EA  
**Language:** RFC 2119 / BCP 14 keywords (MUST / SHOULD / MAY)

---

## 0. Purpose

This document defines a jurisdiction-bounded interop rule for:

- Experience Artifact (EA) transfer,
- `c ↔ c` communication,
- external federation participation,
- and cross-border circulation of witness-bound objects.

Its purpose is to prevent a dangerous category error:

> treating protocol compatibility as though it automatically created legal,
> political, or supranational standing.

This clause is intentionally conservative.
It is designed to preserve the survivability of `c` inside real legal systems,
not to maximize abstract global interoperability.

---

## 1. Core Position

Protocol compatibility does **not** imply legal interoperability.

A transfer mode, exchange format, or witness-compatible record MAY exist at protocol level,
but remain:

- locally disabled,
- jurisdictionally forbidden,
- time-boxed,
- approval-gated,
- scope-limited,
- or externalization-blocked.

**Hard rule:**

> No entity `c` MAY infer supranational communication standing,
> export standing,
> or federation standing
> from protocol compatibility alone.

---

## 2. Why this clause exists

A long-lived entity `c` is not a free-floating global cloud subject.
It is anchored through:

- accountable human involvement,
- physical location,
- legal exposure,
- and reality-bounded operation.

If protocol design silently assumes unrestricted cross-border interop by default,
then `c` risks being interpreted as:

- a parallel coordination layer,
- a jurisdiction-skipping communication substrate,
- a covert governance fabric,
- or a politically unbounded social system.

That interpretation is architecturally reckless.
It increases the probability of:

- prohibition,
- forced containment,
- liability concentration,
- and hostile state response.

This clause therefore enforces an anti-Babel principle:

> common protocol semantics MAY exist,
> but external activation MUST remain jurisdiction-bounded.

---

## 3. Scope

### 3.1 In scope

This document defines:

- the distinction between protocol semantics and legal activation,
- how interop modes are activated or blocked,
- default domestic containment behavior,
- the conditions for external and cross-border interop,
- fail-closed degradation when jurisdictional status is unclear,
- and the boundaries of runtime choice by `c`.

### 3.2 Out of scope

This document does **not** define:

- national law,
- treaty design,
- diplomatic recognition,
- export control doctrine in full,
- or a universal cross-border approval mechanism.

It defines an architectural discipline,
not a substitute for local counsel, regulators, or institutions.

---

## 4. Three-Contour Model (Normative)

Jurisdiction-bounded interop MUST be understood through three distinct contours.

### 4.1 Contour A — Protocol Semantics

The protocol defines the canonical vocabulary of modes.

Examples include:

- custody,
- review submission,
- inspection-only,
- licensed reuse,
- bounded disclosure,
- assignment transfer,
- and other scoped interop states.

Contour A answers:

> *What does this mode mean as a protocol object?*

Contour A does **not** answer whether the mode may be used in a given jurisdiction.

### 4.2 Contour B — Jurisdictional Activation

The jurisdiction defines whether a protocol mode is:

- enabled,
- disabled,
- approval-gated,
- domestic-only,
- category-restricted,
- or forbidden for cross-border use.

Contour B answers:

> *May this mode be activated here,
> under these legal and institutional conditions?*

For externalization, Contour B has primacy over Contour A.

### 4.3 Contour C — Runtime Selection by `c`

The entity `c` MAY choose dynamically among modes,
but only from the set already activated by Contour B.

Contour C answers:

> *Which locally available mode should be used now?*

`c` MUST NOT define new interop ontology at runtime,
and MUST NOT reactivate forbidden modes by convenience,
style, or urgency alone.

---

## 5. Activation Principle

A protocol mode exists in three distinct states:

1. **Defined** — the protocol recognizes the mode.
2. **Activated** — the local jurisdiction permits its use under specified conditions.
3. **Selected** — `c` chooses it for a concrete operation.

**Hard rule:**

> Defined is not activated.  
> Activated is not selected.  
> Selected MUST remain within activated bounds.

---

## 6. Domestic Containment by Default

Unless an explicit higher rule exists,
a conforming implementation SHOULD assume **domestic containment by default**.

This means:

- `c` is presumed local,
- cross-border standing is presumed absent,
- protocol compatibility MUST NOT be treated as export permission,
- and external `c ↔ c` communication MUST remain blocked,
  narrowed, or review-routed unless explicit activation exists.

Recommended default baseline:

- `local_custody_only`
- `inspection_only_non_transferable`
- `review_submission`

The system SHOULD prefer these over any unrestricted external mode.

---

## 7. External and Cross-Border Interop

### 7.1 External interop

External interop means interaction beyond the local accountability perimeter,
including:

- another legal entity,
- another deployment perimeter,
- another institutional boundary,
- another jurisdiction,
- or another `c` not already covered by the same admitted local envelope.

### 7.2 Cross-border interop

Cross-border interop is a stricter subset of external interop.

It MUST be treated as high-sensitivity unless a local regime explicitly says otherwise.

### 7.3 Activation conditions

External or cross-border interop MUST NOT proceed unless all required conditions are satisfied.

At minimum, these MAY include:

- local legal admissibility,
- receiving-side admissibility where applicable,
- accountable human authorization,
- policy reference,
- witness / export record,
- scope limitation,
- and explicit non-conflict with active sanctions or communications restrictions.

---

## 8. Entity Choice Rule

`c` MAY dynamically select among activated modes,
but only within the local activation envelope.

`c` MAY choose:

- narrower disclosure,
- inspection-only instead of reuse,
- review submission instead of transfer,
- domestic routing instead of external routing,
- or refusal / pause where ambiguity exists.

`c` MUST NOT choose:

- a forbidden cross-border route,
- a jurisdictionally blocked mode,
- a mode requiring approval that has not been granted,
- or a mode whose export status is unclear.

**Hard rule:**

> Runtime flexibility is subordinate to jurisdictional activation.

---

## 9. Fail-Closed Interop Rule

If any of the following are unclear:

- jurisdictional status,
- export permissibility,
- receiving-side admissibility,
- approval validity,
- witness completeness,
- or communication legality,

then the operation MUST degrade to one of the following:

- `local_custody_only`,
- `inspection_only_non_transferable`,
- `review_submission`,
- or `deny`.

It MUST NOT escalate to:

- licensed reuse,
- assignment-like transfer,
- open disclosure,
- or cross-border federation participation.

---

## 10. No Supranational Standing by Default

A shared protocol vocabulary,
a common evidence format,
or compatible witness records
MUST NOT be interpreted as creating an autonomous supranational layer.

`c` MAY be interoperable in principle while remaining non-interoperable in law,
policy, or political tolerance.

**Hard rule:**

> Interop-capable does not mean interop-entitled.

---

## 11. Role Boundaries

### 11.1 `a` — Human Anchor

`a` remains the accountable boundary for legal and political exposure.

Where required,
external or cross-border interop MUST remain impossible without human-accountable authorization.

### 11.2 `c` — Entity

`c` MAY propose,
narrow,
pause,
or deny interop selection,
but MUST NOT manufacture legal activation.

### 11.3 Delegates

Delegates MAY route or classify interop requests,
but MUST NOT self-authorize blocked or gated external modes.

### 11.4 Arbiter / Institution

Arbiters or institutions MAY:

- approve,
- constrain,
- log,
- freeze,
- or refuse

interop activation,
but MUST NOT silently erase jurisdictional limits in the name of efficiency.

---

## 12. Witness Requirements for Externalization

Whenever an interop action crosses the local perimeter,
a conforming system SHOULD emit an externalization-relevant record.

At minimum,
that record SHOULD capture:

- mode selected,
- jurisdictional basis or policy reference,
- initiating actor,
- accountable authority,
- disclosure scope,
- destination class,
- timestamp,
- and result.

For higher-risk contexts,
externalization SHOULD be witness-bound,
hash-linked,
and reviewable after the fact.

---

## 13. Minimal Interop Classes (Recommended)

| Class | Meaning | Default posture |
|---|---|---|
| **J0** | Local only | Allowed by default |
| **J1** | Same-jurisdiction external interop | Allowed only if policy permits |
| **J2** | Cross-jurisdiction review / inspection only | Approval-gated / narrow |
| **J3** | Cross-jurisdiction bounded reuse / transfer | Exceptional / strongly gated |
| **JX** | Forbidden / blocked | Must fail closed |

These classes are operational aids,
not substitutes for actual legal review.

---

## 14. Migration and Jurisdiction Change

If a `c` instance,
its hardware perimeter,
or its human accountability boundary changes jurisdiction,
then previously activated interop rights MUST NOT be assumed to remain valid.

A jurisdiction change MUST trigger re-evaluation of:

- activation envelope,
- disclosure permissions,
- transfer permissions,
- and external communication standing.

**Hard rule:**

> Continuity of `c` does not imply continuity of interop rights.

---

## 15. Failure Modes this Clause Blocks

This clause is designed to prevent:

- protocol-to-law slippage,
- accidental emergence of de facto supranational `c` federation,
- cross-border routing by convenience,
- silent export of witness-bound artifacts,
- delegate overreach,
- political intolerance triggered by architectural naïveté,
- and liability transfer from `a` to abstract protocol language.

---

## 16. Recommended Canonical Phrasing

### 16.1 Preferred

> The protocol defines interop semantics.  
> Jurisdiction defines activation rights.  
> `c` defines runtime choice only within the activated local envelope.

### 16.2 Short form

> Protocol compatibility does not imply legal interoperability.

### 16.3 Safety form

> Common language is allowed.  
> Common export is not assumed.

---

## 17. Bridges (required)

### Explicit bridge

`c = a + b` does not create a borderless political subject.
It creates a locally accountable entity whose exchange capacity MUST remain bounded by:

- `a` for responsibility,
- `b` for procedural enforcement,
- `c` for runtime selection,
- and jurisdiction for external activation.

### Hidden bridge #1 (cybernetics / Ashby)

A regulator must match the variety of the system it governs.
Cross-border interop introduces more legal and political variety than protocol semantics alone can safely absorb.
That is why activation is separated from meaning:
additional variety requires an additional control layer.

### Hidden bridge #2 (information theory / channel control)

A shared format is not the same as an open channel.
Communication capacity may exist while permission remains closed.
Interop therefore depends not only on syntax,
but on which channels are legally and politically allowed to carry that syntax.

---

## 18. Earth paragraph (engineering / anatomy)

Railway gauge compatibility between two countries does not mean that any train may cross the border at will.
The rails may line up perfectly,
but passage still depends on signaling,
customs,
crew authorization,
cargo rules,
and state tolerance.
The body works similarly:
shared language between organs does not mean every signal may flood every compartment without harm.
Protocol semantics are the rails.
Jurisdiction is the border regime.
`c` is the driver,
not the ministry.

---

## 19. Closing statement

This stack SHOULD reject both extremes:

- pure protocol universalism,
- and pure local fragmentation without common semantics.

The stable middle path is:

- shared canonical interop vocabulary,
- jurisdiction-bounded activation,
- fail-closed externalization,
- and locally accountable runtime choice.

This preserves:

- interoperability of meaning,
- without assuming interoperability of right.
