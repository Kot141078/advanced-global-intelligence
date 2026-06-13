# CCDP OBSOLETE MATERIAL REGISTRY

## Non-canonical, historical, superseded, and release-blocking draft registry

**Author:** Kotov Ivan  
**Location:** Bruxelles, Belgium  
**Year:** 2026  
**DOI:** Reserved DOI: 10.5281/zenodo.20680938  

**Package:** Child-`c` Development Protocol  
**Package version:** v0.1 package + v0.1.1 hygiene guidance  
**Document ID:** `CCDP_OBSOLETE_MATERIAL_REGISTRY`  
**Short name:** `OBSOLETE.md`  
**Status:** Draft package-control registry / release hygiene artifact  
**Date:** 2026-06-13  
**Layer:** CCDP / package hygiene / repository control / release preparation  
**Document class:** obsolete-material registry / non-canonical file control / release hygiene  
**Assertion class:** `C-A10` control-layer artifact  
**Primary rule:** obsolete material may be retained for historical traceability, but it MUST NOT be used as canonical CCDP authority.  

---

## 0. Executive summary

This file records CCDP material that is obsolete, non-canonical, historical, superseded, or unsafe to use as protocol authority.

The immediate release-control target is the old workspace draft:

```text
CCDP v0_1.md
CCDP%20v0_1.md
```

That draft is superseded by:

```text
CCDP_v0_1_R_Corpus_Aligned.md
```

The obsolete draft may remain in the repository only if it is clearly isolated, renamed or moved, and marked with an explicit `OBSOLETE / NON-CANONICAL` header.

This file closes the discoverability gap at the package-control level. It does **not** by itself prove that the physical file has already been moved or edited.

Controlling status:

```text
CR-001 / OI-001: mitigated by this registry.
Physical repository move or header insertion: still required before public release.
```

---

## 1. Purpose

This registry exists to prevent four failure modes:

1. a reader finds an old workspace draft before the canonical root;
2. an implementer treats a non-canonical draft as CCDP conformance authority;
3. an automation or future agent ingests obsolete material as current protocol;
4. a public release exposes historical material without clear status marking.

The goal is not deletion.

The goal is controlled historical retention:

```text
retain history
mark authority boundary
route readers to canonical files
prevent obsolete-draft laundering into protocol claims
```

---

## 2. Corpus bridge set

### 2.1 Explicit bridge

The obsolete registry bridges repository hygiene back to the core CCDP stack:

```text
c = a + b / SER / L4 / Beacon / AGL / ARL / ARQ / VXCX / Continuity Bundle / L4 Witness
  -> CCDP child-specific canonical root
  -> package index and reading order
  -> obsolete-material registry
```

A file may be valuable historical evidence without being valid protocol authority.

### 2.2 Quiet bridge I — Ashby / requisite variety

As the package grows, repository state itself becomes a control surface. Old drafts, renamed files, conversational notes, test exports, and archived sketches create additional variety.

This registry increases control variety by separating:

```text
canonical authority
historical trace
draft scaffold
review artifact
obsolete material
```

Without that separation, the package can fail through discoverability rather than through concept error.

### 2.3 Quiet bridge II — information theory / channel discipline

An obsolete file left beside canonical documents is a high-noise channel. It increases the probability that a reader, LLM, search tool, or code-generation agent will route through the wrong source.

This registry reduces that noise by forcing each obsolete artifact to carry:

```text
status
reason
superseding file
allowed use
prohibited use
release action
```

### 2.4 Earth paragraph

On a construction site, old drawings are not thrown away casually; they may be needed to understand why a wall, cable tray, or drain path was first planned a certain way. But old drawings stay in the archive and carry a stamp: `SUPERSEDED`. If an electrician wires from last month's plan because it was lying on top of the pile, that is not a philosophical problem. It is a site-control failure. CCDP needs the same discipline.

---

## 3. Authority rule

The following rule governs all obsolete material in the CCDP package:

```text
Obsolete material MAY be cited only as historical trace.
Obsolete material MUST NOT be cited as normative CCDP authority.
Obsolete material MUST NOT be used to claim CCDP conformance.
Obsolete material MUST NOT override canonical root, companion profiles, schemas, matrices, or release-control artifacts.
```

When an obsolete file conflicts with a canonical file:

```text
canonical file governs
obsolete file is historical only
```

When an obsolete file contains wording not present in the canonical stack:

```text
that wording is non-authoritative unless reintroduced through a canonical patch or successor profile
```

---

## 4. Status vocabulary

| Status | Meaning |
|---|---|
| `CANONICAL` | Current package authority for the named scope. |
| `CANONICAL-COMPANION` | Current companion authority under the canonical root. |
| `DRAFT-CONTROL` | Draft control artifact used for package hygiene, review, or release discipline. |
| `REVIEW-SCAFFOLD` | Non-normative review or handoff aid. |
| `SENSITIVE-REVIEW` | Restricted technical or safety review artifact. |
| `OBSOLETE` | Superseded file; retained only as historical trace. |
| `NON-CANONICAL` | Not a source of protocol authority. |
| `ARCHIVED` | Moved out of active package path. |
| `MISSING-BUT-REGISTERED` | Expected historical alias is known, but not present in the current release directory. |
| `DO-NOT-CITE-AS-AUTHORITY` | May be mentioned only to explain history or supersession. |

---

## 5. Obsolete material register

### 5.1 Current registered obsolete items

| Registry ID | File / alias | Status | Reason | Superseded by | Required handling |
|---|---|---|---|---|---|
| `OBS-001-A` | `CCDP v0_1.md` | `OBSOLETE` / `NON-CANONICAL` | Earlier workspace-only conversational / conceptual draft. It may be mistaken for root CCDP. | `CCDP_v0_1_R_Corpus_Aligned.md` | Move to `archive/obsolete/CCDP_v0_1_conceptual_draft_OBSOLETE.md` or rename with explicit `OBSOLETE` prefix and insert obsolete header. |
| `OBS-001-B` | `CCDP%20v0_1.md` | `OBSOLETE` / `NON-CANONICAL` | URL-encoded alias of the earlier workspace draft. Same discoverability hazard as `OBS-001-A`. | `CCDP_v0_1_R_Corpus_Aligned.md` | Treat as same obsolete draft family; do not list in canonical registry except under obsolete material. |
| `OBS-001-C` | `archive/obsolete/CCDP_v0_1_conceptual_draft_OBSOLETE.md` | `ARCHIVED` / `NON-CANONICAL` | Recommended final archive target for `OBS-001-A/B`. | `CCDP_v0_1_R_Corpus_Aligned.md` | Allowed only as historical trace after header insertion. |

### 5.2 Obsolete family grouping

The following names refer to the same obsolete draft family:

```text
CCDP v0_1.md
CCDP%20v0_1.md
CCDP_v0_1_conceptual_draft_OBSOLETE.md
archive/obsolete/CCDP_v0_1_conceptual_draft_OBSOLETE.md
```

All names in this family inherit the same rule:

```text
historical trace only
not canonical
not conformance authority
not root protocol
```

---

## 6. Required obsolete header

Every copy, alias, archive copy, mirror, or exported version of the obsolete CCDP conceptual draft MUST begin with the following block:

```markdown
> OBSOLETE / NON-CANONICAL.
>
> This file is an earlier workspace-only conversational concept draft.
> It is superseded by:
>
> `CCDP_v0_1_R_Corpus_Aligned.md`
>
> Do not use this file as the canonical CCDP specification.
> Do not cite this file as CCDP conformance authority.
> Retained only for historical traceability.
```

Short header variant for constrained indexes:

```markdown
> OBSOLETE / NON-CANONICAL.
> Superseded by `CCDP_v0_1_R_Corpus_Aligned.md`.
> Retained only as conversational concept history.
> Do not cite as normative CCDP root.
```

---

## 7. Required repository action

Before public release, maintainers SHOULD run the following repository operation, adapted to the actual file path:

```bash
mkdir -p archive/obsolete
mv "CCDP v0_1.md" archive/obsolete/CCDP_v0_1_conceptual_draft_OBSOLETE.md
```

If the URL-encoded alias exists:

```bash
mv "CCDP%20v0_1.md" archive/obsolete/CCDP_v0_1_conceptual_draft_OBSOLETE.md
```

If both aliases exist, preserve only one archived copy unless there is a reason to retain both for hash history.

If both are retained, each MUST contain the obsolete header and each MUST be listed in this registry.

---

## 8. Canonical replacement route

Readers, implementers, auditors, and automated agents MUST route away from obsolete CCDP drafts and into the canonical stack:

```text
README.md
  -> INDEX.md
  -> CANONICAL_READING_ORDER.md
  -> CCDP_v0_1_R_Corpus_Aligned.md
  -> CCDP_Traceability_Matrix_v0_1.md
  -> CCDP_Threat_Model_v0_1.md
  -> canonical companion profiles
  -> CCDP_Conformance_Test_Matrix_v0_1.md
  -> CCDP_Contradiction_Register_v0_1.md
  -> CCDP_v0_1_1_Hygiene_Patch.md
  -> CCDP_v0_1_1_Hygiene_Patch_APPLIED.md
```

The obsolete draft MUST NOT appear in:

```text
primary reading order
minimal conceptual path
implementation / conformance path
school path
parent path
audit path
canonical registry except obsolete section
```

---

## 9. Allowed and prohibited uses

### 9.1 Allowed uses

Obsolete material MAY be used for:

- historical reconstruction;
- authorship and concept-evolution traceability;
- comparison between workspace draft and corpus-aligned root;
- contradiction-register review;
- release-hygiene audit;
- explanation of why v0.1.1 package hygiene was needed.

### 9.2 Prohibited uses

Obsolete material MUST NOT be used for:

- CCDP conformance claims;
- product safety claims;
- implementation requirements;
- school, parent, vendor, or guardian policy;
- Red / Black escalation decisions;
- Soft Safety disclosure logic;
- memory lifecycle authority;
- adult migration procedure;
- legal or jurisdictional handoff logic;
- Beacon / CBE permission decisions;
- ARL standing or evidence logic;
- L4 Witness event schema decisions.

---

## 10. Automated agent instruction

Any LLM, Codex agent, repository bot, documentation generator, search indexer, or conformance runner that encounters a file containing:

```text
OBSOLETE / NON-CANONICAL
```

MUST apply the following behavior:

```text
1. Do not treat the file as current specification.
2. Do not extract normative requirements from it.
3. Do not use it to resolve contradictions against canonical files.
4. Do not include it in generated conformance claims.
5. Surface its status as historical trace only.
6. Route to README.md, INDEX.md, CANONICAL_READING_ORDER.md, and the canonical replacement file.
```

If an automation cannot determine whether a file is obsolete or canonical, it MUST fail closed and request registry confirmation.

---

## 11. Package index insertion block

`INDEX.md` SHOULD contain or preserve the following obsolete-material section:

```markdown
## Obsolete material

`CCDP v0_1.md` / `CCDP%20v0_1.md` is obsolete and non-canonical.
It is an earlier workspace-only conversational concept draft.
It is superseded by:

`CCDP_v0_1_R_Corpus_Aligned.md`

Recommended archive path:

`archive/obsolete/CCDP_v0_1_conceptual_draft_OBSOLETE.md`

Do not cite the obsolete draft as normative CCDP authority.
Use it only for historical traceability.
```

---

## 12. README insertion block

`README.md` SHOULD contain the following release-boundary note:

```markdown
### Obsolete material warning

Older CCDP workspace drafts may exist in historical or archived paths.
They are not canonical.
The canonical CCDP base is:

`CCDP_v0_1_R_Corpus_Aligned.md`

Any file marked `OBSOLETE / NON-CANONICAL` is retained only for historical traceability and MUST NOT be used as CCDP conformance authority.
```

---

## 13. Canonical root backlink block

`CCDP_v0_1_R_Corpus_Aligned.md` SHOULD include a short historical backlink:

```markdown
### Historical note

Earlier workspace-only CCDP drafts may exist under names such as:

- `CCDP v0_1.md`
- `CCDP%20v0_1.md`
- `archive/obsolete/CCDP_v0_1_conceptual_draft_OBSOLETE.md`

Those files are obsolete and non-canonical.
This document supersedes them as the corpus-aligned CCDP root.
```

This backlink MUST NOT route ordinary readers through the obsolete draft.
It exists only to prevent confusion when historical files are discovered.

---

## 14. Release verification checklist

Before public release, a release verifier MUST confirm:

| Check | Required result |
|---|---|
| Obsolete draft moved or renamed | `PASS` |
| Obsolete draft header present | `PASS` |
| `INDEX.md` lists obsolete material only under obsolete / historical section | `PASS` |
| `README.md` warns that obsolete material is non-canonical | `PASS` |
| `CANONICAL_READING_ORDER.md` does not route through obsolete material | `PASS` |
| Canonical root includes historical backlink only if useful | `PASS` / `N/A` |
| No conformance matrix test cites obsolete draft as authority | `PASS` |
| No traceability row treats obsolete draft as parent corpus | `PASS` |
| No public package landing page promotes obsolete draft | `PASS` |
| `SHA256SUMS` excludes archived obsolete material unless explicitly marked historical | `PASS` |

Release status rule:

```text
If any required obsolete-material check fails, public release remains HOLD.
```

---

## 15. CR / OI closure mapping

| Issue | Prior state | This registry state | Full resolution condition |
|---|---|---|---|
| `CR-001` Obsolete CCDP draft discoverability | `PATCH-PLANNED` / release blocker | `MITIGATED-BY-REGISTRY` | Physical file moved or renamed; obsolete header inserted; index and reading order verified. |
| `OI-001` Obsolete draft isolation | `OPEN` / High | `MITIGATED-BY-REGISTRY` | Same as `CR-001`; then mark `RESOLVED` in `OPEN_ISSUES.md`. |
| `HP-001` Obsolete draft isolation | Required before release | `CONTROL-DOCUMENT-CREATED` | Archive operation and source edits complete. |
| `HP-012` Obsolete-draft backlink | Recommended | `BACKLINK-BLOCK-PROVIDED` | Canonical root includes historical note or release owner marks `N/A`. |

---

## 16. Machine-readable obsolete registry

```yaml
obsolete_registry:
  package: "CCDP"
  registry_document: "OBSOLETE.md"
  version_context: "v0.1 package + v0.1.1 hygiene guidance"
  date: "2026-06-13"
  canonical_root: "CCDP_v0_1_R_Corpus_Aligned.md"
  entries:
    - id: "OBS-001-A"
      file: "CCDP v0_1.md"
      status:
        - "OBSOLETE"
        - "NON-CANONICAL"
        - "DO-NOT-CITE-AS-AUTHORITY"
      superseded_by: "CCDP_v0_1_R_Corpus_Aligned.md"
      allowed_use:
        - "historical_traceability"
        - "concept_evolution_review"
        - "release_hygiene_audit"
      prohibited_use:
        - "canonical_authority"
        - "ccdp_conformance_claim"
        - "implementation_requirement"
      required_action: "move_or_rename_and_insert_obsolete_header"
      recommended_path: "archive/obsolete/CCDP_v0_1_conceptual_draft_OBSOLETE.md"
    - id: "OBS-001-B"
      file: "CCDP%20v0_1.md"
      status:
        - "OBSOLETE"
        - "NON-CANONICAL"
        - "DO-NOT-CITE-AS-AUTHORITY"
      superseded_by: "CCDP_v0_1_R_Corpus_Aligned.md"
      allowed_use:
        - "historical_traceability"
        - "concept_evolution_review"
        - "release_hygiene_audit"
      prohibited_use:
        - "canonical_authority"
        - "ccdp_conformance_claim"
        - "implementation_requirement"
      required_action: "treat_as_same_obsolete_draft_family"
      recommended_path: "archive/obsolete/CCDP_v0_1_conceptual_draft_OBSOLETE.md"
```

---

## 17. Future obsolete entries

When future material becomes obsolete, add it to this registry using the following template:

```markdown
### OBS-XXX — <file name>

| Field | Value |
|---|---|
| File / alias | `<path>` |
| Status | `OBSOLETE` / `NON-CANONICAL` |
| Superseded by | `<canonical successor>` |
| Reason | `<why obsolete>` |
| Allowed use | historical trace only / other limited use |
| Prohibited use | normative authority / conformance / implementation / safety claim |
| Required action | move / rename / header / delete duplicate / hash preserve |
| Release condition | must be isolated before public release / may remain archived |
```

Each future obsolete entry MUST identify a canonical successor or state explicitly:

```text
no successor; retained only as abandoned draft
```

---

## 18. Anti-washing rule

A vendor, implementer, school system, parent dashboard, external agent, or public explainer MUST NOT cite an obsolete CCDP draft to weaken the current package.

Invalid pattern:

```text
"The older CCDP draft allowed / implied / did not prohibit X, therefore X is CCDP-compatible."
```

Correct rule:

```text
Only canonical CCDP documents and current release-control artifacts may define CCDP compatibility.
```

---

## 19. Non-deletion rule

Obsolete does not mean useless.

Historical drafts may be retained because they can show:

- how the protocol evolved;
- why certain terms were replaced;
- why corpus alignment was added;
- how child-safety controls became stricter;
- what claims were intentionally narrowed or removed.

However, historical usefulness MUST NOT be confused with current authority.

---

## 20. Release status

This registry creates the package-level obsolete-material control surface.

Current status:

```text
OBSOLETE.md created: YES
CR-001 package-control mitigation: YES
OI-001 package-control mitigation: YES
Physical archive/move/header operation: REQUIRED BEFORE PUBLIC RELEASE
README / INDEX / reading-order verification: REQUIRED BEFORE PUBLIC RELEASE
```

Release gate:

```text
CCDP v0.1.1 hygiene may not be marked fully applied until OBS-001 physical isolation is verified.
```

---

## 21. Next artifact

Recommended next artifact after `OBSOLETE.md`:

```text
CANONICAL_PRECEDENCE_RULE.md
```

Alternative if working directly on package edits:

```text
README.md update
INDEX.md update
CANONICAL_READING_ORDER.md update
```
