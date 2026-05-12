# GS Config Adjustment Plan

No GS config changes are made in this sprint.

If future tests reveal a Gamesv1/New Games mismatch, GameServerRegistrar must later generate safe config adjustments only:

- add/update 8001 route IDs;
- add/update game-specific client URL;
- verify New Games API/internal base URL references;
- create/update game template metadata;
- create/update bank/currency game assignment;
- create rollback artifacts;
- validate serializer/import path for `scn` and `jcn`;
- keep production apply forbidden until explicit approval.

`scn`/`jcn` serialized config remains blocked until the serializer/admin/cache process is proven.
