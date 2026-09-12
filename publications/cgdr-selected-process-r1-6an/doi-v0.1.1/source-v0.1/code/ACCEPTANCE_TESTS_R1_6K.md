# R1.6K acceptance tests fixed before implementation

1. Database, trigger capture, independent baseline, scope/config/clock binding,
   and `OBSERVATION_READY` precede a fake first-start callback; missing baseline,
   wrong target, or logger error prevents callback invocation.
2. A fresh local HOLD has empty independent before/after snapshots, a complete
   committed-change capture, and four-layer native acceptance in that local scope.
3. Committed INSERT/UPDATE/DELETE, SQLite REPLACE, UPSERT, and promotion changes
   are detected even when both final protected tables are empty.
4. A rolled-back DML attempt is retained as an attempt but not misclassified as
   a committed protected change.
5. The existing Broker can commit one exact allowed operation and its change is
   observed, proving the collector is not a blanket-deny mechanism.
6. Lost/altered event, missing END/snapshot, disabled capture, target substitution,
   overflow/flush failure, and unknown writer fail closed for the required reason.
7. UTC jump/correlation loss, snapshot-time substitution, and window extension
   beyond capture do not produce a strong witness.
8. OPEN closes before a later RESOLVED effect while the common collector remains
   active through the fake owned-exit boundary.
9. Top-level review retains in-scope FAIL/UNKNOWN; intent is frozen independently
   of actual SQL; foreign identifiers and record hashes are rejected.
10. Guards prove no worker/helper/WSL/S2/matrix run and preserve accepted semantic,
    security, historical R1.6I, and corrective R1.6J bytes.
