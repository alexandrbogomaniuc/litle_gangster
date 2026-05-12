# Presentation Payload Extension Review

Status: EXTENSION_REQUIRED.

## Current Generic Payload

Staging source proves a generic `presentationPayload` with these root fields:

- `featureMode`
- `reelStops`
- `symbolGrid`
- `uiMessages`
- `animationCues`
- `audioCues`
- `counters`
- `labels`

Evidence:

- `Gamesv1/packages/core-protocol/src/schemas.ts`: PROVEN_GENERIC, strict schema.
- `Gamesv1/packages/ui-kit/src/shell/presentation/PremiumPresentationMapper.ts`: PROVEN_GENERIC_MAPPER.
- `Gamesv1/docs/gs/fixtures/playround.response.json`: PROVEN_GENERIC fixture shape.

## v0.3 Payload Need

Little Gangster v0.3 requires render state for:

- cascade steps, removed cells, dropped cells, new symbols, clusters;
- golden-square before/after/events;
- rainbow activation;
- coin and special reveal events;
- feature modes and bonus buy state;
- max-win cap, pre-cap, capped values;
- `winRatio`, `winTier`;
- round completion;
- state persistence and reconnect.

These fields are not part of the current generic root presentation payload.

## Direct Carry Decision

Directly placing the full v0.3 result schema at the root of `presentationPayload` is BLOCKED_PENDING_SCHEMA_REVIEW.

Reason:

- the core protocol schema is strict;
- existing shared mapper expects reel/grid/counter/message/audio/label fields;
- v0.3 has nested feature/cascade/state fields not represented by the generic schema;
- no Little Gangster adapter proves a valid extension point yet.

## Candidate Extension Options

| Option | Status | Notes |
|---|---|---|
| Add `presentationPayload.littleGangsterV03` | RECOMMENDED_FOR_REVIEW | Clean game-specific render payload; requires schema update/review. |
| Add `presentationPayload.gamePayload` | CANDIDATE | More generic extension point; requires schema update/review. |
| Map all v0.3 data into existing `labels`/`counters`/`animationCues` | DO_NOT_USE | Obscures authoritative render state and is brittle. |
| Put v0.3 outside `presentationPayload` | CANDIDATE_ONLY | Would require a new envelope field and transport review. |

## Review Gate

Before implementation, the backend/runtime team must approve one extension path and update or confirm all validators, fixtures, and mappers that enforce the presentation schema.

