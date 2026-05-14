# CCDP INDEX

**Package:** Child-`c` Development Protocol
**Version:** v0.1 package + v0.1.1 hygiene guidance
**Date:** 2026-05-14

---

## 0. Purpose

This file is the package-level document registry for the CCDP corpus.

Use this file to find the canonical documents, identify obsolete drafts, and locate technical, public, sensitive, and control artifacts.

---

## 1. Canonical registry

| File | Role | Status |
| --- | --- | --- |
| `CCDP_v0_1_R_Corpus_Aligned.md` | Root protocol | Canonical base |
| `CCDP_Traceability_Matrix_v0_1.md` | Traceability / corpus-control | Canonical companion |
| `CCDP_Threat_Model_v0_1.md` | Threat model / abuse-case catalog | Canonical companion; sensitive |
| `Child_Beacon_Extension_v0_1.md` | Child-specific Beacon overlay | Canonical profile |
| `Guardian_Topology_ARL_Matrix_v0_1.md` | Guardian roles and ARL conflict matrix | Canonical profile |
| `Child_Memory_and_Adult_Migration_v0_1.md` | Memory lifecycle and adult migration | Canonical profile |
| `Soft_Safety_State_Signaling_Profile_v0_1.md` | State-not-content signaling | Canonical profile |
| `CCDP_Conformance_Test_Matrix_v0_1.md` | Conformance and anti-washing tests | Canonical test artifact |
| `CCDP_Witness_Event_Schema_v0_1.md` | Child-safe witness events | Canonical technical schema |
| `CCDP_Memory_Map_JSON_Schema_v0_1.md` | Memory map JSON schema | Canonical technical schema |
| `CCDP_Adult_Migration_Checklist_v0_1.md` | Adult migration procedure | Canonical checklist |
| `CCDP_Sealed_Zone_Profile_v0_1.md` | Sealed adolescent memory zones | Canonical profile |
| `Child_Dependency_Audit_Profile_v0_1.md` | Dependency / oracle addiction audit | Canonical profile |
| `Child_Physical_Agent_Perimeter_v0_1.md` | Toys / robots / embodied systems | Canonical profile |
| `External_Agent_Handshake_for_CCDP_v0_1.md` | External agent entry protocol | Canonical profile |
| `Peer_C_Child_Exchange_Profile_v0_1.md` | Peer child-c exchange | Canonical profile |
| `Child_Experience_Exchange_Profile_v0_1.md` | Child-safe experience exchange | Canonical profile |
| `Child_cq_Signal_Profile_v0_1.md` | Child c[q] non-collapse profile | Canonical profile |
| `CCDP_School_Interface_Profile_v0_1.md` | School access and educational signals | Canonical profile |
| `CCDP_Red_Black_Escalation_Profile_v0_1.md` | Red / Black crisis routing | Canonical profile |
| `CCDP_Jurisdictional_Handoff_Notes_v0_1.md` | Jurisdictional handoff notes | Canonical handoff artifact |
| `CCDP_Package_Index_and_Reading_Order_v0_1.md` | Package index and reading order | Canonical package-control |
| `CCDP_Contradiction_Register_v0_1.md` | Known tensions and contradictions register | Canonical package-control |
| `CCDP_v0_1_1_Hygiene_Patch.md` | v0.1.1 release hygiene patch | Canonical patch guidance |
| `CCDP_Developmental_Psychology_Review_Notes_v0_1.md` | Developmental psychology review scaffold | Review / handoff artifact |
| `CCDP_Red_Team_Playbook_v0_1.md` | Defensive red-team playbook | Sensitive review artifact |
| `CCDP%20v0_1.md` | Earlier conversational / workspace draft | OBSOLETE / NON-CANONICAL; retain only as history or move to archive/obsolete |

---

## 2. Packaging registry

| File | Role |
| --- | --- |
| `README.md` | Package landing page |
| `INDEX.md` | Document registry |
| `GLOSSARY.md` | Terminology |
| `CHANGELOG.md` | Version history |
| `RELEASE_NOTES.md` | Release summary |
| `OPEN_ISSUES.md` | Known gaps and next work |
| `CANONICAL_READING_ORDER.md` | Reading paths |

---

## 3. Document groups

### 3.1 Root and corpus-control

- `CCDP_v0_1_R_Corpus_Aligned.md`
- `CCDP_Traceability_Matrix_v0_1.md`
- `CCDP_Package_Index_and_Reading_Order_v0_1.md`
- `CCDP_Contradiction_Register_v0_1.md`
- `CCDP_v0_1_1_Hygiene_Patch.md`

### 3.2 Risk and testing

- `CCDP_Threat_Model_v0_1.md`
- `CCDP_Conformance_Test_Matrix_v0_1.md`
- `CCDP_Red_Team_Playbook_v0_1.md`

### 3.3 Recognition, access, and guardian topology

- `Child_Beacon_Extension_v0_1.md`
- `External_Agent_Handshake_for_CCDP_v0_1.md`
- `Guardian_Topology_ARL_Matrix_v0_1.md`
- `CCDP_Jurisdictional_Handoff_Notes_v0_1.md`

### 3.4 Memory, privacy, and migration

- `Child_Memory_and_Adult_Migration_v0_1.md`
- `CCDP_Memory_Map_JSON_Schema_v0_1.md`
- `CCDP_Adult_Migration_Checklist_v0_1.md`
- `CCDP_Sealed_Zone_Profile_v0_1.md`

### 3.5 Signals, dependency, and developmental safety

- `Soft_Safety_State_Signaling_Profile_v0_1.md`
- `Child_cq_Signal_Profile_v0_1.md`
- `Child_Dependency_Audit_Profile_v0_1.md`
- `CCDP_Developmental_Psychology_Review_Notes_v0_1.md`

### 3.6 Physical, school, peer, and exchange profiles

- `Child_Physical_Agent_Perimeter_v0_1.md`
- `CCDP_School_Interface_Profile_v0_1.md`
- `Peer_C_Child_Exchange_Profile_v0_1.md`
- `Child_Experience_Exchange_Profile_v0_1.md`

### 3.7 Witness and escalation

- `CCDP_Witness_Event_Schema_v0_1.md`
- `CCDP_Red_Black_Escalation_Profile_v0_1.md`

---

## 4. Obsolete material

`CCDP%20v0_1.md` is obsolete and non-canonical. It should be moved to an archive folder or renamed with an explicit `OBSOLETE` prefix before public release.

Recommended path:

```text
archive/obsolete/CCDP_v0_1_conceptual_draft_OBSOLETE.md
```

Recommended header:

```markdown
> OBSOLETE / NON-CANONICAL.
> Superseded by CCDP_v0_1_R_Corpus_Aligned.md.
> Retained only as conversational concept history.
```

---

## 5. SHA manifest note

`SHA256SUMS` is not included here. It should be generated by Codex after the final Markdown and PDF set is frozen.
