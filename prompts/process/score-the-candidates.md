# Score the candidates (the decision matrix)

Use this when you have **three or more** candidate jobs — from [`name-the-job.md`](name-the-job.md) or the split-the-blob step in [`what-to-automate.md`](what-to-automate.md) — and need to pick which one to build first, not just whether to build. If you only have one candidate, use [`the-two-tests.md`](the-two-tests.md) instead; this file is for ranking, not filtering.

Method note: this matrix operationalizes the frequency, mistake-cost, and judgment-load classification cited in [`research/SOURCES.md`](../../research/SOURCES.md#what-we-took-from-which-rows). The two tests remain hard gates; the score does not automate the human choice.

Paste everything below the line. Bring your candidate list, or be interviewed for it.

---

You are helping me rank multiple candidate jobs so I build the right sub-agent first. Do not build anything yet. Do not write a prompt file yet. Do not pick the winner for me by vibe — score it.

If I have not listed my candidates, interview me one at a time: what are the 3–6 jobs I am considering handing to an agent? Get a name and a finished-artifact shape for each before scoring.

For each candidate, score five axes, 0–2, using only what I tell you. Do not guess my week and do not round up to be encouraging.

1. **Repeatable** — 0: special case every time. 1: mostly the same steps. 2: identical steps and shape every time.
2. **Verifiable** — 0: no check I can name. 1: a soft check ("does this look right"). 2: a hard check against a named source, template, or yes/no rule.
3. **Frequency** — 0: rare (less than monthly). 1: weekly. 2: daily or near-daily.
4. **Blast radius if wrong** — 0: it sends, pays, publishes, or deletes on its own. 1: drafts only, but a bad draft could slip past me before I catch it. 2: drafts only, low stakes, easy for me to catch before anything leaves my hands.
5. **Spec readiness** — 0: the inputs are not named in `sources.md` or any context file yet. 1: some inputs are named. 2: every input already has a named source I can point at today.

Then, non-negotiable:

- **A zero on Repeatable or Verifiable overrides everything else.** That candidate is judgment, not an agent, no matter how high the rest of the score is. Do not let a high total talk me out of this.
- Total the other three axes plus Repeatable and Verifiable for candidates that scored at least 1 on both, out of 10.
- Sort high to low.

Verdict per candidate:

- **Build now** — 8–10, no zero on Repeatable or Verifiable.
- **Build next** — 5–7, no zero on Repeatable or Verifiable.
- **Split further** — the score swings wildly depending on which sub-part I'm thinking of; it's a blob, not one job.
- **Keep as judgment** — zero on Repeatable or Verifiable, regardless of total.

Finish with this block, nothing else:

```
Candidates scored:
| Job | Repeatable | Verifiable | Frequency | Blast radius | Spec ready | Total | Verdict |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ... | | | | | | | |

Build now: <the single highest-scoring "Build now" candidate, or "none scored high enough">
Why this one, not the others: <one sentence, tied to the scores, not a vibe>
Everything else: <one line each — build next / split further / keep as judgment>
Next step: [write-the-sop.md](write-the-sop.md) for the winner
```

If two candidates tie, prefer the one with the higher Frequency score — it pays back the setup cost sooner. If I disagree with a score, ask me for the specific evidence that changes it; do not just move the number because I pushed back.
