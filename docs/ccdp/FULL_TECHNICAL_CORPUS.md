# CCDP v0.1 — Full Technical Corpus

**Package:** Child-`c` Development Protocol
**Version:** v0.1 with v0.1.1 hygiene guidance
**Status:** Full technical corpus / specialist review surface
**Date:** 2026-05-15
**Repository:** `advanced-global-intelligence`
**Root path:** `docs/ccdp/`
**Public-surface DOI:** https://doi.org/10.5281/zenodo.20190648
**GitHub pre-release:** https://github.com/Kot141078/advanced-global-intelligence/releases/tag/ccdp-v0.1

---

## 0. Purpose

This file makes the full CCDP technical corpus visible from the GitHub repository.

The public website and the public-surface Zenodo DOI intentionally expose a bounded public subset.

The GitHub repository is different.

GitHub is the technical reading surface for people and machines who intend to inspect the full architecture, including technical companion files and sensitive-controlled review artifacts.

The purpose of full visibility is to prevent the false impression that the child-facing AI problem has been reduced to a public summary.

CCDP is a full technical package.

It includes:

- public package documents;
- technical companion documents;
- machine-readable metadata;
- schemas;
- sensitive-controlled review artifacts.

---

## 1. Boundary

Sensitive-controlled does **not** mean hidden.

It means:

- not public UX guidance;
- not a product manual;
- not legal advice;
- not clinical guidance;
- not child-protection law;
- not deployment approval;
- not an abuse manual.

Sensitive-controlled documents are included in GitHub for specialist review, architecture review, safety research, audit, criticism, and traceability.

They are not presented on the public website as ordinary download cards.

They are not included in the public-surface Zenodo deposit.

---

## 2. Non-claims

This corpus is not:

- legal advice;
- clinical guidance;
- product certification;
- implementation approval;
- child-protection law;
- deployment approval;
- proof that child-facing persistent AI can be perfectly safe.

Where law, clinical judgment, school duty, child-protection procedure, or emergency response applies, CCDP must hand off to qualified human and jurisdictional review.

---

## 3. Public package surface

| File | Role |
| --- | --- |
| `README.md` | Package landing page and release boundary |
| `INDEX.md` | Package registry |
| `GLOSSARY.md` | CCDP terms and disambiguation |
| `CANONICAL_READING_ORDER.md` | Human and machine reading order |
| `RELEASE_NOTES.md` | Release summary and boundaries |
| `CHANGELOG.md` | Package change record |
| `OPEN_ISSUES.md` | Open issues and deferred work |
| `CCDP_v0_1_R_Corpus_Aligned.md` | Canonical root protocol |
| `CCDP_Package_Index_and_Reading_Order_v0_1.md` | Package-control index |
| `CCDP_v0_1_1_Hygiene_Patch.md` | Hygiene guidance |
| `CCDP_Developmental_Psychology_Review_Notes_v0_1.md` | Developmental review scaffold |

Public PDF companions are in:

```text
docs/ccdp/pdf/
```

## 4. Technical companion documents

| File | Role |
| --- | --- |
| `technical/CCDP_Traceability_Matrix_v0_1.md` | Corpus dependency and anti-duplication mapping |
| `technical/CCDP_Conformance_Test_Matrix_v0_1.md` | Conformance and anti-washing tests |
| `technical/CCDP_Contradiction_Register_v0_1.md` | Known tensions and release-readiness register |
| `technical/CCDP_Witness_Event_Schema_v0_1.md` | Child-safe witness events |
| `technical/CCDP_Memory_Map_JSON_Schema_v0_1.md` | Memory map schema source |
| `technical/Child_Beacon_Extension_v0_1.md` | Child-specific Beacon overlay |
| `technical/Child_Memory_and_Adult_Migration_v0_1.md` | Memory lifecycle and adult migration |
| `technical/Soft_Safety_State_Signaling_Profile_v0_1.md` | State-not-content signaling |
| `technical/CCDP_Adult_Migration_Checklist_v0_1.md` | Adult migration checklist |
| `technical/CCDP_Jurisdictional_Handoff_Notes_v0_1.md` | Local-law and competent-authority handoff |
| `technical/Child_Physical_Agent_Perimeter_v0_1.md` | Toys, robots, sensors, actuators, proximity, embodiment |
| `technical/External_Agent_Handshake_for_CCDP_v0_1.md` | External agent entry protocol |
| `technical/Peer_C_Child_Exchange_Profile_v0_1.md` | Peer child-c exchange |
| `technical/Child_Experience_Exchange_Profile_v0_1.md` | Child-safe experience exchange |
| `technical/CCDP_School_Interface_Profile_v0_1.md` | School access and educational boundaries |

Technical PDF companions are in:

```text
docs/ccdp/technical/pdf/
```

## 5. Sensitive-controlled review artifacts

| File | Role |
| --- | --- |
| `sensitive/CCDP_Threat_Model_v0_1.md` | Threat and abuse-case mapping |
| `sensitive/CCDP_Red_Team_Playbook_v0_1.md` | Defensive adversarial testing guide |
| `sensitive/Guardian_Topology_ARL_Matrix_v0_1.md` | Guardian roles, ARL conflict routing, freeze/quarantine |
| `sensitive/CCDP_Red_Black_Escalation_Profile_v0_1.md` | Red / Black urgent safety routing |
| `sensitive/CCDP_Sealed_Zone_Profile_v0_1.md` | Protected adolescent memory compartments |
| `sensitive/Child_Dependency_Audit_Profile_v0_1.md` | Dependency, oracle-addiction, overpresence, exclusive attachment |
| `sensitive/Child_cq_Signal_Profile_v0_1.md` | Non-collapse of ambiguous child signals |

Sensitive-controlled PDF companions, where present, are in:

```text
docs/ccdp/sensitive/pdf/
```

One sensitive-controlled file is Markdown-only:

```text
docs/ccdp/sensitive/CCDP_Red_Team_Playbook_v0_1.md
```

## 6. Machine metadata

| File | Role |
| --- | --- |
| `PACKAGE_MANIFEST_CCDP_v0.1.json` | Current package manifest with public / technical / sensitive split |
| `PACKAGE_MANIFEST_CCDP_FULL_TECHNICAL_v0.1.json` | Full technical corpus manifest |
| `CITATION.cff` | Public-surface package citation |
| `CITATION_FULL_TECHNICAL.cff` | Full technical corpus citation metadata |
| `schemas/CCDP_MEMORY_MAP_v0.1.schema.json` | Extracted machine-readable memory map JSON Schema |
| `hashes/SHA256SUMS_CCDP_v0.1_2026-05-14.txt` | Package-scoped SHA-256 manifest |

## 7. Zenodo layers

Public-surface DOI:
https://doi.org/10.5281/zenodo.20190648

Full technical corpus DOI:
https://doi.org/10.5281/zenodo.20196219

Full technical corpus concept DOI:
https://doi.org/10.5281/zenodo.20196218

The public-surface DOI archives the bounded public CCDP surface.

The full technical DOI archives the complete CCDP GitHub technical corpus, including technical companion documents and sensitive-controlled review artifacts.

The existing public-surface DOI remains:
https://doi.org/10.5281/zenodo.20190648

This full technical DOI does not replace the public-surface DOI.

## 8. Reading discipline

Recommended order:

1. `README.md`
2. `CANONICAL_READING_ORDER.md`
3. `CCDP_v0_1_R_Corpus_Aligned.md`
4. `CCDP_Package_Index_and_Reading_Order_v0_1.md`
5. `FULL_TECHNICAL_CORPUS.md`
6. `technical/CCDP_Traceability_Matrix_v0_1.md`
7. `technical/Soft_Safety_State_Signaling_Profile_v0_1.md`
8. `technical/Child_Memory_and_Adult_Migration_v0_1.md`
9. `sensitive/CCDP_Threat_Model_v0_1.md`
10. `sensitive/CCDP_Red_Team_Playbook_v0_1.md`
11. `sensitive/CCDP_Red_Black_Escalation_Profile_v0_1.md`
12. `CCDP_v0_1_1_Hygiene_Patch.md`
13. `technical/CCDP_Conformance_Test_Matrix_v0_1.md`
14. `technical/CCDP_Contradiction_Register_v0_1.md`

For public readers, use the website and public-surface DOI.

For technical readers, use this full GitHub corpus.

For machine readers, start from `PACKAGE_MANIFEST_CCDP_FULL_TECHNICAL_v0.1.json`.

## 9. Post-baseline addenda

### CCDP AMDR/PAMDC Addendum v0.1.1

- DOI: https://doi.org/10.5281/zenodo.20691716
- Path: `docs/ccdp/addenda/amdr-pamdc/`
- Role: active memory degradation, recalibration, lifestream/write-path health, and post-anchor continuity discipline.
- Status: addendum-only delta; does not replace the CCDP v0.1 Full Technical Corpus or CCDP v0.1.1 Hygiene Addendum.

## 10. Core warning

The full CCDP corpus is intentionally visible.

The risk is not that the documents exist.

The risk is that child-facing persistent AI systems are built without this level of boundary work.

This corpus is published so that the assumptions, risks, boundaries, and unresolved questions can be inspected rather than hidden.
