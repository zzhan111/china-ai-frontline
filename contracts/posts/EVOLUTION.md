# contracts/posts/EVOLUTION.md

> 累积 contracts/posts 进化的诊断日志。镜像 bb-adapter-evolver 的 `memory/soul.md`：
> append-mostly，每条记录"做了什么 / 学到什么 / 还没 close 的 open item"。
> **加在底部，不要重写历史。每条都标日期。**

---

## 2026-04-22 — bb-adapter-evolver 精神迁移

四阶段路线沿用：

| Phase | Goal | 本 repo 对应 |
|---|---|---|
| 1 | Contract + eval 静态检查 | `contracts/posts/v1.md` + `tools/posts-eval.py` |
| 2 | Skill loop 单 agent + checker 迭代 | `skills/posts-author.md`（TODO）+ `tools/posts-eval.py` 接入 |
| 3 | Cross-platform 实战 + 反例驱动 refine | dogfood + EVOLUTION.md（本文件） |
| 4 | （条件）单次成功率 <30% 时上 evolver | 暂不动 |

精神迁移结论：**Contract first, evolver later。没有 fitness signal，evolver 退化成随机搜索。**

---

## 2026-05-25 — Phase 1 complete (PR #18 + PR #19)

`contracts/posts/v1` baseline + `v1.1` 修订 merged。

- v1: 4 文件（v1-common + x-cn + xiaohongshu + moments），每个平台 contract extends common
- v1.1: 基于 PR #16 的 3 个真实 draft 评分对照，8 项修订（2 收口 + 6 重写判据）

详细评分对照见 PR #19 描述。

---

## 2026-05-25 — Phase 2 bootstrap: posts-eval v1

`tools/posts-eval.py` 落地，覆盖 v1.1 能机械检测的所有规则（~20 checks）。

### Dogfood 结果（PR #16 已合并的 4 个 draft）

```
TOTAL: 15 PASS / 19 WARN / 0 FAIL
```

| 文件 | post | 平台 | PASS/WARN/FAIL |
|---|---|---|---|
| posts/moments.md | post-2026-05-24-001 | moments | 4/2/0 |
| posts/x.md | post-2026-05-24-001 | x-cn | 4/3/0 |
| posts/x.md | post-2026-05-24-002 | x-cn | 4/8/0 |
| posts/xiaohongshu.md | post-2026-05-24-001 | xiaohongshu | 3/6/0 |

### 验证 v1.1 新增判据是否抓到了"主编直觉发现的问题"

| v1.1 新增判据 | 在 dogfood 中是否触发 | 触发位置 |
|---|---|---|
| `ai-flag:meta-value-assertion` (营销式元价值断言) | ✅ 4 个词命中 | post-002 |
| `retweet:dig-hole` (挖坑不给糖) | ✅ "在 repo 里有完整记录" 无链接 | post-002 |
| `hook:anti-pattern` (软抽象/价值预告开场) | ✅ 命中 3 处 | post-001, post-002 |
| `translationese:new-rhetoric` (新式英文修辞腔) | ✅ "短句自问自答" 1 次 | post-002 |
| `relationship:jargon-low/mid/fatal` (黑话密度阶梯) | ✅ "repo" 命中 jargon-low | moments post-001 |
| `actionable:tech-prereq` (小红书读者基础对齐) | ✅ git/commit/PR 命中 | xiaohongshu post-001 |

**结论：v1.1 加的 6 个判据全部在真实样本上打出了信号。** 这是 contract 修订有效性的直接验证——v1 上跑同样样本不会有这些 WARN。

### 0 FAIL 的解读

post-002 主编直觉是 `rejected`（-19 分），但 posts-eval 只打出 8 个 WARN，0 FAIL。

这是**设计意图**，不是 bug。理由：

- mechanical checks 抓"硬性匹配"（极限词、字数超限），主观判断（"营销腔"程度）抓不到
- 8 个 WARN 本身就是强信号：post-002 是全部 4 个 draft 里 WARN 最多的一个
- 最终 reject/approve 决策留给 LLM 主编，posts-eval 提供"哪些维度要重点看"

bb-adapter-evolver 的 bb-eval 也是同样设计：13 个静态 check 全是 PASS/WARN/FAIL，不算"adapter 综合分"。

### 暴露的 contract / 现状 gap

1. **audience 字段全 4 个 draft 都没填** — v1.1 §2 要求，但实际 posts/ 普遍未填。posts-eval 给 WARN 不给 FAIL。下一步决定：
   - (a) 把 audience 列为硬性必填，所有现有 draft 退到 needs_revision
   - (b) audience 设为可选但建议（保持现状）
   - **倾向 (b)**：posts/ 仍在演化期，硬性要求会阻塞写作

2. **PR/issue 引用计数粗糙** — `PR #14 和 #15` 在正则下只算 1 个引用，不触发"≥2 引用无链接"警告。
   - low-effort fix：改 regex 抓 `#\d+`（含 "和"/"和" 联结的多个）
   - 下次 v1.2 时一并修

3. **营销式短句叠加（list 形式）无法机械识别** — v1.1 加的"三/四字短句堆叠"对 `自我繁殖。天然吸引。` 有效，但对 post-002 的列表项 `1. 真正的差异化 ... 4. 天然吸引` 抓不到。
   - 这是 SKILL 的职责（LLM 看结构），不强行塞进 posts-eval

4. **首发平台需明确为 enum**：现 posts 里写 `X` / `小红书` / `朋友圈`（中文+英文混杂）。posts-eval 用 file name 推断 + metadata fallback，但 contract v1.1 §2 应该明确 `platform` enum 是 `x-cn / xiaohongshu / moments`（已是），而 `首发平台` 元数据字段需要标准化。

### Open items before Phase 2 SKILL

- [ ] 写 `skills/posts-author.md`（参考 bb-adapter-evolver 的 `SKILL.md`）：inviolable rules + authoring workflow + posts-eval 集成
- [ ] 把 posts-eval wire 进 `skills/social-content-loop.md` step 5/6（草稿生成后强制跑 eval，FAIL 直接打回）
- [ ] 累积下一批样本（≥3 个新 draft）后看 v1.2 修订点
- [ ] 决定 audience 字段是否硬性必填（影响 contract v1.2）

---

## How to append to this file

- **人**：每次 contract 修订、checker 更新、或跑 dogfood 发现非显然的事，写一条
- **agent**：每次 contract / posts-eval 工作完成，append "做了什么 / 跑了什么 / 还 open 什么"
- 不写：纯 commit log 能查到的事（用 `git log` 不用 EVOLUTION）
- 只写：跨 session 后下次需要重新捡起来的 context
