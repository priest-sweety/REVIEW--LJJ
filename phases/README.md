# Scientific phases

- [Lifecycle and review states](PHASE_LIFECYCLE.md)
- [Phase index](PHASE_INDEX.tsv) — header only until a phase is initialized
- [Design-only phase template](_template/README.md)

Each planned phase has an independent design, campaign instructions, and a return location for real run evidence. The `_template/` directory is **not** a finished phase; it is a reusable scaffold.

Create a new phase with `python scripts/init_phase.py --id phase-01 --title "Scoped objective"`. The script updates `PHASE_INDEX.tsv` with `DRAFT`, `NOT_EXECUTED`, and `REVIEW_REQUIRED`, which do **not** indicate successful analysis.
