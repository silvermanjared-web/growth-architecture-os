# ADR-002: Bounded mutation over unrestricted agents

**Status:** Accepted

## Decision

Expose named write capabilities with narrow targets, explicit inputs, authority rules, and receipts instead of granting general-purpose mutation.

## Why

Useful autonomy does not require unrestricted authority. Narrow capability design reduces risk and makes behavior easier to test and explain.

## Consequence

Some actions require more explicit contracts, but the system is safer, more legible, and easier to federate.
