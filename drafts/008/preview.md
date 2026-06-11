# 达里奥的"树懒"提案：Anthropic CEO 为什么现在主动求监管？

此为临时预览链接，将在短期内失效

---

原创 之哲 之哲 [UIEVENTS事历]

解读 Anthropic CEO 达里奥·阿莫代伊万字长文。

**Dario Amodei** 的新长文用了一个很聪明的比喻。

《指环王》里的树人 Treebeard 太慢了。霍比特人想让祂去保卫森林，但祂光跟另一棵树打招呼就得花一整天。Dario 说，今天的 AI 和政策系统之间就是这种关系——AI 在指数加速，立法按制度惯性挪动，中间的时间差越来越大。

但这不是重点。

重点是这篇文章争的，已经不是"AI 要不要监管"。它争的是：在一个按指数曲线移动的技术系统面前，谁有资格定义"安全"，谁有资格定义"前沿模型"，谁有资格定义"不可接受风险"。

**Dario 给出的答案是他自己——或者说，以 Anthropic 为代表的"负责任的前沿模型公司"。**

Hacker News 给出的反应是 138 points、198 条评论——以及用户 slopinthebag 那一句被顶到最高处的话[1]

**"目前领先的公司，希望用国家监管权力阻止竞争者追上自己。"**

这就是这篇文章真正值得写的地方。

01

**万字政策提案，核心只有四件事**

Dario 这篇文章原文超过一万字，覆盖监管、宏观经济、科学创新、公民自由、地缘竞争五个方向。但如果只抓他最想让监管者带走的东西，是四件事。

**第一，前沿模型必须接受第三方强制测试。**

超过一定算力阈值的前沿模型，不能只靠公司自己声明"我们测过了，没问题"。需要像飞机、汽车、药品上市前经过安全认证一样，接受外部评估。第三方可以是类似美国联邦航空管理局（FAA）的政府机构，也可以是被政府授权的私营评估机构。[2]

**第二，政府应该有权阻止危险模型部署。**

如果评估显示某个模型在四类特定风险上不可接受——网络安全、生物武器、AI 系统失控、以及会加速这些风险的自动化研发——政府应该有权阻止或威慑它的发布。Dario 强调这不是让政府做政治审查，这条权力必须"有保护措施防止政治偏袒或任意决策"（原文原句："protective measures against political favoritism or arbitrary decisions"）。

**第三，模型权重要有强安全标准。**

前沿模型公司必须保护模型权重，定期做红队测试和渗透测试，和政府一起防御重大威胁行为者。Dario 没有直接写**"禁止开权重模型"**，但这部分被开源社区视为整篇文章最敏感的潜台词。

**第四，就业替代必须提前准备。**

如果 AI 真能完成大多数认知任务，Dario 认为传统的"技术会创造新工作"的叙事可能不够用了。他提出的工具包括：更精细地衡量 AI 就业影响（Anthropic 自己已运营 Economic Index 近一年半[^3]）、工资保险（换工作后补足新旧工资差额）、留岗税收激励、劳动力培训、以及在极端情况下用全民基本收入或提高资本利得税提供长期收入支持。[3]

这四件事放在一起，有一个共同的逻辑：

**前沿模型已经不只是消费级软件。它更像民航客机、更像药物、更像具有大规模杀伤潜力的两用技术。**

既然如此，就不能再按互联网产品的逻辑管它。

02

**从"透明度"到"否决权"：Dario 为什么现在转向**

Dario 不是第一次写政策文章。把时间线拉长，能看到三篇递进的文章：

**1. 《On DeepSeek and Export Controls》——把算力看作国家安全资源**

**2. 《The Urgency of Interpretability》——把模型可解释性看作技术治理前提**

**3. 《Policy on the AI Exponential》（本次）——把立法速度看作下一阶段最大瓶颈**

这次论述整体立法框架，是三篇的收口。

但这次和前两次有一个关键区别：前两次的政策主张主要落在"披露"和"研究"层面，没有直接触及一个核心问题：**某个模型能不能被阻止发布。**这次触及了。

Dario 在文中解释了为什么以前不主张这么硬的监管。2023–2024 年，AI 风险还处在"可能会出现，但不知道以什么形式"的阶段。他原话说得很坦率：

如果提前把监管条文写死，可能出现的情况是，一些后来证明无关紧要的合规要求消耗了公司 95% 的能力，而真正危险的源头完全不在条文覆盖范围内。

所以他当时支持的是透明度路线——要求模型公司披露安全流程、测试方法、重大事故。他也确实推动 Anthropic 支持了加州 SB 53、纽约 RAISE、伊利诺伊 SB 315 等州级透明度立法。[4]

现在他认为情况变了。他的判断基于一个具体信号：**前沿模型在网络安全能力上的跃迁。**

他在文中点名 Claude Mythos Preview 的测试结果，说它"**证明 AI 已经是具有国家和全球战略意义的工具**"[^5]。他同时暗示生物风险和自主性风险可能紧随其后。

于是他从"透明度"转向"强制测试 + 政府否决权"。这个转向有事实基础——scaling laws 已有 10 年以上实证支撑[^6]，过去四年模型能力也确实在急速上升。但也正是这个转向，把争议推到了顶点。[^6]:

因为一旦进入"政府可以阻止模型发布"的领域，讨论就不再是"AI 有没有风险"，而是

**"谁来定义风险，谁来执行阻止，谁来监督执行者"。**

而这些问题的答案，和 Anthropic 作为头部模型公司的利益关系高度纠缠。

03

**社区反弹的不是"安全"，是"谁定义安全"**

截至 2026 年 6 月 11 日 HN 数据（138 pts / 198 comments / 46 top-level，来源：HN Algolia API，整理于 `REPORT.md`），几乎没有评论在认真争论"AI 完全没有风险"。真正的反弹聚集在三个方向上。

**第一个方向：监管捕获。**

这是反对声中最主流的一路。直接引用 HN 用户 slopinthebag 的高赞评论：

"The company currently on top wishes to use the regulatory power of the state to prevent competitors from encroaching on their market dominance."

逻辑很直接：前沿 AI 本就有极高门槛——巨额算力、数据工程、顶级人才。如果强制测试、第三方审计、权重安全标准、政府备案、事故报告再变成硬性要求，合规成本会进一步向少数公司集中。这并非 AI 行业独有的问题，而是所有被监管行业的经典困境。

这不是 AI 行业独有的指控，它是所有被监管行业的经典问题。前沿 AI 本来就有极高的技术和资本门槛——巨额算力、数据工程、顶级人才、推理基础设施。如果强制测试、第三方审计、权重安全标准、政府备案、事故报告再变成硬性要求，合规成本会进一步向少数公司集中。

**第二个方向：强制闭源。**

HN 用户 kouteiheika 的评论直接把潜台词挑明了：

"Make open-weight models illegal. It's nice for Dario to come out and say this so explicitly."

Dario 写的是"模型权重要有强安全标准"，没有写"禁止开源"。但开源社区的逻辑很清晰：一旦前沿模型权重被定义为需要严密保护的高风险资产，open-weight 模型即使不被明令禁止，也会在合规成本、发布审查和公众信任上面临越来越不利的位置。HN 用户 kouteiheika 的评论直接把潜台词挑明了："让开源权重模型非法化。Dario 说得很直白。

**第三个方向：叙事信任。**

HN 用户 SkitterKherpi 指出了时间点的敏感性：

"It is impressive how well they've scheduled all their releases, posts, and other news to dominate the tech news cycle almost every day in this pre-IPO phase."

在 pre-IPO 阶段，他们把所有发布、文章和新闻排得每天霸占科技新闻周期，这节奏令人印象深刻。"在这个节点上，CEO 站出来说"我们需要让政府有权阻止危险模型部署"，外界很难只从公共利益角度去理解它。

这三个反弹方向有一个共同点：它们质疑的不是 Dario 对风险的判断，而是 Dario 的公司身份和他提出的制度方案之间的关系。社区不是在说"AI 不危险"——社区在说：

**就算 AI 危险，为什么由你来告诉我们该怎么管？**

04

**承认风险是一回事，设计规则是另一回事**

这里需要做一个区分。

Dario 对 AI 风险的判断，很多是成立的。前沿模型能力确实在快速上升（四年从"勉强写一行代码"到"写主要 AI 公司大量代码"，原文原句[^7]）。政策系统确实跟不上。风险也确实不能只靠公司自律。就业替代如果等到大规模发生再讨论，成本会高得多。模型权重、网络安全、生物安全、自主性风险——都不是能用"市场自己会调整"带过的问题。[^7]:

**但承认这些，不等于接受他的方案。**

监管不是抽象的善意。它一旦落地，会变成非常具体的东西：算力阈值谁设？第三方评估机构由谁授权？政府否决权如何防滥用？权重安全标准怎样区分危险发布和合法开源？小团队有没有能力承担合规成本？模型被阻止发布时开发者有没有申诉渠道？

Dario 的叙事把问题框定为"AI 太快 vs 政策太慢"。在这个框架里，最大危险是 Treebeard 再不动，森林就要被砍掉。

社区的叙事把问题框定为"公共安全 vs 监管捕获"。在这个框架里，最大危险是 Treebeard 被霍比特人带着跑，却不知道目的地是霍比特人选好的。

两个框架都不是假的。这里藏着一个 AI 治理最根本的矛盾：

**承认风险真实存在的人，往往也是能从监管中获益最多的人。**

这不是说他们虚伪，只是说他们不可能是中立的规则设计者。没有任何一家前沿模型公司是。

05

**这篇文章真正的信号：制度竞争开始了**

如果只把这篇文章读成"AI 安全文章"，会低估它。

它更应该被读成一个信号：**前沿模型公司的竞争正在进入一个新维度。**

过去两年，模型竞争的主要维度是技术——谁的模型更强，上下文更长，代码更好，agent 更稳定，API 更便宜，多模态更自然。这些是开发者、投资人和媒体最关心的事情。

但接下来，会有一个新维度越来越重要：

**制度竞争**

谁能进入企业和政府采购？谁能获得监管信任？谁能证明自己的安全体系更成熟？谁能参与制定评估标准？谁能把自己的内部安全流程变成行业模板？谁能让公众相信自己不是失控的技术加速器？

Dario 这篇文章正在争夺的，就是这些东西。

它告诉监管者：我们已经替你想好了框架——五个政策方向、四类风险、三种评估模式、就业政策工具和资金来源方案。

它告诉公众：我们支持过加州 SB 53、纽约 RAISE、伊利诺伊 SB 315 这些透明度立法，运营了 Economic Index 追踪 Claude 的经济影响近一年半，**现在愿意接受更严格的联邦级监管。**

它也告诉竞争对手：下一阶段，不光要比模型能力，还要比谁更像一个可以被制度信任的玩家。

这就是 Anthropic 一直在建立的差异化——在一个所有前沿模型公司都必须商业化的阶段，"负责任"不再是公益口号，而是竞争策略。但也正因为如此，外界才更需要保持审视：当一家公司的核心品牌资产就是"我们更安全"，它天然有动力把安全标准设计成最有利于自己的形态。

但也正因为如此，外界才更需要警惕。

**当一家公司的核心品牌资产就是"我们更安全"，它天然有动力把安全标准设计成最有利于自己的形态。**

这不说明它虚伪——只说明它不是中立者。

06

**有一件事比"Dario 对不对"更重要**

中文 AI 圈对这篇文章的关注，目前还远不如对产品发布和模型能力的关注。这不奇怪。一篇万字政策文章，没有跑分、没有截图、没有"吊打"叙事，天然不在流量中心。[^8]

但这篇文章可能比很多产品发布更值得花时间。

产品热点的生命周期很短，一个模型发布几天后就被下一个覆盖。但如果前沿模型监管真的开始围绕"强制测试、权重安全、第三方评估、政府否决权"展开——Dario 在文中已明确呼吁配合 MATCH 和 OVERWATCH 这两个正在推进的立法提案——那么今天这些看起来有点枯燥的政策语言，会在未来几年反复出现。[^9]

很多行业变化，最早都不是以爆炸新闻的形式出现的。它们先出现在一篇政策文章里、一次听证会里、一个行业框架里、一个大公司 CEO 的公开信里。刚开始看像姿态，后来变成共识，再后来变成门槛。

Dario 这篇文章未必会原样变成法律。但它大概率会进入政策讨论，公司游说，媒体叙事和公众对 AI 风险的想象。

这比它是"对"还是"错"更重要。

因为无论你支不支持 Dario 的方案，那个他试图回答这比它是"对"还是"错"更重要。因为无论你支不支持 Dario 的方案，他试图回答的那个问题——当技术按指数曲线移动、制度按 Treebeard 速度移动时，中间的时间差由谁来填补——是真问题。

只是谁都不应该让同一个霍比特人同时负责跑、负责喊、负责设计树人 Treebeard 的路线图。

**监管不是 AI 的刹车。它更像方向盘。而接下来最重要的竞争之一，就是谁能握住它。**

参考资料

[^1]: Dario Amodei, *Policy on the AI Exponential*, June 2026. 全文章节标题：1. Regulation and public safety, 2. Macroeconomics and tax policy, 3. Accelerating AI's positive impact, 4. The state and civil liberties, 5. Securing leadership by democracies. 下文所有 Dario 原文引用均出自此篇，不再重复标注 URL。

[^2]: Dario 原文 Section 1，原文措辞："Models above a threshold of compute should undergo mandatory testing by a qualified third party for their level of risk in four specific areas: cybersecurity, biological weapons, loss of control of AI systems, and automated R&D that could accelerate these other risks." 以下"四类风险"出处同此段。

[^3]: 原文 Section 2："Anthropic has been operating an Economic Index of how people use Claude for nearly a year and a half."

[^4]原文开场段："AI's scaling laws, which predict an exponential increase in general cognitive capabilities with increasing computing power, now have over a decade of empirical evidence behind them."

[^5]: 原文 Section 1："Perhaps the most emblematic example is Claude Mythos Preview and the discovery that frontier models pose very real risks to cybersecurity… Mythos Preview scrambled the global cybersecurity landscape. But its broader significance is that it proves beyond doubt that AI models are now tools of global and national strategic consequence."

[^6]:原文开场段："AI's scaling laws, which predict an exponential increase in general cognitive capabilities with increasing computing power, now have over a decade of empirical evidence behind them."

[^7]:原文开场段："in only four years, AI models have gone from barely being able to write a coherent line of code to writing most of the code at major AI companies."

[^8]: 截至 2026 年 6 月 11 日调研窗口，未检索到 APPSO、36 氪、量子位等主要中文 AI 媒体的同步翻译或深度解读。同期 Fable 5 等产品发布占据了中文 AI 自媒体的主要注意力（来源：`REPORT.md` §2.3）。

[^9]: 原文 Section 5："Pending legislation like MATCH and OVERWATCH is a good first step here, and allied democracies need to consider similar measures."
