# Runtime API Test Matrix

Status: TEST PLAN ONLY. No wallet/API calls were executed.

| Area | Test intent | Expected evidence before execution | Status |
|---|---|---|---|
| bootstrap | Confirm Little Gangster launch receives session/config/runtime policy. | Selected runtime API and 8001 route. | blocked |
| opengame | Confirm initial envelope contains wallet, round, feature, presentation, restore, idempotency, retry. | Runtime owner and envelope fixture. | blocked |
| playround | Confirm base spin returns authoritative backend result and v0.3 render payload. | v0.3 payload adapter. | blocked |
| featureaction | Confirm bonus buy/feature decisions use backend-owned outcomes. | Feature action contract and accounting boundary. | blocked |
| resumegame | Confirm unfinished round restoration preserves v0.3 state. | Recovery payload fixture. | blocked |
| gethistory | Confirm read-only history does not advance state and can replay v0.3 payload. | History/VABS contract. | blocked |
| closegame | Confirm close action keeps accounting separate and does not alter completed round. | Closegame contract. | blocked |

## Required Safety Assertions

- Browser does not generate production RNG or authoritative outcomes.
- Client-rendered fields come from backend/runtime payload.
- Wallet/accounting and rendering are validated separately.
- Raw secrets, full launch URLs, and private values are never written to reports.
