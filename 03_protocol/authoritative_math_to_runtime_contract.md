# Authoritative Math To Runtime Contract

Status: planning contract only.

Evidence labels:

- PROVEN: `presentationPayload.gamePayload` is the recommended and patched carrier for game-specific render payloads.
- PROVEN: 24 strict fixtures validated through patched response schemas in prior sprint outputs.
- CANDIDATE: future Little Gangster backend adapter emits `/slot/v1` responses.
- NOT_PROVEN: 8001 runtime owner.
- NOT_PROVEN: production Little Gangster result API.
- NOT_AUTHORITATIVE: 7001 math behavior.

Runtime flow:

1. Server math owner generates authoritative Little Gangster result.
2. Backend adapter maps result to runtime envelope.
3. Runtime envelope includes `presentationPayload.gamePayload`.
4. `gamePayload.gameKey` is `little-gangster`.
5. `gamePayload.schemaVersion` is `v0.3` for current renderer payload.
6. `gamePayload.payload` contains v0.3 render state.
7. Wallet/accounting fields remain outside game payload.
8. Browser renders only.

Backend-owned fields:

- RNG draw references.
- authoritative result values.
- cluster/cascade wins.
- feature mode decisions.
- coin/special reveal values.
- max-win cap.
- round completion.
- state version.
- history snapshot references.

Runtime output must not include browser-generated authoritative fields.

Implementation remains blocked until explicit backend adapter approval.

