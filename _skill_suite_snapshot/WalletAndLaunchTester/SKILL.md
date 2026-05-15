---
name: WalletAndLaunchTester
description: Test launch and BSG Common Wallet behavior with configurable mock fixtures, exact hash rules, XML responses, and no production calls.
---

# WalletAndLaunchTester

## Purpose
Test launch and wallet behavior.

## When To Use
Use after protocol mapping and registration generation.

## Required Inputs
Protocol contract, launch contract, generated registration artifacts, test secret references or fixture PASS_KEY, mock EC config, and lane-dependent
transaction/restart/history/promo checklist items. ExtGame names are used only when ExtGame is proven.

## Preconditions
Read `BSG_COMMON_WALLET_SUMMARY.md` and wallet hash rules.

## Forbidden Actions
No production EC calls, raw secret logging, fake pass results, or hardcoded endpoint paths unless docs prove them.

## Workflow
1. Configure mock EC/server endpoints.
2. Validate MD5 hash with secret reference or fixture only.
3. Default response format: XML/EXTSYSTEM unless live code proves JSON.
4. Test REAL launch, FREE/guest launch if supported, token redaction, Authenticate, bet, win, bet/win separation, amount/transaction formatting,
   duplicate/idempotency, failed bet refund, failed win retry, zero-win final operation if required, `isRoundFinished`, jackpot/promo/negativeBet
   when supported, balance accounting, reload/reconnect, timeout/fail-safe.
5. Generate wallet and launch reports.
6. Add lane-dependent safe fixture tests for process-transaction-equivalent behavior, restart/resume, state restoration, round completion,
   VABS/VBA/history, FRB, OCB, and closeSession/closegame where required. Use `processTransactions`/`restartGame` ExtGame names only if that lane
   is proven. If definitions are missing, mark rows blocked instead of passed.
7. Before wallet/launch tests, require a GS/wallet/runtime responsibility boundary audit
   or equivalent current-GS evidence. WalletAndLaunchTester tests approved boundaries
   and approved endpoints; it must not assume the browser, renderer, or game runtime
   owns the real wallet ledger. Verify accounting references, provider settlement
   behavior, idempotency, pending/stuck transaction handling, and balance source
   through the selected GS/wallet path. Do not implement stuck transaction storage
   unless current GS source proves the game runtime owns it.

## Output Files
`08_qa/wallet_tests/*`, `launch_tests/*`, reports.

## Validation Checklist
All configured wallet calls checked, hashes verified, no raw secrets, failures explicit. Lane-dependent process/restart/history/FRB/OCB requirements
are tested with mocks or explicitly blocked.

## Handoff To Next Skill
Next: RTPAndReleaseAuditor.

## Failure / Blocker Handling
Missing secret references or exact hash rules block real validation.

## SprintReporter Handoff
Report test matrix, commands, pass/fail, and skipped reasons.

## Pilot Pipeline Hardening Addendum

Add lane-dependent tests for VABS/Lasthands/history, state recovery/reconnect, process-transaction or reserve/settle equivalents, restart/FRB/OCB
flows where current GS requires them, winTier/big-win thresholds, and runtime API contract validation. Use mock/local fixtures unless explicit safe
test endpoints are approved.

## Visual History Test Gate

Future games must test or explicitly block VABS/VBA/Lasthands visual history before
release. Wallet/launch testing should cover JSON replay plus visual/render route
behavior for round replay, session replay, whole-session replay, in-game History button
access, and Casino Manager/backoffice access. If only stored JSON exists and no current
GS evidence proves JSON-only replay is acceptable, mark visual history as blocked.

When a route-resolution audit exists, test the selected route model directly: configured
launch/bootstrap history URL, in-game History button, CM/backoffice visual access,
round/session/whole-session replay, and safe not-found/error responses. Do not replace
this with JSON-only `gethistory` checks unless the audit proves JSON-only is accepted.
For games with Little Gangster-style history foundations, test canonical VABS/VBA
routes and any approved legacy alias routes separately; BO/CM acceptance must pass or
remain an explicit blocker.

Also test evidence mode behavior: deterministic replay payload, visual route, selected
`historyEvidenceMode`, capture scope, media manifest when enabled, checksums, retention,
encryption, PII redaction, and blocked responses when media storage is unavailable.

## GS/Wallet Responsibility Boundary

Future games must clarify GS/wallet/runtime ownership before wallet/launch tests.
The client may display balance and submit actions, but real wallet auth, debit, credit,
refund/rollback, pending/stuck transaction recovery, and durable operation storage belong
to the current GS/wallet/provider path unless source proves otherwise. If the boundary is
unproven, block real wallet tests instead of assigning ownership to the game client.
