# Question — v1

The decision this work serves, and exactly what is being predicted, described, or found. The data
equivalent of requirements: changes only with the client, and a change is a new version
(`QUESTION_v2.md`), never an edit to this one. See
[DM1/R1–R10](https://github.com/wmacevoy/data-mining/blob/main/guide/04-requirements.md).

Client (the one voice who can decide): _name_ · Date sent: _yyyy-mm-dd_ · *Tell us what is wrong
with it.*

## The decision

Who decides what, when, with what in front of them today — and what it costs when they get it wrong
([DM1/R1](https://github.com/wmacevoy/data-mining/blob/main/guide/04-requirements.md#r1)).

- **Decision:** _…_
- **What we would do if the answer came out the other way:** _…_ (If "nothing," stop here.)

## People in the data

Whose rows these are, what they were collected for, and whether this use is that
([DM1/P3](https://github.com/wmacevoy/data-mining/blob/main/guide/01-purpose.md#p3),
[DM1/R9](https://github.com/wmacevoy/data-mining/blob/main/guide/04-requirements.md#r9)).

## Bias

A requirement like any other, decided with the client
([DM1/R10](https://github.com/wmacevoy/data-mining/blob/main/guide/04-requirements.md#r10)).

- **Who asks about one case, and which reference class will the answer describe:** _…_
  ([DM1/U8](https://github.com/wmacevoy/data-mining/blob/main/guide/02-unknowing.md#u8))
- **Groups that matter:** _…_ — _who said so_
- **BIAS-1** *(since v1)* The measure (error rate, calibration, or selection rate, per group), the
  largest acceptable gap, and who chose that measure over the others: _…_

| Source | Present here? How we will check |
| ------ | ------------------------------- |
| Historical | |
| Selection, representation | |
| Measurement | |
| Aggregation | |
| Evaluation | |
| Deployment | |

## Definitions

One-way doors: each costs a re-analysis to change
([DM1/R2](https://github.com/wmacevoy/data-mining/blob/main/guide/04-requirements.md#r2)). Prefix
by area (`OUT-1`, `UNIT-1`, …), mark each with the version that last changed it, and cite them as
`Q1/OUT-1`.

- **UNIT-1** *(since v1)* One row is: _…_
- **OUT-1** *(since v1)* The outcome, written so it could be a query: _…_
- **PRED-1** *(since v1)* The prediction point — when the prediction is made, and so what may be
  known: _…_

## The bar

Specific enough to be rejected, written before results are seen
([DM1/R3](https://github.com/wmacevoy/data-mining/blob/main/guide/04-requirements.md#r3)). Mark
guesses *(invented)*.

- **BAR-1** *(since v1)* Metric _…_, on _which split / period_, at least _…_, against the baseline
  _…_ which scores _…_, with the interval reported.

## The price of each error

([DM1/R4](https://github.com/wmacevoy/data-mining/blob/main/guide/04-requirements.md#r4))

| Error | What it looks like here | Who pays | Relative cost |
| ----- | ----------------------- | -------- | ------------- |
| False positive | | | |
| False negative | | | |

## Envelope

([DM1/R8](https://github.com/wmacevoy/data-mining/blob/main/guide/04-requirements.md#r8))

- **Data:** _rows, periods, and — the binding number — events_
- **Labels:** _how many, at what cost, by when; agreement rate if known_
- **Compute:** _per run, and runs budgeted_
- **Expert time:** _whose, how many hours_
- **Inference:** _latency and cost per prediction_
- **Freshness:** _how stale the model may get, and who decides to retrain_

## Assumptions (K4s), read back to the client

In their words, not ours ([DM1/H2](https://github.com/wmacevoy/data-mining/blob/main/guide/09-people.md#h2)).

- "We're assuming _…_. True?" — _answer, date_

## Not for

Populations, conditions, and uses this work will still produce an answer for, and that we will not
stand behind ([DM1/R11](https://github.com/wmacevoy/data-mining/blob/main/guide/04-requirements.md#r11)).

- _…_ — _reason_

## Not yet answered

- _Question_ — _who can answer, by when_
