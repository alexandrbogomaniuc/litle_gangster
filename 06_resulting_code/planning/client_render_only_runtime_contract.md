# Client Render-Only Runtime Contract

Status: REQUIRED_FOR_ANY_FUTURE_CLIENT_WORK.

## Client Role

The client is a renderer. It consumes backend/runtime payloads and maps them to scene/object animation states.

## Client Consumes

- `presentationPayload` after extension/review;
- `round` display fields;
- `feature` action availability;
- `wallet` display fields;
- `restore` and `history` views.

## Client Does Not Produce

- RNG outcomes;
- symbol grids;
- cascade results;
- feature outcomes;
- max-win cap decisions;
- authoritative wallet or round state;
- persisted history truth.

## Build Gate

No `package.json`, `src/`, `public/`, `dist/`, `build/`, runtime implementation, copied template code, or production assets may be created until a later explicit client implementation approval.

