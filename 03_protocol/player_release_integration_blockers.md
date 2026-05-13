# Player Release Integration Blockers

Status: release-to-players is blocked.

## Release Readiness Decision Table

| Work item | Decision | Reason | Required next evidence |
|---|---|---|---|
| Can MathModelDesigner run now? | YES_WITH_LIMITS | RTPs, volatility, bet range, coin ladder, and protocol boundaries are known. Runtime owner is not fully proven, so math must be design/simulation only. | Math package, simulations,
RTP/volatility/max-win reports, backend integration assumptions marked. |
| Can GameClientBuilder run now? | NO_BLOCKED | Math package and approved replacement art are missing; runtime lane is a candidate but `new-games-server` and `@gamesv1/core-protocol` remain uninspected. | Completed math package, approved
art direction/replacement plan, explicit client lane decision, core protocol/new-games server source path. |
| Can GameServerRegistrar run now? | NO_BLOCKED | No 8001 registration inputs exist; `scn` serializer/config pipeline is missing; client path/math package unknown. | Math/client outputs, exact registration record plan,
serializer/import/admin tool, rollback design. |
| Can WalletAndLaunchTester run now? | NO_BLOCKED | 8001 runtime endpoints and registration do not exist; raw secrets intentionally unavailable. | Mock fixtures, local ignored secret reference or fake fixture PASS_KEY, generated
registration/dev route, client build. |
| Can release-to-players be considered yet? | NO_BLOCKED | Assets are scaffold-only and blocked; math unapproved; client not built; registration not generated; wallet/launch/RTP tests not run. | Completion of all later skills and
RTPAndReleaseAuditor approval. |

## Blocking Items

### Runtime / Source

- `new_games_server_source_path_missing`: 7001 docs reference `new-games-server`, but this sprint did not have that explicit source path.
- `core_protocol_package_not_inspected`: 7001/premium-slot import `@gamesv1/core-protocol`, but its root was not inspected.
- `game_8001_runtime_not_created`: no Little Gangster client/runtime exists yet.

### Math / Result

- `math_result_ownership_unknown`: WebGS internal bridge is proven for wallet/session/history, but final slot RNG/result owner is not proven.
- `math_package_missing`: no Little Gangster math package exists yet.

### Registration

- `game_8001_registration_missing`: no 8001 game/bank/template records exist.
- `scn_serializer_missing`: no safe serializer/config-generation tool verified for binary `scn`.
- `rollback_missing`: no registration rollback artifacts exist.

### Assets / Release

- `scaffold_assets_block_release`: 29 scaffold/reference assets remain blocked from release.
- `approved_release_assets_missing`: replacement/approved asset manifest does not exist.

### Tests / Compliance

- `wallet_launch_tests_missing`: no 8001 wallet/launch tests.
- `rtp_validation_missing`: no Little Gangster RTP simulation/audit.
- `client_requirements_gates_missing`: no final Game Client Requirements validation.

## Integration Boundary Reminders

- BSG Common Wallet is wallet/casino protocol only.
- Wallet layer approves/records bet, win, refund, and balance. It does not generate slot outcomes.
- GS/new-games runtime must generate or obtain the game outcome before the client animates it.
- Browser client may animate and display outcomes but must not be authoritative for real-money RNG.
- Bet/result separation, idempotency, request counters, and refund/retry rules still apply.
