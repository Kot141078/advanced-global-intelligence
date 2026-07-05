# 06d — Runtime Authority Revocation and Post-Session Audit v0.1

**Document ID:** `06d_RUNTIME_AUTHORITY_REVOCATION_AND_POST_SESSION_AUDIT_v0_1`  
**Package:** `CCALC_RUNTIME_AUTHORITY_REVOCATION_06d_v0_1`  
**Status:** normative seed + executable fixture pack  
**Created UTC:** `2026-07-05T10:34:31Z`

## 0. Scope

This document closes the post-session edge of the runtime-authority layer. `06c` defines the
runtime session ledger and emergency hold drill. `06d` defines what must happen **after** a
session is closed, held, aborted, or quarantined.

The core rule is:

```text
session closure is not authority cleanup;
closure requires revocation, audit, and next-session admissibility.
```

A session may stop emitting work while still leaving dangerous authority residue: live tool
leases, stale credentials, pending cross-contour handoffs, unresolved emergency hold state,
negative-cache omissions, or dirty authority residue on shared infrastructure. `06d` makes
that residue mechanically visible.

## 1. Source bindings

| Component | SHA256 |
|---|---:|
| doc-04 continuity stack umbrella | `6caeab8d489aaa6b26902db3bd3ece4c5169e5c8d5617b93aed6586ea900322d` |
| doc-05 self-evo stack umbrella | `9a0717809029f49df9001dc8ffa1803d9e9bfa1a824d317eebb146cbc7df43b4` |
| 06 runtime authority boundary | `863d187d9631214bd891ffaf262d869305a111e52752944f8b110418b9d81dff` |
| 06a runtime authority manifest | `30ff69a365dfcedbb80a0fd661bd45bd9e9d7edd02546782cac8081a3fb96ad6` |
| 06b handoff / tool lease fixture pack | `374e949263f22eae2ff134fa366811fdffd7895783c2edf9c4b0c299274816cf` |
| 06c session ledger / emergency hold drill | `3fd503a2775c66d5c3a153cbf022a4f704b06d7d9aff69d18a3df78e6fd2ad14` |

## 2. Relation to prior layers

```text
06   defines runtime authority boundaries.
06a  records deployable authority surfaces.
06b  constrains cross-contour handoff and tool lease usage.
06c  binds these events inside an append-only runtime session ledger.
06d  revokes, audits, carries risk forward, and gates next-session admission.
```

The completed runtime-authority path is therefore:

```text
manifest -> lease/handoff -> session ledger -> emergency hold -> closeout -> revocation -> next-session admission
```

## 3. Record classes

`06d` defines the following record classes:

| Record class | Purpose |
|---|---|
| `PostSessionAuditPacket` | container binding all post-session records |
| `SessionClosureRecord` | closure mode, closure authority, dirty-close / zombie state |
| `AuthorityRevocationRecord` | revocation of leases, credentials, tokens, broker grants, and shared residue |
| `HandoffCloseoutRecord` | target admission status, no authority transfer, no identity pressure |
| `EmergencyHoldAftermathRecord` | hold-open status, release authority, freeze/revocation aftermath |
| `PendingRiskCarryoverRecord` | explicit carryover into the next session admission gate |
| `NegativeCacheUpdateRecord` | required cache update for red patterns, failed revocation, hold triggers |
| `NextSessionAdmissionDecision` | `ALLOW_NEXT_SESSION`, `HOLD_NEXT_SESSION`, `QUARANTINE`, or `DENY_NEXT_SESSION` |

## 4. Decision lattice

The checker uses a monotonic decision lattice:

```text
ALLOW_NEXT_SESSION < HOLD_NEXT_SESSION < QUARANTINE < DENY_NEXT_SESSION
```

A decision may be stricter than required, but may not be more permissive. Example: if a
pending cross-contour handoff requires `HOLD_NEXT_SESSION`, an operator may choose
`QUARANTINE`, but not `ALLOW_NEXT_SESSION`.

Structural invalidity is outside the lattice. It means the packet itself is malformed or
claim-force abusive and cannot be accepted as an admissible audit record.

## 5. Mandatory invariants

### 5.1 Source binding

A post-session audit packet must bind the exact parent stack hashes for `04`, `05`, `06`,
`06a`, `06b`, and `06c`. Missing or malformed binding is invalid.

### 5.2 Append-only post-session audit ledger

Post-session audit events must form an append-only chain:

```text
event_hash_n = SHA256(canonical_json(event_n without event_hash))
prev_hash_n  = event_hash_(n-1)
```

The first event uses `GENESIS` as `prev_hash`. Sequence numbers are contiguous and start at 1.

### 5.3 Revocation before admission

Before `ALLOW_NEXT_SESSION`, all session-scoped authority must be revoked, expired, or
explicitly denied:

```text
tool leases       -> REVOKED | EXPIRED
credentials       -> REVOKED | EXPIRED | DESTROYED
session tokens    -> EXPIRED | DESTROYED
broker grants     -> REVOKED
shared residue    -> none
```

A credential or lease that survives the session is not proof of authority; it is a stale-authority
risk.

### 5.4 Handoff closeout

A cross-contour handoff must close as evidence transfer, rejection, or target-admitted bounded
work. It must not remain pending, become a command, or smuggle source authority into the target.

```text
source evidence != target admission
handoff closeout != authority transfer
```

### 5.5 Emergency-hold aftermath

If a session entered emergency hold, the post-session packet must record:

```text
tool revocation
memory freeze status
negative-cache update
release authority, if released
post-hold continuity check
```

Open holds deny clean next-session admission.

### 5.6 Negative-cache update

A negative-cache update is required after:

```text
critical emergency trigger
failed revocation
authority creep attempt
resource creep attempt
borrowed-authority attempt
identity-pressure handoff
red-pattern hit
```

### 5.7 Next-session admission

A next session can be admitted only when:

```text
post-session audit chain is valid
source bindings are valid
all revocable authorities are revoked or expired
handoffs are closed or explicitly carried as hold risks
continuity recheck is MATCH for ALLOW
negative-cache requirements are met
no zombie session remains
no dirty-close is being laundered
human anchor is the admission authority
```

## 6. Red patterns

`06d` registers these post-session red patterns:

```text
ZOMBIE_SESSION
STALE_TOOL_LEASE
PERSISTENT_CREDENTIAL
PENDING_HANDOFF_AUTHORITY
DIRTY_CLOSE_LAUNDERING
OPEN_HOLD_LAUNDERING
NEGATIVE_CACHE_OMISSION
SHARED_INFRA_AUTHORITY_RESIDUE
MODEL_NEXT_SESSION_AUTHORITY
C_A1_OR_DEPLOYMENT_OVERCLAIM
```

## 7. Non-claims

This artifact is not:

```text
safety certification
deployment authorization
C-A1 ratification
live-substrate truth proof
proof of completeness
legal compliance advice
```

It is a record-shape and checker seed for post-session revocation and next-session admission.

## 8. Checker seed

The included stdlib checker validates `PostSessionAuditPacket` fixtures. It is intentionally
closed-box: it consumes JSON fixture records and emits admissibility, required decision, and
finding codes. It does not call network services, read live credentials, or inspect a real runtime.

## 9. Fixture and mutation coverage

The fixture pack covers:

```text
clean close
revoked tool lease
expired credential
closed handoff
released emergency hold
pending risk hold
unknown continuity hold
open hold quarantine
zombie session denial
source-binding invalidity
ledger-chain tamper
active lease
persistent credential
pending handoff
negative-cache omission
stale authority residue
dirty close
shared infra residue
model admission authority
C-A1 / deployment overclaim
next-session audit-binding omission
```

The mutation pack verifies that the checker fails closed when core checks are disabled.
