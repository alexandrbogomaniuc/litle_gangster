# Presentation Payload Extension Options

Status: PENDING_SCHEMA_REVIEW.

## Preferred Option

Use `presentationPayload.gamePayload`:

```json
{
  "gameKey": "little-gangster",
  "schemaVersion": "v0.3",
  "payload": {
    "...": "v0.3 render state"
  }
}
```

Reason: this creates one reusable extension point for future games while keeping generic `/slot/v1` envelope fields stable.

## Fallback Option

Use `presentationPayload.littleGangsterV03` only if the runtime schema team rejects the generic extension.

## Rejected Option

Do not squeeze v0.3 fields into `labels`, `counters`, or generic `animationCues` as the only data source. That would hide authoritative render state and make replay/reconnect brittle.

## Boundary

The extension carries renderer state only after backend/runtime has produced it. The browser does not author v0.3 outcomes, wins, feature states, wallet state, history, or registration metadata.
