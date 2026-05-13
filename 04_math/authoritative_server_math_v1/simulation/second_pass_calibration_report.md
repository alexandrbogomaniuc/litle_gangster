# Second-Pass Calibration Report

Sprint: MathModelDesigner second-pass calibration tuning  
Created: 2026-05-13T08:12:26Z

## Outcome

Second-pass calibration completed. One `rtp_92`-only provisional tuning set was applied: `clusterPayMultiplier=1.026`. No post-spin forced payout scaling was used, and exact values remain non-final.

## RTP 92 Before / After

- Before: `90.0894%`
- After: `90.9716%`
- Target: `92.0%`
- Status: improved but still slightly under target.

## Regression Check

- rtp_96: `95.3082%`; no_regression_detected.
- rtp_94: `94.1765%`; no_regression_detected.

## Bonus-Buy EV Diagnostic

Bonus-buy EV is calculated as `bonusBuyWinTotal / bonusBuyCostTotal`, where cost is `buyCostMultiplier * betDenominator`. The simulator does run purchased feature spins and counts their wins. The path is still incomplete because it lacks
product-approved purchased feature behavior, premium EV rules, retriggers, and final cost/EV targets.

Result: `bonus_buy_simulation_path_incomplete`. Do not tune bonus buy blindly.

## Blockers

- rtp_92_still_slightly_under_target_after_second_pass
- bonus_buy_simulation_path_incomplete
- bonus_buy_cost_ev_pending
- large_scale_rtp_validation_pending
- certification_pending
