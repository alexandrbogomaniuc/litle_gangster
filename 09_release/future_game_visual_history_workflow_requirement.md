# Future Game Visual History Workflow Requirement

Created: 2026-05-15

## Reusable Rule

Future games must implement or explicitly block visual history/VBA/VABS/Lasthands routes
before release. Stored JSON alone is not enough unless current GS/backoffice evidence
proves JSON-only replay is acceptable.

Every future game must also choose a `historyEvidenceMode`, `historyCaptureScope`, and
`historyMediaStoragePolicy` before release. Deterministic replay remains authoritative;
screenshots and videos are optional supporting evidence controlled by game-level
settings.

## Required Future-Game Coverage

- round replay
- session replay
- whole-session replay
- in-game History button behavior
- Casino Manager/backoffice access
- deterministic replay payload
- visual HTML/render response or accepted blocker
- wallet/accounting references
- math profile identity
- RTP level and volatility level
- feature and bonus-buy state where applicable
- safe not-found and blocked responses
- selected history evidence mode
- screenshot/video media policy if enabled
- storage, retention, checksum, encryption, and PII-redaction policy

## Required Skill Flow

- ProtocolAndSchemaMapper must map visual history route requirements.
- ProtocolAndSchemaMapper must map evidence storage policy and game-level media settings.
- Before implementation, ProtocolAndSchemaMapper must run a route-resolution audit
  against legacy GS/global routes, new-games-server routes, client History behavior,
  Casino Manager/backoffice access, and registration/bootstrap settings.
- GameClientBuilder must not complete release client scope if the History button route
  behavior is unknown.
- WalletAndLaunchTester must test visual history or record it blocked.
- RTPAndReleaseAuditor must block release if visual history is missing without explicit
  evidence-backed acceptance.
- RTPAndReleaseAuditor must block release if evidence mode or media policy gates are
  unresolved.

## Little Gangster Status

Little Gangster 8001 has lifecycle wrapper support, JSON history payload planning, and
visual history source planning. VABS/VBA/Lasthands visual route implementation remains
pending and release-blocking.

## Route-Resolution Audit Lesson

Legacy GS evidence may expose visual history through configured/generated VABS URLs,
while new-games may expose JSON history through `/slot/v1/gethistory`. Future games
must not collapse those into the same gate. Select and document a route-resolution model
before source implementation.

## Evidence Policy Lesson

Full video capture for every spin is not a reusable default. Use deterministic replay
and required visual render first; enable screenshots or videos only by explicit
game-level policy, storage/retention/security policy, and release approval.
