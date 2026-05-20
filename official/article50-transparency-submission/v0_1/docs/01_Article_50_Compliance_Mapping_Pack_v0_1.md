# Article 50 Compliance Mapping Pack v0.1

**Author:** Kotov Ivan
**Location:** Bruxelles, Belgium
**Date:** 2026-05-19
**Document ID:** `Article50_Compliance_Mapping_Pack_v0_1`
**Package:** `Article50_Transparency_Submission_v0_1`
**Status:** Draft technical compliance-mapping contribution
**Intended channel:** European Commission / AI Office consultation on draft Article 50 transparency guidelines
**Legal status:** Not legal advice. Not certification. Not a conformity assessment.
**Primary posture:** architecture-aligned, evidence-oriented, deployment-specific, subject to legal review.

---

## 0. Executive summary

This document maps selected Article 50 transparency obligation areas to concrete technical and procedural controls from the public `c = a + b / SER / L4 / Witness / AGL / ARL / CLI Agent Mesh` corpus.

The central claim is narrow:

> The corpus is strongly architecture-aligned with the direction of Article 50 transparency obligations, but formal compliance depends on the concrete deployed system, role classification, user interface disclosures, marking mechanisms, audit evidence, responsible human review, and legal review.

This document does not claim that a theory, protocol, repository, release, or AI-assisted workflow is compliant by itself.

It proposes a reviewable mapping pattern:

```text
system boundary
  -> actor role
  -> obligation trigger
  -> user-facing disclosure
  -> machine-readable marking or provenance
  -> witness / audit evidence
  -> responsible human or organisation
```

This chain is intended to help prevent a common implementation failure:

```text
general transparency language
  without
system scope, role, control, evidence, or accountable actor
```

---

## 1. Non-claim boundary

This mapping does **not** claim:

1. formal Article 50 compliance;
2. certification;
3. legal adequacy in any Member State;
4. provider or deployer status for every corpus component;
5. that open-source publication equals compliance;
6. that witness records replace user-facing disclosure;
7. that metadata alone is sufficient where visible disclosure is required;
8. that human review is meaningful without named responsibility;
9. that `c = a + b` creates a legal person;
10. that Article 50 is the only relevant AI Act, GDPR, employment, consumer, cybersecurity, or sectoral obligation.

The intended claim is:

```text
candidate compliance architecture;
not compliance conclusion.
```

---

## 2. Consultation context

The European Commission consultation on draft Article 50 transparency guidelines was published on 8 May 2026 and is open until 3 June 2026.

The stated aim is to help providers and deployers meet transparency requirements under Article 50 of the AI Act.

The Commission describes the obligations as covering, among other things:

- informing users when they interact with an AI system;
- implementing machine-readable marks in generative AI systems to enable detection of synthetic content as AI-generated or manipulated;
- informing people when they are exposed to deep fakes;
- informing people when they are exposed to AI-generated publications on matters of public interest;
- informing people about emotion recognition or biometric categorisation systems.

The transparency rules are scheduled to become applicable on 2 August 2026.

This mapping is written for that implementation layer.

---

## 3. Source corpus intake

This mapping was prepared after treating the available project material as a structured Markdown corpus, not as isolated attachments.

The available corpus archive contains 494 Markdown files across multiple repositories and corpus slices.

Relevant corpus groups include:

| Corpus group | Role in this mapping |
|---|---|
| `advanced-global-intelligence` | Root AGI / `c = a + b` / L4 / authorial and publication-control material. |
| `sovereign-entity-recursion` | SER, SER-FED, L4 Witness, ARL, continuity, federation, entity-governance layers. |
| `ester-reality-bound` | Actor grounding, reality-bound operational constraints, evidence discipline. |
| `ester-clean-code` | Executable implementation-adjacent layer and code-facing governance surface. |
| `kot141078.github.io` | Public web / publication / discoverability surface. |
| `advanced-global-intelligence_LOCAL_ONLY` | Local-only material, not treated as public submission evidence unless explicitly released. |
| `volume-i`, `volume-ii`, `volume-iii` and related book repositories | Public narrative/explanatory corpus; not primary Article 50 protocol evidence. |
| CCDP files provided separately in-session | Sensitive child-facing protocol layer; useful for state-not-content, handoff, conformance, but not the primary Article 50 submission surface. |
| `c-governed-cli-agent-mesh` public GitHub repository | Fresh public CLI/cloud agent governance layer, especially relevant to AI-assisted workflows, tool execution, provenance, witness, and human gates. |

Important packaging note:

```text
CCDP and child-facing materials should remain secondary in this Article 50 submission.
```

Reason:

```text
Article 50 transparency
  !=
full child-facing persistent AI safety.
```

---

## 4. Submission model

This document maps Article 50 implementation through six questions.

| Step | Question | Required output |
|---|---|---|
| 1 | What is the system? | A scoped AI system, AI-assisted workflow, publication pipeline, or protocol component. |
| 2 | What is the actor role? | Provider, deployer, researcher, protocol author, enterprise implementer, publisher/editorial actor, or mixed role. |
| 3 | What triggers the transparency obligation? | Interaction, generated content, deepfake, public-interest publication, emotion recognition, biometric categorisation, or other trigger. |
| 4 | What must the human see? | User-facing notice, publication disclosure, content label, or system explanation. |
| 5 | What must machines or auditors inspect? | Metadata, provenance, witness record, hash, review log, task contract, release manifest. |
| 6 | Who is responsible? | Named human or organisation with review, correction, escalation, or publication responsibility. |

This prevents the phrase “transparent AI” from becoming a decorative label.

---

## 5. Role classification matrix

Formal obligations depend on actor role. The same author or organisation may hold different roles in different contexts.

| Role | Description | Article 50 relevance | Required evidence before any compliance claim |
|---|---|---|---|
| Open-source protocol author | Publishes architectural protocols, schemas, documentation, or reference patterns. | Usually not enough by itself to create provider/deployer obligations for a concrete AI system, but may influence implementation practices. | Repository scope, license, non-claim boundary, versioned release, DOI/hash, statement that implementation-specific compliance is separate. |
| Researcher / independent contributor | Submits analysis, architecture patterns, or policy feedback. | Relevant as consultation input and technical contribution; not automatically a deployed-system role. | Author identity, submission scope, references, no certification claim, reproducible package. |
| Provider | Develops or places on the market an AI system, or has an AI system developed and places it under own name or trademark. | Potentially directly relevant to user interaction notice and machine-readable marking obligations. | Product/system definition, technical documentation, UI disclosure, marking method, evidence logs, compliance owner, legal review. |
| Deployer | Uses an AI system under its authority in a concrete context. | Relevant to disclosure obligations for AI interaction, deepfakes, AI-generated public-interest publications, emotion recognition, and biometric categorisation. | Use-case scope, deployment context, user notice, publication disclosure, human review, policy, logs, legal review. |
| Enterprise implementer | Configures AI-assisted workflows inside an organisation, including workers, clients, documents, or operational decisions. | Relevant where users/workers/clients interact with or are affected by AI-assisted outputs. | Internal policy, worker/user notice, boundaries, task contracts, human review, data protection review, audit logs. |
| Publisher / editorial actor | Publishes AI-generated or AI-assisted text, images, audio, video, or reports. | Relevant for public-interest publications and generated/manipulated content disclosures. | Editorial responsibility statement, human review record, content provenance, visible label, metadata, correction procedure. |
| CLI/cloud agent operator | Allows AI agents to execute tasks, modify files, call tools, generate releases, or prepare publications. | Relevant as an AI-assisted workflow and provenance/witness layer; obligation depends on downstream use. | Task contract, permission scope, sandbox, witness event, human gate, review before publication, rollback record. |
| Child-facing system operator | Deploys persistent AI near children or educational environments. | Article 50 may apply, but additional child, education, privacy, safety, and jurisdictional duties likely dominate. | Specialist review, jurisdictional review, state-not-content disclosure, no surveillance, conformance tests, legal review. |

### 5.1 Classification rule

Do not classify the whole corpus as one role.

Classify each concrete system or workflow separately.

Example:

```text
public Markdown protocol repository
  = protocol publication / research contribution

enterprise c used in a company
  = potential deployer / enterprise implementer context

AI-assisted public article pipeline
  = publication workflow / deployer-editorial context

CLI Agent Mesh controlling executable agents
  = governance layer for AI-assisted tool execution, not automatically the public-facing AI system
```

---

## 6. System boundary matrix

| System or workflow | Likely status | Article 50 relevance | Main risk of overclaim | Required next evidence |
|---|---|---|---|---|
| Public `c = a + b` corpus | Protocol / research publication | Supports transparency architecture; not a deployed AI system by itself. | Claiming compliance from theory alone. | Non-claim boundary, DOI/release, references, mapping table. |
| L4 Witness layer | Evidence / audit / witness discipline | Supports auditability and review of privileged transitions. | Treating logs as user disclosure. | Event schema, sample witness event, privacy class, verification method. |
| Beacon / identity / attribution layer | Identity and actor recognition pattern | Supports distinction between entity, tool, oracle, proxy, replay, clone, and continuity-bearing system. | Treating recognition as legal status or safety proof. | Challenge process, attribution record, system role mapping. |
| AGL / Actor Grounding Layer | Source-state qualification | Supports grounding before reliance on source, actor, route, or claim. | Treating grounding as full legal validation. | Source-state log, liveness/provenance record, review threshold. |
| ARL / review / freeze / quarantine | Dispute and review layer | Supports escalation, contested claims, freeze, re-entry, and review. | Treating ARL as court or regulator. | Intake record, standing rule, decision note, human reviewer. |
| CLI Agent Mesh | AI-assisted executable-agent governance layer | Highly relevant to provenance of AI-assisted outputs, code, releases, reports, and submissions. | Treating agent governance as Article 50 compliance by itself. | Task contract, permission scope, witness event, human approval gate. |
| Ester Clean Code | Implementation-adjacent software layer | May become relevant if deployed as a system or component. | Treating repository existence as deployment evidence. | System boundary, user interaction mode, logs, UI disclosure. |
| Enterprise `c` in a company | Potential deployed AI-assisted system | Relevant if workers, clients, or third parties interact with AI or are affected by AI-generated outputs. | Under-disclosing AI role in workplace workflows. | Internal notice, policy, data flow, human review, legal/DPIA review. |
| AI-assisted LinkedIn / website posts | AI-assisted publication workflow | Relevant where content is AI-generated or materially AI-assisted, especially public-interest matters. | Failing to disclose material AI generation/review boundary. | Editorial note, front matter, metadata, human review record. |
| Generated images / audio / video / book covers | Synthetic content workflow | Relevant to generated or manipulated content marking/disclosure. | Relying only on invisible metadata. | Visible label where required, metadata, generation record, human review. |
| CCDP child-facing system | High-sensitivity candidate system | Article 50 may apply but is only one part of the required review. | Submitting child-safety package as generic transparency proof. | Specialist review, legal review, conformance test, jurisdictional annex. |

---

## 7. Article 50 obligation mapping

This section maps major Article 50 transparency areas to candidate controls.

It does not assert final legal interpretation.

| Obligation area | Trigger condition | Actor relevance | Existing architecture-aligned control | Missing deployment evidence | Required proof artifact |
|---|---|---|---|---|---|
| AI interaction disclosure | A person interacts directly with an AI system. | Provider / deployer depending on system role. | System boundary, user notice, entity/tool/oracle distinction, role labelling. | Concrete UI notice, timing, wording, user flow. | Screenshot, UI copy, interaction log, versioned policy. |
| Generative AI machine-readable marking | A generative AI system outputs AI-generated or manipulated content. | Provider primarily; deployer may rely on provider and add publication controls. | Provenance sidecar, metadata policy, hash manifest, witness reference. | Selected marking method, interoperability test, robustness limits. | Metadata sample, C2PA or equivalent record, JSON sidecar, detection test. |
| Deepfake disclosure | AI-generated/manipulated image, audio, or video falsely appears authentic/truthful. | Deployer / publisher / content operator. | Visible disclosure, generation record, editorial review, provenance metadata. | Exact media workflow, label placement, exception review. | Label screenshot, media metadata, review record, takedown/correction path. |
| AI-generated public-interest publication disclosure | AI-generated/manipulated text informs the public on matters of public interest, unless human review/editorial responsibility applies. | Deployer / publisher / editorial actor. | Human review gate, editorial responsibility declaration, publication front matter. | Whether the content is public-interest; review details; responsible human. | Editorial statement, review log, author/responsible editor, publication metadata. |
| Human review and editorial responsibility | Publication or workflow claims human responsibility. | Deployer / publisher. | Human gate, task contract, witness event, review outcome. | Named reviewer, review date, review scope, correction path. | Review record, signed release note, editorial responsibility statement. |
| Emotion recognition notice | System performs emotion recognition in covered contexts. | Provider/deployer depending use. | State classification boundaries; non-diagnostic rule; state-not-content caution. | Whether emotion recognition is actually performed; legal basis; user notice. | Negative declaration or notice, DPIA/legal review, technical description. |
| Biometric categorisation notice | System performs biometric categorisation in covered contexts. | Provider/deployer depending use. | Actor grounding can prevent ungrounded reliance; no default biometric claim. | Whether biometric categorisation exists; category; legal basis; notice. | Negative declaration or notice, DPIA/legal review, data flow diagram. |
| Provenance and attribution | Output or action needs actor/source traceability. | Provider/deployer/publisher/agent operator. | Beacon, AGL, L4 Witness, CLI Agent Mesh task records. | Concrete identifiers, event schema, retention and privacy class. | Witness event, provenance record, hash chain, source-state record. |
| Audit trail | Transparency control must be reviewable. | All roles when claims are made. | L4 Witness, release hygiene, SHA/DOI, task contracts, ARL notes. | Operational logging implementation. | Audit log, witness chain, release manifest, independent review where applicable. |
| User-accessible explanation | Users need meaningful information, not internal noise. | Provider/deployer. | Role labels, system boundary descriptions, non-claim statements. | UI text tested on actual user flow. | Notice text, UX review, version-controlled disclosure policy. |

---

## 8. Control mapping by corpus layer

| Corpus control | Article 50 contribution | What it can prove | What it cannot prove |
|---|---|---|---|
| `c = a + b` | Connects AI system to human anchor, responsibility, and technological substrate. | A disciplined distinction between human actor, technical system, and emergent entity relation. | Legal status, compliance, or personhood. |
| L4 Reality Boundary | Forces cost, time, resource, and irreversibility awareness into system design. | That the architecture avoids fantasy claims of unconstrained autonomy. | That a specific deployment is lawful. |
| L4 Witness | Provides tamper-evident evidence discipline for events and privileged transitions. | That a disclosure, review, generation, or action boundary can be witnessed. | That users were properly informed. |
| Beacon | Distinguishes entity/tool/oracle/proxy/replay/clone-style claims. | Attribution and recognition discipline. | Safety or child suitability by itself. |
| Actor Grounding Layer | Grounds source, actor, route, freshness, and reliance state. | That a claim was not accepted merely because it was fluent. | Legal verification of all facts. |
| ARL | Routes disputes, freeze, quarantine, and review. | That contested states can stop and be reviewed. | Judicial or regulatory authority. |
| CLI Agent Mesh | Governs executable AI/cloud/CLI agents under task contracts and witness. | That AI-assisted operations can be bounded before file/system changes. | Article 50 compliance unless linked to a concrete user/publication workflow. |
| Release hygiene / SHA / DOI | Makes public artifacts stable, referenceable, and verifiable. | Integrity of released documents. | Legal adequacy of content. |
| Human review gate | Connects output to accountable human decision. | That a person reviewed and accepted responsibility. | That review was legally sufficient without scope and record. |
| Publication metadata | Provides content-level provenance and disclosure. | That a given artifact carries visible or machine-readable information. | That downstream copies preserve metadata. |

---

## 9. Provider / deployer distinction

A frequent implementation error is to collapse providers and deployers.

This package recommends keeping the distinction explicit.

### 9.1 Provider-side transparency controls

Provider-side controls may include:

- built-in user interaction notice;
- built-in machine-readable marking for generated outputs;
- documentation for deployers;
- output provenance metadata;
- marking robustness statement;
- technical limitations;
- model/system identity disclosure;
- API output metadata;
- logs or verifiable evidence where appropriate.

### 9.2 Deployer-side transparency controls

Deployer-side controls may include:

- workplace/client/user notice;
- publication disclosure;
- deepfake/content label;
- human review and editorial responsibility;
- local policy;
- screenshots of UI notice;
- correction or takedown process;
- use-case-specific legal review;
- internal training and access controls.

### 9.3 Mixed-role cases

Many small organisations and independent implementers may act in mixed roles.

Example:

```text
author builds a workflow
uses third-party LLMs
uses CLI/cloud agents
publishes AI-assisted public text
archives release artifacts
```

Possible roles:

```text
deployer
publisher/editorial actor
protocol author
agent operator
```

The compliance map should not hide this.

It should show which role applies to each workflow stage.

---

## 10. CLI Agent Mesh bridge

The C-Governed CLI Agent Mesh is a useful Article 50-adjacent control layer because it addresses AI systems that do not merely generate text but may execute tasks through tools.

The relevant bridge is:

```text
AI-assisted workflow
  -> task contract
  -> bounded permission
  -> sandbox / worktree
  -> action
  -> witness event
  -> review
  -> human gate
  -> publication / rejection
```

For Article 50 purposes, this helps with:

- evidence that content was AI-assisted;
- evidence that a human reviewed before publication;
- provenance of generated files;
- traceability of who authorised a release;
- correction and rollback;
- separation between agent output and human acceptance;
- no silent autonomy.

### 10.1 Candidate CLI Agent Mesh controls

| Control | Article 50-adjacent value |
|---|---|
| Task contract | Shows what the AI agent was authorised to do. |
| Permission scope | Shows whether the agent could read, write, execute, publish, or access secrets. |
| Sandbox/worktree | Prevents uncontrolled mutation of public artifacts. |
| Witness event | Records the boundary event without relying on memory or chat logs. |
| Human approval gate | Separates generated output from accepted publication. |
| Rollback / correction path | Supports post-publication accountability. |
| Secrets denial | Prevents hidden private-data leakage into generated outputs. |
| Release manifest | Makes public artifacts inspectable and referenceable. |

### 10.2 Non-claim

CLI Agent Mesh does not make a workflow Article 50-compliant by itself.

It provides a governance grammar for producing the evidence that a compliance review may need.

---

## 11. Disclosure examples

These are draft examples only.

They require legal and UX review before deployment.

### 11.1 AI interaction notice

```text
You are interacting with an AI-assisted system. Important decisions, publications, or actions are reviewed by a responsible human operator.
```

### 11.2 AI-generated content notice

```text
This content was generated or materially assisted by AI and reviewed by a human editor before publication.
```

### 11.3 Public-interest publication notice

```text
This publication contains AI-assisted drafting. Human editorial responsibility remains with Kotov Ivan.
```

### 11.4 Generated media notice

```text
This image/audio/video contains AI-generated or AI-manipulated elements.
```

### 11.5 Negative declaration for non-used sensitive functions

```text
This system does not perform emotion recognition or biometric categorisation.
```

### 11.6 CLI-agent assisted workflow notice

```text
This artifact was prepared through an AI-assisted workflow using bounded CLI/cloud agents. A human review gate was applied before publication.
```

---

## 12. Evidence artifacts

A strong Article 50 implementation should not rely on statements alone.

| Evidence artifact | Purpose |
|---|---|
| UI screenshot | Shows what the user actually saw. |
| UI copy file | Makes notice text version-controlled. |
| Publication front matter | Carries disclosure inside Markdown/PDF/EPUB/web publication. |
| JSON sidecar metadata | Provides machine-readable provenance where embedded metadata is absent or removable. |
| C2PA or equivalent provenance metadata | Supports content authenticity where technically feasible. |
| Hash manifest | Makes released artifacts tamper-evident. |
| L4 Witness event | Records privileged transition or publication boundary. |
| CLI task contract | Shows what AI agents were authorised to do. |
| Human review record | Shows who reviewed, when, and with what scope. |
| Editorial responsibility declaration | Shows who is accountable for a public-interest publication. |
| Correction / takedown log | Shows feedback and remediation loop. |
| Legal review memo | Shows counsel or qualified review where needed. |

---

## 13. Compliance map template

Every concrete implementation should be reducible to this template.

| Field | Required content |
|---|---|
| System name | Name and version of the system or workflow. |
| System boundary | What is inside and outside the system. |
| Actor role | Provider / deployer / publisher / researcher / protocol author / mixed. |
| User class | Public user / worker / client / reader / child / internal reviewer / regulator. |
| Trigger | AI interaction / generated content / deepfake / public-interest publication / emotion recognition / biometric categorisation / other. |
| Disclosure | Exact visible notice or label. |
| Marking | Machine-readable metadata, watermark, C2PA, JSON sidecar, hash, or other mechanism. |
| Provenance | Source, model, agent, route, generation event, review event. |
| Human review | Reviewer, timestamp, scope, outcome. |
| Witness / audit | Event ID, hash, chain, privacy class, retention class. |
| Responsible actor | Named human or organisation. |
| Open legal issue | What still requires counsel or regulatory clarification. |

---

## 14. A/B compliance language slots

### Slot A — strict factual statement

Use when submitting to regulators or legal reviewers:

```text
This package provides a technical mapping between Article 50 transparency obligation areas and candidate controls from the public c = a + b / L4 Witness / AGL / ARL / CLI Agent Mesh corpus. It does not claim formal compliance, certification, or legal sufficiency for any concrete deployment.
```

### Slot B — human-readable explanation

Use in public-facing explanation:

```text
The point is not to say “this system is compliant”. The point is to show the chain: what system is used, what role the human or organisation has, what transparency duty is triggered, what notice or marking is shown, what evidence exists, and who is responsible.
```

If the context is legal, regulatory, or official, default to Slot A.

---

## 15. Explicit bridge

The explicit bridge is:

```text
Article 50 transparency requires disclosure, marking, and responsibility.
c = a + b provides a disciplined separation between human anchor, technological substrate, and entity/workflow behavior.
L4 Witness, AGL, ARL, and CLI Agent Mesh provide evidence and review structures.
```

Therefore, the mapping chain is:

```text
human anchor / responsible actor
  -> AI system or workflow
  -> transparency trigger
  -> disclosure / marking
  -> evidence
  -> review / correction
```

This bridge is engineering-oriented, not metaphysical.

---

## 16. Quiet bridge I — information theory

Transparency is channel design.

A useful disclosure channel must carry enough information for the affected person to understand the AI role without forcing disclosure of irrelevant raw internals.

A useful provenance channel must carry enough information for audit and detection without creating a new privacy leak.

Therefore, Article 50 implementation should distinguish:

```text
human-facing notice
machine-facing mark
auditor-facing evidence
operator-facing review record
```

These are not interchangeable.

---

## 17. Quiet bridge II — Ashby / cybernetics

A single label cannot control all failure modes.

A system that can interact, generate, publish, execute, and revise needs matching control variety:

```text
notice for interaction
marking for synthetic output
provenance for content history
witness for privileged transitions
human review for responsibility
dispute/correction for feedback
```

This is an application of requisite variety.

The transparency mechanism must have enough variety to match the system's modes of action.

---

## 18. Earth paragraph — building inspection analogy

A building permit, a breaker label, an inspection report, and an electrician's signature are different things.

A breaker label helps the person in front of the panel.

The wiring diagram helps the technician.

The inspection report helps the authority.

The signature fixes responsibility.

AI transparency needs the same separation.

A user notice is the breaker label.

Machine-readable provenance is the wiring diagram.

A witness/audit event is the inspection record.

Human editorial responsibility is the signature.

If these are collapsed into one vague sentence, the system may look documented while remaining practically unauditable.

---

## 19. Recommended implementation sequence

For any concrete system or workflow:

1. Define the system boundary.
2. Classify the actor role.
3. Identify Article 50 trigger conditions.
4. Draft visible user-facing disclosure.
5. Select machine-readable marking or metadata method where applicable.
6. Define provenance and witness events.
7. Add human review and editorial responsibility gate.
8. Define correction, takedown, dispute, or rollback path.
9. Collect screenshots, logs, metadata samples, and review records.
10. Send the package to qualified legal review.

No step should be skipped by saying “the architecture already supports transparency.”

Architecture support is not evidence.

Evidence is evidence.

---

## 20. Gaps and open issues

Current open issues for this package:

| ID | Gap | Status |
|---|---|---|
| A50-OI-001 | No final legal review yet. | Open |
| A50-OI-002 | No final system-specific UI disclosure screenshots. | Open |
| A50-OI-003 | No selected production marking method for all media types. | Open |
| A50-OI-004 | No formal deployment role classification for each future system. | Open |
| A50-OI-005 | No DPIA / GDPR review for enterprise or worker-facing deployment. | Open |
| A50-OI-006 | No child-specific legal or developmental review for CCDP deployment. | Open |
| A50-OI-007 | No final EUSurvey submission text accepted by human author. | Open |
| A50-OI-008 | No final PDF / GitHub release / Zenodo archive for this Article 50 package. | Open |

---

## 21. Recommended submission sentence

For EUSurvey or accompanying material:

```text
This submission proposes a practical evidence-chain approach to Article 50 transparency implementation. It maps concrete system boundaries and actor roles to user-facing disclosures, machine-readable marking or provenance, witness/audit records, human review, and responsible actors. The approach is derived from the public c = a + b / L4 Witness / AGL / ARL / C-Governed CLI Agent Mesh corpus, but it does not claim formal compliance for any deployment without system-specific evidence and legal review.
```

---

## 22. References

Official sources:

1. European Commission, consultation on the draft guidelines on transparency obligations under the AI Act, published 8 May 2026, open until 3 June 2026:
   https://digital-strategy.ec.europa.eu/en/consultations/consultation-draft-guidelines-transparency-obligations-under-ai-act

2. European Commission, draft guidelines on implementation of transparency obligations for certain AI systems under Article 50 of the AI Act:
   https://digital-strategy.ec.europa.eu/en/library/draft-guidelines-implementation-transparency-obligations-certain-ai-systems-under-article-50-ai-act

3. European Commission / AI Office, Code of Practice on marking and labelling of AI-generated content:
   https://digital-strategy.ec.europa.eu/en/policies/code-practice-ai-generated-content

Public technical source:

4. Kotov Ivan, C-Governed CLI Agent Mesh v0.1.1, GitHub repository:
   https://github.com/Kot141078/c-governed-cli-agent-mesh

5. Kotov Ivan, C-Governed CLI Agent Mesh v0.1.1, Zenodo DOI:
   https://doi.org/10.5281/zenodo.20257232

---

## 23. Final control statement

The final control statement for this mapping is:

```text
No transparency claim should stand without:
  - a system boundary;
  - an actor role;
  - a trigger;
  - a disclosure or marking control;
  - an evidence artifact;
  - a responsible human or organisation;
  - and an open path for review, correction, or legal handoff.
```

This is the proposed compliance architecture bridge for Article 50.
