# Public-Safe Boundary and Exclusion Policy

## Purpose

This file fixes a short corpus-level boundary discipline for public-safe material, pointer-only references, excluded classes, and explicitly quarantined trees.
It helps maintainers, reviewers, and machine readers keep public corpus work separate from private, dangerous, runtime-sensitive, or off-limits domains.
Use `LOCAL_TO_PUBLIC_PROMOTION_POLICY.md` when material is already public-safe but the remaining question is whether the state is commit-ready or public-facing.

## 1. Why this file exists

A public corpus can fail not only through conceptual drift,
but through accidental mixing of public-safe material
with live, dangerous, private, or deployment-sensitive material.

## 2. Core rule

Public corpus surfaces may describe, point to, classify, or route.
They must not silently import unsafe runtime material into the public-safe layer.

## 3. Boundary classes

| Boundary ID | Boundary class | Meaning | Allowed public treatment | Disallowed treatment |
|---|---|---|---|---|
| `B01` | public-safe canonical corpus material | public canonical artifacts and control surfaces intentionally published as corpus sources | cite; classify; route; verify; use as bounded public source | treat nearby private or runtime material as implicitly included with it |
| `B02` | public-safe companion material | public companion, narrative, or contextual material intentionally released as bounded companion | cite as companion; route as companion; describe its bounded role | read as automatic normative primary or witness proof |
| `B03` | public-safe implementation-facing but bounded material | public implementation-facing skeleton or closure material intentionally published with bounded scope | cite as implementation proof or bounded runtime-facing context | treat as doctrinal owner or as permission to import adjacent private runtime trees |
| `B04` | pointer-only external/private reference | a domain that may be acknowledged as existing without being imported into corpus meaning | mention owner, role, boundary fact, or pointer only | read, summarize, copy from, or use as canonical source |
| `B05` | private runtime-sensitive material | private state, internal runtime traces, operator-sensitive configuration, or continuity-sensitive operational data | at most acknowledge abstract class or boundary fact | ingest, quote, classify as public source, or promote into public verification surfaces |
| `B06` | dangerous / non-public-safe code or operational content | code or operational material whose public corpus inclusion would be unsafe or irresponsible | mention only at high level if boundary explanation requires it | publish operational detail, executable guidance, or code as public corpus content |
| `B07` | excluded mixed environment / live entity domain | a mixed domain where public-safe and live/private material coexist without reliable separation | keep excluded or pointer-only until explicitly separated and classified | cherry-pick from the mixed domain as if it were clean public-safe corpus |
| `B08` | quarantined / off-limits source tree | a tree explicitly designated off-limits by owner or operator | acknowledge only as a quarantine fact if already known from safe surfaces | read, diff, baseline, validate paths against, copy from, or derive corpus layers from it |

## 4. Typical excluded material classes

| Excluded ID | Material class | What it is | Public-safe treatment rule |
|---|---|---|---|
| `E01` | live entity runtime trees | live working trees or active entity environments | exclude from corpus sourcing; at most acknowledge as pointer-only boundary fact |
| `E02` | deployment-sensitive code not intended for public corpus | operational code or procedures not published for public-safe corpus use | do not import; do not restate as public implementation canon |
| `E03` | private keys / secrets / credentials / access tokens | any direct access-bearing secret material | exclude absolutely; never copy, quote, hash, or summarize |
| `E04` | raw personal/private continuity data | raw private continuity records, personal traces, or sensitive operator-linked state | exclude; only abstract class mention is allowed |
| `E05` | unsafe automation or public-dangerous code surfaces | automation or code whose public release would be unsafe | exclude from public corpus; only bounded high-level classification is allowed |
| `E06` | mixed public/private mirrors without explicit classification | mirrors that contain both public-safe and non-public-safe material without clean boundary markers | treat as excluded until explicit classification separates safe from unsafe |
| `E07` | unpublished internal experiment trees | internal experiment domains not intentionally released into public corpus routing | keep excluded or pointer-only until explicit public-safe release exists |
| `E08` | any source tree explicitly marked off-limits by owner/operator | any tree whose operator says it is outside allowed corpus handling | quarantine completely; do not use for baseline, diff, reference, or derivation |

## 5. Pointer-only rule

Some non-public-safe domains may be acknowledged only as boundary facts,
without reading from them, copying from them, or using them as canonical source.

## 6. Quarantine rule

If a source tree is designated off-limits,
it is not to be used for baseline, diff, reference, path validation, or corpus-layer derivation.

## 7. Intake interaction

New package intake must first determine whether candidate material is public-safe,
pointer-only, or excluded before any corpus integration decision proceeds.
Intake class does not by itself decide public-safe boundary class.
Export and handoff bundles may use only public-safe artifacts plus explicit boundary notes; they must not quietly include pointer-only or excluded classes as bundle contents.
Public-safe classification does not by itself make a local state commit-ready or public-facing.

## 8. Fail-closed boundary rule

If maintainers cannot establish that a source or artifact is public-safe for corpus inclusion,
treat it as excluded or pointer-only until clarified.

## 9. Read next

- `CANONICAL_OWNERSHIP_AND_BOUNDARIES.md`
- `PACKAGE_INTAKE_AND_INTEGRATION.md`
- `ENTRY_ACCEPTANCE_AND_REGRESSION.md`
- `CHANGE_CONTROL_AND_SYNC.md`
- `ARTIFACT_ID_AND_REFERENCE_POLICY.md`
- `EXPORT_PROFILES_AND_HANDOFF_BUNDLES.md`
- `LOCAL_TO_PUBLIC_PROMOTION_POLICY.md`
