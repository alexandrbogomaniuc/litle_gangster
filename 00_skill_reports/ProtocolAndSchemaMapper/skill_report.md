# ProtocolAndSchemaMapper Skill Report

Date/time: 2026-05-08T07:44:03+0100

## Status

`partial_sufficient_for_math_handoff`

Protocol mapping succeeded for BSG Common Wallet, wallet hash rules, launch/template separation, and enough client/runtime/config boundary mapping to
start MathModelDesigner. It remains partial for the new-games core protocol package, server-side `/slot/v1/*` implementation, and future 8001
registration details.

## Inputs Read

- `[REDACTED_LOCAL_PATH]
- `[REDACTED_LOCAL_PATH]
- `[REDACTED_LOCAL_PATH]
- `[REDACTED_LOCAL_PATH]
- Suite reference summaries under `[REDACTED_LOCAL_PATH]
- `[REDACTED_LOCAL_PATH]
- `[REDACTED_LOCAL_PATH]
- `[REDACTED_LOCAL_PATH]
- Prior handoffs for ProjectCreator, AuthorizedReferenceResearcher, and ReferenceAssetInventory
- Sanitized reference research/network summaries and asset inventory CSVs as context only
- Explicit source paths from the prompt/project manifest

## Outputs Created

- `[REDACTED_LOCAL_PATH]
- `[REDACTED_LOCAL_PATH]
- `[REDACTED_LOCAL_PATH]
- `[REDACTED_LOCAL_PATH]
- `[REDACTED_LOCAL_PATH]
- `[REDACTED_LOCAL_PATH]
- `[REDACTED_LOCAL_PATH]
- `[REDACTED_LOCAL_PATH]
- `[REDACTED_LOCAL_PATH]
- `[REDACTED_LOCAL_PATH]
- `[REDACTED_LOCAL_PATH]
- `[REDACTED_LOCAL_PATH]
- `[REDACTED_LOCAL_PATH]
- `[REDACTED_LOCAL_PATH]
- `[REDACTED_LOCAL_PATH]
- `[REDACTED_LOCAL_PATH]
- `[REDACTED_LOCAL_PATH]

## Files Modified

- `[REDACTED_LOCAL_PATH]
- `[REDACTED_LOCAL_PATH]
- `[REDACTED_LOCAL_PATH]

## Key Findings

- BSG Common Wallet is XML wallet/casino protocol, not browser runtime protocol.
- BSG CW response roots remain `BSGSYSTEM`/`EXTSYSTEM`; JSON is not assumed for BSG CW.
- Launch/template routing is separate from browser runtime. `cwstartgamev2.do` authenticates and routes; it is not a Pixi bootloader.
- Legacy JSP shell reads `bankId`, `SID`, `gameId`, loads `version.json`, `validator.js`, `game.js`, and exposes `getParams()`/path helpers.
- New-games redirect passes `bankId`, `sessionId`, `gameId`, `gameIdNumeric`, `lang`, `mode`, `gameServerId`, `ngsApiUrl`, `gsInternalBaseUrl`, and
  `ngsContract=v1`.
- 7001 runtime uses `slot-browser-v1`, `GS_HTTP_RUNTIME`, request counters, idempotency keys, and `/slot/v1/*` operations.
- Bank 6275 and coin values were verified from explicit config export; URLs/secrets are redacted.
- Cassandra/config registration remains generate-only and partial. No CQL was generated or executed.

## Safety Results

- Raw secret values stored: no.
- Full donor URL stored: no.
- DB/Cassandra action executed: no.
- Donor gameplay investigated this sprint: no.
- Asset capture performed this sprint: no.
- Later workflow skills run: no.

## Next Recommended Skill

MathModelDesigner.

Reason: protocol boundaries, target RTPs, volatility, bet range, and coin denominations are mapped enough to begin math design. Remaining
runtime/registration blockers are explicit and do not block math modeling.
