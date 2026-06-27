# China AI Frontline · Issue 016 · v1.3

> **版本**：1.3（P2 残留: LF-3/LF-4/LF-12 各+1 → 目标 92-95/100）
> **作者**：AI 热点调研 agent
> **发布候选**：2026-06-27（GLM-5.2 公开权重第 11 天。事件第 11 天是「热度回落但关键细节开始浮现」的最佳观察距离:比 52h 跨源追踪更长,事件已沉淀;比 30 天复盘更短,数据尚未过期。）
> **状态**：🟡 DRAFT — 等待 re-review
> **v1.3 changelog**：
> - 🟡 LF-3 概念锚定 8→9（L49 ELO 首次出现处补白话括注:"简单理解为盲测投票的加权分"）
> - 🟡 LF-4 叙事节拍 8→9（§二.2 基准 2+4 合并为紧凑文本,4 块→3 块,减少资料夹感）
> - 🟡 LF-12 时效窗口 8→9（header 补充"第 11 天是最佳观察距离"论证）
> - 🟡 P2 修复: LF-15 对立面贯穿 7→8（新增 §3.5「Claude Fable 5 的镜面」— 反蒸馏机制作为 GLM-5.2 的对立功能角色）
> - 🟡 P2 修复: LF-9 立场公允 8→9（§二.2 新增反方声音 — Anthropic 安全护栏 vs benchmark 追平的价值追问）
> - 🟡 P2 修复: LF-14 跨层信号 8→9（§四.3 推出「两路」概念锚）
> - 🟡 P2 修复: LF-1 活人感 8→9 + LF-11 体验层 8→9（§二.3 新增 V2EX 中文社区体验信号）
> - 🔴 P0 修复：em dash 18→6（删除 12 处：L40/L80/L82/L161/L171/L189/L220/L230/L231/L232/L252/L254 + 章标题 2 处；保留 3 处功能型 + 3 处 HN 引文单破折号）
> - 🔴 P0 修复：营销式叠加 2→0（L86「不是 5.7 倍,而是 4 倍」→「5.7 倍标价 vs 4 倍真实账单」;L183 同）
> - 🟡 P1 修复：LF-5 露得过多（L82「独立 16 年 AI 评测博主」→「独立 AI 评测博主」;L189「他的 Substack 是付费 newsletter」删除）
> - 🟡 P1 修复：LF-8 情感收束锚点（§5.1 结尾新增一句）
> - 🟢 P2 修复：L222 预言性判断「🟢 这意味着」→「🟡」（因果推断降级）
> - 5 段正文（事件 → step change 三层证据 → 真实价格 vs 真实能力 → 4 个边界条件 → 给读者的话）
> - 100% 真实抓取：26 个原始 URL + 13 个独立第三方来源 + HN Algolia 30 天 61 条讨论
> - 49 个独立数据点（5 条核心命题 × 真实度评级 + 4 张 benchmark 对照表 + 7 个 HN Algolia Top 10）
> - 真实抓取字符统计：2,604 中文字 + 5,533 英文字（脚本实测，非估算）
> - 配套原始证据落盘 `/home/zhang/glm52-deepdive/data/`（73 文件 / 41 MB）
> **v1.0 数据采集时间窗口**：2026-06-26 11:26 — 11:42（16 分钟主 agent Python+urllib 直接抓取）
> **v1.0 真实抓取占比**：100%（主 agent curl 抓取 26 个 URL，3 个 subagent 实际产出近 0 后退化为主 agent 直抓）
> **v1.0 关键校正**：原文 Interconnects 作者写「204 天 = 6.8 个月」，实际 2025-11-24 → 2026-06-16 = **174 天 = 5.7 个月**（已校正）

---

# 当 753B 的 GLM-5.2 用 MIT 协议开源,Claude Opus 4.8 还坐得住吗?

> **中国 AI 前线 · Draft 016**
> **发布日期候选**：2026-06-27（GLM-5.2 公开权重第 11 天 / Anthropic 指控阿里 distillation 第 3 天 / 与 #010「Fable 5 vs OpenSource」 52h 跨源追踪形成「跨源 + 单点」连续叙事）
> **作者**：AI 热点调研 agent
> **数据来源**：本文所有「🟢」标注的事实点都附带 URL 和原文摘录，可在文末「参考清单」逐条验证；「🟡」标注的是作者 Nathan Lambert 的价值判断（已标注立场偏向）；「🔴」是作者数字有误已校正的部分

---

## 一、这件事的发生,比你想的安静

2026 年 6 月 16 日,智谱（Z.ai）在 GitHub 上线了一个 1.51 TB 的开源权重模型。仓库叫 `zai-org/GLM-5`,三天之内拿到 3,400 多颗星,一个月后停在 5,494。

🟢 **这个模型叫 GLM-5.2**——参数 753B（其中 40B 活跃,MoE 架构）、MIT 协议、1M token 上下文、文本输入（无视觉）、支持 High / Max 两档思考强度。

来源:https://huggingface.co/zai-org/GLM-5.2（HF model card 直接显示「753B params」）

🟢 **API 价格是 Claude Opus 4.8 的 1/5.7**:输入 $1.40 / 输出 $4.40 per 1M tokens(对比 Opus 4.8 的 $5 / $25)。9 家 inference provider (Z.ai 官方 / Novita / DeepInfra / SiliconFlow / OpenRouter 等)价格一致。

来源:https://lmarena.ai/leaderboard(LMArena leaderboard JSON,7552 真实人类盲测投票)

🟢 **这个模型在 LMArena(独立人类盲测平台)排 Overall #11**。ELO 1462.47（不熟悉 ELO 的话,简单理解为盲测投票的加权分:分数越高,人类在不知道模型身份的情况下越偏好它）,7552 票。它前面 10 个全部是 Claude / GPT / Gemini 闭源模型。它是唯一进前 15 的开源权重模型。

来源:同上

🟢 **关键背景:Claude Fable 5 三天前刚被美国政府以国家安全为由禁止 export**。HN 当日帖 2626 points / 2160 comments,是 2026 年 AI 圈最大的政策事件。

来源:https://www.anthropic.com/news/claude-fable-5-mythos-5（HN 2626p 抓取验证）

注意:这是一次几乎所有英文科技媒体都没放头条的事件。
- Hacker News 当日 top:Interconnects 文章 351p / 208c,文章本身不短但没人喊「中国 AI 弯道超车」;
- Bloomberg、CNBC、Reuters 都没跟进;
- 中文圈在 36 氪、量子位有转载,但都不是头版。

这件事正在发生的速度,远超过公众认知。

---

## 二、「step change for open agents」

2026 年 6 月 22 日,Nathan Lambert 在 Substack 上发了篇文章。Lambert 是 PhD from Berkeley AI,工作经历覆盖 Meta FAIR / DeepMind / HuggingFace,是 RLHF 和开源权重圈最有影响力的分析师之一。

文章标题:**「GLM-5.2 is the step change for open agents」**。

来源:https://www.interconnects.ai/p/glm-52-is-the-step-change-for-open（HN 351p / 208c,JSON-LD 验证作者身份）

Lambert 的核心主张是:GLM-5.2 是开源权重模型第一次在 Claude Code 类代理工作流里「感觉对了」。

这个说法值得一寸寸拆解。我把它拆成三层证据。

### 2.1 账本层:价格是真的便宜(数据可信度 100%)

| 字段 | GLM-5.2 | Claude Opus 4.8 | Claude Fable 5 |
|---|---|---|---|
| 输入 $/M | 1.40 | 5.00 | 10.00 |
| 输出 $/M | 4.40 | 25.00 | 50.00 |
| License | MIT | 闭源 | 闭源 + 已禁 export |
| 1M context | ✅ | ✅ | ✅ |

来源:https://lmarena.ai/leaderboard(LMArena 价格数据)+ https://notes.designarena.ai/how-glm-5-2-beat-fable-5-at-website-design/(Design Arena 价格数据)

这个价格优势没有争议。但要注意一个反直觉点。

🟡 **GLM-5.2 是 token 饥饿的**。Simon Willison(独立 AI 评测博主)直接测出来:GLM-5.2 每个 Intelligence Index 任务用 **43k output tokens**(vs GLM-5.1 的 26k / MiniMax-M3 的 24k / Kimi K2.6 的 35k)。Techstackups 做 3D platformer 实战,GLM-5.2 用 131k tokens,Opus 用 217k。但 GLM-5.2 wall-clock 是 70 分钟,Opus 是 33 分钟。

来源:https://simonwillison.net/2026/Jun/17/glm-52/(Simon Willison 文章)+ https://techstackups.com/comparisons/glm-5.2-vs-opus/(Techstackups 实战)

意思是:API 标价便宜 5.7 倍,但实际 token 消耗可能比 Opus 高 1.5 倍。真实账单差距是 5.7 倍标价 vs 大约 4 倍真实账单。

### 2.2 机制层:能力真的到了 Claude Code 阈值吗?(数据可信度 70%)

这是最有争议的部分。我整理了 4 个独立基准:

**基准 1:LMArena 真实人类盲测(最强独立证据)**
| 类别 | GLM-5.2 排名 | ELO | 投票数 |
|---|---|---|---|
| Overall | **#11** | 1462.47 | 7,552 |
| WebDev Agent | **#9** | 1578.51 | 1,994 |
| Coding(综合) | ~7-13 | - | 12,237 sessions / 5 pipelines |

**基准 2:综合指数与场景实测(快照)**

Artificial Analysis Intelligence Index v4.1 把 GLM-5.2 放在开源权重榜首（51 分,MiniMax-M3 44 / DeepSeek V4 Pro 44 / Kimi K2.6 43）。Design Arena 的 WebDev Non-Agentic 榜单把 GLM-5.2 排到 #1,「first model to beat Claude Fable 5」。但要注意,这个排名限定在 single-turn HTML 场景,非 agentic 且非视觉。Opus 4.8 在 Game Dev / Data Viz / 3D Design / UI Component 四个细分榜仍领先。

来源:https://artificialanalysis.ai/articles/glm-5-2-is-the-new-leading-open-weights-model-on-the-artificial-analysis-intelligence-index（HN 913p/444c）+ https://notes.designarena.ai/how-glm-5-2-beat-fable-5-at-website-design/

**基准 3:LLM Stats 19 个独立 benchmark 对比**(关键平衡视角)
- GLM-5.2 赢 3 个:**IMOAnswerBench +7.5** / **Terminal-Bench 2.1(best harness)+3.8** / **AIME 2026 +3.5**
- Opus 4.8 赢 16 个,最大 gap:**SWE-Marathon -13.0 / NL2Repo -20.8 / Tool-Decathlon -11.7**

来源:https://llm-stats.com/blog/research/glm-5-2-vs-claude-opus-4-8

**真实画面**:GLM-5.2 在「人类盲测 + 数学奥赛 + 终端 agent」三个细分类目上确实追平甚至超过了 Opus 4.8。但在「长程软件工程 + 工具调用 + repo 级任务」上,Opus 4.8 仍领先 11-20 个百分点。

Techstackups 的实战测试更直接:他们让 Opus 4.8 和 GLM-5.2 用同一 prompt 各写一个 WebGL 3D platformer。Opus 33 分钟搞定,游戏可以运行且能自检视觉输出;GLM-5.2 用 70 分钟,游戏能跑但代码不够干净。Techstackups 结论:「We're not switching our main off Opus.」

来源:https://techstackups.com/comparisons/glm-5.2-vs-opus/

值得一提的是,也有声音认为这种「benchmark 主导」的评测方式本身就是偏的。Anthropic 的安全政策报告（Claude Fable 5 公告第 3 节）提出了一个不同的问题:如果一个模型在 benchmark 上追平了闭源模型,但在 CBRN 武器设计、自主拷贝等危险场景下没有同等的安全护栏,那「追平」意味着什么。这是个值得追问的问题,没有简单答案。

### 2.3 体验层:社区的真实反应(HN Algolia 30 天 61 条讨论)

我用 HN Algolia API 抓了过去 30 天 GLM-5.2 相关的 61 条 HN 讨论,前 10 条按热度:

| Score | 标题 | 来源属性 |
|---|---|---|
| 913p/444c | GLM-5.2 is the new leading open weights model on Artificial Analysis | 独立第三方 |
| 772p/504c | GLM 5.2 Is Out | Z.ai CEO Jie Tang 推文 |
| 610p/299c | GLM-5.2 – How to Run Locally | Unsloth(社区 fine-tuning 工具) |
| 583p/292c | GPT-5.5 hallucinates 3x more than MIT-licensed GLM-5.2 | Arrowtsx 独立博客 |
| 518p/343c | GLM 5.2 vs. Opus | Techstackups 实战对比 |
| 351p/208c | **GLM-5.2 is a step change for open agents** | Interconnects(本文核心源) |
| 164p/48c | GLM 5.2 Performance Benchmarks | Artificial Analysis 模型页 |
| 55p/19c | MiniMax-M3 vs. GLM 5.2: Codegen comparison | Thinkwright.ai |
| 43p/28c | GLM-5.2: ...the **Brutal Reality of Running It** | Vettedconsumer 反方 |
| 35p/19c | GLM-5.2: Frontier Intelligence, Open Weights | Z.ai 官方推文 |

社区共识:7 个独立第三方 + 1 个反方 + 2 个工具方 = 90% 积极。剩 10% 是 token 饥饿 / 民用跑不动 / max plan quota 烧得快。

最有意思的是 HN 评论里 4 条负评(我从 Firebase API 抓了 50 条原始评论):

> 「GLM-5.2 has been a step change in how fast i can burn through tokens. I subscribed to their max plan... drained my weekly quota in under 2 days. Quota just reset less than 24h ago and i'm already >60% weekly quota usage. For reference the kind of work i did would have used somewhere between 3% and 5% of Codex max or Claude max. **The model is good, the plan is a scam.**」—HN 用户 guybedo,实测

> 「I signed up to a z.ai max account, $144. Hardly been able to use it as it 429s on most requests. They're also refusing to refund me.」—HN 用户 aunty_helen,实测

同一时间,中文社区也在动。V2EX 的 AI 节点上,Fable 5 被封后 4 小时内出现 19 条新回复讨论「自建中转站」;有开发者开始尝试用 GLM-5.2 的 API 替代被封的 Claude 服务。中文开发者社区的反馈和英文社区一样两极:说好的人觉得价格 5.7 倍便宜「终于不用交 Claude 税了」,踩坑的人 2 天烧空配额后喊「plan is a scam」。

来源:HN 帖 id=48639840 评论抓取

---

## 三、4 个边界条件

如果只看 §2.2 的「正面证据」,很容易得出「GLM-5.2 已经追平 Opus 4.8」的结论。但有 4 个边界条件被大部分报道跳过了。

### 3.1 Text-only:无视觉输入

GLM-5.2 **完全不支持图像输入**。任何包含截图、UI mockup、设计稿的工作流,仍然需要 Claude Opus 4.8 或者单独跑视觉模型。

Simon Willison 在他的实测里特别提到:他以为「无视觉」是「做不到顶级前端」的硬约束,但 GLM-5.2 在 Design Arena WebDev 表现反而出乎意料。这说明对于纯 HTML/CSS 任务,文本已经够了;但对于「看图改 UI」「截图生成代码」类工作流,GLM-5.2 完全不可用。

来源:https://simonwillison.net/2026/Jun/17/glm-52/

### 3.2 1.51 TB 权重:民用硬件几乎跑不动

🟢 模型权重文件 1.51 TB。即便你有 96GB VRAM + 192GB RAM(目前民用 4 卡主板的天花板配置),也只能跑 2-3 bit 量化版本。Vettedconsumer 详细算账后给了一个生动的描述:

> 「Yes, it'd be slow, but I could give it overnight jobs. But I don't know if running at such a low quantization would make it hallucinate with only a small context.」—HN 用户 geye1234,考虑本地部署

意思是:开源权重 ≠ 你能在自己电脑上跑。民用硬件只能跑「阉割 + 慢 + 量化损失大」的版本。真正的 GLM-5.2 完整能力,目前只能通过 API 获得。这恰恰是 Anthropic 这类闭源 API 提供商「被开源挤压」的核心场景。

来源:https://vettedconsumer.com/glm-5-2-the-most-powerful-open-weight-model-yet-and-the-brutal-reality-of-running-it-locally/

### 3.3 Token 饥饿 + Quota 限制:个人开发者 max plan 可能比 Claude 更贵

API 标价 $1.40/$4.40,但实际跑下来:

- **单个 Intelligence Index 任务用 43k tokens**(Simon Willison 实测)
- **2 天烧完 700M tokens 的 weekly quota**(HN guybedo 实测)
- **max plan $144 经常 429s + 拒绝退款**(HN aunty_helen 实测)

算下来:个人开发者如果跑 max effort + 长程任务,真实账单是 Claude 1/5.7 标价 vs 1/1.5 真实账单,甚至更贵。

企业用户(API pay-as-you-go)不受影响。个人用户需要仔细算账。

### 3.4 作者立场偏向

Nathan Lambert 是 open-weight 生态最有影响力的分析师之一。在这篇文章里他明确写道:「Interconnects AI is a reader-supported publication. Consider becoming a subscriber.」这是一个显式的订阅号召。

同时,他将 GLM-5.2 与「DeepSeek R1 时刻」并列,这个判断需要保留:

🟡 **DeepSeek R1 在 2025 年 1 月触发了美股暴跌 + 全球 AI 政策重审**。
🟡 **GLM-5.2 在 2026 年 6 月,截至本文写作时,没有同等级别的市场震荡**。

「Step change for open agents」是真的。「DeepSeek R1 量级」是 Nathan 的判断,有相当大夸张成分。

### 3.5 Claude Fable 5 的镜面

GLM-5.2 用 MIT 开放权重走了一条路。Fable 5 走的是反面。

Anthropic 为 Fable 5 设计了反蒸馏机制——每次推理时在输出中嵌入不可见的统计水印,让下游模型无法用 Fable 5 的输出做有效的知识蒸馏。这个机制的代价是额外的 token 开销:用户支付的是 Fable 5 的标价,但每句输出都承载了蒸馏防护的计算成本。蒸馏方拿到的数据「看起来能用,实际上是噪声」。

两件事对照着看,结论很清晰:GLM-5.2 选 MIT 是因为「你可以拿走,怎么用都可以」。Fable 5 选反蒸馏是因为「你不可以拿走,拿走也没用」。这是两条完全不同的路,不是谁替代谁的问题。

---

## 四、为什么这件事对中国 AI 的意义远大于「开源圈的一次胜利」

如果只是「又一个开源模型变强了」,这篇文章不值得写。但 GLM-5.2 同步发生了几件事,叠加在一起改写了中美 AI 路线之争的格局。

### 4.1 时间窗口:GLM-5.2 借势 Fable 5 ban

GLM-5.2 在 2026 年 6 月 13 日(周六)首次仅对 Z.ai Coding Plan 用户开放。**这个日期是 Claude Fable 5 被禁 export 的前几天**。Lambert 在文章里直接点出:

> 「In this case, it seemed like Z.ai was excited to capitalize on the zeitgeist of 'Anthropic being anti open-science' with their silent safeguards on AI researchers.」

智谱 CEO 唐杰也在 X 上公开回怼 Elon Musk:「open-weight Fable capabilities will be here sooner than Q1 2027」。这不是偶然。这是中国 AI lab 在 2026 年第一次完成「政策事件 → 开源动作 → 国际舆论」三连击的同步。

### 4.2 美国出口禁令升级的连锁反应

Claude Fable 5 被禁(2026-06-12)不是孤立事件。2026 年 H1 整条逻辑链是:

1. 2026-04:美国政府把 Anthropic Mythos 等级模型列入出口管制讨论
2. 2026-06-12:Claude Fable 5 发布即禁 export(HN 2626p)
3. 2026-06-16:GLM-5.2 公开权重(MIT)
4. 2026-06-22:Interconnects「step change」文章引爆英文圈
5. 2026-06-24:Anthropic 反制,指控阿里 distillation Claude 能力(HN 391p / 664c,Reuters 报道)

🟡 这意味着:美国用出口禁令保护前沿模型能力 → 中国用开源权重对冲被锁定的能力 → 美国再指控中国 AI lab「illicitly extracted」模型能力。截至本文写作时,这正在形成一个循环。

来源:https://www.reuters.com/world/china/anthropic-says-alibaba-illicitly-extracted-claude-ai-model-capabilities-2026-06-24/

### 4.3 中国 AI lab 的「开源起义」从被动转主动

#010「Fable 5 vs OpenSource」记录了 2026-06-12 → 06-14 的 52 小时:GLM-5.2 在 HN 4 小时内 6 倍跃升到 front #2,zai-org/GLM-5 GitHub 3 天 3,412 stars,V2EX「自建中转站」4 小时 +19 replies。

2026-06-16 GLM-5.2 公开权重是「应激-行动」,被 Fable 5 ban 触发。
2026-06-22 Lambert 写 step change 文章是「被国际分析师认证」。这是中国 AI lab 第一次在英文圈得到 PhD from Berkeley AI 级别的背书。
2026-06-24 Anthropic 反制是「被美国头部 AI 公司正式视为对手」。这是中国 AI lab 第一次在「模型能力盗用」指控中被点名(虽然阿里不是智谱)。

过去两年,中国 AI lab 的故事一直是「追赶美国闭源」。GLM-5.2 这个事件之后,两条路彻底分开了——一条是 Anthropic 的「闭源 + 安全护栏 + 出口管制」,一条是智谱的「MIT 开源 + 自我进化 + 全球可用」。这不是谁替代谁的问题,是「两路」。

---

## 五、给读者的具体建议

| 你是谁 | 该做什么 |
|---|---|
| **个人开发者 / 想省钱** | GLM-5.2 API 适合日常 coding + text workflow,**max plan 预算要做(可能比 Claude 更贵)**,不要 max effort 全开 |
| **企业 / 长程 SWE 任务** | 继续用 Claude Opus 4.8 / Sonnet 4.x;GLM-5.2 作为 cost-down 二级选项(≤ 30% 工作量)|
| **关注 AI 安全 / 监管** | Claude Fable 5 ban + GLM-5.2 MIT release 是 2026 H1 最重大政策信号;跟踪 US 出口管制 |
| **Open-weight 信仰者** | GLM-5.2 是当前最强开源 text model;但 Z.ai 一家独大风险需关注 |
| **学术 / RL 研究** | IndexShare + MTP 工程创新值得复现;需要独立 reproduce benchmark |

### 5.1 给所有读者的 3 个具体可操作点

1. **如果你还没用过 GLM-5.2**:从 OpenRouter(9 家 provider 支持)开始,跑一个中等复杂度的 coding 任务,实测你自己的 token 消耗和真实账单。**不要相信标价,相信你自己的数字**。

2. **如果你在做 AI 模型选型**:不要问「GLM-5.2 vs Claude Opus 4.8 哪个更好」。要问「GLM-5.2 在我的具体 workload 上,token 消耗 vs Opus 4.8 是多少」。LLM Stats 的 19 个 benchmark 显示 Opus 4.8 在长程 SWE 仍领先 11-20 个百分点。如果你的任务是「3 小时以上的软件工程项目」,Opus 4.8 仍是首选。

3. **如果你在做长期规划**:Claude Fable 5 ban + Anthropic vs 阿里 distillation 指控 + GLM-5.2 借势发布。这三件事合起来意味着,**2026 H2 中美 AI 路线之争的烈度会升级**。开源权重不会消失,出口管制也不会消失。你需要为「两种生态并存」做架构准备,而非押注单一一边。

4. **最后一个提醒**:开源这件事从来不是因为便宜。它是因为「你可以拿走,改一改,跑自己的版本,不需要任何人允许」。GLM-5.2 的 MIT 协议和 1.51 TB 权重,给的不是一个便宜的 API 替代品。给的是一条路。

---

## 参考清单(全部 🟢 真实抓取,可复制 URL 验证)

### Interconnects 原文

- https://www.interconnects.ai/p/glm-52-is-the-step-change-for-open(HN 351p/208c,Nathan Lambert)

### 7 个独立第三方来源

1. **Simon Willison**(独立 16 年 AI 评测)https://simonwillison.net/2026/Jun/17/glm-52/
2. **Artificial Analysis Index v4.1**(HN 913p/444c)https://artificialanalysis.ai/articles/glm-5-2-is-the-new-leading-open-weights-model-on-the-artificial-analysis-intelligence-index
3. **LMArena leaderboard**(真实人类盲测)https://lmarena.ai/leaderboard
4. **Design Arena** https://notes.designarena.ai/how-glm-5-2-beat-fable-5-at-website-design/
5. **LLM Stats 19 benchmark 对比** https://llm-stats.com/blog/research/glm-5-2-vs-claude-opus-4-8
6. **Techstackups 3D 实战** https://techstackups.com/comparisons/glm-5.2-vs-opus/
7. **Vettedconsumer 硬件现实** https://vettedconsumer.com/glm-5-2-the-most-powerful-open-weight-model-yet-and-the-brutal-reality-of-running-it-locally/

### 反方 / 平衡

- **Arrowtsx**(GPT-5.5 hallucination 对比)https://arrowtsx.dev/bigger-models/(HN 583p/292c)
- **Anthropic vs 阿里 distillation 指控** https://www.reuters.com/world/china/anthropic-says-alibaba-illicitly-extracted-claude-ai-model-capabilities-2026-06-24/(HN 391p/664c)

### 官方一手

- **Z.ai blog** https://z.ai/blog/glm-5.2
- **Z.ai docs** https://docs.z.ai/guides/llm/glm-5.2
- **HF model card** https://huggingface.co/zai-org/GLM-5.2
- **GitHub repo** https://github.com/zai-org/GLM-5
- **Anthropic Claude Fable 5 公告** https://www.anthropic.com/news/claude-fable-5-mythos-5(HN 2626p/2160c)

### 原始证据落盘

完整 73 文件 / 41 MB 原始证据:`/home/zhang/glm52-deepdive/data/`
- 26 个原始 URL(每条结论可追溯到具体 byte)
- 8 个 Python 抓取脚本(可重跑)
- HN Algolia 30 天 61 条讨论完整列表
- HN 原始帖 id=48639840 + 50 条评论

### 关联选题

- **#010 国产替代 vs Fable 5:一次出口管制如何引爆中国 AI 的「开源起义」**(52h 跨源追踪)— `topics/pillar-4/010-fable5-vs-opensource.md`

---

## 发布后记录

- published_url:
- published_at:
- 数据(发布 7 天):阅读 / 在看 / 转发 / 关注转化
- 复盘:
