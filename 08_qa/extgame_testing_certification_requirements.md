# ExtGame Testing And Certification Advisory Checklist

Generated: 2026-05-11
Corrected: 2026-05-11

## Scope

This is an advisory checklist. It does not select ExtGame and does not prove that Little Gangster must expose external endpoints.

## Current-Lane QA Translation

WalletAndLaunchTester and RTPAndReleaseAuditor must test or block the current-lane equivalents of:

- process-transaction behavior.
- restart/resume behavior.
- game state restoration.
- round completion.
- VABS/VBA/history.
- FRB/OCB/promos if product/current GS scope requires them.
- RNG/bot/certification gates.

## Release Rule

Release remains blocked if any required current-lane behavior is undefined, untested, or documented only by secret-bearing evidence.

