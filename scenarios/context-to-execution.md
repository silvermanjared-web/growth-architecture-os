# Scenario: AI Output Looks Polished but Wrong

## Situation

An AI-assisted design workflow produces polished output that uses the wrong voice, invents an unsupported font, and introduces a component behavior that does not exist in the source system.

## Jared's reasoning

I would not solve this by writing a longer prompt.

The failure is upstream:

- source context is incomplete;
- authority between observed and inferred design choices is unclear;
- canonical tokens are not explicit;
- missing evidence is being silently filled.

Fix the operating system before tuning the prose.

## System behavior

AI Context & Design System:

1. validates source context;
2. records missing evidence as gaps;
3. extracts candidate values with provenance;
4. requires review before canon;
5. promotes approved values to canonical tokens;
6. generates derivative CSS;
7. validates the implementation.

The AI Operating System Reference provides the same authority principle: context and capability boundaries before execution.

## Decision

Improve context, provenance, and authority. Do not reward hallucination with more elaborate prompting.

## Learning

The next brief includes a context-readiness gate before generation begins.
