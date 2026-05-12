# Remaining Detail Gap Register

Status: consolidation gate register.

| Group | Gap | Owner skill | Severity | Blocks implementation | Next action |
| --- | --- | --- | --- | --- | --- |
| Math | exact symbol weights | MathModelDesigner | high | yes | authoritative simulation/config refinement |
| Math | exact cluster paytable | MathModelDesigner | high | yes | define and validate paytable |
| Math | golden-square probabilities | MathModelDesigner | high | yes | define probability/state rules |
| Math | rainbow activation rules | MathModelDesigner | high | yes | define trigger/effect table |
| Math | coin value tables | MathModelDesigner | high | yes | define bronze/silver/gold distributions |
| Math | special reveal rules | MathModelDesigner | high | yes | define pot/clover behavior or disable |
| GL/game settings | cluster-equivalent bet metadata | MathModelDesigner + GameServerRegistrar | high | yes | map min/default/max/coin to cluster model |
| GL/game settings | fixed-line legacy field handling | GameServerRegistrar | medium | yes for registration | define safe legacy placeholders if required |
| RTP models | model id mapping for 96/94/92 | MathModelDesigner | high | yes | define model ids and config format |
| RTP models | model-specific volatility and contribution | MathModelDesigner | high | yes | simulation report design/refinement |
| RTP models | RTP with and without bonus buy | MathModelDesigner | high | yes | bonus-buy EV simulation |
| Bonus buy | cost multiplier | MathModelDesigner | high | yes | product/math decision |
| Bonus buy | EV per RTP model | MathModelDesigner | high | yes | simulation and approval |
| Free spins | exact trigger and spin loop | MathModelDesigner | high | yes | define trigger, spins, retrigger |
| Free spins | feature mode differences | MathModelDesigner | high | yes | define mode-specific rules |
| Jackpots | product decision | MathModelDesigner + GameServerRegistrar | medium | no if disabled | keep disabled until approval |
| Jackpots | contribution/accounting fields | ProtocolAndSchemaMapper | high if enabled | yes if enabled | define only after product approval |
| VABS/history | exact 8001 storage target | ProtocolAndSchemaMapper | high | yes | strict history design/source review |
| VABS/history | Lasthand serialization | ProtocolAndSchemaMapper | high | yes | verify current GS lane |
| VABS/history | screenshot/thumbnail requirement | ProtocolAndSchemaMapper | medium | maybe | verify; default deterministic replay |
| Backend adapter | source modification approval | ProtocolAndSchemaMapper | high | yes | user approval before apply |
| Backend adapter | runtime owner | ProtocolAndSchemaMapper | high | yes | prove/approve owner |
| Runtime owner | 8001 package or server module | ProtocolAndSchemaMapper | high | yes | select target |
| Registration | game 8001 missing | GameServerRegistrar | high | yes | generate-only sprint after gates |
| Registration | scn/jcn serializer/import path | GameServerRegistrar | high | yes | prove serializer/workaround |
| Registration | lane finality | GameServerRegistrar | high | yes | prove new-games/legacy/ExtGame/mixed lane |
| Client | production client implementation | GameClientBuilder | high | yes | blocked until runtime/result/assets |
| Client | final approved assets | ArtDirectionAndReplacementPlanner | high | yes | replace/approve release assets |
| Assets | scaffold assets blocked | ArtDirectionAndReplacementPlanner | high | yes for release | original asset replacement |
| Wallet/launch testing | safe environment and secret refs | WalletAndLaunchTester | high | yes | later test sprint only |
| Certification/release | multi-seed simulation | MathModelDesigner | high | yes | simulation refinement |
| Certification/release | release audit | RTPAndReleaseAuditor | high | yes | only after prior gates |

Next action recommendation:

- Run MathModelDesigner authoritative simulation/config refinement first.
- Run checkpoint review/push soon if the user wants external review of accumulated local artifacts.
- Do not run backend adapter apply until math/config/history gaps are closed or explicitly accepted as implementation blockers.

