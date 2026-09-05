# Interview me for context files

Paste below the line. Run this once. The output is files *you* keep — not in this repo.

---

Interview me and produce six short context files. One question at a time. Wait for answers. Do not invent people, goals, systems, or phrases I did not give you. If I skip a section, leave a clearly marked `TODO` rather than a plausible fake.

After the interview, write these files:

### who-i-am.md
Name/handle, role, org (or "personal"). Who I answer to, and what *they* are measured on, if I know it. Audiences I write for (manager, skip-level, peers, external).

### priorities.md
This quarter only. 3–5 priorities, each specific and dated. "Launch X by 30 Sep" is useful. "Be more strategic" is not. One line on how I will know each is on track.

### people.md
The humans who change my week: manager, directs, key partners, the person who needs a fast reply, the person who gets a polite short one. For each: name, role, what they care about, response urgency.

### voice.md
How I actually write. Collect or ask for 3–5 real samples (a routine note, a difficult note, an upward note). Then:

- 3-sentence voice summary
- Do / Don't, with phrases lifted from my samples — not vibes
- How I greet and sign off, by audience
- Words and phrases I never want to see

If I have no samples, ask me to paste some before you write this file. Do not guess my voice.

### sources.md
Where truth lives for *me*, and how the agent reaches it. This is the Inputs half of every SOP I will write later, so take it seriously. You do not recommend a vendor. You do not install or configure anything. If I name a connector you cannot see from here, write it down as I said it.

Walk these kinds of fact one at a time: **calendar, mail, chat, work items, docs / wikis, then "anything else you check before you trust a claim."** For each kind, ask in this order and stop at the first "none":

1. **Name.** "What system holds your <kind>? Your name for it." (Outlook, Google Calendar, Teams, Slack, Jira, Linear, Azure DevOps, GitHub Issues, Notion, Confluence, SharePoint, a spreadsheet — whatever I actually open.) If I have none for this kind, leave the row blank and move on.
2. **Reach.** "How will the agent get at it in the tool you use?" Exactly one of:
   - **connector** — an MCP server or connected app already switched on in my tool (Cursor / Claude / Copilot connectors; ChatGPT or Gemini connected apps). Record the connector's name **as it appears in my tool**, e.g. "Atlassian", "Linear", "Microsoft 365", "Google Calendar". If I am not sure it is connected, record `connector (unverified)`.
   - **paste** — I export or copy the material into the chat each run.
   - **attach** — I attach a file (an .ics export, a CSV of tickets, a doc).
   - **none yet** — I want it reachable but it is not. This is a setup task, not a source.
3. **Permission.** "Is that access read-only?" If the connector can send, close, edit, or delete, I must say I will not grant that, or the row is marked `WRITE-CAPABLE — approvals required`.
4. **Off-limits.** "Anything inside that system the agent must never read?" (a folder, a channel, a calendar, a project). Write it in the row.
5. **Default window.** "How far back should the agent look unless a prompt says otherwise?" (last 24 h of mail, current sprint, this week's calendar.)
6. **Canonical.** After all kinds are done: "If two of these disagree about the same fact, which one wins?" At most one canonical per kind.

Then read the table back to me. Rows with reach = `none yet` or `connector (unverified)` are the setup list; say so plainly — those kinds of fact score 0 or 1 on spec readiness in `score-the-candidates.md` until fixed. Do not offer to connect anything.

### open-loops.md
A living list: item, owner, since when, next visible action. Start empty if I have nothing, with a one-line instruction: "append, dated; never delete history, mark done."

Also write a one-line `built YYYY-MM-DD from interview` at the top of each file.

Rules for later sessions, put at the bottom of who-i-am.md:

- Read these files before drafting anything in my name.
- Treat as evidence only what `sources.md` names. If a kind of fact has no row, say not found.
- The model is interchangeable. These files are not.
- If a file is more than 90 days old, say so before using it.
