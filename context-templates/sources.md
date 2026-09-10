# sources.md

built YYYY-MM-DD from interview

You fill this. The agent does not invent systems. A claim is valid only if it cites a row below (or a file in this folder). If a kind of fact has no row, the answer is "not found" — not a guess, not the open web, not "generally known."

This table is also the **Inputs half of every SOP** you will write. A job whose inputs all have a named system *and* a reach method is ready to spec; one with blanks or `none yet` is not.

| Kind of fact | System of record (my name for it) | Reach: connector name / paste / attach / none yet | Read-only? | Off-limits inside it | Default window | Canonical? |
| --- | --- | --- | --- | --- | --- | --- |
| Calendar | | | | | | |
| Mail | | | | | | |
| Chat | | | | | | |
| Work items | | | | | | |
| Docs / wikis | | | | | | |
| Decisions | `decisions.md` in this folder | attach | yes | — | all | yes, unless I name another |
| Open loops | `open-loops.md` in this folder | attach | yes | — | all | yes |
| Other (add rows) | | | | | | |

**Reach** means how the agent gets the material in the tool you use:

- **connector** — an MCP server or connected app already switched on in your tool. Write its name as your tool shows it (e.g. "Atlassian", "Linear", "Microsoft 365", "Google Calendar"). If you are not sure it is on, write `connector (unverified)`.
- **paste** — you export or copy it into the chat each run.
- **attach** — you attach a file each run.
- **none yet** — you want it reachable and it is not. That is a setup task, not a source.

Examples of system names — only if they are actually yours: Outlook, Google Calendar, Teams, Slack, Jira, Linear, Azure DevOps, GitHub Issues, Confluence, SharePoint, Work IQ, Spark, a spreadsheet. The label is yours. Connecting the tool is not this file's job, and this kit does not install connectors.

**Read-only** is the default. If a connector can send, close, edit, or delete, either do not grant that, or write `WRITE-CAPABLE — approvals required` and expect every workflow to stop before that action.

If two systems disagree, believe the row marked canonical. If none is marked, stop and ask me.

Do not treat the model, a chat transcript, or "I remember from last run" as a source of truth.
