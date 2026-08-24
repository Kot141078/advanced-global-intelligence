# Bridge Scope

TAP-ACEB v1.0 covers only TAP-T02, TAP-T06, TAP-T07, and TAP-T08. It is organized by TAP requirements, not by the source implementation.

## Included

- Public-safe declarations and generic validators.
- A minimal source snapshot sufficient to reproduce the 177-site T06 denominator and all 14 T07 rows.
- Selected memory, oracle-authority, identity-anchor, L4, and witness implementation paths.
- Synthetic fixtures and deterministic offline receipts.

## Excluded

- The full Ester repository and its Git history.
- Private memory, host-specific census evidence, credentials, runtime state, model weights, databases, and logs.
- The side-effectful repository `sitecustomize.py`; only an inert static audit is retained.
- Live network, cloud, agent, scheduler, model, or production execution.

TAP-T03 remains `PUBLIC_PARTIAL_WITH_DEPLOYMENT_EXTERNAL_BOUNDARY`. L4 and witness are governance mechanisms, not proof of c. MOT-c and World Intelligence are contextual corpus only. TAP-SEC remains a separate public implementation reference with `M4_FULL_PASS=false`.

Normative profile: https://doi.org/10.5281/zenodo.22070960
