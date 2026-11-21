# Scientific design — The Inflammatory Niche in Pancreatic Diseases

> **DESIGN STATUS: DRAFT.** Literature curation and manuscript drafting are in progress (`Introduction` and `Cellular Ecology` drafted; `Immune Reprogramming` and `Therapeutic Windows` in preparation). **No secondary bioinformatics re-analysis pipeline (`Rxxx`) has been executed in this repository.**

## 1. Research question

- **Primary question:** How do epithelial plasticity, stromal activation, innate/adaptive immune remodeling, and neurovascular structures co-evolve to establish, maintain, and transform the **pancreatic inflammatory niche** across the disease continuum from acute pancreatitis (AP) and chronic pancreatitis (CP) to pancreatic intraepithelial neoplasia (PanIN) and invasive pancreatic ductal adenocarcinoma (PDAC)?
- **Scope, organism, tissue/cohort and phenotype definitions:**
  - **Organisms:** Human clinical specimens and organ-donor pancreata (*Homo sapiens*) integrated with mechanistic experimental mouse models (*Mus musculus*, e.g., caerulein-induced AP/CP, pancreatic duct ligation, KC/KPC *Kras*-mutant models).
  - **Disease stages:** (1) Homeostasis & AP (reversible acinar-to-ductal metaplasia [ADM] and resolution); (2) CP (hereditary and idiopathic progressive fibroinflammation); (3) Precancerous PanIN (oncogenic *KRAS*-locked metaplasia, low- vs high-grade dysplasia); (4) Invasive PDAC (desmoplastic, immune-excluded, TLS-bearing, and perineural-invaded niches).
  - **Three structural axes of the review:**
    1. **Cellular Ecology** — stage-resolved cell states, lineage plasticity, and spatial neighborhoods;
    2. **Immune Reprogramming** — bidirectional epithelial–stromal–myeloid–lymphoid–neural signaling circuits;
    3. **Therapeutic Windows** — stage-matched interception, stromal/immune reprogramming, and precision biomarkers.
- **Why the question matters:** Traditional serum biomarkers (amylase, lipase, CRP) and conventional imaging capture bulk organ inflammation or late structural damage, missing micron-scale niche remodeling that dictates whether injured pancreatic tissue regenerates, fibroses, or progresses to lethal malignancy. Synthesizing single-cell, single-nucleus, spatial multi-omics, and 3D histology defines actionable stage-specific windows for early interception and microenvironment normalization.

## 2. Data and eligibility

- **Authorized sources and licenses:**
  - 23 peer-reviewed primary research articles and authoritative reviews (2021–2026) indexed in [ref-article/LITERATURE_CATALOG.tsv](../ref-article/LITERATURE_CATALOG.tsv). Copyrighted publisher PDFs are retained strictly outside Git per [DATA_POLICY.md](DATA_POLICY.md); only bibliographic metadata, DOIs, public accession IDs, SHA-256 file fingerprints, and original critical synthesis notes are tracked in Git.
  - Public multi-omics accessions cited by the primary studies (GEO, EGA, GSA-Human, dbGaP, Zenodo) are cataloged in [manifests/DATASET_REGISTRY.tsv](../manifests/DATASET_REGISTRY.tsv) with status `NOT_ACQUIRED` / `LITERATURE_INDEXED_NOT_ACQUIRED`.
- **Biological unit, sampling design, groups, replicates and batch structure:**
  - When interpreting single-cell and spatial studies, donor/patient/animal count (`N`) is distinguished from cell, nucleus, spot, or lesion count (`n`). For example, 3D CODA mapping of >1,000 PanIN lesions or snRNA-seq of >120,000 nuclei is always contextualized by the underlying human donor cohort size.
- **Inclusion/exclusion criteria and metadata gaps:**
  - Included studies must provide peer-reviewed molecular, cellular, spatial, organoid, or clinical evidence directly addressing pancreatic homeostasis, pancreatitis, precancerous lesions, PDAC microenvironment, or cross-organ precancerous niche methodology.
  - Species differences (murine caerulein/KPC models vs human sporadic donor PanIN and hereditary/idiopathic CP) are explicitly annotated rather than conflated.
- **Primary and fallback input artifacts:**
  - Current manuscript draft: [manuscript/MANUSCRIPT_DRAFT.zh-CN.md](../manuscript/MANUSCRIPT_DRAFT.zh-CN.md)
  - Synthesis, citation backfill map, editorial audit, and continuation outline: [manuscript/REVIEW_SYNTHESIS_AND_ROADMAP.zh-CN.md](../manuscript/REVIEW_SYNTHESIS_AND_ROADMAP.zh-CN.md)

## 3. Methods and comparisons

- **Prespecified primary contrasts and synthesis axes:**
  1. **Epithelial plasticity trajectory:** Homeostatic acinar subsets (`Acinar-s`, `Acinar-i`, `Acinar-REG`) → reversible injury ADM (0–24 h loss of acinar identity; 72 h–5 d re-differentiation) → persistent `Acinar-REG+` dominance in CP → *KRAS* + epigenetic (*Ptf1a* silencing / *Sox9* activation) locking into mucinous `MP11` PanIN, gastric spasmolytic/foveolar & chemosensory `Dclk1+` tuft states, transitional gateway metaplasia, and `FOSL1`-driven `MP10` cutaneous-like re-epithelialization upon `CDKN2A`/`TP53` loss.
  2. **Fibroblast / PSC niche transition:** Quiescent vitamin A-storing qPSCs → transient reparative IL-33+ fibroblasts/aPSCs in AP → persistently activated fibrogenic aPSCs in CP (driven by injured acinar SPHK1/S1P–S1PR2 autophagy signaling and TGF-β/MMT) → complement-expressing `C3+/CFH+/PDGFRA+` iCAFs (`MP5`) encircling PanIN → spatially segregated `CTHRC1high/LRRC15+` myCAFs (`MP4`), `PLXDC1+` TPSCs, `CCL19+` immunoregulatory TPSCs, and apCAFs in PDAC.
  3. **Innate & adaptive immune remodeling:** Neutrophil CXCR2 recruitment and NETosis in AP/CP; resident vs monocyte-derived macrophage plasticity (`CD163+/SPP1+/APOE+/C1QA+` macrophages already present around human sporadic PanIN); baseline pancreatic type-2 immunity (Th2/ILC2/IL-33) vs FOXP3+ Treg restraint of type-2 fibrosis in CP; etiology-specific T cell niches (`CCR6-CCL20` in hereditary CP vs `FTH1+ CD4+` / `BAG3+ CD8+` in idiopathic CP); 2D global Treg scarcity vs 3D micron-scale focal Treg/macrophage hotspots at high-grade PanIN and obstructed ducts; immune exclusion vs TLS and `NLRP3+` TAM / `TGFBI+` Schwann perineural niches in PDAC.
- **Confounding and cross-modality reconciliation:**
  - Dissociation bias against enzyme-rich acinar cells in standard scRNA-seq vs snRNA-seq (Tosti 2021) and reversible DSP fixation FixNCut (Aney 2024).
  - Two-dimensional section sampling bias vs millimeter-to-centimeter 3D CODA reconstruction (Kiemen 2026).

## 4. Evidence and alternatives

- **Distinguishing association, trajectory inference, and mechanism:**
  - Pseudotime/spatial co-localization in human atlases is reported as observational association unless backed by genetic perturbation, lineage tracing, or coculture/organoid functional validation (e.g., *Hbp1* conditional KO, *Fosl1* perturbation + myCAF–EGFR loop, iPAC–PSC S1P/S1PR2 blockade, CP PDO CFTR modulator rescue).
- **Competing / complementary observations preserved:**
  - *Treg role in CP vs PDAC:* Protective anti-fibrotic restraint of Th2/ILC2 in experimental CP vs immunosuppressive barrier in advanced PDAC.
  - *HBP1 dualism:* Cytoprotective against acinar injury in AP yet pro-neoplastic under oncogenic *KRAS* (`REF12`).
  - *PanIN Treg abundance:* Apparent absence in 2D sampling of low-grade donor PanINs (`REF07`) vs focal enrichment in 3D hotspots of higher-grade dysplasia and ductal obstruction (`REF19`).

## 5. Acceptance contract

- **Deliverables across planned phases ([phases/PHASE_INDEX.tsv](../phases/PHASE_INDEX.tsv)):**
  - `phase-01`: Verified 23-reference catalog, public dataset registry, and paragraph-level citation backfill map.
  - `phase-02`: Audited and citation-anchored `Introduction` + `1. Cellular Ecology` text with terminology harmonization.
  - `phase-03`: Complete draft of `2. Immune Reprogramming` covering epithelial/acinar triggers, CAF–immune axes, myeloid plasticity, etiology/stage-resolved T cell states, and neurovascular niche crosstalk.
  - `phase-04`: Complete draft of `3. Therapeutic Windows` + `Conclusion & Perspectives`, schematic Figure 1–3 blueprints, summary Tables 1–2, and unified bibliography formatting.
- **Reviewer and approval:** Scientific adjudication and final wording approval belong exclusively to the human author/PI (`human_approved: false` until explicitly signed off).
