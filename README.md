# 中国 AI 前线 (china-ai-frontline)

面向海外华人(UIUC 校友圈为辐射锚点)的中国 AI 生态观察自媒体的**内容运营仓库**。

公众号现状:6400 关注,断更 ~12 个月,处于流量池低端。本仓库用于支撑**复更冷启动 + 长期内容运营**。

---

## 仓库地图

| 目录 | 用途 | 改动频率 |
|---|---|---|
| `docs/` | 战略层:定位、受众画像、内容支柱、冷启动计划 | 低 |
| `raw/` | 原始对话/素材归档,**只增不改**,作为决策溯源 | 仅追加 |
| `topics/` | 选题卡片,每篇一个 markdown,按支柱分子目录 | 高 |
| `ops/` | 发布流程、渠道矩阵、自查清单 | 中 |

## 当前阶段

**冷启动期(验证期)**——以支柱四(中美双边视角)为主力,支柱二/五做延展测试,前 5 篇形成一致内容簇,目标是重建平台信号 + 唤回老粉。

详见 [`docs/cold-start-plan.md`](docs/cold-start-plan.md)。

## 工作流

1. 新选题 → 在 `topics/pillar-X/` 下复制 `_template.md`,新建 `NNN-slug.md`
2. 选题成熟 → 在卡片里把 `status` 改为 `drafting` / `ready` / `published`
3. 发布 → 在卡片底部补 `published_url` 和 `published_at`,在 `ops/distribution-channels.md` 同步分发记录

## 命名约定

- 选题卡片:三位数字编号 + 短 slug,例如 `001-uiuc-7-alumni-returning.md`
- 编号在**全仓库内全局唯一**(不按支柱重置),方便引用和检索
- raw 归档:`YYYY-MM-DD-source-topic.md`
