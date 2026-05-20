# Non-Claims, Open Issues, and Legal Review v0.1

**Author:** Kotov Ivan
**Location:** Bruxelles, Belgium
**Date:** 2026-05-19
**Document ID:** `Article50_Non_Claims_Open_Issues_and_Legal_Review_v0_1`
**Package:** `Article50_Transparency_Submission_v0_1`
**Status:** Draft legal-boundary and review-control document
**Intended channel:** European Commission / AI Office consultation on draft Article 50 transparency guidelines
**Legal status:** Not legal advice. Not certification. Not a conformity assessment.
**Primary posture:** conservative claims, explicit limits, legal handoff before deployment-specific compliance assertions.

---

## 0. Executive summary

This document defines the non-claim boundary, open issues, and legal review requirements for the Article 50 transparency submission package.

The purpose is to prevent the package from being misread as:

- a certification claim;
- a legal compliance conclusion;
- a product conformity assessment;
- an assertion that a public research corpus is automatically Article 50 compliant;
- a statement that L4 Witness, provenance metadata, or CLI Agent Mesh governance can replace legal duties.

The controlling rule is:

```text
architecture alignment
  !=
formal compliance
```

A serious Article 50 claim requires:

```text
concrete system boundary
  -> actor role
  -> obligation trigger
  -> disclosure / marking / review control
  -> evidence
  -> responsible actor
  -> legal review
```

---

## 1. Primary non-claim

This submission does not claim formal Article 50 compliance for any deployed AI system.

It claims only that the public architecture and governance corpus provides candidate patterns for:

- transparency mapping;
- provenance;
- user-facing disclosure;
- machine-readable marking support;
- witness/audit evidence;
- human review;
- responsibility assignment;
- correction and review routes.

The recommended submission sentence is:

```text
This package provides an architecture-aligned evidence-chain approach to Article 50 transparency implementation. It does not claim formal compliance, certification, or legal sufficiency for any concrete deployment without system-specific evidence and legal review.
```

---

## 2. Forbidden claims

The following claims must not be made in the submission, public release, README, EUSurvey response, or cover note.

| Forbidden claim | Reason |
|---|---|
| “This corpus is Article 50 compliant.” | A corpus is not automatically a deployed system, provider control, or deployer workflow. |
| “L4 Witness proves compliance.” | Witness can support evidence; it does not replace legal obligations or user-facing disclosure. |
| “Machine-readable metadata is enough.” | Humans may still require visible disclosure. Metadata may be stripped or inaccessible. |
| “Human review solves public-interest disclosure.” | Review must be real, scoped, recorded, and tied to editorial responsibility. |
| “CLI Agent Mesh makes AI-assisted workflow compliant.” | Agent governance provides evidence infrastructure, not legal compliance by itself. |
| “Publication on GitHub/Zenodo proves regulatory adequacy.” | DOI and SHA support integrity and referenceability, not legal adequacy. |
| “The system does not need legal review because it is architecture-safe.” | Legal duties are jurisdictional and use-case-specific. |
| “CCDP proves child-facing compliance.” | Child-facing deployment requires specialist, legal, psychological, educational, and jurisdictional review. |
| “The architecture replaces provider/deployer classification.” | Role classification is required for concrete obligations. |
| “The architecture creates legal personhood for `c`.” | This package is not a legal-personhood claim. |

---

## 3. Allowed claims

The following claims are acceptable if kept narrow.

| Allowed claim | Condition |
|---|---|
| The corpus is architecture-aligned with Article 50 transparency direction. | Must include “formal compliance is deployment-specific.” |
| L4 Witness can support audit evidence. | Must not be presented as user notice or legal proof. |
| CLI Agent Mesh can support AI-assisted workflow provenance. | Must include task contract, witness, human gate, and non-certification boundary. |
| `c = a + b` helps separate human anchor, technological substrate, and entity/workflow behavior. | Must not claim legal personhood or regulatory approval. |
| Beacon / AGL / ARL can support attribution, grounding, and dispute review. | Must not claim safety or compliance without implementation evidence. |
| A system should map role → obligation → control → evidence. | Should be presented as a proposed implementation discipline. |
| Metadata and provenance are useful for Article 50 implementation. | Must include visible disclosure where required. |
| Human review and editorial responsibility can affect disclosure handling. | Must be documented with reviewer, scope, and responsibility. |

---

## 4. Legal status of this package

This package is:

```text
technical policy contribution
draft compliance mapping
evidence-chain proposal
submission support material
```

This package is not:

```text
legal advice
legal opinion
conformity assessment
provider documentation
deployer declaration
DPIA
GDPR compliance report
AI Act full compliance report
product certification
safety certification
child-safety certification
cybersecurity certification
```

Any later use for a concrete deployment must be reviewed separately.

---

## 5. Role classification open issue

Article 50 obligations are role-dependent.

The package cannot classify the author, repository, or future systems under one single role.

Each concrete use case must be classified separately.

| Use case | Possible role | Review status |
|---|---|---|
| Public protocol publication | Protocol author / researcher | Low direct Article 50 deployment relevance; still useful as policy contribution. |
| AI-assisted public post | Author / editor / deployer-publisher context | Needs publication-specific review. |
| Generated media publication | Deployer / publisher / editor | Needs media-type and deepfake-risk review. |
| CLI-agent assisted release | Agent operator / author / publisher | Needs provenance and human gate review. |
| Enterprise `c` in business workflow | Enterprise operator / deployer | Needs legal, employment, GDPR, data-flow review. |
| Child-facing CCDP implementation | Provider/deployer depending implementation | High-sensitivity; needs specialist and legal review. |
| Public website / diary / publications | Author / publisher / editor | Needs AI-assisted publication disclosure policy. |

Open issue:

```text
A50-LR-001: Produce role classification memo for each concrete deployment before any compliance claim.
```

---

## 6. System boundary open issue

The Article 50 package must not describe “the project” as one system.

The project contains many layers:

- public theory;
- public repositories;
- DOI releases;
- narrative books;
- website publications;
- AI-assisted drafting workflows;
- CLI/cloud agent governance;
- possible enterprise systems;
- possible child-facing systems;
- local/private `c` systems;
- future deployment-specific products.

Each has different legal status.

Open issue:

```text
A50-LR-002: Produce separate system boundary declarations before applying Article 50 obligations.
```

Minimum system boundary fields:

```text
system_name
version
owner/operator
public/private/internal
user class
AI interaction mode
generated content mode
human review mode
publication mode
data categories
jurisdiction
```

---

## 7. Provider / deployer open issue

A single person or organisation may act as:

- researcher;
- author;
- protocol publisher;
- deployer;
- enterprise operator;
- editorial publisher;
- agent operator.

These roles may overlap in practice.

They should not be collapsed in the submission.

Open issue:

```text
A50-LR-003: For each workflow, determine whether the author acts as protocol author, deployer, publisher, agent operator, enterprise operator, or another legally relevant role.
```

Legal review required:

```text
yes
```

---

## 8. Human review and editorial responsibility open issue

Human review is not a magic exception.

A serious human review record should include:

```text
reviewer identity
review date
artifact reviewed
scope of review
what AI assistance was used
what was changed by the human
publication decision
editorial responsibility statement
correction path
```

Open issue:

```text
A50-LR-004: Define standard human review record for AI-assisted public publications and regulatory submissions.
```

Risk:

```text
“human-reviewed” becomes decorative if reviewer, scope, and responsibility are not recorded.
```

---

## 9. Machine-readable marking open issue

The package references machine-readable marking and provenance.

It does not yet select one final marking method for all content types.

Possible marking routes include:

- C2PA or equivalent provenance metadata;
- embedded metadata;
- watermarking where appropriate;
- JSON sidecar metadata;
- release manifest;
- hash-based artifact integrity;
- visible disclosure when metadata may be stripped.

Open issue:

```text
A50-LR-005: Select marking / metadata method per artifact type: Markdown, PDF, web page, image, audio, video, code release, dataset, and generated report.
```

Legal and technical review required:

```text
yes
```

---

## 10. Deepfake and generated media open issue

Generated images, covers, illustrations, audio, or video may require different treatment depending on whether they:

- are clearly illustrative;
- resemble real people;
- imitate a real voice;
- depict real events;
- may mislead a viewer into believing they are authentic;
- are used in public-interest context.

Open issue:

```text
A50-LR-006: Define generated media disclosure policy and deepfake-risk review checklist.
```

Minimum review fields:

```text
media_type
real_person_likeness
real_place_or_event_likeness
voice_or_face_imitation
public_interest_context
visible_label_required
metadata_required
human_review_completed
```

---

## 11. Public-interest publication open issue

Article 50 includes obligations around AI-generated or manipulated text published to inform the public on matters of public interest, subject to conditions and exceptions.

The package cannot determine automatically whether every article, diary entry, post, or technical document is a public-interest publication.

Open issue:

```text
A50-LR-007: Define public-interest publication classification checklist.
```

Candidate criteria:

- topic concerns public policy, AI safety, regulation, rights, risk, public institutions, or social impact;
- publication targets the general public or professional public;
- text is materially AI-generated or AI-assisted;
- human editorial responsibility exists and is documented;
- disclosure is visible where required or prudent.

Legal review required:

```text
yes
```

---

## 12. Emotion recognition open issue

The corpus contains emotional, state, dependency, soft safety, and affective terminology in some contexts.

That does not automatically mean the system performs legally relevant emotion recognition.

However, the boundary must be reviewed carefully.

Open issue:

```text
A50-LR-008: Distinguish emotional style adaptation, state signaling, dependency audit, and legally relevant emotion recognition.
```

Negative declaration is allowed only if technically true:

```text
This system does not perform emotion recognition.
```

But where the system infers or categorises emotions from natural persons, legal review is required.

Risk:

```text
Architectural language about emotion may be misread as an implemented emotion-recognition system.
```

---

## 13. Biometric categorisation open issue

The Article 50 package does not claim that biometric categorisation is used.

If a future system uses:

- face analysis;
- voice identity;
- gait;
- body features;
- biometric templates;
- demographic or sensitive categorisation from biometric data;

then separate legal review is mandatory.

Open issue:

```text
A50-LR-009: Add explicit negative declaration or technical boundary for biometric categorisation in each concrete system.
```

---

## 14. Worker / enterprise deployment open issue

An enterprise `c` in a construction or operational company may involve:

- workers;
- clients;
- subcontractors;
- safety instructions;
- work quality records;
- photos from sites;
- documents;
- scheduling;
- material advice;
- possible AI interaction.

This may trigger more than Article 50:

- GDPR;
- employment law;
- workplace surveillance rules;
- safety obligations;
- client confidentiality;
- liability and professional responsibility;
- sectoral rules.

Open issue:

```text
A50-LR-010: Enterprise c deployment requires separate Belgian/EU legal review, worker notice, data-flow mapping, and internal policy.
```

Article 50 transparency mapping is necessary but not sufficient.

---

## 15. Child-facing deployment open issue

CCDP is not the main submission surface for this Article 50 package.

Reason:

```text
child-facing persistent AI safety
  >
Article 50 transparency
```

Child-facing systems require:

- child-development review;
- education review;
- legal/compliance review;
- privacy/security review;
- jurisdictional review;
- conformance tests;
- red-team review using synthetic fixtures only;
- safe release split between public, technical, restricted, and internal files.

Open issue:

```text
A50-LR-011: Do not present CCDP as Article 50 compliance. Present it only as a high-sensitivity future extension and evidence of state-not-content, handoff, and non-surveillance discipline.
```

---

## 16. CLI Agent Mesh legal boundary

C-Governed CLI Agent Mesh can support provenance for AI-assisted executable workflows.

It can provide:

- task contracts;
- permission scopes;
- sandbox records;
- witness events;
- human gates;
- rollback and review;
- no silent autonomy.

It cannot by itself provide:

- Article 50 certification;
- legal compliance;
- safe deployment;
- user-facing disclosure;
- provider/deployer classification;
- sector-specific legal compliance.

Open issue:

```text
A50-LR-012: Define how CLI Agent Mesh witness records connect to publication disclosure and human editorial responsibility records.
```

---

## 17. Data protection and privacy open issue

Article 50 transparency is not the whole data protection problem.

Any concrete system may also require review under:

- GDPR;
- ePrivacy where relevant;
- employment privacy rules;
- child data protection rules;
- data minimisation requirements;
- retention and deletion policy;
- cross-border transfer rules;
- vendor/cloud data processing terms.

Open issue:

```text
A50-LR-013: Create separate data-flow and data-protection review for any deployed system.
```

This package does not perform that review.

---

## 18. Security and dual-use open issue

Some corpus layers involve:

- CLI/cloud agents;
- tool execution;
- sandboxing;
- secrets;
- privilege escalation prevention;
- witness/audit records;
- defensive containment;
- generated code;
- release automation.

These are legitimate governance topics.

They must not be converted into:

- offensive automation;
- malware;
- credential extraction;
- unauthorized system access;
- hack-back;
- evasion instructions;
- uncontrolled autonomous action.

Open issue:

```text
A50-LR-014: Security review required before any executable-agent deployment or publication of operational details.
```

Submission posture:

```text
defensive governance only
no offensive operationalization
no silent autonomy
no secrets exposure
```

---

## 19. Evidence sufficiency open issue

The package currently proposes evidence types.

It does not yet contain final evidence for a concrete system.

Open issue:

```text
A50-LR-015: For each concrete system, collect evidence pack before claiming readiness.
```

Minimum evidence pack:

```text
role classification memo
system boundary declaration
UI disclosure screenshot
sample generated output with disclosure
sample metadata / mark
sample witness event
human review record
editorial responsibility statement
release manifest / SHA
correction path
legal review memo
```

---

## 20. Submission-channel open issue

The official consultation channel is an online questionnaire.

This package is not submitted merely by preparing Markdown files.

Open issue:

```text
A50-LR-016: Convert this package into a concise EUSurvey response and submit through the official consultation questionnaire before the deadline.
```

Supporting documents may be linked or attached only if the questionnaire permits.

The final answer must be short enough to be read.

---

## 21. Publication order open issue

Recommended publication order:

```text
draft internal package
  -> human review
  -> legal/claim review
  -> PDF generation
  -> GitHub release
  -> Zenodo DOI if appropriate
  -> EUSurvey submission
  -> archive submitted text
```

Do not publish a DOI package if the claims are not stable.

Open issue:

```text
A50-LR-017: Decide whether this package should receive DOI before or after EUSurvey submission.
```

Recommended default:

```text
GitHub first, DOI after final freeze.
```

---

## 22. Claim strength classification

| Claim class | Meaning | Allowed now? |
|---|---|---|
| `A50-C0` | Idea / draft note. | Yes |
| `A50-C1` | Architecture-aligned mapping. | Yes |
| `A50-C2` | Candidate control proposal. | Yes |
| `A50-C3` | Evidence model proposal. | Yes |
| `A50-C4` | Implementation-ready for a named system. | Not yet |
| `A50-C5` | Legally reviewed deployment mapping. | Not yet |
| `A50-C6` | Formal compliance claim. | Not allowed in this package |
| `A50-C7` | Certification / conformity assessment. | Not allowed |

Current package maximum claim:

```text
A50-C3 — evidence model proposal
```

Not higher.

---

## 23. Review checklist

Before submission, check:

```text
[ ] No claim of formal compliance
[ ] No claim of certification
[ ] No claim that witness replaces disclosure
[ ] No claim that metadata replaces visible notice
[ ] No claim that CLI Agent Mesh itself is Article 50 compliant
[ ] Provider/deployer distinction preserved
[ ] Human review defined as recorded responsibility, not decoration
[ ] CCDP kept secondary and high-sensitivity
[ ] Legal review items clearly marked
[ ] Official EUSurvey submission path identified
[ ] Package is short enough for policy review
[ ] Public links are stable
[ ] No private or sensitive implementation details exposed
```

---

## 24. A/B language slots

### Slot A — strict official wording

```text
This submission does not claim formal Article 50 compliance. It provides a technical evidence-chain mapping for implementation discussion: system boundary, actor role, transparency trigger, disclosure or marking control, evidence artifact, responsible actor, and legal review path.
```

### Slot B — plain explanation

```text
The point is not to say “we are compliant.” The point is to show what a serious transparency claim should contain: what system is involved, who is responsible, what duty is triggered, what notice or mark is used, what evidence exists, and what still needs legal review.
```

Use Slot A for the consultation.

---

## 25. Explicit bridge

The explicit bridge is:

```text
Article 50 transparency is legal and procedural.
The corpus contributes architecture and evidence discipline.
The bridge is valid only when the architecture is attached to a concrete system, role, obligation, control, evidence artifact, and responsible actor.
```

This prevents both underclaim and overclaim.

---

## 26. Quiet bridge I — Ashby

A system with many modes of action requires many modes of control.

A single statement cannot cover:

- AI interaction;
- text generation;
- generated images;
- deepfake risk;
- public-interest publication;
- executable agents;
- human review;
- release automation;
- enterprise workflows;
- child-facing systems.

The compliance apparatus must have enough variety to match the system variety.

This is why the package uses matrices instead of one declaration.

---

## 27. Quiet bridge II — information theory

Compliance evidence should transmit enough information to support review.

It should not transmit everything.

The correct compression is:

```text
enough signal for legal review
enough signal for public disclosure
enough signal for technical audit
minimal raw private leakage
```

A good evidence pack is not a data dump.

It is a controlled channel.

---

## 28. Earth paragraph — inspection boundary

In construction, a technical drawing is not a permit.

A permit is not a finished wall.

A finished wall is not an inspection certificate.

An inspection certificate is not a guarantee that nobody will ever misuse the building.

Each document has a boundary.

The same is true here.

The architecture explains the design.

The evidence pack shows what happened.

The legal review checks obligations.

The submission gives policy input.

Mixing these layers creates false confidence.

False confidence is worse than an open issue.

---

## 29. Final non-claim statement

The final non-claim statement for the whole package is:

```text
This Article 50 package is a technical, architecture-aligned, evidence-oriented contribution to transparency implementation. It is not legal advice, not certification, not a conformity assessment, and not a claim that any deployed system is compliant. Formal compliance requires concrete system definition, role classification, disclosure and marking implementation, evidence collection, responsible human review, and qualified legal review.
```

This statement should appear in the final package and in any PDF or release notes.

---

## 30. References

Official sources:

1. European Commission, consultation on draft guidelines on transparency obligations under the AI Act:
   https://digital-strategy.ec.europa.eu/en/consultations/consultation-draft-guidelines-transparency-obligations-under-ai-act

2. European Commission, draft guidelines on implementation of transparency obligations for certain AI systems under Article 50 of the AI Act:
   https://digital-strategy.ec.europa.eu/en/library/draft-guidelines-implementation-transparency-obligations-certain-ai-systems-under-article-50-ai-act

3. European Commission / AI Office, Code of Practice on marking and labelling of AI-generated content:
   https://digital-strategy.ec.europa.eu/en/policies/code-practice-ai-generated-content

Public technical source:

4. Kotov Ivan, C-Governed CLI Agent Mesh v0.1.1:
   https://github.com/Kot141078/c-governed-cli-agent-mesh

5. DOI / Zenodo archive for C-Governed CLI Agent Mesh v0.1.1:
   https://doi.org/10.5281/zenodo.20257232

---

## 31. Final control rule

Do not move from:

```text
architecture-aligned
```

to:

```text
compliant
```

without:

```text
named system
role classification
implemented disclosure
implemented marking/provenance
evidence artifact
responsible actor
legal review
```

That is the safety rail for the Article 50 package.
