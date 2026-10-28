# Changelog

What changed between releases, by principle ID, newest first. A change you cannot spot is a K3
factory ([SE1/U7](https://github.com/wmacevoy/software-engineering/blob/v1.3/guide/02-unknowing.md#u7)),
so changes are listed here by ID, and copies of AGENTS.md and the templates say which release they
came from.

Within DM1, a minor release may add principles, reword them, or extend what they ask; it never moves
an ID ([principle index](README.md#principle-index)). Work toward a release goes under
`## vX.Y — unreleased`; give it a date when you tag it. Until v1.0 is tagged, copies link to `main`;
after, `tools/check.js` requires them to link to the newest dated release. Links to SE1 never name
`main`: they name the SE1 release this guide was last reviewed against, which each release below
states.

**If you keep a copy** of AGENTS.md or the templates, read *For copies* in each release newer than
yours.

## v1.0 — unreleased

· 93 principles

The first release: 75 principles that reframe SE1 principles for data work, and 18 new ones that
SE1 has no counterpart for. Refactored from the course document `DATA-SCIENCE.md`, reorganized into
SE1's ten chapters. Bias is treated as SE1 treats security: a permanent requirement
([DM1/R10](guide/04-requirements.md#r10)), an audit before and after deploy
([DM1/O9](guide/07-operating.md#o9)), and items in the checklists, AGENTS.md, and the templates.

Written on 2026-10-27 against SE1 at commit `d256d10`, between SE1 v1.1 and v1.2, with every SE1
link naming `main`. On 2026-10-28 the links were pinned to **SE1 v1.3**: `tools/check.js` builds
every SE1 link from one constant, `SE_RELEASE`, and CI checks SE1 IDs against that tag. A later SE1
bump is that one edit, a rewrite of the links, and a walk through SE1's CHANGELOG for every ID this
guide reframes, recorded here by ID.

### SE1 v1.2 to v1.3, reviewed

Each SE1 principle that changed between the commit this guide was written against and v1.3, and
what this guide did about it. Reviewed 2026-10-28 by Claude Fable 5.1 with Warren MacEvoy, who
signs the release (SE1/U9).

- [SE1/U7](https://github.com/wmacevoy/software-engineering/blob/v1.3/guide/02-unknowing.md#u7) and
  [SE1/R8](https://github.com/wmacevoy/software-engineering/blob/v1.3/guide/04-requirements.md#r8), *medicine* for
  *cure*: adopted. The guide said *cure* in [DM1/U2](guide/02-unknowing.md#u2),
  [DM1/U6](guide/02-unknowing.md#u6), and [DM1/D9](guide/05-design.md#d9). A K3 factory is
  lessened, not fixed, and so is train/serve skew.
- [SE1/U7](https://github.com/wmacevoy/software-engineering/blob/v1.3/guide/02-unknowing.md#u7), *torn work*: adopted
  into [DM1/U2](guide/02-unknowing.md#u2), which names its data shapes (a pipeline half-run, a
  model trained on a partial extract, a notebook run out of order) and the medicine (idempotent
  stages, the cold run from raw, and treating what you find on resuming as torn), and in one
  sentence into [DM1/U6](guide/02-unknowing.md#u6): an interrupted retrain's checkpoint answers.
- [SE1/A11](https://github.com/wmacevoy/software-engineering/blob/v1.3/guide/10-agents.md#a11), *knowing is not doing*:
  adopted into [DM1/U7](guide/02-unknowing.md#u7), where *look at the rows* becomes something the
  command does on every run, and [DM1/A2](guide/10-agents.md#a2): a leakage check the agent must
  choose to run will be read and not run, so the assertions go in the pipeline and CI. A11's
  other change, that the import boundary is the working directory, is in AGENTS.md.
- [SE1/U8](https://github.com/wmacevoy/software-engineering/blob/v1.3/guide/02-unknowing.md#u8), *leave whitespace*:
  reframed as [DM1/U9](guide/02-unknowing.md#u9). It pulls against [DM1/F4](guide/03-feedback.md#f4)
  to [DM1/F6](guide/03-feedback.md#f6), where every look spends evidence; the resolution is what
  is looked at. Whitespace on the inputs is free and is where K2 lives; on the outcome it is a
  look, and goes in the ledger. GLOSSARY gains *whitespace*.
- [SE1/H4](https://github.com/wmacevoy/software-engineering/blob/v1.3/guide/09-people.md#h4), the stand-up's fourth
  question: reframed as [DM1/H8](guide/09-people.md#h8). The discomfort in data work has a short
  list of shapes, each an early sign of something this guide names, so the question becomes *what
  about the current number do you not believe?*
- [SE1/U9](https://github.com/wmacevoy/software-engineering/blob/v1.3/guide/02-unknowing.md#u9), *rules change*: not a
  principle here. For labels, [DM1/R7](guide/04-requirements.md#r7) already asks who, when, and how
  often a second person disagrees; for definitions, [DM1/H5](guide/09-people.md#h5) asks who chose
  it. What the templates lacked was the falsifier: DATASHEET and MODEL_CARD now say who wrote them,
  when, and what would show them wrong.
- [SE1/A3](https://github.com/wmacevoy/software-engineering/blob/v1.3/guide/10-agents.md#a3), an agent may ask, and a
  private agent memory is a head: confirmed, no change. This guide never said the client does not
  talk to the agent, and [DM1/A3](guide/10-agents.md#a3) already keeps the record of what was
  tried in the ledger, not in the agent's memory.
- [SE1/W7](https://github.com/wmacevoy/software-engineering/blob/v1.3/guide/08-work.md#w7), Brown's experiment as he ran
  it: confirmed, no change. [DM1/W5](guide/08-work.md#w5) cites the gradient and does not restate
  the experiment.
- [SE1/W2](https://github.com/wmacevoy/software-engineering/blob/v1.3/guide/08-work.md#w2) and
  [SE1/T5](https://github.com/wmacevoy/software-engineering/blob/v1.3/guide/06-testing.md#t5), wording only: no DM1
  principle quotes the changed words.
- Not reviewed: whether the 73 reframings written against the earlier commit still read true
  against v1.3's unchanged principles. Their IDs resolve, which is all `tools/check.js` can say.
- AGENTS.md, after SE1 v1.2's: says who drafted it and when, and that nothing in it has been
  tried; loads from copies inside the working directory, with a check that they loaded; a new
  section *After a gap, additions* (the ledger, not the summary, counts looks; derived data found
  after a gap is torn; a kernel is a summary). CHECKLISTS' *Handing an agent data work* aligns
  with SE1's *Handing a task to an agent*: loaded not opened, checks in the pipeline, the retro
  questions. The `./se` line waits until `se` knows this guide's documents.
- `tools/check.js`, after SE1 v1.2.1 to v1.3's: SE1 IDs and anchors resolve at the pinned tag,
  read from the local clone through git, and a clone without the tag is a named problem; copies
  cite no DM1 ID their labeled release lacks; a patch release (`v1.0.1`) changes no principle,
  AGENTS.md, or template, and a principle's text ends at a horizontal rule. Seen red on three
  planted breakages. *Changed in* markers wait for a release to mark against.
- README gains *Why to trust this, and why to doubt it*: SE1/U9 applied to the guide on its front
  page. CI checks out SE1 at the pinned tag and this repository with its history, for the checks
  that read tags.
- `dm`, `dm.ps1`, `dm.py`: a command-line companion for a data project, beside SE1's `se.py`.
  `./dm --doctor` runs SE1's doctor and adds eleven rows this guide asks to be mechanical: both
  working agreements loaded, the question's one-way doors, the plan, the holdout's home and reach,
  every column's knowable-at, raw read-only, raw to report, the ledger and its writer, the model
  card and its bias audit, the environment, and citations of the question. Every row seen red on a
  fixture built to fail it (`tools/test_dm.py`); every threshold invented, none yet run on a real
  project (GAPS 7). CI runs the checker and the tests on Linux, macOS, and Windows, on Python 3.9
  and the newest; `.gitattributes` keeps line endings LF. MODEL_CARD's bias row cites `Q1/BIAS-1`,
  versioned, as the question template asks (SE1/R10).

**For copies:** copy AGENTS.md beside SE1's AGENTS.md, inside the working directory; import both at
every start, and check that they loaded (SE1/A11).

### New

The principles with no SE1 counterpart:

- [DM1/U3](guide/02-unknowing.md#u3) Leakage is the canonical K3: it feels like a good result.
- [DM1/U8](guide/02-unknowing.md#u8) People ask Prob(result | me); the data holds Prob(result |
  the rows it counts as like me).
- [DM1/F4](guide/03-feedback.md#f4) The search is part of the result.
- [DM1/F5](guide/03-feedback.md#f5) The holdout is a consumable.
- [DM1/F6](guide/03-feedback.md#f6) Count your looks, and say the number.
- [DM1/F7](guide/03-feedback.md#f7) A point estimate is half a result.
- [DM1/F8](guide/03-feedback.md#f8) A large sample does not rescue a biased one; it disguises it.
- [DM1/R2](guide/04-requirements.md#r2) Fix the unit, the outcome, and the prediction point before
  anything else.
- [DM1/R6](guide/04-requirements.md#r6) Know, per column, when its value became knowable.
- [DM1/R7](guide/04-requirements.md#r7) A label is an opinion with a timestamp.
- [DM1/T7](guide/06-testing.md#t7) Ask for the diff in the numbers, not only the diff in the code.
- [DM1/T9](guide/06-testing.md#t9) Evaluate by slice.
- [DM1/T11](guide/06-testing.md#t11) Unsupervised results have no answer key: test their stability.
- [DM1/O4](guide/07-operating.md#o4) Name the shift.
- [DM1/H6](guide/09-people.md#h6) Present uncertainty in the client's units and decisions.
- [DM1/A4](guide/10-agents.md#a4) Keep the holdout out of the agent's reach.
- [DM1/A8](guide/10-agents.md#a8) Data sent to an agent has left the room.
- [DM1/A9](guide/10-agents.md#a9) A language model in the pipeline is a model.
