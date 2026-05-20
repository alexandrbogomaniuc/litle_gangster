# Sandbox No-Endpoint Policy

Visual sandboxes must be offline/static unless a later sprint explicitly approves a
different local-only test harness.

Forbidden in sandbox files:

- GS calls
- wallet calls
- BO/CM calls
- VABS route calls
- DB/Cassandra calls
- loopback API calls
- external network calls
- raw private URLs, tokenized query strings, SIDs, signatures, or secrets

Static file loading from the sandbox folder is allowed. External images, scripts,
stylesheets, fonts, analytics, telemetry, or API calls are not allowed.
