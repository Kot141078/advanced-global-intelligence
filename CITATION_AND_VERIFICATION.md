# Citation and Verification

## Purpose

This file fixes the minimum corpus-level rules for citation and verification.
Use it to avoid confusing repo, snapshot, DOI object, hash manifest, package object, and narrative reading surface.
Use `CLAIMS_AND_EVIDENCE_MAP.md` when the starting point is a corpus claim and you need the primary artifact quickly.
Use `STATUS_AND_MATURITY_MAP.md` when the starting point is artifact weight, status, or maturity rather than claim location.
Use `CHANGE_CONTROL_AND_SYNC.md` when the question is what other corpus-control surfaces must move with a citation or verification change.
Use `SUPERSESSION_AND_DEPRECATION.md` when the question is whether an older but still available artifact remains primary, retained, superseded, or merely historical.
Use `ARTIFACT_ID_AND_REFERENCE_POLICY.md` when the question is whether the same artifact remains the same across path or filename drift.
Use `EXPORT_PROFILES_AND_HANDOFF_BUNDLES.md` when the question is which bounded public-safe bundle to hand off externally rather than what exact object to cite.

## 1. What counts as a public object

- repo: a moving public surface on its default branch
- tagged snapshot: a frozen reading surface bound to a tag or exact locked ref
- hash manifest: the integrity source for repository content verification
- DOI-backed object: a released public object with its own DOI, not the whole moving repo
- narrative companion repo: a public reading surface adjacent to, but not replacing, the normative core

## 2. What to cite

- cite the repo when referring to an evolving corpus surface
- cite the tag or locked snapshot when referring to a frozen reading surface
- cite the DOI when a specific DOI-backed public object is the object of reference
- cite the exact document when making a narrow claim about one protocol, note, or package

## 3. What not to confuse

- main branch != frozen snapshot
- GitHub-generated archive != integrity source of truth
- repo citation != document citation
- artifact ID != current path
- artifact ID != claim ID
- narrative companion != normative core
- code skeleton != polished product artifact
- DOI object != whole moving repo

## 4. Minimal verification path

- prefer stable tags and the current `STACK_LOCK_2026-04-12.json`
- prefer repo hash manifests over archive-level assumptions
- verify exact file presence and manifest alignment
- if a path changed, confirm the stable artifact ID before assuming a new artifact exists
- do not rely on screenshots or secondary summaries
- if in doubt, fall back to local verification against repository manifests

## 5. Corpus reading / citation routes

- Research / Normative: start from AGI, then cite the exact SER / DEA / EA-L4 / ERB document or DOI-backed object that carries the claim
- Engineering / Runtime: use stack lock plus ERB and `ester-clean-code`, then verify against repo manifests
- Narrative / Human: cite `qubit-of-hope-volume-i` as a narrative reading surface, not as the normative core
- Claim-first audit / review: use `CLAIMS_AND_EVIDENCE_MAP.md`, then step into the canonical artifact rather than citing the whole corpus at once
- Status-first review / audit: use `STATUS_AND_MATURITY_MAP.md`, then decide whether the artifact should be read as stable core, draft, runtime proof, companion, or reserved territory
- External handoff / export: use `EXPORT_PROFILES_AND_HANDOFF_BUNDLES.md` first, then cite the exact artifacts inside the chosen bounded bundle rather than the whole corpus by default

## 6. Read next

- `CORPUS_PRIMER.json`
- `STACK_LOCK_2026-04-12.json`
- `CANONICAL_DISTINCTIONS.md`
- `OBJECTIONS_AND_REPLIES.md`
- `CLAIMS_AND_EVIDENCE_MAP.md`
- `STATUS_AND_MATURITY_MAP.md`
- `CHANGE_CONTROL_AND_SYNC.md`
- `SUPERSESSION_AND_DEPRECATION.md`
- `ARTIFACT_ID_AND_REFERENCE_POLICY.md`
- `EXPORT_PROFILES_AND_HANDOFF_BUNDLES.md`
- `MASTER_ENTRY.md`
- `https://raw.githubusercontent.com/Kot141078/qubit-of-hope-volume-i/main/CORPUS_CONTEXT.md`
