# Scientific Corrigenda and Regression Hardening v1.0 — signed acceptance

Date: 5 September 2026

This record accepts the already published, source-bound corrigendum bytes and their public routing. It is not a replacement release of either parent package, does not rewrite an old DOI deposit, and does not retroactively sign the source commits listed below.

## Pinned public source states

- AGI: `Kot141078/advanced-global-intelligence` commit `78bce9419de6006a21fdfd8fcf1aee35c383205c`.
- SER: `Kot141078/sovereign-entity-recursion` commit `5132db5c3119fe070182e9e975600304e60f7f4c`.
- Website: `Kot141078/kot141078.github.io` commit `1241ab39323083cdf48b558e3eae7b9a3c9ee113`.
- Website full-gate workflow change: `280cafad177f4646b948e9bab4f0a4e112b9991b`.

`git verify-commit` returned nonzero for each of the three correction source commits. Their history is intentionally left unchanged. The owner GPG signature on the commit containing this file is a new attestation of the checked states and bytes only. Verify that containing commit against fingerprint `48CEE0689BB905F009B9422C75D1828676B0D0EC`.

## Accepted artifact binding

- File: `hardening/SCIENTIFIC_CORRIGENDA_HARDENING_v1_0.zip`.
- Size: `2808783` bytes.
- SHA-256: `ca1e741f7d4f2dbf76a4a66fed7a5d83cf37e599e0fc4552bbca5aaa59b4ffde`.
- Archive inventory: 49 entries; all 48 rows of the internal `SHA256SUMS.txt` validated.
- The AGI archive and the website download were byte-identical.

## Checks observed for this acceptance

- Focused first-party regression suite: 29 of 29 passed.
- Existing website `tools/run_machine_readability_gate.py`: two complete consecutive local passes; each finished all 8 Python steps and 5 schema contracts.
- Generated-output idempotence: `git diff --exit-code` was clean after each complete gate invocation.
- Main machine-readability run `33991466324`: success, including `Reject stale generated files`.
- Main Pages run `33991465881`: success.
- Main live-verification run `33991466386`: success on its first attempt; receipt artifact `9976752753`.
- A separate read-only repetition returned HTTP 200 for all six governed URLs: the corrigendum page, MOT-c notice, CCALC notice, Origin-Neutral notice, `works-index.json`, and the ZIP. The live ZIP was `2808783` bytes with the accepted SHA-256 above.

## Claim ceiling and next action

Complete original Zenodo deposit archives were not acquired, and exact ARQ M2 DOI-deposit membership remains unresolved. No DOI is invented here. No new scientific experiment, identity/continuity result, Real Effect, Economic Value, runtime deployment, model run, private-memory access, or host change is claimed.

This acceptance advances Field Creation through preserved public chronology, Technical Reality through reproducible checks and exact byte binding, and Responsible Scale through bounded correction.

`NEXT=OWNER_ZENODO_UPLOAD`
