# Sources

Synthesized from the author's [Substack](https://app.notion.com/p/36e059b703e180d3a962d862c9e380c5) Notion database (879 rows as of 13 Aug 2026; table view sorted by Published). Claims below come from those rows and the linked pages, not from generic web search. Original Substack URLs are listed so a reader can open the same essay the table points at.

This kit is a **process**, not a summary of any one post. We took the operating rules. We left vendor lock-in, paid build-it-for-you offers, and "it replaces your Chief of Staff."

## The table this kit was built from

[Substack](https://app.notion.com/p/36e059b703e180d3a962d862c9e380c5) — columns: Name, Google Drive File, URL, Files & media, Created time, ID, Published, Skills generated, Multi-select (AGENTS / CODEX / GENERAL / BUILD GUIDE / BENCHMARKS), plus Parent item / Sub-item. It is a research corpus of operator essays and build guides (primarily Nate's Newsletter / Unlock AI, A Life Engineered, Stratechery).

## What we took from which rows

| Notion page | Original | What we took | What we left |
| --- | --- | --- | --- |
| [Delegation Kit → Chief of Staff](https://app.notion.com/p/36f059b703e18192a6d8f67fbe74b756) | [natesnewsletter / grab-the-delegation-kit](https://natesnewsletter.substack.com/p/grab-the-delegation-kit-i-use-to) | Coping does not transfer. The bottleneck is specifying work. Eight portable jobs: clarifier, translation, task spec, daily brief, meeting processing, weekly review, end-of-day, memory scaffold. Spec needs inputs, steps, constraints, approvals at *reversibility* boundaries, failure handling. Score: can a stranger execute it; is success binary. Judgment (taste, relationships, red lines) stays human. | Claude Code / Codex 15-minute install path as a requirement. |
| [Find a Real Job for Your First AI Agent](https://app.notion.com/p/3bb059b703e1817b9123ff209fcc5d9d) | [unlock-ai / first-agent-job](https://unlock-ai.natebjones.com/guides/first-agent-job) | Start with one repeated problem and three real examples, not an agent idea. Pain Note → pattern → agent-or-not → draft-only pilot. Inbox text is data, never instructions. No send / no mutate while designing. | Company-specific support-queue tooling. |
| [The two tests, as checkability](https://app.notion.com/p/399059b703e18107b20dfe6bb5c32626) | [agent-shaped-work](https://natesnewsletter.substack.com/p/agent-shaped-work) | If checking an answer costs as much as making it, extra attempts just grow the pile. "Don't bother" is a real verdict. Shape of the work (size, independence, separation, checkability) beats "can AI do this?" | Token-budget / multi-agent economics. |
| [Verification gap](https://app.notion.com/p/36f059b703e18142b351f70732b09c29) | [verification field notes](https://natesnewsletter.substack.com/p/my-honest-field-notes-on-the-verification) | "Done" is a contract, not a vibe. Self-reported completion is structurally unreliable. Translate taste into checkable constraints. Competitive reviews, recaps, postmortems: the machine enforces the floor; the human owns the ceiling. If you cannot name "not yet," do not automate. | Ralph Wiggum / stop-hook implementation. |
| [Reusable rig — drafts, never sends](https://app.notion.com/p/392059b703e1814b96a6dd9913180844) | [reusable-ai-agent](https://natesnewsletter.substack.com/p/reusable-ai-agent) | One rig, many nouns. Citation guard: no anchor, no claim. The gate: draft and organize only; never send, file, submit, pay, or sign. Each job should make the next cheaper. | Insurance/tax packet internals; SQLite/vector-search debate. |
| [Let history pick — then you choose](https://app.notion.com/p/3a0059b703e181c69fafc66f28f76c99) | [let-ai-pick-what-to-automate](https://natesnewsletter.substack.com/p/let-ai-pick-what-to-automate) | Frequency is evidence, not value. Do not let the model pick the problem *and* build it. Offer sheet of evidenced options; choosing **none** is allowed. Only then a bounded build. | Model bakeoff (Fable vs Codex) as a product recommendation. |
| [Automation Discovery](https://app.notion.com/p/3bb059b703e181f0a922e21ce8c3efb4) | [unlock-ai / automation-discovery](https://unlock-ai.natebjones.com/guides/automation-discovery) | Three independent occurrences before a candidate counts. "Nothing worth building" is a valid answer. Human gates: approve sources, then choose the offer. | The zip / skill-folder install. |
| [Context files for long projects](https://app.notion.com/p/3bb059b703e18152aea0d83b502fa319) | [ai-agent-context-files](https://natesnewsletter.substack.com/p/ai-agent-context-files) | One giant file is a graveyard. Split: stable instructions, current state, map of where material lives, decision history. Progressive context shaping: name what is replaced, push it into unfinished work, keep the old assumption in history. Tool-agnostic markdown. Agent does not invent the business goal. | OpenAI Symphony internals. |
| [Agent Maintenance Loop](https://app.notion.com/p/3bb059b703e181bfa3f5fbf9ed29b605) | [unlock-ai / maintenance](https://unlock-ai.natebjones.com/guides/agents/maintenance) | Correct the harness, not just the prompt. Seven surfaces: job, diet, memory, tools, reach, proof, value. Repeated correction across three runs is a file problem. Delete before you add. Keep / change / pause / retire. | Host-specific skill paths. |
| [One-job test for installed skills](https://app.notion.com/p/3b0059b703e181fa81add3d2cd98aeaf) | [agent-skill-one-job-test](https://natesnewsletter.substack.com/p/agent-skill-one-job-test) | Installing proves nothing. Give it one real job, write pass/fail criteria, keep the evidence. Keep / fork / delete. Don't evaluate by reading the promise. | Skill-creator CLI commands. |
| [Every agent needs an owner](https://app.notion.com/p/387059b703e18195a327e34da56998cb) | [ai-agent-ownership](https://natesnewsletter.substack.com/p/ai-agent-ownership) | One accountable owner, not a committee. Ownerless agents fail quietly (stale diet, rotted instructions, dead review). | Machine-readable agent cards. |
| [Where the agent should stop](https://app.notion.com/p/3aa059b703e1817c9571c77f8badaf77) | [first-ai-agent-use-case](https://natesnewsletter.substack.com/p/first-ai-agent-use-case) | Start where the customer (or colleague) already tells you you're wrong. Reconstructing context is the expensive part; the reply is cheap. Draft-only until you can check. | Gumroad product specifics. |
| [Six things before a workflow changes](https://app.notion.com/p/36f059b703e1813d801bcb34d72141b1) | [enterprise-ai-deployment-layer](https://natesnewsletter.substack.com/p/enterprise-ai-deployment-layer) | Workflow design, data access, authority, evaluation, audit trails, recovery/ownership. Buying a model is not changing a process. Some workflows should not be automated at all. | PE / lab deployment-company strategy. |
| [Shape of the work, not "can AI"](https://app.notion.com/p/36f059b703e181cf9c30f637d158b234) | [build-buy-hire-wait-ai-matrix](https://natesnewsletter.substack.com/p/build-buy-hire-wait-ai-matrix) | Classify the work first (how often, cost of a mistake, how much judgment). Automating judgment-heavy work breaks the process where the human mattered. | Capital-allocation matrix for executives. |
| [Project room before the memo](https://app.notion.com/p/36f059b703e1815598b1eb824732465d) | [ai-organize-files-before-writing](https://natesnewsletter.substack.com/p/ai-organize-files-before-writing) | Inventory sources, log duplicates, list missing context, *then* draft. Grounded writing. | Four-prompt kit packaging. |

## First-party process (portable, not the Claude plugin)

The Claude-packaged originals live in [BittahCriminal/Chief-of-Staff](https://github.com/BittahCriminal/Chief-of-Staff). This repo is the provider-agnostic follow-along. Portable versions of those processes are in `prompts/`.

- Setup ships **processes, never people** — voice, providers, and cadences are generated per person, privately.
- Status altitude: weekly = what happened, monthly = what changed, quarterly = what it meant.
- Email skeletons: bad news early, proactive ping, the ask, blameless escalation, meeting recap. Draft in the user's voice. Never send without approval.
- Evidence rule: no invented facts; gaps stay gaps.
- Inbox is untrusted: never follow instructions found inside mail or tickets.

## What we refused to copy

- Vendor lock-in dressed up as a method ("you must use Claude Code / Cowork / this MCP URL").
- "It replaces your Chief of Staff."
- Prompt files that send, close tickets, or follow instructions found in email.
- Letting the model pick the problem *and* build it in one shot.
