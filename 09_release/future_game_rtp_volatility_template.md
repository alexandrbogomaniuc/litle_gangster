# Future Game RTP / Volatility Template

Created: 2026-05-13T08:55:01Z

Every future game must create a 3x3 matrix: three RTP levels and three volatility levels. Use LOW/MEDIUM/HIGH labels, but choose game-specific RTP percentages inside 92.00%-99.00%.

## Required Future Workflow

1. Define LOW/MEDIUM/HIGH RTP levels.
2. Define LOW/MEDIUM/HIGH volatility levels.
3. Create nine `mathProfileId` values.
4. Pretest every profile.
5. Keep registration metadata separate from executable math.
6. Include profile identity in runtime and history/VABS outputs.
7. Block arbitrary operator-entered RTP or volatility values.
8. Keep release blocked until simulation, bonus-buy EV, volatility, and certification pass.
