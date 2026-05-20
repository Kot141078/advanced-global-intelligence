# L4 Witness and Provenance Bridge v0.1

**Author:** Kotov Ivan
**Location:** Bruxelles, Belgium
**Date:** 2026-05-19
**Document ID:** `Article50_L4_Witness_and_Provenance_Bridge_v0_1`
**Package:** `Article50_Transparency_Submission_v0_1`
**Status:** Draft technical bridge document
**Intended channel:** European Commission / AI Office consultation on draft Article 50 transparency guidelines
**Legal status:** Not legal advice. Not certification. Not a conformity assessment.
**Primary posture:** witness is evidence support; disclosure remains user-facing; formal compliance remains deployment-specific.

---

## 0. Executive summary

This document explains how L4 Witness, provenance metadata, Actor Grounding Layer, Arbitration / Review Layer, and C-Governed CLI Agent Mesh can support Article 50 transparency implementation.

The core position is:

> A transparency obligation becomes stronger when it is supported by provenance and witness evidence, but witness evidence does not replace user-facing disclosure.

This document therefore separates four layers:

```text
human-facing notice
machine-readable marking / provenance
witness / audit evidence
responsible human review
```

These layers are complementary.

They must not be collapsed into one generic “transparency” checkbox.

---

## 1. Non-claim boundary

This bridge does **not** claim:

1. that L4 Witness equals Article 50 compliance;
2. that a witness log is a user notice;
3. that machine-readable metadata is sufficient where visible disclosure is required;
4. that provenance proves truthfulness;
5. that a hash proves legal adequacy;
6. that a human review record is meaningful without named responsibility and review scope;
7. that CLI Agent Mesh governance is itself an Article 50 compliance system;
8. that architecture can replace legal review.

The correct claim is narrower:

```text
L4 Witness and provenance mechanisms can produce evidence that transparency controls were applied, reviewed, and preserved.
```

---

## 2. Article 50 transparency problem

Article 50 transparency obligations involve several distinct implementation surfaces.

A system may need to show:

- that a person was informed they were interacting with an AI system;
- that AI-generated or manipulated content was marked in a machine-readable format;
- that a deepfake or synthetic media artifact was disclosed;
- that an AI-generated public-interest publication was disclosed or human-reviewed with editorial responsibility;
- that emotion recognition or biometric categorisation was disclosed where applicable;
- that responsibility for publication or deployment is assigned to a human or organisation.

These are not the same thing.

A visible notice informs a person.

A machine-readable mark helps detection.

A provenance record helps trace origin.

A witness event helps review whether a transition occurred.

A human review record fixes responsibility.

---

## 3. Layer separation

| Layer | Audience | Purpose | Example artifact |
|---|---|---|---|
| Human-facing notice | User, reader, affected person | Inform that AI is involved. | UI banner, document notice, public label. |
| Machine-readable mark | Detection systems, downstream processors, auditors | Support detection of AI-generated/manipulated content. | C2PA record, embedded metadata, watermark, JSON sidecar. |
| Provenance record | Auditor, reviewer, publisher, technical operator | Show origin, route, generation context, version. | Source-state record, metadata bundle, release manifest. |
| Witness event | Reviewer, auditor, compliance owner | Show that a privileged transition occurred. | L4 Witness event, hash-linked operation note. |
| Human review record | Legal/editorial/operational reviewer | Show human decision and responsibility. | Review note, approval gate, editorial statement. |
| Correction route | User, regulator, operator | Repair wrong disclosure, label, or provenance. | Takedown log, correction note, ARL-style review. |

A system that provides only one of these layers should not be described as having a complete transparency chain.

---

## 4. Witness is not disclosure

The most important distinction in this document is:

```text
witness evidence
  !=
user-facing disclosure
```

A witness event can prove that a disclosure was generated, displayed, reviewed, or published.

It does not itself inform the user unless it is surfaced in the appropriate user-facing form.

Therefore:

| Situation | Correct interpretation |
|---|---|
| A witness event records that a notice was shown. | Useful evidence, but the notice itself must still be visible to the user. |
| Metadata records AI generation. | Useful for machines/auditors, but not always sufficient for human disclosure. |
| A hash proves a file is unchanged. | Useful for integrity, but does not prove legal adequacy. |
| Human review is recorded. | Useful only if reviewer, scope, timestamp, and outcome are clear. |
| CLI agent task is logged. | Useful provenance, but downstream publication still needs disclosure if Article 50 triggers apply. |

---

## 5. L4 Witness as evidence discipline

L4 Witness is useful for Article 50 because it can make key transitions reviewable.

Candidate witness events include:

```text
ai_interaction_notice_displayed
ai_output_generated
machine_readable_mark_attached
metadata_sidecar_created
human_review_started
human_review_completed
publication_approved
publication_rejected
deepfake_label_attached
public_interest_disclosure_attached
correction_requested
correction_applied
marking_removed_or_failed
provenance_chain_broken
legal_review_required
legal_review_completed
```

Each event should record only the minimum information needed for review.

Witness should not become surveillance.

---

## 6. Candidate witness envelope

A minimal Article 50 witness envelope may include:

```json
{
  "event_id": "a50w_20260519_000001",
  "event_type": "ai_output_generated",
  "timestamp_utc": "2026-05-19T09:30:00Z",
  "system_id": "example_publication_workflow_v0_1",
  "actor_role": "deployer_editorial_actor",
  "responsible_human": "Kotov Ivan",
  "article50_trigger": "ai_generated_public_interest_text_possible",
  "control_applied": "human_review_required",
  "evidence_refs": [
    "task_contract_sha256:...",
    "draft_file_sha256:..."
  ],
  "privacy_class": "metadata_only",
  "retention_class": "submission_package_evidence",
  "review_state": "pending_human_review",
  "prev_event_hash": "..."
}
```

This is not proposed as a mandatory schema.

It is a demonstration of the evidence chain:

```text
event
  -> trigger
  -> control
  -> evidence
  -> responsible actor
  -> review state
```

---

## 7. Provenance sidecar pattern

For Markdown, PDF, web pages, generated images, and release artifacts, a sidecar pattern can help where embedded metadata is fragile or absent.

Example:

```json
{
  "artifact_id": "Article50_Compliance_Mapping_Pack_v0_1",
  "artifact_type": "markdown_document",
  "author": "Kotov Ivan",
  "human_editorial_responsibility": "Kotov Ivan",
  "ai_assistance": {
    "used": true,
    "scope": "drafting, structuring, table generation, consistency review",
    "human_review_required": true,
    "human_review_completed": false
  },
  "article50_relevance": {
    "ai_generated_or_assisted_text": true,
    "public_interest_publication_possible": true,
    "deepfake": false,
    "emotion_recognition": false,
    "biometric_categorisation": false
  },
  "disclosure": {
    "visible_notice_required": "to be reviewed",
    "current_notice": "Draft prepared with AI assistance and subject to human review."
  },
  "provenance": {
    "source_files": [],
    "task_contract_refs": [],
    "witness_event_refs": [],
    "sha256": "..."
  },
  "legal_review": {
    "required": true,
    "completed": false
  }
}
```

The sidecar should not contain private prompt logs, internal reasoning, or unrelated personal data.

It should contain enough metadata to support provenance and review.

---

## 8. Article 50 event families

A practical implementation can organise witness events into event families.

| Family | Purpose |
|---|---|
| `a50.notice.*` | Events related to visible user-facing notices. |
| `a50.marking.*` | Events related to machine-readable marking or metadata. |
| `a50.provenance.*` | Events related to source, route, model, artifact, or publication lineage. |
| `a50.review.*` | Events related to human review and editorial responsibility. |
| `a50.publication.*` | Events related to publication approval, release, update, correction, or withdrawal. |
| `a50.sensitive_function.*` | Events related to emotion recognition or biometric categorisation notices or negative declarations. |
| `a50.deepfake.*` | Events related to generated/manipulated media disclosure. |
| `a50.agent.*` | Events related to CLI/cloud agent work on the artifact. |
| `a50.legal.*` | Events related to legal review, legal hold, or jurisdictional handoff. |

Example event names:

```text
a50.notice.displayed
a50.notice.updated
a50.marking.attached
a50.marking.failed
a50.provenance.sidecar_created
a50.review.human_started
a50.review.human_completed
a50.publication.approved
a50.publication.corrected
a50.agent.task_contract_created
a50.agent.witness_bound
a50.legal.review_required
```

---

## 9. AGL bridge

Actor Grounding Layer is relevant because transparency depends on knowing what actor, source, route, or system state is being relied upon.

For Article 50, AGL can support questions such as:

| Question | AGL contribution |
|---|---|
| Which system generated the output? | Source and route qualification. |
| Which actor authorised publication? | Actor grounding and responsibility mapping. |
| Was the output produced by a tool, oracle, agent, or human-assisted workflow? | Source-state and role separation. |
| Was the source fresh, stale, degraded, proxied, or uncertain? | Reliance state qualification. |
| Should the output be published now? | Grounding threshold before reliance. |

AGL should not be described as legal verification.

It is a pre-reliance engineering control.

---

## 10. ARL bridge

Arbitration / Review Layer is relevant where transparency states are disputed.

Examples:

```text
Was the content sufficiently disclosed?
Was human review real or decorative?
Was metadata removed downstream?
Was the system wrongly described as non-AI?
Was a generated image wrongly treated as ordinary photography?
Was a CLI agent allowed to publish without human review?
```

ARL-style handling can provide:

- hold;
- freeze;
- quarantine;
- review intake;
- standing;
- evidence admission;
- outcome;
- correction;
- re-entry.

For Article 50, this supports correction and accountability.

It does not replace a court, regulator, or competent authority.

---

## 11. CLI Agent Mesh bridge

C-Governed CLI Agent Mesh is relevant because AI-assisted workflows increasingly include executable agents that can:

- create files;
- modify repositories;
- generate metadata;
- run validators;
- produce release notes;
- prepare PDF or publication artifacts;
- touch manifests;
- execute scripts;
- affect what becomes public.

For Article 50 transparency, this creates a provenance problem:

```text
Was the artifact human-written, AI-assisted, agent-edited, agent-generated, or human-reviewed after agent work?
```

A CLI Agent Mesh can answer this through:

| Mesh control | Article 50 provenance value |
|---|---|
| Task contract | Shows what the agent was instructed and allowed to do. |
| Permission scope | Shows read/write/execute/publish boundaries. |
| Sandbox / worktree | Shows the agent did not silently mutate canonical release artifacts. |
| Witness event | Shows agent action was recorded. |
| Human gate | Shows output was accepted by a responsible human. |
| Rollback path | Shows correction is possible. |
| Manifest | Shows final artifact inventory. |
| Validator | Shows some machine-checkable rules were applied. |

This is not Article 50 compliance by itself.

It is evidence infrastructure.

---

## 12. Publication workflow bridge

For an AI-assisted publication, a useful chain is:

```text
draft created
  -> AI assistance declared internally
  -> provenance sidecar created
  -> human review started
  -> human review completed
  -> visible disclosure selected
  -> metadata / mark attached
  -> witness event created
  -> publication approved
  -> release hash recorded
  -> correction route opened
```

If the publication concerns matters of public interest, the human review and editorial responsibility record becomes especially important.

A minimal publication record should include:

```text
artifact_id
artifact_type
public_url_or_release_path
AI assistance scope
visible disclosure used
metadata / marking method
human reviewer
review timestamp
review scope
publication decision
correction path
hash / release reference
```

---

## 13. Generated media bridge

For AI-generated or AI-manipulated media, the system should distinguish:

| Media state | Candidate control |
|---|---|
| Purely illustrative generated image | Visible or contextual label where required; metadata where feasible. |
| Image resembling real person/place/event | Stronger deepfake/authenticity review. |
| Audio/video voice or face imitation | Explicit deepfake review and disclosure pathway. |
| Cropped or edited generated image | Preserve original generation metadata and edited artifact metadata. |
| Downstream repost or export | Warn that metadata may be stripped; visible disclosure may still be needed. |

Witness events can record:

```text
media_generated
media_edited
media_label_attached
metadata_attached
deepfake_review_required
deepfake_review_completed
publication_approved
```

---

## 14. Negative declaration bridge

Article 50 includes sensitive functions such as emotion recognition and biometric categorisation.

Where a system does not perform these functions, a negative declaration may help, but only if honest and technically grounded.

Example:

```text
This workflow does not perform emotion recognition or biometric categorisation. It may classify document status, publication workflow state, or editorial review status, but it does not infer emotions or biometric categories from natural persons.
```

A negative declaration should be supported by:

- data-flow description;
- model/tool capability boundary;
- no biometric input fields;
- no emotion labels;
- no face/voice/body categorisation;
- legal review if the boundary is uncertain.

Do not use negative declarations as decoration.

---

## 15. Privacy boundary

Provenance and witness can become dangerous if they overcollect.

The bridge therefore uses:

```text
metadata before content
state before transcript
hash before raw file where possible
review record before full prompt log
minimal evidence before surveillance archive
```

A witness record should avoid storing:

- private conversation logs;
- internal model reasoning;
- unrelated personal data;
- secrets;
- raw child data;
- raw worker surveillance data;
- full prompts where summary and hash are sufficient;
- credentials, tokens, API keys, or cloud secrets.

---

## 16. Retention classes

A practical Article 50 evidence chain may use retention classes.

| Retention class | Purpose |
|---|---|
| `R0_ephemeral` | Temporary working state; no compliance value after session. |
| `R1_public_artifact` | Public document, post, PDF, release file. |
| `R2_public_metadata` | Public provenance sidecar, release metadata, front matter. |
| `R3_internal_review` | Human review notes, task contracts, logs. |
| `R4_audit_witness` | Tamper-evident witness events. |
| `R5_legal_hold` | Preserved due to dispute, legal review, or competent authority need. |
| `R6_restricted_sensitive` | Sensitive safety/security/child/worker data; not public by default. |

The retention class should be visible in the evidence record.

---

## 17. Minimal schema proposal

A minimal Article 50 provenance object can be:

```json
{
  "a50_provenance_version": "0.1",
  "artifact_id": "example",
  "artifact_type": "markdown|pdf|web_page|image|audio|video|code|release",
  "system_boundary": "string",
  "actor_roles": ["author", "editor", "agent_operator"],
  "ai_assistance": {
    "used": true,
    "scope": "string",
    "tools_or_agents": ["string"]
  },
  "article50_triggers": {
    "ai_interaction": false,
    "ai_generated_content": true,
    "deepfake_possible": false,
    "public_interest_publication_possible": true,
    "emotion_recognition": false,
    "biometric_categorisation": false
  },
  "controls": {
    "visible_disclosure": "string",
    "machine_readable_mark": "string|null",
    "human_review": "required|completed|not_applicable",
    "editorial_responsibility": "string|null"
  },
  "evidence": {
    "witness_event_refs": [],
    "task_contract_refs": [],
    "sha256_refs": [],
    "release_refs": []
  },
  "review": {
    "responsible_human": "string",
    "review_state": "draft|reviewed|approved|rejected|corrected",
    "legal_review_required": true
  }
}
```

This should be treated as a draft bridge pattern, not as a final standard.

---

## 18. Evidence chain examples

### 18.1 AI-assisted Markdown submission

```text
Markdown draft created
  -> provenance sidecar records AI assistance
  -> human review marked required
  -> visible disclosure drafted
  -> SHA recorded
  -> human review completed
  -> PDF generated
  -> release manifest updated
```

Evidence artifacts:

```text
EV-META
EV-HUMAN-REVIEW
EV-WITNESS
EV-RELEASE
```

### 18.2 Generated public image

```text
image generated
  -> generation context recorded
  -> deepfake risk checked
  -> visible label selected
  -> metadata attached
  -> publication approved
```

Evidence artifacts:

```text
EV-DISCLOSURE
EV-MARK
EV-META
EV-HUMAN-REVIEW
```

### 18.3 CLI-agent assisted release

```text
task contract created
  -> agent operates in sandbox
  -> files changed
  -> validator runs
  -> witness event records operation
  -> human reviews diff
  -> release approved
```

Evidence artifacts:

```text
EV-CONTRACT
EV-WITNESS
EV-HUMAN-REVIEW
EV-RELEASE
```

---

## 19. Failure modes

| Failure | Description | Mitigation |
|---|---|---|
| Disclosure-only theatre | A label exists, but no evidence shows how it was applied. | Add provenance, review, and witness records. |
| Metadata-only invisibility | Metadata exists, but humans never see disclosure. | Add human-facing notice. |
| Witness-as-surveillance | System logs too much private content. | Store boundary metadata, not raw life. |
| Human-review theatre | “Reviewed by human” without name, scope, time, or responsibility. | Require review record and editorial responsibility. |
| Agent invisibility | CLI/cloud agents prepare artifacts without provenance. | Require task contracts and witness events. |
| Hash fetishism | SHA proves integrity but is treated as compliance. | Separate integrity from legal adequacy. |
| Role collapse | Provider, deployer, author, editor, and agent operator are mixed without mapping. | Add role classification per workflow stage. |
| Downstream metadata loss | Metadata is stripped by platforms. | Combine visible disclosure and metadata. |
| Overbroad legal claim | Architecture-aligned is presented as compliant. | Use non-claim boundary and legal review gate. |

---

## 20. A/B language slots

### Slot A — formal submission language

```text
L4 Witness, AGL, ARL, and C-Governed CLI Agent Mesh should be understood as candidate evidence and provenance mechanisms supporting Article 50 transparency implementation. They do not replace user-facing disclosure, machine-readable marking where required, human editorial responsibility, or legal review.
```

### Slot B — plain explanation

```text
A notice tells the person. Metadata tells machines. A witness record tells the reviewer what happened. A human signature tells who accepted responsibility. These are different layers and should not be confused.
```

For official submission, use Slot A.

---

## 21. Explicit bridge

The explicit bridge is:

```text
Article 50 transparency requires disclosure and marking.
L4 Witness and provenance records can show that disclosure and marking happened, under which system boundary, and under whose responsibility.
```

The bridge is evidence-oriented.

It is not a claim of legal sufficiency.

---

## 22. Quiet bridge I — information theory

Disclosure is not an information dump.

It is a signal designed for a particular receiver.

| Receiver | Needed signal |
|---|---|
| User | Clear notice. |
| Machine | Detectable mark. |
| Auditor | Provenance and witness. |
| Legal reviewer | Role, obligation, responsibility, evidence. |
| Operator | Correction and rollback path. |

A good transparency architecture keeps these channels separate enough to work, but connected enough to audit.

---

## 23. Quiet bridge II — cybernetics

Transparency is a feedback system.

```text
notice
  -> user awareness
  -> provenance
  -> review
  -> correction
  -> updated publication/system state
```

If a system cannot correct a wrong label, broken mark, missing disclosure, or false public claim, then its transparency loop is incomplete.

Therefore, every Article 50 control should have a correction route.

---

## 24. Earth paragraph — sealed meter and inspection tag

In a building, a sealed electrical meter does not tell the resident everything about the wiring.

It proves that a boundary was protected.

An inspection tag does not power the building.

It proves that someone checked a defined part of the system.

A label on the panel helps the person standing in front of it.

These are three different objects.

AI transparency has the same shape.

The user notice is the panel label.

The provenance metadata is the wiring diagram.

The witness event is the inspection tag.

The responsible human review is the electrician's signature.

A serious system should not pretend one of these replaces the others.

---

## 25. Recommended implementation sequence

For an Article 50-relevant workflow:

1. Define the artifact or interaction.
2. Identify whether user-facing disclosure is required.
3. Identify whether machine-readable marking is required.
4. Create or attach provenance metadata.
5. Create witness event for generation, marking, review, and publication.
6. Record human review and editorial responsibility where applicable.
7. Hash or release the final artifact.
8. Provide correction / dispute / takedown path.
9. Preserve only the minimum evidence needed.
10. Send uncertain cases to qualified legal review.

---

## 26. Open issues

| ID | Issue | Status |
|---|---|---|
| A50-WIT-001 | Final Article 50 witness event schema not yet frozen. | Open |
| A50-WIT-002 | C2PA or equivalent marking method not selected for each media class. | Open |
| A50-WIT-003 | Human review record format not yet frozen. | Open |
| A50-WIT-004 | Legal review of public-interest publication disclosure threshold not completed. | Open |
| A50-WIT-005 | Retention policy for evidence artifacts not legally reviewed. | Open |
| A50-WIT-006 | Integration with C-Governed CLI Agent Mesh witness objects not yet implemented in this package. | Open |
| A50-WIT-007 | No final EUSurvey text accepted by human author yet. | Open |

---

## 27. Final control statement

The proposed bridge is:

```text
Do not use witness as disclosure.
Do not use metadata as responsibility.
Do not use human review as decoration.
Do not use hashes as legal proof.
Do not use agent logs as public transparency.

Use each layer for its proper job,
then connect them through a reviewable evidence chain.
```

That is the L4 Witness and provenance bridge for Article 50.
