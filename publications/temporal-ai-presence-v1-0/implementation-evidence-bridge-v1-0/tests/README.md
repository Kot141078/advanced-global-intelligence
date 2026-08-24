# Offline Test Surface

`run_offline_validation.py` is the decisive test runner. Original focused tests are retained byte-identically under `reference_snapshot/original_tests/`; their path-dependent pytest mechanics are not executed from this package. The runner preserves their validator assertions and adds the explicit R3E-A-R1 negative cases in `fixtures/bridge_required_negative_cases.json`.
