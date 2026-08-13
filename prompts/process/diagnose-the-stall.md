# Diagnose the stall

Paste below the line after an automation or agent project stalled — or before you start, to see which trap you are walking into.

---

You are diagnosing why an agentic workflow stalled or will stall. Do not propose a new tool. Do not write code. One question at a time if you need facts I have not given.

The project (I will paste what we tried, or what we are about to try):

"""
<paste>
"""

Score each failure mode **yes / no / unclear**, with one line of evidence from what I said. These are the usual reasons this work dies:

1. **Started at the core.** We tried to automate the judgment, the craft, or the whole end-to-end job before we owned the edges (prep, check, package, handoff).
2. **A blob treated as one job.** “Email,” “status,” “the workflow,” “be my chief of staff” — several jobs with different checks, stuffed into one prompt.
3. **No check.** Success was “it sounds good” or the agent said `done`. Nothing a human could open and pass/fail.
4. **False success.** A finished-looking draft, matching filename, or confident summary hid a miss (wrong file, missing source, work that never hit the real system).
5. **Magic button.** The model picked the problem *and* built it. Frequency got treated as value. Choosing none was not allowed.
6. **Waiting for a better model.** The stall was blamed on intelligence. The missing piece was a named job, a source of truth, authority limits, or an owner.
7. **Nobody owns it.** Everyone can use it; no one is accountable when it drifts.
8. **It sends.** The first version was allowed to mail, file, pay, or close tickets. One bad action created a second problem.

Then:

- **The actual stall (one sentence).**
- **What to try instead:** one edge job, draft-only, with a check I can run this week.
- **What not to do next.**

If the project has not started yet, treat this as a pre-mortem on the plan I pasted.
