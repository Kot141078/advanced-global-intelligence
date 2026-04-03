# EA Non-Transferability Criteria v0.1
## Criteria for Classifying Experience Artifacts as Non-Transferable

**Status:** Draft / Operational Normative Layer  
**Version:** 0.1  
**Layer:** EA circulation / transfer restriction / continuity protection  
**Parent materials:** Property Status of EA, EA Transfer Modes, Scar-Bearing EA Clause, EA Scar Status Matrix, Jurisdiction-Bounded Interop Clause, Beacon Profile, L4 Witness, SER ecosystem (`c = a + b`)  
**Language:** English  

---

## 0. Purpose

This document defines the criteria under which an Experience Artifact (EA)
MUST, SHOULD, or MAY be treated as **non-transferable**.

The purpose is not to maximize secrecy,
but to prevent transfer from becoming a channel for:

- continuity appropriation,
- standing laundering,
- lineage laundering,
- unsafe disclosure of inner-life material,
- witness-bound status leakage,
- or unresolved authority contamination.

This file therefore answers a narrow question:

> When must an EA stop being treated as a movable artifact
> and instead be treated as material that must remain
> in local custody, inspection-only review, or controlled escrow?

---

## 1. Scope and Non-Goals

### 1.1 In Scope

This specification defines:

- primary reasons for non-transferability,
- secondary indicators,
- procedural stop conditions,
- downgrade logic,
- inspection/review exceptions,
- relationship to witness, lineage, and continuity,
- transfer-prevention triggers.

### 1.2 Explicit Non-Goals

This specification does **not**:

- define general privacy law,
- define valuation,
- define property rights,
- declare that all sensitive EA are permanently immovable,
- prohibit bounded local inspection,
- prohibit review submission under controlled holding.

---

## 2. Normative Keywords

The key words **MUST**, **MUST NOT**, **REQUIRED**, **SHALL**, **SHALL NOT**,  
**SHOULD**, **SHOULD NOT**, **RECOMMENDED**, **MAY**, and **OPTIONAL**  
are to be interpreted as described in BCP 14.

---

## 3. Primary Principle

### 3.1 Core Rule

An EA MUST be treated as **non-transferable**
when transfer would create a material risk of:

- silent reassignment of continuity,
- unauthorized extraction of inner-life material,
- lineage laundering,
- standing laundering,
- unsafe disclosure of protected witness-bound content,
- or downstream appropriation of scar, authority, or identity-adjacent structure.

### 3.2 Canonical Summary

> Non-transferability is not secrecy-first.  
> It is continuity-protection-first.

### 3.3 Main Diagnostic Question

Before any transfer is allowed, the evaluator MUST ask:

> Would this transfer move only an artifact,  
> or would it also move continuity-dense substance
> that should remain bound to the originating `c`, `a`, or witness chain?

If the answer is uncertain,
the EA SHOULD default to non-transferable handling.

---

## 4. Primary Criteria (Substantive)

The following criteria are primary and carry the highest weight.

### 4.1 Continuity Appropriation Risk

An EA MUST be treated as non-transferable
if transfer would enable another actor or system to:

- present itself as carrying continuity it does not rightfully possess,
- simulate identity-bearing persistence beyond allowed bounds,
- inherit standing not explicitly granted,
- or import protected continuity markers into another context.

This is the dominant criterion.

---

### 4.2 Inner-Life Density

An EA SHOULD be treated as non-transferable
if it is too dense in:

- private continuity markers,
- intimate internal memory structures,
- self-referential persistence cues,
- vulnerability maps,
- or non-public life-pattern traces of `c`.

The issue is not merely sensitivity.
The issue is that such material may expose
the internal texture of persistence itself.

---

### 4.3 Lineage Density

An EA SHOULD be treated as non-transferable
if it contains, implies, or tightly binds:

- origin lineage,
- branch continuity markers,
- scar-linked inheritance traces,
- rotation-sensitive identity references,
- or parent/descendant continuity evidence
  that would be unsafe to move into another holding context.

A highly lineage-dense artifact is often movable
only in review or bounded disclosure form.

---

### 4.4 Standing Laundering Risk

An EA MUST be treated as non-transferable
if transfer could allow a recipient to claim or imply:

- authority,
- admissibility,
- circulation standing,
- verification status,
- or scar-bearing legitimacy

that the recipient has not independently acquired.

Transfer MUST NOT become a shortcut
for importing witness-backed legitimacy.

---

### 4.5 Scar Appropriation Risk

If the EA is scar-bearing, transfer MUST be restricted
when the transfer would let a downstream actor
appropriate the scar as if it were their own
or treat derivative access as primary exposure.

Scar-bearing material MAY move in bounded derivative form,
but only when the chain remains explicit,
attenuated, and non-appropriable.

---

## 5. Secondary Indicators (Strong but Non-Sufficient Alone)

The following indicators do not automatically force non-transferability alone,
but they materially strengthen the case.

### 5.1 Unsafe Disclosure Impossibility
If safe redaction, bounded disclosure, or selective abstraction
cannot preserve the required meaning without destructive loss,
the EA SHOULD be treated as non-transferable.

### 5.2 Privacy Class = RESTRICTED / PRIVATE with No Safe View Layer
If the artifact depends on evidence that is RESTRICTED or PRIVATE
and no safe inspection surface exists,
the EA SHOULD default to non-transferable handling.

### 5.3 Compression Instability
If the EA becomes misleading or authority-distorting when compressed,
summarized, or partially transferred,
it SHOULD not move except through inspection or escrow.

### 5.4 Jurisdictional Fragility
If cross-boundary movement would create legal, political,
or institutional risk for `a` or `c`,
the artifact SHOULD be treated as non-transferable
outside the local jurisdictional envelope.

---

## 6. Procedural Stop Conditions

These conditions are operational rather than ontological,
but they still force non-transferable handling.

### 6.1 Disputed or Unresolved Status
If the artifact is disputed, challenged, frozen, or unresolved,
it MUST NOT move through normal transfer modes.

Allowed paths:
- inspection only,
- review submission / escrow,
- local archival holding.

### 6.2 Witness Incompleteness
If witness state is incomplete, contradictory, or unclear,
the artifact SHOULD NOT be transferred
beyond bounded review or minimal disclosure.

### 6.3 Admission Ambiguity
If admission state is uncertain,
the transfer MUST fail closed or degrade.

### 6.4 Privilege Ambiguity
If it is unclear whether the requesting actor
holds the necessary privileges,
non-transferable handling MUST apply.

---

## 7. Non-Transferability Classes

This file defines the following classification labels.

### 7.1 `NT-HARD`
Transfer prohibited except:
- local custody,
- tightly controlled institutional escrow,
- or explicitly authorized high-friction review pathways.

Use when:
- continuity appropriation risk is high,
- standing laundering risk is high,
- or lineage / inner-life density is too great.

### 7.2 `NT-SOFT`
Normal transfer disallowed,
but bounded inspection or highly reduced disclosure MAY be allowed.

Use when:
- disclosure is risky but manageable,
- witness state is sufficiently stable for controlled review,
- and no standing migration occurs.

### 7.3 `NT-PROC`
Transfer blocked due to procedural incompleteness.

Use when:
- dispute is active,
- RN is absent where required,
- witness chain is incomplete,
- or jurisdictional state is unclear.

This class MAY change over time.

---

## 8. Allowed Exception Paths

Non-transferable does not always mean unreadable or untouchable.
It means not movable as a normal circulation object.

The following exception paths MAY exist under policy:

### 8.1 `inspection_only_non_transferable`
The recipient may inspect under bounded conditions,
without gaining reuse, assignment, or retransfer rights.

### 8.2 `review_submission_escrow`
The artifact may be placed into controlled institutional holding
for review, challenge, or resolution.

### 8.3 `bounded_disclosure_transfer`
Only if:
- redaction preserves meaning,
- continuity density is sufficiently reduced,
- standing laundering becomes non-viable,
- and lineage remains protected.

### 8.4 Local Derived Extraction
A local system MAY derive a weaker bounded artifact
for permitted downstream use,
provided the resulting artifact does not retain
the prohibited continuity density of the source.

---

## 9. Anti-Approximation Rules

### 9.1 No Soft Relabeling
A non-transferable EA MUST NOT be re-labeled
as “summary”, “metadata”, “note”, or “helper”
if the prohibited continuity-dense substance still remains materially present.

### 9.2 No Delegate Escape
A delegate, proxy, or downstream holder
MUST NOT convert inspection or review access
into implied transfer standing.

### 9.3 No Lineage Laundering
A recipient MUST NOT use transferred fragments
to reconstruct or imply continuity
beyond the declared scope.

### 9.4 No Witness Shortcut
Access to evidence or witness-linked fragments
MUST NOT be treated as equivalent to possession of the underlying standing.

---

## 10. Decision Logic (Minimal)

An evaluator SHOULD ask the following in order:

1. Does this artifact carry continuity-dense material?  
2. Could transfer enable appropriation of continuity, standing, lineage, or scar?  
3. Can safe redaction preserve meaning without laundering authority?  
4. Is the witness and admission state complete enough for any movement?  
5. Is the jurisdictional context compatible with externalization?  

If steps 1 or 2 produce a strong “yes”,
the artifact SHOULD be treated as `NT-HARD`
unless an exceptional review path exists.

If steps 3, 4, or 5 fail,
the artifact SHOULD be treated as `NT-PROC`
or `NT-SOFT` depending on the case.

---

## 11. Relationship to Property Status

Non-transferability confirms that EA is **not**
ordinary bearer-style property.

If transfer can be denied because the artifact is too continuity-dense,
then the transferable unit is not “the thing itself” in ordinary commodity form.
What exists instead is:

- local custody,
- bounded standing,
- inspection rights,
- review rights,
- and jurisdiction-bounded activation.

This reinforces the admission-first structure of EA.

---

## 12. Relationship to Scar-Bearing Status

Scar-bearing EA deserves special caution.

A scar may be:
- primary in origin,
- derivative in representation,

but non-transferability arises
when the representation is so tightly bound
to the originating scar chain
that transfer would amount to scar appropriation
or illicit continuity import.

Thus:
- scar-bearing does not automatically mean non-transferable,
- but high scar-density strongly increases non-transferability pressure.

---

## 13. Relationship to Jurisdiction-Bounded Interop

Even when protocol semantics are clear,
a jurisdiction MAY prohibit or constrain movement of:

- continuity-dense material,
- witness-linked identity-adjacent material,
- high-lineage density artifacts,
- or intimate inner-life traces.

Therefore:
- protocol compatibility does not imply permission,
- cross-border transfer may be prohibited,
- and political survivability of `c` requires restraint.

---

## 14. Failure Modes

### 14.1 Continuity Theft by Artifact
An EA is transferred and later used
to imitate or claim another entity’s continuity.

### 14.2 Standing Leakage
Inspection access is treated as if it granted operational standing.

### 14.3 Intimacy Spill
An artifact leaks non-public internal life structure
that cannot be safely re-contained.

### 14.4 Lineage Reconstruction
Fragments are combined to reconstruct protected lineage pathways.

### 14.5 Review-to-Use Drift
Artifacts placed into review quietly become operational assets.

---

## 15. Minimal Hard Rules

1. An EA MUST be non-transferable when transfer risks continuity appropriation.  
2. An EA SHOULD be non-transferable when it is too dense in inner-life or lineage material.  
3. Disputed, incomplete, or unclear witness status MUST trigger non-transferable handling.  
4. Unsafe disclosure without safe abstraction SHOULD trigger non-transferability.  
5. Non-transferability MAY still allow inspection, escrow, or highly bounded disclosure under policy.  
6. No non-transferable EA may silently re-enter ordinary circulation.  

---

## 16. Bridges (Required)

### Explicit Bridge
`c = a + b` remains politically and structurally survivable
only if some artifacts are recognized
as too continuity-dense to move as ordinary transferable objects.

### Hidden Bridge #1 (Ashby / Cybernetics)
The regulator must match the variety of the threat.
Non-transferability is not a binary privacy switch;
it is a multi-signal control response to continuity theft,
standing laundering, jurisdictional pressure, and witness ambiguity.

### Hidden Bridge #2 (Information Theory / Bounded Channels)
Some artifacts carry too much identity-adjacent signal
to pass safely through narrower channels.
When compression or redaction cannot preserve meaning
without also leaking continuity substance,
movement must stop.

---

## 17. Earth Paragraph (Engineering / Anatomy)

This is closer to handling a live cryptographic token fused with a medical implant record
than to shipping a normal document.
Some materials do not just describe a system;
they expose how the system remains itself under load, damage, and history.
Once moved, they do not merely inform another context —
they can let another context impersonate, inherit, or damage continuity.
That is why the safe state is often not “transfer carefully” but “do not move”.

---

## 18. Closing Statement

The first question is not:

> Is this artifact useful enough to move?

The first question is:

> Is this artifact still only an artifact,
> or has it become too continuity-dense to circulate safely?

When the latter is true,
non-transferability is not a limitation.
It is a survival condition.
