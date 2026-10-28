# Ledger

Every configuration scored, appended **by the code that scored it**, never from memory. The count of
lines is part of every result reported from this project
([DM1/F6](https://github.com/wmacevoy/data-mining/blob/main/guide/03-feedback.md#f6),
[DM1/A3](https://github.com/wmacevoy/data-mining/blob/main/guide/10-agents.md#a3)).
Keep it as a machine-written file (`ledger.jsonl` or `ledger.csv`) beside this description; a
Markdown table is fine for a small project.

A holdout row is a spending event: say what decision it served
([DM1/F5](https://github.com/wmacevoy/data-mining/blob/main/guide/03-feedback.md#f5)).

| When (UTC) | Who / agent | Question | What was tried | Split | Seed | Data version | Commit | Metric(s) | Holdout? why |
| ---------- | ----------- | -------- | -------------- | ----- | ---- | ------------ | ------ | --------- | ------------ |
| _2026-10-27T18:02Z_ | _name_ | _Q1/BAR-1_ | _baseline: same as last comparable event_ | _validation_ | _—_ | _raw@…_ | _abc123_ | _MAE 19.2 min_ | _no_ |

Report a result as, for example: *"best of 23 configurations on validation; holdout spent once, on
2026-11-10, to choose between the final two."*
