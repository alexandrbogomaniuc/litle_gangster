# 8001 Wallet/Config Registration Dependency

Date: 2026-05-15
Status: audit only, no registration generation

## Findings

- PROVEN_SOURCE: wallet behavior is BankInfo/config driven. Source includes
  `WPM_CLASS`, `CWM_TYPE`, common-wallet request client class, auth URL, balance URL,
  wager URL, refund URL, refund support, balance refresh controls, and pending operation
  handling flags.
- PROVEN_SOURCE: history/VBA settings are BankInfo/config driven. Source includes
  history action URL, history/VAB time offset, history item count, history token TTL,
  in-game history enablement, game history URL, and same-window behavior.
- PROVEN_SOURCE: GS has internal new-games wallet/history endpoints that depend on
  current session/account/bank state and wallet protocol manager configuration.
- BLOCKED: exact 8001 registration field shape for wallet config, history URL,
  VABS/VBA alias URL, and BO/CM route exposure remains unproven.

## GameServerRegistrar Boundary

GameServerRegistrar must not generate registration artifacts until wallet/config
responsibility is resolved:

- prove selected bank/source and current GS lane;
- prove whether 8001 needs BankInfo wallet fields or inherits them from an existing
  bank/template;
- prove VABS/VBA/Lasthands URL/config fields for BO/CM and in-game History;
- prove whether `/vabs/show.jsp`, scoped alias, canonical new-games routes, or a
  configured base URL is required;
- preserve blockers when exact fields are not found.

## Blocked Registration Fields

- wallet manager class/source bank mapping;
- common-wallet request client mapping;
- wallet auth/balance/wager/refund endpoint references;
- refund/rollback behavior support;
- in-game history enablement;
- game history URL or VABS/VBA URL field;
- history action URL and time-zone/offset behavior;
- VABS alias base URL or route policy;
- durable history storage source for 8001.

No registration artifact was generated in this sprint.
