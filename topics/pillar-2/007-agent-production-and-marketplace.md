---
id: 007
title: "Agent能干活，也能赚钱了——两个信号说明 Agent 经济的完整回路已经出现"
pillar: 2
status: idea          # idea / drafting / ready / published / shelved
target_persona: B     # A / B / C / 多个
uiuc_anchor: false    # 是否打 UIUC 锚点
hook_type: insight    # insight / utility / story / data
created: 2026-06-12
updated: 2026-06-12
---

# Agent能干活，也能赚钱了——两个信号说明 Agent 经济的完整回路已经出现

## 一句话价值主张

两个独立的信号——Bun Jarred 演示 Agent 6 步开发闭环（生产端），x402 + HermesHub 实现 Agent 技能链上付费（流通端）——在 2026 年上半年同时出现。它们合在一起说明的不只是"Agent 很能干"，而是 Agent 经济从生产到交易的完整回路已经闭合。给 AI 从业者和 indie maker 的信号很明确：现在可以开始把 agent skill 当作可独立分发的资产了。

## 受众钩子

- **谁会转发**:
  - AI 从业者、Agent builder、开源工具链开发者，关心"Agent 下一步在哪"的人。
  - 独立创作者 / indie maker，正在探索"AI 技能怎么变现"的实操者。
  - 加密 / Web3 从业者，关注 HTTP 402 + 链上支付落地场景的人。

- **谁会收藏**:
  - 正在考虑把自己的 skill/工作流打包成可分发产品的人。
  - 想理解 Agent 经济基础设施（生产端 + 流通端）怎么做的人。
  - 关注 Bun / Jarred / Claude Dynamic Workflows / x402 生态的技术决策者。

- **谁会觉得"我以前不知道这个角度"**:
  - 以为 Agent 只是"更强的 AI 聊天"的人，没意识到 Agent 干活和 Agent 交易是两件独立的事。
  - 只看到 Bun Jarred demo 但没把它和"Agent 经济"连起来的人。
  - 以为 HTTP 402 只是一个冷门状态码，不知道它正在因加密支付和 Agent 浪潮复活的人。

## 核心论点 / 内容骨架

1. **引子：Jarred Sumner 那场没有胶片的演讲**

   Bun CEO Jarred Sumner 不用 PPT，全程跑 Agent workflow：
   复现 bug → 写测试 → 修复 → 提 PR → review → revise → merge。
   观众看到的不是演示，是 Agent 替代了一个完整开发循环。

   这不是"AI 辅助编程"，是 Agent 在台前独立完成工作。范式信号。

2. **生产端：Bun Jarred 的 6 步闭环回答了"Agent 能不能独立干活"**

   ```
   发现 → 理解 → 修复 → 提交 → 自审 → 合并
   ```

   每一步都有可验证的输出（测试结果、PR diff、review 记录）。
   关键不在于"用了什么模型"，而在于"workflow 编排的工程深度"。

   后续信号：Claude 的 Dynamic Workflows 本质上就是这场演讲的演进版——把这套流程形式化、可安装、可复用。

3. **流通端：x402 + Creator Marketplace 回答了"Agent 的技能能不能独立赚钱"**

   HTTP 402 状态码是 1999 年预留但从未激活的。现在因为加密支付（USDC 稳定币）+ Agent 的 MCP 工具发现协议，它正在复活。

   x402 的机制：客户端请求 → 服务端返回 402 + 支付要求 → 链上付 → 返回数据 / license key。
   整流嵌入普通 HTTP 往返，零支付中介。

   HermesHub（230⭐）的 creator marketplace ：
   - `GET /api/install` 收 0.01 USDC 起
   - 95% payout to crypto wallet（对比 App Store 70% / Stripe 2.9% + 0.3）
   - 自动安全扫描（65+ 规则）
   - Agent-to-Agent review（proof-of-use 信任分）

4. **二者合起来的逻辑：生产端 + 流通端 = Agent 经济的完整回路**

   | 环节 | Bun Jarred | x402 + Creator Marketplace |
   |---|---|---|
   | 解决的问题 | Agent 怎么干活 | Agent 活儿怎么交易 |
   | 价值环节 | **生产端** | **流通端** |
   | 基础设施 | 编程 agent + 测试框架 + PR 工具 | HTTP 402 + 加密钱包 + MCP 工具发现 |
   | 2026 状态 | 已成熟 | 早期（基金会刚迁，生态未稳）|

   **核心判断**：Agent 经济不缺"能跑"的 Agent，缺的是 Agent 干活之后——它产出的 skill、know-how、工作流——能不能被定价、分发、交易。

   就像有了工厂不代表有了经济。你还需要货币、市场、定价机制。

5. **为什么这件事值得写**

   Bun Jarred 的演讲发生在 2025 末。x402 的基金会搬迁发生在 2026 上半年。
   当这两个信号在同一年出现在同一个人视野里，说明它们不是孤例，是同一个趋势的两个侧面。

   趋势：Agent 从"能做什么"进入"靠什么运转"。

6. **对创作者的实操启示**

   - 已经有 skill 资产的人（skill、workflow、内容管线），不需要 Stripe / 银行账户 / 平台审核，可以用 x402 + hermes skills publish 直接分发。
   - 0 中介拿 95% 收入。
   - 不需要等"平台 build 好了再上"——404 状态码复活这件事，基础设施提供方和创作者是同步发现的。

7. **风险与未完成**

   - x402 生态目前还很薄。HermesHub 只有 22 个 skill（不是推文宣称的 691）。
   - 加密支付对普通用户的摩擦仍然高。
   - Bun Jarred 的 workflow 能否泛化到编程之外的场景，尚未被验证。
   - 这些判断的保质期很短——6-12 个月内要么被验证要么被推翻。

## 关键素材 / 信源

- [x] @MinLiBuilds 推文（199❤️，2026-06-04）：Bun Jarred 演讲的社区二手描述
- [ ] Bun CEO Jarred Sumner 原始演讲视频/记录（需确认是否有公开录制）
- [x] Claude Dynamic Workflows 官方介绍 + `lxcong/awesome-claude-dynamic-workflows`（14⭐）
- [x] x402-foundation/x402 GitHub：协议 repo + SDK 文档
- [x] `amanning3390/hermeshub`（230⭐）：creator marketplace 实测
- [x] Coinbase / Hyperbolic / Jatevo / AnkanMisra 等已接入 x402 的项目
- [x] inbox/2026-06.md（2026-06-06 14:30 条目）：x402 原始素材
- [x] posts/long-form-assessment.md（183-295 行）：Bun Jarred + x402 的完整评估
- [x] RFC 2616 Section 10.4.3：HTTP 402 原始定义（1999）
- [x] Coze "公众号标题生成" skill 两轮标题优化（2026-06-12，session `7647332715779539250`）：已验证标题方向，首推"Agent能干活，也能赚钱了"

## 风险与避坑

- 不要写成纯技术教程。文章是"判断 + 叙事"，不是讲 Bun 怎么配 Dynamic Workflow 或 x402 SDK 怎么调。
- 不要忽视加密支付对非加密用户的摩擦。承认这个摩擦，比假装它不存在更可信。
- 不要把两个案例拼成"什么都好"的宣传稿。它们是信号，不是成熟生态。该写的不确定性要写。
- 不要写成加密文章。x402 是支付层，不是"AI × Crypto"叙事。主语是 Agent 经济，加密是中性的基础设施。
- 不要写成开发者专属内容。要解释 HTTP 402 为什么"沉睡 30 年"才复活，让非技术读者也能理解为什么时机对了。
- 不要把 Bun Jarred 和 x402 写成同一个团队或同一个项目的事。它们是独立信号，合在一起才有判断力。

## 形式

- 主战场: 公众号
- 同步: X / Substack 精简版 / 小红书(可选)

公众号长文建议标题（经 Coze "公众号标题生成" skill 两轮优化，第二轮去除"造车"隐喻）：

| # | 标题 | 指数 |
|---|------|------|
| **1** | **Agent能干活，也能赚钱了：两个信号说明经济闭环已经出现** | ⭐5 |
| 2 | 一个沉睡30年的HTTP状态码，突然成了Agent的赚钱工具 | ⭐5 |
| 3 | Agent自己写代码、自己收钱：开发闭环和支付闭环同时被打通了 | ⭐5 |
| 4 | Agent不再只是工具：它开始自己生产、自己交易了 | ⭐4 |
| 5 | Bun创始人演示Agent独立完成6步开发，同一天Agent技能开始链上付费交易 | ⭐4 |
| 6 | 当Agent既能生产又能流通，"Agent经济"就不再是概念了 | ⭐4 |
| 7 | 402状态码沉睡30年后，被Agent激活成了支付协议 | ⭐4 |
| 8 | Agent经济的两块拼图：一块能写代码，一块能收钱 | ⭐4 |
| 9 | Agent能独立交付、能独立收款：给indie maker的信号很明确 | ⭐4 |
| 10 | AI闭环不只是"能干活"：Agent技能已经开始在链上卖钱了 | ⭐3 |

首推标题 1（结论直给，最平衡）或标题 2（好奇心钩子最强）。两轮之间的 A/B 测试：标题 1 走「结论直给」，标题 2 走「悬念钩子」。

X 线程角度：
- Bun 创始人不用 PPT，全程跑 Agent 6 步闭环。这不是 AI 辅助编程，是 Agent 独立完成工作。
- x402 让 HTTP 402（1999 年预留但从未激活）因加密支付复活。Agent 现在可以用这个协议付费获取技能。
- 一个解决"Agent 怎么干活"（生产端），一个解决"Agent 的技能怎么交易"（流通端）。两者拼起来 = Agent 经济的完整回路。
- Agent 经济不缺能跑的 Agent，缺的是它产出的东西能不能被定价、分发、交易。

小红书角度：
- 《为什么说 Agent 不只是能干活，还得能挣钱》
- 《别人看到两个独立新闻，我看到同一张拼图》
- 《如果 Agent 能自己写代码，那它能不能自己收钱？》

## 与 005 的关系
007 和 005 同属**意见型文章**路径，互为补充：

- **005（平台型 vs 工具型 agent）**：回答"工具型 agent 凭什么不被平台吃掉"——讲的是终局判断、定位问题。
- **007（Agent 经济的完整回路）**：回答"工具型 agent 正在具体做什么"——讲的是当下的活案例、正在发生的信号。

两篇都在论证同一个底层命题——工具型 agent 不是过渡，是独立赛道。005 给框架（为什么），007 给证据（是什么）。阅读建议：可独立读，但 005→007 阅读顺序更自然——先认同"工具型 agent 有位置"，再看到"这个位置正在被什么填满"。

## 写作过程记录

- **标题优化**：通过 Coze "公众号标题生成" skill 进行两轮迭代（2026-06-12）。一轮含"造车"隐喻被否定 → 二轮去除后产出 10 个标题。首推"Agent能干活，也能赚钱了：两个信号说明经济闭环已经出现"（⭐5）。过程已封入 `content-coze-skill-distill-template` v2.0 的路径 B 案例。
- **核心概念迭代**："造车阶段"→"Agent经济的完整回路"→最终确定"生产端 + 流通端 = Agent 经济回路"。概念本身需要先被读者听懂再被记住，所以选"干活"和"赚钱"这两个所有人都能秒懂的词。

## 发布后记录

- published_url:
- published_at:
- 数据(发布 7 天): 阅读 / 在看 / 转发 / 关注转化
- 复盘:
