# Market sizing and scenario models

## 1. Define the market before estimating it

记录品类边界、产品形态、渠道范围、线上/线下、sell-in/sell-out、名义/实际金额、币种、基准年、预测年和是否含税。不同定义不能被平均成一个数字。

## 2. Use three models when data permits

### Top-down

```text
总消费市场 × 目标品类占比 × 目标人群占比 × 目标价格/渠道可服务比例
```

### Bottom-up

```text
目标用户数 × 品类渗透率 × 年购买频次 × 平均成交价
```

### Proxy-based

搜索量、平台 SKU/评价量、排名、渠道覆盖和广告信号可用作需求代理，但不等同于市场规模。必须标记 `proxy_signal`。

## 3. TAM / SAM / SOM

| 层级 | 定义 | 必须说明 |
|---|---|---|
| TAM | 理论总需求 | 是否包含不可服务人群 |
| SAM | 产品、价格、渠道和法规可服务的需求 | 排除了什么 |
| SOM | 在资源、竞争和进入方式约束下可获得的份额 | 是目标还是预测 |

## 4. Scenarios and sensitivity

至少给出基准、上行、下行三种情景；对渗透率、价格、渠道转化、汇率、履约成本、退货率和法规成本做敏感性分析。没有输入数据时保留变量，不得生成看似精确的毛利或市场份额。

每个市场估算表必须有 `formula`、`assumption_ids`、`double_count_check`、`low/base/high`、`currency_basis` 和 `confidence`。
