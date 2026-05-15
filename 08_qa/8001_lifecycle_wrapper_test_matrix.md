# 8001 Lifecycle Wrapper Test Matrix

Date: 2026-05-15
Status: checklist only, no test execution

| Area | Test | Expected result | Status |
| --- | --- | --- | --- |
| Launch | open game | Valid 8001 session opens through wrapper with profile identity. | blocked |
| Launch | resume game | Persisted state restores correct wrapper state. | blocked |
| Launch | close game | Close preserves unfinished state or finalizes clean state correctly. | blocked |
| Base | base spin | Paid action and accounting references recorded. | blocked |
| Base | cascades | Cascade sequence completes server-side and is replayable. | blocked |
| Feature | free spins | Feature spin actions resolve without incorrect paid debit. | blocked |
| Bonus buy | bonus-buy purchase | 100x purchase debit/action recorded; 125x/150x blocked. | blocked |
| Bonus buy | bonus-buy feature result | Purchased feature result, BF_RTP target, cap state, and settlement refs recorded. | blocked |
| Cap | cap enforcement | Pre-cap/capped win and capHit state persisted. | blocked |
| Wallet | reserve/settle/rollback or equivalent | Wallet/accounting references and balance source verified. | blocked |
| Wallet | pending/stuck transaction | Pending/stuck state routes to review/retry/rollback path. | blocked |
| Restart | restart flow | restart advisory routes to `restart_required` and restores context. | blocked |
| FRB | FRB transition | FRB finished/canceled/expired/max-win states handled or blocked. | blocked |
| History | VABS round replay | Single round replay renders deterministically. | blocked |
| History | whole-session replay | Whole session renders ordered replay. | blocked |
| History | session replay | Session list/replay route works. | blocked |
| History | last hand | Last hand/unfinished state available and correct. | blocked |
| Settings | SD_KEYS | SD/KPI mapping proven or blocked with reason. | blocked |
| Settings | FeatureKPI | Feature KPI categories verified. | blocked |
| Errors | error logging | Launch/runtime/wallet/history errors translated and logged. | blocked |
| Release | LQA/licensee acceptance | Licensee/LQA acceptance passes. | blocked |

## Execution Boundary

WalletAndLaunchTester did not run in this sprint. No wallet endpoints, DB/Cassandra actions, registration generation, client code, or release action
  occurred.
