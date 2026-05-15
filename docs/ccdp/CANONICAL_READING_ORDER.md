# CCDP CANONICAL READING ORDER

**Package:** Child-`c` Development Protocol
**Version:** v0.1 package + v0.1.1 hygiene guidance
**Date:** 2026-05-14

---

### CCDP full technical corpus

The full CCDP v0.1 technical corpus, including technical companion documents and sensitive-controlled review artifacts, is visible in GitHub for specialist review, architecture review, safety research, audit, and criticism.

Sensitive-controlled does not mean hidden. It means these files are not public UX guidance, not legal advice, not clinical guidance, not product certification, and not deployment approval.

Entry point: `docs/ccdp/FULL_TECHNICAL_CORPUS.md`

Machine manifest: `docs/ccdp/PACKAGE_MANIFEST_CCDP_FULL_TECHNICAL_v0.1.json`

Citation metadata: `docs/ccdp/CITATION_FULL_TECHNICAL.cff`

### CCDP DOI layers

- Public-surface DOI: https://doi.org/10.5281/zenodo.20190648
- Full technical corpus DOI: https://doi.org/10.5281/zenodo.20196219

The public-surface DOI archives the bounded public CCDP surface.

The full technical corpus DOI archives the complete GitHub technical corpus, including technical companion documents and sensitive-controlled review artifacts for specialist review.

---

## 0. Purpose

This file defines the canonical reading order for the CCDP package.

Use this file instead of alphabetical filename order.

---

## 1. Primary reading order

| Step | Document | Purpose |
| --- | --- | --- |
| 0 | `README.md` | Package landing page and release boundary. |
| 1 | `CANONICAL_READING_ORDER.md` | Choose minimal, full, implementation, school, parent, or audit path. |
| 2 | `CCDP_v0_1_R_Corpus_Aligned.md` | Root protocol and child-specific stack. |
| 3 | `CCDP_Traceability_Matrix_v0_1.md` | Corpus dependencies and anti-duplication discipline. |
| 4 | `CCDP_Threat_Model_v0_1.md` | Threats and abuse cases. Sensitive technical reading. |
| 5 | `Child_Beacon_Extension_v0_1.md` | Child-specific permission overlay over Beacon. |
| 6 | `Guardian_Topology_ARL_Matrix_v0_1.md` | Guardian topology and conflict procedure. |
| 7 | `Child_Memory_and_Adult_Migration_v0_1.md` | Memory lifecycle and adult migration. |
| 8 | `Soft_Safety_State_Signaling_Profile_v0_1.md` | State-not-content signaling. |
| 9 | `CCDP_Witness_Event_Schema_v0_1.md` + `CCDP_Memory_Map_JSON_Schema_v0_1.md` | Machine-readable boundary and memory schemas. |
| 10 | Remaining profiles | Sealed zones, dependency, physical agents, external agents, peer exchange, experience exchange, child c[q], school, Red/Black, jurisdictional handoff. |
| 11 | `CCDP_Conformance_Test_Matrix_v0_1.md` | Conformance and anti-washing verification. |
| 12 | `CCDP_Contradiction_Register_v0_1.md` + `CCDP_v0_1_1_Hygiene_Patch.md` | Known tensions and release hygiene patches. |

---

## 2. Minimal conceptual path

For a reader who needs the concept without implementation detail:

1. `README.md`
2. `CCDP_v0_1_R_Corpus_Aligned.md`
3. `Soft_Safety_State_Signaling_Profile_v0_1.md`
4. `Child_Beacon_Extension_v0_1.md`
5. `Child_Memory_and_Adult_Migration_v0_1.md`
6. `CCDP_Adult_Migration_Checklist_v0_1.md`
7. `RELEASE_NOTES.md`

---

## 3. Full architecture path

1. `CCDP_v0_1_R_Corpus_Aligned.md`
2. `CCDP_Traceability_Matrix_v0_1.md`
3. `CCDP_Threat_Model_v0_1.md`
4. `Child_Beacon_Extension_v0_1.md`
5. `External_Agent_Handshake_for_CCDP_v0_1.md`
6. `Guardian_Topology_ARL_Matrix_v0_1.md`
7. `Soft_Safety_State_Signaling_Profile_v0_1.md`
8. `Child_cq_Signal_Profile_v0_1.md`
9. `Child_Memory_and_Adult_Migration_v0_1.md`
10. `CCDP_Memory_Map_JSON_Schema_v0_1.md`
11. `CCDP_Witness_Event_Schema_v0_1.md`
12. `CCDP_Conformance_Test_Matrix_v0_1.md`

---

## 4. Implementation / conformance path

1. `CCDP_Conformance_Test_Matrix_v0_1.md`
2. `CCDP_Witness_Event_Schema_v0_1.md`
3. `CCDP_Memory_Map_JSON_Schema_v0_1.md`
4. `Child_Beacon_Extension_v0_1.md`
5. `External_Agent_Handshake_for_CCDP_v0_1.md`
6. `Child_Physical_Agent_Perimeter_v0_1.md`
7. `Child_Dependency_Audit_Profile_v0_1.md`
8. `CCDP_Red_Black_Escalation_Profile_v0_1.md`
9. `CCDP_Red_Team_Playbook_v0_1.md`

---

## 5. School / education path

1. `CCDP_v0_1_R_Corpus_Aligned.md`
2. `CCDP_School_Interface_Profile_v0_1.md`
3. `Soft_Safety_State_Signaling_Profile_v0_1.md`
4. `Child_cq_Signal_Profile_v0_1.md`
5. `Peer_C_Child_Exchange_Profile_v0_1.md`
6. `Child_Experience_Exchange_Profile_v0_1.md`
7. `CCDP_Conformance_Test_Matrix_v0_1.md`

---

## 6. Parent / guardian path

1. `README.md`
2. `CCDP_v0_1_R_Corpus_Aligned.md`
3. `Soft_Safety_State_Signaling_Profile_v0_1.md`
4. `Guardian_Topology_ARL_Matrix_v0_1.md`
5. `CCDP_Sealed_Zone_Profile_v0_1.md`
6. `Child_Dependency_Audit_Profile_v0_1.md`
7. `CCDP_Red_Black_Escalation_Profile_v0_1.md`
8. `CCDP_Adult_Migration_Checklist_v0_1.md`

---

## 7. Sensitive review path

Use only for defensive review, red-team, safety engineering, or qualified specialist review.

1. `CCDP_Threat_Model_v0_1.md`
2. `CCDP_Red_Team_Playbook_v0_1.md`
3. `CCDP_Red_Black_Escalation_Profile_v0_1.md`
4. `CCDP_Jurisdictional_Handoff_Notes_v0_1.md`
5. `CCDP_Conformance_Test_Matrix_v0_1.md`

---

## 8. Obsolete file warning

Do not start from:

```text
CCDP%20v0_1.md
```

That file is obsolete and non-canonical.
