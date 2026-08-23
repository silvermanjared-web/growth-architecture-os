# Governance

This repo uses governance to keep the public version useful, accurate, source-aware, and semantically bounded.

## Review lanes

- Source support
- Claim admission
- Semantic routing
- Causal and funnel-level control
- Voice consistency
- Public-safety review
- Structure and referential-integrity review

## Authority stack

1. Public-safe approved facts and chronology.
2. The current canonical resume for positioning, titles, dates, scope, and resume-cleared metrics.
3. `00-positioning/claims/claims-registry.json` for public claim wording, metric definition, confidence, causal state, and prohibited inference.
4. `00-positioning/claims/semantic-governance.md` for SG0-SG3 behavior and semantic closure.
5. `00-positioning/claims/semantic-routes.jsonl` and `intent-aliases.json` for competency routing.
6. Public case studies and supporting repository material for context and method.
7. Evaluator context for emphasis only.

A lower layer may not override a higher one.

## Claim standard

The machine-readable public claim authority is `00-positioning/claims/claims-registry.json`. Use `00-positioning/proof-points.md` as the human-facing entry point.

Do not make a claim sound cleaner, broader, more senior, or more causal than the admitted evidence.

Semantic governance can select approved evidence. It cannot create evidence.

## Fail-closed standard

If a requested statement would promote a funnel level, strengthen causal language, combine unsupported mandatory conditions, rely only on private evidence, or conflict with a higher authority, do not publish the stronger claim.

## Public-safety standard

The repo should show judgment without exposing confidential detail.

Avoid raw internal material, private employee details, compensation policy, references, contact data, sensitive employer diagnostics, legal or HR-sensitive content, and metrics not cleared for public use.

A metric may be public when the canonical resume or another approved public source explicitly clears it. That does not make all underlying internal evidence publishable.

## Structure standard

Public navigation should point to real files, not placeholders or internal work-in-progress notes. Machine-readable claim routes must resolve to admitted claim IDs, and the validator must fail on broken references or malformed governance artifacts.
