# Stage Output Templates

这些模板规定每个阶段先输出什么文件。阶段结束后再给对话框输出 Gate 摘要，不把完整表格塞进对话框。

## Stage 00 — `research-brief.*`

```yaml
project_id: <slug>
brand_or_company: <name>
category: <specific category>
country_or_region: <target>
target_users: []
price_band: <local currency or unknown>
entry_mode: <cross-border|distributor|marketplace|local entity|unknown>
research_depth: quick|standard|deep
research_window: <date range>
existing_materials: []
constraints: []
open_questions: []
```

Markdown must explain the business decision in 2–5 sentences and list out-of-scope questions.

## Stage 01 — `research-outline.md`, `source-registry.csv`, `data-quota.csv`

Markdown must contain：问题树、假设、模块边界、语言/平台要求、来源层级、时间范围、停止条件和 Gate 1 confirmation prompt。

`source-registry.csv` fields：`source_id,url,source_type,authority,language,access_date,coverage,planned_use,known_bias,status`。

`data-quota.csv` fields：`module,hypothesis,source_family,target_n,minimum_n,actual_n,unit_definition,language_required,stop_condition,status`。

## Stage 02 — market pack

`market-metrics.csv` fields：`record_id,metric,value,unit,scope,year,method,formula,assumption,scenario,source_id,confidence,limitation`。

`competitor-matrix.csv` fields：`record_id,brand,sku,segment,price,currency,channel,features,localization,storage,service,regulatory_claim,captured_at,source_id,confidence,limitation`。

`channel-map.csv` fields：`record_id,channel,role,customer_segment,entry_requirement,service_capability,cost_signal,source_id,confidence,limitation`。

`market-pack.md` must separate observed data, estimates, interpretations, decision implications and missing data.

## Stage 03 — user and cultural pack

`ugc-coding.csv` fields：`content_id,country,platform,url,date,language,sku,raw_text,literal_translation,semantic_interpretation,cultural_context,cn_difference,scene,motivation,pain,desired_outcome,barrier,emotion,theme,interaction,sample_status,source_id,confidence,limitation`。

`persona-matrix.csv` fields：`segment_id,segment_name,source_n,platform_n,scene,job,emotional_job,hiring_criteria,language_signal,cultural_signal,price_signal,confidence,limitation`。

`jtbd-map.md` must use：`When [situation], I want to [motivation], so I can [outcome]` and include struggling moment, functional job, personal/social emotional job, hiring criteria, current solution, failure point, progress metric and one non-obvious alternative direction.

`user-cultural-insight.md` must distinguish user evidence, seller claims, researcher interpretation and recommendation. A single expression is an anecdote, not a population finding.

## Stage 04 — regulatory pack

`regulatory-matrix.csv` fields：`record_id,jurisdiction,requirement,applies_if,product_scope,device_firmware_app_cloud_mapping,responsible_party,required_action,official_source,effective_date,cost_or_time,status,risk,confidence,limitation`。

`data-flow-map.md` must cover collection, processing, storage, transfer, access, deletion, incident response and responsible parties. Unresolved legal applicability uses `pending-review`.

## Stage 05 — synthesis pack

`evidence-ledger.csv` fields：`claim_id,claim,claim_type,支持_source_ids,contradicting_source_ids,source_count,sample_scope,confidence,applicability,remaining_uncertainty,decision_impact`。

`decision-matrix.md` must contain：market structure, user/Job fit, regulatory hard gates, channel/unit economics, opportunity priority, decision outcome and evidence conditions.

`assumption-register.md` records every unresolved assumption with owner, impact, falsification condition, minimum next data and current status.

`contradiction-log.md` records conflicting numbers, populations, platforms or legal interpretations without silently averaging them.

`falsification-log.md` records for each major hypothesis：what would disprove it, what was checked, what remains untested, and the next minimum data requirement.

## Stage 06 — final pack

`report-data.json` must expose：`project`, `executive_summary`, `pillars`, `segments`, `opportunities`, `risks`, `actions`, `decision`, `evidence_links`, `sources`, `limitations`。

`report.md` and `report.html` must be content-equivalent at the conclusion level. The HTML is a presentation layer, not a second analysis.
