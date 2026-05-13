# Layout Alignment Report

Status: resolved by switching selected math layout to `6x5_cluster_provisional`.

## Comparison

| Area | Observed/reference layout | Existing v0.1 math | Selected v0.2 math |
|---|---|---|---|
| Grid | 6 columns by 5 rows reported in reference research | 5 reels by 3 rows | 6 reels by 5 rows |
| Pay style | Cluster-style observed/reported | Fixed 20 paylines | Adjacent orthogonal cluster pays |
| Art impact | Large 6x5 board, cluster highlight needs | Smaller classic line-slot board | Matches 6x5 scene mapping expectations |
| Client impact | Needs 6x5 result rendering | Would require redesign away from observed reference | Aligns with expected Little Gangster visual structure |
| Backend/math impact | Cluster result format needed | Payline result format | Cluster result format |

## Risks Of Keeping 5x3

- ArtSceneMapper could map the wrong reel/grid surface.
- ArtDirectionAndReplacementPlanner could brief symbols, board framing, and animations for the wrong layout.
- GameClientBuilder could target payline animations when the desired experience is cluster-based.
- Product expectations would drift from the observed reference game.
- The 5x3 RTP simulator also used payout scaling, which blocks treating that package as true validated math.

## Risks Of Switching To 6x5

- The exact donor rules remain unproven, so v0.2 is not donor-true math.
- Cluster paytable and symbol weights are provisional and need deeper math review.
- Full multi-seed RTP validation is pending.
- Backend/new-games runtime integration remains blocked until source ownership and protocol contracts are proven.

## Recommendation

Switch selected Little Gangster math to `v0.2_6x5_cluster_provisional` before ArtSceneMapper. This keeps the downstream scene, art, client, and result-schema lanes aligned. Keep the old 5x3 v0.1 package preserved as a superseded
alternative, not the selected target.
