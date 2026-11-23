# Reference literature and methods (`ref-article/`)

This directory indexes the **23 peer-reviewed primary research articles and authoritative reviews (2021–2026)** curated for the review project **_The Inflammatory Niche in Pancreatic Diseases_**.

Per [DATA_POLICY.md](../docs/DATA_POLICY.md), **copyrighted publisher PDFs are never uploaded to Git**. Each reference has a dedicated subdirectory containing verified DOI links, public dataset accessions, local archive SHA-256 prefix (`sha256_16` for local integrity verification without path disclosure), key biological findings, and methodological limitations, derived from [REFERENCE_TEMPLATE.md](REFERENCE_TEMPLATE.md). All computational re-analyses remain `NOT_EXECUTED`.

- Machine-readable master table: [LITERATURE_CATALOG.tsv](LITERATURE_CATALOG.tsv)
- Associated public multi-omics accessions ledger: [manifests/DATASET_REGISTRY.tsv](../manifests/DATASET_REGISTRY.tsv)
- Paragraph-level citation backfill map for the manuscript: [manuscript/REVIEW_SYNTHESIS_AND_ROADMAP.zh-CN.md](../manuscript/REVIEW_SYNTHESIS_AND_ROADMAP.zh-CN.md)
- Evidence atlas (Chinese): [INFLAMMATORY_NICHE_EVIDENCE_ATLAS.zh-CN.md](INFLAMMATORY_NICHE_EVIDENCE_ATLAS.zh-CN.md)
- Verified anchor-paper table for the atlas: [VERIFIED_KEY_PAPERS.tsv](VERIFIED_KEY_PAPERS.tsv)

## Thematic index (23 curated references)

### A. Homeostasis, Acute Pancreatitis (AP) & Acinar Metaplastic Plasticity (7)

| ID | Citation | Type | Core focus | Note |
| --- | --- | --- | --- | --- |
| `REF01` | Tosti et al., *Gastroenterology* 2021 | Research | Human pancreas snRNA-seq + in situ (`Acinar-s`, `Acinar-i`, `Acinar-REG`) | [Card](REF01_tosti-2021-gastro-pancreas-snrna/README.md) |
| `REF21` | Ma et al., *Gastroenterology* 2022 | Research | Conserved SPEM-like/tuft metaplasia program in pancreatic injury | [Card](REF21_ma-2022-gastro-conserved-metaplasia/README.md) |
| `REF04` | Marstrand-Daucé et al., *IJMS* 2023 | Review | Reversible ADM vs KRAS/inflammation-driven PanIN progression | [Card](REF04_marstrand-dauce-2023-ijms-adm-review/README.md) |
| `REF02` | Aney et al., *Gastroenterology* 2024 | Research | FixNCut scRNA-seq + GeoMx WTA across AP injury & recovery | [Card](REF02_aney-2024-gastro-fixncut-ap/README.md) |
| `REF12` | Lee et al., *CMGH* 2025 | Research | Dual role of TF `HBP1`: protects in AP vs promotes *Kras* PanIN | [Card](REF12_lee-2025-cmgh-hbp1-dual-role/README.md) |
| `REF05` | Hu et al., *Signal Transduct. Target. Ther.* 2026 | Review | AP mechanisms, immune cascades, AI stratification & therapies | [Card](REF05_hu-2026-sttt-acute-pancreatitis-review/README.md) |
| `REF15` | Aney et al., *CMGH* 2026 | Research | Conserved acinar gateway metaplasia & early precursor subtype priming | [Card](REF15_aney-2026-cmgh-acinar-metaplastic-states/README.md) |

### B. Chronic Pancreatitis (CP): Immune Crosstalk, Fibrosis & Organoid Therapy (5)

| ID | Citation | Type | Core focus | Note |
| --- | --- | --- | --- | --- |
| `REF09` | Lee et al., *Gut* 2022 | Research | Human hereditary vs idiopathic CP scRNA-seq (`CCR6-CCL20` T-myeloid axis) | [Card](REF09_lee-2022-gut-ccr6-ccl20-cp/README.md) |
| `REF08` | Wang et al., *Gastroenterology* 2023 | Research | Injured acinar `SPHK1/S1P–S1PR2` induces PSC autophagy & CP fibrosis | [Card](REF08_wang-2023-gastro-s1p-psc-autophagy/README.md) |
| `REF11` | Thierens et al., *The Lancet* 2025 | Seminar | Clinical CP diagnosis, management & complication surveillance | [Card](REF11_thierens-2025-lancet-cp-seminar/README.md) |
| `REF10` | Mahapatra et al., *Gastroenterology* 2026 | Review | CP inflammatory pathways, Treg-Th2/ILC2 axis & emerging therapies | [Card](REF10_mahapatra-2026-gastro-cp-mechanisms-review/README.md) |
| `REF18` | Osorio-Vasquez et al., *Cell Stem Cell* 2026 | Research | Human CP patient-derived organoids & CFTR modulator rescue | [Card](REF18_osorio-vasquez-2026-csc-cp-organoids-cftr/README.md) |

### C. Precancerous Niche (PanIN) & Malignant Transition (4)

| ID | Citation | Type | Core focus | Note |
| --- | --- | --- | --- | --- |
| `REF07` | Carpenter et al., *Cancer Discovery* 2023 | Research | 30 human donor pancreata: sporadic PanIN `CD163+/SPP1+` TAMs, C3+ iCAFs, scarce Tregs (2D) | [Card](REF07_carpenter-2023-cancerdiscov-donor-panin/README.md) |
| `REF17` | Bell et al., *Cell Systems* 2024 | Research | Spatial multi-omics integration of PanIN & CAF inflammatory transitions | [Card](REF17_bell-2024-cellsys-panin-caf-spatial/README.md) |
| `REF19` | Kiemen et al., *Cell Press Blue* 2026 | Research | CODA 3D histology (>1,000 precancers): micron-scale Treg/macrophage hotspots | [Card](REF19_kiemen-2026-cpblue-3d-histology-panin/README.md) |
| `REF03` | Zhuo et al., *Cancer Cell* 2026 | Research | `FOSL1`-driven `MP10` re-epithelialization & `CTHRC1high` myCAF–EGFR loop in PanIN→PDAC | [Card](REF03_zhuo-2026-ccell-mp10-reepithelialization/README.md) |

### D. PDAC Fibroinflammatory, Stromal, Perineural & Prognostic Niches (6)

| ID | Citation | Type | Core focus | Note |
| --- | --- | --- | --- | --- |
| `REF16` | Du et al., *Advanced Science* 2025 | Research | `PLXDC1+` TPSCs drive desmoplasia, immunosuppression & ICB resistance | [Card](REF16_du-2025-advsci-plxdc1-tpsc/README.md) |
| `REF20` | Xiao & Puré, *Nature Reviews Cancer* 2025 | Review | Concerted fibroblast-myeloid fibroinflammation & stromal normalization | [Card](REF20_xiao-2025-nrc-fibroinflammation-review/README.md) |
| `REF13` | Chen et al., *Cancer Cell* 2025 | Research | `TGFBI+` Schwann cells, `NLRP3+` TAMs & myCAFs in PDAC neural invasion vs TLS | [Card](REF13_chen-2025-ccell-pdac-neural-invasion/README.md) |
| `REF22` | Kung et al., *Nat. Rev. Clin. Oncol.* 2025 | Review | Converting cold-to-hot PDAC TME, CAF/myeloid targeting & RAS combinations | [Card](REF22_kung-2025-nrco-pdac-tme-review/README.md) |
| `REF06` | Mannucci & Goel, *CA Cancer J. Clin.* 2025 | Review | PDAC early detection, high-risk interception & systemic therapy landscape | [Card](REF06_mannucci-2025-caac-pdac-advances-review/README.md) |
| `REF14` | Tang et al., *Cancer Cell* 2026 | Research | 152-patient snRNA survival atlas (`ctPANDA`) & pan-cell-type target `PLOD2` | [Card](REF14_tang-2026-ccell-ctpanda-survival/README.md) |

### E. Cross-Organ Precancerous Spatial Niche Benchmark (1)

| ID | Citation | Type | Core focus | Note |
| --- | --- | --- | --- | --- |
| `REF23` | Peng et al. (Wang & Kadara), *Cancer Cell* 2026 | Research | Spatial co-evolution of epithelial progenitors & `IL1Bhigh` macrophage niches + early interception | [Card](REF23_peng-2026-ccell-luad-precursor-niche/README.md) |

## Evidence atlas and anchor papers

[`INFLAMMATORY_NICHE_EVIDENCE_ATLAS.zh-CN.md`](INFLAMMATORY_NICHE_EVIDENCE_ATLAS.zh-CN.md) is a targeted, non-PRISMA evidence synthesis that maps ten inflammatory niche types (`N1`–`N10`) onto disease stage, defining and maintaining mechanisms, key pathways, immune-reprogramming functions, candidate markers, and evidence level (`E1`–`E4`) across AP, CP, PanIN, and PDAC (evidence cut-off 2026-11-23). It organizes evidence for drafting the review; it is **not** a systematic review, and its scientific statements remain `REVIEW_REQUIRED`.

Its machine-readable companion, [`VERIFIED_KEY_PAPERS.tsv`](VERIFIED_KEY_PAPERS.tsv), lists the 30 key anchor papers collected for the atlas (`K01`–`K30`, 2011–2026). First author, published title, DOI, and PMID/PMCID were cross-checked record by record against PubMed and Crossref on 2026-11-23. Seven anchor papers are shared with the 23 reading cards above and are linked through `catalog_ref_id`; the other 23 are anchor-only records (`NOT_IN_CATALOG`) **without a reading card, dataset-accession indexing, or local archive fingerprint**. Bibliographic verification is not a content review.

| Column | Meaning |
| --- | --- |
| `ref_key` | Anchor-paper key (`K01`–`K30`) |
| `stage`, `niche_id` | Disease stage(s) and atlas niche type(s) the evidence is used for |
| `citation` | `First author et al. Published title` |
| `year`, `journal`, `doi` | Year, journal, and DOI |
| `pmid`, `pmcid` | PubMed ID and PubMed Central ID; `NOT_IN_PMC` when PubMed listed no PMC record at verification time |
| `model_or_cohort`, `main_finding`, `evidence_class`, `limitations` | Original synthesis notes, not publisher abstracts |
| `catalog_ref_id` | Matching `REFxx` card in [LITERATURE_CATALOG.tsv](LITERATURE_CATALOG.tsv) (matched by DOI), or `NOT_IN_CATALOG` |
| `bibliography_verified` | Sources and date of the bibliographic cross-check (`pubmed_crossref_2026-11-23`) |
