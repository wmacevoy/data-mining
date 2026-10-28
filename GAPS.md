# Gaps

Where the guide falls short. In SE1 this file holds field reports — what happened when the guide met
a real project — and each entry is closed by changing the guide, or by a sentence saying why not
([SE1/P4](https://github.com/wmacevoy/software-engineering/blob/main/guide/01-purpose.md#p4)).

**There are no field reports yet.** DM1 has not been applied to a project in its current form; the
first reports are expected from the fall 2026 course projects. Until then, this file lists where the
guide is known to be thin, so that nobody mistakes silence for coverage.

## Known thin places

### 1. Causal claims

The guide is about predictive and descriptive claims: what will happen, what patterns exist. It says
almost nothing about *why* — whether changing X would change Y. Most real decisions are causal
("if we open lot C earlier, will the queue at B shrink?"), and a predictive model answers them badly
and confidently. Confounding, experiments, and observational causal inference need principles of their
own.

**Open:** a chapter, or principles inside chapters 3 and 4, on when a claim is causal and what
evidence that requires.

### 2. Streaming and online learning

Chapter 7 assumes models trained in batches and deployed. A model updated continuously on live data
has no deploy to gate, and its feedback loop ([DM1/O11](guide/07-operating.md#o11)) runs at the speed
of the data.

### 3. Privacy techniques are named, not taught

[DM1/R9](guide/04-requirements.md#r9) and [DM1/O8](guide/07-operating.md#o8) name the threats
(re-identification, membership inference) and the cheapest defense (not keeping the data). They do not
cover aggregation thresholds, differential privacy, or synthetic data, or when each is enough.

### 4. Language models in the pipeline

[DM1/A9](guide/10-agents.md#a9) is one principle covering prompts, nondeterminism, judges, and
contamination. Retrieval systems — chunking, embedding choice, retrieval evaluation — get one line
in [DM1/D2](guide/05-design.md#d2). That is probably not enough, and the course's retrieval lab is
the obvious first field report.

### 5. Untested claims about readability

The guide's chapters are short because SE1 carries the long arguments. Whether a reader who has not
read SE1 can follow the *Reframes* links and come away with the idea — rather than a fragment of it —
has not been tested, with people or with agents.

### 6. Recording the environment without committing the lock

[DM1/O1](guide/07-operating.md#o1) asks that each result record the resolved environment, so that it
works whether or not a lock file is committed.
[SE1/O2](https://github.com/wmacevoy/software-engineering/blob/main/guide/07-operating.md#o2) says to
commit the lock. The course repository leaves its lock file uncommitted, because it resolves
differently across students' machines.

**Open:** whether that is a gap in SE1/O2, or a local exception that should be written down as one.
