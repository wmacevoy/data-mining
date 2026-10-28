#!/usr/bin/env python3
"""Tests for dm.py: every row of the data doctor is seen to fail on a fixture built to fail it (DM1/T3,
SE1/T3), and a fixture built to pass passes every row. Run: python3 -I tools/test_dm.py. Standard
library only; no network, no wall clock, no shared state: every fixture is a fresh git repository in a
temporary directory. SE1's own rows are se.py's to test; here they are only seen to run when se.py is
found (SE_GUIDE, .se1/, or ../software-engineering/)."""
import importlib.util
import json
import os
import stat
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

GUIDE = Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location("dm", GUIDE / "dm.py")
dm = importlib.util.module_from_spec(spec)
spec.loader.exec_module(dm)

DM_AGENTS = (GUIDE / "AGENTS.md").read_text(encoding="utf8")
SE_AGENTS = ("# AGENTS.md\n\nA working agreement. The IDs are defined in the guide at "
             "https://github.com/wmacevoy/software-engineering/tree/v1.3; This copy is from **v1.3**.\n")

GOOD = {
    "AGENTS.md": SE_AGENTS,
    "AGENTS-DM.md": DM_AGENTS,
    "CLAUDE.md": "# Project\n\n@AGENTS.md\n@AGENTS-DM.md\n",
    "CONTRIBUTING.md": (
        "# Contributing\n\n## Run it\n\n"
        "- **Raw to report:** `make report` — every reported number, about four minutes\n"
        "- **Fetch / refresh raw data:** `make fetch`\n\n## Check it\n\n"
        "- **The full check:** `python -m unittest` — the same one CI runs\n- **Success prints:** `OK`\n\n"
        "## Data rules for this repository\n\n"
        "- **Raw data:** lives in `data/raw`, read-only; never hand-edited.\n"
        "- **The holdout:** lives in `../holdout/`; Ann may read it; spent only at a decision.\n"),
    "docs/QUESTION_v1.md": (
        "# Question — v1\n\nClient: Ann · Date sent: 2026-10-20\n\n## The decision\n\n- **Decision:** open lot C early or not\n\n"
        "## Bias\n\n- **Groups that matter:** students and staff — the client\n"
        "- **BIAS-1** *(since v1)* Error rate per group, gap at most 5 points; Ann chose it.\n\n"
        "## Definitions\n\n- **UNIT-1** *(since v1)* One row is: one lot on one event night.\n"
        "- **OUT-1** *(since v1)* The outcome: lot full by 18:40 local.\n"
        "- **PRED-1** *(since v1)* The prediction point: 17:00 local on the event day.\n\n"
        "## The bar\n\n- **BAR-1** *(since v1)* MAE minutes on the 2026 holdout, at most 15, against same-as-last-event at 19.2, with the interval.\n\n"
        "## Not for\n\n- lots off campus — no data\n"),
    "docs/PLAN_v1.md": (
        "# Analysis plan — v1\n\nQuestion: `QUESTION_v1` · Written: 2026-10-21 · Outcome examined yet? _no_\n\n"
        "## Split\n\n- **Grouping:** rows sharing an event stay on one side.\n"
        "- **Holdout:** `../holdout/` — kept by Ann outside the repository; spent once, at the final decision.\n\n"
        "## Metric and baseline\n\n- **Primary metric:** MAE minutes\n"
        "- **Baseline:** same as last comparable event — scored on 2026-10-21: MAE 19.2\n- **Interval:** bootstrap\n\n"
        "## Slices\n\n| Slice | Why it matters | Expected *n* |\n| ----- | -------------- | ------------ |\n| small lots | pooled toward the big ones | 40 |\n\n"
        "## Departures\n"),
    "docs/datasheets/gate.md": (
        "# Datasheet — gate scans\n\n## Origin\n\n- **Source:** the gate system\n"
        "- **This sheet:** written by Ann on 2026-10-21; measured. **What would show it wrong:** the row-count assertion in `src/load.py`\n\n"
        "## Columns\n\n| Column | Meaning | Units / clock | Sentinels and defaults | Knowable at | Absent / late / wrong / lying |\n"
        "| ------ | ------- | ------------- | ---------------------- | ----------- | ----------------------------- |\n"
        "| ts | scan time | UTC | none | ts + 5 min upload lag | dropped when offline |\n"
        "| lot | lot id | — | none | ts | — |\n"),
    "docs/ledger.jsonl": (
        json.dumps({"when": "2026-10-22T18:00Z", "tried": "baseline", "split": "validation", "holdout": False}) + "\n"
        + json.dumps({"when": "2026-10-25T18:00Z", "tried": "gbm 3", "split": "holdout", "holdout": True, "why": "final choice"}) + "\n"),
    "docs/model_cards/lot_fill.md": (
        "# Model card — lot fill, v1\n\n## Identity\n\n"
        "- **Data version:** raw@2026-10-20 · **Code commit:** abc123 · **Seed(s):** 1, 2, 3 · **Environment:** pixi.lock\n"
        "- **Owner:** Ann · **Next check that it is still true:** 2026-12-01\n"
        "- **This card:** written by Ann on 2026-10-25 · **What would retire it:** MAE above 15 on any slice\n\n"
        "## Bias audit\n\n| Group | *n* | Measure (interval) | Calibration | Gap vs. `Q1/BIAS-1` |\n"
        "| ----- | --- | ------------------ | ----------- | ------------------- |\n| students | 400 | 12 (10–14) | ok | 2 |\n"),
    "src/score.py": "LEDGER = 'docs/ledger.jsonl'\n",
    "data/raw/a.csv": "ts,lot\n2026-10-01T00:00Z,C\n",
    "pixi.lock": "version: 6\n",
    "tests/test_pipeline.py": "# Q1/OUT-1 and Q1/BAR-1 are asserted here\n",
    ".gitignore": "data/holdout/\n",
    ".github/workflows/check.yml": "on: push\njobs:\n  check:\n    steps:\n      - run: python -m unittest\n",
}
READ_ONLY = ("data/raw/a.csv",)


def git(repo, *args):
    return subprocess.run(["git", "-c", "user.name=t", "-c", "user.email=t@t", *args], cwd=repo,
                          capture_output=True, text=True, check=True).stdout


def make_repo(tmp, files=GOOD, read_only=READ_ONLY):
    repo = Path(tmp)
    for rel, text in files.items():
        p = repo / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        with open(p, "w", encoding="utf8", newline="\n") as fh:  # Path.write_text(newline=) is 3.10+; this runs on 3.9
            fh.write(text)
    git(repo, "init", "-q")
    git(repo, "add", "-A")
    git(repo, "commit", "-q", "-m", "chore: start")
    for rel in read_only:
        if (repo / rel).exists():
            os.chmod(repo / rel, stat.S_IRUSR | stat.S_IRGRP | stat.S_IROTH)
    return repo


def finding(findings, name):
    return next(f for f in findings if f.name == name)


class Fixture(unittest.TestCase):
    """A fresh repository per test; only DM1's rows, so a missing se.py cannot fail these."""

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()

    def tearDown(self):
        for p in Path(self.tmp.name).rglob("*"):  # a read-only file would block cleanup on Windows
            if p.is_file():
                os.chmod(p, stat.S_IRUSR | stat.S_IWUSR)
        self.tmp.cleanup()

    def doctor(self, files=GOOD, read_only=READ_ONLY):
        repo = make_repo(self.tmp.name, files, read_only)
        return dm.doctor(repo, online=False, se=None)

    def changed(self, **edits):
        files = dict(GOOD)
        for k, v in edits.items():
            if v is None:
                files.pop(k, None)
            else:
                files[k] = v
        return files


DM_ROWS = ("data working agreement", "question", "plan", "holdout", "datasheets", "raw is read-only",
           "raw to report", "ledger", "model card", "environment", "question citations")


class TestGood(Fixture):
    def test_good_project_passes_every_dm_row(self):
        f = self.doctor()
        states = {x.name: x.state for x in f}
        self.assertEqual(states["SE1 doctor"], dm.NONE)  # no se.py handed in: said, not hidden
        for name in DM_ROWS:
            self.assertEqual(states[name], dm.PASS, f"{name}: {finding(f, name).text}")

    def test_guide_itself_is_not_a_project(self):
        f = dm.dm_rows(GUIDE)
        self.assertEqual(finding(f, "question").state, dm.NONE)
        self.assertEqual(finding(f, "datasheets").state, dm.NONE)


class TestAgreements(Fixture):
    def test_no_dm_copy(self):
        f = self.doctor(self.changed(**{"AGENTS-DM.md": None, "CLAUDE.md": "@AGENTS.md\n"}))
        self.assertEqual(finding(f, "data working agreement").state, dm.FAIL)
        self.assertIn("no copy", finding(f, "data working agreement").text)

    def test_no_se_copy(self):
        f = self.doctor(self.changed(**{"AGENTS.md": None, "CLAUDE.md": "@AGENTS-DM.md\n"}))
        self.assertEqual(finding(f, "data working agreement").state, dm.FAIL)
        self.assertIn("SE1 AGENTS.md", finding(f, "data working agreement").text)

    def test_unlabeled_dm_copy(self):
        f = self.doctor(self.changed(**{"AGENTS-DM.md": DM_AGENTS.replace("**v1.0**", "v1.0")}))
        self.assertEqual(finding(f, "data working agreement").state, dm.FAIL)
        self.assertIn("no release label", finding(f, "data working agreement").text)

    def test_claude_md_imports_only_one(self):
        f = self.doctor(self.changed(**{"CLAUDE.md": "@AGENTS.md\n"}))
        self.assertEqual(finding(f, "data working agreement").state, dm.FAIL)
        self.assertIn("does not import AGENTS-DM.md", finding(f, "data working agreement").text)

    def test_no_claude_md_loads_only_the_root_file(self):
        f = self.doctor(self.changed(**{"CLAUDE.md": None}))
        self.assertEqual(finding(f, "data working agreement").state, dm.FAIL)
        self.assertIn("nothing loads", finding(f, "data working agreement").text)


class TestQuestionAndPlan(Fixture):
    def test_no_question(self):
        f = self.doctor(self.changed(**{"docs/QUESTION_v1.md": None, "tests/test_pipeline.py": "# nothing\n",
                                        "docs/model_cards/lot_fill.md": GOOD["docs/model_cards/lot_fill.md"].replace("`Q1/BIAS-1`", "the bias measure")}))
        self.assertEqual(finding(f, "question").state, dm.NONE)
        self.assertEqual(finding(f, "question citations").state, dm.NONE)

    def test_question_missing_a_one_way_door(self):
        q = GOOD["docs/QUESTION_v1.md"].replace("- **PRED-1** *(since v1)* The prediction point: 17:00 local on the event day.\n", "")
        f = self.doctor(self.changed(**{"docs/QUESTION_v1.md": q}))
        self.assertEqual(finding(f, "question").state, dm.FAIL)
        self.assertIn("PRED", finding(f, "question").text)

    def test_question_with_the_templates_placeholder(self):
        q = GOOD["docs/QUESTION_v1.md"].replace("One row is: one lot on one event night.", "One row is: _…_")
        f = self.doctor(self.changed(**{"docs/QUESTION_v1.md": q}))
        self.assertEqual(finding(f, "question").state, dm.FAIL)
        self.assertIn("placeholder", finding(f, "question").text)

    def test_question_without_a_bar(self):
        q = GOOD["docs/QUESTION_v1.md"].replace("**BAR-1** *(since v1)*", "**BAR-1**")
        f = self.doctor(self.changed(**{"docs/QUESTION_v1.md": q, "tests/test_pipeline.py": "# Q1/OUT-1\n"}))
        self.assertEqual(finding(f, "question").state, dm.FAIL)
        self.assertIn("bar", finding(f, "question").text)

    def test_question_without_not_for(self):
        q = GOOD["docs/QUESTION_v1.md"].replace("## Not for", "## Later")
        f = self.doctor(self.changed(**{"docs/QUESTION_v1.md": q}))
        self.assertEqual(finding(f, "question").state, dm.WARN)

    def test_no_plan_with_a_question(self):
        f = self.doctor(self.changed(**{"docs/PLAN_v1.md": None}))
        self.assertEqual(finding(f, "plan").state, dm.WARN)

    def test_plan_holdout_placeholder(self):
        p = GOOD["docs/PLAN_v1.md"].replace("`../holdout/` — kept by Ann outside the repository; spent once, at the final decision.",
                                            "where it is kept, who may read it, and when it will be spent: _…_")
        f = self.doctor(self.changed(**{"docs/PLAN_v1.md": p}))
        self.assertEqual(finding(f, "plan").state, dm.FAIL)
        self.assertIn("holdout", finding(f, "plan").text)

    def test_plan_without_slices_or_a_scored_baseline(self):
        p = GOOD["docs/PLAN_v1.md"].replace("| small lots | pooled toward the big ones | 40 |\n", "").replace("scored on 2026-10-21: MAE 19.2", "scored on _yyyy-mm-dd_: _…_")
        f = self.doctor(self.changed(**{"docs/PLAN_v1.md": p}))
        self.assertEqual(finding(f, "plan").state, dm.WARN)
        self.assertIn("slices", finding(f, "plan").text)
        self.assertIn("baseline", finding(f, "plan").text)


class TestHoldout(Fixture):
    def inside(self, text):
        return self.changed(**{"docs/PLAN_v1.md": GOOD["docs/PLAN_v1.md"].replace("`../holdout/`", "`data/holdout/`"),
                               "CONTRIBUTING.md": GOOD["CONTRIBUTING.md"].replace("`../holdout/`", "`data/holdout/`"), **text})

    def test_absent_and_ignored_is_out_of_reach(self):
        f = self.doctor(self.inside({}))
        self.assertEqual(finding(f, "holdout").state, dm.PASS)
        self.assertIn("git-ignored", finding(f, "holdout").text)

    def test_present_and_readable_is_in_reach(self):
        repo = make_repo(self.tmp.name, self.inside({}))
        (repo / "data" / "holdout").mkdir()
        (repo / "data" / "holdout" / "x.csv").write_text("a\n")
        f = dm.dm_rows(repo)
        self.assertEqual(finding(f, "holdout").state, dm.FAIL)
        self.assertIn("readable", finding(f, "holdout").text)

    def test_tracked_file_named_holdout(self):
        f = self.doctor(self.changed(**{"data/holdout.csv": "a\n"}))
        self.assertEqual(finding(f, "holdout").state, dm.FAIL)
        self.assertIn("tracked", finding(f, "holdout").text)

    def test_named_without_a_path(self):
        p = GOOD["docs/PLAN_v1.md"].replace("`../holdout/` — kept by Ann", "kept by Ann")
        c = GOOD["CONTRIBUTING.md"].replace("lives in `../holdout/`", "Ann has it")
        f = self.doctor(self.changed(**{"docs/PLAN_v1.md": p, "CONTRIBUTING.md": c}))
        self.assertEqual(finding(f, "holdout").state, dm.WARN)


class TestDataAndPipeline(Fixture):
    def test_no_datasheet(self):
        f = self.doctor(self.changed(**{"docs/datasheets/gate.md": None}))
        self.assertEqual(finding(f, "datasheets").state, dm.NONE)

    def test_datasheet_column_without_knowable_at(self):
        d = GOOD["docs/datasheets/gate.md"].replace("| lot | lot id | — | none | ts | — |", "| lot | lot id | — | none |  | — |")
        f = self.doctor(self.changed(**{"docs/datasheets/gate.md": d}))
        self.assertEqual(finding(f, "datasheets").state, dm.FAIL)
        self.assertIn("lot", finding(f, "datasheets").text)

    def test_datasheet_with_the_templates_placeholder(self):
        d = GOOD["docs/datasheets/gate.md"].replace("| ts | scan time | UTC | none | ts + 5 min upload lag |", "| ts | scan time | UTC | none | _ts + upload lag (up to …)_ |")
        f = self.doctor(self.changed(**{"docs/datasheets/gate.md": d}))
        self.assertEqual(finding(f, "datasheets").state, dm.FAIL)

    def test_datasheet_nobody_signed(self):
        d = GOOD["docs/datasheets/gate.md"].replace("- **This sheet:**", "- **Sheet:**")
        f = self.doctor(self.changed(**{"docs/datasheets/gate.md": d}))
        self.assertEqual(finding(f, "datasheets").state, dm.WARN)

    def test_raw_writable(self):
        f = self.doctor(read_only=())
        self.assertEqual(finding(f, "raw is read-only").state, dm.FAIL)
        self.assertIn("writable", finding(f, "raw is read-only").text)

    def test_raw_absent(self):
        f = self.doctor(self.changed(**{"data/raw/a.csv": None}))
        self.assertEqual(finding(f, "raw is read-only").state, dm.NONE)

    def test_raw_to_report_placeholder(self):
        c = GOOD["CONTRIBUTING.md"].replace("`make report`", "`_command_`")
        f = self.doctor(self.changed(**{"CONTRIBUTING.md": c}))
        self.assertEqual(finding(f, "raw to report").state, dm.FAIL)

    def test_raw_to_report_missing(self):
        c = GOOD["CONTRIBUTING.md"].replace("- **Raw to report:** `make report` — every reported number, about four minutes\n", "")
        f = self.doctor(self.changed(**{"CONTRIBUTING.md": c}))
        self.assertEqual(finding(f, "raw to report").state, dm.NONE)


class TestLedgerCardEnvironment(Fixture):
    def test_no_ledger(self):
        f = self.doctor(self.changed(**{"docs/ledger.jsonl": None}))
        self.assertEqual(finding(f, "ledger").state, dm.NONE)

    def test_ledger_nobody_writes(self):
        f = self.doctor(self.changed(**{"src/score.py": "x = 1\n"}))
        self.assertEqual(finding(f, "ledger").state, dm.WARN)
        self.assertIn("from memory", finding(f, "ledger").text)

    def test_ledger_counts_holdout_spends(self):
        f = self.doctor()
        self.assertIn("2 rows, holdout spent 1 time", finding(f, "ledger").text)

    def test_markdown_ledger_ignores_the_templates_example_row(self):
        md = "# Ledger\n\n| When (UTC) | What was tried | Split | Holdout? why |\n| - | - | - | - |\n| _2026-10-27T18:02Z_ | _baseline_ | _validation_ | _no_ |\n"
        f = self.doctor(self.changed(**{"docs/ledger.jsonl": None, "docs/LEDGER.md": md}))
        self.assertEqual(finding(f, "ledger").state, dm.NONE)
        self.assertIn("empty", finding(f, "ledger").text)

    def test_model_card_identity_placeholder(self):
        c = GOOD["docs/model_cards/lot_fill.md"].replace("**Seed(s):** 1, 2, 3", "**Seed(s):** _…_")
        f = self.doctor(self.changed(**{"docs/model_cards/lot_fill.md": c}))
        self.assertEqual(finding(f, "model card").state, dm.FAIL)
        self.assertIn("Seed", finding(f, "model card").text)

    def test_model_card_bias_audit_empty_while_groups_named(self):
        c = GOOD["docs/model_cards/lot_fill.md"].replace("| students | 400 | 12 (10–14) | ok | 2 |\n", "")
        f = self.doctor(self.changed(**{"docs/model_cards/lot_fill.md": c}))
        self.assertEqual(finding(f, "model card").state, dm.FAIL)
        self.assertIn("bias audit empty", finding(f, "model card").text)

    def test_model_card_nobody_signed(self):
        c = GOOD["docs/model_cards/lot_fill.md"].replace("- **This card:**", "- **Card:**")
        f = self.doctor(self.changed(**{"docs/model_cards/lot_fill.md": c}))
        self.assertEqual(finding(f, "model card").state, dm.WARN)

    def test_no_environment_file(self):
        f = self.doctor(self.changed(**{"pixi.lock": None}))
        self.assertEqual(finding(f, "environment").state, dm.NONE)

    def test_untracked_lock_is_the_known_gap(self):
        f = self.doctor(self.changed(**{"pixi.lock": None, ".gitignore": "data/holdout/\npixi.lock\n"}))
        Path(self.tmp.name, "pixi.lock").write_text("version: 6\n")
        f = dm.dm_rows(self.tmp.name)
        self.assertEqual(finding(f, "environment").state, dm.WARN)
        self.assertIn("not tracked", finding(f, "environment").text)


class TestCitations(Fixture):
    def test_bare_citation(self):
        f = self.doctor(self.changed(**{"tests/test_pipeline.py": "# OUT-1 is asserted here\n"}))
        self.assertEqual(finding(f, "question citations").state, dm.FAIL)
        self.assertIn("unversioned", finding(f, "question citations").text)

    def test_stale_citation_after_the_definition_moved(self):
        q2 = GOOD["docs/QUESTION_v1.md"].replace("# Question — v1", "# Question — v2").replace("**OUT-1** *(since v1)*", "**OUT-1** *(since v2)*")
        f = self.doctor(self.changed(**{"docs/QUESTION_v2.md": q2}))
        self.assertEqual(finding(f, "question citations").state, dm.FAIL)
        self.assertIn("stale", finding(f, "question citations").text)


class TestWithSe(unittest.TestCase):
    def test_se_rows_run_when_se_py_is_found(self):
        se, path = dm.find_se(GUIDE)
        if se is None:
            self.skipTest("se.py not found (set SE_GUIDE); SE1's rows not exercised here")
        with tempfile.TemporaryDirectory() as tmp, tempfile.TemporaryDirectory() as cache:
            repo = make_repo(tmp, GOOD, ())
            f = dm.doctor(repo, online=False, cache_dir=cache, se=se)
            names = [x.name for x in f]
            self.assertIn("working set", names)   # SE1's
            self.assertIn("question", names)      # DM1's
            self.assertNotIn("SE1 doctor", names)


if __name__ == "__main__":
    unittest.main(verbosity=1)
