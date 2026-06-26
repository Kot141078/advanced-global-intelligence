# TSW Patch Notes v0.1.1

## Append-first correction for `05_Self_Evo_TRIAD_Sister_Witness_Profile_v0_1`

**Date:** 2026-06-24  
**Patch:** `TSW_PATCH_NOTES_v0_1_1`  
**Previous artifact:** `05_Self_Evo_TRIAD_Sister_Witness_Profile_v0_1.md`  
**Previous SHA-256:** `4abc63944ea1472ea99e87b836686ba11f442fb4cb122dfa128ebf2372761589`  
**New artifact:** `05_Self_Evo_TRIAD_Sister_Witness_Profile_v0_1_1.md`  
**New SHA-256:** `c2761d7a05a91681b336ce5402bdbea5c8fafc2ca0d04fdf2d9667ca02e595ed`  
**New line count:** `2145`  

## Review basis

This patch addresses `TSW_REVIEW_RECORD_v0_1`, which gave `PASS_WITH_LIMITS` and required two determinism fixes before any `TSW-C3` executable-checker claim:

- `TSW-REV-F1`: define deterministic derivation for `anti_echo_status`.
- `TSW-REV-F2`: define one canonical checker-result enum and a total precedence order.
- `TSW-REV-F3`: add Claim Strength Taxonomy pointers beside `claim_strength` fields.
- `TSW-REV-N1`: add local pointers to `SELF-EVO-01 §14.1.1` for `proposal_max_delta` uses.

## Changes

### TSW-REV-F1 closed

Added §14.4.1, a deterministic anti-echo floor:

```text
unknown -> hold
sender-declared pass may not override recomputed hold/fail/unknown
soft echo signals may tighten pass -> hold/fail or hold -> fail
soft echo signals may never loosen fail/hold/unknown -> pass
```

The floor maps the four packet booleans to `pass | hold | fail | unknown` and makes `compute_anti_echo_status(observations)` implementable.

### TSW-REV-F2 closed

Replaced the previous mixed result vocabulary with a canonical enum:

```text
QUARANTINE > FAIL > ARL > HUMAN_GATE > MEMORY_GATE > CGAM_REVIEW > DOWNGRADE > HOLD > WARNING > PASS_WITH_GATES > PASS
```

Updated `TSW-CHECK-001..025`, fixture results, and worked examples to emit one canonical result plus optional annotations.

### TSW-REV-F3 addressed

Added inline pointers to the Claim Strength Taxonomy / `REF-23` beside `claim_strength` and public claim-strength fields.

### TSW-REV-N1 addressed

Added inline pointers to `SELF-EVO-01 §14.1.1` where `proposal_max_delta >= 4` is used.

## Notes

This patch does not integrate or approve the profile. It produces an append-first corrected revision for re-review. The original artifact remains preserved by hash.
