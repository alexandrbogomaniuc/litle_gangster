# Limited Calibration Tuning Report

Sprint: MathModelDesigner limited calibration tuning  
Created: 2026-05-13T04:57:31Z

## Outcome

Limited calibration completed with one provisional tuning set: `2026-05-13_cluster_feature_boost_v1`. The simulator ran successfully. No post-spin forced payout scaling was used as release math.

## Tuning Set

- Cluster paytable entries multiplied by `6.5x` as `diagnostic_only_not_release_math`.
- Feature trigger probability changed from `0.018` to `0.08`.
- Free-spin counts changed from `8/10/12` to `12/15/18` for modes 1/2/3.

## Base / Feature RTP Before And After

| Model | Before observed RTP | After observed RTP | Target RTP |
|---|---:|---:|---:|
| rtp_96 | 22.0500% | 95.3082% | 96.0% |
| rtp_94 | 20.7443% | 94.1765% | 94.0% |
| rtp_92 | 20.0875% | 90.0894% | 92.0% |

## Bonus-Buy Smoke Before And After

| Model | Before bonus-buy smoke RTP | After bonus-buy smoke RTP | Status |
|---|---:|---:|---|
| rtp_96 | 0.5702% | 4.5243% | bonus_buy_cost_ev_pending |
| rtp_94 | 0.5615% | 4.3891% | bonus_buy_cost_ev_pending |
| rtp_92 | 0.5476% | 4.2012% | bonus_buy_cost_ev_pending |

## Contribution Diagnosis

- Base cluster wins increased materially and now contribute about `0.34x` to `0.37x` in the tuned base runs.
- Feature/free-spin smoke now contributes about `0.41x` to `0.45x` in tuned base runs.
- Coin reveal contribution remains present but not independently tuned in this sprint.
- Special reveal contribution remains zero in the current smoke simulator.
- Cap frequency remained zero in limited runs.
- No-win frequency remains high enough to require larger volatility validation.

## Decision

Do not move to backend adapter yet. `rtp_96` and `rtp_94` are close enough for the next calibration pass, but `rtp_92` is under target and bonus-buy EV is still not viable.
