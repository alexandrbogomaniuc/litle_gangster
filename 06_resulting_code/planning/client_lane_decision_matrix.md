# Client Lane Decision Matrix

Status: planning-only. No lane is final.

|Candidate lane|Source evidence|Required packages/endpoints|Risks|Status|Recommendation|
|---|---|---|---|---|---|
|New Games / `slot-browser-v1`|Gamesv1 contains `slot-browser-v1`, `@gamesv1/core-protocol`, Vite/Pixi packages, and `/slot/v1` transport contracts. `new-games-server` exposes `/slot/v1/*` endpoints.|`@gamesv1/core-protocol`,
`@gamesv1/pixi-engine`, `@gamesv1/ui-kit`, `/slot/v1/bootstrap`, `/slot/v1/playround`, `/slot/v1/featureaction`, restore/history/close endpoints.|Little Gangster 8001 runtime owner and v0.3 payload adapter are unproven. Existing 7001 shape
is not 6x5 v0.3.|CANDIDATE|PROCEED_TO_PLANNING only.|
|Legacy `template.jsp` / WebSocket|GS server has `template.jsp`, `validator.js`, and `version.json` legacy paths.|Legacy template path and WebSocket/validator flow.|Could conflict with v0.3 backend result payload; not proven for
8001.|CANDIDATE|BLOCKED_PENDING_RUNTIME_OWNER.|
|ExtGame external backend|Core protocol has an `EXTGAME` transport mode and previous advisory checklist mentions external flows.|External backend endpoint, process-equivalent flow, state/history handoff.|Advisory only; not proven selected
for Little Gangster.|UNVERIFIED|DO_NOT_USE unless current GS proves it.|
|Mixed lane|Registration may route to New Games while GS wallet/history bridge handles accounting.|Route config, GS internal bridge, result runtime adapter.|Higher integration risk; exact boundaries
unproven.|CANDIDATE|BLOCKED_PENDING_RUNTIME_OWNER.|
|Unknown/custom lane|No final result owner evidence for 8001.|Unknown.|Cannot implement safely.|BLOCKED|CANDIDATE_ONLY.|

## Current Recommendation

Use New Games / `slot-browser-v1` as the planning candidate because it has the strongest current source evidence. Do not start implementation until current GS proves the Little Gangster runtime owner and result API payload.

