# Math Config Refinement Blockers

This refinement narrows the next blockers but does not remove implementation gates.

| Blocker | Severity | Blocks | Next action |
| --- | --- | --- | --- |
| `large_scale_rtp_calibration_pending` | High | final RTP, certification, release | Run calibrated 1M/10M+ local simulations after model approval. |
| `bonus_buy_cost_ev_pending` | High | bonus buy finalization, registrar config | Decide cost multipliers and prove EV by simulation. |
| `final_symbol_weights_pending_math_calibration` | High | production math | Tune symbol weights against RTP/volatility targets. |
| `final_cluster_paytable_pending_rtp_calibration` | High | production math | Tune cluster pays with feature contribution targets. |
| `free_spin_counts_retrigger_rules_pending` | Medium | feature math | Product/math decision for retriggers and mode differences. |
| `jackpot_product_decision_pending` | Medium | jackpot support | Keep disabled by default until product confirms. |
| `vabs_screenshot_requirement_unverified` | Medium | history/replay compliance | Confirm whether deterministic replay is sufficient. |
| `runtime_owner_8001_unproven` | High | backend adapter implementation | Approve/create authoritative server-side owner later. |

Implementation remains blocked until explicit approval.
