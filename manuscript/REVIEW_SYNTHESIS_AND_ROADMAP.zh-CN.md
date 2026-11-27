# 《胰腺疾病中的炎症生态位》综述总结整理与续写路线图

> **关联文稿：** [MANUSCRIPT_DRAFT.zh-CN.md](MANUSCRIPT_DRAFT.zh-CN.md) · **文献总表：** [ref-article/LITERATURE_CATALOG.tsv](../ref-article/LITERATURE_CATALOG.tsv) · **公开数据集台账：** [manifests/DATASET_REGISTRY.tsv](../manifests/DATASET_REGISTRY.tsv)

---

## 一、当前综述进度全景盘点

当前压缩包包含两部分核心资产：（1）综述初稿 `The inflammatory niche in pancreatic diseases.docx`（约 7,600 中文字符，共 16 个正文自然段）；（2）`综述文献/` 文件夹下 **23 篇** 高水平英文文献（2021–2026 年，涵盖 *Nature Reviews Cancer*、*Nature Reviews Clinical Oncology*、*The Lancet*、*CA: A Cancer Journal for Clinicians*、*Cancer Cell* ×4、*Cancer Discovery*、*Cell Stem Cell*、*Cell Systems*、*Cell Press Blue*、*Gastroenterology* ×5、*Gut*、*STTT*、*CMGH* ×2、*Advanced Science*、*IJMS*）。

| 模块 | 当前状态 | 已有内容核心亮点 | 待完成工作 |
| --- | --- | --- | --- |
| **Introduction** | 初稿已完成（5 段，~1,210 字） | 清晰建立“稳态协调 → 急性损伤消退 vs 慢性纤维化重塑 → KRAS 协同下 ADM–PanIN–PDAC 演进”主线；对比传统血清学/常规影像与 scRNA/snRNA/空间转录组/影像组学范式，顺畅引出 **pancreatic inflammatory niche** 及全文三大板块。 | 补齐第 2–5 段的综述与方法学引文角标（`REF04`、`REF06`、`REF11`、`REF20`、`REF23`）。 |
| **1. Cellular Ecology** | 主体已完成（6 段，~6,220 字） | 按 **AP → CP → PanIN → PDAC** 四阶段纵向铺陈，已系统覆盖 `Acinar-s/i/REG`、FixNCut+GeoMx 可逆 ADM、遗传性 vs 特发性 CP 免疫分型、供体胰腺 PanIN 生态、`MP11→MP10 (FOSL1)` 再上皮化转变、`CTHRC1high` myCAF、TLS 与神经侵犯微生态位。 | （1）回填全部未标引的原始研究角标；（2）增补二级小标题（`1.1 AP`–`1.4 PDAC`）增强可读性；（3）补充 `HBP1` 双重作用（`REF12`）、过渡态 gateway 化生（`REF15`）、3D CODA 局灶免疫热点（`REF19`）与 `PLXDC1+` TPSC（`REF16`）。 |
| **2. Immune Reprogramming** | 刚起笔（1 段，109 字） | 仅写到星状细胞活化与 α-SMA / 胶原沉积的开头句。 | 修正首句笔误与术语错误；按“上皮/腺泡触发源 → 基质-免疫轴 → 髓系可塑性 → T/B/TLS 重塑 → 神经-免疫耦合”五大机制模块完整展开（建议 3,500–4,500 字）。 |
| **3. Therapeutic Windows** | 尚未动笔（0 字） | 已在 Introduction 末段锚定章节职责。 | 按 **AP 早期控炎促消退 → CP 导管修复（CFTR）与抗纤维化 → PanIN 癌前精准拦截 → PDAC 微环境正常化与靶免联合** 四大时间窗撰写（建议 3,000–4,000 字），并补充全文总结展望（Conclusion & Perspectives）。 |
| **References & Figures** | 仅挂接 1/23 篇，无图表 | 文献库质量极高且与正文高度咬合（16 篇顶刊原创多组学研究 + 7 篇权威临床/机制综述）。 | 统一回填 23 篇文献角标；制作 2–3 幅机制演化主图与 2 张结构化总结表。 |

---

## 二、跨疾病阶段“胰腺炎症生态位”核心演化矩阵（可直接转化为综述 Table 1）

| 维度 | 正常稳态 / 急性胰腺炎（AP） | 慢性胰腺炎（CP） | 癌前病变（PanIN） | 浸润性胰腺癌（PDAC） |
| --- | --- | --- | --- | --- |
| **腺泡与上皮状态** | 稳态含 `Acinar-s`（分泌）、`Acinar-i`（应激缓冲）、`Acinar-REG`（再生）三亚群（`REF01`）；AP 早期（0–24 h）下调消化酶并上调 `KRT8/18/19/SPP1/EPCAM` 进入可逆 ADM，72 h–5 d 逐步重分化修复（`REF02`）；`HBP1` 发挥急性保护作用（`REF12`）。 | 外/内分泌实质显著萎缩，残余腺泡几乎全转为 `Acinar-REG+` 状态（`REF01`），持续 ADM 与胃幽门/SPEM 样化生（`REF21`）；导管上皮出现获得性或遗传性 `CFTR` 功能缺陷（`REF18`）。 | 炎症协同致癌 `KRAS` + 表观锁定（PRC1/2 沉默 *Ptf1a*、SWI/SNF 激活 *Sox9*）形成不可逆 PanIN（`REF04`）；主体呈黏液经典程序 `MP11`（`CLDN18/TFF1/2/MUC5AC`）及 `Dclk1+` Tuft 细胞（`REF03, REF21`），经 gateway 过渡态早期出现亚型分化（`REF15`）；`<4%` 细胞自发开启 `FOSL1` 再上皮化程序 `MP10`，受基底膜与 `CDKN2A/TP53` 约束（`REF03`）。 | `CDKN2A/TP53` 失活后 `FOSL1` 驱动 `MP10`（`LAMC2/ITGB4/F3`）突破基底膜浸润（`REF03`）；恶性上皮分化为 Classical 与高侵袭 Basal-like/`GABRP+` 状态，外分泌 `IL-6/CSF1/CXCLs` 塑造免疫抑制生态（`REF13, REF14, REF22`）。 |
| **成纤维 / 星状细胞（PSC/CAF）** | `qPSC` 富含维生素 A 脂滴；急性损伤短暂激活 `aPSC`，`IL-33+` 成纤维细胞参与修复与 II 型免疫稳态，约第 14 天恢复静息（`REF02`）。 | 受损腺泡通过 `SPHK1/S1P–S1PR2` 诱导 PSC 自噬与持续活化（`REF08`），伴巨噬细胞 `TGF-β` 及 MMT 协同沉积大量 Collagen I/III，形成不可逆间质纤维化（`REF10, REF11`）。 | 病灶被致密胶原及活化成纤维细胞包绕，以补体高表达炎性 `MP5 iCAF`（`C3/CFH/PDGFRA`）为主，伴炎性信号转换，尚未大规模转化为促侵袭 myCAF（`REF03, REF07, REF17`）。 | 高度空间分区：内部富集伤口样 `CTHRC1high/LRRC15+` myCAF（`MP4`，经 EGFR 反向增强上皮 `FOSL1`，`REF03`）与缺氧诱导 `PLXDC1+` TPSC（致免疫排斥与 ICB 耐药，`REF16`）；外周富集 iCAF、免疫富集区存在 `CCL19+` TPSC 及抗原呈递 apCAF（`REF16, REF20, REF22`）。 |
| **髓系免疫（中性粒 / 巨噬 / DC）** | `CXCL1/2–CXCR2` 快速募集早期中性粒细胞；驻留巨噬活化与单核来源巨噬并存且表型连续可塑，消退期恢复稳态；`cDC1/cDC2` 于 ~72 h 扩增（`REF02, REF05`）。 | 中性粒细胞持续释放 ROS/MPO/NE 并形成清除受阻的 `NETs` 损伤导管；巨噬细胞转向长期促炎（`TNF-α/IL-1β/IL-6`）+ 促纤维化（`TGF-β`/PSC 互作/MMT）并分泌 `CCL20`（`REF09, REF10`）。 | `KRAS` 诱导上皮 `ICAM-1` 招募促炎巨噬（`TNF-α/CCL5–MMP7`、`IL-6/STAT3`）；人供体自发 PanIN 周围显著富集 `CD163+` 巨噬且早期即高表达 `SPP1/APOE/MRC1/C1QA/B`（`REF07`）。 | TAM（含 `SPP1+`、`NLRP3+` 亚群）与 TAN 在侵袭前沿及受侵犯神经周围富集，协同驱动血管异常、T 细胞耗竭与治疗抵抗（`REF13, REF20, REF22`）。 |
| **淋巴细胞与三级淋巴结构（T/B/TLS）** | 稳态胰腺即具较高比例组织 `Th2`（约占 T 细胞 26%–50%），与基质 `IL-33` 共同构成基础 II 型免疫特征（`REF02`）。 | 病因特异性重塑：遗传性 CP 富集 `CCR6+ CD4+ Th`、`TNF+ Th1` 与 Treg（`CCR6–CCL20` 轴），特发性 CP 呈 `FTH1+ CD4+` / `BAG3+ CD8+` 特征（`REF09`）；动物模型中 `FOXP3+` Treg 可抑制 Th2/ILC2 限制过度纤维化（`REF10`）。 | PanIN 周围聚集 `CD4+` 与 `CD8+` T（`KLRC1+` 效应及 `GZMK+/KLRG1+` 耗竭前体）；2D 切片整体罕见 `FOXP3+` Treg（`REF07`），但 3D CODA 揭示高级别异型增生与导管梗阻处已出现数十微米级 **Treg+巨噬局灶免疫抑制热点**（`REF19`）。 | 显著空间异质性：多数呈基质阻隔的“免疫排斥（cold TME）”与 T 细胞终末耗竭；部分区域（含未受侵犯神经旁）形成功能性 `TLS`（T/B 聚集），与较好预后及免疫治疗响应相关（`REF13, REF16, REF22`）。 |
| **血管与神经微生态位** | 内皮黏附分子介导白细胞滚动与跨内皮迁移，恢复期血管灌注重建（`REF02, REF05`）。 | 腺体萎缩、微循环障碍与慢性缺氧，导管钙化梗阻与实质纤维化伴慢性神经性疼痛（`REF10, REF11`）。 | 基底膜整体完整构成物理屏障；导管梗阻与微尺度缺氧促进局部基质-免疫热点形成（`REF03, REF19`）。 | 血管结构畸形致低灌注缺氧与给药障碍；高神经侵犯病灶由 `TGFBI+` 施旺细胞、`NLRP3+` TAM、myCAF 与 Basal-like/`GABRP+` 肿瘤细胞组成促侵袭神经生态位（`REF13`）。 |

---

## 三、已写正文逐段文献溯源回填表（Citation Backfill Map）

当前 `.docx` 正文中仅第 1 段挂接了角标 `1`（`REF05`），但 `Cellular Ecology` 各段中大量精确实验数据均直接源自压缩包内的 23 篇文献。下表给出精确段落与 `REF` 编号对应关系，供定稿时直接插入引文管理器（EndNote / Zotero）：

| 正文位置 | 正文关键论据摘录 | 对应库内文献编号与来源 |
| --- | --- | --- |
| **Introduction 第 1 段** | 胆道/酒精/代谢刺激启动炎症应答（角标 `1`）；炎症与 KRAS 协同参与 ADM → PanIN → PDAC | `REF05` Hu et al., *STTT* 2026；`REF04` Marstrand-Daucé et al., *IJMS* 2023 |
| **Introduction 第 2–4 段** | 临床传统评估局限；scRNA/snRNA/空间转录组/影像组学解析胰腺炎症生态位 | `REF01` Tosti 2021；`REF02` Aney 2024；`REF06` Mannucci & Goel 2025；`REF20` Xiao & Puré 2025；`REF23` Peng et al. 2026 |
| **1. Cellular Ecology — AP 段** | “一项结合 FixNCut 单细胞测序与 GeoMx 全转录组空间分析的研究……早期 ADM（0–24 h）……晚期 ADM（72 h–5 d）……cDC1 和 cDC2 在约 72 h 扩增……Th2 约占 26%–50%……成纤维细胞是 IL-33 重要来源，第 14 天恢复静息” | **`REF02`** Aney et al., *Gastroenterology* 2024 (`10.1053/j.gastro.2024.01.043`) |
| **1. Cellular Ecology — AP 段** | “单核测序可知有三种不同的腺泡细胞亚群：Acinar-s、Acinar-i、Acinar-REG（高表达 REG3A、REG3G、REG1B+）” | **`REF01`** Tosti et al., *Gastroenterology* 2021 (`10.1053/j.gastro.2020.11.010`) |
| **1. Cellular Ecology — AP 段** | 中性粒细胞 CXCL1/CXCL2–CXCR2 跨内皮迁移、蛋白酶与 ROS 级联放大 | **`REF05`** Hu et al., *STTT* 2026 (`10.1038/s41392-025-02394-6`) |
| **1. Cellular Ecology — CP 第 1–2 段** | CP 外/内分泌细胞双降，检测到的腺泡细胞均属 `Acinar-REG+` 亚群 | **`REF01`** Tosti et al., *Gastroenterology* 2021 |
| **1. Cellular Ecology — CP 第 2 段** | CP 持续炎症、aPSC 活化、巨噬细胞 TNF-α/IL-1β/IL-6/TGF-β/MMT、NETs 损伤胰管、`FOXP3+` Treg 限制 Th2/ILC2 促纤维化反应 | **`REF10`** Mahapatra et al., *Gastroenterology* 2026 (`10.1053/j.gastro.2026.03.027`)；**`REF11`** Thierens et al., *Lancet* 2025 |
| **1. Cellular Ecology — CP 第 2 段末** | “遗传性与特发性 CP 在 T 细胞层面上亦有差异：前者 `CCR6+ CD4+` 辅助性 T 细胞、`TNF+ Th1`、Treg 增加，后者出现 `FTH1+ CD4+` 和 `BAG3+ CD8+` T 细胞；驻留 CD8+ T 与驻留巨噬互作改变” | **`REF09`** Lee et al., *Gut* 2022 (`10.1136/gutjnl-2021-324546`) |
| **1. Cellular Ecology — PanIN 段** | PRC1/2 沉默 *Ptf1a*、SWI/SNF 激活 *Sox9*、KRAS 诱导 ICAM-1 招募巨噬（TNF-α/CCL5–MMP7、IL-6/JAK/STAT3）、`Dclk1+` Tuft 细胞 | **`REF04`** Marstrand-Daucé et al., *IJMS* 2023；**`REF21`** Ma et al., *Gastroenterology* 2022 |
| **1. Cellular Ecology — PanIN 段** | 经典黏液程序 `MP11`（`CLDN18/TFF1/2/PIGR/MUC5AC`）、`<4%` 低级别 PanIN 上皮自发激活 `FOSL1/JUNB` 皮肤创伤样再上皮化程序 `MP10`（`LAMC2/ITGB4/F3`）、`MP5` 补体 iCAF vs `MP4` `CTHRC1high` myCAF–EGFR 正反馈突破基底膜 | **`REF03`** Zhuo et al., *Cancer Cell* 2026 (`10.1016/j.ccell.2026.03.021`) |
| **1. Cellular Ecology — PanIN 段** | 人类健康供体胰腺解析：PanIN 周围显著富集 `CD163+` 巨噬（高表达 `SPP1/APOE/MRC1/C1QA/B`）、聚集 `KLRC1+` 及 `GZMK+/KLRG1+` CD8+ T、几乎不存在 `FoxP3+` Treg、`C3/CFH/PDGFRA` iCAF 包绕 | **`REF07`** Carpenter et al., *Cancer Discovery* 2023 (`10.1158/2159-8290.CD-23-0013`)；空间 PanIN–CAF 转变亦见 **`REF17`** Bell et al., *Cell Systems* 2024 |
| **1. Cellular Ecology — PDAC 段** | 纤维炎症微环境、myCAF/iCAF/apCAF 空间异质性、Classical vs Basal-like 上皮、免疫排斥与 TLS、异常血管灌注障碍 | **`REF20`** Xiao & Puré, *Nat. Rev. Cancer* 2025；**`REF22`** Kung et al., *Nat. Rev. Clin. Oncol.* 2025；**`REF16`** Du et al., *Adv. Sci.* 2025 |
| **1. Cellular Ecology — PDAC 段末** | 神经侵犯微生态位：施旺细胞（`TGFBI+`）、巨噬细胞（`NLRP3+` TAM）及特定成纤维细胞亚群共同富集并促进神经重塑与迁移 | **`REF13`** Chen et al., *Cancer Cell* 2025 (`10.1016/j.ccell.2025.06.020`) |

---

## 四、现有初稿细节审校与修订建议（7 项具体改进点）

为尊重原始文稿完整性，[MANUSCRIPT_DRAFT.zh-CN.md](MANUSCRIPT_DRAFT.zh-CN.md) 未擅自改动原文措辞；以下审校意见建议在 `phase-02` / `phase-03` 修订时逐条采纳：

1. **`Immune reprogramming` 首句关键笔误与科学术语勘误（高优先级）：**
   - 原文：“*持续损伤的**胰腺星状细胞**可能在促进胰腺星状细胞活化中起到作用……α-平滑肌肌动蛋白（a-SMA）的产生是PSC活化的标志，并伴随着大量**胶原酶I和III**的产生。*”
   - **修正建议：**
     - “持续损伤的胰腺星状细胞”应为“**持续损伤的胰腺腺泡细胞（injured pancreatic acinar cells, iPACs）**”（恰好可直接衔接库内 `REF08` Wang et al., *Gastroenterology* 2023：受损腺泡细胞通过上调 SPHK1 分泌 1-磷酸鞘氨醇 S1P，作用于 PSC 表面 S1PR2 诱导自噬依赖性 PSC 活化）；
     - “**胶原酶 I 和 III**”属于术语误写（胶原酶 collagenase 是降解胶原的 MMP 蛋白酶），此处应改为“**I 型和 III 型胶原蛋白（Collagen type I and III）**”；
     - `a-SMA` 统一规范为希腊字母 `α-SMA`。
2. **PanIN 阶段 Treg 表述的“2D 切片 vs 3D 全景”辩证整合（提升综述学术深度的亮点）：**
   - 原文依据 `REF07`（Carpenter 2023，供体胰腺 2D 切片/空间转录组）指出“人类自发性 PanIN 微环境中几乎不存在 FoxP3+ Tregs”。
   - 文献库中最新纳入的 **`REF19`（Kiemen et al., *Cell Press Blue* 2026）** 利用细胞分辨率 3D 组织学（CODA）重建了人类大体积胰腺标本中超过 1,000 个癌前病灶，发现单个 PanIN 周围的炎症在数十微米尺度上呈高度局灶异质性——低级别区域确实呈现免疫“冷点”，但在**高级别异型增生（high-grade dysplasia）和导管梗阻区域已形成显著富集 Treg 与巨噬细胞的局灶免疫抑制“热点”**。将这两项研究并置讨论，可完美解释为何早期研究未见广泛 Treg 浸润、而免疫抑制微环境实则在癌前特定空间微区已提前萌芽。
3. **尚未充分写入正文的高价值库内文献补位：**
   - **`REF12`（Lee et al., *CMGH* 2025，`HBP1`）**：转录因子 HBP1 在急性胰腺炎中保护腺泡免受损伤，但在致癌 *Kras* 存在时反而促进早期 PanIN 演进——极适合作为“损伤保护程序被癌基因劫持”的分子范例写入第 1 节或第 2 节；
   - **`REF15`（Aney et al., *CMGH* 2026）**：揭示跨外分泌疾病的保守可塑性及早期过渡态“gateway”化生亚群，且 Classical / Basal-like 程序与协同免疫重塑在癌前阶段即已提前分化；
   - **`REF18`（Osorio-Vasquez et al., *Cell Stem Cell* 2026）**：利用人类 CP 患者来源导管类器官（PDO）证实导管功能障碍及临床获批 **CFTR 调节剂**的功能挽救效应——既补充了 CP 生态位中常被忽视的“导管上皮维度”，更是第 3 节治疗窗口的重磅转化证据；
   - **`REF16`（Du et al., *Adv. Sci.* 2025）**：鉴定缺氧/应激激活的 `PLXDC1+` TPSC 亚群驱动致密基质与免疫检查点阻断（ICB）耐药，而 `CCL19+` TPSC 定位于免疫富集区；
   - **`REF14`（Tang et al., *Cancer Cell* 2026，`ctPANDA`）**：152 例 PDAC 患者 snRNA-seq 关联长期生存，证明同一细胞类型在不同空间生态位具有截然相反的预后意义，并验证跨细胞类型靶点 `PLOD2`；
   - **`REF23`（Peng, Wang & Kadara, *Cancer Cell* 2026）**：多模态空间组学揭示癌前上皮祖细胞与 `IL1Bhigh` 促炎巨噬生态位共演化及抗 IL-1β 癌前拦截疗效，可作为跨器官空间炎症生态位与“癌前抗炎拦截窗”的方法学与概念标杆。
4. **缩略语首次定义与去冗余：**
   - `acinar-to-ductal metaplasia (ADM)` 已在 Introduction 第 1 段定义，后续在 AP、PanIN、PDAC 段落中无需再重复拼写英文全称；同理统一 `PSCs`、`CAFs`、`ECM`、`Treg`、`TAMs` 首次出现位置。
5. **分子与基因大小写/斜体规范：**
   - 人类基因/蛋白用全大写（如 *KRAS*、*CDKN2A*、*TP53*、*FOSL1*、SPP1、CTHRC1），小鼠模型基因首字母大写斜体（如 *Ptf1a*、*Sox9*、*Dclk1*），通篇统一 `NF-κB`（修正一处 `NF-kB`）及上标阳离子符号（`CD4⁺`、`CD8⁺`、`CD163⁺`、`FOXP3⁺`）。
6. **文字小瑕疵修正：**
   - Introduction 第 5 段末：“讨论其在胰腺疾病**及及其**炎症生态位的应用前景” → 删去重复的“及”；
   - Cellular Ecology 第 1 段：“测序手段的**更进**” → 建议改为“多组学与空间测序手段的**演进/革新**”。
7. **结构层级优化：**
   - 当前 `Cellular Ecology` 下连续 6 个超长自然段（每段 1,300–1,650 字），建议拆分为清晰的二级标题：`1.1 Homeostasis and acute pancreatitis: reversible injury-repair ecology`、`1.2 Chronic pancreatitis: persistent fibroinflammatory remodeling`、`1.3 Precancerous PanIN: epigenetically locked metaplasia and focal priming`、`1.4 Invasive PDAC: spatially segregated desmoplastic and neurovascular niches`。

---

## 五、待写章节详细续写提纲（Sections 2 & 3 & Conclusion）

### Section 2: Immune Reprogramming（免疫重编程：跨细胞通讯与状态极化机制）

> **核心写作定位：** 与第 1 节“有哪些细胞、分布在哪（What & Where）”形成严格互补，本节聚焦“**细胞间如何通过配体-受体、代谢物、表观遗传与力学信号重编程局部免疫应答（How & Why）**”。

- **2.1 上皮与腺泡损伤信号启动炎症-基质级联（Epithelial & acinar triggers of niche priming）**
  - 受损腺泡释放 DAMPs、趋化因子（CXCL1/2）及脂质介质：重点阐述 `SPHK1/S1P–S1PR2` 轴诱导 PSC 自噬与活化（`REF08`）；
  - 致癌 *KRAS* 与表观重塑因子（*FOSL1*、*HBP1* 双重开关）如何改写上皮分泌谱（ICAM-1、IL-6、CSF1、GM-CSF、CXCLs），将可逆修复信号锁定为持续促炎/促髓系募集信号（`REF03, REF04, REF12, REF15`）；
  - 化生派生的化学感应 `Dclk1+` Tuft 细胞通过类二十烷酸/细胞因子对局部免疫微环境的调控（`REF21`）。
- **2.2 成纤维/星状细胞亚群对免疫微环境的双向雕塑（CAF/PSC-mediated immune polarization and exclusion）**
  - 修复期 `IL-33+` 成纤维细胞维持稳态 II 型免疫（`REF02`） vs 慢性/肿瘤期 iCAF（`C3/CFH/IL-6/CCL2`）驱动补体激活与髓系浸润（`REF03, REF07, REF17`）；
  - `CTHRC1high/LRRC15+` myCAF（`MP4`）与缺氧激活 `PLXDC1+` TPSC 构筑致密胶原力学屏障（`PLOD2` 介导胶原交联），阻隔效应 T 细胞浸润并导致 ICB 耐药，同时通过 EGFR 配体反向强化上皮 `MP10` 侵袭程序（`REF03, REF14, REF16, REF20`）；
  - 免疫支持型基质支路：`CCL19+` TPSC 与淋巴毒素信号诱导 T/B 细胞聚集及三级淋巴结构（TLS）形成，以及 apCAF（MHC-II+ 缺乏共刺激分子）诱导 CD4+ T 细胞失能或 Treg 分化（`REF16, REF22`）。
- **2.3 髓系细胞功能可塑性：从组织清除到促纤维化与免疫抑制（Myeloid plasticity: macrophages, neutrophils, and DCs）**
  - 巨噬细胞谱系演进：胚胎驻留巨噬 vs 单核招募巨噬；从 AP 混合修复态 → CP 促纤维化态（`TGF-β`、MMT、`CCL20` 分泌） → PanIN/PDAC 中 `CD163+/SPP1+/C1QA+` 及 `NLRP3+` TAM 介导的免疫抑制与基质重塑（`REF02, REF07, REF09, REF10, REF13`）；对照癌前 `IL1Bhigh` 促炎巨噬与上皮祖细胞共演化范式（`REF23`）；
  - 中性粒细胞与 NETosis：CXCR2 募集、ROS/蛋白酶损伤、NETs 诱发胰管阻塞及在 PDAC 中排斥细胞毒性 T 细胞的作用（`REF05, REF10, REF22`）；
  - 树突状细胞（cDC1/cDC2）在急性炎症抗原摄取（72 h 扩增）向 PDAC 交叉呈递受损的转变（`REF02, REF22`）。
- **2.4 适应性免疫失衡与神经-血管免疫耦合（Adaptive T/B remodeling and neurovascular-immune crosstalk）**
  - T 细胞功能的阶段与病因依赖性：CP 中 `CCR6–CCL20` 驱动的致病性 Th1/Th17（遗传性 CP，`REF09`）与 `FOXP3+` Treg 抑制 Th2/ILC2 纤维化的保护性制动（`REF10`） vs PanIN 高级别病灶 3D 局灶 Treg 热点萌芽（`REF19`） vs PDAC 中 `GZMK+` 前体耗竭向终末耗竭 CD8+ T 细胞的演进（`REF07, REF22`）；
  - 神经-免疫-基质三元环路：未受侵犯神经毗邻保护性 TLS，而受侵犯神经周围 `TGFBI+` 施旺细胞、`NLRP3+` TAM 与 myCAF 协同重塑神经周围免疫豁免通道（`REF13`）。

---

### Section 3: Therapeutic Windows（治疗窗口：基于疾病演进阶段的分层精准干预）

> **核心写作定位：** 呼应全文“动态演进”视角——同一通路在不同疾病阶段可能具有截然相反的生物学效应（如 Treg 在 CP 抗纤维化 vs 在 PDAC 促免疫逃逸；HBP1 在 AP 护腺泡 vs 在 PanIN 促癌），因此**干预策略必须严格匹配疾病阶段窗口（Right target at the right stage）**。

- **3.1 急性胰腺炎窗口（AP Window）：早期阻断过度炎症级联与促进生理性再生消退**
  - 早期损伤窗（0–72 h）：钙超载/线粒体保护、抑制异常酶原激活、靶向 `CXCR2` / `NLRP3` 炎症小体 / `NETs` 清除以防止局部坏死向全身炎症反应综合征（SIRS）转化，结合 AI 与多模态生物标志物实现早期重症分层（`REF05`）；
  - 修复消退窗（>72 h）：保护 `Acinar-REG` 与可逆 ADM 向腺泡重分化能力，避免过度抑制修复性巨噬细胞或 `IL-33` 稳态修复轴（`REF01, REF02`）。
- **3.2 慢性胰腺炎窗口（CP Window）：解耦炎症-纤维化正反馈与恢复导管/实质稳态**
  - 上皮与导管源头修正：基于患者来源类器官（PDO）分子分型，应用 **CFTR 矫正剂/增效剂（CFTR modulators）** 逆转遗传性及部分特发性 CP 的导管分泌功能障碍（`REF18`）；阻断受损腺泡 `SPHK1/S1P–S1PR2` 信号抑制 PSC 自噬活化（`REF08`）；
  - 病因分层免疫调控：针对遗传性 CP 靶向 `CCR6–CCL20` 或 TNF 轴（`REF09`），同时保留保护性 Treg 对 2 型促纤维化免疫的约束，联合抗纤维化与微创内镜/多学科管理阻断向胰腺内外分泌衰竭及癌变演进（`REF10, REF11`）。
- **3.3 癌前病变拦截窗口（Precancerous PanIN Interception Window）：锁定高危人群与阻断恶性跨越**
  - 高危人群识别与空间风险分层：结合新发糖尿病、慢性胰腺炎、家族遗传背景、液体活检与高分辨影像组学识别高危癌前状态（`REF06`），借鉴 3D 组织学与空间多组学锁定高级别异型增生伴局灶 Treg/巨噬热点的微区（`REF19`）；
  - 癌前靶向拦截策略：借鉴癌前抗 `IL-1β`/抗炎阻断逆转祖细胞扩增的跨癌种范式（`REF23`），在基底膜突破前靶向 KRAS 早期突变信号（如 KRAS G12D 抑制剂/疫苗预防探索）或阻断 `CTHRC1high myCAF–EGFR–FOSL1 (MP10)` 侵袭开关及 `IL-6/STAT3` 促化生轴（`REF03, REF06, REF22`）。
- **3.4 浸润性胰腺癌窗口（PDAC Window）：基质重编程、“冷”转“热”免疫激活与靶免联合**
  - **基质正常化而非盲目清除（Stromal reprogramming over depletion）**：吸取早期无差别清除 α-SMA+ 肌成纤维细胞反而加速肿瘤侵袭的临床教训，精准靶向促癌/免疫排斥亚群（如抑制 `PLXDC1+` TPSC、`LRRC15+/CTHRC1high` myCAF 或跨细胞类型胶原修饰酶 `PLOD2`），降低组织间液压力并保留抗肿瘤基质约束（`REF03, REF14, REF16, REF20`）；
  - **重塑髓系与诱导功能性 TLS（Converting cold TME to hot）**：靶向 `CSF1R`、`CCR2/CXCR2`、`CD40` 激动剂重编程 `SPP1+`/`NLRP3+` TAM 与中性粒细胞，促进树突状细胞交叉呈递及瘤内 TLS 成熟，并干预 `TGFBI+` 施旺细胞神经侵犯轴改善局部控制与癌痛（`REF13, REF22`）；
  - **KRAS 靶向药与微环境协同联合**：将新一代选择性 KRAS G12D/G12C 及泛 RAS 抑制剂、个体化 mRNA 新抗原疫苗与基质/髓系调节剂及免疫检查点阻断（ICB）理性序贯联用，克服适应性微环境耐药（`REF06, REF22`）。
- **Conclusion & Perspectives（总结与展望）**
  - 总结胰腺炎症生态位从“急性可逆修复 → 慢性纤维炎症锁定 → 癌前局灶免疫逃逸萌芽 → 浸润癌多维空间重塑”的核心规律；
  - 展望未来三大方向：（1）融合无解离偏倚单细胞/单核测序（FixNCut/snRNA）、亚细胞三维空间组学（CODA + Spatial Multi-omics）与无创临床影像组学构建跨尺度数字病理孪生；（2）发展保留免疫-基质-神经组件的类器官共培养与器官芯片模型验证因果机制；（3）开展基于微环境生态分型的早期拦截与生物标志物驱动临床试验。

---

## 六、建议配套综述图表设计方案（Figures & Tables Blueprint）

1. **Figure 1（全景演化时间轴图）：*Spatiotemporal Evolution of the Pancreatic Inflammatory Niche from Injury to Malignancy***
   - 横轴分四栏（Homeostasis/AP → CP → Low/High-grade PanIN → Invasive PDAC），纵轴分层展示：上皮可塑性（`Acinar-s/i/REG` → 可逆 ADM → `MP11`/Tuft → `FOSL1+ MP10`）、基质重塑（qPSC → `IL-33+` 修复成纤维 → S1P 驱动持续 aPSC → `C3+` iCAF → `CTHRC1high` myCAF / `PLXDC1+` TPSC）、免疫与神经微区（Th2 稳态 → `CCR6-CCL20` / NETs → 3D 局灶 Treg/TAM 热点 → 免疫排斥 vs TLS vs `TGFBI+` 施旺神经侵犯生态位）。
2. **Figure 2（核心通讯环路机制图）：*Multicellular Crosstalk and Immune Reprogramming Circuits***
   - 中心绘制四大核心信号回路：① `iPAC (SPHK1/S1P) → S1PR2 → PSC 自噬活化`；② `CTHRC1high myCAF → EGFR → 上皮 FOSL1 (MP10) 基底膜突破`；③ `髓系 CCL20–CCR6+ Th / FOXP3+ Treg–Th2/ILC2 纤维化平衡 / SPP1+ & NLRP3+ TAM 抑制轴`；④ `TGFBI+ Schwann–NLRP3+ TAM–myCAF–GABRP+ PDAC 神经侵犯环路`。
3. **Figure 3（分期治疗窗口图）：*Stage-Matched Therapeutic Windows Targeting the Pancreatic Niche***
   - 对应第 3 节四个窗口，标示代表性靶点/药物策略与干预目标（促消退再生 / CFTR 导管挽救+抗纤维化 / 癌前抗炎与 KRAS 早期拦截 / 基质重编程 + TLS 诱导 + RAS-ICB 联合）。
4. **Table 1：** 跨阶段细胞亚群、分子标志物与空间特征对照表（可直接基于本文第二节矩阵扩充）。
5. **Table 2：** 胰腺疾病炎症生态位代表性单细胞/空间多组学研究及潜在治疗靶点汇总表（可直接由 [ref-article/LITERATURE_CATALOG.tsv](../ref-article/LITERATURE_CATALOG.tsv) 导出精编）。
