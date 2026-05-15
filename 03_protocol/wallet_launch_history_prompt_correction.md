# Wallet/Launch/History Prompt Correction

Date: 2026-05-15
Status: reusable prompt correction

## Replace Unsafe Assumptions

Avoid prompts that say or imply:

- the game client owns wallet;
- the renderer stores real balance;
- the Little Gangster `gamePayload` is accounting truth;
- stuck/pending transaction storage should be implemented in runtime without GS proof;
- repeated balance polling is equivalent to settlement.

## Use Correct Prompt Language

Use:

```text
Verify accounting boundary and references. Verify wallet/provider settlement behavior
through an approved test environment. Do not assume the browser/client or game runtime
owns real wallet state. Do not implement stuck transaction storage unless current GS
source proves the game runtime owns it. Treat wallet auth, reserve/debit, settle/credit,
refund/rollback, pending/stuck transaction tracking, session persistence, durable
history, and BO/CM access as GS/platform/provider responsibilities unless source proves
otherwise.
```

## Future WalletAndLaunchTester Scope

WalletAndLaunchTester should test approved endpoints and boundaries after explicit
environment approval. It should report which layer owns each observed behavior, which
references are returned to the runtime/client, and which blockers remain.

## Current Sprint Boundary

No wallet endpoints, GS endpoints, BO/CM endpoints, DB/Cassandra actions, servers, or
local server browsing occurred.
