# Client Render-Only Contract

Status: REQUIRED.

## Principle

The client renders backend/runtime result payloads. It does not generate production RNG, calculate authoritative wins, decide cap outcomes, mutate wallet state, or persist authoritative round state.

## Client May Do

- Send user actions to the selected runtime endpoint.
- Render `presentationPayload` and reviewed v0.3 render state.
- Sequence cascade, reveal, and win-tier animations from backend-provided data.
- Display wallet/bet/win values returned by backend envelope fields.
- Use local animation timing hints.
- Show reconnect/history views from backend-provided restore/history payloads.

## Client Must Not Do

- Generate or modify symbols, grids, cascades, feature outcomes, cap results, or wins.
- Invent state versions, round completion, history records, or restore truth.
- Treat registration metadata as executable math.
- Package donor/scaffold assets into production output.
- Treat planning fixtures as production runtime proof.

## Implementation Gate

GameClientBuilder implementation remains blocked until:

- runtime owner is proven;
- result API contract is proven or fixture-approved for planning only;
- presentation extension is reviewed;
- asset strategy is approved;
- explicit user approval for client code is given.

