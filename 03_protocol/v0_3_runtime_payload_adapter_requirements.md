# v0.3 Runtime Payload Adapter Requirements

## Status

DEFINED_AS_REQUIREMENTS_NOT_IMPLEMENTED_NOT_PROVEN.

## Required Adapter Direction

The backend/runtime owner must transform authoritative Little Gangster math output into the generic runtime envelope. The v0.3 result schema should be represented in `presentationPayload` or an approved equivalent renderer payload while
wallet/accounting remains in envelope wallet/round fields.

## Mandatory v0.3 Rendering Payload Fields

- `cascade_steps`
- `removed_cells`
- `dropped_cells`
- `new_symbols`
- `clusters`
- `golden_squares_before`
- `golden_square_events`
- `golden_squares_after`
- `rainbow_activation_events`
- `coin_reveals`
- `special_reveals`
- `feature_mode_state`
- `bonus_buy_state`
- `max_win_cap`
- `winRatio`
- `winTier`
- `round_completion`
- `state_persistence`
- `animation_hints`

## Mandatory Envelope Fields Outside Presentation

- authoritative balance/currency in `wallet`
- round ID, bet, win, status, and outcome hash in `round`
- feature action state in `feature`
- recovery state in `restore`
- idempotency/retry state in `idempotency` and `retry`

## Adapter Acceptance Criteria

Before GameClientBuilder implementation:

1. The runtime owner is proven by source.
2. The exact endpoint contract is selected for Little Gangster.
3. A v0.3 payload fixture or adapter schema is approved.
4. The adapter is confirmed compatible with strict core-protocol validation or the schema update is reviewed.
5. History/recovery payloads include enough v0.3 state to replay/reconnect safely.
6. Browser result authority remains false.

## Blockers

- `little_gangster_8001_runtime_not_found`
- `v0_3_presentation_payload_extension_unproven`
- `production_rng_owner_unverified_for_current_gs`
- `runtime_result_owner_unproven`
