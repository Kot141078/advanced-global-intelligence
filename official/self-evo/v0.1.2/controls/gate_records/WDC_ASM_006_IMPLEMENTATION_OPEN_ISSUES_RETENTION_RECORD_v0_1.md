# WDC-ASM-006 Implementation Open Issues Retention Record v0.1

## Package-control record for retaining implementation open issues without overclaiming release readiness

**Status:** Gate closure / retention record  
**Date:** 2026-06-27T20:05:00Z  
**Record ID:** `WDC_ASM_006_IMPLEMENTATION_OPEN_ISSUES_RETENTION_RECORD_v0_1`  
**Gate:** `WDC-ASM-006` — record remaining implementation open issues without overclaiming release readiness  
**Closure result:** `CLOSED_AS_RETAINED`  
**Decision owner:** `c-gate + human anchor (a)`  
**Author / package owner:** Kotov Ivan, Bruxelles, Belgique, 2026

> This record closes the documentary gate that requires remaining implementation work to be retained visibly. It does not close the implementation work itself.

---

## 0. Executive statement

`WDC-ASM-006` is satisfied because the WDC package retains the unresolved implementation work in `SELF-EVO-10` and keeps all implementation, conformance, deployment, and runtime claims false.

Evidence:

```text
10_Self_Evo_Open_Issues_WDC_Delta_v0_1_2_v0_1_1.md
sha256: bd87725ddf72ddeac09db597900c465492d570dbaaf68391e26b327aabba5790
review: SEOI_WDC_DELTA_REVIEW_RECORD_v0_1_1.md
review_sha256: c4db6ef14ec27dc5a5c4a618a59cbb5b4be41ab06d9fce3f575940b9f992fc2c
review_result: PASS
```

The closure is retention-only: it records that open implementation issues are visible and bounded. It does not solve them.

---

## 1. Corpus bridge set

### 1.1 Explicit bridge: `c = a + b`

Open implementation issues belong to `b`: they are backlog, implementation, UI, checker, runner, calibration, and runtime work. They do not become `c` maturity and they do not speak as `a` approval.

### 1.2 Quiet bridge I — information theory

An open issue is a preserved uncertainty bit. Deleting or hiding it would compress the package in a dangerous direction. Retaining it keeps the channel honest: the reader sees what is known, what is not implemented, and what must not be claimed.

### 1.3 Quiet bridge II — cybernetics

A control loop needs pending-fault memory. `WDC-ASM-006` keeps the unresolved implementation tasks in the loop so future agents cannot optimize for a clean-looking release surface while bypassing the work.

### 1.4 Quiet bridge III — physiology

A chart may say the diagnosis is understood while the therapy is not yet complete. The retained open issues are the treatment plan, not a cure.

### 1.5 Earth paragraph

A commissioning binder may contain open punch-list items. The honest handover is not “finished”; it is “assembled with these items explicitly not commissioned.” `WDC-ASM-006` is that punch-list retention.

---

## 2. Retained implementation nonclaims

The final package MUST keep these false:

```yaml
checker_implementation_certified: false
fixture_runner_executed: false
implementation_ready: false
runtime_self_evolution_authorized: false
memory_write_authorized: false
autonomous_resource_acquisition_authorized: false
conformance_certificate: false
deployment_authorization: false
witness_independence_certification: false
```

---

## 3. Retained work categories

The open issues remain live work items for future implementation phases:

```text
Witness Resource Floor calibration policy
Challenge Survivability Test acceptance criteria
WRCG machine-record extraction and schema binding
WDC Local Checker implementation binding
WDC fixture runner execution and run records
human review UI / fatigue controls
security / privacy / evidence redaction
lifecycle / dashboard / monitoring
public wording maintenance
package placement and release hygiene
```

These are not blockers to local document package assembly when retained as nonclaims. They are blockers to implementation, conformance, deployment, and witness-independence certification.

---

## 4. Closure semantics

```yaml
WDC-ASM-006:
  status: "CLOSED_AS_RETAINED"
  implementation_open_issues_visible: true
  implementation_open_issues_resolved: false
  release_readiness_overclaim: false
  blocks_checker_conformance_claim: true
  blocks_deployment_claim: true
  blocks_witness_independence_certification: true
```

---

## 5. Manifest effect

The downstream manifest update under `WDC-ASM-001` MUST set:

```yaml
WDC-ASM-006: CLOSED_AS_RETAINED
implementation_open_issues_retained: true
checker_implementation_certified: false
fixture_runner_executed: false
implementation_ready: false
```

---

## 6. Closing

```text
WDC-ASM-006: CLOSED_AS_RETAINED.
The implementation work remains open and visible.
The package may be assembled as a document package only because it explicitly does not claim implementation, conformance, deployment, or witness-independence certification.
```
