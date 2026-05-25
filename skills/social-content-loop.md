# Social Content Loop Skill

## 目标

把 `inbox/` 中的碎片想法推进成可发布的社媒草稿，并在发布后帮助记录反馈。

## 输入

- `inbox/YYYY-MM.md`
- 当前 repo 的 `README.md`、`topics/`、`drafts/` 摘要（用于判断与现有内容主线的关联）
- 用户指定的平台：X / 小红书 / 朋友圈

## 输出

- 更新 `posts/x.md`
- 更新 `posts/xiaohongshu.md`
- 更新 `posts/moments.md`
- 必要时建议升级到 `topics/`

## 工作步骤

1. 从 inbox 中选择最多 3 条最值得处理的想法
2. 每条提炼一句话观点
3. 为每条寻找近似产品、近似实现或相似内容方向
4. 生成平台草稿（写入对应 `posts/*.md` 的"平台草稿"区）
5. **去 AI 味**（详见 [`skills/humanizer-usage.md`](humanizer-usage.md)）
   - 中文草稿 → 调用 `humanizer-zh` 能力
   - 英文草稿 → 调用 `humanizer` 能力
   - 调用入口因 agent 而异（Claude Code、Codex、Hermes、OpenClaw 等），统一约定见 humanizer-usage.md
   - 用 humanized 版本覆盖"平台草稿"区
   - 在 post block 末尾追加 `humanizer: zh@<version> | en@<version> | skipped(reason: ...)`
6. 用 [`ops/social-post-checklist.md`](../ops/social-post-checklist.md) 做发布前检查
7. 标记是否建议发布
8. 发布后根据用户提供的数据补反馈
9. 判断是否升级成长文 topic（标准见 [`docs/platform-strategy.md`](../docs/platform-strategy.md)）

## 限制

- 不创建新目录
- 不修改 `raw/`
- 不修改 `GOVERNANCE.md`
- 不直接改公众号长文（`drafts/`）
- 不为单条想法创建 PR
- 每次最多处理 3 条想法
- 不得对 `inbox/`、`raw/`、`topics/`、`drafts/` 中的内容运行 humanizer
- humanizer 只作用于 `posts/*.md` 的"平台草稿"区，不作用于"一句话观点"、"近似实现"、"发布后反馈"等结构化字段

## 日常 prompt 模板

```
请读取 inbox/YYYY-MM.md 中今天新增的想法。

只选最多 3 条。

对每条做：
1. 提炼一句话观点
2. 找近似产品、近似实现或相似内容方向
3. 生成 X 草稿
4. 生成朋友圈草稿
5. 判断是否值得发
6. 如果值得，写入 posts/x.md 或 posts/moments.md

不要创建新目录。
不要修改 raw。
不要升级成长文 topic，除非我明确要求。
```

## 周复盘 prompt 模板

```
请复盘本周 posts 文件。

输出：
1. 哪些内容已发布
2. 哪些内容反馈最好
3. 哪些内容应该归档
4. 哪些内容值得升级为 topics 选题
5. 如果升级，只生成 1-2 个 topic card，不要超过 2 个
6. 生成本周 PR 描述
```

## PR 节奏

- `inbox/` 追加：每日轻量 PR（或留到周批量）
- `posts/` 新草稿、反馈回填：每周一次批量 PR
- 结构性变更（README、GOVERNANCE、docs、目录规则）：单独 PR

不为单条想法或单次草稿单独开 PR。
