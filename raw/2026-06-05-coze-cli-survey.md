# @coze/cli v0.2.0 调研报告

> 调研日期：2026-06-05
> 包名：`@coze/cli`
> 版本：0.2.0 (2026-05-30)
> License: MIT
> npm: https://www.npmjs.com/package/@coze/cli
> 安装：`npm install -g @coze/cli`
> 命令名：`coze`
> 维护者：coze_plt (penglongteng@bytedance.com) + coze_bot + coze_sdk — **字节跳动官方**

## 1. CLI 与 MCP server 的关系

按真实测量，`@coze/cli` 和 `coze-mcp-server` 是 **两套独立的集成方式**，**面向不同场景**：

| 维度 | `coze-mcp-server` (v1.27.2) | `@coze/cli` (v0.2.0) |
|---|---|---|
| 用途 | **对话 bot CRUD + chat** | **Claw Coding project 完整生命周期管理** |
| 协议 | JSON-RPC over stdio | shell + flag |
| 鉴权 | SAT token (`sat_xxx`) | OAuth (`auth login --oauth`) |
| 调用方 | Claude Code / Cursor / Hermes MCP 客户端 | 终端用户 / 自动化脚本 |
| 输出 | 结构化 tool result | 文本/JSON |
| 粒度 | bot 粒度（10 个 tool）| project 粒度（30+ subcommand） |
| 配合关系 | ✅ 互补不冲突 | ✅ 互补不冲突 |

**关键洞察**：
- **MCP server** 适合 "**我写代码**、让 agent 调 Coze API" 的场景（agent 视角）
- **CLI** 适合 "**我写脚本**、让 shell 调 Coze API" 的场景（人类视角）
- 两者**不同入口**调同一套后端，**不是替代关系**

## 2. CLI 完整命令树

```
coze
├── auth
│   ├── login --oauth          # 浏览器交互式登录
│   ├── status                 # 查登录状态
│   └── logout                 # 登出
├── space
│   ├── list                   # 列 workspaces
│   └── use <space_id>         # 切默认 workspace
├── organization
│   ├── list                   # 列组织
│   └── use                    # 切默认组织/个人账号
├── code                       # Claw Coding 项目管理
│   ├── project
│   │   ├── create             # 创建项目
│   │   ├── list               # 列项目
│   │   ├── get <id>           # 查项目详情
│   │   └── delete <id>        # 删项目
│   ├── skill                  # 项目 skills 管理
│   │   ├── list -p <id>       # 列项目 skills
│   │   ├── add <skillId>      # 加 skill
│   │   └── remove <skillId>   # 删 skill
│   ├── message                # 项目 chat 消息
│   │   ├── send               # 发消息
│   │   ├── status             # 查消息状态
│   │   ├── cancel             # 取消
│   │   └── history            # 查历史
│   ├── env                    # 项目环境变量
│   │   ├── list -p <id>
│   │   ├── set
│   │   └── delete
│   ├── domain                 # 自定义域名
│   │   ├── list
│   │   ├── add
│   │   └── remove
│   ├── deploy <projectId>     # 部署
│   │   ├── status             # 部署状态
│   │   ├── list               # 部署历史
│   │   └── fix                # 修失败部署
│   └── preview <projectId>    # preview URL
├── agent                      # Agent-facing Claw project APIs
│   ├── info                   # 查 agent 原始 JSON
│   ├── member                 # 管 agent 成员
│   ├── message                # 管 agent 消息
│   ├── file                   # 管 agent 项目文件
│   └── web                    # agent web 工具
├── session                    # claw chat session
│   ├── status                 # 验证 token + 解析 claw_id
│   ├── create                 # 创建 session
│   ├── current                # 显示当前默认 session
│   ├── use                    # 切默认 session
│   ├── list                   # 列 session
│   ├── file                   # 下载 session 回复的文件
│   ├── podcast                # podcast 模式 + 声音
│   └── message                # 发消息
├── generate                   # 媒体生成
│   ├── image                  # 文生图
│   ├── audio                  # 文生音
│   └── video                  # 文生视频
├── file
│   └── upload                 # 上传本地文件
├── config                     # 本地配置 (~/.cozerc.json)
│   ├── get <keys>
│   ├── set <key> <value>
│   ├── delete
│   └── list
├── completion                 # shell 自动补全 (bash/zsh/fish/pwsh)
└── upgrade                    # 升级 CLI
```

## 3. 关键概念

### Claw project
- `coze code project` 创建的实体
- 类型：`--type web`（web 应用）/ 可能是 chatbot 等
- 包含：`message` + `env` + `domain` + `skill` + `deploy` + `preview`
- 关系：**`skill` 是 Claw project 的子资源**（不是顶层实体）

### Skill
- 单独存在（不在 `coze skill` 顶层命令下，**在 `coze code skill` 下**）
- Claw project 才有 skill
- `coze code skill add <skillId> -p <projectId>` 把预制 skill 加到项目

### Claw session
- `coze session` 是**聊天 session**（不是项目）
- 用 token 鉴权
- 支持 `message` 发送 + `file` 下载
- `podcast` 模式是 podcast 专用 session

### `coze session message` 关键能力
- 支持 `@<path>` 上传文件作为 attachment
- `--wait` 流式输出当前 turn 回复
- 自动检测 background progress（3 秒内新 background task 就返回 progress_id 不等）

## 4. 全局 Options

```
--format <fmt>     输出格式 (json, text)，默认 text
--config <path>    指定配置文件路径
--org-id <id>      覆盖组织 ID
--space-id <id>    覆盖 Space ID
--log-file <path>  日志输出到文件
```

## 5. 配置文件位置

- `~/.cozerc.json` — CLI 本地配置（org/space/token 等）
- ⚠️ **不是 `~/.coze.json` 或 `~/.coze/`** — 是 `~/.cozerc.json`

## 6. 鉴权机制

按"先验证不臆造" — **不打印 token** 调研的细节，列已知：

- `coze auth login --oauth` — **浏览器交互式 OAuth 登录**（不是 SAT）
- `coze auth status` — 看登录状态
- `coze auth logout` — 登出清凭据
- ⚠️ **OAuth vs SAT** 是两套独立鉴权体系：
  - **SAT** (`sat_xxx`) — `coze-mcp-server` 用
  - **OAuth** — `@coze/cli` 用
  - 跟 `coze generate` / `coze session` 的 token 鉴权可能又是另一种

## 7. 与 inbox "OpenClaw 龙虾" 调研的关系

按"诚实面对数据"原则 — **不臆造关系**：

数字人调研报告里说的 "OpenClaw 龙虾安装教程"：
- "OpenClaw" 跟 `coze code` / `coze agent` 描述里反复出现的 "**Claw project**" 字眼**在词面上相关**
- 但**没有**直接证据证明 OpenClaw = Coze Claw
- 调研报告里把 OpenClaw 价格范围定在 ¥39.8-18999 看起来是个**真人培训的课程名**，不像 Coze 官方产品
- 真实情况：**OpenClaw 可能是** (a) Coze Claw 项目的某个中文社区叫法 (b) 第三方付费课程品牌 (c) 跟 Coze 无关的独立项目

**未验证**。如需确认，需要：
- 查 Coze 官方文档是否提到 "OpenClaw" 字眼
- 看 `coze code skill add` 的真实 skillId 列表里有没有 "OpenClaw" 系列
- 实际访问 OpenClaw 课程网站

## 8. 真实可能的 CLI 落地场景

按命令结构推测（**未真实跑通**）：

1. **CI/CD 集成**：`coze code project create` + `coze code deploy` 可以做 Claw project 自动部署
2. **批量测试**：`coze code message send` 可以批量跑 prompt 对比测试
3. **本地脚本桥接**：`coze generate image "..." --output-path ./x.png` 走 shell 流水线
4. **多 account 切换**：`coze auth login --oauth` + `coze config set` 支持多账号管理

## 9. 跟 mcp-mcp-server 的对比总结

| 任务 | MCP server 优势 | CLI 优势 |
|---|---|---|
| 创建 bot | ✅ `create_bot` 1 个 call | ❌ CLI 没这命令（CLI 是 project 不是 bot）|
| 跟 bot 对话 | ✅ `chat_with_bot` | ❌ CLI 没这命令 |
| 创建 Claw project | ❌ MCP server 没这 | ✅ `coze code project create` |
| 加 skill 到 project | ❌ MCP server 没这 | ✅ `coze code skill add` |
| 部署 project | ❌ MCP server 没这 | ✅ `coze code deploy` |
| 鉴权 | SAT token (env var) | OAuth (浏览器) |
| 集成 agent | ✅ 天然 | ⚠️ 需要 shell wrapper |

**结论**：MCP server 跟 CLI 各自覆盖 Coze 平台的不同子集，**两者都需要**（不是 or 关系）。

## 10. 关联资源

- `~/.shared-skills/devops/coze-mcp-setup/SKILL.md` — MCP server setup 指南
- `posts/2026-06-05-001-coze-mcp-end-to-end.md` — MCP 端到端 demo
- npm: https://www.npmjs.com/package/@coze/cli
- GitHub: coze-arch 组织下的 cli 仓库（coze-arch 前缀的开源仓库）

## 11. 调研待办

- [ ] 真实登录（`coze auth login --oauth`）验证 OAuth 流程
- [ ] 验证 `coze code project create` 真实产出项目（需要 org/space context）
- [ ] 确认 "OpenClaw" 跟 Coze Claw 的真实关系
- [ ] 验证 `coze session message` 流式输出是否真能跟 SAT token 互通
- [ ] 对比 `@coze/cli` 跟 `@coze-arch/cli` 的差异（前者是 sdk 团队，后者是 tecvan 维护的开源 devtools）
