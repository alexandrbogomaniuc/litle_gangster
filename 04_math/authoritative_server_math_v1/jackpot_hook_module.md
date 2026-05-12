# Jackpot Hook Module

Default state:

- `jp_enabled`: false.
- `jp_hook_available`: true for future extension.
- `jackpot_product_decision_pending`: true.

The design does not assume active jackpots.

Hook options:

- Trigger after base spin result.
- Trigger after feature spin result.
- Trigger from special reveal.
- Trigger from coin reveal.
- Trigger from separate jackpot contribution service.

Required boundaries if enabled:

- Jackpot accounting is outside `gamePayload`.
- Jackpot contribution and award state must be server-owned.
- Jackpot award history must include event id, tier, display label, and accounting reference.
- Jackpot RTP impact must be separately reported.

Blocked until:

- Product decision.
- Jackpot math tables.
- Accounting integration.
- Certification plan.

