# Context files for long projects

Original: [ai-agent-context-files](https://natesnewsletter.substack.com/p/ai-agent-context-files).

## What we took

One giant file is a graveyard. Split: stable instructions, current state, map of where material lives (`sources.md`), decision history. Progressive context shaping: name what is replaced, push it into unfinished work, keep the old assumption in history. Tool-agnostic markdown. Agent does not invent the business goal or the vendor.

## How this kit applies it

[Build context](../../prompts/process/build-context.md) and the [context templates](../../context-templates/README.md) separate personal instructions, priorities, source locations, open work, and decision history. Keep filled files private. When a decision changes, identify the old assumption, apply the replacement to unfinished work, and retain the earlier decision as history rather than active guidance.

**Check in practice:** The current instruction is unambiguous, unfinished work reflects it, and the previous assumption remains traceable in [decisions.md](../../context-templates/decisions.md). [sources.md](../../context-templates/sources.md) names where evidence lives and how it can be reached.

## What we left out

OpenAI Symphony internals; connector setup.

[All source notes](../SOURCES.md)
