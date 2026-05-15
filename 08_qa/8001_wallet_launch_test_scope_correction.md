# 8001 Wallet/Launch Test Scope Correction

Date: 2026-05-15
Status: audit only, no tests run

## Scope Correction

WalletAndLaunchTester must verify wallet and launch boundaries. It must not assume that
the browser, renderer, or Little Gangster `gamePayload` owns the real wallet ledger.

Use this language in future prompts:

- verify accounting boundary and references;
- verify wallet/provider settlement behavior through an approved test environment;
- do not assume game runtime owns wallet;
- do not implement stuck transaction storage unless GS source proves the game runtime
  owns it;
- verify that client balance display comes from runtime/settlement responses, not from
  client-side balance ownership;
- verify that pending/stuck transaction states are surfaced and blocked safely.

## What WalletAndLaunchTester Should Test Later

- launch/session creation through the approved GS lane;
- open game, resume game, close game, restart/FRB transition, and reconnect behavior;
- base spin reserve/debit reference;
- base spin settle/credit reference;
- free-spin/feature result accounting representation;
- bonus-buy purchase debit reference and feature result reference;
- rollback/refund behavior if GS route is proven and approved;
- idempotency and duplicate request behavior;
- pending/stuck operation behavior returned by GS/wallet paths;
- balance in envelope after reserve/settle;
- history/VABS/Lasthands references after actions;
- safe logs/errors without raw secrets.

## What WalletAndLaunchTester Must Not Own

- direct wallet mutation in the game client;
- durable wallet operation storage;
- casino provider ledger state;
- Cassandra schema changes;
- BO/CM acceptance;
- registration generation;
- release approval.

## Current Status

No wallet, GS, BO/CM, Cassandra, DB, or local server endpoints were called in this sprint.
Future real endpoint tests require explicit approval and safe environment evidence.
