#!/usr/bin/env python3
"""One-work, byte-exact mirror of the owner-published ACOW English v0.2.
No model/game execution, deposit mutation, global license change, or auto-promotion.
"""
from __future__ import annotations
import argparse
import hashlib
import io
import json
from pathlib import Path
import re
import sys
import urllib.request
import zipfile

SLUG = 'shared-open-worlds-human-ai-dyads-v0-2'
TITLE = 'Shared Open Worlds for Human–AI Dyads: Role Switching, Experience Qualification, and Cross-World Continuity Evaluation'
DOI = '10.5281/zenodo.22542470'
CONCEPT = '10.5281/zenodo.22542469'
RECORD = 'https://zenodo.org/records/22542470'
SITE = 'https://ivankotov.eu/publications/' + SLUG + '/'
ZIP_NAME = 'A_C_SHARED_OPEN_WORLD_EXPERIENCE_v0_2_EN_PUBLIC.zip'
PDF_NAME = 'A_C_SHARED_OPEN_WORLD_EXPERIENCE_PAPER_v0_2_EN.pdf'
ZIP_HASH = '47945ca619f65ea6788de84c22ee278d0cee29fba929ab0e7e1db5fe17cc92ce'
ZIP_BYTES = 301436
PINS = {
 'A_C_SHARED_OPEN_WORLD_EXPERIENCE_PAPER_v0_2_EN.docx': (73105, 'd883ab3c39ded3bffeef94543d5380762f5cbd2e2bd70d0a999cf90e143a8591'),
 'A_C_SHARED_OPEN_WORLD_EXPERIENCE_PAPER_v0_2_EN.md': (84341, 'a832f5e7f207c1b563300ea6976db94785940b7d1342a8db65c629899749c396'),
 PDF_NAME: (307911, '59a69617fdc64092286296126d60d6331285105408ac4f54c474230240e03aee'),
 'CITATION.bib': (427, 'e7eb102f894b126191888e03c7961b18e03a6cf44df3a7de23f7ddee64ac2fb5'),
 'EDITION_AND_SOURCE_NOTE.md': (3372, '674c93b9789822e211e98accab8adde5c403eeb98aaec9769a09ce05cb42c331'),
 'LICENSE.md': (1986, 'deabf811c995784eab75486ee428eaedb9041f432a0f6004fe6042c330e98a7c'),
 'PUBLIC_SOURCE_SCOPE.json': (18087, '7ae75a091baf0dbff6ad7c5d0568730c8b89370136b81d07d19f2643237cacc7'),
 'README.md': (2451, '1970d0b67b1b6b752d3d3d95f9e8887ce4ebbb23fe9a096138ec12c6a62a56f9'),
 'SHA256SUMS.txt': (767, 'f7cc62f6df203b016257b9389c4cd98aec7de04e109430d16670467704da51b2'),
}

def digest(data: bytes) -> str:
 return hashlib.sha256(data).hexdigest()

def check(data: bytes, size: int, expected: str, name: str) -> bytes:
 if len(data) != size or digest(data) != expected:
  raise ValueError('EXACT_BYTE_MISMATCH: ' + name)
 return data

def fetch(name: str, size: int, expected: str) -> tuple[bytes, dict]:
 url = RECORD + '/files/' + name + '?download=1'
 req = urllib.request.Request(url, headers={'User-Agent': 'Kotov-ACOW-Publication-Mirror/0.2'})
 with urllib.request.urlopen(req, timeout=90) as response:
  data = response.read(size + 1)
  observation = {'source_url': url, 'final_url': response.geturl(), 'http_status': response.status}
  if response.status != 200:
   raise ValueError('Unexpected HTTP status for ' + name)
 check(data, size, expected, name)
 observation.update(bytes=len(data), sha256=digest(data))
 return data, observation

def unpack(raw: bytes) -> dict[str, bytes]:
 check(raw, ZIP_BYTES, ZIP_HASH, ZIP_NAME)
 with zipfile.ZipFile(io.BytesIO(raw)) as z:
  infos = z.infolist()
  if len(infos) != 9 or {x.filename for x in infos} != set(PINS):
   raise ValueError('Archive member set differs from the published nine-file package')
  if any(x.is_dir() or (x.external_attr >> 16) & 0o170000 == 0o120000 for x in infos):
   raise ValueError('Unexpected directory or symlink')
  if sum(x.file_size for x in infos) > 1000000:
   raise ValueError('Unexpected expanded archive size')
  members = {x.filename: check(z.read(x), *PINS[x.filename], x.filename) for x in infos}
 checks = members['SHA256SUMS.txt'].decode('utf-8').splitlines()
 names = set()
 for line in checks:
  expected, name = line.split('  ', 1)
  if name in names or name not in members or digest(members[name]) != expected:
   raise ValueError('Internal checksum failure: ' + name)
  names.add(name)
 if names != set(members) - {'SHA256SUMS.txt'}:
  raise ValueError('Incomplete internal checksum coverage')
 for name, data in members.items():
  if name.endswith(('.md', '.json', '.bib', '.txt')):
   text = data.decode('utf-8')
   if re.search(r'https?://(?:drive\.google\.com|docs\.google\.com)', text, re.I):
    raise ValueError('Private Drive locator in public payload: ' + name)
 license_text = members['LICENSE.md'].decode('utf-8')
 if 'https://creativecommons.org/licenses/by/4.0/' not in license_text or 'CC BY-NC' in license_text:
  raise ValueError('Published license mismatch')
 return members

def exact_write(path: Path, data: bytes) -> None:
 if path.is_symlink() or (path.exists() and path.read_bytes() != data):
  raise ValueError('Refusing to replace different existing bytes: ' + str(path))
 path.parent.mkdir(parents=True, exist_ok=True)
 path.write_bytes(data)

def mirror(root: Path, raw: bytes, members: dict[str, bytes], observations: list[dict]) -> dict:
 destination = root / 'publications' / SLUG
 for name, data in members.items():
  exact_write(destination / 'release' / name, data)
 exact_write(destination / ZIP_NAME, raw)
 metadata = {
  'id': SLUG, 'title': TITLE, 'version': '0.2', 'publication_date': '2026-09-06',
  'publication_type': 'preprint', 'language': 'en', 'author': 'Ivan Kotov',
  'orcid': 'https://orcid.org/0009-0009-6002-9845',
  'version_doi': DOI, 'concept_doi': CONCEPT, 'zenodo_record': RECORD,
  'canonical_page': SITE, 'license': 'CC-BY-4.0',
  'license_url': 'https://creativecommons.org/licenses/by/4.0/',
  'archive': {'filename': ZIP_NAME, 'bytes': ZIP_BYTES, 'sha256': ZIP_HASH},
  'payloads': [{'path': 'release/' + n, 'bytes': s, 'sha256': h} for n, (s, h) in PINS.items()],
  'related_works': [{'relation': 'references', 'doi': '10.5281/zenodo.21751985'}, {'relation': 'references', 'doi': '10.5281/zenodo.22085394'}],
  'evidence_boundary': 'Conceptual and methodological preprint; no empirical experiment, runtime implementation, independently annotated benchmark, or separate peer review of English v0.2. C/B1 treatment remains unspecified.',
  'mirror_policy': 'All nine deposited members and the public ZIP remain byte-exact. Post-publication DOI metadata are additive sidecars outside release/.',
 }
 exact_write(destination / 'PUBLICATION.json', (json.dumps(metadata, ensure_ascii=False, indent=2)+'\n').encode())
 citation = f'''cff-version: 1.2.0
message: "Cite the published preprint, not this repository as an empirical implementation."
type: article
title: "{TITLE}"
authors:
  - family-names: Kotov
    given-names: Ivan
    orcid: https://orcid.org/0009-0009-6002-9845
version: "0.2"
date-released: 2026-09-06
doi: {DOI}
url: {SITE}
license: CC-BY-4.0
'''
 exact_write(destination/'CITATION.cff', citation.encode())
 readme = f'''# Shared Open Worlds for Human–AI Dyads

Role Switching, Experience Qualification, and Cross-World Continuity Evaluation.

**Ivan Kotov · English v0.2 · Published 6 September 2026 · Preprint · CC BY 4.0**

- [Version-specific DOI](https://doi.org/{DOI})
- [All-versions DOI](https://doi.org/{CONCEPT})
- [Zenodo record]({RECORD})
- [Canonical website page]({SITE})
- [English PDF](release/{PDF_NAME})
- [English Markdown](release/A_C_SHARED_OPEN_WORLD_EXPERIENCE_PAPER_v0_2_EN.md)
- [Editable DOCX](release/A_C_SHARED_OPEN_WORLD_EXPERIENCE_PAPER_v0_2_EN.docx)
- [Exact deposited public ZIP]({ZIP_NAME})
- [Post-publication citation](CITATION.cff) · [Machine metadata](PUBLICATION.json)
- [Original package checksums](release/SHA256SUMS.txt) · [Original license](release/LICENSE.md)

## Research question

A person and a long-lived candidate AI line may cooperate, compete by agreement, and return to cooperation across open game worlds. The paper separates shared-history utility, behavioral change and human enjoyment from correct handling of current permissions. It connects social-role and memory custody, historical versus operative state, and provenance/experience qualification without inventing another general architecture.

## Claim and evidence boundary

This is a conceptual and methodological proposal, not a working game integration or experimental result. The five author-constructed illustrations are explanatory, not an independently annotated benchmark. English v0.2 was prepared from the author-accepted Russian revision after adjudication of model reviews of v0.1; it has not undergone separate independent peer review. C designates a candidate implementation of requirements. No separate causal C/B1 comparison is planned until an actual treatment is specified. Ordinary baselines retain memory and safeguards. No proof of identity continuity, consciousness, a new AI class, or economic superiority is claimed.

## Published-byte preservation

`release/` reproduces all nine members of the deposited ZIP without changes. Its README and bibliography describe the pre-deposit package and intentionally remain historical. The new DOI is carried by this README, CITATION.cff and PUBLICATION.json, not silently inserted into the published paper, source or archive. Archive SHA-256: `{ZIP_HASH}`.

The package's original documentation is CC BY 4.0. This does not relicense the rest of this repository, cited works, software, game assets, private memories or individual runtime state. No internal review material is included.

## Related work and corpus route

- [AI Social Roles and Memory Custody](https://doi.org/10.5281/zenodo.21751985)
- [World 8 / Z0-A](https://doi.org/10.5281/zenodo.22085394), cited external prior art, not an author affiliation or endorsement
- [AGI corpus entry](../../README.md)
- [Corpus map](https://ivankotov.eu/corpus-map/) · [Temporal AI Presence](https://ivankotov.eu/temporal-ai-presence/)

Rolling back a simulator may restore a virtual crane position, but cannot restore an operator's revoked authorization. Correct interlocks, learned skill and a useful human experience remain separate evaluation targets.
'''
 exact_write(destination/'README.md', readme.encode())
 entry = f'\n- **Shared Open Worlds for Human–AI Dyads v0.2** — conceptual and methodological preprint, English, 6 September 2026. [Publication and exact files](publications/{SLUG}/README.md); [DOI](https://doi.org/{DOI}); CC BY 4.0 for this work only. No empirical game/c-specific result; current permissions, shared-history utility and human enjoyment are evaluated separately.\n'
 parent = root/'README.md'
 text = parent.read_text(encoding='utf-8')
 if DOI not in text:
  anchor = '## Canonical package entry points\n'
  if text.count(anchor) != 1:
   raise ValueError('Root README canonical-package anchor is ambiguous')
  parent.write_text(text.replace(anchor, anchor+entry, 1), encoding='utf-8')
 for name, (size, expected) in PINS.items():
  check((destination/'release'/name).read_bytes(), size, expected, name)
 receipt = {'status': 'PASS_EXACT_ACOW_MIRROR_BUILD', 'doi': DOI, 'archive_bytes': ZIP_BYTES, 'archive_sha256': ZIP_HASH, 'members_verified': 9, 'internal_checksum_rows': 8, 'observations': observations, 'source_changes': 0, 'model_calls': 0, 'game_runs': 0, 'independent_scientific_review': False}
 exact_write(destination/'MIRROR_RECEIPT.json', (json.dumps(receipt, indent=2)+'\n').encode())
 return receipt

def main() -> None:
 parser = argparse.ArgumentParser()
 parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
 parser.add_argument('--local-input', type=Path)
 args = parser.parse_args()
 if args.local_input:
  raw = (args.local_input/ZIP_NAME).read_bytes()
  pdf = (args.local_input/PDF_NAME).read_bytes()
  observations = [{'source': 'local supplied exact-byte fixture', 'remote_verification': False}]
 else:
  raw, zip_observation = fetch(ZIP_NAME, ZIP_BYTES, ZIP_HASH)
  pdf, pdf_observation = fetch(PDF_NAME, *PINS[PDF_NAME])
  observations = [zip_observation, pdf_observation]
 members = unpack(raw)
 check(pdf, *PINS[PDF_NAME], PDF_NAME)
 if pdf != members[PDF_NAME]:
  raise ValueError('Separately downloaded PDF differs from the ZIP member')
 print(json.dumps(mirror(args.root, raw, members, observations), indent=2))

if __name__ == '__main__':
 try:
  main()
 except (OSError, ValueError, KeyError, UnicodeError, zipfile.BadZipFile) as error:
  print('FAIL: ' + str(error), file=sys.stderr)
  raise SystemExit(2)
