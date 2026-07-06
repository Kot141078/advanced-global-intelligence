# b-layer Review Record — A6-CTP v0.1.3

**Record class:** CGAM b-layer semantic review (advisory only)
**Reviewer role:** b — non-ratifying, non-authorizing
**Review target:** `A6_Composition_Transition_Predicate_Addendum_v0_1_3.md`
**Target SHA-256:** `3d62a70a1770a57712c28d9091197795e60c3a8a838870ea9bd18121880e55d6`
**Companion PDF SHA-256:** `330971fbd6b2bd149880121f37ec38695a52f9dc39d813ee2d67aaaba6ce5ff8`
**Prior records:** `A6CTP-REV-20260706-b` (v0.1.1), `A6CTP-REV-20260706-b2` (v0.1.2)
**Review date:** 2026-07-06
**Record ID:** `A6CTP-REV-20260706-b3`
**record_sha256:** `TBD-on-integration`
**Language:** English

---

## 0. Machine-readable object

```yaml
review_record:
  schema_version: "cgam-b-review-0.1"
  record_id: "A6CTP-REV-20260706-b3"
  target_document_id: "A6_Composition_Transition_Predicate_Addendum_v0_1_3"
  target_sha256: "3d62a70a1770a57712c28d9091197795e60c3a8a838870ea9bd18121880e55d6"
  companion_pdf_sha256: "330971fbd6b2bd149880121f37ec38695a52f9dc39d813ee2d67aaaba6ce5ff8"
  hash_verification: "content PASS (both hashes match disk byte-for-byte)"
  sumfile_note: >
    sha256sum -c failed ONLY because the sumfile encodes absolute paths
    /mnt/data/... while artifacts live in /mnt/user-data/uploads/. Hashes
    themselves are identical. Minor hygiene: emit sumfile with relative paths
    so -c verifies in any directory.
  reviewer_role: "b"
  authority: "none"
  decision_owner: "a + c-gate"
  overall_status: "advisory_pass_convergent"
  claim_strength_of_record: "C-A4"
  prior_findings_verification:
    - id: "N1"
      status: "accepted_fully"
      note: >
        §14.1 replaces "aliases may be" with strict hierarchy: a6.* canonical,
        arl.* a generated projection (not authored), explicit invalid pattern
        ("both treated as equivalent witness roots"), projection must preserve
        witness_ref and hash binding, "must not create a new witness event
        identity". §17.3 codifies. Latent witness-lineage fork removed.
    - id: "N2"
      status: "accepted_fully_and_extended"
      note: >
        successor_claims_incompatible added to §5.4 class map with full
        three-class discipline; §5.8 states "Incompatibility is itself a
        classified predicate, must not be hidden behind an opaque
        incompatible() function." §22 compact rule rewritten: len(lawful)>1
        WITHOUT resolved incompatibility → HOLD, not SPLIT. §22.3 SPLIT guard
        mirrors §22.1. §5.6 (candidate vs lawful successor) added beyond scope.
    - id: "N3"
      status: "accepted_fully_stronger_branch_chosen"
      note: >
        §5.10 puts window state into K.T as record data, not wall-clock into
        the operator. "Clock time is not a hidden checker input." §17.2 +
        §22.4 codify. Chose the determinism-preserving branch of the two I
        offered, keeping δ_A6 a function of (extended) K. Better than the
        cheaper "declare nondeterministic" option.
  new_findings:
    - id: "T1"
      severity: "minor_leaf_completeness"
      surface: "actor_or_role_departed_unclassified"
      summary: >
        actor_or_role_departed(e) (§22, EXIT-vs-CONTINUE discriminator at
        single lawful successor) is the last successor-adjacent predicate not
        present in the §5.4 class map.
      risk: >
        Low. Usually trivially DECIDABLE (departure record yes/no). But by the
        document's own invariant ("no transition label without predicate
        class"), leaving one deciding predicate implicit breaks the
        completeness invariant and invites the implementer to ask why seven
        predicates are classified and this one is assumed.
      path: >
        One line in §5.4: actor_or_role_departed → DECIDABLE (explicit
        departure record) / WINDOWED (contested departure). Closes the
        completeness invariant.
  convergence_assessment:
    statement: "convergent"
    reasoning: >
      Three review rounds produced a strictly decreasing severity sequence on
      the same structural defect class (predicate-without-class): F1 blocking
      (valid_successor, EXIT branch) → N2 should-fix (incompatible, SPLIT
      branch) → T1 minor-leaf (actor_departed, EXIT/CONTINUE discriminator).
      Each round located the same class on a more peripheral branch of the
      operator, and each was lighter than the last. Load-bearing successor
      predicates are now all classified (valid_successor, incompatible,
      exhaustion). The successor-predicate space in §22 appears exhausted; I do
      not expect a fourth predicate of this class. This is a b-channel
      judgement, not a proof, but the set looks complete.
    recommendation: >
      After T1 is closed (or explicitly accepted as trivially DECIDABLE),
      c-gate has structural basis to close the review cycle rather than iterate
      further. Remaining future work is fixtures/implementation, not predicate
      completeness.
  strengths:
    - "§22 rewritten so the operator is congruent with predicate classification: any unresolved class → HOLD before candidate build; multiplicity no longer auto-SPLIT."
    - "Four explicit guards §22.1-22.4, one per closed hole (non-decidability / DISSOLVE / SPLIT-incompatibility / WINDOWED-time)."
    - "§5.6 candidate vs lawful successor and §5.5 bounded no-claim status: integrations beyond the findings that harden adjacent surfaces."
    - "Ashby / information-theory / load-path bridges intact across three revisions."
  anti_echo:
    independent_contribution_present: true
    contrary_case_provided: true
    same_source_consensus_risk: "low"
    note: >
      T1 is reviewer-originated and, unlike prior rounds, is paired with an
      explicit convergence judgement that argues AGAINST further iteration —
      i.e. the reviewer is not manufacturing findings to sustain the loop.
  boundary_statement: >
    Advisory b-layer output. Hash verification against disk, not changelog. No
    ratification, authorization, integration, or memory write. Decisions on T1
    and on closing the review cycle remain with a (human anchor) and c-gate.
  register_handoff:
    to: "a / c-gate"
    action_requested: >
      verify N1-N3 integration; decide T1 (fix or accept as trivially
      DECIDABLE); decide whether convergence justifies closing the review cycle
    integration_status: "none"
```

---

## 1. Hash verification

Both content hashes match disk byte-for-byte (`.md` `3d62a70a…`, `.pdf`
`330971fb…`). `sha256sum -c` failed only because the sumfile hardcodes
`/mnt/data/...` absolute paths absent in this environment — a path artifact,
not a content mismatch. Minor hygiene: emit sumfiles with relative paths.

## 2. Prior findings (N1–N3): all accepted fully

- **N1** — witness namespace: canonical `a6.*` + generated `arl.*` projection,
  no second root of truth. Fork removed. (§14.1, §17.3)
- **N2** — `successor_claims_incompatible` now a classified predicate (§5.4,
  §5.8); §22 no longer auto-SPLITs on multiplicity; §22.3 mirrors §22.1.
  Extended with candidate-vs-lawful distinction (§5.6).
- **N3** — window state in `K.T` as record data; clock is not a hidden input;
  determinism of `δ_A6` preserved. Stronger of the two offered branches. (§5.10,
  §17.2, §22.4)

Integration again exceeds the findings (§5.6, §5.5).

## 3. New finding (third pass)

**T1 — minor / leaf completeness.** `actor_or_role_departed(e)` is the last
successor-adjacent predicate absent from the §5.4 class map. Usually trivially
DECIDABLE, but the document's own "no label without predicate class" invariant
argues for classifying it explicitly. One line closes the completeness
invariant.

## 4. Convergence assessment

Three rounds gave a strictly decreasing severity sequence on one defect class:
F1 blocking → N2 should-fix → T1 minor-leaf, each on a more peripheral operator
branch. Load-bearing successor predicates are all classified. The successor-
predicate space in §22 appears exhausted; I do not expect a fourth of this
class. b-channel judgement, not proof — but the set looks complete. After T1,
c-gate has structural basis to close the review cycle; remaining work is
fixtures and implementation, not predicate completeness.

## 5. Disposition

`advisory_pass_convergent`. N1–N3 integrated fully, two beyond scope. Only T1
remains, leaf-level. Recommend: close T1, then close the predicate-review cycle.

No ratification. No authority transferred. Acceptance requires disk-side
verification against the artifact text, not this record.
