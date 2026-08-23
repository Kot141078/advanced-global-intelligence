# TAP R2B Exact Binding Closure Report

## A. Executive result

`TAP_R2B_BINDING_CLOSURE_PASS_WITH_EXPLICIT_EXTERNAL_GAPS_AWAITING_OWNER_REVIEW`

Repository-owned T03, T06, and T07 surfaces have zero `UNRESOLVED` rows under the R2B discovery model. T07 has zero `HIDDEN` rows. T03 retains 78 explicit `DEPLOYMENT_EXTERNAL` rows; those rows are not treated as TAP verification, so T03 remains `LOCAL_PARTIAL_CANDIDATE`.

No live network call, publication, push, release, deployment, website edit, DOI action, or DNS/OVH action occurred.

## B. Frozen custody

| Surface | Required state | Result |
|---|---|---|
| R2A branch | `8fd36a38e97f240a934ea095551f8a2323c1547b` | PASS |
| R2A bundle | `2fec5171ba951f63c73a6dba5b18f68267c164ce9aa176c8802c2af29699fdf5` | PASS, verified |
| R1 branch | `e6e59643727fa9ce9c80d550a44297165d6ee938` | PASS, clean |
| R1 bundle | `8a2e9c0d5e97f3de31515be5a19e6fe66e4cd91c45def0a1355b553559b20d70` | PASS, verified |
| R1 normative JSON | `9878b98074076ef2a56b5f8d07e07c25128e97f186fab5ad848ed65dcdc43da6` | PASS |
| R1 normative schema | `84b0ec3db856d5752e3205a6f70098ecd32ef5542210c2866d5e903bf1ff0e52` | PASS |
| R1 evidence baseline | `5691a22629b5e8787afb11b6c7cad43facae23f89c6661aecbb8e1f33ff466ac` | PASS |
| R0.5 reconciliation | `c0804783a814fdaf643aa4727f2ca707a09cb6ad` | PASS, clean and ignored-clean |
| Original Ester | `main@d1dbd54ba63154698074c13f9742d84c6e327bc8` | PASS, 5 modified, 0 staged, 55 untracked, 60/60 hashes |

## C. Branch ancestry

`origin/main..R2A_HEAD` contains six explained commits: two `INHERITED_BASELINE` commits (`0b978d4`, `c080478`) and four R2A commits (`4ff7cba`, `90f0271`, `8ad25ec`, `8fd36a3`). `UNKNOWN_COMMITS=0`. The merge base is `54cd0c8754587f5e9daf82b16eb84c66a7ac94ef`.

Final topology is branch `tap-r2b-binding-closure-20260823`, HEAD `a668e0501dd9b975fa5e455da781611f9534e509`, ahead 10 and behind 0 relative to `origin/main`.

## D. R2B implementation

R2B adds a separate static binding layer. It does not modify the R2A discovery API. The layer discovers background activation constructs, classifies the stricter network inventory, records cloud authority boundaries, and resolves the R2A agent/executor lifecycle rows. Direct broker routes to known cloud-AI hosts now fail before network and require the existing approved oracle route. The chat API rejects non-loopback model endpoints.

Changed paths: 18. Source/test/config changes are confined to the local R2B branch.

## E. TAP-T03 background/runtime inventory

Discovered: 132.

| Classification | Count |
|---|---:|
| `DEPLOYMENT_EXTERNAL` | 78 |
| `DISABLED_BY_DEFAULT` | 49 |
| `TEST_ONLY` | 3 |
| `LEGACY_INACTIVE` | 2 |
| `UNRESOLVED` | 0 |

The 78 external deployment rows identify service/entry-point activation whose live state cannot be proved from repository bytes. They remain an explicit external gap and are not counted as local TAP verification.

## F. TAP-T06 network/cloud inventory

R2A discovered 179 lexical sites. R2B discovered 177 network primitives. The two removed rows were proven false positives: Flask `test_client.get` and Python `dict.get`. The delta is explicit in `TAP_R2B_T06_DISCOVERY_DELTA.json`.

| Route class | Count |
|---|---:|
| `LOCAL_SERVICE` | 128 |
| `NON_AI_EXTERNAL_NETWORK` | 26 |
| `LOCAL_LOOPBACK_MODEL` | 5 |
| `LEGACY_INACTIVE` | 3 |
| `OTHER_EXPLICIT` | 3 |
| `CLOUD_AI_ORACLE` | 1 |
| `UPDATE_OR_METADATA` | 11 |

Classification totals: `BOUND=4`, `OUT_OF_SCOPE_WITH_REASON=173`, `UNRESOLVED=0`.

The semantic authority map contains three cloud-AI routes: one bound OpenAI oracle route and two explicitly disabled legacy broker routes. All 3/3 include approval/window, minimization, retention, budget, deny, fail-closed, log/witness, and caller identity fields. No live network request was made.

## G. TAP-T07 agent/executor inventory

Discovered: 14.

| Classification | Count |
|---|---:|
| `INVENTORIED` | 8 |
| `DISABLED_BY_DEFAULT` | 4 |
| `LEGACY_INACTIVE` | 1 |
| `OUT_OF_SCOPE_WITH_REASON` | 1 |
| `HIDDEN` | 0 |
| `UNRESOLVED` | 0 |

The synergy `Agent` row is a data model rather than an executor. Desktop, game-mate, installer, and judge runner classes have explicit construction only and no default activation.

## H. C-L4 smoke containment

The machine-specific output default was removed from the companion and smoke tool. `--output-root` is mandatory and must be an absolute external path. Root, drive root, traversal, repository, repository parent, inside-repository targets, unknown filenames, and resolved escapes fail closed. Reset deletes only five known smoke-owned filenames and preserves unrelated files.

Repository-wide counts: `<REMOVED_MACHINE_SPECIFIC_PATH>=0`, `<REMOVED_MACHINE_SPECIFIC_PATH>=0`. The explicit external smoke run completed 10 fixtures with exit code 0 and wrote five files only under the external runtime sandbox. The Windows host did not permit creation of the optional symlink fixture, so that one test is reported as skipped; the implementation itself rejects a resolved target escape.

## I. Validation

| Gate | Collected | Passed | Failed | Skipped | Exit |
|---|---:|---:|---:|---:|---:|
| Existing regression | 104 | 104 | 0 | 0 | 0 |
| Existing TAP R2A | 70 | 70 | 0 | 0 | 0 |
| New R2B | 26 | 25 | 0 | 1 | 0 |
| Decisive combined | 200 | 199 | 0 | 1 | 0 |

R2A retained 58 expected negative fixture rejections with zero accidental passes. R2B fail-closed negative checks passed.

## J. Repository equivalence

`EXACT_EQUIVALENCE_PASS`

Pre/post decisive validation produced zero added, removed, or changed files and directories. Ordinary Git rows and ignored rows were zero. `.pyc=0`, `__pycache__=0`, repository `data/` was absent, and HEAD remained `a668e0501dd9b975fa5e455da781611f9534e509`.

## K. Evidence manifests

Core evidence contains 32 stable artifacts. Full forensic custody contains 665 artifacts and includes external pytest, bytecode-routing, and runtime-sandbox files. The core policy excludes transient state without discarding its full-custody hash coverage.

## L. Git commits and bundle

Commits are local and unsigned because repository signing is enabled but the known local GPG-agent state was not invoked; Git configuration was not changed.

1. `03dc919a7c5ec9e992b28166e31b8ddaf37e13d0` - `feat(tap): close T03 T06 and T07 binding discovery`
2. `b238415f61cf8d2e9f9cec5c67e267da57d24033` - `fix(tap): harden C-L4 smoke output containment`
3. `983cdac5ed9cd2aa4a625b5b5ba46130e77d125d` - `test(tap): add R2B closure fixtures and evidence policy`
4. `a668e0501dd9b975fa5e455da781611f9534e509` - `fix(tap): prioritize evidence-specific network route classes`

Bundle: `bundle/ester-clean-code-r2b-binding-closure.bundle`, 10,111,245 bytes, SHA-256 `d50bb0e50520d3991fed68cee8d02bf2b97cfc393cf22b84a8d6726675426308`. Verification passed and the advertised ref is `a668e0501dd9b975fa5e455da781611f9534e509 refs/heads/tap-r2b-binding-closure-20260823`.

## M. Local evidence matrix

| Test | Local R2B status | Public status |
|---|---|---|
| TAP-T01 | `LOCAL_VERIFIED_CANDIDATE` | `PUBLIC_VERIFIED` |
| TAP-T02 | `LOCAL_VERIFIED_CANDIDATE` | `PUBLIC_CANDIDATE_NEEDS_EXECUTION` |
| TAP-T03 | `LOCAL_PARTIAL_CANDIDATE` | `PUBLIC_CANDIDATE_NEEDS_EXECUTION` |
| TAP-T04 | `LOCAL_VERIFIED_CANDIDATE` | `PUBLIC_VERIFIED` |
| TAP-T05 | `LOCAL_VERIFIED_CANDIDATE` | `PUBLIC_VERIFIED` |
| TAP-T06 | `LOCAL_VERIFIED_CANDIDATE` | `SPECIFICATION_ONLY` |
| TAP-T07 | `LOCAL_VERIFIED_CANDIDATE` | `PUBLIC_CANDIDATE_NEEDS_EXECUTION` |
| TAP-T08 | `LOCAL_VERIFIED_CANDIDATE` | `PUBLIC_CANDIDATE_NEEDS_EXECUTION` |
| TAP-T09 | `LOCAL_VERIFIED_CANDIDATE` | `PUBLIC_VERIFIED` |
| TAP-T10 | `LOCAL_VERIFIED_CANDIDATE` | `PUBLIC_VERIFIED` |

Public TAP evidence status is unchanged. `M4_FULL_PASS=false`. `TAP-C=NOT CLAIMED`.

## N. Remaining gap and recommendation

The exact remaining gap is deployment evidence for the 78 `DEPLOYMENT_EXTERNAL` T03 surfaces. Repository bytes establish their activation routes but not which services are active in a real deployment or whether external process controls enforce the declared pause/revoke boundary.

R2C evidence promotion is not yet authorized. A review-only R2C inspection is technically safe if it preserves T03 as partial and performs no publication, but owner acceptance or deployment activation custody is required before any public evidence upgrade.

Nothing was pushed, released, published, deployed, or changed in the website, Zenodo, OVH, or DNS.
