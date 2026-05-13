# Mantis Lessons For Current GS Checklist

Status: assimilated as advisory checklist, not selected architecture.

## Scope Correction

The sanitized Mantis/ExtGame material is useful as an integration checklist from a similar external-game collaboration. It is not proof that Little Gangster must use an external endpoint, and it does not select `HOSTING_MODE=EXTGAME`.

Little Gangster must work with the user's current GS version. The integration lane must be proven from current GS source, current GS config, current runtime docs, and generated registration evidence.

## Candidate Lanes To Prove

| Lane | Current status | Notes |
|---|---|---|
| new-games / `slot-browser-v1` / HTTP runtime | strongest supported candidate | Current Staging Gamesv1 docs and source describe browser-to-GS `/slot/v1/*` as canonical. |
| legacy GS template / WebSocket / `template.jsp` | supported legacy lane | Current GS still has legacy launch/template support; not preferred for Little Gangster unless product changes direction. |
| ExtGame external-backend lane | candidate / unverified | Current GS has external game id mapping, but no proof was found in this sprint that Little Gangster should implement an external endpoint. |
| mixed lane | possible only if proven | Some flows may combine GS launch, new-games API, GS internal wallet/history bridge, and legacy VABS/history. |
| unknown / blocked | applies to unresolved details | Runtime ownership, registration fields, and certification details still need validation. |

## Checklist Items To Retain

These items must be verified against the current lane, not blindly implemented as ExtGame APIs.

| Area | Advisory lesson | Current-GS validation rule |
|---|---|---|
| Launch and modes | guest, free, real, `cwguestlogin.do`, `cwstartgamev2.do`, startgame wrapper, template fallback, new-games redirect | Verify exact supported launch paths and redaction requirements against current GS source/config. |
| External endpoint | Mantis describes a Start/Enter-style external-provider lane | Treat as candidate only until current GS source/config proves ExtGame support for Little Gangster. |
| Transaction processing | In an external-game model, transactions may be processed every spin, including feature spins | Translate to current lane as reserve/settle/process-equivalent rules. Do not assume `processTransactions` is the
production API. |
| State persistence | `gameState`, `lastAction`, Lasthand, reload/reconnect state | Verify whether GS/new-games runtime or a Little Gangster backend owns persisted state. |
| Round completion | `roundFinishedHelper` and `endRoundSignature` may determine whether a round is complete | Define Little Gangster round-complete fields in math handoff, then verify current GS consumption. |
| Restart / FRB transitions | `restartGame` may be required after FRB/bonus terminal states | Verify current GS restart and FRB/OCB support before implementing lane behavior. |
| Buy Feature | Mantis mentions buy-feature fields and RTP metadata | Keep donor feature-buy parity, but verify current GS representation before registration or wallet tests. |
| RNG | Local deterministic simulation is separate from production RNG | Browser RNG remains forbidden for production outcomes; production RNG owner remains a current-GS validation item. |
| VBA / VABS / history | External integrations may need history/replay endpoints | Do not assume external-side implementation; verify GS VABS/history support and linkage. |
| Win tiers | Mantis gives win-ratio bands | Treat as candidate animation thresholds unless current docs/source override. |
| Bet calculation | Fixed-line formula can cause traps | Little Gangster is 6x5 cluster; define the cluster equivalent and map it to GS bet config. |
| Max win | Separate cap multiplier from possible max win | Keep possible max win, cap multiplier, and cap events distinct in math/result contract. |
| Template parameters | Mantis template fields are useful checks | GameServerRegistrar must verify current GS fields before generation. |
| FRB / OCB / promos | FRB/OCB may be product/lane requirements | Product decision and current GS support must be verified. |
| closeSession | Some integrations require close/end behavior | Verify `/slot/v1/closegame`, `closeSession`, or lane equivalent. |
| Error/translations | Missing error keys and translations block release | GameClientBuilder and QA must test network, restart, session, wallet, unsupported, and translation states. |
| Infrastructure/certification | Dedicated infra, local source, bot tests, load tests may be required | RTPAndReleaseAuditor must gate release on runnable test evidence. |
| Debugging | Support needs sanitized request details | QA reports must include safe endpoint path, headers names, request/response shape, timestamp, gameId, mode, and roundId/spinId when safe. |

## Persistent Blockers

- `extgame_lane_unverified_for_current_gs`
- `vabs_lasthands_history_contract_unverified`
- `round_completion_contract_unverified_for_current_gs`
- `production_rng_owner_unverified_for_current_gs`
- `frb_ocb_promo_support_decision_pending`
- `current_gs_lane_validation_partial`

## Guardrails

- ExtGame cannot be named as the chosen Little Gangster lane without current-GS proof.
- External endpoint launch/runtime behavior cannot be assigned to Little Gangster without current-GS proof.
- `HOSTING_MODE` must remain undecided for ExtGame unless current GS/config evidence selects it.
- `processTransactions` must remain a lane-dependent checklist item unless current GS proves that exact API.
- VBA/history ownership must remain open until the selected lane proves whether GS or Little Gangster owns it.
