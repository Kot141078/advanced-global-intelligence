# Offline-only reproduction for R1.6K

These commands create only new task-local SQLite calibration databases. They do
not start a worker, helper, WSL, S0/S1/S2, endpoint, or measured matrix.

```powershell
$env:PYTHONPATH = "$PWD\src"
python -m py_compile src\cgdr_r1_6b\prospective_observation.py src\cgdr_r1_6b\s2_handoff.py src\cgdr_r1_6b\s2_native.py src\cgdr_r1_6b\native_adapter.py tools\run_s2.py tools\run_observation_calibration.py tests\test_prospective_observation_r1_6k.py
python -m unittest -v tests.test_prospective_observation_r1_6k
python tools\run_observation_calibration.py --output .\calibration-output-new
```

The output path is create-only. `tools/run_s2.py` contains the future integration
seam but its `main` is outside this task's authorization and is not invoked here.
