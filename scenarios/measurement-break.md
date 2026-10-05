# Scenario: Measurement Break During Active Optimization

## Situation

Platform conversions rise 22%, CRM-qualified outcomes fall 14%, and a tracking deployment occurred during the period. Leadership asks whether to scale spend into the apparent platform improvement.

## Jared's reasoning

I would refuse the scale decision until the signal is trustworthy.

The cost of waiting briefly for measurement reconciliation is lower than the cost of reallocating capital against a false signal.

1. Validate event definitions and deduplication.
2. Compare platform, analytics, CRM, and server-side counts where available.
3. Identify the first date divergence appears.
4. Separate real funnel change from instrumentation change.
5. Establish a temporary decision metric if one source remains trustworthy.
6. Restore optimization only when the evidence boundary is clear.

## System behavior

Data Sanity Checker → Funnel Data Validator → Measurement architecture reference → Intelligence synthesis → named information gap.

No mutation is required.

The correct system behavior can be **refusal to optimize**.

## Learning

The next operating cycle adds deployment-aware measurement QA and a fallback decision metric to the brief.
