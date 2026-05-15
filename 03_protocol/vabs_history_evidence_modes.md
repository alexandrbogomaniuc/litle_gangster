# VABS History Evidence Modes

Generated: 2026-05-15

## historyEvidenceMode

Allowed values:

- `deterministic_replay_only`
- `replay_plus_screenshots`
- `replay_plus_feature_video`
- `replay_plus_full_video`

## Mode Definitions

### deterministic_replay_only

Default mode. Deterministic replay payload is required. Visual HTML/render route remains
required. Screenshot/video media capture is disabled unless another policy overrides it.

### replay_plus_screenshots

Deterministic replay and visual route are required. Screenshot references are captured
according to `historyCaptureScope`. This is suitable for quick audit and moderate
storage impact.

### replay_plus_feature_video

Deterministic replay and visual route are required. Video evidence is limited to feature
rounds, bonus-buy rounds, large wins, disputes, samples, or other scoped capture rules.

### replay_plus_full_video

Deterministic replay and visual route are required. Video may be captured for every
covered action. This mode is high storage/performance risk and must require explicit
product/operator/release approval. It is not the default.

## historyCaptureScope

Allowed values:

- `all_actions`
- `paid_spins_only`
- `feature_rounds_only`
- `bonus_buy_only`
- `wins_above_threshold`
- `sampled`
- `disputed_rounds_only`

## historyMediaStoragePolicy

Required fields:

- `enabled`
- `mediaType`
- `captureScope`
- `retentionDays`
- `maxBytesPerRound`
- `maxBytesPerSession`
- `compressionProfile`
- `asyncCapture`
- `storageProvider`
- `checksumRequired`
- `encryptionRequired`
- `piiRedactionRequired`

## Policy Notes

- Deterministic replay is required in every mode.
- Visual VABS route is required in every mode unless explicitly blocked by current GS
  evidence.
- Media mode can support screenshots and videos, but media is never authoritative.
- Full video for every spin is not default because storage and runtime costs are high.
