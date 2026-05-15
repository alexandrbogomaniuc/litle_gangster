# Train / Validation Seed Policy

Training and validation seed families must be distinct.

## Scale Modes

| Mode | Scale | Purpose |
| --- | ---: | --- |
| `smoke` | 2k to 50k rounds total or per profile | Wiring, denominator, profile routing, obvious broken logic. |
| `fast_train_matrix` | About 10M total across 9 profiles | Preliminary train evidence only. |
| `standard_train_profile` | About 10M per profile | Preferred train gate before validation. |
| `heavy_train_profile` | 50M+ per profile | High-volatility or tail-sensitive train evidence. |

The selected mode must be named in every report.

## Training

Training results may guide tuning. Reports must record seed set, rounds, RTP
confidence interval when available, hit rate, standard deviation, volatility
ordering, cap frequency, and win-tier distribution.

## Validation

Validation starts only after the train gate passes. Validation seeds must not be
used for tuning. If validation fails, return to train with a revised training
approach or new training seed split; do not tune from validation output.

## Tail / Max-Win

Tail jobs use a separate seed family. Tail evidence must report cap hits, cap
frequency, max observed win, pre-cap/capped status when available, and whether
possible max win is planning-only or final. Tail evidence is not certification.
