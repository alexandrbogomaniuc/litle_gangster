# VABS Evidence Storage Policy

Generated: 2026-05-15

## Scope

This policy defines the reusable evidence model for Little Gangster and future games.
It is planning only. No VABS route code, screenshot capture, video capture, durable
storage, DB action, wallet call, registration artifact, client code, or release approval
was created by this sprint.

## Evidence Principle

Authoritative deterministic replay is the source of truth.

Visual HTML VABS/history routes are required for Casino Manager/backoffice and in-game
History unless current GS evidence proves JSON-only replay is acceptable.

Screenshots and videos are optional supporting evidence. They can help quick audit and
dispute workflows, but they must not replace deterministic replay and must not be the
only source needed to reconstruct a round/session.

## Evidence Layers

### 1. Authoritative Deterministic Replay Payload

Required.

The replay payload stores math/result/action state as structured JSON or another
structured server-owned payload. It must contain:

- action sequence;
- math profile identity;
- RTP and volatility levels;
- feature/free-spin/bonus-buy state;
- cascade sequence;
- cap state;
- wallet/accounting references;
- replay determinism references;
- round/session completion state.

### 2. Visual VABS HTML / Render Route

Required unless current GS/backoffice evidence proves otherwise.

The visual route uses the deterministic replay payload to render round, session, and
whole-session history. It must support in-game History and CM/backoffice access.

Sanitized legacy route-shape evidence confirms these display/query concepts matter:

- `VIEWSESSID` or game-session equivalent;
- `GAMEID`;
- `LANG`;
- `TIMEZONE`;
- `hideClose`.

### 3. Screenshot Media

Optional.

Screenshots may capture final action/spin states or selected evidence points. They are
useful for quick audit, lower-cost review, and dispute triage, but they are supporting
evidence only.

### 4. Video Media

Optional and high storage cost.

Full video for every spin is not the default. Video is recommended only for selected
feature rounds, bonus-buy rounds, large wins, disputed rounds, sampled QA evidence, or
explicit operator/product requirement.

## Default Decision

Default `historyEvidenceMode`: `deterministic_replay_only`.

This default still requires the visual HTML/render route for release. It means media
capture is off by default; it does not mean visual history is optional.

## Game-Level Settings

Each game must define:

- `historyEvidenceMode`;
- `historyCaptureScope`;
- `historyMediaStoragePolicy`.

If media capture is enabled, retention, max bytes, compression, async capture, storage
provider, checksums, encryption, and PII redaction must be configured before release.

## Release Rule

Release remains blocked until deterministic replay, visual route behavior, evidence
mode, capture policy, and storage/security policy are implemented or explicitly blocked
and accepted with current GS/product evidence.
