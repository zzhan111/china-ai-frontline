# X drafts

## post-2026-05-24-001：缺乏的不是想象力，而是执行力

状态：draft
来源：inbox/2026-05.md#2026-05-24-21-25
首发平台：X
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
我把自媒体运营当 GitHub repo 来做，已经三个月了。

每次发文、每次迭代，都走 branch → PR → merge。

上周合并了 PR #14 和 #15，想公开一下这套系统长什么样。🧵

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

GOVERNANCE.md 锁死这些规则——对 AI 和未来协作者都生效。

**5/**
这套系统的闭环：

输出 → 找竞品 → 发竞品 → 获反馈 → 重新输出

AI 帮我执行每一步。

现在这条 thread 本身，也是 inbox 里的一个想法，经 AI 整理后变成了 posts/x.md 里的一个 draft。

**6/**
类似系统在技术圈有先例：
- Obsidian second brain（本地 vault + git）
- GitHub Agentic Workflows（GitHub 官方也在走 Markdown-driven automation）
- Write-once publishing pipeline（git 作为出版单一真相）

但没见过有人把这套完整地用在中文自媒体运营上，还公开记录。

**7/**
如果你也在用类似系统运营内容，欢迎 reply。

如果你对这套结构感兴趣，后续会出一篇长文，把整个架构和踩坑经验写完整。

→ 关注 @[账号] 等更新

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
是否升级长文：**建议升级（见 posts/long-form-assessment.md）**

### X thread 草稿

**1/**
一个不寻常的内容生产结构：我用 GitHub repo + AI agents 运营自媒体。

不是口号，是真实系统。PR 有记录，GOVERNANCE.md 有规则，AI 是常驻 collaborator。

说一下这条支线为什么值得公开。🧵

**2/**
真实结构长这样：

- `inbox/` 承接睡前/走路时的碎片想法
- `posts/` 按平台（X/小红书/朋友圈）拆草稿
- `topics/` 是选题卡，记录策划到发布全程
- `GOVERNANCE.md` 锁死 AI 的行为边界

每一条内容，都能溯源到某个 commit。

**3/**
为什么公开这件事？

1. 真正的差异化：X 上几乎没有同类
2. 不消耗长文素材（#001~#003 的文章）
3. 可以自我繁殖——每次 PR 和反馈都是下一条内容
4. 天然吸引 AI builder、独立创作者、coding agent 用户

**4/**
PR #14 和 #15 刚合并。

这两个 PR 的内容是什么？在 repo 里有完整记录。

这条 thread 本身，也来自 inbox 里的一条想法——经 AI 整理，进了 posts/x.md，变成了可发布内容。

**5/**
闭环是：

输出 → 竞品调研 → 发布 → 获反馈 → 重新输出

AI 执行每一步。我负责想法和判断。

**6/**
如果你在做类似实验，或者对这套结构有任何问题，欢迎 reply。

后续会出完整长文：《我把自媒体当 GitHub repo 来运营》

### 发布后反馈

发布时间：
链接：
回复：
收藏：
转发：
高质量反馈：
下一步：
