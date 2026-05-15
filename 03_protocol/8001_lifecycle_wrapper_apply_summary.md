# Little Gangster 8001 Lifecycle Wrapper Apply Summary

Created: 2026-05-15

## Outcome

Lifecycle wrapper implementation apply completed for Little Gangster 8001 in Staging
source only. The current 8001 payload mapper remains the result mapper, and the new
wrapper adds lifecycle state, accounting representation, round completion, reconnect
state, persistence metadata, and blocker propagation around `presentationPayload.gamePayload`.

## Source Scope

Created `new-games-server/src/games/little-gangster/lifecycle/` with:

- lifecycle types and required lifecycle states
- lifecycle state derivation with unknown-state rejection
- action/accounting representation
- round completion and restart advisory representation
- lifecycle state persistence
- reconnect recovery representation
- active blocker propagation
- wrapper functions for base spin and approved-for-planning 100x bonus buy

Modified only `new-games-server/src/index.ts` to route guarded gameId 8001 base spin and
100x bonus-buy feature-action payloads through the lifecycle wrapper.

## Preserved Boundaries

- No VABS/VBA visual history route was implemented.
- No GameClientBuilder implementation was created.
- No GameServerRegistrar generation or registration artifact was created.
- No DB/Cassandra action occurred.
- No wallet/API call occurred.
- No donor browsing or asset capture occurred.
- No release approval occurred.
- Active Little Gangster math, bonus-buy rules, RTP/volatility profiles, BF_RTP targets,
  and registration configs were not changed.

## Bonus-Buy Status

100x bonus buy remains approved for implementation planning only. It remains not
release-approved, not certified, not runtime-tested, not wallet-tested, and not
VABS/Lasthands-tested. 125x and 150x remain blocked.

## Active Blockers Carried

- `bonus_buy_runtime_validation_pending`
- `bonus_buy_wallet_accounting_test_pending`
- `bonus_buy_vabs_lasthands_test_pending`
- `bonus_buy_tail_maxwin_confirmation_pending`
- `bonus_buy_release_approval_pending`
- `bonus_buy_certification_false`
- `vabs_visual_history_route_implementation_pending`
- `gameserverregistrar_generation_blocked`
- `release_not_approved`
