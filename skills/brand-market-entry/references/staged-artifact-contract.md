# Staged Artifact Contract

本文件定义 `brand-market-entry` 的阶段文件、元数据和交接字段。编排器必须先检查上游 artifact，再生成下游内容。

## Common metadata

所有 Markdown 阶段文件开头必须包含 YAML 元数据：

```yaml
project_id: vietnam-security-camera
stage: "00"
status: draft|gate_ready|confirmed|blocked|pending-review
executed_at: 2026-08-17T00:00:00+08:00
research_window: 2025-01-01/2026-08-17
country_or_region: Vietnam
category: security-camera
source_mode: primary|secondary|public-fragment|mixed
confidence: high|medium|low
upstream_artifacts: []
```

CSV/JSON 文件必须至少包含对应 metadata 字段，或与同阶段 Markdown 文件通过 `artifact_id` 关联。

## Required structured fields

证据、指标、原始内容、法规和决策表至少保留：

`record_id, claim_or_observation, source_id, source_type, language, captured_at, sample_or_scope, confidence, limitation`

可按模块增加字段，但不得删除上述字段。比例必须注明分母；估算必须注明公式、口径和情景；用户内容必须保留原文与直译。

## Stage artifact map

| Stage | 目录 | 必需文件 | 下游消费者 |
|---|---|---|---|
| 00 | `00-brief/` | `research-brief.md`, `research-brief.json` | 所有阶段 |
| 01 | `01-research-design/` | `research-outline.md`, `source-registry.csv`, `data-quota.csv` | Stage 2–4 |
| 02 | `02-market-competition/` | `market-pack.md`, `market-metrics.csv`, `competitor-matrix.csv`, `channel-map.csv` | Stage 4–6 |
| 03 | `03-user-cultural/` | `user-cultural-insight.md`, `ugc-coding.csv`, `persona-matrix.csv`, `jtbd-map.md` | Stage 5–6 |
| 04 | `04-regulatory-entry/` | `regulatory-entry.md`, `regulatory-matrix.csv`, `data-flow-map.md` | Stage 5–6 |
| 05 | `05-evidence-synthesis/` | `evidence-ledger.csv`, `decision-matrix.md`, `assumption-register.md`, `contradiction-log.md`, `falsification-log.md` | Stage 6 |
| 06 | `06-final-report/` | `report.md`, `report.html`, `report-data.json` | 用户交付 |

## Status rules

- `draft`: 文件存在但仍在编辑；不可作为下游唯一依据。
- `gate_ready`: 本阶段文件齐全、质量检查完成，等待用户确认。
- `confirmed`: 用户确认后可被下游使用。
- `blocked`: 缺文件、关键数据不足或用户要求暂停；不得继续下游。
- `pending-review`: 存在法规或专业判断未决项；可继续做非结论性整理，但不得输出确定性 `GO`。

## Evidence downgrade

当目标样本量未达配额时，必须在 Markdown、CSV/JSON metadata 和 Gate 摘要中同时写明：

1. 有效样本量与目标样本量；
2. `source_mode: public-fragment` 或 `mixed`；
3. 被跳过或降级的模块；
4. 对结论置信度和最终决策的影响。

不得把平台挂牌、供应商主张、单条评论或搜索结果数量当作总体市场规模、用户比例或付费意愿。
