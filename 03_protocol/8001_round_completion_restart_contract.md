# 8001 Round Completion and Restart Contract

Date: 2026-05-15
Status: planning only

## Round Completion Conditions

A Little Gangster round may be marked complete only when all applicable checks are true:

- all cascades complete;
- all base wins and feature triggers resolved;
- all free spins complete;
- all bonus-buy feature spins complete;
- cap enforcement complete;
- wallet/accounting settlement complete or equivalent approved accounting final state recorded;
- no pending restart/FRB transition;
- history/Lasthands payload generated for final state;
- gameState-derived completion requirement satisfied;
- `roundFinishedHelper` / `endRoundSignature` equivalent is satisfied or explicitly mapped.

## Cascades

Cascade state is active until no more winning clusters, drops, new-symbol fills, feature triggers, or cap checks remain. The browser may animate
cascades,
but completion is backend/wrapper-owned.

## Free Spins

Free-spin state is complete only when feature spin count reaches zero, retriggers are resolved, cascade chains from the final spin are complete, and
settlement state is ready.

## Bonus-Buy Feature

Bonus-buy feature is complete only when:

- purchase action is accepted and accounted for;
- purchased feature state starts from the approved 100x package;
- all purchased feature spins/cascades/retriggers are resolved;
- cap state is applied;
- bonus-buy result payload is generated;
- wallet settlement reference is recorded.

## Cap Enforcement

Cap enforcement must run before `round_complete`. If cap is reached, history must store pre-cap win, capped win, cap hit flag, and cap reason.

## Settlement

Round completion and settlement completion are separate. The wrapper may reach `round_complete` before `settlement_complete`, but it must not expose
the
round as fully final for wallet/history/reconnect until settlement has completed or a pending/stuck review state is recorded.

## Restart Advisory Handling

If a restart advisory or `restart=true` equivalent is present, the wrapper must route to `restart_required` and preserve:

- game id;
- bank/session context;
- mode;
- language;
- bonus id if applicable;
- last accepted action;
- last hand or recoverable state.

## FRB and Bonus Checklist

The wrapper plan must explicitly handle or block:

- `FRB_FINISHED`;
- `FRB_CANCELED`;
- `BONUS_EXPIRED`;
- `FRB_MAX_WIN_LIMIT_REACHED`;
- bonus id presence/absence;
- active FRB restart;
- feature state after FRB transition;
- expired/canceled bonus cleanup.

## Blockers

- `round_finished_helper_mapping_pending`
- `end_round_signature_mapping_pending`
- `restart_frb_transition_mapping_pending`
- `bonus_buy_runtime_validation_pending`
- `wallet_settlement_test_pending`
