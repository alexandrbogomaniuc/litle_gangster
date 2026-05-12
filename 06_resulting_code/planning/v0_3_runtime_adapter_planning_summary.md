# v0.3 Runtime Adapter Planning Summary

Status: PLANNING_ONLY.

## Summary

Little Gangster needs a backend/runtime adapter that converts authoritative v0.3 math/result output into the generic `/slot/v1` runtime envelope.

The strongest candidate lane remains `/slot/v1`, but it is still candidate-only for Little Gangster because the 8001 runtime owner and result API are not proven.

## Adapter Needed

1. Backend-owned v0.3 result normalizer.
2. `/slot/v1` envelope projector.
3. Presentation payload extension or reviewed game payload subobject.
4. History/recovery projector.
5. Client render mapper from reviewed runtime payload to v0.3 scene/object states.

## Direct Carry Decision

`presentationPayload` cannot be treated as ready to carry v0.3 directly without extension/review. The current generic schema is strict and supports generic reel/grid/counter/message/cue fields, not the full v0.3 result schema.

## Implementation Decision

GameClientBuilder implementation remains blocked. Planning-only fixture work may be allowed later if explicitly marked non-production.

