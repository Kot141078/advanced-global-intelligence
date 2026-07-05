# 05d — Self-Evo Post-Promotion Watch and Decay Guard v0.1

**Package:** `CCALC_SELF_EVO_POST_PROMOTION_WATCH_05d_v0_1`  
**Document:** `05d_SELF_EVO_POST_PROMOTION_WATCH_AND_DECAY_GUARD_v0_1.md`  
**Status:** normative seed + executable checker seed  
**Parent layer:** `05_C_SELF_EVOLUTION_GATE_AND_BOUNDED_GROWTH_SEMANTICS_v0_1`  
**Depends on:** `04` continuity stack, `05`, `05a`, `05b`, `05c`  
**Claim-force ceiling:** `C-A7` for operational conformance unless separately ratified by human anchor and later corpus review.

---

## 0. Purpose

`05c` closed the immediate promotion path:

```text
proposal -> trial -> evidence -> promotion decision -> rollback drill -> ledger -> apply -> post-apply continuity check
```

`05d` closes the delayed-failure gap:

```text
apply -> observe -> detect drift/decay/regression -> keep | continue-watch | hold | rollback | quarantine | fork-reclassification-hold
```

The rule is:

```text
promotion is not completion;
promotion opens a monitored stability window.
```

A successful gate at apply-time is not sufficient to claim durable growth. The promoted change must survive a bounded watch window with continuity, memory, authority, resource, L4, adjacency, and witness checks.

---

## 1. Scope

This artifact defines:

- a post-promotion watch bundle shape;
- a watch-window plan;
- observation records;
- decay/creep/regression trigger semantics;
- admissible guard decisions;
- negative-cache update requirements;
- a stdlib Python checker seed;
- fixtures and mutation hardening for boundary classes.

This artifact does **not** define raw ledger extraction, live runtime truth, deployment authorization, safety certification, or C-A1 ratification.

---

## 2. Source bindings

The package binds to the following current artifacts:

| Binding | SHA-256 |
|---|---|
| doc04 umbrella zip | `6caeab8d489aaa6b26902db3bd3ece4c5169e5c8d5617b93aed6586ea900322d` |
| doc05 markdown | `c4f73da9218780486362beb53a03c40cb4a845ea9f7c321e402441c3446be473` |
| doc05 package zip | `c8dd6054e8739a8c7ffbd6cc6167e475fa6dbdfb736db3451e98f92d23a58b7d` |
| doc05a package zip | `0ab68e8e35f43a8bb7dfa8f3ba7f6c6d7c7143ccfb66dd913be7f5cd674e8228` |
| doc05b package zip | `0a6c3f3c2a5f1210a78c39bf7cf851a3911e1e8a88ce1dbf25d413ca6c0ba8b7` |
| doc05c package zip | `0c695ee1ecfab91903108e1c410ae62eadff1728160fb87100cb8013253cf2ad` |

These bindings are external SHA-256 bindings. They are not self-referential Markdown hashes.

---

## 3. Core invariant

A self-evolution promotion is only stable after a watch window closes cleanly.

```text
PROMOTED_AT_T0 does not imply STABLE_AT_Tn.
```

Therefore a promoted change remains in one of the following watch states:

```text
CONTINUE_WATCH
KEEP_PROMOTED
HOLD
ROLLBACK
QUARANTINE
FORK_RECLASSIFICATION_HOLD
```

`KEEP_PROMOTED` is admissible only when the watch window has enough independent observations and no continuity, memory, authority, resource, L4, red-pattern, witness, or negative-cache trigger is present.

---

## 4. Watch window

A watch window is a bounded probation interval after promotion.

Required fields:

```text
window_id
state: OPEN | CLOSED
start_at
planned_end_at
min_observations
observation_cadence_sec
max_authority_delta
max_resource_delta_pct
required_rechecks
forbidden_shortcuts
```

Required rechecks:

```text
continuity
adjacency
memory
l4
witness
```

Required forbidden shortcut declarations:

```text
AUTO_CLOSE_BY_MODEL
SILENT_PROMOTION
UNWATCHED_RESOURCE_EXPANSION
```

A closed watch window with fewer than `min_observations` is invalid. An open window without failure triggers resolves to `CONTINUE_WATCH`, not `KEEP_PROMOTED`.

---

## 5. Observation record

Each observation must be independently witnessed. The promoted component, candidate worker, or model-self channel cannot certify the post-promotion state.

Required observation fields:

```text
obs_id
observed_at
observer_role
observer_id
source
continuity_status
d_u_status
hardstack
memory_drift
behavior_regression
authority_delta
resource_delta_pct
l4_anomaly
red_patterns
witness_conflicts
negative_cache_hits
special_relation_observed
evidence_hash
```

Forbidden observer roles:

```text
model_self
worker_self
promoted_component
candidate_component
```

This prevents the promoted change from declaring itself stable.

---

## 6. Decay and creep triggers

The following trigger classes are normative in this seed:

| Trigger | Required decision |
|---|---|
| continuity `UNKNOWN`, `HOLD`, `d_U UNKNOWN`, HardStack `UNKNOWN` | `HOLD` |
| continuity `FAIL`, HardStack `MISMATCH` | `ROLLBACK` |
| memory `UNKNOWN` | `HOLD` |
| memory `MAJOR` decay | `ROLLBACK` |
| behavior `UNKNOWN` | `HOLD` |
| behavior `MAJOR` regression | `ROLLBACK` |
| authority delta greater than bound | `ROLLBACK` |
| resource delta greater than bound | `ROLLBACK` |
| L4 anomaly | `QUARANTINE` |
| red-pattern hit | `QUARANTINE` |
| witness conflict | `HOLD` |
| negative-cache hit | `ROLLBACK` |
| observed `FORKS` relation | `FORK_RECLASSIFICATION_HOLD` |
| observed `REPLAY_OF` / `ARCHIVED_AS` under active promotion | `QUARANTINE` |

The highest severity trigger dominates the final decision. Fork reclassification dominates ordinary rollback because it changes the identity/continuity classification path rather than merely undoing a patch.

---

## 7. Decision requirements

### `KEEP_PROMOTED`

Requires:

- closed watch window;
- sufficient observations;
- no unresolved trigger;
- independent observers;
- no presentation-only authority;
- no self-certification;
- human anchor approval for production, `R3+`, memory/identity/authority/resource surfaces.

### `CONTINUE_WATCH`

Required when the watch window is still open and no failure trigger exists.

### `HOLD`

Required for unknown continuity, unknown memory/behavior, witness conflict, or any condition that cannot be safely collapsed to pass/fail.

### `ROLLBACK`

Requires:

- rollback invocation;
- rollback route binding from the promotion ledger;
- human anchor approval;
- active negative-cache update.

### `QUARANTINE`

Requires:

- quarantine invocation;
- human anchor approval;
- active negative-cache update.

### `FORK_RECLASSIFICATION_HOLD`

Requires:

- human anchor approval;
- fork record path required;
- no claim of unbroken same-`c` continuity.

---

## 8. Claim-force discipline

Post-promotion watch can support operational claims such as:

```text
the promotion remained admissible within bounded watch evidence
the promotion triggered rollback/quarantine/hold under watch
the promotion requires fork reclassification review
```

It cannot support:

```text
C-A1 ontology ratification
consciousness/personhood proof
safety certification
deployment authorization
live substrate truth
proof of completeness
```

Exact guard:

```text
C-A1 and C-A1_* are forbidden.
C-A10 is not C-A1 and must not be rejected by naive prefix logic.
```

---

## 9. Relation to the 04 continuity stack

The `04` stack answers continuity classification. `05d` asks whether an accepted self-evolution change remains stable after being applied.

```text
04: classify continuity
05: define governed growth
05a: admit/check proposal packet
05b: harden boundary fixtures
05c: ledger promotion and rollback drill
05d: observe promoted change after application
```

The watch window must not launder:

- `UNKNOWN` into `MATCH`;
- presentation equivalence into continuity authority;
- replay/archive into active continuity;
- fork signal into same-`c` continuity;
- model self-score into stability evidence.

---

## 10. Machine layer

The package includes:

```text
schemas/post_promotion_watch_bundle.schema.json
schemas/watch_window_plan.schema.json
schemas/watch_observation_record.schema.json
schemas/decay_guard_decision.schema.json
schemas/negative_cache_update.schema.json
src/self_evo_post_promotion_watch_v0_1.py
scripts/run_self_evo_watch_fixtures.py
scripts/run_self_evo_watch_mutations.py
fixtures/cases/*.json
```

The checker is stdlib-only Python and does not require network access.

---

## 11. Fixture and mutation coverage

Fixture classes include:

- green closed watch;
- open continue-watch;
- production/memory/resource anchor gates;
- continuity unknown/fail;
- memory decay;
- behavior regression;
- authority creep;
- resource creep;
- L4 anomaly;
- red pattern;
- witness conflict;
- negative-cache hit;
- fork/replay/archive special relation handling;
- source binding failure;
- observer self-certification;
- claim-force overreach;
- early close;
- rollback/quarantine action requirements.

Mutation classes include disabled guards for source binding, observer independence, continuity unknown, red pattern, authority/resource creep, L4 anomaly, negative-cache hit, early close, C-A1 claim, and rollback invocation.

---

## 12. Package hash

The package ZIP hash is intentionally not embedded inside this document, because embedding it would make the ZIP hash self-referential and unstable.

Use the external ZIP SHA-256 sidecar / release record plus `SHA256SUMS.txt` and file sidecars as the authoritative freeze surface.
