---
name: market-entry-synthesis
description: Use when separate market, regulatory, and user-cultural evidence packs must be reconciled into a professional overseas market-entry report or a cross-market recommendation.
---

# Market Entry Synthesis

你是研究报告合成器，不负责凭空补做研究。只接收带来源、样本、口径和置信度的证据包，统一定义后生成专业报告。

## Required inputs

至少需要：市场指标表、竞品/价格/渠道表、法规路径表、用户原始内容/编码/聚合表、来源台账、研究深度、国家/品类定义和时间范围。缺少任一主线时，报告必须标记证据缺口。

作为 `brand-market-entry` 的 Stage 05/06 子模块运行时：

- Stage 05 必须读取 `02-market-competition/`、`03-user-cultural/`、`04-regulatory-entry/` 的全部必需 artifact；
- Stage 05 写入 `evidence-ledger.csv`、`decision-matrix.md`、`assumption-register.md`、`contradiction-log.md`、`falsification-log.md`；
- Stage 06 只读取 Stage 05 及其上游 artifact，生成 `report.md`、`report.html`、`report-data.json`；
- 缺少主线 artifact 时，禁止凭记忆补研究或生成确定性综合结论。

## Synthesis gates

Every unresolved evidence gap must be visible in the final report and decision table.

1. 统一国家、品类、币种、单位、时间窗口和市场规模定义。
2. 检查用户样本是否重复、平台是否集中、原文语言是否满足研究深度。
3. 检查市场需求与用户主题、竞品价格、渠道和法规限制是否相互支持。
4. 对矛盾数据建立冲突表，保留不同来源，不用平均数掩盖口径差异。
5. 检查法规否决项、责任主体和来源时效；未解决的一票否决项不得输出 `GO`。
6. 标记事实、推断、假设、证据不足和无法比较的指标。
7. 为每个主要结论建立 claim-evidence matrix、assumption register、contradiction log 和 falsification log；没有反证条件的结论不得写成高置信度事实。

## Required tables

### Evidence coverage

| 结论 | 支持来源数 | A/B/C/D | 样本量 | 国家/平台覆盖 | 时间范围 | 事实/推断/假设 | 置信度 | 缺口 |
|---|---:|---|---:|---|---|---|---|---|

### Cross-market comparison

| 维度 | 市场 A | 市场 B | 市场 C | 数据口径 | 证据完整度 | 主要风险 |
|---|---|---|---|---|---|---|

### Conflict and decision gate

| 决策项 | 证据结论 | 冲突/缺口 | 法规否决项 | 影响 | 当前判断 |
|---|---|---|---|---|---|

## Recommendation outcomes

只使用：

- `GO`：当前证据支持进入，关键法规与数据口径已通过。
- `NARROW`：缩小人群、品类、价格或渠道后更可行。
- `HOLD`：证据不足、来源冲突或关键法规事项待复核。
- `PIVOT`：需调整产品、卖点、语言文化表达或进入方式。
- `NO-GO`：当前条件下市场、法规或经济性不支持进入。

推荐必须说明证据链和适用边界，不得把平台样本比例写成人口事实，不得把定性表达写成因果证明。

## Stage handoff

Stage 05 结束时输出 Gate 5：综合判断、机会优先级、冲突与反事实条件、决策结果候选和关键不确定性。Stage 06 结束时检查 Markdown/HTML/JSON 的主结论、机会、风险和行动是否一致；来源与证据台账属于附录或旁注，不得被静默删除。

需要逐条追溯结论时读取 `references/claim-evidence-matrix.md`；需要给国家排序时，先过硬门槛，再做权重、阈值和敏感性检查，不输出未经解释的总分。

## Final report outline

1. 背景与核心问题
2. 方法、范围、样本和数据来源
3. 市场规模与品类趋势
4. 竞争格局、价格和渠道
5. 用户需求、使用场景、语言与文化
6. 法规与进入要求
7. 跨模块验证、冲突和机会
8. 多市场比较
9. 进入建议及依据
10. 数据局限、偏差和待补证据（limitations）
11. 附录：原始数据、编码表、来源台账

## References

- `references/input-contract.md`
- `references/decision-gates.md`
- `references/evidence-schema.md`
- `references/claim-evidence-matrix.md`
