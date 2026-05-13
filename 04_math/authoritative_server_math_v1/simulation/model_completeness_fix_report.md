# Model Completeness Fix Report

Sprint: MathModelDesigner simulator model-completeness fix  
Created: 2026-05-13T04:39:10Z

## Outcome

The non-production simulator was patched and now reports explicit RTP percent/multiplier fields, an explicit cluster-equivalent bet denominator, base-game/cascade counters, feature-mode/free-spin smoke contribution, bonus-buy smoke
reporting, jackpot-disabled status, cap/win-tier metrics, and a deterministic replay sample.

This is still calibration-smoke tooling only. It is not production math and not certification evidence.

## Run Size

- Models: rtp_96, rtp_94, rtp_92
- Seeds: 8101, 8102
- Rounds per seed: 5,000
- Bonus-buy disabled run: yes
- Bonus-buy enabled smoke run: yes, because cost candidates exist; EV remains pending
- Jackpot: disabled

## Base / Feature Smoke Summary

| Model | Target RTP | Target multiplier | Observed multiplier | Observed RTP percent |
|---|---:|---:|---:|---:|
| rtp_96 | 96.0% | 0.96 | 0.220500 | 22.0500% |
| rtp_94 | 94.0% | 0.94 | 0.207443 | 20.7443% |
| rtp_92 | 92.0% | 0.92 | 0.200875 | 20.0875% |

## Bonus-Buy Smoke Summary

| Model | Observed multiplier | Observed RTP percent | Status |
|---|---:|---:|---|
| rtp_96 | 0.005701 | 0.5702% | bonus_buy_cost_ev_pending |
| rtp_94 | 0.005615 | 0.5615% | bonus_buy_cost_ev_pending |
| rtp_92 | 0.005477 | 0.5476% | bonus_buy_cost_ev_pending |

## Denominator Status

- denominatorType: `defaultTotalBet_credits_cluster_equivalent`
- betDenominator: `100.0`
- source: `game_settings_profiles.json` defaultTotalBet for each RTP profile
- missing denominator behavior: simulator fails with `cluster_bet_denominator_missing`

## Feature / Bonus / Jackpot Status

- Free-spin and feature-mode smoke path: present, deterministic, and config-driven from feature probability, mode weights, and starting spins.
- Bonus-buy smoke path: present, deterministic, and cost-candidate driven, but EV remains `bonus_buy_cost_ev_pending`.
- Jackpot: explicitly disabled with `disabled_pending_product_decision`.

## Remaining Calibration Blockers

- Large-scale RTP calibration is still pending.
- Bonus-buy EV is still pending.
- Feature-mode EV tuning is still pending.
- Symbol weights and cluster paytable are still provisional.
- Certification is not claimed.

## Gate Status

Backend adapter implementation, GameServerRegistrar generation, GameClientBuilder implementation, wallet tests, and release remain blocked.
