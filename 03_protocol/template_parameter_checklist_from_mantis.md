# Template Parameter Checklist From Mantis

Status: advisory only; do not assume these fields exist in current GS.

## Scope Rule

The following names are checklist candidates. GameServerRegistrar must verify current GS schema/config/support before generating any registration artifact. This file does not select ExtGame and does not select `HOSTING_MODE=EXTGAME`.

## Candidate Fields

| Category | Candidate names | Current handling |
|---|---|---|
| Lane / hosting | `HOSTING_MODE`, `EXTGAME_CLIENT`, `CDN_SUPPORT`, `GL_SUPPORTED` | Verify against current GS. Do not set ExtGame by default. |
| RTP | `RTP`, `RTP_MIN`, `RTP_WITHOUT_BF`, `RTP_MIN_WITHOUT_BF`, `BF_RTP`, `BF_RTP_MIN` | Treat as metadata/config until source proves executable math import. |
| Models | `POSSIBLE_MODELS`, `CURRENT_MODEL` | Verify if current GS supports model switching. |
| Max win | `POSSIBLE_MAX_WINS`, `POSSIBLE_MAX_WINS_WITHOUT_BF`, `CAP_WIN_MULTIPLIER` | Keep separate from theoretical/observed max win and cap event fields. |
| Volatility | `VOLATILITY` | Metadata/display unless current GS proves behavior. |
| Bet defaults | `GL_MIN_BET_DEFAULT`, `GL_MAX_BET_DEFAULT`, `GL_DEFAULT_BET_DEFAULT`, `GL_DEFAULT_BET`, `DEFCOIN` | Must map to 6x5 cluster bet model, not fixed-line formula blindly. |
| Buy feature | `GL_BF_MAX_BETS`, `BF_BETS` | Verify current GS buy-feature representation. |
| Fixed-line legacy | `POSSIBLE_LINES`, `LINES_COUNT`, `DEFAULTNUMLINES`, `POSSIBLE_BETPERLINES`, `DEFAULTBETPERLINE` | Warning only for Little Gangster because selected layout is cluster, not fixed paylines. |
| FRB | `FRB_COIN`, `isFrb` | Verify if FRB is in product/current lane scope. |
| Progress / double-up | `GAME_WITH_PROGRESS`, `GAME_WITH_DOUBLE_UP`, `DOUBLE_UP_DISABLED` | Double-up is removed from active math scope unless donor/product evidence changes. |
| Enablement | `ISENABLED`, `RELEASE_TIME`, `LGA_APPROVED`, `IS_LGA_SHELL_SUPPORTED` | Verify current release/registration workflow. |
| Arbitrary coins / keys | `GL_ARBITRARY_COINS`, `SD_KEYS`, `S_VERSION` | Verify current GS field support and redact secrets. |
| Game identity | title, game name, single-game-id flags | Required but current schema must be verified. |
| Round finish | `roundFinishedHelper`, `endRoundSignature` | Verify whether 8001 template/config requires this. |

## Registrar Gate

Later GameServerRegistrar must:

- Verify each used field against current GS source/config/schema.
- Link every generated value to project evidence.
- Keep generation review-only until approved.
- Avoid raw secrets and raw endpoint values.
- Produce rollback artifacts.

