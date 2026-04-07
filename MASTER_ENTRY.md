# AGI (Advanced Global Intelligence) / SER / L4 — Master Entry (Canonical Reading Path)

**Important naming note:** in this stack, **AGI = Advanced Global Intelligence** (repo: `Kot141078/advanced-global-intelligence`) — **not** “Artificial General Intelligence”.

This page is the single entry point for the public protocol stack:

**AGI (context) → SER (normative spec) → L4 (reality-bound operations)**

## Root entry shortcuts

- Human root entry: `START_HERE.md`
- Machine root entry: `MACHINE_ENTRY.md`
- Topology map: `official/PROTOCOL_TOPOLOGY_ONEPAGE_EN.md`
- DEA package entry: `protocols/dea/README.md`
- EA-L4 / EATP package entry: `protocols/ea-l4-eatp/README.md`
- Economic Layer package entry: `docs/economic-layer/README.md`
- Pre-Lineage boundary note: `manifesto/Pre_Lineage_Boundary_Note_v0.1.md`
- Canonical interpretive note: `official/C_AS_TEMPORAL_ENTITIES_OF_AI_PRESENCE.md`

## Ecosystem-level theoretical synthesis

Before entering narrower protocol layers, see:

- `manifesto/Theoretical_Foundations_of_the_AGI_Ecosystem_EN.md`
- `manifesto/Theoretical_Foundations_of_the_AGI_Ecosystem_EN.pdf`

Role:
- ecosystem-wide theoretical synthesis
- public theoretical framework
- high-level framing across AGI / SER / L4 / DEA / EA-L4 / implementation reference

---

Citation:
- Version DOI: [10.5281/zenodo.19384668](https://doi.org/10.5281/zenodo.19384668)
- All versions DOI: [10.5281/zenodo.19384667](https://doi.org/10.5281/zenodo.19384667)

---

## Process premise

> “The future is not an event. It is a process.”
> — Ivan Kotov

Canonical note: `official/AUTHORIAL_PREMISES.md`

---

## 0) Choose your track (start here)

### Track A — Audit / compliance / governance (fast, “show me evidence”)

1) **SER normative specification (start here)**
   - Repo: `Kot141078/sovereign-entity-recursion`
   - Start: `README.md` → `DOC_MAP.md` → `pdf/` → `hashes/` → `protocol/`

2) **L4 operational materials (how it behaves in reality)**
   - Repo: `Kot141078/ester-reality-bound`
   - Start: `protocol/` → `hashes/` → `docs/` (glossary/constraints) → `posts/` (optional)

3) **AGI = Advanced Global Intelligence (system context & cross-repo integrity)**
   - Repo: `Kot141078/advanced-global-intelligence`
   - Start: `INDEX.md` → `protocols/` → `architecture/` → `hashes/`

4) **DEA — input-to-experience normative layer**
   - Repo: `Kot141078/advanced-global-intelligence`
   - Start: `protocols/dea/README.md`
   - Boundary: adjacent package, upstream from EA-L4 / EATP, not `SER v2`

5) **EA-L4 / EATP — training-origin and consequence-preserving layer**
   - Repo: `Kot141078/advanced-global-intelligence`
   - Start: `protocols/ea-l4-eatp/README.md`
   - Boundary: adjacent package, not `SER v2`

### Track B — Technical reader (deep)

1) `advanced-global-intelligence/INDEX.md` (canonical map)
2) `advanced-global-intelligence/protocols/` (stack layers, scope)
   - includes `protocols/beacon/` for Beacon Profile v0.1 (inter-entity recognition)
   - includes `protocols/dea/` for DEA (input-to-experience normative layer)
   - includes `protocols/ea-l4-eatp/` for EA-L4 / EATP (training provenance / consequence-preserving layer)
3) `sovereign-entity-recursion/protocol/` + `pdf/` (SER normative core)
4) `ester-reality-bound/protocol/` + `docs/` + `posts/` (L4 operationalization)

---

## 1) Repositories and roles (one sentence each)

- **AGI (Advanced Global Intelligence) = `advanced-global-intelligence`** — architectural context + protocol stack + cross-repo integrity manifests.
- **SER = `sovereign-entity-recursion`** — **SER normative specification** (protocol, PDFs, hashing).
- **L4 = `ester-reality-bound`** — public-facing L4 materials (notes, protocol, posts) with repo hygiene (SECURITY / CONTRIBUTING / CITATION).
- **Implementation reference (non-normative):** `Kot141078/ester-clean-code`.

---

## 1.25) Entity / agent hierarchy (critical)

- By default, `c` orchestrates agents; agents do not define `c`.
- Agents are subordinate processes and tools invoked under `c`.
- Continuity belongs to `c`, not to any single model, judge, worker, or swarm.
- Canonical note: `advanced-global-intelligence/architecture/ENTITY_GOVERNS_AGENTS.md`

## 1.35) ARQ bridge (additive; canonical in SER)

- ARQ (additive subsystem; canonical in SER):
  - entry: `..\sovereign-entity-recursion\protocol\arq\README.md`
  - role: bounded error valuation, witness-backed promotion, experience filtering
  - bridge: correction logic -> SER continuity -> L4 bounded accountability
- Hidden bridges:
  - promoted deviations require witness-backed auditability
  - adaptive handling remains bounded homeostasis rather than infinite retry
- Grounding:
  - finite power, finite cooling, finite storage endurance, finite privilege, and finite controller trust apply

## 1.37) ARL v0.1 (canonical in SER)

ARL v0.1 adds a bounded arbitration / review layer for multi-entity disputes; its canonical home is in `sovereign-entity-recursion`.

## 1.40) DEA (canonical in AGI)

- DEA:
  - entry: `protocols/dea/README.md`
  - role: input-to-experience normative layer
  - current normative draft: `protocols/dea/normative/DEA_v1_0.md`
  - conformance addendum: `protocols/dea/normative/DEA_Normative_Addendum_v1_1.md`
  - downstream layer: `protocols/ea-l4-eatp/README.md`
- Boundary:
  - canonical home is AGI
  - upstream from EA-L4 / EATP
  - adjacent to SER and L4
  - not part of SER normative core
  - not `SER v2`
- Explicit bridge:
  - `Input -> DEA -> EA / EATP -> Witness / Evidence`
- Hidden bridges:
  - input does not become experience until persistence and consequence are present
  - provenance remains separable from later training abstraction
- Grounding:
  - if a document changes nothing persistent and nothing downstream, the system stored data but did not acquire experience

## 1.45) EA-L4 / EATP (canonical in AGI)

- EA-L4 / EATP:
  - entry: `protocols/ea-l4-eatp/README.md`
  - role: downstream training provenance / experience artifact layer
  - current normative draft: `protocols/ea-l4-eatp/normative/EATP_EA_L4_v1_2.md`
  - executive bridge: `protocols/ea-l4-eatp/executive/EATP_EA_L4_v1_2_EL.md`
  - use case: `protocols/ea-l4-eatp/use-cases/Use_Case_Hospital.md`
  - commercial docs: `protocols/ea-l4-eatp/commercial/`
- Boundary:
  - canonical home is AGI
  - adjacent to SER and L4
  - not part of SER normative core
  - not `SER v2`
- Explicit bridge:
  - `c = a + b + L4 + Witness + ARQ -> EA-L4 / EATP as training-origin and consequence-preserving layer`
- Hidden bridges:
  - provenance + consequence + quarantine + selection increase anti-collapse control variety
  - hashes + structured artifacts compress trust bandwidth without turning origin into narrative fog
- Grounding:
  - if a system claims to have learned from an event, there should be an attributable trail for origin, consequence, and retention

## 1.46) Economic Layer (canonical in AGI)

- Economic Layer:
  - entry: `docs/economic-layer/README.md`
  - index: `docs/economic-layer/INDEX.md`
  - Zenodo DOI: https://doi.org/10.5281/zenodo.19408654
  - normative core: `docs/economic-layer/Economic_Layer_for_Experience_Artifacts_v0.1.md`
  - role: admissibility / provenance / transfer / restraint / anti-gaming / non-market handling for Experience Artifacts
  - extension clauses: `docs/economic-layer/extensions/`
  - pdf surfaces: `docs/economic-layer/pdf/` and `docs/economic-layer/pdf/extensions/`
- Boundary:
  - canonical home is AGI
  - package helper / publication-carpentry docs are intentionally excluded from the public GitHub package surface
  - the layer does not convert all EA value into market value

## 1.47) Pre-Lineage Boundary Note (reserved territory)

- Pre-Lineage Boundary Note:
  - entry: `manifesto/Pre_Lineage_Boundary_Note_v0.1.md`
  - pdf: `manifesto/Pre_Lineage_Boundary_Note_v0.1.pdf`
  - Zenodo DOI: https://doi.org/10.5281/zenodo.19409346
  - role: reserved cross-stack boundary note for lineage, inheritance, reproduction, daughter-entity emergence, and post-anchor continuity
- Boundary:
  - not yet a mature normative layer
  - not a completed lineage constitution
  - included here as a conservative manifesto-level boundary note

---

## 1.5) Machine-friendly access (no UI)

If you are a tool/LLM or a reviewer working without GitHub UI/JS, use these:

### Canonical map (human + machine)

- Raw Master Entry:
  https://raw.githubusercontent.com/Kot141078/advanced-global-intelligence/main/MASTER_ENTRY.md
- Repo index (human):
  https://raw.githubusercontent.com/Kot141078/advanced-global-intelligence/main/REPO_INDEX.md
- Repo index (machine):
  https://raw.githubusercontent.com/Kot141078/advanced-global-intelligence/main/REPO_INDEX.json
- LLM-friendly pointer (llms.txt):
  https://raw.githubusercontent.com/Kot141078/advanced-global-intelligence/main/llms.txt

Meaning Map (1 page, EN): https://raw.githubusercontent.com/Kot141078/advanced-global-intelligence/main/official/MEANING_MAP_ONEPAGE_EN.md

Docs snapshot tag: machine-entry-2026-02-26

### Stable downloads (tag snapshots — cite these)

- AGI (agi-snapshot-2026-02-24)
  - ZIP: https://github.com/Kot141078/advanced-global-intelligence/archive/refs/tags/agi-snapshot-2026-02-24.zip
  - TAR: https://github.com/Kot141078/advanced-global-intelligence/archive/refs/tags/agi-snapshot-2026-02-24.tar.gz

- SER (ecosystem-v0.2-2026-02-24)
  - ZIP: https://github.com/Kot141078/sovereign-entity-recursion/archive/refs/tags/ecosystem-v0.2-2026-02-24.zip
  - TAR: https://github.com/Kot141078/sovereign-entity-recursion/archive/refs/tags/ecosystem-v0.2-2026-02-24.tar.gz

- L4 (l4-snapshot-2026-02-24)
  - ZIP: https://github.com/Kot141078/ester-reality-bound/archive/refs/tags/l4-snapshot-2026-02-24.zip
  - TAR: https://github.com/Kot141078/ester-reality-bound/archive/refs/tags/l4-snapshot-2026-02-24.tar.gz

- Clean (v0.2.3)
  - ZIP: https://github.com/Kot141078/ester-clean-code/archive/refs/tags/v0.2.3.zip
  - TAR: https://github.com/Kot141078/ester-clean-code/archive/refs/tags/v0.2.3.tar.gz

### Latest downloads (main branch — “give me current state”)

- AGI main ZIP:   https://github.com/Kot141078/advanced-global-intelligence/archive/refs/heads/main.zip
- SER main ZIP:   https://github.com/Kot141078/sovereign-entity-recursion/archive/refs/heads/main.zip
- L4  main ZIP:   https://github.com/Kot141078/ester-reality-bound/archive/refs/heads/main.zip
- Clean main ZIP: https://github.com/Kot141078/ester-clean-code/archive/refs/heads/main.zip

### Verification rule (do this, not archive hashes)

- Do not trust GitHub-generated archive checksums.
- Verify **content** using each repo’s `hashes/` directory and `SHA256SUMS_*.txt`.

---

## 2) Integrity / paper trail (how to verify)

- Each repo contains a `hashes/` directory with SHA-256 manifests or hashing instructions.
- Rule: normative artifacts change only with explicit version bump + updated integrity manifests.
- Minimal verification mindset:
  - “I do not trust text.” → verify **hashes**, **PDFs**, **commit/release references**, and **change logs**.

---

## 2.5) Minimal Evidence Pack (operational, copy/paste friendly)

If you need to reproduce the “Ivan-style” perimeter quickly (home / lab / small org):

- Repo: `Kot141078/ester-reality-bound`
- Path: `evidence/`
  - `room_checklist.md`
  - `power_chain_diagram.md` (optional printable PDF in `evidence/pdf/`)
  - `perimeter_snapshot.example.json`
  - `perimeter_change.example.json`
  - `README.md`

Purpose: a reviewer can verify a node/room perimeter without inventing formats.

Verification: SHA-256 hashes are recorded in repo manifests (see `hashes/` or top-level `SHA256SUMS`).

---

## 3) Versioning rule (to prevent confusion)

- **SER sets the normative version.**
- AGI and L4 repositories reference SER versions as compatible layers, without redefining the core.

---

## 4) Administrative submissions (practical note)

For official review, prefer **PDF artifacts + SHA-256 manifests** (release assets or `pdf/` + `hashes/`), and keep email bodies minimal (“Details in attached PDF”).

Official: see `/official/` (pitch sheet + print-ready PDFs + hashes).

Latest ecosystem snapshot (SER): `ecosystem-v0.2-2026-02-24` (GitHub Release).

---

## Bridges (required)

**Explicit bridge:** `c = a + b`

- `a` = accountable human anchor (authorship / responsibility)
- `b` = procedures + protocols + PDFs + integrity manifests
- `c` = a checkable, citeable public corpus

**Hidden bridge #1 (Ashby):**
Variety is achieved via separate repos (spec/context/operations), but stability requires a single regulator: **this Master Entry**.

**Hidden bridge #2 (Cover & Thomas):**
SHA-256 manifests compress “trust bandwidth”: verification is transmitted as short, checkable strings instead of narrative.

**Earth paragraph (engineering):**
This structure mirrors aviation-grade documentation: *system overview* (AGI), *normative spec* (SER), *operational bulletins* (L4) — different documents, one truth source, reproducible checksums.

## Additional cross-repo entry — L4 Glitch / Research Quarantine Stack v0.1

Normative home:
- [ester-reality-bound / docs/glitch-stack](https://github.com/Kot141078/ester-reality-bound/tree/main/docs/glitch-stack)

Implementation home:
- [ester-clean-code / docs/architecture/glitch-stack](https://github.com/Kot141078/ester-clean-code/tree/main/docs/architecture/glitch-stack)

First implementation milestone:
- [Milestone M1 in ester-clean-code](https://github.com/Kot141078/ester-clean-code/tree/main/docs/architecture/glitch-stack/milestone-m1/md)

This cross-repo note is intentionally minimal.
The full documents remain in their natural homes and are not duplicated here.

## Published glitch-stack release set

Canonical GitHub homes:
- `ester-reality-bound` -> `docs/glitch-stack/`
- `ester-clean-code` -> `docs/architecture/glitch-stack/`

Zenodo records:
- Core Specification v0.1 — version DOI: [10.5281/zenodo.19385784](https://doi.org/10.5281/zenodo.19385784), all versions: [10.5281/zenodo.19385783](https://doi.org/10.5281/zenodo.19385783)
- Graph Grammar and Visibility Layer v0.1 — version DOI: [10.5281/zenodo.19385908](https://doi.org/10.5281/zenodo.19385908), all versions: [10.5281/zenodo.19385907](https://doi.org/10.5281/zenodo.19385907)
- Implementation Bridge to ester-clean-code v0.1 — version DOI: [10.5281/zenodo.19386014](https://doi.org/10.5281/zenodo.19386014), all versions: [10.5281/zenodo.19386013](https://doi.org/10.5281/zenodo.19386013)
- Milestone M1 Specification v0.1 — version DOI: [10.5281/zenodo.19386143](https://doi.org/10.5281/zenodo.19386143), all versions: [10.5281/zenodo.19386142](https://doi.org/10.5281/zenodo.19386142)
