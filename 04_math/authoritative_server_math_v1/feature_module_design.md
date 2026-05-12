# Feature Module Design

Module model:

- Each feature module has deterministic server input, server-owned RNG consumption, state output, history output, and runtime render output.
- Modules must be independently testable and composable inside the round state machine.
- No module accepts browser-provided outcomes.

Required modules:

1. Base cluster/cascade module.
2. Golden-square module.
3. Rainbow activation module.
4. Coin reveal module.
5. Special reveal module.
6. Free spins / feature spins module.
7. Three feature modes module.
8. Bonus-buy module.
9. Optional jackpot hook module.
10. Max-win cap module.
11. Win-tier module.
12. VABS/history module.
13. State persistence module.

Common interface concept:

- Input: current authoritative game state, approved math config, RNG stream handle, event context.
- Output: next authoritative state, render events, history entries, audit references, blockers if config is incomplete.

Implementation status:

- Defined for planning.
- Not implemented.
- Backend adapter remains blocked until explicit source modification approval.

