# Phase and round lifecycle

Three **independent** state dimensions prevent accidental overstatement:

| Dimension | States | Who changes it? |
| --- | --- | --- |
| Design | `DRAFT → DESIGN_READY → DESIGN_FROZEN`; amendment as `DESIGN_REVISED` | Author with documented review |
| Execution | `NOT_EXECUTED → RUNNING → RETURNED`; exceptional `PARTIAL_BLOCKED` / `BLOCKED` | Executor with real records |
| Scientific review | `REVIEW_REQUIRED → ACCEPTED`; previous record may be `SUPERSEDED` | Authorized scientific reviewer |

A folder or agent prompt is **not** evidence that a pipeline ran. An audit or published file is **not** scientific acceptance.

## Before execution

1. Define scientific question, primary tests, biological units, source data/permissions, design version, feature/variant identifiers, QC, exclusion criteria, and stop conditions.
2. Put reproducible inputs, expected deliverables and quality gates under `01_design/`.
3. Freeze execution instructions and required return format under `02_campaign/`.

## During and after

4. Assign a **unique project-wide** `Rxxx` identifier only for an actual run; record it in `manifests/RUN_INDEX.tsv`.
5. Log commands, software versions, source hashes, environment, parameters, seeds, exclusions, missing data, warnings and failures.
6. Return authorized metadata, summaries and manifests under `03_returns/Rxxx/`, linking controlled large files by safe alias and hash.
7. Audit integrity and science separately; preserve explicit limitations. Do not claim `ACCEPTED` without human review.
8. Correct an error through a new round and a `SUPERSEDES` link. Preserve the original path and hash.

## Pull Request expectations

Identify the phase/round, objective, affected contract, actual commands, data authorization, outputs, checks, unresolved risks, prior-result impact and human approval status. Update the phase index only for evidence-backed changes.
