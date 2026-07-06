# b-layer Review Record — A6-CTP v0.1.2

**Record class:** CGAM b-layer semantic review (advisory only)
**Reviewer role:** b (semantic reviewer / checker) — non-ratifying, non-authorizing
**Review target:** `A6_Composition_Transition_Predicate_Addendum_v0_1_2.md`
**Target SHA-256:** `e5aa43d591cdfd7d24b58ac40fe9a6198f1eb13b36c9bd0cb2215b75ffd73d2e`
**Companion PDF SHA-256:** `acf1ab70049ab77a83428f66f029a2fd316bb5f37ce0de28c9b9bde4ab0cdfbb`
**Prior record integrated by target:** `A6CTP-REV-20260706-b` (against v0.1.1 SHA `be1a6a75…`)
**Review date:** 2026-07-06
**Record ID:** `A6CTP-REV-20260706-b2`
**record_sha256:** `TBD-on-integration`
**Language:** English

---

## 0. Machine-readable object

```yaml
review_record:
  schema_version: "cgam-b-review-0.1"
  record_id: "A6CTP-REV-20260706-b2"
  target_document_id: "A6_Composition_Transition_Predicate_Addendum_v0_1_2"
  target_sha256: "e5aa43d591cdfd7d24b58ac40fe9a6198f1eb13b36c9bd0cb2215b75ffd73d2e"
  companion_pdf_sha256: "acf1ab70049ab77a83428f66f029a2fd316bb5f37ce0de28c9b9bde4ab0cdfbb"
  sumfile_selfconsistent: true
  hash_verification: "PASS (sha256sum -c OK for both .md and .pdf)"
  reviewer_role: "b"
  review_class: "semantic_advisory"
  authority: "none"
  decision_owner: "a + c-gate"
  overall_status: "advisory_pass_with_minor_findings"
  claim_strength_of_record: "C-A4"
  prior_findings_verification:
    - id: "F1"
      status: "accepted_substantively"
      note: >
        §5.3 introduces DECIDABLE/WINDOWED/ESCALATE_ONLY classes; §5.4 assigns
        each predicate by name; §5.5 adds bounded no-claim status (beyond the
        original finding scope); §22.1 adds explicit laundering guard; R17/R20
        codify. Integration exceeds the finding — bounded no-claim status was
        not requested and closes the existential-negation hole deeper.
    - id: "F2"
      status: "accepted_and_symmetrized"
      note: >
        §5.9 defines successor_space_exhaustion_record with full field schema;
        §11.2 default rule forces HOLD unless complete+witnessed; DISSOLVE now
        gated stricter than SPLIT. Asymmetry removed. §24: "A missing claimant
        is not exhaustion."
    - id: "F3"
      status: "accepted"
      note: >
        §1.4 provides section-level claim-strength table (C-A4 / C-A7 / C-A10);
        class binds to section+evidence, not document title.
  new_findings:
    - id: "N1"
      severity: "minor_but_witness_lineage"
      surface: "witness_event_naming"
      summary: >
        §14.1 provides two parallel event-name sets (a6.composition_* and
        arl.composition_*) as "aliases may be" — a fork, not a resolution.
      risk: >
        Two names for one witness event is a latent witness-lineage fork — the
        exact §13 SPLIT trigger ("witness chain broken or forked"). A document
        about classifying forks contains a potential fork in its own witness
        schema. One implementer writes a6.*, another arl.*, checker seeks one,
        log holds the other.
      path: >
        Declare one canonical set and one derived projection with an explicit
        1:1 mapping and direction ("a6.* canonical; arl.* is the ARL-facing
        projection, generated not authored"). Not "aliases may be."
    - id: "N2"
      severity: "should_fix_for_v0_2"
      surface: "incompatible_predicate_unclassified"
      summary: >
        F1 discipline was applied to valid_successor but NOT to the
        incompatible() / admissible_incompatible_successor_claims_exist()
        predicate in §22, which decides the EXIT/SPLIT boundary. §5.8 defines
        incompatibility semantically but does not assign it a DECIDABLE/
        WINDOWED/ESCALATE_ONLY class in the §5.4 map.
      risk: >
        Second-order F1 on the SPLIT branch. Whether two continuation claims
        are incompatible is generally not DECIDABLE — may look compatible on
        the record surface, be incompatible in standing substance (ARL only).
        A checker that honestly classified all successor predicates will still
        hit incompatible() and either under-call to EXIT (incompatibility not
        machine-proven) or over-call to SPLIT.
      path: >
        Add successor_claims_incompatible to §5.4 predicate class map, likely
        WINDOWED/ESCALATE_ONLY, default HOLD when unresolved. Symmetry: if
        lawful_successor passes through three classes, incompatible must too.
    - id: "N3"
      severity: "subtle_structural"
      surface: "time_absent_from_state_model"
      summary: >
        WINDOWED (§5.3) introduces a temporal axis (windows open/close), but
        state K (§5.1) is static (P,R,S,O,Q,W,M,X,I) with no time dimension,
        and δ_A6 : K × Event ⇀ Decision maps instantaneous state. Where does
        "window open until T" live?
      risk: >
        If a WINDOWED predicate depends on whether a window has elapsed, the
        operator is not a pure function of (K,e) — it depends on a clock not
        represented in the model. Two calls on the same (K,e) at different
        times yield different results (window_open → window_closed_no_claim),
        contradicting the §17 "deterministic checker" claim.
      path: >
        Either put time into K explicitly (window timestamps in state, δ stays
        a function of extended K), OR acknowledge in §17.1 that WINDOWED
        transitions are time-nondeterministic by design and the checker returns
        window_open as a terminal status without recomputation. The second is
        cheaper and more honest. Currently a silent gap between §5.1 and §5.3.
  strengths_preserved:
    - "Ashby / information-theory / load-path bridges intact and load-bearing."
    - "§24 closing sharpened: checker-is-not-a-court, missing-claimant-is-not-exhaustion, hidden-judgment-in-a-function-name-is-laundering — each closes one abuse class, all derived from accepted findings."
    - "§5.5 bounded no-claim status: converts existential negation into bounded governance status (beyond original F1 scope)."
    - "Red-line §21 extended (13,14) precisely along F1; §22.1/§22.2 explicit guards."
  anti_echo:
    independent_contribution_present: true
    contrary_case_provided: true
    same_source_consensus_risk: "low"
    note: >
      N1-N3 are reviewer-originated second-pass findings, not restatements.
      N2 in particular contradicts an implicit completeness claim: that F1
      discipline covers the whole operator — it covers the EXIT branch, not
      the SPLIT-boundary predicate.
  boundary_statement: >
    Advisory b-layer output. No ratification, authorization, integration, or
    memory write. Hash verification performed against artifact on disk, not
    against changelog narration. All decisions, including whether to accept
    N1-N3, remain with a (human anchor) and the c-gate.
  register_handoff:
    to: "a / c-gate"
    action_requested: "verify F1-F3 integration acceptance; decide on N1-N3; no auto-integration"
    integration_status: "none"
```

---

## 1. Hash verification (performed first, against disk)

`SHA256SUMS_A6_CTP_v0_1_2.txt` is self-consistent and matches the artifacts on
disk. `sha256sum -c` returns OK for both `.md` (`e5aa43d5…`) and `.pdf`
(`acf1ab70…`). Verification is against the artifact, not against the changelog
claim. Provenance chain to the prior review record (`A6CTP-REV-20260706-b`
against v0.1.1 SHA `be1a6a75…`) is correctly stated in the target's metadata.

## 2. Prior-findings verification

F1, F2, F3 are accepted **substantively**, not cosmetically. F1 is developed
past the finding: §5.5 bounded no-claim status was not requested and closes the
existential-negation hole deeper than the review asked. F2 is symmetrized —
DISSOLVE is now gated stricter than SPLIT, correcting the fail-closed inversion.
F3 binds claim strength per section. This is disciplined integration, not
box-ticking.

## 3. New findings (second pass)

**N1 — minor / witness-lineage.** §14.1 leaves `a6.*` vs `arl.*` event names as
"aliases may be" — a fork rather than a canon. Two names for one witness event
is a latent lineage fork, the very §13 SPLIT trigger. Declare one canonical set,
one generated projection, explicit 1:1 mapping.

**N2 — should-fix for v0.2.** F1 discipline covers `valid_successor` but not the
`incompatible()` predicate that decides the EXIT/SPLIT boundary (§22). §5.8
defines incompatibility semantically but never assigns it a predicate class in
§5.4. This is F1 second-order on the SPLIT branch: whether two claims are
incompatible is generally not DECIDABLE. Add `successor_claims_incompatible` to
the §5.4 map, default HOLD when unresolved. If `lawful_successor` passes through
three classes, `incompatible` must too.

**N3 — subtle / structural.** WINDOWED (§5.3) introduces time; state K (§5.1) is
static; `δ_A6` maps instantaneous state. A window-elapsed dependency makes the
operator clock-dependent, contradicting the §17 determinism claim. Either put
window timestamps into K, or state in §17.1 that WINDOWED transitions are
time-nondeterministic by design and the checker returns `window_open`
terminally. Second option cheaper and more honest. Silent gap between §5.1 and
§5.3.

## 4. Disposition

`advisory_pass_with_minor_findings`. The three prior findings are integrated
correctly, F1 beyond scope. The document is sound and closes the transition
predicate at operator level with observable thresholds. Second-pass findings are
all below blocking: N2 is the one worth closing before a consolidated v0.2,
because — like F1 — it concerns a load-bearing predicate, here on the SPLIT
branch rather than the EXIT branch. N1 touches witness-lineage and should not be
left as an alias fork. N3 is cheap to acknowledge.

No ratification. No authority transferred. Decision remains with a and c-gate.
Acceptance requires disk-side verification against the artifact text, not this
record.
