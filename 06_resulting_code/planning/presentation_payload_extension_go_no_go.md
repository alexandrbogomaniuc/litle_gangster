# Presentation Payload Extension Go / No-Go

## `presentationPayload.gamePayload`

Recommendation: GO_TO_SCHEMA_REVIEW, NO-GO_FOR_IMPLEMENTATION_TODAY.

Reason: It is reusable and matches the need for a game-specific render payload, but core-protocol `PresentationPayloadSchema` is strict and does not allow this field today.

## `presentationPayload.littleGangsterV03`

Recommendation: FALLBACK_ONLY.

Reason: It is easier for one game but creates a game-specific root field. It still requires schema review/change.

## Existing Generic Fields Only

Recommendation: DO_NOT_USE_FOR_FULL_V0_3.

Reason: Cascades, golden-square persistence, rainbow activation, coin/special reveals, feature modes, cap state, completion, and persistence are too rich to hide in generic labels/cues/counters.

## Decision

Proceed next with schema extension review or fixture-only static prototype if explicitly approved. Do not start production implementation.
Evidence label summary: BLOCKED_SCHEMA_CHANGE for implementation today; CANDIDATE_FALLBACK for game-specific field; DO_NOT_USE for overloading generic labels/cues.

