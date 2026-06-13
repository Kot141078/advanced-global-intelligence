# DOI-SAFE PATCH STRATEGY v0.1

## Addendum-only patch discipline for DOI-bound CCDP artifacts

**Author:** Kotov Ivan  
**Location:** Bruxelles, Belgium  
**Year:** 2026  
**DOI:** Reserved DOI: 10.5281/zenodo.20680938  

**Document ID:** `DOI_SAFE_PATCH_STRATEGY_v0_1`  
**Short name:** `DSP-0.1`  
**Status:** Draft release-control strategy  
**Date:** 2026-06-13  
**Mode selected:** `MODE_A_ADDENDUM_ONLY`  
**Package target:** CCDP v0.1 DOI-bound / release-bound corpus slice  
**Patch layer:** CCDP v0.1.1 hygiene addendum / publication integrity / Codex-safe patch routing  
**Document class:** release-control / DOI hygiene / corpus immutability strategy  
**Assertion class:** `C-A10` control-layer artifact; does not upgrade any child-safety, legal, clinical, or product-readiness claim  
**Legal status:** Not legal advice. Not DOI-provider policy. Not repository-host policy. This document defines internal corpus discipline for patching already published research artifacts without silently mutating cited objects.

---

## 0. Executive summary

This document defines how the CCDP corpus must be patched when the target documents are already **DOI-bound**, release-bound, PDF-paired, SHA-manifested, or otherwise externally citable.

The selected strategy is:

```text
MODE A = addendum-only patching.
```

Under Mode A:

1. the original DOI-bound CCDP v0.1 artifacts remain frozen;
2. no canonical v0.1 source file is silently edited in place;
3. no paired PDF is regenerated under the same identity;
4. no historical SHA manifest is overwritten;
5. v0.1.1 hygiene corrections are published as a separate addendum pack;
6. the addendum defines how v0.1 must be read for current use;
7. future full source edits require a new versioned release workflow, not Mode A.

Core rule:

> **A DOI-bound artifact is a witness object. It may be interpreted, clarified, deprecated, superseded, or versioned, but it must not be silently rewritten.**

---

## 1. Why this document exists

The CCDP v0.1 package has accumulated hygiene issues that should be corrected before broad release, implementation, audit, or conformance claims.

However, some source documents are already externally published, DOI-bound, paired with PDFs, or otherwise citable as fixed artifacts.

That creates a release-control tension:

```text
hygiene defects should be patched
but DOI-bound artifacts must remain historically stable
```

This document resolves the tension by selecting addendum-only patching as the safe default.

---

## 2. Scope

### 2.1 In scope

This strategy applies to:

- CCDP v0.1 source Markdown files already tied to DOI / release / citation state;
- paired PDFs generated from those files;
- SHA256 manifests or integrity records for the original release;
- v0.1.1 hygiene documents already created or planned;
- future Codex patch work on CCDP package hygiene;
- repository layout decisions around obsolete drafts;
- package indexes, release notes, and addendum manifests;
- public / technical / sensitive package split declarations;
- errata, clarification, deprecation, and supersession records.

### 2.2 Out of scope

This strategy does **not**:

- define DOI provider policy;
- define legal publication requirements;
- provide legal advice;
- alter the scientific claims of CCDP v0.1;
- validate CCDP child-safety claims;
- validate developmental psychology, legal compliance, or product readiness;
- create a new CCDP root protocol;
- create a new child-safety mechanism;
- create Mode B full versioned release artifacts.

---

## 3. Corpus bridge set

### 3.1 Explicit bridge

In the `c = a + b` frame, `c` depends on continuity, witness, and consequence. A published corpus must follow the same discipline. If the text that defines a protocol can be silently rewritten after it is cited, the corpus loses its own witness integrity.

Therefore, DOI-bound documents must behave like L4 witness objects:

```text
stable identity
stable content
stable citation boundary
explicit correction path
no silent mutation
```

### 3.2 Quiet bridge I

Ashby's law of requisite variety applies to publication control. One patch mode is not enough for every defect type. Typo correction, obsolete draft isolation, raw-evidence centralization, safety clarification, and full redesign require different routing states. Mode A provides variety without corrupting the historical baseline.

### 3.3 Quiet bridge II

Information theory applies to citation integrity. A DOI-bound document is a signal fixed in time. Silent mutation injects ambiguity into the channel: two readers cite the same object but may have read different content. An addendum preserves the original signal and transmits a second corrective signal.

### 3.4 Earth paragraph

In a building, an inspection report is not edited after the inspector signs it. If a defect is found later, a new correction sheet, addendum, or follow-up inspection is issued. The old report remains what it was. Otherwise no one can reconstruct what was known, when it was known, and who acted on which version. DOI-bound protocol documents require the same discipline.

---

## 4. Definitions

### 4.1 DOI-bound artifact

A **DOI-bound artifact** is any file, PDF, package, archive, release, or document whose content is externally citable through a DOI or DOI-linked publication record.

A DOI-bound artifact SHOULD be treated as immutable for scientific citation purposes.

### 4.2 Release-bound artifact

A **release-bound artifact** is any document tied to a tagged release, public package, SHA manifest, archived ZIP, GitHub release asset, Zenodo record, HAL entry, ORCID work entry, or equivalent public reference.

Release-bound artifacts may not have a DOI yet, but they still require mutation discipline.

### 4.3 Baseline package

The **baseline package** is the original CCDP v0.1 package as published or prepared for DOI / release citation.

In Mode A, the baseline package remains frozen.

### 4.4 Addendum

An **addendum** is a new document that clarifies, corrects, limits, deprecates, or supersedes interpretation of a baseline artifact without modifying the baseline artifact itself.

### 4.5 Erratum

An **erratum** records a known error in a baseline artifact.

An erratum does not rewrite the baseline.

### 4.6 Clarification

A **clarification** resolves ambiguity in baseline wording without claiming that the baseline text itself has changed.

### 4.7 Supersession

A **supersession** states that a newer document controls current interpretation or future implementation of a specific baseline issue.

Supersession does not alter historical citation of the baseline.

### 4.8 Silent mutation

A **silent mutation** is any in-place change to a DOI-bound or release-bound artifact without a new version identity, addendum record, changelog entry, and integrity trail.

Silent mutation is prohibited.

### 4.9 Paired PDF

A **paired PDF** is a PDF generated from a Markdown or source document and published as part of the same release identity.

If the source is DOI-bound, the paired PDF must be treated as DOI-bound too.

### 4.10 Codex patch run

A **Codex patch run** is a future automated or semi-automated repository modification session that may create, move, rename, edit, generate, or delete files.

Codex patch runs MUST follow this strategy when CCDP DOI-bound artifacts are in scope.

---

## 5. Selected strategy: Mode A

### 5.1 Mode A definition

Mode A is an addendum-only strategy:

```text
Original v0.1 artifacts remain frozen.
Patch documents are created as v0.1.1 addendum artifacts.
The addendum defines current reading, not historical replacement.
```

### 5.2 Mode A purpose

Mode A exists to:

- preserve DOI integrity;
- avoid silent source mutation;
- make corrections discoverable;
- allow hygiene improvements before a full v0.1.1 source release;
- support implementation and audit without confusing historical citations;
- give Codex a safe patch boundary.

### 5.3 Mode A non-goals

Mode A does not:

- regenerate the full CCDP source package;
- rewrite DOI-bound documents;
- create a new DOI by itself;
- claim that the baseline files have been patched;
- close validation gaps that require specialist review;
- upgrade any document from draft to product standard.

---

## 6. Mode A directory layout

The recommended repository layout is:

```text
ccdp-v0.1.1-hygiene-addendum/
  README.md
  CCDP_v0_1_1_ADDENDUM_INDEX.md
  DOI_SAFE_PATCH_STRATEGY.md
  CCDP_v0_1_1_Hygiene_Patch_APPLIED.md
  OBSOLETE.md
  CANONICAL_PRECEDENCE_RULE.md
  RAW_EVIDENCE_EXCEPTION_CANONICAL.md
  TERMINOLOGY_AXIS_CLARIFICATION.md
  PUBLIC_TECHNICAL_SENSITIVE_SPLIT.md
  CLEAN_START_CLARIFICATION.md
  SOFT_SAFETY_RED_BLACK_MUST_CLARIFICATION.md
  RELEASE_NOTES_v0_1_1.md
  manifest/
    ADDENDUM_MANIFEST.json
    SHA256SUMS
  codex/
    CODEX_DOI_SAFE_PATCH_RUNBOOK.md
```

If a repository cannot use this exact layout, it MUST preserve the same logical separation:

```text
baseline artifacts != addendum artifacts
```

---

## 7. Existing addendum documents

At the time this strategy is created, the following v0.1.1 addendum documents already exist or are intended to exist:

| Document | Status | Role |
|---|---|---|
| `CCDP_v0_1_1_Hygiene_Patch_APPLIED.md` | created | Applied-control map for HP-001…HP-013. |
| `OBSOLETE.md` | created | Non-canonical / obsolete draft registry and handling rule. |
| `CANONICAL_PRECEDENCE_RULE.md` | created | Package-wide precedence and interpretation rule. |
| `RAW_EVIDENCE_EXCEPTION_CANONICAL.md` | created | Canonical raw-evidence exception protocol. |
| `DOI_SAFE_PATCH_STRATEGY.md` | current | Addendum-only publication integrity rule. |
| `CCDP_v0_1_1_ADDENDUM_INDEX.md` | planned | Addendum package registry and reading order. |
| `TERMINOLOGY_AXIS_CLARIFICATION.md` | planned | Separation of C0–C5, CCDP-0…5, C-A*, M*, D*, PF*, etc. |
| `PUBLIC_TECHNICAL_SENSITIVE_SPLIT.md` | planned | Release split and distribution boundary. |
| `CLEAN_START_CLARIFICATION.md` | planned | Clean-start rule without unlawful destruction of minimal witness/legal records. |
| `SOFT_SAFETY_RED_BLACK_MUST_CLARIFICATION.md` | planned | Red / Black MUST disclosure and bypass clarification. |
| `RELEASE_NOTES_v0_1_1.md` | planned | v0.1.1 addendum release summary. |

---

## 8. Prohibited operations under Mode A

The following operations are prohibited unless the project explicitly switches to Mode B full versioned release:

1. editing DOI-bound Markdown files in place;
2. editing DOI-bound PDFs in place;
3. regenerating paired PDFs under the same version identity;
4. overwriting historical `SHA256SUMS`;
5. replacing archived release assets;
6. deleting obsolete drafts from a DOI-bound package without a versioned archival record;
7. renaming DOI-bound source files in a way that breaks citation mapping;
8. changing document status labels inside frozen files;
9. silently resolving open issues inside frozen files;
10. claiming that v0.1 source documents have been patched when only an addendum exists.

Fail-closed rule:

> If it is unclear whether a target file is DOI-bound, treat it as DOI-bound until proven otherwise.

---

## 9. Allowed operations under Mode A

The following operations are allowed:

1. create new addendum documents;
2. create a new addendum index;
3. create an addendum README;
4. create addendum release notes;
5. create an addendum SHA manifest;
6. create a machine-readable addendum manifest;
7. add new files under a clearly separated addendum directory;
8. create errata records for baseline documents;
9. create supersession notes for current interpretation;
10. create Codex runbooks for future safe patching;
11. create new PDFs for addendum documents only;
12. prepare a future Mode B plan without executing it.

Allowed operations MUST NOT mutate the baseline package.

---

## 10. Interpretation rule

### 10.1 Historical reading

For historical citation, CCDP v0.1 means the original DOI-bound / release-bound artifact exactly as published.

Historical citation SHOULD use:

```text
CCDP v0.1 baseline artifact, DOI / release identifier, access date if needed.
```

### 10.2 Current operational reading

For current use after Mode A addendum publication, CCDP SHOULD be read as:

```text
CCDP v0.1 baseline
+ CCDP v0.1.1 hygiene addendum
```

### 10.3 Conflict between baseline and addendum

If a baseline v0.1 statement conflicts with a v0.1.1 addendum clarification, then for current operational interpretation:

```text
v0.1.1 addendum controls interpretation
without altering the historical v0.1 artifact
```

This is a supersession relation, not an in-place edit.

### 10.4 Safety floor

No addendum clarification may weaken:

- child physical safety;
- lawful jurisdictional obligations;
- parent corpus mechanisms;
- minimal disclosure;
- state-not-content discipline;
- raw child life minimization;
- witness integrity;
- adult migration autonomy.

If an addendum appears to weaken any of these, the addendum MUST be held for review.

---

## 11. Patch materiality classes

| Class | Name | Meaning | Mode A handling |
|---|---|---|---|
| `DSP-M0` | Typo / formatting | Does not affect meaning. | Record in errata; do not mutate baseline. |
| `DSP-M1` | Navigation / discoverability | Reader may find wrong file or miss intended order. | Addendum index / obsolete registry. |
| `DSP-M2` | Terminology ambiguity | Reader may confuse classes or axes. | Terminology clarification addendum. |
| `DSP-M3` | Normative ambiguity | Requirement may be misread. | Canonical clarification addendum. |
| `DSP-M4` | Safety interpretation hazard | Misread may create unsafe implementation. | Urgent addendum; conformance warning. |
| `DSP-M5` | Architecture contradiction | Baseline mechanism may require redesign. | Stop Mode A; plan Mode B / major version. |

No `DSP-M5` issue is currently asserted by this document.

---

## 12. Codex-safe patch workflow

### 12.1 Preflight

Before any Codex patch run, Codex MUST create or inspect a target list:

```text
target_files[]
operation_type
known_doi_bound?
paired_pdf?
sha_manifested?
release_asset?
```

If any target is DOI-bound or unknown, Codex MUST NOT edit it in place.

### 12.2 Decision tree

```text
Is target DOI-bound / release-bound / PDF-paired / SHA-manifested?
  yes -> no in-place edit
         create addendum record or switch to Mode B
  no  -> may edit only if repository owner confirms non-bound status

Is requested change a correction to baseline meaning?
  yes -> addendum / erratum / supersession
  no  -> create new non-baseline file if useful

Does requested change require source replacement?
  yes -> Mode B required
  no  -> Mode A allowed
```

### 12.3 Required Codex output

Every Mode A Codex patch run MUST produce:

```text
CODEX_PATCH_REPORT.md
```

with:

- files created;
- files intentionally not edited;
- DOI-bound files detected;
- addendum references created;
- unresolved manual actions;
- validation result;
- fail-closed stops if any.

### 12.4 Git diff rule

Under Mode A, the final Git diff MUST NOT show modifications to baseline DOI-bound source or PDF files.

Expected diff shape:

```text
A ccdp-v0.1.1-hygiene-addendum/...
```

Unexpected diff shape:

```text
M CCDP_v0_1_R_Corpus_Aligned.md
M Soft_Safety_State_Signaling_Profile_v0_1.md
M CCDP_Witness_Event_Schema_v0_1.md
M *.pdf
M SHA256SUMS  # historical manifest
```

If unexpected baseline modifications appear, Codex MUST stop and revert them.

---

## 13. Obsolete draft handling under Mode A

Mode A does not physically delete or rewrite obsolete DOI-bound artifacts.

Instead:

1. `OBSOLETE.md` records obsolete / non-canonical documents;
2. the addendum index points readers away from obsolete drafts;
3. future Mode B may move obsolete drafts into `archive/obsolete/`;
4. if physical movement is performed later, the move must be versioned and recorded.

Required obsolete registry rule:

```text
A document may be obsolete for current use while still preserved for historical traceability.
```

Prohibited:

```text
delete obsolete draft to make the package look cleaner
```

Allowed:

```text
mark obsolete in addendum
preserve historical trace
route readers to canonical document
```

---

## 14. Clean start handling under Mode A

If baseline documents ambiguously describe `clean start`, Mode A handles this through `CLEAN_START_CLARIFICATION.md`.

The clarification MUST state:

```text
clean start = active adult continuity clean start
not unlawful destruction of minimal witness, lawful, protection, or legal-hold records
```

The baseline text remains unchanged.

Current users MUST read clean start through the v0.1.1 addendum.

---

## 15. Raw-evidence exception handling under Mode A

If baseline profiles duplicate or slightly vary raw-evidence exception language, Mode A handles this through `RAW_EVIDENCE_EXCEPTION_CANONICAL.md`.

Current interpretation:

```text
all raw-evidence exception language routes to the canonical addendum document
```

Baseline duplicated wording is not edited in Mode A.

Future Mode B MAY replace duplicated wording with cross-references.

---

## 16. Precedence handling under Mode A

If baseline modules contain inconsistent precedence wording, Mode A handles this through `CANONICAL_PRECEDENCE_RULE.md`.

Current interpretation:

```text
package-wide precedence is controlled by the v0.1.1 addendum rule
```

Baseline files are not modified.

Future Mode B MAY insert the short cross-reference block into all relevant modules.

---

## 17. Terminology handling under Mode A

If baseline documents overload similar class names, Mode A handles this through `TERMINOLOGY_AXIS_CLARIFICATION.md`.

Minimum namespaces to distinguish:

```text
C0-C5        child maturity levels
CCDP-0..5    conformance classes
C-A*         assertion classes
M0-M12       memory classes
D0-D4        dependency levels
PF-*         personality formation classes
DSP-M*       DOI patch materiality classes
```

No baseline terminology is rewritten in Mode A.

---

## 18. Public / technical / sensitive split under Mode A

If baseline package distribution boundaries are unclear, Mode A handles this through `PUBLIC_TECHNICAL_SENSITIVE_SPLIT.md`.

The split MUST classify each document as one of:

```text
public
technical
restricted
internal
sensitive review artifact
obsolete / historical
```

Mode A does not remove sensitive files from historical packages.

It defines current distribution guidance.

---

## 19. Citation guidance

### 19.1 Historical citation

Use when discussing the original frozen release:

```text
CCDP v0.1 baseline, DOI: <DOI_FOR_CCDP_v0_1>, frozen as of <date>.
```

### 19.2 Current interpretation citation

Use when discussing current corrected package reading:

```text
CCDP v0.1 baseline + CCDP v0.1.1 Hygiene Addendum, Mode A addendum-only strategy.
```

### 19.3 Errata citation

Use when citing a specific known correction:

```text
See CCDP v0.1.1 Hygiene Addendum, <document>, <section>, which clarifies / supersedes the v0.1 baseline wording for current use.
```

### 19.4 Prohibited citation form

Do not cite an edited baseline file as if it were the original DOI artifact.

Prohibited:

```text
CCDP v0.1, DOI: <same DOI>, patched silently in repository.
```

---

## 20. Machine-readable manifest draft

A future `ADDENDUM_MANIFEST.json` SHOULD encode:

```json
{
  "package": "CCDP",
  "baseline_version": "v0.1",
  "addendum_version": "v0.1.1",
  "patch_mode": "MODE_A_ADDENDUM_ONLY",
  "baseline_mutation_allowed": false,
  "doi_bound_assumption": true,
  "documents": [
    {
      "file": "DOI_SAFE_PATCH_STRATEGY.md",
      "role": "doi-safe patch strategy",
      "status": "created",
      "controls": ["publication_integrity", "codex_patch_routing"]
    },
    {
      "file": "CCDP_v0_1_1_Hygiene_Patch_APPLIED.md",
      "role": "applied hygiene control map",
      "status": "created",
      "controls": ["HP-001", "HP-002", "HP-003", "HP-004", "HP-005", "HP-006", "HP-007", "HP-008", "HP-009", "HP-010", "HP-011", "HP-012", "HP-013"]
    },
    {
      "file": "OBSOLETE.md",
      "role": "obsolete draft registry",
      "status": "created",
      "controls": ["OI-001", "CR-001", "HP-001"]
    },
    {
      "file": "CANONICAL_PRECEDENCE_RULE.md",
      "role": "package-wide precedence rule",
      "status": "created",
      "controls": ["OI-004", "HP-004"]
    },
    {
      "file": "RAW_EVIDENCE_EXCEPTION_CANONICAL.md",
      "role": "canonical raw-evidence exception protocol",
      "status": "created",
      "controls": ["OI-005", "HP-007"]
    }
  ],
  "prohibited_operations": [
    "edit_baseline_in_place",
    "regenerate_baseline_pdf_under_same_identity",
    "overwrite_historical_sha256sums",
    "delete_obsolete_baseline_without_versioned_record"
  ]
}
```

---

## 21. Acceptance checklist

Mode A addendum pack is acceptable only if:

```text
[ ] Baseline DOI-bound files are not edited.
[ ] Baseline PDFs are not edited or regenerated.
[ ] Historical SHA manifests are not overwritten.
[ ] Addendum documents are stored separately.
[ ] Addendum index exists.
[ ] Addendum release notes exist.
[ ] Addendum SHA256SUMS exists.
[ ] Obsolete draft registry exists.
[ ] Canonical precedence rule exists.
[ ] Canonical raw-evidence exception protocol exists.
[ ] Clean-start clarification exists.
[ ] Terminology axis clarification exists.
[ ] Public / technical / sensitive split exists.
[ ] Red / Black MUST clarification exists.
[ ] Codex runbook exists before automated repository patching.
[ ] No addendum claims that v0.1 source files were patched in place.
```

---

## 22. Anti-washing rule

A system, vendor, school, reviewer, or implementer MUST NOT claim:

```text
CCDP v0.1.1 conformance
```

merely because it cites this addendum pack.

The addendum is a release-control and hygiene correction layer.

Conformance still requires:

- applicable CCDP Conformance Test Matrix evidence;
- witnessable behavior;
- no red-line failures;
- public / technical / sensitive boundary compliance;
- jurisdictional handoff where applicable;
- specialist review where stronger child-safety claims are made.

---

## 23. Non-expansion rule

This strategy does not add a new child-safety mechanism.

It only controls how existing and future CCDP hygiene corrections are published without corrupting frozen artifacts.

If a proposed addendum attempts to introduce a new mechanism, it MUST be reclassified as:

```text
new profile
future version
or Mode B / major release work
```

---

## 24. Future Mode B trigger

Mode B full versioned release becomes required if:

1. source text must be rewritten extensively;
2. duplicated exception language must be removed from baseline modules;
3. schemas must be embedded into the canonical source package;
4. paired PDFs must be regenerated;
5. new SHA manifest must cover all source and PDF artifacts;
6. a new DOI / release version is desired;
7. existing v0.1 documents need to be superseded as current canonical sources rather than interpreted through addendum.

Mode B MUST NOT be started accidentally by Codex.

Mode B requires explicit human authorization.

---

## 25. Codex carry-forward actions

For future Codex work:

```text
TODO-CODEX-001: Create ccdp-v0.1.1-hygiene-addendum/ directory.
TODO-CODEX-002: Move created addendum docs into that directory.
TODO-CODEX-003: Create CCDP_v0_1_1_ADDENDUM_INDEX.md.
TODO-CODEX-004: Create README.md for addendum pack.
TODO-CODEX-005: Create RELEASE_NOTES_v0_1_1.md.
TODO-CODEX-006: Create ADDENDUM_MANIFEST.json.
TODO-CODEX-007: Generate SHA256SUMS for addendum files only.
TODO-CODEX-008: Do not edit DOI-bound baseline files.
TODO-CODEX-009: Do not move obsolete baseline files unless Mode B or versioned archival action is explicitly selected.
TODO-CODEX-010: If obsolete draft handling is required under Mode A, record it in OBSOLETE.md and addendum index only.
TODO-CODEX-011: Produce CODEX_PATCH_REPORT.md after any repository operation.
```

---

## 26. Final rule

Mode A is conservative by design.

It prefers a slightly heavier addendum trail over a clean-looking but corrupted publication history.

Final compact rule:

```text
Do not rewrite the witness.
Write the correction next to it.
Make the reader follow the correction.
Keep the old object stable.
```
