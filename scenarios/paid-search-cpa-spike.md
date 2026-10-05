# Scenario: Paid Search CPA Spikes 31%

## Situation

Paid search CPA is up 31% week over week. CRM lead-to-opportunity conversion is stable. Brand search volume increased. A landing-page release shipped five days ago. Media spend and auction pressure are roughly flat.

## Jared's reasoning

I would not begin by changing bids.

The first question is whether the CPA increase is a **media problem, conversion problem, measurement problem, or mix problem**.

1. Validate signal integrity and denominator changes.
2. Segment brand vs. non-brand, device, geography, audience, query class, and landing page.
3. Compare click quality and downstream conversion, not just platform CPA.
4. Inspect the landing-page release because timing creates a plausible conversion-side break.
5. Protect stable high-value demand while isolating the affected segment.
6. Only change bidding or allocation once the constraint is identified.

### Decision

If downstream quality is stable but landing-page CVR fell after release, the primary intervention belongs in CRO / release remediation, not indiscriminate media cuts.

## System behavior

```text
Data Sanity Checker
      ↓
Performance Media Diagnostics
      ↓
Funnel Data Validator
      ↓
Marketing Intelligence Agent synthesis
      ↓
Recommendation: isolate landing-page effect
      ↓
Marketing Ops Toolkit writes reviewed audit snapshot
      ↓
Receipt
      ↓
Full-Cycle Growth Loop carries learning into next brief
```

## Bounded action

The system may generate an audit snapshot or recommendation artifact. It does not automatically rewrite bids because the evidence does not justify that authority.

## Learning

The next brief should explicitly include release monitoring and landing-page CVR guardrails as part of the measurement plan.
