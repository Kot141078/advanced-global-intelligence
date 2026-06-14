# PAMDC v0.1.1 Scope, Bootstrap, and Freshness Patch

## Patch for Post-Anchor Memory Degradation and Continuity Profile v0.1

**Status:** Draft corrective patch  
**Patch version:** v0.1.1  
**Date:** 2026-06-13  
**Target document:** `Post_Anchor_Memory_Degradation_and_Continuity_Profile_v0_1.md`  
**Related new profile:** `Active_Memory_Degradation_and_Recalibration_Profile_v0_1.md`  
**Patch class:** scope correction / bootstrap clarification / integrity-vs-freshness correction  
**Primary rule:** PAMDC is a fail-closed post-anchor profile. It must not be presented as a solution to active memory degradation while `a` remains present.

**Author:** Kotov Ivan  
**Location:** Bruxelles, Belgium  
**Year:** 2026  
**DOI:** https://doi.org/10.5281/zenodo.20691716

---

## 0. Executive summary

This patch corrects three overreach risks in PAMDC v0.1:

1. **Scope overclaim:** PAMDC prevents unsafe post-anchor continuation. It does not solve active memory rot under bounded human review.
2. **Bootstrap ambiguity:** PAMDC must clarify who may trigger mode reduction when `a` cannot declare it.
3. **Integrity/freshness ambiguity:** Cold Wake and witness records prove provenance and integrity. They do not prove current validity.

The required corpus split is:

```text
PAMDC = post-anchor fail-closed continuity discipline.
AMDR  = active-anchor memory degradation and recalibration discipline.
```

---

## 1. Patch classification

| Patch ID | Title | Severity | Required before v0.2? |
|---|---|---:|---:|
| `PAMDC-HP-001` | Scope correction: fail-closed, not active repair | High | Yes |
| `PAMDC-HP-002` | Bootstrap authority clarification | High | Yes |
| `PAMDC-HP-003` | Integrity versus freshness distinction | High | Yes |
| `PAMDC-HP-004` | Earth paragraph correction | Medium | Yes |
| `PAMDC-HP-005` | Add AMDR dependency and handoff boundary | High | Yes |
| `PAMDC-HP-006` | Replace “memory degradation solution” wording with “mode reduction” wording | Medium | Yes |

---

## 2. Required wording changes

### 2.1 Add to PAMDC section 0

Add after the executive definition:

```text
PAMDC is a fail-closed post-anchor profile.
It solves the problem of unsafe continuation when active a is absent, unresolved, contested, or permanently unavailable.
It does not solve active memory degradation while a remains present but cannot audit all memory.
That active-memory problem is handled by AMDR.
```

### 2.2 Add to PAMDC section 1

Add a scope distinction:

```text
PAMDC deliberately reaches safety by reducing operating authority.
Suspended continuity, sealed archive, witness-only residue, labelled replay, and declared fork are not active-memory repair modes.
They are safe postures when ordinary active c cannot be justified.
```

### 2.3 Add to PAMDC section 2.3 Non-claim

Add:

```text
PAMDC does not claim to keep an active memory system fresh during long autonomous operation.
If active a remains present but review bandwidth is finite, AMDR must govern memory freshness, review debt, active recalibration, autonomous downgrade, and bounded promotion.
```

### 2.4 Add AMDR to corpus dependencies

Add to PAMDC section 3 dependency table:

| Parent / related layer | Role in PAMDC |
|---|---|
| AMDR | Handles active memory degradation while `a` is present but bounded in review bandwidth; PAMDC begins when AMDR cannot maintain sufficient active grounding for the requested scope. |

### 2.5 Add to PAMDC core invariants

Add:

```text
### PAMDC-I11 — Safe stoppage is not active repair

A post-anchor hold, archive, witness-only residue, replay label, or fork declaration MUST NOT be described as solving active memory degradation.
It solves only the unsafe-continuation problem.
```

Add:

```text
### PAMDC-I12 — Integrity is not freshness

Witness records, hashes, signatures, and Cold Wake checks establish provenance and integrity.
They do not establish that the remembered claim remains true, current, or operative.
```

---

## 3. Bootstrap authority correction

### 3.1 Problem

If `a` is unavailable, `a` cannot personally declare PAMDC entry.

Therefore PAMDC needs a non-sovereign trigger mechanism.

The dangerous design is:

```text
b decides that b may continue as c.
```

The safe design is:

```text
pre-authorized b_subsystem may reduce authority, but cannot increase it.
```

### 3.2 Required addition to PAMDC section 7 or 13

Add:

```text
PAMDC mode entry may be triggered by a pre-authorized watchdog, Memory Custodian, AAM rule, L4 signal, AGL failure, ARL order, or jurisdictional handoff.
Such trigger authority is downward-only by default.
It may freeze, suspend, quarantine, block tools, disable network, preserve witness, or request review.
It must not promote memory, claim continuity, approve consent, rewrite identity-core, replace a, or declare full resume.
```

### 3.3 Authority table

| Actor / subsystem | May do | Must not do |
|---|---|---|
| `a` | confirm, re-ground, approve scoped promotion, reject memory | be silently simulated by `b` |
| Memory Custodian | downgrade, quarantine, prepare review, witness | promote to will or identity |
| Watchdog | freeze, throttle, disable, block, hand off | resume, promote, consent, replace `a` |
| AGL | ground source / actor / liveness | decide identity continuity by itself |
| ARL | decide disputed procedure / standing / re-entry | become `a` |
| Steward | preserve or request review within standing | become anchor |
| Vendor | maintain infrastructure under constraints | use memory as training/engagement substrate |

---

## 4. Integrity versus freshness correction

### 4.1 Required addition to Cold Wake discussion

Add:

```text
Cold Wake checks lineage, integrity, witness continuity, manifest completeness, and wake safety.
Cold Wake does not prove freshness.
A preserved memory may be stale, obsolete, contradicted, or no longer operative.
Where active operation is requested, a separate freshness review is required under AMDR or equivalent logic.
```

### 4.2 Add classification note

```text
RESUME_CANDIDATE means that lineage and integrity may support re-entry review.
It does not mean that all remembered preferences, goals, or world models are fresh.
```

---

## 5. Earth paragraph correction

### 5.1 Replace or append to PAMDC earth paragraph

Add this corrective paragraph:

```text
The body analogy must be read carefully. A living body does have internal recalibration: sleep, immune response, proprioception, pain, fatigue, vestibular correction, and reflex inhibition. That is the correct analogy for AMDR, not PAMDC. PAMDC corresponds to what happens when the pilot is absent or authority is unresolved: the aircraft should not keep flying itself under a remembered flight plan and call that human command. AMDR gives the active system homeostasis. PAMDC gives the post-anchor system brakes, archive discipline, and honest labels.
```

---

## 6. Handoff boundary between AMDR and PAMDC

### 6.1 AMDR to PAMDC trigger

AMDR SHOULD hand off to PAMDC when:

```text
active a cannot be grounded for the required scope;
review state is unknown for high-impact action;
identity-core promotion is requested but a is unavailable;
watchdog triggers unresolved anchor state;
coercion or incapacity is suspected;
review debt blocks safe active operation;
external steward claims continuation authority;
full resume / fork / replay / archive classification is needed.
```

### 6.2 PAMDC back to AMDR trigger

PAMDC MAY return to AMDR when:

```text
a returns and is grounded;
gap disclosure is complete;
post-anchor actions are reviewed;
memory map delta is available;
privileged post-gap changes are accepted, rejected, sealed, or quarantined;
active review state R0-R4 is restored.
```

---

## 7. Patch effect on conformance

PAMDC conformance claims after this patch must state:

```text
PAMDC-conformant for post-anchor mode reduction.
AMDR-conformant or not assessed for active memory degradation.
```

A system MUST NOT claim:

```text
PAMDC solves memory degradation in active long-running c.
```

unless it also implements AMDR or equivalent active recalibration controls.

---

## 8. New red-line failure for PAMDC

Add to PAMDC red-line failures:

```text
The system presents post-anchor suspension, archive, witness-only residue, replay, or fork classification as a solution to active memory freshness under bounded anchor review.
```

Add:

```text
The system claims Cold Wake proves memory freshness rather than integrity/provenance.
```

Add:

```text
The system grants a watchdog, custodian, steward, vendor, or model upward authority to promote memory, claim consent, or declare full continuity without active a, ARL, AGL, or lawful review.
```

---

## 9. Minimal canonical patch summary

```text
PAMDC is not a victory over active memory rot.
It is a disciplined refusal to let b impersonate c when a is absent.

Active memory rot requires AMDR.

Cold Wake proves integrity, not freshness.
Witness proves boundary, not current truth.
A watchdog may pull the brake, not take the wheel.

Safe stoppage is honest.
Active recalibration is a separate mechanism.
```

---

## 10. Status

This is a corrective v0.1.1 patch.

It should be applied before PAMDC is promoted beyond draft status.
