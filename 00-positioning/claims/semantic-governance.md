# Semantic Claim Governance

Semantic governance controls **meaning and evidence selection**, not truth. It may classify what an evaluator is testing and route to approved evidence, but it may never override the canonical resume, promote a quarantined fact, change a funnel level, or manufacture a qualification.

## Admission tiers

| Tier | Question shape | Behavior |
|---|---|---|
| **SG0** | Direct factual or scope request | Retrieve the exact admitted claim. No semantic reinterpretation. |
| **SG1** | Clear single competency | Route to the default approved evidence for that competency. |
| **SG2** | Ambiguous, behavioral, multi-axis, or role-specific | Classify intent, build the eligible evidence set, rank it, test semantic closure, then tailor the explanation. |
| **SG3** | Unsupported, contradictory, causal-risk, sensitive, or materially composite | Fail closed. Qualify the answer, request additional evidence, or do not make the claim. |

## Decision pipeline

`question -> semantic classification -> SG tier -> eligible claim set -> deterministic ranking -> semantic closure -> public wording -> claim validation`

Classification and evidence selection are separate stages. A classifier can say that a question is about operating transformation; it does not get to invent which career story proves that transformation.

## Evidence ranking

When more than one admitted claim could answer a question:

1. Prefer the evidence that directly matches the competency and business decision being tested.
2. Prefer newer and more senior evidence when proof strength is otherwise comparable.
3. Use older evidence when it is materially stronger, more quantified, or uniquely matched.
4. Prefer one primary claim and at most one supporting proof point.
5. Never stack unrelated metrics simply because they are impressive.

## Semantic closure

A routed answer is not valid merely because one relevant claim exists. Every material axis of the question must be supported.

Example: a prompt asking for a transformation, stakeholder resistance, and a measurable outcome requires evidence for all three. If the registry supports transformation and outcome but not stakeholder resistance, the route does not close. Escalate to SG3 rather than filling the missing axis with plausible prose.

## Causal controls

The registry distinguishes:

- `directly_supported` — the source supports the stated relationship.
- `associated_after_change` — the outcome was observed after a broader change; do not assign single-tactic causality.
- `scope_only` — the metric establishes scale, not performance impact.
- `contextual` — useful supporting context with narrower public use.

A semantic route may narrow a claim. It may not strengthen the causal state.

## Fail-closed triggers

Escalate to SG3 when:

- the requested qualification is not in the admitted registry;
- a question combines multiple mandatory conditions and one is unsupported;
- public wording would convert applications, engagements, enrollments, or adoption into revenue or profit;
- a metric would be attributed to one tactic when the evidence supports only a broader program or sequence;
- a role-specific keyword would create unsupported ownership such as formal P&L, MMM, incrementality, or another unverified capability;
- two source layers materially conflict;
- the only available support is private, sensitive, or not cleared for public use.

## Output provenance

A governed implementation should be able to explain internally:

- semantic route selected;
- SG tier;
- primary and supporting claim IDs;
- source authority;
- causal controls applied;
- closure result;
- final admission verdict.

The public prose can remain concise. The reasoning behind the claim should still be inspectable.
