# Calibration Diagnostics Blockers

Created: 2026-05-13T03:56:32Z

## Active Blockers

- rtp_denominator_and_unit_model_pending: target RTP profile values are percent-style, while observed return is reported as a multiplier without explicit denominator.
- free_spin_feature_mode_simulation_pending: current simulator does not execute full free-spin or feature-mode loops.
- bonus_buy_ev_model_pending: bonus-buy EV is not modeled or certified.
- provisional_weights_paytable_not_certified: symbol weights and cluster paytable are candidates only.

## Implementation Gates

Backend adapter implementation and GameServerRegistrar generation remain blocked until simulator/model outputs are coherent enough to serve as authoritative input contracts.
