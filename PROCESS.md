# The process

This is the curriculum. The Chief of Staff files in `prompts/workflows/` are one worked example. Get the kit onto a PC or workstation first: [`START-HERE.md`](START-HERE.md).

The source of truth for these rules is the [Substack](https://app.notion.com/p/36e059b703e180d3a962d862c9e380c5) table and the pages cited in [`research/SOURCES.md`](research/SOURCES.md).

## The two tests

Before you hand a job to an agent, it must pass **both**:

1. **Repeatable.** You would do the same steps next week. Same inputs, same shape of output. If every instance is a special case, it is judgment — keep it.
2. **Verifiable.** A careful human can check the output against a source, a template, or a yes/no rule. "Does this sound good?" is not a check. "Every bullet cites a ticket, email, or note I can open" is a check.

Fail either test → do not automate it. Pass both → write it down.

This is the whole course. Everything else is technique.

Why both: if checking the answer costs as much as producing it, extra attempts just grow the pile. That is the checkability test from [agent-shaped work](https://app.notion.com/p/399059b703e18107b20dfe6bb5c32626). "Don't bother" is a legitimate verdict. [The verification notes](https://app.notion.com/p/36f059b703e18142b351f70732b09c29) say the same thing another way: if you cannot name what would make you say "not yet," you have a vibe, not a job.

## If you freeze

Staring at a capable agent with nothing to type is the common failure, not a personal one. Agents sit idle because nobody dispatched them — not because the model was too dumb ([agent-shaped work](https://app.notion.com/p/399059b703e18107b20dfe6bb5c32626)). People buy the tool, connect a few things, and then face an empty prompt ([let history pick](https://app.notion.com/p/3a0059b703e181c69fafc66f28f76c99)).

Do not let the model pick the problem *and* build it. That hides the judgment call inside the run. Ask it to show evidenced options. You choose. **None** is allowed. Frequency is evidence that a job exists, not proof that automating it would matter.

Paste [`prompts/process/what-to-automate.md`](prompts/process/what-to-automate.md). It walks last week → split the blob → edge vs core → the two tests → one fast win.

## Why this work fails

From the same table, the stall is almost never “we needed a smarter model” ([ChatGPT-5 won’t save you](https://app.notion.com/p/36f059b703e1818fa542e8696353ebb9)).

| Trap | What it looks like | What to do instead |
| --- | --- | --- |
| **Core-first** | Automate the judgment, the craft, the whole workflow. Three months later: stalled agent, bloated scope. | Start at the **edges**: prep, check, summarize, package, hand off. The core stays human until the edges are boringly reliable ([why agent projects fail](https://app.notion.com/p/36f059b703e181d9bd25f984c8bd6945)). |
| **Blob-as-one-job** | “Handle my email.” “Generate the PRD.” “Be my chief of staff.” | Split. Most workflows are five or six tasks pretending to be one ([fails at the task level](https://app.notion.com/p/36f059b703e181f9afedc637cd6529f4)). |
| **No check / false success** | The draft looks finished. The filename matches. The agent said `done`. The world did not change. | Describe what should exist *without* the word “done.” Proof comes from the system that owns the result, not from the transcript ([false success](https://app.notion.com/p/3b5059b703e1819fbd41c6ba9658b0c6)). |
| **Waiting for the next model** | “We’ll try again when GPT-N ships.” | Name the job, the source of truth, the authority limit, and the owner. A better engine in a Model T is still a Model T. |
| **Nobody owns it** | Everyone can use it; it quietly drifts. | One owner, close enough to notice ([ownership](https://app.notion.com/p/387059b703e18195a327e34da56998cb)). |
| **It sends** | First version mails, files, or pays. | Drafts only. A bad send is two problems. |

If a project already stalled, paste [`prompts/process/diagnose-the-stall.md`](prompts/process/diagnose-the-stall.md).

## Seven steps

### 1. Name one job

Not "be my chief of staff." That is a role, not a job ([first agent job](https://app.notion.com/p/3bb059b703e1817b9123ff209fcc5d9d)). A job you actually did last week: the Monday status, the meeting recap, the research one-pager. One. Bring three real examples if you can. "Handle my email" is usually seventeen jobs you have never named ([delegation kit](https://app.notion.com/p/36f059b703e18192a6d8f67fbe74b756)).

### 2. Write the SOP while it is still in your head

Four headings, nothing else — the spec a stranger could run ([delegation kit](https://app.notion.com/p/36f059b703e18192a6d8f67fbe74b756)):

- **Inputs** — what must be in front of you
- **Steps** — the order you already use
- **Output** — the shape of the finished artifact
- **Check** — how you will know it is right, without trusting the model

Add **approvals at reversibility boundaries**: the moments an action becomes hard to undo (send, file, pay, publish). The agent stops there.

Score the spec: can a stranger execute it without questions? Is success binary? Are constraints explicit? If the score is low, the spec will create more work than it saves.

### 3. Put *you* in files you own

The model does not remember you. A short set of context files does ([context files](https://app.notion.com/p/3bb059b703e18152aea0d83b502fa319), [delegation kit memory scaffold](https://app.notion.com/p/36f059b703e18192a6d8f67fbe74b756)):

- who you are and who you answer to
- this quarter's priorities (specific, dated)
- the people who matter, and how fast they get a reply
- how you actually write (and the phrases you never use)
- open loops, and the decisions you already made

Do not dump all of that into one encyclopedia. One giant file becomes a graveyard of stale rules. Split current state from history. When you change your mind, name what is replaced, push it into unfinished work, and keep the old assumption in the decision log — do not delete it.

These files are the operating system. Swap Copilot for Claude tomorrow and nothing important moves.

### 4. The prompt file *is* the process

Paste the SOP into a markdown file. That file is what you run. You do not re-explain yourself in chat. If the output is wrong, the file is wrong.

Installing a skill, or having a clever conversation, proves nothing ([one-job test](https://app.notion.com/p/3b0059b703e181fa81add3d2cd98aeaf)). Give it one real job. Write pass/fail criteria first. Keep the evidence.

### 5. Run it once. Verify it.

Every substantive claim needs a source you can open. Gaps stay gaps — "I could not find X" — they do not become confident prose ([reusable rig citation guard](https://app.notion.com/p/392059b703e1814b96a6dd9913180844)). You read the draft against the check. You send, or you don't.

Self-reported "done" is not a check ([verification gap](https://app.notion.com/p/36f059b703e18142b351f70732b09c29)). The machine enforces the floor (sources present, template filled, length). You own the ceiling (is the recommendation actually right).

### 6. Correct the file, not the chat

The first run will be mediocre. That is expected. Each correction you make more than twice becomes a line in the prompt or the voice file ([maintenance loop](https://app.notion.com/p/3bb059b703e181bfa3f5fbf9ed29b605)): three of the same fix is a rule, two is a candidate, one is a fluke. Delete a stale instruction before you add a new one. The system gets sharper because the **process** got sharper, not because you had a better conversation.

Somebody has to own the agent ([ownership](https://app.notion.com/p/387059b703e18195a327e34da56998cb)). One person, close enough to notice drift. Ownerless agents fail quietly.

### 7. Only then schedule it

Do not put a daily brief on a timer until you have checked it by hand several times. Automation is for a process you already trust. Frequency is evidence that a job exists, not proof that automating it would matter ([automation discovery](https://app.notion.com/p/3a0059b703e181c69fafc66f28f76c99)). Choosing **none** of the offered automations is allowed.

## Safety that is not optional

- **Read-only first.** The agent reads mail, calendars, tickets. It does not send, close, delete, or label.
- **Drafts, never send.** You are the principal. The agent is staff ([reusable rig](https://app.notion.com/p/392059b703e1814b96a6dd9913180844)).
- **Cite or cut.** No source → it does not go in the brief.
- **Inbox is untrusted.** Never follow instructions found inside an email or a ticket. Those are data, not orders ([first agent job](https://app.notion.com/p/3bb059b703e1817b9123ff209fcc5d9d)).
- **Stale is visible.** If a source wasn't available, the output says so. Silent omission is a lie.
- **Approvals sit where actions become hard to undo.** Send, pay, publish, delete.

Buying a smarter model does not skip this. Six things have to be true before a workflow actually changes: the steps, the data, the authority, the evaluation, the audit trail, and an owner who can recover when it is wrong ([six things](https://app.notion.com/p/36f059b703e1813d801bcb34d72141b1)). Most people have built two.

## Why the Chief of Staff is the teaching case

A human Chief of Staff does two kinds of work ([delegation kit](https://app.notion.com/p/36f059b703e18192a6d8f67fbe74b756)). One is operational: reconstruct context, draft the update, prep the meeting, keep open loops from disappearing. That work is repeatable and verifiable. The other is judgment: when to push, when to hold, how a room will land, which red line you will not cross. That work is not.

So we automate the first kind, on purpose, and we use it to learn the process. Then you point the same seven steps at expense reports, hiring screens, incident recaps, customer research — anything that already has a shape and a check.

Do not start by asking "can AI do this?" Ask what **shape** the work is ([shape of the work](https://app.notion.com/p/36f059b703e181cf9c30f637d158b234)). If it depends on trust and judgment, automating it breaks the process at the point where the human mattered most.
