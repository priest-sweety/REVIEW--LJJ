# Adopt this template

This public repository is a **template of management practices**, not a public research project. Start actual unpublished projects in **private** repositories unless your institution and collaborators approve release.

## Steps

1. Create a new repository under your own account. If it is unpublished research, choose **Private**.
2. Download/copy only the template files into your new, clean Git history; do not add any other project's Git history or private remote references.
3. Replace placeholders in `README.md`, `config/project.yaml`, and `docs/SCIENTIFIC_DESIGN.md`. Remove this template's generic project metadata if not applicable.
4. Create authorized sample/source ledgers in `manifests/`. Store sensitive native objects outside Git; use non-sensitive aliases or repository-private metadata.
5. Create an initial design-only phase: `python scripts/init_phase.py --id phase-01 --title "Your scoped question"`.
6. Freeze a reviewable design and acceptance criteria before initiating an AI-agent campaign. Read `phases/_template/02_campaign/AGENT_ENTRY.md`.
7. After actual work runs, create a new `Rxxx` return with real outputs, run manifest, failures, and scientific review, then update indices.
8. Run the local checks and submit a focused PR.

## Checks

```bash
python scripts/validate_repo.py
python -m unittest discover -s tests -v
```

Checks cover file layout, internal Markdown links, basic manifest headers, common oversized/sensitive file formats and obvious accidental secret strings. They cannot establish that a repository is safe to publish, nor verify scientific validity. Manual review and institutional policy still apply.

## Useful links

- [Student prompt (Chinese)](../STUDENT_PROMPT.zh-CN.md)
- [Quality gates](QUALITY_GATES.md)
- [Data and security](DATA_POLICY.md)
- [Maintenance](MAINTENANCE.md)
