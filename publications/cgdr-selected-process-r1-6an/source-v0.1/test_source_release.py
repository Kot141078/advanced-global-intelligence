"""Tests of the publication checker, never of the CGDR runtime."""
import hashlib
import json
from pathlib import Path
import shutil
import tempfile
import unittest
from verify_source_release import safe_path, verify

ROOT = Path(__file__).resolve().parent


def reseal(root):
    rows = []
    for p in sorted(root.rglob('*')):
        if p.is_file() and p != root / 'SHA256SUMS.txt':
            rows.append(hashlib.sha256(p.read_bytes()).hexdigest() + '  ' + p.relative_to(root).as_posix())
    (root / 'SHA256SUMS.txt').write_text('\n'.join(rows) + '\n', encoding='utf-8')


class SourceReleaseTests(unittest.TestCase):
    def test_original(self):
        self.assertEqual(verify(ROOT)['accepted_source_files'], 93)

    def _modified(self, change, reseal_after=False):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td) / 'release'
            shutil.copytree(ROOT, root)
            change(root)
            if reseal_after:
                reseal(root)
            with self.assertRaises((ValueError, OSError)):
                verify(root)

    def test_tampered_code(self):
        self._modified(lambda r: (r / 'code/src/cgdr_r1_6b/common.py').write_text('changed'), True)

    def test_missing_notice_even_after_reseal(self):
        self._modified(lambda r: (r / 'NOTICES/c-hardening-pack-LICENSE.md').unlink(), True)

    def test_extra_code_even_after_reseal(self):
        self._modified(lambda r: (r / 'code/unexpected.py').write_text(''), True)

    def test_notice_byte_change_even_after_reseal(self):
        self._modified(lambda r: (r / 'NOTICES/CGAM-LICENSE.md').write_text('changed'), True)

    def test_source_manifest_change_even_after_reseal(self):
        self._modified(lambda r: (r / 'MANIFEST_CURRENT_AK.json').write_text('{}'), True)

    def test_missing_attribution(self):
        def change(r):
            p = r / 'SOURCE_LICENCE_INDEX.json'
            d = json.loads(p.read_text()); d['files'].pop()
            p.write_text(json.dumps(d))
        self._modified(change, True)

    def test_dependency_version_change(self):
        def change(r):
            p = r / 'DEPENDENCY_LICENCES.json'
            d = json.loads(p.read_text()); d['dependencies'][0]['version'] = '0.0.0'
            p.write_text(json.dumps(d))
        self._modified(change, True)

    def test_unsafe_paths(self):
        for name in ('../x', '/x', 'C:/x', 'a\\b', 'a/../b'):
            with self.subTest(name=name), self.assertRaises(ValueError):
                safe_path(name)

    def test_symlink(self):
        self._modified(lambda r: (r / 'link').symlink_to(r / 'README.md'))


if __name__ == '__main__':
    unittest.main()
