# Analysis plan — v1

What we will do, and how we will judge it, written **before the outcome is examined**. Not because
it will be right, but as a dated record of how many choices were open
([DM1/F6](https://github.com/wmacevoy/data-mining/blob/main/guide/03-feedback.md#f6)). Departing from
it is normal; departing silently is the problem — add a dated line under *Departures*. A substantial
change is a new version.

Question: `QUESTION_v1` · Written: _yyyy-mm-dd_ · Outcome examined yet? _no_

## Split

How rows are divided, and why that matches how the model will be used
([DM1/F7](https://github.com/wmacevoy/data-mining/blob/main/guide/03-feedback.md#f7)).

- **Grouping:** rows sharing _…_ stay on one side.
- **Time:** train on _period_, validate on _period_, hold out _period_.
- **Holdout:** where it is kept, who may read it, and when it will be spent
  ([DM1/F5](https://github.com/wmacevoy/data-mining/blob/main/guide/03-feedback.md#f5)): _…_

## Metric and baseline

([DM1/T1](https://github.com/wmacevoy/data-mining/blob/main/guide/06-testing.md#t1))

- **Primary metric:** _…_, because _…_ (tie to the price of errors in the question)
- **Second metric**, the one the search is not told about
  ([DM1/F9](https://github.com/wmacevoy/data-mining/blob/main/guide/03-feedback.md#f9)): _…_
- **Baseline:** _the dumbest reasonable method_ — scored on _yyyy-mm-dd_: _…_
- **Interval:** _bootstrap / analytic; seeds per configuration_

## Slices

Chosen now, so they are not chosen to flatter
([DM1/T9](https://github.com/wmacevoy/data-mining/blob/main/guide/06-testing.md#t9)).

| Slice | Why it matters | Expected *n* |
| ----- | -------------- | ------------ |

## Search budget

What will be tried, and roughly how many configurations
([DM1/F4](https://github.com/wmacevoy/data-mining/blob/main/guide/03-feedback.md#f4)). The ledger
records the actual count.

- _Model families: …_
- _Features: …_
- _Tuning: … configurations_
- _For pattern search (rules, subgroups, clusters): correction for the number of candidates — …_

## Missing data

For each input with gaps: why it is missing, and what we will do — drop, impute, or model the
indicator ([DM1/R5](https://github.com/wmacevoy/data-mining/blob/main/guide/04-requirements.md#r5)).

| Input | Why missing | Treatment |
| ----- | ----------- | --------- |

## Departures

- _yyyy-mm-dd_ — _what changed, why, and whether the outcome had been seen_
