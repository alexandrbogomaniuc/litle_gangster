# VABS Evidence Media Test Matrix

Generated: 2026-05-15

| Test | Purpose | Required Before Release |
| --- | --- | --- |
| deterministic replay payload present | Ensure authoritative evidence exists for every replayable action. | yes |
| visual route uses replay payload | Confirm visual VABS route reconstructs from deterministic replay. | yes |
| sanitized legacy display params | Confirm session/game/language/time-zone/hide-close shape is handled without raw secrets. | yes |
| default mode no media capture | Confirm `deterministic_replay_only` does not capture screenshots/videos. | yes |
| screenshot refs optional | Confirm screenshot refs can be empty when screenshots disabled. | yes |
| video refs optional | Confirm video refs can be empty when video disabled. | yes |
| screenshot mode manifest | Confirm screenshot refs, checksums, retention, and storage provider fields appear when enabled. | when enabled |
| feature video mode manifest | Confirm video refs are scoped to feature/bonus/large-win/dispute policy. | when enabled |
| full video explicit approval | Confirm full-video mode cannot be enabled without explicit release/product setting. | when enabled |
| max bytes per round | Confirm media capture respects round budget. | when enabled |
| max bytes per session | Confirm media capture respects session budget. | when enabled |
| checksum required | Confirm media refs have checksum entries. | when enabled |
| encryption required | Confirm storage policy records encryption requirement. | when enabled |
| PII redaction required | Confirm media policy blocks PII leakage. | when enabled |
| retention expiry | Confirm `retentionExpiresAt` is populated. | when enabled |
| durable storage unavailable | Confirm implementation returns blocked/unavailable instead of inventing media refs. | yes |
| release gate | Release blocked if visual route/evidence mode/media policy gates are unresolved. | yes |
