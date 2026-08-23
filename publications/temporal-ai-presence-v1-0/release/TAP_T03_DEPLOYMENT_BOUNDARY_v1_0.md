# TAP-T03 Deployment Boundary v1.0

**Status:** partial
**Zenodo version DOI:** 10.5281/zenodo.22070960

TAP-T03 remains partial.

TAP-T03 is publicly documented as partial with an explicit deployment-external boundary.

Repository evidence establishes:

- the background-processing declaration model;
- discovery and classification of repository-owned surfaces;
- zero unresolved repository-owned rows under the R2B discovery model;
- controls and evidence requirements for those surfaces.

Repository evidence does not establish:

- activation state in every deployment;
- which external orchestrators are active;
- whether all declared pause routes are enforced in production;
- whether all revoke routes are operational in production;
- whether all deployment-level witness routes are active;
- full production deployment conformance.

R2C identified 78 deployment-external evidence-requirement rows:

| Requirement category | Rows |
|---|---:|
| `DEPLOYMENT_CONFIG_REQUIRED` | 26 |
| `EXTERNAL_ORCHESTRATOR_REQUIRED` | 8 |
| `MULTIPLE_EVIDENCE_REQUIRED` | 9 |
| `OPERATOR_DECLARATION_REQUIRED` | 17 |
| `RUNTIME_SNAPSHOT_REQUIRED` | 18 |
| **Total** | **78** |

These rows are explicit unverified deployment evidence requirements, not failures. No host-specific deployment data is included in this package. Passing repository tests or a sandbox fixture does not establish the activation, pause, revoke, or witness state of every real deployment.
