# 中国 AI 前线 (china-ai-frontline)

面向海外华人(UIUC 校友圈为辐射锚点)的中国 AI 生态观察自媒体的**内容运营仓库**。

公众号现状:6400 关注,断更 ~12 个月,处于流量池低端。本仓库用于支撑**复更冷启动 + 长期内容运营**。

---

## 📊 文章进度总览

| # | 标题 | 支柱 | 状态 | 终稿 | 发布 |
|---|---|---|---|---|---|
| 001 | [我认识的 7 个 UIUC 校友，过去 12 个月里 4 个回国了](drafts/001/README.md) | 四 | ✅ final-candidate | [`001-final-final.md`](drafts/001/001-final-final.md) | — |
| 002 | [海外华人团队正在重做 AI 家教：教育 AI 出海的第一批用户从哪来？](drafts/002/README.md) | 四 | ✅ final-candidate | [`002-preview.md`](drafts/002/002-preview.md) | — |
| 003 | Anthropic vs DeepSeek 推理对比 | 三 | 💡 idea | — | — |
| 004 | 海外用中国 AI API 指南 | 五 | 💡 idea | — | — |
| 005 | 回还是留：UIUC 深度对话 | 四 | 💡 idea | — | — |

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
│   └── cold-start-plan.md
├── raw/                         ← 原始素材归档（只追加，不可变）
│   ├── 2026-05-11-opus-brainstorm.md
│   ├── 2026-05-11-git-branching-dialogue-memory.md
│   ├── 2026-05-12-cowork-001-article-constitution.md
│   └── 2026-05-12-cowork-comments-revision-guide.md
├── topics/                      ← 选题卡片
│   ├── _template.md
│   ├── pillar-1/  pillar-2/  pillar-3/
│   ├── pillar-4/
│   │   ├── 001-uiuc-7-alumni-returning.md       ← #001 完整执行母版
│   │   ├── 002-overseas-education-ai-growth.md  ← #002 选题卡片
│   │   ├── 003-anthropic-vs-deepseek-reasoning.md
│   │   └── 005-return-or-stay-uiuc-deep-talk.md
│   └── pillar-5/
│       └── 004-overseas-china-api-guide.md
├── drafts/                      ← 文章草稿（每篇一个子目录）
│   ├── 001/                     ← #001 项目目录
│   │   ├── README.md            ← 进度、版本演进分析、发布数据
│   │   ├── 001-draft-v1.md
│   │   ├── 001-draft(refactor)-v2.md
│   │   ├── 001-draft-v2.1.md
│   │   ├── 001-Final.md
│   │   └── 001-final-final.md   ← #001 终稿候选
│   └── 002/                     ← #002 项目目录
│       ├── README.md            ← 进度、三版演进分析（v1.1→V2→Preview）、发布数据
│       ├── 002-draft-v1.1.md
│       ├── 002-draft-V2.md
│       └── 002-preview.md       ← #002 终稿候选（发送前预览稿）
└── ops/                         ← 运营流程
    ├── publishing-checklist.md
    ├── distribution-channels.md
    └── pr-checklist.md
```

| 目录 | 用途 | 改动频率 | 可变性 |
|---|---|---|---|
| `GOVERNANCE.md` | **治理规则,最高优先级** | 极低,需 `governance/*` 分支 | 通过 PR |
| `docs/` | 战略层:定位、受众画像、内容支柱、冷启动计划 | 低 | 通过 PR |
| `raw/` | 原始对话/素材归档 | 仅追加 | **不可修改** |
| `topics/` | 选题卡片,每篇一个 markdown,按支柱分子目录 | 高 | 通过 PR |
| `drafts/` | 文章草稿,每篇一个子目录含 README + 版本文件 | 高 | 通过 PR |
| `ops/` | 发布流程、渠道矩阵、自查清单、PR checklist | 中 | 通过 PR(部分 §3.5 豁免) |

## 当前阶段

**冷启动期(验证期)**——以支柱四(中美双边视角)为主力,支柱二/五做延展测试,前 5 篇形成一致内容簇,目标是重建平台信号 + 唤回老粉。

详见 [`docs/cold-start-plan.md`](docs/cold-start-plan.md)。

## 工作流(在 PR 框架下)

1. 新选题 → **切 `topic/NNN-slug` 分支** → 在 `topics/pillar-X/` 下复制 `_template.md`,新建 `NNN-slug.md` → 提 PR
2. 选题成熟 → 在卡片里把 `status` 改为 `drafting` / `ready` / `published`,**通过新 PR 提交**
3. 写作完成 → 在 `drafts/NNN/README.md` 中更新状态和终稿链接
4. 发布 → 在 `drafts/NNN/README.md` 补发布数据,在 `ops/distribution-channels.md` 同步分发记录
   - 仅"分发记录表填一行"和"发布数据填充"可走 §3.5 豁免

合并任何 PR 前 → 走 [`ops/pr-checklist.md`](ops/pr-checklist.md)。

## 命名约定

- 选题卡片:三位数字编号 + 短 slug,例如 `001-uiuc-7-alumni-returning.md`
- 草稿目录:三位数字编号,例如 `drafts/001/README.md`
- 编号在**全仓库内全局唯一**(不按支柱重置),方便引用和检索
- raw 归档:`YYYY-MM-DD-source-topic.md`
- 分支命名:见 [`GOVERNANCE.md`](GOVERNANCE.md) §4
- Commit message:见 [`GOVERNANCE.md`](GOVERNANCE.md) §5(包括 `express:` 豁免前缀)
