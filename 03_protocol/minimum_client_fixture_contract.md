# Minimum Client Fixture Contract

Status: PLANNING_ONLY_ALLOWED.

## Purpose

Define the minimum fixture shape that may be created later for renderer planning without proving production runtime ownership.

No fixture JSON was created in this sprint.

## Fixture Boundaries

A future fixture must be:

- clearly named planning-only;
- stored under planning/test documentation, not production runtime code;
- deterministic and static;
- free of donor/scaffold asset bodies;
- free of secrets, sessions, tokens, private links, and real wallet values;
- marked non-authoritative for production RNG, outcomes, wallet, history, and registration.

## Minimum Shape

The fixture should contain:

- generic `/slot/v1` envelope groups: `wallet`, `round`, `feature`, `presentationPayload`, `restore`, `idempotency`, `retry`;
- a reviewed placeholder for v0.3 render payload, such as `presentationPayload.littleGangsterV03`, if schema review allows it;
- one base cascade example;
- one golden-square event;
- one rainbow activation event;
- bronze/silver/gold coin reveal examples;
- optional special reveal candidate;
- one feature-mode state;
- one max-win cap example;
- one round-completion state;
- one reconnect/restore example.

## Fixture Use

Allowed:

- client renderer planning;
- scene/object mapping checks;
- animation sequencing review;
- documentation examples.

Forbidden:

- production runtime;
- payout certification;
- wallet accounting;
- registration import;
- release approval.

