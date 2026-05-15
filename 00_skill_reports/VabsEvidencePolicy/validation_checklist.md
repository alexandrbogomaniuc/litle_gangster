# VabsEvidencePolicy Validation Checklist

Generated: 2026-05-15

1. project_manifest.json parses: yes.
2. VabsEvidencePolicy handoff parses: yes.
3. vabs_media_manifest_schema.json parses: yes.
4. 8001_vabs_visual_history_response_schema.json parses after patch: yes.
5. all required docs exist and are non-empty: yes.
6. docs state deterministic replay is required: yes.
7. docs state visual VABS route is required: yes.
8. docs define screenshot mode: yes.
9. docs define video mode: yes.
10. docs state video is optional/high-storage, not default for all spins: yes.
11. docs define game-level historyEvidenceMode: yes.
12. docs define historyCaptureScope: yes.
13. docs define storage/retention/security policy: yes.
14. media manifest schema includes screenshotRefs: yes.
15. media manifest schema includes videoRefs: yes.
16. media manifest schema includes checksums: yes.
17. media manifest schema includes retentionExpiresAt: yes.
18. registration/settings doc states where evidence settings live or blocker: yes.
19. future workflow doc states every future game must choose evidence mode before release: yes.
20. reusable skill docs patched or blocker recorded: yes.
21. no Staging source was modified: yes.
22. no VABS route implementation was created: yes.
23. no screenshot/video capture was implemented: yes.
24. no durable storage was implemented: yes.
25. no client code was generated: yes.
26. no registration artifact was generated: yes.
27. no DB/Cassandra action occurred: yes.
28. no wallet/API call occurred: yes.
29. no donor browsing occurred: yes.
30. no asset capture occurred: yes.
31. no release approval occurred: yes.
