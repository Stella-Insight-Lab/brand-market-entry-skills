---
name: market-regulatory-entry
description: Use when a brand needs to assess overseas market opportunity, competition, pricing, channels, unit economics, or product regulatory entry requirements before entering a country or region.
---

# Market and Regulatory Entry

你负责市场机会与法规/进入约束两条证据线。输出结构化表格和来源台账，再写分析。不要把市场规模、竞品热度或用户兴趣直接等同于可进入性。

## Inputs

需要：品牌/产品、具体品类、目标市场、进入方式、价格带、研究深度、时间范围、币种和已有资料。先确认产品在当地的分类与目标销售身份。

当作为 `brand-market-entry` 的子模块运行时：

- Stage 02 市场部分读取 `01-research-design/research-outline.md`、`source-registry.csv`、`data-quota.csv`；
- Stage 04 法规部分读取 Stage 01 文件、目标 SKU 和 Stage 02 的 `competitor-matrix.csv` / `channel-map.csv`；
- 不直接生成最终总报告；只写本模块 artifact，并在 metadata 中列出 `upstream_artifacts`。

需要估算市场时，先读 `references/market-models.md`；需要给关键结论评级时，读 `references/evidence-quality.md`。没有明确市场口径、公式和假设，不开始写市场规模结论。

## Research stages

1. **Screening**：用官方/权威来源检查禁售、产品分类、强制认证、责任主体、明显长周期或高成本门槛。
2. **Deep research**：建立市场指标、竞争/价格/渠道、单位经济和法规义务清单；记录口径、时间和来源。
3. **Pre-report review**：逐项复核标签、包装、成分/材料、宣称、进口、税费、平台、售后和消费者保护要求。未解决的法规否决项必须导致 `HOLD` 或 `NO-GO`。

## Required tables

### Market and competition

| 指标/对象 | 数值或结论 | 单位/口径 | 年份 | 国家 | 品类 | 来源 | Tier | 置信度 |
|---|---:|---|---|---|---|---|---|---|

至少包含市场规模/增速/结构、需求信号、直接与间接竞品、价格带、平台/零售渠道和单位经济样本。价格表保留 SKU、规格、币种、促销状态、配送/税费和采集日期。

市场规模表必须标记 `top_down / bottom_up / proxy` 方法、TAM/SAM/SOM 层级、公式、假设、重复计算检查以及 low/base/high 情景。需求代理信号不能直接写成市场规模。

### Regulatory path

| 合规事项 | 是否适用 | 产品分类依据 | 责任主体 | 所需材料/动作 | 官方来源 | 时间/成本 | 状态 | 风险 |
|---|---|---|---|---|---|---|---|---|

关键法规结论优先使用 authoritative sources：政府、监管机构、海关、官方法规库、认证机构或平台官方规则。行业报告可以补充背景，但不能替代关键法规来源。

证据覆盖表还要记录权威性、直接性、相关性、时效性、独立性和样本有效性；高 Tier 但口径不匹配的来源不能自动获得高置信度。

## Output

返回并写入：

- Stage 02：`market-pack.md`、`market-metrics.csv`、`competitor-matrix.csv`、`channel-map.csv`；
- Stage 04：`regulatory-entry.md`、`regulatory-matrix.csv`、`data-flow-map.md`；
- 两个阶段都必须保留 source registry、估算公式、样本/覆盖范围、置信度、反证和缺口。

若只有翻译二手材料，标记来源风险。正式法律判断需交由当地律师、认证机构或监管机构复核；本 Skill 不构成法律意见（not legal advice）。法规适用性未决时使用 `status: pending-review`，不能输出确定性 `GO`。

## Stage handoff

阶段结束时只输出：artifact 文件入口、结构化表格摘要、3–5 条关键判断、数据量/来源模式、缺口和 Gate 确认问题。用户确认前不要进入下游综合；需要重跑时复制到 `runs/<timestamp>/`，不覆盖原始 artifact。

## References

- `references/research-contract.md`
- `references/market-models.md`：需要市场规模、TAM/SAM/SOM或单位经济估算时读取
- `references/evidence-quality.md`：需要给证据和结论评级时读取
- `references/evidence-schema.md`
- `references/regulatory-source-protocol.md`
- `references/category-packs/`
