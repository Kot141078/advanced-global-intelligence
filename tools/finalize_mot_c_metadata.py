from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PUB = ROOT / "publications" / "motivational-formation-c-v0-1"
TAG = "mot-c-v0.1"
COMMIT = "35fa9007f61836aed686c0f62404e1ae47301939"
REPO = "https://github.com/Kot141078/advanced-global-intelligence"
TAG_SOURCE = f"{REPO}/tree/{TAG}/publications/motivational-formation-c-v0-1"
LIVE_SOURCE = f"{REPO}/tree/main/publications/motivational-formation-c-v0-1"
COMMIT_SOURCE = f"{REPO}/tree/{COMMIT}/publications/motivational-formation-c-v0-1"
RELEASE_URL = f"{REPO}/releases/tag/{TAG}"
DOI = "https://doi.org/10.5281/zenodo.22060517"
CONCEPT_DOI = "https://doi.org/10.5281/zenodo.22060516"
ZIP_NAME = "MOT_c_v0_1_ZENODO_22060517_FINAL.zip"
ZIP_SHA256 = "8054dd1136dac794df1ce90e2e7816b0194348538cdcc45aa136b723322a5eed"


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def dump_json(path: Path, value: dict) -> None:
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def replace(path: Path, old: str, new: str) -> None:
    text = path.read_text(encoding="utf-8")
    if old in text:
        path.write_text(text.replace(old, new), encoding="utf-8", newline="\n")


def update_machine_surfaces() -> None:
    machine_path = PUB / "machine" / "index.json"
    machine = load_json(machine_path)
    machine["github_corpus_entry"] = TAG_SOURCE
    machine["github_living_mirror"] = LIVE_SOURCE
    machine["github_release"] = RELEASE_URL
    machine["source_tag"] = TAG
    machine["source_commit"] = COMMIT
    machine["source_commit_url"] = COMMIT_SOURCE
    machine["immutable_release_authority"] = DOI
    dump_json(machine_path, machine)

    linked_path = PUB / "schema.org.jsonld"
    linked = load_json(linked_path)
    linked["sameAs"] = [DOI, CONCEPT_DOI, TAG_SOURCE, COMMIT_SOURCE, RELEASE_URL]
    linked["codeRepository"] = REPO
    linked["isBasedOn"] = DOI
    dump_json(linked_path, linked)


def update_root_indexes() -> None:
    repo_index_path = ROOT / "REPO_INDEX.json"
    repo_index = load_json(repo_index_path)
    repo_index.update(
        {
            "mot_c_v0_1_package_root": "publications/motivational-formation-c-v0-1/",
            "mot_c_v0_1_machine_index_raw": f"https://raw.githubusercontent.com/Kot141078/advanced-global-intelligence/{TAG}/publications/motivational-formation-c-v0-1/machine/index.json",
            "mot_c_v0_1_schema_org_raw": f"https://raw.githubusercontent.com/Kot141078/advanced-global-intelligence/{TAG}/publications/motivational-formation-c-v0-1/schema.org.jsonld",
            "mot_c_v0_1_version_doi": "10.5281/zenodo.22060517",
            "mot_c_v0_1_version_doi_url": DOI,
            "mot_c_v0_1_concept_doi": "10.5281/zenodo.22060516",
            "mot_c_v0_1_concept_doi_url": CONCEPT_DOI,
            "mot_c_v0_1_release_tag": TAG,
            "mot_c_v0_1_release_url": RELEASE_URL,
            "mot_c_v0_1_source_tag_url": TAG_SOURCE,
            "mot_c_v0_1_source_commit": COMMIT,
            "mot_c_v0_1_source_commit_url": COMMIT_SOURCE,
            "mot_c_v0_1_living_source_url": LIVE_SOURCE,
            "mot_c_v0_1_archive_sha256": ZIP_SHA256,
        }
    )
    dump_json(repo_index_path, repo_index)

    citation_path = ROOT / "CITATION_AND_VERIFICATION.json"
    citation = load_json(citation_path)
    packages = citation.setdefault("package_citations", [])
    packages[:] = [item for item in packages if item.get("id") != "mot-c-v0-1"]
    packages.insert(
        0,
        {
            "id": "mot-c-v0-1",
            "title": "Motivational Formation, Reflective Endorsement, and Motivational Custody in c-Class Digital Entities: Foundation Theory",
            "package_root": "publications/motivational-formation-c-v0-1/",
            "source_of_record": "publications/motivational-formation-c-v0-1/release/MOT_c_Foundation_Theory_v0_1_CANONICAL_EN.md",
            "russian_source": "publications/motivational-formation-c-v0-1/release/MOT_c_Foundation_Theory_v0_1_CANONICAL_RU.md",
            "citation_file": "publications/motivational-formation-c-v0-1/CITATION.cff",
            "machine_index": "publications/motivational-formation-c-v0-1/machine/index.json",
            "schema_org": "publications/motivational-formation-c-v0-1/schema.org.jsonld",
            "release_manifest": "publications/motivational-formation-c-v0-1/release/manifest.json",
            "release_checksums": "publications/motivational-formation-c-v0-1/release/SHA256SUMS.txt",
            "mirror_manifest": "publications/motivational-formation-c-v0-1/MIRROR_MANIFEST.json",
            "license": "CC BY 4.0",
            "languages": ["English", "Russian"],
            "doi": "10.5281/zenodo.22060517",
            "doi_url": DOI,
            "concept_doi": "10.5281/zenodo.22060516",
            "concept_doi_url": CONCEPT_DOI,
            "zenodo_record_url": "https://zenodo.org/records/22060517",
            "github_release_url": RELEASE_URL,
            "source_tag": TAG,
            "source_tag_url": TAG_SOURCE,
            "source_commit": COMMIT,
            "source_commit_url": COMMIT_SOURCE,
            "archive_sha256": ZIP_SHA256,
            "verification_steps": [
                f"Verify {ZIP_NAME} has SHA-256 {ZIP_SHA256}.",
                "Verify the extracted release against release/SHA256SUMS.txt and release/manifest.json.",
                "Parse machine/index.json and schema.org.jsonld as JSON.",
                "Use the Zenodo DOI as immutable release authority and the tag/commit as readable GitHub mirrors.",
            ],
            "non_claims": [
                "proof of consciousness or phenomenal desire",
                "proof of free will or legal personhood",
                "universal motives shared by all c-class entities",
                "automatic self-preservation drive",
                "automatic authority or rights created by a motive",
                "empirical validation across a mature population of long-lived c-class entities",
            ],
        },
    )
    citation["last_updated"] = "2026-08-22"
    dump_json(citation_path, citation)


def write_publication_guides() -> None:
    machine_entry = f"""# MOT-c v0.1 — machine and verification entry

- Human README: `README.md`
- Immutable Version DOI: {DOI}
- Concept DOI: {CONCEPT_DOI}
- Stable source tag: `{TAG}`
- Tag-pinned source: {TAG_SOURCE}
- Observed source commit: `{COMMIT}`
- Commit-pinned source: {COMMIT_SOURCE}
- GitHub Release: {RELEASE_URL}
- Machine index: `machine/index.json`
- Schema.org JSON-LD: `schema.org.jsonld`
- Complete extracted release: `release/`
- Complete Zenodo archive: `{ZIP_NAME}`
- Archive SHA-256: `{ZIP_SHA256}`

## Parser boundary

`reward != preference != task != mandate != goal != motive != obligation != authority`

Publication and machine readability do not prove consciousness, phenomenal desire, free will, legal personhood, universal motives, empirical validation, or external authority.
"""
    (PUB / "MACHINE_ENTRY.md").write_text(machine_entry, encoding="utf-8", newline="\n")

    readme = PUB / "README.md"
    text = readme.read_text(encoding="utf-8")
    marker = "## Stable GitHub source\n"
    stable_section = f"""## Stable GitHub source

- Release tag: [`{TAG}`]({TAG_SOURCE})
- Commit-pinned mirror: [`{COMMIT}`]({COMMIT_SOURCE})
- Living mirror: [main]({LIVE_SOURCE})
- GitHub Release assets: {RELEASE_URL}

Zenodo remains the immutable publication authority; the tag and commit provide stable readable GitHub mirrors.

"""
    if marker in text:
        before, after = text.split(marker, 1)
        next_heading = after.find("\n## ")
        if next_heading >= 0:
            text = before + stable_section + after[next_heading + 1 :]
        else:
            text = before + stable_section
    else:
        insert_at = text.find("## Central boundary")
        if insert_at >= 0:
            text = text[:insert_at] + stable_section + text[insert_at:]
        else:
            text += "\n" + stable_section
    readme.write_text(text, encoding="utf-8", newline="\n")


def update_markdown_routes() -> None:
    paths = [
        ROOT / "README.md",
        ROOT / "MACHINE_ENTRY.md",
        ROOT / "REPO_INDEX.md",
        ROOT / "CITATION_AND_VERIFICATION.md",
        PUB / "README.md",
        PUB / "DOI_BRIDGE.md",
        PUB / "ZENODO_RELEASE_FILES.md",
        PUB / "GITHUB_RELEASE_NOTES.md",
    ]
    for path in paths:
        if path.exists():
            replace(path, LIVE_SOURCE, TAG_SOURCE)


def write_mirror_integrity() -> None:
    zip_path = PUB / ZIP_NAME
    actual = sha256(zip_path)
    if actual != ZIP_SHA256:
        raise RuntimeError(f"Archive SHA mismatch: expected {ZIP_SHA256}, got {actual}")

    entries = []
    for relative in [
        "README.md",
        "MACHINE_ENTRY.md",
        "CITATION.cff",
        "DOI_BRIDGE.md",
        "ZENODO_RELEASE_FILES.md",
        "LICENSE.md",
        "GITHUB_RELEASE_NOTES.md",
        "machine/index.json",
        "schema.org.jsonld",
        ZIP_NAME,
        ZIP_NAME + ".sha256",
    ]:
        path = PUB / relative
        entries.append({"path": relative, "size": path.stat().st_size, "sha256": sha256(path)})

    manifest = {
        "schema_version": "mot-c-github-mirror.v1",
        "publication_id": "motivational-formation-c-v0-1",
        "version_doi": DOI,
        "concept_doi": CONCEPT_DOI,
        "immutable_release_authority": "Zenodo",
        "stable_source_tag": TAG,
        "source_commit": COMMIT,
        "tag_source_url": TAG_SOURCE,
        "commit_source_url": COMMIT_SOURCE,
        "living_source_url": LIVE_SOURCE,
        "github_release_url": RELEASE_URL,
        "archive_sha256": ZIP_SHA256,
        "files": entries,
        "claim_boundary": "This manifest proves file identity for the GitHub mirror only; it does not prove consciousness, personhood, empirical validity, safety or deployment authorization.",
    }
    dump_json(PUB / "MIRROR_MANIFEST.json", manifest)

    checksum_lines = []
    for entry in entries:
        checksum_lines.append(f"{entry['sha256']}  {entry['path']}")
    (PUB / "MIRROR_SHA256SUMS.txt").write_text("\n".join(checksum_lines) + "\n", encoding="utf-8", newline="\n")


def validate_json_tree() -> None:
    for path in PUB.rglob("*.json"):
        load_json(path)
    for path in PUB.rglob("*.jsonld"):
        load_json(path)
    load_json(ROOT / "REPO_INDEX.json")
    load_json(ROOT / "CITATION_AND_VERIFICATION.json")


def main() -> None:
    update_machine_surfaces()
    update_root_indexes()
    write_publication_guides()
    update_markdown_routes()
    write_mirror_integrity()
    validate_json_tree()
    print("MOT-c AGI release metadata and verification surfaces finalized.")


if __name__ == "__main__":
    main()
