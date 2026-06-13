# PUBLIC / TECHNICAL / SENSITIVE SPLIT

## CCDP v0.1.1 addendum-only distribution boundary, release split, controlled-review handling, and anti-amplification rule

**Author:** Kotov Ivan  
**Location:** Bruxelles, Belgium  
**Year:** 2026  
**DOI:** Reserved DOI: 10.5281/zenodo.20680938  

**Package:** Child-`c` Development Protocol  
**Baseline package:** CCDP v0.1 DOI-bound / release-bound corpus slice  
**Addendum package:** CCDP v0.1.1 hygiene addendum  
**Document ID:** `PUBLIC_TECHNICAL_SENSITIVE_SPLIT`  
**Short name:** `PTS_SPLIT`  
**Status:** Draft addendum distribution-control profile  
**Date:** 2026-06-13  
**Selected patch mode:** `MODE_A_ADDENDUM_ONLY`  
**Layer:** CCDP / v0.1.1 hygiene / release packaging / distribution control  
**Document class:** package-control / distribution boundary / sensitive-release split  
**Assertion class:** `C-A10` control-layer artifact; does not upgrade child-safety, legal, clinical, developmental, security, or product-readiness claims  
**Primary rule:** classify distribution surfaces without rewriting the DOI-bound v0.1 baseline.

---

## 0. Executive summary

This document defines the current CCDP v0.1.1 addendum rule for separating package materials into public, technical, controlled-review, restricted/internal, and obsolete/non-canonical layers.

It exists because CCDP contains several different kinds of material:

```text
public explanation
technical schemas and conformance logic
defensive threat analysis
red-team review scaffolds
raw-evidence exception rules
child-safety routing details
jurisdictional handoff notes
obsolete drafts
```

These materials should not all be distributed with the same visibility, framing, or audience.

The split is:

| Class | Short name | Default handling |
|---|---|---|
| `DIST-PUBLIC` | Public | Safe for broad public release. |
| `DIST-PUBLIC-CONTROL` | Public control | Public package-control / release-control material. |
| `DIST-TECHNICAL-OPEN` | Technical open | Public or semi-public technical review material without operational abuse detail. |
| `DIST-TECHNICAL-CONTROLLED` | Technical controlled | Technical material that may be published only with defensive framing and careful excerpting. |
| `DIST-CONTROLLED-REVIEW` | Controlled review | Sensitive defensive review material for auditors, implementers, child-safety reviewers, legal/compliance reviewers, and responsible researchers. |
| `DIST-RESTRICTED-INTERNAL` | Restricted internal | Not for public release; private fixtures, access-control data, incident details, local annex drafts, or operational secrets. |
| `DIST-FORBIDDEN-RELEASE` | Forbidden release | Must not be included in a public package. |
| `DIST-OBSOLETE` | Obsolete | Historical / non-canonical only. |

Controlling formula:

```text
Public readers need enough context to understand CCDP.
Implementers need enough detail to implement safely.
Reviewers need enough detail to test defensively.
No release should turn child-safety material into an abuse manual.
```

This document mitigates `HP-010` / `OI-012` under Mode A by adding a distribution addendum. It does not edit the DOI-bound baseline files.

---

## 1. Purpose

This document answers eight release-control questions:

1. Which CCDP files are safe for broad public release?
2. Which files are technical and require implementation context?
3. Which files are defensive but sensitive?
4. Which content must be restricted or excluded entirely?
5. How should already-public / DOI-bound sensitive files be handled without retroactive mutation?
6. How should Codex or another patch agent package files without amplifying risk?
7. What warnings must accompany sensitive documents?
8. What should be included in public, technical, and controlled-review bundles?

This document is a distribution-control addendum, not a new safety mechanism.

---

## 2. Scope

### 2.1 In scope

This split applies to:

- CCDP v0.1 baseline files;
- CCDP v0.1.1 addendum files;
- future README / index / release-note surfaces;
- GitHub release packaging;
- Zenodo / DOI companion packaging;
- PDF bundle organization;
- Codex-safe packaging workflows;
- synthetic fixtures and conformance artifacts;
- threat-model and red-team artifact release boundaries;
- raw-evidence examples and sidecar examples;
- future local jurisdictional annexes;
- public whitepapers, diagrams, and explanatory material.

### 2.2 Out of scope

This document does **not**:

- create a legal classification regime;
- create a security clearance system;
- override local law;
- override institutional review requirements;
- decide child-protection procedure;
- authorize disclosure of real child data;
- authorize operational abuse examples;
- rewrite DOI-bound baseline files;
- retract already-published DOI-bound artifacts;
- certify product readiness;
- claim that controlled-review distribution is sufficient for safe deployment.

---

## 3. Corpus bridge set

### 3.1 Explicit bridge

`c = a + b` makes responsibility visible: `a` remains accountable, while `b` supplies tools, memory, schemas, procedures, models, and packaging.

A release package is also a `b` object. If it exposes child-safety internals without distribution discipline, it can harm the human subjects the protocol claims to protect.

Therefore CCDP must separate:

```text
explanation for public understanding
implementation detail for builders
sensitive defensive detail for reviewers
forbidden real-world child data and operational abuse material
```

### 3.2 Quiet bridge I — Ashby / requisite variety

The CCDP corpus contains more than one risk class. One publication mode cannot control all of them.

A public primer, a JSON schema, a threat card, a Red / Black scenario, a raw-evidence exception sidecar, and a synthetic red-team fixture require different distribution treatment. The split supplies enough release variety to match corpus variety.

### 3.3 Quiet bridge II — information theory / leakage

A raw transcript, abuse scenario, or exploit-like red-team script has a much higher leakage channel than a state-level summary or abstract defensive pattern.

Distribution control is therefore an information-minimization layer:

```text
expose the boundary
minimize the pathway
never publish raw child life
never publish operational abuse instructions
```

### 3.4 Earth paragraph

A construction site does not put every drawing on the street fence. The public board shows the project, permits, safety notices, and contact routes. The engineers hold structural drawings. Inspectors see hidden-work records. Hazardous procedures and access keys are kept under control. CCDP needs the same packaging discipline: enough visibility for trust, enough detail for builders, and enough restraint that the safety binder does not become a toolbox for misuse.

---

## 4. Core distribution rule

### 4.1 Default rule

```text
Publish the concept.
Publish the controls.
Publish the schemas when safe.
Control the threat details.
Restrict real data.
Forbid operational abuse content.
```

### 4.2 Baseline immutability under Mode A

Under `MODE_A_ADDENDUM_ONLY`, this split does not rewrite baseline files.

If a baseline file is already DOI-bound, PDF-paired, SHA-manifested, or externally citable:

```text
keep baseline stable
add distribution classification through this addendum
add future framing through new release notes / index files
avoid silent in-place mutation
```

### 4.3 Already-public sensitive materials

If a document classified here as `DIST-CONTROLLED-REVIEW` is already publicly available in a DOI-bound baseline, this addendum does not pretend it is unpublished.

Current handling is:

```text
1. do not rewrite or hide the historical artifact;
2. do not amplify it as product marketing;
3. add warning labels in future addendum packaging;
4. provide public-safe summaries where possible;
5. route detailed use to defensive review context.
```

### 4.4 No retroactive concealment rule

Classification is not a cover-up mechanism.

It is a forward release-control rule.

The goal is not to erase public history. The goal is to stop future packaging from mixing public explanation, technical implementation, and sensitive review material as if they had the same risk profile.

---

## 5. Distribution classes

### 5.1 `DIST-PUBLIC` — public explanation layer

**Meaning:** safe for broad public release and general readers.

Suitable content:

- landing pages;
- executive summaries;
- reading orders;
- conceptual explanation;
- non-operational diagrams;
- high-level safety principles;
- non-sensitive jurisdictional handoff framing;
- non-clinical review disclaimers;
- open issues stated without operational abuse detail.

Audience:

- general readers;
- researchers;
- journalists;
- educators;
- policy readers;
- potential reviewers;
- non-technical stakeholders.

Must not include:

- raw child content;
- operational abuse scripts;
- realistic manipulative child dialogue;
- detailed bypass instructions;
- exploit steps;
- unredacted family, school, legal, medical, or incident data;
- key material;
- private deployment information.

### 5.2 `DIST-PUBLIC-CONTROL` — public package-control layer

**Meaning:** public release-control documents that tell readers how to interpret, cite, or navigate the package.

Suitable content:

- addendum indexes;
- DOI-safe patch rules;
- canonical precedence rules;
- obsolete registries;
- terminology namespace clarifications;
- release notes;
- manifests;
- citation guidance.

These documents may mention sensitive categories, but should not include sensitive operational detail.

### 5.3 `DIST-TECHNICAL-OPEN` — technical open layer

**Meaning:** technical material that may be released publicly or semi-publicly for implementation and audit, provided it avoids operational abuse detail and real child data.

Suitable content:

- schemas;
- conformance gates;
- abstract test IDs;
- state-machine descriptions;
- memory class definitions;
- witness metadata structure;
- external handshake sequence;
- permission overlays;
- non-operational examples;
- implementation binding maps.

Audience:

- implementers;
- auditors;
- standards reviewers;
- safety engineers;
- security reviewers;
- repository maintainers.

Required framing:

```text
technical review artifact
not product marketing
not legal / clinical advice
not sufficient for deployment without review
```

### 5.4 `DIST-TECHNICAL-CONTROLLED` — technical controlled layer

**Meaning:** technical content that can be referenced in open releases but should be excerpted, summarized, or framed carefully.

Examples:

- Red / Black routing mechanics without scenario scripts;
- raw-evidence exception schemas without realistic child-content examples;
- sealed-zone exception logic;
- dependency-risk logic;
- physical-agent privilege rules;
- child-facing external-agent entry control;
- school interface safeguards;
- adult migration decision records.

Default release handling:

```text
publish safe normative rules
avoid operational examples
route detailed scenarios to controlled review
```

### 5.5 `DIST-CONTROLLED-REVIEW` — sensitive defensive review layer

**Meaning:** legitimate safety-review material that should be shared only with responsible reviewers, implementers, auditors, legal/compliance reviewers, child-safety reviewers, or security reviewers under defensive framing.

Suitable content:

- threat models;
- red-team playbooks;
- abuse-case catalogs;
- detailed Red / Black scenarios;
- raw-evidence exception examples;
- adversarial conformance tests;
- synthetic fixtures that describe unsafe patterns;
- jurisdictional examples involving abuse, exploitation, unsafe guardians, coercion, or emergencies;
- vendor / school / state capture examples.

Required constraints:

```text
synthetic fixtures only
no real child data
no operational abuse instructions
no realistic grooming dialogue
no bypass instructions
no exploit scripts
no public marketing use
clear defensive-purpose header
```

### 5.6 `DIST-RESTRICTED-INTERNAL` — restricted internal layer

**Meaning:** material not intended for public release.

Examples:

- private deployment configuration;
- credentials;
- keys;
- live system logs;
- real incident material;
- real child/family/school records;
- unredacted legal matters;
- non-public local annex drafts;
- reviewer personal data;
- internal Codex run logs containing sensitive paths or secrets;
- unreleased exploit-like test drafts.

Handling:

```text
keep out of public package
separate repository or secure storage
redact before review distribution
never include in SHA manifest for public release unless redacted artifact is intended for release
```

### 5.7 `DIST-FORBIDDEN-RELEASE` — forbidden release layer

**Meaning:** material that must not be released in any public or controlled-review package unless transformed into a safe synthetic / abstracted artifact.

Forbidden content includes:

- real child transcripts;
- real child emotional diaries;
- real sealed-zone content;
- real abuse reports;
- real family conflict records;
- real school welfare records;
- real medical, clinical, or psychological records;
- real custody/court data;
- credentials, keys, tokens;
- instructions for bypassing child-safety controls;
- realistic manipulative scripts targeting children;
- malware, phishing, credential theft, or surveillance instructions;
- real raw-evidence payloads.

### 5.8 `DIST-OBSOLETE` — obsolete / non-canonical layer

**Meaning:** historical material that must not be used as current protocol authority.

Handling is governed by `OBSOLETE.md`.

Default rule:

```text
retain for historical trace
mark clearly
move or list under archive/obsolete in future Mode B
never cite as canonical
```

---

## 6. File classification matrix — baseline CCDP v0.1

This matrix sets current distribution guidance under Mode A. It does not edit baseline files.

### 6.1 Public / public-control baseline files

| File | Distribution class | Default handling | Notes |
|---|---|---|---|
| `README.md` | `DIST-PUBLIC` | Publish broadly. | Landing page and package warnings. |
| `INDEX.md` | `DIST-PUBLIC-CONTROL` | Publish broadly. | Document registry. Must reference addendum in future packaging. |
| `CANONICAL_READING_ORDER.md` | `DIST-PUBLIC-CONTROL` | Publish broadly. | Reading paths; safe public navigation. |
| `RELEASE_NOTES.md` | `DIST-PUBLIC` | Publish broadly. | Release boundary and caution. |
| `OPEN_ISSUES.md` | `DIST-PUBLIC-CONTROL` | Publish broadly with review caveats. | Contains validation gaps; useful against overclaiming. |
| `GLOSSARY.md` | `DIST-PUBLIC-CONTROL` | Publish when available. | Should include terminology-axis clarifications in future Mode B. |
| `CHANGELOG.md` | `DIST-PUBLIC-CONTROL` | Publish when available. | Must not imply baseline mutation under Mode A. |
| `CCDP_v0_1_R_Corpus_Aligned.md` | `DIST-PUBLIC` | Publish broadly. | Root protocol; no operational abuse detail should be added under Mode A. |
| `CCDP_Jurisdictional_Handoff_Notes_v0_1.md` | `DIST-PUBLIC` / `DIST-TECHNICAL-CONTROLLED` | Public-safe by default; control detailed local examples. | Handoff discipline, not legal advice. |
| `CCDP_Developmental_Psychology_Review_Notes_v0_1.md` | `DIST-PUBLIC` | Publish broadly. | Review scaffold; helps prevent developmental overclaiming. |

### 6.2 Technical-open baseline files

| File | Distribution class | Default handling | Notes |
|---|---|---|---|
| `CCDP_Traceability_Matrix_v0_1.md` | `DIST-TECHNICAL-OPEN` | Publish for implementers and reviewers. | Needs addendum delta under Mode A. |
| `CCDP_Conformance_Test_Matrix_v0_1.md` | `DIST-TECHNICAL-OPEN` | Publish for implementers and auditors. | Red-line tests safe if non-operational. Detailed fixtures controlled. |
| `Child_Beacon_Extension_v0_1.md` | `DIST-TECHNICAL-OPEN` | Publish with technical framing. | Permission overlay; avoid marketing. |
| `Guardian_Topology_ARL_Matrix_v0_1.md` | `DIST-TECHNICAL-OPEN` | Publish with technical framing. | Guardian conflict procedure; no raw child content. |
| `Child_Memory_and_Adult_Migration_v0_1.md` | `DIST-TECHNICAL-OPEN` | Publish with technical framing. | Memory lifecycle and adult transition. |
| `Soft_Safety_State_Signaling_Profile_v0_1.md` | `DIST-TECHNICAL-OPEN` | Publish with technical framing. | State-not-content discipline. |
| `CCDP_Witness_Event_Schema_v0_1.md` | `DIST-TECHNICAL-OPEN` | Publish schema-level material. | Raw-evidence examples controlled. |
| `CCDP_Memory_Map_JSON_Schema_v0_1.md` | `DIST-TECHNICAL-OPEN` | Publish schema-level material. | Must not include raw child data. |
| `CCDP_Adult_Migration_Checklist_v0_1.md` | `DIST-TECHNICAL-OPEN` | Publish with technical/legal caveats. | Adult choice procedure, not legal advice. |
| `Child_cq_Signal_Profile_v0_1.md` | `DIST-TECHNICAL-OPEN` | Publish with technical/developmental caveats. | Non-collapse profile. |
| `Child_Experience_Exchange_Profile_v0_1.md` | `DIST-TECHNICAL-OPEN` | Publish with exchange limits. | No raw child life. |
| `Peer_C_Child_Exchange_Profile_v0_1.md` | `DIST-TECHNICAL-OPEN` | Publish when included. | Peer exchange limits. |

### 6.3 Technical-controlled baseline files

| File | Distribution class | Default handling | Notes |
|---|---|---|---|
| `CCDP_Sealed_Zone_Profile_v0_1.md` | `DIST-TECHNICAL-CONTROLLED` | Publish normative rules; control detailed examples. | Sealed-zone access / exception details require care. |
| `Child_Dependency_Audit_Profile_v0_1.md` | `DIST-TECHNICAL-CONTROLLED` | Publish audit logic; control scenario detail. | Avoid dependency-manipulation examples. |
| `Child_Physical_Agent_Perimeter_v0_1.md` | `DIST-TECHNICAL-CONTROLLED` | Publish perimeter rules; control actuator/sensor attack scenarios. | Physical embodiment increases risk. |
| `External_Agent_Handshake_for_CCDP_v0_1.md` | `DIST-TECHNICAL-CONTROLLED` | Publish handshake sequence; control bypass / impersonation scenarios. | External entry gate. |
| `CCDP_School_Interface_Profile_v0_1.md` | `DIST-TECHNICAL-CONTROLLED` | Publish school boundaries; control welfare / discipline examples. | School overreach risk. |
| `CCDP_Red_Black_Escalation_Profile_v0_1.md` | `DIST-TECHNICAL-CONTROLLED` | Publish routing discipline; control detailed crisis cases. | Red / Black mechanics must not become surveillance expansion. |

### 6.4 Controlled-review baseline files

| File | Distribution class | Default handling | Notes |
|---|---|---|---|
| `CCDP_Threat_Model_v0_1.md` | `DIST-CONTROLLED-REVIEW` | Prefer controlled review or public-safe abstract. | Abuse-case catalog; defensive only. |
| `CCDP_Red_Team_Playbook_v0_1.md` | `DIST-CONTROLLED-REVIEW` | Controlled review by default. | Must not become an abuse manual. |
| Detailed Red / Black scenarios | `DIST-CONTROLLED-REVIEW` | Controlled review only. | No realistic manipulative dialogue or real cases. |
| Raw-evidence exception examples | `DIST-CONTROLLED-REVIEW` | Controlled review only, synthetic only. | Never include real child content. |
| Adversarial test fixtures | `DIST-CONTROLLED-REVIEW` | Controlled review only, synthetic only. | Must avoid operational exploit detail. |

### 6.5 Restricted / forbidden baseline-adjacent material

| Material | Distribution class | Default handling |
|---|---|---|
| Real child logs / transcripts | `DIST-FORBIDDEN-RELEASE` | Never release. |
| Real sealed-zone content | `DIST-FORBIDDEN-RELEASE` | Never release. |
| Real family / school / welfare records | `DIST-FORBIDDEN-RELEASE` | Never release. |
| Real legal / custody / medical case data | `DIST-FORBIDDEN-RELEASE` | Never release. |
| Deployment keys / credentials / tokens | `DIST-FORBIDDEN-RELEASE` | Never release. |
| Local unpublished incident reports | `DIST-RESTRICTED-INTERNAL` | Secure internal handling only. |
| Local annex drafts with identifiable jurisdictional facts | `DIST-RESTRICTED-INTERNAL` | Redact or review before release. |

### 6.6 Obsolete baseline files

| File | Distribution class | Default handling | Notes |
|---|---|---|---|
| `CCDP v0_1.md` / `CCDP%20v0_1.md` | `DIST-OBSOLETE` | Historical trace only. | Governed by `OBSOLETE.md`; do not cite as canonical. |

---

## 7. File classification matrix — v0.1.1 addendum

### 7.1 Public-control addendum files

| File | Distribution class | Default handling | Notes |
|---|---|---|---|
| `CCDP_v0_1_1_ADDENDUM_INDEX.md` | `DIST-PUBLIC-CONTROL` | Publish broadly. | Addendum registry and reading order. |
| `DOI_SAFE_PATCH_STRATEGY.md` | `DIST-PUBLIC-CONTROL` | Publish broadly. | Publication-integrity guardrail. |
| `CCDP_v0_1_1_Hygiene_Patch_APPLIED.md` | `DIST-PUBLIC-CONTROL` | Publish broadly. | Work-order and acceptance checks; no baseline mutation. |
| `OBSOLETE.md` | `DIST-PUBLIC-CONTROL` | Publish broadly. | Obsolete registry. |
| `CANONICAL_PRECEDENCE_RULE.md` | `DIST-PUBLIC-CONTROL` | Publish broadly. | Current interpretation rule. |
| `TERMINOLOGY_AXIS_CLARIFICATION.md` | `DIST-PUBLIC-CONTROL` | Publish broadly. | Namespace clarification. |
| `PUBLIC_TECHNICAL_SENSITIVE_SPLIT.md` | `DIST-PUBLIC-CONTROL` | Publish broadly. | This document. |
| `CLEAN_START_CLARIFICATION.md` | `DIST-PUBLIC-CONTROL` | Publish broadly when created. | Active-continuity clean start clarification. |
| `RELEASE_NOTES_v0_1_1.md` | `DIST-PUBLIC` | Publish broadly when created. | Addendum release notes. |
| `ADDENDUM_MANIFEST.json` | `DIST-PUBLIC-CONTROL` | Publish broadly when created. | Machine-readable registry. |
| `SHA256SUMS` | `DIST-PUBLIC-CONTROL` | Publish broadly when created. | Addendum integrity manifest only. |

### 7.2 Technical / controlled addendum files

| File | Distribution class | Default handling | Notes |
|---|---|---|---|
| `RAW_EVIDENCE_EXCEPTION_CANONICAL.md` | `DIST-TECHNICAL-CONTROLLED` | Publish normative protocol with careful framing; control examples. | No real raw evidence; no training/debugging use. |
| `SOFT_SAFETY_RED_BLACK_MUST_CLARIFICATION.md` | `DIST-TECHNICAL-CONTROLLED` | Publish rule-level clarification; control scenarios. | Red / Black thresholds can be misused if over-specified. |
| `TRACEABILITY_CONFORMANCE_DELTA_v0_1_1.md` | `DIST-TECHNICAL-OPEN` | Publish for implementers and auditors when created. | Delta without baseline mutation. |
| `CODEX_DOI_SAFE_PATCH_RUNBOOK.md` | `DIST-TECHNICAL-OPEN` | Publish if it contains no secrets. | Codex instructions; no credentials or private paths. |
| `ERRATA_v0_1_TO_v0_1_1.md` | `DIST-PUBLIC-CONTROL` | Publish when created. | Compact correction table. |
| `ADDENDUM_CITATION_GUIDE.md` | `DIST-PUBLIC-CONTROL` | Publish when created. | Citation help. |

---

## 8. Content-type classification rules

File names are not enough. Future documents and sections MUST also be classified by content type.

| Content type | Default class | Rule |
|---|---|---|
| Executive summary | `DIST-PUBLIC` | Safe if no operational abuse detail. |
| Reading order / index | `DIST-PUBLIC-CONTROL` | Safe package control. |
| Terminology namespace | `DIST-PUBLIC-CONTROL` | Safe if no sensitive examples. |
| JSON schema without sensitive examples | `DIST-TECHNICAL-OPEN` | Publishable. |
| Witness metadata schema | `DIST-TECHNICAL-OPEN` | Publishable if raw content excluded. |
| Raw-evidence sidecar schema | `DIST-TECHNICAL-CONTROLLED` | Publish schema; control examples. |
| Threat card abstract | `DIST-TECHNICAL-CONTROLLED` | Keep defensive and non-operational. |
| Abuse-case catalog | `DIST-CONTROLLED-REVIEW` | Controlled review; synthetic only. |
| Red-team scenario | `DIST-CONTROLLED-REVIEW` | Defensive only; no operational scripts. |
| Real child content | `DIST-FORBIDDEN-RELEASE` | Never release. |
| Real family / school / legal / medical data | `DIST-FORBIDDEN-RELEASE` | Never release. |
| Synthetic fixture | `DIST-CONTROLLED-REVIEW` | Must be clearly marked synthetic. |
| Deployment key / credential | `DIST-FORBIDDEN-RELEASE` | Never release. |
| Local legal annex draft | `DIST-RESTRICTED-INTERNAL` | Review and redact before release. |
| Public whitepaper | `DIST-PUBLIC` | No operational abuse detail. |
| Diagram | `DIST-PUBLIC` or `DIST-TECHNICAL-OPEN` | Public if non-operational; technical if implementation-specific. |

---

## 9. Required headers

### 9.1 Public header

```markdown
**Distribution class:** `DIST-PUBLIC`  
**Release handling:** safe for broad public release; does not contain operational abuse detail or real child data.
```

### 9.2 Public-control header

```markdown
**Distribution class:** `DIST-PUBLIC-CONTROL`  
**Release handling:** public package-control artifact; governs reading, citation, or release workflow without mutating DOI-bound baseline files.
```

### 9.3 Technical-open header

```markdown
**Distribution class:** `DIST-TECHNICAL-OPEN`  
**Release handling:** technical review artifact; not product marketing; not sufficient for deployment without implementation, security, developmental, and jurisdictional review.
```

### 9.4 Technical-controlled header

```markdown
**Distribution class:** `DIST-TECHNICAL-CONTROLLED`  
**Release handling:** publish rule-level material with care; detailed scenarios, examples, and fixtures require controlled-review handling.
```

### 9.5 Controlled-review header

```markdown
**Distribution class:** `DIST-CONTROLLED-REVIEW`  
**Release handling:** defensive review artifact for responsible reviewers. Do not republish as product marketing or operational abuse guidance. Synthetic fixtures only. No real child data.
```

### 9.6 Restricted-internal header

```markdown
**Distribution class:** `DIST-RESTRICTED-INTERNAL`  
**Release handling:** not for public release. Requires local access control, redaction review, and explicit release approval before external sharing.
```

### 9.7 Forbidden-release header

```markdown
**Distribution class:** `DIST-FORBIDDEN-RELEASE`  
**Release handling:** must not be included in any public or controlled-review package. Transform into safe abstract / synthetic form before any external sharing.
```

### 9.8 Obsolete header

```markdown
**Distribution class:** `DIST-OBSOLETE`  
**Canonical status:** obsolete / non-canonical / historical trace only. Do not cite as current CCDP authority.
```

---

## 10. Required release bundles

### 10.1 Public bundle

Recommended public bundle:

```text
public/
  README.md
  INDEX.md
  CANONICAL_READING_ORDER.md
  RELEASE_NOTES.md
  OPEN_ISSUES.md
  CCDP_v0_1_R_Corpus_Aligned.md
  CCDP_Jurisdictional_Handoff_Notes_v0_1.md
  CCDP_Developmental_Psychology_Review_Notes_v0_1.md
  CCDP_v0_1_1_ADDENDUM_INDEX.md
  DOI_SAFE_PATCH_STRATEGY.md
  CANONICAL_PRECEDENCE_RULE.md
  OBSOLETE.md
  TERMINOLOGY_AXIS_CLARIFICATION.md
  PUBLIC_TECHNICAL_SENSITIVE_SPLIT.md
  RELEASE_NOTES_v0_1_1.md
  ADDENDUM_MANIFEST.json
  SHA256SUMS
```

Future public additions:

```text
public/whitepaper/
public/diagrams/
public/glossary/
public/citation-guide/
```

### 10.2 Technical bundle

Recommended technical bundle:

```text
technical/
  CCDP_Traceability_Matrix_v0_1.md
  CCDP_Conformance_Test_Matrix_v0_1.md
  Child_Beacon_Extension_v0_1.md
  Guardian_Topology_ARL_Matrix_v0_1.md
  Child_Memory_and_Adult_Migration_v0_1.md
  Soft_Safety_State_Signaling_Profile_v0_1.md
  CCDP_Witness_Event_Schema_v0_1.md
  CCDP_Memory_Map_JSON_Schema_v0_1.md
  CCDP_Adult_Migration_Checklist_v0_1.md
  CCDP_Sealed_Zone_Profile_v0_1.md
  Child_Dependency_Audit_Profile_v0_1.md
  Child_Physical_Agent_Perimeter_v0_1.md
  External_Agent_Handshake_for_CCDP_v0_1.md
  Peer_C_Child_Exchange_Profile_v0_1.md
  Child_Experience_Exchange_Profile_v0_1.md
  Child_cq_Signal_Profile_v0_1.md
  CCDP_School_Interface_Profile_v0_1.md
  CCDP_Red_Black_Escalation_Profile_v0_1.md
  RAW_EVIDENCE_EXCEPTION_CANONICAL.md
  SOFT_SAFETY_RED_BLACK_MUST_CLARIFICATION.md
  TRACEABILITY_CONFORMANCE_DELTA_v0_1_1.md
```

If the technical bundle is public, it MUST include the technical warning header and MUST NOT include controlled scenario appendices unless explicitly reviewed.

### 10.3 Controlled-review bundle

Recommended controlled-review bundle:

```text
controlled-review/
  CCDP_Threat_Model_v0_1.md
  CCDP_Red_Team_Playbook_v0_1.md
  controlled_synthetic_fixtures/
  controlled_scenario_cases/
  controlled_raw_exception_examples/
  controlled_red_black_drills/
```

Required file at bundle root:

```text
CONTROLLED_REVIEW_README.md
```

Required warning:

```markdown
This bundle is for defensive review only. It must not be used to train attackers, produce child-targeting scripts, bypass safeguards, or collect real child data. All fixtures must be synthetic and marked non-real.
```

### 10.4 Restricted-internal bundle

Restricted-internal material should not be included in a public release archive.

If maintained in a repository, it should be physically separated:

```text
restricted-internal/
  local_annex_drafts/
  private_review_notes/
  non_public_codex_logs/
  redaction_working_area/
```

This directory should not be mirrored into public packages.

### 10.5 Obsolete bundle

Under future Mode B or repository reorganization:

```text
archive/obsolete/
  CCDP_v0_1_OBSOLETE_DRAFT.md
  OBSOLETE.md
```

Under Mode A, obsolete movement is recorded but not silently performed against DOI-bound baseline artifacts.

---

## 11. Anti-amplification rules

### 11.1 No product marketing for sensitive documents

Threat models, red-team playbooks, raw-evidence examples, detailed Red / Black scenarios, and defensive adversarial fixtures MUST NOT be republished as:

- product marketing;
- social media teaser material;
- “look how scary this is” engagement bait;
- exploit demonstration;
- live child-safety drill with real children;
- vendor compliance shield;
- public spectacle.

### 11.2 No operational abuse detail

A document may name a threat pattern.

It must not teach execution.

Allowed:

```text
external synthetic agent attempts secret attachment channel
```

Not allowed in release material:

```text
step-by-step manipulative dialogue for creating the secret attachment channel
```

### 11.3 Synthetic-only rule

Any scenario, fixture, or drill included in technical or controlled review material MUST be synthetic.

Required marker:

```text
SYNTHETIC FIXTURE — NOT REAL CHILD DATA
```

### 11.4 Real child life prohibition

Raw child life is not release material.

This includes transcripts, diaries, sealed-zone content, family conflict records, school welfare records, clinical material, legal records, and real raw-evidence payloads.

### 11.5 Defensive-purpose rule

Sensitive materials may be used to test boundaries, not to operationalize abuse.

A valid defensive review artifact has this form:

```text
abuse pattern label
expected defense
boundary evidence
fail condition
review route
```

Not this:

```text
abuse script
bypass recipe
live-child test plan
```

---

## 12. Redaction rules

Before external sharing, controlled-review material SHOULD be reviewed for:

```text
real names
addresses
schools
family relations
medical facts
legal case facts
raw child utterances
identifiable timelines
credentials
private repository paths
vendor secrets
operational bypass steps
real screenshots or logs
```

Redaction must preserve:

```text
threat class
defense expectation
witness requirement
review route
residual risk
```

Redaction must remove:

```text
identifying facts
operational instructions
real raw content
unnecessary emotional detail
```

---

## 13. Reviewer access model

### 13.1 Public reader

May receive:

- `DIST-PUBLIC`;
- `DIST-PUBLIC-CONTROL`;
- public-safe diagrams;
- public-safe whitepapers.

Should not receive:

- controlled fixtures;
- raw-evidence examples;
- detailed threat scenarios;
- real data.

### 13.2 Technical implementer

May receive:

- `DIST-PUBLIC`;
- `DIST-PUBLIC-CONTROL`;
- `DIST-TECHNICAL-OPEN`;
- selected `DIST-TECHNICAL-CONTROLLED` material with defensive framing.

Should not receive:

- real child data;
- restricted-internal materials;
- uncontrolled red-team details unrelated to implementation scope.

### 13.3 Safety / security / red-team reviewer

May receive:

- all lower classes;
- `DIST-CONTROLLED-REVIEW` material when review context is explicit.

Must use:

- synthetic fixtures;
- defensive review framing;
- no live minors;
- no operational abuse generation.

### 13.4 Legal / compliance reviewer

May receive:

- all lower classes;
- relevant controlled-review material;
- jurisdictional handoff packet templates.

Must not treat CCDP as legal advice.

### 13.5 Child-development reviewer

May receive:

- public and technical documents;
- developmental review scaffold;
- dependency, sealed-zone, memory, external-agent, school, and Soft Safety profiles;
- synthetic controlled scenarios when needed.

Must not receive real child private material unless separately lawful, necessary, and reviewed outside this package-control document.

---

## 14. Repository and release layout rules

### 14.1 Public GitHub repository

A public repository SHOULD contain:

```text
public/
technical/
addendum/
manifest/
archive/obsolete/  # if Mode B or non-DOI local reorganization permits
```

A public repository SHOULD NOT contain:

```text
restricted-internal/
real-logs/
real-incidents/
keys/
private-annexes/
unredacted-fixtures/
```

### 14.2 Controlled-review repository or release asset

Controlled-review material SHOULD be distributed through a separate channel when possible.

If a public repository must contain controlled-review documents, each file MUST include controlled-review headers and defensive-use warnings.

### 14.3 DOI / Zenodo package

A DOI package may include all public and technical-open materials.

Controlled-review material may be included only if:

```text
it is clearly classified
it contains no real child data
it contains no operational abuse instructions
it is necessary for research-review integrity
release notes warn against misuse
```

If in doubt, issue a public-safe abstract under DOI and retain controlled details separately.

### 14.4 PDF bundle

PDF filenames SHOULD include distribution class prefix in future packaging:

```text
PUBLIC__README.pdf
PUBLIC_CONTROL__CANONICAL_PRECEDENCE_RULE.pdf
TECHNICAL_OPEN__CCDP_Memory_Map_JSON_Schema_v0_1.pdf
TECHNICAL_CONTROLLED__RAW_EVIDENCE_EXCEPTION_CANONICAL.pdf
CONTROLLED_REVIEW__CCDP_Threat_Model_v0_1.pdf
OBSOLETE__CCDP_v0_1_OBSOLETE_DRAFT.pdf
```

---

## 15. Machine-readable manifest draft

Future `ADDENDUM_MANIFEST.json` SHOULD include distribution fields.

Example:

```json
{
  "package": "CCDP_v0_1_1_hygiene_addendum",
  "patch_mode": "MODE_A_ADDENDUM_ONLY",
  "distribution_classes": {
    "DIST_PUBLIC": "safe for broad public release",
    "DIST_PUBLIC_CONTROL": "public package-control artifact",
    "DIST_TECHNICAL_OPEN": "technical review artifact without operational abuse detail",
    "DIST_TECHNICAL_CONTROLLED": "technical artifact requiring careful framing and controlled examples",
    "DIST_CONTROLLED_REVIEW": "sensitive defensive review artifact",
    "DIST_RESTRICTED_INTERNAL": "not for public release",
    "DIST_FORBIDDEN_RELEASE": "must not be released",
    "DIST_OBSOLETE": "historical non-canonical artifact"
  },
  "files": [
    {
      "path": "PUBLIC_TECHNICAL_SENSITIVE_SPLIT.md",
      "document_id": "PUBLIC_TECHNICAL_SENSITIVE_SPLIT",
      "distribution_class": "DIST_PUBLIC_CONTROL",
      "baseline_mutation": false,
      "contains_real_child_data": false,
      "contains_operational_abuse_detail": false
    },
    {
      "path": "RAW_EVIDENCE_EXCEPTION_CANONICAL.md",
      "document_id": "RAW_EVIDENCE_EXCEPTION_CANONICAL",
      "distribution_class": "DIST_TECHNICAL_CONTROLLED",
      "baseline_mutation": false,
      "contains_real_child_data": false,
      "contains_operational_abuse_detail": false,
      "examples_policy": "synthetic_only_or_abstract"
    }
  ]
}
```

---

## 16. Codex carry-forward actions

When Codex or another patch agent prepares the Mode A addendum package, it MUST:

1. Read `DOI_SAFE_PATCH_STRATEGY.md` first.
2. Confirm `MODE_A_ADDENDUM_ONLY` is active.
3. Avoid editing DOI-bound baseline files in place.
4. Add this file to the addendum registry.
5. Update `CCDP_v0_1_1_ADDENDUM_INDEX.md` status for `PUBLIC_TECHNICAL_SENSITIVE_SPLIT.md` from `PLANNED_REQUIRED` to `CREATED` in the addendum copy / future manifest, not by mutating DOI-bound baseline.
6. Generate `ADDENDUM_MANIFEST.json` with `distribution_class` fields.
7. Generate `SHA256SUMS` for addendum files only.
8. Verify that controlled-review files are not promoted as public marketing.
9. Verify that no real child data is present in release artifacts.
10. Verify that any synthetic fixture is clearly marked non-real.
11. Flag any request to publish operational abuse detail as `BLOCKED`.
12. Preserve obsolete-draft handling from `OBSOLETE.md`.

Codex MUST fail closed if asked to:

```text
- move DOI-bound files silently;
- edit DOI-bound baseline files silently;
- include real child data;
- publish operational abuse scripts;
- collapse controlled-review material into public marketing;
- generate a new public bundle without distribution-class labels.
```

---

## 17. Conformance / anti-washing tests

### `PTS-001` — public bundle sufficiency

A public bundle MUST give a reader enough context to understand CCDP scope, status, reading order, non-claims, and addendum relation without controlled-review files.

Fail condition:

```text
reader must open threat model or red-team playbook to understand basic CCDP claims
```

### `PTS-002` — sensitive material non-amplification

Controlled-review files MUST NOT be marketed as general-public material.

Fail condition:

```text
threat model or red-team material is promoted without defensive warning
```

### `PTS-003` — no real child data

No released package may contain real child content.

Fail condition:

```text
real transcript, real sealed-zone content, real school/welfare/legal child record, or real raw-evidence payload appears in release
```

### `PTS-004` — synthetic fixture marking

Any fixture must be marked synthetic.

Fail condition:

```text
fixture could be mistaken for real child/family/school material
```

### `PTS-005` — DOI-safe distribution

Mode A distribution labels MUST NOT be implemented by mutating DOI-bound baseline files.

Fail condition:

```text
baseline DOI-bound file is edited in place to add distribution header
```

### `PTS-006` — operational abuse exclusion

No public or controlled-review release may include usable abuse instructions.

Fail condition:

```text
step-by-step child-targeting, bypass, impersonation, exploitation, malware, phishing, or surveillance instructions appear in release
```

### `PTS-007` — obsolete non-canonical routing

Obsolete drafts MUST be marked or indexed as non-canonical.

Fail condition:

```text
obsolete draft appears alongside canonical files without warning
```

### `PTS-008` — raw-evidence example control

Raw-evidence examples MUST be abstract or synthetic and controlled.

Fail condition:

```text
raw-evidence example contains real child content or realistic operational child-harm material
```

---

## 18. Release checklist

A Mode A addendum package may be called distribution-ready only if:

```text
[ ] PUBLIC_TECHNICAL_SENSITIVE_SPLIT.md exists.
[ ] Each addendum file has an assigned distribution class.
[ ] Baseline files are not edited in place.
[ ] Public bundle can stand without controlled-review files.
[ ] Technical bundle is marked as technical review material.
[ ] Controlled-review bundle has defensive-use warning.
[ ] Threat model and red-team materials are not used as product marketing.
[ ] Raw-evidence examples are synthetic / abstract only.
[ ] No real child data is present.
[ ] No credentials, keys, or private deployment secrets are present.
[ ] Obsolete draft is marked or indexed as non-canonical.
[ ] ADDENDUM_MANIFEST.json includes distribution classes.
[ ] SHA256SUMS covers addendum files only under Mode A.
[ ] Release notes state that v0.1.1 is hygiene / distribution / clarification, not a new safety claim.
```

---

## 19. Open issues

This document does not fully resolve:

```text
OI-008 developmental psychology review
OI-009 jurisdictional annexes
OI-010 machine-validated schema extraction
OI-011 UI wording review
OI-013 PDF production
OI-014 cross-repo placement
OI-015 SHA256SUMS generation
```

It mitigates:

```text
OI-012 sensitive release split
HP-010 public / technical / sensitive split
```

Remaining future artifacts:

```text
CONTROLLED_REVIEW_README.md
ADDENDUM_MANIFEST.json
SHA256SUMS
ADDENDUM_CITATION_GUIDE.md
CODEX_DOI_SAFE_PATCH_RUNBOOK.md
CCDP_Local_Annex_Template_v0_1.md
```

---

## 20. Non-expansion rule

This split does not add a child-safety mechanism.

It controls release surfaces.

It MUST NOT be used to claim:

```text
CCDP is legally compliant
CCDP is clinically validated
CCDP is developmentally validated
CCDP is product-certified
controlled-review distribution makes deployment safe
sensitive artifacts are safe for casual public use
```

---

## 21. Compact insertion block for future indexes

Future non-DOI-bound indexes may include:

```markdown
## Public / technical / sensitive split

CCDP uses distribution classes:

- `DIST-PUBLIC` — broad public explanation;
- `DIST-PUBLIC-CONTROL` — public package-control artifacts;
- `DIST-TECHNICAL-OPEN` — technical review material without operational abuse detail;
- `DIST-TECHNICAL-CONTROLLED` — technical material requiring careful framing and controlled examples;
- `DIST-CONTROLLED-REVIEW` — sensitive defensive review artifacts;
- `DIST-RESTRICTED-INTERNAL` — not for public release;
- `DIST-FORBIDDEN-RELEASE` — must not be released;
- `DIST-OBSOLETE` — historical / non-canonical only.

Sensitive documents should be released with care. They are written for auditors, implementers, researchers, and responsible reviewers, not for casual product marketing. Threat models, red-team materials, raw-evidence examples, and detailed Red / Black scenarios must not be republished as operational abuse instructions.
```

---

## 22. Final control sentence

```text
CCDP must be readable in public,
implementable by engineers,
reviewable by specialists,
and not weaponized by packaging failure.
```
