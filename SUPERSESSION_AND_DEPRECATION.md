# Supersession and Deprecation

## Purpose

This file fixes the minimum corpus-level rules for how evolving artifacts should be read once newer, stronger, or better-routed surfaces appear.
Use it when the question is not "what is this artifact?" but "is this still primary, merely retained, historically preserved, companion-only, or no longer preferred for first reading?"
Use `TERMINOLOGY_AND_ALIAS_POLICY.md` when the apparent supersession risk is only alias drift or naming drift rather than an actual change of semantic role.
Use `ENTRY_ACCEPTANCE_AND_REGRESSION.md` when the question is whether the overall corpus layer still passes acceptance after a supersession-sensitive edit.
Use `CANONICAL_OWNERSHIP_AND_BOUNDARIES.md` when the question is ownership rather than reading preference or retention state.
Use `ARTIFACT_ID_AND_REFERENCE_POLICY.md` when the question is whether a rename or move preserves the same artifact identity rather than creating a new one.
Use `PUBLIC_CORRECTION_AND_ERRATA_POLICY.md` when the public-history question is not just preferred-current state, but which explicit correction class should now be used.

## 1. Why this file exists

The corpus preserves history, but preservation must not create ambiguity about what is primary now.
Historical availability is valuable only if the canonical layer also makes present preference explicit.

## 2. Core rule

- supersession is explicit, not implicit
- retention is not equality
- historical availability does not imply current primacy
- deprecation does not mean erasure

## 3. Canonical state vocabulary

| State | What it means | How it should be read | Citable | Preferred for new readers |
|---|---|---|---|---|
| `primary` | current preferred surface for its semantic role | read first when that role is the question | yes | yes |
| `retained` | still intentionally available and still meaningful, but not the main first-hop surface | read as valid supporting or continuity-preserving material | yes | not by default |
| `superseded` | an older surface has been overtaken by a stronger current surface for the same role | read with explicit awareness that a newer preferred surface exists | yes | no |
| `companion` | a narrative or adjacent interpretive surface that remains important without becoming normative core | read for human or context-bearing value, not as doctrinal replacement | yes, as companion | only for companion reading |
| `historical-only` | preserved mainly for trace, chronology, and review of how the corpus evolved | read when transition history or historical comparison matters | yes, for historical reference | no |
| `control-surface` | routing, discipline, or corpus-control surface rather than doctrinal artifact | read to determine entry, preference, marking, or review rules | yes | yes, when routing is the question |

## 4. Supersession triggers

| Trigger | What changes | What must be updated | What must not be forgotten |
|---|---|---|---|
| `D01` | a newer canonical artifact replaces an older primary artifact | `CITATION_AND_VERIFICATION.md`; `CLAIMS_AND_EVIDENCE_MAP.md`; `STATUS_AND_MATURITY_MAP.md`; `CHANGE_CONTROL_AND_SYNC.md`; relevant entry/control surface | older artifact may remain citable even when no longer primary |
| `D02` | a draft becomes the preferred current reading surface | `STATUS_AND_MATURITY_MAP.md`; `STACK_LOCK_2026-04-12.json`; `CITATION_AND_VERIFICATION.md`; relevant entry/control surface | preferred current reading does not by itself make the artifact mature core |
| `D03` | a former entry surface remains valid but is no longer first-hop preferred | `MASTER_ENTRY.md`; `REPO_INDEX.md`; `REPO_INDEX.json`; `MACHINE_ENTRY.md`; `CHANGE_CONTROL_AND_SYNC.md` | retained entry surface is still available, but routing must show the preference change |
| `D04` | a historical artifact stays citable but must no longer be treated as current primary | `CITATION_AND_VERIFICATION.md`; `SUPERSESSION_AND_DEPRECATION.md`; relevant entry/control surface | citable != preferred |
| `D05` | a companion surface changes role without becoming normative core | `STATUS_AND_MATURITY_MAP.md`; `CHANGE_CONTROL_AND_SYNC.md`; affected companion context | companion != superseded normative artifact |
| `D06` | a control-layer file is replaced by a stronger control-layer file | `REPO_INDEX.md`; `REPO_INDEX.json`; `MASTER_ENTRY.md`; `MACHINE_ENTRY.md`; `CHANGE_CONTROL_AND_SYNC.md` | stronger control layer does not silently erase the older control trace |
| `D07` | a stable snapshot is superseded by a newer frozen public object | `STACK_LOCK_2026-04-12.json`; `CITATION_AND_VERIFICATION.md`; `REPO_INDEX.md`; `REPO_INDEX.json`; manifests where current repo pattern requires them | old frozen object may still be citeable for historical or locked reading |
| `D08` | a path/name changes but semantic role stays the same | `REPO_INDEX.md`; `REPO_INDEX.json`; `CLAIMS_AND_EVIDENCE_MAP.md`; `STATUS_AND_MATURITY_MAP.md`; raw cross-repo pointers | rename alone does not imply supersession |
| `D09` | a claim’s supporting artifact changes while primary artifact remains unchanged | `CLAIMS_AND_EVIDENCE_MAP.md`; `CHANGE_CONTROL_AND_SYNC.md`; `CITATION_AND_VERIFICATION.md` only if preferred citation path changed | supporting change != primary change |
| `D10` | a reserved territory note becomes more developed but still not mature core | `STATUS_AND_MATURITY_MAP.md`; `CHANGE_CONTROL_AND_SYNC.md`; relevant entry/control surface | more developed reserved territory is still not mature core unless explicitly reclassified |

## 5. Minimal marking rule

When supersession happens, the corpus should make the change visible in the canonical layer.
Readers should not have to infer preference from chronology alone.

## 6. Required sync surfaces on supersession

- `STACK_LOCK_2026-04-12.json`
- `CITATION_AND_VERIFICATION.md`
- `CLAIMS_AND_EVIDENCE_MAP.md`
- `STATUS_AND_MATURITY_MAP.md`
- `CHANGE_CONTROL_AND_SYNC.md`
- `ENTRY_ACCEPTANCE_AND_REGRESSION.md`
- `TERMINOLOGY_AND_ALIAS_POLICY.md`
- `REPO_INDEX.md` / `REPO_INDEX.json` / `MASTER_ENTRY.md` / relevant entry surface
- companion context if affected

## 7. Anti-confusion note

Older does not mean weaker.
Newer does not automatically mean canonical.
Available does not mean preferred.
An older surface may remain citable without remaining first-hop preferred.
A retained or superseded surface may still be citable without staying first-hop preferred.
Citation preference does not redefine ontological status or maturity, companion is not degraded superseded normativity, and historical-only still means preserved rather than erased.
Supersession or retention does not by itself reassign canonical package ownership.
Path drift does not by itself create a new artifact identity.

## 8. Read next

- `STACK_LOCK_2026-04-12.json`
- `CITATION_AND_VERIFICATION.md`
- `CLAIMS_AND_EVIDENCE_MAP.md`
- `STATUS_AND_MATURITY_MAP.md`
- `CHANGE_CONTROL_AND_SYNC.md`
- `CANONICAL_OWNERSHIP_AND_BOUNDARIES.md`
- `ARTIFACT_ID_AND_REFERENCE_POLICY.md`
- `PUBLIC_HISTORY_ANNOTATION_AND_RELEASE_NOTE_POLICY.md`
- `PUBLIC_CORRECTION_AND_ERRATA_POLICY.md`
