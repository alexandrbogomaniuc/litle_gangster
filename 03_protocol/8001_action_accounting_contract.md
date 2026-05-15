# 8001 Action Accounting Contract

Date: 2026-05-15
Status: planning only

## Principle

Every gameplay action that changes wager, feature state, win, balance, replay state, or round completion must have an action/accounting
  representation. Browser rendering state is never accounting truth.

## Paid Base Spin

Every paid base spin requires:

- action id;
- client operation id;
- idempotency key;
- selected approved `mathProfileId`;
- RTP level and volatility level;
- total bet credits;
- reserve/debit or equivalent accounting reference;
- backend-owned result reference;
- settle/credit or equivalent accounting reference;
- round id;
- round finished status;
- history payload reference.

## Free Spin and Feature Spin

Every free spin or feature spin requires:

- action id;
- parent round id;
- feature mode id;
- feature spin index;
- spins remaining;
- retrigger count;
- cascade/result sequence;
- win credits;
- cap state;
- round completion update.

Free spin and feature spin results must be represented even when they do not create a paid debit.

## Bonus-Buy Purchase

The approved-for-planning 100x bonus-buy purchase requires:

- purchase action id;
- purchase id;
- requested cost multiplier: 100;
- selected `mathProfileId`;
- `baseRtpTarget`;
- `declaredBfRtpTarget`;
- total bet credits;
- purchase cost credits;
- wallet debit/reserve reference;
- accepted/blocked status;
- blocker flags.

125x and 150x must reject or remain unavailable until separately approved.

## Bonus-Buy Feature Result

The purchased feature result requires a separate representation from the purchase:

- result action id;
- purchase id;
- bonus-buy cost multiplier;
- feature win credits;
- declared BF_RTP target;
- observed BF_RTP only when reporting aggregate/planning evidence;
- cascade sequence;
- feature state;
- cap state;
- round completion;
- wallet credit/settle reference;
- history/VABS payload reference.

## Balance Rule

Balance must come from the settle/process response or approved accounting result. Repeated `getBalance` must not be used as a substitute for correct
  settlement state.

## Idempotency

The wrapper must treat action id, client operation id, idempotency key, round id, and purchase id as replay/retry controls. Duplicate requests must
  not double debit, double credit, or advance feature state twice.

## Pending and Stuck Recovery

Pending or stuck actions must preserve:

- last accepted action;
- last accounting reference;
- current wrapper state;
- recoverable payload;
- history/lasthand snapshot;
- retry/rollback status.

Any unresolved accounting state must route to `stuck_transaction_review`.

## Sprint Boundary

No wallet endpoint calls occurred in this sprint. This document is a planning contract only.
