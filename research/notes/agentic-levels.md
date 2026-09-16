# The five levels of agentic work

Original: the AI-native platform ("thinking with platforms") material in the ByteCloud platform-engineering library. Internal report; no public link. The level names and constraints below follow that material's four-levels-plus-zero ladder for AI-assisted development.

## What we took

The ladder itself, translated out of developer language:

| Level | Name | What changes | What limits you |
| --- | --- | --- | --- |
| 0 | Human is the loop | A working process, no agent yet. Build this first. | Nothing to automate until the job is written down. |
| 1 | Human in the loop | The agent drafts. You accept every output. | Your review time. Gains are roughly linear. |
| 2 | Human on the loop | You dispatch jobs, including on a timer. You check evidence, not every line. | How deterministic your checks are. |
| 3 | Human as orchestrator | The agent reacts to signals without being asked. You review the rules, not the runs. | How mature your rules and policy are. |
| 4 | Autonomous | The agent starts work from what it observes. You set constraints and escalation boundaries. | Production-system maturity. Not reachable with a better model alone. |

The load-bearing claim: the quality of your written checks and rules decides how much autonomy you can safely grant. Most organizations sit between Level 1 and Level 2, and the jump from 1 to 2 is the hard one.

## How this kit applies it

Everything in this kit is Level 1 by design. Drafts only, you send, every owner and date is checked against a line in the notes. Step 7 of [PROCESS.md](../../PROCESS.md), [Only then schedule it](../../prompts/process/schedule-it.md), is the door to Level 2: a timer is dispatch. The three-verified-runs gate exists because Level 2 only works when the check in your SOP is one the agent can fail against without you reading the whole output.

**Check in practice:** Name the level you are on for one job. If you still read every line, you are at Level 1. Do not put the job on a timer until the [Check](../../prompts/process/write-the-sop.md) is something a careful stranger could apply in under a minute.

## What we left out

Dispatch paths, non-human identity, workspace isolation, GPU platforms, and the governance planes. Those are platform-team problems. Operators need the ladder and the gate, not the infrastructure.

[All source notes](../SOURCES.md)
