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

· 91 principles

The first release: 73 principles that reframe SE1 principles for data work, and 18 new ones that
SE1 has no counterpart for. Refactored from the course document `DATA-SCIENCE.md`, reorganized into
SE1's ten chapters. Bias is treated as SE1 treats security: a permanent requirement
([DM1/R10](guide/04-requirements.md#r10)), an audit before and after deploy
([DM1/O9](guide/07-operating.md#o9)), and items in the checklists, AGENTS.md, and the templates.

Written on 2026-10-27 against SE1 at commit `d256d10`, between SE1 v1.1 and v1.2, with every SE1
link naming `main`. On 2026-10-28 the links were pinned to **SE1 v1.3**: `tools/check.js` builds
every SE1 link from one constant, `SE_RELEASE`, and CI checks SE1 IDs against that tag. A later SE1
bump is that one edit, a rewrite of the links, and a walk through SE1's CHANGELOG for every ID this
guide reframes, recorded here by ID.

**For copies:** copy AGENTS.md beside SE1's AGENTS.md, and import both at every start.

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
