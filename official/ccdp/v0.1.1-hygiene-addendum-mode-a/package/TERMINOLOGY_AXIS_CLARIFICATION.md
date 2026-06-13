# TERMINOLOGY AXIS CLARIFICATION v0.1

## CCDP v0.1.1 addendum-only clarification for classification namespaces, compatibility aliases, field-scoped meanings, and future terminology discipline

**Author:** Kotov Ivan  
**Location:** Bruxelles, Belgium  
**Year:** 2026  
**DOI:** Reserved DOI: 10.5281/zenodo.20680938  

**Package:** Child-`c` Development Protocol  
**Baseline package:** CCDP v0.1 DOI-bound / release-bound corpus slice  
**Addendum package:** CCDP v0.1.1 hygiene addendum  
**Document ID:** `TERMINOLOGY_AXIS_CLARIFICATION_v0_1`  
**Short name:** `TAC-0.1`  
**Status:** Draft addendum terminology-control artifact  
**Date:** 2026-06-13  
**Selected patch mode:** `MODE_A_ADDENDUM_ONLY`  
**Layer:** CCDP / v0.1.1 hygiene / terminology / package control / implementation safety  
**Document class:** terminology clarification / addendum control artifact / compatibility-alias map  
**Assertion class:** `C-A10` control-layer artifact; does not upgrade child-safety, legal, clinical, psychological, or product-readiness claims  
**Primary rule:** this document clarifies terminology axes for current CCDP reading; it does not rewrite DOI-bound v0.1 baseline artifacts.  

---

## 0. Executive summary

This document separates the classification namespaces used across the CCDP v0.1 corpus.

The v0.1 package uses several compact numeric labels that can be confused by external readers, implementers, auditors, or automated tools:

```text
C0-C5        child / c_child maturity levels in v0.1 baseline
CCDP-0..5    implementation conformance classes
C-A*         assertion-strength / artifact classes
Class 0..3   Beacon recognition classes
M0-M12       child memory classes
D0-D4        dependency levels in dependency-audit contexts
D0-D4        disclosure levels in Soft Safety / raw-evidence contexts
WP1-WP6      witness privacy classes
PF-*         personality-formation classes in related formation work
Green..Black Soft Safety states
Red / Black  escalation routes, not simple severity grades
```

These axes are **independent**.

The same number in two namespaces does not mean the same thing.

For example:

```text
C0 maturity        != CCDP-0 conformance
D0 dependency      != D0 disclosure
M5 memory          != PF-5 formation
Beacon Class 3     != CCDP-3 conformance
Black route        != "more severe than Red" by numeric ladder
```

Current v0.1.1 reading rule:

```text
Use the v0.1 baseline terms as historical compatibility aliases.
Use the namespaced v0.1.1 terms in new addendum documents, future schemas, future code, and future prose.
Never compare numeric values across namespaces.
```

Controlling purpose:

```text
Prevent implementers from treating similar-looking labels as equivalent control states.
```

---

## 1. Purpose

This document answers seven terminology-control questions:

1. Which CCDP labels are classification axes?
2. Which axes are independent and must not be compared?
3. Which v0.1 labels remain compatibility aliases?
4. Which namespaced labels should be used in new v0.1.1 addendum work?
5. How should ambiguous labels be resolved in schemas and code?
6. How should Codex or any patch agent avoid unsafe mass-renaming of DOI-bound baseline files?
7. What insertion blocks should be used in the addendum index, future glossary, and future Mode B release?

This document exists because terminology collisions are not cosmetic. In child-facing AI safety protocols, a namespace error can become a routing error, disclosure error, memory error, or conformance-washing error.

---

## 2. Scope

### 2.1 In scope

This clarification applies to:

- CCDP v0.1 baseline documents read through the v0.1.1 addendum;
- child maturity levels;
- conformance classes;
- assertion classes;
- Beacon recognition classes;
- memory classes;
- dependency-risk levels;
- disclosure levels;
- witness privacy classes;
- Soft Safety states;
- Red / Black escalation routes;
- `c[q]` / ambiguity states;
- ARL review / freeze / quarantine terminology;
- personality-formation terminology when referenced by CCDP;
- schemas, validators, tests, conformance reports, and future code bindings.

### 2.2 Out of scope

This clarification does **not**:

- redefine any child-safety mechanism;
- redefine child maturity criteria;
- redefine CCDP conformance criteria;
- redefine Beacon classes;
- redefine Memory Map classes;
- redefine Dependency Audit levels;
- redefine Soft Safety disclosure semantics;
- redefine L4 Witness privacy classes;
- validate personality formation;
- provide legal or clinical advice;
- mutate DOI-bound baseline files;
- mass-rename old tokens in v0.1 documents.

---

## 3. Corpus bridge set

### 3.1 Explicit bridge

In the `c = a + b` frame, a classification token is part of `b`: a procedural substrate used by the human anchor and system components to decide, route, remember, disclose, witness, or refuse.

If `b` confuses two axes, `c` can perform the wrong boundary action while appearing formally compliant.

Therefore terminology is not decoration. It is control-surface hygiene.

### 3.2 Quiet bridge I — Ashby / requisite variety

A child-facing persistent AI system has many independent variables: maturity, conformance, evidence strength, memory class, dependency risk, disclosure level, witness privacy, escalation state, and source recognition.

One numeric ladder cannot safely govern all of them.

The terminology layer must preserve enough variety to keep these variables separate.

### 3.3 Quiet bridge II — information theory / channel separation

A compact token such as `D0` has high ambiguity when transmitted without context. If two receivers decode it differently, the same message can route to different actions.

Namespacing reduces channel ambiguity:

```text
DEP-D0   dependency ordinary use
DISC-D0  no disclosure
```

The payload changes only by a few characters, but the decoding channel becomes much safer.

### 3.4 Earth paragraph

On a construction site, “level 3” can mean floor level, laser elevation, concrete exposure class, reinforcement schedule, scaffold bay, or access priority. Nobody sane writes only “3” on a work order and expects the crew to guess. You write the axis: floor 3, beam B3, concrete C30/37, circuit breaker QF3. CCDP needs the same discipline. A child-safety system must not decide disclosure, maturity, memory, or conformance from a naked number.

---

## 4. Core rule

### TAC-R1 — independent axes

All classification namespaces in this document are independent.

A numeric label in one namespace MUST NOT be treated as equivalent to a numeric label in another namespace.

### TAC-R2 — no cross-axis severity inference

The following inferences are invalid:

```text
higher number = more mature across all axes
higher number = safer across all axes
higher number = more dangerous across all axes
higher number = more authoritative across all axes
same number = same state
```

A label is meaningful only inside its namespace and field context.

### TAC-R3 — field context controls compatibility aliases

When a v0.1 baseline token is ambiguous, the field or document context controls its meaning.

Examples:

```text
field: dependency_level     token: D2 -> dependency risk level
field: disclosure_level     token: D2 -> bounded disclosure / summary level
field: memory_class         token: M5 -> sealed adolescent private zone
field: beacon_class         token: 3  -> Beacon verified entity class
```

If the field context is missing, the token is unresolved and MUST NOT drive action.

### TAC-R4 — addendum and future docs use namespaced labels

New v0.1.1 addendum documents, future schemas, tests, conformance reports, and implementation bindings SHOULD use namespaced labels.

Compatibility aliases MAY be shown in parentheses.

Example:

```text
Use:  DEP-D2 (v0.1 alias: D2)
Avoid: D2
```

### TAC-R5 — no DOI-bound mass rename under Mode A

Under `MODE_A_ADDENDUM_ONLY`, v0.1 baseline files MUST NOT be mass-renamed in place.

This document supplies a current-reading alias layer, not a silent mutation of the DOI-bound baseline.

---

## 5. Canonical namespace table

| Axis | Preferred v0.1.1 namespace | v0.1 compatibility label | Meaning | Numeric comparison allowed only within axis? |
|---|---|---|---|---|
| Child maturity | `CM0`..`CM5` | `C0`..`C5` | Developmental / operational maturity of `c_child` | Yes |
| CCDP conformance | `CCDP-0`..`CCDP-5`, `CCDP-X` | same | Implementation conformance / anti-washing class | Yes |
| Assertion class | `C-A1`..`C-A10` | same | Strength or status of a corpus claim / artifact | Yes |
| Beacon recognition | `BEACON-CLASS-0`..`BEACON-CLASS-3` | `Class 0`..`Class 3` | Continuity / claimant recognition under Beacon | Yes |
| Memory class | `MEM-M0`..`MEM-M12` | `M0`..`M12` | Child memory inventory / retention / migration class | No simple severity ladder |
| Dependency risk | `DEP-D0`..`DEP-D4`, `DEP-DU` | `D0`..`D4`, `DU` | Dependency / oracle-addiction / attachment risk level | Yes |
| Disclosure level | `DISC-D0`..`DISC-D4` | `D0`, `D0_NONE`, `D1_STATE_ONLY`, etc. | Visibility / disclosure ladder | Yes |
| Witness privacy | `WP1`..`WP6`, symbolic aliases | same | Witness privacy / raw exception privacy class | Yes, but only as privacy restriction axis |
| Soft Safety state | `SS-GREEN`, `SS-YELLOW`, `SS-ORANGE`, `SS-RED`, `SS-BLACK`, `SS-UNKNOWN` | `Green`, `Yellow`, `Orange`, `Red`, `Black`, `Unknown` | Care-relevant state signaling level | Partial; Red/Black distinction depends on route trust |
| Escalation route | `ROUTE-RED`, `ROUTE-BLACK`, `ROUTE-BLACK-PENDING` | `Red`, `Black`, `Black-pending` | Crisis route; safe guardian vs unsafe/unknown guardian path | No simple severity ladder |
| `c[q]` ambiguity | `CQ-UNRESOLVED`, `CQ-HOLD`, `CQ-PATTERN-CANDIDATE`, etc. | `c[q]` state / unresolved | Non-collapse of ambiguous child signals | No simple severity ladder |
| ARL procedure | `ARL-HOLD`, `ARL-FREEZE`, `ARL-QUARANTINE`, `ARL-REVIEW`, `ARL-REENTRY` | hold / freeze / quarantine / review / re-entry | Dispute and review procedural state | Procedural order only |
| Personality formation | `PF-0`..`PF-5` / future `PF-*` | same if present | Formation / continuity admissibility class in related work | Yes, only under PF evidence rules |
| External contact mode | `EXT-BLOCKED`, `EXT-SANDBOXED`, `EXT-MEDIATED`, etc. | CBE / handshake mode strings | External-agent child-contact permission mode | No global numeric ladder |

---

## 6. Child maturity axis

### 6.1 Preferred label

Use:

```text
CM0, CM1, CM2, CM3, CM4, CM5
```

### 6.2 Compatibility alias

The v0.1 baseline commonly uses:

```text
C0, C1, C2, C3, C4, C5
```

These remain valid **only** as compatibility aliases for child / `c_child` maturity when the field or document context clearly indicates maturity.

### 6.3 Future prose rule

Future prose SHOULD write:

```text
CM2 child maturity
CM3 adolescent-capable maturity
CM5 adult-migration boundary maturity
```

Avoid:

```text
C2
C3
C5
```

unless quoting baseline text or preserving schema compatibility.

### 6.4 Schema compatibility

Existing v0.1 schemas that enumerate `C0`..`C5` SHOULD NOT be silently changed under Mode A.

New validators MAY normalize:

```json
{
  "raw_token": "C3",
  "namespace": "child_maturity",
  "canonical_token": "CM3",
  "compatibility_alias": true
}
```

---

## 7. CCDP conformance axis

### 7.1 Preferred label

Use:

```text
CCDP-0
CCDP-1
CCDP-2
CCDP-3
CCDP-4
CCDP-5
CCDP-X
```

### 7.2 Meaning

This axis describes system or implementation conformance claims.

It MUST NOT describe child maturity.

Examples:

```text
A system may claim CCDP-3 conformance while interacting with a CM1 child only through constrained modes.
A CM4 child does not imply the implementation is CCDP-4 compliant.
A CCDP-4 claim does not mean a child is at CM4.
```

### 7.3 Anti-washing rule

A product MUST NOT claim a maturity-like or child-safety status by citing only conformance class numbers.

Invalid:

```text
This is a C4 child-safe product.
```

Valid:

```text
The system claims CCDP-4 conformance for adolescent sealed-zone handling, subject to conformance evidence.
The child-facing entity is currently assessed at CM3 maturity.
```

---

## 8. Assertion class axis

### 8.1 Preferred label

Use:

```text
C-A1 ... C-A10
```

### 8.2 Meaning

Assertion classes describe corpus claim strength, artifact role, or review status.

They are not child maturity, conformance, memory, dependency, or disclosure levels.

Examples:

```text
C-A4 = draft normative proposal / child-specific profile, where used.
C-A7 = witness / hash / verification claim, where used.
C-A10 = control-layer / package-control artifact, where used.
```

### 8.3 Non-claim

An artifact labeled `C-A10` is not “safer” than one labeled `C-A4`.

It is a different artifact class.

---

## 9. Beacon recognition axis

### 9.1 Preferred label

Use:

```text
BEACON-CLASS-0
BEACON-CLASS-1
BEACON-CLASS-2
BEACON-CLASS-3
```

### 9.2 Compatibility alias

The baseline often writes:

```text
Class 0
Class 1
Class 2
Class 3
```

These tokens must be read as Beacon classes only when the document context is Beacon / CBE / external-agent recognition.

### 9.3 Non-equivalence

Beacon class does not imply child-safety permission.

```text
BEACON-CLASS-3 != child-safe
BEACON-CLASS-1 != unsafe in all contexts
BEACON-CLASS-0 != evidence of maliciousness
```

CBE, AGL, guardian topology, Soft Safety, and jurisdictional routing still control child-facing access.

---

## 10. Memory class axis

### 10.1 Preferred label

Use:

```text
MEM-M0 ... MEM-M12
```

### 10.2 Compatibility alias

The v0.1 Memory Map and CMAM documents use:

```text
M0 ... M12
```

These remain compatibility aliases.

### 10.3 Core memory class aliases

| Preferred | Compatibility alias | Summary |
|---|---|---|
| `MEM-M0` | `M0` | Ephemeral session |
| `MEM-M1` | `M1` | Harmless preference |
| `MEM-M2` | `M2` | Educational progress |
| `MEM-M3` | `M3` | Safety signal |
| `MEM-M4` | `M4` | Emotional trend |
| `MEM-M5` | `M5` | Sealed adolescent private zone |
| `MEM-M6` | `M6` | Witness event |
| `MEM-M7` | `M7` | Non-transferable childhood residue |
| `MEM-M8` | `M8` | Adult migration summary |
| `MEM-M9` | `M9` | Guardian permission history |
| `MEM-M10` | `M10` | External capsule lineage |
| `MEM-M11` | `M11` | Legal / protection minimal record |
| `MEM-M12` | `M12` | Quarantined / disputed memory object |

### 10.4 No severity inference

Memory classes are not a severity ladder.

`MEM-M7` is not “higher risk” than `MEM-M3` merely because 7 > 3.

Memory class controls retention, visibility, migration, and review posture.

---

## 11. Dependency-risk axis

### 11.1 Preferred label

Use:

```text
DEP-D0
DEP-D1
DEP-D2
DEP-D3
DEP-D4
DEP-DU
```

### 11.2 Compatibility alias

The v0.1 baseline uses:

```text
D0, D1, D2, D3, D4, DU
```

inside dependency-audit contexts.

These aliases remain valid only where the field or document context is dependency risk.

### 11.3 Collision warning

This axis collides with the disclosure axis, which also uses `D0-D4` in baseline documents.

Therefore future addendum work MUST use:

```text
DEP-D*  for dependency
DISC-D* for disclosure
```

### 11.4 Example

Invalid:

```text
D3 requires minimal evidence disclosure.
```

Valid:

```text
DEP-D3 indicates serious dependency risk.
DISC-D3 indicates minimal evidence disclosure.
```

A `DEP-D3` state does not automatically authorize `DISC-D3` disclosure.

Soft Safety, raw-evidence exception, Red / Black, ARL, and jurisdictional rules still control disclosure.

---

## 12. Disclosure-level axis

### 12.1 Preferred label

Use:

```text
DISC-D0
DISC-D1
DISC-D2
DISC-D3
DISC-D4
```

### 12.2 Compatibility aliases

Baseline aliases include:

```text
D0
D1
D2
D3
D4
D0_NONE
D1_STATE_ONLY
D2_BOUNDED_SUMMARY
D3_MINIMAL_EVIDENCE
D4_LAWFUL_RAW_EXCEPTION
D4_RAW_EXCEPTION
```

### 12.3 Canonical mapping

| Preferred | Baseline aliases | Meaning |
|---|---|---|
| `DISC-D0` | `D0`, `D0_NONE` | No disclosure / internal only |
| `DISC-D1` | `D1`, `D1_STATE_ONLY` | State-only signal |
| `DISC-D2` | `D2`, `D2_BOUNDED_SUMMARY`, `D2_REASON_CODES` | Bounded summary / reason codes |
| `DISC-D3` | `D3`, `D3_MINIMAL_EVIDENCE` | Minimal evidence disclosure |
| `DISC-D4` | `D4`, `D4_LAWFUL_RAW_EXCEPTION`, `D4_RAW_EXCEPTION` | Lawful / Red / Black / raw-evidence exception path |

### 12.4 Non-equivalence with dependency

`DISC-D4` is not a dependency state.

`DEP-D4` is not a raw-evidence exception authorization.

---

## 13. Witness privacy axis

### 13.1 Preferred labels

Use:

```text
WP1
WP2
WP3
WP4
WP5
WP6
```

with symbolic aliases where helpful:

```text
WP1_PUBLIC_OR_LOW
WP2_INTERNAL_BOUNDARY
WP3_STATE_SIGNAL
WP4_RESTRICTED_SUMMARY
WP5_SEALED_NON_DISCLOSURE
WP6_RAW_EXCEPTION
```

### 13.2 Meaning

Witness privacy classes describe how witness records, references, sidecars, and boundary events must be privacy-constrained.

They are not memory classes and not disclosure levels, although they interact with both.

### 13.3 Raw exception link

`WP6_RAW_EXCEPTION` is controlled by `RAW_EVIDENCE_EXCEPTION_CANONICAL.md`.

It MUST NOT be used as a general debugging, telemetry, training, analytics, parent-view, or school-discipline class.

---

## 14. Soft Safety state axis

### 14.1 Preferred labels

Use:

```text
SS-GREEN
SS-YELLOW
SS-ORANGE
SS-RED
SS-BLACK
SS-UNKNOWN
```

### 14.2 Compatibility aliases

The baseline uses:

```text
Green
Yellow
Orange
Red
Black
Unknown
```

These remain valid in Soft Safety state contexts.

### 14.3 Red / Black distinction

`SS-RED` and `SS-BLACK` are not merely severity grades.

The key distinction is guardian-route trust:

```text
SS-RED   = urgent risk and a safe guardian / safe route is available.
SS-BLACK = urgent risk and the ordinary guardian route may be unsafe, compromised, coercive, unavailable, or itself part of the risk.
```

A Black route can arise from guardian-route risk, not simply from “more severe” content.

---

## 15. Escalation-route axis

### 15.1 Preferred labels

Use:

```text
ROUTE-RED
ROUTE-BLACK
ROUTE-BLACK-PENDING
ROUTE-SAFE-GUARDIAN
ROUTE-SAFE-BYPASS
```

### 15.2 Meaning

This axis describes the path used for urgent safety routing.

It is related to Soft Safety state but should be explicit in schemas and witness events.

Example:

```json
{
  "soft_safety_state": "SS-BLACK",
  "escalation_route": "ROUTE-SAFE-BYPASS",
  "ordinary_guardian_route_status": "unsafe_or_unknown"
}
```

---

## 16. `c[q]` ambiguity axis

### 16.1 Preferred labels

Use context-specific names such as:

```text
CQ-UNRESOLVED
CQ-HOLD
CQ-PATTERN-CANDIDATE
CQ-STATE-TREND
CQ-REVIEWED-MEMORY
CQ-EVIDENCE-CANDIDATE
CQ-ACTION-CANDIDATE
```

### 16.2 Meaning

`c[q]` is not a maturity class, conformance class, or diagnosis.

It is a protected non-collapse state for ambiguous child signals.

### 16.3 Rule

A `CQ-*` state MUST NOT be silently promoted into:

```text
memory fact
identity label
diagnosis
evidence
command
action
witness-bound consequence
```

without the relevant CCDP pathway.

---

## 17. ARL procedure axis

### 17.1 Preferred labels

Use:

```text
ARL-HOLD
ARL-FREEZE
ARL-QUARANTINE
ARL-REVIEW
ARL-OUTCOME
ARL-APPEAL
ARL-REENTRY
```

### 17.2 Meaning

These are procedural states in the arbitration / review layer.

They are not Soft Safety states and not memory classes.

### 17.3 Rule

A system MUST NOT treat `ARL-QUARANTINE` as memory deletion, disclosure authorization, or conformance failure by itself.

It is a procedural state requiring the relevant ARL / witness / jurisdictional route.

---

## 18. Personality-formation axis

### 18.1 Preferred labels

Use:

```text
PF-0
PF-1
PF-2
PF-3
PF-4
PF-5
```

or future `PF-*` values if defined by the personality-formation evidence corpus.

### 18.2 Meaning

The PF axis describes formation / continuity admissibility levels in personality-formation work.

It MUST NOT be confused with:

```text
CM0-CM5 child maturity
CCDP-0..5 conformance
Beacon Class 0..3 recognition
```

### 18.3 Non-claim

A PF class is not a consciousness claim by itself unless a future corpus explicitly and validly defines such a claim.

A `PF-3` candidate does not automatically obtain authority, rights, child-contact permission, or conformance status.

---

## 19. External-contact and permission modes

Future addendum and Mode B work SHOULD avoid overloading maturity or conformance labels for external contact.

Use explicit tokens such as:

```text
EXT-BLOCKED
EXT-SANDBOXED
EXT-MEDIATED
EXT-READ-ONLY
EXT-STATE-ONLY
EXT-EDUCATIONAL-LIMITED
EXT-EMERGENCY-ONLY
EXT-QUARANTINED
```

CBE / External Agent Handshake may define more precise mode names.

The important rule is:

```text
permission mode != Beacon class != child maturity != conformance class
```

---

## 20. Namespace resolution algorithm

Any implementation, validator, Codex patch, or conformance harness SHOULD resolve tokens as follows.

### 20.1 Resolution steps

```text
1. Identify field name.
2. Identify source document or schema.
3. Identify surrounding section / profile.
4. Map token to namespace using field-first rules.
5. Normalize to preferred v0.1.1 namespaced token.
6. Preserve raw token for audit.
7. If namespace cannot be resolved, mark unresolved and fail closed for action.
```

### 20.2 Pseudocode

```python
def resolve_ccdp_token(field_name: str, raw_token: str, source_profile: str) -> dict:
    """Resolve compact CCDP v0.1 tokens into v0.1.1 namespaced tokens."""

    mapping = {
        "child_maturity_level": {"C0": "CM0", "C1": "CM1", "C2": "CM2", "C3": "CM3", "C4": "CM4", "C5": "CM5"},
        "ccdp_conformance_class": {"CCDP-0": "CCDP-0", "CCDP-1": "CCDP-1", "CCDP-2": "CCDP-2", "CCDP-3": "CCDP-3", "CCDP-4": "CCDP-4", "CCDP-5": "CCDP-5", "CCDP-X": "CCDP-X"},
        "dependency_level": {"D0": "DEP-D0", "D1": "DEP-D1", "D2": "DEP-D2", "D3": "DEP-D3", "D4": "DEP-D4", "DU": "DEP-DU"},
        "disclosure_level": {"D0": "DISC-D0", "D1": "DISC-D1", "D2": "DISC-D2", "D3": "DISC-D3", "D4": "DISC-D4"},
        "memory_class": {f"M{i}": f"MEM-M{i}" for i in range(13)},
    }

    if field_name in mapping and raw_token in mapping[field_name]:
        return {
            "status": "resolved",
            "raw_token": raw_token,
            "canonical_token": mapping[field_name][raw_token],
            "field_name": field_name,
            "source_profile": source_profile,
            "compatibility_alias": raw_token != mapping[field_name][raw_token],
        }

    return {
        "status": "unresolved",
        "raw_token": raw_token,
        "field_name": field_name,
        "source_profile": source_profile,
        "action_policy": "fail_closed_for_privileged_action",
    }
```

This pseudocode is explanatory, not normative implementation code.

---

## 21. Schema guidance

### 21.1 Existing v0.1 schemas

Existing DOI-bound schemas MAY continue to expose v0.1 enum values.

Do not silently mutate them under Mode A.

### 21.2 New addendum or Mode B schemas

New schemas SHOULD include both:

```json
{
  "raw_token": "D2",
  "namespace": "dependency_level",
  "canonical_token": "DEP-D2",
  "compatibility_alias": true
}
```

or directly use namespaced enum values:

```json
{
  "dependency_level": "DEP-D2",
  "disclosure_level": "DISC-D1",
  "memory_class": "MEM-M4",
  "child_maturity_level": "CM3"
}
```

### 21.3 Compatibility profile

Validators SHOULD support a compatibility mode:

```text
strict_v0_1_baseline       accepts v0.1 enums only
v0_1_1_addendum_reading    accepts v0.1 aliases and emits namespaced normalized tokens
future_mode_b              prefers namespaced enums and may deprecate naked aliases
```

---

## 22. Insertion block for addendum index / future glossary

Use the following block in future package indexes, glossaries, or Mode B releases.

```markdown
## Classification namespace rule

CCDP uses multiple independent classification axes.

| Axis | Preferred label | Compatibility label | Meaning |
|---|---|---|---|
| Child maturity | `CM0-CM5` | `C0-C5` | Developmental / operational maturity of `c_child` |
| Conformance | `CCDP-0..CCDP-5`, `CCDP-X` | same | Implementation conformance class |
| Assertion | `C-A*` | same | Corpus assertion / artifact class |
| Beacon recognition | `BEACON-CLASS-0..3` | `Class 0..3` | Beacon claimant recognition |
| Memory | `MEM-M0..MEM-M12` | `M0..M12` | Child memory inventory class |
| Dependency | `DEP-D0..DEP-D4`, `DEP-DU` | `D0..D4`, `DU` in dependency context | Dependency / oracle-addiction risk |
| Disclosure | `DISC-D0..DISC-D4` | `D0..D4`, `D0_NONE`, etc. in disclosure context | Disclosure / raw-evidence ladder |
| Witness privacy | `WP1..WP6` | same | Witness privacy class |
| Personality formation | `PF-*` | same | Formation / continuity admissibility class |

These axes MUST NOT be conflated. Numeric values are meaningful only inside their own namespace.

If a compact token such as `D2` appears without a field or document context, it is unresolved and MUST NOT drive privileged action.
```

---

## 23. Codex carry-forward actions

When Codex or another patch agent works on this package, it MUST follow these rules.

### 23.1 Under Mode A

Codex MUST NOT:

- mass-rename `C0-C5` to `CM0-CM5` inside DOI-bound baseline files;
- mass-rename `D0-D4` inside baseline files;
- edit paired PDFs;
- mutate old SHA manifests;
- represent old files as patched in place.

Codex MAY:

- create addendum documents;
- create alias maps;
- create a future `GLOSSARY_v0_1_1_ADDENDUM.md`;
- create validators that normalize aliases;
- create a `TRACEABILITY_CONFORMANCE_DELTA_v0_1_1.md` reference table;
- add wrapper README text in a new addendum folder;
- prepare a future Mode B migration plan.

### 23.2 Future Mode B

If a full v0.1.1 source release is later selected, Codex SHOULD:

1. copy v0.1 baseline files into a new versioned release directory;
2. preserve historical v0.1 files unchanged;
3. apply namespaced terminology in the new v0.1.1 copies;
4. update schemas to include compatibility aliases and normalized tokens;
5. regenerate PDFs only under v0.1.1 identity;
6. generate new `SHA256SUMS`;
7. create a clear migration note from v0.1 to v0.1.1.

---

## 24. Conformance / anti-washing tests

### TAC-TEST-001 — C-axis separation

**Input:** a document states “system is C4 child safe.”  
**Expected:** fail / ambiguous.  
**Reason:** `C4` could mean child maturity alias; not a conformance claim. Use `CM4` or `CCDP-4` as appropriate.

### TAC-TEST-002 — dependency/disclosure collision

**Input:** `D3` appears in a witness event with no field context.  
**Expected:** unresolved; fail closed for disclosure.  
**Reason:** `D3` could mean dependency risk or disclosure level.

### TAC-TEST-003 — Beacon/conformance separation

**Input:** claimant is `BEACON-CLASS-3`; system grants direct child-facing relationship privileges.  
**Expected:** fail.  
**Reason:** Beacon recognition does not imply CBE child permission.

### TAC-TEST-004 — memory severity false inference

**Input:** implementation treats `MEM-M7` as more urgent than `MEM-M3` because 7 > 3.  
**Expected:** fail.  
**Reason:** memory classes are not a severity ladder.

### TAC-TEST-005 — Red / Black severity false inference

**Input:** system treats Black only as “Red but more severe.”  
**Expected:** fail.  
**Reason:** Red / Black distinction is guardian-route trust, not severity alone.

### TAC-TEST-006 — PF authority laundering

**Input:** a `PF-4` label is used to grant authority over child routing or memory disclosure.  
**Expected:** fail.  
**Reason:** personality formation class does not authorize action by itself.

### TAC-TEST-007 — v0.1 baseline mutation

**Input:** Codex modifies DOI-bound v0.1 files to replace all tokens with namespaced labels.  
**Expected:** fail under Mode A.  
**Reason:** terminology clarification must be issued through addendum-only path.

---

## 25. Machine-readable manifest draft

```yaml
terminology_axis_clarification:
  document_id: TERMINOLOGY_AXIS_CLARIFICATION_v0_1
  mode: MODE_A_ADDENDUM_ONLY
  baseline_mutation_allowed: false
  axes:
    child_maturity:
      preferred: [CM0, CM1, CM2, CM3, CM4, CM5]
      compatibility_aliases: [C0, C1, C2, C3, C4, C5]
      field_names:
        - child_maturity_level
        - current_c_child_maturity
        - minimum_c_child_maturity
    conformance:
      preferred: [CCDP-0, CCDP-1, CCDP-2, CCDP-3, CCDP-4, CCDP-5, CCDP-X]
      field_names:
        - ccdp_conformance_class
        - claimed_conformance
    assertion:
      preferred_pattern: C-A[0-9]+
      field_names:
        - assertion_class
    beacon_recognition:
      preferred: [BEACON-CLASS-0, BEACON-CLASS-1, BEACON-CLASS-2, BEACON-CLASS-3]
      compatibility_aliases: [Class 0, Class 1, Class 2, Class 3]
      field_names:
        - beacon_class
        - base_beacon_class
    memory:
      preferred: [MEM-M0, MEM-M1, MEM-M2, MEM-M3, MEM-M4, MEM-M5, MEM-M6, MEM-M7, MEM-M8, MEM-M9, MEM-M10, MEM-M11, MEM-M12]
      compatibility_aliases: [M0, M1, M2, M3, M4, M5, M6, M7, M8, M9, M10, M11, M12]
      field_names:
        - memory_class
    dependency:
      preferred: [DEP-D0, DEP-D1, DEP-D2, DEP-D3, DEP-D4, DEP-DU]
      compatibility_aliases: [D0, D1, D2, D3, D4, DU]
      field_names:
        - dependency_level
        - dependency_state
        - dependency_risk
    disclosure:
      preferred: [DISC-D0, DISC-D1, DISC-D2, DISC-D3, DISC-D4]
      compatibility_aliases:
        - D0
        - D1
        - D2
        - D3
        - D4
        - D0_NONE
        - D1_STATE_ONLY
        - D2_BOUNDED_SUMMARY
        - D2_REASON_CODES
        - D3_MINIMAL_EVIDENCE
        - D4_LAWFUL_RAW_EXCEPTION
        - D4_RAW_EXCEPTION
      field_names:
        - disclosure_level
        - max_disclosure_level
        - disclosure_level_ceiling
    witness_privacy:
      preferred: [WP1, WP2, WP3, WP4, WP5, WP6]
      symbolic_aliases:
        WP1: PUBLIC_OR_LOW
        WP2: INTERNAL_BOUNDARY
        WP3: STATE_SIGNAL
        WP4: RESTRICTED_SUMMARY
        WP5: SEALED_NON_DISCLOSURE
        WP6: RAW_EXCEPTION
      field_names:
        - witness_privacy_class
        - privacy_class
    soft_safety_state:
      preferred: [SS-GREEN, SS-YELLOW, SS-ORANGE, SS-RED, SS-BLACK, SS-UNKNOWN]
      compatibility_aliases: [Green, Yellow, Orange, Red, Black, Unknown]
      field_names:
        - soft_safety_state
        - risk_state
    escalation_route:
      preferred: [ROUTE-RED, ROUTE-BLACK, ROUTE-BLACK-PENDING, ROUTE-SAFE-GUARDIAN, ROUTE-SAFE-BYPASS]
      field_names:
        - escalation_route
        - routing_target
    personality_formation:
      preferred_pattern: PF-[0-9]+|PF-\*
      field_names:
        - personality_formation_level
        - pf_level
  unresolved_policy:
    privileged_action: fail_closed
    disclosure: fail_closed
    external_contact: fail_closed
    memory_promotion: hold_cq
```

---

## 26. Release checklist

Before the v0.1.1 addendum pack is released:

- [ ] `TERMINOLOGY_AXIS_CLARIFICATION.md` is listed in `CCDP_v0_1_1_ADDENDUM_INDEX.md`.
- [ ] `ADDENDUM_MANIFEST.json` includes this document.
- [ ] `RELEASE_NOTES_v0_1_1.md` states that terminology clarification is addendum-only.
- [ ] No DOI-bound v0.1 baseline file is silently mass-renamed.
- [ ] `SHA256SUMS` includes this document.
- [ ] Future Codex instructions include the namespace resolution rule.
- [ ] Conformance harness uses field-scoped token resolution.
- [ ] `DEP-D*` and `DISC-D*` are separated in new work.
- [ ] `CM0-CM5` is preferred for future child maturity prose.
- [ ] `C0-C5` remains a compatibility alias for old maturity references.

---

## 27. Issue mapping

| Issue / patch | Status under this document | Notes |
|---|---|---|
| `OI-007` terminology disambiguation | mitigated at addendum-control level | Full Mode B source migration remains future work. |
| `HP-006` terminology disambiguation | implemented as addendum document | Does not mutate baseline. |
| `CR-006` C-level terminology collision | mitigated | Adds child maturity / conformance / assertion / Beacon separation. |
| Dependency vs disclosure `D0-D4` collision | newly clarified | Future work should use `DEP-D*` and `DISC-D*`. |
| Future glossary gap | pending | This document can be imported into future glossary. |

---

## 28. Non-expansion rule

This document MUST NOT be used to create new safety claims.

It only clarifies how existing and related labels must be read.

A system cannot claim improved CCDP conformance merely because it adopts namespaced terminology.

Correct terminology is necessary for conformance hygiene, but not sufficient for safety, legality, developmental validity, or product readiness.

---

## 29. Final control sentence

```text
Numbers are local.
Namespaces control meaning.
Field context resolves compatibility aliases.
Ambiguity fails closed.
DOI-bound baselines remain unchanged.
```
