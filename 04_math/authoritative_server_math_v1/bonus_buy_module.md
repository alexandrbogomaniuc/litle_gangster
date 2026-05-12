# Bonus Buy Module

Purpose: define purchase and feature-start boundary for bonus buy.

Status: designed with blocker `bonus_buy_cost_ev_pending`.

Server-owned behavior:

- Validate product availability.
- Validate bet, currency, jurisdiction, and responsible gaming restrictions.
- Calculate approved purchase cost from product configuration.
- Request wallet/accounting outside game payload.
- Start purchased feature only after accounting succeeds.
- Generate feature state server-side.

Unknowns:

- Final cost multiplier.
- Bonus-buy RTP and EV.
- Whether player chooses mode or server randomizes mode.
- Eligibility by jurisdiction or configuration.

History:

- Purchase request.
- Approved cost.
- Selected mode or random mode decision.
- Feature start state.
- Wallet transaction reference outside game payload.

Client boundary:

- Browser may request a purchase and render confirmation.
- Browser must not generate purchased feature outcomes.

