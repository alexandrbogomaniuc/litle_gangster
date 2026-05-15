# 8001 VABS Route Implementation Update After Media Policy

Generated: 2026-05-15

## Updated Future Implementation Requirement

The future 8001 VABS route foundation should support:

- deterministic replay payload;
- visual HTML/render response;
- media manifest reference;
- optional screenshot references;
- optional video references;
- checksum map;
- storage provider field;
- retention expiry field;
- clear blocked response when durable media storage is unavailable.

## Not Implemented In This Sprint

- VABS route code;
- screenshot capture;
- video capture;
- durable DB/object storage;
- lifecycle wrapper changes;
- backend adapter changes;
- client code;
- registration artifacts.

## Route Shape Reminder

Sanitized legacy route-shape evidence uses session id equivalent, game id, language,
time zone, and hide-close display behavior. Do not persist raw URLs or raw IDs.

## Default Little Gangster Media Policy

- `historyEvidenceMode`: `deterministic_replay_only`;
- `historyMediaStoragePolicy.enabled`: false;
- screenshots: policy-supported, not implemented;
- video: policy-supported, not implemented;
- visual VABS route: required, implementation pending.
