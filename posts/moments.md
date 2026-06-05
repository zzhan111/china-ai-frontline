# 朋友圈 drafts

## post-2026-05-24-001：缺乏的不是想象力，而是执行闭环

状态：draft
来源：inbox/2026-05.md#2026-05-24-21-25
首发平台：朋友圈
audience：熟人圈：同事 + tech 朋友 + 家人
是否升级长文：待观察

### 一句话观点

AI 最有用的地方不是帮我"想更多"，而是帮我"推进一点"。

### 近似实现 / 待查

- AI content workflow
- creator operating system
- GitHub writing workflow
- AI agent social media workflow

### 朋友圈草稿

最近越来越觉得，AI 最有用的地方不是帮我"想更多"，而是帮我"推进一点"。

很多想法其实早就有了，问题是没有被整理、没有被找近似实现、没有被发出去、也没有反馈。

所以我准备把自己的内容仓库改成一个执行闭环：

想法进来 → AI 找相似实现 → 生成社媒草稿 → 发出去 → 收反馈 → 再更新。

缺的不是想象力，是闭环。

### Humanizer

humanizer: zh@2026-05-25 (prompts/humanizer-zh.md vendored fallback by Claude Opus 4.7)

应用项："repo"→"仓库"（去行话，关系适配 §3.3）。无其他改动。

### 发布后反馈

发布时间：
链接：
回复：
收藏：
转发：
高质量反馈：
下一步：

---

## post-2026-05-25-001：最满意的 22 分钟

状态：draft
来源：inbox/2026-05.md#2026-05-24-22-36
首发平台：朋友圈
audience：熟人圈：同事 + tech 朋友 + 家人
是否升级长文：否

### 朋友圈草稿

最满意的 22 分钟。

不是自己花 2 小时逆向 12306 的 API，而是发现 browse.sh 早就有了 12306 的查票方案。

花了 22 分钟验证：从浏览器上下文调接口，返回 15 趟列车实时时刻 + 余票。0 token 消耗。

不重复造轮子不是口号，是工程实践。

完整的 X thread 和笔记在写，晚点发。

### posts-eval

acknowledged: ai-flag:over-structure（短文出现数字 emoji）— eval false positive：正文无数字 emoji (1️⃣2️⃣3️⃣4️⃣5️⃣)；bug 在 `text.count(c)` 对普通数字字符匹配到含 U+20E3 variant selector 的 codepoint 组合。本 post 正文纯文本，无结构化 emoji。

acknowledged: ai-flag:count（1 red flag）— 上述 false positive 的副产品。

### Humanizer

humanizer: zh@2026-05-25 (prompts/humanizer-zh.md vendored fallback by Claude Opus 4.7)

应用项：本 post 正文短且干净（5 句，168 字），无 em dash / 否定排比 / meta-value 断言 / 营销腔。0 处改动。

### 发布后反馈

发布时间：
链接：
回复：
收藏：
转发：
高质量反馈：
下一步：

---

## post-2026-05-26-001：DeepSeek 月度成本 ¥33 vs 海外 ¥8,000+

状态：draft
来源：inbox/2026-05.md#2026-05-25-17-08
首发平台：朋友圈（同步 X thread）
audience：熟人圈：同事 + tech 朋友 + 家人
是否升级长文：否（X thread 先行）

### 一句话观点

¥33 买的不只是 token，是"不用精打细算"的自由。

### 近似实现 / 待查

见 posts/x.md post-2026-05-26-001。

### 朋友圈草稿

5 月 AI 账单：4,155 次调用，410M tokens，¥33.36。

去 OpenRouter 查了同量用 OpenAI / Anthropic 的价格：$1,150 和 $1,280。差 250 倍。

最意外的不在价格本身。在于便宜到一定程度之后，你就不再想优化 prompt 了。完整文件、超长上下文直接丢。¥33 一个月。

某种意义上，AI 普及的根本是调用成本降到了你不用思考的程度。跟模型是不是更聪明没关系。

### posts-eval

acknowledged: ai-flag:over-structure（短文出现数字 emoji）— eval false positive：正文无数字 emoji，bug 在 text.count(c) 对普通数字字符匹配到含 U+20E3 variant selector 的 codepoint 组合。

acknowledged: ai-flag:count（1 red flag）— 上述 false positive 的副产品。

### Humanizer

humanizer: zh@2026-05-26 (prompts/humanizer-zh.md vendored fallback by Claude Sonnet 4.6 + manual touch-up)

应用项：轻量 pass，保留口语节奏

### 发布后反馈

发布时间：
链接：
回复：
收藏：
转发：
高质量反馈：
下一步：

---

## post-2026-05-26-002：API 不平等 — 群里聊出来的灵感

状态：draft
来源：inbox/2026-05.md#2026-05-26-16-30 + 微信群聊
首发平台：朋友圈
audience：熟人圈：同事 + tech 朋友 + 跨境电商朋友
是否升级长文：可联动

### 一句话观点

平台不给 API，AI agent 可以自己去"长"出来。

### 朋友圈草稿

今天群里聊阿里、京东、小红书的 API 问题。一个做亚马逊的朋友说 AI 写 listing 已经很稳，推不上去——因为没 API。

我分享了一下正在做的东西：browse.sh 上有 400+ 网站的内部 API 端点，翻译成本地适配器后，AI agent 能 0 token 直接调用。12306 查票、京东搜索、小红书热门都跑通了。

群里三个人立刻说要去研究。一个朋友已经在想"AI 生成 listing → AI 直接推上亚马逊"。

感觉"API 不平等"这件事，不是只有我在意。发了个 PR：https://github.com/epiral/bb-sites/pull/79

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

## post-2026-05-28-001：合作式监控的盲区

状态：draft
来源：inbox/2026-05.md#2026-05-26-17-45
首发平台：朋友圈
audience：熟人圈：同事 + tech 朋友 + 家人
是否升级长文：否（配合长文 "API 不平等" 支线）

### 一句话观点

需要用数据监控的人，恰好不会把数据给你。这是合作式监控的天然盲区。

### 朋友圈草稿

一个做药品品牌的朋友，讲他们线上控价的流程：

找第三方开发了一套系统。然后——不是爬数据，是一个一个联系平台上的药店，请对方开放自己美团、拼多多、淘宝店铺的 API 授权。用商家自己的账号拉销售数据，汇到总部。

我问：那砸价最凶的那几家，配合了吗？

他沉默了。

不配合。而且恰好是最需要被监控的那些——串货的、异地低价冲量的、来路不明的陌生卖家——一个都不会给你开门。

合作式监控覆盖的，是不需要被监控的人。

而解决这件事不需要对方同意。只要价格挂在公开页面上，就能拿到。

### Humanizer

humanizer: zh@2026-05-28 (prompts/humanizer-zh.md vendored fallback)

### 发布后反馈

发布时间：
链接：
回复：
收藏：
转发：
高质量反馈：
下一步：

---

## post-2026-05-28-002：访谈准备，换了个顺序

状态：draft
来源：inbox/2026-05.md#2026-05-28-15-30
首发平台：朋友圈
audience：熟人圈：同事 + tech 朋友 + 家人
是否升级长文：否（见 x.md 同期 thread）

### 朋友圈草稿

准备一场访谈。以前的做法：拿背景资料，脑暴一堆问题，整理好发过去。

问题挺全。但对方拿到，给的还是准备好的答案。

这次换了顺序。先把对方写过的所有东西灌进 Claude，读完。不急着写问题，先找缝——前后矛盾的地方。

找到之后，Claude 列出来给我。我来判断：哪些是真矛盾，哪些值得追，哪些追下去会好看。判断完，Claude 用对方的原话搭问题。

看清楚这层分工：AI 做穷举，我做筛选。它负责不漏，我负责不无聊。它把材料里所有的矛盾标出来——这是执行层。我删掉九成，只留那几个真正有追问价值的——这是决策层。

以前脑暴，是在自己已有的认知里排列组合。现在 AI 从材料里挖出我不知道的东西，我来判断值不值得追。

一套全新的访谈准备方法：人判断，AI 执行。互不越界。

### Humanizer

humanizer: zh@2026-05-28 (prompts/humanizer-zh.md vendored fallback)

应用项：删 em dash；删「缝」多重定义只留一句；删「根」「着力点」「悬空」等模糊词；删「比任何暖场都管用」等过度总结；新增分工反差（穷举vs筛选、不漏vs不无聊、执行层vs决策层）；结尾四层递进

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
首发平台：朋友圈
audience：熟人圈：同事 + tech 朋友

### 朋友圈草稿

读到一篇蚂蚁的分析文章，里面把 AI 产业切成三个阶段：修路（2022-2026）→ 造车（2026-2028）→ 收过路费（2028-2035）。

我对了一下自己在做的事——0 token 找 API、访谈方法论里 AI 穷举 + 人判断——全落在第二阶段「造车」上。不是刻意选的，是回头看才看清。

知道自己在造车，比不知道自己在干嘛强。方向没偏。

### Humanizer

humanizer: zh@2026-05-28 (prompts/humanizer-zh.md vendored fallback by Claude Sonnet 4.6)

应用项：去「文章在评论区」错误引用；「bb-browser 适配器」改为「0 token 找 API」；删「social content loop」未发布内容；全文无 em dash；无 meta-value 断言。

### 发布后反馈

发布时间：
链接：
回复：
收藏：
转发：
高质量反馈：
下一步：


## post-2026-06-01-001：周榜 5 个高星 AI 项目实测

状态：draft
来源：inbox/2026-06.md#2026-06-01-14-30
首发平台：朋友圈
audience：熟人圈：同事 + tech 朋友 + 家人
是否升级长文：否

### 朋友圈草稿

这周把 GitHub 周榜 10 个项目里值得装的全装了。

5 个实测：Understand-Anything（45.9k 知识图谱）→ markitdown（132k 文档转 markdown）→ ECC（199k skill 库）→ Anthropic 20 个官方插件 → stop-slop（AI 写作痕检测）。

最值的发现：5 个工具刚好串成 Agent 三件套——理解、执行、数据。下周写一下 ECC 那 249 个 skill 怎么快速摸清全貌。

### Humanizer

humanizer: zh@2026-06-02 (prompts/humanizer-zh.md vendored fallback by deepseek-v4-pro)

---

## post-2026-05-30-001：读 MiniMax M2 技术报告

状态：draft
来源：inbox/2026-05.md#2026-05-30-00-30
首发平台：朋友圈
audience：熟人圈：同事 + tech 朋友 + 家人
是否升级长文：否

### 朋友圈草稿

读完了 MiniMax M2 技术报告。

229B 参数，每 token 只激活 4.3%。不是大所以强，是够大但跑起来轻。

最让我在意的：训练阶段就把模型泡在 agent 环境里。不是训好再接 agent，训练本身就是 agent。还有个版本能自己 debug 训练失败。

Agent 的能力不该是接上去的，应该是长出来的。第二阶段 Agent 工具链的窗口，越来越实了。

### Humanizer

humanizer: zh@2026-06-01 (prompts/humanizer-zh.md vendored fallback by deepseek-v4-pro)

应用项：删 em dash、删引号装饰

### 发布后反馈

发布时间：
链接：
回复：
高质量反馈：
下一步：

---

## post-2026-06-03-001：领域垂直 agent 的最小可行解

状态：draft
来源：inbox/2026-06.md#2026-06-02-14-30
首发平台：朋友圈
audience：熟人圈（创业者 / 产品 / 技术朋友）
是否升级长文：否

### 一句话观点

"垂直领域 agent" 不一定要 RAG，当知识源是"一个人、一套方法"时，路由式 SKILL.md + rg 全文检索就够了。

### 朋友圈草稿

刷到一个让我失眠的 GitHub 项目：有人把倪海厦 12 门课全部灌进 Claude Code，做成"中医 Agent Skill"。

3.5M 字、849 个医案、295 star。零 RAG、零 embedding、零向量数据库。

一个 846KB 的 SKILL.md + 46 个 references/ 模块 + 一个 rg 全文检索脚本，完事。

最反共识的事：1M token context 装得下 400 万中文字，"垂直领域 agent"根本不需要 RAG。SKILL.md 不是堆数据，是一张路由决策表——"问症状就加载伤寒-太阳篇，问方剂就加载金匮-方剂索引"。

把"什么时候用什么知识"写死在 prompt 里，比让 embedding 帮你猜，更专业。

参考仓库：JuneYaooo/nihaisha-tcm。

### Humanizer

humanizer: zh@2026-06-03 (prompts/humanizer-zh.md vendored fallback by MiniMax-M3 + manual touch-up)

应用项：
- 删 em dash（"——" 改为逗号）
- 删"我盯着 X 看了半小时"AI 感画面 → "刷到一个让我失眠"
- 数字加粗做节奏（3.5M 字、849 个医案、295 star）
- 收尾"反共识"过度元评论 → 删除，直接收
- 控制在 200 字内，手机屏幕不折叠
- "参考仓库"做社交货币钩子，引导对话

### 发布后反馈

发布时间：
链接：
回复：
高质量反馈：
下一步：

## post-2026-06-04-001：金矿门口开了个直播间

状态：draft
来源：inbox/2026-06.md#2026-06-04-22-30
首发平台：朋友圈
audience：熟人圈：同事 + tech 朋友 + 家人
是否升级长文：否

### 朋友圈草稿

晚上刷到一个直播间，卖 OpenClaw 安装教程，1500 一节课，1000 多人在线。

免费能搜到的命令，为什么有人花 1500 买？"能搜到"和"能看懂"之间有条巨大的沟。

花了一下午调研数字人直播的技术栈、AI 卖课的市场和观众画像。用 AI 数字人卖 AI 知识，可能是今年最土也最实在的变现方式。

方案写完了，明天跑第一步。想聊细节的私我。

### Humanizer

humanizer: zh@2026-06-04 (prompts/humanizer-zh.md vendored fallback by DeepSeek-V4-Pro-A)

应用项：
- 删 "顺着这个逻辑往下想" → 太书面
- "结论是" → 直接说
- 控制在 200 字内，手机不折叠
- 保持对话式，收在 "想聊细节的私我"

### 发布后反馈

发布时间：
链接：
回复：
高质量反馈：
下一步：
