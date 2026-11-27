# phase-01 research & synthesis design — not executed

1. **Question and scope:** Are all empirical claims in the review draft traceable to verified peer-reviewed primary studies or authoritative reviews with explicit species, assay, and cohort context?
2. **Scientific thesis:** Systematic mapping of the 23 curated references (2021-2026) resolves citation gaps in Introduction and Section 1 while identifying public multi-omics datasets for potential downstream figure verification.
3. **Analytical unit:** Individual peer-reviewed study / independent donor or animal cohort reported per reference
4. **Authorized inputs:** `ref-article/LITERATURE_CATALOG.tsv`, `manifests/DATASET_REGISTRY.tsv`, `manuscript/MANUSCRIPT_DRAFT.zh-CN.md`
5. **Primary contrasts:** Primary experimental multi-omics studies (n=16) vs clinical/mechanistic reviews (n=7); Human donor/surgical cohorts vs murine genetic/injury models
6. **Quality & eligibility rules:** Exclude unverified citations or non-peer-reviewed claims; Retain copyrighted publisher PDFs outside Git; record DOI and sha256_16 only; Separate literature indexing from computational re-execution (NOT_EXECUTED)
7. **Expected deliverables & stopping criteria:** ref-article/LITERATURE_CATALOG.tsv; ref-article/REF01..REF23 structured cards; manifests/DATASET_REGISTRY.tsv; Citation backfill table in manuscript/REVIEW_SYNTHESIS_AND_ROADMAP.zh-CN.md — Stop when: All 23 curated PDFs verified with exact DOI and mapped to review sections; Zero broken links or >2 MiB files in validate_repo.py
8. **Scientific reviewer:** `priest-sweety` (`human_approved: false` until reviewed)
