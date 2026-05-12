# Simulation Certification Test Matrix

Status: test plan only.

Simulation tiers:

- smoke deterministic.
- multi-seed sanity.
- 1M rounds.
- 10M rounds.
- lab-scale run.

Metrics:

- RTP.
- confidence interval.
- volatility.
- hit frequency.
- feature trigger frequency.
- feature mode split.
- bonus-buy RTP if enabled.
- jackpot contribution if enabled.
- cap hit frequency.
- replay failure count.

Certification checks:

- deterministic replay.
- reproducible report inputs.
- config versioning.
- RNG audit references.
- no browser authority.
- no registration math import.

