# Game Server Runtime Contract

Status: partial

## Launch Source Classes

Verified source classes:

- `CWStartGameAction.java`
  - Handles `cwstartgamev2.do` launch.
  - Authenticates through Common Wallet with the launch token (`lines 99-108`).
  - Resolves new-games routing (`line 101`).
  - Creates/uses session info (`lines 313-316`).
  - Invokes session/multiplayer/gameplay/protocol routing bridges and shadow calls (`lines 319-392`).
  - Redirects to new-games when enabled (`lines 416-423`).
- `BaseStartGameAction.java`
  - Builds new-games redirect params (`lines 878-904`).
  - Resolves new-games client URL including per-game keys and default 7001 branch (`lines 917-935`).
  - Builds legacy multiplayer JSP redirect with websocket URL (`lines 1023-1031`).
- `template.jsp`
  - Legacy shell that reads bank/session/game params and loads game resources (`lines 52-114`, `250-328`).

## New-Games Runtime Flow

Verified 7001 runbook:

1. `POST /slot/v1/bootstrap`
2. `POST /slot/v1/opengame`
3. `POST /slot/v1/playround`
4. `POST /slot/v1/resumegame`
5. `POST /slot/v1/featureaction`
6. `POST /slot/v1/gethistory`
7. `POST /slot/v1/closegame`

Verified browser client:

- Uses `GS_HTTP_RUNTIME`.
- Sends `contractVersion=slot-browser-v1`.
- Sends `requestCounter`, `currentStateVersion`, `idempotencyKey`, and `clientOperationId`.
- Reads wallet balance from runtime response wallet envelope.

## Wallet Service / Common Wallet Clues

Verified:

- `CWStartGameAction.java:106-108` performs external-side authentication through Common Wallet during launch.
- `CCommonWallet.java:3-75` defines wallet parameter constants and XML response constants.
- `CWMType.java:6-10`, `29-108` defines win send/accumulation conditions tied to `isRoundFinished`, `winAmount`, and `negativeBetAmount`.
- `WalletProtocolFactory` targeted evidence shows credit condition and intercept methods around `isRoundFinished`, win amount, negative bet, and promo win checks.

Unknown:

- Exact wallet client class implementation path for the local `CanexCWClient` was not fully inspected.
- Exact EC/ES request builder and retry implementation must be tested later.

## Runtime Servlet / Action Pattern

Known:

- Legacy multiplayer route forwards to `/<mode>/mp/template.jsp` and passes `WEB_SOCKET_URL` ending in `/websocket/mplobby`.
- New-games route forwards to a client URL and passes `ngsApiUrl`, `gsInternalBaseUrl`, and `ngsContract=v1`.
- Legacy CQL examples use `servlet`/`swfLocation`, but 8001 must use a verified new-games registration pattern if that path is selected.

Unknown:

- The server-side implementation of `/slot/v1/*` endpoints was not fully mapped because the core protocol/server package root was not explicit in this sprint.

## MQ / WebSocket Clues

Known:

- Legacy JSP and `BaseStartGameAction.java:1023-1031` pass `WEB_SOCKET_URL` for `/websocket/mplobby`.
- `CWStartGameAction` uses `MultiplayerServiceRoutingBridge`, `GameplayOrchestratorRoutingBridge`, and `ProtocolAdapterRoutingBridge`.

Unknown:

- Whether future Little Gangster 8001 uses legacy websocket/MQ, new-games HTTP runtime only, or both during launch is not final.

## Transaction / Fail-Safe Clues

Known:

- BSG CW docs define refund behavior and idempotency expectations.
- GS wallet classes track `roundId`, `isRoundFinished`, `negativeBet`, `jpContribution`, and `jpWin`.
- Browser runtime sends idempotency and request counters for new-games slot operations.

Unknown:

- Exact GS-side duplicate replay enforcement for `/slot/v1/*`.
- Exact wallet retry/refund ordering in code for game 8001.
- Exact offline credit/fail-safe policy for the new-games path.

## RNG / Result Ownership

Unknown for Little Gangster 8001.

Evidence boundary:

- 7001 has demo/provisional runtime paths and math scripts, but this sprint did not run MathModelDesigner.
- Do not assume client-side RNG/result ownership for 8001.
- MathModelDesigner must define authoritative math package and simulation. GameClientBuilder and WalletAndLaunchTester must verify final runtime ownership.
