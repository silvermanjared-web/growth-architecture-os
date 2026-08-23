# Semantically Governed Claims

This directory is the public, inspectable evidence-routing layer behind Jared Silverman's professional positioning.

It is intentionally not a resume, cover letter, application-answer bank, compensation policy, or repository of private employer data. It shows how approved public claims are admitted, bounded, ranked, and selected when an evaluator is testing a specific capability.

## Why this exists

A list of impressive metrics is not a reliable evidence system. The same number can become misleading if it is moved to the wrong funnel level, stripped of scope, or presented as causal when the source only supports association.

The claims layer separates four jobs:

1. **Factual authority** decides what may be stated publicly.
2. **Claim control** defines scope, confidence, funnel level, and causal boundaries.
3. **Semantic governance** determines what a question is actually testing.
4. **Evidence routing** selects the strongest admissible proof without manufacturing qualifications.

## Authority order

1. Public-safe approved facts and chronology.
2. The current canonical resume for positioning, titles, dates, scope, and resume-cleared metrics.
3. `claims-registry.json` for allowed wording, metric definitions, confidence, causal state, and prohibited inference.
4. `semantic-governance.md` for SG0-SG3 admission behavior and semantic-closure rules.
5. `semantic-routes.jsonl` for competency-to-evidence routing and deterministic preference rules.
6. Public case studies and supporting repository material for context and method.
7. Evaluator or role context for emphasis only. Context may not create a qualification or promote an unsupported claim.

If two layers conflict, the higher authority controls.

## Files

- [`claims-registry.json`](claims-registry.json) — machine-readable public claim authority.
- [`semantic-routes.jsonl`](semantic-routes.jsonl) — competency routing and evidence preference rules.
- [`semantic-governance.md`](semantic-governance.md) — SG0-SG3 admission, closure, conflict, and fail-closed behavior.
- [`../proof-points.md`](../proof-points.md) — concise human-facing entry point.

## What the registry stores

Each claim records the professional context, canonical public wording, metric or scope, funnel level when applicable, causal state, confidence, source basis, eligible competencies, and prohibited inference.

The goal is not to maximize the number of claims. The goal is to make the strongest claim that the evidence actually supports.

## Public-safety boundary

This public system excludes private application policies, compensation floors, references, contact data, sensitive employer diagnostics, internal personnel information, and unapproved operational detail. Private evidence may inform the canonical resume or application system, but it is not automatically publishable here.
