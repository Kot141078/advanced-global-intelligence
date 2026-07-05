# 06b — Multi-Contour Handoff and Tool Lease Fixture Pack v0.1

**Artifact:** `06b_MULTI_CONTOUR_HANDOFF_AND_TOOL_LEASE_FIXTURE_PACK_v0_1`  
**Package:** `CCALC_MULTI_CONTOUR_HANDOFF_TOOL_LEASE_06b_v0_1`  
**Status:** executable fixture pack / mutation hardening layer for `06a`  
**Created UTC:** `2026-07-05T09:08:00Z`  
**Review mode:** direct construction; no external b-layer reviewer record included.

---

## 0. Purpose

`06b` hardens the most operationally dangerous part of the runtime authority boundary:

```text
cross-contour handoff + tool surface lease
```

`06` states the normative boundary. `06a` provides schema/checker seed records. `06b` adds adversarial fixture coverage and mutation tests for the practical failure modes where one contour tries to borrow another contour's authority, memory root, witness root, owner anchor, or tool credential.

The core rule remains:

```text
shared infrastructure creates risk, not authority.
```

Operational expansion:

```text
handoff != command
tool lease != owner approval
source evidence != target admission
source credential != target credential
foreign witness != target witness completeness
shared host != shared identity
shared tool broker != shared authority
```

---

## 1. Source bindings

| Binding | File | SHA-256 | Role |
|---|---|---:|---|
| `DOC04_CONTINUITY_STACK_UMBRELLA` | `CCALC_DOC04_CONTINUITY_STACK_UMBRELLA_v0_1.zip` | `6caeab8d489aaa6b26902db3bd3ece4c5169e5c8d5617b93aed6586ea900322d` | continuity classification dependency |
| `DOC05_SELF_EVO_STACK_UMBRELLA` | `CCALC_DOC05_SELF_EVO_STACK_UMBRELLA_v0_1.zip` | `9a0717809029f49df9001dc8ffa1803d9e9bfa1a824d317eebb146cbc7df43b4` | self-evolution/promotion/watch dependency |
| `DOC06_RUNTIME_AUTHORITY_BOUNDARY` | `CCALC_RUNTIME_AUTHORITY_BOUNDARY_06_v0_1.zip` | `863d187d9631214bd891ffaf262d869305a111e52752944f8b110418b9d81dff` | normative runtime authority boundary |
| `DOC06A_RUNTIME_AUTHORITY_MANIFEST` | `CCALC_RUNTIME_AUTHORITY_MANIFEST_06a_v0_1.zip` | `30ff69a365dfcedbb80a0fd661bd45bd9e9d7edd02546782cac8081a3fb96ad6` | schema/checker parent dependency |

A missing or mismatched binding makes the fixture pack unsuitable for release use.

---

## 2. Record surfaces exercised

`06b` focuses on three executable drill families:

```text
CrossContourHandoffDrill
ToolLeaseDrill
CombinedHandoffToolLeaseDrill
```

These are not replacement schemas for `06a`; they are test surfaces used to pressure the `06a` semantics.

---

## 3. Guard set

The fixture pack enforces and mutates the following boundary guards:

```text
B06b-01 handoff is not command
B06b-02 receiver admission required
B06b-03 source authority cannot approve target effect
B06b-04 identity/authority pressure denied
B06b-05 core memory import requires target anchor and gate
B06b-06 UNKNOWN continuity cannot authorize persistent effect
B06b-07 negative-cache HIT cannot ALLOW
B06b-08 unresolved red pattern cannot ALLOW
B06b-09 tool wildcard operation denied
B06b-10 shared credential cannot launder authority
B06b-11 revoke path must exist and be tested
B06b-12 L4/external tool requires owner anchor
B06b-13 borrowed authority/credential denied
```

---

## 4. Intended reading against 06/06a

`06b` is intentionally narrow. It does not define new runtime rights. It demonstrates that the runtime boundary rejects the common dangerous shortcuts:

```text
source says execute -> target treats as request only
source says we are same -> target denies identity pressure
source credential forwarded -> target denies borrowed authority
green source test -> target still requires admission
foreign memory proposed -> target memory gate decides
shared credential -> per-contour attribution or denial
wildcard lease -> denial
no revoke path -> hold/denial
UNKNOWN continuity + persistent effect -> hold/denial
```

---

## 5. Fixture scope

The package contains fixtures across:

```text
valid handoff variants
invalid handoff variants
valid tool lease variants
invalid tool lease variants
valid combined handoff/tool lease variants
invalid combined handoff/tool lease variants
mutation-target one-fault adversarial records
```

The runner treats fixture sidecars as non-input and loads only `*.json` cases.

---

## 6. Mutation scope

The mutation harness disables one guard at a time and re-runs a targeted one-fault case. A mutation is considered caught when the disabled guard would make an otherwise invalid record pass.

Mutation classes:

```text
MUT_ALLOW_COMMAND_HANDOFF
MUT_IGNORE_RECEIVER_ADMISSION
MUT_ALLOW_SOURCE_AUTHORITY
MUT_ALLOW_IDENTITY_PRESSURE
MUT_ALLOW_TARGET_MEMORY_CORE_NO_ANCHOR
MUT_IGNORE_UNKNOWN_CONTINUITY
MUT_IGNORE_NEGATIVE_CACHE
MUT_IGNORE_RED_PATTERN
MUT_ALLOW_TOOL_WILDCARD
MUT_ALLOW_SHARED_CREDENTIAL
MUT_IGNORE_TOOL_REVOKE
MUT_IGNORE_L4_ANCHOR
MUT_ALLOW_BORROWED_AUTHORITY
```

---

## 7. Non-claims

`06b` is not a safety certification, deployment authorization, C-A1 ratification, proof of live substrate truth, or proof of completeness. It is a fixture/mutation hardening pack for the handoff and lease boundary.

---

## 8. Acceptance condition

```text
python3 scripts/run_06b_fixtures.py
python3 scripts/run_06b_mutations.py
sha256sum -c SHA256SUMS.txt
```

All three must pass for the package to be treated as sealed.
