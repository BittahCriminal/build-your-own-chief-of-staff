# Scheduling workflows

Where to paste schedule prompts across tools. Schedule only after 3 manual runs pass `verify.md` (Step 7 in `PROCESS.md`). Build the wrapper with [`prompts/process/schedule-it.md`](../prompts/process/schedule-it.md).

| Tool | Can a pasted prompt create the schedule? | How | Catch |
| --- | --- | --- | --- |
| **ChatGPT** | **Yes** | Put the *when* in the message: "Every weekday at 7:30 AM <your timezone>, …". It proposes the schedule, you confirm once. Edit later by replying in the same chat. | Leave out the time and it just answers now. No file attachments inside the task, so context must be pasted into the prompt body. Free tier: windows ("morning"), not exact times. |
| **Gemini** | **Yes** | Same: include the time and cadence in the prompt. Gemini replies with a summary of the scheduled action. Can also convert an existing chat into one. | 10 slots. Pro/Ultra or qualifying Workspace. Prepared ahead of time, so not live data. |
| **M365 Copilot** | **Yes in the Work tab** since Dec 2025 ("…every Monday at 9 AM"). Elsewhere: run the prompt once, hover, **Schedule this prompt**. | Natural language in mainline Work chat; click path in Teams/Outlook/agents. | Default end date about two weeks out — clear it. 10 per user. Needs a Copilot license. |
| **Claude** | **Claude Code: yes, via `/schedule <description>`** — creates a cloud routine conversationally. **Desktop scheduled tasks: UI only.** **claude.ai chat: no scheduler.** | `/schedule daily morning brief at 7:30am` in a Claude Code session. | Cloud routines get a fresh clone — no local private folder. Desktop tasks read local files but are set in the sidebar, not by prompt. |
| **Cursor** | **Partly.** A chat prompt in the Agents Window can draft an Automation and open the editor prefilled; you save. `/loop` schedules within a session by prompt, but dies with the session. | `/loop 1h …` for session-only. Automations editor for persistent. | Automations run in a repo, so the private folder has to be committed somewhere private. |

## Check paths

"Scheduled" is a claim about the world. Proof comes from the tool's management surface, not the transcript:

- **ChatGPT:** Click **Scheduled** in the sidebar to confirm active tasks.
- **Gemini:** Open the Scheduled actions list.
- **M365 Copilot:** Open Scheduled prompts in the Work tab; clear the default 2-week end date.
- **Claude:** Check cloud routines in Claude Code or sidebar Scheduled tasks in Claude Desktop.
- **Cursor:** Open the Automations dashboard.
