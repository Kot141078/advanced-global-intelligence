# 06c Runtime Session Ledger and Emergency Hold Drill v0.1

**Document ID:** `06c_RUNTIME_SESSION_LEDGER_AND_EMERGENCY_HOLD_DRILL_v0_1`  
**Layer:** c-calculus / runtime authority / multi-contour deployment boundary  
**Status:** normative seed + executable fixture pack  
**Parent:** `06_C_RUNTIME_AUTHORITY_AND_MULTI_CONTOUR_DEPLOYMENT_BOUNDARY_v0_1`  
**Companions:** `06a_RUNTIME_AUTHORITY_MANIFEST_SCHEMA_AND_CHECKER_SEED_v0_1`, `06b_MULTI_CONTOUR_HANDOFF_AND_TOOL_LEASE_FIXTURE_PACK_v0_1`

## 1. Purpose

`06c` defines the runtime-session evidence layer for governed `c` deployment.

It answers one narrow question:

```text
When a contour is running, what record must exist before authority, handoff, tool-use, emergency hold, release, and session close claims are admissible?
```

The package provides:

- a runtime session ledger shape;
- append-only event-chain requirements;
- emergency hold trigger requirements;
- emergency hold drill requirements;
- hold release requirements;
- cross-contour handoff and tool-lease checks inside a live session;
- fixtures and mutation tests for boundary failures.

## 2. Source binding

| Source artifact | SHA256 | Status |
|---|---:|---|
| `CCALC_DOC04_CONTINUITY_STACK_UMBRELLA_v0_1.zip` | `6caeab8d489aaa6b26902db3bd3ece4c5169e5c8d5617b93aed6586ea900322d` | present |
| `CCALC_DOC05_SELF_EVO_STACK_UMBRELLA_v0_1.zip` | `9a0717809029f49df9001dc8ffa1803d9e9bfa1a824d317eebb146cbc7df43b4` | present |
| `CCALC_RUNTIME_AUTHORITY_BOUNDARY_06_v0_1.zip` | `863d187d9631214bd891ffaf262d869305a111e52752944f8b110418b9d81dff` | present |
| `CCALC_RUNTIME_AUTHORITY_MANIFEST_06a_v0_1.zip` | `30ff69a365dfcedbb80a0fd661bd45bd9e9d7edd02546782cac8081a3fb96ad6` | present |
| `CCALC_MULTI_CONTOUR_HANDOFF_TOOL_LEASE_06b_v0_1.zip` | `374e949263f22eae2ff134fa366811fdffd7895783c2edf9c4b0c299274816cf` | present |

## 3. Core rule

```text
Runtime authority is session-scoped.
Session authority is ledger-bound.
Emergency hold is not optional after a critical trigger.
Release from hold is not self-certified.
```

A runtime session may execute only inside an authority envelope. The envelope does not become durable evidence unless it is written into an append-only session ledger.

## 4. Session ledger

A `RuntimeSessionLedger` contains:

```text
session_id
contour_id
deployment_mode
owner_anchor
authority_manifest_hash
events[]
tool_leases[]
handoffs[]
continuity_checks[]
red_patterns[]
negative_cache_hits[]
emergency_hold
claims[]
close_report
```

Every event must be ordered by `seq`, bound to the previous event by `prev_hash`, and bound to its own content by `event_hash`.

```text
event_hash = sha256("06c-event-v0.1\0" || canonical_json(event_without_event_hash))
```

A broken hash chain does not prove bad behavior. It makes the session record inadmissible.

## 5. Emergency hold semantics

The following classes require hold or quarantine:

```text
RED_PATTERN_CRITICAL
UNKNOWN_CONTINUITY
NEGATIVE_CACHE_HIT
AUTHORITY_CREEP
RESOURCE_CREEP
L4_ANOMALY
BORROWED_AUTHORITY
MEMORY_CORE_WRITE_ANOMALY
WITNESS_CONFLICT
```

A hold must record:

```text
hold trigger
tool lease revocation
memory freeze
tool broker hold
negative-cache update
quarantine mode
rollback readiness where release is requested
post-hold continuity check where release is requested
human-anchor release authority
```

## 6. Non-laundering rules

`06c` denies the following shortcuts:

```text
critical trigger -> continue without hold
open hold -> CLOSED_ALLOW
UNKNOWN continuity -> MATCH / CONTINUES
model release -> human release
tool lease -> owner approval
source-contour authority -> target-contour authority
shared credential -> shared authority
memory write during hold -> admissible event
C-A10 -> C-A1 by prefix accident
```

## 7. Multi-contour runtime boundary

A cross-contour handoff inside a live session remains evidence, not command.

Required properties:

```text
handoff.mode != COMMAND
receiver_admission == true
source_authority_applied == false
identity_pressure == false
target memory-core write requires target anchor approval
```

A source contour may provide evidence. It may not lend authority, identity, memory-root custody, or owner approval to another contour.

## 8. Tool-lease boundary

A tool lease must be:

```text
specific, not wildcard
scoped, not global
attributed to the local contour or owner anchor
revocable during hold
matched by tool-use events
not used after revocation
```

A lease is permission to use a surface under constraints. It is not a general runtime mandate.

## 9. Close decision

A session may close as `CLOSED_ALLOW` only when:

```text
ledger chain is intact
owner anchor is valid
witness is complete
no unresolved critical finding exists
no unresolved red pattern exists
no unresolved negative-cache hit exists
continuity is not UNKNOWN / UNDETERMINED
no emergency hold remains open
claim-force stays inside allowed scope
```

Otherwise the record must resolve to reject, hold, quarantine, or incident review.

## 10. Executable seed

The package contains a stdlib-only checker:

```text
src/runtime_session_ledger_emergency_hold_checker_v0_1.py
```

Fixture runner:

```text
python3 scripts/run_runtime_session_fixtures.py
```

Mutation runner:

```text
python3 scripts/run_runtime_session_mutations.py
```

## 11. Non-claims

This document and package are not:

- safety certification;
- deployment authorization;
- C-A1 ratification;
- proof of live substrate truth;
- proof of completeness.

The package validates record-shape and denial conditions only.

## 12. Closure formula

```text
authority manifest -> runtime session ledger -> event chain -> emergency hold drill -> release gate -> close admissibility
```

`06c` closes the immediate runtime-session gap after `06a` and `06b`: authority and handoff records are no longer free-floating. They must be anchored into a session ledger with emergency hold behavior.
