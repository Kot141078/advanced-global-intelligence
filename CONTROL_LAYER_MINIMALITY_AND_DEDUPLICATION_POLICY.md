# Control-Layer Minimality and Deduplication Policy

## Purpose

Provide one compact canonical policy for keeping the corpus control stack minimal:
when a new layer is justified, when an existing layer should be extended instead,
and how to avoid duplication and schema-noise without flattening real distinctions.
Use `QUESTION_TO_CONTROL_SURFACE_MAP.md` when the remaining question is where a
reader should start, not whether a new control layer is justified. Use
`CONTROL_STACK_COMPLETENESS_AND_STOP_RULE.md` when the remaining question is
whether the assembled stack is already sufficient enough to stop adding layers.

## 1. Why this file exists

A mature control stack can fail not only by absence, but by accretion,
duplication, and schema-noise.

## 2. Core rule

New control-layer surfaces must justify their existence. Similarity is not enough
for merge; convenience is not enough for duplication.

## 3. Canonical minimality rules

| Rule ID | Rule | What it protects | Typical application | What it must not be confused with |
| --- | --- | --- | --- | --- |
| `ML01` | prefer bounded extension of an existing canonical layer over creating a near-duplicate | stack compactness without losing canon | a new review need fits an existing control surface with one short added rule | forced merge of surfaces with different control meaning |
| `ML02` | create a new layer only when it adds a genuinely new control function | new layers remain rare and justified | a new file is proposed only after existing layers fail to cover the function cleanly | cosmetic splitting or naming preference |
| `ML03` | do not merge layers that differ in authority semantics, even if wording overlaps | control hierarchy and source meaning | status, promotion, correction, supersession, and ownership stay distinct | superficial deduplication by wording similarity |
| `ML04` | routing or discoverability repetition may be short and local, but doctrinal ownership must not duplicate | bounded pointers without parallel doctrine | a machine-entry file adds one raw pointer to an AGI control surface | cross-repo restatement as new canon |
| `ML05` | JSON companion is justified only when it adds structural machine-use value beyond markdown | machine structure stays useful rather than noisy | JSON is skipped when markdown already carries the needed bounded table | decorative schema duplication |
| `ML06` | weak coupling is not enough reason to auto-touch adjacent control layers | change scope stays bounded | a nearby surface is reviewed but left untouched after dependency check | mandatory rewrite of every neighbor |
| `ML07` | compactness must not erase necessary distinctions | real control semantics survive cleanup | superficially similar layers stay separate when they answer different governance questions | semantic flattening sold as simplification |
| `ML08` | control layers should remain dry and bounded; avoid narrative inflation | maintainers can audit rules quickly | a control file states rule and boundary without manifesto-style expansion | stylistic compression that drops control force |
| `ML09` | a local convenience note is not automatically a new corpus-control layer | local helpers do not become canon by drift | a note remains local or pointer-only until real corpus-level function exists | silent canonization of convenience text |
| `ML10` | if unclear whether a new layer is justified, fail closed and prefer updating the smallest fitting existing layer | anti-sprawl default | proposed new canon is deferred until its unique function is explainable in one short line | deletion by default or refusal to improve existing layers |

## 4. Deduplication anti-patterns

| Anti-pattern ID | What goes wrong | Why it matters |
| --- | --- | --- |
| `DP01` | a new layer is created for a wording tweak only | canon grows while control function stays unchanged |
| `DP02` | a JSON companion is created without new structure | machine-facing surfaces accumulate schema-noise instead of value |
| `DP03` | the same rule is restated as if new canon in multiple places | reviewers lose track of the real governing source |
| `DP04` | distinct control meanings are merged into one “simplified” layer | important authority differences disappear behind cleaner phrasing |
| `DP05` | cross-repo convenience text drifts into parallel doctrine | bounded routing starts competing with canonical ownership |
| `DP06` | coupling is interpreted as mandatory rewrite everywhere | review discipline turns into unnecessary multi-file churn |
| `DP07` | a new control layer is added before checking whether an existing one can absorb the change | the stack expands by habit rather than need |
| `DP08` | the stack is “cleaned up” by deleting distinctions that still carry real control value | apparent simplicity hides real governance loss |

## 5. Fail-closed minimality rule

If maintainers cannot explain in one short line what new control function a
proposed layer adds, the layer should probably not be created yet.

## 6. Read next

- `CANONICAL_OWNERSHIP_AND_BOUNDARIES.md`
- `QUESTION_TO_CONTROL_SURFACE_MAP.md`
- `CONTROL_STACK_COMPLETENESS_AND_STOP_RULE.md`
- `CONTROL_SURFACE_DEPENDENCY_AND_COUPLING_MAP.md`
- `ENTRY_ACCEPTANCE_AND_REGRESSION.md`
- `PACKAGE_INTAKE_AND_INTEGRATION.md`
- `PRECEDENCE_AND_RESOLUTION.md`
