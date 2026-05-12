# Backend Adapter Output Contract

Status: DEFINED_FOR_FUTURE_IMPLEMENTATION_NOT_APPLIED.

The future adapter output must be a valid `/slot/v1` runtime envelope response with v0.3 render data nested under
`presentationPayload.gamePayload`.

## Required Output Groups

| Output group | Required content | Evidence label |
|---|---|---|
| Envelope | `ok`, `requestId`, `sessionId`, `requestCounter`, `stateVersion` | PROVEN_SCHEMA |
| Wallet | `balanceMinor`, `previousBalanceMinor`, `currencyCode`, cent/truncation flags | PROVEN_SCHEMA |
| Round | canonical `roundId`, `status`, `betMinor`, `winMinor`, `netEffectMinor`, `outcomeHash` | PROVEN_SCHEMA |
| Feature | `mode`, `remainingActions`, `nextAllowedActions`, `featureContext` | PROVEN_SCHEMA |
| Presentation generic fields | `featureMode`, `reelStops`, `symbolGrid`, `uiMessages`, `animationCues`, `audioCues`, `counters`, `labels` | PROVEN_SCHEMA |
| Game payload extension | `gameKey`, `schemaVersion`, `payload` | PROVEN_PATCHED_SCHEMA |
| Restore | unfinished-round flags, resume state version, opaque restore payload | PROVEN_SCHEMA |
| Idempotency/retry | duplicate/replay/retry policy | PROVEN_SCHEMA |
| History | replay/history records when endpoint is `gethistory` | PROVEN_SCHEMA_HISTORY |

## Little Gangster Payload Location

```json
{
  "presentationPayload": {
    "gamePayload": {
      "gameKey": "little-gangster",
      "schemaVersion": "v0.3",
      "payload": {}
    }
  }
}
```

Evidence label: PROVEN_BY_STRICT_FIXTURES.

All 24 strict fixtures use this location and validate against patched response schemas and v0.3 result schema.

## Separation Rules

- Wallet/accounting truth must remain in `wallet`, `round`, and backend accounting records, not inside
  `gamePayload`.
- Runtime recovery truth must remain in runtime persistence/restore/history records, while render recovery hints can
  be mirrored inside `gamePayload.payload.state_persistence`.
- Browser-owned authority fields must not be present.

