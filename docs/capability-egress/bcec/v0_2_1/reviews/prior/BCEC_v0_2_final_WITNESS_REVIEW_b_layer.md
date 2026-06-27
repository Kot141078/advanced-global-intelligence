# BCEC v0.2-final — Witness-Compatible Review Record (b-layer)
## Independent conformance review and convergence record for the Bounded Capability Extraction Clause

**Status:** Advisory review record / b-layer checker output / not an approval
**Record type:** witness-compatible review record + append-first convergence record
**Reviewer role:** b-layer checker (advisory only — no self-approval, no memory write, no integration authority)
**Date:** 2026-06-25
**Language:** English. Package format. RFC 2119 keywords used in the ordinary protocol sense where they appear in recommendations.

**Reviewed artifact:** `Bounded_Capability_Extraction_Clause_v0.2-final.md`
**Artifact SHA-256:** `a289dadf7440eef4ed65127eb7b6ec31bd857cb5965cbff1a23cb76eb6d3277a`
**Prior version on this convergence line:** `Bounded_Capability_Extraction_Clause_v0.1.md` (b-layer skeleton, authored upstream)

**Verdict:** `PASS_WITH_LIMITS`
**Record seal:** `record_sha256: PLACEHOLDER_SEALED_AT_INTEGRATION`

---

## Machine-readable record

```yaml
review_record:
  schema: cgam-b-layer-review-0.1
  reviewed_artifact:
    name: Bounded_Capability_Extraction_Clause_v0.2-final.md
    sha256: a289dadf7440eef4ed65127eb7b6ec31bd857cb5965cbff1a23cb76eb6d3277a
    declared_version: 0.2-final
    declared_status: final textual clause / normative draft ready for checker and witness pass
  reviewer:
    role: b_layer_checker
    authority: advisory_only
    self_approval: false
    memory_write: false
    integration_authority: false
  verdict:
    value: PASS_WITH_LIMITS
    blocker_defects: 0
    structural_defects: 0
    refinement_defects: 6
    rationale: >
      Internally coherent and conformant on all checked CGAM axioms. Bridges and earth
      paragraph present and genuine. Central v0.1 defect (summation vacuity) is correctly
      identified and corrected. Remaining defects are refinements at the level of cap
      derivation, unit commensurability, and limits-section completeness, not structural
      failures. A clean PASS is withheld because one load-bearing cap term
      (C_sybil_adjusted) is invoked in the central correction but not derived, and the
      min() in 6.7 may compare incommensurable units.
  conformance_checks:
    anti_echo_discipline: present            # 13
    slot_a_b_with_auto_rollback: present     # 14
    witness_compatible_packet: present       # 11
    record_sha256_placeholder: present       # 11, header
    fail_closed_posture: present             # throughout
    hard_separation_no_redefinition: present # 4, 22
    explicit_non_claims: present             # 2.3, 6.11, 21
    quarantine_on_breach: present            # 10, 12
  bridge_verification:
    explicit_bridges: 1                      # 19.1
    hidden_bridges: 2                        # 19.2 Ashby, 19.3 information theory
    earth_paragraph: present                 # 20 (blood bank = physiology; repair shop = engineering)
    cross_corpus: true                       # cybernetics x information theory x own-stack layers
    requirement: ">=1 explicit, >=2 hidden, earth paragraph"
    requirement_met: true
  convergence:
    direction: v0.1 -> v0.2-final
    mode: append_first
    central_correction_accepted: true
    correction_summary: >
      Summation bounds extraction only after budget issuance is itself bounded;
      cap reframed from naive participant sum to C_effective = min(participant_sum,
      oracle_profile, license, reconstruct, sybil_adjusted); extraction principal
      introduced to defeat account splitting.
  defects:
    - id: D1
      severity: moderate
      locus: [1.12, 6.7]
      title: C_sybil_adjusted lacks an explicit derivation rule
    - id: D2
      severity: moderate
      locus: [6.10, 21.4]
      title: principal-grounding re-imports the coalition problem; genuinely-independent populous adversary unbounded by principal accounting
    - id: D3
      severity: low_moderate
      locus: [6.3, 6.4]
      title: retention double-encoded as both a query profile and a multiplier
    - id: D4
      severity: low
      locus: [6.4, 6.6]
      title: cost(query_i) not explicitly equated to the multiplied expression
    - id: D5
      severity: low_moderate
      locus: [6.1, 6.3, 6.7]
      title: Formal-mode bits and Operational-mode risk points may be compared in min() across incommensurable units
    - id: D6
      severity: very_low
      locus: [2.2, 6.7, 11]
      title: C_license / terms refs sit close to disclaimed ToS adjudication
  limits_to_seal_at_integration:
    - resolve D1 derivation before C_effective is treated as enforceable
    - state D5 single-unit rule before min() is implemented
    - record D2 populous-adversary limit explicitly in 21
  record_sha256: PLACEHOLDER_SEALED_AT_INTEGRATION
```

---

## 1. Scope of this review

This record is an independent b-layer conformance pass over BCEC v0.2-final. It reads the full document, maps section headers, verifies bridges and earth paragraph, checks conformance against the CGAM axioms the corpus enforces (anti-echo, Slot A/B with auto-rollback, hard separation, explicit non-claims, fail-closed, witness compatibility), records the v0.1 to v0.2 convergence (append-first), and lists independent defects with severity and recommendation.

It does not seal, approve, integrate, or write to memory. `record_sha256` remains a placeholder for a separate integration / witness pass.

---

## 2. Convergence record (append-first, v0.1 to v0.2-final)

The v0.1 skeleton stated, as its central quantitative claim, that per-participant summation bounds a coalition "even under perfect coordination." That claim was true only as a bound of consumed budget against issued budget, and was silently conditional on bounded budget issuance. Against a populous adversary able to mint many legitimately-budgeted participants, the participant sum is unbounded and the cap is vacuous.

v0.2-final corrects this and the correction is accepted:

- **Extraction principal** (1.5): budgets attach to the real controlling party, not to visible accounts; numerically distinct accounts are not automatically independent.
- **C_effective = min(...)** (1.12, 6.7): the enforceable cap is the minimum of participant sum, oracle-profile cap, license cap, reconstruction cap, and Sybil-adjusted cap. A large participant sum no longer raises the ceiling.
- **Explicit critical correction** stated in 0, 6.7, and 6.10: counting every participant prevents hidden overrun; it does not by itself prevent lawful-looking mass reconstruction.

Additional convergence improvements judged sound:

- **Dual-mode budget** (6.1 formal information bound + 6.3 operational risk points): answers the v0.1 open item that `b_extract,max` is hard to calibrate, by providing a conservative computable proxy.
- **Retention and response-surface multipliers** (6.4, 6.5), **warning zones** (6.8).
- **`EXTRACT_RESIDUE_UNLAWFUL` renamed to `EXTRACT_RESIDUE_NONCONFORMANT`** (5.6): removes a legal claim the clause is not entitled to make; consistent with corpus anti-overclaim discipline.
- **Operational implementation sketch** (15) grounding the clause in the actual local architecture (local LLM substrate vs cloud Judge as external oracle; vector-store and P2P provenance tagging).

Convergence verdict: genuine refinement, not cosmetic restatement. Passes the corpus anti-echo proof-revision rule (a revision is not accepted merely for restating boundedness in fancier words; this revision changes the claim).

---

## 3. Conformance verification (CGAM axioms)

| Axiom / requirement | Location | Result |
|---|---|---|
| Anti-echo discipline | 13 | present; covers budget-as-proof, qualitative/quantitative substitution, BCEC→Judge→BCEC circularity |
| Slot A / Slot B + auto-rollback | 14 | present; invalid over-reads enumerated ("metered therefore clean", etc.) |
| Hard separation (no redefinition of parent layers) | 4, 22 | present; Beacon, ARL, AGL, Witness, EA, Synthetic, A6 each preserved |
| Explicit non-claims | 2.3, 6.11, 21 | present and specific |
| Fail-closed posture | 1.2, 6.7, 6.8, 7, 10 | present; unmetered path, unknown cap, missing witness all fail closed |
| Witness compatibility + unsealed record | 11 | present; packet carries principal mapping, all caps, source-class, side-channel status |
| Quarantine on breach / re-admission mismatch | 10, 12 | present |

No axiom violation found.

---

## 4. Bridge and earth-paragraph verification

- **Explicit bridge** (19.1): A6 / Synthetic Laundering / EA Value / ARQ, with an operational chain. Genuine.
- **Hidden bridge #1** (19.2): Ashby / requisite variety, in the refined form — regulation is relocated to the controlled boundary to *avoid* a variety race rather than enter one. Genuine, load-bearing, not decorative.
- **Hidden bridge #2** (19.3): information theory / channel discipline — chain-rule bound on `I(F; responses)` and the two-channel (quantitative vs qualitative) separation. Genuine.
- **Earth paragraph** (20): blood bank (physiology / consent / contamination) plus load-bearing repair shop (engineering / refurbished-part-not-factory-new). Satisfies the anatomy/engineering grounding requirement.

Requirement (≥1 explicit, ≥2 hidden, earth paragraph, cross-corpus): **met.**

---

## 5. Independent defects

### D1 — `C_sybil_adjusted` lacks an explicit derivation rule (moderate)
**Locus:** 1.12, 6.7. Every other term in the 6.7 min() has an explicit source: `C_participant_sum = Σ budget_p` (6.6), `C_reconstruct = T_reconstruct(profile)` (6.9), `C_oracle_profile` and `C_license` supplied by profile/authorization. `C_sybil_adjusted` is named but never derived. The mechanism exists in prose (1.5: ground principals; else collapse to a shared budget or fail closed; reinforced by 7 R2), but no rule computes the numeric cap from principal review. This is the load-bearing anti-Sybil term and is currently a placeholder name — the v0.2 analog of the v0.1 `b_extract,max` gap.
**Recommendation:** add a derivation, e.g. `C_sybil_adjusted = Σ over review-passed independent principals of their principal caps; participants with failed or unknown principal review collapse into a single shared principal budget; if collapse is impossible, fail closed.`

### D2 — Principal-grounding re-imports the coalition problem; populous-adversary limit not stated (moderate)
**Locus:** 6.10, 21.4. Section 6.10 asserts BCEC "does not need to detect every coalition." But `C_sybil_adjusted` depends on deciding whether N accounts are one principal or N — which is the coalition-grounding problem under another name. Two honest consequences are unstated: (a) when independence cannot be grounded, the clause fails closed, which can over-throttle a legitimately diverse federation (false-positive cost); (b) when an adversary's principals are *genuinely* independent — a populous actor fielding many real distinct anchors — principal review passes, `C_sybil_adjusted` equals the full sum, and principal accounting provides no bound. In that case only `C_oracle_profile` and `C_reconstruct` bind, and both are oracle-operator-set (the external horizon). The populous-adversary case is therefore, by design, deferred to the oracle's own aggregate cap and is not solved on the conformant side.
**Recommendation:** state this explicitly in 21 — principal accounting bounds *concealed* multiplicity, not *genuine* multiplicity; against genuine multiplicity only oracle-side aggregate caps apply, which is the external-horizon limit already named in 21.4.

### D3 — Retention double-encoded as profile and multiplier (low-moderate)
**Locus:** 6.3, 6.4. The 6.3 profile table contains `retained_summary` (8 points) while 6.4 encodes retention as a multiplier (`EA` 2×, etc.). A retained summary can be scored two inconsistent ways. The retention semantic lives on both the profile axis and the multiplier axis.
**Recommendation:** make the axes orthogonal — profiles describe query type, multipliers describe retention/surface — and either remove retention-named profile rows or state that `retained_summary` already includes retention and MUST NOT be multiplied again.

### D4 — `cost(query_i)` not equated to the multiplied expression (low)
**Locus:** 6.4, 6.6. 6.4 gives `B_consumed = Σ risk_points × retention_mult × surface_mult`; 6.6 gives `B_p_consumed = Σ cost(query_i)` without stating that `cost(query_i)` is that product. An implementer could compute participant cost without multipliers.
**Recommendation:** state `cost(query_i) ≡ risk_points(query_i) × retention_multiplier_i × response_surface_multiplier_i`.

### D5 — min() may compare incommensurable units (low-moderate)
**Locus:** 6.1, 6.3, 6.7. Formal mode is in declared information bits; operational mode is in risk points. If caps within one `C_effective` are expressed in different units, the 6.7 min() is unsound. The witness packet's `budget_model.unit` is a single enum per record (good), but the clause does not forbid mixing modes within one composition's cap computation.
**Recommendation:** add a rule that all caps in a single `C_effective` MUST share one unit, and Formal and Operational modes MUST NOT be mixed within one composition.

### D6 — `C_license` / terms refs sit close to disclaimed ToS adjudication (very low)
**Locus:** 2.2, 6.7, 11. 2.2 disclaims ToS enforcement, yet 6.7 includes `C_license` "under authorization, license, contract, or terms profile" and the packet records `license_ref` / `oracle_terms_ref` / `tos_bound`. Recording is not enforcing, so this is consistent, but the line is thin.
**Recommendation:** one clarifying line that `C_license` is a *declared* ceiling supplied by the operator, not an adjudication of contract validity.

---

## 6. Verdict

`PASS_WITH_LIMITS`.

The clause is internally coherent, conformant on every checked CGAM axiom, with genuine bridges and a conforming earth paragraph, and it correctly fixes the central defect of its predecessor. A clean `PASS` is withheld for two reasons that touch enforceability rather than structure: D1 (the load-bearing `C_sybil_adjusted` is invoked in the central correction but not derived) and D5 (the min() may compare incommensurable units). D2 is an honesty-completeness gap in the limits section. D3, D4, D6 are operational-consistency refinements.

None of the six is a blocker. All are sealable at integration. The document is suitable to carry forward to an independent checker and witness pass once D1 and D5 are resolved and D2 is recorded.

---

## 7. Register handoff

| Target | What this review record hands forward | What it does not assert |
|---|---|---|
| Integration / witness pass | verdict `PASS_WITH_LIMITS`, SHA-256 binding, the three limits to seal | a sealed record (`record_sha256` stays placeholder) |
| Author (convergence line) | D1–D6 with recommendations; append-first convergence acceptance of the central correction | a rewrite; authorship remains upstream |
| A6 / Synthetic Laundering / EA Value / ARQ | confirmation that BCEC does not redefine them | any change to those layers |
| ARL / Conflict Class | none required (no contested standing raised by this review) | a dispute filing |

---

**Role note:** Advisory b-layer review record. No self-approval, no memory write, no integration authority. The verdict is a reviewer opinion for an independent checker and witness pass, not an integration act. `record_sha256` is sealed only at integration.
