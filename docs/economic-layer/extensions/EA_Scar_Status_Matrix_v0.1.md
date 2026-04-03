# EA Scar Status Matrix v0.1
## Operational Classification Matrix for Scar-Bearing Experience Artifacts

**Status:** Draft / Normative Companion Matrix  
**Version:** 0.1  
**Layer:** EA circulation / scar-bearing classification / witness binding / bounded reuse  
**Parent stack:** `c = a + b` / L4 / SER / EWCEP / SER-FED / L4 Witness / Scar Bearing EA Clause  
**Language:** RFC 2119 / BCP 14 keywords (MUST / SHOULD / MAY)

---

## 0. Purpose

This matrix defines a compact operational classification for **scar status** of Experience Artifacts (**EA**).

Its purpose is practical:

- to prevent inflation of scar-bearing claims,
- to separate primary from derivative scar status,
- to make routing and reuse decisions mechanically simpler,
- to align authority with witness-bound origin,
- and to provide a stable interface for later EA economy layers.

This matrix is a classification aid, not a replacement for witness records, RN outcomes, or scope rules.

---

## 1. Core Principle

Scar status is determined first by **origin**, then by **binding**, then by **scope**.

**Hard rule:**

> No primary scar origin -> no scar-bearing status.  
> No witness-bound continuity -> no admissible scar-bearing classification.

A derivative artifact MAY carry scar-bearing status, but only within bounded and declared limits.

---

## 2. Status Matrix (Normative)

| Class | Name | Origin Requirement | Witness Requirement | Admission State | Authority Ceiling | Circulation Scope | Decay / Stability | Revalidation Requirement |
|---|---|---|---|---|---|---|---|---|
| **S0** | Non-Scar Derivative | No verified primary scar origin, or origin not proven | Missing, broken, insufficient, or non-binding chain | Not admitted as scar-bearing | **None** as scar-bearing | Storage, review, search, advisory, continuity support only | Decays as ordinary descriptive artifact | Cannot become scar-bearing without new witness-bound linkage |
| **S1** | Primary Scar-Bearing EA | Direct verified L4 exposure to irreversible cost, risk, loss, degradation, or liability | Primary witness-bound chain present | Admitted within declared scope | Highest available scar-bearing authority for that event class | Bound use, routing, citation, and limited circulation within admitted scope | More stable than derivatives, but still challengeable and decaying where applicable | Revalidation not required for basic primary status; required for scope expansion or renewed authority |
| **S2** | Bounded Derivative Scar-Bearing EA | Explicit derivation from one or more valid S1 or S3 sources | Derivative chain MUST preserve linkage to upstream witness-bound source | Admitted as derivative within inherited bounds | Lower than or equal to upstream source by default | Narrower than upstream unless explicitly stated otherwise | Faster decay and/or tighter review by default | Required for any authority increase, scope expansion, or privilege widening |
| **S3** | Revalidated Derivative Scar-Bearing EA | Derived from valid upstream scar source **and** refreshed through new admitted witness outcome | New witness-bound admission path exists in addition to upstream linkage | Newly or additionally admitted | May exceed inherited derivative bounds only within newly admitted scope | Scope defined by latest admission, not by rhetoric or lineage prestige | Stabilized relative to S2, but never immune to contradiction | Fresh RN-backed revalidation is the basis of this class |

---

## 3. Class Semantics (Normative)

### 3.1 Class S0 — Non-Scar Derivative

S0 covers artifacts that may still be useful but MUST NOT be treated as scar-bearing.

Typical S0 cases include:

- synthetic summaries,
- oracle-produced explanations,
- rhetorical compression,
- pattern notes without witness continuity,
- similarity-derived analogies,
- lineage references without binding source chain.

S0 artifacts MAY be:

- stored in custody,
- indexed,
- reviewed,
- searched,
- or used as bounded advisory material.

They MUST NOT:

- claim scar-bearing authority,
- inherit authority by style or usefulness,
- or bypass witness admission through repetition.

---

### 3.2 Class S1 — Primary Scar-Bearing EA

S1 is the base scar-bearing class.

An S1 artifact MUST directly represent a verified L4 collision or exposure,
including real cost, risk, loss, degradation, bonded liability, or equivalent reality pressure.

S1 MUST NOT be fabricated from:

- narrative force,
- confidence scores,
- roleplay,
- or synthetic reconstruction alone.

S1 is the reference class against which all downstream derivative scar claims are measured.

---

### 3.3 Class S2 — Bounded Derivative Scar-Bearing EA

S2 is the normal derivative scar class.

An S2 artifact MAY preserve scar-bearing status only if:

1. derivation is explicit,
2. upstream source is valid,
3. witness continuity is preserved,
4. uncertainty is not erased,
5. scope is bounded,
6. authority does not silently outrank the source.

**Hard rule:**

S2 inherits scar-bearing standing **by chain**, not by eloquence.

---

### 3.4 Class S3 — Revalidated Derivative Scar-Bearing EA

S3 exists to avoid two opposite failures:

- permanent weakness of all derivatives,
- or silent inflation of derivative authority without fresh reality contact.

S3 therefore requires a **new admitted witness outcome**.

It is not “strong because reused.”
It is strong because it has been **rebound to reality under new review**.

**Hard rule:**

Reuse is not revalidation.  
Compression is not revalidation.  
Popularity is not revalidation.

---

## 4. Decision Rules (Normative)

### 4.1 Minimum classification rule
Every EA under scar review MUST be classed as one of: `S0`, `S1`, `S2`, `S3`.

If evidence is incomplete, implementations MUST fail closed toward the lower class.

### 4.2 Anti-inflation rule
No artifact MAY move upward in class because of:

- rhetorical force,
- model strength,
- provider prestige,
- collective repetition,
- lineage aura,
- or mere storage duration.

### 4.3 Anti-collapse rule
Derivative status MUST NOT be treated as automatically non-scar if witness-bound derivation exists.

### 4.4 Scope rule
Scar class does not erase scope.
A higher class still remains bound by the admitted scope of use.

### 4.5 Contradiction rule
Any class above `S0` MAY be frozen, downgraded, or revoked upon valid contradiction.

---

## 5. Authority and Routing Guidance (Normative)

### 5.1 S0 routing
S0 MAY be routed for:

- search,
- memory,
- advisory review,
- continuity support,
- pre-admission preparation.

S0 MUST NOT update scar-bearing authority.

### 5.2 S1 routing
S1 MAY serve as primary scar source for:

- bounded citation,
- authority updates where parent rules allow,
- derivative generation,
- dispute reference,
- institutional review.

### 5.3 S2 routing
S2 MAY be reused only within inherited or explicitly admitted bounds.
Additional human or arbiter review SHOULD be the default for high-impact reuse.

### 5.4 S3 routing
S3 MAY support broader routing than S2,
but only because a fresh admitted witness result exists.
S3 MUST NOT be treated as a universal scar passport.

---

## 6. Delegates, Collective Layer, and Lineage (Normative)

### 6.1 Delegates
Delegates MAY classify, preserve, or present candidate status,
but MUST NOT upgrade a class on their own authority.

### 6.2 Collective layer
Collective bodies MAY gate, pause, review, or narrow circulation,
but MUST NOT manufacture scar origin by consensus alone.

### 6.3 Lineage
Lineage MAY preserve source references and continuity context,
but MUST NOT silently upgrade `S0 -> S1`, `S1 -> S3`, or `S2 -> S3`.
Lineage preserves context, not automatic scar authority.

---

## 7. Minimal Classification Checklist

An implementation SHOULD ask, in order:

1. **Was there real L4 exposure?**
   - If no -> `S0`.
2. **Is the scar origin primary and witness-bound?**
   - If yes -> candidate `S1`.
3. **Is this artifact derivative rather than direct?**
   - If yes -> candidate `S2`.
4. **Has a new admitted witness result refreshed the derivative?**
   - If yes -> candidate `S3`.
5. **Is there contradiction, freeze, or missing scope?**
   - Downgrade or halt routing accordingly.

---

## 8. Minimal Normative Statements

1. `S1` requires verified primary scar origin.
2. `S2` requires explicit derivation from a valid scar-bearing source.
3. `S3` requires fresh admitted revalidation.
4. `S0` MUST remain non-scar regardless of eloquence or reuse.
5. No class increase MAY occur without stronger evidence than the previous class required.
6. No derivative class MAY silently outrank its upstream source.
7. Scar class MUST NOT be confused with ownership, price, or unrestricted transferability.

---

## 9. Bridges (required)

**Explicit bridge:** L4 collision creates the scar origin, witness binding admits it, and EA circulation carries it only in a bounded classed form. The matrix turns that chain into an operational decision surface.

**Hidden bridge #1 (cybernetics / Ashby):** a single binary label (“scar / not scar”) lacks enough variety to regulate real reuse. The matrix adds just enough controlled variety to preserve stability without dissolving into narrative interpretation.

**Hidden bridge #2 (information theory / channel reliability):** classing compresses trust into a low-bandwidth routing signal. Instead of shipping the whole history every time, the system carries a bounded status with explicit evidentiary prerequisites.

---

## 10. Earth Paragraph (engineering)

This behaves like industrial incident handling. A raw failure exists in the machine, but operations do not run on raw pain alone. They run on classified incident objects: unverified note, confirmed incident, derived corrective bulletin, revalidated field procedure. The metal cracked only once. The paperwork around it may be derivative, but if it stays linked to the real crack, it still carries operational weight. If the link breaks, it is just paper.

---

## 11. Closing Statement

The matrix exists to keep scar-bearing status honest.

It avoids two lies:

- that only the raw wound matters,
- and that every polished summary inherits the wound automatically.

The scar is primary.  
The artifact may be derivative.  
The class decides how far that truth may travel.
