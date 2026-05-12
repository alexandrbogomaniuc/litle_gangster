# Strict Fixture Runtime Envelope Test Plan

Status: TEST_PLAN_ONLY.

Future backend adapter implementation tests should use the strict fixtures as expected response-envelope examples.

Required future tests:

1. Adapter output validates against the same patched response schema used by the matching strict fixture.
2. Adapter output includes `presentationPayload.gamePayload.gameKey = little-gangster`.
3. Adapter output includes `presentationPayload.gamePayload.schemaVersion = v0.3`.
4. Adapter output `gamePayload.payload` validates against v0.3 `result_schema.json`.
5. Wallet/accounting fields remain outside `gamePayload`.
6. Browser/client does not provide authoritative outcome fields.
7. Reconnect and history outputs preserve enough payload for state recovery and replay.
8. 7001 `mathBridge` compatibility remains unchanged.

This plan does not approve backend adapter implementation or GameClientBuilder implementation.
