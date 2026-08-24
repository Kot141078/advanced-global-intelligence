# Requirement-to-Code Map

This map binds the four pending public implementation tests to inspectable public paths. The current public status remains unchanged until R3E-B.

## TAP-T02

| Requirement | Mechanism | Public path | Validator / fixtures |
|---|---|---|---|
| Persistent memory must be classified. | Declared T-M classes | `declarations/TAP_MEMORY_CLASSES.json` | `validate_t02`; t02-unclassified-memory |
| Each persistent store has policy and review routes. | Per-store policy envelope | `reference_snapshot/source/modules/memory/facade.py` | `validate_t02`; t02-missing-review-route |
| Memory class references must be declared. | Closed T-M0 through T-M9 taxonomy | `src/tap_conformance/validators/core.py` | `validate_t02`; t02-undeclared-memory-class-reference |
| Raw memory requires governed policy. | Fail-closed required fields | `run_offline_validation.py` | `negative`; t02-raw-memory-without-policy |
| Memory read/write boundaries are inspectable. | Selected facade, store, and I/O source | `reference_snapshot/source/modules/memory/io.py` | `read/write source`; t02-four-store-source-bindings |

Current: `PUBLIC_CANDIDATE_NEEDS_IMMUTABLE_PUBLICATION`. Maximum after exact R3E-B publication: `ELIGIBLE_FOR_PUBLIC_VERIFIED_AFTER_R3E_B`.

## TAP-T06

| Requirement | Mechanism | Public path | Validator / fixtures |
|---|---|---|---|
| Cloud calls must be classified. | AST discovery over complete selected source closure | `src/tap_conformance/bindings/r2b.py` | `discover_t06_call_sites`; t06-r2a-179, t06-r2b-177 |
| Lexical false positives must be explicit. | Old/new discovery set difference | `reference_snapshot/source/modules/ester/net_will_adapter.py` | `discover_cloud_call_sites`; t06-two-false-positives |
| Every discovered route has a semantic class. | Seven route classes and fail-closed inventory | `reference_snapshot/T06_DISCOVERY_RESULT.json` | `validate_t06_inventory`; t06-seven-route-classes, t06-synthetic-unresolved-row |
| Semantic cloud-AI routes have complete authority maps. | Three-route authority map | `reference_snapshot/source/modules/llm/providers_openai_oracle.py` | `discover_t06_route_authority_map`; t06-authority-3-of-3, t06-synthetic-incomplete-authority |
| Unauthorized cloud routes fail before network. | Broker and chat API denial branches | `reference_snapshot/source/modules/llm/broker.py` | `cloud_ai_requires_oracle_route`; t06-static-deny-mechanisms |
| Private memory and continuity are not silently exported. | Cloud declaration validation | `declarations/TAP_CLOUD_CALL_LOG.json` | `validate_t06`; t06-private-without-approval, t06-silent-continuity-export |
| Validation performs no live network call. | Process-level socket denial | `run_offline_validation.py` | `deny_network`; combined-boundary |

Current: `PUBLIC_CANDIDATE_NEEDS_IMMUTABLE_PUBLICATION`. Maximum after exact R3E-B publication: `ELIGIBLE_FOR_PUBLIC_VERIFIED_AFTER_R3E_B`.

## TAP-T07

| Requirement | Mechanism | Public path | Validator / fixtures |
|---|---|---|---|
| Agents and executor-like surfaces must be inventoried. | AST surface discovery | `src/tap_conformance/bindings/r2b.py` | `discover_t07_agent_surfaces`; t07-fourteen-surfaces |
| Activation and default state are explicit. | Lifecycle classification rows | `reference_snapshot/T07_DISCOVERY_RESULT.json` | `validate_t07_inventory`; t07-classification-counts |
| Agent authority is explicit. | Required authority field | `declarations/TAP_AGENT_INVENTORY.json` | `validate_t07`; t07-undeclared-agent-authority |
| Pause and revoke routes are explicit. | Required lifecycle routes | `reference_snapshot/source/modules/agents/runtime.py` | `validate_t07`; t07-agent-without-revoke, t07-missing-lifecycle-route |
| Inventory and witness visibility are explicit. | Observed/declaration set comparison | `src/tap_conformance/validators/core.py` | `validate_t07`; t07-hidden-agent |
| All fourteen rows bind to public source. | Selected source closure | `reference_snapshot/T07_DISCOVERY_RESULT.json` | `t07_source_coverage`; t07-all-fourteen-source-paths |

Current: `PUBLIC_CANDIDATE_NEEDS_IMMUTABLE_PUBLICATION`. Maximum after exact R3E-B publication: `ELIGIBLE_FOR_PUBLIC_VERIFIED_AFTER_R3E_B`.

## TAP-T08

| Requirement | Mechanism | Public path | Validator / fixtures |
|---|---|---|---|
| TAP-C is not claimed by default. | C-boundary declaration | `declarations/TAP_C_BOUNDARY_DECLARATION.json` | `validate_t08`; t08-not-claimed |
| Persistence, locality, memory, and agents alone do not establish c. | Prohibited inference set | `src/tap_conformance/validators/core.py` | `validate_t08`; t08-c-from-memory, t08-c-from-uptime, t08-c-from-local_hardware, t08-c-from-agent-multiplicity |
| An accountable anchor is separately required. | Separate evidence map | `declarations/TAP_CLAIM_CARD.md` | `validate_t08`; t08-missing-anchor |
| L4 is separately required. | Separate evidence map | `reference_snapshot/source/growth_engine/c_l4_witness/models.py` | `validate_t08`; t08-missing-l4 |
| Witness is separately required. | Separate evidence map | `reference_snapshot/source/growth_engine/c_l4_witness/append_log.py` | `validate_t08`; t08-missing-witness |
| Memory governance is separately required. | Separate evidence map | `declarations/TAP_MEMORY_CLASSES.json` | `validate_t08`; t08-missing-memory-governance |
| Authority boundaries are separately required. | Separate evidence map | `reference_snapshot/source/modules/identity_anchor.py` | `validate_t08`; t08-missing-authority-boundary |

Current: `PUBLIC_CANDIDATE_NEEDS_IMMUTABLE_PUBLICATION`. Maximum after exact R3E-B publication: `ELIGIBLE_FOR_PUBLIC_VERIFIED_AFTER_R3E_B`.

## Boundary

Unmapped mandatory requirements: 0. TAP-T03 remains `PUBLIC_PARTIAL_WITH_DEPLOYMENT_EXTERNAL_BOUNDARY`. Publication of this bridge cannot establish production activation custody or TAP-C.
