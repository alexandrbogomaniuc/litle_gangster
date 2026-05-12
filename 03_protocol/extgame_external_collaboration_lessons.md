# ExtGame External-Collaboration Lessons

Generated: 2026-05-11
Corrected: 2026-05-11

## Corrected Scope

This file is now an advisory checklist summary. It does not select ExtGame for Little Gangster and does not prove that Little Gangster must implement an external endpoint.

Current integration lane selection must come from current GS source/config/docs. New-games `slot-browser-v1` / HTTP runtime is candidate evidence only, with ExtGame also candidate/unverified.

## Source Boundary

No raw Mantis text is stored. No private links, emails, raw endpoints, SIDs, signatures, tokens, passwords, PASS_KEY values, or secret values are stored.

## Advisory Lessons To Verify Against Current GS

- External-game collaboration notes can reveal missing checklist areas, but they must not force architecture.
- `processTransactions` is an external-lane concept until current GS proves otherwise; translate it to current-lane reserve/settle/process-equivalent validation.
- `gameState`, `lastAction`, Lasthand, and restore behavior must be verified against current GS/new-games source.
- `roundFinishedHelper` and `endRoundSignature` are current-GS template/config concepts that may matter for round completion, but 8001 usage remains unverified.
- `restartGame`, FRB transitions, OCB/cash bonus, and closeSession are lane-dependent checklist items.
- VABS/VBA/history may be provided by GS or may require project-specific renderer work; do not assume external-side implementation.
- Template/config fields are candidates only until GameServerRegistrar verifies current GS support.
- RNG, bot testing, certification, source/local test environment, and performance gates must block release until proven.

## Current Project Interpretation

- ExtGame selected: false.
- ExtGame lane status: candidate/unverified.
- Current selected lane: none; new-games `slot-browser-v1` remains candidate evidence pending direct current-GS verification.
- Next workflow impact: MathModelDesigner retry should include the checklist-derived state/round-complete/win-tier/bet-mapping fields, without assuming ExtGame APIs.
