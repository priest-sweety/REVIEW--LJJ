# Repository maintenance and upload rules

1. Start from `README.md` and `AGENTS.md`; keep project scope and paths coherent.
2. Open a dedicated branch for one scientific aim or fix. Do not silently rewrite prior evidence or unrelated work.
3. Keep research design, instructions, and returned evidence in their designated phase folders.
4. Record unique run ID, source hashes, parameters, commands, software/runtime versions, actual outputs and failures.
5. Update `phases/PHASE_INDEX.tsv`, `manifests/RUN_INDEX.tsv` and any current-status summary **only after facts change**. Avoid claiming scientific acceptance merely because a pipeline returned files.
6. Confirm authorization, licensing, privacy, small-file policy, Markdown link resolution and output limitations.
7. Run structural validation and tests; report what was *not* independently checked.
8. Open a Pull Request with scope, evidence, checks, risks, and needed human decision.
9. After acceptance, link a known commit SHA or tagged version in downstream handoffs. Make follow-up corrections append-only.

Suggested commit style: `docs: ...`, `design(phase-01): ...`, `run(R001): ...`, `audit(R001): ...`, `fix: ...`.
