# gamePayload Schema Contract For Future Client

Status: FUTURE_CLIENT_CONTRACT_PLANNING_ONLY

## Contract

Future client code should read Little Gangster v0.3 renderer state from:

```text
runtimeEnvelope.presentationPayload.gamePayload.payload
```

Required wrapper fields:

| Field | Required | Meaning |
|---|---:|---|
| `gameKey` | yes | Must be `little-gangster` for Little Gangster. |
| `schemaVersion` | yes | Must be `v0.3` for the current renderer payload. |
| `payload` | yes | Object containing v0.3 render state. |

## Client Boundary

The future client may render `payload` but must not generate production RNG, authoritative outcomes, payout results, wallet/accounting fields, or persisted history truth.

## Fallback

`presentationPayload.littleGangsterV03` remains a documented fallback only. It is not recommended unless the platform rejects generic `gamePayload`.

## GameClientBuilder Impact

This contract helps future client implementation, but it does not unlock full GameClientBuilder. Runtime owner, schema patch, backend adapter, final asset strategy, and explicit build approval remain required.
