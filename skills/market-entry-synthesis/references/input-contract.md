# Input contract

| 输入包 | 必须字段 | 不能缺少的元数据 |
|---|---|---|
| market | 指标、数值、口径、时间、来源 | 国家、品类、币种、来源 tier |
| competition/channel | SKU、价格、渠道、采集日期 | 规格、促销、税费/配送说明 |
| regulation | 义务、适用性、责任主体、来源 | jurisdiction、官方来源、时效、veto_flag |
| user/culture | 原文、翻译、编码、聚合 | 语言、平台、日期、n、分母、平台偏差 |

任何字段缺失要进入 `evidence_gaps`，而不是被默认为“无问题”。
