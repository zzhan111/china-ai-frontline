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

### 发布后反馈

发布时间：
链接：
点赞：
收藏：
评论：
高质量反馈：
下一步：
