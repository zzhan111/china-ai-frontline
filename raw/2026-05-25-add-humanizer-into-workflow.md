### **核心改动：把 humanizer 作为 `posts/` 内容生成的强制前置步骤接入 `skills/social-content-loop.md` 和 `ops/social-post-checklist.md`，并在 `skills/` 下新增一个极短的本地适配文件 `skills/humanizer-usage.md`，不引入 git submodule，不改 README 顶部结构。**

我先说明假设，然后给出精确的文件改动。

### **假设**

1. 你已经把 `op7418/Humanizer-zh` 或 `blader/humanizer` 安装到了 Claude Code 的 `~/.claude/skills/` 下，能用 `/humanizer-zh` 或 `/humanizer` 触发。如果还没装，下面会包含一条最小安装指引。
2. 你不想把 humanizer 仓库 vendor 进 `china-ai-frontline`，避免和上游脱节、也不想破坏 repo 的轻量原则。
3. 中文内容默认走 `humanizer-zh`，英文内容走 `humanizer`。
4. humanizer 只作用于 `posts/*.md` 的“平台草稿”区，不作用于 `inbox/`、`raw/`、`topics/`、`drafts/`。这一点必须明确，否则会污染原始想法和长文。

### **设计原则**

- **不新增目录**。只改两个现有文件，加一个本地短文档。
- **接入点尽量靠后**。humanizer 应该在“草稿生成完”和“发布前检查”之间，不是一开始就 humanize。否则会丢失 AI 的结构化优势。
- **可跳过但必须声明**。如果跳过 humanizer，必须在 post block 里写明原因，避免静默退化。

---

### **改动 1：`skills/social-content-loop.md` 工作步骤里插入 humanizer 阶段**

在原来的 8 步工作流里，把 humanizer 作为 step 5（紧跟生成平台草稿之后、发布前检查之前）。

建议把 `skills/social-content-loop.md` 的“工作步骤”区改成：

```markdown
## 工作步骤

1. 从 inbox 中选择最多 3 条最值得处理的想法
2. 每条提炼一句话观点
3. 为每条寻找近似产品、近似实现或相似内容方向
4. 生成平台草稿（写入对应 `posts/*.md` 的"平台草稿"区）
5. **去 AI 味**（详见 `skills/humanizer-usage.md`）
   - 中文草稿 → 调用 `/humanizer-zh`
   - 英文草稿 → 调用 `/humanizer`
   - 用 humanized 版本覆盖"平台草稿"区
   - 在 post block 末尾追加 `humanizer: zh@<version> | en@<version> | skipped(reason: ...)`
6. 用 `ops/social-post-checklist.md` 做发布前检查
7. 标记是否建议发布
8. 发布后根据用户提供的数据补反馈
9. 判断是否升级成长文 topic
```

同时在“限制”区追加两条：

```markdown
## 限制

- 不创建新目录
- 不修改 `raw/`
- 不修改 `GOVERNANCE.md`
- 不直接改公众号长文
- 不为单条想法创建 PR
- 每次最多处理 3 条想法
- **不得对 `inbox/`、`raw/`、`topics/`、`drafts/` 中的内容运行 humanizer**
- **humanizer 只作用于 `posts/*.md` 的"平台草稿"区，不作用于"一句话观点"、"近似实现"、"发布后反馈"等结构化字段**
```

理由：humanizer 的价值是让发布内容更像人写的；如果对结构化字段也跑一遍，会把表格、链接、checklist 破坏掉。

---

### **改动 2：`ops/social-post-checklist.md` 增加一条强制项**

在“发布前检查”里加一条，位置放在“是否适合当前平台”之后、“是否值得现在发”之前：

```markdown
## 发布前检查

- [ ] 第一行是否有明确观点？
- [ ] 是否只讲一个核心想法？
- [ ] 是否不像公众号摘录？
- [ ] 是否有具体场景、例子或判断？
- [ ] 是否有一个可回复的问题？
- [ ] 是否已经找过近似产品、近似实现或相似内容？
- [ ] 是否适合当前平台？（平台职责见 [`docs/platform-strategy.md`](../docs/platform-strategy.md)）
- [ ] **是否已运行 humanizer 去除 AI 味？**（中文 `/humanizer-zh`，英文 `/humanizer`，详见 [`skills/humanizer-usage.md`](../skills/humanizer-usage.md)。若跳过须在 post block 注明原因）
- [ ] 是否值得现在发，而不是继续打磨？
```

不需要为 humanizer 再开一份单独的 checklist。一条 checkbox 足够，因为细节都在 `skills/humanizer-usage.md` 里。

---

### **改动 3：新增 `skills/humanizer-usage.md`（极短）**

放在已有的 `skills/social-content-loop.md` 旁边。整个文件控制在一屏内。

```markdown
# Humanizer 使用约定

社媒草稿在发布前必须去 AI 味。本仓库不 vendor humanizer 源码，只声明使用约定。

## 选择哪个版本

- 中文草稿 → `op7418/Humanizer-zh`，命令 `/humanizer-zh`
- 英文草稿 → `blader/humanizer`，命令 `/humanizer`
- 中英混合 → 先按主语言跑一次，再人工调整另一种语言的句子

## 一次性安装（仅需执行一次）

```bash
# 中文
npx skills add https://github.com/op7418/Humanizer-zh.git

# 英文
git clone https://github.com/blader/humanizer.git ~/.claude/skills/humanizer
```

## 调用方式

在 Claude Code 中：

```
/humanizer-zh
<粘贴 posts/*.md 中"平台草稿"区的内容>
```

或：

```
/humanizer
<paste the "平台草稿" content here>
```

## 处理范围

- 只对 `posts/*.md` 中 `### 平台草稿` 区的正文运行
- 不对 `一句话观点`、`近似实现 / 待查`、`发布后反馈` 运行
- 不对 `inbox/`、`raw/`、`topics/`、`drafts/` 运行

## 输出处理

1. 用 humanized 版本覆盖原"平台草稿"区
2. 在 post block 末尾追加一行：

   ```
   humanizer: zh@<version-or-date> | en@<version-or-date> | skipped(reason: ...)
   ```

3. 如果 humanized 版本明显丢失关键信息或专有名词，回滚并手动小修

## 必须保留的元素

humanizer 不应改动以下内容，如改动需手动复原：

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

其他情况一律必须 humanize。
```

---

### **post block 模板的最小调整**

`posts/README.md` 中的 post block 模板末尾追加一行就够。不要重写整个模板。

在原模板里：

```markdown
### 发布后反馈

发布时间：
链接：
回复：
收藏：
转发：
高质量反馈：
下一步：
```

之后加一行（建议放在“发布后反馈”之前，作为发布前签名）：

```markdown
### Humanizer

humanizer: zh@<version-or-date> | en@<version-or-date> | skipped(reason: ...)
```

也可以更简洁，直接合并进“发布后反馈”里，但单独一节有个好处：可以让 agent 在 step 5 完成时直接写入，不用等发布。

---

### **改动 4（可选，但建议）：在 `posts/x.md` 和 `posts/moments.md` 已有的第一个 post block 上补一次回填**

现在已有的两条草稿（meta-idea 那条）是合并 PR #14 时一起写进去的，没有经过 humanizer。

建议合并这次 PR 后，立刻对它们运行一次 humanizer，然后在 block 里补：

```markdown
### Humanizer

humanizer: zh@2026-05-25 (op7418/Humanizer-zh) | skipped for en
```

这样可以保证“工作流要求 humanize → 但 main 上有未 humanize 的草稿”不会变成长期不一致。

---

### **不建议做的事**

为了保持 simplicity first，下面几件事我建议**不要做**：

1. **不要把 humanizer 仓库 vendor 进 china-ai-frontline**。它有自己的版本演进（README 显示已经到 v2.5.1），vendor 进来会脱节。
2. **不要为 humanizer 写自动化脚本**。每天处理 ≤3 条 idea，手动 `/humanizer-zh` 完全可控。引入脚本反而增加结构性变更，需要走重 PR。
3. **不要新增 `humanized/` 目录或 `posts/raw/` vs `posts/final/` 双版本结构**。覆盖式更新 + 一行 humanizer 签名足够追溯，git history 已经保留了原始版本。
4. **不要把 humanizer 强制应用到 `topics/` 或 `drafts/`**。长文有更复杂的论证结构，machine humanize 可能破坏论证链；那是人工 + 复盘的事。

---

### **建议这次 PR 的最小分支与 commit**

| 项 | 建议 |
|---|---|
| 分支名 | `repo-os/humanize-before-post` |
| 是否走 express | 否，这是 skills + ops 流程性变更，必须 PR |
| 文件改动数 | 3 个文件 |
| commit | 单 commit：`repo-os: require humanizer pass before posts publish` |

具体 diff 范围：

```text
modified:   skills/social-content-loop.md   (insert step 5 + 2 限制条款)
modified:   ops/social-post-checklist.md    (insert 1 checkbox)
new file:   skills/humanizer-usage.md       (≤ 60 行)
optional:   posts/README.md                 (post block 末尾追加 Humanizer 字段)
optional:   posts/x.md, posts/moments.md    (对已有 block 补 Humanizer 签名)
```

如果你想一次到位，把 optional 也一起做；如果想最小化，只做前 3 个。

---

### **成功标准**

合并这次 PR 后，下次走 Day 1 流程时验证：

```text
1. 生成一条新 X 草稿 → verify: posts/x.md 多了一个新 block，"平台草稿"区有内容
2. 运行 /humanizer-zh → verify: 平台草稿区被替换，且未改动数字/链接/人名
3. block 末尾出现 humanizer 签名行
4. social-post-checklist 上 humanizer 一项被勾选
5. 手动发布，发布后反馈区有时间和链接
```

如果跑完这 5 步觉得“humanizer 一步是不是有点烦”，再讨论是否做更轻的封装。但在跑完之前不要预先优化。

---

### **关于 humanizer 本身的一个 push back**

humanizer 的核心是“去掉 AI-isms”，但你 X 上的内容已经具备了一些非常人化的元素：具体数字（7 个、4 个）、具体场景（UIUC、AI 家教）、具体判断（“不是统计学样本”）。这些原本就不容易被 AI-ify。

所以 humanizer 在你这里的作用，**不是把 AI 文本变人话**，而是**做发布前的最后一道安全网**，主要拦截：

- 三段式法则（“无缝、直观、强大”）
- 系动词回避（“作为……的证明”）
- 通用积极结论（“未来值得期待”）
- 否定式排比（“不只是……而是……”）

这些恰好是 thread 写久了最容易混进来的句式。把它当成 lint，而不是当成写作助手。这个心态会让你更愿意每次发前跑一遍。