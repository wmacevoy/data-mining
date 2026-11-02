# Review of DM1, toward v1.0

A review of all 93 principles against the first real project they have met, with what to change before tagging v1.0.
Written 2026-11-01 by Claude Opus 5.5 (`claude-opus-5-5`) for Warren MacEvoy, who decides and signs. The field report it rests on
is in [GAPS.md](GAPS.md). What follows *Status* is kept as written, when it was a proposal and no principle had been changed.

## Status

Addressed the same day, by another session of the same model, on the branch `field-report-1`. That session read this review, not the
project, so nothing here has been checked against the project itself. Before this was pushed, on the owner's decision, this file and
`GAPS.md` were made more general about the project, so some evidence below is vaguer than what was observed.

| Proposed | What happened |
| -------- | ------------- |
| Five principles | All in the guide: R12, U10, F10, T12, A10. |
| Seven changes | All in: D6, W7, R10, F9, O8, U7, A9. O8 and U7 use general examples, not the project's. |
| Smaller wording | All in: F5, A4, R2, O2, R8, W5. R8 omits the token figures. F6 and the templates take the ledger's reads and searches. |
| Doctor and templates | All in. `raw to report` can only ask and say, so it remains unable to see what this review caught: a project can answer it falsely. |
| Day of the tag, 2, 3, 6 | Done: what was tested is said, what's unproven is in `CHANGELOG.md` by chapter, and the handoff is in `archive/`. |
| **The tag** | **The owner, 2026-11-02: no, not now.** So this review's recommendation was not taken, and links stay on `main` (item 4). No principle was merged (item 1). |
| **The SE1 pin** | **The owner, 2026-11-02: stays at v1.3** (item 5). |
| The course's open item, one repository of several projects | **The owner, 2026-11-02:** one run is one project. In the doctor and `GAPS.md`. |

Corrections to this review, found while applying it:

- **"All have exact text or a named change" was not so.** P5, R3, D13, and A6 are marked *Extend* with no text anywhere below. Each now has a
  sentence, written while applying this, so those four are not what the review proposed.
- **T1, T3, and A8 had only a "see".** Each now points to the new principle.
- **T12's basis.** SE1/T8 isn't about baselines. The reframing runs through DM1/T1, and now says so. U10's basis in SE1/T3 is good: that text names
  "a tool that exits zero because it found nothing to check".
- **The tally reproduces:** 26, 14, 6, 20, 27, and each chapter's row, recounted by script from the table below. That checks the arithmetic, not the verdicts.

## The recommendation

**Tag v1.0 after the changes below, without waiting for the course projects, and say plainly what has been tested.**

Tagging freezes IDs, not wording: a minor release may add and reword, and never moves an ID. So the only work that truly
has to come first is what a freeze makes impossible, plus what would be untrue on the day of the tag. Copies of the guide
are already citing these IDs, so a freeze now costs little and helps them.

1. **The core held.** Where the principles reached this project, they found real faults, several before they happened
   and some only after I ignored them. Nothing here says a principle is wrong about prediction.
2. **The guide's frame is too narrow.** It assumes a claim is a prediction. This project's claims are about what a document
   says. Most of what didn't fit traces to that one thing, so one new principle, R12 below, does most of the repair.
3. **Five additions, seven changes, and the doctor's rows.** All have exact text or a named change below.
4. **Most of the guide remains untested.** Nothing here reached a trained model, a holdout, or production. Chapter 7 is almost
   wholly unproven. v1.0 has to say so: a tag isn't evidence.

**Wrong if** a course project finds that a principle needs to be removed or to mean something else, since an ID can't then be
reused. That is the risk of tagging now, and I think it's small, because a principle can still be reworded.

## What this rests on, and why to doubt it

- **The project.** One person preparing a decision on dozens of confidential cases about people, from thousands of pages of PDFs.
  Retrieval, extraction, and briefs written by a language model, with every quotation checked against its page. Nothing is
  trained, and nothing is predicted. That makes it close to the opposite of the guide's running example, which is why it's a
  useful test and a poor one for most of the book.
- **What I read.** All ten chapters, whole, plus `GAPS.md`, the opening of `CHANGELOG.md`, and the README's sections on change
  and trust. I ran `tools/check.js` (0 problems), `tools/test_dm.py` (OK), and `dm --doctor` on the project.
- **What I didn't read.** `CHECKLISTS.md`, `GLOSSARY.md`, the templates beyond the opening of `QUESTION_v1.md`, and each SE1 principle
  behind a *Reframes* line. So this doesn't test whether a reframing is faithful to its source.
- **Who's speaking.** A Claude model reviewing rules that Claude models drafted (SE1/U9), on a project it did itself. Several
  observations below are of my own mistakes, which helps with honesty and doesn't make me independent. No person and no
  other model family has reviewed this. One project, one owner, one model family: treat every "held" as one data point.
- **What's left out on purpose.** The project is confidential, so this file gives counts and kinds, never a case, a person, an
  institution, or any content from a document.

**Evidence labels.** *Observed*: it happened in the project. *Reasoned*: an argument from what the project is, not tested.

## The main finding: name the kind of claim

R2 says to fix "the unit, the outcome, and the prediction point", and R3 a metric and bar. Here the decision and the unit fit
at once. There is no outcome to score against and no moment of prediction, and writing them anyway would have meant inventing
fields, which the working agreement forbids. The same frame explains the rest:

- **The doctor:** of 23 rows, 8 said *none yet*, most of them shaped like a model (plan, holdout, ledger, model card). All true,
  with no way to say "this doesn't apply", so they read as work to do.
- **W7 and D6:** "regenerate the number from raw" doesn't reach prose written by a model. The working equivalent was a script that
  re-finds each quotation on its cited page.
- **R10:** "which groups matter" points at demographic slices, and here collecting those would itself be the harm. The bias
  that mattered was in how the evidence was read.
- **F5 and A4:** the holdout became questions a person writes and keeps off the machine.

`GAPS.md` item 4 expected this ("retrieval is probably thin"). It's thin, and the fix is a frame rather than a chapter.

## Five proposed principles

New IDs go at the end of each chapter, so nothing moves.

### R12. Name the kind of claim first: predicted, described, explained, or extracted

*New.*

Every principle in this guide was written with the first kind in mind, and not all of them bind the others. Say which kind of
claim the work makes before anything else, because that decides what you can score against.

| Kind | Example | Scored against | What stands in for the prediction point |
| --------- | ------------------------------------ | ------------------------------- | ------------------------------------ |
| Predicted | which lots fill tonight | an outcome that arrives later | the moment of prediction |
| Described | how occupancy varies across lots | a held-out period or sample | the period it describes |
| Explained | if we open lot C earlier, does the queue shrink | an experiment, or a stated causal design | the intervention (`GAPS.md`, item 1) |
| Extracted | what this document says about X | the document itself: a person can check the page | the date of the document, and the unit of citation |

An extracted claim has an unusual gift: each one can be checked against its source. And an unusual hazard: the check can't see
what was left out, which is the proposed F10. Where a principle doesn't apply to your kind of claim, say so and say why,
rather than filling in its template with something invented.

> **Ask:** "Which kind of claim is this, and what would it be checked against?"

### U10. "None found" is a claim about the search

*Reframes [SE1/T3](https://github.com/wmacevoy/software-engineering/blob/v1.3/guide/06-testing.md#t3).*

An absence is the cheapest K3 there is. It takes no evidence to report, and it looks like diligence. A search that could not
have found the thing returns the same answer as a search that found nothing.

So every "none" carries how it was looked for, and what it would have looked like if it were there. See the search find a planted
case first (DM1/T3). Say what was not searched. A "none found" in text means less on a page with no
text layer, so report absences by how the page was read (DM1/T9).

Before reporting that something is missing across many cases, open one by hand.

> **Ask:** "What would this search have returned if the thing were there, and have we seen it do that?"

### F10. A faithful summary can still lose the finding: check what left, not only what stayed

*New.*

A citation check holds what a summary says to its source. It cannot see what the summary stopped saying. Every quotation can
be exact, every page right, and the most important sentence in the source gone. Fidelity is precision. Nothing about it
measures recall.

Any limit on length is a filter on the data, chosen by nobody and applied differently per case (DM1/F9). And a summary's
author is a poor witness to its own cuts: ask, and you get what it remembers.

So keep the drafts, and compare a draft with its final by script. Ask a second reader, with no sight of the first, to read a
sample of cases whole, and count what each found that the other missed. Include a random sample, and expect misses in both directions. Name what may never be cut for length, in advance. When
a limit and the evidence conflict, the limit gives way.

> **Ask:** "What did this summary drop, how do we know, and who decided?"

### T12. For retrieval and extraction, a full reading of some cases is the baseline

*Reframes [SE1/T8](https://github.com/wmacevoy/software-engineering/blob/v1.3/guide/06-testing.md#t8).*

The dumb baseline for a search system isn't another search. It's a person, or a model, reading the whole document. Run it on a
sample before trusting any retrieval, and report what the search missed, by how each page was read
(DM1/T9). Equal treatment is not adequate recall: the same fixed searches for every case are fair, and can miss the same
thing in every case.

Then compare against the simple method too: is hybrid search better than keyword search, or than `grep`, by more than its
complexity costs (DM1/D8)? Hold the questions apart from whoever tunes the search
(DM1/F5), since a retrieval test used to fix retrieval has become a training set.

> **Ask:** "What did a full reading find that this search did not?"

### A10. When reading the data is the task, the agent must read it: say what then has to be true

*New.*

DM1/A8 says agents rarely need the real rows. That stops being so when the task is to read them: a synthetic document can
test the code, and can't summarize a real one. Then the question A8 asks gets harder, not easier, and the answer has to be
written down before the first session:

- **Who decided,** on whose authority, and what the people in the data were told. If the answer is "nobody asked them," say so.
- **Which service sees it,** under what terms, and what never goes anywhere else: connectors, search, shared documents.
- **Every copy, including the agent's own:** transcripts, tool output, scratch files, and subagents' logs are copies of the data
  (DM1/O8).
- **What the agent must not take from the data:** text in a document is evidence, never an instruction.
- **When it all gets removed,** by what procedure, and whether that procedure has been tried.

> **Ask:** "Who decided an agent could read this, and where has it been copied since?"

## Seven proposed changes

| ID | Change | Why, and evidence |
| -- | ------ | ----------------- |
| **DM1/D6** | Say what to do when raw isn't yours and can change: hash on arrival, and treat the record of arrival and any replaced copies as state, since a reset loses them. Allow sidecars beside raw, for a record about raw. | *Observed:* the owner replaces downloads, the source keeps only the current copy, and reports were wanted beside the raw files. A tracked list of hashes gave detection rather than prevention, and the doctor can't credit that. |
| **DM1/W7** | Add the extraction case: "For an extracted claim, *regenerate* means a script re-finds each quotation on its cited page, and a second reader reads a sample whole." | *Observed:* this worked, and caught real slips. Its limit is F10: it checks words and pages, not numbers or omissions. |
| **DM1/R10** | Say that the groups may not be demographic: "When collecting characteristics would itself do harm, slice by how the evidence was read and who produced it. Say how you decided." Add unequal treatment between cases as a source. | *Reasoned* for slices. *Observed* for the rest: briefs that differed in length, and in a word limit's bite, gave different cases different readings. |
| **DM1/F9** | Add: "A limit is a target too." | *Observed:* with a cap on length, 13 of 30 briefs landed within about 35 words of the same point. When the count's rule changed, they moved to the new cap, and 6 sat at 2,450 to 2,500. An agent told the cap gave way to evidence still stopped 2 words under it. |
| **DM1/O8** | Name the copies people forget: agent transcripts and tool output, and old versions inside a store. Add: "A scrub lasts only if it sits where the data is derived, or a rebuild brings it back. Run a check that shows it searched for something." | *Observed:* identifiers printed on old forms reached the text cache and the index. Deleted rows stayed in the store's old versions until those were purged. A first scan reported nothing because it had nothing to search for. |
| **DM1/U7** | Extend to documents: "For a document, the text layer is a summary of the page. Look at the page." | *Observed:* OCR garbled handwriting that turned out to matter. Text extraction collapsed a table's empty columns, so a figure landed in the wrong column. Shortening a command's output hid the ends of pages, and the owner caught that by asking. |
| **DM1/A9** | Keep it, and move retrieval and extraction out to T12 and F10. Add a sample of two independent reads as the prose form of "score several samples". | *Observed:* 10 cases were read twice, by readers who didn't see the first brief until theirs passed its check. The first two were early briefs. Then, with a bar fixed beforehand, 5 high-priority and 3 random: the first read had a decision-affecting miss in 5 of 5 and 2 of 3, on a definition readers called broad. Second reads missed as many as first reads or more. The reads agreed on the main facts, and none reversed a finding. Two reads by one model share any blind spot. |

Smaller wording, each one sentence: **DM1/F5** and **DM1/A4**, name "a person keeps it, on paper or elsewhere" as the plain answer to
what `GAPS.md` item 7 leaves open. **DM1/R2**, point to R12 for claims with no outcome. **DM1/O2**, say what stands in for CI on a
repository that may not have a remote. **DM1/R8**, name reading: tokens per document are a budget like compute, and each case here cost
roughly 250,000 to 500,000. **DM1/W5**, add a second pathology: when the deliverable is a summary, the pressure is to be concise, and
what it costs is omission.

## Every principle

**Held**: it reached this project and proved right. **Extend** or **Change**: as proposed above. **Reasoned**: it fits by argument,
untested. **Didn't reach**: nothing here tested it, which says nothing about whether it's right.

| ID | Verdict | What happened |
| -- | ------- | ------------- |
| P1 | Reasoned | The question narrowed, as it says, to one group first. |
| P2 | Reasoned | For extraction the gap is between a page and the world: a form can be wrong. |
| P3 | Held | The people in the data were not asked, and identifiers printed on their forms reached derived data. |
| P4 | Held | A passing citation check retired no fear about omission. The strongest case for the idea here. |
| P5 | Extend | See W7: prose can't be re-derived, only re-checked. |
| U1 | Held | Looking found what names hid: document layouts differed by source. |
| U2 | Held | A text tool silently returned nothing; a first check gave 32 confident false problems. |
| U3 | Didn't reach | No model. |
| U4 | Reasoned | "The rule source is current" and "a form says what happened" are K4s. |
| U5 | Reasoned | Reading cost is a box, not an estimate. |
| U6 | Held | Telling a writer to say "nothing in the file says why", or that handwriting wasn't legible, worked. |
| U7 | Extend | See above. |
| U8 | Didn't reach | No probability is ever given about a case. |
| U9 | Didn't reach | No outcome to keep out of view. |
| F1 | Reasoned | One-way doors here: a decision, and a citation that a reader relies on. |
| F2 | Held | A quotation checker made checking a brief cheap, and changed what got checked. |
| F3 | Held | The owner, reading, caught what no check did. |
| F4 | Reasoned | Searching a case for problems is a forking path. Fixed searches were the answer. |
| F5 | Extend | A person holds the questions. Not yet spent, so unproven. |
| F6 | Held | Logging reads caught 13 pages a brief hadn't read. |
| F7 | Didn't reach | No metric, though see A9 on repeated reads. |
| F8 | Reasoned | "Who's missing" became which evidence a case lacks. |
| F9 | Extend | See above. |
| R1 | Held | The decision was clear from the start, and it decided what a brief is for. |
| R2 | Change | Unit fit. Outcome and prediction point don't exist here: see R12. |
| R3 | Extend | No bar was set for retrieval, and that's a real gap. Open. |
| R4 | Didn't reach | No threshold. |
| R5 | Held | All four: absent, late (a source post-dating what it judged), wrong, and lying (a text layer). |
| R6 | Reasoned | Fits as written, for documents dated after what they judge. |
| R7 | Held | Scores in the documents are labels. And readers given one set of definitions applied them unevenly, with silence read as "false". |
| R8 | Extend | See above. |
| R9 | Held | Stopped on these at each step. |
| R10 | Change | See above. |
| R11 | Reasoned | A stated non-goal worked in every brief. |
| D1 | Held | Listing state showed how many stores held the same text. |
| D2 | Reasoned | The index is a cache of the corpus; not stressed. |
| D3 | Didn't reach | No training set. |
| D4 | Held | Re-indexing after a scrub put back exactly the rows removed. |
| D5 | Didn't reach | Dates only. |
| D6 | Change | See above. |
| D7 | Held | Pure logic gave fast tests throughout. |
| D8 | Held | It exposed a fault: hybrid search has never been shown to beat keyword search. Open. |
| D9 | Reasoned | One definition of each section and flag, in one procedure. |
| D10 | Didn't reach | No model card. Briefs name their model. |
| D11 | Didn't reach | No tracked metric. |
| D12 | Didn't reach | Nothing deployed. |
| D13 | Extend | A value's provenance needs "read by text, OCR, or eye", and it mattered. |
| T1 | Extend | The baseline hadn't been run. See T12. |
| T2 | Reasoned | Light use: counts checked at boundaries. |
| T3 | Extend | Instruments too: see U10, on a scan that searched for nothing. |
| T4 | Didn't reach | No metric. |
| T5 | Didn't reach | No tolerance exists for prose. Worth a thought. |
| T6 | Held | Tests on tidy fixtures passed, and real files then gave the 32 false problems. |
| T7 | Didn't reach | No golden output for prose. |
| T8 | Didn't reach | No model. |
| T9 | Reasoned | The useful slice is how a page was read. Not yet run. |
| T10 | Didn't reach | |
| T11 | Didn't reach | Nothing unsupervised. |
| O1 | Reasoned | Environment recorded; never tested by a difference. |
| O2 | Extend | Local only, so one script is the gate. |
| O3 | Didn't reach | Nothing in production. |
| O4 | Didn't reach | |
| O5 | Didn't reach | |
| O6 | Didn't reach | |
| O7 | Didn't reach | |
| O8 | Extend | See above. |
| O9 | Didn't reach | No model. See R10. |
| O10 | Held | Running on everything early found what a sample wouldn't have. |
| O11 | Didn't reach | Though the briefs could shape how others read the cases: nobody has looked. |
| W1 | Reasoned | The loop back to the question fits. |
| W2 | Reasoned | The expensive choices came early: the procedure and what a brief must hold. |
| W3 | Held | One brief, then two, then all: the first changed the method more than any later one. |
| W4 | Didn't reach | |
| W5 | Extend | See above: here the pathology was omission. |
| W6 | Held | Dead ends were recorded, and got reused. |
| W7 | Change | See above. |
| H1 | Held | The owner is the expert. Their questions caught what checks missed. |
| H2 | Reasoned | |
| H3 | Held | Bad news delivered early, including my own errors, cost less than it would have later. |
| H4 | Didn't reach | One person. |
| H5 | Reasoned | One label in a source was a color somebody chose. |
| H6 | Didn't reach | |
| H7 | Didn't reach | |
| H8 | Reasoned | |
| A1 | Held | Reading got cheap. Knowing what a reading missed didn't. |
| A2 | Held | A rule in the procedure was read and broken repeatedly. A script comparing drafts is what changed the work. |
| A3 | Held | Logged, fixed searches and read logs kept the count honest. |
| A4 | Extend | See F5. |
| A5 | Held | Tests and checkers were written by the agent, and mattered. |
| A6 | Extend | In extraction, K3 is in what was read and dropped: point review there. |
| A7 | Reasoned | The owner holds the decision and reads the source. |
| A8 | Change | See A10. |
| A9 | Change | See above. |

## What *Before you start* got wrong in practice

Reported here because it counts against me as much as the guide. I skipped the question, the plan, and the datasheets: the doctor
said *none yet*, the working agreement said to report that once, and I did. I now think that was a mistake for one of them. A
datasheet asking "what does a case file hold, how was each page made, and what might be printed on it?" would probably have
caught a misplaced document and the printed identifiers. *Reasoned*, since I didn't write one. So the datasheet row deserves
to survive R12 for every kind of claim, even where the plan and ledger rows give way.

## The doctor and the templates

| Thing | Change | Evidence |
| ----- | ------ | -------- |
| `dm --doctor`, every row | Add *not applicable*, with a required reason. Keyed by R12's kind of claim. | *Observed:* 8 of 23 rows. |
| `raw is read-only` | Let a project name what counts as raw, such as `inputs/*.zip`. | *Observed:* it fails on reports the owner asked for beside raw files. Left failing, knowingly. |
| `raw to report` | Tighten it. It passed on a command that makes reports about the files, and doesn't make the briefs, the project's main product. | *Observed:* a pass that hid something, which is what `GAPS.md` item 7 said to watch for. |
| `ledger` | Credit logs of reads and searches, which were the real ledger here. | *Observed:* it said *none yet* with those logs in place. |
| `citations`, and the agreement rows | Keep. They caught real slips. | *Observed.* |
| `QUESTION_v1` | Add the kind of claim; make outcome and prediction point conditional on it. | R12. |
| `DATASHEET` | Add a form for documents: how each page was made, which have no text layer, what identifiers may be printed. | See above. |
| `LEDGER` | Add reads and searches as looks. | F6. |

## What has to be true on the day of the tag

1. **Decide on merges now.** This is the one thing a freeze ends. I looked at P5/D6/W7/D13 (regenerate), D9/H4 (one definition), and
   U3/R6/D3 (leakage) and recommend keeping all of them. Each is at a different stage of the work, and the repetition is how
   a reader meets the idea from wherever they start. If you want a shorter book, this is the last chance.
2. **Stop saying nothing has been tested.** The header of `AGENTS.md`, README's *Why to trust this*, and `GAPS.md` all say no field report
   exists. Replace that with what was tested, and how little: the counts below.
3. **Say in the release what's unproven,** by chapter, in `CHANGELOG.md`. Chapter 7 above all.
4. **Links:** copies move from `main` to the dated release, which `tools/check.js` then requires.
5. **Bump the SE1 pin?** The project's vendored SE1 is v1.3.2 and the guide is pinned to v1.3. Decide, and walk the changes by ID if so.
6. **Retire `HANDOFF-migrate-to-SE1-v1.3.md`** to `archive/`, as step 7 of that note waited to do.

**Not blockers, though I'd want them soon:** a reader who hasn't read SE1 following the *Reframes* links (`GAPS.md` item 5), a review by a
person or by another model family, and the first predictive project through the course.

## Where that leaves it

Of 93 principles: **26 held, 14 to extend, 6 to change, 20 fit by argument only, and 27 didn't reach this project.** So 46 met
real work, and 47 didn't.

| Chapter | Held | Extend | Change | Reasoned | Didn't reach |
| ------- | ---- | ------ | ------ | -------- | ------------ |
| 1 Purpose | 2 | 1 | 0 | 2 | 0 |
| 2 Unknowing | 3 | 1 | 0 | 2 | 3 |
| 3 Feedback | 3 | 2 | 0 | 3 | 1 |
| 4 Requirements | 4 | 2 | 2 | 2 | 1 |
| 5 Design | 4 | 1 | 1 | 2 | 5 |
| 6 Testing | 1 | 2 | 0 | 2 | 6 |
| 7 Operating | 1 | 2 | 0 | 1 | 7 |
| 8 Work | 2 | 1 | 1 | 2 | 1 |
| 9 People | 2 | 0 | 0 | 3 | 3 |
| 10 Agents | 4 | 2 | 2 | 1 | 0 |

The verdicts are one model's judgment on one project, and no check stands behind them. "Held" means it reached this work and
looked right, and doesn't mean it was tried and survived a test built to break it.

## Retro

- **What I had to read that I shouldn't have needed:** my first report on this guide covered 22 principles, some cut off, because I
  was reading with a shortened command. Reading all of them changed what I recommend, and the fault was mine, not the guide's.
- **What I assumed because nobody wrote it down:** that a report going to a repository with a GitHub remote should name no institution. The owner
  should check that this is general enough, because the owner knows what the combination of details could reveal.
