# CCDP OPEN ISSUES

**Package:** Child-`c` Development Protocol
**Version:** v0.1 package + v0.1.1 hygiene guidance
**Date:** 2026-05-14

---

## 0. Purpose

This file lists unresolved issues, release blockers, validation gaps, and hygiene tasks for the CCDP package.

These are not root contradictions unless explicitly marked as such.

Current registered hard contradictions:

```text
0
```

---

## 1. Open issue register

| ID | Issue | Required action | Priority | Owner stage |
| --- | --- | --- | --- | --- |
| OI-001 | Obsolete draft isolation | Move or mark `CCDP%20v0_1.md` as obsolete / non-canonical. | High | v0.1.1 hygiene |
| OI-002 | Traceability refresh | Update traceability matrix to include all modules created after the initial matrix. | High | v0.1.1 hygiene |
| OI-003 | Conformance refresh | Update conformance matrix with late modules and concrete test IDs. | High | v0.1.1 hygiene |
| OI-004 | Canonical precedence rule | Apply one package-wide precedence rule across all modules. | High | v0.1.1 hygiene |
| OI-005 | Raw evidence exception centralization | Define one canonical raw-evidence exception protocol in Witness Schema and reference it elsewhere. | High | v0.1.1 hygiene |
| OI-006 | Clean start clarification | Clarify that clean start means active adult continuity clean start, not unlawful destruction of minimal witness/legal records. | High | v0.1.1 hygiene |
| OI-007 | Terminology disambiguation | Separate child maturity `C0–C5`, conformance `CCDP-0…5`, assertion `C-A*`, memory `M*`, dependency `D*`. | Medium | Glossary / package index |
| OI-008 | Developmental psychology review | External specialist review needed for attachment, privacy, dependency, sealed zones, adolescence, and adult migration. | High | Specialist review |
| OI-009 | Jurisdictional annexes | Belgium / EU and other local annexes needed. CCDP cannot decide local law. | High | Legal/compliance |
| OI-010 | Implementation schema validation | Extract JSON schemas from prose files into machine-validated `.schema.json` files. | Medium | Implementation |
| OI-011 | UI wording review | Review child/parent/school wording for coercion, over-trust, false reassurance, and disclosure confusion. | Medium | UX / developmental review |
| OI-012 | Sensitive release split | Define which files are public, technical, restricted, or internal before public release. | High | Release control |
| OI-013 | PDF production | Produce PDFs after Markdown freeze; avoid SHA manifest until PDF set is included. | Medium | Publication |
| OI-014 | Cross-repo placement | Decide final GitHub paths and repository ownership. | Medium | Repository planning |
| OI-015 | SHA256SUMS | Generate after all Markdown/PDF files are finalized. | Medium | Codex release step |

---

## 2. Release blockers before public package

1. Mark or move obsolete draft.
2. Refresh Traceability and Conformance matrices.
3. Centralize raw-evidence exception wording.
4. Add canonical precedence rule to package index and relevant documents.
5. Produce final `SHA256SUMS` only after PDFs are included.
6. Decide public / technical / sensitive split.
7. Add release notes and canonical reading order to root package.

---

## 3. Specialist review blockers

Before any claim stronger than draft research protocol:

- child-development review;
- education review;
- legal/compliance review;
- privacy/security review;
- implementation security review;
- red-team review using synthetic fixtures only.

---

## 4. Not blockers for v0.1 draft

These are acceptable as open future work for v0.1 draft release:

- no product implementation;
- no legal annex;
- no clinical validation;
- no country-specific custody procedure;
- no full JSON Schema extraction;
- no certification body;
- no public UX guide yet.
