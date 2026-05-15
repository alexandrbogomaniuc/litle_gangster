# 8001 Registration Settings Dependency After Lifecycle Audit

Date: 2026-05-15
Status: planning only, generation blocked

## Summary

GameServerRegistrar generation remains blocked. The lifecycle wrapper and VABS route plan do not resolve registration settings. They make the
dependencies
more explicit.

## Required Dependencies

| Setting | Dependency / blocker |
| --- | --- |
| `POSSIBLE_MODELS` | Must map the 3x3 `mathProfileId` set to current GS model semantics. |
| `RTP_WITHOUT_BF` | Must carry base RTP values separately from BF_RTP. |
| `BF_RTP` | Exact current-GS key mapping unproven; do not generate until proven. |
| `BF_RTP_MIN` | Exact current-GS key mapping unproven; do not generate until proven. |
| `SD_KEYS` | Exact current-GS key mapping unproven; map to SD/KPI route or block. |
| `FeatureKPI` | Feature categories need mapping for base, free spins, bonus buy, caps, and special features. |
| `CAP_WIN_MULTIPLIER` | Planning-only mapping; cap/tail confirmation still pending. |
| `MAX_WIN` | Supported concept, final value and product/regulatory readiness pending. |
| `POSSIBLE_MAX_WINS` | Planning-only; must not be equated blindly with cap multiplier. |
| `GL_MIN_BET_DEFAULT` | Exact Little Gangster value and current GS unit basis required. |
| `GL_MAX_BET_DEFAULT` | Exact Little Gangster value and current GS unit basis required. |
| `GL_DEFAULT_BET` | Exact Little Gangster value and current GS unit basis required. |
| `POSSIBLE_LINES` | Cluster-slot compatibility must be confirmed. |
| `LINES_COUNT` | Cluster-slot compatibility must be confirmed. |
| `DEFAULTNUMLINES` | Cluster-slot compatibility must be confirmed. |
| `DEFAULTBETPERLINE` | Cluster-slot compatibility must be confirmed. |
| `BF_BETS` | Exact current-GS key mapping unproven; 100x standard candidate only. |
| `LANGUAGES_SUPPORTED` | Exact current-GS key mapping unproven; language route still required for VABS/launch. |
| `isFrb` | FRB behavior needs scope decision or mapping. |
| `FRB_COIN` | Required if FRB/free-round behavior is in scope. |
| `roundFinishedHelper` | Must be mapped to round completion contract. |
| `endRoundSignature` | Must be mapped to round completion contract. |
| VABS/VBA URL fields | Required if current GS history routes need preconfigured URLs or template params. |

## Generation Decision

GameServerRegistrar generation allowed: false.

Generate-only registration may be reconsidered only after lifecycle wrapper contract acceptance, VABS route planning acceptance, settings key mapping
proof,
wallet/history tests, and explicit user approval.
