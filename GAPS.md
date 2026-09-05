# Gaps

Known holes in the kit. Noted 2026-09-05 after `f6de67a`. Each one names the file, what is missing, and the smallest fix. Close them or delete the row; do not let this become a backlog.

| # | File | Gap | Smallest fix |
| --- | --- | --- | --- |
| 1 | `prompts/process/score-the-candidates.md` | Verdicts cover 8–10 (build now) and 5–7 (build next). A candidate with no zero on Repeatable or Verifiable can still total 2–4 and gets no verdict. | Add a **Not yet** verdict for 2–4: passes both tests, but too rare, too risky, or too unspecified to be worth the setup. Revisit when frequency or spec readiness changes. |
| 2 | `README.md` | Repo map does not list `TALK-FLOW.md`. Presenters will not find the 15/30-minute run of show from the front page. | One line in the repo map: `TALK-FLOW.md — run of show for the talk (15 and 30 min)`. |
| 3 | `research/SOURCES.md` | No row for the decision matrix. `PROCESS.md` cites [shape of the work](https://app.notion.com/p/36f059b703e181cf9c30f637d158b234) for it, but `AGENTS.md` says method changes get a row in SOURCES. | Extend the existing "Shape of the work" row: what we took now includes the five-axis score; what we left is the executive capital-allocation matrix. |
