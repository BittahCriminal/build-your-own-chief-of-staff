# Citation Guard + Assumption Checker

Original: [open-skills / context-engineering](https://unlock-ai.natebjones.com/open-skills/context-engineering).

## What we took

Claims either cite evidence that *supports* them, ask for confirmation, or get cut. Three-state verdicts. An adversarial pass hunts unstated assumptions and evidence gaps — skeptic, not collaborator. Inventory sources before drafting ([project room](project-room.md)). Portable as `evidence-based-investigation.md`: user-named systems, not a vendor MCP.

## How this kit applies it

[Verify](../../prompts/process/verify.md) checks a draft against a known SOP. [Evidence-based investigation](../../prompts/process/evidence-based-investigation.md) checks the underlying facts and assumptions when the plan itself may be wrong. A citation must resolve and support the specific claim. The source's three verdicts are pass, needs review, and fail; needs review is not a pass for an unsupported claim.

**Check in practice:** Open the evidence, compare dates, amounts, and asserted decisions, and expose contradictions or unsupported assumptions. Keep inferred and assumed statements distinct from verified facts. Start with the [project-room inventory](project-room.md) when the source set is unclear.

## What we left out

SQLite case store; Open Brain; EngHub / WorkIQ / mutation-gate specifics.

[All source notes](../SOURCES.md)
