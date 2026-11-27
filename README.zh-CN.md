# REVIEW--LJJ：《胰腺疾病中的炎症生态位》综述与研究仓库

本仓库围绕综述课题 **《The Inflammatory Niche in Pancreatic Diseases》（胰腺疾病中的炎症生态位）** 构建，采用阶段化科研与文献证据管理架构，整合综述初稿、章节审校与续写提纲、23 篇核心参考文献结构化卡片、炎症生态位证据图谱与 30 篇已核验锚点文献表、15 组公开单细胞/空间多组学数据集索引及四阶段推进计划。

[English README](README.md) · [综述初稿正文](manuscript/MANUSCRIPT_DRAFT.zh-CN.md) · [总结整理与续写路线图](manuscript/REVIEW_SYNTHESIS_AND_ROADMAP.zh-CN.md) · [23 篇文献索引](ref-article/README.md) · [炎症生态位证据图谱](ref-article/INFLAMMATORY_NICHE_EVIDENCE_ATLAS.zh-CN.md) · [公开数据集台账](manifests/DATASET_REGISTRY.tsv) · [科学设计](docs/SCIENTIFIC_DESIGN.md)

## 当前进展总览（2026-11）

| 模块 | 当前状态 | 入口文件 |
| --- | --- | --- |
| **Introduction（引言）** | 初稿已完成（~1,210 字，5 段） | [manuscript/MANUSCRIPT_DRAFT.zh-CN.md](manuscript/MANUSCRIPT_DRAFT.zh-CN.md) |
| **1. Cellular Ecology（细胞生态）** | 主体初稿已完成（~6,220 字，覆盖 AP / CP / PanIN / PDAC 四阶段） | [manuscript/MANUSCRIPT_DRAFT.zh-CN.md](manuscript/MANUSCRIPT_DRAFT.zh-CN.md) |
| **2. Immune Reprogramming（免疫重编程）** | 已起笔首段（~110 字），已完成首段勘误与 2.1–2.4 详细写作提纲 | [manuscript/REVIEW_SYNTHESIS_AND_ROADMAP.zh-CN.md](manuscript/REVIEW_SYNTHESIS_AND_ROADMAP.zh-CN.md) |
| **3. Therapeutic Windows（治疗窗口）** | 待动笔，已完成 AP / CP / PanIN 拦截 / PDAC 四大窗口写作提纲与文献锚点 | [manuscript/REVIEW_SYNTHESIS_AND_ROADMAP.zh-CN.md](manuscript/REVIEW_SYNTHESIS_AND_ROADMAP.zh-CN.md) |
| **参考文献库（23 篇，2021–2026）** | 全部核验 DOI、期刊、公开数据集编号与章节映射（原始 PDF 本地留存不入 Git） | [ref-article/README.md](ref-article/README.md) · [LITERATURE_CATALOG.tsv](ref-article/LITERATURE_CATALOG.tsv) |
| **炎症生态位证据图谱 + 锚点文献表（30 篇）** | 10 类生态位（`N1`–`N10`）× 疾病阶段 × 机制 × 通路 × 标志物 × 证据等级（`E1`–`E4`）；30 篇锚点文献的第一作者/题目/DOI/PMID 已对照 PubMed 与 Crossref 核验（2026-11-23），其中 23 篇尚无阅读卡片；科学表述待作者审阅（`REVIEW_REQUIRED`） | [证据图谱](ref-article/INFLAMMATORY_NICHE_EVIDENCE_ATLAS.zh-CN.md) · [VERIFIED_KEY_PAPERS.tsv](ref-article/VERIFIED_KEY_PAPERS.tsv) |
| **公开多组学数据集台账（15 项）** | 已从原始研究提取 GEO/EGA/GSA/dbGaP/Zenodo 编号（状态均为 `NOT_ACQUIRED`） | [manifests/DATASET_REGISTRY.tsv](manifests/DATASET_REGISTRY.tsv) |
| **分阶段计划（`phase-01`–`phase-04`）** | 仅完成 `01_design` 设计契约（`DRAFT` / `NOT_EXECUTED`） | [phases/PHASE_INDEX.tsv](phases/PHASE_INDEX.tsv) |

## 核心工作流与后续步骤

1. **回填引文与修订第 1 节（[phase-01](phases/phase-01/README.md) & [phase-02](phases/phase-02/README.md)）：** 对照 [总结整理与续写路线图](manuscript/REVIEW_SYNTHESIS_AND_ROADMAP.zh-CN.md) 第三节的逐段引文溯源表补齐正文角标，并采纳第四节的 7 项细节审校意见（含首句腺泡细胞笔误、`Collagen I/III` 术语修正、2D vs 3D PanIN Treg 局灶热点整合）。
2. **撰写第 2 节与第 3 节（[phase-03](phases/phase-03/README.md) & [phase-04](phases/phase-04/README.md)）：** 按照路线图第五节的二级提纲与配图蓝图（Figures 1–3、Tables 1–2）完成 *Immune Reprogramming*、*Therapeutic Windows* 及 *Conclusion & Perspectives*。
3. **合规校验与分支协作：** 每次更新后运行下方校验脚本，确保无受版权保护的 PDF/大文件（>2 MiB）、无断链、无本地绝对路径泄露，并通过 Pull Request 合入 `main`。

```bash
python3 scripts/validate_repo.py
python3 -m unittest discover -s tests -v
```

## 科研与数据合规底线

- **版权与隐私保护：** 出版商原始 PDF（共 23 篇，约 277 MB）及含个人元数据的二进制 `.docx` 仅保存在本地隔离目录，不纳入 Git（已在 `.gitignore` 拦截）；仓库仅记录可公开核验的 DOI、公开数据库编号、文件哈希前缀与原创学术总结。
- **状态诚实原则：** 严格区分“文献整理/设计草案（`DRAFT`）”与“实际生信重分析执行（`NOT_EXECUTED`）”，不虚构任何统计结果、重分析图表或人工审批状态（见 [AGENTS.md](AGENTS.md) 与 [docs/DATA_POLICY.md](docs/DATA_POLICY.md)）。
- **可见性提醒：** 若后续文稿包含未发表原创观点或投稿前定稿内容，建议在 GitHub Settings 中将仓库切换为 `Private`（参见 [docs/PUBLIC_RELEASE_CHECKLIST.md](docs/PUBLIC_RELEASE_CHECKLIST.md)）。

## 架构来源

本仓库管理脚手架源自 [LCGaoZzz/Bioinformatics-Research-Template](https://github.com/LCGaoZzz/Bioinformatics-Research-Template)（[MIT License](LICENSE)）。第三方文献、数据、方法与图表的知识产权归原权利人所有。
