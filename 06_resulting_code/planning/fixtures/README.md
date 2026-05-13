# Little Gangster Fixture Planning Pack

Status: NON_PRODUCTION_PLANNING_ONLY.

This folder contains static renderer fixture requirements and JSON examples for Little Gangster v0.3 planning.

The fixtures are not production runtime proof. They are not backend implementation, wallet payloads, registration metadata, or release approval. The runtime owner for Little Gangster / 8001 remains unproven, and the v0.3 result API contract
remains unapproved for implementation.

The browser/client remains renderer-only. It must not generate production RNG, calculate authoritative wins, decide cap outcomes, mutate wallet/accounting state, or persist authoritative round state.

Fixture payloads prefer `presentationPayload.gamePayload` as a reusable game-specific presentation extension:

```json
{
  "gameKey": "little-gangster",
  "schemaVersion": "v0.3",
  "payload": {
    "...": "v0.3 render state"
  }
}
```

Fallback option: `presentationPayload.littleGangsterV03`, only if the runtime schema team rejects a generic `gamePayload` extension.

Both extension paths are pending schema review. Neither is approved for production implementation.
