# Current GS Registration / Runtime Boundary

## Boundary Summary

| Layer | Responsibility | Evidence status | Notes |
|---|---|---|---|
| Registration/config | Game ID, game name, template record, bank/currency assignment, route/client/API URLs, RTP display/config, volatility/max-win/cap metadata, feature flags. | PROVEN | Current GS cache/persister code and runtime exports
support this. |
| Executable runtime | Generates or obtains round outcomes, owns state transitions, applies math rules, exposes result envelope. | CANDIDATE | New Games server currently generates provisional results for sample flows, but Little Gangster
owner is not final. |
| Wallet/accounting | Session validation, reserve, settle, balance, history persistence bridge. | PROVEN | WebGS internal API exposes `/session/validate`, `/wallet/reserve`, `/wallet/settle`, `/history/write`, `/history/read`. |
| Client rendering | Sends selected bet/feature action and renders server/backend result payload. | PROVEN as client rule | Gamesv1 core protocol treats browser as transport/presentation; browser result authority remains forbidden. |
| Math/result generation | v0.3 math package should define result schema and rules; consumed by the proven backend/runtime owner, not by registration unless source later proves otherwise. | LIKELY with blocker | No registration math import
found. |

## Responsibilities By Layer

Registration should configure:

- `gameId`
- game title/name
- bank/casino assignment
- client path or New Games client URL
- API/runtime URL references
- RTP display values and model IDs
- bet range and denomination metadata
- feature availability flags
- cap/max-win display/config metadata
- `roundFinishedHelper` / `endRoundSignature` only if selected lane requires them

Registration should not own:

- real-money RNG
- cluster/cascade math evaluation
- feature-mode math
- final win generation
- browser rendering state beyond config hints

Runtime should own:

- RNG/result generation
- round state
- cascade/golden-square/rainbow/coin-reveal evaluation
- max-win cap application
- feature mode transitions
- wallet reserve/settle ordering or a lane-equivalent contract

## Gamesv1 Assumptions Still Unproven

- That Little Gangster must use `slot-browser-v1`.
- That Crazy Rooster 7001 is a direct template.
- That premium-slot is a direct template.
- That current GS registration alone imports math.
- That the final result owner is definitely New Games server rather than classic GS, game-specific server package, or GS processor.

Current stance: Gamesv1/New Games is the strongest candidate direction from Staging evidence, but not final.
