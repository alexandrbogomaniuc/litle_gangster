# VabsVisualHistorySourcePlanning Validation Checklist

Created: 2026-05-15

1. `project_manifest.json` parses: pass.
2. VabsVisualHistorySourcePlanning handoff parses: pass.
3. source target map JSON parses: pass.
4. response schema JSON parses: pass.
5. all required docs exist and are non-empty: pass.
6. route contract includes round replay: pass.
7. route contract includes whole-session replay: pass.
8. route contract includes session replay: pass.
9. route contract includes visual/render response: pass.
10. route contract includes in-game History button: pass.
11. route contract includes Casino Manager/backoffice access: pass.
12. storage contract includes lifecycle state persistence source: pass.
13. storage contract includes wallet/accounting references: pass.
14. response schema includes `mathProfileId`: pass.
15. response schema includes `bonusBuyCostMultiplier`: pass.
16. response schema includes `declaredBfRtpTarget`: pass.
17. response schema includes `actionSequence`: pass.
18. response schema includes visualReplay payload or URL: pass.
19. security doc bans raw tokens/signatures/private URLs: pass.
20. test plan includes round/session/whole-session/backoffice/history button tests: pass.
21. future workflow doc states visual history route is required for future games unless explicitly blocked: pass.
22. no Staging source was modified: pass.
23. no VABS route code was created: pass.
24. no client code was generated: pass.
25. no registration artifact was generated: pass.
26. no DB/Cassandra action occurred: pass.
27. no wallet/API call occurred: pass.
28. no donor browsing occurred: pass.
29. no asset capture occurred: pass.
30. no release approval occurred: pass.
