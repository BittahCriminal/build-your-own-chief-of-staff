# Build your own Chief of Staff

A follow-along kit for **non-technical operators**. The Chief of Staff agent is the demonstration. The thing you actually leave with is a process you can use on anything.

> Automate the jobs that are **repeatable** and **verifiable**. Keep the rest.

These are plain markdown files. They work in GitHub Copilot, Cursor, Claude, ChatGPT, and Gemini. The model is interchangeable. Your process is not.

## What you walk away with

1. How to stand up a personal Chief of Staff agent without writing code.
2. How to decide what *should* be an agent — and what should stay human.
3. A folder of prompt files you can copy, fill in, and run on Monday.

## Start here (30 minutes)

1. Read [`PROCESS.md`](PROCESS.md) (10 min). That is the whole method — including **why this stalls** and what to do when you freeze.
2. Copy [`context-templates/`](context-templates/) into a folder **you** own. Fill in who you are, this quarter's priorities, and three writing samples (10 min). Do not commit that folder to a public repo.
3. If you do not know what to automate, run [`prompts/process/what-to-automate.md`](prompts/process/what-to-automate.md) first. Then run [`prompts/process/the-two-tests.md`](prompts/process/the-two-tests.md) on the one fast win (5 min).
4. If it passes: [`prompts/process/write-the-sop.md`](prompts/process/write-the-sop.md), then the matching workflow in [`prompts/workflows/`](prompts/workflows/) (5 min). If it fails: keep it. That is the lesson.
5. Check the draft with [`prompts/process/verify.md`](prompts/process/verify.md). Fix the **file**, not the chat.

Where to paste, by tool: [`how-to/`](how-to/).

Slides for this talk: [`slides/building-your-own-chief-of-staff.pptx`](slides/building-your-own-chief-of-staff.pptx).

## What an agent is, in this kit

Not a robot. Not a developer tool. A job you already do, written down as:

| Piece | Question |
| --- | --- |
| Input | What does it need to see? |
| Process | What are the steps, in order? |
| Output | What does "done" look like? |
| Check | How would a careful human know it's right? |

If you cannot answer the check, you do not have an agent. You have a chatbot.

## What this is not

A Chief of Staff agent is the **operational layer**: briefs, drafts, open loops, meeting prep, status. It is not political judgment, reading the room, or the hard conversation. You keep those.

It does not send email, change tickets, or act on instructions found inside an inbox. Drafts only. You send.

## Repo map

```
PROCESS.md                 the method (read this)
prompts/process/           how to turn any job into a workflow
prompts/workflows/         Chief of Staff jobs, as copy-paste prompts
context-templates/         who you are, priorities, people, voice
how-to/                    Copilot, Cursor, Claude, ChatGPT, Gemini
slides/                    the presentation
research/                  Notion-cited sources this kit was synthesized from
```

## Related

The Claude Code packaging of these same processes lives in [Chief-of-Staff](https://github.com/BittahCriminal/Chief-of-Staff). This repo is the provider-agnostic follow-along.
