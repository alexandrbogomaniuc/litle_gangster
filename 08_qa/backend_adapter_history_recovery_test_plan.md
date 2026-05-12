# Backend Adapter History Recovery Test Plan

Status: TEST_PLAN_ONLY.

Future history/recovery tests should verify:

- reconnect returns current grid, pending cascades, golden-square state, feature mode, and cap state;
- unfinished rounds set `restore.hasUnfinishedRound=true`;
- finished rounds set `round.status=FINAL` and no unfinished restore pointer;
- history records can replay cascades, reveals, bonus buy, feature modes, max-win cap, and round completion;
- `gethistory` returns a schema-valid envelope and history records;
- Lasthand/VABS payload storage contains enough state to reconstruct v0.3 render payload;
- browser/client cannot mutate history truth.

