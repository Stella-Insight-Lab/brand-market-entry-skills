# Brand Market Entry Skills

用于品牌进入海外国家或区域前的市场、用户文化与法规研究。它把公开数据、当地语言用户内容、法规来源和结构化证据台账组织成一份可追溯的专业研究报告。

## What it does

- 按国家/地区与品类选择不同的数据来源、指标、样本配额和法规问题。
- 将市场机会、用户需求/文化和法规/进入约束作为三条并行证据线。
- 对用户评论、论坛、社媒和问答保留原文，记录直译、语义解释、文化背景、编码和频次统计。
- 通过假设台账、支持/反证、替代解释、市场测算和敏感性分析，避免从“有数据”直接跳到“有结论”。
- 先生成结构化表格，再形成叙述性结论；数据不足时输出缺口，不用模型推断填补。
- 分阶段写入 Markdown、CSV、JSON 和 HTML；每阶段经过 Gate 后才进入下一阶段，支持暂停、恢复和单模块重跑。
- 最终合并为 `report.md`、`report.html` 和 `report-data.json`，并保留市场、用户文化、法规三条证据线及冲突记录。

V1 内置品类：美妆个护、包装食品/饮料、消费电子/小家电。其它品类可沿用同一字段扩展 category pack。

## Skills

| Skill | 用途 |
|---|---|
| `brand-market-entry` | 默认入口：收集 brief、选择适配器、编排全流程和生成最终报告 |
| `market-regulatory-entry` | 市场规模、需求、竞品、价格、渠道、单位经济和法规进入要求 |
| `user-cultural-insight` | 用户内容采集、原文保留、编码统计、语言文化解释和用户证据表 |
| `market-entry-synthesis` | 合并证据包、检查冲突与缺口、横向比较并生成决策建议 |

## Install

安装默认入口：

```bash
npx skills add <owner>/brand-market-entry-skills --skill brand-market-entry --agent codex --global --yes
```

安装全部 Skill：

```bash
npx skills add <owner>/brand-market-entry-skills --skill '*' --agent codex --global --yes
```

按需安装模块：

```bash
npx skills add <owner>/brand-market-entry-skills --skill market-regulatory-entry --agent codex --global --yes
npx skills add <owner>/brand-market-entry-skills --skill user-cultural-insight --agent codex --global --yes
npx skills add <owner>/brand-market-entry-skills --skill market-entry-synthesis --agent codex --global --yes
```

将 `<owner>` 替换为实际 GitHub 用户名或组织名。也可以下载仓库后，把需要的 `skills/<skill-name>/` 目录复制到兼容 Agent Skills 的目录。

## Expected research output

默认入口会创建以下阶段目录，Markdown 用于解释，CSV/JSON 用于可复查数据，HTML 用于分享/打印：

```text
market-entry-project/
├── 00-brief/
├── 01-research-design/
├── 02-market-competition/
├── 03-user-cultural/
├── 04-regulatory-entry/
├── 05-evidence-synthesis/
├── 06-final-report/
└── runs/<timestamp>/        # 只重跑某阶段时保存新版本
```

阶段文件和 Gate 规则见 `skills/brand-market-entry/references/`。默认输出包括：

| 阶段 | 关键产物 |
|---|---|
| Brief | `research-brief.md` + `research-brief.json` |
| 研究设计 | `research-outline.md` + `source-registry.csv` + `data-quota.csv` |
| 市场/竞品 | `market-pack.md` + `market-metrics.csv` + `competitor-matrix.csv` + `channel-map.csv` |
| 用户/文化 | `user-cultural-insight.md` + `ugc-coding.csv` + `persona-matrix.csv` + `jtbd-map.md` |
| 法规/进入 | `regulatory-entry.md` + `regulatory-matrix.csv` + `data-flow-map.md` |
| 证据综合 | `evidence-ledger.csv` + `decision-matrix.md` + `assumption-register.md` + `contradiction-log.md` + `falsification-log.md` |
| 总报告 | `report.md` + `report.html` + `report-data.json` |

## Staged usage

```text
请运行品牌出海市场进入研究：
品类：安防摄像头
国家：越南
目标用户：家庭、小微商户
研究深度：标准
输出：按阶段执行，每阶段先给我中间产物，我回复“继续”后再进入下一阶段
```

用户回复 `继续` 会确认最近一个 Gate 并推进；回复 `重跑用户模块` 或 `补法规` 会在 `runs/<timestamp>/` 中生成新版本，不覆盖已有证据。

完整示例见 `examples/vietnam-security-camera/`。

用户内容比例只表示当前采集样本中的分布，不自动代表国家总体。公开内容采集必须遵守来源平台条款、隐私要求、版权边界和合理访问频率。专业研究还应保留假设台账、反证记录、冲突记录和市场测算公式。

## Scope and disclaimer

本项目是研究工作流与证据组织工具，不提供正式法律意见、认证承诺或监管机构判断。法规结论应回到目标市场的官方法规库、监管机构、海关、认证机构或当地专业顾问复核。

## License

MIT License. 详见 `LICENSE`。
