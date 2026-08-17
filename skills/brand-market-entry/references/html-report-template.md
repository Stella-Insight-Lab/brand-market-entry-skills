# HTML Report Template

生成 `report.html` 时使用单文件、离线可读结构。不要引入 Chart.js、Mermaid 或外部运行时；图表使用 inline SVG，数据和结论来自 `report.md` 与 `report-data.json`。

```html
<!doctype html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{{REPORT_TITLE}}</title>
  <style>
    :root{--bg:#F7F1E8;--surface:#FFFCF6;--ink:#2E2A24;--muted:#9B9185;--primary:#355C4A;--primary-soft:#E4EDE6;--accent:#B85C38;--accent-soft:#F3E2D7;--gold:#B0843A;--line:#E3D9C8;}
    *{box-sizing:border-box} body{margin:0;background:var(--bg);color:var(--ink);font:16px/1.75 -apple-system,BlinkMacSystemFont,"PingFang SC","Microsoft YaHei",sans-serif}
    .report{max-width:900px;margin:0 auto;padding:64px 24px}.cover{border-bottom:2px solid var(--primary);padding-bottom:24px}.summary{font-size:1.3rem;color:var(--primary)}
    .card{background:var(--surface);border:1px solid var(--line);border-radius:10px;padding:24px;margin:16px 0}.hero{background:var(--primary-soft);border-left:4px solid var(--primary)}
    .risk{background:var(--accent-soft);border:1px solid #E6C9B6;border-radius:10px;padding:24px}.source{font-size:.8rem;color:var(--muted);border-top:1px dashed var(--line);padding-top:4px}
    table{width:100%;border-collapse:collapse;margin:16px 0}th,td{border:1px solid var(--line);padding:8px 12px;text-align:left;vertical-align:top}th{background:var(--primary-soft);color:var(--primary)}
    @page{size:A4;margin:18mm}@media print{body{background:#fff}.card,.risk,table{break-inside:avoid}}
  </style>
</head>
<body><main class="report">
  <header class="cover"><h1>{{REPORT_TITLE}}</h1><p>{{RESEARCH_META}}</p><p class="summary">{{EXECUTIVE_SUMMARY}}</p></header>
  <section class="card hero"><h2>{{CORE_CLAIM}}</h2><p>{{CORE_SUPPORT}}</p><p class="source">{{CORE_EVIDENCE_NOTE}}</p></section>
  {{PILLARS_AND_TABLES}}
  <section class="risk"><h2>风险与不确定性</h2>{{RISKS}}</section>
  <details><summary>方法与来源</summary>{{APPENDIX}}</details>
</main></body></html>
```

`{{...}}` 仅是模板变量，交付前必须替换为真实内容；不得把变量原样留在最终报告。HTML 的主结论、机会、风险、行动和决策必须与 Markdown/JSON 一致。
