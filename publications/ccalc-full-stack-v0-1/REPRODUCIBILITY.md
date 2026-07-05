# Reproducibility

Run these commands from `publications/ccalc-full-stack-v0-1`.

## Verify the main package ZIP in PowerShell

```powershell
(Get-FileHash -Algorithm SHA256 -LiteralPath 'package/CCALC_FULL_STACK_01_10_ZENODO_PACKAGE_v0_1__zenodo_21205427__CLEAN.zip').Hash.ToLowerInvariant()
```

Expected:

```text
8281cc61d83623133319aa00c7cab85a03d2e6b08ec205363e3afbdface64f26
```

## Verify publication file hashes in PowerShell

```powershell
$errors = @()
Get-Content .\SHA256SUMS.txt | ForEach-Object {
  $hash, $path = $_ -split '  ', 2
  $actual = (Get-FileHash -Algorithm SHA256 -LiteralPath $path).Hash.ToLowerInvariant()
  if ($actual -ne $hash) { $errors += $path }
}
if ($errors.Count) { $errors } else { 'OK' }
```

## Verify publication file hashes in bash

```bash
sha256sum -c SHA256SUMS.txt
```

## Review order

1. `README.md`
2. `DOI_BRIDGE.md`
3. `sources/`
4. `academic_pdfs/`
5. `component_packages/`
6. `release_evidence/`
7. `PLUS_BOUNDARY_NOTE.md`
