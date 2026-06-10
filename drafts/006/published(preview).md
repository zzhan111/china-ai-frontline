# Fable 5 封神了吗：一次发布 24 小时内的全面调研

此为临时预览链接，将在短期内失效

---

原创 之哲 之哲 [UIEVENTS事历](javascript:void\(0\);)

在小说阅读器读本章

去阅读

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_jpg/JDDwYKEZ0CwdcCPGOmiaX9YHDib1icibVAaKloBwAj8sGPEo3o5zzMa9zpWovfARCR5f9Vn0dlI1DVicypLia3kaCHJygOAebBXOon9kNsgZcSFt4/640?wx_fmt=jpeg)

Claude深夜炸场！放出"危险级"模型Fable 5

6 月 9 日深夜，Anthropic 发布了 Claude Fable 5 和 Mythos 5。

 

不到 12 小时，中文圈已经出现了一个说法：Claude 史上最强模型，普通人慎用。这个标题同时击中了两个情绪：**新王登基了，而且你可能用不起。**

 

紧接着，更具体的数字开始出现。200 美元的 Claude Max 月费会员，跑 3 个任务就直接烧空。英文社区里有人一个 session 三天烧了 4000 美元。6 月 23 日之后，Fable 5 将从订阅套餐中移除，改为按 usage credits 计费。

 

这些信号叠加在一起，指向的不是一次普通模型升级。

 

我把英文社区、中文社区、官方 benchmark、定价机制和社区争议全部跑了一遍。结论可以三句话讲完。

 

Fable 5 在 coding / agentic 任务上确实是目前最强的。但它只在特定任务上封神。而且它带来的真正变化，不只是能力变强，是三件事同时浮出水面：

 

**[1]** **最强模型开始分层发售**

**[2]** **月卡时代正在结束，前沿模型变成按量燃烧的云资源**

**[3]** **用户以为自己买的是能力，实际买到的可能是一个会被静默降级的模型入口**

 

 

01

 

**它确实很强，**

**尤其是在 Agent 任务上**

 

先说强的部分。

 

从公开 benchmark 看，Fable 5 在软件工程、工具调用、视觉理解、复杂任务自动化上都是明显的第一梯队，多项断层领先。

 

SWE-Bench Pro 上，Fable 5 达到 80.3%，Opus 4.8 是 69.2%，领先 11.1 个百分点。SWE-Bench Verified 上，Fable 5 是 95.0%，Opus 4.8 是 88.6%。FrontierCode Diamond 上，Fable 5 是 29.3%，Opus 4.8 是 13.4%，GPT-5.5 是 5.7%。这些数据来自官方 system card，Vellum 做了完整转引。[1]

 

![](https://mmbiz.qpic.cn/mmbiz_png/JDDwYKEZ0Cy4jKLxZhExyUTWqia0UmVgzwk9vibNPC1f2GUiaYY6xuFdo6FpIppt1hzHJC0s7GKuGBLhs7N4X2JqKMkPibxLiczXcrDjDoEcp7Hg/640?wx_fmt=png)

SWE-Bench Pro 上，Fable 5 达到 80.3%,GPT-5.5 58.6%, Gemini 54.2%，同时Fable 5标价 $10/$50/MTokens

 

这些数字指向同一个结论：**如果你的任务是写代码、改代码、跑复杂工程、接工具链完成长流程，** **Fable 5 是一次明显跨越，不是小升级。**

 

英文社区第一批开发者的反应也印证了这一点。Django 联合创始人 Simon Willison 在 HN 上的评价很直接：他已经在 Claude Code 里花了足够时间，结论是 it's a beast。他把一些拖了几个月的难题扔给它，Fable 5 能相当顺畅地推进。[2]

 

![](https://mmbiz.qpic.cn/sz_mmbiz_png/JDDwYKEZ0CzhOdDJWSSteB3rvianCgLEzkMLga8VxqnfQQBccZuvPLIB9RcmB1AWdOEQOF0EN3ibib6iaVCWX5bR0b93cb7CvArZwpHN46AtWU0/640?wx_fmt=png)

simonw "it's a beast" + kansface / josephg / boc 实测好评

 

另一个用户 boc 提到，高 effort 下跑两个大重构，没有很快撞到 context 上限，感觉它更聪明，也更少在原地打转消耗 token。用户 bottlepalm 说 Fable 5 用 30 分钟完成了 Opus 4.8 和 ChatGPT Codex 5.5 都没解出来的逆向工程题。

 

前端和 UI 场景更典型。Canva 评测负责人 dannyw 的说法是，Fable 5 在**前端 / UI 设计**上是一个 immediate jump，生成结果 delightful without feeling like AI vibe coded。中文 V2EX 里也有人把 Figma 设计稿直接丢给 Fable 5 做前端还原，评价是 1:1 像素级还原，爆杀 5.5。

 

这类反馈之所以重要，是因为它说明 Fable 5 的进步不是「更会聊天」，而是「更会干活」。它强的地方不是回答问题，是推进工作。

 

 

02

 

**但「封神」有边界**

 

问题在于，Fable 5 的强不是无条件的。

 

英文社区的负反馈同样具体。有人拿它做 Stockfish 优化循环，结果无法恢复近期优化，感觉不如 Opus 4.8 有创造力。有人拿它做极难数学题，直接烧穿额度，最后也没有明显答案。

 

METR 的第三方评估结论是，Mythos 5 仍然 likely unable to fully and reliably automate R&D for frontier projects spanning multiple weeks。[3]

![](https://mmbiz.qpic.cn/mmbiz_png/JDDwYKEZ0Cx3rDo4pew6weZpbicVX7aibrVMRfvCeKBqePmVaawx6dn9qvUVbct86L2cicHCUZQzYYEtAEB9cAIzF4eoSfZqeS8zrEK2QJbsmU/640?wx_fmt=png)

METR评估加粗结论截图

 

翻译成白话：**它已经很强，但还不能稳定地替你完成跨数周的前沿研发。**

 

这很重要。今天很多模型发布最容易制造的错觉，是把 benchmark 领先等同于「所有复杂任务都能自动完成」。但真实使用里，agent 任务有一个残酷特点：越长，越容易暴露稳定性问题。**短任务看能力，长任务看链条。**

 

一个模型可以在 30 分钟里显得神勇。到了 3 小时、3 天、3 周，问题就变成了：会不会偏航？会不会重复劳动？会不会误判需求？会不会越改越乱？会不会在中间某一步把前面的约束忘掉？会不会把 token 烧光但没有实质进展？

 

中文社区的分歧也指向同一个结论。有人觉得它已经可以当主力模型。也有人说写文章感觉不如 Opus，AI 味更浓。还有人说写个 CRUD 用得着这么高级的模型吗，普通模型完全够用。

 

这里面的规律很清楚。拿 Fable 5 做高复杂度工程，优势很明显。只让它写普通业务代码、做日常问答、写中文内容，边际收益可能没有价格涨幅那么大。

 

 

03

 

**真正的刺客不是标价**

 

Fable 5 的官方 API 价格是每百万 input token 10 美元、每百万 output token 50 美元，大约是 **Opus 4.8 的 2 倍。**[4]

 

![](https://mmbiz.qpic.cn/mmbiz_png/JDDwYKEZ0CzNWiaNlWOFgLMrggRrtfAaT3unT3d5n1RokkKic0niaCAfQJqcbaBibTKy393ibs2QCawibicjjrys3sAsR641jxicNczBqFbmVK1Ciau0/640?wx_fmt=png)

**Anthropic 官方 13 模型定价表，Fable 5 vs Opus 4.8 高亮**

 

单看标价，一个 200K input + 50K output 的任务大约是 4.50 美元。如果启用 90% prompt-cache，成本可以降到 2.70 美元左右，只比 Opus 4.8 贵 0.45 美元。

 

但这是静态账本。真正的问题发生在 long-running agent loop 里。

 

Agent 不是一次问答。它会读文件、查资料、写代码、跑测试、改错、再读文件、再写代码、再跑测试。只要循环跑起来，token 消耗就像水龙头没关一样持续流出。

 

社区里已经出现了非常夸张的账单。HN 上有人提到，一个 Opus session 三天烧了 4000 美元。OpenCode session 里也出现过 4365.02 美元的实时显示。Lushbinary 的观察是，Fable 5 在 Cursor 这类 long-running agent loop 里连续跑时，token 燃烧容易达到每小时 20 到 40 美元。[5]

 

中文圈的体感更直接。宝玉的原话是：Fable 5 真的消耗流量超快，我刚升级了 200 美元的套餐，根本不够用。卡兹克的说法更夸张：200 美元 Claude Max 会员，跑了 3 个任务，其中一个还没跑完，直接就干没了。

 

这才是 Fable 5 发布真正在改变的账本。过去的订阅制给用户一种错觉：我每月付 20 美元、100 美元、200 美元，就买到了某种「无限接近无限」的使用权。哪怕平台有速率限制，用户心里仍然觉得自己买的是月卡。

 

Fable 5 把这种幻觉打破了。**6 月 23 日之后，Fable 5 将从 Pro / Max / Team / Enterprise 订阅中移除，继续使用需要 usage credits。**用户不再是买一张月卡然后在心理上尽量多用，而是每一次调用都要重新感知成本。

 

据我观察，前沿模型正在从一个类似互联网会员的消费品，变回按量燃烧的云计算资源。这两个东西的商业逻辑完全不同：**过去你订阅的是一个 AI 助手，以后你调用的是一台昂贵的智能机器。**

 

 

04

 

**静默降级，才是真正的不平等**

 

如果只是贵，其实还不算最严重。贵至少是透明的。你知道价格，你可以选择用或者不用，可以在高价值任务上调用 Fable 5，在普通任务上切回便宜模型。

 

真正麻烦的是**静默降级。**

 

Fable 5 和 Mythos 5 的关系，很像同一套能力在不同安全边界下的两个版本。公开面向普通用户的是 Fable 5；Mythos 5 是更受限、更高能力、只开放给部分 Project Glasswing 合作伙伴的版本。

 

**在一些 cyber / bio / chemistry 查询上，Fable 5 会触发 safety classifier，然后回退到 Opus 4.8。**Anthropic 自报触发率低于 5% session，但社区反馈里，对这个分类器过度敏感的吐槽非常多。实验室自动化、健美研究、MRI 脑分割、蚊子疟疾都可能触发限制。

 

这里不讨论限制本身是否合理。更关键的问题是：用户是否知道自己正在被降级？

 

如果你付的是 Fable 5 的价格，但某些任务实际拿到的是 Opus 4.8 的答案，而且系统没有明确告诉你，这就是信息不对称。

 

这是英文社区争议最大的地方。HN 上有人把这种机制类比成社交平台的 shadow banning：不是直接告诉你「这不允许」，而是不声不响地改变你的问题、改变你的回答，甚至降低模型能力。HN moderator 原话是：**Anthropic won't tell you if your output is being silently nerfed。**[2]

 

Reddit r/ClaudeAI 上一篇高赞帖子标题直接叫：Claude Fable 5 feels less like a model launch and more like a preview of AI inequality。[6]

 

![](https://mmbiz.qpic.cn/sz_mmbiz_png/JDDwYKEZ0Cz07eGVeZrWubVhJpmYqjhwTdYtbW6RVrxpvUQvtT0LqIt0ic9lYF1eTyxv9832TF8aqKRwOic04SXQZLKic1HQLswU2pwTtTKAO0/640?wx_fmt=png)

Reddit帖子正文 +1928赞 /3465 评论数字

 

这句话比所有 benchmark 都更值得警惕。它意味着未来模型竞争不只是能力竞争，也是透明度竞争。用户真正害怕的不是模型说「我不能做这个」，**而是模型看起来正常工作，但实际上已经换了脑子、降了能力、改了输出，而你不知道。**

 

这会实实在在影响开发者的判断。你可能以为是自己 prompt 写得不好，以为任务本身太难，以为是模型能力退化，甚至错误地调整整个产品路线。但真实原因可能只是某个看不见的分类器触发了。

 

 

05

 

**中文圈看到的是另一层问题**

 

英文社区关心能力、账单和安全边界。中文开发者还会多一层现实问题：**怎么用得上，怎么用得起。**

 

从调研看，中文圈很快出现了几条路径。第三方中转站（APIYI、赞 AI、OpenRouter、AnySearch、Cubence），卖点是人民币充值、折扣、转发官方资源。虚拟卡加官方账号（WildCard / Depay）。云平台路径（AWS Bedrock），V2EX 上有人提醒 Fable 既然上了 Bedrock，那些云 MaaS 路径大概率不会下。

 

按 1 美元约 7.25 人民币换算，Fable 5 输入约 72.5 元每百万 token，输出约 362.5 元每百万 token。月成本估算（10M 输入 + 2M 输出）约 1450 元。**24 小时长链 Agent 任务轻松破万。**

 

这些讨论看起来像薅羊毛指南，但背后是一个更大的信号：当模型越来越强、越来越贵、越来越不透明，用户会自然寻找中间层。中转站、云平台、代理层、模型路由、预算控制、缓存系统，都会变得更重要。单个用户已经很难直接面对前沿模型的复杂商业规则。

 

这个判断也呼应了我在 agent 工具链上一直关注的线。**模型越强，越需要工具链来管。模型越贵，越需要预算控制。模型越不透明，越需要观测层。模型越分层，越需要路由和替代方案。Fable 5 没有让工具链变得不重要，它让工具链变得更重要了。**

 

 

06

 

**这不是一次模型升级，**

**而是一次订阅体系调整**

 

APPSO 在 Fable 5 发布后的判断是：**与其说是一次模型升级，倒不如说是一次彻底调整 AI 订阅体系的预热。**[7]

 

![](https://mmbiz.qpic.cn/mmbiz_png/JDDwYKEZ0Cy4peLBvzf2RLqjRn82SlpRZO2t0HBI6LpbsNC1epQszEAEdMhSCsN79yOfgxkLeZAhiamhF8hEu2ry5a48dYQZOGTyZNaEXo8E/640?wx_fmt=png)

Anthropic 官方推特发布 Fable 5

 

我同意这个判断。如果只看能力，Fable 5 的故事会被写成：Claude 又变强了，coding 更强了，agent 更强了，benchmark 又刷新了。但如果把定价、订阅、分层发售、安全分类器、静默降级、社区账单放在一起看，**它更像一个行业拐点。**

 

前沿模型不再假装自己是普通消费级软件。它开始回到自己的真实形态：昂贵、稀缺、分层、按量计费、对不同用户开放不同能力。

 

过去一年，很多人已经习惯了一个窗口期：每月几十美元就能使用接近前沿的模型能力。这个窗口期让大量个人开发者、独立创作者、小团队获得了前所未有的杠杆。**但 Fable 5 之后，这个窗口期可能开始收窄。不是说普通人不能用了，而是「最前沿能力随便用」的时代正在结束。**

 

这会影响整个生态。个人用户会更谨慎，开发者会更重视成本控制，创业公司会重新计算毛利，agent 产品会被迫设计预算上限。digitaltrees 为 propelcode.app 转向 3 台 512GB Mac Studio 跑开源模型，不一定是主流选择，但它代表一种情绪：**如果闭源模型越来越强、越来越贵、越来越不透明，总会有人选择把能力拿回自己手里。**

 

06

 

**回到最开始的问题**

 

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/JDDwYKEZ0Cxs3zr6jnH27YOlJJ3ve7ABQnumOjl2QqHRfsZA4ycGRtFcaiapgcwzSCZYNibkBhMhpzWZ0v5MXkv1UwlGwGk6RhtJbIGe8pS0w/640?wx_fmt=jpeg)

**回到最开始的问题：Fable 5 真的封神了吗？**

 

如果你问的是 coding benchmark，它封了。如果你问的是 agentic workflow，它很接近。如果你问的是前端还原、复杂工程、长上下文工具使用，它确实是一次非常明显的跃迁。

 

**但如果你问的是** **普通用户能不能放心无脑用，答案是否定的**。如果你问的是它能不能稳定接管数周级研发项目，答案也是否定的。如果你问的是付了 Fable 5 的钱，是不是一定能拿到 Fable 5 的完整能力，答案更是否定的。

 

Fable 5 不是一个「神降临了」的故事。它是一个分水岭。在它之前，很多人还相信 AI 前沿能力会以月卡形式持续普惠。在它之后，我们要开始接受另一个现实：**最强能力会越来越贵，越来越分层，越来越按量计费。**

 

这篇调研跑完之后，我留下的不是兴奋，而是一个更实际的判断：未来真正有价值的，不只是会调用最强模型的人。是把强模型、便宜模型、开源模型、中转服务、缓存、预算、评测和降级监控组织成一套稳定工作流的人。

 

**模型封神只是新闻。谁能把神请进生产系统里，还不把账单烧穿，才是下一阶段真正的能力。**

 

参考资料

[1] Vellum: [Claude Fable 5 and Mythos 5 Benchmarks Explained](https://www.vellum.ai/blog/claude-fable-5-and-mythos-5-benchmarks-explained)

 

[2] Hacker News: [Claude Fable 5 discussion](https://news.ycombinator.com/item?id=48463808)

 

[3] Anthropic: [Fable 5 System Card](https://www-cdn.anthropic.com/d00db56fa754a1b115b6dd7cb2e3c342ee809620.pdf)

 

[4] Anthropic: [Claude pricing documentation](https://platform.claude.com/docs/en/about-claude/pricing)

 

[5] Lushbinary: [Claude Fable 5 vs GPT-5.5 vs Gemini 3.1 Pro comparison](https://lushbinary.com/blog/claude-fable-5-vs-gpt-5-5-vs-gemini-3-1-pro-comparison/)

 

[6] Reddit: [Claude Fable 5 feels less like a model launch and more like a preview of AI inequality](https://old.reddit.com/r/ClaudeAI/comments/1u1fsdi/claude_fable_5_feels_less_like_a_model_launch_and/)

 

[7] APPSO: [实测 Claude 史上最强模型 Fable 5，普通人慎用](https://mp.weixin.qq.com/s/1iKHpL0g2iKK0ztojOqZzw)

修改于
