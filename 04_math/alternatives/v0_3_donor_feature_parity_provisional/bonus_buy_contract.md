# Bonus Buy Contract

Generated/updated: 2026-05-11 11:05:00 Europe/London

Status: PROVISIONAL_CONTRACT. This is not donor-true certified math, not runtime code, not registration generation, and not release approval.

## Required Fields

- buy options for `mode_1`, `mode_2`, and `mode_3`;
- selected mode;
- cost multiplier placeholder;
- `betType_or_current_gs_equivalent=UNKNOWN_UNLESS_SOURCE_PROVES`;
- EV/RTP blocker;
- wallet/accounting boundary;
- confirmation UI requirement;
- purchased feature start state.

## Boundary

Bonus-buy accounting is backend/wallet-owned. The browser may request/display a choice but must not settle, generate outcomes, or become source of truth.

## Blockers

- exact buy cost unobserved;
- exact buy EV/RTP unapproved;
- current-GS bonus-buy representation unverified;
- wallet accounting flow not tested.
