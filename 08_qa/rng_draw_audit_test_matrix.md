# RNG Draw Audit Test Matrix

Status: test plan only.

| Draw Category | Test | Expected Result |
| --- | --- | --- |
| Base grid | deterministic seed produces stable grid | server-owned stable output |
| Cascade refill | refill draw indexes do not skip or duplicate | stable cascade replay |
| Feature trigger | trigger frequency matches configured model | certification report output |
| Golden-square | state creation references are recorded | replayable state |
| Rainbow | activation references are recorded | replayable event |
| Coin reveal | tier/value distribution audited | reportable distribution |
| Special reveal | candidate reveal audited | blocked until final rules |
| Feature mode | mode decision audited | reportable mode split |
| Bonus buy | purchase path separates accounting and RNG | wallet boundary preserved |
| Jackpot hook | no draw when disabled | disabled by default |
| Max-win cap | cap terminates without extra outcome authority | capped state recorded |

Forbidden:

- raw RNG secrets in payloads.
- browser-generated RNG.

