# SEOI Patch Notes v0.1.1

## Append-first correction record for `10_Self_Evo_Open_Issues_v0_1.md`

**Status:** patch notes / package-control artifact  
**Date:** 2026-06-25  
**Patch ID:** `SEOI_PATCH_NOTES_v0_1_1`  
**Reviewed artifact:** `10_Self_Evo_Open_Issues_v0_1.md`  
**Corrected artifact:** `10_Self_Evo_Open_Issues_v0_1_1.md`  
**Review record:** `SEOI_REVIEW_RECORD_v0_1.md`  
**Review result:** `PASS_WITH_LIMITS`  
**Patch type:** append-first correction / no deletion of review history

---

## 0. Hashes

```text
reviewed v0.1 SHA-256:
ec0752599562fcede77bf2924e42ea8d933bc28f7c2806a3f264e2a34c21f483

corrected v0.1.1 SHA-256:
25777ee1029aec7d0d9ac9af02d0d06b703021709566fbfc27f6b013142903e4

corrected v0.1.1 line count:
857
```

---

## 1. Review summary

`SEOI_REVIEW_RECORD_v0_1.md` reviewed `10_Self_Evo_Open_Issues_v0_1.md` and returned `PASS_WITH_LIMITS`.

The review found no red line, no authority leakage, and verified that the conversion from `SELF-EVO-09` §9 was lossless, including preservation of `WATCH` statuses.

The review raised two minor findings:

| Finding | Class | Summary | Status in v0.1.1 |
|---|---|---|---|
| `SEOI-REV-F1` | minor | Object-model `issue_id` required `SE-OI-YYYY-NNN`, but actual backlog IDs use `SE-OI-NNN`, domain-prefixed IDs, and `SE-OI-SELF-NNN`. | closed |
| `SEOI-REV-F2` | nit | `C_SELF_EVO_BACKLOG_SUMMARY` showed all-zero counts without being labeled as a template. | closed |

---

## 2. Changes made

### 2.1 `SEOI-REV-F1` closed

Added a new section:

```text
§4.6 Issue ID scheme
```

The corrected rule is:

```text
The canonical open-issue ID scheme does not use a year component.
Time belongs in created_at, review records, patch notes, and witness / manifest metadata.
```

Allowed issue ID families are now explicitly defined:

```text
SE-OI-NNN
SE-SCHEMA-NNN
SE-CHECKER-NNN
SE-FIX-NNN
SE-PKG-NNN
SE-TRIAD-NNN
SE-SRLM-NNN
SE-MEM-NNN
SE-RES-NNN
SE-PUB-NNN
SE-UX-NNN
SE-REV-NNN
SE-OI-SELF-NNN
```

Updated §19.1:

```yaml
issue_id: "SE-OI-NNN | SE-<DOMAIN>-NNN | SE-OI-SELF-NNN"
```

and added:

```text
issue_id MUST follow the v0.1.1 ID scheme in §4.6.
The unused SE-OI-YYYY-NNN form from v0.1 is intentionally not valid.
```

### 2.2 `SEOI-REV-F2` closed

Updated §19.2 to label `C_SELF_EVO_BACKLOG_SUMMARY` as a schema template / example object.

The zero counts are now explicitly placeholders, not the current backlog summary:

```text
This block is a schema template / example object, not the current numeric backlog summary for v0.1.1.
The zero values below are placeholders showing shape only.
A real backlog summary MUST be generated from the actual issue table during final package manifest creation.
```

### 2.3 Self-tracking register updated

Updated §24:

```text
SE-OI-SELF-001 -> PATCHED
```

Added:

```text
SE-OI-SELF-004 — SEOI-REV-F1 patched
SE-OI-SELF-005 — SEOI-REV-F2 patched
```

### 2.4 Header and scope updated

Updated document title and status:

```text
Self-Evo Open Issues v0.1.1
Draft package-control backlog v0.1.1 / append-first corrected revision
```

Updated `SELF-EVO-10` scope row to point to:

```text
10_Self_Evo_Open_Issues_v0_1_1.md
```

---

## 3. Claims

Allowed current claim:

```text
10_Self_Evo_Open_Issues_v0_1_1.md is a patched append-first revision addressing SEOI-REV-F1/F2.
```

Forbidden claims:

```text
This patch does not make the package implemented.
This patch does not make the package conformance-supported.
This patch does not make the package public-release-ready.
This patch does not authorize live self-evo.
This patch does not replace final manifest / package index / release notes.
```

---

## 4. Recommended next step

Request repeat review of:

```text
10_Self_Evo_Open_Issues_v0_1_1.md
```

If confirmed, proceed to the package-control layer:

```text
SELF_EVO_PACKAGE_INDEX_AND_READING_ORDER_v0_1.md
SELF_EVO_PACKAGE_MANIFEST_v0_1.json
SELF_EVO_RELEASE_NOTES_v0_1.md
```

---

## 5. Closing

```text
Backlog fixed.
Authority not granted.
Next: package index and reading order.
```
