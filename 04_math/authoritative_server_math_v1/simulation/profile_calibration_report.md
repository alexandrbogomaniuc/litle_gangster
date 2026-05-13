# 3x3 RTP / Volatility Calibration Report

Created: 2026-05-13T09:40:42+00:00

## Scope

First-pass local smoke calibration only. This is not certification, not final math approval, and not production runtime code.

## Run

- Profiles tested: 9 / 9.
- Seeds per profile: 2.
- Rounds per seed: 1000.
- Calibration iterations used: 2.
- Bonus buy tuned: false.
- Jackpot enabled: false.
- Exact values final: false.
- Certification status: false.

## Final Results

| mathProfileId | Target RTP | Before RTP | After RTP | Delta After | Hit Rate | Std Dev | Cap Freq | Status |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| LG_8001_RTP_LOW_VOL_LOW | 92.00% | 91.473747% | 91.473747% | -0.526253 | 0.317000 | 1.911702 | 0.00000000 | within_tolerance |
| LG_8001_RTP_LOW_VOL_MEDIUM | 92.00% | 99.099081% | 91.292400% | -0.707600 | 0.283500 | 2.242763 | 0.00000000 | within_tolerance |
| LG_8001_RTP_LOW_VOL_HIGH | 92.00% | 77.423263% | 91.808156% | -0.191844 | 0.219000 | 2.834902 | 0.00000000 | within_tolerance |
| LG_8001_RTP_MEDIUM_VOL_LOW | 94.00% | 103.103817% | 94.318845% | 0.318845 | 0.336000 | 1.847374 | 0.00000000 | within_tolerance |
| LG_8001_RTP_MEDIUM_VOL_MEDIUM | 94.00% | 96.275600% | 93.318060% | -0.681940 | 0.290000 | 2.211388 | 0.00000000 | within_tolerance |
| LG_8001_RTP_MEDIUM_VOL_HIGH | 94.00% | 92.794070% | 92.794070% | -1.205930 | 0.229000 | 2.720140 | 0.00000000 | within_tolerance |
| LG_8001_RTP_HIGH_VOL_LOW | 96.00% | 99.962842% | 96.474596% | 0.474596 | 0.320500 | 1.982789 | 0.00000000 | within_tolerance |
| LG_8001_RTP_HIGH_VOL_MEDIUM | 96.00% | 90.413750% | 96.731109% | 0.731109 | 0.253500 | 2.482539 | 0.00000000 | within_tolerance |
| LG_8001_RTP_HIGH_VOL_HIGH | 96.00% | 79.500566% | 96.236926% | 0.236926 | 0.214000 | 3.207764 | 0.00000000 | within_tolerance |

## Summary

- Profiles within +/-2.0 percentage points: 9.
- Profiles outside +/-2.0 percentage points: 0.
- Volatility ordering preserved: true.

## Blockers

- `bonus_buy_ev_pending`
- `profile_stability_large_sample_pending`
- `max_win_tail_frequency_unproven`
- `standard_deviation_targets_pending_large_simulation`
- `certification_pending`
