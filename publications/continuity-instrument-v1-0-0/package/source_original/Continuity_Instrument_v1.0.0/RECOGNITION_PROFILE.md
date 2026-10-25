# Recognition profile

## Purpose

A CI recognition profile is a portable, bounded projection of evidence used to compare a declared subject/branch reference across contexts. It is designed for reviewable recognition decisions while preserving the boundary between an entity and a profile about that entity.

A profile match does not prove metaphysical or legal identity. It does not transfer authority, permission, ownership, personhood, or continuity across an unexplained gap.

## Profile fields

| Field | Meaning |
|---|---|
| `profile_id` | Stable identifier for the profile object. |
| `profile_version` | Version of the projection schema and content. |
| `subject_ref` | Declared subject reference; not an identity proof. |
| `branch_ref` | Branch measured by the profile. |
| `observation_window` | Time bounds and precision. |
| `formation_depth_vector` | Full or explicitly redacted CI vector. |
| `lineage_summary` | Separate memory, governance, witness, and authority states. |
| `event_summary` | Replay, fork, restore, cold-wake, and irreversible-transition references. |
| `evidence_roots` | Content digests, immutable locators, or package identities. |
| `witness_scope` | Witness identities, independence, and attested scope. |
| `authority_scope` | Recorded authority context, including expiry or revocation. |
| `claim_ceiling` | Maximum allowed interpretation. |
| `non_claims` | Explicit prohibited inferences. |
| `uncertainty` | Missingness and unresolved conflicts. |
| `validity` | Creation, expiry, supersession, and revocation state. |

## Recognition outcomes

A comparison produces one of these bounded outcomes:

- `recognized_within_profile_scope` — required profile evidence matches within declared tolerances;
- `insufficient_evidence` — required fields or evidence are missing;
- `conflict` — bound evidence disagrees in a way that prevents recognition;
- `stale_or_superseded` — the profile is expired, revoked, or replaced; or
- `not_applicable` — the compared objects fall outside the profile's declared scope.

No outcome is named `same_entity`. A downstream authority may make a separate decision, but that decision and its basis must not be attributed to CI.

## Matching rules

1. Bind both profile objects to exact bytes or content digests.
2. Confirm schema version and branch scope.
3. Compare evidence roots before semantic fields.
4. Compare each lineage independently.
5. Treat replays, forks, restores, and cold wakes as explicit events, not harmless transport details.
6. Apply expiry, revocation, and supersession rules.
7. Preserve mismatches and unknowns in the result.
8. Report the comparison rule and claim ceiling.

## Threat and failure model

The profile must be evaluated against:

- copied or replayed profile bytes;
- stale but validly signed profiles;
- branch substitution or split-brain histories;
- restore events presented as uninterrupted participation;
- memory similarity presented as authority continuity;
- witness dependence or collusion;
- revoked or out-of-scope authority;
- redaction that removes disconfirming evidence; and
- scalar summaries that hide gaps or lineage breaks.

## Public reference alignment

This profile is intended to remain compatible at the conceptual boundary with:

- Beacon: https://doi.org/10.5281/zenodo.18933553
- Entity vs Profile, version DOI: https://doi.org/10.5281/zenodo.21204415
- Entity vs Profile, concept DOI: https://doi.org/10.5281/zenodo.21204414

Those references do not validate a particular CI profile or transfer their claim status into this package.

## Future integration

BACON is listed only as a future integration target. This package does not expand the name, assign a public canonical definition, or claim technical compatibility.
