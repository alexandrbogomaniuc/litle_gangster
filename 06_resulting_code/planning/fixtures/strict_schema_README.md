# Strict Schema Fixture Pack

Status: NON_PRODUCTION_STRICT_SCHEMA_VALIDATED.

This folder contains strict-schema-compatible candidate `/slot/v1` runtime envelope responses for Little Gangster v0.3 planning.

The strict variants are stored in `strict_schema_examples/` and use the same filenames as the original renderer-planning fixtures.

These fixtures are still non-production. They do not prove runtime owner, backend adapter implementation, wallet/accounting correctness, registration readiness, or release readiness.

Each strict fixture carries the v0.3 renderer payload through:

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

The non-production markers are preserved under `gamePayload.payload.state_persistence.fixture_metadata` so the payload remains compatible with the v0.3 result schema.

Validation summary:

- Strict fixture files created: 24
- Patched response-schema valid fixtures: 24
- v0.3 result-schema valid payloads: 24
- Backend adapter implementation allowed: false
- GameClientBuilder implementation allowed: false
