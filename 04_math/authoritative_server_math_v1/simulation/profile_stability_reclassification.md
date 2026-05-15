# Profile Stability Reclassification

Created: 2026-05-13T11:16:56+00:00

## Correction

The prior 10,000-round-per-seed profile results are reclassified as `small_sample_profile_stability_inconclusive`. They are smoke evidence only and
  must not be treated as true RTP failures or true RTP approval.

Terminology changes:

- `failed profiles` -> `profiles outside small-sample smoke tolerance`.
- `failure category` -> `smoke instability category`.
- `recalibration required` -> `large-sample confidence required before further tuning`.

## Reclassified Profiles

| mathProfileId | Target RTP | Observed RTP | Delta | Prior wording | Correct wording |
| --- | ---: | ---: | ---: | --- | --- |
| LG_8001_RTP_LOW_VOL_LOW | 92.00% | 96.159839% | 4.159839 | failed | `outside_small_sample_smoke_tolerance` /
  `small_sample_profile_stability_inconclusive` |
| LG_8001_RTP_LOW_VOL_MEDIUM | 92.00% | 84.761733% | -7.238267 | failed | `outside_small_sample_smoke_tolerance` /
  `small_sample_profile_stability_inconclusive` |
| LG_8001_RTP_LOW_VOL_HIGH | 92.00% | 95.372517% | 3.372517 | failed | `outside_small_sample_smoke_tolerance` /
  `small_sample_profile_stability_inconclusive` |
| LG_8001_RTP_MEDIUM_VOL_LOW | 94.00% | 90.704672% | -3.295328 | failed | `outside_small_sample_smoke_tolerance` /
  `small_sample_profile_stability_inconclusive` |
| LG_8001_RTP_MEDIUM_VOL_MEDIUM | 94.00% | 90.115414% | -3.884586 | failed | `outside_small_sample_smoke_tolerance` /
  `small_sample_profile_stability_inconclusive` |
| LG_8001_RTP_MEDIUM_VOL_HIGH | 94.00% | 87.224039% | -6.775961 | failed | `outside_small_sample_smoke_tolerance` /
  `small_sample_profile_stability_inconclusive` |
| LG_8001_RTP_HIGH_VOL_LOW | 96.00% | 101.083091% | 5.083091 | failed | `outside_small_sample_smoke_tolerance` /
  `small_sample_profile_stability_inconclusive` |
| LG_8001_RTP_HIGH_VOL_MEDIUM | 96.00% | 101.859882% | 5.859882 | failed | `outside_small_sample_smoke_tolerance` /
  `small_sample_profile_stability_inconclusive` |
| LG_8001_RTP_HIGH_VOL_HIGH | 96.00% | 96.941348% | 0.941348 | passed | `inside_small_sample_smoke_tolerance` /
  `small_sample_profile_stability_inconclusive` |

## Gate Impact

- Backend adapter implementation remains blocked.
- GameServerRegistrar generation remains blocked.
- Release/certification remains blocked.
- Tuning should not be aggressive until larger train/validation evidence exists.
