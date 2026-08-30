# Talk flow — 15 vs. 30 minutes

26 slides total. The deck is built to run at 30 minutes with all slides, or 15 minutes on a marked core path. Both versions pivot on the same moment: slide 14, the live meeting-recap demo.

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

1. Fill in a real `voice.md` (or a plausible sample one, sanitized) ahead of time.
2. Have one real meeting's title, date, attendee list, and notes or transcript ready to paste — sanitize names/numbers if needed, but keep it realistic enough that the recap looks like real work, not a toy example.
3. Have `prompts/workflows/meeting-recap.md` open in a tab, ready to paste into whatever tool you're demoing in.
4. Do a dry run once beforehand so you know roughly what the output looks like and aren't debugging a prompt live.

## 30-minute run of show (all 26 slides)

| Segment | Slides | Time | Beat |
| --- | --- | --- | --- |
| Why | 1–10 | ~9 min | Not a vendor talk, the two tests, why people freeze, why projects fail, edges vs. core |
| Setup | 11–13 | ~3 min | CoS is the teaching case (flag meeting-recap), same markdown/any tool, what's in the kit |
| **Live demo** | **14** | **~3–4 min** | **Paste voice.md + meeting details + real notes into meeting-recap.md live. Let the room watch the cited draft come back.** |
| How | 15–21 | ~9 min | Steps 1–7, using the demo you just ran as the running example on each slide |
| Generalize | 22–23 | ~3 min | Decision matrix for ranking multiple candidate jobs, then "point the same process at anything" |
| Close | 24–26 | ~3 min | Thirty-minute homework path, non-negotiable safety rules, close |

## 15-minute core path

Cut to these 16 slides; skip the rest or mention them only if asked:

1, 4, 7, 8, 10, 11, **14 (live demo)**, 15, 17, 18, 19, 20, 22 (decision matrix), 23, 25, 26

What this drops: the "not a vendor talk" contrast slide (3), the repeatable/verifiable example slides (5, 6), why-it-fails detail (9), the tool-agnostic grid (12), the kit map (13), step 2's SOP breakdown (16), step 7's scheduling slide (21 — mention it verbally as "and only then schedule it" instead), and the 30-minute homework breakdown (24, mention verbally).

Narrate the live demo (slide 14) a little longer in the 15-minute version — since you're skipping the SOP-anatomy slide (16), use the demo itself to show Inputs → Steps → Output → Check by walking the actual paste-in and result instead of the card slide.

## If the live demo doesn't cooperate

Have the dry-run output saved as a fallback screenshot or a second tab. If the model invents something not in the notes, don't panic — that's a live example of why Step 5 (verify, cite or cut) exists. Point at it and say so; it's a stronger teaching moment than a perfect run.

## After the talk

Point people at the [`README.md`](README.md) "Start here (30 minutes)" homework path — it calls out meeting-recap as the recommended first run, and [`prompts/process/score-the-candidates.md`](prompts/process/score-the-candidates.md) for anyone who leaves with three or more ideas instead of one.
