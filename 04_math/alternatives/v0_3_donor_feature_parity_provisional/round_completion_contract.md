# Round Completion Contract

Generated/updated: 2026-05-11 11:05:00 Europe/London

Status: PROVISIONAL_CONTRACT. This is not donor-true certified math, not runtime code, not registration generation, and not release approval.

## Completion Conditions

A round can be complete only when:

- base spin evaluation is complete;
- cascade sequence is complete;
- no pending cascade remains;
- no pending reveal remains;
- no pending feature transition remains;
- feature spin is complete if a feature is active;
- purchased bonus-buy feature is complete if applicable;
- max-win cap handling is complete if reached;
- final state is ready for history/state persistence.

## Current-GS Status

`roundFinished`, `roundFinishedHelper`, and `endRoundSignature` remain current-GS-equivalent checklist items. They are not selected implementation APIs until current source/config proves the required lane.
