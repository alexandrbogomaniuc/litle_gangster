# Volatility Profile Blockers

Created: 2026-05-13

- `volatility_profile_specific_calibration_pending`: all 9 profiles run, but RTP drift is material for several LOW/HIGH volatility combinations.
- `bonus_buy_ev_pending`: bonus-buy profile RTP remains excluded from the volatility smoke.
- `max_win_tail_frequency_unproven`: cap frequency was zero in the small smoke run.
- `standard_deviation_targets_pending_large_simulation`: target bands are provisional and require larger multi-seed runs.
- `gs_profile_matrix_storage_unproven`: registration storage for the full 3x3 matrix remains unproven.
- `certification_pending`: no volatility result is certified or final.

Implementation, backend adapter work, GameClientBuilder work, GameServerRegistrar artifact generation, wallet tests, DB work, and release approval remain blocked.

