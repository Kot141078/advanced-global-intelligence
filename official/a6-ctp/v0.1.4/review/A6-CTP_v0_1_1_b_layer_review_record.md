# b-layer Review Record — A6-CTP v0.1.1

**Record class:** CGAM b-layer semantic review (advisory only)
**Reviewer role:** b (semantic reviewer / checker) — non-ratifying, non-authorizing
**Review target:** `A6_Composition_Transition_Predicate_Addendum_v0_1_1.md`
**Target SHA-256:** `be1a6a750b770cef7d00e149ffec5db8c8a2d070dce8c49a8f57a3d7256d9b14`
**Review date:** 2026-07-06
**Record ID:** `A6CTP-REV-20260706-b`
**record_sha256:** `TBD-on-integration`
**Language:** English (normative artifact review)

---

## 0. Machine-readable object

```yaml
review_record:
  schema_version: "cgam-b-review-0.1"
  record_id: "A6CTP-REV-20260706-b"
  target_document_id: "A6_Composition_Transition_Predicate_Addendum_v0_1_1"
  target_sha256: "be1a6a750b770cef7d00e149ffec5db8c8a2d070dce8c49a8f57a3d7256d9b14"
  reviewer_role: "b"
  review_class: "semantic_advisory"
  authority: "none"          # b does not ratify, authorize, or integrate
  decision_owner: "a + c-gate"
  overall_status: "advisory_pass_with_findings"
  claim_strength_of_record: "C-A4"   # reviewer opinion, not authority
  findings:
    - id: "F1"
      severity: "blocking_for_v0_2"
      surface: "core_operator"
      summary: >
        lawful_successors(K,e) is the load-bearing predicate of the whole
        operator but is defined as a list containing existential-negation
        subpredicates (no_hidden_successor_claim, no_prohibited_authority
        _laundering). These cannot be discharged by a deterministic checker;
        they can only be declared after a bounded window or escalated.
      risk: >
        Section 22 presents the full branch as machine-decidable. A first
        implementer will place human judgment inside lawful_successors() under
        the appearance of a check — the exact laundering the document forbids
        (Section 21 item 12).
      path: >
        Split subpredicates into two explicit classes: DECIDABLE (witness
        appended? quorum satisfiable given roster? — yes/no) vs
        ESCALATE_ONLY (hidden claim absent? — window + ARL, never checker).
        Mark them in Section 5.3 and Section 22 so the machine/human boundary
        is visible, not hidden one layer down.
    - id: "F2"
      severity: "should_fix_for_v0_2"
      surface: "dissolve_gate_asymmetry"
      summary: >
        SPLIT requires positive proof of incompatible successor claims
        (Section 9.2). DISSOLVE requires proof of successor-space exhaustion
        (no admissible successor), an existential negation, but its gate is
        stated only negatively (Section 21 item 4) and is softer than SPLIT's.
      risk: >
        DISSOLVE is the only irreversible outcome (archive / line end). A
        fail-closed system must gate its heaviest irreversible outcome most
        strictly, not least. Current framing makes it easier to slide into
        DISSOLVE than into SPLIT.
      path: >
        Symmetrize: require an explicit successor_space_exhaustion_record with
        witness before DISSOLVE; default to HOLD otherwise. Make the DISSOLVE
        gate at least as strict as the SPLIT gate.
    - id: "F3"
      severity: "minor_hygiene"
      surface: "claim_strength_mapping"
      summary: >
        Header declares both C-A4 and C-A10 without mapping claim strength to
        section. Reader cannot tell which passages are draft clarification vs
        implementation-mapping guidance.
      path: >
        Attach claim strength per section (e.g. Sections 0-13 = C-A4;
        Sections 14-17 checker/impl = C-A10). Per corpus claim-strength
        discipline, class binds to section, not to whole document.
  strengths:
    - "Unique-lawful-successor threshold replaces headcount/emotion with a countable operator (∃! K')."
    - "Ashby (§4.2) and information-theory (§4.3) bridges independently converge on the same threshold — load-bearing, not decorative."
    - "HOLD reframed as active refusal to launder uncertainty into action (§24); post-hoc witness laundering closed (§21.12)."
    - "§19 back-propagates the operator to c = a + b itself: (a absent + b running = continuity) is marked invalid."
    - "Load-path bridge (§4.4-4.5) and earth paragraph make the critical/non-critical distinction bodily legible."
  anti_echo:
    independent_contribution_present: true
    contrary_case_provided: true
    same_source_consensus_risk: "low"
    note: >
      Findings F1-F3 are reviewer-originated and push against the document,
      not restatements of its own framing. F1 in particular contradicts the
      document's implicit claim of full machine-decidability.
  boundary_statement: >
    This record is advisory b-layer output. It does not ratify, authorize,
    integrate, or write to memory. All decisions, including whether to accept
    F1-F3, remain with a (human anchor) and the c-gate. Acceptance requires
    disk-side verification against the artifact text, not this narration.
  register_handoff:
    to: "a / c-gate"
    action_requested: "review findings; decide accept/reject per finding; no auto-integration"
    integration_status: "none"
```

---

## 1. Human-readable summary

The addendum closes a real gap: it replaces "who left / who feels wronged /
who is louder" with a countable transition operator whose threshold is
**unique lawful successor** (`∃! K'`). EXIT = departure with exactly one
lawful continuation; SPLIT = loss of unique continuation under incompatible
claims; HOLD = refusal to launder uncertainty into action; DISSOLVE = no
admissible successor remains. The operator is partial and fail-closed, which
is correct.

The two hidden bridges (Ashby requisite variety; information-theoretic
successor selection) are not ornamental — they give a second and third
independent definition of the same threshold, which is why the threshold
reads as real rather than stipulated.

## 2. Findings (see YAML for structured form)

**F1 — blocking for v0.2 — `lawful_successors` is undefined at the load-bearing point.**
The whole operator rests on this predicate, yet it contains existential
negations ("no hidden successor claim", "no prohibited authority laundering")
that a deterministic checker cannot discharge. Section 22 presents the branch
as machine-decidable; part of it is not. Unless DECIDABLE vs ESCALATE_ONLY
subpredicates are split explicitly, an implementer will bury human judgment
inside a function named like a check — the precise laundering §21.12 forbids.

**F2 — should fix for v0.2 — DISSOLVE gate is asymmetrically soft.**
SPLIT demands positive proof of incompatible claims; DISSOLVE demands proof of
successor-space exhaustion but is gated only negatively and more weakly.
DISSOLVE is the sole irreversible outcome. A fail-closed system must gate its
heaviest irreversible step most strictly. Require a witnessed
`successor_space_exhaustion_record`; default to HOLD otherwise.

**F3 — minor — claim-strength not mapped to section.**
Header carries both C-A4 and C-A10. Bind claim strength per section so
normative clarification and implementation-mapping guidance are not conflated.

## 3. Disposition

`advisory_pass_with_findings`. The document is sound in structure and closes
the transition-predicate gap at the correct level (operator with observable
threshold, not declaration). F1 is the single item worth closing before a
consolidated v0.2, because the document's "countability" claim rests on it.
F2 hardens the one irreversible path. F3 is hygiene.

No ratification. No authority transferred. Decision remains with a and c-gate.
