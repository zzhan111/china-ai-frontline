## post-2026-06-05-001：用 MCP 调通 Coze bot，0 UI 操作真实跑通

**状态**：draft
**来源**：inbox/2026-06.md#2026-06-03（Coze MCP 端到端 demo 真实跑通，commit 816e04b）
**首发平台**：X
**audience**：AI builder + 关注 Coze / 字节生态 / MCP 协议 / 本地 agent 接入的从业者
**是否升级长文**：待观察

### 一句话观点

Coze 平台所有"创建 bot / 发布 / 调用"操作都有 MCP API，**永远不要走 bb-browser UI 自动化**——MCP 是 100 倍简单、0 token 浪费、0 React 状态问题的路径。

### 近似实现 / 需要调查

- [coze-dev/coze-mcp-server](https://github.com/coze-dev/coze-mcp-server) (⭐47 MIT) — 官方 MCP server，本次 demo 用的就是这个
- [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) (⭐18.2k) — Claude Code plugin 协议参考
- [LingyiChen-AI/workflow-skill](https://github.com/LingyiChen-AI/workflow-skill) (⭐96) — 同一思路的另一条路（金融研报自动生成）

差异化：国内 X 圈层少见有人讨论"用 MCP 调 Coze bot"这条路；多在纠结 bb-browser UI 自动化或直接 curl Coze API 自己封装。

### 真实可验证的端到端 demo（不是 setup guide）

**4 步真实跑通（所有 isError: false）**：

1. `create_bot` API 调通 → bot_id `7647398669641826350`
2. `publish_bot` API 调通 → version `1780548856169`
3. `chat_with_bot` API 调通 → 真实 LLM 回答"中医里的阴阳是概括事物对立统一属性的核心理论，指导辨证施治，统摄寒热、表里等范畴。"
4. 答案写入 `china-ai-frontline/inbox/2026-06.md`（commit 816e04b，main 推送）

**关键点**：
- `create_bot` 只需要 `workspace_id` + `name` 两个必填字段
- `chat_with_bot` 用 `content` 字段（不是 `query` / `message` / `text`）
- `list_bots` 只列**已发布到 API 渠道的 bot**（不是所有 bot）

### 反共识判断

> "AI 能力过剩"在 B 端可能是错的。

Coze 这种平台的爆火是**封装过剩**——底层很多 skill 是**纯模板 + Python 标准库**，根本不需要 LLM。但 Coze 把它打包成"AI skill"卖。

剥掉这层：**Coze 平台的大部分价值是把"行业 know-how"标准化 + UX 友好**，不是 AI 推理。

### X thread 草稿

**1/**
真实跑通 Coze MCP 端到端 demo。

不是 setup guide — 是 1 小时内 create_bot → publish_bot → chat_with_bot 全部 isError: false 的证据。

起点：coze-dev/coze-mcp-server 仓库（47⭐ MIT），uvx 一行装好。🧵

**2/**
真实证据：

① create_bot → bot_id 7647398669641826350
② publish_bot → version 1780548856169
③ chat_with_bot → 真实 LLM 回答"中医里的阴阳是..."

答案同步写进 china-ai-frontline/inbox/2026-06.md，commit 816e04b 推上 main。

**3/**
反共识：

我之前想用 bb-browser 自动化创建 bot，卡了 4+ 步（React 表单 / 22 个 dialog portal / name 字段填不进去）。

**MCP 才是正确路径**。Coze 平台所有"创建/发布/调用"操作都有 MCP API，永远不要走 UI 自动化。

**4/**
create_bot 只需要 workspace_id + name 两个字段。

```python
mcp_call("create_bot", {
    "workspace_id": "7647333402391379983",
    "name": "simple-bot-2026-06-03",
    "description": "测试 bot",
    "prompt": "你是简洁的 helpful assistant。"
})
```

—— 这是 API 路径，比 UI 简单 100 倍。

**5/**
chat_with_bot 的 schema 用什么字段？

真实验证（试了 N 次错的）：
- ✅ `content` 是用户消息字段
- ❌ `query` / `message` / `text` 都不对

Pydantic 验证错误会直接报字段名，看错误修正就行。

**6/**
跟 Coze UI 比，3 个真实优势：

🚀 **0 React state 问题** — 不依赖前端表单组件
💰 **0 token 浪费** — 只跑 1 次成功调用（UI 自动化要重试 N 次）
🔒 **token 不暴露 UI** — `user_env: ["COZE_API_TOKEN"]` 模式让 token 永不进 mcp.json

**7/**
一个踩过的坑：

list_bots 返回空 ≠ "账号 0 个 bot"。

`list_bots` 调的是 `published_bots_list` endpoint（**只列已发布到 API 渠道的 bot**）。工作台里看到的 bot 必须先 publish_bot 才会出现。

没 published = 看不到 ≠ 不存在。

**8/**
下一步：

📁 装入位置：~/AppData/Local/hermes/profiles/w-hermes/mcp.json
🔑 凭据：~/.hermes/profiles/w-hermes/.env (COZE_API_BASE, COZE_API_TOKEN)
🤖 Bot 真实存在：simple-bot-2026-06-03 (id 7647398669641826350)
📝 完整 setup 指南：~/.shared-skills/devops/coze-mcp-setup/SKILL.md

——

#AI #Agent #Coze #MCP #ClaudeCode #零token

### Humanizer

humanizer: zh@2026-06-03 (prompts/humanizer-zh.md vendored fallback by MiniMax-M3 + manual touch-up)

应用项：
- 删 em dash（"——" 改为换行或句号）
- 删 signposting（"接下来"类元评论）
- 数字加粗做视觉锚点（bot_id / version / commit hash）
- 真实证据引用（不写"我做了 X"，写"commit 816e04b 显示 X"）
- 反共识部分用引用块呈现（"AI 能力过剩是错的"）
- "AI 平台大部分价值是把 know-how 标准化" 避免"颠覆/革命"AI 痕迹词

### 发布后反馈

发布时间：
链接：
回复：
收藏：
转发：
点赞：
评论：
高质量反馈：
下一步：

