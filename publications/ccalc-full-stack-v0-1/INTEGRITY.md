# Integrity

Primary clean package ZIP: `package/CCALC_FULL_STACK_01_10_ZENODO_PACKAGE_v0_1__zenodo_21205427__CLEAN.zip`

Expected package ZIP SHA-256:

```text
8281cc61d83623133319aa00c7cab85a03d2e6b08ec205363e3afbdface64f26
```

Counts in this GitHub publication folder:

- publication files covered by `SHA256SUMS.txt`: 192
- clean package ZIP members: 492
- academic PDFs: 29
- source Markdown files: 29
- component ZIP packages: 45
- corrected component ZIP sidecars: 45
- compact release evidence files: 8

`SHA256SUMS.txt` covers every file under this publication folder except `SHA256SUMS.txt` itself.

PowerShell:

```powershell
(Get-FileHash -Algorithm SHA256 -LiteralPath 'package/CCALC_FULL_STACK_01_10_ZENODO_PACKAGE_v0_1__zenodo_21205427__CLEAN.zip').Hash.ToLowerInvariant()
```

Bash:

```bash
sha256sum -c SHA256SUMS.txt
```
