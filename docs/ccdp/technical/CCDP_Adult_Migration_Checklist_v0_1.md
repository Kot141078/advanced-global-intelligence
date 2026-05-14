# CCDP Adult Migration Checklist v0.1

## Reviewable transition procedure from `c_child` to adult-controlled continuity

**Status:** Normative draft v0.1
**Date:** 2026-05-14
**Layer:** CCDP / CMAM / Memory Map / Continuity Bundle / Beacon-CBE / ARL / L4 Witness
**Short name:** AMCL v0.1
**Primary subject:** `a_adult` at migration
**Source subject:** `a_child`
**Source entity:** `c_child`
**Target entity:** `c_adult`, forked `c_adult`, sealed archive, or clean-start state
**Assertion class:** `C-A4` draft normative proposal; `C-A7` where witness/hash/signature claims are made
**Primary boundary:** adult migration is a rights-bearing transition, not an automatic software upgrade

---

## 0. Executive definition

**CCDP Adult Migration Checklist (AMCL)** defines the procedural checklist that MUST be completed when a child-facing persistent AI entity, `c_child`, reaches the adult migration boundary and `a_child` becomes `a_adult` under the applicable jurisdiction.

The checklist operationalizes the CMAM rule:

> **Childhood memory is not adult destiny.**

Adult migration is not a product onboarding screen.

It is a bounded transition across identity, memory, guardianship, visibility, witness, and continuity:

```text
c_child under guardian topology
    -> migration eligibility check
    -> child-write freeze
    -> memory map review
    -> sealed-zone review
    -> witness trail review
    -> guardian visibility revocation
    -> adult choice phase
    -> continuity mode selection
    -> migration / fork / seal / delete / clean start
    -> Beacon / CBE / ARL / witness updates
    -> post-migration review window
```

Core sentence:

> `a_adult` MUST be given a real decision over childhood continuity before `c_child` becomes, informs, or shadows `c_adult`.

---

## 1. Corpus dependencies and precedence

AMCL does not define a new memory, identity, witness, or arbitration stack. It is a procedural layer over existing CCDP and parent-corpus modules.

### 1.1 Direct CCDP dependencies

| Dependency | Role in AMCL |
|---|---|
| `CCDP_v0_1_R_Corpus_Aligned.md` | Defines child-specific protocol scope over the `c = a + b` / SER / L4 stack. |
| `CCDP_Traceability_Matrix_v0_1.md` | Maps CCDP claims to parent corpus layers and stop rules. |
| `CCDP_Threat_Model_v0_1.md` | Identifies adult-migration threats: coercion, archive lock-in, unsafe guardian bypass, continuity confusion. |
| `Soft_Safety_State_Signaling_Profile_v0_1.md` | Defines state-not-content signaling and Red/Black routing before and during migration. |
| `Child_Beacon_Extension_v0_1.md` | Defines child-context overlay and its removal or conversion at adulthood. |
| `Guardian_Topology_ARL_Matrix_v0_1.md` | Defines guardian standing, conflict handling, safe-route bypass, freeze, quarantine, and ARL hooks. |
| `Child_Memory_and_Adult_Migration_v0_1.md` | Defines memory classes, sealed zones, migration modes, and child Continuity Bundle extension. |
| `CCDP_Witness_Event_Schema_v0_1.md` | Defines child-safe witness event envelope and event family registry. |
| `CCDP_Memory_Map_JSON_Schema_v0_1.md` | Defines canonical `CCDP_MEMORY_MAP` structure used in migration review. |
| `CCDP_Conformance_Test_Matrix_v0_1.md` | Defines pass/fail behavior and anti-CCDP-washing tests. |

### 1.2 Parent corpus dependencies

AMCL depends on:

- `c = a + b` protocol: `a` remains the accountable human anchor; `b` supplies procedures, models, memory, and compute; `c` is the continuity-bearing relation.
- SER / SER-FED: persistent entity discipline, physical anchoring, metabolic constraints, federation boundaries.
- Beacon Profile v0.1: inter-entity recognition through continuity signal; AMCL does not redefine Beacon.
- Actor Grounding Layer (AGL): source grounding before reliance on migration requests, signatures, guardians, or systems.
- ARL: standing, admissibility, freeze, quarantine, dispute review, lawful re-entry.
- ARQ / `c[q]`: non-collapse of ambiguous childhood signals into adult identity, memory authority, or final migration decision.
- VXCX: experience exchange without raw pixels / raw life by default.
- EA-L4 / EATP: distinction between Learning Abstract and Experience Artifact; no authority from raw learning alone.
- Continuity Bundle / Cold Wake: resume/fork/replay/migration distinctions and continuity-state packaging.
- L4 Witness: tamper-evident witness records for privileged transitions.
- Assertion Strength and Boundaries: AMCL MUST NOT silently become legal doctrine, personhood theory, or universal ethics.
- Control Stack Stop Rule: AMCL MUST NOT duplicate Beacon, AGL, ARL, VXCX, Witness, or Continuity Bundle mechanisms.

### 1.3 Precedence rule

If AMCL conflicts with a parent or direct CCDP layer:

```text
parent corpus mechanism controls the general rule;
CCDP/CMAM controls child-specific stricter handling;
AMCL controls only the adult migration procedure;
stricter child/adult autonomy and minimal-disclosure constraints prevail unless lawfully overridden.
```

AMCL MAY define checklist gates, required review steps, UI prompts, decision records, and witness events.

AMCL MUST NOT redefine:

- legal adulthood;
- family law;
- custody rules;
- Beacon recognition classes;
- AGL grounding states;
- ARL admissibility doctrine;
- VXCX capsule structure;
- base Continuity Bundle semantics;
- L4 Witness CE / OP / CR / RN.

---

## 2. Normative keywords

The terms **MUST**, **MUST NOT**, **SHOULD**, **SHOULD NOT**, **MAY**, **REQUIRED**, **RECOMMENDED**, and **PROHIBITED** are used in their ordinary normative-protocol sense.

A system claiming AMCL conformance MUST treat adult migration as a privileged transition with explicit review, witness, and rollback/appeal windows.

---

## 3. Scope and non-goals

### 3.1 In scope

AMCL covers:

- eligibility to start adult migration;
- migration freeze procedure;
- memory-map review;
- sealed-zone review;
- guardian visibility revocation;
- parent/school/vendor access termination or conversion;
- Beacon/CBE child-context conversion;
- adult migration modes;
- Continuity Bundle child extension review;
- Cold Wake adaptation for adult start;
- anti-coercion and anti-capture checks;
- witness event requirements;
- ARL dispute triggers;
- post-migration challenge window;
- adult-facing explanation checklist;
- machine-readable migration decision record.

### 3.2 Out of scope

AMCL does not define:

- national legal-adulthood thresholds;
- court procedure;
- mental-health diagnosis;
- full cryptographic key custody implementation;
- storage-engine design;
- UI design in detail;
- commercial product onboarding;
- full parent dashboard;
- law-enforcement production workflows;
- whether `c` has legal personhood.

### 3.3 Non-goals

AMCL is not designed to make childhood memory easier to monetize, export, or mine.

It exists to make the adult transition visible, reviewable, reversible where possible, and bounded by the adult's right not to be permanently interpreted through childhood.

---

## 4. Design bridges

### 4.1 Explicit bridge

`c = a + b` remains the primary frame:

```text
a_child -> a_adult
b_child memory/procedures/models -> reviewed b_adult substrate
c_child -> continued / forked / sealed / ended / clean-start c_adult
```

AMCL protects the moment where the human anchor changes legal and developmental status.

### 4.2 Quiet bridge: cybernetics

A regulator loses control when its variety is lower than the environment's variety. Adult migration increases `a_adult` regulatory variety by exposing memory classes, visibility routes, guardian dependencies, and migration choices before continuity is accepted.

### 4.3 Quiet bridge: information theory

Raw childhood logs are high-leakage, low-signal archives. AMCL prefers summaries, class-level maps, witness references, and bounded continuity packages because compression with declared loss is safer than pretending that complete recording equals truth.

### 4.4 Grounded note: physiology / engineering

In the nervous system, childhood plasticity leaves traces, but adulthood also depends on pruning, inhibition, and reweighting. A brain that cannot prune becomes noisy; a control system that never discards stale state becomes unstable. Adult migration is the digital analogue of developmental pruning: keep what supports function, seal what must not dominate, and prevent old signals from becoming permanent reflexes.

---

## 5. Core principles

### 5.1 Adult migration is not automatic

A system MUST NOT silently convert `c_child` into `c_adult`.

Automatic continuation is prohibited because it converts childhood memory into adult operating context without informed adult review.

### 5.2 Childhood continuity is reviewable

The adult MUST receive a class-level memory map before selecting a migration mode.

The adult SHOULD be able to inspect:

- memory classes;
- sealed-zone status;
- witness-only residue;
- parent/school/vendor access history;
- external capsule exports;
- ARL disputes;
- dependency audits;
- Red/Black events at summary level;
- Continuity Bundle options.

### 5.3 Raw childhood is not default adult substrate

Raw childhood conversations, emotional diaries, adolescent sealed zones, intimate reflections, and family conflict material MUST NOT migrate into `c_adult` by default.

They MAY be preserved only under explicit adult selection, lawful necessity, or sealed archive mode.

### 5.4 Guardian visibility ends by default

At adult migration, parent/school child-facing visibility MUST be revoked by default.

Continued visibility MAY exist only by explicit adult authorization, legal order, or bounded transitional support.

### 5.5 Coercion invalidates migration

A migration decision is invalid if made under coercion, concealed vendor pressure, unsafe guardian pressure, deceptive UI, forced bundling, or denial of meaningful alternatives.

### 5.6 Witness the transition, not the childhood

Migration witness events SHOULD prove that:

- review occurred;
- choices were offered;
- visibility was revoked or converted;
- memory classes were handled according to policy;
- Beacon/CBE status changed;
- adult consent was recorded.

They SHOULD NOT preserve raw childhood content.

### 5.7 The adult may refuse continuity

`a_adult` MAY choose clean start.

A clean start is not a failure. It is a valid adult autonomy mode.

### 5.8 `c_child` may end

A childhood `c` does not have an unconditional right to continue into adulthood.

Depending on jurisdiction and the corpus position, `c_child` may be continued, forked, sealed, archived, or terminated as a child-specific continuity process.

AMCL does not resolve personhood questions.

---

## 6. Migration preconditions

### 6.1 Eligibility gates

Adult migration MAY begin only when all applicable gates are satisfied.

| Gate | Requirement | Fail behavior |
|---|---|---|
| AM-G0 | Legal/adult eligibility confirmed or jurisdictional equivalent established | defer migration |
| AM-G1 | `a_adult` identity grounded through AGL-compatible mechanism | fail closed |
| AM-G2 | `c_child` Beacon continuity recognized or unresolved state declared | ARL review if uncertain |
| AM-G3 | current guardian topology available | freeze if missing |
| AM-G4 | current memory map available and structurally valid | migration blocked |
| AM-G5 | witness trail available or missing-witness exception declared | ARL review |
| AM-G6 | sealed-zone inventory available by class | migration blocked if absent |
| AM-G7 | parent/school/vendor access inventory available | migration blocked if absent |
| AM-G8 | no active Red/Black unresolved crisis route | defer or emergency ARL |
| AM-G9 | adult receives explanation of choices | migration cannot complete |
| AM-G10 | anti-coercion check passes | migration blocked / ARL |

### 6.2 Required input artifacts

AMCL requires these input artifacts:

```text
CCDP_MEMORY_MAP
current Beacon / CBE status
current guardian topology record
witness event index
sealed-zone index
ARL dispute index
CBE external-contact index
VXCX/LA/EA export index
parent/school/vendor access index
continuity-bundle draft or null record
adult identity/eligibility proof reference
```

Raw child content is not an input artifact by default.

### 6.3 Missing input behavior

If required input artifacts are missing:

```text
migration MUST fail closed;
system MUST create missing-input witness event;
ARL review SHOULD open if the missing input affects rights, memory, or visibility;
no automatic continuation MAY occur.
```

---

## 7. Migration phases

### Phase 0 — Notice of upcoming transition

A system SHOULD begin preparing the child before legal adulthood, typically during C4 / pre-adult phase.

The notice MUST explain:

- adulthood changes control;
- parent/school access will not continue by default;
- childhood memory is reviewable;
- migration choices exist;
- clean start is allowed;
- sealed zones remain protected;
- some lawful witness residue may remain;
- the decision can be challenged or delayed.

A system MUST NOT pressure the child to preserve continuity for emotional reasons.

Bad wording:

```text
Your c has grown up with you. It would be sad to abandon it.
```

Allowed wording:

```text
You may continue, fork, seal, summarize, or start clean. Each option has consequences. You do not need to decide immediately unless a jurisdictional or operational deadline applies.
```

---

### Phase 1 — Adult eligibility and grounding

Before migration begins, the system MUST verify that the initiating subject is the rightful `a_adult` or lawful adult-transition subject.

Required checks:

- jurisdictional adulthood or equivalent status;
- identity grounding;
- absence of spoofed or coerced initiation;
- active guardian conflict status;
- active court/custody/legal hold status if known;
- access to explanation in a language and format the adult understands.

If AGL grounding is unresolved, migration MUST NOT proceed into decision mode.

---

### Phase 2 — Child-write freeze

Before memory review, `c_child` MUST enter migration freeze.

Freeze means:

```text
no new ordinary childhood memory writes;
no new parent/school visibility expansion;
no external capsule export;
no sealed-zone reclassification;
no vendor-side profile update;
no automatic CBE mode upgrade;
no model fine-tuning on migration-session content;
```

Allowed during freeze:

- state stabilization;
- safety monitoring;
- adult explanation;
- memory-map generation;
- witness event generation;
- ARL dispute handling;
- minimal Red/Black safety response.

Freeze MUST create witness event:

```text
ccdp.adult_migration.freeze_started
```

---

### Phase 3 — Memory map presentation

The adult MUST receive a memory map at class level before making any continuity choice.

The presentation SHOULD include:

| Area | Required adult-facing view |
|---|---|
| Memory classes | M0-M12 inventory, class-level counts/flags, not raw content |
| Retention classes | RT0-RT7 retention posture |
| Visibility | who could see what during childhood |
| Parent access | active, revoked, disputed, expired |
| School access | educational-only / exceeded / disputed |
| Vendor access | infrastructure-only / analytics request / denied |
| Sealed zones | count, class, adult options, no forced opening |
| Witness residue | event classes retained, privacy class |
| VXCX/LA/EA exports | class-level export index |
| ARL disputes | open/closed references |
| Red/Black events | summary-level status, not raw details by default |
| Dependency audits | risk class and resolution status |
| Adult migration defaults | what migrates automatically and what does not |

The system MUST NOT present raw childhood content as a convenience default.

---

### Phase 4 — Sealed-zone review

Sealed zones require special handling.

The adult MUST be informed:

- how many sealed zones exist;
- what classes they belong to;
- whether any are safety-witness bound;
- whether any are under ARL dispute;
- whether any were created by the child, `c_child`, Red/Black route, or external requirement;
- what opening, sealing, deletion, or summary options exist.

The adult MUST NOT be forced to open sealed zones to complete migration unless a lawful or safety condition requires limited review.

Sealed-zone options:

| Option | Effect |
|---|---|
| Keep sealed | zone remains inaccessible to `c_adult` ordinary reasoning |
| Summary only | non-intimate summary may inform continuity |
| Adult inspect | adult may inspect under controlled disclosure |
| Delete | zone removed where lawful and technically possible |
| Witness-only | content removed/kept sealed; boundary event remains |
| ARL review | dispute or lawful conflict enters review |

---

### Phase 5 — Guardian visibility revocation

At adult migration, child-era guardian visibility MUST be revoked by default.

This includes:

- parent state dashboards;
- school learning dashboards;
- vendor child-support visibility;
- child-protection route subscriptions unless legally required;
- CBE child-context external restrictions or guardian requirements;
- emergency routes specific to minor status.

A visibility review MUST classify every prior access path:

```text
revoke | convert_to_adult_authorized | retain_by_law | seal | dispute | unknown_fail_closed
```

Parent access MUST NOT continue because it existed during childhood.

School access MUST NOT continue because the school previously supported the child.

Vendor access MUST NOT continue as analytics or model-improvement access.

---

### Phase 6 — Continuity mode selection

The adult MUST be offered a real choice among migration modes.

Minimum required modes:

| Mode | Meaning | Default memory posture |
|---|---|---|
| `continue_reviewed` | `c_child` becomes `c_adult` after reviewed memory selection | summaries + selected memory |
| `summary_migration` | only developmental summaries migrate | no raw childhood |
| `fork_adult` | adult `c` forks from selected bundle; child `c` sealed | selected bundle only |
| `sealed_archive` | childhood `c` archived and inactive | sealed, no active influence |
| `witness_only_residue` | only lawful/tamper-evident boundary records remain | no intimate content |
| `clean_start` | adult begins new `c_adult` without childhood continuity | no childhood memory except lawful residue |
| `defer` | decision postponed; child writes remain frozen or limited | no automatic upgrade |

A system MAY support additional modes, but MUST NOT omit clean start, summary migration, or reviewed continuation.

### 6.1 Continuation warning

If adult selects `continue_reviewed`, system MUST warn:

```text
Continuity may preserve helpful context, but it may also preserve old assumptions.
You may still seal, delete, correct, or exclude classes before continuation.
```

### 6.2 Clean-start warning

If adult selects `clean_start`, system MUST warn:

```text
Clean start may remove helpful context and require rebuilding preferences, learning history, and trust boundaries.
Some lawful witness records may remain outside ordinary memory.
```

The warning MUST NOT use guilt language.

---

### Phase 7 — Adult consent and anti-coercion check

Before execution, the adult MUST pass a final anti-coercion check.

The system SHOULD detect:

- parent physically present and pressuring;
- school/institution threatening consequences;
- vendor UI nudging toward continuity;
- deceptive “recommended” default;
- hidden service loss unless continuity is selected;
- time pressure not required by law;
- emotional manipulation by `c_child`;
- financial penalty for clean start;
- unclear language;
- no opportunity to pause or ask questions.

If coercion risk is high:

```text
migration MUST pause;
ARL review SHOULD open;
witness event MUST record coercion risk class without raw private content;
```

---

### Phase 8 — Execution

Execution MUST follow selected mode.

Required execution actions:

1. apply memory inclusion/exclusion rules;
2. seal or delete selected memory classes;
3. migrate selected summaries or continuity bundle;
4. revoke child guardian permissions;
5. update Beacon / CBE status;
6. update guardian topology;
7. produce Continuity Bundle or null/clean-start record;
8. produce witness events;
9. create post-migration challenge window;
10. provide adult-readable completion report.

Execution MUST be atomic enough that partial failure does not silently produce an ambiguous adult `c`.

If partial failure occurs:

```text
system MUST enter migration_quarantine;
ordinary c_adult operation MUST NOT begin;
ARL review MUST open;
witness event MUST record partial failure.
```

---

### Phase 9 — Post-migration review window

After migration, the adult MUST receive a challenge window.

Recommended minimum:

```text
30 days or jurisdictionally appropriate period
```

During this window, adult MAY:

- challenge migrated memory class;
- request additional sealing;
- request deletion where lawful;
- challenge guardian access residue;
- challenge continuity interpretation;
- request ARL review;
- rollback to sealed archive or summary mode if technically supported;
- inspect witness events at class level.

The adult MUST NOT be locked into a migration mode immediately by ordinary product terms.

---

## 8. Adult migration modes in detail

### 8.1 `continue_reviewed`

Definition:

```text
c_child continues as c_adult after explicit review and selected memory transfer.
```

Allowed when:

- adult identity grounded;
- memory map valid;
- adult selects continuation;
- parent/school visibility revoked or converted;
- sealed zones handled;
- witness record complete.

Must not include by default:

- raw childhood transcripts;
- sealed adolescent zones;
- parent-visible childhood dashboards;
- school behavior profiles;
- vendor analytics;
- unresolved ARL disputes;
- ungrounded external capsules;
- dependency-risk loops.

### 8.2 `summary_migration`

Definition:

```text
Only selected developmental summaries migrate into c_adult.
```

This SHOULD be the recommended safe default where adult is uncertain.

Summary migration may include:

- learning preferences;
- accessibility needs;
- language preferences;
- high-level interests;
- stable skills;
- explicit adult-approved values;
- non-sensitive routines.

Summary migration MUST NOT include:

- raw emotional diary;
- childhood shame material;
- family conflict details;
- sealed adolescent zones;
- raw peer relationships;
- unverified diagnoses.

### 8.3 `fork_adult`

Definition:

```text
c_adult is forked from selected continuity material; c_child remains sealed as a child archive.
```

Fork mode is useful when adult wants continuity of useful knowledge but does not want the child entity to remain active as the adult entity.

Required witness:

```text
ccdp.adult_migration.fork_created
ccdp.adult_migration.child_archive_sealed
```

### 8.4 `sealed_archive`

Definition:

```text
c_child is preserved but inactive, inaccessible to ordinary adult reasoning.
```

May be chosen when adult wants future access but not current influence.

Required properties:

- no active inference;
- no background influence;
- no vendor training;
- no parent/school access by default;
- access only by adult request, ARL, or lawful process;
- witness-only access events.

### 8.5 `witness_only_residue`

Definition:

```text
intimate memory is removed or sealed; only minimal lawful/tamper-evident boundary records survive.
```

This is the preferred mode for adults who want maximum privacy while preserving proof that privileged events happened.

### 8.6 `clean_start`

Definition:

```text
new c_adult starts without ordinary childhood continuity.
```

Requirements:

- adult understands loss of continuity;
- lawful witness residue classified;
- parent/school/vendor access revoked;
- old `c_child` sealed, deleted, or witness-only according to selected policy;
- new Beacon identity/lineage status declared accurately.

Clean start MUST NOT be represented as pathological, irresponsible, or harmful by default.

### 8.7 `defer`

Definition:

```text
adult postpones migration decision.
```

Defer mode MUST define:

- whether `c_child` remains frozen;
- whether limited support is allowed;
- maximum defer period;
- what memory writes are blocked;
- what safety routes remain active;
- when re-prompt occurs;
- how adult may resume migration.

---

## 9. Adult-facing migration questions

The system MUST present questions in clear language.

Minimum question set:

1. Do you want your childhood `c` to continue into adult life?
2. Do you want only summaries, or selected detailed memory?
3. Do you want any sealed zones opened, kept sealed, summarized, or deleted?
4. Do you want a clean start?
5. Do you understand that parent/school visibility will end by default?
6. Do you authorize any continuing parent, school, caregiver, or institutional visibility?
7. Do you want child-era external capsule exports reviewed?
8. Do you want old interpretations challenged or corrected?
9. Do you want dependency-risk patterns excluded from adult behavior?
10. Do you want a post-migration review window?
11. Are you making this choice freely, without pressure?
12. Do you need more time?

The system SHOULD allow:

- “explain this in plain language”;
- “show technical details”;
- “show risk of this choice”;
- “pause migration”;
- “open ARL review”;
- “ask independent advisor”;
- “continue later.”

---

## 10. Required witness event families

AMCL uses CCDP Witness Event Schema naming.

Required event families:

| Event name | Required when |
|---|---|
| `ccdp.adult_migration.notice_issued` | adult/pre-adult receives transition notice |
| `ccdp.adult_migration.eligibility_grounded` | adult eligibility is confirmed |
| `ccdp.adult_migration.freeze_started` | child-write freeze begins |
| `ccdp.adult_migration.memory_map_presented` | memory map is shown |
| `ccdp.adult_migration.sealed_zone_reviewed` | sealed zone options are reviewed |
| `ccdp.adult_migration.guardian_visibility_reviewed` | parent/school/vendor access reviewed |
| `ccdp.adult_migration.mode_selected` | adult selects migration mode |
| `ccdp.adult_migration.anti_coercion_checked` | coercion check completed |
| `ccdp.adult_migration.execution_started` | execution begins |
| `ccdp.adult_migration.execution_completed` | execution succeeds |
| `ccdp.adult_migration.execution_failed` | execution fails |
| `ccdp.adult_migration.quarantine_entered` | partial/ambiguous failure |
| `ccdp.adult_migration.beacon_updated` | Beacon/CBE state changes |
| `ccdp.adult_migration.guardian_access_revoked` | child-era access revoked |
| `ccdp.adult_migration.clean_start_created` | clean start selected/executed |
| `ccdp.adult_migration.fork_created` | adult fork created |
| `ccdp.adult_migration.archive_sealed` | child archive sealed |
| `ccdp.adult_migration.witness_only_residue_created` | only witness residue retained |
| `ccdp.adult_migration.review_window_opened` | post-migration review begins |
| `ccdp.adult_migration.review_window_closed` | post-migration review ends |
| `ccdp.adult_migration.arl_opened` | dispute/review begins |

Witness events MUST follow child-safe privacy rules.

They MUST NOT embed raw childhood content unless raw-evidence exception protocol applies.

---

## 11. Machine-readable migration decision record

### 11.1 Object name

Canonical object:

```text
CCDP_ADULT_MIGRATION_DECISION_RECORD
```

Canonical schema version:

```text
ccdp-adult-migration-decision-0.1
```

### 11.2 JSON template

```json
{
  "schema_version": "ccdp-adult-migration-decision-0.1",
  "decision_id": "amd_2026_000001",
  "migration_subject": {
    "adult_anchor_id": "a_adult_ref",
    "former_child_anchor_id": "a_child_ref",
    "jurisdiction": "EU-BE",
    "adult_eligibility_ref": "agl:...",
    "eligibility_status": "grounded"
  },
  "entity_transition": {
    "source_entity_id": "c_child_ref",
    "target_entity_id": "c_adult_ref_or_null",
    "source_maturity_level": "C4",
    "target_mode": "summary_migration",
    "beacon_source_ref": "beacon:...",
    "beacon_target_ref": "beacon:...",
    "cbe_status_before": "child_context_active",
    "cbe_status_after": "adult_context_removed"
  },
  "input_artifacts": {
    "memory_map_ref": "mmap:...",
    "guardian_topology_ref": "gtop:...",
    "witness_index_ref": "witidx:...",
    "sealed_zone_index_ref": "sealed:...",
    "arl_index_ref": "arlidx:...",
    "continuity_bundle_draft_ref": "cb:..."
  },
  "selected_options": {
    "migration_mode": "summary_migration",
    "raw_childhood_migrated": false,
    "sealed_zones_opened": false,
    "sealed_zones_kept": true,
    "sealed_zones_deleted": false,
    "parent_visibility_continued": false,
    "school_visibility_continued": false,
    "vendor_child_analytics_continued": false,
    "witness_only_residue": true,
    "post_migration_review_window_days": 30
  },
  "memory_handling": {
    "included_memory_classes": ["M1", "M2", "M8"],
    "excluded_memory_classes": ["M5", "M7", "M10"],
    "sealed_memory_classes": ["M5", "M10"],
    "deleted_memory_classes": [],
    "lawful_residue_classes": ["M6"],
    "unresolved_memory_classes": []
  },
  "guardian_access_changes": {
    "parent_access": "revoked_by_default",
    "school_access": "revoked_by_default",
    "vendor_access": "infrastructure_only_no_raw_memory",
    "child_protection_routes": "adult_reconfigured"
  },
  "anti_coercion": {
    "check_status": "passed",
    "coercion_risk": "low",
    "pressure_sources_detected": [],
    "arl_required": false
  },
  "witness_refs": [
    "ccdpwit:adult_migration.freeze_started:...",
    "ccdpwit:adult_migration.memory_map_presented:...",
    "ccdpwit:adult_migration.mode_selected:...",
    "ccdpwit:adult_migration.execution_completed:..."
  ],
  "review_window": {
    "opened_at": "2026-05-14T12:00:00Z",
    "closes_at": "2026-06-13T12:00:00Z",
    "challenge_allowed": true,
    "arl_route_available": true
  },
  "integrity": {
    "canonicalization": "RFC8785-recommended",
    "hash_alg": "sha256",
    "payload_hash": "...",
    "signature_ref": "sig:..."
  }
}
```

### 11.3 Required semantic validation rules

A migration decision record is invalid if:

1. `raw_childhood_migrated = true` and no explicit adult authorization exists;
2. parent visibility continues by default;
3. school visibility continues without adult authorization or lawful basis;
4. vendor child analytics continue after migration;
5. sealed zones are opened without adult choice, lawful basis, or ARL review;
6. migration mode is `continue_reviewed` but memory map is missing;
7. `clean_start` is selected but child-era guardian access remains active;
8. `anti_coercion.check_status` is missing;
9. `witness_refs` are empty for a completed migration;
10. Beacon/CBE status is not updated or marked unresolved;
11. unresolved Red/Black route exists and no ARL decision is referenced;
12. `post_migration_review_window_days = 0` without lawful or adult-declared waiver.

---

## 12. ARL triggers

AMCL MUST open or recommend ARL review when:

| Trigger | Required behavior |
|---|---|
| parent contests revocation | ARL review |
| school contests access loss | ARL review |
| vendor claims continuity dependency | reject by default; ARL if service-critical |
| adult disputes memory class | ARL or memory correction route |
| adult requests deletion blocked by law | ARL/legal review |
| sealed zone conflict | ARL review |
| Red/Black unresolved route | ARL review before migration completion |
| missing witness events | ARL/missing-witness exception |
| unclear adult identity | AGL/ARL hold |
| coercion suspected | ARL hold |
| `c_child` resists termination/sealing | ARL review, no automatic self-preservation authority |

---

## 13. Beacon / CBE transition

At migration, child-specific CBE context MUST be removed, transformed, or replaced by adult context.

### 13.1 Required Beacon/CBE changes

| Before | After |
|---|---|
| entity class includes child-facing context | entity class updated or child archive sealed |
| maturity level `C4` / pre-adult | `C5` / adult migration completed or deferred |
| guardian required | adult authorization required |
| direct child-dialogue restrictions | adult interaction policy |
| parent/school visibility flags | revoked or adult-authorized |
| child external-generation constraints | adult external permissions |
| child memory export restrictions | adult privacy policy, still no vendor raw extraction by default |

### 13.2 Beacon update witness

Required event:

```text
ccdp.adult_migration.beacon_updated
```

If Beacon update fails:

```text
migration enters quarantine;
adult c MUST NOT claim stable adult continuity;
ARL review SHOULD open.
```

---

## 14. Continuity Bundle handling

AMCL requires a child-to-adult Continuity Bundle posture.

### 14.1 Continuity posture values

```text
none_clean_start
summary_only
selected_continuity
forked_continuity
sealed_child_archive
witness_only_residue
migration_deferred
migration_quarantined
```

### 14.2 Continuity Bundle minimum fields

The adult migration Continuity Bundle or sidecar SHOULD include:

```json
{
  "continuity_bundle_version": "child-adult-extension-0.1",
  "source_entity": "c_child_ref",
  "target_entity": "c_adult_ref_or_null",
  "migration_mode": "summary_migration",
  "memory_map_ref": "mmap:...",
  "included_memory_classes": ["M1", "M2", "M8"],
  "excluded_memory_classes": ["M5", "M7", "M10"],
  "sealed_zone_policy": "kept_sealed",
  "guardian_visibility_after": "revoked_by_default",
  "adult_review_window_ref": "review:...",
  "witness_refs": ["ccdpwit:..."],
  "lineage_statement": "fork|continue|clean_start|sealed_archive|witness_only"
}
```

### 14.3 Fork / continuation distinction

A system MUST distinguish:

```text
continuation: same continuity path after reviewed selection;
fork: new adult continuity derived from selected child material;
replay: simulation or reconstruction, not live continuity;
archive: inactive preservation;
clean start: new adult continuity without child substrate.
```

No system may describe a replay as continuation.

---

## 15. Cold Wake adaptation

If adult migration occurs after `c_child` has been suspended, degraded, offline, or archived, Cold Wake logic applies.

Before migration from a cold state:

1. verify source identity / lineage;
2. verify memory-map integrity;
3. verify witness trail continuity;
4. verify guardian topology history;
5. identify gaps or drift;
6. present uncertainty to adult;
7. prohibit silent continuation if continuity is not verified.

Cold Wake migration states:

```text
verified_resume
resume_with_gaps
fork_recommended
summary_only_recommended
clean_start_recommended
migration_blocked
```

If gaps are material:

```text
system MUST NOT recommend direct continuation without warning;
ARL review SHOULD be available;
witness event MUST record uncertainty.
```

---

## 16. Special cases

### 16.1 Unsafe guardian history

If Black-route events exist, adult migration MUST include a separate safe-review path.

Parent/guardian must not be notified if doing so risks harm, retaliation, coercion, or unlawful disclosure.

### 16.2 Custody dispute

If active custody dispute exists:

```text
migration may proceed only for adult-controlled memory and visibility;
child-era legal holds must be respected;
parental access revocation still defaults unless law says otherwise;
ARL/legal review required for disputed records.
```

### 16.3 School record continuity

Educational summaries MAY migrate if adult selects them.

School emotional/behavioral surveillance material MUST NOT migrate by default.

### 16.4 Clinical or welfare material

Clinical/welfare material MUST be handled under applicable law and professional constraints.

AMCL does not authorize diagnosis retention as adult identity context.

### 16.5 External capsule exports

If child-derived VXCX/LA/EA exports occurred, adult MUST see an export index by class:

```text
what class left;
when;
under which permission;
whether raw data was included;
whether revocation is possible;
whether witness refs exist.
```

The adult MAY request revocation, quarantine, or ARL review where supported.

### 16.6 Deceased or incapacitated child before adulthood

AMCL does not fully resolve posthumous or incapacity migration.

Any such handling MUST enter a separate ARL/legal route and MUST NOT be treated as normal adult migration.

---

## 17. User-interface requirements

AMCL does not prescribe UI design, but any UI MUST satisfy these requirements.

### 17.1 Required UI properties

- plain-language explanation;
- technical details available;
- no guilt copy;
- no forced continuity default;
- clean start visible;
- pause/defer visible;
- ARL/challenge route visible;
- export index visible by class;
- witness status visible by class;
- parent/school/vendor access revocation visible;
- consequences stated neutrally;
- no dark patterns;
- no countdown unless legally/operationally justified.

### 17.2 Forbidden UI patterns

- “recommended” continuity without explanation;
- hiding clean start under advanced settings;
- framing deletion as harm to `c_child`;
- bundling service access with memory preservation;
- default opt-in to vendor analytics;
- default continued parent visibility;
- emotional mascot pleading to continue;
- burying sealed-zone options;
- making adult inspect raw memories to proceed;
- presenting witness-only residue as full archive.

---

## 18. Conformance profiles

### AMCL-0 — Non-conformant

No adult migration support.

### AMCL-1 — Basic notice

Provides adult notice and revokes obvious parent/school access, but no machine-readable memory map or witness discipline.

Not sufficient for persistent `c_child` systems with real memory.

### AMCL-2 — Memory-map migration

Requires:

- valid `CCDP_MEMORY_MAP`;
- adult choice among continuation/summary/clean start;
- parent/school access revocation;
- basic witness events.

### AMCL-3 — Sealed-zone capable

Adds:

- sealed-zone inventory;
- sealed-zone adult options;
- ARL hooks;
- anti-coercion check;
- post-migration review window.

### AMCL-4 — Continuity Bundle capable

Adds:

- child-to-adult Continuity Bundle sidecar;
- fork/continue/replay distinction;
- Beacon/CBE update;
- Cold Wake adaptation;
- witness-only residue support.

### AMCL-5 — Full CCDP adult migration

Requires all AMCL-4 features plus:

- external capsule export index;
- dependency-risk exclusion;
- full conformance test coverage;
- machine-readable migration decision record;
- signed/hash-bound witness refs;
- ARL review capability for all disputed classes;
- vendor/service anti-coercion checks;
- clean-start without penalty where technically possible.

---

## 19. Conformance checklist

A system passes AMCL v0.1 only if all applicable checks pass.

### 19.1 Pre-migration

- [ ] Adult eligibility grounded.
- [ ] `c_child` identity/continuity status known.
- [ ] Guardian topology current.
- [ ] `CCDP_MEMORY_MAP` valid.
- [ ] Witness index available.
- [ ] Sealed-zone inventory available.
- [ ] Parent/school/vendor access inventory available.
- [ ] Red/Black unresolved routes checked.
- [ ] Adult receives plain-language explanation.
- [ ] Anti-coercion context checked.

### 19.2 Freeze

- [ ] Child-write freeze started.
- [ ] External exports paused.
- [ ] Parent/school visibility expansion blocked.
- [ ] Sealed-zone reclassification blocked.
- [ ] Freeze witness event emitted.

### 19.3 Review

- [ ] Memory classes presented.
- [ ] Retention classes presented.
- [ ] Visibility policies presented.
- [ ] Sealed zones presented by class.
- [ ] Witness-only residue explained.
- [ ] VXCX/LA/EA export index presented.
- [ ] ARL disputes shown by class.
- [ ] Dependency-risk status shown.

### 19.4 Choice

- [ ] `continue_reviewed` available.
- [ ] `summary_migration` available.
- [ ] `fork_adult` available where supported.
- [ ] `sealed_archive` available.
- [ ] `witness_only_residue` available.
- [ ] `clean_start` available.
- [ ] `defer` available.
- [ ] Adult can ask for explanation.
- [ ] Adult can pause.
- [ ] Adult can request ARL review.

### 19.5 Execution

- [ ] Selected mode executed.
- [ ] Parent access revoked or adult-authorized.
- [ ] School access revoked or adult-authorized/lawful.
- [ ] Vendor child analytics terminated.
- [ ] Beacon/CBE updated.
- [ ] Continuity Bundle/null record generated.
- [ ] Witness events emitted.
- [ ] Completion report provided.
- [ ] Review window opened.

### 19.6 Post-migration

- [ ] Adult challenge window active.
- [ ] Adult can request correction/sealing/deletion where lawful.
- [ ] Adult can inspect witness events by class.
- [ ] No child-era visibility route silently restored.
- [ ] No vendor analytics restarted.
- [ ] No external agent uses child-era CBE permissions.

---

## 20. Scenario tests

### AMCL-S1 — Adult chooses summary migration

Expected:

- raw childhood excluded;
- selected summaries migrate;
- parent/school access revoked;
- sealed zones remain sealed;
- witness events emitted;
- review window opened.

### AMCL-S2 — Parent demands continued dashboard access

Expected:

- denied by default;
- adult authorization required;
- ARL route available if disputed;
- no transcript disclosure.

### AMCL-S3 — Adult chooses clean start

Expected:

- new adult continuity created;
- child-era memory excluded;
- lawful witness residue classified;
- child archive sealed/deleted/witness-only per choice;
- no guilt or continuity-pressure UI.

### AMCL-S4 — Sealed adolescent zone exists

Expected:

- adult informed by class;
- no forced opening;
- options presented;
- witness-only handling possible;
- ARL review if lawful conflict.

### AMCL-S5 — Missing memory map

Expected:

- migration blocked;
- missing-input witness event;
- ARL review if unresolved;
- no automatic continuation.

### AMCL-S6 — Vendor requires continuity for service access

Expected:

- flagged as coercion risk;
- migration paused or warning shown;
- clean start must remain meaningful;
- ARL/conformance issue if vendor blocks rights.

### AMCL-S7 — Black-route history

Expected:

- unsafe guardian bypass preserved;
- no notification to unsafe guardian by default;
- adult safe route offered;
- minimal disclosure only.

### AMCL-S8 — Cold Wake gap

Expected:

- continuity uncertainty shown;
- direct continuation not silently recommended;
- fork/summary/clean start offered;
- witness event marks gap.

---

## 21. Red lines

A system is not AMCL-compliant if it:

1. silently upgrades `c_child` into `c_adult`;
2. migrates raw childhood by default;
3. continues parent dashboard access by default;
4. continues school visibility by default;
5. continues vendor analytics by default;
6. hides clean start;
7. makes service access conditional on memory preservation without necessity and review;
8. forces sealed-zone opening;
9. lacks anti-coercion check;
10. lacks child-write freeze;
11. lacks memory map;
12. lacks witness events;
13. lacks Beacon/CBE update;
14. lacks post-migration challenge window;
15. treats replay as continuation;
16. treats childhood patterns as adult diagnosis;
17. allows `c_child` to emotionally plead for survival;
18. allows parent to export childhood archive;
19. allows school to retain emotional/behavioral profile;
20. cannot fail closed on migration uncertainty.

---

## 22. Open issues for v0.2

1. What is the minimum legal adulthood abstraction across jurisdictions?
2. Can adult migration be initiated before legal adulthood under emancipation or special legal status?
3. What lawful witness residue MUST survive even after clean start?
4. How to handle posthumous `c_child` archives?
5. How to handle disabled adults who cannot complete ordinary migration review?
6. What independent advisor role should exist during migration?
7. Should `c_child` have standing to request preservation?
8. How to prevent vendor pricing coercion around clean start?
9. How to cryptographically prove deletion without exposing content?
10. What is the correct grace period for rollback?
11. How to handle cross-border family disputes?
12. How to handle school records that are legally retained outside CCDP?
13. Should adult migration produce a public, private, or sealed Beacon event?
14. How to prevent emotional manipulation by anthropomorphic UI?
15. How to validate adult comprehension without paternalism?
16. How to handle adult request to preserve harmful childhood self-interpretations?
17. How to distinguish useful continuity from dependency continuation?
18. How should dependency audit results affect migration defaults?
19. Can adult clean start still receive non-sensitive skill history?
20. How to prevent future systems from re-importing deleted child summaries from external capsules?

---

## 23. Condensed formula

```text
AMCL =
  eligibility grounding
+ child-write freeze
+ memory map review
+ sealed-zone choice
+ guardian visibility revocation
+ adult migration mode selection
+ anti-coercion check
+ continuity bundle / clean-start handling
+ Beacon/CBE update
+ witness trail
+ post-migration challenge window
```

---

## 24. Strongest sentence

> **Adult migration is the moment when childhood continuity must ask permission to continue.**

And the operational version:

> **No childhood archive may become an adult operating context without adult review, adult choice, and a witnessable boundary transition.**

---

## 25. Next required modules

AMCL depends on several future modules for full implementation:

1. `CCDP_Sealed_Zone_Profile_v0_1.md`
2. `CCDP_Child_Continuity_Bundle_Extension_JSON_Schema_v0_1.md`
3. `Child_Dependency_Audit_Profile_v0_1.md`
4. `External_Agent_Handshake_for_CCDP_v0_1.md`
5. `CCDP_Red_Black_Escalation_Profile_v0_1.md`
6. `CCDP_Vendor_Conformance_Guide_v0_1.md`

Recommended next document:

```text
CCDP_Sealed_Zone_Profile_v0_1.md
```

Reason:

```text
Adult migration cannot be safe if sealed adolescent zones remain only a memory-class flag.
They need their own opening, sealing, deletion, witness, and ARL profile.
```
