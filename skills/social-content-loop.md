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

> **跨文件 step 编号说明**：本 loop 是 inbox → 发布的整体节奏（10 步）；每条 draft 的内部 authoring 详细流程在 [`skills/posts-author.md`](posts-author.md) 里（8 步 authoring workflow）。每个 step 末尾标了 → posts-author.md 的对应 step 引用。

1. 对 inbox 每条未处理条目跑 eval（见下方 eval 规则），在条目末尾追加一行 `eval:` 标注；`vague` 或 `missing-task` 的条目跳过，等用户补充后再处理
2. 从通过 eval（`ready`）的条目中选择最多 3 条最值得处理的想法
3. 每条提炼一句话观点
4. 为每条寻找近似产品、近似实现或相似内容方向
5. 生成平台草稿（写入对应 `posts/*.md` 的"平台草稿"区）
   → 详细做法见 [`skills/posts-author.md`](posts-author.md) **step 1-4 + 6**（read contract → identify route → draft → self-review → write to file）
6. **跑 posts-eval 静态检查**（详见 [`tools/README.md`](../tools/README.md)）
   - `python tools/posts-eval.py <draft 文件路径>`
   - 任何 FAIL → 按类型分别回跳（详见 posts-author.md step 5）：
     • `hard-reject:audience-mismatch` / `hard-reject:ad-law` → 回 step 2-4（路由/audience 决策错了，不是稿子问题）
     • `len:*` / `fmt:*` / `hook:*` / `ai-flag:hard-reject` → 回 step 5 改稿
     • 任何 FAIL **不允许** soften 绕过（rename audience / 把极限词改"次极限" / "压一压" AI 词汇等）
   - 每个 WARN → 修复（首选）或在 post block 加 `acknowledged: <reason>`
   → 对应 posts-author.md **step 5**
7. **去 AI 味**（详见 [`skills/humanizer-usage.md`](humanizer-usage.md)）
   - **Pre-check**：`python tools/install-humanizer.py --check`；任何 `[MISS]` → 先 `python tools/install-humanizer.py` 装上；离线则走 `prompts/humanizer-{zh,}.md` fallback
   - 中文草稿 → 调用 `humanizer-zh` 能力
   - 英文草稿 → 调用 `humanizer` 能力
   - 调用入口因 agent 而异（Claude Code、Codex、Hermes、OpenClaw 等），统一约定见 humanizer-usage.md
   - 用 humanized 版本覆盖"平台草稿"区
   - 在 post block 末尾追加 `humanizer: zh@<version> | en@<version> | skipped(reason: ...)`
   - **顺序约束**：humanizer 必须在 posts-eval 之后跑——humanizer 重写自然语言会破坏链接/数字/专有名词，eval 抓不到原 draft 的真实问题
   - **VERIFY**：humanize 若改了单推字数 / 列表结构 / 换行，**必须重跑 step 6 的 posts-eval**（防止 humanize 让 x-cn 单推超 140 字、小红书低于 500 字等）
   → 对应 posts-author.md **step 7**
8. 用 [`ops/social-post-checklist.md`](../ops/social-post-checklist.md) 做发布前检查
   → 对应 posts-author.md **step 8**
9. 标记是否建议发布
10. 发布后根据用户提供的数据补反馈
11. 判断是否升级成长文 topic（标准见 [`docs/platform-strategy.md`](../docs/platform-strategy.md)）

## 限制

- 不创建新目录
- 不修改 `raw/`
- 不修改 `GOVERNANCE.md`
- 不直接改公众号长文（`drafts/`）
- 不为单条想法创建 PR
- 每次最多处理 3 条想法
- `inbox/` 已有条目内只允许追加一行 `eval:` 标注（格式见 inbox/README.md）；其余内容（处理记录、调研结果、"已处理"标注）全部写入 `posts/`
- 不得对 `inbox/`、`raw/`、`topics/`、`drafts/` 中的内容运行 humanizer
- humanizer 只作用于 `posts/*.md` 的"平台草稿"区，不作用于"一句话观点"、"近似实现"、"发布后反馈"等结构化字段

## inbox eval 规则

评估每条未处理条目的 `原始想法 + 我想让 AI 帮我做` 组合，判断是否可处理：

| status | 触发条件 |
|--------|---------|
| `ready` | 想法足够具体，AI 任务明确或可从想法推断 |
| `vague` | 想法过于模糊，AI 无法判断内容方向 |
| `missing-task` | 想法清晰但没有 `我想让 AI 帮我做` 且方向不明 |
| `done` | 已处理并发布，跳过不再处理 |

格式（追加到条目末尾，严格一行）：

```
eval: ready | X thread 方向清晰
eval: vague | 需补充：具体是哪类 skill？
eval: missing-task | 建议加：改成 X 内容 / 判断是否升级成长文
```

已有 `eval:` 的条目跳过，不重复评估。

## eval 常见陷阱（dogfood 积累）

| 陷阱 | 说明 | 发现日期 |
|------|------|---------|
| **用 niche 工具链判断 idea 价值** | 不要因为"WSL 下不可行""需要特定 OS 环境"就否定想法。WSL/特定工具链是小众群体，idea 应面向通用场景评估。技术约束放在 `我想让 AI 帮我做` 里作为实现任务，不影响 eval 判定。 | 2026-05-26 |

发现新陷阱后追加到此表。

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
