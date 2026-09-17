# Talk flow: 20 minutes, then questions

11 slides. Three places on screen during the talk: the slides, GitHub in the browser, and your editor with the private folder open. Microsoft 365 Copilot is a fourth tab for pulling evidence with Work IQ. You use it before the talk, not during.

The demo is `prompts/workflows/weekly-update.md`. Slide 6 is the pivot. Everything before it is why. Everything after it is how, using the update you just produced.

## Why the weekly update is the demo

Every operator in the room already writes one on Friday, so nobody has to imagine the job. It has the clearest check of the six: every Done line cites a ticket, a meeting, or a message you can open. And it shows the context files doing work, because the same evidence reads differently to a manager, a researcher, and a stakeholder.

| Workflow | Required context files before it produces anything |
| --- | --- |
| `weekly-update.md` | `who-i-am.md`, `priorities.md`, `voice.md`, plus last week's evidence |
| `meeting-recap.md` | `voice.md` only, plus the transcript or notes you paste in |
| `draft-email.md` | `voice.md`, `who-i-am.md` |
| `meeting-prep.md` | `people.md`, `priorities.md`, `open-loops.md`, `decisions.md` |
| `morning-brief.md` | `priorities.md`, `people.md`, `open-loops.md` |
| `open-loops.md` | `open-loops.md` only, plus today's date |

The cost is three filled context files, so the prep is yours, not the room's. If someone in the room has none of them filled, the meeting recap is the cheaper first run at home. Slide 8 sends them to the weekly update anyway because they just watched it.

## Prep the day before

1. Fill three private files in `../chief-of-staff-context`: `who-i-am.md`, `priorities.md`, `voice.md`.
2. Pick the voice for the demo. Use your own `voice.md`, or copy one of the three samples in `context-templates/voices/` (researchers, managers, stakeholders) over it and say on stage that it is a sample. The managers sample is the natural fit for a weekly update.
3. Pull last week's evidence with the three Work IQ prompts below. Save the answers as `../chief-of-staff-context/evidence.md`.
4. Do the dry run with the presenter card commands. Save the output as `../chief-of-staff-context/demo-output.md`. That is your fallback tab.
5. Read `demo-output.md` against the evidence once. Know which line you will click on stage, and whether the model invented anything. An invented number is a better teaching moment than a clean run, but you want to know it is there.

## Work IQ prompts

Paste each one into Microsoft 365 Copilot chat on its own. Replace the two dates. Paste each answer under its heading in `evidence.md`.

Prompt 1, meetings:

```
From my calendar and meeting notes between Monday <date> and Friday <date>, list every meeting I attended. For each one give the date, the title, the decisions recorded, and the action items assigned to me. Include a link to the meeting or its recap. If a meeting has no notes or recap, write "no notes" instead of summarizing the invite.
```

Prompt 2, commitments and asks:

```
From my sent mail and my Teams messages between Monday <date> and Friday <date>, list every commitment I made (something I said I would do or deliver) and every ask I made of someone else. For each one give the date, who it was to, what it was, the deadline if I named one, and a link to the message. Leave out messages I only received.
```

Prompt 3, work items and files:

```
From work items assigned to me and files I edited in SharePoint or OneDrive between Monday <date> and Friday <date>, list each item with its state (todo, in progress, blocked, or done), the date it last changed, and a link. Mark anything that reached done this week.
```

Use this shape for `evidence.md`. The date range in the first line is the date range the prompt asks for.

```
# Evidence, week of <Mon date> to <Fri date>

## Meetings (Work IQ, prompt 1)

## Commitments and asks (Work IQ, prompt 2)

## Work items and files (Work IQ, prompt 3)

## Unverified
```

Any line Work IQ returns without a link goes under Unverified. The weekly-update prompt will leave it out of Done, which is the point.

## Presenter card

Nothing is typed live. Two commands before you walk up, run from the kit folder.

Open the three GitHub tabs in slide order:

```bash
open https://github.com/BittahCriminal/build-your-own-chief-of-staff https://github.com/BittahCriminal/build-your-own-chief-of-staff/blob/main/prompts/workflows/weekly-update.md https://github.com/BittahCriminal/build-your-own-chief-of-staff/blob/main/PROCESS.md
```

Build the demo paste, save it, and put it on the clipboard:

```bash
cat prompts/workflows/weekly-update.md ../chief-of-staff-context/who-i-am.md ../chief-of-staff-context/priorities.md ../chief-of-staff-context/voice.md ../chief-of-staff-context/evidence.md | tee ../chief-of-staff-context/demo-paste.md | pbcopy
```

Then open your editor with the kit folder and the private folder, start an empty chat, and leave it there. If you copy anything else before slide 6, open `demo-paste.md`, select all, copy again.

Tabs, in order: README, weekly-update.md, PROCESS.md, your editor, the fallback `demo-output.md`.

## Run of show

Planned at 18.5 minutes so it lands at 20 for real. The demo is the only beat that stretches.

| Slides | Where | Time |
| --- | --- | --- |
| 1 to 4 | Slides | 6 min |
| 5 | GitHub, README | 1 min |
| 6 | GitHub, then your editor | 6 min |
| 7 | GitHub, PROCESS.md | 3 min |
| 8 to 11 | Slides | 2.5 min |
| Questions | Slide 10 stays up | rest of the slot |

---

### Slide 1 of 11. Build your own chief of staff agent

Where: slides. Time: 1 minute.

- This is not a product demo. Nobody leaves with a login or a reason to switch tools.
- They leave with a process they can run Monday in whatever they already have.
- The Chief of Staff is the worked example. The weekly update is the file we run live.
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

Where: slides. Time: 90 seconds.

- Edges: prep, check, summarize, package, hand off. Errors are cheap and a human can catch one.
- The core is where people want help first and where first projects die.
- The weekly update is packaging. When to push, which story to tell, stays core.

---

### Slide 4 of 11. The Chief of Staff is the teaching case

Where: slides. Time: 90 seconds.

- Left column, automate. Right column, keep.
- The right column is not "AI cannot do it". It is "checking it costs as much as doing it".
- Flag the weekly update. Say the next slide leaves PowerPoint.

---

### Slide 5 of 11. Open the kit

Where: click the URL on the slide, or switch to the README tab. Time: 1 minute.

- Stay on the README. Point at the six names. Do not open files.
- Personal data never ships here. The templates are blanks you copy privately.
- Park "which model is best" for questions.

Do: switch back to the slides for slide 6.

---

### Slide 6 of 11. Weekly update, live

Where: slides for ten seconds, then the weekly-update.md tab, then your editor. Time: 6 minutes.

Say while the slide is up:

- Three context files and last week's evidence. The evidence came from Work IQ, one prompt each for meetings, sent mail, and work items.
- Every Done line has to cite something you can open. That is the check.

Do, in this order:

1. Click the weekly-update.md tab. Ten seconds. "This is the whole prompt. Inputs, steps, output, check."
2. Switch to the editor. Paste into the empty chat. The clipboard holds the prompt, then who-i-am.md, priorities.md, voice.md, and evidence.md, in that order. Say the order out loud.
3. Run it. While it runs, say which voice you used and that the same evidence would read differently to a researcher or a stakeholder. The samples are in context-templates/voices/.
4. Read the draft out loud, top to bottom. Click one Done link. Check one number against evidence.md.
5. If the model invented an owner, a date, or a metric, say so. That is step 5, cite or cut, happening live.

If the tool stalls past 90 seconds, switch to the fallback tab and narrate from `demo-output.md`.

---

### Slide 7 of 11. The method is this page

Where: the PROCESS.md tab. Stay there. Time: 3 minutes, about 25 seconds a step.

1. Name one job. Weekly update. Named before the demo, which is why it moved fast.
2. Write the SOP. Inputs: three files plus evidence. Output: one screen. Check: every line cites something you can open.
3. Put you in files you own. Swap the tool tomorrow and nothing moves.
4. The prompt file is the process. Wrong draft, wrong file.
5. Verify. Cite or cut. Gaps stay gaps.
6. Correct the file, not the chat. Three of the same correction is a rule.
7. Only then schedule it. Three checked Fridays first.

Then: point the seven steps at expense reports, hiring screens, incident recaps. A smarter model skips none of this.

Do: switch back to the slides.

---

### Slide 8 of 11. Thirty minutes on Monday

Where: slides. Time: 90 seconds.

- Same run, their own week. Three files, the evidence, the prompt, the check, one fix.
- A Done line with no link gets cut. That is the agent working.
- No timer until three Fridays checked by hand.

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
| Does this need Work IQ? | No. Work IQ was the fastest way to pull my evidence. A pasted list of tickets and meeting links works. `sources.md` is where you name your systems. |
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
| Slide 6, then the editor | 5 min | Live run. Narrate inputs, steps, output, check from the actual paste and result. |
| Slide 8 | 2 min | Thirty minutes on Monday. |
| Slide 11 | 1 min | Close. URL and QR to `START-HERE.md`. |

Say three things out loud instead of showing them: drafts only, never send (slide 10); no timer until three hand-checked runs (`PROCESS.md` step 7); the method is `PROCESS.md` if they want the seven steps. The edges (slide 3), the levels (slide 9), and the safety card (slide 10) are not in this path.

## If the demo does not cooperate

The fallback tab has `demo-output.md`. Narrate from it. If the model invents something that is not in the evidence, that is a live example of why step 5 exists. Point at it and say so.

## After the talk

Point people at the [`README.md`](README.md) start-here path. It names the meeting recap as the cheapest first run for someone with no context files filled, and the weekly update for anyone who watched this talk. Anyone who leaves with three ideas instead of one gets [`prompts/process/score-the-candidates.md`](prompts/process/score-the-candidates.md).
