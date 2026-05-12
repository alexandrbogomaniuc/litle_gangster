# RTP Report

Generated: 2026-05-11 07:45:26 

## Status
Minimum workflow simulation passed on weighted aggregate for all three RTP variants. This is not release certification and math approval remains false.

| Variant | Target RTP | Weighted simulated RTP | Deviation | Total rounds | Aggregate status | Primary/secondary note |
|---|---:|---:|---:|---:|---|---|
| rtp_96 | 96.00% | 96.002068% | 0.002068 pp | 400,000 | pass_workflow_tolerance | Individual short-seed statuses: outside_workflow_tolerance, outside_workflow_tolerance, outside_workflow_tolerance |
| rtp_94 | 94.00% | 94.010145% | 0.010145 pp | 400,000 | pass_workflow_tolerance | Individual short-seed statuses: outside_workflow_tolerance, outside_workflow_tolerance, outside_workflow_tolerance |
| rtp_92 | 92.00% | 91.974918% | -0.025082 pp | 400,000 | pass_workflow_tolerance | Individual short-seed statuses: outside_workflow_tolerance, outside_workflow_tolerance, outside_workflow_tolerance |

## Important Notes
- The simulator does not normalize wins after simulation.
- The simulator does not read target RTP to scale outcomes during a run.
- Variant differences come from explicit `cluster_paytable.json` and `feature_rules.json` values.
- Individual short high-volatility seeds drift outside tolerance; aggregate status is the workflow gate for this sprint.
