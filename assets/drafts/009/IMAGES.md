# IMAGES.md — drafts/009 配图

每张图对应 draft 的特定章节。5 张图全部自渲染（Pillow）+ 1 张品牌引用。

---

## 图片映射表

| 文件名 | 对应章节 | 画面内容 | 尺寸 | 渲染脚本 | License |
|---|---|---|---|---|---|
| `xometry-logo.png` | 文章头部 | Xometry 官方 logo | 600×auto | cairosvg 转 PNG | 品牌引用（非原创） |
| `card-timeline.png` | **一**：一个靠报价引擎上市的公司 | 2013→Q1 2026 七个关键节点 | 1800×700 | `render_cards_v2.py` | 原创 |
| `card-ai-architecture.png` | **一**：AI 引擎三层架构 | 客户侧报价 / 平台侧匹配 / 数据飞轮 | 1800×800 | `render_cards_v2.py` | 原创 |
| `card-4company-comparison.png` | **二**：四个玩家，三种活法 | Xometry / Protolabs / Fast Radius / Fictiv 四家对比 | 1800×1000 | `render_cards.py` | 原创 |
| `card-china-comparison.png` | **三**/**四**：中国玩家 + 结构性约束 | Xometry / JLCPCB Group / RapidDirect 三方对照 + Key Insight | 1600×850 | `render_cards.py` | 原创 |

---

## 章节配图逻辑

### 一：一个靠报价引擎上市的公司

- **先放 `card-timeline.png`**：给读者 12 年历史全景（2013 → Q1 2026），建立"这不是新公司，是跑通了的"的认知
- **再放 `card-ai-architecture.png`**：在数据密度最高段落后（"不是人工估价。不是查价格表"）插入，解释三层的具体机制

### 二：四个玩家，三种活法

- **放 `card-4company-comparison.png`**：在四种模式讲完后插入，作为视觉总结。四栏对齐，SCALING / MATURE / DEFUNCT / PRIVATE 的状态标签一目了然

### 三/四：中国不是没人做 + 三个结构性约束

- **放 `card-china-comparison.png`**：在第三章"三家全死"段落后或第四章末尾插入。三方对照 + Key Insight box 直接呼应核心论点

---

## 渲染脚本位置

```
~/research/xometry/sources/images/render_cards.py        # 4-company + China 对比
~/research/xometry/sources/images/render_cards_v2.py     # timeline + AI architecture
```

重新生成：
```bash
cd ~/research/xometry/sources/images && python3 render_cards.py && python3 render_cards_v2.py
cp *.png /home/zhang/china-ai-frontline/assets/drafts/009/
```

---

## 版本历史

- v1 (2026-06-15): emoji 渲染失败 → v2 修复
- v2 (2026-06-15): 新增 timeline + AI architecture，修复箭头 glyph + 文本溢出
