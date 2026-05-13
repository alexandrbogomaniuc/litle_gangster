# Calibration Next Tuning Actions

Created: 2026-05-13T03:56:32Z

## Do Next

1. Add explicit RTP normalization to the non-production simulator: report both multiplier and percent, and load cluster-equivalent bet metadata from game settings.
2. Integrate free-spin, feature-mode, and bonus-buy EV smoke paths before touching weights or paytables.
3. Re-run the same 3-model / 3-seed / 10,000-round diagnostic after model-completeness fixes.

## Do Not Do Yet

- Do not tune endlessly.
- Do not use post-spin payout scaling to force RTP.
- Do not claim certification-grade RTP.
- Do not start backend adapter implementation.
- Do not generate registration artifacts.

## Top Tuning Levers After Simulator Fixes

1. Cluster paytable scale and size bands.
2. Symbol weights, especially high-symbol frequency and special-symbol frequency.
3. Feature trigger, free-spin, coin reveal, and bonus-buy contribution rules.

## Current Blockers

- rtp_denominator_and_unit_model_pending
- free_spin_feature_mode_simulation_pending
- bonus_buy_ev_model_pending
- provisional_weights_paytable_not_certified
