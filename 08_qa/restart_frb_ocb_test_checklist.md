# Restart / FRB / OCB Test Checklist

Status: QA gate only; no tests executed.

## Required Tests If In Scope

- `/slot/v1/resumegame` restores pending round/feature state.
- Restart after FRB terminal states if FRB is enabled.
- Restart after bonus expired/canceled/capped states if applicable.
- OCB/cash bonus behavior if product/current GS scope requires it.
- Bonus buy state and purchased feature restore.
- `closegame` / closeSession equivalent on player exit.
- No duplicate settlement on restart or resume.

## Product Decisions

- FRB support for Little Gangster: pending.
- OCB/cash bonus support for Little Gangster: pending.
- Tournament/TTP support: not assumed.

