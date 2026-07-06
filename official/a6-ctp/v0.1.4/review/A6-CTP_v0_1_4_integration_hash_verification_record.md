# Integration Hash Verification Record — A6-CTP v0.1.4

**Record class:** integration-side artifact verification  
**Record ID:** `A6CTP-HASH-VERIFY-20260706-v014`  
**Date:** 2026-07-06  
**Verifier:** assistant-side local file check  
**Authority:** none; verification record only  

---

## 1. Artifacts checked

- `A6_Composition_Transition_Predicate_Addendum_v0_1_4.md`
- `A6_Composition_Transition_Predicate_Addendum_v0_1_4_academic.pdf`
- `SHA256SUMS_A6_CTP_v0_1_4.txt`

## 2. Results

```text
61126c2d8a71a03eaa301f181168d02c1334ad0a3c5b68d778a6565707eb6152  A6_Composition_Transition_Predicate_Addendum_v0_1_4.md
b371dace3e74e59e32fa736f5ac3bf13d9665f9856c1e7c5c30e9190955d4c89  A6_Composition_Transition_Predicate_Addendum_v0_1_4_academic.pdf
```

`sha256sum -c SHA256SUMS_A6_CTP_v0_1_4.txt` was run from the artifact directory
and returned OK for both files.

## 3. Boundary note

This record verifies local artifact bytes in the integration environment. It
does not change the b-layer review record's statement that the PDF was
unverified in the separate reviewer session. The two statements are compatible:

```text
b-review session: PDF unavailable -> PDF hash unverified there.
integration session: PDF available -> PDF hash verified here.
```

## 4. Disposition

The package-level Markdown and PDF hashes are verified in this environment.
Use relative-path sumfiles for portable `sha256sum -c` checks.
