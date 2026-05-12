# Presentation Payload Schema Extension Decision

Status: DECISION_RECOMMENDED_SCHEMA_CHANGE_REQUIRED.

## Decision

Recommend `presentationPayload.gamePayload` as the preferred future extension point.

Use `presentationPayload.littleGangsterV03` only as a fallback if the runtime/schema team rejects a reusable generic extension.

Do not hide v0.3 state inside `labels`, `counters`, or generic `animationCues` as the only data source.

## Current Schema Support

| Question | Answer | Evidence label |
|---|---|---|
| Does `PresentationPayloadSchema` allow unknown fields? | No. The core-protocol Zod schema is strict. | PROVEN_SCHEMA_BLOCKER |
| Can `presentationPayload.gamePayload` be added without schema change? | No, not for canonical strict validation. | BLOCKED_SCHEMA_CHANGE_REQUIRED |
| Can HTTP transport pass it without strict schema validation? | Likely yes, because the parser treats presentation payload as a record. That is not enough for approval. | LIKELY_TRANSPORT_PASS_THROUGH |
| Is a generic `gamePayload` compatible with current style? | It matches the practical `mathBridge` extension pattern, but must be formalized in core schema and mapper policy. | CANDIDATE_PATTERN |
| Is `littleGangsterV03` more realistic? | It is simpler for one game but less reusable. Keep it as fallback only. | CANDIDATE_FALLBACK |

## Required Schema Shape For Review

```json
{
  "presentationPayload": {
    "featureMode": "BASE",
    "reelStops": [[1, 2, 3, 4, 5]],
    "symbolGrid": [[1, 2, 3, 4, 5, 6]],
    "uiMessages": [],
    "animationCues": [],
    "audioCues": [],
    "counters": [],
    "labels": {},
    "gamePayload": {
      "gameKey": "little-gangster",
      "schemaVersion": "v0.3",
      "payload": {}
    }
  }
}
```

## Source Files Likely To Change

| File | Needed change | Evidence label |
|---|---|---|
| `Gamesv1/packages/core-protocol/src/schemas.ts` | Add reviewed `gamePayload` field or equivalent to `PresentationPayloadSchema`. | REQUIRED_SCHEMA_CHANGE |
| `Gamesv1/packages/core-protocol/src/IGameTransport.ts` | Document or type the game extension if the interface should become explicit. | OPTIONAL_TYPE_HARDENING |
| `Gamesv1/packages/core-protocol/src/http/GsHttpRuntimeTransport.ts` | Add explicit parsing/validation only if runtime team wants transport-level enforcement. | OPTIONAL_TRANSPORT_HARDENING |
| `Gamesv1/packages/ui-kit/src/shell/presentation/PremiumPresentationMapper.ts` | Preserve/pass through the game extension or document that game-specific clients read it before/after shared mapping. | REQUIRED_CLIENT_MAPPER_POLICY |
| `new-games-server/src/index.ts` | Future Little Gangster branch should build the v0.3 `gamePayload`. | REQUIRED_ADAPTER_IMPLEMENTATION_LATER |
| `Gamesv1/games/8001/...` | Future client-specific mapper should consume `gamePayload` and map to scene/object states. | REQUIRED_8001_CLIENT_LATER |

## Gate

No backend adapter implementation or GameClientBuilder implementation may start until the extension is reviewed and the schema-change path is approved.
