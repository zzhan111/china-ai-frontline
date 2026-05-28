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

今天给即将到来的一场访谈准备问题集。

以前的做法：拿到背景，脑暴问题，整理发过去。问题看起来挺全，但悬空，对方拿到没有任何着力点，给你预备好的答案。

这次换了个顺序：先把所有一手材料读完，然后不急着写问题，先找"缝"——材料之间对不上、说不通的地方。找到缝，校准一遍，再写问题，而且每个问题必须扎在对方真实说过的话上。

最后用被访者自己的原话搭问题。对方感受到"你认真读过我写的东西"，比任何暖场都管用。

AI 帮我做了材料梳理，准备时间从半天压到两小时。

### Humanizer

humanizer: zh@2026-05-28 (prompts/humanizer-zh.md vendored fallback by Claude Sonnet 4.6)

应用项：无需改动，口语节奏自然，无 AI 痕迹标志词，无 em dash，无结构感。

### 发布后反馈

发布时间：
链接：
回复：
收藏：
转发：
高质量反馈：
下一步：
