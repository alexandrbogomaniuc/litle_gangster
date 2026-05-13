# Registration Metadata Boundary

Generated/updated: 2026-05-11 11:05:00 Europe/London

Status: PROVISIONAL_CONTRACT. This is not donor-true certified math, not runtime code, not registration generation, and not release approval.

## Registration May Need Metadata

Later GameServerRegistrar may need game ID, title, RTP model IDs/display values, min/default/max bet, coin/denomination/base-bet metadata, volatility, max-win/cap metadata, feature flags, bonus-buy support flags, FRB/OCB flags if confirmed,
and client/runtime route references.

## Registration Must Not Contain Executable Math Unless Future Source Proves It

Do not put these into GS registration as executable runtime logic:

- simulator code;
- cluster evaluation logic;
- reel strips or symbol weights as executable math;
- paytables as executable math;
- feature rules as executable math;
- production RNG implementation;
- full result-engine code.

Current evidence status: math import during registration is NOT_FOUND.
