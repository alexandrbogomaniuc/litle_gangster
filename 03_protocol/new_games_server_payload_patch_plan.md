# New Games Server Payload Patch Plan

Status: PLAN_ONLY_NO_SOURCE_PATCH
Primary file to patch later: `new-games-server/src/index.ts`

## Current Source State

| Area | Finding | Evidence label |
|---|---|---|
| Runtime envelope builder | Accepts optional `presentationPayload` record-like input and can construct a runtime envelope. | PROVEN_SERVER_PERMISSIVE_PATH |
| 7001 presentation branch | `gameId === 7001` has a special presentation payload branch. | PROVEN_7001_BRANCH |
| Little Gangster branch | No 8001/Little Gangster presentation branch was found in targeted source inspection. | NOT_FOUND_8001 |
| `mathBridge` use | 7001 emits generic fields plus `mathBridge`. | CANDIDATE_PATTERN |

## Future Patch Steps

1. Prove or create the Little Gangster/8001 runtime package and result owner.
2. Define a `buildLittleGangsterPresentationPayload` or equivalent adapter entrypoint.
3. Emit generic presentation fields required by shared UI surfaces.
4. Emit `presentationPayload.gamePayload` with `{ gameKey, schemaVersion, payload }`.
5. Preserve backend-owned authoritative fields outside browser control.
6. Ensure history/recovery snapshots retain enough v0.3 payload state for reconnect and replay.
7. Add tests for successful playround, feature action, resume, and history envelope construction.
8. Add negative tests proving browser-supplied payload is not trusted as authoritative outcome.

## Adapter Output Target

The future server-side adapter should output a strict-runtime-compatible envelope whose presentation area contains:

- existing generic presentation fields needed by shell/UI-kit
- `gamePayload.gameKey = little-gangster`
- `gamePayload.schemaVersion = v0.3`
- `gamePayload.payload = v0.3 renderer payload`

## Implementation Status

No new-games-server source was modified in this sprint. New-games-server patching remains blocked until schema patch approval and runtime owner/path proof are complete.

## Source Patch Apply Update - 2026-05-12

Evidence label: LIKELY_ALREADY_PERMISSIVE

`new-games-server/src/index.ts` was reviewed and left unchanged. Its existing runtime-envelope helper accepts an
optional record-shaped `presentationPayload`, so the reusable schema/type patch does not require a generic server
change by itself.

Evidence label: BLOCKED_FOR_8001

No 8001 branch or Little Gangster adapter was added. The future server work remains blocked until a backend
adapter implementation sprint is explicitly approved.
