# VABS Lasthands History Completeness Matrix

Status: planning audit.

Terminology: VBS in this sprint is treated as the project VABS/VBA/Lasthands/history/replay evidence system.

Decision: deterministic replay payload is preferred over screenshot binary storage unless GS/product evidence proves screenshot or thumbnail storage is required. Blocker retained: `vabs_screenshot_requirement_unverified`.

| Requirement | Covered by current design | Evidence | Storage recommendation | Open blocker |
| --- | --- | --- | --- | --- |
| Round history | Yes, planning | authoritative history contract | server history record | implementation target unproven |
| Session history | Partial | GS bridge concepts and runtime contract | session-linked history records | 8001 mapping unproven |
| Lasthand | Partial | protocol checklist | deterministic replay payload | exact serialization unproven |
| VABS/VBA | Partial | advisory/current GS concepts | replay payload plus audit refs | exact GS package/path unproven |
| Screenshots or visual evidence | Not proven | no required binary screenshot proof | prefer deterministic replay | vabs_screenshot_requirement_unverified |
| Replay payload | Yes, planning | v0.3 strict fixtures and history contract | compact `gamePayload.payload` snapshot | storage target unproven |
| Presentation payload snapshot | Yes, planning | `presentationPayload.gamePayload` | snapshot or reconstructable payload | adapter not implemented |
| State snapshot | Yes, planning | state persistence module | state versioned snapshot | persistence owner unproven |
| gameState / lastAction equivalent | Partial | Mantis checklist only | map to selected lane state fields | current lane mapping unproven |
| Starting grid | Yes | v0.3 result/history design | store in replay payload | math implementation pending |
| Cascade steps | Yes | strict fixtures/v0.3 schema | ordered cascade events | math implementation pending |
| Final grid | Yes | history contract | final state snapshot | math implementation pending |
| Golden/rainbow/coin/special reveal | Yes, planning | feature modules | ordered events and state | exact rules pending |
| Feature mode state | Yes, planning | feature module design | mode state snapshots | exact mode rules pending |
| Bonus buy state | Yes, planning | bonus-buy module | purchase/start state | cost/EV pending |
| Free spins state | Yes, planning | free spins module | remaining spins/state | exact rules pending |
| Jackpot state if any | Hook only | jackpot module | disabled unless enabled | product decision pending |
| Cap/win tier | Yes | cap/win-tier modules | pre-cap/capped/tier fields | final thresholds pending |
| RNG audit references | Yes | RNG draw plan | references, not raw secrets | implementation pending |
| Wallet transaction reference | Yes boundary | adapter contracts | outside gamePayload | wallet integration pending |
| Recovery snapshot | Yes | persistence plan | resumegame/recovery state | runtime owner unproven |
| What not to store | Yes | history module | no raw secrets/RNG/browser authority | ongoing safety gate |

Completeness conclusion:

- Design coverage is broad enough for planning.
- Production completeness is not proven until exact 8001 history storage, Lasthand/VABS serialization, and screenshot-vs-replay requirements are verified.

Validation keyword coverage:

- round history.
- session history.
- presentation payload snapshot.
- starting grid.
- cascade steps.
- final grid.
- golden/rainbow/coin/special reveal.
- feature mode state.
- bonus buy state.
- free-spins state.
- jackpot state.
- cap/win tier.
- wallet transaction reference.
- recovery snapshot.
