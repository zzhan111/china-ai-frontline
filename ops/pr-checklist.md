# Self-Merge PR Checklist

> 单人仓库的 PR-only 流程,最大的退化风险是 **self-merge 变成机械点击**。
> 本清单是合并前的最后一道闸口,逐项确认完才点 Merge。
> 任何一项不过关 → 不合并,在原分支继续 commit(见 [`GOVERNANCE.md`](../GOVERNANCE.md) §2.3)。

---

## 通用项(所有 PR 都查)

### 一、规则合规

- [ ] PR 在 §2.2 规定的四项信息(分支名 / 改动文件 / 改动意图 / 链接)在对话中已明确报告
- [ ] PR 改动是否包含对 `raw/` 中**已有文件**的修改? → 如果是,**强制 close,不合并**(违反 §1)
- [ ] PR 改动是否触碰 `GOVERNANCE.md`? → 如果是,分支前缀必须是 `governance/`,且 PR description 显式说明改了哪些条款
- [ ] 所有 commit message 是否符合 §5 格式(`<scope>: <imperative summary>`)?

### 二、命名与组织

- [ ] 分支名是否符合 §4 的前缀约定?
- [ ] 文件是否落在正确目录?(选题卡片在 `topics/pillar-X/`,战略文档在 `docs/`,运营文档在 `ops/`)
- [ ] 文件名是否符合命名约定?(选题卡片:`NNN-slug.md`,编号全局唯一;raw:`YYYY-MM-DD-source-topic.md`)

### 三、内部一致性

- [ ] 改动有没有连带需要更新的兄弟文档?
  - 改了 `docs/cold-start-plan.md` 里的篇目顺序 → `topics/` 下对应卡片的 `id` 是否还一致?
  - 改了某篇选题的 status → `docs/cold-start-plan.md` 的状态表是否同步?
  - 改了支柱定义 → `docs/content-pillars.md` 与各 `topics/pillar-X/README.md` 是否一致?
- [ ] 内部链接(相对路径)是否有效?新建 / 重命名文件后,有没有遗留的失效引用?

### 四、可读性

- [ ] PR description 中是否说清"为什么改"(不是"改了什么" —— diff 已经说明改了什么)?
- [ ] 改动较大(>200 行)的 PR,是否在 description 里给了 reviewer 的导读顺序?

---

## 特定 PR 类型的额外项

### A. 新增选题卡片(`topic/*`)

- [ ] 编号是否全局唯一?(扫一眼 `topics/` 全树,确认没冲突)
- [ ] 卡片 frontmatter 完整:`id` / `title` / `pillar` / `status` / `target_persona` / `hook_type` / `created`
- [ ] `status: idea` 起步,不要跳级到 `drafting` 以上
- [ ] 价值主张、受众钩子、避坑清单三段是否都填了?(不填的预留位写 TBD 即可,但不留空标题)
- [ ] 是否反映到 `docs/cold-start-plan.md` 的篇目表?

### B. 选题卡片状态推进(`topic/*`)

- [ ] `status` 流转是否合法?(`idea → drafting → ready → published`,不可回退,例外需在 PR description 解释)
- [ ] 从 `ready` 推进到 `published` 时,**必须**已填:`published_url` / `published_at`
- [ ] 是否同步更新了 `ops/distribution-channels.md` 的分发记录表?
  - **例外**:仅"分发记录表填一行"可走 §3.5 豁免直推

### C. 战略文档变更(`docs/*`)

- [ ] 改动是否会让已有的 `topics/` 卡片"失效"?(例如改了受众权重,某些卡片的 target_persona 设定是否仍合理?)
- [ ] PR description 是否回答了"为什么现在改"(触发事件 / 数据 / 新认知)?

### D. 治理变更(`governance/*`)

- [ ] 改动是否会让历史 raw 的解读发生漂移?如果是,PR description 必须说明
- [ ] 是否需要同步更新 Claude 的 `memory_user_edits`?
- [ ] 历史豁免段落(§8 类)是否需要追加新日期/事件?

### E. raw 追加(`raw/*`)

- [ ] **再次确认是追加,不是修改**
- [ ] 文件名格式:`YYYY-MM-DD-source-topic.md`
- [ ] 内容是否真的"原始"?(没经过整理 / 重新组织 / 修正措辞 —— 如果整理过,应该放 `docs/` 而非 `raw/`)
- [ ] frontmatter 是否标注了来源、时间、`status: archived`?

---

## §3.5 豁免直推的事后核查(每月一次)

不属于 PR 流程,但是治理链的一部分,放在这里以免散落。

每月第一个工作日:

- [ ] 跑 `git log main --grep="^express:" --since="1 month ago"`
- [ ] 逐条核对:每条 `express:` 提交是否真的属于 §3.5 白名单?
- [ ] 有没有夹带非豁免改动(例如借 typo 修复之名顺手改了一句策略)?
- [ ] 豁免频率是否异常?(基线:每周 ≤ 3 条;若显著高于此值,说明白名单设计有问题,需要走 `governance/*` PR 重新审视)
