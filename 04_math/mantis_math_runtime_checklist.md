# Mantis Math Runtime Checklist

Status: checklist only; no math implementation generated in this sprint.

## Scope

The Mantis/ExtGame lessons are advisory validation inputs for the next MathModelDesigner retry. They do not select ExtGame and do not prove that `processTransactions` is the current Little Gangster runtime API.

## Required Next Math Retry Checks

| Requirement | v0.3/vNext math impact | Status |
|---|---|---|
| Donor feature parity | Keep cascade, golden-square, rainbow, coin reveal, feature modes, bonus buy, and max-win cap contract. | required |
| Round completion state | Expose a backend-owned round-complete marker compatible with current GS/new-games or a verified `roundFinishedHelper` path. | required |
| `winRatio` / `winTier` | Expose win ratio and candidate tier for animation hints using advisory thresholds unless current GS/docs override. | required |
| Max-win cap fields | Separate possible max win, cap multiplier, pre-cap win, capped win, and cap event location. | required |
| Bet formula mapping | Define 6x5 cluster total bet mapping to GS coin/denomination/min/default/max config. Do not use fixed-line formula blindly. | required |
| State / lastAction handoff | Expose restore-safe state for cascades, golden squares, feature modes, pending collect, cap reached, and history replay. | required |
| Process-transaction equivalent | Expose accounting-relevant values for current-lane reserve/settle/process-equivalent flow. Do not assume ExtGame `processTransactions` unless source proves it. | required |
| RNG boundary | Simulation RNG is local deterministic only. Production outcome RNG owner remains backend/current-GS validation item. | required |
| Double-up | Keep removed from active scope unless direct donor/product evidence changes. | required |

## Non-Implementation Statement

This sprint did not change the selected math package and did not generate a new math implementation. These items are requirements for the next MathModelDesigner retry or audit.

## Blockers

- `production_rng_owner_unverified_for_current_gs`
- `round_completion_contract_unverified_for_current_gs`
- `state_persistence_owner_unverified`
- `process_transaction_equivalent_unverified_for_current_gs`
- `cluster_bet_mapping_to_current_gs_unverified`

