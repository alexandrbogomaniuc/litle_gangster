# Runtime Payload Output Requirements

The future adapter output must be a valid `/slot/v1` runtime envelope response.

Required presentation output:

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

Payload content:

- v0.3 render state.
- cascade steps.
- removed cells.
- dropped/refilled cells.
- golden-square overlays.
- rainbow activations.
- coin reveals.
- special reveals.
- feature mode state.
- bonus-buy state.
- max-win cap event.
- win ratio and tier.
- round completion state.
- reconnect/recovery state.

Outside gamePayload:

- wallet/accounting fields.
- transport/session metadata.
- runtime envelope status.
- history endpoint metadata as required by platform.

Rules:

- `gamePayload` is reusable and game-specific inside `payload`.
- UI-kit should preserve it without interpretation.
- Browser renders it but does not author it.

