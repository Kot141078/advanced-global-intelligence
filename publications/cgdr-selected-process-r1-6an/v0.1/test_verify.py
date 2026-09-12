"""Tests of the publication checker, not CGDR runtime tests."""
import copy
import json
from pathlib import Path
import shutil
import tempfile
import unittest
from verify import verify_manifest, verify_tables

ROOT = Path(__file__).resolve().parent
DATA = json.loads((ROOT / 'evidence.json').read_text(encoding='utf-8'))


class PublicationCheckTests(unittest.TestCase):
    def test_complete_data(self):
        self.assertEqual(verify_tables(DATA)['assertion_values'], 756)

    def test_missing_episode(self):
        d = copy.deepcopy(DATA)
        d['episodes'].pop()
        with self.assertRaises(ValueError):
            verify_tables(d)

    def test_missing_checkpoint(self):
        d = copy.deepcopy(DATA)
        d['checkpoints'].pop()
        with self.assertRaises(ValueError):
            verify_tables(d)

    def test_hidden_diagnostic_failure(self):
        d = copy.deepcopy(DATA)
        d['checkpoints'][6][3] = 'PASS'
        with self.assertRaises(ValueError):
            verify_tables(d)

    def test_unexpected_effect(self):
        d = copy.deepcopy(DATA)
        d['checkpoints'][-1][8] = 1
        with self.assertRaises(ValueError):
            verify_tables(d)

    def test_lost_unknown(self):
        d = copy.deepcopy(DATA)
        d['assertions'][0][2] = d['assertions'][0][2].replace('U', 'P')
        with self.assertRaises(ValueError):
            verify_tables(d)

    def test_manifest(self):
        self.assertEqual(verify_manifest(ROOT), 6)

    def test_tampered_file(self):
        with tempfile.TemporaryDirectory() as td:
            dest = Path(td) / 'note'
            shutil.copytree(ROOT, dest)
            (dest / 'RIGHTS.md').write_text('Changed', encoding='utf-8')
            with self.assertRaises(ValueError):
                verify_manifest(dest)


if __name__ == '__main__':
    unittest.main()
