# Client Interoperability

The operating contract is intentionally client-neutral.

A ChatGPT workflow, Claude session, CLI, desktop application, or MCP-compatible client should consume the same basic surface:

1. discover capabilities;
2. inspect input and authority requirements;
3. invoke one named capability;
4. receive a structured receipt;
5. decide whether another action is warranted.

## MCP-shaped boundary

The reference does not require an MCP server to prove the architecture. A capability can be exposed as an MCP tool when a client benefits from protocol-level discovery and invocation.

The important design choice is that protocol transport does not own business authority. The capability contract still defines what the operation may touch, whether it mutates state, and what evidence it returns.

## Anti-pattern

Do not create separate hidden capability models for every client. That causes permission drift and makes the system impossible to reason about.

Prefer one admitted capability contract with multiple thin client adapters.