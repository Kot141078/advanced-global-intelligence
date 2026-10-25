# Reproducibility

## Reproduction boundary

This package supports reproduction of the specified CI v1 transformation and byte-level verification of its public release files. It also provides exact locators and pins for three external evidence objects. It does not redistribute private corpus bytes, model files, runtime binaries, or the frozen evidence archives.

Reproducing a procedure is distinct from validating a scientific conclusion. No reproduction step raises the claim ceiling without admissible evidence and independent review.

## Reference transformation

`REFERENCE_IMPLEMENTATION/ci_profile.py` identifies itself as `ci-profile-reference/1.0.0`. It requires Python 3.10 or later and imports only Python standard-library modules. The versioned structural contracts are:

- `REFERENCE_IMPLEMENTATION/schemas/ci-profile-input-v1.schema.json`
- `REFERENCE_IMPLEMENTATION/schemas/ci-profile-output-v1.schema.json`

From the package root:

```text
python REFERENCE_IMPLEMENTATION/ci_profile.py INPUT.json --output OUTPUT.json
python -m unittest discover -s tests -p "test_*.py" -v
```

The transformation reads no clock, environment variable, network, model, or frozen evidence directory. It uses caller-declared integer ticks and closed-open intervals, unions admitted eligible participation without double-counting, computes gaps inside the declared observation window, sorts event and lineage records deterministically, preserves structured uncertainty, and emits canonical UTF-8 JSON. The vector checksum is SHA-256 over canonical JSON bytes without a trailing line feed.

The implementation rejects duplicate JSON keys, invalid or out-of-window bounds, duplicate local identifiers, duration eligibility on non-admitted intervals, overlap between eligible participation and known pauses, and omission of mandatory prohibited inferences. Passing the focused tests establishes only the tested transformation behavior.

## External evidence objects

Always retrieve by exact ID and verify the complete bytes before interpretation.

| Episode | Drive URL | Bytes | SHA-256 | Bound result |
|---|---|---:|---|---|
| R157 | https://drive.google.com/file/d/16Koyf3ckIkKjSni5C8C97L9c4DiuhIdE/view | 3703123 | `fc8564656fb777b1266d763bea841af0dd5f13b03e2f727db6f3ec3689270c8a` | `OD11_TQ_R157_PASS_OPEN_SYNTHETIC_SEMANTIC_GATE_FIDELITY` |
| R160 | https://drive.google.com/file/d/1JmLtDLkL4aQhTSIFprGjsd-xZDN2XRqC/view | 251185 | `8b80604a62aa7d5232bf9659b87009537951a3f3b89151bc8164b88d4387952b` | `REAL_LOCAL_OLLAMA_CORPUS_QUALIFICATION_NOT_ESTABLISHED` |
| R161 | https://drive.google.com/file/d/1m11yDfvrhbIQ0Zlp-amxKiMixzNgWv76/view | 191074 | `56c586b665b83c3485c19c3186ed989b17cd03fbf21555d7642f1316bb48002f` | `REAL_LOCAL_OLLAMA_QWEN25_CORPUS_QUALIFICATION_NOT_ESTABLISHED` |

R157 is an immutable open-synthetic predecessor. This package does not rerun or repackage its producer, gate, Run1, or Run2. R160 and R161 are consumed negative attempts. They are not corrected, rescored under new rules, or relabeled as PASS.

## R160 frozen environment summary

The R160 negative evidence binds, among other details:

| Component | Pin |
|---|---|
| Attempt key | `CI_OD11_TQ_R160_REAL_LOCAL_OLLAMA_CORPUS_ATTEMPT_20261025_01` |
| Ollama client | `0.21.2` |
| `ollama.exe` SHA-256 | `4a5eae4cce39073d96f4ec34af8f47a3e9bc76f68c083d4fe5f8f315f1bf07c4` |
| Runtime aggregate SHA-256 | `ee6551e834b4d283ac92cc3f07563776d96f3f7fd96f87b4c7d98afb8161f272` |
| Model | `qwen3-vl:32b` |
| Model manifest SHA-256 | `ff2e46876908853b8d0872595047c46d599d970056277e4864c8a1f0fd93fd3b` |
| Python executable SHA-256 | `3cce33d75d6fdae4e004d0bdf149320b3147482a9caf370079dcb9c191a1b260` |
| Episode | one service start, five requests, retries `0` |

The independent R160 custody review found the 251,185-byte Drive object intact and confirmed the preserved negative result. The scorer read the frozen outer `response` field, which was empty for all five records; it did not substitute the model's separate `thinking` field after capture.

## R161 result summary

R161 used a separately frozen local `qwen2.5:32b` episode over five immutable Git-blob records. It completed all five requests with retries `0`. The independently recomputed frozen metrics were:

- schema valid: `5/5`;
- claim boundary exact: `5/5`;
- role exact: `4/5`;
- class exact: `3/5`;
- evidence exact: `0/5`;
- records satisfying every predicate: `0/5`.

The all-or-nothing threshold therefore failed. Independent custody review returned `CONFIRMED_CONSUMED_NEGATIVE_RETURN`: exact Drive identity and readback matched `191074` bytes and the recorded SHA-256; ZIP CRC and all `62/62` manifest member pins passed within the `63`-member archive. Partial metric success is diagnostic evidence rather than qualification.

## Corpus privacy and rights boundary

The external evidence uses owner-controlled corpus material pinned to immutable repository objects. This public package includes repository identifiers and integrity metadata only. It contains no holdout prompt, raw response, Qubit narrative, excerpt, translation, or derivative corpus text. Qubit material remains All Rights Reserved.

## Release verification

`PUBLICATION_MANIFEST.json` pins every release payload member except the manifest and checksum index themselves. `SHA256SUMS.txt` additionally pins the manifest. The deterministic ZIP uses:

- ordinal path ordering;
- UTF-8 forward-slash member names;
- timestamp `1980-01-01 00:00:00`;
- DEFLATE compression;
- regular-file mode `100644`.

A verifier should:

1. verify the ZIP SHA-256 supplied with the release;
2. read every member to check CRC;
3. reject duplicate, absolute, parent-traversal, or symlink entries;
4. verify the exact manifest member set, byte lengths, and SHA-256 values;
5. run the focused reference-implementation tests; and
6. preserve the claim ceiling in `SCIENTIFIC_CLAIM_MAP.md`.

## DOI readiness boundary

The scientific text and metadata are explicitly CC BY 4.0. The reference implementation, schemas, and tests use the exact custom rights statement `Copyright © 2026 Ivan Kotov. All rights reserved. No license grant.` The Zenodo UI must record both rights entries with their stated scopes. A DOI is not assigned until the deposit is published and its bytes are verified.
