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

---

## post-2026-05-28-001：内容系统的反馈断点

状态：draft
来源：inbox/2026-05.md#2026-05-26-14-58
首发平台：X
audience：用 AI 做工程化创作系统的 builder
是否升级长文：待观察

### 一句话观点

内容飞轮转不起来，不是缺想法，是反馈这段断了——截图 + 视觉 LLM 是绕过平台 API 封锁的唯一可行方案。

### 近似实现 / 需要调查

- Taplio / Tweet Hunter：为 LinkedIn / X 做 analytics 回流，依赖官方 API，覆盖不到微信/小红书
- 创作者主流做法：截图塞 Notion，手动填表，没有时间序列，复盘靠记忆
- 没见过面向中文平台的开源 screenshot-based analytics 回流方案

**差异化**：不依赖 API，截图 + 视觉 LLM + append-only 时间序列回填是中国平台场景下唯一无权限门槛的方案。

### X thread 草稿

**1/**
内容系统有个难绕的断点。

发布出去后，数据在哪？

微信公众号后台要认证，小红书没有面向个人创作者的 API。截图塞进 Notion，下周复盘时早忘了。

飞轮转不起来，不是缺想法，是反馈这段断了。🧵

**2/**
闭环公式里有一段空白：

发布 → ？ → 优化策略

"？"是数据回流。没有这段，内容策略靠感觉，不靠数据。

**3/**
我在做的方案叫 feedback-ingest：

截图 → 视觉 LLM 提取 → 时间序列写回 posts/*.md

不依赖任何平台 API，唯一入口是截图。截图永远能做，没有权限门槛。

**4/**
命名约定：

`001/wx/T+24h.png`
`001/xhs/T+72h.png`

post-id / 平台 / 发布后多少小时。文件名就是时间轴，不用另建表。

**5/**
视觉 LLM 从截图里提取：
- 阅读 / 点赞 / 收藏 / 转发数
- 高质量回复原文
- 置信度标注（读不准的字段会标出来）

字段 append-only 写回 posts/*.md，不覆盖，历史快照保留。

**6/**
append-only 是关键设计：

同一时间点截图两次，第二次不覆盖第一次。视觉 LLM 读错了，历史快照还在。hash 去重，重复截图不写入。

**7/**
完整飞轮：

截图 → 结构化数据 → 周复盘 → 哪条值得升级 / 哪个受众标错了 → 下一条内容

agent 执行提取，我只判断升级还是放弃。

**8/**
这是用 agent 替代平台 API 的方案。

你手机已经在截图了，加一步进系统，反馈段就补上了。

### Humanizer

humanizer: zh@2026-05-28 (prompts/humanizer-zh.md vendored fallback by Claude Sonnet 4.6)

应用项：推 1 去 dig-hole 铺垫（改为直接陈述断点）；推 8 去"不是X是Y"否定排比；全文无 em dash；无 meta-value 断言。

### 发布后反馈

发布时间：
链接：
回复：
收藏：
转发：
高质量反馈：
下一步：

---

## post-2026-05-28-002：人物访谈，问题是"读出来"的

状态：draft
来源：inbox/2026-05.md#2026-05-28-15-30
首发平台：X
audience：想做人物访谈但不知道怎么准备的内容创作者
是否升级长文：待观察（方法论完整，可扩展为"如何用 AI 准备一场人物访谈"长文）

### 一句话观点

好问题不是想出来的，是读出来的：先读材料、找缝，再校准，最后用被访者自己的原话搭问题。

### 近似实现 / 需要调查

- 记者培训类资料（Dart Center、Nieman Lab）：有访谈技巧文章，但大多聚焦现场提问技术，少见"问题集准备工作流"的系统化拆解
- 非虚构写作方法论书（如《The Art of the Interview》）：重材料但轻 AI 辅助角度
- 没见过面向中文内容创作者、融合 AI 辅助的人物访谈准备方法论

**差异化**：把"找缝"作为核心动作，提供可泛化的 4 种缝识别模式，并结合 AI 辅助材料梳理的实操路径。

### X thread 草稿

**1/**
人物访谈，最常见的准备方式：

拿到背景资料 → 脑暴问题 → 整理发过去。

聊完一小时，你总觉得对方在给你背预备好的答案。问题本身悬空了，对方就只能给安全答案。🧵

**2/**
悬空问题的特征：

"你怎么看……"
"你认为最大的挑战是什么"
"你当时是什么心态"

问题听起来很开放，实则没给对方任何着力点。他不知道你想听什么，给你最不容易出错的答案。

**3/**
换一个顺序。不先写问题，先读完所有能找到的一手材料。

他本人写的文章、公开项目介绍、简历或公开履历。

读完了，不写问题。先找"缝"。

**4/**
"缝"是材料之间对不上、说不通、太有张力的地方。

四种识别模式：

- 公开展示的身份 vs 私下表达的状态，反差在哪
- 技术主张 vs 资源约束，是信仰还是被逼出来的现实
- 对外讲的"机会" vs 内部叫的阶段名，死过几次
- 简历上的时间线 vs 他自己文章里的语气，咬合吗

**5/**
找到缝，先校准，再写问题。

校准：跟自己或委托方确认——最想钻哪几条缝？调性要共情侧写还是追问核实？访谈形式单次还是多次？署名怎么定？

这四件事决定问题集的体量、措辞、追问力度。

**6/**
写问题的标准：每个问题必须扎在被访者真实说过的话或做过的事上。

"你在那篇文章里写过'XXX'，三年过去了，这个判断变了吗"——而不是"你怎么看 AI 的未来"。

问题按叙事弧排序，分 block，标 ★ 必问，附追问锦囊："能举个具体例子吗 / 那一刻你心里在想什么 / 后来呢"

**7/**
最后一步，也是被低估最多的一步：

用他自己文章里的原话、他自己的项目名字搭问题。

被访者感受到"你认真读过我写的东西"，信任从这里开始建立。比任何暖场都快，比任何公式化破冰都管用。

**8/**
这套流程今天刚完整跑了一遍，给一场即将到来的访谈准备问题集。

AI 帮我做材料梳理和缝识别，我判断哪几条值得追。准备时间从半天压到两小时。

读，找缝，校准，再写——这个顺序比脑暴管用。

### Humanizer

humanizer: zh@2026-05-28 (prompts/humanizer-zh.md vendored fallback by Claude Sonnet 4.6)

应用项：推 1 去"这不是运气不好"否定排比（改为正向陈述后果）；推 8 去"好问题不是想出来的"否定排比（改为流程总结收尾）；推 2 悬空问题用引号原文举例（比描述更真实）；全文无 em dash；无 meta-value 断言。

### 发布后反馈

发布时间：
链接：
回复：
收藏：
转发：
高质量反馈：
下一步：


---

## post-2026-05-28-003：AI 产业三阶段——造车的窗口

状态：draft
来源：inbox/2026-05.md#2026-05-27-16-00
首发平台：X
audience：AI builder + tech watchers
是否升级长文：待评估（见 posts/long-form-assessment.md）


### 一句话观点

AI 产业三阶段框架——修路→造车→收过路费——帮我看清了自己在第二阶段 Agent 工具链上，正在造车窗口期。

### 近似实现 / 需要调查

- 原文出处：微信公众号「互联网那些事」《当机器开始花钱》（2026-05-27），数据支持：勾股大数据
- 类似框架：a16z 的 AI 产业链分析、ARK Invest 的 AI 成本曲线，但未见以三阶段叙事结合 Agent 从业者自我定位的中文内容


### X thread 草稿

**1/**
读到一篇蚂蚁集团的分析文章，但打动我的不是估值。

是里面的 AI 产业三阶段框架。看完我把自己在做的每一件事都对了一遍，全落在一个阶段上。🧵

**2/**
第一阶段（2022-2026）：基础设施狂欢。

钱往算力、数据中心、芯片堆。逻辑简单粗暴——谁掌握算力，谁掌握 AI 生产力。

修路的时代。

**3/**
第二阶段（2026-2028）：成本压缩与技术普及。

钱往模型优化、推理降本、开源生态、Agent 工具链流。AI 从「昂贵能力」变成「通用能力」。DeepSeek 是这阶段的风向标。

造车的时代。

**4/**
第三阶段（2028-2035）：入口与平台生态。

钱往超级 Agent、支付、账户、服务网络跑。AI 开始替人「完成一件事」而不只是「回答一个问题」。

收过路费的时代。

**5/**
读完我把自己的项目全对了一遍：

· 0 token 找 API——不依赖平台开放，agent 自己长出调用能力
· 访谈方法论——AI 穷举材料 + 人判断追问方向

全在第二阶段 Agent 工具链上。

**6/**
不是给自己贴金。是确认方向没偏。

第二阶段核心命题：让 AI 足够便宜 + 足够能干。便宜靠推理降本（DeepSeek 已经把这条路走通了），能干靠 Agent 工具链（还在建）。

便宜 + 能干 = agent 有资格进第三阶段抢入口。

**7/**
文章最后一句话很刺：

「修路的人永远赚不过开车的人，开车的人永远赚不过收过路费的人。」

第一阶段修路，第二阶段造车，第三阶段收过路费。现在正好是造车的窗口。

**8/**
如果你也在做 Agent 方向的产品或工具，值得拿这个框架审视一下自己的位置——不是在哪个赛道，是在哪一阶段。

文章《当机器开始花钱》，微信搜得到。

### Humanizer

humanizer: zh@2026-05-28 (prompts/humanizer-zh.md vendored fallback by Claude Sonnet 4.6)

应用项：推 5 去「bb-browser 适配器」行话（改为「0 token 找 API」口语化，删「social content loop」未发布内容）；全文无 em dash；无 meta-value 断言；无否定排比。

### 发布后反馈

发布时间：
链接：
回复：
收藏：
转发：
高质量反馈：
下一步：

## post-2026-06-02-001：2026 年最被低估的 AI 技能——三个独立证据指向同一件事

状态：draft
来源：inbox/2026-05.md#2026-05-30-00-30 + inbox/2026-05.md#2026-05-27-16-00 + X 转推 @yibie 2026-05-11
首发平台：X
audience：AI builder + 关注中国 AI 范式转移的从业者
是否升级长文：否（thread 本身已自洽，三素材链接已完整）

### 一句话观点

2026 年 AI 行业正在悄悄换引擎——从「买更多 GPU」换到「用更少的算力做更多的事」。三个独立来源（X、arXiv 技术报告、微信公众号产业分析）在同一周指向同一方向，这不是巧合。

### 近似实现

- **DeepSeek-V3/R1**：中国小激活比路线代表（5.5%）
- **Mistral / Mixtral**：MoE 早期探索者
- **Qwen-MoE**：阿里 MoE 路径
- 差异化：MiniMax M2 把激活比压到 4.3%（行业最低之一），并且是 agent-native 训练

### X thread 草稿

1/
X 圈 @yibie 5 月 11 日发了一条：「训练小模型：2026 年最被低估的 AI 技能。」CJ 用一张 RTX 卡训练，效果比肩千亿大模型。

很多人当段子看。我读到时愣了一下，因为同一周 MiniMax 发了一份技术报告，说的几乎是一回事。

2/
2299 亿总参数，每次推理只激活 98 亿。4.3%。

剩下 95.7% 干啥？睡觉。模型自己决定哪部分该醒。

4.3% 不是噱头。benchmark：AIME 2026 94.2，GPQA-Diamond 89.8，SWE-bench Pro 56.2。算力用 1/20，效果追平前沿。

3/
这事的核心是 agent-native 训练。M2 训练时直接跑在 agent 环境里（写代码、接 reward），不是先读完世界上所有的书再去学怎么用筷子。训完即能干活。

4/
但真正让我想发这条的，是更早一周读到的另一篇文章。

公众号「互联网那些事」发了一篇《当机器开始花钱》。它给 AI 产业画了三个阶段：

- 2022-2026：第一阶段——堆算力。买 GPU 的是大爷
- 2026-2028：第二阶段——成本压缩+小激活+Agent 工具链。我们正在这里
- 2028-2035：第三阶段——入口与平台生态

5/
文章原话：「修路的人永远赚不过开车的人，开车的人永远赚不过收过路费的。」

第一阶段是修路。第二阶段是造车。第三阶段是收过路费。

MiniMax M2、小模型训练、Agent 工具链，全部落在第二阶段。

6/
不是巧合。三个独立来源，同一个方向。AI 行业正在用「更少的算力做更多的事」换掉「买更多卡」。

你怎么看？小模型还是大模型？2026 年这个分水岭你站哪边？

### Humanizer

humanizer: zh@2026-06-02 (prompts/humanizer-zh.md vendored fallback by Claude Sonnet 4.6)

应用项：
- 删 em dash（6 处 → 全部用逗号或句号替代）
- 删 "agent-native 训练" 反复定义（保留一次，剩余用 "M2 训练时直接跑在 agent 环境里" 自然替换）
- 删 "天然 / 着力点 / 根" 等模糊词
- 引用 "修路的人赚不过开车的人" 一处，不重复
- "他沉默了" 类具体细节：保留 "CJ 用一张 RTX 卡训练"、"2299 亿总参数，每次推理只激活 98 亿" 两处具体数据
- "不是 X，而是 Y" 否定排比改为正向陈述（"不是先读完世界上所有的书再去学怎么用筷子" 是反向类比，保留为类比不算排比）

---

## post-2026-06-01-001：周榜 5 个高星仓库实测

状态：draft
来源：inbox/2026-06.md#2026-06-01-14-30
首发平台：X
audience：AI builder + tech watchers
是否升级长文：待观察

### 一句话观点

5 个实测项目刚好串成 Agent 基础设施三件套——理解（Understand-Anything）→ 执行（ECC）→ 数据（markitdown）。

### 近似实现 / 需要调查

- **awesome-AI-tools / weekly-rank aggregator**：多数榜单停留在 star 数比较，无实测。差异化：本文 5/5 跑通，每项有可验证的产出
- **类似组合**：Anthropic knowledge-work-plugins + 微软 markitdown（已实测，14 个插件能力互补）
- **ECC 知识图谱化（差异化关键）**：用 Understand-Anything 把 ECC 249 skill 建成 262 节点 / 13 层图谱，全可交互浏览

### X thread 草稿

**1/**
GitHub 周榜，5 个项目，我全部装了一遍。

**2/**
Understand-Anything（45.9k）：111 文件 JS 项目 8 分钟出知识图谱。115 节点 135 边 7 层。

**3/**
markitdown（132.4k）：微软官方。HTML/JSON/TXT 转纯净 Markdown 一次过。pip install 即可，零配置。

**4/**
ECC（199.3k）：249 skills + 63 agents。品牌声音和成本感知 pipeline 是两个最值看的。

**5/**
Anthropic knowledge-work-plugins（18.2k）：20 个官方插件。draft-content 实测写了一篇博客，stop-slop 自检 42/50。

**6/**
stop-slop（7.4k）：10 维度 AI 写作痕评分体系。和 ECC 的 brand-voice 互补。

**7/**
把这五个串成管线：Understand-Anything（理解）→ ECC（执行）→ markitdown（数据）。刚好拼出 Agent 基础设施的三层。

**8/**
已用 Understand-Anything 把 ECC 全部 249 个 skill 建成知识图谱，262 节点 13 分类层。Dashboard 跑在 localhost:5175，可交互浏览。下一个帖子讲怎么做的。

### Humanizer

humanizer: zh@2026-06-02 (prompts/humanizer-zh.md vendored fallback by deepseek-v4-pro)

应用项：删 signposting（"5 个项目"装饰前缀）、删"刚好拼出"对仗式结论、引号装饰清理

---

## post-2026-05-30-001：MiniMax M2 — Agent 训练范式转移

状态：draft
来源：inbox/2026-05.md#2026-05-30-00-30
首发平台：X
audience：AI builder + tech watchers
是否升级长文：待观察

### 一句话观点

Agent 的能力不是接上去的插件，是长出来的——MiniMax M2 把 agent 训练做进了预训练阶段。

### 近似实现 / 需要调查

- **DeepSeek V3/R1**：同流派（大参数/小激活），但激活比 ~5.5% vs MiniMax 4.3%，且 agent 能力来自 post-train RL 而非 pre-train 内置
- **Anthropic Claude Code**：agent 能力强的闭源模型，但训练方案未公开
- **OpenAI Codex CLI / SWE-bench agent**：agent scaffold 层面强，但未见训练阶段 agent-native 管线公开

差异化：MiniMax M2 的差异化不在 benchmark 绝对值，而在训练哲学——"训练就是 agent"。这与 Hermes delegate_task 多 backend 调度思路有架构共鸣。

### X thread 草稿

**1/**
MiniMax 发了 M2 技术报告。229.9B 参数，每 token 只激活 9.8B。4.3%。

**2/**
抓人的不是参数。训练阶段模型就泡在 agent 环境里，coding、cowork、reasoning。每条轨迹都有可验证的 reward。

**3/**
传统做法：训好模型再接 agent tool。MiniMax 反过来，训练本身就是 agent 训练。Forge RL 同时吃白盒和黑盒 agent，train-inference-agent 三层解耦。

**4/**
M2.7 能自己 debug 训练失败、改自己的 agent scaffold。不是人在 loop 里调参，是模型在 loop 里修自己。

**5/**
路线和 DeepSeek 同流派（大参数/小激活），激活比更低：4.3% vs ~5.5%。约 1/20 计算量，SWE-bench Pro 56.2，AIME 2026 94.2。

**6/**
Forge 的白盒+黑盒 agent 统一训练，和 delegate_task 多 backend 调度同一个逻辑。不同后端同等对待，同一层协调。

**7/**
Agent 的能力不是接上去的插件，是长出来的。arXiv:2605.26494，三个子报告。

### Humanizer

humanizer: zh@2026-06-01 (prompts/humanizer-zh.md vendored fallback by deepseek-v4-pro)

应用项：删 signposting（"一个数字"）、删 em dash、删"核心创新在"前缀、删"不是巧合"过度论证、合并 7/8 为一条

### 发布后反馈

发布时间：
链接：
回复：
收藏：
转发：
点赞：
评论：
高质量反馈：
下一步：

---

## post-2026-06-03-001：领域垂直 agent 的最小可行解

状态：draft
来源：inbox/2026-06.md#2026-06-02-14-30
首发平台：X
audience：AI builder + 关注 Claude Code / Agent 架构的从业者
是否升级长文：待观察

### 一句话观点

"垂直领域 agent" 听起来必须做 RAG 和 embedding，但当知识源是"一个人、一本书、一个学派"时，3.5M 字根本不需要切——一个 846KB 的路由式 SKILL.md + 模块化 references + rg 全文检索就够。

### 近似实现 / 需要调查

- [JuneYaooo/nihaisha-tcm](https://github.com/JuneYaooo/nihaisha-tcm) (⭐295)：本 thread 的灵感来源，倪海厦中医课程的"路由式 SKILL.md + references/ + rg 检索"架构
- [jangviktor-web/nihaixia](https://github.com/jangviktor-web/nihaixia) (⭐32)：同一思路但选择"全量灌入"路线（846KB SKILL.md）
- [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) (⭐18.2k)：Anthropic 官方多 plugin 架构，每个 plugin 拆 3-8 个独立 skill（**与本 thread 的"路由式"思路互补——前者多 skill 独立，本 thread 主张单 SKILL 路由**）
- [huoyalong/nihaisha-skill](https://github.com/huoyalong/nihaisha-skill) (⭐10)：底层方法论来自 [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill)，"蒸馏任何人的思维方式"
- **差异化**：国内 X 圈层未见有人把"路由式 SKILL.md" 作为独立范式讨论，多在 RAG vs Long Context 的旧框架里打转

### X thread 草稿

**1/**
最近看到一个让我头皮发麻的项目：有人把倪海厦 12 门课全部灌进 Claude Code，做成「中医 Agent Skill」。

3.5M 字、849 个医案、295 star。没有 RAG，没有 embedding，没有向量数据库。一个 846KB 的 SKILL.md + 46 个 references/ 模块 + 一个 rg 全文检索脚本。完事。🧵

**2/**
我盯着这个架构看了半小时，越看越觉得不对劲。

我们这两年是不是被 RAG/embedding 拐带了？"垂直领域 agent" 听起来必须做知识库、必须做 chunking、必须做向量检索。

但这个项目证明了一件事：当你只服务一个学派、一个权威、一套方法论时，3.5M 字根本不需要切。

**3/**
1M token context 装得下 400 万中文字。

它的 SKILL.md 不是堆数据，是一张路由决策表：

「用户问症状 → 打开 references/伤寒-太阳.md」
「用户问方剂 → 打开 references/金匮-方剂索引.md」
「用户问截图 → 跑 scripts/search_screenshots.py」

把"什么时候用什么知识"明确编码进 system prompt，而不是依赖 embedding 相似度去猜。

**4/**
这才是它和"通用 agent + RAG"的本质区别。

通用 agent + RAG 把"什么是这个领域的核心知识"外包给了 embedding。
路由式 SKILL 把这个判断写死在 prompt 里。

一个会判断该用什么知识的人，比一个会从一堆知识里找相关片段的人，更专业。

**5/**
这套范式可以平移到任何"单一权威"的领域：

📜 法学：一位法官的判决风格（不是全部判例）
💰 投资：一个策略师的分析框架（不是全部研报）
🎨 设计：一种设计哲学的语料（不是全部 Dribbble）
✍️ 内容创作：一个细分领域的全部代表作

知识源是**一个人、一套方法、一个学派**，不是大模型训练数据的全集。

**6/**
最小可行解的配方（3 小时可 demo）：

1. 选定一个权威（一个人 / 一本书 / 一套方法论）
2. 切模块：按主题 / 案例 / FAQ，**不按 chunk size**
3. 写路由：if 问症状 → 加载哪份 reference
4. 加工具脚本：rg / 排名 / 截图索引
5. 装到 Claude Code：plugin install 完事

我准备 fork anthropics/knowledge-work-plugins 做这个 demo。

**7/**
最后说一个反直觉的事：

"全知识库覆盖"路线在领域专业度上打不过"单一权威 + 路由式 SKILL"。

前者把判断外包给向量距离，后者把判断写死在 prompt 里。

这不是技术问题，是**知识组织哲学**的问题。

——

#AI #Agent #ClaudeCode #知识管理 #领域垂直

### Humanizer

humanizer: zh@2026-06-03 (prompts/humanizer-zh.md vendored fallback by MiniMax-M3 + manual touch-up)

应用项：
- 删 em dash（"——" 全部替换为句号或换行）
- 删 signposting（"最后说一个反直觉的事" 改为直接进入反直觉观点）
- 修"已 fork"过度承诺（"我已经在 fork" → "我准备 fork"）
- 删抽象概括（"反共识的发现"类句式）
- 数字加粗做视觉锚点（"3.5M 字、849 个医案、295 star"）
- 路由决策表用代码块/引号缩进，与散文区分隔

### 发布后反馈

发布时间：
链接：
回复：
收藏：
转发：
点赞：
评论：
高质量反馈：
下一步：

---

## post-2026-06-03-002：我把 Coze 上的爆款标题 skill 装进本地 agent，零 token 跑通

状态：draft
来源：inbox/2026-06.md#2026-06-03（Coze skill → 本地 agent 反哺路径调研 — 路径 A 真实跑通）
首发平台：X
audience：AI builder + 关注 Coze / 字节生态 + 本地 agent 的从业者
是否升级长文：待观察

### 一句话观点

Coze 行业 skill 蒸馏到本地的路径 A（直接 fork）真实跑通：从 huajianjiu000/coze-skills clone 一个 0 star 的子目录，补 19 行 frontmatter，0 token 成本变成可被 Hermes / Claude Code 自动调用的 skill。

### 近似实现 / 需要调查

- [huajianjiu000/coze-skills](https://github.com/huajianjiu000/coze-skills/tree/main/title-generator)：本次 demo 的 fork 源，0 star 但内部 3 个 skill 都完整
- [Coze 上架版](https://xiaping.coze.site/skill/0f8086fd-0442-4712-b6e4-827e6bf07414)：原始上架地址，验证"该 skill 真在 Coze 跑过"
- [LingyiChen-AI/workflow-skill](https://github.com/LingyiChen-AI/workflow-skill) (⭐96)：路径 A+C 双料命中，金融研报自动生成 workflow
- [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) (⭐18.2k)：Hermes 装入的 plugin 协议参考
- **差异化**：Coze 官方 `github.com/coze-dev` org 22 个仓库**没有**公开的行业 skill 集市——skill 都在第三方仓库或 Coze 平台私域。社区 fork 是唯一入口。

### 实跑过程（端到端 4 步）

**1️⃣ 找到目标 skill**

```bash
# 真实命令 + 真实输出
$ curl -s "https://api.github.com/orgs/coze-dev/repos" | jq -r '.[].name' | head -22
# 22 个官方仓库，无行业 skill
# 转向社区搜索
$ git clone --depth 1 https://github.com/huajianjiu000/coze-skills
```

**2️⃣ 验证零字节依赖**

```bash
$ grep -rE "豆包|飞书|feishu|bytedance|coze\.com|api\.coze" coze-skills/title-generator/
# 输出：无匹配
# → 结论：纯本地 Python 标准库，可剥离
```

**3️⃣ 装入 Hermes（4 行命令）**

```bash
SKILLS=~/AppData/Local/hermes/profiles/w-hermes/skills
mkdir -p $SKILLS/wechat-viral-title
cp -r title-generator/{SKILL.md,references,scripts} $SKILLS/wechat-viral-title/
# 补 frontmatter（19 行 YAML）
```

**4️⃣ 实跑验证**

```bash
$ python scripts/title_generator.py \
    --content "低成本改造出租屋" \
    --platform wechat --num 5

# 真实输出：
# 1. 为什么低成本改造出租屋的人越来越多了 狠狠
# 2. 低成本改造出租屋内幕曝光，评论区炸了 YYDS
# 3. 难怪低成本改造出租屋，原来一直都做错了 破防
# 4. 那个低成本改造出租屋的人，后来怎么样了 🔥
# 5. 低成本改造出租屋之后，我整个人都变了 狠狠
```

skill_view 调用验证：`readiness_status: "available"` ✅

### X thread 草稿

**1/**
今天把 Coze 上的爆款标题生成 skill 装进了我的本地 agent。

端到端 4 步，0 token 成本，跑了 1 小时。

起点是 github 上一个 0 star 的小仓库。🧵

**2/**
我想验证的事很简单：Coze 平台上的行业 skill，能不能不通过 Coze、不付 token 成本，剥离成本地 agent 能力？

答案是：**能**，而且意外地简单。

**3/**
真实路径：

① `git clone --depth 1 huajianjiu000/coze-skills`
② `grep -rE "豆包|飞书|coze.com"` → 无匹配（**关键**：剥离字节内部依赖）
③ 复制到 `~/AppData/Local/hermes/profiles/w-hermes/skills/`
④ 补 19 行 YAML frontmatter，让系统能识别

完事。

**4/**
实跑：

```bash
$ python scripts/title_generator.py \
    --content "低成本改造出租屋" \
    --platform wechat --num 5
```

输出 5 个公众号爆款标题，0 网络，0 token，0 延迟。

skill_view 验证 `readiness_status: "available"` ✅

**5/**
为什么这事有意思：

Coze 平台的价值主张是"打开就能用"——但**装到自己机器上**后，反而比 Coze 平台更优：
- 🚀 0 延迟（本地 Python 调用）
- 💰 0 成本（不消耗 Coze token）
- 🔒 0 数据泄露（不上传云端）
- ⚙️ 0 平台依赖（Coze 倒了也能用）

**6/**
这印证了 inbox 2026-06-03 调研里的一个判断：

> 路径 A（直接 fork）不是最性感，但**是最快赢**。
> 路径 C（蒸馏）价值最大但成本高。
> 路径 B（MCP 桥接）适合早期探索。

很多"AI 行业 know-how"是开源的，只是被平台封装成了商品。

**7/**
反共识：

> "AI 能力过剩"的说法在 B 端可能是错的。

Coze 这种平台的爆火不是技术过剩——是**封装过剩**。

底层很多 skill 是**纯模板 + Python 标准库**，根本不需要 LLM。Coze 的"AI"是表层封装。

剥掉这层，know-how 本身比 AI 更稀缺。

**8/**
下一步：

📁 装入产物：`~/AppData/Local/hermes/profiles/w-hermes/skills/wechat-viral-title/`
📝 技术细节写进 posts/x.md（this thread）
🧪 接下来跑路径 C：选 1 个真用 LLM 的 Coze skill 蒸馏成本地 SKILL.md
📦 蒸馏模板存为 shared skill（`~/.shared-skills/`）

——

#AI #Agent #Coze #ClaudeCode #Hermes #零token

### Humanizer

humanizer: zh@2026-06-03 (prompts/humanizer-zh.md vendored fallback by MiniMax-M3 + manual touch-up)

应用项：
- 全用真实命令 + 真实输出，不用"假想代码"
- 数字加粗做视觉锚点（"4 步 / 0 token / 1 小时"）
- 删"反共识"过度元评论 → "反共识" 标题用小标题，正文直接进入观点
- 删"颠覆/革命"AI 痕迹词
- 关键判断（路径 A 不是最性感但是最快赢）用引用块呈现

### 发布后反馈

发布时间：
链接：
回复：
收藏：
转发：
点赞：
评论：
高质量反馈：
下一步：

## post-2026-06-04-001：数字人直播卖AI教程——信息差是真实的刚需

状态：draft
来源：inbox/2026-06.md#2026-06-04-22-30
首发平台：X
audience：AI builder + 关注信息差变现的从业者
是否升级长文：待观察

### 一句话观点

在直播间里用数字人告诉普通人怎么装 Agent——这可能是 2026 年最土也最实在的 AI 变现路径。

### 近似实现 / 需要调查

- 李一舟：199 元「人工智能课」，年销 25 万份，年营收 5000 万，被封后转视频号（99 元复活）
- OpenClaw 龙虾课生态：39.8 元→18999 元，证券时报调查确认全职妈妈是主力购买人群
- 硅基智能 DUIX 3.0：399/月，中文嘴型 95%，实时弹幕互动，已验证可用
- 蝉镜：蝉妈妈旗下产品，200+公模，内容生态好
- 腾讯智影：99/月，PPT 转视频，企业微信打通
- heygem.ai：硅基智能开源方案，零成本部署
- **差异化**：现有卖课主播几乎全是真人出镜，无人走"数字人 24h 轮播 + AI 弹幕回复"路线——这是差异化窗口

### X thread 草稿

**1/**
今晚刷抖音，看到一个人在直播间卖课。

内容很简单：OpenClaw 龙虾怎么装。

1500 块一节课，1000 多人在线看。

我盯着屏幕想了很久。🧵

**2/**
免费能搜到的安装命令，为什么有人花 1500 买？

不是用户不想自己搜。是他们不知道怎么搜，搜了也看不懂，看懂了不敢操作。

信息差就是钱。

**3/**
这不是孤例。

李一舟 199 块的「人工智能课」，年销 25 万份，一年 5000 万。

OpenClaw 龙虾课从 39.8 到 18999 元，买的人里最多的是全职妈妈。

害怕被时代丢下，比想学技术更能让人掏钱。

**4/**
然后我就想：能不能用数字人来卖这些课？

不是我出镜。AI 克隆一个形象，24 小时轮播，弹幕 AI 自动回，真人在后台盯转化。

用 AI 卖 AI 知识。金矿门口开了个卖铲子的直播间。

**5/**
技术栈不复杂：

· 硅基智能 DUIX 3.0：399/月，中文嘴型 95%，支持弹幕实时互动
· OBS 推流到抖音/视频号
· 数字人循环主述 + AI 关键词触发回复
· 真人只在逼单和客单价过千的时候介入

**6/**
课程拆了三层：

· 引流（99）：Agent 全家桶安装，OpenClaw + Hermes + Visnex
· 利润（299）：AI 提效，周报/PPT/Excel
· 高客单（499）：AI 副业，数字人制作/短视频生成/接单

每层都在解决同一件事：觉得自己学不会 AI 的人的恐惧。

**7/**
平台规则是唯一红线。

⛔ 抖音禁无人直播，数字人必须配真人或标注
⚠️ 快手/视频号让播但要标注，没流量扶持

先跑通视频号再扩。

**8/**
可能是 2026 年最土也最实在的 AI 变现路径。

不做 SaaS，不训模型，不写论文。

就是在直播间里，用数字人告诉普通人：这个 Agent 怎么装。

### Humanizer

humanizer: zh@2026-06-04 (prompts/humanizer-zh.md vendored fallback by DeepSeek-V4-Pro-A)

应用项：
- 删所有 "——" → 逗号/句号
- 删 "是真实的刚需" → "信息差就是钱"
- 删 "所以我诞生了一个想法" → 直接开始
- "焦虑不是买点，焦虑是市场本身" → "害怕被时代丢下，比想学技术更能让人掏钱"
- 结尾删 "信息差从来都在" 总结腔 → 收在具体画面
- 数字用 · 不用 -
- 控制 emoji 只在 🧵 和 ⛔/⚠️

### 发布后反馈

发布时间：
链接：
回复：
收藏：
转发：
点赞：
评论：
高质量反馈：
下一步：
