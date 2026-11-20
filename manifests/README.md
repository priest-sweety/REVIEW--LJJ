# Data and run manifests

TSV registries are **headers only**. An empty table means there are no registered sources, samples, environments or completed rounds; never interpret absence of rows as a negative scientific finding.

| File | Purpose |
| --- | --- |
| `DATASET_REGISTRY.tsv` | Source, authorization, reference build and safe storage aliases |
| `SAMPLE_MANIFEST.tsv` | Safe sample aliases, biological units and eligibility |
| `ENVIRONMENT_REGISTRY.tsv` | Tools, versions, runtime/environment references |
| `RUN_INDEX.tsv` | Unique executed round IDs, design versions, return status and review |

Actual controlled-access and unpublished identifiers should be stored in the approved private system, not in a public repository. Record source hashes and safe lookup keys if licensed and authorized.
