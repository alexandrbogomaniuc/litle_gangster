# AuthorizedReferenceResearcher Preflight Blocker Resolution

## Scope

This preflight verified only the explicit paths and values provided by the user for workflow test stage 2. No alternative paths were searched. Secret-bearing files were not read for raw values.

## Verification Results

| Key | Path | Exists | Readable | Type | Used for | Verification result | Blocker |
|---|---|---:|---:|---|---|---|---|
| Portal / preloader client | `[DEV_ROOT]/_worktrees/7000-release-pack-skeleton-20260322-1858/new-games-client` | yes | yes | directory | Candidate portal/preloader client root | Path exists/readable | none |
| Actual Crazy Rooster game package | `[DEV_ROOT]/_worktrees/7000-release-pack-skeleton-20260322-1858/Gamesv1/games/7001` | yes | yes | directory | Candidate client source root/reference game package | Path exists/readable | none |
| Active GS source | `[DEV_ROOT]/_worktrees/7000-release-pack-skeleton-20260322-1858/gs-server` | yes | yes | directory | Candidate Game Server source root | Path exists/readable | none |
| Base template / architecture reference | `[DEV_ROOT]/_worktrees/7000-release-pack-skeleton-20260322-1858/Gamesv1/games/premium-slot` | yes | yes | directory | Candidate template game path | Path exists/readable | none |
| Legacy GS JSP shell | `[DEV_ROOT]/GSRefactor-beta-local-procedure-live-20260307/gs-server/game-server/web-gs/src/main/webapp/real/mp/template.jsp` | yes | yes | file | Candidate launch template path | Path exists/readable | none |
| New-games launch routing logic | `[DEV_ROOT]/_worktrees/7000-release-pack-skeleton-20260322-1858/gs-server/game-server/web-gs/src/main/java/com/dgphoenix/casino/actions/enter/game/cwv3/CWStartGameAction.java` | yes | yes | file |
Candidate launch routing source | Path exists/readable | none |
| Base launch action | `[DEV_ROOT]/_worktrees/7000-release-pack-skeleton-20260322-1858/gs-server/game-server/web-gs/src/main/java/com/dgphoenix/casino/actions/enter/game/BaseStartGameAction.java` | yes | yes | file | Candidate launch
routing source | Path exists/readable | none |
| Live bank/config export | `[DEV_ROOT]/docker-groups/refactoredgs-microservices/release-zero-20260423T141209Z/runtime/export_localmachine/com.abs.casino.common.cache.BankInfoCache.xml` | yes | yes | file | Candidate bank/config/default
bank/coin/PASS_KEY reference source | Path exists/readable; raw values not read | none |
| Live release stack compose | `[DEV_ROOT]/docker-groups/refactoredgs-microservices/release-zero-20260423T141209Z/docker-compose.yml` | yes | yes | file | Candidate release stack reference | Path exists/readable | none |
| Canonical Crazy Rooster runbook | `[DEV_ROOT]/_worktrees/7000-release-pack-skeleton-20260322-1858/Gamesv1/games/7001/docs/GS_7001_NEWGAMES_RUNBOOK.md` | yes | yes | file | Candidate bank/subCasino/runbook source | Path exists/readable |
none |
| PASS_KEY property declaration file | `[DEV_ROOT]/GSRefactor-beta-local-procedure-live-20260307/gs-server/common/src/main/java/com/abs/casino/common/cache/data/bank/BankInfo.java` | yes | yes | file | Candidate PASS_KEY property
declaration source | Path exists/readable; raw values not applicable | none |
| Support/default token source | `[DEV_ROOT]/runtime-patches/commonwallet/commonWallet.jsp` | yes | yes | file | Candidate test token/user reference source | Path exists/readable; token values not read | none |
| Probe/canary token source | `[DEV_ROOT]/GSRefactor-beta-local-procedure-live-20260307/gs-server/deploy/scripts/phase4-protocol-wallet-canary-probe.sh` | yes | yes | file | Candidate test token/user reference source | Path exists/readable;
token values not read | none |

## Manifest Updates Applied

- `reference.reference_mode` changed to `authorized_capture_for_internal_scaffold`.
- `reference.authorization_status` changed to the user-provided internal scaffold authorization statement.
- Client, portal client, template, launch template, launch routing, Game Server, Cassandra/config, release stack, default bank/source, PASS_KEY secret-reference, test-user secret-reference, and coin-denomination fields were updated only
from explicit user-provided inputs with path presence/readability verified where paths were supplied.
- PASS_KEY and test-user raw values were intentionally not read, printed, copied, or persisted.

## Remaining Preflight Blockers

- Raw PASS_KEY values remain intentionally unavailable and must stay out of chat/files.
- Raw test-user/token values remain intentionally unavailable and must stay out of chat/files.
- Path contents are not verified as protocol/build truths until their dedicated future skills are explicitly run.
