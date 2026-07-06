# b-layer Review Record — A6-CTP v0.1.4

**Record class:** CGAM b-layer semantic review (advisory only)  
**Reviewer role:** b — non-ratifying, non-authorizing  
**Review target:** `A6_Composition_Transition_Predicate_Addendum_v0_1_4.md`  
**Target SHA-256:** `61126c2d8a71a03eaa301f181168d02c1334ad0a3c5b68d778a6565707eb6152`  
**Companion PDF SHA-256 (claimed by package; not verified in reviewer session):** `b371dace3e74e59e32fa736f5ac3bf13d9665f9856c1e7c5c30e9190955d4c89`  
**Prior records:** `A6CTP-REV-20260706-b` (v0.1.1), `A6CTP-REV-20260706-b2` (v0.1.2), `A6CTP-REV-20260706-b3` (v0.1.3)  
**Review date:** 2026-07-06  
**Record ID:** `A6CTP-REV-20260706-b4`  
**record_sha256:** `external-only; see SHA256SUMS`  
**Language:** English

---

## 0. Machine-readable object

```yaml
review_record:
  schema_version: "cgam-b-review-0.1"
  record_id: "A6CTP-REV-20260706-b4"
  target_document_id: "A6_Composition_Transition_Predicate_Addendum_v0_1_4"
  target_sha256: "61126c2d8a71a03eaa301f181168d02c1334ad0a3c5b68d778a6565707eb6152"
  companion_pdf_sha256_claimed: "b371dace3e74e59e32fa736f5ac3bf13d9665f9856c1e7c5c30e9190955d4c89"
  companion_pdf_status_in_reviewer_session: "UNVERIFIED — PDF not present on disk in the reviewer session; md hash matched sumfile byte-for-byte"
  reviewer_role: "b"
  authority: "none"
  decision_owner: "a + c-gate"
  overall_status: "advisory_pass_cycle_convergent_recommend_close"
  claim_strength_of_record: "C-A4"
  prior_finding_verification:
    - id: "T1"
      status: "accepted_fully_definition_and_executable_rule"
      note: >
        actor_or_role_departed added to §5.4 class map with full three-class
        discipline including a no-departure record path; new rule A6CTP-R25;
        red-line item 15; guard paragraph; and the §22 compact rule now runs
        classify_actor_or_role_departure as a separate gate: window_open /
        escalate_unresolved / decidable_unclear -> HOLD before the deciding
        branch, and inside len(lawful)==1 a ternary: departed -> EXIT,
        no_departure -> CONTINUE, else -> HOLD
        (reason="actor_or_role_departure_status_unclassified"). No path from a
        single lawful successor reaches EXIT or CONTINUE without an explicitly
        classified departure status. Closed in definition and executable rule.
  new_findings: []
  predicate_space_closure:
    statement: "closed"
    successor_predicates_in_operator:
      - "valid_successor (§5.3/§5.4) — classified"
      - "successor_claims_incompatible (§5.4/§5.8) — classified"
      - "successor_space_exhausted (§5.4/§5.9) — classified"
      - "actor_or_role_departed (§5.4) — classified in v0.1.4"
    existential_predicates_handled_by_bounded_discipline:
      - "admissible_successor_claims_exist / no_remaining / no_visible -> §5.5 bounded no-claim + §22.2 DISSOLVE guard; never machine-decided by absence"
    non_successor_gate:
      - "material_to_composition — entry gate, not a successor predicate"
    reasoning: >
      classify_actor_or_role_departure introduces no new sub-predicate: it
      consumes the same three classes from §5.4 and is closed by the §22 guard.
      The four deciding successor predicates are all in the class map with
      default HOLD. The predicate-without-class defect that recurred F1 -> N2 -> T1
      has no remaining branch to appear on. The b3 convergence prediction is
      confirmed: T1 was the last leaf.
  cycle_recommendation:
    recommend: "close the predicate-review cycle"
    basis: >
      Four rounds, strictly decreasing severity (F1 blocking -> N2 should-fix ->
      T1 minor-leaf -> b4 no-finding), on one defect class now exhausted. The
      deciding-predicate tree is complete. Remaining work is fixtures, checker
      implementation, and parent A6 DOI insertion before publication; none of
      these are predicate-completeness work. Further b-layer iteration on the
      predicate surface would manufacture findings, not surface them.
  outstanding_non_findings:
    - "Parent DOI still TBD in metadata — insert before publication."
    - "Companion PDF was not verifiable in reviewer session; verify separately if PDF hash binding is required."
    - "Use relative paths in future sumfiles."
  anti_echo:
    independent_contribution_present: true
    contrary_case_provided: false
    same_source_consensus_risk: "low"
    note: >
      No new finding is asserted because none exists on the predicate surface.
      Withholding a manufactured finding, and explicitly recommending cycle
      closure, is the anti-echo discipline here: the reviewer declines to
      sustain the loop for its own sake. A finding would be the echo; its
      absence, argued, is the signal.
  boundary_statement: >
    Advisory b-layer output. Markdown hash verified against disk in the reviewer
    session; PDF hash claimed but unverified in that session. No ratification,
    authorization, integration, or memory write. Decision to close the review
    cycle, insert parent DOI, and publish remains with a (human anchor) and
    c-gate.
  register_handoff:
    to: "a / c-gate"
    action_requested: >
      confirm T1 closure by disk-side read; decide to close the predicate-review
      cycle; schedule fixtures/implementation as separate work; insert parent
      A6 DOI before publication
    integration_status: "none"
```

---

## 1. Verification

`.md` hash `61126c2d…` matched the reviewer's disk byte-for-byte. The companion
PDF hash was claimed by the package but the PDF was not present in that reviewer
session; it is therefore marked **UNVERIFIED**, not mismatched. A separate
integration-side verification record may bind the PDF hash when the PDF artifact
is present.

## 2. T1 — closed in definition and executable rule

`actor_or_role_departed` is now a fully classified predicate (§5.4) with a
no-departure path, rule R25, red-line item 15, and a guard paragraph. The §22
compact rule runs `classify_actor_or_role_departure` as a separate gate and,
at a single lawful successor, branches ternary: departed -> EXIT,
no_departure -> CONTINUE, otherwise -> HOLD. No path reaches EXIT or CONTINUE
without an explicit classified departure status.

## 3. Predicate space is closed

The four deciding successor predicates — `valid_successor`,
`successor_claims_incompatible`, `successor_space_exhausted`, and
`actor_or_role_departed` — are all in the §5.4 class map with default HOLD.
Existential predicates are handled by §5.5 bounded no-claim discipline and the
§22.2 DISSOLVE guard, never decided by absence. `classify_actor_or_role_departure`
adds no new sub-predicate. The predicate-without-class defect that recurred
across F1 -> N2 -> T1 has no remaining branch to appear on.

## 4. Recommendation: close the cycle

Four rounds, strictly decreasing severity, one defect class now exhausted. The
deciding-predicate tree is complete. Remaining work — fixtures, checker
implementation, parent DOI insertion — is not predicate completeness. Continuing
b-layer iteration on this surface would manufacture findings rather than surface
them. Recommendation: c-gate should close the predicate-review cycle and move
the artifact to fixture / checker implementation work.

No ratification. No authority transferred. Confirmation requires disk-side read
of the artifact, not this record.
