# BCEC v0.2.1-final — Witness-Compatible Review Record (b-layer)
## Defect-closure verification and convergence record for the Bounded Capability Extraction Clause

**Status:** Advisory review record / b-layer checker output / not an integration approval
**Record type:** witness-compatible review record + append-first convergence record
**Reviewer role:** b-layer checker (advisory only — no self-approval, no memory write, no integration authority)
**Date:** 2026-06-26
**Language:** English. Package format.

**Reviewed artifact:** `Bounded_Capability_Extraction_Clause_v0.2.1-final.md`
**Artifact SHA-256:** `421f82cce59bf10c93b360543332cab2cba2961794d9f2345716a036b3ae064f`

**Convergence chain:**
- `v0.1` (b-layer skeleton, authored upstream)
- `v0.2-final` — SHA-256 `a289dadf7440eef4ed65127eb7b6ec31bd857cb5965cbff1a23cb76eb6d3277a` — reviewed `PASS_WITH_LIMITS`, 6 refinement defects
- `v0.2.1-final` — SHA-256 `421f82cce59bf10c93b360543332cab2cba2961794d9f2345716a036b3ae064f` — this review

**Verdict:** `PASS` (b-layer review level; sealing and integration remain a separate step)
**Record seal:** `record_sha256: PLACEHOLDER_SEALED_AT_INTEGRATION`

---

## Machine-readable record

```yaml
review_record:
  schema: cgam-b-layer-review-0.1
  reviewed_artifact:
    name: Bounded_Capability_Extraction_Clause_v0.2.1-final.md
    sha256: 421f82cce59bf10c93b360543332cab2cba2961794d9f2345716a036b3ae064f
    declared_version: 0.2.1-final
  prior_review:
    artifact: Bounded_Capability_Extraction_Clause_v0.2-final.md
    sha256: a289dadf7440eef4ed65127eb7b6ec31bd857cb5965cbff1a23cb76eb6d3277a
    verdict: PASS_WITH_LIMITS
    defects_raised: [D1, D2, D3, D4, D5, D6]
  reviewer:
    role: b_layer_checker
    authority: advisory_only
    self_approval: false
    memory_write: false
    integration_authority: false
  verdict:
    value: PASS
    level: b_layer_review
    blocker_defects: 0
    structural_defects: 0
    soundness_defects: 0
    open_advisory_notes: 2          # N2 low, N4 trivial
    rationale: >
      All six refinement defects from the v0.2 review are closed and sound. The two
      items that withheld a clean PASS (D1 underived C_sybil_adjusted, D5 mixed-unit
      min) are fully resolved with correct, fail-closed derivations. Section renumbering
      after the new 6.2 insertion is clean and breaks no cross-reference. Bridges and
      earth paragraph are unchanged and still conform. Residual items are one
      low-severity interoperability recommendation and one trivial housekeeping nit;
      neither is structural, unsound, or axiom-violating.
  defect_closure:
    - id: D1
      title: C_sybil_adjusted lacks derivation
      status: CLOSED
      how: >
        1.12 and 6.8.1 add principal-review equivalence-class derivation:
        C_principal_g = min(sum allocated, principal profile, oracle profile, reconstruct);
        C_sybil_adjusted = sum over classes; missing principal cap fails closed.
      soundness: ok
    - id: D2
      title: populous-principal horizon not stated
      status: CLOSED
      how: >
        Stated in 0, 6.11, and renamed 21.4: principal accounting bounds concealed
        multiplicity, not genuine multiplicity; genuine multiplicity is bound by
        C_oracle_profile and C_reconstruct, the operator-set horizon.
      soundness: ok
    - id: D3
      title: retention double-encoded
      status: CLOSED
      how: 6.4 declares query-profile and retention orthogonal; retained_summary row removed.
      soundness: ok
    - id: D4
      title: cost(query_i) ambiguity
      status: CLOSED
      how: 6.7 defines cost(query_i) = risk_points x retention_mult x surface_mult, with MUST-NOT-ignore rule.
      soundness: ok
    - id: D5
      title: mixed-unit min()
      status: CLOSED
      how: >
        New 6.2 Single-Unit Rule; 6.8 cap-unit rule; 21.6 unit-conversion prohibition;
        packet fields single_unit_rule_satisfied / mixed_unit_computation_used.
      soundness: ok
    - id: D6
      title: C_license adjudication ambiguity
      status: CLOSED
      how: 1.12 clarifies C_license is a declared metering input, not contract adjudication.
      soundness: ok
  integrity_checks:
    section_sequence_top_level: "0..24 contiguous, no gap, no duplicate"
    section_sequence_6: "6.1..6.12 contiguous, no gap, no duplicate"
    cross_references_valid: true       # §12, §5.6, §9, §10, §11, §6.5, §1.12 all resolve
    renumber_breakage: none
  bridge_verification:
    explicit_bridges: 1                # 19.1 unchanged
    hidden_bridges: 2                  # 19.2 Ashby, 19.3 information theory, unchanged
    earth_paragraph: present           # 20 unchanged
    requirement_met: true
  observations:
    - id: N1
      type: observation_not_defect
      note: >
        C_oracle_profile and C_reconstruct appear in both the per-class cap (6.8.1)
        and the outer C_effective min (6.8). This is intentional defense-in-depth
        (per-class enforcement plus aggregate enforcement), not redundancy in error.
  advisory_notes:
    - id: N2
      severity: low
      locus: [1.12, 6.8.1]
      title: unknown-independence policy is an unbound implementation choice
      recommendation: >
        The choice between "collapse into shared unresolved class" and "fail closed"
        for unknown independence should be a declared oracle-profile parameter, so
        behavior is witnessable and comparable across conformant implementations.
    - id: N4
      severity: trivial
      locus: [header]
      title: Date field not bumped
      recommendation: Date still reads 2026-06-25 on the 0.2.1 revision; set to revision date.
  convergence:
    direction: v0.2-final -> v0.2.1-final
    mode: append_first
    thesis_changed: false
    correction_record_present: true    # 23
  record_sha256: PLACEHOLDER_SEALED_AT_INTEGRATION
```

---

## 1. Scope

This record is a focused b-layer pass over BCEC v0.2.1-final. It was produced as a direct diff against v0.2-final (the prior reviewed version) to verify whether the six refinement defects raised in the prior review are closed, whether the closures are sound, and whether the edits introduced any new defect. It also re-checks section/cross-reference integrity after renumbering, and confirms the bridges and earth paragraph still conform.

It does not seal, approve, integrate, or write to memory. `record_sha256` remains a placeholder.

---

## 2. Defect-closure verification

**D1 — `C_sybil_adjusted` derivation. CLOSED, sound.** Section 1.12 now derives the cap from extraction-principal equivalence classes `G`: for each class `g`, `C_principal_g = min(Σ_{p∈g} B_p_allocated, C_principal_profile(g), C_oracle_profile, C_reconstruct)`, and `C_sybil_adjusted = Σ_{g∈G} C_principal_g`. Section 6.8.1 adds the equivalence relation, a conservative accounting-state table, and the fail-closed handling for missing/ambiguous/wrong-unit principal caps. The added epistemic note is correct and valuable: principal classes are accounting objects, not identity claims; passing principal review permits a bounded metering treatment, it does not prove independence. The load-bearing anti-Sybil term is no longer a placeholder.

**D2 — populous-principal horizon. CLOSED, sound.** Stated in three places (0, 6.11, and the renamed 21.4 "External-Adversary and Populous-Principal Horizon"). The statement is exactly the honest position: principal accounting bounds *concealed* multiplicity (one party split across many handles) but not *genuine* multiplicity (many truly independent principals), and genuine multiplicity is bound only by `C_oracle_profile`, `C_reconstruct`, and any provider-side aggregate cap. The clause now explicitly disclaims that its own ledger can prevent a whole population of genuinely independent actors from collectively approximating an oracle. This is the correct closure of the through-line of the whole design and removes a latent overclaim.

**D3 — retention double-encoding. CLOSED.** Section 6.4 declares query profile and retention orthogonal axes; the `retained_summary` row is removed from the baseline profile table; a profile name MUST NOT pre-include retention.

**D4 — `cost(query_i)` ambiguity. CLOSED.** Section 6.7 defines `cost(query_i) ≡ risk_points × retention_multiplier × response_surface_multiplier` and forbids computing participant cost from base risk points alone.

**D5 — mixed-unit `min()`. CLOSED, thorough.** New Single-Unit Rule (6.2): all caps inside one `C_effective` share one declared unit; `min()` over mixed units is invalid; Formal and Operational modes are separate ledgers with no implicit conversion; if both are active, extraction is allowed only when every active ledger is within its own cap. Reinforced in 6.8 (cap-unit rule), 21.6 (conversion prohibited until a witnessed conversion profile exists), and witness packet fields.

**D6 — `C_license` adjudication. CLOSED.** Section 1.12 clarifies `C_license` is a declared metering input, not an adjudication of contract validity.

All six are closed. No closure is unsound.

---

## 3. Soundness note on the cap algebra

The per-class cap includes `C_oracle_profile` and `C_reconstruct`, and the outer `C_effective` min includes them again. This is not an error. `C_sybil_adjusted = Σ_g C_principal_g` can exceed `C_oracle_profile` when there are many principal classes; the outer min with `C_oracle_profile` catches this, so genuine multiplicity is bound by the oracle-profile cap in the outer min — which is exactly what 21.4 now states. The inner inclusion additionally provides a per-class enforcement bound (a single principal class cannot individually exceed the oracle profile or reconstruction cap). The two together are defense-in-depth, and the resulting `C_effective` is well-defined and conservative. Logged as observation N1, not a defect.

---

## 4. Reference and numbering integrity

After inserting the new 6.2 (Single-Unit Rule), the entire 6.x sequence and the top-level sequence were re-verified:

- top-level sections: `0 … 24` contiguous, no gap, no duplicate;
- 6.x subsections: `6.1 … 6.12` contiguous, no gap, no duplicate;
- internal cross-references (`§12`, `§5.6`, `§9`, `§10`, `§11`, `§6.5`, `§1.12`) all resolve to the correct sections;
- no stale reference to a pre-renumber section number.

Renumber breakage: none.

---

## 5. New advisory notes (non-blocking)

**N2 — unknown-independence policy (low).** For `independence unknown` and `review failed`, both 1.12 and 6.8.1 permit either "collapse into a single shared unresolved class" or "fail closed." Both options are safe, but the choice is left to the implementation, so two conformant systems may behave differently on the same unknown population. Recommendation: make this choice a declared oracle-profile parameter so the behavior is witnessable and comparable. Not a blocker; both branches are conservative.

**N4 — date field (trivial).** The header `Date` still reads 2026-06-25 while the revision is 0.2.1. Housekeeping only.

No other new defect was found.

---

## 6. Bridges and earth paragraph

Unchanged from v0.2 (19.1 explicit; 19.2 Ashby; 19.3 information theory; 20 blood bank + load-bearing repair shop). Previously verified as genuine and conforming. Requirement (≥1 explicit, ≥2 hidden, earth paragraph, cross-corpus) remains met.

---

## 7. Verdict

`PASS` at the b-layer review level.

All six prior defects are closed and sound; renumbering is clean; bridges and earth paragraph conform; the central thesis is unchanged and now free of the latent overclaim that v0.2 still carried (the populous-principal horizon is stated honestly). The only residuals are one low-severity interoperability recommendation (N2) and one trivial housekeeping nit (N4), neither of which is structural, unsound, or axiom-violating.

What this PASS means: in the reviewer's b-layer opinion, the clause is internally coherent, conformant, and ready to be carried to an independent checker and witness pass.

What this PASS does not mean: it is not a seal, not an integration act, and not memory. `record_sha256` is set only at integration. Sealing and conformance acceptance remain a separate step outside this advisory role.

---

## 8. Register handoff

| Target | What this review record hands forward | What it does not assert |
|---|---|---|
| Integration / witness pass | verdict `PASS`, SHA-256 binding, advisory notes N2 / N4 for optional polish | a sealed record (`record_sha256` stays placeholder) |
| Author (convergence line) | confirmation D1–D6 closed and sound; N2 / N4 as optional next-iteration polish | a rewrite; authorship remains upstream |
| A6 / Synthetic Laundering / EA Value / ARQ | confirmation BCEC still does not redefine them | any change to those layers |
| ARL / Conflict Class | none required | a dispute filing |

---

**Role note:** Advisory b-layer review record. No self-approval, no memory write, no integration authority. `PASS` is a reviewer opinion for an independent checker and witness pass, not an integration act. `record_sha256` is sealed only at integration.
