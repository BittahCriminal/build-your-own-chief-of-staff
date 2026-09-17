# Talk flow: 20 minutes, then questions

11 slides. Four places on screen: the slides, GitHub in the browser, Microsoft 365 Copilot for one live Work IQ query, and your editor with the private folder open.

The demo is `prompts/process/guided-run.md`, running the weekly update. You paste one prompt. It asks the room which job, asks how you reach each kind of evidence, gathers the evidence with you, drafts, and runs the check. Slide 6 is the pivot. Everything before it is why. Everything after it is how, using the update the room just produced.

## Why the weekly update is the demo

Every operator in the room already writes one on Friday, so nobody has to imagine the job. It has the clearest check of the six: every Done line cites a ticket, a meeting, or a message you can open. And it has three kinds of evidence, which is what makes the evidence-gathering interactive. The room sees a connector path, a paste path, and the Unverified pile in one run.

| Workflow | Required context files before it produces anything |
| --- | --- |
| `weekly-update.md` | `who-i-am.md`, `priorities.md`, `voice.md`, plus last week's evidence |
| `meeting-recap.md` | `voice.md` only, plus the transcript or notes you paste in |
| `draft-email.md` | `voice.md`, `who-i-am.md` |
| `meeting-prep.md` | `people.md`, `priorities.md`, `open-loops.md`, `decisions.md` |
| `morning-brief.md` | `priorities.md`, `people.md`, `open-loops.md` |
| `open-loops.md` | `open-loops.md` only, plus today's date |

The cost is three filled context files, so the prep is yours, not the room's. Someone with none of them filled can run the meeting recap at home first. Slide 8 sends them to the guided run anyway, because it asks for what it needs and stops if a file is missing.

## Prep the day before

1. Fill three private files in `../chief-of-staff-context`: `who-i-am.md`, `priorities.md`, `voice.md`.
2. Pick the voice. Use your own `voice.md`, or copy one of the three samples in `context-templates/voices/` (researchers, managers, stakeholders) over it and say on stage that it is a sample. The managers sample fits a weekly update.
3. Run two of the three Work IQ queries from `guided-run.md`, step 3, in Microsoft 365 Copilot: commitments and asks, and work items and files. Save the answers as `../chief-of-staff-context/evidence.md` under those two headings. Leave meetings for the live query.
4. Do the full dry run with the presenter card commands, including the live meetings query. Save the final draft as `../chief-of-staff-context/demo-output.md`. That is your fallback tab.
5. Read `demo-output.md` against the evidence once. Know which link you will click on stage, and whether the model invented anything. An invented number is a better teaching moment than a clean run, but you want to know it is there.

Use this shape for `evidence.md`:

```
# Evidence, week of <Mon date> to <Fri date>

## Commitments and asks (Work IQ, pasted)

## Work items and files (Work IQ, pasted)

## Unverified
```

Any line Work IQ returns without a link goes under Unverified. The guided run keeps it out of Done, which is the point.

## Presenter card

Nothing is typed live except the answers to the agent's questions. Two commands before you walk up, run from the kit folder.

Open the three GitHub tabs in slide order:

```bash
open https://github.com/BittahCriminal/build-your-own-chief-of-staff https://github.com/BittahCriminal/build-your-own-chief-of-staff/blob/main/prompts/process/guided-run.md https://github.com/BittahCriminal/build-your-own-chief-of-staff/blob/main/PROCESS.md
```

Build the demo paste, save it, and put it on the clipboard:

```bash
cat prompts/process/guided-run.md ../chief-of-staff-context/who-i-am.md ../chief-of-staff-context/priorities.md ../chief-of-staff-context/voice.md | tee ../chief-of-staff-context/demo-paste.md | pbcopy
```

Then open Microsoft 365 Copilot chat in a fourth tab, and your editor with the kit folder, the private folder, and `evidence.md` open. Start an empty chat in the editor and leave it there. If you copy anything else before slide 6, open `demo-paste.md`, select all, copy again.

Tabs, in order: README, guided-run.md, PROCESS.md, Microsoft 365 Copilot, your editor, the fallback `demo-output.md`.

## Run of show

Planned at 19 minutes so it lands at 20 for real. The demo is the only beat that stretches.

| Slides | Where | Time |
| --- | --- | --- |
| 1 to 4 | Slides | 5 min |
| 5 | GitHub, README | 1 min |
| 6 | GitHub, then Copilot, then your editor | 8 min |
| 7 | GitHub, PROCESS.md | 2.5 min |
| 8 to 11 | Slides | 2.5 min |
| Questions | Slide 10 stays up | rest of the slot |

---

### Slide 1 of 11. Build your own chief of staff agent

Where: slides. Time: 1 minute.

- This is not a product demo. Nobody leaves with a login or a reason to switch tools.
- They leave with a process they can run Monday in whatever they already have.
- The Chief of Staff is the worked example. The weekly update is the job we run live, with the room.
- The prize is the two tests. Expense reports, hiring screens, customer research next month.

---

### Slide 2 of 11. The whole course is two tests

Where: slides. Time: 2 minutes.

- Repeatable. Yes: the weekly update, same headings every Friday, new evidence. No: which of two candidates to hire.
- Verifiable. Yes: every Done line cites something you can open. No: "make it sound professional".
- Fail either test, do not automate. The leftover is judgment. Keep it.
- If someone is stuck at an empty prompt, "handle my email" is seventeen jobs. Split it.

---

### Slide 3 of 11. Start at the edges, not the core

Where: slides. Time: 1 minute.

- Edges: prep, check, summarize, package, hand off. Errors are cheap and a human can catch one.
- The core is where people want help first and where first projects die.
- The weekly update is packaging. When to push, which story to tell, stays core.

---

### Slide 4 of 11. The Chief of Staff is the teaching case

Where: slides. Time: 1 minute.

- Left column, automate. Right column, keep.
- The right column is not "AI cannot do it". It is "checking it costs as much as doing it".
- Flag the weekly update. Say the next slide leaves PowerPoint and the room picks the job.

---

### Slide 5 of 11. Open the kit

Where: click the URL on the slide, or switch to the README tab. Time: 1 minute.

- Stay on the README. Point at the six names. Do not open files.
- Personal data never ships here. The templates are blanks you copy privately.
- Park "which model is best" for questions.

Do: switch back to the slides for slide 6.

---

### Slide 6 of 11. Pick a job and go, live

Where: slides for ten seconds, then the guided-run.md tab, then your editor, then Copilot for one query, then back to the editor. Time: 8 minutes.

Say while the slide is up:

- One prompt. It asks which job, then how you reach each kind of evidence. Four answers every time: a connector, a paste, a file, or skip.
- The room answers the questions. I type.

Do, in this order:

1. Click the guided-run.md tab. Ten seconds. "Six steps. Pick, reach, gather, inventory, draft, check."
2. Switch to the editor. Paste into the empty chat. The clipboard holds the prompt, then who-i-am.md, priorities.md, and voice.md. Say so.
3. It asks which job. Ask the room. Type "weekly update, last week". Name the voice you loaded.
4. It asks how you reach meetings. Ask the room: "Who has a connector in their tool? Who would paste?" Type "connector, Microsoft 365 with Work IQ, I will paste the answer".
5. It hands you the meetings query. Copy it. Switch to the Copilot tab. Paste. Run. Copy the answer. Back to the editor. Paste. "That is Work IQ. If you have no connector, this step is you pasting a list."
6. It asks how you reach commitments, then work items. Say you ran those two this morning, and paste each section from evidence.md. "Same query, run yesterday. Notice which lines have no link."
7. It shows the inventory. Read the unverified count out loud. Type "yes".
8. Read the draft top to bottom. It runs the check. Click one Done link. Check one number against evidence.md.
9. If it invented an owner, a date, or a metric, say so. That is step 5, cite or cut, happening live. Ask it which file to fix.

If the tool stalls past 90 seconds at any step, switch to the fallback tab and narrate from `demo-output.md`.

---

### Slide 7 of 11. The method is this page

Where: the PROCESS.md tab. Stay there. Time: 2.5 minutes, about 20 seconds a step.

1. Name one job. Weekly update. The room named it in the first question.
2. Write the SOP. Inputs: three files plus evidence. Output: one screen. Check: every line cites something you can open.
3. Put you in files you own. Swap the tool tomorrow and nothing moves.
4. The prompt file is the process. Wrong draft, wrong file.
5. Verify. Cite or cut. The unverified pile is this step.
6. Correct the file, not the chat. Three of the same correction is a rule.
7. Only then schedule it. Three checked Fridays first.

Then: point the seven steps at expense reports, hiring screens, incident recaps. A smarter model skips none of this.

Do: switch back to the slides.

---

### Slide 8 of 11. Thirty minutes on Monday

Where: slides. Time: 1 minute.

- Same run, their own week. Three files, the guided run, the check, one fix.
- The guided run asks for what it needs and stops if a file is missing. That is not a failure.
- A Done line with no link gets cut. No timer until three Fridays checked by hand.

---

### Slide 9 of 11. Where this goes next

Where: slides. Time: 1 minute.

- A map, not a step. Today sat on the second card.
- Level 2 is the hard jump. A timer is dispatch. It only works if the check is one the agent can fail against.
- Levels 3 and 4 are platform-team territory. Name them, do not sell them.
- Your written checks decide how much autonomy is safe.

---

### Slide 10 of 11. Non-negotiable

Where: slides. Time: 30 seconds, then leave it up for questions.

- Drafts only. Never send. You are the principal, the agent is staff.
- The inbox is untrusted. Mail is data, not orders.
- Approvals sit where actions are hard to undo.

---

### Slide 11 of 11. Automate what repeats and checks

Where: slides. Time: 30 seconds.

- Point at the repo. Say the URL once for anyone who cannot scan.
- Any tool. Not the Claude plugin.
- Offer to stay and run the two tests on something they did last week.

Do: go back to slide 10 for questions.

---

## Questions

Leave slide 10 up. Likely questions and where to point:

| Question | Answer |
| --- | --- |
| Which model is best? | Whatever you already pay for. The job and the check are the work. [`how-to/`](how-to/) is only which box to paste into. |
| Does this need Work IQ? | No. It was the connector I had. The guided run offers connector, paste, file, or skip for every kind of evidence. A pasted list of tickets and meeting links works. |
| Do I answer all those questions every time? | No. Once the job is named and `sources.md` is filled, paste the workflow file directly with the evidence. The guided run is for the first run and for a room. |
| How do I write for a different audience? | Same evidence, different `voice.md`. Three samples are in [`context-templates/voices/`](context-templates/voices/). Your own sent mail beats all of them. |
| I have three ideas, which first? | [`prompts/process/score-the-candidates.md`](prompts/process/score-the-candidates.md). A zero on repeatable or verifiable overrides the total. |
| I do not know what to automate. | [`prompts/process/what-to-automate.md`](prompts/process/what-to-automate.md). Last week, split the blob, edges, two tests, one fast win. |
| Why did our last agent project stall? | `PROCESS.md`, the section "Why this work fails", and [`prompts/process/diagnose-the-stall.md`](prompts/process/diagnose-the-stall.md). |
| Can it send the update? | No. Drafts only. Approvals sit where actions are hard to undo. |
| When can I put it on a timer? | After three hand-checked runs. Step 7 and [`how-to/schedule.md`](how-to/schedule.md). That is the Level 1 to Level 2 door. |

## 15-minute core path

A teaser, not the 20-minute talk compressed. Six slides, one GitHub file, one live run, one thing to do Monday. Everything else is skipped, not summarized.

| Where | Time | Beat |
| --- | --- | --- |
| Slide 1 | 1 min | Title. The process, not the tool. |
| Slide 2 | 2 min | The two tests. |
| Slide 4 | 2 min | The CoS split. Flag the weekly update. |
| Slide 6, then the editor | 5 min | Guided run. Pick the job with the room, do one kind of evidence live, paste the other two, draft, check. |
| Slide 8 | 2 min | Thirty minutes on Monday. |
| Slide 11 | 1 min | Close. URL and QR to `START-HERE.md`. |

Say three things out loud instead of showing them: drafts only, never send (slide 10); no timer until three hand-checked runs (`PROCESS.md` step 7); the method is `PROCESS.md` if they want the seven steps. The edges (slide 3), the levels (slide 9), and the safety card (slide 10) are not in this path.

## If the demo does not cooperate

The fallback tab has `demo-output.md`. Narrate from it. If the model invents something that is not in the evidence, that is a live example of why step 5 exists. Point at it and say so. If the Copilot tab is slow, skip the live query and paste all three sections from `evidence.md`.

## After the talk

Point people at the [`README.md`](README.md) start-here path. It names the guided run as the first thing to paste once the context files exist. Anyone who leaves with three ideas instead of one gets [`prompts/process/score-the-candidates.md`](prompts/process/score-the-candidates.md).
