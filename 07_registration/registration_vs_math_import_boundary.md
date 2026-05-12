# Registration vs Math Import Boundary

## Direct Answer

Registration is not proven to import executable math into GS.

## Registration Metadata

Future registration may include:

- game ID and title;
- bank/sub-casino assignment;
- route/client/API/internal URL values;
- RTP display/config values;
- volatility label;
- max win/cap metadata;
- bet range and coin/denomination metadata;
- feature flags;
- template round-finish helper fields if selected lane requires them.

## Executable Math

Executable math should live in the proven runtime owner:

- New Games backend if selected and implemented;
- game-specific backend package if selected;
- classic GS processor only if source/config proves it;
- never browser-side for production outcomes.

## GameServerRegistrar Boundary

GameServerRegistrar must not:

- place `math_package.json` into CQL as executable code;
- put reel strips, cluster paytables, or feature-rule execution into registration unless current GS schema explicitly requires it;
- mark math as imported by registration without source proof;
- execute DB changes in generation sprint.
