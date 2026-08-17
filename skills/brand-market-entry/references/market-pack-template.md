# Market pack template

每个国家/地区应有一个独立 Market Pack。没有 Market Pack 时，只能做快速扫描，不得声称完成本地化深度研究。

```text
market-pack/<country-or-region>/
├── source-registry.md
├── platform-registry.md
├── language-keywords.md
├── regulation-registry.md
├── cultural-context.md
└── collection-notes.md
```

## Required fields

| 文件 | 必须记录 |
|---|---|
| source-registry | 机构、URL、来源类型、覆盖指标、更新时间、语言、权威性 |
| platform-registry | 平台、用户类型、内容类型、访问限制、商业/非商业属性 |
| language-keywords | 当地语言词、同义词、俚语、场景词、否定词、竞品词、翻译陷阱 |
| regulation-registry | 法规机构、法规版本、生效日期、适用品类、责任主体 |
| cultural-context | 只记录有来源的制度/文化背景，不写无证据的国民性格描述 |
| collection-notes | 查询日期、检索式、筛选规则、去重规则、失败来源和替代来源 |

Market Pack 要区分国家级事实、平台级事实和目标细分人群事实；不能用一个平台的用户语言代表整个国家。
