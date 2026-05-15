# 8001 Wallet/Launch/History Responsibility Test Matrix

Date: 2026-05-15
Status: future test scope, no tests run

| Area | Future Test | Expected Owner | Current Status |
| --- | --- | --- | --- |
| Launch | launch URL produces valid session context | GS/WebGS + registration/config | blocked pending approved environment |
| Open game | `/slot/v1/opengame` returns runtime envelope and does not mutate wallet directly in browser | new-games runtime + GS session | blocked
pending tests |
| Resume | reconnect restores lifecycle state and pending action markers | lifecycle wrapper + GS session persistence | blocked pending tests |
| Close | close game triggers GS close/session finish behavior | GS game processor/session persistence | blocked pending tests |
| Balance display | client displays envelope balance only | browser/client display | blocked pending client build |
| Wallet auth | auth uses configured GS/wallet provider path | GS wallet manager/provider | blocked pending safe wallet config |
| Bet/debit | base spin creates reserve/debit reference | GS wallet bridge/provider; wrapper references | blocked pending wallet tests |
| Win/credit | settlement creates credit/settle reference | GS wallet bridge/provider; wrapper references | blocked pending wallet tests |
| Refund/rollback | failed action uses proven GS rollback/refund path | GS wallet bridge/provider | blocked, exact 8001 path unproven |
| Idempotency | duplicate client operation does not double debit/credit | runtime + GS internal bridge | blocked pending tests |
| Pending/stuck | unresolved transaction surfaces blocked state | GS wallet tracker/persistence + wrapper marker | blocked pending tests |
| Session persistence | session survives reconnect/close | Cassandra/GS session storage | blocked pending tests |
| Round persistence | round/action history stored durably | Cassandra/GS bet/round storage | blocked for 8001 durable source |
| Last hand | last hand persists/replays | GS history/Lasthand + 8001 payload | blocked pending tests |
| VABS visual route | canonical and alias visual routes render safe replay | 8001 route foundation + GS/BO config | BO/CM acceptance blocked |
| BO/CM history | CM/backoffice opens configured visual route | BO/CM + GS configured URL | blocked pending acceptance |
| Restart/FRB | restart-required and FRB transitions are honored | GS FRB/session + lifecycle flag | blocked pending tests |
| Cap enforcement | cap state is server-side and history-visible | game runtime/lifecycle + config | blocked pending wallet/history tests |
| Logs/errors | errors and wallet failures have traceable safe logs | GS/new-games server | blocked pending tests |
| Registration config | wallet/history fields mapped before generation | GameServerRegistrar + GS config evidence | generation blocked |

## Scope Guard

This matrix tests ownership boundaries. It does not grant permission to call real
wallet, GS, BO/CM, DB, or Cassandra endpoints.
