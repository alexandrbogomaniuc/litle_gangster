# Max-Win Cap Module

Purpose: enforce the 10000x win cap.

Server-owned behavior:

- Track cumulative pre-cap win.
- Compare against cap after every win event.
- Record cap event if reached.
- Stop further math resolution if cap policy requires immediate termination.
- Emit final capped win.

Required fields:

- cap multiplier.
- pre-cap win.
- capped win.
- cap reached flag.
- cap event step.
- round completion reason.

Certification:

- Simulation must report cap hit frequency and RTP effect.

Client boundary:

- Browser renders max-win cap event only from server result.

