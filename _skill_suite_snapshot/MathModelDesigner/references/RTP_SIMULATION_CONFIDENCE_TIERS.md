# RTP Simulation Confidence Tiers

Use these tiers before interpreting RTP simulation output.

## Core Rules

- Never treat 2k, 5k, 10k, or 50k runs as RTP approval.
- 10k and 50k runs are smoke or diagnostic evidence, not calibration proof.
- Calibration decisions require larger multi-seed runs with train/validation comparison.
- High-volatility games and max-win-tail games may require tens of millions, hundreds of millions, or one billion rounds.
- Certification or lab-style confidence requires very large simulations and replay evidence.
- Always report confidence intervals, or state that confidence cannot be estimated.
- Never approve backend adapter, registration, or release from smoke-only RTP evidence.
- Always separate `simulator_wiring_passed` from `rtp_calibrated`.
- Use `outside_smoke_tolerance` instead of `failed_profile` unless a statistical confidence threshold is met.

## Tiers

| Tier | Approximate rounds | Purpose | Allowed decisions | Forbidden decisions |
| --- | ---: | --- | --- | --- |
| Wiring smoke | 2k to 10k | Check simulator starts, denominator, profile routing, obvious broken logic. | Fix wiring and config bugs. | RTP approval, profile rejection, backend, registration, release. |
| Diagnostic smoke | 10k to 50k | Check contribution direction and obvious drift. | Prioritize investigation. | RTP approval or aggressive tuning. |
| Calibration trend | 100k to 500k | Early multi-seed trend evidence. | Cautious tuning candidates. | High-volatility approval or release gates. |
| Calibration confidence | 1M to 5M | Better confidence for model tuning. | Tune after train/validation evidence. | Certification or rare-tail approval. |
| Pre-certification | 10M to 50M | Stronger RTP/volatility validation. | Prepare implementation-adjacent handoff if gates allow. | Final release approval. |
| Certification/lab scale | 100M to 1B | Rare feature, jackpot, cap, and tail behavior. | Lab package preparation. | Shortcutting formal review. |

## Required Reporting

- Sample size and seed count.
- Observed RTP and target RTP.
- Standard deviation and confidence interval when possible.
- Feature contribution and bonus-buy contribution separately.
- Cap/max-win/tail observation status.
- Clear gate statement for backend, registration, and release.

