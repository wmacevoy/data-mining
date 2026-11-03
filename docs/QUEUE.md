# Queue

The shared cursor ([SE1/W10](https://github.com/wmacevoy/software-engineering/blob/v1.4/guide/08-work.md#w10)).
Only a human marks an item done.

| # | Item | Versioned requirement IDs (or *chore*) | Owner | Done when | Estimate (number / range / time box) | Status | Since |
| - | ---- | ---------------------------- | ----- | --------- | ------------------------------------ | ------ | ----- |
| 1 | Confirm or correct the reconstructed mission, shape, requirements, and non-goals | REQ1/MISSION-1, REQ1/SHAPE-1, REQ1/SHAPE-2 | Warren MacEvoy | the *(inferred)* marks are gone or say why they stay, and verdicts are recorded | time box: 30 minutes | ready | 2026-11-03 |
| 2 | Phrase test and hook, in a fresh session | chore | Warren MacEvoy | a fresh session quotes a line of each agreement without opening a file, and shows `se --post`'s report | 5 minutes | ready | 2026-11-03 |
| 3 | Decide: port `tools/check.js` to Python, as SE1 did at v1.4 | REQ1/CHK-1 | Warren MacEvoy | decided; if yes, the port ran beside the JavaScript with identical output before replacing it | range: 2 to 4 hours | blocked: on the owner's decision | 2026-11-03 |
| 4 | `dm --doctor` reads *(judged)* in a question and reports its verdict | REQ1/DOC-1 | unassigned | a question with `DECISION-1` and no verdict reads as waiting on a fixture, seen red first | range: 1 to 2 hours | ready | 2026-11-03 |
| 5 | Name requirements in tests for the checker | REQ1/CHK-1, REQ1/PIN-1, REQ1/AGR-1 | unassigned | the doctor's trace row has no untested requirement | blocked with #3 | blocked: on #3 | 2026-11-03 |
