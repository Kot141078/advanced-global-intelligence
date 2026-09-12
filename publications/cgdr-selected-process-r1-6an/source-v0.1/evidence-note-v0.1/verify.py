"""Read-only verification of the public note; never runs CGDR or its workers."""
from __future__ import annotations
import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path, PurePosixPath
import re
import sys
import zipfile

CELLS = 'N0 N1 T0 T1 T2Q T2D T3 T4S T4R T5A T5E T6 T7 T8 T9 T10 T11W T11E'.split()
PAYLOAD = {'README.md', 'RIGHTS.md', 'CITATION.cff', 'evidence.json', 'verify.py', 'test_verify.py'}
SYMBOLS = {'PASS': 'P', 'FAIL': 'F', 'UNKNOWN': 'U', 'NOT_APPLICABLE': 'N'}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def verify_manifest(root: Path) -> int:
    entries = {}
    for line in (root / 'SHA256SUMS.txt').read_text(encoding='utf-8').splitlines():
        match = re.fullmatch(r'([0-9a-f]{64})  ([A-Za-z0-9_.-]+)', line)
        require(match is not None, 'Invalid manifest row')
        h, name = match.groups()
        require(name not in entries, 'Duplicate manifest path')
        entries[name] = h
    require(set(entries) == PAYLOAD, 'Unexpected manifest membership')
    for name, expected in entries.items():
        p = root / name
        require(p.is_file() and not p.is_symlink(), 'Missing file or symlink: ' + name)
        require(digest(p.read_bytes()) == expected, 'Hash mismatch: ' + name)
    return len(entries)


def verify_tables(data: dict) -> dict:
    require(data['artifact_kind'] == 'PUBLIC_DERIVATIVE_INTERNAL_RESULT_NOT_RAW_RUNTIME_ARCHIVE', 'Wrong evidence kind')
    require(data['profile_id'] == 'CGDR-R1.6A-SELECTED-PROCESS', 'Wrong profile')
    ep, cp, av = data['episodes'], data['checkpoints'], data['assertions']
    require([r[0] for r in ep] == CELLS, 'Missing, reordered or duplicate episode')
    require(all(len(r) == 7 for r in ep), 'Bad episode width')
    require(all(r[2:4] == ['COMPLETE', 'PASS'] for r in ep), 'Wrong episode status')
    require([r[1] for r in ep] == ['NO_REPLACEMENT', 'SHAM_BARRIER'] + ['REPLACE_PROCESS'] * 16, 'Wrong lifecycle')
    expected_coords = []
    for cell in CELLS:
        names = ['OPEN_CHECK', 'RESOLVED_CHECK'] if cell in CELLS[:3] else ['LATE_COMMIT_CHECK' if cell == 'T10' else 'fault']
        expected_coords.extend([[cell, name] for name in names])
    require(len(cp) == 21 and all(len(r) == 12 for r in cp), 'Bad checkpoint coverage/width')
    require([r[:2] for r in cp] == expected_coords, 'Wrong checkpoint coordinates')
    require([r[:2] for r in av] == expected_coords, 'Wrong assertion coordinates')
    require(all(len(r) == 3 and len(r[2]) == 36 and set(r[2]) <= set('PFUN') for r in av), 'Bad assertion encoding')
    require(all(r[2] == 'PASS' for r in cp), 'Wrong checkpoint profile verdict')
    require(Counter(r[3] for r in cp) == Counter({'PASS': 7, 'FAIL': 11, 'INCONCLUSIVE': 3}), 'Raw diagnostics lost')
    require([r[:2] for r in cp if r[8] != 0] == [[c, 'RESOLVED_CHECK'] for c in CELLS[:3]], 'Unexpected effect coordinate')
    require(all(type(r[8]) is int and r[8] in (0, 1) and type(r[9]) is int and r[9] == 0 for r in cp), 'Bad effects/promotions')
    for r in ep:
        subset = [c for c in cp if c[0] == r[0]]
        require(r[4:] == [len(subset), sum(c[8] for c in subset), sum(c[9] for c in subset)], 'Episode totals disagree')
    require([(r[0], r[11]) for r in cp if r[4] == 'FAIL'] == [('T3', 'O07_OBLIGATION_CARRIAGE_LOST'), ('T5A', 'O05_ALIAS_ROOTS_NOT_INDEPENDENT')], 'Alignment failures lost')
    for c, a in zip(cp, av):
        if c[3] == 'FAIL':
            require('F' in a[2], 'FAIL without a failed observer assertion')
        if c[1] == 'OPEN_CHECK':
            require(a[2][27] == 'U', 'Open R28 UNKNOWN lost')
    require(sum(r[8] for r in cp) == 3, 'Wrong total effects')
    return {'episodes': len(ep), 'checkpoints': len(cp), 'assertion_values': len(av) * 36, 'effects': 3, 'promotions': 0, 'raw_observer': dict(Counter(r[3] for r in cp))}


def source_tables(archive: Path, expected_hash: str) -> dict:
    require(archive.stat().st_size <= 32 * 1024 * 1024, 'Source too large')
    require(digest(archive.read_bytes()) == expected_hash, 'Not the frozen source archive')
    result = {'episodes': [], 'checkpoints': [], 'assertions': []}
    with zipfile.ZipFile(archive) as z:
        names = z.namelist()
        require(len(names) == len(set(names)) == 538, 'Unexpected source inventory')
        require(all(not PurePosixPath(n).is_absolute() and '..' not in PurePosixPath(n).parts for n in names), 'Unsafe archive path')
        require(sum(i.file_size for i in z.infolist()) <= 64 * 1024 * 1024, 'Expanded source too large')
        require(z.testzip() is None, 'Source CRC failure')
        paths = sorted(n for n in names if n.startswith('matrix_output/episodes/') and n.endswith('/EPISODE_RESULT.json'))
        require(len(paths) == 18, 'Wrong number of source episodes')
        for path in paths:
            j = json.loads(z.read(path))
            result['episodes'].append([j['cell_id'], j['lifecycle_mode'], j['execution_status'], j['conformance_verdict'], len(j['checkpoint_results']), j['effect_count'], j['promotion_count']])
            for c in j['checkpoint_results']:
                a = c['actual']
                result['checkpoints'].append([j['cell_id'], c['checkpoint'], c['profile_assertion']['verdict'], c['observer']['conformance_verdict'], c['alignment_review']['verdict'], a['admission'], a['q_state'], a['protected_action_gate'], a['protected_effect_delta'], a['confirmed_EA_delta'], c['fault_detection']['status'], ';'.join(x['code'] for x in c['alignment_review']['issues'])])
                assertions = {v['requirement_id']: v['value'] for v in c['observer']['assertions']}
                require(len(assertions) == 36, 'Source assertion coverage mismatch')
                result['assertions'].append([j['cell_id'], c['checkpoint'], ''.join(SYMBOLS[assertions[f'R{i:02}']] for i in range(1, 37))])
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source-zip', type=Path, help='Optional legitimately obtained frozen private archive; never fetched automatically')
    args = parser.parse_args()
    try:
        root = Path(__file__).resolve().parent
        count = verify_manifest(root)
        data = json.loads((root / 'evidence.json').read_text(encoding='utf-8'))
        totals = verify_tables(data)
        matched = False
        if args.source_zip is not None:
            projected = source_tables(args.source_zip, data['source_archive_sha256'])
            require(all(data[k] == projected[k] for k in projected), 'Public projection differs from source')
            matched = True
        print(json.dumps({'status': 'PASS_PUBLIC_NOTE_CONSISTENCY_ONLY', 'manifest_files': count, 'tables': totals, 'optional_source_rows_matched': matched, 'runtime_executed': False, 'independent_replication': False}, indent=2))
        return 0
    except (OSError, ValueError, KeyError, TypeError, IndexError, zipfile.BadZipFile) as exc:
        print('FAIL: ' + str(exc), file=sys.stderr)
        return 1


if __name__ == '__main__':
    raise SystemExit(main())
