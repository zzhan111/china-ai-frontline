# 长文升级评估

## 候选：《我把自媒体当 GitHub repo 来运营》

**评估日期**：2026-05-25
**来源**：inbox/2026-05.md#2026-05-24-22-24
**状态**：建议升级 ✅

---

### 竞品调研摘要

| 方向 | 代表项目/文章 | 与本方案的差异 |
|------|--------------|----------------|
| AI second brain | [obsidian-second-brain](https://github.com/eugeniughelbur/obsidian-second-brain), [COG-second-brain](https://github.com/huytieu/COG-second-brain) | 以 Obsidian vault 为中心，侧重个人知识管理，无内容运营 + PR 治理层 |
| Git-driven publishing | [Write-Once Publishing Pipeline](https://dev.to/12ww1160/building-a-write-once-publishing-pipeline-f60) | Markdown in Git 发布多平台，但无 AI agent 协作和治理规则 |
| GitHub 官方方向 | [GitHub Agentic Workflows](https://github.blog/ai-and-ml/automate-repository-tasks-with-github-agentic-workflows/) | 用 Markdown 定义 AI workflow，走 "Continuous AI" 方向，与本方案思路高度共鸣，但面向开发者，非内容创作者 |
| 创作者 OS | Notion/Obsidian 模板生态 | 无版本控制，无 AI agent 协作边界，无 PR 审批流 |

**结论**：没有现有方案同时覆盖「中文自媒体运营 + GitHub repo 治理 + AI agent 协作规则」三个维度，稀缺性成立。

---

### 升级理由

1. **话题本身具有示范性**：把真实 PR（#14、#15）、真实 GOVERNANCE.md、真实 express lane 拿出来讲，是可验证的方法论，不是空泛建议。
2. **受众扩圈潜力大**：AI builder、独立创作者、coding agent 用户——这三类受众目前不是 #001~#003 的主要读者，升级长文可以作为账号第二条支线，不消耗现有选题资源。
3. **自我繁殖属性**：这篇长文本身就是这套系统的产物，发出去后收到的每条反馈都可以成为下一次 PR。
4. **X 上无同类**：竞品搜索未见以中文写作、面向海外华人受众、公开记录整套系统的同类内容。

---

### 候选标题（3 个）

1. **《我把自媒体当 GitHub repo 来运营》**（直白，工程师受众强共鸣）
2. **《当内容创作遇上 PR review：一个工程师的自媒体操作系统》**（强调方法论，适合长文展开）
3. **《Conversation as Code：用 AI agent 运营中文自媒体的三个月实验》**（英文关键词，吸引 AI builder 圈层）

---

### 建议文章结构

```
一、引子：缺的不是想法，而是执行力
二、系统全貌：repo 目录结构 + 各层职责
三、核心机制：为什么是 PR，不是直接改文件
    - GOVERNANCE.md 的作用
    - express lane 的设计逻辑
    - raw/ append-only 的意义
四、AI 的角色：collaborator 而非 owner
    - Claude 能做什么 / 不能做什么
    - 真实案例：PR #14、#15 的诞生过程
五、竞品对比：为什么不是 Obsidian / Notion
六、三个月复盘：闭环是否真的转起来了
七、开放问题：这套系统的边界和下一步
```

---

### 下一步行动

- [ ] 发布 X thread（posts/x.md #post-2026-05-24-002）并观察反馈
- [ ] 发布小红书笔记（posts/xiaohongshu.md）并观察反馈
- [ ] 若反馈正向，开 drafts/004/ 开始长文写作
- [ ] 长文候选标题最终确认后更新此文件

---

## 候选：《API 不平等：当中国互联网不给 AI 开门》

**评估日期**：2026-05-26
**来源**：inbox/2026-05.md#2026-05-26-16-30 + 微信群聊「AI 出海工具链」
**状态**：建议升级 ✅

---

### 竞品调研摘要

| 方向 | 代表内容 | 与本方案的差异 |
|------|----------|----------------|
| AI 写电商文案 | 大量公众号/小红书教程 | 只解决「生成」，不解决「推送」— 文案写好了还是手动粘贴 |
| 亚马逊 SP-API 教程 | 官方文档、开发者博客 | 仅限亚马逊，申请门槛高，中国平台无对应物 |
| RPA/浏览器自动化 | UiPath、影刀、Selenium 教程 | 图形界面操作，脆弱、慢、token 消耗大，反爬升级即失效 |
| browse.sh 原站 | https://browse.sh | 400+ 站点 API 端点集合，但绑定云端浏览器，无法本地 agent 调用 |

**结论**：跨境电商圈内容集中在「AI 生成文案」和「官方 API 教程」两条线，没有人讲「不申请 API，让 agent 通过浏览器自己长出 API」。蓝海。

---

### 升级理由

1. **受众完全不重叠**：现有内容面向 AI builder，这篇面向跨境电商实操者（亚马逊卖家、TikTok 店主、1688 选品人）。这是第二条增长线，不消耗现有选题资源。
2. **有 external social proof**：群聊中已有亚马逊卖家把 listing 生成跑稳两个品类，就差接 API 推上去。他看见方案的反应是「我去研究起来」。不是假设需求，是 already-in-motion。
3. **概念有穿透力**：「API 不平等」四字比「repo 运营」更直觉。大模型越强越刺眼——agent 能力强了但没入口。能出圈。
4. **产品化路径清晰**：repo 运营是个人方法论，模仿成本高。API 不平等 → bb-browser 适配器 → 读者 clone 后她的 agent 立刻能调京东 API。不是「看我怎么做」，是「你也能做」。
5. **竞品真空**：跨境电商+AI agent+中国平台 API 这个交叉点，目前没有人用中文系统性地写。

---

### 候选标题（3 个）

1. **《API 不平等：中国平台不对 AI 开放接口，然后呢？》**（概念驱动，适合出圈）
2. **《我让 AI 自己「长」出了京东和小红书的 API》**（技术好奇感，吸引 AI builder）
3. **《跨境电商的 AI 最后一公里：没有 API 怎么把内容推上去？》**（直击痛点，吸引跨境电商从业者）

---

### 建议文章结构

```
一、引子：一段群聊 —「阿里的 API 不可能随便开放」
二、API 不平等的真相：硅谷开放 vs 中国封闭
三、两个死胡同：等官方 API（等不到）vs 浏览器自动化（反爬）
四、第三条路：0 token CDP 提取 — browse.sh 翻译 → bb-browser 适配器
五、现场演示：12306 查票 / 京东搜索 / 小红书热门（均 0 token）
六、电商全链路愿景：AI 写文案 → AI 推 listing → AI 改价
七、开放问题：这东西能走多远？平台会封吗？
```

---

### 下一步行动

- [ ] 群聊反馈持续观察（已有 3 人表示要研究，1 人索要 PR 链接）
- [ ] 写 X thread 试水（从群聊截图开始，讲 API 不平等的概念）
- [ ] 若 X 反馈正向，开 drafts/005/ 开始长文写作
