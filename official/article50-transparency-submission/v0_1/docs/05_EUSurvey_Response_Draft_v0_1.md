# EUSurvey Response Draft v0.1

**Author:** Kotov Ivan
**Location:** Bruxelles, Belgium
**Date:** 2026-05-19
**Document ID:** `Article50_EUSurvey_Response_Draft_v0_1`
**Package:** `Article50_Transparency_Submission_v0_1`
**Status:** Draft questionnaire response support document
**Intended channel:** European Commission / AI Office consultation on draft Article 50 transparency guidelines
**Legal status:** Not legal advice. Not certification. Not a conformity assessment.
**Submission status:** Not submitted. Requires human review before use.

---

## 0. Use note

This document is a drafting aid for the official EUSurvey consultation response.

It is not the submission itself.

The official response must be entered through the European Commission's online consultation questionnaire before the deadline.

This draft should be adapted to:

- the actual questionnaire fields;
- word or character limits;
- available attachment/link options;
- final human review;
- legal/claim review before submission.

Do not paste the entire package into the questionnaire.

Use concise answers and link or attach the supporting package only where the questionnaire allows.

---

## 1. Respondent profile draft

Use or adapt:

```text
Name: Kotov Ivan
Location: Bruxelles, Belgium
Stakeholder type: Independent researcher / independent consultant / AI systems architect / protocol author
Relevant work: c = a + b protocol, L4 Reality Boundary, L4 Witness, Actor Grounding Layer, Arbitration / Review Layer, C-Governed CLI Agent Mesh, AI transparency and evidence-chain architecture
Submission type: Technical implementation contribution / evidence-chain mapping for Article 50 transparency obligations
```

If the form asks for organisation:

```text
Independent individual / independent researcher
```

If the form asks whether the response may be published:

```text
To be selected by the author after final review.
```

Recommended public-facing descriptor:

```text
Independent researcher and AI systems architect, Bruxelles, Belgium.
```

Avoid:

```text
Certified compliance expert
Official legal representative
Provider of a certified Article 50 system
```

unless legally verified.

---

## 2. One-sentence summary

Short version:

```text
This submission proposes an evidence-chain approach to Article 50 transparency: each obligation should be mapped from a concrete system boundary and actor role to user-facing disclosure, machine-readable marking or provenance, witness/audit evidence, human review, and a responsible actor.
```

Very short version:

```text
Article 50 transparency should be implemented as a traceable chain: system, role, trigger, disclosure, marking/provenance, evidence, human responsibility.
```

---

## 3. Main contribution — short field

Use if the questionnaire has a short “main feedback” field.

```text
I support practical guidance that makes Article 50 obligations operational for providers and deployers. My contribution is an evidence-chain mapping pattern: every transparency claim should identify the concrete system boundary, actor role, obligation trigger, user-facing disclosure, machine-readable marking or provenance, witness/audit evidence, human review, and responsible actor. This avoids both overclaiming and purely decorative transparency notices.
```

---

## 4. Main contribution — medium field

Use if the questionnaire allows a medium-length answer.

```text
My submission proposes a practical evidence-chain approach to Article 50 transparency implementation. In my view, transparency should not be treated as a general declaration that “AI was used”. A useful transparency control should be mapped to a concrete system and role: provider, deployer, publisher/editorial actor, enterprise operator, or AI-assisted workflow operator.

For each obligation, the implementation should show: the trigger, the visible disclosure shown to the person, the machine-readable mark or provenance mechanism where applicable, the audit or witness evidence that the control was applied, the human review record where relevant, and the responsible human or organisation.

This is especially important for AI-assisted publication workflows and executable agent workflows. A model may generate text, but a tool-using AI agent may also create files, modify repositories, generate metadata, prepare release artifacts, or assist with public submissions. The guidelines should encourage a separation between AI output, provenance evidence, and human acceptance before publication.

The submission does not claim formal compliance or certification. It provides an architecture-aligned implementation pattern based on public work around c = a + b, L4 Witness, Actor Grounding Layer, Arbitration / Review Layer, and C-Governed CLI Agent Mesh.
```

---

## 5. Main contribution — long field

Use if the questionnaire allows a longer free-text response.

```text
I welcome the Commission's effort to provide practical guidance on Article 50 transparency obligations. My main suggestion is that the guidelines should encourage providers and deployers to implement transparency as an evidence chain, not as a single policy statement or label.

A serious transparency claim should be mapped through the following chain:

system boundary -> actor role -> obligation trigger -> user-facing disclosure -> machine-readable marking or provenance -> witness/audit evidence -> human review -> responsible actor -> correction or review route.

This mapping is important because the same AI-assisted workflow can contain several distinct transparency surfaces. A user-facing notice informs a person. A machine-readable mark supports detection. A provenance record supports traceability. A witness or audit record supports review. Human editorial responsibility assigns accountability. A correction route closes the feedback loop. These functions should not be collapsed into one generic checkbox.

I recommend that the guidelines explicitly encourage implementers to preserve the provider/deployer distinction while also addressing mixed-role situations. Independent creators, SMEs, researchers, publishers, and enterprise operators may use third-party models, local tools, and CLI/cloud agents in the same workflow. In such cases, the relevant question is not only “which model generated the output?” but also “who deployed the system, who reviewed the output, who accepted responsibility, and what evidence exists?”

This is especially relevant for AI-assisted public-interest publications and generated media. Where a human review or editorial responsibility path is used, it should be substantive and evidenced. A mere statement that “a human was involved” should not be enough. A useful record should identify the reviewer or responsible editor, the reviewed artifact, the review scope, the decision, the timestamp, and the correction route.

The same reasoning applies to executable agent workflows. AI agents may not only generate text; they may create files, modify code, run scripts, prepare metadata, update releases, or publish artifacts. I therefore recommend that the guidelines recognise task contracts, permission scopes, sandbox records, witness events, and human approval gates as useful evidence mechanisms for AI-assisted workflows.

My submission does not claim that my public corpus or any protocol is formally compliant. It proposes a reusable implementation grammar for Article 50: no transparency claim without a system boundary, role classification, trigger identification, disclosure or marking control, evidence artifact, responsible actor, and legal review path.
```

---

## 6. Answer on Article 50(1): direct AI interaction disclosure

Draft answer:

```text
For direct interaction with an AI system, the guidelines should emphasise that the notice must be visible, timely, and understandable to the natural person. It should not be hidden in a general terms-of-service document or depend on the user asking whether the system is AI.

I recommend that implementers record evidence that the notice was actually presented in the relevant interaction flow. A screenshot, versioned UI copy, or interaction-state log can support later review. However, such evidence should not replace the notice itself.

The guidelines should also encourage role clarity. The user should not only know that “AI is involved”, but should understand, at least at a practical level, whether the system is an AI assistant, tool, oracle-like service, automated agent, or AI-assisted workflow with human review.
```

Shorter version:

```text
Article 50(1) guidance should distinguish the visible user notice from internal evidence that the notice was displayed. A witness or audit log can support review, but it is not a substitute for informing the person in the interaction flow.
```

---

## 7. Answer on Article 50(2): machine-readable marking

Draft answer:

```text
For machine-readable marking, I recommend that the guidelines encourage layered provenance rather than a single fragile mechanism. In practice, embedded metadata may be stripped, watermarks may be altered, and downstream platforms may transform files. Therefore, marking should be supported where possible by sidecar metadata, release manifests, hash references, or other provenance records.

The guidelines should distinguish between three audiences: natural persons, machines/detection systems, and auditors. A visible disclosure informs the person. A machine-readable mark supports detection. A provenance or witness record supports audit. These layers should be connected, but not confused.

For AI-assisted publication workflows, the mark or metadata should ideally identify the artifact, the AI assistance scope, the responsible human/editorial actor, and the review state.
```

Shorter version:

```text
Machine-readable marking should be treated as part of a provenance chain, not as the whole transparency control. Visible disclosure, metadata, witness/audit evidence, and human responsibility serve different audiences and should be connected.
```

---

## 8. Answer on Article 50(3): emotion recognition and biometric categorisation

Draft answer:

```text
The guidelines should encourage deployers to provide clear positive notices when emotion recognition or biometric categorisation is used, and clear negative declarations where systems may otherwise be misunderstood.

This is important because many systems perform state classification, style adaptation, risk scoring, sentiment analysis, or user-context adaptation without necessarily being designed as legally relevant emotion recognition or biometric categorisation systems. The boundary should be technically described and legally reviewed.

I recommend that the guidelines encourage implementers to maintain a technical function map: what inputs are processed, whether biometric data is used, whether emotional or biometric categories are inferred, who sees the result, and whether the result affects the person.
```

Shorter version:

```text
The guidelines should help distinguish ordinary state/workflow classification from legally relevant emotion recognition or biometric categorisation, while requiring clear notices where such functions are actually used.
```

---

## 9. Answer on Article 50(4): deepfakes and public-interest publications

Draft answer:

```text
For deepfakes and AI-generated public-interest publications, I recommend stronger guidance on evidence of human editorial responsibility. A general statement that a human reviewed the output is not enough unless the review is substantive, scoped, and attributable.

A useful human review record should identify the reviewed artifact, reviewer or responsible editor, review date, review scope, publication decision, and correction route. This is especially important where human review affects whether a disclosure is required or how it is presented.

For generated or manipulated media, visible disclosure should be combined with machine-readable provenance where possible, because metadata alone may not be visible to the public and may be removed downstream.

The guidelines should also address AI-assisted workflows where CLI/cloud agents prepare publication artifacts, not only cases where a model directly emits final text or media.
```

Shorter version:

```text
For Article 50(4), human editorial responsibility should be evidenced, not merely declared. Generated media and public-interest AI-assisted publications should combine visible disclosure, provenance/marking, and a recorded human review or correction path.
```

---

## 10. Suggested implementation pattern for the guidelines

Draft answer:

```text
I suggest including an implementation pattern such as:

1. Define the AI system or AI-assisted workflow.
2. Classify the actor role: provider, deployer, publisher/editorial actor, enterprise operator, agent operator, or mixed role.
3. Identify the Article 50 trigger.
4. Define the visible user-facing disclosure.
5. Define the machine-readable mark or provenance mechanism where applicable.
6. Record audit or witness evidence that the control was applied.
7. Record human review and editorial responsibility where relevant.
8. Define a correction, takedown, dispute, or review route.
9. Preserve evidence with data minimisation.
10. Seek legal review for uncertain or high-impact use cases.

This pattern would help implementers move from declarative transparency to testable transparency.
```

---

## 11. Suggested language on evidence

Draft answer:

```text
The guidelines could clarify that evidence of transparency is not the same as transparency itself. For example, a log showing that a notice was displayed can help an auditor, but the person must still have received a clear notice. A machine-readable mark can help detection, but visible disclosure may still be required. A human review record can support editorial responsibility, but only if the review is substantive and attributable.
```

---

## 12. Suggested language on AI-assisted workflows and agents

Draft answer:

```text
I recommend that the guidelines explicitly address AI-assisted workflows involving tool-using or CLI/cloud agents. These systems may create or modify files, generate release artifacts, prepare publications, run validators, or produce metadata. Transparency guidance should therefore consider task contracts, permission scopes, sandbox records, witness events, and human approval gates as useful evidence mechanisms.

This would be particularly useful for SMEs, independent researchers, publishers, developers, and organisations that use AI agents internally before publishing content or systems externally.
```

---

## 13. Suggested language on public-interest AI-generated text

Draft answer:

```text
For AI-generated or AI-assisted text on matters of public interest, the guidelines should clarify what level of human involvement counts as meaningful editorial responsibility. In my view, a superficial spelling pass should not be treated the same as substantive review. The evidence should show who reviewed the content, what was reviewed, what was changed or accepted, and who remains responsible after publication.
```

---

## 14. Suggested language on provenance

Draft answer:

```text
The guidelines should encourage provenance practices that remain useful across formats. For example, Markdown, PDF, HTML, images, audio, video, and code releases may require different marking methods. A practical approach may combine visible labels, embedded metadata, C2PA or equivalent records where feasible, JSON sidecar metadata, release manifests, and hash references.

The key is not to rely on one fragile mechanism, but to preserve a reviewable chain.
```

---

## 15. Suggested language on data minimisation

Draft answer:

```text
The guidelines should also warn against overcollection in the name of transparency. Audit and witness records should preserve the boundary event, provenance, and review state, but should not become a surveillance archive or store unnecessary private prompts, conversations, secrets, or personal data.

A useful principle is: enough evidence for review, minimal raw leakage.
```

---

## 16. Suggested language on mixed roles

Draft answer:

```text
The guidelines could include examples for mixed-role actors. Independent creators, SMEs, researchers, publishers, and enterprise operators may use third-party AI systems, local models, AI agents, and human editors in one workflow. In such cases, a single label such as “provider” or “deployer” may not explain the entire chain. The guidance should encourage role classification per workflow stage.
```

---

## 17. Suggested attachment note

Use if the EUSurvey form allows attachments or supporting links:

```text
I attach or link a short supporting package titled “Article50_Transparency_Submission_v0_1”. It contains a cover note, compliance mapping pack, system-role-obligation-control-evidence table, L4 Witness/provenance bridge, and non-claims/legal review boundary. The package is a technical implementation contribution and does not claim formal compliance or certification.
```

If only a link is allowed:

```text
Supporting package link: [insert GitHub or Zenodo URL after publication/freeze]
```

Do not insert a private local path.

---

## 18. Suggested closing statement

Draft answer:

```text
The final guideline should help implementers avoid both under-disclosure and overclaiming. Transparency should be concrete enough for users, machine-readable enough for detection, evidenced enough for audit, and responsible enough for legal review. My recommendation is simple: no transparency claim without a system boundary, actor role, trigger, disclosure or marking control, evidence artifact, and responsible human or organisation.
```

---

## 19. Ultra-short final answer

Use where the form gives very limited space:

```text
Please treat Article 50 transparency as an evidence chain: system boundary, actor role, trigger, user notice, machine-readable mark/provenance, audit/witness evidence, human review, responsible actor, and correction route. This prevents decorative labels and supports practical enforcement.
```

---

## 20. A/B slots for tone control

### Slot A — formal / official

```text
This contribution proposes a technical evidence-chain model for implementing Article 50 transparency obligations. It does not claim certification or formal compliance. It recommends that every transparency claim be mapped to a concrete system boundary, actor role, obligation trigger, disclosure or marking control, evidence artifact, responsible actor, and legal review path.
```

### Slot B — plain explanation

```text
The practical problem is not whether someone says “AI was used”. The practical problem is whether we can see what system was used, who was responsible, what notice or marking was applied, what evidence exists, and how errors can be corrected.
```

Use Slot A in the official consultation.

---

## 21. Claims to avoid in EUSurvey

Do not write:

```text
My system is Article 50 compliant.
My architecture proves compliance.
L4 Witness solves transparency.
CLI Agent Mesh is a compliance system.
The EU should recognise c as a legal entity.
My corpus already covers all Article 50 obligations.
```

Write instead:

```text
My submission proposes an architecture-aligned evidence-chain mapping that may help providers and deployers implement Article 50 transparency obligations in a more auditable way.
```

---

## 22. Final checklist before submission

```text
[ ] Check actual questionnaire fields.
[ ] Respect character limits.
[ ] Use official consultation channel.
[ ] Remove excessive theory.
[ ] Keep response focused on Article 50.
[ ] Do not overclaim compliance.
[ ] Keep CCDP secondary or omit if space is limited.
[ ] Include CLI Agent Mesh only as workflow provenance/evidence bridge.
[ ] Include supporting package link only after final public freeze.
[ ] Human author reviews all final text.
[ ] Legal review if any concrete compliance claim is added.
```

---

## 23. Recommended final response package

If the form permits one main response and one attachment/link, use:

Main response:

```text
This contribution proposes an evidence-chain approach to Article 50 transparency implementation. Each transparency claim should be mapped from a concrete system boundary and actor role to the relevant obligation trigger, visible disclosure, machine-readable marking or provenance mechanism, audit/witness evidence, human review, responsible actor, and correction route. This is particularly important for AI-assisted publication workflows and tool-using AI agents, where the output may pass through multiple stages before publication. The contribution is architecture-aligned and technical; it does not claim formal compliance or certification for any deployed system.
```

Attachment/link note:

```text
A short supporting package is available with a compliance mapping table, system-role-obligation-control-evidence matrix, L4 Witness/provenance bridge, and non-claim/legal review boundary.
```

---

## 24. References to cite or link if allowed

Official sources:

1. European Commission, consultation on draft guidelines on transparency obligations under the AI Act:
   https://digital-strategy.ec.europa.eu/en/consultations/consultation-draft-guidelines-transparency-obligations-under-ai-act

2. European Commission, draft guidelines on implementation of transparency obligations for certain AI systems under Article 50 of the AI Act:
   https://digital-strategy.ec.europa.eu/en/library/draft-guidelines-implementation-transparency-obligations-certain-ai-systems-under-article-50-ai-act

3. European Commission / AI Office, Code of Practice on marking and labelling of AI-generated content:
   https://digital-strategy.ec.europa.eu/en/policies/code-practice-ai-generated-content

Supporting technical source:

4. Kotov Ivan, C-Governed CLI Agent Mesh v0.1.1:
   https://github.com/Kot141078/c-governed-cli-agent-mesh

5. DOI / Zenodo archive for C-Governed CLI Agent Mesh v0.1.1:
   https://doi.org/10.5281/zenodo.20257232

---

## 25. Final control statement

The EUSurvey response should be short enough to be read and strict enough not to overclaim.

The message is:

```text
Make Article 50 transparency auditable:
system, role, trigger, disclosure, marking/provenance, evidence, human responsibility, correction route.
```

Do not make the message:

```text
Please validate my whole architecture.
```

That is the boundary.
