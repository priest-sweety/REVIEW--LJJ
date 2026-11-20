# REVIEW--LJJ

**A clean, phase-oriented bioinformatics research workspace for humans and AI coding agents.**

[中文指南](README.zh-CN.md) · [Get started](docs/GETTING_STARTED.md) · [Scientific rules](AGENTS.md) · [Phase lifecycle](phases/PHASE_LIFECYCLE.md) · [Data safety](docs/DATA_POLICY.md)

> **Status: INITIALIZED, NOT STARTED.** This repository is set up with a phase-oriented management scaffold and contains **no study data, real experiment, analyses, results, or completed research rounds**. Fields marked `TODO` are unanswered prompts awaiting truthful entries from the project owner.

## Why this structure?

Bioinformatics projects need more than code: scientific decisions, input provenance, analysis contracts, execution logs, returned evidence, limitations, and independent review must remain distinguishable. This repository adopts a lightweight, reusable framework without prescribing a particular organism, disease, assay, or method.

## At a glance

| Area | What belongs here | Entry point |
| --- | --- | --- |
| Research scope | Questions, hypotheses, design decisions | [Scientific design](docs/SCIENTIFIC_DESIGN.md) |
| Data provenance | Data registration; authorized storage *references* | [Manifest rules](manifests/README.md) |
| Quality and claims | Eligibility checks and interpretation boundaries | [Quality gates](docs/QUALITY_GATES.md) |
| Planned work | Design contracts distinct from execution | [Phase organization](phases/README.md) |
| Returned evidence | Immutable run records and audit trails | [Lifecycle](phases/PHASE_LIFECYCLE.md) |
| Agent collaboration | Rules for Codex, GPT and other tools | [AGENTS.md](AGENTS.md) |
| Repository maintenance | Reviews, change control and release hygiene | [Contributing](CONTRIBUTING.md) |

## Project metadata

| Field | Value |
| --- | --- |
| Project name | REVIEW--LJJ |
| Scientific question | `TODO: RESEARCH_QUESTION` |
| Assay(s) / organism | `TODO: ASSAYS_AND_MODEL` |
| Project owner | [priest-sweety](https://github.com/priest-sweety) |
| Data access level | `TODO: PRIVATE / CONTROLLED / PUBLIC` |
| Current phase | **Not started** |
| Latest validated result | **None** |

## Directory structure

```text
.
├── .github/                  # Review and CI automation
├── config/                   # Project-level configuration
├── docs/                     # Scientific design, policies and guides
├── manifests/                # Source/sample/environment registries (headers only)
├── ref-article/              # Reference reading and methods notes
├── scripts/                  # Local utilities and structural checks
├── tests/                    # Repository scaffold test suite
├── phases/
│   ├── PHASE_INDEX.tsv       # Phase overview, empty until real work begins
│   ├── PHASE_LIFECYCLE.md    # Design/execution/review state machine
│   └── _template/            # Copy to phases/phase-01, phase-02, ...
│       ├── 01_design/        # Pre-run scientific contract
│       ├── 02_campaign/      # Agent execution + return instructions
│       └── 03_returns/       # Read-only outputs *after* actual execution
├── AGENTS.md                 # General agent rules
├── CLAUDE.md                 # Pointers for compatible agent clients
└── README.zh-CN.md           # Student-friendly quick start
```

## A typical research round

1. **Define** — specify the scientific question, contrasts, inputs, exclusion criteria, analysis plan, and acceptance gates in `01_design/`.
2. **Freeze** — review and version the design; issue an agent-specific instruction from `02_campaign/`.
3. **Execute** — perform real analyses in an authorized environment; log commands, versions, parameters, inputs and failures.
4. **Return** — archive allowable summaries and metadata as a unique `03_returns/Rxxx/` package, linking external large or sensitive artifacts by authorized reference.
5. **Review** — audit file integrity and scientific interpretation *separately*. Only an authorized reviewer can approve biological claims.
6. **Update** — adjust the phase index and reporting status only after a real status change; preserve prior returns.

**A design document is not a completed experiment. A successful CI check is not scientific validation.**

## Quick start

```bash
# Start a new research phase (design-only; never synthetic results).
python scripts/init_phase.py --id phase-01 --title "Initial data assessment"
python scripts/validate_repo.py
python -m unittest discover -s tests -v
```

`init_phase.py` creates a *design-only* phase. Edit the generated contracts and register your authorized inputs before executing analysis.

## Provenance and license

The management scaffold of this repository is adopted from [LCGaoZzz/Bioinformatics-Research-Template](https://github.com/LCGaoZzz/Bioinformatics-Research-Template) and is distributed under the [MIT License](LICENSE). Rights in third-party datasets, methods, software, and figures are **not** granted by this license. Before making this repository public with real study content, complete the [public release checklist](docs/PUBLIC_RELEASE_CHECKLIST.md).
