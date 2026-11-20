# Offline maintenance and reproducibility

This sibling package records Corrigendum 01 for Continuity Instrument v1.0.0. Its maintenance tools reproduce the reviewed correction specification, corrected text copies, comparison diffs, and the EN corrigendum. They do not run a CI evaluator, qualify a corpus, publish a record, or deploy a site.

The new maintenance tools and template are copyright © 2026 Ivan Kotov, All rights reserved. Frozen source artifacts retain the rights under which their respective versions were issued. The sibling package does not replace their license notices or the original v1.0.0 mirror.

## Required environment and inputs

Use Python 3.9 or later; only the standard library is required. Git is optional for the historical regression harness's two patch-applicability checks. The package includes both build scripts, their EN template, the 17 frozen predecessor files, and all reviewed corrected copies. No network access is needed for the package validation below.

The reviewed correction specification remains byte-identical:

`patches/corrections.json`

SHA-256: `9ac75661c364d139c8f4c2f3656a285d63fa89d6e34aac6786b4d72ad6e065dd`.

It contains 25 edits in 17 files. Its historical machine category `token` covers 16 name/reference edits: 10 literal name substitutions and 6 edits that also add a reference, adapter wording, or a correction notice. The other 9 edits remove or repair claims arising from the misspelling. The spec's original date and status strings remain part of the reviewed evidence; current publication status is recorded separately in this package.

The frozen source bindings refer to:

- `Kot141078/advanced-global-intelligence` at `bb062414b598afae970bef37ce7489433a51868d`.
- `Kot141078/kot141078.github.io` at `f77956b4dc45583d4b271c0f4499f0bbdab41e16`.

## Validate an assembled sibling package

Run from the package directory:

```bash
python3 -B tools/validate_package.py
```

The validator checks the pinned spec identity, every file listed in `SHA256SUMS.txt`, and complete checksum coverage of the package. It then regenerates the spec, the EN corrigendum, all 17 corrected text copies, both comparison diffs, and `evidence/APPLY_REPORT.json` into temporary storage outside the package. It requires byte equality with the packaged outputs and rechecks the frozen input hashes. It removes temporary files after the check and writes its result to standard output.

Keep validation logs outside the package being checked. A final package must have a complete `SHA256SUMS.txt` covering every file except that checksum file itself. If package content changes, regenerate that checksum list and validate the completed package again. Checksum consistency is an integrity check; it does not grant rights, publication permission, or scientific acceptance.

## Regenerate individual outputs

Use a new output path outside the package's frozen source roots:

```bash
python3 -B build/build_spec.py \
  source_snapshots/advanced-global-intelligence \
  source_snapshots/kot141078.github.io \
  /tmp/ci-corrigendum-spec.json

python3 -B build/render_corrigendum.py \
  build/CORRIGENDUM_EN.template.md \
  patches/corrections.json \
  /tmp/ci-corrigendum-en.md

python3 -B tools/apply_corrections.py \
  --agi-root source_snapshots/advanced-global-intelligence \
  --site-root source_snapshots/kot141078.github.io \
  --output /tmp/ci-corrigendum-corrected
```

All three commands refuse to overwrite an existing output. The spec builder also refuses output inside either frozen input root and refuses any generated spec whose SHA-256 differs from the reviewed pin. The renderer requires that same spec identity and exactly one table marker in its template. The correction tool checks each predecessor's bytes, each exact replacement count, and every corrected hash before writing new copies.

The EN renderer generates the 17-file correction table. The surrounding text, including the preservation table for five PDFs and two archives, is maintained in the template. It does not introduce a new DOI or infer a publication date.

## Historical regression record

The independent review observed `74 PASS / 0 FAIL / 2 SKIP` from the original regression suite on the frozen snapshot directories. The two skipped checks were subsequently run separately, read-only, on actual checkouts at the two pinned commits, and both succeeded. This remains **74 suite checks plus 2 separate pinned-checkout checks**; it is not retrospectively relabeled as one `76/0/0` run.

The retained maintenance harness can be invoked explicitly when a changed tool requires checking:

```bash
python3 -B tools/test_regressions.py \
  --agi-root source_snapshots/advanced-global-intelligence \
  --site-root source_snapshots/kot141078.github.io
```

Its string-based semantic check verifies only the presence of a DOI or adapter wording. Independent textual review remains necessary to assess meaning and claim scope. Regenerating the author's fixed replacement choices does not independently establish their scientific correctness.

## Comparison diffs and preservation

`patches/advanced-global-intelligence.diff` and `patches/kot141078.github.io.diff` are reproducible comparison evidence against the pinned predecessors. **Do not apply the AGI diff to the immutable v1.0.0 mirror.** The nested `corrected_text` paths are proposed corrected copies kept within this sibling package; they are not a replacement mirror.

The site diff preserves the original dated proposal. A later site update must use a current reviewed patch, the actual publication date, and the eventual corrigendum link. Successful `git apply --check` only establishes applicability to its pinned predecessor; it does not authorize deployment or establish compatibility with Beacon.
