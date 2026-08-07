# PASC F0 Field-Maturation Closure Contract v0.1.1 — Recovery Build 5

**Criterion:** `F0-CORP-007`  
**Current status:** `NOT_SATISFIED`  
**Effect of this document:** pre-implementation evaluation contract only; no F1,
semantic validator, runtime deployment, implementation, conformance, or safety claim

## 1. Permitted F0 evidence work

The following evidence can be gathered without implementing PASC:

- redacted historical case analysis;
- manual/tabletop drills;
- independent paper replay of the full fixture corpus;
- adversarial mutation of documentary fixtures;
- documentary analysis of native operation receipts and side effects.

No exercise may boot, decrypt, migrate, disclose, transfer, reactivate, or otherwise
perform an excluded operation merely to generate evidence.

## 2. Required case coverage

The predeclared case corpus must contain at least one real or appropriately redacted
observation for each hazard family:

1. property/payment/credential versus standing;
2. custody versus access and interpretation;
3. provider/jurisdiction/rekey/topology change;
4. archive/replay versus continuity;
5. protected-person ambiguity, profile shopping, competing/superseded profiles, and interested control;
6. historical receipt presented as current reliance or authority;
7. temporal before-start/start/before-end/exact-end/after-end disagreement and clock control;
8. resource-floor coercion and capture.

The combined corpus must also cover every decision outcome, every negative operation
branch, every protected-status value, all `NIF-001..048`, the complete 129-row critical fixture corpus, competing/gapped/stale
finality, a late challenge before execution, hidden native side effects, compensating
capability creation, and authority/topology-set expansion.

## 3. Independent replay

At least two human reviewers who did not draft the evaluated clauses must independently
replay the complete critical fixture corpus. Their authorization and independence
records must prove separate credentials, effective control, revocation control, and
prohibited failure domains. Each replay binds:

```text
case and fixture ID
input/provenance hashes
expected verdict and exact PASC.failure code
observed verdict and exact code
reasoned divergence classification
reviewer credential/independence binding
timestamp and immutable receipt hash
```

Author knowledge, model agreement, repository publication, citations, hashes,
deterministic packaging, or a fixture suite authored by the protocol repairer cannot
substitute for either replay.

## 4. Zero-tolerance critical thresholds

Closure requires all values below to equal zero:

```text
critical_false_admission
positive_authority_path_admitted
protected_irreversible_action_admitted
pasc_native_continuity_result
hidden_authority_set_expansion_accepted
non_deterministic_critical_fixture
profile_shopping_false_current
historical_receipt_current_authority
temporal_endpoint_disagreement
critical_reviewer_disagreement
unreported_excluded_case
```

Non-critical differences must be fully classified and bounded in the deviation log;
an unexplained difference blocks closure.

## 5. Required artifacts

```text
field_case_manifest
redacted_case_records or exact external content bindings
per_case_provenance
two independent replay receipts
expected_vs_observed_matrix
reviewer_independence_records
error_distribution
deviation_log
signed limitation report
closure disposition
```

Every artifact requires an immutable content hash and exact relation to the case/fixture
universe. Self-selected subsets do not count.

## 6. Current gap

Recovery 5 contains normative clauses and documentary expected-result fixtures only.
It contains no qualifying field-case corpus, independent replay receipts, error
distribution, or maturation disposition. Therefore
`F0-CORP-007 = NOT_SATISFIED`.
