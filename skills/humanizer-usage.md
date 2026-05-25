# Humanizer 使用约定

社媒草稿在发布前必须去 AI 味。本仓库不 vendor humanizer 源码，只声明使用约定。

## 选择哪个版本

- 中文草稿 → [`op7418/Humanizer-zh`](https://github.com/op7418/Humanizer-zh)
- 英文草稿 → [`blader/humanizer`](https://github.com/blader/humanizer)
- 中英混合 → 先按主语言跑一次，再人工调整另一种语言的句子

## Agent 工具兼容性

本约定不绑定具体 agent CLI。下表给出常见工具的接入与调用方式：

| Agent | 接入方式 | 调用入口 |
|---|---|---|
| Claude Code | `npx skills add https://github.com/op7418/Humanizer-zh.git`（或手动 clone 到 `~/.claude/skills/`） | slash command：`/humanizer-zh`、`/humanizer` |
| Codex CLI | 把 humanizer 的 system prompt 放到 `~/.codex/prompts/humanizer-zh.md` | slash command：`/humanizer-zh`、`/humanizer` |
| Hermes | 按 Hermes skill/agent 注册流程加载 humanizer prompt | Hermes 内部 skill 调用 |
| OpenClaw | 在 OpenClaw skill 目录中放入 humanizer prompt | OpenClaw 内部 skill 调用 |
| 其它 / fallback | 直接复制 humanizer 仓库 README 中的 system prompt | 普通对话方式提供给 LLM |

无论哪个工具，输入输出形式一致：

```
input:  posts/*.md 中 ### 平台草稿 区的原文
output: humanized 后的同长度文本
```

## 一次性安装（仅需执行一次）

参考上表对应行。Claude Code 用户可以直接：

```bash
# 中文
npx skills add https://github.com/op7418/Humanizer-zh.git

# 英文
git clone https://github.com/blader/humanizer.git ~/.claude/skills/humanizer
```

其它 agent 工具按各自的 skill / prompt 装载方式接入同一份源码即可。

## 调用流程（跨工具通用）

1. 在 agent 中触发 humanizer 能力（具体命令见上表）
2. 输入：`posts/*.md` 中 `### 平台草稿` 区的原始文本
3. 接收：humanized 后的文本
4. 用 humanized 文本覆盖原"平台草稿"区
5. 在 post block 末尾追加签名行

## 处理范围

- 只对 `posts/*.md` 中 `### 平台草稿` 区的正文运行
- 不对 `### 一句话观点`、`### 近似实现 / 待查`、`### 发布后反馈` 运行
- 不对 `inbox/`、`raw/`、`topics/`、`drafts/` 运行

## 签名格式

每次运行后在 post block 末尾追加一行：

```
humanizer: zh@<version-or-date> | en@<version-or-date> | skipped(reason: ...)
```

例：

```
humanizer: zh@2026-05-25 (op7418/Humanizer-zh)
```

如果 humanized 版本明显丢失关键信息或专有名词，回滚并手动小修，签名照写。

## 必须保留的元素

humanizer 不应改动以下内容，若被改动需手动复原：

- 具体数字与日期
- 真实人名、地名、机构名
- 链接和 URL
- 代码块和 markdown 结构
- 引号内的原话引用

## 跳过 humanizer 的合法理由

只有以下情况可以跳过，并必须在 post block 里写明：

- 内容主要是数字、链接或代码片段，没有自然语言可被改写
- 是已发布原文的截取，需保持原貌
- 平台对原始性有要求（极少见，需说明）

其它情况一律必须 humanize。
