# Checklists

Every checklist in the guide, in the order a project meets them. Each item cites the principle that
explains it; if an item retires no fear on your project, drop it and say why
([DM1/P4](guide/01-purpose.md#p4)). SE1's
[checklists](https://github.com/wmacevoy/software-engineering/blob/v1.3/CHECKLISTS.md) still apply
to the pipeline as software; these are the ones data work adds.

## Starting

**The first conversation with the client**

- [ ] The decision before the technique: who decides what, when, and what a wrong call costs.
      ([DM1/R1](guide/04-requirements.md#r1))
- [ ] What would they do if the answer came out the other way? If nothing, stop.
      ([DM1/R1](guide/04-requirements.md#r1))
- [ ] Whose rows are these, what were they collected for, and is this that?
      ([DM1/P3](guide/01-purpose.md#p3), [DM1/R9](guide/04-requirements.md#r9))
- [ ] Which mistake is worse, by about how much? ([DM1/R4](guide/04-requirements.md#r4))
- [ ] Is the question about one case or about a population? If one case, which reference class
      will the answer actually describe? ([DM1/U8](guide/02-unknowing.md#u8))
- [ ] Which groups matter — to the client and to the people in the data — and which gap between
      them would be unacceptable? ([DM1/R10](guide/04-requirements.md#r10))
- [ ] Who knows what the columns mean, and how many of their hours can we have?
      ([DM1/R8](guide/04-requirements.md#r8), [DM1/H1](guide/09-people.md#h1))

**Before looking at the outcome**

- [ ] Unit, outcome, and prediction point written in `QUESTION_v1`, and read to the client.
      ([DM1/R2](guide/04-requirements.md#r2))
- [ ] The bar — metric, baseline, threshold, split — written and dated.
      ([DM1/R3](guide/04-requirements.md#r3))
- [ ] The holdout split off, out of casual reach — including agents'.
      ([DM1/F5](guide/03-feedback.md#f5), [DM1/A4](guide/10-agents.md#a4))
- [ ] `PLAN_v1` written: split, metrics, slices, search budget, missing-data treatment.
      ([DM1/F6](guide/03-feedback.md#f6), [DM1/T9](guide/06-testing.md#t9))
- [ ] The ledger exists and the scoring code appends to it. ([DM1/F6](guide/03-feedback.md#f6))

## Building

**For every data source**

- [ ] A datasheet: origin, license, exclusions, people, revisions.
      ([DM1/D13](guide/05-design.md#d13))
- [ ] Per column: units, clock, sentinels, and *when it becomes knowable*.
      ([DM1/R6](guide/04-requirements.md#r6), [DM1/D5](guide/05-design.md#d5))
- [ ] Absent, late, wrong, lying: a stated answer for each. Why it is missing before how to fill it.
      ([DM1/R5](guide/04-requirements.md#r5))
- [ ] The raw copy is immutable, with its fetch time and source recorded.
      ([DM1/D6](guide/05-design.md#d6), [DM1/D2](guide/05-design.md#d2))

**Before trusting a pipeline**

- [ ] One command from raw to every reported number, run from a cold cache.
      ([DM1/D6](guide/05-design.md#d6))
- [ ] Row counts asserted across every join and filter; keys asserted unique.
      ([DM1/T2](guide/06-testing.md#t2))
- [ ] A fixture with hand-computed answers, containing the ugliest real cases, large enough to reach
      every branch. ([DM1/T3](guide/06-testing.md#t3), [DM1/T6](guide/06-testing.md#t6))
- [ ] Each stage idempotent; re-running it changes nothing. ([DM1/D4](guide/05-design.md#d4))
- [ ] Features built with as-of joins at the prediction point. ([DM1/D3](guide/05-design.md#d3))
- [ ] Transforms are functions; notebooks only call them. ([DM1/D7](guide/05-design.md#d7))
- [ ] A golden output committed, and its diff part of every review.
      ([DM1/T7](guide/06-testing.md#t7))
- [ ] Run once at full size, and timed. ([DM1/O10](guide/07-operating.md#o10))

## Claiming

**Before presenting a number**

- [ ] It beats the baseline by more than its interval and the seed spread.
      ([DM1/T1](guide/06-testing.md#t1), [DM1/F7](guide/03-feedback.md#f7))
- [ ] The count of things tried is stated. ([DM1/F6](guide/03-feedback.md#f6))
- [ ] If it looks too good: one prediction traced to its rows, each row knowable at the prediction
      point. ([DM1/U3](guide/02-unknowing.md#u3))
- [ ] Reported by slice, with *n*. ([DM1/T9](guide/06-testing.md#t9))
- [ ] The bias measures the requirements chose, per group, with intervals; each source of bias
      (historical, selection, measurement, aggregation, evaluation, deployment) checked or named as
      unchecked. ([DM1/R10](guide/04-requirements.md#r10))
- [ ] The reference class is stated with any number about an individual case.
      ([DM1/U8](guide/02-unknowing.md#u8))
- [ ] Who is missing from the rows is said out loud. ([DM1/F8](guide/03-feedback.md#f8))
- [ ] A plot and the rows that disagree most have been looked at. ([DM1/U7](guide/02-unknowing.md#u7))
- [ ] Stated in the decision's units, with how often it will be wrong.
      ([DM1/H6](guide/09-people.md#h6))
- [ ] The K4s it rests on are written and have been read to the client.
      ([DM1/U4](guide/02-unknowing.md#u4), [DM1/H2](guide/09-people.md#h2))
- [ ] Someone other than the author regenerated it from raw. ([DM1/W7](guide/08-work.md#w7))

**Before spending the holdout**

- [ ] There is a decision it serves, written in the ledger. ([DM1/F5](guide/03-feedback.md#f5))
- [ ] Everything to be compared is frozen; nothing will be tuned afterward.
- [ ] You know where the next fresh holdout comes from.

**Before trusting a pattern** (clusters, rules, subgroups, anomalies)

- [ ] Corrected for the number of candidates searched. ([DM1/F4](guide/03-feedback.md#f4))
- [ ] Survives resampling, another period, and the arbitrary settings.
      ([DM1/T11](guide/06-testing.md#t11))
- [ ] A domain expert has seen members, not centroids. ([DM1/H1](guide/09-people.md#h1))

## Deploying

**Before a model decides anything**

- [ ] A model card: identity, intended use, not-for, slices, threshold and its price ratio.
      ([DM1/D10](guide/05-design.md#d10))
- [ ] Training and serving compute every feature with the same code.
      ([DM1/D9](guide/05-design.md#d9))
- [ ] Inputs outside the training envelope are flagged or refused. ([DM1/U6](guide/02-unknowing.md#u6))
- [ ] A bias audit: per-group measures and calibration on the holdout, and a search for the group
      it is worst for, confirmed on fresh data. ([DM1/O9](guide/07-operating.md#o9))
- [ ] A fallback that is not a model, and the switch to it tested. ([DM1/O5](guide/07-operating.md#o5))
- [ ] Run in shadow against the current model, by slice. ([DM1/O6](guide/07-operating.md#o6))
- [ ] What it will change about future training data is written, and a slice is kept without it.
      ([DM1/O11](guide/07-operating.md#o11))
- [ ] Environment and hardware recorded with the artifact. ([DM1/O1](guide/07-operating.md#o1))

**While it runs**

- [ ] Input distributions, output distribution, abstention rate, and source freshness are
      monitored, with alerts a person will believe. ([DM1/O3](guide/07-operating.md#o3))
- [ ] Each kind of shift has a named signal. ([DM1/O4](guide/07-operating.md#o4))
- [ ] The per-group gaps are monitored as labels arrive, and who the model is used on is compared
      with who it was trained on. ([DM1/O9](guide/07-operating.md#o9))
- [ ] Realized error and calibration, by slice, as labels arrive. ([DM1/O3](guide/07-operating.md#o3))
- [ ] An owner and a date for the next "is it still true?" ([DM1/D12](guide/05-design.md#d12))
- [ ] Every retrain passes the same checks as a code change. ([DM1/O6](guide/07-operating.md#o6))

## Working with agents

**Handing an agent data work**

- [ ] It loads both AGENTS.md files at start. ([AGENTS.md](AGENTS.md))
- [ ] It cannot read the holdout. ([DM1/A4](guide/10-agents.md#a4))
- [ ] It sees the schema and a fixture, not rows about people, unless decided otherwise.
      ([DM1/A8](guide/10-agents.md#a8))
- [ ] Its scoring appends to the ledger. ([DM1/A3](guide/10-agents.md#a3))

**Reviewing what it produced**

- [ ] The diff in the numbers, not only the code. ([DM1/T7](guide/06-testing.md#t7))
- [ ] The joins, filters, splits, and fills read line by line. ([DM1/A6](guide/10-agents.md#a6))
- [ ] Its count of tries, and its holdout looks (should be zero). ([DM1/A3](guide/10-agents.md#a3))
- [ ] You can explain the number without it. ([DM1/A7](guide/10-agents.md#a7))
