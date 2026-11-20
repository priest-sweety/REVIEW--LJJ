# Contributing and maintenance

Use focused branches and Pull Requests after repository initialization. A meaningful PR should name: (1) scientific aim or maintenance rationale; (2) affected phase and round, if any; (3) added or modified design/campaign/return files; (4) authorization and privacy review; (5) local checks performed; and (6) remaining assumptions or blockers.

## Routine

1. Read `AGENTS.md` and relevant phase documents.
2. Register data and design changes before analysis; do not edit frozen evidence.
3. Keep code, small manifests, and permitted summaries in Git. Externalize protected or large files.
4. Run `python scripts/validate_repo.py` and `python -m unittest discover -s tests -v`.
5. Confirm Markdown links, repository paths, status and sample denominators. Manual science review is separate.
6. Open a PR using `.github/pull_request_template.md`; update status/indices only for verified changes.

Use additive revisions and `SUPERSEDES` metadata to correct existing returns. A successful file integrity check does not constitute scientific approval.
