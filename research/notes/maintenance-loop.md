# Agent Maintenance Loop

Original: [unlock-ai / maintenance](https://unlock-ai.natebjones.com/guides/agents/maintenance).

## What we took

Correct the harness, not just the prompt. Seven surfaces: job, diet, memory, tools, reach, proof, value. Repeated correction across three runs is a file problem. Delete before you add. Keep / change / pause / retire.

## How this kit applies it

Use [Correct the file](../../prompts/process/correct-the-file.md) for a repeated correction, and [Diagnose the stall](../../prompts/process/diagnose-the-stall.md) when the job or surrounding setup is failing. Inspect the task, inputs, saved context, available tools, permissions, verification, and benefit. A prompt edit cannot repair missing access or an obsolete source.

**Check in practice:** Compare recent runs, locate the cause of the repeated mistake, and verify that the proposed change fixes it. The kit's separate rule of three verified runs before scheduling is an adaptation, documented in [SOURCES.md](../SOURCES.md#first-party-process-portable-not-the-claude-plugin), rather than a guarantee from the source.

## What we left out

Host-specific skill paths.

[All source notes](../SOURCES.md)
