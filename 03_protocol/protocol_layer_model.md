# Protocol Layer Model

Status: completed with partial runtime/config blockers

## Layer Separation

| Layer | Role | Evidence | Status |
|---|---|---|---|
| Launch/template layer | Accepts casino launch routes, authenticates through Common Wallet, creates/locates a session, then redirects to either legacy JSP shell or new-games client. | BSG CW summary; `CWStartGameAction.java:55-108`;
`BaseStartGameAction.java:878-904`; `template.jsp:52-114` | mapped |
| Browser/client runtime layer | Browser client reads launch params, opens a GS HTTP runtime session, and sends slot contract operations such as bootstrap/open/play/feature/history/close. | `GsRuntimeClient.ts:96-120`, `158-236`, `265-392`;
`GS_7001_NEWGAMES_RUNBOOK.md:59-66` | partial |
| Game Server runtime layer | GS start action authenticates, resolves route bridges, shadows session/gameplay/protocol decisions, and passes launch params to new-games or legacy shell. | `CWStartGameAction.java:313-423`;
`BaseStartGameAction.java:878-904`, `1023-1031` | partial |
| BSG Common Wallet layer | Wallet/casino protocol for Authenticate, Bet/Result, Refund Bet, MD5 hash, XML/EXTSYSTEM/BSGSYSTEM responses, balance/accounting. | `BSG_COMMON_WALLET_SUMMARY.md`; `VERIFIED_FACTS.md`; `CCommonWallet.java:3-75` |
mapped from docs plus constants |
| Cassandra/config registration layer | Bank/game/template config evidence, including `RCasinoSCKS` registration, bank config, new-games route properties, and rollback requirement. | `CASSANDRA_REGISTRATION_SUMMARY.md`;
`BankInfoCache.xml:786-925`; `docker-compose.yml:59-62`; `GS_7001_NEWGAMES_RUNBOOK.md:43-51` | partial |
| Math/result-generation layer | Produces authoritative or provisional slot outcomes consumed by runtime responses; final Little Gangster math not designed in this sprint. | `GsRuntimeClient.ts:265-392`; `ConfigManager.ts:runtime policies`
targeted evidence; user requirements | known boundary only |
| Wallet/External Casino layer | External wallet/auth/wager/refund side called by Common Wallet client. | BSG CW docs; `CWStartGameAction.java:106-108`; BankInfo Common Wallet URL properties | partial, no endpoint calls |

## Critical Rules

- BSG Common Wallet is a wallet/casino protocol. It is not the full browser runtime protocol.
- Browser runtime protocol must come from live client/GS source and the new-games slot contract, not from BSG CW alone.
- Launch/template routing is separate from browser runtime; `cwstartgamev2.do` is launch/GS routing, not generic Pixi bootloader logic.
- Cassandra/config registration is separate from wallet calls. Registration remains generate-only until explicitly approved later.
- Donor asset inventory is separate from protocol mapping. Captured scaffold assets remain blocked from release.
- Unknowns are recorded in `protocol_blockers.md`; no protocol fields, DB columns, or hash orders were invented.

## Stage 4 Conclusion

The protocol model is sufficient to hand MathModelDesigner the project constraints and runtime boundaries, but it is not a release-ready implementation contract. Later skills must still validate the `@gamesv1/core-protocol` transport
package, Game Server slot endpoints, registration serialization, and wallet tests against fixtures/local ignored secret references.
