# Current Registration Readiness

## 2026-05-15 Update - Lifecycle Wrapper Registration Dependencies

The lifecycle wrapper plan did not unblock registration. GameServerRegistrar generation remains blocked until settings dependencies are resolved for
`POSSIBLE_MODELS`, `RTP_WITHOUT_BF`, `BF_RTP`, `BF_RTP_MIN`, `BF_BETS`, `SD_KEYS`, FeatureKPI, CAP_WIN/MAX_WIN/POSSIBLE_MAX_WINS, GL bet fields,
language fields, FRB fields, roundFinishedHelper/endRoundSignature, and any required VABS/VBA URL fields.

Registration artifacts must not be generated in the next sprint unless explicitly approved after these dependencies are mapped.

## 2026-05-15 Update - Legacy GS Settings Audit

GameServerRegistrar generation remains blocked. Legacy GS source supports several required settings such as `POSSIBLE_MODELS`, `RTP_WITHOUT_BF`,
`RTP_MIN_WITHOUT_BF`, `RTP_MIN`, `MAX_WIN`, GL bet settings, possible lines, default line/bet settings, and FRB coin settings.

The inspected current GS core paths did not prove first-class registration support for `BF_RTP`, `BF_RTP_MIN`, `BF_BETS`, or `SD_KEYS` under those
exact names. These require explicit mapping or current-GS registration proof before generation. CAP_WIN/POSSIBLE_MAX_WINS mapping also remains
planning-only and blocked.




## 2026-05-15 Update - Adapter Representation Planning

Backend adapter representation planning now includes the approved-for-planning 100x bonus-buy payload and VABS/Lasthands/history fields. Registration
generation remains blocked until runtime validation, wallet/accounting tests, VABS/Lasthands/history tests, tail/max-win confirmation, and
product/release gates are complete.

## 2026-05-14 Update - Bonus-Buy 100x Product Decision

Option A was selected for 100x bonus buy: approved for implementation planning only. Future registration planning may represent 100x as a candidate
with separate BF_RTP/BF_RTP_MIN fields, but GameServerRegistrar generation/apply remains blocked. 125x and 150x remain blocked.

## 2026-05-14 Update - Bonus-Buy 100x Registration Impact

Bonus-buy 100x is ready for product approval review, but registration generation remains blocked. BF_BETS standard candidate is 100x. BF_RTP and
BF_RTP_MIN are planning-only validation-backed values and remain separate from RTP_WITHOUT_BF and RTP_MIN_WITHOUT_BF. 125x and 150x are not included
in registration now.

Registration generation allowed: false.

Generated: 2026-05-14T11:02:16.092089+00:00
Status: registration_generation_blocked

## Summary

GS registration generation remains blocked. Registration artifacts must not be generated yet.

## Ready For Planning Only

- Base 3x3 RTP/volatility profile matrix exists.
- Base train gate passed: 9 / 9 profiles within +/-2%.
- Validation gate passed: 9 / 9 profiles within +/-2%.
- Operator-selectable profiles are represented by `mathProfileId`, not arbitrary runtime RTP/volatility values.

## Not Ready For Generation

- `BF_RTP` and `BF_RTP_MIN` are not final.
- Current bonus-buy 100x/125x/150x candidates are unacceptable.
- Bonus-buy v2 is draft-only and inactive.
- POSSIBLE_MAX_WINS is planning-only.
- CAP_WIN_MULTIPLIER / 10,000x cap was not empirically hit.
- `max_win_tail_frequency_unproven` remains active.
- VABS/Lasthands runtime tests are missing.
- Backend adapter is not implemented.

## Registration Decision

GameServerRegistrar generation allowed: false.

Registration may continue as metadata planning only. It must not import executable math and must not generate artifacts until bonus-buy, tail/max-win,
runtime/history, and approval gates are resolved.

## Backend Adapter Apply Update - 2026-05-15

Backend adapter payload representation exists in Staging for planning/testing only. Registration generation remains blocked.

Registration blockers still active:
- BF_RTP/BF_RTP_MIN values remain planning/provisional, not certification-final;
- 100x bonus buy still requires runtime validation, wallet/accounting tests, and VABS/Lasthands/history tests;
- 125x/150x premium/super tiers remain blocked;
- max-win/tail confirmation remains pending;
- GameServerRegistrar generation/apply is not allowed;
- release approval remains false.

## 2026-05-15 Update - Lifecycle Wrapper Source Planning

Lifecycle wrapper source planning did not unblock registration. GameServerRegistrar generation remains blocked.

Registration-impacting blockers still active:
- `POSSIBLE_MODELS` mapping must be finalized;
- `RTP_WITHOUT_BF`, `BF_RTP`, and `BF_RTP_MIN` must remain separate;
- `BF_BETS` standard 100x planning value is not a generated artifact;
- `SD_KEYS` and FeatureKPI mapping remain unresolved;
- CAP_WIN/MAX_WIN/POSSIBLE_MAX_WINS are not final;
- GL bet settings and VABS/VBA URL requirements remain unresolved.

No registration artifacts were generated.

## 2026-05-15 Update - Lifecycle Wrapper Apply

Lifecycle wrapper implementation was applied in Staging source for guarded 8001 runtime planning/testing only. Registration generation remains
blocked.

Registration-impacting blockers still active:
- VABS/VBA/Lasthands visual history route implementation remains pending;
- wallet/launch/history runtime tests remain pending;
- 100x bonus buy is still planning-only, not release-approved, and not certified;
- BF_RTP/BF_RTP_MIN values remain planning/provisional, not final certification values;
- 125x/150x premium/super tiers remain blocked;
- GameServerRegistrar generation/apply is not allowed;
- release approval remains false.

No registration artifact was generated.

## 2026-05-15 Update - GS Wallet/Config Responsibility Audit

GameServerRegistrar generation remains blocked. The GS responsibility audit proved that
wallet/config responsibility is BankInfo/current-GS driven, not browser/client driven.

Registration-impacting blockers still active:
- wallet manager/source bank mapping must be proven;
- common-wallet request client/auth/balance/wager/refund field mapping must be proven
  or inherited from a proven bank/template;
- refund/rollback support for 8001 remains unproven;
- VABS/VBA/history URL and BO/CM route config field shape remains unproven;
- durable history storage source for 8001 remains unproven;
- GameServerRegistrar must not generate fields from runtime/client assumptions.

No registration artifact was generated.
