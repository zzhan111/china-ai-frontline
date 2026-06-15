# 国产替代 vs Fable 5：一次出口管制如何引爆中国 AI 的「开源起义」

原创 之哲 [UIEVENTS事历]

---

6 月 12 日，一个开发者在 V2EX 上发了一条帖子。[1]

"There's an issue with the selected model (claude-fable-5). It may not exist or you may not have access to it."

这不是 bug。Anthropic 执行了美国政府的指令：暂停所有外国公民对 Fable 5 和 Mythos 5 的访问权限。

帖子下面 15 条回复。有人截图了自己的 Claude Code 终端，红色的报错信息刺眼地躺在黑色背景上。有人问「被误封了怎么办」。有人说「换 Kimi 吧」。

最后这个人说的对。但不是「换 Kimi」这么简单。

52 小时后我回看这场封锁，发现中国 AI 社区没有在等。但真正让我意外的不是他们做了什么，是大洋彼岸的英文社区用脚投票的速度比中文社区还快。

---

## 一、48 小时内，发生了什么

Fable 5 被封的那一刻，整个事件的走向其实是可以预测的。

第一步，愤怒。Hacker News 上「Statement on US government directive to suspend access to Fable 5 and Mythos 5」冲到了 #1。截至 6 月 14 日 08:54，**3,055 人点赞，2,190 条评论。** 中文互联网上，「美国突然限用 Claude 5 说明了什么」登上头条热榜 #7，954 万热度。

第二步，吃瓜结束。48 小时后，这条头条从 954 万暴跌到 36 万，排名从 #7 跌到 #40。微博热搜 50 条，0 条 AI 相关。大众层退场了。

第三步不是「什么都没发生」。

第三步是 **开发者层开始行动了。**

微博 0 条 AI 热搜的同一天，V2EX 上有 86 条 AI 讨论在活跃。不是在围观，是在动手。「领赛博鸡蛋啦，自建中转，送 $50 永久额度」，497 条回复。另一条「# 自己搭的 AI 中转站，给 V 友送点福利$15」，同期从 58 条回复涨到 77 条，4 小时内涨了三分之一。

与此同时，Hacker News 上「Open source AI must win」从 #3 升到了 #2，1,510 人点赞。GLM 5.2 的帖子在 4 小时内从 120 分涨到 310 分。**6 倍跃升**，直接冲到 HN front page #2。到我写下这段文字时，这个帖子已经涨到了 **332 分，187 条评论**，而且还在往上走。

一个国产开源模型，在英文社区主战场，排在全站第二。

**这是第一次。**

---

## 二、GLM 5.2：不是在比赛，是在填空

Fable 5 不是一般的强。两周前我写过一篇它的全面调研[2]：Django 联合创始人 Simon Willison 在 HN 上的评价是 **it's a beast。** SWE-Bench Pro 上 **80.3%**，FrontierCode Diamond 上 **29.3%**，在 coding 和 agentic 任务上是 **断层领先。** 卡兹克说 200 美元 Claude Max 会员跑了 3 个任务就烧没了。宝玉说刚升级的套餐根本不够用。英文社区里有人一个 session 三天烧了 4000 美元。

Fable 5 是真的很强。而且 **真的很贵。**

GLM 5.2 不是突然出现的。智谱在 Fable 5 被封之前就已经发布了它。Reddit r/LocalLLaMA 上，24 小时内有三条 GLM 5.2 的帖子排进了前 18，最高一条 283 分，58 条评论。

但 Fable 5 被封之后，GLM 5.2 的定位发生了质变。它不再只是「又一个国产开源模型」。它变成了 **Fable 5 的最直接替代选项。**

MIT 开源协议。1M context 支持。全量开放。

这三个关键词打在了 Fable 5 的痛点上。不是技术上超越了 Fable 5——在 raw coding 能力上，差距仍然存在。但 GLM 5.2 提供了一件 Fable 5 永远无法提供的东西：**不可封锁。**

而且 **不烧钱。**

6 月 14 日凌晨 05:00，GLM 5.2 在 HN 上是 #10，120 分。到 08:54，它到了 #2，310 分。4 小时内涨了 190 分。zai-org/GLM-5 的 GitHub 仓库拿到了 3,412 颗星。

在 HN 的帖子里，Z.ai（智谱）的创始人写了这样一段话：[3]

> "Today, the sudden restriction of certain frontier models is deeply regrettable. At a time when access to frontier models is abruptly cut off for non-technical reasons, we are even more convinced of one thing: science should be global. The path to AGI must never be enclosed by high walls."

这段话下午被 AI 圈刷屏。中文版更直接：「前沿智能，不该只属于少数人，也不该被少数规则随时收回。它应该开放、可用、可构建，服务每一位开发者。」

V2EX 上，有人用 GLM 5.2 跑了一个实战项目：「使用 glm5.2 完成了一个复杂 2d 渲染桥接引擎，很强，opus 级别的。」[4]

**很强，Opus 级别的。**

这不是官方 benchmark。这是一个真实用户，在真实项目里跑完之后的评价。

6 月 13 日深夜，新智元发了一篇头条：「Fable 5 突遭下架，GLM-5.2 全量开放！」[5]。文章里引了另一位内测用户的原话：「用过 5.2 回不去 5.1 了，在大项目里面有种 4.7 到 5 的跨越式进步。上头的感觉。」知乎上有人说：「从下周开始，通过中转站用 Opus 的人必须面对一个问题——你用的 Opus 如果是 GLM-5.2 冒充的，你可能分辨不出来，甚至表现更好。」

这些声音的方向完全一致：**GLM 5.2 在真实 coding 场景里，已经摸到了 Opus 级别的门槛。**

同一天，量子位的头条是「实测小米最快 1T 大模型：吞吐量每秒 1000+ Tokens，Vibe Coding 七秒交付」。36氪的头条是「月之暗面们重写估值游戏规则」——注意那个「们」字。阿里和百度在同一天推出了高考志愿填报 Agent，一个免费，一个主打「真人专家验真」。

**不是一家公司在做。是一个生态在形成。**

---

## 三、Kimi K2.7：另一条线，同一个困境

GLM 5.2 不是唯一一个在 HN 上顶刊的国产模型。

Kimi K2.7-Code 是月之暗面推出的开源 coding 模型。它稳居 HN best #16，截至 08:54 是 444 分，**24 小时以上的顶刊。** Hacker News 的 best page 是按得分和时间加权排的，相当于「全站历史上最好的帖子」。一个国产 coding 模型能在上面待 24 小时，本身就是信号。

但 Kimi K2.7 的故事还有另一面。

官方的卖点是「更好的 token 效率」。V2EX 上的实测反馈是：「Kimi2.7 很拉！且 Token 消耗增高而不是所谓的减少 30%」。这条帖子 4 小时内从 5 条回复涨到了 10 条，**翻了一倍。**

为什么会这样？

因为 **Kimi K2.7 也带了反蒸馏机制。** 和 Fable 5 一模一样。

一个月前，量子位写过一篇专题：「Fable 5 自带反蒸馏机制！检测到就降智，误触率高到离谱」。现在同样的批评落到了国产模型身上。这不是 Fable 5 的专利，是前沿模型的通用困境：想防止被蒸馏就得多烧 token，多烧 token 用户体验就崩。

**国产模型在「安全」和「体验」之间，也在走 Fable 5 的同一条钢丝。**

这不是一个令人振奋的发现，但它是诚实的。它说明国产模型不是在重复造轮子，而是在重复造同一个问题。**重复同一个问题，意味着它们已经进入了同一个竞技场。**

---

## 四、监管没有停在 Anthropic

Fable 5 被封的时候，很多人觉得这只是 Anthropic 一家的合规问题。

但如果回看 Fable 5 发布后的两周，信任的裂缝其实比「被封」更早出现。Fable 5 的官方 API 价格是 Opus 4.8 的 **2 倍**——input $10/M、output $50/M。[2] 长任务里 token 燃烧轻松达到 **每小时 20 到 40 美元。** 更隐蔽的是 **静默降级**：在某些 cyber / bio / chemistry 查询上，Fable 5 会触发 safety classifier，然后**不声不响地回退到 Opus 4.8。** 用户付的是 Fable 5 的价格，实际拿到的是 Opus 4.8 的答案。HN 上有人把这种机制类比成社交平台的 shadow banning。[2]

贵至少是透明的。**静默降级是不透明的。** 6 月 23 日之后，Fable 5 将从订阅套餐中移除，改为 usage credits 计费——前沿模型正在从「互联网会员产品」变回「按量燃烧的云计算资源」。[2]

被封只是最后一张多米诺骨牌。倒之前，信任已经在裂了。

而 6 月 14 日上午的数据表明，监管远没有停在 Anthropic。

Hacker News 的 1 小时窗口里出现了一条新帖：「US Secretary of War Comments on Anthropic」。美国战争部长公开评论 Anthropic。12 分，2 条评论，刚刚发出。需要说明的是，这是一条刚冒出来的帖子，内容尚未交叉验证。但标题本身就是一个信号级别跃迁：**从商务部的出口管制，跳到了国防部的公开表态。**

同期，HN front page #24 是「State Attorneys General Are Investigating OpenAI」。州级检察联盟启动对 OpenAI 的调查。17 分，2 条评论。

而那条 WSJ 独家——「Amazon CEO's talks with U.S. officials triggered crackdown on Anthropic models」——已经从 05:00 的 307 分涨到了 08:54 的 511 分。**4 小时内涨了 204 分。**

**商务部。战争部长。州检察联盟。** 三个不同层级的监管力量在一个周末里先后浮出水面。

Fable 5 的封锁不是终点。它是一张多米诺骨牌的第一张。如果监管继续扩散到 OpenAI、Google、Meta，「去美国云 API 化」就不再是中国开发者的应激反应，而是 **全球开发者的必然选择。**

V2EX 上已经有人在问了：「现在有哪些国内公司能够无上限用 Claude Fable 5？」34 条回复。

另一条：「订阅制还能持续多久呢？oai 和 anthropic 的订阅制都是赔本赚吆喝吧？」34 条回复。

同一时刻，36氪的 AI 频道头条是「志愿填报 Agent：腾讯克制，阿里激进」。当美国在讨论「谁能用 Fable 5」的时候，中国的大厂已经在讨论「Agent 应该免费还是收费」。

**这不是技术讨论。这是商业信任的崩塌与重建，同时发生在太平洋两岸。**

---

## 五、「温差」

有一个数据值得单独拿出来说。

Fable 5 被封 48 小时后，微博热搜 50 条，0 条 AI 相关。

如果你只看微博，你会以为中国互联网已经忘了 Fable 5。

但同一时间，V2EX 上有 86 条 AI 讨论在活跃。「自建中转站」的帖子 4 小时内从 58 条回复涨到 77 条，涨了三分之一。36氪的 AI 频道头条是「月之暗面们重写估值游戏规则」——再读一遍那个「们」字。量子位的头条是「中国第一、全球第二！HiDream-O1-Image-1.5 登顶文生图榜单，超越谷歌、英伟达」。HN front page #2 是 GLM 5.2。

我管这个叫 **「温差」。**

**大众层在吃瓜，开发者层在动手。** 两个层的温度完全不一样。而决定 AI 行业走向的，从来不是前者。

1943 年，IBM 总裁托马斯·沃森说过一句著名的话：「我觉得全世界大概只需要 5 台计算机。」他看的是大众层。

2026 年 6 月 14 日，微博热搜 0 条 AI 相关。但 V2EX 上一个自建中转站的帖子 4 小时内多了 19 条回复。36氪的头条里藏着那个「们」字——不是「月之暗面」，是 **「月之暗面们」。**

大众层看到的永远是「美国突然限用 Claude 5 说明了什么」，一个需要被解释的事件。开发者层看到的是「订阅制还能持续多久」，一个需要被解决的机会。

**这就是温差。**

---

## 六、不是替代，是填空

52 小时后，我的判断是三句话。

Fable 5 的封锁不是在创造「国产替代」的需求。这个需求本来就在。封锁只是把时间表提前了。GLM 5.2 的 6 倍跃升、Kimi K2.7 的 24 小时顶刊，不是因为国产模型突然变强了，而是因为 **Fable 5 留出了一个它本来占据的位置。**

但替代不是终点，**填空才是。** 国产模型填的不只是 Fable 5 的 coding 能力缺口。它们还在填反蒸馏的坑，填 token 效率的坑，填 Opus 级别实战的坑。这条路 Fable 5 走过一遍，国产模型正在重走。不同的是，Fable 5 被封之前是一个人走，**国产模型是一群人走。**

如果美国 AI 监管继续从 Anthropic 扩散到 OpenAI、Google、Meta——战争部长已经开口，州检察联盟已经动手，Amazon CEO 的那通电话已经被 WSJ 写成了独家——那么「去美国云 API 化」将不再是中国开发者的话题，而是 **全球开发者的共识。** 到那一天，GLM 5.2 在 HN 上的 #2 就不是一个意外。**它是一个预演。**

Fable 5 被封的那一刻，很多人在愤怒。52 小时后，很多人在动手。

**愤怒会过去。动手的人会留下来。** 而留下来的人会发现，他们不是一个人在走，他们身边有一整个正在形成的生态。

---

*全文约 3,400 字。*

## 参考资料

[1] V2EX: [There's an issue with the selected model (claude-fable-5)](https://v2ex.com/t/1219959)，2026-06-12

[2] 之哲，[Fable 5 封神了吗：一次发布 24 小时内的全面调研](https://mp.weixin.qq.com/s/...)，2026-06-10。文中引用的 Fable 5 成本数据（$200/3 任务、$4000 session、$20-40/h）、SWE-Bench Pro 80.3%、Simon Willison "it's a beast"、静默降级机制均来自此篇。

[3] Hacker News: [GLM 5.2 Is Out](https://news.ycombinator.com/item?id=48518684)，Z.ai 创始人声明出现在评论区首位（easygenes 引用），2026-06-14。实时验证得分 332 分 / 187 评论。

[4] V2EX: [致开发者：GLM-5.2 全量开放，前沿智能属于所有人](https://v2ex.com/t/1220146)，2026-06-13

[5] 新智元，[Fable 5 突遭下架，GLM-5.2 全量开放！](https://mp.weixin.qq.com/s/qcw-3FcVnAZ0AxYU471nUQ)，2026-06-13 22:24。AICodeKing 评价由新智元转引，未独立交叉验证。

[6] Hacker News: [Open source AI must win](https://news.ycombinator.com/item?id=48511908)，2026-06-13。实时验证得分 1,510 分。

[7] Hacker News: [Amazon CEO's talks with U.S. officials triggered crackdown on Anthropic models](https://news.ycombinator.com/item?id=48519092)，WSJ 报道，2026-06-13。实时验证得分 511 分。

[8] Hacker News: [Kimi K2.7-Code: open-source coding model with better token efficiency](https://news.ycombinator.com/item?id=48502347)，2026-06-13。实时验证得分 444 分。

其他数据来源：Hacker News front/best/Show HN（2026-06-14 05:00 + 08:54 CST 双窗口抓取），HN Algolia API，V2EX hot/tech/AI/all（HTML 解析），头条 hot-board（HTML 解析），微博热搜 Ajax API，GitHub trending，36氪 AI 频道，量子位首页。
