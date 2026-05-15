# Parallel Math Validation Workflow

ParallelMathValidator exists so large validation can run beside the main
workflow without turning the main thread into an endless simulation loop.

## Standard Flow

1. Validate the request: exactly three RTP labels, exactly three volatility
   labels, ascending RTP values inside 91.00% to 99.70%, and nine profiles
   unless a smaller matrix is explicitly approved.
2. Create a parallel output folder and a safe worker prompt.
3. Run local jobs, external server jobs, subagents, or parallel GPT threads
   only inside the approved scope.
4. Import machine-readable results.
5. Validate train/validation/tail seed separation.
6. Validate profile coverage, round counts, RTP, standard deviation, hit rate,
   cap frequency, max observed win, and optional bonus-buy/FRB evidence.
7. Extract registration math fields or blockers.
8. Create a non-certified evidence package.
9. Handoff to the main workflow with explicit gate states.

## Parallel Rules

- Parallel workers write only to the declared parallel output folder.
- Active configs, active math, backend, client, registration, DB/wallet, donor,
  asset, and release work remain forbidden.
- The main workflow owns all changes outside the parallel output folder.
- Validation seeds are never used for tuning.

## Main Workflow Continuation

The main workflow may continue on unrelated planning, art, protocol, or source
review work while validation runs. It must not proceed to implementation or
release gates that depend on missing math evidence.
