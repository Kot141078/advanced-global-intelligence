# CGDR R1.6AN: current-AK source disclosure v0.1

Ivan Kotov · 12 September 2026 · Research/evaluation source-available package.

## What is now public

All **93 files of the accepted current-AK source tree**, unchanged byte for
byte, plus the **three selected-profile files**, the original **evidence note
v0.1**, per-file attribution, external-dependency license declarations, the
applicable upstream notices and an explicit research/verification permission.
This is a source publication, not merely the earlier seven-file evidence note.
The source-only publication scope and license/notice preparation are completed
for this named package. No universal ownership or legal-compliance certificate
is claimed.

`code/` has 36 Python files as well as documents, schemas, fixtures and locks;
93 is a file-tree count, not a Python-module count. No source file is changed
or upgraded for publication. The original source manifest is preserved:
SHA-256 `2c4c37d65763f08b7df2381c43400b036f4a358a65db96661c67170e3c234c49`.

## Permissions

Read LICENSE.md and SOURCE_LICENCE_INDEX.json. Independent examination,
research execution, necessary verification/portability modifications and
publication of positive or negative findings are permitted without further
approval for the covered rights. Commercial operational use of new CGDR code
is reserved for a separate agreement. Existing CC BY 4.0 rights in the CGAM
and SER documents are **not** narrowed. The c-hardening-pack's previous rights
remain intact alongside the additional research permission. This is not MIT,
Apache or OSI-approved open-source licensing of the entire package.

## Verify without running the research system

Extract this archive into a new directory. With Python 3.10+:

```sh
python -B verify_source_release.py
python -B -m unittest -v test_source_release.py
cd evidence-note-v0.1
python -B verify.py
python -B -m unittest -v test_verify.py
```

These are publication/checker tests, **not CGDR runtime tests**. They do not
import `code/`, call its entry points, start WSL/workers or replay the matrix.
The source checker verifies the complete public inventory, all 93 accepted
source hashes, all 96 source/profile attribution rows, the 12 external
package entries and the required notice files. Hashes establish byte identity,
not historical event truth or legal title. Compare the outer ZIP SHA-256 with
the independently published value before relying on its internal manifest.

## Result being disclosed

The unchanged implementation's original exact selected-process matrix was
internally accepted on 11 September 2026: 18/18 episodes, 21/21 profile
checkpoints, three expected synthetic effects and zero promotions. The
accompanying evidence note preserves 7 raw-observer PASS, 11 FAIL and 3
INCONCLUSIVE results, and all 756 original observer assertion values. The
fault-test profile verdict is distinct from these raw diagnostics. No failure
has been relabeled to prepare this release.

The accepted historical experiment is not repeated here. AG/AH/AJ historical
outcomes remain unchanged. See the evidence note for limits, historical
internal labels, expected injected faults and result-schema scope.

## Source completeness versus experiment completeness

This archive is the complete **accepted current-AK tree**, not the complete
private AN execution/custody archive. It excludes private raw logs, account and
session metadata, keys, one-shot execution bindings, original launch controls,
the run-specific AN driver/preflight and control evidence. The frozen upstream
`code/REPRODUCE.md` describes an earlier offline calibration step; it is not
silently promoted to an end-to-end AN replication guide. The driver logic
inside `code/` can be studied, but this release does not claim a ready-to-run
independent 18/21 experiment with all authorization inputs already supplied.

Independent researchers may build a separately recorded experiment on their
authorized equipment under the research permission. Use fresh identifiers,
new output directories and reviewed local inputs. Never resume the historical
AN attempt, count a new run as that attempt, import private credentials or
claim changed code is the accepted unchanged source. No new experiment was
performed for this publication; independent clean-host replication remains
outstanding.

## Privacy and packaging decisions

The code/profile files contain no Drive/Docs locators, email addresses, private
key blocks or non-placeholder credential assignment found by the recorded
static scan. Six historical canary path literals in one test file include
`Users/kotov`; these source-code test strings are explicitly retained, not
presented as current account, credential or host-state evidence. The source
also contains generic isolation paths. No live user files or their contents
are included. This bounded scan is not a universal secret-detection guarantee.

The 18 local scenario fixtures beneath the pinned hardening-directory name
are marked as CGDR overlays in the source index; the path does not falsely
claim those fixtures exist at the upstream commit. Native Python packages,
wheels, virtual environments, system binaries and private runtime outputs
are excluded. The twelve license entries concern external installation
dependencies, not redistributed binaries or a current security certification.

## Engineering and research boundaries

The unchanged controller source, the bench test record and the permission to
reuse the drawing are three different things. This release supplies the source
and applicable paperwork; it does not turn a passed synthetic bench test into
permission for a production installation. Source custody and licensing do not
establish runtime authority. Likewise, publication makes an existing technical
result inspectable without becoming independent replication or a measured
real-world effect.

No identity continuity, same c, consciousness, lawful succession, B5 superiority,
c-specific real effect, economic value, general-stack conformance or live
readiness is established. Five Proofs contribution: inspectable Technical
Reality and responsible distribution; no new experimental or economic credit.

Canonical work page: https://ivankotov.eu/publications/cgdr-selected-process-r1-6an/
Public corpus home: https://github.com/Kot141078/advanced-global-intelligence/tree/main/publications/cgdr-selected-process-r1-6an
Historical evidence-note commit: 76f16004ebe2c2583d56db465f7a5ec044645446.
No DOI or formal GitHub Release is asserted by this source archive alone.
