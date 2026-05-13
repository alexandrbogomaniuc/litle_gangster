# Source Patch Apply Preflight

Sprint: ProtocolAndSchemaMapper source patch apply for `presentationPayload.gamePayload`

Status: preflight completed with git-topology caveat

## Approved Scope

Only the reviewed reusable `presentationPayload.gamePayload` schema/type/mapper patch may be applied.

No Little Gangster backend adapter, 8001 runtime package, production client code, registration artifact,
wallet/API call, DB/Cassandra action, donor browsing, donor asset capture, public export, or release approval
is allowed in this sprint.

## Path Existence

All approved Staging target paths and read-only review paths were present at preflight.

## Git Baseline

Command context: `[STAGING_ROOT]`

- Resolved git root: `[DEV_ROOT]`
- Branch: `Codex`
- Pre-patch commit hash : [REDACTED_FIXTURE]

Scoped target status showed the approved target files as untracked under the parent git repository.
Scoped Staging status reported the Staging subtree as untracked (`?? ./`).

Because the resolved git root is outside the sprint's allowed source root, no broad parent-repository
dirty scan was performed. The sprint proceeds using scoped target-file status and hash evidence only.

Preflight did not identify unrelated tracked modifications inside the approved target-file set.

## Pre-Patch Target Hashes

```text
a165cea4711be1fe006fe3d6278474008f666b7819524c4ecfae36ddb30d5e9a  opengame.response.schema.json
c5134feffc08a4b0e03f7966407baf6ad231ddeb58f4a2f399d1f2791eb7ca97  playround.response.schema.json
1bfdd15bbc11cc0839e30367d460f889c863cc43bc17948fdaac192b8052a5d7  featureaction.response.schema.json
105efa29af9bbf2a745766ca9d7a30b28032619eeeae25ea486ffcf1388441e0  resumegame.response.schema.json
bae175b9bf172f3f9aae9fecaa06b344efa80defa15a6341031a942fec2e80d0  gethistory.response.schema.json
a2c9d5fc5512471a17def5f3975788e039b86d0f6f567f3e8e6c07db644c62f1  closegame.response.schema.json
5a8afd7481f71d41f4a0351cac65f1e4735fe9806828d02a3271fd5ae3056ac7  core-protocol/src/schemas.ts
a29248dd661d5e6485baaa1ca5c83f580ef41f748ace10cd422eaf2fb3c248ab  core-protocol/src/IGameTransport.ts
b75e701483442e21f1274afea61eadd99c9db853bcdb6b0bd4386ecadc622a87  ui-kit/src/shell/presentation/PremiumPresentationMapper.ts
c98c90125ce279890f0d0ae4c0833777193b7a865f2f054f0886c59ebc94e540  new-games-server/src/index.ts
```

## Preflight Decision

Proceed with the approved patch set, but record that rollback cannot rely on tracked-file checkout unless the
Staging source is later placed under its own clean repository baseline. The rollback report must include both
git-checkout guidance and manual reverse-patch guidance.
