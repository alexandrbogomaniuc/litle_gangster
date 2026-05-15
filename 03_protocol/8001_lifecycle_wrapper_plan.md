# 8001 Lifecycle Wrapper Plan

Date: 2026-05-15
Status: planning only, no implementation

## Wrapper Purpose

The Little Gangster 8001 lifecycle wrapper is the integration boundary that must sit around the current `presentationPayload.gamePayload` backend
adapter.
Its job is to own launch/session lifecycle, runtime action sequencing, state persistence, wallet/accounting references, recovery, history routing,
blocker
propagation, and registration dependency checks.

## Current Adapter Is Payload Mapper Only

The current 8001 adapter is a guarded payload mapper. It can translate a backend-shaped Little Gangster result into `presentationPayload.gamePayload`,
but
it does not own launch/session creation, restart/FRB flow, close session, wallet transaction control, VABS/VBA routes, Lasthands storage, or GS
registration/cache settings.

The mapper may remain, but it must be wrapped. The current adapter is payload mapper only and not a complete runtime owner or release-ready
implementation.

Key planning status phrases:

- current adapter payload mapper only
- lifecycle wrapper required
- VABS visual history route required
- GameClientBuilder blocked
- GameServerRegistrar blocked

## Lifecycle States

The wrapper must coordinate these states:

- `session_start`
- `open_game`
- `base_idle`
- `base_spin_pending`
- `cascade_active`
- `feature_triggered`
- `free_spins_active`
- `bonus_buy_purchase_pending`
- `bonus_buy_feature_active`
- `cap_reached`
- `round_complete`
- `settlement_pending`
- `settlement_complete`
- `reconnect_pending`
- `restart_required`
- `close_pending`
- `error_pending`
- `stuck_transaction_review`

## Action Flow

1. Launch/session wrapper validates game id, bank/session context, language, mode, selected model/profile, and registration settings readiness.
2. `open_game` resolves player/session state and chooses whether to start clean, resume, or route to restart handling.
3. Base spin action creates a paid action record, reserves/settles through the approved accounting boundary, and forwards backend-owned result state
   into
the adapter mapper.
4. Cascade completion remains backend-owned and must be represented as action/state progression, not inferred by the browser.
5. Feature/free-spin actions continue from persisted feature state and must not charge as paid spins unless rules require an explicit paid purchase.
6. Bonus-buy purchase action records the 100x purchase/debit separately from the purchased feature result.
7. Bonus-buy feature action resolves the feature result, stores the BF_RTP profile context, and preserves blockers because 100x remains planning-only,
   not
release/certified.
8. Cap enforcement runs before round completion and settlement completion are marked final.
9. History and Lasthands payloads are emitted after each action that changes replayable state.
10. Close/reconnect/restart paths must use persisted wrapper state, not only the renderer payload.

## Wallet and Accounting Boundary

The wrapper must keep wallet truth outside `presentationPayload.gamePayload`. The game payload may carry references only:

- debit/reserve reference;
- settle/credit reference;
- rollback reference if applicable;
- idempotency key;
- action id;
- round id;
- accounting status.

Balance must come from the settle/process response or equivalent wallet/accounting control path, not from repeated polling as a substitute for
settlement.

## State Persistence Boundary

Persisted state must include wrapper state, current action id, round id, game session id, selected `mathProfileId`, action sequence,
cascade/free-spin/bonus-buy state, cap state, wallet/accounting references, `roundFinished`/completion signature status, and replay determinism
references.

The adapter's `statePersistence` object is an output representation and can be stored as part of replay/reconnect data, but it is not the only state
store.

## Recovery Boundary

Recovery must account for:

- reconnect during idle state;
- reconnect during cascade;
- reconnect during free spins;
- reconnect after purchase debit but before bonus-buy feature settlement;
- restart-required or FRB transition states;
- stuck/pending wallet transactions;
- close-session behavior with unfinished round state.

Any unresolved transaction must route to `stuck_transaction_review` and must not be hidden by a fresh `getBalance` call.

## History Boundary

The wrapper must produce or persist the history payload required by the VABS/VBA/Lasthands route plan. The current adapter's `historyReplay` and
`vabsFields` are necessary inputs, but route/service integration is still required for round replay, session replay, whole-session replay, last hand,
in-game history, and backoffice access.

## Registration Dependency

The wrapper cannot remove registration blockers. Current blockers include `POSSIBLE_MODELS`, `BF_RTP`, `BF_RTP_MIN`, `BF_BETS`, `SD_KEYS`,
`FeatureKPI`,
`CAP_WIN_MULTIPLIER`, `MAX_WIN`, `POSSIBLE_MAX_WINS`, GL bet fields, language settings, FRB fields, and round-finished helpers/signatures.

## Blocker Propagation

Every wrapper response for 8001 must propagate:

- `legacy_lifecycle_wrapper_required` until implemented and tested;
- `vabs_visual_history_route_required` until route/service exists and is tested;
- `bonus_buy_runtime_validation_pending`;
- `bonus_buy_wallet_accounting_test_pending`;
- `bonus_buy_vabs_lasthands_test_pending`;
- `bonus_buy_tail_maxwin_confirmation_pending`;
- `bonus_buy_release_approval_pending`;
- `bonus_buy_certification_false`;
- `gameclientbuilder_implementation_blocked`;
- `gameserverregistrar_generation_blocked`;
- `release_not_approved`.

## Why GameClientBuilder Remains Blocked

GameClientBuilder remains blocked because the client cannot safely target a runtime contract until wrapper responsibilities are accepted, VABS/history
route
expectations are known, wallet/accounting references are tested, and registration settings dependencies are resolved. The current adapter proves
payload
shape only, not full runtime lifecycle.
