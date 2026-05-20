# Future Game Visual Sandbox Gate

Future games may use VisualPrototypeSandboxBuilder when owners need to review visuals
before production client implementation is allowed.

This gate is useful when:

- GameClientBuilder implementation is blocked.
- Registration is blocked.
- Wallet endpoint tests are blocked.
- Release/certification are blocked.
- Donor/reference placeholders are available for internal review.

Passing this gate does not unlock production work. It only creates a safer internal
surface for visual feedback while technical, asset, registration, wallet, and release
gates remain closed.
