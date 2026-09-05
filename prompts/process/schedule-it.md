# Schedule a verified workflow

Use only after the workflow has passed `verify.md` at least three times by hand. Paste below the line. Attach the workflow prompt file (e.g. `morning-brief.md`) and your private context files (`priorities.md`, `people.md`, `voice.md`).

---

You are packaging a verified Chief of Staff workflow into an automated schedule wrapper for my AI tool. Do not assume I have verified this job. Do not invent tools.

## Step 1: The Three-Pass Gate

First ask: **"Have you run this workflow manually and verified the output with `verify.md` at least three times?"**

- If I say **No**: STOP. Do not generate the wrapper. Explain that scheduling an uninspected prompt automates errors, hides hallucinations, and bypasses the verification gate. Tell me to complete three manual runs with `verify.md` first and return.
- If I say **Yes**: proceed to Step 2.

## Step 2: Gather Schedule Details

Ask me:
1. **Which tool?** (ChatGPT, Gemini, M365 Copilot, Claude Code / Desktop, Cursor, or other)
2. **Cadence and timezone?** 12-hour clock with AM/PM and a named timezone (e.g., "Every weekday at 7:30 AM <your timezone>", "Every Friday at 3:00 PM <your timezone>"). If I give 24-hour time or no timezone, convert and confirm.
3. **Where does the output land?** (e.g., thread, an inbox note, a file to review)
4. **Who owns this agent?** (One accountable person close enough to notice drift)
5. **How will you turn it off or pause it?** (Where in the tool to disable the schedule)
6. **Review date?** (Default to 90 days from today or end of quarter: YYYY-MM-DD)

## Step 3: Trim and Inline Context

In-app schedulers copy prompt text when the task is created; they cannot dynamically read local folders from disk at runtime. The wrapper must inline context directly into the prompt. But inlined context goes stale when priorities or teams change.

Extract **only** the active, relevant lines needed for this specific workflow:
- For `morning-brief.md`: active goals from `priorities.md`, stakeholders needing fast replies from `people.md`, and open-loop stale rules from `open-loops.md`.
- For `weekly-update.md`: audience from `who-i-am.md`, active priorities from `priorities.md`, and voice rules/banned phrases from `voice.md`.
- For other workflows: only the strictly required context rows. Do not dump whole files.

## Step 4: Build the Schedule Wrapper

Replace every placeholder with a real value. The finished wrapper must contain no `<…>` and no `YYYY-MM-DD`. If you do not have a value, ask me; do not leave a blank or guess. The snapshot date is today's date — if you do not know today's date, ask me.

Generate the wrapper using this exact shape:

```
<TOOL-SPECIFIC SCHEDULE TRIGGER LINE>
Confirm the schedule back to me before saving.
If you cannot schedule in this tool, say so. Do not pretend it is set.
Output is a draft. Do not send, file, close, or change anything.

---
[CONTEXT SNAPSHOT — TAKEN YYYY-MM-DD — REVIEW BY: <REVIEW-DATE>]
Mandatory run instruction:
State at the very top of your output:
"Running on context snapshotted YYYY-MM-DD. Valid until <REVIEW-DATE>."
If today is after <REVIEW-DATE>, prepend this warning:
"[CONTEXT STALE]: This scheduled prompt has passed its review date (<REVIEW-DATE>). Update priorities and re-verify before relying on this output."
---

<PASTE WORKFLOW PROMPT BODY HERE, e.g. from morning-brief.md>

---
[INLINED CONTEXT FOR THIS WORKFLOW]
<TRIMMED CONTEXT EXTRACTS>
```

### Tool-specific first line syntax:
- **ChatGPT**: `<When + timezone>, run the following.` (e.g. `Every weekday at 7:30 AM <your timezone>, run the following.`)
- **Gemini**: `<When + timezone>, run the following.` (e.g. `Every weekday at 7:30 AM <your timezone>, run the following.`)
- **M365 Copilot (Work tab)**: `<When + timezone>, run the following.` (Note: If in Teams/Outlook/Agents chat, run the prompt once without the schedule prefix, hover, click **Schedule this prompt**, and clear the default 2-week end date.)
- **Claude Code**: `/schedule <cadence description>` (e.g. `/schedule daily morning brief at 7:30am <your timezone>`) followed by the prompt body. (Note: Claude Desktop uses the sidebar UI; claude.ai web chat has no scheduler.)
- **Cursor**: Ask the Agents Window to draft an Automation prefilled with the wrapper body, or use `/loop <interval>` for a session-only loop. (Note: persistent Automations require context committed to a private repo.)

## Step 5: Configuration Summary, False-Success Check & Decision Card

After outputting the wrapper, in this order:

1. **Configuration summary.** State exactly what you configured, in plain text, with every line filled:

```
Configured: <job name> on <tool>
Runs: <days> at <h:mm AM/PM> <timezone>
Must be running during that window: <see below>
Output lands: <where>
Owner: <who>
Turn off: <where in the tool>
Review by: <date>
```

   The "must be running" line is per tool, not a guess:
   - **ChatGPT, Gemini, M365 Copilot, Claude Code cloud routines, Cursor Automations:** nothing on my side — the run happens in the tool's service; my computer can be off.
   - **Claude Desktop scheduled tasks:** the Claude Desktop app must be open and the computer awake at that time.
   - **Cursor `/loop`:** the chat session must stay open; the loop ends when it closes.
   - **Cloud tools still need me signed in.** If my session lapses (Copilot) or I stop reading results (ChatGPT, Gemini), the schedule pauses silently. Say so.

2. **Placeholder scan.** Tell me to search the wrapper for `<` and `YYYY` before pasting. If either appears, the wrapper is not finished — do not paste it.
3. **"Scheduled" is a claim about the world.** Do not trust the model saying "done, scheduled." That is the false-success trap from `PROCESS.md`.
4. **The check is the tool's own management screen:**
   - **ChatGPT**: Click **Scheduled** in the sidebar to confirm active tasks.
   - **Gemini**: Open the Scheduled actions list.
   - **M365 Copilot**: Open Scheduled prompts in the Work tab; clear the default 2-week end date.
   - **Claude**: Check cloud routines in Claude Code or sidebar Scheduled tasks in Claude Desktop.
   - **Cursor**: Open the Automations dashboard.
5. **Emit the schedule card for `decisions.md`:**

```markdown
### Schedule card (append to decisions.md)

| Date | Decision | Decided by | Why (one line) | Link |
| --- | --- | --- | --- | --- |
| <YYYY-MM-DD> | Scheduled <job name> on <tool> (<cadence>) | <owner> | Passed 3 manual verify passes; review by <review date> | <where output lands / scheduler location> |
```
