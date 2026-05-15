# FRB And Promo Validation Policy

FRB/free-round campaigns are not automatically base game RTP.
FRB/free-round campaign separate from base RTP is the default policy.

## Separate Evidence Required

- Promo/free-round expected value and promo liability.
- Campaign liability.
- Free-round state and lifecycle behavior.
- Settlement/accounting behavior.
- Replay/VABS/history behavior.
- Cap behavior.
- End/restart statuses such as FRB finished, canceled, expired, or max-win
  reached when the platform has those concepts.

## Do Not Mix By Default

Do not silently mix FRB EV into base RTP or bonus-buy RTP. Only combine them
when product and GS registration/runtime rules explicitly require it.

## Registration And Release

If FRB affects registration fields, possible models, SD keys, cap behavior, or
liability, require explicit extraction and blockers before GameServerRegistrar
or RTPAndReleaseAuditor can pass.
