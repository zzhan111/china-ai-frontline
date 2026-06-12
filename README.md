# 中国 AI 前线 (china-ai-frontline)

面向海外华人、AI 创业者与中国 AI 生态观察者的**多平台内容操作系统**。

本仓库不只服务公众号长文，也服务 X、小红书、朋友圈等碎片化输出渠道。公众号负责长文沉淀；X、小红书、朋友圈负责想法验证、反馈收集和同好连接。

核心闭环：

```
idea → AI 整理 → 找近似实现 → 平台草稿 → 发布检查 → 手动发布 → 反馈记录 → 升级成长文或归档
```

公众号现状：6400 关注，断更 ~12 个月，处于流量池低端。本仓库用于支撑**复更冷启动 + 长期内容运营 + 多平台执行闭环**。

---

## 📊 文章进度总览

| # | 标题 | 支柱 | 状态 | 终稿 | 发布 |
|---|---|---|---|---|---|
| 001 | [我认识的 7 个 UIUC 校友，过去 12 个月里 4 个回国了](drafts/001/README.md) | 四 | ✅ 已发 | [`001-final-final.md`](drafts/001/001-final-final.md) | 2026-05-12 |
| 002 | [海外华人团队正在重做 AI 家教：教育 AI 出海的第一批用户从哪来？](drafts/002/README.md) | 二+五 | ✅ 已发 | [`002-preview.md`](drafts/002/002-preview.md) | 2026-05-16 |
| 003 | 中国 AI 生态地图:海外华人最容易误读的差异 | 二 | ✅ 已发  | [`003-preview.md`](drafts/003/003-preview.md)  | 2026-05-21 |
| 004 | [让大模型走出屏幕，去拧动工厂里的阀门](drafts/004/README.md) | 三 | ✅ 已发 | [`preview.md`](drafts/004/preview.md) | 2026-05-29 |
| 005 | [大平台都有 Agent 之后，为什么你还是会需要一个自己的 AI 助手？](drafts/005/README.md) | 二 | ✅ 已发 | [`preview.md`](drafts/005/preview.md) | 2026-06 |
| 006 | [Fable 5 封神了吗：一次发布 24 小时内的全面调研](drafts/006/evolution.md) | 二 | ✅ 已发 | [`006-published(preview).md`](drafts/006/006-published\(preview\).md) | 2026-06 |
| 007 | [Agent能干活，也能赚钱了——两个信号说明 Agent 经济的完整回路已经出现](drafts/007/evolution.md) | 二 | ✅ 已发 | [`published.md`](drafts/007/published.md) | 2026-06-12 |
| 008 | 达里奥的"树懒"提案：Anthropic CEO 为什么现在主动求监管？ | 二 | ✅ 已发 | [`published.md`](drafts/008/published.md) | 2026-06 |

> 状态说明：💡 idea → 📝 drafting → ✅ final-candidate → 🚀 published

---

## ⚠️ 协作准则:先读 GOVERNANCE

**任何对本仓库做写操作的 agent / 工具 / 人,在动手之前必须读 [`GOVERNANCE.md`](GOVERNANCE.md)。**

核心三条(简版,不替代正文):

1. **对话即代码,仓库即 context,演进即 PR** — 完整理念见 [`raw/2026-05-11-git-branching-dialogue-memory.md`](raw/2026-05-11-git-branching-dialogue-memory.md)
2. **`raw/` 不可变** — 只追加,绝不修改/删除/重命名
3. **永不直接 commit `main`** — 一切走分支 + PR,审核合并权在仓库所有者
   - 例外:符合 [`GOVERNANCE.md`](GOVERNANCE.md) §3.5 的封闭白名单(typo、链接修复、分发记录填充等),可走 `express:` 直推

合并 PR 前请走一遍 [`ops/pr-checklist.md`](ops/pr-checklist.md)。

违反以上等同于损坏仓库的认知基线。

---

## 仓库地图

```
china-ai-frontline/
├── README.md                    ← 你在这里
├── GOVERNANCE.md                ← 治理规则（最高优先级）
├── docs/                        ← 战略层
│   ├── strategy.md
│   ├── audience-personas.md
│   ├── content-pillars.md
│   ├── cold-start-plan.md
│   └── platform-strategy.md     ← 多平台职责与升级规则
├── inbox/                       ← 碎片想法捕捉（按月份一个文件）
│   ├── README.md
│   ├── 2026-05.md
│   └── 2026-06.md
├── posts/                       ← 社媒发布包（X / 小红书 / 朋友圈）
│   ├── README.md
│   ├── x.md
│   ├── xiaohongshu.md
│   └── moments.md
├── raw/                         ← 原始素材归档（只追加，不可变）
│   ├── 2026-05-11-opus-brainstorm.md
│   ├── 2026-05-11-git-branching-dialogue-memory.md
│   ├── 2026-05-12-cowork-001-article-constitution.md
│   ├── 2026-05-12-cowork-comments-revision-guide.md
│   ├── 2026-05-18-china-ai-wechat-account-resurrection-cross-analysis-90day-roadmap.md
│   └── 2026-05-18-china-ai-wechat-account-resurrection-longitudinal-horizontal-analysis.md
├── topics/                      ← 选题卡片
│   ├── README.md                ← 支柱总览表
│   ├── _template.md
│   ├── pillar-1/
│   │   └── README.md
│   ├── pillar-2/
│   │   ├── README.md
│   │   ├── 002-overseas-education-ai-growth.md
│   │   ├── 003-china-ai-ecosystem-map-misread-differences.md
│   │   ├── 005-agent-platform-vs-personal.md
│   │   └── 007-agent-production-and-marketplace.md
│   ├── pillar-3/
│   │   └── README.md
│   ├── pillar-4/
│   │   ├── README.md
│   │   └── 001-uiuc-7-alumni-returning.md
│   └── pillar-5/
│       └── README.md
├── data/                        ← 结构化数据明细
│   ├── README.md
│   ├── 001/
│   │   └── 20260513_数据明细(毕业9年后,我认识的4个UIUC...).xls
│   └── 002/
│       └── 20260517_数据明细(AI行业薪资与融资).xls
├── drafts/                      ← 文章草稿（每篇一个子目录）
│   ├── 001/                     ← #001 项目目录
│   │   ├── README.md            ← 进度、版本演进分析、发布数据
│   │   ├── 001-draft-v1.md
│   │   ├── 001-draft(refactor)-v2.md
│   │   ├── 001-draft-v2.1.md
│   │   ├── 001-Final.md
│   │   └── 001-final-final.md   ← 终稿
│   ├── 002/                     ← #002 项目目录
│   │   ├── README.md
│   │   ├── 002-draft-v1.1.md
│   │   ├── 002-draft-V2.md
│   │   └── 002-preview.md       ← 终稿
│   ├── 003/                     ← #003（卡片已发，草稿待补）
│   ├── 004/                     ← #004（人物访谈）
│   │   ├── README.md
│   │   ├── 004-draft-v1.md
│   │   ├── 004-draft-v2.md
│   │   └── preview.md           ← 终稿
│   ├── 005/                     ← #005（意见型，平台 vs 本地 Agent）
│   │   ├── README.md
│   │   ├── 005-draft-v1.md
│   │   ├── 005-draft-v1.1.md
│   │   ├── 005-draft-v1.2.md
│   │   ├── 005-draft-v1.3.md
│   │   ├── preview.md           ← 终稿
│   │   └── evolution.md
│   ├── 006/                     ← #006（热点调研型，Fable 5 封神）
│   │   ├── 006-draft-v1.0.md
│   │   ├── 006-draft-v1.1.md
│   │   ├── 006-published(preview).md  ← 终稿
│   │   └── evolution.md
│   ├── 007/                     ← #007（意见型，Agent 经济回路）
│   │   ├── 007-draft-v1.0.md
│   │   ├── 007-draft-v1.1.md
│   │   ├── preview.md
│   │   ├── published.md         ← 终稿
│   │   └── evolution.md
│   └── 008/                     ← #008（热点调研型，达里奥提案）
│       ├── draft-v1.0.md
│       ├── draft-v1.1.md
│       ├── draft-v1.2.md
│       ├── preview.md
│       ├── published.md         ← 终稿
│       └── evolution.md
├── contracts/                   ← 发布质量契约
│   ├── posts/                    ← 短社媒 contract
│   └── longform/                 ← 长文 contract (building-blocks)
│       ├── building-blocks.md    ← LF-1~LF-13 维度与判据（v0.4）
│       └── EVOLUTION.md          ← contract 自身演进记录
├── ops/                         ← 运营流程
│   ├── publishing-checklist.md
│   ├── distribution-channels.md
│   ├── pr-checklist.md
│   └── social-post-checklist.md ← 社媒统一发布检查
├── skills/                      ← coding agent 工作说明
│   └── social-content-loop.md   ← inbox → posts 闭环工作流
└── .tmp/                        ← 临时文件（不入库）
```

| 目录 | 用途 | 改动频率 | 可变性 |
|---|---|---|---|
| `GOVERNANCE.md` | **治理规则,最高优先级** | 极低,需 `governance/*` 分支 | 通过 PR |
| `docs/` | 战略层:定位、受众画像、内容支柱、冷启动计划、平台策略 | 低 | 通过 PR |
| `raw/` | 原始对话/素材归档 | 仅追加 | **不可修改** |
| `inbox/` | 碎片想法捕捉（按月份一个文件） | 极高（每日） | 通过 PR（可批量） |
| `posts/` | 社媒发布包（X / 小红书 / 朋友圈） | 高（每周批量） | 通过 PR |
| `contracts/` | 长文与短社媒的发布质量契约（building-blocks LF-1~LF-13） | 中 | 通过 PR |
| `topics/` | 选题卡片 + README 总览,按支柱分子目录 | 高 | 通过 PR |
| `drafts/` | 文章草稿,每篇一个子目录含 README + 版本文件 | 高 | 通过 PR |
| `data/` | 结构化数据明细(Excel/CSV/JSON),按文章编号分子目录 | 低 | 通过 PR |
| `ops/` | 发布流程、渠道矩阵、自查清单、PR checklist、社媒检查 | 中 | 通过 PR(部分 §3.5 豁免) |
| `skills/` | coding agent 工作说明（如 social-content-loop） | 低 | 通过 PR |

## 当前阶段

**冷启动期(验证期)**——以支柱四(中美双边视角)为主力,支柱二/五做延展测试,前 5 篇形成一致内容簇,目标是重建平台信号 + 唤回老粉。

详见 [`docs/cold-start-plan.md`](docs/cold-start-plan.md)。

## 工作流(在 PR 框架下)

### 长文工作流（公众号）

1. 新选题 → **切 `topic/NNN-slug` 分支** → 在 `topics/pillar-X/` 下复制 `_template.md`,新建 `NNN-slug.md` → 提 PR
2. 选题成熟 → 在卡片里把 `status` 改为 `drafting` / `ready` / `published`,**通过新 PR 提交**
3. 写作完成 → 在 `drafts/NNN/README.md` 中更新状态和终稿链接
4. 发布 → 在 `drafts/NNN/README.md` 补发布数据,在 `ops/distribution-channels.md` 同步分发记录
   - 仅"分发记录表填一行"和"发布数据填充"可走 §3.5 豁免

### 社媒工作流（X / 小红书 / 朋友圈）

1. 想法捕捉 → 追加到 `inbox/YYYY-MM.md`
2. AI 处理 → 按 [`skills/social-content-loop.md`](skills/social-content-loop.md) 生成 `posts/` 草稿
3. 发布前检查 → [`ops/social-post-checklist.md`](ops/social-post-checklist.md)
4. 手动发布 → 在 post block 内回填链接和反馈
5. 周复盘 → 决定是否升级为 `topics/` 长文选题
6. PR 节奏：`inbox/` 可日批量，`posts/` 周批量，结构性变更单独 PR

合并任何 PR 前 → 走 [`ops/pr-checklist.md`](ops/pr-checklist.md)。

## 命名约定

- 选题卡片:三位数字编号 + 短 slug,例如 `001-uiuc-7-alumni-returning.md`
- 草稿目录:三位数字编号,例如 `drafts/001/README.md`
- 编号在**全仓库内全局唯一**(不按支柱重置),方便引用和检索
- raw 归档:`YYYY-MM-DD-source-topic.md`
- 分支命名:见 [`GOVERNANCE.md`](GOVERNANCE.md) §4
- Commit message:见 [`GOVERNANCE.md`](GOVERNANCE.md) §5(包括 `express:` 豁免前缀)
