# History Button Route Resolution Plan

Generated: 2026-05-15

## Client Strategy

The Little Gangster client should not hardcode a visual history path. The in-game History
button should open the route provided by bootstrap/configuration or by backend-generated
history records.

## Recommended Flow

1. Launch/bootstrap provides `historyPolicy.gameHistoryUrl` or equivalent route metadata.
2. Client requests JSON history through the supported runtime transport when needed.
3. Backend/history response includes a visual replay URL or enough route metadata to open
   round replay, session replay, or whole-session replay.
4. Client opens the visual route in the approved shell/popup/modal behavior.
5. If visual route metadata is missing, client must show a blocked/not-available state
   rather than pretending JSON storage is visual history.

## Route Types To Support

- round replay
- session replay
- whole-session replay
- backoffice-safe visual render
- blocked/not-found response

## Current Blocker

Gamesv1 has JSON history transport evidence, but no proven generic visual VABS renderer
or 8001 visual route resolver. GameClientBuilder remains blocked for release scope until
route implementation and route-resolution evidence are accepted.
