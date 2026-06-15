# drafts/009/evolution.md

> 本文演化记录。append-mostly。不重写历史。

---

## 2026-06-15 — v1.0 初稿生成

### 做了什么

- 基于选题卡 5 个论点压缩为 6 个章节：一（平台画像）→ 二（四种模式对比）→ 三（中国玩家验证）→ 四（三个结构性约束）→ 五（非 Agent 经济但前身）→ 六（总结：平台的正确打开方式）
- 结构性选择：把"论点 5（与 007 的关系）"单独成章，而非塞进其他章节
- 开头用"2013 年第一笔交易"的场景开场而非直接摆数据
- 语言策略：所有判断句都紧跟数据锚点
- 第四章"三个结构性约束"是和 inbox 笔记最大不同的地方——补充了"客户信任"和"资本市场"

### 学到什么

- 5 个论点做 5 章 + 1 个收束（共 6 章）是合适的结构
- 纯产业分析风格与选题卡定位"洞察型"一致

### 还没 close 的 open item

- [ ] 字数审视
- [ ] 第四章三个约束过度简化风险
- [ ] 第五章交叉验证
- [ ] 结尾 too strong
- [ ] 配图映射
- [ ] RapidDirect AI Creator Lab
- [ ] 标题太长

---

## 2026-06-15 — v1.1 迭代

### 做了什么

1. 标题压缩："中美 AI 制造平台，差了一个 Xometry" → "差了一个 Xometry"
2. 软化结尾："正确打开方式" → "可能不是从最热闹的地方开始"
3. 第四章加边界声明："这三个不是完整解释"
4. 第五章加交叉验证：肺结节检测 AI（Mayo Clinic 94%）
5. 压缩 Fast Radius 段落：7 行 → 4 行
6. 加入 RapidDirect AI Creator Lab
7. 开场"中国没有跑出"加量级限定

### 学到什么

- 边界声明是防杠利器
- 医疗 AI 交叉验证效果好——双案例对照可复用
- 结尾从结论变为信号的改动比预想的重要
- Fast Radius 压缩揭示了"反例权重原则"

### 还没 close 的 open item

- [ ] 配图映射
- [ ] 开头场景虚构问题（humanizer 阶段核查）
- [ ] 字数 7,410 字符——如需瘦身可压缩第四章
- [ ] RapidDirect AI Creator Lab 引用未实测

---

## 2026-06-15 — v1.1.1 配图完成

### 做了什么

- assets/drafts/009/IMAGES.md：5 张图的章节映射表 + 渲染脚本路径
- 新增 2 张 Pillow 渲染卡：card-timeline.png + card-ai-architecture.png
- v2 修复（render_cards_v2.py）：标签缩短 / 文本溢出 / →→箭头替换 / em-dash 替换
- 已有 3 张图从 research 目录复制到 assets/drafts/009/
- 图片不被 git 追踪（.gitignore 已有规则）

### 配图映射

| 图 | 章节 | 插入时机 |
|---|---|---|
| xometry-logo.png | 头部 | 文章 header |
| card-timeline.png | 一 | 第一段数据密度最高处之后 |
| card-ai-architecture.png | 一 | "不是人工估价"段落后 |
| card-4company-comparison.png | 二 | 四种模式讲完后 |
| card-china-comparison.png | 三/四 | "三家全死"段落后或第四章末尾 |

### 学到什么

- vision_analyze 验证是关键——v1 版 3 处 bug 全部被 vision 抓到
- → 字符在 Pillow 默认字体里不可靠，用 "->" 代替
- Timeline 卡片文本长度约束比预想严格（1800px / 7 节点 ≈ 230px 每节点）

### 还没 close 的 open item

- [ ] 公众号排版时具体图片插入位置需微调
- [ ] render_cards 脚本目前在 ~/research/ 而非 repo 内——是否应提交到 china-ai-frontline？
- [ ] 开头场景虚构问题
- [ ] RapidDirect AI Creator Lab 未实测
