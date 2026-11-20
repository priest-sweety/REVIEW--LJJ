# REVIEW--LJJ 科研仓库指南

本仓库采用阶段化科研管理架构搭建，供学生及 GPT、Codex 等 AI 编码助手协作使用。目前**不含真实研究数据**，不绑定疾病、物种、组学技术或未发表课题。

[English README](README.md) · [上手教程](docs/GETTING_STARTED.md) · [Agent 规范](AGENTS.md) · [学生提示词](STUDENT_PROMPT.zh-CN.md)

## 使用方式

1. 本仓库已按模板完成初始化；接下来填写 `config/project.yaml`、首页的研究简介、`docs/SCIENTIFIC_DESIGN.md`，并根据授权情况填写 `manifests/` 中的清单。除非课题负责人批准，**不要把实际研究内容公开到 Public 仓库之外的平台**。
2. 让 AI Agent 先阅读 `AGENTS.md`、`phases/PHASE_LIFECYCLE.md`；新课题阶段使用 `python scripts/init_phase.py --id phase-01 --title "Your phase title"`。
3. 按照 `01_design → 02_campaign → 03_returns` 保存设计、执行指令、实际回传证据，不将“设计完成”误写成“已完成分析”。
4. 执行 `python scripts/validate_repo.py` 与 `python -m unittest discover -s tests -v`，通过 Pull Request 提交更新。

## 标准目录

| 目录 | 用途 |
| --- | --- |
| `docs/` | 科学设计、质量门槛、安全管理、维护方法 |
| `config/` | 项目元数据和配置 |
| `manifests/` | 数据来源、样本、软件环境和执行记录索引 |
| `ref-article/` | 文献及方法学索引 |
| `scripts/` | 可复现代码和仓库维护脚本 |
| `phases/` | 分阶段科研任务、独立轮次及审计归档 |

**科研底线：** 不编造数据和分析结果；不提交原始测序文件、可识别信息、未经授权的数据、密钥或私有路径；不覆盖既有回传记录；技术检查与生物学验证必须分开。

## 架构来源

本仓库的管理架构取自 [LCGaoZzz/Bioinformatics-Research-Template](https://github.com/LCGaoZzz/Bioinformatics-Research-Template)（MIT 许可证，见 [LICENSE](LICENSE)）。第三方数据、方法、软件与图表的权利不在该许可证授予范围内。
