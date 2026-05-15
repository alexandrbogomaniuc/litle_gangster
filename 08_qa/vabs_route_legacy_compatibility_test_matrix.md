# VABS Route Legacy Compatibility Test Matrix

Generated: 2026-05-15

| Test | Purpose | Expected Status Before Release |
| --- | --- | --- |
| Legacy session visual URL | Open visual history using `VIEWSESSID` and `GAMEID`. | Required |
| Legacy round visual URL | Open visual history using `ROUNDID`, `VIEWSESSID`, and `GAMEID`. | Required |
| Whole-session visual URL | Open session visual history with whole-session flag/route. | Required |
| Token-to-round redirect | Resolve token history to visual round route if supported. | Required or explicitly blocked |
| `/slot/v1/gethistory` JSON | Confirm JSON history records remain read-only and deterministic. | Required |
| Modern 8001 round route | Return JSON replay and visual/render response for a round. | Required |
| Modern 8001 session route | Return JSON replay and visual/render response for a session. | Required |
| In-game History button | Opens configured/backend-generated route, not hardcoded path. | Required |
| Casino Manager/backoffice | Opens visual URL or receives safe not-found/blocked response. | Required |
| Language | `LANG`/language parameter is preserved or safely defaulted. | Required |
| Time zone | time-zone parameter is honored or safely defaulted. | Required |
| Online session params | `SESSION`/online behavior is accepted or safely rejected. | Required |
| Missing history | Missing round/session returns not-found without leaking internals. | Required |
| Security scan | No raw tokens, signatures, private hosts, or secrets in stored URLs. | Required |
| Wallet/accounting refs | Visual payload references settlement/accounting ids only as safe placeholders or approved ids. | Required |
| Bonus-buy replay | 100x bonus-buy purchase/result replay includes planning-only release blockers. | Required |
| Lasthands | Lasthands route or accepted blocker is recorded. | Required |
| Release gate | Release remains blocked until visual route tests pass or product/GS explicitly accepts blocker. | Required |
