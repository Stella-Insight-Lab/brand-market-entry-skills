# Final Report Contract

## Required narrative structure

最终报告采用结论先行结构，最多 7 个 H2：

1. 核心论点；
2. 支撑判断一；
3. 支撑判断二；
4. 支撑判断三；
5. 机会与行动；
6. 风险与不确定性；
7. 附录与来源。

执行摘要、市场/用户/法规证据、机会地图、决策门和方法论属于上述 H2 下的内容块，不单独扩张为 10+ 个并列章节。

## Claim traceability

每条主结论必须带：`claim_id`、支持 source IDs、反证/冲突 source IDs、样本或口径、置信度、适用范围和剩余不确定性。建议写法：

```markdown
结论句。

> 证据来源 · claim_id C-03 · source_ids S-01,S-08 · 样本/口径 · ... · 置信度 · 中 · 局限 · ...
```

## Required visuals and tables

- 市场规模/口径或价格带图；
- 人群 × Job/场景矩阵；
- 机会地图；
- 证据强度或决策门表；
- 行动路线图：行动、Owner、资源、领先 KPI、决策门、前置依赖。

HTML 必须离线可读，视觉层与内容同源，不使用外部 JS 图表库。若没有可比数字，展示区间、空白和口径说明，不伪造精确图形。
生成结构加载 `html-report-template.md`；交付前不得保留 `{{...}}` 模板变量。

## Required decision outcomes

最终报告只能使用：`GO`、`NARROW`、`HOLD`、`PIVOT`、`NO-GO`。法规待复核或单位经济未成立时，必须在决策门中写清触发条件，不得用模糊的“建议关注”。

## Quality checks

- Markdown/HTML 主结论一致；
- H2 不超过 7 个；
- 每条主结论可回链 evidence ledger；
- 事实、估算、解读、建议分层；
- 公开用户样本不写成人口代表性；
- 法规结论标注法律意见边界；
- 结构化 `report-data.json` 与正文机会/风险/行动一致。
