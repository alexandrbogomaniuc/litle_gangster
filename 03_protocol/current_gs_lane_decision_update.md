# Current GS Lane Decision Update

## Decision Table

| Candidate lane | Evidence | Missing evidence | Risks | Current status | Recommended use |
|---|---|---|---|---|---|
| new-games / `slot-browser-v1` | Current GS has New Games route keys, New Games launch redirect, WebGS internal bridge, `new-games-server` `/slot/v1/*`, and Gamesv1 client protocol. | 8001 registration missing; final result owner unproven;
v0.3 math integration not implemented; serializer/tooling blocked. | Strong candidate may still be wrong if current deploy route or runtime package differs. | LIKELY/CANDIDATE | PROCEED_WITH_LIMITS for MathModelDesigner contract work only.
|
| legacy `template.jsp` / WebSocket | Current GS still has legacy template redirect and `SPGameProcessor` infrastructure. | No Little Gangster 8001 legacy game processor/client source. | Would require larger client/runtime assumptions and
possibly browser template mismatch. | CANDIDATE | BLOCKED_PENDING_EVIDENCE. |
| ExtGame external backend | Mantis checklist exists; Gamesv1 has a deprecated `ExtGameTransport` alias; GS has external ID mapping table. | No current source proof of Little Gangster needing ExtGame endpoint or `HOSTING_MODE=EXTGAME`. |
Could force wrong architecture. | CANDIDATE/UNVERIFIED | DO_NOT_USE unless proven. |
| mixed lane | New Games route plus WebGS internal wallet/history bridge is effectively mixed; runtime math owner could be separate. | Ownership and deploy topology unproven for 8001. | Boundary confusion: registration, wallet, runtime, and
math must stay separate. | CANDIDATE | PROCEED_WITH_LIMITS as architecture question. |
| unknown | Remaining blockers are material. | Requires 8001 config/runtime proof. | Blocks registration/client release. | BLOCKED | Use until runtime owner and registration pipeline are verified. |

## Recommended Current Position

Current recommended lane: `new-games / slot-browser-v1` as strongest candidate, not final.

GameClientBuilder remains blocked for full build. MathModelDesigner retry may proceed as a boundary/schema contract task because it can produce backend-oriented outputs without selecting the final runtime owner.
