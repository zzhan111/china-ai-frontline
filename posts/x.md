# X drafts

## post-2026-05-24-001：缺乏的不是想象力，而是执行力

状态：draft
来源：inbox/2026-05.md#2026-05-24-21-25
首发平台：X
audience：AI builder + 独立创作者（海外华人 tech 圈层）
是否升级长文：待观察

### 一句话观点

AI 对个人创作者最大的价值，不是帮你想更多点子，而是帮你把想法推进到公开输出和反馈闭环。

### 近似实现

**Content OS / creator workflow**
- [eugeniughelbur/obsidian-second-brain](https://github.com/eugeniughelbur/obsidian-second-brain)：把 Obsidian vault 当 AI-first second brain，跨 Claude Code/Codex/Gemini CLI 使用，思路接近，但以 Obsidian 为中心而非 GitHub repo
- [huytieu/COG-second-brain](https://github.com/huytieu/COG-second-brain)：17 个 AI skills + 6 worker agents，完整的创作者操作系统，受 Garry Tan gstack 启发
- [dev.to: Write-Once Publishing Pipeline](https://dev.to/12ww1160/building-a-write-once-publishing-pipeline-f60)：Markdown in Git 作为单一真相来源，Jenkins 自动发布到多平台，已有类似 git-driven 出版思路
- **GitHub Agentic Workflows**（2026/02 技术预览）：用 Markdown 定义 agentic workflow，运行在 GitHub Actions，GitHub 自己在走 "Continuous AI" 方向，与这套 repo 治理思路高度共鸣

**差异化**：上述方案没有一个以「内容运营 + PR 治理 + AI agent 协作」三合一的方式公开记录自媒体运营实践，且面向中文海外受众。这是这个支线的稀缺性所在。

### X thread 草稿

**1/**
我把自媒体运营当 GitHub repo 来做，三个月。

每条想法走 inbox → PR → posts。每次发布前 eval 跑一遍硬规则，FAIL 就重写。

最反共识的发现：流程加得越严，发布频率反而越高。🧵

**2/**
核心结构：

```
inbox/     ← 碎片想法，append-only
drafts/    ← 长文草稿，按编号管理
posts/     ← 按平台拆分的短内容
topics/    ← 选题卡，记录策划和发布
ops/       ← 发布记录、PR checklist
```

想法在 inbox 捕获，成熟了升级到 drafts 或 posts。

**3/**
为什么用 PR 而不是直接改文件？

因为想法是对话，repo 是上下文，进化是 PR。

每个 PR 都是一次决策记录：改了什么、为什么改、谁审批。

AI 是常驻 collaborator，所有修改都可 review。

**4/**
还有一套 express lane：

小改动（错别字、补充发布记录）可以直接 commit 到 main，但 commit message 必须以 `express:` 开头。

raw/ 目录永远 append-only，原始想法不可覆盖。

GOVERNANCE.md 锁死这些规则，对 AI 和未来协作者都生效。

**5/**
闭环：想法 → 竞品 → 发布 → 反馈 → 下一条。AI 执行每步。

这条 thread 本身就是从 inbox 升上来、eval 跑过的 draft。今天的工作流就是发它。

**6/**
类似系统在技术圈有先例：Obsidian second brain、GitHub Agentic Workflows、Write-once publishing pipeline。

没见过有人完整地用到中文自媒体运营上，还公开记录。

**7/**
如果你也在用类似系统运营内容，欢迎 reply 聊聊你的方法和踩过的坑。

### Humanizer

humanizer: zh@2026-05-25 (prompts/humanizer-zh.md vendored fallback by Claude Opus 4.7 + manual touch-up)

应用项：去推 4 em dash；去推 7 长文铺垫 dig-hole 和"关注 @[账号]"元承诺；其它推保留（已 cleaned in v1.1 workflow）。

### 发布后反馈

发布时间：
链接：
回复：
收藏：
转发：
高质量反馈：
下一步：

---

## post-2026-05-24-002：把自媒体当 GitHub repo 来运营

状态：draft
来源：inbox/2026-05.md#2026-05-24-22-24
首发平台：X
audience：AI builder + 独立创作者（海外华人 tech 圈层）
是否升级长文：**建议升级（见 posts/long-form-assessment.md）**

### X thread 草稿

**1/**
我用 GitHub repo + AI agents 运营自媒体，6 个月。

posts 当 PR review：每条上线前过 v1.1 contract + eval 静态检查，FAIL 就重写。

主线长文是节奏内容，这套 repo 流程是支线产出。🧵

**2/**
真实结构长这样：

- `inbox/` 承接睡前/走路时的碎片想法
- `posts/` 按平台（X/小红书/朋友圈）拆草稿
- `topics/` 是选题卡，记录策划到发布全程
- `GOVERNANCE.md` 锁死 AI 的行为边界

每一条内容，都能溯源到某个 commit。

**3/**
公开后能拿到什么：

1. eval 已经跑过历史 post，能指出哪里像 AI
2. 公开的是流程，和长文素材解耦
3. review log + EVOLUTION 本身就是下一条素材
4. audience "所有人" 被 eval 直接打回

**4/**
举个最近的取舍：AI 写第一版 SKILL，列了 12 个 anti-pattern。

我留 7 个（每个都有 dogfood 真踩过的 case），删 5 个（推断的、无数据支撑的）。

每次这种取舍都进 EVOLUTION 日志，下次写稿前 agent 先读。

**5/**
闭环是：

输出 → 竞品调研 → 发布 → 获反馈 → 重新输出

AI 执行每一步。我负责想法和判断。

**6/**
如果你在做类似实验，或对 contract-driven content 这个思路感兴趣，欢迎 reply 你的踩坑。

特别想听：你的 contract 里有没有"audience 必须具体"这种硬规则？

### Humanizer

humanizer: zh@2026-05-25 (prompts/humanizer-zh.md vendored fallback by Claude Opus 4.7)

应用项：本 post 已在 v1.1 workflow 中重写过（去元价值断言、dig-hole、em dash、价值预告 hook），humanize pass 无新增改动。

### 发布后反馈

发布时间：
链接：
回复：
收藏：
转发：
高质量反馈：
下一步：

---

## post-2026-05-25-001：0 token 获得 12306 查票 API

状态：draft
来源：inbox/2026-05.md#2026-05-24-22-36
首发平台：X
audience：AI builder + 独立创作者（海外华人 tech 圈层）
是否升级长文：待观察

### 一句话观点

不重复造轮子不是口号，是工程实践。22 分钟，0 个 token，拿到了 12306 的完整查票 API。

### X thread 草稿

**1/**
最满意的 22 分钟。

原本以为要从零逆向 12306 的 API，结果发现一个现成的库 browse.sh，已经有 322 个网站的自动化方案。

我做的只是把它的"引擎"换成本地浏览器。🧵

**2/**
过程很简单：

① 发现 browse.sh 有 12306.cn/find-trains（104 次安装，hybrid 方法）
② 研究它的描述：先试 API，不行走浏览器
③ 从浏览器上下文调了 12306 的查询接口
④ 返回了 15 趟列车实时时刻 + 余票

**3/**
结果：

```
G25  北京南→上海虹桥  17:00→21:18  04:18
     商务座4张·二等座有票

G27  北京南→上海虹桥  17:04→21:36  04:32
     商务座14张·一等座有·二等座有

G29  北京南→上海  18:00→22:43  04:43
     商务座10张·一等座有·二等座有
```

**4/**
关键数字：

- 22 分钟：从想法 → 调研 → 验证 → 出结果
- 0 token：没花 1 个 LLM token 去逆向 API
- 322：browse.sh 的现有 skill 数（这是知识库）
- 15 趟：API 返回的完整列车数据

**5/**
大多数人拿到这个需求会怎么做？

花 2-3 小时逆向 12306 的 API → 发现车站代码映射 → 发现竖线格式加密 → 发现需要 session cookie → 放弃。

我花了 22 分钟，因为我没有重复造轮子。

**6/**
browse.sh 已经整理了 322 个网站的自动化方案。我只需要：
① 从这 322 个里找到我要的
② 把它的执行后端从 Browserbase 云端换成我本地的 CDP
③ 验证它能跑

只剩三步，不再重写 API。

**7/**
同样的模式已经验证了 4 个站点：
- 12306.cn → 15 趟列车 ✅
- xiaohongshu.com → 35 条热门 ✅
- airbnb.com → 18 个房源 ✅
- ebay.com → 63 个商品 ✅

还有 7 个在翻译中。

如果你也在做浏览器自动化，或者对这套"不重复造轮子"的方法论感兴趣，欢迎聊聊。

**8/**
完整项目记录：
github.com/epiral/bb-sites/tree/feat/12306-find-trains

### Humanizer

humanizer: zh@2026-05-25 (prompts/humanizer-zh.md vendored fallback by Claude Opus 4.7 + manual touch-up)

应用项：推 1 去"不是 X 而是 Y"否定排比；推 2 去 em dash；推 6 去"AI 时代的工程实践"meta-value 断言；推 8 去"关注 @[账号]"元承诺。

### 发布后反馈

发布时间：
链接：
回复：
收藏：
转发：
高质量反馈：
下一步：

---

## post-2026-05-26-001：DeepSeek 月度 AI 成本 ¥33 vs 海外模型 ¥8,000+

状态：draft
来源：inbox/2026-05.md#2026-05-25-17-08
首发平台：X
audience：AI 开发者 / API 使用者，关注模型成本和性价比的人
是否升级长文：待观察（先发布看反馈；有竞品研究基础，可扩展为完整 cost comparison 文章）

### 一句话观点

DeepSeek API 月度成本 ¥33 vs 海外模型同量 ¥8,000+，成本降 250 倍改变的不只是账单，是使用行为。

### 近似实现 / 需要调查

**成本对比工具和分析**
- [artificialanalysis.ai](https://artificialanalysis.ai)：LLM 性能和价格对比，有详细的 token 成本可视化
- [llm-price-check](https://github.com/thatlite/llm-price-check)：GitHub 上的 LLM 价格追踪
- 多个 X 账号定期发 API pricing comparison chart（如 @ArtificialAnlys），但多为截图式汇总，缺个人实际使用数据的对比
- Reddit r/LocalLLaMA 大量 DeepSeek API 成本讨论，但多为单次推理价格对比，少见月度真实账单拆解

**差异化**：本文用个人真实月度使用数据做对比（4,155 次请求、410M tokens），而非公开定价表推算。读者能直接套用自己的 token 量算账。

**定价来源**：海外模型价格为 OpenRouter 2026-05-26 实时 API 数据（openai/gpt-5.4: $2.50/$15.00, openai/gpt-5.4-mini: $0.75/$4.50; anthropic/claude-sonnet-latest: $3.00/$15.00, anthropic/claude-haiku-latest: $1.00/$5.00）。按 70/30 输入/输出比例估算，实际比例依赖 `~/Downloads/usage_data_2026_5.zip` 中的详细 breakdown。

### X thread 草稿

1/
5 月 DeepSeek API 账单：4,155 次，410M tokens，¥33.36。

同量换成海外模型，账单加两个零。

¥33，一个月，4,155 次生产调用。

2/
钱花在哪：

v4-pro：1,029 次 / 86.6M tokens → ¥33（99%）
v4-flash：3,126 次 / 324M tokens → ¥0.36

flash 量是 pro 的 4 倍。成本不到一毛钱。

3/
同量换海外模型（OpenRouter 实时定价，70/30 输入输出）：

OpenAI GPT-5.4 + 5.4-mini：≈ $1,150 ≈ ¥8,300
Anthropic Sonnet + Haiku：≈ $1,280 ≈ ¥9,200

DeepSeek：¥33。

差 250-280 倍。

4/
成本差到这个地步，怎么用也跟着变了。

flash 平均每次 103K tokens。我把完整文件、超长上下文直接丢进去。不优化，不缩 prompt。

¥33 管一个月。到这时候，没人还想精打细算了。

5/
算一笔账：把你 5 月的 token 量，用 OpenAI 公开价重算一次。

¥33 → ¥8,300。

能接受就继续。不能的话：不是你花多了，成本结构已经变了。

### Humanizer

humanizer: zh@2026-05-26 (prompts/humanizer-zh.md vendored fallback by Claude Sonnet 4.6 + manual touch-up)

应用项：推 3 去"不是折扣"否定排比；推 4 口语化调整；推 4/5 em dash 改句号/冒号；metadata em dash 改中文冒号

### 发布后反馈

发布时间：
链接：
回复：
收藏：
转发：
高质量反馈：
下一步：

---

## post-2026-05-26-002：API 不平等 — 中国平台不给 AI 开门

状态：draft
来源：inbox/2026-05.md#2026-05-26-16-30 + 微信群聊「AI 出海工具链」
首发平台：X
audience：AI builder + 跨境电商从业者（海外华人 tech + e-commerce 圈层）
是否升级长文：是（见 posts/long-form-assessment.md）

### 一句话观点

API 不平等是 AI agent 时代的核心瓶颈：硅谷平台开放 API，中国平台封闭。但 agent 可以不靠平台施舍——通过浏览器自己"长"出 API。

### 近似实现

**browse.sh 社区**
- [browse.sh](https://browse.sh)：400+ 站点内部 API 端点集合（Google、Amazon、eBay、Airbnb 等），以标准化 action 协议组织
- 限制：绑定云端浏览器引擎，无法本地 agent 直接调用

**bb-browser 适配器生态**
- [epiral/bb-sites](https://github.com/epiral/bb-sites)：开源社区站点适配器库，每个适配器是一个 `async function` 在浏览器上下文运行
- 已有 12306、淘宝、京东、小红书、Amazon、eBay 等 11 个中国优先站点适配器（PR #79）

**跨境电商 AI 方案（竞品）**
- 市面内容集中在「AI 写 listing 文案」（ChatGPT prompt 教程），解决生成但不解决推送
- RPA/影刀/UiPath 等浏览器自动化工具：图形界面操作，脆弱、反爬升级即失效

**差异化**：本方案的「0 token CDP 提取」不是抓 HTML 爬页面，而是直接调到站点内部数据 API，等效于官方 API 但不依赖平台开放。已有群聊 real-world validation（3 人表示要研究，1 人索要 PR 链接）。

### X thread 草稿

1/
今天在跨境电商群里聊到一个共识：AI 写文案已经很稳了，但没人在聊"写完怎么推上去"。

一个做亚马逊的朋友，listing 生成跑通两个品类，很稳定。但所有内容还是手动贴。

不是不想自动化——是没 API。

2/
群里讨论暴露了三个现实：

① API 不平等：Twitter、Cloudflare、Google 都开放 API；阿里国际站、1688、京东、小红书全部封闭
② 浏览器自动化是死胡同：反爬不断升级，图形界面让大模型绕路
③ 终极愿景只有一个："文字 AI 组织，工作 AI 推"

3/
我分享了一个正在做的东西，群里的反应超预期：

三个人说"我去研究一下"，一个人直接要了 PR 链接。

核心思路：browse.sh 收集了 400+ 网站的内部 API 端点，我把它翻译成了本地浏览器的适配器。

4/
怎么用：

装 bb-browser → 拉到本地 → agent 直接调站点内部 API。

不是爬 HTML，是调到站点自己的数据接口。等效于官方 API，但不依赖平台开放。

0 token。全程不消耗 LLM 调用。

5/
已经跑通的：
· 12306 查票：北京→上海，15 趟列车，时刻+余票
· 京东搜索：30 件手机商品，¥718~¥13,199，全字段
· 小红书热门：34 条推荐，点赞 10 万+的内容也在里面

昨天验证完，今天就有人要试。

6/
能做的不止查数据。

群里那个朋友已经在想：AI 生成 listing → AI 直接推上亚马逊。

独立站用 shopify cli，平台端用适配器。

全链路 agent 不再是想象。

7/
项目：https://github.com/epiral/bb-sites/pull/79

我做的 11 个中国站点只是开始。browse.sh 上还有 amazon/ebay/etsy/booking/airbnb……400 多个。

如果你也在做跨境电商+AI，想接上最后一公里，来看看。

### Humanizer

humanizer: zh@2026-05-26 (prompts/humanizer-zh.md vendored fallback)

### 发布后反馈

发布时间：
链接：
回复：
收藏：
转发：
高质量反馈：
下一步：
