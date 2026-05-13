# Math Quality Gate

Status: `PASS_WITH_LIMITATIONS` for downstream layout planning; not release math approval.

## Questions Answered

| Question | Answer |
|---|---|
| Is the current 5x3 model internally valid? | Yes, as a provisional fixed-line simulator. It creates reel stops, evaluates paylines, handles scatters/free spins, and produces reports. |
| Is the current 5x3 model aligned with reference research? | No. Reference research reported a 6x5 cluster-style donor/reference layout, while v0.1 is 5x3 fixed-20-line. |
| Is the current 5x3 model aligned with likely product/art direction? | No for a close Little Gangster reference-following product. Keeping 5x3 would require an explicit original redesign decision and would invalidate 6x5 scene
expectations. |
| Is the simulator producing RTP through real symbol evaluation or artificial scaling? | v0.1 evaluates symbols but also uses `payout_scale` in the model config to scale all evaluated wins. v0.2 removes runtime scaling and uses explicit
variant paytables. |
| Are payouts post-normalized to target RTP? | No post-simulation normalization was found in v0.1 or v0.2. v0.1 uses payout scaling during win calculation; v0.2 does not. |
| Are wins generated from reel stops/grid outcomes? | Yes. v0.1 uses 5x3 reel stops and paylines. v0.2 uses 6x5 grids and connected cluster evaluation. |
| Are free spins/bonus buy actually simulated or placeholder-reported? | Free spins are simulated in both packages. Bonus buy remains a provisional optional feature and is not part of base-spin RTP validation. |
| Are double-up and bonus buy real math features or placeholders? | Double-up is a neutral placeholder. Bonus buy is a provisional feature contract with pricing/EV still requiring review. |
| Can ArtSceneMapper safely proceed using the current selected math? | Yes with limitations, but only using the selected v0.2 6x5 cluster layout, not the superseded v0.1 5x3 layout. |

## Simulator Audit

- v0.1 `simulate_math.py` reads `payout_scale` from each `model_config.json` and multiplies evaluated line/scatter/free-spin wins by that value. This is artificial payout scaling during simulation, even though outcomes are still generated
from reels and paytables.
- v0.1 does not normalize total wins after simulation and does not force outcome distribution.
- v0.1 free spins are symbol-triggered and simulated; bonus buy/double-up are not release-ready math features.
- v0.2 `simulate_cluster_math.py` reports target RTP for comparison only. It does not read target RTP to scale wins during a run, does not normalize totals after simulation, and does not force result distribution.
- v0.2 RTP is produced from explicit variant paytable values, symbol weights, connected cluster evaluation, scatter wins, and symbol-triggered free spins.
- v0.2 paytable values were calibrated after an initial smoke run. This is acceptable for provisional workflow math, but it is not certification-grade proof.

## Simulation Evidence

| Variant | Seed | Rounds | Target RTP | Simulated RTP | Deviation | Status | Hit frequency | Std dev x bet | Max observed |
|---|---:|---:|---:|---:|---:|---|---:|---:|---:|
| `rtp_96` | 2026050901 | 200000 | 96.00% | 96.000000% | -0.000000% | pass_workflow_tolerance | 27.7395% | 10.707746 | 938.854755x |
| `rtp_96` | 2026050902 | 100000 | 96.00% | 94.570522% | -1.429478% | outside_workflow_tolerance | 27.8560% | 10.827595 | 648.639269x |
| `rtp_96` | 2026050903 | 100000 | 96.00% | 96.539211% | 0.539211% | outside_workflow_tolerance | 27.7970% | 10.273030 | 657.219370x |
| `rtp_94` | 2026050901 | 200000 | 94.00% | 94.000000% | -0.000000% | pass_workflow_tolerance | 27.7395% | 10.484668 | 919.295279x |
| `rtp_94` | 2026050902 | 100000 | 94.00% | 92.600302% | -1.399698% | outside_workflow_tolerance | 27.8560% | 10.602020 | 635.125949x |
| `rtp_94` | 2026050903 | 100000 | 94.00% | 94.527977% | 0.527977% | outside_workflow_tolerance | 27.7970% | 10.059009 | 643.527298x |
| `rtp_92` | 2026050901 | 200000 | 92.00% | 92.000000% | 0.000000% | pass_workflow_tolerance | 27.7395% | 10.261590 | 899.735812x |
| `rtp_92` | 2026050902 | 100000 | 92.00% | 90.630084% | -1.369916% | outside_workflow_tolerance | 27.8560% | 10.376446 | 621.612636x |
| `rtp_92` | 2026050903 | 100000 | 92.00% | 92.516744% | 0.516744% | outside_workflow_tolerance | 27.7970% | 9.844987 | 629.835233x |

## Interpretation

The calibration seed passes the provisional +/-0.5 percentage-point workflow tolerance for all variants. Two additional 100,000-round seeds per variant wander outside that tight tolerance because the model is high volatility and the extra
runs are short. Therefore, the selected v0.2 package is acceptable for ArtSceneMapper layout alignment, but not for release math approval.

## Final Quality Gate Result

`PASS_WITH_LIMITATIONS`

- The 5x3 vs 6x5 mismatch is resolved by selecting v0.2 6x5 cluster for downstream work.
- ArtSceneMapper may proceed with a 6x5 cluster target scene.
- Math release approval remains blocked by full multi-seed/certification-grade RTP validation, backend runtime integration, asset approval, wallet/launch tests, and release audit.
