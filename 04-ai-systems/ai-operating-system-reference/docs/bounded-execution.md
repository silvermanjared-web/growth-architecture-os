# Bounded Execution

Bounded execution is the middle path between read-only assistants and unconstrained agents.

A bounded mutation has five properties:

1. a named capability;
2. a narrow target;
3. explicit accepted inputs;
4. a known authority requirement;
5. a receipt describing the result.

The system should refuse work when the requested target falls outside the capability boundary.

## Example

`artifact.write` may write `reports/today.md` under an admitted sandbox. It may not write `../../.ssh/config`, even if the caller asks.

This is simpler and stronger than adding a general-purpose approval engine around unrestricted filesystem access.

## Human authority

Confirmation is appropriate when the effect is consequential and not already covered by an admitted recurring contract.

Confirmation is not a substitute for capability design. A dangerous general-purpose tool does not become well-bounded merely because a human clicked yes.