# Simulation And Certification Plan

Simulation status: planned, not run.

Required simulation tiers:

- deterministic single-seed smoke run.
- multi-seed sanity run.
- 1M round tier.
- 10M round tier.
- larger lab tier as required.

Reports required:

- RTP by configured model.
- RTP with and without bonus buy.
- standard deviation and volatility.
- hit frequency.
- feature trigger frequency.
- mode split.
- coin reveal distribution.
- golden-square frequency.
- rainbow activation frequency.
- special reveal frequency.
- cap hit frequency.
- max win credits and cap multiplier.
- jackpot contribution and award frequency if enabled.
- history replay validation.

Bot testing:

- base spin bot.
- feature entry bot.
- bonus-buy bot.
- reconnect interruption bot.
- cap pursuit bot.
- error/idempotency bot.

Certification readiness:

- deterministic replay from history.
- clear RNG audit references.
- documented model versions.
- config-controlled RTP variants.
- no browser authority.
- reproducible report generation.

RTP fields:

- `BF_RTP`.
- `BF_RTP_MIN`.
- configured RTP variant.
- simulated RTP.
- confidence interval.
- cap-adjusted RTP.

## Simulation Config Refinement Update

A local deterministic smoke simulator now exists under `simulation/`. It is suitable for parsing configs and producing a sample report only. It is not certification evidence. Required future certification tiers still include calibrated 1M,
10M, and larger simulations, volatility reports, feature contribution reports, bonus-buy EV proof, cap frequency reporting, and deterministic replay validation.
