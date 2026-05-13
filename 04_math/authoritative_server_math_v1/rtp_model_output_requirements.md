# RTP Model Output Requirements

Each approved math build must produce:

- math version.
- RTP variant id.
- target RTP.
- simulated RTP.
- confidence interval.
- volatility metric.
- hit frequency.
- feature contribution.
- base contribution.
- bonus-buy contribution when enabled.
- jackpot contribution when enabled.
- cap hit frequency.
- max win multiplier.
- top award frequency.
- feature mode contribution.
- coin reveal contribution.
- special reveal contribution.

Configuration fields:

- `BF_RTP`.
- `BF_RTP_MIN`.
- RTP variant list.
- max win cap.
- jackpot enabled flag.
- bonus-buy enabled flag.

Release rule:

- Release approval remains false until simulation reports and lab-ready evidence exist.

## Simulation Config Refinement Update

RTP output requirements now have concrete planning structures in `simulation_config_refinement/rtp_model_profiles.json`. The three model IDs are `rtp_96`, `rtp_94`, and `rtp_92`. Each records target RTP, RTP without bonus buy, bonus-buy
RTP, min/max RTP, volatility target, max-win cap, feature contribution buckets, and non-final status fields.
