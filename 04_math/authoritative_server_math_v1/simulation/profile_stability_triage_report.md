# Profile Stability Triage Report

Updated: 2026-05-13

## Reclassification

The prior triage language is corrected. The 10,000-round-per-seed run is smoke evidence only: `small_sample_profile_stability_inconclusive`. Profiles are not true RTP failures from this sample size.

## Result

- Profiles listed: 9.
- Profiles outside small-sample smoke tolerance: 8.
- Profiles inside small-sample smoke tolerance: 1.
- Harness bug found: false.
- Simulator/harness patched: false.
- Tuning values changed: false.

## Profiles Outside Small-Sample Smoke Tolerance

- `LG_8001_RTP_LOW_VOL_LOW`: target 92.00%, observed 96.159839%, delta 4.159839, seeds [93.285534, 97.214608, 97.979374], status `outside_small_sample_smoke_tolerance`.
- `LG_8001_RTP_LOW_VOL_MEDIUM`: target 92.00%, observed 84.761733%, delta -7.238267, seeds [85.625175, 83.288975, 85.371049], status `outside_small_sample_smoke_tolerance`.
- `LG_8001_RTP_LOW_VOL_HIGH`: target 92.00%, observed 95.372517%, delta 3.372517, seeds [95.661775, 96.353568, 94.102208], status `outside_small_sample_smoke_tolerance`.
- `LG_8001_RTP_MEDIUM_VOL_LOW`: target 94.00%, observed 90.704672%, delta -3.295328, seeds [93.210347, 91.73862, 87.165048], status `outside_small_sample_smoke_tolerance`.
- `LG_8001_RTP_MEDIUM_VOL_MEDIUM`: target 94.00%, observed 90.115414%, delta -3.884586, seeds [88.937826, 89.946726, 91.46169], status `outside_small_sample_smoke_tolerance`.
- `LG_8001_RTP_MEDIUM_VOL_HIGH`: target 94.00%, observed 87.224039%, delta -6.775961, seeds [85.870729, 84.32727, 91.474118], status `outside_small_sample_smoke_tolerance`.
- `LG_8001_RTP_HIGH_VOL_LOW`: target 96.00%, observed 101.083091%, delta 5.083091, seeds [101.388655, 102.801027, 99.059589], status `outside_small_sample_smoke_tolerance`.
- `LG_8001_RTP_HIGH_VOL_MEDIUM`: target 96.00%, observed 101.859882%, delta 5.859882, seeds [104.277877, 102.782991, 98.518779], status `outside_small_sample_smoke_tolerance`.

## Correct Interpretation

- These results indicate smoke instability, not statistically proven RTP failure.
- The previous 2 seeds x 1,000 rounds calibration pass was too small to establish confidence.
- The 10,000-round-per-seed run is useful for routing, denominator, and obvious drift checks, not approval/rejection.
- Large-sample confidence is required before further tuning decisions.

## Harness Checks

- Profile calibration adjustments covered all 9 profiles: true.
- mathProfileId resolution matched the 9-profile matrix: true.
- No evidence was found that the harness ignored profile-specific adjustments or reused one base profile for all 9 profiles.

## Next Safest Math Step

Define confidence-scale simulation tiers and then run larger train/validation calibration only when explicitly approved; do not treat smoke variance as profile failure.

Backend adapter implementation and GameServerRegistrar generation remain blocked.
