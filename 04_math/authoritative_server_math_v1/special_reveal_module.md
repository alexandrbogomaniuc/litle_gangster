# Special Reveal Module

Purpose: design pot-of-gold and four-leaf-clover special reveal candidates.

Default status: candidate feature, not final math.

Server-owned behavior:

- Determine special reveal eligibility.
- Select reveal type and outcome from approved tables.
- Record reveal source and outcome.
- Apply max-win cap after any win increase.

Special reveal types:

- `pot_of_gold`
- `four_leaf_clover`

Open blockers:

- Exact reward table.
- Exact trigger probability.
- Whether special reveal is active in base, feature, or both.
- Whether reveal can trigger jackpot hook.

Client boundary:

- Browser may display reveal badges and transitions only.

