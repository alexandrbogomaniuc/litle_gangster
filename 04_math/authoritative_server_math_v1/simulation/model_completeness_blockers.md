# Model Completeness Blockers

Created: 2026-05-13T04:39:10Z

## Remaining Blockers

- large_scale_rtp_calibration_pending: post-fix smoke runs are limited to 5,000 rounds per seed and do not prove RTP.
- bonus_buy_cost_ev_pending: cost candidates exist, but bonus-buy EV is not validated.
- feature_mode_ev_tuning_pending: feature modes now run in smoke form, but their EV contribution is not calibrated.
- symbol_weights_paytable_calibration_pending: weights/paytables were not tuned in this sprint.
- certification_pending: no certification-grade simulation or lab report exists.

## Cleared Simulator Completeness Blockers

- RTP percent vs multiplier reporting is now explicit.
- Bet denominator is now explicit and sourced from game settings.
- Missing denominator now fails loudly.
- Free-spin/feature-mode smoke path is present.
- Bonus-buy smoke path is present but EV-pending.
- Jackpot disabled state is explicit.
