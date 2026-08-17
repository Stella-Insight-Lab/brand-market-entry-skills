# Orchestration workflow

## 1. Brief and configuration

先输出配置表，不直接开始写结论：

| 字段 | 内容 |
|---|---|
| brand/product | 品牌、SKU、配方/规格、现有认证 |
| category | 具体品类及相邻品类排除项 |
| market | 国家、地区、语言、目标城市（如适用） |
| route | 跨境电商、平台店、代理、经销、本地实体等 |
| target user | 人群、场景、价格带、购买者/使用者 |
| research mode | 快速扫描/标准研究/深度研究 |
| decision question | 要比较的市场、产品或进入方式 |

## 2. Hypothesis and evidence design

在采集前建立 decision questions、hypothesis ledger 和 claim-evidence matrix。每个问题写出支持证据、反证、替代解释、证伪条件和最低数据配额。需要这套判断规则时读取 `inference-protocol.md`。

## 3. Two-module handoff

调用市场法规模块时传递：brief、category pack、market pack、研究深度、指标口径和法规核验范围。

调用用户文化模块时传递：brief、当地语言、用户平台候选、关键词方向、目标样本量、时间范围和隐私/采集限制。

两个模块都必须返回：`tables`、`source_registry`、`evidence_gaps`、`confidence_notes`，而不是只有一段总结。

## 4. Synthesis gate

在合成前检查：市场定义、品类定义、币种、时间范围、样本去重、平台偏差、来源层级、原文语言、事实/推断/假设标记。如果法规有未解决否决项，合成结果不得写成 GO。

## 5. Output order

先写方法和表格，再写洞察和建议。报告必须让读者能从一条结论回到一行数据，再回到原始来源。最终目录应额外保留 `assumption-register.md`、`contradiction-log.md`、`falsification-log.md` 和市场测算公式。
