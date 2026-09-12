"""Check publication bytes and DOI bindings. Never execute or import CGDR code."""
from __future__ import annotations
import hashlib
import json
from pathlib import Path, PurePosixPath
import re
import sys

DOI = '10.5281/zenodo.22724626'
VERSION = '0.1.1'
SOURCE_TREE = '657c4e884aaf2a3a50811be722fdad9fe03bb5c3'


def require(ok: bool, message: str) -> None:
    if not ok:
        raise ValueError(message)


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def object_hash(kind: str, data: bytes) -> str:
    return hashlib.sha1(kind.encode() + b' ' + str(len(data)).encode() + b'\0' + data).hexdigest()


def git_tree(root: Path) -> str:
    """Compute the Git tree identity of a 100644-file/040000-directory snapshot."""
    entries = []
    for p in root.iterdir():
        require(not p.is_symlink(), 'Symlink excluded')
        name = p.name.encode('utf-8')
        if p.is_dir():
            mode, sha, order = b'40000', git_tree(p), name + b'/'
        elif p.is_file():
            mode, sha, order = b'100644', object_hash('blob', p.read_bytes()), name
        else:
            raise ValueError('Non-regular archive member')
        entries.append((order, mode + b' ' + name + b'\0' + bytes.fromhex(sha)))
    return object_hash('tree', b''.join(row for _, row in sorted(entries)))


def verify(root: Path) -> dict:
    root = root.resolve()
    rows = {}
    for line in (root / 'SHA256SUMS.txt').read_text(encoding='utf-8').splitlines():
        match = re.fullmatch(r'([a-f0-9]{64})  (.+)', line)
        require(match is not None, 'Malformed checksum row')
        sha, name = match.groups()
        path = PurePosixPath(name)
        require(not path.is_absolute() and str(path) == name and '..' not in path.parts
                and '\\' not in name and ':' not in name, 'Unsafe checksum path')
        require(name not in rows and name != 'SHA256SUMS.txt', 'Duplicate/self checksum')
        rows[name] = sha
    paths = list(root.rglob('*'))
    require(not any(p.is_symlink() for p in paths), 'Symlink excluded')
    actual = {p.relative_to(root).as_posix() for p in paths if p.is_file()}
    require(actual == set(rows) | {'SHA256SUMS.txt'}, 'Publication inventory mismatch')
    require(sum((root / p).stat().st_size for p in actual) < 20_000_000, 'Package size limit')
    for name, sha in rows.items():
        require(digest((root / name).read_bytes()) == sha, 'Hash mismatch: ' + name)
    src = root / 'source-v0.1'
    require(git_tree(src) == SOURCE_TREE, 'Frozen source publication differs from Git tree')
    source_files = [p for p in src.rglob('*') if p.is_file()]
    require(len(source_files) == 118, 'Wrong original source-publication count')
    manifest = json.loads((src / 'MANIFEST_CURRENT_AK.json').read_text(encoding='utf-8'))
    require(manifest['file_count'] == len(manifest['files']) == 93, 'Wrong current-AK count')
    for row in manifest['files']:
        data = (src / 'code' / row['path']).read_bytes()
        require(len(data) == row['bytes'] and digest(data) == row['sha256'], 'Changed accepted source')
    fields = json.loads((root / 'ZENODO_FORM_VALUES.json').read_text(encoding='utf-8'))
    require(fields['doi'] == DOI and fields['version'] == VERSION, 'Wrong DOI/version')
    require(fields['creators'] == [{'type': 'Person', 'given_name': 'Ivan', 'family_name': 'Kotov',
                                   'orcid': '0009-0009-6002-9845', 'affiliation': None}], 'Wrong author')
    require(len(fields['licenses']) == 1 and fields['licenses'][0]['type'] == 'custom', 'Wrong blanket license')
    for name in ('CITATION.cff', 'CITATION.bib', 'README.md', 'codemeta.json', 'TECHNICAL_REPORT.md'):
        require(DOI in (root / name).read_text(encoding='utf-8'), 'DOI absent: ' + name)
    evidence = json.loads((src / 'evidence-note-v0.1/evidence.json').read_text(encoding='utf-8'))
    return {'status': 'PASS_PUBLICATION_BYTES_AND_CITATION_ONLY', 'doi': DOI, 'version': VERSION,
            'publication_files': len(actual), 'checksums': len(rows), 'frozen_source_publication_files': 118,
            'accepted_source_files_unchanged': 93, 'profile_files_unchanged': 3,
            'source_git_tree': SOURCE_TREE, 'episode_rows': len(evidence['episodes']),
            'checkpoint_rows': len(evidence['checkpoints']), 'observer_values': sum(len(r[2]) for r in evidence['assertions']),
            'research_runtime_executed': False, 'independent_replication': False,
            'zenodo_submission_performed': False}


def main() -> int:
    try:
        print(json.dumps(verify(Path(__file__).resolve().parent), indent=2))
        return 0
    except (OSError, ValueError, KeyError, TypeError) as exc:
        print('FAIL_PUBLICATION_CHECK: ' + str(exc), file=sys.stderr)
        return 1


if __name__ == '__main__':
    raise SystemExit(main())
