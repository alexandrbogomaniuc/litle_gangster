# Little Gangster v0.2 6x5 Cluster Volatility Report

Status: high-volatility provisional model.

## Evidence

The simulator reports standard deviation around 10x total bet for 100,000 to 200,000-round smoke runs, with hit frequency near 27.7% and large free-spin contribution. This supports the requested high-volatility profile at workflow level
only.

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

## Notes

- Free spins contribute more than base-game wins in the calibration-seed summaries.
- Max observed wins remained far below the proposed 10,000x cap in these short runs.
- Longer simulations are required to evaluate tail behavior and max-win plausibility.
