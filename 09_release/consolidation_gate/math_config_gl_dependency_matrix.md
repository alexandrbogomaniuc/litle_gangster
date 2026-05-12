# Math Config GL Dependency Matrix

Status: strict audit matrix.

Cluster-game rule: Little Gangster is a 6x5 cluster game. Fixed-line fields must be treated as legacy compatibility/display metadata unless current GS registration proves otherwise. Do not blindly use a fixed-line bet formula.

| Field | Source | Owner | Dependency | Registration field | Runtime field | Math model field | VABS/history field | Blocker status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| GL_MIN_BET_DEFAULT | Mantis checklist / bet config | registration config | coin/bet model | min bet metadata | selected bet validation | minimum stake | bet | needs final cluster mapping |
| GL_MAX_BET_DEFAULT | Mantis checklist / bet config | registration config | operator limits | max bet metadata | selected bet validation | maximum stake | bet | needs final cluster mapping |
| GL_DEFAULT_BET | Mantis checklist | registration config | default UI bet | default bet metadata | opengame defaults | default stake | initial bet | needs final cluster mapping |
| GL_DEFAULT_BET_DEFAULT | Mantis checklist | registration config | fallback default | fallback default bet | opengame defaults | default stake fallback | initial bet | needs final cluster mapping |
| GL_BF_MAX_BETS | Mantis checklist | registration/math config | bonus-buy cost model | buy-feature max bet metadata | featureaction purchase validation | max eligible bonus-buy bet | purchase state | blocked by bonus_buy_cost_ev_pending |
| BF_BETS | Mantis checklist | registration/math config | bonus-buy options | buy-feature bet options | featureaction purchase options | purchase cost options | bonus-buy state | blocked by bonus_buy_cost_ev_pending |
| DEFCOIN | Mantis checklist / denominations | registration config | coin denominations | default coin | selected denomination | stake unit | bet display | needs final bank mapping |
| POSSIBLE_LINES | Mantis fixed-line legacy | compatibility metadata | cluster equivalent | legacy lines field if required | none or display | not a line game | not needed | unresolved if GS requires legacy value |
| LINES_COUNT | Mantis fixed-line legacy | compatibility metadata | cluster equivalent | legacy line count | none or display | not a line game | not needed | unresolved if GS requires legacy value |
| DEFAULTNUMLINES | Mantis fixed-line legacy | compatibility metadata | cluster equivalent | default lines fallback | none or display | not a line game | not needed | unresolved if GS requires legacy value |
| POSSIBLE_BETPERLINES | Mantis fixed-line legacy | compatibility metadata | cluster equivalent | legacy bet-per-line | none or display | cluster base bet metadata | bet | unresolved cluster equivalent |
| DEFAULTBETPERLINE | Mantis fixed-line legacy | compatibility metadata | cluster equivalent | legacy default bet per line | none or display | cluster base bet metadata | bet | unresolved cluster equivalent |
| RTP | Mantis checklist / math targets | math config plus registration display | RTP model | display/config RTP | model selected | target RTP | model id | model outputs pending |
| RTP_MIN | Mantis checklist | math config plus registration display | min RTP policy | display/config min RTP | model selected | min allowed RTP | model id | model outputs pending |
| RTP_WITHOUT_BF | Mantis checklist | math config | bonus-buy split | display/config RTP without buy feature | model selected | base RTP excluding bonus-buy | model id | simulation pending |
| RTP_MIN_WITHOUT_BF | Mantis checklist | math config | bonus-buy split | display/config min RTP without buy feature | model selected | min base RTP excluding bonus-buy | model id | simulation pending |
| BF_RTP | Mantis checklist | math config | bonus-buy EV | display/config bonus-buy RTP | purchase validation | bonus-buy RTP | purchase state | blocked by bonus_buy_cost_ev_pending |
| BF_RTP_MIN | Mantis checklist | math config | bonus-buy EV minimum | display/config min bonus-buy RTP | purchase validation | min bonus-buy RTP | purchase state | blocked by bonus_buy_cost_ev_pending |
| POSSIBLE_MODELS | Mantis checklist / project target | registration config | 96/94/92 support | model list | rtpVariant | RTP variant list | model id | needs final model id mapping |
| CURRENT_MODEL | Mantis checklist | runtime/operator config | operator selection | default model | rtpVariant/current model | active RTP model | model id | needs bank/operator selection proof |
| POSSIBLE_MAX_WINS | Mantis checklist | math/registration metadata | cap and theoretical max | possible max win display | cap fields | max possible win | cap event | needs model-specific confirmation |
| POSSIBLE_MAX_WINS_WITHOUT_BF | Mantis checklist | math metadata | bonus-buy split | max win without buy feature | cap fields | base max possible win | cap event | simulation pending |
| CAP_WIN_MULTIPLIER | Mantis checklist / v0.3 | math owner | cap policy | cap metadata | max_win_cap | 10000x cap | cap reached/pre-cap/capped | needs final signoff |
| VOLATILITY | Mantis checklist / math target | math config plus display | simulation output | volatility metadata | rtpVariant metadata | volatility metric | model id | simulation pending |
| isFrb | Mantis checklist | registration/runtime config | FRB decision | FRB enabled flag | promo/free-bet context | not core math unless enabled | promo history | FRB scope unverified |
| FRB_COIN | Mantis checklist | registration/runtime config | FRB decision | FRB coin metadata | promo/free-bet context | stake override if enabled | promo history | FRB scope unverified |
| GAME_WITH_PROGRESS | Mantis checklist | registration/runtime config | progress feature decision | feature flag | progress state if any | progress hook if enabled | progress state | product decision pending |
| GAME_WITH_DOUBLE_UP | Mantis checklist | registration/math config | double-up decision | feature flag false | none | double-up out of scope | none | disabled by design |
| DOUBLE_UP_DISABLED | project decision | registration/math config | double-up decision | true/disabled metadata | none | double-up disabled | none | resolved unless product changes |
| KEY_SINGLE_GAME_ID_FOR_ALL_PLATFORMS | Mantis checklist | registration config | platform identity | single game id flag | game id | none | game id | verify current GS support |
| SD_KEYS | Mantis checklist | registration/config | key namespace | config keys only | none | none | none | verify support and redact secrets |
| S_VERSION | Mantis checklist | registration/runtime config | schema/content version | version metadata | schemaVersion | math/schema version | history schema version | needs final version policy |
| RELEASE_TIME | Mantis checklist | release metadata | release gate | release timestamp | none | none | release metadata | release blocked |
| title / game name | registration docs | registration config | product naming | title/name | gameName | none | display name | needs final product signoff |
| gameId | manifest / registration audit | registration/runtime | 8001 routing | game id | gameId | game id | game id | 8001 registration missing |
| bankId | manifest/history docs | registration/wallet boundary | bank routing | bank id | launch/session context | none | session context | bank/source must be final |
| subCasinoId | manifest/history docs | registration/wallet boundary | operator routing | sub-casino id | launch/session context | none | session context | verify final value |
| coin denominations | manifest / bet config | registration/math config | stake ladder | coin list | selected denomination | stake units | bet display | final cluster mapping needed |
| bonus-buy cost | bonus-buy module | math config | purchase EV | buy-feature metadata | featureaction cost | cost multiplier | purchase state | bonus_buy_cost_ev_pending |
| bonus-buy EV | bonus-buy module | math config | simulation | buy-feature RTP metadata | purchase model | bonus-buy contribution | purchase state | bonus_buy_cost_ev_pending |
| jackpot enabled | jackpot module | product/math config | product decision | jackpot flag | jackpot state if enabled | jp_enabled false by default | jackpot event if any | jackpot_product_decision_pending |
| jackpot contribution | jackpot module | jackpot/accounting | JP accounting | contribution metadata if enabled | jackpot accounting reference | JP RTP contribution | jackpot event | pending product/accounting |
| jackpot hit fields | jackpot module | jackpot/runtime | JP event model | jackpot metadata | jackpot event | JP award model | jackpot history | pending product/accounting |
| free spins enabled | v0.3 design | math config | feature rules | feature flag | feature state | free/feature spin loop | feature state | exact flow pending |
| feature modes enabled | v0.3 design | math config | mode rules | feature mode flag | feature mode state | mode rules | mode state | exact mode EV pending |
| autoplay/turbo/settings | donor settings / client config | client/runtime config | UI behavior | settings metadata if needed | timing/display only | no math authority | none | autoplay stop conditions unobserved |
| history/VABS enabled | protocol/history docs | runtime/history config | history storage | history flag/package if required | gethistory/history group | none | replay payload | exact 8001 mapping unproven |
| Lasthand replay enabled | protocol/history docs | runtime/history config | replay storage | lasthand flag/package if required | gethistory/history group | none | replay payload | exact 8001 mapping unproven |

Audit conclusion:

- Registration metadata values are separable from executable math.
- Runtime payload values are separable from registration metadata.
- Wallet/accounting values are separable from animation/presentation data.
- The blocking gap is not matrix coverage; it is final values, ownership, and proof.

