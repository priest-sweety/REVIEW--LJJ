# Local utilities

- `python scripts/init_phase.py --id phase-01 --title "..."` — create a planned phase with `NOT_EXECUTED` status; do not create real results.
- `python scripts/validate_repo.py` — check required files, internal Markdown links, phase index consistency, large/native file patterns and obvious credentials.
- `python -m unittest discover -s tests -v` — test repository scaffolding.

The validator is heuristic. A passing check cannot replace manual privacy, licensing or scientific review.
