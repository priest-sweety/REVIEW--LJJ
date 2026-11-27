# Agent execution entry — instructions only

**Default:** `NOT_EXECUTED`. Do not imply work was performed from this document's existence.

## Prerequisites

Read the repository `AGENTS.md`, the phase `01_design/` contract, the input registry, data-use authorization and `phases/PHASE_LIFECYCLE.md`. If essential items are unknown, mark `BLOCKED` rather than guessing.

## Execution requirements

- Quote the frozen design version, target comparisons, inputs and allowed filesystem/workspace.
- Execute in an isolated workspace; log exact commands, resolved versions, seeds, warnings and exit codes.
- Preserve all tested denominators (including exclusions, failures and non-estimable cases).
- Do not copy restricted data into Git or overwrite previously frozen returns.
- Generate auditable outputs and a machine-readable manifest with input/output hashes.
- Never equate computed associations or trajectories with mechanistic experimental proof.

## Handback

Follow [RETURN_TO_GITHUB.md](RETURN_TO_GITHUB.md). Explicitly disclose which steps truly ran and which were simulated, skipped or blocked. No pre-filled success claims.
