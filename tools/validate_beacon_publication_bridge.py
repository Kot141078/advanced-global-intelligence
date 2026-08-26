#!/usr/bin/env python3
"""Validate the Beacon v0.1 DOI-safe publication bridge."""

from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path, PurePosixPath
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
PUBLICATION_DIR = ROOT / "protocols" / "beacon" / "publication"
PUBLICATION_RECORD = PUBLICATION_DIR / "PUBLICATION_RECORD.json"
CITATION_CFF = PUBLICATION_DIR / "CITATION.cff"
HISTORICAL_MANIFEST = ROOT / "hashes" / "SHA256SUMS_beacon_v0.1_2026-03-10.txt"
PUBLICATION_MANIFEST = PUBLICATION_DIR / "SHA256SUMS_PUBLICATION_BRIDGE.txt"

OFFICIAL_CFF_SCHEMA_URL = (
    "https://raw.githubusercontent.com/citation-file-format/citation-file-format/1.2.0/schema.json"
)
OFFICIAL_CFF_SCHEMA_SHA256 = "0b8d22140da702d766df318dcff3a91af2f39521298dcf36d76315fd99cc169b"
OFFICIAL_SCHEMA_VALIDATED_CFF_SHA256 = "66fa7ab787eef421aa77b2ad94e0e4d7d490a72f488b073a34c0e2ccd7833ebf"

PUBLISHED_DOI = "10.5281/zenodo.18933553"
GUESSED_CONCEPT_DOI = "10.5281/zenodo.18933552"
HISTORICAL_COMMIT = "15695853223c798379538aad69dc573730e1ee96"
IMPLEMENTATION_COMMIT = "54cd0c8754587f5e9daf82b16eb84c66a7ac94ef"
IMPLEMENTATION_MODULE = "modules/beacon_profile/profile.py"
IMPLEMENTATION_TESTS = "tests/test_beacon_profile.py"
IMPLEMENTATION_STATUS = "Structural reference classifier and persistence sidecar."
IMPLEMENTATION_STATUS_MACHINE = "structural_reference_classifier_and_persistence_sidecar"
STATUS_CEILING = (
    "Published DOI-linked informative synthesis profile containing normative-style local requirements. "
    "It is not a standards-track specification, not a certification regime, and not a completed "
    "cryptographic conformance package."
)

PROTECTED_HASHES = {
    "protocols/beacon/Beacon_Profile_v0.1_EN.md":
        "4e5061fc655ce384dcbf75843ff158a10c5e1f39e3c2bdf60e2a85ffed494de1",
    "protocols/beacon/Beacon_Profile_v0.1_EN.pdf":
        "d646934ea8657785741af57e422d9e044a0de407f2f9d5a6089f083a37b6eeb0",
    "protocols/beacon/README.md":
        "9bf3b577e38519b7d25eb7051667e7c7db89b302c2f7ef5a80179593ed99dd26",
}
HISTORICAL_MANIFEST_SHA256 = "2cbbff8a1948866f05e00faf675b2a818b62b3af21b9ad27ca74935f07a2a3bd"

ROUTING_SURFACES = (
    "README.md",
    "INDEX.md",
    "MASTER_ENTRY.md",
    "REPO_INDEX.md",
    "REPO_INDEX.json",
    "MACHINE_ENTRY.md",
    "llms.txt",
)
PUBLICATION_FILES = (
    "CITATION.cff",
    "PUBLICATION_RECORD.json",
    "README.md",
    "SHA256SUMS_PUBLICATION_BRIDGE.txt",
)
PUBLICATION_PAYLOADS = (
    "README.md",
    "PUBLICATION_RECORD.json",
    "CITATION.cff",
)

CHECKSUM_LINE = re.compile(r"^([0-9a-f]{64})  ([^\r\n]+)$")


class DuplicateKeyError(ValueError):
    """Raised when a JSON object repeats a key."""


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def normalized(text: str) -> str:
    return " ".join(text.split())


def duplicate_safe_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise DuplicateKeyError(f"duplicate JSON key {key!r}")
        result[key] = value
    return result


def reject_nonfinite(value: str) -> None:
    raise ValueError(f"non-finite JSON number {value!r}")


def load_json(path: Path, errors: list[str]) -> Any | None:
    try:
        raw = path.read_bytes()
        if raw.startswith(b"\xef\xbb\xbf"):
            raise ValueError("UTF-8 BOM is not permitted")
        return json.loads(
            raw.decode("utf-8"),
            object_pairs_hook=duplicate_safe_object,
            parse_constant=reject_nonfinite,
        )
    except (OSError, UnicodeDecodeError, json.JSONDecodeError, ValueError) as exc:
        errors.append(f"{path.relative_to(ROOT).as_posix()}: invalid JSON: {exc}")
        return None


def read_utf8(path: Path, errors: list[str]) -> str:
    try:
        raw = path.read_bytes()
        if raw.startswith(b"\xef\xbb\xbf"):
            errors.append(f"{path.relative_to(ROOT).as_posix()}: UTF-8 BOM is not permitted")
        return raw.decode("utf-8")
    except (OSError, UnicodeDecodeError) as exc:
        errors.append(f"{path.relative_to(ROOT).as_posix()}: cannot read UTF-8 text: {exc}")
        return ""


def parse_checksum_manifest(
    manifest: Path,
    base: Path,
    expected_paths: tuple[str, ...],
    errors: list[str],
) -> list[tuple[str, str]]:
    label = manifest.relative_to(ROOT).as_posix()
    try:
        raw = manifest.read_bytes()
    except OSError as exc:
        errors.append(f"{label}: cannot read checksum manifest: {exc}")
        return []

    if not raw.endswith(b"\n"):
        errors.append(f"{label}: checksum manifest must end with LF")
    if b"\r" in raw:
        errors.append(f"{label}: checksum manifest must use LF line endings")
    try:
        lines = raw.decode("ascii").splitlines()
    except UnicodeDecodeError as exc:
        errors.append(f"{label}: checksum manifest is not ASCII: {exc}")
        return []

    entries: list[tuple[str, str]] = []
    seen: set[str] = set()
    for line_number, line in enumerate(lines, start=1):
        match = CHECKSUM_LINE.fullmatch(line)
        if match is None:
            errors.append(f"{label}:{line_number}: expected lowercase SHA-256, two spaces, and path")
            continue
        expected_hash, relative = match.groups()
        pure = PurePosixPath(relative)
        if pure.is_absolute() or ".." in pure.parts or "\\" in relative or not pure.parts:
            errors.append(f"{label}:{line_number}: unsafe or non-POSIX path {relative!r}")
            continue
        if relative in seen:
            errors.append(f"{label}:{line_number}: duplicate path {relative!r}")
            continue
        seen.add(relative)
        entries.append((relative, expected_hash))

        target = base.joinpath(*pure.parts)
        if not target.is_file() or target.is_symlink():
            errors.append(f"{label}:{line_number}: missing regular file {relative!r}")
            continue
        actual_hash = sha256(target)
        if actual_hash != expected_hash:
            errors.append(
                f"{label}:{line_number}: SHA-256 mismatch for {relative!r}; "
                f"expected {expected_hash}, got {actual_hash}"
            )

    actual_paths = tuple(path for path, _ in entries)
    if actual_paths != expected_paths:
        errors.append(f"{label}: paths/order mismatch; expected {expected_paths!r}, got {actual_paths!r}")
    return entries


def validate_protected_files(errors: list[str]) -> None:
    for relative, expected_hash in PROTECTED_HASHES.items():
        path = ROOT.joinpath(*PurePosixPath(relative).parts)
        if not path.is_file() or path.is_symlink():
            errors.append(f"{relative}: protected artifact is missing or not a regular file")
            continue
        actual_hash = sha256(path)
        if actual_hash != expected_hash:
            errors.append(f"{relative}: protected SHA-256 expected {expected_hash}, got {actual_hash}")

    if not HISTORICAL_MANIFEST.is_file() or HISTORICAL_MANIFEST.is_symlink():
        errors.append("hashes/SHA256SUMS_beacon_v0.1_2026-03-10.txt: protected manifest is missing")
    else:
        actual_hash = sha256(HISTORICAL_MANIFEST)
        if actual_hash != HISTORICAL_MANIFEST_SHA256:
            errors.append(
                "hashes/SHA256SUMS_beacon_v0.1_2026-03-10.txt: protected manifest SHA-256 "
                f"expected {HISTORICAL_MANIFEST_SHA256}, got {actual_hash}"
            )

    entries = parse_checksum_manifest(
        HISTORICAL_MANIFEST,
        ROOT,
        tuple(PROTECTED_HASHES),
        errors,
    )
    if entries and dict(entries) != PROTECTED_HASHES:
        errors.append("historical Beacon manifest entries do not equal the protected hash set")


def validate_publication_inventory(errors: list[str]) -> None:
    if not PUBLICATION_DIR.is_dir() or PUBLICATION_DIR.is_symlink():
        errors.append("protocols/beacon/publication/: missing regular directory")
        return
    actual = tuple(sorted(path.name for path in PUBLICATION_DIR.iterdir()))
    if actual != PUBLICATION_FILES:
        errors.append(f"protocols/beacon/publication/: expected exactly {PUBLICATION_FILES!r}, got {actual!r}")
    for child in PUBLICATION_DIR.iterdir():
        if not child.is_file() or child.is_symlink():
            errors.append(f"protocols/beacon/publication/{child.name}: must be a regular file")


def validate_publication_record(errors: list[str]) -> None:
    record = load_json(PUBLICATION_RECORD, errors)
    if not isinstance(record, dict):
        if record is not None:
            errors.append("protocols/beacon/publication/PUBLICATION_RECORD.json: root must be an object")
        return

    expected_scalars = {
        "schema": "beacon_profile_publication_bridge.v0.1",
        "record_status": "doi_backfill_publication_facade",
        "title": "Beacon Profile v0.1 — Inter-Entity Recognition for Sovereign Digital Entities",
        "short_title": "Beacon Profile v0.1",
        "version": "v0.1",
        "document_date": "2026-03-09",
        "published_doi": PUBLISHED_DOI,
        "doi_url": f"https://doi.org/{PUBLISHED_DOI}",
        "doi_role": "unresolved",
        "version_doi": None,
        "concept_doi": None,
        "zenodo_record_url": "https://zenodo.org/records/18933553",
        "zenodo_metadata_verified": False,
        "zenodo_file_inventory_verified": False,
        "zenodo_byte_identity_verified": False,
        "doi_role_resolution_note": (
            "The exact DOI is confirmed, but version/concept relation metadata has not yet been ingested. "
            "No neighboring DOI is inferred."
        ),
        "status": "published_doi_linked_informative_synthesis_profile_with_normative_style_local_requirements",
        "historical_integrity_manifest": "hashes/SHA256SUMS_beacon_v0.1_2026-03-10.txt",
    }
    for key, expected in expected_scalars.items():
        if key not in record or record[key] != expected or (expected is False and record[key] is not False):
            errors.append(f"PUBLICATION_RECORD.json: {key} must be {expected!r}")

    expected_author = {
        "name": "Ivan Kotov",
        "orcid": "https://orcid.org/0009-0009-6002-9845",
        "location": "Bruxelles, Belgium",
    }
    if record.get("author") != expected_author:
        errors.append("PUBLICATION_RECORD.json: author object mismatch")

    expected_repository = {
        "repository": "Kot141078/advanced-global-intelligence",
        "historical_source_commit": HISTORICAL_COMMIT,
        "root": "protocols/beacon/",
        "publication_bridge": "protocols/beacon/publication/",
    }
    if record.get("canonical_repository") != expected_repository:
        errors.append("PUBLICATION_RECORD.json: canonical_repository object mismatch")

    expected_artifacts = [
        {"role": "canonical_markdown_mirror", "path": path, "sha256": digest}
        if path.endswith(".md") and not path.endswith("README.md")
        else {"role": "publication_pdf_mirror", "path": path, "sha256": digest}
        if path.endswith(".pdf")
        else {"role": "historical_package_readme", "path": path, "sha256": digest}
        for path, digest in PROTECTED_HASHES.items()
    ]
    if record.get("historical_artifacts") != expected_artifacts:
        errors.append("PUBLICATION_RECORD.json: historical_artifacts mismatch")

    expected_demonstrates = [
        "bundle data structures",
        "Slot A and Slot B classification flow",
        "fail-closed downgrade",
        "class-to-privilege mapping",
        "bundle and decision persistence",
        "raw-memory disclosure rejected by default",
    ]
    expected_denials = [
        "payload-hash recomputation",
        "cryptographic signature verification",
        "Ed25519 verification",
        "key resolution",
        "key rotation proof",
        "key revocation proof",
        "witness-reference resolution",
        "challenge execution",
        "independent interoperability",
        "production deployment conformance",
    ]
    bridge = record.get("implementation_bridge")
    if not isinstance(bridge, dict):
        errors.append("PUBLICATION_RECORD.json: implementation_bridge must be an object")
    else:
        expected_bridge = {
            "repository": "Kot141078/ester-clean-code",
            "commit": IMPLEMENTATION_COMMIT,
            "module": IMPLEMENTATION_MODULE,
            "tests": IMPLEMENTATION_TESTS,
            "status": IMPLEMENTATION_STATUS_MACHINE,
            "demonstrates": expected_demonstrates,
            "does_not_demonstrate": expected_denials,
        }
        if bridge != expected_bridge:
            errors.append("PUBLICATION_RECORD.json: implementation_bridge mismatch")

    expected_protocol_boundary = {
        "beacon": "recognition semantics",
        "vxcx": "bounded visual-experience capsule structure and transfer",
        "l4_witness": "challengeable evidence and consequence-bearing resolution",
        "authority": "separate receiver-local policy decision",
    }
    if record.get("protocol_boundary") != expected_protocol_boundary:
        errors.append("PUBLICATION_RECORD.json: protocol_boundary mismatch")


def validate_citation_cff(errors: list[str]) -> None:
    expected = """cff-version: 1.2.0
message: \"Please cite the Beacon Profile v0.1 report using the metadata in preferred-citation.\"
title: \"Beacon Profile v0.1 — DOI-safe Publication Bridge Metadata\"
type: dataset
version: \"v0.1-bridge\"
authors:
  - family-names: \"Kotov\"
    given-names: \"Ivan\"
    orcid: \"https://orcid.org/0009-0009-6002-9845\"
repository-code: \"https://github.com/Kot141078/advanced-global-intelligence\"
url: \"https://github.com/Kot141078/advanced-global-intelligence/tree/main/protocols/beacon/publication\"
abstract: \"Structured metadata and discovery bridge for the published Beacon Profile v0.1 report. The dataset type applies only to this metadata package; the report itself is represented in preferred-citation.\"
preferred-citation:
  type: report
  title: \"Beacon Profile v0.1 — Inter-Entity Recognition for Sovereign Digital Entities\"
  authors:
    - family-names: \"Kotov\"
      given-names: \"Ivan\"
      orcid: \"https://orcid.org/0009-0009-6002-9845\"
  version: \"v0.1\"
  year: 2026
  doi: \"10.5281/zenodo.18933553\"
  url: \"https://doi.org/10.5281/zenodo.18933553\"
"""
    actual = read_utf8(CITATION_CFF, errors)
    if actual != expected:
        errors.append("protocols/beacon/publication/CITATION.cff: bounded CFF 1.2.0 structure mismatch")

    # Offline CI accepts only the exact payload independently validated against
    # the official tagged CFF 1.2.0 schema identified above. Any CFF edit must
    # be revalidated against that schema and update this digest deliberately.
    if CITATION_CFF.is_file() and sha256(CITATION_CFF) != OFFICIAL_SCHEMA_VALIDATED_CFF_SHA256:
        errors.append(
            "CITATION.cff: SHA-256 does not match the payload validated against "
            f"official CFF schema {OFFICIAL_CFF_SCHEMA_URL} "
            f"(schema SHA-256 {OFFICIAL_CFF_SCHEMA_SHA256})"
        )

    lines = actual.splitlines()
    top_level = [line for line in lines if line and not line.startswith(" ")]
    if "type: dataset" not in top_level:
        errors.append("CITATION.cff: top-level type must be dataset for the metadata package")
    if 'title: "Beacon Profile v0.1 — DOI-safe Publication Bridge Metadata"' not in top_level:
        errors.append("CITATION.cff: top-level title must identify the publication bridge metadata package")
    if any(line.startswith("doi:") for line in top_level):
        errors.append("CITATION.cff: top-level DOI must be absent")
    if "preferred-citation:" not in top_level:
        errors.append("CITATION.cff: preferred-citation must describe the Beacon report")
        preferred_lines: list[str] = []
    else:
        preferred_lines = lines[lines.index("preferred-citation:") + 1:]
    preferred_expected = (
        "  type: report",
        '  title: "Beacon Profile v0.1 — Inter-Entity Recognition for Sovereign Digital Entities"',
        '  version: "v0.1"',
        '  doi: "10.5281/zenodo.18933553"',
    )
    for required in preferred_expected:
        if required not in preferred_lines:
            errors.append(f"CITATION.cff: preferred-citation is missing {required.strip()!r}")
    expected_abstract = (
        'abstract: "Structured metadata and discovery bridge for the published Beacon Profile v0.1 '
        "report. The dataset type applies only to this metadata package; the report itself is "
        'represented in preferred-citation."'
    )
    if expected_abstract not in top_level:
        errors.append("CITATION.cff: abstract must limit dataset classification to the metadata bridge")
    for forbidden in ("date-released:", "license:", "related-identifiers:", GUESSED_CONCEPT_DOI):
        if forbidden in actual:
            errors.append(f"CITATION.cff: forbidden or unverified value {forbidden!r}")


def validate_publication_readme(errors: list[str]) -> None:
    path = PUBLICATION_DIR / "README.md"
    text = read_utf8(path, errors)
    compact = normalized(text)
    for heading in (
        "# Beacon Profile v0.1 — Publication Bridge",
        "## Purpose",
        "## Published identifier",
        "## Historical source artifacts",
        "## Status",
        "## Public implementation evidence",
        "## Protocol boundary",
        "## Bridge discipline",
        "## Citation",
        "## Non-claims",
    ):
        if heading not in text:
            errors.append(f"publication README: missing heading {heading!r}")
    if STATUS_CEILING not in compact:
        errors.append("publication README: exact status ceiling is missing")
    if IMPLEMENTATION_STATUS not in text:
        errors.append("publication README: exact implementation status is missing")

    required_fragments = (
        PUBLISHED_DOI,
        "DOI role: unresolved pending authoritative relation metadata",
        "Concept DOI: unresolved; not guessed",
        "The Zenodo file inventory has not yet been ingested into this repository.",
        "Exact Zenodo ↔ GitHub byte identity is not claimed by this bridge.",
        "recomputation of payload hashes",
        "cryptographic signature verification",
        "Ed25519 verification",
        "key resolution",
        "key rotation or revocation proof",
        "witness-reference resolution",
        "challenge execution",
        "independent interoperability",
        "production deployment conformance",
        "Authority remains a separate local policy decision.",
        "Ashby/requisite variety",
        "bounded information-theoretic disclosure",
        "canonical section 17",
    )
    for fragment in required_fragments:
        if fragment not in text:
            errors.append(f"publication README: missing required boundary {fragment!r}")

    for relative, digest in PROTECTED_HASHES.items():
        if relative not in text or digest not in text:
            errors.append(f"publication README: missing historical artifact/hash for {relative}")
        for ref in ("main", HISTORICAL_COMMIT):
            url = f"https://github.com/Kot141078/advanced-global-intelligence/blob/{ref}/{relative}"
            if url not in text:
                errors.append(f"publication README: missing historical mirror {url}")
    manifest_relative = "hashes/SHA256SUMS_beacon_v0.1_2026-03-10.txt"
    for ref in ("main", HISTORICAL_COMMIT):
        url = f"https://github.com/Kot141078/advanced-global-intelligence/blob/{ref}/{manifest_relative}"
        if url not in text:
            errors.append(f"publication README: missing historical manifest mirror {url}")

    for relative in (IMPLEMENTATION_MODULE, IMPLEMENTATION_TESTS):
        url = f"https://github.com/Kot141078/ester-clean-code/blob/{IMPLEMENTATION_COMMIT}/{relative}"
        if url not in text:
            errors.append(f"publication README: missing immutable implementation link {url}")

    if "cryptographically verified implementation" in text.casefold():
        errors.append("publication README: forbidden cryptographically verified implementation claim")


def validate_routing_surfaces(errors: list[str]) -> None:
    texts: dict[str, str] = {}
    for relative in ROUTING_SURFACES:
        text = read_utf8(ROOT / relative, errors)
        texts[relative] = text
        compact = normalized(text)
        for required in (
            PUBLISHED_DOI,
            "protocols/beacon/publication/",
            "PUBLICATION_RECORD.json",
            "hashes/SHA256SUMS_beacon_v0.1_2026-03-10.txt",
            IMPLEMENTATION_COMMIT,
            IMPLEMENTATION_MODULE,
            IMPLEMENTATION_TESTS,
        ):
            if required not in text:
                errors.append(f"{relative}: missing Beacon routing value {required!r}")
        if STATUS_CEILING not in compact:
            errors.append(f"{relative}: exact Beacon status ceiling is missing")

    human_surfaces = set(ROUTING_SURFACES) - {"REPO_INDEX.json"}
    for relative in sorted(human_surfaces):
        if IMPLEMENTATION_STATUS not in texts.get(relative, ""):
            errors.append(f"{relative}: exact implementation claim ceiling is missing")

    repo_index_text = texts.get("REPO_INDEX.md", "")
    if "docs-meaning-map/protocols/beacon" in repo_index_text:
        errors.append("REPO_INDEX.md: stale docs-meaning-map Beacon route remains")

    scan_paths = [PUBLICATION_DIR / name for name in PUBLICATION_FILES]
    scan_paths.extend(ROOT / relative for relative in ROUTING_SURFACES)
    for path in scan_paths:
        text = read_utf8(path, errors)
        relative = path.relative_to(ROOT).as_posix()
        if GUESSED_CONCEPT_DOI in text:
            errors.append(f"{relative}: forbidden guessed concept DOI {GUESSED_CONCEPT_DOI}")
        if path.parent == PUBLICATION_DIR and "Beacon Profile v0.2" in text:
            errors.append(f"{relative}: forbidden Beacon Profile v0.2 occurrence")


def validate_repo_index_json(errors: list[str]) -> None:
    data = load_json(ROOT / "REPO_INDEX.json", errors)
    if not isinstance(data, dict):
        if data is not None:
            errors.append("REPO_INDEX.json: root must be an object")
        return
    expected = {
        "beacon_profile_v0_1_root": "protocols/beacon/",
        "beacon_profile_v0_1_markdown_raw": (
            "https://raw.githubusercontent.com/Kot141078/advanced-global-intelligence/main/"
            "protocols/beacon/Beacon_Profile_v0.1_EN.md"
        ),
        "beacon_profile_v0_1_pdf_raw": (
            "https://raw.githubusercontent.com/Kot141078/advanced-global-intelligence/main/"
            "protocols/beacon/Beacon_Profile_v0.1_EN.pdf"
        ),
        "beacon_profile_v0_1_historical_commit": HISTORICAL_COMMIT,
        "beacon_profile_v0_1_published_doi": PUBLISHED_DOI,
        "beacon_profile_v0_1_doi_url": f"https://doi.org/{PUBLISHED_DOI}",
        "beacon_profile_v0_1_doi_role": "unresolved",
        "beacon_profile_v0_1_concept_doi": None,
        "beacon_profile_v0_1_zenodo_record": "https://zenodo.org/records/18933553",
        "beacon_profile_v0_1_publication_bridge_raw": (
            "https://raw.githubusercontent.com/Kot141078/advanced-global-intelligence/main/"
            "protocols/beacon/publication/README.md"
        ),
        "beacon_profile_v0_1_publication_record_raw": (
            "https://raw.githubusercontent.com/Kot141078/advanced-global-intelligence/main/"
            "protocols/beacon/publication/PUBLICATION_RECORD.json"
        ),
        "beacon_profile_v0_1_integrity_manifest_raw": (
            "https://raw.githubusercontent.com/Kot141078/advanced-global-intelligence/main/"
            "hashes/SHA256SUMS_beacon_v0.1_2026-03-10.txt"
        ),
        "beacon_profile_v0_1_implementation_repository": "Kot141078/ester-clean-code",
        "beacon_profile_v0_1_implementation_commit": IMPLEMENTATION_COMMIT,
        "beacon_profile_v0_1_implementation_module": IMPLEMENTATION_MODULE,
        "beacon_profile_v0_1_implementation_tests": IMPLEMENTATION_TESTS,
        "beacon_profile_v0_1_implementation_status": IMPLEMENTATION_STATUS_MACHINE,
        "beacon_profile_v0_1_claim_ceiling": STATUS_CEILING,
    }
    for key, value in expected.items():
        if data.get(key) != value:
            errors.append(f"REPO_INDEX.json: {key} must be {value!r}")
    if data.get("beacon_profile_v0_1_concept_doi", object()) is not None:
        errors.append("REPO_INDEX.json: beacon_profile_v0_1_concept_doi must be JSON null")


def validate_implementation_denials(errors: list[str]) -> None:
    record = load_json(PUBLICATION_RECORD, errors)
    readme = read_utf8(PUBLICATION_DIR / "README.md", errors)
    machine_entry = read_utf8(ROOT / "MACHINE_ENTRY.md", errors)
    if not isinstance(record, dict):
        return
    bridge = record.get("implementation_bridge")
    denials = bridge.get("does_not_demonstrate") if isinstance(bridge, dict) else None
    expected_json = {
        "payload-hash recomputation",
        "cryptographic signature verification",
        "Ed25519 verification",
        "key resolution",
        "witness-reference resolution",
    }
    if not isinstance(denials, list) or not expected_json.issubset(set(denials)):
        errors.append("PUBLICATION_RECORD.json: required implementation denials are incomplete")
    readme_terms = {
        "recomputation of payload hashes",
        "cryptographic signature verification",
        "Ed25519 verification",
        "key resolution",
        "witness-reference resolution",
    }
    missing_readme = sorted(term for term in readme_terms if term not in readme)
    if missing_readme:
        errors.append(f"publication README: required implementation denials missing {missing_readme!r}")
    machine_terms = {
        "payload-hash recomputation",
        "cryptographic signature verification",
        "Ed25519 verification",
        "key resolution",
        "witness-reference resolution",
    }
    missing_machine = sorted(term for term in machine_terms if term not in machine_entry)
    if missing_machine:
        errors.append(f"MACHINE_ENTRY.md: implementation boundary missing {missing_machine!r}")


def main() -> int:
    errors: list[str] = []
    validate_protected_files(errors)
    validate_publication_inventory(errors)
    validate_publication_record(errors)
    validate_citation_cff(errors)
    validate_publication_readme(errors)
    validate_routing_surfaces(errors)
    validate_repo_index_json(errors)
    validate_implementation_denials(errors)
    parse_checksum_manifest(
        PUBLICATION_MANIFEST,
        PUBLICATION_DIR,
        PUBLICATION_PAYLOADS,
        errors,
    )

    if errors:
        for error in errors:
            print(f"FAIL: {error}", file=sys.stderr)
        return 1

    print("PASS Beacon v0.1 DOI-safe publication bridge")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
