# Math Config To Registration Field Map

This document maps simulation config fields to future registration metadata. It is not a registration artifact.

| Config area | Future registration field or metadata | Status | Notes |
| --- | --- | --- | --- |
| RTP model IDs | POSSIBLE_MODELS, CURRENT_MODEL | provisional_pending_registration_review | Supports rtp_96, rtp_94, rtp_92. |
| Display RTP | RTP, RTP_MIN, RTP_WITHOUT_BF, RTP_MIN_WITHOUT_BF, BF_RTP, BF_RTP_MIN | provisional_pending_simulation | Exact values not final. |
| Cluster bet metadata | GL_MIN_BET_DEFAULT, GL_DEFAULT_BET, GL_MAX_BET_DEFAULT | placeholder_pending_math_validation | Use cluster-equivalent totals, not fixed-line math. |
| Compatibility lines | POSSIBLE_LINES, LINES_COUNT, DEFAULTNUMLINES | placeholder_pending_cluster_registration_mapping | Compatibility only if GS requires line-shaped fields. |
| Bonus buy | BF_BETS, GL_BF_MAX_BETS, bonusBuyOptions | blocked_pending_ev_validation | Cost and EV not final. |
| Max win | POSSIBLE_MAX_WINS, POSSIBLE_MAX_WINS_WITHOUT_BF, CAP_WIN_MULTIPLIER | provisional_pending_math_validation | Needs calibrated cap proof. |
| Feature flags | freeSpinsEnabled, featureModesEnabled, jackpotEnabled | planning_candidate | Jackpot false by default. |
| History flags | historyEnabled, vabsEnabled, lasthandEnabled | planning_candidate | Deterministic replay preferred. |
