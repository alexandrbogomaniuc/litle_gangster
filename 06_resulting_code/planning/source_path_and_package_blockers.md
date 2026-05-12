# Source Path And Package Blockers

Status: planning-only.

## Resolved For Planning

- Staging root exists.
- Gamesv1 root exists.
- `@gamesv1/core-protocol` package exists and was inspected at a high level.
- `new-games-server` source exists and was inspected at a high level.
- `new-games-client` source exists and was inspected at a high level.
- GS server legacy/template paths exist.

## Still Blocked For Implementation

- no Little Gangster 8001 client package found.
- no Little Gangster 8001 runtime package found.
- no proven v0.3 result adapter from runtime envelope to Little Gangster scene fields.
- no proven production asset package path.
- no proven registration route for 8001.
- no proven serializer/import path for `scn`/`jcn`.
- no proven history/VABS/Lasthands replay path for v0.3 result payload.

## Implementation Rule

GameClientBuilder must not create `package.json`, `src/`, `public/`, copied template files, or production assets until these blockers are resolved and the user explicitly approves code generation.

