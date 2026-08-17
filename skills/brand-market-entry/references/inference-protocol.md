# Inference protocol

## Required reasoning chain

Do not move from a data table directly to a recommendation. For every material decision, build:

```text
decision_question
→ hypothesis
→ required evidence
→ collection / calculation
→ supporting evidence
→ contradicting evidence
→ alternative explanations
→ falsification condition
→ bounded conclusion
→ decision impact
```

## Claim levels

| Level | Meaning | Allowed wording |
|---|---|---|
| Observation | Directly seen in a source or sample | “样本中出现……” |
| Pattern | Repeated observation within a defined sample | “在本次样本中，……占……” |
| Inference | Interpretation supported by multiple signals | “证据支持……可能……” |
| Hypothesis | Plausible but unconfirmed explanation | “待验证假设……” |
| Recommendation | Decision under stated assumptions | “在……条件下建议……” |

## Required anti-confirmation check

每个重要假设都要主动寻找反证。不能只收集支持卖点的评论；要采集低评分、替代方案、放弃购买、退货、法规限制和竞品失败信息。若反证无法排除，降低置信度或把结论改为 HOLD。

## Claim card

```text
claim_id
decision_question
hypothesis
required_evidence
supporting_evidence_ids
contradicting_evidence_ids
alternative_explanations
falsification_condition
assumptions
conclusion_level
confidence
decision_impact
```

如果一个结论不能填写 `falsification_condition`，通常说明它仍是观点或叙事，而不是可检验结论。
