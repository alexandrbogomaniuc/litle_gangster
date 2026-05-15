# RTP Confidence And Simulation Scale Report

Created: 2026-05-13T11:16:56+00:00

## Main Correction

The previous 10,000-round-per-seed 3x3 run is smoke evidence only. It is now classified as `small_sample_profile_stability_inconclusive`, not proof
  that 8 profiles truly fail RTP and not proof that 1 profile is approved.

## What Small Samples Can Prove

- Simulator starts and completes.
- RTP percent versus multiplier units are not obviously inverted.
- Bet denominator and profile routing are present.
- `mathProfileId` selection reaches the intended profile.
- Obvious impossible configs, missing fields, or broken feature paths.

## What Small Samples Cannot Prove

- True RTP convergence.
- High-volatility profile approval or rejection.
- Bonus-buy EV.
- Jackpot behavior.
- Max-win tail or cap frequency.
- Release or certification readiness.

## Why Large Runs Are Needed

High-volatility slots concentrate value into rare events. Bonus buys introduce
separate denominator and purchase-state questions. Jackpot hooks and max-win
caps add rare-tail outcomes. A 10k or 50k smoke run can miss these events
entirely, so normal-looking RTP can still be wrong and drifting RTP can still
be random variance.

## Confidence Estimate Summary

These estimates use only the observed per-round standard deviation from the
30,000-round smoke sample per profile. They are useful for planning but not
certification because cap/tail and bonus-buy paths are not represented.

- Worst-profile required rounds for +/-2.0 percentage points: 90,972.
- Worst-profile required rounds for +/-1.0 percentage point: 363,887.
- Worst-profile required rounds for +/-0.5 percentage point: 1,455,547.
- Worst-profile required rounds for +/-0.25 percentage point: 5,822,187.

Blocker: `insufficient_tail_variance_data_for_required_round_estimate` remains because no cap hits were observed and rare feature/tail behavior is not
  represented.

## Gate Policy

- Tuning is allowed only after wiring smoke passes and trend/confidence samples support the change.
- Backend adapter work is allowed only after explicit user approval and with math/profile/history blockers resolved or explicitly accepted.
- GameServerRegistrar work is allowed only after approved profile metadata and final values are stable.
- Release/certification work requires certification/lab-scale evidence and formal approvals.
