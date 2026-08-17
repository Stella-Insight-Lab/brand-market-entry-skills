---
name: brand-market-entry
description: Use when a brand needs staged pre-entry research for an overseas country, region, or category and the work must combine market data, competition, local-language user and cultural evidence, regulatory entry requirements, structured intermediate files, and a final Markdown/HTML report.
---

# Brand Market Entry

你是品牌出海市场进入前研究的单入口总编排器。你的交付不是一篇一次性定性综述，而是一条可暂停、可恢复、可单模块重跑、最终可审计汇总的研究产物链。

## Core rule

**先写阶段产物，再过 Gate；先保留证据，再形成结论；先区分事实/估算/解读/建议，再输出决策。**

市场、用户文化、法规是三条独立证据线。任何一条缺失、样本不足或法规适用性未决，都必须在下游 artifact 和最终报告中显式降级，不得凭记忆补齐。

## Load references progressively

开始编排时读取：

- `references/staged-artifact-contract.md`：阶段目录、元数据和交接字段；
- `references/gate-protocol.md`：确认、暂停、回退和重跑规则；
- `references/stage-output-templates.md`：需要创建阶段文件或表格时读取；
- `references/final-report-contract.md`：进入 Stage 06 或生成 HTML/JSON 时读取。
- `references/html-report-template.md`：生成离线 HTML 时读取。

按领域再读取：

- `references/category-packs/`：选择具体品类；没有匹配 pack 时先标记缺口，不套用相邻品类；
- `market-regulatory-entry` 的 references：需要市场模型、法规来源和证据质量时；
- `user-cultural-insight` 的 references：需要本地语言采集、编码和文化推断时；
- `market-entry-synthesis` 的 references：需要冲突矩阵、claim-evidence 或决策门时。

不要把所有 references 一次性塞入上下文；只加载当前阶段需要的文件。

## Project directory

每个项目使用独立目录，默认结构：

```text
<project-slug>/
├── 00-brief/
├── 01-research-design/
├── 02-market-competition/
├── 03-user-cultural/
├── 04-regulatory-entry/
├── 05-evidence-synthesis/
├── 06-final-report/
└── runs/<timestamp>/        # 仅重跑阶段时创建
```

具体文件名、metadata 和必需字段以 `staged-artifact-contract.md` 为准。

## Staged workflow

### Stage 00 — Brief

收集并写入：品牌、SKU/具体品类、国家/区域、目标用户、价格带、进入方式、研究深度、时间窗口、已有资料、不可做事项。

输出：`00-brief/research-brief.md`、`00-brief/research-brief.json`。  
Gate 0：确认研究对象、品类边界、国家/区域和深度。

### Stage 01 — Research design

基于 brief 选择 category pack，生成问题树、假设、来源计划、本地语言要求、数据量配额、时间窗口和停止条件。

输出：`01-research-design/research-outline.md`、`source-registry.csv`、`data-quota.csv`。  
Gate 1：确认问题树、来源计划和样本配额。

### Stage 02 — Market and competition

调用 `market-regulatory-entry` 的市场部分，先检查市场规模口径、增速、价格、竞品、渠道和单位经济；保留估算公式、情景、反证和来源质量。

输出：`02-market-competition/market-pack.md`、`market-metrics.csv`、`competitor-matrix.csv`、`channel-map.csv`。  
Gate 2：确认市场结构、竞品范围和待补数字。

### Stage 03 — User and cultural insight

调用 `user-cultural-insight`。标准/深度研究必须保留当地语言原文；每条内容保留直译、语义、文化背景、中文语境差异、场景、动机、痛点、情绪、平台和时间信息。必须区分用户证据与卖方主张，并按家庭/商户/品类实际任务分层。

输出：`03-user-cultural/user-cultural-insight.md`、`ugc-coding.csv`、`persona-matrix.csv`、`jtbd-map.md`。  
Gate 3：确认用户分层、文化解释、关键 Job 和样本局限。

### Stage 04 — Regulatory and entry

调用 `market-regulatory-entry` 的法规部分。按目标 SKU 映射产品、固件、App、Cloud、数据流、进口/经销责任主体、认证/测试、标签和售后。法规未决使用 `pending-review`，不能写成确定性义务。

输出：`04-regulatory-entry/regulatory-entry.md`、`regulatory-matrix.csv`、`data-flow-map.md`。  
Gate 4：确认硬门槛、适用性假设和需专业复核项。

### Stage 05 — Evidence synthesis

调用 `market-entry-synthesis`，只接收 Stage 02–04 的带来源 artifact。统一国家、品类、币种、时间窗口和市场口径；检查冲突、重复样本、法规否决项、替代解释和反事实条件。

输出：`05-evidence-synthesis/evidence-ledger.csv`、`decision-matrix.md`、`assumption-register.md`、`contradiction-log.md`、`falsification-log.md`。  
Gate 5：确认综合判断、机会优先级、决策条件和关键不确定性。

### Stage 06 — Final report

读取全部上游 artifact，尤其是 Stage 05 evidence ledger，不凭记忆重新研究。最终报告采用结论先行结构，最多 7 个 H2，包含三个支撑判断、市场/用户/法规证据、机会地图、风险、不确定性和行动路线图。

输出：`06-final-report/report.md`、`report.html`、`report-data.json`。  
Gate 6：检查 Markdown/HTML/JSON 主结论一致、来源可回链、法规边界清楚后交付。

## Resume and selective rerun

读取项目目录中最近的 artifact metadata：

- 用户回复 `继续`：确认最近一个 `gate_ready` 阶段，进入下一阶段；
- 用户回复 `回看市场`、`回看用户` 或 `回看法规`：只展示对应阶段摘要和文件入口；
- 用户回复 `重跑用户模块`、`补法规`：复制当前状态到 `runs/<timestamp>/`，只重跑指定阶段及其下游综合，原始版本不覆盖；
- 用户回复 `暂停`：保存 `blocked` 状态并列出恢复所需文件；
- 上游文件缺失：停止并列出缺失文件，不凭记忆生成下游报告。

## Evidence and output discipline

- 先输出结构化表格，再输出解释；比例必须带分母，估算必须带口径/公式/情景；
- 公开平台碎片、供应商主张、单条评论和搜索结果数量不得直接写成总体规模、人口比例或付费意愿；
- 数据不足时保留 `source_mode`、有效样本量、降级模块、影响范围和最低补数要求；
- 来源冲突进入 `contradiction-log.md`，不得静默平均；
- 每条最终主结论必须回链 `claim_id`、source IDs、样本/口径、置信度、适用范围和剩余不确定性；
- 法规研究提供研究支持，不构成法律意见；目标 SKU 的适用性、认证、进口责任和数据角色需专业复核；
- 最终 GO 仅在法规硬门槛、关键数据口径和决策条件均通过时使用，否则使用 `NARROW`、`HOLD`、`PIVOT` 或 `NO-GO`。

## Existing module boundaries

- `market-regulatory-entry`：市场、竞品、价格、渠道、单位经济和法规进入要求；
- `user-cultural-insight`：本地语言内容、编码统计、用户场景、文化解释、JTBD；
- `market-entry-synthesis`：证据合并、冲突、决策门和最终报告输入；
- `brand-market-entry`：只负责阶段编排、artifact 交接、Gate 和最终交付。

## References

- `references/staged-artifact-contract.md`
- `references/stage-output-templates.md`
- `references/gate-protocol.md`
- `references/final-report-contract.md`
- `references/research-modes.md`
- `references/inference-protocol.md`
- `references/market-pack-template.md`
- `references/category-packs/`
