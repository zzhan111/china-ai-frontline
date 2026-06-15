---
id: 009
title: "中美 AI 制造平台差了一个 Xometry：为什么中国跑不出全球级 asset-light 按需制造 marketplace？"
pillar: 4
secondary_pillar: 2
status: drafting
target_persona: B
uiuc_anchor: false
hook_type: insight
role: "作为 007 Agent 经济回路文章的中美产业对照案例——Xometry 证明了 AI 把工程师知识工作 API 化可以跑通，但不是 agent 经济。中国有玩家但缺了三个结构性条件。"
status: published
created: 2026-06-15
updated: 2026-06-27
published_url: https://mp.weixin.qq.com/s/3d1H48bbVu_BuVBwJbv0KA
published_title: "12年亏出来的护城河：Xometry如何用AI把工程师经验变成印钞机"
data_windows:
  - "2026-06-15 SEC EDGAR 直接抓取 — Xometry 10-K 2025 + S-1 2021 + Q1 2026 10-Q"
  - "2026-06-15 官网抓取 — Protolabs 10-K 2025 / Fast Radius 10-K 2021 (已退市) / Fictiv.com / Hubs(Protolabs Network) / Rapiddirect.com / 嘉立创 5 个子站"
---

# 中美 AI 制造平台差了一个 Xometry

> 触发：china-ai-frontline/inbox/2026-06.md 第 587-651 行（"AI 驱动产业平台"选题的主动扩展）
> 调研产物：`~/research/xometry/REPORT.md`（22.8KB，9 章节，52MB 原始素材）
> 标题备选：「为什么中国跑不出全球级 AI 制造平台」「Xometry：AI 制造平台的正确打开方式」「差了一个 Xometry」

## 一句话价值主张

**Xometry 是全球第一个跑通"AI 即时报价 + 全球供应商网络"的 industrial marketplace——2025 年营收 $686.6M（+26%）、1.65 亿零件出货——但它的护城河不是 AI 算法，是 10 年累积的"CAD 模型 × AI 报价 × 实际生产"配对数据。中国有 RapidDirect / 嘉立创在做同样的事，但跑不出全球级 + asset-light + 上市公司版本，根本原因不是技术，是数据共享 + 客户信任 + 资本市场三个结构性约束。**

## 受众钩子

- **谁会转发**：
  - AI 从业者 / Agent builder，关心"AI 在制造业到底跑通了什么"
  - 制造业从业者 / 工业互联网创业者，想理解"中国为什么没有 Xometry"
  - 中美科技观察者，关心"为什么同一个赛道中美不同命"

- **谁会收藏**：
  - 正在考虑做 B2B 制造平台的创业者（Xometry 的财务模型和竞争格局是参考标杆）
  - 关注 AI agent 经济的投资人（Xometry 是"非 agent 但 AI 驱动"的对照案例）
  - 做中美产业对比的研究者（数据翔实，来源可验证）

- **谁会觉得"我以前不知道这个角度"**：
  - 以为"中国制造业数字化领先美国"的人（实际中国在 CNC/注塑这类非标工艺的 AI 报价上落后）
  - 以为"AI agent 经济是下一波"的人（Xometry 证明 AI 工具链标准化可能更早跑通）

## 核心论点 / 内容骨架

### 论点 1：Xometry 跑通了，但靠的不是 AI 算法

- **数据**：2025 Revenue $686.6M（+26%），Marketplace $629.6M（+30%），81,821 Active Buyers，4,996 Active Suppliers，165M+ Parts Shipped 累计
- **毛利率扩张路径**：Marketplace gross margin 从 2018 17% → 2020 24% → 2024 33.5% → 2025 34.7%
- **商业模式真相**：Xometry 不是"制造业 Uber"，而是以卖家身份和买家成交再向 supplier 采购——自己承担库存和品质风险，赚价差（不是抽佣）
- **护城河 = 配对数据**：1.65 亿零件的"CAD × AI 报价 × 实际生产"数据集，10 年不可压缩的时间函数
- **信源**：SEC EDGAR 10-K 2025 + S-1 2021

### 论点 2：赛道上的竞争者验证了一个规律——pure marketplace 是唯一规模化路径

| 公司 | 模式 | 2025 营收 | 增速 | 净利润 | 关键事件 |
|---|---|---|---|---|---|
| Xometry | Pure marketplace | $686.6M | +26% | 净亏损（收窄中）| 13 年，1.65 亿零件 |
| Protolabs | Hybrid（自有工厂+收购 Hubs）| $533.1M | +6% | +$21.2M（盈利）| 27 年，增速触顶 |
| Fast Radius | Hybrid（自有微工厂）| — | — | $(67.9)M (2021) | **2022 退市/破产** |
| Fictiv | Hybrid | — | — | — | 私募，6,000+ companies |

- **规律**：pure marketplace 牺牲短期毛利率换长期增速，hybrid 盈利但增速触顶，hybrid+微工厂直接破产
- **信源**：Protolabs 10-K 2025 / Fast Radius 10-K 2021 / Fictiv 官网

### 论点 3：中国不是没人做——是有玩家但跑不出全球级上市公司

- **嘉立创集团**（5 个子站：JLCPCB / JLCSMT / JLCCNC / JLC3DP / JLCFA）：PCB 标准化工艺 + 参数化报价，集团化运营，但 CNC/注塑仍在参数化阶段（不是 ML 几何特征识别）
- **RapidDirect**（rapiddirect.com）：2017 创立，700+ 供应商，20,000+ 全球客户，120+ 国家——和 Xometry 几乎相同的叙事，但主打全球英语客户，不在中国本土获客
- **inbox 列的 4 家公司有 3 家已死**：云工厂（域名失效）、未来工场（DNS 失败）、速加网（域名被抢注）

### 论点 4：三个结构性约束解释了中美的"同赛道不同命"

| 约束 | 美国 | 中国 |
|---|---|---|
| **数据共享** | 标准化报价数据可沉淀（NDA + 数字化采购成熟）| 工厂报价数据分散 + 不标准化 + 不共享 |
| **客户信任** | 平台 API 集成 + Enterprise onboarding 成熟 | 关系型供应链，看厂验货文化 |
| **资本市场** | SPAC / IPO 渠道畅通，支持长期亏损换增长 | VIE 架构限制 + 中美紧张 + 盈利要求 |

### 论点 5：Xometry 和 007 Agent 经济回路的交叉点

- **Xometry 不是 agent 经济案例**：它是 ML pipeline（CAD → 几何特征 → 报价），不是 LLM agent
- **但它是 agent 经济的前身**：把"工程师的知识工作（读 CAD 报价）"做成了 API——这是 agent 工具链标准化的极致案例
- **对比启示**：AI 在"必需确定性结果的 B 端场景"下也能跑通，但要求训练数据足够大 + ML 模型足够准 + 流程容错性低
- **和 007 选题呈对照关系**：007 讲 Agent 经济回路（生产+流通闭合），009 讲 AI 工具链标准化（非 agent 但同样有经济回路）

## 关键素材 / 信源

- [x] Xometry 10-K 2025-12-31（$686.6M revenue / 81,821 Buyers / 34.7% mkt margin）
- [x] Xometry S-1 2021-06-04（2018-2020 CAGR 92% / 6M+ parts / 30% Fortune 500）
- [x] Xometry 10-Q 2026-03-31（Q1 2026 $205.1M revenue +36% / net loss $(5.3)M）
- [x] Xometry 官网 About（85,000+ Buyers / 165M+ Parts / 1,500+ Team Members）
- [x] Protolabs 10-K 2025-12-31（$533.1M revenue +6% / 48,415 customer contacts / 60 patents）
- [x] Fast Radius 10-K 2021-12-31（$(67.9)M net loss / 退市 25-NSE 2022-12-21）
- [x] Fictiv 官网（42M+ parts / 6,000+ companies / 5 supply regions）
- [x] 嘉立创 5 个子站（JLCPCB / JLCSMT / JLCCNC / JLC3DP / JLCFA）
- [x] RapidDirect 官网（700+ suppliers / 20,000+ customers / 120+ countries / No minimum order）
- [x] Wayken / SR MFG / Made-in-China / 黑湖智造 / 京东工品汇 / 震坤行 — 验证非直接竞品
- [ ] ~~Xometry engineering blog 详细页（machine-learning / instant-quoting-engine 404）~~ — 10-K Item 1 Business 提供等效内容
- [ ] ~~Xometry IR / 8-K earnings calls~~ — 超时，待 WSL 网络恢复后补

## 风险与避坑

- **避坑"AI 万能论"**：Xometry 的成功不是"AI 颠覆制造业"，而是"10 年数据积累让 ML 报价足够准"。不要写成 AI 叙事软文。
- **避坑"中国落后论"**：嘉立创和 RapidDirect 已经在做，不是落后，是路径不同。准确说"中国没有跑出全球级 + asset-light + 上市公司"，而非"中国没有 AI 制造平台"。
- **数据口径一致性**：Active Buyers 81,821（10-K LTM 12 个月）≠ 官网 85,000+（可能是累计口径）。引用时要标注来源和口径差异。
- **时效性**：调研基于 2026-06-15 的 SEC 文件，如果文章在 2 个月后发布需更新 Q2 2026 数据。
- **inbox 过时数据需修正**："几十万笔交易训练出来的报价模型" → 应为 1.65 亿+ Parts Shipped（累计）+ hundreds of millions of data inputs（per 10-K）。

## 形式

- 主战场：公众号长文（drafts/009/）— 2,500-3,000 字，对比叙事 + 数据驱动
- 同步：X thread（6-8 条，核心数据切片）、小红书（对比矩阵图 + 洞察卡片）
- 子用途：007 Agent 经济回路文章的产业对照章节（约 500 字压缩版）

## 发布后记录

- published_url:
- published_at:
- 数据（发布 7 天）：阅读 / 在看 / 转发 / 关注转化
- 复盘：
