# Little Gangster Authoritative Server Math v1

Status: planning design only.

This package defines the intended server-authoritative math, state, recovery, history, and certification design for Little Gangster. It does not implement runtime code, backend adapter code, browser client code, registration artifacts,
wallet calls, or release approval.

7001 / Crazy Rooster is not an authoritative math source for this package. It may only be used later as a structural reference for package layout, mapper style, test style, envelope usage, and presentation payload handling.

The recommended future owner is a game-specific server math/runtime module for Little Gangster, integrated through the patched `presentationPayload.gamePayload` runtime extension and a backend adapter. Ownership remains unproven until a
real approved implementation target exists.

Primary design goals:

- Server owns RNG, result generation, win evaluation, persistence, history, and recovery.
- Browser remains renderer-only.
- Registration remains metadata, configuration, and routing only.
- Jackpots are disabled by default, with documented hooks for future product approval.
- Double-up/gamble is out of active scope unless product evidence changes.
- The design should become a reusable reference template for future games.

Key blockers remain documented in `authoritative_math_blockers.md`.

