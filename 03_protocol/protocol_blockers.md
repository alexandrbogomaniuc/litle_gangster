# Protocol Blockers

## Critical / Must Resolve Before Build Or Registration

| ID | Status | Severity | Blocker | Needed to unblock |
|---|---|---|---|---|
| `core_protocol_package_not_inspected` | open | high | `@gamesv1/core-protocol` is imported by 7001/premium-slot runtime, but its package root was not an explicit allowed path in this sprint. | User must provide explicit path to the core
protocol package or allow inspection of the relevant package root. |
| `slot_v1_server_implementation_partial` | open | high | Browser client and runbook prove `/slot/v1/*` operation names, but server-side endpoint implementation was not fully mapped. | Provide explicit new-games server/API source path for
targeted inspection. |
| `game_8001_registration_missing` | open | high | No game 8001 registration artifacts exist yet. | Run GameServerRegistrar later after MathModelDesigner and GameClientBuilder produce required inputs. |
| `scn_serializer_missing` | open | high | `RCasinoSCKS.bankinfocf.scn` is a serialized binary config and cannot be generated safely without a real serializer/tool. | Provide serializer/tool or use approved config-generation pipeline. |
| `math_result_ownership_unknown` | open | high | RNG/result ownership for future 8001 is unknown. | Run MathModelDesigner and later runtime integration validation. |

## Wallet / Secret Blockers

| ID | Status | Severity | Blocker | Needed to unblock |
|---|---|---|---|---|
| `pass_key_value_intentionally_unavailable` | open by design | future wallet-test blocker | Raw PASS_KEY values are not stored and must not be requested in chat. | WalletAndLaunchTester must use a local ignored secret reference or fake
fixture PASS_KEY. |
| `test_token_values_intentionally_unavailable` | open by design | future launch-test blocker | Test user/token raw values are not stored. | Use local ignored secret reference or approved fixture in WalletAndLaunchTester. |
| `wallet_client_implementation_partial` | open | medium | Wallet parameter constants and BSG docs are mapped, but exact local request builder/retry code was not fully mapped. | Targeted inspection of wallet client implementation path, or
fixture tests against mock EC. |
| `cwm_type_for_8001_unknown` | open | medium | Future game/bank `CWM_TYPE` is unknown. | Resolve in GameServerRegistrar/WalletAndLaunchTester from generated config. |

## Launch / Runtime Blockers

| ID | Status | Severity | Blocker | Needed to unblock |
|---|---|---|---|---|
| `legacy_vs_new_games_stack_split` | open | medium | Uploaded docs describe legacy Webpack/Vue/PIXI template; explicit 7001 paths use Vite/PIXI v8/new-games slot runtime. | GameClientBuilder must choose approved target path and record
user/design decision. |
| `window_game_config_not_verified_in_live_template` | open | low | Uploaded docs mention `window.gameConfig`; live JSP inspected exposes `getParams()` and path helpers instead. | Inspect exact target launch template used by future 8001
build. |
| `demo_fallback_not_release_contract` | open | medium | 7001 source can use demo/provisional runtime fallback; this is not release proof. | Later build/test must disable or gate dev fallback for release. |

## Asset / Release Blockers That Remain In Force

| ID | Status | Severity | Blocker | Needed to unblock |
|---|---|---|---|---|
| `scaffold_assets_block_release` | open | release blocker | 29 captured reference assets are internal scaffold only and blocked from release. | Explicit ownership approval or replacement by approved original/licensed assets. |
| `release_not_approved` | open | release blocker | No release audit has run. | Complete all later workflow skills and RTP/release audit. |

## Not Blockers For MathModelDesigner

The following are sufficient for starting MathModelDesigner:

- Target RTPs are known: `96.0`, `94.0`, `92.0`.
- Volatility target is known: high.
- Bet range is known: min `0.20`, default `1.00`, max `100.00`.
- Coin denominations are known from explicit config evidence.
- Protocol layers and wallet hash rules are separated enough for math work.

MathModelDesigner must still not generate final math from screenshots alone and must not assume runtime ownership.
