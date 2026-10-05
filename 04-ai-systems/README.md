# AI Systems

This section defines how AI becomes operating leverage inside the Growth Architecture OS.

The purpose is not to present AI as a novelty layer. The purpose is to show how context, capabilities, bounded execution, evidence, and human authority can make repeated work faster and more reliable without turning the system into a maze of approvals or opaque agents.

## Five-minute path

Start with the [AI Operating System Reference](ai-operating-system-reference/README.md).

It is the public-safe technical reference for the architecture used across the portfolio:

- explicit capability discovery;
- observe / propose / mutate effect classes;
- bounded mutation;
- structured receipts;
- client and MCP interoperability;
- smoke, unit, and security tests;
- minimum necessary governance.

Then use the supporting documents for domain-specific detail.

## Files

- [AI Operating System Reference](ai-operating-system-reference/README.md) — executable public-safe architecture reference
- [AI Operating Model](ai-operating-model.md) — practical adoption principles for growth and marketing operations
- [Agent Workflows](agent-workflows.md) — reusable patterns for briefs, readouts, CRO roadmaps, case studies, and QA
- [Prompt Library](prompt-library.md) — source-aware prompts for executive communication and operating-model work
- [Governance and Risk](governance-and-risk.md) — confidentiality, accuracy, ownership, tone, and risk boundaries

## Core point of view

AI is most useful when it changes the operating model, not when it merely produces faster prose.

A useful system should:

- know what context is authoritative;
- expose what it can actually do;
- distinguish observation from mutation;
- let ordinary work happen without repeated permission loops;
- keep mutations narrow;
- return evidence after execution;
- preserve human judgment for consequential decisions;
- maintain and clean itself where the work is deterministic;
- avoid governance layers that add more friction than safety.

## Public implementation examples

| Repository | AI operating-system pattern |
|---|---|
| [Marketing Intelligence Agent](https://github.com/silvermanjared-web/marketing-intelligence-agent) | Source-aware intelligence, capability discovery, agent routing, receipts |
| [Marketing Ops Toolkit](https://github.com/silvermanjared-web/marketing-ops-toolkit) | Deterministic checks and five bounded mutation contracts |
| [AI Context & Design System](https://github.com/silvermanjared-web/brand-context-system) | Structured context, extraction, canonical tokens, implementation handoff |
| [Private-to-Public Release Gate](https://github.com/silvermanjared-web/private-to-public-release-gate) | Fail-closed publication boundary, privacy scanning, drift evidence |

## Standard

AI should make the operating system lighter, clearer, more capable, and more self-sufficient.

If an AI implementation adds layers without adding useful capability, it has failed the design test.
