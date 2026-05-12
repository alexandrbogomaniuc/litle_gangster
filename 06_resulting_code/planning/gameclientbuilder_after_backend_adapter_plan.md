# GameClientBuilder After Backend Adapter Plan

Status: FULL_IMPLEMENTATION_BLOCKED.

The backend adapter implementation plan does not unlock GameClientBuilder implementation.

Before full GameClientBuilder implementation can start:

1. Backend adapter must be implemented after explicit approval.
2. 8001 runtime owner must be selected or created.
3. Server-emitted `/slot/v1` responses must validate against patched schemas.
4. Server-emitted `presentationPayload.gamePayload.payload` must validate against v0.3 result schema.
5. History/reconnect behavior must be tested.
6. Approved production-safe assets must exist.
7. User must explicitly approve GameClientBuilder implementation.

The existing static renderer remains non-production only.

