# MathModelDesigner Math Quality Gate Skill Report

## Scope

Only MathModelDesigner and SprintReporter were run for this sprint. The sprint audited the mismatch between reference research's 6x5 cluster-style observations and the previous 5x3 fixed-line provisional math package.

## Actions Performed

- Read the required skill suite instructions, project AGENTS, manifest, prior reference reports, protocol reports, asset inventory summaries, and prior math outputs.
- Audited the prior v0.1 simulator and found symbol/reel evaluation plus `payout_scale` runtime payout scaling.
- Determined the 5x3 v0.1 package is internally valid as a preserved provisional alternative but not acceptable as the selected downstream layout.
- Selected `Option 2`: switch Little Gangster to a provisional 6x5 cluster model.
- Created `v0.2_6x5_cluster_provisional` under `04_math/alternatives/v0_2_6x5_cluster/`.
- Created a backend-oriented 6x5 cluster simulator that reads explicit package files, does not access network/secrets/GS/wallet/database, and does not scale wins during simulation.
- Ran 200,000-round calibration-seed smoke simulations for RTP 96/94/92 and two 100,000-round secondary seeds per variant.
- Updated math reports, manifest, assumptions, decisions log, and handoff.

## Quality Gate Result

`PASS_WITH_LIMITATIONS`

ArtSceneMapper may proceed using the selected 6x5 cluster layout. Math is not release-approved.

## Simulation Summary

| Variant | Seed | Rounds | Target | Simulated | Deviation | Status |
|---|---:|---:|---:|---:|---:|---|
| `rtp_96` | 2026050901 | 200000 | 96.00% | 96.000000% | -0.000000% | pass_workflow_tolerance |
| `rtp_96` | 2026050902 | 100000 | 96.00% | 94.570522% | -1.429478% | outside_workflow_tolerance |
| `rtp_96` | 2026050903 | 100000 | 96.00% | 96.539211% | 0.539211% | outside_workflow_tolerance |
| `rtp_94` | 2026050901 | 200000 | 94.00% | 94.000000% | -0.000000% | pass_workflow_tolerance |
| `rtp_94` | 2026050902 | 100000 | 94.00% | 92.600302% | -1.399698% | outside_workflow_tolerance |
| `rtp_94` | 2026050903 | 100000 | 94.00% | 94.527977% | 0.527977% | outside_workflow_tolerance |
| `rtp_92` | 2026050901 | 200000 | 92.00% | 92.000000% | 0.000000% | pass_workflow_tolerance |
| `rtp_92` | 2026050902 | 100000 | 92.00% | 90.630084% | -1.369916% | outside_workflow_tolerance |
| `rtp_92` | 2026050903 | 100000 | 92.00% | 92.516744% | 0.516744% | outside_workflow_tolerance |

## Important Findings

- The 5x3 vs 6x5 mismatch is resolved by selecting v0.2 6x5 for downstream work.
- v0.1 uses runtime payout scaling, so v0.1 RTP validation is superseded and not release-trustworthy.
- v0.2 produces wins from generated grids, cluster rules, paytables, scatters, and free spins without simulation-time scaling.
- v0.2 smoke validation is useful for workflow planning, but full independent multi-seed RTP validation remains pending.

## Forbidden Actions Confirmation

No browser work, donor gameplay investigation, donor asset capture, donor asset body inspection, client build, Cassandra/DB action, wallet call, raw secret handling, full donor URL persistence, release approval, or later workflow skill was
performed.
