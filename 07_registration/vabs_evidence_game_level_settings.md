# VABS Evidence Game-Level Settings

Generated: 2026-05-15

## Settings Required Before Release

Every future game must choose:

- `historyEvidenceMode`;
- `historyCaptureScope`;
- `historyMediaStoragePolicy`.

## Proposed Setting Ownership

| Setting | Recommended Home | Notes |
| --- | --- | --- |
| `historyEvidenceMode` | product/release config and runtime config | Product-facing decision; runtime must enforce it. |
| `historyCaptureScope` | product/release config and runtime config | May be operator-specific if approved. |
| `historyMediaStoragePolicy.enabled` | server environment config plus product/release config | Must not enable storage accidentally. |
| `historyMediaStoragePolicy.mediaType` | runtime config | Screenshots and videos require different storage controls. |
| `retentionDays` | operator override or product/release config | Must meet compliance and storage constraints. |
| `maxBytesPerRound` | server environment config | Protects runtime/storage budgets. |
| `maxBytesPerSession` | server environment config | Protects session-level storage budget. |
| `compressionProfile` | server environment config | Depends on media implementation. |
| `asyncCapture` | runtime config | Should default true when media capture exists. |
| `storageProvider` | server environment config | Durable provider not implemented. |
| `checksumRequired` | product/release config | Must be true for media evidence. |
| `encryptionRequired` | product/release config | Must be true outside local non-production fixtures. |
| `piiRedactionRequired` | product/release config | Must be true. |

## Registration Impact

Do not generate registration artifacts yet.

The visual route URL/config path remains blocked because exact field shape is unproven.
Evidence settings may belong partly in registration metadata, but storage provider,
retention, and capture budgets likely belong in runtime/server environment and
product/release config.

## Current Little Gangster Plan

- default `historyEvidenceMode`: `deterministic_replay_only`;
- `historyCaptureScope`: blocked until product/operator chooses media mode;
- `historyMediaStoragePolicy.enabled`: false by default;
- visual VABS route: required and still pending implementation;
- screenshot/video capture: policy-supported but not implemented;
- durable media storage: not implemented.
