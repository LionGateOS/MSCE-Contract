# MSCE Memory Contract v1

## Purpose

MSCE Memory Contract defines the interface between:

WorkRunner execution interpretation (MSCE)

and

LionGateOS Memory continuity preservation.

The contract is an independent bridge.

## Ownership

WorkRunner owns:
- execution;
- jobs;
- routing;
- permissions;
- raw events.

MSCE owns:
- lifecycle interpretation;
- grouping;
- decisions;
- outcomes;
- blockers;
- evidence references.

MSCE-Contract owns:
- schema;
- validation;
- compatibility;
- examples;
- versioning.

Memory owns:
- continuity;
- provenance;
- retrieval;
- refinement;
- review;
- canonical storage.

## v1 Principles

- The contract does not create Memory.
- The contract does not execute tasks.
- The contract does not contain consumer-specific logic.
- Human review remains the final authority.

## Validation

v1 requires:

- valid contract_version;
- required identity fields;
- controlled lifecycle states;
- confidence between 0.0 and 1.0;
- provenance metadata.

