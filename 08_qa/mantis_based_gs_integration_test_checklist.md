# Mantis-Based GS Integration Test Checklist

Status: QA gate only; no tests executed.

## Test Areas

- Launch paths: guest, free, real, `cwguestlogin.do`, `cwstartgamev2.do`, startgame wrapper, new-games redirect, legacy fallback if applicable.
- Token/session/query redaction in logs and reports.
- `/slot/v1/bootstrap`, `/opengame`, `/playround`, `/featureaction`, `/resumegame`, `/gethistory`, `/closegame` if new-games lane is selected.
- Transaction equivalent for every paid spin, free spin, feature spin, bonus buy, collect, and zero/failed win state.
- Duplicate/idempotent retry and request counter mismatch.
- Reconnect/reload/resume while a round is pending.
- Max-win cap settlement.
- Wallet/accounting separation from browser animation.
- Error handling and translations.

## Safety

Use mock/safe fixtures unless a later sprint explicitly approves dev/stage endpoints and secret references. Do not call production wallet endpoints.

