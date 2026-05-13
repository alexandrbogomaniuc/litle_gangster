# Runtime API Contract Review

Status: planning-only review. This document does not authorize client implementation.

## 1. Result Payload The Client Must Consume

The client must consume a backend/runtime-owned result payload compatible with `04_math/alternatives/v0_3_donor_feature_parity_provisional/result_schema.json`.

Minimum runtime envelope needs:

- session and idempotency state: `sessionId`, `requestCounter`, `stateVersion`, `clientOperationId` or equivalent.
- wallet/accounting summary from backend only, not animation logic.
- round result with `roundId`, `spinId`, `totalWin`, `winRatio`, `winTier`, and cap state.
- presentation payload containing v0.3 render states.
- restore/history payload for reconnect and replay.

## 2. Mandatory v0.3 Rendering Fields

- `base_game.grid_before`
- `base_game.cascade_steps[]`
- `base_game.cascade_steps[].removed_cells`
- `base_game.cascade_steps[].dropped_cells`
- `base_game.cascade_steps[].new_symbols`
- `base_game.cascade_steps[].clusters`
- `base_game.total_cascade_win`
- `base_game.final_grid`
- `base_game.golden_squares_before`
- `base_game.golden_square_events`
- `base_game.golden_squares_after`
- `base_game.rainbow_activation_events`
- `base_game.coin_reveals[]`
- `feature_mode_state`
- `bonus_buy_state`
- `max_win_cap`
- `winRatio`
- `winTier`
- `round_completion`
- `state_persistence`
- `animation_hints`

## 3. Optional Or Provisional Fields

- `base_game.special_reveals[]`
- `base_game.affected_golden_squares`
- `base_game.activation_source`
- `feature_mode_state.spins_or_rounds_remaining` if a feature mode is active.
- `bonus_buy_state.purchased_feature_start_state`
- `state_persistence.lastAction_or_current_gs_equivalent`

These fields are documented for v0.3 parity but may need adapter names once the current runtime owner is proven.

## 4. Fields Requiring Runtime Owner Proof

- authoritative grid/cascade sequence.
- all win amounts and cap state.
- feature-mode state and free-spin/feature-round progression.
- bonus-buy purchase state and cost.
- state persistence, restore, and history payloads.
- wallet/accounting values.

## 5. Animation Hints Only

`animation_hints`, win-tier labels, timing hints, and scene/object IDs are renderer instructions. They cannot be used as payout, settlement, RNG, or registration authority.

## 6. Fields The Browser Must Not Author

The browser must not author RNG values, symbol outcomes, cascade decisions, cluster wins, cap decisions, round completion authority, wallet/accounting mutations, or registration metadata.

## 7. Wallet/Accounting Boundary

Wallet balance, reserve, settle, collect, and close-session decisions belong to the current GS/runtime wallet flow. The client may display balances returned by backend payloads, but it must not infer wallet state from animation.

## 8. Registration Metadata Boundary

Registration metadata may provide game ID, display RTP, bet limits, cap display values, routes, title, and feature flags. It must not be treated as executable math or as the animation result payload.

## 9. Likely But Unproven API Shape

Staging evidence suggests a candidate `slot-browser-v1` contract with endpoints for bootstrap, opengame, playround, featureaction, resumegame, gethistory, and closegame. The Gamesv1 `RuntimeEnvelopeResponse` shape contains `wallet`,
`round`, `feature`, `presentationPayload`, `restore`, `idempotency`, and `retry`.

For Little Gangster, the missing proof is that the chosen runtime emits the v0.3 result payload or a documented adapter from runtime envelope to v0.3 fields.

## 10. Source Evidence Still Needed

- final Little Gangster result owner.
- exact endpoint path and request/response schema for game 8001.
- whether `@gamesv1/core-protocol` is the selected transport package for this game.
- whether `new-games-server` is the real runtime owner or only a scaffold/reference.
- whether a game-specific backend package will consume `math_package.json`.
- how VABS/Lasthands/history uses the v0.3 state payload.
## RuntimeApiInspection Update

Status: PARTIAL_GENERIC_PROOF_ONLY.

The current source proves generic `/slot/v1` endpoints and a generic `RuntimeEnvelopeResponse`, but it does not prove a Little Gangster/8001 runtime owner or v0.3 payload adapter. `/slot/v1` remains a candidate lane for Little Gangster
implementation, not a selected production lane.

Evidence labels:

- PROVEN generic: `/slot/v1/bootstrap`, `opengame`, `playround`, `featureaction`, `resumegame`, `gethistory`, `closegame`.
- PROVEN generic: envelope fields `wallet`, `round`, `feature`, `presentationPayload`, `restore`, `idempotency`, `retry`.
- LIKELY/CANDIDATE: `presentationPayload` as the right browser-visible container for v0.3 render state.
- NOT_FOUND: Little Gangster/8001 runtime package, runtime owner, and payload adapter.
- NOT_FOUND: direct consumption of project `math_package.json` by current GS registration/runtime.

Implementation decision: GameClientBuilder implementation remains blocked. A later sprint must prove the runtime owner and approve the v0.3 adapter contract before code generation.

## FixturePlanning Update

Status: NON_PRODUCTION_FIXTURES_CREATED.

The fixture planning sprint created static renderer fixtures under `06_resulting_code/planning/fixtures/`.

Fixture payloads use the candidate generic extension `presentationPayload.gamePayload`:

```json
{
  "gameKey": "little-gangster",
  "schemaVersion": "v0.3",
  "payload": {
    "...": "v0.3 render state"
  }
}
```

Fallback option remains `presentationPayload.littleGangsterV03` if the runtime schema team rejects a reusable generic extension.

This fixture work does not prove the runtime owner, does not prove the v0.3 result API contract, does not approve the presentation extension, and does not permit client implementation.
