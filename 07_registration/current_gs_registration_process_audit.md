# Current GS Registration Process Audit

## Summary

The current GS registration process is configuration-first. It requires game template records, bank/currency game records, and bank route/config values. It does not currently prove executable math import.

## Evidence

| Area | Status | Evidence | Registrar implication |
|---|---|---|---|
| Game template | PROVEN | `GameTInfoCF` via `CassandraBaseGameInfoTemplatePersister.java:14-52`. | Generate template spec for 8001 only after schema/serializer path is proven. |
| Bank game config | PROVEN | `GameInfoCF` via `CassandraBaseGameInfoPersister.java:39-54`, `173-181`. | Generate bank/currency assignment spec and rollback. |
| Bank route config | PROVEN | `BankInfo.java:852-862`; `BaseStartGameAction.java:878-904`. | Generate bank property patch for route/client/API/internal URLs if selected. |
| Serialized config | PROVEN with blocker | `scn`/`jcn` columns in persisters. | `scn` serializer/admin import is required before apply. |
| Math import | NOT_FOUND | No registration persister consumes paytables/reels/features. | Do not generate math import as registration. |

## Generate-Only Boundary

No registration artifacts were generated in this sprint. Future GameServerRegistrar may generate:

- reviewed JSON specs;
- CQL templates only if the serializer/import method is known;
- rollback specs;
- validation checklist;
- no production apply.
