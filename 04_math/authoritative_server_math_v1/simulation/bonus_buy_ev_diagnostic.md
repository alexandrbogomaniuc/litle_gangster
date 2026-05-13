# Bonus-Buy EV Diagnostic

Created: 2026-05-13T08:12:26Z

## Answers

1. bonusBuyCostMultiplier: candidates are `100`, `125`, and `150` for modes 1/2/3.
2. Denominator: `bonusBuyCostTotal = buyCostMultiplier * betDenominator`, with `betDenominator=100.0` from defaultTotalBet.
3. Purchased feature spins: yes, the simulator calls the purchased feature spin smoke path.
4. Purchased feature wins counted: yes, feature wins are counted into `bonusBuyWinTotal`.
5. EV formula: yes, EV is reported as `bonusBuyWinTotal / bonusBuyCostTotal`.
6. Low EV cause: the path is structurally incomplete for product EV. It uses ordinary feature-spin smoke behavior and does not model bonus-buy-specific premium state, guaranteed value, retrigger rules, or final product EV.

## Decision

Do not tune bonus buy in this sprint. Keep `bonus_buy_simulation_path_incomplete` and `bonus_buy_cost_ev_pending` active.
