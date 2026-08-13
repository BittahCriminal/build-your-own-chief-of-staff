# Get this kit onto your machine

No install. No plugin. You want **two folders**:

| Folder | What it is | Share it? |
| --- | --- | --- |
| **The kit** | These prompt files (`PROCESS.md`, `prompts/`, `how-to/`) | Yes — it is public |
| **Your context** | Filled-in copies of `who-i-am.md`, `priorities.md`, `voice.md`, … | **Never** — that is you |

Pick the path that matches how you work. Then go back to the [30-minute start](README.md#start-here-30-minutes).

---

## 1. Browser only (ChatGPT, Gemini, claude.ai)

You do not need the repo on disk.

1. Open the prompt you want, e.g. [what-to-automate.md](https://github.com/BittahCriminal/build-your-own-chief-of-staff/blob/main/prompts/process/what-to-automate.md).
2. Click **Raw**, select all, copy, paste into a new chat.
3. When you have context files, **attach** those files to the same chat (or to a Project / Gem so they persist). Do not paste secrets into a prompt you will screenshot.

That is the whole consume path. The kit lives on GitHub; *you* live in the attachments.

---

## 2. A PC (Windows or Mac) — unzip and go

Git is optional. You need a browser and a folder you own.

1. On the GitHub repo, click the green **Code** button → **Download ZIP**. Unzip it. GitHub names the folder `build-your-own-chief-of-staff-main` — rename it to `chief-of-staff-kit` if you want.
2. Put that folder somewhere boring and durable:
   - Windows: `Documents\chief-of-staff-kit`
   - Mac: `Documents/chief-of-staff-kit`
3. Copy the folder `context-templates` to a **sibling** folder named `chief-of-staff-context` (also under Documents). That copy is yours. Fill it in. Do not put it in Dropbox/Google Drive shared with a team, and do not email it.
4. Open a prompt file in Notepad / TextEdit, copy everything below the line, paste into Copilot / ChatGPT / Claude / Gemini. Attach files from `chief-of-staff-context`.

To update the kit later: download a new zip, replace `chief-of-staff-kit`, leave `chief-of-staff-context` alone.

---

## 3. A workstation (Cursor, Copilot, Claude Code)

1. Get the kit onto disk — unzip as above, **or** `git clone https://github.com/BittahCriminal/build-your-own-chief-of-staff.git` if you already use git.
2. Open **that folder** as the project (Cursor: File → Open Folder).
3. Paste [`prompts/process/bring-it-home.md`](prompts/process/bring-it-home.md) into the agent. It will create the private context folder **next to** the kit (not inside the git repo) and stop. You fill the blanks, or run [`build-context.md`](prompts/process/build-context.md) to be interviewed.
4. After that: `@` the private files when you run a workflow. Drafts only.

If you already use GitHub, fork the repo (or clone it) and work from *your* copy. Still keep context files out of git.

---

## What not to do

- Do not fill in `context-templates/` inside the public kit and push it.
- Do not grant send / delete / pay permissions on the first run.
- Do not paste the whole kit into one chat and hope. One prompt file per run.
