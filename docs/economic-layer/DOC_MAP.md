# DOC_MAP — Economic Layer for Experience Artifacts v0.1
## Canonical document map for the Economic Layer package

**Package:** Economic Layer for Experience Artifacts v0.1  
**Short name:** ELA v0.1  
**Canonical home:** `advanced-global-intelligence`  
**Author:** Ivan Kotov  
**Location:** Brussels  
**Year:** 2026  

---

## 1. Purpose

This file defines the canonical document map for the Economic Layer package.

Its purpose is to prevent:
- confusion between normative core and supporting documents,
- drift between package-facing and rule-facing texts,
- duplicate interpretation during repository integration,
- and later publication chaos when PDF, hashes, and deposit objects are prepared.

This file is package-facing.
It does not replace the normative core.
Pre-Lineage Boundary Note remains a separate manifesto-level boundary note in AGI and is not part of the Economic Layer package.

---

## 2. Package structure

### 2.1 Primary entry documents

1. `README.md`  
   Package facade, external orientation, and high-level scope.

2. `INDEX.md`  
   Canonical reading order and package navigation.

3. `Executive_Summary_Economic_Layer_v0.1.md`  
   One-page dry public entry for quick review, audit triage, and public overview.

4. `Economic_Layer_for_Experience_Artifacts_v0.1.md`  
   **Normative core** of the package.

---

### 2.2 Normative support documents

5. `EA_Value_Class_Taxonomy_v0.1.md`  
   Canonical taxonomy of EA value classes and mixed-class collisions.

6. `Provenance_Admissibility_and_Transfer_Rules_v0.1.md`  
   Provenance discipline, admissibility thresholds, receiver-mode discipline, and transfer legality.

7. `Escrow_Freeze_and_Dispute_Hooks_for_EA_Exchange_v0.1.md`  
   Economic restraint states, release discipline, and ARL escalation hooks.

8. `Anti_Gaming_and_Synthetic_Laundering_Risk_Model_v0.1.md`  
   Threat model and fail-closed constraints against source laundering, prestige inflation, and cartelization.

9. `Disclosure_Privacy_and_Reusability_Boundaries_v0.1.md`  
   Disclosure classes, privacy-preserving handling, and lawful reuse limits.

---

### 2.3 Package-control documents

10. `DOC_MAP.md`  
    Canonical package map and document-role surface.

11. `Repository_Integration_Notes_Economic_Layer_v0.1.md`  
    Repository-facing placement and discoverability notes.

12. `Publication_and_Integrity_Notes_Economic_Layer_v0.1.md`  
    Publication-facing and integrity-facing notes for PDF, hash, and package-object formation.

13. `Consistency_Pass_Notes_Economic_Layer_v0.1.md`  
    Package-level invariant lock and cross-document consistency pass.

---

### 2.4 Published extension / satellite clauses

14. `extensions/ARL_vs_C_Continuity_Precedence_Clause_v0.1.md`
15. `extensions/EA_Circulation_Rights_v0.1.md`
16. `extensions/EA_Non_Transferability_Criteria_v0.1.md`
17. `extensions/EA_Operative_vs_Historical_Truth_Clause_v0.1.md`
18. `extensions/EA_Receiver_Mode_and_Fidelity_Clause_v0.1.md`
19. `extensions/EA_Scar_Status_Matrix_v0.1.md`
20. `extensions/EA_Transfer_Modes_v0.1.md`
21. `extensions/EA_Value_Non_Numeric_v0.1.md`
22. `extensions/Economic_Escrow_and_Circulation_Hold_Clause_v0.1.md`
23. `extensions/Economically_Admissible_But_Non_Market_EA_Clause_v0.1.md`
24. `extensions/Institutional_Emergence_of_EA_Value_v0.1.md`
25. `extensions/Jurisdiction_Bounded_Interop_Clause_v0.1.md`
26. `extensions/Lineage_Linked_EA_Value_and_Risk_Clause_v0.1.md`
27. `extensions/Property_Status_of_EA_v0.1.md`
28. `extensions/Scar_Bearing_EA_Clause_v0.1.md`
29. `extensions/Synthetic_Laundering_and_Source_Class_Clause_v0.1.md`

---

### 2.5 Published PDF surfaces

- root human-facing PDFs in `pdf/`
- extension PDFs in `pdf/extensions/`
- `pdf/extensions/EA_Scar_Status_Matrix_v0.1.pdf` is present
- helper/control PDFs are intentionally excluded from this GitHub package surface

---

## 3. Reading order

### 3.1 Recommended reading order for humans

1. `Executive_Summary_Economic_Layer_v0.1.md`
2. `Economic_Layer_for_Experience_Artifacts_v0.1.md`
3. `EA_Value_Class_Taxonomy_v0.1.md`
4. `Provenance_Admissibility_and_Transfer_Rules_v0.1.md`
5. `Escrow_Freeze_and_Dispute_Hooks_for_EA_Exchange_v0.1.md`
6. `Anti_Gaming_and_Synthetic_Laundering_Risk_Model_v0.1.md`
7. `Disclosure_Privacy_and_Reusability_Boundaries_v0.1.md`
8. `README.md`
9. `INDEX.md`

### 3.2 Recommended reading order for reviewers / auditors

1. `Executive_Summary_Economic_Layer_v0.1.md`
2. `Economic_Layer_for_Experience_Artifacts_v0.1.md`
3. `Provenance_Admissibility_and_Transfer_Rules_v0.1.md`
4. `Escrow_Freeze_and_Dispute_Hooks_for_EA_Exchange_v0.1.md`
5. `Anti_Gaming_and_Synthetic_Laundering_Risk_Model_v0.1.md`
6. `Disclosure_Privacy_and_Reusability_Boundaries_v0.1.md`
7. `EA_Value_Class_Taxonomy_v0.1.md`

### 3.3 Recommended reading order for implementation / downstream structuring

1. `Economic_Layer_for_Experience_Artifacts_v0.1.md`
2. `Provenance_Admissibility_and_Transfer_Rules_v0.1.md`
3. `Escrow_Freeze_and_Dispute_Hooks_for_EA_Exchange_v0.1.md`
4. `Disclosure_Privacy_and_Reusability_Boundaries_v0.1.md`
5. `Anti_Gaming_and_Synthetic_Laundering_Risk_Model_v0.1.md`
6. `EA_Value_Class_Taxonomy_v0.1.md`

---

## 4. Document roles

### 4.1 What is normative
The following documents are normative for ELA v0.1:

- `Economic_Layer_for_Experience_Artifacts_v0.1.md`
- `EA_Value_Class_Taxonomy_v0.1.md`
- `Provenance_Admissibility_and_Transfer_Rules_v0.1.md`
- `Escrow_Freeze_and_Dispute_Hooks_for_EA_Exchange_v0.1.md`
- `Anti_Gaming_and_Synthetic_Laundering_Risk_Model_v0.1.md`
- `Disclosure_Privacy_and_Reusability_Boundaries_v0.1.md`

### 4.2 What is orienting / package-facing
The following documents are orienting or package-facing:

- `README.md`
- `INDEX.md`
- `Executive_Summary_Economic_Layer_v0.1.md`
- `DOC_MAP.md`
- `Repository_Integration_Notes_Economic_Layer_v0.1.md`
- `Publication_and_Integrity_Notes_Economic_Layer_v0.1.md`
- `Consistency_Pass_Notes_Economic_Layer_v0.1.md`

---

## 5. Canonical bridges

### 5.1 Explicit bridge
**DEA / EA ↔ ARL ↔ Economic Layer**

### 5.2 Hidden bridges
- L4 scarcity / boundedness
- SER-FED anti-capture / anti-cartel

---

## 6. Earth paragraph

In a real supply chain, one binder tells you which paper is the shipping rule, which paper is the customs form, which paper is the inspection note, and which paper is just the quick front summary for the next shift. Without that map, people start improvising and the warehouse fills with “almost the same” versions of the truth. This document exists to stop that from happening to the Economic Layer package.

---

## 7. Current status

Current package status:
- text layer: assembled
- package-facing facade: assembled
- normative support docs: assembled
- package-control docs: assembled
- repository placement: present in `docs/economic-layer/`
- extension subtree: present in `extensions/`
- PDF layer: present in `pdf/` and `pdf/extensions/`
- helper/publication carpentry docs: intentionally excluded from GitHub
- SHA-256 manifest: pending
