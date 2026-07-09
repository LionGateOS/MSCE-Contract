# MSCE Memory Contract Versioning

## Version Policy

MSCE-Contract uses explicit versioning.

Breaking changes require a new major contract version.

Example:

v1 → v2

Non-breaking additions may occur within a version line.

## Rules

Allowed without breaking v1:

- additional optional fields;
- additional examples;
- documentation improvements;
- validator improvements that do not change meaning.

Requires new major version:

- removing required fields;
- changing field meaning;
- changing lifecycle state definitions;
- changing provenance requirements.

## Principle

The contract defines a stable interface between independent systems.

Changes must preserve interoperability.
