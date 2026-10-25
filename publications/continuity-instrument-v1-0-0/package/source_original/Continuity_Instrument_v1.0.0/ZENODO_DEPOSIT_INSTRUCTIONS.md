# Direct Zenodo deposit instructions

Upload the exact frozen `CI_CONTINUITY_INSTRUMENT_V1_0_0.zip`. Do not extract, edit, normalize, or rebuild it during deposit.

## Core metadata

- Resource type: `Software`
- Title: `Continuity Instrument (CI): Evidence-Bound Measurement of Governed Continuity in Long-Lived AI Systems, v1.0`
- Version: `1.0.0`
- Creator: `Ivan Kotov`
- ORCID: `0009-0009-6002-9845`
- Access: `Open`

Use `.zenodo.json` for the description, keywords, and related identifiers. Keep the stated claim ceiling: R157 is open-synthetic evidence; R160 and R161 are consumed negative attempts; empirical qualification is not established.

## Rights: enter two separate entries

1. Select `Creative Commons Attribution 4.0 International (CC BY 4.0)` and state its scope as: `scientific text and metadata`.
2. Add a custom rights entry with this exact text:

   `Copyright © 2026 Ivan Kotov. All rights reserved. No license grant.`

   State its scope as: `REFERENCE_IMPLEMENTATION/, its schemas, and tests/test_ci_profile.py`.

The second entry preserves copyright and grants no permission beyond access to the deposited bytes. Do not describe the code as CC BY, MIT, Apache, open source, or public domain.

## DOI and byte custody

1. Reserve or assign the DOI in Zenodo.
2. Publish the same frozen ZIP without rebuilding it.
3. Download the published file through Zenodo.
4. Verify its byte length and SHA-256 against the local frozen ZIP.
5. Record the version DOI, concept DOI, public URL, deposited byte length, and SHA-256.

Do not include private corpus bytes, Qubit source text, R157/R160/R161 private archives, model files, or runtime binaries in the deposit.
