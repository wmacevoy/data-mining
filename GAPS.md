# Gaps

Where the guide falls short. In SE1 this file holds field reports — what happened when the guide met
a real project — and each entry is closed by changing the guide, or by a sentence saying why not
([SE1/P4](https://github.com/wmacevoy/software-engineering/blob/v1.3/guide/01-purpose.md#p4)).

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
[SE1/O2](https://github.com/wmacevoy/software-engineering/blob/v1.3/guide/07-operating.md#o2) says to
commit the lock. The course repository leaves its lock file uncommitted, because it resolves
differently across students' machines.

**Open:** whether that is a gap in SE1/O2, or a local exception that should be written down as one.

### 7. The doctor has never met a project

`dm --doctor` (`dm.py`, beside SE1's `se.py` in a project) was written on 2026-10-28 from the
principles, not from a project. Every row is something this guide says must be mechanical rather
than told ([DM1/A4](guide/10-agents.md#a4), [DM1/D6](guide/05-design.md#d6),
[DM1/F6](guide/03-feedback.md#f6), [DM1/R6](guide/04-requirements.md#r6)), and every threshold and
heuristic in it is invented: which files count as the ledger, what a placeholder looks like, what
*readable* means for a holdout. Its tests are fixtures written beside it, which is the guard tested
against its own stub that SE1's GAPS warns about. It has not been run on a repository that was not
built to pass it.

Two things it exposed while being written:

- **The two AGENTS.md copies had no names.** Closed 2026-10-29: SE1's stays `AGENTS.md` at the root,
  where SE1's doctor and Claude Code's own read look for it, and this guide's is `AGENTS-DM.md`
  beside it, both imported from `CLAUDE.md` (AGENTS.md's header, the README, the CONTRIBUTING
  template). The doctor still tells them apart by which guide they link to, so a project that chose
  other names is told the guide's, not failed. Whether two files loaded from one CLAUDE.md behave
  as one agreement is untested, like the rest.
- **"Readable from the working directory" has no definition** ([DM1/A4](guide/10-agents.md#a4)).
  The doctor treats a path outside the repository, or inside it but absent and git-ignored, as out
  of reach, and a tracked or present file as in reach. An agent with a shell can read any path the
  user can; the thing that would make a holdout truly unreachable, a permission or another host, is
  not something a doctor can see from the repository.

**Wrong if** the first course project runs it and every row that failed was one the owner already
knew about, or a row that passed hid the thing that went wrong. **Open:** the first field report.
