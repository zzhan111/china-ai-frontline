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

来源：走路 / 睡前 / 做家务 / 聊天 / 阅读 / 反思

原始想法：

<在这里粗略写，不需要完整句子>

我想让 AI 帮我做：

- 找近似产品或现有实现
- 改成 X 内容
- 改成小红书内容
- 判断是否值得升级成长文
```

## 处理方式

每天由 coding agent 按 [`skills/social-content-loop.md`](../skills/social-content-loop.md) 中的工作流处理。

## 不要做的事

- 不要在 inbox 里写完整内容（那是 `posts/` 的工作）
- 不要在 inbox 里做竞品研究（那是 `posts/` 的 post block 里的事）
- 不要在 inbox 里直接升级成 topics（升级标准见 [`docs/platform-strategy.md`](../docs/platform-strategy.md)）
