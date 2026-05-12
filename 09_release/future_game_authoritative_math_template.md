# Future Game Authoritative Math Template

Every future game should provide:

- server result owner decision.
- math state machine.
- RNG draw plan.
- feature modules.
- bonus-buy and jackpot boundaries.
- state persistence contract.
- history / VABS / Lasthands contract.
- backend adapter input contract.
- runtime payload output contract.
- simulation and certification plan.
- strict fixtures.
- schema validation report.
- release gate.

Template principles:

- Browser renders only.
- Registration is metadata only.
- Runtime adapter maps server result to transport.
- Game-specific render data uses `presentationPayload.gamePayload`.
- Public or reviewer claims must be validated against actual artifacts.

Little Gangster is intended to become this reference template after implementation and validation.

