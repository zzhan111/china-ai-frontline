# inbox/ — 碎片想法捕捉层

## 作用

`inbox/` 只负责接住想法，不负责完美。

允许粗糙、重复、口语化。可以从手机、语音转写、聊天记录、随手笔记里直接贴进来。

## 文件约定

**按月份一个文件**，不要每条 idea 一个文件：

```
inbox/2026-05.md
inbox/2026-06.md
```

新月份开始时新建一个文件。

## 条目格式

每条 idea 一个二级标题，时间戳精确到分钟：

```markdown
## YYYY-MM-DD HH:MM

来源：[描述]

[原始想法，不需要完整句子]

我想让 AI 帮我做：

- [选项 1]
- [选项 2，可选]
```

`我想让 AI 帮我做：` 是可选的，常用选项：找近似产品或现有实现 / 改成 X 内容 / 改成小红书内容 / 判断是否值得升级成长文。

## 处理方式

每天由 coding agent 按 [`skills/social-content-loop.md`](../skills/social-content-loop.md) 中的工作流处理。

## AI 允许的唯一回写：eval 标注

AI 处理前可在条目末尾追加一行 eval，格式固定：

```
eval: [ready|vague|missing-task|done] | [可选备注，≤20字]
```

示例：
- `eval: ready | 建议路由 X thread`
- `eval: vague | 原始想法需补充具体场景`
- `eval: missing-task | 建议加：改成 X 内容`
- `eval: done | 已发布`

**规则**：eval 只能一行，不得扩展成段落、列表或表格。

## 不要做的事

- 不要在 inbox 里写完整内容（那是 `posts/` 的工作）
- 不要在 inbox 里做竞品研究（那是 `posts/` 的 post block 里的事）
- 不要在 inbox 里直接升级成 topics（升级标准见 [`docs/platform-strategy.md`](../docs/platform-strategy.md)）
- AI 不得在条目内追加 eval 以外的任何内容（处理结果、调研记录、"已处理"标注一律写入 `posts/`）
