"""Publication checker tests only; not CGDR experiments."""
from pathlib import Path
import hashlib
import json
import shutil
import tempfile
import unittest
from verify_publication import verify, git_tree, SOURCE_TREE
ROOT = Path(__file__).resolve().parent

class PublicationTests(unittest.TestCase):
    def mutate(self, fn, resign=False):
        with tempfile.TemporaryDirectory() as td:
            dst=Path(td)/'publication'
            shutil.copytree(ROOT,dst)
            fn(dst)
            if resign:
                lines=[]
                for p in sorted(dst.rglob('*')):
                    if p.is_file() and p != dst/'SHA256SUMS.txt':
                        lines.append(hashlib.sha256(p.read_bytes()).hexdigest()+'  '+p.relative_to(dst).as_posix())
                (dst/'SHA256SUMS.txt').write_text('\n'.join(lines)+'\n',encoding='utf-8')
            with self.assertRaises((ValueError, OSError)):
                verify(dst)
    def test_exact_publication(self):
        self.assertEqual(verify(ROOT)['accepted_source_files_unchanged'],93)
    def test_frozen_source_tree(self):
        self.assertEqual(git_tree(ROOT/'source-v0.1'),SOURCE_TREE)
    def test_changed_document(self):
        self.mutate(lambda r:(r/'README.md').write_text('tamper'))
    def test_extra_file(self):
        self.mutate(lambda r:(r/'extra.txt').write_text('extra'))
    def test_missing_notice(self):
        self.mutate(lambda r:(r/'source-v0.1/NOTICES/CGAM-LICENSE.md').unlink())
    def test_rehashed_source_tamper(self):
        self.mutate(lambda r:(r/'source-v0.1/README.md').write_text('rewritten'),True)
    def test_wrong_doi_even_if_rehashed(self):
        def change(r):
            p=r/'ZENODO_FORM_VALUES.json';d=json.loads(p.read_text());d['doi']='10.5281/zenodo.0';p.write_text(json.dumps(d))
        self.mutate(change,True)
    def test_unsafe_manifest(self):
        self.mutate(lambda r:(r/'SHA256SUMS.txt').write_text('0'*64+'  ../escape\n'))

if __name__ == '__main__':
    unittest.main()
