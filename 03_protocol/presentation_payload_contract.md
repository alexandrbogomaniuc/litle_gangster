# Presentation Payload Contract

## Status

`presentationPayload` is PROVEN as the generic browser-visible rendering payload. The exact Little Gangster v0.3 payload is NOT_FOUND/BLOCKED until a runtime adapter is implemented or formally specified.

## Current Generic Schema

Current core protocol schema expects:

- `featureMode`
- `reelStops`
- `symbolGrid`
- `uiMessages`
- `animationCues`
- `audioCues`
- `counters`
- `labels`

The shared presentation mapper consumes those fields and maps them to UI-facing reel/counter/message/audio/animation structures.

## Existing Adapter Pattern

`new-games-server/src/index.ts` builds a Crazy Rooster presentation payload from provisional sample output. `premium-slot` then maps the runtime response through a presentation mapper. This proves the adapter pattern, not the Little Gangster adapter.

## v0.3 Compatibility Gap

Little Gangster v0.3 requires fields beyond the generic line/reel payload:

- cascade steps and per-step removed/dropped/refilled cells
- golden-square state before/after
- rainbow activation events
- coin and special reveal events
- feature mode state
- bonus-buy state
- max-win cap state
- winRatio/winTier
- round completion
- state persistence/reconnect hints
- animation hints

The current generic schema is strict. A Little Gangster adapter must be reviewed before implementation so these fields are either accepted in a game-specific nested payload or represented by approved generic fields.

## Client Rule

The client may render `presentationPayload`. It must not trust browser-produced data as authoritative for outcome, wallet, RNG, round completion, or persisted state.
