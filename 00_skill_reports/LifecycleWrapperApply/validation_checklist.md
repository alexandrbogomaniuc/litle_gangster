# LifecycleWrapperApply Validation Checklist

Created: 2026-05-15

1. `project_manifest.json` parses: pass.
2. LifecycleWrapperApply handoff parses: pass.
3. lifecycle apply source changes JSON parses: pass.
4. only allowed Staging files were created/modified: pass.
5. `lifecycleTypes.ts` exists: pass.
6. `lifecycleStateMachine.ts` exists: pass.
7. `actionAccounting.ts` exists: pass.
8. `roundCompletion.ts` exists: pass.
9. `statePersistence.ts` exists: pass.
10. `reconnectRecovery.ts` exists: pass.
11. `blockerPropagation.ts` exists: pass.
12. `lifecycleWrapper.ts` exists: pass.
13. lifecycle wrapper preserves `presentationPayload.gamePayload`: pass.
14. lifecycle wrapper includes `mathProfileId`: pass.
15. lifecycle wrapper includes RTP/volatility: pass.
16. lifecycle wrapper includes 100x bonus-buy fields: pass.
17. lifecycle wrapper includes action accounting representation: pass.
18. lifecycle wrapper includes round completion representation: pass.
19. lifecycle wrapper includes reconnect/persistence representation: pass.
20. lifecycle wrapper includes blocker flags: pass.
21. VABS visual route implementation remains false: pass.
22. release/certification flags remain false: pass.
23. targeted tests run or blocker recorded: pass.
24. rollback plan exists: pass.
25. no GameClientBuilder implementation was created: pass.
26. no Gamesv1/games/8001 was created: pass.
27. no registration artifact was generated: pass.
28. no DB/Cassandra action occurred: pass.
29. no wallet/API call occurred: pass.
30. no donor browsing occurred: pass.
31. no asset capture occurred: pass.
32. no release approval occurred: pass.
