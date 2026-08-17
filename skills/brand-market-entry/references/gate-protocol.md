# Gate Protocol

## Gate sequence

| Gate | After | User confirms | Next |
|---|---|---|---|
| Gate 0 | Brief | 品类、国家、用户、研究深度 | Stage 01 |
| Gate 1 | Research design | 问题树、来源、样本配额 | Stage 02–04 |
| Gate 2 | Market pack | 市场口径、竞品、渠道范围 | Stage 03/04 或补采 |
| Gate 3 | User-cultural pack | 用户分层、文化解读、JTBD、样本限制 | Stage 05 |
| Gate 4 | Regulatory pack | 硬门槛、适用性假设、待专业复核项 | Stage 05 |
| Gate 5 | Evidence synthesis | 综合判断、机会优先级、决策条件 | Stage 06 |
| Gate 6 | Final report | 最终交付检查 | 完成 |

## Dialogue behavior

- 阶段结束：先写产物，再输出 3–5 条关键发现、有效样本量、置信度、缺口和确认选项。
- 用户回复 `继续`：确认最近一个 `gate_ready` 阶段并进入下一个阶段。
- 用户回复 `回看市场`、`回看用户` 或 `回看法规`：只展示指定阶段的摘要与文件入口，不重跑其他阶段。
- 用户回复 `重跑用户模块`、`补法规`：复制当前项目状态到 `runs/<timestamp>/`，只重跑指定阶段及其下游综合；原始版本不覆盖。
- 用户回复 `暂停`：保存当前状态为 `blocked`，列出恢复所需文件或选择。
- 用户未确认：不得把下一阶段内容混入当前 Gate 输出。

## Blocking rules

1. 上游必需文件缺失时，停止并列出文件路径。
2. 法规关键适用性未决时，状态使用 `pending-review`，不得给确定性 `GO`。
3. 目标样本量不足时，可以输出降级证据包，但不得伪造代表性、比例或趋势。
4. 来源冲突必须写入 `contradiction-log.md`，最终报告保留口径差异。
5. 最终报告必须回链 `evidence-ledger.csv`；没有证据链接的主结论降级为假设或删除。
