# Mantis Template Parameter Registration Checklist

Status: checklist only; no registration artifacts generated.

## Scope Rule

Do not assume `HOSTING_MODE=EXTGAME`. Do not assume Mantis template fields exist in current GS. Do not generate Cassandra or template registration until GameServerRegistrar verifies current GS schema/config and creates rollback artifacts.

## Later Registrar Checks

| Area | Required validation |
|---|---|
| Lane selection | Verify whether 8001 uses new-games, legacy template, ExtGame, or mixed lane from current GS config/source. |
| Template fields | Verify every used field against current GS classes, support UI, schema, or existing registration examples. |
| RTP fields | Store RTP and max-win as metadata/display/config unless current source proves executable math import. |
| Bet fields | Map 6x5 cluster bet model to GS min/default/max/coin config. |
| Buy feature | Verify buy-feature pricing/EV/config fields before generating. |
| FRB/OCB | Verify product decision and current GS support before adding flags. |
| Round finish | Verify `roundFinishedHelper` / `endRoundSignature` need for 8001. |
| VABS/history | Verify history/VABS config path and renderer package needs. |
| Secrets | Use secret references only. Never store raw PASS_KEY, token, SID, signature, or private endpoint values. |

## Generate-Only Boundary

Future GameServerRegistrar must remain generate-only until explicitly approved for a dev/stage apply. This sprint generated no CQL, no rollback CQL, and no DB changes.

