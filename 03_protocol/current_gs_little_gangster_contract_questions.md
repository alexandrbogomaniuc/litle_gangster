# Current GS Little Gangster Contract Questions

Status: open contract questions for later ProtocolAndSchemaMapper/GameClientBuilder/GameServerRegistrar/WalletAndLaunchTester.

## Launch And Routing

- Which current Staging route will launch game 8001: startgame wrapper, `cwstartgamev2.do`, guest/free launch, or a combination?
- Which bank/config record will add game 8001 to `NEW_GAMES_ROUTE_GAME_ID` or the current equivalent?
- Which game-specific client URL key will be used for 8001?
- Which `ngsApiUrl`, `gsInternalBaseUrl`, and `ngsContract` values are safe for dev/stage without persisting secrets?

## Runtime Contract

- Does Little Gangster use the current `slot-browser-v1` envelope exactly, or does v0.3 require schema extension?
- Which result fields carry cascade steps, golden cells, rainbow activation, coin reveals, feature modes, cap status, and restore state?
- Which endpoint owns buy-feature confirmation and purchased feature entry?
- Is `featureaction` the right endpoint for collect, buy-feature choice, feature continuation, or all of these?

## Transaction And State

- What is the current-lane equivalent of Mantis `processTransactions`?
- Is wallet reserve/settle split across `/slot/v1/playround` and `/slot/v1/featureaction`, or hidden behind new-games server calls?
- Which fields are idempotency keys and operation IDs for duplicate retry?
- Where is the authoritative `gameState` or restore payload stored?
- Is Lasthand still the canonical state/history substrate for game 8001?

## Round Completion

- Does game 8001 need `roundFinishedHelper` / `endRoundSignature` in GS template/config?
- If yes, can a standard helper work, or does Little Gangster require a custom cascade/feature-mode completion marker?
- Which v0.3 math field is the authoritative round-complete marker?

## History / VABS

- Does GS provide the Little Gangster history and replay renderer, or must GameClientBuilder produce a VABS package?
- Which in-game History button URL should be used?
- Does `/slot/v1/gethistory` supply enough data for VABS/replay and player-facing history?
- Which records are needed for round and session history?

## FRB / OCB / Promos

- Are FRB and OCB required for Little Gangster?
- Does current GS support them in the new-games lane for 8001?
- Are restart transitions needed after FRB finished/canceled/expired/capped states?

## Certification

- What bot-test volume is required for math/runtime certification?
- What source package and local runnable environment must be delivered to certification?
- Which performance/mobile/memory gates must pass before release?

