# tools/

Repo 工具脚本。每个工具单文件，stdlib only，跨平台。

## posts-eval.py

Static checker for `posts/` drafts against `contracts/posts/v1.1`.

### 用法

```bash
# 检查单文件
python tools/posts-eval.py posts/x.md

# 检查整个目录（递归 .md）
python tools/posts-eval.py posts/

# 输出 JSON（给 agent 消化）
python tools/posts-eval.py --json posts/x.md
```

退出码：

- `0` — 没有 FAIL
- `1` — 至少一个 post 触发 FAIL
- `2` — 用法错误

### 设计选择

参考 [bb-adapter-evolver/tools/bb-eval](../docs/decisions/) 的两条规则：

1. **只做机械检查（mechanical checks）。** 字数、AI 词汇频次、极限词、audience 路由、黑话密度——能用 regex 抓到的都在这里抓。
2. **不做内容质量评判（subjective scoring）。** 钩子强度、可转发性、真实痕迹——这些要 LLM 主编看，归 SKILL（暂未实现）和人工 review。

输出三档：

- **PASS** — 通过该检查
- **WARN** — 提示性问题，主编需要看一眼
- **FAIL** — 触发硬性禁区，直接 rejected

### 当前覆盖（v1）

| 层 | 检查 | 触发条件 |
|---|---|---|
| common §2 | `meta:状态/来源/首发平台/audience` | 字段缺失 |
| common §3 #5 | `ai-flag:hard-reject` | ≥3 个 red flag → FAIL |
| common §4.4 | `ai-flag:*` | AI 词汇 / 元价值断言 / 不是X是Y / em dash / 排比 ... |
| x-cn §2.1 | `hook:anti-pattern` | 软抽象/元描述/无锚反问开场 |
| x-cn §2.3 | `translationese:old` | 在...背景下 / 进行+动词 / 性字滥用 |
| x-cn §2.3 | `translationese:new-rhetoric` | 短句自问自答 / setup-punch |
| x-cn §2.4 | `retweet:dig-hole` | "详见/在 repo 里有记录" 无链接 |
| x-cn §3 | `len:tweet-overflow` | 单推 >140 中文字符 |
| x-cn §3 | `fmt:hashtag-overflow / markdown-heading` | hashtag >2 / 出现 `# 标题` |
| xiaohongshu §3.1 | `title:length` | 标题 >20 字 |
| xiaohongshu §4 | `len:under / len:over` | <500 / >1800 字 |
| xiaohongshu §6 #1 | `hard-reject:ad-law` | 最/第一/唯一/绝对 → FAIL |
| xiaohongshu §6 #5 | `hard-reject:audience-mismatch` | audience 含工程师/coding agent → FAIL |
| xiaohongshu §3.3 | `actionable:tech-prereq` | 出现 git/commit/PR/CLI 等 |
| moments §3.2 | `len:hard-limit / len:warn` | >500 FAIL / >300 WARN |
| moments §3.1 | `authenticity:formal-opening` | "今天想和大家分享" → FAIL |
| moments §3.3 | `relationship:jargon-{low,mid,fatal}` | 按黑话字符占比分级 |

### 已知限制

- **营销式短句叠加无法机械识别**：v1.1 common §4.4 加的"三/四字短句堆叠"判据，对 `自我繁殖。天然吸引。` 这种连续短句有效，但对 `1. ... 2. ... 3. ...` 形式的列表项营销腔抓不到——那是结构/语义问题，需要 LLM 看。
- **PR/issue 引用计数粗糙**：`PR #14 和 #15` 只算 1 个引用（正则匹配 `PR\s*#\d+`），不会触发"≥2 引用无 github 链接"警告。
- **黑话密度是 heuristic**：用"黑话词字符数 / 总字符数"估算密度，对短文容易偏高/偏低。准确率参考 ±10%。
- **首发平台从文件名推断**：`posts/x.md` → x-cn，`posts/x-2026-05-24-foo.md` → x-cn。元数据里 `首发平台:` 作 fallback。

### 不做的事

- ❌ 总分计算（mechanical 维度算不出综合分；分数计算归 LLM 主编）
- ❌ 自动改稿（评分器只指出问题，不修）
- ❌ 翻 git history 找历史版本对比（diff 用 git）
- ❌ 调外部 LLM API（保持 stdlib only，零依赖）

### Phase 2 路线

posts-eval v1 是 phase 2 的第一个 deliverable。下一步：

- `skills/posts-author.md` — 给 agent 写稿前看的 SKILL（包含 inviolable rules、authoring workflow、posts-eval 集成）
- 把 posts-eval wire 进 `skills/social-content-loop.md` step 5/6
- 累积 dogfood 反馈，refine checks（见 [contracts/posts/EVOLUTION.md](../contracts/posts/EVOLUTION.md)）

Phase 3 / 4 见 [bb-adapter-evolver 四阶段思路](https://github.com/) 的本地翻译。
