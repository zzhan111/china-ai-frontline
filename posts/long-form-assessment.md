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
