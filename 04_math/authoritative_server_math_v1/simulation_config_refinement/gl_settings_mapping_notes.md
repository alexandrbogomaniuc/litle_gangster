# GL Settings Mapping Notes

The game settings profiles include every GL/template field requested for this sprint, but values remain provisional.

Cluster games should not be forced into fixed-line math. The compatibility fields `POSSIBLE_LINES`, `LINES_COUNT`, `DEFAULTNUMLINES`, `POSSIBLE_BETPERLINES`, and `DEFAULTBETPERLINE` are included only to satisfy possible current GS
registration shape expectations. The authoritative math should use cluster-equivalent bet fields: `clusterBaseBetCredits`, `clusterBetMultiplier`, `minTotalBet`, `defaultTotalBet`, and `maxTotalBet`.

Registration remains metadata/config/routing only. It must not import executable math or create authoritative outcomes.
