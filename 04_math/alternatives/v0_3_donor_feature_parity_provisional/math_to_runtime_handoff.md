# Math To Runtime Handoff

Generated/updated: 2026-05-11 11:05:00 Europe/London

Status: PROVISIONAL_CONTRACT. This is not donor-true certified math, not runtime code, not registration generation, and not release approval.

## Runtime Owner Status

The runtime owner remains unproven. Candidate owners are New Games backend, classic GS processor, game-specific backend package, or another current-GS-supported runtime. Browser is forbidden.

## Runtime Must Consume

- `result_schema.json`;
- cluster/cascade evaluation contract;
- golden-square state contract;
- rainbow activation contract;
- coin/special reveal contract;
- feature-mode and bonus-buy contracts;
- max-win cap contract;
- round-completion and state-persistence contracts;
- registration metadata values only as display/config inputs, not executable import.

## Transaction/State Handoff

The result must expose enough state for reserve/settle or current-GS process-equivalent accounting, history replay, reconnect recovery, and lastAction/state restoration. Do not assume Mantis `processTransactions` unless ExtGame is later proven.
