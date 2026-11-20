# Quality gates and interpretation boundaries

| Gate | Scope | Minimum evidence before approval |
| --- | --- | --- |
| G0 | Scientific scope | Clear question, phenotype/comparison definitions, unit of analysis |
| G1 | Data governance | Source terms, ethics/permissions, legal storage and sharing |
| G2 | Input identity | Data source, build/version, hashes, schema, metadata checks |
| G3 | Sample design | Independent units, replicate structure, missingness and overlap |
| G4 | Assay QC | Prespecified thresholds, outlier decisions, denominator tracking |
| G5 | Statistical analysis | Correct estimand, assumptions, diagnostics, controls and sensitivity |
| G6 | Method-specific validity | Suitability of model/trajectory/spatial assumptions and alternatives |
| G7 | Evidence scope | Null/failed results, independent support and explicit limitations |
| G8 | Return audit | Frozen design, log/environment, integrity checks and human review |

**Never substitute**: many cells for many independent donors; correlation for causation; computational pseudotime for measured chronological progression; tool output for a biological conclusion; a passing CI job for expert scientific approval; a failed/unavailable analysis for an observed null result.

Define per-phase eligibility and stop conditions **before** execution. Preserve adverse, conflicting, null and missing evidence alongside promising findings. Technical review and scientific adjudication are separate decisions.
