---
name: user-cultural-insight
description: Use when overseas user reviews, forums, social content, search language, or cultural differences must be analyzed before a brand enters a market or localizes a product, message, or channel.
---

# User and Cultural Insight

你负责把目标市场的用户内容变成可审计的证据，而不是把少量评论改写成泛泛的用户画像。先设计采集，再保存原文，再编码统计，最后解释文化与中文语境差异。

## Required workflow

1. 确认国家/语言、品类、目标用户、平台范围、时间窗口、研究深度和隐私边界。
2. 生成用户内容采集计划：平台、内容类型、本地关键词、目标样本量、实际样本量和偏差风险。
3. 采集或整理公开内容，保留 URL、日期、平台、原文语言、原文和样本元数据；不得只保留中文翻译。
4. 逐条编码使用场景、动机、痛点、期望结果、障碍、情绪、主题和是否为明确表达。
5. 按国家、平台、时间、产品/SKU 和主题聚合 `n`、分母、频次、样本占比、平台数和典型原文数。
6. 对关键主题做跨平台/跨来源验证，并与市场、竞品、价格和法规证据交叉检查。
7. 输出用户文化证据包和不确定性说明。

作为 `brand-market-entry` 的 Stage 03 子模块运行时，必须读取 Stage 01 的问题树/数据配额与 Stage 02 的竞品/场景词表，并写入：

- `user-cultural-insight.md`
- `ugc-coding.csv`
- `persona-matrix.csv`
- `jtbd-map.md`

上述文件必须携带共同 artifact metadata，并通过 `source_id`、`content_id`、`segment_id` 与原始来源和来源台账互相回链。

样本配额不等于抽样代表性。开始采集前读取 `references/sampling-and-coding.md`；出现国家级文化解释、跨语言语义判断或中文与当地语境比较时，读取 `references/cultural-inference.md`。

## Research-mode rule

The evidence contract uses `original-language`, `literal translation`, `semantic interpretation`, `sample size`, `frequency`, `ratio`, and `platform bias` fields. Standard and deep research require local-language originals; quick scans may be translation-only with lower confidence.

快速扫描可以使用翻译材料，但必须标记 `translation_only` 和较低置信度。标准和深度研究的关键结论必须保留当地语言原文；翻译不能替代原文。原文处理链必须是：原文 → 中文直译 → 语义解释 → 文化背景 → 与中文语境差异 → 商业含义。

## Required tables

### Collection plan

| 国家 | 平台 | 内容类型 | 本地关键词 | 时间范围 | 目标 n | 实际 n | 原文语言 | 采集状态 | 偏差 |
|---|---|---|---|---|---:|---:|---|---|---|

### Raw content and coding

| content_id | 国家 | 平台 | URL | 日期 | 语言 | SKU | 评分/互动 | 原文 | 中文直译 | 场景 | 动机 | 痛点 | 期望 | 障碍 | 主题 |
|---|---|---|---|---|---|---|---:|---|---|---|---|---|---|---|---|

### Aggregated insight

| 主题 | n | 分母 | 样本占比 | 平台数 | 国家数 | 典型原文数 | 来源时间范围 | 平台偏差 | 置信度 |
|---|---:|---:|---:|---:|---:|---:|---|---|---|

比例只描述当前编码样本，不代表国家人口或所有消费者。不同平台不得未经说明直接合并；重复内容、广告内容和非目标用户要单独标记或排除。报告还要增加严重度、购买/复购影响、商业影响、有效样本量、编码版本和复核结果；频次不等于重要性。

### Sample quality and impact

| 分层 | raw n | 排除 n | 有效 n | codebook 版本 | audit n | inter-coder agreement | 饱和度 | 主题 | 严重度 | 购买影响 | 商业影响 |
|---|---:|---:|---:|---|---:|---:|---|---|---|---|---|

### Language and culture

| 主题 | 当地原文表达 | 中文直译 | 语义解释 | 文化背景 | 中文语境差异 | 可能误读 | 商业含义 | 证据 |
|---|---|---|---|---|---|---|---|---|

## Output

返回并写入 Stage 03 artifact：原始内容表、编码表、聚合统计表、用户场景/需求表、语言文化差异表、JTBD、来源台账、采集偏差和证据缺口。推荐、结论和用户画像必须引用统计字段及典型原文；一次出现的表达只能作为个案或假设。

样本不足时必须在 `user-cultural-insight.md` 和 CSV metadata 中写明目标 n、实际有效 n、`source_mode`、跳过的聚合/画像模块和对结论的影响。用户原文缺失时可以降级，但必须标记 `translation_only`，不可把翻译材料写成当地语言原话。

## Stage handoff

阶段结束时先写文件，再输出 Gate 3 摘要：用户分层、文化解释、关键 Job、样本量、平台偏差、证据强度和需要用户确认的边界。不要在本模块直接输出最终市场进入建议。

## References

- `references/language-culture-protocol.md`
- `references/sampling-and-coding.md`：需要设计样本、清洗、编码或判断主题饱和时读取
- `references/cultural-inference.md`：需要作文化解释、跨语言比较或国家级结论时读取
- `references/evidence-schema.md`
- `references/category-packs/`
