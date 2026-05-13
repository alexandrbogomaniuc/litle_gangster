# RNG Testing And Certification Checklist

Status: advisory QA/release checklist.

## Current Source Signals

| Topic | Evidence | Meaning |
|---|---|---|
| GS RNG utility | `rng/src/main/java/com/dgphoenix/casino/common/util/RNG.java:20-76` seeds GS utility RNG from system entropy sources. | Current GS has RNG utilities, but Little Gangster production RNG owner is not proven. |
| New-games provisional result generation | `new-games-server/src/index.ts:453-465` derives deterministic outcomes from a hash and runtime salt for current demo/provisional flow. | Backend creates outcomes in current new-games server;
release-grade RNG/certification remains unproven. |
| Browser random use | 7001 browser code uses `Math.random` for visual particles/effects and a provisional math source in demo/runtime files. | Browser random is acceptable for presentation only, not production outcome authority. |

## Required Gates

- Local math simulation may use deterministic pseudo-random seeds.
- Production browser RNG is forbidden for real-money outcomes.
- Production RNG owner must be proven from current GS/new-games runtime or approved backend runtime.
- Bot testing must cover normal spins, feature modes, bonus buy, caps, retries, restart/resume, and history.
- Certification package must include source/build context, local runnable environment, test reports, and RNG/state recovery evidence.
- Release audit must retain 10M-spin or product-required long-run gate if required by certification policy.

## Blockers

- `production_rng_owner_unverified_for_current_gs`
- `certification_rng_evidence_missing`
- `bot_test_volume_requirement_unverified`
- `state_recovery_certification_missing`

