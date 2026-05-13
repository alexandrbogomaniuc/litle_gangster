# Volatility Profile Smoke Report

Created: 2026-05-13

## Scope

This fast-lane sprint added local non-production support for selecting Little Gangster simulation profiles by `mathProfileId` and applying provisional LOW / MEDIUM / HIGH volatility modifiers in memory. It did not change production math,
backend code, Staging source, client code, registration artifacts, wallet flows, or release gates.

## Run

- Profiles tested: 9 / 9.
- Seeds per profile: 2.
- Rounds per seed: 2,000.
- Total base rounds: 36,000.
- Bonus buy: disabled for volatility smoke because EV remains pending.
- Jackpot: disabled.
- Certification claim: false.
- Exact values final: false.

## Profile Results

| mathProfileId | Target RTP | Observed RTP | Hit Rate | Std Dev | Max Win | Feature Trigger | Cap Freq | Status |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| LG_8001_RTP_LOW_VOL_LOW | 92.00% | 96.790317% | 0.32875 | 2.02733 | 17.3315 | 0.09450 | 0.00000000 | smoke_completed_not_certified |
| LG_8001_RTP_LOW_VOL_MEDIUM | 92.00% | 91.482036% | 0.26850 | 2.256998 | 28.1060 | 0.08175 | 0.00000000 | smoke_completed_not_certified |
| LG_8001_RTP_LOW_VOL_HIGH | 92.00% | 86.059328% | 0.21475 | 3.186073 | 99.8065 | 0.05825 | 0.00000000 | smoke_completed_not_certified |
| LG_8001_RTP_MEDIUM_VOL_LOW | 94.00% | 97.698377% | 0.33400 | 1.999909 | 16.6296 | 0.08825 | 0.00000000 | smoke_completed_not_certified |
| LG_8001_RTP_MEDIUM_VOL_MEDIUM | 94.00% | 97.264800% | 0.28250 | 2.363980 | 22.4960 | 0.07850 | 0.00000000 | smoke_completed_not_certified |
| LG_8001_RTP_MEDIUM_VOL_HIGH | 94.00% | 85.435794% | 0.22050 | 2.695538 | 47.9600 | 0.05950 | 0.00000000 | smoke_completed_not_certified |
| LG_8001_RTP_HIGH_VOL_LOW | 96.00% | 101.452114% | 0.32750 | 2.124725 | 15.6804 | 0.09850 | 0.00000000 | smoke_completed_not_certified |
| LG_8001_RTP_HIGH_VOL_MEDIUM | 96.00% | 99.923125% | 0.27175 | 2.467303 | 21.7750 | 0.08175 | 0.00000000 | smoke_completed_not_certified |
| LG_8001_RTP_HIGH_VOL_HIGH | 96.00% | 89.493697% | 0.22425 | 2.788398 | 35.3966 | 0.06125 | 0.00000000 | smoke_completed_not_certified |

## Findings

- Simulator can now select profiles by `mathProfileId`.
- LOW volatility produced higher hit rates than HIGH volatility in all RTP rows.
- HIGH volatility generally produced lower feature trigger rates and higher tail potential.
- Observed RTP is unstable across volatility levels because the current modifiers are provisional and not rebalanced per profile.
- Cap frequency stayed at zero in this small smoke, so max-win/cap tail behavior remains unproven.
- Bonus-buy EV remains excluded from this smoke and still blocks full profile approval.

## Next Action

Run a fast-lane MathModelDesigner 3x3 volatility calibration sprint that tunes each volatility row toward target RTP while preserving hit-rate and standard-deviation ordering. Keep all values non-final until larger multi-seed validation and
certification-scale simulation pass.

