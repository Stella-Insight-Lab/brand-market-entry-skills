# Sampling and coding protocol

## Stratified collection

按国家/语言、平台、内容类型、时间段、产品/SKU、评分或讨论立场分层。每层记录目标 n、实际 n、有效 n 和排除原因；不要用一个总配额掩盖平台集中。

## Cleaning rules

保留 raw 数据，不覆盖原始内容。编码前标记重复、转发、广告/达人合作、非目标用户、机器生成、无关内容、缺失语言和不可读文本。报告同时写 `raw_n`、`excluded_n`、`valid_n`。

## Collection fallback

支持公开网页检索、浏览器人工采集和用户提供的 CSV/JSON。无法访问、需要登录、违反平台条款或无法确认公开授权的来源，记录在 `failed_sources`，不得用模型补写内容。对原文中的姓名、邮箱、订单号、位置等个人信息先脱敏；引用只保留研究所需的最短片段，并保留来源 URL 与访问日期。

## Codebook

每个主题要定义：名称、包含条件、排除条件、正例、反例、是否为用户明确表达、可能的替代编码。允许当地语言新主题进入 codebook，但要记录何时加入和影响哪些早期样本。

## Reliability and saturation

关键主题至少抽样复核一部分编码；多人或模型协作时记录 inter-coder agreement（`inter_coder_agreement`）或人工复核结果。若一致性低，先修订 codebook，不得直接汇总。继续采集后没有新增核心主题时，才可记录“主题趋于饱和”；饱和不是总体代表性。

## Frequency is not importance

在频次之外记录严重度、是否影响购买/复购、替代成本、法规风险、解决后价值和典型性。高频低影响主题与低频高风险主题分开呈现。

## Required fields

```text
stratum
raw_n
excluded_n
valid_n
exclusion_reason
codebook_version
coder_or_model
audit_n
inter_coder_agreement
saturation_status
severity
purchase_impact
repeat_impact
commercial_impact
```
