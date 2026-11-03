# Findings

What we learned the expensive way ([SE1/W10](https://github.com/wmacevoy/software-engineering/blob/v1.4/guide/08-work.md#w10)).
Blameless: say what would have found it, not who should have asked.

## 2026-11-03 — This guide cited SE1 and did not follow it, and no hook could run

- **What happened:** the owner noticed no hooks ran at session start. There was nothing to run: no
  `.claude/settings.json`, no `CLAUDE.md`, and no copy of SE1's agreement. The doctor passed *loads at every
  start* from the configuration, yet in the session that found this the root `AGENTS.md` was not in context:
  the agent had to open it. The doctor's *working agreement* and *data working agreement* rows had failed.
- **Kind:** K2 (surprise)
- **Cost:** sessions in this repository ran without SE1's rules in context, and without the self test.
- **Findable by:** running `./dm --doctor` in this repository, or the CI running it.
- **Changed:** the copies, `CLAUDE.md`, and the hook. Whether CI should run the doctor on this repository
  changed nothing yet: most of its rows are *none yet* on a guide.

## 2026-11-03 — The check command needs Node, which this machine does not have

- **What happened:** `node tools/check.js` failed with `command not found` when the migration began. It
  was run with a Node 24 left in another session's temporary directory, which will not last.
- **Kind:** K2 (surprise)
- **Cost:** a check that a contributor here cannot run without installing something first; SE1 removed the
  same need at v1.4.
- **Findable by:** a fresh checkout on a machine with only Python.
- **Changed:** CONTRIBUTING names the prerequisite, and queue #3 asks whether to port it.
