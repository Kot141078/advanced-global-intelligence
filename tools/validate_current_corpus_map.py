#!/usr/bin/env python3
"""Validate CURRENT_CORPUS_MAP.json without third-party dependencies."""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parents[1]
MAP_PATH = ROOT / "CURRENT_CORPUS_MAP.json"
SCHEMA_PATH = ROOT / "schemas" / "current-corpus-map-v1.schema.json"
SHA1 = re.compile(r"^[0-9a-f]{40}$")
DOI = re.compile(r"^10\.5281/zenodo\.[0-9]+$")

TOP_LEVEL_KEYS = {
    "$schema",
    "schema",
    "schema_version",
    "map_id",
    "last_verified",
    "canonical_owner",
    "scope",
    "authority",
    "claim_boundaries",
    "current_pointer_policy",
    "historical_locks",
    "repositories",
}
REPOSITORY_KEYS = {
    "repository",
    "corpus_class",
    "role",
    "lifecycle",
    "authority_scope",
    "current_pointer",
    "declared_release",
    "entrypoints",
}

EXPECTED_REPOSITORIES = {
    "Kot141078/advanced-global-intelligence",
    "Kot141078/ai-social-role-separation-memory-custody",
    "Kot141078/c-governed-cli-agent-mesh",
    "Kot141078/c-hardening-pack",
    "Kot141078/cleanroom-arm-p-open-verification",
    "Kot141078/ester-clean-code",
    "Kot141078/ester-reality-bound",
    "Kot141078/ester-site",
    "Kot141078/ester-theoretical-core",
    "Kot141078/instrumental-c-public-portfolio",
    "Kot141078/kot141078.github.io",
    "Kot141078/qubit-of-hope-volume-i",
    "Kot141078/qubit-of-hope-volume-ii",
    "Kot141078/qubit-of-hope-volume-iii",
    "Kot141078/sovereign-entity-recursion",
    "Kot141078/tap-sec-reference-implementation",
    "Kot141078/world-intelligence",
    "Kot141078/world-intelligence-serial-edition-01",
}


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def require_https(errors: list[str], label: str, value: object) -> None:
    if not isinstance(value, str):
        fail(errors, f"{label}: expected string URL")
        return
    parsed = urlparse(value)
    if parsed.scheme != "https" or not parsed.netloc:
        fail(errors, f"{label}: expected absolute HTTPS URL, got {value!r}")


def require_date(errors: list[str], label: str, value: object) -> None:
    if not isinstance(value, str):
        fail(errors, f"{label}: expected ISO date string")
        return
    try:
        dt.date.fromisoformat(value)
    except ValueError:
        fail(errors, f"{label}: invalid ISO date {value!r}")


def validate_structure(data: dict[str, object], schema: dict[str, object]) -> list[str]:
    errors: list[str] = []

    if set(data) != TOP_LEVEL_KEYS:
        fail(errors, f"top-level keys mismatch; missing={sorted(TOP_LEVEL_KEYS - set(data))}, extra={sorted(set(data) - TOP_LEVEL_KEYS)}")
    if data.get("$schema") != "schemas/current-corpus-map-v1.schema.json":
        fail(errors, "$schema must point to schemas/current-corpus-map-v1.schema.json")
    if data.get("schema") != "agi.current_corpus_map.v1":
        fail(errors, "schema must be agi.current_corpus_map.v1")
    if data.get("schema_version") != "1.0.0":
        fail(errors, "schema_version must be 1.0.0")
    if schema.get("$schema") != "https://json-schema.org/draft/2020-12/schema":
        fail(errors, "schema document must use JSON Schema draft 2020-12")
    require_date(errors, "last_verified", data.get("last_verified"))
    if data.get("map_id") != f"urn:ivankotov:corpus-map:public:{data.get('last_verified')}":
        fail(errors, "map_id must end with the exact last_verified date")
    if data.get("canonical_owner") != {
        "name": "Ivan Kotov",
        "github": "Kot141078",
        "orcid": "https://orcid.org/0009-0009-6002-9845",
    }:
        fail(errors, "canonical_owner must identify Ivan Kotov, Kot141078, and ORCID 0009-0009-6002-9845")

    scope = data.get("scope")
    if not isinstance(scope, dict) or scope.get("repository_count") != 18:
        fail(errors, "scope.repository_count must be 18")

    authority = data.get("authority")
    if not isinstance(authority, dict):
        fail(errors, "authority must be an object")
    else:
        if authority.get("map_status") != "derived current-discovery snapshot":
            fail(errors, "authority.map_status must identify a derived current-discovery snapshot")
        for key in ("authoritative_for", "not_authoritative_for", "precedence"):
            value = authority.get(key)
            if not isinstance(value, list) or not value or not all(isinstance(item, str) and item for item in value):
                fail(errors, f"authority.{key} must be a non-empty string array")

    boundaries = data.get("claim_boundaries")
    if not isinstance(boundaries, list) or len(boundaries) < 5:
        fail(errors, "claim_boundaries must contain at least five explicit boundaries")

    locks = data.get("historical_locks")
    if not isinstance(locks, list) or not locks:
        fail(errors, "historical_locks must be a non-empty array")
    else:
        for index, lock in enumerate(locks):
            if not isinstance(lock, dict) or lock.get("status") != "historical_snapshot":
                fail(errors, f"historical_locks[{index}] must be explicitly historical_snapshot")
            if isinstance(lock, dict) and lock.get("path") == "STACK_LOCK_2026-04-12.json":
                if lock.get("date") != "2026-04-12":
                    fail(errors, "STACK_LOCK_2026-04-12.json must retain its original date")
                lock_path = ROOT / "STACK_LOCK_2026-04-12.json"
                if not lock_path.is_file():
                    fail(errors, "historical stack-lock file is missing")
                else:
                    actual_sha256 = hashlib.sha256(lock_path.read_bytes()).hexdigest()
                    if lock.get("sha256") != actual_sha256:
                        fail(errors, "historical stack-lock sha256 does not match the retained file bytes")

    repositories = data.get("repositories")
    if not isinstance(repositories, list):
        fail(errors, "repositories must be an array")
        return errors
    if len(repositories) != 18:
        fail(errors, f"repositories must contain 18 records, got {len(repositories)}")

    names = [record.get("repository") for record in repositories if isinstance(record, dict)]
    if len(names) != len(set(names)):
        fail(errors, "repository names must be unique")
    if set(names) != EXPECTED_REPOSITORIES:
        missing = sorted(EXPECTED_REPOSITORIES - set(names))
        extra = sorted(set(names) - EXPECTED_REPOSITORIES)
        fail(errors, f"repository membership mismatch; missing={missing}, extra={extra}")

    for index, record in enumerate(repositories):
        if not isinstance(record, dict):
            fail(errors, f"repositories[{index}] must be an object")
            continue
        name = record.get("repository")
        label = str(name)
        if set(record) != REPOSITORY_KEYS:
            fail(errors, f"{label}: record keys mismatch; missing={sorted(REPOSITORY_KEYS - set(record))}, extra={sorted(set(record) - REPOSITORY_KEYS)}")
        if not isinstance(record.get("role"), str) or not record.get("role"):
            fail(errors, f"{label}: role must be non-empty")
        if not isinstance(record.get("authority_scope"), str) or not record.get("authority_scope"):
            fail(errors, f"{label}: authority_scope must be non-empty")

        pointer = record.get("current_pointer")
        if not isinstance(pointer, dict):
            fail(errors, f"{label}: current_pointer must be an object")
            continue
        if pointer.get("ref_type") != "branch" or pointer.get("ref") != "main":
            fail(errors, f"{label}: mutable current pointer must be branch main")
        if pointer.get("observed_at") != data.get("last_verified"):
            fail(errors, f"{label}: observed_at must equal map last_verified")
        require_date(errors, f"{label}.current_pointer.observed_at", pointer.get("observed_at"))
        sha = pointer.get("observed_head_commit")
        if not isinstance(sha, str) or not SHA1.fullmatch(sha):
            fail(errors, f"{label}: observed_head_commit must be a 40-character lowercase SHA-1")
        for key in ("branch_url", "raw_branch_base", "observed_commit_url", "raw_observed_base"):
            require_https(errors, f"{label}.current_pointer.{key}", pointer.get(key))
        if isinstance(sha, str):
            slug = label.split("/", 1)[-1]
            expected_urls = {
                "branch_url": f"https://github.com/Kot141078/{slug}/tree/main",
                "raw_branch_base": f"https://raw.githubusercontent.com/Kot141078/{slug}/main/",
                "observed_commit_url": f"https://github.com/Kot141078/{slug}/tree/{sha}",
                "raw_observed_base": f"https://raw.githubusercontent.com/Kot141078/{slug}/{sha}/",
            }
            for key, expected_url in expected_urls.items():
                if pointer.get(key) != expected_url:
                    fail(errors, f"{label}: {key} must be {expected_url}")
            if sha not in str(pointer.get("observed_commit_url", "")):
                fail(errors, f"{label}: observed_commit_url must contain observed_head_commit")
            if sha not in str(pointer.get("raw_observed_base", "")):
                fail(errors, f"{label}: raw_observed_base must contain observed_head_commit")

        release = record.get("declared_release")
        if not isinstance(release, dict):
            fail(errors, f"{label}: declared_release must be an object")
        else:
            doi = release.get("doi")
            if doi is not None and (not isinstance(doi, str) or not DOI.fullmatch(doi)):
                fail(errors, f"{label}: declared release DOI has unsupported syntax: {doi!r}")
            if doi is None and release.get("doi_source") is not None:
                fail(errors, f"{label}: doi_source must be null when doi is null")
            if doi is not None and not release.get("doi_source"):
                fail(errors, f"{label}: doi_source is required when doi is present")
            version = release.get("version")
            if version is None and release.get("version_source") is not None:
                fail(errors, f"{label}: version_source must be null when version is null")
            if version is not None and not release.get("version_source"):
                fail(errors, f"{label}: version_source is required when version is present")
            if release.get("metadata_consistency") == "known_conflict" and not release.get("note"):
                fail(errors, f"{label}: known metadata conflicts require an explicit note")

        entrypoints = record.get("entrypoints")
        if not isinstance(entrypoints, list) or not entrypoints:
            fail(errors, f"{label}: entrypoints must be a non-empty array")
        elif any(not isinstance(path, str) or path.startswith("/") or ".." in Path(path).parts for path in entrypoints):
            fail(errors, f"{label}: entrypoints must be safe relative paths")

    archived = {record["repository"] for record in repositories if record.get("lifecycle") == "archived"}
    if archived != {"Kot141078/ester-site"}:
        fail(errors, f"only ester-site may be marked archived in this snapshot, got {sorted(archived)}")

    clean = next((record for record in repositories if record.get("repository") == "Kot141078/ester-clean-code"), None)
    if not isinstance(clean, dict) or clean.get("declared_release", {}).get("metadata_consistency") != "aligned":
        fail(errors, "ester-clean-code release metadata must remain aligned")

    return errors


def validate_workspace(data: dict[str, object], workspace_root: Path) -> list[str]:
    """Optionally verify the exact locally observed commits and entrypoint presence."""
    errors: list[str] = []
    for record in data["repositories"]:
        slug = record["repository"].split("/", 1)[1]
        candidates = [workspace_root / slug, workspace_root / "corpus" / slug]
        if slug == "kot141078.github.io":
            candidates.extend([workspace_root / "site-repo", workspace_root.parent / "site-repo"])
        repo_dir = next((path for path in candidates if (path / ".git").exists()), None)
        if repo_dir is None:
            fail(errors, f"{record['repository']}: local clone not found below {workspace_root}")
            continue
        try:
            head = subprocess.check_output(
                ["git", "-C", str(repo_dir), "rev-parse", "HEAD"], text=True, stderr=subprocess.DEVNULL
            ).strip()
        except subprocess.CalledProcessError:
            fail(errors, f"{record['repository']}: unable to read local git HEAD")
            continue
        expected = record["current_pointer"]["observed_head_commit"]
        if head != expected:
            fail(errors, f"{record['repository']}: local HEAD {head} != observed {expected}")
        for relative in record["entrypoints"]:
            if not (repo_dir / relative).is_file():
                fail(errors, f"{record['repository']}: missing local entrypoint {relative}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--workspace-root",
        type=Path,
        help="Optional directory containing all sibling repository clones; validates commits and entrypoint files.",
    )
    args = parser.parse_args()

    try:
        data = json.loads(MAP_PATH.read_text(encoding="utf-8"))
        schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1

    errors = validate_structure(data, schema)
    if args.workspace_root is not None:
        errors.extend(validate_workspace(data, args.workspace_root.resolve()))

    if errors:
        for error in errors:
            print(f"FAIL: {error}", file=sys.stderr)
        return 1

    suffix = " + workspace snapshot" if args.workspace_root is not None else ""
    print(f"PASS: CURRENT_CORPUS_MAP.json (18 repositories{suffix})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
