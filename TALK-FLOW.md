# Talk flow — 20 minutes, then questions

11 slides. The argument stays on slides. The files live on GitHub. After slide 4 you leave PowerPoint and open the repo; you only come back for Monday homework, the levels ladder, the safety card, and the close.

Both versions pivot on the same moment: slide 6, then a live run of `prompts/workflows/meeting-recap.md` copied from GitHub.

## Why meeting-recap is the demo

Of the six Chief of Staff jobs in the kit, `prompts/workflows/meeting-recap.md` has the lowest setup cost:

| Workflow | Required context files before it produces anything |
| --- | --- |
| `meeting-recap.md` | `voice.md` only, plus the transcript/notes you paste in |
| `draft-email.md` | `voice.md`, `who-i-am.md` |
| `weekly-update.md` | `who-i-am.md`, `priorities.md`, `voice.md` |
| `meeting-prep.md` | `people.md`, `priorities.md`, `open-loops.md`, `decisions.md` |
| `morning-brief.md` | `priorities.md`, `people.md`, `open-loops.md` |
| `open-loops.md` | `open-loops.md` only, plus today's date |

Running `morning-brief.md` live risks an empty or generic-looking output if the room hasn't filled in three context files first. `meeting-recap.md` only needs one context file (`voice.md`, which you fill in before the talk), the meeting title/date/attendees, and one real, current transcript or notes dump — something you can prep in five minutes and swap for a fresh one on the day.

It is also the cleanest demonstration of "verifiable": every decision, owner, and date in the output has to trace back to a specific line you can point at in the source notes. If the model invents an owner, the audience catches it instantly, which is a better teaching moment than a clean run.

## Prep before you present

Pre-open four browser tabs. Slides 5–7 are portals with clickable GitHub URLs and a QR; use the tabs so you are not typing mid-talk.

1. [Repo README](https://github.com/BittahCriminal/build-your-own-chief-of-staff)
2. [`prompts/workflows/meeting-recap.md`](https://github.com/BittahCriminal/build-your-own-chief-of-staff/blob/main/prompts/workflows/meeting-recap.md)
3. [`PROCESS.md`](https://github.com/BittahCriminal/build-your-own-chief-of-staff/blob/main/PROCESS.md)
4. The tool you will demo in (Copilot, Cursor, Claude, ChatGPT, or Gemini), with a filled `voice.md` and one real meeting's title, date, attendees, and notes ready to paste

Also:

- Do a dry run once so you know roughly what the output looks like.
- Save that dry-run output as a fallback screenshot or a fifth tab.

## 20-minute run of show, then questions (11 slides)

Planned at 18.5 minutes so it lands at 20 for real. The demo is the only beat that stretches; everything else is one or two lines per slide.

| Segment | Where | Time | Beat |
| --- | --- | --- | --- |
| Why | Slides 1–4 | ~6 min | Title (process, not a vendor). The two tests. Edges, not the core. The CoS split. Flag meeting-recap. |
| **Open the kit** | **Slide 5 → GitHub README** | **~1 min** | **Click the URL. Point at the six names. Do not tour files.** |
| **Live demo** | **Slide 6 → `meeting-recap.md` → your tool** | **~6 min** | **Copy the prompt from GitHub. Paste voice.md + meeting details + real notes. Let the room watch the cited draft come back.** |
| **How** | **Slide 7 → `PROCESS.md`** | **~3 min** | **Walk steps 1–7 on that page, about 25 seconds each, using the recap you just ran.** |
| Close | Slides 8–11 | ~2.5 min | Monday homework, the five levels (this kit is Level 1), safety card, URL + QR to `START-HERE.md`. |
| Questions | Slide 10 stays up | rest of slot | See below. |

Cut from the earlier 30-minute deck: walk-away-with, not-a-vendor, fail-either-test, the freeze, why-it-fails, and the ranking card. The freeze and why-it-fails sections are still in `PROCESS.md`; point at them during the walk if the room needs them. The ranking card is [`prompts/process/score-the-candidates.md`](prompts/process/score-the-candidates.md); open it only if someone asks.

## Questions

Leave the safety card (slide 10) up. Likely questions and where to point:

| Question | Answer |
| --- | --- |
| Which model is best? | Whatever you already pay for. The job and the check are the work. [`how-to/`](how-to/) is only which box to paste into. |
| I have three ideas, which first? | [`prompts/process/score-the-candidates.md`](prompts/process/score-the-candidates.md). Zero on repeatable or verifiable overrides the total. |
| I do not know what to automate. | [`prompts/process/what-to-automate.md`](prompts/process/what-to-automate.md): last week, split the blob, edges, two tests, one fast win. |
| Why did our last agent project stall? | `PROCESS.md`, "Why this work fails" and [`prompts/process/diagnose-the-stall.md`](prompts/process/diagnose-the-stall.md). |
| Can it send the email? | No. Drafts only. Approvals sit where actions are hard to undo. |
| When can I put it on a timer? | After three hand-checked runs. Step 7 and [`how-to/schedule.md`](how-to/schedule.md). That is the Level 1 to Level 2 door. |

## 15-minute core path

This is a teaser, not the 20-minute talk compressed. Six slides, one GitHub file, one live run, one thing to do Monday. Everything else is skipped, not summarized.

| Where | Time | Beat |
| --- | --- | --- |
| Slide 1 | 1 min | Title. Process, not a vendor. |
| Slide 2 | 2 min | The two tests: repeatable, verifiable. |
| Slide 4 | 2 min | The CoS split. Flag meeting-recap as the file you are about to open. |
| **Slide 6 → `meeting-recap.md`** | **5 min** | **Live run. Narrate Inputs → Steps → Output → Check from the actual paste-in and result.** |
| Slide 8 | 2 min | The thirty-minute take-home: the same run, on their own meeting, Monday. |
| Slide 11 | 1 min | Close: URL and QR to `START-HERE.md`. |

Say three things out loud instead of showing them: drafts only, never send (slide 10); only put it on a timer after several hand-checked runs (`PROCESS.md` step 7); and the method is `PROCESS.md` if they want the seven steps. If someone leaves with three ideas instead of one, point them at [`prompts/process/score-the-candidates.md`](prompts/process/score-the-candidates.md); the edges (slide 3), the levels ladder (slide 9), and the safety card (slide 10) are not in this path.

## If the live demo doesn't cooperate

Have the dry-run output saved as a fallback screenshot or a second tab. If the model invents something not in the notes, don't panic — that's a live example of why Step 5 (verify, cite or cut) exists. Point at it and say so; it's a stronger teaching moment than a perfect run.

## After the talk

Point people at the [`README.md`](README.md) "Start here (30 minutes)" homework path — it calls out meeting-recap as the recommended first run, and [`prompts/process/score-the-candidates.md`](prompts/process/score-the-candidates.md) for anyone who leaves with three or more ideas instead of one.
