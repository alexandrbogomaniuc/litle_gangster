# Game 8001 Registration Readiness

## Game ID Checked

Project manifest lists future game ID 8001. This audit checked for 8001 in Staging and project docs.

## Readiness Table

| Question | Answer | Status |
|---|---|---|
| Is gameId 8001 registered anywhere? | No current registration record was found in Staging source/config/runtime exports. Mentions are project planning docs or an unrelated free-game test value. | NOT_FOUND |
| What records/configs are needed? | `GameTInfoCF`, `GameInfoCF`, `BankInfoCF` route/config, optional `ExtGameIds` only if lane requires it, serialized `scn`/`jcn`. | PROVEN/LIKELY |
| What bank/default lane should be used? | Bank 6275 remains candidate from prior project context; New Games route is strongest candidate but not final. | CANDIDATE |
| What route/client/runtime path is needed? | If New Games is selected: add 8001 to `NEW_GAMES_ROUTE_GAME_ID`, set game-specific client URL if needed, verify `NEW_GAMES_API_URL` and `NEW_GAMES_GS_INTERNAL_BASE_URL`. | LIKELY |
| What RTP/model values are ready? | v0.3 math planning has RTP models and cap metadata, but release math is not approved. | CANDIDATE |
| What math values are not ready? | Final certified RTP, final runtime owner integration, production RNG owner, bonus-buy EV, feature-mode exact probabilities. | BLOCKED |
| What asset/client values are not ready? | Production client path and final approved release assets are not available. | BLOCKED |
| What blocks registration generation? | Missing 8001 client/runtime path, serializer/import path, final runtime lane, release-safe assets, and math approval. | BLOCKED |

## Decision

GameServerRegistrar must remain blocked for artifact generation. It may only use this audit as input for a later generate-only sprint.
