# Little Gangster v0.2 6x5 Cluster Feature Contribution Report

Status: provisional.

## Features Modeled

- Base game cluster wins.
- Wild substitution for cluster pay symbols.
- Scatter pays.
- Scatter-triggered free spins.
- Free-spin retriggers capped at 50 free spins per round.
- Bonus buy contract placeholder, not included in base-spin RTP.
- Double-up neutral placeholder, not included in base-spin RTP.
- Jackpot not modeled.

## Contribution Summary

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

The calibration-seed summaries show base contribution around 36.3% to 37.9% and free-spins contribution around 55.7% to 58.1%, depending on RTP variant.

## Blockers

- Bonus buy EV and pricing need review.
- Double-up needs product/regulatory decision.
- Free-spin exact rules remain provisional.
- Full multi-seed feature contribution confidence is pending.
