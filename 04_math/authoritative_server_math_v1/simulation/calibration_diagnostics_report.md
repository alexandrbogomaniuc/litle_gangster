# Calibration Diagnostics Report

Sprint: MathModelDesigner calibration diagnostics and limited tuning  
Created: 2026-05-13T03:56:32Z

## Result

Calibration diagnostics completed. The simulator runs deterministically, but it is not reliable for calibration yet. Limited tuning was skipped because sanity checks found structural calibration defects rather than a small safe tuning
issue.

## Diagnostic Run Size

- Models: rtp_96, rtp_94, rtp_92
- Seeds per model: 3
- Rounds per seed: 10,000
- Total rounds: 90,000
- Bonus buy: disabled
- Jackpot: disabled by default
- Certification claim: false

## RTP Diagnostic Summary

| Model | Seeds | Rounds/seed | Mean observed return multiplier | Min | Max |
|---|---:|---:|---:|---:|---:|
| rtp_96 | 3 | 10000 | 0.205943 | 0.198275 | 0.215570 |
| rtp_94 | 3 | 10000 | 0.208106 | 0.201627 | 0.220625 |
| rtp_92 | 3 | 10000 | 0.198437 | 0.194050 | 0.201531 |

The earlier 75-round smoke results were noisy, but the 10,000-round diagnostics still cluster around 0.20x. The low return is therefore not explained by tiny sample size alone.

## Sanity Audit

- Target RTP unit: profile values are 96.0, 94.0, and 92.0, which are percent-style values.
- Observed return formula: `sum(totalWinMultiplier) / roundCount`.
- Bet denominator: no explicit cluster/base bet denominator is loaded from game settings.
- Cluster base bet handling: cluster paytable values are treated directly as multipliers.
- Grid generation: deterministic weighted symbol selection exists.
- Cluster detection: adjacent same-symbol clusters are found with minimum cluster size 5.
- Cluster limitations: wild, rainbow, coin, and special symbols are excluded; wild substitution is not modeled.
- Cascade/refill: winning cells are removed, columns collapse, and refills occur up to the configured cascade limit.
- Feature contribution: coin reveals can add win, but free-spin/feature-mode/bonus-buy EV is not modeled into total return.
- Max-win cap: cap logic exists; no cap hits occurred in the diagnostic runs.
- Seed determinism: confirmed.

## Diagnosis

The primary issue is structural simulator incompleteness: RTP units and bet normalization are not explicit, feature/free-spin/bonus-buy contributions are absent or partial, and provisional weights/paytables are not calibrated. No
production/runtime/client code was touched.

## Tuning Decision

No tuning was applied. Tuning paytables or weights now would hide the missing denominator and feature-EV defects. The next sprint should first repair the non-production simulator math model, then rerun diagnostics.

## Gates

- Backend adapter implementation remains blocked.
- GameServerRegistrar generation remains blocked.
- GameClientBuilder implementation remains blocked.
- Release remains blocked.
