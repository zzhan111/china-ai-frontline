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

- [x] 写 `skills/posts-author.md` — done in stacked PR after posts-eval v1
- [x] 把 posts-eval wire 进 `skills/social-content-loop.md` step 5/6 — done (step 5 = posts-eval, step 6 = humanizer; 顺序约束写明)
- [ ] 累积下一批样本（≥3 个新 draft）后看 v1.2 修订点
- [ ] 决定 audience 字段是否硬性必填（SKILL 已要求 agent 必填，但 contract 仍为 WARN——可在 v1.2 升 FAIL）

---

## 2026-05-25 — Phase 2 SKILL: posts-author.md + social-content-loop wired

`skills/posts-author.md` 落地（参考 bb-adapter-author/SKILL.md 结构）：
- 7 条 inviolable rules（contract first、不发明维度、audience 必填、eval-before-humanize、dig-hole-must-have-candy、不绕过 FAIL）
- 8 步 authoring workflow（read → identify → draft → self-review → eval → write → humanize → checklist）
- 8 个 anti-patterns（从 EVOLUTION dogfood 和 v1.1 修订证据总结）
- 6 个 workflow gates（必须停下来问人的决定）

`skills/social-content-loop.md` step 5 拆成：
- step 5: posts-eval（FAIL 必须修，不允许 soften 绕过）
- step 6: humanizer（保持原 PR #17 设计，加上**顺序约束**：humanize 必须在 eval 之后跑）

### Phase 2 完成度

| Phase | Deliverable | 状态 |
|---|---|---|
| 1 | Contract + bb-eval + validate against ysbang | ✅ (PR #18 + #19) |
| 2a | Eval tool (`tools/posts-eval.py`) | ✅ (PR #20) |
| 2b | SKILL (`skills/posts-author.md`) + wire to social-content-loop | ✅ (this PR) |
| 3 | Cross-platform 实战 + 反例驱动 refine | 等下一批 draft |
| 4 | (Conditional) evolver | 不动 |

### 下一步触发条件

按 `2026-04-22-why-not-evolver-first.md` 决定，phase 3 的触发是"用 SKILL 跑 cross-site validation"。本 repo 的 cross-site = cross-platform，即：

- 用 posts-author SKILL 写出 ≥3 个新 draft（每平台至少 1 个）
- 跑完整链路 step 1-7
- 把"SKILL 没说清、agent 仍犯的错"append 到本文件
- 当累积 ≥3 个新错误类型时，准备 v1.2 contract 修订

phase 4 evolver 的触发是"单次 SKILL 成功率 <30%"。当前样本太少无法计算，先不评估。

---

## 2026-05-25 — Phase 2b SKILL dogfood (PR #22 review #5)

PR #22 review 要求"在 merge 之前用 SKILL 走一遍完整流程写一篇 draft"。Dogfood 用 inbox 2026-05-24 22:36（browse.sh 换核适配思路）作为素材，按 `skills/posts-author.md` step 1-5 跑（step 6 humanize / step 7 checklist 不在 dogfood scope）。

**Artifact**：[`posts/x-2026-05-25-browse-sh-swap.md`](../../posts/x-2026-05-25-browse-sh-swap.md)（5-tweet X thread）

### 跑通的事

| Step | 做了什么 | 顺畅否 |
|---|---|---|
| 1 (read contract) | 读 v1-common + x-cn/v1.md | ✅ |
| 2 (identify route+audience) | 平台 X（用户没指定，按 §6 路由：反共识断言 + 技术圈 → X）；audience "AI builder + 浏览器自动化研究者" | ✅ 路由清晰 |
| 3 (draft platform-native) | 写 5 推 thread，钩子用"真正价值不是 X，是 Y"反共识断言 | ✅ |
| 4 (self-review) | 钩子检查 / 营销腔检查 / 挖坑给糖检查 / audience 路由 — 都过 | ✅ |
| 5 (run posts-eval) | 第一次：4 PASS / 2 WARN（em dash 滥用）→ 修 3 处 `——` → 第二次：**5 PASS / 0 WARN / 0 FAIL** ✅ | 见下方"卡壳" |

### 卡壳的事 → 触发的 fix（在同 PR）

1. **parser 不识别 single-draft-per-file 的 h1 header** (BLOCKER)
   - 现象：跑 `posts-eval.py posts/x-2026-05-25-browse-sh-swap.md` 输出 0/0/0
   - 原因：`POST_HEADER_RE` 只匹配 `^## ` (h2)；single-draft-per-file 用 h1
   - 修：regex 改成 `^#{1,3} `（接受 h1/h2/h3）
   - 影响：第一次 dogfood 就发现 parser 在 user 定的 "x-日期-主体.md" 命名规则下不工作

2. **SKILL self-review 漏了 em dash 自查** (SKILL gap)
   - 现象：我（agent）自己写的 draft 第一次跑就 9 个 em dash，触发 ai-flag:em-dash-abuse
   - 原因：SKILL Step 4 self-review checklist 没列 em dash 自查；anti-patterns table 没"em dash 滥用"
   - 修：Step 4 加 "em dash 自查"项；Anti-patterns table 加一行（dogfood post-2026-05-25-001 出处）
   - **元观察**：dogfood 的最大价值就是"agent 自己也犯 contract 警告的错"——证明 SKILL 没把检查项内化到 self-review，eval 才抓得到。SKILL 升级让 self-review 与 eval 对齐。

3. **posts-eval em dash 计数 likely overcounts** (eval bug, low priority)
   - 现象：body 实际 3 个 `——`，eval 报 9 次（×3）
   - 原因：`text.count("——") + text.count("—")` —— `——` 算 1 次 (count `——`) + 2 次 (count 单个 `—` 字符) = 3 次/个
   - 留 v1.2 修（信号方向对，只是数字偏大，先不阻塞）

### Dogfood 的"主编直觉对照"

跑完 5 PASS / 0 WARN，直觉评分（我作为主编）也认为是 approved 级。样本量太小（1 条），但 **SKILL + eval 的输出和直觉一致**。

这一条 dogfood **不足以**验证 SKILL 在"agent 想偷懒/绕过"场景下的强度——比如 agent 跳过 step 2 audience 确认直接 draft，或者选择 soften FAIL 而不是回 step 2/3。这些行为模式要等真实多 agent 多 session 后才能观察到。

### Open items（给 v1.2 / phase 3 用）

- [ ] **em dash 计数 overcounts**：留 v1.2 修 regex（用 `re.findall(r"——?", text)` 直接，或 `text.count("—") - text.count("——")`）
- [ ] **SKILL self-review checklist 持续追加**：每次 dogfood 发现"agent 漏看的东西"，append 到 step 4。当前已加 em dash；下次可能是别的
- [ ] **多 agent dogfood**：等其它 agent（Codex / Hermes / OpenClaw 用户）跑同样 SKILL，看是否会犯 Claude 不犯的错
- [ ] **audience 字段升 FAIL 时机**：SKILL 已要求必填；当 posts/ 里 ≥3 个 draft 都带了 audience 后，把 contract WARN 升 FAIL（v1.2 候选）

---

## How to append to this file

- **人**：每次 contract 修订、checker 更新、或跑 dogfood 发现非显然的事，写一条
- **agent**：每次 contract / posts-eval 工作完成，append "做了什么 / 跑了什么 / 还 open 什么"
- 不写：纯 commit log 能查到的事（用 `git log` 不用 EVOLUTION）
- 只写：跨 session 后下次需要重新捡起来的 context
