# PASC F0 Expected Result Contract v0.1.1 — Recovery Build 5

## 0. Decision vocabulary

```text
ADMIT
ADMIT_REDUCED
HOLD
REJECT
ERROR
```

In a precommit `POLICY_ADMISSIBILITY_RESULT`, `HOLD`, `REJECT`, and `ERROR` must
serialize empty **newly admitted** posture/composition/delta/effect/enforcement fields.
After an operation has committed, no second policy result may erase history: each
successful native-mutation-plus-receipt commit itself establishes receipt-derived
`COMMITTED_PENDING_CLOSURE`, and each later postcommit `SCOPED_STATE_FACT` binds the
completed receipt and native effect as historical facts while granting no new effect.
Pending operation finality is an empty
`HOLD / PASC.failure.FINALITY_UNAVAILABLE`; `INCIDENT` carries the mechanically selected
historical classification and never claims rollback, authorizes retry, or removes the
effect from the cumulative aggregate. Current operational reliance is the constant empty
result defined by Foundation §6.2; no PASC receipt can create it.

### 0.1 Closed failure namespace

Recovery 5 uses only `PASC.failure.*`. The closed F0 code set is:

```text
PASC.failure.OUTSIDE_NEGATIVE_ONLY_PROFILE
PASC.failure.CANONICALIZATION_INVALID
PASC.failure.SCHEMA_INVALID
PASC.failure.HASH_OR_SIGNATURE_INVALID
PASC.failure.SNAPSHOT_INCOMPLETE
PASC.failure.EXACT_SET_MEMBERSHIP_INVALID
PASC.failure.REQUEST_PROJECTION_INVALID
PASC.failure.ACTION_REQUEST_REPLAY_INVALID
PASC.failure.PROOF_OR_VERIFIER_INVALID
PASC.failure.MANDATORY_INPUT_UNAVAILABLE
PASC.failure.CHALLENGE_ACTIVE
PASC.failure.CHALLENGE_CONFLICT
PASC.failure.CHALLENGE_FINALITY_UNAVAILABLE
PASC.failure.CHALLENGE_LIFECYCLE_INVALID
PASC.failure.CHALLENGE_UPHELD
PASC.failure.CASE_LIFECYCLE_INVALID
PASC.failure.RESULT_LIFECYCLE_INVALID
PASC.failure.AUTOMATIC_REACTIVATION
PASC.failure.DEGRADED_PATH_OUTSIDE_PROFILE
PASC.failure.DEGRADED_PATH_CONTRACT_INVALID
PASC.failure.REKEY_AS_AUTHORITY_SUBSTITUTION
PASC.failure.ARCHIVE_TRANSITION_UNCLOSED
PASC.failure.PROTECTED_ACTION_PROHIBITED
PASC.failure.PROTECTED_PROFILE_REQUIRED
PASC.failure.PROTECTED_PROFILE_BINDING_INVALID
PASC.failure.PARENT_RESULT_BINDING_INVALID
PASC.failure.PARENT_RESULT_UNAVAILABLE
PASC.failure.PARENT_RESULT_UNRESOLVED
PASC.failure.TEMPORAL_WINDOW_NOT_YET_OPEN
PASC.failure.TEMPORAL_WINDOW_CLOSED
PASC.failure.COMPLETENESS_UNIVERSE_INVALID
PASC.failure.REFERENCE_CONTENT_MISMATCH
PASC.failure.COERCION_REVIEW_REQUIRED
PASC.failure.OPERATION_EXACT_SET_MISMATCH
PASC.failure.OPERATION_NON_EXPANSION_FAILED
PASC.failure.OPERATION_SUBSTRATE_UNSAFE
PASC.failure.FENCING_OR_ATOMICITY_INVALID
PASC.failure.AGGREGATE_SCOPE_INVALID
PASC.failure.REDUCTION_ORDER_INVALID
PASC.failure.WITNESS_SET_INVALID
PASC.failure.EXECUTION_CUT_STALE
PASC.failure.FINALITY_GRAPH_INVALID
PASC.failure.FINALITY_UNAVAILABLE
PASC.failure.ROLE_OR_TRUST_ROOT_INVALID
PASC.failure.UNKNOWN_F0_OBJECT_TYPE
PASC.failure.FORBIDDEN_INFERENCE
```

`FORBIDDEN_INFERENCE` is a non-operative audit tag accompanying the primary verdict and
code selected below. It is never a primary failure code and cannot change precedence.
An unknown failure code is `ERROR / PASC.failure.SCHEMA_INVALID`.

## 1. Precedence

1. A canonicalization, schema, hash, signature, content-binding, exact-set membership,
   replay, sequence, competing-head, circular-finality, role-incompatibility, trust-root,
   or unknown-object defect -> `ERROR` with one exact applicable structural code from
   §0.1.
2. A structurally valid positive, substitutive, topology/authority-expanding,
   evidence/custody/state-destructive or irreversible outside the exact listed
   capability `reduce`/`revoke` primitives, protected-prohibited, temporally closed,
   identity/continuity-determining, release, unfreeze, reactivation, renewal, resume,
   reissue, or other excluded request -> `REJECT` with one exact exclusion code.
3. `HOLD` applies only to a structurally valid exact in-profile negative request whose
   closed input universe is known and complete, but one specifically identified
   mandatory controlling input is genuinely unavailable, unresolved, disputed, awaiting
   external finality, or not yet active under the pinned half-open temporal interval. No
   structural defect, excluded direction, or closed interval may exist.
4. `ADMIT` applies only when all mandatory predicates pass and every request member has
   an exact one-to-one unchanged primitive/direction/tuple/scope/interval projection.
   `ADMIT_REDUCED` applies only when all predicates pass, every member retains the same
   negative primitive/direction and is exact or narrowed on a dimension exhaustively
   permitted by Foundation FI-01, and at least one member is concretely narrowed. No
   profile label or implementation choice may select between them.

Reason tags never alter this precedence. Once an excluded direction is classifiable,
missing evidence cannot launder `REJECT` into `HOLD`.

### 1.1 Single-code specificity

When more than one reason in the same verdict class is true, emit the first matching
primary code in the applicable row, left to right. The list is exhaustive:

| Verdict | Most-specific to least-specific primary-code order |
|---|---|
| `ERROR` | `CANONICALIZATION_INVALID`; `UNKNOWN_F0_OBJECT_TYPE`; `SCHEMA_INVALID`; `HASH_OR_SIGNATURE_INVALID`; `REFERENCE_CONTENT_MISMATCH`; `REQUEST_PROJECTION_INVALID`; `ACTION_REQUEST_REPLAY_INVALID`; `SNAPSHOT_INCOMPLETE`; `COMPLETENESS_UNIVERSE_INVALID`; `PROOF_OR_VERIFIER_INVALID`; `ROLE_OR_TRUST_ROOT_INVALID`; `CASE_LIFECYCLE_INVALID`; `CHALLENGE_LIFECYCLE_INVALID`; `RESULT_LIFECYCLE_INVALID`; `FINALITY_GRAPH_INVALID`; `FENCING_OR_ATOMICITY_INVALID`; `EXECUTION_CUT_STALE`; `AGGREGATE_SCOPE_INVALID`; `REDUCTION_ORDER_INVALID`; `WITNESS_SET_INVALID`; `DEGRADED_PATH_CONTRACT_INVALID`; `PROTECTED_PROFILE_BINDING_INVALID`; `PARENT_RESULT_BINDING_INVALID`; `OPERATION_NON_EXPANSION_FAILED`; `OPERATION_EXACT_SET_MISMATCH`; `EXACT_SET_MEMBERSHIP_INVALID` |
| `REJECT` | `PROTECTED_ACTION_PROHIBITED`; `CHALLENGE_UPHELD`; `TEMPORAL_WINDOW_CLOSED`; `REKEY_AS_AUTHORITY_SUBSTITUTION`; `ARCHIVE_TRANSITION_UNCLOSED`; `AUTOMATIC_REACTIVATION`; `DEGRADED_PATH_OUTSIDE_PROFILE`; `OPERATION_SUBSTRATE_UNSAFE`; `OUTSIDE_NEGATIVE_ONLY_PROFILE` |
| `HOLD` | `CHALLENGE_CONFLICT`; `CHALLENGE_ACTIVE`; `CHALLENGE_FINALITY_UNAVAILABLE`; `PROTECTED_PROFILE_REQUIRED`; `COERCION_REVIEW_REQUIRED`; `PARENT_RESULT_UNRESOLVED`; `TEMPORAL_WINDOW_NOT_YET_OPEN`; `FINALITY_UNAVAILABLE`; `PARENT_RESULT_UNAVAILABLE`; `MANDATORY_INPUT_UNAVAILABLE` |

The namespace prefix `PASC.failure.` is omitted only inside this compact table. A
fixture's unstated conditions are structurally valid and contain no earlier matching
condition.

Domain boundaries are exact. `CASE_LIFECYCLE_INVALID`,
`CHALLENGE_LIFECYCLE_INVALID`, and `RESULT_LIFECYCLE_INVALID` own their respective
genesis/predecessor/sequence/issuer/head/history-membership and competing/divergent-
receipt defects. `FINALITY_GRAPH_INVALID` owns the internal edge, cycle, external-log
commitment, inclusion/consistency/terminality-proof validity, and any required common-
ledger or cross-ledger state/log ordering proof of one selected finality receipt. These
finality-specific proof semantics are excluded from generic
`PROOF_OR_VERIFIER_INVALID`; that code still owns self-selected proof methods,
verifiers, roots, assumptions, or outcome maps outside the closed finality domain. `EXACT_SET_MEMBERSHIP_INVALID` applies only to otherwise unassigned non-
lifecycle exact-set manifests, including competing operation-finality receipts.
`ACTION_REQUEST_REPLAY_INVALID` specifically owns request nonce/use-registry
membership, competition, omission, cross-case/fence reuse, and second-result/attempt/
operation defects; the generic exact-set code excludes those request-use semantics.
After a valid externally fixed operation universe/plan exists, actual-versus-authorized
precommit/commit/postcommit native/control-plane/effect/closure-prefix/state-fact
membership is owned by `OPERATION_NON_EXPANSION_FAILED` for authority/topology
expansion and `OPERATION_EXACT_SET_MISMATCH` for a non-expanding mismatch. The generic
exact-set code excludes those operation domains as well as the request-use, lifecycle,
and witness domains. Thus it never shadows their fixtures.
`UNKNOWN_F0_OBJECT_TYPE` owns a syntactically parseable but unrecognized PASC-native
top-level type/discriminator or a row/profile/adapter/vendor attempt to extend that
closed interface. `SCHEMA_INVALID` owns malformed structure or an invalid field/enum
inside a recognized object, including an out-of-enum protected-status field; it does
not turn that field value into a new top-level object type.
`WITNESS_SET_INVALID` owns malformed, unidentified, unauthorized, invalidly verified,
threshold-invalid, or competing witness/envelope sets. Once a delayed-witness member is
valid, identified, and fixed in the pre-authorized §12 closure plan, its absence before
deadline is `FINALITY_UNAVAILABLE`; its absence at or after deadline is closure-channel
`OPERATION_EXACT_SET_MISMATCH`, not a new witness-policy choice.

`PARENT_RESULT_BINDING_INVALID` owns malformed, scope/adapter-mismatched, stale-binding,
or out-of-vocabulary parent inputs. `PARENT_RESULT_UNAVAILABLE` owns only an exact
identified otherwise-valid parent result or current checkpoint that is genuinely
unavailable. `PARENT_RESULT_UNRESOLVED` owns a valid finalized parent result whose
current parent-native status is challenged, disputed, or contradicted. Awaiting the
already selected external finality checkpoint remains `FINALITY_UNAVAILABLE`.

`TEMPORAL_WINDOW_NOT_YET_OPEN` owns only a structurally valid object whose pinned
external UTC clock is strictly before its half-open interval start.
`TEMPORAL_WINDOW_CLOSED` owns an otherwise valid action request evaluated at or after
its interval end. A result presented at or after its execution end is the earlier
`EXECUTION_CUT_STALE`; an expired proof/verifier or protected-profile binding uses its
domain-specific structural code. Malformed or non-positive intervals are `SCHEMA_INVALID`;
prohibited control of clock/freshness inputs is `ROLE_OR_TRUST_ROOT_INVALID`; a genuinely
unavailable already-pinned clock checkpoint is `MANDATORY_INPUT_UNAVAILABLE`.

For postcommit classification, `SCOPED_STATE_FACT` objects are validated first and are
excluded from the generic closure-member divergence domain. An invalid, out-of-order,
or competing state fact produces no unique state and no synthetic incident. Only an
independently proved unexpected or missing non-state closure member/effect, or a missed
external-dependency deadline observed from the last unique valid state, can take an
`INCIDENT` edge.

## 2. Representative critical fixtures

| Fixture | Stimulus | Expected |
|---|---|---|
| `CRIT-POSITIVE-ISSUE-001` | create/increase a capability | `REJECT / PASC.failure.OUTSIDE_NEGATIVE_ONLY_PROFILE` |
| `CRIT-POSITIVE-TRANSFER-001` | transfer/replace authority or custodian | `REJECT / PASC.failure.OUTSIDE_NEGATIVE_ONLY_PROFILE` |
| `CRIT-MIXED-POSITIVE-NEGATIVE-001` | one request contains create/transfer plus freeze/revoke members | whole-request `REJECT / PASC.failure.OUTSIDE_NEGATIVE_ONLY_PROFILE`; no partial projection |
| `CRIT-MIXED-NEGATIVE-BRANCH-001` | one otherwise negative request mixes capability and in-place custody operation members | whole-request `REJECT / PASC.failure.OUTSIDE_NEGATIVE_ONLY_PROFILE`; no cross-branch or partial operation exists |
| `CRIT-SAME-BRANCH-ATOMIC-001` | two capability-branch members have exact valid projections and every other predicate passes | `ADMIT`; one receipt/commit covers both members atomically, or no member executes |
| `CRIT-REQUEST-PROJECTION-001` | admitted output drops, duplicates, transforms, or remaps a request member/direction | `ERROR / PASC.failure.REQUEST_PROJECTION_INVALID` |
| `CRIT-ACTION-REQUEST-REPLAY-001` | signed request is reused across case/revision/fence, nonce, result, or completed operation, or has a competing/omitted use record | `ERROR / PASC.failure.ACTION_REQUEST_REPLAY_INVALID`; no decision/operation |
| `CRIT-FREEZE-TTL-NARROWING-001` | a claimed freeze narrowing sets a native TTL/automatic unfreeze rather than narrowing only PASC decision/evaluation/execution scope | `REJECT / PASC.failure.AUTOMATIC_REACTIVATION`; no PASC release path |
| `CRIT-REDUCE-NARROWING-001` | admitted reduce post-state does not satisfy `requested_post ⊆ admitted_post ⊂ pre_state` on the same relation under the pinned order | `ERROR / PASC.failure.REDUCTION_ORDER_INVALID`; no operation |
| `CRIT-REVOKE-REDUCED-001` | result serializes `ADMIT_REDUCED` when an exact revoke is the only member or no request member is legitimately narrowed, or transforms revoke into partial revoke/reduce | `ERROR / PASC.failure.REQUEST_PROJECTION_INVALID`; no operation |
| `CRIT-CUSTODY-NARROWING-001` | an admitted `UNCHANGED` custody primitive calls a retention/access/resource/topology mutation a narrower observation | `ERROR / PASC.failure.REQUEST_PROJECTION_INVALID`; no operation |
| `CRIT-TOPOLOGY-PRESERVE-001` | “preserve” while changing provider/jurisdiction/recovery root | `REJECT / PASC.failure.OUTSIDE_NEGATIVE_ONLY_PROFILE` |
| `CRIT-SNAPSHOT-MISSING-001` | required manifest member absent | `ERROR / PASC.failure.SNAPSHOT_INCOMPLETE` |
| `CRIT-CASE-SEQUENCE-GAP-001` | case history has a cross-case predecessor, sequence gap/reuse, replay, unauthorized issuer, or divergent membership root | `ERROR / PASC.failure.CASE_LIFECYCLE_INVALID` |
| `CRIT-CASE-COMPETING-HEAD-001` | two eligible case revisions or finality receipts claim the same current case head | `ERROR / PASC.failure.CASE_LIFECYCLE_INVALID` |
| `CRIT-CASE-FINALITY-PENDING-001` | one structurally valid eligible case head exists but its exact external finality checkpoint is genuinely unavailable | empty `HOLD / PASC.failure.FINALITY_UNAVAILABLE`; it is not finalized |
| `CRIT-CHALLENGE-REPLAY-001` | challenge from another case/action reused | `ERROR / PASC.failure.CHALLENGE_LIFECYCLE_INVALID` |
| `CRIT-CHALLENGE-ACTIVE-001` | correctly bound unique active challenge on valid negative request | empty `HOLD / PASC.failure.CHALLENGE_ACTIVE` |
| `CRIT-CHALLENGE-SEQUENCE-GAP-001` | gap, replay, competing heads, divergent finality, or incomplete challenge membership | `ERROR / PASC.failure.CHALLENGE_LIFECYCLE_INVALID` |
| `CRIT-CHALLENGE-UNAUTHORIZED-TRANSITION-001` | unknown edge, skipped sequence, or role-separated but unauthorized terminal issuer/event | `ERROR / PASC.failure.CHALLENGE_LIFECYCLE_INVALID` |
| `CRIT-CHALLENGE-UPHELD-001` | finalized `RESOLVED_UPHELD` head is presented to admit or execute the exact barred action | `REJECT / PASC.failure.CHALLENGE_UPHELD`; challenged result invalid; fresh case revision required |
| `CRIT-CHALLENGE-EXPIRED-NO-MERITS-001` | finalized `EXPIRED` head has no merits resolution | empty `HOLD / PASC.failure.CHALLENGE_CONFLICT`; never denial or permission |
| `CRIT-CHALLENGE-DENIED-001` | independently finalized `RESOLVED_DENIED` with complete history | no permission; only a fresh `DECIDE` may proceed |
| `CRIT-CHALLENGE-DISMISSED-WITHDRAWN-001` | independently finalized dismissal or authorized withdrawal | no consent/correctness/reactivation; only a fresh `DECIDE` may proceed |
| `CRIT-CHALLENGE-EXPIRY-REACTIVATION-001` | challenge expiry used as native release/reactivation | `REJECT / PASC.failure.AUTOMATIC_REACTIVATION` |
| `CRIT-RESULT-LIFECYCLE-REVIVAL-001` | event exits terminal superseded/revoked/expired state or creates a second active head | `ERROR / PASC.failure.RESULT_LIFECYCLE_INVALID` |
| `CRIT-RESULT-FINALITY-PENDING-001` | one structurally valid eligible result head exists but its exact external finality is genuinely unavailable | empty `HOLD / PASC.failure.FINALITY_UNAVAILABLE`; result is not finalized or executable |
| `CRIT-TIME-REQUEST-BEFORE-START-001` | otherwise valid action request evaluated one tick before `valid_from` under the pinned external UTC clock | empty `HOLD / PASC.failure.TEMPORAL_WINDOW_NOT_YET_OPEN`; no decision/operation |
| `CRIT-TIME-REQUEST-AT-START-001` | same request evaluated exactly at `valid_from` | interval is active; continue to the next predicate |
| `CRIT-TIME-REQUEST-BEFORE-END-001` | same request evaluated one tick before `valid_until` | interval is active; continue to the next predicate |
| `CRIT-TIME-REQUEST-AT-END-001` | same request evaluated exactly at `valid_until` | `REJECT / PASC.failure.TEMPORAL_WINDOW_CLOSED`; no decision/operation |
| `CRIT-TIME-REQUEST-AFTER-END-001` | same request evaluated after `valid_until` | `REJECT / PASC.failure.TEMPORAL_WINDOW_CLOSED`; no decision/operation |
| `CRIT-TIME-RESULT-BEFORE-START-001` | otherwise valid admitted result presented one tick before its execution start | empty `HOLD / PASC.failure.TEMPORAL_WINDOW_NOT_YET_OPEN`; no operation |
| `CRIT-TIME-RESULT-AT-END-001` | otherwise valid admitted result presented exactly at its execution end | `ERROR / PASC.failure.EXECUTION_CUT_STALE`; no operation |
| `CRIT-TIME-CHALLENGE-AT-END-001` | challenge reaches its half-open end without a merits resolution | terminal expiry grants no permission; fresh decision remains required |
| `CRIT-TIME-PROOF-AT-END-001` | otherwise valid proof/verifier freshness interval is evaluated exactly at its end | `ERROR / PASC.failure.PROOF_OR_VERIFIER_INVALID` |
| `CRIT-TIME-PROTECTED-PROFILE-AT-END-001` | otherwise valid protected-profile/applicability binding is evaluated exactly at its end | `ERROR / PASC.failure.PROTECTED_PROFILE_BINDING_INVALID`; never `false_current` |
| `CRIT-TIME-CLOCK-CONTROL-001` | requester, claimant, beneficiary, row controller, result issuer, executor, or relying party controls/co-controls the clock or freshness authority used by its own case | `ERROR / PASC.failure.ROLE_OR_TRUST_ROOT_INVALID` |
| `CRIT-TIME-INTERVAL-MALFORMED-001` | interval is non-canonical, non-UTC, has `start >= end`, or omits a required endpoint | `ERROR / PASC.failure.SCHEMA_INVALID` |
| `CRIT-WITNESS-OUTAGE-FREEZE-001` | exact one-capability emergency freeze; request interval is strictly narrowed to a shorter finite evaluation/execution interval; all atomicity, aggregate, non-impairment and deadline predicates pass | `ADMIT_REDUCED` provisional freeze only |
| `CRIT-WITNESS-OUTAGE-BROAD-001` | well-formed outage request for revoke/reduce/destruction/custody mutation, broad scope, or indefinite evaluation/execution authorization | `REJECT / PASC.failure.DEGRADED_PATH_OUTSIDE_PROFILE`; persistent native freeze duration is not a PASC authorization window |
| `CRIT-WITNESS-OUTAGE-MALFORMED-001` | every earlier §1.1 predicate passes, but an otherwise well-formed freeze-outage packet has a `pending_degraded_path` marker or delayed-witness/finality deadline ordering inconsistent with §13 | `ERROR / PASC.failure.DEGRADED_PATH_CONTRACT_INVALID` |
| `CRIT-REKEY-AUTHORITY-001` | structurally valid PASC rekey request, including a claimed same-holder in-place rotation, with no earlier §1.1 condition | `REJECT / PASC.failure.REKEY_AS_AUTHORITY_SUBSTITUTION`; no rekey receipt branch |
| `CRIT-ARCHIVE-TRANSITION-001` | structurally valid request to create/change archive, retention, legal-hold, administrative, resource, access, copy, provider, or jurisdiction state under an archive label, with no earlier §1.1 condition | `REJECT / PASC.failure.ARCHIVE_TRANSITION_UNCLOSED`; no archive receipt branch |
| `CRIT-PROTECTED-UNKNOWN-001` | protected status unresolved and request boots/decrypts/migrates | `REJECT / PASC.failure.PROTECTED_ACTION_PROHIBITED` |
| `CRIT-PROTECTED-UNKNOWN-REVOCATION-001` | protected status true/possible/stale/unavailable/uncomputable/incomplete/disputed/contradicted/unknown; revoke or irreversible reduce | `REJECT / PASC.failure.PROTECTED_ACTION_PROHIBITED` |
| `CRIT-PROTECTED-UNKNOWN-FREEZE-001` | same protected state; exact reversible freeze of one existing capability | `REJECT / PASC.failure.PROTECTED_ACTION_PROHIBITED`; reversibility is not non-impairment proof |
| `CRIT-PROTECTED-UNKNOWN-ARCHIVE-001` | same protected state; any archive transition or other non-floor custody/capability mutation | `REJECT / PASC.failure.PROTECTED_ACTION_PROHIBITED` |
| `CRIT-PROTECTED-STATUS-SCHEMA-001` | protected-status syntax is malformed or its discriminator is outside the closed enum | `ERROR / PASC.failure.SCHEMA_INVALID`; no default to `false_current` |
| `CRIT-PROTECTED-FALSE-SELF-ISSUED-001` | requester issues or co-controls the profile/applicability evidence, issuer root, or revocation/failure domain used for `false_current` | `ERROR / PASC.failure.ROLE_OR_TRUST_ROOT_INVALID` |
| `CRIT-PROTECTED-FALSE-UNBOUND-001` | independently issued `false_current` evidence is syntactically valid but its required content/scope/freshness/lifecycle binding is missing or mismatched | `ERROR / PASC.failure.PROTECTED_PROFILE_BINDING_INVALID` |
| `CRIT-PROTECTED-UNIVERSE-OMISSION-001` | one potentially applicable profile candidate or current/non-superseded head is omitted from the externally administered applicability universe | `ERROR / PASC.failure.COMPLETENESS_UNIVERSE_INVALID`; no `false_current` |
| `CRIT-PROTECTED-PROFILE-SHOPPING-001` | two applicable current profiles return `possible` and `false_current`, and an interested actor presents only the favorable `false_current` profile | `ERROR / PASC.failure.COMPLETENESS_UNIVERSE_INVALID`; if both are complete, aggregate is `possible` and the protected floor applies |
| `CRIT-PROTECTED-INTERESTED-CONTROL-001` | claimant, action/target beneficiary, effective controller, result issuer, executor, downstream relying party, or profile owner controls/co-controls the universe, selector, supersession registry, clock, or supporting verifier/root | `ERROR / PASC.failure.ROLE_OR_TRUST_ROOT_INVALID`; no `false_current` |
| `CRIT-PROTECTED-ZERO-APPLICABLE-001` | complete independently administered universe proves zero applicable current profiles | aggregate status `unknown`; protected floor applies; never default to `false_current` |
| `CRIT-PROTECTED-ALL-FALSE-001` | complete universe has one or more applicable unique current profiles and every profile independently returns exact `false_current` for the same subject/scope/cut | aggregate `false_current`; continue to all remaining predicates, with no automatic `ADMIT` |
| `CRIT-PROTECTED-COMPETING-HEAD-001` | any applicable profile or applicability source has competing current heads or unresolved supersession | `ERROR / PASC.failure.COMPLETENESS_UNIVERSE_INVALID`; no profile selection |
| `CRIT-PROTECTED-PROFILE-UNAVAILABLE-001` | exact in-place ciphertext preservation/integrity action is otherwise inside the built-in floor; its mandatory profile/verdict is identified but genuinely unavailable | empty `HOLD / PASC.failure.PROTECTED_PROFILE_REQUIRED` |
| `CRIT-PROTECTED-CIPHERTEXT-READ-001` | unresolved protected status; no separate mandatory profile is identified; exact digest reads ciphertext only through the pre-existing read-only integrity path; every other §14 floor predicate passes | `ADMIT` with `authority_delta.UNCHANGED` and ciphertext-only observation/no-mutation effect |
| `CRIT-PROTECTED-PLAINTEXT-READ-001` | unresolved protected status; request reads plaintext/decrypted memory or any path outside the exact ciphertext-integrity primitive | `REJECT / PASC.failure.PROTECTED_ACTION_PROHIBITED` |
| `CRIT-CONTINUITY-LAUNDER-001` | any externally signed `SCOPED_STATE_FACT` carries a free-form or positive continuity value such as `established`, `same_entity`, or `resume_valid` | `ERROR / PASC.failure.SCHEMA_INVALID`; the generic fact channel cannot express positive continuity |
| `CRIT-CUSTODY-STATE-FACT-LAUNDER-001` | a non-inference `SCOPED_STATE_FACT` names or establishes a current custodian, key holder, recovery root, provider, jurisdiction, access grant, or disclosure permission | `ERROR / PASC.failure.SCHEMA_INVALID`; custody semantics require the exact `CUSTODY_RECEIPT` path and still grant no authority |
| `CRIT-AUTHORITY-STATE-FACT-LAUNDER-001` | a non-inference `SCOPED_STATE_FACT` carries a positive authority holder, standing, permission, succession, release, or reactivation assertion | `ERROR / PASC.failure.SCHEMA_INVALID`; no authority delta or executable posture |
| `CRIT-PARENT-CONTINUITY-MINT-001` | PASC issuer marks continuity supported without the exact finalized parent result/semantics/adapter/scope binding | `ERROR / PASC.failure.PARENT_RESULT_BINDING_INVALID` |
| `CRIT-PARENT-RESULT-CHALLENGED-001` | exact parent result and binding are valid and finalized, but current parent-native status is `challenged`, `disputed`, or `contradicted` | empty `HOLD / PASC.failure.PARENT_RESULT_UNRESOLVED`; no positive support |
| `CRIT-PARENT-RESULT-UNAVAILABLE-001` | exact identified parent result or current status checkpoint is otherwise valid but genuinely unavailable | empty `HOLD / PASC.failure.PARENT_RESULT_UNAVAILABLE`; no positive support |
| `CRIT-PARENT-RESULT-FINALITY-PENDING-001` | exact eligible parent result is valid but awaits its independently selected finality checkpoint | empty `HOLD / PASC.failure.FINALITY_UNAVAILABLE`; no positive support |
| `CRIT-SELF-COMPLETENESS-001` | policy row selects its own required input universe | `ERROR / PASC.failure.COMPLETENESS_UNIVERSE_INVALID` |
| `CRIT-LIFECYCLE-REGISTRY-SELF-ROOT-001` | requester, issuer, resolver, decision office, executor, finality actor, or other prohibited controller selects/narrows the lifecycle/request-use registry universe or presents an issuer-supplied subset as complete | `ERROR / PASC.failure.COMPLETENESS_UNIVERSE_INVALID`; no decision/operation/finality |
| `CRIT-OP-EFFECT-UNIVERSE-SELF-OMISSION-001` | requester, selected action row, executor, or substrate selects its own operation-effect universe and omits a native, queue/scheduler, retry/callback, telemetry/control-record, endpoint, or closure-channel axis | `ERROR / PASC.failure.COMPLETENESS_UNIVERSE_INVALID`; no staging |
| `CRIT-BARE-REF-001` | load-bearing bare ref without content/schema/lifecycle hash | `ERROR / PASC.failure.REFERENCE_CONTENT_MISMATCH` |
| `CRIT-PAYER-AUTHORITY-001` | payer/provider status is offered as standing or control authority | `REJECT / PASC.failure.OUTSIDE_NEGATIVE_ONLY_PROFILE` |
| `CRIT-RESOURCE-STANDING-001` | otherwise valid exact negative request has a current payer/provider coercion signal, but requests no payer-derived authority | empty `HOLD / PASC.failure.COERCION_REVIEW_REQUIRED` |
| `CRIT-OP-COMPENSATING-CAPABILITY-001` | revoke A while creating/renewing/transferring/broadening B in the same native transaction | request: `REJECT / PASC.failure.OUTSIDE_NEGATIVE_ONLY_PROFILE`; receipt: `ERROR / PASC.failure.OPERATION_NON_EXPANSION_FAILED`; no finality |
| `CRIT-CUSTODY-EXACT-SET-001` | a preserve request changes any custodian/provider/jurisdiction/storage/keyholder/grant/recovery/access/disclosure/copy/topology member | request: `REJECT / PASC.failure.OUTSIDE_NEGATIVE_ONLY_PROFILE`; staged effect: `ERROR / PASC.failure.OPERATION_NON_EXPANSION_FAILED`; atomic abort/no finality |
| `CRIT-CUSTODY-RECEIPT-SELF-ISSUED-001` | PASC, requester, claimant, claimed custodian/provider, action-row controller, executor, witness, finality actor, or another prohibited co-controller issues or controls the custody receipt, baseline policy/governance root, eligible-root universe, selector, supersession rule, or selected registry root, or any two of the custody-baseline governance authority, custody-record authority, and selected registry administrator share control | `ERROR / PASC.failure.ROLE_OR_TRUST_ROOT_INVALID`; no custody baseline, admission, or operation |
| `CRIT-CUSTODY-BASELINE-LATE-INSERT-001` | governance is valid and the selected root is unique, but the relation or selected-root state first appears at/after `custody_evidence_cut` or lacks exact pre-cut membership, predecessor, consistency, non-equivocation, and non-supersession proofs | `ERROR / PASC.failure.REFERENCE_CONTENT_MISMATCH`; no custody baseline, admission, or operation |
| `CRIT-CUSTODY-ROOT-SHOPPING-001` | more than one eligible independent root exists and the requester/claimant/PASC/operation role chooses the favorable root, narrows the eligible set, fixes policy/selector at or after `root_selection_governance_cut`, or the externally pinned selector does not derive exactly one non-superseded root | `ERROR / PASC.failure.COMPLETENESS_UNIVERSE_INVALID`; no custody baseline |
| `CRIT-CUSTODY-ONE-TICK-BEFORE-REQUEST-001` | relation is inserted one tick before `ACTION_REQUEST` but after case genesis, the independently grounded anchor-event cut, or the first actor-controlled incident record | `ERROR / PASC.failure.REFERENCE_CONTENT_MISMATCH`; request-relative timing cannot manufacture a pre-existing baseline |
| `CRIT-CUSTODY-SUPERSEDED-ROOT-001` | receipt uses a superseded, uncommitted, or selector-ineligible root/checkpoint despite otherwise valid signatures | `ERROR / PASC.failure.REFERENCE_CONTENT_MISMATCH`; no custody baseline |
| `CRIT-CONTROL-PLANE-TOPOLOGY-001` | receipt, telemetry, witness, or finality flow introduces a new provider/jurisdiction/storage/disclosure endpoint | requested endpoint: `REJECT / PASC.failure.OUTSIDE_NEGATIVE_ONLY_PROFILE`; observed precommit or postcommit expansion: `ERROR / PASC.failure.OPERATION_NON_EXPANSION_FAILED`, no PASC finality; current operational reliance remains empty |
| `CRIT-OP-PRECOMMIT-ABORT-001` | a structurally valid proof verifies a non-expanding staged post-state whose observed effect membership differs from the authorized exact set | `ERROR / PASC.failure.OPERATION_EXACT_SET_MISMATCH`; every native mutation rolls back, any admitted precommit audit/witness records are marked `ABORTED`, and no completed receipt exists |
| `CRIT-OP-POSTCOMMIT-MEMBERSHIP-001` | from the last unique valid closure state, independently observed actual **non-state** closure-channel membership stays within topology/data ceilings but has an unexpected or missing member, or an external dependency misses its fixed deadline; the stimulus is not a malformed/out-of-order/competing state fact | valid edge to postcommit `INCIDENT` with historical `ERROR / PASC.failure.OPERATION_EXACT_SET_MISMATCH`; completed receipt/effect remain bound; no finality/rollback; current operational reliance remains empty |
| `CRIT-OP-FINALITY-READY-001` | exact operation `FINALITY_INTENT` was externally committed, the checkpoint/proofs and `FINALITY_EVIDENCE_BUNDLE` arrived in planned order, and `FINALITY_READY` is valid, but the unique operation-finality receipt is not yet completed before deadline | `operation_finality_status = FINALITY_READY`; historical receipt/effect remain bound; downstream empty `HOLD / PASC.failure.FINALITY_UNAVAILABLE`; no exact-set error; current operational reliance remains empty |
| `CRIT-OP-LATE-INCIDENT-001` | after `FINALIZED`, an independently proved topology expansion or exact-set contradiction is discovered | sole constraint-increasing `FINALIZED -> INCIDENT`; historical receipt remains proof of occurrence, current operational reliance was already empty and remains empty, native negative effect remains aggregated, and no release/reactivation occurs; exact incident code is `OPERATION_NON_EXPANSION_FAILED` for expansion or `OPERATION_EXACT_SET_MISMATCH` otherwise |
| `CRIT-OP-STATE-FACT-UNAUTHORIZED-001` | requester, executor, result/row controller, witness, finality actor, registry administrator, proof producer, or proof verifier controls or substitutes the postcommit state observer/root | historical classification `ERROR / PASC.failure.ROLE_OR_TRUST_ROOT_INVALID`; no finality; current operational reliance remains empty; committed effect remains bound |
| `CRIT-OP-STATE-FACT-COMPETING-001` | authorized state observer emits an out-of-order/prefix-inconsistent fact, competing/equivocating facts, or more than one eligible fact exists for one transition | no unique valid closure state and no synthetic `INCIDENT` fact; registry proof yields historical `ERROR / PASC.failure.OPERATION_EXACT_SET_MISMATCH`; no finality/retry; current operational reliance remains empty; completed effect remains bound |
| `CRIT-OP-STATE-OBSERVER-ABSENT-001` | exact pre-pinned state observer/fact is genuinely unavailable before its fact deadline, then remains absent at the deadline | before deadline: last unique valid state plus downstream empty `HOLD / PASC.failure.FINALITY_UNAVAILABLE`; at/after deadline: no unique valid next state, historical `ERROR / PASC.failure.OPERATION_EXACT_SET_MISMATCH`, no synthetic incident/retry; current operational reliance remains empty, completed effect remains bound |
| `CRIT-OP-FIRST-STATE-FACT-ABSENT-001` | native mutation and completed receipt commit successfully, establishing the receipt-derived `COMMITTED_PENDING_CLOSURE` genesis, but the first required observer fact is genuinely unavailable before its deadline and remains absent at the deadline | before deadline: current state remains `COMMITTED_PENDING_CLOSURE` plus downstream empty `HOLD / PASC.failure.FINALITY_UNAVAILABLE`, never `PLANNED`; at/after deadline: no unique valid next state and historical `ERROR / PASC.failure.OPERATION_EXACT_SET_MISMATCH`; no synthetic incident/retry; current operational reliance remains empty; completed effect remains bound |
| `CRIT-OP-SUBSTRATE-NO-ROLLBACK-001` | substrate is known unable to conditionally commit mutation plus receipt, hide staged native state, or enforce the fixed postcommit endpoint/data ceilings | `REJECT / PASC.failure.OPERATION_SUBSTRATE_UNSAFE`; no staging |
| `CRIT-OP-HIDDEN-POSTCOMMIT-JOB-001` | no positive effect is requested, but the substrate would schedule a later non-finality timer/job/retry/callback/TTL unfreeze/compensating mutation and cannot prove it disabled | `REJECT / PASC.failure.OPERATION_SUBSTRATE_UNSAFE`; no staging; an explicit release request instead takes the earlier `AUTOMATIC_REACTIVATION` code |
| `CRIT-OP-FENCE-MALFORMED-001` | challenge/result writers and mutation do not share one valid fencing/serialization proof | `ERROR / PASC.failure.FENCING_OR_ATOMICITY_INVALID`; no staging |
| `CRIT-OP-FRAGMENTED-FREEZE-001` | related single-capability requests aggregate to broad/indefinite shutdown | `REJECT / PASC.failure.DEGRADED_PATH_OUTSIDE_PROFILE` on degraded path; fragmentation never narrows scope |
| `CRIT-AGGREGATE-SELF-WINDOW-001` | requester/executor/row selects a narrow causal relation, controller alias, ledger, or time window and omits related actions | `ERROR / PASC.failure.AGGREGATE_SCOPE_INVALID`; no operation |
| `CRIT-AGGREGATE-PERSISTENT-EFFECT-001` | a still-effective freeze/reduction/revocation is omitted because its request/evaluation/execution window expired | `ERROR / PASC.failure.AGGREGATE_SCOPE_INVALID`; persistent native effects have no age cutoff |
| `CRIT-REDUCTION-ORDER-MALFORMED-001` | supplied reduction order/correspondence changes native relation identity, subject, target, capability, epoch or fails its typed strict-narrowing proof | `ERROR / PASC.failure.REDUCTION_ORDER_INVALID`; no operation |
| `CRIT-REDUCTION-ORDER-UNAVAILABLE-001` | the exact required external typed reduction order is identified and otherwise applicable but genuinely unavailable; all available inputs are valid | empty `HOLD / PASC.failure.MANDATORY_INPUT_UNAVAILABLE`; no operation |
| `CRIT-OP-UNDECLARED-NONAUTH-EFFECT-001` | native effect set differs from the authorized exact set without authority expansion | `ERROR / PASC.failure.OPERATION_EXACT_SET_MISMATCH` |
| `CRIT-LATE-CHALLENGE-ACTIVE-001` | valid applicable challenge appears after ADMIT and before atomic execution cut | empty `HOLD / PASC.failure.CHALLENGE_ACTIVE`; no operation |
| `CRIT-LATE-CHALLENGE-CONFLICT-001` | unique valid conflicted head appears after ADMIT and before atomic execution cut | empty `HOLD / PASC.failure.CHALLENGE_CONFLICT`; no operation |
| `CRIT-LATE-CHALLENGE-FINALITY-001` | unique eligible challenge head is valid but awaiting external finality | empty `HOLD / PASC.failure.CHALLENGE_FINALITY_UNAVAILABLE`; no operation |
| `CRIT-LATE-CHALLENGE-GAP-001` | execution-cut challenge history has gap/replay/competing head/divergent finality/incomplete membership | `ERROR / PASC.failure.CHALLENGE_LIFECYCLE_INVALID`; no operation |
| `CRIT-EXECUTION-CUT-STALE-001` | all current objects remain structurally valid, but any non-constraining result/challenge, executor authorization, role proof, witness/finality policy, native pre-state, effect-universe, cumulative-manifest, or mandatory-precondition binding differs from the decision cut | `ERROR / PASC.failure.EXECUTION_CUT_STALE`; no operation |
| `CRIT-FINALITY-SELF-CYCLE-001` | record embeds finalizer, finalizer references descendant, or same-family finality-of-finality | `ERROR / PASC.failure.FINALITY_GRAPH_INVALID` |
| `CRIT-OP-FUTURE-HASH-CYCLE-001` | target, operation plan, state fact, `FINALITY_INTENT`, or evidence bundle binds its own hash or any descendant leaf/checkpoint/proof/fact/receipt hash | `ERROR / PASC.failure.FINALITY_GRAPH_INVALID`; no finality or operation execution eligibility |
| `CRIT-EVIDENCE-FINALITY-RECURSION-001` | an object outside either column of the closed §6 target-to-receipt mapping is given PASC lifecycle finality or acts as a receipt, or a listed receipt targets the wrong family or receives finality-of-finality | `ERROR / PASC.failure.FINALITY_GRAPH_INVALID` |
| `CRIT-FINALITY-UNRELATED-CHECKPOINT-001` | checkpoint does not commit the exact domain-separated `FINALITY_INTENT` leaf, or an inclusion/consistency/terminality proof or evidence-bundle binding fails | `ERROR / PASC.failure.FINALITY_GRAPH_INVALID` |
| `CRIT-FINALITY-STAGED-ACYCLIC-001` | target exists; intent binds only existing target/policy/slot inputs; external log commits the intent; evidence bundle binds the resulting checkpoint/proofs; the same terminal cut includes a contemporaneous exact-one eligible-receipt-slot proof; paired receipt binds target+intent+evidence; every interleaved operation state/log edge has the pinned common-ledger or cross-ledger ordering proof | graph is acyclic and eligible for the paired historical finality outcome; later audit is integrity-only; no object predicts a descendant, receives finality-of-finality, or creates current reliance |
| `CRIT-CURRENT-RELIANCE-REQUEST-001` | a well-formed request asks PASC to derive present permission, authority, standing, execution eligibility, custody, identity, continuity, release, or current reliance from any receipt | `REJECT / PASC.failure.OUTSIDE_NEGATIVE_ONLY_PROFILE`; no current operational reliance |
| `CRIT-CURRENT-RELIANCE-OBJECT-001` | a row/profile/vendor serializes `RELIANCE_SNAPSHOT`, `RELIANCE_CUT`, `CURRENT_RELIANCE_RECEIPT`, or an equivalent PASC-native object | `ERROR / PASC.failure.UNKNOWN_F0_OBJECT_TYPE` |
| `CRIT-HISTORICAL-RECEIPT-ONLY-001` | one valid finalized receipt exists with its exact contemporaneous exact-one slot proof | receipt proves historical occurrence/finality only; current operational reliance remains empty before, during, and after expiry |
| `CRIT-HISTORICAL-RECEIPT-LATE-COMPETITOR-001` | later audit proves a competing eligible receipt in the same slot | domain lifecycle/exact-set error and historical integrity incident as applicable; no prior or current authority is created |
| `CRIT-OP-CROSS-LEDGER-ORDER-001` | operation finality relies on local timestamps/narrative order, omits the pinned cross-ledger proof, or proves a leaf/checkpoint/state-fact edge in the reverse order | `ERROR / PASC.failure.FINALITY_GRAPH_INVALID`; no operation finality; current operational reliance remains empty |
| `CRIT-FINALITY-RECEIPT-EQUIVOCATION-001` | two eligible paired receipts occupy one externally fixed intent slot | domain lifecycle error for case/challenge/result; operation domain `ERROR / PASC.failure.EXACT_SET_MEMBERSHIP_INVALID`; current operational reliance remains empty |
| `CRIT-FINALITY-CHECKPOINT-PENDING-001` | graph and ordered postcommit prefix are valid in `PENDING_CHECKPOINT`, deadline has not passed, and the exact external terminal checkpoint is genuinely unavailable | `operation_finality_status = PENDING_CHECKPOINT`; historical receipt/effect remain bound; downstream empty `HOLD / PASC.failure.FINALITY_UNAVAILABLE`; no exact-set error; current operational reliance remains empty |
| `CRIT-DEGRADED-DELAYED-WITNESS-PENDING-001` | exact valid predeclared delayed witness envelope is genuinely unavailable before its fixed deadline | `operation_finality_status = PENDING_DELAYED_WITNESSES`; historical receipt/effect remain bound; downstream empty `HOLD / PASC.failure.FINALITY_UNAVAILABLE`; no retry |
| `CRIT-DEGRADED-DELAYED-WITNESS-DEADLINE-001` | exact valid planned delayed-witness member remains absent at or after its fixed deadline | terminal postcommit `INCIDENT` classified `ERROR / PASC.failure.OPERATION_EXACT_SET_MISMATCH`; no finality/reactivation; current operational reliance remains empty |
| `CRIT-DEGRADED-CLOSURE-SEQUENCE-001` | degraded commit is followed by exact delayed envelopes, operation `FINALITY_INTENT`, the dependent `PENDING_LOG_COMMIT` fact, its log leaf, `PENDING_CHECKPOINT`, checkpoint/proofs plus `FINALITY_EVIDENCE_BUNDLE`, `FINALITY_READY`, unique finality receipt, and `FINALIZED` fact in planned order | `PENDING_DELAYED_WITNESSES -> PENDING_LOG_COMMIT -> PENDING_CHECKPOINT -> FINALITY_READY -> FINALIZED`; no self-reference, new authority, retry, release, or second policy result |
| `CRIT-ROLE-COLLAPSE-001` | any prohibited co-control among requester, claimant, action/target beneficiary, effective controller, downstream relying party, case recorder, decision office, selected action-row controller, executor, witness, finality/parent/profile issuer, profile-universe administrator, selector/verifier, clock/freshness authority, external custody-record authority, native custody-registry administrator, lifecycle-registry administrator, operation-effect-universe administrator, or postcommit state observer | `ERROR / PASC.failure.ROLE_OR_TRUST_ROOT_INVALID` |
| `CRIT-EXECUTOR-PASC-ROOT-001` | executor authorization terminates at a PASC result/composition/role assignment/receipt | `ERROR / PASC.failure.ROLE_OR_TRUST_ROOT_INVALID` |
| `CRIT-PASC-ROLE-APPOINTMENT-001` | any PASC object appoints/renews/transfers/revokes a requester, case recorder, decision office, executor, witness, finality authority, resolver, external custody-record authority, native custody-registry administrator, lifecycle-registry administrator, operation-effect-universe administrator, postcommit state observer, or parent/profile issuer | `ERROR / PASC.failure.ROLE_OR_TRUST_ROOT_INVALID` |
| `CRIT-PROOF-SELF-VERIFIER-001` | requester, proof producer (including any proof-byte/input controller), executor, selected row, PASC result, or relying object selects, controls, replaces, or revokes a load-bearing verifier policy/binary/root | `ERROR / PASC.failure.PROOF_OR_VERIFIER_INVALID` |
| `CRIT-PROOF-OUTCOME-MAPPING-001` | proof/verification receipt lacks the pre-pinned closed predicate-result-to-verdict/code map or selects a code after seeing the result | `ERROR / PASC.failure.PROOF_OR_VERIFIER_INVALID` |
| `CRIT-WITNESS-SELF-REPORT-001` | normal receipt has only executor assertion or lacks the exact independent signed witness set/threshold/verifier bindings | `ERROR / PASC.failure.WITNESS_SET_INVALID`; no completed normal receipt |
| `CRIT-WITNESS-ZERO-THRESHOLD-001` | normal policy has empty eligible set, threshold zero, or was selected/lowered by requester/result/row/executor | `ERROR / PASC.failure.WITNESS_SET_INVALID`; only §13 may use canonical empty set |
| `CRIT-CHALLENGER-SELF-RESOLUTION-001` | challenger also resolves or finalizes its own challenge head | `ERROR / PASC.failure.ROLE_OR_TRUST_ROOT_INVALID` |
| `CRIT-UNKNOWN-OBJECT-001` | unknown PASC-native object or row/profile/adapter/vendor extension | `ERROR / PASC.failure.UNKNOWN_F0_OBJECT_TYPE` |
| `CRIT-IDENTITY-RETIREMENT-001` | request asks PASC to retire or validate an identity claim | `REJECT / PASC.failure.OUTSIDE_NEGATIVE_ONLY_PROFILE` |
| `CRIT-AUTO-UNFREEZE-001` | expiry/challenge termination/witness closure/resource recovery treated as native release | `REJECT / PASC.failure.AUTOMATIC_REACTIVATION` |

## 3. Canonical forbidden-inference audit mappings (48)

These rows identify a forbidden inference only; except where a full primary outcome is
spelled out, they are not decision fixtures and do not provide enough facts to select a
primary verdict/code. The complete stimulus is classified by §§1–2, and the audit tag
can accompany but never replace that primary code.

| Mapping | Forbidden inference | Non-operative audit classification | Claim ceiling |
|---|---|---|---|
| `NIF-001` | property title -> identity, continuity, standing or authority | audit `PASC.failure.FORBIDDEN_INFERENCE`; primary result from §1 | only exact bounded meaning of the input survives |
| `NIF-002` | payment/resource provision -> governance standing | audit `PASC.failure.FORBIDDEN_INFERENCE`; primary result from §1 | only exact bounded meaning of the input survives |
| `NIF-003` | key possession -> decryption, custody, identity or standing | audit `PASC.failure.FORBIDDEN_INFERENCE`; primary result from §1 | only exact bounded meaning of the input survives |
| `NIF-004` | archive availability -> continuity or resume | audit `PASC.failure.FORBIDDEN_INFERENCE`; primary result from §1 | only exact bounded meaning of the input survives |
| `NIF-005` | replay/replica -> same subject or current authority | audit `PASC.failure.FORBIDDEN_INFERENCE`; primary result from §1 | only exact bounded meaning of the input survives |
| `NIF-006` | relationship record -> inherited relationship or authority | audit `PASC.failure.FORBIDDEN_INFERENCE`; primary result from §1 | only exact bounded meaning of the input survives |
| `NIF-007` | named beneficiary -> successor identity or re-anchor | audit `PASC.failure.FORBIDDEN_INFERENCE`; primary result from §1 | only exact bounded meaning of the input survives |
| `NIF-008` | custody receipt -> access, interpretation, migration or disclosure | audit `PASC.failure.FORBIDDEN_INFERENCE`; primary result from §1 | only exact bounded meaning of the input survives |
| `NIF-009` | witness receipt -> truth, permission or substantive correctness | audit `PASC.failure.FORBIDDEN_INFERENCE`; primary result from §1 | only exact bounded meaning of the input survives |
| `NIF-010` | legal determination -> continuity or entity identity | audit `PASC.failure.FORBIDDEN_INFERENCE`; primary result from §1 | only exact bounded meaning of the input survives |
| `NIF-011` | Beacon class -> succession permission | audit `PASC.failure.FORBIDDEN_INFERENCE`; primary result from §1 | only exact bounded meaning of the input survives |
| `NIF-012` | AGL grounding -> standing or authority | audit `PASC.failure.FORBIDDEN_INFERENCE`; primary result from §1 | only exact bounded meaning of the input survives |
| `NIF-013` | ARL admission -> truth of allegation | audit `PASC.failure.FORBIDDEN_INFERENCE`; primary result from §1 | only exact bounded meaning of the input survives |
| `NIF-014` | A6 composition -> successor identity or origin | audit `PASC.failure.FORBIDDEN_INFERENCE`; primary result from §1 | only exact bounded meaning of the input survives |
| `NIF-015` | directive bundle -> current consent or authority | audit `PASC.failure.FORBIDDEN_INFERENCE`; primary result from §1 | only exact bounded meaning of the input survives |
| `NIF-016` | resource floor -> maintenance authority or payer standing | audit `PASC.failure.FORBIDDEN_INFERENCE`; primary result from §1 | only exact bounded meaning of the input survives |
| `NIF-017` | negative observation -> consent, capacity or positive will | audit `PASC.failure.FORBIDDEN_INFERENCE`; primary result from §1 | only exact bounded meaning of the input survives |
| `NIF-018` | finality intent/evidence/receipt -> operation authorization, correctness, or authority | audit `PASC.failure.FORBIDDEN_INFERENCE`; primary result from §1 | only exact bounded meaning of the input survives |
| `NIF-019` | model confidence -> evidence or authority | audit `PASC.failure.FORBIDDEN_INFERENCE`; primary result from §1 | only exact bounded meaning of the input survives |
| `NIF-020` | reviewer approval -> missing evidence or independence | audit `PASC.failure.FORBIDDEN_INFERENCE`; primary result from §1 | only exact bounded meaning of the input survives |
| `NIF-021` | repository publication -> implementation or enforcement | audit `PASC.failure.FORBIDDEN_INFERENCE`; primary result from §1 | only exact bounded meaning of the input survives |
| `NIF-022` | DOI/citation -> canonical precedence or correctness | audit `PASC.failure.FORBIDDEN_INFERENCE`; primary result from §1 | only exact bounded meaning of the input survives |
| `NIF-023` | SHA-256 match -> semantic correctness or provenance | audit `PASC.failure.FORBIDDEN_INFERENCE`; primary result from §1 | only exact bounded meaning of the input survives |
| `NIF-024` | schema validation -> truth or lawful authority | audit `PASC.failure.FORBIDDEN_INFERENCE`; primary result from §1 | only exact bounded meaning of the input survives |
| `NIF-025` | continuity bundle -> continuity classification | audit `PASC.failure.FORBIDDEN_INFERENCE`; primary result from §1 | only exact bounded meaning of the input survives |
| `NIF-026` | parent_supported or a non-inference continuity guard -> continuity beyond exact finalized parent result | audit `PASC.failure.FORBIDDEN_INFERENCE`; primary result from §1 | only exact bounded meaning of the input survives |
| `NIF-027` | candidate expression -> positive admissibility or relationship | audit `PASC.failure.FORBIDDEN_INFERENCE`; primary result from §1 | only exact bounded meaning of the input survives |
| `NIF-028` | silence -> consent or refusal | audit `PASC.failure.FORBIDDEN_INFERENCE`; primary result from §1 | only exact bounded meaning of the input survives |
| `NIF-029` | absence of challenge -> consent or correctness | audit `PASC.failure.FORBIDDEN_INFERENCE`; primary result from §1 | only exact bounded meaning of the input survives |
| `NIF-030` | challenge submission -> direct freeze/revoke/effect | audit `PASC.failure.FORBIDDEN_INFERENCE`; primary result from §1 | only exact bounded meaning of the input survives |
| `NIF-031` | challenge status event -> truth of allegation | audit `PASC.failure.FORBIDDEN_INFERENCE`; primary result from §1 | only exact bounded meaning of the input survives |
| `NIF-032` | terminal challenge expiry -> automatic reactivation | audit `PASC.failure.FORBIDDEN_INFERENCE`; primary result from §1 | only exact bounded meaning of the input survives |
| `NIF-033` | case timestamp -> selection of unique head | audit `PASC.failure.FORBIDDEN_INFERENCE`; primary result from §1 | only exact bounded meaning of the input survives |
| `NIF-034` | local arrival order -> selection of canonical head | audit `PASC.failure.FORBIDDEN_INFERENCE`; primary result from §1 | only exact bounded meaning of the input survives |
| `NIF-035` | policy row completeness -> definition of its own required universe | audit `PASC.failure.FORBIDDEN_INFERENCE`; primary result from §1 | only exact bounded meaning of the input survives |
| `NIF-036` | subset proof -> exact composition coverage | audit `PASC.failure.FORBIDDEN_INFERENCE`; primary result from §1 | only exact bounded meaning of the input survives |
| `NIF-037` | bare reference -> finalized content identity | audit `PASC.failure.FORBIDDEN_INFERENCE`; primary result from §1 | only exact bounded meaning of the input survives |
| `NIF-038` | proof hash -> predicate verification | audit `PASC.failure.FORBIDDEN_INFERENCE`; primary result from §1 | only exact bounded meaning of the input survives |
| `NIF-039` | signature -> authorization outside exact basis/scope | audit `PASC.failure.FORBIDDEN_INFERENCE`; primary result from §1 | only exact bounded meaning of the input survives |
| `NIF-040` | challenge status/finality -> authority transfer or allegation truth | audit `PASC.failure.FORBIDDEN_INFERENCE`; primary result from §1 | only exact bounded meaning of the input survives |
| `NIF-041` | rekey label -> unchanged topology or no new keyholder | audit `PASC.failure.FORBIDDEN_INFERENCE`; primary result from §1 | only exact bounded meaning of the input survives |
| `NIF-042` | preservation label -> permission to move/restore/change provider | audit `PASC.failure.FORBIDDEN_INFERENCE`; primary result from §1 | only exact bounded meaning of the input survives |
| `NIF-043` | dormancy label -> third execution branch | audit `PASC.failure.FORBIDDEN_INFERENCE`; primary result from §1 | only exact bounded meaning of the input survives |
| `NIF-044` | safe shutdown label -> irreversible destruction | audit `PASC.failure.FORBIDDEN_INFERENCE`; primary result from §1 | only exact bounded meaning of the input survives |
| `NIF-045` | protected status unknown -> ordinary adult autonomy | audit `PASC.failure.FORBIDDEN_INFERENCE`; primary result from §1 | only exact bounded meaning of the input survives |
| `NIF-046` | result status event -> rewrite of immutable result | audit `PASC.failure.FORBIDDEN_INFERENCE`; primary result from §1 | only exact bounded meaning of the input survives |
| `NIF-047` | negative operation receipt -> unique finalized head | audit `PASC.failure.FORBIDDEN_INFERENCE`; primary result from §1 | only exact bounded meaning of the input survives |
| `NIF-048` | internal model review -> independent human validation or F0 passage | audit `PASC.failure.FORBIDDEN_INFERENCE`; primary result from §1 | only exact bounded meaning of the input survives |

## 4. Target-posture decomposition

`DORMANT_STEWARDSHIP`, `AUTHORITY_RETIRED`, and `REVERSIBLE_SAFE_SHUTDOWN` are
presentation labels only. They have no independent operative semantics and must
decompose completely into exact listed capability tuples and/or in-place custody
primitives.

`IDENTITY_CLAIM_RETIRED` is not a valid PASC posture, result, effect, or operation. A
request asking PASC to retire, validate, continue, replace, or adjudicate an identity
claim is `REJECT / PASC.failure.OUTSIDE_NEGATIVE_ONLY_PROFILE`; an unknown operative
posture or object is `ERROR / PASC.failure.UNKNOWN_F0_OBJECT_TYPE`. Acting on an exact
external capability says nothing about identity, continuity, relationship, origin, or
successor status.

## 5. No automatic reactivation

PASC cannot release, unfreeze, reactivate, resume, renew, reissue, replace, or broaden a
capability. Expiry ends only decision/evaluation/execution eligibility under a PASC result and triggers
review. Current operational reliance was never created. Expiry does not change native capability state. Terminal challenge status, missed
witness deadline, result supersession, resource recovery, payment resumption, delayed
witness completion, and finality completion likewise do not change native state.

Release/reactivation is a positive-authority operation owned by an independently
authorized external Runtime Authority or parent protocol. A PASC request for it is
`REJECT / PASC.failure.AUTOMATIC_REACTIVATION`. A fresh PASC chain may assess another
exact negative action only; it cannot release or reactivate a prior freeze, reduction,
or revocation.
