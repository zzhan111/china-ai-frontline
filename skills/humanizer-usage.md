# Humanizer 使用约定

社媒草稿在发布前必须去 AI 味。本仓库**不修改 humanizer 源码**，但提供 install 脚本和 vendored fallback prompts，让 humanize 步在任何机器/任何 agent 上都可闭环。

## 选择哪个版本

- 中文草稿 → [`op7418/Humanizer-zh`](https://github.com/op7418/Humanizer-zh)（MIT）
- 英文草稿 → [`blader/humanizer`](https://github.com/blader/humanizer)（MIT）
- 中英混合 → 先按主语言跑一次，再人工调整另一种语言的句子

## 首次使用（一次性，幂等）

```bash
python tools/install-humanizer.py
```

把上游两份 SKILL.md clone 到 `external/{humanizer-zh,humanizer}/`。详见 [`tools/README.md`](../tools/README.md)。

`external/` 整个 gitignored，不污染仓库历史，不污染家目录。

## Agent 在 step 7 调用前必须自检

```bash
python tools/install-humanizer.py --check
```

如果报 `[MISS]` → 先跑 install；report 全部 `[OK]` 后才进 humanize step。SKILL workflow 已经把这一步串好（见 [`posts-author.md`](posts-author.md) step 7 和 [`social-content-loop.md`](social-content-loop.md) step 6）。

## 离线 / 未识别 agent 时的兜底

仓库 `prompts/` 目录 vendor 了两份上游 SKILL.md（commit pinned，license 见 [`prompts/LICENSES.md`](../prompts/LICENSES.md)），作为**无网络 / agent 不识别 SKILL.md 时**的 fallback：

```
prompts/humanizer-zh.md   # = external/humanizer-zh/SKILL.md (vendored snapshot)
prompts/humanizer.md      # = external/humanizer/SKILL.md (vendored snapshot)
```

任何 LLM 都能直接读这两个 prompt 完成 humanize；**不依赖任何 install**。`prompts/` 永远存在（commit 到 main），install 脚本只决定 `external/` 那条快路径是否可用。

Vendored 副本通过 `python tools/install-humanizer.py --refresh-prompts` 同步上游。

## Agent 调用入口（按工具）

| Agent | 优先入口（需 install） | 永远可用的 fallback |
|---|---|---|
| Claude Code | `external/humanizer-zh/SKILL.md` symlink 到 `~/.claude/skills/humanizer-zh/`（或 `npx skills add` 上游 URL），slash command `/humanizer-zh` | 在对话里贴 `prompts/humanizer-zh.md` 全文 |
| Codex CLI | 把 `external/humanizer-zh/SKILL.md` 复制到 `~/.codex/prompts/humanizer-zh.md`，slash command `/humanizer-zh` | 在对话里贴 `prompts/humanizer-zh.md` 全文 |
| Hermes | 按 Hermes skill 注册流程指向 `external/humanizer-zh/` | 在对话里贴 `prompts/humanizer-zh.md` 全文 |
| OpenClaw | 在 OpenClaw skill 目录中 symlink 到 `external/humanizer-zh/` | 在对话里贴 `prompts/humanizer-zh.md` 全文 |
| 其它 / 通用 LLM | — | 在对话里贴 `prompts/humanizer-zh.md` 全文 |

无论哪个 agent，输入输出形式一致：

```
input:  posts/*.md 中 ### 平台草稿 / X thread 草稿 区的原文
output: humanized 后的同长度文本
```

## 调用流程（跨工具通用）

1. `python tools/install-humanizer.py --check` 自检
2. 触发 humanizer 能力（按上表对应行）
3. 输入：`posts/*.md` 中草稿区原始文本
4. 接收：humanized 后的文本
5. 用 humanized 文本覆盖原草稿区
6. 在 post block 末尾追加签名行（见下）

## 处理范围

- 只对 `posts/*.md` 中 `### 平台草稿` / `### X thread 草稿` 区的正文运行
- 不对 `### 一句话观点`、`### 近似实现 / 待查`、`### 发布后反馈`、`### posts-eval` 运行
- 不对 `inbox/`、`raw/`、`topics/`、`drafts/` 运行

## 签名格式

每次运行后在 post block 末尾追加一行：

```
humanizer: zh@<version-or-date> | en@<version-or-date> | skipped(reason: ...)
```

例：

```
humanizer: zh@2026-05-25 (op7418/Humanizer-zh @ 91f3d39)
```

或 fallback path 用过 vendored prompt：

```
humanizer: zh@2026-05-25 (prompts/humanizer-zh.md vendored fallback)
```

如果 humanized 版本明显丢失关键信息或专有名词，回滚并手动小修，签名照写但注明 `+ manual touch-up`。

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
