# PDF Build Order and Submission Checklist v0.1

**Author:** Kotov Ivan
**Location:** Bruxelles, Belgium
**Date:** 2026-05-19
**Document ID:** `Article50_PDF_Build_Order_and_Submission_Checklist_v0_1`
**Package:** `Article50_Transparency_Submission_v0_1`
**Status:** Draft package-control and PDF-readiness document
**Intended channel:** European Commission / AI Office consultation on draft Article 50 transparency guidelines
**Legal status:** Not legal advice. Not certification. Not a conformity assessment.
**Primary posture:** build only after Markdown freeze and human claim review.

---

## 0. Purpose

This document defines the build order, PDF inclusion policy, submission-readiness checklist, and final freeze sequence for the Article 50 transparency submission package.

It answers four practical questions:

1. Which Markdown files belong in the formal PDF?
2. Which files are package-control or supporting files?
3. What must be checked before PDF generation?
4. What remains to be done before EUSurvey submission?

This file is a package-control artifact.

It does not add new Article 50 theory.

---

## 1. Current package inventory

Current expected package:

```text
Article50_Transparency_Submission_v0_1/
├── README.md
├── 00_Cover_Note.md
├── 01_Article_50_Compliance_Mapping_Pack_v0_1.md
├── 02_System_Role_Obligation_Control_Evidence_Table_v0_1.md
├── 03_L4_Witness_and_Provenance_Bridge_v0_1.md
├── 04_Non_Claims_Open_Issues_and_Legal_Review_v0_1.md
├── 05_EUSurvey_Response_Draft_v0_1.md
└── 06_PDF_Build_Order_and_Submission_Checklist_v0_1.md
```

At this stage, these files form a coherent draft package.

---

## 2. Recommended PDF types

There are two useful PDF outputs.

### 2.1 Full supporting package PDF

Filename:

```text
Kotov_Ivan_Article50_Transparency_Submission_v0_1_FULL.pdf
```

Purpose:

```text
Full supporting package for GitHub / Zenodo / legal review / archival record.
```

Include:

```text
00_Cover_Note.md
01_Article_50_Compliance_Mapping_Pack_v0_1.md
02_System_Role_Obligation_Control_Evidence_Table_v0_1.md
03_L4_Witness_and_Provenance_Bridge_v0_1.md
04_Non_Claims_Open_Issues_and_Legal_Review_v0_1.md
05_EUSurvey_Response_Draft_v0_1.md
06_PDF_Build_Order_and_Submission_Checklist_v0_1.md
```

Do not include `README.md` inside the main PDF unless a repository-style front matter is desired.

`README.md` is primarily for repository navigation.

### 2.2 Short submission PDF

Filename:

```text
Kotov_Ivan_Article50_Transparency_Submission_v0_1_SHORT.pdf
```

Purpose:

```text
Shorter attachment if the official questionnaire allows limited supporting material.
```

Include:

```text
00_Cover_Note.md
01_Article_50_Compliance_Mapping_Pack_v0_1.md
02_System_Role_Obligation_Control_Evidence_Table_v0_1.md
04_Non_Claims_Open_Issues_and_Legal_Review_v0_1.md
05_EUSurvey_Response_Draft_v0_1.md
```

Exclude:

```text
03_L4_Witness_and_Provenance_Bridge_v0_1.md
06_PDF_Build_Order_and_Submission_Checklist_v0_1.md
README.md
```

Reason:

```text
03 is technically useful but may be too detailed for a short policy attachment.
06 is a package-control file, not part of the substantive submission.
README is repository navigation.
```

---

## 3. Recommended canonical reading order

For the full package:

| Order | File | Include in full PDF | Include in short PDF | Role |
|---:|---|---:|---:|---|
| 0 | `00_Cover_Note.md` | Yes | Yes | Entry point, non-claim boundary, purpose. |
| 1 | `01_Article_50_Compliance_Mapping_Pack_v0_1.md` | Yes | Yes | Main compliance-mapping argument. |
| 2 | `02_System_Role_Obligation_Control_Evidence_Table_v0_1.md` | Yes | Yes | Operational evidence table. |
| 3 | `03_L4_Witness_and_Provenance_Bridge_v0_1.md` | Yes | Optional / No | Technical bridge for witness/provenance. |
| 4 | `04_Non_Claims_Open_Issues_and_Legal_Review_v0_1.md` | Yes | Yes | Claim safety and legal boundary. |
| 5 | `05_EUSurvey_Response_Draft_v0_1.md` | Yes | Yes | Questionnaire-ready response draft. |
| 6 | `06_PDF_Build_Order_and_Submission_Checklist_v0_1.md` | Yes | No | Package-control and readiness checklist. |
| repo | `README.md` | No by default | No | Repository landing page. |

---

## 4. PDF generation rule

Do not generate the formal PDF until the Markdown set is frozen.

Freeze means:

```text
[ ] file list accepted
[ ] filenames accepted
[ ] order accepted
[ ] non-claim boundary accepted
[ ] no known overclaim
[ ] no missing required document
[ ] no unresolved “should we include this?” decision
```

At the current stage, the package is close to PDF-ready, but final human review is still required.

---

## 5. Pre-PDF review checklist

Before PDF generation, check every file for:

```text
[ ] No “we are compliant” wording
[ ] No “certified” wording
[ ] No claim that L4 Witness replaces disclosure
[ ] No claim that metadata replaces visible notice
[ ] No claim that CLI Agent Mesh is a compliance system by itself
[ ] Provider/deployer distinction preserved
[ ] Human review treated as recorded responsibility, not decoration
[ ] CCDP kept secondary, not main Article 50 submission surface
[ ] EUSurvey path clearly identified
[ ] Official dates and links correct
[ ] File names stable
[ ] Markdown headings clean
[ ] Tables not too wide for PDF
[ ] Long code blocks not overflowing
[ ] Legal status repeated where needed
[ ] “Not legal advice / not certification / not conformity assessment” present
```

If any item fails:

```text
repair Markdown first;
do not generate PDF yet.
```

---

## 6. Table-width warning

The package contains wide tables.

PDF generation must handle:

- landscape tables where necessary;
- smaller table font if needed;
- text wrapping inside cells;
- no right-edge overflow;
- no clipped URLs;
- no broken code blocks;
- no unreadable dense table pages.

Recommended PDF style:

```text
A4
strict academic / regulatory style
clear heading hierarchy
monospace code blocks
compact but readable tables
no decorative design
professional margins
table wrapping enabled
URLs preserved
page breaks before major documents
```

---

## 7. Recommended PDF front matter

For the full PDF, use a front page:

```text
Article 50 Transparency Submission Pack v0.1

Technical evidence-chain contribution to the European Commission / AI Office consultation on draft Article 50 transparency guidelines

Kotov Ivan
Bruxelles, Belgium
2026-05-19

Status:
Draft technical submission package
Not legal advice
Not certification
Not a conformity assessment
Formal compliance remains deployment-specific and subject to legal review
```

Optional subtitle:

```text
System -> Role -> Obligation -> Control -> Evidence -> Responsible Actor
```

---

## 8. Recommended PDF footer

Use a footer similar to:

```text
Kotov Ivan — Article 50 Transparency Submission Pack v0.1 — Draft / Not legal advice
```

Do not use dramatic or promotional footer text.

---

## 9. Submission package versus corpus package

Do not attach the entire AGI/SER/L4/CCDP/CLI corpus to the consultation.

Use this package as the concise bridge.

The larger corpus can be referenced through:

- GitHub links;
- DOI links;
- selected source references;
- C-Governed CLI Agent Mesh link;
- later appendix if requested.

The first submission should be readable without requiring the reviewer to inspect 494 Markdown files.

---

## 10. GitHub placement recommendation

Recommended repository:

```text
advanced-global-intelligence
```

Recommended path:

```text
official/article50-transparency-submission/v0_1/
```

Alternative path:

```text
submissions/eu-ai-act/article50-transparency/v0_1/
```

Recommended files:

```text
README.md
00_Cover_Note.md
01_Article_50_Compliance_Mapping_Pack_v0_1.md
02_System_Role_Obligation_Control_Evidence_Table_v0_1.md
03_L4_Witness_and_Provenance_Bridge_v0_1.md
04_Non_Claims_Open_Issues_and_Legal_Review_v0_1.md
05_EUSurvey_Response_Draft_v0_1.md
06_PDF_Build_Order_and_Submission_Checklist_v0_1.md
Kotov_Ivan_Article50_Transparency_Submission_v0_1_FULL.pdf
SHA256SUMS
RELEASE_NOTES.md
```

Do not place first in CCDP.

Reason:

```text
This is an Article 50 transparency submission, not a child-facing AI package.
```

---

## 11. Zenodo recommendation

Zenodo should be used only after final freeze.

Recommended title:

```text
Article 50 Transparency Submission Pack v0.1: Evidence-Chain Mapping for AI Act Transparency Implementation
```

Recommended description:

```text
A technical evidence-chain contribution to the European Commission / AI Office consultation on draft Article 50 transparency guidelines under the EU AI Act. The package maps system boundaries, actor roles, transparency triggers, disclosure and marking controls, witness/audit evidence, human review, and responsible actors. It does not claim formal compliance, certification, or legal sufficiency for any concrete deployment.
```

Recommended keywords:

```text
EU AI Act
Article 50
Transparency
AI-generated content
Provenance
Audit trail
L4 Witness
Actor Grounding
Human review
AI-assisted workflows
C-Governed CLI Agent Mesh
```

Do not mint DOI before final claim review.

---

## 12. EUSurvey submission sequence

Recommended sequence:

```text
1. Freeze Markdown.
2. Generate short or full PDF.
3. Publish package to GitHub if desired.
4. Optionally publish to Zenodo after final freeze.
5. Open the official EUSurvey questionnaire.
6. Paste concise answer from `05_EUSurvey_Response_Draft_v0_1.md`.
7. Add supporting link or attachment if permitted.
8. Save final submitted text.
9. Archive submitted response in repository after submission, if appropriate.
```

Do not submit the raw package without checking the actual questionnaire fields.

---

## 13. EUSurvey response length control

If the questionnaire has a small text box, use:

```text
Please treat Article 50 transparency as an evidence chain: system boundary, actor role, trigger, user notice, machine-readable mark/provenance, audit or witness evidence, human review, responsible actor, and correction route. This prevents decorative labels and supports practical enforcement.
```

If the questionnaire has a larger text box, use the medium or long response from:

```text
05_EUSurvey_Response_Draft_v0_1.md
```

---

## 14. Final package status table

| File | Status | PDF role |
|---|---|---|
| `README.md` | Drafted | Repository navigation; not required in PDF. |
| `00_Cover_Note.md` | Drafted | Required. |
| `01_Article_50_Compliance_Mapping_Pack_v0_1.md` | Drafted | Required. |
| `02_System_Role_Obligation_Control_Evidence_Table_v0_1.md` | Drafted | Required. |
| `03_L4_Witness_and_Provenance_Bridge_v0_1.md` | Drafted | Full PDF / optional in short PDF. |
| `04_Non_Claims_Open_Issues_and_Legal_Review_v0_1.md` | Drafted | Required. |
| `05_EUSurvey_Response_Draft_v0_1.md` | Drafted | Required for internal package; may be omitted from public PDF if final survey answer differs. |
| `06_PDF_Build_Order_and_Submission_Checklist_v0_1.md` | Drafted | Full PDF / package control; not needed in short PDF. |

---

## 15. Remaining optional documents

The core package is complete after this document.

Optional files that may be created before release:

```text
RELEASE_NOTES.md
SHA256SUMS
07_Publication_Metadata_Sidecar_Template_v0_1.md
08_Human_Review_Record_Template_v0_1.md
09_Cover_Letter_to_European_Commission_AI_Office_v0_1.md
```

Recommended priority:

1. `07_Publication_Metadata_Sidecar_Template_v0_1.md`
2. `08_Human_Review_Record_Template_v0_1.md`
3. `RELEASE_NOTES.md`

Do not create too many documents before the consultation.

The package must stay readable.

---

## 16. PDF readiness decision

Current decision:

```text
Core Markdown package: complete enough for first PDF draft.
Human review: still required.
Legal review: still required before any compliance claim.
PDF generation: allowed as draft after this file.
Formal submission: not yet; requires final EUSurvey text and official form check.
```

Recommended next action:

```text
Create one draft full PDF from:
00, 01, 02, 03, 04, 05, 06.
```

Recommended short PDF:

```text
Create short PDF from:
00, 01, 02, 04, 05.
```

---

## 17. Final control statement

PDF generation is allowed only with this footer-level boundary:

```text
Draft technical submission package.
Not legal advice.
Not certification.
Not a conformity assessment.
Formal compliance remains deployment-specific and subject to legal review.
```

If that boundary is removed, the PDF should not be released.

---

## 18. Final build instruction

For the first PDF draft, build:

```text
Kotov_Ivan_Article50_Transparency_Submission_v0_1_FULL_DRAFT.pdf
```

from:

```text
00_Cover_Note.md
01_Article_50_Compliance_Mapping_Pack_v0_1.md
02_System_Role_Obligation_Control_Evidence_Table_v0_1.md
03_L4_Witness_and_Provenance_Bridge_v0_1.md
04_Non_Claims_Open_Issues_and_Legal_Review_v0_1.md
05_EUSurvey_Response_Draft_v0_1.md
06_PDF_Build_Order_and_Submission_Checklist_v0_1.md
```

Do not include:

```text
README.md
```

unless building a repository documentation PDF.

---

## 19. End state

When the files above are reviewed and accepted, the Markdown phase can be considered:

```text
complete for draft PDF generation
```

The next phase is:

```text
PDF build
  -> human review
  -> optional claim tightening
  -> GitHub placement
  -> optional Zenodo
  -> EUSurvey submission
```
