# Future Game Parallel Math Validation Playbook

Status: generic playbook for future projects.

## Example Request

Create a game with:

- RTP LOW = 93.00%
- RTP MEDIUM = 97.00%
- RTP HIGH = 99.00%
- volatility LOW / MEDIUM / HIGH
- nine `mathProfileId` profiles
- optional bonus buy
- optional FRB/free-round campaign
- optional jackpot

## 3 RTP x 3 Volatility Setup

Every future game should have nine pretested profiles unless product explicitly approves a smaller matrix:

- LOW RTP / LOW volatility
- LOW RTP / MEDIUM volatility
- LOW RTP / HIGH volatility
- MEDIUM RTP / LOW volatility
- MEDIUM RTP / MEDIUM volatility
- MEDIUM RTP / HIGH volatility
- HIGH RTP / LOW volatility
- HIGH RTP / MEDIUM volatility
- HIGH RTP / HIGH volatility

Operators select approved profiles only. Operators must not enter arbitrary RTP or volatility values at runtime.

## Train Simulation Loop

Use train seeds only. Adjust only from train evidence. Keep all changes in the main approved math lane; parallel workers must not modify active
  configs.

## Validation Gate

Run validation with validation seeds only after the train gate is ready. Validation seeds must not be used for tuning.

## Bonus-Buy Gate

If bonus buy exists, validate separately:

- cost denominator;
- purchased feature start state;
- `BF_RTP`;
- `BF_RTP_MIN`;
- `BF_BETS`;
- cap behavior based on base bet, not bonus-buy stake;
- VABS/history and wallet accounting blockers.

## FRB/Promo Gate

FRB/free-round campaigns are separate from base RTP unless product/GS rules explicitly require combining them. Validate:

- promo EV;
- campaign liability;
- state/history behavior;
- settlement/accounting behavior;
- replay/VABS behavior;
- cap behavior.

## Tail/Max-Win Gate

Run tail/max-win evidence with a separate seed family. Report cap frequency, max observed win, confidence level, and whether values are planning-only.

## Registration Field Extraction

Use the extractor to produce or block:

- `POSSIBLE_MODELS`;
- `RTP_WITHOUT_BF`;
- `RTP_MIN_WITHOUT_BF`;
- `BF_RTP`;
- `BF_RTP_MIN`;
- `BF_BETS`;
- `SD_KEYS`;
- `CAP_WIN_MULTIPLIER`;
- `MAX_WIN`;
- `POSSIBLE_MAX_WINS`;
- volatility and `mathProfileId` mapping.

`POSSIBLE_MODELS` must cover the maximum RTP across supported strategies. `BF_RTP` must not exceed `POSSIBLE_MODELS`.

## Release And Certification Evidence

Parallel evidence is non-certified by default. A certification evidence package may be assembled, but release remains blocked until the final
  release/lab gate approves it.

## Hard Rules

- No validation-seed tuning.
- No active config changes from a parallel thread without main-thread approval.
- No backend/client/registration/release actions from parallel workers.
- No certification claim from parallel evidence alone.
