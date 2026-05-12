# Feature Module Test Matrix

Status: test plan only.

| Module | Unit Tests | Integration Tests | Blockers |
| --- | --- | --- | --- |
| Base cluster/cascade | cluster find, pay, drop, refill | base round completion | paytable/weights |
| Golden-square | create/persist/clear | cascade and feature interaction | exact rules |
| Rainbow | activation eligibility | overlay/reveal event chain | exact rules |
| Coin reveal | tier/value table | golden/rainbow interaction | value tables |
| Special reveal | pot/clover choice | feature and cap interaction | product rules |
| Free spins | spin loop | feature completion | spins/retrigger rules |
| Feature modes | mode setup | mode-specific simulation | mode EV |
| Bonus buy | eligibility/cost | purchase to feature start | cost/EV |
| Jackpot hook | disabled guard | enabled mock integration | product decision |
| Max-win cap | cap math | cap event history | threshold confirmation |

No test may use 7001 math as expected Little Gangster behavior.

