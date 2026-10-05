# Governance

Governance exists to preserve safe autonomy, not to create ceremony.

## Rules

1. Read operations should remain low-friction.
2. Write operations must declare their mutation boundary.
3. Capabilities may not expand their own authority.
4. Unknown or ambiguous targets are refused.
5. High-impact writes require explicit confirmation or an already-admitted owner contract.
6. Execution returns a receipt.
7. Private data, credentials, and environment-specific identifiers do not belong in this public reference.
8. Cleanup is bounded: deterministic wins first, classify the rest, stop.

## Decision hierarchy

Use the simplest control that reliably contains the risk:

`read-only > preview > bounded mutation > explicit confirmation > refuse`.

Do not add approval gates when a narrower capability contract solves the same problem.