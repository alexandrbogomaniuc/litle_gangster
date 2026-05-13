# Little Gangster v0.2 6x5 Cluster RTP Report

Status: provisional smoke validation only; not release certification.

## Summary

The selected v0.2 package uses explicit per-variant paytables and a shared 6x5 cluster simulator. The simulator does not scale wins during a run and does not normalize totals after simulation. RTP comes from generated grids, symbol weights,
connected cluster wins, scatter wins, and symbol-triggered free spins.

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

## Result

- Calibration-seed smoke status: pass provisional workflow tolerance for all variants.
- Extra short-seed status: outside +/-0.5 percentage-point tolerance on the 100,000-round seeds.
- Validation level: `smoke_provisional_high_volatility_multi_seed_pending`.
- Release status: blocked until longer independent multi-seed simulations and RTPAndReleaseAuditor.
