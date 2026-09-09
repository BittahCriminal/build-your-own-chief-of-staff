# Talk flow — 15 vs. 30 minutes

16 slides. The argument stays on slides. The files live on GitHub. After slide 9 you leave PowerPoint and open the repo; you only come back for the ranking card, Monday homework, and the close.

Both versions pivot on the same moment: slide 11, then a live run of `prompts/workflows/meeting-recap.md` copied from GitHub.

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

Pre-open four browser tabs. Slides 10–13 are portals with clickable GitHub URLs and a QR; use the tabs so you are not typing mid-talk.

1. [Repo README](https://github.com/BittahCriminal/build-your-own-chief-of-staff)
2. [`prompts/workflows/meeting-recap.md`](https://github.com/BittahCriminal/build-your-own-chief-of-staff/blob/main/prompts/workflows/meeting-recap.md)
3. [`PROCESS.md`](https://github.com/BittahCriminal/build-your-own-chief-of-staff/blob/main/PROCESS.md)
4. The tool you will demo in (Copilot, Cursor, Claude, ChatGPT, or Gemini), with a filled `voice.md` and one real meeting's title, date, attendees, and notes ready to paste

Also:

- Do a dry run once so you know roughly what the output looks like.
- Save that dry-run output as a fallback screenshot or a fifth tab.

## 30-minute run of show (16 slides)

| Segment | Where | Time | Beat |
| --- | --- | --- | --- |
| Why | Slides 1–9 | ~10 min | Not a vendor, two tests, freeze, why it fails, edges, CoS split. Flag meeting-recap. |
| **Open the kit** | **Slide 10 → GitHub README** | **~1 min** | **Click the URL. Point at the six names. Do not tour files.** |
| **Live demo** | **Slide 11 → `meeting-recap.md` → your tool** | **~4 min** | **Copy the prompt from GitHub. Paste voice.md + meeting details + real notes. Let the room watch the cited draft come back.** |
| **How** | **Slide 12 → `PROCESS.md`** | **~7 min** | **Walk steps 1–7 on that page, using the recap you just ran. Do not return to slides for each step.** |
| Rank | Slide 13 → `score-the-candidates.md` if needed | ~2 min | Decision matrix. Open the file only if someone has three ideas. |
| Close | Slides 14–16 | ~4 min | Monday homework (same recap, their meeting), safety card, URL + QR to `START-HERE.md` |

## 15-minute core path

This is a teaser, not the 30-minute talk compressed. Six slides, one GitHub file, one live run, one thing to do Monday. Everything else is skipped, not summarized.

| Where | Time | Beat |
| --- | --- | --- |
| Slide 1 | 1 min | Title. Process, not a vendor. |
| Slide 4 | 2 min | The two tests: repeatable, verifiable. |
| Slide 9 | 2 min | The CoS split. Flag meeting-recap as the file you are about to open. |
| **Slide 11 → `meeting-recap.md`** | **5 min** | **Live run. Narrate Inputs → Steps → Output → Check from the actual paste-in and result.** |
| Slide 14 | 2 min | The thirty-minute take-home: the same run, on their own meeting, Monday. |
| Slide 16 | 1 min | Close: URL and QR to `START-HERE.md`. |

Say three things out loud instead of showing them: drafts only, never send (slide 15); only put it on a timer after several hand-checked runs (`PROCESS.md` step 7); and the method is `PROCESS.md` if they want the seven steps. If someone leaves with three ideas instead of one, point them at [`prompts/process/score-the-candidates.md`](prompts/process/score-the-candidates.md); the decision matrix (slide 13) is not in this path.

## If the live demo doesn't cooperate

Have the dry-run output saved as a fallback screenshot or a second tab. If the model invents something not in the notes, don't panic — that's a live example of why Step 5 (verify, cite or cut) exists. Point at it and say so; it's a stronger teaching moment than a perfect run.

## After the talk

Point people at the [`README.md`](README.md) "Start here (30 minutes)" homework path — it calls out meeting-recap as the recommended first run, and [`prompts/process/score-the-candidates.md`](prompts/process/score-the-candidates.md) for anyone who leaves with three or more ideas instead of one.
