# GameClientBuilder Next Prompt Requirements

Status: planning-only next-step prompt guidance.

## Recommended Next Skill

ProtocolAndSchemaMapper runtime API inspection.

## Exact Scope Needed

The next sprint should prove or block:

- which current GS component owns Little Gangster 8001 result generation.
- whether New Games `/slot/v1` is the selected production lane.
- whether `@gamesv1/core-protocol` is the selected client transport.
- exact request/response contract for bootstrap, opengame, playround, featureaction, resumegame, gethistory, and closegame.
- how v0.3 `result_schema.json` maps into `presentationPayload` or equivalent.
- how wallet/accounting, history/VABS/Lasthands, restore, and closegame boundaries work.
- whether a fixture contract can be approved for client implementation planning.

## Keep Forbidden

Do not generate client code, registration artifacts, runtime implementation, DB changes, wallet calls, donor browsing, donor asset capture, or release approval.
## RuntimeApiInspection Update

The next prompt should not request full client implementation yet. It should first request one of:

1. ProtocolAndSchemaMapper runtime adapter proof/fixture review for Little Gangster v0.3 payload, or
2. backend/runtime adapter planning using `/slot/v1` as candidate only.

Minimum required wording for a future implementation prompt:

- state that runtime owner has been proven by source;
- state the selected runtime API and endpoint contract;
- attach or reference the approved v0.3 payload adapter contract;
- forbid browser-authoritative RNG/outcome generation;
- forbid donor/scaffold asset packaging;
- explicitly approve client code generation.

## FixturePlanning Update

The next recommended technical step remains ProtocolAndSchemaMapper backend/runtime adapter proof unless the user explicitly asks for a static renderer prototype.

If the user asks for a prototype next, the prompt must say:

- consume only `06_resulting_code/planning/fixtures/` static non-production fixtures;
- do not generate production client code;
- do not create runtime implementation;
- do not package donor/scaffold assets;
- keep GameClientBuilder implementation blocked.
