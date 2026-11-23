# REVIEW--LJJ: The Inflammatory Niche in Pancreatic Diseases

**Stage-resolved literature synthesis, spatial-multiomics evidence mapping, and phase-oriented research workspace for _The Inflammatory Niche in Pancreatic Diseases_（胰腺疾病中的炎症生态位）.**

[中文主页](README.zh-CN.md) · [综述初稿](manuscript/MANUSCRIPT_DRAFT.zh-CN.md) · [总结与续写路线图](manuscript/REVIEW_SYNTHESIS_AND_ROADMAP.zh-CN.md) · [23 篇文献库索引](ref-article/README.md) · [证据图谱](ref-article/INFLAMMATORY_NICHE_EVIDENCE_ATLAS.zh-CN.md) · [公开数据集台账](manifests/DATASET_REGISTRY.tsv) · [科学设计](docs/SCIENTIFIC_DESIGN.md)

> **Status: DRAFTING IN PROGRESS · COMPUTATIONAL RE-ANALYSIS `NOT_EXECUTED`.**
> `Introduction` and `1. Cellular Ecology` (spanning AP, CP, PanIN, and PDAC) are drafted in [manuscript/MANUSCRIPT_DRAFT.zh-CN.md](manuscript/MANUSCRIPT_DRAFT.zh-CN.md); `2. Immune Reprogramming` has an opening stub; `3. Therapeutic Windows` is outlined and ready for drafting. All 23 curated reference papers (2021–2026) and 15 associated multi-omics dataset series are indexed with DOIs and accessions. Copyrighted publisher PDFs and raw sequencing objects are kept strictly outside Git per [docs/DATA_POLICY.md](docs/DATA_POLICY.md).

## Scientific overview

Pancreatic inflammation is not an isolated cytokine cascade, but a dynamic, spatially organized **inflammatory niche** co-constructed by plastic acinar/ductal epithelium, pancreatic stellate cells (PSCs) and cancer-associated fibroblasts (CAFs), innate myeloid populations (neutrophils, resident and monocyte-derived macrophages, dendritic cells), adaptive lymphocytes (Th1/Th2/Th17, FOXP3+ Tregs, CD8+ T subsets, B cells/TLS), vascular endothelium, and Schwann-associated perineural structures.

This review synthesizes single-cell, single-nucleus, spatial transcriptomic, 3D histological, organoid, and translational clinical evidence across **four disease stages** and **three thematic pillars**:

1. **Cellular Ecology** — Stage-resolved cellular composition, acinar plasticity (`Acinar-s/i/REG` → reversible ADM → *KRAS*-locked mucinous `MP11` & tuft metaplasia → `FOSL1`-driven `MP10` cutaneous-like re-epithelialization), CAF heterogeneity (`IL-33+` reparative fibroblasts → fibrogenic aPSCs → `C3+` iCAFs → `CTHRC1high` myCAFs & `PLXDC1+` TPSCs), and micron-scale immune/perineural organization.
2. **Immune Reprogramming** — Bidirectional intercellular circuits (`SPHK1/S1P–S1PR2` acinar-to-PSC autophagy activation, `CCR6–CCL20` hereditary CP T-myeloid crosstalk, Treg restraint of type-2 fibrosis vs focal 3D precancerous Treg/TAM hotspots, `CTHRC1high` myCAF–EGFR–`FOSL1` invasion loop, and `TGFBI+` Schwann–`NLRP3+` TAM perineural niches).
3. **Therapeutic Windows** — Stage-matched interventions: promoting resolution in AP, rescuing ductal `CFTR` function and halting fibrogenesis in CP, intercepting high-risk precancerous PanIN niches, and reprogramming cold desmoplastic TME in combination with KRAS inhibitors, neoantigen vaccines, and immunotherapy in PDAC.

## Project metadata

| Field | Value |
| --- | --- |
| Project name | `REVIEW--LJJ` — *The Inflammatory Niche in Pancreatic Diseases* |
| Disease continuum | Homeostasis → Acute Pancreatitis (AP) → Chronic Pancreatitis (CP) → PanIN → PDAC |
| Modalities synthesized | scRNA-seq (incl. FixNCut), snRNA-seq, Spatial Transcriptomics (GeoMx, Visium, ISS), ATAC-seq, 3D CODA Histology, PDOs, Radiomics |
| Project owner | [priest-sweety](https://github.com/priest-sweety) |
| Curated literature | **23** peer-reviewed articles (2021–2026) in [ref-article/](ref-article/README.md) ([TSV](ref-article/LITERATURE_CATALOG.tsv)) |
| Evidence atlas & anchor papers | Niche atlas `N1`–`N10` (zh-CN) + **30** PubMed/Crossref-verified anchor papers (`K01`–`K30`, 2011–2026; 7 shared with the curated set) in [ref-article/](ref-article/README.md) |
| Indexed public datasets | **15** multi-omics accession entries (`NOT_ACQUIRED`) in [manifests/DATASET_REGISTRY.tsv](manifests/DATASET_REGISTRY.tsv) |
| Active phases | `phase-01` to `phase-04` (`DRAFT` / `NOT_EXECUTED` / `REVIEW_REQUIRED`) in [phases/PHASE_INDEX.tsv](phases/PHASE_INDEX.tsv) |
| Validated computational runs | **None** (`manifests/RUN_INDEX.tsv` empty) |

## Quick navigation

| Area | Contents | Entry point |
| --- | --- | --- |
| **Review manuscript** | Current Chinese review draft (`~7,600` chars) imported cleanly from Word | [manuscript/MANUSCRIPT_DRAFT.zh-CN.md](manuscript/MANUSCRIPT_DRAFT.zh-CN.md) |
| **Synthesis & roadmap** | Progress audit, AP→PDAC comparison matrix, citation backfill map, 7 editorial errata, Sections 2–3 outline & Figure blueprints | [manuscript/REVIEW_SYNTHESIS_AND_ROADMAP.zh-CN.md](manuscript/REVIEW_SYNTHESIS_AND_ROADMAP.zh-CN.md) |
| **Literature library** | 23 structured reading cards (`REF01`–`REF23`) + DOI/accession master table | [ref-article/README.md](ref-article/README.md) |
| **Evidence atlas** | Niche types `N1`–`N10` × stage × mechanism × pathway × markers × evidence level, with a 30-paper verified anchor table | [ref-article/INFLAMMATORY_NICHE_EVIDENCE_ATLAS.zh-CN.md](ref-article/INFLAMMATORY_NICHE_EVIDENCE_ATLAS.zh-CN.md) · [ref-article/VERIFIED_KEY_PAPERS.tsv](ref-article/VERIFIED_KEY_PAPERS.tsv) |
| **Scientific design** | Scope, cross-stage contrasts, competing evidence & acceptance criteria | [docs/SCIENTIFIC_DESIGN.md](docs/SCIENTIFIC_DESIGN.md) |
| **Data provenance** | Public GEO/EGA/GSA/dbGaP/Zenodo accessions cited in curated papers (`NOT_ACQUIRED`) | [manifests/DATASET_REGISTRY.tsv](manifests/DATASET_REGISTRY.tsv) |
| **Planned phases** | Four structured review & verification phases ([phase-01](phases/phase-01/README.md)–[phase-04](phases/phase-04/README.md)) | [phases/PHASE_INDEX.tsv](phases/PHASE_INDEX.tsv) |
| **Governance & safety** | Agent rules, quality gates, data policy, and public release checklist | [AGENTS.md](AGENTS.md) · [docs/QUALITY_GATES.md](docs/QUALITY_GATES.md) · [docs/DATA_POLICY.md](docs/DATA_POLICY.md) |

## Repository structure

```text
.
├── .github/                  # CI validation workflow and PR/Issue templates
├── config/                   # Project metadata (config/project.yaml)
├── docs/                     # Scientific design, quality gates, data & release policies
├── manifests/                # Public dataset registry (NOT_ACQUIRED) & run ledgers
├── manuscript/               # Review draft (Markdown) + synthesis, citation map & outline
├── ref-article/              # LITERATURE_CATALOG.tsv, VERIFIED_KEY_PAPERS.tsv, evidence atlas, 23 reference notes (REF01-REF23)
├── phases/                   # Phase lifecycle + phase-01..phase-04 design contracts
├── scripts/                  # init_phase.py and validate_repo.py hygiene checks
└── tests/                    # Dependency-free repository validation unit tests
```

## Validation commands

```bash
python3 scripts/validate_repo.py
python3 -m unittest discover -s tests -v
```

## Provenance and license

The repository management scaffold is adapted from [LCGaoZzz/Bioinformatics-Research-Template](https://github.com/LCGaoZzz/Bioinformatics-Research-Template) under the [MIT License](LICENSE). Rights in third-party publications, datasets, methods, and figures remain with their respective copyright holders. Before releasing unpublished manuscript revisions publicly, review [docs/PUBLIC_RELEASE_CHECKLIST.md](docs/PUBLIC_RELEASE_CHECKLIST.md).
