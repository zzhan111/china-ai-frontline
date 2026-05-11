# 中国 AI 前线 (china-ai-frontline)

面向海外华人(UIUC 校友圈为辐射锚点)的中国 AI 生态观察自媒体的**内容运营仓库**。

公众号现状:6400 关注,断更 ~12 个月,处于流量池低端。本仓库用于支撑**复更冷启动 + 长期内容运营**。

---

## ⚠️ 协作准则:先读 GOVERNANCE

**任何对本仓库做写操作的 agent / 工具 / 人,在动手之前必须读 [`GOVERNANCE.md`](GOVERNANCE.md)。**

核心三条(简版,不替代正文):

1. **对话即代码,仓库即 context,演进即 PR** — 完整理念见 [`raw/2026-05-11-git-branching-dialogue-memory.md`](raw/2026-05-11-git-branching-dialogue-memory.md)
2. **`raw/` 不可变** — 只追加,绝不修改/删除/重命名
3. **永不直接 commit `main`** — 一切走分支 + PR,审核合并权在仓库所有者

违反这三条等同于损坏仓库的认知基线。

---

## 仓库地图

| 目录 | 用途 | 改动频率 | 可变性 |
|---|---|---|---|
| `GOVERNANCE.md` | **治理规则,最高优先级** | 极低,需 `governance/*` 分支 | 通过 PR |
| `docs/` | 战略层:定位、受众画像、内容支柱、冷启动计划 | 低 | 通过 PR |
| `raw/` | 原始对话/素材归档 | 仅追加 | **不可修改** |
| `topics/` | 选题卡片,每篇一个 markdown,按支柱分子目录 | 高 | 通过 PR |
| `ops/` | 发布流程、渠道矩阵、自查清单 | 中 | 通过 PR |

## 当前阶段

**冷启动期(验证期)**——以支柱四(中美双边视角)为主力,支柱二/五做延展测试,前 5 篇形成一致内容簇,目标是重建平台信号 + 唤回老粉。

详见 [`docs/cold-start-plan.md`](docs/cold-start-plan.md)。

## 工作流(在 PR 框架下)

1. 新选题 → **切 `topic/NNN-slug` 分支** → 在 `topics/pillar-X/` 下复制 `_template.md`,新建 `NNN-slug.md` → 提 PR
2. 选题成熟 → 在卡片里把 `status` 改为 `drafting` / `ready` / `published`,**通过新 PR 提交**
3. 发布 → 在卡片底部补 `published_url` 和 `published_at`,在 `ops/distribution-channels.md` 同步分发记录,**仍通过 PR**

(以上每一步都不直接 commit main)

## 命名约定

- 选题卡片:三位数字编号 + 短 slug,例如 `001-uiuc-7-alumni-returning.md`
- 编号在**全仓库内全局唯一**(不按支柱重置),方便引用和检索
- raw 归档:`YYYY-MM-DD-source-topic.md`
- 分支命名:见 [`GOVERNANCE.md`](GOVERNANCE.md) §4
