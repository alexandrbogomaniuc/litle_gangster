# RTP Model Flexibility Matrix

Status: planning audit.

Principle: Little Gangster must not hardcode a single RTP model. Registration/runtime/math must support 96, 94, and 92 model variants, while final simulation evidence remains pending.

| Topic | RTP 96 | RTP 94 | RTP 92 | Owner | Blocker |
| --- | --- | --- | --- | --- | --- |
| Model ID mapping | placeholder `rtp_96` | placeholder `rtp_94` | placeholder `rtp_92` | math/config | final model ids pending |
| Bank/operator selection | selectable by config | selectable by config | selectable by config | registration/runtime | operator selection proof pending |
| Registration display RTP | 96 display value | 94 display value | 92 display value | GameServerRegistrar later | generation blocked |
| Actual math RTP | simulated 96 target | simulated 94 target | simulated 92 target | MathModelDesigner | simulation pending |
| RTP_MIN | model-specific min | model-specific min | model-specific min | math/config | min policy pending |
| RTP without bonus buy | required | required | required | math model | simulation pending |
| RTP_MIN_WITHOUT_BF | required | required | required | math model | simulation pending |
| BF_RTP | required if bonus buy enabled | required if bonus buy enabled | required if bonus buy enabled | math model | bonus_buy_cost_ev_pending |
| BF_RTP_MIN | required if bonus buy enabled | required if bonus buy enabled | required if bonus buy enabled | math model | bonus_buy_cost_ev_pending |
| Volatility | model-specific report | model-specific report | model-specific report | simulation | simulation pending |
| Feature contribution | model-specific report | model-specific report | model-specific report | simulation | exact mode rules pending |
| Bonus-buy EV | model-specific report | model-specific report | model-specific report | simulation | bonus_buy_cost_ev_pending |
| Max win | likely shared pending proof | likely shared pending proof | likely shared pending proof | math config | final confirmation pending |
| Cap multiplier | candidate global 10000x | candidate global 10000x | candidate global 10000x | math config | final signoff pending |
| Future additional RTP model | add model id/config row | add model id/config row | add model id/config row | math/config | requires simulation |

Backend adapter must receive:

- active RTP model id;
- math version;
- RTP display/config fields;
- model-specific max-win/cap metadata;
- model-specific feature/bonus/jackpot status;
- authoritative result generated under that model.

GameServerRegistrar must later generate:

- registration display RTP fields;
- possible model list;
- current/default model;
- min/max bet and denomination metadata;
- bonus-buy and jackpot feature flags;
- max win/cap metadata;
- no executable math import.

Avoid hardcoding:

- Do not hardcode 96 as the only model.
- Do not hardcode bonus-buy RTP as equal to base RTP.
- Do not hardcode a line-based bet formula for a cluster game.
- Do not hardcode jackpot enabled.

Validation keyword coverage:

- volatility.
- bonus-buy EV.
- cap multiplier.
