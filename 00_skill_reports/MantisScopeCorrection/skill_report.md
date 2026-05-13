# Mantis Scope Correction Skill Report

Generated: 2026-05-11

## Sprint Identity

Scope-correction sprint: ProtocolAndSchemaMapper current-GS integration clarification plus advisory Mantis checklist assimilation.

## Tasks Performed

- Created corrected Mantis/current-GS checklist package under `03_protocol/`.
- Performed targeted Staging source signal scan only inside allowed current roots and compose-derived Staging paths.
- Corrected existing ExtGame project docs to advisory/candidate wording.
- Added MathModelDesigner next-retry checklist files without generating math implementation.
- Added GameServerRegistrar checklist files without generating registration artifacts.
- Added WalletAndLaunchTester/RTPAndReleaseAuditor QA gate files without executing tests.
- Patched reusable skill-suite wording so ExtGame/Mantis material is advisory unless current GS proves the lane.
- Updated project manifest, assumptions, decisions, and protocol summary.

## Current GS Findings

- New-games `slot-browser-v1` / HTTP runtime has useful candidate source signals, but it is not trusted or selected until current GS source/config/docs prove the lane directly for Little Gangster.
- ExtGame external endpoint support for Little Gangster remains candidate/unverified.
- Current GS shows external game id mapping, but that is not the same as a selected external endpoint lane.
- Current GS/new-games candidate source shows `/slot/v1/*` endpoints, GS internal wallet/history bridge, VABS/VBA/history concepts, Lasthand concepts, restart/resume concepts, round-finished helper concepts, and RNG utility/provisional
backend outcome signals.
- New game registration should be treated as metadata/config/routing/display setup unless current GS source proves executable math import.
- RNG/result generation must be server/backend-side, not browser-side; the exact owner remains unproven.
- Little Gangster-specific 8001 registration, VABS/history package, round completion, process-equivalent flow, FRB/OCB scope, production RNG owner, and certification gates remain open.

## Safety

- No raw Mantis text was stored.
- No private links, emails, SIDs, signatures, tokens, PASS_KEY values, passwords, donor assets, screenshots, HAR, or full donor URLs were stored.
- No donor browser work, asset capture, client build, math implementation, registration generation, DB/Cassandra action, wallet call, release approval, or public push occurred.

## Next Recommended Skill

MathModelDesigner retry/audit, using the corrected current-GS checklist as validation input and without assuming ExtGame API names unless current GS later proves ExtGame.
