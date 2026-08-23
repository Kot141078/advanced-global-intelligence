# TAP R2B Core Evidence Manifest Policy

## Core evidence

Core evidence is the stable minimum needed to inspect or reproduce the R2B claim: the main report, branch ancestry, discovery inventories, route-authority map, discovery delta, custody receipts, validation logs, pre/post equivalence record, test receipts, bundle verification, and the verified Git bundle.

The core manifest includes stable `.md`, `.txt`, `.csv`, `.json`, `.jsonl`, `.patch`, and `.bundle` artifacts outside excluded transient directories. The core manifest excludes itself and the full-custody manifest to avoid recursive hashing.

## Forensic-only custody

Full forensic custody covers every regular file under the R2B evidence root except the full-custody manifest itself. It therefore includes external pytest temporary state, routed bytecode, and external runtime-sandbox output. These files preserve execution context but are not promoted to claim evidence.

## Exclusions from core evidence

The following are excluded from core evidence: `tmp/`, `pycache/`, `__pycache__/`, `.pytest_cache/`, `runtime_sandbox/`, `.pyc`, `.pyo`, machine scratch, and transient runtime state that has not been explicitly reduced to a receipt.

Exclusion does not weaken reproducibility because the deterministic commands, collected counts, exit codes, stable receipts, exact source commit, bundle, inventories, and byte-equivalence result remain in core evidence. Full custody retains hashes for the excluded execution material.
