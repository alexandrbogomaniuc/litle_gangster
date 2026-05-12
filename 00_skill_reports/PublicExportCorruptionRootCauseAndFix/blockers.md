# PublicExportCorruptionRootCauseAndFix Blockers

No active blocker remains after replacement commit `25cbf1c3f8ce1d6f89871f11a43f40478a8e2e6c` passed project-local GitHub raw validation.

Residual note: exact newline-collapse root cause remains not proven from current local files. The durable fix is the new validation trust boundary: public export success is only valid after project-local raw validation of the pushed commit.
