"""Read-only source publication verification; never imports or runs CGDR."""
from __future__ import annotations
import argparse
import ast
import hashlib
import json
from pathlib import Path, PurePosixPath
import re
import sys

SOURCE_MANIFEST_HASH = '2c4c37d65763f08b7df2381c43400b036f4a358a65db96661c67170e3c234c49'
NOTICE_BLOBS = {
    'c-hardening-pack-LICENSE.md': '744e1965596813db66b40fd4284ac531fffb6d3b',
    'c-hardening-pack-COMMERCIAL_AND_NON_IMPLEMENTATION_NOTICE.md': '5b2fff993695b1b4f238cf01c3b4d420ddacbf23',
    'CGAM-LICENSE.md': 'f583c64bc43b1a3da8f6a69b99661b35a0aad41d',
    'LICENSE-DOCS-CC-BY-4.0.md': 'a89e7b0b59a9f4b1504bf441410bc4e08b198e3c',
}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def safe_path(name: str) -> PurePosixPath:
    p = PurePosixPath(name)
    require(bool(name) and not p.is_absolute() and p.as_posix() == name,
            'Noncanonical path: ' + name)
    require('..' not in p.parts and '\\' not in name and ':' not in name,
            'Unsafe path: ' + name)
    return p


def read_json(path: Path):
    def unique(pairs):
        d = {}
        for k, v in pairs:
            require(k not in d, 'Duplicate JSON key: ' + k)
            d[k] = v
        return d
    return json.loads(path.read_text(encoding='utf-8'), object_pairs_hook=unique)


def verify(root: Path) -> dict:
    root = root.resolve()
    manifest = {}
    for line in (root / 'SHA256SUMS.txt').read_text(encoding='utf-8').splitlines():
        match = re.fullmatch(r'([a-f0-9]{64})  (.+)', line)
        require(match is not None, 'Malformed public manifest row')
        digest, name = match.groups()
        safe_path(name)
        require(name not in manifest and name != 'SHA256SUMS.txt', 'Duplicate/self manifest entry')
        manifest[name] = digest
    all_paths = list(root.rglob('*'))
    require(not any(p.is_symlink() for p in all_paths), 'Symlink is not part of the release')
    actual = {p.relative_to(root).as_posix() for p in all_paths if p.is_file()}
    require(actual == set(manifest) | {'SHA256SUMS.txt'}, 'Public inventory mismatch (including caches)')
    for name, digest in manifest.items():
        require(sha((root / name).read_bytes()) == digest, 'Public file hash mismatch: ' + name)

    raw = (root / 'MANIFEST_CURRENT_AK.json').read_bytes()
    require(sha(raw) == SOURCE_MANIFEST_HASH, 'Not the accepted current-AK manifest')
    source = read_json(root / 'MANIFEST_CURRENT_AK.json')
    require(source['file_count'] == len(source['files']) == 93, 'Source denominator mismatch')
    expected = {'code/' + r['path']: r for r in source['files']}
    require(len(expected) == 93, 'Duplicate accepted source path')
    require({n for n in actual if n.startswith('code/')} == set(expected), 'Source inventory mismatch')
    for name, row in expected.items():
        safe_path(name)
        data = (root / name).read_bytes()
        require(len(data) == row['bytes'] and sha(data) == row['sha256'], 'Source byte mismatch: ' + name)

    index = read_json(root / 'SOURCE_LICENCE_INDEX.json')
    rows = index['files']
    indexed = {r['path']: r for r in rows}
    payload = {n for n in actual if n.startswith(('code/', 'profile/'))}
    require(index['source_files'] == 93 and index['profile_files'] == 3, 'Attribution denominator mismatch')
    require(len(rows) == len(indexed) == len(payload) == 96 and set(indexed) == payload,
            'Attribution coverage mismatch')
    for name, row in indexed.items():
        safe_path(name)
        data = (root / name).read_bytes()
        require(row['bytes'] == len(data) and row['sha256'] == sha(data), 'Attribution byte binding mismatch')
        require(row['publication_transformation'] == 'NONE', 'Unexpected source transformation')
        require(bool(row['notices']), 'Missing applicable notices')
        for notice in row['notices']:
            safe_path(notice)
            require(notice in actual, 'Missing notice: ' + notice)
        if row['origin_category'] in ('CGAM_DOCUMENT', 'SER_DOCUMENT'):
            require(row['existing_license'] == 'CC-BY-4.0' and row['research_supplement'] is False,
                    'Existing CC BY rights were narrowed')
    for name, expected_blob in NOTICE_BLOBS.items():
        data = (root / 'NOTICES' / name).read_bytes()
        blob = hashlib.sha1(b'blob ' + str(len(data)).encode('ascii') + b'\0' + data).hexdigest()
        require(blob == expected_blob, 'Upstream notice copy changed: ' + name)

    lock = read_json(root / 'code' / 'DEPENDENCY_LOCK.json')
    pinned = dict(lock['native_requirements'], **lock['signer_requirements'])
    registry = read_json(root / 'DEPENDENCY_LICENCES.json')
    deps = registry['dependencies']
    require(len(deps) == len(pinned) == 12, 'Dependency denominator mismatch')
    require({r['name']: r['version'] for r in deps} == pinned, 'Dependency versions were changed')
    require(registry['wheels_in_package'] is False and registry['environments_in_package'] is False,
            'Unexpected binary/environments claim')
    require(all(r['scope'] == 'EXTERNAL_INSTALLATION_DEPENDENCY_NOT_REDISTRIBUTED' for r in deps),
            'Dependency distribution boundary changed')
    count = 0
    for name in expected:
        if name.endswith('.py'):
            ast.parse((root / name).read_text(encoding='utf-8'), filename=name)
            count += 1
    require(count == 36, 'Python source count mismatch')
    return {'status': 'PASS_SOURCE_PUBLICATION_INTEGRITY_AND_COVERAGE_ONLY',
            'public_payload_files': len(manifest), 'accepted_source_files': 93,
            'profile_files': 3, 'attribution_rows': 96, 'external_dependency_entries': 12,
            'upstream_notice_copies_matched': 4, 'python_source_files_parsed': 36,
            'source_runtime_executed': False, 'matrix_replayed': False,
            'legal_title_certification': False, 'independent_replication': False}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parent)
    args = parser.parse_args()
    try:
        print(json.dumps(verify(args.root), indent=2))
        return 0
    except (OSError, ValueError, KeyError, TypeError, SyntaxError) as exc:
        print('FAIL: ' + str(exc), file=sys.stderr)
        return 1


if __name__ == '__main__':
    raise SystemExit(main())
