# 6. Testing

Checks worth trusting, for the two things a data system has to get right: the *pipeline*, which is
ordinary code and tests like it, and the *model*, which cannot be read and must be tested from
outside. Read with [SE1 chapter 6](https://github.com/wmacevoy/software-engineering/blob/v1.3/guide/06-testing.md),
all of which applies to the pipeline as written.

---

### <a id="t1"></a>T1. Build the evaluation before the model, and enter a dumb baseline first

*Reframes [SE1/T8](https://github.com/wmacevoy/software-engineering/blob/v1.3/guide/06-testing.md#t8).*

SE1/T8: when you don't know how to build it, write the tests that would pass when it works. In
modeling, that test is the evaluation harness — the split, the metric, the bar
([DM1/R3](04-requirements.md#r3)), and the report — and it comes first, before any model exists.

The first contestant is the dumbest one that could win: the mean, the majority class, *same as last
week*, *same as the last comparable event*. Three things follow:

- The harness is exercised end to end on day one, so its bugs are found while the stakes are low.
- Every later model has a number to beat, and "beats the baseline by more than the interval" is the
  done sentence.
- Sometimes the baseline wins. That is a finding, and an inexpensive one.

> **Ask:** "What does the dumbest reasonable method score on this — and have we run it?"

### <a id="t2"></a>T2. A reliable pipeline checks itself: assert what joins and filters break

*Reframes [SE1/T2](https://github.com/wmacevoy/software-engineering/blob/v1.3/guide/06-testing.md#t2).*

SE1/T2's ladder ends at *a reliable thing checks itself*. A pipeline does that with assertions that
run every time, on real data, not only in tests:

- **Row counts across every join and filter** — expected equal, expected at most, or expected within
  a range — so a many-to-many join cannot silently triple the table.
- **Key uniqueness** where a key is supposed to be unique.
- **A monotone, gap-checked time index** where time is the index.
- **Units and plausible ranges** at the boundary where data enters: no negative occupancy, no lot
  with more cars than spaces.
- **Fractions of missing and defaulted values**, compared with the last run.

Each one turns a returned value back into an exception ([DM1/U2](02-unknowing.md#u2)). A failed
assertion that stops a run is a gift; the same problem as a plausible number is a liability.

> **Ask:** "If this join multiplied the rows, which line would fail?"

### <a id="t3"></a>T3. A check that cannot fail proves nothing — including a fixture too small to exercise the estimator

*Reframes [SE1/T3](https://github.com/wmacevoy/software-engineering/blob/v1.3/guide/06-testing.md#t3).*

Data tests are especially prone to asserting shape instead of value: the output is non-empty, the
column exists, the row count survived. Those pass on garbage.

A subtler case: a fixture too small to reach the logic. A one-day fixture fed to a daily aggregate
returns one row; a rolling z-score over one row is `NaN`; the assertion that input and output have
the same length compares 1 to 1, and the estimator under test never ran. Make each fixture large
enough to exercise every branch, and assert on values you worked out by hand.

The same rule covers every instrument that judges a result — a metric script, a labeler, an LLM used
as a judge. Each must be seen to disagree with a bad answer before its agreement means anything.

> **Ask:** "What wrong output would this test still pass — and have I seen it fail?"

### <a id="t4"></a>T4. A number that moves for no reason trains everyone to ignore it

*Reframes [SE1/T4](https://github.com/wmacevoy/software-engineering/blob/v1.3/guide/06-testing.md#t4).*

SE1/T4: a loop you do not trust is worse than none. In data, the untrusted loop is a metric that
changes between runs with nothing changed — unseeded randomness, nondeterministic data order, a
source that returns a different revision, a cache that may or may not be stale. After the third
unexplained wobble, a real regression of the same size gets the same shrug.

Make every run reproduce its number, or report the spread it is expected to have
([DM1/T5](#t5)). Then a move outside that spread means something.

> **Ask:** "If this metric moved by two points tomorrow, would anyone believe it meant something?"

### <a id="t5"></a>T5. Decide which results must be identical and which must agree within a tolerance

*Reframes [SE1/T5](https://github.com/wmacevoy/software-engineering/blob/v1.3/guide/06-testing.md#t5) and [SE1/T9](https://github.com/wmacevoy/software-engineering/blob/v1.3/guide/06-testing.md#t9).*

A seed is necessary and not sufficient. GPU kernels, thread scheduling, library versions, and the
order of floating-point sums all change results across machines and sometimes across runs. Demanding
bit-for-bit equality everywhere produces flaky tests; demanding nothing produces untestable claims.
Decide per claim:

- **Identical:** data transforms on a fixed input, splits, anything with no floating-point
  reduction. Test with equality.
- **Within a tolerance:** model outputs, metrics, exports to another runtime. Test with a stated
  tolerance, chosen from the observed run-to-run spread, not from what makes the test pass.
- **Within a distribution:** results that depend on the seed. Test the mean and spread over several
  seeds ([DM1/F7](03-feedback.md#f7)).

> **Ask:** "Must this be the same number, or a close one — and how close, and who chose that?"

### <a id="t6"></a>T6. A fixture must fail the way real data fails

*Reframes [SE1/T6](https://github.com/wmacevoy/software-engineering/blob/v1.3/guide/06-testing.md#t6).*

SE1/T6: the mock and the real thing answer to the same test. A synthetic dataset is a mock of reality,
and a clean one tests only the happy path. Build the fixture from the failures you have actually
seen, small enough to work out its answers by hand:

- a missing hour, a `NaN`, a sentinel value, a duplicate key;
- a sensor that went `unreachable` at the peak;
- a reading uploaded late, and a value revised after the fact;
- both daylight-saving boundaries ([DM1/D5](05-design.md#d5));
- a category never seen in training.

Commit it, with the expected output beside it. It is the cheapest test in the repository and the one
every later change runs against.

> **Ask:** "Does the fixture contain the ugliest thing we have seen in the real data?"

### <a id="t7"></a>T7. Ask for the diff in the numbers, not only the diff in the code

*New.*

A code review shows what changed in the code. It does not show what changed in the output, and in a
data system that is the change that matters. A refactor that "shouldn't change anything" is a
hypothesis, testable in seconds against the fixture.

Keep a **golden output**: the fixture's full result, committed. Every change regenerates it, and the
diff is part of the review. An unexpected diff is a finding; an expected one is documented in the
same commit.

> **Ask:** "What did this change do to the numbers — and was that intended?"

### <a id="t8"></a>T8. Test a model with properties it must have, not only with a score

*Reframes [SE1/T10](https://github.com/wmacevoy/software-engineering/blob/v1.3/guide/06-testing.md#t10).*

SE1/T10: state the rule that must hold for every input, and let the machine generate the cases. A
model's rules are behavioral:

- **Invariance:** changes that must not change the answer. A digit shifted two pixels is the same
  digit. Renaming a lot does not change its forecast.
- **Direction:** changes that must move the answer one way. More tickets sold must not predict *more*
  free spaces.
- **Minimum functionality:** cases simple enough that any working model must get them right.

Each is a test that runs in seconds and catches failures an aggregate score hides. For transforms,
the properties are the invariants of [DM1/T2](#t2): row counts, key uniqueness, conservation of
totals.

> **Ask:** "What must this model never do, whatever the input — and does a test check it?"

### <a id="t9"></a>T9. Evaluate by slice; the aggregate hides the subgroup that fails

*New.*

An overall score is an average over slices, and an average can be fine while one slice is broken: the
small lots, the concerts, the first event after a schedule change, the people under-represented in
the data. Simpson's paradox is the extreme case: a model can be better in every slice and worse
overall, or the reverse.

Choose the slices with the question ([DM1/R2](04-requirements.md#r2)) — before results, so they are
not chosen to flatter — and report each with its *n* and interval. This is also where bias
becomes something you can check rather than assert: a slice is a group, and the per-slice error is
the treatment that group receives ([DM1/R10](04-requirements.md#r10), [DM1/O9](07-operating.md#o9)).

> **Ask:** "Which slice is this model worst on — and how many rows does that slice have?"

### <a id="t10"></a>T10. When someone else owns "correct," compare against their implementation

*Reframes [SE1/T11](https://github.com/wmacevoy/software-engineering/blob/v1.3/guide/06-testing.md#t11).*

Many results in data mining have an owner of correctness who is not you: a reference library's
implementation of an algorithm, the original runtime of a model you exported, the published numbers
of a method you reimplemented. Test against them directly, within a tolerance ([DM1/T5](#t5)):

- your hand-written estimator against the library's on the same input;
- the exported model (ONNX, a browser runtime) against the training framework on real inputs;
- your reproduction against the paper's reported metric, with the gap explained.

> **Ask:** "Who else computes this, and does a test ask them?"

### <a id="t11"></a>T11. Unsupervised results have no answer key: test their stability

*New.*

Clusters, association rules, embeddings, and anomaly scores have no labels to score against, which
makes them the easiest results in the field to believe and the hardest to check. Three tests remain:

- **Stability under resampling.** Re-run on bootstrap samples or a different period. Clusters that
  rearrange themselves were not found; they were drawn.
- **Stability under the arbitrary choices.** Vary the seed, *k*, the distance, the scaling. A pattern
  that survives only one setting is a property of the setting.
- **A domain expert, shown examples.** Not the cluster centroids — five members of each cluster, and
  the question "do these belong together, and why?"

And because the search was large, apply [DM1/F4](03-feedback.md#f4): a rule that stands out among
thousands is expected to exist by chance.

> **Ask:** "If we ran this again on a different month, would we find the same thing?"

---

Next: [7. Operating](07-operating.md) — what happens to a model after it leaves your machine.
