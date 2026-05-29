# contracts/longform/EVOLUTION.md

> 累积 contracts/longform 进化的诊断日志。镜像 `contracts/posts/EVOLUTION.md` 的精神：
> append-mostly，每条记录"做了什么 / 学到什么 / 还没 close 的 open item"。
> **加在底部，不要重写历史。每条都标日期。**

---

## 2026-05-29 — v0 building blocks 诞生（来源：004 v1 人工评审）

公众号长文是 `contracts/posts/`（短社媒）覆盖不到的体裁。004 访谈初稿 v1 第一次跑"AI 铺满型长文"，用户人工评审给出关键诊断：

- **架构层（优点，保留）**：从"人的故事 → 初心想法 → 实践 → 下一个想法"形成闭环；结尾把人设丰富起来，读者能清晰感受到。
- **文笔层（病灶）**：① 流水账、一笔带过、没有重点；② 缺"活人感"；③ 不与读者共情（陌生概念不解释，如"反应釜"；不会用"内在对话逻辑"带读者探索）；④ 场景调性偏"直播间/自媒体喧嚣"，cheap/虚假，应改为稳重/人文/引发思考。

由此抽象出 6 条长文特有维度 **LF-1～LF-6**（见 `building-blocks.md`）。正面样本锚定为南方人物周刊《失控的爱》（`raw/references/`）。

### 关键判断
- **contract first 哲学延续**：先沉淀 building block，不急着写评分器。长文主观维度（活人感/节拍）机械检测难，先靠 SKILL/人评，等样本够再编译 v1。
- **不重复造轮子**：AI 痕迹 / 硬性禁区 / 观察者红线全部继承 `posts/v1-common` + 001 宪法，longform 只加 6 条特有维度。

### Open items（v1 编译前）
- [ ] 004 v2 重写后，把"哪些 LF 维度真的改善了文笔"回填本文件（v1→v2 的 before/after 是 LF 维度的第一组实证）。
- [ ] 等下一篇长文（005?）再走一遍，凑齐每条维度 ≥2 病例/正例。
- [ ] humanizer 当前文档限定 `posts/*.md`、明确不含 `drafts/`（见 `skills/humanizer-usage.md` §处理范围）。本次用户要求对长文 draft 跑 humanizer——属工作流扩展，需决定：是否把 humanizer 处理范围正式扩到 `drafts/` 长文，还是长文用独立的 craft-pass。先记录，v1 时定。

### How to append
- 每次长文走"铺满→人评→重写"，把人评反馈映射回 LF-1～LF-6，append 一条。
- 只写跨 session 后需要重新捡起来的 context；纯 commit log 能查到的不写。
