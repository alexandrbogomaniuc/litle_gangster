# Current GS RNG / Result Ownership Audit

## Direct Answer

RNG/result generation is not proven to be owned by classic GS for Little Gangster. Current Staging evidence shows:

- classic GS has RNG utilities and legacy game processor infrastructure;
- WebGS New Games internal API owns session, wallet, idempotency, and history bridge;
- `new-games-server` currently generates deterministic sample outcomes and presentation payloads before calling GS reserve/settle/history;
- browser/client RNG for production outcomes is not supported and remains forbidden.

Final Little Gangster result owner remains `UNKNOWN/BLOCKED`.

## Evidence Matrix

| Question | Answer | Status | Evidence |
|---|---|---|---|
| Is RNG/result generation on GS side? | Classic GS has RNG utilities and game processor classes, but no Little Gangster/8001 processor exists and no proof was found that GS will run Little Gangster math. | CANDIDATE | `RNG.java:20-120`;
`InternalRNG.java:15-156`; `SPGameProcessor.java:22-65`; `AbstractGameProcessor.java:43-95`. |
| Which GS component if yes? | Possible legacy `SPGameProcessor` / `AbstractSPGameEngine` style, but not selected for Little Gangster. | CANDIDATE | Runtime template exports use `SPGameProcessor`; no 8001 template exists. |
| Is result generation in New Games backend? | New Games server currently creates deterministic outcomes in `/v1/placebet` and presentation payloads for game 7001. | LIKELY for sample/provisional New Games flows, not final for 8001 |
`new-games-server/src/index.ts:453-465`, `472-565`, `1165-1321`, `1700-1764`. |
| Does WebGS internal bridge generate results? | No direct evidence. It validates session, reserves, settles, and reads/writes history. | NOT_FOUND | `NewGamesInternalApiServlet.java:62-67`, `156-221`, `224-299`, `301-375`. |
| Is there browser/client RNG for real results? | No production-authoritative browser result generation should be allowed. `Math.random` in client transport is request ID fallback, not outcome generation. | PROVEN as forbidden policy;
NOT_FOUND as production result source | `GsHttpRuntimeTransport.ts:48-53`; project policy. |
| Does current source show certified/central RNG? | GS has RNG utility classes using `/dev/random`, `SecureRandom`, and Mersenne Twister; certification status and Little Gangster consumption are unproven. | CANDIDATE | `RNG.java:20-79`;
`InternalRNG.java:15-17`. |
| What must v0.3 output? | A backend-oriented result contract independent of registration: cascade steps, state, feature modes, cap state, wallet/accounting handoff values, and metadata values for registration separately. | PROVEN as
project requirement | v0.3 docs and this audit. |

## Owner Candidates

| Candidate owner | Status | Reason |
|---|---|---|
| Classic GS processor | CANDIDATE | Existing GS processor and RNG utilities exist, but no 8001 game processor evidence. |
| New Games backend | LIKELY/CANDIDATE | Source currently generates sample outcomes and mediates `/slot/v1` flows, but final Little Gangster integration is not implemented. |
| Game-specific backend package | CANDIDATE | Could consume v0.3 math package if selected. No current 8001 package exists. |
| Browser client | DO_NOT_USE | Browser must remain non-authoritative for real-money results. |
| Cassandra registration | NOT_FOUND | No executable math import found in registration stores. |

## Blockers

- `runtime_result_owner_unproven`
- `production_rng_owner_unverified_for_current_gs`
- `game_8001_runtime_package_missing`
- `core_protocol_contract_needs_final_runtime_alignment`
