# Control Stack Completeness and Stop Rule

## Purpose

Provide one compact canonical rule for deciding when the current corpus control
stack is already functionally sufficient, when a genuinely new control layer is
still justified, and when the correct action is to stop adding files.

## 1. Why this file exists

The corpus already has many control surfaces. The next maintainer question is
not always "what else can be added?" but "what is already enough for bounded
control coverage right now?"

This file exists so completeness is not confused with public-history
completion, local cleanliness, promotion readiness, or metaphysical finality.
Open questions can remain open while the control stack is still functionally
complete enough for its present corpus-control role.

## 2. Core rule

The current stack should be treated as functionally sufficient when the
existing control surfaces already cover the corpus-level control functions that
serious readers and maintainers actually need.

A new layer is justified only when maintainers can point to an irreducible
missing control function that cannot be cleanly answered by the existing stack,
its bounded adjacent surfaces, or a short extension of an existing owner file.

Discomfort with incompleteness, cumulative local dirtiness, or a desire for one
more summary is not by itself a missing control function.

## 3. Canonical completeness criteria

| Completeness ID | Criterion | What it means | Why it matters | What failure would look like |
| --- | --- | --- | --- | --- |
| `CC01` | entry and orientation surfaces exist and are discoverable | readers can reach the corpus through primer, machine-entry, and index routes without reconstructing the stack ad hoc | serious reading starts from stable entry rather than guesswork | maintainers keep adding orientation files because the existing entry path is unclear |
| `CC02` | claims, status, and assertion boundaries exist | the corpus can distinguish what is claimed, how mature it is, and how strongly it should be read | control logic fails if positive claims and their force blur together | readers treat tentative or companion material as settled canon because the boundary layer is missing |
| `CC03` | ownership, precedence, and invariant boundaries exist | the stack can say which repo owns what, what outranks what, and what cannot be casually contradicted | corpus-control meaning depends on source hierarchy rather than prose convenience | new notes appear because maintainers cannot tell who owns the doctrine or how conflicts resolve |
| `CC04` | public-safe, exclusion, and handoff boundaries exist | the stack can distinguish what may be surfaced publicly, what stays pointer-only, and what belongs in bounded handoff bundles | safety and scope depend on more than simple availability | outward routing starts absorbing unsafe, excluded, or over-broad material because boundary classes are absent |
| `CC05` | promotion, atomicity, tranche, and cutover discipline exists | the stack can separate local control assembly from later public-history movement and can describe how future movement should stay bounded | promotion confusion otherwise gets misread as conceptual absence | maintainers keep inventing new planning layers because promotion logic is still implicit |
| `CC06` | correction and annotation discipline exists | the stack can describe how public notes and later corrections should be typed and bounded | without this, later maintenance becomes theatrical or silent | future public-history treatment would require ad hoc correction language every time |
| `CC07` | question-triage and current-state surfaces exist | the stack can answer where a reader should start and what the current local condition is without inventing new routing notes | maintainers need bounded routing and present-tense visibility | every new question produces a fresh meta-note because there is no stable triage or snapshot surface |
| `CC08` | coupling, minimality, and anti-sprawl discipline exists | the stack can say what should be co-reviewed, what should stay separate, and why not every discomfort justifies another layer | mature stacks fail by uncontrolled growth as much as by omission | new control files keep appearing because there is no fail-closed rule against duplication or auto-touch sprawl |
| `CC09` | open questions and explicit non-claims remain visible | incompleteness is represented explicitly instead of being hidden or patched over with synthetic closure | a complete control stack can still contain unresolved territory | maintainers add summary layers to mask open territory instead of naming it as open |
| `CC10` | the stack can answer both what is here now and what should happen later without inventing a new file | current-state, staging, blockers, and later promotion logic together already cover present condition and future movement in bounded form | completeness means the existing stack can carry present and next-step control load | maintainers create another meta-layer only because they have not routed through the already assembled present/future surfaces |

## 4. Stop-rule anti-patterns

| Stop-rule ID | Anti-pattern | Why it is a stop signal rather than a justification |
| --- | --- | --- |
| `SR01` | a new layer is proposed because an existing control file feels too short | shortness alone does not prove a missing control function |
| `SR02` | a new layer is proposed because bounded uncertainty feels uncomfortable | discomfort with non-closure is not the same as a real coverage gap |
| `SR03` | a new layer mainly restates doctrine that already has an owner surface | restatement increases stack weight without adding new control force |
| `SR04` | a new JSON companion is proposed only because neighboring layers have JSON | parity with adjacent files is schema-noise, not structure |
| `SR05` | a new layer is proposed before checking whether triage plus adjacent reading already answers the gap | the stack should be used before it is expanded |
| `SR06` | cumulative local dirtiness is treated as proof that more control theory is needed | messy promotion state is a maintenance problem, not automatically a missing layer |
| `SR07` | not yet committed is treated as not yet conceptually represented | local public-history posture and conceptual coverage are different questions |
| `SR08` | maintenance discomfort is solved by adding a fresh meta-layer instead of using the existing stack | the default should be better routing and bounded reuse, not reflexive accretion |

## 5. Fail-closed stop rule

If maintainers cannot state in one short line what irreducible new control
function is missing, the default action is to stop adding layers and use the
existing stack.

Stopping does not mean no future layer can ever be justified. It means the
burden of proof stays on the proposed new control function, not on the current
stack to keep expanding until it feels total.

## 6. Read next

- `CONTROL_LAYER_MINIMALITY_AND_DEDUPLICATION_POLICY.md`
- `CONTROL_SURFACE_DEPENDENCY_AND_COUPLING_MAP.md`
- `CURRENT_CORPUS_STATE_AND_READINESS_SNAPSHOT.md`
- `CURRENT_LOCAL_CONTROL_STACK_STAGING_MAP.md`
- `QUESTION_TO_CONTROL_SURFACE_MAP.md`
- `OPEN_QUESTIONS_AND_EXPLICIT_NON_CLAIMS.md`
