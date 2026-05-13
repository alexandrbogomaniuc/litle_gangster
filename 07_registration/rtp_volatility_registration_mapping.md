# RTP / Volatility Registration Mapping

Created: 2026-05-13T08:55:01Z

GameServerRegistrar must register possible profile choices as metadata only. It must not import executable math or generate runtime math behavior.

## Required Registration Metadata

- RTP levels: LOW, MEDIUM, HIGH.
- Volatility levels: LOW, MEDIUM, HIGH.
- Approved `mathProfileId` values for the 3x3 matrix.
- `registrationModelCode` for each profile.
- Display RTP percent and status.
- `RTP`, `POSSIBLE_MODELS`, `CURRENT_MODEL`, `VOLATILITY`, `BF_RTP`, and `RTP_WITHOUT_BF` must point to pretested profile metadata.

## Blocker

`gs_profile_matrix_storage_unproven`: current GS storage support for a full 3x3 RTP/volatility profile matrix is not proven. If GS can only store current flat RTP models, GameServerRegistrar must map profile metadata conservatively and
record the unresolved matrix storage gap.
