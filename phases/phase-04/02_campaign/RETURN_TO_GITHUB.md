# Return-to-GitHub instructions

Return only after **actual authorized execution**. Assign a unique `Rxxx` and open a focused PR.

1. Verify the frozen design, actual run ID, environment, input identities/hashes, commands, and permissions.
2. Create `03_returns/Rxxx/` with `README.md`, `METHODS.md`, `RESULTS.md`, `AUDIT.md`, `DOWNSTREAM_HANDOFF.md`, `DATA_PATHS.tsv`, `RUN_MANIFEST.json` and applicable allowed figures/tables. A missing deliverable must be marked `NOT_AVAILABLE` with reason, not fabricated.
3. Record successes, failures, exclusions, tested denominators, uncertainties and unresolved decisions. Separate verification of file bytes from scientific review.
4. Register controlled large outputs only by authorized safe alias, hash, schema, and retrieval instructions; never commit restricted objects.
5. Update `phases/PHASE_INDEX.tsv` and `manifests/RUN_INDEX.tsv` to the **actual** status. `RETURNED` does not imply `ACCEPTED`.
6. Run local checks; create a PR including changed paths, outputs, warnings, limitations, approvals and impact on earlier returns.
7. Never overwrite older `Rxxx` files. Correct through a new return and explicit `SUPERSEDES` record.
