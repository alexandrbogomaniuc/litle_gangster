---
name: GameServerRegistrar
description: Generate safe Cassandra/Game Server registration and rollback artifacts from verified schema evidence without executing DB changes.
---

# GameServerRegistrar

## Purpose
Generate safe registration artifacts.

## When To Use
Use after client build and protocol mapping.

## Required Inputs
Manifest, game id/name/path, bank id/source, Cassandra contract, client dist path, RTP/bet config, current GS lane evidence, and advisory
  Mantis/ExtGame template checklist items. Do not assume ExtGame or any template field exists without current GS proof.

## Preconditions
Read `CASSANDRA_REGISTRATION_SUMMARY.md` and `03_protocol/cassandra_registration_contract.md`.

If registration fields depend on unresolved simulation evidence, require
ParallelMathValidator output before generation. Do not generate registration if
`POSSIBLE_MODELS`, `BF_RTP`, `BF_RTP_MIN`, `BF_BETS`, `SD_KEYS`, `MAX_WIN`,
`CAP_WIN_MULTIPLIER`, `POSSIBLE_MAX_WINS`, volatility, or `mathProfileId`
mapping are missing, unsupported, or not backed by simulation evidence or
explicit blockers.

## Forbidden Actions
No production DB apply, no Cassandra execution by default, no guessed tables, no `RCasinoKS_schema.cql` alone, no raw secrets.

## Workflow
1. Generate CQL/config only.
2. Generate rollback.
3. Validate table/keyspace evidence.
4. Include `gametinfocf`, `gameinfocf`, `bankinfocf`, bank assignment, `swfLocation`, servlet/path, RTP, bets, video capture if documented.
5. Mark `scn` blob/Java serialized fields blocked unless serializer/tool exists.
6. Create dev/stage apply instructions only after approval.
7. Verify current GS fields before generation. If ExtGame is proven, generate registration/template artifacts only after every ExtGame parameter is
  verified or explicitly blocked. If a different lane is selected, translate advisory checklist items into that lane's fields and do not infer
  `HOSTING_MODE=EXTGAME`, `processTransactions`, `gameState`, `roundFinishedHelper`, `restartGame`, or VBA/FRB/OCB flags.
8. Check ParallelMathValidator reports when present. Registration math fields
   must preserve `RTP_WITHOUT_BF` separately from `BF_RTP`, preserve
   `RTP_MIN_WITHOUT_BF` separately from `BF_RTP_MIN`, enforce
   `BF_RTP <= POSSIBLE_MODELS`, and block generation when CAP_WIN/MAX_WIN
   states are unresolved.

## Output Files
`07_registration/cql/*`, `rollback/*`, `validation/*`, `registration_report.md`, reports.

## Validation Checklist
CQL parses heuristically, rollback exists, unknown serializer blocked, no apply command run. Template parameters are evidence-linked, redacted,
  lane-appropriate, and not guessed.

## Handoff To Next Skill
Next: WalletAndLaunchTester.

## Failure / Blocker Handling
Missing bank/source/schema evidence blocks registration.

## SprintReporter Handoff
Report generated CQL, rollback, table evidence, and no-apply status.

## Pilot Pipeline Hardening Addendum

Require a registration-vs-math-import boundary before generating artifacts. Verify current GS fields and scn/jcn or equivalent serializer/tooling
  before generation. Generate registration and rollback artifacts only after approval, and never assume registration imports executable math unless
  current GS source proves it.
