# System / Role / Obligation / Control / Evidence Table v0.1

**Author:** Kotov Ivan
**Location:** Bruxelles, Belgium
**Date:** 2026-05-19
**Document ID:** `Article50_System_Role_Obligation_Control_Evidence_Table_v0_1`
**Package:** `Article50_Transparency_Submission_v0_1`
**Status:** Draft technical evidence table
**Intended channel:** European Commission / AI Office consultation on draft Article 50 transparency guidelines
**Legal status:** Not legal advice. Not certification. Not a conformity assessment.
**Primary posture:** system-boundary first; role-specific; evidence-oriented; deployment-specific; subject to legal review.

---

## 0. Executive purpose

This document is the table-first operational core of the Article 50 submission package.

It translates broad transparency obligations into a repeatable engineering chain:

```text
system
  -> role
  -> obligation trigger
  -> control
  -> evidence artifact
  -> responsible actor
  -> legal review item
```

It is designed for review by policy, legal, compliance, and technical readers.

The document intentionally avoids claiming that any existing corpus artifact is compliant by itself.

It answers a narrower question:

> If a concrete system or AI-assisted workflow were reviewed under Article 50 transparency obligations, what evidence chain should be shown?

---

## 1. Use rule

Use this table only after a concrete system or workflow is named.

Do not use it to claim corpus-level compliance.

The minimum input is:

```text
system name
system boundary
actor role
user or affected person class
AI interaction or generated-content trigger
publication / deployment context
```

Without those inputs, the result is:

```text
mapping incomplete
formal compliance not assessable
```

---

## 2. Evidence vocabulary

| Evidence class | Meaning | Example |
|---|---|---|
| `EV-DISCLOSURE` | Human-visible disclosure | UI banner, modal, post notice, document front matter. |
| `EV-MARK` | Machine-readable mark | C2PA record, embedded metadata, watermark, detectable marker. |
| `EV-META` | Documentary metadata | JSON sidecar, YAML front matter, provenance header. |
| `EV-WITNESS` | Tamper-evident event record | L4 Witness event, signed event, hash-linked event. |
| `EV-CONTRACT` | AI-agent task contract | CLI Agent Mesh contract, bounded scope, permissions. |
| `EV-LOG` | Operational log | Generation log, user-notice log, tool-call log. |
| `EV-HUMAN-REVIEW` | Human review evidence | Reviewer, date, scope, outcome, editorial responsibility. |
| `EV-RELEASE` | Release integrity evidence | SHA256SUMS, tag, DOI, release notes, manifest. |
| `EV-POLICY` | Policy or procedure | Disclosure policy, takedown procedure, internal AI use policy. |
| `EV-LEGAL` | Legal review artifact | Counsel memo, DPIA, role classification memo, jurisdictional review. |
| `EV-NEGATIVE` | Negative functional declaration | “No emotion recognition”, “No biometric categorisation”, “No autonomous publication”. |
| `EV-DRILL` | Test or simulation record | Controlled scenario, red-team drill, replay, conformance test. |

---

## 3. Responsible actor vocabulary

| Actor | Meaning |
|---|---|
| `AUTHOR` | Kotov Ivan as author of the submitted package or public publication. |
| `EDITOR` | Human editor responsible for publication acceptance. |
| `PROTOCOL_AUTHOR` | Author of architecture, protocol, or schema. |
| `PROVIDER` | Actor responsible for provider-side AI system obligations, where applicable. |
| `DEPLOYER` | Actor using an AI system under its authority, where applicable. |
| `ENTERPRISE_OPERATOR` | Organisation or business operating a concrete workflow. |
| `AGENT_OPERATOR` | Human or organisation authorising CLI/cloud agents. |
| `LEGAL_REVIEWER` | Counsel or qualified legal/compliance reviewer. |
| `AUDITOR` | Internal or external technical reviewer. |
| `USER` | Natural person interacting with or exposed to the AI system/output. |

---

## 4. System-role table

| System / workflow | Boundary | Likely role(s) | Article 50 relevance | Primary evidence needed | Compliance posture |
|---|---|---|---|---|---|
| Public `c = a + b` corpus | Published Markdown/PDF/DOI protocols and explanatory materials. | `PROTOCOL_AUTHOR`, `RESEARCHER` | Indirect: provides architectural transparency patterns. | `EV-RELEASE`, `EV-META`, non-claim boundary. | Architecture-aligned; not a deployed AI system by itself. |
| L4 Witness layer | Witness / audit / event evidence discipline. | `PROTOCOL_AUTHOR`, possible `PROVIDER`/`DEPLOYER` component if implemented. | Supports auditability and traceability. | `EV-WITNESS`, schema, sample event, privacy class. | Candidate evidence control; not user disclosure by itself. |
| Beacon / identity / attribution layer | Recognition and attribution of entity/tool/oracle/proxy/replay-style claims. | `PROTOCOL_AUTHOR`, implementation-dependent. | Supports actor/source attribution. | Beacon record, challenge record, attribution map. | Supports transparency; not compliance alone. |
| Actor Grounding Layer / AGL | Source-state qualification before reliance. | `PROTOCOL_AUTHOR`, implementation-dependent. | Helps prevent ungrounded AI/source claims being relied upon. | Source-state log, route/liveness record. | Candidate control for provenance and reliance. |
| ARL / review / freeze / quarantine | Dispute and review routing. | `PROTOCOL_AUTHOR`, implementation-dependent. | Supports correction, contestability, and review. | Review intake, freeze record, outcome note. | Review layer; not a regulator or court. |
| C-Governed CLI Agent Mesh | Governance of executable CLI/cloud agents under persistent `c` governance. | `PROTOCOL_AUTHOR`, `AGENT_OPERATOR`; possibly deployer component if used. | Relevant to AI-assisted workflows and generated artifacts. | `EV-CONTRACT`, `EV-WITNESS`, sandbox record, human gate. | Strong evidence bridge; not Article 50 compliance by itself. |
| AI-assisted public post workflow | Drafting, editing, image generation, publication. | `AUTHOR`, `EDITOR`, possibly `DEPLOYER`/publisher. | May trigger AI-generated public-interest disclosure or generated media labeling. | Visible disclosure, human review record, metadata. | Deployment/publication-specific. |
| AI-assisted technical submission | Use of AI to draft regulatory/policy documents. | `AUTHOR`, `EDITOR`, possibly `AGENT_OPERATOR`. | Transparency relevance if published or submitted with AI assistance. | Editorial responsibility, provenance note, task logs. | Requires clear human responsibility. |
| Generated image workflow | AI-generated or manipulated images. | `DEPLOYER`, `AUTHOR`, `EDITOR`. | Deepfake/synthetic content marking/disclosure where applicable. | Visible label, metadata, generation record. | Depends on content type and authenticity risk. |
| Enterprise `c` for business operations | Internal worker/client/document workflow. | `ENTERPRISE_OPERATOR`, possible `DEPLOYER`. | User/worker/client transparency may be relevant. | Internal notice, policy, logs, legal review. | Requires employment/GDPR/legal review. |
| Child-facing CCDP system | Persistent AI near a child, school, toy, or generated media system. | `DEPLOYER`, possibly `PROVIDER`; high-sensitivity. | Article 50 may apply but is not sufficient. | Specialist review, legal review, conformance tests, state-not-content evidence. | Not suitable as primary Article 50 submission surface. |

---

## 5. Article 50 obligation-to-evidence table

| ID | Obligation area | Trigger | Role | Control | Evidence artifact | Responsible actor | Legal review item |
|---|---|---|---|---|---|---|---|
| A50-001 | AI interaction disclosure | Natural person interacts with an AI system. | `PROVIDER` / `DEPLOYER` | Clear notice before or during interaction. | `EV-DISCLOSURE`, screenshot, UI copy version. | `PROVIDER` / `DEPLOYER` | Whether system is in scope and notice timing is sufficient. |
| A50-002 | Generative AI machine-readable marking | AI system generates or manipulates audio, image, video, or text. | `PROVIDER` | Machine-readable mark or provenance mechanism. | `EV-MARK`, `EV-META`, detection sample. | `PROVIDER` | Whether method is effective, interoperable, robust, technically feasible. |
| A50-003 | Deepfake disclosure | Generated/manipulated image/audio/video resembles authentic persons, objects, places, entities, or events. | `DEPLOYER` / publisher | Visible disclosure to exposed persons or audience. | `EV-DISCLOSURE`, media metadata, review record. | `DEPLOYER`, `EDITOR` | Whether exceptions apply; whether content qualifies as deepfake. |
| A50-004 | AI-generated public-interest publication disclosure | AI-generated/manipulated text informs public on matters of public interest. | `DEPLOYER` / publisher | Disclosure unless human review and editorial responsibility apply. | Publication note, `EV-HUMAN-REVIEW`, editorial statement. | `EDITOR`, `AUTHOR` | Whether publication is public-interest; sufficiency of review/responsibility. |
| A50-005 | Human review / editorial responsibility | Human review is used as part of the disclosure logic. | `EDITOR`, `AUTHOR`, `DEPLOYER` | Named reviewer, scope, outcome, correction route. | `EV-HUMAN-REVIEW`, `EV-POLICY`, release note. | `EDITOR`, `AUTHOR` | Whether review process is real, documented, and sufficient. |
| A50-006 | Emotion recognition notice | System performs emotion recognition where Article 50 applies. | `PROVIDER` / `DEPLOYER` | Explicit notice or negative declaration if absent. | `EV-DISCLOSURE` or `EV-NEGATIVE`, DPIA/legal review. | `PROVIDER` / `DEPLOYER` | Whether functionality counts as emotion recognition. |
| A50-007 | Biometric categorisation notice | System performs biometric categorisation where Article 50 applies. | `PROVIDER` / `DEPLOYER` | Explicit notice or negative declaration if absent. | `EV-DISCLOSURE` or `EV-NEGATIVE`, data flow. | `PROVIDER` / `DEPLOYER` | Whether biometric categorisation exists and is lawful. |
| A50-008 | User-accessible clarity | Disclosure must be understandable to natural persons. | All relevant actors | Short plain-language notice, not raw internal logs. | UI text, UX/legal review. | `PROVIDER` / `DEPLOYER` / `EDITOR` | Whether wording is clear, timely, and non-misleading. |
| A50-009 | Provenance support | Generated output or AI-assisted publication requires traceability. | Mixed | Metadata, witness, source-state, task record. | `EV-META`, `EV-WITNESS`, `EV-CONTRACT`. | `AGENT_OPERATOR`, `EDITOR` | Retention, privacy, and disclosure boundaries. |
| A50-010 | Correction and dispute path | Disclosure, marking, or provenance is contested or wrong. | Mixed | Correction/takedown/review workflow. | `EV-POLICY`, correction log, ARL-style review. | `EDITOR`, `DEPLOYER`, `LEGAL_REVIEWER` | Required correction timing and legal duty. |

---

## 6. Control-to-evidence detail table

| Control | Minimum acceptable evidence | Stronger evidence | Failure mode if missing |
|---|---|---|---|
| AI interaction notice | Screenshot of notice in user flow. | Versioned UI copy + log showing notice displayed. | User may not know they interact with AI. |
| Publication disclosure | Visible note in post/document/page. | Front matter + rendered page + archive hash. | Public cannot distinguish human-only from AI-assisted content. |
| Machine-readable mark | Embedded metadata or sidecar. | C2PA or equivalent + detection test + hash. | Synthetic content may be stripped from provenance chain. |
| Human editorial review | Reviewer name/role + timestamp + scope. | Signed review note + release gate + correction route. | “Human reviewed” becomes decorative. |
| CLI task contract | Agent task file with scope and permissions. | Contract + sandbox path + witness + review gate. | Executable agent work becomes invisible. |
| L4 Witness event | Event ID + timestamp + actor + action + hash. | Chain-linked witness event + privacy class + resolution note. | Privileged transition cannot be audited. |
| Source grounding | Source/actor/route record. | AGL record with freshness, route, liveness, and reliance state. | Ungrounded AI or proxy claim may drive publication/action. |
| Release integrity | SHA manifest or release tag. | SHA + signed tag + DOI + release notes. | Artifact can change without trace. |
| Negative sensitive-function declaration | Statement of absence. | Technical configuration + audit log + legal review. | Readers may assume emotion/biometric functions are absent without proof. |
| Correction path | Policy text. | Correction log + owner + response time + witness record. | Wrong label/metadata cannot be repaired visibly. |

---

## 7. System-specific table templates

### 7.1 Public protocol repository

| Field | Entry |
|---|---|
| System | Public protocol repository. |
| Boundary | Markdown/PDF/metadata/release artifacts only. |
| Role | `PROTOCOL_AUTHOR` / `RESEARCHER`. |
| Article 50 trigger | Usually indirect unless repository itself contains AI-generated content or interactive AI functionality. |
| Control | Non-claim boundary, stable release, DOI/SHA, authorship, references. |
| Evidence | `EV-RELEASE`, `EV-META`, `EV-POLICY`. |
| Responsible actor | `AUTHOR`. |
| Legal issue | Avoid presenting protocol publication as deployed-system compliance. |

### 7.2 AI-assisted public post or article

| Field | Entry |
|---|---|
| System | AI-assisted public publication workflow. |
| Boundary | Drafting, editing, image generation, human review, publication. |
| Role | `AUTHOR`, `EDITOR`, possible `DEPLOYER`. |
| Article 50 trigger | AI-generated/manipulated public-interest text or generated media, depending content. |
| Control | Visible AI assistance note where required; human editorial responsibility. |
| Evidence | Publication front matter, review record, metadata, generated media label. |
| Responsible actor | `AUTHOR` / `EDITOR`. |
| Legal issue | Determine whether the publication concerns matters of public interest and whether human review/editorial responsibility exception applies. |

### 7.3 AI-generated image

| Field | Entry |
|---|---|
| System | AI-generated image workflow. |
| Boundary | Prompt, model/tool, generated file, editing, publication. |
| Role | `AUTHOR`, `DEPLOYER`, possible publisher. |
| Article 50 trigger | Synthetic or manipulated image; deepfake if it falsely appears authentic/truthful. |
| Control | Visible label and/or metadata depending context. |
| Evidence | Generation record, metadata, visible label, review note. |
| Responsible actor | `AUTHOR` / `EDITOR`. |
| Legal issue | Whether it resembles real persons/places/events and whether disclosure must be visible. |

### 7.4 CLI-agent assisted release

| Field | Entry |
|---|---|
| System | CLI/cloud agent prepares repository changes, release notes, metadata, or package. |
| Boundary | Task contract, worktree, file edits, validation, human review, release. |
| Role | `AGENT_OPERATOR`, `AUTHOR`, possibly `DEPLOYER` for workflow. |
| Article 50 trigger | Indirect unless output is public AI-generated/assisted content or AI system interaction is user-facing. |
| Control | Contract, permissions, sandbox, witness, human gate, release integrity. |
| Evidence | `EV-CONTRACT`, `EV-WITNESS`, `EV-HUMAN-REVIEW`, `EV-RELEASE`. |
| Responsible actor | `AGENT_OPERATOR` / `AUTHOR`. |
| Legal issue | Distinguish internal tool execution from public transparency obligations; preserve provenance. |

### 7.5 Enterprise worker-facing `c`

| Field | Entry |
|---|---|
| System | Enterprise/work-bound `c` used in company operations. |
| Boundary | Worker interface, document workflow, safety notices, task routing, logs. |
| Role | `ENTERPRISE_OPERATOR`, possible `DEPLOYER`. |
| Article 50 trigger | Workers or clients interact with or are affected by AI-assisted system. |
| Control | Worker/client notice, policy, human oversight, logs, escalation. |
| Evidence | UI notice, policy, access logs, review records, legal review. |
| Responsible actor | `ENTERPRISE_OPERATOR`. |
| Legal issue | Employment law, GDPR, DPIA, workplace surveillance, data minimisation. |

---

## 8. Negative declarations table

A useful submission should also say what is **not** being claimed or performed.

| Declaration | Meaning | Evidence |
|---|---|---|
| No formal compliance claim | The package maps controls; it does not certify compliance. | Non-claim section, cover note. |
| No autonomous publication | AI/agent outputs require human approval before public release. | Human gate, release record. |
| No emotion recognition by default | State or tone adaptation is not automatically emotion recognition. | Technical description, legal review if needed. |
| No biometric categorisation by default | No face/voice/body categorisation unless explicitly implemented. | Technical configuration, data-flow declaration. |
| No child-facing deployment in this Article 50 submission | CCDP is referenced as high-sensitivity architecture, not deployed system evidence. | Scope statement. |
| No vendor telemetry by default | Private memory or witness records are not ordinary vendor analytics. | Data flow, policy, implementation evidence. |
| No legal personhood claim | `c = a + b` is not submitted as a legal-personhood claim. | Cover note, non-claim boundary. |

---

## 9. EUSurvey-ready condensed table

This shorter table can be converted into survey answers.

| Question | Submission answer |
|---|---|
| What is the contribution? | A practical evidence-chain mapping for Article 50 transparency implementation. |
| What problem does it address? | Transparency claims often lack system boundary, role, control, evidence, and responsible actor. |
| What is proposed? | Map every transparency obligation to visible disclosure, machine-readable marking/provenance, witness/audit evidence, and human responsibility. |
| What technical layers support it? | `c = a + b`, L4 Witness, Beacon, AGL, ARL, C-Governed CLI Agent Mesh. |
| Is compliance claimed? | No. The package is architecture-aligned and deployment-specific, not a conformity assessment. |
| What evidence is recommended? | UI notice, metadata, witness event, task contract, human review record, release integrity, correction path. |
| Why is this useful? | It makes Article 50 implementation testable rather than declarative. |

---

## 10. Explicit bridge

The explicit bridge is:

```text
Article 50 asks whether people are informed and whether generated content can be marked or disclosed.
The corpus asks whether actions, identities, sources, and publications can be bounded, grounded, witnessed, and reviewed.
The shared implementation problem is evidence.
```

Therefore:

```text
transparency without evidence = policy decoration
evidence without disclosure = internal compliance theatre
disclosure without responsibility = label without owner
```

A serious Article 50 implementation needs all three.

---

## 11. Quiet bridge I — information theory

The table separates human-facing and machine-facing signals.

Reason:

```text
a user needs understandable disclosure;
a machine needs detectable structure;
an auditor needs evidence;
a legal reviewer needs responsibility and scope.
```

One signal cannot serve all four audiences well.

This is a channel-design problem, not a wording problem.

---

## 12. Quiet bridge II — cybernetic control

Every control in the table should close a loop.

| Loop component | Article 50 analogue |
|---|---|
| Sensor | User notice, metadata, witness record. |
| Comparator | Human/legal review against obligation. |
| Actuator | Label, correction, takedown, refusal, rollback. |
| Memory | Audit log, release manifest, witness chain. |
| Responsible controller | Human or organisation. |

If a control has no feedback path, it is not a control.

It is a statement.

---

## 13. Earth paragraph — invoice, toolbox, and signature

On a real job site, a worker can have good tools and still do bad work.

A label on a box does not prove the job was done.

An invoice does not prove the wiring is safe.

A signature without inspection is theatre.

The useful chain is:

```text
work order
  -> tool used
  -> inspected result
  -> responsible signature
  -> correction route if something fails
```

AI transparency needs the same discipline.

The model is the tool.

The output is the work.

The disclosure is the label.

The witness record is the inspection trail.

The human review is the signature.

---

## 14. Minimal implementation checklist

For a concrete system, require:

```text
[ ] System boundary defined
[ ] Actor role classified
[ ] Article 50 trigger identified
[ ] User-facing notice drafted
[ ] Machine-readable marking selected where applicable
[ ] Provenance metadata defined
[ ] Witness/audit event defined
[ ] Human review gate defined
[ ] Responsible human or organisation named
[ ] Correction / takedown / rollback route defined
[ ] Legal review item recorded
```

If any item is missing:

```text
do not claim compliance
```

---

## 15. Red flags

| Red flag | Why it matters |
|---|---|
| “The system is transparent because we publish our philosophy.” | Publication is not user-facing disclosure. |
| “The system logs everything.” | Logs may create surveillance and still fail to inform users. |
| “The metadata is enough.” | Metadata may be stripped or invisible to natural persons. |
| “A human was involved.” | Involvement is not the same as documented review and responsibility. |
| “The AI did not decide, it only suggested.” | AI-assisted workflows may still affect public content, users, workers, or clients. |
| “The agent only changed files locally.” | Local changes may become public through release or publication. |
| “The user can ask if it is AI.” | Transparency should not depend on interrogation by the user. |
| “The repo has a DOI.” | DOI supports integrity, not legal compliance. |
| “The protocol is safe for children.” | Child-facing claims require specialist/legal review beyond Article 50. |

---

## 16. Final table rule

A system should not be described as Article 50-ready unless this row can be filled:

| System | Role | Trigger | Disclosure | Marking / provenance | Evidence | Responsible actor | Legal review |
|---|---|---|---|---|---|---|---|
| `...` | `...` | `...` | `...` | `...` | `...` | `...` | `...` |

If the row cannot be filled, the system may still be interesting.

It is not ready for a serious transparency claim.

---

## 17. References

Official sources:

- European Commission, consultation on draft guidelines on transparency obligations under the AI Act:
  https://digital-strategy.ec.europa.eu/en/consultations/consultation-draft-guidelines-transparency-obligations-under-ai-act

- European Commission / AI Office, Code of Practice on marking and labelling of AI-generated content:
  https://digital-strategy.ec.europa.eu/en/policies/code-practice-ai-generated-content

Public technical source:

- Kotov Ivan, C-Governed CLI Agent Mesh v0.1.1:
  https://github.com/Kot141078/c-governed-cli-agent-mesh

- DOI / Zenodo archive for C-Governed CLI Agent Mesh v0.1.1:
  https://doi.org/10.5281/zenodo.20257232

---

## 18. Final control statement

The operational standard proposed by this table is:

```text
No Article 50 transparency claim without:
  system boundary
  role classification
  trigger identification
  disclosure or marking control
  evidence artifact
  responsible actor
  legal review path
```

This is the minimum evidence chain for a serious transparency implementation.
