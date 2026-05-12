# RNG Draw Plan

RNG owner: server-side authoritative math module.

Browser RNG status: FORBIDDEN for production outcomes.

Draw categories:

| Category | When Consumed | Owner | State Record | RTP Impact | Simulation | History | Lab Review |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Base grid symbols | `base_grid_generate` | Server math | initial grid draw reference | Yes | deterministic seed stream | starting grid | Required |
| Cascade refill symbols | each `cascade_step` refill | Server math | per-cell refill draw reference | Yes | deterministic seed stream | refill symbols | Required |
| Feature trigger decisions | after cluster/cascade resolution | Server math | trigger decision reference | Yes | trigger frequency report | trigger event | Required |
| Golden-square decisions | during base/cascade/feature rules | Server math | before/after golden state | Yes | state frequency report | golden events | Required |
| Rainbow activation decisions | eligible activation windows | Server math | activation event reference | Yes | activation frequency report | rainbow event | Required |
| Coin tier/value decisions | reveal window | Server math | tier/value reference | Yes | value distribution report | coin reveal | Required |
| Special reveal decisions | eligible special reveal window | Server math | pot/clover decision reference | Yes | feature contribution report | special reveal | Required |
| Feature mode selection | feature entry or bonus buy start | Server math or approved player choice validator | mode reference | Yes | mode split report | feature entry | Required |
| Feature spin outcomes | every feature spin | Server math | feature spin draw references | Yes | feature RTP report | feature spin snapshots | Required |
| Bonus-buy mode/start state | purchase accepted | Server math | purchase and start references | Yes | bonus buy RTP report | purchase/start snapshot | Required |
| Jackpot hook decisions | only if jackpot enabled | Server jackpot/math integration | jackpot event reference | Yes if enabled | jackpot contribution report | jackpot event | Required if enabled |
| Max-win cap handling | after any win addition | Server math | cap check state | Yes as payout cap | cap frequency report | cap event | Required |

Audit policy:

- Store deterministic replay references, draw indexes, model version, and seed batch references.
- Do not store raw RNG secrets in gameplay payloads or public reports.
- Reconnect must replay from committed state, not re-consume RNG.
- Bot testing and certification simulations must use controlled deterministic runs.

Open blockers:

- Exact symbol weights.
- Exact feature trigger probabilities.
- Bonus-buy cost and EV.
- Free-spin mode details.
- Jackpot product decision.

