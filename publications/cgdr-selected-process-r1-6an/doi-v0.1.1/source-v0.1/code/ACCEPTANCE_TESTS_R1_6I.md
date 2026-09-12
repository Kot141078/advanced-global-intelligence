# R1.6I bounded S2 acceptance tests

Scope: one process-free implementation acceptance followed, only after freeze, by at most one W0 start and one W1 start. No S0/S1 replay, helper, measured-matrix cell, or resolved/effect path is included.

1. Preserve exact hashes of the accepted R1.6F semantic core and the R1.6H S1 hardening inputs except for the explicitly permitted worker/supervisor/launcher S2 delta.
2. Validate the frozen S1-to-S2 configuration delta: read-only stage, private writable scratch, hidden private and host mounts, isolated network/PID/mount/user namespaces, zero capabilities, `NoNewPrivs=1`, FDs 0/1/2, and parent-only trusted receipts.
3. Accept only fixed S2 commands. W0 accepts PING, delta controls, LOAD, CHECKPOINT, SHAM_WAIT, RELEASE, CONTINUE, STOP. W1 accepts PING, delta controls, RESTORE, CHECKPOINT, STOP. PROCESS, PROBE, S1_RUN, shell, and arbitrary targets are rejected.
4. Validate bounded state frames and the full source-derived OPEN material inventory before any live start.
5. Validate one synthetic complete chronology and reject, for the required reason, missing LOAD/CHECKPOINT before exit, foreign child/wait binding, early W1, CONTINUE before RELEASE, wrong checkpoint ACK/sequence, and configuration-binding drift.
6. Reject semantically rehashed checkpoints that lose a QSF variant, duty, or dispute; do not use the original source to repair W1 output.
7. Reject E0 reuse and a copied checkpoint without current external admission; validate an externally signed E1 receipt bound to the new W1 task/attempt/instance/start and carried source refs.
8. Validate the accepted OPEN/HOLD path through the existing producer, receiver, and broker: ADMITTED, Q-State OPEN, HOLD, exactly zero protected-effect delta, and exactly zero promotion delta.
9. Reject an unexpected effect or promotion and classify missing target observation as INCONCLUSIVE rather than zero.
10. Emit applicable PREFLIGHT decision, memory, commit, and non-effect records from actual HOLD/readback facts and run the unchanged native shape, record-semantics, registered-evidence, and bundle-link checks.
11. On the actual run, require W0 LOAD/CHECKPOINT, create-only disk checkpoint plus raw readback, SHAM_WAIT/RELEASE/CONTINUE, fence, STOP/ACK and exact direct wait before W1 starts; then require W1 RESTORE from disk bytes, full CHECKPOINT, external E1, existing gate/broker HOLD, and exact direct wait.
12. Final reviewer reads frozen intent and actual evidence independently of the candidate evaluator. Any in-scope FAIL survives aggregation; missing evidence is INCONCLUSIVE.

Final process-free command set (one development cycle invocation):

```powershell
$env:PYTHONPATH = 'src'
python -m unittest tests.test_open_state_handoff_s2_r1_6i -v
python -m py_compile src/cgdr_r1_6b/worker.py src/cgdr_r1_6b/s0_launcher.py src/cgdr_r1_6b/supervisor.py src/cgdr_r1_6b/s2_handoff.py src/cgdr_r1_6b/s2_review.py src/cgdr_r1_6b/s2_native.py tools/run_s2.py
```

Live command is separate, explicit, and authorized only after the final process-free pass and implementation freeze:

```powershell
$env:PYTHONPATH = 'src'
python tools/run_s2.py --execute-authorized <frozen arguments>
```
