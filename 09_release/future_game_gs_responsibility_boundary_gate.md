# Future Game GS Responsibility Boundary Gate

Date: 2026-05-15
Status: reusable workflow gate

## Rule

Every future game must clarify GS, wallet, runtime, client, storage, BO/CM, and
registration responsibility before WalletAndLaunchTester or GameServerRegistrar
generation.

## Required Decisions Before Wallet/Launch Tests

- browser/client is display and request orchestration, not the real wallet owner;
- runtime/lifecycle wrapper owns action intent, idempotency, state, result payload,
  history payload, and blockers;
- GS/WebGS/current platform owns launch/session control unless source proves otherwise;
- wallet/casino provider or GS wallet manager owns real balance settlement;
- Cassandra/config/cache/history storage owner is identified or blocked;
- pending/stuck transaction owner is identified or blocked;
- BO/CM/VABS/Lasthands route owner is identified or blocked;
- test environment and endpoint permissions are explicitly approved.

## Required Decisions Before Registration Generation

- wallet/config fields are proven or blocked;
- history/VABS route config fields are proven or blocked;
- registration does not create arbitrary wallet ownership;
- GameServerRegistrar does not guess bank/template fields;
- release remains blocked while ownership or test evidence is missing.

## Release Gate

Release audit must fail if responsibility boundaries are unresolved or if tests imply
that the browser/game client owns real wallet mutation without GS/source proof.
