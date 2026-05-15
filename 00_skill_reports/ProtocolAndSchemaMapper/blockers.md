# ProtocolAndSchemaMapper Blockers

## Open Blockers

| ID | Severity | Description | Needed to unblock |
|---|---|---|---|
| `core_protocol_package_not_inspected` | high | `@gamesv1/core-protocol` is imported by 7001 and premium-slot runtimes, but its package root was not
an explicit allowed path. | Provide explicit package path or allow targeted inspection. |
| `slot_v1_server_implementation_partial` | high | `/slot/v1/*` operation names are mapped from client/runbook, but server-side endpoint
implementation was not fully mapped. | Provide explicit new-games server/API source path. |
| `game_8001_registration_missing` | high | No 8001 registration record/artifacts exist yet. | Run GameServerRegistrar later after math/client/build
inputs exist. |
| `scn_serializer_missing` | high | `RCasinoSCKS.scn` serialized binary config cannot be generated safely without real tooling. | Provide
serializer/tool or approved config-generation pipeline. |
| `math_result_ownership_unknown` | high | RNG/result ownership for 8001 is not proven. | Resolve through MathModelDesigner and later runtime
validation. |
| `pass_key_value_intentionally_unavailable` | future wallet-test blocker | Raw PASS_KEY values are intentionally not stored. | Use local ignored
secret reference or fake fixture in WalletAndLaunchTester. |
| `test_token_values_intentionally_unavailable` | future launch-test blocker | Test user/token raw values are intentionally not stored. | Use local
ignored secret reference or fake fixture in WalletAndLaunchTester. |
| `scaffold_assets_block_release` | release blocker | Captured reference assets remain scaffold/internal-only and blocked from release. | Replace or
explicitly approve assets before release. |

## Not Blocking MathModelDesigner

- BSG wallet hash orders are mapped.
- Target RTPs, volatility, bet range, and coin values are known.
- Protocol layers are separated enough to avoid confusing wallet protocol with browser runtime.

MathModelDesigner must still not generate final math from screenshots alone.
