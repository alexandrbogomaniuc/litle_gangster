---
name: ProtocolAndSchemaMapper
description: Map documented launch, wallet, runtime, and Cassandra/config contracts without donor investigation or guessed schema/protocol details.
---

# ProtocolAndSchemaMapper

## Purpose
Map protocol layers and schema requirements from uploaded docs and explicit source paths.

## When To Use
Use after project creation and before build/registration/test work.

## Required Inputs
Manifest, BSG CW docs, extracted ZIP docs, explicit client/server/config source paths if provided, and sanitized external-collaboration notes as
advisory checklist material. External-collaboration notes do not select ExtGame unless current GS source/config proves that lane.

## Preconditions
Read `references/PROTOCOL_LAYER_MODEL.md`, `BSG_COMMON_WALLET_SUMMARY.md`, `CASSANDRA_REGISTRATION_SUMMARY.md`, and
`references/MANTIS_EXTERNAL_COLLABORATION_CHECKLIST.md` when external-collaboration lessons are in scope. Read
`references/EXTGAME_EXTERNAL_COLLABORATION_REQUIREMENTS.md` only as an advisory checklist unless current GS proves ExtGame.

## Forbidden Actions
No donor investigation, broad filesystem search, fake source roots, guessed hash orders, guessed DB tables, or Cassandra execution.

## Workflow
1. Separate launch/template, browser runtime, Game Server/MQ/WebSocket, BSG CW, and Cassandra layers.
2. Map Authenticate, Bet/Result, Refund Bet.
3. Extract exact hash rules and parameter orders.
4. Extract XML/EXTSYSTEM/BSGSYSTEM response rules.
5. Extract idempotency, retry, refund, and fail-safe behavior.
6. Extract Cassandra registration/config evidence.
7. Mark unknown browser runtime and Game Server fields as blockers unless source proves them.
8. Treat Mantis/ExtGame notes as advisory checklist material until current GS source/config proves a selected lane. If ExtGame is merely
   candidate/unverified, record `processTransactions`, `gameState`, `roundFinishedHelper`, `restartGame`, template parameters, VBA/VABS/history,
   FRB/OCB, and certification as lane-dependent validation items, not selected APIs. If ExtGame is proven, map it as a separate lane without
   storing raw external-collaboration text.

## Output Files
`03_protocol/*` contracts, blockers, skill reports, handoff.

## Validation Checklist
Every field has source evidence or blocker; no donor facts; no DB execution; advisory ExtGame/Mantis checklist items are separate from selected BSG
CW, new-games runtime, and legacy template layers; confidential collaboration content is summarized and redacted.

## Handoff To Next Skill
Next: MathModelDesigner.

## Failure / Blocker Handling
If source root or schema evidence is missing, block that sub-area.

## SprintReporter Handoff
Report source docs used, contracts generated, unknowns, and validation results.

## Pilot Pipeline Hardening Addendum

Before GameClientBuilder or GameServerRegistrar, require a current-GS lane, registration, RNG, and math ownership audit. Treat prior-agent
architecture directions as candidate evidence only. Treat ExtGame/Mantis/external-collaboration information as advisory checklist material unless
current GS source/config directly proves that lane. Use evidence labels and keep registration metadata separate from executable math unless source
proves otherwise.

## Visual History Route Requirement

For future games, map VABS/VBA/Lasthands visual history as a first-class runtime
contract before release. Stored JSON history alone is not enough unless current GS,
Casino Manager/backoffice, and in-game History evidence proves JSON-only replay is
accepted. Protocol planning must either define round replay, session replay,
whole-session replay, visual/render responses, deterministic replay payloads, and
wallet/accounting references, or explicitly carry a release-blocking visual-history
route blocker.

Before implementing visual history routes, run a route-resolution audit against legacy
GS/global VABS routes, new-games-server history routes, game client History behavior,
Casino Manager/backoffice access, and registration/bootstrap settings. Select a route
model with evidence labels before patching source; do not assume `/slot/v1/gethistory`
JSON replay is equivalent to visual VABS/VBA/Lasthands replay.

Future games must define VABS evidence policy before release: deterministic replay
payload required, visual VABS route required unless current GS proves otherwise,
selected `historyEvidenceMode`, screenshot/video media policy if enabled, and
storage/retention/security settings. Do not treat screenshots or video as the
authoritative result source.

## GS/Wallet Responsibility Boundary Requirement

Before wallet/launch tests or registration generation, future games must document the
responsibility boundary between browser/client, game runtime, lifecycle wrapper,
current GS/WebGS, wallet/casino provider, Cassandra/config/cache/history storage,
BO/CM/VABS, GameServerRegistrar, and WalletAndLaunchTester. Protocol mapping must
identify who owns launch/session control, wallet auth, debit, credit, refund/rollback,
pending/stuck transaction state, idempotency, durable history, logs/monitoring, and
registration fields. The browser/client must not be marked as real wallet owner, and
runtime must not own real casino balance unless current GS source explicitly requires it.
If ownership is unclear, record blockers and correct the downstream WalletAndLaunchTester
prompt to verify boundaries and approved endpoints rather than inventing wallet storage.
