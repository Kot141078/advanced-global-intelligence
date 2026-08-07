# Reproducibility and Integrity

## 1. Release boundary

The ZIP contains one top-level directory named
`pasc_foundation_gate_v0_1_1_recovery_5/`. Member paths are relative, UTF-8 encoded, and
sorted lexicographically. ZIP timestamps are fixed to 1980-01-01 00:00:00 and regular-file
permissions are fixed to 0644.

## 2. Manifest and checksum policy

`PASC_FOUNDATION_GATE_MANIFEST_v0_1_1_RECOVERY_5.json` lists every public package member
except itself and `SHA256SUMS.txt`. Each record binds path, role, media type, byte size, and
SHA-256.

`SHA256SUMS.txt` lists every regular package file except itself, including the manifest. This
avoids a checksum cycle while still binding the manifest.

The external file `PASC_FOUNDATION_GATE_v0_1_1_RECOVERY_5_EXTERNAL_SHA256SUMS.txt` is not
embedded in the ZIP. It binds the final ZIP and the two standalone publication PDFs.

## 3. Verification

From the extracted package root:

```bash
sha256sum -c SHA256SUMS.txt
python -m json.tool PASC_FOUNDATION_GATE_MANIFEST_v0_1_1_RECOVERY_5.json > /dev/null
python -m json.tool package/PASC_CANONICAL_BASELINE_INVENTORY_v0_1_1_RECOVERY_5.json > /dev/null
```

For the final ZIP:

```bash
unzip -t PASC_FOUNDATION_GATE_v0_1_1_RECOVERY_5.zip
sha256sum -c PASC_FOUNDATION_GATE_v0_1_1_RECOVERY_5_EXTERNAL_SHA256SUMS.txt
```

## 4. PDF relation

The primary PDF is generated from the eight Markdown research documents. The supplement is
generated from the canonical JSON inventory. Both PDFs are searchable and contain embedded
fonts. The standalone files uploaded beside the ZIP are byte-identical to their copies inside
the ZIP.
