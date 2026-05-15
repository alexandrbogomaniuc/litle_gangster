# 8001 Next Implementation Sequence

Date: 2026-05-15

## Recommended Sequence

1. Lifecycle wrapper implementation apply or source planning.
   - Requires explicit approval before any Staging source modification.
   - Must wrap launch/session, open/resume/close, base actions, feature actions, bonus-buy action, cap state, wallet/accounting references, reconnect,
     restart/FRB, and blocker propagation.

2. VABS visual history route implementation planning.
   - Define route/API owner, round/session/whole-session replay paths, Lasthands storage, and backoffice access before implementation.

3. Wallet/history runtime tests.
   - Run WalletAndLaunchTester only after wrapper and route implementation are approved and present.
   - Include pending/stuck transaction and last hand tests.

4. GameClientBuilder.
   - Run only after wrapper/payload contract is accepted and history route expectations are stable.

5. GameServerRegistrar generate-only.
   - Run only after settings dependencies are resolved for models, RTP/BF_RTP, SD/KPI, cap/max-win, GL bets, FRB/language/history fields.

6. Release audit.
   - Run only after math, wrapper, client, registration, wallet/history, art, LQA/licensee, and certification gates pass.

## Current Recommendation

Next prompt should ask for ProtocolAndSchemaMapper lifecycle wrapper source planning or explicitly approved lifecycle wrapper implementation apply.
  Keep VABS implementation, GameClientBuilder, GameServerRegistrar, wallet endpoints, DB/Cassandra, and release blocked unless explicitly opened by
  the user.
