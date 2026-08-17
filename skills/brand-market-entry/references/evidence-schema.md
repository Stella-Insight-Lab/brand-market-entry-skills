# Evidence schema

每条来源或样本至少保留：

```text
evidence_id
claim_or_signal
fact / inference / hypothesis
source_url
source_name
source_type
source_tier
country
category
language
published_date
retrieved_date
sample_size
time_range
original_text_or_metric
translation
coding_or_calculation
confidence
bias_or_limitation
next_validation
```

用户样本额外保留 `platform`、`content_type`、`rating`、`engagement`、`product_sku`、`scene`、`motivation`、`pain_point`、`desired_outcome`、`barrier`、`theme`。统计表额外保留 `n`、`denominator`、`ratio`、`platform_count` 和 `country_count`。
