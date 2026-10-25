#!/usr/bin/env python3
"""Verify the frozen CI academic package using only Python's standard library.

Copyright 2026 Ivan Kotov. All rights reserved. No license grant.
This verifies byte integrity, not the truth of scientific or identity claims.
"""
from __future__ import annotations
import hashlib
import json
import re
import stat
import sys
import zipfile
from pathlib import Path, PurePosixPath

ORIGINAL_BYTES=50765
ORIGINAL_SHA256='be87dd926ed96e91e8de25bae2e18666f74ac738b173379ddc0092f98563f663'
MANIFEST='PACKAGE_MANIFEST.json'
INDEX='SHA256SUMS.txt'

def digest(path: Path) -> str:
    h=hashlib.sha256()
    with path.open('rb') as f:
        for block in iter(lambda:f.read(1024*1024),b''):
            h.update(block)
    return h.hexdigest()

def safe_relative(name: str) -> PurePosixPath:
    p=PurePosixPath(name)
    if not name or p.is_absolute() or '..' in p.parts or '\\' in name or str(p)!=name:
        raise ValueError('Unsafe or non-canonical member path: '+repr(name))
    return p

def verify(root: Path) -> dict:
    manifest=json.loads((root/MANIFEST).read_text(encoding='utf-8'))
    if manifest.get('schema')!='CI_ACADEMIC_PACKAGE_MANIFEST_V1':
        raise ValueError('Unsupported outer manifest schema')
    if manifest.get('edition')!='academic-pdf-2' or manifest.get('source_version')!='1.0.0':
        raise ValueError('Unexpected edition/source identity')
    listed={}
    for item in manifest['files']:
        name=item['path'];safe_relative(name)
        if name in listed or name in [MANIFEST,INDEX]:
            raise ValueError('Duplicate or self-included manifest path: '+name)
        listed[name]=item
    actual=set()
    for p in root.rglob('*'):
        if p.is_symlink():raise ValueError('Symlink found: '+str(p))
        if p.is_file():actual.add(p.relative_to(root).as_posix())
    expected=set(listed)|{MANIFEST,INDEX}
    if actual!=expected:
        raise ValueError('File set mismatch: missing='+repr(sorted(expected-actual))+'; extra='+repr(sorted(actual-expected)))
    for name,item in listed.items():
        p=root/name
        if p.stat().st_size!=item['bytes'] or digest(p)!=item['sha256']:
            raise ValueError('Manifest size/digest mismatch: '+name)
    checksum_rows={}
    for line in (root/INDEX).read_text(encoding='utf-8').splitlines():
        m=re.fullmatch(r'([0-9a-f]{64})  (.+)',line)
        if not m:raise ValueError('Malformed checksum row')
        h,name=m.groups();safe_relative(name)
        if name in checksum_rows:raise ValueError('Duplicate checksum row: '+name)
        checksum_rows[name]=h
    if set(checksum_rows)!=expected-{INDEX}:
        raise ValueError('Checksum index file set mismatch')
    for name,h in checksum_rows.items():
        if digest(root/name)!=h:raise ValueError('Checksum mismatch: '+name)
    original=root/'source_original'/'CI_CONTINUITY_INSTRUMENT_V1_0_0.zip'
    if original.stat().st_size!=ORIGINAL_BYTES or digest(original)!=ORIGINAL_SHA256:
        raise ValueError('Original _02 ZIP identity mismatch')
    with zipfile.ZipFile(original) as z:
        infos=z.infolist();names=[i.filename for i in infos]
        if len(names)!=22 or len(set(names))!=22:
            raise ValueError('Original ZIP member count/uniqueness mismatch')
        for info in infos:
            safe_relative(info.filename)
            if stat.S_ISLNK(info.external_attr>>16):
                raise ValueError('Original ZIP contains a symlink')
            if not info.filename.startswith('Continuity_Instrument_v1.0.0/'):
                raise ValueError('Unexpected original ZIP prefix')
            raw=z.read(info)
            target=root/'source_original'/info.filename
            if target.read_bytes()!=raw:
                raise ValueError('Extracted source differs from original ZIP: '+info.filename)
        if z.testzip() is not None:raise ValueError('Original ZIP CRC mismatch')
    return {'status':'PACKAGE_INTEGRITY_VERIFIED','payload_files':len(listed),
            'checksum_rows':len(checksum_rows),'original_source_members':22,
            'original_source_sha256':ORIGINAL_SHA256,'scientific_qualification':'NOT_ESTABLISHED',
            'claim':'byte consistency only; not an authentication or truth attestation'}

def main() -> int:
    root=Path(__file__).resolve().parent.parent
    try:
        result=verify(root)
    except (OSError,ValueError,KeyError,TypeError,zipfile.BadZipFile) as exc:
        print('PACKAGE_VERIFICATION_FAILED: '+str(exc),file=sys.stderr)
        return 2
    print(json.dumps(result,ensure_ascii=False,indent=2))
    return 0

if __name__=='__main__':
    raise SystemExit(main())
