# Coin Reveal Module

Purpose: reveal bronze, silver, and gold coin outcomes from server state.

Server-owned behavior:

- Determine reveal eligibility.
- Select coin tier and value from approved distribution.
- Record value, tier, triggering state, and display metadata.

Output fields:

- reveal id.
- cell.
- tier: bronze, silver, or gold.
- credit value or multiplier value.
- associated feature or cascade step.

Open blockers:

- Coin value tables.
- Reveal frequency.
- Interaction with special reveal candidates.

History requirement:

- Coin reveals must be present in Lasthands/VABS replay and certification logs.

