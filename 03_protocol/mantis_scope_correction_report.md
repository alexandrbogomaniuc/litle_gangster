# Mantis Scope Correction Report

Generated: 2026-05-11

## Correction

Mantis/ExtGame information is now treated as an advisory current-GS checklist. It is not selected architecture for Little Gangster.

## What Changed

- New docs distinguish current-GS lane proof from ExtGame checklist lessons.
- ExtGame is labelled candidate/unverified unless current GS source/config proves support.
- `processTransactions`, `gameState`, `roundFinishedHelper`, `restartGame`, VABS/VBA/Lasthands, FRB/OCB, RNG, template fields, and certification are now checklist items to verify against the selected current lane.
- New-games `slot-browser-v1` / HTTP runtime remains a candidate direction only; it is not guaranteed truth and is not selected until current GS is verified directly.

## Current GS Findings

- Current Staging GS launch code has new-games redirect signals with `ngsApiUrl`, `gsInternalBaseUrl`, and `ngsContract=v1`.
- Current Staging new-games server candidate source implements `/slot/v1/*` browser endpoints.
- Current Staging Gamesv1 docs call ExtGame an archived legacy marker and identify `slot-browser-v1` as canonical for that candidate source lane.
- Current GS source has external game id mapping, VABS/VBA/history, Lasthand, restart, FRB, cash bonus, and RNG concepts.
- This sprint did not prove that Little Gangster must expose an external ExtGame endpoint.
- This sprint did not prove that Little Gangster must use Gamesv1/Crazy Rooster/slot-browser-v1.
- New game registration should be treated as metadata/config/routing/display setup unless current GS source proves executable math import.
- RNG/result generation must remain server/backend-side, not browser-side, but the owner is still unproven.

## Non-Actions

- No MathModelDesigner implementation was run.
- No client code was generated.
- No registration artifacts were generated.
- No DB/Cassandra action occurred.
- No wallet endpoint was called.
- No donor URL was browsed.
- No assets were captured.
- No public GitHub push was performed.

## Next Recommended Skill

MathModelDesigner retry remains next, with the Mantis checklist used as validation input for v0.3/vNext result-state handoff fields. It must not assume `processTransactions` is the production API unless the current lane proves it.
