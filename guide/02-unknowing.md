# 2. Unknowing

The five kinds of not-knowing (`K0`–`K4`) from [SE1 chapter 2](https://github.com/wmacevoy/software-engineering/blob/main/guide/02-unknowing.md),
applied to datasets and methods — and why data work is unusually good at producing the dangerous
kind. The labels are defined there and in [GLOSSARY.md](../GLOSSARY.md).

---

### <a id="u1"></a>U1. Mining is discovering, in the right order and at the right price, which category each column and each step belongs to

*Reframes [SE1/U2](https://github.com/wmacevoy/software-engineering/blob/main/guide/02-unknowing.md#u2).*

| From | To     | How, in data                                                                                       |
| ---- | ------ | -------------------------------------------------------------------------------------------------- |
| K0   | stays  | An assertion in the pipeline beats a sentence in a README, and both beat a fact in your head.       |
| K1   | K0     | Look: profile the column, plot the distribution, read the data dictionary, ask who collected it. The only category you can simply decide to spend money on. |
| K2   | K1     | Run end to end on real data early, plot the residuals, show a domain expert, score on a period you did not develop on. You cannot search for these; you can only arrange to be surprised sooner. |
| K3   | K0     | A check that could have failed, a plot you actually looked at, a baseline that could have won, a second person who does not share your assumption. |
| K4   | chosen | Name the falsehood, write down where it is load-bearing ([DM1/U4](#u4)).                             |

K2 in data work is not a risk; it is a certainty, and it usually arrives as a sentence: *that column
means something different before 2024*. Plan for the sentence.

> **Ask:** "Have I looked at this column, or only at its name?"

### <a id="u2"></a>U2. Data work manufactures K3, because the failure is a returned value, not an exception

*Reframes [SE1/U3](https://github.com/wmacevoy/software-engineering/blob/main/guide/02-unknowing.md#u3) and [SE1/U7](https://github.com/wmacevoy/software-engineering/blob/main/guide/02-unknowing.md#u7).*

Software that is wrong tends to stop. Analysis that is wrong tends to continue and produce a chart.

A join that silently duplicates rows returns a DataFrame. A timezone off by six hours returns
timestamps. A `dropna()` that removes exactly the interesting cases returns a smaller, cleaner,
entirely misleading table. A `try/except` around a fetch turns an outage into a quiet day. Every one
of these is a K3 factory in the sense of SE1/U7 — it keeps saying "fine" with no way to say "wrong" —
and pandas ships with dozens.

SE1/F4 says software has no mass, so nothing sags to warn you. Data has less than none: a wrong
number has the same shape as a right one, and the most likely thing to happen to it is that it gets
used.

The cure is the one SE1/U7 names: give each of these a way to say *wrong*. Row counts asserted
across every join, keys asserted unique, ranges and units asserted at the boundary
([DM1/T2](06-testing.md#t2)).

> **Ask:** "What here would return a plausible number if it were wrong?"

### <a id="u3"></a>U3. Leakage is the canonical K3: it feels like a good result

*New.*

Leakage is any path by which information about the answer reaches the model at training time that
will not be there at prediction time: a feature that encodes the label, a split with the same lot
and night on both sides, a normalization computed before the split, an "arrival time" column that is
really the time the gate scan was uploaded.

Leakage does not feel like a mistake. The metric improves and cross-validation agrees, because
**everything you would normally use to catch an error is the thing being fooled.** That is why
leakage is found by reading provenance — when each value became knowable ([DM1/R6](04-requirements.md#r6))
— not by reading the score.

Which gives a rule with no counterpart in software: **a result too good for the problem is a bug
report until proven otherwise.** "The AUC is 0.97" is K3 until you have traced one prediction back
to the rows that produced it and checked that each of them existed at the prediction point.

> **Ask:** "Could the model have known this at the moment it would have to predict?"

### <a id="u4"></a>U4. Every model is a chosen falsehood; name the direction it is wrong

*Reframes [SE1/U4](https://github.com/wmacevoy/software-engineering/blob/main/guide/02-unknowing.md#u4).*

Box's *all models are wrong, some are useful* is a sentence about K4, and the half that matters is
unspoken: **wrong in a specific, nameable direction.** A catalogue, every entry false and every
entry in use:

- The rows are independent. (They share a sensor, a night, an event, a household.)
- The sample represents the population. (It represents whoever was easy to measure.)
- The past distribution is the future distribution. (Stationarity is a hope with a p-value.)
- The label is the truth. (It is what a tired person clicked, under instructions from last year.)
- Missing is missing at random. (A sensor is most likely to drop off the network when the lot is
  busiest.)
- A day is twenty-four hours. (Two a year are not; [DM1/D5](05-design.md#d5).)
- De-identified means anonymous. (It means nobody has tried yet.)

You cannot analyze anything without these. The work is choosing them deliberately, writing them
down, and knowing the blast radius: independence fails and your intervals are too narrow;
stationarity fails and your backtest was fiction. **A K4 you have chosen is an asset; the same
falsehood held unknowingly is K3** — and the distance between them is one written sentence.

> **Ask:** "Which of these are we assuming, and where is it written?"

### <a id="u5"></a>U5. Estimate the category: time-box the cleaning, estimate the modeling

*Reframes [SE1/U5](https://github.com/wmacevoy/software-engineering/blob/main/guide/02-unknowing.md#u5).*

"Two days to clean this dataset" is a K0 statement about K2 work: you cannot estimate the time to
discover things you do not know are there. Cleaning and exploration get time-boxed, and each box ends
on a fence ([DM1/W4](08-work.md#w4)). Modeling from a known-good feature table, with a fixed metric
and split, estimates fine.

Say which kind you are handing over. "I'll know by Thursday whether the gate data is usable" is
honest. "The model will be done Thursday" usually is not, because it hides a cleaning box inside a
modeling estimate.

> **Ask:** "Is this an estimate, a range, or a time box — and is there cleaning hidden inside it?"

### <a id="u6"></a>U6. A model always answers; give it a way to say "I don't know"

*Reframes [SE1/U7](https://github.com/wmacevoy/software-engineering/blob/main/guide/02-unknowing.md#u7).*

A classifier asked about an input unlike anything it was trained on does not raise. It returns a
class, often with high confidence. That is the purest K3 factory in the field: it has no way to say
*wrong*, and no way to say *I have never seen this*.

Three cures, cheapest first:

- **Check the input against the training envelope** — ranges, categories never seen, a lot that
  did not exist last season — and refuse or flag outside it.
- **Calibrate**, so that 0.8 means right about 80% of the time, and check that it does on data you
  did not fit on.
- **Abstain**: let the model return *no answer* below a confidence, and count how often it does.
  A rising abstention rate is a drift alarm that needs no labels ([DM1/O3](07-operating.md#o3)).

> **Ask:** "What does this model say when it is shown something it has never seen?"

### <a id="u7"></a>U7. A summary statistic is a concussion: look at the rows

*Reframes [SE1/A11](https://github.com/wmacevoy/software-engineering/blob/main/guide/10-agents.md#a11).*

SE1/A11 says a summary of a session drops things without knowing what it dropped, and must be
checked from outside. A mean, a correlation, or an accuracy is the same thing for a dataset.
Anscombe's four datasets share their means, variances, correlation, and regression line, and look
nothing alike.

Checking from outside, here, means a plot and a handful of raw rows — chosen at random, and then
chosen at the extremes. Before you trust a summary, look at the rows that most disagree with it.

> **Ask:** "What did this number average away — and have I looked at the rows that disagree?"

### <a id="u8"></a>U8. People ask Prob(result | me); the data holds Prob(result | the rows it counts as like me)

*New.*

Most questions put to a model are about one case, with a yes-or-no or categorical answer: will *I*
get the loan, will *this* lot fill tonight, is *this* reading a fault? What data can estimate is a
rate in a population: among rows like this one, how often did it happen? A model conditions on the
columns it has, which narrows the population — but never down to you. Which rows count as "like
you" is decided by which columns were recorded and how the model pools them, not by what is true
about you.

Two consequences, both easy to miss:

- **A probability for one binary outcome is a property of a reference class, not of the case.**
  "70%" means: of a hundred cases the model cannot tell apart from yours, about seventy happened.
  Yours will happen or it won't. Say it that way ([DM1/H6](09-people.md#h6)), and name the class.
- **Putting yourself in the data does not fix it.** Your row is one of *n*, so the estimate for you
  is mostly other people's outcomes. What makes you different from them is exactly what the columns
  do not hold.

This is the common K3 behind most bias. The number looks like an answer to the question asked, so
nobody checks that it answers a different one. And the gap is not spread evenly. A model pools sparse
groups toward the majority — shared parameters and regularization exist to do exactly that — so a
group that is small, under-recorded, or measured differently gets an answer shaped by everyone else.
For the majority, Prob(result | class) is close to Prob(result | me); for a minority it can be off
**systematically, in one direction.** That systematic gap is bias, and it is found only by looking
for it ([DM1/R10](04-requirements.md#r10), [DM1/O9](07-operating.md#o9)).

In the running example, a driver asks, "Will I find a space in lot C?" The model knows how often lot
C was full by 6:40 on nights like this. Whether *this* driver finds a space depends on when they
arrive, which entrance they use, and what else happens tonight — none of which is in the rows. And
the small lots, with few events of their own, get forecasts shaped by the big ones.

> **Ask:** "Is this question about one case or a population — and which reference class does this
> number actually describe?"

---

Next: [3. Feedback](03-feedback.md) — what evidence costs, and why searching for it changes it.
