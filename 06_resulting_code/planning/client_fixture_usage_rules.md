# Client Fixture Usage Rules

Status: PLANNING_ONLY.

## Allowed

- Use the 24 fixture JSON files for renderer planning and scene/object review.
- Use fixture payloads to design animation sequencing for cascades, reveals, features, cap state, and reconnect.
- Use fake IDs and non-production data only.
- Keep all fixture work under `06_resulting_code/planning` unless a future prompt explicitly approves a static prototype.

## Not Allowed

- Treat fixtures as production runtime proof.
- Treat fixtures as wallet payloads or registration metadata.
- Use fixtures to certify RTP, payouts, or production RNG.
- Package donor/scaffold assets or production client code.
- Generate a production GameClientBuilder app from fixtures without runtime owner and result API proof.

## Prototype Boundary

A future static renderer prototype may be started only if the user explicitly approves it. That prototype must be fixture-only, non-production, and clearly separate from full GameClientBuilder implementation.
Evidence label summary: PROVEN_PROJECT_FIXTURES for fixture inventory; CONDITIONAL_PLANNING_ONLY for future static prototype; BLOCKED for production implementation.

