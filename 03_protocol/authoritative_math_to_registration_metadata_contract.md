# Authoritative Math To Registration Metadata Contract

Status: planning contract only.

Evidence labels:

- PROVEN: registration is project-defined as metadata/config/routing only.
- BLOCKED: registration as executable math import.

Registration may include:

- game id.
- game key.
- display metadata.
- RTP variant identifiers.
- enabled feature flags.
- bonus-buy enabled flag.
- jackpot enabled flag.
- max-win metadata.
- launch route.
- runtime route.
- client route.

Registration must not include:

- executable RNG.
- paytable execution code.
- feature outcome logic.
- free-spin resolution logic.
- bonus-buy result generation.
- jackpot award logic.
- browser-authoritative result input.

Future implementation rule:

- Registration may point to approved server math version.
- Registration must not become the math owner.

