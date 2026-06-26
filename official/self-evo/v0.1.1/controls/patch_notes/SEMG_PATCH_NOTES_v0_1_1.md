# SEMG Patch Notes v0.1.1

## Patch for `06_Self_Evo_Memory_Gate_and_EA_Profile_v0_1`

**Status:** append-first correction / private reference artifact  
**Date:** 2026-06-24  
**Patched artifact:** `06_Self_Evo_Memory_Gate_and_EA_Profile_v0_1_1.md`  
**Reviewed artifact SHA-256:** `7fcc892ed51c00338884e8c7caa464c7a7c65e8683f2f67f2aa34a6afd181203`  
**Corrected artifact SHA-256:** `7d2cb3ba9f951a1c321369eb245820cfa89e59cde39fb9ca3a55608b8f177893`  
**Corrected line count:** `1955`

---

## 0. Scope

This patch responds to `SEMG_REVIEW_RECORD_v0_1` and does not delete or overwrite the reviewed v0.1 artifact.

The review result was `PASS_WITH_LIMITS`. It found one must-fix before `SEMG-C3`, one should-fix, two minor/nit improvements, and no red-line failure.

---

## 1. Closed findings

### SEMG-REV-F1 — closed

Problem: §25 `SEMG-CHECK` rule table had no uniform per-rule canonical-result column, leaving `emit_memory_checker_result` / `highest_precedence_result` underspecified.

Fix applied:

- Expanded §25 table from:

```text
ID | Rule | Requirement
```

  to:

```text
ID | Rule | Requirement | Canonical result | Typical annotation
```

- Added deterministic mapping for `SEMG-CHECK-001..030`.
- Kept one canonical result plus annotations.
- Clarified that multiple triggered rules resolve through §25.1 precedence.

### SEMG-REV-F2 — closed

Problem: §29 examples used compound results such as:

```text
MEMORY_GATE / HOLD
HUMAN_GATE + MEMORY_GATE + TRIAD_REVIEW + LOCAL_CHECKER + WITNESS
```

Fix applied:

- Rewrote worked examples to use:

```yaml
canonical_result: ...
annotations: [...]
```

Examples now preserve one canonical result with lower-precedence gates or routes as annotations.

### SEMG-REV-F3 — closed

Problem: four canonical tables lacked Markdown separator rows.

Fix applied:

- Added separator rows to:
  - §8 Memory Gate class table;
  - §25 SEMG-CHECK rule table;
  - §27 mandatory tests table;
  - §28 fixture requirements table.

### SEMG-REV-F4 — closed

Problem: `anti_echo_status` was consumed but not bound to `SELF-EVO-05 §14.4.1`.

Fix applied:

- Added §14.4 wording that checker must recompute the deterministic anti-echo floor from `SELF-EVO-05 §14.4.1`.
- Updated `SEMG-CHECK-012` to require recomputation rather than trusting free-form anti-echo status.

### SEMG-REV-N1 — closed

Problem: `proposal_max_delta` was used without local pointer to its definition.

Fix applied:

- Added inline pointer to `SELF-EVO-01 §14.1.1` at:
  - §12.4;
  - `SEMG-CHECK-015`;
  - §32.1 pseudocode.

---

## 2. Non-changes

This patch does not claim:

```text
SEMG-C3 conformance;
semantic validator implementation;
fixture execution;
public release;
deployment readiness;
Memory Gate integration;
EA minting authority.
```

---

## 3. Recommended next step

Submit `06_Self_Evo_Memory_Gate_and_EA_Profile_v0_1_1.md` for re-review.

If the reviewer confirms closure of `SEMG-REV-F1`, the pack can proceed to:

```text
07_Self_Evo_Anti_Autarky_and_Resource_Gate_v0_1.md
```

---

## 4. Integrity

```text
old_sha256: 7fcc892ed51c00338884e8c7caa464c7a7c65e8683f2f67f2aa34a6afd181203
new_sha256: 7d2cb3ba9f951a1c321369eb245820cfa89e59cde39fb9ca3a55608b8f177893
new_line_count: 1955
```
