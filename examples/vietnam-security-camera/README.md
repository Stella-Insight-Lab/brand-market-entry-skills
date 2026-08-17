# Vietnam Security Camera Example

这个示例只演示如何调用分阶段工作流，不包含预先写好的市场结论。

## Prompt

```text
请运行品牌出海市场进入研究：
品类：家庭和小微商户 Wi-Fi/IP 安防摄像头
国家：越南
目标用户：家庭照护者、单店/小办公室经营者
进入方式：本地经销/官方电商店/可选安装服务，尚未确定
研究深度：标准
重点：市场规模与价格、越南语用户内容、家庭与商户分层、QCVN 135、个人数据、Cloud/SD、渠道责任
输出：按阶段执行，每阶段生成 Markdown + CSV/JSON；我回复“继续”后再进入下一阶段；最后生成 Markdown + HTML + JSON 总报告
```

## Expected project tree

```text
vietnam-security-camera/
├── 00-brief/research-brief.md
├── 00-brief/research-brief.json
├── 01-research-design/research-outline.md
├── 01-research-design/source-registry.csv
├── 01-research-design/data-quota.csv
├── 02-market-competition/market-pack.md
├── 02-market-competition/market-metrics.csv
├── 02-market-competition/competitor-matrix.csv
├── 02-market-competition/channel-map.csv
├── 03-user-cultural/user-cultural-insight.md
├── 03-user-cultural/ugc-coding.csv
├── 03-user-cultural/persona-matrix.csv
├── 03-user-cultural/jtbd-map.md
├── 04-regulatory-entry/regulatory-entry.md
├── 04-regulatory-entry/regulatory-matrix.csv
├── 04-regulatory-entry/data-flow-map.md
├── 05-evidence-synthesis/evidence-ledger.csv
├── 05-evidence-synthesis/decision-matrix.md
├── 05-evidence-synthesis/assumption-register.md
├── 05-evidence-synthesis/contradiction-log.md
├── 05-evidence-synthesis/falsification-log.md
└── 06-final-report/report.md + report.html + report-data.json
```

## Rerun examples

```text
重跑用户模块：补充越南语论坛、电商评价，保持市场与法规原版本不变。
补法规：只更新越南目标 SKU 的法规矩阵和数据流图，再重新生成证据综合。
回看市场：只展示市场包、竞品矩阵和价格口径，不进入下一阶段。
```
