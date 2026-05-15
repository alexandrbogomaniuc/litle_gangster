# 8001 Lifecycle Wrapper Implementation Gate

Date: 2026-05-15
Status: gate only, no approval

## Gate Rules

- Lifecycle wrapper implementation requires separate explicit approval.
- VABS visual history route implementation requires separate explicit approval.
- Backend adapter payload mapper may remain, but it needs a lifecycle wrapper.
- GameClientBuilder remains blocked until lifecycle wrapper contract is accepted.
- GameServerRegistrar remains blocked until registration settings dependencies are resolved.
- WalletAndLaunchTester must run only after wrapper implementation exists and is explicitly approved for safe testing.
- Release remains blocked.

## Current Allowed Work

- Planning and documentation.
- Source planning for wrapper/route shape if explicitly requested.

## Current Forbidden Work

- Staging source modifications.
- Backend adapter changes.
- VABS/VBA route implementation.
- GameClientBuilder implementation.
- GameServerRegistrar generation/apply.
- Registration artifacts.
- DB/Cassandra changes.
- Wallet/API calls.
- Donor browsing or asset capture.
- Release approval.

## Required Approval Text For Next Implementation Sprint

Any future implementation sprint must explicitly approve the exact Staging source root and files to modify. Without that approval, implementation
  remains blocked.
