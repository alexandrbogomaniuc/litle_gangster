# RTP / Volatility Profile Validation Matrix

Created: 2026-05-13T08:55:01Z

| Check | Expected |
|---|---|
| RTP labels | exactly LOW, MEDIUM, HIGH |
| Volatility labels | exactly LOW, MEDIUM, HIGH |
| Profile count | 9 |
| RTP range | every profile between 92.00% and 99.00% |
| Profile identity | mathProfileId, registrationModelCode, runtimeProfileCode, historyProfileCode |
| Operator selection | pretested profiles only |
| Registration | metadata only, no executable math import |
| Runtime | backend-resolved profile identity included in result |
| History/VABS | math profile identity stored with replay payload |
| Client/browser | no profile mutation authority |
| Release | not approved until simulation and certification pass |

Current blockers: `volatility_profile_specific_simulation_pending`, `gs_profile_matrix_storage_unproven`, `bonus_buy_ev_pending`, `certification_pending`.
